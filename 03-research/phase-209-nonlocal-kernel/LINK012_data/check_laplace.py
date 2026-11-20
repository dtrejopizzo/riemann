"""Independent upper bound: exact Laplace formula, finite sums, explicit tail."""
import json
from pathlib import Path
from flint import arb, ctx
ctx.prec = 128
T = arb(4)/5
w = arb.pi()/(2*T)
r = 3*(w*w+arb(1)/4)/(9*w*w+arb(1)/4)
def laplace(a):
    z = r/(a*a+w*w)-3/(a*a+9*w*w)
    return a/(1+r*r)*(r*r/(a*a+w*w)+1/(a*a+9*w*w)) + (1+(-2*a*T).exp())*w*w/(T*(1+r*r))*z*z
J = 200
arch = (arb(1)/4).digamma()-arb.pi().log()
for j in range(J):
    a = 2*j+arb(1)/2
    arch += 2*(1/a-laplace(a))
aJ = 2*J+arb(1)/2
derivative_norm = w*w*(r*r+9)/(1+r*r)
tail = 2*derivative_norm*(aJ**(-3)+1/(4*aJ*aJ))
def correlation(u):
    def diag(v):
        return ((2*T-u)*(v*u).cos()+(v*u).sin()/v)/(2*T)
    s1, s3 = (w*u).sin(), (3*w*u).sin()
    off = ((s3-s1)/(-2*w)+(s3+s1)/(4*w))/(2*T)
    return (r*r*diag(w)+diag(3*w)-2*r*off)/(1+r*r)
comb = arb(0)
for n, lam in [(2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())]:
    comb += 2*lam/arb(n).sqrt()*correlation(arb(n).log())
upper = arch+tail-comb
assert upper < arb('0.02')
result = {k:str(v) for k,v in [('arch_partial',arch),('arch_tail_bound',tail),('comb',comb),('Q_upper',upper)]}
result['Q_less_002'] = bool(upper < arb('0.02'))
print(json.dumps(result, indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
