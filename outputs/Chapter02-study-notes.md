# Chapter02 · Computer Systems, Computer Functions, Processor Structure and Function

ITDS-211 · Computer Architecture & Operating System · W.Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter02.pdf** จำนวน 46 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter02 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/วิเคราะห์/คำนวณ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 22 หัวข้อ · 🔴 ต้องจำแน่นอน 17 หัวข้อ (77.3%) · 🟡 สำคัญ 5 หัวข้อ (22.7%) · ⚪ อ่านเสริม 0 หัวข้อ (0.0%) · แบบฝึก 66 ข้อ · Flashcard 50 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter02 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| Von Neumann และ Harvard Computer Model | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 3–4 |
| Bus และเส้น Data / Control / Address | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 5–6 |
| การชิงสิทธิ์ Bus (Bus Arbitration) | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 7 |
| Hardware และ Software Approaches | 🟡 สำคัญ | itds-211_comp_arch_Chapter02.pdf, หน้า 8–9 |
| องค์ประกอบระดับบนและ MAR / MBR / I/OAR / I/OBR | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 10–11 |
| Basic Instruction Cycle และ Fetch | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 12–13 |
| ตัวอย่างเครื่องสมมติและการเดินโปรแกรม | 🟡 สำคัญ | itds-211_comp_arch_Chapter02.pdf, หน้า 14 |
| Instruction Cycle State Diagram | 🟡 สำคัญ | itds-211_comp_arch_Chapter02.pdf, หน้า 15 |
| MARIE: Register 7 ตัวและขนาด | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 17–18 |
| MARIE Architecture และ Data Path | 🟡 สำคัญ | itds-211_comp_arch_Chapter02.pdf, หน้า 18–20 |
| MARIE ISA และรูปแบบคำสั่ง | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 21–22 |
| การอ่าน Bit Pattern: LOAD และ SKIPCOND | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 23–24 |
| Microoperations และ RTL ของ LOAD / ADD | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 25–26 |
| RTL ของ SKIPCOND และเงื่อนไข AC | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 24, 27 |
| MARIE Fetch–Decode–Execute และ Operand | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 28–29 |
| Interrupt: เหตุเกิดและการเข้า ISR | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 30–32 |
| Maskable/Nonmaskable และ I/O ของ MARIE | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 33–34 |
| โปรแกรม MARIE 100–106 (hex) และ ADD 105 | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 35–36 |
| Classes of Interrupts 4 กลุ่ม | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 37 |
| Program Flow และ Instruction Cycle เมื่อมี Interrupt | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 38–40, 43 |
| Short และ Long I/O Wait กับ Interrupt | 🟡 สำคัญ | itds-211_comp_arch_Chapter02.pdf, หน้า 41–42 |
| Multiple Interrupts: Sequential และ Nested | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter02.pdf, หน้า 44–45 |

### บทนี้เรียนเพื่ออะไร

บทนี้เชื่อมภาพระบบคอมพิวเตอร์กับการทำงานทีละคำสั่ง: โมเดลและ bus พาข้อมูลไปยัง CPU/memory, MARIE ช่วยอ่าน register/ISA/RTL และส่วน interrupt อธิบายว่าระบบหยุดงานปัจจุบันไปบริการเหตุอื่นแล้วกลับมาทำต่ออย่างไร

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 3–15, 17–45

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- เปรียบเทียบ Von Neumann/Harvard และแยก bus lines กับวิธี arbitration (itds-211_comp_arch_Chapter02.pdf, หน้า 3–7)
- ติดตาม instruction cycle, PC/IR และข้อมูลผ่าน register ของระบบและ MARIE (itds-211_comp_arch_Chapter02.pdf, หน้า 10–20, 28–29)
- อ่าน MARIE ISA, bit pattern, RTL และ trace ADD 105 พร้อมแยกจุดขัดกันของเอกสาร (itds-211_comp_arch_Chapter02.pdf, หน้า 21–27, 35–36)
- อธิบายเหตุ/กลุ่ม interrupt, ISR, masking, I/O wait และ sequential/nested handling (itds-211_comp_arch_Chapter02.pdf, หน้า 30–34, 37–45)

วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ สไลด์ไม่มีรายการ Chapter Objectives แยกชัดเจน; เป้าหมายต่อไปนี้สรุปจากเนื้อหา

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- อ่านครบ 46 หน้า: หน้า 1 ปก หน้า 2 Course Outline หน้า 16 เปิดหัวข้อ Simple Computer Function และหน้า 46 Q & A ไม่มีเนื้อหาวิชาที่ต้องตั้งคำถามเพิ่ม
- ไม่พบรายการ Chapter Objectives แยกโดยตรง: ต้องตรวจสอบจากต้นฉบับ เป้าหมายข้างต้นเป็นสรุปจากเนื้อหา
- หน้า 21 เขียน MARIE มี 13 instructions แต่หน้า 22 แสดง 9 รายการเท่านั้น; รายชื่ออีก 4 รายการต้องตรวจสอบจากต้นฉบับ
- หน้า 24 ระบุ SKIPCOND field 10 เมื่อ AC > 0 แต่หน้า 27 RTL ให้ 11: ต้องตรวจสอบจากต้นฉบับ
- หน้า 35 binary Store 106 เริ่ม 0100 ขณะที่ hex เป็น 4106 และตารางหน้า 22 ให้ Store opcode 0010: ต้องตรวจสอบจากต้นฉบับ
- ภาพเครื่องสมมติหน้า 14 เป็นคนละ instruction table กับ MARIE หน้า 22; แยกรหัสสองชุดไว้ชัดเจน
- สไลด์หน้า 34 ไม่อธิบาย interrupt-driven I/O เชิงลึก และไม่มีข้อสอบเก่าหรือน้ำหนักสอบ จึงไม่อ้างว่าหัวข้อใดออกแน่นอน

## 2. สรุปรายบทและหัวข้อ

### 1. Von Neumann และ Harvard Computer Model

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 3–4**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

Von Neumann model ใช้ stored program โดย memory เก็บทั้งโปรแกรมและข้อมูล และอ้างตำแหน่งด้วย address มากกว่าชนิดของเนื้อหา; สไลด์ระบุการเข้าถึง/ทำงานแบบ sequential หรือ linear. Harvard model แยก memory และ bus สำหรับ instructions กับ data เพื่อลด bottleneck แต่เพิ่มความซับซ้อน. สไลด์ยกแนวทางผสมที่แยกแบบ Harvard ที่ L1 cache แต่ใช้แบบ Von Neumann ที่ main memory.

**ประเด็นที่ต้องจำ**

- Von Neumann: stored program; program/data อยู่ใน memory และระบุตำแหน่งด้วย address (หน้า 3)
- Harvard: instruction/data ใช้ memory และ bus แยกกัน (หน้า 4)
- Hybrid ในสไลด์: Harvard-style ที่ L1; Von Neumann ที่ main memory (หน้า 4)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- stored program = แนวคิดให้ memory เก็บ program และ data
- address = หมายเลขตำแหน่งใน memory
- instruction memory / data memory; L1 cache / main memory

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบแผนภาพหน้า 3–4 แล้วชี้ว่าทางเดินของ instructions กับ data แยกกันหรือใช้ร่วมกันในแต่ละโมเดล

| โมเดล | หน่วยความจำ/ทางเดิน | ข้อสังเกตตามสไลด์ |
| --- | --- | --- |
| Von Neumann | โปรแกรมกับข้อมูลอยู่ใน memory | stored program; sequential/linear |
| Harvard | instructions/data แยก memory และ bus | ลด bottleneck แต่ซับซ้อนขึ้น |
| Hybrid ตัวอย่าง | แยกที่ L1; รวมที่ main memory | ใช้สองแนวทางคนละระดับ |

**จุดที่อาจสับสน:** อย่าสรุปว่าเครื่องผสมต้องแยก main memory ด้วย; หน้า 4 ระบุ main memory เป็น Von Neumann ในตัวอย่าง

**ประโยคช่วยจำ:** Von Neumann เก็บร่วม; Harvard แยกทาง; Hybrid แยก L1 แต่รวม main memory

### 2. Bus และเส้น Data / Control / Address

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 5–6**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

สไลด์แบ่ง bus ที่พบบ่อยเป็น point-to-point กับ multipoint และระบุว่า bus มี data, control และ address lines. Data lines ส่ง bits ระหว่างอุปกรณ์; control lines กำหนดทิศทางการไหลและจังหวะที่อุปกรณ์ใช้ bus; address lines ระบุ source หรือ destination. Multipoint bus เป็นทรัพยากรที่ใช้ร่วมกัน จึงมี protocol ใน hardware เพื่อควบคุมการเข้าถึง.

**ประเด็นที่ต้องจำ**

- point-to-point และ multipoint เป็น bus สองแบบที่สไลด์กล่าวถึง
- data lines ส่ง bits; control lines คุมทิศทาง/สิทธิ์ใช้; address lines ระบุตำแหน่งต้นทาง/ปลายทาง
- multipoint เป็น shared resource และควบคุมการเข้าถึงด้วย hardware protocols

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Bus = ทางเชื่อมอุปกรณ์ที่ประกอบด้วย data/control/address lines ตามหน้า 5
- Multipoint bus = bus ที่หลายอุปกรณ์ใช้ร่วมกันตามหน้า 6

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ภาพหน้า 5 ชี้เส้น address, data, control ระหว่าง CPU, memory และ I/O แล้วดูภาพ multipoint หน้า 6

| Line | หน้าที่ |
| --- | --- |
| Data | ส่ง bits |
| Control | กำหนดทิศทางและเวลาเข้าถึง bus |
| Address | ระบุตำแหน่ง source/destination |

**จุดที่อาจสับสน:** address line บอกตำแหน่ง source/destination ไม่ได้ขน bits ของข้อมูลแทน data line

**ประโยคช่วยจำ:** Data ขนบิต; Control คุมใช้; Address บอกที่

### 3. การชิงสิทธิ์ Bus (Bus Arbitration)

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 7**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

เมื่อระบบ master-slave มีอุปกรณ์มากกว่าหนึ่งตัวที่เป็น bus master ได้ คำขอใช้ bus พร้อมกันต้องผ่าน arbitration. สไลด์ให้ 4 แบบ: distributed self-detection, distributed collision-detection, daisy chain และ centralized parallel. สองแบบแรกให้อุปกรณ์ตัดสินกันหรือทดลองใช้แล้วเริ่มใหม่เมื่อชนกัน; สองแบบหลังส่งสิทธิ์ตามลำดับความสำคัญหรือใช้วงจร arbitration กลาง.

**ประเด็นที่ต้องจำ**

- มี bus masters หลายตัวพร้อมขอใช้ bus → ต้อง arbitrate
- self-detection: devices ตัดสินกันเอง; collision-detection: ใครก็ลองใช้ ถ้าชนให้ลองใหม่
- daisy chain: ส่ง permission จาก priority สูงไปต่ำ; centralized parallel: ต่อเข้าวงจร arbitration โดยตรง

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- bus master = อุปกรณ์ที่ร้องขอ/ควบคุมการใช้ bus ในบริบทนี้
- arbitration = การตัดสินสิทธิ์เมื่อมีคำขอพร้อมกัน

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จับคู่ชื่อแต่ละกลุ่มกับวิธีตัดสินสิทธิ์ตาม bullet หน้า 7

**จุดที่อาจสับสน:** อย่าสลับ distributed self-detection กับ collision-detection; ชนกันแล้วลองใหม่เป็นแบบหลัง

**ประโยคช่วยจำ:** ตรวจเอง–ชนแล้วลองใหม่–ส่งสิทธิ์ต่อ–มีวงจรกลาง

### 4. Hardware และ Software Approaches

**🟡 สำคัญ** · itds-211_comp_arch_Chapter02.pdf, **หน้า 8–9**

เหตุผลการจัดระดับ: เป็นตัวอย่างหรือแผนภาพเปรียบเทียบที่ช่วยใช้แนวคิดหลัก

ภาพหน้า 8 เปรียบเทียบการจัดลำดับฟังก์ชัน arithmetic/logic ใน hardware กับการส่ง instruction codes ให้ instruction interpreter คุมวงจรทั่วไปใน software approach. สไลด์หน้า 9 นิยาม software เป็นลำดับ codes/instructions ที่ hardware ส่วนหนึ่งแปลและสร้าง control signals. โปรแกรมใหม่จึงให้ลำดับคำสั่งใหม่แทนการต่อวงจรใหม่ทุกครั้ง และแยกองค์ประกอบหลักเป็น CPU กับ I/O components.

**ประเด็นที่ต้องจำ**

- hardware approach ในภาพ: ลำดับฟังก์ชัน arithmetic/logic ทำใน hardware
- software approach: instruction codes → interpreter → control signals → general-purpose functions
- CPU มี instruction interpreter และ arithmetic/logic; I/O รับข้อมูล/คำสั่งและรายงานผล

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Software = sequence of codes/instructions ตามหน้า 9
- instruction interpreter และ control signals ตามภาพหน้า 8

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ลูกศรภาพหน้า 8 จาก instruction codes ผ่าน interpreter ไปยัง general-purpose functions

**จุดที่อาจสับสน:** สไลด์ไม่ได้ระบุว่า software ไม่ใช้ hardware; ระบุว่ามี hardware ส่วนหนึ่งตีความคำสั่ง

**ประโยคช่วยจำ:** เปลี่ยนโปรแกรมด้วย code; interpreter สร้างสัญญาณคุม

### 5. องค์ประกอบระดับบนและ MAR / MBR / I/OAR / I/OBR

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 10–11**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

หน้า 11 แสดง CPU, main memory และ I/O module เชื่อมด้วย system bus. หน้า 10 แจกหน้าที่ register สำหรับติดต่อ memory และ I/O: MAR ชี้ address ที่จะอ่าน/เขียน, MBR เก็บข้อมูลที่อ่านมาหรือจะเขียน, I/OAR ระบุอุปกรณ์ I/O และ I/OBR แลกข้อมูลระหว่าง I/O module กับ CPU. ชื่อ register บอกได้ว่าเก็บ address หรือ data/buffer ของฝ่ายใด.

**ประเด็นที่ต้องจำ**

- MAR = address ใน memory สำหรับ read/write; MBR = data เข้า/ออก memory
- I/OAR = อุปกรณ์ I/O ที่เลือก; I/OBR = data แลกระหว่าง I/O module กับ CPU
- ภาพ top-level: CPU, main memory, I/O module เชื่อมผ่าน system bus

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- MAR = Memory Address Register
- MBR = Memory Buffer Register
- I/OAR = I/O Address Register
- I/OBR = I/O Buffer Register

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านภาพหน้า 11 แล้ววางหน้าที่ register ทั้งสี่จากหน้า 10 ลงบนเส้นทาง CPU–Memory และ CPU–I/O

| Register | สิ่งที่เก็บ/ระบุ |
| --- | --- |
| MAR | memory address |
| MBR | data จาก/ไป memory |
| I/OAR | I/O device |
| I/OBR | data ระหว่าง I/O module กับ CPU |

**จุดที่อาจสับสน:** MAR/MBR เป็นคู่ memory ส่วน I/OAR/I/OBR เป็นคู่ I/O; อย่าสลับ address กับ buffer

**ประโยคช่วยจำ:** ตัว A ชี้ที่; ตัว B บรรทุกข้อมูล — คู่ memory และ I/O

### 6. Basic Instruction Cycle และ Fetch

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 12–13**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

วงจรคำสั่งพื้นฐานในหน้า 12 สลับ Fetch Cycle กับ Execute Cycle ไปจน HALT. ต้นแต่ละวงจร processor ดึง instruction จาก memory โดย PC ถือ address ของคำสั่งที่จะดึง; หลัง fetch จะเพิ่ม PC เพื่อชี้คำสั่งถัดไป. คำสั่งที่ดึงมาใส่ IR แล้ว processor ตีความและทำ action ที่ต้องการ.

**ประเด็นที่ต้องจำ**

- ภาพหน้า 12: Fetch Next Instruction → Execute Instruction → วนหรือ HALT
- PC ถือ address ของ instruction ที่จะ fetch ถัดไป และเพิ่มค่าหลัง fetch
- IR รับ fetched instruction ก่อน processor แปลและปฏิบัติ

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- PC = Program Counter
- IR = Instruction Register
- Fetch Cycle / Execute Cycle ตามหน้า 12–13

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เริ่มจาก PC ในหน้า 13 แล้วชี้เส้นทาง fetch → IR → interpret/perform action ก่อนกลับไป fetch ถัดไป

**จุดที่อาจสับสน:** การเพิ่ม PC หลัง fetch เป็นการเดินตามลำดับ; แผนภาพและคำสั่งควบคุมอาจเปลี่ยนทางเดินได้ในหัวข้ออื่น

**ประโยคช่วยจำ:** PC ชี้ที่; IR ถือคำสั่ง; Fetch แล้ว Execute

### 7. ตัวอย่างเครื่องสมมติและการเดินโปรแกรม

**🟡 สำคัญ** · itds-211_comp_arch_Chapter02.pdf, **หน้า 14**

เหตุผลการจัดระดับ: เป็นตัวอย่างหรือแผนภาพเปรียบเทียบที่ช่วยใช้แนวคิดหลัก

ภาพหน้า 14 ใช้เครื่องสมมติที่แบ่ง instruction format เป็น opcode กับ address และแสดง PC, IR, AC. คำสั่ง 0001 โหลด memory เข้า AC, 0101 บวก memory เข้า AC และ 0010 เก็บ AC กลับ memory. ลำดับภาพใช้ค่าที่ address 940 = 0003 และ 941 = 0002 จน AC เป็น 0005 แล้วเก็บที่ 941; นี่เป็นตัวอย่างเครื่องสมมติในหน้านี้ ไม่ใช่ opcode table ของ MARIE หน้า 22.

**ประเด็นที่ต้องจำ**

- instruction format ของเครื่องสมมติ: opcode bits 0–3 และ address bits 4–15
- PC = address of instruction; IR = instruction being executed; AC = temporary storage
- ตัวอย่าง 0003 + 0002 = 0005 แล้ว store ที่ address 941

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- AC = Accumulator
- Opcode = ส่วนรหัสการทำงาน; Address = ส่วนตำแหน่งตามภาพ
- 0001 Load, 0010 Store, 0101 Add — เฉพาะตัวอย่างหน้า 14

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ 6 ช่องในภาพหน้า 14: fetch 1940 → AC รับ 0003; fetch 5941 → AC เป็น 0005; fetch 2941 → memory 941 เป็น 0005

**จุดที่อาจสับสน:** รหัส Add/Store ในเครื่องสมมติหน้า 14 ต่างจากรหัส MARIE หน้า 22; อย่านำสองชุดมาปน

**ประโยคช่วยจำ:** Load 3 → Add 2 → Store 5 ในภาพเครื่องสมมติ

### 8. Instruction Cycle State Diagram

**🟡 สำคัญ** · itds-211_comp_arch_Chapter02.pdf, **หน้า 15**

เหตุผลการจัดระดับ: เป็นตัวอย่างหรือแผนภาพเปรียบเทียบที่ช่วยใช้แนวคิดหลัก

ภาพ state diagram ขยาย fetch/execute เป็น instruction address calculation, instruction fetch, instruction operation decoding, operand address calculation/fetch, data operation และ operand address calculation/store. เส้นทาง operand fetch อาจวนเมื่อมี multiple operands และ store อาจวนเมื่อมี multiple results. เมื่อคำสั่งเสร็จ จะกลับไปคำนวณ address เพื่อ fetch คำสั่งถัดไป.

**ประเด็นที่ต้องจำ**

- แกนภาพ: instruction fetch → decode → operand address/fetch → data operation → operand address/store
- มีทางวน multiple operands และ multiple results
- คำสั่งเสร็จแล้วกลับเส้น fetch next instruction

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Instruction Cycle State Diagram = ภาพสถานะละเอียดของ fetch/execute ตามหน้า 15
- Operand fetch / Operand store = สถานะดึง/เก็บ operand ตามภาพ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามลูกศรจาก instruction fetch ไป data operation แล้วตรวจเส้นย้อนสำหรับหลาย operands/results

**จุดที่อาจสับสน:** ภาพไม่ได้บอกว่าทุกคำสั่งต้องผ่านทุกสถานะ; เส้นทางขึ้นกับ operand และผลลัพธ์

**ประโยคช่วยจำ:** Fetch คำสั่ง → Decode → Operand → Operate → Store/วน

### 9. MARIE: Register 7 ตัวและขนาด

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 17–18**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

สไลด์แนะนำ MARIE ผ่าน register 7 ตัวและภาพ architecture. AC กับ MBR เป็น 16-bit; MAR กับ PC เป็น 12-bit; InREG กับ OutREG เป็น 8-bit; IR ถือ instruction ก่อน execute. หน้าที่หลักคือ AC เก็บ operand/เงื่อนไขตามสไลด์, MAR เก็บ address, MBR เก็บ data, PC ชี้คำสั่งถัดไป และ InREG/OutREG รับส่งข้อมูลอุปกรณ์.

**ประเด็นที่ต้องจำ**

- AC/MBR = 16-bit; MAR/PC = 12-bit; InREG/OutREG = 8-bit
- IR ถือ instruction ก่อน execute; สไลด์ไม่ได้ระบุความกว้าง IR เป็นตัวเลขในรายการหน้า 17
- AC, MAR, MBR, PC, IR, InREG, OutREG รวม 7 ตัว

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- AC = Accumulator
- MAR = Memory Address Register; MBR = Memory Buffer Register
- PC = Program Counter; IR = Instruction Register
- InREG / OutREG = input/output register

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้แผนภาพหน้า 18 วาง register บริเวณ CPU, ALU, I/O และ main memory แล้วทวนหน้าที่หน้า 17

| Register | ขนาดที่สไลด์ระบุ | หน้าที่หลัก |
| --- | --- | --- |
| AC | 16-bit | เก็บ operand/เงื่อนไขตามคำอธิบาย |
| MAR / PC | 12-bit | address ใน memory / address ของคำสั่งถัดไป |
| MBR | 16-bit | data จาก/ไป memory |
| InREG / OutREG | 8-bit | input / output |
| IR | ไม่ระบุตัวเลขในรายการ | instruction ก่อน execute |

**จุดที่อาจสับสน:** คำบรรยาย AC หน้า 17 ใช้คำ “conditional operator” ซึ่งอาจทำให้งง; ให้ยึดข้อความและภาพต้นฉบับ ไม่เติมความหมายที่ไม่มี

**ประโยคช่วยจำ:** 16: AC/MBR; 12: MAR/PC; 8: In/Out — IR ถือคำสั่ง

### 10. MARIE Architecture และ Data Path

**🟡 สำคัญ** · itds-211_comp_arch_Chapter02.pdf, **หน้า 18–20**

เหตุผลการจัดระดับ: เป็นตัวอย่างหรือแผนภาพเปรียบเทียบที่ช่วยใช้แนวคิดหลัก

ภาพ architecture แสดง register, ALU, control unit และ main memory ของ MARIE. Register เชื่อมกันและเชื่อม main memory ผ่าน common data bus โดยแต่ละอุปกรณ์บน bus มีหมายเลขเฉพาะซึ่งกำหนดบน control lines เมื่อจะให้ทำงาน. ยังมีทางเชื่อมแยกระหว่าง AC–MBR และ ALU–AC/MBR เพื่อถ่ายข้อมูลบางส่วนโดยไม่ใช้ main data bus; หน้า 20 วาด data path เชิงภาพ.

**ประเด็นที่ต้องจำ**

- register และ main memory เชื่อมผ่าน common data bus
- control lines ตั้ง unique number ของอุปกรณ์ที่จะทำงาน
- ทางเชื่อมแยก AC/MBR/ALU ช่วย transfer โดยไม่ใช้ main bus

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Data path = เส้นทางข้อมูลตามภาพหน้า 20
- common data bus / control lines ตามหน้า 19

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบ architecture หน้า 18 กับ data path หน้า 20 แล้วหาทาง main bus กับทางเชื่อมแยกของ ALU

**จุดที่อาจสับสน:** หมายเลขอุปกรณ์บน control lines ใช้ระบุ device ไม่ใช่ memory address จาก MAR โดยตรง

**ประโยคช่วยจำ:** บัสหลักเชื่อมทั้งหมด; ทางแยกช่วย AC–MBR–ALU

### 11. MARIE ISA และรูปแบบคำสั่ง

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 21–22**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

ISA กำหนดรูปแบบ instructions และ primitive operations ที่เครื่องทำได้ จึงเป็น interface ระหว่าง hardware กับ software. หน้า 21 กล่าวว่า MARIE มี 13 instructions ส่วนหน้า 22 แสดงรูปแบบ 16-bit แบ่ง opcode bits 15–12 กับ address bits 11–0 และตาราง fundamental instructions ที่มองเห็น 9 รายการ. ต้องตรวจสอบจากต้นฉบับหากต้องการรายชื่อครบ 13 เพราะสไลด์หน้านี้ให้รายการเพียง 9.

**ประเด็นที่ต้องจำ**

- ISA ระบุ instruction format และ primitive operations
- รูปแบบ MARIE: opcode 4 bits (15–12) + address 12 bits (11–0)
- ตารางหน้า 22: Load1, Store2, Add3, Subt4, Input5, Output6, Halt7, Skipcond8, Jump9

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- ISA = Instruction Set Architecture
- Opcode = bits 15–12; Address = bits 11–0 ในคำสั่ง 16-bit
- Load/Store/Add/Subt/Input/Output/Halt/Skipcond/Jump ตามตารางหน้า 22

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านตารางหน้า 22 จับคู่เลข hex 1–9 กับ mnemonic และผลของคำสั่งที่ตารางบอก

| Hex | Mnemonic | ผลตามตารางหน้า 22 |
| --- | --- | --- |
| 1 | Load X | AC ← memory[X] |
| 2 | Store X | memory[X] ← AC |
| 3 | Add X | บวก memory[X] เข้า AC |
| 4 | Subt X | ลบ memory[X] จาก AC |
| 5/6 | Input / Output | รับค่าเข้า AC / ส่งค่า AC ไป display |
| 7/8/9 | Halt / Skipcond / Jump X | หยุด / ข้ามตามเงื่อนไข / ใส่ X ใน PC |

**จุดที่อาจสับสน:** หน้า 21 เขียน 13 instructions แต่หน้า 22 มองเห็น 9 รายการ; รายการอีก 4 ตัวต้องตรวจสอบจากต้นฉบับ และห้ามแต่งเพิ่ม

**ประโยคช่วยจำ:** MARIE 16 บิต: 4 opcode + 12 address; ตารางที่เห็น 1–9

### 12. การอ่าน Bit Pattern: LOAD และ SKIPCOND

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 23–24**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

ตัวอย่าง LOAD ใน IR หน้า 23 มี opcode 1 และ address 3 จึงเป็นการโหลดข้อมูลจากตำแหน่ง 3. ตัวอย่าง SKIPCOND หน้า 24 มี opcode 8 และ bits 11–10 เป็น 10; คำบรรยายหน้านั้นบอกว่าข้ามคำสั่งถัดไปหาก AC > 0. ทว่า RTL หน้า 27 เขียนกรณี AC > 0 ด้วย bits 11–10 = 11 ซึ่งขัดกับหน้า 24; เงื่อนไขรหัสนี้ต้องตรวจสอบจากต้นฉบับ.

**ประเด็นที่ต้องจำ**

- LOAD: opcode 0001 / address 3 (หน้า 23)
- SKIPCOND: opcode 1000 / bits 11–10 = 10 และคำบรรยาย AC > 0 (หน้า 24)
- หน้า 27 ใช้ 11 สำหรับ AC > 0 จึงมีความไม่ตรงกัน

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- IR[15–12] = opcode; IR[11–0] = address/field ตามรูปคำสั่ง
- IR[11–10] = field เงื่อนไขในตัวอย่าง SKIPCOND

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านกลุ่ม 4 บิตแรกจากภาพหน้า 23–24 เป็น opcode แล้วดู 12 บิตถัดไป ก่อนเทียบคำบรรยายกับ RTL

**จุดที่อาจสับสน:** อย่าท่องว่า AC > 0 ต้องเป็น 10 หรือ 11 โดยไม่ระบุหน้าอ้างอิง: สไลด์สองหน้าขัดกัน ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** 4 บิตหน้าเป็น opcode; SKIPCOND มีจุดขัดกันหน้า 24/27

### 13. Microoperations และ RTL ของ LOAD / ADD

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 25–26**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

คำสั่งหนึ่งประกอบด้วย microoperations หลายขั้น และสไลด์ใช้ Register Transfer Language (RTL) ระบุลำดับการย้ายข้อมูล. M[X] คือค่าที่เก็บใน memory location X ส่วนลูกศร ← หมายถึงย้ายค่าไปยัง register หรือ memory location. LOAD X ทำ MAR ← X, MBR ← M[MAR], AC ← MBR; ADD X ใช้สองขั้นแรกเหมือนกัน แล้วทำ AC ← AC + MBR.

**ประเด็นที่ต้องจำ**

- microoperations = ขั้นย่อยในหนึ่ง instruction
- M[X] หมายถึงค่าจริงใน memory ที่ address X; ← คือการย้ายค่า
- LOAD และ ADD ต่างที่ขั้นสุดท้าย: AC ← MBR เทียบกับ AC ← AC + MBR

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RTL = Register Transfer Language
- M[X] = data at memory location X
- MAR, MBR, AC ตามหน้า 25–26

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เขียน LOAD/ADD 3 ขั้นจากสไลด์แล้วชี้ว่าต้องอ่าน memory ผ่าน MAR → MBR ก่อนปรับ AC

**สูตรที่ต้องรู้**

```text
LOAD X: MAR ← X → MBR ← M[MAR] → AC ← MBR
ADD X: MAR ← X → MBR ← M[MAR] → AC ← AC + MBR
```

ลำดับ microoperations ตามต้นฉบับ

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 26

**จุดที่อาจสับสน:** อย่าสลับ LOAD กับ ADD: LOAD แทน AC ด้วย MBR ส่วน ADD เก็บ AC เดิมมาบวก MBR

**ประโยคช่วยจำ:** MAR ชี้ที่ → MBR รับค่า → AC แทนหรือบวก

### 14. RTL ของ SKIPCOND และเงื่อนไข AC

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 24, 27**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

RTL หน้า 27 ให้ SKIPCOND เพิ่ม PC อีก 1 เมื่อเงื่อนไข AC ตรงกับ field ใน IR[11–10]: 00 กับ AC < 0, 01 กับ AC = 0 และ 11 กับ AC > 0. การเพิ่ม PC นี้คือการข้าม instruction ถัดไปในบริบทของคำสั่ง. แต่ภาพหน้า 24 เขียน field = 10 สำหรับ AC > 0; ต้องตรวจสอบจากต้นฉบับว่ารหัสใดถูกต้องก่อนใช้ตอบโจทย์.

**ประเด็นที่ต้องจำ**

- หน้า 27: 00 → AC < 0; 01 → AC = 0; 11 → AC > 0
- เมื่อเงื่อนไขจริง: PC ← PC + 1
- หน้า 24 ระบุ 10 → AC > 0 ซึ่งขัดกับ RTL หน้า 27

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SKIPCOND = skip next instruction on condition
- IR[11–10] = condition bits ในตัวอย่าง
- PC ← PC + 1 ตาม RTL หน้า 27

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบตารางเงื่อนไขที่สรุปจาก RTL หน้า 27 กับ bit pattern และคำบรรยายหน้า 24 ทีละรายการ

**สูตรที่ต้องรู้**

```text
if IR[11–10] = 00 and AC < 0: PC ← PC + 1
if IR[11–10] = 01 and AC = 0: PC ← PC + 1
if IR[11–10] = 11 and AC > 0: PC ← PC + 1
```

ถอด RTL หน้า 27 ตรงตามต้นฉบับ; กรณี AC > 0 ขัดกับคำบรรยายหน้า 24

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 27

| เงื่อนไข | รหัสที่ปรากฏ | สถานะ |
| --- | --- | --- |
| AC < 0 | 00 ใน RTL หน้า 27 | ตรงในหน้า 27 |
| AC = 0 | 01 ใน RTL หน้า 27 | ตรงในหน้า 27 |
| AC > 0 | 10 หน้า 24 / 11 หน้า 27 | ต้องตรวจสอบจากต้นฉบับ |

**จุดที่อาจสับสน:** รหัสกรณี AC > 0 ขัดกันในสไลด์เอง; ต้องตรวจสอบจากต้นฉบับ ไม่แก้ด้วยความรู้นอกเอกสาร

**ประโยคช่วยจำ:** 00 ติดลบ; 01 ศูนย์; กรณีบวกมีความขัดกัน 10/11

### 15. MARIE Fetch–Decode–Execute และ Operand

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 28–29**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

Instruction processing ดึง instruction จาก memory เข้า IR แล้ว decode เพื่อกำหนดงาน. ถ้าต้องใช้ operand จาก memory จะนำค่ามาไว้ใน MBR ก่อน execute. Flowchart หน้า 29 แสดง PC → MAR, M[MAR] → IR พร้อมเพิ่ม PC, แยก opcode/address ระหว่าง decode, แล้วจึงดึง operand หากจำเป็นและ execute.

**ประเด็นที่ต้องจำ**

- fetch: MAR ← PC; IR ← M[MAR]; PC เพิ่ม 1
- decode: แยกส่วน instruction และวาง IR[11–0] ใน MAR ตามภาพ
- operand ที่ต้องอ่าน: MBR ← M[MAR] แล้ว execute

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Fetch–Decode–Execute cycle = ชุดขั้นที่เครื่องทำเมื่อรันโปรแกรม
- IR[11–0] = address field ตามภาพหน้า 29

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ flowchart หน้า 29 สองทางหลังคำถาม “Instruction requires operand?” แล้วกลับไป fetch คำสั่งถัดไป

**จุดที่อาจสับสน:** อย่าคิดว่าทุก instruction ต้องอ่าน operand; ภาพมีทาง No ไป execute โดยตรง

**ประโยคช่วยจำ:** PC→MAR→IR; Decode; ถ้าต้องใช้จึง MBR; Execute

### 16. Interrupt: เหตุเกิดและการเข้า ISR

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 30–32**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

สไลด์ระบุว่าการ interrupt หยุด/แทรก fetch-decode-execute cycle ได้ เช่น user break, การร้องขอ I/O และ critical error; แบ่ง hardware กับ software interrupt โดย software อาจเรียก OS system call. เมื่อมี interrupt วงจรเพิ่มขั้นตรวจและประมวลผล. ภาพหน้า 32 ให้ลำดับตรวจสัญญาณ → save variables/registers → หา ISR address ใน interrupt vector table → ใส่ address ใน PC และ branch ไป ISR → ทำงาน → restore แล้วกลับไปวงจรหลัก.

**ประเด็นที่ต้องจำ**

- ตัวอย่างเหตุ: user break, I/O request, critical error
- ISR = Interrupt Service Routine; vector table ใช้หา ISR address
- ภาพ ISR ต้อง save/restore สถานะก่อนกลับไป fetch-decode-execute

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Hardware interrupt / Software interrupt ตามหน้า 30
- ISR = Interrupt Service Routine
- interrupt vector table ตามภาพหน้า 32

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ทวนภาพหน้า 31 เพิ่ม interrupt step แล้วไล่ภาพหน้า 32 จาก signal ไป ISR และกลับโปรแกรม

**จุดที่อาจสับสน:** เหตุ interrupt กับ class ของ interrupt ในหน้า 37 เป็นคนละรายการจัดหมวด; อย่าปนเป็นคำจำกัดความเดียว

**ประโยคช่วยจำ:** พบสัญญาณ → เก็บสถานะ → หา ISR → ทำงาน → คืนสถานะ

### 17. Maskable/Nonmaskable และ I/O ของ MARIE

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 33–34**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

ระบบทั่วไปมักปิด interrupts ระหว่างกำลังประมวลผล interrupt โดยตั้ง bit ใน flags register; interrupt ที่ถูกเพิกเฉยกรณีนี้เรียก maskable. Nonmaskable ต้องถูกประมวลผลเพื่อรักษาเสถียรภาพระบบ. หน้า 34 ระบุว่า MARIE ใช้ modified programmed I/O: output ไป OutREG และ CPU polls InREG จนมี input แล้วคัดลอกเข้า AC; รายละเอียด interrupt-driven I/O อยู่นอกขอบเขตสไลด์.

**ประเด็นที่ต้องจำ**

- maskable ถูก ignore ได้ในสถานการณ์ที่ disable interrupts
- nonmaskable ต้อง process เพื่อให้ระบบ stable
- MARIE: output → OutREG; CPU polls InREG → AC เมื่อรับ input

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- flags register bit ตามหน้า 33
- polling = CPU ตรวจ InREG ซ้ำตามคำอธิบายหน้า 34
- programmed I/O / interrupt-driven I/O เป็นชื่อแนวทางในหน้า 34

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จับคู่ข้อเปรียบเทียบหน้า 33 และตามทางข้อมูล OutREG/InREG ในหน้า 34

| ชนิด | ตามคำอธิบายหน้า 33 |
| --- | --- |
| Maskable | ถูกเพิกเฉยได้เมื่อ interrupts ถูกปิด |
| Nonmaskable | ต้องประมวลผลเพื่อความเสถียร |

**จุดที่อาจสับสน:** ไม่ขยายรายละเอียด interrupt-driven I/O เกินสไลด์ เพราะหน้า 34 ระบุว่าอยู่นอกขอบเขต

**ประโยคช่วยจำ:** Maskable อาจพัก; Nonmaskable ต้องทำ; MARIE polls InREG

### 18. โปรแกรม MARIE 100–106 (hex) และ ADD 105

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 35–36**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

ตารางหน้า 35 ให้โปรแกรมที่ address 100–103 เป็น Load 104, Add 105, Store 106, Halt และข้อมูลที่ 104 = 0023, 105 = FFE9, 106 = 0000 (hex). หน้า 36 ไล่คำสั่ง Add 105: เริ่ม PC 101, AC 0023; หลัง fetch/decode ได้ IR 3105, MAR 105, MBR FFE9 แล้ว execute ให้ AC 000C. อย่างไรก็ตาม binary contents ของ Store 106 ในหน้า 35 ขึ้นต้น 0100 ซึ่งไม่ตรงกับ hex 4106 และตาราง opcode Store = 0010 หน้า 22; ต้องตรวจสอบจากต้นฉบับ.

**ประเด็นที่ต้องจำ**

- program address 100–103: Load 104 / Add 105 / Store 106 / Halt
- ADD 105 trace: PC 101 → 102; IR 3105; MAR 105; MBR FFE9; AC 0023 → 000C
- Store 106 มีความขัดกัน: binary 0100..., hex 4106, opcode Store ในหน้า 22 = 0010

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RTN = หัวคอลัมน์ Register Transfer Notation ในตารางหน้า 36
- ค่าทุกตัวในตัวอย่างนี้เป็น hex ตามหน้า 35
- IR/PC/MAR/MBR/AC เป็นคอลัมน์ register ใน trace

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามตารางหน้า 36 ทีละแถว Fetch → Decode → Get operand → Execute และเทียบค่าก่อน/หลังของแต่ละ register

**Trace ADD 105 จากต้นฉบับ**

1. เริ่ม PC 101, IR 1104, MAR 104, MBR 0023, AC 0023
2. Fetch: MAR ← PC = 101; IR ← M[101] = 3105; PC ← 102
3. Decode: MAR ← IR[11–0] = 105
4. Get operand: MBR ← M[105] = FFE9
5. Execute: AC ← AC + MBR; ตารางให้ AC = 000C

**คำตอบ:** หลัง ADD 105: PC 102, IR 3105, MAR 105, MBR FFE9, AC 000C

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 35–36

**จุดที่อาจสับสน:** อย่าคัดลอกรหัส Store แบบ binary จากหน้า 35 เป็นกฎโดยไม่ระบุความขัดกันกับ hex/table; ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** 100 Load → 101 Add → 102 Store → 103 Halt; ADD จบ AC 000C

### 19. Classes of Interrupts 4 กลุ่ม

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 37**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

ตารางหน้า 37 แยก interrupt ตามแหล่ง/เหตุเป็น Program, Timer, I/O และ Hardware failure. Program เกิดจากเงื่อนไขระหว่าง execution เช่น overflow, division by zero, illegal instruction หรือ memory reference นอกพื้นที่ที่อนุญาต. Timer มาจาก timer ใน processor เพื่อให้งาน OS เกิดเป็นระยะ; I/O มาจาก controller เพื่อบอกการเสร็จงาน/ขอ service/แจ้ง error; Hardware failure เช่น power failure หรือ memory parity error.

**ประเด็นที่ต้องจำ**

- 4 classes: Program, Timer, I/O, Hardware failure
- Program: overflow/divide by zero/illegal instruction/memory out of allowed range
- Timer ให้ OS ทำหน้าที่เป็นระยะ; I/O controller แจ้ง completion/service/error
- Hardware failure เช่น power failure และ memory parity error

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Program interrupt / Timer interrupt / I/O interrupt / Hardware failure ตามตารางหน้า 37

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จัดตัวอย่างในตารางหน้า 37 ลงสี่กลุ่ม โดยใช้เกณฑ์แหล่งกำเนิดตามสไลด์

| Class | ที่มา/ตัวอย่าง |
| --- | --- |
| Program | เงื่อนไขจากการรันคำสั่ง เช่น divide by zero |
| Timer | timer ใน processor เพื่อให้ OS ทำงานเป็นระยะ |
| I/O | I/O controller แจ้งเสร็จงาน/ขอ service/error |
| Hardware failure | power failure หรือ memory parity error |

**จุดที่อาจสับสน:** I/O request ในหน้า 30 เป็นตัวอย่างเหตุ interrupt; หน้า 37 ให้รายละเอียด class I/O โดย controller

**ประโยคช่วยจำ:** โปรแกรมผิด–Timer นัด–I/O แจ้ง–Hardware เสีย

### 20. Program Flow และ Instruction Cycle เมื่อมี Interrupt

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 38–40, 43**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

ภาพหน้า 38 เปรียบเทียบการเดินโปรแกรมขณะมี I/O โดยไม่มี interrupt กับมี interrupt; แบบหลังเปลี่ยนไปทำ interrupt handler แล้วกลับงานผู้ใช้. หน้า 39 วาดการย้าย control จาก user program ไป interrupt handler และกลับไปจุดต่อ. หน้า 40 เพิ่ม interrupt cycle หลัง execute เมื่อเปิด interrupts; state diagram หน้า 43 เพิ่ม interrupt check และ interrupt ก่อนกลับไป fetch คำสั่งถัดไป.

**ประเด็นที่ต้องจำ**

- หน้า 38–39: handler รับ control ชั่วคราวแล้วกลับ user program
- หน้า 40: check for interrupts หลัง execute เมื่อ interrupts enabled; หาก disabled เดินต่อ
- หน้า 43: interrupt check ต่อจากการทำงานคำสั่ง ก่อน fetch รอบใหม่

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Interrupt handler = ชุดการทำงานที่รับ control ระหว่าง interrupt ตามภาพ
- Interrupt cycle / Interrupt check ตามภาพหน้า 40, 43

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** วาดเส้นลูกศร user program → handler → user program จากหน้า 39 แล้วใส่ตำแหน่ง check จากหน้า 40/43

**จุดที่อาจสับสน:** การกลับโปรแกรมไม่ได้แปลว่ารันเริ่มต้นใหม่; ภาพแสดงกลับจุดต่อของ user program

**ประโยคช่วยจำ:** Execute → ตรวจ interrupt → handler (ถ้ามี) → กลับไป fetch

### 21. Short และ Long I/O Wait กับ Interrupt

**🟡 สำคัญ** · itds-211_comp_arch_Chapter02.pdf, **หน้า 41–42**

เหตุผลการจัดระดับ: เป็นตัวอย่างหรือแผนภาพเปรียบเทียบที่ช่วยใช้แนวคิดหลัก

ภาพ timing หน้า 41 เทียบกรณี I/O wait สั้น: เมื่อไม่มี interrupt processor รอช่วง I/O; เมื่อมี interrupt processor ทำงานอื่นควบคู่ระหว่าง I/O แล้วรับการแจ้งกลับ. หน้า 42 กรณี wait ยาวแสดงว่าแม้มี interrupt ก็อาจใช้เวลาทำงานอื่นได้เพียงบางส่วน แล้ว processor ยังต้องรอจน I/O เสร็จ. จึงควรอ่านลำดับและช่อง waiting ในภาพ ไม่สรุปว่า interrupt ตัดการรอได้หมดเสมอ.

**ประเด็นที่ต้องจำ**

- สองภาพเปรียบเทียบ without interrupts กับ with interrupts
- short wait: ช่วง I/O อาจซ้อนกับ processor executing
- long wait: หลังงานอื่นหมด processor ยังรอ I/O ต่อได้

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- I/O wait = ช่วงรอ I/O ตามแกนเวลาในภาพหน้า 41–42
- concurrent with processor executing เป็นคำกำกับในภาพ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบช่องสีดำ processor waits และช่วง I/O operation ทั้งสองคอลัมน์ในหน้า 41 กับ 42

| กรณี | ผลที่ภาพ with interrupts แสดง |
| --- | --- |
| Short I/O wait | processor ทำงานอื่นซ้อนช่วง I/O |
| Long I/O wait | ซ้อนการทำงานได้บางช่วง แต่ยังมีช่วงรอ I/O |

**จุดที่อาจสับสน:** อย่าพูดว่า interrupts ทำให้ไม่ต้องรอ I/O ทุกกรณี; หน้า 42 แสดงการรอที่เหลือชัดเจน

**ประโยคช่วยจำ:** สั้นอาจซ้อนพอดี; ยาวยังเหลือช่วงรอ

### 22. Multiple Interrupts: Sequential และ Nested

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter02.pdf, **หน้า 44–45**

เหตุผลการจัดระดับ: เป็นนิยาม โครงสร้าง ขั้นตอน หรือภาษาสัญลักษณ์หลักที่สไลด์อธิบายโดยตรง

หน้า 44 เปรียบเทียบ sequential interrupt processing ซึ่ง handler หนึ่งเสร็จแล้วจึงไปอีก handler กับ nested processing ซึ่ง interrupt ใหม่แทรกกลาง handler ที่ทำอยู่แล้วค่อยกลับ. หน้า 45 ยกเวลาในภาพ: user program ถูก printer interrupt ที่ t=10; communication แทรกที่ t=15; กลับ printer ที่ t=25; disk แทรกที่ t=25; กลับ printer ที่ t=35; กลับ user program ที่ t=40. ลำดับนี้เป็นตัวอย่างเฉพาะภาพ ไม่ใช่กฎเวลา interrupt ทั่วไป.

**ประเด็นที่ต้องจำ**

- Sequential: ทำ handler ทีละตัว แล้วกลับลำดับตามภาพ
- Nested: handler ใหม่อาจแทรก handler ปัจจุบัน
- ตัวอย่างหน้า 45: printer → communication → printer → disk → printer → user program

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Sequential interrupt processing / Nested interrupt processing ตามหน้า 44
- Printer, Communication, Disk ISR เป็นชื่อในภาพหน้า 45

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้นิ้วตามลูกศรเวลา t=10,15,25,25,35,40 ในหน้า 45 แล้วจับคู่กับรูป nested หน้า 44

| รูปแบบ | การย้าย control |
| --- | --- |
| Sequential | handler หนึ่งจบก่อนจึงทำอีก handler |
| Nested | handler ใหม่แทรกกลาง handler ปัจจุบัน แล้วกลับมาทำต่อ |

**จุดที่อาจสับสน:** เวลา t ในหน้า 45 เป็นตัวอย่างจากภาพ; ไม่ใช่เวลามาตรฐานของระบบจริง และภาพไม่ได้กำหนดนโยบาย priority ทั่วไป

**ประโยคช่วยจำ:** Sequential ต่อคิว; Nested แทรกซ้อนแล้วกลับ

## 3. Roadmap ทบทวน

1. **ตั้งภาพระบบก่อน** — แยก Von Neumann/Harvard และเส้น bus ก่อนดู CPU (itds-211_comp_arch_Chapter02.pdf, หน้า 3–7)
2. **ตามคำสั่งเข้า CPU** — ดู top-level, PC/IR, fetch/execute และ state diagram (itds-211_comp_arch_Chapter02.pdf, หน้า 8–15)
3. **วาง register ของ MARIE** — จำขนาด/หน้าที่ แล้วอ่าน architecture และ data path (itds-211_comp_arch_Chapter02.pdf, หน้า 17–20)
4. **อ่านคำสั่งเป็น microoperations** — ISA/bit pattern → RTL LOAD/ADD/SKIPCOND → fetch/decode/execute (itds-211_comp_arch_Chapter02.pdf, หน้า 21–29)
5. **ฝึก trace ต้นฉบับ** — ไล่ Load/Add/Store/Halt และตาราง ADD 105 โดยตรวจจุดขัดกัน (itds-211_comp_arch_Chapter02.pdf, หน้า 35–36)
6. **ต่อด้วย Interrupt** — เหตุและ ISR → class/masking → timing → sequential/nested (itds-211_comp_arch_Chapter02.pdf, หน้า 30–34, 37–45)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · โมเดลและ Bus

อ่านหน้า 3–11 พร้อมชี้แผนภาพและจับคู่หน้าที่เส้น/การชิง bus

**เกณฑ์ผ่าน:** ตอบความต่าง Von Neumann/Harvard และ bus 3 เส้น/4 arbitration ได้

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 3–11

### รอบ 2 · Instruction Cycle

ไล่ PC→IR→execute และภาพเครื่องสมมติ โดยแยก ISA ออกจาก MARIE

**เกณฑ์ผ่าน:** อธิบาย fetch/execute และค่าตัวอย่าง AC 0005 ได้

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 12–15

### รอบ 3 · MARIE

ท่อง register และอ่าน ISA/bit fields/RTL จากภาพ

**เกณฑ์ผ่าน:** เขียน LOAD/ADD RTL ได้และชี้ความขัดกัน SKIPCOND ได้

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 17–29

### รอบ 4 · Trace

ทำตาราง ADD 105 โดยปิดเฉลยก่อน แล้วเทียบ register ทีละแถว

**เกณฑ์ผ่าน:** ได้ AC 000C และอธิบาย PC/IR/MAR/MBR ตลอด trace ได้

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 35–36

### รอบ 5 · Interrupt

ฝึกแยกเหตุ/class, ISR, masking, timing และ nested ด้วยภาพ

**เกณฑ์ผ่าน:** ไล่เส้นทาง interrupt และแยก long wait กับ short wait ได้

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 30–34, 37–45

### รอบ 6 · ทดสอบรวม

สุ่มคำถามทุกหัวข้อ ทำ Flashcard แล้วกลับไปดูภาพ/หน้าที่ตอบผิด

**เกณฑ์ผ่าน:** ตอบแบบฝึกครบและทวนสองจุดที่ต้องตรวจสอบจากต้นฉบับ

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 3–45

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1 โมเดล/Bus/วงจรคำสั่ง หน้า 3–15; วัน 2 MARIE register/ISA/RTL/trace หน้า 17–29, 35–36; วัน 3 interrupt หน้า 30–34, 37–45 และทำแบบฝึก/ทวนจุดผิด
- **ถ้าเหลือ 1 วัน:** เริ่ม MARIE register→ISA→RTL→trace หน้า 17–29, 35–36; ต่อ ISR/class/masking/nested หน้า 30–34, 37, 44–45; ปิดท้ายโมเดล/Bus หน้า 3–7 และ timing หน้า 41–42
- **ถ้าเหลือ 3 ชั่วโมง:** 0–25 นาที โมเดล/Bus หน้า 3–7; 25–55 นาที PC/IR/MARIE registers หน้า 10–20; 55–110 นาที ISA/RTL/trace หน้า 21–29, 35–36; 110–155 นาที ISR/class/timing/nested หน้า 30–34, 37–45; 155–180 นาทีสุ่มคำถามและทวนจุดผิด

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

ให้เวลากับ register, ISA/RTL, trace และ interrupt ก่อน เพราะสไลด์ให้ขั้นตอน/ภาพ/ตารางละเอียด เป็นการประเมินเพื่อจัดเวลาอ่าน ไม่ใช่การทำนายข้อสอบจริง

- **ควรท่องจำ:** ชื่อ/หน้าที่ MAR, MBR, PC, IR, MARIE 7 registers, bus lines/arbitration, opcode ที่ตารางแสดง, class interrupt (หน้า 5–7, 10, 17, 22, 37)
- **ควรเข้าใจแนวคิด:** ทางเดิน instruction/operand, ISR save–branch–restore, short/long wait และ sequential/nested (หน้า 12–15, 28–34, 38–45)
- **ควรฝึกแก้โจทย์:** อ่าน bit fields/RTL และ trace ADD 105 ตามต้นฉบับ ระบุ PC/IR/MAR/MBR/AC ทีละขั้น; แยกจุดขัดกันก่อนใช้รหัส (หน้า 21–27, 35–36)
- **เตรียมข้อสอบแบบผสม:** เลือกตอบจับคู่คำศัพท์/rules; อัตนัยอธิบายขั้น; วิเคราะห์ภาพและเปรียบเทียบ; คำนวณ/trace เฉพาะตัวอย่างที่อยู่ในสไลด์ ไม่อ้างว่าเป็นข้อสอบจริง

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 22 ข้อ, อัตนัย 20 ข้อ, วิเคราะห์ 22 ข้อ, คำนวณ 2 ข้อ

### Von Neumann และ Harvard Computer Model

**ข้อ 1 · เลือกตอบ: โมเดลใดแยก memory และ bus สำหรับ instructions กับ data?**

- A. Harvard
- B. Von Neumann
- C. MARIE RTL
- D. Daisy chain

เฉลย: Harvard model ตามหน้า 4

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 4

**ข้อ 2 · อัตนัย: stored program ในหน้า 3 หมายถึงอะไร?**

เฉลย: Memory เก็บทั้ง program และ data และเข้าถึงด้วยตำแหน่ง address

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 3

**ข้อ 3 · วิเคราะห์: Hybrid ที่สไลด์ยกตัวอย่างใช้สองโมเดลที่ระดับใด?**

เฉลย: Harvard-style ที่ L1 cache และ Von Neumann ที่ main memory

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 4

### Bus และเส้น Data / Control / Address

**ข้อ 4 · เลือกตอบ: เส้นใดระบุตำแหน่ง source หรือ destination?**

- A. Address lines
- B. Data lines
- C. Clock period
- D. IR

เฉลย: Address lines กำหนดตำแหน่งตามหน้า 5

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 5

**ข้อ 5 · อัตนัย: Control lines มีหน้าที่อะไรตามหน้า 5?**

เฉลย: กำหนดทิศทางข้อมูลและเวลาที่แต่ละอุปกรณ์เข้าถึง bus

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 5

**ข้อ 6 · วิเคราะห์: ทำไม multipoint bus จึงต้องมี protocol?**

เฉลย: เพราะหลายอุปกรณ์ใช้ทรัพยากรเดียวกัน ต้องควบคุมการเข้าถึงผ่าน protocol ใน hardware

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 6

### การชิงสิทธิ์ Bus (Bus Arbitration)

**ข้อ 7 · เลือกตอบ: แบบใดให้แต่ละอุปกรณ์ต่อเข้าวงจร arbitration โดยตรง?**

- A. Centralized parallel
- B. Daisy chain
- C. Collision-detection
- D. Self-detection

เฉลย: Centralized parallel ตามหน้า 7

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 7

**ข้อ 8 · อัตนัย: Daisy chain ส่งสิทธิ์อย่างไร?**

เฉลย: จากอุปกรณ์ priority สูงสุดลงไปยังต่ำสุด

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 7

**ข้อ 9 · วิเคราะห์: Distributed self-detection ต่างจาก collision-detection อย่างไร?**

เฉลย: แบบแรกอุปกรณ์ตัดสินกันว่าใครได้ bus; แบบหลังอุปกรณ์ลองใช้ได้และลองใหม่หากข้อมูลชนกัน

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 7

### Hardware และ Software Approaches

**ข้อ 10 · เลือกตอบ: Software approach ในภาพหน้า 8 ส่งสิ่งใดเข้า instruction interpreter?**

- A. Instruction codes
- B. Memory address only
- C. Interrupt vector only
- D. Bus priority

เฉลย: Instruction codes ตามภาพ

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 8

**ข้อ 11 · อัตนัย: สไลด์นิยาม software ว่าอย่างไร?**

เฉลย: ลำดับ codes หรือ instructions ที่ hardware ส่วนหนึ่งตีความแล้วสร้าง control signals

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 9

**ข้อ 12 · วิเคราะห์: เหตุใดหน้า 9 จึงกล่าวว่าไม่ต้อง rewiring hardware ทุกโปรแกรม?**

เฉลย: เพราะเปลี่ยนเป็นลำดับคำสั่งใหม่ที่ interpreter ตีความและควบคุมฟังก์ชันทั่วไป

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 9

### องค์ประกอบระดับบนและ MAR / MBR / I/OAR / I/OBR

**ข้อ 13 · เลือกตอบ: Register ใดเก็บข้อมูลที่จะเขียนลง memory หรืออ่านขึ้นมา?**

- A. MBR
- B. MAR
- C. I/OAR
- D. PC

เฉลย: MBR เป็น buffer ของข้อมูล memory

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 10

**ข้อ 14 · อัตนัย: I/OAR ต่างจาก I/OBR อย่างไร?**

เฉลย: I/OAR ระบุอุปกรณ์ I/O; I/OBR ใช้แลกข้อมูลระหว่าง I/O module และ CPU

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 10

**ข้อ 15 · วิเคราะห์: ภาพ top-level มีองค์ประกอบใดเชื่อมผ่าน system bus?**

เฉลย: CPU, main memory และ I/O module

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 11

### Basic Instruction Cycle และ Fetch

**ข้อ 16 · เลือกตอบ: PC ถืออะไรที่ต้น instruction cycle?**

- A. Address ของ instruction ที่จะ fetch ถัดไป
- B. ข้อมูลที่เพิ่ง output
- C. ผล arithmetic ล่าสุด
- D. หมายเลข I/O device

เฉลย: PC ถือ address ของคำสั่งถัดไปตามหน้า 13

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 13

**ข้อ 17 · อัตนัย: หลัง fetch processor ทำอะไรกับ PC และ IR?**

เฉลย: เพิ่ม PC และนำ fetched instruction ไปไว้ใน IR

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 13

**ข้อ 18 · วิเคราะห์: ภาพ Basic Instruction Cycle แสดงการวนระหว่างขั้นใด?**

เฉลย: Fetch Next Instruction และ Execute Instruction จน HALT

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 12

### ตัวอย่างเครื่องสมมติและการเดินโปรแกรม

**ข้อ 19 · เลือกตอบ: ในเครื่องสมมติหน้า 14 รหัส 0101 ทำอะไร?**

- A. Add to AC from Memory
- B. Load AC from Memory
- C. Store AC to Memory
- D. Halt

เฉลย: 0101 เป็น Add ตาม partial opcode list

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 14

**ข้อ 20 · คำนวณ: เมื่อโหลด 0003 แล้วบวก 0002 ค่า AC ในภาพเป็นเท่าไร?**

เฉลย: 0003 + 0002 = 0005 ตาม Step 4

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 14

**ข้อ 21 · วิเคราะห์: ทำไมไม่ควรใช้รหัส 0101 นี้แทน Add ของ MARIE?**

เฉลย: เป็นคนละเครื่อง/ตารางรหัส: หน้า 14 เป็น hypothetical machine ส่วนหน้า 22 เป็น MARIE ISA

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 14, 22

### Instruction Cycle State Diagram

**ข้อ 22 · เลือกตอบ: เส้นทางใดในภาพรองรับ multiple operands?**

- A. วงกลับระหว่าง operand address calculation กับ operand fetch
- B. กลับจาก HALT ไป START
- C. ข้าม instruction fetch
- D. ไป I/OAR

เฉลย: ภาพวนที่ operand fetch สำหรับ multiple operands

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 15

**ข้อ 23 · อัตนัย: หลัง instruction operation decoding ภาพไปยังกลุ่มสถานะใด?**

เฉลย: operand address calculation และต่อไป operand fetch/data operation

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 15

**ข้อ 24 · วิเคราะห์: ทำไมจึงไม่ควรจำว่าทุกคำสั่งต้องผ่าน operand fetch และ store?**

เฉลย: ภาพมีหลายเส้นทางตามลักษณะ operand/result ไม่ได้บังคับผ่านทุกสถานะ

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 15

### MARIE: Register 7 ตัวและขนาด

**ข้อ 25 · เลือกตอบ: คู่ใดเป็น 12-bit ตามหน้า 17?**

- A. MAR และ PC
- B. AC และ MBR
- C. InREG และ OutREG
- D. IR และ ALU

เฉลย: MAR และ PC ระบุ 12-bit

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 17

**ข้อ 26 · อัตนัย: MBR ทำหน้าที่อะไรใน MARIE?**

เฉลย: เก็บข้อมูลหลังดึงจาก memory หรือก่อนวางลง memory

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 17

**ข้อ 27 · วิเคราะห์: InREG กับ OutREG ต่างกันอย่างไร?**

เฉลย: InREG ถือข้อมูลที่อ่านจาก input device; OutREG ถือข้อมูลที่พร้อมสำหรับ output device

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 17

### MARIE Architecture และ Data Path

**ข้อ 28 · เลือกตอบ: ข้อใดถ่ายข้อมูลโดยไม่ใช้ main data bus ได้ตามหน้า 19?**

- A. ทางเชื่อมแยก AC–MBR และ ALU–AC/MBR
- B. เฉพาะ main memory
- C. เฉพาะ OutREG ไป keyboard
- D. ทุกอุปกรณ์โดยไม่ต้องมี bus

เฉลย: หน้า 19 ระบุ separate connections

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 19

**ข้อ 29 · อัตนัย: MARIE เชื่อม registers กับ main memory ด้วยอะไร?**

เฉลย: common data bus

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 19

**ข้อ 30 · วิเคราะห์: หมายเลขเฉพาะของอุปกรณ์ใช้ตรงไหนเมื่อจะให้ทำงาน?**

เฉลย: ตั้งบน control lines ตามหน้า 19

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 19

### MARIE ISA และรูปแบบคำสั่ง

**ข้อ 31 · เลือกตอบ: ใน MARIE instruction bits 15–12 ใช้ทำอะไร?**

- A. Opcode
- B. Memory buffer
- C. Input data
- D. Interrupt priority

เฉลย: ภาพหน้า 22 กำหนด bits 15–12 เป็น opcode

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 22

**ข้อ 32 · อัตนัย: ISA เป็น interface ระหว่างสิ่งใด?**

เฉลย: hardware และ software

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 21

**ข้อ 33 · วิเคราะห์: เหตุใดรายชื่อ 13 คำสั่งของ MARIE ยังต้องตรวจสอบจากต้นฉบับ?**

เฉลย: หน้า 21 บอกว่ามี 13 แต่ตารางหน้า 22 แสดงเพียง 9 รายการ จึงไม่มีรายชื่อครบในสไลด์ที่เห็น

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 21–22

### การอ่าน Bit Pattern: LOAD และ SKIPCOND

**ข้อ 34 · เลือกตอบ: ภาพ LOAD หน้า 23 ระบุ address ใด?**

- A. 3
- B. 8
- C. 10
- D. 11

เฉลย: ภาพและคำบรรยายระบุ address 3

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 23

**ข้อ 35 · อัตนัย: หน้า 24 ระบุ bits 11–10 ของ SKIPCOND และเงื่อนไขอย่างไร?**

เฉลย: ระบุ 10 และบอกว่าจะข้ามคำสั่งถัดไปเมื่อ AC > 0

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 24

**ข้อ 36 · วิเคราะห์: เหตุใดรหัสเงื่อนไข AC > 0 ต้องตรวจสอบ?**

เฉลย: หน้า 24 เขียน 10 แต่ RTL หน้า 27 เขียน 11 สำหรับ AC > 0

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 24, 27

### Microoperations และ RTL ของ LOAD / ADD

**ข้อ 37 · เลือกตอบ: ขั้นสุดท้ายของ ADD X คือข้อใด?**

- A. AC ← AC + MBR
- B. AC ← MBR
- C. MAR ← PC
- D. PC ← PC + 1

เฉลย: RTL ของ ADD หน้า 26 จบด้วย AC ← AC + MBR

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 26

**ข้อ 38 · อัตนัย: M[X] ใน MARIE RTL หมายถึงอะไร?**

เฉลย: ค่าข้อมูลจริงที่เก็บใน memory location X

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 25

**ข้อ 39 · วิเคราะห์: LOAD X และ ADD X ต่างกันที่ microoperation สุดท้ายอย่างไร?**

เฉลย: LOAD: AC ← MBR; ADD: AC ← AC + MBR

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 26

### RTL ของ SKIPCOND และเงื่อนไข AC

**ข้อ 40 · เลือกตอบ: RTL หน้า 27 ระบุ field ใดเมื่อ AC = 0?**

- A. 01
- B. 00
- C. 10
- D. 11

เฉลย: หน้า 27 ให้ IR[11–10] = 01 แล้วทดสอบ AC = 0

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 27

**ข้อ 41 · อัตนัย: SKIPCOND ทำอะไรกับ PC เมื่อเงื่อนไขเป็นจริง?**

เฉลย: PC ← PC + 1 เพื่อข้ามคำสั่งถัดไป

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 27

**ข้อ 42 · วิเคราะห์: หน้า 24 กับ 27 ต่างกันตรงไหนในกรณี AC > 0?**

เฉลย: หน้า 24 เขียน bits 11–10 = 10; หน้า 27 เขียน = 11 ต้องตรวจสอบจากต้นฉบับ

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 24, 27

### MARIE Fetch–Decode–Execute และ Operand

**ข้อ 43 · เลือกตอบ: หาก instruction ต้องใช้ operand จาก memory ค่าจะไป register ใดก่อน execute?**

- A. MBR
- B. OutREG
- C. I/OAR
- D. flags register

เฉลย: หน้า 28–29 ให้นำ operand เข้า MBR

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 28–29

**ข้อ 44 · อัตนัย: ขั้น fetch ตาม flowchart หน้า 29 ใช้ PC และ MAR อย่างไร?**

เฉลย: คัดลอก PC ไป MAR แล้วคัดลอก memory ณ MAR ไป IR และเพิ่ม PC

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 29

**ข้อ 45 · วิเคราะห์: เมื่อ instruction ไม่ต้องใช้ operand flowchart ไปทางใด?**

เฉลย: ข้ามการนำค่าเข้า MBR แล้วไป Execute the instruction

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 29

### Interrupt: เหตุเกิดและการเข้า ISR

**ข้อ 46 · เลือกตอบ: ISR ย่อมาจากอะไรตามหน้า 32?**

- A. Interrupt Service Routine
- B. Instruction State Register
- C. Input Signal Router
- D. Interrupt System Rate

เฉลย: คำขยายอยู่หน้า 32

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 32

**ข้อ 47 · อัตนัย: ยก 2 เหตุ interrupt จากหน้า 30**

เฉลย: เช่น user break และ I/O request; critical error ก็เป็นอีกเหตุหนึ่ง

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 30

**ข้อ 48 · วิเคราะห์: ทำไมต้อง save แล้ว restore variables/registers ตามภาพหน้า 32?**

เฉลย: ภาพกำหนดให้เก็บสถานะก่อน branch ไป ISR และคืนก่อนกลับสู่วงจร fetch-decode-execute

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 32

### Maskable/Nonmaskable และ I/O ของ MARIE

**ข้อ 49 · เลือกตอบ: MARIE รับ input อย่างไรตามหน้า 34?**

- A. CPU polls InREG แล้วคัดลอกค่าเข้า AC
- B. interrupt-driven I/O ที่สไลด์ลงรายละเอียด
- C. อ่าน OutREG เข้า PC
- D. อ่าน address จาก IR โดยตรง

เฉลย: หน้า 34 ระบุ CPU polls InREG

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 34

**ข้อ 50 · อัตนัย: Maskable กับ nonmaskable ต่างกันอย่างไร?**

เฉลย: แบบแรกถูก ignore ได้เมื่อ disable interrupts; แบบหลังต้อง process เพื่อรักษาระบบให้ stable

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 33

**ข้อ 51 · วิเคราะห์: ทำไมไม่ควรอธิบายขั้น interrupt-driven I/O ละเอียดจากสไลด์นี้?**

เฉลย: หน้า 34 บอกว่าอยู่นอกขอบเขต discussion และให้เพียง MARIE modified programmed I/O

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 34

### โปรแกรม MARIE 100–106 (hex) และ ADD 105

**ข้อ 52 · เลือกตอบ: ADD 105 ในตารางหน้า 36 อ่าน operand จาก address ใด?**

- A. 105
- B. 100
- C. 102
- D. 106

เฉลย: แถว Get operand ชี้ address 105

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 36

**ข้อ 53 · คำนวณ: ตามตาราง ADD 105 ให้ AC 0023 บวก MBR FFE9 แล้ว AC เป็นค่าใด?**

เฉลย: AC เป็น 000C ตามแถว Execute ในตารางหน้า 36

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 36

**ข้อ 54 · วิเคราะห์: Store 106 มีจุดใดที่ต้องตรวจสอบ?**

เฉลย: binary ขึ้นต้น 0100 แต่ hex เป็น 4106 และตาราง opcode หน้า 22 ให้ Store = 0010; สไลด์ไม่ตรงกัน

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 22, 35

### Classes of Interrupts 4 กลุ่ม

**ข้อ 55 · เลือกตอบ: Division by zero อยู่ใน class ใดตามตาราง?**

- A. Program
- B. Timer
- C. I/O
- D. Hardware failure

เฉลย: เป็นตัวอย่าง Program interrupt

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 37

**ข้อ 56 · อัตนัย: Timer interrupt มีประโยชน์ตามตารางอย่างไร?**

เฉลย: ทำให้ OS ปฏิบัติบางหน้าที่เป็นระยะ

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 37

**ข้อ 57 · วิเคราะห์: I/O กับ Hardware failure ต่างกันตามแหล่งกำเนิดอย่างไร?**

เฉลย: I/O มาจาก I/O controller; Hardware failure มาจากความล้มเหลว เช่นไฟดับหรือ memory parity error

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 37

### Program Flow และ Instruction Cycle เมื่อมี Interrupt

**ข้อ 58 · เลือกตอบ: ภาพ Instruction Cycle with Interrupts วาง Check for Interrupts หลังขั้นใด?**

- A. Execute Instruction
- B. START
- C. Fetch Next Instruction ก่อนเริ่ม
- D. HALT

เฉลย: หน้า 40 วาง check หลัง execute

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 40

**ข้อ 59 · อัตนัย: หน้า 39 แสดง transfer of control ระหว่างอะไร?**

เฉลย: user program กับ interrupt handler แล้วกลับ user program

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 39

**ข้อ 60 · วิเคราะห์: หน้า 43 เพิ่มสถานะใดจาก state diagram แบบไม่มี interrupt?**

เฉลย: Interrupt check และ Interrupt ก่อนวนกลับไป fetch next instruction

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 15, 43

### Short และ Long I/O Wait กับ Interrupt

**ข้อ 61 · เลือกตอบ: ภาพ Long I/O wait เมื่อมี interrupt แสดงผลใด?**

- A. processor ทำงานอื่นแล้วอาจยังรอ
- B. processor ไม่ต้องรอแน่นอน
- C. I/O หยุดทำงานทันที
- D. ไม่มีการกลับเข้าโปรแกรม

เฉลย: หน้า 42 แสดงช่วง processor waits หลัง concurrent work

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 42

**ข้อ 62 · อัตนัย: หน้า 41 เปรียบเทียบ timing สองแบบใด?**

เฉลย: without interrupts กับ with interrupts ในกรณี short I/O wait

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 41

**ข้อ 63 · วิเคราะห์: ทำไมจึงสรุปไม่ได้ว่า interrupt ลบเวลารอ I/O ทั้งหมด?**

เฉลย: หน้า 42 กรณี long I/O wait ยังแสดง processor waits หลังจากทำงานอื่นช่วงหนึ่ง

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 42

### Multiple Interrupts: Sequential และ Nested

**ข้อ 64 · เลือกตอบ: รูปแบบใดให้ interrupt Y แทรกระหว่าง handler X?**

- A. Nested
- B. Sequential
- C. Point-to-point bus
- D. Stored program

เฉลย: ภาพ (b) หน้า 44 เป็น nested interrupt processing

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 44

**ข้อ 65 · อัตนัย: หน้า 45 ลำดับ handler หลัง printer เริ่มที่ t=10 เป็นอย่างไร?**

เฉลย: communication แทรกที่ t=15; กลับ printer t=25; disk แทรก t=25; กลับ printer t=35; user program t=40

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 45

**ข้อ 66 · วิเคราะห์: Sequential กับ nested ต่างกันอย่างไรตามภาพหน้า 44?**

เฉลย: Sequential ทำ handler ทีละตัว; nested อนุญาตให้ handler ใหม่แทรก handler ที่กำลังทำ

อ้างอิง: itds-211_comp_arch_Chapter02.pdf, หน้า 44

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- Von Neumann model: ภาพ CPU, memory และการเก็บโปรแกรม/ข้อมูลร่วมกัน (itds-211_comp_arch_Chapter02.pdf, หน้า 3)
- Harvard model: ภาพแยก instruction memory กับ data memory (itds-211_comp_arch_Chapter02.pdf, หน้า 4)
- เส้นของ Bus: ภาพ CPU–Memory–I/O พร้อม Address/Data/Control bus (itds-211_comp_arch_Chapter02.pdf, หน้า 5)
- Multipoint bus: อุปกรณ์หลายตัวใช้ bus เดียวร่วมกัน (itds-211_comp_arch_Chapter02.pdf, หน้า 6)
- Bus arbitration 4 แบบ: รายชื่อ self-detection, collision-detection, daisy chain และ centralized parallel (itds-211_comp_arch_Chapter02.pdf, หน้า 7)
- Hardware/Software approaches: แผนภาพ sequence ใน hardware เทียบ instruction interpreter (itds-211_comp_arch_Chapter02.pdf, หน้า 8)
- MAR/MBR/I/OAR/I/OBR: ภาพหน้าที่ register ฝั่ง memory และ I/O (itds-211_comp_arch_Chapter02.pdf, หน้า 10)
- Computer components: CPU, main memory และ I/O module ผ่าน system bus (itds-211_comp_arch_Chapter02.pdf, หน้า 11)
- Basic instruction cycle: Fetch/Execute วนจน HALT (itds-211_comp_arch_Chapter02.pdf, หน้า 12)
- เครื่องสมมติ: Load–Add–Store: ภาพ 6 ขั้น 0003 + 0002 = 0005; เป็นคนละ ISA กับ MARIE (itds-211_comp_arch_Chapter02.pdf, หน้า 14)
- Instruction cycle state diagram: สถานะ fetch, decode, operand, operation, store (itds-211_comp_arch_Chapter02.pdf, หน้า 15)
- MARIE architecture: แผนผัง register, ALU, CPU และ main memory (itds-211_comp_arch_Chapter02.pdf, หน้า 18)
- MARIE data path: ภาพการเชื่อม register และ bus (itds-211_comp_arch_Chapter02.pdf, หน้า 20)
- MARIE instruction format: ภาพ opcode/address และตาราง 9 คำสั่งที่เห็น (itds-211_comp_arch_Chapter02.pdf, หน้า 22)
- LOAD bit pattern: Opcode 1 และ address 3 ใน IR (itds-211_comp_arch_Chapter02.pdf, หน้า 23)
- SKIPCOND bit pattern: หน้า 24 บอก field 10 เมื่อ AC > 0; ขัดกับหน้า 27 (itds-211_comp_arch_Chapter02.pdf, หน้า 24)
- RTL ของ LOAD และ ADD: ลำดับ MAR, MBR, AC ที่สไลด์ระบุ (itds-211_comp_arch_Chapter02.pdf, หน้า 26)
- RTL ของ SKIPCOND: หน้า 27 บอก field 11 เมื่อ AC > 0; ขัดกับหน้า 24 (itds-211_comp_arch_Chapter02.pdf, หน้า 27)
- MARIE fetch–decode–execute: Flowchart แบบมี/ไม่มี operand (itds-211_comp_arch_Chapter02.pdf, หน้า 29)
- Interrupt เพิ่มในวงจร: แผนภาพการตรวจและ process interrupt (itds-211_comp_arch_Chapter02.pdf, หน้า 31)
- ขั้นตอนเข้า ISR: save state, vector table, branch, restore (itds-211_comp_arch_Chapter02.pdf, หน้า 32)
- Maskable/Nonmaskable: คำอธิบายการปิด interrupts และประเภทที่ยังต้องทำ (itds-211_comp_arch_Chapter02.pdf, หน้า 33)
- โปรแกรม MARIE 100–106: ตาราง mnemonic/binary/hex; Store 106 มีจุดขัดกัน (itds-211_comp_arch_Chapter02.pdf, หน้า 35)
- Trace ADD 105: ค่าของ PC/IR/MAR/MBR/AC ทีละขั้น (itds-211_comp_arch_Chapter02.pdf, หน้า 36)
- Classes of interrupts: ตาราง Program/Timer/I/O/Hardware failure (itds-211_comp_arch_Chapter02.pdf, หน้า 37)
- Program flow กับ interrupt: แผนภาพ without/with interrupt (itds-211_comp_arch_Chapter02.pdf, หน้า 38)
- Instruction cycle with interrupts: เพิ่มการตรวจ interrupt หลัง execute (itds-211_comp_arch_Chapter02.pdf, หน้า 40)
- Short I/O wait: timing เปรียบเทียบกรณีมี/ไม่มี interrupt (itds-211_comp_arch_Chapter02.pdf, หน้า 41)
- Long I/O wait: timing แสดงช่วง processor waits ที่ยังเหลือ (itds-211_comp_arch_Chapter02.pdf, หน้า 42)
- State diagram with interrupt: เพิ่ม interrupt check และ interrupt (itds-211_comp_arch_Chapter02.pdf, หน้า 43)
- Sequential/Nested interrupts: เส้นทาง control ของ handler X/Y (itds-211_comp_arch_Chapter02.pdf, หน้า 44)
- ตัวอย่างเวลา multiple interrupts: Printer/Communication/Disk ISR ที่ t=10–40 (itds-211_comp_arch_Chapter02.pdf, หน้า 45)
