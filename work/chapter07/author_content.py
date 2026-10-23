"""Chapter07 notes, questions and figure map from the supplied 53-page PDF."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = 'itds-211_comp_arch_Chapter07.pdf'
topics = []


def add(id, title, level, pages, summary, remember, terms, example, confusion, mnemonic, quiz, image_pages=(), comparison=None, formulas=None, worked=None):
    assert len(quiz) == 3
    m, a, b = quiz
    questions = [
        dict(type='เลือกตอบ', q=m[0], options=m[1], correct=m[2], answer=m[3], pages=pages),
        dict(type='อัตนัย', q=a[0], answer=a[1], pages=pages),
        dict(type='คำนวณ' if any(x in b[0] for x in ('คำนวณ', 'จงหา', 'เท่าไร')) else 'วิเคราะห์', q=b[0], answer=b[1], pages=pages),
    ]
    entry = dict(id=id, title=title, level=level, pages=pages,
        reason={'core':'เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท',
                'important':'เป็นภาพการไหลของคำสั่งและการประยุกต์กลไกหลักกับคำสั่งจริง',
                'extra':'เป็นภาพรายละเอียดประกอบหรือข้อสรุปเชิงภาพรวม'}[level],
        summary=summary, remember=remember, terms=terms, example=example,
        confusion=confusion, mnemonic=mnemonic, questions=questions,
        figures=[f'fig-{p}' for p in image_pages])
    if comparison: entry['comparison'] = dict(headers=comparison[0], rows=comparison[1])
    if formulas: entry['formulas'] = formulas
    if worked: entry['worked'] = worked
    topics.append(entry)


add('pipelining-analogy','Pipelining analogy: ซักผ้าแบบซ้อนงาน','core','หน้า 3',
    'สไลด์อธิบาย pipelining ด้วยการซักผ้าที่ซ้อนขั้นตอนกัน (overlapping execution) ทำให้งานหลายชิ้นอยู่คนละขั้นพร้อมกัน. parallelism แบบนี้เพิ่มประสิทธิภาพ: งานซัก 4 load ใช้ speedup 8/3.5 ≈ 2.3 และถ้าทำต่อเนื่องไม่หยุด speedup จะเข้าใกล้จำนวนขั้น (number of stages).',
    ['Pipelined laundry = overlapping execution (หน้า 3)','Parallelism improves performance (หน้า 3)','4 loads: speedup = 8/3.5 = 2.3 (หน้า 3)','Non-stop: speedup ≈ 4 = number of stages (หน้า 3)'],
    ['pipelining','overlapping execution','parallelism','speedup','number of stages'],
    'ภาพหน้า 3 บนคือทำทีละ load (เรียงต่อกัน) ภาพล่างคือ load ถัดไปเริ่มเมื่อขั้นแรกว่าง',
    'สูตร non-stop บนสไลด์พิมพ์เป็น “2n/0.5n + 1.5 ≈ 4” ซึ่งต้องอ่านเป็นนิพจน์ตามภาพ; ความหมายที่สไลด์ยืนยันคือ speedup เข้าใกล้จำนวนขั้น',
    'ซ้อนขั้นได้กี่ขั้น เร็วขึ้นได้ราวเท่านั้น',
    [('เมื่องานไหลต่อเนื่องไม่หยุด speedup ของ pipeline เข้าใกล้ค่าใด?',['จำนวน stages','จำนวนคำสั่ง','1 เสมอ','ครึ่งหนึ่งของ stages'],0,'จำนวน stages (หน้า 3)'),
     ('อธิบายว่า pipelined laundry ทำให้เร็วขึ้นอย่างไร','ซ้อนขั้นตอนของงานคนละชิ้นให้ทำพร้อมกัน (overlapping execution) จึงเกิด parallelism'),
     ('คำนวณ speedup ของตัวอย่าง 4 loads จากเวลาที่สไลด์ให้ (8 กับ 3.5)','8/3.5 ≈ 2.3')],(3,),
    formulas=[dict(expr='Speedup (4 loads) = 8 / 3.5 ≈ 2.3',description='ตัวเลขตามตัวอย่างซักผ้าหน้า 3',pages='หน้า 3'),
              dict(expr='Non-stop speedup ≈ number of stages (≈ 4)',description='กรณีงานไหลต่อเนื่องจำนวนมากตามสไลด์',pages='หน้า 3')])

add('riscv-stages','RISC-V pipeline 5 ขั้น','core','หน้า 4',
    'RISC-V pipeline แบ่งการทำคำสั่งเป็น 5 ขั้น ขั้นละหนึ่ง step: IF ดึงคำสั่งจากหน่วยความจำ, ID ถอดรหัสและอ่าน register, EX คำนวณหรือคำนวณ address, MEM เข้าถึง operand ในหน่วยความจำ และ WB เขียนผลกลับ register. ชื่อขั้นเหล่านี้ใช้ต่อในทุกภาพและชื่อ pipeline register ของบท.',
    ['IF: Instruction fetch from memory (หน้า 4)','ID: Instruction decode & register read (หน้า 4)','EX: Execute operation or calculate address (หน้า 4)','MEM: Access memory operand (หน้า 4)','WB: Write result back to register (หน้า 4)'],
    ['IF','ID','EX','MEM','WB','stage'],
    'ld ใช้ครบ 5 ขั้น: fetch → decode/อ่าน register → คำนวณ address → อ่าน memory → เขียน register',
    'EX ของ load/store คือคำนวณ address ไม่ใช่การอ่าน memory; การอ่าน/เขียน memory เกิดใน MEM',
    'ดึง–ถอด–ทำ–จำ–เขียน (IF–ID–EX–MEM–WB)',
    [('ขั้นใดเขียนผลกลับ register?',['WB','MEM','EX','ID'],0,'WB (หน้า 4)'),
     ('ขั้น ID ทำอะไรบ้างตามสไลด์?','ถอดรหัสคำสั่ง (decode) และอ่าน register'),
     ('คำสั่ง ld ใช้ขั้น EX และ MEM ทำอะไรตามลำดับ?','EX คำนวณ address, MEM เข้าถึง (อ่าน) operand ในหน่วยความจำ')])

add('pipeline-performance','Pipeline performance: single-cycle เทียบ pipelined','core','หน้า 5–6',
    'สไลด์สมมติเวลา 100ps สำหรับอ่าน/เขียน register และ 200ps สำหรับขั้นอื่น. คำสั่งแต่ละชนิดใช้เวลารวมต่างกัน (ld 800ps, sd 700ps, R-format 600ps, beq 500ps) ดังนั้น single-cycle ต้องใช้ clock ยาวตามคำสั่งที่ช้าสุด Tc = 800ps ส่วน pipelined ใช้ Tc = 200ps ตามขั้นที่ช้าที่สุด.',
    ['Register read/write = 100ps; ขั้นอื่น = 200ps (หน้า 5)','ld 800ps, sd 700ps, R-format 600ps, beq 500ps (หน้า 5)','Single-cycle Tc = 800ps; Pipelined Tc = 200ps (หน้า 6)'],
    ['clock cycle time (Tc)','single-cycle datapath','pipelined datapath','ps (picosecond)'],
    'ในภาพหน้า 6 คำสั่ง ld ถัดไปเริ่มทุก 800ps ใน single-cycle แต่เริ่มทุก 200ps ใน pipelined',
    'Pipelined ไม่ได้ทำให้คำสั่งเดียวเสร็จเร็วขึ้น แต่ทำให้คำสั่งถัดไปเริ่มได้ถี่ขึ้น',
    'single รอตัวช้าสุดทั้งคำสั่ง; pipeline รอขั้นช้าสุดขั้นเดียว',
    [('ตามหน้า 6 pipelined datapath มี Tc เท่าใด?',['200ps','100ps','500ps','800ps'],0,'200ps (หน้า 6)'),
     ('ทำไม single-cycle จึงมี Tc = 800ps?','clock ต้องยาวพอสำหรับคำสั่งที่ใช้เวลามากที่สุด คือ ld 800ps (หน้า 5–6)'),
     ('คำนวณเวลารวมของ sd จากตารางหน้า 5','200 + 100 + 200 + 200 = 700ps (ไม่มี register write)')],(5,6),
    comparison=(['คำสั่ง','IF','Reg read','ALU','MEM','Reg write','รวม'],[['ld','200','100','200','200','100','800ps'],['sd','200','100','200','200','–','700ps'],['R-format','200','100','200','–','100','600ps'],['beq','200','100','200','–','–','500ps']]),
    formulas=[dict(expr='Single-cycle Tc = 800ps\nPipelined Tc = 200ps',description='ค่า Tc จากภาพหน้า 6; อัตราส่วนเวลาระหว่างการเริ่มคำสั่ง 800/200 = 4 คำนวณจากตัวเลขในสไลด์',pages='หน้า 6')])

add('isa-design','Pipelining และการออกแบบ ISA','important','หน้า 7',
    'RISC-V ISA ถูกออกแบบมาให้ทำ pipeline ได้ง่าย: ทุกคำสั่งยาว 32 บิต ทำให้ fetch และ decode ได้ในรอบเดียว (ต่างจาก x86 ที่ยาว 1–17 ไบต์), รูปแบบคำสั่งน้อยและสม่ำเสมอจึง decode และอ่าน register ได้ในขั้นเดียว, และใช้ load/store addressing จึงคำนวณ address ในขั้นที่ 3 แล้วเข้าถึง memory ในขั้นที่ 4.',
    ['All instructions are 32-bits (หน้า 7)','c.f. x86: 1- to 17-byte instructions (หน้า 7)','Few and regular formats → decode + read registers in one step (หน้า 7)','Load/store addressing → address ในขั้นที่ 3, memory ในขั้นที่ 4 (หน้า 7)'],
    ['ISA','instruction format','load/store addressing','x86'],
    'เทียบกับ x86 ที่ความยาวคำสั่งไม่คงที่ ทำให้ fetch/decode ในรอบเดียวยากกว่า',
    'ขั้นที่ 3 = EX (คำนวณ address) และขั้นที่ 4 = MEM ไม่ใช่กลับกัน',
    'ยาวเท่ากัน รูปแบบน้อย load/store ชัด → pipeline ง่าย',
    [('คำสั่ง RISC-V ทุกคำสั่งยาวเท่าใด?',['32 บิต','1–17 ไบต์','16 บิต','64 บิต'],0,'32 บิต (หน้า 7)'),
     ('รูปแบบคำสั่งที่น้อยและสม่ำเสมอช่วย pipeline อย่างไร?','decode และอ่าน register ได้ในขั้นเดียว'),
     ('ถ้า ISA มีคำสั่งยาวไม่เท่ากันแบบ x86 จะกระทบขั้นใดตามสไลด์?','การ fetch และ decode ในรอบเดียวทำได้ยากขึ้น (หน้า 7)')])

add('hazards-overview','Hazards 3 ชนิด','core','หน้า 8',
    'Hazard คือสถานการณ์ที่ทำให้เริ่มคำสั่งถัดไปในรอบถัดไปไม่ได้. สไลด์แบ่งเป็น structure hazard (ทรัพยากรที่ต้องใช้ไม่ว่าง), data hazard (ต้องรอคำสั่งก่อนหน้าอ่าน/เขียนข้อมูลให้เสร็จ) และ control hazard (การตัดสินใจ control ขึ้นกับคำสั่งก่อนหน้า).',
    ['Hazard = prevents starting the next instruction in the next cycle (หน้า 8)','Structure: required resource is busy (หน้า 8)','Data: wait for previous instruction’s data read/write (หน้า 8)','Control: control action depends on previous instruction (หน้า 8)'],
    ['hazard','structure hazard','data hazard','control hazard'],
    'ใช้ตารางเปรียบเทียบด้านล่างจับคู่ “สาเหตุ” กับชนิด hazard',
    'Data hazard เกี่ยวกับค่าข้อมูลที่ยังไม่พร้อม; control hazard เกี่ยวกับการเลือกคำสั่งถัดไป (เช่น branch)',
    'ของไม่ว่าง–ข้อมูลไม่พร้อม–ไม่รู้ทางไป',
    [('การที่ทรัพยากรที่ต้องใช้กำลังถูกใช้อยู่ คือ hazard ชนิดใด?',['Structure hazard','Data hazard','Control hazard','Load-use hazard'],0,'Structure hazard (หน้า 8)'),
     ('ให้นิยาม hazard ตามสไลด์','สถานการณ์ที่ทำให้เริ่มคำสั่งถัดไปในรอบถัดไปไม่ได้'),
     ('คำสั่ง branch ที่ยังไม่รู้ผลทำให้ fetch คำสั่งถัดไปไม่ได้ จัดเป็น hazard ชนิดใดและเพราะอะไร?','Control hazard เพราะการตัดสินใจ control ขึ้นกับผลของคำสั่งก่อนหน้า (หน้า 8, 14)')],
    comparison=(['ชนิด','สาเหตุตามสไลด์','ตัวอย่างในบท'],[['Structure','resource ไม่ว่าง','single memory (หน้า 9)'],['Data','รอข้อมูลจากคำสั่งก่อน','add x19 → sub ใช้ x19 (หน้า 10)'],['Control','control ขึ้นกับคำสั่งก่อน','branch (หน้า 14)']]))

add('structure-hazard','Structure hazard และการแยก memory','core','หน้า 9',
    'Structure hazard คือการแย่งใช้ทรัพยากร. ใน RISC-V pipeline ที่มี memory เดียว load/store ต้องเข้าถึงข้อมูล ทำให้ instruction fetch ต้อง stall ในรอบนั้นและเกิด pipeline “bubble”. ดังนั้น pipelined datapath ต้องแยก instruction/data memory หรือแยก instruction/data cache.',
    ['Conflict for use of a resource (หน้า 9)','Single memory: load/store data access ชน instruction fetch → stall/bubble (หน้า 9)','แก้ด้วย separate instruction/data memories หรือ caches (หน้า 9)'],
    ['structure hazard','stall','bubble','separate instruction/data memory','instruction/data cache'],
    'ถ้า ld อยู่ขั้น MEM พร้อมกับอีกคำสั่งอยู่ขั้น IF และมี memory เดียว ทั้งสองต้องใช้ memory ในรอบเดียวกัน',
    'Bubble คือรอบที่ไม่มีงานจริงจาก stall ไม่ใช่คำสั่งใหม่',
    'memory เดียวชนกัน → แยกคำสั่ง/ข้อมูล',
    [('วิธีแก้ structure hazard จาก single memory ตามสไลด์คืออะไร?',['แยก instruction/data memory หรือ cache','เพิ่ม forwarding','ทำนาย branch','เรียงโค้ดใหม่'],0,'แยก instruction/data memories หรือ caches (หน้า 9)'),
     ('อธิบายว่า single memory ทำให้เกิด bubble อย่างไร','load/store ต้องใช้ memory เพื่อเข้าถึงข้อมูล instruction fetch จึงต้อง stall ในรอบนั้น เกิด bubble'),
     ('ถ้า pipeline มี instruction cache และ data cache แยกกัน hazard แบบหน้า 9 ยังเกิดหรือไม่?','ไม่เกิดในกรณีนี้ เพราะ fetch กับ data access ไม่ต้องแย่ง memory เดียวกัน (หน้า 9)')])

add('data-hazard-forwarding','Data hazard และ forwarding (bypassing)','core','หน้า 10–11',
    'Data hazard เกิดเมื่อคำสั่งหนึ่งต้องรอการเข้าถึงข้อมูลของคำสั่งก่อนหน้า เช่น add x19,x0,x1 แล้ว sub x2,x19,x3 ต้องใช้ x19. ถ้ารอจนเขียน register ก็ต้องแทรก bubble หลายรอบ (ภาพหน้า 10). Forwarding (bypassing) ใช้ผลทันทีที่คำนวณเสร็จโดยไม่รอเก็บลง register แต่ต้องเพิ่มเส้นทางใน datapath.',
    ['ตัวอย่าง add x19,x0,x1 → sub x2,x19,x3 (หน้า 10)','Forwarding: use result when it is computed (หน้า 11)','Don’t wait for it to be stored in a register (หน้า 11)','Requires extra connections in the datapath (หน้า 11)'],
    ['data hazard','forwarding','bypassing','dependency','bubble'],
    'ภาพหน้า 11: ผลจาก EX ของ add x1,x2,x3 ส่งตรงเข้าขั้น EX ของ sub x4,x1,x5',
    'Forwarding ไม่ได้ลบ dependency แต่ส่งค่าเร็วขึ้น; บางกรณีก็ยังต้อง stall (ดูหน้า 12)',
    'ได้ผลแล้วส่งเลย ไม่ต้องรอเข้าทะเบียน',
    [('อีกชื่อหนึ่งของ forwarding คืออะไร?',['Bypassing','Flushing','Stalling','Branch prediction'],0,'Bypassing (หน้า 11)'),
     ('ข้อดีและต้นทุนของ forwarding ตามสไลด์คืออะไร?','ใช้ผลทันทีที่คำนวณได้ไม่ต้องรอเขียน register แต่ต้องเพิ่มการเชื่อมต่อใน datapath'),
     ('ใน add x19,x0,x1 และ sub x2,x19,x3 register ใดก่อ data hazard และเพราะอะไร?','x19 เพราะ sub ต้องอ่านค่าที่ add ยังไม่ได้เขียนกลับ (หน้า 10)')],(10,11))

add('load-use','Load-use data hazard','core','หน้า 12',
    'Forwarding ไม่สามารถกำจัด stall ได้ทุกครั้ง: ถ้าค่ายังคำนวณไม่ได้ในเวลาที่ต้องใช้ ก็ส่งย้อนเวลาไม่ได้ (“Can’t forward backward in time!”). ตัวอย่าง ld x1,0(x2) แล้ว sub x4,x1,x5 ต้องรอค่าจาก MEM จึงต้องมี bubble หนึ่งรอบก่อน forward.',
    ['Can’t always avoid stalls by forwarding (หน้า 12)','If value not computed when needed (หน้า 12)','Can’t forward backward in time (หน้า 12)','ตัวอย่าง ld x1,0(x2) → sub x4,x1,x5 (หน้า 12)'],
    ['load-use hazard','stall','forwarding'],
    'ภาพหน้า 12 ค่า x1 ได้หลัง MEM ของ ld จึงส่งให้ EX ของ sub ได้หลังแทรก bubble',
    'ld ได้ค่าใน MEM (ช้ากว่าคำสั่ง ALU ที่ได้ค่าใน EX) จึงต่างจาก data hazard ทั่วไปที่ forward ได้ทันที',
    'load ได้ของช้า ใช้ต่อทันทีต้องรอหนึ่งจังหวะ',
    [('ทำไม load-use hazard จึงแก้ด้วย forwarding อย่างเดียวไม่ได้?',['ค่ายังไม่ถูกคำนวณตอนที่ต้องใช้','memory มีอันเดียว','branch ยังไม่รู้ผล','register x0 เขียนไม่ได้'],0,'ค่ายังไม่ได้ตอนต้องใช้ — forward ย้อนเวลาไม่ได้ (หน้า 12)'),
     ('อธิบายประโยค “Can’t forward backward in time”','ค่าจาก ld พร้อมหลังขั้น MEM ซึ่งช้ากว่าเวลาที่คำสั่งถัดไปต้องใช้ใน EX จึงส่งย้อนไปไม่ได้ ต้อง stall'),
     ('ใน ld x1,0(x2) ตามด้วย sub x4,x1,x5 ต้องแทรก bubble กี่รอบตามภาพหน้า 12 ก่อน forward ได้?','1 รอบ (ภาพหน้า 12; สอดคล้องกับ 1-cycle stall หน้า 45)')],(12,))

add('code-scheduling','Code scheduling เพื่อหลบ stall','core','หน้า 13',
    'คอมไพเลอร์สามารถเรียงโค้ดใหม่ไม่ให้ใช้ผลของ load ในคำสั่งถัดไปทันที. ตัวอย่าง C code a = b + e; c = b + f; ลำดับเดิมมี stall 2 จุด ใช้ 13 cycles; เมื่อย้าย ld x4,16(x0) ขึ้นมาก่อน add ลดเหลือ 11 cycles.',
    ['Reorder code to avoid use of load result in the next instruction (หน้า 13)','ลำดับเดิม: 2 stalls, 13 cycles (หน้า 13)','ลำดับใหม่: ld x1, ld x2, ld x4, add, sd, add, sd = 11 cycles (หน้า 13)'],
    ['code scheduling','reorder','load-use','stall'],
    'ลำดับเดิม add x3,x1,x2 ใช้ x2 ทันทีหลัง ld x2 และ add x5,x1,x4 ใช้ x4 ทันทีหลัง ld x4 → 2 stalls',
    'การเรียงใหม่ต้องรักษาผลลัพธ์เดิม (a และ c ยังได้ค่าเดิม) ไม่ใช่สลับคำสั่งตามใจ',
    'โหลดไว้ก่อน ใช้ทีหลัง',
    [('หลังจัดลำดับโค้ดใหม่ในหน้า 13 ใช้กี่ cycles?',['11','13','9','15'],0,'11 cycles (หน้า 13)'),
     ('ระบุคู่คำสั่งในลำดับเดิมที่ทำให้ stall','ld x2,8(x0) → add x3,x1,x2 และ ld x4,16(x0) → add x5,x1,x4'),
     ('คำนวณจำนวน cycles ที่ประหยัดได้จากการจัดลำดับใหม่','13 − 11 = 2 cycles (เท่ากับจำนวน stall ที่หายไป)')],(13,),
    worked=[dict(title='ตัวอย่างจัดลำดับโค้ด (หน้า 13)',steps=['ลำดับเดิม: ld x1 · ld x2 · add x3,x1,x2 (stall) · sd x3 · ld x4 · add x5,x1,x4 (stall) · sd x5 = 13 cycles','ย้าย ld x4,16(x0) ขึ้นไปก่อน add x3,x1,x2','ไม่มีคำสั่งใดใช้ผล load ในคำสั่งถัดไปทันที → 11 cycles'],answer='ลดจาก 13 เหลือ 11 cycles',pages='หน้า 13')])

add('control-hazard','Control hazard และ stall on branch','core','หน้า 14–15',
    'Branch กำหนดการไหลของโปรแกรม การ fetch คำสั่งถัดไปจึงขึ้นกับผล branch และ pipeline อาจ fetch คำสั่งที่ถูกไม่ได้ขณะ branch ยังอยู่ขั้น ID. RISC-V จึงเพิ่ม hardware เพื่อเปรียบเทียบ register และคำนวณ target ตั้งแต่ขั้น ID. วิธีง่ายสุดคือ stall รอจนรู้ผล branch ก่อน fetch ต่อ (ภาพหน้า 15).',
    ['Fetching next instruction depends on branch outcome (หน้า 14)','Compare registers and compute target early → add hardware in ID (หน้า 14)','Stall on branch: wait until outcome determined (หน้า 15)'],
    ['control hazard','branch outcome','branch target','stall on branch'],
    'ภาพหน้า 15: add x4,x5,x6 → beq x1,x0,40 → or x7,x8,x9 ต้องรอ bubble ก่อน fetch or',
    'การย้ายการตัดสิน branch มาที่ ID ลดความล่าช้าได้แต่ไม่ได้ทำให้ไม่มีความล่าช้าเลย',
    'branch ยังไม่ชี้ทาง อย่าเพิ่งเดิน',
    [('RISC-V เพิ่ม hardware ใดใน ID เพื่อลด control hazard?',['เปรียบเทียบ register และคำนวณ target','forwarding unit','data cache','MEM/WB register'],0,'Compare registers + compute target ใน ID (หน้า 14)'),
     ('ทำไม pipeline จึงอาจ fetch คำสั่งที่ถูกไม่ได้หลัง branch?','ผล branch ยังไม่รู้เพราะ branch ยังอยู่ขั้น ID ขณะที่ต้อง fetch คำสั่งถัดไป'),
     ('จากภาพหน้า 15 ถ้าใช้ stall on branch คำสั่ง or x7,x8,x9 ถูก fetch เมื่อใด?','หลังจากรู้ผล branch แล้ว โดยมี bubble คั่นระหว่าง beq กับ or (ภาพหน้า 15)')],(15,))

add('branch-prediction','Branch prediction: static และ dynamic','core','หน้า 16–17',
    'pipeline ที่ยาวขึ้นรู้ผล branch ได้ช้า stall penalty จึงรับไม่ได้ จึงทำนายผล branch และ stall เฉพาะเมื่อทำนายผิด. RISC-V ทำนาย branch not taken แล้ว fetch คำสั่งถัดไปทันที. Static prediction ใช้พฤติกรรมทั่วไป (backward taken, forward not taken) ส่วน dynamic prediction ให้ hardware จดประวัติจริงของแต่ละ branch และปรับเมื่อทำนายผิด.',
    ['Predict outcome; only stall if prediction is wrong (หน้า 16)','RISC-V: predict branches not taken (หน้า 16)','Static: backward taken, forward not taken (หน้า 17)','Dynamic: record recent history; when wrong, stall, re-fetch, update history (หน้า 17)'],
    ['branch prediction','predict not taken','static branch prediction','dynamic branch prediction','branch history'],
    'branch ของ loop มักกระโดดย้อนกลับ (backward) จึงทำนายว่า taken ตาม static prediction',
    'Static ไม่ได้ดูประวัติจริง; dynamic อาศัยประวัติที่ hardware วัด',
    'ย้อนกลับ=กระโดด, ไปข้างหน้า=ไม่กระโดด; dynamic จำประวัติ',
    [('Static branch prediction ทำนาย backward branch อย่างไร?',['Taken','Not taken','สุ่ม','Stall เสมอ'],0,'Predict backward branches taken (หน้า 17)'),
     ('Dynamic branch prediction ทำอะไรเมื่อทำนายผิด?','stall ขณะ re-fetch และ update history (หน้า 17)'),
     ('เปรียบเทียบเมื่อใดที่ branch prediction ไม่มีค่าเสียเวลาใน RISC-V ตามหน้า 16','เมื่อทำนาย not taken แล้วถูก จะ fetch คำสั่งถัดจาก branch โดยไม่มี delay; stall เฉพาะตอนทำนายผิด')],
    comparison=(['แบบ','พื้นฐาน','กฎ/การทำงาน'],[['Static','typical branch behavior','backward → taken, forward → not taken'],['Dynamic','วัดพฤติกรรมจริงด้วย hardware','จด history, ทำนายตามแนวโน้ม, ผิดแล้ว re-fetch + update']]))

add('pipeline-summary','Pipeline summary: throughput และ latency','important','หน้า 18',
    'The BIG Picture: pipelining เพิ่มประสิทธิภาพด้วยการเพิ่ม instruction throughput โดยทำหลายคำสั่งขนานกัน แต่ latency ของแต่ละคำสั่งยังเท่าเดิม. pipeline ต้องรับมือ hazards (structure, data, control) และการออกแบบ instruction set มีผลต่อความซับซ้อนของการ implement pipeline.',
    ['Increase instruction throughput (หน้า 18)','Each instruction has the same latency (หน้า 18)','Subject to structure, data, control hazards (หน้า 18)','ISA design affects pipeline complexity (หน้า 18)'],
    ['throughput','latency','The BIG Picture'],
    'เชื่อมกับหน้า 6: Tc ลดจาก 800 เป็น 200ps แต่คำสั่งหนึ่งยังผ่านครบ 5 ขั้น',
    'pipeline เพิ่ม throughput ไม่ได้ลด latency ของคำสั่งเดี่ยว',
    'ส่งงานออกถี่ขึ้น แต่งานชิ้นเดียวไม่ได้เสร็จเร็วขึ้น',
    [('Pipelining เพิ่มประสิทธิภาพด้วยการเพิ่มอะไร?',['Instruction throughput','Latency ของแต่ละคำสั่ง','จำนวน register','ขนาด memory'],0,'Instruction throughput (หน้า 18)'),
     ('Latency ของแต่ละคำสั่งเปลี่ยนไปอย่างไรเมื่อใช้ pipeline ตามสไลด์?','เท่าเดิม (same latency)'),
     ('ทำไม ISA design จึงสัมพันธ์กับความซับซ้อนของ pipeline? ยกตัวอย่างจากบท','เช่นความยาวคำสั่งคงที่ 32 บิตและรูปแบบน้อยของ RISC-V ทำให้ fetch/decode ในขั้นเดียวได้ (หน้า 7, 18)')])

add('pipelined-datapath','Pipelined datapath และ pipeline registers','core','หน้า 19–20',
    'Datapath แบ่งเป็นช่วง IF, ID, EX, MEM, WB. การไหลจากขวาไปซ้าย (right-to-left flow) คือ WB เขียน register และ MEM เลือก PC ใหม่ (branch) ซึ่งนำไปสู่ hazards. ต้องมี pipeline registers ระหว่างขั้น (IF/ID, ID/EX, EX/MEM, MEM/WB) เพื่อเก็บข้อมูลที่ขั้นก่อนหน้าผลิตในรอบก่อน.',
    ['Right-to-left flow leads to hazards (หน้า 19)','Need registers between stages (หน้า 20)','Hold information produced in previous cycle (หน้า 20)','ชื่อ pipeline registers: IF/ID, ID/EX, EX/MEM, MEM/WB (หน้า 20)'],
    ['pipelined datapath','pipeline register','IF/ID','ID/EX','EX/MEM','MEM/WB','right-to-left flow'],
    'ภาพหน้า 19 ชี้กล่อง MEM (ส่ง PC ใหม่ย้อนไป IF) และ WB (ส่งข้อมูลย้อนไป register file)',
    'ชื่อ pipeline register บอกขั้นสองฝั่ง เช่น ID/EX อยู่ระหว่าง ID กับ EX',
    'ย้อนทางเมื่อไร เสี่ยง hazard เมื่อนั้น',
    [('Pipeline register ระหว่างขั้น EX และ MEM ชื่ออะไร?',['EX/MEM','ID/EX','MEM/WB','IF/ID'],0,'EX/MEM (หน้า 20)'),
     ('Pipeline registers มีไว้ทำอะไร?','เก็บข้อมูลที่ขั้นก่อนหน้าผลิตไว้ในรอบก่อนเพื่อส่งต่อขั้นถัดไป'),
     ('จากหน้า 19 การไหลขวาไปซ้ายสองจุดคืออะไร และนำไปสู่อะไร?','WB เขียนกลับ register file และ MEM ส่งผล branch/PC กลับไป IF; นำไปสู่ hazards (data และ control)')],(19,20))

add('pipeline-operation-load','Pipeline operation ของ load และ datapath ที่แก้แล้ว','important','หน้า 21–27',
    'สไลด์ใช้ single-clock-cycle diagram ไล่ ld ทีละขั้น: IF (หน้า 22), ID (หน้า 23), EX (หน้า 24), MEM (หน้า 25), WB (หน้า 26). ใน WB ภาพชี้ว่าใช้ “wrong register number” เพราะหมายเลข register ปลายทางที่ใช้ตอนนั้นมาจากคำสั่งที่อยู่ใน IF/ID แล้ว. Corrected datapath (หน้า 27) จึงส่งหมายเลข write register ไปกับ pipeline registers จนถึง WB.',
    ['Single-clock-cycle diagram: แสดงการใช้ทรัพยากรในหนึ่งรอบ; multi-clock-cycle: กราฟตามเวลา (หน้า 21)','ld ผ่าน IF→ID→EX→MEM→WB (หน้า 22–26)','WB for Load: wrong register number (หน้า 26)','Corrected datapath ส่ง write register number ไปตาม pipeline (หน้า 27)'],
    ['single-clock-cycle diagram','multi-clock-cycle diagram','write register','corrected datapath'],
    'ดูส่วนที่ระบายสีฟ้าในภาพแต่ละหน้าเพื่อตามว่าขั้นนั้นใช้หน่วยใด',
    'ข้อผิดในหน้า 26 ไม่ได้อยู่ที่ข้อมูลที่เขียน แต่อยู่ที่หมายเลข register ปลายทาง',
    'หมายเลขปลายทางต้องเดินทางไปพร้อมคำสั่ง',
    [('ปัญหาที่หน้า 26 ชี้ใน WB for Load คืออะไร?',['Wrong register number','Wrong ALU result','Memory busy','Branch misprediction'],0,'Wrong register number (หน้า 26)'),
     ('Single-clock-cycle diagram ต่างจาก multi-clock-cycle diagram อย่างไร?','single แสดงการใช้ทรัพยากรของ pipeline ในหนึ่งรอบ; multi แสดงการทำงานตามเวลา (หน้า 21)'),
     ('วิเคราะห์ว่าทำไม corrected datapath (หน้า 27) แก้ปัญหาหน้า 26 ได้','ส่งหมายเลข write register ของ ld ผ่าน ID/EX, EX/MEM, MEM/WB จนถึง WB จึงเขียนถูก register (ภาพหน้า 27)')],(22,23,24,25,26,27))

add('pipeline-operation-store','Pipeline operation ของ store','important','หน้า 28–30',
    'sd ใช้ขั้น IF และ ID เหมือน load (หน้า 22–23) จากนั้น EX คำนวณ address (หน้า 28), MEM เขียนข้อมูลลง data memory (หน้า 29) และในขั้น WB ภาพหน้า 30 ไม่มีส่วนใดถูกระบายว่าใช้งาน สอดคล้องกับตารางหน้า 5 ที่ sd ไม่มี register write.',
    ['EX for Store: คำนวณ address (หน้า 28)','MEM for Store: เขียน data memory (หน้า 29)','WB for Store: ไม่ได้เขียน register (หน้า 30, ตารางหน้า 5)'],
    ['store (sd)','data memory write','write-back'],
    'เทียบหน้า 25 (ld อ่าน memory) กับหน้า 29 (sd เขียน memory)',
    'sd ยังผ่านขั้น WB ใน pipeline แต่ไม่ได้ทำงานเขียน register',
    'store จบงานที่ MEM',
    [('ขั้นใดที่ sd เขียนข้อมูลลงหน่วยความจำ?',['MEM','EX','WB','ID'],0,'MEM (หน้า 29)'),
     ('ขั้น WB ของ sd ทำอะไร?','ไม่มีการเขียน register (หน้า 30; ตารางหน้า 5 ช่อง Register write ของ sd ว่าง)'),
     ('เปรียบเทียบงานขั้น MEM ของ ld กับ sd','ld อ่านข้อมูลจาก data memory (หน้า 25) ส่วน sd เขียนข้อมูลลง data memory (หน้า 29)')],(28,29,30))

add('pipeline-diagrams','Multi-cycle และ single-cycle pipeline diagrams','important','หน้า 31–33',
    'Multi-cycle pipeline diagram มี 2 แบบ: แบบแสดงการใช้ทรัพยากร (IM, Reg, ALU, DM, Reg; หน้า 31) และแบบดั้งเดิมที่เขียนชื่อขั้นในแต่ละ clock cycle (หน้า 32) โดยตัวอย่างใช้ 5 คำสั่งใน CC1–CC9. Single-cycle pipeline diagram (หน้า 33) แสดงสถานะ pipeline ในรอบเดียว ซึ่งในตัวอย่างมี 5 คำสั่งอยู่ครบ 5 ขั้น.',
    ['Multi-cycle: form showing resource usage (หน้า 31)','Multi-cycle: traditional form (หน้า 32)','5 คำสั่งเสร็จใน CC1–CC9 ตามภาพ (หน้า 31–32)','Single-cycle: state of pipeline in a given cycle (หน้า 33)'],
    ['multi-cycle pipeline diagram','single-cycle pipeline diagram','clock cycle (CC)','IM','DM'],
    'หน้า 33: add x14 อยู่ IF, ld x13 อยู่ ID, add x12 อยู่ EX, sub x11 อยู่ MEM, ld x10 อยู่ WB',
    'multi-cycle มองข้ามเวลา (หลายรอบ) ส่วน single-cycle มองภาพนิ่งหนึ่งรอบ',
    'multi = ภาพยนตร์, single = ภาพถ่าย',
    [('Single-cycle pipeline diagram แสดงอะไร?',['สถานะ pipeline ในรอบหนึ่ง','การทำงานตลอดเวลา','จำนวน hazard','ขนาดคำสั่ง'],0,'State of pipeline in a given cycle (หน้า 33)'),
     ('Multi-cycle diagram มีกี่รูปแบบในสไลด์ และต่างกันอย่างไร?','2 แบบ: แสดงการใช้ทรัพยากร (หน้า 31) และแบบดั้งเดิมที่เขียนชื่อขั้น (หน้า 32)'),
     ('คำนวณจำนวน clock cycles ที่ 5 คำสั่งใช้จนเสร็จในภาพหน้า 32','9 cycles (CC1–CC9): 5 ขั้นของคำสั่งแรก + อีก 4 คำสั่งเพิ่มคำสั่งละ 1 รอบ')],(31,32,33),
    comparison=(['Diagram','มุมมอง','หน้า'],[['Multi-cycle (resource usage)','หลายรอบ แสดง IM/Reg/ALU/DM','31'],['Multi-cycle (traditional)','หลายรอบ เขียนชื่อขั้น','32'],['Single-cycle','สถานะในหนึ่งรอบ','33']]))

add('pipelined-control','Pipelined control (simplified)','extra','หน้า 34',
    'ภาพหน้า 34 เพิ่มสัญญาณควบคุมลงใน pipelined datapath: RegWrite ที่ register file, ALUSrc และ ALU control/ALUOp ในขั้น EX, Branch กับ Zero เข้าสู่ gate ที่สร้าง PCSrc, MemWrite/MemRead ที่ data memory และ MemtoReg ที่ mux ขั้น WB. รายละเอียดค่าสัญญาณแต่ละคำสั่งไม่มีในสไลด์นี้.',
    ['ภาพแสดง PCSrc, Branch, RegWrite, ALUSrc, ALUOp, MemWrite, MemRead, MemtoReg (หน้า 34)','Branch และ Zero รวมกันเพื่อกำหนด PCSrc (ภาพหน้า 34)','ค่าสัญญาณรายคำสั่ง: ต้องตรวจสอบจากต้นฉบับ'],
    ['RegWrite','ALUSrc','ALUOp','MemWrite','MemRead','MemtoReg','Branch','PCSrc'],
    'ไล่สัญญาณสีฟ้าในภาพตามตำแหน่งขั้น: EX (ALUSrc/ALUOp), MEM (Branch/MemWrite/MemRead), WB (MemtoReg)',
    'MemtoReg เลือกค่าที่เขียนกลับ register (จาก memory หรือ ALU) ไม่ใช่สัญญาณเขียน memory',
    'EX เลือก operand, MEM ตัดสินหน่วยความจำ/branch, WB เลือกค่าเขียนกลับ',
    [('สัญญาณใดอยู่ที่ data memory ในภาพหน้า 34?',['MemWrite และ MemRead','ALUSrc','RegWrite','MemtoReg'],0,'MemWrite และ MemRead (หน้า 34)'),
     ('PCSrc ในภาพเกิดจากสัญญาณใด?','Branch ร่วมกับ Zero จาก ALU (ภาพหน้า 34)'),
     ('วิเคราะห์ว่า MemtoReg อยู่ในขั้นใดและทำหน้าที่อะไรตามภาพ','อยู่ที่ mux ขั้น WB เลือกว่าจะเขียนกลับ register ด้วยข้อมูลจาก memory หรือผล ALU (ภาพหน้า 34)')],(34,))

add('alu-dependencies','Data hazards ในคำสั่ง ALU และ dependencies','core','หน้า 35–36',
    'ลำดับ sub x2,x1,x3; and x12,x2,x5; or x13,x6,x2; add x14,x2,x2; sd x15,100(x2) ทุกคำสั่งหลังจาก sub ใช้ x2. ภาพหน้า 36 แสดงค่า x2 = 10 ใน CC1–CC4, 10/−20 ใน CC5 และ −20 ตั้งแต่ CC6. เส้นแดงคือ dependency ที่ย้อนเวลา (and, or) ต้องแก้ด้วย forwarding; คำถามต่อไปคือจะตรวจจับเมื่อใดต้อง forward.',
    ['ลำดับคำสั่ง sub/and/or/add/sd ใช้ x2 (หน้า 35)','We can resolve hazards with forwarding (หน้า 35)','ค่า x2: 10 (CC1–4), 10/−20 (CC5), −20 (CC6–9) (หน้า 36)','and และ or ต้องการค่าก่อน sub เขียนกลับ (เส้นแดง หน้า 36)'],
    ['dependency','forwarding','register x2','clock cycle'],
    'and อ่าน x2 ใน CC3 และ or อ่านใน CC4 ก่อน sub เขียนเสร็จ (CC5) จึงต้อง forward; add อ่านใน CC5 และ sd ใน CC6',
    'add x14 ใน CC5 ถูกวาดอ่านจาก register file ไม่ใช่เส้นแดง — ค่า 10/−20 หมายถึงค่าเปลี่ยนในรอบนั้น',
    'ย้อนเวลา=เส้นแดง=ต้อง forward',
    [('ในภาพหน้า 36 ค่า x2 ใน CC6 เป็นเท่าใด?',['−20','10','10/−20','0'],0,'−20 (หน้า 36)'),
     ('คำสั่งใดในลำดับหน้า 35 ที่ต้องใช้ forwarding ตามเส้นแดงในหน้า 36?','and x12,x2,x5 และ or x13,x6,x2'),
     ('วิเคราะห์ทำไม sd x15,100(x2) ไม่มีเส้นแดงในภาพหน้า 36','sd อ่าน x2 หลัง CC5 ที่ sub เขียนค่า −20 แล้ว จึงอ่านค่าใหม่จาก register ได้โดยไม่ย้อนเวลา')],(36,))

add('forward-detection','การตรวจจับว่าต้อง forward','core','หน้า 37–38',
    'ส่งหมายเลข register ไปตาม pipeline เช่น ID/EX.RegisterRs1. operand ของ ALU ในขั้น EX คือ ID/EX.RegisterRs1 และ ID/EX.RegisterRs2. data hazard เกิดเมื่อ Rd ใน EX/MEM (เงื่อนไข 1a/1b) หรือ MEM/WB (2a/2b) ตรงกับ Rs1/Rs2 นั้น แต่จะ forward ก็ต่อเมื่อคำสั่งนั้นเขียน register (RegWrite) และ Rd ไม่ใช่ x0.',
    ['1a. EX/MEM.RegisterRd = ID/EX.RegisterRs1 (หน้า 37)','1b. EX/MEM.RegisterRd = ID/EX.RegisterRs2 (หน้า 37)','2a. MEM/WB.RegisterRd = ID/EX.RegisterRs1; 2b. … = Rs2 (หน้า 37)','ต้องมี RegWrite และ RegisterRd ≠ 0 (หน้า 38)'],
    ['ID/EX.RegisterRs1','ID/EX.RegisterRs2','EX/MEM.RegisterRd','MEM/WB.RegisterRd','RegWrite','x0'],
    'ลำดับหน้า 35: sub x2 → and x12,x2,x5 ตรงเงื่อนไข 1a (EX/MEM.Rd = x2 = ID/EX.Rs1)',
    '1x = forward จาก EX/MEM, 2x = forward จาก MEM/WB; a = Rs1, b = Rs2',
    'ตรงชื่อ + เขียนจริง + ไม่ใช่ x0 = forward',
    [('เงื่อนไข 2b ตามหน้า 37 คือข้อใด?',['MEM/WB.RegisterRd = ID/EX.RegisterRs2','EX/MEM.RegisterRd = ID/EX.RegisterRs1','EX/MEM.RegisterRd = ID/EX.RegisterRs2','MEM/WB.RegisterRd = ID/EX.RegisterRs1'],0,'MEM/WB.RegisterRd = ID/EX.RegisterRs2 (หน้า 37)'),
     ('ทำไมต้องตรวจ RegisterRd ≠ 0 ก่อน forward?','เพราะ x0 ไม่ใช่ผลที่ต้องส่งต่อ สไลด์กำหนดให้ forward เฉพาะเมื่อ Rd ไม่ใช่ x0 (หน้า 38)'),
     ('sub x2,x1,x3 แล้ว or x13,x6,x2 (ห่างกัน 1 คำสั่ง) ตรงเงื่อนไขใด?','2b: MEM/WB.RegisterRd (x2) = ID/EX.RegisterRs2 (x2) — forward จาก MEM/WB (หน้า 35–37)')],(37,),
    formulas=[dict(expr='EX hazard: EX/MEM.RegWrite and EX/MEM.RegisterRd ≠ 0\n  and EX/MEM.RegisterRd = ID/EX.RegisterRs1 (หรือ Rs2)\nMEM hazard: MEM/WB.RegWrite and MEM/WB.RegisterRd ≠ 0\n  and MEM/WB.RegisterRd = ID/EX.RegisterRs1 (หรือ Rs2)',description='รวมเงื่อนไข 1a–2b หน้า 37 กับข้อกำหนด RegWrite/Rd≠0 หน้า 38',pages='หน้า 37–38')])

add('forwarding-paths','Forwarding paths และ ForwardA/ForwardB','core','หน้า 39–40',
    'Forwarding unit ควบคุม mux สองตัวหน้า ALU ด้วย ForwardA (operand แรก) และ ForwardB (operand ที่สอง). ค่า 00 = มาจาก register file (ID/EX), 10 = forward ผล ALU ก่อนหน้า (EX/MEM), 01 = forward จาก data memory หรือผล ALU ก่อนหน้านั้น (MEM/WB).',
    ['ForwardA/B = 00 → ID/EX (register file) (หน้า 40)','= 10 → EX/MEM (prior ALU result) (หน้า 40)','= 01 → MEM/WB (data memory หรือ earlier ALU result) (หน้า 40)','Forwarding unit รับ Rs1/Rs2 และ EX/MEM.RegisterRd, MEM/WB.RegisterRd (ภาพหน้า 39)'],
    ['forwarding unit','ForwardA','ForwardB','mux'],
    'sub x2 → and x12,x2,x5: x2 เป็น operand แรกและอยู่ใน EX/MEM → ForwardA = 10',
    'ระวังสลับ 10 กับ 01: 10 = EX/MEM (ใหม่กว่า), 01 = MEM/WB',
    '10 ใกล้ (EX/MEM), 01 ไกล (MEM/WB), 00 ไม่ forward',
    [('ForwardB = 10 หมายถึงอะไร?',['operand ที่สองมาจากผล ALU ก่อนหน้า (EX/MEM)','operand แรกจาก register file','operand ที่สองจาก MEM/WB','ไม่มีการ forward'],0,'Second ALU operand forwarded from prior ALU result, EX/MEM (หน้า 40)'),
     ('ForwardA = 01 ส่งข้อมูลจากที่ใด?','MEM/WB: จาก data memory หรือผล ALU ก่อนหน้านั้น (หน้า 40)'),
     ('ในลำดับหน้า 35 คำสั่ง or x13,x6,x2 ควรได้ ForwardB เป็นอะไร?','01 — x2 เป็น operand ที่สองและค่าจาก sub อยู่ใน MEM/WB ตอน or อยู่ EX (หน้า 35–37, 40)')],(39,40),
    comparison=(['Mux control','Source','ความหมาย'],[['00','ID/EX','จาก register file'],['10','EX/MEM','forward จากผล ALU ก่อนหน้า'],['01','MEM/WB','forward จาก data memory หรือผล ALU ก่อนหน้านั้น']]))

add('double-data-hazard','Double data hazard และ revised forwarding condition','core','หน้า 41–43',
    'ลำดับ add x1,x1,x2; add x1,x1,x3; add x1,x1,x4 ทำให้เกิดทั้ง EX hazard และ MEM hazard พร้อมกันสำหรับคำสั่งที่สาม. ต้องใช้ค่าล่าสุด จึงแก้เงื่อนไข MEM hazard ให้ forward จาก MEM/WB เฉพาะเมื่อเงื่อนไข EX hazard ไม่เป็นจริง. ภาพหน้า 43 แสดง datapath ที่มี forwarding unit.',
    ['Both hazards occur → want the most recent (หน้า 41)','Only fwd (MEM) if EX hazard condition isn’t true (หน้า 41)','Revised condition เพิ่ม and not(EX/MEM.RegWrite and EX/MEM.RegisterRd ≠ 0 and EX/MEM.RegisterRd = ID/EX.RegisterRs1) (หน้า 42)','Datapath with forwarding (หน้า 43)'],
    ['double data hazard','EX hazard','MEM hazard','most recent value'],
    'คำสั่งที่ 3 ใช้ x1: ค่าใน EX/MEM (จากคำสั่งที่ 2) ใหม่กว่าใน MEM/WB (จากคำสั่งที่ 1) จึงต้องเลือก EX/MEM',
    'ถ้าไม่แก้เงื่อนไข จะ forward ค่าเก่าจาก MEM/WB ผิด',
    'สองทางชนกัน เลือกค่าใหม่สุด (EX/MEM)',
    [('ใน double data hazard ต้องเลือกค่าจากที่ใด?',['ค่าล่าสุด (EX/MEM)','ค่าเก่าสุด (MEM/WB)','register file','สุ่ม'],0,'Most recent — EX/MEM (หน้า 41)'),
     ('Revised MEM hazard condition เพิ่มเงื่อนไขอะไร?','forward จาก MEM/WB เฉพาะเมื่อ EX hazard condition ไม่เป็นจริง (หน้า 41–42)'),
     ('ในลำดับ add x1,x1,x2 / add x1,x1,x3 / add x1,x1,x4 คำสั่งที่สามควรได้ ForwardA เป็นอะไร?','10 — เพราะ EX hazard เป็นจริง จึงใช้ค่าล่าสุดจาก EX/MEM (หน้า 40–42)')],(42,43),
    formulas=[dict(expr='if (MEM/WB.RegWrite and (MEM/WB.RegisterRd ≠ 0)\n  and not(EX/MEM.RegWrite and (EX/MEM.RegisterRd ≠ 0)\n          and (EX/MEM.RegisterRd = ID/EX.RegisterRs1))\n  and (MEM/WB.RegisterRd = ID/EX.RegisterRs1)) ForwardA = 01',description='ForwardB ใช้รูปแบบเดียวกันโดยเปลี่ยน Rs1 เป็น Rs2',pages='หน้า 42')])

add('load-use-detection','Load-use hazard detection และการ stall','core','หน้า 44–47',
    'ตรวจ load-use ตอนคำสั่งที่ใช้ค่าอยู่ขั้น ID โดยดู IF/ID.RegisterRs1/Rs2. hazard เกิดเมื่อ ID/EX.MemRead และ ID/EX.RegisterRd ตรงกับ register ต้นทางของคำสั่งใน IF/ID; ถ้าพบให้ stall และแทรก bubble. การ stall ทำโดยบังคับ control ใน ID/EX เป็น 0 (EX/MEM/WB ทำ nop) และห้ามอัปเดต PC กับ IF/ID ทำให้ decode และ fetch ซ้ำ; stall 1 รอบให้ ld อ่าน memory แล้ว forward ไป EX ได้.',
    ['Load-use hazard when ID/EX.MemRead and ID/EX.RegisterRd ตรงกับ IF/ID.RegisterRs1/Rs2 (หน้า 44)','Force control values in ID/EX to 0 → nop (หน้า 45)','Prevent update of PC and IF/ID (หน้า 45)','1-cycle stall แล้ว forward ไป EX (หน้า 45)','Hazard detection unit ใช้ PCWrite, IF/IDWrite (ภาพหน้า 47)'],
    ['hazard detection unit','MemRead','bubble','nop','PCWrite','IF/IDWrite'],
    'ภาพหน้า 46: ld x2,20(x1) แล้ว and x4,x2,x5 — and กลายเป็น nop (bubble) ตรงจุด “Stall inserted here” แล้ว and ถูกทำซ้ำในแถวถัดไป',
    'สไลด์หน้า 44 พิมพ์เงื่อนไขเป็น IF/ID.RegisterRs1 ทั้งสองครั้ง แต่ข้อความก่อนหน้ากล่าวถึง Rs1 และ Rs2 — วงเล็บที่สองควรเป็น Rs2 หรือไม่: ต้องตรวจสอบจากต้นฉบับ',
    'load อยู่ข้างหน้า ผู้ใช้ตามติด → ล้าง control เป็น 0 แล้วรอหนึ่งรอบ',
    [('การ stall pipeline ทำอะไรกับ PC และ IF/ID?',['ห้ามอัปเดต','ล้างเป็น 0','เพิ่มค่า 4','สลับค่า'],0,'Prevent update of PC and IF/ID register (หน้า 45)'),
     ('เขียนเงื่อนไข load-use hazard ตามสไลด์','ID/EX.MemRead and ((ID/EX.RegisterRd = IF/ID.RegisterRs1) or (ID/EX.RegisterRd = IF/ID.RegisterRs1[หรือ Rs2 — ต้องตรวจสอบจากต้นฉบับ])) (หน้า 44)'),
     ('ทำไม stall เพียง 1 รอบจึงพอสำหรับ ld ตามด้วยคำสั่งที่ใช้ผล?','หนึ่งรอบทำให้ขั้น MEM อ่านข้อมูลของ ld ได้ แล้ว forward ไปขั้น EX ของคำสั่งที่ใช้ (หน้า 45)')],(44,46,47),
    formulas=[dict(expr='Load-use hazard when\n  ID/EX.MemRead and\n  ((ID/EX.RegisterRd = IF/ID.RegisterRs1) or\n   (ID/EX.RegisterRd = IF/ID.RegisterRs1))',description='พิมพ์ตามสไลด์; วงเล็บที่สองซ้ำ Rs1 ทั้งที่หัวข้อกล่าวถึง Rs1, Rs2 — ต้องตรวจสอบจากต้นฉบับ',pages='หน้า 44')])

add('stalls-performance','Stalls และ performance','important','หน้า 48',
    'The BIG Picture: stall ลดประสิทธิภาพแต่จำเป็นเพื่อให้ได้ผลถูกต้อง. คอมไพเลอร์สามารถจัดลำดับโค้ดเพื่อหลบ hazard และ stall ได้ แต่ต้องรู้โครงสร้างของ pipeline.',
    ['Stalls reduce performance but are required for correct results (หน้า 48)','Compiler can arrange code to avoid hazards and stalls (หน้า 48)','Requires knowledge of the pipeline structure (หน้า 48)'],
    ['stall','compiler scheduling','correctness'],
    'เชื่อมกับหน้า 13: การจัดลำดับโค้ดลดจาก 13 เหลือ 11 cycles',
    'stall ไม่ใช่ข้อผิดพลาด แต่เป็นราคาของความถูกต้อง',
    'ช้าหน่อยแต่ถูก; คอมไพเลอร์ช่วยลดได้',
    [('ทำไมยังต้องมี stall แม้จะลดประสิทธิภาพ?',['เพื่อให้ได้ผลถูกต้อง','เพื่อลด latency','เพื่อเพิ่ม register','เพื่อทำนาย branch'],0,'Required to get correct results (หน้า 48)'),
     ('คอมไพเลอร์ช่วยลด stall ได้อย่างไร และต้องรู้อะไร?','จัดลำดับโค้ดหลบ hazard โดยต้องรู้โครงสร้าง pipeline (หน้า 48)'),
     ('ยกตัวอย่างจากบทที่คอมไพเลอร์ลด stall ได้ และผลลัพธ์เป็นอย่างไร','code scheduling หน้า 13: ย้าย ld x4 ขึ้นก่อน ลดจาก 13 เหลือ 11 cycles')])

add('branch-hazard-flush','Branch hazards: ตัดสินใน MEM และ flush','core','หน้า 49',
    'ถ้าผล branch ถูกตัดสินในขั้น MEM เมื่อ branch taken คำสั่งสามคำสั่งที่ fetch ตามมา (44 and, 48 or, 52 add) ต้องถูก flush โดยตั้ง control values เป็น 0 แล้ว PC ไปที่ 72 ld x4.',
    ['If branch outcome determined in MEM (หน้า 49)','Flush these instructions (set control values to 0) (หน้า 49)','ภาพ: 40 beq x1,x0,16 → flush 44, 48, 52 → 72 ld x4,100(x7) (หน้า 49)'],
    ['branch hazard','flush','control values = 0','PC'],
    'นับจากภาพ: คำสั่งที่ถูก flush มี 3 คำสั่งเมื่อ branch ตัดสินใน MEM',
    'ภาพหน้า 49 ใช้ beq x1,x0,16 และ ld x4,100(x7) แต่หน้า 50 ใช้ beq x1,x3,16 และ ld x4,50(x7): ตัวอย่างไม่ตรงกัน ต้องตรวจสอบจากต้นฉบับ',
    'ตัดสินช้า ทิ้งเยอะ',
    [('เมื่อ flush คำสั่ง สไลด์ทำอย่างไร?',['ตั้ง control values เป็น 0','ลบคำสั่งออกจาก memory','เพิ่ม PC เป็น 4','เขียน x0'],0,'Set control values to 0 (หน้า 49)'),
     ('ถ้าผล branch ตัดสินใน MEM จะเกิดอะไรกับคำสั่งที่ fetch หลัง branch เมื่อ branch taken?','ต้องถูก flush เพราะเป็นคำสั่งผิดทาง (หน้า 49)'),
     ('จากภาพหน้า 49 นับจำนวนคำสั่งที่ต้อง flush เท่าไร?','3 คำสั่ง: 44 and, 48 or, 52 add')],(49,))

add('reduce-branch-delay','Reducing branch delay: ย้ายการตัดสินไป ID','core','หน้า 50–52',
    'ย้าย hardware ที่ตัดสินผล branch ไปไว้ขั้น ID ได้แก่ target address adder และ register comparator. ตัวอย่าง branch taken: 40: beq x1,x3,16 เป็น PC-relative ไป 40 + 16×2 = 72. ภาพ Clock 3 (หน้า 51) มีสัญญาณ IF.Flush และ Clock 4 (หน้า 52) แสดง Bubble (nop) ตามด้วย ld x4,50(x7) ที่ PC 72.',
    ['Move hardware to determine outcome to ID: target address adder + register comparator (หน้า 50)','40: beq x1,x3,16 → target 40 + 16×2 = 72 (หน้า 50)','Clock 3: IF.Flush (หน้า 51)','Clock 4: Bubble (nop) แล้ว ld x4,50(x7) (หน้า 52)'],
    ['target address adder','register comparator','PC-relative branch','IF.Flush','bubble (nop)'],
    'เทียบกับหน้า 49: ตัดสินใน MEM ต้อง flush 3 คำสั่ง แต่ตัดสินใน ID ภาพหน้า 52 เหลือ bubble 1 ช่อง',
    'offset 16 ไม่ได้บวกตรง ๆ แต่คูณ 2 ตามสไลด์ (40 + 16×2)',
    'ตัดสินเร็วที่ ID ทิ้งแค่ตัวเดียว',
    [('Hardware ใดถูกย้ายไป ID เพื่อลด branch delay?',['Target address adder และ register comparator','Data memory','Forwarding unit','MEM/WB register'],0,'Target address adder + register comparator (หน้า 50)'),
     ('อธิบายเหตุการณ์ใน Clock 3 และ Clock 4 ของตัวอย่าง branch taken','Clock 3 สั่ง IF.Flush คำสั่งที่ fetch ผิดทาง; Clock 4 ช่องนั้นกลายเป็น bubble (nop) และ fetch ld x4,50(x7) ที่ 72 (หน้า 51–52)'),
     ('คำนวณ branch target ของ 40: beq x1,x3,16 ตามสไลด์','40 + 16×2 = 72')],(50,51,52),
    formulas=[dict(expr='Branch target = PC + offset × 2 = 40 + 16 × 2 = 72',description='ตัวอย่าง PC-relative branch ในหน้า 50',pages='หน้า 50')])

FIG = {
    3:('Pipelining Analogy','ภาพซักผ้าแบบเรียงกับแบบ pipeline พร้อม speedup 8/3.5 และ ≈ จำนวนขั้น'),
    5:('Pipeline Performance','ตารางเวลาแต่ละขั้นของ ld, sd, R-format, beq'),
    6:('Pipeline Performance','single-cycle Tc 800ps เทียบ pipelined Tc 200ps'),
    10:('Data Hazards','add x19 → sub ใช้ x19 พร้อม bubble ระหว่างรอ'),
    11:('Forwarding (aka Bypassing)','ส่งผลจาก EX ของ add ไปยัง EX ของ sub'),
    12:('Load-Use Data Hazard','ld → sub ต้องมี bubble ก่อน forward'),
    13:('Code Scheduling to Avoid Stalls','จัดลำดับโค้ดจาก 13 cycles เหลือ 11 cycles'),
    15:('Stall on Branch','beq รอผลก่อน fetch คำสั่ง or พร้อม bubble'),
    19:('RISC-V Pipelined Datapath','datapath 5 ขั้นและการไหลขวาไปซ้ายที่ทำให้เกิด hazard'),
    20:('Pipeline registers','IF/ID, ID/EX, EX/MEM, MEM/WB ระหว่างขั้น'),
    22:('IF for Load, Store, …','ขั้น IF: instruction memory และ PC'),
    23:('ID for Load, Store, …','ขั้น ID: อ่าน register และ imm gen'),
    24:('EX for Load','ขั้น EX ของ ld: คำนวณ address'),
    25:('MEM for Load','ขั้น MEM ของ ld: อ่าน data memory'),
    26:('WB for Load','ขั้น WB ของ ld ชี้ wrong register number'),
    27:('Corrected Datapath for Load','ส่ง write register number ไปตาม pipeline'),
    28:('EX for Store','ขั้น EX ของ sd: คำนวณ address'),
    29:('MEM for Store','ขั้น MEM ของ sd: เขียน data memory'),
    30:('WB for Store','ขั้น WB ของ sd ไม่มีการเขียน register'),
    31:('Multi-Cycle Pipeline Diagram','แบบแสดงการใช้ทรัพยากร IM/Reg/ALU/DM'),
    32:('Multi-Cycle Pipeline Diagram','แบบดั้งเดิมเขียนชื่อขั้นใน CC1–CC9'),
    33:('Single-Cycle Pipeline Diagram','สถานะ 5 คำสั่งในรอบเดียว'),
    34:('Pipelined Control (Simplified)','สัญญาณควบคุม RegWrite, ALUSrc, ALUOp, Branch, PCSrc, MemWrite, MemRead, MemtoReg'),
    36:('Dependencies & Forwarding','ค่า x2 แต่ละรอบและเส้น dependency ที่ต้อง forward'),
    37:('Detecting the Need to Forward','เงื่อนไข 1a/1b/2a/2b'),
    39:('Forwarding Paths','forwarding unit และ mux ForwardA/ForwardB'),
    40:('Forwarding Conditions','ตารางค่า ForwardA/ForwardB 00/10/01'),
    42:('Revised Forwarding Condition','เงื่อนไข MEM hazard ที่แก้แล้ว'),
    43:('Datapath with Forwarding','datapath ที่มี forwarding unit'),
    44:('Load-Use Hazard Detection','เงื่อนไขตรวจ load-use ใน ID'),
    46:('Load-Use Data Hazard','and กลายเป็น nop และ stall inserted'),
    47:('Datapath with Hazard Detection','hazard detection unit, PCWrite, IF/IDWrite'),
    49:('Branch Hazards','ตัดสิน branch ใน MEM และ flush 3 คำสั่ง'),
    50:('Reducing Branch Delay','ย้ายการตัดสินไป ID และตัวอย่าง target 72'),
    51:('Example: Branch Taken','Clock 3 พร้อม IF.Flush'),
    52:('Example: Branch Taken','Clock 4 มี bubble (nop) และ ld x4,50(x7)'),
}
figures=[]
for p,(title,caption) in FIG.items():
    figures.append(dict(id=f'fig-{p}',page=p,file=f'slide-{p:02d}.png',title=f'{title} · หน้า {p}',
                        caption=f'{caption} ({SOURCE}, หน้า {p})'))

flashcards=[dict(front=t['title'],back=t['remember'][0],pages=t['pages']) for t in topics]
term_cards=[
    ('IF / ID / EX / MEM / WB','fetch / decode+read reg / execute หรือ address / memory / write back','หน้า 4'),
    ('Single-cycle vs pipelined Tc','800ps vs 200ps','หน้า 6'),
    ('Hazard','สถานการณ์ที่เริ่มคำสั่งถัดไปในรอบถัดไปไม่ได้','หน้า 8'),
    ('Structure hazard','required resource is busy; แก้ด้วยแยก I/D memory หรือ cache','หน้า 8–9'),
    ('Data hazard','ต้องรอคำสั่งก่อนหน้าอ่าน/เขียนข้อมูลให้เสร็จ','หน้า 8, 10'),
    ('Control hazard','การตัดสินใจ control ขึ้นกับคำสั่งก่อนหน้า (branch)','หน้า 8, 14'),
    ('Forwarding / Bypassing','ใช้ผลทันทีที่คำนวณได้ ไม่รอเก็บลง register','หน้า 11'),
    ('Load-use hazard','ค่ายังไม่พร้อม ต้อง stall — forward ย้อนเวลาไม่ได้','หน้า 12'),
    ('Static prediction','backward taken, forward not taken','หน้า 17'),
    ('Dynamic prediction','hardware จด history ของแต่ละ branch','หน้า 17'),
    ('Throughput vs latency','pipeline เพิ่ม throughput; latency เท่าเดิม','หน้า 18'),
    ('ForwardA/B = 00','จาก register file (ID/EX)','หน้า 40'),
    ('ForwardA/B = 10','จาก EX/MEM (prior ALU result)','หน้า 40'),
    ('ForwardA/B = 01','จาก MEM/WB (data memory หรือ earlier ALU result)','หน้า 40'),
    ('Double data hazard','ใช้ค่าล่าสุด; MEM forward เฉพาะเมื่อ EX hazard ไม่จริง','หน้า 41–42'),
    ('Stall the pipeline','control ใน ID/EX = 0, ห้ามอัปเดต PC และ IF/ID','หน้า 45'),
    ('Flush','ตั้ง control values เป็น 0 ให้คำสั่งผิดทาง','หน้า 49'),
    ('Branch target ตัวอย่าง','40 + 16×2 = 72','หน้า 50'),
]
flashcards += [dict(front=f,back=b,pages=p) for f,b,p in term_cards]

data=dict(
    source=SOURCE,sourcePageCount=53,
    course='ITDS-211 · Computer Architecture & Operating System',
    instructor='W. Suntiamorntut, Ph.D.',
    chapter='Chapter07 · Computing Unit (Pipelining)',
    description='RISC-V pipeline 5 ขั้น, hazards, forwarding, stall และ branch prediction',
    notice='เลขหน้าเป็นหน้า PDF 1–53; หัวสไลด์พิมพ์ “Chapter 4 — The Processor — 29–81” ซึ่งเป็นเลขอีกชุด และมีจุดพิมพ์ไม่ตรงกันที่หน้า 44 และหน้า 49–50 ที่ต้องตรวจสอบจากต้นฉบับ',
    purpose='บทนี้เรียนเพื่อเข้าใจว่า pipelining ทำให้ CPU ทำคำสั่งซ้อนกันเพื่อเพิ่ม throughput อย่างไร, hazards แบบ structure/data/control เกิดจากอะไร และ datapath ของ RISC-V แก้ด้วย forwarding, stall, flush และ branch prediction อย่างไร',
    purposePages='หน้า 2–52',
    objectiveNote='วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจาก course outline หน้า 2 (computing units – Pipelining) และเนื้อหาหน้า 3–52',
    flashcardNote='Flashcards ใช้ศัพท์ เงื่อนไข และตัวเลขจากสไลด์เท่านั้น',
    goals=[
        dict(text='อธิบายแนวคิด pipelining, 5 ขั้นของ RISC-V และเทียบ Tc ของ single-cycle กับ pipelined',pages='หน้า 3–7, 18'),
        dict(text='จำแนก structure/data/control hazards และวิธีรับมือเบื้องต้น',pages='หน้า 8–17'),
        dict(text='ตามการไหลของ ld/sd ผ่าน pipelined datapath และ pipeline registers',pages='หน้า 19–34'),
        dict(text='เขียนเงื่อนไข forwarding, ค่า ForwardA/B และการตรวจ load-use hazard',pages='หน้า 35–48'),
        dict(text='อธิบาย branch hazard, flush และการย้ายการตัดสิน branch ไป ID',pages='หน้า 49–52')],
    limits=[
        'อ่านและตรวจภาพครบ 53 หน้า: หน้า 1 ปก, หน้า 2 course outline, หน้า 53 Q&A',
        'สไลด์ไม่มีรายการ Chapter Objectives โดยตรงหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; ระดับสีเป็นลำดับเวลาอ่าน ไม่ใช่สถิติการออกสอบ',
        'หน้า 44 เงื่อนไข load-use เขียน IF/ID.RegisterRs1 ซ้ำสองครั้ง (คาดว่าควรมี Rs2): ต้องตรวจสอบจากต้นฉบับ',
        'หน้า 49 ใช้ beq x1,x0,16 และ 72 ld x4,100(x7) ส่วนหน้า 50–52 ใช้ beq x1,x3,16 และ ld x4,50(x7): ต้องตรวจสอบจากต้นฉบับ',
        'สูตร non-stop speedup หน้า 3 พิมพ์ “2n/0.5n + 1.5 ≈ 4” ตามภาพ; การจัดวงเล็บของนิพจน์: ต้องตรวจสอบจากต้นฉบับ',
        'หน้า 34 แสดงเฉพาะตำแหน่งสัญญาณควบคุม ไม่มีตารางค่าสัญญาณรายคำสั่ง',
        'คำถามคำนวณใช้เฉพาะตัวเลขในสไลด์; ไม่มีการอ้างว่าเป็นข้อสอบจริง'],
    figures=figures,topics=topics,
    roadmap=[
        dict(title='1 · แนวคิด pipeline',text='analogy → 5 ขั้น → Tc 800 vs 200ps → ISA design',pages='หน้า 3–7',topic='pipelining-analogy'),
        dict(title='2 · Hazards ภาพรวม',text='structure/data/control → forwarding, load-use, code scheduling, branch stall/prediction',pages='หน้า 8–18',topic='hazards-overview'),
        dict(title='3 · Datapath',text='pipeline registers → ld/sd ทีละขั้น → diagrams → control signals',pages='หน้า 19–34',topic='pipelined-datapath'),
        dict(title='4 · Forwarding & stall',text='เงื่อนไข 1a–2b → ForwardA/B → double hazard → load-use detection',pages='หน้า 35–48',topic='alu-dependencies'),
        dict(title='5 · Control hazards',text='flush เมื่อตัดสินใน MEM → ย้ายไป ID → ตัวอย่าง branch taken',pages='หน้า 49–52',topic='branch-hazard-flush')],
    plan=[
        dict(title='รอบ 1 · แนวคิดและตัวเลข',task='อ่านหน้า 3–7; เขียน 5 ขั้นและคำนวณเวลา ld/sd/R/beq จากตารางหน้า 5',check='บอก Tc 800/200ps และอธิบาย throughput vs latency ได้',pages='หน้า 3–7, 18'),
        dict(title='รอบ 2 · Hazards',task='ทำตาราง 3 hazard ด้วยตัวเอง; อธิบาย forwarding, load-use และไล่ code scheduling 13→11 cycles',check='ชี้คู่คำสั่งที่ stall ในหน้า 13 ได้ และแยก static/dynamic prediction',pages='หน้า 8–17'),
        dict(title='รอบ 3 · Datapath',task='วาด 4 pipeline registers และไล่ ld/sd ทีละขั้นตามภาพ',check='อธิบาย wrong register number และ diagram แบบ single/multi ได้',pages='หน้า 19–34'),
        dict(title='รอบ 4 · เงื่อนไข forwarding/stall',task='เขียนเงื่อนไข 1a–2b, ตาราง ForwardA/B, revised condition และ load-use จากความจำ',check='ตั้งค่า ForwardA/B ให้ลำดับหน้า 35 และ 41 ได้ถูก',pages='หน้า 35–48'),
        dict(title='รอบ 5 · Branch และสุ่ม Quiz',task='เทียบ flush 3 คำสั่ง (MEM) กับ bubble 1 ช่อง (ID); ทำ Quiz ทุกหัวข้อ',check='คำนวณ target 72 และตอบหัวข้อแดงครบ',pages='หน้า 49–52')],
    cram=[
        dict(title='ถ้าเหลือ 3 วัน',text='วัน 1 หน้า 3–18; วัน 2 datapath หน้า 19–34; วัน 3 forwarding/stall/branch หน้า 35–52 และทำ Quiz'),
        dict(title='ถ้าเหลือ 1 วัน',text='5 ขั้นและ Tc หน้า 4–6 → hazards หน้า 8–17 → เงื่อนไข forward หน้า 37–42 → load-use หน้า 44–46 → branch หน้า 49–50'),
        dict(title='ถ้าเหลือ 3 ชั่วโมง',text='0–30 นาที หน้า 3–7; 30–75 นาที hazards หน้า 8–18; 75–135 นาที forwarding/load-use หน้า 35–47; 135–165 นาที branch หน้า 49–52; 165–180 นาทีสุ่ม Quiz')],
    strategyIntro='เน้นหัวข้อที่สไลด์ให้นิยาม เงื่อนไข และตัวอย่างโค้ด เช่น 5 stages, hazards, forwarding conditions, load-use และ branch; ไม่มีข้อสอบเก่าจึงไม่ยืนยันโอกาสออกจริง',
    strategy=[
        dict(title='ควรท่องจำ',text='IF/ID/EX/MEM/WB, นิยาม hazard 3 ชนิด, เงื่อนไข 1a–2b, ForwardA/B 00/10/01, วิธี stall และ flush (หน้า 4, 8, 37–45, 49)'),
        dict(title='ควรฝึกโจทย์',text='รวมเวลาคำสั่งตารางหน้า 5; speedup 8/3.5; นับ cycles 13→11; ระบุ ForwardA/B ของลำดับหน้า 35/41; target 40+16×2 (หน้า 3, 5, 13, 35–42, 50)'),
        dict(title='ควรเข้าใจแนวคิด',text='throughput vs latency, ทำไม load-use ต้อง stall, ทำไมต้องเลือกค่าล่าสุดใน double hazard, ทำไมย้าย branch ไป ID ลด flush (หน้า 12, 18, 41, 49–50)'),
        dict(title='เตรียมข้อสอบแบบผสม',text='เลือกตอบจับคู่ศัพท์/ขั้น; อัตนัยอธิบายกลไก; คำนวณตามตัวเลขสไลด์; วิเคราะห์ภาพ pipeline diagram และเงื่อนไข hazard (หน้า 3–52)')],
    flashcards=flashcards)

assert len(topics)==25 and len({t['id'] for t in topics})==25
assert all(len(t['questions'])==3 and t['pages'] and t['summary'] for t in topics)
assert set(f['id'] for f in figures)==set(fid for t in topics for fid in t['figures'])
assert all((HERE/f['file']).is_file() for f in figures)
(HERE/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('topics',len(topics),'figures',len(figures),'questions',sum(len(t['questions']) for t in topics),'flashcards',len(flashcards))
