from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent
paths = sorted(root.glob('page-*.png'))
for start in range(0, len(paths), 8):
    sheet = Image.new('RGB', (1600, 1000), 'white')
    draw = ImageDraw.Draw(sheet)
    for offset, path in enumerate(paths[start:start+8]):
        im = Image.open(path).convert('RGB')
        im.thumbnail((390, 220))
        x, y = (offset % 4) * 400, (offset // 4) * 500
        sheet.paste(im, (x, y+25))
        draw.text((x+10, y+5), path.stem, fill='black')
    sheet.save(root / f'contact-{start//8+1}.png')
print(len(paths))
