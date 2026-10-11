"""Check a pinned native Google Doc against its approved presentation plan.

This verifies observable structure, not the literary quality of the prose.
"""
from __future__ import annotations

import argparse
import json
import re

PROFILE_ID = 'personal-agents-approved-v1'
BASELINE_DOCUMENT_ID = '1DFhe3Cnd0haepgIPSbJ6tT2L9gV4ilzmW2dsWvgpNrA'
BASELINE_REVISION_ID = 'AHj4eMShcsUIR1_7O_gd5ZRzjEyxGkKhb61ezsBTwzgqCNTelmC9Ye1uIvXxJ4ZuQD_uL2Y5wDIJMlbyJ8N_4GZkdFTfyl4Oh6jrvRxoS8g'
from pathlib import Path


def _paragraphs(document):
    def visit(content, styles=None):
        for item in content or []:
            if 'paragraph' in item:
                yield dict(item['paragraph'], _namedStyles=styles)
            if 'table' in item:
                for row in item['table'].get('tableRows', []):
                    for cell in row.get('tableCells', []):
                        yield from visit(cell.get('content'), styles)
            if 'tableOfContents' in item:
                yield from visit(item['tableOfContents'].get('content'), styles)
    if document.get('tabs'):
        def tabs(items):
            for tab in items:
                resource = tab.get('documentTab') or tab
                yield from visit(resource.get('body', {}).get('content'), resource.get('namedStyles') or tab.get('namedStyles') or document.get('namedStyles'))
                yield from tabs(tab.get('childTabs', []))
        return list(tabs(document['tabs']))
    return list(visit((document.get('body') or {}).get('content'), document.get('namedStyles')))


def _runs(paragraph):
    return [e['textRun'] for e in paragraph.get('elements', []) if 'textRun' in e]


def _text(paragraph):
    return ''.join(r.get('content', '') for r in _runs(paragraph)).strip()


def _approved_exception(plan, feature):
    # A worker-authored plan cannot grant itself an exception to this profile.
    return False


def _effective_text_style(paragraph, run):
    named = paragraph.get('_namedStyles') or {}
    values = named.get('styles', []) if isinstance(named, dict) else named
    styles = {value.get('namedStyleType'): value.get('textStyle', {}) for value in values}
    result = dict(styles.get('NORMAL_TEXT', {}))
    result.update(styles.get(paragraph.get('paragraphStyle', {}).get('namedStyleType'), {}))
    result.update(run.get('textStyle', {}))
    return result


def _is_black(rgb):
    return isinstance(rgb, dict) and all(rgb.get(key, 0) == 0 for key in ("red", "green", "blue"))


def _has_emoji(value):
    return any(0x1F000 <= ord(char) <= 0x1FAFF or 0x2600 <= ord(char) <= 0x27BF for char in value)


def validate(document: dict, plan: dict) -> dict:
    """Return a passing audit report; raise ValueError with all failures otherwise.

    Plan schema: document_id, revision_id, profile_id, baseline_document_id,
    baseline_revision_id, optional title, and nonempty icons, opening_emphasis, explanatory_list,
    headings arrays. Citation policy requires anchors (possibly empty, explicitly
    decided) and allowed_inline_links (possibly empty). Every expectation uses
    a zero-based paragraph index in the chapter, ending before the heading
    'Chapter Writing Notes'. This production profile does not allow self-approved exceptions.
    """
    errors = []
    for field, actual in [('document_id', document.get('documentId')),
                          ('revision_id', document.get('revisionId'))]:
        if not actual or plan.get(field) != actual:
            errors.append(f'{field} missing or does not match native document')
    for field in ('profile_id', 'baseline_document_id', 'baseline_revision_id'):
        if not isinstance(plan.get(field), str) or not plan[field].strip():
            errors.append(f'{field} missing from pinned plan')
    for field in ('icons', 'opening_emphasis', 'explanatory_list', 'headings'):
        if not isinstance(plan.get(field), list) or (not plan[field] and not _approved_exception(plan, field)):
            errors.append(f'{field} has no explicit opportunities or approved exception')
    citation = plan.get('citation_policy')
    if not isinstance(citation, dict) or not isinstance(citation.get('anchors'), list) or not isinstance(citation.get('allowed_inline_links'), list):
        errors.append('citation_policy requires explicit anchors and allowed_inline_links decisions')
        citation = {'anchors': [], 'allowed_inline_links': []}
    for field, expected in [('profile_id', PROFILE_ID), ('baseline_document_id', BASELINE_DOCUMENT_ID), ('baseline_revision_id', BASELINE_REVISION_ID)]:
        if plan.get(field) != expected:
            errors.append(f'{field} differs from approved production profile')
    paragraphs = _paragraphs(document)
    if not paragraphs:
        errors.append('native document paragraphs unavailable')
    cutoff = next((i for i, p in enumerate(paragraphs) if _text(p).casefold() == 'chapter writing notes'), len(paragraphs))
    chapter = paragraphs[:cutoff]
    if not chapter:
        errors.append('chapter content unavailable before Chapter Writing Notes')

    def at(entry, kind):
        if not isinstance(entry, dict) or type(entry.get('paragraph_index')) is not int:
            errors.append(f'{kind}: missing paragraph_index')
            return None
        index = entry['paragraph_index']
        if not 0 <= index < len(chapter):
            errors.append(f'{kind}: paragraph {index} outside chapter')
            return None
        return chapter[index]

    title_entry = plan.get('title')
    title_index = title_entry.get('paragraph_index') if isinstance(title_entry, dict) else None
    if title_entry is not None:
        p = at(title_entry, 'title')
        if p is not None:
            if p.get('paragraphStyle', {}).get('namedStyleType') != 'TITLE':
                errors.append('chapter title must use native TITLE style')
            if _text(p) != title_entry.get('text'):
                errors.append('title text differs from plan')
            for run in _runs(p):
                if run.get('content', '').strip():
                    style = _effective_text_style(p, run)
                    if (style.get('fontSize', {}).get('magnitude') != 26 or
                        (style.get('weightedFontFamily', {}).get('fontFamily') or style.get('fontFamily')) != 'Georgia' or
                        not _is_black(style.get('foregroundColor', {}).get('color', {}).get('rgbColor'))):
                        errors.append(f'title typography differs from approved Georgia 26pt black at paragraph {title_index}')
    actual_headings = [(i, _text(p), p.get('paragraphStyle', {}).get('namedStyleType'))
                       for i, p in enumerate(chapter)
                       if i != title_index and re.fullmatch(r'HEADING_[1-6]', str(p.get('paragraphStyle', {}).get('namedStyleType', '')))]
    expected_headings = []
    for entry in plan.get('headings', []):
        p = at(entry, 'heading')
        if p is None:
            continue
        title = entry.get('title')
        style = entry.get('level')
        if not isinstance(title, str) or not title or _text(p) != title or p.get('paragraphStyle', {}).get('namedStyleType') != style or not re.fullmatch(r'HEADING_[1-6]', str(style)):
            errors.append(f'heading: expected exact title and named style at paragraph {entry["paragraph_index"]}')
        expected_headings.append((entry['paragraph_index'], title, style))
    for i, title, level in actual_headings:
        expected_size = 17 if level == 'HEADING_1' else 13
        for run in _runs(chapter[i]):
            if not run.get('content', '').strip():
                continue
            style = _effective_text_style(chapter[i], run)
            size = style.get('fontSize', {}).get('magnitude')
            family = style.get('weightedFontFamily', {}).get('fontFamily') or style.get('fontFamily')
            rgb = style.get('foregroundColor', {}).get('color', {}).get('rgbColor')
            if size != expected_size or family != 'Georgia' or not _is_black(rgb):
                errors.append(f'heading typography differs from approved Georgia {expected_size}pt black at paragraph {i}')
    if actual_headings != expected_headings:
        errors.append('actual heading sequence differs from approved presentation plan')
    main_number = 0
    for i, title, level in actual_headings:
        if level == 'HEADING_1':
            main_number += 1
            if not re.match(r'^' + str(main_number) + r'\.\s+', title):
                errors.append(f'main heading numbering must be sequential at paragraph {i}')
        if '[TECH]' in title or '[WOW MOMENT]' in title:
            errors.append(f'internal commitment marker in reader heading at paragraph {i}')
        if level != 'HEADING_1' and (level != 'HEADING_2' or re.match(r'^\s*\d+(?:\.\d+)*[.)]?\s+', title)):
            errors.append(f'unapproved subsection numbering or heading level at paragraph {i}')
    for entry in plan.get('icons', []):
        p = at(entry, 'icon')
        if p is None:
            continue
        symbol = entry.get('symbol')
        if (not isinstance(symbol, str) or not _has_emoji(symbol) or
            not (_text(p).startswith(symbol) or re.match(r'^\d+\.\s+' + re.escape(symbol) + r'\s+', _text(p)))):
            errors.append(f'icon missing at paragraph {entry["paragraph_index"]}')
        if entry.get('location') != 'heading':
            errors.append('production profile requires icons in headings')
        if entry.get('location') == 'heading' and not re.fullmatch(r'HEADING_[1-6]', str(p.get('paragraphStyle', {}).get('namedStyleType', ''))):
            errors.append(f'icon location is not a heading at paragraph {entry["paragraph_index"]}')
    for entry in plan.get('opening_emphasis', []):
        p = at(entry, 'opening emphasis')
        if p is None:
            continue
        if p.get('bullet') or re.fullmatch(r'HEADING_[1-6]', str(p.get('paragraphStyle', {}).get('namedStyleType', ''))):
            errors.append(f'opening emphasis must be body prose at paragraph {entry["paragraph_index"]}')
        lead = entry.get('text')
        if not isinstance(lead, str) or not lead.strip() or not _text(p).startswith(lead):
            errors.append(f'opening emphasis lead missing at paragraph {entry["paragraph_index"]}')
            continue
        remaining = len(lead)
        for run in _runs(p):
            content = run.get('content', '')
            if not remaining:
                break
            span = min(len(content), remaining)
            if content[:span].strip() and run.get('textStyle', {}).get('bold') is not True:
                errors.append(f'opening emphasis not bold at paragraph {entry["paragraph_index"]}')
                break
            remaining -= span
    for entry in plan.get('explanatory_list', []):
        p = at(entry, 'explanatory list')
        if p is None:
            continue
        lead = entry.get('lead_in')
        expected = entry.get('text')
        if 'bullet' not in p or not isinstance(expected, str) or not expected.strip() or _text(p) != expected or not isinstance(lead, str) or not lead.strip() or not expected.startswith(lead) or len(expected.strip()) <= len(lead.strip()):
            errors.append(f'explanatory list item missing or lacks explanation at paragraph {entry["paragraph_index"]}')
            continue
        remaining = len(lead)
        for run in _runs(p):
            if not remaining:
                break
            span = min(len(run.get('content', '')), remaining)
            if run.get('content', '')[:span].strip() and run.get('textStyle', {}).get('bold') is not True:
                errors.append(f'explanatory list lead-in not bold at paragraph {entry["paragraph_index"]}')
                break
            remaining -= span
    actual_links = []
    for i, p in enumerate(chapter):
        for run in _runs(p):
            url = run.get('textStyle', {}).get('link', {}).get('url')
            if url:
                actual_links.append({'paragraph_index': i, 'text': run.get('content', '').strip(), 'url': url})
    allowed = citation['allowed_inline_links']
    if allowed:
        errors.append('production profile disallows inline citation links in chapter body')
    for link in allowed:
        if link not in actual_links:
            errors.append(f'approved inline link missing: {link}')
    for link in actual_links:
        if link not in allowed:
            errors.append(f'unapproved inline link: {link}')
    notes_text = '\n'.join(_text(p) for p in paragraphs[cutoff:])
    notes_urls = {r.get('textStyle', {}).get('link', {}).get('url') for p in paragraphs[cutoff:] for r in _runs(p)}
    for anchor in citation['anchors']:
        p = at(anchor, 'citation anchor')
        if p is not None and (not isinstance(anchor.get('text'), str) or anchor['text'] not in _text(p)):
            errors.append(f'citation anchor missing at paragraph {anchor["paragraph_index"]}')
        source_url = anchor.get('source_url')
        if not isinstance(source_url, str) or not source_url.startswith(('https://', 'http://')) or (source_url not in notes_text and source_url not in notes_urls):
            errors.append(f'citation source URL missing from Handoff after Notes: {source_url}')
    if errors:
        raise ValueError('; '.join(errors))
    return {'valid': True, 'document_id': document['documentId'], 'revision_id': document['revisionId'], 'chapter_paragraphs': len(chapter), 'checked': {key: len(plan[key]) for key in ('headings', 'icons', 'opening_emphasis', 'explanatory_list')}, 'inline_links': len(actual_links)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('document_json', type=Path)
    parser.add_argument('presentation_plan_json', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(validate(json.loads(args.document_json.read_text()), json.loads(args.presentation_plan_json.read_text())), indent=2))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(2, f'INVALID: {exc}\n')


if __name__ == '__main__':
    main()
