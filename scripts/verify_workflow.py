"""Read-only structural/integrity check; not a live connector or model test."""
from pathlib import Path
import hashlib
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'Book Orchestrator Agent'
SOURCE_REVISION = '1512c022298eb542de5e3683b06727dba43294bd'
PACKAGES = {
    'broad-research-skill-v2': ('Broad-research-node/broad-research-agent', ['book-profile.md', 'output-formatting.md', 'writing-style.md']),
    'research-analysis-skill-v2': ('research-analysis-node/Research Analysis Agent', ['output-formatting.md']),
    'chapter-blueprint-5': ('Chapter-blueprint-node/Chapter Blueprint Agent', ['output-formatting.md', 'section-design-guide.md', 'structural-patterns.md']),
    'mapping-research-to-chapter-3-3': ('Research-mapping-node/mapping-research-to-chapter-3-3', ['output-formatting.md']),
    'deep-research-skill-3': ('Deep-research-node/deep-research-skill-3', ['output-formatting.md']),
    'anshul-chapter-writing-4': ('Chapter-writing-node/Chapter Writing Agent', ['anshul-voice.md', 'output-formatting.md', 'writing-style.md']),
    'evaluate-skill-v2': ('Broad-research-node/Evaluate', []),
    'diagnose-skill-v2': ('Broad-research-node/Diagnose', []),
}
NODES = ['broad_research', 'research_analysis', 'chapter_blueprint', 'research_mapping', 'deep_research', 'chapter_writing']

def require(condition, message):
    if not condition:
        raise SystemExit('FAIL: ' + message)

for name, (relative, refs) in PACKAGES.items():
    directory = BASE / relative
    text = (directory / 'SKILL.md').read_text()
    match = re.search(r'^name:\s*[\"\']?([^\n\"\']+)', text, re.M)
    require(match and match.group(1).strip() == name, 'frontmatter mismatch: ' + relative)
    require((directory / 'instruction.md').is_file(), 'missing worker instruction: ' + relative)
    require((directory.parent / 'instruction.md').is_file(), 'missing node instruction: ' + relative)
    for ref in refs:
        require((directory / 'references' / ref).is_file(), 'missing reference: ' + relative + '/' + ref)
    if name in ['evaluate-skill-v2', 'diagnose-skill-v2']:
        for rubric in ['README.md'] + [node + '.yaml' for node in NODES]:
            require((directory / 'references/rubrics' / rubric).is_file(), 'missing rubric: ' + rubric)
    print('PACKAGE OK:', name)

for relative in ['WORK_START.md', 'Book Orchestrator Agent/SKILL.md', 'Book Orchestrator Agent/references/codex-runtime.md']:
    require((ROOT / relative).is_file(), 'missing entry point: ' + relative)

# Compare every original node file with the production source commit.
# Git history must be retained; this intentionally does not accept an unverified ZIP.
try:
    listing = subprocess.check_output(['git', '-C', str(ROOT), 'ls-tree', '-r', '--name-only', SOURCE_REVISION], text=True)
except subprocess.CalledProcessError:
    raise SystemExit('FAIL: pinned source history unavailable; fetch the source revision before validation')
count = 0
for relative in listing.splitlines():
    if not relative.startswith('Book Orchestrator Agent/') or relative == 'Book Orchestrator Agent/instruction.md':
        continue
    original = subprocess.check_output(['git', '-C', str(ROOT), 'show', SOURCE_REVISION + ':' + relative])
    current = ROOT / relative
    require(current.is_file(), 'missing original file: ' + relative)
    require(hashlib.sha256(current.read_bytes()).digest() == hashlib.sha256(original).digest(), 'original stage file changed: ' + relative)
    count += 1
print('SOURCE INTEGRITY OK:', count, 'original node files unchanged')
print('OK: entry point, eight packages, six rubric names, references and source integrity verified')
print('NOT TESTED: receiving account authorization, models, HTML conversion, anchored comments or scheduler')
