# Extract midpoints (200 sig digits) of Mori's arb matrices A,J,pole,band,U per parity into compact JSON.
import gzip,json,sys,re,os
from pathlib import Path
R=Path(os.environ['SP'])/'zen/pwb/certificate-VIII/notes/0792_claude_lowmem_generator/runs'
OUT=Path(os.environ['SP'])/'mori15'
from flint import arb,ctx
ctx.prec=3400
def mid(s):
    a=arb(s)  # parse arb string
    return a.mid().str(200,radius=False)
for p in (0,1):
    for name in ('A','J','pole','band','U'):
        f=R/f'm15n1664p3328q224_p{p}_{name}.json.gz'
        if not f.exists(): print('missing',f); continue
        out=OUT/f'p{p}_{name}_mid.json'
        if out.exists(): continue
        M=json.load(gzip.open(f,'rt'))
        rows=[[mid(x) for x in row] for row in M]
        json.dump(rows,open(out,'w'))
        print('done',p,name,len(rows),flush=True)
