import json,re
from fractions import Fraction
from pathlib import Path

d=json.loads(Path(__file__).with_name('content.json').read_text(encoding='utf-8'))
covered=set()
for t in d['topics']:
    for a,b in re.findall(r'(\d+)(?:[–-](\d+))?',t['pages']):
        covered.update(range(int(a),int(b or a)+1))
    for q in t['questions']:
        assert q['answer'] and q['pages']
        if 'options' in q:assert 0<=q['correct']<len(q['options'])
assert set(range(3,43))<=covered
assert len(d['topics'])==19 and sum(len(t['questions']) for t in d['topics'])==57
ratio=Fraction(15,10)
cycles_a=10*2_000_000_000
cycles_b=Fraction(12,10)*cycles_a
rate_b=cycles_b/6
time_a_per_i=Fraction(20,10)*250
time_b_per_i=Fraction(12,10)*500
cpi_ratio=time_b_per_i/time_a_per_i
assert (ratio,cycles_a,cycles_b,rate_b,time_a_per_i,time_b_per_i,cpi_ratio)==(Fraction(3,2),20_000_000_000,24_000_000_000,4_000_000_000,500,600,Fraction(6,5))
print('Source coverage: substantive pages 3–42; cover/outline/section/Q&A accounted for.')
print('Recomputed: relative performance=1.5; cycles A/B=20e9/24e9; clock B=4GHz; CPI example=500I/600I ps; A faster=1.2.')
