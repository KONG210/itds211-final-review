"""Source-grounded Chapter03 study data. Page numbers are PDF pages, not textbook footers."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = 'itds-211_comp_arch_Chapter03_RiscV.pdf'
topics = []

def add(id, title, level, pages, summary, remember, terms, example, confusion,
        mnemonic, quiz, image_pages=(), comparison=None):
    """quiz: (question, four options, correct index, answer), then two Q/A pairs."""
    assert len(quiz) == 3
    m, a, b = quiz
    questions = [dict(type='เลือกตอบ', q=m[0], options=m[1], correct=m[2],
                      answer=m[3], pages=pages),
                 dict(type='อัตนัย', q=a[0], answer=a[1], pages=pages),
                 dict(type='วิเคราะห์' if not any(x in a[0]+b[0] for x in ('คำนวณ','จงหา','เท่าไร')) else 'คำนวณ',
                      q=b[0], answer=b[1], pages=pages)]
    entry = dict(id=id,title=title,level=level,pages=pages,
        reason={'core':'นิยาม สูตร รูปแบบคำสั่ง หรือขั้นตอนหลักที่สไลด์ใช้ต่อยอด',
                'important':'ตัวอย่างและการประยุกต์ที่ช่วยแยกแนวคิดหลัก',
                'extra':'รายละเอียดประกอบหรือส่วน Self-study ที่อ่านหลังแกนหลัก'}[level],
        summary=summary,remember=remember,terms=terms,example=example,
        confusion=confusion,mnemonic=mnemonic,questions=questions,
        figures=[f'fig-{p}' for p in image_pages])
    if comparison: entry['comparison'] = dict(headers=comparison[0],rows=comparison[1])
    topics.append(entry)

add('data-map','ข้อมูลเชิงปริมาณและระบบเลข','core','หน้า 4–8',
    'บทเริ่มจากการเก็บข้อมูลใน register ที่มีจำนวนบิตจำกัด แล้วแยกข้อมูลเป็น quantitative กับ qualitative. ข้อมูลเชิงปริมาณแบ่ง integer/non-integer และ signed/unsigned; ระบบฐานที่ใช้คือ 10, 2, 8 และ 16.',
    ['Unsigned n บิตมีค่า 0 ถึง 2^n−1 (หน้า 5)','quantitative: integer/non-integer; integer อาจ signed หรือ unsigned (หน้า 6–8)','ฐาน 2 ใช้ 0–1, ฐาน 8 ใช้ 0–7, ฐาน 16 ใช้ 0–9 และ A–F (หน้า 7)'],
    ['bit/register','unsigned','decimal/binary/octal/hexadecimal'],
    'สไลด์ยก +20, −20 เป็น integer และ 10.25, 3.3333, 1/8 เป็น non-integer (หน้า 8)',
    'จำนวนบิตจำกัดทำให้ช่วงค่าจำกัด; อย่าใช้ช่วง signed แทนสูตร unsigned',
    'จำนวนบิตกำหนดช่วง; ฐานกำหนดชุดหลัก',
    [('Unsigned n บิตมีค่าสูงสุดเท่าไร?',['2^n−1','2^(n−1)−1','2^n','n−1'],0,'2^n−1 ตามหน้า 5'),('ข้อมูล quantitative แบ่งอย่างไร?','integer และ non-integer; integer แยก signed/unsigned ตามหน้า 6–8'),('เลขฐาน 16 ใช้สัญลักษณ์ใดเพิ่มจาก 0–9?','A–F ตามหน้า 7')],(5,6,7))

add('sign-magnitude','Sign & Magnitude','core','หน้า 9–12',
    'การแทน signed แบบ Sign & Magnitude ใช้หนึ่งบิตเป็น sign และ n บิตเป็น magnitude. sign 0 หมายถึงบวกหรือศูนย์, sign 1 หมายถึงลบหรือศูนย์ จึงมีรหัสศูนย์สองแบบและช่วง −(2^n−1) ถึง +(2^n−1).',
    ['หนึ่ง sign bit + n magnitude bits (หน้า 10)','8 บิตทั้งหมดมี magnitude 7 บิต จึงได้ −127 ถึง +127 (หน้า 10–11)','00000000 และ 10000000 เป็นศูนย์สองรูป (หน้า 11)'],
    ['Sign & Magnitude','sign bit','magnitude','positive zero / negative zero'],
    'เปลี่ยนเครื่องหมายโดยกลับ sign bit; สไลด์ระบุว่า absolute value ทำได้ตรงไปตรงมา (หน้า 12)',
    'อย่าสับสน n magnitude bits ในสูตรกับจำนวนบิตทั้งหมด; แบบนี้ไม่ได้ใช้บวก/ลบด้วยขั้นเดียวกันเสมอ',
    'หนึ่งบิตบอกเครื่องหมาย; ที่เหลือบอกขนาด; ศูนย์สองตัว',
    [('8-bit Sign & Magnitude มีค่าสูงสุดเท่าไร?',['+127','+128','+255','+256'],0,'+127 เพราะมี magnitude 7 บิต'),('เหตุใดแบบนี้มีศูนย์สองรหัส?','magnitude 0 จับคู่กับ sign 0 หรือ sign 1 ได้'),('รหัส 10000000 ใน 8-bit Sign & Magnitude หมายถึงอะไร?','negative zero ตามหน้า 11')],(10,11,12))

add('complement-family','(r−1)’s และ r’s complement','core','หน้า 13–15',
    'สไลด์จัด complement เป็น (r−1)’s กับ r’s ตามฐาน r. สำหรับเลข n หลัก m สูตรคือ (r^n−1)−m และ r^n−m; ฐานสิบจึงมี 9’s/10’s และฐานสองมี 1’s/2’s complement.',
    ['(r−1)’s complement = (r^n−1)−m (หน้า 14)','r’s complement = r^n−m (หน้า 14)','ตัวอย่าง m=382, n=3: 9’s =617 และ 10’s =618 (หน้า 15)'],
    ['radix r','(r−1)’s complement','r’s complement','9’s/10’s; 1’s/2’s complement'],
    '999−382=617 แล้วบวกหนึ่งเป็น 618 ตามตัวอย่างฐานสิบหน้า 15',
    'หน้า 14 คำอธิบายสูตร r’s ใช้ n แต่สูตรใช้ m; หน้า 15 เรียกผลฐานสิบว่า 1’/2’ complement แทน 9’s/10’s: ต้องตรวจสอบจากต้นฉบับ',
    'ลบจากทุกหลักสูงสุด; ถ้าจะเป็น r’s เพิ่มหนึ่ง',
    [('ฐานสองเรียก (r−1)’s complement ว่าอะไร?',['1’s complement','2’s complement','9’s complement','biased-127'],0,'1’s complement'),('สูตร r’s complement ของ m ใน n หลักคืออะไร?','r^n−m ตามสูตรหน้า 14'),('จงหา 10’s complement ของ 382 ในสามหลักตามสไลด์','1000−382=618')],(13,14,15))

add('ones-complement','1’s complement และ end-around carry','core','หน้า 16–17',
    '1’s complement ของเลขฐานสองได้จากการกลับทุกบิต. แบบ 8 บิตมีช่วง −127 ถึง +127 และมีศูนย์สองรหัส; การบวกต้องนำ carry ที่หลุดออกมาบวกวนกลับ.',
    ['0101 กลับบิตเป็น 1010 ซึ่งสไลด์ใช้แทน −5 (หน้า 16)','8-bit: −127 ถึง +127; ศูนย์ 00000000 และ 11111111 (หน้า 16)','end-around carry นำ carry-out มาบวกเข้าผลลัพธ์ (หน้า 17)'],
    ['1’s complement','end-around carry','negative zero'],
    'ภาพหน้า 17 สาธิตบวก carry กลับเข้าผล; ใช้เพื่อดูขั้นตอนเท่านั้น',
    'หน้า 17 เรียกตัวอย่างว่า “3-bit add 6 and −3” ทั้งที่ 1’s complement 3 บิตแทน +6 ไม่ได้: ต้องตรวจสอบจากต้นฉบับ',
    'หนึ่งส์กลับทุกบิต; carry วนกลับ; ศูนย์สองแบบ',
    [('1’s complement หาอย่างไร?',['กลับทุกบิต','กลับ sign bit เท่านั้น','เติม bias','เลื่อนซ้ายหนึ่งบิต'],0,'กลับทุกบิตตามหน้า 16'),('end-around carry ทำอะไร?','นำ carry-out กลับไปบวกกับผลบวก'),('ทำไมตัวอย่าง 3-bit +6 หน้า 17 จึงควรตรวจต้นฉบับ?','3-bit 1’s complement มีช่วง −3 ถึง +3 จึงแทน +6 ไม่ได้')],(16,17))

add('twos-complement','2’s complement และการบวก','core','หน้า 18–22',
    '2’s complement หาโดยกลับบิตแล้วบวก 1 และใช้การบวกเลข signed ได้โดยทิ้ง carry ที่เกินความกว้าง. แบบ 8 บิตมีช่วง −128 ถึง +127 และศูนย์รหัสเดียว; ภาพเปรียบเทียบกับ Sign & Magnitude และ 1’s complement.',
    ['2’s = 1’s complement + 1 (หน้า 18–19)','8-bit: −128 ถึง +127; ศูนย์เดียว (หน้า 18,21–22)','4-bit: 0110 (+6) + 1011 (−5) = 0001 หลังทิ้ง carry (หน้า 20)'],
    ['2’s complement','carry-out','signed range −2^(n−1)..2^(n−1)−1'],
    'หน้า 19 ใช้ 0101011 → กลับบิต 1010100 → บวก 1 เป็น 1010101',
    'อย่าส่ง carry วนกลับแบบ 1’s complement; 2’s complement ทิ้ง carry ที่พ้นบิต',
    'ทูส์: กลับบิตบวกหนึ่ง; carry เกินทิ้ง; ศูนย์หนึ่ง',
    [('8-bit 2’s complement มีค่าต่ำสุดเท่าไร?',['−128','−127','0','−255'],0,'−128'),('หา 2’s complement จากเลขบวกอย่างไร?','กลับทุกบิตแล้วบวก 1'),('ตัวอย่าง 4-bit 6 + (−5) ในหน้า 20 ได้อะไร?','0110 + 1011 = 1 0001; ทิ้ง carry ได้ 0001 หรือ +1')],(18,19,20,21,22),(['แบบ','ศูนย์','ช่วง 8 บิต'],[['Sign & Magnitude','สองรหัส','−127..+127'],['1’s complement','สองรหัส','−127..+127'],['2’s complement','หนึ่งรหัส','−128..+127']]))

add('bias','Bias / Excess notation','core','หน้า 23–24',
    'Bias notation แปลบิตเป็น unsigned ก่อน แล้วลบค่า bias B เพื่อได้ค่าที่แทน. ตัวอย่าง 8 บิต B=127 ทำให้ 00000000 เป็น −127, 01111111 เป็น 0 และ 11111111 เป็น +128.',
    ['value = unsigned(bit pattern) − B (หน้า 23)','B=127: 00000000→−127; 01111111→0; 10000000→+1; 11111111→+128 (หน้า 24)'],
    ['Bias notation','Excess notation','biased-127'],
    'แปล 10000000 เป็น unsigned 128 แล้วลบ 127 ได้ +1 ตามตารางหน้า 24',
    'บิตบนสุดใน biased-127 ไม่ใช่ sign bit แบบ Sign & Magnitude',
    'อ่าน unsigned ก่อน ลบ Bias ทีหลัง',
    [('biased-127 ของ 01111111 คืออะไร?',['0','−1','+1','+127'],0,'127−127=0'),('สูตรแปล biased notation คืออะไร?','unsigned value − bias B'),('จงหาค่าของ 11111111 ใน biased-127','255−127=+128')],(23,24))

add('float-concept','Floating-point: sign, mantissa, exponent','core','หน้า 25–26',
    'Floating-point แยก sign, mantissa, exponent และ radix เพื่อแทนจำนวนที่มีจุดทศนิยมหรือสเกลใหญ่เล็ก. ในรูปฐานสอง สไลด์เขียน N = (−1)^s m 2^e.',
    ['รูปทั่วไปมี sign, mantissa, exponent, radix (หน้า 25)','N = (−1)^s m 2^e (หน้า 26)','ตัวอย่างฐานสิบ +3207.23 = 3.20723×10^3 และ −0.000321 = −3.21×10^−4 (หน้า 25)'],
    ['mantissa','exponent','radix','N = (−1)^s m 2^e'],
    'อ่านตัวอย่างหน้า 25 โดยแยกเครื่องหมาย ค่าสัมประสิทธิ์ และเลขชี้กำลัง',
    'mantissa ไม่ใช่ exponent; radix เป็นฐานของการยกกำลัง',
    'เครื่องหมาย–แมนทิสซา–ชี้กำลัง–ฐาน',
    [('สัญลักษณ์ e ใน N=(−1)^s m 2^e คืออะไร?',['exponent','sign','mantissa','bias'],0,'exponent'),('ส่วนประกอบ floating-point ที่หน้า 25 ระบุมีอะไร?','sign, mantissa, exponent และ radix'),('−0.000321 ในรูปที่สไลด์ยกเป็นอย่างไร?','−3.21×10^−4')],(25,26))

add('ieee-layout','IEEE single/double และ biased exponent','core','หน้า 27–29',
    'สไลด์เทียบ single precision 32 บิตกับ double precision 64 บิตตามช่อง sign/exponent/mantissa. สำหรับ single แบบ normalized ใช้ N=(−1)^s(1.m)2^(E−127), E=e+127; E=1..254 ให้ e=−126..+127 โดย 0 และ 255 ถูกสงวนสำหรับกรณีพิเศษตามสไลด์.',
    ['single = 1 sign + 8 exponent + 23 mantissa bits (หน้า 27)','double = 1 + 11 + 52 bits (หน้า 27)','single normalized: E=e+127; e=−126..+127 (หน้า 28–29)'],
    ['IEEE FPS ตามชื่อสไลด์','single/double precision','normalized 1.m','NaN','E/e'],
    'ตัวอย่าง e=4 จึง E=131 ในหน้า 31 เชื่อมสูตรหน้า 28',
    'หน้า 29 เขียน 2^128 เป็น “maximum representable” ทั้งที่ก่อนหน้าให้ m สูงสุด 2−2^−23; ค่านี้เป็นการประมาณขอบบน: ต้องตรวจสอบจากต้นฉบับ',
    'Single 1–8–23; Double 1–11–52; exponent บวก 127',
    [('single precision ใช้ exponent กี่บิต?',['8','11','23','52'],0,'8 บิต'),('สมการ normalized single ในสไลด์คืออะไร?','N=(−1)^s(1.m)2^(E−127)'),('ถ้า e=4 ค่า E เท่าไร?','4+127=131')],(27,28,29),(['รูปแบบ','รวม','sign','exponent','mantissa'],[['Single','32','1','8','23'],['Double','64','1','11','52']]))

add('binary-fraction','แปลงเศษส่วนฐานสองและตัวอย่าง single','important','หน้า 30–31',
    'เศษส่วนฐานสองมีน้ำหนักตำแหน่ง 2^−1, 2^−2 ต่อไปตามลำดับ; ตัวอย่าง 101.1101₂ = 5.8125₁₀. หน้า 31 ใช้ 17.15₁₀ เพื่อสาธิตการ normalize และเติม E=131 ใน single precision แต่เศษส่วนฐานสองที่พิมพ์เป็นเพียงค่าประมาณ.',
    ['101.1101₂ = 4+1+1/2+1/4+1/16 = 5.8125 (หน้า 30)','17.15 ตัวอย่างหน้า 31: exponent จริง e=4; E=131=10000011₂','bit sign =0 สำหรับตัวอย่างบวก (หน้า 31)'],
    ['binary fraction','normalization','biased exponent'],
    'แยกส่วนเต็ม 101₂=5 และเศษ .1101₂=.8125 ก่อนรวม (หน้า 30)',
    'หน้า 31 ใช้เครื่องหมายเท่ากับกับชุดบิตเศษส่วนที่ไม่ครบสำหรับ 17.15: ต้องตรวจสอบจากต้นฉบับ; อย่าจำว่า 17.15 มี binary สิ้นสุด',
    'จุดขยับเป็น 1.x; exponent ใส่ bias',
    [('101.1101₂ มีค่าเท่าไร?',['5.8125','5.625','6.8125','17.15'],0,'5.8125 ตามหน้า 30'),('การ normalize ตัวอย่าง 17.15 หน้า 31 ทำให้ e เท่าไร?','e=4'),('เหตุใดบิตของ 17.15 หน้า 31 ต้องอ่านเป็นค่าประมาณ?','เศษส่วนที่พิมพ์มีเพียงบางบิตและไม่ให้ค่า 17.15 แบบตรงทั้งหมด')],(30,31))

add('characters','อักขระ ASCII และ Unicode ในสไลด์','core','หน้า 32–38',
    'ข้อมูล qualitative รวมอักขระและ control symbols ซึ่งต้องแปลงเป็นรหัสบิตก่อนเก็บ. สไลด์กล่าวถึง ASCII, EBCDIC, Unicode; ASCII ใช้ 7 บิต 128 รหัส โดยมีทั้ง printable/control และยก A=0x41, a=0x61 ซึ่งต่างกัน 0x20.',
    ['ASCII = 7-bit/128 codes; สไลด์ยก parity bit เมื่อจัดเป็น byte (หน้า 33–34)','A=0x41, a=0x61; รหัสอักษรกับค่าตัวเลขเป็นคนละสิ่ง (หน้า 37)','หน้า 82 เพิ่ม ASCII 95 graphic+33 control, Latin-1 256 และ UTF-8/UTF-16 แบบความยาวแปรผัน'],
    ['ASCII','EBCDIC','Unicode','Latin-1','UTF-8/UTF-16','control character'],
    'ดูตาราง ASCII หน้า 35–36 เพื่อเทียบอักษรใหญ่/เล็กและรหัสตัวเลข',
    'หน้า 82 เรียก Unicode “32-bit character set” เป็นถ้อยคำของสไลด์; รายละเอียดมาตรฐานจริงเกินเอกสาร: ต้องตรวจสอบจากต้นฉบับ',
    'อักขระเป็นรหัส; รหัสเลขไม่ใช่ค่าเลข',
    [('ASCII พื้นฐานในสไลด์มีกี่รหัส?',['128','64','256','1024'],0,'128 รหัส 7 บิต'),('A กับ a ในตัวอย่างมีรหัส hex อะไร?','A=0x41; a=0x61'),('รหัสอักขระตัวเลขต่างจาก numeric value อย่างไร?','เก็บรหัสแทนตัวอักษร ไม่ใช่ค่าจำนวนสำหรับคำนวณโดยตรง')],(34,35,37))

add('isa-arithmetic','ISA และคำสั่งคำนวณสามตัวถูกดำเนินการ','core','หน้า 39–44',
    'ส่วน RISC-V เริ่มที่หน้า 39–40 แล้วอธิบาย ISA เป็นภาษาคำสั่งระดับเครื่องซึ่งต่างกันระหว่างสถาปัตยกรรม. รูปคำสั่ง arithmetic ใช้ destination และ source สองตัว เช่น add a,b,c; หลักการออกแบบที่สไลด์ย้ำคือ simplicity favors regularity.',
    ['RISC-V เป็น ISA แบบ open ตามคำบรรยายประวัติในสไลด์หน้า 42','add a,b,c หมายถึง a=b+c (หน้า 43)','f=(g+h)−(i+j) ใช้ add สองครั้งและ sub หนึ่งครั้ง (หน้า 44)'],
    ['ISA','RISC-V','add/sub','destination/source','simplicity favors regularity'],
    'หน้า 44 ใช้ t0=g+h, t1=i+j แล้ว f=t0−t1',
    'อย่าสลับ destination กับ source; ชื่อองค์กรดูแล RISC-V ในหน้า 42 เป็นข้อความตามสไลด์ ไม่ใช่ข้อมูลสถานะปัจจุบัน',
    'ปลายทางก่อน; แหล่งสองตัวตามหลัง',
    [('add a,b,c ให้ค่าใด?',['a=b+c','c=a+b','b=a+c','a=b−c'],0,'a=b+c'),('หลักการออกแบบที่หน้า 43 ย้ำคืออะไร?','simplicity favors regularity'),('ต้องใช้การคำนวณกี่ขั้นเพื่อทำ f=(g+h)−(i+j) ในหน้า 44?','สอง add เพื่อได้ผลย่อย แล้วหนึ่ง sub เพื่อหาผลลัพธ์')],(42,43,44))

add('registers','RISC-V register 32 ตัวและบทบาท','core','หน้า 45–47',
    'สไลด์ใช้ชุด integer register 32 ตัว กว้างตัวละ 64 บิตในบริบท RV64 โดยเรียกข้อมูล 64 บิตว่า doubleword และ 32 บิตว่า word. ชื่อ x0–x31 เชื่อมกับบทบาท เช่น x0 ค่าศูนย์, x1 return address, x2 stack pointer, x10–x17 arguments/results และกลุ่ม temporary/saved.',
    ['x0=0, x1=return address, x2=stack pointer (หน้า 46)','x5–x7,x28–x31 temporaries; x8 frame pointer; x9,x18–x27 saved (หน้า 46)','x10–x11 arguments/results; x12–x17 arguments (หน้า 46)'],
    ['x0–x31','word=32-bit','doubleword=64-bit','sp','return address','saved/temporary'],
    'หน้า 47 เขียนคำสั่งด้วยหมายเลข x5,x6,x19–x23 เพื่อแทนตัวแปรในนิพจน์',
    'อย่าเอาเลข register x10–x17 ไปตีความเป็นค่าตัวเลขที่เก็บอยู่',
    '0 คงศูนย์, 1 กลับ, 2 กองซ้อน, 10–17 ส่งค่า',
    [('register ใดเป็น stack pointer?',['x2','x0','x1','x10'],0,'x2'),('temporary registers ที่หน้า 46 ระบุมีกลุ่มใด?','x5–x7 และ x28–x31'),('word กับ doubleword ตามหน้า 45 ต่างกันอย่างไร?','word 32 บิต; doubleword 64 บิต')],(45,46,47))

add('memory-endian','Byte addressing, endian และ load/store','core','หน้า 48–51',
    'หน่วยความจำในสไลด์อ้าง address ทีละ byte และ RISC-V ใช้ little-endian ซึ่ง byte น้ำหนักต่ำอยู่ address ต่ำ. การคำนวณใช้ค่าที่ register; ต้อง load จาก memory ก่อนและ store ผลกลับเมื่อจำเป็น จึงมีตัวอย่าง A[12]=h+A[8] ที่คูณ index ด้วย 8 byte ต่อ doubleword.',
    ['ภาพหน้า 48 เทียบ big/little endian; หน้า 49 ระบุ RISC-V little-endian','ld/sd ย้าย doubleword ระหว่าง memory/register (หน้า 49–50)','A[8] offset 64, A[12] offset 96 จาก base x22 (หน้า 50)'],
    ['byte addressed','little-endian','big-endian','ld','sd','base+offset'],
    'ld x9,64(x22); add x9,x21,x9; sd x9,96(x22) ตามหน้า 50',
    'ตำแหน่ง array เป็น byte offset ไม่ใช่เลข index ตรง ๆ; หน้า 48 เป็นแผนภาพเปรียบเทียบ แต่หน้า 49 ระบุ RISC-V little-endian',
    'คูณ index ด้วย 8; load–add–store',
    [('A[8] แบบ doubleword มี byte offset เท่าไร?',['64','8','32','96'],0,'8×8=64'),('RISC-V ใช้ endian แบบใดตามหน้า 49?','little-endian'),('A[12] ในตัวอย่างเก็บกลับที่ offset เท่าไร?','12×8=96')],(48,49,50))

add('immediate-signed','Immediate และ signed/unsigned','core','หน้า 52–53',
    'addi ใช้ค่าคงที่ immediate โดยไม่ต้องโหลดค่าคงที่จาก memory. สไลด์ทวนช่วง unsigned n บิตและ signed 2’s complement พร้อมวิธี sign extension เมื่อโหลดข้อมูลขนาดเล็กเข้าสู่ register ที่กว้างกว่า.',
    ['addi x22,x22,4 เพิ่ม x22 อีก 4 (หน้า 52)','unsigned n-bit 0..2^n−1; signed n-bit −2^(n−1)..2^(n−1)−1 (หน้า 53)','sign extension คัดลอก sign bit ขึ้นไปยังบิตใหม่ (หน้า 53)'],
    ['addi','immediate','sign extension','signed/unsigned'],
    'หน้า 53 ยกการหา −2 จาก +2: กลับบิตแล้วบวก 1',
    'immediate เป็น operand ในคำสั่ง ไม่ใช่ address memory เสมอไป',
    'addi ใส่ค่าเลย; signed ขยายเครื่องหมาย',
    [('addi x22,x22,4 ทำอะไร?',['x22 เพิ่ม 4','x22 ลด 4','load memory offset 4','เก็บ x22 ที่ address 4'],0,'เพิ่ม x22 อีก 4'),('signed 2’s complement n บิตมีช่วงเท่าไร?','−2^(n−1) ถึง 2^(n−1)−1'),('sign extension ทำอย่างไร?','ทำบิตใหม่ด้านบนให้ตรงกับ sign bit ของค่าเดิม')],(52,53))

add('instruction-formats','R/I/S instruction formats และ encoding','core','หน้า 54–59',
    'RISC-V คำสั่งหลักในช่วงนี้กว้าง 32 บิต และสไลด์แจก field ของ R, I, S format. R มี funct7,rs2,rs1,funct3,rd,opcode; I ใช้ immediate 12 บิต; S แยก immediate สองช่วง. ตัวอย่าง add x9,x20,x21 ถูกแปลงเป็น hex 015A04B3.',
    ['R: 7+5+5+3+5+7=32 บิต (หน้า 55)','I: imm12,rs1,funct3,rd,opcode (หน้า 57)','S: imm[11:5],rs2,rs1,funct3,imm[4:0],opcode (หน้า 58)'],
    ['opcode','rd','rs1/rs2','funct3/funct7','R/I/S format','stored program'],
    'หน้า 56 ให้ add x9,x20,x21: funct7=0,rs2=21,rs1=20,funct3=0,rd=9,opcode=51 → 015A04B3₁₆',
    'S format ไม่มี rd ที่ตำแหน่งเดียวกับ R/I; immediate ถูกแบ่ง; หน้า 59 ย้ำคำสั่งกับข้อมูลอยู่ใน memory แบบ stored program',
    'R สอง source; I ค่าทันที; S กระจาย offset',
    [('R-format กว้างกี่บิต?',['32','16','64','12'],0,'32 บิต'),('field ของ S-format immediate แบ่งอย่างไร?','imm[11:5] และ imm[4:0]'),('add x9,x20,x21 ตามหน้า 56 มี hex อะไร?','015A04B3₁₆')],(54,55,56,57,58))

add('logical','Logical operations และ bit mask','core','หน้า 60–64',
    'สไลด์แนะนำ shift left/right, AND, OR, XOR และการทำ NOT ด้วย XOR กับบิตหนึ่งทั้งหมด. การ shift logical เลื่อนบิตพร้อมเติม 0; สำหรับ unsigned การเลื่อน i ตำแหน่งสัมพันธ์กับคูณ/หาร 2^i. AND ใช้ mask เลือกบิต, OR ใช้ตั้งบิต และ XOR ชี้ความต่างของบิต.',
    ['slli/srli เลื่อน logical; unsigned shift i ตำแหน่งสัมพันธ์กับ 2^i (หน้า 61)','AND ใช้ mask คงบิตที่ต้องการ (หน้า 62)','OR ตั้งบิต; XOR ให้ 1 เมื่อบิตต่างกัน; NOT ด้วย XOR all-ones (หน้า 63–64)'],
    ['slli','srli','AND/OR/XOR','mask','logical shift'],
    'ใช้ภาพ AND หน้า 62 ดูว่า mask 0 ลบบิตและ mask 1 รักษาบิต',
    'คำเปรียบเทียบคูณ/หาร 2^i ในสไลด์จำกัดบริบท unsigned; อย่าใช้กับ signed โดยไม่พิจารณาเงื่อนไข',
    'AND เลือก, OR ตั้ง, XOR ต่าง, Shift ขยับ',
    [('bitwise XOR ให้ 1 เมื่อใด?',['บิตต่างกัน','บิตเหมือนกัน','ทั้งคู่เป็น 0','ทั้งคู่เป็น 1 เท่านั้น'],0,'เมื่อบิตสองฝั่งต่างกัน'),('AND mask ใช้ทำอะไรตามหน้า 62?','รักษาบิตที่ mask เป็น 1 และตัดบิตที่ mask เป็น 0'),('shift unsigned ไปซ้าย i ตำแหน่งสัมพันธ์กับอะไร?','คูณ 2^i ตามหน้า 61')],(60,61,62,64))

add('branches','Branches, loop และ signed comparison','core','หน้า 65–70',
    'beq/bne เปลี่ยนทางเดินเมื่อสอง register เท่ากันหรือไม่เท่ากัน; blt/bge เปรียบเทียบลำดับและต้องแยก signed กับ unsigned. ตัวอย่าง if/else ใช้ branch ข้ามบล็อก ส่วน while คำนวณ address save[i], load, เปรียบเทียบ k, เพิ่ม i แล้ววน. สไลด์นิยาม basic block เป็นช่วงคำสั่งต่อเนื่องที่ไม่มี branch ภายในนอกจากท้าย.',
    ['beq = branch if equal; bne = branch if not equal (หน้า 65)','if/else หน้า 66: bne ไป Else, beq x0,x0 ไป Exit','loop หน้า 67: slli index 3 บิต → load → bne Exit → addi index → branch Loop','signed กับ unsigned ทำให้ bit pattern เดียวกันเทียบต่างกัน (หน้า 69–70)'],
    ['beq/bne','blt/bge','basic block','signed/unsigned branch'],
    'หน้า 70 ให้ x22 เป็น all-ones และ x23 เป็น +1: signed เห็น −1 < +1 แต่ unsigned เห็นค่ามากกว่า +1',
    'beq x0,x0 เป็น branch แบบไม่มีเงื่อนไขในตัวอย่าง; อย่าเทียบ signed/unsigned โดยดู bit pattern อย่างเดียว',
    'Equal/Not equal เลือกทาง; signed/unsigned เลือกความหมาย',
    [('bne branch เมื่อใด?',['ค่าต่างกัน','ค่าเท่ากัน','ค่าติดลบ','overflow'],0,'เมื่อสอง register ไม่เท่ากัน'),('basic block ตามหน้า 68 คืออะไร?','ช่วงคำสั่งต่อเนื่องที่ไม่มี branch ภายใน ยกเว้นท้าย และไม่มีเป้าหมาย branch ภายใน ยกเว้นต้น'),('all-ones เทียบ +1 แบบ signed กับ unsigned ต่างกันอย่างไร?','signed แปลเป็น −1 จึงน้อยกว่า +1; unsigned แปลเป็นค่าบวกสูง จึงมากกว่า +1')],(65,66,67,68,70))

add('procedure-convention','Procedure call, parameters และ return','core','หน้า 71–72',
    'การเรียก procedure ส่ง arguments ผ่าน x10–x17, เก็บตำแหน่งกลับใน x1 และรับผลใน register ผลลัพธ์ตามข้อตกลงที่สไลด์อธิบาย. jal x1,label กระโดดไป procedure พร้อมบันทึก return address; jalr x0,0(x1) ใช้กลับผู้เรียก.',
    ['x10–x17 รับ parameters; x10–x11 ใช้ผลลัพธ์ (หน้า 71,46)','jal x1,ProcedureLabel เก็บ return address แล้วกระโดด (หน้า 72)','jalr x0,0(x1) กลับ caller (หน้า 72)'],
    ['procedure','caller/callee','jal','jalr','return address'],
    'ไล่ขั้นหน้า 71: วาง parameter → transfer control → storage → operation → result → return',
    'x1 เป็นที่อยู่กลับ ไม่ใช่ register ผลลัพธ์',
    'ส่งค่า x10–17; กระโดด jal; กลับ jalr ผ่าน x1',
    [('return address อยู่ register ใด?',['x1','x0','x2','x10'],0,'x1'),('jal x1,label ทำอะไร?','บันทึกที่อยู่กลับใน x1 และย้าย control ไป label'),('คำสั่งกลับ caller ในหน้า 72 คืออะไร?','jalr x0,0(x1)')],(71,72))

add('leaf-stack','Leaf procedure และ stack save/restore','core','หน้า 73–76',
    'leaf procedure ในตัวอย่างคำนวณ f=(g+h)−(i+j) และไม่เรียก procedure อื่น แต่ยังใช้ stack บันทึก register ที่ต้องคืนค่าก่อนกลับ. stack pointer x2/sp ลดเมื่อจองที่ และเพิ่มเมื่อคืนพื้นที่; temporary กับ saved register มีข้อตกลงการรักษาค่าต่างกัน.',
    ['หน้า 73 กำหนด g,h,i,j ใน x10–x13 และผล f ใน x20','หน้า 74 จอง stack 24 byte, save x5,x6,x20 และ load คืนก่อนกลับ','x5–x7,x28–x31 ไม่ต้อง preserve โดย callee; x8–x9,x18–x27 ต้อง preserve เมื่อใช้งาน (หน้า 76)'],
    ['leaf procedure','stack frame','sp','callee-saved/temporary'],
    'อ่านภาพ stack หน้า 75 ร่วมกับลำดับ save→compute→restore หน้า 74',
    'หน้า 74 มี sd x20,0(sp ขาดวงเล็บ และ add x6,x12,x1 ทั้งที่ comment บอก i+j และหน้า 73 กำหนด j=x13: ต้องตรวจสอบจากต้นฉบับ อย่าจำบรรทัดนี้เป็นโค้ดที่ถูก',
    'จอง–เก็บ–คำนวณ–คืน–กลับ',
    [('leaf procedure ต่างจาก non-leaf อย่างไร?',['ไม่เรียก procedure อื่น','ไม่มี register','ไม่ใช้ stack ได้เสมอ','ไม่มี return'],0,'leaf ไม่เรียก procedure อื่น'),('กลุ่ม saved register หน้า 76 คืออะไร?','x8–x9 และ x18–x27 (x8 เป็น frame pointer ด้วย)'),('เพราะเหตุใด add x6,x12,x1 หน้า 74 ต้องตรวจต้นฉบับ?','x1 เป็น return address แต่คำอธิบายต้องการ i+j และหน้า 73 ระบุ j ใน x13')],(73,74,75,76))

add('nonleaf-recursion','Non-leaf procedure และ factorial recursion','core','หน้า 77–79',
    'non-leaf procedure เรียก procedure อื่น จึงต้องรักษา return address และค่าที่ยังต้องใช้หลังการเรียก. ตัวอย่าง factorial ใช้ stack เก็บ x1 กับ n ใน x10, เรียก fact(n−1), โหลดค่ากลับ แล้วคูณก่อน return.',
    ['non-leaf ต้องรักษา return address และ live values ข้ามการเรียก (หน้า 77)','ตัวอย่าง fact หน้า 79 จอง 16 byte; save x1 ที่ 8(sp), x10 ที่ 0(sp)','base case ใน assembly หน้า 79 ตั้ง x10=1; recursive case คูณ n×fact(n−1)'],
    ['non-leaf','recursion','stack frame','live values','factorial'],
    'ไล่หน้า 79 จาก save → ตรวจ n<1 → call fact → restore n/x1 → mul → return',
    'หน้า 78 C เขียน return f ซึ่งไม่ได้กำหนด แต่ assembly หน้า 79 base case คืน 1; หน้า 79 ยังตั้งหัวข้อ Leaf ทั้งที่เป็น recursion: ต้องตรวจสอบจากต้นฉบับ',
    'เรียกซ้อนต้องเก็บทางกลับและค่าที่จะใช้ต่อ',
    [('non-leaf ต้องรักษาอะไรเป็นพิเศษ?',['return address และค่าที่ยังใช้อยู่','x0 อย่างเดียว','opcode','endian'],0,'return address และ live values'),('ตัวอย่าง factorial เก็บ x1 และ x10 ที่ไหน?','บน stack หลังจอง 16 byte: x1 ที่ 8(sp), x10 ที่ 0(sp)'),('base case ของ C/assembly ในหน้า 78–79 ขัดกันอย่างไร?','C ระบุ return f ที่ไม่ประกาศ; assembly ตั้งผลเป็น 1')],(77,78,79))

add('memory-layout-char','Memory layout, activation record และข้อมูลขนาดย่อย','important','หน้า 80–83',
    'ภาพ layout วาง text, static data, heap และ stack คนละบริเวณ; activation record เก็บบริบทของ procedure. คำสั่ง load ขนาด byte/halfword/word มีแบบ sign-extend และ zero-extend ส่วน store เขียนเพียงบิตต่ำตามขนาดข้อมูล.',
    ['text/static data/heap/stack ตามภาพหน้า 80','activation record ตามหน้า 81 ใช้จัด context ของ call','lb/lh/lw sign-extend; lbu/lhu/lwu zero-extend; sb/sh/sw เก็บ 8/16/32 บิตต่ำ (หน้า 83)'],
    ['text','static data','heap','stack','activation record','lb/lbu','sb'],
    'เทียบ lb กับ lbu เมื่อ byte บิตบนสุดเป็น 1: แบบแรกขยาย sign แบบหลังเติม 0 (หน้า 83)',
    'อย่าเหมารวม load ทุกแบบเป็น sign extension; ชื่อที่ลงท้าย u คือ unsigned/zero extension',
    'มี u เติมศูนย์; ไม่มี u ขยายเครื่องหมาย',
    [('lbu ขยาย byte แบบใด?',['zero-extend','sign-extend','rotate','ไม่ขยาย'],0,'zero-extend'),('memory layout หน้า 80 แบ่งหลัก ๆ อย่างไร?','text, static data, heap และ stack'),('sb เก็บกี่บิตต่ำตามหน้า 83?','8 บิต')],(80,81,82,83))

add('strcpy','Self-study: String copy','important','หน้า 84–86',
    'หน้า 84 แยกส่วนถัดไปเป็น Self-study. ตัวอย่าง strcpy วนคัดลอกอักขระจาก source ไป destination ทีละ byte จนพบ NUL แล้วคืน stack/register; นำมาใช้ฝึกอ่าน address, lbu, sb และ branch.',
    ['string จบเมื่อ byte เป็น 0 (หน้า 85–86)','lbu อ่าน byte, sb เขียน byte, beq ตรวจ NUL (หน้า 86)','ใช้ x19 เป็น index และ stack บันทึก x19 (หน้า 86)'],
    ['Self-study','strcpy','NUL','lbu/sb'],
    'ติดตามหนึ่งรอบ loop: หา address source → lbu → หา address destination → sb → ตรวจ 0 → เพิ่ม index',
    'หน้า 86 เขียน add x5,x19,x10 แต่ comment ว่า address ของ y[i], ขณะที่ x10 เป็น x และ x11 เป็น y ตามตัวอย่าง: ต้องตรวจสอบจากต้นฉบับ',
    'อ่านหนึ่งไบต์–เขียนหนึ่งไบต์–เช็กศูนย์',
    [('strcpy หยุดเมื่อเจออะไร?',['NUL byte','space','ตัวอักษร A','ครบ 8 byte'],0,'NUL byte หรือ 0'),('หน้า 86 ใช้คำสั่งใดอ่านและเขียน byte?','lbu อ่าน; sb เขียน'),('จุดขัดกันของ address y[i] หน้า 86 คืออะไร?','comment ว่า y[i] แต่บรรทัดใช้ x10 ซึ่งเป็น x ตามการกำหนด register ในตัวอย่าง')],(84,85,86))

add('wide-immediate','Self-study: Wide immediate และ branch address','important','หน้า 87–91',
    'ค่าคงที่ขนาดเกิน immediate 12 บิตประกอบด้วย lui เติมส่วนบนแล้ว addi เติมส่วนล่าง. สไลด์อธิบาย branch address แบบ PC-relative, jump ด้วย JAL และการประกอบ jump ไกลด้วย LUI/JALR พร้อมภาพสรุปรูปแบบ addressing/encoding.',
    ['lui วาง constant 20 บิตที่ [31:12] และล้าง [11:0] (หน้า 87)','ตัวอย่าง lui x19,976; addi x19,x19,128 (หน้า 87)','branch target = PC + immediate×2 ตามหน้า 88; JAL และ JALR หน้า 89'],
    ['lui','addi','PC-relative','SB/UJ format','JAL/JALR'],
    'ถ้าตีตามตัวเลขคำสั่ง 976×4096+128 = 0x003D0080',
    'หน้า 87 comment ที่ addi 128 เขียน 0x500 และภาพบิตท้าย 0101 0000 0000 (=0x500), ไม่ตรงกับ 128 (=0x080): ต้องตรวจสอบจากต้นฉบับ',
    'lui เติมบน; addi เติมล่าง; branch อิง PC',
    [('lui เติม constant กี่บิตในช่องบน?',['20','12','8','32'],0,'20 บิต'),('branch target ตามหน้า 88 คำนวณอย่างไร?','PC + immediate×2'),('ทำไมตัวอย่าง addi 128 หน้า 87 ต้องตรวจต้นฉบับ?','128 เป็น 0x080 แต่ comment/ภาพแสดง 0x500')],(87,88,89,90,91))

add('atomics','Self-study: Atomic operations','important','หน้า 92–94',
    'เมื่อหลายหน่วยทำงานกับข้อมูลร่วมกัน อาจเกิด data race จึงต้องมีการอ่านและเขียนแบบ atomic. สไลด์ใช้ lr.d เพื่ออ่านพร้อม reservation แล้ว sc.d พยายามเขียน; sc.d คืน 0 เมื่อสำเร็จและ nonzero เมื่อไม่สำเร็จ จึงวนลองใหม่ได้.',
    ['data race เกิดจาก access ร่วมที่ลำดับเวลาเปลี่ยนผล (หน้า 92)','lr.d อ่านและตั้ง reservation; sc.d เขียนแบบมีเงื่อนไข (หน้า 93)','sc.d สำเร็จคืน 0; ล้มเหลวคืน nonzero; หน้า 94 แสดง retry และ unlock ด้วย sd x0,0(x20)'],
    ['data race','atomic','lr.d','sc.d','reservation'],
    'ตามลูกศร retry หน้า 94 เมื่อ sc.d ไม่สำเร็จแล้วลองใหม่',
    'อย่าสับสนค่า 0 จาก sc.d กับค่าข้อมูลที่ต้องการเขียน; เป็นสถานะสำเร็จ',
    'LR จอง; SC ลองเขียน; ศูนย์คือสำเร็จ',
    [('sc.d คืนค่าอะไรเมื่อสำเร็จ?',['0','1','−1','address'],0,'0'),('lr.d ทำหน้าที่อะไร?','load พร้อมสร้าง reservation สำหรับคู่ sc.d'),('เหตุใดตัวอย่างหน้า 94 จึงต้อง retry?','sc.d อาจล้มเหลวหาก reservation ไม่คงอยู่/ข้อมูลถูกเปลี่ยน')],(92,93,94))

add('translation-runtime','Self-study: จาก source ไป executable และ runtime','important','หน้า 95–101',
    'สไลด์ไล่ source ผ่าน compiler/assembler/linker/loader ไปจนรันโปรแกรม. Object module มี text/data/relocation/symbol/debug; linker รวมและแก้ references, loader วางใน memory และเริ่ม main. ช่วงท้ายยก dynamic linking และ Java VM/JIT เป็นแนวทางเชื่อม/แปลตอนรัน.',
    ['object module: header,text,static data,relocation,symbol,debug (หน้า 96)','linker merge object files, resolve symbols, patch locations (หน้า 97)','loader จัด memory/text/data/stack/registers แล้วเริ่มโปรแกรม (หน้า 98)','dynamic linking กับ lazy linkage หน้า 99–100; JVM/JIT หน้า 101'],
    ['compiler','assembler','object module','linker','loader','dynamic linking','JVM/JIT'],
    'อ่านภาพหน้า 95 เป็นสายงาน source→object→executable→memory แล้วจับคู่หน้าที่หน้า 96–98',
    'linker แก้การเชื่อม object files; loader นำ executable ลง memory; อย่าสลับสองขั้น',
    'แปล–รวม–โหลด–รัน',
    [('ขั้นใด resolve symbols ระหว่าง object files?',['linker','loader','register','ALU'],0,'linker'),('object module หน้า 96 มีส่วนสำคัญใดบ้าง?','header, text, static data, relocation, symbol และ debug'),('dynamic linking ต่างจาก static link ในจังหวะใดตามสไลด์?','เชื่อม library บางส่วนขณะรัน/เมื่อจำเป็น แทนการรวมทั้งหมดก่อนรัน')],(95,96,97,98,100,101))

add('swap','Self-study: Swap procedure','important','หน้า 102–103',
    'ตัวอย่าง swap รับ base address กับ index แล้วคำนวณตำแหน่งของ v[k] และ v[k+1] โดยเลื่อน index ซ้าย 3 บิตสำหรับ doubleword. จากนั้น load สองค่าและ store สลับตำแหน่ง ก่อน return.',
    ['shift left 3 = index×8 byte (หน้า 103)','ld จาก offset 0 และ 8 แล้ว sd กลับสลับค่า (หน้า 103)','เป็น leaf procedure ในตัวอย่างหน้า 102–103'],
    ['swap','index×8','ld/sd'],
    'ติดตาม address base+8k แล้วอีกตำแหน่งคือ base+8k+8',
    'อย่าสลับ offset 8 byte ของสมาชิกถัดไปกับ index k+1 ที่ต้องคูณ 8',
    'คูณ 8–โหลดคู่–เก็บสลับ',
    [('สมาชิก doubleword ถัดไปห่างกี่ byte?',['8','1','4','16'],0,'8 byte'),('swap หน้า 103 คำนวณ address v[k] อย่างไร?','base address + k×8'),('swap สลับค่าด้วยคำสั่ง memory กลุ่มใด?','ld สองค่า แล้ว sd กลับสลับตำแหน่ง')],(102,103))

add('sort','Self-study: Sort loops และการรักษา register','important','หน้า 104–107',
    'ตัวอย่าง sort แยก outer loop และ inner loop เพื่อตรวจลำดับสมาชิกติดกันแล้วเรียก swap เมื่อจำเป็น. การเรียก swap ทำให้ sort เป็น non-leaf และต้องรักษา register ที่ใช้ต่อ รวมถึง return address ตามภาพ stack หน้า 107.',
    ['หน้า 104 ให้ C sort กับตัวแปร i,j และการเรียก swap','หน้า 105 outer loop; หน้า 106 inner loop ตรวจ j≥0 และ v[j]>v[j+1]','หน้า 107 จอง 40 byte สำหรับ register 5 ตัวในตัวอย่าง'],
    ['outer/inner loop','non-leaf sort','swap','save/restore'],
    'หน้า 106 ใช้ slli j,3 เพื่อเข้าถึง doubleword สองตัวติดกัน ก่อน branch และ call swap',
    'หน้า 107 หัวข้อ Restore saved registers แต่ใช้ sd ทุกบรรทัดซึ่งเป็น store ไม่ใช่ load: ต้องตรวจสอบจากต้นฉบับ อย่าคัดลอกเป็นขั้น restore ที่ถูก',
    'วนรอบนอก–เทียบคู่ใน–swap–คืนค่าที่เก็บ',
    [('sort เรียก procedure ใดในตัวอย่าง?',['swap','strcpy','fact','loader'],0,'swap'),('inner loop หน้า 106 ตรวจอะไร?','j≥0 และ v[j]>v[j+1] ก่อนเรียก swap'),('เหตุใด restore หน้า 107 ต้องตรวจต้นฉบับ?','บรรทัดใต้ Restore ใช้ sd ซึ่งเขียน memory ไม่ได้โหลดค่ากลับเข้า register')],(104,105,106,107))

add('optimization','Self-study: บทเรียนจากการวัดผลและ compiler','extra','หน้า 108–110',
    'กราฟเปรียบเทียบผลของ optimization และภาษา/algorithm ภายใต้ตัวอย่างในสไลด์. บทเรียนสรุปว่า instruction count หรือ CPI เดี่ยว ๆ ไม่พออธิบาย performance ทั้งหมด; ผลของ optimization ขึ้นกับ algorithm และ JIT ต่างจาก interpreter ตามการใช้งาน.',
    ['อ่านกราฟหน้า 108–109 เป็นการเปรียบเทียบกรณีตัวอย่าง ไม่ใช่ค่ามาตรฐาน','หน้า 110 ย้ำ algorithm สำคัญ และไม่มีเทคนิคใดแก้ algorithm ที่ไม่เหมาะได้ทั้งหมด'],
    ['instruction count','CPI','compiler optimization','JIT/interpreter'],
    'ใช้กราฟหน้า 108–109 ชี้ว่าการเปลี่ยน algorithm/ภาษา/optimization อาจเปลี่ยนเวลา',
    'อย่าทำนายผล performance จาก CPI เพียงตัวเดียวตามบทเรียนหน้า 110',
    'เริ่มที่ algorithm; วัดเวลาจริงและบริบท',
    [('สไลด์หน้า 110 เตือนเรื่องใด?',['CPI อย่างเดียวไม่พอ','CPI บอกทุกอย่าง','algorithm ไม่สำคัญ','JIT เร็วเสมอ'],0,'CPI อย่างเดียวไม่พอ'),('ทำไมกราฟหน้า 108–109 ไม่ควรใช้เป็นตัวเลขสากล?','เป็นผลเปรียบเทียบของกรณี/สภาพแวดล้อมในสไลด์'),('ถ้า algorithm ไม่เหมาะ optimization อย่างเดียวช่วยได้เสมอหรือไม่?','ไม่; หน้า 110 ย้ำว่าการเลือก algorithm มีผลสำคัญ')],(108,109,110))

add('arrays-pointers','Self-study: Array indexing เทียบ pointer','important','หน้า 111–113',
    'สไลด์เทียบ loop ล้าง array ด้วย index กับ pointer แล้วแสดง assembly สองแนว. แบบ index คำนวณ offset จาก i; แบบ pointer เพิ่ม address ไปทีละ element. ประเด็นคือ compiler อาจ optimize การคำนวณ address ได้ และควรเลือกโค้ดที่อ่านและตรวจได้.',
    ['หน้า 112 เปรียบเทียบ clear1(array[i]) กับ clear2(*p)','assembly ตัวอย่างใช้ slli index,3 และ pointer increment 8 (หน้า 112)','หน้า 113 อธิบาย compiler optimization ทำให้ความต่างของรูปเขียนไม่ตายตัว'],
    ['array indexing','pointer','address arithmetic','compiler optimization'],
    'ไล่ภาพหน้า 112 ว่า x7 เป็น endpoint ในแบบ pointer และ x6 เป็น byte offset ในแบบ index',
    'C ตัวอย่างประกาศ int แต่ assembly เลื่อน 3/เพิ่ม 8 เป็นขนาด doubleword; ไม่สอดคล้องกัน: ต้องตรวจสอบจากต้นฉบับ',
    'index คูณขนาด; pointer เดินทีละช่อง',
    [('แบบ pointer เลื่อนอะไรในแต่ละรอบ?',['address','opcode','bias','return address'],0,'address ของ pointer'),('แบบ index หา address สมาชิกอย่างไร?','base + index×ขนาดสมาชิก'),('เหตุใด C กับ assembly หน้า 112 ต้องตรวจต้นฉบับ?','C ใช้ int แต่ assembly ใช้ stride 8 byte')],(111,112,113))

add('isa-comparison-extensions','Self-study: MIPS เทียบ RISC-V และ extensions','extra','หน้า 114–117',
    'ท้ายบทเทียบ MIPS ซึ่งเป็นสถาปัตยกรรมก่อนหน้ากับ RISC-V ผ่านตาราง/รูป encoding แล้วสรุป RV64I/RV32I และกลุ่ม extension. ตัวอักษร M, A, F, D, C แสดงชุดความสามารถเพิ่มเติมตามรายการในสไลด์.',
    ['หน้า 114–115 เทียบ MIPS/RISC-V และ instruction encoding','หน้า 116 ระบุ RV64I/RV32I และคำสั่ง word บางแบบ','หน้า 117: M=integer multiply/divide, A=atomic, F=single float, D=double float, C=compressed'],
    ['MIPS','RV64I/RV32I','M/A/F/D/C extensions'],
    'อ่านตารางหน้า 117 แล้วจับคู่ชื่อ extension กับหน้าที่',
    'หน้า 116 มีชื่อ srlw ซ้ำในรายการที่ควรต่างกัน: ต้องตรวจสอบจากต้นฉบับ; อย่าอนุมานรายการแก้ไขเอง',
    'M คูณหาร, A atomic, F/D float, C compressed',
    [('extension A หมายถึงอะไร?',['Atomic','Address','ASCII','Array'],0,'Atomic'),('F กับ D ในหน้า 117 ต่างกันอย่างไร?','F เป็น single-precision floating point; D เป็น double-precision floating point'),('รายการคำสั่งหน้า 116 จุดใดต้องตรวจต้นฉบับ?','มี srlw ซ้ำในรายการ')],(114,115,116,117))

figure_pages = [5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,37,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,60,61,62,64,65,66,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117]
page_text = {p['page']:p['text'] for p in json.loads((HERE/'pages.json').read_text(encoding='utf-8'))}
caption_override = {
  17:'แผนภาพ end-around carry; ตัวอย่าง 3 บิตกับ +6 เกินช่วงที่แทนได้: ต้องตรวจสอบจากต้นฉบับ',
  31:'ตัวอย่าง single precision ของ 17.15; บิตเศษส่วนที่แสดงเป็นค่าโดยประมาณ: ต้องตรวจสอบจากต้นฉบับ',
  74:'โค้ด leaf procedure บันทึกและคืน register; บรรทัดคำนวณ i+j ไม่ตรงกับ register ที่กำหนด: ต้องตรวจสอบจากต้นฉบับ',
  78:'C factorial แบบ non-leaf; base case เขียน return f ที่ไม่ได้กำหนด: ต้องตรวจสอบจากต้นฉบับ',
  79:'Assembly factorial เก็บ return address และ n บน stack; หัวข้อ Leaf ขัดกับการเรียกตัวเอง: ต้องตรวจสอบจากต้นฉบับ',
  86:'Assembly strcpy โหลดและเขียนทีละ byte; comment address y[i] ไม่ตรงกับ register: ต้องตรวจสอบจากต้นฉบับ',
  87:'ตัวอย่าง lui+addi สร้างค่าคงที่; addi 128 ไม่ตรงกับภาพ/comment 0x500: ต้องตรวจสอบจากต้นฉบับ',
  107:'ตัวอย่าง save/restore register ของ sort; ส่วน restore ใช้ sd แทน load: ต้องตรวจสอบจากต้นฉบับ',
  112:'เทียบ clear array แบบ index และ pointer; C ระบุ int แต่ assembly ขยับ 8 byte: ต้องตรวจสอบจากต้นฉบับ',
}
def page_heading(page):
    lines = [line.strip(' •\t') for line in page_text[page].splitlines() if line.strip()]
    lines = [line for line in lines if not line.startswith(('ITDS-211:', 'W.Suntiamorntut', 'Chapter 2 —', 'Mahidol University', '©'))]
    return next((line for line in lines if len(line)>4 and not line.startswith(('','','•'))), '')

figures = []
for p in figure_pages:
    owner = next(t for t in topics if f'fig-{p}' in t['figures'])
    heading = page_heading(p) or owner['title']
    details = caption_override.get(p, f'สไลด์แสดง {heading} เพื่อทบทวนหัวข้อ {owner["title"]}')
    figures.append(dict(id=f'fig-{p}',page=p,file=f'slide-{p:03d}.png',
        title=f'{heading} · หน้า {p}',
        caption=f'{details} ({SOURCE}, หน้า {p})'))

flashcards = [dict(front=t['title'],back=t['remember'][0],pages=t['pages']) for t in topics]
term_cards = [
 ('Unsigned n บิต','0 ถึง 2^n−1','หน้า 5'),
 ('Sign & Magnitude','หนึ่ง sign bit และ n magnitude bits; มีศูนย์สองรหัส','หน้า 10–11'),
 ('(r−1)’s complement','(r^n−1)−m','หน้า 14'),
 ('r’s complement','r^n−m','หน้า 14'),
 ('1’s complement','กลับทุกบิตของค่าฐานสอง','หน้า 16'),
 ('end-around carry','นำ carry-out กลับมาบวกกับผลรวม','หน้า 17'),
 ('2’s complement','กลับทุกบิตแล้วบวก 1','หน้า 18–19'),
 ('biased-127','ค่า unsigned ของบิตลบด้วย 127','หน้า 23–24'),
 ('Floating-point N','N=(−1)^s m 2^e','หน้า 26'),
 ('IEEE single fields','sign 1, exponent 8, mantissa 23 บิต','หน้า 27'),
 ('IEEE double fields','sign 1, exponent 11, mantissa 52 บิต','หน้า 27'),
 ('Single exponent bias','E=e+127 ใน normalized form','หน้า 28'),
 ('ASCII','7 บิต 128 รหัสตามสไลด์','หน้า 33–34'),
 ('add a,b,c','a=b+c','หน้า 43'),
 ('x0','ค่าคงที่ 0','หน้า 46'),
 ('x1','return address','หน้า 46, 72'),
 ('x2/sp','stack pointer','หน้า 46, 74'),
 ('word / doubleword','32 บิต / 64 บิตในตัวอย่าง RV64','หน้า 45'),
 ('little-endian','byte น้ำหนักต่ำอยู่ address ต่ำตามหน้า 49','หน้า 49'),
 ('addi','คำสั่งบวกค่าคงที่ immediate','หน้า 52'),
 ('R-format fields','funct7, rs2, rs1, funct3, rd, opcode','หน้า 55'),
 ('I-format immediate','immediate 12 บิต','หน้า 57'),
 ('S-format immediate','แยก imm[11:5] และ imm[4:0]','หน้า 58'),
 ('beq / bne','branch เมื่อเท่ากัน / ไม่เท่ากัน','หน้า 65'),
 ('jal / jalr','เรียก procedure พร้อม link / กลับผ่าน return address','หน้า 72'),
 ('leaf / non-leaf','ไม่เรียก procedure อื่น / เรียก procedure อื่น','หน้า 73, 77'),
 ('lbu / lb','โหลด byte แบบ zero extension / sign extension','หน้า 83'),
 ('lr.d / sc.d','load-reserved / store-conditional เพื่อทำ atomic operation','หน้า 93'),
 ('linker / loader','รวมและแก้ reference / วาง executable ใน memory เริ่มรัน','หน้า 97–98'),
 ('M/A/F/D/C','multiply-divide / atomic / single float / double float / compressed','หน้า 117'),
]
flashcards += [dict(front=f,back=b,pages=p) for f,b,p in term_cards]

data = dict(
 source=SOURCE,sourcePageCount=118,
 course='ITDS-211 · Computer Architecture & Operating System',
 instructor='W. Suntiamorntut, Ph.D.',
 chapter='Chapter03 · Data Representation & RISC-V ISA',
 description='จากบิตและรูปแบบข้อมูล สู่ register, คำสั่ง, memory, control flow และ procedure ของ RISC-V',
 notice='อ่านเลขหน้าเป็นหน้า PDF (1–118) ไม่ใช่เลขท้ายสไลด์จากตำรา; หน้า 84 เป็นต้นไปมีป้าย Self-study และมีจุดไม่สอดคล้องในตัวอย่างหลายหน้า ซึ่งระบุให้ตรวจต้นฉบับแล้ว',
 purpose='บทนี้ช่วยให้เห็นว่าข้อมูลจำนวนและอักขระถูกเข้ารหัสในบิตอย่างไร แล้วเชื่อมรหัสนั้นกับ ISA ของ RISC-V: คำสั่งอ่าน/เขียน memory, คำนวณ, เปลี่ยนทางเดิน และเรียก procedure จนถึงกระบวนการสร้างโปรแกรม',
 purposePages='หน้า 4–37, 39–117',
 objectiveNote='รายการวัตถุประสงค์รายบทที่ระบุเป็นข้อชัดเจน: ต้องตรวจสอบจากต้นฉบับ; เป้าหมายต่อไปนี้สังเคราะห์จากหัวข้อที่ปรากฏในสไลด์',
 flashcardNote='Flashcards ใช้คำศัพท์และกฎจากสไลด์; บางใบเป็นคำช่วยทวน ไม่ใช่นิยามเต็ม จึงควรเปิดหัวข้อและภาพประกอบก่อนตอบข้อสอบ',
 goals=[
   dict(text='แปลจำนวนใน unsigned, Sign & Magnitude, complement, bias และ floating-point พร้อมชี้ข้อจำกัด',pages='หน้า 4–31'),
   dict(text='แยก encoding อักขระจากค่าตัวเลข และอ่าน ASCII ตามตารางต้นฉบับ',pages='หน้า 32–37, 82'),
   dict(text='อ่าน register, memory, instruction formats, logical/branch และ procedure ของ RISC-V',pages='หน้า 41–83'),
   dict(text='ใช้ส่วน Self-study ฝึกตามโค้ดและแผนภาพ toolchain, atomics, sort, array และ extensions โดยระบุจุดขัดกัน',pages='หน้า 84–117')],
 limits=[
   'ตรวจครบ 118 หน้า: หน้า 1 ปก, 2 Course Outline, 3/39/40/84 หน้าเปิดส่วน, 38 Assignment2, 118 Q&A; หน้า 84–117 ระบุ Self-study',
   'ไม่มีรายการ Chapter Objectives เฉพาะบทอย่างชัดเจน: ต้องตรวจสอบจากต้นฉบับ',
   'ไม่มีข้อสอบเก่าหรือน้ำหนักคะแนน จึงให้ระดับความสำคัญจากความเป็นนิยาม/สูตร/ขั้นตอน/ตัวอย่างในสไลด์ ไม่อ้างว่าจะออกจริง',
   'หน้า 17 ตัวอย่าง 3-bit 1’s complement กับ +6 เกินช่วง; หน้า 31 การแปลง 17.15 ใช้บิตเศษส่วนไม่ครบ: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 15 ตัวอย่างฐานสิบเขียนชื่อ 1’/2’ complement ทั้งที่สูตรหน้า 13–14 จับคู่ฐานสิบกับ 9’s/10’s: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 74 add x6,x12,x1 ไม่ตรงกับ i+j; หน้า 78 C base case return f ไม่กำหนด; หน้า 79 หัวข้อเรียก Leaf ทั้งที่ recursive: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 86 address y[i] ใช้ x10 ตาม code/comment ที่ไม่ตรง; หน้า 87 addi 128 แต่ภาพ/comment 0x500: ต้องตรวจสอบจากต้นฉบับ',
   'หน้า 107 หัวข้อ restore แต่คำสั่งเป็น sd; หน้า 112 C int แต่ assembly stride 8; หน้า 116 มี srlw ซ้ำ: ต้องตรวจสอบจากต้นฉบับ',
   'ภาพบางหน้ามีข้อความ/รหัสจำนวนมาก จึงเก็บสไลด์ต้นทางในแกลเลอรีให้ขยายดู; สรุปไม่ได้คัดโค้ดยาวจากภาพ'],
 figures=figures,topics=topics,
 roadmap=[
   dict(title='1 · รูปแบบข้อมูล',text='เริ่มชนิดข้อมูลและ unsigned ก่อนเลือกวิธีแทน signed',pages='หน้า 4–8',topic='data-map'),
   dict(title='2 · Signed representation',text='เทียบ Sign & Magnitude → complement → 2’s → bias พร้อมช่วงค่า/ศูนย์',pages='หน้า 9–24',topic='sign-magnitude'),
   dict(title='3 · Floating และอักขระ',text='ต่อ floating-point, IEEE, binary fraction แล้วค่อย ASCII',pages='หน้า 25–37',topic='float-concept'),
   dict(title='4 · ISA และข้อมูลในเครื่อง',text='RISC-V arithmetic → register → memory/endianness → signed/immediate',pages='หน้า 41–53',topic='isa-arithmetic'),
   dict(title='5 · คำสั่งและ control flow',text='อ่าน R/I/S encoding ก่อน logical operations และ branch/loop',pages='หน้า 54–70',topic='instruction-formats'),
   dict(title='6 · Procedure',text='call/return → leaf stack → non-leaf recursion → memory layout',pages='หน้า 71–83',topic='procedure-convention'),
   dict(title='7 · Self-study',text='String/wide immediate → atomic/toolchain → swap/sort → optimization/array/extensions',pages='หน้า 84–117',topic='strcpy')],
 plan=[
   dict(title='รอบ 1 · อ่านภาพรวม',task='อ่านตาม roadmap และเปิดภาพต้นฉบับทุกหัวข้อ พร้อมทำเครื่องหมายสูตร/field/register ที่ยังจำไม่ได้',check='อธิบายว่าบทนี้ต่อจากรหัสข้อมูลไปถึงการรันโปรแกรมอย่างไร',pages='หน้า 4–117'),
   dict(title='รอบ 2 · แกนคำนวณ',task='ฝึกช่วงค่า signed/unsigned, 1’s/2’s/bias, IEEE และ byte offset ด้วยตัวอย่างจากสไลด์',check='คำนวณ 6+(−5), biased-127 และ A[8]/A[12] ได้ พร้อมชี้ตัวอย่างผิด',pages='หน้า 9–31, 49–53'),
   dict(title='รอบ 3 · ภาษาเครื่อง',task='ท่อง register/format แล้วไล่ arithmetic, load/store, logical, branch และ procedure ด้วยภาพ',check='อ่าน add x9,x20,x21 และ jal/jalr พร้อม field/บทบาท register ได้',pages='หน้า 41–83'),
   dict(title='รอบ 4 · Self-study',task='ไล่ภาพ/โค้ดประกอบเฉพาะหน้า 84–117 และจดจุดที่ต้องตรวจจากต้นฉบับ',check='อธิบาย strcpy, lr/sc, linker/loader, swap/sort และ extensions ได้',pages='หน้า 84–117'),
   dict(title='รอบ 5 · ทดสอบเว้นระยะ',task='สุ่มแบบทดสอบ/Flashcard; ทวนเฉพาะข้อผิดแล้วกลับมาทำใหม่ในวันถัดไปตามเวลาที่มี',check='ตอบคำถาม 3 ข้อต่อหัวข้อครบ และแยกข้อที่สไลด์ขัดกันได้',pages='หน้า 4–117')],
 cram=[
   dict(title='ถ้าเหลือ 3 วัน',text='วัน 1 จำนวน/IEEE/ASCII หน้า 4–37; วัน 2 RISC-V register/memory/format/branch/procedure หน้า 41–83; วัน 3 Self-study หน้า 84–117 แล้วสุ่มข้อสอบและทวนจุดผิด'),
   dict(title='ถ้าเหลือ 1 วัน',text='เริ่ม 2’s/IEEE หน้า 18–31 → RISC-V register/format/memory หน้า 45–59 → branch/procedure หน้า 65–79 → Self-study เฉพาะหัวข้อที่ยังตอบไม่ได้และข้อผิดในแบบทดสอบ'),
   dict(title='ถ้าเหลือ 3 ชั่วโมง',text='0–35 นาที signed/IEEE หน้า 9–31; 35–90 นาที register/memory/format หน้า 45–59; 90–135 นาที branch/procedure หน้า 65–79; 135–160 นาที Self-study ภาพสรุป/คำศัพท์ หน้า 84–117; 160–180 นาทีสุ่มข้อสอบและทวนจุดขัดกัน')],
 strategyIntro='ให้ความสำคัญกับนิยาม สูตร encoding, register, branch และ stack ก่อน เพราะสไลด์ใช้เป็นฐานของตัวอย่างต่อเนื่อง; นี่เป็นการจัดลำดับเพื่อทบทวน ไม่ใช่การยืนยันแนวข้อสอบจริง',
 strategy=[
   dict(title='ควรท่องจำ',text='ช่วงค่า/สูตร signed และ bias, IEEE 1–8–23/1–11–52, ชื่อ register, R/I/S field, branch/jal/jalr, M/A/F/D/C (หน้า 5, 9–29, 45–46, 54–58, 65–72, 117)'),
   dict(title='ควรฝึกโจทย์',text='กลับบิต/บวกหนึ่ง/ทิ้ง carry, biased-127, 101.1101₂, byte offset A[8]/A[12], add encoding และการไล่ if/loop/stack (หน้า 16–31, 50, 56, 66–79)'),
   dict(title='ควรเข้าใจแนวคิด',text='endian, load/store, signed/unsigned comparison, caller/callee, atomics, linker/loader และผลของ algorithm/optimization (หน้า 48–51, 69–81, 92–110)'),
   dict(title='เตรียมข้อสอบแบบผสม',text='เลือกตอบจับคู่ศัพท์/field; อัตนัยอธิบายวิธีแทนค่าและ call flow; คำนวณจากตัวอย่างในสไลด์; วิเคราะห์โค้ด/ภาพและชี้จุดไม่สอดคล้อง')],
 flashcards=flashcards)

assert len(topics) == 30 and len({t['id'] for t in topics}) == 30
assert all(len(t['questions']) == 3 and len(t['summary'].split('。')) < 10 for t in topics)
assert set(f['id'] for f in figures) == set(fid for t in topics for fid in t['figures'])
(HERE / 'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('topics',len(topics),'figures',len(figures),'questions',sum(len(t['questions']) for t in topics),'flashcards',len(flashcards))
