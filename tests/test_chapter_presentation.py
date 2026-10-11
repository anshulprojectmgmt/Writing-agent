import copy
import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / 'plugins/writing-agent-plus/skills/writing-agent-plus/scripts/validate_chapter_presentation.py'
spec = importlib.util.spec_from_file_location('chapter_presentation', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def para(text, *, level='NORMAL_TEXT', bold_lead='', bullet=False, link=None):
    if bold_lead:
        elements = [{'textRun': {'content': bold_lead, 'textStyle': {'bold': True}}}, {'textRun': {'content': text[len(bold_lead):]}}]
    else:
        elements = [{'textRun': {'content': text}}]
    if level.startswith('HEADING_'):
        for element in elements:
            element['textRun'].setdefault('textStyle', {}).update({
                'weightedFontFamily': {'fontFamily': 'Georgia'},
                'fontSize': {'magnitude': 17 if level == 'HEADING_1' else 13, 'unit': 'PT'},
                'foregroundColor': {'color': {'rgbColor': {'red': 0, 'green': 0, 'blue': 0}}}})
    if link:
        elements[0]['textRun']['textStyle'] = {'link': {'url': link}}
    result = {'paragraphStyle': {'namedStyleType': level}, 'elements': elements}
    if bullet:
        result['bullet'] = {'listId': 'list-1'}
    return {'paragraph': result}


def fixture():
    content = [para('1. 🧭 The agent changes the work', level='HEADING_1'),
               para('The key shift arrives when work moves.', bold_lead='The key shift'),
               para('Trust: Explain what the agent may do.', bold_lead='Trust:', bullet=True),
               para('A specific sourced example appears here.'),
               para('Chapter Writing Notes', level='HEADING_1'),
               para('https://source.example', link='https://source.example')]
    doc = {'documentId': 'new-doc', 'revisionId': 'rev-2', 'body': {'content': content}}
    plan = {'document_id': 'new-doc', 'revision_id': 'rev-2',
            'profile_id': module.PROFILE_ID, 'baseline_document_id': module.BASELINE_DOCUMENT_ID,
            'baseline_revision_id': module.BASELINE_REVISION_ID,
            'headings': [{'paragraph_index': 0, 'title': '1. 🧭 The agent changes the work', 'level': 'HEADING_1'}],
            'icons': [{'paragraph_index': 0, 'symbol': '1. 🧭', 'location': 'heading'}],
            'opening_emphasis': [{'paragraph_index': 1, 'text': 'The key shift'}],
            'explanatory_list': [{'paragraph_index': 2, 'lead_in': 'Trust:', 'text': 'Trust: Explain what the agent may do.'}],
            'citation_policy': {'anchors': [{'paragraph_index': 3, 'text': 'sourced example', 'source_url': 'https://source.example'}], 'allowed_inline_links': []}}
    return doc, plan


def test_valid_body_and_flattened_tabs():
    doc, plan = fixture()
    assert module.validate(doc, plan)['valid']
    tabbed = {'documentId': doc['documentId'], 'revisionId': doc['revisionId'],
              'tabs': [{'documentTab': {'body': doc['body']}}]}
    assert module.validate(tabbed, plan)['chapter_paragraphs'] == 4
    flattened = {'documentId': doc['documentId'], 'revisionId': doc['revisionId'], 'body': None,
                 'tabs': [{'tabId': 't.0', 'body': doc['body']}]}
    assert module.validate(flattened, plan)['chapter_paragraphs'] == 4


def test_zero_icons_and_openings_fails_even_with_midparagraph_bold():
    doc, plan = fixture()
    plan['icons'] = []
    plan['opening_emphasis'] = []
    doc['body']['content'][1] = para('The key shift arrives when work moves.')
    doc['body']['content'][1]['paragraph']['elements'].append({'textRun': {'content': ' strong aside', 'textStyle': {'bold': True}}})
    with pytest.raises(ValueError, match='icons has no explicit|opening_emphasis has no explicit'):
        module.validate(doc, plan)


def test_missing_icon_or_bold_opening_or_list_lead():
    for index, replacement, match in [
        (0, para('1. The agent changes the work', level='HEADING_1'), 'icon missing'),
        (1, para('The key shift arrives when work moves.'), 'opening emphasis not bold'),
        (2, para('Trust: Explain what the agent may do.', bullet=True), 'lead-in not bold'),
        (2, para('Trust:', bold_lead='Trust:', bullet=True), 'lacks explanation')]:
        doc, plan = fixture()
        doc['body']['content'][index] = replacement
        with pytest.raises(ValueError, match=match):
            module.validate(doc, plan)


def test_unplanned_hierarchical_heading_and_inline_link_fail():
    doc, plan = fixture()
    doc['body']['content'].insert(3, para('3.1 New section', level='HEADING_2'))
    with pytest.raises(ValueError, match='unapproved subsection numbering'):
        module.validate(doc, plan)
    doc, plan = fixture()
    doc['body']['content'][3] = para('A specific sourced example appears here.', link='https://source.example')
    with pytest.raises(ValueError, match='unapproved inline link'):
        module.validate(doc, plan)


def test_stale_plan_and_missing_audit_fail():
    doc, plan = fixture()
    plan['revision_id'] = 'old'
    with pytest.raises(ValueError, match='revision_id missing or does not match'):
        module.validate(doc, plan)
    doc, plan = fixture()
    plan.pop('citation_policy')
    with pytest.raises(ValueError, match='citation_policy requires'):
        module.validate(doc, plan)
    doc, plan = fixture()
    plan['profile_id'] = 'invented-profile'
    with pytest.raises(ValueError, match='approved production profile'):
        module.validate(doc, plan)


def test_source_url_must_survive_in_notes():
    doc, plan = fixture()
    doc['body']['content'][-1] = para('Citation table omitted the source URL')
    with pytest.raises(ValueError, match='source URL missing'):
        module.validate(doc, plan)


def test_plan_cannot_self_approve_empty_features_or_fake_icon():
    doc, plan = fixture()
    plan['icons'] = []
    plan['exceptions'] = {'icons': {'author_approved': True, 'reason': 'No opportunity'}}
    with pytest.raises(ValueError, match='icons has no explicit'):
        module.validate(doc, plan)
    doc, plan = fixture()
    plan['icons'][0]['symbol'] = '1.'
    with pytest.raises(ValueError, match='icon missing'):
        module.validate(doc, plan)


def test_opening_emphasis_cannot_be_heading_or_bullet():
    doc, plan = fixture()
    plan['opening_emphasis'][0] = {'paragraph_index': 0, 'text': '1. 🧭'}
    with pytest.raises(ValueError, match='must be body prose'):
        module.validate(doc, plan)


def test_heading_typography_must_match_profile():
    doc, plan = fixture()
    doc['body']['content'][0]['paragraph']['elements'][0]['textRun']['textStyle']['fontSize']['magnitude'] = 18
    with pytest.raises(ValueError, match='heading typography differs'):
        module.validate(doc, plan)


def test_native_black_can_omit_zero_rgb_components():
    doc, plan = fixture()
    doc['body']['content'][0]['paragraph']['elements'][0]['textRun']['textStyle']['foregroundColor']['color']['rgbColor'] = {}
    assert module.validate(doc, plan)['valid']


def test_main_numbering_cannot_be_overridden_by_plan():
    doc, plan = fixture()
    doc['body']['content'][0]['paragraph']['elements'][0]['textRun']['content'] = '3. 🧭 The agent changes the work'
    plan['headings'][0]['title'] = '3. 🧭 The agent changes the work'
    plan['icons'][0]['symbol'] = '3. 🧭'
    with pytest.raises(ValueError, match='main heading numbering'):
        module.validate(doc, plan)
