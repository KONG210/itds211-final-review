# Chapter08 · Parallel Processors from Client to Cloud

ITDS-211 · Computer Architecture & Operating System · W. Suntiamorntut, Ph.D.

แหล่งข้อมูลของบท: **itds-211_comp_arch_Chapter08.pdf** จำนวน 41 หน้า อ่านและตรวจภาพครบทุกหน้า

ขอบเขตงาน: Chapter08 ทั้งหมด · รูปแบบฝึก: เลือกตอบ/อัตนัย/วิเคราะห์/คำนวณ · เวลาทบทวน: ไม่จำกัด

## 1. ภาพรวมเนื้อหาและระดับความสำคัญ

1 บท · 29 หัวข้อ · 🔴 ต้องจำแน่นอน 15 หัวข้อ (51.7%) · 🟡 สำคัญ 11 หัวข้อ (37.9%) · ⚪ อ่านเสริม 3 หัวข้อ (10.3%) · แบบฝึก 87 ข้อ · Flashcard 48 ใบ

**ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่าน Chapter08 ไม่ยืนยันความถี่หรือโอกาสออก Final**

| หัวข้อ | ระดับ | ตำแหน่งในต้นฉบับ |
| --- | --- | --- |
| Taxonomy ของ parallel processor architectures | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 3 |
| Introduction: เป้าหมายของ multiprocessors | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 4–5 |
| Hardware และ software: serial/parallel, sequential/concurrent | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 6–7 |
| ความยากของการเขียน parallel program | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 8 |
| Instruction/data streams และ SPMD | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 9 |
| Vector processors และ vector extension ของ RISC-V | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 10 |
| ตัวอย่าง DAXPY: scalar loop เทียบ vector code | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 11 |
| Vector vs. scalar | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 12 |
| SIMD | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 13 |
| Vector vs. multimedia extensions | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 14 |
| Hardware multithreading: fine-grain และ coarse-grain | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 15 |
| Simultaneous multithreading (SMT) และตัวอย่าง | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 16–17 |
| Future of multithreading | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter08.pdf, หน้า 18 |
| Shared memory multiprocessor (SMP), UMA และ NUMA | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 19 |
| ตัวอย่าง sum reduction บน 64-processor UMA | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 20–21 |
| ประวัติ GPU และกราฟิกในระบบ | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter08.pdf, หน้า 22–23 |
| GPU architectures | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 24 |
| ตัวอย่าง NVIDIA Fermi | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 25–26 |
| GPU memory structures | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 27 |
| Classifying GPUs | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 28 |
| Putting GPUs into perspective | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 29–30 |
| Message passing | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 31 |
| Loosely coupled clusters | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 32 |
| Grid computing | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 33 |
| Interconnection network topologies และ multistage networks | 🔴 ต้องจำแน่นอน | itds-211_comp_arch_Chapter08.pdf, หน้า 34–35 |
| Network characteristics | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 36 |
| Parallel benchmarks และ code or applications | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 37–38 |
| Modeling performance และ arithmetic intensity | 🟡 สำคัญ | itds-211_comp_arch_Chapter08.pdf, หน้า 39 |
| Concluding remarks | ⚪ อ่านเสริม | itds-211_comp_arch_Chapter08.pdf, หน้า 40 |

### บทนี้เรียนเพื่ออะไร

บทนี้เรียนเพื่อเข้าใจว่าการใช้หลาย processor เพิ่มประสิทธิภาพได้อย่างไร: จำแนกสถาปัตยกรรมแบบ SISD/SIMD/MIMD, เทียบ vector/SIMD, multithreading, shared memory, GPU, clusters และ network topologies พร้อมความยากของ parallel software และวิธีวัดประสิทธิภาพ

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 4–40

### จุดประสงค์ของบทนี้ — สรุปเป้าหมายจากเนื้อหา

- อธิบายเป้าหมาย multiprocessors และความยากของ parallel programming (itds-211_comp_arch_Chapter08.pdf, หน้า 5–8)
- จำแนก SISD/SIMD/MISD/MIMD/SPMD และเทียบ vector กับ SIMD/multimedia extensions (itds-211_comp_arch_Chapter08.pdf, หน้า 3, 9–14)
- แยก fine-grain, coarse-grain และ simultaneous multithreading (itds-211_comp_arch_Chapter08.pdf, หน้า 15–18)
- อธิบาย shared memory (UMA/NUMA) และไล่ตัวอย่าง sum reduction (itds-211_comp_arch_Chapter08.pdf, หน้า 19–21)
- อธิบายสถาปัตยกรรม GPU, Fermi, memory structures และการจำแนก GPU (itds-211_comp_arch_Chapter08.pdf, หน้า 22–30)
- เทียบ message passing, clusters, grid และ network topologies/characteristics (itds-211_comp_arch_Chapter08.pdf, หน้า 31–36)
- รู้จัก parallel benchmarks และ arithmetic intensity (itds-211_comp_arch_Chapter08.pdf, หน้า 37–39)

วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจาก Chapter Overview หน้า 4 และ Concluding Remarks หน้า 40

### ขอบเขตและข้อมูลที่ต้องตรวจสอบ

- อ่านและตรวจภาพครบ 41 หน้า: หน้า 1 ปก, หน้า 2 course outline, หน้า 4 chapter overview, หน้า 41 Q&A
- สไลด์ไม่มีรายการ Chapter Objectives โดยตรงหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; ระดับสีเป็นลำดับเวลาอ่าน ไม่ใช่สถิติการออกสอบ
- หน้า 3 เป็น Figure 17.1 จาก Pearson (ต่างจากตำรา MK ส่วนอื่นของบท)
- หน้า 30 Guide to GPU Terms ตัวอักษรเล็กเกินกว่าจะสรุปรายละเอียดได้: ต้องตรวจสอบจากต้นฉบับ
- ภาพหน้า 21 แสดงต้นไม้ half = 4, 2, 1 (8 processors) ขณะที่โค้ดเริ่ม half = 64
- ภาพหน้า 14 ถูกตัดขอบบางส่วน; ตัวเลขตารางหน้า 29 เป็นค่าตามสไลด์ ไม่ใช่สเปกปัจจุบัน
- คำถามคำนวณใช้เฉพาะตัวเลขและนิยามในสไลด์; ไม่มีการอ้างว่าเป็นข้อสอบจริง

## 2. สรุปรายบทและหัวข้อ

### 1. Taxonomy ของ parallel processor architectures

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 3**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

ภาพหน้า 3 (Figure 17.1 จาก Pearson) แบ่ง processor organizations เป็น SISD, SIMD, MISD และ MIMD. SISD คือ uniprocessor; SIMD แตกเป็น vector processor และ array processor; MIMD แตกเป็น shared memory (tightly coupled) ซึ่งมี SMP และ NUMA กับ distributed memory (loosely coupled) ซึ่งคือ clusters.

**ประเด็นที่ต้องจำ**

- SISD → Uniprocessor (หน้า 3)
- SIMD → Vector processor, Array processor (หน้า 3)
- MIMD → Shared memory (tightly coupled): SMP, NUMA (หน้า 3)
- MIMD → Distributed memory (loosely coupled): Clusters (หน้า 3)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SISD
- SIMD
- MISD
- MIMD
- SMP
- NUMA
- clusters
- tightly coupled
- loosely coupled

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ต้นไม้หน้า 3 เป็นแผนที่ของบท: SIMD/vector (หน้า 9–14), shared memory (หน้า 19–21), clusters (หน้า 31–33)

**จุดที่อาจสับสน:** Tightly coupled = shared memory; loosely coupled = distributed memory/clusters อย่าสลับกัน

**ประโยคช่วยจำ:** MIMD แยกสองทาง: แชร์ memory (แน่น) หรือแยก memory (หลวม)

### 2. Introduction: เป้าหมายของ multiprocessors

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 4–5**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

เป้าหมายคือเชื่อมหลายคอมพิวเตอร์เพื่อให้ได้ประสิทธิภาพสูงขึ้น. Multiprocessors ให้ scalability, availability และ power efficiency. Task-level (process-level) parallelism ให้ throughput สูงสำหรับงานอิสระ; parallel processing program คือโปรแกรมเดียวที่รันบนหลาย processor; multicore microprocessor คือชิปที่มีหลาย processor (cores).

**ประเด็นที่ต้องจำ**

- Goal: connecting multiple computers to get higher performance (หน้า 5)
- Multiprocessors: scalability, availability, power efficiency (หน้า 5)
- Task-level parallelism: high throughput for independent jobs (หน้า 5)
- Parallel processing program: single program on multiple processors (หน้า 5)
- Multicore: chips with multiple processors (cores) (หน้า 5)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- multiprocessor
- task-level (process-level) parallelism
- parallel processing program
- multicore
- scalability
- availability

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** Chapter overview หน้า 4 เรียงหัวข้อ: difficulty → SISD/MIMD/SIMD/SPMD/Vector → multithreading → shared memory → GPUs → clusters → network topologies

**จุดที่อาจสับสน:** Task-level parallelism คือหลายงานอิสระ; parallel processing program คือโปรแกรมเดียวแบ่งไปหลาย processor

**ประโยคช่วยจำ:** หลายงานอิสระ = task-level; งานเดียวแบ่งช่วย = parallel program

### 3. Hardware และ software: serial/parallel, sequential/concurrent

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 6–7**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

Hardware แบ่งเป็น serial (เช่น Pentium 4) และ parallel (เช่น quad-core Xeon e5345). Software แบ่งเป็น sequential (เช่น matrix multiplication) และ concurrent (เช่น operating system). software ทั้งสองแบบรันได้บน hardware ทั้งสองแบบ ความท้าทายคือใช้ parallel hardware ให้มีประสิทธิภาพ. หน้า 7 ทบทวนหัวข้อ parallelism ที่เคยเรียน: synchronization, subword parallelism, ILP และ cache coherence.

**ประเด็นที่ต้องจำ**

- Serial HW: Pentium 4; Parallel HW: quad-core Xeon e5345 (หน้า 6)
- Sequential SW: matrix multiplication; Concurrent SW: operating system (หน้า 6)
- Challenge: making effective use of parallel hardware (หน้า 6)
- Covered: synchronization, subword parallelism, ILP, cache coherence (หน้า 7)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- serial hardware
- parallel hardware
- sequential software
- concurrent software
- cache coherence
- subword parallelism

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** matrix multiplication เป็น sequential software ได้ แต่ก็รันบน parallel hardware ได้ตามหน้า 6

|  | Serial HW | Parallel HW |
| --- | --- | --- |
| Sequential SW | matrix multiply บน Pentium 4 | matrix multiply บน Xeon e5345 |
| Concurrent SW | OS บน Pentium 4 | OS บน Xeon e5345 |

**จุดที่อาจสับสน:** Sequential/concurrent อธิบาย software; serial/parallel อธิบาย hardware

**ประโยคช่วยจำ:** Hardware: serial/parallel · Software: sequential/concurrent

### 4. ความยากของการเขียน parallel program

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 8**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

ปัญหาอยู่ที่ parallel software: ต้องได้ performance improvement อย่างมีนัยสำคัญ ไม่เช่นนั้นใช้ uniprocessor ที่เร็วขึ้นจะง่ายกว่า. ความยากหลักคือ partitioning, coordination และ communications overhead.

**ประเด็นที่ต้องจำ**

- Parallel software is the problem (หน้า 8)
- ต้องได้ significant performance improvement มิฉะนั้นใช้ faster uniprocessor (หน้า 8)
- Difficulties: partitioning, coordination, communications overhead (หน้า 8)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- partitioning
- coordination
- communications overhead
- uniprocessor

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตัวอย่าง sum reduction หน้า 20–21 ต้อง partition ข้อมูล, synch() เพื่อ coordination และรวมผลระหว่าง processor

**จุดที่อาจสับสน:** ปัญหาที่สไลด์เน้นคือ software ไม่ใช่การหา hardware

**ประโยคช่วยจำ:** แบ่ง–ประสาน–สื่อสาร (P-C-C)

### 5. Instruction/data streams และ SPMD

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 9**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

จำแนกตามจำนวน instruction stream และ data stream: SISD (Intel Pentium 4), SIMD (SSE instructions ของ x86), MISD (ไม่มีตัวอย่างในปัจจุบัน) และ MIMD (Intel Xeon e5345). SPMD (Single Program Multiple Data) คือ parallel program บน MIMD computer ที่ใช้ conditional code ให้ processor ต่างกันทำงานต่างกัน.

**ประเด็นที่ต้องจำ**

- SISD: Intel Pentium 4; SIMD: SSE of x86 (หน้า 9)
- MISD: no examples today; MIMD: Intel Xeon e5345 (หน้า 9)
- SPMD: parallel program on a MIMD computer (หน้า 9)
- SPMD ใช้ conditional code for different processors (หน้า 9)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SISD
- SIMD
- MISD
- MIMD
- SPMD
- instruction stream
- data stream

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** โค้ด sum reduction หน้า 21 ใช้ if (Pn < half) แยกงานตาม processor — ตรงกับลักษณะ SPMD

| Instruction \ Data | Single | Multiple |
| --- | --- | --- |
| Single | SISD: Intel Pentium 4 | SIMD: SSE instructions of x86 |
| Multiple | MISD: No examples today | MIMD: Intel Xeon e5345 |

**จุดที่อาจสับสน:** SPMD ไม่ใช่ประเภทฮาร์ดแวร์ในตาราง 2×2 แต่เป็นรูปแบบโปรแกรมบน MIMD

**ประโยคช่วยจำ:** S/M ตัวแรก = instruction, S/M ตัวหลัง = data

### 6. Vector processors และ vector extension ของ RISC-V

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 10**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

Vector processor ใช้ function units ที่ pipeline สูง และ stream ข้อมูลระหว่าง vector registers กับ units: ดึงข้อมูลจาก memory เข้า registers แล้วเก็บผลจาก registers กลับ memory. ตัวอย่าง vector extension ของ RISC-V มี v0–v31 เป็น 32 registers แต่ละตัวมี 64 elements (element ละ 64 บิต) และคำสั่ง fld.v/fsd.v, fadd.d.v, fadd.d.vs ซึ่งลด instruction-fetch bandwidth อย่างมาก.

**ประเด็นที่ต้องจำ**

- Highly pipelined function units (หน้า 10)
- v0–v31: 32 × 64-element registers, 64-bit elements (หน้า 10)
- fld.v, fsd.v: load/store vector; fadd.d.v: add vectors; fadd.d.vs: add scalar to each element (หน้า 10)
- Significantly reduces instruction-fetch bandwidth (หน้า 10)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- vector register
- fld.v
- fsd.v
- fadd.d.v
- fadd.d.vs
- instruction-fetch bandwidth

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** fadd.d.vs บวก scalar เข้ากับทุก element ของ vector; fadd.d.v บวก vector กับ vector

**สูตรที่ต้องรู้**

```text
1 vector register = 64 elements × 64 bits = 4096 bits
v0–v31 = 32 registers
```

คำนวณจากข้อกำหนดหน้า 10

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 10

**จุดที่อาจสับสน:** v0–v31 คือ 32 registers ไม่ใช่ 32 elements; แต่ละ register มี 64 elements

**ประโยคช่วยจำ:** .v = vector กับ vector, .vs = vector กับ scalar

### 7. ตัวอย่าง DAXPY: scalar loop เทียบ vector code

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 11**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

DAXPY (Y = a × X + Y) คือคำสั่ง linear algebra ใน library BLAS (double-precision A*X Plus Y). โค้ด RISC-V แบบปกติใช้ loop ที่ load x[i], คูณ a, load y[i], บวก, store y[i] และเพิ่ม index ทีละ 8 จนถึง x19+512. โค้ด vector ทำงานเดียวกันด้วย 6 คำสั่ง: fld, fld.v, fmul.d.vs, fld.v, fadd.d.v, fsd.v โดยไม่มี loop.

**ประเด็นที่ต้องจำ**

- DAXPY = double-precision A*X Plus Y ใน BLAS (หน้า 11)
- Conventional: loop 8 คำสั่ง (fld, fmul.d, fld, fadd.d, fsd, addi, addi, bltu) (หน้า 11)
- Vector: 6 คำสั่ง ไม่มี loop (หน้า 11)
- addi x5,x19,512 = end of array X; index เพิ่มทีละ 8 (หน้า 11)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- DAXPY
- BLAS
- fmul.d.vs
- fadd.d.v
- loop

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** C: for (i = 0; i < n; i++) y[i] = a * x[i] + y[i];

**นับรอบ loop ของ DAXPY แบบ scalar (หน้า 11)**

1. x5 = x19 + 512 คือจุดสิ้นสุดของ array X
2. ทุกรอบ addi x19,x19,8 เลื่อน index ไป 8 ไบต์ (double หนึ่งตัว)
3. bltu x19,x5,loop วนจนกว่า x19 ถึง x5

**คำตอบ:** 512 / 8 = 64 รอบ; vector code แทนด้วย 6 คำสั่งไม่มี loop

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 10–11

**จุดที่อาจสับสน:** fmul.d.vs คูณ vector กับ scalar a; fadd.d.v บวก vector กับ vector

**ประโยคช่วยจำ:** scalar วนทีละตัว, vector ทำทีเดียวทั้งแถว

### 8. Vector vs. scalar

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 12**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

Vector architecture และ compiler ทำให้เขียน data-parallel program ง่ายขึ้น: ระบุชัดว่าไม่มี loop-carried dependence จึงลดการตรวจใน hardware, access pattern ที่สม่ำเสมอได้ประโยชน์จาก interleaved และ burst memory, และหลีกเลี่ยง control hazard เพราะไม่มี loop. vector ยังทั่วไปกว่า media extension เฉพาะกิจ (MMX, SSE) และเข้ากับ compiler technology ได้ดีกว่า.

**ประเด็นที่ต้องจำ**

- Explicit absence of loop-carried dependences → reduced checking in hardware (หน้า 12)
- Regular access patterns benefit from interleaved and burst memory (หน้า 12)
- Avoid control hazards by avoiding loops (หน้า 12)
- More general than MMX, SSE; better match with compiler technology (หน้า 12)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- loop-carried dependence
- interleaved memory
- burst memory
- control hazard
- MMX
- SSE

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เชื่อมกับ Chapter07: ไม่มี loop = ไม่มี branch ของ loop = ไม่มี control hazard จาก loop

**จุดที่อาจสับสน:** ข้อดีเรื่อง control hazard มาจากการไม่มี loop ไม่ใช่จาก branch prediction

**ประโยคช่วยจำ:** ไม่มี loop: ไม่มี dependence ข้ามรอบ ไม่มี branch

### 9. SIMD

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 13**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

SIMD ทำงานแบบ elementwise บน vector ของข้อมูล เช่น MMX และ SSE ใน x86 ที่มีหลาย data elements ใน register กว้าง 128 บิต. processor ทุกตัวทำคำสั่งเดียวกันในเวลาเดียวกันแต่ใช้ data address ต่างกัน ทำให้ synchronization ง่ายขึ้น ใช้ instruction control hardware น้อยลง และเหมาะกับงานที่ data-parallel สูง.

**ประเด็นที่ต้องจำ**

- Operate elementwise on vectors of data (หน้า 13)
- MMX/SSE: multiple data elements in 128-bit registers (หน้า 13)
- All processors execute same instruction at same time, different data address (หน้า 13)
- Simplifies synchronization; reduced instruction control hardware (หน้า 13)
- Works best for highly data-parallel applications (หน้า 13)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SIMD
- elementwise
- MMX
- SSE
- 128-bit register
- data-parallel

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** MMX/SSE ใส่หลาย data elements ลงใน register 128 บิต แล้วคำสั่งเดียวทำกับทุก element พร้อมกัน

**จุดที่อาจสับสน:** SIMD ทุก processor ทำคำสั่งเดียวกัน; ถ้าต้องการคำสั่งต่างกันคือ MIMD

**ประโยคช่วยจำ:** คำสั่งเดียว ข้อมูลหลายชุด เดินพร้อมกัน

### 10. Vector vs. multimedia extensions

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 14**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

Vector instructions มีความกว้าง vector ที่เปลี่ยนได้ (variable) ส่วน multimedia extensions มีความกว้างคงที่ (fixed). vector รองรับ strided access แต่ multimedia extensions ไม่รองรับ. vector unit อาจเป็นการผสมระหว่าง pipelined และ arrayed functional units ตามภาพที่แบ่งเป็น lanes.

**ประเด็นที่ต้องจำ**

- Vector: variable width; multimedia: fixed width (หน้า 14)
- Vector supports strided access; multimedia does not (หน้า 14)
- Vector units = pipelined + arrayed functional units (หน้า 14)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- variable vector width
- fixed width
- strided access
- lane
- arrayed functional units

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 14 แสดง vector unit แบบ 4 lanes แต่ละ lane มี FP add/FP mul pipe และ vector registers ส่วนหนึ่ง

| คุณสมบัติ | Vector | Multimedia extensions |
| --- | --- | --- |
| ความกว้าง | variable | fixed |
| Strided access | รองรับ | ไม่รองรับ |

**จุดที่อาจสับสน:** ภาพขวาหน้า 14 ถูกตัดขอบบางส่วน รายละเอียดเลข lane: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** Vector ยืดได้ กระโดดได้; multimedia คงที่

### 11. Hardware multithreading: fine-grain และ coarse-grain

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 15**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

Multithreading คือทำหลาย thread ขนานกันโดย replicate registers, PC ฯลฯ และสลับ thread ได้เร็ว. Fine-grain สลับ thread ทุก cycle (interleave) ถ้า thread หนึ่ง stall ก็ทำ thread อื่น. Coarse-grain สลับเฉพาะ stall ยาว (เช่น L2-cache miss) ทำให้ hardware ง่ายแต่ซ่อน stall สั้น (เช่น data hazard) ไม่ได้.

**ประเด็นที่ต้องจำ**

- Replicate registers, PC; fast switching (หน้า 15)
- Fine-grain: switch after each cycle; interleave; if one stalls, others execute (หน้า 15)
- Coarse-grain: switch only on long stall เช่น L2-cache miss (หน้า 15)
- Coarse-grain: simpler HW แต่ไม่ซ่อน short stalls (data hazards) (หน้า 15)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- multithreading
- fine-grain multithreading
- coarse-grain multithreading
- thread switching
- L2-cache miss
- stall

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 17 แถว Fine MT สลับสีทุกแถว (cycle) ส่วน Coarse MT ทำ thread เดียวนานจนเกิด stall ยาวจึงเปลี่ยน

| แบบ | สลับ thread เมื่อ | ข้อดี/ข้อจำกัด |
| --- | --- | --- |
| Fine-grain | ทุก cycle | thread อื่นทำงานเมื่อ thread หนึ่ง stall |
| Coarse-grain | stall ยาว (L2 miss) | hardware ง่าย แต่ไม่ซ่อน short stall |

**จุดที่อาจสับสน:** Coarse-grain ไม่ซ่อน data hazard สั้น ๆ เพราะสลับเฉพาะ stall ยาว

**ประโยคช่วยจำ:** Fine ละเอียด สลับทุกจังหวะ; Coarse หยาบ สลับตอนรอนาน

### 12. Simultaneous multithreading (SMT) และตัวอย่าง

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 16–17**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

SMT ใช้ใน multiple-issue dynamically scheduled processor: schedule คำสั่งจากหลาย thread พร้อมกัน คำสั่งจาก thread อิสระทำงานเมื่อ function unit ว่าง ภายใน thread ใช้ scheduling และ register renaming จัดการ dependency. ตัวอย่าง Intel Pentium-4 HT มี 2 threads ที่ duplicate registers แต่แชร์ function units และ caches. ภาพหน้า 17 เทียบ issue slots ของ Coarse MT, Fine MT และ SMT.

**ประเด็นที่ต้องจำ**

- SMT ใน multiple-issue dynamically scheduled processor (หน้า 16)
- Schedule instructions from multiple threads; execute when function units available (หน้า 16)
- Within threads: scheduling and register renaming (หน้า 16)
- Pentium-4 HT: 2 threads, duplicated registers, shared function units and caches (หน้า 16)
- ภาพ issue slots: Coarse MT, Fine MT, SMT (หน้า 17)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- simultaneous multithreading (SMT)
- multiple-issue
- dynamic scheduling
- register renaming
- issue slot
- Hyper-Threading (HT)

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 17: SMT เติม issue slots ในแถวเดียวกันด้วยคำสั่งจากหลาย thread ขณะที่ fine/coarse MT ใช้ thread เดียวต่อแถว

**จุดที่อาจสับสน:** SMT ต่างจาก fine-grain ที่ fine-grain สลับ thread ระหว่าง cycle แต่ SMT ผสมหลาย thread ใน cycle เดียว

**ประโยคช่วยจำ:** SMT = หลาย thread ใน cycle เดียว

### 13. Future of multithreading

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter08.pdf, **หน้า 18**

เหตุผลการจัดระดับ: เป็นภาพรวม ประวัติ หรือข้อสรุปประกอบ

สไลด์ตั้งคำถามว่า multithreading จะอยู่รอดหรือไม่และในรูปแบบใด. ข้อพิจารณาเรื่อง power ทำให้ microarchitecture เรียบง่ายขึ้น จึงใช้ multithreading แบบง่ายขึ้น; การทน cache-miss latency อาจใช้ thread switch ได้ดีที่สุด; และ multiple simple cores อาจแชร์ทรัพยากรได้มีประสิทธิภาพกว่า.

**ประเด็นที่ต้องจำ**

- Power considerations ⇒ simplified microarchitectures (หน้า 18)
- Simpler forms of multithreading (หน้า 18)
- Tolerating cache-miss latency: thread switch may be most effective (หน้า 18)
- Multiple simple cores might share resources more effectively (หน้า 18)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- power considerations
- cache-miss latency
- thread switch
- simple cores

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เชื่อมกับหน้า 15: thread switch เมื่อ cache miss คือแนวคิดของ coarse-grain

**จุดที่อาจสับสน:** หน้านี้เป็นแนวโน้มเชิงความเห็น ไม่ใช่นิยาม

**ประโยคช่วยจำ:** พลังงานบีบให้ง่าย — สลับ thread ตอน miss

### 14. Shared memory multiprocessor (SMP), UMA และ NUMA

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 19**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

SMP (shared memory multiprocessor) คือ hardware ให้ single physical address space แก่ทุก processor และ synchronize shared variables ด้วย locks. ด้าน memory access time แบ่งเป็น UMA (uniform) และ NUMA (nonuniform). ภาพแสดงแต่ละ processor มี cache ต่อเข้ากับ interconnection network ไปยัง memory และ I/O ร่วม.

**ประเด็นที่ต้องจำ**

- SMP: single physical address space for all processors (หน้า 19)
- Synchronize shared variables using locks (หน้า 19)
- UMA (uniform) vs. NUMA (nonuniform) memory access time (หน้า 19)
- Processor → Cache → Interconnection Network → Memory, I/O (ภาพหน้า 19)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SMP
- single physical address space
- lock
- UMA
- NUMA
- interconnection network

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ตัวอย่าง sum reduction หน้า 20 ใช้ 64-processor UMA

|  | Shared memory (SMP) | Message passing |
| --- | --- | --- |
| Address space | single physical, ร่วมกัน | private ต่อ processor |
| การประสาน | locks | send/receive messages |
| หน้า | 19 | 31 |

**จุดที่อาจสับสน:** SMP แชร์ address space; message passing (หน้า 31) แต่ละ processor มี private address space

**ประโยคช่วยจำ:** SMP: ที่อยู่เดียว แชร์กัน ล็อกกัน

### 15. ตัวอย่าง sum reduction บน 64-processor UMA

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 20–21**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

รวมเลข 64,000 ตัวบน UMA 64 processors: processor มี ID 0 ≤ Pn ≤ 63 แบ่งให้ตัวละ 1000 ตัว แต่ละตัวรวม sum[Pn] ของช่วงตัวเอง. จากนั้นรวม partial sums แบบ divide and conquer: ครึ่งหนึ่งของ processors บวกเป็นคู่ แล้วเหลือหนึ่งในสี่ ... และต้อง synch() ระหว่างแต่ละขั้น. ถ้า half เป็นเลขคี่ processor 0 รับ element ที่ขาด.

**ประเด็นที่ต้องจำ**

- 64,000 numbers / 64 processors = 1000 per processor (หน้า 20)
- sum[Pn] รวม A[1000*Pn] ถึง A[1000*(Pn+1)−1] (หน้า 20)
- Reduction: divide and conquer; synchronize between steps (หน้า 20)
- if (half%2 != 0 && Pn == 0) sum[0] += sum[half-1] (หน้า 21)
- if (Pn < half) sum[Pn] += sum[Pn+half] (หน้า 21)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- sum reduction
- partial sum
- divide and conquer
- synch()
- UMA

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** โค้ดหน้า 21 เริ่ม half = 64 แล้วหารครึ่ง 32, 16, 8, 4, 2, 1 → 6 รอบของ loop

**สูตรที่ต้องรู้**

```text
64,000 / 64 = 1000 numbers per processor
sum[Pn] = Σ A[i], i = 1000·Pn … 1000·(Pn+1) − 1
```

การแบ่งงานขั้นแรกตามหน้า 20

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 20

**ไล่ loop reduction (หน้า 21)**

1. เริ่ม half = 64
2. แต่ละรอบ: synch() → ถ้า half คี่และ Pn = 0 ให้ sum[0] += sum[half−1] → half = half/2 → ถ้า Pn < half ให้ sum[Pn] += sum[Pn+half]
3. half หลังหาร: 32 → 16 → 8 → 4 → 2 → 1
4. เมื่อ half = 1 เงื่อนไข while (half > 1) เป็นเท็จ

**คำตอบ:** 6 รอบ ผลรวมทั้งหมดอยู่ใน sum[0]

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 21

**จุดที่อาจสับสน:** ภาพต้นไม้หน้า 21 แสดงเพียง half = 4, 2, 1 (8 processors) เพื่อสาธิต ขณะที่โค้ดเริ่มที่ half = 64

**ประโยคช่วยจำ:** แบ่งก่อนรวมเอง แล้วครึ่งต่อครึ่งจนเหลือหนึ่ง

### 16. ประวัติ GPU และกราฟิกในระบบ

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter08.pdf, **หน้า 22–23**

เหตุผลการจัดระดับ: เป็นภาพรวม ประวัติ หรือข้อสรุปประกอบ

เริ่มจาก video card ยุคแรกที่มี frame buffer memory กับ address generation สำหรับ video output. 3D graphics processing เดิมอยู่ในคอมพิวเตอร์ระดับสูง (เช่น SGI) แล้ว Moore’s Law ทำให้ราคาต่ำลงและหนาแน่นขึ้นจนมี 3D graphics card สำหรับ PC และเครื่องเกม. GPU คือ processor ที่มุ่งงาน 3D graphics เช่น vertex/pixel processing, shading, texture mapping, rasterization. หน้า 23 แสดงตำแหน่ง GPU ในระบบ (ต่อผ่าน PCI-Express กับ North Bridge/chipset และมี GPU memory).

**ประเด็นที่ต้องจำ**

- Early video cards: frame buffer memory + address generation (หน้า 22)
- Moore’s Law ⇒ lower cost, higher density (หน้า 22)
- GPU tasks: vertex/pixel processing, shading, texture mapping, rasterization (หน้า 22)
- GPU ต่อผ่าน x16 PCI-Express link และมี GPU memory ของตัวเอง (ภาพหน้า 23)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- frame buffer
- 3D graphics
- Moore’s Law
- vertex/pixel processing
- shading
- texture mapping
- rasterization
- PCI-Express

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ภาพหน้า 23 เทียบระบบ VGA controller เก่า กับ Intel CPU + North Bridge + GPU และ AMD CPU ที่มี North Bridge ในชิป

**จุดที่อาจสับสน:** GPU memory ในภาพแยกจาก system DDR2 memory

**ประโยคช่วยจำ:** Video card → 3D card → GPU

### 17. GPU architectures

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 24**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

งานของ GPU เป็น data-parallel สูง. GPU เป็น highly multithreaded ใช้ thread switching ซ่อน memory latency จึงพึ่ง multi-level caches น้อยลง และ graphics memory กว้างและ bandwidth สูง. มีแนวโน้มไปสู่ general purpose GPU ในระบบ heterogeneous: CPU ทำ sequential code, GPU ทำ parallel code. ภาษา/API ได้แก่ DirectX, OpenGL, Cg, HLSL และ CUDA.

**ประเด็นที่ต้องจำ**

- Processing is highly data-parallel (หน้า 24)
- Highly multithreaded; thread switching to hide memory latency; less reliance on multi-level caches (หน้า 24)
- Graphics memory is wide and high-bandwidth (หน้า 24)
- Heterogeneous: CPU for sequential code, GPU for parallel code (หน้า 24)
- APIs: DirectX, OpenGL, Cg, HLSL, CUDA (หน้า 24)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- GPU
- data-parallel
- thread switching
- memory latency
- heterogeneous CPU/GPU
- CUDA
- DirectX
- OpenGL
- HLSL
- Cg

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบกับ multithreading หน้า 15: GPU ใช้ thread switching แบบเดียวกันเพื่อซ่อน latency

**จุดที่อาจสับสน:** GPU ไม่ได้ซ่อน latency ด้วย cache ใหญ่ แต่ด้วยการสลับ thread

**ประโยคช่วยจำ:** GPU ซ่อนการรอด้วยการสลับ thread ไม่ใช่ด้วย cache

### 18. ตัวอย่าง NVIDIA Fermi

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 25–26**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

Fermi ประกอบด้วย SIMD processors หลายตัว แต่ละตัวมี 16 SIMD lanes (thread processors). SIMD instruction ทำงานบน thread กว้าง 32 elements และถูก schedule แบบ dynamic บน processor กว้าง 16 ใน 2 cycles. มี registers 32K × 32-bit กระจายทั่ว lanes และ 64 registers ต่อ thread context. ภาพหน้า 25 แสดง instruction register, lanes ที่มี Reg 1K×32 และ load/store unit, address coalescing unit, interconnection network และ local memory 64 KiB.

**ประเด็นที่ต้องจำ**

- SIMD Processor: 16 SIMD lanes (หน้า 26)
- SIMD instruction: 32 element wide threads, 16-wide processor over 2 cycles (หน้า 26)
- 32K × 32-bit registers; 64 registers per thread context (หน้า 26)
- ภาพ: Reg 1K×32 ต่อ lane, Local Memory 64 KiB (หน้า 25)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SIMD lane
- thread processor
- thread context
- address coalescing unit
- local memory

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** 32 elements / 16 lanes = 2 cycles ต่อ SIMD instruction

**สูตรที่ต้องรู้**

```text
32 elements / 16 lanes = 2 cycles
32K × 32-bit registers; 64 registers per thread context
```

ตัวเลขจากหน้า 26

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 26

**จุดที่อาจสับสน:** 32 คือความกว้าง thread ส่วน 16 คือจำนวน lanes จึงใช้ 2 cycles

**ประโยคช่วยจำ:** 32 งาน 16 มือ = 2 รอบ

### 19. GPU memory structures

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 27**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

ภาพหน้า 27 แสดงลำดับชั้น memory ของ GPU: CUDA thread แต่ละตัวมี per-CUDA thread private memory, thread block ใช้ per-block local memory ร่วมกัน และ grid (Grid 0, Grid 1 ตามลำดับเวลา) ใช้ GPU memory โดยมี inter-grid synchronization ระหว่าง grid.

**ประเด็นที่ต้องจำ**

- CUDA thread ↔ per-CUDA thread private memory (หน้า 27)
- Thread block ↔ per-block local memory (หน้า 27)
- Grid 0, Grid 1 ↔ GPU memory; inter-grid synchronization (หน้า 27)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- CUDA thread
- thread block
- grid
- private memory
- local memory
- GPU memory
- inter-grid synchronization

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ไล่จากเล็กไปใหญ่: thread → block → grid และ memory ก็ขยายตาม private → local → GPU memory

**จุดที่อาจสับสน:** Local memory ในภาพนี้คือ per-block (แชร์ใน block) ไม่ใช่ private ของ thread เดียว

**ประโยคช่วยจำ:** thread ส่วนตัว · block แชร์กลุ่ม · grid ใช้ GPU memory

### 20. Classifying GPUs

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 28**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

GPU ไม่เข้ากับโมเดล SIMD/MIMD อย่างลงตัว: conditional execution ใน thread ทำให้ดูเหมือน MIMD แต่ประสิทธิภาพลดลง จึงต้องเขียน general purpose code อย่างระวัง. ตารางแบ่ง parallelism ตามระดับและเวลาที่ค้นพบ: ILP แบบ static = VLIW, dynamic = Superscalar; DLP แบบ static = SIMD or Vector, dynamic = Tesla Multiprocessor.

**ประเด็นที่ต้องจำ**

- Don’t fit nicely into SIMD/MIMD model (หน้า 28)
- Conditional execution → illusion of MIMD but performance degradation (หน้า 28)
- ILP: static VLIW, dynamic Superscalar (หน้า 28)
- DLP: static SIMD or Vector, dynamic Tesla Multiprocessor (หน้า 28)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- VLIW
- superscalar
- SIMD
- vector
- Tesla multiprocessor
- instruction-level parallelism
- data-level parallelism

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** Static = discovered at compile time; Dynamic = discovered at runtime

|  | Static (compile time) | Dynamic (runtime) |
| --- | --- | --- |
| Instruction-Level Parallelism | VLIW | Superscalar |
| Data-Level Parallelism | SIMD or Vector | Tesla Multiprocessor |

**จุดที่อาจสับสน:** Tesla multiprocessor อยู่ช่อง data-level + dynamic ไม่ใช่ instruction-level

**ประโยคช่วยจำ:** Compile time = Static (VLIW, SIMD/Vector); Runtime = Dynamic (Superscalar, Tesla)

### 21. Putting GPUs into perspective

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 29–30**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

ตารางหน้า 29 เทียบ multicore with SIMD กับ GPU: SIMD processors 4–8 vs 8–16, SIMD lanes/processor 2–4 vs 8–16, multithreading support 2–4 vs 16–32, single:double precision 2:1 ทั้งคู่, largest cache 8 MB vs 0.75 MB, memory address 64-bit ทั้งคู่, main memory 8–256 GB vs 4–6 GB, page protection Yes ทั้งคู่, demand paging Yes vs No, integrated scalar/SIMD processor Yes vs No, cache coherent Yes vs No. หน้า 30 เป็นตาราง Guide to GPU Terms.

**ประเด็นที่ต้องจำ**

- GPU: SIMD processors 8–16, lanes 8–16, MT support 16–32 (หน้า 29)
- Largest cache: multicore 8 MB vs GPU 0.75 MB (หน้า 29)
- GPU: No demand paging, not cache coherent, no integrated scalar processor (หน้า 29)
- Guide to GPU Terms (หน้า 30): ตัวอักษรเล็ก รายละเอียดต้องตรวจสอบจากต้นฉบับ

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- multicore with SIMD
- demand paging
- cache coherent
- SIMD lanes
- memory protection

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ใช้ตารางด้านล่างจำว่า GPU “มากกว่า” ที่ lanes/threads แต่ “น้อยกว่า/ไม่มี” ที่ cache, memory, paging, coherence

| Feature | Multicore with SIMD | GPU |
| --- | --- | --- |
| SIMD processors | 4 to 8 | 8 to 16 |
| SIMD lanes/processor | 2 to 4 | 8 to 16 |
| MT support for SIMD threads | 2 to 4 | 16 to 32 |
| Single:double precision | 2:1 | 2:1 |
| Largest cache | 8 MB | 0.75 MB |
| Memory address | 64-bit | 64-bit |
| Main memory | 8–256 GB | 4–6 GB |
| Page-level protection | Yes | Yes |
| Demand paging | Yes | No |
| Integrated scalar/SIMD | Yes | No |
| Cache coherent | Yes | No |

**จุดที่อาจสับสน:** ทั้งคู่มี memory address 64-bit และ page-level protection เหมือนกัน

**ประโยคช่วยจำ:** GPU: thread เยอะ cache เล็ก ไม่ coherent

### 22. Message passing

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 31**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

ใน message-passing multiprocessor แต่ละ processor มี private physical address space และ hardware ส่ง/รับ messages ระหว่าง processors. ภาพแสดงแต่ละ processor มี cache และ memory ของตัวเองเชื่อมกันผ่าน interconnection network.

**ประเด็นที่ต้องจำ**

- Each processor has private physical address space (หน้า 31)
- Hardware sends/receives messages between processors (หน้า 31)
- Processor → Cache → Memory ของตัวเอง → Interconnection Network (ภาพหน้า 31)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- message passing
- private physical address space
- send/receive
- interconnection network

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เทียบภาพหน้า 19 (memory ร่วมหลัง network) กับหน้า 31 (memory อยู่กับแต่ละ processor ก่อน network)

**จุดที่อาจสับสน:** ตำแหน่ง memory ในภาพคือจุดต่าง: shared memory อยู่หลัง network, message passing อยู่ติด processor

**ประโยคช่วยจำ:** ไม่มีที่อยู่ร่วม ต้องส่งจดหมาย (message)

### 23. Loosely coupled clusters

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 32**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

Cluster คือเครือข่ายของคอมพิวเตอร์อิสระ แต่ละเครื่องมี private memory และ OS เชื่อมกันผ่าน I/O system (เช่น Ethernet/switch, Internet). เหมาะกับงานที่เป็น independent tasks เช่น web servers, databases, simulations และให้ high availability, scalable, affordable. ปัญหาคือ administration cost (นิยมใช้ virtual machines) และ interconnect bandwidth ต่ำเมื่อเทียบ processor/memory bandwidth ของ SMP.

**ประเด็นที่ต้องจำ**

- Network of independent computers; private memory and OS (หน้า 32)
- Connected using I/O system: Ethernet/switch, Internet (หน้า 32)
- Suitable for independent tasks: web servers, databases, simulations (หน้า 32)
- High availability, scalable, affordable (หน้า 32)
- Problems: administration cost (prefer VMs), low interconnect bandwidth (หน้า 32)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- cluster
- loosely coupled
- private memory and OS
- I/O system
- virtual machine
- interconnect bandwidth

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** Concluding remarks หน้า 40: SaaS สำคัญขึ้นและ clusters เข้ากันได้ดี

**จุดที่อาจสับสน:** Cluster ต่อกันผ่าน I/O system ไม่ใช่ memory bus จึง bandwidth ต่ำกว่า SMP

**ประโยคช่วยจำ:** แยกเครื่อง แยก OS ต่อผ่าน network — ถูก ทนทาน แต่ช้าตอนคุยกัน

### 24. Grid computing

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 33**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

Grid computing คือคอมพิวเตอร์แยกกันที่เชื่อมด้วย long-haul networks เช่น Internet. งานถูกแบ่งเป็น work units ส่งออกไปแล้วส่งผลกลับ และใช้ประโยชน์จากเวลาว่างของ PC ได้ เช่น SETI@home และ World Community Grid.

**ประเด็นที่ต้องจำ**

- Separate computers interconnected by long-haul networks (หน้า 33)
- Work units farmed out, results sent back (หน้า 33)
- Use idle time on PCs: SETI@home, World Community Grid (หน้า 33)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- grid computing
- long-haul network
- work unit
- idle time

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** SETI@home ส่ง work unit ให้ PC ที่ว่างประมวลผลแล้วส่งผลกลับ

**จุดที่อาจสับสน:** Grid ต่างจาก cluster ตรงที่เชื่อมด้วย long-haul network และใช้ PC ที่ว่าง

**ประโยคช่วยจำ:** แจกงานไปไกล ทำตอนเครื่องว่าง ส่งผลกลับ

### 25. Interconnection network topologies และ multistage networks

**🔴 ต้องจำแน่นอน** · itds-211_comp_arch_Chapter08.pdf, **หน้า 34–35**

เหตุผลการจัดระดับ: เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด

Network topology คือการจัดวาง processors, switches และ links. หน้า 34 แสดง bus, ring, 2D mesh, N-cube (N = 3) และ fully connected. หน้า 35 แสดง multistage networks: crossbar, Omega network และ Omega network switch box (อินพุต A, B ไป C, D).

**ประเด็นที่ต้องจำ**

- Topology = arrangements of processors, switches, and links (หน้า 34)
- Bus, Ring, 2D Mesh, N-cube (N = 3), Fully connected (หน้า 34)
- Multistage: a. Crossbar, b. Omega network, c. Omega switch box (หน้า 35)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- network topology
- bus
- ring
- 2D mesh
- N-cube
- fully connected
- crossbar
- Omega network
- switch box

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** N-cube (N = 3) ในภาพคือ cube มี 8 nodes (2³) — นับจากภาพ

**จุดที่อาจสับสน:** Crossbar กับ Omega เป็น multistage/switch network ไม่ใช่ topology ของ node แบบ bus/ring

**ประโยคช่วยจำ:** B-R-M-C-F: Bus, Ring, Mesh, Cube, Fully connected

### 26. Network characteristics

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 36**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

คุณลักษณะของ network ได้แก่ performance (latency per message บน unloaded network; throughput ซึ่งแยกเป็น link bandwidth, total network bandwidth และ bisection bandwidth; congestion delays ที่ขึ้นกับ traffic), cost, power และ routability in silicon.

**ประเด็นที่ต้องจำ**

- Latency per message (unloaded network) (หน้า 36)
- Throughput: link, total network, bisection bandwidth (หน้า 36)
- Congestion delays (depending on traffic) (หน้า 36)
- Cost, power, routability in silicon (หน้า 36)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- latency
- throughput
- link bandwidth
- total network bandwidth
- bisection bandwidth
- congestion delay
- routability

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** จัดเป็น 4 กลุ่ม: performance, cost, power, routability

**จุดที่อาจสับสน:** Latency วัดบน unloaded network; congestion delay ขึ้นกับ traffic

**ประโยคช่วยจำ:** Performance-Cost-Power-Route

### 27. Parallel benchmarks และ code or applications

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 37–38**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

Benchmarks: Linpack (matrix linear algebra), SPECrate (parallel run ของ SPEC CPU, job-level parallelism), SPLASH (Stanford, mix of kernels/applications, strong scaling), NAS (NASA, CFD kernels) และ PARSEC (Princeton, multithreaded apps ด้วย Pthreads และ OpenMP). หน้า 38: benchmark ดั้งเดิมใช้ code และ data คงที่ แต่ parallel programming เปลี่ยนเร็ว จึงเสนอเทียบระบบที่ implement application ที่กำหนด (เช่น Linpack, Berkeley Design Patterns) เพื่อส่งเสริมนวัตกรรม.

**ประเด็นที่ต้องจำ**

- Linpack: matrix linear algebra; SPECrate: job-level parallelism (หน้า 37)
- SPLASH: strong scaling; NAS: CFD kernels (หน้า 37)
- PARSEC: Pthreads and OpenMP (หน้า 37)
- Traditional: fixed code and data sets (หน้า 38)
- Compare systems implementing a given application → foster innovation (หน้า 38)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- Linpack
- SPECrate
- SPLASH
- NAS
- PARSEC
- Pthreads
- OpenMP
- Berkeley Design Patterns
- strong scaling

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ถ้าต้องการวัด job-level parallelism ให้ใช้ SPECrate

**จุดที่อาจสับสน:** Linpack ถูกยกทั้งในหน้า 37 (benchmark) และหน้า 38 (ตัวอย่างการเทียบตาม application)

**ประโยคช่วยจำ:** L-S-S-N-P: Linpack, SPECrate, SPLASH, NAS, PARSEC

### 28. Modeling performance และ arithmetic intensity

**🟡 สำคัญ** · itds-211_comp_arch_Chapter08.pdf, **หน้า 39**

เหตุผลการจัดระดับ: เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก

สมมติ metric ที่สนใจคือ achievable GFLOPs/sec วัดด้วย computational kernels จาก Berkeley Design Patterns. Arithmetic intensity ของ kernel คือ FLOPs ต่อ byte ของ memory ที่เข้าถึง. สำหรับคอมพิวเตอร์หนึ่งเครื่องให้หา peak GFLOPS (จาก data sheet) และ peak memory bytes/sec (ด้วย Stream benchmark).

**ประเด็นที่ต้องจำ**

- Metric: achievable GFLOPs/sec (หน้า 39)
- Arithmetic intensity = FLOPs per byte of memory accessed (หน้า 39)
- Peak GFLOPS from data sheet (หน้า 39)
- Peak memory bytes/sec using Stream benchmark (หน้า 39)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- GFLOPs/sec
- arithmetic intensity
- Berkeley Design Patterns
- peak GFLOPS
- Stream benchmark

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** ขั้นตอนตามสไลด์: หา arithmetic intensity ของ kernel แล้วหา peak GFLOPS (data sheet) และ peak memory bytes/sec (Stream) ของเครื่อง

**สูตรที่ต้องรู้**

```text
Arithmetic intensity = FLOPs / bytes of memory accessed
```

นิยามจากหน้า 39

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 39

**จุดที่อาจสับสน:** Peak GFLOPS มาจาก data sheet ส่วน peak memory bandwidth วัดด้วย Stream benchmark อย่าสลับ

**ประโยคช่วยจำ:** งานคำนวณ ÷ ไบต์ที่อ่าน = arithmetic intensity

### 29. Concluding remarks

**⚪ อ่านเสริม** · itds-211_comp_arch_Chapter08.pdf, **หน้า 40**

เหตุผลการจัดระดับ: เป็นภาพรวม ประวัติ หรือข้อสรุปประกอบ

เป้าหมายคือประสิทธิภาพสูงขึ้นด้วยการใช้หลาย processor. ความยากคือการพัฒนา parallel software และออกแบบ architecture ที่เหมาะสม. SaaS มีความสำคัญมากขึ้นและ clusters เข้ากันได้ดี. performance per dollar และ performance per Joule เป็นตัวขับเคลื่อนทั้ง mobile และ WSC.

**ประเด็นที่ต้องจำ**

- Goal: higher performance using multiple processors (หน้า 40)
- Difficulties: parallel software, appropriate architectures (หน้า 40)
- SaaS growing; clusters are a good match (หน้า 40)
- Performance per dollar and per Joule drive mobile and WSC (หน้า 40)

**ศัพท์ นิยาม สูตร และสัญลักษณ์ที่เอกสารให้**

- SaaS
- WSC
- performance per dollar
- performance per Joule

**ตัวอย่างวิธีอ่าน/จัดหมวดจากเอกสาร:** เชื่อมกับหน้า 8: ความยากด้าน software ยังเป็นประเด็นหลักจนจบบท

**จุดที่อาจสับสน:** สไลด์ไม่ได้ขยายความ WSC ในเนื้อหาส่วนอื่นของบท: ต้องตรวจสอบจากต้นฉบับ

**ประโยคช่วยจำ:** เร็วขึ้นด้วยหลายตัว แต่ software ยาก; เงินและพลังงานเป็นตัวตัดสิน

## 3. Roadmap ทบทวน

1. **1 · ภาพรวมและความยาก** — taxonomy → goal/multicore → HW/SW → partitioning/coordination/communication (itds-211_comp_arch_Chapter08.pdf, หน้า 3–8)
2. **2 · SIMD และ vector** — ตาราง SISD–MIMD/SPMD → vector registers → DAXPY → vector vs scalar/SIMD/multimedia (itds-211_comp_arch_Chapter08.pdf, หน้า 9–14)
3. **3 · Multithreading** — fine vs coarse → SMT และภาพ issue slots → แนวโน้ม (itds-211_comp_arch_Chapter08.pdf, หน้า 15–18)
4. **4 · Shared memory และ GPU** — SMP/UMA/NUMA → sum reduction → GPU architecture, Fermi, memory, classification, perspective (itds-211_comp_arch_Chapter08.pdf, หน้า 19–30)
5. **5 · Message passing และการวัดผล** — message passing → clusters/grid → topologies/characteristics → benchmarks/arithmetic intensity (itds-211_comp_arch_Chapter08.pdf, หน้า 31–40)

## 4. แผนทบทวนตามเวลา

ผู้ใช้ระบุว่าเวลาไม่จำกัด จึงวางแผนเป็นรอบตามสิ่งที่ทำได้ ไม่กำหนดวันสอบหรือชั่วโมงให้เอง ผ่านเกณฑ์แต่ละรอบแล้วจึงไปต่อ

### รอบ 1 · แผนที่บท

วาดต้นไม้หน้า 3 และตาราง 2×2 หน้า 9 จากความจำ; จำ 3 difficulties หน้า 8

**เกณฑ์ผ่าน:** จับคู่ SISD/SIMD/MISD/MIMD กับตัวอย่างและบอกนิยาม SPMD ได้

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 3–9

### รอบ 2 · Vector/SIMD

อ่าน DAXPY ทั้งสองแบบ นับคำสั่งและรอบ loop; ทำตาราง vector vs multimedia

**เกณฑ์ผ่าน:** อธิบาย .v/.vs และคิด 512/8 = 64 ได้

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 10–14

### รอบ 3 · Multithreading และ shared memory

เทียบ fine/coarse/SMT ด้วยภาพหน้า 17; ไล่โค้ด sum reduction ทีละรอบ

**เกณฑ์ผ่าน:** บอกว่า coarse-grain ไม่ซ่อน short stalls และ reduction ใช้ 6 รอบ

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 15–21

### รอบ 4 · GPU

ท่องตัวเลข Fermi, ตาราง classifying GPUs และ perspective

**เกณฑ์ผ่าน:** ตอบ 16 lanes/32-wide/2 cycles และเทียบ cache/paging/coherence ได้

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 22–30

### รอบ 5 · Clusters, networks และ Quiz

เทียบ SMP vs message passing vs cluster vs grid; จำ topologies และ benchmarks; ทำ Quiz ทุกหัวข้อ

**เกณฑ์ผ่าน:** ตอบหัวข้อแดงครบและอธิบาย arithmetic intensity ได้

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 31–40

### ตัวเลือกเมื่อเวลาน้อย

- **ถ้าเหลือ 3 วัน:** วัน 1 หน้า 3–14 (taxonomy, SIMD, vector); วัน 2 หน้า 15–30 (multithreading, shared memory, GPU); วัน 3 หน้า 31–40 และทำ Quiz
- **ถ้าเหลือ 1 วัน:** ตารางหน้า 9 → vector/DAXPY หน้า 10–11 → multithreading หน้า 15–16 → SMP/reduction หน้า 19–21 → GPU หน้า 24–29 → message passing/clusters/topologies หน้า 31–36
- **ถ้าเหลือ 3 ชั่วโมง:** 0–40 นาที หน้า 3–14; 40–80 นาที หน้า 15–21; 80–130 นาที หน้า 22–30; 130–165 นาที หน้า 31–39; 165–180 นาทีสุ่ม Quiz

## 5. กลยุทธ์สอบและชุดคำถามฝึกตอบ

เน้นหัวข้อที่สไลด์ให้นิยาม ตารางจำแนก และตัวเลข เช่น SISD–MIMD, vector registers, multithreading, SMP/UMA/NUMA, Fermi, classifying GPUs และ topologies; ไม่มีข้อสอบเก่าจึงไม่ยืนยันโอกาสออกจริง

- **ควรท่องจำ:** ตาราง SISD/SIMD/MISD/MIMD, SPMD, fine/coarse/SMT, UMA/NUMA, VLIW/Superscalar/SIMD/Tesla, topologies 5 แบบ, benchmarks 5 ชุด (หน้า 9, 15–19, 28, 34, 37)
- **ควรฝึกโจทย์:** 64,000/64 = 1000 และรอบ reduction; DAXPY 512/8 = 64; Fermi 32/16 = 2 cycles; arithmetic intensity FLOPs/byte (หน้า 11, 20–21, 26, 39)
- **ควรเข้าใจแนวคิด:** ทำไม parallel software ยาก, vector หลบ control hazard, GPU ซ่อน latency ด้วย thread switching, shared memory vs message passing (หน้า 8, 12, 24, 19, 31)
- **เตรียมข้อสอบแบบผสม:** เลือกตอบจับคู่ศัพท์/ตัวอย่าง; อัตนัยเทียบสถาปัตยกรรม; คำนวณจากตัวเลขสไลด์; วิเคราะห์ภาพ multithreading, memory และ topologies (หน้า 3–40)

คำถามต่อไปนี้เป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง: เลือกตอบ 29 ข้อ, อัตนัย 29 ข้อ, วิเคราะห์ 23 ข้อ, คำนวณ 6 ข้อ

### Taxonomy ของ parallel processor architectures

**ข้อ 1 · เลือกตอบ: ในภาพหน้า 3 clusters อยู่ภายใต้กลุ่มใด?**

- A. MIMD → Distributed memory (loosely coupled)
- B. SIMD → Array processor
- C. MIMD → Shared memory
- D. SISD

เฉลย: Distributed memory (loosely coupled) ของ MIMD (หน้า 3)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 3

**ข้อ 2 · อัตนัย: SIMD แตกเป็นอะไรบ้างตามภาพ?**

เฉลย: Vector processor และ Array processor (หน้า 3)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 3

**ข้อ 3 · วิเคราะห์: เปรียบเทียบ SMP กับ clusters ตามตำแหน่งในต้นไม้หน้า 3**

เฉลย: SMP อยู่ใต้ shared memory (tightly coupled) ส่วน clusters อยู่ใต้ distributed memory (loosely coupled) ทั้งคู่เป็น MIMD

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 3

### Introduction: เป้าหมายของ multiprocessors

**ข้อ 4 · เลือกตอบ: ข้อใดคือ multicore microprocessor ตามสไลด์?**

- A. ชิปที่มีหลาย processor (cores)
- B. โปรแกรมเดียวบนหลายเครื่อง
- C. เครือข่าย Internet
- D. GPU เท่านั้น

เฉลย: Chips with multiple processors (cores) (หน้า 5)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 4–5

**ข้อ 5 · อัตนัย: ข้อดีของ multiprocessors 3 ข้อตามสไลด์คืออะไร?**

เฉลย: Scalability, availability, power efficiency (หน้า 5)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 4–5

**ข้อ 6 · วิเคราะห์: เว็บเซิร์ฟเวอร์ที่รับคำขออิสระจำนวนมากใช้ parallelism แบบใดตามหน้า 5?**

เฉลย: Task-level (process-level) parallelism เพราะให้ high throughput สำหรับ independent jobs

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 4–5

### Hardware และ software: serial/parallel, sequential/concurrent

**ข้อ 7 · เลือกตอบ: ตัวอย่าง concurrent software ในสไลด์คืออะไร?**

- A. Operating system
- B. Matrix multiplication
- C. Pentium 4
- D. Xeon e5345

เฉลย: Operating system (หน้า 6)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 6–7

**ข้อ 8 · อัตนัย: ความท้าทายหลักตามหน้า 6 คืออะไร?**

เฉลย: การใช้ parallel hardware ให้มีประสิทธิภาพ

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 6–7

**ข้อ 9 · วิเคราะห์: จัดหมวด “matrix multiplication บน quad-core Xeon e5345” ตามตาราง hardware/software หน้า 6**

เฉลย: Software: sequential, Hardware: parallel — สไลด์ระบุว่า sequential software รันบน parallel hardware ได้

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 6–7

### ความยากของการเขียน parallel program

**ข้อ 10 · เลือกตอบ: ข้อใดไม่ใช่ difficulty ตามหน้า 8?**

- A. Cache size
- B. Partitioning
- C. Coordination
- D. Communications overhead

เฉลย: Cache size ไม่อยู่ในรายการ (หน้า 8)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 8

**ข้อ 11 · อัตนัย: ทำไมถ้า parallel program ไม่เร็วขึ้นมาก ควรใช้ uniprocessor ที่เร็วกว่า?**

เฉลย: เพราะง่ายกว่า (สไลด์: “since it’s easier!”)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 8

**ข้อ 12 · วิเคราะห์: วิเคราะห์ว่า synch() ในหน้า 21 ตรงกับ difficulty ใดในหน้า 8**

เฉลย: Coordination — ต้องประสานจังหวะระหว่าง processor ก่อนแต่ละขั้น reduction

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 8

### Instruction/data streams และ SPMD

**ข้อ 13 · เลือกตอบ: ประเภทใดที่สไลด์ระบุว่า “No examples today”?**

- A. MISD
- B. SIMD
- C. MIMD
- D. SISD

เฉลย: MISD (หน้า 9)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 9

**ข้อ 14 · อัตนัย: SPMD คืออะไร?**

เฉลย: Single Program Multiple Data: parallel program บน MIMD ที่ใช้ conditional code ต่อ processor (หน้า 9)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 9

**ข้อ 15 · วิเคราะห์: Intel Xeon e5345 จัดอยู่ประเภทใด และสอดคล้องกับหน้า 6 อย่างไร?**

เฉลย: MIMD (หน้า 9) สอดคล้องกับหน้า 6 ที่ยกเป็น parallel hardware (quad-core)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 9

### Vector processors และ vector extension ของ RISC-V

**ข้อ 16 · เลือกตอบ: คำสั่งใดบวก scalar เข้ากับทุก element ของ vector?**

- A. fadd.d.vs
- B. fadd.d.v
- C. fld.v
- D. fsd.v

เฉลย: fadd.d.vs (หน้า 10)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 10

**ข้อ 17 · อัตนัย: Vector processor ช่วยลดอะไรอย่างมีนัยสำคัญตามสไลด์?**

เฉลย: Instruction-fetch bandwidth (หน้า 10)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 10

**ข้อ 18 · คำนวณ: คำนวณจำนวนบิตทั้งหมดใน vector register หนึ่งตัวของ RISC-V vector extension ตามหน้า 10**

เฉลย: 64 elements × 64 บิต = 4096 บิต (คำนวณจากตัวเลขในสไลด์)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 10

### ตัวอย่าง DAXPY: scalar loop เทียบ vector code

**ข้อ 19 · เลือกตอบ: โค้ด vector ของ DAXPY มีกี่คำสั่ง?**

- A. 6
- B. 8
- C. 10
- D. 64

เฉลย: 6 คำสั่ง (หน้า 11)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 11

**ข้อ 20 · อัตนัย: อธิบาย DAXPY ทำอะไร**

เฉลย: นำเวกเตอร์ X คูณด้วยสเกลาร์ a แล้วบวกกับ vector Y เก็บกลับใน Y (Y = aX + Y) (หน้า 11)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 11

**ข้อ 21 · คำนวณ: จงหาจำนวนรอบ loop ของโค้ด scalar จาก addi x5,x19,512 และ addi x19,x19,8**

เฉลย: 512 / 8 = 64 รอบ (ตรงกับ 64 elements ต่อ vector register หน้า 10)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 11

### Vector vs. scalar

**ข้อ 22 · เลือกตอบ: Vector หลีกเลี่ยง control hazard ได้อย่างไร?**

- A. หลีกเลี่ยง loop
- B. ใช้ cache ใหญ่
- C. เพิ่ม register
- D. ใช้ MISD

เฉลย: Avoid control hazards by avoiding loops (หน้า 12)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 12

**ข้อ 23 · อัตนัย: การระบุว่าไม่มี loop-carried dependence ช่วยอะไร?**

เฉลย: ลดการตรวจสอบใน hardware (reduced checking) (หน้า 12)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 12

**ข้อ 24 · วิเคราะห์: เปรียบเทียบ vector กับ MMX/SSE ตามหน้า 12**

เฉลย: vector ทั่วไปกว่า ad-hoc media extensions และเข้ากับ compiler technology ได้ดีกว่า

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 12

### SIMD

**ข้อ 25 · เลือกตอบ: MMX/SSE ใน x86 ใช้ register กว้างเท่าใดตามสไลด์?**

- A. 128 บิต
- B. 64 บิต
- C. 32 บิต
- D. 512 บิต

เฉลย: 128-bit wide registers (หน้า 13)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 13

**ข้อ 26 · อัตนัย: SIMD ช่วยเรื่อง synchronization อย่างไร?**

เฉลย: ทุก processor ทำคำสั่งเดียวกันในเวลาเดียวกัน จึง synchronize ง่าย (หน้า 13)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 13

**ข้อ 27 · วิเคราะห์: เปรียบเทียบ SIMD (หน้า 13) กับ SPMD บน MIMD (หน้า 9) ในด้านคำสั่งที่ processor ทำ**

เฉลย: SIMD: ทุก processor ทำคำสั่งเดียวกันพร้อมกัน; SPMD: โปรแกรมเดียวแต่ใช้ conditional code ให้แต่ละ processor ทำต่างกันได้

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 13

### Vector vs. multimedia extensions

**ข้อ 28 · เลือกตอบ: ข้อใดที่ vector รองรับแต่ multimedia extensions ไม่รองรับ?**

- A. Strided access
- B. Fixed width
- C. 128-bit register
- D. SIMD instruction

เฉลย: Strided access (หน้า 14)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 14

**ข้อ 29 · อัตนัย: ความกว้างของ vector instruction กับ multimedia extension ต่างกันอย่างไร?**

เฉลย: Vector: variable width; multimedia: fixed width (หน้า 14)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 14

**ข้อ 30 · วิเคราะห์: วิเคราะห์ว่าทำไม vector unit จึงเรียกว่า “combination of pipelined and arrayed functional units” จากภาพหน้า 14**

เฉลย: มีหลาย lanes วางขนานกัน (arrayed) และแต่ละ lane มี functional unit แบบ pipeline (FP add/mul pipe)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 14

### Hardware multithreading: fine-grain และ coarse-grain

**ข้อ 31 · เลือกตอบ: Coarse-grain multithreading สลับ thread เมื่อใด?**

- A. เมื่อ stall ยาว เช่น L2-cache miss
- B. ทุก cycle
- C. ไม่เคยสลับ
- D. เมื่อ branch

เฉลย: Only switch on long stall (หน้า 15)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 15

**ข้อ 32 · อัตนัย: ข้อเสียของ coarse-grain ตามสไลด์คืออะไร?**

เฉลย: ไม่ซ่อน short stalls เช่น data hazards (หน้า 15)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 15

**ข้อ 33 · วิเคราะห์: เปรียบเทียบ fine-grain และ coarse-grain ในด้าน hardware และการซ่อน stall**

เฉลย: Fine-grain สลับทุก cycle ซ่อน stall ได้ทั้งสั้นยาว; coarse-grain hardware ง่ายกว่าแต่ซ่อนได้เฉพาะ stall ยาว

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 15

### Simultaneous multithreading (SMT) และตัวอย่าง

**ข้อ 34 · เลือกตอบ: Pentium-4 HT แชร์อะไรระหว่าง 2 threads?**

- A. Function units และ caches
- B. Registers
- C. PC
- D. ไม่แชร์อะไร

เฉลย: Shared function units and caches (หน้า 16)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 16–17

**ข้อ 35 · อัตนัย: ภายใน thread เดียว SMT จัดการ dependency อย่างไร?**

เฉลย: ด้วย scheduling และ register renaming (หน้า 16)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 16–17

**ข้อ 36 · วิเคราะห์: วิเคราะห์ภาพหน้า 17 ว่าทำไม SMT ใช้ issue slots ได้เต็มกว่า fine MT**

เฉลย: SMT นำคำสั่งจากหลาย thread มาใส่ slot ใน cycle เดียวกัน ส่วน fine MT ใช้ thread เดียวต่อ cycle จึงเหลือ slot ว่าง

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 16–17

### Future of multithreading

**ข้อ 37 · เลือกตอบ: อะไรผลักให้ microarchitecture ง่ายขึ้นตามหน้า 18?**

- A. Power considerations
- B. Moore’s Law
- C. Clusters
- D. Grid computing

เฉลย: Power considerations (หน้า 18)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 18

**ข้อ 38 · อัตนัย: วิธีใดอาจมีประสิทธิภาพที่สุดในการทน cache-miss latency?**

เฉลย: Thread switch (หน้า 18)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 18

**ข้อ 39 · วิเคราะห์: วิเคราะห์ความเชื่อมโยงระหว่างหน้า 18 กับ multicore ในหน้า 5**

เฉลย: หน้า 18 เสนอว่า multiple simple cores อาจแชร์ทรัพยากรได้ดีกว่า ซึ่งตรงกับ multicore = ชิปที่มีหลาย cores (หน้า 5)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 18

### Shared memory multiprocessor (SMP), UMA และ NUMA

**ข้อ 40 · เลือกตอบ: SMP ใช้อะไร synchronize shared variables?**

- A. Locks
- B. Messages
- C. Interrupts
- D. Branch prediction

เฉลย: Locks (หน้า 19)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 19

**ข้อ 41 · อัตนัย: UMA กับ NUMA ต่างกันอย่างไร?**

เฉลย: ต่างกันที่ memory access time: UMA uniform, NUMA nonuniform (หน้า 19)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 19

**ข้อ 42 · วิเคราะห์: เปรียบเทียบ address space ของ SMP (หน้า 19) กับ message passing (หน้า 31)**

เฉลย: SMP: single physical address space ร่วมกัน; message passing: แต่ละ processor มี private physical address space และส่ง/รับ messages

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 19

### ตัวอย่าง sum reduction บน 64-processor UMA

**ข้อ 43 · เลือกตอบ: แต่ละ processor ได้ตัวเลขกี่ตัวในตัวอย่างหน้า 20?**

- A. 1000
- B. 64
- C. 64,000
- D. 100

เฉลย: 1000 (หน้า 20)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 20–21

**ข้อ 44 · อัตนัย: ทำไมต้องมี synch() ในแต่ละรอบ reduction?**

เฉลย: เพื่อให้ partial sums ของรอบก่อนเสร็จก่อนจะนำไปบวกต่อ (Need to synchronize between reduction steps, หน้า 20–21)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 20–21

**ข้อ 45 · คำนวณ: จงหาจำนวนรอบของ do–while ในโค้ดหน้า 21 เมื่อ half เริ่มที่ 64**

เฉลย: 6 รอบ: half = 32, 16, 8, 4, 2, 1 แล้วหยุดเมื่อ half > 1 เป็นเท็จ

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 20–21

### ประวัติ GPU และกราฟิกในระบบ

**ข้อ 46 · เลือกตอบ: งานใดเป็นงานของ GPU ตามหน้า 22?**

- A. Rasterization
- B. Linpack
- C. Message passing
- D. Grid computing

เฉลย: Rasterization (หน้า 22)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 22–23

**ข้อ 47 · อัตนัย: Moore’s Law ส่งผลต่อ 3D graphics อย่างไรตามสไลด์?**

เฉลย: ทำให้ราคาต่ำลงและความหนาแน่นสูงขึ้น จน 3D graphics cards ใช้ใน PC และเครื่องเกมได้ (หน้า 22)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 22–23

**ข้อ 48 · วิเคราะห์: จากภาพหน้า 23 GPU เชื่อมกับระบบผ่านอะไรในฝั่ง Intel CPU?**

เฉลย: x16 PCI-Express link ไปยัง North Bridge และมี GPU Memory แยก (ภาพหน้า 23)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 22–23

### GPU architectures

**ข้อ 49 · เลือกตอบ: GPU ซ่อน memory latency ด้วยวิธีใด?**

- A. Thread switching
- B. Multi-level caches ใหญ่
- C. Branch prediction
- D. Locks

เฉลย: Thread switching (หน้า 24)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 24

**ข้อ 50 · อัตนัย: ในระบบ heterogeneous CPU/GPU แบ่งงานอย่างไร?**

เฉลย: CPU ทำ sequential code, GPU ทำ parallel code (หน้า 24)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 24

**ข้อ 51 · วิเคราะห์: เปรียบเทียบการพึ่ง cache ของ GPU กับ multicore โดยใช้ข้อมูลหน้า 24 และ 29**

เฉลย: GPU พึ่ง multi-level caches น้อย (หน้า 24) สอดคล้องกับ largest cache 0.75 MB ของ GPU เทียบ 8 MB ของ multicore (หน้า 29)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 24

### ตัวอย่าง NVIDIA Fermi

**ข้อ 52 · เลือกตอบ: SIMD processor ของ Fermi มีกี่ SIMD lanes?**

- A. 16
- B. 32
- C. 64
- D. 8

เฉลย: 16 SIMD lanes (หน้า 26)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 25–26

**ข้อ 53 · อัตนัย: Register ต่อ thread context มีกี่ตัว?**

เฉลย: 64 registers per thread context (หน้า 26)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 25–26

**ข้อ 54 · คำนวณ: คำนวณจำนวน cycles ที่ SIMD instruction กว้าง 32 elements ใช้บน processor กว้าง 16**

เฉลย: 32 / 16 = 2 cycles (ตรงกับ “over 2 cycles” หน้า 26)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 25–26

### GPU memory structures

**ข้อ 55 · เลือกตอบ: Thread block ใช้ memory ระดับใดในภาพหน้า 27?**

- A. Per-block local memory
- B. Per-thread private memory
- C. Disk
- D. L2 cache

เฉลย: Per-Block Local Memory (หน้า 27)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 27

**ข้อ 56 · อัตนัย: ระหว่าง Grid 0 กับ Grid 1 มีอะไรตามภาพ?**

เฉลย: Inter-grid synchronization (หน้า 27)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 27

**ข้อ 57 · วิเคราะห์: วิเคราะห์ความสัมพันธ์ระหว่างระดับการทำงานกับระดับ memory ในภาพหน้า 27**

เฉลย: ยิ่งกลุ่มใหญ่ขึ้น (thread → block → grid) memory ที่ใช้ก็กว้างขึ้น (private → per-block local → GPU memory)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 27

### Classifying GPUs

**ข้อ 58 · เลือกตอบ: ช่อง Data-Level Parallelism + Dynamic ในตารางหน้า 28 คืออะไร?**

- A. Tesla Multiprocessor
- B. VLIW
- C. Superscalar
- D. SIMD or Vector

เฉลย: Tesla Multiprocessor (หน้า 28)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 28

**ข้อ 59 · อัตนัย: ทำไม conditional execution ใน GPU จึงเรียกว่า “illusion of MIMD”?**

เฉลย: ทำให้ thread ดูเหมือนทำคำสั่งต่างกันได้เหมือน MIMD แต่แลกกับ performance degradation (หน้า 28)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 28

**ข้อ 60 · วิเคราะห์: จัด VLIW และ Superscalar ตามตารางหน้า 28 และอธิบายเกณฑ์**

เฉลย: ทั้งคู่เป็น instruction-level parallelism; VLIW ค้นพบที่ compile time (static), Superscalar ค้นพบที่ runtime (dynamic)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 28

### Putting GPUs into perspective

**ข้อ 61 · เลือกตอบ: ข้อใดที่ GPU ไม่มีตามตารางหน้า 29?**

- A. Demand paging
- B. 64-bit memory address
- C. Memory protection at page level
- D. SIMD lanes

เฉลย: Demand paging: GPU = No (หน้า 29)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 29–30

**ข้อ 62 · อัตนัย: ขนาด largest cache ของ multicore และ GPU ต่างกันเท่าใด?**

เฉลย: Multicore 8 MB, GPU 0.75 MB (หน้า 29)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 29–30

**ข้อ 63 · คำนวณ: คำนวณว่า largest cache ของ multicore ใหญ่กว่า GPU กี่เท่าตามตารางหน้า 29**

เฉลย: 8 / 0.75 ≈ 10.7 เท่า

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 29–30

### Message passing

**ข้อ 64 · เลือกตอบ: ใน message passing processor แต่ละตัวมี address space แบบใด?**

- A. Private physical address space
- B. Single shared address space
- C. ไม่มี address space
- D. Virtual เท่านั้น

เฉลย: Private physical address space (หน้า 31)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 31

**ข้อ 65 · อัตนัย: Processor สื่อสารกันอย่างไรใน message passing?**

เฉลย: Hardware ส่งและรับ messages ระหว่าง processors (หน้า 31)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 31

**ข้อ 66 · วิเคราะห์: วิเคราะห์ความต่างของตำแหน่ง memory ในภาพหน้า 19 และ 31**

เฉลย: หน้า 19 memory ร่วมอยู่หลัง interconnection network; หน้า 31 memory แยกอยู่กับ processor แต่ละตัวก่อนต่อ network

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 31

### Loosely coupled clusters

**ข้อ 67 · เลือกตอบ: Cluster เชื่อมคอมพิวเตอร์ด้วยอะไรตามสไลด์?**

- A. I/O system เช่น Ethernet/switch
- B. Shared memory bus
- C. PCI-Express GPU
- D. Register file

เฉลย: I/O system: Ethernet/switch, Internet (หน้า 32)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 32

**ข้อ 68 · อัตนัย: ปัญหาของ cluster 2 ข้อตามหน้า 32 คืออะไร?**

เฉลย: Administration cost (ใช้ VMs ช่วย) และ low interconnect bandwidth

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 32

**ข้อ 69 · วิเคราะห์: ทำไม web server จึงเหมาะกับ cluster ตามหน้า 32?**

เฉลย: เพราะเป็นงาน independent tasks และ cluster ให้ high availability, scalable, affordable

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 32

### Grid computing

**ข้อ 70 · เลือกตอบ: ตัวอย่าง grid computing ตามสไลด์คือข้อใด?**

- A. SETI@home
- B. Linpack
- C. CUDA
- D. Pentium-4 HT

เฉลย: SETI@home, World Community Grid (หน้า 33)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 33

**ข้อ 71 · อัตนัย: Grid computing ใช้ทรัพยากรใดที่ปกติถูกปล่อยว่าง?**

เฉลย: Idle time on PCs (หน้า 33)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 33

**ข้อ 72 · วิเคราะห์: เปรียบเทียบการเชื่อมต่อของ grid (หน้า 33) กับ cluster (หน้า 32)**

เฉลย: Grid ใช้ long-haul networks เช่น Internet; cluster ใช้ I/O system เช่น Ethernet/switch (Internet ก็ยกเป็นตัวอย่างได้)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 33

### Interconnection network topologies และ multistage networks

**ข้อ 73 · เลือกตอบ: Topology ใดในหน้า 34 ที่ทุก node ต่อกันโดยตรง?**

- A. Fully connected
- B. Bus
- C. Ring
- D. 2D Mesh

เฉลย: Fully connected (หน้า 34)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 34–35

**ข้อ 74 · อัตนัย: Multistage networks ในหน้า 35 มีอะไรบ้าง?**

เฉลย: Crossbar, Omega network และ Omega network switch box

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 34–35

**ข้อ 75 · คำนวณ: คำนวณจำนวน nodes ของ N-cube เมื่อ N = 3 ตามภาพหน้า 34**

เฉลย: 2³ = 8 nodes

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 34–35

### Network characteristics

**ข้อ 76 · เลือกตอบ: ข้อใดอยู่ในกลุ่ม throughput ตามหน้า 36?**

- A. Bisection bandwidth
- B. Latency per message
- C. Cost
- D. Power

เฉลย: Bisection bandwidth (หน้า 36)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 36

**ข้อ 77 · อัตนัย: Throughput แบ่งเป็นอะไรบ้าง?**

เฉลย: Link bandwidth, total network bandwidth, bisection bandwidth (หน้า 36)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 36

**ข้อ 78 · วิเคราะห์: เปรียบเทียบ latency per message กับ congestion delays ตามหน้า 36**

เฉลย: Latency วัดบน unloaded network; congestion delays เกิดเพิ่มตาม traffic

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 36

### Parallel benchmarks และ code or applications

**ข้อ 79 · เลือกตอบ: Benchmark ใดใช้ Pthreads และ OpenMP?**

- A. PARSEC
- B. Linpack
- C. NAS
- D. SPECrate

เฉลย: PARSEC (หน้า 37)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 37–38

**ข้อ 80 · อัตนัย: ปัญหาของ traditional benchmarks ตามหน้า 38 คืออะไร?**

เฉลย: ใช้ code และ data sets คงที่ ขณะที่ parallel programming กำลังพัฒนา

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 37–38

**ข้อ 81 · วิเคราะห์: ถ้าต้องการวัด computational fluid dynamics kernels ควรเลือก benchmark ใด?**

เฉลย: NAS (NASA Advanced Supercomputing) suite (หน้า 37)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 37–38

### Modeling performance และ arithmetic intensity

**ข้อ 82 · เลือกตอบ: Peak memory bytes/sec วัดด้วยอะไรตามสไลด์?**

- A. Stream benchmark
- B. Data sheet
- C. Linpack
- D. SPECrate

เฉลย: Stream benchmark (หน้า 39)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 39

**ข้อ 83 · อัตนัย: ให้นิยาม arithmetic intensity**

เฉลย: FLOPs per byte of memory accessed (หน้า 39)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 39

**ข้อ 84 · วิเคราะห์: สำหรับคอมพิวเตอร์หนึ่งเครื่อง ต้องหาค่าอะไร 2 ค่า และได้มาจากแหล่งใด?**

เฉลย: Peak GFLOPS จาก data sheet และ peak memory bytes/sec จาก Stream benchmark (หน้า 39)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 39

### Concluding remarks

**ข้อ 85 · เลือกตอบ: อะไรขับเคลื่อนทั้ง mobile และ WSC ตามหน้า 40?**

- A. Performance per dollar และ per Joule
- B. จำนวน register
- C. ขนาด cache
- D. Clock rate

เฉลย: Performance per dollar and performance per Joule (หน้า 40)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 40

**ข้อ 86 · อัตนัย: ความยาก 2 ข้อตามหน้า 40 คืออะไร?**

เฉลย: Developing parallel software และ devising appropriate architectures

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 40

**ข้อ 87 · วิเคราะห์: ทำไม clusters จึงเข้ากับ SaaS ตามหน้า 32 และ 40?**

เฉลย: SaaS สำคัญขึ้น (หน้า 40) และ clusters เหมาะกับ independent tasks เช่น web servers พร้อม high availability, scalable, affordable (หน้า 32)

อ้างอิง: itds-211_comp_arch_Chapter08.pdf, หน้า 40

## ภาพสำคัญที่ใช้ในเว็บ

ภาพเป็นภาพสไลด์ต้นฉบับที่เรนเดอร์จาก PDF ไม่ใช่แผนภาพความรู้ที่สร้างขึ้นใหม่

- A Taxonomy of Parallel Processor Architectures · หน้า 3: ต้นไม้ SISD/SIMD/MISD/MIMD, SMP, NUMA, clusters (Figure 17.1, Pearson) (itds-211_comp_arch_Chapter08.pdf, หน้า 3) (itds-211_comp_arch_Chapter08.pdf, หน้า 3)
- Instruction and Data Streams · หน้า 9: ตาราง SISD/SIMD/MISD/MIMD และ SPMD (itds-211_comp_arch_Chapter08.pdf, หน้า 9) (itds-211_comp_arch_Chapter08.pdf, หน้า 9)
- Example: DAXPY · หน้า 11: โค้ด RISC-V แบบ loop เทียบ vector code และคำอธิบาย DAXPY (itds-211_comp_arch_Chapter08.pdf, หน้า 11) (itds-211_comp_arch_Chapter08.pdf, หน้า 11)
- Vector vs. Multimedia Extensions · หน้า 14: vector unit แบบ lanes ผสม pipelined/arrayed (itds-211_comp_arch_Chapter08.pdf, หน้า 14) (itds-211_comp_arch_Chapter08.pdf, หน้า 14)
- Multithreading Example · หน้า 17: issue slots ของ Coarse MT, Fine MT และ SMT (itds-211_comp_arch_Chapter08.pdf, หน้า 17) (itds-211_comp_arch_Chapter08.pdf, หน้า 17)
- Shared Memory · หน้า 19: processor/cache ต่อ interconnection network ไป memory และ I/O (itds-211_comp_arch_Chapter08.pdf, หน้า 19) (itds-211_comp_arch_Chapter08.pdf, หน้า 19)
- Example: Sum Reduction · หน้า 20: แบ่ง 64,000 ตัวให้ 64 processors และโค้ดรวมผลขั้นแรก (itds-211_comp_arch_Chapter08.pdf, หน้า 20) (itds-211_comp_arch_Chapter08.pdf, หน้า 20)
- Example: Sum Reduction · หน้า 21: โค้ด reduction และต้นไม้ half = 4, 2, 1 (itds-211_comp_arch_Chapter08.pdf, หน้า 21) (itds-211_comp_arch_Chapter08.pdf, หน้า 21)
- Graphics in the System · หน้า 23: ตำแหน่ง GPU, North Bridge และ GPU memory ในระบบ (itds-211_comp_arch_Chapter08.pdf, หน้า 23) (itds-211_comp_arch_Chapter08.pdf, หน้า 23)
- Example: NVIDIA Fermi · หน้า 25: SIMD processor 16 lanes, registers, load/store units, local memory 64 KiB (itds-211_comp_arch_Chapter08.pdf, หน้า 25) (itds-211_comp_arch_Chapter08.pdf, หน้า 25)
- GPU Memory Structures · หน้า 27: CUDA thread, thread block, grid และ memory แต่ละระดับ (itds-211_comp_arch_Chapter08.pdf, หน้า 27) (itds-211_comp_arch_Chapter08.pdf, หน้า 27)
- Classifying GPUs · หน้า 28: ตาราง ILP/DLP × static/dynamic (itds-211_comp_arch_Chapter08.pdf, หน้า 28) (itds-211_comp_arch_Chapter08.pdf, หน้า 28)
- Putting GPUs into Perspective · หน้า 29: ตารางเทียบ multicore with SIMD กับ GPU (itds-211_comp_arch_Chapter08.pdf, หน้า 29) (itds-211_comp_arch_Chapter08.pdf, หน้า 29)
- Guide to GPU Terms · หน้า 30: ตารางศัพท์ GPU (ตัวอักษรเล็ก ต้องตรวจสอบจากต้นฉบับ) (itds-211_comp_arch_Chapter08.pdf, หน้า 30) (itds-211_comp_arch_Chapter08.pdf, หน้า 30)
- Message Passing · หน้า 31: processor/cache/memory ของแต่ละตัวต่อ interconnection network (itds-211_comp_arch_Chapter08.pdf, หน้า 31) (itds-211_comp_arch_Chapter08.pdf, หน้า 31)
- Interconnection Networks · หน้า 34: bus, ring, 2D mesh, N-cube (N = 3), fully connected (itds-211_comp_arch_Chapter08.pdf, หน้า 34) (itds-211_comp_arch_Chapter08.pdf, หน้า 34)
- Multistage Networks · หน้า 35: crossbar, Omega network, Omega switch box (itds-211_comp_arch_Chapter08.pdf, หน้า 35) (itds-211_comp_arch_Chapter08.pdf, หน้า 35)
