import json
import argparse
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--chapter',default='00')
chapter_number=int(parser.parse_args().chapter)
chapter_label=f'Chapter{chapter_number:02d}'
DATA = json.loads((Path(__file__).parent.parent / f'chapter{chapter_number:02d}' / 'content.json').read_text(encoding='utf-8'))
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)
labels = {'core': '🔴 ต้องจำแน่นอน', 'important': '🟡 สำคัญ', 'extra': '⚪ อ่านเสริม'}
src = DATA['source']
counts=Counter(t['level'] for t in DATA['topics'])
questions=[q for t in DATA['topics'] for q in t['questions']]
question_types=Counter(q['type'] for q in questions)
stats=' · '.join(f"{labels[k]} {counts[k]} หัวข้อ ({counts[k]/len(DATA['topics'])*100:.1f}%)" for k in labels)
lines = [f"# {DATA['chapter']}", '', f"{DATA['course']} · {DATA['instructor']}", '',
         f"แหล่งข้อมูลของบท: **{src}** จำนวน {DATA.get('sourcePageCount',9)} หน้า อ่านและตรวจภาพครบทุกหน้า", '',
         f"ขอบเขตงาน: {chapter_label} ทั้งหมด · รูปแบบฝึก: {'/'.join(question_types)} · เวลาทบทวน: ไม่จำกัด", '',
         '## 1. ภาพรวมเนื้อหาและระดับความสำคัญ', '',
         f"1 บท · {len(DATA['topics'])} หัวข้อ · {stats} · แบบฝึก {len(questions)} ข้อ · Flashcard {len(DATA['flashcards'])} ใบ", '',
         f"**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน {chapter_label} ไม่ยืนยันความถี่หรือโอกาสออก Final**", '',
         '| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |', '| --- | --- | --- |']
for t in DATA['topics']:
    lines.append(f"| {t['title']} | {labels[t['level']]} | {src}, {t['pages']} |")
lines += ['', '### บทนี้เรียนเพื่ออะไร', '', DATA['purpose'], '',
          f"อ้างอิง: {src}, {DATA['purposePages']}", '',
          '### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา', '']
for g in DATA['goals']:
    lines.append(f"- {g['text']} ({src}, {g['pages']})")
lines += ['', DATA.get('objectiveNote','วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ'), '', '### ขอบเขตและข้อมูลที่ต้องตรวจสอบ', '']
lines += ['- ' + x for x in DATA['limits']]
lines += ['', '## 2. สรุปรายบทและหัวข้อ', '']
for i,t in enumerate(DATA['topics'],1):
    lines += [f"### {i}. {t['title']}", '', f"**{labels[t['level']]}** · {src}, **{t['pages']}**", '',
              f"เหตุผลการจัดระดับ: {t['reason']}", '', t['summary'], '', '**ประเด็นที่ต้องจำ**', '']
    lines += ['- '+x for x in t['remember']]
    lines += ['', '**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**', '']
    lines += ['- '+x for x in t['terms']]
    lines += ['', '**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** '+t['example'], '']
    for formula in t.get('formulas',[]):
        lines += ['**สูตรที่ต้องรู้**', '', '```text',formula['expr'],'```', '', formula['description'], '', f"อ้างอิง: {src}, {formula['pages']}", '']
    for work in t.get('worked',[]):
        lines += ['**'+work['title']+'**', '']
        lines += [f"{j}. {step}" for j,step in enumerate(work['steps'],1)]
        lines += ['', '**คำตอบ:** '+work['answer'], '', f"อ้างอิง: {src}, {work['pages']}", '']
    if 'comparison' in t:
        c=t['comparison']
        lines += ['| '+' | '.join(c['headers'])+' |', '| '+' | '.join(['---']*len(c['headers']))+' |']
        lines += ['| '+' | '.join(row)+' |' for row in c['rows']]
        lines += ['']
    lines += ['**จุดที่อาจสับสน:** '+t['confusion'], '', '**ประโยคช่วยจำ:** '+t['mnemonic'], '']
lines += ['## 3. Roadmap ทบทวน', '']
for i,s in enumerate(DATA['roadmap'],1):
    lines += [f"{i}. **{s['title']}** — {s['text']} ({src}, {s['pages']})"]
lines += ['', '## 4. แผนทบทวนตามเวลา', '',
          'ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ', '']
for p in DATA['plan']:
    lines += [f"### {p['title']}", '', p['task'], '', '**เกณฑ์ผ่าน:** '+p['check'], '', f"อ้างอิง: {src}, {p['pages']}", '']
lines += ['### ตัวเลือกเมื่อเวลาน้อย', '']
for p in DATA['cram']:
    lines += [f"- **{p['title']}:** {p['text']}"]
lines += ['', '## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ', '', DATA.get('strategyIntro','ยังระบุไม่ได้ว่าหัวข้อใดออก Final มากที่สุด เพราะไม่มีขอบเขต Final หรือข้อสอบเก่าในชุดเอกสารนี้'), '']
for s in DATA['strategy']:
    lines += [f"- **{s['title']}:** {s['text']}"]
lines += ['', 'คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: '+', '.join(f'{kind} {n} ข้อ' for kind,n in question_types.items()), '']
qn=0
for t in DATA['topics']:
    lines += [f"### {t['title']}", '']
    for q in t['questions']:
        qn+=1
        lines += [f"**ข้อ {qn} · {q['type']}: {q['q']}**", '']
        if 'options' in q:
            lines += [f"- {chr(65+i)}. {o}" for i,o in enumerate(q['options'])]
            lines += ['']
        lines += ['เฉลย: '+q['answer'], '', f"อ้างอิง: {src}, {q['pages']}", '']
lines += ['## ภาพสำคัญที่ใช้ในเว็บ', '', 'ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่', '']
for f in DATA['figures']:
    lines += [f"- {f['title']}: {f['caption']} ({src}, หน้า {f['page']})"]
path=OUT/f'{chapter_label}-study-notes.md'
path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(path)
