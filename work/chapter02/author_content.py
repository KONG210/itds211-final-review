import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = 'itds-211_comp_arch_Chapter02.pdf'
topics = []

def mc(q, options, correct, answer, pages):
    return dict(type='เลือกตอบ', q=q, options=options, correct=correct, answer=answer, pages=pages)

def qa(q, answer, pages, kind='อัตนัย'):
    return dict(type=kind, q=q, answer=answer, pages=pages)

def table(headers, rows):
    return dict(headers=headers, rows=rows)

def add(id, title, level, pages, summary, remember, terms, example, confusion, mnemonic, questions, figures=(), comparison=None, **extra):
    assert len(questions) == 3
    reason = {
        'core': 'เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง',
        'important': 'เป็นตัวอย่างหรือแผนภาพเปรียบเทียบที่ช่วยใช้แนวคิดหลัก',
        'extra': 'เป็นรายละเอียดประกอบสำหรับอ่านเสริม',
    }[level]
    topic = dict(id=id,title=title,level=level,pages=pages,reason=reason,summary=summary,
                 remember=remember,terms=terms,example=example,confusion=confusion,
                 mnemonic=mnemonic,questions=questions,figures=list(figures),**extra)
    if comparison: topic['comparison'] = comparison
    topics.append(topic)

add('computer-models','Von Neumann และ Harvard Computer Model','core','หน้า 3–4',
'Von Neumann model ใช้ stored program โดย memory เก็บทั้งโปรแกรมและข้อมูล และอ้างตำแหน่งด้วย address มากกว่าชนิดของเนื้อหา; สไลด์ระบุการเข้าถึง/ทำงานแบบ sequential หรือ linear. Harvard model แยก memory และ bus สำหรับ instructions กับ data เพื่อลด bottleneck แต่เพิ่มความซับซ้อน. สไลด์ยกแนวทางผสมที่แยกแบบ Harvard ที่ L1 cache แต่ใช้แบบ Von Neumann ที่ main memory.',
['Von Neumann: stored program; program/data อยู่ใน memory และระบุตำแหน่งด้วย address (หน้า 3)','Harvard: instruction/data ใช้ memory และ bus แยกกัน (หน้า 4)','Hybrid ในสไลด์: Harvard-style ที่ L1; Von Neumann ที่ main memory (หน้า 4)'],
['stored program = แนวคิดให้ memory เก็บ program และ data','address = หมายเลขตำแหน่งใน memory','instruction memory / data memory; L1 cache / main memory'],
'เทียบแผนภาพหน้า 3–4 แล้วชี้ว่าทางเดินของ instructions กับ data แยกกันหรือใช้ร่วมกันในแต่ละโมเดล',
'อย่าสรุปว่าเครื่องผสมต้องแยก main memory ด้วย; หน้า 4 ระบุ main memory เป็น Von Neumann ในตัวอย่าง',
'Von Neumann เก็บร่วม; Harvard แยกทาง; Hybrid แยก L1 แต่รวม main memory',
[mc('โมเดลใดแยก memory และ bus สำหรับ instructions กับ data?',['Harvard','Von Neumann','MARIE RTL','Daisy chain'],0,'Harvard model ตามหน้า 4','หน้า 4'),qa('stored program ในหน้า 3 หมายถึงอะไร?','Memory เก็บทั้ง program และ data และเข้าถึงด้วยตำแหน่ง address','หน้า 3'),qa('Hybrid ที่สไลด์ยกตัวอย่างใช้สองโมเดลที่ระดับใด?','Harvard-style ที่ L1 cache และ Von Neumann ที่ main memory','หน้า 4','วิเคราะห์')],
['models-von','models-harvard'],table(['โมเดล','หน่วยความจำ/ทางเดิน','ข้อสังเกตตามสไลด์'],[['Von Neumann','โปรแกรมกับข้อมูลอยู่ใน memory','stored program; sequential/linear'],['Harvard','instructions/data แยก memory และ bus','ลด bottleneck แต่ซับซ้อนขึ้น'],['Hybrid ตัวอย่าง','แยกที่ L1; รวมที่ main memory','ใช้สองแนวทางคนละระดับ']]))

add('bus-lines','Bus และเส้น Data / Control / Address','core','หน้า 5–6',
'สไลด์แบ่ง bus ที่พบบ่อยเป็น point-to-point กับ multipoint และระบุว่า bus มี data, control และ address lines. Data lines ส่ง bits ระหว่างอุปกรณ์; control lines กำหนดทิศทางการไหลและจังหวะที่อุปกรณ์ใช้ bus; address lines ระบุ source หรือ destination. Multipoint bus เป็นทรัพยากรที่ใช้ร่วมกัน จึงมี protocol ใน hardware เพื่อควบคุมการเข้าถึง.',
['point-to-point และ multipoint เป็น bus สองแบบที่สไลด์กล่าวถึง','data lines ส่ง bits; control lines คุมทิศทาง/สิทธิ์ใช้; address lines ระบุตำแหน่งต้นทาง/ปลายทาง','multipoint เป็น shared resource และควบคุมการเข้าถึงด้วย hardware protocols'],
['Bus = ทางเชื่อมอุปกรณ์ที่ประกอบด้วย data/control/address lines ตามหน้า 5','Multipoint bus = bus ที่หลายอุปกรณ์ใช้ร่วมกันตามหน้า 6'],
'ใช้ภาพหน้า 5 ชี้เส้น address, data, control ระหว่าง CPU, memory และ I/O แล้วดูภาพ multipoint หน้า 6',
'address line บอกตำแหน่ง source/destination ไม่ได้ขน bits ของข้อมูลแทน data line',
'Data ขนบิต; Control คุมใช้; Address บอกที่',
[mc('เส้นใดระบุตำแหน่ง source หรือ destination?',['Address lines','Data lines','Clock period','IR'],0,'Address lines กำหนดตำแหน่งตามหน้า 5','หน้า 5'),qa('Control lines มีหน้าที่อะไรตามหน้า 5?','กำหนดทิศทางข้อมูลและเวลาที่แต่ละอุปกรณ์เข้าถึง bus','หน้า 5'),qa('ทำไม multipoint bus จึงต้องมี protocol?','เพราะหลายอุปกรณ์ใช้ทรัพยากรเดียวกัน ต้องควบคุมการเข้าถึงผ่าน protocol ใน hardware','หน้า 6','วิเคราะห์')],['bus-lines','multipoint-bus'],table(['Line','หน้าที่'],[['Data','ส่ง bits'],['Control','กำหนดทิศทางและเวลาเข้าถึง bus'],['Address','ระบุตำแหน่ง source/destination']]))

add('bus-arbitration','การชิงสิทธิ์ Bus (Bus Arbitration)','core','หน้า 7',
'เมื่อระบบ master-slave มีอุปกรณ์มากกว่าหนึ่งตัวที่เป็น bus master ได้ คำขอใช้ bus พร้อมกันต้องผ่าน arbitration. สไลด์ให้ 4 แบบ: distributed self-detection, distributed collision-detection, daisy chain และ centralized parallel. สองแบบแรกให้อุปกรณ์ตัดสินกันหรือทดลองใช้แล้วเริ่มใหม่เมื่อชนกัน; สองแบบหลังส่งสิทธิ์ตามลำดับความสำคัญหรือใช้วงจร arbitration กลาง.',
['มี bus masters หลายตัวพร้อมขอใช้ bus → ต้อง arbitrate','self-detection: devices ตัดสินกันเอง; collision-detection: ใครก็ลองใช้ ถ้าชนให้ลองใหม่','daisy chain: ส่ง permission จาก priority สูงไปต่ำ; centralized parallel: ต่อเข้าวงจร arbitration โดยตรง'],
['bus master = อุปกรณ์ที่ร้องขอ/ควบคุมการใช้ bus ในบริบทนี้','arbitration = การตัดสินสิทธิ์เมื่อมีคำขอพร้อมกัน'],
'จับคู่ชื่อแต่ละกลุ่มกับวิธีตัดสินสิทธิ์ตาม bullet หน้า 7',
'อย่าสลับ distributed self-detection กับ collision-detection; ชนกันแล้วลองใหม่เป็นแบบหลัง',
'ตรวจเอง–ชนแล้วลองใหม่–ส่งสิทธิ์ต่อ–มีวงจรกลาง',
[mc('แบบใดให้แต่ละอุปกรณ์ต่อเข้าวงจร arbitration โดยตรง?',['Centralized parallel','Daisy chain','Collision-detection','Self-detection'],0,'Centralized parallel ตามหน้า 7','หน้า 7'),qa('Daisy chain ส่งสิทธิ์อย่างไร?','จากอุปกรณ์ priority สูงสุดลงไปยังต่ำสุด','หน้า 7'),qa('Distributed self-detection ต่างจาก collision-detection อย่างไร?','แบบแรกอุปกรณ์ตัดสินกันว่าใครได้ bus; แบบหลังอุปกรณ์ลองใช้ได้และลองใหม่หากข้อมูลชนกัน','หน้า 7','วิเคราะห์')],['bus-arbitration'])

add('hardware-software','Hardware และ Software Approaches','important','หน้า 8–9',
'ภาพหน้า 8 เปรียบเทียบการจัดลำดับฟังก์ชัน arithmetic/logic ใน hardware กับการส่ง instruction codes ให้ instruction interpreter คุมวงจรทั่วไปใน software approach. สไลด์หน้า 9 นิยาม software เป็นลำดับ codes/instructions ที่ hardware ส่วนหนึ่งแปลและสร้าง control signals. โปรแกรมใหม่จึงให้ลำดับคำสั่งใหม่แทนการต่อวงจรใหม่ทุกครั้ง และแยกองค์ประกอบหลักเป็น CPU กับ I/O components.',
['hardware approach ในภาพ: ลำดับฟังก์ชัน arithmetic/logic ทำใน hardware','software approach: instruction codes → interpreter → control signals → general-purpose functions','CPU มี instruction interpreter และ arithmetic/logic; I/O รับข้อมูล/คำสั่งและรายงานผล'],
['Software = sequence of codes/instructions ตามหน้า 9','instruction interpreter และ control signals ตามภาพหน้า 8'],
'ไล่ลูกศรภาพหน้า 8 จาก instruction codes ผ่าน interpreter ไปยัง general-purpose functions',
'สไลด์ไม่ได้ระบุว่า software ไม่ใช้ hardware; ระบุว่ามี hardware ส่วนหนึ่งตีความคำสั่ง',
'เปลี่ยนโปรแกรมด้วย code; interpreter สร้างสัญญาณคุม',
[mc('Software approach ในภาพหน้า 8 ส่งสิ่งใดเข้า instruction interpreter?',['Instruction codes','Memory address only','Interrupt vector only','Bus priority'],0,'Instruction codes ตามภาพ','หน้า 8'),qa('สไลด์นิยาม software ว่าอย่างไร?','ลำดับ codes หรือ instructions ที่ hardware ส่วนหนึ่งตีความแล้วสร้าง control signals','หน้า 9'),qa('เหตุใดหน้า 9 จึงกล่าวว่าไม่ต้อง rewiring hardware ทุกโปรแกรม?','เพราะเปลี่ยนเป็นลำดับคำสั่งใหม่ที่ interpreter ตีความและควบคุมฟังก์ชันทั่วไป','หน้า 9','วิเคราะห์')],['hardware-software'])

add('top-level-registers','องค์ประกอบระดับบนและ MAR / MBR / I/OAR / I/OBR','core','หน้า 10–11',
'หน้า 11 แสดง CPU, main memory และ I/O module เชื่อมด้วย system bus. หน้า 10 แจกหน้าที่ register สำหรับติดต่อ memory และ I/O: MAR ชี้ address ที่จะอ่าน/เขียน, MBR เก็บข้อมูลที่อ่านมาหรือจะเขียน, I/OAR ระบุอุปกรณ์ I/O และ I/OBR แลกข้อมูลระหว่าง I/O module กับ CPU. ชื่อ register บอกได้ว่าเก็บ address หรือ data/buffer ของฝ่ายใด.',
['MAR = address ใน memory สำหรับ read/write; MBR = data เข้า/ออก memory','I/OAR = อุปกรณ์ I/O ที่เลือก; I/OBR = data แลกระหว่าง I/O module กับ CPU','ภาพ top-level: CPU, main memory, I/O module เชื่อมผ่าน system bus'],
['MAR = Memory Address Register','MBR = Memory Buffer Register','I/OAR = I/O Address Register','I/OBR = I/O Buffer Register'],
'อ่านภาพหน้า 11 แล้ววางหน้าที่ register ทั้งสี่จากหน้า 10 ลงบนเส้นทาง CPU–Memory และ CPU–I/O',
'MAR/MBR เป็นคู่ memory ส่วน I/OAR/I/OBR เป็นคู่ I/O; อย่าสลับ address กับ buffer',
'ตัว A ชี้ที่; ตัว B บรรทุกข้อมูล — คู่ memory และ I/O',
[mc('Register ใดเก็บข้อมูลที่จะเขียนลง memory หรืออ่านขึ้นมา?',['MBR','MAR','I/OAR','PC'],0,'MBR เป็น buffer ของข้อมูล memory','หน้า 10'),qa('I/OAR ต่างจาก I/OBR อย่างไร?','I/OAR ระบุอุปกรณ์ I/O; I/OBR ใช้แลกข้อมูลระหว่าง I/O module และ CPU','หน้า 10'),qa('ภาพ top-level มีองค์ประกอบใดเชื่อมผ่าน system bus?','CPU, main memory และ I/O module','หน้า 11','วิเคราะห์')],['registers','top-level'],table(['Register','สิ่งที่เก็บ/ระบุ'],[['MAR','memory address'],['MBR','data จาก/ไป memory'],['I/OAR','I/O device'],['I/OBR','data ระหว่าง I/O module กับ CPU']]))

add('fetch-cycle','Basic Instruction Cycle และ Fetch','core','หน้า 12–13',
'วงจรคำสั่งพื้นฐานในหน้า 12 สลับ Fetch Cycle กับ Execute Cycle ไปจน HALT. ต้นแต่ละวงจร processor ดึง instruction จาก memory โดย PC ถือ address ของคำสั่งที่จะดึง; หลัง fetch จะเพิ่ม PC เพื่อชี้คำสั่งถัดไป. คำสั่งที่ดึงมาใส่ IR แล้ว processor ตีความและทำ action ที่ต้องการ.',
['ภาพหน้า 12: Fetch Next Instruction → Execute Instruction → วนหรือ HALT','PC ถือ address ของ instruction ที่จะ fetch ถัดไป และเพิ่มค่าหลัง fetch','IR รับ fetched instruction ก่อน processor แปลและปฏิบัติ'],
['PC = Program Counter','IR = Instruction Register','Fetch Cycle / Execute Cycle ตามหน้า 12–13'],
'เริ่มจาก PC ในหน้า 13 แล้วชี้เส้นทาง fetch → IR → interpret/perform action ก่อนกลับไป fetch ถัดไป',
'การเพิ่ม PC หลัง fetch เป็นการเดินตามลำดับ; แผนภาพและคำสั่งควบคุมอาจเปลี่ยนทางเดินได้ในหัวข้ออื่น',
'PC ชี้ที่; IR ถือคำสั่ง; Fetch แล้ว Execute',
[mc('PC ถืออะไรที่ต้น instruction cycle?',['Address ของ instruction ที่จะ fetch ถัดไป','ข้อมูลที่เพิ่ง output','ผล arithmetic ล่าสุด','หมายเลข I/O device'],0,'PC ถือ address ของคำสั่งถัดไปตามหน้า 13','หน้า 13'),qa('หลัง fetch processor ทำอะไรกับ PC และ IR?','เพิ่ม PC และนำ fetched instruction ไปไว้ใน IR','หน้า 13'),qa('ภาพ Basic Instruction Cycle แสดงการวนระหว่างขั้นใด?','Fetch Next Instruction และ Execute Instruction จน HALT','หน้า 12','วิเคราะห์')],['basic-cycle'])

add('hypothetical-machine','ตัวอย่างเครื่องสมมติและการเดินโปรแกรม','important','หน้า 14',
'ภาพหน้า 14 ใช้เครื่องสมมติที่แบ่ง instruction format เป็น opcode กับ address และแสดง PC, IR, AC. คำสั่ง 0001 โหลด memory เข้า AC, 0101 บวก memory เข้า AC และ 0010 เก็บ AC กลับ memory. ลำดับภาพใช้ค่าที่ address 940 = 0003 และ 941 = 0002 จน AC เป็น 0005 แล้วเก็บที่ 941; นี่เป็นตัวอย่างเครื่องสมมติในหน้านี้ ไม่ใช่ opcode table ของ MARIE หน้า 22.',
['instruction format ของเครื่องสมมติ: opcode bits 0–3 และ address bits 4–15','PC = address of instruction; IR = instruction being executed; AC = temporary storage','ตัวอย่าง 0003 + 0002 = 0005 แล้ว store ที่ address 941'],
['AC = Accumulator','Opcode = ส่วนรหัสการทำงาน; Address = ส่วนตำแหน่งตามภาพ','0001 Load, 0010 Store, 0101 Add — เฉพาะตัวอย่างหน้า 14'],
'ไล่ 6 ช่องในภาพหน้า 14: fetch 1940 → AC รับ 0003; fetch 5941 → AC เป็น 0005; fetch 2941 → memory 941 เป็น 0005',
'รหัส Add/Store ในเครื่องสมมติหน้า 14 ต่างจากรหัส MARIE หน้า 22; อย่านำสองชุดมาปน',
'Load 3 → Add 2 → Store 5 ในภาพเครื่องสมมติ',
[mc('ในเครื่องสมมติหน้า 14 รหัส 0101 ทำอะไร?',['Add to AC from Memory','Load AC from Memory','Store AC to Memory','Halt'],0,'0101 เป็น Add ตาม partial opcode list','หน้า 14'),qa('เมื่อโหลด 0003 แล้วบวก 0002 ค่า AC ในภาพเป็นเท่าไร?','0003 + 0002 = 0005 ตาม Step 4','หน้า 14','คำนวณ'),qa('ทำไมไม่ควรใช้รหัส 0101 นี้แทน Add ของ MARIE?','เป็นคนละเครื่อง/ตารางรหัส: หน้า 14 เป็น hypothetical machine ส่วนหน้า 22 เป็น MARIE ISA','หน้า 14, 22','วิเคราะห์')],['hypothetical-program'])

add('cycle-state','Instruction Cycle State Diagram','important','หน้า 15',
'ภาพ state diagram ขยาย fetch/execute เป็น instruction address calculation, instruction fetch, instruction operation decoding, operand address calculation/fetch, data operation และ operand address calculation/store. เส้นทาง operand fetch อาจวนเมื่อมี multiple operands และ store อาจวนเมื่อมี multiple results. เมื่อคำสั่งเสร็จ จะกลับไปคำนวณ address เพื่อ fetch คำสั่งถัดไป.',
['แกนภาพ: instruction fetch → decode → operand address/fetch → data operation → operand address/store','มีทางวน multiple operands และ multiple results','คำสั่งเสร็จแล้วกลับเส้น fetch next instruction'],
['Instruction Cycle State Diagram = ภาพสถานะละเอียดของ fetch/execute ตามหน้า 15','Operand fetch / Operand store = สถานะดึง/เก็บ operand ตามภาพ'],
'ตามลูกศรจาก instruction fetch ไป data operation แล้วตรวจเส้นย้อนสำหรับหลาย operands/results',
'ภาพไม่ได้บอกว่าทุกคำสั่งต้องผ่านทุกสถานะ; เส้นทางขึ้นกับ operand และผลลัพธ์',
'Fetch คำสั่ง → Decode → Operand → Operate → Store/วน',
[mc('เส้นทางใดในภาพรองรับ multiple operands?',['วงกลับระหว่าง operand address calculation กับ operand fetch','กลับจาก HALT ไป START','ข้าม instruction fetch','ไป I/OAR'],0,'ภาพวนที่ operand fetch สำหรับ multiple operands','หน้า 15'),qa('หลัง instruction operation decoding ภาพไปยังกลุ่มสถานะใด?','operand address calculation และต่อไป operand fetch/data operation','หน้า 15'),qa('ทำไมจึงไม่ควรจำว่าทุกคำสั่งต้องผ่าน operand fetch และ store?','ภาพมีหลายเส้นทางตามลักษณะ operand/result ไม่ได้บังคับผ่านทุกสถานะ','หน้า 15','วิเคราะห์')],['state-diagram'])

add('marie-registers','MARIE: Register 7 ตัวและขนาด','core','หน้า 17–18',
'สไลด์แนะนำ MARIE ผ่าน register 7 ตัวและภาพ architecture. AC กับ MBR เป็น 16-bit; MAR กับ PC เป็น 12-bit; InREG กับ OutREG เป็น 8-bit; IR ถือ instruction ก่อน execute. หน้าที่หลักคือ AC เก็บ operand/เงื่อนไขตามสไลด์, MAR เก็บ address, MBR เก็บ data, PC ชี้คำสั่งถัดไป และ InREG/OutREG รับส่งข้อมูลอุปกรณ์.',
['AC/MBR = 16-bit; MAR/PC = 12-bit; InREG/OutREG = 8-bit','IR ถือ instruction ก่อน execute; สไลด์ไม่ได้ระบุความกว้าง IR เป็นตัวเลขในรายการหน้า 17','AC, MAR, MBR, PC, IR, InREG, OutREG รวม 7 ตัว'],
['AC = Accumulator','MAR = Memory Address Register; MBR = Memory Buffer Register','PC = Program Counter; IR = Instruction Register','InREG / OutREG = input/output register'],
'ใช้แผนภาพหน้า 18 วาง register บริเวณ CPU, ALU, I/O และ main memory แล้วทวนหน้าที่หน้า 17',
'คำบรรยาย AC หน้า 17 ใช้คำ “conditional operator” ซึ่งอาจทำให้งง; ให้ยึดข้อความและภาพต้นฉบับ ไม่เติมความหมายที่ไม่มี',
'16: AC/MBR; 12: MAR/PC; 8: In/Out — IR ถือคำสั่ง',
[mc('คู่ใดเป็น 12-bit ตามหน้า 17?',['MAR และ PC','AC และ MBR','InREG และ OutREG','IR และ ALU'],0,'MAR และ PC ระบุ 12-bit','หน้า 17'),qa('MBR ทำหน้าที่อะไรใน MARIE?','เก็บข้อมูลหลังดึงจาก memory หรือก่อนวางลง memory','หน้า 17'),qa('InREG กับ OutREG ต่างกันอย่างไร?','InREG ถือข้อมูลที่อ่านจาก input device; OutREG ถือข้อมูลที่พร้อมสำหรับ output device','หน้า 17','วิเคราะห์')],['marie-architecture'],table(['Register','ขนาดที่สไลด์ระบุ','หน้าที่หลัก'],[['AC','16-bit','เก็บ operand/เงื่อนไขตามคำอธิบาย'],['MAR / PC','12-bit','address ใน memory / address ของคำสั่งถัดไป'],['MBR','16-bit','data จาก/ไป memory'],['InREG / OutREG','8-bit','input / output'],['IR','ไม่ระบุตัวเลขในรายการ','instruction ก่อน execute']]))

add('marie-datapath','MARIE Architecture และ Data Path','important','หน้า 18–20',
'ภาพ architecture แสดง register, ALU, control unit และ main memory ของ MARIE. Register เชื่อมกันและเชื่อม main memory ผ่าน common data bus โดยแต่ละอุปกรณ์บน bus มีหมายเลขเฉพาะซึ่งกำหนดบน control lines เมื่อจะให้ทำงาน. ยังมีทางเชื่อมแยกระหว่าง AC–MBR และ ALU–AC/MBR เพื่อถ่ายข้อมูลบางส่วนโดยไม่ใช้ main data bus; หน้า 20 วาด data path เชิงภาพ.',
['register และ main memory เชื่อมผ่าน common data bus','control lines ตั้ง unique number ของอุปกรณ์ที่จะทำงาน','ทางเชื่อมแยก AC/MBR/ALU ช่วย transfer โดยไม่ใช้ main bus'],
['Data path = เส้นทางข้อมูลตามภาพหน้า 20','common data bus / control lines ตามหน้า 19'],
'เทียบ architecture หน้า 18 กับ data path หน้า 20 แล้วหาทาง main bus กับทางเชื่อมแยกของ ALU',
'หมายเลขอุปกรณ์บน control lines ใช้ระบุ device ไม่ใช่ memory address จาก MAR โดยตรง',
'บัสหลักเชื่อมทั้งหมด; ทางแยกช่วย AC–MBR–ALU',
[mc('ข้อใดถ่ายข้อมูลโดยไม่ใช้ main data bus ได้ตามหน้า 19?',['ทางเชื่อมแยก AC–MBR และ ALU–AC/MBR','เฉพาะ main memory','เฉพาะ OutREG ไป keyboard','ทุกอุปกรณ์โดยไม่ต้องมี bus'],0,'หน้า 19 ระบุ separate connections','หน้า 19'),qa('MARIE เชื่อม registers กับ main memory ด้วยอะไร?','common data bus','หน้า 19'),qa('หมายเลขเฉพาะของอุปกรณ์ใช้ตรงไหนเมื่อจะให้ทำงาน?','ตั้งบน control lines ตามหน้า 19','หน้า 19','วิเคราะห์')],['marie-datapath'])

add('marie-isa','MARIE ISA และรูปแบบคำสั่ง','core','หน้า 21–22',
'ISA กำหนดรูปแบบ instructions และ primitive operations ที่เครื่องทำได้ จึงเป็น interface ระหว่าง hardware กับ software. หน้า 21 กล่าวว่า MARIE มี 13 instructions ส่วนหน้า 22 แสดงรูปแบบ 16-bit แบ่ง opcode bits 15–12 กับ address bits 11–0 และตาราง fundamental instructions ที่มองเห็น 9 รายการ. ต้องตรวจสอบจากต้นฉบับหากต้องการรายชื่อครบ 13 เพราะสไลด์หน้านี้ให้รายการเพียง 9.',
['ISA ระบุ instruction format และ primitive operations','รูปแบบ MARIE: opcode 4 bits (15–12) + address 12 bits (11–0)','ตารางหน้า 22: Load1, Store2, Add3, Subt4, Input5, Output6, Halt7, Skipcond8, Jump9'],
['ISA = Instruction Set Architecture','Opcode = bits 15–12; Address = bits 11–0 ในคำสั่ง 16-bit','Load/Store/Add/Subt/Input/Output/Halt/Skipcond/Jump ตามตารางหน้า 22'],
'อ่านตารางหน้า 22 จับคู่เลข hex 1–9 กับ mnemonic และผลของคำสั่งที่ตารางบอก',
'หน้า 21 เขียน 13 instructions แต่หน้า 22 มองเห็น 9 รายการ; รายการอีก 4 ตัวต้องตรวจสอบจากต้นฉบับ และห้ามแต่งเพิ่ม',
'MARIE 16 บิต: 4 opcode + 12 address; ตารางที่เห็น 1–9',
[mc('ใน MARIE instruction bits 15–12 ใช้ทำอะไร?',['Opcode','Memory buffer','Input data','Interrupt priority'],0,'ภาพหน้า 22 กำหนด bits 15–12 เป็น opcode','หน้า 22'),qa('ISA เป็น interface ระหว่างสิ่งใด?','hardware และ software','หน้า 21'),qa('เหตุใดรายชื่อ 13 คำสั่งของ MARIE ยังต้องตรวจสอบจากต้นฉบับ?','หน้า 21 บอกว่ามี 13 แต่ตารางหน้า 22 แสดงเพียง 9 รายการ จึงไม่มีรายชื่อครบในสไลด์ที่เห็น','หน้า 21–22','วิเคราะห์')],['marie-isa'],table(['Hex','Mnemonic','ผลตามตารางหน้า 22'],[['1','Load X','AC ← memory[X]'],['2','Store X','memory[X] ← AC'],['3','Add X','บวก memory[X] เข้า AC'],['4','Subt X','ลบ memory[X] จาก AC'],['5/6','Input / Output','รับค่าเข้า AC / ส่งค่า AC ไป display'],['7/8/9','Halt / Skipcond / Jump X','หยุด / ข้ามตามเงื่อนไข / ใส่ X ใน PC']]))

add('marie-bit-pattern','การอ่าน Bit Pattern: LOAD และ SKIPCOND','core','หน้า 23–24',
'ตัวอย่าง LOAD ใน IR หน้า 23 มี opcode 1 และ address 3 จึงเป็นการโหลดข้อมูลจากตำแหน่ง 3. ตัวอย่าง SKIPCOND หน้า 24 มี opcode 8 และ bits 11–10 เป็น 10; คำบรรยายหน้านั้นบอกว่าข้ามคำสั่งถัดไปหาก AC > 0. ทว่า RTL หน้า 27 เขียนกรณี AC > 0 ด้วย bits 11–10 = 11 ซึ่งขัดกับหน้า 24; เงื่อนไขรหัสนี้ต้องตรวจสอบจากต้นฉบับ.',
['LOAD: opcode 0001 / address 3 (หน้า 23)','SKIPCOND: opcode 1000 / bits 11–10 = 10 และคำบรรยาย AC > 0 (หน้า 24)','หน้า 27 ใช้ 11 สำหรับ AC > 0 จึงมีความไม่ตรงกัน'],
['IR[15–12] = opcode; IR[11–0] = address/field ตามรูปคำสั่ง','IR[11–10] = field เงื่อนไขในตัวอย่าง SKIPCOND'],
'อ่านกลุ่ม 4 บิตแรกจากภาพหน้า 23–24 เป็น opcode แล้วดู 12 บิตถัดไป ก่อนเทียบคำบรรยายกับ RTL',
'อย่าท่องว่า AC > 0 ต้องเป็น 10 หรือ 11 โดยไม่ระบุหน้าอ้างอิง: สไลด์สองหน้าขัดกัน ต้องตรวจสอบจากต้นฉบับ',
'4 บิตหน้าเป็น opcode; SKIPCOND มีจุดขัดกันหน้า 24/27',
[mc('ภาพ LOAD หน้า 23 ระบุ address ใด?',['3','8','10','11'],0,'ภาพและคำบรรยายระบุ address 3','หน้า 23'),qa('หน้า 24 ระบุ bits 11–10 ของ SKIPCOND และเงื่อนไขอย่างไร?','ระบุ 10 และบอกว่าจะข้ามคำสั่งถัดไปเมื่อ AC > 0','หน้า 24'),qa('เหตุใดรหัสเงื่อนไข AC > 0 ต้องตรวจสอบ?','หน้า 24 เขียน 10 แต่ RTL หน้า 27 เขียน 11 สำหรับ AC > 0','หน้า 24, 27','วิเคราะห์')],['load-bits','skipcond-bits'])

add('rtl-load-add','Microoperations และ RTL ของ LOAD / ADD','core','หน้า 25–26',
'คำสั่งหนึ่งประกอบด้วย microoperations หลายขั้น และสไลด์ใช้ Register Transfer Language (RTL) ระบุลำดับการย้ายข้อมูล. M[X] คือค่าที่เก็บใน memory location X ส่วนลูกศร ← หมายถึงย้ายค่าไปยัง register หรือ memory location. LOAD X ทำ MAR ← X, MBR ← M[MAR], AC ← MBR; ADD X ใช้สองขั้นแรกเหมือนกัน แล้วทำ AC ← AC + MBR.',
['microoperations = ขั้นย่อยในหนึ่ง instruction','M[X] หมายถึงค่าจริงใน memory ที่ address X; ← คือการย้ายค่า','LOAD และ ADD ต่างที่ขั้นสุดท้าย: AC ← MBR เทียบกับ AC ← AC + MBR'],
['RTL = Register Transfer Language','M[X] = data at memory location X','MAR, MBR, AC ตามหน้า 25–26'],
'เขียน LOAD/ADD 3 ขั้นจากสไลด์แล้วชี้ว่าต้องอ่าน memory ผ่าน MAR → MBR ก่อนปรับ AC',
'อย่าสลับ LOAD กับ ADD: LOAD แทน AC ด้วย MBR ส่วน ADD เก็บ AC เดิมมาบวก MBR',
'MAR ชี้ที่ → MBR รับค่า → AC แทนหรือบวก',
[mc('ขั้นสุดท้ายของ ADD X คือข้อใด?',['AC ← AC + MBR','AC ← MBR','MAR ← PC','PC ← PC + 1'],0,'RTL ของ ADD หน้า 26 จบด้วย AC ← AC + MBR','หน้า 26'),qa('M[X] ใน MARIE RTL หมายถึงอะไร?','ค่าข้อมูลจริงที่เก็บใน memory location X','หน้า 25'),qa('LOAD X และ ADD X ต่างกันที่ microoperation สุดท้ายอย่างไร?','LOAD: AC ← MBR; ADD: AC ← AC + MBR','หน้า 26','วิเคราะห์')],['rtl'],
formulas=[dict(expr='LOAD X: MAR ← X → MBR ← M[MAR] → AC ← MBR\nADD X: MAR ← X → MBR ← M[MAR] → AC ← AC + MBR',description='ลำดับ microoperations ตามต้นฉบับ',pages='หน้า 26')])

add('skipcond-rtl','RTL ของ SKIPCOND และเงื่อนไข AC','core','หน้า 24, 27',
'RTL หน้า 27 ให้ SKIPCOND เพิ่ม PC อีก 1 เมื่อเงื่อนไข AC ตรงกับ field ใน IR[11–10]: 00 กับ AC < 0, 01 กับ AC = 0 และ 11 กับ AC > 0. การเพิ่ม PC นี้คือการข้าม instruction ถัดไปในบริบทของคำสั่ง. แต่ภาพหน้า 24 เขียน field = 10 สำหรับ AC > 0; ต้องตรวจสอบจากต้นฉบับว่ารหัสใดถูกต้องก่อนใช้ตอบโจทย์.',
['หน้า 27: 00 → AC < 0; 01 → AC = 0; 11 → AC > 0','เมื่อเงื่อนไขจริง: PC ← PC + 1','หน้า 24 ระบุ 10 → AC > 0 ซึ่งขัดกับ RTL หน้า 27'],
['SKIPCOND = skip next instruction on condition','IR[11–10] = condition bits ในตัวอย่าง','PC ← PC + 1 ตาม RTL หน้า 27'],
'เทียบตารางเงื่อนไขที่สรุปจาก RTL หน้า 27 กับ bit pattern และคำบรรยายหน้า 24 ทีละรายการ',
'รหัสกรณี AC > 0 ขัดกันในสไลด์เอง; ต้องตรวจสอบจากต้นฉบับ ไม่แก้ด้วยความรู้นอกเอกสาร',
'00 ติดลบ; 01 ศูนย์; กรณีบวกมีความขัดกัน 10/11',
[mc('RTL หน้า 27 ระบุ field ใดเมื่อ AC = 0?',['01','00','10','11'],0,'หน้า 27 ให้ IR[11–10] = 01 แล้วทดสอบ AC = 0','หน้า 27'),qa('SKIPCOND ทำอะไรกับ PC เมื่อเงื่อนไขเป็นจริง?','PC ← PC + 1 เพื่อข้ามคำสั่งถัดไป','หน้า 27'),qa('หน้า 24 กับ 27 ต่างกันตรงไหนในกรณี AC > 0?','หน้า 24 เขียน bits 11–10 = 10; หน้า 27 เขียน = 11 ต้องตรวจสอบจากต้นฉบับ','หน้า 24, 27','วิเคราะห์')],['skipcond-rtl'],
comparison=table(['เงื่อนไข','รหัสที่ปรากฏ','สถานะ'],[['AC < 0','00 ใน RTL หน้า 27','ตรงในหน้า 27'],['AC = 0','01 ใน RTL หน้า 27','ตรงในหน้า 27'],['AC > 0','10 หน้า 24 / 11 หน้า 27','ต้องตรวจสอบจากต้นฉบับ']]),
formulas=[dict(expr='if IR[11–10] = 00 and AC < 0: PC ← PC + 1\nif IR[11–10] = 01 and AC = 0: PC ← PC + 1\nif IR[11–10] = 11 and AC > 0: PC ← PC + 1',description='ถอด RTL หน้า 27 ตรงตามต้นฉบับ; กรณี AC > 0 ขัดกับคำบรรยายหน้า 24',pages='หน้า 27')])

add('marie-processing','MARIE Fetch–Decode–Execute และ Operand','core','หน้า 28–29',
'Instruction processing ดึง instruction จาก memory เข้า IR แล้ว decode เพื่อกำหนดงาน. ถ้าต้องใช้ operand จาก memory จะนำค่ามาไว้ใน MBR ก่อน execute. Flowchart หน้า 29 แสดง PC → MAR, M[MAR] → IR พร้อมเพิ่ม PC, แยก opcode/address ระหว่าง decode, แล้วจึงดึง operand หากจำเป็นและ execute.',
['fetch: MAR ← PC; IR ← M[MAR]; PC เพิ่ม 1','decode: แยกส่วน instruction และวาง IR[11–0] ใน MAR ตามภาพ','operand ที่ต้องอ่าน: MBR ← M[MAR] แล้ว execute'],
['Fetch–Decode–Execute cycle = ชุดขั้นที่เครื่องทำเมื่อรันโปรแกรม','IR[11–0] = address field ตามภาพหน้า 29'],
'ไล่ flowchart หน้า 29 สองทางหลังคำถาม “Instruction requires operand?” แล้วกลับไป fetch คำสั่งถัดไป',
'อย่าคิดว่าทุก instruction ต้องอ่าน operand; ภาพมีทาง No ไป execute โดยตรง',
'PC→MAR→IR; Decode; ถ้าต้องใช้จึง MBR; Execute',
[mc('หาก instruction ต้องใช้ operand จาก memory ค่าจะไป register ใดก่อน execute?',['MBR','OutREG','I/OAR','flags register'],0,'หน้า 28–29 ให้นำ operand เข้า MBR','หน้า 28–29'),qa('ขั้น fetch ตาม flowchart หน้า 29 ใช้ PC และ MAR อย่างไร?','คัดลอก PC ไป MAR แล้วคัดลอก memory ณ MAR ไป IR และเพิ่ม PC','หน้า 29'),qa('เมื่อ instruction ไม่ต้องใช้ operand flowchart ไปทางใด?','ข้ามการนำค่าเข้า MBR แล้วไป Execute the instruction','หน้า 29','วิเคราะห์')],['marie-fetch-flow'])

add('interrupt-entry','Interrupt: เหตุเกิดและการเข้า ISR','core','หน้า 30–32',
'สไลด์ระบุว่าการ interrupt หยุด/แทรก fetch-decode-execute cycle ได้ เช่น user break, การร้องขอ I/O และ critical error; แบ่ง hardware กับ software interrupt โดย software อาจเรียก OS system call. เมื่อมี interrupt วงจรเพิ่มขั้นตรวจและประมวลผล. ภาพหน้า 32 ให้ลำดับตรวจสัญญาณ → save variables/registers → หา ISR address ใน interrupt vector table → ใส่ address ใน PC และ branch ไป ISR → ทำงาน → restore แล้วกลับไปวงจรหลัก.',
['ตัวอย่างเหตุ: user break, I/O request, critical error','ISR = Interrupt Service Routine; vector table ใช้หา ISR address','ภาพ ISR ต้อง save/restore สถานะก่อนกลับไป fetch-decode-execute'],
['Hardware interrupt / Software interrupt ตามหน้า 30','ISR = Interrupt Service Routine','interrupt vector table ตามภาพหน้า 32'],
'ทวนภาพหน้า 31 เพิ่ม interrupt step แล้วไล่ภาพหน้า 32 จาก signal ไป ISR และกลับโปรแกรม',
'เหตุ interrupt กับ class ของ interrupt ในหน้า 37 เป็นคนละรายการจัดหมวด; อย่าปนเป็นคำจำกัดความเดียว',
'พบสัญญาณ → เก็บสถานะ → หา ISR → ทำงาน → คืนสถานะ',
[mc('ISR ย่อมาจากอะไรตามหน้า 32?',['Interrupt Service Routine','Instruction State Register','Input Signal Router','Interrupt System Rate'],0,'คำขยายอยู่หน้า 32','หน้า 32'),qa('ยก 2 เหตุ interrupt จากหน้า 30','เช่น user break และ I/O request; critical error ก็เป็นอีกเหตุหนึ่ง','หน้า 30'),qa('ทำไมต้อง save แล้ว restore variables/registers ตามภาพหน้า 32?','ภาพกำหนดให้เก็บสถานะก่อน branch ไป ISR และคืนก่อนกลับสู่วงจร fetch-decode-execute','หน้า 32','วิเคราะห์')],['interrupt-branch','isr-flow'])

add('masking-io','Maskable/Nonmaskable และ I/O ของ MARIE','core','หน้า 33–34',
'ระบบทั่วไปมักปิด interrupts ระหว่างกำลังประมวลผล interrupt โดยตั้ง bit ใน flags register; interrupt ที่ถูกเพิกเฉยกรณีนี้เรียก maskable. Nonmaskable ต้องถูกประมวลผลเพื่อรักษาเสถียรภาพระบบ. หน้า 34 ระบุว่า MARIE ใช้ modified programmed I/O: output ไป OutREG และ CPU polls InREG จนมี input แล้วคัดลอกเข้า AC; รายละเอียด interrupt-driven I/O อยู่นอกขอบเขตสไลด์.',
['maskable ถูก ignore ได้ในสถานการณ์ที่ disable interrupts','nonmaskable ต้อง process เพื่อให้ระบบ stable','MARIE: output → OutREG; CPU polls InREG → AC เมื่อรับ input'],
['flags register bit ตามหน้า 33','polling = CPU ตรวจ InREG ซ้ำตามคำอธิบายหน้า 34','programmed I/O / interrupt-driven I/O เป็นชื่อแนวทางในหน้า 34'],
'จับคู่ข้อเปรียบเทียบหน้า 33 และตามทางข้อมูล OutREG/InREG ในหน้า 34',
'ไม่ขยายรายละเอียด interrupt-driven I/O เกินสไลด์ เพราะหน้า 34 ระบุว่าอยู่นอกขอบเขต',
'Maskable อาจพัก; Nonmaskable ต้องทำ; MARIE polls InREG',
[mc('MARIE รับ input อย่างไรตามหน้า 34?',['CPU polls InREG แล้วคัดลอกค่าเข้า AC','interrupt-driven I/O ที่สไลด์ลงรายละเอียด','อ่าน OutREG เข้า PC','อ่าน address จาก IR โดยตรง'],0,'หน้า 34 ระบุ CPU polls InREG','หน้า 34'),qa('Maskable กับ nonmaskable ต่างกันอย่างไร?','แบบแรกถูก ignore ได้เมื่อ disable interrupts; แบบหลังต้อง process เพื่อรักษาระบบให้ stable','หน้า 33'),qa('ทำไมไม่ควรอธิบายขั้น interrupt-driven I/O ละเอียดจากสไลด์นี้?','หน้า 34 บอกว่าอยู่นอกขอบเขต discussion และให้เพียง MARIE modified programmed I/O','หน้า 34','วิเคราะห์')],['interrupt-masking'],table(['ชนิด','ตามคำอธิบายหน้า 33'],[['Maskable','ถูกเพิกเฉยได้เมื่อ interrupts ถูกปิด'],['Nonmaskable','ต้องประมวลผลเพื่อความเสถียร']]))

add('marie-simple-program','โปรแกรม MARIE 100–106 (hex) และ ADD 105','core','หน้า 35–36',
'ตารางหน้า 35 ให้โปรแกรมที่ address 100–103 เป็น Load 104, Add 105, Store 106, Halt และข้อมูลที่ 104 = 0023, 105 = FFE9, 106 = 0000 (hex). หน้า 36 ไล่คำสั่ง Add 105: เริ่ม PC 101, AC 0023; หลัง fetch/decode ได้ IR 3105, MAR 105, MBR FFE9 แล้ว execute ให้ AC 000C. อย่างไรก็ตาม binary contents ของ Store 106 ในหน้า 35 ขึ้นต้น 0100 ซึ่งไม่ตรงกับ hex 4106 และตาราง opcode Store = 0010 หน้า 22; ต้องตรวจสอบจากต้นฉบับ.',
['program address 100–103: Load 104 / Add 105 / Store 106 / Halt','ADD 105 trace: PC 101 → 102; IR 3105; MAR 105; MBR FFE9; AC 0023 → 000C','Store 106 มีความขัดกัน: binary 0100..., hex 4106, opcode Store ในหน้า 22 = 0010'],
['RTN = หัวคอลัมน์ Register Transfer Notation ในตารางหน้า 36','ค่าทุกตัวในตัวอย่างนี้เป็น hex ตามหน้า 35','IR/PC/MAR/MBR/AC เป็นคอลัมน์ register ใน trace'],
'ตามตารางหน้า 36 ทีละแถว Fetch → Decode → Get operand → Execute และเทียบค่าก่อน/หลังของแต่ละ register',
'อย่าคัดลอกรหัส Store แบบ binary จากหน้า 35 เป็นกฎโดยไม่ระบุความขัดกันกับ hex/table; ต้องตรวจสอบจากต้นฉบับ',
'100 Load → 101 Add → 102 Store → 103 Halt; ADD จบ AC 000C',
[mc('ADD 105 ในตารางหน้า 36 อ่าน operand จาก address ใด?',['105','100','102','106'],0,'แถว Get operand ชี้ address 105','หน้า 36'),qa('ตามตาราง ADD 105 ให้ AC 0023 บวก MBR FFE9 แล้ว AC เป็นค่าใด?','AC เป็น 000C ตามแถว Execute ในตารางหน้า 36','หน้า 36','คำนวณ'),qa('Store 106 มีจุดใดที่ต้องตรวจสอบ?','binary ขึ้นต้น 0100 แต่ hex เป็น 4106 และตาราง opcode หน้า 22 ให้ Store = 0010; สไลด์ไม่ตรงกัน','หน้า 22, 35','วิเคราะห์')],['marie-program','marie-add-trace'],
worked=[dict(title='Trace ADD 105 จากต้นฉบับ',steps=['เริ่ม PC 101, IR 1104, MAR 104, MBR 0023, AC 0023','Fetch: MAR ← PC = 101; IR ← M[101] = 3105; PC ← 102','Decode: MAR ← IR[11–0] = 105','Get operand: MBR ← M[105] = FFE9','Execute: AC ← AC + MBR; ตารางให้ AC = 000C'],answer='หลัง ADD 105: PC 102, IR 3105, MAR 105, MBR FFE9, AC 000C',pages='หน้า 35–36')])

add('interrupt-classes','Classes of Interrupts 4 กลุ่ม','core','หน้า 37',
'ตารางหน้า 37 แยก interrupt ตามแหล่ง/เหตุเป็น Program, Timer, I/O และ Hardware failure. Program เกิดจากเงื่อนไขระหว่าง execution เช่น overflow, division by zero, illegal instruction หรือ memory reference นอกพื้นที่ที่อนุญาต. Timer มาจาก timer ใน processor เพื่อให้งาน OS เกิดเป็นระยะ; I/O มาจาก controller เพื่อบอกการเสร็จงาน/ขอ service/แจ้ง error; Hardware failure เช่น power failure หรือ memory parity error.',
['4 classes: Program, Timer, I/O, Hardware failure','Program: overflow/divide by zero/illegal instruction/memory out of allowed range','Timer ให้ OS ทำหน้าที่เป็นระยะ; I/O controller แจ้ง completion/service/error','Hardware failure เช่น power failure และ memory parity error'],
['Program interrupt / Timer interrupt / I/O interrupt / Hardware failure ตามตารางหน้า 37'],
'จัดตัวอย่างในตารางหน้า 37 ลงสี่กลุ่ม โดยใช้เกณฑ์แหล่งกำเนิดตามสไลด์',
'I/O request ในหน้า 30 เป็นตัวอย่างเหตุ interrupt; หน้า 37 ให้รายละเอียด class I/O โดย controller',
'โปรแกรมผิด–Timer นัด–I/O แจ้ง–Hardware เสีย',
[mc('Division by zero อยู่ใน class ใดตามตาราง?',['Program','Timer','I/O','Hardware failure'],0,'เป็นตัวอย่าง Program interrupt','หน้า 37'),qa('Timer interrupt มีประโยชน์ตามตารางอย่างไร?','ทำให้ OS ปฏิบัติบางหน้าที่เป็นระยะ','หน้า 37'),qa('I/O กับ Hardware failure ต่างกันตามแหล่งกำเนิดอย่างไร?','I/O มาจาก I/O controller; Hardware failure มาจากความล้มเหลว เช่นไฟดับหรือ memory parity error','หน้า 37','วิเคราะห์')],['interrupt-classes'],table(['Class','ที่มา/ตัวอย่าง'],[['Program','เงื่อนไขจากการรันคำสั่ง เช่น divide by zero'],['Timer','timer ใน processor เพื่อให้ OS ทำงานเป็นระยะ'],['I/O','I/O controller แจ้งเสร็จงาน/ขอ service/error'],['Hardware failure','power failure หรือ memory parity error']]))

add('interrupt-control-flow','Program Flow และ Instruction Cycle เมื่อมี Interrupt','core','หน้า 38–40, 43',
'ภาพหน้า 38 เปรียบเทียบการเดินโปรแกรมขณะมี I/O โดยไม่มี interrupt กับมี interrupt; แบบหลังเปลี่ยนไปทำ interrupt handler แล้วกลับงานผู้ใช้. หน้า 39 วาดการย้าย control จาก user program ไป interrupt handler และกลับไปจุดต่อ. หน้า 40 เพิ่ม interrupt cycle หลัง execute เมื่อเปิด interrupts; state diagram หน้า 43 เพิ่ม interrupt check และ interrupt ก่อนกลับไป fetch คำสั่งถัดไป.',
['หน้า 38–39: handler รับ control ชั่วคราวแล้วกลับ user program','หน้า 40: check for interrupts หลัง execute เมื่อ interrupts enabled; หาก disabled เดินต่อ','หน้า 43: interrupt check ต่อจากการทำงานคำสั่ง ก่อน fetch รอบใหม่'],
['Interrupt handler = ชุดการทำงานที่รับ control ระหว่าง interrupt ตามภาพ','Interrupt cycle / Interrupt check ตามภาพหน้า 40, 43'],
'วาดเส้นลูกศร user program → handler → user program จากหน้า 39 แล้วใส่ตำแหน่ง check จากหน้า 40/43',
'การกลับโปรแกรมไม่ได้แปลว่ารันเริ่มต้นใหม่; ภาพแสดงกลับจุดต่อของ user program',
'Execute → ตรวจ interrupt → handler (ถ้ามี) → กลับไป fetch',
[mc('ภาพ Instruction Cycle with Interrupts วาง Check for Interrupts หลังขั้นใด?',['Execute Instruction','START','Fetch Next Instruction ก่อนเริ่ม','HALT'],0,'หน้า 40 วาง check หลัง execute','หน้า 40'),qa('หน้า 39 แสดง transfer of control ระหว่างอะไร?','user program กับ interrupt handler แล้วกลับ user program','หน้า 39'),qa('หน้า 43 เพิ่มสถานะใดจาก state diagram แบบไม่มี interrupt?','Interrupt check และ Interrupt ก่อนวนกลับไป fetch next instruction','หน้า 15, 43','วิเคราะห์')],['control-flow','interrupt-cycle','state-with-interrupt'])

add('io-wait-timing','Short และ Long I/O Wait กับ Interrupt','important','หน้า 41–42',
'ภาพ timing หน้า 41 เทียบกรณี I/O wait สั้น: เมื่อไม่มี interrupt processor รอช่วง I/O; เมื่อมี interrupt processor ทำงานอื่นควบคู่ระหว่าง I/O แล้วรับการแจ้งกลับ. หน้า 42 กรณี wait ยาวแสดงว่าแม้มี interrupt ก็อาจใช้เวลาทำงานอื่นได้เพียงบางส่วน แล้ว processor ยังต้องรอจน I/O เสร็จ. จึงควรอ่านลำดับและช่อง waiting ในภาพ ไม่สรุปว่า interrupt ตัดการรอได้หมดเสมอ.',
['สองภาพเปรียบเทียบ without interrupts กับ with interrupts','short wait: ช่วง I/O อาจซ้อนกับ processor executing','long wait: หลังงานอื่นหมด processor ยังรอ I/O ต่อได้'],
['I/O wait = ช่วงรอ I/O ตามแกนเวลาในภาพหน้า 41–42','concurrent with processor executing เป็นคำกำกับในภาพ'],
'เทียบช่องสีดำ processor waits และช่วง I/O operation ทั้งสองคอลัมน์ในหน้า 41 กับ 42',
'อย่าพูดว่า interrupts ทำให้ไม่ต้องรอ I/O ทุกกรณี; หน้า 42 แสดงการรอที่เหลือชัดเจน',
'สั้นอาจซ้อนพอดี; ยาวยังเหลือช่วงรอ',
[mc('ภาพ Long I/O wait เมื่อมี interrupt แสดงผลใด?',['processor ทำงานอื่นแล้วอาจยังรอ','processor ไม่ต้องรอแน่นอน','I/O หยุดทำงานทันที','ไม่มีการกลับเข้าโปรแกรม'],0,'หน้า 42 แสดงช่วง processor waits หลัง concurrent work','หน้า 42'),qa('หน้า 41 เปรียบเทียบ timing สองแบบใด?','without interrupts กับ with interrupts ในกรณี short I/O wait','หน้า 41'),qa('ทำไมจึงสรุปไม่ได้ว่า interrupt ลบเวลารอ I/O ทั้งหมด?','หน้า 42 กรณี long I/O wait ยังแสดง processor waits หลังจากทำงานอื่นช่วงหนึ่ง','หน้า 42','วิเคราะห์')],['short-wait','long-wait'],table(['กรณี','ผลที่ภาพ with interrupts แสดง'],[['Short I/O wait','processor ทำงานอื่นซ้อนช่วง I/O'],['Long I/O wait','ซ้อนการทำงานได้บางช่วง แต่ยังมีช่วงรอ I/O']]))

add('multiple-interrupts','Multiple Interrupts: Sequential และ Nested','core','หน้า 44–45',
'หน้า 44 เปรียบเทียบ sequential interrupt processing ซึ่ง handler หนึ่งเสร็จแล้วจึงไปอีก handler กับ nested processing ซึ่ง interrupt ใหม่แทรกกลาง handler ที่ทำอยู่แล้วค่อยกลับ. หน้า 45 ยกเวลาในภาพ: user program ถูก printer interrupt ที่ t=10; communication แทรกที่ t=15; กลับ printer ที่ t=25; disk แทรกที่ t=25; กลับ printer ที่ t=35; กลับ user program ที่ t=40. ลำดับนี้เป็นตัวอย่างเฉพาะภาพ ไม่ใช่กฎเวลา interrupt ทั่วไป.',
['Sequential: ทำ handler ทีละตัว แล้วกลับลำดับตามภาพ','Nested: handler ใหม่อาจแทรก handler ปัจจุบัน','ตัวอย่างหน้า 45: printer → communication → printer → disk → printer → user program'],
['Sequential interrupt processing / Nested interrupt processing ตามหน้า 44','Printer, Communication, Disk ISR เป็นชื่อในภาพหน้า 45'],
'ใช้นิ้วตามลูกศรเวลา t=10,15,25,25,35,40 ในหน้า 45 แล้วจับคู่กับรูป nested หน้า 44',
'เวลา t ในหน้า 45 เป็นตัวอย่างจากภาพ; ไม่ใช่เวลามาตรฐานของระบบจริง และภาพไม่ได้กำหนดนโยบาย priority ทั่วไป',
'Sequential ต่อคิว; Nested แทรกซ้อนแล้วกลับ',
[mc('รูปแบบใดให้ interrupt Y แทรกระหว่าง handler X?',['Nested','Sequential','Point-to-point bus','Stored program'],0,'ภาพ (b) หน้า 44 เป็น nested interrupt processing','หน้า 44'),qa('หน้า 45 ลำดับ handler หลัง printer เริ่มที่ t=10 เป็นอย่างไร?','communication แทรกที่ t=15; กลับ printer t=25; disk แทรก t=25; กลับ printer t=35; user program t=40','หน้า 45'),qa('Sequential กับ nested ต่างกันอย่างไรตามภาพหน้า 44?','Sequential ทำ handler ทีละตัว; nested อนุญาตให้ handler ใหม่แทรก handler ที่กำลังทำ','หน้า 44','วิเคราะห์')],['multiple-interrupts','multiple-timeline'],table(['รูปแบบ','การย้าย control'],[['Sequential','handler หนึ่งจบก่อนจึงทำอีก handler'],['Nested','handler ใหม่แทรกกลาง handler ปัจจุบัน แล้วกลับมาทำต่อ']]))

figure_specs = [
 (3,'models-von','Von Neumann model','ภาพ CPU, memory และการเก็บโปรแกรม/ข้อมูลร่วมกัน'),
 (4,'models-harvard','Harvard model','ภาพแยก instruction memory กับ data memory'),
 (5,'bus-lines','เส้นของ Bus','ภาพ CPU–Memory–I/O พร้อม Address/Data/Control bus'),
 (6,'multipoint-bus','Multipoint bus','อุปกรณ์หลายตัวใช้ bus เดียวร่วมกัน'),
 (7,'bus-arbitration','Bus arbitration 4 แบบ','รายชื่อ self-detection, collision-detection, daisy chain และ centralized parallel'),
 (8,'hardware-software','Hardware/Software approaches','แผนภาพ sequence ใน hardware เทียบ instruction interpreter'),
 (10,'registers','MAR/MBR/I/OAR/I/OBR','ภาพหน้าที่ register ฝั่ง memory และ I/O'),
 (11,'top-level','Computer components','CPU, main memory และ I/O module ผ่าน system bus'),
 (12,'basic-cycle','Basic instruction cycle','Fetch/Execute วนจน HALT'),
 (14,'hypothetical-program','เครื่องสมมติ: Load–Add–Store','ภาพ 6 ขั้น 0003 + 0002 = 0005; เป็นคนละ ISA กับ MARIE'),
 (15,'state-diagram','Instruction cycle state diagram','สถานะ fetch, decode, operand, operation, store'),
 (18,'marie-architecture','MARIE architecture','แผนผัง register, ALU, CPU และ main memory'),
 (20,'marie-datapath','MARIE data path','ภาพการเชื่อม register และ bus'),
 (22,'marie-isa','MARIE instruction format','ภาพ opcode/address และตาราง 9 คำสั่งที่เห็น'),
 (23,'load-bits','LOAD bit pattern','Opcode 1 และ address 3 ใน IR'),
 (24,'skipcond-bits','SKIPCOND bit pattern','หน้า 24 บอก field 10 เมื่อ AC > 0; ขัดกับหน้า 27'),
 (26,'rtl','RTL ของ LOAD และ ADD','ลำดับ MAR, MBR, AC ที่สไลด์ระบุ'),
 (27,'skipcond-rtl','RTL ของ SKIPCOND','หน้า 27 บอก field 11 เมื่อ AC > 0; ขัดกับหน้า 24'),
 (29,'marie-fetch-flow','MARIE fetch–decode–execute','Flowchart แบบมี/ไม่มี operand'),
 (31,'interrupt-branch','Interrupt เพิ่มในวงจร','แผนภาพการตรวจและ process interrupt'),
 (32,'isr-flow','ขั้นตอนเข้า ISR','save state, vector table, branch, restore'),
 (33,'interrupt-masking','Maskable/Nonmaskable','คำอธิบายการปิด interrupts และประเภทที่ยังต้องทำ'),
 (35,'marie-program','โปรแกรม MARIE 100–106','ตาราง mnemonic/binary/hex; Store 106 มีจุดขัดกัน'),
 (36,'marie-add-trace','Trace ADD 105','ค่าของ PC/IR/MAR/MBR/AC ทีละขั้น'),
 (37,'interrupt-classes','Classes of interrupts','ตาราง Program/Timer/I/O/Hardware failure'),
 (38,'control-flow','Program flow กับ interrupt','แผนภาพ without/with interrupt'),
 (40,'interrupt-cycle','Instruction cycle with interrupts','เพิ่มการตรวจ interrupt หลัง execute'),
 (41,'short-wait','Short I/O wait','timing เปรียบเทียบกรณีมี/ไม่มี interrupt'),
 (42,'long-wait','Long I/O wait','timing แสดงช่วง processor waits ที่ยังเหลือ'),
 (43,'state-with-interrupt','State diagram with interrupt','เพิ่ม interrupt check และ interrupt'),
 (44,'multiple-interrupts','Sequential/Nested interrupts','เส้นทาง control ของ handler X/Y'),
 (45,'multiple-timeline','ตัวอย่างเวลา multiple interrupts','Printer/Communication/Disk ISR ที่ t=10–40'),
]
figures = [dict(id=id,page=page,file=f'slide-{page:02d}.png',title=title,caption=caption)
           for page,id,title,caption in figure_specs]

flashcards = [
 ('Von Neumann: stored program','Memory เก็บ program และ data; address ระบุตำแหน่ง ไม่ใช่ชนิดเนื้อหา','หน้า 3'),
 ('Harvard model','แยก memory และ buses ของ instructions กับ data','หน้า 4'),
 ('Hybrid ในสไลด์','Harvard-style ที่ L1 cache; Von Neumann ที่ main memory','หน้า 4'),
 ('Data lines','ส่ง bits ระหว่างอุปกรณ์','หน้า 5'),
 ('Control lines','กำหนดทิศทาง data และเวลา/สิทธิ์ที่ device ใช้ bus','หน้า 5'),
 ('Address lines','ระบุตำแหน่ง source หรือ destination','หน้า 5'),
 ('Multipoint bus','Shared resource; access ควบคุมด้วย hardware protocols','หน้า 6'),
 ('Self-detection','อุปกรณ์ตัดสินกันเองว่าใครได้ bus','หน้า 7'),
 ('Collision-detection','ลองใช้ bus; ถ้าข้อมูลชนกันให้ลองใหม่','หน้า 7'),
 ('Daisy chain','ส่งสิทธิ์จาก priority สูงไปต่ำ','หน้า 7'),
 ('Centralized parallel','แต่ละอุปกรณ์ต่อเข้าวงจร arbitration โดยตรง','หน้า 7'),
 ('Software ตามสไลด์','ลำดับ codes/instructions ที่ hardware ส่วนหนึ่งตีความและสร้าง control signals','หน้า 9'),
 ('MAR','Memory Address Register: address สำหรับ memory read/write','หน้า 10'),
 ('MBR','Memory Buffer Register: data ที่อ่านจาก/จะเขียนไป memory','หน้า 10'),
 ('I/OAR','I/O Address Register: ระบุ I/O device','หน้า 10'),
 ('I/OBR','I/O Buffer Register: data ระหว่าง I/O module และ CPU','หน้า 10'),
 ('PC ใน Fetch Cycle','เก็บ address ของ instruction ที่จะ fetch ถัดไป','หน้า 13'),
 ('IR ใน Fetch Cycle','รับ fetched instruction','หน้า 13'),
 ('MARIE AC / MBR กี่บิต?','อย่างละ 16-bit','หน้า 17'),
 ('MARIE MAR / PC กี่บิต?','อย่างละ 12-bit','หน้า 17'),
 ('MARIE InREG / OutREG กี่บิต?','อย่างละ 8-bit','หน้า 17'),
 ('MARIE IR','ถือ instruction ทันทีก่อน execution; รายการหน้า 17 ไม่ให้ตัวเลขความกว้าง','หน้า 17'),
 ('ISA','กำหนด instruction format และ primitive operations; interface hardware/software','หน้า 21'),
 ('MARIE instruction format','16 bits: opcode bits 15–12; address bits 11–0','หน้า 22'),
 ('MARIE Load / Store / Add / Subt','Hex opcode 1 / 2 / 3 / 4 ตามตาราง','หน้า 22'),
 ('MARIE Input / Output / Halt','Hex opcode 5 / 6 / 7 ตามตาราง','หน้า 22'),
 ('MARIE Skipcond / Jump','Hex opcode 8 / 9 ตามตาราง','หน้า 22'),
 ('LOAD bit pattern ตัวอย่าง','Opcode 1, address 3','หน้า 23'),
 ('SKIPCOND AC > 0 field','หน้า 24 ระบุ 10 แต่หน้า 27 ระบุ 11: ต้องตรวจสอบจากต้นฉบับ','หน้า 24, 27'),
 ('M[X] ใน RTL','ค่าข้อมูลจริงที่ memory location X','หน้า 25'),
 ('← ใน RTL','ย้ายค่าไป register หรือ memory location','หน้า 25'),
 ('LOAD X ใน RTL','MAR ← X; MBR ← M[MAR]; AC ← MBR','หน้า 26'),
 ('ADD X ใน RTL','MAR ← X; MBR ← M[MAR]; AC ← AC + MBR','หน้า 26'),
 ('SKIPCOND เมื่อเงื่อนไขจริง','PC ← PC + 1 เพื่อข้ามคำสั่งถัดไป','หน้า 27'),
 ('Fetch–Decode–Execute','fetch เข้า IR; decode; get operand เข้า MBR ถ้าต้องใช้; execute','หน้า 28–29'),
 ('ISR','Interrupt Service Routine','หน้า 32'),
 ('Interrupt vector table','ภาพใช้ค้นหา ISR address','หน้า 32'),
 ('Maskable interrupt','ถูก ignore ได้เมื่อระบบปิด interrupts ระหว่างจัดการ interrupt','หน้า 33'),
 ('Nonmaskable interrupt','ต้อง process เพื่อรักษาเสถียรภาพระบบ','หน้า 33'),
 ('MARIE input / output','poll InREG แล้วรับเข้า AC / วาง output ใน OutREG','หน้า 34'),
 ('ADD 105 ในตัวอย่าง','PC 101→102; IR 3105; MBR FFE9; AC 0023→000C','หน้า 35–36'),
 ('Store 106 จุดขัดกัน','binary หน้า 35 เริ่ม 0100 แต่ hex 4106 และตารางหน้า 22 ให้ Store opcode 0010: ต้องตรวจสอบจากต้นฉบับ','หน้า 22, 35'),
 ('Interrupt class: Program','เงื่อนไขจากการรัน instruction เช่น divide by zero','หน้า 37'),
 ('Interrupt class: Timer','timer ใน processor เพื่อให้ OS ทำงานเป็นระยะ','หน้า 37'),
 ('Interrupt class: I/O','I/O controller แจ้งเสร็จงาน/ขอ service/error','หน้า 37'),
 ('Interrupt class: Hardware failure','เช่น power failure หรือ memory parity error','หน้า 37'),
 ('Interrupt cycle','ตรวจ interrupt หลัง execute เมื่อเปิด interrupts','หน้า 40'),
 ('Long I/O wait','แม้มี interrupt processor ยังอาจต้องรอหลังทำงานอื่นช่วงหนึ่ง','หน้า 42'),
 ('Sequential interrupt processing','handler หนึ่งเสร็จก่อนจึงทำอีกตัว','หน้า 44'),
 ('Nested interrupt processing','handler ใหม่แทรกกลาง handler ปัจจุบัน แล้วกลับ','หน้า 44'),
]

data = dict(
 source=SOURCE, sourcePageCount=46,
 course='ITDS-211 · Computer Architecture & Operating System',
 instructor='W.Suntiamorntut, Ph.D.',
 chapter='Chapter02 · Computer Systems, Computer Functions, Processor Structure and Function',
 description='จากโมเดลเครื่องและ Bus ไปสู่ MARIE Instruction Processing และ Interrupt',
 notice='เนื้อหาบทนี้มีแผนภาพและตารางคำสั่งจำนวนมาก ควรเปิดภาพต้นฉบับประกอบ โดยเฉพาะ RTL, ADD 105 และ Interrupt มีสองจุดที่สไลด์ขัดกันเองและทำเครื่องหมายให้ตรวจสอบแล้ว',
 purpose='บทนี้เชื่อมภาพระบบคอมพิวเตอร์กับการทำงานทีละคำสั่ง: โมเดลและ bus พาข้อมูลไปยัง CPU/memory, MARIE ช่วยอ่าน register/ISA/RTL และส่วน interrupt อธิบายว่าระบบหยุดงานปัจจุบันไปบริการเหตุอื่นแล้วกลับมาทำต่ออย่างไร',
 purposePages='หน้า 3–15, 17–45',
 objectiveNote='วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ สไลด์ไม่มีรายการ Chapter Objectives แยกชัดเจน; เป้าหมายต่อไปนี้สรุปจากเนื้อหา',
 flashcardNote='Flashcard ใช้เฉพาะศัพท์ ขั้นตอน รหัส และตัวอย่างที่ปรากฏใน Chapter02; จุดที่สไลด์ขัดกันเองระบุให้ตรวจสอบ',
 goals=[
   dict(text='เปรียบเทียบ Von Neumann/Harvard และแยก bus lines กับวิธี arbitration',pages='หน้า 3–7'),
   dict(text='ติดตาม instruction cycle, PC/IR และข้อมูลผ่าน register ของระบบและ MARIE',pages='หน้า 10–20, 28–29'),
   dict(text='อ่าน MARIE ISA, bit pattern, RTL และ trace ADD 105 พร้อมแยกจุดขัดกันของเอกสาร',pages='หน้า 21–27, 35–36'),
   dict(text='อธิบายเหตุ/กลุ่ม interrupt, ISR, masking, I/O wait และ sequential/nested handling',pages='หน้า 30–34, 37–45'),
 ],
 limits=[
   'อ่านครบ 46 หน้า: หน้า 1 ปก หน้า 2 Course Outline หน้า 16 เปิดหัวข้อ Simple Computer Function และหน้า 46 Q & A ไม่มีเนื้อหาวิชาที่ต้องตั้งคำถามเพิ่ม',
   'ไม่พบรายการ Chapter Objectives แยกโดยตรง: ต้องตรวจสอบจากต้นฉบับ เป้าหมายข้างต้นเป็นสรุปจากเนื้อหา',
   'หน้า 21 เขียน MARIE มี 13 instructions แต่หน้า 22 แสดง 9 รายการเท่านั้น; รายชื่ออีก 4 รายการต้องตรวจสอบจากต้นฉบับ',
   'หน้า 24 ระบุ SKIPCOND field 10 เมื่อ AC > 0 แต่หน้า 27 RTL ให้ 11: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 35 binary Store 106 เริ่ม 0100 ขณะที่ hex เป็น 4106 และตารางหน้า 22 ให้ Store opcode 0010: ต้องตรวจสอบจากต้นฉบับ',
   'ภาพเครื่องสมมติหน้า 14 เป็นคนละ instruction table กับ MARIE หน้า 22; แยกรหัสสองชุดไว้ชัดเจน',
   'สไลด์หน้า 34 ไม่อธิบาย interrupt-driven I/O เชิงลึก และไม่มีข้อสอบเก่าหรือน้ำหนักสอบ จึงไม่อ้างว่าหัวข้อใดออกแน่นอน',
 ],
 figures=figures, topics=topics,
 roadmap=[
   dict(title='ตั้งภาพระบบก่อน',text='แยก Von Neumann/Harvard และเส้น bus ก่อนดู CPU',pages='หน้า 3–7',topic='computer-models'),
   dict(title='ตามคำสั่งเข้า CPU',text='ดู top-level, PC/IR, fetch/execute และ state diagram',pages='หน้า 8–15',topic='fetch-cycle'),
   dict(title='วาง register ของ MARIE',text='จำขนาด/หน้าที่ แล้วอ่าน architecture และ data path',pages='หน้า 17–20',topic='marie-registers'),
   dict(title='อ่านคำสั่งเป็น microoperations',text='ISA/bit pattern → RTL LOAD/ADD/SKIPCOND → fetch/decode/execute',pages='หน้า 21–29',topic='marie-isa'),
   dict(title='ฝึก trace ต้นฉบับ',text='ไล่ Load/Add/Store/Halt และตาราง ADD 105 โดยตรวจจุดขัดกัน',pages='หน้า 35–36',topic='marie-simple-program'),
   dict(title='ต่อด้วย Interrupt',text='เหตุและ ISR → class/masking → timing → sequential/nested',pages='หน้า 30–34, 37–45',topic='interrupt-entry'),
 ],
 plan=[
   dict(title='รอบ 1 · โมเดลและ Bus',task='อ่านหน้า 3–11 พร้อมชี้แผนภาพและจับคู่หน้าที่เส้น/การชิง bus',check='ตอบความต่าง Von Neumann/Harvard และ bus 3 เส้น/4 arbitration ได้',pages='หน้า 3–11'),
   dict(title='รอบ 2 · Instruction Cycle',task='ไล่ PC→IR→execute และภาพเครื่องสมมติ โดยแยก ISA ออกจาก MARIE',check='อธิบาย fetch/execute และค่าตัวอย่าง AC 0005 ได้',pages='หน้า 12–15'),
   dict(title='รอบ 3 · MARIE',task='ท่อง register และอ่าน ISA/bit fields/RTL จากภาพ',check='เขียน LOAD/ADD RTL ได้และชี้ความขัดกัน SKIPCOND ได้',pages='หน้า 17–29'),
   dict(title='รอบ 4 · Trace',task='ทำตาราง ADD 105 โดยปิดเฉลยก่อน แล้วเทียบ register ทีละแถว',check='ได้ AC 000C และอธิบาย PC/IR/MAR/MBR ตลอด trace ได้',pages='หน้า 35–36'),
   dict(title='รอบ 5 · Interrupt',task='ฝึกแยกเหตุ/class, ISR, masking, timing และ nested ด้วยภาพ',check='ไล่เส้นทาง interrupt และแยก long wait กับ short wait ได้',pages='หน้า 30–34, 37–45'),
   dict(title='รอบ 6 · ทดสอบรวม',task='สุ่มคำถามทุกหัวข้อ ทำ Flashcard แล้วกลับไปดูภาพ/หน้าที่ตอบผิด',check='ตอบแบบฝึกครบและทวนสองจุดที่ต้องตรวจสอบจากต้นฉบับ',pages='หน้า 3–45'),
 ],
 cram=[
   dict(title='ถ้าเหลือ 3 วัน',text='วัน 1 โมเดล/Bus/วงจรคำสั่ง หน้า 3–15; วัน 2 MARIE register/ISA/RTL/trace หน้า 17–29, 35–36; วัน 3 interrupt หน้า 30–34, 37–45 และทำแบบฝึก/ทวนจุดผิด'),
   dict(title='ถ้าเหลือ 1 วัน',text='เริ่ม MARIE register→ISA→RTL→trace หน้า 17–29, 35–36; ต่อ ISR/class/masking/nested หน้า 30–34, 37, 44–45; ปิดท้ายโมเดล/Bus หน้า 3–7 และ timing หน้า 41–42'),
   dict(title='ถ้าเหลือ 3 ชั่วโมง',text='0–25 นาที โมเดล/Bus หน้า 3–7; 25–55 นาที PC/IR/MARIE registers หน้า 10–20; 55–110 นาที ISA/RTL/trace หน้า 21–29, 35–36; 110–155 นาที ISR/class/timing/nested หน้า 30–34, 37–45; 155–180 นาทีสุ่มคำถามและทวนจุดผิด'),
 ],
 strategyIntro='ให้เวลากับ register, ISA/RTL, trace และ interrupt ก่อน เพราะสไลด์ให้ขั้นตอน/ภาพ/ตารางละเอียด เป็นการประเมินเพื่อจัดเวลาอ่าน ไม่ใช่การทำนายข้อสอบจริง',
 strategy=[
   dict(title='ควรท่องจำ',text='ชื่อ/หน้าที่ MAR, MBR, PC, IR, MARIE 7 registers, bus lines/arbitration, opcode ที่ตารางแสดง, class interrupt (หน้า 5–7, 10, 17, 22, 37)'),
   dict(title='ควรเข้าใจแนวคิด',text='ทางเดิน instruction/operand, ISR save–branch–restore, short/long wait และ sequential/nested (หน้า 12–15, 28–34, 38–45)'),
   dict(title='ควรฝึกแก้โจทย์',text='อ่าน bit fields/RTL และ trace ADD 105 ตามต้นฉบับ ระบุ PC/IR/MAR/MBR/AC ทีละขั้น; แยกจุดขัดกันก่อนใช้รหัส (หน้า 21–27, 35–36)'),
   dict(title='เตรียมข้อสอบแบบผสม',text='เลือกตอบจับคู่คำศัพท์/rules; อัตนัยอธิบายขั้น; วิเคราะห์ภาพและเปรียบเทียบ; คำนวณ/trace เฉพาะตัวอย่างที่อยู่ในสไลด์ ไม่อ้างว่าเป็นข้อสอบจริง'),
 ],
 flashcards=[dict(front=front,back=back,pages=pages) for front,back,pages in flashcards],
)

assert len({t['id'] for t in topics}) == len(topics)
assert all(len(t['questions']) == 3 for t in topics)
assert len({f['id'] for f in figures}) == len(figures)
assert all(f['id'] in {fig for t in topics for fig in t['figures']} for f in figures)
(ROOT / 'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(topics), len(figures), len(flashcards))
