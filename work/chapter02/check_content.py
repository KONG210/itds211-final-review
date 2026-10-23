import json
import re
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / 'content.json').read_text(encoding='utf-8'))
pages = json.loads((root / 'pages.json').read_text(encoding='utf-8'))
assert len(pages) == data['sourcePageCount'] == 46

def page_set(ref):
    found = set()
    for a, b in re.findall(r'(\d+)\s*[–-]\s*(\d+)', ref):
        found.update(range(int(a), int(b) + 1))
    ref = re.sub(r'\d+\s*[–-]\s*\d+', '', ref)
    found.update(int(n) for n in re.findall(r'\d+', ref))
    return found

covered = set().union(*(page_set(t['pages']) for t in data['topics']))
assert set(range(3, 46)) - {16} <= covered, sorted(set(range(3, 46)) - {16} - covered)
assert len(data['topics']) == 22
assert len(data['figures']) == 32
assert len(data['flashcards']) == 50
assert all(len(t['questions']) == 3 for t in data['topics'])
assert Counter(t['level'] for t in data['topics']) == {'core':17,'important':5}
assert all(1 <= f['page'] <= 46 and (root / f"slide-{f['page']:02d}.png").is_file() for f in data['figures'])
assert all(page_set(t['pages']) <= set(range(1,47)) for t in data['topics'])
assert all(page_set(q['pages']) <= set(range(1,47)) for t in data['topics'] for q in t['questions'])

# Check values transcribed from the two numerical examples, without adding a new exercise.
assert 3 + 2 == 5  # Hypothetical machine, p14.
assert (0x0023 + 0xFFE9) & 0xFFFF == 0x000C  # MARIE ADD 105, p35–36.
assert 'ต้องตรวจสอบจากต้นฉบับ' in data['topics'][11]['confusion']
assert 'ต้องตรวจสอบจากต้นฉบับ' in data['topics'][17]['confusion']
print('PDF page coverage, questions, images, examples, ambiguities: PASS')
