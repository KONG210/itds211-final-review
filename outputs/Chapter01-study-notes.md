# Chapter01 · Basic Computer Components & Introduction to Computer Architecture

ITDS-211 · Computer Architecture & Operating System · W.Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter01.pdf** จำนวน 43 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter01 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/วิเคราะห์/คำนวณ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 19 หัวข้อ · 🔴 ต้องจำแน่นอน 14 หัวข้อ (73.7%) · 🟡 สำคัญ 4 หัวข้อ (21.1%) · ⚪ อ่านเสริม 1 หัวข้อ (5.3%) · แบบฝึก 57 ข้อ · Flashcard 52 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter01 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| Architecture, Organization และขอบเขตการออกแบบ | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 3–4 |
| Classes of Computers, Embedded Systems และ ARM | 🟡 สำคัญ | itds-211_comp_arch_Chapter01.pdf, หน้า 5, 28–31 |
| Cloud Computing และ SaaS / PaaS / IaaS | 🟡 สำคัญ | itds-211_comp_arch_Chapter01.pdf, หน้า 6–8 |
| ปัจจัยที่กำหนด Performance และ Eight Great Ideas | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 9–10 |
| Below Your Program และ Levels of Program Code | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 11–12 |
| ส่วนประกอบคอมพิวเตอร์และโครงสร้างภายใน CPU | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 13–14 |
| Machine Cycle และ Registers ใน CPU | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 15–16 |
| Cache Memory และระดับ L1 / L2 / L3 | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 17–18 |
| Multi-core, Multi-thread และการมอง Motherboard → Core | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 19–23 |
| Manufacturing ICs, Yield และตัวอย่าง Wafer | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter01.pdf, หน้า 24–25 |
| อ่านกราฟ Single Processor Performance | 🟡 สำคัญ | itds-211_comp_arch_Chapter01.pdf, หน้า 26 |
| RISC vs CISC Architecture | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 27 |
| Application Parallelism กับ Architectural Parallelism | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 32 |
| Flynn’s Taxonomy: SISD / SIMD / MISD / MIMD | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 33 |
| System Level Architecture Patterns | 🟡 สำคัญ | itds-211_comp_arch_Chapter01.pdf, หน้า 34 |
| Performance และ Relative Performance | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 35–36 |
| Elapsed Time, CPU Time และ Clock | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 37–38 |
| CPU Time และโจทย์ออกแบบ Clock Rate | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 39–40 |
| Instruction Count, CPI และการเปรียบเทียบ CPU | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter01.pdf, หน้า 41–42 |

### บทนี้เรียนเพื่ออะไร

บทนี้ปูความเข้าใจว่าสถาปัตยกรรมและการจัดระบบคอมพิวเตอร์ต่างกันอย่างไร โปรแกรมเชื่อมกับ software/hardware ชั้นใด และองค์ประกอบ CPU ทำงานร่วมกันอย่างไร จากนั้นใช้การจำแนก parallelism และสมการเวลา/จำนวนคำสั่ง/CPI เพื่ออธิบายและเปรียบเทียบสมรรถนะจากโจทย์ในสไลด์

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 3–4, 11–21, 32–42

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- แยก Architecture/WHAT กับ Organization/HOW และอธิบายขอบเขตการออกแบบที่กว้างกว่า ISA (itds-211_comp_arch_Chapter01.pdf, หน้า 3–4)
- เชื่อมระดับโปรแกรมกับ system software/hardware พร้อมอธิบายองค์ประกอบ CPU และ Machine Cycle (itds-211_comp_arch_Chapter01.pdf, หน้า 11–16)
- แยก cache levels, Multi-core/Multi-thread, parallelism และ Flynn’s Taxonomy ตามเกณฑ์ในสไลด์ (itds-211_comp_arch_Chapter01.pdf, หน้า 17–23, 32–33)
- เข้าใจบริบท Cloud, Embedded/ARM และรูปแบบระบบที่สไลด์ยกตัวอย่าง (itds-211_comp_arch_Chapter01.pdf, หน้า 5–8, 28–31, 34)
- คำนวณ Relative Performance, CPU Time และโจทย์ CPI โดยคุมสมการ หน่วย และสมมติฐานให้ตรงตัวอย่าง (itds-211_comp_arch_Chapter01.pdf, หน้า 36–42)

วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ สไลด์ไม่ได้แยกรายการ Chapter Objectives; เป้าหมายต่อไปนี้สรุปจากเนื้อหาของบท

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- อ่านครบ 43 หน้า: หน้า 1 เป็นปก หน้า 2 เป็น Course Outline หน้า 35 เปิดส่วน Performance และหน้า 43 เป็น Q & A; ไม่มีเนื้อหาสำหรับออกคำถามใหม่ในหน้าปิดบท
- ไม่พบรายการ Chapter Objectives ที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ เป้าหมายบนเว็บเป็นการสรุปจากเนื้อหาพร้อมเลขหน้า
- หน้า 16 ให้ชื่อ PC/IR/Status register แต่ไม่ให้รายละเอียดการอัปเดต register หรือความหมาย flags; หน้า 10 เอ่ย Moore’s Law โดยไม่ให้นิยาม: ต้องตรวจสอบจากต้นฉบับ
- หน้า 27 พิมพ์ mPM = Microprocessor Mode และมี CW โดยไม่อธิบายครบ คำขยาย/ความหมายเหล่านี้ต้องตรวจสอบจากต้นฉบับ ไม่แก้ด้วยข้อมูลจากภายนอก
- ภาพบอร์ด Apple A5 และ Cortex-M3 มีป้ายย่อยที่เล็กหรือพร่า สรุปเฉพาะข้อความที่ตรวจได้และให้เปิดภาพต้นฉบับประกอบ; จุดที่อ่านไม่ชัดต้องตรวจสอบจากต้นฉบับ
- กราฟหน้า 26 ครอบคลุม 1978–2018; ตัวอย่างเทคโนโลยี/คำอ้างความแพร่หลายของ ARM และ MISD เป็นข้อความในสไลด์ ไม่ใช่การตรวจสอบสถานะปัจจุบัน
- การเปรียบเทียบ IaaS/PaaS/SaaS ยึดขอบเขต Client/CSP ตามแผนภาพหน้า 8 โดยเฉพาะ ไม่แทนด้วยตารางจากแหล่งอื่น
- ยังไม่มีข้อมูลยืนยันขอบเขต Final หรือน้ำหนักข้อสอบ แบ่งสีเพื่อจัดเวลาอ่านตามนิยาม หลักการ และสูตรในเอกสารเท่านั้น

## 2. สรุปรายบทและหัวข้อ

### 1. Architecture, Organization และขอบเขตการออกแบบ

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 3–4**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Architecture คือคุณลักษณะที่โปรแกรมเมอร์มองเห็นและมีผลต่อการทำงานเชิงตรรกะของโปรแกรม ส่วน Organization คือหน่วยทำงานและการเชื่อมต่อที่ทำให้ข้อกำหนดนั้นเกิดขึ้นจริง สไลด์ย่อความต่างเป็น WHAT กับ HOW มุมมอง “Old” เน้น ISA design ขณะที่ “Real” computer architecture รวม ISA, microarchitecture และ hardware เพื่อเพิ่ม performance ภายใต้ cost, power และ availability

**ประเด็นที่ต้องจำ**

- Architecture: instruction set, addressing modes, data types — มุมของผู้ใช้/โปรแกรมเมอร์ (หน้า 3)
- Organization: วงจร, cache, pipeline, bus width, clock speed — การทำให้ข้อกำหนดเกิดขึ้นจริง (หน้า 3)
- การตัดสินใจ ISA ในหน้า 4: registers, memory addressing, addressing modes, instruction operands, available operations, control flow instructions, instruction encoding
- การออกแบบต้องตอบ specific requirements ของ target machine และพิจารณา cost, power, availability

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Architecture = คุณลักษณะที่โปรแกรมเมอร์เห็นและกระทบ logical execution
- Organization = operational units และ interconnections ที่ realise architectural specifications
- ISA = Instruction Set Architecture ตามหน้า 4; WHAT/HOW เป็นคำช่วยแยกมุมมองในหน้า 3

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตัวอย่างจากหน้า 3: addressing modes อยู่ฝั่ง Architecture ส่วน bus width/clock speed อยู่ฝั่ง Organization ใช้เกณฑ์สิ่งที่โปรแกรมเมอร์เห็นเทียบกับวิธีสร้างระบบจริง

| มุมมอง | สิ่งที่พิจารณา | ตัวอย่าง |
| --- | --- | --- |
| Architecture / WHAT | คุณลักษณะที่โปรแกรมเมอร์เห็น | instruction set, addressing modes, data types |
| Organization / HOW | หน่วยทำงานและการเชื่อมต่อจริง | cache, pipeline, bus width, clock speed |

**จุดที่อาจสับสน:** หน้า 4 ขยายขอบเขต “Real” computer architecture ให้กว้างกว่า ISA จึงควรแยกนิยามเปรียบเทียบ WHAT/HOW หน้า 3 ออกจากขอบเขตการออกแบบรวมหน้า 4

**ประโยคช่วยจำ:** Architecture บอก WHAT; Organization ทำ HOW — คำช่วยจำตรงจากหน้า 3

### 2. Classes of Computers, Embedded Systems และ ARM

**🟡 สำคัญ** · itds-211_comp_arch_Chapter01.pdf, **หน้า 5, 28–31**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือบริบทช่วยประยุกต์แนวคิดหลัก

Supercomputers ใช้การคำนวณวิทยาศาสตร์และวิศวกรรมระดับสูง มีความสามารถสูงแต่เป็นสัดส่วนเล็กของตลาดตามสไลด์ ส่วน Embedded Computers เป็นส่วนหนึ่งของระบบอื่นและมีข้อจำกัด power/performance/cost ที่เข้มงวด Embedded Systems ใช้อิเล็กทรอนิกส์และซอฟต์แวร์ในผลิตภัณฑ์ เชื่อมกับสภาพแวดล้อมและอาจมี real-time constraints สไลด์ใช้ ARM และ Cortex-M3 เป็นตัวอย่าง โดยระบุ low power และการจัดการ interrupt ที่รวดเร็ว/กำหนดพฤติกรรมได้แน่นอน

**ประเด็นที่ต้องจำ**

- Supercomputers: high-end scientific/engineering calculations; Embedded Computers: hidden as components of systems (หน้า 5)
- Embedded Systems อยู่ในอุปกรณ์ขนาดใหญ่กว่าและมักผูกกับสิ่งแวดล้อม; หลายกิจกรรมพร้อมกันทำให้ real-time constraints ซับซ้อนขึ้น (หน้า 28)
- ARM ในหน้า 29 พัฒนาจากแนวคิด RISC; สไลด์ระบุ small die size และ low power requirements
- หน้า 30 แสดง Cortex-A/Cortex-A50, Cortex-R และ Cortex-M; กลุ่ม M ที่แสดงคือ M0, M0+, M3, M4
- หน้า 31: Cortex-M series มี fast, highly deterministic interrupt management และ low power; Cortex-M3 ระบุ 16/32-bit applications พร้อม debug/trace

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Embedded system: การใช้อิเล็กทรอนิกส์และซอฟต์แวร์ภายในผลิตภัณฑ์ (หน้า 28)
- ARM: สไลด์ให้ชื่อ Acorn RISC Machine / Advanced RISC Machine (หน้า 29)
- Cortex-M3: ตัวอย่าง microcontroller chip ตามหัวข้อหน้า 31

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ Cortex-M3 เป็นตัวอย่างที่เอกสารให้ ไม่เปลี่ยนรายการ ARM Products หน้า 30 ให้เป็นการจัดอันดับประสิทธิภาพ เพราะสไลด์ไม่ได้ระบุเช่นนั้น

| ประเภท | จุดเน้นตามสไลด์ |
| --- | --- |
| Supercomputers | การคำนวณวิทยาศาสตร์/วิศวกรรมระดับสูง |
| Embedded Computers | เป็นส่วนของระบบอื่นและมีข้อจำกัด power/performance/cost |

**จุดที่อาจสับสน:** ข้ออ้างเรื่องจำนวนผลิตหรือความแพร่หลายในสไลด์เป็นบริบทของเอกสาร ไม่ใช่ข้อมูลตลาดปัจจุบัน และชื่อ Cortex แต่ละกลุ่มยังไม่ได้มีรายละเอียดเปรียบเทียบครบทุกด้าน

**ประโยคช่วยจำ:** Embedded = อยู่ในผลิตภัณฑ์ และต้องคิดเรื่องพลังงาน–สมรรถนะ–ต้นทุนตามข้อจำกัด

### 3. Cloud Computing และ SaaS / PaaS / IaaS

**🟡 สำคัญ** · itds-211_comp_arch_Chapter01.pdf, **หน้า 6–8**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือบริบทช่วยประยุกต์แนวคิดหลัก

Cloud Computing เป็นโมเดลการเข้าถึงกลุ่มทรัพยากรคอมพิวเตอร์ที่ปรับตั้งได้ร่วมกันผ่านเครือข่ายอย่างสะดวกและตามต้องการ Cloud networking คือเครือข่ายและหน้าที่จัดการเครือข่ายที่ทำให้ cloud ทำงาน ส่วน Cloud Storage ตามหน้า 6 เน้น database storage และ database applications ที่อยู่บน cloud servers ระยะไกล หน้า 7 แยก SaaS, PaaS, IaaS และหน้า 8 เปรียบเทียบชั้นที่ client/CSP ดูแลพร้อม trade-off ด้านความซับซ้อน ค่าใช้จ่ายเริ่มต้น scalability และ customization

**ประเด็นที่ต้องจำ**

- SaaS: ให้ application software ที่ทำงานและเข้าถึงได้ใน cloud
- PaaS: ให้ platform ที่ application ของลูกค้าสามารถรันได้
- IaaS: ให้ virtual machines และ abstracted hardware/operating systems โดยอาจควบคุมผ่าน service API
- แผนภาพหน้า 8 ไล่ Traditional IT → IaaS → PaaS → SaaS; ฝั่ง SaaS แสดง CSP ดูแลทุกชั้น
- ตามลูกศรเปรียบเทียบในหน้า 8: ไปทาง SaaS มีความซับซ้อน/ต้นทุนล่วงหน้าลดลง และ scalable มากขึ้น แต่ customizable ลดลง

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SaaS = Software as a Service; PaaS = Platform as a Service; IaaS = Infrastructure as a Service
- API = application programming interface ตามหน้า 7; CSP = cloud service provider ตามหน้า 8
- Cloud Storage ในชุดนี้ให้ความหมายเฉพาะตามข้อความหน้า 6 ไม่ขยายตัวอย่างนอกเอกสาร

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านหน้า 7 ว่าให้บริการ “อะไร” ก่อน แล้วดูภาพหน้า 8 ว่า client/CSP ดูแลชั้นใด แผนภาพ IaaS ในต้นฉบับจัด Operating system อยู่ฝั่ง CSP จึงอ้างขอบเขตนี้ว่าเป็น “ตามแผนภาพหน้า 8”

| โมเดล | บริการตามหน้า 7 |
| --- | --- |
| SaaS | application software บน cloud |
| PaaS | platform ให้ application ลูกค้ารัน |
| IaaS | virtual machines และ abstracted hardware/OS; อาจควบคุมผ่าน API |

**จุดที่อาจสับสน:** อย่าสลับ software ที่พร้อมใช้กับ platform สำหรับรัน application และอย่านำการแบ่งความรับผิดชอบจากแหล่งอื่นมาแทนภาพในสไลด์

**ประโยคช่วยจำ:** S = Software, P = Platform, I = Infrastructure — เทียบสิ่งที่ลูกค้าได้รับ

### 4. ปัจจัยที่กำหนด Performance และ Eight Great Ideas

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 9–10**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Performance ของโปรแกรมไม่ได้ขึ้นกับ processor เพียงส่วนเดียว เพราะ algorithm กำหนดจำนวน operations ขณะที่ภาษา compiler และ architecture กำหนดจำนวน machine instructions ต่อ operation Processor/memory system กำหนดความเร็วของคำสั่ง และ I/O system รวม OS กำหนดความเร็วของงาน I/O หน้า 10 เสนอ Eight Great Ideas เป็นชุดแนวคิดออกแบบ แต่ไม่ได้อธิบายกลไกของทุกแนวคิดอย่างละเอียด

**ประเด็นที่ต้องจำ**

- Algorithm → จำนวน operations ที่ถูกทำ
- Programming language, compiler, architecture → machine instructions ต่อ operation
- Processor และ memory system → ความเร็วที่ instructions ถูกทำ; I/O system (รวม OS) → ความเร็ว I/O operations
- Design for Moore’s Law
- Use abstraction to simplify design
- Make the common case fast
- Performance via parallelism
- Performance via pipelining
- Performance via prediction
- Hierarchy of memories
- Dependability via redundancy

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- abstraction, common case, parallelism, pipelining, prediction, hierarchy, redundancy เป็นชื่อแนวคิดตามหน้า 10
- Moore’s Law ถูกเอ่ยชื่อในหน้า 10 แต่ไม่มีคำนิยามหรือช่วงเวลาการเพิ่มจำนวนทรานซิสเตอร์: ต้องตรวจสอบจากต้นฉบับ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** วิธีไล่เหตุผลจากหน้า 9: เมื่อ compiler เปลี่ยน ให้ดูผลต่อจำนวน machine instructions ต่อ operation ก่อน ห้ามสรุปว่า clock rate เปลี่ยนด้วยโดยไม่มีข้อมูล

**จุดที่อาจสับสน:** อย่าสรุปว่าตัวเลข clock สูงหมายถึงโปรแกรมเร็วขึ้นเสมอ และอย่าเติมนิยาม/เงื่อนไขของ Moore’s Law ที่หน้า 10 ไม่ได้ให้

**ประโยคช่วยจำ:** ไล่จากงาน → คำสั่ง → การประมวลผล → I/O; ส่วน 8 Ideas ให้จำเป็นรายการตามสไลด์

### 5. Below Your Program และ Levels of Program Code

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 11–12**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Application software เขียนด้วย high-level language และอาศัย system software กับ hardware ที่อยู่ข้างใต้ Compiler แปล HLL ไปเป็น machine code ขณะที่ OS ให้บริการ I/O การจัดการ memory/storage และการจัดตารางงาน/ใช้ทรัพยากรร่วม หน้า 12 แสดงตัวอย่างเส้นทาง High-level C → Compiler → Assembly RISC-V → Assembler → Binary machine language โดย assembly เป็นข้อความแทนคำสั่ง ส่วน hardware representation ใช้ bits แทน instructions/data

**ประเด็นที่ต้องจำ**

- Application software / System software / Hardware เป็นสามชั้นในภาพหน้า 11
- System software: Compiler และ Operating System
- OS: handling input/output; managing memory/storage; scheduling tasks/sharing resources
- Hardware: processor, memory, I/O controllers
- High-level language ใกล้ problem domain ช่วย productivity/portability; Assembly เป็น textual representation of instructions; hardware representation เป็น binary digits

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Compiler: แปล HLL code ไป machine code ตามหน้า 11
- Assembler: ขั้นแปลง Assembly ไป Binary ในภาพหน้า 12
- bits = binary digits; HLL = high-level language ตามบริบทหน้า 11–12

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตัวอย่าง swap ในหน้า 12 ถูกแสดงใน C, Assembly สำหรับ RISC-V และ Binary ตามลำดับ ใช้อธิบายระดับการแทนโปรแกรม ไม่ต้องแต่งความหมายของแต่ละ instruction ที่สไลด์ไม่ได้สอน

**จุดที่อาจสับสน:** Compiler และ Assembler เป็นคนละขั้นในภาพ และ Assembly ที่เป็นข้อความไม่ใช่ Binary bits โดยตรง

**ประโยคช่วยจำ:** C → Compiler → Assembly → Assembler → Binary — ตามภาพหน้า 12

### 6. ส่วนประกอบคอมพิวเตอร์และโครงสร้างภายใน CPU

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 13–14**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

คอมพิวเตอร์ในหน้า 13 มี Input Devices, CPU, Memory (RAM), Storage Devices, Motherboard, Output Devices, Power Supply Unit และ GPU ภายใน CPU หน้า 14 แยก Control Unit, ALU, Registers และ CPU interconnection โดยให้หน้าที่ควบคุม ประมวลผล เก็บข้อมูลภายใน และสื่อสารระหว่างส่วนเหล่านั้นตามลำดับ

**ประเด็นที่ต้องจำ**

- จำส่วนประกอบทั้ง 8 กลุ่มตามหน้า 13
- Control Unit: controls the operation of the CPU
- ALU: performs the computer’s data processing function
- Registers: provide storage internal to CPU
- CPU interconnection: communication among Control Unit, ALU และ registers

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- CPU = Central Processing Unit; GPU = Graphics Processing Unit
- ALU = Arithmetic and Logic Unit
- Memory ในรายการหน้า 13 ระบุ RAM ส่วน Storage Devices เป็นอีกรายการหนึ่ง

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ภาพหน้า 13 แยกสิ่งที่เป็น processor, memory, input/output ก่อน แล้วขยายเฉพาะ processor ด้วยรายการภายใน CPU หน้า 14

**จุดที่อาจสับสน:** Registers เป็นที่เก็บภายใน CPU ตามนิยามหน้า 14 จึงไม่ควรแทนคำนี้ด้วย Memory (RAM) ซึ่งถูกแยกในหน้า 13

**ประโยคช่วยจำ:** CPU: ควบคุม–ประมวลผล–เก็บภายใน–เชื่อมต่อ

### 7. Machine Cycle และ Registers ใน CPU

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 15–16**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Machine Cycle ในภาพหน้า 15 เรียง Fetch → Decode → Execute → Store โดย fetch instruction จาก memory, decode เป็น commands, execute commands และ store result กลับ memory ภาพเชื่อม Decode กับ Control Unit และ Execute กับ ALU หน้า 16 ระบุชื่อ Program counter (PC), Instruction Register (IR) และ Status register/flags พร้อมภาพองค์ประกอบ แต่ไม่ได้อธิบายรายละเอียดการอัปเดตแต่ละ register

**ประเด็นที่ต้องจำ**

- Fetch: ดึง instruction จาก memory
- Decode: แปลง instructions เป็น commands; Execute: ทำ commands; Store: เก็บ result ใน memory
- จำลำดับ Fetch–Decode–Execute–Store ตามภาพ
- Registers ที่ระบุ: Program counter (PC), Instruction Register (IR), Status register (status/flags)
- ภาพหน้า 16 วาง Program Counter และ Instruction Register ใน Control Unit; มี ALU/Accumulator และ RAM/ROM ในส่วนที่แยกกัน

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- PC = Program counter; IR = Instruction Register
- Status register: status, flags ตามข้อความหน้า 16
- หน้าที่ละเอียดของ PC/IR และบิต flags ไม่ได้อธิบายเป็นข้อความในไฟล์: ต้องตรวจสอบจากต้นฉบับ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านหมายเลขในภาพหน้า 15 เป็นขั้น 1–4 แล้วชี้ว่า instruction มาจาก memory และผลลัพธ์กลับสู่ memory โดยไม่แทรกขั้นใหม่จากภายนอก

**จุดที่อาจสับสน:** Machine Cycle 4 ขั้นในหน้า 15 ไม่ได้เท่ากับคำอ้างว่าแต่ละ instruction ต้องใช้ 4 clock cycles; Chapter01 ไม่ได้ระบุความสัมพันธ์ตายตัวเช่นนั้น

**ประโยคช่วยจำ:** ดึง–ถอด–ทำ–เก็บ = Fetch–Decode–Execute–Store

### 8. Cache Memory และระดับ L1 / L2 / L3

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 17–18**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Cache เป็นชั้นหน่วยความจำระหว่าง processor กับ main memory ซึ่งเล็กกว่าและเร็วกว่า main memory ใช้เก็บข้อมูลจาก main memory ที่คาดว่าจะถูกใช้อีกในอนาคตใกล้เพื่อเร่ง memory access การใช้หลายระดับอาจเพิ่ม performance ได้ โดย L1 อยู่ใกล้ core ที่สุด และ L2/L3 อยู่ห่างออกไปตามลำดับในคำอธิบายหน้า 18

**ประเด็นที่ต้องจำ**

- หน้า 17 ระบุ L1 fastest and smallest; L2 เป็นระดับถัดไป
- Cache smaller and faster than main memory (หน้า 18)
- คัดข้อมูลที่น่าจะใช้อีกใน near future มาไว้ใน cache
- L1 closest to core; additional levels L2/L3 progressively farther
- ภาพหน้า 17 มีตัวอย่าง L1 Data Cache แยกต่อ core และ Smart-Shared L2 Cache

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Cache Memory: หลายชั้นระหว่าง processor และ main memory
- L1 / L2 / L3 เป็นชื่อระดับที่ต้นฉบับใช้
- หน้า 17 ให้ตัวอย่างการแบ่ง/แชร์ cache; ไม่ใช่ข้อกำหนดว่า CPU ทุกแบบต้องจัดเหมือนภาพ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ภาพตัวอย่างหน้า 17 ไล่ CPU/L1 → L2 → Memory และเทียบภาพ shared L2 โดยอ้างว่าเป็น layout ที่สไลด์ยกตัวอย่าง

**จุดที่อาจสับสน:** ความใกล้ core ความเร็ว และขนาดเป็นคนละมิติ; อย่าอ้างว่า shared cache ทุกระดับเหมือนกันใน CPU ทุกตัว

**ประโยคช่วยจำ:** Cache: เล็ก–เร็ว–ใกล้ข้อมูลที่จะใช้; L1 ใกล้ core ที่สุด

### 9. Multi-core, Multi-thread และการมอง Motherboard → Core

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 19–23**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Multi-core ในสไลด์หมายถึง hardware ทางกายภาพที่แยกประมวลผลงานแบบ parallel ส่วน Multi-thread ถูกอธิบายเป็นเทคนิคเสมือนในการแบ่งงานย่อยป้อนให้ core โดยเปรียบ core เป็นจำนวนเชฟและ thread เป็นจำนวนแขนของเชฟ หน้า 21 ไล่ภาพจาก Motherboard → Processor chip → Core เพื่อแสดงระดับขององค์ประกอบ ส่วนหน้า 22–23 เป็นตัวอย่างบอร์ด two quad-core Xeon และภาพภายใน Apple A5

**ประเด็นที่ต้องจำ**

- Multi-core: hardware จริง รับงานมาประมวลผลแยกแบบ parallel (หน้า 19–20)
- Multi-thread: เทคนิคแบ่งการทำงานเสมือน จัดการงานเบื้องหลัง/แบ่งงานย่อยให้ core ตามคำอธิบายสไลด์
- หน้า 19 ยก Hyper-Threading ของ Intel หรือ SMT ของ AMD ตามข้อความต้นฉบับ
- หน้า 21: motherboard มี main memory chips/I/O chips/processor chip; processor chip มีหลาย core และ L3 cache
- Core ในภาพหน้า 21 มี instruction logic, ALU, load/store logic และ L1/L2 instruction/data caches
- หน้า 22 เป็น motherboard with two Intel quad-core Xeon processors; หน้า 23 เป็น Apple A5 ตัวอย่างองค์ประกอบบนชิป

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Multi-core / Multi-thread; parallel
- Hyper-Threading / SMT เป็นชื่อที่สไลด์ยก ไม่ได้ให้รายละเอียดกลไก
- Motherboard, Processor chip และ Core เป็นคนละระดับของภาพ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้อุปมาในหน้า 20: จำนวนเชฟเทียบกับจำนวน core ส่วนจำนวนแขนของเชฟเทียบกับ thread แล้วดูภาพขยายหน้า 21 เพื่อไม่สับสนระดับ chip กับ core

| ประเด็น | Multi-core | Multi-thread ตามสไลด์ |
| --- | --- | --- |
| ลักษณะ | hardware ทางกายภาพ | เทคนิคแบ่งงานเสมือน |
| อุปมา | จำนวนเชฟ | จำนวนแขนต่อเชฟ |
| คำอธิบายงาน | แยกประมวลผล parallel | แบ่งงานย่อยป้อน core |

**จุดที่อาจสับสน:** คำอธิบาย Multi-thread ในหน้า 19–20 เป็นแบบย่อ ไม่ใช่การนิยามทุกกรณีของ software threads และภาพ Apple A5 ไม่ได้ใช้แทน layout ของทุก processor

**ประโยคช่วยจำ:** Core = เชฟ; Thread = แขนของเชฟ (อุปมาต้นฉบับหน้า 20)

### 10. Manufacturing ICs, Yield และตัวอย่าง Wafer

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter01.pdf, **หน้า 24–25**

เหตุผลการจัดระดับ: เป็นรายละเอียดประกอบและตัวอย่างการผลิต ไม่ใช่แกนการคำนวณสมรรถนะ

ภาพการผลิตเริ่มจาก silicon ingot ผ่าน slicer เป็น blank wafers ทำ processing steps แล้วทดสอบ wafer ก่อนตัดเป็น dies ที่นำไปบรรจุและทดสอบอีกครั้ง Yield ในสไลด์หมายถึงสัดส่วน dies ที่ใช้งานได้ต่อ wafer หน้า 25 เป็นตัวอย่าง Intel Core i7 wafer ขนาด 300 mm มี 280 chips ใช้เทคโนโลยี 32 nm และระบุขนาด chip 20.7 × 10.5 mm

**ประเด็นที่ต้องจำ**

- ลำดับภาพ: silicon ingot → slicer → blank wafers → 20–40 processing steps → patterned wafers
- Wafer tester → tested wafer → dicer → tested dies → bond die to package
- Packaged dies → part tester → tested packaged dies → ship to customers
- Yield: proportion of working dies per wafer
- ตัวเลข 300 mm / 280 chips / 32 nm / 20.7 × 10.5 mm เป็นตัวอย่างเฉพาะในหน้า 25

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Wafer และ die/chip เป็นคนละระดับในภาพ
- Yield = สัดส่วนของ working dies ต่อ wafer; ไม่มีสูตร yield ขั้นสูงในสไลด์

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านลูกศรหน้า 24 แบบซ้าย→ขวาในแถวแรก ขวา→ซ้ายในแถวสอง แล้วซ้าย→ขวาในแถวท้าย เพื่อไม่สลับ dicer กับ wafer tester

**จุดที่อาจสับสน:** 300 mm เป็นขนาด wafer ในตัวอย่าง ไม่ใช่ขนาด chip; ตัวเลขตัวอย่างไม่ได้ยืนยันกระบวนการผลิตปัจจุบันทุกแบบ

**ประโยคช่วยจำ:** สร้างลาย–ทดสอบ wafer–ตัด–แพ็ก–ทดสอบแพ็ก

### 11. อ่านกราฟ Single Processor Performance

**🟡 สำคัญ** · itds-211_comp_arch_Chapter01.pdf, **หน้า 26**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือบริบทช่วยประยุกต์แนวคิดหลัก

กราฟหน้า 26 แสดงตัวอย่างแนวโน้มสมรรถนะของระบบตั้งแต่ปี 1978 ถึง 2018 โดยมีอัตราเติบโตที่กำกับในช่วงต่าง ๆ เป็น 25%, 52%, 23%, 12% และ 3.5% ต่อปี ช่วงท้ายกราฟยังเพิ่มขึ้นแต่ด้วยอัตราที่ต่ำกว่าช่วง 52% ต่อปี จึงต้องแยก “ระดับ performance” ออกจาก “อัตราการเพิ่ม” และไม่ใช้กราฟนี้ยืนยันค่าหลังปี 2018

**ประเด็นที่ต้องจำ**

- แกนนอนเป็นปี 1978–2018; แกนตั้งแสดง performance ด้วยช่วงตัวเลข 1, 10, 100, 1000, 10000, 100000
- อัตราที่กำกับตามลำดับช่วง: 25% → 52% → 23% → 12% → 3.5% ต่อปี
- ชื่อ processor/system และ clock rates ในกราฟเป็นข้อมูลตัวอย่างเฉพาะจุด
- กราฟนี้เป็นหลักฐานของตัวอย่างช่วงเวลาที่แสดง ไม่ใช่คำทำนายสถาปัตยกรรมหรือ benchmark ปัจจุบัน

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Single Processor Performance: ชื่อหัวข้อกราฟ
- %/year ในกราฟเป็นอัตราการเติบโต ไม่ใช่ execution time หน่วยวินาที

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เปรียบเทียบข้อความ 52%/year กับ 3.5%/year ที่ปลายกราฟ: อัตราเพิ่มลดลง แต่ค่าจุด performance ยังสูงกว่าจุดต้นกราฟ

**จุดที่อาจสับสน:** อย่าตีความอัตราโตที่ลดลงว่า performance กลับลดลง และอย่าอ่านช่วงแกนตั้งเป็นระยะเชิงเส้นเท่ากัน

**ประโยคช่วยจำ:** แยก “สูงแค่ไหน” ออกจาก “โตเร็วแค่ไหน”

### 12. RISC vs CISC Architecture

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 27**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

RISC ย่อจาก Reduced Instruction Set Computing ส่วน CISC ย่อจาก Complex Instruction Set Computing สไลด์แสดงเส้นทางควบคุมสองภาพ ฝั่งซ้ายมี Program Memory → IR → Decoder และฝั่งขวามี Program Memory → mPC → mPM ก่อนเชื่อมไป Data path ภาพนี้ยังไม่ได้ให้ตารางเปรียบเทียบ instruction length, CPI หรือผล benchmark จึงไม่ควรเติมคุณสมบัติเหล่านั้นเอง

**ประเด็นที่ต้องจำ**

- จำชื่อเต็ม RISC และ CISC ให้ตรง
- ภาพทั้งสองมี PC, Program Memory, Data Memory และ Data path
- ฝั่งซ้ายมี IR/Decoder; ฝั่งขวามี mPC/mPM; มีสัญลักษณ์ CW ในเส้นทางเชื่อม
- สไลด์ขยาย mPC = microprogram counter และพิมพ์ mPM = Microprocessor Mode ตามต้นฉบับ

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RISC = Reduced Instruction Set Computing
- CISC = Complex Instruction Set Computing
- คำขยาย mPM ที่พิมพ์ว่า Microprocessor Mode และความหมาย CW: ต้องตรวจสอบจากต้นฉบับก่อนใช้เป็นคำนิยามทางเทคนิค

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตอบจากภาพว่า “ฝั่งซ้ายมี Decoder ส่วนฝั่งขวามี mPC/mPM” ได้ แต่ไม่ใช้ภาพเดียวกล่าวว่าทุกระบบ RISC/CISC ต้องมีการจัดวงจรเหมือนกันทั้งหมด

| ประเด็นที่มีในต้นฉบับ | ฝั่งซ้ายของภาพ | ฝั่งขวาของภาพ |
| --- | --- | --- |
| บล็อกหลัง Program Memory | IR → Decoder | mPC → mPM |
| บล็อกร่วม | PC / Data Memory / Data path | PC / Data Memory / Data path |

**จุดที่อาจสับสน:** Complex ในชื่อ CISC ไม่ใช่หลักฐานว่าเร็วกว่าเสมอ และ Reduced ในชื่อ RISC ไม่ได้ให้จำนวนคำสั่งหรือ CPI ของเครื่องใดในสไลด์นี้

**ประโยคช่วยจำ:** R = Reduced; C = Complex; รายละเอียดต้องยึดภาพที่มี

### 13. Application Parallelism กับ Architectural Parallelism

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 32**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

สไลด์แบ่ง parallelism เป็นสองมุม คือประเภทที่พบใน applications และประเภทของ architectural parallelism กลุ่ม applications ระบุ Data-Level Parallelism กับ Task-Level Parallelism ส่วนกลุ่ม architecture ระบุ Instruction-Level, Vector architectures/GPUs, Thread-Level และ Request-Level Parallelism เอกสารหน้านี้เป็นรายการจำแนก ไม่ได้ให้กลไกหรือโจทย์วัดความเร็วของแต่ละประเภท

**ประเด็นที่ต้องจำ**

- Applications: Data-Level Parallelism (DLP), Task-Level Parallelism (TLP)
- Architectural: Instruction-Level Parallelism (ILP)
- Architectural: Vector architectures / Graphic Processor Units (GPUs)
- Architectural: Thread-Level Parallelism และ Request-Level Parallelism

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- DLP = Data-Level Parallelism; TLP ในรายการ applications = Task-Level Parallelism
- ILP = Instruction-Level Parallelism
- Task-Level กับ Thread-Level เป็นคนละข้อความในคนละกลุ่มของหน้า 32; ไม่สลับชื่อเต็มของตัวย่อ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** วาดสองคอลัมน์ตามหัวข้อในหน้า 32 แล้วจัด DLP/TLP ไว้ application ส่วนอีก 4 รายการไว้ architectural

| มุมจำแนก | รายการ |
| --- | --- |
| Applications | DLP; Task-Level Parallelism (TLP) |
| Architectural | ILP; Vector/GPUs; Thread-Level; Request-Level |

**จุดที่อาจสับสน:** Thread-Level ไม่ใช่ Task-Level ที่ใช้ชื่อแทนกันได้โดยอัตโนมัติในสไลด์นี้ และชื่อประเภทไม่ได้บอก speedup เป็นตัวเลข

**ประโยคช่วยจำ:** Application มี Data/Task; Architecture มี Instruction/Vector- GPU/Thread/Request

### 14. Flynn’s Taxonomy: SISD / SIMD / MISD / MIMD

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 33**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Flynn’s Taxonomy ในสไลด์จัดกลุ่มจาก instruction streams และ data streams ที่เป็น single หรือ multiple จึงได้ SISD, SIMD, MISD และ MIMD หน้า 33 ยก vector architectures, multimedia extensions และ GPUs ไว้ภายใต้ SIMD ระบุ MISD ว่าไม่มี commercial implementation ในบริบทสไลด์ และแบ่ง MIMD เป็น tightly-coupled กับ loosely-coupled

**ประเด็นที่ต้องจำ**

- SISD: Single instruction stream, single data stream
- SIMD: Single instruction stream, multiple data streams
- MISD: Multiple instruction streams, single data stream
- MIMD: Multiple instruction streams, multiple data streams
- SIMD examples: vector architectures, multimedia extensions, graphics processor units
- MISD: No commercial implementation ตามข้อความในสไลด์; MIMD แยก tightly-coupled/loosely-coupled

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- I หมายถึง instruction stream; D หมายถึง data stream
- S = Single; M = Multiple ในชื่อกลุ่มทั้งสี่
- ข้อความเรื่อง commercial implementation เป็นคำอ้างในต้นฉบับ ไม่ขยายไปเป็นข้อยืนยันตลาดปัจจุบัน

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ทำตาราง 2 × 2 จาก Single/Multiple instruction streams กับ Single/Multiple data streams แล้วใส่ชื่อย่อให้ครบทั้งสี่ช่อง

| ชนิด | Instruction streams | Data streams |
| --- | --- | --- |
| SISD | Single | Single |
| SIMD | Single | Multiple |
| MISD | Multiple | Single |
| MIMD | Multiple | Multiple |

**จุดที่อาจสับสน:** นับ streams ตามเกณฑ์ในหน้า 33 ไม่ใช่ใช้จำนวน core ที่เห็นเพียงอย่างเดียวแทนนิยาม และอย่าสลับลำดับ I กับ D

**ประโยคช่วยจำ:** อ่านตัวอักษรหน้า I ก่อน แล้วตัวอักษรหน้า D: Instruction → Data

### 15. System Level Architecture Patterns

**🟡 สำคัญ** · itds-211_comp_arch_Chapter01.pdf, **หน้า 34**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือบริบทช่วยประยุกต์แนวคิดหลัก

Monolithic คือระบบที่รวมเป็นหนึ่งเดียว ส่วน Client-server แยกเครื่องที่ร้องขอกับเครื่องที่ให้บริการ Distributed systems กระจายการคำนวณไปยังเครื่องที่เชื่อมผ่านเครือข่าย และ Micro services เป็นบริการแบบ modular ที่ deploy ได้อย่างอิสระ สไลด์กำกับ Micro services ว่าเป็น software architecture pattern มากกว่า

**ประเด็นที่ต้องจำ**

- Monolithic: Single unified system
- Client-server: split between requesting and serving machines
- Distributed systems: computation spread across networked machines
- Micro services: modular, independently deployable services; more of a software architecture pattern

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Monolithic; Client-server; Distributed systems; Micro services เป็นชื่อรูปแบบตามหน้า 34
- independently deployable เป็นลักษณะที่สไลด์ใช้กับ Micro services

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จับคู่คำสำคัญ: unified → Monolithic; requesting/serving → Client-server; spread across network → Distributed; independently deployable services → Micro services

| Pattern | จุดเน้น |
| --- | --- |
| Monolithic | ระบบเดียวรวมเป็นหนึ่ง |
| Client-server | บทบาทเครื่องร้องขอ/ให้บริการ |
| Distributed | กระจายการคำนวณผ่านเครือข่าย |
| Micro services | บริการ modular แยก deploy ได้ |

**จุดที่อาจสับสน:** รูปแบบระดับระบบในหน้านี้ใช้เกณฑ์ต่างจาก Flynn’s Taxonomy หน้า 33 จึงไม่ควรนำชื่อสองชุดมาจัดเป็นกลุ่มเดียวกัน

**ประโยคช่วยจำ:** รวม–ขอ/ให้–กระจาย–บริการแยก deploy

### 16. Performance และ Relative Performance

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 35–36**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

หน้า 35 เปิดส่วน Performance และหน้า 36 นิยาม Performance = 1/Execution Time ดังนั้นเวลาน้อยกว่าหมายถึง performance มากกว่า การกล่าวว่า X เร็วกว่า Y เป็น n เท่าใช้ Performance_X/Performance_Y = ExecutionTime_Y/ExecutionTime_X ตัวอย่างโปรแกรมเดียวกันใช้เวลา 10 s บน A และ 15 s บน B จึงได้ A เร็วกว่า B 1.5 เท่า

**ประเด็นที่ต้องจำ**

- Performance ผกผันกับ Execution Time ตามนิยามในหน้า 36
- เมื่อเปรียบเทียบ X กับ Y ให้วางเวลาของ Y เป็นตัวตั้งและของ X เป็นตัวหาร
- ตัวอย่างต้นฉบับ: A = 10 s, B = 15 s → 15/10 = 1.5
- ค่า “กี่เท่า” เป็นอัตราส่วนเวลาเดียวกัน จึงไม่มีหน่วยวินาทีเหลือ

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Performance = 1 / Execution Time
- Performance_X / Performance_Y = ExecutionTime_Y / ExecutionTime_X = n
- ตัวห้อย X/Y ระบุเครื่องที่เปรียบเทียบ ไม่ใช่เครื่องหมายคูณ

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ก่อนหารให้เขียนประโยคว่า “A เร็วกว่า B กี่เท่า” แล้วแทน Time_B/Time_A = 15 s / 10 s

**สูตรที่ต้องรู้**

```text
Performance = 1 / Execution Time
```

เวลาที่ใช้ต้องเป็นเกณฑ์เดียวกันเมื่อเปรียบเทียบ

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 36

**สูตรที่ต้องรู้**

```text
Performance_X / Performance_Y
= ExecutionTime_Y / ExecutionTime_X = n
```

X เร็วกว่า Y เป็น n เท่า

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 36

**ตัวอย่างต้นฉบับ: A 10 s, B 15 s**

1. กำหนด Time_A = 10 s และ Time_B = 15 s
2. Performance_A / Performance_B = Time_B / Time_A
3. แทนค่า 15 s / 10 s = 1.5

**คำตอบ:** A เร็วกว่า B 1.5 เท่า

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 36

**จุดที่อาจสับสน:** การหาร Time_A/Time_B จะได้อัตราส่วนเวลาของ A ต่อ B ซึ่งกลับด้านจาก Performance_A/Performance_B อย่ารายงาน 10/15 ว่า A เร็วกว่า B 0.67 เท่าตามนิยามที่ใช้

**ประโยคช่วยจำ:** ถาม X เร็วกว่า Y → เอาเวลา Y หารเวลา X

### 17. Elapsed Time, CPU Time และ Clock

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 37–38**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Elapsed time คือเวลาตอบสนองรวม processing, I/O, OS overhead และ idle time จึงใช้พิจารณา system performance ส่วน CPU time คือเวลาประมวลผลงานหนึ่งซึ่งตัด I/O time และเวลาที่งานอื่นใช้ CPU ออก และรวม user CPU time กับ system CPU time หน้า 38 นิยาม clock period เป็นช่วงเวลาต่อ cycle และ clock frequency/rate เป็นจำนวน cycles ต่อวินาที พร้อมตัวอย่างการแปลง ps, ns, GHz และ MHz

**ประเด็นที่ต้องจำ**

- Elapsed time: total response time รวม processing, I/O, OS overhead, idle
- CPU time: processing given job; discounts I/O และ other jobs’ shares; comprises user CPU + system CPU time
- สไลด์ระบุว่าแต่ละโปรแกรมได้รับผลจาก CPU/system performance ต่างกัน
- Clock period = duration of a clock cycle; Clock rate = cycles per second
- 250 ps = 0.25 ns = 250 × 10⁻¹² s
- 4.0 GHz = 4000 MHz = 4.0 × 10⁹ Hz

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Elapsed time / CPU time เป็นเกณฑ์เวลาคนละขอบเขต
- Clock cycle time หรือ period เป็นเวลา/cycle; rate เป็น cycles/second
- ps, ns, s; MHz, GHz, Hz — ต้องแปลงหน่วยให้สอดคล้องก่อนแทนสูตร

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ตัวอย่างหน่วยในหน้า 38 ทวน 250 ps → 0.25 ns และ 4 GHz → 4 × 10⁹ Hz ก่อนทำสูตร CPU Time ในหัวข้อถัดไป

| ตัววัด | ความหมาย | ขอบเขต/หน่วย |
| --- | --- | --- |
| Elapsed time | เวลาตอบสนองรวม | processing + I/O + OS overhead + idle |
| CPU time | เวลาประมวลผลงาน | user CPU + system CPU time |
| Clock period | ระยะเวลาของ cycle | เช่น 250 ps |
| Clock rate | cycles ต่อวินาที | เช่น 4 GHz |

**จุดที่อาจสับสน:** อย่าแทน Elapsed time ลงสูตร CPU Time โดยไม่ตรวจว่าข้อมูลโจทย์ให้เวลาแบบใด และอย่าสับสน clock period กับ clock rate

**ประโยคช่วยจำ:** Elapsed นับเวลารวม; CPU นับการประมวลผลของงาน — period เป็นเวลา, rate เป็นอัตรา

### 18. CPU Time และโจทย์ออกแบบ Clock Rate

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 39–40**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

CPU Time เท่ากับจำนวน CPU Clock Cycles คูณ Clock Cycle Time หรือหารด้วย Clock Rate จึงเพิ่ม performance ได้ด้วยการลด cycles หรือเพิ่ม rate โดยต้องดู trade-off ระหว่างสองค่า ตัวอย่างหน้า 40 ให้เครื่อง A มี 2 GHz และ CPU Time 10 s แล้วออกแบบ B ให้ใช้ 6 s แต่ต้องใช้ cycles มากกว่า A 1.2 เท่า ผลลัพธ์คือ B ต้องมี Clock Rate 4 GHz

**ประเด็นที่ต้องจำ**

- CPU Time = CPU Clock Cycles × Clock Cycle Time = CPU Clock Cycles / Clock Rate
- ลด clock cycles หรือเพิ่ม clock rate ช่วย performance โดยต้องพิจารณาอีกตัวแปรร่วมด้วย
- A: 10 s × 2 GHz = 20 × 10⁹ cycles
- B: cycles = 1.2 × 20 × 10⁹ = 24 × 10⁹; เป้าหมาย CPU time = 6 s
- ClockRate_B = 24 × 10⁹ / 6 s = 4 × 10⁹ Hz = 4 GHz

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- CPU Clock Cycles: จำนวน cycles รวมที่งานใช้
- Clock Cycle Time: เวลา/cycle; Clock Rate: cycles/second
- CPU Time: เวลา CPU ของงาน หน่วย s เมื่อใช้ cycles กับ Hz

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ทำตามลำดับตัวอย่างหน้า 40: หา cycles_A จากเวลาและ rate → ปรับ cycles_B ด้วย 1.2 → หารด้วยเวลาที่ต้องการ 6 s

**สูตรที่ต้องรู้**

```text
CPU Time = CPU Clock Cycles × Clock Cycle Time
         = CPU Clock Cycles / Clock Rate
```

Cycles × seconds/cycle หรือ cycles ÷ cycles/second ให้ผลเป็น seconds

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 39

**สูตรที่ต้องรู้**

```text
ClockRate_B = (1.2 × ClockCycles_A) / 6 s
```

เป็นสมการเฉพาะโจทย์หน้า 40 ไม่ใช่ค่าคงที่ทั่วไป

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 40

**ตัวอย่างต้นฉบับ: ออกแบบ B ให้ใช้เวลา 6 s**

1. A: Clock Rate = 2 GHz และ CPU Time = 10 s
2. ClockCycles_A = 10 × 2 × 10⁹ = 20 × 10⁹ cycles
3. ClockCycles_B = 1.2 × 20 × 10⁹ = 24 × 10⁹ cycles
4. ClockRate_B = (24 × 10⁹ cycles) / 6 s = 4 × 10⁹ Hz

**คำตอบ:** B ต้องใช้ clock rate 4 GHz

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 40

**จุดที่อาจสับสน:** โจทย์เปลี่ยนทั้ง clock rate และจำนวน cycles จึงห้ามใช้เพียงอัตรา 10/6 คูณ 2 GHz โดยลืมตัวประกอบ 1.2

**ประโยคช่วยจำ:** เวลา = รอบ / อัตรา; รอบเปลี่ยนต้องคูณให้ครบก่อนหารเวลา

### 19. Instruction Count, CPI และการเปรียบเทียบ CPU

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter01.pdf, **หน้า 41–42**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ ขั้นตอน การจำแนก หรือสูตรหลักที่เอกสารระบุโดยตรง

Clock Cycles เท่ากับ Instruction Count คูณ Cycles per Instruction จึงเขียน CPU Time เป็น IC × CPI × Clock Cycle Time หรือ IC × CPI / Clock Rate ได้ Instruction Count ขึ้นกับ program, ISA และ compiler ขณะที่ average CPI ขึ้นกับ CPU hardware และ instruction mix ตัวอย่างหน้า 42 ใช้จำนวนคำสั่ง I เท่ากัน: A มี cycle time 250 ps/CPI 2.0 ส่วน B 500 ps/CPI 1.2 จึงได้เวลา 500I ps กับ 600I ps และ A เร็วกว่า 1.2 เท่า

**ประเด็นที่ต้องจำ**

- Clock Cycles = Instruction Count × Cycles per Instruction
- CPU Time = Instruction Count × CPI × Clock Cycle Time = Instruction Count × CPI / Clock Rate
- Instruction Count determined by program, ISA, compiler
- Average CPI determined by CPU hardware; หากแต่ละ instruction มี CPI ต่างกัน average CPI ขึ้นกับ instruction mix
- ตัวอย่าง A: I × 2.0 × 250 ps = I × 500 ps; B: I × 1.2 × 500 ps = I × 600 ps
- CPUTime_B / CPUTime_A = 600I/500I = 1.2 → A เร็วกว่า

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Instruction Count (IC): จำนวนคำสั่งของโปรแกรมตามบริบทสไลด์
- CPI = Cycles per Instruction; ในการใช้ค่ารวมให้พิจารณา average CPI
- I ในตัวอย่างหน้า 42 แทน Instruction Count ที่ตั้งให้เท่ากัน; ps เป็นหน่วยเวลา ไม่ใช่ CPI

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ I เดียวกันตามการแทนค่าในตัวอย่างหน้า 42 คำนวณเวลาแต่ละเครื่องก่อน แล้วนำเวลาของเครื่องช้าหารด้วยเวลาของเครื่องเร็ว

**สูตรที่ต้องรู้**

```text
Clock Cycles = Instruction Count × CPI
```

จำนวนรอบรวมจากจำนวนคำสั่งและรอบเฉลี่ยต่อคำสั่ง

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 41

**สูตรที่ต้องรู้**

```text
CPU Time = Instruction Count × CPI × Clock Cycle Time
         = (Instruction Count × CPI) / Clock Rate
```

ใช้พิจารณา IC, CPI และ clock ร่วมกัน

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 41

**ตัวอย่างต้นฉบับ: A กับ B ใช้ I เท่ากัน**

1. A: Cycle Time = 250 ps, CPI = 2.0 → Time_A = I × 2.0 × 250 = 500I ps
2. B: Cycle Time = 500 ps, CPI = 1.2 → Time_B = I × 1.2 × 500 = 600I ps
3. เครื่อง A ใช้เวลาน้อยกว่า จึงหา Time_B / Time_A
4. 600I ps / 500I ps = 1.2 โดย I และหน่วย ps ตัดกัน

**คำตอบ:** A เร็วกว่า B 1.2 เท่า แม้ A มี CPI สูงกว่า

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 42

**จุดที่อาจสับสน:** CPI ต่ำกว่าเพียงอย่างเดียวไม่พอยืนยันว่าเร็วกว่า เพราะ cycle time และ Instruction Count อยู่ในสมการด้วย ตัวอย่างใช้ I เท่ากันตามที่แสดง ไม่ควรขยายว่า Same ISA ทำให้จำนวนคำสั่งเท่ากันทุกโปรแกรม เพราะหน้า 41 ยังระบุ program/compiler เป็นปัจจัย

**ประโยคช่วยจำ:** เวลา CPU มองสามตัว: จำนวนคำสั่ง × รอบต่อคำสั่ง × เวลาต่อรอบ

## 3. Roadmap ทบทวน

1. **เริ่มจาก WHAT / HOW** — แยกนิยามและขอบเขต Architecture/Organization ก่อนใช้ชื่อองค์ประกอบ (itds-211_comp_arch_Chapter01.pdf, หน้า 3–4)
2. **ตามโปรแกรมลงสู่ CPU** — High-level → Assembly → Binary แล้วดู Control Unit/ALU/Registers และ Machine Cycle (itds-211_comp_arch_Chapter01.pdf, หน้า 11–16)
3. **ขยายระบบ Memory และหลาย Core** — ดู cache levels แล้วแยก core/thread และระดับ motherboard/chip/core (itds-211_comp_arch_Chapter01.pdf, หน้า 17–23)
4. **จัดประเภทและบริบทระบบ** — ทวน Cloud, Embedded/ARM, RISC/CISC, application/architectural parallelism และ Flynn ก่อนเปรียบเทียบ patterns (itds-211_comp_arch_Chapter01.pdf, หน้า 5–8, 27–34)
5. **นิยาม Performance และหน่วย** — เริ่มส่วนกลับของเวลา แยก elapsed/CPU time และทวน ps/ns/GHz (itds-211_comp_arch_Chapter01.pdf, หน้า 9–10, 36–38)
6. **ฝึกคำนวณจากตัวอย่างจริง** — ทำโจทย์ clock rate หน้า 40 และ CPI หน้า 42 โดยไม่เปิดเฉลย แล้วตรวจทุกขั้น (itds-211_comp_arch_Chapter01.pdf, หน้า 39–42)
7. **อ่านรายละเอียดประกอบแล้วทดสอบ** — ดู manufacturing/wafer/กราฟประวัติเป็นภาพประกอบ ปิดท้ายแบบฝึกผสมและกลับไปหน้าที่ตอบผิด (itds-211_comp_arch_Chapter01.pdf, หน้า 24–26)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · นิยามและระดับโปรแกรม

อ่าน Architecture/Organization และชั้นโปรแกรม แล้วอธิบายด้วยคำตนเอง

**เกณฑ์ผ่าน:** จำ WHAT/HOW และเส้นทาง Compiler/Assembler ได้พร้อมตัวอย่างในเอกสาร

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 3–4, 11–12

### รอบ 2 · Hardware ที่ต้องอธิบายได้

ทวน CPU, cycle, registers, cache และ core/thread พร้อมชี้ภาพ

**เกณฑ์ผ่าน:** ไล่ Fetch–Decode–Execute–Store และแยก core/chip/motherboard ได้

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 13–23

### รอบ 3 · ตารางเปรียบเทียบ

ทำตาราง Cloud, Embedded/ARM, RISC/CISC, parallelism, Flynn และ patterns

**เกณฑ์ผ่าน:** ใช้เกณฑ์ของแต่ละตารางถูกต้อง ไม่สลับ Task-Level กับ Thread-Level

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 5–8, 27–34

### รอบ 4 · สูตรและหน่วย

ทวน Performance, elapsed/CPU time, clock period/rate แล้วเขียนสมการจากความจำ

**เกณฑ์ผ่าน:** วางอัตราส่วนเวลาได้ถูกทิศ และแปลง 250 ps/4 GHz ได้

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 36–39, 41

### รอบ 5 · ทำตัวอย่างต้นฉบับเอง

ปิดเฉลยหน้า 40/42 แล้วทำโจทย์ทั้งสองใหม่ทุกขั้น

**เกณฑ์ผ่าน:** ได้ B = 4 GHz และ A เร็วกว่า B 1.2 เท่า พร้อมอธิบายเหตุผล

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 40–42

### รอบ 6 · ฝึกแบบผสมและซ่อมจุดผิด

ทำคำถาม 57 ข้อ แยกข้อที่ต้องจำกับข้อที่คำนวณผิด แล้วอ่านหน้าที่อ้างอิงซ้ำ

**เกณฑ์ผ่าน:** ตอบและตรวจเหตุผลได้จากต้นฉบับ ไม่เติมรายละเอียดที่เอกสารไม่ให้

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 3–42

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1: นิยาม/โปรแกรม/CPU/cache/core (หน้า 3–4, 11–23); วัน 2: Cloud/Embedded/การจำแนก (หน้า 5–10, 27–34); วัน 3: หน่วยและสูตรหน้า 36–42 ทำโจทย์เดิมและแบบฝึก ทวนจุดผิด; หน้า 24–26 อ่านประกอบ
- **ถ้าเหลือ 1 วัน:** เริ่มหน้า 36–42 ให้สูตร/หน่วย/วิธีทำครบ แล้วทวนนิยามหน้า 3–4, CPU/cycle/cache หน้า 14–21 และ Flynn/parallelism หน้า 32–33 ปิดท้าย Cloud/Embedded/patterns และข้อที่ตอบผิด
- **ถ้าเหลือ 3 ชั่วโมง:** 0–20 นาที: นิยาม/CPU หน้า 3–4, 14–16; 20–40: cache/core หน้า 17–21; 40–60: RISC/parallelism/Flynn หน้า 27, 32–33; 60–85: performance/เวลา/clock หน้า 36–38; 85–130: โจทย์ CPU/CPI หน้า 39–42; 130–160: แบบฝึก; 160–180: ทวน Cloud/Embedded/patterns และจุดผิด เป็นตัวเลือกทั่วไปสำหรับเวลาน้อย

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

เริ่มจากนิยาม/CPU/ขั้นตอน/การจำแนก และสูตรหน้า 36–42 เพราะเป็นแกนที่เอกสารให้ชัดเจน ยังบอกความถี่ออก Final ไม่ได้จากสไลด์เพียงไฟล์เดียว

- **ควรท่องจำ:** WHAT/HOW, หน้าที่ CPU, cycle 4 ขั้น, ชื่อเต็ม RISC/CISC, เกณฑ์ Flynn, หน่วย และสมการหลัก (หน้า 3–4, 14–18, 27, 32–33, 36–41)
- **ควรเข้าใจ:** ความเชื่อมโยง software/hardware, cache, core/thread, ปัจจัย performance และเหตุที่ CPI หรือ clock เพียงตัวเดียวไม่พอตัดสินความเร็ว (หน้า 9–23, 39–42)
- **ควรฝึกคำนวณ:** ตัวอย่าง 10/15 s หน้า 36, หน่วยหน้า 38, clock rate หน้า 40 และ CPI หน้า 42 ใช้ข้อมูลโจทย์เดิมและแสดงขั้น/หน่วยครบ
- **เตรียมข้อสอบแบบผสม:** เลือกตอบจับคู่คำนิยาม/ประเภท; อัตนัยอธิบายหน้าที่/ลำดับ; วิเคราะห์เปรียบเทียบด้วยเกณฑ์ที่ถูก; คำนวณด้วยโจทย์ต้นฉบับ ไม่อ้างว่าเป็นข้อสอบจริง

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 19 ข้อ, อัตนัย 15 ข้อ, วิเคราะห์ 19 ข้อ, คำนวณ 4 ข้อ

### Architecture, Organization และขอบเขตการออกแบบ

**ข้อ 1 · เลือกตอบ: ข้อใดเป็นตัวอย่าง Architecture ตามนิยามหน้า 3?**

- A. addressing modes
- B. bus width
- C. clock speed
- D. cache design

เฉลย: addressing modes เป็นคุณลักษณะที่สไลด์จัดให้โปรแกรมเมอร์มองเห็น

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 3

**ข้อ 2 · อัตนัย: มุมมอง Old กับ Real computer architecture ต่างกันอย่างไร?**

เฉลย: Old เน้น ISA design; Real พิจารณาความต้องการเครื่องเป้าหมาย และรวม ISA/microarchitecture/hardware เพื่อเพิ่ม performance ภายใต้ cost, power, availability

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 4

**ข้อ 3 · วิเคราะห์: หากกำลังพิจารณา bus width ควรจัดเป็น WHAT หรือ HOW ตามหน้า 3 เพราะเหตุใด?**

เฉลย: HOW / Organization เพราะเป็นรายละเอียดหน่วยทำงานและการเชื่อมต่อที่ทำให้ข้อกำหนดสถาปัตยกรรมเกิดขึ้นจริง

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 3

### Classes of Computers, Embedded Systems และ ARM

**ข้อ 4 · เลือกตอบ: กลุ่มใดถูกระบุว่ามี power/performance/cost constraints ที่เข้มงวด?**

- A. Embedded Computers
- B. Supercomputers
- C. Compiler
- D. Assembler

เฉลย: Embedded Computers ถูกระบุเช่นนั้นในหน้า 5

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 5

**ข้อ 5 · อัตนัย: ARM Products หน้า 30 แสดงกลุ่มอะไร และ Cortex-M มีตัวอย่างรุ่นใด?**

เฉลย: Cortex-A/Cortex-A50, Cortex-R, Cortex-M; รุ่น M ที่แสดงคือ M0, M0+, M3, M4

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 30

**ข้อ 6 · วิเคราะห์: เหตุใดหลายกิจกรรมใน Embedded System จึงทำให้ข้อจำกัดซับซ้อนขึ้นตามหน้า 28?**

เฉลย: ต้องจัดการหลายกิจกรรมพร้อมกันภายใต้ความสัมพันธ์กับสิ่งแวดล้อม จึงเพิ่มความซับซ้อนของ real-time constraints ตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 28

### Cloud Computing และ SaaS / PaaS / IaaS

**ข้อ 7 · เลือกตอบ: บริการใดให้ platform เพื่อให้ application ของลูกค้ารันได้?**

- A. PaaS
- B. SaaS
- C. Cloud networking
- D. Compiler

เฉลย: PaaS ให้ platform สำหรับรัน customer applications ตามหน้า 7

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 7

**ข้อ 8 · อัตนัย: Cloud Computing, Cloud networking และ Cloud Storage ต่างกันอย่างไรตามหน้า 6?**

เฉลย: Computing เป็นโมเดลเข้าถึงทรัพยากรร่วมตามต้องการ; networking เป็นเครือข่ายและหน้าที่จัดการที่รองรับ cloud; Storage ในสไลด์คือ database storage/applications ที่โฮสต์ระยะไกล

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 6

**ข้อ 9 · วิเคราะห์: จากแผนภาพหน้า 8 การไปทาง SaaS มี trade-off อะไร?**

เฉลย: แผนภาพแสดง less complex, lower upfront cost, more scalable แต่ less customizable เทียบกับด้าน Traditional IT

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 8

### ปัจจัยที่กำหนด Performance และ Eight Great Ideas

**ข้อ 10 · เลือกตอบ: สิ่งใดกำหนดจำนวน operations ตามหน้า 9?**

- A. Algorithm
- B. I/O system
- C. Power Supply Unit
- D. Status register

เฉลย: Algorithm กำหนดจำนวน operations executed

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 9

**ข้อ 11 · อัตนัย: ระบุ Eight Great Ideas ทั้ง 8 ข้อ**

เฉลย: Design for Moore’s Law; Use abstraction to simplify design; Make the common case fast; Performance via parallelism; Performance via pipelining; Performance via prediction; Hierarchy of memories; Dependability via redundancy

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 10

**ข้อ 12 · วิเคราะห์: หากภาษา/ compiler เปลี่ยน หน้า 9 บอกให้พิจารณาค่าระดับใด?**

เฉลย: จำนวน machine instructions ที่ถูกทำต่อ operation ไม่ใช่อนุมานว่า clock rate ต้องเปลี่ยน

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 9

### Below Your Program และ Levels of Program Code

**ข้อ 13 · เลือกตอบ: Assembly language ถูกอธิบายว่าเป็นอะไร?**

- A. Textual representation of instructions
- B. Binary digits เท่านั้น
- C. OS scheduling tasks
- D. I/O controllers

เฉลย: Assembly เป็น textual representation of instructions

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 12

**ข้อ 14 · อัตนัย: OS ในหน้า 11 มีหน้าที่บริการอะไร 3 กลุ่ม?**

เฉลย: ดูแล I/O; จัดการ memory/storage; scheduling tasks และ sharing resources

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 11

**ข้อ 15 · วิเคราะห์: เรียงลำดับตัวอย่างการแปล C ในภาพหน้า 12 และระบุเครื่องมือในแต่ละขั้น**

เฉลย: High-level C → Compiler → Assembly (RISC-V) → Assembler → Binary machine language (RISC-V)

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 12

### ส่วนประกอบคอมพิวเตอร์และโครงสร้างภายใน CPU

**ข้อ 16 · เลือกตอบ: ส่วนใดทำหน้าที่ data processing ใน CPU?**

- A. ALU
- B. Control Unit
- C. Power Supply Unit
- D. Motherboard

เฉลย: ALU ทำ data processing ส่วน Control Unit ควบคุมการทำงาน

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 14

**ข้อ 17 · อัตนัย: โครงสร้างภายใน CPU ที่หน้า 14 แบ่งไว้มีอะไรและทำหน้าที่อย่างไร?**

เฉลย: Control Unit ควบคุม; ALU ประมวลผล; Registers เก็บภายใน; CPU interconnection สื่อสารระหว่างส่วนเหล่านี้

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 14

**ข้อ 18 · วิเคราะห์: เหตุใด Registers กับ Memory (RAM) จึงไม่ควรถูกใช้แทนกันในสรุปนี้?**

เฉลย: หน้า 14 ระบุ registers เป็น internal storage ของ CPU ส่วนหน้า 13 จัด Memory (RAM) เป็นส่วนประกอบคอมพิวเตอร์แยกต่างหาก

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 13–14

### Machine Cycle และ Registers ใน CPU

**ข้อ 19 · เลือกตอบ: ลำดับใดตรง Machine Cycle ในสไลด์?**

- A. Fetch → Decode → Execute → Store
- B. Decode → Store → Fetch → Execute
- C. Store → Execute → Fetch → Decode
- D. Execute → Fetch → Store → Decode

เฉลย: ภาพหน้า 15 ให้ลำดับ Fetch–Decode–Execute–Store

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 15

**ข้อ 20 · อัตนัย: PC และ IR มีชื่อเต็มว่าอะไร และ register อีกกลุ่มที่หน้า 16 ระบุคืออะไร?**

เฉลย: Program counter; Instruction Register; อีกกลุ่มคือ Status register (status/flags)

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 16

**ข้อ 21 · วิเคราะห์: ในภาพ Machine Cycle ส่วนใดสัมพันธ์กับ Decode/Execute และผลลัพธ์ไปที่ใด?**

เฉลย: Decode สัมพันธ์กับ Control Unit; Execute กับ ALU; Store result ลง memory

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 15

### Cache Memory และระดับ L1 / L2 / L3

**ข้อ 22 · เลือกตอบ: ระดับใดถูกระบุว่าใกล้ core ที่สุด?**

- A. L1
- B. L3
- C. Main memory
- D. Storage Devices

เฉลย: L1 closest to the core ตามหน้า 18

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 18

**ข้อ 23 · อัตนัย: Cache ช่วยเร่ง memory access อย่างไรตามหน้า 18?**

เฉลย: นำข้อมูลจาก main memory ที่น่าจะใช้ในอนาคตใกล้มาไว้ใน cache ซึ่งเล็กกว่าและเร็วกว่า main memory

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 18

**ข้อ 24 · วิเคราะห์: จากภาพ shared L2 ในหน้า 17 สรุปได้หรือไม่ว่า CPU ทุกตัวต้องแชร์ L2 แบบเดียวกัน?**

เฉลย: ไม่ได้ ภาพแสดงตัวอย่าง layout ส่วนข้อความหน้า 18 อธิบายหลักการหลายระดับ ไม่ได้กำหนด layout เดียวสำหรับ CPU ทุกตัว

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 17–18

### Multi-core, Multi-thread และการมอง Motherboard → Core

**ข้อ 25 · เลือกตอบ: ตามหน้า 20 ข้อใดอธิบาย Multi-core?**

- A. Hardware ทางกายภาพที่มีอยู่จริง
- B. จำนวนแขนของเชฟแต่ละคน
- C. Cloud Storage
- D. Assembly representation

เฉลย: Multi-core ถูกอธิบายเป็น hardware ทางกายภาพที่แยกงานแบบ parallel

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 20

**ข้อ 26 · อัตนัย: อุปมาเชฟและแขนในสไลด์ใช้แยกอะไร?**

เฉลย: จำนวนเชฟ = จำนวน core; จำนวนแขนของเชฟแต่ละคน = thread ตามการเปรียบเทียบในหน้า 20

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 20

**ข้อ 27 · วิเคราะห์: เรียงระดับภาพหน้า 21 และยกองค์ประกอบภายใน Core**

เฉลย: Motherboard → Processor chip → Core; ใน Core มี instruction logic, ALU, load/store logic และ L1/L2 instruction/data caches

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 21

### Manufacturing ICs, Yield และตัวอย่าง Wafer

**ข้อ 28 · เลือกตอบ: Yield ในหน้า 24 หมายถึงอะไร?**

- A. สัดส่วน working dies ต่อ wafer
- B. Clock cycles ต่อ instruction
- C. จำนวน threads ต่อ core
- D. ความถี่ clock ต่อวินาที

เฉลย: Yield คือ proportion of working dies per wafer

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 24

**ข้อ 29 · อัตนัย: หลังได้ patterned wafers กระบวนการหลักในภาพมีอะไรต่อ?**

เฉลย: Wafer tester → tested wafer → dicer → tested dies → bond die to package → packaged dies → part tester → tested packaged dies → ship

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 24

**ข้อ 30 · วิเคราะห์: หากจำว่า chip ในตัวอย่างกว้าง 300 mm ผิดตรงไหน?**

เฉลย: 300 mm เป็น wafer ส่วน chip มีขนาด 20.7 × 10.5 mm ตามตัวอย่างหน้า 25

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 25

### อ่านกราฟ Single Processor Performance

**ข้อ 31 · เลือกตอบ: อัตราการเติบโตช่วงท้ายที่กราฟกำกับคือค่าใด?**

- A. 3.5%/year
- B. 52%/year
- C. 25%/year
- D. 23%/year

เฉลย: บริเวณปลายกราฟกำกับ 3.5%/year

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 26

**ข้อ 32 · อัตนัย: กราฟครอบคลุมปีใด และแสดงชุดอัตราการเติบโตอะไร?**

เฉลย: ปี 1978–2018; 25%, 52%, 23%, 12%, 3.5% ต่อปีตามลำดับช่วงในภาพ

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 26

**ข้อ 33 · วิเคราะห์: กราฟที่มีอัตราเติบโตลดลงช่วงท้ายหมายความว่า performance ลดลงหรือไม่?**

เฉลย: ไม่จำเป็น และในภาพนี้ค่าระดับ performance ยังเพิ่มขึ้น เพียงอัตราการเพิ่มต่ำลง ต้องดูทั้งตำแหน่งจุดและอัตราที่กำกับ

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 26

### RISC vs CISC Architecture

**ข้อ 34 · เลือกตอบ: RISC มีชื่อเต็มใด?**

- A. Reduced Instruction Set Computing
- B. Complex Instruction Set Computing
- C. Request-Level Parallelism
- D. Instruction-Level Parallelism

เฉลย: RISC = Reduced Instruction Set Computing

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 27

**ข้อ 35 · อัตนัย: เส้นทางหลัง Program Memory สองฝั่งของภาพต่างกันตรงไหน?**

เฉลย: ฝั่งซ้ายผ่าน IR แล้ว Decoder ส่วนฝั่งขวาผ่าน mPC แล้ว mPM ก่อนส่วนที่เชื่อมไป Data path

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 27

**ข้อ 36 · วิเคราะห์: จากหน้า 27 เพียงหน้าเดียว สรุปว่า CISC เร็วกว่า RISC เสมอได้หรือไม่?**

เฉลย: ไม่ได้ สไลด์ให้ชื่อเต็มและภาพเส้นทางควบคุม แต่ไม่มีผล benchmark หรือข้อมูลเวลา/จำนวนคำสั่งสำหรับข้อสรุปนั้น

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 27

### Application Parallelism กับ Architectural Parallelism

**ข้อ 37 · เลือกตอบ: ข้อใดเป็นคู่ประเภทใน applications ตามหน้า 32?**

- A. DLP และ Task-Level Parallelism
- B. ILP และ Request-Level Parallelism
- C. Thread-Level และ Vector architectures
- D. SISD และ MIMD

เฉลย: Applications ระบุ DLP และ Task-Level Parallelism (TLP)

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 32

**ข้อ 38 · อัตนัย: Architectural parallelism มี 4 รายการใด?**

เฉลย: Instruction-Level Parallelism; Vector architectures/GPUs; Thread-Level Parallelism; Request-Level Parallelism

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 32

**ข้อ 39 · วิเคราะห์: ถ้าขยาย TLP ในรายการ applications ว่า Thread-Level จะตรงสไลด์หรือไม่?**

เฉลย: ไม่ตรง เพราะ TLP ในรายการ applications ถูกขยายเป็น Task-Level ส่วน Thread-Level อยู่ในรายการ architectural อีกกลุ่มหนึ่ง

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 32

### Flynn’s Taxonomy: SISD / SIMD / MISD / MIMD

**ข้อ 40 · เลือกตอบ: Single instruction stream กับ multiple data streams เรียกว่าอะไร?**

- A. SIMD
- B. SISD
- C. MISD
- D. MIMD

เฉลย: SIMD = Single instruction stream, multiple data streams

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 33

**ข้อ 41 · อัตนัย: สรุป SISD, SIMD, MISD, MIMD และชนิดย่อย MIMD ที่หน้า 33 ให้**

เฉลย: SISD single/single; SIMD single/multiple; MISD multiple/single; MIMD multiple/multiple; MIMD มี tightly-coupled และ loosely-coupled

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 33

**ข้อ 42 · วิเคราะห์: เหตุใดจึงจัด GPUs ในกลุ่ม SIMD เมื่อทำแบบฝึกจากสไลด์นี้?**

เฉลย: เพราะหน้า 33 วาง graphics processor units เป็นตัวอย่างใต้ SIMD โดยตรง คำตอบนี้อ้างการจัดกลุ่มในสไลด์ ไม่ขยายกลไก GPU นอกเอกสาร

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 33

### System Level Architecture Patterns

**ข้อ 43 · เลือกตอบ: รูปแบบใดมี independently deployable services?**

- A. Micro services
- B. Monolithic
- C. SISD
- D. RISC

เฉลย: Micro services ถูกอธิบายว่า modular และ independently deployable

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 34

**ข้อ 44 · อัตนัย: จับคู่ความหมายสั้น ๆ ของทั้ง 4 patterns**

เฉลย: Monolithic ระบบรวม; Client-server แยก requesting/serving; Distributed กระจาย computation บน networked machines; Micro services เป็น modular services ที่ deploy แยกได้

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 34

**ข้อ 45 · วิเคราะห์: คำอธิบาย Client-server กับ Distributed systems เน้นต่างกันตรงไหนตามสไลด์?**

เฉลย: Client-server เน้นการแบ่งบทบาท requesting กับ serving ส่วน Distributed systems เน้น computation ที่กระจายข้าม networked machines

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 34

### Performance และ Relative Performance

**ข้อ 46 · เลือกตอบ: สูตรใดตรงกับ Performance_X/Performance_Y?**

- A. ExecutionTime_Y/ExecutionTime_X
- B. ExecutionTime_X/ExecutionTime_Y
- C. ExecutionTime_X × ExecutionTime_Y
- D. ExecutionTime_X + ExecutionTime_Y

เฉลย: Performance เป็นส่วนกลับของเวลา จึงกลับตำแหน่งเวลาของ X/Y

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 36

**ข้อ 47 · คำนวณ: โปรแกรมใช้เวลา 10 s บน A และ 15 s บน B เครื่องใดเร็วกว่าและกี่เท่า?**

เฉลย: A เร็วกว่า B: Time_B/Time_A = 15/10 = 1.5 เท่า ตามตัวอย่างเดิม

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 36

**ข้อ 48 · วิเคราะห์: เมื่อ A ใช้เวลาน้อยกว่า B ทำไม Performance_A/Performance_B จึงมากกว่า 1?**

เฉลย: เพราะ Performance = 1/Time และอัตราส่วน performance กลายเป็น Time_B/Time_A ซึ่งตัวตั้งมากกว่าตัวหารในตัวอย่างนี้

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 36

### Elapsed Time, CPU Time และ Clock

**ข้อ 49 · เลือกตอบ: Elapsed time รวมรายการใดตามหน้า 37?**

- A. Processing, I/O, OS overhead, idle time
- B. เฉพาะ user CPU time
- C. เฉพาะ system CPU time
- D. เฉพาะจำนวน instructions

เฉลย: Elapsed time เป็น total response time รวมทั้งสี่กลุ่มตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 37

**ข้อ 50 · คำนวณ: แปลงตัวอย่าง 250 ps เป็น ns และ 4.0 GHz เป็น Hz**

เฉลย: 250 ps = 0.25 ns = 250 × 10⁻¹² s; 4.0 GHz = 4.0 × 10⁹ Hz (และเท่ากับ 4000 MHz)

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 38

**ข้อ 51 · วิเคราะห์: CPU time นับ system CPU time หรือไม่ และต่างจาก elapsed time ตรงไหน?**

เฉลย: นับทั้ง user CPU time และ system CPU time แต่ตัด I/O time และส่วนเวลาของงานอื่น; elapsed time นับเวลาตอบสนองรวมตามรายการหน้า 37

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 37

### CPU Time และโจทย์ออกแบบ Clock Rate

**ข้อ 52 · เลือกตอบ: สมการ CPU Time ใดตรงสไลด์?**

- A. CPU Clock Cycles / Clock Rate
- B. CPU Clock Cycles × Clock Rate
- C. Clock Rate / CPU Clock Cycles
- D. Clock Rate + Clock Cycles

เฉลย: CPU Time = cycles/rate หรือ cycles × cycle time

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 39

**ข้อ 53 · คำนวณ: ใช้ข้อมูลต้นฉบับ A: 2 GHz, 10 s; B: cycles มากขึ้น 1.2 เท่า ต้องใช้เวลา 6 s จงหา cycles_A, cycles_B และ rate_B**

เฉลย: cycles_A = 20 × 10⁹; cycles_B = 24 × 10⁹; rate_B = 24 × 10⁹/6 = 4 × 10⁹ Hz = 4 GHz

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 40

**ข้อ 54 · วิเคราะห์: เพราะเหตุใดการเพิ่ม clock rate อย่างเดียวจึงยังต้องดูจำนวน cycles?**

เฉลย: CPU Time ขึ้นกับ cycles/rate และสไลด์ระบุ trade-off ระหว่าง clock rate กับ cycle count; ในตัวอย่าง B เพิ่ม rate แต่ทำให้ cycles เพิ่ม 1.2 เท่า

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 39–40

### Instruction Count, CPI และการเปรียบเทียบ CPU

**ข้อ 55 · เลือกตอบ: Instruction Count ถูกกำหนดโดยกลุ่มใดตามหน้า 41?**

- A. Program, ISA, compiler
- B. เฉพาะ clock rate
- C. เฉพาะ power supply
- D. เฉพาะจำนวน cache levels

เฉลย: Instruction Count ขึ้นกับ program, ISA และ compiler

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 41

**ข้อ 56 · คำนวณ: จากตัวอย่าง A: 250 ps/CPI 2.0 และ B: 500 ps/CPI 1.2 โดยใช้ I เท่ากัน จงเปรียบเทียบความเร็ว**

เฉลย: Time_A = I × 500 ps; Time_B = I × 600 ps; Time_B/Time_A = 1.2 ดังนั้น A เร็วกว่า B 1.2 เท่า

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 42

**ข้อ 57 · วิเคราะห์: B มี CPI 1.2 ต่ำกว่า A ที่ 2.0 เหตุใด B จึงยังช้ากว่าในตัวอย่าง?**

เฉลย: B มี cycle time 500 ps ซึ่งมากกว่า A 250 ps เมื่อคูณ CPI แล้ว B ใช้ 600 ps ต่อ instruction เทียบกับ A 500 ps โดยตัวอย่างใช้ IC เท่ากัน

อ้างอิง: itds-211_comp_arch_Chapter01.pdf, หน้า 41–42

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- Cloud: ชั้นที่ Client/CSP ดูแล: แผนภาพเปรียบเทียบ Traditional IT, IaaS, PaaS, SaaS และ trade-off ตามต้นฉบับ (itds-211_comp_arch_Chapter01.pdf, หน้า 8)
- Eight Great Ideas: รายชื่อแนวคิดออกแบบทั้ง 8 ข้อ โดยต้นฉบับไม่ได้ขยายกลไกของทุกข้อ (itds-211_comp_arch_Chapter01.pdf, หน้า 10)
- ชั้น Application / System / Hardware: ภาพวงซ้อนและหน้าที่ของ Compiler, OS และ Hardware (itds-211_comp_arch_Chapter01.pdf, หน้า 11)
- High-level → Assembly → Binary: ตัวอย่าง C swap ผ่าน Compiler และ Assembler ไปยัง RISC-V representations (itds-211_comp_arch_Chapter01.pdf, หน้า 12)
- ส่วนประกอบคอมพิวเตอร์: รายการองค์ประกอบและภาพ Processor/Memory/Input/Output (itds-211_comp_arch_Chapter01.pdf, หน้า 13)
- Fetch–Decode–Execute–Store: ลำดับ 4 ขั้น เชื่อม Control Unit, ALU และ Memory (itds-211_comp_arch_Chapter01.pdf, หน้า 15)
- Registers และภาพภายใน CPU: PC, IR, Status register พร้อมภาพ ALU, Control Unit และหน่วยความจำ (itds-211_comp_arch_Chapter01.pdf, หน้า 16)
- ระดับและการแชร์ Cache: ตัวอย่าง L1/L2 และ Smart-Shared L2 Cache เป็น layout ที่สไลด์ยกตัวอย่าง (itds-211_comp_arch_Chapter01.pdf, หน้า 17)
- Multi-core VS Multi-thread: ภาพเปรียบเทียบ hardware cores กับการแบ่งงานตามคำอธิบายต้นฉบับ (itds-211_comp_arch_Chapter01.pdf, หน้า 19)
- Motherboard → Processor chip → Core: ภาพขยายสามระดับ พร้อมตำแหน่ง cache และส่วนประกอบใน core (itds-211_comp_arch_Chapter01.pdf, หน้า 21)
- บอร์ด Two Quad-Core Xeon: ภาพ motherboard ตัวอย่างที่ใช้ Intel quad-core Xeon processors สองตัว (itds-211_comp_arch_Chapter01.pdf, หน้า 22)
- Inside the Processor: Apple A5: ภาพตัวอย่างองค์ประกอบบน Apple A5 ตามป้ายในสไลด์ (itds-211_comp_arch_Chapter01.pdf, หน้า 23)
- กระบวนการ Manufacturing ICs: ลำดับจาก silicon ingot ถึง packaged dies ที่ทดสอบแล้ว พร้อมนิยาม Yield (itds-211_comp_arch_Chapter01.pdf, หน้า 24)
- Intel Core i7 Wafer: ตัวอย่าง wafer 300 mm, 280 chips, 32 nm และ chip 20.7 × 10.5 mm (itds-211_comp_arch_Chapter01.pdf, หน้า 25)
- กราฟ Single Processor Performance: กราฟช่วงปี 1978–2018 และอัตราเติบโตที่กำกับ ไม่ใช่ข้อมูลหลังช่วงในกราฟ (itds-211_comp_arch_Chapter01.pdf, หน้า 26)
- แผนภาพ RISC vs CISC: ชื่อเต็มและเส้นทาง IR/Decoder เทียบกับ mPC/mPM; คำขยาย mPM ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter01.pdf, หน้า 27)
- ARM ใน Embedded Systems: ภาพคำอธิบาย ARM ที่เชื่อมกับหลัก RISC, small die size และ low power (itds-211_comp_arch_Chapter01.pdf, หน้า 29)
- ARM Products: รายการ Cortex-A/Cortex-A50, Cortex-R และ Cortex-M ตามสไลด์ (itds-211_comp_arch_Chapter01.pdf, หน้า 30)
- Microcontroller chip based on Cortex-M3: ภาพโครงสร้างตัวอย่าง Cortex-M3 พร้อมข้อความเรื่อง interrupt, low power, debug/trace (itds-211_comp_arch_Chapter01.pdf, หน้า 31)
- Flynn’s Taxonomy: การจำแนก SISD/SIMD/MISD/MIMD และตัวอย่างที่สไลด์จัดให้ (itds-211_comp_arch_Chapter01.pdf, หน้า 33)
- สมการ Relative Performance: สมการส่วนกลับของ Execution Time และตัวอย่าง A 10 s, B 15 s (itds-211_comp_arch_Chapter01.pdf, หน้า 36)
- Clock period และ Clock rate: ภาพ clock cycles พร้อมตัวอย่าง 250 ps และ 4.0 GHz (itds-211_comp_arch_Chapter01.pdf, หน้า 38)
- สมการ CPU Time: CPU Time = cycles × cycle time = cycles / rate และ trade-off (itds-211_comp_arch_Chapter01.pdf, หน้า 39)
- โจทย์ Clock Rate ของ Computer B: วิธีคำนวณต้นฉบับจาก A 2 GHz/10 s ไป B 6 s ที่ใช้ cycles เพิ่ม 1.2 เท่า (itds-211_comp_arch_Chapter01.pdf, หน้า 40)
- Instruction Count และ CPI: สมการ Clock Cycles และ CPU Time พร้อมปัจจัยที่กำหนด IC/CPI (itds-211_comp_arch_Chapter01.pdf, หน้า 41)
- โจทย์เปรียบเทียบ CPI ของ A/B: ตัวอย่างต้นฉบับที่ A ใช้ 500I ps, B ใช้ 600I ps และ A เร็วกว่า 1.2 เท่า (itds-211_comp_arch_Chapter01.pdf, หน้า 42)
