# Chapter03 · Data Representation & RISC-V ISA

ITDS-211 · Computer Architecture & Operating System · W. Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter03_RiscV.pdf** จำนวน 118 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter03 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/วิเคราะห์/คำนวณ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 30 หัวข้อ · 🔴 ต้องจำแน่นอน 19 หัวข้อ (63.3%) · 🟡 สำคัญ 9 หัวข้อ (30.0%) · ⚪ อ่านเสริม 2 หัวข้อ (6.7%) · แบบฝึก 90 ข้อ · Flashcard 60 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter03 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| ข้อมูลเชิงปริมาณและระบบเลข | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–8 |
| Sign & Magnitude | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 9–12 |
| (r−1)’s และ r’s complement | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 13–15 |
| 1’s complement และ end-around carry | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 16–17 |
| 2’s complement และการบวก | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 18–22 |
| Bias / Excess notation | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 23–24 |
| Floating-point: sign, mantissa, exponent | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 25–26 |
| IEEE single/double และ biased exponent | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 27–29 |
| แปลงเศษส่วนฐานสองและตัวอย่าง single | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 30–31 |
| อักขระ ASCII และ Unicode ในสไลด์ | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 32–38 |
| ISA และคำสั่งคำนวณสามตัวถูกดำเนินการ | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 39–44 |
| RISC-V register 32 ตัวและบทบาท | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 45–47 |
| Byte addressing, endian และ load/store | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 48–51 |
| Immediate และ signed/unsigned | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 52–53 |
| R/I/S instruction formats และ encoding | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 54–59 |
| Logical operations และ bit mask | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 60–64 |
| Branches, loop และ signed comparison | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 65–70 |
| Procedure call, parameters และ return | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 71–72 |
| Leaf procedure และ stack save/restore | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 73–76 |
| Non-leaf procedure และ factorial recursion | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 77–79 |
| Memory layout, activation record และข้อมูลขนาดย่อย | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 80–83 |
| Self-study: String copy | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84–86 |
| Self-study: Wide immediate และ branch address | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 87–91 |
| Self-study: Atomic operations | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 92–94 |
| Self-study: จาก source ไป executable และ runtime | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 95–101 |
| Self-study: Swap procedure | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 102–103 |
| Self-study: Sort loops และการรักษา register | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 104–107 |
| Self-study: บทเรียนจากการวัดผลและ compiler | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 108–110 |
| Self-study: Array indexing เทียบ pointer | 🟡 สำคัญ | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 111–113 |
| Self-study: MIPS เทียบ RISC-V และ extensions | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 114–117 |

### บทนี้เรียนเพื่ออะไร

บทนี้ช่วยให้เห็นว่าข้อมูลจำนวนและอักขระถูกเข้ารหัสในบิตอย่างไร แล้วเชื่อมรหัสนั้นกับ ISA ของ RISC-V: คำสั่งอ่าน/เขียน memory, คำนวณ, เปลี่ยนทางเดิน และเรียก procedure จนถึงกระบวนการสร้างโปรแกรม

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–37, 39–117

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- แปลจำนวนใน unsigned, Sign & Magnitude, complement, bias และ floating-point พร้อมชี้ข้อจำกัด (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–31)
- แยก encoding อักขระจากค่าตัวเลข และอ่าน ASCII ตามตารางต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 32–37, 82)
- อ่าน register, memory, instruction formats, logical/branch และ procedure ของ RISC-V (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 41–83)
- ใช้ส่วน Self-study ฝึกตามโค้ดและแผนภาพ toolchain, atomics, sort, array และ extensions โดยระบุจุดขัดกัน (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84–117)

รายการวัตถุประสงค์รายบทที่ระบุเป็นข้อชัดเจน: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สังเคราะห์จากหัวข้อที่ปรากฏในสไลด์

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- ตรวจครบ 118 หน้า: หน้า 1 ปก, 2 Course Outline, 3/39/40/84 หน้าเปิดส่วน, 38 Assignment2, 118 Q&A; หน้า 84–117 ระบุ Self-study
- ไม่มีรายการ Chapter Objectives เฉพาะบทอย่างชัดเจน: ต้องตรวจสอบจากต้นฉบับ
- ไม่มีข้อสอบเก่าหรือน้ำหนักคะแนน จึงให้ระดับความสำคัญจากความเป็นนิยาม/สูตร/ขั้นตอน/ตัวอย่างในสไลด์ ไม่อ้างว่าจะออกจริง
- หน้า 17 ตัวอย่าง 3-bit 1’s complement กับ +6 เกินช่วง; หน้า 31 การแปลง 17.15 ใช้บิตเศษส่วนไม่ครบ: ต้องตรวจสอบจากต้นฉบับ
- หน้า 15 ตัวอย่างฐานสิบเขียนชื่อ 1’/2’ complement ทั้งที่สูตรหน้า 13–14 จับคู่ฐานสิบกับ 9’s/10’s: ต้องตรวจสอบจากต้นฉบับ
- หน้า 74 add x6,x12,x1 ไม่ตรงกับ i+j; หน้า 78 C base case return f ไม่กำหนด; หน้า 79 หัวข้อเรียก Leaf ทั้งที่ recursive: ต้องตรวจสอบจากต้นฉบับ
- หน้า 86 address y[i] ใช้ x10 ตาม code/comment ที่ไม่ตรง; หน้า 87 addi 128 แต่ภาพ/comment 0x500: ต้องตรวจสอบจากต้นฉบับ
- หน้า 107 หัวข้อ restore แต่คำสั่งเป็น sd; หน้า 112 C int แต่ assembly stride 8; หน้า 116 มี srlw ซ้ำ: ต้องตรวจสอบจากต้นฉบับ
- ภาพบางหน้ามีข้อความ/รหัสจำนวนมาก จึงเก็บสไลด์ต้นทางในแกลเลอรีให้ขยายดู; สรุปไม่ได้คัดโค้ดยาวจากภาพ

## 2. สรุปรายบทและหัวข้อ

### 1. ข้อมูลเชิงปริมาณและระบบเลข

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 4–8**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

บทเริ่มจากการเก็บข้อมูลใน register ที่มีจำนวนบิตจำกัด แล้วแยกข้อมูลเป็น quantitative กับ qualitative. ข้อมูลเชิงปริมาณแบ่ง integer/non-integer และ signed/unsigned; ระบบฐานที่ใช้คือ 10, 2, 8 และ 16.

**ประเด็นที่ต้องจำ**

- Unsigned n บิตมีค่า 0 ถึง 2^n−1 (หน้า 5)
- quantitative: integer/non-integer; integer อาจ signed หรือ unsigned (หน้า 6–8)
- ฐาน 2 ใช้ 0–1, ฐาน 8 ใช้ 0–7, ฐาน 16 ใช้ 0–9 และ A–F (หน้า 7)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- bit/register
- unsigned
- decimal/binary/octal/hexadecimal

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** สไลด์ยก +20, −20 เป็น integer และ 10.25, 3.3333, 1/8 เป็น non-integer (หน้า 8)

**จุดที่อาจสับสน:** จำนวนบิตจำกัดทำให้ช่วงค่าจำกัด; อย่าใช้ช่วง signed แทนสูตร unsigned

**ประโยคช่วยจำ:** จำนวนบิตกำหนดช่วง; ฐานกำหนดชุดหลัก

### 2. Sign & Magnitude

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 9–12**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

การแทน signed แบบ Sign & Magnitude ใช้หนึ่งบิตเป็น sign และ n บิตเป็น magnitude. sign 0 หมายถึงบวกหรือศูนย์, sign 1 หมายถึงลบหรือศูนย์ จึงมีรหัสศูนย์สองแบบและช่วง −(2^n−1) ถึง +(2^n−1).

**ประเด็นที่ต้องจำ**

- หนึ่ง sign bit + n magnitude bits (หน้า 10)
- 8 บิตทั้งหมดมี magnitude 7 บิต จึงได้ −127 ถึง +127 (หน้า 10–11)
- 00000000 และ 10000000 เป็นศูนย์สองรูป (หน้า 11)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Sign & Magnitude
- sign bit
- magnitude
- positive zero / negative zero

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เปลี่ยนเครื่องหมายโดยกลับ sign bit; สไลด์ระบุว่า absolute value ทำได้ตรงไปตรงมา (หน้า 12)

**จุดที่อาจสับสน:** อย่าสับสน n magnitude bits ในสูตรกับจำนวนบิตทั้งหมด; แบบนี้ไม่ได้ใช้บวก/ลบด้วยขั้นเดียวกันเสมอ

**ประโยคช่วยจำ:** หนึ่งบิตบอกเครื่องหมาย; ที่เหลือบอกขนาด; ศูนย์สองตัว

### 3. (r−1)’s และ r’s complement

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 13–15**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

สไลด์จัด complement เป็น (r−1)’s กับ r’s ตามฐาน r. สำหรับเลข n หลัก m สูตรคือ (r^n−1)−m และ r^n−m; ฐานสิบจึงมี 9’s/10’s และฐานสองมี 1’s/2’s complement.

**ประเด็นที่ต้องจำ**

- (r−1)’s complement = (r^n−1)−m (หน้า 14)
- r’s complement = r^n−m (หน้า 14)
- ตัวอย่าง m=382, n=3: 9’s =617 และ 10’s =618 (หน้า 15)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- radix r
- (r−1)’s complement
- r’s complement
- 9’s/10’s; 1’s/2’s complement

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** 999−382=617 แล้วบวกหนึ่งเป็น 618 ตามตัวอย่างฐานสิบหน้า 15

**จุดที่อาจสับสน:** หน้า 14 คำอธิบายสูตร r’s ใช้ n แต่สูตรใช้ m; หน้า 15 เรียกผลฐานสิบว่า 1’/2’ complement แทน 9’s/10’s: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** ลบจากทุกหลักสูงสุด; ถ้าจะเป็น r’s เพิ่มหนึ่ง

### 4. 1’s complement และ end-around carry

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 16–17**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

1’s complement ของเลขฐานสองได้จากการกลับทุกบิต. แบบ 8 บิตมีช่วง −127 ถึง +127 และมีศูนย์สองรหัส; การบวกต้องนำ carry ที่หลุดออกมาบวกวนกลับ.

**ประเด็นที่ต้องจำ**

- 0101 กลับบิตเป็น 1010 ซึ่งสไลด์ใช้แทน −5 (หน้า 16)
- 8-bit: −127 ถึง +127; ศูนย์ 00000000 และ 11111111 (หน้า 16)
- end-around carry นำ carry-out มาบวกเข้าผลลัพธ์ (หน้า 17)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- 1’s complement
- end-around carry
- negative zero

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 17 สาธิตบวก carry กลับเข้าผล; ใช้เพื่อดูขั้นตอนเท่านั้น

**จุดที่อาจสับสน:** หน้า 17 เรียกตัวอย่างว่า “3-bit add 6 and −3” ทั้งที่ 1’s complement 3 บิตแทน +6 ไม่ได้: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** หนึ่งส์กลับทุกบิต; carry วนกลับ; ศูนย์สองแบบ

### 5. 2’s complement และการบวก

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 18–22**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

2’s complement หาโดยกลับบิตแล้วบวก 1 และใช้การบวกเลข signed ได้โดยทิ้ง carry ที่เกินความกว้าง. แบบ 8 บิตมีช่วง −128 ถึง +127 และศูนย์รหัสเดียว; ภาพเปรียบเทียบกับ Sign & Magnitude และ 1’s complement.

**ประเด็นที่ต้องจำ**

- 2’s = 1’s complement + 1 (หน้า 18–19)
- 8-bit: −128 ถึง +127; ศูนย์เดียว (หน้า 18,21–22)
- 4-bit: 0110 (+6) + 1011 (−5) = 0001 หลังทิ้ง carry (หน้า 20)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- 2’s complement
- carry-out
- signed range −2^(n−1)..2^(n−1)−1

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 19 ใช้ 0101011 → กลับบิต 1010100 → บวก 1 เป็น 1010101

| แบบ | ศูนย์ | ช่วง 8 บิต |
| --- | --- | --- |
| Sign & Magnitude | สองรหัส | −127..+127 |
| 1’s complement | สองรหัส | −127..+127 |
| 2’s complement | หนึ่งรหัส | −128..+127 |

**จุดที่อาจสับสน:** อย่าส่ง carry วนกลับแบบ 1’s complement; 2’s complement ทิ้ง carry ที่พ้นบิต

**ประโยคช่วยจำ:** ทูส์: กลับบิตบวกหนึ่ง; carry เกินทิ้ง; ศูนย์หนึ่ง

### 6. Bias / Excess notation

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 23–24**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

Bias notation แปลบิตเป็น unsigned ก่อน แล้วลบค่า bias B เพื่อได้ค่าที่แทน. ตัวอย่าง 8 บิต B=127 ทำให้ 00000000 เป็น −127, 01111111 เป็น 0 และ 11111111 เป็น +128.

**ประเด็นที่ต้องจำ**

- value = unsigned(bit pattern) − B (หน้า 23)
- B=127: 00000000→−127; 01111111→0; 10000000→+1; 11111111→+128 (หน้า 24)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Bias notation
- Excess notation
- biased-127

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** แปล 10000000 เป็น unsigned 128 แล้วลบ 127 ได้ +1 ตามตารางหน้า 24

**จุดที่อาจสับสน:** บิตบนสุดใน biased-127 ไม่ใช่ sign bit แบบ Sign & Magnitude

**ประโยคช่วยจำ:** อ่าน unsigned ก่อน ลบ Bias ทีหลัง

### 7. Floating-point: sign, mantissa, exponent

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 25–26**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

Floating-point แยก sign, mantissa, exponent และ radix เพื่อแทนจำนวนที่มีจุดทศนิยมหรือสเกลใหญ่เล็ก. ในรูปฐานสอง สไลด์เขียน N = (−1)^s m 2^e.

**ประเด็นที่ต้องจำ**

- รูปทั่วไปมี sign, mantissa, exponent, radix (หน้า 25)
- N = (−1)^s m 2^e (หน้า 26)
- ตัวอย่างฐานสิบ +3207.23 = 3.20723×10^3 และ −0.000321 = −3.21×10^−4 (หน้า 25)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- mantissa
- exponent
- radix
- N = (−1)^s m 2^e

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านตัวอย่างหน้า 25 โดยแยกเครื่องหมาย ค่าสัมประสิทธิ์ และเลขชี้กำลัง

**จุดที่อาจสับสน:** mantissa ไม่ใช่ exponent; radix เป็นฐานของการยกกำลัง

**ประโยคช่วยจำ:** เครื่องหมาย–แมนทิสซา–ชี้กำลัง–ฐาน

### 8. IEEE single/double และ biased exponent

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 27–29**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

สไลด์เทียบ single precision 32 บิตกับ double precision 64 บิตตามช่อง sign/exponent/mantissa. สำหรับ single แบบ normalized ใช้ N=(−1)^s(1.m)2^(E−127), E=e+127; E=1..254 ให้ e=−126..+127 โดย 0 และ 255 ถูกสงวนสำหรับกรณีพิเศษตามสไลด์.

**ประเด็นที่ต้องจำ**

- single = 1 sign + 8 exponent + 23 mantissa bits (หน้า 27)
- double = 1 + 11 + 52 bits (หน้า 27)
- single normalized: E=e+127; e=−126..+127 (หน้า 28–29)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- IEEE FPS ตามชื่อสไลด์
- single/double precision
- normalized 1.m
- NaN
- E/e

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตัวอย่าง e=4 จึง E=131 ในหน้า 31 เชื่อมสูตรหน้า 28

| รูปแบบ | รวม | sign | exponent | mantissa |
| --- | --- | --- | --- | --- |
| Single | 32 | 1 | 8 | 23 |
| Double | 64 | 1 | 11 | 52 |

**จุดที่อาจสับสน:** หน้า 29 เขียน 2^128 เป็น “maximum representable” ทั้งที่ก่อนหน้าให้ m สูงสุด 2−2^−23; ค่านี้เป็นการประมาณขอบบน: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** Single 1–8–23; Double 1–11–52; exponent บวก 127

### 9. แปลงเศษส่วนฐานสองและตัวอย่าง single

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 30–31**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

เศษส่วนฐานสองมีน้ำหนักตำแหน่ง 2^−1, 2^−2 ต่อไปตามลำดับ; ตัวอย่าง 101.1101₂ = 5.8125₁₀. หน้า 31 ใช้ 17.15₁₀ เพื่อสาธิตการ normalize และเติม E=131 ใน single precision แต่เศษส่วนฐานสองที่พิมพ์เป็นเพียงค่าประมาณ.

**ประเด็นที่ต้องจำ**

- 101.1101₂ = 4+1+1/2+1/4+1/16 = 5.8125 (หน้า 30)
- 17.15 ตัวอย่างหน้า 31: exponent จริง e=4; E=131=10000011₂
- bit sign =0 สำหรับตัวอย่างบวก (หน้า 31)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- binary fraction
- normalization
- biased exponent

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** แยกส่วนเต็ม 101₂=5 และเศษ .1101₂=.8125 ก่อนรวม (หน้า 30)

**จุดที่อาจสับสน:** หน้า 31 ใช้เครื่องหมายเท่ากับกับชุดบิตเศษส่วนที่ไม่ครบสำหรับ 17.15: ต้องตรวจสอบจากต้นฉบับ; อย่าจำว่า 17.15 มี binary สิ้นสุด

**ประโยคช่วยจำ:** จุดขยับเป็น 1.x; exponent ใส่ bias

### 10. อักขระ ASCII และ Unicode ในสไลด์

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 32–38**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

ข้อมูล qualitative รวมอักขระและ control symbols ซึ่งต้องแปลงเป็นรหัสบิตก่อนเก็บ. สไลด์กล่าวถึง ASCII, EBCDIC, Unicode; ASCII ใช้ 7 บิต 128 รหัส โดยมีทั้ง printable/control และยก A=0x41, a=0x61 ซึ่งต่างกัน 0x20.

**ประเด็นที่ต้องจำ**

- ASCII = 7-bit/128 codes; สไลด์ยก parity bit เมื่อจัดเป็น byte (หน้า 33–34)
- A=0x41, a=0x61; รหัสอักษรกับค่าตัวเลขเป็นคนละสิ่ง (หน้า 37)
- หน้า 82 เพิ่ม ASCII 95 graphic+33 control, Latin-1 256 และ UTF-8/UTF-16 แบบความยาวแปรผัน

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- ASCII
- EBCDIC
- Unicode
- Latin-1
- UTF-8/UTF-16
- control character

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูตาราง ASCII หน้า 35–36 เพื่อเทียบอักษรใหญ่/เล็กและรหัสตัวเลข

**จุดที่อาจสับสน:** หน้า 82 เรียก Unicode “32-bit character set” เป็นถ้อยคำของสไลด์; รายละเอียดมาตรฐานจริงเกินเอกสาร: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** อักขระเป็นรหัส; รหัสเลขไม่ใช่ค่าเลข

### 11. ISA และคำสั่งคำนวณสามตัวถูกดำเนินการ

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 39–44**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

ส่วน RISC-V เริ่มที่หน้า 39–40 แล้วอธิบาย ISA เป็นภาษาคำสั่งระดับเครื่องซึ่งต่างกันระหว่างสถาปัตยกรรม. รูปคำสั่ง arithmetic ใช้ destination และ source สองตัว เช่น add a,b,c; หลักการออกแบบที่สไลด์ย้ำคือ simplicity favors regularity.

**ประเด็นที่ต้องจำ**

- RISC-V เป็น ISA แบบ open ตามคำบรรยายประวัติในสไลด์หน้า 42
- add a,b,c หมายถึง a=b+c (หน้า 43)
- f=(g+h)−(i+j) ใช้ add สองครั้งและ sub หนึ่งครั้ง (หน้า 44)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- ISA
- RISC-V
- add/sub
- destination/source
- simplicity favors regularity

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 44 ใช้ t0=g+h, t1=i+j แล้ว f=t0−t1

**จุดที่อาจสับสน:** อย่าสลับ destination กับ source; ชื่อองค์กรดูแล RISC-V ในหน้า 42 เป็นข้อความตามสไลด์ ไม่ใช่ข้อมูลสถานะปัจจุบัน

**ประโยคช่วยจำ:** ปลายทางก่อน; แหล่งสองตัวตามหลัง

### 12. RISC-V register 32 ตัวและบทบาท

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 45–47**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

สไลด์ใช้ชุด integer register 32 ตัว กว้างตัวละ 64 บิตในบริบท RV64 โดยเรียกข้อมูล 64 บิตว่า doubleword และ 32 บิตว่า word. ชื่อ x0–x31 เชื่อมกับบทบาท เช่น x0 ค่าศูนย์, x1 return address, x2 stack pointer, x10–x17 arguments/results และกลุ่ม temporary/saved.

**ประเด็นที่ต้องจำ**

- x0=0, x1=return address, x2=stack pointer (หน้า 46)
- x5–x7,x28–x31 temporaries; x8 frame pointer; x9,x18–x27 saved (หน้า 46)
- x10–x11 arguments/results; x12–x17 arguments (หน้า 46)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- x0–x31
- word=32-bit
- doubleword=64-bit
- sp
- return address
- saved/temporary

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 47 เขียนคำสั่งด้วยหมายเลข x5,x6,x19–x23 เพื่อแทนตัวแปรในนิพจน์

**จุดที่อาจสับสน:** อย่าเอาเลข register x10–x17 ไปตีความเป็นค่าตัวเลขที่เก็บอยู่

**ประโยคช่วยจำ:** 0 คงศูนย์, 1 กลับ, 2 กองซ้อน, 10–17 ส่งค่า

### 13. Byte addressing, endian และ load/store

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 48–51**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

หน่วยความจำในสไลด์อ้าง address ทีละ byte และ RISC-V ใช้ little-endian ซึ่ง byte น้ำหนักต่ำอยู่ address ต่ำ. การคำนวณใช้ค่าที่ register; ต้อง load จาก memory ก่อนและ store ผลกลับเมื่อจำเป็น จึงมีตัวอย่าง A[12]=h+A[8] ที่คูณ index ด้วย 8 byte ต่อ doubleword.

**ประเด็นที่ต้องจำ**

- ภาพหน้า 48 เทียบ big/little endian; หน้า 49 ระบุ RISC-V little-endian
- ld/sd ย้าย doubleword ระหว่าง memory/register (หน้า 49–50)
- A[8] offset 64, A[12] offset 96 จาก base x22 (หน้า 50)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- byte addressed
- little-endian
- big-endian
- ld
- sd
- base+offset

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ld x9,64(x22); add x9,x21,x9; sd x9,96(x22) ตามหน้า 50

**จุดที่อาจสับสน:** ตำแหน่ง array เป็น byte offset ไม่ใช่เลข index ตรง ๆ; หน้า 48 เป็นแผนภาพเปรียบเทียบ แต่หน้า 49 ระบุ RISC-V little-endian

**ประโยคช่วยจำ:** คูณ index ด้วย 8; load–add–store

### 14. Immediate และ signed/unsigned

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 52–53**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

addi ใช้ค่าคงที่ immediate โดยไม่ต้องโหลดค่าคงที่จาก memory. สไลด์ทวนช่วง unsigned n บิตและ signed 2’s complement พร้อมวิธี sign extension เมื่อโหลดข้อมูลขนาดเล็กเข้าสู่ register ที่กว้างกว่า.

**ประเด็นที่ต้องจำ**

- addi x22,x22,4 เพิ่ม x22 อีก 4 (หน้า 52)
- unsigned n-bit 0..2^n−1; signed n-bit −2^(n−1)..2^(n−1)−1 (หน้า 53)
- sign extension คัดลอก sign bit ขึ้นไปยังบิตใหม่ (หน้า 53)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- addi
- immediate
- sign extension
- signed/unsigned

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 53 ยกการหา −2 จาก +2: กลับบิตแล้วบวก 1

**จุดที่อาจสับสน:** immediate เป็น operand ในคำสั่ง ไม่ใช่ address memory เสมอไป

**ประโยคช่วยจำ:** addi ใส่ค่าเลย; signed ขยายเครื่องหมาย

### 15. R/I/S instruction formats และ encoding

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 54–59**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

RISC-V คำสั่งหลักในช่วงนี้กว้าง 32 บิต และสไลด์แจก field ของ R, I, S format. R มี funct7,rs2,rs1,funct3,rd,opcode; I ใช้ immediate 12 บิต; S แยก immediate สองช่วง. ตัวอย่าง add x9,x20,x21 ถูกแปลงเป็น hex 015A04B3.

**ประเด็นที่ต้องจำ**

- R: 7+5+5+3+5+7=32 บิต (หน้า 55)
- I: imm12,rs1,funct3,rd,opcode (หน้า 57)
- S: imm[11:5],rs2,rs1,funct3,imm[4:0],opcode (หน้า 58)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- opcode
- rd
- rs1/rs2
- funct3/funct7
- R/I/S format
- stored program

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 56 ให้ add x9,x20,x21: funct7=0,rs2=21,rs1=20,funct3=0,rd=9,opcode=51 → 015A04B3₁₆

**จุดที่อาจสับสน:** S format ไม่มี rd ที่ตำแหน่งเดียวกับ R/I; immediate ถูกแบ่ง; หน้า 59 ย้ำคำสั่งกับข้อมูลอยู่ใน memory แบบ stored program

**ประโยคช่วยจำ:** R สอง source; I ค่าทันที; S กระจาย offset

### 16. Logical operations และ bit mask

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 60–64**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

สไลด์แนะนำ shift left/right, AND, OR, XOR และการทำ NOT ด้วย XOR กับบิตหนึ่งทั้งหมด. การ shift logical เลื่อนบิตพร้อมเติม 0; สำหรับ unsigned การเลื่อน i ตำแหน่งสัมพันธ์กับคูณ/หาร 2^i. AND ใช้ mask เลือกบิต, OR ใช้ตั้งบิต และ XOR ชี้ความต่างของบิต.

**ประเด็นที่ต้องจำ**

- slli/srli เลื่อน logical; unsigned shift i ตำแหน่งสัมพันธ์กับ 2^i (หน้า 61)
- AND ใช้ mask คงบิตที่ต้องการ (หน้า 62)
- OR ตั้งบิต; XOR ให้ 1 เมื่อบิตต่างกัน; NOT ด้วย XOR all-ones (หน้า 63–64)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- slli
- srli
- AND/OR/XOR
- mask
- logical shift

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ภาพ AND หน้า 62 ดูว่า mask 0 ลบบิตและ mask 1 รักษาบิต

**จุดที่อาจสับสน:** คำเปรียบเทียบคูณ/หาร 2^i ในสไลด์จำกัดบริบท unsigned; อย่าใช้กับ signed โดยไม่พิจารณาเงื่อนไข

**ประโยคช่วยจำ:** AND เลือก, OR ตั้ง, XOR ต่าง, Shift ขยับ

### 17. Branches, loop และ signed comparison

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 65–70**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

beq/bne เปลี่ยนทางเดินเมื่อสอง register เท่ากันหรือไม่เท่ากัน; blt/bge เปรียบเทียบลำดับและต้องแยก signed กับ unsigned. ตัวอย่าง if/else ใช้ branch ข้ามบล็อก ส่วน while คำนวณ address save[i], load, เปรียบเทียบ k, เพิ่ม i แล้ววน. สไลด์นิยาม basic block เป็นช่วงคำสั่งต่อเนื่องที่ไม่มี branch ภายในนอกจากท้าย.

**ประเด็นที่ต้องจำ**

- beq = branch if equal; bne = branch if not equal (หน้า 65)
- if/else หน้า 66: bne ไป Else, beq x0,x0 ไป Exit
- loop หน้า 67: slli index 3 บิต → load → bne Exit → addi index → branch Loop
- signed กับ unsigned ทำให้ bit pattern เดียวกันเทียบต่างกัน (หน้า 69–70)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- beq/bne
- blt/bge
- basic block
- signed/unsigned branch

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 70 ให้ x22 เป็น all-ones และ x23 เป็น +1: signed เห็น −1 < +1 แต่ unsigned เห็นค่ามากกว่า +1

**จุดที่อาจสับสน:** beq x0,x0 เป็น branch แบบไม่มีเงื่อนไขในตัวอย่าง; อย่าเทียบ signed/unsigned โดยดู bit pattern อย่างเดียว

**ประโยคช่วยจำ:** Equal/Not equal เลือกทาง; signed/unsigned เลือกความหมาย

### 18. Procedure call, parameters และ return

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 71–72**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

การเรียก procedure ส่ง arguments ผ่าน x10–x17, เก็บตำแหน่งกลับใน x1 และรับผลใน register ผลลัพธ์ตามข้อตกลงที่สไลด์อธิบาย. jal x1,label กระโดดไป procedure พร้อมบันทึก return address; jalr x0,0(x1) ใช้กลับผู้เรียก.

**ประเด็นที่ต้องจำ**

- x10–x17 รับ parameters; x10–x11 ใช้ผลลัพธ์ (หน้า 71,46)
- jal x1,ProcedureLabel เก็บ return address แล้วกระโดด (หน้า 72)
- jalr x0,0(x1) กลับ caller (หน้า 72)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- procedure
- caller/callee
- jal
- jalr
- return address

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ขั้นหน้า 71: วาง parameter → transfer control → storage → operation → result → return

**จุดที่อาจสับสน:** x1 เป็นที่อยู่กลับ ไม่ใช่ register ผลลัพธ์

**ประโยคช่วยจำ:** ส่งค่า x10–17; กระโดด jal; กลับ jalr ผ่าน x1

### 19. Leaf procedure และ stack save/restore

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 73–76**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

leaf procedure ในตัวอย่างคำนวณ f=(g+h)−(i+j) และไม่เรียก procedure อื่น แต่ยังใช้ stack บันทึก register ที่ต้องคืนค่าก่อนกลับ. stack pointer x2/sp ลดเมื่อจองที่ และเพิ่มเมื่อคืนพื้นที่; temporary กับ saved register มีข้อตกลงการรักษาค่าต่างกัน.

**ประเด็นที่ต้องจำ**

- หน้า 73 กำหนด g,h,i,j ใน x10–x13 และผล f ใน x20
- หน้า 74 จอง stack 24 byte, save x5,x6,x20 และ load คืนก่อนกลับ
- x5–x7,x28–x31 ไม่ต้อง preserve โดย callee; x8–x9,x18–x27 ต้อง preserve เมื่อใช้งาน (หน้า 76)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- leaf procedure
- stack frame
- sp
- callee-saved/temporary

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านภาพ stack หน้า 75 ร่วมกับลำดับ save→compute→restore หน้า 74

**จุดที่อาจสับสน:** หน้า 74 มี sd x20,0(sp ขาดวงเล็บ และ add x6,x12,x1 ทั้งที่ comment บอก i+j และหน้า 73 กำหนด j=x13: ต้องตรวจสอบจากต้นฉบับ อย่าจำบรรทัดนี้เป็นโค้ดที่ถูก

**ประโยคช่วยจำ:** จอง–เก็บ–คำนวณ–คืน–กลับ

### 20. Non-leaf procedure และ factorial recursion

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 77–79**

เหตุผลการจัดระดับ: นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด

non-leaf procedure เรียก procedure อื่น จึงต้องรักษา return address และค่าที่ยังต้องใช้หลังการเรียก. ตัวอย่าง factorial ใช้ stack เก็บ x1 กับ n ใน x10, เรียก fact(n−1), โหลดค่ากลับ แล้วคูณก่อน return.

**ประเด็นที่ต้องจำ**

- non-leaf ต้องรักษา return address และ live values ข้ามการเรียก (หน้า 77)
- ตัวอย่าง fact หน้า 79 จอง 16 byte; save x1 ที่ 8(sp), x10 ที่ 0(sp)
- base case ใน assembly หน้า 79 ตั้ง x10=1; recursive case คูณ n×fact(n−1)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- non-leaf
- recursion
- stack frame
- live values
- factorial

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่หน้า 79 จาก save → ตรวจ n<1 → call fact → restore n/x1 → mul → return

**จุดที่อาจสับสน:** หน้า 78 C เขียน return f ซึ่งไม่ได้กำหนด แต่ assembly หน้า 79 base case คืน 1; หน้า 79 ยังตั้งหัวข้อ Leaf ทั้งที่เป็น recursion: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** เรียกซ้อนต้องเก็บทางกลับและค่าที่จะใช้ต่อ

### 21. Memory layout, activation record และข้อมูลขนาดย่อย

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 80–83**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

ภาพ layout วาง text, static data, heap และ stack คนละบริเวณ; activation record เก็บบริบทของ procedure. คำสั่ง load ขนาด byte/halfword/word มีแบบ sign-extend และ zero-extend ส่วน store เขียนเพียงบิตต่ำตามขนาดข้อมูล.

**ประเด็นที่ต้องจำ**

- text/static data/heap/stack ตามภาพหน้า 80
- activation record ตามหน้า 81 ใช้จัด context ของ call
- lb/lh/lw sign-extend; lbu/lhu/lwu zero-extend; sb/sh/sw เก็บ 8/16/32 บิตต่ำ (หน้า 83)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- text
- static data
- heap
- stack
- activation record
- lb/lbu
- sb

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบ lb กับ lbu เมื่อ byte บิตบนสุดเป็น 1: แบบแรกขยาย sign แบบหลังเติม 0 (หน้า 83)

**จุดที่อาจสับสน:** อย่าเหมารวม load ทุกแบบเป็น sign extension; ชื่อที่ลงท้าย u คือ unsigned/zero extension

**ประโยคช่วยจำ:** มี u เติมศูนย์; ไม่มี u ขยายเครื่องหมาย

### 22. Self-study: String copy

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 84–86**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

หน้า 84 แยกส่วนถัดไปเป็น Self-study. ตัวอย่าง strcpy วนคัดลอกอักขระจาก source ไป destination ทีละ byte จนพบ NUL แล้วคืน stack/register; นำมาใช้ฝึกอ่าน address, lbu, sb และ branch.

**ประเด็นที่ต้องจำ**

- string จบเมื่อ byte เป็น 0 (หน้า 85–86)
- lbu อ่าน byte, sb เขียน byte, beq ตรวจ NUL (หน้า 86)
- ใช้ x19 เป็น index และ stack บันทึก x19 (หน้า 86)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Self-study
- strcpy
- NUL
- lbu/sb

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ติดตามหนึ่งรอบ loop: หา address source → lbu → หา address destination → sb → ตรวจ 0 → เพิ่ม index

**จุดที่อาจสับสน:** หน้า 86 เขียน add x5,x19,x10 แต่ comment ว่า address ของ y[i], ขณะที่ x10 เป็น x และ x11 เป็น y ตามตัวอย่าง: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** อ่านหนึ่งไบต์–เขียนหนึ่งไบต์–เช็กศูนย์

### 23. Self-study: Wide immediate และ branch address

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 87–91**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

ค่าคงที่ขนาดเกิน immediate 12 บิตประกอบด้วย lui เติมส่วนบนแล้ว addi เติมส่วนล่าง. สไลด์อธิบาย branch address แบบ PC-relative, jump ด้วย JAL และการประกอบ jump ไกลด้วย LUI/JALR พร้อมภาพสรุปรูปแบบ addressing/encoding.

**ประเด็นที่ต้องจำ**

- lui วาง constant 20 บิตที่ [31:12] และล้าง [11:0] (หน้า 87)
- ตัวอย่าง lui x19,976; addi x19,x19,128 (หน้า 87)
- branch target = PC + immediate×2 ตามหน้า 88; JAL และ JALR หน้า 89

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- lui
- addi
- PC-relative
- SB/UJ format
- JAL/JALR

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ถ้าตีตามตัวเลขคำสั่ง 976×4096+128 = 0x003D0080

**จุดที่อาจสับสน:** หน้า 87 comment ที่ addi 128 เขียน 0x500 และภาพบิตท้าย 0101 0000 0000 (=0x500), ไม่ตรงกับ 128 (=0x080): ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** lui เติมบน; addi เติมล่าง; branch อิง PC

### 24. Self-study: Atomic operations

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 92–94**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

เมื่อหลายหน่วยทำงานกับข้อมูลร่วมกัน อาจเกิด data race จึงต้องมีการอ่านและเขียนแบบ atomic. สไลด์ใช้ lr.d เพื่ออ่านพร้อม reservation แล้ว sc.d พยายามเขียน; sc.d คืน 0 เมื่อสำเร็จและ nonzero เมื่อไม่สำเร็จ จึงวนลองใหม่ได้.

**ประเด็นที่ต้องจำ**

- data race เกิดจาก access ร่วมที่ลำดับเวลาเปลี่ยนผล (หน้า 92)
- lr.d อ่านและตั้ง reservation; sc.d เขียนแบบมีเงื่อนไข (หน้า 93)
- sc.d สำเร็จคืน 0; ล้มเหลวคืน nonzero; หน้า 94 แสดง retry และ unlock ด้วย sd x0,0(x20)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- data race
- atomic
- lr.d
- sc.d
- reservation

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามลูกศร retry หน้า 94 เมื่อ sc.d ไม่สำเร็จแล้วลองใหม่

**จุดที่อาจสับสน:** อย่าสับสนค่า 0 จาก sc.d กับค่าข้อมูลที่ต้องการเขียน; เป็นสถานะสำเร็จ

**ประโยคช่วยจำ:** LR จอง; SC ลองเขียน; ศูนย์คือสำเร็จ

### 25. Self-study: จาก source ไป executable และ runtime

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 95–101**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

สไลด์ไล่ source ผ่าน compiler/assembler/linker/loader ไปจนรันโปรแกรม. Object module มี text/data/relocation/symbol/debug; linker รวมและแก้ references, loader วางใน memory และเริ่ม main. ช่วงท้ายยก dynamic linking และ Java VM/JIT เป็นแนวทางเชื่อม/แปลตอนรัน.

**ประเด็นที่ต้องจำ**

- object module: header,text,static data,relocation,symbol,debug (หน้า 96)
- linker merge object files, resolve symbols, patch locations (หน้า 97)
- loader จัด memory/text/data/stack/registers แล้วเริ่มโปรแกรม (หน้า 98)
- dynamic linking กับ lazy linkage หน้า 99–100; JVM/JIT หน้า 101

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- compiler
- assembler
- object module
- linker
- loader
- dynamic linking
- JVM/JIT

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านภาพหน้า 95 เป็นสายงาน source→object→executable→memory แล้วจับคู่หน้าที่หน้า 96–98

**จุดที่อาจสับสน:** linker แก้การเชื่อม object files; loader นำ executable ลง memory; อย่าสลับสองขั้น

**ประโยคช่วยจำ:** แปล–รวม–โหลด–รัน

### 26. Self-study: Swap procedure

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 102–103**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

ตัวอย่าง swap รับ base address กับ index แล้วคำนวณตำแหน่งของ v[k] และ v[k+1] โดยเลื่อน index ซ้าย 3 บิตสำหรับ doubleword. จากนั้น load สองค่าและ store สลับตำแหน่ง ก่อน return.

**ประเด็นที่ต้องจำ**

- shift left 3 = index×8 byte (หน้า 103)
- ld จาก offset 0 และ 8 แล้ว sd กลับสลับค่า (หน้า 103)
- เป็น leaf procedure ในตัวอย่างหน้า 102–103

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- swap
- index×8
- ld/sd

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ติดตาม address base+8k แล้วอีกตำแหน่งคือ base+8k+8

**จุดที่อาจสับสน:** อย่าสลับ offset 8 byte ของสมาชิกถัดไปกับ index k+1 ที่ต้องคูณ 8

**ประโยคช่วยจำ:** คูณ 8–โหลดคู่–เก็บสลับ

### 27. Self-study: Sort loops และการรักษา register

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 104–107**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

ตัวอย่าง sort แยก outer loop และ inner loop เพื่อตรวจลำดับสมาชิกติดกันแล้วเรียก swap เมื่อจำเป็น. การเรียก swap ทำให้ sort เป็น non-leaf และต้องรักษา register ที่ใช้ต่อ รวมถึง return address ตามภาพ stack หน้า 107.

**ประเด็นที่ต้องจำ**

- หน้า 104 ให้ C sort กับตัวแปร i,j และการเรียก swap
- หน้า 105 outer loop; หน้า 106 inner loop ตรวจ j≥0 และ v[j]>v[j+1]
- หน้า 107 จอง 40 byte สำหรับ register 5 ตัวในตัวอย่าง

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- outer/inner loop
- non-leaf sort
- swap
- save/restore

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 106 ใช้ slli j,3 เพื่อเข้าถึง doubleword สองตัวติดกัน ก่อน branch และ call swap

**จุดที่อาจสับสน:** หน้า 107 หัวข้อ Restore saved registers แต่ใช้ sd ทุกบรรทัดซึ่งเป็น store ไม่ใช่ load: ต้องตรวจสอบจากต้นฉบับ อย่าคัดลอกเป็นขั้น restore ที่ถูก

**ประโยคช่วยจำ:** วนรอบนอก–เทียบคู่ใน–swap–คืนค่าที่เก็บ

### 28. Self-study: บทเรียนจากการวัดผลและ compiler

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 108–110**

เหตุผลการจัดระดับ: รายละเอียดประกอบหรือส่วน Self-study ที่อ่านหลังแกนหลัก

กราฟเปรียบเทียบผลของ optimization และภาษา/algorithm ภายใต้ตัวอย่างในสไลด์. บทเรียนสรุปว่า instruction count หรือ CPI เดี่ยว ๆ ไม่พออธิบาย performance ทั้งหมด; ผลของ optimization ขึ้นกับ algorithm และ JIT ต่างจาก interpreter ตามการใช้งาน.

**ประเด็นที่ต้องจำ**

- อ่านกราฟหน้า 108–109 เป็นการเปรียบเทียบกรณีตัวอย่าง ไม่ใช่ค่ามาตรฐาน
- หน้า 110 ย้ำ algorithm สำคัญ และไม่มีเทคนิคใดแก้ algorithm ที่ไม่เหมาะได้ทั้งหมด

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- instruction count
- CPI
- compiler optimization
- JIT/interpreter

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้กราฟหน้า 108–109 ชี้ว่าการเปลี่ยน algorithm/ภาษา/optimization อาจเปลี่ยนเวลา

**จุดที่อาจสับสน:** อย่าทำนายผล performance จาก CPI เพียงตัวเดียวตามบทเรียนหน้า 110

**ประโยคช่วยจำ:** เริ่มที่ algorithm; วัดเวลาจริงและบริบท

### 29. Self-study: Array indexing เทียบ pointer

**🟡 สำคัญ** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 111–113**

เหตุผลการจัดระดับ: ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก

สไลด์เทียบ loop ล้าง array ด้วย index กับ pointer แล้วแสดง assembly สองแนว. แบบ index คำนวณ offset จาก i; แบบ pointer เพิ่ม address ไปทีละ element. ประเด็นคือ compiler อาจ optimize การคำนวณ address ได้ และควรเลือกโค้ดที่อ่านและตรวจได้.

**ประเด็นที่ต้องจำ**

- หน้า 112 เปรียบเทียบ clear1(array[i]) กับ clear2(*p)
- assembly ตัวอย่างใช้ slli index,3 และ pointer increment 8 (หน้า 112)
- หน้า 113 อธิบาย compiler optimization ทำให้ความต่างของรูปเขียนไม่ตายตัว

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- array indexing
- pointer
- address arithmetic
- compiler optimization

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ภาพหน้า 112 ว่า x7 เป็น endpoint ในแบบ pointer และ x6 เป็น byte offset ในแบบ index

**จุดที่อาจสับสน:** C ตัวอย่างประกาศ int แต่ assembly เลื่อน 3/เพิ่ม 8 เป็นขนาด doubleword; ไม่สอดคล้องกัน: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** index คูณขนาด; pointer เดินทีละช่อง

### 30. Self-study: MIPS เทียบ RISC-V และ extensions

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter03_RiscV.pdf, **หน้า 114–117**

เหตุผลการจัดระดับ: รายละเอียดประกอบหรือส่วน Self-study ที่อ่านหลังแกนหลัก

ท้ายบทเทียบ MIPS ซึ่งเป็นสถาปัตยกรรมก่อนหน้ากับ RISC-V ผ่านตาราง/รูป encoding แล้วสรุป RV64I/RV32I และกลุ่ม extension. ตัวอักษร M, A, F, D, C แสดงชุดความสามารถเพิ่มเติมตามรายการในสไลด์.

**ประเด็นที่ต้องจำ**

- หน้า 114–115 เทียบ MIPS/RISC-V และ instruction encoding
- หน้า 116 ระบุ RV64I/RV32I และคำสั่ง word บางแบบ
- หน้า 117: M=integer multiply/divide, A=atomic, F=single float, D=double float, C=compressed

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- MIPS
- RV64I/RV32I
- M/A/F/D/C extensions

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านตารางหน้า 117 แล้วจับคู่ชื่อ extension กับหน้าที่

**จุดที่อาจสับสน:** หน้า 116 มีชื่อ srlw ซ้ำในรายการที่ควรต่างกัน: ต้องตรวจสอบจากต้นฉบับ; อย่าอนุมานรายการแก้ไขเอง

**ประโยคช่วยจำ:** M คูณหาร, A atomic, F/D float, C compressed

## 3. Roadmap ทบทวน

1. **1 · รูปแบบข้อมูล** — เริ่มชนิดข้อมูลและ unsigned ก่อนเลือกวิธีแทน signed (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–8)
2. **2 · Signed representation** — เทียบ Sign & Magnitude → complement → 2’s → bias พร้อมช่วงค่า/ศูนย์ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 9–24)
3. **3 · Floating และอักขระ** — ต่อ floating-point, IEEE, binary fraction แล้วค่อย ASCII (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 25–37)
4. **4 · ISA และข้อมูลในเครื่อง** — RISC-V arithmetic → register → memory/endianness → signed/immediate (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 41–53)
5. **5 · คำสั่งและ control flow** — อ่าน R/I/S encoding ก่อน logical operations และ branch/loop (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 54–70)
6. **6 · Procedure** — call/return → leaf stack → non-leaf recursion → memory layout (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 71–83)
7. **7 · Self-study** — String/wide immediate → atomic/toolchain → swap/sort → optimization/array/extensions (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84–117)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · อ่านภาพรวม

อ่านตาม roadmap และเปิดภาพต้นฉบับทุกหัวข้อ พร้อมทำเครื่องหมายสูตร/field/register ที่ยังจำไม่ได้

**เกณฑ์ผ่าน:** อธิบายว่าบทนี้ต่อจากรหัสข้อมูลไปถึงการรันโปรแกรมอย่างไร

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–117

### รอบ 2 · แกนคำนวณ

ฝึกช่วงค่า signed/unsigned, 1’s/2’s/bias, IEEE และ byte offset ด้วยตัวอย่างจากสไลด์

**เกณฑ์ผ่าน:** คำนวณ 6+(−5), biased-127 และ A[8]/A[12] ได้ พร้อมชี้ตัวอย่างผิด

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 9–31, 49–53

### รอบ 3 · ภาษาเครื่อง

ท่อง register/format แล้วไล่ arithmetic, load/store, logical, branch และ procedure ด้วยภาพ

**เกณฑ์ผ่าน:** อ่าน add x9,x20,x21 และ jal/jalr พร้อม field/บทบาท register ได้

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 41–83

### รอบ 4 · Self-study

ไล่ภาพ/โค้ดประกอบเฉพาะหน้า 84–117 และจดจุดที่ต้องตรวจจากต้นฉบับ

**เกณฑ์ผ่าน:** อธิบาย strcpy, lr/sc, linker/loader, swap/sort และ extensions ได้

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84–117

### รอบ 5 · ทดสอบเว้นระยะ

สุ่มแบบทดสอบ/Flashcard; ทวนเฉพาะข้อผิดแล้วกลับมาทำใหม่ในวันถัดไปตามเวลาที่มี

**เกณฑ์ผ่าน:** ตอบคำถาม 3 ข้อต่อหัวข้อครบ และแยกข้อที่สไลด์ขัดกันได้

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–117

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1 จำนวน/IEEE/ASCII หน้า 4–37; วัน 2 RISC-V register/memory/format/branch/procedure หน้า 41–83; วัน 3 Self-study หน้า 84–117 แล้วสุ่มข้อสอบและทวนจุดผิด
- **ถ้าเหลือ 1 วัน:** เริ่ม 2’s/IEEE หน้า 18–31 → RISC-V register/format/memory หน้า 45–59 → branch/procedure หน้า 65–79 → Self-study เฉพาะหัวข้อที่ยังตอบไม่ได้และข้อผิดในแบบทดสอบ
- **ถ้าเหลือ 3 ชั่วโมง:** 0–35 นาที signed/IEEE หน้า 9–31; 35–90 นาที register/memory/format หน้า 45–59; 90–135 นาที branch/procedure หน้า 65–79; 135–160 นาที Self-study ภาพสรุป/คำศัพท์ หน้า 84–117; 160–180 นาทีสุ่มข้อสอบและทวนจุดขัดกัน

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

ให้ความสำคัญกับนิยาม สูตร encoding, register, branch และ stack ก่อน เพราะสไลด์ใช้เป็นฐานของตัวอย่างต่อเนื่อง; นี่เป็นการจัดลำดับเพื่อทบทวน ไม่ใช่การยืนยันแนวข้อสอบจริง

- **ควรท่องจำ:** ช่วงค่า/สูตร signed และ bias, IEEE 1–8–23/1–11–52, ชื่อ register, R/I/S field, branch/jal/jalr, M/A/F/D/C (หน้า 5, 9–29, 45–46, 54–58, 65–72, 117)
- **ควรฝึกโจทย์:** กลับบิต/บวกหนึ่ง/ทิ้ง carry, biased-127, 101.1101₂, byte offset A[8]/A[12], add encoding และการไล่ if/loop/stack (หน้า 16–31, 50, 56, 66–79)
- **ควรเข้าใจแนวคิด:** endian, load/store, signed/unsigned comparison, caller/callee, atomics, linker/loader และผลของ algorithm/optimization (หน้า 48–51, 69–81, 92–110)
- **เตรียมข้อสอบแบบผสม:** เลือกตอบจับคู่ศัพท์/field; อัตนัยอธิบายวิธีแทนค่าและ call flow; คำนวณจากตัวอย่างในสไลด์; วิเคราะห์โค้ด/ภาพและชี้จุดไม่สอดคล้อง

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 30 ข้อ, อัตนัย 30 ข้อ, วิเคราะห์ 21 ข้อ, คำนวณ 9 ข้อ

### ข้อมูลเชิงปริมาณและระบบเลข

**ข้อ 1 · เลือกตอบ: Unsigned n บิตมีค่าสูงสุดเท่าไร?**

- A. 2^n−1
- B. 2^(n−1)−1
- C. 2^n
- D. n−1

เฉลย: 2^n−1 ตามหน้า 5

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–8

**ข้อ 2 · อัตนัย: ข้อมูล quantitative แบ่งอย่างไร?**

เฉลย: integer และ non-integer; integer แยก signed/unsigned ตามหน้า 6–8

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–8

**ข้อ 3 · วิเคราะห์: เลขฐาน 16 ใช้สัญลักษณ์ใดเพิ่มจาก 0–9?**

เฉลย: A–F ตามหน้า 7

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 4–8

### Sign & Magnitude

**ข้อ 4 · เลือกตอบ: 8-bit Sign & Magnitude มีค่าสูงสุดเท่าไร?**

- A. +127
- B. +128
- C. +255
- D. +256

เฉลย: +127 เพราะมี magnitude 7 บิต

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 9–12

**ข้อ 5 · อัตนัย: เหตุใดแบบนี้มีศูนย์สองรหัส?**

เฉลย: magnitude 0 จับคู่กับ sign 0 หรือ sign 1 ได้

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 9–12

**ข้อ 6 · วิเคราะห์: รหัส 10000000 ใน 8-bit Sign & Magnitude หมายถึงอะไร?**

เฉลย: negative zero ตามหน้า 11

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 9–12

### (r−1)’s และ r’s complement

**ข้อ 7 · เลือกตอบ: ฐานสองเรียก (r−1)’s complement ว่าอะไร?**

- A. 1’s complement
- B. 2’s complement
- C. 9’s complement
- D. biased-127

เฉลย: 1’s complement

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 13–15

**ข้อ 8 · อัตนัย: สูตร r’s complement ของ m ใน n หลักคืออะไร?**

เฉลย: r^n−m ตามสูตรหน้า 14

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 13–15

**ข้อ 9 · คำนวณ: จงหา 10’s complement ของ 382 ในสามหลักตามสไลด์**

เฉลย: 1000−382=618

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 13–15

### 1’s complement และ end-around carry

**ข้อ 10 · เลือกตอบ: 1’s complement หาอย่างไร?**

- A. กลับทุกบิต
- B. กลับ sign bit เท่านั้น
- C. เติม bias
- D. เลื่อนซ้ายหนึ่งบิต

เฉลย: กลับทุกบิตตามหน้า 16

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 16–17

**ข้อ 11 · อัตนัย: end-around carry ทำอะไร?**

เฉลย: นำ carry-out กลับไปบวกกับผลบวก

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 16–17

**ข้อ 12 · วิเคราะห์: ทำไมตัวอย่าง 3-bit +6 หน้า 17 จึงควรตรวจต้นฉบับ?**

เฉลย: 3-bit 1’s complement มีช่วง −3 ถึง +3 จึงแทน +6 ไม่ได้

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 16–17

### 2’s complement และการบวก

**ข้อ 13 · เลือกตอบ: 8-bit 2’s complement มีค่าต่ำสุดเท่าไร?**

- A. −128
- B. −127
- C. 0
- D. −255

เฉลย: −128

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 18–22

**ข้อ 14 · อัตนัย: หา 2’s complement จากเลขบวกอย่างไร?**

เฉลย: กลับทุกบิตแล้วบวก 1

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 18–22

**ข้อ 15 · วิเคราะห์: ตัวอย่าง 4-bit 6 + (−5) ในหน้า 20 ได้อะไร?**

เฉลย: 0110 + 1011 = 1 0001; ทิ้ง carry ได้ 0001 หรือ +1

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 18–22

### Bias / Excess notation

**ข้อ 16 · เลือกตอบ: biased-127 ของ 01111111 คืออะไร?**

- A. 0
- B. −1
- C. +1
- D. +127

เฉลย: 127−127=0

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 23–24

**ข้อ 17 · อัตนัย: สูตรแปล biased notation คืออะไร?**

เฉลย: unsigned value − bias B

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 23–24

**ข้อ 18 · คำนวณ: จงหาค่าของ 11111111 ใน biased-127**

เฉลย: 255−127=+128

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 23–24

### Floating-point: sign, mantissa, exponent

**ข้อ 19 · เลือกตอบ: สัญลักษณ์ e ใน N=(−1)^s m 2^e คืออะไร?**

- A. exponent
- B. sign
- C. mantissa
- D. bias

เฉลย: exponent

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 25–26

**ข้อ 20 · อัตนัย: ส่วนประกอบ floating-point ที่หน้า 25 ระบุมีอะไร?**

เฉลย: sign, mantissa, exponent และ radix

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 25–26

**ข้อ 21 · วิเคราะห์: −0.000321 ในรูปที่สไลด์ยกเป็นอย่างไร?**

เฉลย: −3.21×10^−4

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 25–26

### IEEE single/double และ biased exponent

**ข้อ 22 · เลือกตอบ: single precision ใช้ exponent กี่บิต?**

- A. 8
- B. 11
- C. 23
- D. 52

เฉลย: 8 บิต

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 27–29

**ข้อ 23 · อัตนัย: สมการ normalized single ในสไลด์คืออะไร?**

เฉลย: N=(−1)^s(1.m)2^(E−127)

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 27–29

**ข้อ 24 · คำนวณ: ถ้า e=4 ค่า E เท่าไร?**

เฉลย: 4+127=131

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 27–29

### แปลงเศษส่วนฐานสองและตัวอย่าง single

**ข้อ 25 · เลือกตอบ: 101.1101₂ มีค่าเท่าไร?**

- A. 5.8125
- B. 5.625
- C. 6.8125
- D. 17.15

เฉลย: 5.8125 ตามหน้า 30

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 30–31

**ข้อ 26 · อัตนัย: การ normalize ตัวอย่าง 17.15 หน้า 31 ทำให้ e เท่าไร?**

เฉลย: e=4

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 30–31

**ข้อ 27 · คำนวณ: เหตุใดบิตของ 17.15 หน้า 31 ต้องอ่านเป็นค่าประมาณ?**

เฉลย: เศษส่วนที่พิมพ์มีเพียงบางบิตและไม่ให้ค่า 17.15 แบบตรงทั้งหมด

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 30–31

### อักขระ ASCII และ Unicode ในสไลด์

**ข้อ 28 · เลือกตอบ: ASCII พื้นฐานในสไลด์มีกี่รหัส?**

- A. 128
- B. 64
- C. 256
- D. 1024

เฉลย: 128 รหัส 7 บิต

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 32–38

**ข้อ 29 · อัตนัย: A กับ a ในตัวอย่างมีรหัส hex อะไร?**

เฉลย: A=0x41; a=0x61

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 32–38

**ข้อ 30 · วิเคราะห์: รหัสอักขระตัวเลขต่างจาก numeric value อย่างไร?**

เฉลย: เก็บรหัสแทนตัวอักษร ไม่ใช่ค่าจำนวนสำหรับคำนวณโดยตรง

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 32–38

### ISA และคำสั่งคำนวณสามตัวถูกดำเนินการ

**ข้อ 31 · เลือกตอบ: add a,b,c ให้ค่าใด?**

- A. a=b+c
- B. c=a+b
- C. b=a+c
- D. a=b−c

เฉลย: a=b+c

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 39–44

**ข้อ 32 · อัตนัย: หลักการออกแบบที่หน้า 43 ย้ำคืออะไร?**

เฉลย: simplicity favors regularity

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 39–44

**ข้อ 33 · คำนวณ: ต้องใช้การคำนวณกี่ขั้นเพื่อทำ f=(g+h)−(i+j) ในหน้า 44?**

เฉลย: สอง add เพื่อได้ผลย่อย แล้วหนึ่ง sub เพื่อหาผลลัพธ์

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 39–44

### RISC-V register 32 ตัวและบทบาท

**ข้อ 34 · เลือกตอบ: register ใดเป็น stack pointer?**

- A. x2
- B. x0
- C. x1
- D. x10

เฉลย: x2

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 45–47

**ข้อ 35 · อัตนัย: temporary registers ที่หน้า 46 ระบุมีกลุ่มใด?**

เฉลย: x5–x7 และ x28–x31

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 45–47

**ข้อ 36 · วิเคราะห์: word กับ doubleword ตามหน้า 45 ต่างกันอย่างไร?**

เฉลย: word 32 บิต; doubleword 64 บิต

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 45–47

### Byte addressing, endian และ load/store

**ข้อ 37 · เลือกตอบ: A[8] แบบ doubleword มี byte offset เท่าไร?**

- A. 64
- B. 8
- C. 32
- D. 96

เฉลย: 8×8=64

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 48–51

**ข้อ 38 · อัตนัย: RISC-V ใช้ endian แบบใดตามหน้า 49?**

เฉลย: little-endian

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 48–51

**ข้อ 39 · คำนวณ: A[12] ในตัวอย่างเก็บกลับที่ offset เท่าไร?**

เฉลย: 12×8=96

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 48–51

### Immediate และ signed/unsigned

**ข้อ 40 · เลือกตอบ: addi x22,x22,4 ทำอะไร?**

- A. x22 เพิ่ม 4
- B. x22 ลด 4
- C. load memory offset 4
- D. เก็บ x22 ที่ address 4

เฉลย: เพิ่ม x22 อีก 4

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 52–53

**ข้อ 41 · อัตนัย: signed 2’s complement n บิตมีช่วงเท่าไร?**

เฉลย: −2^(n−1) ถึง 2^(n−1)−1

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 52–53

**ข้อ 42 · คำนวณ: sign extension ทำอย่างไร?**

เฉลย: ทำบิตใหม่ด้านบนให้ตรงกับ sign bit ของค่าเดิม

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 52–53

### R/I/S instruction formats และ encoding

**ข้อ 43 · เลือกตอบ: R-format กว้างกี่บิต?**

- A. 32
- B. 16
- C. 64
- D. 12

เฉลย: 32 บิต

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 54–59

**ข้อ 44 · อัตนัย: field ของ S-format immediate แบ่งอย่างไร?**

เฉลย: imm[11:5] และ imm[4:0]

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 54–59

**ข้อ 45 · วิเคราะห์: add x9,x20,x21 ตามหน้า 56 มี hex อะไร?**

เฉลย: 015A04B3₁₆

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 54–59

### Logical operations และ bit mask

**ข้อ 46 · เลือกตอบ: bitwise XOR ให้ 1 เมื่อใด?**

- A. บิตต่างกัน
- B. บิตเหมือนกัน
- C. ทั้งคู่เป็น 0
- D. ทั้งคู่เป็น 1 เท่านั้น

เฉลย: เมื่อบิตสองฝั่งต่างกัน

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 60–64

**ข้อ 47 · อัตนัย: AND mask ใช้ทำอะไรตามหน้า 62?**

เฉลย: รักษาบิตที่ mask เป็น 1 และตัดบิตที่ mask เป็น 0

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 60–64

**ข้อ 48 · วิเคราะห์: shift unsigned ไปซ้าย i ตำแหน่งสัมพันธ์กับอะไร?**

เฉลย: คูณ 2^i ตามหน้า 61

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 60–64

### Branches, loop และ signed comparison

**ข้อ 49 · เลือกตอบ: bne branch เมื่อใด?**

- A. ค่าต่างกัน
- B. ค่าเท่ากัน
- C. ค่าติดลบ
- D. overflow

เฉลย: เมื่อสอง register ไม่เท่ากัน

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 65–70

**ข้อ 50 · อัตนัย: basic block ตามหน้า 68 คืออะไร?**

เฉลย: ช่วงคำสั่งต่อเนื่องที่ไม่มี branch ภายใน ยกเว้นท้าย และไม่มีเป้าหมาย branch ภายใน ยกเว้นต้น

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 65–70

**ข้อ 51 · วิเคราะห์: all-ones เทียบ +1 แบบ signed กับ unsigned ต่างกันอย่างไร?**

เฉลย: signed แปลเป็น −1 จึงน้อยกว่า +1; unsigned แปลเป็นค่าบวกสูง จึงมากกว่า +1

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 65–70

### Procedure call, parameters และ return

**ข้อ 52 · เลือกตอบ: return address อยู่ register ใด?**

- A. x1
- B. x0
- C. x2
- D. x10

เฉลย: x1

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 71–72

**ข้อ 53 · อัตนัย: jal x1,label ทำอะไร?**

เฉลย: บันทึกที่อยู่กลับใน x1 และย้าย control ไป label

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 71–72

**ข้อ 54 · วิเคราะห์: คำสั่งกลับ caller ในหน้า 72 คืออะไร?**

เฉลย: jalr x0,0(x1)

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 71–72

### Leaf procedure และ stack save/restore

**ข้อ 55 · เลือกตอบ: leaf procedure ต่างจาก non-leaf อย่างไร?**

- A. ไม่เรียก procedure อื่น
- B. ไม่มี register
- C. ไม่ใช้ stack ได้เสมอ
- D. ไม่มี return

เฉลย: leaf ไม่เรียก procedure อื่น

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 73–76

**ข้อ 56 · อัตนัย: กลุ่ม saved register หน้า 76 คืออะไร?**

เฉลย: x8–x9 และ x18–x27 (x8 เป็น frame pointer ด้วย)

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 73–76

**ข้อ 57 · วิเคราะห์: เพราะเหตุใด add x6,x12,x1 หน้า 74 ต้องตรวจต้นฉบับ?**

เฉลย: x1 เป็น return address แต่คำอธิบายต้องการ i+j และหน้า 73 ระบุ j ใน x13

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 73–76

### Non-leaf procedure และ factorial recursion

**ข้อ 58 · เลือกตอบ: non-leaf ต้องรักษาอะไรเป็นพิเศษ?**

- A. return address และค่าที่ยังใช้อยู่
- B. x0 อย่างเดียว
- C. opcode
- D. endian

เฉลย: return address และ live values

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 77–79

**ข้อ 59 · อัตนัย: ตัวอย่าง factorial เก็บ x1 และ x10 ที่ไหน?**

เฉลย: บน stack หลังจอง 16 byte: x1 ที่ 8(sp), x10 ที่ 0(sp)

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 77–79

**ข้อ 60 · วิเคราะห์: base case ของ C/assembly ในหน้า 78–79 ขัดกันอย่างไร?**

เฉลย: C ระบุ return f ที่ไม่ประกาศ; assembly ตั้งผลเป็น 1

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 77–79

### Memory layout, activation record และข้อมูลขนาดย่อย

**ข้อ 61 · เลือกตอบ: lbu ขยาย byte แบบใด?**

- A. zero-extend
- B. sign-extend
- C. rotate
- D. ไม่ขยาย

เฉลย: zero-extend

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 80–83

**ข้อ 62 · อัตนัย: memory layout หน้า 80 แบ่งหลัก ๆ อย่างไร?**

เฉลย: text, static data, heap และ stack

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 80–83

**ข้อ 63 · วิเคราะห์: sb เก็บกี่บิตต่ำตามหน้า 83?**

เฉลย: 8 บิต

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 80–83

### Self-study: String copy

**ข้อ 64 · เลือกตอบ: strcpy หยุดเมื่อเจออะไร?**

- A. NUL byte
- B. space
- C. ตัวอักษร A
- D. ครบ 8 byte

เฉลย: NUL byte หรือ 0

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84–86

**ข้อ 65 · อัตนัย: หน้า 86 ใช้คำสั่งใดอ่านและเขียน byte?**

เฉลย: lbu อ่าน; sb เขียน

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84–86

**ข้อ 66 · วิเคราะห์: จุดขัดกันของ address y[i] หน้า 86 คืออะไร?**

เฉลย: comment ว่า y[i] แต่บรรทัดใช้ x10 ซึ่งเป็น x ตามการกำหนด register ในตัวอย่าง

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84–86

### Self-study: Wide immediate และ branch address

**ข้อ 67 · เลือกตอบ: lui เติม constant กี่บิตในช่องบน?**

- A. 20
- B. 12
- C. 8
- D. 32

เฉลย: 20 บิต

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 87–91

**ข้อ 68 · อัตนัย: branch target ตามหน้า 88 คำนวณอย่างไร?**

เฉลย: PC + immediate×2

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 87–91

**ข้อ 69 · คำนวณ: ทำไมตัวอย่าง addi 128 หน้า 87 ต้องตรวจต้นฉบับ?**

เฉลย: 128 เป็น 0x080 แต่ comment/ภาพแสดง 0x500

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 87–91

### Self-study: Atomic operations

**ข้อ 70 · เลือกตอบ: sc.d คืนค่าอะไรเมื่อสำเร็จ?**

- A. 0
- B. 1
- C. −1
- D. address

เฉลย: 0

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 92–94

**ข้อ 71 · อัตนัย: lr.d ทำหน้าที่อะไร?**

เฉลย: load พร้อมสร้าง reservation สำหรับคู่ sc.d

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 92–94

**ข้อ 72 · วิเคราะห์: เหตุใดตัวอย่างหน้า 94 จึงต้อง retry?**

เฉลย: sc.d อาจล้มเหลวหาก reservation ไม่คงอยู่/ข้อมูลถูกเปลี่ยน

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 92–94

### Self-study: จาก source ไป executable และ runtime

**ข้อ 73 · เลือกตอบ: ขั้นใด resolve symbols ระหว่าง object files?**

- A. linker
- B. loader
- C. register
- D. ALU

เฉลย: linker

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 95–101

**ข้อ 74 · อัตนัย: object module หน้า 96 มีส่วนสำคัญใดบ้าง?**

เฉลย: header, text, static data, relocation, symbol และ debug

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 95–101

**ข้อ 75 · วิเคราะห์: dynamic linking ต่างจาก static link ในจังหวะใดตามสไลด์?**

เฉลย: เชื่อม library บางส่วนขณะรัน/เมื่อจำเป็น แทนการรวมทั้งหมดก่อนรัน

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 95–101

### Self-study: Swap procedure

**ข้อ 76 · เลือกตอบ: สมาชิก doubleword ถัดไปห่างกี่ byte?**

- A. 8
- B. 1
- C. 4
- D. 16

เฉลย: 8 byte

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 102–103

**ข้อ 77 · อัตนัย: swap หน้า 103 คำนวณ address v[k] อย่างไร?**

เฉลย: base address + k×8

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 102–103

**ข้อ 78 · คำนวณ: swap สลับค่าด้วยคำสั่ง memory กลุ่มใด?**

เฉลย: ld สองค่า แล้ว sd กลับสลับตำแหน่ง

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 102–103

### Self-study: Sort loops และการรักษา register

**ข้อ 79 · เลือกตอบ: sort เรียก procedure ใดในตัวอย่าง?**

- A. swap
- B. strcpy
- C. fact
- D. loader

เฉลย: swap

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 104–107

**ข้อ 80 · อัตนัย: inner loop หน้า 106 ตรวจอะไร?**

เฉลย: j≥0 และ v[j]>v[j+1] ก่อนเรียก swap

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 104–107

**ข้อ 81 · วิเคราะห์: เหตุใด restore หน้า 107 ต้องตรวจต้นฉบับ?**

เฉลย: บรรทัดใต้ Restore ใช้ sd ซึ่งเขียน memory ไม่ได้โหลดค่ากลับเข้า register

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 104–107

### Self-study: บทเรียนจากการวัดผลและ compiler

**ข้อ 82 · เลือกตอบ: สไลด์หน้า 110 เตือนเรื่องใด?**

- A. CPI อย่างเดียวไม่พอ
- B. CPI บอกทุกอย่าง
- C. algorithm ไม่สำคัญ
- D. JIT เร็วเสมอ

เฉลย: CPI อย่างเดียวไม่พอ

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 108–110

**ข้อ 83 · อัตนัย: ทำไมกราฟหน้า 108–109 ไม่ควรใช้เป็นตัวเลขสากล?**

เฉลย: เป็นผลเปรียบเทียบของกรณี/สภาพแวดล้อมในสไลด์

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 108–110

**ข้อ 84 · วิเคราะห์: ถ้า algorithm ไม่เหมาะ optimization อย่างเดียวช่วยได้เสมอหรือไม่?**

เฉลย: ไม่; หน้า 110 ย้ำว่าการเลือก algorithm มีผลสำคัญ

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 108–110

### Self-study: Array indexing เทียบ pointer

**ข้อ 85 · เลือกตอบ: แบบ pointer เลื่อนอะไรในแต่ละรอบ?**

- A. address
- B. opcode
- C. bias
- D. return address

เฉลย: address ของ pointer

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 111–113

**ข้อ 86 · อัตนัย: แบบ index หา address สมาชิกอย่างไร?**

เฉลย: base + index×ขนาดสมาชิก

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 111–113

**ข้อ 87 · วิเคราะห์: เหตุใด C กับ assembly หน้า 112 ต้องตรวจต้นฉบับ?**

เฉลย: C ใช้ int แต่ assembly ใช้ stride 8 byte

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 111–113

### Self-study: MIPS เทียบ RISC-V และ extensions

**ข้อ 88 · เลือกตอบ: extension A หมายถึงอะไร?**

- A. Atomic
- B. Address
- C. ASCII
- D. Array

เฉลย: Atomic

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 114–117

**ข้อ 89 · อัตนัย: F กับ D ในหน้า 117 ต่างกันอย่างไร?**

เฉลย: F เป็น single-precision floating point; D เป็น double-precision floating point

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 114–117

**ข้อ 90 · วิเคราะห์: รายการคำสั่งหน้า 116 จุดใดต้องตรวจต้นฉบับ?**

เฉลย: มี srlw ซ้ำในรายการ

อ้างอิง: itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 114–117

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- Data Representation in Computers · หน้า 5: สไลด์แสดง Data Representation in Computers เพื่อทบทวนหัวข้อ ข้อมูลเชิงปริมาณและระบบเลข (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 5) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 5)
- Data Representation (Cont.) · หน้า 6: สไลด์แสดง Data Representation (Cont.) เพื่อทบทวนหัวข้อ ข้อมูลเชิงปริมาณและระบบเลข (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 6) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 6)
- Number Systems · หน้า 7: สไลด์แสดง Number Systems เพื่อทบทวนหัวข้อ ข้อมูลเชิงปริมาณและระบบเลข (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 7) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 7)
- 1. Sign & Magnitude Representation · หน้า 10: สไลด์แสดง 1. Sign & Magnitude Representation เพื่อทบทวนหัวข้อ Sign & Magnitude (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 10) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 10)
- Example — Sign & Magnitude · หน้า 11: สไลด์แสดง Example — Sign & Magnitude เพื่อทบทวนหัวข้อ Sign & Magnitude (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 11) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 11)
- Sign & Magnitude (Cont.) · หน้า 12: สไลด์แสดง Sign & Magnitude (Cont.) เพื่อทบทวนหัวข้อ Sign & Magnitude (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 12) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 12)
- 2. Complement Method · หน้า 13: สไลด์แสดง 2. Complement Method เพื่อทบทวนหัวข้อ (r−1)’s และ r’s complement (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 13) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 13)
- Complement Method - Deﬁnition · หน้า 14: สไลด์แสดง Complement Method - Deﬁnition เพื่อทบทวนหัวข้อ (r−1)’s และ r’s complement (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 14) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 14)
- Example - Complement Method · หน้า 15: สไลด์แสดง Example - Complement Method เพื่อทบทวนหัวข้อ (r−1)’s และ r’s complement (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 15) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 15)
- 1’s complement · หน้า 16: สไลด์แสดง 1’s complement เพื่อทบทวนหัวข้อ 1’s complement และ end-around carry (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 16) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 16)
- Addition with 1’s Complement · หน้า 17: แผนภาพ end-around carry; ตัวอย่าง 3 บิตกับ +6 เกินช่วงที่แทนได้: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 17) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 17)
- 2’s Complement · หน้า 18: สไลด์แสดง 2’s Complement เพื่อทบทวนหัวข้อ 2’s complement และการบวก (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 18) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 18)
- Example - 2’s Complement · หน้า 19: สไลด์แสดง Example - 2’s Complement เพื่อทบทวนหัวข้อ 2’s complement และการบวก (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 19) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 19)
- Example - 2’s Complement (Cont.) · หน้า 20: สไลด์แสดง Example - 2’s Complement (Cont.) เพื่อทบทวนหัวข้อ 2’s complement และการบวก (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 20) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 20)
- 1’s vs. 2’s Complement · หน้า 21: สไลด์แสดง 1’s vs. 2’s Complement เพื่อทบทวนหัวข้อ 2’s complement และการบวก (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 21) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 21)
- S & M, 1’s, & 2’s · หน้า 22: สไลด์แสดง S & M, 1’s, & 2’s เพื่อทบทวนหัวข้อ 2’s complement และการบวก (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 22) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 22)
- 3. Bias Notation · หน้า 23: สไลด์แสดง 3. Bias Notation เพื่อทบทวนหัวข้อ Bias / Excess notation (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 23) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 23)
- Bias Notation (Cont.) · หน้า 24: สไลด์แสดง Bias Notation (Cont.) เพื่อทบทวนหัวข้อ Bias / Excess notation (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 24) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 24)
- Floating Point Numbers · หน้า 25: สไลด์แสดง Floating Point Numbers เพื่อทบทวนหัวข้อ Floating-point: sign, mantissa, exponent (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 25) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 25)
- Floating Point Numbers (Cont.) · หน้า 26: สไลด์แสดง Floating Point Numbers (Cont.) เพื่อทบทวนหัวข้อ Floating-point: sign, mantissa, exponent (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 26) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 26)
- IEEE Floating Point Standard (FPS) · หน้า 27: สไลด์แสดง IEEE Floating Point Standard (FPS) เพื่อทบทวนหัวข้อ IEEE single/double และ biased exponent (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 27) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 27)
- IEEE Floating Point Standard (Cont.) · หน้า 28: สไลด์แสดง IEEE Floating Point Standard (Cont.) เพื่อทบทวนหัวข้อ IEEE single/double และ biased exponent (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 28) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 28)
- Single Precision · หน้า 29: สไลด์แสดง Single Precision เพื่อทบทวนหัวข้อ IEEE single/double และ biased exponent (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 29) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 29)
- Review - Binary Fractions · หน้า 30: สไลด์แสดง Review - Binary Fractions เพื่อทบทวนหัวข้อ แปลงเศษส่วนฐานสองและตัวอย่าง single (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 30) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 30)
- Example - Single Precision · หน้า 31: ตัวอย่าง single precision ของ 17.15; บิตเศษส่วนที่แสดงเป็นค่าโดยประมาณ: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 31) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 31)
- ASCII · หน้า 34: สไลด์แสดง ASCII เพื่อทบทวนหัวข้อ อักขระ ASCII และ Unicode ในสไลด์ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 34) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 34)
- ASCII Table · หน้า 35: สไลด์แสดง ASCII Table เพื่อทบทวนหัวข้อ อักขระ ASCII และ Unicode ในสไลด์ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 35) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 35)
- ASCII - Things to Note · หน้า 37: สไลด์แสดง ASCII - Things to Note เพื่อทบทวนหัวข้อ อักขระ ASCII และ Unicode ในสไลด์ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 37) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 37)
- RISC-V Instruction Set · หน้า 42: สไลด์แสดง RISC-V Instruction Set เพื่อทบทวนหัวข้อ ISA และคำสั่งคำนวณสามตัวถูกดำเนินการ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 42) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 42)
- Arithmetic Operations · หน้า 43: สไลด์แสดง Arithmetic Operations เพื่อทบทวนหัวข้อ ISA และคำสั่งคำนวณสามตัวถูกดำเนินการ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 43) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 43)
- Arithmetic Example · หน้า 44: สไลด์แสดง Arithmetic Example เพื่อทบทวนหัวข้อ ISA และคำสั่งคำนวณสามตัวถูกดำเนินการ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 44) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 44)
- Register Operands · หน้า 45: สไลด์แสดง Register Operands เพื่อทบทวนหัวข้อ RISC-V register 32 ตัวและบทบาท (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 45) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 45)
- RISC-V Registers · หน้า 46: สไลด์แสดง RISC-V Registers เพื่อทบทวนหัวข้อ RISC-V register 32 ตัวและบทบาท (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 46) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 46)
- Register Operand Example · หน้า 47: สไลด์แสดง Register Operand Example เพื่อทบทวนหัวข้อ RISC-V register 32 ตัวและบทบาท (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 47) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 47)
- Endian Support - Word Load/Store with E-bit · หน้า 48: สไลด์แสดง Endian Support - Word Load/Store with E-bit เพื่อทบทวนหัวข้อ Byte addressing, endian และ load/store (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 48) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 48)
- Memory Operands · หน้า 49: สไลด์แสดง Memory Operands เพื่อทบทวนหัวข้อ Byte addressing, endian และ load/store (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 49) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 49)
- Memory Operand Example · หน้า 50: สไลด์แสดง Memory Operand Example เพื่อทบทวนหัวข้อ Byte addressing, endian และ load/store (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 50) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 50)
- Immediate Operands · หน้า 52: สไลด์แสดง Immediate Operands เพื่อทบทวนหัวข้อ Immediate และ signed/unsigned (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 52) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 52)
- RISC-V : Numbers · หน้า 53: สไลด์แสดง RISC-V : Numbers เพื่อทบทวนหัวข้อ Immediate และ signed/unsigned (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 53) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 53)
- Representing Instructions · หน้า 54: สไลด์แสดง Representing Instructions เพื่อทบทวนหัวข้อ R/I/S instruction formats และ encoding (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 54) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 54)
- RISC-V R-format Instructions · หน้า 55: สไลด์แสดง RISC-V R-format Instructions เพื่อทบทวนหัวข้อ R/I/S instruction formats และ encoding (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 55) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 55)
- R-format Example · หน้า 56: สไลด์แสดง R-format Example เพื่อทบทวนหัวข้อ R/I/S instruction formats และ encoding (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 56) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 56)
- RISC-V I-format Instructions · หน้า 57: สไลด์แสดง RISC-V I-format Instructions เพื่อทบทวนหัวข้อ R/I/S instruction formats และ encoding (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 57) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 57)
- RISC-V S-format Instructions · หน้า 58: สไลด์แสดง RISC-V S-format Instructions เพื่อทบทวนหัวข้อ R/I/S instruction formats และ encoding (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 58) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 58)
- Logical Operations · หน้า 60: สไลด์แสดง Logical Operations เพื่อทบทวนหัวข้อ Logical operations และ bit mask (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 60) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 60)
- Shift Operations · หน้า 61: สไลด์แสดง Shift Operations เพื่อทบทวนหัวข้อ Logical operations และ bit mask (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 61) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 61)
- AND Operations · หน้า 62: สไลด์แสดง AND Operations เพื่อทบทวนหัวข้อ Logical operations และ bit mask (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 62) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 62)
- XOR Operations · หน้า 64: สไลด์แสดง XOR Operations เพื่อทบทวนหัวข้อ Logical operations และ bit mask (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 64) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 64)
- Conditional Operations · หน้า 65: สไลด์แสดง Conditional Operations เพื่อทบทวนหัวข้อ Branches, loop และ signed comparison (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 65) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 65)
- Branches, loop และ signed comparison · หน้า 66: สไลด์แสดง Branches, loop และ signed comparison เพื่อทบทวนหัวข้อ Branches, loop และ signed comparison (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 66) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 66)
- Compiling Loop Statements · หน้า 67: สไลด์แสดง Compiling Loop Statements เพื่อทบทวนหัวข้อ Branches, loop และ signed comparison (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 67) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 67)
- Basic Blocks · หน้า 68: สไลด์แสดง Basic Blocks เพื่อทบทวนหัวข้อ Branches, loop และ signed comparison (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 68) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 68)
- Signed vs Unsigned · หน้า 70: สไลด์แสดง Signed vs Unsigned เพื่อทบทวนหัวข้อ Branches, loop และ signed comparison (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 70) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 70)
- Procedure Calling · หน้า 71: สไลด์แสดง Procedure Calling เพื่อทบทวนหัวข้อ Procedure call, parameters และ return (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 71) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 71)
- Procedure Call Instructions · หน้า 72: สไลด์แสดง Procedure Call Instructions เพื่อทบทวนหัวข้อ Procedure call, parameters และ return (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 72) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 72)
- Leaf Procedure Example · หน้า 73: สไลด์แสดง Leaf Procedure Example เพื่อทบทวนหัวข้อ Leaf procedure และ stack save/restore (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 73) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 73)
- leaf_example: · หน้า 74: โค้ด leaf procedure บันทึกและคืน register; บรรทัดคำนวณ i+j ไม่ตรงกับ register ที่กำหนด: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 74) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 74)
- Local Data on the Stack · หน้า 75: สไลด์แสดง Local Data on the Stack เพื่อทบทวนหัวข้อ Leaf procedure และ stack save/restore (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 75) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 75)
- Register Usage · หน้า 76: สไลด์แสดง Register Usage เพื่อทบทวนหัวข้อ Leaf procedure และ stack save/restore (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 76) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 76)
- Non-Leaf Procedures · หน้า 77: สไลด์แสดง Non-Leaf Procedures เพื่อทบทวนหัวข้อ Non-leaf procedure และ factorial recursion (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 77) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 77)
- Non-Leaf Procedure Example · หน้า 78: C factorial แบบ non-leaf; base case เขียน return f ที่ไม่ได้กำหนด: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 78) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 78)
- fact: · หน้า 79: Assembly factorial เก็บ return address และ n บน stack; หัวข้อ Leaf ขัดกับการเรียกตัวเอง: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 79) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 79)
- Memory Layout · หน้า 80: สไลด์แสดง Memory Layout เพื่อทบทวนหัวข้อ Memory layout, activation record และข้อมูลขนาดย่อย (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 80) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 80)
- Local Data on the Stack · หน้า 81: สไลด์แสดง Local Data on the Stack เพื่อทบทวนหัวข้อ Memory layout, activation record และข้อมูลขนาดย่อย (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 81) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 81)
- Character Data · หน้า 82: สไลด์แสดง Character Data เพื่อทบทวนหัวข้อ Memory layout, activation record และข้อมูลขนาดย่อย (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 82) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 82)
- Byte/Halfword/Word Operations · หน้า 83: สไลด์แสดง Byte/Halfword/Word Operations เพื่อทบทวนหัวข้อ Memory layout, activation record และข้อมูลขนาดย่อย (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 83) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 83)
- RISC-V in details: Students can explore by themselves · หน้า 84: สไลด์แสดง RISC-V in details: Students can explore by themselves เพื่อทบทวนหัวข้อ Self-study: String copy (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 84)
- String Copy Example · หน้า 85: สไลด์แสดง String Copy Example เพื่อทบทวนหัวข้อ Self-study: String copy (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 85) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 85)
- strcpy: · หน้า 86: Assembly strcpy โหลดและเขียนทีละ byte; comment address y[i] ไม่ตรงกับ register: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 86) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 86)
- lui rd, constant · หน้า 87: ตัวอย่าง lui+addi สร้างค่าคงที่; addi 128 ไม่ตรงกับภาพ/comment 0x500: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 87) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 87)
- Branch Addressing · หน้า 88: สไลด์แสดง Branch Addressing เพื่อทบทวนหัวข้อ Self-study: Wide immediate และ branch address (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 88) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 88)
- Jump Addressing · หน้า 89: สไลด์แสดง Jump Addressing เพื่อทบทวนหัวข้อ Self-study: Wide immediate และ branch address (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 89) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 89)
- RISC-V Addressing Summary · หน้า 90: สไลด์แสดง RISC-V Addressing Summary เพื่อทบทวนหัวข้อ Self-study: Wide immediate และ branch address (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 90) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 90)
- RISC-V Encoding Summary · หน้า 91: สไลด์แสดง RISC-V Encoding Summary เพื่อทบทวนหัวข้อ Self-study: Wide immediate และ branch address (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 91) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 91)
- Synchronization · หน้า 92: สไลด์แสดง Synchronization เพื่อทบทวนหัวข้อ Self-study: Atomic operations (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 92) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 92)
- Synchronization in RISC-V · หน้า 93: สไลด์แสดง Synchronization in RISC-V เพื่อทบทวนหัวข้อ Self-study: Atomic operations (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 93) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 93)
- Synchronization in RISC-V · หน้า 94: สไลด์แสดง Synchronization in RISC-V เพื่อทบทวนหัวข้อ Self-study: Atomic operations (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 94) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 94)
- Translation and Startup · หน้า 95: สไลด์แสดง Translation and Startup เพื่อทบทวนหัวข้อ Self-study: จาก source ไป executable และ runtime (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 95) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 95)
- Producing an Object Module · หน้า 96: สไลด์แสดง Producing an Object Module เพื่อทบทวนหัวข้อ Self-study: จาก source ไป executable และ runtime (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 96) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 96)
- Linking Object Modules · หน้า 97: สไลด์แสดง Linking Object Modules เพื่อทบทวนหัวข้อ Self-study: จาก source ไป executable และ runtime (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 97) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 97)
- Loading a Program · หน้า 98: สไลด์แสดง Loading a Program เพื่อทบทวนหัวข้อ Self-study: จาก source ไป executable และ runtime (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 98) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 98)
- Lazy Linkage · หน้า 100: สไลด์แสดง Lazy Linkage เพื่อทบทวนหัวข้อ Self-study: จาก source ไป executable และ runtime (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 100) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 100)
- Starting Java Applications · หน้า 101: สไลด์แสดง Starting Java Applications เพื่อทบทวนหัวข้อ Self-study: จาก source ไป executable และ runtime (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 101) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 101)
- C Sort Example · หน้า 102: สไลด์แสดง C Sort Example เพื่อทบทวนหัวข้อ Self-study: Swap procedure (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 102) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 102)
- swap: · หน้า 103: สไลด์แสดง swap: เพื่อทบทวนหัวข้อ Self-study: Swap procedure (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 103) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 103)
- The Sort Procedure in C · หน้า 104: สไลด์แสดง The Sort Procedure in C เพื่อทบทวนหัวข้อ Self-study: Sort loops และการรักษา register (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 104) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 104)
- li   x19,0 // i = 0 · หน้า 105: สไลด์แสดง li   x19,0 // i = 0 เพื่อทบทวนหัวข้อ Self-study: Sort loops และการรักษา register (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 105) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 105)
- addi x20,x19,-1    // j = i −1 · หน้า 106: สไลด์แสดง addi x20,x19,-1    // j = i −1 เพื่อทบทวนหัวข้อ Self-study: Sort loops และการรักษา register (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 106) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 106)
- addi sp,sp,-40  // make ro om on stack for 5 regs · หน้า 107: ตัวอย่าง save/restore register ของ sort; ส่วน restore ใช้ sd แทน load: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 107) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 107)
- Effect of Compiler Optimization · หน้า 108: สไลด์แสดง Effect of Compiler Optimization เพื่อทบทวนหัวข้อ Self-study: บทเรียนจากการวัดผลและ compiler (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 108) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 108)
- Effect of Language and Algorithm · หน้า 109: สไลด์แสดง Effect of Language and Algorithm เพื่อทบทวนหัวข้อ Self-study: บทเรียนจากการวัดผลและ compiler (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 109) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 109)
- Lessons Learnt · หน้า 110: สไลด์แสดง Lessons Learnt เพื่อทบทวนหัวข้อ Self-study: บทเรียนจากการวัดผลและ compiler (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 110) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 110)
- Arrays vs. Pointers · หน้า 111: สไลด์แสดง Arrays vs. Pointers เพื่อทบทวนหัวข้อ Self-study: Array indexing เทียบ pointer (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 111) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 111)
- Example: Clearing an Array · หน้า 112: เทียบ clear array แบบ index และ pointer; C ระบุ int แต่ assembly ขยับ 8 byte: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 112) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 112)
- Comparison of Array vs. Ptr · หน้า 113: สไลด์แสดง Comparison of Array vs. Ptr เพื่อทบทวนหัวข้อ Self-study: Array indexing เทียบ pointer (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 113) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 113)
- MIPS Instructions · หน้า 114: สไลด์แสดง MIPS Instructions เพื่อทบทวนหัวข้อ Self-study: MIPS เทียบ RISC-V และ extensions (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 114) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 114)
- Instruction Encoding · หน้า 115: สไลด์แสดง Instruction Encoding เพื่อทบทวนหัวข้อ Self-study: MIPS เทียบ RISC-V และ extensions (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 115) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 115)
- Other RISC-V Instructions · หน้า 116: สไลด์แสดง Other RISC-V Instructions เพื่อทบทวนหัวข้อ Self-study: MIPS เทียบ RISC-V และ extensions (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 116) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 116)
- Instruction Set Extensions · หน้า 117: สไลด์แสดง Instruction Set Extensions เพื่อทบทวนหัวข้อ Self-study: MIPS เทียบ RISC-V และ extensions (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 117) (itds-211_comp_arch_Chapter03_RiscV.pdf, หน้า 117)
