# Chapter06 · Storage Systems (External memory)

ITDS-211 · Computer Architecture & Operating System · W. Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter06.pdf** จำนวน 45 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter06 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/วิเคราะห์/คำนวณ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 22 หัวข้อ · 🔴 ต้องจำแน่นอน 14 หัวข้อ (63.6%) · 🟡 สำคัญ 7 หัวข้อ (31.8%) · ⚪ อ่านเสริม 1 หัวข้อ (4.5%) · แบบฝึก 66 ข้อ · Flashcard 41 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter06 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| สื่อแม่เหล็กและหัวอ่าน/เขียน | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 4–6 |
| Track, sector, cylinder และรูปแบบ sector | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 7–9 |
| ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง | 🟡 สำคัญ | itds-211_comp_arch_Chapter06.pdf, หน้า 10–13 |
| เวลา I/O ของ magnetic disk | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 14–15 |
| RAID: ภาพรวมและจำนวนดิสก์ | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 16–19 |
| RAID 0: striping ไม่มี redundancy | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 18, 20–21 |
| RAID 1: mirroring | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 18, 22 |
| RAID 2: Hamming code | 🟡 สำคัญ | itds-211_comp_arch_Chapter06.pdf, หน้า 18, 23 |
| RAID 3: bit-interleaved parity | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 19, 24 |
| RAID 4: block parity แยกดิสก์ | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 19, 25 |
| RAID 5: distributed parity | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26 |
| RAID 6: dual distributed parity | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26 |
| ตารางเปรียบเทียบ RAID และการเลือกอ่าน | 🟡 สำคัญ | itds-211_comp_arch_Chapter06.pdf, หน้า 17, 27–28 |
| SSD เทียบ HDD ในสไลด์ | 🟡 สำคัญ | itds-211_comp_arch_Chapter06.pdf, หน้า 29–30 |
| โครงสร้าง SSD | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 31 |
| ปัญหาการเขียนและอายุใช้งาน SSD | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 32 |
| ตระกูล optical disk | 🟡 สำคัญ | itds-211_comp_arch_Chapter06.pdf, หน้า 33 |
| CD-ROM: การผลิต การอ่าน และ block format | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 34–37 |
| CD-R กับ CD-RW | 🟡 สำคัญ | itds-211_comp_arch_Chapter06.pdf, หน้า 38 |
| DVD-ROM, Blu-Ray และความหนาแน่น optical | 🟡 สำคัญ | itds-211_comp_arch_Chapter06.pdf, หน้า 39–40 |
| Magnetic tape: serial และ serpentine | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter06.pdf, หน้า 41–42 |
| ตาราง LTO เป็นตัวอย่างในสไลด์ | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter06.pdf, หน้า 43 |

### บทนี้เรียนเพื่ออะไร

บทนี้เรียนเพื่อเข้าใจว่าสื่อจัดเก็บภายนอกบันทึก จัดตำแหน่ง เข้าถึง และป้องกันข้อมูลอย่างไร: เริ่มจาก disk layout และเวลา I/O แล้วเทียบ RAID, SSD, optical disk กับ magnetic tape ตามกลไกและข้อจำกัดในสไลด์

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 3–44

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- ระบุส่วนประกอบ magnetic disk, layout และคำนวณ access time ตามนิยามในสไลด์ (itds-211_comp_arch_Chapter06.pdf, หน้า 4–15)
- แยก RAID 0–6 ตาม striping/mirror/parity, parallel/independent access และจำนวนดิสก์ (itds-211_comp_arch_Chapter06.pdf, หน้า 16–28)
- อธิบาย SSD controller, flash erase/write และวิธีกระจายการสึกหรอ (itds-211_comp_arch_Chapter06.pdf, หน้า 29–32)
- เทียบชนิด optical disk/block format และลำดับบันทึกแบบ magnetic tape (itds-211_comp_arch_Chapter06.pdf, หน้า 33–44)

วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจาก outline หน้า 3 และ summary หน้า 44

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- อ่านและตรวจภาพครบ 45 หน้า: หน้า 1 ปก, หน้า 2 course outline, หน้า 3 chapter outline, หน้า 44 summary, หน้า 45 Q&A
- สไลด์ไม่มีรายการ Chapter Objectives โดยตรงหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; ระดับสีเป็นลำดับเวลาอ่าน ไม่ใช่สถิติการออกสอบ
- หน้า 16 อธิบาย RAID แบบมี redundant parity ครบทุกระดับ แต่หน้า 17–18 ระบุ RAID 0 nonredundant: ต้องตรวจสอบจากต้นฉบับ
- ตาราง HDD หน้า 13, SSD/HDD หน้า 30, optical หน้า 33 และ LTO หน้า 43 เป็นตัวอย่างจากช่วงเวลาของสไลด์ ไม่ใช่ข้อมูลราคา/สเปกปัจจุบัน
- สไลด์หน้า 23 เขียน byte/word strips ในเนื้อหาและมีหมายเหตุภาษาไทยว่า bit-level; ระดับ strip ที่แน่ชัดของ RAID 2 ในบริบทนี้: ต้องตรวจสอบจากต้นฉบับ
- คำถามคำนวณใช้เฉพาะสูตรและตัวเลขที่อยู่ในสไลด์; ไม่มีการอ้างว่าเป็นข้อสอบจริง

## 2. สรุปรายบทและหัวข้อ

### 1. สื่อแม่เหล็กและหัวอ่าน/เขียน

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 4–6**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

Magnetic disk ใช้ platter ที่เคลือบวัสดุแม่เหล็กและเก็บบิตด้วยสภาพการเป็นแม่เหล็กของบริเวณเล็ก ๆ. สไลด์เทียบวัสดุฐานอะลูมิเนียมกับแก้ว และแสดงหัวเขียนแบบ inductive กับหัวอ่านแบบ magnetoresistive. การอ่านกับเขียนจึงเป็นกระบวนการคนละทิศของการแปลงสัญญาณและสภาพแม่เหล็ก.

**ประเด็นที่ต้องจำ**

- Platter มี substrate และ magnetizable coating (หน้า 4)
- ฐานแก้วช่วยผิวสม่ำเสมอ ลด defect และเอื้อ fly height ต่ำในสไลด์ (หน้า 4)
- ภาพแยก inductive write กับ magnetoresistive read (หน้า 5–6)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- platter
- substrate
- magnetizable material
- inductive write
- magnetoresistive read
- read/write head

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านภาพหน้า 5–6 โดยตามทิศสัญญาณจากหัวเขียนสู่สื่อ และจากสื่อกลับสู่หัวอ่าน

**จุดที่อาจสับสน:** อย่านำชนิดหัวอ่านไปเรียกว่าหัวเขียน; บิตในภาพสัมพันธ์กับสภาพแม่เหล็กบนสื่อ

**ประโยคช่วยจำ:** เขียนให้สื่อเปลี่ยน อ่านจากสื่อกลับมา

### 2. Track, sector, cylinder และรูปแบบ sector

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 7–9**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

ผิว platter แบ่งเป็น tracks วงซ้อนและ sectors ตามส่วนโค้ง; cylinder คือ tracks ที่ตำแหน่งรัศมีเดียวกันของหลายผิว. ภาพยังแสดง inter-track/inter-sector gaps และหัวอ่านหนึ่งหัวต่อผิว. สไลด์เปรียบ constant angular velocity กับ multiple zone recording และยก Winchester ST506 เป็นตัวอย่าง sector ที่มี ID, data, CRC และ gaps.

**ประเด็นที่ต้องจำ**

- Track เป็นวง; sector เป็นส่วนของ track; cylinder รวม track ที่รัศมีตรงกัน (หน้า 7)
- Multiple zone recording แบ่ง track เป็น zones ให้จำนวน sectors/track ต่างกัน (หน้า 8)
- ST506 เป็นตัวอย่าง 600 bytes/sector แต่ data จริง 512 bytes พร้อมข้อมูลจัดรูปแบบ (หน้า 9)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- track
- sector
- cylinder
- constant angular velocity (CAV)
- multiple zone recording
- CRC
- ID field

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตัวอย่างหน้า 9: 17+7+41+515+20 = 600 bytes/sector; data field 515 bytes มี synch 1, data 512 และ CRC 2

**สูตรที่ต้องรู้**

```text
600 − 512 = 88 bytes
```

overhead ของ sector ST506 ในตัวอย่างหน้า 9; ไม่ใช่ค่าทั่วไปของดิสก์ทุกแบบ

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 9

**จุดที่อาจสับสน:** 600 bytes เป็นขนาด physical sector ในตัวอย่าง ST506 ไม่ใช่ 600 bytes ของ user data

**ประโยคช่วยจำ:** วง track–ชิ้น sector–ชั้น cylinder

### 3. ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง

**🟡 สำคัญ** · itds-211_comp_arch_Chapter06.pdf, **หน้า 10–13**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก

สไลด์จำแนก fixed-head/movable-head, removable/nonremovable, single-/double-sided, จำนวน platters และระยะสัมผัสหัวกับจาน. หัวที่แคบเพิ่มความหนาแน่นได้ แต่ต้องเข้าใกล้ผิวมากขึ้นและเสี่ยงต่อข้อผิดพลาด. Winchester ใช้ enclosure ปิดเพื่อลดสิ่งปนเปื้อน และหัวลอยเหนือผิวเมื่อหมุน; ตารางหน้า 13 เป็นสเปกอุปกรณ์ตัวอย่างของเอกสาร.

**ประเด็นที่ต้องจำ**

- Fixed-head เลือกหัว; movable-head เคลื่อนหัวไป track (หน้า 10–11)
- Removable media ถอดออกจาก drive ได้; double-sided ใช้สองผิว (หน้า 10–11)
- Winchester ใช้หัวลอยตามอากาศเหนือผิวใน enclosure ปิด (หน้า 12)
- ค่ารุ่นในตารางหน้า 13 เป็นตัวอย่างของช่วงเวลาสไลด์

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- fixed-head
- movable-head
- removable disk
- double-sided
- Winchester disk
- fly height

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้หัวตารางหน้า 13 อ่านความสัมพันธ์ capacity, rpm, seek และ transfer rate ของรุ่นที่ยก ไม่ใช้แทนสเปกปัจจุบัน

**จุดที่อาจสับสน:** fixed-head หมายถึงหัวประจำ track ไม่ใช่ platter หยุดหมุน; ตัวเลขตารางไม่ใช่มาตรฐานปัจจุบัน

**ประโยคช่วยจำ:** เลือกหัวหรือเลื่อนหัว; จานยังหมุน

### 4. เวลา I/O ของ magnetic disk

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 14–15**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

ภาพเวลา I/O แยกการรออุปกรณ์ รอ channel การ seek การรอจานหมุน และการ transfer. Seek time คือเวลาวางหัวที่ track เป้าหมายใน movable-head; rotational delay คือรอ sector มาถึงหัว. Access time ในสไลด์นิยามเป็น seek time + rotational delay แล้วจึงเกิด transfer time.

**ประเด็นที่ต้องจำ**

- Seek time: วางหัวที่ track (หน้า 15)
- Rotational delay: รอ sector หมุนมาถึงหัว (หน้า 15)
- Access time = seek time + rotational delay; transfer time เกิดเมื่อหัวอยู่ตำแหน่งแล้ว (หน้า 15)
- ภาพหน้า 14 ยังแยก device/channel wait

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- seek time
- rotational delay / rotational latency
- access time
- transfer time
- device busy
- wait for channel

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จากนิยามหน้า 15 ให้รวม seek time กับ rotational delay เพื่อหา access time โดยแยก transfer time ไว้หลังจากนั้น

**สูตรที่ต้องรู้**

```text
Access time = seek time + rotational delay
```

นิยามในสไลด์ ไม่รวม transfer time หรือเวลา wait for device/channel

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 15

**จุดที่อาจสับสน:** อย่ารวม transfer หรือ device/channel wait เข้า access time ตามนิยามหน้า 15

**ประโยคช่วยจำ:** เข้าถึง = หา track + รอ sector; จากนั้นถ่ายข้อมูล

### 5. RAID: ภาพรวมและจำนวนดิสก์

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 16–19**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

RAID (Redundant Array of Independent Disks) ทำให้หลาย physical disks ปรากฏเป็น logical drive และกระจายข้อมูลด้วย striping. ตารางแยก RAID 0–6 ตาม nonredundant, mirroring, Hamming และ parity รวมทั้ง parallel versus independent access. จำนวนดิสก์ในตารางคือ RAID 0 = N, RAID 1 = 2N, RAID 2 = N+m, RAID 3–5 = N+1 และ RAID 6 = N+2.

**ประเด็นที่ต้องจำ**

- N คือจำนวน data disks; m แปรตาม log N ใน RAID 2 (หน้า 17)
- RAID 2–3 เป็น parallel access; RAID 4–6 เป็น independent access (หน้า 17)
- หน้า 16 กล่าวว่าทุกระดับมี redundancy แต่หน้า 17 ระบุ RAID 0 nonredundant: ต้องตรวจสอบจากต้นฉบับ

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID
- logical drive
- striping
- mirroring
- parity
- N
- m

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ตารางหน้า 17 แล้วจับคู่ระดับกับวิธี redundancy และจำนวนดิสก์ ก่อนอ่านภาพการจัด strip หน้า 18–19

| ระดับ | รูปแบบ | จำนวนดิสก์ |
| --- | --- | --- |
| 0 | nonredundant striping | N |
| 1 | mirroring | 2N |
| 2 | Hamming code | N+m |
| 3/4/5 | parity ต่างการจัดวาง | N+1 |
| 6 | dual distributed parity | N+2 |

**จุดที่อาจสับสน:** ข้อความเหมารวมเรื่อง parity/redundancy หน้า 16 ขัดกับ RAID 0 หน้า 17–18; ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** 0 ไม่มีสำรอง; 1 ทำคู่; 2–6 ต่างวิธีตรวจและกระจาย

### 6. RAID 0: striping ไม่มี redundancy

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 18, 20–21**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

RAID 0 แบ่ง logical data เป็น strips กระจายบนดิสก์หลายตัวโดยไม่สำรอง. ภาพหน้า 20 แสดง logical strips 0–15 แมปไปสี่ physical disks. ความเร็วขึ้นกับทั้งทางเดินจาก host memory ไปดิสก์และรูปแบบ I/O request; small request มักถูก seek/rotational latency ครอบงำ ส่วนหลาย request กระจายภาระได้.

**ประเด็นที่ต้องจำ**

- Nonredundant; ใช้ N ดิสก์ตามตาราง (หน้า 17–18)
- logical strips กระจายลง physical disks (หน้า 20)
- small request ถูก seek/rotation ครอบงำ; large strip อาจให้หลาย request ทำพร้อมกัน (หน้า 21)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID 0
- strip
- striping
- logical disk
- physical disk
- load balancing

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตาม strip 0,1,2,3 ในภาพหน้า 20 จะอยู่คนละ physical disk ก่อนวนกลับ

**จุดที่อาจสับสน:** RAID 0 ไม่มี parity หรือ mirror แม้หน้า 16 จะพูดถึงคุณลักษณะ RAID แบบรวม

**ประโยคช่วยจำ:** ศูนย์ = กระจาย แต่ไม่สำรอง

### 7. RAID 1: mirroring

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 18, 22**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

RAID 1 ทำสำเนาข้อมูลทั้งชุด โดย logical strip หนึ่งแมปลงดิสก์สองตัวที่เป็น mirror กัน. อ่านจากตัวใดก็ได้ และเมื่อไดรฟ์เสียจะเข้าถึงจากสำเนาอีกตัวแล้วฟื้นระบบได้ง่าย. สไลด์ระบุว่าไม่มี “write penalty” ในความหมายของตน และข้อเสียหลักคือค่าใช้จ่ายของดิสก์ที่ซ้ำ.

**ประเด็นที่ต้องจำ**

- Mirroring = duplicate all data; 2N disks (หน้า 17–18, 22)
- อ่านจากดิสก์คู่ใดก็ได้และสำรองแบบ real time (หน้า 22)
- สไลด์กล่าวไม่มี “write penalty”; ข้อเสียหลักคือ cost (หน้า 22)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID 1
- mirroring
- mirror disk
- logical strip
- read request

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 18 วาง strip ชุดเดียวกันซ้ำทั้งฝั่งซ้ายและขวา

**จุดที่อาจสับสน:** การเขียนยังต้องทำสำเนา แต่สไลด์ใช้คำว่าไม่มี “write penalty”; อย่าตีความเป็นเขียนดิสก์เดียว

**ประโยคช่วยจำ:** หนึ่ง = มีคู่สำเนา

### 8. RAID 2: Hamming code

**🟡 สำคัญ** · itds-211_comp_arch_Chapter06.pdf, **หน้า 18, 23**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก

RAID 2 ใช้ parallel access ที่ดิสก์ทำงานร่วมกันทุก I/O request และกระจายข้อมูลเป็น strips เล็กระดับ byte/word. คำนวณ Hamming code ข้ามบิตจาก data disks แล้วเก็บ code บน redundant disks หลายตัว. ตามสไลด์ Hamming code แก้ single-bit error และตรวจ double-bit error ได้ โดยจำนวนดิสก์เสริมแปรตาม log N.

**ประเด็นที่ต้องจำ**

- parallel access และ synchronized spindles (หน้า 23)
- strips เล็กมากและ Hamming ECC เก็บบนหลายดิสก์ (หน้า 18, 23)
- single-bit correction/double-bit detection ตามสไลด์ (หน้า 23)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID 2
- parallel access
- Hamming code
- ECC
- N+m

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูภาพหน้า 18: b0–b3 เป็นข้อมูล และ f0(b)–f2(b) เป็น code ที่แยกดิสก์

**จุดที่อาจสับสน:** Hamming code ของ RAID 2 ไม่ใช่ parity disk เดียวแบบ RAID 3

**ประโยคช่วยจำ:** สอง = code หลายดิสก์

### 9. RAID 3: bit-interleaved parity

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 19, 24**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

RAID 3 ใช้ parallel access และ strips เล็ก โดยคำนวณ parity จากบิตตำแหน่งตรงกันบน data disks แล้วเก็บบนดิสก์สำรองหนึ่งตัว. สไลด์ยกอัตรา transfer สูงและการ reconstruct เมื่อดิสก์เสีย. ระหว่างซ่อมยังมีข้อมูลใน reduced mode แต่ workload แบบ transaction-oriented ทำงานด้อยลง.

**ประเด็นที่ต้องจำ**

- parity disk เดียวไม่ว่าขนาดอาร์เรย์ (หน้า 24)
- parallel access และ small strips (หน้า 24)
- เสียหนึ่งตัว: reconstruct จากดิสก์ที่เหลือกับ parity และทำงาน reduced mode (หน้า 24)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID 3
- bit-interleaved parity
- parallel access
- reduced mode
- parity disk

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดู P(b) บนดิสก์ขวาของ RAID 3 ในภาพหน้า 19

**จุดที่อาจสับสน:** RAID 3 เป็น parallel access; อย่าสลับกับ RAID 4 ที่เป็น independent access

**ประโยคช่วยจำ:** สาม = parity หนึ่งตัวและดิสก์ทำพร้อมกัน

### 10. RAID 4: block parity แยกดิสก์

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 19, 25**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

RAID 4 ใช้ independent access และ strips ค่อนข้างใหญ่ โดย parity ของแต่ละกลุ่มอยู่บนดิสก์เฉพาะ. การเขียน strip เล็กต้องอ่าน old user strip กับ old parity แล้วเขียน user strip และ parity ใหม่ จึงเป็น 2 reads + 2 writes. ดิสก์ parity กลายเป็นคอขวดของการเขียนที่สไลด์ชี้ให้เห็น.

**ประเด็นที่ต้องจำ**

- independent access: ดิสก์รับ request แยกกันได้ (หน้า 25)
- large strips และ dedicated parity disk (หน้า 19, 25)
- small write = 2 reads + 2 writes (หน้า 25)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID 4
- independent access
- block-interleaved parity
- dedicated parity disk
- write penalty

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ติดตาม P(0–3), P(4–7) ในภาพหน้า 19: parity อยู่คอลัมน์เดิม

**จุดที่อาจสับสน:** อย่าสับสนกับ RAID 5 ที่ parity หมุนเวียนบนทุกดิสก์

**ประโยคช่วยจำ:** สี่ = parity ดิสก์เดียว; เขียนต้องแตะสี่ครั้ง

### 11. RAID 5: distributed parity

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 19, 26**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

RAID 5 จัด block-level strips คล้าย RAID 4 แต่หมุนตำแหน่ง parity strips ไปตามดิสก์ทุกตัว มักเป็น round-robin. การกระจายนี้หลีกเลี่ยงคอขวด I/O บน dedicated parity disk ของ RAID 4. ตารางหน้า 17 จัดเป็น N+1 disks และ independent access.

**ประเด็นที่ต้องจำ**

- distributed parity; ไม่ fix บนดิสก์เดียว (หน้า 19, 26)
- typical allocation แบบ round-robin (หน้า 26)
- หลีกเลี่ยง RAID 4 parity-disk bottleneck (หน้า 26)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID 5
- block-interleaved distributed parity
- round-robin
- independent access
- N+1

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูภาพหน้า 19: P(0–3), P(4–7), P(8–11) ย้ายตำแหน่งดิสก์

**จุดที่อาจสับสน:** หน้า 26 แบ่งสองคอลัมน์: dual parity เป็นของ RAID 6 ไม่ใช่ RAID 5

**ประโยคช่วยจำ:** ห้า = parity หมุนเวียน

### 12. RAID 6: dual distributed parity

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 19, 26**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

RAID 6 ใช้ parity สองชุดจากการคำนวณต่างกัน เก็บคนละ block บนคนละดิสก์. สไลด์อธิบาย data availability สูง: ต้องมีสามดิสก์เสียภายใน mean time to repair (MTTR) จึงทำข้อมูลหายตามเงื่อนไขที่กล่าว. แลกกับ write penalty เพราะการเขียนหนึ่งครั้งกระทบ parity สอง block; ตารางจัด N+2 ดิสก์.

**ประเด็นที่ต้องจำ**

- dual distributed parity หรือ P และ Q ในภาพ (หน้า 19, 26)
- parity สอง block กระทบเมื่อเขียน (หน้า 26)
- ตารางให้ N+2 disks (หน้า 17)
- คำอธิบายสามดิสก์เสียผูกกับช่วง MTTR ตามสไลด์ (หน้า 26)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAID 6
- dual parity
- P/Q
- MTTR
- N+2
- write penalty

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบ P(0–3) และ Q(0–3) ในภาพหน้า 19 ซึ่งอยู่คนละดิสก์

**จุดที่อาจสับสน:** อย่าตีความประโยคสามดิสก์เสียโดยละคำว่า within MTTR interval ในสไลด์

**ประโยคช่วยจำ:** หก = parity สองชุด

### 13. ตารางเปรียบเทียบ RAID และการเลือกอ่าน

**🟡 สำคัญ** · itds-211_comp_arch_Chapter06.pdf, **หน้า 17, 27–28**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก

ตาราง RAID เปรียบ data availability, large transfer, small request และตัวอย่างการใช้งานของแต่ละระดับ. ใช้อ่านเชิงเปรียบเทียบกับภาพหน้า 18–19: RAID 0 เน้น striping แต่ไม่มี redundancy, RAID 1 ทำ mirror, RAID 2–3 ทำงานแบบ parallel และ RAID 4–6 เป็น independent access. ตารางหน้า 27–28 เป็นการจัดกลุ่มและตัวอย่างของเอกสาร ไม่ใช่คำรับรองความเหมาะสมของระบบปัจจุบัน.

**ประเด็นที่ต้องจำ**

- จับคู่ level ↔ redundancy ↔ disks required จากหน้า 17
- แยก parallel access (2–3) กับ independent access (4–6)
- ตารางหน้า 27–28 มีตัวอย่าง application/use ในสไลด์

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- data availability
- large I/O data transfer capacity
- small I/O request rate
- parallel access
- independent access

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เมื่อเจอ workload ในตาราง ให้เริ่มจาก read/write/transfer pattern แล้วกลับไปดูคอลัมน์ระดับที่ตรง

**จุดที่อาจสับสน:** คอลัมน์ performance เป็นการเปรียบเทียบภายใต้เงื่อนไขของตาราง; ห้ามแปลงเป็นอันดับสากลโดยไม่ดูบริบท

**ประโยคช่วยจำ:** ดูวิธีสำรองก่อนดูความเร็ว

### 14. SSD เทียบ HDD ในสไลด์

**🟡 สำคัญ** · itds-211_comp_arch_Chapter06.pdf, **หน้า 29–30**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก

สไลด์ยกข้อดีของ SSD ต่อ HDD เช่น IOPS สูง เวลาเข้าถึง/latency ต่ำ เสียงและพลังงานต่ำ ตลอดจนความทนทานเชิงกล. ตารางหน้า 30 เทียบ NAND SSD กับ Seagate laptop HDD ด้วยรุ่น ความเร็ว กำลังไฟ ความจุ และราคาในช่วงที่จัดทำสไลด์. จึงใช้เพื่อฝึกอ่านเกณฑ์เปรียบเทียบ ไม่ใช้ราคาหรือสเปกนั้นแทนปัจจุบัน.

**ประเด็นที่ต้องจำ**

- SSD ไม่มีการรอหัว/จานแบบ HDD ตามภาพรวมข้อดีในหน้า 29
- เกณฑ์หน้า 30: performance, power, capacity, cost
- ตัวเลขและคำว่า current ในเอกสารเป็นข้อมูล ณ เวลาสไลด์

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SSD
- HDD
- NAND
- IOPS
- access time
- latency

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เลือกคอลัมน์หนึ่งในตารางหน้า 30 เช่น power แล้วเทียบเฉพาะรุ่นที่สไลด์ยก

**จุดที่อาจสับสน:** ข้อดีในสไลด์เป็นการเทียบตามบริบท ไม่ใช่คำรับรองว่า SSD ทุกรุ่นดีกว่า HDD ทุกด้านในปัจจุบัน

**ประโยคช่วยจำ:** SSD ดู latency และ IOPS; ตารางรุ่นให้อ่านเป็นตัวอย่าง

### 15. โครงสร้าง SSD

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 31**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

ภาพ SSD architecture ต่อ host system ซึ่งมี OS, file system และ I/O driver ผ่าน interface ไปยัง controller ของ SSD. ภายใน controller มี addressing, data buffer/cache และ error correction ก่อนเชื่อม flash memory components. ภาพนี้ช่วยแยกส่วนซอฟต์แวร์ฝั่ง host ออกจากส่วนควบคุมและสื่อ flash ฝั่ง SSD.

**ประเด็นที่ต้องจำ**

- host: OS/file system/I/O driver/interface
- SSD: interface/controller/addressing/buffer-cache/error correction/flash components
- controller เป็นจุดจัดการก่อนถึง flash

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- host system
- SSD interface
- controller
- addressing
- data buffer/cache
- error correction
- flash memory

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ภาพจาก I/O driver → host interface → SSD interface → controller → flash memory

**จุดที่อาจสับสน:** อย่าใส่ file system ไว้ใน SSD controller; ในภาพมันอยู่ฝั่ง host

**ประโยคช่วยจำ:** host สั่ง–controller จัด–flash เก็บ

### 16. ปัญหาการเขียนและอายุใช้งาน SSD

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 32**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

สไลด์อธิบายว่า performance ของ SSD มีแนวโน้มช้าลงเมื่อใช้งาน เพราะแก้ข้อมูลใน flash block ต้องอ่าน block เข้า RAM buffer ลบทั้ง block แล้วเขียนกลับ. Flash มีจำนวนรอบเขียนจำกัด จึงใช้ cache เพื่อรวม writes, wear leveling เพื่อกระจายการเขียน และ bad-block management. อุปกรณ์ยังประเมิน remaining lifetime เพื่อให้ระบบเตรียมรับความเสียหาย.

**ประเด็นที่ต้องจำ**

- read entire block → RAM buffer → erase entire block → write back (หน้า 32)
- write endurance จำกัด; cache/group writes ช่วยลดภาระ (หน้า 32)
- wear leveling กระจาย writes; bad-block management จัดการ block เสีย (หน้า 32)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- RAM buffer
- erase block
- write endurance
- wear leveling
- bad-block management
- remaining lifetime

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่ขั้นตอนแก้ block ตามลำดับลูกศรในข้อความหน้า 32 ก่อนจำเทคนิคยืดอายุ

**จุดที่อาจสับสน:** wear leveling คือกระจายการเขียน ไม่ใช่การทำสำเนาข้อมูลแบบ RAID 1

**ประโยคช่วยจำ:** อ่าน–ลบทั้ง block–เขียนกลับ; กระจายรอบเขียน

### 17. ตระกูล optical disk

**🟡 สำคัญ** · itds-211_comp_arch_Chapter06.pdf, **หน้า 33**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก

ตาราง optical memory แยก CD, DVD และ Blu-Ray พร้อมรุ่น read-only, recordable และ rewritable. แกนสำคัญคือสื่อผลิตข้อมูลมาแล้วอ่านอย่างเดียว, ผู้ใช้เขียนครั้งเดียว หรือเขียนซ้ำได้. ความจุในตารางเป็นค่าของรูปแบบที่สไลด์ยก ไม่ควรถือเป็นคำอธิบายครบทุก variant.

**ประเด็นที่ต้องจำ**

- CD-ROM/DVD-ROM เป็น read-only
- CD-R/DVD-R เป็น recordable; CD-RW/DVD-RW เป็น rewritable
- Blu-Ray ปรากฏในตารางเป็นตระกูล optical

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- CD-ROM
- CD-R
- CD-RW
- DVD-ROM
- DVD-R
- DVD-RW
- Blu-Ray

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จับคู่ suffix ROM/R/RW กับอ่านอย่างเดียว/บันทึกครั้งเดียว/เขียนซ้ำจากแถวตารางหน้า 33

**จุดที่อาจสับสน:** คำว่า recordable ไม่เท่ากับ rewritable; ตารางไม่ได้ครอบคลุมทุกมาตรฐานใหม่

**ประโยคช่วยจำ:** ROM อ่าน, R เขียนครั้ง, RW เขียนซ้ำ

### 18. CD-ROM: การผลิต การอ่าน และ block format

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 34–37**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

CD-ROM ทำจาก polycarbonate ที่สร้าง pits ตาม master แล้วเคลือบชั้นสะท้อนและป้องกัน; laser อ่านความต่างระหว่าง pit/land ตามภาพ. Block format หน้า 36 มี 2352 bytes: sync 12, ID 4, user data 2048 และ layered ECC 288. สไลด์ยกการทำสำเนาจำนวนมากและสื่อถอดเก็บเป็นข้อดี แต่ read-only และการเข้าถึงช้ากว่า magnetic disk เป็นข้อจำกัด.

**ประเด็นที่ต้องจำ**

- polycarbonate/pits/reflective layer/protective layer ในลำดับผลิต (หน้า 34–35)
- 12+4+2048+288 = 2352 bytes ต่อ block ในภาพ (หน้า 36)
- ROM อ่านอย่างเดียวและใช้แจกจ่ายปริมาณมาก (หน้า 37)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- polycarbonate
- pit
- land
- laser
- sync
- ID
- L-ECC
- CD-ROM

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** คำนวณ overhead ของ block หน้า 36: 2352−2048 = 304 bytes ซึ่งมาจาก sync 12 + ID 4 + ECC 288

**สูตรที่ต้องรู้**

```text
2352 = 12 (SYNC) + 4 (ID) + 2048 (Data) + 288 (L-ECC) bytes
```

block format ตามภาพ CD-ROM; overhead = 304 bytes

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 36

**จุดที่อาจสับสน:** 2352 bytes คือขนาด block รวม; user data คือ 2048 bytes ไม่ใช่ 2352

**ประโยคช่วยจำ:** 12–4–2048–288 รวม 2352

### 19. CD-R กับ CD-RW

**🟡 สำคัญ** · itds-211_comp_arch_Chapter06.pdf, **หน้า 38**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก

CD-R เป็นสื่อเขียนครั้งเดียวโดยใช้ dye layer ที่เปลี่ยนสภาพเมื่อบันทึก. CD-RW ใช้วัสดุ phase-change ระหว่าง amorphous/crystalline เพื่อให้ลบและเขียนซ้ำได้. สไลด์กล่าวถึงข้อจำกัดอายุการเขียนซ้ำของ CD-RW.

**ประเด็นที่ต้องจำ**

- CD-R: write once ด้วย dye layer
- CD-RW: phase-change และ rewritable
- amorphous/crystalline เป็นสองสภาพของวัสดุ CD-RW

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- CD-R
- CD-RW
- dye layer
- phase-change
- amorphous
- crystalline

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** แยกคำถามว่า media ใช้ dye หรือ phase-change ก่อนสรุปว่าบันทึกซ้ำได้หรือไม่

**จุดที่อาจสับสน:** CD-R บันทึกครั้งเดียว แม้จะอ่านหลายครั้ง; CD-RW จึงเป็นตัวที่เขียนซ้ำ

**ประโยคช่วยจำ:** R ใช้ dye; RW เปลี่ยน phase

### 20. DVD-ROM, Blu-Ray และความหนาแน่น optical

**🟡 สำคัญ** · itds-211_comp_arch_Chapter06.pdf, **หน้า 39–40**

เหตุผลการจัดระดับ: เป็นภาพเปรียบเทียบและการประยุกต์กลไกหลัก

ภาพเปรียบ CD-ROM ชั้นเดียวด้านเดียวกับ DVD-ROM แบบ double-sided, dual-layer ที่ laser โฟกัสชั้นข้อมูลต่างกันและต้องพลิกแผ่นเพื่ออ่านอีกด้าน. ตัวอย่างในภาพให้ 682 MB เทียบ 17 GB. ภาพ optical characteristics เทียบความยาวคลื่น CD 780 nm, DVD 650 nm และ Blu-ray 405 nm พร้อม track/pit spacing ต่างกัน.

**ประเด็นที่ต้องจำ**

- DVD-ROM ในภาพเป็น double-sided, dual-layer (หน้า 39)
- CD 780 nm, DVD 650 nm, Blu-ray 405 nm ตามภาพ (หน้า 40)
- 682 MB และ 17 GB เป็นตัวอย่างรูปแบบแผ่นในภาพหน้า 39

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- DVD-ROM
- double-sided
- dual-layer
- semireflective layer
- Blu-ray
- laser wavelength

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ดูหน้า 39 จากชั้นสะท้อนของแต่ละด้าน แล้วหน้า 40 เทียบ beam spot/pit/track ตาม wavelength

**จุดที่อาจสับสน:** 17 GB เป็นตัวอย่าง double-sided dual-layer ในภาพ ไม่ใช่ค่าของ DVD ทุกแผ่น

**ประโยคช่วยจำ:** CD 780 → DVD 650 → Blu-ray 405 nm

### 21. Magnetic tape: serial และ serpentine

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter06.pdf, **หน้า 41–42**

เหตุผลการจัดระดับ: เป็นคำจำกัดความ โครงสร้าง กลไก หรือกฎที่สไลด์ใช้ต่อยอด

Magnetic tape เคลือบวัสดุแม่เหล็กบนแถบ polyester และบันทึกข้อมูลตามแนวยาวเป็น tracks แบบ serial. Physical records หรือ blocks คั่นด้วย inter-record gaps. ภาพหน้า 42 แสดง serpentine ที่ทิศอ่าน/เขียนสลับเมื่อเปลี่ยน track และตัวอย่างระบบอ่าน/เขียน 4 tracks พร้อมกัน.

**ประเด็นที่ต้องจำ**

- polyester tape + magnetizable coating (หน้า 41)
- serial recording, parallel longitudinal tracks และ inter-record gaps (หน้า 41)
- serpentine สลับทิศระหว่าง tracks; ภาพล่างอ่าน/เขียน 4 tracks พร้อมกัน (หน้า 42)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- magnetic tape
- serial recording
- inter-record gap
- serpentine
- track
- physical record

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตามลูกศร Track 0 → Track 1 → Track 2 ในภาพบนหน้า 42; อีกภาพแสดง block 1–4 อยู่คนละ track ในคอลัมน์แรก

**จุดที่อาจสับสน:** parallel tracks ในเทปหมายถึง tracks หลายแนว; ลำดับเข้าถึงสื่อยังเป็น serial ตามหน้า 41

**ประโยคช่วยจำ:** เทปวิ่งยาว–จบแถวกลับทิศ

### 22. ตาราง LTO เป็นตัวอย่างในสไลด์

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter06.pdf, **หน้า 43**

เหตุผลการจัดระดับ: เป็นตารางรุ่นหรือรายละเอียดตัวอย่างตามช่วงเวลาของสไลด์

ตารางหน้า 43 เปรียบเทียบ LTO generations 1–8 ด้วย capacity และ transfer rate ของแต่ละรุ่น. ใช้ฝึกอ่านแนวโน้มภายในตารางและศัพท์ของเทปเท่านั้น. บางแถวมีค่าอนาคตหรือ TBA จากช่วงเวลาที่ทำสไลด์ จึงต้องตรวจสอบจากต้นฉบับก่อนนำไปอ้างเป็นสเปกปัจจุบัน.

**ประเด็นที่ต้องจำ**

- LTO เป็นตาราง generations 1–8 ในเอกสาร
- หัวตารางเทียบ capacity/transfer rate
- ค่า TBA และแถวอนาคตไม่ใช่ข้อมูลยืนยันปัจจุบัน

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- LTO
- generation
- native capacity
- transfer rate
- TBA

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** อ่านจากหัวแถว generation ไปยังค่าความจุและอัตราโอนของรุ่นเดียวกัน โดยระบุว่าเป็นค่าตามสไลด์

**จุดที่อาจสับสน:** อย่าคัดตัวเลขในตารางไปใช้เป็น specification ปัจจุบันโดยไม่มีแหล่งใหม่; งานนี้จำกัดเฉพาะสไลด์

**ประโยคช่วยจำ:** LTO ตารางรุ่น = ตัวอย่าง ไม่ใช่ราคาหรือสเปกวันนี้

## 3. Roadmap ทบทวน

1. **1 · Magnetic disk** — เริ่มสื่อ/หัวอ่าน → track/sector/cylinder → seek/rotation/transfer (itds-211_comp_arch_Chapter06.pdf, หน้า 4–15)
2. **2 · RAID ภาพรวม** — จำ N, striping, redundancy และตาราง RAID 0–6 พร้อมข้อขัดกันหน้า 16–17 (itds-211_comp_arch_Chapter06.pdf, หน้า 16–19)
3. **3 · RAID ทีละระดับ** — ไล่ 0/1 แล้ว 2/3 แบบ parallel ต่อด้วย 4/5/6 แบบ independent (itds-211_comp_arch_Chapter06.pdf, หน้า 18–28)
4. **4 · SSD** — เทียบ HDD, วาด controller→flash แล้วอธิบาย erase/write และ wear leveling (itds-211_comp_arch_Chapter06.pdf, หน้า 29–32)
5. **5 · Optical และ tape** — อ่าน ROM/R/RW, CD-ROM block, DVD/Blu-ray แล้วจบด้วย serial/serpentine tape (itds-211_comp_arch_Chapter06.pdf, หน้า 33–43)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · แผนที่สื่อและ layout

ดูภาพหน้า 4–13; วาด platter/track/sector/cylinder และแยกชนิดหัว

**เกณฑ์ผ่าน:** ระบุส่วนของ disk และอ่าน sector ST506 ได้โดยไม่สับสน data/overhead

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 4–13

### รอบ 2 · เวลาและ RAID

คำนวณ access time หน้า 15 แล้วทำตาราง RAID 0–6 จากความจำก่อนเปิดหน้า 17–28

**เกณฑ์ผ่าน:** จำ seek+rotation, redundancy และจำนวนดิสก์แต่ละระดับได้

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 14–28

### รอบ 3 · SSD

ตามภาพ controller และเขียนลำดับ read–erase–write พร้อม wear leveling

**เกณฑ์ผ่าน:** อธิบายปัญหา block erase และวิธีรับมือจากหน้า 32 ได้

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 29–32

### รอบ 4 · Optical/tape

ทวน ROM/R/RW, คิด 2352-byte block, เทียบ laser wavelengths และตาม serpentine

**เกณฑ์ผ่าน:** แยก write-once/rewritable และบอก 12+4+2048+288 ได้

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 33–43

### รอบ 5 · เว้นระยะและสุ่ม Quiz

ตอบ 3 ข้อต่อหัวข้อ; ทวนข้อที่ผิดจากภาพต้นฉบับในวันถัดไป

**เกณฑ์ผ่าน:** ตอบหัวข้อแดงครบและชี้ตารางเก่าหรือข้อขัดกันที่ต้องตรวจสอบได้

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 4–43

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1 disk หน้า 4–15; วัน 2 RAID หน้า 16–28; วัน 3 SSD/optical/tape หน้า 29–43 และทำ Quiz
- **ถ้าเหลือ 1 วัน:** disk timing หน้า 14–15 → RAID table/levels หน้า 17–26 → SSD หน้า 31–32 → CD block/optical/tape หน้า 33–42
- **ถ้าเหลือ 3 ชั่วโมง:** 0–35 นาที layout/timing หน้า 7–15; 35–105 นาที RAID หน้า 16–26; 105–135 นาที SSD หน้า 29–32; 135–165 นาที optical/tape หน้า 33–42; 165–180 นาทีสุ่ม Quiz

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

เน้นหัวข้อที่สไลด์ให้นิยาม กลไก ภาพและตารางซ้ำ เช่น disk timing, RAID 0–6, SSD block write และ CD-ROM block; ไม่มีข้อสอบเก่าจึงไม่ยืนยันโอกาสออกจริง

- **ควรท่องจำ:** track/sector/cylinder, access time, RAID 0–6 กับ N/2N/N+m/N+1/N+2, ROM/R/RW, CD-ROM block และศัพท์ tape (หน้า 7–9, 15–17, 33–42)
- **ควรฝึกโจทย์:** บวก seek+rotational delay; คิด sector overhead 600−512; คิด CD block 2352−2048; นับ disk RAID และ read/write RAID 4 (หน้า 9, 15, 17, 25, 36)
- **ควรเข้าใจแนวคิด:** RAID parity/mirror, เหตุ RAID 5 ลดคอขวด RAID 4, SSD erase/write/wear leveling และ optical/tape access (หน้า 16–32, 34–42)
- **เตรียมข้อสอบแบบผสม:** เลือกตอบจับคู่คำศัพท์/level; อัตนัยอธิบายกลไก; คำนวณเฉพาะสูตร/ตัวเลขในสไลด์; วิเคราะห์ภาพ mapping, RAID parity, SSD controller และ tape (หน้า 7–42)

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 22 ข้อ, อัตนัย 22 ข้อ, วิเคราะห์ 19 ข้อ, คำนวณ 3 ข้อ

### สื่อแม่เหล็กและหัวอ่าน/เขียน

**ข้อ 1 · เลือกตอบ: ตัวใดเป็นวัสดุฐาน platter ที่สไลด์กล่าวถึง?**

- A. อะลูมิเนียมและแก้ว
- B. กระดาษและไม้
- C. ซิลิกอนล้วน
- D. เทปโพลีเอสเตอร์

เฉลย: อะลูมิเนียมและแก้ว

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 4–6

**ข้อ 2 · อัตนัย: หัวเขียนและหัวอ่านในภาพหน้า 6 ใช้หลักใด?**

เฉลย: หัวเขียน inductive; หัวอ่าน magnetoresistive

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 4–6

**ข้อ 3 · วิเคราะห์: เหตุใดสไลด์กล่าวถึงฐานแก้ว?**

เฉลย: ผิวสม่ำเสมอ defect น้อย เอื้อ fly height ต่ำ เพิ่มความแข็งและทนแรงกระแทก

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 4–6

### Track, sector, cylinder และรูปแบบ sector

**ข้อ 4 · เลือกตอบ: หน่วยใดคือ track ที่รัศมีเดียวกันบนหลายผิว?**

- A. Cylinder
- B. Sector
- C. Gap
- D. Spindle

เฉลย: Cylinder

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 7–9

**ข้อ 5 · อัตนัย: Multiple zone recording ต่างจากการแบ่ง sector แบบเดิมอย่างไร?**

เฉลย: แบ่งเป็น zones เพื่อให้จำนวน sectors ต่อ track ต่างกันตามตำแหน่ง

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 7–9

**ข้อ 6 · คำนวณ: คำนวณ overhead ใน sector ตัวอย่าง 600 bytes ที่มี data 512 bytes**

เฉลย: 600−512 = 88 bytes สำหรับ field/gap/ข้อมูลควบคุมตามภาพ

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 7–9

### ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง

**ข้อ 7 · เลือกตอบ: แบบใดต้องเคลื่อนหัวไปยัง track?**

- A. Movable-head
- B. Fixed-head
- C. Removable media
- D. Double-sided

เฉลย: Movable-head

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 10–13

**ข้อ 8 · อัตนัย: เหตุใด Winchester จึงใช้ enclosure ปิด?**

เฉลย: ลดสิ่งปนเปื้อนเพื่อให้หัวลอยใกล้ผิวได้ตามสไลด์

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 10–13

**ข้อ 9 · วิเคราะห์: เมื่อหัวแคบลง ข้อดีและความเสี่ยงที่สไลด์กล่าวคืออะไร?**

เฉลย: ความหนาแน่นเพิ่ม แต่ต้องอยู่ใกล้จานมากขึ้นและเสี่ยงข้อผิดพลาด

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 10–13

### เวลา I/O ของ magnetic disk

**ข้อ 10 · เลือกตอบ: Access time ตามสไลด์ประกอบด้วยอะไร?**

- A. Seek + rotational delay
- B. Seek + transfer
- C. Channel wait + transfer
- D. Transfer เท่านั้น

เฉลย: Seek + rotational delay

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 14–15

**ข้อ 11 · อัตนัย: ลำดับ seek, rotational delay และ transfer เป็นอย่างไร?**

เฉลย: วางหัวที่ track → รอ sector หมุนมาถึง → อ่าน/เขียนข้อมูล

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 14–15

**ข้อ 12 · คำนวณ: จงเขียนวิธีคำนวณ access time จาก seek time และ rotational delay**

เฉลย: นำ seek time บวก rotational delay; ไม่รวม transfer time ตามนิยามหน้า 15

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 14–15

### RAID: ภาพรวมและจำนวนดิสก์

**ข้อ 13 · เลือกตอบ: RAID ระดับใด nonredundant ตามตาราง?**

- A. 0
- B. 1
- C. 5
- D. 6

เฉลย: 0

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 16–19

**ข้อ 14 · อัตนัย: N และ m ในตาราง RAID หมายถึงอะไร?**

เฉลย: N = จำนวน data disks; m = จำนวน redundant disks ของ RAID 2 ที่แปรตาม log N

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 16–19

**ข้อ 15 · วิเคราะห์: ตารางต้องใช้กี่ดิสก์สำหรับ RAID 6 เมื่อ N=4?**

เฉลย: N+2 = 6 ดิสก์ ตามตารางหน้า 17

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 16–19

### RAID 0: striping ไม่มี redundancy

**ข้อ 16 · เลือกตอบ: RAID 0 เก็บข้อมูลสำรองแบบใด?**

- A. ไม่มี
- B. mirror
- C. parity แยก
- D. dual parity

เฉลย: ไม่มี

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 20–21

**ข้อ 17 · อัตนัย: เงื่อนไขสองข้อของ high transfer capacity หน้า 21 คืออะไร?**

เฉลย: ทางเดิน host–disk ต้องรองรับสูง และ application ออก request ที่ใช้อาร์เรย์ได้มีประสิทธิภาพ

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 20–21

**ข้อ 18 · วิเคราะห์: เหตุใด small I/O request จึงไม่ใช่การถ่ายข้อมูลอย่างเดียว?**

เฉลย: เวลามักถูก seek และ rotational latency ครอบงำตามหน้า 21

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 20–21

### RAID 1: mirroring

**ข้อ 19 · เลือกตอบ: RAID 1 ได้ redundancy โดยอะไร?**

- A. Mirroring
- B. Hamming
- C. single parity
- D. dual parity

เฉลย: Mirroring

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 22

**ข้อ 20 · อัตนัย: เหตุใดอ่านข้อมูลได้เมื่อดิสก์ตัวหนึ่งเสีย?**

เฉลย: มี mirror disk ที่เก็บข้อมูลเดียวกัน

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 22

**ข้อ 21 · วิเคราะห์: ถ้า N=4 data disks ตารางหน้า 17 ให้ RAID 1 ใช้ทั้งหมดกี่ดิสก์?**

เฉลย: 2N = 8 ดิสก์

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 22

### RAID 2: Hamming code

**ข้อ 22 · เลือกตอบ: RAID 2 ใช้รหัสใดตามสไลด์?**

- A. Hamming
- B. CRC อย่างเดียว
- C. AES
- D. NTFS

เฉลย: Hamming

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 23

**ข้อ 23 · อัตนัย: parallel access ใน RAID 2 หมายถึงอะไร?**

เฉลย: member disks ร่วมทำทุก I/O request และ spindle synchronized

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 23

**ข้อ 24 · วิเคราะห์: RAID 2 ต่าง RAID 3 ใน redundancy อย่างไร?**

เฉลย: RAID 2 ใช้ Hamming code บนหลายดิสก์; RAID 3 ใช้ parity disk เดียว

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 18, 23

### RAID 3: bit-interleaved parity

**ข้อ 25 · เลือกตอบ: RAID 3 ใช้ redundant disks กี่ตัว?**

- A. หนึ่ง
- B. สอง
- C. N
- D. ไม่มี

เฉลย: หนึ่ง

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 24

**ข้อ 26 · อัตนัย: reduced mode หน้า 24 คืออะไร?**

เฉลย: ยังเข้าถึงข้อมูลได้หลังดิสก์เสียโดย reconstruct จาก parity และดิสก์ที่เหลือ

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 24

**ข้อ 27 · วิเคราะห์: เหตุใด transaction-oriented workload จึงเป็นข้อเสียของ RAID 3 ตามสไลด์?**

เฉลย: สไลด์ระบุ performance suffers สำหรับ workload นี้ ขณะที่ทุกดิสก์ร่วมกันต่อ I/O request

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 24

### RAID 4: block parity แยกดิสก์

**ข้อ 28 · เลือกตอบ: small strip write ของ RAID 4 มี I/O กี่ครั้งตามสไลด์?**

- A. 2 reads + 2 writes
- B. 1 read + 1 write
- C. 4 reads
- D. ไม่มี parity I/O

เฉลย: 2 reads + 2 writes

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 25

**ข้อ 29 · อัตนัย: เหตุใด dedicated parity disk อาจเป็นคอขวด?**

เฉลย: ทุกการปรับ parity ต้องเข้าไปยังดิสก์เดียว

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 25

**ข้อ 30 · วิเคราะห์: ถ้าเขียนหนึ่ง strip เล็ก จงนับ read/write ตามหน้า 25**

เฉลย: อ่าน old user+old parity = 2; เขียน new user+new parity = 2

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 25

### RAID 5: distributed parity

**ข้อ 31 · เลือกตอบ: RAID 5 แก้ bottleneck RAID 4 ด้วยอะไร?**

- A. กระจาย parity
- B. เพิ่ม dedicated parity disk
- C. เอา parity ออก
- D. เปลี่ยนเป็น tape

เฉลย: กระจาย parity

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26

**ข้อ 32 · อัตนัย: RAID 5 กับ RAID 4 ต่างกันตรงตำแหน่ง parity อย่างไร?**

เฉลย: RAID 4 ใช้ดิสก์ parity เฉพาะ; RAID 5 กระจาย parity strips

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26

**ข้อ 33 · วิเคราะห์: เมื่อ N=4 ตารางหน้า 17 ให้ RAID 5 รวมกี่ดิสก์?**

เฉลย: N+1 = 5 ดิสก์

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26

### RAID 6: dual distributed parity

**ข้อ 34 · เลือกตอบ: RAID 6 เก็บ parity กี่ชุด?**

- A. สอง
- B. หนึ่ง
- C. ไม่มี
- D. N ชุด

เฉลย: สอง

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26

**ข้อ 35 · อัตนัย: เหตุใดสไลด์ระบุ write penalty ของ RAID 6?**

เฉลย: การเขียนหนึ่งครั้งกระทบ parity สอง blocks

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26

**ข้อ 36 · วิเคราะห์: ถ้า N=4 RAID 6 ใช้กี่ดิสก์ตามตาราง?**

เฉลย: N+2 = 6 ดิสก์

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 19, 26

### ตารางเปรียบเทียบ RAID และการเลือกอ่าน

**ข้อ 37 · เลือกตอบ: RAID 4–6 อยู่หมวด access ใดในตาราง?**

- A. Independent
- B. Parallel
- C. Serial tape
- D. Optical

เฉลย: Independent

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 17, 27–28

**ข้อ 38 · อัตนัย: สามเกณฑ์เปรียบเทียบหลักในหน้า 17 คืออะไร?**

เฉลย: data availability, large I/O data transfer capacity และ small I/O request rate

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 17, 27–28

**ข้อ 39 · วิเคราะห์: เหตุใดจึงไม่ควรใช้ตารางหน้า 27–28 เป็นคำแนะนำซื้ออุปกรณ์ปัจจุบัน?**

เฉลย: เป็นตัวอย่างและการเปรียบเทียบตามสไลด์ ไม่ระบุข้อมูลสเปกหรือราคา ณ ปัจจุบัน

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 17, 27–28

### SSD เทียบ HDD ในสไลด์

**ข้อ 40 · เลือกตอบ: ตัวชี้วัดใดอยู่ในข้อดี SSD หน้า 29?**

- A. IOPS
- B. seek arm length
- C. tape speed
- D. optical pit depth

เฉลย: IOPS

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 29–30

**ข้อ 41 · อัตนัย: ตารางหน้า 30 ใช้เปรียบเทียบอะไร?**

เฉลย: NAND SSD กับ laptop HDD ตัวอย่างตาม performance, power, capacity, cost

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 29–30

**ข้อ 42 · วิเคราะห์: เหตุใดไม่ควรจดจำราคาหน้า 30 เป็นราคาปัจจุบัน?**

เฉลย: เป็นตารางรุ่นในสไลด์ ไม่ใช่ข้อมูลราคาปัจจุบัน

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 29–30

### โครงสร้าง SSD

**ข้อ 43 · เลือกตอบ: ส่วนใดอยู่ฝั่ง host ในภาพ?**

- A. File system software
- B. Flash memory components
- C. SSD controller
- D. Error correction block

เฉลย: File system software

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 31

**ข้อ 44 · อัตนัย: SSD controller ในภาพเชื่อมกับฟังก์ชันใด?**

เฉลย: addressing, data buffer/cache, error correction และ flash components

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 31

**ข้อ 45 · วิเคราะห์: ตามภาพข้อมูลจาก host ไป flash ผ่านส่วนใดบ้าง?**

เฉลย: interfaces → controller/addressing/buffer-cache/error correction → flash components

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 31

### ปัญหาการเขียนและอายุใช้งาน SSD

**ข้อ 46 · เลือกตอบ: วิธีใดกระจายจำนวนครั้งเขียนระหว่าง blocks?**

- A. Wear leveling
- B. Mirroring
- C. Seek
- D. Inter-record gap

เฉลย: Wear leveling

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 32

**ข้อ 47 · อัตนัย: เหตุใดการแก้ข้อมูลใน flash block จึงต้องใช้ buffer ตามสไลด์?**

เฉลย: ต้องอ่านทั้ง block เข้า RAM ก่อนลบทั้ง block และเขียนกลับ

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 32

**ข้อ 48 · วิเคราะห์: cache หน้า 32 ช่วยเรื่องอายุอย่างไร?**

เฉลย: หน่วงและรวม write operations เพื่อลดการเขียนลง flash

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 32

### ตระกูล optical disk

**ข้อ 49 · เลือกตอบ: suffix ใดหมายถึงเขียนซ้ำในรายการสไลด์?**

- A. RW
- B. ROM
- C. R
- D. ECC

เฉลย: RW

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 33

**ข้อ 50 · อัตนัย: ตารางหน้า 33 แยก optical memory เป็นตระกูลใด?**

เฉลย: CD, DVD และ Blu-Ray

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 33

**ข้อ 51 · วิเคราะห์: CD-R ต่าง CD-RW อย่างไรตามรายการ?**

เฉลย: CD-R บันทึกครั้งเดียว; CD-RW เขียนซ้ำได้

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 33

### CD-ROM: การผลิต การอ่าน และ block format

**ข้อ 52 · เลือกตอบ: user data ใน CD-ROM block หน้า 36 มีกี่ bytes?**

- A. 2048
- B. 2352
- C. 288
- D. 12

เฉลย: 2048

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 34–37

**ข้อ 53 · อัตนัย: ชั้นหลักของแผ่น CD-ROM และหน้าที่ laser ในภาพคืออะไร?**

เฉลย: polycarbonate มี pits, ชั้นสะท้อนและป้องกัน; laser อ่านรูปแบบ pit/land

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 34–37

**ข้อ 54 · คำนวณ: คำนวณ overhead เมื่อ block 2352 bytes มี data 2048 bytes**

เฉลย: 2352−2048 = 304 bytes = sync 12 + ID 4 + ECC 288

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 34–37

### CD-R กับ CD-RW

**ข้อ 55 · เลือกตอบ: ชนิดใดใช้ phase-change ตามสไลด์?**

- A. CD-RW
- B. CD-R
- C. CD-ROM
- D. magnetic tape

เฉลย: CD-RW

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 38

**ข้อ 56 · อัตนัย: CD-R กับ CD-RW ต่างกันอย่างไร?**

เฉลย: CD-R เขียนครั้งเดียวด้วย dye; CD-RW เปลี่ยนสภาพ amorphous/crystalline เพื่อเขียนซ้ำ

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 38

**ข้อ 57 · วิเคราะห์: เหตุใดจึงไม่ควรเรียก CD-R ว่า rewritable?**

เฉลย: สไลด์จัด CD-R เป็น write once; กลไกเขียนซ้ำอยู่ใน CD-RW

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 38

### DVD-ROM, Blu-Ray และความหนาแน่น optical

**ข้อ 58 · เลือกตอบ: แสงของ Blu-ray ในภาพหน้า 40 ยาวคลื่นเท่าไร?**

- A. 405 nm
- B. 650 nm
- C. 780 nm
- D. 1.2 mm

เฉลย: 405 nm

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 39–40

**ข้อ 59 · อัตนัย: ภาพ DVD-ROM หน้า 39 เพิ่มชั้น/ด้านอย่างไร?**

เฉลย: double-sided และ dual-layer มีชั้นสะท้อน/กึ่งสะท้อนให้ laser โฟกัสต่างชั้น

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 39–40

**ข้อ 60 · วิเคราะห์: เรียง wavelength จากยาวไปสั้นตามหน้า 40**

เฉลย: CD 780 nm → DVD 650 nm → Blu-ray 405 nm

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 39–40

### Magnetic tape: serial และ serpentine

**ข้อ 61 · เลือกตอบ: สิ่งใดคั่น physical records บนเทป?**

- A. Inter-record gaps
- B. Sector ID
- C. Parity disk
- D. ECC controller

เฉลย: Inter-record gaps

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 41–42

**ข้อ 62 · อัตนัย: serpentine ในภาพหมายถึงอะไร?**

เฉลย: เมื่อเปลี่ยน track ทิศอ่าน/เขียนกลับด้านไปมา

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 41–42

**ข้อ 63 · วิเคราะห์: ภาพหน้า 42 ตัวอย่างอ่าน/เขียนพร้อมกันกี่ tracks?**

เฉลย: 4 tracks

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 41–42

### ตาราง LTO เป็นตัวอย่างในสไลด์

**ข้อ 64 · เลือกตอบ: ตารางหน้า 43 ว่าด้วยอะไร?**

- A. LTO generations
- B. RAID levels
- C. CD block
- D. SSD controller

เฉลย: LTO generations

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 43

**ข้อ 65 · อัตนัย: ตาราง LTO มีวัตถุประสงค์ทบทวนอย่างไร?**

เฉลย: เทียบรุ่นและอ่านเกณฑ์ capacity/transfer rate ตามเอกสาร

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 43

**ข้อ 66 · วิเคราะห์: เหตุใดค่าที่ระบุ TBA ในตารางจึงใช้ตอบสเปกปัจจุบันไม่ได้?**

เฉลย: สไลด์ไม่ได้ยืนยันค่าและอยู่ในบริบทเวลาเดิม; ต้องตรวจสอบจากต้นฉบับ

อ้างอิง: itds-211_comp_arch_Chapter06.pdf, หน้า 43

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- Magnetic Disk · หน้า 4: ภาพสไลด์เรื่อง สื่อแม่เหล็กและหัวอ่าน/เขียน สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 4) (itds-211_comp_arch_Chapter06.pdf, หน้า 4)
- Read / Write Process · หน้า 5: ภาพสไลด์เรื่อง สื่อแม่เหล็กและหัวอ่าน/เขียน สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 5) (itds-211_comp_arch_Chapter06.pdf, หน้า 5)
- Track width · หน้า 6: ภาพสไลด์เรื่อง สื่อแม่เหล็กและหัวอ่าน/เขียน สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 6) (itds-211_comp_arch_Chapter06.pdf, หน้า 6)
- Figure 6.2  Disk Data Layout · หน้า 7: ผัง track, sector, cylinder, platter, head และ gaps (itds-211_comp_arch_Chapter06.pdf, หน้า 7) (itds-211_comp_arch_Chapter06.pdf, หน้า 7)
- (a) Constant angular velocity (b) Multiple zone recording · หน้า 8: ภาพสไลด์เรื่อง Track, sector, cylinder และรูปแบบ sector สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 8) (itds-211_comp_arch_Chapter06.pdf, หน้า 8)
- 17 7 41 515 20 17 7 41 515 20 · หน้า 9: Winchester ST506: ส่วนประกอบ sector ตัวอย่าง 600 bytes (itds-211_comp_arch_Chapter06.pdf, หน้า 9) (itds-211_comp_arch_Chapter06.pdf, หน้า 9)
- Table 6.1 · หน้า 10: ภาพสไลด์เรื่อง ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 10) (itds-211_comp_arch_Chapter06.pdf, หน้า 10)
- Characteristics · หน้า 11: ภาพสไลด์เรื่อง ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 11) (itds-211_comp_arch_Chapter06.pdf, หน้า 11)
- Classification · หน้า 12: ภาพสไลด์เรื่อง ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 12) (itds-211_comp_arch_Chapter06.pdf, หน้า 12)
- Table 6.2 · หน้า 13: ภาพสไลด์เรื่อง ชนิดดิสก์ หัวอ่าน และตารางพารามิเตอร์ตัวอย่าง สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 13) (itds-211_comp_arch_Chapter06.pdf, หน้า 13)
- Wait for · หน้า 14: ลำดับเวลา disk I/O: device/channel wait, seek, rotational delay, transfer (itds-211_comp_arch_Chapter06.pdf, หน้า 14) (itds-211_comp_arch_Chapter06.pdf, หน้า 14)
- Disk Performance Parameters · หน้า 15: ภาพสไลด์เรื่อง เวลา I/O ของ magnetic disk สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 15) (itds-211_comp_arch_Chapter06.pdf, หน้า 15)
- n Consists of 7 levels · หน้า 16: ภาพสไลด์เรื่อง RAID: ภาพรวมและจำนวนดิสก์ สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 16) (itds-211_comp_arch_Chapter06.pdf, หน้า 16)
- N= number of data disks;    mproportional to log N · หน้า 17: ตาราง RAID 0–6: redundancy, จำนวนดิสก์ และ performance (itds-211_comp_arch_Chapter06.pdf, หน้า 17) (itds-211_comp_arch_Chapter06.pdf, หน้า 17)
- strip 12 · หน้า 18: ภาพกระจายข้อมูล RAID 0, mirror RAID 1 และ Hamming RAID 2 (itds-211_comp_arch_Chapter06.pdf, หน้า 18) (itds-211_comp_arch_Chapter06.pdf, หน้า 18)
- block 12 · หน้า 19: ภาพ parity ของ RAID 3–6 รวม P/Q ของ RAID 6 (itds-211_comp_arch_Chapter06.pdf, หน้า 19) (itds-211_comp_arch_Chapter06.pdf, หน้า 19)
- strip 4 · หน้า 20: logical-to-physical strip mapping ของ RAID 0 (itds-211_comp_arch_Chapter06.pdf, หน้า 20) (itds-211_comp_arch_Chapter06.pdf, หน้า 20)
- Level 0 · หน้า 21: ภาพสไลด์เรื่อง RAID 0: striping ไม่มี redundancy สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 21) (itds-211_comp_arch_Chapter06.pdf, หน้า 21)
- Level 1 · หน้า 22: ภาพสไลด์เรื่อง RAID 1: mirroring สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 22) (itds-211_comp_arch_Chapter06.pdf, หน้า 22)
- Level 2 · หน้า 23: ภาพสไลด์เรื่อง RAID 2: Hamming code สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 23) (itds-211_comp_arch_Chapter06.pdf, หน้า 23)
- Level 3 · หน้า 24: ภาพสไลด์เรื่อง RAID 3: bit-interleaved parity สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 24) (itds-211_comp_arch_Chapter06.pdf, หน้า 24)
- Level 4 · หน้า 25: ภาพสไลด์เรื่อง RAID 4: block parity แยกดิสก์ สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 25) (itds-211_comp_arch_Chapter06.pdf, หน้า 25)
- Level 5 · หน้า 26: ภาพสไลด์เรื่อง RAID 5: distributed parity สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 26) (itds-211_comp_arch_Chapter06.pdf, หน้า 26)
- Table 6.4 · หน้า 27: ตารางเปรียบ RAID ตามสไลด์ (itds-211_comp_arch_Chapter06.pdf, หน้า 27) (itds-211_comp_arch_Chapter06.pdf, หน้า 27)
- Table 6.4 · หน้า 28: ตารางเปรียบ RAID และตัวอย่างงานตามสไลด์ (itds-211_comp_arch_Chapter06.pdf, หน้า 28) (itds-211_comp_arch_Chapter06.pdf, หน้า 28)
- SSD Compared to HDD · หน้า 29: ภาพสไลด์เรื่อง SSD เทียบ HDD ในสไลด์ สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 29) (itds-211_comp_arch_Chapter06.pdf, หน้า 29)
- NAND Flash Drives  Seagate Laptop Internal · หน้า 30: ตาราง SSD/HDD รุ่นตัวอย่างในช่วงเวลาของสไลด์ (itds-211_comp_arch_Chapter06.pdf, หน้า 30) (itds-211_comp_arch_Chapter06.pdf, หน้า 30)
- Figure 6.8  Solid State Drive Architecture · หน้า 31: แผนผัง host, SSD controller และ flash components (itds-211_comp_arch_Chapter06.pdf, หน้า 31) (itds-211_comp_arch_Chapter06.pdf, หน้า 31)
- Practical Issues · หน้า 32: ปัญหา write/erase ของ SSD และ wear leveling (itds-211_comp_arch_Chapter06.pdf, หน้า 32) (itds-211_comp_arch_Chapter06.pdf, หน้า 32)
- Table 6. 6 · หน้า 33: ตารางชนิด optical disk และรูปแบบ ROM/R/RW (itds-211_comp_arch_Chapter06.pdf, หน้า 33) (itds-211_comp_arch_Chapter06.pdf, หน้า 33)
- Compact Disk Read · หน้า 34: ภาพสไลด์เรื่อง CD-ROM: การผลิต การอ่าน และ block format สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 34) (itds-211_comp_arch_Chapter06.pdf, หน้า 34)
- Polycarbonate · หน้า 35: ภาพสไลด์เรื่อง CD-ROM: การผลิต การอ่าน และ block format สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 35) (itds-211_comp_arch_Chapter06.pdf, หน้า 35)
- 00 00 Data · หน้า 36: CD-ROM block 2352 bytes และส่วนประกอบ (itds-211_comp_arch_Chapter06.pdf, หน้า 36) (itds-211_comp_arch_Chapter06.pdf, หน้า 36)
- ROM is appropriate for the distribution of large · หน้า 37: ภาพสไลด์เรื่อง CD-ROM: การผลิต การอ่าน และ block format สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 37) (itds-211_comp_arch_Chapter06.pdf, หน้า 37)
- CD Recordable · หน้า 38: ภาพสไลด์เรื่อง CD-R กับ CD-RW สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 38) (itds-211_comp_arch_Chapter06.pdf, หน้า 38)
- 1.2 mm · หน้า 39: ชั้น CD-ROM เทียบ DVD-ROM แบบ double-sided, dual-layer (itds-211_comp_arch_Chapter06.pdf, หน้า 39) (itds-211_comp_arch_Chapter06.pdf, หน้า 39)
- Beam spot Land · หน้า 40: ความยาวคลื่นและ pit/track ของ CD, DVD, Blu-ray (itds-211_comp_arch_Chapter06.pdf, หน้า 40) (itds-211_comp_arch_Chapter06.pdf, หน้า 40)
- Magnetic Tape · หน้า 41: ภาพสไลด์เรื่อง Magnetic tape: serial และ serpentine สำหรับทบทวนตำแหน่งและรายละเอียด (itds-211_comp_arch_Chapter06.pdf, หน้า 41) (itds-211_comp_arch_Chapter06.pdf, หน้า 41)
- Bottom · หน้า 42: serpentine tape tracks และตัวอย่างอ่าน/เขียน 4 tracks (itds-211_comp_arch_Chapter06.pdf, หน้า 42) (itds-211_comp_arch_Chapter06.pdf, หน้า 42)
- Table 6.7 · หน้า 43: ตาราง LTO generations เป็นตัวอย่างตามสไลด์ (itds-211_comp_arch_Chapter06.pdf, หน้า 43) (itds-211_comp_arch_Chapter06.pdf, หน้า 43)
