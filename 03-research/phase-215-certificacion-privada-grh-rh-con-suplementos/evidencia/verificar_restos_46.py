"""Rigorous coarse bounds for the independent quadrature/inertia reconstruction."""
import json
from pathlib import Path
from flint import arb,ctx
ctx.prec=640
T=arb(5).log()/2;rho=arb('3.2');y=(rho-1/rho)/8
assert y<arb('.361')
wmin=arb(1)/4-y/2
assert 1/wmin<15
assert sum((1/(wmin+k) for k in range(1,8)),arb(0))<3
# |w+8|<130 on all the ellipses; Re(w+8)>=8.
assert ((arb('240.5')/2)**2+(arb('8.5'))**2).sqrt()<130
assert arb(130).log()+arb.pi()/2+arb(1)/16+arb(1)/768<7
assert arb.pi().log()<2
assert (y*arb(4).log()).cosh()<2
assert (2*T*y).exp()<2
# |g|<34 and normalized Bessel product contributes <2, hence M=70.
remainder=8*120*70*(2*T/arb.pi())*rho**(-92)/(1-rho**(-2))
assert remainder<arb('2e-42')
def tail(k):
    c=240*T
    df=arb(1)
    for j in range(1,2*k+2,2): df*=j
    term=c**(2*k+1)/df**2
    ratio=c**2/(2*k+3)**2
    assert ratio<1
    return 2/arb.pi()*term/(1-ratio)
l1=tail(280);l2=tail(330)
assert l1<arb('4.5e-20') and l2<arb('3.9e-70')
result=dict(quadrature_remainder=remainder.str(40),Lambda280=l1.str(40),Lambda330=l2.str(40),status='rigorous ball predicates passed; proof in NUMERICA-46.md')
print(json.dumps(result,indent=2))
Path(__file__).with_name('restos_46_arb.json').write_text(json.dumps(result,indent=2))
