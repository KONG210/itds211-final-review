import json
import re
import zipfile
from pathlib import Path

out = Path(__file__).resolve().parents[2] / 'outputs'
html = (out / 'Chapter00-review.html').read_text(encoding='utf-8')
raw = re.search(r'<script id="study-data" type="application/json">(.*?)</script>', html, re.S).group(1)
library = json.loads(raw)
assert len(library['chapters']) == 9
available=[c for c in library['chapters'] if c['data']]
assert len(available)==9
chapter03 = next(c['data'] for c in available if c['id'] == 'chapter03')
assert len(chapter03['topics']) == 30
assert len(chapter03['figures']) == 99
assert len(chapter03['flashcards']) == 60
assert all(len(t['questions']) == 3 for t in chapter03['topics'])
assert all(chapter03['source'] in f['caption'] and 'หน้า' in f['caption'] for f in chapter03['figures'])
chapter04 = next(c['data'] for c in available if c['id'] == 'chapter04')
assert len(chapter04['topics']) == 30
assert len(chapter04['figures']) == 108
assert len(chapter04['flashcards']) == 54
assert all(len(t['questions']) == 3 for t in chapter04['topics'])
assert all(chapter04['source'] in f['caption'] and 'หน้า' in f['caption'] for f in chapter04['figures'])
chapter05 = next(c['data'] for c in available if c['id'] == 'chapter05')
assert len(chapter05['topics']) == 23
assert len(chapter05['figures']) == 48
assert len(chapter05['flashcards']) == 46
assert all(len(t['questions']) == 3 for t in chapter05['topics'])
assert all(chapter05['source'] in f['caption'] and 'หน้า' in f['caption'] for f in chapter05['figures'])
chapter06 = next(c['data'] for c in available if c['id'] == 'chapter06')
assert len(chapter06['topics']) == 22
assert len(chapter06['figures']) == 40
assert len(chapter06['flashcards']) == 41
assert all(len(t['questions']) == 3 for t in chapter06['topics'])
assert all(chapter06['source'] in f['caption'] and 'หน้า' in f['caption'] for f in chapter06['figures'])
chapter07 = next(c['data'] for c in available if c['id'] == 'chapter07')
assert len(chapter07['topics']) == 25
assert len(chapter07['figures']) == 36
assert len(chapter07['flashcards']) == 43
assert all(len(t['questions']) == 3 for t in chapter07['topics'])
assert all(chapter07['source'] in f['caption'] and 'หน้า' in f['caption'] for f in chapter07['figures'])
chapter08 = next(c['data'] for c in available if c['id'] == 'chapter08')
assert len(chapter08['topics']) == 29
assert len(chapter08['figures']) == 17
assert len(chapter08['flashcards']) == 48
assert all(len(t['questions']) == 3 for t in chapter08['topics'])
assert all(chapter08['source'] in f['caption'] and 'หน้า' in f['caption'] for f in chapter08['figures'])
assert 'id="chapter-side"' in html and 'id="side-topics"' in html and 'id="side-chapters"' in html
assert all(f['src'].startswith('data:image/webp;base64,') for c in available for f in c['data']['figures'])
assert not re.search(r'<script[^>]+src=|@import|https?://', html)
with zipfile.ZipFile(out / 'Chapter00-review.zip') as z:
    assert z.testzip() is None
    assert len([n for n in z.namelist() if '/images/' in n]) == sum(len(c['data']['figures']) for c in available)
with zipfile.ZipFile(out / 'final-exam-review-site.zip') as z:
    skill = z.read('final-exam-review-site/SKILL.md').decode('utf-8')
    assert 'บทนี้เรียนเพื่ออะไร' in skill and 'จุดประสงค์ของบทนี้' in skill
print('Standalone embedded assets / no external dependencies / ZIP integrity / updated skill package: PASS')
