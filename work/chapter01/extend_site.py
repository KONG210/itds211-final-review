from pathlib import Path

path=Path(__file__).parent.parent/'chapter00'/'site-template.html'
h=path.read_text(encoding='utf-8')
def change(old,new):
    global h
    assert old in h,old[:90]
    h=h.replace(old,new)

change('<h3>แผนทบทวน 5 รอบ</h3>','<h3 id="plan-title">แผนทบทวน</h3>')
change('<p class="small-text muted">จุดเน้นหน้า 6 และ Objectives/CLOs หน้า 7–8 เป็นแกนของบท แต่ยังประเมินไม่ได้ว่าหัวข้อใดออก Final มากที่สุด</p>','<p class="small-text muted" id="strategy-description"></p>')
change('เป็นแผนทั่วไปสำหรับ Chapter00 เผื่อต้องเร่งทบทวนภายหลัง ไม่ใช่เวลาที่กำหนดให้คุณ','เป็นตัวเลือกทั่วไปสำหรับบทที่เลือก เผื่อต้องเร่งทบทวนภายหลัง ไม่ใช่เวลาที่กำหนดให้คุณ')
helper='''
function mathBlocks(t){
  const formulas=(t.formulas||[]).map(f=>'<div class="formula-box"><h4>สูตรที่ต้องรู้</h4><pre class="formula">'+esc(f.expr)+'</pre><p class="small-text">'+esc(f.description)+'</p>'+source(f.pages)+'</div>').join('');
  const worked=(t.worked||[]).map(w=>'<section class="worked-example"><h4>'+esc(w.title)+'</h4><ol>'+w.steps.map(step=>'<li>'+esc(step)+'</li>').join('')+'</ol><p><strong>คำตอบ:</strong> '+esc(w.answer)+'</p>'+source(w.pages)+'</section>').join('');
  return formulas+worked;
}
'''
change('function renderNotes(){',helper+'\nfunction renderNotes(){')
change("+(t.comparison?table(t.comparison):'')+", "+mathBlocks(t)+(t.comparison?table(t.comparison):'')+")
change("$('chapter-notice').textContent=D.limits[0];", "$('chapter-notice').textContent=D.notice||D.limits[0];")
change("renderChapterIntro();renderChapterPlan();renderNotes();updateProgress();$('quiz-type').value='all';startQuiz();", "renderChapterIntro();renderChapterPlan();renderNotes();updateProgress();$('plan-title').textContent='แผนทบทวน '+D.plan.length+' รอบ';$('strategy-description').textContent=D.strategyIntro||'เริ่มจากนิยาม หลักการ และหัวข้อแกนกลางของบท ยังไม่ทราบความถี่ออก Final จากสไลด์เพียงอย่างเดียว';const kinds=[...new Set(ALLQ.map(q=>q.type))];$('quiz-type').innerHTML='<option value=\"all\">ทุกแบบ</option>'+kinds.map(kind=>'<option value=\"'+esc(kind)+'\">'+esc(kind)+' ('+ALLQ.filter(q=>q.type===kind).length+')</option>').join('');startQuiz();")
css='''
.formula-box{border:1px solid var(--line);border-left:3px solid var(--brand);border-radius:11px;padding:19px;margin-top:19px;background:var(--brandsoft);min-width:0}
.formula{font:500 .95rem/1.85 Consolas,"Leelawadee UI",monospace;white-space:pre-wrap;overflow-wrap:anywhere;margin:12px 0;color:var(--ink)}
.worked-example{padding:21px;border:1px solid var(--line);border-radius:11px;margin-top:19px;background:var(--panel)}.worked-example li{margin-top:10px;overflow-wrap:anywhere}.worked-example p{font-size:.92rem}
@media(max-width:560px){.formula-box,.worked-example{padding:16px}.formula{font-size:.83rem}}
'''
h=h.replace('</style>',css+'</style>')
path.write_text(h,encoding='utf-8')
print('Added formula panels, worked examples and per-chapter question filters.')
