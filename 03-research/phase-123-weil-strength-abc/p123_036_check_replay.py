#!/usr/bin/env python3
"""Check regenerated printed Arb enclosures against every recombination input."""
from pathlib import Path
import hashlib
import json
import re
from flint import arb, ctx

ctx.prec=1024
base=Path(__file__).resolve().parent
logs=base/'endpoint_replay_20260905'
report=json.loads((logs/'report.json').read_text())
source=base.parents[1]/'04-papers/42-arithmetic-lefschetz-programme/certificates/row_d_log2'
assert report['all_exit_zero'] and len(report['jobs'])==8
for name,job in report['jobs'].items():
    assert job['status']=='exited' and job['returncode']==0,name
for name,digest in report['input_sha256'].items():
    assert hashlib.sha256((source/name).read_bytes()).hexdigest()==digest,name

def ball(job,label):
    text=(logs/(job+'.log')).read_text()
    match=re.search(re.escape(label)+r'\s*(\[[^\]]+\]|0)(?:\s|$)',text)
    assert match,(job,label)
    return arb(match.group(1))

for name,parity in [('even_gap','even'),('odd_gap','odd')]:
    text=(logs/(name+'.log')).read_text()
    assert f'PASS lifted {parity}:' in text
    assert ball(name,'disk=')>0

mu1=ball('vector1','Rayleigh mu=')
r1=ball('vector1','total residual^2=')
mu2=ball('vector2','Rayleigh mu=')
r2=ball('vector2','total residual^2=')
muo=ball('vector_odd','Rayleigh mu=')
ro=ball('vector_odd','total residual^2=')
alpha=ball('generic_bounds','generic alpha=')
beta2=ball('generic_bounds','generic beta^2=')
capacity=ball('capacity','directed normalized delta[0,20] lower=')
threshold=ball('capacity','directed capacity threshold upper=')
assert -mu1<arb('.000001746475') and r1<arb('4.441e-24')
assert mu2>arb('.0020336972824697') and r2<arb('8.623e-20')
assert muo>arb('.00000813856175479') and ro<arb('9.741e-22')
assert alpha>arb('1.5396358725647215')
assert beta2<arb('.000365731341571119')
assert capacity>arb('1.27084620358308') and threshold<arb('1.2111')
assert capacity>threshold
# Use the original conservative big-block inputs, but retain regenerated mu2.
a=arb('1.53');d=arb('.5');b=arb('.0362')
gbig=(d+a-((a-d)**2+4*b).sqrt())/2
g2=(mu2+gbig-((gbig-mu2)**2+4*r2).sqrt())/2
assert g2>arb('.0020336972824697')
g=arb('.0015');eta=arb('.0003');h=g-eta
ell=arb('.000001746475')+arb('4.441e-24')/eta
delta=arb('1.27084620358308')
even_margin=h*h*delta/(1-h*delta)-ell
godd=(arb('.05')+a-((a-arb('.05'))**2+4*arb('.000366')).sqrt())/2
odd_lower=(muo+godd-((godd-muo)**2+4*ro).sqrt())/2
assert even_margin>arb('8.63386022095e-8') and odd_lower>arb('8.13856175478e-6')
result={'status':'PASS','scope':'log2 endpoint input regeneration and bound matching; not global D',
        'checked_jobs':list(report['jobs']),
        'regenerated_v2_complement':str(g2),
        'directed_even_capacity_margin':str(even_margin),
        'directed_odd_lower':str(odd_lower),
        'log_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in logs.glob('*.log')}}
(logs/'enclosure_check.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS all regenerated directed enclosures dominate the original budget inputs')
print('PASS regenerated v2 complement also exceeds the published .0020336972824697 bound')
print('SCOPE: endpoint certificate replay, no proof of global D or common A/B/C realization')
