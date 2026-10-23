# Chapter04 · Memory System Organization, Hierarchy, Cache Memory

ITDS-211 · Computer Architecture & Operating System · W. Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter04.pdf** จำนวน 112 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter04 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/วิเคราะห์/คำนวณ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 30 หัวข้อ · 🔴 ต้องจำแน่นอน 22 หัวข้อ (73.3%) · 🟡 สำคัญ 8 หัวข้อ (26.7%) · ⚪ อ่านเสริม 0 หัวข้อ (0.0%) · แบบฝึก 90 ข้อ · Flashcard 54 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter04 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| Locality และ Memory Hierarchy | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 3–8 |
| SRAM, DRAM และเทคนิคเพิ่ม bandwidth | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 9–14 |
| Flash: NOR, NAND และ wear leveling | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 15–16 |
| Disk sector และเวลาการเข้าถึง | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 17–20 |
| Cache lookup, direct mapping, tag และ valid | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 21–24 |
| ไล่สถานะ 8-block direct-mapped cache | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 25–30 |
| Tag–Index–Offset และการคำนวณ block | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 31–32 |
| ขนาด block กับการจัดการ cache miss | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 33–34 |
| Write-through, write-back และ write miss | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 35–37 |
| Split cache และ main memory ที่รองรับ cache | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 38–40 |
| Memory stall CPI และ AMAT | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 41–44 |
| Direct, n-way และ fully associative | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 45–47 |
| ตัวอย่าง access 0, 8, 0, 6, 8 | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 48–50 |
| Replacement policy: LRU และ Random | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 51–52 |
| L1/L2 และตัวอย่าง CPI หลายระดับ | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 53–56 |
| Advanced CPU, locality ของ software และ blocking | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 57–62 |
| Dependability: MTTF, MTTR, MTBF, Availability | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 63–64 |
| Hamming SEC และ SEC/DEC | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 65–68 |
| Virtual Machines, VMM และ privileged support | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 69–72 |
| Virtual Memory, address translation และ page fault | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 73–75 |
| Page table, PTE และ replacement/write-back | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 76–79 |
| TLB lookup, miss handler และ page fault handler | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 80–84 |
| TLB/Cache interaction และ Memory Protection | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 85–86 |
| กรอบร่วมของ Memory Hierarchy | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 87–91 |
| Compulsory, Capacity, Conflict miss และ trade-offs | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 92–93 |
| Cache Controller ด้วย Finite State Machine | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 94–97 |
| Cache Coherence และ invalidating snooping | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 98–101 |
| Memory Consistency และลำดับการมองเห็น writes | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter04.pdf, หน้า 102 |
| ARM/Intel cache, 2-level TLB และ system instructions | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 103–107 |
| Pitfalls และข้อสรุป Memory Hierarchy | 🟡 สำคัญ | itds-211_comp_arch_Chapter04.pdf, หน้า 108–111 |

### บทนี้เรียนเพื่ออะไร

บทนี้เรียนเพื่อเข้าใจว่าระบบให้ภาพเสมือนหน่วยความจำที่ทั้งเร็วและใหญ่ได้อย่างไร: อาศัย locality และ cache หลายระดับ พร้อมดูต้นทุนของ miss, การป้องกัน/แก้ข้อผิดพลาด, virtual memory และความสอดคล้องของ cache เมื่อมีหลาย core

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 3–8, 41–44, 63–86, 98–102, 111

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- อธิบาย locality, memory technology และการส่ง block ผ่าน memory hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 3–20)
- อ่าน cache mapping, associativity, write policy และคำนวณ hit/miss, CPI, AMAT จากตัวอย่าง (itds-211_comp_arch_Chapter04.pdf, หน้า 21–56)
- เชื่อม software locality, dependability/ECC, VM, page table และ TLB กับผลต่อประสิทธิภาพ (itds-211_comp_arch_Chapter04.pdf, หน้า 57–86)
- ใช้กรอบ placement/finding/replacement/write เพื่อวิเคราะห์ cache controller, coherence, consistency และ pitfalls (itds-211_comp_arch_Chapter04.pdf, หน้า 87–111)

รายการวัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สังเคราะห์จาก Chapter Overview หน้า 3 และหัวข้อในสไลด์

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- ตรวจครบ 112 หน้า: หน้า 1 ปก, 2 Course Outline, 3 Chapter Overview, 112 Q&A; เนื้อหาวิชาอยู่หน้า 4–111
- ไม่มีข้อสอบเก่าหรือน้ำหนักคะแนนในไฟล์ จึงจัดระดับจากหลักการ สูตร ขั้นตอน และตัวอย่างที่สไลด์ให้ ไม่อ้างว่าเป็นข้อสอบจริง
- ไม่มีรายการ Chapter Objectives ที่ประกาศเป็นข้อชัดเจน: ต้องตรวจสอบจากต้นฉบับ
- หน้า 32 ภาพ address มีเลขบิตสูงสุดที่ชวนเข้าใจเป็น 64 บิต แต่ Tag 22 + Index 6 + Offset 4 รวม 32 บิต: ต้องตรวจสอบจากต้นฉบับ
- หน้า 55 ข้อความ extra penalty = 500 cycles ไม่ตรงกับการแปลง 100 ns / 0.25 ns และสมการที่ใช้ 400 cycles: ต้องตรวจสอบจากต้นฉบับ
- ราคาหน่วยความจำและตัวอย่างระบบในสไลด์เป็นตัวอย่างตามเอกสาร ไม่ใช่ข้อมูลตลาดหรือสเปกปัจจุบัน
- ตารางและแผนภาพที่มีข้อความหนาแน่นเก็บเป็นภาพขยายในแกลเลอรี เพื่ออ่านคู่กับสรุปที่ย่อแล้ว

## 2. สรุปรายบทและหัวข้อ

### 1. Locality และ Memory Hierarchy

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 3–8**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

โปรแกรมใช้เพียงส่วนเล็กของ address space ในแต่ละช่วงเวลา จึงเกิด temporal locality และ spatial locality. ลำดับชั้นหน่วยความจำอาศัยการคัดลอกข้อมูลที่ใช้ล่าสุดหรืออยู่ใกล้กันจาก disk สู่ DRAM แล้วสู่ SRAM cache; การพบข้อมูลระดับบนคือ hit มิฉะนั้นต้องย้าย block ขึ้นมาและเกิด miss penalty.

**ประเด็นที่ต้องจำ**

- Temporal: สิ่งที่ใช้ไม่นานมักถูกใช้ซ้ำ; Spatial: สิ่งที่อยู่ใกล้กันมักถูกใช้ต่อ (หน้า 4)
- Disk → main memory/DRAM → cache/SRAM ใกล้ CPU (หน้า 5–7)
- Block/line เป็นหน่วยคัดลอก; hit ratio=hits/accesses; miss ratio=1−hit ratio (หน้า 8)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- temporal locality
- spatial locality
- block/line
- hit/miss ratio
- miss penalty

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** สไลด์ยก loop/induction variables สำหรับ temporal และ sequential instructions/array data สำหรับ spatial (หน้า 4)

**จุดที่อาจสับสน:** hit หมายถึงพบที่ระดับบน ณ การเข้าถึงครั้งนั้น; miss แล้วจึงคัดลอก block จากระดับล่าง ไม่ใช่เพิ่มข้อมูลทีละ byte เสมอ

**ประโยคช่วยจำ:** ใช้ซ้ำเร็ว = temporal; ใช้ข้างกัน = spatial; ย้ายเป็น block

### 2. SRAM, DRAM และเทคนิคเพิ่ม bandwidth

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 9–14**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

สไลด์เปรียบ SRAM, DRAM และ magnetic disk ตามเวลาเข้าถึง ความจุ และต้นทุนในบริบทตัวอย่าง. DRAM เก็บประจุใน capacitor จึงต้อง refresh; การจัดแถว row, burst, DDR/QDR และ banking ช่วยการส่งข้อมูลต่อเนื่องหรือพร้อมกัน. ภาพหน้า 14 เปรียบ memory หนึ่ง word, 4-word wide และ 4-bank interleaved ด้วยจำนวน bus cycles.

**ประเด็นที่ต้องจำ**

- ตัวเลขหน้า 9 เป็นค่าตัวอย่างในสไลด์: SRAM 0.5–2.5ns; DRAM 50–70ns; disk 5–20ms
- DRAM read/refresh เป็นระดับ row; burst ส่งคำต่อเนื่อง; DDR ส่งบนขอบขึ้นและลง (หน้า 10–13)
- ตัวอย่างหน้า 14: 4-word wide 17 cycles/0.94 B-cycle; 4-bank interleaved 20 cycles/0.8 B-cycle

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SRAM
- DRAM
- refresh
- row buffer
- burst
- DDR/QDR
- banking

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 14 คำนวณ 16/17≈0.94 B/cycle และ 16/20=0.8 B/cycle ตามสมมติฐานในภาพ

**จุดที่อาจสับสน:** ห้ามนำตัวเลขเวลา/ราคา/DRAM generations หน้า 9,12 ไปอ้างเป็นข้อมูลปัจจุบัน; เป็นตัวอย่างในเอกสาร

**ประโยคช่วยจำ:** DRAM ต้อง refresh; row/burst/bank ช่วยส่งข้อมูล

### 3. Flash: NOR, NAND และ wear leveling

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 15–16**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

Flash เป็น nonvolatile semiconductor storage ที่สไลด์เปรียบกับ disk. NOR เน้น random access และตัวอย่าง instruction memory ใน embedded system; NAND หนาแน่นกว่าและเข้าถึงเป็น block. การเขียนซ้ำทำให้เสื่อม จึงมี wear leveling กระจายการใช้งาน block.

**ประเด็นที่ต้องจำ**

- Flash ไม่หายเมื่อปิดไฟตามคำว่า nonvolatile (หน้า 15)
- NOR: random read/write; NAND: denser, block-at-a-time และใช้กับ USB/media storage (หน้า 16)
- Wear leveling remap ไปยัง block ที่ถูกใช้น้อย (หน้า 16)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- nonvolatile
- NOR flash
- NAND flash
- wear leveling

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จับคู่ NOR กับ instruction memory embedded และ NAND กับ USB/media storage ตามหน้า 16

**จุดที่อาจสับสน:** ตัวเลขความเร็ว/ราคา/อายุการเขียนหน้า 15–16 เป็นบริบทของสไลด์ ไม่ใช่สเปกปัจจุบันทุกอุปกรณ์

**ประโยคช่วยจำ:** NOR อ่านสุ่ม; NAND อ่านเป็น block; สึกแล้วกระจายเขียน

### 4. Disk sector และเวลาการเข้าถึง

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 17–20**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Disk เป็น nonvolatile rotating magnetic storage; sector มีรหัสระบุ ข้อมูล ECC และส่วนช่วยซิงโครไนซ์. เวลาการเข้าถึงหนึ่ง sector รวม queue, seek, rotational latency, transfer และ controller overhead. ตัวอย่าง 15,000 rpm/512B ให้เวลาอ่านเฉลี่ยประมาณ 6.2ms โดยเวลา seek เป็นส่วนสำคัญ.

**ประเด็นที่ต้องจำ**

- องค์ประกอบการเข้าถึง: queue, seek, rotation, transfer, controller (หน้า 18)
- ตัวอย่างหน้า 19: 4ms seek +2ms rotation +0.005ms transfer +0.2ms controller ≈6.2ms
- ถ้า actual average seek 1ms สไลด์ให้ average read 3.2ms (หน้า 19)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- sector
- seek
- rotational latency
- transfer time
- controller overhead
- disk cache

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ½ revolution /(15000/60 revolutions/s)=2ms rotational latency ตามหน้า 19

**จุดที่อาจสับสน:** ค่า 6.2ms เป็นการปัดจาก 6.205ms และสมมติ disk idle; หน้า 20 ระบุ locality/OS scheduling ทำให้ seek จริงต่างจากค่าเฉลี่ยผู้ผลิต

**ประโยคช่วยจำ:** รอคิว–หา track–รอหมุน–ส่งข้อมูล–คุมอุปกรณ์

### 5. Cache lookup, direct mapping, tag และ valid

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 21–24**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Cache เป็นระดับใน memory hierarchy ที่ใกล้ CPU; ต้องตอบว่าข้อมูลอยู่ใน cache หรือไม่และควรหา entry ไหน. Direct-mapped cache ให้แต่ละ memory block มีตำแหน่งเดียว โดย index = block address mod จำนวน cache blocks. Tag แยก block ที่ชน index และ valid bit ระบุว่าช่องนั้นมีข้อมูลจริงหรือไม่.

**ประเด็นที่ต้องจำ**

- Direct mapped: index = block address modulo #cache blocks (หน้า 23)
- ถ้า #blocks เป็นกำลังสอง ใช้บิตล่างเป็น index; tag เป็นบิตสูงของ block address (หน้า 23–24)
- valid=1 แปลมีข้อมูล, 0 แปลไม่มี; ค่าเริ่มต้น 0 (หน้า 24)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- direct mapped
- index
- tag
- valid bit

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** cache 8 blocks ใช้ 3 index bits; หน้า 25 แสดงทุก entry เริ่ม valid=N

**จุดที่อาจสับสน:** index ตรงกันยังไม่พอเป็น hit ต้อง valid และ tag ตรงกัน

**ประโยคช่วยจำ:** Index ชี้ช่อง; Tag เช็กตัวตน; Valid เช็กว่ามี

### 6. ไล่สถานะ 8-block direct-mapped cache

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 25–30**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

ตัวอย่าง cache 8 blocks, 1 word/block เริ่มทุก valid bit เป็น N แล้วเข้าถึง word addresses หลายตัว. Word 22 ลง index 110/tag 10 และ word 26 ลง index 010/tag 11; การเข้าซ้ำเป็น hit จน word 18 มาใช้ index 010 เดียวกับ 26 และแทนที่ด้วย tag 10.

**ประเด็นที่ต้องจำ**

- 22→binary 10 110→index110 miss ครั้งแรก; 26→11 010→index010 miss (หน้า 26–27)
- 22 และ 26 เข้าซ้ำเป็น hit ตามสถานะหลังโหลด (หน้า 28)
- 16→index000 miss; 3→index011 miss; 16 เข้าซ้ำ hit; 18→index010 miss/แทน 26 (หน้า 29–30)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- cache trace
- hit/miss
- tag/index collision

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามตารางหน้า 25–30 ทีละ access แล้วปรับ valid/tag/data เฉพาะช่องที่ miss

**จุดที่อาจสับสน:** หน้า 29 มีลำดับตัวอย่างย่อย 16,3,16; อย่าสับสนกับ access 22/26 ในหน้าก่อนและอย่าอ่านสีตารางแทนลำดับเวลา

**ประโยคช่วยจำ:** แปลง address → index/tag → เทียบ → อัปเดตเฉพาะ miss

### 7. Tag–Index–Offset และการคำนวณ block

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 31–32**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

ที่อยู่ byte แบ่งเป็น tag, index และ offset เพื่อหา cache entry และตำแหน่งภายใน block. ตัวอย่าง 64 blocks ขนาด 16 bytes/block ให้ block address=floor(1200/16)=75 แล้ว cache block=75 mod64=11; offset 4 บิตและ index 6 บิต.

**ประเด็นที่ต้องจำ**

- block address=floor(byte address/bytes per block) (หน้า 32)
- cache block number=block address mod #blocks (หน้า 32)
- 64 blocks→6 index bits; 16 bytes/block→4 offset bits (หน้า 32)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- tag
- index
- byte offset
- block address
- modulo

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** 1200/16=75 และ 75 mod64=11 ตามตัวอย่างหน้า 32

**จุดที่อาจสับสน:** รูปหน้า 32 เขียนช่วง bit address ถึง 63 แต่ระบุ tag 22+index6+offset4=32 บิต ขัดกัน: ต้องตรวจสอบจากต้นฉบับ; อย่าเดาความกว้าง address จากรูปนี้

**ประโยคช่วยจำ:** หารขนาด block ก่อน; mod จำนวนช่องต่อ

### 8. ขนาด block กับการจัดการ cache miss

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 33–34**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

block ใหญ่ใช้ spatial locality เพื่อลด miss บางส่วน แต่ cache ขนาดคงที่มีจำนวน block น้อยลง จึงเพิ่ม competition/pollution และ miss penalty. เมื่อ cache miss CPU อาจ stall แล้วดึง block จากระดับล่าง; instruction miss กลับไป fetch ส่วน data miss ทำ data access ต่อ.

**ประเด็นที่ต้องจำ**

- larger block อาจลด miss จาก spatial locality แต่เพิ่ม miss penalty (หน้า 33)
- cache ขนาดคงที่: block ใหญ่→จำนวน entry น้อย→competition/pollution (หน้า 33)
- on miss: stall pipeline, fetch block; instruction/data miss กลับขั้นต่างกัน (หน้า 34)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- block size
- pollution
- miss penalty
- early restart
- critical-word-first

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** หน้า 33 ระบุ early restart/critical-word-first ว่าช่วยลดผลของ miss penalty

**จุดที่อาจสับสน:** อย่าจำว่า block ใหญ่ยิ่งดีเสมอ; มีทั้งประโยชน์จาก locality และค่าเสียโอกาสของ entry

**ประโยคช่วยจำ:** Block ใหญ่ช่วยใกล้เคียง แต่กินช่องและโหลดนาน

### 9. Write-through, write-back และ write miss

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 35–37**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Write-through เขียนทั้ง cache และ memory ทุก write hit จึงอาจใช้ write buffer ลดการรอ. Write-back เขียน cache ก่อน ติด dirty bit แล้วค่อยเขียน block กลับเมื่อถูกแทนที่. เมื่อ write miss สไลด์เทียบ write allocate (fetch block) กับ write-around (ไม่ fetch) และระบุ write-back มัก fetch block.

**ประเด็นที่ต้องจำ**

- Write-through อัปเดต cache+memory; ตัวอย่าง base CPI1, stores10%, write100 cycles→CPI11 (หน้า 35)
- Write buffer ให้ CPU เดินต่อได้จน buffer เต็ม (หน้า 35)
- Write-back ใช้ dirty bit; write miss แบบ allocate ดึง block, write-around ไม่ดึง (หน้า 36–37)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- write-through
- write-back
- dirty bit
- write buffer
- write allocate
- write-around

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เปรียบหน้า 35–36: เขียน memory ทุกครั้งกับเขียนเมื่อแทน dirty block

| เรื่อง | Write-through | Write-back |
| --- | --- | --- |
| เขียนเมื่อ hit | cache และ memory | cache ก่อน |
| การเขียนระดับล่าง | ทุก write hit | เมื่อ dirty block ถูกแทน |
| สิ่งช่วย/สถานะ | write buffer | dirty bit |

**จุดที่อาจสับสน:** Write policy สำหรับ hit กับ write allocation สำหรับ miss เป็นคนละการตัดสินใจ

**ประโยคช่วยจำ:** Through เขียนล่างทันที; Back เขียนล่างตอนแทน; Miss เลือกดึงหรือข้าม

### 10. Split cache และ main memory ที่รองรับ cache

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 38–40**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

กรณี Intrinsity FastMATH ในสไลด์ใช้ split I-cache/D-cache และแสดง miss rate ต่างกัน; เป็นตัวอย่างสถาปัตยกรรมเฉพาะ. หน้า 40 แสดงว่าความกว้าง memory/bus ส่งผลต่อ miss penalty และ bandwidth โดยตัวอย่าง 4-word block ผ่าน memory กว้างหนึ่ง word ใช้ 65 bus cycles.

**ประเด็นที่ต้องจำ**

- ตัวอย่าง FastMATH: I-cache/D-cache อย่างละ 16KB, 256 blocks×16 words/block; miss rate 0.4%/11.4% (หน้า 38)
- หน้า 40: address1 + DRAM 4×15 + transfer4×1 =65 bus cycles
- bandwidth=16 bytes/65 cycles≈0.25 B/cycle (หน้า 40)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- split cache
- I-cache/D-cache
- bus width
- miss penalty
- bandwidth

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ภาพหน้า 39 ดู tag/index/offset ของ split cache และคำนวณหน้า 40

**จุดที่อาจสับสน:** ตัวเลข miss rate และขนาด cache หน้า 38 เป็นของเครื่องตัวอย่าง ไม่ใช่ค่า RISC-V ทั่วไป

**ประโยคช่วยจำ:** กว้างบัส/หน่วยความจำกำหนดเวลาขนหนึ่ง block

### 11. Memory stall CPI และ AMAT

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 41–44**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

สไลด์แยก CPU cycles สำหรับการรันโปรแกรมออกจาก memory stall cycles ที่มักเกิดจาก cache miss. ภายใต้สมมติฐานที่ระบุ miss cycles คำนวณจากจำนวน access หรือ miss ต่อ instruction คูณ miss penalty; AMAT รวม hit time กับ miss rate×miss penalty. ตัวอย่างแสดง actual CPI 5.44 และ AMAT 2ns.

**ประเด็นที่ต้องจำ**

- memory stall cycles≈memory accesses/program×miss rate×miss penalty (หน้า 41)
- I-cache:0.02×100=2; D-cache:0.36×0.04×100=1.44; actual CPI=2+2+1.44=5.44 (หน้า 42)
- AMAT=hit time+miss rate×miss penalty; ตัวอย่าง 1+0.05×20=2ns (หน้า 43)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- CPI
- memory stall cycles
- AMAT
- hit time
- miss rate
- miss penalty

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตัวอย่างหน้า 42 ideal CPI 2 เทียบ actual 5.44 ให้สัดส่วน 5.44/2=2.72 ตามสไลด์

**จุดที่อาจสับสน:** miss rate ของ I-cache ต่อ instruction ต่างจาก D-cache ที่ต้องคูณสัดส่วน load/store 0.36; หน้า 44 ย้ำดู cache behavior เมื่อประเมิน performance

**ประโยคช่วยจำ:** CPI ฐานบวก stall; AMAT hit บวกโอกาส miss คูณ penalty

### 12. Direct, n-way และ fully associative

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 45–47**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Fully associative วาง block ใน entry ใดก็ได้แต่ต้องเทียบทุก entry; n-way set associative กำหนด set จาก block number mod จำนวน sets แล้วค้นหา n entries ใน set. ภาพหน้า 46–47 แสดงสองแบบนี้เทียบกับ direct mapped ซึ่งมีเพียงตำแหน่งเดียว.

**ประเด็นที่ต้องจำ**

- Fully associative: วางได้ทุก entry ต้องค้นพร้อมกันทุก entry (หน้า 45)
- n-way: set=block number mod #sets; ค้น n entries ใน set (หน้า 45)
- direct mapped เป็น 1-way; spectrum หน้า 47 ใช้ cache 8 entries

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- fully associative
- n-way set associative
- set index
- comparator

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านภาพหน้า 46 โดยตาม block เดียวไปได้หนึ่งช่อง/หนึ่ง set/ทุกช่องตามสามรูปแบบ

| Mapping | ที่วาง block | จำนวนเปรียบเทียบตามหน้า 89 |
| --- | --- | --- |
| Direct mapped | หนึ่ง entry | 1 |
| n-way | หนึ่งใน n entries ของ set | n |
| Fully associative | ทุก entry | จำนวน entries |

**จุดที่อาจสับสน:** associativity เพิ่มทางเลือกตำแหน่งแต่เพิ่ม comparator/ความซับซ้อน ไม่ใช่เพิ่มจำนวน entries ของ cache ในตัวอย่างเทียบ

**ประโยคช่วยจำ:** หนึ่งช่อง–หลายช่องใน set–ทุกช่อง

### 13. ตัวอย่าง access 0, 8, 0, 6, 8

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 48–50**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

สไลด์เทียบ cache ขนาด 4 blocks ที่รับลำดับ 0,8,0,6,8. Direct mapped ชน index จน miss ทุกครั้ง; 2-way set associative ได้ hit ที่ 0 ครั้งที่สอง; fully associative ได้ hit ที่ 0 และ 8 ที่กลับมา. ข้อมูล simulation หน้า 50 แสดง miss rate ลดลงเมื่อ associativity สูงขึ้นแต่ผลเพิ่มเริ่มน้อยลง.

**ประเด็นที่ต้องจำ**

- Direct mapped: 5 misses ใน 5 accesses (หน้า 48)
- 2-way: miss,miss,hit,miss,miss; fully: miss,miss,hit,miss,hit (หน้า 49)
- SPEC2000 example หน้า 50: 1/2/4/8-way miss 10.3/8.6/8.3/8.1%

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- conflict miss
- set
- associativity
- diminishing returns

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ตารางหน้า 48–49 ทีละ access; 0 กับ 8 ใช้ index 0 ใน direct mapped

**จุดที่อาจสับสน:** ตัวเลขหน้า 50 เป็นผล simulation กรณี 64KB D-cache ไม่ใช่กฎว่าทุก cache มี miss rate ตามนี้

**ประโยคช่วยจำ:** เพิ่มทางเลือกที่วาง ลดการชน แต่ผลเพิ่มลดลง

### 14. Replacement policy: LRU และ Random

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 51–52**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

เมื่อ miss แล้วต้องแทน entry, direct mapped ไม่มีตัวเลือก ส่วน set associative ควรใช้ entry invalid ก่อน. หากเต็มแล้วจึงเลือกตามนโยบาย เช่น LRU เลือก entry ที่ไม่ถูกใช้นานที่สุด หรือ random. สไลด์ระบุ LRU ซับซ้อนขึ้นเมื่อ associativity สูง.

**ประเด็นที่ต้องจำ**

- direct mapped ไม่มี choice ในการแทน (หน้า 52)
- set associative ใช้ non-valid entry ก่อน; เต็มแล้วจึงเลือกใน set (หน้า 52)
- LRU เลือก entry ไม่ใช้ยาวนานสุด; random ใกล้ LRU ใน high associativity ตามสไลด์ (หน้า 52)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- replacement policy
- LRU
- random
- valid entry

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูภาพการจัด set หน้า 51 แล้วถามว่าถ้ามีช่อง invalid จะต้องแทนของเดิมหรือไม่

**จุดที่อาจสับสน:** LRU หมายถึงเวลาตั้งแต่ใช้งานครั้งล่าสุด ไม่ใช่ข้อมูลที่เก่าที่สุดตามเวลานำเข้าครั้งแรก

**ประโยคช่วยจำ:** ว่างก่อน; เต็มแล้วค่อยเลือก LRU หรือสุ่ม

### 15. L1/L2 และตัวอย่าง CPI หลายระดับ

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 53–56**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

L1 อยู่ใกล้ CPU จึงเน้น hit time ต่ำ ส่วน L2 ใหญ่กว่าและรับ miss จาก L1 เพื่อลดการไป main memory. ตัวอย่าง 4GHz/base CPI1 มี L1 อย่างเดียว CPI9; เมื่อมี L2 สไลด์คำนวณ CPI3.4 และ performance ratio 9/3.4≈2.6. หน้าตัวอย่างมีคำบรรยาย penalty หนึ่งจุดไม่ตรงกับสมการ จึงต้องอ่านคู่กัน.

**ประเด็นที่ต้องจำ**

- L1 เล็ก/เร็ว; L2 ใหญ่/ช้ากว่า L1 แต่เร็วกว่า main memory (หน้า 53,56)
- 4GHz→cycle 0.25ns; 100ns main memory→400 cycles; L1 only CPI=1+0.02×400=9 (หน้า 54)
- L2 access 5ns→20 cycles; global miss 0.5%; สมการหน้า 55 ให้ CPI=1+0.02×20+0.005×400=3.4

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- L1/L2 cache
- global miss rate
- miss penalty
- effective CPI

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ฝึกคำนวณแยก penalty ที่ L2 กับ main memory จากตัวอย่างหน้า 54–55

**จุดที่อาจสับสน:** หน้า 55 เขียน “Extra penalty = 500 cycles” แต่สมการใช้ 400 cycles และ 100ns/0.25ns ในหน้า 54 เท่ากับ 400: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** L1 เน้น hit เร็ว; L2 กัน miss ลง DRAM

### 16. Advanced CPU, locality ของ software และ blocking

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 57–62**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

out-of-order CPU อาจทำงานอิสระต่อได้ขณะ cache miss จึงวิเคราะห์เวลาได้ยากและสไลด์เสนอ simulation. รูปแบบการเข้าถึง memory ขึ้นกับ algorithm/compiler; ตัวอย่าง DGEMM ใช้ blocking เพื่อใช้ข้อมูลซ้ำก่อนถูกแทนใน cache และภาพหน้า 60–62 เปรียบ access pattern.

**ประเด็นที่ต้องจำ**

- out-of-order: dependent instructions รอ, independent instructions อาจเดินต่อ (หน้า 57)
- miss rate ขึ้นกับ memory access pattern/algorithm/compiler (หน้า 58)
- blocking เป้าหมายคือใช้ข้อมูลให้มากก่อนถูกแทน; ตัวอย่างใช้ BLOCKSIZE=32 (หน้า 59–62)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- out-of-order
- memory access pattern
- DGEMM
- blocking
- BLOCKSIZE

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามภาพ C/A/B หน้า 60 กับ blocked access pattern หน้า 62 เพื่อเห็นการใช้ข้อมูลซ้ำในบริเวณย่อย

**จุดที่อาจสับสน:** อย่าอ้างว่า cache miss ทุกครั้ง stall CPU เต็ม penalty เมื่อเป็น out-of-order; หน้า 57 ระบุ independent work ยังทำได้

**ประโยคช่วยจำ:** จัดงานเป็น block ใช้ข้อมูลซ้ำก่อนหลุด cache

### 17. Dependability: MTTF, MTTR, MTBF, Availability

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 63–64**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

สไลด์แยก fault ของ component ออกจาก failure ของ service; fault อาจนำหรือไม่ไปสู่ system failure. ความเชื่อถือได้วัดด้วย MTTF และเวลาซ่อมด้วย MTTR; MTBF=MTTF+MTTR และ availability=MTTF/(MTTF+MTTR). เพิ่ม availability ได้โดยเพิ่ม MTTF หรือ ลด MTTR.

**ประเด็นที่ต้องจำ**

- fault เป็น failure ของ component แต่อาจไม่ทำให้บริการล้ม (หน้า 63)
- MTBF=MTTF+MTTR; Availability=MTTF/(MTTF+MTTR) (หน้า 64)
- เพิ่ม MTTF ผ่าน avoidance/tolerance/forecasting; ลด MTTR ด้วย diagnosis/repair ที่ดีขึ้น (หน้า 64)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- fault
- failure
- restoration
- MTTF
- MTTR
- MTBF
- availability

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ภาพหน้า 63 จาก service delivered → interruption → restoration กลับ service

**จุดที่อาจสับสน:** MTBF รวมเวลาทำงานก่อนเสียกับเวลาซ่อม; อย่าใช้แทน MTTF ในสูตร availability โดยไม่แปลง

**ประโยคช่วยจำ:** เวลาทำงานเทียบงานบวกเวลาซ่อม คือ availability

### 18. Hamming SEC และ SEC/DEC

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 65–68**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Hamming distance คือจำนวนตำแหน่งบิตที่ต่างกัน; minimum distance 2 ตรวจข้อผิดพลาดหนึ่งบิต และ 3 แก้หนึ่งบิตพร้อมตรวจสองบิตตามสไลด์. การเข้ารหัส SEC วาง parity bits ที่ตำแหน่งกำลังสองเมื่อเลขตำแหน่งเริ่ม 1 จากซ้าย. เพิ่ม parity ทั้ง word ให้ SEC/DEC มี distance 4 และใช้ parity syndrome ช่วยแยกกรณี error.

**ประเด็นที่ต้องจำ**

- Hamming distance 2 ตรวจ 1-bit; distance 3 แก้ 1-bit/ตรวจ 2-bit (หน้า 65)
- SEC parity positions 1,2,4,8; ตารางหน้า 66 บอก data bits ที่แต่ละตัวตรวจ
- syndrome 0000→no error; 1010→bit 10 flipped (หน้า 67)
- เพิ่ม whole-word parity p_n เป็น SEC/DEC distance4; สไลด์ยก ECC DRAM 8 bits ต่อ 64 bits (หน้า 68)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Hamming distance
- SEC
- SEC/DEC
- parity bit
- syndrome
- ECC DRAM

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูตารางหน้า 66 แล้วอ่าน syndrome 1010 ว่าเลขตำแหน่ง 10 ตามตัวอย่างหน้า 67

**จุดที่อาจสับสน:** หน้า 68 ใช้ถ้อยคำ H even/odd ร่วมกับ p_n even/odd; ต้องตรวจสอบจากต้นฉบับหากจะนำไปคำนวณชุด parity โดยละเอียด เพราะสไลด์ไม่ได้ให้ตัวอย่างข้อมูลครบ

**ประโยคช่วยจำ:** พาริตีอยู่ 1,2,4,8; syndrome ชี้ตำแหน่ง; เพิ่ม parity ทั้ง word ตรวจสองบิต

### 19. Virtual Machines, VMM และ privileged support

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 69–72**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Virtual machine ให้ host จำลอง guest OS และทรัพยากรเพื่อแยกผู้ใช้หลายกลุ่มและแชร์เครื่อง. VMM map virtual resources ไป physical resources; guest code ทำงาน user mode และ trap ไป VMM เมื่อใช้ privileged instruction หรือ protected resource. ตัวอย่าง timer virtualization แสดง VMM รับ interrupt จริงและจำลองให้ VM.

**ประเด็นที่ต้องจำ**

- VM ช่วย isolation และ resource sharing แต่มี performance impact (หน้า 69)
- VMM map memory/I-O/CPU; privileged access trap ไป VMM (หน้า 70)
- หน้า 71 เปรียบ OS จัด process กับ VMM จัด VM บน timer interrupt
- หน้า 72 system/user modes และ privileged instructions คุ้มครอง physical resources

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- VM
- host/guest
- VMM
- trap
- privileged instruction
- timer virtualization

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านหน้า 71 เปรียบเส้นทาง timer ของ native machine กับ VMM

**จุดที่อาจสับสน:** guest OS ไม่ได้เข้าถึงอุปกรณ์จริงได้อิสระ; VMM จัดการ real I/O และ emulates virtual I/O ตามหน้า 70

**ประโยคช่วยจำ:** Guest เห็นเครื่องเสมือน; VMM จับสิทธิ์และ map ของจริง

### 20. Virtual Memory, address translation และ page fault

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 73–75**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Virtual memory ใช้ main memory เป็น cache ของ disk โดย CPU hardware กับ OS ร่วมกันจัดการ. โปรแกรมมี virtual address space ของตน และ address translation แปลง virtual page number เป็น physical page number โดย page offset คงเดิม. ถ้า page ไม่อยู่ใน memory เกิด page fault ซึ่งมี penalty สูงและ OS ต้องนำ page จาก disk.

**ประเด็นที่ต้องจำ**

- VM block เรียก page; translation miss เรียก page fault (หน้า 73)
- ตัวอย่าง fixed-size 4K page มี offset 12 bits ตามภาพหน้า 74
- page fault ดึง page จาก disk ใช้หลายล้าน cycles; OS handle (หน้า 75)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- virtual address
- physical address
- page
- page offset
- page fault

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามลูกศรภาพหน้า 74: แปล page number แต่ส่ง offset เดิมไปต่อ physical address

**จุดที่อาจสับสน:** page fault เป็น page ไม่อยู่ main memory; ไม่ใช่ TLB miss ทุกครั้ง (แยกในหน้า 82–84)

**ประโยคช่วยจำ:** เปลี่ยนเลข page; offset คง; ไม่พบจึงไป disk

### 21. Page table, PTE และ replacement/write-back

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 76–79**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Page table มี PTE ตาม virtual page number; ถ้า present จะให้ physical page number กับ status bits หากไม่อยู่ memory อาจชี้ swap space. Reference/use bit ช่วยประมาณ LRU และ dirty bit ระบุ page ที่ถูกเขียน. Disk write ช้ามากจึงใช้ write-back เมื่อจำเป็นต้องแทน page.

**ประเด็นที่ต้องจำ**

- Page table register ชี้ page table ใน physical memory; PTE indexed by virtual page number (หน้า 76)
- PTE เก็บ physical page number/status หรือที่อยู่ swap space (หน้า 76–78)
- reference bit set เมื่อ access และ OS ล้างเป็นระยะ; dirty bit set เมื่อเขียน page (หน้า 79)
- page ที่ dirty ต้องเขียน disk เมื่อถูกแทน; write-through ไม่เหมาะกับ disk (หน้า 79)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- PTE
- page table register
- swap space
- reference bit
- dirty bit
- write-back

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 77–78 ชี้ว่า page ใน virtual space บางหน้า map ไป physical memory และบางหน้าไป disk

**จุดที่อาจสับสน:** valid/present bit กับ dirty/reference มีหน้าที่ต่างกัน; reference=0 เพียงบอกว่าไม่น่าใช้ล่าสุดตามการล้างรอบก่อน

**ประโยคช่วยจำ:** PTE บอกที่; reference บอกใช้; dirty บอกต้องเขียนกลับ

### 22. TLB lookup, miss handler และ page fault handler

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 80–84**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

TLB เป็น cache ของ PTE ใน CPU เพื่อไม่ต้องเข้าถึง page table ใน memory ทุกครั้ง. TLB miss อาจเกิดทั้งเมื่อ page อยู่ memory หรือไม่อยู่; กรณีแรกเติม PTE แล้ว retry ส่วนกรณีหลังเป็น page fault ให้ OS นำ page จาก disk อัปเดต page table และ restart instruction. ภาพหน้า 81 แสดง TLB, page table, physical memory และ disk ร่วมกัน.

**ประเด็นที่ต้องจำ**

- TLB=Translation Look-aside Buffer; cache PTE ใน CPU (หน้า 80)
- page present แต่ไม่ใน TLB→โหลด PTE จาก memory/retry (หน้า 82–83)
- page absent→OS locate disk, choose replacement, write dirty page, read page, update table, restart (หน้า 82–84)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- TLB
- PTE
- TLB hit/miss
- page fault handler
- restart instruction

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านแผนภาพหน้า 81 แล้วตามสองทาง: TLB miss แต่ PTE valid กับ PTE invalid/page fault

**จุดที่อาจสับสน:** TLB miss ไม่เท่ากับ page fault เสมอ; คำว่า “page not preset” หน้า 83 ดูเป็น typo ของ present แต่ใช้บริบทหน้า 82 ประกอบ

**ประโยคช่วยจำ:** TLB ไม่มีรายการ ≠ page ไม่มีใน RAM; ตรวจ PTE ก่อน

### 23. TLB/Cache interaction และ Memory Protection

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 85–86**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

ถ้า cache ใช้ physical address เป็น tag ต้องแปล virtual address ก่อน lookup; การใช้ virtual tag มีปัญหา aliasing เมื่อหลาย virtual address ชี้ physical address เดียวกัน. Hardware กับ OS ยังต้องป้องกัน address space ผ่าน supervisor mode, privileged instructions และ page tables ที่เข้าถึงได้เฉพาะสิทธิ์สูง.

**ประเด็นที่ต้องจำ**

- physical tag→translate ก่อน cache lookup (หน้า 85)
- virtual tag มี aliasing เมื่อ virtual addresses ต่างกันแชร์ physical address (หน้า 85)
- supervisor/kernel mode และ privileged instructions ป้องกัน page table/resource; ecall เป็นตัวอย่าง system call (หน้า 86)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- physical/virtual tag
- aliasing
- supervisor mode
- privileged instruction
- ecall

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 85 เทียบลำดับ TLB→cache กับทางเลือก virtual-address tag

**จุดที่อาจสับสน:** อย่าสับสน address translation เพื่อหาตำแหน่งจริงกับ memory protection เพื่อจำกัดสิทธิ์เข้าถึง

**ประโยคช่วยจำ:** แปลก่อนหาเมื่อ tag จริง; kernel คุมสิทธิ์

### 24. กรอบร่วมของ Memory Hierarchy

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 87–91**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

ทุกระดับของ memory hierarchy มีคำถามร่วมกันสี่เรื่อง: วาง block ที่ไหน, หา block อย่างไร, miss แล้วแทนตัวใด และเขียนข้อมูลลงระดับล่างเมื่อใด. ระดับ associativity กำหนดทางเลือกในการวางและจำนวน tag comparison; write-through กับ write-back มีต้นทุนและสถานะที่ต้องเก็บต่างกัน.

**ประเด็นที่ต้องจำ**

- Placement: direct 1 ที่, n-way n ที่ใน set, fully ที่ใดก็ได้ (หน้า 88)
- Finding: direct เปรียบเทียบ tag 1, n-way n, fully ตามจำนวน entries; full lookup table เป็นอีกวิธี (หน้า 89)
- Replacement: LRU หรือ random; virtual memory ใช้ LRU approximation (หน้า 90)
- Write-through อัปเดตบน/ล่าง; write-back อัปเดตล่างเมื่อถูกแทน; virtual memory ใช้ write-back เพราะ disk latency (หน้า 91)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- block placement
- tag comparison
- replacement
- LRU
- write-through
- write-back

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตารางหน้า 89 แสดง index → 1 comparison; set index → n comparisons; search all entries → #entries comparisons

| แบบ | ตำแหน่งวาง | การเปรียบเทียบ tag |
| --- | --- | --- |
| Direct mapped | 1 | 1 |
| n-way set associative | n ภายใน set | n |
| Fully associative | ที่ใดก็ได้ | #entries |

**จุดที่อาจสับสน:** associativity สูงลด miss แต่เพิ่มความซับซ้อน ต้นทุน และ access time; ไม่ได้ดีขึ้นทุกมิติ

**ประโยคช่วยจำ:** วาง–หา–แทน–เขียน

### 25. Compulsory, Capacity, Conflict miss และ trade-offs

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 92–93**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Compulsory miss เกิดเมื่อเข้าถึง block ครั้งแรก; capacity miss เกิดเพราะ cache จำกัดจน block เดิมถูกแทนและต้องใช้ซ้ำ; conflict miss เกิดจากหลาย block แย่งตำแหน่งใน set ของ cache ที่ไม่ fully associative. การเพิ่มขนาด cache, associativity และ block size ลด miss ต่างชนิดกัน แต่มีต้นทุนเรื่อง access time, miss penalty หรือ pollution.

**ประเด็นที่ต้องจำ**

- Compulsory = first access (หน้า 92)
- Capacity = finite size ทำให้ block ที่ถูกแทนถูกเรียกอีก (หน้า 92)
- Conflict = แข่ง entry ใน set; ไม่เกิดใน fully associative ขนาดรวมเท่ากัน (หน้า 92)
- เพิ่ม cache size ลด capacity; เพิ่ม associativity ลด conflict; เพิ่ม block size ลด compulsory แต่ใหญ่มากอาจเพิ่ม miss/pollution (หน้า 93)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- compulsory/cold start
- capacity
- conflict/collision
- pollution
- miss penalty

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตารางหน้า 93 จับคู่ design change กับชนิด miss ที่ลดและผลเสียด้านเวลา

| Miss | สาเหตุ | แนวลดตามสไลด์ |
| --- | --- | --- |
| Compulsory | เรียก block ครั้งแรก | เพิ่ม block size |
| Capacity | cache รวมไม่พอ | เพิ่ม cache size |
| Conflict | block ชนกันใน set | เพิ่ม associativity |

**จุดที่อาจสับสน:** อย่าจับคู่เพิ่ม associativity กับ capacity miss; ผลโดยตรงในตารางคือ conflict miss

**ประโยคช่วยจำ:** ครั้งแรก–ที่ไม่พอ–ที่ชนกัน

### 26. Cache Controller ด้วย Finite State Machine

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 94–97**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

ตัวอย่าง cache เป็น direct-mapped, write-back, write allocate, blocking cache ขนาด 16 KB มี 1024 blocks ขนาด block 16 bytes และ address 32 บิต. Controller ใช้ FSM คุมขั้นตอนตาม clock โดยเก็บ current state ใน register, หา next state จาก current state กับ input และสร้าง control output จาก current state. ภาพ FSM แสดงทางเดิน hit, miss, dirty write-back และ memory read.

**ประเด็นที่ต้องจำ**

- ตัวอย่าง: 32-bit byte address; tag 18, index 10, offset 4 (หน้า 94)
- valid/dirty bit ต่อ block; CPU รอ access ให้เสร็จใน blocking cache (หน้า 94)
- interface CPU–cache–memory มี read/write, valid, address, data, ready และการเข้าถึง memory หลาย cycles (หน้า 95)
- next state = fn(current state,current inputs); outputs = fo(current state) (หน้า 96)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- FSM
- current state
- next state
- valid bit
- dirty bit
- blocking cache

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** 16 KB/16 B = 1024 blocks จึงใช้ index 10 บิต; offset 4 บิต; tag 32−10−4=18 บิต (หน้า 94)

**จุดที่อาจสับสน:** write-back miss ที่ victim dirty ต้องเขียน block เดิมกลับก่อนโหลด block ใหม่; อ่านรายละเอียดลูกศรหน้า 97

**ประโยคช่วยจำ:** สถานะปัจจุบัน + input → สถานะถัดไป

### 27. Cache Coherence และ invalidating snooping

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 98–101**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

เมื่อหลาย core แชร์ physical address แต่เก็บสำเนาไว้ใน cache ของตน การเขียนของ core หนึ่งอาจทำให้สำเนาอีก core เก่า. Coherence ต้องให้การอ่านเห็นค่าที่เขียนล่าสุดตามเงื่อนไขในสไลด์ และทุก processor เห็นลำดับการเขียนไปยัง X เหมือนกัน. Snooping เฝ้าดู bus ส่วน directory-based เก็บสถานะผู้แชร์; invalidating snooping ส่ง invalidate เมื่อขอสิทธิ์เขียนแบบ exclusive.

**ประเด็นที่ต้องจำ**

- ตัวอย่าง CPU A/B อ่าน X=0 แล้ว A เขียน 1: cache B อาจยังมี 0 (หน้า 98)
- coherence ครอบคลุม read-after-own-write, read-after-other-write เมื่อเวลาพอ และลำดับ write ต่อ X เหมือนกัน (หน้า 99)
- snooping monitor bus; directory บันทึก sharing status (หน้า 100)
- invalidate → read ของ cache อื่น miss แล้ว owner ส่งค่าล่าสุด (หน้า 101)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- cache coherence
- snooping
- directory-based
- invalidate
- exclusive access

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ตารางหน้า 101: A/B อ่าน X=0, A เขียน X=1 และ invalidate, B อ่านซ้ำแล้ว miss ก่อนรับค่าใหม่

**จุดที่อาจสับสน:** write-through ให้ memory ใหม่ได้ แต่ไม่ได้ทำให้สำเนาใน cache อื่นใหม่เอง; ต้องมี coherence protocol

**ประโยคช่วยจำ:** เขียนร่วม → แจ้งลบสำเนาเก่า

### 28. Memory Consistency และลำดับการมองเห็น writes

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter04.pdf, **หน้า 102**

เหตุผลการจัดระดับ: เป็นนิยาม หลักการ สูตร ขั้นตอน หรือกลไกหลักที่ใช้ต่อยอดในบท

Memory consistency ถามว่า write ของ processor หนึ่งจะถูก processor อื่นมองเห็นเมื่อใด โดย “เห็น” หมายถึง read คืนค่าที่เขียน. ภายใต้สมมติฐานของสไลด์ write เสร็จเมื่อทุก processor เห็นแล้ว และ processor ไม่สลับลำดับ write กับ access อื่น. จึงถ้า P เขียน X แล้ว Y ทุก processor ที่เห็นค่าใหม่ของ Y จะเห็นค่าใหม่ของ X ด้วย.

**ประเด็นที่ต้องจำ**

- “seen” = read คืน written value (หน้า 102)
- write completes เมื่อทุก processor เห็นตาม assumptions ของสไลด์ (หน้า 102)
- P เขียน X ก่อน Y → เห็น Y ใหม่แล้วต้องเห็น X ใหม่ (หน้า 102)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- memory consistency
- write visibility
- write ordering

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้สถานการณ์ X ก่อน Y หน้า 102 ตรวจว่า observation ของอีก processor สอดคล้องสมมติฐานหรือไม่

**จุดที่อาจสับสน:** coherence หน้า 99 เน้นค่าและลำดับการเขียนของ X เดียว; consistency หน้า 102 ถามการมองเห็น write ของ X และ Y

**ประโยคช่วยจำ:** เห็น Y ใหม่ ต้องเห็น X ใหม่

### 29. ARM/Intel cache, 2-level TLB และ system instructions

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 103–107**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

สไลด์ยก ARM Cortex-A53 และ Intel Core i7 เพื่อดู multilevel on-chip caches กับ 2-level TLB organization จากภาพ. ทั้งสองมี multi-banked cache เพื่อรองรับหลาย access ต่อ cycle เมื่อไม่ชน bank และมีแนวทาง requested-word-first, non-blocking cache, hit/miss under miss และ data prefetching. ตาราง RISC-V แสดงกลุ่ม fence, CSR access และ system instructions; DGEMM ผสาน cache blocking กับ subword parallelism.

**ประเด็นที่ต้องจำ**

- ภาพ hierarchy ARM/Intel (หน้า 103) และ TLB สองระดับ (หน้า 104) ต้องดูตัวเลขจากภาพต้นฉบับ
- multi-banked รองรับ multiple issue เมื่อไม่มี bank conflict (หน้า 105)
- fence.i/fence/sfence.vm; CSR read/write/set/clear; ecall/ebreak/sret/wfi (หน้า 106)
- DGEMM รวม cache blocking และ subword parallelism (หน้า 107)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- multi-banked cache
- non-blocking cache
- prefetching
- fence
- CSR
- DGEMM

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 103–104 เปรียบการจัด L1/L2 และ TLB; หน้า 107 แสดงแนว blocking ของ matrix multiply

**จุดที่อาจสับสน:** อย่าตีความว่า multi-bank รับหลายคำขอได้เสมอ: สไลด์กำกับเงื่อนไข no bank conflicts

**ประโยคช่วยจำ:** หลาย bank ต้องไม่ชน; DGEMM บล็อกข้อมูล

### 30. Pitfalls และข้อสรุป Memory Hierarchy

**🟡 สำคัญ** · itds-211_comp_arch_Chapter04.pdf, **หน้า 108–111**

เหตุผลการจัดระดับ: เป็นตัวอย่างและการเปรียบเทียบที่สไลด์ใช้ประยุกต์หลักการ

การสับสน byte กับ word address เปลี่ยนตำแหน่ง mapping ใน cache; stride ใหญ่จากการวนแถว/คอลัมน์ผิดแบบทำให้ locality แย่. ใน multiprocessor ต้องคำนึง associativity ของ shared L2/L3; AMAT อย่างเดียวไม่สะท้อน out-of-order ที่มี non-blocked accesses. บทสรุปย้ำว่าลำดับชั้นและ caching อาศัย locality เพื่อให้ภาพเหมือน memory ทั้งเร็วและใหญ่.

**ประเด็นที่ต้องจำ**

- 32-byte cache, 4-byte blocks: byte 36 → block 1; word 36 → block 4 (หน้า 108)
- large stride ลด locality (หน้า 108)
- shared cache associativity น้อยกว่า core count อาจเกิด conflict misses (หน้า 109)
- AMAT ไม่รวมผล non-blocked accesses ของ out-of-order; สไลด์แนะนำ simulation (หน้า 109)
- segmentation และ VMM บน ISA ที่ไม่เอื้อต่อ virtualization เป็น pitfalls อีกสองข้อ (หน้า 110)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- byte/word address
- stride
- AMAT
- non-blocked access
- segmentation
- VMM

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** byte 36: floor(36/4)=9, 9 mod 8=1; word 36: 36 mod 8=4 ตาม cache 8 blocks หน้า 108

**จุดที่อาจสับสน:** อย่าใช้ AMAT ตัวเดียวตัดสิน out-of-order CPU; และอย่าสลับหน่วย byte/word ก่อนคำนวณ block index

**ประโยคช่วยจำ:** หน่วยก่อน index; locality ก่อนความเร็ว

## 3. Roadmap ทบทวน

1. **1 · หลัก locality และเทคโนโลยี** — เริ่ม temporal/spatial locality, memory hierarchy, SRAM/DRAM, flash และ disk (itds-211_comp_arch_Chapter04.pdf, หน้า 3–20)
2. **2 · Cache พื้นฐานและ mapping** — อ่าน block/tag/valid แล้วไล่ direct-mapped trace และ address fields (itds-211_comp_arch_Chapter04.pdf, หน้า 21–34)
3. **3 · Write, performance และ associativity** — แยก write policy ก่อนคำนวณ CPI/AMAT และเทียบ direct/n-way/fully (itds-211_comp_arch_Chapter04.pdf, หน้า 35–56)
4. **4 · Software และความน่าเชื่อถือ** — ต่อ locality ของโค้ด/blocked matrix แล้วทบทวน MTTF/Availability และ ECC (itds-211_comp_arch_Chapter04.pdf, หน้า 57–68)
5. **5 · Virtualization และ address translation** — ตาม VM/VMM → virtual memory/page table → TLB/page fault/protection (itds-211_comp_arch_Chapter04.pdf, หน้า 69–86)
6. **6 · กรอบออกแบบและ controller** — สรุป placement/finding/replacement/write, ประเภท miss และ FSM (itds-211_comp_arch_Chapter04.pdf, หน้า 87–97)
7. **7 · Multiprocessor และข้อควรระวัง** — ปิดด้วย coherence/consistency ระบบตัวอย่าง และ pitfalls (itds-211_comp_arch_Chapter04.pdf, หน้า 98–111)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · วางแผนภาพรวม

อ่านหน้า 3 และสรุป locality → hierarchy → cache → VM → multicore ด้วยภาษาตัวเอง

**เกณฑ์ผ่าน:** อธิบายว่าทำไม cache ช่วยให้เหมือนมีหน่วยความจำใหญ่และเร็วได้

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 3–8, 111

### รอบ 2 · ฝึก cache ทีละขั้น

ไล่ block/tag/index/offset, direct trace, write policy, associativity และ CPI/AMAT พร้อมเปิดภาพขยาย

**เกณฑ์ผ่าน:** ทำ trace หน้า 25–30 และ 48–49 รวมตัวอย่างหน้า 41–43 ได้

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 21–56

### รอบ 3 · ระบบที่พึ่ง cache

ทบทวน software blocking, dependability/ECC, VM/page table/TLB และ protection

**เกณฑ์ผ่าน:** แยก TLB miss กับ page fault และคำนวณ availability ได้

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 57–86

### รอบ 4 · วิเคราะห์ระบบหลาย core

ใช้สี่คำถามของ hierarchy วิเคราะห์ miss/FSM/coherence/consistency และ pitfalls

**เกณฑ์ผ่าน:** อธิบายเหตุผลของ invalidate และผลของ stride/byte-vs-word ได้

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 87–111

### รอบ 5 · ทดสอบเว้นระยะ

ทำคำถาม 3 ข้อต่อหัวข้อ สุ่ม quiz แล้วกลับไปอ่านเฉพาะข้อผิดในวันถัดไปตามเวลาที่มี

**เกณฑ์ผ่าน:** ตอบครบทุกหัวข้อและชี้จุดหน้า 32/55 ที่ต้องตรวจต้นฉบับได้

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 3–111

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1 locality + cache mapping/write/trace หน้า 3–40; วัน 2 CPI/AMAT/associativity/ECC/VM/TLB หน้า 41–86; วัน 3 miss/FSM/coherence/pitfalls หน้า 87–111 และทำคำถาม
- **ถ้าเหลือ 1 วัน:** เริ่ม cache mapping/trace/write หน้า 21–37 → CPI/AMAT/associativity หน้า 41–56 → VM/TLB หน้า 73–86 → miss/coherence หน้า 92–102 → สุ่มข้อผิด
- **ถ้าเหลือ 3 ชั่วโมง:** 0–45 นาที locality/cache mapping/write หน้า 4–37; 45–95 นาที CPI/AMAT/associativity หน้า 41–56; 95–140 นาที ECC/VM/TLB หน้า 63–86; 140–165 นาที miss/coherence หน้า 92–102; 165–180 นาที quiz และจุดหน้า 32/55

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

ลำดับความสำคัญเพื่อทบทวนตั้งจากนิยาม สูตร กลไก และตัวอย่างที่สไลด์เน้นต่อเนื่อง; ไม่สามารถยืนยันความถี่ออกสอบจากไฟล์เดียว

- **ควรท่องจำ:** locality, hit/miss, tag/index/offset, write policies, AMAT/CPI, associativity, MTTF/MTTR/MTBF/Availability, SEC/DEC, TLB และประเภท miss (หน้า 4–8, 21–56, 63–68, 73–93)
- **ควรฝึกโจทย์:** disk access 15k rpm, direct-map trace, address subdivision, CPI/AMAT, associative trace, L1/L2, availability และ byte/word mapping (หน้า 19, 25–32, 41–55, 64, 108)
- **ควรเข้าใจแนวคิด:** software blocking, VM/page fault, protection, FSM, coherence/consistency, bank conflicts และ pitfalls (หน้า 57–62, 69–86, 94–111)
- **เตรียมข้อสอบแบบผสม:** เลือกตอบศัพท์/แยก miss; อัตนัยอธิบายลำดับขั้น cache/VM/coherence; คำนวณ CPI/AMAT/mapping; วิเคราะห์ trace, diagram และจุดไม่สอดคล้องในต้นฉบับ

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 30 ข้อ, อัตนัย 30 ข้อ, วิเคราะห์ 22 ข้อ, คำนวณ 8 ข้อ

### Locality และ Memory Hierarchy

**ข้อ 1 · เลือกตอบ: สิ่งที่เพิ่งใช้มีแนวโน้มใช้ซ้ำเป็น locality แบบใด?**

- A. Temporal
- B. Spatial
- C. Write-back
- D. Fully associative

เฉลย: Temporal locality

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 3–8

**ข้อ 2 · อัตนัย: miss ratio สัมพันธ์กับ hit ratio อย่างไร?**

เฉลย: miss ratio = 1 − hit ratio

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 3–8

**ข้อ 3 · วิเคราะห์: หลังเกิด miss ข้อมูลถูกนำขึ้นมาในหน่วยใด?**

เฉลย: block หรือ line จากระดับล่างขึ้นระดับบน

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 3–8

### SRAM, DRAM และเทคนิคเพิ่ม bandwidth

**ข้อ 4 · เลือกตอบ: DRAM ต้องทำอะไรเป็นระยะตามหน้า 10?**

- A. Refresh
- B. Invalidate
- C. Page fault
- D. Write-around

เฉลย: Refresh

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 9–14

**ข้อ 5 · อัตนัย: DDR ต่างจากการส่งหนึ่งขอบสัญญาณอย่างไร?**

เฉลย: ส่งข้อมูลทั้ง rising และ falling clock edges

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 9–14

**ข้อ 6 · คำนวณ: ตัวอย่าง 4-word wide หน้า 14 มี bandwidth เท่าไร?**

เฉลย: 16 bytes/17 cycles≈0.94 B/cycle

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 9–14

### Flash: NOR, NAND และ wear leveling

**ข้อ 7 · เลือกตอบ: Flash ประเภทใดในสไลด์หนาแน่นและเข้าถึงเป็น block?**

- A. NAND
- B. NOR
- C. DRAM
- D. SRAM

เฉลย: NAND

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 15–16

**ข้อ 8 · อัตนัย: wear leveling ทำอะไร?**

เฉลย: ย้าย/กระจายข้อมูลไป block ที่ใช้น้อยเพื่อลดการสึกเฉพาะจุด

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 15–16

**ข้อ 9 · วิเคราะห์: Flash หน้า 15 ต่างจาก DRAM ด้านการคงข้อมูลอย่างไร?**

เฉลย: Flash เป็น nonvolatile; DRAM เก็บประจุและต้อง refresh ตามหน้า 10

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 15–16

### Disk sector และเวลาการเข้าถึง

**ข้อ 10 · เลือกตอบ: ส่วนใดคือเวลารอหัวอ่านย้ายตำแหน่ง?**

- A. Seek
- B. Rotation
- C. Transfer
- D. Refresh

เฉลย: Seek

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 17–20

**ข้อ 11 · อัตนัย: เวลาการเข้าถึง sector ประกอบด้วยอะไรบ้าง?**

เฉลย: queue, seek, rotational latency, transfer และ controller overhead

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 17–20

**ข้อ 12 · คำนวณ: ตัวอย่างหน้า 19 เมื่อ seek เหลือ 1ms ได้ read time ประมาณเท่าไร?**

เฉลย: 3.2ms ตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 17–20

### Cache lookup, direct mapping, tag และ valid

**ข้อ 13 · เลือกตอบ: direct-mapped block address หา index อย่างไร?**

- A. mod #cache blocks
- B. บวก tag
- C. หาร hit ratio
- D. คูณ miss penalty

เฉลย: block address mod จำนวน cache blocks

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 21–24

**ข้อ 14 · อัตนัย: valid bit ช่วยตอบอะไร?**

เฉลย: ช่อง cache มีข้อมูลที่ใช้ได้หรือยัง

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 21–24

**ข้อ 15 · วิเคราะห์: เหตุใด index ตรงแต่ tag ต่างจึงเป็น miss?**

เฉลย: ช่องเดียวกันอาจเก็บคนละ memory block จึงต้องเทียบ tag

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 21–24

### ไล่สถานะ 8-block direct-mapped cache

**ข้อ 16 · เลือกตอบ: word 22 ใช้ index ใดในตัวอย่าง?**

- A. 110
- B. 010
- C. 000
- D. 011

เฉลย: 110

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 25–30

**ข้อ 17 · อัตนัย: เพราะเหตุใด word 18 เป็น miss ที่ index 010?**

เฉลย: index เดียวกับ 26 แต่ tag 10 ต่างจาก tag 11 ที่เก็บอยู่

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 25–30

**ข้อ 18 · วิเคราะห์: access 16 ครั้งที่สองในหน้า 29 เป็น hit หรือ miss?**

เฉลย: Hit เพราะ entry 000 valid และ tag 10 ยังตรง

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 25–30

### Tag–Index–Offset และการคำนวณ block

**ข้อ 19 · เลือกตอบ: 16 bytes/block ต้องใช้ offset กี่บิต?**

- A. 4
- B. 6
- C. 10
- D. 22

เฉลย: 4 บิต

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 31–32

**ข้อ 20 · อัตนัย: สูตรหา block address จาก byte address คืออะไร?**

เฉลย: floor(address/bytes per block)

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 31–32

**ข้อ 21 · วิเคราะห์: address 1200 ใน cache 64 blocks, 16B/block ไป block ไหน?**

เฉลย: floor(1200/16)=75; 75 mod64=11

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 31–32

### ขนาด block กับการจัดการ cache miss

**ข้อ 22 · เลือกตอบ: block ใหญ่ใน cache ขนาดคงที่ทำให้จำนวน entry อย่างไร?**

- A. ลดลง
- B. เพิ่มขึ้น
- C. ไม่เปลี่ยน
- D. เป็นศูนย์

เฉลย: ลดลง

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 33–34

**ข้อ 23 · อัตนัย: CPU ทำอะไรเมื่อ cache miss ตามหน้า 34?**

เฉลย: stall pipeline แล้วดึง block จากระดับถัดไป

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 33–34

**ข้อ 24 · วิเคราะห์: เหตุใด block ใหญ่อาจเพิ่ม miss rate?**

เฉลย: มี entry น้อยลง เกิด competition/pollution มากขึ้น

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 33–34

### Write-through, write-back และ write miss

**ข้อ 25 · เลือกตอบ: นโยบายใดต้องติด dirty bit?**

- A. Write-back
- B. Write-through
- C. Write-around
- D. Direct mapped

เฉลย: Write-back

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 35–37

**ข้อ 26 · อัตนัย: write-around หมายถึงอะไรในหน้า 37?**

เฉลย: write miss แล้วไม่ fetch block เข้าค cache

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 35–37

**ข้อ 27 · คำนวณ: ตัวอย่างหน้า 35 effective CPI เท่าไร?**

เฉลย: 1+0.1×100=11

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 35–37

### Split cache และ main memory ที่รองรับ cache

**ข้อ 28 · เลือกตอบ: I-cache กับ D-cache ในตัวอย่างหน้า 38 แยกกันหรือรวมกัน?**

- A. แยกกัน
- B. รวมกัน
- C. ไม่ใช้ cache
- D. เป็น disk

เฉลย: แยกกัน

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 38–40

**ข้อ 29 · อัตนัย: miss penalty หน้า 40 ของ 4-word block ผ่าน 1-word DRAM เท่าไร?**

เฉลย: 65 bus cycles

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 38–40

**ข้อ 30 · คำนวณ: bandwidth ตัวอย่างหน้า 40 ได้เท่าไร?**

เฉลย: 16/65≈0.25 B/cycle

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 38–40

### Memory stall CPI และ AMAT

**ข้อ 31 · เลือกตอบ: สูตร AMAT คือข้อใด?**

- A. Hit time + miss rate×miss penalty
- B. Hit time×miss rate
- C. CPI+clock rate
- D. Tag+index+offset

เฉลย: Hit time + miss rate×miss penalty

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 41–44

**ข้อ 32 · อัตนัย: ทำไม D-cache หน้า 42 ต้องคูณ 0.36?**

เฉลย: มี load/store 36% ของ instructions จึงไม่ใช่ทุกคำสั่งที่เข้าถึง D-cache

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 41–44

**ข้อ 33 · คำนวณ: จงหา actual CPI ตัวอย่างหน้า 42**

เฉลย: 2+0.02×100+0.36×0.04×100=5.44

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 41–44

### Direct, n-way และ fully associative

**ข้อ 34 · เลือกตอบ: แบบใดวาง block ได้ทุก entry?**

- A. Fully associative
- B. Direct mapped
- C. Write-through
- D. Page table

เฉลย: Fully associative

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 45–47

**ข้อ 35 · อัตนัย: n-way set associative หา set อย่างไร?**

เฉลย: block number mod จำนวน sets

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 45–47

**ข้อ 36 · วิเคราะห์: ทำไม fully associative มี hardware cost สูง?**

เฉลย: ต้องค้น/เปรียบเทียบหลาย entry พร้อมกัน

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 45–47

### ตัวอย่าง access 0, 8, 0, 6, 8

**ข้อ 37 · เลือกตอบ: ลำดับ 0,8,0,6,8 แบบ fully associative มี hit กี่ครั้ง?**

- A. 2
- B. 0
- C. 1
- D. 5

เฉลย: 2 ครั้ง: ที่ 0 ครั้งที่สอง และ 8 ครั้งสุดท้าย

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 48–50

**ข้อ 38 · อัตนัย: direct mapped ในตัวอย่างมีเหตุใด miss ทุกครั้ง?**

เฉลย: 0 และ 8 ชน index เดียวกันและแทนกัน; access อื่นก็ไม่ทำให้มี hit ในลำดับนี้

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 48–50

**ข้อ 39 · วิเคราะห์: 2-way set associative ในหน้า 49 มี hit ที่ access ไหน?**

เฉลย: access 0 ครั้งที่สอง

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 48–50

### Replacement policy: LRU และ Random

**ข้อ 40 · เลือกตอบ: LRU แทน entry ใด?**

- A. ที่ไม่ถูกใช้นานที่สุด
- B. ที่เพิ่งใช้ล่าสุด
- C. tag ต่ำสุด
- D. entry แรกเสมอ

เฉลย: ไม่ถูกใช้นานที่สุด

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 51–52

**ข้อ 41 · อัตนัย: direct mapped มีนโยบายเลือก entry แทนหรือไม่?**

เฉลย: ไม่มี choice เพราะแต่ละ block มีที่เดียว

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 51–52

**ข้อ 42 · วิเคราะห์: ถ้ามี invalid entry ใน set ควรทำอย่างไรตามหน้า 52?**

เฉลย: ใช้ entry นั้นก่อนแทนข้อมูลที่ valid

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 51–52

### L1/L2 และตัวอย่าง CPI หลายระดับ

**ข้อ 43 · เลือกตอบ: L1 มักเน้นสิ่งใด?**

- A. hit time ต่ำ
- B. จุใหญ่ที่สุด
- C. disk latency
- D. ECC

เฉลย: hit time ต่ำ

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 53–56

**ข้อ 44 · อัตนัย: CPI เมื่อมีเพียง primary cache ในตัวอย่างเท่าไร?**

เฉลย: 1+0.02×400=9

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 53–56

**ข้อ 45 · คำนวณ: สมการ CPI เมื่อเพิ่ม L2 หน้า 55 ให้ผลเท่าไร?**

เฉลย: 1+0.02×20+0.005×400=3.4; แต่คำบรรยาย extra penalty ต้องตรวจต้นฉบับ

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 53–56

### Advanced CPU, locality ของ software และ blocking

**ข้อ 46 · เลือกตอบ: blocking ใน DGEMM มีเป้าหมายอะไร?**

- A. ใช้ข้อมูลซ้ำก่อนถูกแทน
- B. ปิด cache
- C. เพิ่ม stride
- D. ลบ DRAM

เฉลย: ใช้ข้อมูลซ้ำก่อนถูกแทน

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 57–62

**ข้อ 47 · อัตนัย: out-of-order CPU ทำอะไรระหว่าง miss ได้?**

เฉลย: คำสั่งอิสระบางส่วนยังเดินต่อ ส่วน dependent รอ

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 57–62

**ข้อ 48 · คำนวณ: BLOCKSIZE ในโค้ดตัวอย่างหน้า 61 เป็นเท่าไร?**

เฉลย: 32 ตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 57–62

### Dependability: MTTF, MTTR, MTBF, Availability

**ข้อ 49 · เลือกตอบ: สูตร Availability ในสไลด์คืออะไร?**

- A. MTTF/(MTTF+MTTR)
- B. MTTR/MTTF
- C. MTTF×MTTR
- D. MTBF−MTTR

เฉลย: MTTF/(MTTF+MTTR)

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 63–64

**ข้อ 50 · อัตนัย: MTBF สัมพันธ์กับ MTTF/MTTR อย่างไร?**

เฉลย: MTBF=MTTF+MTTR

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 63–64

**ข้อ 51 · วิเคราะห์: fault ทุกครั้งเป็น system failure หรือไม่?**

เฉลย: ไม่; หน้า 63 ระบุ fault อาจนำหรือไม่สู่ system failure

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 63–64

### Hamming SEC และ SEC/DEC

**ข้อ 52 · เลือกตอบ: minimum distance 3 ทำอะไรได้ตามสไลด์?**

- A. แก้ 1-bit และตรวจ 2-bit
- B. แก้ 2-bit
- C. ตรวจ 3-bit เท่านั้น
- D. ไม่ตรวจได้

เฉลย: แก้ 1-bit และตรวจ 2-bit

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 65–68

**ข้อ 53 · อัตนัย: parity bit ของ SEC วางที่ตำแหน่งใด?**

เฉลย: ตำแหน่งเลขกำลังสองเมื่อเริ่มนับ 1 จากซ้าย เช่น 1,2,4,8

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 65–68

**ข้อ 54 · วิเคราะห์: syndrome 1010 ในหน้า 67 หมายถึงอะไร?**

เฉลย: บิตตำแหน่ง 10 พลิก

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 65–68

### Virtual Machines, VMM และ privileged support

**ข้อ 55 · เลือกตอบ: ใคร map virtual resource ไป physical resource?**

- A. VMM
- B. guest application
- C. cache tag
- D. disk sector

เฉลย: VMM

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 69–72

**ข้อ 56 · อัตนัย: guest code ในตัวอย่างรัน mode ใด?**

เฉลย: user mode และ trap เมื่อเจอ privileged access

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 69–72

**ข้อ 57 · วิเคราะห์: timer interrupt ใต้ VMM จัดหน่วยใดต่อ?**

เฉลย: VMM เลือก/สลับ VM และจำลอง timer ให้ VM ที่ต้องการ

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 69–72

### Virtual Memory, address translation และ page fault

**ข้อ 58 · เลือกตอบ: หน่วย block ของ virtual memory เรียกว่าอะไร?**

- A. Page
- B. Sector
- C. Tag
- D. Word

เฉลย: Page

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 73–75

**ข้อ 59 · อัตนัย: page fault เกิดเมื่อใด?**

เฉลย: page ที่ต้องการไม่อยู่ใน main memory ต้องดึงจาก disk

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 73–75

**ข้อ 60 · วิเคราะห์: offset ของ 4K page ในภาพหน้า 74 กี่บิต?**

เฉลย: 12 บิต

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 73–75

### Page table, PTE และ replacement/write-back

**ข้อ 61 · เลือกตอบ: bit ใดบอก page ถูกเขียน?**

- A. Dirty bit
- B. Reference bit
- C. Tag bit
- D. Offset

เฉลย: Dirty bit

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 76–79

**ข้อ 62 · อัตนัย: PTE เก็บอะไรเมื่อ page อยู่ใน physical memory?**

เฉลย: physical page number และ status bits

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 76–79

**ข้อ 63 · วิเคราะห์: เหตุใด virtual memory ใช้ write-back?**

เฉลย: การเขียน disk ช้ามาก จึงเขียนเป็น page/block เมื่อจำเป็น

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 76–79

### TLB lookup, miss handler และ page fault handler

**ข้อ 64 · เลือกตอบ: TLB เก็บอะไรเป็นหลัก?**

- A. PTE
- B. sector data
- C. ECC syndrome
- D. CPU instruction text ทั้งหมด

เฉลย: PTE

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 80–84

**ข้อ 65 · อัตนัย: ถ้า page อยู่ RAM แต่ TLB miss จะทำอย่างไร?**

เฉลย: นำ PTE จาก page table มาเติม TLB แล้ว retry instruction

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 80–84

**ข้อ 66 · วิเคราะห์: ถ้า page ไม่อยู่ RAM ใครจัดการและทำอะไร?**

เฉลย: OS page fault handler ดึงจาก disk อัปเดต page table แล้ว restart

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 80–84

### TLB/Cache interaction และ Memory Protection

**ข้อ 67 · เลือกตอบ: physical-address cache tag ต้องทำอะไรก่อน lookup?**

- A. translate address
- B. write disk
- C. invalidate ทุก block
- D. เพิ่ม CPI

เฉลย: translate address

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 85–86

**ข้อ 68 · อัตนัย: aliasing ในหน้า 85 เกิดจากอะไร?**

เฉลย: virtual addresses ต่างกันอ้าง physical address ร่วมกัน

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 85–86

**ข้อ 69 · วิเคราะห์: หน้า 86 ระบุโหมดที่เข้าถึง page table/state ที่มีสิทธิ์สูงคืออะไร?**

เฉลย: supervisor/kernel mode

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 85–86

### กรอบร่วมของ Memory Hierarchy

**ข้อ 70 · เลือกตอบ: direct mapped มีทางเลือกวาง block กี่ตำแหน่ง?**

- A. 1
- B. n
- C. #entries
- D. ไม่จำกัด

เฉลย: 1

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 87–91

**ข้อ 71 · อัตนัย: ทำไม virtual memory ใช้ write-back?**

เฉลย: disk write latency สูงตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 87–91

**ข้อ 72 · วิเคราะห์: n-way set associative ต้องเปรียบเทียบ tag กี่รายการใน set?**

เฉลย: n รายการ

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 87–91

### Compulsory, Capacity, Conflict miss และ trade-offs

**ข้อ 73 · เลือกตอบ: first access เป็น miss ประเภทใด?**

- A. compulsory
- B. capacity
- C. conflict
- D. coherence

เฉลย: compulsory

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 92–93

**ข้อ 74 · อัตนัย: เพิ่ม associativity ลด miss ใดตามตาราง?**

เฉลย: conflict miss

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 92–93

**ข้อ 75 · วิเคราะห์: เหตุใดเพิ่ม block size มากเกินไปอาจเสียผล?**

เฉลย: miss penalty เพิ่ม และ pollution อาจทำให้ miss rate สูงขึ้น

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 92–93

### Cache Controller ด้วย Finite State Machine

**ข้อ 76 · เลือกตอบ: ตัวอย่าง cache หน้า 94 เป็นนโยบายใด?**

- A. write-back/write allocate
- B. write-through/write around
- C. fully associative
- D. non-blocking

เฉลย: write-back/write allocate

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 94–97

**ข้อ 77 · อัตนัย: เหตุใด index 10 บิต?**

เฉลย: 1024 blocks = 2^10 ตำแหน่ง

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 94–97

**ข้อ 78 · คำนวณ: FSM คำนวณ next state จากอะไร?**

เฉลย: current state และ current inputs

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 94–97

### Cache Coherence และ invalidating snooping

**ข้อ 79 · เลือกตอบ: snooping protocol ตรวจอะไร?**

- A. bus reads/writes
- B. disk sectors
- C. register file
- D. page offset

เฉลย: bus reads/writes

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 98–101

**ข้อ 80 · อัตนัย: directory-based protocol เก็บอะไร?**

เฉลย: sharing status ของ blocks ใน cache/memory

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 98–101

**ข้อ 81 · วิเคราะห์: หลัง A invalidate X แล้ว B อ่าน X จะเกิดอะไร?**

เฉลย: B cache miss แล้วได้ค่าที่อัปเดตจาก owner ตามตัวอย่าง

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 98–101

### Memory Consistency และลำดับการมองเห็น writes

**ข้อ 82 · เลือกตอบ: คำว่า seen หมายถึงอะไร?**

- A. read คืนค่าที่เขียน
- B. write เริ่มต้น
- C. cache miss
- D. disk เสร็จ

เฉลย: read คืนค่าที่เขียน

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 102

**ข้อ 83 · อัตนัย: สไลด์กำหนดว่า write complete เมื่อใด?**

เฉลย: เมื่อทุก processor เห็น write นั้น

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 102

**ข้อ 84 · วิเคราะห์: P เขียน X แล้ว Y; ถ้าอีก core เห็น Y ใหม่ ต้องเห็นอะไร?**

เฉลย: X ใหม่ด้วย ภายใต้สมมติฐานหน้า 102

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 102

### ARM/Intel cache, 2-level TLB และ system instructions

**ข้อ 85 · เลือกตอบ: multi-banked cache ช่วย multiple access ภายใต้เงื่อนไขใด?**

- A. ไม่มี bank conflicts
- B. cache fully associative
- C. ไม่มี TLB
- D. disk idle

เฉลย: ไม่มี bank conflicts

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 103–107

**ข้อ 86 · อัตนัย: หน้า 106 จัด ecall อยู่ในกลุ่มใด?**

เฉลย: System

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 103–107

**ข้อ 87 · วิเคราะห์: DGEMM หน้า 107 รวมเทคนิคใด?**

เฉลย: cache blocking กับ subword parallelism

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 103–107

### Pitfalls และข้อสรุป Memory Hierarchy

**ข้อ 88 · เลือกตอบ: byte 36 ในตัวอย่างหน้า 108 map ไป cache block ใด?**

- A. 1
- B. 4
- C. 9
- D. 36

เฉลย: 1

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 108–111

**ข้อ 89 · อัตนัย: ทำไม AMAT ไม่พอสำหรับ out-of-order processors?**

เฉลย: ไม่รวมผลของ non-blocked accesses ตามหน้า 109

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 108–111

**ข้อ 90 · วิเคราะห์: หลักการใดทำให้ caching ช่วยประสาน memory เร็วเล็กกับช้าใหญ่?**

เฉลย: principle of locality ตามหน้า 111

อ้างอิง: itds-211_comp_arch_Chapter04.pdf, หน้า 108–111

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- Principle of Locality · หน้า 4: สไลด์แสดง Principle of Locality สำหรับหัวข้อ Locality และ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 4) (itds-211_comp_arch_Chapter04.pdf, หน้า 4)
- Taking Advantage of locality · หน้า 5: สไลด์แสดง Taking Advantage of locality สำหรับหัวข้อ Locality และ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 5) (itds-211_comp_arch_Chapter04.pdf, หน้า 5)
- Memory Hierarchy · หน้า 6: สไลด์แสดง Memory Hierarchy สำหรับหัวข้อ Locality และ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 6) (itds-211_comp_arch_Chapter04.pdf, หน้า 6)
- Cache and Main Memory · หน้า 7: สไลด์แสดง Cache and Main Memory สำหรับหัวข้อ Locality และ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 7) (itds-211_comp_arch_Chapter04.pdf, หน้า 7)
- Memory Hierarchy Levels · หน้า 8: สไลด์แสดง Memory Hierarchy Levels สำหรับหัวข้อ Locality และ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 8) (itds-211_comp_arch_Chapter04.pdf, หน้า 8)
- Memory Technology · หน้า 9: สไลด์แสดง Memory Technology สำหรับหัวข้อ SRAM, DRAM และเทคนิคเพิ่ม bandwidth (itds-211_comp_arch_Chapter04.pdf, หน้า 9) (itds-211_comp_arch_Chapter04.pdf, หน้า 9)
- DRAM Technology · หน้า 10: สไลด์แสดง DRAM Technology สำหรับหัวข้อ SRAM, DRAM และเทคนิคเพิ่ม bandwidth (itds-211_comp_arch_Chapter04.pdf, หน้า 10) (itds-211_comp_arch_Chapter04.pdf, หน้า 10)
- Advanced DRAM Organization · หน้า 11: สไลด์แสดง Advanced DRAM Organization สำหรับหัวข้อ SRAM, DRAM และเทคนิคเพิ่ม bandwidth (itds-211_comp_arch_Chapter04.pdf, หน้า 11) (itds-211_comp_arch_Chapter04.pdf, หน้า 11)
- DRAM Generations · หน้า 12: สไลด์แสดง DRAM Generations สำหรับหัวข้อ SRAM, DRAM และเทคนิคเพิ่ม bandwidth (itds-211_comp_arch_Chapter04.pdf, หน้า 12) (itds-211_comp_arch_Chapter04.pdf, หน้า 12)
- DRAM Performance Factors · หน้า 13: สไลด์แสดง DRAM Performance Factors สำหรับหัวข้อ SRAM, DRAM และเทคนิคเพิ่ม bandwidth (itds-211_comp_arch_Chapter04.pdf, หน้า 13) (itds-211_comp_arch_Chapter04.pdf, หน้า 13)
- Increasing Memory Bandwidth · หน้า 14: สไลด์แสดง Increasing Memory Bandwidth สำหรับหัวข้อ SRAM, DRAM และเทคนิคเพิ่ม bandwidth (itds-211_comp_arch_Chapter04.pdf, หน้า 14) (itds-211_comp_arch_Chapter04.pdf, หน้า 14)
- Chapter 6 — Storage and Other I/O Topics — 11 · หน้า 15: สไลด์แสดง Chapter 6 — Storage and Other I/O Topics — 11 สำหรับหัวข้อ Flash: NOR, NAND และ wear leveling (itds-211_comp_arch_Chapter04.pdf, หน้า 15) (itds-211_comp_arch_Chapter04.pdf, หน้า 15)
- Chapter 6 — Storage and Other I/O Topics — 12 · หน้า 16: สไลด์แสดง Chapter 6 — Storage and Other I/O Topics — 12 สำหรับหัวข้อ Flash: NOR, NAND และ wear leveling (itds-211_comp_arch_Chapter04.pdf, หน้า 16) (itds-211_comp_arch_Chapter04.pdf, หน้า 16)
- Chapter 6 — Storage and Other I/O Topics — 13 · หน้า 17: สไลด์แสดง Chapter 6 — Storage and Other I/O Topics — 13 สำหรับหัวข้อ Disk sector และเวลาการเข้าถึง (itds-211_comp_arch_Chapter04.pdf, หน้า 17) (itds-211_comp_arch_Chapter04.pdf, หน้า 17)
- Chapter 6 — Storage and Other I/O Topics — 14 · หน้า 18: สไลด์แสดง Chapter 6 — Storage and Other I/O Topics — 14 สำหรับหัวข้อ Disk sector และเวลาการเข้าถึง (itds-211_comp_arch_Chapter04.pdf, หน้า 18) (itds-211_comp_arch_Chapter04.pdf, หน้า 18)
- Chapter 6 — Storage and Other I/O Topics — 15 · หน้า 19: แผนภาพเวลา disk access และตัวอย่าง 15,000 rpm ที่สไลด์ประมาณ 6.2 ms (itds-211_comp_arch_Chapter04.pdf, หน้า 19) (itds-211_comp_arch_Chapter04.pdf, หน้า 19)
- Chapter 6 — Storage and Other I/O Topics — 16 · หน้า 20: สไลด์แสดง Chapter 6 — Storage and Other I/O Topics — 16 สำหรับหัวข้อ Disk sector และเวลาการเข้าถึง (itds-211_comp_arch_Chapter04.pdf, หน้า 20) (itds-211_comp_arch_Chapter04.pdf, หน้า 20)
- Cache Memory · หน้า 21: สไลด์แสดง Cache Memory สำหรับหัวข้อ Cache lookup, direct mapping, tag และ valid (itds-211_comp_arch_Chapter04.pdf, หน้า 21) (itds-211_comp_arch_Chapter04.pdf, หน้า 21)
- Elements of Cache Design · หน้า 22: สไลด์แสดง Elements of Cache Design สำหรับหัวข้อ Cache lookup, direct mapping, tag และ valid (itds-211_comp_arch_Chapter04.pdf, หน้า 22) (itds-211_comp_arch_Chapter04.pdf, หน้า 22)
- Direct Mapped Cache · หน้า 23: สไลด์แสดง Direct Mapped Cache สำหรับหัวข้อ Cache lookup, direct mapping, tag และ valid (itds-211_comp_arch_Chapter04.pdf, หน้า 23) (itds-211_comp_arch_Chapter04.pdf, หน้า 23)
- Tags and Valid Bits · หน้า 24: สไลด์แสดง Tags and Valid Bits สำหรับหัวข้อ Cache lookup, direct mapping, tag และ valid (itds-211_comp_arch_Chapter04.pdf, หน้า 24) (itds-211_comp_arch_Chapter04.pdf, หน้า 24)
- Cache Example · หน้า 25: สไลด์แสดง Cache Example สำหรับหัวข้อ ไล่สถานะ 8-block direct-mapped cache (itds-211_comp_arch_Chapter04.pdf, หน้า 25) (itds-211_comp_arch_Chapter04.pdf, หน้า 25)
- Cache Example · หน้า 26: สไลด์แสดง Cache Example สำหรับหัวข้อ ไล่สถานะ 8-block direct-mapped cache (itds-211_comp_arch_Chapter04.pdf, หน้า 26) (itds-211_comp_arch_Chapter04.pdf, หน้า 26)
- Cache Example · หน้า 27: สไลด์แสดง Cache Example สำหรับหัวข้อ ไล่สถานะ 8-block direct-mapped cache (itds-211_comp_arch_Chapter04.pdf, หน้า 27) (itds-211_comp_arch_Chapter04.pdf, หน้า 27)
- Cache Example · หน้า 28: สไลด์แสดง Cache Example สำหรับหัวข้อ ไล่สถานะ 8-block direct-mapped cache (itds-211_comp_arch_Chapter04.pdf, หน้า 28) (itds-211_comp_arch_Chapter04.pdf, หน้า 28)
- Cache Example · หน้า 29: ตารางไล่ direct-mapped cache จากลำดับการเข้าถึงในตัวอย่าง 8 blocks (itds-211_comp_arch_Chapter04.pdf, หน้า 29) (itds-211_comp_arch_Chapter04.pdf, หน้า 29)
- Cache Example · หน้า 30: ตารางสรุป hit/miss และ block ที่ถูกแทนในตัวอย่าง direct-mapped (itds-211_comp_arch_Chapter04.pdf, หน้า 30) (itds-211_comp_arch_Chapter04.pdf, หน้า 30)
- Address Subdivision · หน้า 31: สไลด์แสดง Address Subdivision สำหรับหัวข้อ Tag–Index–Offset และการคำนวณ block (itds-211_comp_arch_Chapter04.pdf, หน้า 31) (itds-211_comp_arch_Chapter04.pdf, หน้า 31)
- Example: Larger Block Size · หน้า 32: ภาพแบ่ง Tag–Index–Offset ของ address; เลข bit สูงสุดกับผลรวมช่องไม่ตรงกัน: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter04.pdf, หน้า 32) (itds-211_comp_arch_Chapter04.pdf, หน้า 32)
- Block Size Considerations · หน้า 33: สไลด์แสดง Block Size Considerations สำหรับหัวข้อ ขนาด block กับการจัดการ cache miss (itds-211_comp_arch_Chapter04.pdf, หน้า 33) (itds-211_comp_arch_Chapter04.pdf, หน้า 33)
- Cache Misses · หน้า 34: สไลด์แสดง Cache Misses สำหรับหัวข้อ ขนาด block กับการจัดการ cache miss (itds-211_comp_arch_Chapter04.pdf, หน้า 34) (itds-211_comp_arch_Chapter04.pdf, หน้า 34)
- Write-Through · หน้า 35: สไลด์แสดง Write-Through สำหรับหัวข้อ Write-through, write-back และ write miss (itds-211_comp_arch_Chapter04.pdf, หน้า 35) (itds-211_comp_arch_Chapter04.pdf, หน้า 35)
- Write-Back · หน้า 36: สไลด์แสดง Write-Back สำหรับหัวข้อ Write-through, write-back และ write miss (itds-211_comp_arch_Chapter04.pdf, หน้า 36) (itds-211_comp_arch_Chapter04.pdf, หน้า 36)
- Write Allocation · หน้า 37: สไลด์แสดง Write Allocation สำหรับหัวข้อ Write-through, write-back และ write miss (itds-211_comp_arch_Chapter04.pdf, หน้า 37) (itds-211_comp_arch_Chapter04.pdf, หน้า 37)
- Example: Intrinsity FastMATH · หน้า 38: สไลด์แสดง Example: Intrinsity FastMATH สำหรับหัวข้อ Split cache และ main memory ที่รองรับ cache (itds-211_comp_arch_Chapter04.pdf, หน้า 38) (itds-211_comp_arch_Chapter04.pdf, หน้า 38)
- Example: Intrinsity FastMATH · หน้า 39: สไลด์แสดง Example: Intrinsity FastMATH สำหรับหัวข้อ Split cache และ main memory ที่รองรับ cache (itds-211_comp_arch_Chapter04.pdf, หน้า 39) (itds-211_comp_arch_Chapter04.pdf, หน้า 39)
- Main Memory Supporting Caches · หน้า 40: สไลด์แสดง Main Memory Supporting Caches สำหรับหัวข้อ Split cache และ main memory ที่รองรับ cache (itds-211_comp_arch_Chapter04.pdf, หน้า 40) (itds-211_comp_arch_Chapter04.pdf, หน้า 40)
- Measuring Cache Performance · หน้า 41: ตัวอย่าง memory stall cycles และ CPI จาก instruction mix (itds-211_comp_arch_Chapter04.pdf, หน้า 41) (itds-211_comp_arch_Chapter04.pdf, หน้า 41)
- Cache Performance Example · หน้า 42: ตัวอย่าง CPI เปรียบการลด miss rate และ miss penalty (itds-211_comp_arch_Chapter04.pdf, หน้า 42) (itds-211_comp_arch_Chapter04.pdf, หน้า 42)
- Average Access Time · หน้า 43: สูตร Average Memory Access Time (AMAT) และตัวอย่าง (itds-211_comp_arch_Chapter04.pdf, หน้า 43) (itds-211_comp_arch_Chapter04.pdf, หน้า 43)
- Performance Summary · หน้า 44: สไลด์แสดง Performance Summary สำหรับหัวข้อ Memory stall CPI และ AMAT (itds-211_comp_arch_Chapter04.pdf, หน้า 44) (itds-211_comp_arch_Chapter04.pdf, หน้า 44)
- Associative Caches · หน้า 45: สไลด์แสดง Associative Caches สำหรับหัวข้อ Direct, n-way และ fully associative (itds-211_comp_arch_Chapter04.pdf, หน้า 45) (itds-211_comp_arch_Chapter04.pdf, หน้า 45)
- Associative Cache Example · หน้า 46: สไลด์แสดง Associative Cache Example สำหรับหัวข้อ Direct, n-way และ fully associative (itds-211_comp_arch_Chapter04.pdf, หน้า 46) (itds-211_comp_arch_Chapter04.pdf, หน้า 46)
- Spectrum of Associativity · หน้า 47: สไลด์แสดง Spectrum of Associativity สำหรับหัวข้อ Direct, n-way และ fully associative (itds-211_comp_arch_Chapter04.pdf, หน้า 47) (itds-211_comp_arch_Chapter04.pdf, หน้า 47)
- Associativity Example · หน้า 48: ตาราง direct-mapped cache สำหรับลำดับ 0,8,0,6,8 (itds-211_comp_arch_Chapter04.pdf, หน้า 48) (itds-211_comp_arch_Chapter04.pdf, หน้า 48)
- Associativity Example · หน้า 49: ตารางเทียบ 2-way กับ fully associative สำหรับลำดับเดียวกัน (itds-211_comp_arch_Chapter04.pdf, หน้า 49) (itds-211_comp_arch_Chapter04.pdf, หน้า 49)
- How Much Associativity · หน้า 50: สไลด์แสดง How Much Associativity สำหรับหัวข้อ ตัวอย่าง access 0, 8, 0, 6, 8 (itds-211_comp_arch_Chapter04.pdf, หน้า 50) (itds-211_comp_arch_Chapter04.pdf, หน้า 50)
- Set Associative Cache Organization · หน้า 51: สไลด์แสดง Set Associative Cache Organization สำหรับหัวข้อ Replacement policy: LRU และ Random (itds-211_comp_arch_Chapter04.pdf, หน้า 51) (itds-211_comp_arch_Chapter04.pdf, หน้า 51)
- Replacement Policy · หน้า 52: สไลด์แสดง Replacement Policy สำหรับหัวข้อ Replacement policy: LRU และ Random (itds-211_comp_arch_Chapter04.pdf, หน้า 52) (itds-211_comp_arch_Chapter04.pdf, หน้า 52)
- Multilevel Caches · หน้า 53: สไลด์แสดง Multilevel Caches สำหรับหัวข้อ L1/L2 และตัวอย่าง CPI หลายระดับ (itds-211_comp_arch_Chapter04.pdf, หน้า 53) (itds-211_comp_arch_Chapter04.pdf, หน้า 53)
- Multilevel Cache Example · หน้า 54: สไลด์แสดง Multilevel Cache Example สำหรับหัวข้อ L1/L2 และตัวอย่าง CPI หลายระดับ (itds-211_comp_arch_Chapter04.pdf, หน้า 54) (itds-211_comp_arch_Chapter04.pdf, หน้า 54)
- Example (cont.) · หน้า 55: ตัวอย่าง L1/L2: ข้อความ extra penalty 500 cycles ไม่ตรงกับสมการที่ใช้ 400 cycles: ต้องตรวจสอบจากต้นฉบับ (itds-211_comp_arch_Chapter04.pdf, หน้า 55) (itds-211_comp_arch_Chapter04.pdf, หน้า 55)
- Multilevel Cache Considerations · หน้า 56: สไลด์แสดง Multilevel Cache Considerations สำหรับหัวข้อ L1/L2 และตัวอย่าง CPI หลายระดับ (itds-211_comp_arch_Chapter04.pdf, หน้า 56) (itds-211_comp_arch_Chapter04.pdf, หน้า 56)
- Interactions with Advanced CPUs · หน้า 57: สไลด์แสดง Interactions with Advanced CPUs สำหรับหัวข้อ Advanced CPU, locality ของ software และ blocking (itds-211_comp_arch_Chapter04.pdf, หน้า 57) (itds-211_comp_arch_Chapter04.pdf, หน้า 57)
- Interactions with Software · หน้า 58: สไลด์แสดง Interactions with Software สำหรับหัวข้อ Advanced CPU, locality ของ software และ blocking (itds-211_comp_arch_Chapter04.pdf, หน้า 58) (itds-211_comp_arch_Chapter04.pdf, หน้า 58)
- Software Optimization via Blocking · หน้า 59: สไลด์แสดง Software Optimization via Blocking สำหรับหัวข้อ Advanced CPU, locality ของ software และ blocking (itds-211_comp_arch_Chapter04.pdf, หน้า 59) (itds-211_comp_arch_Chapter04.pdf, หน้า 59)
- DGEMM Access Pattern · หน้า 60: สไลด์แสดง DGEMM Access Pattern สำหรับหัวข้อ Advanced CPU, locality ของ software และ blocking (itds-211_comp_arch_Chapter04.pdf, หน้า 60) (itds-211_comp_arch_Chapter04.pdf, หน้า 60)
- Cache Blocked DGEMM · หน้า 61: สไลด์แสดง Cache Blocked DGEMM สำหรับหัวข้อ Advanced CPU, locality ของ software และ blocking (itds-211_comp_arch_Chapter04.pdf, หน้า 61) (itds-211_comp_arch_Chapter04.pdf, หน้า 61)
- Blocked DGEMM Access Pattern · หน้า 62: สไลด์แสดง Blocked DGEMM Access Pattern สำหรับหัวข้อ Advanced CPU, locality ของ software และ blocking (itds-211_comp_arch_Chapter04.pdf, หน้า 62) (itds-211_comp_arch_Chapter04.pdf, หน้า 62)
- Chapter 6 — Storage and Other I/O Topics — 58 · หน้า 63: สไลด์แสดง Chapter 6 — Storage and Other I/O Topics — 58 สำหรับหัวข้อ Dependability: MTTF, MTTR, MTBF, Availability (itds-211_comp_arch_Chapter04.pdf, หน้า 63) (itds-211_comp_arch_Chapter04.pdf, หน้า 63)
- Chapter 6 — Storage and Other I/O Topics — 59 · หน้า 64: สไลด์แสดง Chapter 6 — Storage and Other I/O Topics — 59 สำหรับหัวข้อ Dependability: MTTF, MTTR, MTBF, Availability (itds-211_comp_arch_Chapter04.pdf, หน้า 64) (itds-211_comp_arch_Chapter04.pdf, หน้า 64)
- The Hamming SEC Code · หน้า 65: แผนภาพ Hamming code เพิ่ม parity bits เพื่อแก้ single-bit error (itds-211_comp_arch_Chapter04.pdf, หน้า 65) (itds-211_comp_arch_Chapter04.pdf, หน้า 65)
- Encoding SEC · หน้า 66: สไลด์แสดง Encoding SEC สำหรับหัวข้อ Hamming SEC และ SEC/DEC (itds-211_comp_arch_Chapter04.pdf, หน้า 66) (itds-211_comp_arch_Chapter04.pdf, หน้า 66)
- Decoding SEC · หน้า 67: สไลด์แสดง Decoding SEC สำหรับหัวข้อ Hamming SEC และ SEC/DEC (itds-211_comp_arch_Chapter04.pdf, หน้า 67) (itds-211_comp_arch_Chapter04.pdf, หน้า 67)
- SEC/DEC Code · หน้า 68: ตาราง syndrome และ parity สำหรับ SEC/DEC; ไม่มีตัวอย่างครบทุกบิตในหน้านี้ (itds-211_comp_arch_Chapter04.pdf, หน้า 68) (itds-211_comp_arch_Chapter04.pdf, หน้า 68)
- Virtual Machines · หน้า 69: สไลด์แสดง Virtual Machines สำหรับหัวข้อ Virtual Machines, VMM และ privileged support (itds-211_comp_arch_Chapter04.pdf, หน้า 69) (itds-211_comp_arch_Chapter04.pdf, หน้า 69)
- Virtual Machine Monitor · หน้า 70: สไลด์แสดง Virtual Machine Monitor สำหรับหัวข้อ Virtual Machines, VMM และ privileged support (itds-211_comp_arch_Chapter04.pdf, หน้า 70) (itds-211_comp_arch_Chapter04.pdf, หน้า 70)
- Example: Timer Virtualization · หน้า 71: สไลด์แสดง Example: Timer Virtualization สำหรับหัวข้อ Virtual Machines, VMM และ privileged support (itds-211_comp_arch_Chapter04.pdf, หน้า 71) (itds-211_comp_arch_Chapter04.pdf, หน้า 71)
- Instruction Set Support · หน้า 72: สไลด์แสดง Instruction Set Support สำหรับหัวข้อ Virtual Machines, VMM และ privileged support (itds-211_comp_arch_Chapter04.pdf, หน้า 72) (itds-211_comp_arch_Chapter04.pdf, หน้า 72)
- Virtual Memory · หน้า 73: สไลด์แสดง Virtual Memory สำหรับหัวข้อ Virtual Memory, address translation และ page fault (itds-211_comp_arch_Chapter04.pdf, หน้า 73) (itds-211_comp_arch_Chapter04.pdf, หน้า 73)
- Address Translation · หน้า 74: ภาพแปล virtual address เป็น physical address โดยคง page offset (itds-211_comp_arch_Chapter04.pdf, หน้า 74) (itds-211_comp_arch_Chapter04.pdf, หน้า 74)
- Page Fault Penalty · หน้า 75: สไลด์แสดง Page Fault Penalty สำหรับหัวข้อ Virtual Memory, address translation และ page fault (itds-211_comp_arch_Chapter04.pdf, หน้า 75) (itds-211_comp_arch_Chapter04.pdf, หน้า 75)
- Page Tables · หน้า 76: สไลด์แสดง Page Tables สำหรับหัวข้อ Page table, PTE และ replacement/write-back (itds-211_comp_arch_Chapter04.pdf, หน้า 76) (itds-211_comp_arch_Chapter04.pdf, หน้า 76)
- Translation Using a Page Table · หน้า 77: แผนภาพ Virtual Page Number, page table และ Physical Page Number (itds-211_comp_arch_Chapter04.pdf, หน้า 77) (itds-211_comp_arch_Chapter04.pdf, หน้า 77)
- Mapping Pages to Storage · หน้า 78: สไลด์แสดง Mapping Pages to Storage สำหรับหัวข้อ Page table, PTE และ replacement/write-back (itds-211_comp_arch_Chapter04.pdf, หน้า 78) (itds-211_comp_arch_Chapter04.pdf, หน้า 78)
- Replacement and Writes · หน้า 79: สไลด์แสดง Replacement and Writes สำหรับหัวข้อ Page table, PTE และ replacement/write-back (itds-211_comp_arch_Chapter04.pdf, หน้า 79) (itds-211_comp_arch_Chapter04.pdf, หน้า 79)
- Fast Translation Using a TLB · หน้า 80: สไลด์แสดง Fast Translation Using a TLB สำหรับหัวข้อ TLB lookup, miss handler และ page fault handler (itds-211_comp_arch_Chapter04.pdf, หน้า 80) (itds-211_comp_arch_Chapter04.pdf, หน้า 80)
- Fast Translation Using a TLB · หน้า 81: ลำดับ TLB hit/miss กับ page table และ page fault (itds-211_comp_arch_Chapter04.pdf, หน้า 81) (itds-211_comp_arch_Chapter04.pdf, หน้า 81)
- TLB Misses · หน้า 82: สไลด์แสดง TLB Misses สำหรับหัวข้อ TLB lookup, miss handler และ page fault handler (itds-211_comp_arch_Chapter04.pdf, หน้า 82) (itds-211_comp_arch_Chapter04.pdf, หน้า 82)
- TLB Miss Handler · หน้า 83: สไลด์แสดง TLB Miss Handler สำหรับหัวข้อ TLB lookup, miss handler และ page fault handler (itds-211_comp_arch_Chapter04.pdf, หน้า 83) (itds-211_comp_arch_Chapter04.pdf, หน้า 83)
- Page Fault Handler · หน้า 84: สไลด์แสดง Page Fault Handler สำหรับหัวข้อ TLB lookup, miss handler และ page fault handler (itds-211_comp_arch_Chapter04.pdf, หน้า 84) (itds-211_comp_arch_Chapter04.pdf, หน้า 84)
- TLB and Cache Interaction · หน้า 85: สไลด์แสดง TLB and Cache Interaction สำหรับหัวข้อ TLB/Cache interaction และ Memory Protection (itds-211_comp_arch_Chapter04.pdf, หน้า 85) (itds-211_comp_arch_Chapter04.pdf, หน้า 85)
- Memory Protection · หน้า 86: สไลด์แสดง Memory Protection สำหรับหัวข้อ TLB/Cache interaction และ Memory Protection (itds-211_comp_arch_Chapter04.pdf, หน้า 86) (itds-211_comp_arch_Chapter04.pdf, หน้า 86)
- The Memory Hierarchy · หน้า 87: สไลด์แสดง The Memory Hierarchy สำหรับหัวข้อ กรอบร่วมของ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 87) (itds-211_comp_arch_Chapter04.pdf, หน้า 87)
- Block Placement · หน้า 88: สไลด์แสดง Block Placement สำหรับหัวข้อ กรอบร่วมของ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 88) (itds-211_comp_arch_Chapter04.pdf, หน้า 88)
- Finding a Block · หน้า 89: สไลด์แสดง Finding a Block สำหรับหัวข้อ กรอบร่วมของ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 89) (itds-211_comp_arch_Chapter04.pdf, หน้า 89)
- Replacement · หน้า 90: สไลด์แสดง Replacement สำหรับหัวข้อ กรอบร่วมของ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 90) (itds-211_comp_arch_Chapter04.pdf, หน้า 90)
- Write Policy · หน้า 91: สไลด์แสดง Write Policy สำหรับหัวข้อ กรอบร่วมของ Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 91) (itds-211_comp_arch_Chapter04.pdf, หน้า 91)
- Sources of Misses · หน้า 92: สไลด์แสดง Sources of Misses สำหรับหัวข้อ Compulsory, Capacity, Conflict miss และ trade-offs (itds-211_comp_arch_Chapter04.pdf, หน้า 92) (itds-211_comp_arch_Chapter04.pdf, หน้า 92)
- Cache Design Trade-offs · หน้า 93: สไลด์แสดง Cache Design Trade-offs สำหรับหัวข้อ Compulsory, Capacity, Conflict miss และ trade-offs (itds-211_comp_arch_Chapter04.pdf, หน้า 93) (itds-211_comp_arch_Chapter04.pdf, หน้า 93)
- Cache Control · หน้า 94: ตัวอย่าง cache 16 KB, block 16 B, address 32 บิต และ field tag/index/offset (itds-211_comp_arch_Chapter04.pdf, หน้า 94) (itds-211_comp_arch_Chapter04.pdf, หน้า 94)
- Interface Signals · หน้า 95: สไลด์แสดง Interface Signals สำหรับหัวข้อ Cache Controller ด้วย Finite State Machine (itds-211_comp_arch_Chapter04.pdf, หน้า 95) (itds-211_comp_arch_Chapter04.pdf, หน้า 95)
- Finite State Machines · หน้า 96: สไลด์แสดง Finite State Machines สำหรับหัวข้อ Cache Controller ด้วย Finite State Machine (itds-211_comp_arch_Chapter04.pdf, หน้า 96) (itds-211_comp_arch_Chapter04.pdf, หน้า 96)
- Cache Controller FSM · หน้า 97: แผนภาพสถานะ FSM ของ cache controller (itds-211_comp_arch_Chapter04.pdf, หน้า 97) (itds-211_comp_arch_Chapter04.pdf, หน้า 97)
- Cache Coherence Problem · หน้า 98: ตารางสอง CPU core แสดงสำเนา X ใน cache ที่อาจไม่ตรงกัน (itds-211_comp_arch_Chapter04.pdf, หน้า 98) (itds-211_comp_arch_Chapter04.pdf, หน้า 98)
- Coherence Defined · หน้า 99: สไลด์แสดง Coherence Defined สำหรับหัวข้อ Cache Coherence และ invalidating snooping (itds-211_comp_arch_Chapter04.pdf, หน้า 99) (itds-211_comp_arch_Chapter04.pdf, หน้า 99)
- Cache Coherence Protocols · หน้า 100: สไลด์แสดง Cache Coherence Protocols สำหรับหัวข้อ Cache Coherence และ invalidating snooping (itds-211_comp_arch_Chapter04.pdf, หน้า 100) (itds-211_comp_arch_Chapter04.pdf, หน้า 100)
- Invalidating Snooping Protocols · หน้า 101: ตาราง invalidating snooping หลัง CPU A เขียน X แล้ว CPU B อ่านซ้ำ (itds-211_comp_arch_Chapter04.pdf, หน้า 101) (itds-211_comp_arch_Chapter04.pdf, หน้า 101)
- Memory Consistency · หน้า 102: สไลด์แสดง Memory Consistency สำหรับหัวข้อ Memory Consistency และลำดับการมองเห็น writes (itds-211_comp_arch_Chapter04.pdf, หน้า 102) (itds-211_comp_arch_Chapter04.pdf, หน้า 102)
- Multilevel On-Chip Caches · หน้า 103: ภาพลำดับ cache ของ ARM Cortex-A53 และ Intel Core i7 (itds-211_comp_arch_Chapter04.pdf, หน้า 103) (itds-211_comp_arch_Chapter04.pdf, หน้า 103)
- 2-Level TLB Organization · หน้า 104: ภาพการจัด TLB สองระดับของระบบตัวอย่าง (itds-211_comp_arch_Chapter04.pdf, หน้า 104) (itds-211_comp_arch_Chapter04.pdf, หน้า 104)
- Supporting Multiple Issue · หน้า 105: สไลด์แสดง Supporting Multiple Issue สำหรับหัวข้อ ARM/Intel cache, 2-level TLB และ system instructions (itds-211_comp_arch_Chapter04.pdf, หน้า 105) (itds-211_comp_arch_Chapter04.pdf, หน้า 105)
- RISC-V System Instructions · หน้า 106: สไลด์แสดง RISC-V System Instructions สำหรับหัวข้อ ARM/Intel cache, 2-level TLB และ system instructions (itds-211_comp_arch_Chapter04.pdf, หน้า 106) (itds-211_comp_arch_Chapter04.pdf, หน้า 106)
- DGEMM · หน้า 107: ภาพ DGEMM ที่รวม cache blocking กับ subword parallelism (itds-211_comp_arch_Chapter04.pdf, หน้า 107) (itds-211_comp_arch_Chapter04.pdf, หน้า 107)
- Pitfalls · หน้า 108: ตัวอย่าง byte 36 กับ word 36 map ไป cache block ต่างกัน (itds-211_comp_arch_Chapter04.pdf, หน้า 108) (itds-211_comp_arch_Chapter04.pdf, หน้า 108)
- Pitfalls · หน้า 109: สไลด์แสดง Pitfalls สำหรับหัวข้อ Pitfalls และข้อสรุป Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 109) (itds-211_comp_arch_Chapter04.pdf, หน้า 109)
- Pitfalls · หน้า 110: สไลด์แสดง Pitfalls สำหรับหัวข้อ Pitfalls และข้อสรุป Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 110) (itds-211_comp_arch_Chapter04.pdf, หน้า 110)
- Concluding Remarks · หน้า 111: สไลด์แสดง Concluding Remarks สำหรับหัวข้อ Pitfalls และข้อสรุป Memory Hierarchy (itds-211_comp_arch_Chapter04.pdf, หน้า 111) (itds-211_comp_arch_Chapter04.pdf, หน้า 111)
