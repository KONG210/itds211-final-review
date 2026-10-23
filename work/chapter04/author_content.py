"""Chapter04 study notes: only facts and examples visible in the supplied PDF."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = 'itds-211_comp_arch_Chapter04.pdf'
topics = []

def add(id, title, level, pages, summary, remember, terms, example, confusion,
        mnemonic, quiz, image_pages=(), comparison=None):
    assert len(quiz) == 3
    m, a, b = quiz
    questions = [dict(type='เลือกตอบ', q=m[0], options=m[1], correct=m[2], answer=m[3], pages=pages),
                 dict(type='อัตนัย', q=a[0], answer=a[1], pages=pages),
                 dict(type='คำนวณ' if any(w in b[0] for w in ('คำนวณ','จงหา','เท่าไร')) else 'วิเคราะห์',
                      q=b[0], answer=b[1], pages=pages)]
    entry = dict(id=id,title=title,level=level,pages=pages,
        reason={'core':'เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท',
                'important':'เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ',
                'extra':'เป็นรายละเอียดประกอบหรือกรณีเทคโนโลยีตัวอย่าง'}[level],
        summary=summary,remember=remember,terms=terms,example=example,
        confusion=confusion,mnemonic=mnemonic,questions=questions,
        figures=[f'fig-{p}' for p in image_pages])
    if comparison: entry['comparison']=dict(headers=comparison[0],rows=comparison[1])
    topics.append(entry)

add('locality-hierarchy','Locality และ Memory Hierarchy','core','หน้า 3–8',
    'โปรแกรมใช้เพียงส่วนเล็กของ address space ในแต่ละช่วงเวลา จึงเกิด temporal locality และ spatial locality. ลำดับชั้นหน่วยความจำอาศัยการคัดลอกข้อมูลที่ใช้ล่าสุดหรืออยู่ใกล้กันจาก disk สู่ DRAM แล้วสู่ SRAM cache; การพบข้อมูลระดับบนคือ hit มิฉะนั้นต้องย้าย block ขึ้นมาและเกิด miss penalty.',
    ['Temporal: สิ่งที่ใช้ไม่นานมักถูกใช้ซ้ำ; Spatial: สิ่งที่อยู่ใกล้กันมักถูกใช้ต่อ (หน้า 4)','Disk → main memory/DRAM → cache/SRAM ใกล้ CPU (หน้า 5–7)','Block/line เป็นหน่วยคัดลอก; hit ratio=hits/accesses; miss ratio=1−hit ratio (หน้า 8)'],
    ['temporal locality','spatial locality','block/line','hit/miss ratio','miss penalty'],
    'สไลด์ยก loop/induction variables สำหรับ temporal และ sequential instructions/array data สำหรับ spatial (หน้า 4)',
    'hit หมายถึงพบที่ระดับบน ณ การเข้าถึงครั้งนั้น; miss แล้วจึงคัดลอก block จากระดับล่าง ไม่ใช่เพิ่มข้อมูลทีละ byte เสมอ',
    'ใช้ซ้ำเร็ว = temporal; ใช้ข้างกัน = spatial; ย้ายเป็น block',
    [('สิ่งที่เพิ่งใช้มีแนวโน้มใช้ซ้ำเป็น locality แบบใด?',['Temporal','Spatial','Write-back','Fully associative'],0,'Temporal locality'),('miss ratio สัมพันธ์กับ hit ratio อย่างไร?','miss ratio = 1 − hit ratio'),('หลังเกิด miss ข้อมูลถูกนำขึ้นมาในหน่วยใด?','block หรือ line จากระดับล่างขึ้นระดับบน')],(4,5,6,7,8))

add('memory-technology','SRAM, DRAM และเทคนิคเพิ่ม bandwidth','core','หน้า 9–14',
    'สไลด์เปรียบ SRAM, DRAM และ magnetic disk ตามเวลาเข้าถึง ความจุ และต้นทุนในบริบทตัวอย่าง. DRAM เก็บประจุใน capacitor จึงต้อง refresh; การจัดแถว row, burst, DDR/QDR และ banking ช่วยการส่งข้อมูลต่อเนื่องหรือพร้อมกัน. ภาพหน้า 14 เปรียบ memory หนึ่ง word, 4-word wide และ 4-bank interleaved ด้วยจำนวน bus cycles.',
    ['ตัวเลขหน้า 9 เป็นค่าตัวอย่างในสไลด์: SRAM 0.5–2.5ns; DRAM 50–70ns; disk 5–20ms','DRAM read/refresh เป็นระดับ row; burst ส่งคำต่อเนื่อง; DDR ส่งบนขอบขึ้นและลง (หน้า 10–13)','ตัวอย่างหน้า 14: 4-word wide 17 cycles/0.94 B-cycle; 4-bank interleaved 20 cycles/0.8 B-cycle'],
    ['SRAM','DRAM','refresh','row buffer','burst','DDR/QDR','banking'],
    'หน้า 14 คำนวณ 16/17≈0.94 B/cycle และ 16/20=0.8 B/cycle ตามสมมติฐานในภาพ',
    'ห้ามนำตัวเลขเวลา/ราคา/DRAM generations หน้า 9,12 ไปอ้างเป็นข้อมูลปัจจุบัน; เป็นตัวอย่างในเอกสาร',
    'DRAM ต้อง refresh; row/burst/bank ช่วยส่งข้อมูล',
    [('DRAM ต้องทำอะไรเป็นระยะตามหน้า 10?',['Refresh','Invalidate','Page fault','Write-around'],0,'Refresh'),('DDR ต่างจากการส่งหนึ่งขอบสัญญาณอย่างไร?','ส่งข้อมูลทั้ง rising และ falling clock edges'),('ตัวอย่าง 4-word wide หน้า 14 มี bandwidth เท่าไร?','16 bytes/17 cycles≈0.94 B/cycle')],(9,10,11,12,13,14))

add('flash-storage','Flash: NOR, NAND และ wear leveling','important','หน้า 15–16',
    'Flash เป็น nonvolatile semiconductor storage ที่สไลด์เปรียบกับ disk. NOR เน้น random access และตัวอย่าง instruction memory ใน embedded system; NAND หนาแน่นกว่าและเข้าถึงเป็น block. การเขียนซ้ำทำให้เสื่อม จึงมี wear leveling กระจายการใช้งาน block.',
    ['Flash ไม่หายเมื่อปิดไฟตามคำว่า nonvolatile (หน้า 15)','NOR: random read/write; NAND: denser, block-at-a-time และใช้กับ USB/media storage (หน้า 16)','Wear leveling remap ไปยัง block ที่ถูกใช้น้อย (หน้า 16)'],
    ['nonvolatile','NOR flash','NAND flash','wear leveling'],
    'จับคู่ NOR กับ instruction memory embedded และ NAND กับ USB/media storage ตามหน้า 16',
    'ตัวเลขความเร็ว/ราคา/อายุการเขียนหน้า 15–16 เป็นบริบทของสไลด์ ไม่ใช่สเปกปัจจุบันทุกอุปกรณ์',
    'NOR อ่านสุ่ม; NAND อ่านเป็น block; สึกแล้วกระจายเขียน',
    [('Flash ประเภทใดในสไลด์หนาแน่นและเข้าถึงเป็น block?',['NAND','NOR','DRAM','SRAM'],0,'NAND'),('wear leveling ทำอะไร?','ย้าย/กระจายข้อมูลไป block ที่ใช้น้อยเพื่อลดการสึกเฉพาะจุด'),('Flash หน้า 15 ต่างจาก DRAM ด้านการคงข้อมูลอย่างไร?','Flash เป็น nonvolatile; DRAM เก็บประจุและต้อง refresh ตามหน้า 10')],(15,16))

add('disk-access','Disk sector และเวลาการเข้าถึง','core','หน้า 17–20',
    'Disk เป็น nonvolatile rotating magnetic storage; sector มีรหัสระบุ ข้อมูล ECC และส่วนช่วยซิงโครไนซ์. เวลาการเข้าถึงหนึ่ง sector รวม queue, seek, rotational latency, transfer และ controller overhead. ตัวอย่าง 15,000 rpm/512B ให้เวลาอ่านเฉลี่ยประมาณ 6.2ms โดยเวลา seek เป็นส่วนสำคัญ.',
    ['องค์ประกอบการเข้าถึง: queue, seek, rotation, transfer, controller (หน้า 18)','ตัวอย่างหน้า 19: 4ms seek +2ms rotation +0.005ms transfer +0.2ms controller ≈6.2ms','ถ้า actual average seek 1ms สไลด์ให้ average read 3.2ms (หน้า 19)'],
    ['sector','seek','rotational latency','transfer time','controller overhead','disk cache'],
    '½ revolution /(15000/60 revolutions/s)=2ms rotational latency ตามหน้า 19',
    'ค่า 6.2ms เป็นการปัดจาก 6.205ms และสมมติ disk idle; หน้า 20 ระบุ locality/OS scheduling ทำให้ seek จริงต่างจากค่าเฉลี่ยผู้ผลิต',
    'รอคิว–หา track–รอหมุน–ส่งข้อมูล–คุมอุปกรณ์',
    [('ส่วนใดคือเวลารอหัวอ่านย้ายตำแหน่ง?',['Seek','Rotation','Transfer','Refresh'],0,'Seek'),('เวลาการเข้าถึง sector ประกอบด้วยอะไรบ้าง?','queue, seek, rotational latency, transfer และ controller overhead'),('ตัวอย่างหน้า 19 เมื่อ seek เหลือ 1ms ได้ read time ประมาณเท่าไร?','3.2ms ตามสไลด์')],(17,18,19,20))

add('cache-basics','Cache lookup, direct mapping, tag และ valid','core','หน้า 21–24',
    'Cache เป็นระดับใน memory hierarchy ที่ใกล้ CPU; ต้องตอบว่าข้อมูลอยู่ใน cache หรือไม่และควรหา entry ไหน. Direct-mapped cache ให้แต่ละ memory block มีตำแหน่งเดียว โดย index = block address mod จำนวน cache blocks. Tag แยก block ที่ชน index และ valid bit ระบุว่าช่องนั้นมีข้อมูลจริงหรือไม่.',
    ['Direct mapped: index = block address modulo #cache blocks (หน้า 23)','ถ้า #blocks เป็นกำลังสอง ใช้บิตล่างเป็น index; tag เป็นบิตสูงของ block address (หน้า 23–24)','valid=1 แปลมีข้อมูล, 0 แปลไม่มี; ค่าเริ่มต้น 0 (หน้า 24)'],
    ['direct mapped','index','tag','valid bit'],
    'cache 8 blocks ใช้ 3 index bits; หน้า 25 แสดงทุก entry เริ่ม valid=N',
    'index ตรงกันยังไม่พอเป็น hit ต้อง valid และ tag ตรงกัน',
    'Index ชี้ช่อง; Tag เช็กตัวตน; Valid เช็กว่ามี',
    [('direct-mapped block address หา index อย่างไร?',['mod #cache blocks','บวก tag','หาร hit ratio','คูณ miss penalty'],0,'block address mod จำนวน cache blocks'),('valid bit ช่วยตอบอะไร?','ช่อง cache มีข้อมูลที่ใช้ได้หรือยัง'),('เหตุใด index ตรงแต่ tag ต่างจึงเป็น miss?','ช่องเดียวกันอาจเก็บคนละ memory block จึงต้องเทียบ tag')],(21,22,23,24))

add('direct-cache-trace','ไล่สถานะ 8-block direct-mapped cache','important','หน้า 25–30',
    'ตัวอย่าง cache 8 blocks, 1 word/block เริ่มทุก valid bit เป็น N แล้วเข้าถึง word addresses หลายตัว. Word 22 ลง index 110/tag 10 และ word 26 ลง index 010/tag 11; การเข้าซ้ำเป็น hit จน word 18 มาใช้ index 010 เดียวกับ 26 และแทนที่ด้วย tag 10.',
    ['22→binary 10 110→index110 miss ครั้งแรก; 26→11 010→index010 miss (หน้า 26–27)','22 และ 26 เข้าซ้ำเป็น hit ตามสถานะหลังโหลด (หน้า 28)','16→index000 miss; 3→index011 miss; 16 เข้าซ้ำ hit; 18→index010 miss/แทน 26 (หน้า 29–30)'],
    ['cache trace','hit/miss','tag/index collision'],
    'ตามตารางหน้า 25–30 ทีละ access แล้วปรับ valid/tag/data เฉพาะช่องที่ miss',
    'หน้า 29 มีลำดับตัวอย่างย่อย 16,3,16; อย่าสับสนกับ access 22/26 ในหน้าก่อนและอย่าอ่านสีตารางแทนลำดับเวลา',
    'แปลง address → index/tag → เทียบ → อัปเดตเฉพาะ miss',
    [('word 22 ใช้ index ใดในตัวอย่าง?',['110','010','000','011'],0,'110'),('เพราะเหตุใด word 18 เป็น miss ที่ index 010?','index เดียวกับ 26 แต่ tag 10 ต่างจาก tag 11 ที่เก็บอยู่'),('access 16 ครั้งที่สองในหน้า 29 เป็น hit หรือ miss?','Hit เพราะ entry 000 valid และ tag 10 ยังตรง')],(25,26,27,28,29,30))

add('address-subdivision','Tag–Index–Offset และการคำนวณ block','core','หน้า 31–32',
    'ที่อยู่ byte แบ่งเป็น tag, index และ offset เพื่อหา cache entry และตำแหน่งภายใน block. ตัวอย่าง 64 blocks ขนาด 16 bytes/block ให้ block address=floor(1200/16)=75 แล้ว cache block=75 mod64=11; offset 4 บิตและ index 6 บิต.',
    ['block address=floor(byte address/bytes per block) (หน้า 32)','cache block number=block address mod #blocks (หน้า 32)','64 blocks→6 index bits; 16 bytes/block→4 offset bits (หน้า 32)'],
    ['tag','index','byte offset','block address','modulo'],
    '1200/16=75 และ 75 mod64=11 ตามตัวอย่างหน้า 32',
    'รูปหน้า 32 เขียนช่วง bit address ถึง 63 แต่ระบุ tag 22+index6+offset4=32 บิต ขัดกัน: ต้องตรวจสอบจากต้นฉบับ; อย่าเดาความกว้าง address จากรูปนี้',
    'หารขนาด block ก่อน; mod จำนวนช่องต่อ',
    [('16 bytes/block ต้องใช้ offset กี่บิต?',['4','6','10','22'],0,'4 บิต'),('สูตรหา block address จาก byte address คืออะไร?','floor(address/bytes per block)'),('address 1200 ใน cache 64 blocks, 16B/block ไป block ไหน?','floor(1200/16)=75; 75 mod64=11')],(31,32))

add('block-size-misses','ขนาด block กับการจัดการ cache miss','core','หน้า 33–34',
    'block ใหญ่ใช้ spatial locality เพื่อลด miss บางส่วน แต่ cache ขนาดคงที่มีจำนวน block น้อยลง จึงเพิ่ม competition/pollution และ miss penalty. เมื่อ cache miss CPU อาจ stall แล้วดึง block จากระดับล่าง; instruction miss กลับไป fetch ส่วน data miss ทำ data access ต่อ.',
    ['larger block อาจลด miss จาก spatial locality แต่เพิ่ม miss penalty (หน้า 33)','cache ขนาดคงที่: block ใหญ่→จำนวน entry น้อย→competition/pollution (หน้า 33)','on miss: stall pipeline, fetch block; instruction/data miss กลับขั้นต่างกัน (หน้า 34)'],
    ['block size','pollution','miss penalty','early restart','critical-word-first'],
    'หน้า 33 ระบุ early restart/critical-word-first ว่าช่วยลดผลของ miss penalty',
    'อย่าจำว่า block ใหญ่ยิ่งดีเสมอ; มีทั้งประโยชน์จาก locality และค่าเสียโอกาสของ entry',
    'Block ใหญ่ช่วยใกล้เคียง แต่กินช่องและโหลดนาน',
    [('block ใหญ่ใน cache ขนาดคงที่ทำให้จำนวน entry อย่างไร?',['ลดลง','เพิ่มขึ้น','ไม่เปลี่ยน','เป็นศูนย์'],0,'ลดลง'),('CPU ทำอะไรเมื่อ cache miss ตามหน้า 34?','stall pipeline แล้วดึง block จากระดับถัดไป'),('เหตุใด block ใหญ่อาจเพิ่ม miss rate?','มี entry น้อยลง เกิด competition/pollution มากขึ้น')],(33,34))

add('cache-writes','Write-through, write-back และ write miss','core','หน้า 35–37',
    'Write-through เขียนทั้ง cache และ memory ทุก write hit จึงอาจใช้ write buffer ลดการรอ. Write-back เขียน cache ก่อน ติด dirty bit แล้วค่อยเขียน block กลับเมื่อถูกแทนที่. เมื่อ write miss สไลด์เทียบ write allocate (fetch block) กับ write-around (ไม่ fetch) และระบุ write-back มัก fetch block.',
    ['Write-through อัปเดต cache+memory; ตัวอย่าง base CPI1, stores10%, write100 cycles→CPI11 (หน้า 35)','Write buffer ให้ CPU เดินต่อได้จน buffer เต็ม (หน้า 35)','Write-back ใช้ dirty bit; write miss แบบ allocate ดึง block, write-around ไม่ดึง (หน้า 36–37)'],
    ['write-through','write-back','dirty bit','write buffer','write allocate','write-around'],
    'เปรียบหน้า 35–36: เขียน memory ทุกครั้งกับเขียนเมื่อแทน dirty block',
    'Write policy สำหรับ hit กับ write allocation สำหรับ miss เป็นคนละการตัดสินใจ',
    'Through เขียนล่างทันที; Back เขียนล่างตอนแทน; Miss เลือกดึงหรือข้าม',
    [('นโยบายใดต้องติด dirty bit?',['Write-back','Write-through','Write-around','Direct mapped'],0,'Write-back'),('write-around หมายถึงอะไรในหน้า 37?','write miss แล้วไม่ fetch block เข้าค cache'),('ตัวอย่างหน้า 35 effective CPI เท่าไร?','1+0.1×100=11')],(35,36,37),(['เรื่อง','Write-through','Write-back'],[['เขียนเมื่อ hit','cache และ memory','cache ก่อน'],['การเขียนระดับล่าง','ทุก write hit','เมื่อ dirty block ถูกแทน'],['สิ่งช่วย/สถานะ','write buffer','dirty bit']]))

add('cache-organization-example','Split cache และ main memory ที่รองรับ cache','important','หน้า 38–40',
    'กรณี Intrinsity FastMATH ในสไลด์ใช้ split I-cache/D-cache และแสดง miss rate ต่างกัน; เป็นตัวอย่างสถาปัตยกรรมเฉพาะ. หน้า 40 แสดงว่าความกว้าง memory/bus ส่งผลต่อ miss penalty และ bandwidth โดยตัวอย่าง 4-word block ผ่าน memory กว้างหนึ่ง word ใช้ 65 bus cycles.',
    ['ตัวอย่าง FastMATH: I-cache/D-cache อย่างละ 16KB, 256 blocks×16 words/block; miss rate 0.4%/11.4% (หน้า 38)','หน้า 40: address1 + DRAM 4×15 + transfer4×1 =65 bus cycles','bandwidth=16 bytes/65 cycles≈0.25 B/cycle (หน้า 40)'],
    ['split cache','I-cache/D-cache','bus width','miss penalty','bandwidth'],
    'ใช้ภาพหน้า 39 ดู tag/index/offset ของ split cache และคำนวณหน้า 40',
    'ตัวเลข miss rate และขนาด cache หน้า 38 เป็นของเครื่องตัวอย่าง ไม่ใช่ค่า RISC-V ทั่วไป',
    'กว้างบัส/หน่วยความจำกำหนดเวลาขนหนึ่ง block',
    [('I-cache กับ D-cache ในตัวอย่างหน้า 38 แยกกันหรือรวมกัน?',['แยกกัน','รวมกัน','ไม่ใช้ cache','เป็น disk'],0,'แยกกัน'),('miss penalty หน้า 40 ของ 4-word block ผ่าน 1-word DRAM เท่าไร?','65 bus cycles'),('bandwidth ตัวอย่างหน้า 40 ได้เท่าไร?','16/65≈0.25 B/cycle')],(38,39,40))

add('cache-performance','Memory stall CPI และ AMAT','core','หน้า 41–44',
    'สไลด์แยก CPU cycles สำหรับการรันโปรแกรมออกจาก memory stall cycles ที่มักเกิดจาก cache miss. ภายใต้สมมติฐานที่ระบุ miss cycles คำนวณจากจำนวน access หรือ miss ต่อ instruction คูณ miss penalty; AMAT รวม hit time กับ miss rate×miss penalty. ตัวอย่างแสดง actual CPI 5.44 และ AMAT 2ns.',
    ['memory stall cycles≈memory accesses/program×miss rate×miss penalty (หน้า 41)','I-cache:0.02×100=2; D-cache:0.36×0.04×100=1.44; actual CPI=2+2+1.44=5.44 (หน้า 42)','AMAT=hit time+miss rate×miss penalty; ตัวอย่าง 1+0.05×20=2ns (หน้า 43)'],
    ['CPI','memory stall cycles','AMAT','hit time','miss rate','miss penalty'],
    'ตัวอย่างหน้า 42 ideal CPI 2 เทียบ actual 5.44 ให้สัดส่วน 5.44/2=2.72 ตามสไลด์',
    'miss rate ของ I-cache ต่อ instruction ต่างจาก D-cache ที่ต้องคูณสัดส่วน load/store 0.36; หน้า 44 ย้ำดู cache behavior เมื่อประเมิน performance',
    'CPI ฐานบวก stall; AMAT hit บวกโอกาส miss คูณ penalty',
    [('สูตร AMAT คือข้อใด?',['Hit time + miss rate×miss penalty','Hit time×miss rate','CPI+clock rate','Tag+index+offset'],0,'Hit time + miss rate×miss penalty'),('ทำไม D-cache หน้า 42 ต้องคูณ 0.36?','มี load/store 36% ของ instructions จึงไม่ใช่ทุกคำสั่งที่เข้าถึง D-cache'),('จงหา actual CPI ตัวอย่างหน้า 42','2+0.02×100+0.36×0.04×100=5.44')],(41,42,43,44))

add('associativity','Direct, n-way และ fully associative','core','หน้า 45–47',
    'Fully associative วาง block ใน entry ใดก็ได้แต่ต้องเทียบทุก entry; n-way set associative กำหนด set จาก block number mod จำนวน sets แล้วค้นหา n entries ใน set. ภาพหน้า 46–47 แสดงสองแบบนี้เทียบกับ direct mapped ซึ่งมีเพียงตำแหน่งเดียว.',
    ['Fully associative: วางได้ทุก entry ต้องค้นพร้อมกันทุก entry (หน้า 45)','n-way: set=block number mod #sets; ค้น n entries ใน set (หน้า 45)','direct mapped เป็น 1-way; spectrum หน้า 47 ใช้ cache 8 entries'],
    ['fully associative','n-way set associative','set index','comparator'],
    'อ่านภาพหน้า 46 โดยตาม block เดียวไปได้หนึ่งช่อง/หนึ่ง set/ทุกช่องตามสามรูปแบบ',
    'associativity เพิ่มทางเลือกตำแหน่งแต่เพิ่ม comparator/ความซับซ้อน ไม่ใช่เพิ่มจำนวน entries ของ cache ในตัวอย่างเทียบ',
    'หนึ่งช่อง–หลายช่องใน set–ทุกช่อง',
    [('แบบใดวาง block ได้ทุก entry?',['Fully associative','Direct mapped','Write-through','Page table'],0,'Fully associative'),('n-way set associative หา set อย่างไร?','block number mod จำนวน sets'),('ทำไม fully associative มี hardware cost สูง?','ต้องค้น/เปรียบเทียบหลาย entry พร้อมกัน')],(45,46,47),(['Mapping','ที่วาง block','จำนวนเปรียบเทียบตามหน้า 89'],[['Direct mapped','หนึ่ง entry','1'],['n-way','หนึ่งใน n entries ของ set','n'],['Fully associative','ทุก entry','จำนวน entries']]))

add('associativity-trace','ตัวอย่าง access 0, 8, 0, 6, 8','important','หน้า 48–50',
    'สไลด์เทียบ cache ขนาด 4 blocks ที่รับลำดับ 0,8,0,6,8. Direct mapped ชน index จน miss ทุกครั้ง; 2-way set associative ได้ hit ที่ 0 ครั้งที่สอง; fully associative ได้ hit ที่ 0 และ 8 ที่กลับมา. ข้อมูล simulation หน้า 50 แสดง miss rate ลดลงเมื่อ associativity สูงขึ้นแต่ผลเพิ่มเริ่มน้อยลง.',
    ['Direct mapped: 5 misses ใน 5 accesses (หน้า 48)','2-way: miss,miss,hit,miss,miss; fully: miss,miss,hit,miss,hit (หน้า 49)','SPEC2000 example หน้า 50: 1/2/4/8-way miss 10.3/8.6/8.3/8.1%'],
    ['conflict miss','set','associativity','diminishing returns'],
    'ไล่ตารางหน้า 48–49 ทีละ access; 0 กับ 8 ใช้ index 0 ใน direct mapped',
    'ตัวเลขหน้า 50 เป็นผล simulation กรณี 64KB D-cache ไม่ใช่กฎว่าทุก cache มี miss rate ตามนี้',
    'เพิ่มทางเลือกที่วาง ลดการชน แต่ผลเพิ่มลดลง',
    [('ลำดับ 0,8,0,6,8 แบบ fully associative มี hit กี่ครั้ง?',['2','0','1','5'],0,'2 ครั้ง: ที่ 0 ครั้งที่สอง และ 8 ครั้งสุดท้าย'),('direct mapped ในตัวอย่างมีเหตุใด miss ทุกครั้ง?','0 และ 8 ชน index เดียวกันและแทนกัน; access อื่นก็ไม่ทำให้มี hit ในลำดับนี้'),('2-way set associative ในหน้า 49 มี hit ที่ access ไหน?','access 0 ครั้งที่สอง')],(48,49,50))

add('replacement','Replacement policy: LRU และ Random','core','หน้า 51–52',
    'เมื่อ miss แล้วต้องแทน entry, direct mapped ไม่มีตัวเลือก ส่วน set associative ควรใช้ entry invalid ก่อน. หากเต็มแล้วจึงเลือกตามนโยบาย เช่น LRU เลือก entry ที่ไม่ถูกใช้นานที่สุด หรือ random. สไลด์ระบุ LRU ซับซ้อนขึ้นเมื่อ associativity สูง.',
    ['direct mapped ไม่มี choice ในการแทน (หน้า 52)','set associative ใช้ non-valid entry ก่อน; เต็มแล้วจึงเลือกใน set (หน้า 52)','LRU เลือก entry ไม่ใช้ยาวนานสุด; random ใกล้ LRU ใน high associativity ตามสไลด์ (หน้า 52)'],
    ['replacement policy','LRU','random','valid entry'],
    'ดูภาพการจัด set หน้า 51 แล้วถามว่าถ้ามีช่อง invalid จะต้องแทนของเดิมหรือไม่',
    'LRU หมายถึงเวลาตั้งแต่ใช้งานครั้งล่าสุด ไม่ใช่ข้อมูลที่เก่าที่สุดตามเวลานำเข้าครั้งแรก',
    'ว่างก่อน; เต็มแล้วค่อยเลือก LRU หรือสุ่ม',
    [('LRU แทน entry ใด?',['ที่ไม่ถูกใช้นานที่สุด','ที่เพิ่งใช้ล่าสุด','tag ต่ำสุด','entry แรกเสมอ'],0,'ไม่ถูกใช้นานที่สุด'),('direct mapped มีนโยบายเลือก entry แทนหรือไม่?','ไม่มี choice เพราะแต่ละ block มีที่เดียว'),('ถ้ามี invalid entry ใน set ควรทำอย่างไรตามหน้า 52?','ใช้ entry นั้นก่อนแทนข้อมูลที่ valid')],(51,52))

add('multilevel-cache','L1/L2 และตัวอย่าง CPI หลายระดับ','core','หน้า 53–56',
    'L1 อยู่ใกล้ CPU จึงเน้น hit time ต่ำ ส่วน L2 ใหญ่กว่าและรับ miss จาก L1 เพื่อลดการไป main memory. ตัวอย่าง 4GHz/base CPI1 มี L1 อย่างเดียว CPI9; เมื่อมี L2 สไลด์คำนวณ CPI3.4 และ performance ratio 9/3.4≈2.6. หน้าตัวอย่างมีคำบรรยาย penalty หนึ่งจุดไม่ตรงกับสมการ จึงต้องอ่านคู่กัน.',
    ['L1 เล็ก/เร็ว; L2 ใหญ่/ช้ากว่า L1 แต่เร็วกว่า main memory (หน้า 53,56)','4GHz→cycle 0.25ns; 100ns main memory→400 cycles; L1 only CPI=1+0.02×400=9 (หน้า 54)','L2 access 5ns→20 cycles; global miss 0.5%; สมการหน้า 55 ให้ CPI=1+0.02×20+0.005×400=3.4'],
    ['L1/L2 cache','global miss rate','miss penalty','effective CPI'],
    'ฝึกคำนวณแยก penalty ที่ L2 กับ main memory จากตัวอย่างหน้า 54–55',
    'หน้า 55 เขียน “Extra penalty = 500 cycles” แต่สมการใช้ 400 cycles และ 100ns/0.25ns ในหน้า 54 เท่ากับ 400: ต้องตรวจสอบจากต้นฉบับ',
    'L1 เน้น hit เร็ว; L2 กัน miss ลง DRAM',
    [('L1 มักเน้นสิ่งใด?',['hit time ต่ำ','จุใหญ่ที่สุด','disk latency','ECC'],0,'hit time ต่ำ'),('CPI เมื่อมีเพียง primary cache ในตัวอย่างเท่าไร?','1+0.02×400=9'),('สมการ CPI เมื่อเพิ่ม L2 หน้า 55 ให้ผลเท่าไร?','1+0.02×20+0.005×400=3.4; แต่คำบรรยาย extra penalty ต้องตรวจต้นฉบับ')],(53,54,55,56))

add('software-blocking','Advanced CPU, locality ของ software และ blocking','important','หน้า 57–62',
    'out-of-order CPU อาจทำงานอิสระต่อได้ขณะ cache miss จึงวิเคราะห์เวลาได้ยากและสไลด์เสนอ simulation. รูปแบบการเข้าถึง memory ขึ้นกับ algorithm/compiler; ตัวอย่าง DGEMM ใช้ blocking เพื่อใช้ข้อมูลซ้ำก่อนถูกแทนใน cache และภาพหน้า 60–62 เปรียบ access pattern.',
    ['out-of-order: dependent instructions รอ, independent instructions อาจเดินต่อ (หน้า 57)','miss rate ขึ้นกับ memory access pattern/algorithm/compiler (หน้า 58)','blocking เป้าหมายคือใช้ข้อมูลให้มากก่อนถูกแทน; ตัวอย่างใช้ BLOCKSIZE=32 (หน้า 59–62)'],
    ['out-of-order','memory access pattern','DGEMM','blocking','BLOCKSIZE'],
    'ตามภาพ C/A/B หน้า 60 กับ blocked access pattern หน้า 62 เพื่อเห็นการใช้ข้อมูลซ้ำในบริเวณย่อย',
    'อย่าอ้างว่า cache miss ทุกครั้ง stall CPU เต็ม penalty เมื่อเป็น out-of-order; หน้า 57 ระบุ independent work ยังทำได้',
    'จัดงานเป็น block ใช้ข้อมูลซ้ำก่อนหลุด cache',
    [('blocking ใน DGEMM มีเป้าหมายอะไร?',['ใช้ข้อมูลซ้ำก่อนถูกแทน','ปิด cache','เพิ่ม stride','ลบ DRAM'],0,'ใช้ข้อมูลซ้ำก่อนถูกแทน'),('out-of-order CPU ทำอะไรระหว่าง miss ได้?','คำสั่งอิสระบางส่วนยังเดินต่อ ส่วน dependent รอ'),('BLOCKSIZE ในโค้ดตัวอย่างหน้า 61 เป็นเท่าไร?','32 ตามสไลด์')],(57,58,59,60,61,62))

add('dependability','Dependability: MTTF, MTTR, MTBF, Availability','core','หน้า 63–64',
    'สไลด์แยก fault ของ component ออกจาก failure ของ service; fault อาจนำหรือไม่ไปสู่ system failure. ความเชื่อถือได้วัดด้วย MTTF และเวลาซ่อมด้วย MTTR; MTBF=MTTF+MTTR และ availability=MTTF/(MTTF+MTTR). เพิ่ม availability ได้โดยเพิ่ม MTTF หรือ ลด MTTR.',
    ['fault เป็น failure ของ component แต่อาจไม่ทำให้บริการล้ม (หน้า 63)','MTBF=MTTF+MTTR; Availability=MTTF/(MTTF+MTTR) (หน้า 64)','เพิ่ม MTTF ผ่าน avoidance/tolerance/forecasting; ลด MTTR ด้วย diagnosis/repair ที่ดีขึ้น (หน้า 64)'],
    ['fault','failure','restoration','MTTF','MTTR','MTBF','availability'],
    'ไล่ภาพหน้า 63 จาก service delivered → interruption → restoration กลับ service',
    'MTBF รวมเวลาทำงานก่อนเสียกับเวลาซ่อม; อย่าใช้แทน MTTF ในสูตร availability โดยไม่แปลง',
    'เวลาทำงานเทียบงานบวกเวลาซ่อม คือ availability',
    [('สูตร Availability ในสไลด์คืออะไร?',['MTTF/(MTTF+MTTR)','MTTR/MTTF','MTTF×MTTR','MTBF−MTTR'],0,'MTTF/(MTTF+MTTR)'),('MTBF สัมพันธ์กับ MTTF/MTTR อย่างไร?','MTBF=MTTF+MTTR'),('fault ทุกครั้งเป็น system failure หรือไม่?','ไม่; หน้า 63 ระบุ fault อาจนำหรือไม่สู่ system failure')],(63,64))

add('ecc-hamming','Hamming SEC และ SEC/DEC','core','หน้า 65–68',
    'Hamming distance คือจำนวนตำแหน่งบิตที่ต่างกัน; minimum distance 2 ตรวจข้อผิดพลาดหนึ่งบิต และ 3 แก้หนึ่งบิตพร้อมตรวจสองบิตตามสไลด์. การเข้ารหัส SEC วาง parity bits ที่ตำแหน่งกำลังสองเมื่อเลขตำแหน่งเริ่ม 1 จากซ้าย. เพิ่ม parity ทั้ง word ให้ SEC/DEC มี distance 4 และใช้ parity syndrome ช่วยแยกกรณี error.',
    ['Hamming distance 2 ตรวจ 1-bit; distance 3 แก้ 1-bit/ตรวจ 2-bit (หน้า 65)','SEC parity positions 1,2,4,8; ตารางหน้า 66 บอก data bits ที่แต่ละตัวตรวจ','syndrome 0000→no error; 1010→bit 10 flipped (หน้า 67)','เพิ่ม whole-word parity p_n เป็น SEC/DEC distance4; สไลด์ยก ECC DRAM 8 bits ต่อ 64 bits (หน้า 68)'],
    ['Hamming distance','SEC','SEC/DEC','parity bit','syndrome','ECC DRAM'],
    'ดูตารางหน้า 66 แล้วอ่าน syndrome 1010 ว่าเลขตำแหน่ง 10 ตามตัวอย่างหน้า 67',
    'หน้า 68 ใช้ถ้อยคำ H even/odd ร่วมกับ p_n even/odd; ต้องตรวจสอบจากต้นฉบับหากจะนำไปคำนวณชุด parity โดยละเอียด เพราะสไลด์ไม่ได้ให้ตัวอย่างข้อมูลครบ',
    'พาริตีอยู่ 1,2,4,8; syndrome ชี้ตำแหน่ง; เพิ่ม parity ทั้ง word ตรวจสองบิต',
    [('minimum distance 3 ทำอะไรได้ตามสไลด์?',['แก้ 1-bit และตรวจ 2-bit','แก้ 2-bit','ตรวจ 3-bit เท่านั้น','ไม่ตรวจได้'],0,'แก้ 1-bit และตรวจ 2-bit'),('parity bit ของ SEC วางที่ตำแหน่งใด?','ตำแหน่งเลขกำลังสองเมื่อเริ่มนับ 1 จากซ้าย เช่น 1,2,4,8'),('syndrome 1010 ในหน้า 67 หมายถึงอะไร?','บิตตำแหน่ง 10 พลิก')],(65,66,67,68))

add('virtual-machines','Virtual Machines, VMM และ privileged support','core','หน้า 69–72',
    'Virtual machine ให้ host จำลอง guest OS และทรัพยากรเพื่อแยกผู้ใช้หลายกลุ่มและแชร์เครื่อง. VMM map virtual resources ไป physical resources; guest code ทำงาน user mode และ trap ไป VMM เมื่อใช้ privileged instruction หรือ protected resource. ตัวอย่าง timer virtualization แสดง VMM รับ interrupt จริงและจำลองให้ VM.',
    ['VM ช่วย isolation และ resource sharing แต่มี performance impact (หน้า 69)','VMM map memory/I-O/CPU; privileged access trap ไป VMM (หน้า 70)','หน้า 71 เปรียบ OS จัด process กับ VMM จัด VM บน timer interrupt','หน้า 72 system/user modes และ privileged instructions คุ้มครอง physical resources'],
    ['VM','host/guest','VMM','trap','privileged instruction','timer virtualization'],
    'อ่านหน้า 71 เปรียบเส้นทาง timer ของ native machine กับ VMM',
    'guest OS ไม่ได้เข้าถึงอุปกรณ์จริงได้อิสระ; VMM จัดการ real I/O และ emulates virtual I/O ตามหน้า 70',
    'Guest เห็นเครื่องเสมือน; VMM จับสิทธิ์และ map ของจริง',
    [('ใคร map virtual resource ไป physical resource?',['VMM','guest application','cache tag','disk sector'],0,'VMM'),('guest code ในตัวอย่างรัน mode ใด?','user mode และ trap เมื่อเจอ privileged access'),('timer interrupt ใต้ VMM จัดหน่วยใดต่อ?','VMM เลือก/สลับ VM และจำลอง timer ให้ VM ที่ต้องการ')],(69,70,71,72))

add('virtual-memory','Virtual Memory, address translation และ page fault','core','หน้า 73–75',
    'Virtual memory ใช้ main memory เป็น cache ของ disk โดย CPU hardware กับ OS ร่วมกันจัดการ. โปรแกรมมี virtual address space ของตน และ address translation แปลง virtual page number เป็น physical page number โดย page offset คงเดิม. ถ้า page ไม่อยู่ใน memory เกิด page fault ซึ่งมี penalty สูงและ OS ต้องนำ page จาก disk.',
    ['VM block เรียก page; translation miss เรียก page fault (หน้า 73)','ตัวอย่าง fixed-size 4K page มี offset 12 bits ตามภาพหน้า 74','page fault ดึง page จาก disk ใช้หลายล้าน cycles; OS handle (หน้า 75)'],
    ['virtual address','physical address','page','page offset','page fault'],
    'ตามลูกศรภาพหน้า 74: แปล page number แต่ส่ง offset เดิมไปต่อ physical address',
    'page fault เป็น page ไม่อยู่ main memory; ไม่ใช่ TLB miss ทุกครั้ง (แยกในหน้า 82–84)',
    'เปลี่ยนเลข page; offset คง; ไม่พบจึงไป disk',
    [('หน่วย block ของ virtual memory เรียกว่าอะไร?',['Page','Sector','Tag','Word'],0,'Page'),('page fault เกิดเมื่อใด?','page ที่ต้องการไม่อยู่ใน main memory ต้องดึงจาก disk'),('offset ของ 4K page ในภาพหน้า 74 กี่บิต?','12 บิต')],(73,74,75))

add('page-table','Page table, PTE และ replacement/write-back','core','หน้า 76–79',
    'Page table มี PTE ตาม virtual page number; ถ้า present จะให้ physical page number กับ status bits หากไม่อยู่ memory อาจชี้ swap space. Reference/use bit ช่วยประมาณ LRU และ dirty bit ระบุ page ที่ถูกเขียน. Disk write ช้ามากจึงใช้ write-back เมื่อจำเป็นต้องแทน page.',
    ['Page table register ชี้ page table ใน physical memory; PTE indexed by virtual page number (หน้า 76)','PTE เก็บ physical page number/status หรือที่อยู่ swap space (หน้า 76–78)','reference bit set เมื่อ access และ OS ล้างเป็นระยะ; dirty bit set เมื่อเขียน page (หน้า 79)','page ที่ dirty ต้องเขียน disk เมื่อถูกแทน; write-through ไม่เหมาะกับ disk (หน้า 79)'],
    ['PTE','page table register','swap space','reference bit','dirty bit','write-back'],
    'ภาพหน้า 77–78 ชี้ว่า page ใน virtual space บางหน้า map ไป physical memory และบางหน้าไป disk',
    'valid/present bit กับ dirty/reference มีหน้าที่ต่างกัน; reference=0 เพียงบอกว่าไม่น่าใช้ล่าสุดตามการล้างรอบก่อน',
    'PTE บอกที่; reference บอกใช้; dirty บอกต้องเขียนกลับ',
    [('bit ใดบอก page ถูกเขียน?',['Dirty bit','Reference bit','Tag bit','Offset'],0,'Dirty bit'),('PTE เก็บอะไรเมื่อ page อยู่ใน physical memory?','physical page number และ status bits'),('เหตุใด virtual memory ใช้ write-back?','การเขียน disk ช้ามาก จึงเขียนเป็น page/block เมื่อจำเป็น')],(76,77,78,79))

add('tlb','TLB lookup, miss handler และ page fault handler','core','หน้า 80–84',
    'TLB เป็น cache ของ PTE ใน CPU เพื่อไม่ต้องเข้าถึง page table ใน memory ทุกครั้ง. TLB miss อาจเกิดทั้งเมื่อ page อยู่ memory หรือไม่อยู่; กรณีแรกเติม PTE แล้ว retry ส่วนกรณีหลังเป็น page fault ให้ OS นำ page จาก disk อัปเดต page table และ restart instruction. ภาพหน้า 81 แสดง TLB, page table, physical memory และ disk ร่วมกัน.',
    ['TLB=Translation Look-aside Buffer; cache PTE ใน CPU (หน้า 80)','page present แต่ไม่ใน TLB→โหลด PTE จาก memory/retry (หน้า 82–83)','page absent→OS locate disk, choose replacement, write dirty page, read page, update table, restart (หน้า 82–84)'],
    ['TLB','PTE','TLB hit/miss','page fault handler','restart instruction'],
    'อ่านแผนภาพหน้า 81 แล้วตามสองทาง: TLB miss แต่ PTE valid กับ PTE invalid/page fault',
    'TLB miss ไม่เท่ากับ page fault เสมอ; คำว่า “page not preset” หน้า 83 ดูเป็น typo ของ present แต่ใช้บริบทหน้า 82 ประกอบ',
    'TLB ไม่มีรายการ ≠ page ไม่มีใน RAM; ตรวจ PTE ก่อน',
    [('TLB เก็บอะไรเป็นหลัก?',['PTE','sector data','ECC syndrome','CPU instruction text ทั้งหมด'],0,'PTE'),('ถ้า page อยู่ RAM แต่ TLB miss จะทำอย่างไร?','นำ PTE จาก page table มาเติม TLB แล้ว retry instruction'),('ถ้า page ไม่อยู่ RAM ใครจัดการและทำอะไร?','OS page fault handler ดึงจาก disk อัปเดต page table แล้ว restart')],(80,81,82,83,84))

add('tlb-cache-protection','TLB/Cache interaction และ Memory Protection','important','หน้า 85–86',
    'ถ้า cache ใช้ physical address เป็น tag ต้องแปล virtual address ก่อน lookup; การใช้ virtual tag มีปัญหา aliasing เมื่อหลาย virtual address ชี้ physical address เดียวกัน. Hardware กับ OS ยังต้องป้องกัน address space ผ่าน supervisor mode, privileged instructions และ page tables ที่เข้าถึงได้เฉพาะสิทธิ์สูง.',
    ['physical tag→translate ก่อน cache lookup (หน้า 85)','virtual tag มี aliasing เมื่อ virtual addresses ต่างกันแชร์ physical address (หน้า 85)','supervisor/kernel mode และ privileged instructions ป้องกัน page table/resource; ecall เป็นตัวอย่าง system call (หน้า 86)'],
    ['physical/virtual tag','aliasing','supervisor mode','privileged instruction','ecall'],
    'ภาพหน้า 85 เทียบลำดับ TLB→cache กับทางเลือก virtual-address tag',
    'อย่าสับสน address translation เพื่อหาตำแหน่งจริงกับ memory protection เพื่อจำกัดสิทธิ์เข้าถึง',
    'แปลก่อนหาเมื่อ tag จริง; kernel คุมสิทธิ์',
    [('physical-address cache tag ต้องทำอะไรก่อน lookup?',['translate address','write disk','invalidate ทุก block','เพิ่ม CPI'],0,'translate address'),('aliasing ในหน้า 85 เกิดจากอะไร?','virtual addresses ต่างกันอ้าง physical address ร่วมกัน'),('หน้า 86 ระบุโหมดที่เข้าถึง page table/state ที่มีสิทธิ์สูงคืออะไร?','supervisor/kernel mode')],(85,86))

add('memory-framework','กรอบร่วมของ Memory Hierarchy','core','หน้า 87–91',
    'ทุกระดับของ memory hierarchy มีคำถามร่วมกันสี่เรื่อง: วาง block ที่ไหน, หา block อย่างไร, miss แล้วแทนตัวใด และเขียนข้อมูลลงระดับล่างเมื่อใด. ระดับ associativity กำหนดทางเลือกในการวางและจำนวน tag comparison; write-through กับ write-back มีต้นทุนและสถานะที่ต้องเก็บต่างกัน.',
    ['Placement: direct 1 ที่, n-way n ที่ใน set, fully ที่ใดก็ได้ (หน้า 88)','Finding: direct เปรียบเทียบ tag 1, n-way n, fully ตามจำนวน entries; full lookup table เป็นอีกวิธี (หน้า 89)','Replacement: LRU หรือ random; virtual memory ใช้ LRU approximation (หน้า 90)','Write-through อัปเดตบน/ล่าง; write-back อัปเดตล่างเมื่อถูกแทน; virtual memory ใช้ write-back เพราะ disk latency (หน้า 91)'],
    ['block placement','tag comparison','replacement','LRU','write-through','write-back'],
    'ตารางหน้า 89 แสดง index → 1 comparison; set index → n comparisons; search all entries → #entries comparisons',
    'associativity สูงลด miss แต่เพิ่มความซับซ้อน ต้นทุน และ access time; ไม่ได้ดีขึ้นทุกมิติ',
    'วาง–หา–แทน–เขียน',
    [('direct mapped มีทางเลือกวาง block กี่ตำแหน่ง?',['1','n','#entries','ไม่จำกัด'],0,'1'),('ทำไม virtual memory ใช้ write-back?','disk write latency สูงตามสไลด์'),('n-way set associative ต้องเปรียบเทียบ tag กี่รายการใน set?','n รายการ')],(87,88,89,90,91),
    (['แบบ','ตำแหน่งวาง','การเปรียบเทียบ tag'],[['Direct mapped','1','1'],['n-way set associative','n ภายใน set','n'],['Fully associative','ที่ใดก็ได้','#entries']]))

add('miss-taxonomy','Compulsory, Capacity, Conflict miss และ trade-offs','core','หน้า 92–93',
    'Compulsory miss เกิดเมื่อเข้าถึง block ครั้งแรก; capacity miss เกิดเพราะ cache จำกัดจน block เดิมถูกแทนและต้องใช้ซ้ำ; conflict miss เกิดจากหลาย block แย่งตำแหน่งใน set ของ cache ที่ไม่ fully associative. การเพิ่มขนาด cache, associativity และ block size ลด miss ต่างชนิดกัน แต่มีต้นทุนเรื่อง access time, miss penalty หรือ pollution.',
    ['Compulsory = first access (หน้า 92)','Capacity = finite size ทำให้ block ที่ถูกแทนถูกเรียกอีก (หน้า 92)','Conflict = แข่ง entry ใน set; ไม่เกิดใน fully associative ขนาดรวมเท่ากัน (หน้า 92)','เพิ่ม cache size ลด capacity; เพิ่ม associativity ลด conflict; เพิ่ม block size ลด compulsory แต่ใหญ่มากอาจเพิ่ม miss/pollution (หน้า 93)'],
    ['compulsory/cold start','capacity','conflict/collision','pollution','miss penalty'],
    'ตารางหน้า 93 จับคู่ design change กับชนิด miss ที่ลดและผลเสียด้านเวลา',
    'อย่าจับคู่เพิ่ม associativity กับ capacity miss; ผลโดยตรงในตารางคือ conflict miss',
    'ครั้งแรก–ที่ไม่พอ–ที่ชนกัน',
    [('first access เป็น miss ประเภทใด?',['compulsory','capacity','conflict','coherence'],0,'compulsory'),('เพิ่ม associativity ลด miss ใดตามตาราง?','conflict miss'),('เหตุใดเพิ่ม block size มากเกินไปอาจเสียผล?','miss penalty เพิ่ม และ pollution อาจทำให้ miss rate สูงขึ้น')],(92,93),
    (['Miss','สาเหตุ','แนวลดตามสไลด์'],[['Compulsory','เรียก block ครั้งแรก','เพิ่ม block size'],['Capacity','cache รวมไม่พอ','เพิ่ม cache size'],['Conflict','block ชนกันใน set','เพิ่ม associativity']]))

add('cache-fsm','Cache Controller ด้วย Finite State Machine','core','หน้า 94–97',
    'ตัวอย่าง cache เป็น direct-mapped, write-back, write allocate, blocking cache ขนาด 16 KB มี 1024 blocks ขนาด block 16 bytes และ address 32 บิต. Controller ใช้ FSM คุมขั้นตอนตาม clock โดยเก็บ current state ใน register, หา next state จาก current state กับ input และสร้าง control output จาก current state. ภาพ FSM แสดงทางเดิน hit, miss, dirty write-back และ memory read.',
    ['ตัวอย่าง: 32-bit byte address; tag 18, index 10, offset 4 (หน้า 94)','valid/dirty bit ต่อ block; CPU รอ access ให้เสร็จใน blocking cache (หน้า 94)','interface CPU–cache–memory มี read/write, valid, address, data, ready และการเข้าถึง memory หลาย cycles (หน้า 95)','next state = fn(current state,current inputs); outputs = fo(current state) (หน้า 96)'],
    ['FSM','current state','next state','valid bit','dirty bit','blocking cache'],
    '16 KB/16 B = 1024 blocks จึงใช้ index 10 บิต; offset 4 บิต; tag 32−10−4=18 บิต (หน้า 94)',
    'write-back miss ที่ victim dirty ต้องเขียน block เดิมกลับก่อนโหลด block ใหม่; อ่านรายละเอียดลูกศรหน้า 97',
    'สถานะปัจจุบัน + input → สถานะถัดไป',
    [('ตัวอย่าง cache หน้า 94 เป็นนโยบายใด?',['write-back/write allocate','write-through/write around','fully associative','non-blocking'],0,'write-back/write allocate'),('เหตุใด index 10 บิต?','1024 blocks = 2^10 ตำแหน่ง'),('FSM คำนวณ next state จากอะไร?','current state และ current inputs')],(94,95,96,97))

add('cache-coherence','Cache Coherence และ invalidating snooping','core','หน้า 98–101',
    'เมื่อหลาย core แชร์ physical address แต่เก็บสำเนาไว้ใน cache ของตน การเขียนของ core หนึ่งอาจทำให้สำเนาอีก core เก่า. Coherence ต้องให้การอ่านเห็นค่าที่เขียนล่าสุดตามเงื่อนไขในสไลด์ และทุก processor เห็นลำดับการเขียนไปยัง X เหมือนกัน. Snooping เฝ้าดู bus ส่วน directory-based เก็บสถานะผู้แชร์; invalidating snooping ส่ง invalidate เมื่อขอสิทธิ์เขียนแบบ exclusive.',
    ['ตัวอย่าง CPU A/B อ่าน X=0 แล้ว A เขียน 1: cache B อาจยังมี 0 (หน้า 98)','coherence ครอบคลุม read-after-own-write, read-after-other-write เมื่อเวลาพอ และลำดับ write ต่อ X เหมือนกัน (หน้า 99)','snooping monitor bus; directory บันทึก sharing status (หน้า 100)','invalidate → read ของ cache อื่น miss แล้ว owner ส่งค่าล่าสุด (หน้า 101)'],
    ['cache coherence','snooping','directory-based','invalidate','exclusive access'],
    'ไล่ตารางหน้า 101: A/B อ่าน X=0, A เขียน X=1 และ invalidate, B อ่านซ้ำแล้ว miss ก่อนรับค่าใหม่',
    'write-through ให้ memory ใหม่ได้ แต่ไม่ได้ทำให้สำเนาใน cache อื่นใหม่เอง; ต้องมี coherence protocol',
    'เขียนร่วม → แจ้งลบสำเนาเก่า',
    [('snooping protocol ตรวจอะไร?',['bus reads/writes','disk sectors','register file','page offset'],0,'bus reads/writes'),('directory-based protocol เก็บอะไร?','sharing status ของ blocks ใน cache/memory'),('หลัง A invalidate X แล้ว B อ่าน X จะเกิดอะไร?','B cache miss แล้วได้ค่าที่อัปเดตจาก owner ตามตัวอย่าง')],(98,99,100,101))

add('memory-consistency','Memory Consistency และลำดับการมองเห็น writes','core','หน้า 102',
    'Memory consistency ถามว่า write ของ processor หนึ่งจะถูก processor อื่นมองเห็นเมื่อใด โดย “เห็น” หมายถึง read คืนค่าที่เขียน. ภายใต้สมมติฐานของสไลด์ write เสร็จเมื่อทุก processor เห็นแล้ว และ processor ไม่สลับลำดับ write กับ access อื่น. จึงถ้า P เขียน X แล้ว Y ทุก processor ที่เห็นค่าใหม่ของ Y จะเห็นค่าใหม่ของ X ด้วย.',
    ['“seen” = read คืน written value (หน้า 102)','write completes เมื่อทุก processor เห็นตาม assumptions ของสไลด์ (หน้า 102)','P เขียน X ก่อน Y → เห็น Y ใหม่แล้วต้องเห็น X ใหม่ (หน้า 102)'],
    ['memory consistency','write visibility','write ordering'],
    'ใช้สถานการณ์ X ก่อน Y หน้า 102 ตรวจว่า observation ของอีก processor สอดคล้องสมมติฐานหรือไม่',
    'coherence หน้า 99 เน้นค่าและลำดับการเขียนของ X เดียว; consistency หน้า 102 ถามการมองเห็น write ของ X และ Y',
    'เห็น Y ใหม่ ต้องเห็น X ใหม่',
    [('คำว่า seen หมายถึงอะไร?',['read คืนค่าที่เขียน','write เริ่มต้น','cache miss','disk เสร็จ'],0,'read คืนค่าที่เขียน'),('สไลด์กำหนดว่า write complete เมื่อใด?','เมื่อทุก processor เห็น write นั้น'),('P เขียน X แล้ว Y; ถ้าอีก core เห็น Y ใหม่ ต้องเห็นอะไร?','X ใหม่ด้วย ภายใต้สมมติฐานหน้า 102')],(102,))

add('real-systems','ARM/Intel cache, 2-level TLB และ system instructions','important','หน้า 103–107',
    'สไลด์ยก ARM Cortex-A53 และ Intel Core i7 เพื่อดู multilevel on-chip caches กับ 2-level TLB organization จากภาพ. ทั้งสองมี multi-banked cache เพื่อรองรับหลาย access ต่อ cycle เมื่อไม่ชน bank และมีแนวทาง requested-word-first, non-blocking cache, hit/miss under miss และ data prefetching. ตาราง RISC-V แสดงกลุ่ม fence, CSR access และ system instructions; DGEMM ผสาน cache blocking กับ subword parallelism.',
    ['ภาพ hierarchy ARM/Intel (หน้า 103) และ TLB สองระดับ (หน้า 104) ต้องดูตัวเลขจากภาพต้นฉบับ','multi-banked รองรับ multiple issue เมื่อไม่มี bank conflict (หน้า 105)','fence.i/fence/sfence.vm; CSR read/write/set/clear; ecall/ebreak/sret/wfi (หน้า 106)','DGEMM รวม cache blocking และ subword parallelism (หน้า 107)'],
    ['multi-banked cache','non-blocking cache','prefetching','fence','CSR','DGEMM'],
    'ภาพหน้า 103–104 เปรียบการจัด L1/L2 และ TLB; หน้า 107 แสดงแนว blocking ของ matrix multiply',
    'อย่าตีความว่า multi-bank รับหลายคำขอได้เสมอ: สไลด์กำกับเงื่อนไข no bank conflicts',
    'หลาย bank ต้องไม่ชน; DGEMM บล็อกข้อมูล',
    [('multi-banked cache ช่วย multiple access ภายใต้เงื่อนไขใด?',['ไม่มี bank conflicts','cache fully associative','ไม่มี TLB','disk idle'],0,'ไม่มี bank conflicts'),('หน้า 106 จัด ecall อยู่ในกลุ่มใด?','System'),('DGEMM หน้า 107 รวมเทคนิคใด?','cache blocking กับ subword parallelism')],(103,104,105,106,107))

add('pitfalls-conclusion','Pitfalls และข้อสรุป Memory Hierarchy','important','หน้า 108–111',
    'การสับสน byte กับ word address เปลี่ยนตำแหน่ง mapping ใน cache; stride ใหญ่จากการวนแถว/คอลัมน์ผิดแบบทำให้ locality แย่. ใน multiprocessor ต้องคำนึง associativity ของ shared L2/L3; AMAT อย่างเดียวไม่สะท้อน out-of-order ที่มี non-blocked accesses. บทสรุปย้ำว่าลำดับชั้นและ caching อาศัย locality เพื่อให้ภาพเหมือน memory ทั้งเร็วและใหญ่.',
    ['32-byte cache, 4-byte blocks: byte 36 → block 1; word 36 → block 4 (หน้า 108)','large stride ลด locality (หน้า 108)','shared cache associativity น้อยกว่า core count อาจเกิด conflict misses (หน้า 109)','AMAT ไม่รวมผล non-blocked accesses ของ out-of-order; สไลด์แนะนำ simulation (หน้า 109)','segmentation และ VMM บน ISA ที่ไม่เอื้อต่อ virtualization เป็น pitfalls อีกสองข้อ (หน้า 110)'],
    ['byte/word address','stride','AMAT','non-blocked access','segmentation','VMM'],
    'byte 36: floor(36/4)=9, 9 mod 8=1; word 36: 36 mod 8=4 ตาม cache 8 blocks หน้า 108',
    'อย่าใช้ AMAT ตัวเดียวตัดสิน out-of-order CPU; และอย่าสลับหน่วย byte/word ก่อนคำนวณ block index',
    'หน่วยก่อน index; locality ก่อนความเร็ว',
    [('byte 36 ในตัวอย่างหน้า 108 map ไป cache block ใด?',['1','4','9','36'],0,'1'),('ทำไม AMAT ไม่พอสำหรับ out-of-order processors?','ไม่รวมผลของ non-blocked accesses ตามหน้า 109'),('หลักการใดทำให้ caching ช่วยประสาน memory เร็วเล็กกับช้าใหญ่?','principle of locality ตามหน้า 111')],(108,109,110,111))

page_text = {p['page']: p['text'] for p in json.loads((HERE/'pages.json').read_text(encoding='utf-8'))}
figure_pages = sorted({int(fid[4:]) for t in topics for fid in t['figures']})
caption_override = {
    19:'แผนภาพเวลา disk access และตัวอย่าง 15,000 rpm ที่สไลด์ประมาณ 6.2 ms',
    29:'ตารางไล่ direct-mapped cache จากลำดับการเข้าถึงในตัวอย่าง 8 blocks',
    30:'ตารางสรุป hit/miss และ block ที่ถูกแทนในตัวอย่าง direct-mapped',
    32:'ภาพแบ่ง Tag–Index–Offset ของ address; เลข bit สูงสุดกับผลรวมช่องไม่ตรงกัน: ต้องตรวจสอบจากต้นฉบับ',
    41:'ตัวอย่าง memory stall cycles และ CPI จาก instruction mix',
    42:'ตัวอย่าง CPI เปรียบการลด miss rate และ miss penalty',
    43:'สูตร Average Memory Access Time (AMAT) และตัวอย่าง',
    48:'ตาราง direct-mapped cache สำหรับลำดับ 0,8,0,6,8',
    49:'ตารางเทียบ 2-way กับ fully associative สำหรับลำดับเดียวกัน',
    55:'ตัวอย่าง L1/L2: ข้อความ extra penalty 500 cycles ไม่ตรงกับสมการที่ใช้ 400 cycles: ต้องตรวจสอบจากต้นฉบับ',
    65:'แผนภาพ Hamming code เพิ่ม parity bits เพื่อแก้ single-bit error',
    68:'ตาราง syndrome และ parity สำหรับ SEC/DEC; ไม่มีตัวอย่างครบทุกบิตในหน้านี้',
    74:'ภาพแปล virtual address เป็น physical address โดยคง page offset',
    77:'แผนภาพ Virtual Page Number, page table และ Physical Page Number',
    81:'ลำดับ TLB hit/miss กับ page table และ page fault',
    94:'ตัวอย่าง cache 16 KB, block 16 B, address 32 บิต และ field tag/index/offset',
    97:'แผนภาพสถานะ FSM ของ cache controller',
    98:'ตารางสอง CPU core แสดงสำเนา X ใน cache ที่อาจไม่ตรงกัน',
    101:'ตาราง invalidating snooping หลัง CPU A เขียน X แล้ว CPU B อ่านซ้ำ',
    103:'ภาพลำดับ cache ของ ARM Cortex-A53 และ Intel Core i7',
    104:'ภาพการจัด TLB สองระดับของระบบตัวอย่าง',
    107:'ภาพ DGEMM ที่รวม cache blocking กับ subword parallelism',
    108:'ตัวอย่าง byte 36 กับ word 36 map ไป cache block ต่างกัน',
}

def page_heading(page):
    lines = [x.strip(' •\t') for x in page_text[page].splitlines() if x.strip()]
    lines = [x for x in lines if not x.startswith(('ITDS-211:', 'W.Suntiamorntut', 'Chapter 5 —', '§', '©'))]
    return next((x for x in lines if len(x) > 4 and not x.startswith(('','','•'))), '')

figures = []
for p in figure_pages:
    owner = next(t for t in topics if f'fig-{p}' in t['figures'])
    heading = page_heading(p) or owner['title']
    desc = caption_override.get(p, f'สไลด์แสดง {heading} สำหรับหัวข้อ {owner["title"]}')
    figures.append(dict(id=f'fig-{p}',page=p,file=f'slide-{p:03d}.png',
        title=f'{heading} · หน้า {p}',caption=f'{desc} ({SOURCE}, หน้า {p})'))

flashcards = [dict(front=t['title'],back=t['remember'][0],pages=t['pages']) for t in topics]
term_cards = [
    ('Temporal locality','มีแนวโน้มใช้ข้อมูลเดิมอีกในเวลาใกล้กัน','หน้า 4'),
    ('Spatial locality','มีแนวโน้มใช้ address ที่อยู่ใกล้ข้อมูลที่เพิ่งใช้','หน้า 4'),
    ('Hit / Miss','พบ block ที่ระดับบน / ไม่พบและต้องไประดับล่าง','หน้า 7–8'),
    ('Miss penalty','เวลาที่ต้องใช้ดึง block จากระดับล่างหลัง miss','หน้า 8'),
    ('SRAM / DRAM','SRAM เร็วและแพงกว่า; DRAM ใช้เป็น main memory ใน hierarchy','หน้า 9–12'),
    ('Direct mapped','แต่ละ memory block มีตำแหน่ง cache ได้หนึ่งตำแหน่ง','หน้า 22–24'),
    ('Tag / Index / Offset','ตรวจ identity ของ block / เลือก entry-set / เลือกตำแหน่งภายใน block','หน้า 31–32'),
    ('Write-through','เขียน cache และระดับล่าง','หน้า 35, 91'),
    ('Write-back','เขียน cache ก่อน แล้วระดับล่างเมื่อ block ถูกแทน','หน้า 35, 91'),
    ('Write allocate','เมื่อ write miss ดึง block เข้า cache ก่อนเขียน','หน้า 36–37'),
    ('AMAT','Hit time + Miss rate × Miss penalty','หน้า 43'),
    ('n-way set associative','block วางได้ n ตำแหน่งใน set ของตน','หน้า 45–47, 88'),
    ('LRU','เลือกแทน entry ที่ไม่ถูกใช้นานที่สุด','หน้า 52, 90'),
    ('MTBF','MTTF + MTTR ตามสไลด์','หน้า 63–64'),
    ('Availability','MTTF / (MTTF + MTTR)','หน้า 64'),
    ('SEC / SEC-DED','แก้ 1-bit error / แก้ 1-bit และตรวจ 2-bit error','หน้า 65–68'),
    ('Virtual Machine Monitor','ชั้นที่จัดการและแยก VM จาก physical resources','หน้า 69–72'),
    ('Page fault','virtual page ที่ต้องการไม่อยู่ใน physical memory','หน้า 74–75, 82–84'),
    ('PTE','page table entry ที่ใช้แปล page และเก็บสถานะที่เกี่ยวข้อง','หน้า 76–79'),
    ('TLB','cache ของ page table entries เพื่อเร่ง translation','หน้า 80'),
    ('Compulsory / Capacity / Conflict','ครั้งแรก / cache รวมไม่พอ / block ชน set','หน้า 92'),
    ('Cache coherence','ทำให้ core ต่าง ๆ เห็นค่าของ shared location ตามกติกา coherence','หน้า 98–101'),
    ('Memory consistency','กติกาเวลาที่ write ถูก processor อื่นมองเห็น','หน้า 102'),
    ('FSM','current state และ input กำหนด next state ของ controller','หน้า 96–97'),
]
flashcards += [dict(front=f,back=b,pages=p) for f,b,p in term_cards]

data = dict(
 source=SOURCE,sourcePageCount=112,
 course='ITDS-211 · Computer Architecture & Operating System',
 instructor='W. Suntiamorntut, Ph.D.',
 chapter='Chapter04 · Memory System Organization, Hierarchy, Cache Memory',
 description='จาก locality สู่ memory hierarchy, cache performance, dependability, virtual memory และ multicore coherence',
 notice='เลขหน้าคือหน้า PDF 1–112; หน้า 32 และ 55 มีตัวเลขในสไลด์ที่ไม่สอดคล้องกัน จึงระบุให้ตรวจต้นฉบับในหัวข้อที่เกี่ยวข้อง',
 purpose='บทนี้เรียนเพื่อเข้าใจว่าระบบให้ภาพเสมือนหน่วยความจำที่ทั้งเร็วและใหญ่ได้อย่างไร: อาศัย locality และ cache หลายระดับ พร้อมดูต้นทุนของ miss, การป้องกัน/แก้ข้อผิดพลาด, virtual memory และความสอดคล้องของ cache เมื่อมีหลาย core',
 purposePages='หน้า 3–8, 41–44, 63–86, 98–102, 111',
 objectiveNote='รายการวัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สังเคราะห์จาก Chapter Overview หน้า 3 และหัวข้อในสไลด์',
 flashcardNote='บัตรทบทวนยึดศัพท์ นิยาม สูตร และหลักการที่ปรากฏในสไลด์; เมื่อเจอหน้าที่ตัวเลขขัดกันให้เปิดภาพและใช้ป้าย “ต้องตรวจสอบจากต้นฉบับ”',
 goals=[
   dict(text='อธิบาย locality, memory technology และการส่ง block ผ่าน memory hierarchy',pages='หน้า 3–20'),
   dict(text='อ่าน cache mapping, associativity, write policy และคำนวณ hit/miss, CPI, AMAT จากตัวอย่าง',pages='หน้า 21–56'),
   dict(text='เชื่อม software locality, dependability/ECC, VM, page table และ TLB กับผลต่อประสิทธิภาพ',pages='หน้า 57–86'),
   dict(text='ใช้กรอบ placement/finding/replacement/write เพื่อวิเคราะห์ cache controller, coherence, consistency และ pitfalls',pages='หน้า 87–111')],
 limits=[
   'ตรวจครบ 112 หน้า: หน้า 1 ปก, 2 Course Outline, 3 Chapter Overview, 112 Q&A; เนื้อหาวิชาอยู่หน้า 4–111',
   'ไม่มีข้อสอบเก่าหรือน้ำหนักคะแนนในไฟล์ จึงจัดระดับจากหลักการ สูตร ขั้นตอน และตัวอย่างที่สไลด์ให้ ไม่อ้างว่าเป็นข้อสอบจริง',
   'ไม่มีรายการ Chapter Objectives ที่ประกาศเป็นข้อชัดเจน: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 32 ภาพ address มีเลขบิตสูงสุดที่ชวนเข้าใจเป็น 64 บิต แต่ Tag 22 + Index 6 + Offset 4 รวม 32 บิต: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 55 ข้อความ extra penalty = 500 cycles ไม่ตรงกับการแปลง 100 ns / 0.25 ns และสมการที่ใช้ 400 cycles: ต้องตรวจสอบจากต้นฉบับ',
   'ราคาหน่วยความจำและตัวอย่างระบบในสไลด์เป็นตัวอย่างตามเอกสาร ไม่ใช่ข้อมูลตลาดหรือสเปกปัจจุบัน',
   'ตารางและแผนภาพที่มีข้อความหนาแน่นเก็บเป็นภาพขยายในแกลเลอรี เพื่ออ่านคู่กับสรุปที่ย่อแล้ว'],
 figures=figures,topics=topics,
 roadmap=[
   dict(title='1 · หลัก locality และเทคโนโลยี',text='เริ่ม temporal/spatial locality, memory hierarchy, SRAM/DRAM, flash และ disk',pages='หน้า 3–20',topic='locality-hierarchy'),
   dict(title='2 · Cache พื้นฐานและ mapping',text='อ่าน block/tag/valid แล้วไล่ direct-mapped trace และ address fields',pages='หน้า 21–34',topic='cache-basics'),
   dict(title='3 · Write, performance และ associativity',text='แยก write policy ก่อนคำนวณ CPI/AMAT และเทียบ direct/n-way/fully',pages='หน้า 35–56',topic='cache-writes'),
   dict(title='4 · Software และความน่าเชื่อถือ',text='ต่อ locality ของโค้ด/blocked matrix แล้วทบทวน MTTF/Availability และ ECC',pages='หน้า 57–68',topic='software-blocking'),
   dict(title='5 · Virtualization และ address translation',text='ตาม VM/VMM → virtual memory/page table → TLB/page fault/protection',pages='หน้า 69–86',topic='virtual-machines'),
   dict(title='6 · กรอบออกแบบและ controller',text='สรุป placement/finding/replacement/write, ประเภท miss และ FSM',pages='หน้า 87–97',topic='memory-framework'),
   dict(title='7 · Multiprocessor และข้อควรระวัง',text='ปิดด้วย coherence/consistency ระบบตัวอย่าง และ pitfalls',pages='หน้า 98–111',topic='cache-coherence')],
 plan=[
   dict(title='รอบ 1 · วางแผนภาพรวม',task='อ่านหน้า 3 และสรุป locality → hierarchy → cache → VM → multicore ด้วยภาษาตัวเอง',check='อธิบายว่าทำไม cache ช่วยให้เหมือนมีหน่วยความจำใหญ่และเร็วได้',pages='หน้า 3–8, 111'),
   dict(title='รอบ 2 · ฝึก cache ทีละขั้น',task='ไล่ block/tag/index/offset, direct trace, write policy, associativity และ CPI/AMAT พร้อมเปิดภาพขยาย',check='ทำ trace หน้า 25–30 และ 48–49 รวมตัวอย่างหน้า 41–43 ได้',pages='หน้า 21–56'),
   dict(title='รอบ 3 · ระบบที่พึ่ง cache',task='ทบทวน software blocking, dependability/ECC, VM/page table/TLB และ protection',check='แยก TLB miss กับ page fault และคำนวณ availability ได้',pages='หน้า 57–86'),
   dict(title='รอบ 4 · วิเคราะห์ระบบหลาย core',task='ใช้สี่คำถามของ hierarchy วิเคราะห์ miss/FSM/coherence/consistency และ pitfalls',check='อธิบายเหตุผลของ invalidate และผลของ stride/byte-vs-word ได้',pages='หน้า 87–111'),
   dict(title='รอบ 5 · ทดสอบเว้นระยะ',task='ทำคำถาม 3 ข้อต่อหัวข้อ สุ่ม quiz แล้วกลับไปอ่านเฉพาะข้อผิดในวันถัดไปตามเวลาที่มี',check='ตอบครบทุกหัวข้อและชี้จุดหน้า 32/55 ที่ต้องตรวจต้นฉบับได้',pages='หน้า 3–111')],
 cram=[
   dict(title='ถ้าเหลือ 3 วัน',text='วัน 1 locality + cache mapping/write/trace หน้า 3–40; วัน 2 CPI/AMAT/associativity/ECC/VM/TLB หน้า 41–86; วัน 3 miss/FSM/coherence/pitfalls หน้า 87–111 และทำคำถาม'),
   dict(title='ถ้าเหลือ 1 วัน',text='เริ่ม cache mapping/trace/write หน้า 21–37 → CPI/AMAT/associativity หน้า 41–56 → VM/TLB หน้า 73–86 → miss/coherence หน้า 92–102 → สุ่มข้อผิด'),
   dict(title='ถ้าเหลือ 3 ชั่วโมง',text='0–45 นาที locality/cache mapping/write หน้า 4–37; 45–95 นาที CPI/AMAT/associativity หน้า 41–56; 95–140 นาที ECC/VM/TLB หน้า 63–86; 140–165 นาที miss/coherence หน้า 92–102; 165–180 นาที quiz และจุดหน้า 32/55')],
 strategyIntro='ลำดับความสำคัญเพื่อทบทวนตั้งจากนิยาม สูตร กลไก และตัวอย่างที่สไลด์เน้นต่อเนื่อง; ไม่สามารถยืนยันความถี่ออกสอบจากไฟล์เดียว',
 strategy=[
   dict(title='ควรท่องจำ',text='locality, hit/miss, tag/index/offset, write policies, AMAT/CPI, associativity, MTTF/MTTR/MTBF/Availability, SEC/DEC, TLB และประเภท miss (หน้า 4–8, 21–56, 63–68, 73–93)'),
   dict(title='ควรฝึกโจทย์',text='disk access 15k rpm, direct-map trace, address subdivision, CPI/AMAT, associative trace, L1/L2, availability และ byte/word mapping (หน้า 19, 25–32, 41–55, 64, 108)'),
   dict(title='ควรเข้าใจแนวคิด',text='software blocking, VM/page fault, protection, FSM, coherence/consistency, bank conflicts และ pitfalls (หน้า 57–62, 69–86, 94–111)'),
   dict(title='เตรียมข้อสอบแบบผสม',text='เลือกตอบศัพท์/แยก miss; อัตนัยอธิบายลำดับขั้น cache/VM/coherence; คำนวณ CPI/AMAT/mapping; วิเคราะห์ trace, diagram และจุดไม่สอดคล้องในต้นฉบับ')],
 flashcards=flashcards)

assert len(topics)==30 and len({t['id'] for t in topics})==30
assert all(len(t['questions'])==3 and t['pages'] for t in topics)
assert set(f['id'] for f in figures)==set(fid for t in topics for fid in t['figures'])
(HERE/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('topics',len(topics),'figures',len(figures),'questions',sum(len(t['questions']) for t in topics),'flashcards',len(flashcards))
