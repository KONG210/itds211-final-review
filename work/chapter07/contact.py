import sys
from pathlib import Path
from PIL import Image, ImageDraw
root = Path(sys.argv[1])
paths = sorted(root.glob('slide-*.png'))
for start in range(0, len(paths), 6):
    sheet = Image.new('RGB', (1600, 1380), 'white')
    d = ImageDraw.Draw(sheet)
    for k, p in enumerate(paths[start:start+6]):
        im = Image.open(p).convert('RGB'); im.thumbnail((795, 440))
        x, y = (k % 2) * 805, (k // 2) * 460
        sheet.paste(im, (x, y+18)); d.text((x+6, y+3), p.stem, fill='red')
    sheet.save(root / f'contact-{start//6+1}.png')
print(len(paths))
