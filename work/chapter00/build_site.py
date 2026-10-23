import base64
import copy
import json
import re
import zipfile
from pathlib import Path
from PIL import Image

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[1]
OUT = ROOT / 'outputs'
SITE = OUT / 'chapter00-review'
IMAGES = SITE / 'images'
IMAGES.mkdir(parents=True, exist_ok=True)
template = (WORK / 'site-template.html').read_text(encoding='utf-8')
library = {'chapters': []}
for number in range(8):
    chapter_id = f'chapter{number:02d}'
    chapter_work = WORK.parent / chapter_id
    content_path = chapter_work / 'content.json'
    entry = {'id': chapter_id, 'number': number, 'data': None}
    if content_path.is_file():
        data = json.loads(content_path.read_text(encoding='utf-8'))
        chapter_images = IMAGES / chapter_id
        chapter_images.mkdir(exist_ok=True)
        for f in data['figures']:
            slide = next((chapter_work / name for name in (
                f"slide-{f['page']}.png",
                f"slide-{f['page']:02d}.png",
                f"slide-{f['page']:03d}.png",
            ) if (chapter_work / name).is_file()), None)
            if slide is None:
                raise FileNotFoundError(f"Missing figure source: {chapter_id} page {f['page']}")
            f['file'] = Path(f['file']).with_suffix('.webp').name
            target = chapter_images / f['file']
            if not target.is_file() or target.stat().st_mtime < slide.stat().st_mtime:
                Image.open(slide).save(target, format='WEBP', lossless=True, method=4)
            f['src'] = f"images/{chapter_id}/{f['file']}"
        for old_png in chapter_images.glob('*.png'):
            old_png.unlink()
        entry['data'] = data
    library['chapters'].append(entry)

def render(d):
    text = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return template.replace('__STUDY_DATA__', text)

(SITE / 'index.html').write_text(render(library), encoding='utf-8')
embedded = copy.deepcopy(library)
for entry in embedded['chapters']:
    if entry['data']:
        for f in entry['data']['figures']:
            f['src'] = 'data:image/webp;base64,' + base64.b64encode((SITE / f['src']).read_bytes()).decode('ascii')
(OUT / 'Chapter00-review.html').write_text(render(embedded), encoding='utf-8')
with zipfile.ZipFile(OUT / 'Chapter00-review.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(SITE / 'index.html', 'chapter00-review/index.html')
    for entry in library['chapters']:
        if entry['data']:
            for f in entry['data']['figures']:
                z.write(SITE / f['src'], Path('chapter00-review') / f['src'])

# Check portable asset references, data coverage, and JavaScript parse independently.
assert len(library['chapters']) == 8
for entry in library['chapters']:
    if entry['data']:
        data = entry['data']
        assert all(len(t['questions']) == 3 for t in data['topics'])
        assert all(t['pages'] and t['summary'] for t in data['topics'])
        assert all((SITE / f['src']).is_file() for f in data['figures'])
scripts = re.findall(r'<script>(.*?)</script>', template, re.S)
(WORK / 'client.js').write_text('\n'.join(scripts), encoding='utf-8')
print(f"Built {SITE / 'index.html'}")
print(f"Standalone: {(OUT / 'Chapter00-review.html').stat().st_size:,} bytes")
print(f"ZIP: {(OUT / 'Chapter00-review.zip').stat().st_size:,} bytes")
