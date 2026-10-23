"""Chapter05 study content derived from the supplied 52-page PDF only."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = 'itds-211_comp_arch_Chapter05.pdf'
topics = []

def add(id, title, level, pages, summary, remember, terms, example, confusion, mnemonic, quiz, image_pages=(), comparison=None):
    assert len(quiz) == 3
    m, a, b = quiz
    questions = [dict(type='เลือกตอบ',q=m[0],options=m[1],correct=m[2],answer=m[3],pages=pages),
                 dict(type='อัตนัย',q=a[0],answer=a[1],pages=pages),
                 dict(type='คำนวณ' if any(x in b[0] for x in ('คำนวณ','จงหา','เท่าไร')) else 'วิเคราะห์',q=b[0],answer=b[1],pages=pages)]
    entry = dict(id=id,title=title,level=level,pages=pages,
        reason={'core':'เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด',
                'important':'เป็นภาพเปรียบเทียบ ตัวอย่างการประยุกต์ หรือการเชื่อมกลไกหลัก',
                'extra':'เป็นอุปกรณ์หรือเทคโนโลยีตัวอย่างที่สไลด์ให้รายละเอียดประกอบ'}[level],
        summary=summary,remember=remember,terms=terms,example=example,
        confusion=confusion,mnemonic=mnemonic,questions=questions,
        figures=[f'fig-{p}' for p in image_pages])
    if comparison: entry['comparison']=dict(headers=comparison[0],rows=comparison[1])
    topics.append(entry)

add('io-model','I/O module และ external device','core','หน้า 3–5',
    'I/O module เชื่อม system bus กับ peripheral devices ผ่าน address, data และ control lines. External device แลกข้อมูลกับสิ่งแวดล้อมผ่าน link ไปยัง I/O module และแบ่งเป็น human readable, machine readable กับ communication. ภาพอุปกรณ์แสดง control logic, buffer และ transducer ที่แปลงข้อมูลระหว่างอุปกรณ์กับสิ่งแวดล้อม.',
    ['System bus มี address/data/control lines ต่อ I/O module (หน้า 3)','External devices มี 3 หมวด: human readable, machine readable, communication (หน้า 4)','อุปกรณ์ตัวอย่างมี control logic, buffer, transducer พร้อม data/status/control signals (หน้า 5)'],
    ['I/O module','system bus','peripheral device','control logic','buffer','transducer'],
    'ตามลูกศรหน้า 5: ข้อมูลจากสิ่งแวดล้อมผ่าน transducer/buffer ไปเป็น data bits ของ I/O module',
    'อย่าสับสน I/O module ที่เชื่อม bus กับ external device ที่แปลง/รับส่งข้อมูลจากสิ่งแวดล้อม',
    'bus → module → device → environment',
    [('อะไรเชื่อม system bus กับ peripheral?',['I/O module','transducer','application buffer','ISR'],0,'I/O module'),('สามกลุ่ม external device ในสไลด์คืออะไร?','human readable, machine readable และ communication'),('ภาพหน้า 5 แยกหน้าที่ control logic กับ transducer อย่างไร?','control logic รับสัญญาณควบคุม/รายงานสถานะ; transducer แปลงข้อมูลที่เกี่ยวกับสิ่งแวดล้อม')],(3,4,5))

add('io-functions','หน้าที่และโครงสร้างภายใน I/O module','core','หน้า 6–7',
    'I/O module ประสานการไหลของข้อมูลและเวลา สื่อสารกับ processor และ device จัด buffer ให้ความเร็วต่างกัน และตรวจ error. ภาพโครงสร้างมี data registers, status/control registers, I/O logic และ external-device interface logic เชื่อมกับ system bus และอุปกรณ์.',
    ['Control and timing ประสาน traffic; processor communication ถอด command รับ address/data/status (หน้า 6)','Device communication ส่ง command/status/data; buffering ชดเชยความเร็ว; error detection รายงานข้อผิดพลาด (หน้า 6)','Data registers และ status/control registers แยกหน้าที่ใน I/O module (หน้า 7)'],
    ['control and timing','processor communication','device communication','data buffering','error detection','data register'],
    'อ่านภาพหน้า 7 จาก data/address/control lines ไปยัง I/O logic แล้วออก external-device interface logic',
    'buffering เป็นหนึ่งในหน้าที่ I/O module; ไม่ใช่การแทนที่ register ทุกชนิด',
    'คุม–คุย CPU–คุย device–พักข้อมูล–ตรวจผิด',
    [('หน้าที่ใดชดเชยความเร็วระหว่าง device กับ memory?',['Data buffering','Address recognition','Bus arbitration','Software poll'],0,'Data buffering'),('หน้าที่หลักห้ากลุ่มของ I/O module คืออะไร?','control/timing, processor communication, device communication, data buffering และ error detection'),('data register ต่างจาก status/control register ในภาพหน้า 7 อย่างไร?','ช่องแรกเก็บข้อมูล; อีกช่องเก็บสถานะหรือการควบคุมตามชื่อในภาพ')],(6,7))

add('io-techniques','Programmed I/O, Interrupt-driven I/O และ DMA','core','หน้า 8–9',
    'Programmed I/O ให้ processor สั่งและรอ I/O module จนเสร็จ จึงเสียเวลาหาก processor เร็วกว่าอุปกรณ์. Interrupt-driven I/O ให้ processor ทำงานอื่นระหว่างรอ แล้ว module แจ้งเมื่อเสร็จ. DMA ให้ I/O module กับ main memory แลกข้อมูลโดยตรงโดยไม่ให้ processor อยู่ในทางเดินข้อมูล.',
    ['Programmed: processor control และ wait (หน้า 8)','Interrupt-driven: สั่งแล้วทำงานต่อ; module interrupt เมื่อเสร็จ (หน้า 8)','DMA: I/O-to-memory โดยตรง ต่างจากสองวิธีที่ผ่าน processor (หน้า 8–9)'],
    ['programmed I/O','interrupt-driven I/O','direct memory access (DMA)','polling'],
    'ตารางหน้า 9 จัด programmed/interrupt-driven เป็น I/O-to-memory ผ่าน processor; DMA เป็น direct transfer',
    'interrupt ช่วยให้ CPU ไม่ต้องรอเฉย ๆ แต่ทางเดิน data ยังผ่าน processor ในตารางหน้า 9; DMA เปลี่ยนทางเดิน data',
    'รอเอง–ให้เรียก–ส่งตรง',
    [('เทคนิคใดโอนข้อมูล I/O↔memory โดยตรง?',['DMA','Programmed I/O','Interrupt-driven I/O','Software poll'],0,'DMA'),('Programmed ต่างจาก interrupt-driven อย่างไรเมื่อรอ device?','programmed รอ; interrupt-driven ไปทำงานอื่นและถูกแจ้งเมื่อ device พร้อม'),('ถ้าต้องแยก interrupt-driven กับ DMA จากตารางหน้า 9 ใช้เกณฑ์ใด?','ดูว่า data transfer ผ่าน processor หรือเป็น direct I/O-to-memory')],(8,9),
    (['เทคนิค','CPU ระหว่างรอ','ทางเดินข้อมูล'],[['Programmed','รอ','ผ่าน processor'],['Interrupt-driven','ทำงานอื่นจน interrupt','ผ่าน processor'],['DMA','ช่วยตั้งต้น/จบงาน','I/O↔memory โดยตรง']]))

add('io-commands','คำสั่ง Control, Test, Read, Write','core','หน้า 10',
    'I/O module รับคำสั่งจาก processor ได้สี่ชนิด. Control เปิดใช้และบอกอุปกรณ์ให้ทำงาน, Test ตรวจเงื่อนไขสถานะ, Read นำข้อมูลจาก peripheral เข้าสู่ internal buffer และ Write นำข้อมูลจาก data bus ไปส่งให้อุปกรณ์.',
    ['Control = activate/tell peripheral what to do','Test = test status conditions','Read = peripheral→internal buffer','Write = data bus→peripheral'],
    ['Control','Test','Read','Write','internal buffer'],
    'แยกทิศข้อมูล: Read เข้ามาใน I/O module; Write ออกจาก data bus ไป peripheral',
    'Test ตรวจสถานะ ไม่ใช่อ่าน data item จาก peripheral; Read ต่างจาก Test',
    'คุม–เช็ก–รับ–ส่ง',
    [('คำสั่งใดตรวจ status condition?',['Test','Read','Control','Write'],0,'Test'),('Read กับ Write มีทิศข้อมูลอย่างไร?','Read peripheral→internal buffer; Write data bus→peripheral'),('ถ้า processor ต้องเปิด peripheral ก่อนโอนข้อมูล ใช้คำสั่งประเภทใด?','Control')],(10,))

add('input-flow','ผังการรับ block ของข้อมูลด้วยสามเทคนิค','important','หน้า 11',
    'ผังหน้า 11 วาง programmed, interrupt-driven และ DMA ข้างกันเพื่อเทียบลำดับการรับ block. สองแบบแรกยังให้ CPU อ่าน word จาก I/O module และเขียนลง memory; programmed วนตรวจ status ขณะ interrupt-driven ทำงานอื่นระหว่างรอ. DMA รับคำสั่งเป็น block แล้วมี interrupt/status เมื่อสิ้นสุดการโอน.',
    ['Programmed: issue read → read/check status ซ้ำ → CPU read word → CPU write memory (หน้า 11)','Interrupt-driven: CPU ทำอย่างอื่นระหว่างรอ แต่ยัง read word/write memory หลัง interrupt (หน้า 11)','DMA: issue read block → CPU ทำอย่างอื่น → รับ completion interrupt/status (หน้า 11)'],
    ['status check','block read','completion interrupt','CPU-to-memory transfer'],
    'ไล่สามคอลัมน์หน้า 11 แล้วทำเครื่องหมายว่าช่วงใด CPU เป็นผู้ย้าย word',
    'interrupt-driven ไม่เท่ากับ DMA: ผังกลางยังมี CPU→memory write word',
    'ดูว่าใครย้าย word',
    [('ผังใดให้ CPU วน read status เมื่อยังไม่พร้อม?',['Programmed I/O','DMA','DCA','DDIO'],0,'Programmed I/O'),('ผัง interrupt-driven มีส่วนที่ยังเหมือน programmed อย่างไร?','CPU ยังอ่าน word จาก module แล้วเขียน word ลง memory'),('DMA ในผังหน้า 11 ต่างตรงคำสั่งเริ่มอย่างไร?','เริ่มด้วย read block command แล้ว DMA จัดการโอน block')],(11,))

add('io-addressing','I/O instructions, Memory-mapped และ Isolated I/O','core','หน้า 12–14',
    'แต่ละ I/O device มี identifier/address และ module ตีความ address lines เพื่อรับคำสั่งของตน. Memory-mapped I/O ใช้ address space ร่วมกับ memory จึงใช้คำสั่งอ่าน/เขียนแบบ memory; isolated I/O แยก address space และมีคำสั่ง/สัญญาณเลือก I/O เฉพาะ. ภาพ keyboard หน้า 14 แสดง register ที่ address 516/517 เทียบกับ instruction Load I/O/Test I/O/In ของ isolated I/O.',
    ['Memory-mapped: address space ร่วม, read/write lines เดียว, memory access commands ใช้ได้ (หน้า 12–13)','Isolated: separate address spaces, I/O-or-memory select lines, special I/O commands (หน้า 13)','Keyboard example memory-mapped ใช้ input data register 516, status/control 517 (หน้า 14)'],
    ['device address','memory-mapped I/O','isolated I/O','status/control register','I/O select line'],
    'เทียบสองคอลัมน์หน้า 14: ทางซ้ายใช้ load/store address 516/517, ทางขวาใช้ Load I/O, Test I/O, In กับ operand 5',
    'เลข 516/517 และ operand 5 เป็นตัวอย่างของคนละ address space/รูปแบบคำสั่ง ไม่ใช่ค่าที่ต้องเท่ากัน',
    'mapped ใช้ address ร่วม; isolated แยก',
    [('แบบใดแชร์ address space กับ memory?',['Memory-mapped','Isolated','DMA','Vectored'],0,'Memory-mapped'),('isolated I/O ต้องใช้อะไรต่างจาก memory-mapped?','address space แยกและ special I/O commands/selection lines'),('ภาพหน้า 14 keyboard status/control register อยู่ address ใดในตัวอย่าง memory-mapped?','517')],(12,13,14),
    (['แบบ','Address space','คำสั่ง'],[['Memory-mapped','ร่วมกับ memory','memory read/write'],['Isolated','แยกจาก memory','special I/O commands']]))

add('interrupt-processing','Interrupt-driven I/O และการเก็บ/คืนสถานะ','core','หน้า 15–17',
    'Interrupt-driven I/O ให้ processor ออกคำสั่งแล้วทำงานอื่นจน I/O module พร้อมจึงขอ interrupt. ในผัง simple interrupt processor จบ current instruction, acknowledge, เก็บ PSW กับ PC บน control stack แล้วโหลด PC ของ routine ใหม่. Software เก็บ state ที่เหลือ ประมวลผล interrupt แล้วคืน state, PSW และ PC เดิมเพื่อทำงานต่อ.',
    ['CPU จบคำสั่งปัจจุบันก่อนตอบ interrupt (หน้า 16)','เก็บ PSW/PC บน control stack แล้ว load new PC ตาม interrupt (หน้า 16)','Software save/process/restore state; ภาพหน้า 17 แสดง memory/register ก่อนและหลัง return (หน้า 16–17)'],
    ['interrupt','acknowledgement','PC','PSW','control stack','ISR'],
    'ไล่ลูกศรหน้า 16 จาก hardware ไป software และตาม PC/stack ในภาพหน้า 17',
    'แยกการเก็บ PSW/PC โดย processor กับการเก็บ remainder of process state ใน software ตามผัง; อย่าบอกว่า interrupt เริ่มกลางคำสั่งที่ยังไม่จบ',
    'จบคำสั่ง–เก็บ PC/PSW–บริการ–คืน',
    [('ก่อนเข้า routine ใหม่ processor เก็บอะไรบน control stack?',['PSW และ PC','DMA count','I/O buffer','cache tag'],0,'PSW และ PC'),('ลำดับ simple interrupt หลังกำเนิด request คืออะไร?','จบ current instruction, acknowledge, เก็บ PSW/PC, โหลด PC ใหม่, เก็บ state ที่เหลือ, service, restore'),('เหตุใดต้องคืน PC/PSW เดิม?','เพื่อกลับไปประมวลผลต่อจากจุดที่ถูก interrupt ตามภาพหน้า 16–17')],(15,16,17))

add('interrupt-identification','ปัญหา priority และวิธีระบุ device ที่ interrupt','core','หน้า 18–19',
    'เมื่อมี I/O modules หลายตัว processor ต้องรู้ว่าใครขอ interrupt และเมื่อมีหลาย request ต้องตัดสินใจลำดับที่จัดการ. สไลด์ยกสี่วิธีระบุแหล่ง: multiple interrupt lines, software poll, daisy chain แบบ vectored และ bus arbitration แบบ vectored. Software poll ใช้ routine ตรวจ module ทีละตัว ส่วน vectored ส่ง identifier/vector เพื่อพาไปยัง device-service routine.',
    ['สอง design issues: identify requester และเลือกจัดการเมื่อ interrupts หลายตัว (หน้า 18)','Software poll ต้องไล่ตรวจ module และกินเวลา; daisy chain ส่ง acknowledge ผ่าน module (หน้า 19)','Bus arbitration: module ได้ bus ก่อน, processor acknowledge, module วาง vector บน data lines (หน้า 19)'],
    ['multiple interrupt lines','software poll','daisy chain','bus arbitration','vectored interrupt','vector'],
    'ตาราง 4 ช่องหน้า 19: จับคู่ชื่อวิธีกับสัญญาณ/ลำดับของมัน',
    'คำว่า vector ในสไลด์คือ address หรือ identifier ที่ใช้ชี้ routine ไม่ใช่ตัวข้อมูล I/O ที่รับส่ง',
    'ใครขอ? ใครก่อน? poll หรือ vector',
    [('วิธีใดให้ routine ไล่ถามแต่ละ I/O module?',['Software poll','Daisy chain','DMA','Memory-mapped'],0,'Software poll'),('สองคำถามออกแบบ interrupt หน้า 18 คืออะไร?','ระบุ device ที่ร้องขอ และเลือก interrupt ที่จะจัดการเมื่อมีหลายตัว'),('bus arbitration แบบ vectored ส่ง vector ผ่านอะไรหลัง acknowledge?','data lines')],(18,19),
    (['วิธี','ระบุผู้ร้องขอ'],[['Multiple lines','แยก interrupt line'],['Software poll','routine ถาม module ทีละตัว'],['Daisy chain','acknowledge ผ่าน chain แล้วใช้ vector'],['Bus arbitration','ผู้ได้ bus ส่ง vector บน data lines']]))

add('interrupt-controller-example','82C59A interrupt controller แบบ master/slave','extra','หน้า 20',
    'ภาพหน้า 20 ยกการต่อ external devices เข้ากับ slave 82C59A หลายตัว แล้ว slave ส่ง INT ไปยัง IR inputs ของ master. Master ส่ง INT ไปยัง INTR ของ processor 80386. นี่เป็นตัวอย่างโครงสร้าง interrupt controller ในสไลด์ ไม่ใช่ข้อกำหนดของทุกระบบ.',
    ['Slave รับ external-device lines IR0–IR7 (หน้า 20)','INT ของ slave เข้าสู่ master; INT ของ master เข้าสู่ INTR ของ processor (หน้า 20)','ภาพยก 80386 และ 82C59A เป็นตัวอย่างระบบ (หน้า 20)'],
    ['82C59A','master','slave','IR0–IR7','INT','INTR'],
    'ตามเส้นจาก external device 00 ผ่าน slave ตัวบน, master แล้วถึง processor',
    'อย่าสลับ INT output ของ controller กับ INTR input ของ processor ในภาพนี้',
    'device → slave → master → CPU',
    [('INT ของ master ต่อเข้าขาใดของ 80386 ในภาพ?',['INTR','DREQ','HLDA','PSW'],0,'INTR'),('slave controller ในภาพมี input อะไร?','IR0–IR7 จาก external devices'),('เหตุใดรูปนี้จึงเรียกว่า master/slave?','slave รวม request จาก devices แล้วส่งต่อให้ master ซึ่งแจ้ง processor')],(20,))

add('ppi-8255','Intel 8255A/82C55A และ control word','important','หน้า 21–23',
    'ตัวอย่าง programmable peripheral interface แสดง Port A, Port B และ Port C ที่แบ่ง upper/lower พร้อม data-bus buffer และ read/write control logic. Control word หน้า 22 ตั้ง mode และทิศ input/output ของ ports หรือเลือก bit set/reset ใน Port C. ภาพหน้า 23 แสดงการใช้ Port A รับ keyboard, Port B ส่ง display และ Port C ทำ handshake/interrupt.',
    ['8255A block diagram มี Port A/B อย่างละ 8 บิต และ Port C upper/lower อย่างละ 4 บิต (หน้า 21)','Control word: D7=1 ใช้ mode set; D7=0 ใช้ bit set/reset ของ Port C (หน้า 22)','ตัวอย่าง keyboard↔Port A, display↔Port B, Port C ใช้ ready/acknowledge/interrupt (หน้า 23)'],
    ['8255A','82C55A','control word','mode set','bit set/reset','Port A/B/C'],
    'เทียบ (a) mode definition กับ (b) bit definition หน้า 22 แล้วตามการต่อจริงหน้า 23',
    'หน้า 21–22 เรียก 8255A แต่หน้า 23 เรียก 82C55A; ชื่อรุ่นในภาพต้องอ่านตามแต่ละสไลด์ ไม่รวมเป็นเลขเดียวโดยเดา',
    'A รับ keyboard, B ส่ง display, C คุมสัญญาณในภาพ',
    [('D7=0 ใน control word หน้า 22 ใช้ทำอะไร?',['Bit set/reset Port C','Mode set','DMA request','Interrupt acknowledge'],0,'Bit set/reset Port C'),('Port C แบ่งอย่างไรใน block diagram?','upper 4 bits กับ lower 4 bits'),('ในตัวอย่างหน้า 23 Port B ต่อกับอะไร?','display output port')],(21,22,23))

add('dma-motivation','ข้อจำกัดของ I/O ผ่าน CPU และเหตุผลใช้ DMA','core','หน้า 24',
    'Programmed และ interrupt-driven I/O มีข้อจำกัดร่วมคืออัตราโอนขึ้นกับความเร็วที่ processor ตรวจ/บริการ device และ processor ต้องรันหลายคำสั่งต่อการโอนแต่ละครั้ง. เมื่อย้ายข้อมูลปริมาณมาก สไลด์จึงเสนอ direct memory access เพื่อให้โอนได้มีประสิทธิภาพกว่า.',
    ['Transfer rate ถูกจำกัดด้วยความเร็วตรวจ/บริการ device ของ processor (หน้า 24)','Processor ยังจัดการ transfer และรัน instructions ต่อครั้ง (หน้า 24)','Large data volume เป็นเหตุผลใช้ DMA (หน้า 24)'],
    ['I/O transfer rate','programmed I/O','interrupt-driven I/O','DMA'],
    'เชื่อมตารางหน้า 9 กับข้อเสียหน้า 24: ทั้งสองแบบแรกยังมี CPU ในเส้นทางการโอน',
    'interrupt ลดการรอว่าง แต่ไม่ได้ย้าย CPU ออกจากการโอนข้อมูลแต่ละ word ตามผังหน้า 11',
    'ข้อมูลมาก → ให้ DMA รับทางเดิน',
    [('ข้อเสียร่วมของ programmed และ interrupt-driven คืออะไร?',['CPU จัดการ transfer','ไม่มี I/O module','ไม่มี device address','ใช้แต่ bus แยก'],0,'CPU จัดการ transfer'),('เหตุใดสไลด์เสนอ DMA สำหรับข้อมูลจำนวนมาก?','ลดภาระ CPU ที่ต้อง test/service และรันหลายคำสั่งต่อ I/O transfer'),('ข้อเสียนี้สัมพันธ์กับผังรับ block หน้า 11 อย่างไร?','สองวิธีแรกยังให้ CPU อ่าน word และเขียน memory')],(24,))

add('dma-controller','DMA block diagram และ breakpoint ใน instruction cycle','core','หน้า 25–26',
    'DMA controller ในภาพมี data count, data register, address register และ control logic พร้อม request/acknowledge, interrupt, read/write signals. ภาพ instruction cycle แยก DMA breakpoints ที่อยู่ระหว่าง processor cycles หลายจุด กับ interrupt breakpoint หลัง store result ก่อนขั้น process interrupt. หมายเหตุภาษาไทยบนสไลด์อธิบาย DMA แทรกเกี่ยวกับ hardware bus โดยตรง.',
    ['data count/address/data register และ control logic ใน DMA module (หน้า 25)','DMA breakpoints ปรากฏหลายจุดใน instruction cycle; interrupt breakpoint ปรากฏก่อน process interrupt (หน้า 26)','อ่าน request, acknowledge, read/write, interrupt ตามลูกศรของ DMA controller (หน้า 25)'],
    ['DMA controller','data count','address register','DMA breakpoint','interrupt breakpoint'],
    'ตามภาพหน้า 26: จุด DMA มีหลัง fetch/decode/execute ตามลูกศร; interrupt อยู่หลัง store result',
    'อย่ากล่าวว่า DMA ต้องรอ interrupt checkpoint จุดเดียว; ภาพแยก DMA กับ interrupt breakpoint',
    'DMA ดู bus หลายจุด; interrupt หลังคำสั่ง',
    [('DMA controller มี register ใดบอกตำแหน่ง memory?',['Address register','PSW','Status register','Port C'],0,'Address register'),('ภาพหน้า 25 แสดงองค์ประกอบหลักใดใน DMA module?','data count, data register, address register, control logic'),('DMA breakpoint ต่างจาก interrupt breakpoint ในภาพหน้า 26 อย่างไร?','DMA อยู่ได้หลายจุดระหว่าง processor cycles; interrupt อยู่ก่อนขั้น process interrupt')],(25,26))

add('dma-configurations','Alternative DMA configurations และ Intel 8237A','important','หน้า 27–30',
    'ภาพหน้า 27 เทียบ DMA แยกบน single bus, DMA รวมกับ I/O บน single bus และแบบแยก I/O bus. ตัวอย่าง 8237 หน้า 28 แสดง DREQ/DACK ระหว่าง disk controller กับ DMA และ HRQ/HLDA ระหว่าง DMA กับ CPU. หน้า 29 ระบุว่า data ไม่เก็บใน DMA chip, มี 4 channels และทำ memory-to-memory ผ่าน register ได้; ตาราง register หน้า 30 มีรายการ status ซ้ำที่อ่านแล้วกำกวม.',
    ['สาม configuration: single-bus detached, single-bus integrated DMA-I/O, I/O bus (หน้า 27)','DREQ/DACK = DMA request/acknowledge; HRQ/HLDA = hold request/acknowledge (หน้า 28)','8237 มี 4 channels 0–3; data ไม่เก็บใน chip ระหว่าง transfer ตามคำอธิบาย (หน้า 29)','ตาราง Intel 8237A มี command/status/mode/masks; E/D และ TC มีคำขยายใต้ตาราง (หน้า 30)'],
    ['single-bus DMA','I/O bus','DREQ','DACK','HRQ','HLDA','terminal count','8237A'],
    'ตามสัญญาณหน้า 28: disk controller ขอ DMA ด้วย DREQ; DMA ขอ hold จาก CPU ด้วย HRQ; หลังยืนยันจึงใช้ bus ตามภาพ',
    'หน้า 29 พูด DMA ปกติระหว่าง I/O port-memory แต่ระบุข้อยกเว้น memory-to-memory ผ่าน register; หน้า 30 status แถว D4–D7 พิมพ์ Channel 0 request ซ้ำ: ต้องตรวจสอบจากต้นฉบับ',
    'DREQ ขอ DMA; HRQ ขอ bus',
    [('สัญญาณขอ DMA จาก device ชื่ออะไร?',['DREQ','DACK','HLDA','PSW'],0,'DREQ'),('สามโครงสร้าง DMA ในหน้า 27 คืออะไร?','single-bus detached, single-bus integrated DMA-I/O และ I/O bus'),('แถวใดใน status column หน้า 30 ชวนตรวจต้นฉบับ?','D4–D7 พิมพ์ Channel 0 request ซ้ำ')],(27,28,29,30))

add('dca-motivation','Direct Cache Access (DCA) และภาพ Xeon','important','หน้า 31–32',
    'สไลด์นำ DCA ต่อจาก DMA เพราะปริมาณ network I/O ในตัวอย่างระบบสูงขึ้นจน DMA อย่างเดียวมีข้อจำกัดการขยายตัวตามคำอธิบาย. ภาพ Xeon E5-2600/4600 แสดง cores, L1/L2/L3 cache, PCIe/QPI และ memory controller hub เพื่อวางตำแหน่ง data path. ตัวเลข 10/100 Gbps และรุ่นชิปเป็นบริบทตัวอย่างในสไลด์.',
    ['แรงผลักในสไลด์คือ network data rate สูง เช่น 10/100-Gbps Ethernet และ Wi-Fi ระดับ gigabit (หน้า 31)','ภาพ Xeon มี cores 0–7, L1/L2 ต่อ core, L3 segments, PCIe/QPI และ memory controller hub (หน้า 32)','DCA ถูกเสนอหลังปัญหาการ scale ของ DMA ในกรณี network I/O (หน้า 31)'],
    ['Direct Cache Access (DCA)','network I/O','Xeon E5-2600/4600','PCIe','QPI','L3 cache'],
    'อ่านภาพหน้า 32 จาก PCIe สำหรับ I/O เข้าสู่วง cache และ cores; ใช้เพื่อเห็นจุดที่ cache เกี่ยวข้องกับ packet',
    'อย่าอ้างว่า 10/100 Gbps หรือสถาปัตยกรรม Xeon นี้เป็นสเปกปัจจุบัน; เป็นตัวอย่างจากสไลด์',
    'network เร็วขึ้น → data path ผ่าน cache สำคัญขึ้น',
    [('อะไรเป็นแรงผลักให้สไลด์พูดถึง DCA?',['network I/O data rates สูงขึ้น','keyboard ช้าลง','จำนวนคำสั่ง ISA ลด','disk ไม่มี sector'],0,'network I/O data rates สูงขึ้น'),('ภาพหน้า 32 แสดง cache ระดับใดรอบ cores?','L1, L2 และ L3'),('เหตุใดต้องมอง cache ในเส้นทาง network I/O?','packet ผ่าน memory/cache/core ตามสไลด์หน้า 33–34')],(31,32))

add('packet-cache','Packet traffic, buffers และ cache-related performance','important','หน้า 33–35',
    'Network traffic อยู่ในรูป packets/PDU; สไลด์ยก Ethernet ที่ครอบ IP/TCP และการทำงานของ NIC. ใน DMA scheme ขาออก application buffer ถูกคัดไป system buffer ใน main memory พร้อม TCP/IP headers ก่อน NIC นำไป; ขาเข้าก็มีการย้ายระหว่าง buffers. ขั้น incoming หน้า 35 มี DMA, NIC interrupt, retrieval, cache miss, header processing และ payload transfer.',
    ['Ethernet packet บรรทุก higher-level IP/TCP packet ตามลำดับชั้นที่สไลด์อธิบาย (หน้า 33)','Outgoing DMA path ใช้ application buffer→system buffer พร้อม headers→NIC (หน้า 34)','Incoming: packet arrives→DMA→NIC interrupts host→retrieve descriptors/headers→cache miss→process header→transfer payload (หน้า 35)','Outgoing: request→create packet→invoke output→DMA→NIC completion→driver frees buffer (หน้า 35)'],
    ['packet','PDU','Ethernet','IP','TCP','NIC','application buffer','system buffer','cache miss'],
    'ใช้ตารางสองคอลัมน์หน้า 35 เพื่อเทียบ incoming/outgoing; เชื่อมกับข้อความ buffer copy หน้า 34',
    'อย่าสรุปว่า DMA ไม่เกี่ยวกับ cache: หน้า 34–35 ระบุ core, main memory และ cache ล้วนอยู่ในทางเดิน',
    'packet ผ่าน buffer และ cache ก่อนถึงงานของ core',
    [('อุปกรณ์ใดส่ง packet ระหว่าง network กับ host ในสไลด์?',['NIC','PSW','8255 control word','ISR stack'],0,'NIC'),('outgoing DMA path ใช้ buffer ใดบ้าง?','application-assigned buffer และ system buffer ใน main memory'),('incoming หลัง NIC interrupt มีขั้นใดที่ชี้ต้นทุน cache?','retrieve descriptors/headers แล้ว cache miss ก่อน process header')],(33,34,35))

add('dca-ddio','DCA prefetch, cache injection และ DDIO','core','หน้า 36–37',
    'DCA แบบ prototype ในสไลด์ใช้กับ incoming network traffic: memory controller ส่ง prefetch hint เมื่อ data พร้อมใน system memory เพื่อให้ core ดึง packet จาก system buffer ล่วงหน้า. แนวที่ก้าวต่อไปคือหลีกเลี่ยง system buffer ใน main memory ผ่าน cache injection ซึ่งสไลด์เรียก Direct Data I/O (DDIO) ในสาย Xeon. ภาพหน้า 37 เทียบ DMA ที่โอนผ่าน main memory กับ DDIO ที่เข้าหรือออกผ่าน last-level cache.',
    ['DCA prototype เฉพาะ incoming; memory controller ส่ง prefetch hint ให้ core (หน้า 36)','cache injection/DDIO ลดการผ่าน system buffer ใน main memory (หน้า 36)','ภาพเปรียบ DMA transfer to/from memory กับ DDIO transfer to/from cache (หน้า 37)'],
    ['DCA','prefetch hint','system buffer','cache injection','Direct Data I/O (DDIO)','last-level cache'],
    'ดูภาพ (a)–(d) หน้า 37 แล้วตามลูกศรสีเขียวว่าข้อมูลผ่าน main memory หรือ last-level cache',
    'DCA prototype ที่อธิบาย incoming only ไม่ใช่ข้อจำกัดที่ระบุให้ DDIO ทุกกรณี; ภาพ DDIO มีทั้ง transfer to cache และ to I/O',
    'DCA เตรียม cache; DDIO ส่งผ่าน cache',
    [('prefetch hint ของ DCA prototype มาจากส่วนใด?',['memory controller','keyboard','control stack','8255A'],0,'memory controller'),('DDIO แตกต่างจาก normal DMA ในภาพหน้า 37 อย่างไร?','DDIO ใช้ last-level cache เป็นทางเดินข้อมูลแทนการผ่าน main memory ในภาพเปรียบ'),('DCA prototype หน้า 36 ใช้กับ traffic ทิศใด?','incoming network traffic')],(36,37),
    (['กลไก','ทางเดิน/บทบาทในสไลด์'],[['Normal DMA','I/O ↔ main memory'],['DCA prototype','data อยู่ system memory แล้วส่ง prefetch hint'],['DDIO/cache injection','I/O ↔ last-level cache']]))

add('io-evolution','วิวัฒนาการ I/O function และ I/O channel','core','หน้า 38–39',
    'สไลด์เรียงวิวัฒนาการจาก CPU คุมอุปกรณ์ตรง → เพิ่ม I/O module แบบ programmed → interrupt → DMA → module เป็น processor เฉพาะทาง → module มี local memory จนทำงานได้คล้ายคอมพิวเตอร์ของตน. ภาพ I/O channel แยก selector channel กับ multiplexor channel โดยทั้งคู่เชื่อม memory/CPU กับ I/O controllers แต่จัดทางเชื่อมอุปกรณ์ต่างกัน.',
    ['6 ขั้นวิวัฒนาการเรียงจาก CPU direct control ถึง I/O module ที่มี local memory (หน้า 38)','Interrupt ลดเวลารอของ CPU; DMA ย้าย block โดย CPU ช่วยเริ่ม/จบตามคำอธิบาย (หน้า 38)','Selector กับ multiplexor channel เป็นสองสถาปัตยกรรมในภาพหน้า 39'],
    ['I/O function','I/O module','DMA','I/O channel','selector channel','multiplexor channel','local memory'],
    'จับคู่ขั้นที่ 2–4 หน้า 38 กับ programmed, interrupt และ DMA แล้วดูรูป selector/multiplexor หน้า 39',
    'อย่าคิดว่าทุกขั้นของวิวัฒนาการแทนของเดิมทั้งหมด; สไลด์เป็นลำดับการเพิ่มความสามารถของ module',
    'CPU คุม → module → interrupt → DMA → processor I/O',
    [('วิวัฒนาการขั้นใดให้ I/O module เข้าถึง memory โดยตรง?',['DMA','Programmed no interrupt','CPU direct','Software poll'],0,'DMA'),('ลำดับหกขั้นในหน้า 38 สรุปอย่างไร?','CPU direct → module/programmed → interrupt → DMA → specialized I/O processor → module มี local memory'),('ภาพหน้า 39 เทียบ channel สองชนิดใด?','selector และ multiplexor')],(38,39))

add('usb','USB generations และ host-controller tree','important','หน้า 41',
    'สไลด์ยก USB เป็นตัวอย่าง peripheral connection หลายรุ่น และแยก signaling rate ออกจาก usable data rate ใน SuperSpeed. ตัวเลขที่ให้มี USB 1.0 low/full 1.5/12 Mbps, USB 2.0 480 Mbps, USB 3.0 signaling 5 Gbps usable สูงสุด 4 Gbps, USB 3.1 Gen2 signaling 10 Gbps usable ตามสไลด์ 9.7 Gbps และ USB 3.2 Gen2x2 20 Gbps. Root host controller เชื่อมอุปกรณ์เป็น hierarchical tree.',
    ['USB 1.0 Low/Full Speed 1.5/12 Mbps; USB 2.0 480 Mbps (หน้า 41)','USB 3.0/3.1 Gen1 signaling 5 Gbps, usable สูงสุด 4 Gbps; Gen2 signaling 10 Gbps, usable ทฤษฎี 9.7 Gbps (หน้า 41)','USB 3.2 Gen2x2 20 Gbps; root host controller จัด tree topology (หน้า 41)'],
    ['USB','Low Speed','Full Speed','SuperSpeed','SuperSpeed+','signaling rate','usable data rate','root host controller'],
    'อ่านตัวเลขหน้า 41 โดยแยกความเร็วสัญญาณกับ usable data rate แล้วจับคู่ generation',
    'เลขเหล่านี้เป็นตัวเลขตามสไลด์/ยุคของเอกสาร ไม่ใช่สเปก USB ปัจจุบัน; อย่าสลับ signaling 5 Gbps กับ usable 4 Gbps',
    'ดูรุ่น–ดูหน่วย–แยก signaling/usable',
    [('USB 2.0 ในสไลด์ระบุ data rate เท่าไร?',['480 Mbps','12 Mbps','5 Gbps','20 Gbps'],0,'480 Mbps'),('USB 3.0 ในหน้า 41 แยก signaling กับ usable อย่างไร?','5 Gbps signaling; usable สูงสุด 4 Gbps เพราะ overhead ตามสไลด์'),('อุปกรณ์ USB จัดเป็น topology แบบใดในหน้า 41?','hierarchical tree ภายใต้ root host controller')],(41,))

add('firewire-scsi','FireWire และ SCSI ในชุดตัวอย่าง','extra','หน้า 42–43',
    'FireWire ตามสไลด์คือ IEEE 1394 high-performance serial bus ที่ใช้ daisy chain และรองรับ hot plugging/automatic configuration. SCSI เป็น Small Computer System Interface สำหรับ peripheral โดยภาพรวมหน้า 43 กล่าวถึง shared parallel bus และการใช้กับ mass memory ใน enterprise. ทั้งสองหน้าเป็นตัวอย่างเทคโนโลยีที่ถูกจัดให้รายงานกลุ่ม.',
    ['FireWire: IEEE 1394, daisy chain สูงสุด 63 devices ต่อ port, hot plugging และ auto config (หน้า 42)','SCSI: shared bus แบบ parallel, 16 หรือ 32 devices ตาม generation, high-speed version สำหรับ mass memory (หน้า 43)','SCSI ย่อจาก Small Computer System Interface (หน้า 43)'],
    ['FireWire','IEEE 1394','daisy chain','hot plugging','SCSI','parallel bus'],
    'เทียบ serial daisy chain ของ FireWire หน้า 42 กับ shared parallel bus ของ SCSI หน้า 43',
    'ข้อเปรียบเทียบนี้อ้างเฉพาะระบบ/รุ่นในสไลด์; อย่าถือว่าเป็นคำแนะนำเลือกใช้อุปกรณ์ปัจจุบัน',
    'FireWire serial chain; SCSI parallel shared',
    [('SCSI ย่อจากอะไร?',['Small Computer System Interface','Serial Cache System Interface','System Control Signal Input','Single Channel Serial I/O'],0,'Small Computer System Interface'),('FireWire ในสไลด์มีคุณสมบัติต่ออุปกรณ์โดยไม่ปิดเครื่องว่าอะไร?','hot plugging'),('FireWire กับ SCSI ในสไลด์ต่างรูป bus อย่างไร?','FireWire serial daisy chain; SCSI shared parallel bus')],(42,43),
    (['ตัวอย่าง','รูปแบบในสไลด์','จุดเด่นที่ให้'],[['FireWire','serial daisy chain','hot plugging/auto config'],['SCSI','shared parallel bus','mass memory/enterprise']]))

add('thunderbolt-infiniband','Thunderbolt และ InfiniBand','extra','หน้า 44–45',
    'Thunderbolt ในสไลด์รวม data, video, audio และ power ในสายเชื่อม peripheral เดียว พร้อมตัวเลขตัวอย่าง 10 Gbps ต่อทิศและ 10 W. InfiniBand ถูกวางสำหรับ high-end server และ storage area networking ผ่าน fabric ของ switches/links เพื่อเชื่อม server, storage และ network devices. ตัวเลขความเร็วและขนาดระบบเป็นข้อมูลตามสไลด์.',
    ['Thunderbolt รวม data/video/audio/power และระบุ 10 Gbps แต่ละทิศ, 10 W ตามสไลด์ (หน้า 44)','InfiniBand มุ่ง high-end server, storage area networking และ switch-based fabric (หน้า 45)','สไลด์ยก IBM zEnterprise และสูงสุด 64,000 devices เป็นบริบทตัวอย่าง (หน้า 45)'],
    ['Thunderbolt','InfiniBand','fabric','switch-based architecture','storage area network'],
    'ใช้หัวข้อการใช้งานเทียบ: Thunderbolt ต่อ peripherals; InfiniBand เชื่อมระบบ server/storage จำนวนมากใน fabric',
    'ตัวเลข 10 Gbps/10 W และ 64,000 เป็นข้อมูลในเอกสาร ไม่ใช่ข้อเท็จจริงอัปเดตของเทคโนโลยี',
    'Thunderbolt รวมสาย; InfiniBand รวม fabric',
    [('เทคโนโลยีใดในหน้า 45 ใช้ switch-based fabric?',['InfiniBand','Thunderbolt','SCSI','USB 1.0'],0,'InfiniBand'),('Thunderbolt ในหน้า 44 รวมสัญญาณใด?','data, video, audio และ power'),('InfiniBand เหมาะกับงานกลุ่มใดตามหน้า 45?','high-end servers และ storage area networking')],(44,45))

add('pcie-sata','PCI Express และ SATA','extra','หน้า 46',
    'สไลด์ยก PCI Express เป็น high-speed bus สำหรับเชื่อม peripherals หลายชนิดและความเร็ว. SATA ย่อจาก Serial Advanced Technology Attachment และใช้เป็น interface สำหรับ disk storage systems. ตัวเลข data rate ในหน้า 46 เป็นตัวอย่างตามเอกสารและควรอ่านเป็นข้อมูลประจำสไลด์.',
    ['PCI Express: high-speed bus สำหรับ peripherals หลายประเภท/ความเร็ว (หน้า 46)','SATA = Serial Advanced Technology Attachment; interface สำหรับ disk storage (หน้า 46)','สไลด์ให้ตัวเลขสูงสุด 6 Gbps และ 300 Mbps ต่อ device ในคำอธิบาย SATA: ต้องตรวจสอบจากต้นฉบับก่อนใช้คำนวณหรืออ้างเป็นสเปก (หน้า 46)'],
    ['PCI Express','PCIe','SATA','Serial Advanced Technology Attachment'],
    'ดูภาพการ์ด PCIe และสาย/drive SATA หน้า 46 เพื่อแยกบริบทการใช้งาน',
    'หน้า 46 วาง 6 Gbps กับ 300 Mbps ต่อ device ในหัวข้อ SATA โดยไม่อธิบายเงื่อนไขที่ทำให้ต่างกัน: ต้องตรวจสอบจากต้นฉบับ; อย่าอนุมานรุ่นหรือความเร็วจริง',
    'PCIe ต่อ peripherals; SATA ต่อ disk',
    [('SATA ย่อจากอะไร?',['Serial Advanced Technology Attachment','System Address Transfer Architecture','Storage Array Timing Access','Serial Application Transfer Address'],0,'Serial Advanced Technology Attachment'),('PCI Express ใช้เชื่อมอะไรตามหน้า 46?','peripherals หลายชนิดและหลายความเร็ว'),('ตัวเลข SATA สองค่าใดในหน้า 46 ต้องตรวจเงื่อนไขก่อนใช้?','6 Gbps กับ 300 Mbps ต่อ device: ต้องตรวจสอบจากต้นฉบับ')],(46,))

add('ethernet-wifi','Ethernet และ Wi-Fi ในชุดตัวอย่าง','extra','หน้า 47–48',
    'Ethernet ในสไลด์เป็น wired networking ที่เปลี่ยนจาก bus-based ไป switch-based โดยมี central switch เชื่อมอุปกรณ์. Wi-Fi เป็น wireless Internet access ที่เชื่อมอุปกรณ์หลายประเภทและพัฒนามาตรฐาน IEEE 802.11 ต่อเนื่อง. ตัวเลข 100 Gbps Ethernet และ 802.11ac 3.2 Gbps เป็นตัวอย่างที่สไลด์ให้ ณ ช่วงของเอกสาร.',
    ['Ethernet: wired, bus-based → switch-based central switch; ตัวเลขในสไลด์สูงสุด 100 Gbps (หน้า 47)','Wi-Fi: wireless Internet access; IEEE 802.11; สไลด์ระบุ 802.11ac (2014) สูงสุด 3.2 Gbps (หน้า 48)','หน้า 40 จัด Ethernet และ Wi-Fi อยู่ในชุดหัวข้อรายงานกลุ่ม'],
    ['Ethernet','wired network','central switch','Wi-Fi','IEEE 802.11','802.11ac'],
    'เทียบลูกศร/ภาพหน้า 47 Ethernet cable กับหน้า 48 wireless devices',
    'อย่าใช้คำว่า “current version” จากหน้า 48 เป็นคำบอกเวอร์ชันปัจจุบัน ณ วันนี้; เป็นถ้อยคำในสไลด์',
    'Ethernet มีสาย/สวิตช์; Wi-Fi ไร้สาย/802.11',
    [('เทคโนโลยีใดเป็น predominant wireless Internet access ในสไลด์?',['Wi-Fi','Ethernet','SATA','PCIe'],0,'Wi-Fi'),('Ethernet เปลี่ยน topology ตามสไลด์อย่างไร?','จาก bus-based เป็น switch-based มี central switch'),('ตัวเลข “current version 802.11ac” ควรตีความอย่างไร?','เป็นคำของสไลด์หน้า 48 ไม่ใช่สถานะเทคโนโลยีปัจจุบัน')],(47,48))

add('ibm-channel-example','ตัวอย่าง IBM EC12 I/O channel subsystem','extra','หน้า 49–51',
    'ภาพท้ายบทแสดง IBM EC12 channel subsystem, ตู้ I/O frames และการเชื่อม books ผ่าน PCIe/InfiniBand ไปยัง I/O controllers/channels. หน้า 49 ให้ตัวเลข partitions, channel subsystems และ channels ในภาพ แต่ข้อความจำนวน partitions สูงสุดด้านบนกับด้านล่างไม่ตรงกัน. จึงใช้ภาพทบทวนความสัมพันธ์เชิงโครงสร้างโดยไม่สรุปจำนวน partitions ที่ขัดกัน.',
    ['หน้า 49 มี 4 channel subsystems และระบุไม่เกิน 256 channels ต่อ subsystem ในภาพ','หน้า 50 ภาพตู้แสดง PCIe drawer, I/O cage, processor books, InfiniBand/PCIe interconnects','หน้า 51 เชื่อม 4 books กับ PCIe switches และ InfiniBand multiplexors เพื่อไป controllers/channels'],
    ['IBM EC12','channel subsystem','partition','channel','PCIe I/O drawer','InfiniBand multiplexer'],
    'ตามแผนภาพหน้า 51 จาก book→PCIe/HCA→switch/multiplexer→controller/channel',
    'หน้า 49 ด้านบนเขียน ≤60 partitions/system แต่ด้านล่างเขียน ≤1024 partitions/system: ต้องตรวจสอบจากต้นฉบับ; ห้ามนำตัวเลขใดเป็นคำตอบแน่นอน',
    'book → channel subsystem → channel → device',
    [('หน้า 49 แสดง channel subsystem กี่ชุด?',['4','8','15','256'],0,'4 ชุด'),('ภาพหน้า 51 แสดงเส้นทาง I/O ผ่านส่วนใด?','books ไป PCIe/HCA แล้วผ่าน switch/multiplexer สู่ controllers/channels'),('จำนวน partitions ต่อ system หน้า 49 สรุปได้หรือไม่?','ต้องตรวจสอบจากต้นฉบับ เพราะภาพเขียน ≤60 และ ≤1024 ขัดกัน')],(49,50,51))

page_text = {p['page']:p['text'] for p in json.loads((HERE/'pages.json').read_text(encoding='utf-8'))}
figure_pages = sorted({int(fid[4:]) for t in topics for fid in t['figures']})
caption_override = {
  3:'ผัง I/O module เชื่อม address/data/control lines ของ system bus กับ peripheral links',
  5:'ผัง external device แยก control logic, buffer และ transducer',
  7:'ผัง I/O module มี data registers, status/control registers และ device interface logic',
  9:'ตารางสรุปทางเดินข้อมูลของ programmed, interrupt-driven และ DMA',
  11:'ผังสามเทคนิคการรับ block: CPU รอ/ทำงานอื่น/ให้ DMA โอน',
  14:'ตัวอย่าง keyboard เปรียบ memory-mapped address 516/517 กับ isolated I/O operand 5',
  16:'ผัง simple interrupt: จบคำสั่ง เก็บ PSW/PC ไป ISR แล้วคืน state',
  17:'ภาพก่อนและหลัง interrupt ใน main memory, control stack และ registers',
  19:'สี่วิธีระบุ I/O module ที่ร้องขอ interrupt',
  20:'82C59A slave controllers ส่ง INT ผ่าน master ไปยัง 80386',
  22:'รูปแบบ control word ของ Intel 8255A สำหรับ mode set และ bit set/reset',
  23:'ภาพ keyboard/display interface ต่อ Port A/B/C ของ 82C55A',
  25:'DMA block diagram: data count, data/address registers และ control logic',
  26:'ตำแหน่ง DMA breakpoints และ interrupt breakpoint ใน instruction cycle',
  27:'แผนภาพ DMA สาม configuration: detached, integrated และ I/O bus',
  28:'สัญญาณ DREQ/DACK และ HRQ/HLDA ของตัวอย่าง 8237 DMA',
  30:'ตาราง Intel 8237A registers; status แถว D4–D7 มี Channel 0 request ซ้ำ: ต้องตรวจสอบจากต้นฉบับ',
  32:'สถาปัตยกรรม Xeon E5-2600/4600 ตัวอย่าง cache และ I/O data path',
  35:'ตารางขั้น incoming/outgoing packet traffic',
  36:'DCA prefetch hint เทียบกับ cache injection/Direct Data I/O',
  37:'ผัง normal DMA กับ DDIO สำหรับ transfer to memory/cache และ to I/O',
  39:'I/O channel architecture เปรียบ selector กับ multiplexor',
  46:'ภาพ PCI Express และ SATA; ตัวเลข 6 Gbps กับ 300 Mbps ต่อ device ต้องตรวจสอบจากต้นฉบับ',
  49:'IBM EC12 channel subsystems; จำนวน partitions ด้านบน/ล่างไม่ตรงกัน: ต้องตรวจสอบจากต้นฉบับ',
  50:'ภาพตู้ IBM zEC12 I/O frames พร้อมป้าย PCIe drawer, I/O cage และ processor books',
  51:'ภาพ IBM EC12 books ผ่าน PCIe/InfiniBand ไปยัง I/O controllers',
}

def heading(p):
    lines=[x.strip(' •\t') for x in page_text[p].splitlines() if x.strip()]
    lines=[x for x in lines if not x.startswith(('ITDS-211:','©','W.Suntiamorntut'))]
    return next((x for x in lines if len(x)>5 and not x.startswith(('■','•'))), '')

figures=[]
for p in figure_pages:
    owner=next(t for t in topics if f'fig-{p}' in t['figures'])
    title=heading(p) or owner['title']
    caption=caption_override.get(p,f'ภาพสไลด์เรื่อง {title} สำหรับทบทวนหัวข้อ {owner["title"]}')
    figures.append(dict(id=f'fig-{p}',page=p,file=f'slide-{p:03d}.png',title=f'{title} · หน้า {p}',
                        caption=f'{caption} ({SOURCE}, หน้า {p})'))

flashcards=[dict(front=t['title'],back=t['remember'][0],pages=t['pages']) for t in topics]
term_cards=[
 ('I/O module','เชื่อม system bus กับ peripheral devices','หน้า 3'),
 ('External device 3 กลุ่ม','human readable, machine readable, communication','หน้า 4'),
 ('Transducer','ส่วนแปลงข้อมูลระหว่างอุปกรณ์กับสิ่งแวดล้อมในภาพ','หน้า 5'),
 ('I/O module functions','control/timing, processor/device communication, buffering, error detection','หน้า 6'),
 ('Programmed I/O','processor สั่งและรอ I/O operation ให้เสร็จ','หน้า 8'),
 ('Interrupt-driven I/O','สั่ง I/O แล้วทำงานอื่น; module interrupt เมื่อเสร็จ','หน้า 8, 15'),
 ('DMA','I/O module กับ main memory แลกข้อมูลตรงโดยไม่ให้ processor อยู่ในทางเดินข้อมูล','หน้า 8–9'),
 ('Control/Test/Read/Write','สั่งงาน/ตรวจสถานะ/รับเข้า buffer/ส่งออกจาก data bus','หน้า 10'),
 ('Memory-mapped I/O','memory และ devices แชร์ address space','หน้า 12–14'),
 ('Isolated I/O','แยก address space และมี I/O commands เฉพาะ','หน้า 13–14'),
 ('PC/PSW ก่อน ISR','processor เก็บบน control stack ก่อนโหลด PC ใหม่','หน้า 16'),
 ('Vectored interrupt','ใช้ vector ชี้ device-service routine','หน้า 19'),
 ('DREQ/DACK','DMA request / DMA acknowledge ในภาพ 8237','หน้า 28'),
 ('HRQ/HLDA','HOLD request / HOLD acknowledge ในภาพ 8237','หน้า 28'),
 ('8237 channels','4 ช่อง หมายเลข 0, 1, 2, 3','หน้า 29'),
 ('DCA prototype','memory controller ส่ง prefetch hint สำหรับ incoming network traffic','หน้า 36'),
 ('DDIO','ตัวอย่าง cache injection ให้ I/O transfer ผ่าน last-level cache','หน้า 36–37'),
 ('Selector/Multiplexor','I/O channel architectures สองแบบในแผนภาพ','หน้า 39'),
 ('USB root host controller','เชื่อมอุปกรณ์เป็น hierarchical tree ตามสไลด์','หน้า 41'),
 ('FireWire','IEEE 1394 serial bus, daisy chain และ hot plugging','หน้า 42'),
 ('SCSI','Small Computer System Interface; shared parallel bus ตามสไลด์','หน้า 43'),
 ('SATA','Serial Advanced Technology Attachment สำหรับ disk storage','หน้า 46'),
 ('Ethernet/Wi-Fi','wired switch-based / wireless IEEE 802.11 ตามสไลด์','หน้า 47–48'),
]
flashcards += [dict(front=f,back=b,pages=p) for f,b,p in term_cards]

data=dict(
 source=SOURCE,sourcePageCount=52,
 course='ITDS-211 · Computer Architecture & Operating System',
 instructor='W. Suntiamorntut, Ph.D.',
 chapter='Chapter05 · I/O Systems',
 description='จาก I/O module สู่ programmed/interrupt-driven I/O, DMA, DCA/DDIO, I/O channel และตัวอย่างการเชื่อมต่อ',
 notice='เลขหน้าคือหน้า PDF 1–52; หน้า 40 เป็นโจทย์รายงานกลุ่ม และหน้า 41–48 เป็นหัวข้อรายงานตามสไลด์ ตัวเลขบางจุดในหน้า 30, 46, 49 ต้องตรวจต้นฉบับ',
 purpose='บทนี้เรียนเพื่อเข้าใจว่า processor, I/O module, อุปกรณ์ภายนอก, memory และ cache ประสานการรับส่งข้อมูลอย่างไร โดยเทียบเวลารอและทางเดินข้อมูลของ programmed, interrupt-driven, DMA และ DCA/DDIO แล้วมองการขยายระบบด้วย I/O channels และตัวอย่าง interfaces',
 purposePages='หน้า 2–3, 6–9, 24–39, 41–51',
 objectiveNote='วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจากหัวข้อและแผนภาพในสไลด์',
 flashcardNote='Flashcards ยึดชื่อส่วนประกอบ กลไก สัญญาณ และนิยามจากสไลด์; ตัวเลขเทคโนโลยีเป็นข้อมูลประจำเอกสาร ไม่ใช่สเปกปัจจุบัน',
 goals=[
   dict(text='ระบุองค์ประกอบ external device และ I/O module พร้อมหน้าที่ของแต่ละส่วน',pages='หน้า 3–7'),
   dict(text='เปรียบเทียบ programmed, interrupt-driven และ DMA ทั้งเวลารอและทางเดินข้อมูล รวม I/O addressing/commands',pages='หน้า 8–14, 24–30'),
   dict(text='ไล่ interrupt, ระบุ requester/priority และอธิบายผลของ cache ต่อ network I/O พร้อม DCA/DDIO',pages='หน้า 15–23, 31–37'),
   dict(text='อ่าน I/O channels และแยกบทบาท interfaces/IBM channel ที่เป็นตัวอย่างในสไลด์',pages='หน้า 38–39, 41–51')],
 limits=[
   'อ่านและตรวจภาพครบ 52 หน้า: หน้า 1 ปก, หน้า 2 Course Outline, หน้า 52 Q&A; เนื้อหาหลักหน้า 3–39 และตัวอย่างหน้า 41–51',
   'หน้า 40 เป็น Assignment ให้รายงานกลุ่ม 9 เรื่อง และหน้า 41–48 เป็นหัวข้อรายงาน; ไม่มีหลักฐานว่าส่วนนี้มีน้ำหนักข้อสอบเท่าใด',
   'ไม่มี Chapter Objectives แบบรายการชัดเจนหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; การจัดระดับเป็นการจัดเวลาอ่าน',
   'หน้า 21–22 ใช้ชื่อ Intel 8255A แต่ภาพหน้า 23 ใช้ 82C55A; อ่านชื่อรุ่นตามหน้าต้นฉบับ',
   'หน้า 30 ตาราง Intel 8237A status แถว D4–D7 พิมพ์ Channel 0 request ซ้ำ: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 46 คำอธิบาย SATA วาง 6 Gbps กับ 300 Mbps ต่อ device โดยไม่แจกเงื่อนไข: ต้องตรวจสอบจากต้นฉบับก่อนใช้คำนวณ',
   'หน้า 49 ภาพ IBM EC12 เขียน ≤60 และ ≤1024 partitions/system คนละตำแหน่ง: ต้องตรวจสอบจากต้นฉบับ',
   'อัตราและคำว่า current ในหน้า 31, 41–48 เป็นคำในสไลด์ ไม่ใช่ข้อมูลสเปกหรือสถานะเทคโนโลยีปัจจุบัน',
   'Chapter05 ไม่มีตัวอย่างโจทย์คำนวณแยกเป็นข้อในสไลด์ จึงเน้นคำถามเลือกตอบ อัตนัย และวิเคราะห์ภาพ/ทางเดินข้อมูล'],
 figures=figures,topics=topics,
 roadmap=[
   dict(title='1 · โครงสร้าง I/O',text='เริ่ม system bus–module–external device แล้วจำห้าหน้าที่ของ I/O module',pages='หน้า 3–7',topic='io-model'),
   dict(title='2 · คำสั่งและทางเดินข้อมูล',text='เทียบ programmed/interrupt-driven/DMA, command 4 ชนิด และ addressing สองแบบ',pages='หน้า 8–14',topic='io-techniques'),
   dict(title='3 · Interrupt',text='ไล่ PC/PSW/ISR แล้วตอบว่า device ใดร้องขอและจัด priority อย่างไร',pages='หน้า 15–23',topic='interrupt-processing'),
   dict(title='4 · DMA',text='จับข้อจำกัดสองวิธีแรก → DMA controller/breakpoints/configurations/8237',pages='หน้า 24–30',topic='dma-motivation'),
   dict(title='5 · Cache กับ network I/O',text='ตาม packet buffers/cache miss ก่อนเทียบ DCA prefetch กับ DDIO cache injection',pages='หน้า 31–37',topic='dca-motivation'),
   dict(title='6 · ระบบใหญ่และ interfaces',text='จบด้วยวิวัฒนาการ/channel แล้วอ่านหน้า 41–51 ในฐานะตัวอย่างและหัวข้อรายงาน',pages='หน้า 38–51',topic='io-evolution')],
 plan=[
   dict(title='รอบ 1 · ผังภาพรวม',task='อ่านหน้า 3–9 แล้ววาดเส้นทาง bus→I/O module→device กับเปรียบ 3 เทคนิค',check='บอกได้ว่า CPU รอหรือไม่ และ data ผ่าน CPU หรือไม่ในแต่ละเทคนิค',pages='หน้า 3–9'),
   dict(title='รอบ 2 · Trace คำสั่งและ interrupt',task='ไล่ Control/Test/Read/Write, memory-mapped/isolated และภาพ interrupt หน้า 16–19',check='เล่าลำดับเก็บ/คืน PC/PSW และวิธีระบุ requester ได้',pages='หน้า 10–19'),
   dict(title='รอบ 3 · Trace DMA',task='อ่านข้อจำกัดหน้า 24 แล้วตาม data count/address, breakpoint, DREQ/DACK/HRQ/HLDA และ configurations',check='ชี้ผู้ขอ DMA, ผู้ขอ bus และทางเดิน block ได้',pages='หน้า 24–30'),
   dict(title='รอบ 4 · Cache/Channel/ตัวอย่าง',task='ตาม incoming/outgoing packet, DCA/DDIO, I/O channel แล้วทวนกลุ่ม interface ตามบทบาท',check='อธิบาย buffer copy กับ cache injection และแยก wired/wireless/storage/server interfaces ได้จากสไลด์',pages='หน้า 31–51'),
   dict(title='รอบ 5 · ทดสอบเว้นระยะ',task='ตอบ 3 ข้อต่อหัวข้อแล้วสุ่ม Quiz; วันถัดไปทวนข้อที่ผิดและเปิดภาพสไลด์ต้นทาง',check='ตอบครบหัวข้อสำคัญและชี้หน้า 30/46/49 ที่ต้องตรวจต้นฉบับได้',pages='หน้า 3–51')],
 cram=[
   dict(title='ถ้าเหลือ 3 วัน',text='วัน 1 module/สามเทคนิค/commands/mapping หน้า 3–14; วัน 2 interrupt/DMA หน้า 15–30; วัน 3 DCA/channel/interfaces หน้า 31–51 พร้อม Quiz'),
   dict(title='ถ้าเหลือ 1 วัน',text='เรียงสามเทคนิค/ผังหน้า 8–11 → mapping/interrupt หน้า 12–19 → DMA หน้า 24–30 → DCA/DDIO หน้า 33–37 → interface เฉพาะศัพท์ที่ยังสับสน หน้า 41–51'),
   dict(title='ถ้าเหลือ 3 ชั่วโมง',text='0–35 นาทีโครงสร้าง/สามเทคนิค หน้า 3–11; 35–70 นาที mapping/interrupt หน้า 12–19; 70–125 นาที DMA หน้า 24–30; 125–155 นาที DCA/DDIO/channel หน้า 31–39; 155–180 นาที interface key terms/Quiz')],
 strategyIntro='หัวข้อกลไกและผังการโอนข้อมูลมีน้ำหนักในการทบทวนมากกว่าตัวเลขรุ่น interface เพราะเป็นฐานต่อเนื่องในสไลด์; ไม่มีข้อสอบเก่า จึงไม่ยืนยันความถี่ออกสอบ',
 strategy=[
   dict(title='ควรท่องจำ',text='I/O module functions, สาม I/O techniques, Control/Test/Read/Write, memory-mapped/isolated, PC/PSW, interrupt identification, DREQ/DACK/HRQ/HLDA (หน้า 6–19, 25–29)'),
   dict(title='ควรฝึกโจทย์',text='ไล่ผังรับ block หน้า 11, keyboard addressing หน้า 14, simple interrupt หน้า 16–17, DMA breakpoints/configurations หน้า 26–28 และ DMA/DDIO หน้า 37'),
   dict(title='ควรเข้าใจแนวคิด',text='เหตุผลใช้ DMA, packet buffer/cache miss, DCA prefetch versus DDIO cache injection, I/O channel evolution (หน้า 24, 31–39)'),
   dict(title='เตรียมข้อสอบแบบผสม',text='เลือกตอบจับคู่คำศัพท์/สัญญาณ; อัตนัยอธิบาย sequence; วิเคราะห์ผังและทางเดิน data. สไลด์ไม่มีโจทย์คำนวณแยก จึงไม่สร้างโจทย์ตัวเลขที่ไม่มีในเอกสาร')],
 flashcards=flashcards)

assert len(topics)==23 and len({t['id'] for t in topics})==23
assert all(len(t['questions'])==3 and t['pages'] and t['summary'] for t in topics)
assert set(f['id'] for f in figures)==set(fid for t in topics for fid in t['figures'])
(HERE/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('topics',len(topics),'figures',len(figures),'questions',sum(len(t['questions']) for t in topics),'flashcards',len(flashcards))
