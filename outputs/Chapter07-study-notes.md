# Chapter07 · Computing Unit (Pipelining)

ITDS-211 · Computer Architecture & Operating System · W. Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter07.pdf** จำนวน 53 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter07 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/คำนวณ/วิเคราะห์ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 25 หัวข้อ · 🔴 ต้องจำแน่นอน 18 หัวข้อ (72.0%) · 🟡 สำคัญ 6 หัวข้อ (24.0%) · ⚪ อ่านเสริม 1 หัวข้อ (4.0%) · แบบฝึก 75 ข้อ · Flashcard 43 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter07 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| Pipelining analogy: ซักผ้าแบบซ้อนงาน | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 3 |
| RISC-V pipeline 5 ขั้น | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 4 |
| Pipeline performance: single-cycle เทียบ pipelined | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 5–6 |
| Pipelining และการออกแบบ ISA | 🟡 สำคัญ | itds-211_comp_arch_Chapter07.pdf, หน้า 7 |
| Hazards 3 ชนิด | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 8 |
| Structure hazard และการแยก memory | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 9 |
| Data hazard และ forwarding (bypassing) | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 10–11 |
| Load-use data hazard | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 12 |
| Code scheduling เพื่อหลบ stall | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 13 |
| Control hazard และ stall on branch | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 14–15 |
| Branch prediction: static และ dynamic | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 16–17 |
| Pipeline summary: throughput และ latency | 🟡 สำคัญ | itds-211_comp_arch_Chapter07.pdf, หน้า 18 |
| Pipelined datapath และ pipeline registers | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 19–20 |
| Pipeline operation ของ load และ datapath ที่แก้แล้ว | 🟡 สำคัญ | itds-211_comp_arch_Chapter07.pdf, หน้า 21–27 |
| Pipeline operation ของ store | 🟡 สำคัญ | itds-211_comp_arch_Chapter07.pdf, หน้า 28–30 |
| Multi-cycle และ single-cycle pipeline diagrams | 🟡 สำคัญ | itds-211_comp_arch_Chapter07.pdf, หน้า 31–33 |
| Pipelined control (simplified) | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter07.pdf, หน้า 34 |
| Data hazards ในคำสั่ง ALU และ dependencies | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 35–36 |
| การตรวจจับว่าต้อง forward | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 37–38 |
| Forwarding paths และ ForwardA/ForwardB | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 39–40 |
| Double data hazard และ revised forwarding condition | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 41–43 |
| Load-use hazard detection และการ stall | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 44–47 |
| Stalls และ performance | 🟡 สำคัญ | itds-211_comp_arch_Chapter07.pdf, หน้า 48 |
| Branch hazards: ตัดสินใน MEM และ flush | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 49 |
| Reducing branch delay: ย้ายการตัดสินไป ID | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter07.pdf, หน้า 50–52 |

### บทนี้เรียนเพื่ออะไร

บทนี้เรียนเพื่อเข้าใจว่า pipelining ทำให้ CPU ทำคำสั่งซ้อนกันเพื่อเพิ่ม throughput อย่างไร, hazards แบบ structure/data/control เกิดจากอะไร และ datapath ของ RISC-V แก้ด้วย forwarding, stall, flush และ branch prediction อย่างไร

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 2–52

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- อธิบายแนวคิด pipelining, 5 ขั้นของ RISC-V และเทียบ Tc ของ single-cycle กับ pipelined (itds-211_comp_arch_Chapter07.pdf, หน้า 3–7, 18)
- จำแนก structure/data/control hazards และวิธีรับมือเบื้องต้น (itds-211_comp_arch_Chapter07.pdf, หน้า 8–17)
- ตามการไหลของ ld/sd ผ่าน pipelined datapath และ pipeline registers (itds-211_comp_arch_Chapter07.pdf, หน้า 19–34)
- เขียนเงื่อนไข forwarding, ค่า ForwardA/B และการตรวจ load-use hazard (itds-211_comp_arch_Chapter07.pdf, หน้า 35–48)
- อธิบาย branch hazard, flush และการย้ายการตัดสิน branch ไป ID (itds-211_comp_arch_Chapter07.pdf, หน้า 49–52)

วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจาก course outline หน้า 2 (computing units – Pipelining) และเนื้อหาหน้า 3–52

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- อ่านและตรวจภาพครบ 53 หน้า: หน้า 1 ปก, หน้า 2 course outline, หน้า 53 Q&A
- สไลด์ไม่มีรายการ Chapter Objectives โดยตรงหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; ระดับสีเป็นลำดับเวลาอ่าน ไม่ใช่สถิติการออกสอบ
- หน้า 44 เงื่อนไข load-use เขียน IF/ID.RegisterRs1 ซ้ำสองครั้ง (คาดว่าควรมี Rs2): ต้องตรวจสอบจากต้นฉบับ
- หน้า 49 ใช้ beq x1,x0,16 และ 72 ld x4,100(x7) ส่วนหน้า 50–52 ใช้ beq x1,x3,16 และ ld x4,50(x7): ต้องตรวจสอบจากต้นฉบับ
- สูตร non-stop speedup หน้า 3 พิมพ์ “2n/0.5n + 1.5 ≈ 4” ตามภาพ; การจัดวงเล็บของนิพจน์: ต้องตรวจสอบจากต้นฉบับ
- หน้า 34 แสดงเฉพาะตำแหน่งสัญญาณควบคุม ไม่มีตารางค่าสัญญาณรายคำสั่ง
- คำถามคำนวณใช้เฉพาะตัวเลขในสไลด์; ไม่มีการอ้างว่าเป็นข้อสอบจริง

## 2. สรุปรายบทและหัวข้อ

### 1. Pipelining analogy: ซักผ้าแบบซ้อนงาน

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 3**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

สไลด์อธิบาย pipelining ด้วยการซักผ้าที่ซ้อนขั้นตอนกัน (overlapping execution) ทำให้งานหลายชิ้นอยู่คนละขั้นพร้อมกัน. parallelism แบบนี้เพิ่มประสิทธิภาพ: งานซัก 4 load ใช้ speedup 8/3.5 ≈ 2.3 และถ้าทำต่อเนื่องไม่หยุด speedup จะเข้าใกล้จำนวนขั้น (number of stages).

**ประเด็นที่ต้องจำ**

- Pipelined laundry = overlapping execution (หน้า 3)
- Parallelism improves performance (หน้า 3)
- 4 loads: speedup = 8/3.5 = 2.3 (หน้า 3)
- Non-stop: speedup ≈ 4 = number of stages (หน้า 3)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- pipelining
- overlapping execution
- parallelism
- speedup
- number of stages

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 3 บนคือทำทีละ load (เรียงต่อกัน) ภาพล่างคือ load ถัดไปเริ่มเมื่อขั้นแรกว่าง

**สูตรที่ต้องรู้**

```text
Speedup (4 loads) = 8 / 3.5 ≈ 2.3
```

ตัวเลขตามตัวอย่างซักผ้าหน้า 3

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 3

**สูตรที่ต้องรู้**

```text
Non-stop speedup ≈ number of stages (≈ 4)
```

กรณีงานไหลต่อเนื่องจำนวนมากตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 3

**จุดที่อาจสับสน:** สูตร non-stop บนสไลด์พิมพ์เป็น “2n/0.5n + 1.5 ≈ 4” ซึ่งต้องอ่านเป็นนิพจน์ตามภาพ; ความหมายที่สไลด์ยืนยันคือ speedup เข้าใกล้จำนวนขั้น

**ประโยคช่วยจำ:** ซ้อนขั้นได้กี่ขั้น เร็วขึ้นได้ราวเท่านั้น

### 2. RISC-V pipeline 5 ขั้น

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 4**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

RISC-V pipeline แบ่งการทำคำสั่งเป็น 5 ขั้น ขั้นละหนึ่ง step: IF ดึงคำสั่งจากหน่วยความจำ, ID ถอดรหัสและอ่าน register, EX คำนวณหรือคำนวณ address, MEM เข้าถึง operand ในหน่วยความจำ และ WB เขียนผลกลับ register. ชื่อขั้นเหล่านี้ใช้ต่อในทุกภาพและชื่อ pipeline register ของบท.

**ประเด็นที่ต้องจำ**

- IF: Instruction fetch from memory (หน้า 4)
- ID: Instruction decode & register read (หน้า 4)
- EX: Execute operation or calculate address (หน้า 4)
- MEM: Access memory operand (หน้า 4)
- WB: Write result back to register (หน้า 4)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- IF
- ID
- EX
- MEM
- WB
- stage

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ld ใช้ครบ 5 ขั้น: fetch → decode/อ่าน register → คำนวณ address → อ่าน memory → เขียน register

**จุดที่อาจสับสน:** EX ของ load/store คือคำนวณ address ไม่ใช่การอ่าน memory; การอ่าน/เขียน memory เกิดใน MEM

**ประโยคช่วยจำ:** ดึง–ถอด–ทำ–จำ–เขียน (IF–ID–EX–MEM–WB)

### 3. Pipeline performance: single-cycle เทียบ pipelined

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 5–6**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

สไลด์สมมติเวลา 100ps สำหรับอ่าน/เขียน register และ 200ps สำหรับขั้นอื่น. คำสั่งแต่ละชนิดใช้เวลารวมต่างกัน (ld 800ps, sd 700ps, R-format 600ps, beq 500ps) ดังนั้น single-cycle ต้องใช้ clock ยาวตามคำสั่งที่ช้าสุด Tc = 800ps ส่วน pipelined ใช้ Tc = 200ps ตามขั้นที่ช้าที่สุด.

**ประเด็นที่ต้องจำ**

- Register read/write = 100ps; ขั้นอื่น = 200ps (หน้า 5)
- ld 800ps, sd 700ps, R-format 600ps, beq 500ps (หน้า 5)
- Single-cycle Tc = 800ps; Pipelined Tc = 200ps (หน้า 6)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- clock cycle time (Tc)
- single-cycle datapath
- pipelined datapath
- ps (picosecond)

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ในภาพหน้า 6 คำสั่ง ld ถัดไปเริ่มทุก 800ps ใน single-cycle แต่เริ่มทุก 200ps ใน pipelined

**สูตรที่ต้องรู้**

```text
Single-cycle Tc = 800ps
Pipelined Tc = 200ps
```

ค่า Tc จากภาพหน้า 6; อัตราส่วนเวลาระหว่างการเริ่มคำสั่ง 800/200 = 4 คำนวณจากตัวเลขในสไลด์

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 6

| คำสั่ง | IF | Reg read | ALU | MEM | Reg write | รวม |
| --- | --- | --- | --- | --- | --- | --- |
| ld | 200 | 100 | 200 | 200 | 100 | 800ps |
| sd | 200 | 100 | 200 | 200 | – | 700ps |
| R-format | 200 | 100 | 200 | – | 100 | 600ps |
| beq | 200 | 100 | 200 | – | – | 500ps |

**จุดที่อาจสับสน:** Pipelined ไม่ได้ทำให้คำสั่งเดียวเสร็จเร็วขึ้น แต่ทำให้คำสั่งถัดไปเริ่มได้ถี่ขึ้น

**ประโยคช่วยจำ:** single รอตัวช้าสุดทั้งคำสั่ง; pipeline รอขั้นช้าสุดขั้นเดียว

### 4. Pipelining และการออกแบบ ISA

**🟡 สำคัญ** · itds-211_comp_arch_Chapter07.pdf, **หน้า 7**

เหตุผลการจัดระดับ: เป็นภาพการไหลของคำสั่งและการประยุกต์กลไกหลักกับคำสั่งจริง

RISC-V ISA ถูกออกแบบมาให้ทำ pipeline ได้ง่าย: ทุกคำสั่งยาว 32 บิต ทำให้ fetch และ decode ได้ในรอบเดียว (ต่างจาก x86 ที่ยาว 1–17 ไบต์), รูปแบบคำสั่งน้อยและสม่ำเสมอจึง decode และอ่าน register ได้ในขั้นเดียว, และใช้ load/store addressing จึงคำนวณ address ในขั้นที่ 3 แล้วเข้าถึง memory ในขั้นที่ 4.

**ประเด็นที่ต้องจำ**

- All instructions are 32-bits (หน้า 7)
- c.f. x86: 1- to 17-byte instructions (หน้า 7)
- Few and regular formats → decode + read registers in one step (หน้า 7)
- Load/store addressing → address ในขั้นที่ 3, memory ในขั้นที่ 4 (หน้า 7)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- ISA
- instruction format
- load/store addressing
- x86

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบกับ x86 ที่ความยาวคำสั่งไม่คงที่ ทำให้ fetch/decode ในรอบเดียวยากกว่า

**จุดที่อาจสับสน:** ขั้นที่ 3 = EX (คำนวณ address) และขั้นที่ 4 = MEM ไม่ใช่กลับกัน

**ประโยคช่วยจำ:** ยาวเท่ากัน รูปแบบน้อย load/store ชัด → pipeline ง่าย

### 5. Hazards 3 ชนิด

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 8**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

Hazard คือสถานการณ์ที่ทำให้เริ่มคำสั่งถัดไปในรอบถัดไปไม่ได้. สไลด์แบ่งเป็น structure hazard (ทรัพยากรที่ต้องใช้ไม่ว่าง), data hazard (ต้องรอคำสั่งก่อนหน้าอ่าน/เขียนข้อมูลให้เสร็จ) และ control hazard (การตัดสินใจ control ขึ้นกับคำสั่งก่อนหน้า).

**ประเด็นที่ต้องจำ**

- Hazard = prevents starting the next instruction in the next cycle (หน้า 8)
- Structure: required resource is busy (หน้า 8)
- Data: wait for previous instruction’s data read/write (หน้า 8)
- Control: control action depends on previous instruction (หน้า 8)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- hazard
- structure hazard
- data hazard
- control hazard

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ตารางเปรียบเทียบด้านล่างจับคู่ “สาเหตุ” กับชนิด hazard

| ชนิด | สาเหตุตามสไลด์ | ตัวอย่างในบท |
| --- | --- | --- |
| Structure | resource ไม่ว่าง | single memory (หน้า 9) |
| Data | รอข้อมูลจากคำสั่งก่อน | add x19 → sub ใช้ x19 (หน้า 10) |
| Control | control ขึ้นกับคำสั่งก่อน | branch (หน้า 14) |

**จุดที่อาจสับสน:** Data hazard เกี่ยวกับค่าข้อมูลที่ยังไม่พร้อม; control hazard เกี่ยวกับการเลือกคำสั่งถัดไป (เช่น branch)

**ประโยคช่วยจำ:** ของไม่ว่าง–ข้อมูลไม่พร้อม–ไม่รู้ทางไป

### 6. Structure hazard และการแยก memory

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 9**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

Structure hazard คือการแย่งใช้ทรัพยากร. ใน RISC-V pipeline ที่มี memory เดียว load/store ต้องเข้าถึงข้อมูล ทำให้ instruction fetch ต้อง stall ในรอบนั้นและเกิด pipeline “bubble”. ดังนั้น pipelined datapath ต้องแยก instruction/data memory หรือแยก instruction/data cache.

**ประเด็นที่ต้องจำ**

- Conflict for use of a resource (หน้า 9)
- Single memory: load/store data access ชน instruction fetch → stall/bubble (หน้า 9)
- แก้ด้วย separate instruction/data memories หรือ caches (หน้า 9)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- structure hazard
- stall
- bubble
- separate instruction/data memory
- instruction/data cache

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ถ้า ld อยู่ขั้น MEM พร้อมกับอีกคำสั่งอยู่ขั้น IF และมี memory เดียว ทั้งสองต้องใช้ memory ในรอบเดียวกัน

**จุดที่อาจสับสน:** Bubble คือรอบที่ไม่มีงานจริงจาก stall ไม่ใช่คำสั่งใหม่

**ประโยคช่วยจำ:** memory เดียวชนกัน → แยกคำสั่ง/ข้อมูล

### 7. Data hazard และ forwarding (bypassing)

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 10–11**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

Data hazard เกิดเมื่อคำสั่งหนึ่งต้องรอการเข้าถึงข้อมูลของคำสั่งก่อนหน้า เช่น add x19,x0,x1 แล้ว sub x2,x19,x3 ต้องใช้ x19. ถ้ารอจนเขียน register ก็ต้องแทรก bubble หลายรอบ (ภาพหน้า 10). Forwarding (bypassing) ใช้ผลทันทีที่คำนวณเสร็จโดยไม่รอเก็บลง register แต่ต้องเพิ่มเส้นทางใน datapath.

**ประเด็นที่ต้องจำ**

- ตัวอย่าง add x19,x0,x1 → sub x2,x19,x3 (หน้า 10)
- Forwarding: use result when it is computed (หน้า 11)
- Don’t wait for it to be stored in a register (หน้า 11)
- Requires extra connections in the datapath (หน้า 11)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- data hazard
- forwarding
- bypassing
- dependency
- bubble

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 11: ผลจาก EX ของ add x1,x2,x3 ส่งตรงเข้าขั้น EX ของ sub x4,x1,x5

**จุดที่อาจสับสน:** Forwarding ไม่ได้ลบ dependency แต่ส่งค่าเร็วขึ้น; บางกรณีก็ยังต้อง stall (ดูหน้า 12)

**ประโยคช่วยจำ:** ได้ผลแล้วส่งเลย ไม่ต้องรอเข้าทะเบียน

### 8. Load-use data hazard

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 12**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

Forwarding ไม่สามารถกำจัด stall ได้ทุกครั้ง: ถ้าค่ายังคำนวณไม่ได้ในเวลาที่ต้องใช้ ก็ส่งย้อนเวลาไม่ได้ (“Can’t forward backward in time!”). ตัวอย่าง ld x1,0(x2) แล้ว sub x4,x1,x5 ต้องรอค่าจาก MEM จึงต้องมี bubble หนึ่งรอบก่อน forward.

**ประเด็นที่ต้องจำ**

- Can’t always avoid stalls by forwarding (หน้า 12)
- If value not computed when needed (หน้า 12)
- Can’t forward backward in time (หน้า 12)
- ตัวอย่าง ld x1,0(x2) → sub x4,x1,x5 (หน้า 12)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- load-use hazard
- stall
- forwarding

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 12 ค่า x1 ได้หลัง MEM ของ ld จึงส่งให้ EX ของ sub ได้หลังแทรก bubble

**จุดที่อาจสับสน:** ld ได้ค่าใน MEM (ช้ากว่าคำสั่ง ALU ที่ได้ค่าใน EX) จึงต่างจาก data hazard ทั่วไปที่ forward ได้ทันที

**ประโยคช่วยจำ:** load ได้ของช้า ใช้ต่อทันทีต้องรอหนึ่งจังหวะ

### 9. Code scheduling เพื่อหลบ stall

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 13**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

คอมไพเลอร์สามารถเรียงโค้ดใหม่ไม่ให้ใช้ผลของ load ในคำสั่งถัดไปทันที. ตัวอย่าง C code a = b + e; c = b + f; ลำดับเดิมมี stall 2 จุด ใช้ 13 cycles; เมื่อย้าย ld x4,16(x0) ขึ้นมาก่อน add ลดเหลือ 11 cycles.

**ประเด็นที่ต้องจำ**

- Reorder code to avoid use of load result in the next instruction (หน้า 13)
- ลำดับเดิม: 2 stalls, 13 cycles (หน้า 13)
- ลำดับใหม่: ld x1, ld x2, ld x4, add, sd, add, sd = 11 cycles (หน้า 13)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- code scheduling
- reorder
- load-use
- stall

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ลำดับเดิม add x3,x1,x2 ใช้ x2 ทันทีหลัง ld x2 และ add x5,x1,x4 ใช้ x4 ทันทีหลัง ld x4 → 2 stalls

**ตัวอย่างจัดลำดับโค้ด (หน้า 13)**

1. ลำดับเดิม: ld x1 · ld x2 · add x3,x1,x2 (stall) · sd x3 · ld x4 · add x5,x1,x4 (stall) · sd x5 = 13 cycles
2. ย้าย ld x4,16(x0) ขึ้นไปก่อน add x3,x1,x2
3. ไม่มีคำสั่งใดใช้ผล load ในคำสั่งถัดไปทันที → 11 cycles

**คำตอบ:** ลดจาก 13 เหลือ 11 cycles

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 13

**จุดที่อาจสับสน:** การเรียงใหม่ต้องรักษาผลลัพธ์เดิม (a และ c ยังได้ค่าเดิม) ไม่ใช่สลับคำสั่งตามใจ

**ประโยคช่วยจำ:** โหลดไว้ก่อน ใช้ทีหลัง

### 10. Control hazard และ stall on branch

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 14–15**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

Branch กำหนดการไหลของโปรแกรม การ fetch คำสั่งถัดไปจึงขึ้นกับผล branch และ pipeline อาจ fetch คำสั่งที่ถูกไม่ได้ขณะ branch ยังอยู่ขั้น ID. RISC-V จึงเพิ่ม hardware เพื่อเปรียบเทียบ register และคำนวณ target ตั้งแต่ขั้น ID. วิธีง่ายสุดคือ stall รอจนรู้ผล branch ก่อน fetch ต่อ (ภาพหน้า 15).

**ประเด็นที่ต้องจำ**

- Fetching next instruction depends on branch outcome (หน้า 14)
- Compare registers and compute target early → add hardware in ID (หน้า 14)
- Stall on branch: wait until outcome determined (หน้า 15)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- control hazard
- branch outcome
- branch target
- stall on branch

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 15: add x4,x5,x6 → beq x1,x0,40 → or x7,x8,x9 ต้องรอ bubble ก่อน fetch or

**จุดที่อาจสับสน:** การย้ายการตัดสิน branch มาที่ ID ลดความล่าช้าได้แต่ไม่ได้ทำให้ไม่มีความล่าช้าเลย

**ประโยคช่วยจำ:** branch ยังไม่ชี้ทาง อย่าเพิ่งเดิน

### 11. Branch prediction: static และ dynamic

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 16–17**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

pipeline ที่ยาวขึ้นรู้ผล branch ได้ช้า stall penalty จึงรับไม่ได้ จึงทำนายผล branch และ stall เฉพาะเมื่อทำนายผิด. RISC-V ทำนาย branch not taken แล้ว fetch คำสั่งถัดไปทันที. Static prediction ใช้พฤติกรรมทั่วไป (backward taken, forward not taken) ส่วน dynamic prediction ให้ hardware จดประวัติจริงของแต่ละ branch และปรับเมื่อทำนายผิด.

**ประเด็นที่ต้องจำ**

- Predict outcome; only stall if prediction is wrong (หน้า 16)
- RISC-V: predict branches not taken (หน้า 16)
- Static: backward taken, forward not taken (หน้า 17)
- Dynamic: record recent history; when wrong, stall, re-fetch, update history (หน้า 17)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- branch prediction
- predict not taken
- static branch prediction
- dynamic branch prediction
- branch history

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** branch ของ loop มักกระโดดย้อนกลับ (backward) จึงทำนายว่า taken ตาม static prediction

| แบบ | พื้นฐาน | กฎ/การทำงาน |
| --- | --- | --- |
| Static | typical branch behavior | backward → taken, forward → not taken |
| Dynamic | วัดพฤติกรรมจริงด้วย hardware | จด history, ทำนายตามแนวโน้ม, ผิดแล้ว re-fetch + update |

**จุดที่อาจสับสน:** Static ไม่ได้ดูประวัติจริง; dynamic อาศัยประวัติที่ hardware วัด

**ประโยคช่วยจำ:** ย้อนกลับ=กระโดด, ไปข้างหน้า=ไม่กระโดด; dynamic จำประวัติ

### 12. Pipeline summary: throughput และ latency

**🟡 สำคัญ** · itds-211_comp_arch_Chapter07.pdf, **หน้า 18**

เหตุผลการจัดระดับ: เป็นภาพการไหลของคำสั่งและการประยุกต์กลไกหลักกับคำสั่งจริง

The BIG Picture: pipelining เพิ่มประสิทธิภาพด้วยการเพิ่ม instruction throughput โดยทำหลายคำสั่งขนานกัน แต่ latency ของแต่ละคำสั่งยังเท่าเดิม. pipeline ต้องรับมือ hazards (structure, data, control) และการออกแบบ instruction set มีผลต่อความซับซ้อนของการ implement pipeline.

**ประเด็นที่ต้องจำ**

- Increase instruction throughput (หน้า 18)
- Each instruction has the same latency (หน้า 18)
- Subject to structure, data, control hazards (หน้า 18)
- ISA design affects pipeline complexity (หน้า 18)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- throughput
- latency
- The BIG Picture

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เชื่อมกับหน้า 6: Tc ลดจาก 800 เป็น 200ps แต่คำสั่งหนึ่งยังผ่านครบ 5 ขั้น

**จุดที่อาจสับสน:** pipeline เพิ่ม throughput ไม่ได้ลด latency ของคำสั่งเดี่ยว

**ประโยคช่วยจำ:** ส่งงานออกถี่ขึ้น แต่งานชิ้นเดียวไม่ได้เสร็จเร็วขึ้น

### 13. Pipelined datapath และ pipeline registers

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 19–20**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

Datapath แบ่งเป็นช่วง IF, ID, EX, MEM, WB. การไหลจากขวาไปซ้าย (right-to-left flow) คือ WB เขียน register และ MEM เลือก PC ใหม่ (branch) ซึ่งนำไปสู่ hazards. ต้องมี pipeline registers ระหว่างขั้น (IF/ID, ID/EX, EX/MEM, MEM/WB) เพื่อเก็บข้อมูลที่ขั้นก่อนหน้าผลิตในรอบก่อน.

**ประเด็นที่ต้องจำ**

- Right-to-left flow leads to hazards (หน้า 19)
- Need registers between stages (หน้า 20)
- Hold information produced in previous cycle (หน้า 20)
- ชื่อ pipeline registers: IF/ID, ID/EX, EX/MEM, MEM/WB (หน้า 20)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- pipelined datapath
- pipeline register
- IF/ID
- ID/EX
- EX/MEM
- MEM/WB
- right-to-left flow

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 19 ชี้กล่อง MEM (ส่ง PC ใหม่ย้อนไป IF) และ WB (ส่งข้อมูลย้อนไป register file)

**จุดที่อาจสับสน:** ชื่อ pipeline register บอกขั้นสองฝั่ง เช่น ID/EX อยู่ระหว่าง ID กับ EX

**ประโยคช่วยจำ:** ย้อนทางเมื่อไร เสี่ยง hazard เมื่อนั้น

### 14. Pipeline operation ของ load และ datapath ที่แก้แล้ว

**🟡 สำคัญ** · itds-211_comp_arch_Chapter07.pdf, **หน้า 21–27**

เหตุผลการจัดระดับ: เป็นภาพการไหลของคำสั่งและการประยุกต์กลไกหลักกับคำสั่งจริง

สไลด์ใช้ single-clock-cycle diagram ไล่ ld ทีละขั้น: IF (หน้า 22), ID (หน้า 23), EX (หน้า 24), MEM (หน้า 25), WB (หน้า 26). ใน WB ภาพชี้ว่าใช้ “wrong register number” เพราะหมายเลข register ปลายทางที่ใช้ตอนนั้นมาจากคำสั่งที่อยู่ใน IF/ID แล้ว. Corrected datapath (หน้า 27) จึงส่งหมายเลข write register ไปกับ pipeline registers จนถึง WB.

**ประเด็นที่ต้องจำ**

- Single-clock-cycle diagram: แสดงการใช้ทรัพยากรในหนึ่งรอบ; multi-clock-cycle: กราฟตามเวลา (หน้า 21)
- ld ผ่าน IF→ID→EX→MEM→WB (หน้า 22–26)
- WB for Load: wrong register number (หน้า 26)
- Corrected datapath ส่ง write register number ไปตาม pipeline (หน้า 27)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- single-clock-cycle diagram
- multi-clock-cycle diagram
- write register
- corrected datapath

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูส่วนที่ระบายสีฟ้าในภาพแต่ละหน้าเพื่อตามว่าขั้นนั้นใช้หน่วยใด

**จุดที่อาจสับสน:** ข้อผิดในหน้า 26 ไม่ได้อยู่ที่ข้อมูลที่เขียน แต่อยู่ที่หมายเลข register ปลายทาง

**ประโยคช่วยจำ:** หมายเลขปลายทางต้องเดินทางไปพร้อมคำสั่ง

### 15. Pipeline operation ของ store

**🟡 สำคัญ** · itds-211_comp_arch_Chapter07.pdf, **หน้า 28–30**

เหตุผลการจัดระดับ: เป็นภาพการไหลของคำสั่งและการประยุกต์กลไกหลักกับคำสั่งจริง

sd ใช้ขั้น IF และ ID เหมือน load (หน้า 22–23) จากนั้น EX คำนวณ address (หน้า 28), MEM เขียนข้อมูลลง data memory (หน้า 29) และในขั้น WB ภาพหน้า 30 ไม่มีส่วนใดถูกระบายว่าใช้งาน สอดคล้องกับตารางหน้า 5 ที่ sd ไม่มี register write.

**ประเด็นที่ต้องจำ**

- EX for Store: คำนวณ address (หน้า 28)
- MEM for Store: เขียน data memory (หน้า 29)
- WB for Store: ไม่ได้เขียน register (หน้า 30, ตารางหน้า 5)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- store (sd)
- data memory write
- write-back

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบหน้า 25 (ld อ่าน memory) กับหน้า 29 (sd เขียน memory)

**จุดที่อาจสับสน:** sd ยังผ่านขั้น WB ใน pipeline แต่ไม่ได้ทำงานเขียน register

**ประโยคช่วยจำ:** store จบงานที่ MEM

### 16. Multi-cycle และ single-cycle pipeline diagrams

**🟡 สำคัญ** · itds-211_comp_arch_Chapter07.pdf, **หน้า 31–33**

เหตุผลการจัดระดับ: เป็นภาพการไหลของคำสั่งและการประยุกต์กลไกหลักกับคำสั่งจริง

Multi-cycle pipeline diagram มี 2 แบบ: แบบแสดงการใช้ทรัพยากร (IM, Reg, ALU, DM, Reg; หน้า 31) และแบบดั้งเดิมที่เขียนชื่อขั้นในแต่ละ clock cycle (หน้า 32) โดยตัวอย่างใช้ 5 คำสั่งใน CC1–CC9. Single-cycle pipeline diagram (หน้า 33) แสดงสถานะ pipeline ในรอบเดียว ซึ่งในตัวอย่างมี 5 คำสั่งอยู่ครบ 5 ขั้น.

**ประเด็นที่ต้องจำ**

- Multi-cycle: form showing resource usage (หน้า 31)
- Multi-cycle: traditional form (หน้า 32)
- 5 คำสั่งเสร็จใน CC1–CC9 ตามภาพ (หน้า 31–32)
- Single-cycle: state of pipeline in a given cycle (หน้า 33)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- multi-cycle pipeline diagram
- single-cycle pipeline diagram
- clock cycle (CC)
- IM
- DM

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 33: add x14 อยู่ IF, ld x13 อยู่ ID, add x12 อยู่ EX, sub x11 อยู่ MEM, ld x10 อยู่ WB

| Diagram | มุมมอง | หน้า |
| --- | --- | --- |
| Multi-cycle (resource usage) | หลายรอบ แสดง IM/Reg/ALU/DM | 31 |
| Multi-cycle (traditional) | หลายรอบ เขียนชื่อขั้น | 32 |
| Single-cycle | สถานะในหนึ่งรอบ | 33 |

**จุดที่อาจสับสน:** multi-cycle มองข้ามเวลา (หลายรอบ) ส่วน single-cycle มองภาพนิ่งหนึ่งรอบ

**ประโยคช่วยจำ:** multi = ภาพยนตร์, single = ภาพถ่าย

### 17. Pipelined control (simplified)

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter07.pdf, **หน้า 34**

เหตุผลการจัดระดับ: เป็นภาพรายละเอียดประกอบหรือข้อสรุปเชิงภาพรวม

ภาพหน้า 34 เพิ่มสัญญาณควบคุมลงใน pipelined datapath: RegWrite ที่ register file, ALUSrc และ ALU control/ALUOp ในขั้น EX, Branch กับ Zero เข้าสู่ gate ที่สร้าง PCSrc, MemWrite/MemRead ที่ data memory และ MemtoReg ที่ mux ขั้น WB. รายละเอียดค่าสัญญาณแต่ละคำสั่งไม่มีในสไลด์นี้.

**ประเด็นที่ต้องจำ**

- ภาพแสดง PCSrc, Branch, RegWrite, ALUSrc, ALUOp, MemWrite, MemRead, MemtoReg (หน้า 34)
- Branch และ Zero รวมกันเพื่อกำหนด PCSrc (ภาพหน้า 34)
- ค่าสัญญาณรายคำสั่ง: ต้องตรวจสอบจากต้นฉบับ

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RegWrite
- ALUSrc
- ALUOp
- MemWrite
- MemRead
- MemtoReg
- Branch
- PCSrc

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่สัญญาณสีฟ้าในภาพตามตำแหน่งขั้น: EX (ALUSrc/ALUOp), MEM (Branch/MemWrite/MemRead), WB (MemtoReg)

**จุดที่อาจสับสน:** MemtoReg เลือกค่าที่เขียนกลับ register (จาก memory หรือ ALU) ไม่ใช่สัญญาณเขียน memory

**ประโยคช่วยจำ:** EX เลือก operand, MEM ตัดสินหน่วยความจำ/branch, WB เลือกค่าเขียนกลับ

### 18. Data hazards ในคำสั่ง ALU และ dependencies

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 35–36**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

ลำดับ sub x2,x1,x3; and x12,x2,x5; or x13,x6,x2; add x14,x2,x2; sd x15,100(x2) ทุกคำสั่งหลังจาก sub ใช้ x2. ภาพหน้า 36 แสดงค่า x2 = 10 ใน CC1–CC4, 10/−20 ใน CC5 และ −20 ตั้งแต่ CC6. เส้นแดงคือ dependency ที่ย้อนเวลา (and, or) ต้องแก้ด้วย forwarding; คำถามต่อไปคือจะตรวจจับเมื่อใดต้อง forward.

**ประเด็นที่ต้องจำ**

- ลำดับคำสั่ง sub/and/or/add/sd ใช้ x2 (หน้า 35)
- We can resolve hazards with forwarding (หน้า 35)
- ค่า x2: 10 (CC1–4), 10/−20 (CC5), −20 (CC6–9) (หน้า 36)
- and และ or ต้องการค่าก่อน sub เขียนกลับ (เส้นแดง หน้า 36)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- dependency
- forwarding
- register x2
- clock cycle

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** and อ่าน x2 ใน CC3 และ or อ่านใน CC4 ก่อน sub เขียนเสร็จ (CC5) จึงต้อง forward; add อ่านใน CC5 และ sd ใน CC6

**จุดที่อาจสับสน:** add x14 ใน CC5 ถูกวาดอ่านจาก register file ไม่ใช่เส้นแดง — ค่า 10/−20 หมายถึงค่าเปลี่ยนในรอบนั้น

**ประโยคช่วยจำ:** ย้อนเวลา=เส้นแดง=ต้อง forward

### 19. การตรวจจับว่าต้อง forward

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 37–38**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

ส่งหมายเลข register ไปตาม pipeline เช่น ID/EX.RegisterRs1. operand ของ ALU ในขั้น EX คือ ID/EX.RegisterRs1 และ ID/EX.RegisterRs2. data hazard เกิดเมื่อ Rd ใน EX/MEM (เงื่อนไข 1a/1b) หรือ MEM/WB (2a/2b) ตรงกับ Rs1/Rs2 นั้น แต่จะ forward ก็ต่อเมื่อคำสั่งนั้นเขียน register (RegWrite) และ Rd ไม่ใช่ x0.

**ประเด็นที่ต้องจำ**

- 1a. EX/MEM.RegisterRd = ID/EX.RegisterRs1 (หน้า 37)
- 1b. EX/MEM.RegisterRd = ID/EX.RegisterRs2 (หน้า 37)
- 2a. MEM/WB.RegisterRd = ID/EX.RegisterRs1; 2b. … = Rs2 (หน้า 37)
- ต้องมี RegWrite และ RegisterRd ≠ 0 (หน้า 38)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- ID/EX.RegisterRs1
- ID/EX.RegisterRs2
- EX/MEM.RegisterRd
- MEM/WB.RegisterRd
- RegWrite
- x0

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ลำดับหน้า 35: sub x2 → and x12,x2,x5 ตรงเงื่อนไข 1a (EX/MEM.Rd = x2 = ID/EX.Rs1)

**สูตรที่ต้องรู้**

```text
EX hazard: EX/MEM.RegWrite and EX/MEM.RegisterRd ≠ 0
  and EX/MEM.RegisterRd = ID/EX.RegisterRs1 (หรือ Rs2)
MEM hazard: MEM/WB.RegWrite and MEM/WB.RegisterRd ≠ 0
  and MEM/WB.RegisterRd = ID/EX.RegisterRs1 (หรือ Rs2)
```

รวมเงื่อนไข 1a–2b หน้า 37 กับข้อกำหนด RegWrite/Rd≠0 หน้า 38

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 37–38

**จุดที่อาจสับสน:** 1x = forward จาก EX/MEM, 2x = forward จาก MEM/WB; a = Rs1, b = Rs2

**ประโยคช่วยจำ:** ตรงชื่อ + เขียนจริง + ไม่ใช่ x0 = forward

### 20. Forwarding paths และ ForwardA/ForwardB

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 39–40**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

Forwarding unit ควบคุม mux สองตัวหน้า ALU ด้วย ForwardA (operand แรก) และ ForwardB (operand ที่สอง). ค่า 00 = มาจาก register file (ID/EX), 10 = forward ผล ALU ก่อนหน้า (EX/MEM), 01 = forward จาก data memory หรือผล ALU ก่อนหน้านั้น (MEM/WB).

**ประเด็นที่ต้องจำ**

- ForwardA/B = 00 → ID/EX (register file) (หน้า 40)
- = 10 → EX/MEM (prior ALU result) (หน้า 40)
- = 01 → MEM/WB (data memory หรือ earlier ALU result) (หน้า 40)
- Forwarding unit รับ Rs1/Rs2 และ EX/MEM.RegisterRd, MEM/WB.RegisterRd (ภาพหน้า 39)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- forwarding unit
- ForwardA
- ForwardB
- mux

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** sub x2 → and x12,x2,x5: x2 เป็น operand แรกและอยู่ใน EX/MEM → ForwardA = 10

| Mux control | Source | ความหมาย |
| --- | --- | --- |
| 00 | ID/EX | จาก register file |
| 10 | EX/MEM | forward จากผล ALU ก่อนหน้า |
| 01 | MEM/WB | forward จาก data memory หรือผล ALU ก่อนหน้านั้น |

**จุดที่อาจสับสน:** ระวังสลับ 10 กับ 01: 10 = EX/MEM (ใหม่กว่า), 01 = MEM/WB

**ประโยคช่วยจำ:** 10 ใกล้ (EX/MEM), 01 ไกล (MEM/WB), 00 ไม่ forward

### 21. Double data hazard และ revised forwarding condition

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 41–43**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

ลำดับ add x1,x1,x2; add x1,x1,x3; add x1,x1,x4 ทำให้เกิดทั้ง EX hazard และ MEM hazard พร้อมกันสำหรับคำสั่งที่สาม. ต้องใช้ค่าล่าสุด จึงแก้เงื่อนไข MEM hazard ให้ forward จาก MEM/WB เฉพาะเมื่อเงื่อนไข EX hazard ไม่เป็นจริง. ภาพหน้า 43 แสดง datapath ที่มี forwarding unit.

**ประเด็นที่ต้องจำ**

- Both hazards occur → want the most recent (หน้า 41)
- Only fwd (MEM) if EX hazard condition isn’t true (หน้า 41)
- Revised condition เพิ่ม and not(EX/MEM.RegWrite and EX/MEM.RegisterRd ≠ 0 and EX/MEM.RegisterRd = ID/EX.RegisterRs1) (หน้า 42)
- Datapath with forwarding (หน้า 43)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- double data hazard
- EX hazard
- MEM hazard
- most recent value

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** คำสั่งที่ 3 ใช้ x1: ค่าใน EX/MEM (จากคำสั่งที่ 2) ใหม่กว่าใน MEM/WB (จากคำสั่งที่ 1) จึงต้องเลือก EX/MEM

**สูตรที่ต้องรู้**

```text
if (MEM/WB.RegWrite and (MEM/WB.RegisterRd ≠ 0)
  and not(EX/MEM.RegWrite and (EX/MEM.RegisterRd ≠ 0)
          and (EX/MEM.RegisterRd = ID/EX.RegisterRs1))
  and (MEM/WB.RegisterRd = ID/EX.RegisterRs1)) ForwardA = 01
```

ForwardB ใช้รูปแบบเดียวกันโดยเปลี่ยน Rs1 เป็น Rs2

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 42

**จุดที่อาจสับสน:** ถ้าไม่แก้เงื่อนไข จะ forward ค่าเก่าจาก MEM/WB ผิด

**ประโยคช่วยจำ:** สองทางชนกัน เลือกค่าใหม่สุด (EX/MEM)

### 22. Load-use hazard detection และการ stall

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 44–47**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

ตรวจ load-use ตอนคำสั่งที่ใช้ค่าอยู่ขั้น ID โดยดู IF/ID.RegisterRs1/Rs2. hazard เกิดเมื่อ ID/EX.MemRead และ ID/EX.RegisterRd ตรงกับ register ต้นทางของคำสั่งใน IF/ID; ถ้าพบให้ stall และแทรก bubble. การ stall ทำโดยบังคับ control ใน ID/EX เป็น 0 (EX/MEM/WB ทำ nop) และห้ามอัปเดต PC กับ IF/ID ทำให้ decode และ fetch ซ้ำ; stall 1 รอบให้ ld อ่าน memory แล้ว forward ไป EX ได้.

**ประเด็นที่ต้องจำ**

- Load-use hazard when ID/EX.MemRead and ID/EX.RegisterRd ตรงกับ IF/ID.RegisterRs1/Rs2 (หน้า 44)
- Force control values in ID/EX to 0 → nop (หน้า 45)
- Prevent update of PC and IF/ID (หน้า 45)
- 1-cycle stall แล้ว forward ไป EX (หน้า 45)
- Hazard detection unit ใช้ PCWrite, IF/IDWrite (ภาพหน้า 47)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- hazard detection unit
- MemRead
- bubble
- nop
- PCWrite
- IF/IDWrite

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 46: ld x2,20(x1) แล้ว and x4,x2,x5 — and กลายเป็น nop (bubble) ตรงจุด “Stall inserted here” แล้ว and ถูกทำซ้ำในแถวถัดไป

**สูตรที่ต้องรู้**

```text
Load-use hazard when
  ID/EX.MemRead and
  ((ID/EX.RegisterRd = IF/ID.RegisterRs1) or
   (ID/EX.RegisterRd = IF/ID.RegisterRs1))
```

พิมพ์ตามสไลด์; วงเล็บที่สองซ้ำ Rs1 ทั้งที่หัวข้อกล่าวถึง Rs1, Rs2 — ต้องตรวจสอบจากต้นฉบับ

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 44

**จุดที่อาจสับสน:** สไลด์หน้า 44 พิมพ์เงื่อนไขเป็น IF/ID.RegisterRs1 ทั้งสองครั้ง แต่ข้อความก่อนหน้ากล่าวถึง Rs1 และ Rs2 — วงเล็บที่สองควรเป็น Rs2 หรือไม่: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** load อยู่ข้างหน้า ผู้ใช้ตามติด → ล้าง control เป็น 0 แล้วรอหนึ่งรอบ

### 23. Stalls และ performance

**🟡 สำคัญ** · itds-211_comp_arch_Chapter07.pdf, **หน้า 48**

เหตุผลการจัดระดับ: เป็นภาพการไหลของคำสั่งและการประยุกต์กลไกหลักกับคำสั่งจริง

The BIG Picture: stall ลดประสิทธิภาพแต่จำเป็นเพื่อให้ได้ผลถูกต้อง. คอมไพเลอร์สามารถจัดลำดับโค้ดเพื่อหลบ hazard และ stall ได้ แต่ต้องรู้โครงสร้างของ pipeline.

**ประเด็นที่ต้องจำ**

- Stalls reduce performance but are required for correct results (หน้า 48)
- Compiler can arrange code to avoid hazards and stalls (หน้า 48)
- Requires knowledge of the pipeline structure (หน้า 48)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- stall
- compiler scheduling
- correctness

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เชื่อมกับหน้า 13: การจัดลำดับโค้ดลดจาก 13 เหลือ 11 cycles

**จุดที่อาจสับสน:** stall ไม่ใช่ข้อผิดพลาด แต่เป็นราคาของความถูกต้อง

**ประโยคช่วยจำ:** ช้าหน่อยแต่ถูก; คอมไพเลอร์ช่วยลดได้

### 24. Branch hazards: ตัดสินใน MEM และ flush

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 49**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

ถ้าผล branch ถูกตัดสินในขั้น MEM เมื่อ branch taken คำสั่งสามคำสั่งที่ fetch ตามมา (44 and, 48 or, 52 add) ต้องถูก flush โดยตั้ง control values เป็น 0 แล้ว PC ไปที่ 72 ld x4.

**ประเด็นที่ต้องจำ**

- If branch outcome determined in MEM (หน้า 49)
- Flush these instructions (set control values to 0) (หน้า 49)
- ภาพ: 40 beq x1,x0,16 → flush 44, 48, 52 → 72 ld x4,100(x7) (หน้า 49)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- branch hazard
- flush
- control values = 0
- PC

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** นับจากภาพ: คำสั่งที่ถูก flush มี 3 คำสั่งเมื่อ branch ตัดสินใน MEM

**จุดที่อาจสับสน:** ภาพหน้า 49 ใช้ beq x1,x0,16 และ ld x4,100(x7) แต่หน้า 50 ใช้ beq x1,x3,16 และ ld x4,50(x7): ตัวอย่างไม่ตรงกัน ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** ตัดสินช้า ทิ้งเยอะ

### 25. Reducing branch delay: ย้ายการตัดสินไป ID

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter07.pdf, **หน้า 50–52**

เหตุผลการจัดระดับ: เป็นนิยาม กลไก เงื่อนไข หรือวิธีแก้ hazard ที่สไลด์ใช้ต่อยอดทั้งบท

ย้าย hardware ที่ตัดสินผล branch ไปไว้ขั้น ID ได้แก่ target address adder และ register comparator. ตัวอย่าง branch taken: 40: beq x1,x3,16 เป็น PC-relative ไป 40 + 16×2 = 72. ภาพ Clock 3 (หน้า 51) มีสัญญาณ IF.Flush และ Clock 4 (หน้า 52) แสดง Bubble (nop) ตามด้วย ld x4,50(x7) ที่ PC 72.

**ประเด็นที่ต้องจำ**

- Move hardware to determine outcome to ID: target address adder + register comparator (หน้า 50)
- 40: beq x1,x3,16 → target 40 + 16×2 = 72 (หน้า 50)
- Clock 3: IF.Flush (หน้า 51)
- Clock 4: Bubble (nop) แล้ว ld x4,50(x7) (หน้า 52)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- target address adder
- register comparator
- PC-relative branch
- IF.Flush
- bubble (nop)

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบกับหน้า 49: ตัดสินใน MEM ต้อง flush 3 คำสั่ง แต่ตัดสินใน ID ภาพหน้า 52 เหลือ bubble 1 ช่อง

**สูตรที่ต้องรู้**

```text
Branch target = PC + offset × 2 = 40 + 16 × 2 = 72
```

ตัวอย่าง PC-relative branch ในหน้า 50

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 50

**จุดที่อาจสับสน:** offset 16 ไม่ได้บวกตรง ๆ แต่คูณ 2 ตามสไลด์ (40 + 16×2)

**ประโยคช่วยจำ:** ตัดสินเร็วที่ ID ทิ้งแค่ตัวเดียว

## 3. Roadmap ทบทวน

1. **1 · แนวคิด pipeline** — analogy → 5 ขั้น → Tc 800 vs 200ps → ISA design (itds-211_comp_arch_Chapter07.pdf, หน้า 3–7)
2. **2 · Hazards ภาพรวม** — structure/data/control → forwarding, load-use, code scheduling, branch stall/prediction (itds-211_comp_arch_Chapter07.pdf, หน้า 8–18)
3. **3 · Datapath** — pipeline registers → ld/sd ทีละขั้น → diagrams → control signals (itds-211_comp_arch_Chapter07.pdf, หน้า 19–34)
4. **4 · Forwarding & stall** — เงื่อนไข 1a–2b → ForwardA/B → double hazard → load-use detection (itds-211_comp_arch_Chapter07.pdf, หน้า 35–48)
5. **5 · Control hazards** — flush เมื่อตัดสินใน MEM → ย้ายไป ID → ตัวอย่าง branch taken (itds-211_comp_arch_Chapter07.pdf, หน้า 49–52)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · แนวคิดและตัวเลข

อ่านหน้า 3–7; เขียน 5 ขั้นและคำนวณเวลา ld/sd/R/beq จากตารางหน้า 5

**เกณฑ์ผ่าน:** บอก Tc 800/200ps และอธิบาย throughput vs latency ได้

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 3–7, 18

### รอบ 2 · Hazards

ทำตาราง 3 hazard ด้วยตัวเอง; อธิบาย forwarding, load-use และไล่ code scheduling 13→11 cycles

**เกณฑ์ผ่าน:** ชี้คู่คำสั่งที่ stall ในหน้า 13 ได้ และแยก static/dynamic prediction

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 8–17

### รอบ 3 · Datapath

วาด 4 pipeline registers และไล่ ld/sd ทีละขั้นตามภาพ

**เกณฑ์ผ่าน:** อธิบาย wrong register number และ diagram แบบ single/multi ได้

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 19–34

### รอบ 4 · เงื่อนไข forwarding/stall

เขียนเงื่อนไข 1a–2b, ตาราง ForwardA/B, revised condition และ load-use จากความจำ

**เกณฑ์ผ่าน:** ตั้งค่า ForwardA/B ให้ลำดับหน้า 35 และ 41 ได้ถูก

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 35–48

### รอบ 5 · Branch และสุ่ม Quiz

เทียบ flush 3 คำสั่ง (MEM) กับ bubble 1 ช่อง (ID); ทำ Quiz ทุกหัวข้อ

**เกณฑ์ผ่าน:** คำนวณ target 72 และตอบหัวข้อแดงครบ

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 49–52

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1 หน้า 3–18; วัน 2 datapath หน้า 19–34; วัน 3 forwarding/stall/branch หน้า 35–52 และทำ Quiz
- **ถ้าเหลือ 1 วัน:** 5 ขั้นและ Tc หน้า 4–6 → hazards หน้า 8–17 → เงื่อนไข forward หน้า 37–42 → load-use หน้า 44–46 → branch หน้า 49–50
- **ถ้าเหลือ 3 ชั่วโมง:** 0–30 นาที หน้า 3–7; 30–75 นาที hazards หน้า 8–18; 75–135 นาที forwarding/load-use หน้า 35–47; 135–165 นาที branch หน้า 49–52; 165–180 นาทีสุ่ม Quiz

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

เน้นหัวข้อที่สไลด์ให้นิยาม เงื่อนไข และตัวอย่างโค้ด เช่น 5 stages, hazards, forwarding conditions, load-use และ branch; ไม่มีข้อสอบเก่าจึงไม่ยืนยันโอกาสออกจริง

- **ควรท่องจำ:** IF/ID/EX/MEM/WB, นิยาม hazard 3 ชนิด, เงื่อนไข 1a–2b, ForwardA/B 00/10/01, วิธี stall และ flush (หน้า 4, 8, 37–45, 49)
- **ควรฝึกโจทย์:** รวมเวลาคำสั่งตารางหน้า 5; speedup 8/3.5; นับ cycles 13→11; ระบุ ForwardA/B ของลำดับหน้า 35/41; target 40+16×2 (หน้า 3, 5, 13, 35–42, 50)
- **ควรเข้าใจแนวคิด:** throughput vs latency, ทำไม load-use ต้อง stall, ทำไมต้องเลือกค่าล่าสุดใน double hazard, ทำไมย้าย branch ไป ID ลด flush (หน้า 12, 18, 41, 49–50)
- **เตรียมข้อสอบแบบผสม:** เลือกตอบจับคู่ศัพท์/ขั้น; อัตนัยอธิบายกลไก; คำนวณตามตัวเลขสไลด์; วิเคราะห์ภาพ pipeline diagram และเงื่อนไข hazard (หน้า 3–52)

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 25 ข้อ, อัตนัย 25 ข้อ, คำนวณ 6 ข้อ, วิเคราะห์ 19 ข้อ

### Pipelining analogy: ซักผ้าแบบซ้อนงาน

**ข้อ 1 · เลือกตอบ: เมื่องานไหลต่อเนื่องไม่หยุด speedup ของ pipeline เข้าใกล้ค่าใด?**

- A. จำนวน stages
- B. จำนวนคำสั่ง
- C. 1 เสมอ
- D. ครึ่งหนึ่งของ stages

เฉลย: จำนวน stages (หน้า 3)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 3

**ข้อ 2 · อัตนัย: อธิบายว่า pipelined laundry ทำให้เร็วขึ้นอย่างไร**

เฉลย: ซ้อนขั้นตอนของงานคนละชิ้นให้ทำพร้อมกัน (overlapping execution) จึงเกิด parallelism

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 3

**ข้อ 3 · คำนวณ: คำนวณ speedup ของตัวอย่าง 4 loads จากเวลาที่สไลด์ให้ (8 กับ 3.5)**

เฉลย: 8/3.5 ≈ 2.3

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 3

### RISC-V pipeline 5 ขั้น

**ข้อ 4 · เลือกตอบ: ขั้นใดเขียนผลกลับ register?**

- A. WB
- B. MEM
- C. EX
- D. ID

เฉลย: WB (หน้า 4)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 4

**ข้อ 5 · อัตนัย: ขั้น ID ทำอะไรบ้างตามสไลด์?**

เฉลย: ถอดรหัสคำสั่ง (decode) และอ่าน register

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 4

**ข้อ 6 · วิเคราะห์: คำสั่ง ld ใช้ขั้น EX และ MEM ทำอะไรตามลำดับ?**

เฉลย: EX คำนวณ address, MEM เข้าถึง (อ่าน) operand ในหน่วยความจำ

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 4

### Pipeline performance: single-cycle เทียบ pipelined

**ข้อ 7 · เลือกตอบ: ตามหน้า 6 pipelined datapath มี Tc เท่าใด?**

- A. 200ps
- B. 100ps
- C. 500ps
- D. 800ps

เฉลย: 200ps (หน้า 6)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 5–6

**ข้อ 8 · อัตนัย: ทำไม single-cycle จึงมี Tc = 800ps?**

เฉลย: clock ต้องยาวพอสำหรับคำสั่งที่ใช้เวลามากที่สุด คือ ld 800ps (หน้า 5–6)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 5–6

**ข้อ 9 · คำนวณ: คำนวณเวลารวมของ sd จากตารางหน้า 5**

เฉลย: 200 + 100 + 200 + 200 = 700ps (ไม่มี register write)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 5–6

### Pipelining และการออกแบบ ISA

**ข้อ 10 · เลือกตอบ: คำสั่ง RISC-V ทุกคำสั่งยาวเท่าใด?**

- A. 32 บิต
- B. 1–17 ไบต์
- C. 16 บิต
- D. 64 บิต

เฉลย: 32 บิต (หน้า 7)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 7

**ข้อ 11 · อัตนัย: รูปแบบคำสั่งที่น้อยและสม่ำเสมอช่วย pipeline อย่างไร?**

เฉลย: decode และอ่าน register ได้ในขั้นเดียว

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 7

**ข้อ 12 · วิเคราะห์: ถ้า ISA มีคำสั่งยาวไม่เท่ากันแบบ x86 จะกระทบขั้นใดตามสไลด์?**

เฉลย: การ fetch และ decode ในรอบเดียวทำได้ยากขึ้น (หน้า 7)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 7

### Hazards 3 ชนิด

**ข้อ 13 · เลือกตอบ: การที่ทรัพยากรที่ต้องใช้กำลังถูกใช้อยู่ คือ hazard ชนิดใด?**

- A. Structure hazard
- B. Data hazard
- C. Control hazard
- D. Load-use hazard

เฉลย: Structure hazard (หน้า 8)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 8

**ข้อ 14 · อัตนัย: ให้นิยาม hazard ตามสไลด์**

เฉลย: สถานการณ์ที่ทำให้เริ่มคำสั่งถัดไปในรอบถัดไปไม่ได้

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 8

**ข้อ 15 · วิเคราะห์: คำสั่ง branch ที่ยังไม่รู้ผลทำให้ fetch คำสั่งถัดไปไม่ได้ จัดเป็น hazard ชนิดใดและเพราะอะไร?**

เฉลย: Control hazard เพราะการตัดสินใจ control ขึ้นกับผลของคำสั่งก่อนหน้า (หน้า 8, 14)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 8

### Structure hazard และการแยก memory

**ข้อ 16 · เลือกตอบ: วิธีแก้ structure hazard จาก single memory ตามสไลด์คืออะไร?**

- A. แยก instruction/data memory หรือ cache
- B. เพิ่ม forwarding
- C. ทำนาย branch
- D. เรียงโค้ดใหม่

เฉลย: แยก instruction/data memories หรือ caches (หน้า 9)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 9

**ข้อ 17 · อัตนัย: อธิบายว่า single memory ทำให้เกิด bubble อย่างไร**

เฉลย: load/store ต้องใช้ memory เพื่อเข้าถึงข้อมูล instruction fetch จึงต้อง stall ในรอบนั้น เกิด bubble

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 9

**ข้อ 18 · วิเคราะห์: ถ้า pipeline มี instruction cache และ data cache แยกกัน hazard แบบหน้า 9 ยังเกิดหรือไม่?**

เฉลย: ไม่เกิดในกรณีนี้ เพราะ fetch กับ data access ไม่ต้องแย่ง memory เดียวกัน (หน้า 9)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 9

### Data hazard และ forwarding (bypassing)

**ข้อ 19 · เลือกตอบ: อีกชื่อหนึ่งของ forwarding คืออะไร?**

- A. Bypassing
- B. Flushing
- C. Stalling
- D. Branch prediction

เฉลย: Bypassing (หน้า 11)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 10–11

**ข้อ 20 · อัตนัย: ข้อดีและต้นทุนของ forwarding ตามสไลด์คืออะไร?**

เฉลย: ใช้ผลทันทีที่คำนวณได้ไม่ต้องรอเขียน register แต่ต้องเพิ่มการเชื่อมต่อใน datapath

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 10–11

**ข้อ 21 · วิเคราะห์: ใน add x19,x0,x1 และ sub x2,x19,x3 register ใดก่อ data hazard และเพราะอะไร?**

เฉลย: x19 เพราะ sub ต้องอ่านค่าที่ add ยังไม่ได้เขียนกลับ (หน้า 10)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 10–11

### Load-use data hazard

**ข้อ 22 · เลือกตอบ: ทำไม load-use hazard จึงแก้ด้วย forwarding อย่างเดียวไม่ได้?**

- A. ค่ายังไม่ถูกคำนวณตอนที่ต้องใช้
- B. memory มีอันเดียว
- C. branch ยังไม่รู้ผล
- D. register x0 เขียนไม่ได้

เฉลย: ค่ายังไม่ได้ตอนต้องใช้ — forward ย้อนเวลาไม่ได้ (หน้า 12)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 12

**ข้อ 23 · อัตนัย: อธิบายประโยค “Can’t forward backward in time”**

เฉลย: ค่าจาก ld พร้อมหลังขั้น MEM ซึ่งช้ากว่าเวลาที่คำสั่งถัดไปต้องใช้ใน EX จึงส่งย้อนไปไม่ได้ ต้อง stall

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 12

**ข้อ 24 · วิเคราะห์: ใน ld x1,0(x2) ตามด้วย sub x4,x1,x5 ต้องแทรก bubble กี่รอบตามภาพหน้า 12 ก่อน forward ได้?**

เฉลย: 1 รอบ (ภาพหน้า 12; สอดคล้องกับ 1-cycle stall หน้า 45)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 12

### Code scheduling เพื่อหลบ stall

**ข้อ 25 · เลือกตอบ: หลังจัดลำดับโค้ดใหม่ในหน้า 13 ใช้กี่ cycles?**

- A. 11
- B. 13
- C. 9
- D. 15

เฉลย: 11 cycles (หน้า 13)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 13

**ข้อ 26 · อัตนัย: ระบุคู่คำสั่งในลำดับเดิมที่ทำให้ stall**

เฉลย: ld x2,8(x0) → add x3,x1,x2 และ ld x4,16(x0) → add x5,x1,x4

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 13

**ข้อ 27 · คำนวณ: คำนวณจำนวน cycles ที่ประหยัดได้จากการจัดลำดับใหม่**

เฉลย: 13 − 11 = 2 cycles (เท่ากับจำนวน stall ที่หายไป)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 13

### Control hazard และ stall on branch

**ข้อ 28 · เลือกตอบ: RISC-V เพิ่ม hardware ใดใน ID เพื่อลด control hazard?**

- A. เปรียบเทียบ register และคำนวณ target
- B. forwarding unit
- C. data cache
- D. MEM/WB register

เฉลย: Compare registers + compute target ใน ID (หน้า 14)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 14–15

**ข้อ 29 · อัตนัย: ทำไม pipeline จึงอาจ fetch คำสั่งที่ถูกไม่ได้หลัง branch?**

เฉลย: ผล branch ยังไม่รู้เพราะ branch ยังอยู่ขั้น ID ขณะที่ต้อง fetch คำสั่งถัดไป

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 14–15

**ข้อ 30 · วิเคราะห์: จากภาพหน้า 15 ถ้าใช้ stall on branch คำสั่ง or x7,x8,x9 ถูก fetch เมื่อใด?**

เฉลย: หลังจากรู้ผล branch แล้ว โดยมี bubble คั่นระหว่าง beq กับ or (ภาพหน้า 15)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 14–15

### Branch prediction: static และ dynamic

**ข้อ 31 · เลือกตอบ: Static branch prediction ทำนาย backward branch อย่างไร?**

- A. Taken
- B. Not taken
- C. สุ่ม
- D. Stall เสมอ

เฉลย: Predict backward branches taken (หน้า 17)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 16–17

**ข้อ 32 · อัตนัย: Dynamic branch prediction ทำอะไรเมื่อทำนายผิด?**

เฉลย: stall ขณะ re-fetch และ update history (หน้า 17)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 16–17

**ข้อ 33 · วิเคราะห์: เปรียบเทียบเมื่อใดที่ branch prediction ไม่มีค่าเสียเวลาใน RISC-V ตามหน้า 16**

เฉลย: เมื่อทำนาย not taken แล้วถูก จะ fetch คำสั่งถัดจาก branch โดยไม่มี delay; stall เฉพาะตอนทำนายผิด

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 16–17

### Pipeline summary: throughput และ latency

**ข้อ 34 · เลือกตอบ: Pipelining เพิ่มประสิทธิภาพด้วยการเพิ่มอะไร?**

- A. Instruction throughput
- B. Latency ของแต่ละคำสั่ง
- C. จำนวน register
- D. ขนาด memory

เฉลย: Instruction throughput (หน้า 18)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 18

**ข้อ 35 · อัตนัย: Latency ของแต่ละคำสั่งเปลี่ยนไปอย่างไรเมื่อใช้ pipeline ตามสไลด์?**

เฉลย: เท่าเดิม (same latency)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 18

**ข้อ 36 · วิเคราะห์: ทำไม ISA design จึงสัมพันธ์กับความซับซ้อนของ pipeline? ยกตัวอย่างจากบท**

เฉลย: เช่นความยาวคำสั่งคงที่ 32 บิตและรูปแบบน้อยของ RISC-V ทำให้ fetch/decode ในขั้นเดียวได้ (หน้า 7, 18)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 18

### Pipelined datapath และ pipeline registers

**ข้อ 37 · เลือกตอบ: Pipeline register ระหว่างขั้น EX และ MEM ชื่ออะไร?**

- A. EX/MEM
- B. ID/EX
- C. MEM/WB
- D. IF/ID

เฉลย: EX/MEM (หน้า 20)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 19–20

**ข้อ 38 · อัตนัย: Pipeline registers มีไว้ทำอะไร?**

เฉลย: เก็บข้อมูลที่ขั้นก่อนหน้าผลิตไว้ในรอบก่อนเพื่อส่งต่อขั้นถัดไป

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 19–20

**ข้อ 39 · วิเคราะห์: จากหน้า 19 การไหลขวาไปซ้ายสองจุดคืออะไร และนำไปสู่อะไร?**

เฉลย: WB เขียนกลับ register file และ MEM ส่งผล branch/PC กลับไป IF; นำไปสู่ hazards (data และ control)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 19–20

### Pipeline operation ของ load และ datapath ที่แก้แล้ว

**ข้อ 40 · เลือกตอบ: ปัญหาที่หน้า 26 ชี้ใน WB for Load คืออะไร?**

- A. Wrong register number
- B. Wrong ALU result
- C. Memory busy
- D. Branch misprediction

เฉลย: Wrong register number (หน้า 26)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 21–27

**ข้อ 41 · อัตนัย: Single-clock-cycle diagram ต่างจาก multi-clock-cycle diagram อย่างไร?**

เฉลย: single แสดงการใช้ทรัพยากรของ pipeline ในหนึ่งรอบ; multi แสดงการทำงานตามเวลา (หน้า 21)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 21–27

**ข้อ 42 · วิเคราะห์: วิเคราะห์ว่าทำไม corrected datapath (หน้า 27) แก้ปัญหาหน้า 26 ได้**

เฉลย: ส่งหมายเลข write register ของ ld ผ่าน ID/EX, EX/MEM, MEM/WB จนถึง WB จึงเขียนถูก register (ภาพหน้า 27)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 21–27

### Pipeline operation ของ store

**ข้อ 43 · เลือกตอบ: ขั้นใดที่ sd เขียนข้อมูลลงหน่วยความจำ?**

- A. MEM
- B. EX
- C. WB
- D. ID

เฉลย: MEM (หน้า 29)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 28–30

**ข้อ 44 · อัตนัย: ขั้น WB ของ sd ทำอะไร?**

เฉลย: ไม่มีการเขียน register (หน้า 30; ตารางหน้า 5 ช่อง Register write ของ sd ว่าง)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 28–30

**ข้อ 45 · วิเคราะห์: เปรียบเทียบงานขั้น MEM ของ ld กับ sd**

เฉลย: ld อ่านข้อมูลจาก data memory (หน้า 25) ส่วน sd เขียนข้อมูลลง data memory (หน้า 29)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 28–30

### Multi-cycle และ single-cycle pipeline diagrams

**ข้อ 46 · เลือกตอบ: Single-cycle pipeline diagram แสดงอะไร?**

- A. สถานะ pipeline ในรอบหนึ่ง
- B. การทำงานตลอดเวลา
- C. จำนวน hazard
- D. ขนาดคำสั่ง

เฉลย: State of pipeline in a given cycle (หน้า 33)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 31–33

**ข้อ 47 · อัตนัย: Multi-cycle diagram มีกี่รูปแบบในสไลด์ และต่างกันอย่างไร?**

เฉลย: 2 แบบ: แสดงการใช้ทรัพยากร (หน้า 31) และแบบดั้งเดิมที่เขียนชื่อขั้น (หน้า 32)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 31–33

**ข้อ 48 · คำนวณ: คำนวณจำนวน clock cycles ที่ 5 คำสั่งใช้จนเสร็จในภาพหน้า 32**

เฉลย: 9 cycles (CC1–CC9): 5 ขั้นของคำสั่งแรก + อีก 4 คำสั่งเพิ่มคำสั่งละ 1 รอบ

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 31–33

### Pipelined control (simplified)

**ข้อ 49 · เลือกตอบ: สัญญาณใดอยู่ที่ data memory ในภาพหน้า 34?**

- A. MemWrite และ MemRead
- B. ALUSrc
- C. RegWrite
- D. MemtoReg

เฉลย: MemWrite และ MemRead (หน้า 34)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 34

**ข้อ 50 · อัตนัย: PCSrc ในภาพเกิดจากสัญญาณใด?**

เฉลย: Branch ร่วมกับ Zero จาก ALU (ภาพหน้า 34)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 34

**ข้อ 51 · วิเคราะห์: วิเคราะห์ว่า MemtoReg อยู่ในขั้นใดและทำหน้าที่อะไรตามภาพ**

เฉลย: อยู่ที่ mux ขั้น WB เลือกว่าจะเขียนกลับ register ด้วยข้อมูลจาก memory หรือผล ALU (ภาพหน้า 34)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 34

### Data hazards ในคำสั่ง ALU และ dependencies

**ข้อ 52 · เลือกตอบ: ในภาพหน้า 36 ค่า x2 ใน CC6 เป็นเท่าใด?**

- A. −20
- B. 10
- C. 10/−20
- D. 0

เฉลย: −20 (หน้า 36)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 35–36

**ข้อ 53 · อัตนัย: คำสั่งใดในลำดับหน้า 35 ที่ต้องใช้ forwarding ตามเส้นแดงในหน้า 36?**

เฉลย: and x12,x2,x5 และ or x13,x6,x2

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 35–36

**ข้อ 54 · วิเคราะห์: วิเคราะห์ทำไม sd x15,100(x2) ไม่มีเส้นแดงในภาพหน้า 36**

เฉลย: sd อ่าน x2 หลัง CC5 ที่ sub เขียนค่า −20 แล้ว จึงอ่านค่าใหม่จาก register ได้โดยไม่ย้อนเวลา

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 35–36

### การตรวจจับว่าต้อง forward

**ข้อ 55 · เลือกตอบ: เงื่อนไข 2b ตามหน้า 37 คือข้อใด?**

- A. MEM/WB.RegisterRd = ID/EX.RegisterRs2
- B. EX/MEM.RegisterRd = ID/EX.RegisterRs1
- C. EX/MEM.RegisterRd = ID/EX.RegisterRs2
- D. MEM/WB.RegisterRd = ID/EX.RegisterRs1

เฉลย: MEM/WB.RegisterRd = ID/EX.RegisterRs2 (หน้า 37)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 37–38

**ข้อ 56 · อัตนัย: ทำไมต้องตรวจ RegisterRd ≠ 0 ก่อน forward?**

เฉลย: เพราะ x0 ไม่ใช่ผลที่ต้องส่งต่อ สไลด์กำหนดให้ forward เฉพาะเมื่อ Rd ไม่ใช่ x0 (หน้า 38)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 37–38

**ข้อ 57 · วิเคราะห์: sub x2,x1,x3 แล้ว or x13,x6,x2 (ห่างกัน 1 คำสั่ง) ตรงเงื่อนไขใด?**

เฉลย: 2b: MEM/WB.RegisterRd (x2) = ID/EX.RegisterRs2 (x2) — forward จาก MEM/WB (หน้า 35–37)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 37–38

### Forwarding paths และ ForwardA/ForwardB

**ข้อ 58 · เลือกตอบ: ForwardB = 10 หมายถึงอะไร?**

- A. operand ที่สองมาจากผล ALU ก่อนหน้า (EX/MEM)
- B. operand แรกจาก register file
- C. operand ที่สองจาก MEM/WB
- D. ไม่มีการ forward

เฉลย: Second ALU operand forwarded from prior ALU result, EX/MEM (หน้า 40)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 39–40

**ข้อ 59 · อัตนัย: ForwardA = 01 ส่งข้อมูลจากที่ใด?**

เฉลย: MEM/WB: จาก data memory หรือผล ALU ก่อนหน้านั้น (หน้า 40)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 39–40

**ข้อ 60 · วิเคราะห์: ในลำดับหน้า 35 คำสั่ง or x13,x6,x2 ควรได้ ForwardB เป็นอะไร?**

เฉลย: 01 — x2 เป็น operand ที่สองและค่าจาก sub อยู่ใน MEM/WB ตอน or อยู่ EX (หน้า 35–37, 40)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 39–40

### Double data hazard และ revised forwarding condition

**ข้อ 61 · เลือกตอบ: ใน double data hazard ต้องเลือกค่าจากที่ใด?**

- A. ค่าล่าสุด (EX/MEM)
- B. ค่าเก่าสุด (MEM/WB)
- C. register file
- D. สุ่ม

เฉลย: Most recent — EX/MEM (หน้า 41)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 41–43

**ข้อ 62 · อัตนัย: Revised MEM hazard condition เพิ่มเงื่อนไขอะไร?**

เฉลย: forward จาก MEM/WB เฉพาะเมื่อ EX hazard condition ไม่เป็นจริง (หน้า 41–42)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 41–43

**ข้อ 63 · วิเคราะห์: ในลำดับ add x1,x1,x2 / add x1,x1,x3 / add x1,x1,x4 คำสั่งที่สามควรได้ ForwardA เป็นอะไร?**

เฉลย: 10 — เพราะ EX hazard เป็นจริง จึงใช้ค่าล่าสุดจาก EX/MEM (หน้า 40–42)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 41–43

### Load-use hazard detection และการ stall

**ข้อ 64 · เลือกตอบ: การ stall pipeline ทำอะไรกับ PC และ IF/ID?**

- A. ห้ามอัปเดต
- B. ล้างเป็น 0
- C. เพิ่มค่า 4
- D. สลับค่า

เฉลย: Prevent update of PC and IF/ID register (หน้า 45)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 44–47

**ข้อ 65 · อัตนัย: เขียนเงื่อนไข load-use hazard ตามสไลด์**

เฉลย: ID/EX.MemRead and ((ID/EX.RegisterRd = IF/ID.RegisterRs1) or (ID/EX.RegisterRd = IF/ID.RegisterRs1[หรือ Rs2 — ต้องตรวจสอบจากต้นฉบับ])) (หน้า 44)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 44–47

**ข้อ 66 · วิเคราะห์: ทำไม stall เพียง 1 รอบจึงพอสำหรับ ld ตามด้วยคำสั่งที่ใช้ผล?**

เฉลย: หนึ่งรอบทำให้ขั้น MEM อ่านข้อมูลของ ld ได้ แล้ว forward ไปขั้น EX ของคำสั่งที่ใช้ (หน้า 45)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 44–47

### Stalls และ performance

**ข้อ 67 · เลือกตอบ: ทำไมยังต้องมี stall แม้จะลดประสิทธิภาพ?**

- A. เพื่อให้ได้ผลถูกต้อง
- B. เพื่อลด latency
- C. เพื่อเพิ่ม register
- D. เพื่อทำนาย branch

เฉลย: Required to get correct results (หน้า 48)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 48

**ข้อ 68 · อัตนัย: คอมไพเลอร์ช่วยลด stall ได้อย่างไร และต้องรู้อะไร?**

เฉลย: จัดลำดับโค้ดหลบ hazard โดยต้องรู้โครงสร้าง pipeline (หน้า 48)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 48

**ข้อ 69 · วิเคราะห์: ยกตัวอย่างจากบทที่คอมไพเลอร์ลด stall ได้ และผลลัพธ์เป็นอย่างไร**

เฉลย: code scheduling หน้า 13: ย้าย ld x4 ขึ้นก่อน ลดจาก 13 เหลือ 11 cycles

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 48

### Branch hazards: ตัดสินใน MEM และ flush

**ข้อ 70 · เลือกตอบ: เมื่อ flush คำสั่ง สไลด์ทำอย่างไร?**

- A. ตั้ง control values เป็น 0
- B. ลบคำสั่งออกจาก memory
- C. เพิ่ม PC เป็น 4
- D. เขียน x0

เฉลย: Set control values to 0 (หน้า 49)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 49

**ข้อ 71 · อัตนัย: ถ้าผล branch ตัดสินใน MEM จะเกิดอะไรกับคำสั่งที่ fetch หลัง branch เมื่อ branch taken?**

เฉลย: ต้องถูก flush เพราะเป็นคำสั่งผิดทาง (หน้า 49)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 49

**ข้อ 72 · คำนวณ: จากภาพหน้า 49 นับจำนวนคำสั่งที่ต้อง flush เท่าไร?**

เฉลย: 3 คำสั่ง: 44 and, 48 or, 52 add

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 49

### Reducing branch delay: ย้ายการตัดสินไป ID

**ข้อ 73 · เลือกตอบ: Hardware ใดถูกย้ายไป ID เพื่อลด branch delay?**

- A. Target address adder และ register comparator
- B. Data memory
- C. Forwarding unit
- D. MEM/WB register

เฉลย: Target address adder + register comparator (หน้า 50)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 50–52

**ข้อ 74 · อัตนัย: อธิบายเหตุการณ์ใน Clock 3 และ Clock 4 ของตัวอย่าง branch taken**

เฉลย: Clock 3 สั่ง IF.Flush คำสั่งที่ fetch ผิดทาง; Clock 4 ช่องนั้นกลายเป็น bubble (nop) และ fetch ld x4,50(x7) ที่ 72 (หน้า 51–52)

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 50–52

**ข้อ 75 · คำนวณ: คำนวณ branch target ของ 40: beq x1,x3,16 ตามสไลด์**

เฉลย: 40 + 16×2 = 72

อ้างอิง: itds-211_comp_arch_Chapter07.pdf, หน้า 50–52

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- Pipelining Analogy · หน้า 3: ภาพซักผ้าแบบเรียงกับแบบ pipeline พร้อม speedup 8/3.5 และ ≈ จำนวนขั้น (itds-211_comp_arch_Chapter07.pdf, หน้า 3) (itds-211_comp_arch_Chapter07.pdf, หน้า 3)
- Pipeline Performance · หน้า 5: ตารางเวลาแต่ละขั้นของ ld, sd, R-format, beq (itds-211_comp_arch_Chapter07.pdf, หน้า 5) (itds-211_comp_arch_Chapter07.pdf, หน้า 5)
- Pipeline Performance · หน้า 6: single-cycle Tc 800ps เทียบ pipelined Tc 200ps (itds-211_comp_arch_Chapter07.pdf, หน้า 6) (itds-211_comp_arch_Chapter07.pdf, หน้า 6)
- Data Hazards · หน้า 10: add x19 → sub ใช้ x19 พร้อม bubble ระหว่างรอ (itds-211_comp_arch_Chapter07.pdf, หน้า 10) (itds-211_comp_arch_Chapter07.pdf, หน้า 10)
- Forwarding (aka Bypassing) · หน้า 11: ส่งผลจาก EX ของ add ไปยัง EX ของ sub (itds-211_comp_arch_Chapter07.pdf, หน้า 11) (itds-211_comp_arch_Chapter07.pdf, หน้า 11)
- Load-Use Data Hazard · หน้า 12: ld → sub ต้องมี bubble ก่อน forward (itds-211_comp_arch_Chapter07.pdf, หน้า 12) (itds-211_comp_arch_Chapter07.pdf, หน้า 12)
- Code Scheduling to Avoid Stalls · หน้า 13: จัดลำดับโค้ดจาก 13 cycles เหลือ 11 cycles (itds-211_comp_arch_Chapter07.pdf, หน้า 13) (itds-211_comp_arch_Chapter07.pdf, หน้า 13)
- Stall on Branch · หน้า 15: beq รอผลก่อน fetch คำสั่ง or พร้อม bubble (itds-211_comp_arch_Chapter07.pdf, หน้า 15) (itds-211_comp_arch_Chapter07.pdf, หน้า 15)
- RISC-V Pipelined Datapath · หน้า 19: datapath 5 ขั้นและการไหลขวาไปซ้ายที่ทำให้เกิด hazard (itds-211_comp_arch_Chapter07.pdf, หน้า 19) (itds-211_comp_arch_Chapter07.pdf, หน้า 19)
- Pipeline registers · หน้า 20: IF/ID, ID/EX, EX/MEM, MEM/WB ระหว่างขั้น (itds-211_comp_arch_Chapter07.pdf, หน้า 20) (itds-211_comp_arch_Chapter07.pdf, หน้า 20)
- IF for Load, Store, … · หน้า 22: ขั้น IF: instruction memory และ PC (itds-211_comp_arch_Chapter07.pdf, หน้า 22) (itds-211_comp_arch_Chapter07.pdf, หน้า 22)
- ID for Load, Store, … · หน้า 23: ขั้น ID: อ่าน register และ imm gen (itds-211_comp_arch_Chapter07.pdf, หน้า 23) (itds-211_comp_arch_Chapter07.pdf, หน้า 23)
- EX for Load · หน้า 24: ขั้น EX ของ ld: คำนวณ address (itds-211_comp_arch_Chapter07.pdf, หน้า 24) (itds-211_comp_arch_Chapter07.pdf, หน้า 24)
- MEM for Load · หน้า 25: ขั้น MEM ของ ld: อ่าน data memory (itds-211_comp_arch_Chapter07.pdf, หน้า 25) (itds-211_comp_arch_Chapter07.pdf, หน้า 25)
- WB for Load · หน้า 26: ขั้น WB ของ ld ชี้ wrong register number (itds-211_comp_arch_Chapter07.pdf, หน้า 26) (itds-211_comp_arch_Chapter07.pdf, หน้า 26)
- Corrected Datapath for Load · หน้า 27: ส่ง write register number ไปตาม pipeline (itds-211_comp_arch_Chapter07.pdf, หน้า 27) (itds-211_comp_arch_Chapter07.pdf, หน้า 27)
- EX for Store · หน้า 28: ขั้น EX ของ sd: คำนวณ address (itds-211_comp_arch_Chapter07.pdf, หน้า 28) (itds-211_comp_arch_Chapter07.pdf, หน้า 28)
- MEM for Store · หน้า 29: ขั้น MEM ของ sd: เขียน data memory (itds-211_comp_arch_Chapter07.pdf, หน้า 29) (itds-211_comp_arch_Chapter07.pdf, หน้า 29)
- WB for Store · หน้า 30: ขั้น WB ของ sd ไม่มีการเขียน register (itds-211_comp_arch_Chapter07.pdf, หน้า 30) (itds-211_comp_arch_Chapter07.pdf, หน้า 30)
- Multi-Cycle Pipeline Diagram · หน้า 31: แบบแสดงการใช้ทรัพยากร IM/Reg/ALU/DM (itds-211_comp_arch_Chapter07.pdf, หน้า 31) (itds-211_comp_arch_Chapter07.pdf, หน้า 31)
- Multi-Cycle Pipeline Diagram · หน้า 32: แบบดั้งเดิมเขียนชื่อขั้นใน CC1–CC9 (itds-211_comp_arch_Chapter07.pdf, หน้า 32) (itds-211_comp_arch_Chapter07.pdf, หน้า 32)
- Single-Cycle Pipeline Diagram · หน้า 33: สถานะ 5 คำสั่งในรอบเดียว (itds-211_comp_arch_Chapter07.pdf, หน้า 33) (itds-211_comp_arch_Chapter07.pdf, หน้า 33)
- Pipelined Control (Simplified) · หน้า 34: สัญญาณควบคุม RegWrite, ALUSrc, ALUOp, Branch, PCSrc, MemWrite, MemRead, MemtoReg (itds-211_comp_arch_Chapter07.pdf, หน้า 34) (itds-211_comp_arch_Chapter07.pdf, หน้า 34)
- Dependencies & Forwarding · หน้า 36: ค่า x2 แต่ละรอบและเส้น dependency ที่ต้อง forward (itds-211_comp_arch_Chapter07.pdf, หน้า 36) (itds-211_comp_arch_Chapter07.pdf, หน้า 36)
- Detecting the Need to Forward · หน้า 37: เงื่อนไข 1a/1b/2a/2b (itds-211_comp_arch_Chapter07.pdf, หน้า 37) (itds-211_comp_arch_Chapter07.pdf, หน้า 37)
- Forwarding Paths · หน้า 39: forwarding unit และ mux ForwardA/ForwardB (itds-211_comp_arch_Chapter07.pdf, หน้า 39) (itds-211_comp_arch_Chapter07.pdf, หน้า 39)
- Forwarding Conditions · หน้า 40: ตารางค่า ForwardA/ForwardB 00/10/01 (itds-211_comp_arch_Chapter07.pdf, หน้า 40) (itds-211_comp_arch_Chapter07.pdf, หน้า 40)
- Revised Forwarding Condition · หน้า 42: เงื่อนไข MEM hazard ที่แก้แล้ว (itds-211_comp_arch_Chapter07.pdf, หน้า 42) (itds-211_comp_arch_Chapter07.pdf, หน้า 42)
- Datapath with Forwarding · หน้า 43: datapath ที่มี forwarding unit (itds-211_comp_arch_Chapter07.pdf, หน้า 43) (itds-211_comp_arch_Chapter07.pdf, หน้า 43)
- Load-Use Hazard Detection · หน้า 44: เงื่อนไขตรวจ load-use ใน ID (itds-211_comp_arch_Chapter07.pdf, หน้า 44) (itds-211_comp_arch_Chapter07.pdf, หน้า 44)
- Load-Use Data Hazard · หน้า 46: and กลายเป็น nop และ stall inserted (itds-211_comp_arch_Chapter07.pdf, หน้า 46) (itds-211_comp_arch_Chapter07.pdf, หน้า 46)
- Datapath with Hazard Detection · หน้า 47: hazard detection unit, PCWrite, IF/IDWrite (itds-211_comp_arch_Chapter07.pdf, หน้า 47) (itds-211_comp_arch_Chapter07.pdf, หน้า 47)
- Branch Hazards · หน้า 49: ตัดสิน branch ใน MEM และ flush 3 คำสั่ง (itds-211_comp_arch_Chapter07.pdf, หน้า 49) (itds-211_comp_arch_Chapter07.pdf, หน้า 49)
- Reducing Branch Delay · หน้า 50: ย้ายการตัดสินไป ID และตัวอย่าง target 72 (itds-211_comp_arch_Chapter07.pdf, หน้า 50) (itds-211_comp_arch_Chapter07.pdf, หน้า 50)
- Example: Branch Taken · หน้า 51: Clock 3 พร้อม IF.Flush (itds-211_comp_arch_Chapter07.pdf, หน้า 51) (itds-211_comp_arch_Chapter07.pdf, หน้า 51)
- Example: Branch Taken · หน้า 52: Clock 4 มี bubble (nop) และ ld x4,50(x7) (itds-211_comp_arch_Chapter07.pdf, หน้า 52) (itds-211_comp_arch_Chapter07.pdf, หน้า 52)
