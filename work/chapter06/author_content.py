"""Chapter06 notes, questions and figure map from the supplied 45-page PDF."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = 'itds-211_comp_arch_Chapter06.pdf'
topics = []


def add(id, title, level, pages, summary, remember, terms, example, confusion, mnemonic, quiz, image_pages=(), comparison=None, formulas=None):
    assert len(quiz) == 3
    m, a, b = quiz
    questions = [
        dict(type='เลือกตอบ', q=m[0], options=m[1], correct=m[2], answer=m[3], pages=pages),
        dict(type='อัตนัย', q=a[0], answer=a[1], pages=pages),
        dict(type='คำนวณ' if any(x in b[0] for x in ('คำนวณ', 'จงหา', 'เท่าไร')) else 'วิเคราะห์', q=b[0], answer=b[1], pages=pages),
    ]
    entry = dict(id=id, title=title, level=level, pages=pages,
        reason={'core':'เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด',
                'important':'เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก',
                'extra':'เป็นตารางรุ่นหรือรายละเอียดตัวอย่างตามช่วงเวลาของสไลด์'}[level],
        summary=summary, remember=remember, terms=terms, example=example,
        confusion=confusion, mnemonic=mnemonic, questions=questions,
        figures=[f'fig-{p}' for p in image_pages])
    if comparison: entry['comparison'] = dict(headers=comparison[0], rows=comparison[1])
    if formulas: entry['formulas'] = formulas
    topics.append(entry)


add('magnetic-medium','สื่อแม่เหล็กและหัวอ่าน/เขียน','core','หน้า 4–6',
    'Magnetic disk ใช้ platter ที่เคลือบวัสดุแม่เหล็กและเก็บบิตด้วยสภาพการเป็นแม่เหล็กของบริเวณเล็ก ๆ. สไลด์เทียบวัสดุฐานอะลูมิเนียมกับแก้ว และแสดงหัวเขียนแบบ inductive กับหัวอ่านแบบ magnetoresistive. การอ่านกับเขียนจึงเป็นกระบวนการคนละทิศของการแปลงสัญญาณและสภาพแม่เหล็ก.',
    ['Platter มี substrate และ magnetizable coating (หน้า 4)','ฐานแก้วช่วยผิวสม่ำเสมอ ลด defect และเอื้อ fly height ต่ำในสไลด์ (หน้า 4)','ภาพแยก inductive write กับ magnetoresistive read (หน้า 5–6)'],
    ['platter','substrate','magnetizable material','inductive write','magnetoresistive read','read/write head'],
    'อ่านภาพหน้า 5–6 โดยตามทิศสัญญาณจากหัวเขียนสู่สื่อ และจากสื่อกลับสู่หัวอ่าน',
    'อย่านำชนิดหัวอ่านไปเรียกว่าหัวเขียน; บิตในภาพสัมพันธ์กับสภาพแม่เหล็กบนสื่อ',
    'เขียนให้สื่อเปลี่ยน อ่านจากสื่อกลับมา',
    [('ตัวใดเป็นวัสดุฐาน platter ที่สไลด์กล่าวถึง?',['อะลูมิเนียมและแก้ว','กระดาษและไม้','ซิลิกอนล้วน','เทปโพลีเอสเตอร์'],0,'อะลูมิเนียมและแก้ว'),('หัวเขียนและหัวอ่านในภาพหน้า 6 ใช้หลักใด?','หัวเขียน inductive; หัวอ่าน magnetoresistive'),('เหตุใดสไลด์กล่าวถึงฐานแก้ว?','ผิวสม่ำเสมอ defect น้อย เอื้อ fly height ต่ำ เพิ่มความแข็งและทนแรงกระแทก')],range(4,7))

add('disk-layout','Track, sector, cylinder และรูปแบบ sector','core','หน้า 7–9',
    'ผิว platter แบ่งเป็น tracks วงซ้อนและ sectors ตามส่วนโค้ง; cylinder คือ tracks ที่ตำแหน่งรัศมีเดียวกันของหลายผิว. ภาพยังแสดง inter-track/inter-sector gaps และหัวอ่านหนึ่งหัวต่อผิว. สไลด์เปรียบ constant angular velocity กับ multiple zone recording และยก Winchester ST506 เป็นตัวอย่าง sector ที่มี ID, data, CRC และ gaps.',
    ['Track เป็นวง; sector เป็นส่วนของ track; cylinder รวม track ที่รัศมีตรงกัน (หน้า 7)','Multiple zone recording แบ่ง track เป็น zones ให้จำนวน sectors/track ต่างกัน (หน้า 8)','ST506 เป็นตัวอย่าง 600 bytes/sector แต่ data จริง 512 bytes พร้อมข้อมูลจัดรูปแบบ (หน้า 9)'],
    ['track','sector','cylinder','constant angular velocity (CAV)','multiple zone recording','CRC','ID field'],
    'ตัวอย่างหน้า 9: 17+7+41+515+20 = 600 bytes/sector; data field 515 bytes มี synch 1, data 512 และ CRC 2',
    '600 bytes เป็นขนาด physical sector ในตัวอย่าง ST506 ไม่ใช่ 600 bytes ของ user data',
    'วง track–ชิ้น sector–ชั้น cylinder',
    [('หน่วยใดคือ track ที่รัศมีเดียวกันบนหลายผิว?',['Cylinder','Sector','Gap','Spindle'],0,'Cylinder'),('Multiple zone recording ต่างจากการแบ่ง sector แบบเดิมอย่างไร?','แบ่งเป็น zones เพื่อให้จำนวน sectors ต่อ track ต่างกันตามตำแหน่ง'),('คำนวณ overhead ใน sector ตัวอย่าง 600 bytes ที่มี data 512 bytes','600−512 = 88 bytes สำหรับ field/gap/ข้อมูลควบคุมตามภาพ')],(7,8,9),
    formulas=[dict(expr='600 − 512 = 88 bytes',description='overhead ของ sector ST506 ในตัวอย่างหน้า 9; ไม่ใช่ค่าทั่วไปของดิสก์ทุกแบบ',pages='หน้า 9')])

add('disk-types','ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง','important','หน้า 10–13',
    'สไลด์จำแนก fixed-head/movable-head, removable/nonremovable, single-/double-sided, จำนวน platters และระยะสัมผัสหัวกับจาน. หัวที่แคบเพิ่มความหนาแน่นได้ แต่ต้องเข้าใกล้ผิวมากขึ้นและเสี่ยงต่อข้อผิดพลาด. Winchester ใช้ enclosure ปิดเพื่อลดสิ่งปนเปื้อน และหัวลอยเหนือผิวเมื่อหมุน; ตารางหน้า 13 เป็นสเปกอุปกรณ์ตัวอย่างของเอกสาร.',
    ['Fixed-head เลือกหัว; movable-head เคลื่อนหัวไป track (หน้า 10–11)','Removable media ถอดออกจาก drive ได้; double-sided ใช้สองผิว (หน้า 10–11)','Winchester ใช้หัวลอยตามอากาศเหนือผิวใน enclosure ปิด (หน้า 12)','ค่ารุ่นในตารางหน้า 13 เป็นตัวอย่างของช่วงเวลาสไลด์'],
    ['fixed-head','movable-head','removable disk','double-sided','Winchester disk','fly height'],
    'ใช้หัวตารางหน้า 13 อ่านความสัมพันธ์ capacity, rpm, seek และ transfer rate ของรุ่นที่ยก ไม่ใช้แทนสเปกปัจจุบัน',
    'fixed-head หมายถึงหัวประจำ track ไม่ใช่ platter หยุดหมุน; ตัวเลขตารางไม่ใช่มาตรฐานปัจจุบัน',
    'เลือกหัวหรือเลื่อนหัว; จานยังหมุน',
    [('แบบใดต้องเคลื่อนหัวไปยัง track?',['Movable-head','Fixed-head','Removable media','Double-sided'],0,'Movable-head'),('เหตุใด Winchester จึงใช้ enclosure ปิด?','ลดสิ่งปนเปื้อนเพื่อให้หัวลอยใกล้ผิวได้ตามสไลด์'),('เมื่อหัวแคบลง ข้อดีและความเสี่ยงที่สไลด์กล่าวคืออะไร?','ความหนาแน่นเพิ่ม แต่ต้องอยู่ใกล้จานมากขึ้นและเสี่ยงข้อผิดพลาด')],range(10,14))

add('disk-timing','เวลา I/O ของ magnetic disk','core','หน้า 14–15',
    'ภาพเวลา I/O แยกการรออุปกรณ์ รอ channel การ seek การรอจานหมุน และการ transfer. Seek time คือเวลาวางหัวที่ track เป้าหมายใน movable-head; rotational delay คือรอ sector มาถึงหัว. Access time ในสไลด์นิยามเป็น seek time + rotational delay แล้วจึงเกิด transfer time.',
    ['Seek time: วางหัวที่ track (หน้า 15)','Rotational delay: รอ sector หมุนมาถึงหัว (หน้า 15)','Access time = seek time + rotational delay; transfer time เกิดเมื่อหัวอยู่ตำแหน่งแล้ว (หน้า 15)','ภาพหน้า 14 ยังแยก device/channel wait'],
    ['seek time','rotational delay / rotational latency','access time','transfer time','device busy','wait for channel'],
    'จากนิยามหน้า 15 ให้รวม seek time กับ rotational delay เพื่อหา access time โดยแยก transfer time ไว้หลังจากนั้น',
    'อย่ารวม transfer หรือ device/channel wait เข้า access time ตามนิยามหน้า 15',
    'เข้าถึง = หา track + รอ sector; จากนั้นถ่ายข้อมูล',
    [('Access time ตามสไลด์ประกอบด้วยอะไร?',['Seek + rotational delay','Seek + transfer','Channel wait + transfer','Transfer เท่านั้น'],0,'Seek + rotational delay'),('ลำดับ seek, rotational delay และ transfer เป็นอย่างไร?','วางหัวที่ track → รอ sector หมุนมาถึง → อ่าน/เขียนข้อมูล'),('จงเขียนวิธีคำนวณ access time จาก seek time และ rotational delay','นำ seek time บวก rotational delay; ไม่รวม transfer time ตามนิยามหน้า 15')],(14,15),
    formulas=[dict(expr='Access time = seek time + rotational delay',description='นิยามในสไลด์ ไม่รวม transfer time หรือเวลา wait for device/channel',pages='หน้า 15')])

add('raid-framework','RAID: ภาพรวมและจำนวนดิสก์','core','หน้า 16–19',
    'RAID (Redundant Array of Independent Disks) ทำให้หลาย physical disks ปรากฏเป็น logical drive และกระจายข้อมูลด้วย striping. ตารางแยก RAID 0–6 ตาม nonredundant, mirroring, Hamming และ parity รวมทั้ง parallel versus independent access. จำนวนดิสก์ในตารางคือ RAID 0 = N, RAID 1 = 2N, RAID 2 = N+m, RAID 3–5 = N+1 และ RAID 6 = N+2.',
    ['N คือจำนวน data disks; m แปรตาม log N ใน RAID 2 (หน้า 17)','RAID 2–3 เป็น parallel access; RAID 4–6 เป็น independent access (หน้า 17)','หน้า 16 กล่าวว่าทุกระดับมี redundancy แต่หน้า 17 ระบุ RAID 0 nonredundant: ต้องตรวจสอบจากต้นฉบับ'],
    ['RAID','logical drive','striping','mirroring','parity','N','m'],
    'ไล่ตารางหน้า 17 แล้วจับคู่ระดับกับวิธี redundancy และจำนวนดิสก์ ก่อนอ่านภาพการจัด strip หน้า 18–19',
    'ข้อความเหมารวมเรื่อง parity/redundancy หน้า 16 ขัดกับ RAID 0 หน้า 17–18; ต้องตรวจสอบจากต้นฉบับ',
    '0 ไม่มีสำรอง; 1 ทำคู่; 2–6 ต่างวิธีตรวจและกระจาย',
    [('RAID ระดับใด nonredundant ตามตาราง?',['0','1','5','6'],0,'0'),('N และ m ในตาราง RAID หมายถึงอะไร?','N = จำนวน data disks; m = จำนวน redundant disks ของ RAID 2 ที่แปรตาม log N'),('ตารางต้องใช้กี่ดิสก์สำหรับ RAID 6 เมื่อ N=4?','N+2 = 6 ดิสก์ ตามตารางหน้า 17')],(16,17,18,19),
    comparison=(['ระดับ','รูปแบบ','จำนวนดิสก์'],[['0','nonredundant striping','N'],['1','mirroring','2N'],['2','Hamming code','N+m'],['3/4/5','parity ต่างการจัดวาง','N+1'],['6','dual distributed parity','N+2']]))

add('raid0','RAID 0: striping ไม่มี redundancy','core','หน้า 18, 20–21',
    'RAID 0 แบ่ง logical data เป็น strips กระจายบนดิสก์หลายตัวโดยไม่สำรอง. ภาพหน้า 20 แสดง logical strips 0–15 แมปไปสี่ physical disks. ความเร็วขึ้นกับทั้งทางเดินจาก host memory ไปดิสก์และรูปแบบ I/O request; small request มักถูก seek/rotational latency ครอบงำ ส่วนหลาย request กระจายภาระได้.',
    ['Nonredundant; ใช้ N ดิสก์ตามตาราง (หน้า 17–18)','logical strips กระจายลง physical disks (หน้า 20)','small request ถูก seek/rotation ครอบงำ; large strip อาจให้หลาย request ทำพร้อมกัน (หน้า 21)'],
    ['RAID 0','strip','striping','logical disk','physical disk','load balancing'],
    'ตาม strip 0,1,2,3 ในภาพหน้า 20 จะอยู่คนละ physical disk ก่อนวนกลับ',
    'RAID 0 ไม่มี parity หรือ mirror แม้หน้า 16 จะพูดถึงคุณลักษณะ RAID แบบรวม',
    'ศูนย์ = กระจาย แต่ไม่สำรอง',
    [('RAID 0 เก็บข้อมูลสำรองแบบใด?',['ไม่มี','mirror','parity แยก','dual parity'],0,'ไม่มี'),('เงื่อนไขสองข้อของ high transfer capacity หน้า 21 คืออะไร?','ทางเดิน host–disk ต้องรองรับสูง และ application ออก request ที่ใช้อาร์เรย์ได้มีประสิทธิภาพ'),('เหตุใด small I/O request จึงไม่ใช่การถ่ายข้อมูลอย่างเดียว?','เวลามักถูก seek และ rotational latency ครอบงำตามหน้า 21')],(20,21))

add('raid1','RAID 1: mirroring','core','หน้า 18, 22',
    'RAID 1 ทำสำเนาข้อมูลทั้งชุด โดย logical strip หนึ่งแมปลงดิสก์สองตัวที่เป็น mirror กัน. อ่านจากตัวใดก็ได้ และเมื่อไดรฟ์เสียจะเข้าถึงจากสำเนาอีกตัวแล้วฟื้นระบบได้ง่าย. สไลด์ระบุว่าไม่มี “write penalty” ในความหมายของตน และข้อเสียหลักคือค่าใช้จ่ายของดิสก์ที่ซ้ำ.',
    ['Mirroring = duplicate all data; 2N disks (หน้า 17–18, 22)','อ่านจากดิสก์คู่ใดก็ได้และสำรองแบบ real time (หน้า 22)','สไลด์กล่าวไม่มี “write penalty”; ข้อเสียหลักคือ cost (หน้า 22)'],
    ['RAID 1','mirroring','mirror disk','logical strip','read request'],
    'ภาพหน้า 18 วาง strip ชุดเดียวกันซ้ำทั้งฝั่งซ้ายและขวา',
    'การเขียนยังต้องทำสำเนา แต่สไลด์ใช้คำว่าไม่มี “write penalty”; อย่าตีความเป็นเขียนดิสก์เดียว',
    'หนึ่ง = มีคู่สำเนา',
    [('RAID 1 ได้ redundancy โดยอะไร?',['Mirroring','Hamming','single parity','dual parity'],0,'Mirroring'),('เหตุใดอ่านข้อมูลได้เมื่อดิสก์ตัวหนึ่งเสีย?','มี mirror disk ที่เก็บข้อมูลเดียวกัน'),('ถ้า N=4 data disks ตารางหน้า 17 ให้ RAID 1 ใช้ทั้งหมดกี่ดิสก์?','2N = 8 ดิสก์')],(22,))

add('raid2','RAID 2: Hamming code','important','หน้า 18, 23',
    'RAID 2 ใช้ parallel access ที่ดิสก์ทำงานร่วมกันทุก I/O request และกระจายข้อมูลเป็น strips เล็กระดับ byte/word. คำนวณ Hamming code ข้ามบิตจาก data disks แล้วเก็บ code บน redundant disks หลายตัว. ตามสไลด์ Hamming code แก้ single-bit error และตรวจ double-bit error ได้ โดยจำนวนดิสก์เสริมแปรตาม log N.',
    ['parallel access และ synchronized spindles (หน้า 23)','strips เล็กมากและ Hamming ECC เก็บบนหลายดิสก์ (หน้า 18, 23)','single-bit correction/double-bit detection ตามสไลด์ (หน้า 23)'],
    ['RAID 2','parallel access','Hamming code','ECC','N+m'],
    'ดูภาพหน้า 18: b0–b3 เป็นข้อมูล และ f0(b)–f2(b) เป็น code ที่แยกดิสก์',
    'Hamming code ของ RAID 2 ไม่ใช่ parity disk เดียวแบบ RAID 3',
    'สอง = code หลายดิสก์',
    [('RAID 2 ใช้รหัสใดตามสไลด์?',['Hamming','CRC อย่างเดียว','AES','NTFS'],0,'Hamming'),('parallel access ใน RAID 2 หมายถึงอะไร?','member disks ร่วมทำทุก I/O request และ spindle synchronized'),('RAID 2 ต่าง RAID 3 ใน redundancy อย่างไร?','RAID 2 ใช้ Hamming code บนหลายดิสก์; RAID 3 ใช้ parity disk เดียว')],(23,))

add('raid3','RAID 3: bit-interleaved parity','core','หน้า 19, 24',
    'RAID 3 ใช้ parallel access และ strips เล็ก โดยคำนวณ parity จากบิตตำแหน่งตรงกันบน data disks แล้วเก็บบนดิสก์สำรองหนึ่งตัว. สไลด์ยกอัตรา transfer สูงและการ reconstruct เมื่อดิสก์เสีย. ระหว่างซ่อมยังมีข้อมูลใน reduced mode แต่ workload แบบ transaction-oriented ทำงานด้อยลง.',
    ['parity disk เดียวไม่ว่าขนาดอาร์เรย์ (หน้า 24)','parallel access และ small strips (หน้า 24)','เสียหนึ่งตัว: reconstruct จากดิสก์ที่เหลือกับ parity และทำงาน reduced mode (หน้า 24)'],
    ['RAID 3','bit-interleaved parity','parallel access','reduced mode','parity disk'],
    'ดู P(b) บนดิสก์ขวาของ RAID 3 ในภาพหน้า 19',
    'RAID 3 เป็น parallel access; อย่าสลับกับ RAID 4 ที่เป็น independent access',
    'สาม = parity หนึ่งตัวและดิสก์ทำพร้อมกัน',
    [('RAID 3 ใช้ redundant disks กี่ตัว?',['หนึ่ง','สอง','N','ไม่มี'],0,'หนึ่ง'),('reduced mode หน้า 24 คืออะไร?','ยังเข้าถึงข้อมูลได้หลังดิสก์เสียโดย reconstruct จาก parity และดิสก์ที่เหลือ'),('เหตุใด transaction-oriented workload จึงเป็นข้อเสียของ RAID 3 ตามสไลด์?','สไลด์ระบุ performance suffers สำหรับ workload นี้ ขณะที่ทุกดิสก์ร่วมกันต่อ I/O request')],(24,))

add('raid4','RAID 4: block parity แยกดิสก์','core','หน้า 19, 25',
    'RAID 4 ใช้ independent access และ strips ค่อนข้างใหญ่ โดย parity ของแต่ละกลุ่มอยู่บนดิสก์เฉพาะ. การเขียน strip เล็กต้องอ่าน old user strip กับ old parity แล้วเขียน user strip และ parity ใหม่ จึงเป็น 2 reads + 2 writes. ดิสก์ parity กลายเป็นคอขวดของการเขียนที่สไลด์ชี้ให้เห็น.',
    ['independent access: ดิสก์รับ request แยกกันได้ (หน้า 25)','large strips และ dedicated parity disk (หน้า 19, 25)','small write = 2 reads + 2 writes (หน้า 25)'],
    ['RAID 4','independent access','block-interleaved parity','dedicated parity disk','write penalty'],
    'ติดตาม P(0–3), P(4–7) ในภาพหน้า 19: parity อยู่คอลัมน์เดิม',
    'อย่าสับสนกับ RAID 5 ที่ parity หมุนเวียนบนทุกดิสก์',
    'สี่ = parity ดิสก์เดียว; เขียนต้องแตะสี่ครั้ง',
    [('small strip write ของ RAID 4 มี I/O กี่ครั้งตามสไลด์?',['2 reads + 2 writes','1 read + 1 write','4 reads','ไม่มี parity I/O'],0,'2 reads + 2 writes'),('เหตุใด dedicated parity disk อาจเป็นคอขวด?','ทุกการปรับ parity ต้องเข้าไปยังดิสก์เดียว'),('ถ้าเขียนหนึ่ง strip เล็ก จงนับ read/write ตามหน้า 25','อ่าน old user+old parity = 2; เขียน new user+new parity = 2')],(25,))

add('raid5','RAID 5: distributed parity','core','หน้า 19, 26',
    'RAID 5 จัด block-level strips คล้าย RAID 4 แต่หมุนตำแหน่ง parity strips ไปตามดิสก์ทุกตัว มักเป็น round-robin. การกระจายนี้หลีกเลี่ยงคอขวด I/O บน dedicated parity disk ของ RAID 4. ตารางหน้า 17 จัดเป็น N+1 disks และ independent access.',
    ['distributed parity; ไม่ fix บนดิสก์เดียว (หน้า 19, 26)','typical allocation แบบ round-robin (หน้า 26)','หลีกเลี่ยง RAID 4 parity-disk bottleneck (หน้า 26)'],
    ['RAID 5','block-interleaved distributed parity','round-robin','independent access','N+1'],
    'ดูภาพหน้า 19: P(0–3), P(4–7), P(8–11) ย้ายตำแหน่งดิสก์',
    'หน้า 26 แบ่งสองคอลัมน์: dual parity เป็นของ RAID 6 ไม่ใช่ RAID 5',
    'ห้า = parity หมุนเวียน',
    [('RAID 5 แก้ bottleneck RAID 4 ด้วยอะไร?',['กระจาย parity','เพิ่ม dedicated parity disk','เอา parity ออก','เปลี่ยนเป็น tape'],0,'กระจาย parity'),('RAID 5 กับ RAID 4 ต่างกันตรงตำแหน่ง parity อย่างไร?','RAID 4 ใช้ดิสก์ parity เฉพาะ; RAID 5 กระจาย parity strips'),('เมื่อ N=4 ตารางหน้า 17 ให้ RAID 5 รวมกี่ดิสก์?','N+1 = 5 ดิสก์')],(26,))

add('raid6','RAID 6: dual distributed parity','core','หน้า 19, 26',
    'RAID 6 ใช้ parity สองชุดจากการคำนวณต่างกัน เก็บคนละ block บนคนละดิสก์. สไลด์อธิบาย data availability สูง: ต้องมีสามดิสก์เสียภายใน mean time to repair (MTTR) จึงทำข้อมูลหายตามเงื่อนไขที่กล่าว. แลกกับ write penalty เพราะการเขียนหนึ่งครั้งกระทบ parity สอง block; ตารางจัด N+2 ดิสก์.',
    ['dual distributed parity หรือ P และ Q ในภาพ (หน้า 19, 26)','parity สอง block กระทบเมื่อเขียน (หน้า 26)','ตารางให้ N+2 disks (หน้า 17)','คำอธิบายสามดิสก์เสียผูกกับช่วง MTTR ตามสไลด์ (หน้า 26)'],
    ['RAID 6','dual parity','P/Q','MTTR','N+2','write penalty'],
    'เทียบ P(0–3) และ Q(0–3) ในภาพหน้า 19 ซึ่งอยู่คนละดิสก์',
    'อย่าตีความประโยคสามดิสก์เสียโดยละคำว่า within MTTR interval ในสไลด์',
    'หก = parity สองชุด',
    [('RAID 6 เก็บ parity กี่ชุด?',['สอง','หนึ่ง','ไม่มี','N ชุด'],0,'สอง'),('เหตุใดสไลด์ระบุ write penalty ของ RAID 6?','การเขียนหนึ่งครั้งกระทบ parity สอง blocks'),('ถ้า N=4 RAID 6 ใช้กี่ดิสก์ตามตาราง?','N+2 = 6 ดิสก์')],())

add('raid-tables','ตารางเปรียบเทียบ RAID และการเลือกอ่าน','important','หน้า 17, 27–28',
    'ตาราง RAID เปรียบ data availability, large transfer, small request และตัวอย่างการใช้งานของแต่ละระดับ. ใช้อ่านเชิงเปรียบเทียบกับภาพหน้า 18–19: RAID 0 เน้น striping แต่ไม่มี redundancy, RAID 1 ทำ mirror, RAID 2–3 ทำงานแบบ parallel และ RAID 4–6 เป็น independent access. ตารางหน้า 27–28 เป็นการจัดกลุ่มและตัวอย่างของเอกสาร ไม่ใช่คำรับรองความเหมาะสมของระบบปัจจุบัน.',
    ['จับคู่ level ↔ redundancy ↔ disks required จากหน้า 17','แยก parallel access (2–3) กับ independent access (4–6)','ตารางหน้า 27–28 มีตัวอย่าง application/use ในสไลด์'],
    ['data availability','large I/O data transfer capacity','small I/O request rate','parallel access','independent access'],
    'เมื่อเจอ workload ในตาราง ให้เริ่มจาก read/write/transfer pattern แล้วกลับไปดูคอลัมน์ระดับที่ตรง',
    'คอลัมน์ performance เป็นการเปรียบเทียบภายใต้เงื่อนไขของตาราง; ห้ามแปลงเป็นอันดับสากลโดยไม่ดูบริบท',
    'ดูวิธีสำรองก่อนดูความเร็ว',
    [('RAID 4–6 อยู่หมวด access ใดในตาราง?',['Independent','Parallel','Serial tape','Optical'],0,'Independent'),('สามเกณฑ์เปรียบเทียบหลักในหน้า 17 คืออะไร?','data availability, large I/O data transfer capacity และ small I/O request rate'),('เหตุใดจึงไม่ควรใช้ตารางหน้า 27–28 เป็นคำแนะนำซื้ออุปกรณ์ปัจจุบัน?','เป็นตัวอย่างและการเปรียบเทียบตามสไลด์ ไม่ระบุข้อมูลสเปกหรือราคา ณ ปัจจุบัน')],(27,28))

add('ssd-contrast','SSD เทียบ HDD ในสไลด์','important','หน้า 29–30',
    'สไลด์ยกข้อดีของ SSD ต่อ HDD เช่น IOPS สูง เวลาเข้าถึง/latency ต่ำ เสียงและพลังงานต่ำ ตลอดจนความทนทานเชิงกล. ตารางหน้า 30 เทียบ NAND SSD กับ Seagate laptop HDD ด้วยรุ่น ความเร็ว กำลังไฟ ความจุ และราคาในช่วงที่จัดทำสไลด์. จึงใช้เพื่อฝึกอ่านเกณฑ์เปรียบเทียบ ไม่ใช้ราคาหรือสเปกนั้นแทนปัจจุบัน.',
    ['SSD ไม่มีการรอหัว/จานแบบ HDD ตามภาพรวมข้อดีในหน้า 29','เกณฑ์หน้า 30: performance, power, capacity, cost','ตัวเลขและคำว่า current ในเอกสารเป็นข้อมูล ณ เวลาสไลด์'],
    ['SSD','HDD','NAND','IOPS','access time','latency'],
    'เลือกคอลัมน์หนึ่งในตารางหน้า 30 เช่น power แล้วเทียบเฉพาะรุ่นที่สไลด์ยก',
    'ข้อดีในสไลด์เป็นการเทียบตามบริบท ไม่ใช่คำรับรองว่า SSD ทุกรุ่นดีกว่า HDD ทุกด้านในปัจจุบัน',
    'SSD ดู latency และ IOPS; ตารางรุ่นให้อ่านเป็นตัวอย่าง',
    [('ตัวชี้วัดใดอยู่ในข้อดี SSD หน้า 29?',['IOPS','seek arm length','tape speed','optical pit depth'],0,'IOPS'),('ตารางหน้า 30 ใช้เปรียบเทียบอะไร?','NAND SSD กับ laptop HDD ตัวอย่างตาม performance, power, capacity, cost'),('เหตุใดไม่ควรจดจำราคาหน้า 30 เป็นราคาปัจจุบัน?','เป็นตารางรุ่นในสไลด์ ไม่ใช่ข้อมูลราคาปัจจุบัน')],(29,30))

add('ssd-architecture','โครงสร้าง SSD','core','หน้า 31',
    'ภาพ SSD architecture ต่อ host system ซึ่งมี OS, file system และ I/O driver ผ่าน interface ไปยัง controller ของ SSD. ภายใน controller มี addressing, data buffer/cache และ error correction ก่อนเชื่อม flash memory components. ภาพนี้ช่วยแยกส่วนซอฟต์แวร์ฝั่ง host ออกจากส่วนควบคุมและสื่อ flash ฝั่ง SSD.',
    ['host: OS/file system/I/O driver/interface','SSD: interface/controller/addressing/buffer-cache/error correction/flash components','controller เป็นจุดจัดการก่อนถึง flash'],
    ['host system','SSD interface','controller','addressing','data buffer/cache','error correction','flash memory'],
    'ไล่ภาพจาก I/O driver → host interface → SSD interface → controller → flash memory',
    'อย่าใส่ file system ไว้ใน SSD controller; ในภาพมันอยู่ฝั่ง host',
    'host สั่ง–controller จัด–flash เก็บ',
    [('ส่วนใดอยู่ฝั่ง host ในภาพ?',['File system software','Flash memory components','SSD controller','Error correction block'],0,'File system software'),('SSD controller ในภาพเชื่อมกับฟังก์ชันใด?','addressing, data buffer/cache, error correction และ flash components'),('ตามภาพข้อมูลจาก host ไป flash ผ่านส่วนใดบ้าง?','interfaces → controller/addressing/buffer-cache/error correction → flash components')],(31,))

add('ssd-practical','ปัญหาการเขียนและอายุใช้งาน SSD','core','หน้า 32',
    'สไลด์อธิบายว่า performance ของ SSD มีแนวโน้มช้าลงเมื่อใช้งาน เพราะแก้ข้อมูลใน flash block ต้องอ่าน block เข้า RAM buffer ลบทั้ง block แล้วเขียนกลับ. Flash มีจำนวนรอบเขียนจำกัด จึงใช้ cache เพื่อรวม writes, wear leveling เพื่อกระจายการเขียน และ bad-block management. อุปกรณ์ยังประเมิน remaining lifetime เพื่อให้ระบบเตรียมรับความเสียหาย.',
    ['read entire block → RAM buffer → erase entire block → write back (หน้า 32)','write endurance จำกัด; cache/group writes ช่วยลดภาระ (หน้า 32)','wear leveling กระจาย writes; bad-block management จัดการ block เสีย (หน้า 32)'],
    ['RAM buffer','erase block','write endurance','wear leveling','bad-block management','remaining lifetime'],
    'ไล่ขั้นตอนแก้ block ตามลำดับลูกศรในข้อความหน้า 32 ก่อนจำเทคนิคยืดอายุ',
    'wear leveling คือกระจายการเขียน ไม่ใช่การทำสำเนาข้อมูลแบบ RAID 1',
    'อ่าน–ลบทั้ง block–เขียนกลับ; กระจายรอบเขียน',
    [('วิธีใดกระจายจำนวนครั้งเขียนระหว่าง blocks?',['Wear leveling','Mirroring','Seek','Inter-record gap'],0,'Wear leveling'),('เหตุใดการแก้ข้อมูลใน flash block จึงต้องใช้ buffer ตามสไลด์?','ต้องอ่านทั้ง block เข้า RAM ก่อนลบทั้ง block และเขียนกลับ'),('cache หน้า 32 ช่วยเรื่องอายุอย่างไร?','หน่วงและรวม write operations เพื่อลดการเขียนลง flash')],(32,))

add('optical-families','ตระกูล optical disk','important','หน้า 33',
    'ตาราง optical memory แยก CD, DVD และ Blu-Ray พร้อมรุ่น read-only, recordable และ rewritable. แกนสำคัญคือสื่อผลิตข้อมูลมาแล้วอ่านอย่างเดียว, ผู้ใช้เขียนครั้งเดียว หรือเขียนซ้ำได้. ความจุในตารางเป็นค่าของรูปแบบที่สไลด์ยก ไม่ควรถือเป็นคำอธิบายครบทุก variant.',
    ['CD-ROM/DVD-ROM เป็น read-only','CD-R/DVD-R เป็น recordable; CD-RW/DVD-RW เป็น rewritable','Blu-Ray ปรากฏในตารางเป็นตระกูล optical'],
    ['CD-ROM','CD-R','CD-RW','DVD-ROM','DVD-R','DVD-RW','Blu-Ray'],
    'จับคู่ suffix ROM/R/RW กับอ่านอย่างเดียว/บันทึกครั้งเดียว/เขียนซ้ำจากแถวตารางหน้า 33',
    'คำว่า recordable ไม่เท่ากับ rewritable; ตารางไม่ได้ครอบคลุมทุกมาตรฐานใหม่',
    'ROM อ่าน, R เขียนครั้ง, RW เขียนซ้ำ',
    [('suffix ใดหมายถึงเขียนซ้ำในรายการสไลด์?',['RW','ROM','R','ECC'],0,'RW'),('ตารางหน้า 33 แยก optical memory เป็นตระกูลใด?','CD, DVD และ Blu-Ray'),('CD-R ต่าง CD-RW อย่างไรตามรายการ?','CD-R บันทึกครั้งเดียว; CD-RW เขียนซ้ำได้')],(33,))

add('cdrom','CD-ROM: การผลิต การอ่าน และ block format','core','หน้า 34–37',
    'CD-ROM ทำจาก polycarbonate ที่สร้าง pits ตาม master แล้วเคลือบชั้นสะท้อนและป้องกัน; laser อ่านความต่างระหว่าง pit/land ตามภาพ. Block format หน้า 36 มี 2352 bytes: sync 12, ID 4, user data 2048 และ layered ECC 288. สไลด์ยกการทำสำเนาจำนวนมากและสื่อถอดเก็บเป็นข้อดี แต่ read-only และการเข้าถึงช้ากว่า magnetic disk เป็นข้อจำกัด.',
    ['polycarbonate/pits/reflective layer/protective layer ในลำดับผลิต (หน้า 34–35)','12+4+2048+288 = 2352 bytes ต่อ block ในภาพ (หน้า 36)','ROM อ่านอย่างเดียวและใช้แจกจ่ายปริมาณมาก (หน้า 37)'],
    ['polycarbonate','pit','land','laser','sync','ID','L-ECC','CD-ROM'],
    'คำนวณ overhead ของ block หน้า 36: 2352−2048 = 304 bytes ซึ่งมาจาก sync 12 + ID 4 + ECC 288',
    '2352 bytes คือขนาด block รวม; user data คือ 2048 bytes ไม่ใช่ 2352',
    '12–4–2048–288 รวม 2352',
    [('user data ใน CD-ROM block หน้า 36 มีกี่ bytes?',['2048','2352','288','12'],0,'2048'),('ชั้นหลักของแผ่น CD-ROM และหน้าที่ laser ในภาพคืออะไร?','polycarbonate มี pits, ชั้นสะท้อนและป้องกัน; laser อ่านรูปแบบ pit/land'),('คำนวณ overhead เมื่อ block 2352 bytes มี data 2048 bytes','2352−2048 = 304 bytes = sync 12 + ID 4 + ECC 288')],range(34,38),
    formulas=[dict(expr='2352 = 12 (SYNC) + 4 (ID) + 2048 (Data) + 288 (L-ECC) bytes',description='block format ตามภาพ CD-ROM; overhead = 304 bytes',pages='หน้า 36')])

add('cdr-cdrw','CD-R กับ CD-RW','important','หน้า 38',
    'CD-R เป็นสื่อเขียนครั้งเดียวโดยใช้ dye layer ที่เปลี่ยนสภาพเมื่อบันทึก. CD-RW ใช้วัสดุ phase-change ระหว่าง amorphous/crystalline เพื่อให้ลบและเขียนซ้ำได้. สไลด์กล่าวถึงข้อจำกัดอายุการเขียนซ้ำของ CD-RW.',
    ['CD-R: write once ด้วย dye layer','CD-RW: phase-change และ rewritable','amorphous/crystalline เป็นสองสภาพของวัสดุ CD-RW'],
    ['CD-R','CD-RW','dye layer','phase-change','amorphous','crystalline'],
    'แยกคำถามว่า media ใช้ dye หรือ phase-change ก่อนสรุปว่าบันทึกซ้ำได้หรือไม่',
    'CD-R บันทึกครั้งเดียว แม้จะอ่านหลายครั้ง; CD-RW จึงเป็นตัวที่เขียนซ้ำ',
    'R ใช้ dye; RW เปลี่ยน phase',
    [('ชนิดใดใช้ phase-change ตามสไลด์?',['CD-RW','CD-R','CD-ROM','magnetic tape'],0,'CD-RW'),('CD-R กับ CD-RW ต่างกันอย่างไร?','CD-R เขียนครั้งเดียวด้วย dye; CD-RW เปลี่ยนสภาพ amorphous/crystalline เพื่อเขียนซ้ำ'),('เหตุใดจึงไม่ควรเรียก CD-R ว่า rewritable?','สไลด์จัด CD-R เป็น write once; กลไกเขียนซ้ำอยู่ใน CD-RW')],(38,))

add('dvd-bluray','DVD-ROM, Blu-Ray และความหนาแน่น optical','important','หน้า 39–40',
    'ภาพเปรียบ CD-ROM ชั้นเดียวด้านเดียวกับ DVD-ROM แบบ double-sided, dual-layer ที่ laser โฟกัสชั้นข้อมูลต่างกันและต้องพลิกแผ่นเพื่ออ่านอีกด้าน. ตัวอย่างในภาพให้ 682 MB เทียบ 17 GB. ภาพ optical characteristics เทียบความยาวคลื่น CD 780 nm, DVD 650 nm และ Blu-ray 405 nm พร้อม track/pit spacing ต่างกัน.',
    ['DVD-ROM ในภาพเป็น double-sided, dual-layer (หน้า 39)','CD 780 nm, DVD 650 nm, Blu-ray 405 nm ตามภาพ (หน้า 40)','682 MB และ 17 GB เป็นตัวอย่างรูปแบบแผ่นในภาพหน้า 39'],
    ['DVD-ROM','double-sided','dual-layer','semireflective layer','Blu-ray','laser wavelength'],
    'ดูหน้า 39 จากชั้นสะท้อนของแต่ละด้าน แล้วหน้า 40 เทียบ beam spot/pit/track ตาม wavelength',
    '17 GB เป็นตัวอย่าง double-sided dual-layer ในภาพ ไม่ใช่ค่าของ DVD ทุกแผ่น',
    'CD 780 → DVD 650 → Blu-ray 405 nm',
    [('แสงของ Blu-ray ในภาพหน้า 40 ยาวคลื่นเท่าไร?',['405 nm','650 nm','780 nm','1.2 mm'],0,'405 nm'),('ภาพ DVD-ROM หน้า 39 เพิ่มชั้น/ด้านอย่างไร?','double-sided และ dual-layer มีชั้นสะท้อน/กึ่งสะท้อนให้ laser โฟกัสต่างชั้น'),('เรียง wavelength จากยาวไปสั้นตามหน้า 40','CD 780 nm → DVD 650 nm → Blu-ray 405 nm')],(39,40))

add('tape-layout','Magnetic tape: serial และ serpentine','core','หน้า 41–42',
    'Magnetic tape เคลือบวัสดุแม่เหล็กบนแถบ polyester และบันทึกข้อมูลตามแนวยาวเป็น tracks แบบ serial. Physical records หรือ blocks คั่นด้วย inter-record gaps. ภาพหน้า 42 แสดง serpentine ที่ทิศอ่าน/เขียนสลับเมื่อเปลี่ยน track และตัวอย่างระบบอ่าน/เขียน 4 tracks พร้อมกัน.',
    ['polyester tape + magnetizable coating (หน้า 41)','serial recording, parallel longitudinal tracks และ inter-record gaps (หน้า 41)','serpentine สลับทิศระหว่าง tracks; ภาพล่างอ่าน/เขียน 4 tracks พร้อมกัน (หน้า 42)'],
    ['magnetic tape','serial recording','inter-record gap','serpentine','track','physical record'],
    'ตามลูกศร Track 0 → Track 1 → Track 2 ในภาพบนหน้า 42; อีกภาพแสดง block 1–4 อยู่คนละ track ในคอลัมน์แรก',
    'parallel tracks ในเทปหมายถึง tracks หลายแนว; ลำดับเข้าถึงสื่อยังเป็น serial ตามหน้า 41',
    'เทปวิ่งยาว–จบแถวกลับทิศ',
    [('สิ่งใดคั่น physical records บนเทป?',['Inter-record gaps','Sector ID','Parity disk','ECC controller'],0,'Inter-record gaps'),('serpentine ในภาพหมายถึงอะไร?','เมื่อเปลี่ยน track ทิศอ่าน/เขียนกลับด้านไปมา'),('ภาพหน้า 42 ตัวอย่างอ่าน/เขียนพร้อมกันกี่ tracks?','4 tracks')],(41,42))

add('lto-example','ตาราง LTO เป็นตัวอย่างในสไลด์','extra','หน้า 43',
    'ตารางหน้า 43 เปรียบเทียบ LTO generations 1–8 ด้วย capacity และ transfer rate ของแต่ละรุ่น. ใช้ฝึกอ่านแนวโน้มภายในตารางและศัพท์ของเทปเท่านั้น. บางแถวมีค่าอนาคตหรือ TBA จากช่วงเวลาที่ทำสไลด์ จึงต้องตรวจสอบจากต้นฉบับก่อนนำไปอ้างเป็นสเปกปัจจุบัน.',
    ['LTO เป็นตาราง generations 1–8 ในเอกสาร','หัวตารางเทียบ capacity/transfer rate','ค่า TBA และแถวอนาคตไม่ใช่ข้อมูลยืนยันปัจจุบัน'],
    ['LTO','generation','native capacity','transfer rate','TBA'],
    'อ่านจากหัวแถว generation ไปยังค่าความจุและอัตราโอนของรุ่นเดียวกัน โดยระบุว่าเป็นค่าตามสไลด์',
    'อย่าคัดตัวเลขในตารางไปใช้เป็น specification ปัจจุบันโดยไม่มีแหล่งใหม่; งานนี้จำกัดเฉพาะสไลด์',
    'LTO ตารางรุ่น = ตัวอย่าง ไม่ใช่ราคาหรือสเปกวันนี้',
    [('ตารางหน้า 43 ว่าด้วยอะไร?',['LTO generations','RAID levels','CD block','SSD controller'],0,'LTO generations'),('ตาราง LTO มีวัตถุประสงค์ทบทวนอย่างไร?','เทียบรุ่นและอ่านเกณฑ์ capacity/transfer rate ตามเอกสาร'),('เหตุใดค่าที่ระบุ TBA ในตารางจึงใช้ตอบสเปกปัจจุบันไม่ได้?','สไลด์ไม่ได้ยืนยันค่าและอยู่ในบริบทเวลาเดิม; ต้องตรวจสอบจากต้นฉบับ')],(43,))


page_text = {p['page']:p['text'] for p in json.loads((HERE/'pages.json').read_text(encoding='utf-8'))}
figure_pages = list(range(4,44))
caption_override = {
    7:'ผัง track, sector, cylinder, platter, head และ gaps',
    9:'Winchester ST506: ส่วนประกอบ sector ตัวอย่าง 600 bytes',
    14:'ลำดับเวลา disk I/O: device/channel wait, seek, rotational delay, transfer',
    17:'ตาราง RAID 0–6: redundancy, จำนวนดิสก์ และ performance',
    18:'ภาพกระจายข้อมูล RAID 0, mirror RAID 1 และ Hamming RAID 2',
    19:'ภาพ parity ของ RAID 3–6 รวม P/Q ของ RAID 6',
    20:'logical-to-physical strip mapping ของ RAID 0',
    27:'ตารางเปรียบ RAID ตามสไลด์',
    28:'ตารางเปรียบ RAID และตัวอย่างงานตามสไลด์',
    30:'ตาราง SSD/HDD รุ่นตัวอย่างในช่วงเวลาของสไลด์',
    31:'แผนผัง host, SSD controller และ flash components',
    32:'ปัญหา write/erase ของ SSD และ wear leveling',
    33:'ตารางชนิด optical disk และรูปแบบ ROM/R/RW',
    36:'CD-ROM block 2352 bytes และส่วนประกอบ',
    39:'ชั้น CD-ROM เทียบ DVD-ROM แบบ double-sided, dual-layer',
    40:'ความยาวคลื่นและ pit/track ของ CD, DVD, Blu-ray',
    42:'serpentine tape tracks และตัวอย่างอ่าน/เขียน 4 tracks',
    43:'ตาราง LTO generations เป็นตัวอย่างตามสไลด์',
}

def heading(p):
    lines=[x.strip(' •\t') for x in page_text[p].splitlines() if x.strip()]
    lines=[x for x in lines if not x.startswith(('ITDS-211:','©','W.Suntiamorntut'))]
    return next((x for x in lines if len(x)>5 and not x.startswith(('■','•'))), '')

figures=[]
for p in figure_pages:
    owner=next(t for t in topics if f'fig-{p}' in t['figures'])
    title=heading(p) or owner['title']
    caption=caption_override.get(p,f'ภาพสไลด์เรื่อง {owner["title"]} สำหรับทบทวนตำแหน่งและรายละเอียด')
    figures.append(dict(id=f'fig-{p}',page=p,file=f'slide-{p:03d}.png',title=f'{title} · หน้า {p}',
                        caption=f'{caption} ({SOURCE}, หน้า {p})'))

flashcards=[dict(front=t['title'],back=t['remember'][0],pages=t['pages']) for t in topics]
term_cards=[
    ('Track / Sector / Cylinder','วงข้อมูล / ส่วนของ track / track ที่รัศมีตรงกันหลายผิว','หน้า 7'),
    ('ST506 sector','600 bytes รวม overhead; data จริง 512 bytes ในตัวอย่าง','หน้า 9'),
    ('Seek time','เวลาวางหัวที่ track ใน movable-head','หน้า 15'),
    ('Rotational delay','เวลารอ sector หมุนมาถึงหัว','หน้า 15'),
    ('Access time','seek time + rotational delay','หน้า 15'),
    ('RAID 0','striping; nonredundant','หน้า 17–18'),
    ('RAID 1','mirroring; 2N disks','หน้า 17–18, 22'),
    ('RAID 2','parallel access; Hamming code','หน้า 17, 23'),
    ('RAID 3','parallel access; one parity disk','หน้า 17, 24'),
    ('RAID 4','independent access; dedicated parity disk','หน้า 17, 25'),
    ('RAID 5','distributed parity แบบ round-robin','หน้า 17, 26'),
    ('RAID 6','dual distributed parity; N+2 disks','หน้า 17, 26'),
    ('MTTR','mean time to repair ที่สไลด์ใช้กับเงื่อนไข RAID 6','หน้า 26'),
    ('Wear leveling','กระจายจำนวน writes ข้าม flash blocks','หน้า 32'),
    ('CD-ROM block','12 sync + 4 ID + 2048 data + 288 ECC = 2352 bytes','หน้า 36'),
    ('CD-R / CD-RW','dye write once / phase-change rewritable','หน้า 38'),
    ('Optical wavelengths','CD 780 nm; DVD 650 nm; Blu-ray 405 nm','หน้า 40'),
    ('Inter-record gap','ช่องว่างระหว่าง physical records บนเทป','หน้า 41'),
    ('Serpentine','อ่าน/เขียนสลับทิศเมื่อเปลี่ยน track','หน้า 42'),
]
flashcards += [dict(front=f,back=b,pages=p) for f,b,p in term_cards]

data=dict(
    source=SOURCE,sourcePageCount=45,
    course='ITDS-211 · Computer Architecture & Operating System',
    instructor='W. Suntiamorntut, Ph.D.',
    chapter='Chapter06 · Storage Systems (External memory)',
    description='magnetic disk, RAID 0–6, SSD, optical memory และ magnetic tape',
    notice='เลขหน้าเป็นหน้า PDF 1–45; ข้อมูลรุ่น/ราคา/ความจุในตารางเป็นตัวอย่างตามสไลด์ และข้อความ RAID หน้า 16 กับ RAID 0 หน้า 17 ต้องตรวจสอบจากต้นฉบับ',
    purpose='บทนี้เรียนเพื่อเข้าใจว่าสื่อจัดเก็บภายนอกบันทึก จัดตำแหน่ง เข้าถึง และป้องกันข้อมูลอย่างไร: เริ่มจาก disk layout และเวลา I/O แล้วเทียบ RAID, SSD, optical disk กับ magnetic tape ตามกลไกและข้อจำกัดในสไลด์',
    purposePages='หน้า 3–44',
    objectiveNote='วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจาก outline หน้า 3 และ summary หน้า 44',
    flashcardNote='Flashcards ใช้ศัพท์ สูตร และโครงสร้างจากสไลด์; ตัวเลขตารางรุ่นเป็นตัวอย่างเฉพาะเอกสาร',
    goals=[
        dict(text='ระบุส่วนประกอบ magnetic disk, layout และคำนวณ access time ตามนิยามในสไลด์',pages='หน้า 4–15'),
        dict(text='แยก RAID 0–6 ตาม striping/mirror/parity, parallel/independent access และจำนวนดิสก์',pages='หน้า 16–28'),
        dict(text='อธิบาย SSD controller, flash erase/write และวิธีกระจายการสึกหรอ',pages='หน้า 29–32'),
        dict(text='เทียบชนิด optical disk/block format และลำดับบันทึกแบบ magnetic tape',pages='หน้า 33–44')],
    limits=[
        'อ่านและตรวจภาพครบ 45 หน้า: หน้า 1 ปก, หน้า 2 course outline, หน้า 3 chapter outline, หน้า 44 summary, หน้า 45 Q&A',
        'สไลด์ไม่มีรายการ Chapter Objectives โดยตรงหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; ระดับสีเป็นลำดับเวลาอ่าน ไม่ใช่สถิติการออกสอบ',
        'หน้า 16 อธิบาย RAID แบบมี redundant parity ครบทุกระดับ แต่หน้า 17–18 ระบุ RAID 0 nonredundant: ต้องตรวจสอบจากต้นฉบับ',
        'ตาราง HDD หน้า 13, SSD/HDD หน้า 30, optical หน้า 33 และ LTO หน้า 43 เป็นตัวอย่างจากช่วงเวลาของสไลด์ ไม่ใช่ข้อมูลราคา/สเปกปัจจุบัน',
        'สไลด์หน้า 23 เขียน byte/word strips ในเนื้อหาและมีหมายเหตุภาษาไทยว่า bit-level; ระดับ strip ที่แน่ชัดของ RAID 2 ในบริบทนี้: ต้องตรวจสอบจากต้นฉบับ',
        'คำถามคำนวณใช้เฉพาะสูตรและตัวเลขที่อยู่ในสไลด์; ไม่มีการอ้างว่าเป็นข้อสอบจริง'],
    figures=figures,topics=topics,
    roadmap=[
        dict(title='1 · Magnetic disk',text='เริ่มสื่อ/หัวอ่าน → track/sector/cylinder → seek/rotation/transfer',pages='หน้า 4–15',topic='magnetic-medium'),
        dict(title='2 · RAID ภาพรวม',text='จำ N, striping, redundancy และตาราง RAID 0–6 พร้อมข้อขัดกันหน้า 16–17',pages='หน้า 16–19',topic='raid-framework'),
        dict(title='3 · RAID ทีละระดับ',text='ไล่ 0/1 แล้ว 2/3 แบบ parallel ต่อด้วย 4/5/6 แบบ independent',pages='หน้า 18–28',topic='raid0'),
        dict(title='4 · SSD',text='เทียบ HDD, วาด controller→flash แล้วอธิบาย erase/write และ wear leveling',pages='หน้า 29–32',topic='ssd-contrast'),
        dict(title='5 · Optical และ tape',text='อ่าน ROM/R/RW, CD-ROM block, DVD/Blu-ray แล้วจบด้วย serial/serpentine tape',pages='หน้า 33–43',topic='optical-families')],
    plan=[
        dict(title='รอบ 1 · แผนที่สื่อและ layout',task='ดูภาพหน้า 4–13; วาด platter/track/sector/cylinder และแยกชนิดหัว',check='ระบุส่วนของ disk และอ่าน sector ST506 ได้โดยไม่สับสน data/overhead',pages='หน้า 4–13'),
        dict(title='รอบ 2 · เวลาและ RAID',task='คำนวณ access time หน้า 15 แล้วทำตาราง RAID 0–6 จากความจำก่อนเปิดหน้า 17–28',check='จำ seek+rotation, redundancy และจำนวนดิสก์แต่ละระดับได้',pages='หน้า 14–28'),
        dict(title='รอบ 3 · SSD',task='ตามภาพ controller และเขียนลำดับ read–erase–write พร้อม wear leveling',check='อธิบายปัญหา block erase และวิธีรับมือจากหน้า 32 ได้',pages='หน้า 29–32'),
        dict(title='รอบ 4 · Optical/tape',task='ทวน ROM/R/RW, คิด 2352-byte block, เทียบ laser wavelengths และตาม serpentine',check='แยก write-once/rewritable และบอก 12+4+2048+288 ได้',pages='หน้า 33–43'),
        dict(title='รอบ 5 · เว้นระยะและสุ่ม Quiz',task='ตอบ 3 ข้อต่อหัวข้อ; ทวนข้อที่ผิดจากภาพต้นฉบับในวันถัดไป',check='ตอบหัวข้อแดงครบและชี้ตารางเก่าหรือข้อขัดกันที่ต้องตรวจสอบได้',pages='หน้า 4–43')],
    cram=[
        dict(title='ถ้าเหลือ 3 วัน',text='วัน 1 disk หน้า 4–15; วัน 2 RAID หน้า 16–28; วัน 3 SSD/optical/tape หน้า 29–43 และทำ Quiz'),
        dict(title='ถ้าเหลือ 1 วัน',text='disk timing หน้า 14–15 → RAID table/levels หน้า 17–26 → SSD หน้า 31–32 → CD block/optical/tape หน้า 33–42'),
        dict(title='ถ้าเหลือ 3 ชั่วโมง',text='0–35 นาที layout/timing หน้า 7–15; 35–105 นาที RAID หน้า 16–26; 105–135 นาที SSD หน้า 29–32; 135–165 นาที optical/tape หน้า 33–42; 165–180 นาทีสุ่ม Quiz')],
    strategyIntro='เน้นหัวข้อที่สไลด์ให้นิยาม กลไก ภาพและตารางซ้ำ เช่น disk timing, RAID 0–6, SSD block write และ CD-ROM block; ไม่มีข้อสอบเก่าจึงไม่ยืนยันโอกาสออกจริง',
    strategy=[
        dict(title='ควรท่องจำ',text='track/sector/cylinder, access time, RAID 0–6 กับ N/2N/N+m/N+1/N+2, ROM/R/RW, CD-ROM block และศัพท์ tape (หน้า 7–9, 15–17, 33–42)'),
        dict(title='ควรฝึกโจทย์',text='บวก seek+rotational delay; คิด sector overhead 600−512; คิด CD block 2352−2048; นับ disk RAID และ read/write RAID 4 (หน้า 9, 15, 17, 25, 36)'),
        dict(title='ควรเข้าใจแนวคิด',text='RAID parity/mirror, เหตุ RAID 5 ลดคอขวด RAID 4, SSD erase/write/wear leveling และ optical/tape access (หน้า 16–32, 34–42)'),
        dict(title='เตรียมข้อสอบแบบผสม',text='เลือกตอบจับคู่คำศัพท์/level; อัตนัยอธิบายกลไก; คำนวณเฉพาะสูตร/ตัวเลขในสไลด์; วิเคราะห์ภาพ mapping, RAID parity, SSD controller และ tape (หน้า 7–42)')],
    flashcards=flashcards)

assert len(topics)==22 and len({t['id'] for t in topics})==22
assert all(len(t['questions'])==3 and t['pages'] and t['summary'] for t in topics)
assert set(f['id'] for f in figures)==set(fid for t in topics for fid in t['figures'])
(HERE/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('topics',len(topics),'figures',len(figures),'questions',sum(len(t['questions']) for t in topics),'flashcards',len(flashcards))
