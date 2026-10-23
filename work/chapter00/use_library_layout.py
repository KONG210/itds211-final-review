from pathlib import Path
import re

path = Path(__file__).with_name('site-template.html')
h = path.read_text(encoding='utf-8')

def change(old, new):
    global h
    assert old in h, old[:100]
    h = h.replace(old, new)

change('const D=JSON.parse(document.getElementById(\'study-data\').textContent);', "const LIB=JSON.parse(document.getElementById('study-data').textContent);let activeChapter='chapter00';let D=LIB.chapters.find(c=>c.data).data;")
change('const F=Object.fromEntries(D.figures.map(f=>[f.id,f]));', 'let F=Object.fromEntries(D.figures.map(f=>[f.id,f]));')
change('const ALLQ=D.topics.flatMap', 'let ALLQ=D.topics.flatMap')

# Compact header and a chapter selector. Sections within a chapter remain one scrollable document.
head_start = h.index('<header class="topbar">')
head_end = h.index('</header>', head_start) + len('</header>')
h = h[:head_start] + '''<div class="site-header"><header class="topbar"><div class="crumb"><strong>ติวสอบ · Computer Architecture & OS</strong><span id="library-status">ITDS-211 · พร้อมอ่าน 1 จาก 8 บท</span></div><div class="topbar-actions"><span class="progress-chip"><span class="progress-label">อ่านแล้ว </span><strong id="header-progress">0/8</strong></span><button class="theme" id="theme-button" aria-pressed="false">◐ <span>โหมดมืด</span></button></div></header><nav class="chapter-tabs" id="chapter-tabs" aria-label="เลือกบท"></nav></div>''' + h[head_end:]
change('<main id="main" class="main" tabindex="-1">', '<main id="main" class="main" tabindex="-1"><section class="panel pending-chapter" id="pending-chapter" hidden aria-labelledby="pending-title"><div class="chapter-number" id="pending-number">01</div><h1 id="pending-title">รอเอกสารของบทนี้</h1><p class="muted">ยังไม่มีเอกสารสำหรับบทนี้ จึงยังไม่มีสรุปหรือคำถามฝึกตอบ</p><button class="btn primary" data-chapter="chapter00">กลับไป Chapter00</button></section><div id="chapter-content">')
hero_start = h.index('    <div class="hero">')
hero_end = h.index('    <div class="stats">', hero_start)
h = h[:hero_start] + '''    <div class="hero"><div class="chapter-heading"><span class="chapter-number" id="chapter-number">00</span><div><div class="eyebrow muted">Computer Architecture & Operating Systems</div><h1 id="overview-title">ภาพรวมรายวิชา</h1><p id="chapter-description">ขอบเขตวิชา จุดเน้นการเรียน และผลลัพธ์ที่ควรทำได้เมื่อจบรายวิชา</p></div></div><div class="hero-actions"><button class="btn primary" data-view="notes">อ่านสรุป ↓</button><button class="btn secondary" id="hero-quick">ทบทวนด่วน · เฉพาะสีแดง</button></div></div>
''' + h[hero_end:]
change('<strong>1 <small style="font-size:1rem">/ 8</small></strong><span>บท / หัวข้อทบทวน</span>', '<strong id="stat-topics">8</strong><span>หัวข้อในบทนี้</span>')
change('<strong>24</strong><span>คำถามแบบผสม</span>', '<strong id="stat-questions">24</strong><span>คำถามแบบผสม</span>')
change('<strong>16</strong><span>Flashcards จากสไลด์</span>', '<strong id="stat-flashcards">16</strong><span>Flashcards จากสไลด์</span>')
notice_start = h.index('    <div class="notice"><p><strong>อ่านขอบเขตนี้ก่อน:')
notice_end = h.index('</div>', notice_start) + len('</div>')
h = h[:notice_start] + '<div class="notice"><p id="chapter-notice"></p></div>' + h[notice_end:]
change('<p class="tiny muted">วัตถุประสงค์รายบทที่ระบุโดยตรง: <strong>ต้องตรวจสอบจากต้นฉบับ</strong> เป้าหมายหน้า 6–8 เป็นระดับรายวิชา</p>', '<p class="tiny muted" id="objective-limit"></p>')
change('<p class="small-text muted">เริ่มจากจุดเน้นรายวิชาและ CLOs ก่อนข้อมูลประกอบ ไม่พบหลักฐานความถี่ข้อสอบ Final ในไฟล์นี้</p>', '<p class="small-text muted">ระดับสีเป็นการประเมินเพื่อจัดเวลาอ่านจากเอกสาร ไม่ใช่การยืนยันว่าจะออกสอบ</p>')
change('<div class="priority-bar" aria-label="ต้องจำ 62.5 เปอร์เซ็นต์ สำคัญ 25 เปอร์เซ็นต์ อ่านเสริม 12.5 เปอร์เซ็นต์">', '<div class="priority-bar" id="priority-bar">')
change('<div class="legend"><span>🔴 5 หัวข้อ · 62.5%</span><span>🟡 2 · 25%</span><span>⚪ 1 · 12.5%</span></div><div id="overview-topic-list" class="topic-list" style="margin-top:23px"></div>', '<div class="legend" id="priority-legend"></div><details class="overview-topics"><summary>ดูหัวข้อและระดับความสำคัญทั้งหมด</summary><div id="overview-topic-list" class="topic-list" style="margin-top:18px"></div></details>')
# CLO information is retained in the notes; avoid a duplicate map that would belong only to Chapter00.
map_start = h.index('    <section class="panel" style="margin-top:22px"><div class="section-head"')
map_end = h.index('</section>', map_start) + len('</section>')
h = h[:map_start] + h[map_end:]
change('<h2 id="notes-title">สรุปเนื้อหา Chapter00</h2><p class="muted">8 หัวข้อ พร้อมหลักฐานจากเอกสารและคำถามหัวข้อละ 3 ข้อ</p>', '<h2 id="notes-title">สรุปเนื้อหา Chapter00</h2><p class="muted" id="notes-description"></p>')
change('<p class="muted">24 ข้อจากทุกหัวข้อ · เลือกตอบ อัตนัย วิเคราะห์ · ลองตอบก่อนดูเฉลย</p>', '<p class="muted" id="quiz-description"></p>')
change('คำถามเป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง ไม่มีโจทย์คำนวณเชิงวิชาที่สไลด์ไม่รองรับ ข้ออัตนัยและวิเคราะห์ให้เทียบแนวคำตอบและประเมินตนเอง', 'คำถามเป็นแบบฝึกจากเอกสาร ไม่ใช่ข้อสอบจริง ข้ออัตนัยและวิเคราะห์ให้เทียบแนวคำตอบและประเมินตนเอง')
change('<p class="muted">ทวนศัพท์และเป้าหมายที่สไลด์ระบุ · 16 ใบ</p>', '<p class="muted" id="flash-description"></p>')
change('<div class="notice"><p>สไลด์ยังไม่ให้นิยามหรือสูตรเชิงเทคนิค บัตรจึงทวนชื่อหัวข้อ การจับคู่ CLOs และเป้าหมาย ไม่เติมนิยามจากภายนอก</p></div>', '<div class="notice"><p id="flash-note"></p></div>')
change('<p class="muted">5 ภาพจากต้นฉบับ · แตะภาพเพื่อขยาย</p>', '<p class="muted" id="gallery-description"></p>')
change('<p class="tiny muted" style="margin-top:22px">ภาพเป็นสไลด์ต้นฉบับที่เรนเดอร์จาก PDF รวมตาราง CLOs และตารางหัวข้อเรียน ไม่มีภาพแผนภาพเชิงกลไกใน Chapter00</p>', '<p class="tiny muted" style="margin-top:22px">ภาพจากเอกสารต้นฉบับ พร้อมคำอธิบายและเลขหน้าต้นทาง</p>')
change('  <footer class="footer">ITDS-211 · Chapter00 · สรุปจากเอกสารที่ให้เท่านั้น', '  </div><footer class="footer"><span id="footer-label">ITDS-211 · สรุปจากเอกสารที่ให้เท่านั้น</span>')

# Re-render the current chapter from its data when another available chapter is added later.
intro_start = h.index("$('purpose-text').textContent=D.purpose;")
intro_end = h.index('function searchText(t)', intro_start)
intro = h[intro_start:intro_end]
intro = intro.replace("$('clo-source').innerHTML=src('หน้า 7–8');", '')
intro = intro.replace("+'<br>ตำแหน่งหน้าใช้ลำดับใน PDF; หน้า 2–9 มีเลขสไลด์ตรงกัน'", "+'<br>ตำแหน่งหน้าใช้ลำดับใน PDF'")
intro = intro.replace("$('topic-jump').innerHTML+=", "$('topic-jump').innerHTML='<option value=\"\">ไปยังหัวข้อ…</option>'+ ")
intro = intro.replace("'<optgroup label=\"Chapter00\">'", "'<optgroup label=\"'+esc(activeChapter)+'\">'")
h = h[:intro_start] + 'function renderChapterIntro(){\n' + intro + '}\n' + h[intro_end:]
plan_start = h.index("$('roadmap-list').innerHTML=D.roadmap.map")
plan_end = h.index('function shuffle(arr)', plan_start)
plan = h[plan_start:plan_end]
h = h[:plan_start] + 'function renderChapterPlan(){\n' + plan + '}\n' + h[plan_end:]
change('<details class="note-deep"><summary>ประเด็นต้องจำ', '<details class="note-deep" open><summary>ประเด็นต้องจำ')
change("state.done[t.id]", "doneMap()[t.id]")
change("state.done[el.dataset.done]", "doneMap()[el.dataset.done]")
change("function goSection(view,scroll=true){if(!TITLES[view])view='overview';history.replaceState(null,'','#'+view);", "function goSection(view,scroll=true){if(!TITLES[view])view='overview';history.replaceState(null,'','#'+activeChapter+'/'+view);")
change("document.addEventListener('click',e=>{const v=", "document.addEventListener('click',e=>{const ch=e.target.closest('[data-chapter]');if(ch)selectChapter(ch.dataset.chapter);const v=")
old_tail = "window.addEventListener('hashchange',()=>{const v=location.hash.slice(1);if(TITLES[v])goSection(v);});\nsetTheme();updateProgress();renderNotes();startQuiz();renderFlash();renderGallery();save();goSection(TITLES[location.hash.slice(1)]?location.hash.slice(1):'overview',false);"
new_tail = r'''
function doneMap(){if(!state.chapters)state.chapters={chapter00:state.done||{}};if(!state.chapters[activeChapter])state.chapters[activeChapter]={};return state.chapters[activeChapter];}
function renderChapterTabs(){
  $('chapter-tabs').innerHTML=LIB.chapters.map(c=>'<button class="chapter-tab '+(c.id===activeChapter?'active':'')+'" data-chapter="'+c.id+'" aria-current="'+(c.id===activeChapter?'page':'false')+'"><span>Chapter'+String(c.number).padStart(2,'0')+'</span><small>'+(c.data?'พร้อมอ่าน':'รอเอกสาร')+'</small></button>').join('');
  $('library-status').textContent='ITDS-211 · พร้อมอ่าน '+LIB.chapters.filter(c=>c.data).length+' จาก '+LIB.chapters.length+' บท';
}
function selectChapter(id,scroll=true,section='overview'){
  const c=LIB.chapters.find(c=>c.id===id)||LIB.chapters[0];activeChapter=c.id;renderChapterTabs();
  $('pending-chapter').hidden=!!c.data;$('chapter-content').hidden=!c.data;
  if(!c.data){$('pending-number').textContent=String(c.number).padStart(2,'0');$('pending-title').textContent='Chapter'+String(c.number).padStart(2,'0')+' · รอเอกสาร';$('header-progress').textContent='—';history.replaceState(null,'','#'+activeChapter);if(scroll)window.scrollTo({top:0,behavior:'smooth'});return;}
  D=c.data;F=Object.fromEntries(D.figures.map(f=>[f.id,f]));ALLQ=D.topics.flatMap(t=>t.questions.map((q,i)=>({...q,topic:t.title,topicId:t.id,qid:t.id+'-'+i})));
  quick=false;onlyImages=false;$('search').value='';$('gallery-search').value='';updateToggles();
  $('chapter-number').textContent=String(c.number).padStart(2,'0');$('overview-title').textContent=D.chapter.split('·').slice(1).join('·').trim()||D.chapter;
  $('chapter-description').textContent=D.description||D.purpose;
  $('stat-topics').textContent=D.topics.length;$('stat-questions').textContent=ALLQ.length;$('stat-flashcards').textContent=D.flashcards.length;
  $('chapter-notice').textContent=D.limits[0];$('objective-limit').textContent=D.objectiveNote||'วัตถุประสงค์รายบทที่ระบุโดยตรง: ต้องตรวจสอบจากต้นฉบับ';
  const counts=Object.fromEntries(Object.keys(LABEL).map(k=>[k,D.topics.filter(t=>t.level===k).length]));
  $('priority-bar').innerHTML=Object.entries(counts).map(([k,n])=>'<span class="'+k+'" style="width:'+(n/D.topics.length*100)+'%"></span>').join('');
  $('priority-bar').setAttribute('aria-label',Object.entries(counts).map(([k,n])=>LABEL[k]+' '+n+' หัวข้อ').join(', '));
  $('priority-legend').innerHTML=Object.entries(counts).map(([k,n])=>'<span>'+badge(k)+' '+n+' หัวข้อ</span>').join('');
  $('notes-title').textContent='สรุปเนื้อหา · Chapter'+String(c.number).padStart(2,'0');$('notes-description').textContent=D.topics.length+' หัวข้อ พร้อมตำแหน่งอ้างอิงและคำถามฝึกตอบ';
  $('quiz-description').textContent=ALLQ.length+' ข้อจากทุกหัวข้อ · ลองตอบก่อนดูเฉลย';$('flash-description').textContent='ทวนสิ่งที่เอกสารระบุ · '+D.flashcards.length+' ใบ';
  $('flash-note').textContent=D.flashcardNote||'บัตรทบทวนใช้เฉพาะคำศัพท์ นิยาม สูตร หรือเป้าหมายที่เอกสารรองรับ';
  $('gallery-description').textContent=D.figures.length+' ภาพจากต้นฉบับ · แตะภาพเพื่อขยาย';$('footer-label').textContent=D.course+' · Chapter'+String(c.number).padStart(2,'0')+' · สรุปจากเอกสารที่ให้เท่านั้น';
  renderChapterIntro();renderChapterPlan();renderNotes();updateProgress();$('quiz-type').value='all';startQuiz();cards=[...D.flashcards];fi=0;flipped=false;renderFlash();renderGallery();
  document.title='Chapter'+String(c.number).padStart(2,'0')+' · ITDS-211 Study Guide';goSection(section,scroll);
}
function readRoute(scroll=true){const route=location.hash.slice(1).split('/');const chapter=LIB.chapters.find(c=>c.id===route[0]);selectChapter(chapter?chapter.id:'chapter00',scroll,chapter?(route[1]||'overview'):(TITLES[route[0]]?route[0]:'overview'));}
window.addEventListener('hashchange',()=>readRoute());setTheme();readRoute(false);save();
'''
change(old_tail, new_tail)

# Warm cream and terracotta, light borders, open reading cards, and compact chapter tabs.
css = '''
:root{--bg:#f8f7f1;--panel:#fffdf8;--ink:#302d27;--muted:#777267;--line:#e2dfd5;--brand:#b14c2e;--brandsoft:#f8e9e2;--nav:#70402f;--red:#a63b35;--redsoft:#f8e4df;--yellow:#82601c;--yellowsoft:#fbf1d5;--gray:#69665d;--graysoft:#efede6;--shadow:none;--radius:14px}
[data-theme=dark]{--bg:#1d1c19;--panel:#25241f;--ink:#eee9dc;--muted:#b8b0a0;--line:#454037;--brand:#e7a083;--brandsoft:#3e2c24;--red:#f4a69b;--redsoft:#442b27;--yellow:#e1c17b;--yellowsoft:#3d3524;--gray:#c5bfb1;--graysoft:#37342e}
h1,h2{font-family:Georgia,"Leelawadee UI",Tahoma,serif;letter-spacing:-.025em}.site-header{position:sticky;top:0;z-index:30;background:var(--bg);border-bottom:1px solid var(--line)}.topbar{position:static;height:70px;max-width:1200px;margin:auto;border:0;background:transparent}.topbar strong{font-size:.96rem}.topbar .crumb{font-size:.76rem}.chapter-tabs{max-width:1200px;margin:auto;padding:0 38px 13px;display:flex;gap:7px;overflow-x:auto}.chapter-tab{flex:0 0 auto;border:1px solid transparent;border-radius:9px;background:transparent;color:var(--muted);padding:8px 14px;text-align:left;min-width:106px;line-height:1.35}.chapter-tab small{display:block;font-size:.64rem;margin-top:4px;opacity:.8}.chapter-tab.active{background:var(--panel);border-color:var(--line);box-shadow:0 2px 4px #40321c08;color:var(--brand);font-weight:700}.chapter-tab:hover{background:var(--panel)}.main{max-width:1200px;padding-top:35px}.hero{display:block;padding:0 0 23px}.chapter-heading{display:flex;gap:24px;align-items:start}.chapter-number{font:700 4.8rem/.98 Georgia,serif;color:var(--brand);letter-spacing:-.075em}.chapter-heading h1{font-size:2.2rem;margin:5px 0 12px}.chapter-heading p{font-size:.95rem;max-width:800px}.hero-actions{margin-top:18px}.stats{gap:12px}.stat{padding:17px 20px}.stat strong{font:600 1.7rem/1.3 Georgia,serif}.stat span{font-size:.8rem}.panel{box-shadow:none}.notice{border:1px solid #dabfb1;border-left:3px solid var(--brand);background:var(--brandsoft);border-radius:10px}.overview-topics{margin-top:22px;border-top:1px solid var(--line);padding-top:16px}.overview-topics summary,details>summary{cursor:pointer}.view+.view{margin-top:52px;padding-top:34px}.view{scroll-margin-top:150px}.filters{position:static}.note-card{scroll-margin-top:150px}.note-card h3{font-size:1.16rem}.note-deep{margin-top:14px}.note-deep summary{font-size:.9rem}.note-deep .details-body{font-size:.94rem}.note-card .summary{font-size:.96rem}.topic-num{font-family:Georgia,serif;color:var(--brand);font-weight:600}.subbox{border:1px solid var(--line);background:var(--brandsoft)}.note-card .subbox{background:var(--bg)}.theme,.btn,.toggle,.searchbox input,.jump{border-radius:9px}.btn.primary{background:var(--brand);color:var(--panel)}.pending-chapter{margin:35px 0 120px;padding:48px}.pending-chapter h1{font-size:2rem;margin-top:24px}.quiz-progress div{background:var(--brand)}#quiz-card{scroll-margin-top:150px}.table-wrap th{background:var(--graysoft)}
@media(max-width:850px){.topbar{height:68px}.chapter-tabs{padding:0 22px 12px}.chapter-tab{min-width:100px;padding:8px 12px}.main{padding-top:28px}}
@media(max-width:560px){.topbar{padding:0 16px}.topbar .crumb strong{font-size:.76rem}.topbar .crumb{font-size:.66rem}.topbar .theme span{display:none}.theme{width:40px}.chapter-tabs{padding:0 16px 11px;gap:4px}.chapter-tab{min-width:96px;font-size:.81rem;padding:8px 11px}.chapter-heading{gap:16px}.chapter-number{font-size:3.8rem}.chapter-heading h1{font-size:1.65rem;line-height:1.4}.chapter-heading p{font-size:.86rem}.chapter-heading .eyebrow{font-size:.6rem;letter-spacing:.07em}.view{scroll-margin-top:150px}.note-card{scroll-margin-top:150px}.pending-chapter{padding:28px}.pending-chapter h1{font-size:1.5rem}.main{padding-top:26px}}
'''
h = h.replace('</style>', css + '</style>')
path.write_text(h, encoding='utf-8')
print('Applied warm reading layout and chapter library UI.')
