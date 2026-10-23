import json
from pathlib import Path

pages = json.loads((Path(__file__).parent / 'pages.json').read_text(encoding='utf-8'))
for page in pages:
    excerpt = ' | '.join(line.strip() for line in page['text'].splitlines() if line.strip())
    print(f"{page['page']:3}: {excerpt[:220]}")
