import json
import sys
from pathlib import Path

start, end = map(int, sys.argv[1:3])
pages = json.loads((Path(__file__).parent / 'pages.json').read_text(encoding='utf-8'))
for item in pages[start - 1:end]:
    print(f"\n===== PDF PAGE {item['page']} =====")
    print(item['text'])
