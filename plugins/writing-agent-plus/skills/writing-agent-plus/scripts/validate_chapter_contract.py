"""Verify pinned writing dependencies and pipeline ownership before dispatch."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

WORKER = Path('Book Orchestrator Agent/Chapter-writing-node/Chapter Writing Agent')
PLUGIN = Path('plugins/writing-agent-plus/skills/writing-agent-plus')
CHECKS = ['references_verified', 'story_architecture', 'write_format_humanize',
          'story_integrity', 'formatted_document_verified']

def validate(root: Path) -> None:
    worker = root / WORKER
    manifest = json.loads((worker / 'references/skill-sources.json').read_text())
    if manifest.get('contract_version') != 1:
        raise ValueError('Unsupported chapter writing contract')
    deps = manifest.get('dependencies', [])
    names = [d.get('name') for d in deps]
    if names != ['storytelling-article', 'anshul-writing-style', 'ai-humanizer-core']:
        raise ValueError('Missing, duplicate or misordered writing dependencies')
    for dep in deps:
        path = worker / dep['path']
        if not path.resolve().is_relative_to(worker.resolve()):
            raise ValueError('Dependency escapes worker package')
        data = path.read_bytes()
        git_sha = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if hashlib.sha256(data).hexdigest() != dep['sha256'] or git_sha != dep['source_blob_sha']:
            raise ValueError('Dependency integrity mismatch: ' + dep['name'])
    for name in ['anshul-voice.md', 'writing-style.md', 'output-formatting.md']:
        if not (worker / 'references' / name).is_file():
            raise ValueError('Missing inner reference: ' + name)
    config = json.loads((root / PLUGIN / 'pipeline.json').read_text())
    contract = config.get('chapter_writing_contract', {})
    if contract.get('version') != 1 or contract.get('required_checks') != CHECKS:
        raise ValueError('Pipeline execution checks do not match worker contract')
    if contract.get('worker_steps') != CHECKS[1:]:
        raise ValueError('Pipeline writing steps are missing or misordered')
    if contract.get('visual_placement_rewrites_prose') is not False:
        raise ValueError('Visual Placement must preserve completed prose')
    if config.get('chapter_writing_subflow') != ['canonical_chapter_worker', 'canonical_clean_evaluate', 'visual_placement_linkedin', 'final_clean_evaluate']:
        raise ValueError('Unexpected Chapter Writing role order')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('production_root', type=Path)
    args = parser.parse_args()
    try:
        validate(args.production_root)
    except (OSError, KeyError, ValueError) as exc:
        parser.exit(2, 'INVALID: ' + str(exc) + '\n')
    print('VALID: integrated chapter dependencies, inner references and routing')
