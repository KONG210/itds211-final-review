"""Chapter08 notes, questions and figure map from the supplied 41-page PDF."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = 'itds-211_comp_arch_Chapter08.pdf'
topics = []


def add(id, title, level, pages, summary, remember, terms, example, confusion, mnemonic, quiz, image_pages=(), comparison=None, formulas=None, worked=None):
    assert len(quiz) == 3
    m, a, b = quiz
    questions = [
        dict(type='เลือกตอบ', q=m[0], options=m[1], correct=m[2], answer=m[3], pages=pages),
        dict(type='อัตนัย', q=a[0], answer=a[1], pages=pages),
        dict(type='คำนวณ' if any(x in b[0] for x in ('คำนวณ', 'จงหา', 'เท่าไร')) else 'วิเคราะห์', q=b[0], answer=b[1], pages=pages),
    ]
    entry = dict(id=id, title=title, level=level, pages=pages,
        reason={'core':'เป็นนิยาม การจำแนก หรือกลไกหลักของ parallel processor ที่สไลด์ใช้ต่อยอด',
                'important':'เป็นตัวอย่าง การเปรียบเทียบ หรือการประยุกต์แนวคิดหลัก',
                'extra':'เป็นภาพรวม ประวัติ หรือข้อสรุปประกอบ'}[level],
        summary=summary, remember=remember, terms=terms, example=example,
        confusion=confusion, mnemonic=mnemonic, questions=questions,
        figures=[f'fig-{p}' for p in image_pages])
    if comparison: entry['comparison'] = dict(headers=comparison[0], rows=comparison[1])
    if formulas: entry['formulas'] = formulas
    if worked: entry['worked'] = worked
    topics.append(entry)


add('processor-taxonomy','Taxonomy ของ parallel processor architectures','important','หน้า 3',
    'ภาพหน้า 3 (Figure 17.1 จาก Pearson) แบ่ง processor organizations เป็น SISD, SIMD, MISD และ MIMD. SISD คือ uniprocessor; SIMD แตกเป็น vector processor และ array processor; MIMD แตกเป็น shared memory (tightly coupled) ซึ่งมี SMP และ NUMA กับ distributed memory (loosely coupled) ซึ่งคือ clusters.',
    ['SISD → Uniprocessor (หน้า 3)','SIMD → Vector processor, Array processor (หน้า 3)','MIMD → Shared memory (tightly coupled): SMP, NUMA (หน้า 3)','MIMD → Distributed memory (loosely coupled): Clusters (หน้า 3)'],
    ['SISD','SIMD','MISD','MIMD','SMP','NUMA','clusters','tightly coupled','loosely coupled'],
    'ใช้ต้นไม้หน้า 3 เป็นแผนที่ของบท: SIMD/vector (หน้า 9–14), shared memory (หน้า 19–21), clusters (หน้า 31–33)',
    'Tightly coupled = shared memory; loosely coupled = distributed memory/clusters อย่าสลับกัน',
    'MIMD แยกสองทาง: แชร์ memory (แน่น) หรือแยก memory (หลวม)',
    [('ในภาพหน้า 3 clusters อยู่ภายใต้กลุ่มใด?',['MIMD → Distributed memory (loosely coupled)','SIMD → Array processor','MIMD → Shared memory','SISD'],0,'Distributed memory (loosely coupled) ของ MIMD (หน้า 3)'),
     ('SIMD แตกเป็นอะไรบ้างตามภาพ?','Vector processor และ Array processor (หน้า 3)'),
     ('เปรียบเทียบ SMP กับ clusters ตามตำแหน่งในต้นไม้หน้า 3','SMP อยู่ใต้ shared memory (tightly coupled) ส่วน clusters อยู่ใต้ distributed memory (loosely coupled) ทั้งคู่เป็น MIMD')],(3,))

add('introduction','Introduction: เป้าหมายของ multiprocessors','core','หน้า 4–5',
    'เป้าหมายคือเชื่อมหลายคอมพิวเตอร์เพื่อให้ได้ประสิทธิภาพสูงขึ้น. Multiprocessors ให้ scalability, availability และ power efficiency. Task-level (process-level) parallelism ให้ throughput สูงสำหรับงานอิสระ; parallel processing program คือโปรแกรมเดียวที่รันบนหลาย processor; multicore microprocessor คือชิปที่มีหลาย processor (cores).',
    ['Goal: connecting multiple computers to get higher performance (หน้า 5)','Multiprocessors: scalability, availability, power efficiency (หน้า 5)','Task-level parallelism: high throughput for independent jobs (หน้า 5)','Parallel processing program: single program on multiple processors (หน้า 5)','Multicore: chips with multiple processors (cores) (หน้า 5)'],
    ['multiprocessor','task-level (process-level) parallelism','parallel processing program','multicore','scalability','availability'],
    'Chapter overview หน้า 4 เรียงหัวข้อ: difficulty → SISD/MIMD/SIMD/SPMD/Vector → multithreading → shared memory → GPUs → clusters → network topologies',
    'Task-level parallelism คือหลายงานอิสระ; parallel processing program คือโปรแกรมเดียวแบ่งไปหลาย processor',
    'หลายงานอิสระ = task-level; งานเดียวแบ่งช่วย = parallel program',
    [('ข้อใดคือ multicore microprocessor ตามสไลด์?',['ชิปที่มีหลาย processor (cores)','โปรแกรมเดียวบนหลายเครื่อง','เครือข่าย Internet','GPU เท่านั้น'],0,'Chips with multiple processors (cores) (หน้า 5)'),
     ('ข้อดีของ multiprocessors 3 ข้อตามสไลด์คืออะไร?','Scalability, availability, power efficiency (หน้า 5)'),
     ('เว็บเซิร์ฟเวอร์ที่รับคำขออิสระจำนวนมากใช้ parallelism แบบใดตามหน้า 5?','Task-level (process-level) parallelism เพราะให้ high throughput สำหรับ independent jobs')])

add('hardware-software','Hardware และ software: serial/parallel, sequential/concurrent','important','หน้า 6–7',
    'Hardware แบ่งเป็น serial (เช่น Pentium 4) และ parallel (เช่น quad-core Xeon e5345). Software แบ่งเป็น sequential (เช่น matrix multiplication) และ concurrent (เช่น operating system). software ทั้งสองแบบรันได้บน hardware ทั้งสองแบบ ความท้าทายคือใช้ parallel hardware ให้มีประสิทธิภาพ. หน้า 7 ทบทวนหัวข้อ parallelism ที่เคยเรียน: synchronization, subword parallelism, ILP และ cache coherence.',
    ['Serial HW: Pentium 4; Parallel HW: quad-core Xeon e5345 (หน้า 6)','Sequential SW: matrix multiplication; Concurrent SW: operating system (หน้า 6)','Challenge: making effective use of parallel hardware (หน้า 6)','Covered: synchronization, subword parallelism, ILP, cache coherence (หน้า 7)'],
    ['serial hardware','parallel hardware','sequential software','concurrent software','cache coherence','subword parallelism'],
    'matrix multiplication เป็น sequential software ได้ แต่ก็รันบน parallel hardware ได้ตามหน้า 6',
    'Sequential/concurrent อธิบาย software; serial/parallel อธิบาย hardware',
    'Hardware: serial/parallel · Software: sequential/concurrent',
    [('ตัวอย่าง concurrent software ในสไลด์คืออะไร?',['Operating system','Matrix multiplication','Pentium 4','Xeon e5345'],0,'Operating system (หน้า 6)'),
     ('ความท้าทายหลักตามหน้า 6 คืออะไร?','การใช้ parallel hardware ให้มีประสิทธิภาพ'),
     ('จัดหมวด “matrix multiplication บน quad-core Xeon e5345” ตามตาราง hardware/software หน้า 6','Software: sequential, Hardware: parallel — สไลด์ระบุว่า sequential software รันบน parallel hardware ได้')],(),
    comparison=(['','Serial HW','Parallel HW'],[['Sequential SW','matrix multiply บน Pentium 4','matrix multiply บน Xeon e5345'],['Concurrent SW','OS บน Pentium 4','OS บน Xeon e5345']]))

add('parallel-programming','ความยากของการเขียน parallel program','core','หน้า 8',
    'ปัญหาอยู่ที่ parallel software: ต้องได้ performance improvement อย่างมีนัยสำคัญ ไม่เช่นนั้นใช้ uniprocessor ที่เร็วขึ้นจะง่ายกว่า. ความยากหลักคือ partitioning, coordination และ communications overhead.',
    ['Parallel software is the problem (หน้า 8)','ต้องได้ significant performance improvement มิฉะนั้นใช้ faster uniprocessor (หน้า 8)','Difficulties: partitioning, coordination, communications overhead (หน้า 8)'],
    ['partitioning','coordination','communications overhead','uniprocessor'],
    'ตัวอย่าง sum reduction หน้า 20–21 ต้อง partition ข้อมูล, synch() เพื่อ coordination และรวมผลระหว่าง processor',
    'ปัญหาที่สไลด์เน้นคือ software ไม่ใช่การหา hardware',
    'แบ่ง–ประสาน–สื่อสาร (P-C-C)',
    [('ข้อใดไม่ใช่ difficulty ตามหน้า 8?',['Cache size','Partitioning','Coordination','Communications overhead'],0,'Cache size ไม่อยู่ในรายการ (หน้า 8)'),
     ('ทำไมถ้า parallel program ไม่เร็วขึ้นมาก ควรใช้ uniprocessor ที่เร็วกว่า?','เพราะง่ายกว่า (สไลด์: “since it’s easier!”)'),
     ('วิเคราะห์ว่า synch() ในหน้า 21 ตรงกับ difficulty ใดในหน้า 8','Coordination — ต้องประสานจังหวะระหว่าง processor ก่อนแต่ละขั้น reduction')])

add('instruction-data-streams','Instruction/data streams และ SPMD','core','หน้า 9',
    'จำแนกตามจำนวน instruction stream และ data stream: SISD (Intel Pentium 4), SIMD (SSE instructions ของ x86), MISD (ไม่มีตัวอย่างในปัจจุบัน) และ MIMD (Intel Xeon e5345). SPMD (Single Program Multiple Data) คือ parallel program บน MIMD computer ที่ใช้ conditional code ให้ processor ต่างกันทำงานต่างกัน.',
    ['SISD: Intel Pentium 4; SIMD: SSE of x86 (หน้า 9)','MISD: no examples today; MIMD: Intel Xeon e5345 (หน้า 9)','SPMD: parallel program on a MIMD computer (หน้า 9)','SPMD ใช้ conditional code for different processors (หน้า 9)'],
    ['SISD','SIMD','MISD','MIMD','SPMD','instruction stream','data stream'],
    'โค้ด sum reduction หน้า 21 ใช้ if (Pn < half) แยกงานตาม processor — ตรงกับลักษณะ SPMD',
    'SPMD ไม่ใช่ประเภทฮาร์ดแวร์ในตาราง 2×2 แต่เป็นรูปแบบโปรแกรมบน MIMD',
    'S/M ตัวแรก = instruction, S/M ตัวหลัง = data',
    [('ประเภทใดที่สไลด์ระบุว่า “No examples today”?',['MISD','SIMD','MIMD','SISD'],0,'MISD (หน้า 9)'),
     ('SPMD คืออะไร?','Single Program Multiple Data: parallel program บน MIMD ที่ใช้ conditional code ต่อ processor (หน้า 9)'),
     ('Intel Xeon e5345 จัดอยู่ประเภทใด และสอดคล้องกับหน้า 6 อย่างไร?','MIMD (หน้า 9) สอดคล้องกับหน้า 6 ที่ยกเป็น parallel hardware (quad-core)')],(9,),
    comparison=(['Instruction \\ Data','Single','Multiple'],[['Single','SISD: Intel Pentium 4','SIMD: SSE instructions of x86'],['Multiple','MISD: No examples today','MIMD: Intel Xeon e5345']]))

add('vector-processors','Vector processors และ vector extension ของ RISC-V','core','หน้า 10',
    'Vector processor ใช้ function units ที่ pipeline สูง และ stream ข้อมูลระหว่าง vector registers กับ units: ดึงข้อมูลจาก memory เข้า registers แล้วเก็บผลจาก registers กลับ memory. ตัวอย่าง vector extension ของ RISC-V มี v0–v31 เป็น 32 registers แต่ละตัวมี 64 elements (element ละ 64 บิต) และคำสั่ง fld.v/fsd.v, fadd.d.v, fadd.d.vs ซึ่งลด instruction-fetch bandwidth อย่างมาก.',
    ['Highly pipelined function units (หน้า 10)','v0–v31: 32 × 64-element registers, 64-bit elements (หน้า 10)','fld.v, fsd.v: load/store vector; fadd.d.v: add vectors; fadd.d.vs: add scalar to each element (หน้า 10)','Significantly reduces instruction-fetch bandwidth (หน้า 10)'],
    ['vector register','fld.v','fsd.v','fadd.d.v','fadd.d.vs','instruction-fetch bandwidth'],
    'fadd.d.vs บวก scalar เข้ากับทุก element ของ vector; fadd.d.v บวก vector กับ vector',
    'v0–v31 คือ 32 registers ไม่ใช่ 32 elements; แต่ละ register มี 64 elements',
    '.v = vector กับ vector, .vs = vector กับ scalar',
    [('คำสั่งใดบวก scalar เข้ากับทุก element ของ vector?',['fadd.d.vs','fadd.d.v','fld.v','fsd.v'],0,'fadd.d.vs (หน้า 10)'),
     ('Vector processor ช่วยลดอะไรอย่างมีนัยสำคัญตามสไลด์?','Instruction-fetch bandwidth (หน้า 10)'),
     ('คำนวณจำนวนบิตทั้งหมดใน vector register หนึ่งตัวของ RISC-V vector extension ตามหน้า 10','64 elements × 64 บิต = 4096 บิต (คำนวณจากตัวเลขในสไลด์)')],(),
    formulas=[dict(expr='1 vector register = 64 elements × 64 bits = 4096 bits\nv0–v31 = 32 registers',description='คำนวณจากข้อกำหนดหน้า 10',pages='หน้า 10')])

add('daxpy','ตัวอย่าง DAXPY: scalar loop เทียบ vector code','core','หน้า 11',
    'DAXPY (Y = a × X + Y) คือคำสั่ง linear algebra ใน library BLAS (double-precision A*X Plus Y). โค้ด RISC-V แบบปกติใช้ loop ที่ load x[i], คูณ a, load y[i], บวก, store y[i] และเพิ่ม index ทีละ 8 จนถึง x19+512. โค้ด vector ทำงานเดียวกันด้วย 6 คำสั่ง: fld, fld.v, fmul.d.vs, fld.v, fadd.d.v, fsd.v โดยไม่มี loop.',
    ['DAXPY = double-precision A*X Plus Y ใน BLAS (หน้า 11)','Conventional: loop 8 คำสั่ง (fld, fmul.d, fld, fadd.d, fsd, addi, addi, bltu) (หน้า 11)','Vector: 6 คำสั่ง ไม่มี loop (หน้า 11)','addi x5,x19,512 = end of array X; index เพิ่มทีละ 8 (หน้า 11)'],
    ['DAXPY','BLAS','fmul.d.vs','fadd.d.v','loop'],
    'C: for (i = 0; i < n; i++) y[i] = a * x[i] + y[i];',
    'fmul.d.vs คูณ vector กับ scalar a; fadd.d.v บวก vector กับ vector',
    'scalar วนทีละตัว, vector ทำทีเดียวทั้งแถว',
    [('โค้ด vector ของ DAXPY มีกี่คำสั่ง?',['6','8','10','64'],0,'6 คำสั่ง (หน้า 11)'),
     ('อธิบาย DAXPY ทำอะไร','นำเวกเตอร์ X คูณด้วยสเกลาร์ a แล้วบวกกับ vector Y เก็บกลับใน Y (Y = aX + Y) (หน้า 11)'),
     ('จงหาจำนวนรอบ loop ของโค้ด scalar จาก addi x5,x19,512 และ addi x19,x19,8','512 / 8 = 64 รอบ (ตรงกับ 64 elements ต่อ vector register หน้า 10)')],(11,),
    worked=[dict(title='นับรอบ loop ของ DAXPY แบบ scalar (หน้า 11)',steps=['x5 = x19 + 512 คือจุดสิ้นสุดของ array X','ทุกรอบ addi x19,x19,8 เลื่อน index ไป 8 ไบต์ (double หนึ่งตัว)','bltu x19,x5,loop วนจนกว่า x19 ถึง x5'],answer='512 / 8 = 64 รอบ; vector code แทนด้วย 6 คำสั่งไม่มี loop',pages='หน้า 10–11')])

add('vector-vs-scalar','Vector vs. scalar','important','หน้า 12',
    'Vector architecture และ compiler ทำให้เขียน data-parallel program ง่ายขึ้น: ระบุชัดว่าไม่มี loop-carried dependence จึงลดการตรวจใน hardware, access pattern ที่สม่ำเสมอได้ประโยชน์จาก interleaved และ burst memory, และหลีกเลี่ยง control hazard เพราะไม่มี loop. vector ยังทั่วไปกว่า media extension เฉพาะกิจ (MMX, SSE) และเข้ากับ compiler technology ได้ดีกว่า.',
    ['Explicit absence of loop-carried dependences → reduced checking in hardware (หน้า 12)','Regular access patterns benefit from interleaved and burst memory (หน้า 12)','Avoid control hazards by avoiding loops (หน้า 12)','More general than MMX, SSE; better match with compiler technology (หน้า 12)'],
    ['loop-carried dependence','interleaved memory','burst memory','control hazard','MMX','SSE'],
    'เชื่อมกับ Chapter07: ไม่มี loop = ไม่มี branch ของ loop = ไม่มี control hazard จาก loop',
    'ข้อดีเรื่อง control hazard มาจากการไม่มี loop ไม่ใช่จาก branch prediction',
    'ไม่มี loop: ไม่มี dependence ข้ามรอบ ไม่มี branch',
    [('Vector หลีกเลี่ยง control hazard ได้อย่างไร?',['หลีกเลี่ยง loop','ใช้ cache ใหญ่','เพิ่ม register','ใช้ MISD'],0,'Avoid control hazards by avoiding loops (หน้า 12)'),
     ('การระบุว่าไม่มี loop-carried dependence ช่วยอะไร?','ลดการตรวจสอบใน hardware (reduced checking) (หน้า 12)'),
     ('เปรียบเทียบ vector กับ MMX/SSE ตามหน้า 12','vector ทั่วไปกว่า ad-hoc media extensions และเข้ากับ compiler technology ได้ดีกว่า')])

add('simd','SIMD','core','หน้า 13',
    'SIMD ทำงานแบบ elementwise บน vector ของข้อมูล เช่น MMX และ SSE ใน x86 ที่มีหลาย data elements ใน register กว้าง 128 บิต. processor ทุกตัวทำคำสั่งเดียวกันในเวลาเดียวกันแต่ใช้ data address ต่างกัน ทำให้ synchronization ง่ายขึ้น ใช้ instruction control hardware น้อยลง และเหมาะกับงานที่ data-parallel สูง.',
    ['Operate elementwise on vectors of data (หน้า 13)','MMX/SSE: multiple data elements in 128-bit registers (หน้า 13)','All processors execute same instruction at same time, different data address (หน้า 13)','Simplifies synchronization; reduced instruction control hardware (หน้า 13)','Works best for highly data-parallel applications (หน้า 13)'],
    ['SIMD','elementwise','MMX','SSE','128-bit register','data-parallel'],
    'MMX/SSE ใส่หลาย data elements ลงใน register 128 บิต แล้วคำสั่งเดียวทำกับทุก element พร้อมกัน',
    'SIMD ทุก processor ทำคำสั่งเดียวกัน; ถ้าต้องการคำสั่งต่างกันคือ MIMD',
    'คำสั่งเดียว ข้อมูลหลายชุด เดินพร้อมกัน',
    [('MMX/SSE ใน x86 ใช้ register กว้างเท่าใดตามสไลด์?',['128 บิต','64 บิต','32 บิต','512 บิต'],0,'128-bit wide registers (หน้า 13)'),
     ('SIMD ช่วยเรื่อง synchronization อย่างไร?','ทุก processor ทำคำสั่งเดียวกันในเวลาเดียวกัน จึง synchronize ง่าย (หน้า 13)'),
     ('เปรียบเทียบ SIMD (หน้า 13) กับ SPMD บน MIMD (หน้า 9) ในด้านคำสั่งที่ processor ทำ','SIMD: ทุก processor ทำคำสั่งเดียวกันพร้อมกัน; SPMD: โปรแกรมเดียวแต่ใช้ conditional code ให้แต่ละ processor ทำต่างกันได้')])

add('vector-vs-multimedia','Vector vs. multimedia extensions','important','หน้า 14',
    'Vector instructions มีความกว้าง vector ที่เปลี่ยนได้ (variable) ส่วน multimedia extensions มีความกว้างคงที่ (fixed). vector รองรับ strided access แต่ multimedia extensions ไม่รองรับ. vector unit อาจเป็นการผสมระหว่าง pipelined และ arrayed functional units ตามภาพที่แบ่งเป็น lanes.',
    ['Vector: variable width; multimedia: fixed width (หน้า 14)','Vector supports strided access; multimedia does not (หน้า 14)','Vector units = pipelined + arrayed functional units (หน้า 14)'],
    ['variable vector width','fixed width','strided access','lane','arrayed functional units'],
    'ภาพหน้า 14 แสดง vector unit แบบ 4 lanes แต่ละ lane มี FP add/FP mul pipe และ vector registers ส่วนหนึ่ง',
    'ภาพขวาหน้า 14 ถูกตัดขอบบางส่วน รายละเอียดเลข lane: ต้องตรวจสอบจากต้นฉบับ',
    'Vector ยืดได้ กระโดดได้; multimedia คงที่',
    [('ข้อใดที่ vector รองรับแต่ multimedia extensions ไม่รองรับ?',['Strided access','Fixed width','128-bit register','SIMD instruction'],0,'Strided access (หน้า 14)'),
     ('ความกว้างของ vector instruction กับ multimedia extension ต่างกันอย่างไร?','Vector: variable width; multimedia: fixed width (หน้า 14)'),
     ('วิเคราะห์ว่าทำไม vector unit จึงเรียกว่า “combination of pipelined and arrayed functional units” จากภาพหน้า 14','มีหลาย lanes วางขนานกัน (arrayed) และแต่ละ lane มี functional unit แบบ pipeline (FP add/mul pipe)')],(14,),
    comparison=(['คุณสมบัติ','Vector','Multimedia extensions'],[['ความกว้าง','variable','fixed'],['Strided access','รองรับ','ไม่รองรับ']]))

add('multithreading','Hardware multithreading: fine-grain และ coarse-grain','core','หน้า 15',
    'Multithreading คือทำหลาย thread ขนานกันโดย replicate registers, PC ฯลฯ และสลับ thread ได้เร็ว. Fine-grain สลับ thread ทุก cycle (interleave) ถ้า thread หนึ่ง stall ก็ทำ thread อื่น. Coarse-grain สลับเฉพาะ stall ยาว (เช่น L2-cache miss) ทำให้ hardware ง่ายแต่ซ่อน stall สั้น (เช่น data hazard) ไม่ได้.',
    ['Replicate registers, PC; fast switching (หน้า 15)','Fine-grain: switch after each cycle; interleave; if one stalls, others execute (หน้า 15)','Coarse-grain: switch only on long stall เช่น L2-cache miss (หน้า 15)','Coarse-grain: simpler HW แต่ไม่ซ่อน short stalls (data hazards) (หน้า 15)'],
    ['multithreading','fine-grain multithreading','coarse-grain multithreading','thread switching','L2-cache miss','stall'],
    'ภาพหน้า 17 แถว Fine MT สลับสีทุกแถว (cycle) ส่วน Coarse MT ทำ thread เดียวนานจนเกิด stall ยาวจึงเปลี่ยน',
    'Coarse-grain ไม่ซ่อน data hazard สั้น ๆ เพราะสลับเฉพาะ stall ยาว',
    'Fine ละเอียด สลับทุกจังหวะ; Coarse หยาบ สลับตอนรอนาน',
    [('Coarse-grain multithreading สลับ thread เมื่อใด?',['เมื่อ stall ยาว เช่น L2-cache miss','ทุก cycle','ไม่เคยสลับ','เมื่อ branch'],0,'Only switch on long stall (หน้า 15)'),
     ('ข้อเสียของ coarse-grain ตามสไลด์คืออะไร?','ไม่ซ่อน short stalls เช่น data hazards (หน้า 15)'),
     ('เปรียบเทียบ fine-grain และ coarse-grain ในด้าน hardware และการซ่อน stall','Fine-grain สลับทุก cycle ซ่อน stall ได้ทั้งสั้นยาว; coarse-grain hardware ง่ายกว่าแต่ซ่อนได้เฉพาะ stall ยาว')],(),
    comparison=(['แบบ','สลับ thread เมื่อ','ข้อดี/ข้อจำกัด'],[['Fine-grain','ทุก cycle','thread อื่นทำงานเมื่อ thread หนึ่ง stall'],['Coarse-grain','stall ยาว (L2 miss)','hardware ง่าย แต่ไม่ซ่อน short stall']]))

add('smt','Simultaneous multithreading (SMT) และตัวอย่าง','core','หน้า 16–17',
    'SMT ใช้ใน multiple-issue dynamically scheduled processor: schedule คำสั่งจากหลาย thread พร้อมกัน คำสั่งจาก thread อิสระทำงานเมื่อ function unit ว่าง ภายใน thread ใช้ scheduling และ register renaming จัดการ dependency. ตัวอย่าง Intel Pentium-4 HT มี 2 threads ที่ duplicate registers แต่แชร์ function units และ caches. ภาพหน้า 17 เทียบ issue slots ของ Coarse MT, Fine MT และ SMT.',
    ['SMT ใน multiple-issue dynamically scheduled processor (หน้า 16)','Schedule instructions from multiple threads; execute when function units available (หน้า 16)','Within threads: scheduling and register renaming (หน้า 16)','Pentium-4 HT: 2 threads, duplicated registers, shared function units and caches (หน้า 16)','ภาพ issue slots: Coarse MT, Fine MT, SMT (หน้า 17)'],
    ['simultaneous multithreading (SMT)','multiple-issue','dynamic scheduling','register renaming','issue slot','Hyper-Threading (HT)'],
    'ภาพหน้า 17: SMT เติม issue slots ในแถวเดียวกันด้วยคำสั่งจากหลาย thread ขณะที่ fine/coarse MT ใช้ thread เดียวต่อแถว',
    'SMT ต่างจาก fine-grain ที่ fine-grain สลับ thread ระหว่าง cycle แต่ SMT ผสมหลาย thread ใน cycle เดียว',
    'SMT = หลาย thread ใน cycle เดียว',
    [('Pentium-4 HT แชร์อะไรระหว่าง 2 threads?',['Function units และ caches','Registers','PC','ไม่แชร์อะไร'],0,'Shared function units and caches (หน้า 16)'),
     ('ภายใน thread เดียว SMT จัดการ dependency อย่างไร?','ด้วย scheduling และ register renaming (หน้า 16)'),
     ('วิเคราะห์ภาพหน้า 17 ว่าทำไม SMT ใช้ issue slots ได้เต็มกว่า fine MT','SMT นำคำสั่งจากหลาย thread มาใส่ slot ใน cycle เดียวกัน ส่วน fine MT ใช้ thread เดียวต่อ cycle จึงเหลือ slot ว่าง')],(17,))

add('future-multithreading','Future of multithreading','extra','หน้า 18',
    'สไลด์ตั้งคำถามว่า multithreading จะอยู่รอดหรือไม่และในรูปแบบใด. ข้อพิจารณาเรื่อง power ทำให้ microarchitecture เรียบง่ายขึ้น จึงใช้ multithreading แบบง่ายขึ้น; การทน cache-miss latency อาจใช้ thread switch ได้ดีที่สุด; และ multiple simple cores อาจแชร์ทรัพยากรได้มีประสิทธิภาพกว่า.',
    ['Power considerations ⇒ simplified microarchitectures (หน้า 18)','Simpler forms of multithreading (หน้า 18)','Tolerating cache-miss latency: thread switch may be most effective (หน้า 18)','Multiple simple cores might share resources more effectively (หน้า 18)'],
    ['power considerations','cache-miss latency','thread switch','simple cores'],
    'เชื่อมกับหน้า 15: thread switch เมื่อ cache miss คือแนวคิดของ coarse-grain',
    'หน้านี้เป็นแนวโน้มเชิงความเห็น ไม่ใช่นิยาม',
    'พลังงานบีบให้ง่าย — สลับ thread ตอน miss',
    [('อะไรผลักให้ microarchitecture ง่ายขึ้นตามหน้า 18?',['Power considerations','Moore’s Law','Clusters','Grid computing'],0,'Power considerations (หน้า 18)'),
     ('วิธีใดอาจมีประสิทธิภาพที่สุดในการทน cache-miss latency?','Thread switch (หน้า 18)'),
     ('วิเคราะห์ความเชื่อมโยงระหว่างหน้า 18 กับ multicore ในหน้า 5','หน้า 18 เสนอว่า multiple simple cores อาจแชร์ทรัพยากรได้ดีกว่า ซึ่งตรงกับ multicore = ชิปที่มีหลาย cores (หน้า 5)')])

add('shared-memory','Shared memory multiprocessor (SMP), UMA และ NUMA','core','หน้า 19',
    'SMP (shared memory multiprocessor) คือ hardware ให้ single physical address space แก่ทุก processor และ synchronize shared variables ด้วย locks. ด้าน memory access time แบ่งเป็น UMA (uniform) และ NUMA (nonuniform). ภาพแสดงแต่ละ processor มี cache ต่อเข้ากับ interconnection network ไปยัง memory และ I/O ร่วม.',
    ['SMP: single physical address space for all processors (หน้า 19)','Synchronize shared variables using locks (หน้า 19)','UMA (uniform) vs. NUMA (nonuniform) memory access time (หน้า 19)','Processor → Cache → Interconnection Network → Memory, I/O (ภาพหน้า 19)'],
    ['SMP','single physical address space','lock','UMA','NUMA','interconnection network'],
    'ตัวอย่าง sum reduction หน้า 20 ใช้ 64-processor UMA',
    'SMP แชร์ address space; message passing (หน้า 31) แต่ละ processor มี private address space',
    'SMP: ที่อยู่เดียว แชร์กัน ล็อกกัน',
    [('SMP ใช้อะไร synchronize shared variables?',['Locks','Messages','Interrupts','Branch prediction'],0,'Locks (หน้า 19)'),
     ('UMA กับ NUMA ต่างกันอย่างไร?','ต่างกันที่ memory access time: UMA uniform, NUMA nonuniform (หน้า 19)'),
     ('เปรียบเทียบ address space ของ SMP (หน้า 19) กับ message passing (หน้า 31)','SMP: single physical address space ร่วมกัน; message passing: แต่ละ processor มี private physical address space และส่ง/รับ messages')],(19,),
    comparison=(['','Shared memory (SMP)','Message passing'],[['Address space','single physical, ร่วมกัน','private ต่อ processor'],['การประสาน','locks','send/receive messages'],['หน้า','19','31']]))

add('sum-reduction','ตัวอย่าง sum reduction บน 64-processor UMA','core','หน้า 20–21',
    'รวมเลข 64,000 ตัวบน UMA 64 processors: processor มี ID 0 ≤ Pn ≤ 63 แบ่งให้ตัวละ 1000 ตัว แต่ละตัวรวม sum[Pn] ของช่วงตัวเอง. จากนั้นรวม partial sums แบบ divide and conquer: ครึ่งหนึ่งของ processors บวกเป็นคู่ แล้วเหลือหนึ่งในสี่ ... และต้อง synch() ระหว่างแต่ละขั้น. ถ้า half เป็นเลขคี่ processor 0 รับ element ที่ขาด.',
    ['64,000 numbers / 64 processors = 1000 per processor (หน้า 20)','sum[Pn] รวม A[1000*Pn] ถึง A[1000*(Pn+1)−1] (หน้า 20)','Reduction: divide and conquer; synchronize between steps (หน้า 20)','if (half%2 != 0 && Pn == 0) sum[0] += sum[half-1] (หน้า 21)','if (Pn < half) sum[Pn] += sum[Pn+half] (หน้า 21)'],
    ['sum reduction','partial sum','divide and conquer','synch()','UMA'],
    'โค้ดหน้า 21 เริ่ม half = 64 แล้วหารครึ่ง 32, 16, 8, 4, 2, 1 → 6 รอบของ loop',
    'ภาพต้นไม้หน้า 21 แสดงเพียง half = 4, 2, 1 (8 processors) เพื่อสาธิต ขณะที่โค้ดเริ่มที่ half = 64',
    'แบ่งก่อนรวมเอง แล้วครึ่งต่อครึ่งจนเหลือหนึ่ง',
    [('แต่ละ processor ได้ตัวเลขกี่ตัวในตัวอย่างหน้า 20?',['1000','64','64,000','100'],0,'1000 (หน้า 20)'),
     ('ทำไมต้องมี synch() ในแต่ละรอบ reduction?','เพื่อให้ partial sums ของรอบก่อนเสร็จก่อนจะนำไปบวกต่อ (Need to synchronize between reduction steps, หน้า 20–21)'),
     ('จงหาจำนวนรอบของ do–while ในโค้ดหน้า 21 เมื่อ half เริ่มที่ 64','6 รอบ: half = 32, 16, 8, 4, 2, 1 แล้วหยุดเมื่อ half > 1 เป็นเท็จ')],(20,21),
    formulas=[dict(expr='64,000 / 64 = 1000 numbers per processor\nsum[Pn] = Σ A[i], i = 1000·Pn … 1000·(Pn+1) − 1',description='การแบ่งงานขั้นแรกตามหน้า 20',pages='หน้า 20')],
    worked=[dict(title='ไล่ loop reduction (หน้า 21)',steps=['เริ่ม half = 64','แต่ละรอบ: synch() → ถ้า half คี่และ Pn = 0 ให้ sum[0] += sum[half−1] → half = half/2 → ถ้า Pn < half ให้ sum[Pn] += sum[Pn+half]','half หลังหาร: 32 → 16 → 8 → 4 → 2 → 1','เมื่อ half = 1 เงื่อนไข while (half > 1) เป็นเท็จ'],answer='6 รอบ ผลรวมทั้งหมดอยู่ใน sum[0]',pages='หน้า 21')])

add('gpu-history','ประวัติ GPU และกราฟิกในระบบ','extra','หน้า 22–23',
    'เริ่มจาก video card ยุคแรกที่มี frame buffer memory กับ address generation สำหรับ video output. 3D graphics processing เดิมอยู่ในคอมพิวเตอร์ระดับสูง (เช่น SGI) แล้ว Moore’s Law ทำให้ราคาต่ำลงและหนาแน่นขึ้นจนมี 3D graphics card สำหรับ PC และเครื่องเกม. GPU คือ processor ที่มุ่งงาน 3D graphics เช่น vertex/pixel processing, shading, texture mapping, rasterization. หน้า 23 แสดงตำแหน่ง GPU ในระบบ (ต่อผ่าน PCI-Express กับ North Bridge/chipset และมี GPU memory).',
    ['Early video cards: frame buffer memory + address generation (หน้า 22)','Moore’s Law ⇒ lower cost, higher density (หน้า 22)','GPU tasks: vertex/pixel processing, shading, texture mapping, rasterization (หน้า 22)','GPU ต่อผ่าน x16 PCI-Express link และมี GPU memory ของตัวเอง (ภาพหน้า 23)'],
    ['frame buffer','3D graphics','Moore’s Law','vertex/pixel processing','shading','texture mapping','rasterization','PCI-Express'],
    'ภาพหน้า 23 เทียบระบบ VGA controller เก่า กับ Intel CPU + North Bridge + GPU และ AMD CPU ที่มี North Bridge ในชิป',
    'GPU memory ในภาพแยกจาก system DDR2 memory',
    'Video card → 3D card → GPU',
    [('งานใดเป็นงานของ GPU ตามหน้า 22?',['Rasterization','Linpack','Message passing','Grid computing'],0,'Rasterization (หน้า 22)'),
     ('Moore’s Law ส่งผลต่อ 3D graphics อย่างไรตามสไลด์?','ทำให้ราคาต่ำลงและความหนาแน่นสูงขึ้น จน 3D graphics cards ใช้ใน PC และเครื่องเกมได้ (หน้า 22)'),
     ('จากภาพหน้า 23 GPU เชื่อมกับระบบผ่านอะไรในฝั่ง Intel CPU?','x16 PCI-Express link ไปยัง North Bridge และมี GPU Memory แยก (ภาพหน้า 23)')],(23,))

add('gpu-architectures','GPU architectures','core','หน้า 24',
    'งานของ GPU เป็น data-parallel สูง. GPU เป็น highly multithreaded ใช้ thread switching ซ่อน memory latency จึงพึ่ง multi-level caches น้อยลง และ graphics memory กว้างและ bandwidth สูง. มีแนวโน้มไปสู่ general purpose GPU ในระบบ heterogeneous: CPU ทำ sequential code, GPU ทำ parallel code. ภาษา/API ได้แก่ DirectX, OpenGL, Cg, HLSL และ CUDA.',
    ['Processing is highly data-parallel (หน้า 24)','Highly multithreaded; thread switching to hide memory latency; less reliance on multi-level caches (หน้า 24)','Graphics memory is wide and high-bandwidth (หน้า 24)','Heterogeneous: CPU for sequential code, GPU for parallel code (หน้า 24)','APIs: DirectX, OpenGL, Cg, HLSL, CUDA (หน้า 24)'],
    ['GPU','data-parallel','thread switching','memory latency','heterogeneous CPU/GPU','CUDA','DirectX','OpenGL','HLSL','Cg'],
    'เทียบกับ multithreading หน้า 15: GPU ใช้ thread switching แบบเดียวกันเพื่อซ่อน latency',
    'GPU ไม่ได้ซ่อน latency ด้วย cache ใหญ่ แต่ด้วยการสลับ thread',
    'GPU ซ่อนการรอด้วยการสลับ thread ไม่ใช่ด้วย cache',
    [('GPU ซ่อน memory latency ด้วยวิธีใด?',['Thread switching','Multi-level caches ใหญ่','Branch prediction','Locks'],0,'Thread switching (หน้า 24)'),
     ('ในระบบ heterogeneous CPU/GPU แบ่งงานอย่างไร?','CPU ทำ sequential code, GPU ทำ parallel code (หน้า 24)'),
     ('เปรียบเทียบการพึ่ง cache ของ GPU กับ multicore โดยใช้ข้อมูลหน้า 24 และ 29','GPU พึ่ง multi-level caches น้อย (หน้า 24) สอดคล้องกับ largest cache 0.75 MB ของ GPU เทียบ 8 MB ของ multicore (หน้า 29)')])

add('nvidia-fermi','ตัวอย่าง NVIDIA Fermi','important','หน้า 25–26',
    'Fermi ประกอบด้วย SIMD processors หลายตัว แต่ละตัวมี 16 SIMD lanes (thread processors). SIMD instruction ทำงานบน thread กว้าง 32 elements และถูก schedule แบบ dynamic บน processor กว้าง 16 ใน 2 cycles. มี registers 32K × 32-bit กระจายทั่ว lanes และ 64 registers ต่อ thread context. ภาพหน้า 25 แสดง instruction register, lanes ที่มี Reg 1K×32 และ load/store unit, address coalescing unit, interconnection network และ local memory 64 KiB.',
    ['SIMD Processor: 16 SIMD lanes (หน้า 26)','SIMD instruction: 32 element wide threads, 16-wide processor over 2 cycles (หน้า 26)','32K × 32-bit registers; 64 registers per thread context (หน้า 26)','ภาพ: Reg 1K×32 ต่อ lane, Local Memory 64 KiB (หน้า 25)'],
    ['SIMD lane','thread processor','thread context','address coalescing unit','local memory'],
    '32 elements / 16 lanes = 2 cycles ต่อ SIMD instruction',
    '32 คือความกว้าง thread ส่วน 16 คือจำนวน lanes จึงใช้ 2 cycles',
    '32 งาน 16 มือ = 2 รอบ',
    [('SIMD processor ของ Fermi มีกี่ SIMD lanes?',['16','32','64','8'],0,'16 SIMD lanes (หน้า 26)'),
     ('Register ต่อ thread context มีกี่ตัว?','64 registers per thread context (หน้า 26)'),
     ('คำนวณจำนวน cycles ที่ SIMD instruction กว้าง 32 elements ใช้บน processor กว้าง 16','32 / 16 = 2 cycles (ตรงกับ “over 2 cycles” หน้า 26)')],(25,),
    formulas=[dict(expr='32 elements / 16 lanes = 2 cycles\n32K × 32-bit registers; 64 registers per thread context',description='ตัวเลขจากหน้า 26',pages='หน้า 26')])

add('gpu-memory','GPU memory structures','important','หน้า 27',
    'ภาพหน้า 27 แสดงลำดับชั้น memory ของ GPU: CUDA thread แต่ละตัวมี per-CUDA thread private memory, thread block ใช้ per-block local memory ร่วมกัน และ grid (Grid 0, Grid 1 ตามลำดับเวลา) ใช้ GPU memory โดยมี inter-grid synchronization ระหว่าง grid.',
    ['CUDA thread ↔ per-CUDA thread private memory (หน้า 27)','Thread block ↔ per-block local memory (หน้า 27)','Grid 0, Grid 1 ↔ GPU memory; inter-grid synchronization (หน้า 27)'],
    ['CUDA thread','thread block','grid','private memory','local memory','GPU memory','inter-grid synchronization'],
    'ไล่จากเล็กไปใหญ่: thread → block → grid และ memory ก็ขยายตาม private → local → GPU memory',
    'Local memory ในภาพนี้คือ per-block (แชร์ใน block) ไม่ใช่ private ของ thread เดียว',
    'thread ส่วนตัว · block แชร์กลุ่ม · grid ใช้ GPU memory',
    [('Thread block ใช้ memory ระดับใดในภาพหน้า 27?',['Per-block local memory','Per-thread private memory','Disk','L2 cache'],0,'Per-Block Local Memory (หน้า 27)'),
     ('ระหว่าง Grid 0 กับ Grid 1 มีอะไรตามภาพ?','Inter-grid synchronization (หน้า 27)'),
     ('วิเคราะห์ความสัมพันธ์ระหว่างระดับการทำงานกับระดับ memory ในภาพหน้า 27','ยิ่งกลุ่มใหญ่ขึ้น (thread → block → grid) memory ที่ใช้ก็กว้างขึ้น (private → per-block local → GPU memory)')],(27,))

add('classifying-gpus','Classifying GPUs','core','หน้า 28',
    'GPU ไม่เข้ากับโมเดล SIMD/MIMD อย่างลงตัว: conditional execution ใน thread ทำให้ดูเหมือน MIMD แต่ประสิทธิภาพลดลง จึงต้องเขียน general purpose code อย่างระวัง. ตารางแบ่ง parallelism ตามระดับและเวลาที่ค้นพบ: ILP แบบ static = VLIW, dynamic = Superscalar; DLP แบบ static = SIMD or Vector, dynamic = Tesla Multiprocessor.',
    ['Don’t fit nicely into SIMD/MIMD model (หน้า 28)','Conditional execution → illusion of MIMD but performance degradation (หน้า 28)','ILP: static VLIW, dynamic Superscalar (หน้า 28)','DLP: static SIMD or Vector, dynamic Tesla Multiprocessor (หน้า 28)'],
    ['VLIW','superscalar','SIMD','vector','Tesla multiprocessor','instruction-level parallelism','data-level parallelism'],
    'Static = discovered at compile time; Dynamic = discovered at runtime',
    'Tesla multiprocessor อยู่ช่อง data-level + dynamic ไม่ใช่ instruction-level',
    'Compile time = Static (VLIW, SIMD/Vector); Runtime = Dynamic (Superscalar, Tesla)',
    [('ช่อง Data-Level Parallelism + Dynamic ในตารางหน้า 28 คืออะไร?',['Tesla Multiprocessor','VLIW','Superscalar','SIMD or Vector'],0,'Tesla Multiprocessor (หน้า 28)'),
     ('ทำไม conditional execution ใน GPU จึงเรียกว่า “illusion of MIMD”?','ทำให้ thread ดูเหมือนทำคำสั่งต่างกันได้เหมือน MIMD แต่แลกกับ performance degradation (หน้า 28)'),
     ('จัด VLIW และ Superscalar ตามตารางหน้า 28 และอธิบายเกณฑ์','ทั้งคู่เป็น instruction-level parallelism; VLIW ค้นพบที่ compile time (static), Superscalar ค้นพบที่ runtime (dynamic)')],(28,),
    comparison=(['','Static (compile time)','Dynamic (runtime)'],[['Instruction-Level Parallelism','VLIW','Superscalar'],['Data-Level Parallelism','SIMD or Vector','Tesla Multiprocessor']]))

add('gpu-perspective','Putting GPUs into perspective','important','หน้า 29–30',
    'ตารางหน้า 29 เทียบ multicore with SIMD กับ GPU: SIMD processors 4–8 vs 8–16, SIMD lanes/processor 2–4 vs 8–16, multithreading support 2–4 vs 16–32, single:double precision 2:1 ทั้งคู่, largest cache 8 MB vs 0.75 MB, memory address 64-bit ทั้งคู่, main memory 8–256 GB vs 4–6 GB, page protection Yes ทั้งคู่, demand paging Yes vs No, integrated scalar/SIMD processor Yes vs No, cache coherent Yes vs No. หน้า 30 เป็นตาราง Guide to GPU Terms.',
    ['GPU: SIMD processors 8–16, lanes 8–16, MT support 16–32 (หน้า 29)','Largest cache: multicore 8 MB vs GPU 0.75 MB (หน้า 29)','GPU: No demand paging, not cache coherent, no integrated scalar processor (หน้า 29)','Guide to GPU Terms (หน้า 30): ตัวอักษรเล็ก รายละเอียดต้องตรวจสอบจากต้นฉบับ'],
    ['multicore with SIMD','demand paging','cache coherent','SIMD lanes','memory protection'],
    'ใช้ตารางด้านล่างจำว่า GPU “มากกว่า” ที่ lanes/threads แต่ “น้อยกว่า/ไม่มี” ที่ cache, memory, paging, coherence',
    'ทั้งคู่มี memory address 64-bit และ page-level protection เหมือนกัน',
    'GPU: thread เยอะ cache เล็ก ไม่ coherent',
    [('ข้อใดที่ GPU ไม่มีตามตารางหน้า 29?',['Demand paging','64-bit memory address','Memory protection at page level','SIMD lanes'],0,'Demand paging: GPU = No (หน้า 29)'),
     ('ขนาด largest cache ของ multicore และ GPU ต่างกันเท่าใด?','Multicore 8 MB, GPU 0.75 MB (หน้า 29)'),
     ('คำนวณว่า largest cache ของ multicore ใหญ่กว่า GPU กี่เท่าตามตารางหน้า 29','8 / 0.75 ≈ 10.7 เท่า')],(29,30),
    comparison=(['Feature','Multicore with SIMD','GPU'],[['SIMD processors','4 to 8','8 to 16'],['SIMD lanes/processor','2 to 4','8 to 16'],['MT support for SIMD threads','2 to 4','16 to 32'],['Single:double precision','2:1','2:1'],['Largest cache','8 MB','0.75 MB'],['Memory address','64-bit','64-bit'],['Main memory','8–256 GB','4–6 GB'],['Page-level protection','Yes','Yes'],['Demand paging','Yes','No'],['Integrated scalar/SIMD','Yes','No'],['Cache coherent','Yes','No']]))

add('message-passing','Message passing','core','หน้า 31',
    'ใน message-passing multiprocessor แต่ละ processor มี private physical address space และ hardware ส่ง/รับ messages ระหว่าง processors. ภาพแสดงแต่ละ processor มี cache และ memory ของตัวเองเชื่อมกันผ่าน interconnection network.',
    ['Each processor has private physical address space (หน้า 31)','Hardware sends/receives messages between processors (หน้า 31)','Processor → Cache → Memory ของตัวเอง → Interconnection Network (ภาพหน้า 31)'],
    ['message passing','private physical address space','send/receive','interconnection network'],
    'เทียบภาพหน้า 19 (memory ร่วมหลัง network) กับหน้า 31 (memory อยู่กับแต่ละ processor ก่อน network)',
    'ตำแหน่ง memory ในภาพคือจุดต่าง: shared memory อยู่หลัง network, message passing อยู่ติด processor',
    'ไม่มีที่อยู่ร่วม ต้องส่งจดหมาย (message)',
    [('ใน message passing processor แต่ละตัวมี address space แบบใด?',['Private physical address space','Single shared address space','ไม่มี address space','Virtual เท่านั้น'],0,'Private physical address space (หน้า 31)'),
     ('Processor สื่อสารกันอย่างไรใน message passing?','Hardware ส่งและรับ messages ระหว่าง processors (หน้า 31)'),
     ('วิเคราะห์ความต่างของตำแหน่ง memory ในภาพหน้า 19 และ 31','หน้า 19 memory ร่วมอยู่หลัง interconnection network; หน้า 31 memory แยกอยู่กับ processor แต่ละตัวก่อนต่อ network')],(31,))

add('clusters','Loosely coupled clusters','core','หน้า 32',
    'Cluster คือเครือข่ายของคอมพิวเตอร์อิสระ แต่ละเครื่องมี private memory และ OS เชื่อมกันผ่าน I/O system (เช่น Ethernet/switch, Internet). เหมาะกับงานที่เป็น independent tasks เช่น web servers, databases, simulations และให้ high availability, scalable, affordable. ปัญหาคือ administration cost (นิยมใช้ virtual machines) และ interconnect bandwidth ต่ำเมื่อเทียบ processor/memory bandwidth ของ SMP.',
    ['Network of independent computers; private memory and OS (หน้า 32)','Connected using I/O system: Ethernet/switch, Internet (หน้า 32)','Suitable for independent tasks: web servers, databases, simulations (หน้า 32)','High availability, scalable, affordable (หน้า 32)','Problems: administration cost (prefer VMs), low interconnect bandwidth (หน้า 32)'],
    ['cluster','loosely coupled','private memory and OS','I/O system','virtual machine','interconnect bandwidth'],
    'Concluding remarks หน้า 40: SaaS สำคัญขึ้นและ clusters เข้ากันได้ดี',
    'Cluster ต่อกันผ่าน I/O system ไม่ใช่ memory bus จึง bandwidth ต่ำกว่า SMP',
    'แยกเครื่อง แยก OS ต่อผ่าน network — ถูก ทนทาน แต่ช้าตอนคุยกัน',
    [('Cluster เชื่อมคอมพิวเตอร์ด้วยอะไรตามสไลด์?',['I/O system เช่น Ethernet/switch','Shared memory bus','PCI-Express GPU','Register file'],0,'I/O system: Ethernet/switch, Internet (หน้า 32)'),
     ('ปัญหาของ cluster 2 ข้อตามหน้า 32 คืออะไร?','Administration cost (ใช้ VMs ช่วย) และ low interconnect bandwidth'),
     ('ทำไม web server จึงเหมาะกับ cluster ตามหน้า 32?','เพราะเป็นงาน independent tasks และ cluster ให้ high availability, scalable, affordable')])

add('grid-computing','Grid computing','important','หน้า 33',
    'Grid computing คือคอมพิวเตอร์แยกกันที่เชื่อมด้วย long-haul networks เช่น Internet. งานถูกแบ่งเป็น work units ส่งออกไปแล้วส่งผลกลับ และใช้ประโยชน์จากเวลาว่างของ PC ได้ เช่น SETI@home และ World Community Grid.',
    ['Separate computers interconnected by long-haul networks (หน้า 33)','Work units farmed out, results sent back (หน้า 33)','Use idle time on PCs: SETI@home, World Community Grid (หน้า 33)'],
    ['grid computing','long-haul network','work unit','idle time'],
    'SETI@home ส่ง work unit ให้ PC ที่ว่างประมวลผลแล้วส่งผลกลับ',
    'Grid ต่างจาก cluster ตรงที่เชื่อมด้วย long-haul network และใช้ PC ที่ว่าง',
    'แจกงานไปไกล ทำตอนเครื่องว่าง ส่งผลกลับ',
    [('ตัวอย่าง grid computing ตามสไลด์คือข้อใด?',['SETI@home','Linpack','CUDA','Pentium-4 HT'],0,'SETI@home, World Community Grid (หน้า 33)'),
     ('Grid computing ใช้ทรัพยากรใดที่ปกติถูกปล่อยว่าง?','Idle time on PCs (หน้า 33)'),
     ('เปรียบเทียบการเชื่อมต่อของ grid (หน้า 33) กับ cluster (หน้า 32)','Grid ใช้ long-haul networks เช่น Internet; cluster ใช้ I/O system เช่น Ethernet/switch (Internet ก็ยกเป็นตัวอย่างได้)')])

add('network-topologies','Interconnection network topologies และ multistage networks','core','หน้า 34–35',
    'Network topology คือการจัดวาง processors, switches และ links. หน้า 34 แสดง bus, ring, 2D mesh, N-cube (N = 3) และ fully connected. หน้า 35 แสดง multistage networks: crossbar, Omega network และ Omega network switch box (อินพุต A, B ไป C, D).',
    ['Topology = arrangements of processors, switches, and links (หน้า 34)','Bus, Ring, 2D Mesh, N-cube (N = 3), Fully connected (หน้า 34)','Multistage: a. Crossbar, b. Omega network, c. Omega switch box (หน้า 35)'],
    ['network topology','bus','ring','2D mesh','N-cube','fully connected','crossbar','Omega network','switch box'],
    'N-cube (N = 3) ในภาพคือ cube มี 8 nodes (2³) — นับจากภาพ',
    'Crossbar กับ Omega เป็น multistage/switch network ไม่ใช่ topology ของ node แบบ bus/ring',
    'B-R-M-C-F: Bus, Ring, Mesh, Cube, Fully connected',
    [('Topology ใดในหน้า 34 ที่ทุก node ต่อกันโดยตรง?',['Fully connected','Bus','Ring','2D Mesh'],0,'Fully connected (หน้า 34)'),
     ('Multistage networks ในหน้า 35 มีอะไรบ้าง?','Crossbar, Omega network และ Omega network switch box'),
     ('คำนวณจำนวน nodes ของ N-cube เมื่อ N = 3 ตามภาพหน้า 34','2³ = 8 nodes')],(34,35))

add('network-characteristics','Network characteristics','important','หน้า 36',
    'คุณลักษณะของ network ได้แก่ performance (latency per message บน unloaded network; throughput ซึ่งแยกเป็น link bandwidth, total network bandwidth และ bisection bandwidth; congestion delays ที่ขึ้นกับ traffic), cost, power และ routability in silicon.',
    ['Latency per message (unloaded network) (หน้า 36)','Throughput: link, total network, bisection bandwidth (หน้า 36)','Congestion delays (depending on traffic) (หน้า 36)','Cost, power, routability in silicon (หน้า 36)'],
    ['latency','throughput','link bandwidth','total network bandwidth','bisection bandwidth','congestion delay','routability'],
    'จัดเป็น 4 กลุ่ม: performance, cost, power, routability',
    'Latency วัดบน unloaded network; congestion delay ขึ้นกับ traffic',
    'Performance-Cost-Power-Route',
    [('ข้อใดอยู่ในกลุ่ม throughput ตามหน้า 36?',['Bisection bandwidth','Latency per message','Cost','Power'],0,'Bisection bandwidth (หน้า 36)'),
     ('Throughput แบ่งเป็นอะไรบ้าง?','Link bandwidth, total network bandwidth, bisection bandwidth (หน้า 36)'),
     ('เปรียบเทียบ latency per message กับ congestion delays ตามหน้า 36','Latency วัดบน unloaded network; congestion delays เกิดเพิ่มตาม traffic')])

add('benchmarks','Parallel benchmarks และ code or applications','important','หน้า 37–38',
    'Benchmarks: Linpack (matrix linear algebra), SPECrate (parallel run ของ SPEC CPU, job-level parallelism), SPLASH (Stanford, mix of kernels/applications, strong scaling), NAS (NASA, CFD kernels) และ PARSEC (Princeton, multithreaded apps ด้วย Pthreads และ OpenMP). หน้า 38: benchmark ดั้งเดิมใช้ code และ data คงที่ แต่ parallel programming เปลี่ยนเร็ว จึงเสนอเทียบระบบที่ implement application ที่กำหนด (เช่น Linpack, Berkeley Design Patterns) เพื่อส่งเสริมนวัตกรรม.',
    ['Linpack: matrix linear algebra; SPECrate: job-level parallelism (หน้า 37)','SPLASH: strong scaling; NAS: CFD kernels (หน้า 37)','PARSEC: Pthreads and OpenMP (หน้า 37)','Traditional: fixed code and data sets (หน้า 38)','Compare systems implementing a given application → foster innovation (หน้า 38)'],
    ['Linpack','SPECrate','SPLASH','NAS','PARSEC','Pthreads','OpenMP','Berkeley Design Patterns','strong scaling'],
    'ถ้าต้องการวัด job-level parallelism ให้ใช้ SPECrate',
    'Linpack ถูกยกทั้งในหน้า 37 (benchmark) และหน้า 38 (ตัวอย่างการเทียบตาม application)',
    'L-S-S-N-P: Linpack, SPECrate, SPLASH, NAS, PARSEC',
    [('Benchmark ใดใช้ Pthreads และ OpenMP?',['PARSEC','Linpack','NAS','SPECrate'],0,'PARSEC (หน้า 37)'),
     ('ปัญหาของ traditional benchmarks ตามหน้า 38 คืออะไร?','ใช้ code และ data sets คงที่ ขณะที่ parallel programming กำลังพัฒนา'),
     ('ถ้าต้องการวัด computational fluid dynamics kernels ควรเลือก benchmark ใด?','NAS (NASA Advanced Supercomputing) suite (หน้า 37)')])

add('modeling-performance','Modeling performance และ arithmetic intensity','important','หน้า 39',
    'สมมติ metric ที่สนใจคือ achievable GFLOPs/sec วัดด้วย computational kernels จาก Berkeley Design Patterns. Arithmetic intensity ของ kernel คือ FLOPs ต่อ byte ของ memory ที่เข้าถึง. สำหรับคอมพิวเตอร์หนึ่งเครื่องให้หา peak GFLOPS (จาก data sheet) และ peak memory bytes/sec (ด้วย Stream benchmark).',
    ['Metric: achievable GFLOPs/sec (หน้า 39)','Arithmetic intensity = FLOPs per byte of memory accessed (หน้า 39)','Peak GFLOPS from data sheet (หน้า 39)','Peak memory bytes/sec using Stream benchmark (หน้า 39)'],
    ['GFLOPs/sec','arithmetic intensity','Berkeley Design Patterns','peak GFLOPS','Stream benchmark'],
    'ขั้นตอนตามสไลด์: หา arithmetic intensity ของ kernel แล้วหา peak GFLOPS (data sheet) และ peak memory bytes/sec (Stream) ของเครื่อง',
    'Peak GFLOPS มาจาก data sheet ส่วน peak memory bandwidth วัดด้วย Stream benchmark อย่าสลับ',
    'งานคำนวณ ÷ ไบต์ที่อ่าน = arithmetic intensity',
    [('Peak memory bytes/sec วัดด้วยอะไรตามสไลด์?',['Stream benchmark','Data sheet','Linpack','SPECrate'],0,'Stream benchmark (หน้า 39)'),
     ('ให้นิยาม arithmetic intensity','FLOPs per byte of memory accessed (หน้า 39)'),
     ('สำหรับคอมพิวเตอร์หนึ่งเครื่อง ต้องหาค่าอะไร 2 ค่า และได้มาจากแหล่งใด?','Peak GFLOPS จาก data sheet และ peak memory bytes/sec จาก Stream benchmark (หน้า 39)')],(),
    formulas=[dict(expr='Arithmetic intensity = FLOPs / bytes of memory accessed',description='นิยามจากหน้า 39',pages='หน้า 39')])

add('concluding-remarks','Concluding remarks','extra','หน้า 40',
    'เป้าหมายคือประสิทธิภาพสูงขึ้นด้วยการใช้หลาย processor. ความยากคือการพัฒนา parallel software และออกแบบ architecture ที่เหมาะสม. SaaS มีความสำคัญมากขึ้นและ clusters เข้ากันได้ดี. performance per dollar และ performance per Joule เป็นตัวขับเคลื่อนทั้ง mobile และ WSC.',
    ['Goal: higher performance using multiple processors (หน้า 40)','Difficulties: parallel software, appropriate architectures (หน้า 40)','SaaS growing; clusters are a good match (หน้า 40)','Performance per dollar and per Joule drive mobile and WSC (หน้า 40)'],
    ['SaaS','WSC','performance per dollar','performance per Joule'],
    'เชื่อมกับหน้า 8: ความยากด้าน software ยังเป็นประเด็นหลักจนจบบท',
    'สไลด์ไม่ได้ขยายความ WSC ในเนื้อหาส่วนอื่นของบท: ต้องตรวจสอบจากต้นฉบับ',
    'เร็วขึ้นด้วยหลายตัว แต่ software ยาก; เงินและพลังงานเป็นตัวตัดสิน',
    [('อะไรขับเคลื่อนทั้ง mobile และ WSC ตามหน้า 40?',['Performance per dollar และ per Joule','จำนวน register','ขนาด cache','Clock rate'],0,'Performance per dollar and performance per Joule (หน้า 40)'),
     ('ความยาก 2 ข้อตามหน้า 40 คืออะไร?','Developing parallel software และ devising appropriate architectures'),
     ('ทำไม clusters จึงเข้ากับ SaaS ตามหน้า 32 และ 40?','SaaS สำคัญขึ้น (หน้า 40) และ clusters เหมาะกับ independent tasks เช่น web servers พร้อม high availability, scalable, affordable (หน้า 32)')])

FIG = {
    3:('A Taxonomy of Parallel Processor Architectures','ต้นไม้ SISD/SIMD/MISD/MIMD, SMP, NUMA, clusters (Figure 17.1, Pearson)'),
    9:('Instruction and Data Streams','ตาราง SISD/SIMD/MISD/MIMD และ SPMD'),
    11:('Example: DAXPY','โค้ด RISC-V แบบ loop เทียบ vector code และคำอธิบาย DAXPY'),
    14:('Vector vs. Multimedia Extensions','vector unit แบบ lanes ผสม pipelined/arrayed'),
    17:('Multithreading Example','issue slots ของ Coarse MT, Fine MT และ SMT'),
    19:('Shared Memory','processor/cache ต่อ interconnection network ไป memory และ I/O'),
    20:('Example: Sum Reduction','แบ่ง 64,000 ตัวให้ 64 processors และโค้ดรวมผลขั้นแรก'),
    21:('Example: Sum Reduction','โค้ด reduction และต้นไม้ half = 4, 2, 1'),
    23:('Graphics in the System','ตำแหน่ง GPU, North Bridge และ GPU memory ในระบบ'),
    25:('Example: NVIDIA Fermi','SIMD processor 16 lanes, registers, load/store units, local memory 64 KiB'),
    27:('GPU Memory Structures','CUDA thread, thread block, grid และ memory แต่ละระดับ'),
    28:('Classifying GPUs','ตาราง ILP/DLP × static/dynamic'),
    29:('Putting GPUs into Perspective','ตารางเทียบ multicore with SIMD กับ GPU'),
    30:('Guide to GPU Terms','ตารางศัพท์ GPU (ตัวอักษรเล็ก ต้องตรวจสอบจากต้นฉบับ)'),
    31:('Message Passing','processor/cache/memory ของแต่ละตัวต่อ interconnection network'),
    34:('Interconnection Networks','bus, ring, 2D mesh, N-cube (N = 3), fully connected'),
    35:('Multistage Networks','crossbar, Omega network, Omega switch box'),
}
figures=[]
for p,(title,caption) in FIG.items():
    figures.append(dict(id=f'fig-{p}',page=p,file=f'slide-{p:02d}.png',title=f'{title} · หน้า {p}',
                        caption=f'{caption} ({SOURCE}, หน้า {p})'))

flashcards=[dict(front=t['title'],back=t['remember'][0],pages=t['pages']) for t in topics]
term_cards=[
    ('SISD / SIMD / MISD / MIMD','Pentium 4 / SSE x86 / no examples today / Xeon e5345','หน้า 9'),
    ('SPMD','Single Program Multiple Data บน MIMD ด้วย conditional code','หน้า 9'),
    ('Task-level parallelism','high throughput สำหรับ independent jobs','หน้า 5'),
    ('Parallel programming difficulties','partitioning, coordination, communications overhead','หน้า 8'),
    ('RISC-V vector registers','v0–v31: 32 × 64-element, 64-bit elements','หน้า 10'),
    ('fadd.d.v vs fadd.d.vs','vector+vector vs scalar+ทุก element','หน้า 10'),
    ('DAXPY','Y = a × X + Y (BLAS)','หน้า 11'),
    ('Fine-grain MT','switch threads after each cycle','หน้า 15'),
    ('Coarse-grain MT','switch only on long stall (L2-cache miss)','หน้า 15'),
    ('SMT','schedule instructions from multiple threads ใน multiple-issue processor','หน้า 16'),
    ('SMP','single physical address space; locks','หน้า 19'),
    ('UMA / NUMA','uniform / nonuniform memory access time','หน้า 19'),
    ('Fermi SIMD processor','16 lanes; 32-wide thread over 2 cycles; 64 regs/thread','หน้า 26'),
    ('VLIW / Superscalar','ILP static / ILP dynamic','หน้า 28'),
    ('SIMD or Vector / Tesla','DLP static / DLP dynamic','หน้า 28'),
    ('Message passing','private physical address space; send/receive messages','หน้า 31'),
    ('Grid computing','long-haul networks; ใช้ idle time ของ PC','หน้า 33'),
    ('Bisection bandwidth','หนึ่งใน throughput ของ network','หน้า 36'),
    ('Arithmetic intensity','FLOPs per byte of memory accessed','หน้า 39'),
]
flashcards += [dict(front=f,back=b,pages=p) for f,b,p in term_cards]

data=dict(
    source=SOURCE,sourcePageCount=41,
    course='ITDS-211 · Computer Architecture & Operating System',
    instructor='W. Suntiamorntut, Ph.D.',
    chapter='Chapter08 · Parallel Processors from Client to Cloud',
    description='multiprocessors, SIMD/vector, multithreading, shared memory, GPUs, clusters และ network topologies',
    notice='เลขหน้าเป็นหน้า PDF 1–41; หัวสไลด์พิมพ์ “Chapter 6 — Parallel Processors from Client to Cloud — 2–56” ซึ่งเป็นเลขอีกชุด; หน้า 3 เป็นภาพจาก Pearson และหน้า 30 ตัวอักษรเล็กต้องตรวจสอบจากต้นฉบับ',
    purpose='บทนี้เรียนเพื่อเข้าใจว่าการใช้หลาย processor เพิ่มประสิทธิภาพได้อย่างไร: จำแนกสถาปัตยกรรมแบบ SISD/SIMD/MIMD, เทียบ vector/SIMD, multithreading, shared memory, GPU, clusters และ network topologies พร้อมความยากของ parallel software และวิธีวัดประสิทธิภาพ',
    purposePages='หน้า 4–40',
    objectiveNote='วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สรุปจาก Chapter Overview หน้า 4 และ Concluding Remarks หน้า 40',
    flashcardNote='Flashcards ใช้ศัพท์ ตัวเลข และการจำแนกจากสไลด์เท่านั้น',
    goals=[
        dict(text='อธิบายเป้าหมาย multiprocessors และความยากของ parallel programming',pages='หน้า 5–8'),
        dict(text='จำแนก SISD/SIMD/MISD/MIMD/SPMD และเทียบ vector กับ SIMD/multimedia extensions',pages='หน้า 3, 9–14'),
        dict(text='แยก fine-grain, coarse-grain และ simultaneous multithreading',pages='หน้า 15–18'),
        dict(text='อธิบาย shared memory (UMA/NUMA) และไล่ตัวอย่าง sum reduction',pages='หน้า 19–21'),
        dict(text='อธิบายสถาปัตยกรรม GPU, Fermi, memory structures และการจำแนก GPU',pages='หน้า 22–30'),
        dict(text='เทียบ message passing, clusters, grid และ network topologies/characteristics',pages='หน้า 31–36'),
        dict(text='รู้จัก parallel benchmarks และ arithmetic intensity',pages='หน้า 37–39')],
    limits=[
        'อ่านและตรวจภาพครบ 41 หน้า: หน้า 1 ปก, หน้า 2 course outline, หน้า 4 chapter overview, หน้า 41 Q&A',
        'สไลด์ไม่มีรายการ Chapter Objectives โดยตรงหรือข้อสอบเก่า: ต้องตรวจสอบจากต้นฉบับ; ระดับสีเป็นลำดับเวลาอ่าน ไม่ใช่สถิติการออกสอบ',
        'หน้า 3 เป็น Figure 17.1 จาก Pearson (ต่างจากตำรา MK ส่วนอื่นของบท)',
        'หน้า 30 Guide to GPU Terms ตัวอักษรเล็กเกินกว่าจะสรุปรายละเอียดได้: ต้องตรวจสอบจากต้นฉบับ',
        'ภาพหน้า 21 แสดงต้นไม้ half = 4, 2, 1 (8 processors) ขณะที่โค้ดเริ่ม half = 64',
        'ภาพหน้า 14 ถูกตัดขอบบางส่วน; ตัวเลขตารางหน้า 29 เป็นค่าตามสไลด์ ไม่ใช่สเปกปัจจุบัน',
        'คำถามคำนวณใช้เฉพาะตัวเลขและนิยามในสไลด์; ไม่มีการอ้างว่าเป็นข้อสอบจริง'],
    figures=figures,topics=topics,
    roadmap=[
        dict(title='1 · ภาพรวมและความยาก',text='taxonomy → goal/multicore → HW/SW → partitioning/coordination/communication',pages='หน้า 3–8',topic='processor-taxonomy'),
        dict(title='2 · SIMD และ vector',text='ตาราง SISD–MIMD/SPMD → vector registers → DAXPY → vector vs scalar/SIMD/multimedia',pages='หน้า 9–14',topic='instruction-data-streams'),
        dict(title='3 · Multithreading',text='fine vs coarse → SMT และภาพ issue slots → แนวโน้ม',pages='หน้า 15–18',topic='multithreading'),
        dict(title='4 · Shared memory และ GPU',text='SMP/UMA/NUMA → sum reduction → GPU architecture, Fermi, memory, classification, perspective',pages='หน้า 19–30',topic='shared-memory'),
        dict(title='5 · Message passing และการวัดผล',text='message passing → clusters/grid → topologies/characteristics → benchmarks/arithmetic intensity',pages='หน้า 31–40',topic='message-passing')],
    plan=[
        dict(title='รอบ 1 · แผนที่บท',task='วาดต้นไม้หน้า 3 และตาราง 2×2 หน้า 9 จากความจำ; จำ 3 difficulties หน้า 8',check='จับคู่ SISD/SIMD/MISD/MIMD กับตัวอย่างและบอกนิยาม SPMD ได้',pages='หน้า 3–9'),
        dict(title='รอบ 2 · Vector/SIMD',task='อ่าน DAXPY ทั้งสองแบบ นับคำสั่งและรอบ loop; ทำตาราง vector vs multimedia',check='อธิบาย .v/.vs และคิด 512/8 = 64 ได้',pages='หน้า 10–14'),
        dict(title='รอบ 3 · Multithreading และ shared memory',task='เทียบ fine/coarse/SMT ด้วยภาพหน้า 17; ไล่โค้ด sum reduction ทีละรอบ',check='บอกว่า coarse-grain ไม่ซ่อน short stalls และ reduction ใช้ 6 รอบ',pages='หน้า 15–21'),
        dict(title='รอบ 4 · GPU',task='ท่องตัวเลข Fermi, ตาราง classifying GPUs และ perspective',check='ตอบ 16 lanes/32-wide/2 cycles และเทียบ cache/paging/coherence ได้',pages='หน้า 22–30'),
        dict(title='รอบ 5 · Clusters, networks และ Quiz',task='เทียบ SMP vs message passing vs cluster vs grid; จำ topologies และ benchmarks; ทำ Quiz ทุกหัวข้อ',check='ตอบหัวข้อแดงครบและอธิบาย arithmetic intensity ได้',pages='หน้า 31–40')],
    cram=[
        dict(title='ถ้าเหลือ 3 วัน',text='วัน 1 หน้า 3–14 (taxonomy, SIMD, vector); วัน 2 หน้า 15–30 (multithreading, shared memory, GPU); วัน 3 หน้า 31–40 และทำ Quiz'),
        dict(title='ถ้าเหลือ 1 วัน',text='ตารางหน้า 9 → vector/DAXPY หน้า 10–11 → multithreading หน้า 15–16 → SMP/reduction หน้า 19–21 → GPU หน้า 24–29 → message passing/clusters/topologies หน้า 31–36'),
        dict(title='ถ้าเหลือ 3 ชั่วโมง',text='0–40 นาที หน้า 3–14; 40–80 นาที หน้า 15–21; 80–130 นาที หน้า 22–30; 130–165 นาที หน้า 31–39; 165–180 นาทีสุ่ม Quiz')],
    strategyIntro='เน้นหัวข้อที่สไลด์ให้นิยาม ตารางจำแนก และตัวเลข เช่น SISD–MIMD, vector registers, multithreading, SMP/UMA/NUMA, Fermi, classifying GPUs และ topologies; ไม่มีข้อสอบเก่าจึงไม่ยืนยันโอกาสออกจริง',
    strategy=[
        dict(title='ควรท่องจำ',text='ตาราง SISD/SIMD/MISD/MIMD, SPMD, fine/coarse/SMT, UMA/NUMA, VLIW/Superscalar/SIMD/Tesla, topologies 5 แบบ, benchmarks 5 ชุด (หน้า 9, 15–19, 28, 34, 37)'),
        dict(title='ควรฝึกโจทย์',text='64,000/64 = 1000 และรอบ reduction; DAXPY 512/8 = 64; Fermi 32/16 = 2 cycles; arithmetic intensity FLOPs/byte (หน้า 11, 20–21, 26, 39)'),
        dict(title='ควรเข้าใจแนวคิด',text='ทำไม parallel software ยาก, vector หลบ control hazard, GPU ซ่อน latency ด้วย thread switching, shared memory vs message passing (หน้า 8, 12, 24, 19, 31)'),
        dict(title='เตรียมข้อสอบแบบผสม',text='เลือกตอบจับคู่ศัพท์/ตัวอย่าง; อัตนัยเทียบสถาปัตยกรรม; คำนวณจากตัวเลขสไลด์; วิเคราะห์ภาพ multithreading, memory และ topologies (หน้า 3–40)')],
    flashcards=flashcards)

assert len(topics)==29 and len({t["id"] for t in topics})==29
assert all(len(t['questions'])==3 and t['pages'] and t['summary'] for t in topics)
assert set(f['id'] for f in figures)==set(fid for t in topics for fid in t['figures'])
assert all((HERE/f['file']).is_file() for f in figures)
(HERE/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('topics',len(topics),'figures',len(figures),'questions',sum(len(t['questions']) for t in topics),'flashcards',len(flashcards))
