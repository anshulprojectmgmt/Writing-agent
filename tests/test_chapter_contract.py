from pathlib import Path
import importlib.util
import json
import shutil

import pytest

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / 'plugins/writing-agent-plus/skills/writing-agent-plus/scripts/validate_chapter_contract.py'
spec = importlib.util.spec_from_file_location('chapter_contract', SCRIPT)
contract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contract)

def copy_contract(tmp_path):
    for directory in [contract.WORKER, contract.PLUGIN, contract.VISUAL]:
        shutil.copytree(ROOT / directory, tmp_path / directory)
    return tmp_path

def test_pinned_production_dependencies_and_routing():
    contract.validate(ROOT)

def test_missing_image_only_contract_blocks_dispatch(tmp_path):
    root = copy_contract(tmp_path)
    (root / contract.VISUAL / 'references/placement-contract.md').unlink()
    with pytest.raises(ValueError, match='Missing image-only placement contract'):
        contract.validate(root)

@pytest.mark.parametrize('name', ['storytelling-article', 'anshul-writing-style', 'ai-humanizer-core'])
def test_modified_dependency_blocks_dispatch(tmp_path, name):
    root = copy_contract(tmp_path)
    path = root / contract.WORKER / 'references' / (name + '.md')
    path.write_text(path.read_text() + '\nChanged instruction\n')
    with pytest.raises(ValueError, match='integrity mismatch'):
        contract.validate(root)

def test_missing_inner_reference_blocks_dispatch(tmp_path):
    root = copy_contract(tmp_path)
    (root / contract.WORKER / 'references/output-formatting.md').unlink()
    with pytest.raises(ValueError, match='Missing inner reference'):
        contract.validate(root)

def test_visual_rewrite_or_misordered_steps_blocks_dispatch(tmp_path):
    root = copy_contract(tmp_path)
    path = root / contract.PLUGIN / 'pipeline.json'
    original = json.loads(path.read_text())
    for change in ['rewrite', 'order']:
        value = json.loads(json.dumps(original))
        if change == 'rewrite':
            value['chapter_writing_contract']['visual_placement_rewrites_prose'] = True
        else:
            value['chapter_writing_contract']['worker_steps'].reverse()
        path.write_text(json.dumps(value))
        with pytest.raises(ValueError):
            contract.validate(root)
