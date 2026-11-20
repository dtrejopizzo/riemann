"""Interval certificate for the corrected centered symbol at radius five."""
from flint import arb,acb,ctx
from math import isqrt
ctx.prec=160
w=4299682032598
terms=[]
for p in range(2,22027):
    if any(p%k==0 for k in range(2,isqrt(p)+1)): continue
    q=p
    while q<=22026:
        l=arb(q).log()
        terms.append((l,2*arb(p).log()/arb(q).sqrt()))
        q*=p
assert arb(10).exp().floor().unique_fmpz() == 22026
assert acb(arb(1)/4,arb(w-1)/2).digamma().real-arb.pi().log() > 27
assert 2*(arb(5).exp()+1)/(w-1) < arb(1)/1000
# Taylor coefficients of prime cosine sum, about the central frequency
cs=[arb(0) for _ in range(33)]
for l,a in terms:
    z=acb(0,l*w).exp()*a
    for k in range(len(cs)):
        cs[k]+=z.real
        z*=acb(0,l)/(k+1)
err=sum(a for l,a in terms)*arb(3)**33/arb.fac_ui(33)
for j in range(-3000,3000):
    x=arb(2*j+1,1)/20000
    p=cs[-1]
    for c in reversed(cs[:-1]): p=c+x*p
    # Uniform arch lower bound via monotonicity of Re digamma.
    d=x-arb(7)/200
    packet=14*d.sinc()**2*(12*d).cos()
    assert 27-p-err+packet-arb(1)/1000>1,(j,27-p-err+packet)
print('PASS 6000 cells; centered corrected symbol >1, Taylor remainder',err)
