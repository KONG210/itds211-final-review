import sys
from pathlib import Path
import pypdfium2 as pdfium

src, dest = Path(sys.argv[1]), Path(sys.argv[2])
pdf = pdfium.PdfDocument(str(src))
for i, page in enumerate(pdf, 1):
    page.render(scale=1600 / page.get_width()).to_pil().save(dest / f'slide-{i:02d}.png')
print(len(pdf))

