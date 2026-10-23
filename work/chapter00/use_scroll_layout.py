from pathlib import Path
import re

path = Path(__file__).with_name('site-template.html')
html = path.read_text(encoding='utf-8')
html, removed = re.subn(r'<aside class="sidebar".*?</aside>\s*', '', html, count=1, flags=re.S)
assert removed == 1
html = re.sub(r'\.sidebar\{.*?(?=\.shell\{)', '', html, count=1)
for selector in [r'\.sidebar', r'\.brandmark', r'\.brandicon', r'\.brandname small', r'\.side-label,\.side-bottom', r'\.mainnav', r'\.navbtn', r'\.navno']:
    html = re.sub(selector + r'\{[^{}]*\}', '', html)
html = html.replace('.shell{margin-left:238px}', '.shell{margin:0}')
html = html.replace('.shell{margin-left:205px}', '.shell{margin:0}')
html = html.replace('.topbar{height:80px;', '.topbar{position:sticky;top:0;z-index:30;height:80px;')
html = html.replace('.filters{position:sticky;top:0;', '.filters{position:sticky;top:80px;')
html = html.replace('.filters{top:0}', '.filters{top:65px}')
html = html.replace('.note-card{scroll-margin-top:180px;', '.note-card{scroll-margin-top:260px;')
html = html.replace('.note-card{scroll-margin-top:230px}', '.note-card{scroll-margin-top:310px}')
extra_css = '''
.view{scroll-margin-top:104px}.view+.view{margin-top:76px;padding-top:42px;border-top:1px solid var(--line)}
.topbar-actions{display:flex;align-items:center;gap:12px}.progress-chip{border:1px solid var(--line);border-radius:30px;padding:6px 13px;font-size:.8rem;color:var(--muted);white-space:nowrap}.progress-chip strong{display:inline;color:var(--brand);font-size:.85rem}
#quiz-card{scroll-margin-top:100px}
@media(max-width:560px){.view+.view{margin-top:50px;padding-top:30px}.view{scroll-margin-top:85px}.topbar-actions{gap:8px}.progress-chip{padding:6px 10px}.progress-label{display:none}.topbar .crumb{font-size:.68rem}.topbar strong{font-size:.75rem}}
'''
html = html.replace('</style>', extra_css + '</style>')
html = html.replace('class="view" hidden aria-labelledby=', 'class="view" aria-labelledby=')
old_header = '<header class="topbar"><div class="crumb">ITDS-211 / CHAPTER 00<strong id="current-title">ภาพรวมรายวิชา</strong></div><button class="theme" id="theme-button" aria-pressed="false">◐ <span>โหมดมืด</span></button></header>'
new_header = '<header class="topbar"><div class="crumb">ITDS-211 / CHAPTER 00<strong>ทบทวนแบบเลื่อนอ่าน</strong></div><div class="topbar-actions"><span class="progress-chip"><span class="progress-label">ทบทวนแล้ว </span><strong id="header-progress">0/8</strong></span><button class="theme" id="theme-button" aria-pressed="false">◐ <span>โหมดมืด</span></button></div></header>'
assert old_header in html
html = html.replace(old_header, new_header)
html = html.replace("let currentView='overview',quick=false,onlyImages=false;", "let quick=false,onlyImages=false;")
old_function = "function showView(view,scroll=true){if(!TITLES[view])view='overview';currentView=view;document.querySelectorAll('.view').forEach(p=>p.hidden=p.id!=='view-'+view);document.querySelectorAll('.mainnav .navbtn').forEach(b=>b.setAttribute('aria-current',b.dataset.view===view?'page':'false'));$('current-title').textContent=TITLES[view];history.replaceState(null,'','#'+view);if(scroll)window.scrollTo({top:0,behavior:'instant'});if(view==='notes')renderNotes();if(view==='gallery')renderGallery();}"
new_function = "function goSection(view,scroll=true){if(!TITLES[view])view='overview';history.replaceState(null,'','#'+view);if(view==='notes')renderNotes();if(view==='gallery')renderGallery();if(scroll)$('view-'+view).scrollIntoView({behavior:'smooth',block:'start'});}"
assert old_function in html
html = html.replace(old_function, new_function).replace('showView(', 'goSection(')
old_progress = "$('side-progress-text').textContent='ทบทวนแล้ว '+n+'/'+D.topics.length+' หัวข้อ';$('side-progress-fill').style.width=(n/D.topics.length*100)+'%';"
assert old_progress in html
html = html.replace(old_progress, "$('header-progress').textContent=n+'/'+D.topics.length;")
path.write_text(html, encoding='utf-8')
print('Removed sidebar; all six sections now appear in one continuous page.')
