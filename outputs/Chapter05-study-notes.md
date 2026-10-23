# Chapter05 · I/O Systems

ITDS-211 · Computer Architecture & Operating System · W. Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter05.pdf** จำนวน 52 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter05 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/วิเคราะห์ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 23 หัวข้อ · 🔴 ต้องจำแน่นอน 11 หัวข้อ (47.8%) · 🟡 สำคัญ 6 หัวข้อ (26.1%) · ⚪ อ่านเสริม 6 หัวข้อ (26.1%) · แบบฝึก 69 ข้อ · Flashcard 46 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter05 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| I/O module และ external device | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 3–5 |
| หน้าที่และโครงสร้างภายใน I/O module | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 6–7 |
| Programmed I/O, Interrupt-driven I/O และ DMA | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 8–9 |
| คำสั่ง Control, Test, Read, Write | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 10 |
| ผังการรับ block ของข้อมูลด้วยสามเทคนิค | 🟡 สำคัญ | itds-211_comp_arch_Chapter05.pdf, หน้า 11 |
| I/O instructions, Memory-mapped และ Isolated I/O | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 12–14 |
| Interrupt-driven I/O และการเก็บ/คืนสถานะ | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 15–17 |
| ปัญหา priority และวิธีระบุ device ที่ interrupt | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 18–19 |
| 82C59A interrupt controller แบบ master/slave | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter05.pdf, หน้า 20 |
| Intel 8255A/82C55A และ control word | 🟡 สำคัญ | itds-211_comp_arch_Chapter05.pdf, หน้า 21–23 |
| ข้อจำกัดของ I/O ผ่าน CPU และเหตุผลใช้ DMA | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 24 |
| DMA block diagram และ breakpoint ใน instruction cycle | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 25–26 |
| Alternative DMA configurations และ Intel 8237A | 🟡 สำคัญ | itds-211_comp_arch_Chapter05.pdf, หน้า 27–30 |
| Direct Cache Access (DCA) และภาพ Xeon | 🟡 สำคัญ | itds-211_comp_arch_Chapter05.pdf, หน้า 31–32 |
| Packet traffic, buffers และ cache-related performance | 🟡 สำคัญ | itds-211_comp_arch_Chapter05.pdf, หน้า 33–35 |
| DCA prefetch, cache injection และ DDIO | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 36–37 |
| วิวัฒนาการ I/O function และ I/O channel | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter05.pdf, หน้า 38–39 |
| USB generations และ host-controller tree | 🟡 สำคัญ | itds-211_comp_arch_Chapter05.pdf, หน้า 41 |
| FireWire และ SCSI ในชุดตัวอย่าง | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter05.pdf, หน้า 42–43 |
| Thunderbolt และ InfiniBand | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter05.pdf, หน้า 44–45 |
| PCI Express และ SATA | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter05.pdf, หน้า 46 |
| Ethernet และ Wi-Fi ในชุดตัวอย่าง | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter05.pdf, หน้า 47–48 |
| ตัวอย่าง IBM EC12 I/O channel subsystem | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter05.pdf, หน้า 49–51 |

### บทนี้เรียนเพื่ออะไร

บทนี้เรียนเพื่อเข้าใจว่า processor, I/O module, อุปกรณ์ภายนอก, memory และ cache ประสานการรับส่งข้อมูลอย่างไร โดยเทียบเวลารอและทางเดินข้อมูลของ programmed, interrupt-driven, DMA และ DCA/DDIO แล้วมองการขยายระบบด้วย I/O channels และตัวอย่าง interfaces

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 2–3, 6–9, 24–39, 41–51

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- ระบุองค์ประกอบ external device และ I/O module พร้อมหน้าที่ของแต่ละส่วน (itds-211_comp_arch_Chapter05.pdf, หน้า 3–7)
- เปรียบเทียบ programmed, interrupt-driven และ DMA ทั้งเวลารอและทางเดินข้อมูล รวม I/O addressing/commands (itds-211_comp_arch_Chapter05.pdf, หน้า 8–14, 24–30)
- ไล่ interrupt, ระบุ requester/priority และอธิบายผลของ cache ต่อ network I/O พร้อม DCA/DDIO (itds-211_comp_arch_Chapter05.pdf, หน้า 15–23, 31–37)
- อ่าน I/O channels และแยกบทบาท interfaces/IBM channel ที่เป็นตัวอย่างในสไลด์ (itds-211_comp_arch_Chapter05.pdf, หน้า 38–39, 41–51)

วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจากหัวข้อและแผนภาพในสไลด์

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- อ่านและตรวจภาพครบ 52 หน้า: หน้า 1 ปก, หน้า 2 Course Outline, หน้า 52 Q&A; เนื้อหาหลักหน้า 3–39 และตัวอย่างหน้า 41–51
- หน้า 40 เป็น Assignment ให้รายงานกลุ่ม 9 เรื่อง และหน้า 41–48 เป็นหัวข้อรายงาน; ไม่มีหลักฐานว่าส่วนนี้มีน้ำหนักข้อสอบเท่าใด
- ไม่มี Chapter Objectives แบบรายการชัดเจนหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; การจัดระดับเป็นการจัดเวลาอ่าน
- หน้า 21–22 ใช้ชื่อ Intel 8255A แต่ภาพหน้า 23 ใช้ 82C55A; อ่านชื่อรุ่นตามหน้าต้นฉบับ
- หน้า 30 ตาราง Intel 8237A status แถว D4–D7 พิมพ์ Channel 0 request ซ้ำ: ต้องตรวจสอบจากต้นฉบับ
- หน้า 46 คำอธิบาย SATA วาง 6 Gbps กับ 300 Mbps ต่อ device โดยไม่แจกเงื่อนไข: ต้องตรวจสอบจากต้นฉบับก่อนใช้คำนวณ
- หน้า 49 ภาพ IBM EC12 เขียน ≤60 และ ≤1024 partitions/system คนละตำแหน่ง: ต้องตรวจสอบจากต้นฉบับ
- อัตราและคำว่า current ในหน้า 31, 41–48 เป็นคำในสไลด์ ไม่ใช่ข้อมูลสเปกหรือสถานะเทคโนโลยีปัจจุบัน
- Chapter05 ไม่มีตัวอย่างโจทย์คำนวณแยกเป็นข้อในสไลด์ จึงเน้นคำถามเลือกตอบ อัตนัย และวิเคราะห์ภาพ/ทางเดินข้อมูล

## 2. สรุปรายบทและหัวข้อ

### 1. I/O module และ external device

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 3–5**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

I/O module เชื่อม system bus กับ peripheral devices ผ่าน address, data และ control lines. External device แลกข้อมูลกับสิ่งแวดล้อมผ่าน link ไปยัง I/O module และแบ่งเป็น human readable, machine readable กับ communication. ภาพอุปกรณ์แสดง control logic, buffer และ transducer ที่แปลงข้อมูลระหว่างอุปกรณ์กับสิ่งแวดล้อม.

**ประเด็นที่ต้องจำ**

- System bus มี address/data/control lines ต่อ I/O module (หน้า 3)
- External devices มี 3 หมวด: human readable, machine readable, communication (หน้า 4)
- อุปกรณ์ตัวอย่างมี control logic, buffer, transducer พร้อม data/status/control signals (หน้า 5)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- I/O module
- system bus
- peripheral device
- control logic
- buffer
- transducer

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามลูกศรหน้า 5: ข้อมูลจากสิ่งแวดล้อมผ่าน transducer/buffer ไปเป็น data bits ของ I/O module

**จุดที่อาจสับสน:** อย่าสับสน I/O module ที่เชื่อม bus กับ external device ที่แปลง/รับส่งข้อมูลจากสิ่งแวดล้อม

**ประโยคช่วยจำ:** bus → module → device → environment

### 2. หน้าที่และโครงสร้างภายใน I/O module

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 6–7**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

I/O module ประสานการไหลของข้อมูลและเวลา สื่อสารกับ processor และ device จัด buffer ให้ความเร็วต่างกัน และตรวจ error. ภาพโครงสร้างมี data registers, status/control registers, I/O logic และ external-device interface logic เชื่อมกับ system bus และอุปกรณ์.

**ประเด็นที่ต้องจำ**

- Control and timing ประสาน traffic; processor communication ถอด command รับ address/data/status (หน้า 6)
- Device communication ส่ง command/status/data; buffering ชดเชยความเร็ว; error detection รายงานข้อผิดพลาด (หน้า 6)
- Data registers และ status/control registers แยกหน้าที่ใน I/O module (หน้า 7)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- control and timing
- processor communication
- device communication
- data buffering
- error detection
- data register

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านภาพหน้า 7 จาก data/address/control lines ไปยัง I/O logic แล้วออก external-device interface logic

**จุดที่อาจสับสน:** buffering เป็นหนึ่งในหน้าที่ I/O module; ไม่ใช่การแทนที่ register ทุกชนิด

**ประโยคช่วยจำ:** คุม–คุย CPU–คุย device–พักข้อมูล–ตรวจผิด

### 3. Programmed I/O, Interrupt-driven I/O และ DMA

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 8–9**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

Programmed I/O ให้ processor สั่งและรอ I/O module จนเสร็จ จึงเสียเวลาหาก processor เร็วกว่าอุปกรณ์. Interrupt-driven I/O ให้ processor ทำงานอื่นระหว่างรอ แล้ว module แจ้งเมื่อเสร็จ. DMA ให้ I/O module กับ main memory แลกข้อมูลโดยตรงโดยไม่ให้ processor อยู่ในทางเดินข้อมูล.

**ประเด็นที่ต้องจำ**

- Programmed: processor control และ wait (หน้า 8)
- Interrupt-driven: สั่งแล้วทำงานต่อ; module interrupt เมื่อเสร็จ (หน้า 8)
- DMA: I/O-to-memory โดยตรง ต่างจากสองวิธีที่ผ่าน processor (หน้า 8–9)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- programmed I/O
- interrupt-driven I/O
- direct memory access (DMA)
- polling

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตารางหน้า 9 จัด programmed/interrupt-driven เป็น I/O-to-memory ผ่าน processor; DMA เป็น direct transfer

| เทคนิค | CPU ระหว่างรอ | ทางเดินข้อมูล |
| --- | --- | --- |
| Programmed | รอ | ผ่าน processor |
| Interrupt-driven | ทำงานอื่นจน interrupt | ผ่าน processor |
| DMA | ช่วยตั้งต้น/จบงาน | I/O↔memory โดยตรง |

**จุดที่อาจสับสน:** interrupt ช่วยให้ CPU ไม่ต้องรอเฉย ๆ แต่ทางเดิน data ยังผ่าน processor ในตารางหน้า 9; DMA เปลี่ยนทางเดิน data

**ประโยคช่วยจำ:** รอเอง–ให้เรียก–ส่งตรง

### 4. คำสั่ง Control, Test, Read, Write

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 10**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

I/O module รับคำสั่งจาก processor ได้สี่ชนิด. Control เปิดใช้และบอกอุปกรณ์ให้ทำงาน, Test ตรวจเงื่อนไขสถานะ, Read นำข้อมูลจาก peripheral เข้าสู่ internal buffer และ Write นำข้อมูลจาก data bus ไปส่งให้อุปกรณ์.

**ประเด็นที่ต้องจำ**

- Control = activate/tell peripheral what to do
- Test = test status conditions
- Read = peripheral→internal buffer
- Write = data bus→peripheral

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Control
- Test
- Read
- Write
- internal buffer

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** แยกทิศข้อมูล: Read เข้ามาใน I/O module; Write ออกจาก data bus ไป peripheral

**จุดที่อาจสับสน:** Test ตรวจสถานะ ไม่ใช่อ่าน data item จาก peripheral; Read ต่างจาก Test

**ประโยคช่วยจำ:** คุม–เช็ก–รับ–ส่ง

### 5. ผังการรับ block ของข้อมูลด้วยสามเทคนิค

**🟡 สำคัญ** · itds-211_comp_arch_Chapter05.pdf, **หน้า 11**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบ ตัวอย่างการประยุกต์ หรือการเชื่อมกลไกหลัก

ผังหน้า 11 วาง programmed, interrupt-driven และ DMA ข้างกันเพื่อเทียบลำดับการรับ block. สองแบบแรกยังให้ CPU อ่าน word จาก I/O module และเขียนลง memory; programmed วนตรวจ status ขณะ interrupt-driven ทำงานอื่นระหว่างรอ. DMA รับคำสั่งเป็น block แล้วมี interrupt/status เมื่อสิ้นสุดการโอน.

**ประเด็นที่ต้องจำ**

- Programmed: issue read → read/check status ซ้ำ → CPU read word → CPU write memory (หน้า 11)
- Interrupt-driven: CPU ทำอย่างอื่นระหว่างรอ แต่ยัง read word/write memory หลัง interrupt (หน้า 11)
- DMA: issue read block → CPU ทำอย่างอื่น → รับ completion interrupt/status (หน้า 11)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- status check
- block read
- completion interrupt
- CPU-to-memory transfer

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่สามคอลัมน์หน้า 11 แล้วทำเครื่องหมายว่าช่วงใด CPU เป็นผู้ย้าย word

**จุดที่อาจสับสน:** interrupt-driven ไม่เท่ากับ DMA: ผังกลางยังมี CPU→memory write word

**ประโยคช่วยจำ:** ดูว่าใครย้าย word

### 6. I/O instructions, Memory-mapped และ Isolated I/O

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 12–14**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

แต่ละ I/O device มี identifier/address และ module ตีความ address lines เพื่อรับคำสั่งของตน. Memory-mapped I/O ใช้ address space ร่วมกับ memory จึงใช้คำสั่งอ่าน/เขียนแบบ memory; isolated I/O แยก address space และมีคำสั่ง/สัญญาณเลือก I/O เฉพาะ. ภาพ keyboard หน้า 14 แสดง register ที่ address 516/517 เทียบกับ instruction Load I/O/Test I/O/In ของ isolated I/O.

**ประเด็นที่ต้องจำ**

- Memory-mapped: address space ร่วม, read/write lines เดียว, memory access commands ใช้ได้ (หน้า 12–13)
- Isolated: separate address spaces, I/O-or-memory select lines, special I/O commands (หน้า 13)
- Keyboard example memory-mapped ใช้ input data register 516, status/control 517 (หน้า 14)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- device address
- memory-mapped I/O
- isolated I/O
- status/control register
- I/O select line

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบสองคอลัมน์หน้า 14: ทางซ้ายใช้ load/store address 516/517, ทางขวาใช้ Load I/O, Test I/O, In กับ operand 5

| แบบ | Address space | คำสั่ง |
| --- | --- | --- |
| Memory-mapped | ร่วมกับ memory | memory read/write |
| Isolated | แยกจาก memory | special I/O commands |

**จุดที่อาจสับสน:** เลข 516/517 และ operand 5 เป็นตัวอย่างของคนละ address space/รูปแบบคำสั่ง ไม่ใช่ค่าที่ต้องเท่ากัน

**ประโยคช่วยจำ:** mapped ใช้ address ร่วม; isolated แยก

### 7. Interrupt-driven I/O และการเก็บ/คืนสถานะ

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 15–17**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

Interrupt-driven I/O ให้ processor ออกคำสั่งแล้วทำงานอื่นจน I/O module พร้อมจึงขอ interrupt. ในผัง simple interrupt processor จบ current instruction, acknowledge, เก็บ PSW กับ PC บน control stack แล้วโหลด PC ของ routine ใหม่. Software เก็บ state ที่เหลือ ประมวลผล interrupt แล้วคืน state, PSW และ PC เดิมเพื่อทำงานต่อ.

**ประเด็นที่ต้องจำ**

- CPU จบคำสั่งปัจจุบันก่อนตอบ interrupt (หน้า 16)
- เก็บ PSW/PC บน control stack แล้ว load new PC ตาม interrupt (หน้า 16)
- Software save/process/restore state; ภาพหน้า 17 แสดง memory/register ก่อนและหลัง return (หน้า 16–17)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- interrupt
- acknowledgement
- PC
- PSW
- control stack
- ISR

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ลูกศรหน้า 16 จาก hardware ไป software และตาม PC/stack ในภาพหน้า 17

**จุดที่อาจสับสน:** แยกการเก็บ PSW/PC โดย processor กับการเก็บ remainder of process state ใน software ตามผัง; อย่าบอกว่า interrupt เริ่มกลางคำสั่งที่ยังไม่จบ

**ประโยคช่วยจำ:** จบคำสั่ง–เก็บ PC/PSW–บริการ–คืน

### 8. ปัญหา priority และวิธีระบุ device ที่ interrupt

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 18–19**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

เมื่อมี I/O modules หลายตัว processor ต้องรู้ว่าใครขอ interrupt และเมื่อมีหลาย request ต้องตัดสินใจลำดับที่จัดการ. สไลด์ยกสี่วิธีระบุแหล่ง: multiple interrupt lines, software poll, daisy chain แบบ vectored และ bus arbitration แบบ vectored. Software poll ใช้ routine ตรวจ module ทีละตัว ส่วน vectored ส่ง identifier/vector เพื่อพาไปยัง device-service routine.

**ประเด็นที่ต้องจำ**

- สอง design issues: identify requester และเลือกจัดการเมื่อ interrupts หลายตัว (หน้า 18)
- Software poll ต้องไล่ตรวจ module และกินเวลา; daisy chain ส่ง acknowledge ผ่าน module (หน้า 19)
- Bus arbitration: module ได้ bus ก่อน, processor acknowledge, module วาง vector บน data lines (หน้า 19)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- multiple interrupt lines
- software poll
- daisy chain
- bus arbitration
- vectored interrupt
- vector

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตาราง 4 ช่องหน้า 19: จับคู่ชื่อวิธีกับสัญญาณ/ลำดับของมัน

| วิธี | ระบุผู้ร้องขอ |
| --- | --- |
| Multiple lines | แยก interrupt line |
| Software poll | routine ถาม module ทีละตัว |
| Daisy chain | acknowledge ผ่าน chain แล้วใช้ vector |
| Bus arbitration | ผู้ได้ bus ส่ง vector บน data lines |

**จุดที่อาจสับสน:** คำว่า vector ในสไลด์คือ address หรือ identifier ที่ใช้ชี้ routine ไม่ใช่ตัวข้อมูล I/O ที่รับส่ง

**ประโยคช่วยจำ:** ใครขอ? ใครก่อน? poll หรือ vector

### 9. 82C59A interrupt controller แบบ master/slave

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter05.pdf, **หน้า 20**

เหตุผลการจัดระดับ: เป็นอุปกรณ์หรือเทคโนโลยีตัวอย่างที่สไลด์ให้รายละเอียดประกอบ

ภาพหน้า 20 ยกการต่อ external devices เข้ากับ slave 82C59A หลายตัว แล้ว slave ส่ง INT ไปยัง IR inputs ของ master. Master ส่ง INT ไปยัง INTR ของ processor 80386. นี่เป็นตัวอย่างโครงสร้าง interrupt controller ในสไลด์ ไม่ใช่ข้อกำหนดของทุกระบบ.

**ประเด็นที่ต้องจำ**

- Slave รับ external-device lines IR0–IR7 (หน้า 20)
- INT ของ slave เข้าสู่ master; INT ของ master เข้าสู่ INTR ของ processor (หน้า 20)
- ภาพยก 80386 และ 82C59A เป็นตัวอย่างระบบ (หน้า 20)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- 82C59A
- master
- slave
- IR0–IR7
- INT
- INTR

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามเส้นจาก external device 00 ผ่าน slave ตัวบน, master แล้วถึง processor

**จุดที่อาจสับสน:** อย่าสลับ INT output ของ controller กับ INTR input ของ processor ในภาพนี้

**ประโยคช่วยจำ:** device → slave → master → CPU

### 10. Intel 8255A/82C55A และ control word

**🟡 สำคัญ** · itds-211_comp_arch_Chapter05.pdf, **หน้า 21–23**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบ ตัวอย่างการประยุกต์ หรือการเชื่อมกลไกหลัก

ตัวอย่าง programmable peripheral interface แสดง Port A, Port B และ Port C ที่แบ่ง upper/lower พร้อม data-bus buffer และ read/write control logic. Control word หน้า 22 ตั้ง mode และทิศ input/output ของ ports หรือเลือก bit set/reset ใน Port C. ภาพหน้า 23 แสดงการใช้ Port A รับ keyboard, Port B ส่ง display และ Port C ทำ handshake/interrupt.

**ประเด็นที่ต้องจำ**

- 8255A block diagram มี Port A/B อย่างละ 8 บิต และ Port C upper/lower อย่างละ 4 บิต (หน้า 21)
- Control word: D7=1 ใช้ mode set; D7=0 ใช้ bit set/reset ของ Port C (หน้า 22)
- ตัวอย่าง keyboard↔Port A, display↔Port B, Port C ใช้ ready/acknowledge/interrupt (หน้า 23)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- 8255A
- 82C55A
- control word
- mode set
- bit set/reset
- Port A/B/C

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบ (a) mode definition กับ (b) bit definition หน้า 22 แล้วตามการต่อจริงหน้า 23

**จุดที่อาจสับสน:** หน้า 21–22 เรียก 8255A แต่หน้า 23 เรียก 82C55A; ชื่อรุ่นในภาพต้องอ่านตามแต่ละสไลด์ ไม่รวมเป็นเลขเดียวโดยเดา

**ประโยคช่วยจำ:** A รับ keyboard, B ส่ง display, C คุมสัญญาณในภาพ

### 11. ข้อจำกัดของ I/O ผ่าน CPU และเหตุผลใช้ DMA

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 24**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

Programmed และ interrupt-driven I/O มีข้อจำกัดร่วมคืออัตราโอนขึ้นกับความเร็วที่ processor ตรวจ/บริการ device และ processor ต้องรันหลายคำสั่งต่อการโอนแต่ละครั้ง. เมื่อย้ายข้อมูลปริมาณมาก สไลด์จึงเสนอ direct memory access เพื่อให้โอนได้มีประสิทธิภาพกว่า.

**ประเด็นที่ต้องจำ**

- Transfer rate ถูกจำกัดด้วยความเร็วตรวจ/บริการ device ของ processor (หน้า 24)
- Processor ยังจัดการ transfer และรัน instructions ต่อครั้ง (หน้า 24)
- Large data volume เป็นเหตุผลใช้ DMA (หน้า 24)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- I/O transfer rate
- programmed I/O
- interrupt-driven I/O
- DMA

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เชื่อมตารางหน้า 9 กับข้อเสียหน้า 24: ทั้งสองแบบแรกยังมี CPU ในเส้นทางการโอน

**จุดที่อาจสับสน:** interrupt ลดการรอว่าง แต่ไม่ได้ย้าย CPU ออกจากการโอนข้อมูลแต่ละ word ตามผังหน้า 11

**ประโยคช่วยจำ:** ข้อมูลมาก → ให้ DMA รับทางเดิน

### 12. DMA block diagram และ breakpoint ใน instruction cycle

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 25–26**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

DMA controller ในภาพมี data count, data register, address register และ control logic พร้อม request/acknowledge, interrupt, read/write signals. ภาพ instruction cycle แยก DMA breakpoints ที่อยู่ระหว่าง processor cycles หลายจุด กับ interrupt breakpoint หลัง store result ก่อนขั้น process interrupt. หมายเหตุภาษาไทยบนสไลด์อธิบาย DMA แทรกเกี่ยวกับ hardware bus โดยตรง.

**ประเด็นที่ต้องจำ**

- data count/address/data register และ control logic ใน DMA module (หน้า 25)
- DMA breakpoints ปรากฏหลายจุดใน instruction cycle; interrupt breakpoint ปรากฏก่อน process interrupt (หน้า 26)
- อ่าน request, acknowledge, read/write, interrupt ตามลูกศรของ DMA controller (หน้า 25)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- DMA controller
- data count
- address register
- DMA breakpoint
- interrupt breakpoint

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามภาพหน้า 26: จุด DMA มีหลัง fetch/decode/execute ตามลูกศร; interrupt อยู่หลัง store result

**จุดที่อาจสับสน:** อย่ากล่าวว่า DMA ต้องรอ interrupt checkpoint จุดเดียว; ภาพแยก DMA กับ interrupt breakpoint

**ประโยคช่วยจำ:** DMA ดู bus หลายจุด; interrupt หลังคำสั่ง

### 13. Alternative DMA configurations และ Intel 8237A

**🟡 สำคัญ** · itds-211_comp_arch_Chapter05.pdf, **หน้า 27–30**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบ ตัวอย่างการประยุกต์ หรือการเชื่อมกลไกหลัก

ภาพหน้า 27 เทียบ DMA แยกบน single bus, DMA รวมกับ I/O บน single bus และแบบแยก I/O bus. ตัวอย่าง 8237 หน้า 28 แสดง DREQ/DACK ระหว่าง disk controller กับ DMA และ HRQ/HLDA ระหว่าง DMA กับ CPU. หน้า 29 ระบุว่า data ไม่เก็บใน DMA chip, มี 4 channels และทำ memory-to-memory ผ่าน register ได้; ตาราง register หน้า 30 มีรายการ status ซ้ำที่อ่านแล้วกำกวม.

**ประเด็นที่ต้องจำ**

- สาม configuration: single-bus detached, single-bus integrated DMA-I/O, I/O bus (หน้า 27)
- DREQ/DACK = DMA request/acknowledge; HRQ/HLDA = hold request/acknowledge (หน้า 28)
- 8237 มี 4 channels 0–3; data ไม่เก็บใน chip ระหว่าง transfer ตามคำอธิบาย (หน้า 29)
- ตาราง Intel 8237A มี command/status/mode/masks; E/D และ TC มีคำขยายใต้ตาราง (หน้า 30)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- single-bus DMA
- I/O bus
- DREQ
- DACK
- HRQ
- HLDA
- terminal count
- 8237A

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามสัญญาณหน้า 28: disk controller ขอ DMA ด้วย DREQ; DMA ขอ hold จาก CPU ด้วย HRQ; หลังยืนยันจึงใช้ bus ตามภาพ

**จุดที่อาจสับสน:** หน้า 29 พูด DMA ปกติระหว่าง I/O port-memory แต่ระบุข้อยกเว้น memory-to-memory ผ่าน register; หน้า 30 status แถว D4–D7 พิมพ์ Channel 0 request ซ้ำ: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** DREQ ขอ DMA; HRQ ขอ bus

### 14. Direct Cache Access (DCA) และภาพ Xeon

**🟡 สำคัญ** · itds-211_comp_arch_Chapter05.pdf, **หน้า 31–32**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบ ตัวอย่างการประยุกต์ หรือการเชื่อมกลไกหลัก

สไลด์นำ DCA ต่อจาก DMA เพราะปริมาณ network I/O ในตัวอย่างระบบสูงขึ้นจน DMA อย่างเดียวมีข้อจำกัดการขยายตัวตามคำอธิบาย. ภาพ Xeon E5-2600/4600 แสดง cores, L1/L2/L3 cache, PCIe/QPI และ memory controller hub เพื่อวางตำแหน่ง data path. ตัวเลข 10/100 Gbps และรุ่นชิปเป็นบริบทตัวอย่างในสไลด์.

**ประเด็นที่ต้องจำ**

- แรงผลักในสไลด์คือ network data rate สูง เช่น 10/100-Gbps Ethernet และ Wi-Fi ระดับ gigabit (หน้า 31)
- ภาพ Xeon มี cores 0–7, L1/L2 ต่อ core, L3 segments, PCIe/QPI และ memory controller hub (หน้า 32)
- DCA ถูกเสนอหลังปัญหาการ scale ของ DMA ในกรณี network I/O (หน้า 31)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Direct Cache Access (DCA)
- network I/O
- Xeon E5-2600/4600
- PCIe
- QPI
- L3 cache

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านภาพหน้า 32 จาก PCIe สำหรับ I/O เข้าสู่วง cache และ cores; ใช้เพื่อเห็นจุดที่ cache เกี่ยวข้องกับ packet

**จุดที่อาจสับสน:** อย่าอ้างว่า 10/100 Gbps หรือสถาปัตยกรรม Xeon นี้เป็นสเปกปัจจุบัน; เป็นตัวอย่างจากสไลด์

**ประโยคช่วยจำ:** network เร็วขึ้น → data path ผ่าน cache สำคัญขึ้น

### 15. Packet traffic, buffers และ cache-related performance

**🟡 สำคัญ** · itds-211_comp_arch_Chapter05.pdf, **หน้า 33–35**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบ ตัวอย่างการประยุกต์ หรือการเชื่อมกลไกหลัก

Network traffic อยู่ในรูป packets/PDU; สไลด์ยก Ethernet ที่ครอบ IP/TCP และการทำงานของ NIC. ใน DMA scheme ขาออก application buffer ถูกคัดไป system buffer ใน main memory พร้อม TCP/IP headers ก่อน NIC นำไป; ขาเข้าก็มีการย้ายระหว่าง buffers. ขั้น incoming หน้า 35 มี DMA, NIC interrupt, retrieval, cache miss, header processing และ payload transfer.

**ประเด็นที่ต้องจำ**

- Ethernet packet บรรทุก higher-level IP/TCP packet ตามลำดับชั้นที่สไลด์อธิบาย (หน้า 33)
- Outgoing DMA path ใช้ application buffer→system buffer พร้อม headers→NIC (หน้า 34)
- Incoming: packet arrives→DMA→NIC interrupts host→retrieve descriptors/headers→cache miss→process header→transfer payload (หน้า 35)
- Outgoing: request→create packet→invoke output→DMA→NIC completion→driver frees buffer (หน้า 35)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- packet
- PDU
- Ethernet
- IP
- TCP
- NIC
- application buffer
- system buffer
- cache miss

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ตารางสองคอลัมน์หน้า 35 เพื่อเทียบ incoming/outgoing; เชื่อมกับข้อความ buffer copy หน้า 34

**จุดที่อาจสับสน:** อย่าสรุปว่า DMA ไม่เกี่ยวกับ cache: หน้า 34–35 ระบุ core, main memory และ cache ล้วนอยู่ในทางเดิน

**ประโยคช่วยจำ:** packet ผ่าน buffer และ cache ก่อนถึงงานของ core

### 16. DCA prefetch, cache injection และ DDIO

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 36–37**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

DCA แบบ prototype ในสไลด์ใช้กับ incoming network traffic: memory controller ส่ง prefetch hint เมื่อ data พร้อมใน system memory เพื่อให้ core ดึง packet จาก system buffer ล่วงหน้า. แนวที่ก้าวต่อไปคือหลีกเลี่ยง system buffer ใน main memory ผ่าน cache injection ซึ่งสไลด์เรียก Direct Data I/O (DDIO) ในสาย Xeon. ภาพหน้า 37 เทียบ DMA ที่โอนผ่าน main memory กับ DDIO ที่เข้าหรือออกผ่าน last-level cache.

**ประเด็นที่ต้องจำ**

- DCA prototype เฉพาะ incoming; memory controller ส่ง prefetch hint ให้ core (หน้า 36)
- cache injection/DDIO ลดการผ่าน system buffer ใน main memory (หน้า 36)
- ภาพเปรียบ DMA transfer to/from memory กับ DDIO transfer to/from cache (หน้า 37)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- DCA
- prefetch hint
- system buffer
- cache injection
- Direct Data I/O (DDIO)
- last-level cache

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูภาพ (a)–(d) หน้า 37 แล้วตามลูกศรสีเขียวว่าข้อมูลผ่าน main memory หรือ last-level cache

| กลไก | ทางเดิน/บทบาทในสไลด์ |
| --- | --- |
| Normal DMA | I/O ↔ main memory |
| DCA prototype | data อยู่ system memory แล้วส่ง prefetch hint |
| DDIO/cache injection | I/O ↔ last-level cache |

**จุดที่อาจสับสน:** DCA prototype ที่อธิบาย incoming only ไม่ใช่ข้อจำกัดที่ระบุให้ DDIO ทุกกรณี; ภาพ DDIO มีทั้ง transfer to cache และ to I/O

**ประโยคช่วยจำ:** DCA เตรียม cache; DDIO ส่งผ่าน cache

### 17. วิวัฒนาการ I/O function และ I/O channel

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter05.pdf, **หน้า 38–39**

เหตุผลการจัดระดับ: เป็นโครงสร้าง คำสั่ง ขั้นตอน หรือกลไกหลักที่สไลด์ใช้ต่อยอด

สไลด์เรียงวิวัฒนาการจาก CPU คุมอุปกรณ์ตรง → เพิ่ม I/O module แบบ programmed → interrupt → DMA → module เป็น processor เฉพาะทาง → module มี local memory จนทำงานได้คล้ายคอมพิวเตอร์ของตน. ภาพ I/O channel แยก selector channel กับ multiplexor channel โดยทั้งคู่เชื่อม memory/CPU กับ I/O controllers แต่จัดทางเชื่อมอุปกรณ์ต่างกัน.

**ประเด็นที่ต้องจำ**

- 6 ขั้นวิวัฒนาการเรียงจาก CPU direct control ถึง I/O module ที่มี local memory (หน้า 38)
- Interrupt ลดเวลารอของ CPU; DMA ย้าย block โดย CPU ช่วยเริ่ม/จบตามคำอธิบาย (หน้า 38)
- Selector กับ multiplexor channel เป็นสองสถาปัตยกรรมในภาพหน้า 39

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- I/O function
- I/O module
- DMA
- I/O channel
- selector channel
- multiplexor channel
- local memory

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จับคู่ขั้นที่ 2–4 หน้า 38 กับ programmed, interrupt และ DMA แล้วดูรูป selector/multiplexor หน้า 39

**จุดที่อาจสับสน:** อย่าคิดว่าทุกขั้นของวิวัฒนาการแทนของเดิมทั้งหมด; สไลด์เป็นลำดับการเพิ่มความสามารถของ module

**ประโยคช่วยจำ:** CPU คุม → module → interrupt → DMA → processor I/O

### 18. USB generations และ host-controller tree

**🟡 สำคัญ** · itds-211_comp_arch_Chapter05.pdf, **หน้า 41**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบ ตัวอย่างการประยุกต์ หรือการเชื่อมกลไกหลัก

สไลด์ยก USB เป็นตัวอย่าง peripheral connection หลายรุ่น และแยก signaling rate ออกจาก usable data rate ใน SuperSpeed. ตัวเลขที่ให้มี USB 1.0 low/full 1.5/12 Mbps, USB 2.0 480 Mbps, USB 3.0 signaling 5 Gbps usable สูงสุด 4 Gbps, USB 3.1 Gen2 signaling 10 Gbps usable ตามสไลด์ 9.7 Gbps และ USB 3.2 Gen2x2 20 Gbps. Root host controller เชื่อมอุปกรณ์เป็น hierarchical tree.

**ประเด็นที่ต้องจำ**

- USB 1.0 Low/Full Speed 1.5/12 Mbps; USB 2.0 480 Mbps (หน้า 41)
- USB 3.0/3.1 Gen1 signaling 5 Gbps, usable สูงสุด 4 Gbps; Gen2 signaling 10 Gbps, usable ทฤษฎี 9.7 Gbps (หน้า 41)
- USB 3.2 Gen2x2 20 Gbps; root host controller จัด tree topology (หน้า 41)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- USB
- Low Speed
- Full Speed
- SuperSpeed
- SuperSpeed+
- signaling rate
- usable data rate
- root host controller

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านตัวเลขหน้า 41 โดยแยกความเร็วสัญญาณกับ usable data rate แล้วจับคู่ generation

**จุดที่อาจสับสน:** เลขเหล่านี้เป็นตัวเลขตามสไลด์/ยุคของเอกสาร ไม่ใช่สเปก USB ปัจจุบัน; อย่าสลับ signaling 5 Gbps กับ usable 4 Gbps

**ประโยคช่วยจำ:** ดูรุ่น–ดูหน่วย–แยก signaling/usable

### 19. FireWire และ SCSI ในชุดตัวอย่าง

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter05.pdf, **หน้า 42–43**

เหตุผลการจัดระดับ: เป็นอุปกรณ์หรือเทคโนโลยีตัวอย่างที่สไลด์ให้รายละเอียดประกอบ

FireWire ตามสไลด์คือ IEEE 1394 high-performance serial bus ที่ใช้ daisy chain และรองรับ hot plugging/automatic configuration. SCSI เป็น Small Computer System Interface สำหรับ peripheral โดยภาพรวมหน้า 43 กล่าวถึง shared parallel bus และการใช้กับ mass memory ใน enterprise. ทั้งสองหน้าเป็นตัวอย่างเทคโนโลยีที่ถูกจัดให้รายงานกลุ่ม.

**ประเด็นที่ต้องจำ**

- FireWire: IEEE 1394, daisy chain สูงสุด 63 devices ต่อ port, hot plugging และ auto config (หน้า 42)
- SCSI: shared bus แบบ parallel, 16 หรือ 32 devices ตาม generation, high-speed version สำหรับ mass memory (หน้า 43)
- SCSI ย่อจาก Small Computer System Interface (หน้า 43)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- FireWire
- IEEE 1394
- daisy chain
- hot plugging
- SCSI
- parallel bus

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบ serial daisy chain ของ FireWire หน้า 42 กับ shared parallel bus ของ SCSI หน้า 43

| ตัวอย่าง | รูปแบบในสไลด์ | จุดเด่นที่ให้ |
| --- | --- | --- |
| FireWire | serial daisy chain | hot plugging/auto config |
| SCSI | shared parallel bus | mass memory/enterprise |

**จุดที่อาจสับสน:** ข้อเปรียบเทียบนี้อ้างเฉพาะระบบ/รุ่นในสไลด์; อย่าถือว่าเป็นคำแนะนำเลือกใช้อุปกรณ์ปัจจุบัน

**ประโยคช่วยจำ:** FireWire serial chain; SCSI parallel shared

### 20. Thunderbolt และ InfiniBand

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter05.pdf, **หน้า 44–45**

เหตุผลการจัดระดับ: เป็นอุปกรณ์หรือเทคโนโลยีตัวอย่างที่สไลด์ให้รายละเอียดประกอบ

Thunderbolt ในสไลด์รวม data, video, audio และ power ในสายเชื่อม peripheral เดียว พร้อมตัวเลขตัวอย่าง 10 Gbps ต่อทิศและ 10 W. InfiniBand ถูกวางสำหรับ high-end server และ storage area networking ผ่าน fabric ของ switches/links เพื่อเชื่อม server, storage และ network devices. ตัวเลขความเร็วและขนาดระบบเป็นข้อมูลตามสไลด์.

**ประเด็นที่ต้องจำ**

- Thunderbolt รวม data/video/audio/power และระบุ 10 Gbps แต่ละทิศ, 10 W ตามสไลด์ (หน้า 44)
- InfiniBand มุ่ง high-end server, storage area networking และ switch-based fabric (หน้า 45)
- สไลด์ยก IBM zEnterprise และสูงสุด 64,000 devices เป็นบริบทตัวอย่าง (หน้า 45)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Thunderbolt
- InfiniBand
- fabric
- switch-based architecture
- storage area network

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้หัวข้อการใช้งานเทียบ: Thunderbolt ต่อ peripherals; InfiniBand เชื่อมระบบ server/storage จำนวนมากใน fabric

**จุดที่อาจสับสน:** ตัวเลข 10 Gbps/10 W และ 64,000 เป็นข้อมูลในเอกสาร ไม่ใช่ข้อเท็จจริงอัปเดตของเทคโนโลยี

**ประโยคช่วยจำ:** Thunderbolt รวมสาย; InfiniBand รวม fabric

### 21. PCI Express และ SATA

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter05.pdf, **หน้า 46**

เหตุผลการจัดระดับ: เป็นอุปกรณ์หรือเทคโนโลยีตัวอย่างที่สไลด์ให้รายละเอียดประกอบ

สไลด์ยก PCI Express เป็น high-speed bus สำหรับเชื่อม peripherals หลายชนิดและความเร็ว. SATA ย่อจาก Serial Advanced Technology Attachment และใช้เป็น interface สำหรับ disk storage systems. ตัวเลข data rate ในหน้า 46 เป็นตัวอย่างตามเอกสารและควรอ่านเป็นข้อมูลประจำสไลด์.

**ประเด็นที่ต้องจำ**

- PCI Express: high-speed bus สำหรับ peripherals หลายประเภท/ความเร็ว (หน้า 46)
- SATA = Serial Advanced Technology Attachment; interface สำหรับ disk storage (หน้า 46)
- สไลด์ให้ตัวเลขสูงสุด 6 Gbps และ 300 Mbps ต่อ device ในคำอธิบาย SATA: ต้องตรวจสอบจากต้นฉบับก่อนใช้คำนวณหรืออ้างเป็นสเปก (หน้า 46)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- PCI Express
- PCIe
- SATA
- Serial Advanced Technology Attachment

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูภาพการ์ด PCIe และสาย/drive SATA หน้า 46 เพื่อแยกบริบทการใช้งาน

**จุดที่อาจสับสน:** หน้า 46 วาง 6 Gbps กับ 300 Mbps ต่อ device ในหัวข้อ SATA โดยไม่อธิบายเงื่อนไขที่ทำให้ต่างกัน: ต้องตรวจสอบจากต้นฉบับ; อย่าอนุมานรุ่นหรือความเร็วจริง

**ประโยคช่วยจำ:** PCIe ต่อ peripherals; SATA ต่อ disk

### 22. Ethernet และ Wi-Fi ในชุดตัวอย่าง

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter05.pdf, **หน้า 47–48**

เหตุผลการจัดระดับ: เป็นอุปกรณ์หรือเทคโนโลยีตัวอย่างที่สไลด์ให้รายละเอียดประกอบ

Ethernet ในสไลด์เป็น wired networking ที่เปลี่ยนจาก bus-based ไป switch-based โดยมี central switch เชื่อมอุปกรณ์. Wi-Fi เป็น wireless Internet access ที่เชื่อมอุปกรณ์หลายประเภทและพัฒนามาตรฐาน IEEE 802.11 ต่อเนื่อง. ตัวเลข 100 Gbps Ethernet และ 802.11ac 3.2 Gbps เป็นตัวอย่างที่สไลด์ให้ ณ ช่วงของเอกสาร.

**ประเด็นที่ต้องจำ**

- Ethernet: wired, bus-based → switch-based central switch; ตัวเลขในสไลด์สูงสุด 100 Gbps (หน้า 47)
- Wi-Fi: wireless Internet access; IEEE 802.11; สไลด์ระบุ 802.11ac (2014) สูงสุด 3.2 Gbps (หน้า 48)
- หน้า 40 จัด Ethernet และ Wi-Fi อยู่ในชุดหัวข้อรายงานกลุ่ม

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Ethernet
- wired network
- central switch
- Wi-Fi
- IEEE 802.11
- 802.11ac

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบลูกศร/ภาพหน้า 47 Ethernet cable กับหน้า 48 wireless devices

**จุดที่อาจสับสน:** อย่าใช้คำว่า “current version” จากหน้า 48 เป็นคำบอกเวอร์ชันปัจจุบัน ณ วันนี้; เป็นถ้อยคำในสไลด์

**ประโยคช่วยจำ:** Ethernet มีสาย/สวิตช์; Wi-Fi ไร้สาย/802.11

### 23. ตัวอย่าง IBM EC12 I/O channel subsystem

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter05.pdf, **หน้า 49–51**

เหตุผลการจัดระดับ: เป็นอุปกรณ์หรือเทคโนโลยีตัวอย่างที่สไลด์ให้รายละเอียดประกอบ

ภาพท้ายบทแสดง IBM EC12 channel subsystem, ตู้ I/O frames และการเชื่อม books ผ่าน PCIe/InfiniBand ไปยัง I/O controllers/channels. หน้า 49 ให้ตัวเลข partitions, channel subsystems และ channels ในภาพ แต่ข้อความจำนวน partitions สูงสุดด้านบนกับด้านล่างไม่ตรงกัน. จึงใช้ภาพทบทวนความสัมพันธ์เชิงโครงสร้างโดยไม่สรุปจำนวน partitions ที่ขัดกัน.

**ประเด็นที่ต้องจำ**

- หน้า 49 มี 4 channel subsystems และระบุไม่เกิน 256 channels ต่อ subsystem ในภาพ
- หน้า 50 ภาพตู้แสดง PCIe drawer, I/O cage, processor books, InfiniBand/PCIe interconnects
- หน้า 51 เชื่อม 4 books กับ PCIe switches และ InfiniBand multiplexors เพื่อไป controllers/channels

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- IBM EC12
- channel subsystem
- partition
- channel
- PCIe I/O drawer
- InfiniBand multiplexer

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามแผนภาพหน้า 51 จาก book→PCIe/HCA→switch/multiplexer→controller/channel

**จุดที่อาจสับสน:** หน้า 49 ด้านบนเขียน ≤60 partitions/system แต่ด้านล่างเขียน ≤1024 partitions/system: ต้องตรวจสอบจากต้นฉบับ; ห้ามนำตัวเลขใดเป็นคำตอบแน่นอน

**ประโยคช่วยจำ:** book → channel subsystem → channel → device

## 3. Roadmap ทบทวน

1. **1 · โครงสร้าง I/O** — เริ่ม system bus–module–external device แล้วจำห้าหน้าที่ของ I/O module (itds-211_comp_arch_Chapter05.pdf, หน้า 3–7)
2. **2 · คำสั่งและทางเดินข้อมูล** — เทียบ programmed/interrupt-driven/DMA, command 4 ชนิด และ addressing สองแบบ (itds-211_comp_arch_Chapter05.pdf, หน้า 8–14)
3. **3 · Interrupt** — ไล่ PC/PSW/ISR แล้วตอบว่า device ใดร้องขอและจัด priority อย่างไร (itds-211_comp_arch_Chapter05.pdf, หน้า 15–23)
4. **4 · DMA** — จับข้อจำกัดสองวิธีแรก → DMA controller/breakpoints/configurations/8237 (itds-211_comp_arch_Chapter05.pdf, หน้า 24–30)
5. **5 · Cache กับ network I/O** — ตาม packet buffers/cache miss ก่อนเทียบ DCA prefetch กับ DDIO cache injection (itds-211_comp_arch_Chapter05.pdf, หน้า 31–37)
6. **6 · ระบบใหญ่และ interfaces** — จบด้วยวิวัฒนาการ/channel แล้วอ่านหน้า 41–51 ในฐานะตัวอย่างและหัวข้อรายงาน (itds-211_comp_arch_Chapter05.pdf, หน้า 38–51)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · ผังภาพรวม

อ่านหน้า 3–9 แล้ววาดเส้นทาง bus→I/O module→device กับเปรียบ 3 เทคนิค

**เกณฑ์ผ่าน:** บอกได้ว่า CPU รอหรือไม่ และ data ผ่าน CPU หรือไม่ในแต่ละเทคนิค

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 3–9

### รอบ 2 · Trace คำสั่งและ interrupt

ไล่ Control/Test/Read/Write, memory-mapped/isolated และภาพ interrupt หน้า 16–19

**เกณฑ์ผ่าน:** เล่าลำดับเก็บ/คืน PC/PSW และวิธีระบุ requester ได้

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 10–19

### รอบ 3 · Trace DMA

อ่านข้อจำกัดหน้า 24 แล้วตาม data count/address, breakpoint, DREQ/DACK/HRQ/HLDA และ configurations

**เกณฑ์ผ่าน:** ชี้ผู้ขอ DMA, ผู้ขอ bus และทางเดิน block ได้

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 24–30

### รอบ 4 · Cache/Channel/ตัวอย่าง

ตาม incoming/outgoing packet, DCA/DDIO, I/O channel แล้วทวนกลุ่ม interface ตามบทบาท

**เกณฑ์ผ่าน:** อธิบาย buffer copy กับ cache injection และแยก wired/wireless/storage/server interfaces ได้จากสไลด์

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 31–51

### รอบ 5 · ทดสอบเว้นระยะ

ตอบ 3 ข้อต่อหัวข้อแล้วสุ่ม Quiz; วันถัดไปทวนข้อที่ผิดและเปิดภาพสไลด์ต้นทาง

**เกณฑ์ผ่าน:** ตอบครบหัวข้อสำคัญและชี้หน้า 30/46/49 ที่ต้องตรวจต้นฉบับได้

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 3–51

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1 module/สามเทคนิค/commands/mapping หน้า 3–14; วัน 2 interrupt/DMA หน้า 15–30; วัน 3 DCA/channel/interfaces หน้า 31–51 พร้อม Quiz
- **ถ้าเหลือ 1 วัน:** เรียงสามเทคนิค/ผังหน้า 8–11 → mapping/interrupt หน้า 12–19 → DMA หน้า 24–30 → DCA/DDIO หน้า 33–37 → interface เฉพาะศัพท์ที่ยังสับสน หน้า 41–51
- **ถ้าเหลือ 3 ชั่วโมง:** 0–35 นาทีโครงสร้าง/สามเทคนิค หน้า 3–11; 35–70 นาที mapping/interrupt หน้า 12–19; 70–125 นาที DMA หน้า 24–30; 125–155 นาที DCA/DDIO/channel หน้า 31–39; 155–180 นาที interface key terms/Quiz

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

หัวข้อกลไกและผังการโอนข้อมูลมีน้ำหนักในการทบทวนมากกว่าตัวเลขรุ่น interface เพราะเป็นฐานต่อเนื่องในสไลด์; ไม่มีข้อสอบเก่า จึงไม่ยืนยันความถี่ออกสอบ

- **ควรท่องจำ:** I/O module functions, สาม I/O techniques, Control/Test/Read/Write, memory-mapped/isolated, PC/PSW, interrupt identification, DREQ/DACK/HRQ/HLDA (หน้า 6–19, 25–29)
- **ควรฝึกโจทย์:** ไล่ผังรับ block หน้า 11, keyboard addressing หน้า 14, simple interrupt หน้า 16–17, DMA breakpoints/configurations หน้า 26–28 และ DMA/DDIO หน้า 37
- **ควรเข้าใจแนวคิด:** เหตุผลใช้ DMA, packet buffer/cache miss, DCA prefetch versus DDIO cache injection, I/O channel evolution (หน้า 24, 31–39)
- **เตรียมข้อสอบแบบผสม:** เลือกตอบจับคู่คำศัพท์/สัญญาณ; อัตนัยอธิบาย sequence; วิเคราะห์ผังและทางเดิน data. สไลด์ไม่มีโจทย์คำนวณแยก จึงไม่สร้างโจทย์ตัวเลขที่ไม่มีในเอกสาร

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 23 ข้อ, อัตนัย 23 ข้อ, วิเคราะห์ 23 ข้อ

### I/O module และ external device

**ข้อ 1 · เลือกตอบ: อะไรเชื่อม system bus กับ peripheral?**

- A. I/O module
- B. transducer
- C. application buffer
- D. ISR

เฉลย: I/O module

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 3–5

**ข้อ 2 · อัตนัย: สามกลุ่ม external device ในสไลด์คืออะไร?**

เฉลย: human readable, machine readable และ communication

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 3–5

**ข้อ 3 · วิเคราะห์: ภาพหน้า 5 แยกหน้าที่ control logic กับ transducer อย่างไร?**

เฉลย: control logic รับสัญญาณควบคุม/รายงานสถานะ; transducer แปลงข้อมูลที่เกี่ยวกับสิ่งแวดล้อม

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 3–5

### หน้าที่และโครงสร้างภายใน I/O module

**ข้อ 4 · เลือกตอบ: หน้าที่ใดชดเชยความเร็วระหว่าง device กับ memory?**

- A. Data buffering
- B. Address recognition
- C. Bus arbitration
- D. Software poll

เฉลย: Data buffering

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 6–7

**ข้อ 5 · อัตนัย: หน้าที่หลักห้ากลุ่มของ I/O module คืออะไร?**

เฉลย: control/timing, processor communication, device communication, data buffering และ error detection

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 6–7

**ข้อ 6 · วิเคราะห์: data register ต่างจาก status/control register ในภาพหน้า 7 อย่างไร?**

เฉลย: ช่องแรกเก็บข้อมูล; อีกช่องเก็บสถานะหรือการควบคุมตามชื่อในภาพ

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 6–7

### Programmed I/O, Interrupt-driven I/O และ DMA

**ข้อ 7 · เลือกตอบ: เทคนิคใดโอนข้อมูล I/O↔memory โดยตรง?**

- A. DMA
- B. Programmed I/O
- C. Interrupt-driven I/O
- D. Software poll

เฉลย: DMA

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 8–9

**ข้อ 8 · อัตนัย: Programmed ต่างจาก interrupt-driven อย่างไรเมื่อรอ device?**

เฉลย: programmed รอ; interrupt-driven ไปทำงานอื่นและถูกแจ้งเมื่อ device พร้อม

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 8–9

**ข้อ 9 · วิเคราะห์: ถ้าต้องแยก interrupt-driven กับ DMA จากตารางหน้า 9 ใช้เกณฑ์ใด?**

เฉลย: ดูว่า data transfer ผ่าน processor หรือเป็น direct I/O-to-memory

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 8–9

### คำสั่ง Control, Test, Read, Write

**ข้อ 10 · เลือกตอบ: คำสั่งใดตรวจ status condition?**

- A. Test
- B. Read
- C. Control
- D. Write

เฉลย: Test

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 10

**ข้อ 11 · อัตนัย: Read กับ Write มีทิศข้อมูลอย่างไร?**

เฉลย: Read peripheral→internal buffer; Write data bus→peripheral

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 10

**ข้อ 12 · วิเคราะห์: ถ้า processor ต้องเปิด peripheral ก่อนโอนข้อมูล ใช้คำสั่งประเภทใด?**

เฉลย: Control

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 10

### ผังการรับ block ของข้อมูลด้วยสามเทคนิค

**ข้อ 13 · เลือกตอบ: ผังใดให้ CPU วน read status เมื่อยังไม่พร้อม?**

- A. Programmed I/O
- B. DMA
- C. DCA
- D. DDIO

เฉลย: Programmed I/O

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 11

**ข้อ 14 · อัตนัย: ผัง interrupt-driven มีส่วนที่ยังเหมือน programmed อย่างไร?**

เฉลย: CPU ยังอ่าน word จาก module แล้วเขียน word ลง memory

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 11

**ข้อ 15 · วิเคราะห์: DMA ในผังหน้า 11 ต่างตรงคำสั่งเริ่มอย่างไร?**

เฉลย: เริ่มด้วย read block command แล้ว DMA จัดการโอน block

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 11

### I/O instructions, Memory-mapped และ Isolated I/O

**ข้อ 16 · เลือกตอบ: แบบใดแชร์ address space กับ memory?**

- A. Memory-mapped
- B. Isolated
- C. DMA
- D. Vectored

เฉลย: Memory-mapped

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 12–14

**ข้อ 17 · อัตนัย: isolated I/O ต้องใช้อะไรต่างจาก memory-mapped?**

เฉลย: address space แยกและ special I/O commands/selection lines

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 12–14

**ข้อ 18 · วิเคราะห์: ภาพหน้า 14 keyboard status/control register อยู่ address ใดในตัวอย่าง memory-mapped?**

เฉลย: 517

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 12–14

### Interrupt-driven I/O และการเก็บ/คืนสถานะ

**ข้อ 19 · เลือกตอบ: ก่อนเข้า routine ใหม่ processor เก็บอะไรบน control stack?**

- A. PSW และ PC
- B. DMA count
- C. I/O buffer
- D. cache tag

เฉลย: PSW และ PC

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 15–17

**ข้อ 20 · อัตนัย: ลำดับ simple interrupt หลังกำเนิด request คืออะไร?**

เฉลย: จบ current instruction, acknowledge, เก็บ PSW/PC, โหลด PC ใหม่, เก็บ state ที่เหลือ, service, restore

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 15–17

**ข้อ 21 · วิเคราะห์: เหตุใดต้องคืน PC/PSW เดิม?**

เฉลย: เพื่อกลับไปประมวลผลต่อจากจุดที่ถูก interrupt ตามภาพหน้า 16–17

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 15–17

### ปัญหา priority และวิธีระบุ device ที่ interrupt

**ข้อ 22 · เลือกตอบ: วิธีใดให้ routine ไล่ถามแต่ละ I/O module?**

- A. Software poll
- B. Daisy chain
- C. DMA
- D. Memory-mapped

เฉลย: Software poll

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 18–19

**ข้อ 23 · อัตนัย: สองคำถามออกแบบ interrupt หน้า 18 คืออะไร?**

เฉลย: ระบุ device ที่ร้องขอ และเลือก interrupt ที่จะจัดการเมื่อมีหลายตัว

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 18–19

**ข้อ 24 · วิเคราะห์: bus arbitration แบบ vectored ส่ง vector ผ่านอะไรหลัง acknowledge?**

เฉลย: data lines

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 18–19

### 82C59A interrupt controller แบบ master/slave

**ข้อ 25 · เลือกตอบ: INT ของ master ต่อเข้าขาใดของ 80386 ในภาพ?**

- A. INTR
- B. DREQ
- C. HLDA
- D. PSW

เฉลย: INTR

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 20

**ข้อ 26 · อัตนัย: slave controller ในภาพมี input อะไร?**

เฉลย: IR0–IR7 จาก external devices

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 20

**ข้อ 27 · วิเคราะห์: เหตุใดรูปนี้จึงเรียกว่า master/slave?**

เฉลย: slave รวม request จาก devices แล้วส่งต่อให้ master ซึ่งแจ้ง processor

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 20

### Intel 8255A/82C55A และ control word

**ข้อ 28 · เลือกตอบ: D7=0 ใน control word หน้า 22 ใช้ทำอะไร?**

- A. Bit set/reset Port C
- B. Mode set
- C. DMA request
- D. Interrupt acknowledge

เฉลย: Bit set/reset Port C

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 21–23

**ข้อ 29 · อัตนัย: Port C แบ่งอย่างไรใน block diagram?**

เฉลย: upper 4 bits กับ lower 4 bits

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 21–23

**ข้อ 30 · วิเคราะห์: ในตัวอย่างหน้า 23 Port B ต่อกับอะไร?**

เฉลย: display output port

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 21–23

### ข้อจำกัดของ I/O ผ่าน CPU และเหตุผลใช้ DMA

**ข้อ 31 · เลือกตอบ: ข้อเสียร่วมของ programmed และ interrupt-driven คืออะไร?**

- A. CPU จัดการ transfer
- B. ไม่มี I/O module
- C. ไม่มี device address
- D. ใช้แต่ bus แยก

เฉลย: CPU จัดการ transfer

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 24

**ข้อ 32 · อัตนัย: เหตุใดสไลด์เสนอ DMA สำหรับข้อมูลจำนวนมาก?**

เฉลย: ลดภาระ CPU ที่ต้อง test/service และรันหลายคำสั่งต่อ I/O transfer

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 24

**ข้อ 33 · วิเคราะห์: ข้อเสียนี้สัมพันธ์กับผังรับ block หน้า 11 อย่างไร?**

เฉลย: สองวิธีแรกยังให้ CPU อ่าน word และเขียน memory

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 24

### DMA block diagram และ breakpoint ใน instruction cycle

**ข้อ 34 · เลือกตอบ: DMA controller มี register ใดบอกตำแหน่ง memory?**

- A. Address register
- B. PSW
- C. Status register
- D. Port C

เฉลย: Address register

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 25–26

**ข้อ 35 · อัตนัย: ภาพหน้า 25 แสดงองค์ประกอบหลักใดใน DMA module?**

เฉลย: data count, data register, address register, control logic

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 25–26

**ข้อ 36 · วิเคราะห์: DMA breakpoint ต่างจาก interrupt breakpoint ในภาพหน้า 26 อย่างไร?**

เฉลย: DMA อยู่ได้หลายจุดระหว่าง processor cycles; interrupt อยู่ก่อนขั้น process interrupt

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 25–26

### Alternative DMA configurations และ Intel 8237A

**ข้อ 37 · เลือกตอบ: สัญญาณขอ DMA จาก device ชื่ออะไร?**

- A. DREQ
- B. DACK
- C. HLDA
- D. PSW

เฉลย: DREQ

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 27–30

**ข้อ 38 · อัตนัย: สามโครงสร้าง DMA ในหน้า 27 คืออะไร?**

เฉลย: single-bus detached, single-bus integrated DMA-I/O และ I/O bus

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 27–30

**ข้อ 39 · วิเคราะห์: แถวใดใน status column หน้า 30 ชวนตรวจต้นฉบับ?**

เฉลย: D4–D7 พิมพ์ Channel 0 request ซ้ำ

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 27–30

### Direct Cache Access (DCA) และภาพ Xeon

**ข้อ 40 · เลือกตอบ: อะไรเป็นแรงผลักให้สไลด์พูดถึง DCA?**

- A. network I/O data rates สูงขึ้น
- B. keyboard ช้าลง
- C. จำนวนคำสั่ง ISA ลด
- D. disk ไม่มี sector

เฉลย: network I/O data rates สูงขึ้น

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 31–32

**ข้อ 41 · อัตนัย: ภาพหน้า 32 แสดง cache ระดับใดรอบ cores?**

เฉลย: L1, L2 และ L3

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 31–32

**ข้อ 42 · วิเคราะห์: เหตุใดต้องมอง cache ในเส้นทาง network I/O?**

เฉลย: packet ผ่าน memory/cache/core ตามสไลด์หน้า 33–34

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 31–32

### Packet traffic, buffers และ cache-related performance

**ข้อ 43 · เลือกตอบ: อุปกรณ์ใดส่ง packet ระหว่าง network กับ host ในสไลด์?**

- A. NIC
- B. PSW
- C. 8255 control word
- D. ISR stack

เฉลย: NIC

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 33–35

**ข้อ 44 · อัตนัย: outgoing DMA path ใช้ buffer ใดบ้าง?**

เฉลย: application-assigned buffer และ system buffer ใน main memory

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 33–35

**ข้อ 45 · วิเคราะห์: incoming หลัง NIC interrupt มีขั้นใดที่ชี้ต้นทุน cache?**

เฉลย: retrieve descriptors/headers แล้ว cache miss ก่อน process header

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 33–35

### DCA prefetch, cache injection และ DDIO

**ข้อ 46 · เลือกตอบ: prefetch hint ของ DCA prototype มาจากส่วนใด?**

- A. memory controller
- B. keyboard
- C. control stack
- D. 8255A

เฉลย: memory controller

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 36–37

**ข้อ 47 · อัตนัย: DDIO แตกต่างจาก normal DMA ในภาพหน้า 37 อย่างไร?**

เฉลย: DDIO ใช้ last-level cache เป็นทางเดินข้อมูลแทนการผ่าน main memory ในภาพเปรียบ

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 36–37

**ข้อ 48 · วิเคราะห์: DCA prototype หน้า 36 ใช้กับ traffic ทิศใด?**

เฉลย: incoming network traffic

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 36–37

### วิวัฒนาการ I/O function และ I/O channel

**ข้อ 49 · เลือกตอบ: วิวัฒนาการขั้นใดให้ I/O module เข้าถึง memory โดยตรง?**

- A. DMA
- B. Programmed no interrupt
- C. CPU direct
- D. Software poll

เฉลย: DMA

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 38–39

**ข้อ 50 · อัตนัย: ลำดับหกขั้นในหน้า 38 สรุปอย่างไร?**

เฉลย: CPU direct → module/programmed → interrupt → DMA → specialized I/O processor → module มี local memory

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 38–39

**ข้อ 51 · วิเคราะห์: ภาพหน้า 39 เทียบ channel สองชนิดใด?**

เฉลย: selector และ multiplexor

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 38–39

### USB generations และ host-controller tree

**ข้อ 52 · เลือกตอบ: USB 2.0 ในสไลด์ระบุ data rate เท่าไร?**

- A. 480 Mbps
- B. 12 Mbps
- C. 5 Gbps
- D. 20 Gbps

เฉลย: 480 Mbps

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 41

**ข้อ 53 · อัตนัย: USB 3.0 ในหน้า 41 แยก signaling กับ usable อย่างไร?**

เฉลย: 5 Gbps signaling; usable สูงสุด 4 Gbps เพราะ overhead ตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 41

**ข้อ 54 · วิเคราะห์: อุปกรณ์ USB จัดเป็น topology แบบใดในหน้า 41?**

เฉลย: hierarchical tree ภายใต้ root host controller

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 41

### FireWire และ SCSI ในชุดตัวอย่าง

**ข้อ 55 · เลือกตอบ: SCSI ย่อจากอะไร?**

- A. Small Computer System Interface
- B. Serial Cache System Interface
- C. System Control Signal Input
- D. Single Channel Serial I/O

เฉลย: Small Computer System Interface

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 42–43

**ข้อ 56 · อัตนัย: FireWire ในสไลด์มีคุณสมบัติต่ออุปกรณ์โดยไม่ปิดเครื่องว่าอะไร?**

เฉลย: hot plugging

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 42–43

**ข้อ 57 · วิเคราะห์: FireWire กับ SCSI ในสไลด์ต่างรูป bus อย่างไร?**

เฉลย: FireWire serial daisy chain; SCSI shared parallel bus

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 42–43

### Thunderbolt และ InfiniBand

**ข้อ 58 · เลือกตอบ: เทคโนโลยีใดในหน้า 45 ใช้ switch-based fabric?**

- A. InfiniBand
- B. Thunderbolt
- C. SCSI
- D. USB 1.0

เฉลย: InfiniBand

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 44–45

**ข้อ 59 · อัตนัย: Thunderbolt ในหน้า 44 รวมสัญญาณใด?**

เฉลย: data, video, audio และ power

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 44–45

**ข้อ 60 · วิเคราะห์: InfiniBand เหมาะกับงานกลุ่มใดตามหน้า 45?**

เฉลย: high-end servers และ storage area networking

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 44–45

### PCI Express และ SATA

**ข้อ 61 · เลือกตอบ: SATA ย่อจากอะไร?**

- A. Serial Advanced Technology Attachment
- B. System Address Transfer Architecture
- C. Storage Array Timing Access
- D. Serial Application Transfer Address

เฉลย: Serial Advanced Technology Attachment

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 46

**ข้อ 62 · อัตนัย: PCI Express ใช้เชื่อมอะไรตามหน้า 46?**

เฉลย: peripherals หลายชนิดและหลายความเร็ว

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 46

**ข้อ 63 · วิเคราะห์: ตัวเลข SATA สองค่าใดในหน้า 46 ต้องตรวจเงื่อนไขก่อนใช้?**

เฉลย: 6 Gbps กับ 300 Mbps ต่อ device: ต้องตรวจสอบจากต้นฉบับ

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 46

### Ethernet และ Wi-Fi ในชุดตัวอย่าง

**ข้อ 64 · เลือกตอบ: เทคโนโลยีใดเป็น predominant wireless Internet access ในสไลด์?**

- A. Wi-Fi
- B. Ethernet
- C. SATA
- D. PCIe

เฉลย: Wi-Fi

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 47–48

**ข้อ 65 · อัตนัย: Ethernet เปลี่ยน topology ตามสไลด์อย่างไร?**

เฉลย: จาก bus-based เป็น switch-based มี central switch

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 47–48

**ข้อ 66 · วิเคราะห์: ตัวเลข “current version 802.11ac” ควรตีความอย่างไร?**

เฉลย: เป็นคำของสไลด์หน้า 48 ไม่ใช่สถานะเทคโนโลยีปัจจุบัน

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 47–48

### ตัวอย่าง IBM EC12 I/O channel subsystem

**ข้อ 67 · เลือกตอบ: หน้า 49 แสดง channel subsystem กี่ชุด?**

- A. 4
- B. 8
- C. 15
- D. 256

เฉลย: 4 ชุด

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 49–51

**ข้อ 68 · อัตนัย: ภาพหน้า 51 แสดงเส้นทาง I/O ผ่านส่วนใด?**

เฉลย: books ไป PCIe/HCA แล้วผ่าน switch/multiplexer สู่ controllers/channels

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 49–51

**ข้อ 69 · วิเคราะห์: จำนวน partitions ต่อ system หน้า 49 สรุปได้หรือไม่?**

เฉลย: ต้องตรวจสอบจากต้นฉบับ เพราะภาพเขียน ≤60 และ ≤1024 ขัดกัน

อ้างอิง: itds-211_comp_arch_Chapter05.pdf, หน้า 49–51

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- Generic Model of an I/O Module · หน้า 3: ผัง I/O module เชื่อม address/data/control lines ของ system bus กับ peripheral links (itds-211_comp_arch_Chapter05.pdf, หน้า 3) (itds-211_comp_arch_Chapter05.pdf, หน้า 3)
- External Devices · หน้า 4: ภาพสไลด์เรื่อง External Devices สำหรับทบทวนหัวข้อ I/O module และ external device (itds-211_comp_arch_Chapter05.pdf, หน้า 4) (itds-211_comp_arch_Chapter05.pdf, หน้า 4)
- Block Diagram of an External Device · หน้า 5: ผัง external device แยก control logic, buffer และ transducer (itds-211_comp_arch_Chapter05.pdf, หน้า 5) (itds-211_comp_arch_Chapter05.pdf, หน้า 5)
- The major functions for an I/O module fall into the · หน้า 6: ภาพสไลด์เรื่อง The major functions for an I/O module fall into the สำหรับทบทวนหัวข้อ หน้าที่และโครงสร้างภายใน I/O module (itds-211_comp_arch_Chapter05.pdf, หน้า 6) (itds-211_comp_arch_Chapter05.pdf, หน้า 6)
- Block Diagram of an I/O Module · หน้า 7: ผัง I/O module มี data registers, status/control registers และ device interface logic (itds-211_comp_arch_Chapter05.pdf, หน้า 7) (itds-211_comp_arch_Chapter05.pdf, หน้า 7)
- Programmed I/O · หน้า 8: ภาพสไลด์เรื่อง Programmed I/O สำหรับทบทวนหัวข้อ Programmed I/O, Interrupt-driven I/O และ DMA (itds-211_comp_arch_Chapter05.pdf, หน้า 8) (itds-211_comp_arch_Chapter05.pdf, หน้า 8)
- Summary of I/O Techniques · หน้า 9: ตารางสรุปทางเดินข้อมูลของ programmed, interrupt-driven และ DMA (itds-211_comp_arch_Chapter05.pdf, หน้า 9) (itds-211_comp_arch_Chapter05.pdf, หน้า 9)
- I/O Commands · หน้า 10: ภาพสไลด์เรื่อง I/O Commands สำหรับทบทวนหัวข้อ คำสั่ง Control, Test, Read, Write (itds-211_comp_arch_Chapter05.pdf, หน้า 10) (itds-211_comp_arch_Chapter05.pdf, หน้า 10)
- Three Techniques for Input of a Block of Data · หน้า 11: ผังสามเทคนิคการรับ block: CPU รอ/ทำงานอื่น/ให้ DMA โอน (itds-211_comp_arch_Chapter05.pdf, หน้า 11) (itds-211_comp_arch_Chapter05.pdf, หน้า 11)
- I/O Instructions · หน้า 12: ภาพสไลด์เรื่อง I/O Instructions สำหรับทบทวนหัวข้อ I/O instructions, Memory-mapped และ Isolated I/O (itds-211_comp_arch_Chapter05.pdf, หน้า 12) (itds-211_comp_arch_Chapter05.pdf, หน้า 12)
- I/O Mapping Summary · หน้า 13: ภาพสไลด์เรื่อง I/O Mapping Summary สำหรับทบทวนหัวข้อ I/O instructions, Memory-mapped และ Isolated I/O (itds-211_comp_arch_Chapter05.pdf, หน้า 13) (itds-211_comp_arch_Chapter05.pdf, หน้า 13)
- Memory-Mapped and Isolated I/O · หน้า 14: ตัวอย่าง keyboard เปรียบ memory-mapped address 516/517 กับ isolated I/O operand 5 (itds-211_comp_arch_Chapter05.pdf, หน้า 14) (itds-211_comp_arch_Chapter05.pdf, หน้า 14)
- Interrupt-driven I/O และการเก็บ/คืนสถานะ · หน้า 15: ภาพสไลด์เรื่อง Interrupt-driven I/O และการเก็บ/คืนสถานะ สำหรับทบทวนหัวข้อ Interrupt-driven I/O และการเก็บ/คืนสถานะ (itds-211_comp_arch_Chapter05.pdf, หน้า 15) (itds-211_comp_arch_Chapter05.pdf, หน้า 15)
- Simple Interrupt Processing · หน้า 16: ผัง simple interrupt: จบคำสั่ง เก็บ PSW/PC ไป ISR แล้วคืน state (itds-211_comp_arch_Chapter05.pdf, หน้า 16) (itds-211_comp_arch_Chapter05.pdf, หน้า 16)
- Changes in Memory and Registers for an Interrupt · หน้า 17: ภาพก่อนและหลัง interrupt ใน main memory, control stack และ registers (itds-211_comp_arch_Chapter05.pdf, หน้า 17) (itds-211_comp_arch_Chapter05.pdf, หน้า 17)
- Design Issues · หน้า 18: ภาพสไลด์เรื่อง Design Issues สำหรับทบทวนหัวข้อ ปัญหา priority และวิธีระบุ device ที่ interrupt (itds-211_comp_arch_Chapter05.pdf, หน้า 18) (itds-211_comp_arch_Chapter05.pdf, หน้า 18)
- Device Identiﬁcation · หน้า 19: สี่วิธีระบุ I/O module ที่ร้องขอ interrupt (itds-211_comp_arch_Chapter05.pdf, หน้า 19) (itds-211_comp_arch_Chapter05.pdf, หน้า 19)
- Use of the 82C59A Interrupt Controller · หน้า 20: 82C59A slave controllers ส่ง INT ผ่าน master ไปยัง 80386 (itds-211_comp_arch_Chapter05.pdf, หน้า 20) (itds-211_comp_arch_Chapter05.pdf, หน้า 20)
- Intel 8255A Programmable Peripheral Interface · หน้า 21: ภาพสไลด์เรื่อง Intel 8255A Programmable Peripheral Interface สำหรับทบทวนหัวข้อ Intel 8255A/82C55A และ control word (itds-211_comp_arch_Chapter05.pdf, หน้า 21) (itds-211_comp_arch_Chapter05.pdf, หน้า 21)
- Intel 8255A Control Word · หน้า 22: รูปแบบ control word ของ Intel 8255A สำหรับ mode set และ bit set/reset (itds-211_comp_arch_Chapter05.pdf, หน้า 22) (itds-211_comp_arch_Chapter05.pdf, หน้า 22)
- Keyboard / Display Interface to 82C55A · หน้า 23: ภาพ keyboard/display interface ต่อ Port A/B/C ของ 82C55A (itds-211_comp_arch_Chapter05.pdf, หน้า 23) (itds-211_comp_arch_Chapter05.pdf, หน้า 23)
- Drawbacks of Programmed and Interrupt-Driven I/O · หน้า 24: ภาพสไลด์เรื่อง Drawbacks of Programmed and Interrupt-Driven I/O สำหรับทบทวนหัวข้อ ข้อจำกัดของ I/O ผ่าน CPU และเหตุผลใช้ DMA (itds-211_comp_arch_Chapter05.pdf, หน้า 24) (itds-211_comp_arch_Chapter05.pdf, หน้า 24)
- Typical DMA Block Diagram · หน้า 25: DMA block diagram: data count, data/address registers และ control logic (itds-211_comp_arch_Chapter05.pdf, หน้า 25) (itds-211_comp_arch_Chapter05.pdf, หน้า 25)
- DMA and Interrupt Breakpoints During an Instruction Cycle · หน้า 26: ตำแหน่ง DMA breakpoints และ interrupt breakpoint ใน instruction cycle (itds-211_comp_arch_Chapter05.pdf, หน้า 26) (itds-211_comp_arch_Chapter05.pdf, หน้า 26)
- Alternative DMA Conﬁgurations · หน้า 27: แผนภาพ DMA สาม configuration: detached, integrated และ I/O bus (itds-211_comp_arch_Chapter05.pdf, หน้า 27) (itds-211_comp_arch_Chapter05.pdf, หน้า 27)
- 8237 DMA Usage of System Bus · หน้า 28: สัญญาณ DREQ/DACK และ HRQ/HLDA ของตัวอย่าง 8237 DMA (itds-211_comp_arch_Chapter05.pdf, หน้า 28) (itds-211_comp_arch_Chapter05.pdf, หน้า 28)
- Alternative DMA configurations และ Intel 8237A · หน้า 29: ภาพสไลด์เรื่อง Alternative DMA configurations และ Intel 8237A สำหรับทบทวนหัวข้อ Alternative DMA configurations และ Intel 8237A (itds-211_comp_arch_Chapter05.pdf, หน้า 29) (itds-211_comp_arch_Chapter05.pdf, หน้า 29)
- Table 7.2 · หน้า 30: ตาราง Intel 8237A registers; status แถว D4–D7 มี Channel 0 request ซ้ำ: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter05.pdf, หน้า 30) (itds-211_comp_arch_Chapter05.pdf, หน้า 30)
- Direct Cache Access (DCA) · หน้า 31: ภาพสไลด์เรื่อง Direct Cache Access (DCA) สำหรับทบทวนหัวข้อ Direct Cache Access (DCA) และภาพ Xeon (itds-211_comp_arch_Chapter05.pdf, หน้า 31) (itds-211_comp_arch_Chapter05.pdf, หน้า 31)
- Xeon E5-2600/4600 Chip Architecture · หน้า 32: สถาปัตยกรรม Xeon E5-2600/4600 ตัวอย่าง cache และ I/O data path (itds-211_comp_arch_Chapter05.pdf, หน้า 32) (itds-211_comp_arch_Chapter05.pdf, หน้า 32)
- Cache-Related Performance Issues · หน้า 33: ภาพสไลด์เรื่อง Cache-Related Performance Issues สำหรับทบทวนหัวข้อ Packet traffic, buffers และ cache-related performance (itds-211_comp_arch_Chapter05.pdf, หน้า 33) (itds-211_comp_arch_Chapter05.pdf, หน้า 33)
- Cache-Related Performance Issues · หน้า 34: ภาพสไลด์เรื่อง Cache-Related Performance Issues สำหรับทบทวนหัวข้อ Packet traffic, buffers และ cache-related performance (itds-211_comp_arch_Chapter05.pdf, หน้า 34) (itds-211_comp_arch_Chapter05.pdf, หน้า 34)
- Packet Traffic Steps: · หน้า 35: ตารางขั้น incoming/outgoing packet traffic (itds-211_comp_arch_Chapter05.pdf, หน้า 35) (itds-211_comp_arch_Chapter05.pdf, หน้า 35)
- Direct Cache Access Strategies · หน้า 36: DCA prefetch hint เทียบกับ cache injection/Direct Data I/O (itds-211_comp_arch_Chapter05.pdf, หน้า 36) (itds-211_comp_arch_Chapter05.pdf, หน้า 36)
- Comparison of DMA and DDIO · หน้า 37: ผัง normal DMA กับ DDIO สำหรับ transfer to memory/cache และ to I/O (itds-211_comp_arch_Chapter05.pdf, หน้า 37) (itds-211_comp_arch_Chapter05.pdf, หน้า 37)
- Evolution of the I/O Function · หน้า 38: ภาพสไลด์เรื่อง Evolution of the I/O Function สำหรับทบทวนหัวข้อ วิวัฒนาการ I/O function และ I/O channel (itds-211_comp_arch_Chapter05.pdf, หน้า 38) (itds-211_comp_arch_Chapter05.pdf, หน้า 38)
- I/O Channel Architecture · หน้า 39: I/O channel architecture เปรียบ selector กับ multiplexor (itds-211_comp_arch_Chapter05.pdf, หน้า 39) (itds-211_comp_arch_Chapter05.pdf, หน้า 39)
- 1. Universal Serial Bus (USB) · หน้า 41: ภาพสไลด์เรื่อง 1. Universal Serial Bus (USB) สำหรับทบทวนหัวข้อ USB generations และ host-controller tree (itds-211_comp_arch_Chapter05.pdf, หน้า 41) (itds-211_comp_arch_Chapter05.pdf, หน้า 41)
- 2. FireWire Serial Bus (1999 - 2000) · หน้า 42: ภาพสไลด์เรื่อง 2. FireWire Serial Bus (1999 - 2000) สำหรับทบทวนหัวข้อ FireWire และ SCSI ในชุดตัวอย่าง (itds-211_comp_arch_Chapter05.pdf, หน้า 42) (itds-211_comp_arch_Chapter05.pdf, หน้า 42)
- 3. SCSI · หน้า 43: ภาพสไลด์เรื่อง 3. SCSI สำหรับทบทวนหัวข้อ FireWire และ SCSI ในชุดตัวอย่าง (itds-211_comp_arch_Chapter05.pdf, หน้า 43) (itds-211_comp_arch_Chapter05.pdf, หน้า 43)
- 4. Thunderbolt · หน้า 44: ภาพสไลด์เรื่อง 4. Thunderbolt สำหรับทบทวนหัวข้อ Thunderbolt และ InfiniBand (itds-211_comp_arch_Chapter05.pdf, หน้า 44) (itds-211_comp_arch_Chapter05.pdf, หน้า 44)
- 5. InfiniBand · หน้า 45: ภาพสไลด์เรื่อง 5. InfiniBand สำหรับทบทวนหัวข้อ Thunderbolt และ InfiniBand (itds-211_comp_arch_Chapter05.pdf, หน้า 45) (itds-211_comp_arch_Chapter05.pdf, หน้า 45)
- connecting peripherals of a · หน้า 46: ภาพ PCI Express และ SATA; ตัวเลข 6 Gbps กับ 300 Mbps ต่อ device ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter05.pdf, หน้า 46) (itds-211_comp_arch_Chapter05.pdf, หน้า 46)
- 8. Ethernet · หน้า 47: ภาพสไลด์เรื่อง 8. Ethernet สำหรับทบทวนหัวข้อ Ethernet และ Wi-Fi ในชุดตัวอย่าง (itds-211_comp_arch_Chapter05.pdf, หน้า 47) (itds-211_comp_arch_Chapter05.pdf, หน้า 47)
- 9. Wi-Fi · หน้า 48: ภาพสไลด์เรื่อง 9. Wi-Fi สำหรับทบทวนหัวข้อ Ethernet และ Wi-Fi ในชุดตัวอย่าง (itds-211_comp_arch_Chapter05.pdf, หน้า 48) (itds-211_comp_arch_Chapter05.pdf, หน้า 48)
- IBM EC12 I/O Channel Subsystem Structure · หน้า 49: IBM EC12 channel subsystems; จำนวน partitions ด้านบน/ล่างไม่ตรงกัน: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter05.pdf, หน้า 49) (itds-211_comp_arch_Chapter05.pdf, หน้า 49)
- Figure 7.20 · หน้า 50: ภาพตู้ IBM zEC12 I/O frames พร้อมป้าย PCIe drawer, I/O cage และ processor books (itds-211_comp_arch_Chapter05.pdf, หน้า 50) (itds-211_comp_arch_Chapter05.pdf, หน้า 50)
- IBM EC12 I/O System Structure · หน้า 51: ภาพ IBM EC12 books ผ่าน PCIe/InfiniBand ไปยัง I/O controllers (itds-211_comp_arch_Chapter05.pdf, หน้า 51) (itds-211_comp_arch_Chapter05.pdf, หน้า 51)
