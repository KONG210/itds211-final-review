import json
from pathlib import Path

from pypdf import PdfReader

source = Path(r'C:\Users\kongk\Downloads\ITDS211_Computer Architecture and Operating Systems\itds-211_comp_arch_Chapter06.pdf')
dest = Path(__file__).resolve().parent
pages = [{'page': i + 1, 'text': page.extract_text() or ''} for i, page in enumerate(PdfReader(str(source)).pages)]
(dest / 'pages.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2), encoding='utf-8')
(dest / 'text.txt').write_text(''.join(f"\n\n===== PAGE {item['page']} =====\n{item['text']}" for item in pages), encoding='utf-8')
print(len(pages), sum(len(item['text']) for item in pages))



