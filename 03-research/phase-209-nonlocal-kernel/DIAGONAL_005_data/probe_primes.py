"""Exploratory, not certified: test signs of the defined R_(1/4), no Q_T claim."""
import json, math
from pathlib import Path
import mpmath as mp
mp.mp.dps=35

def tsum(a):
    if a>1:
        return 2*mp.fsum(mp.exp(-mp.pi*a*n*n) for n in range(1,int(mp.sqrt(110/(mp.pi*a)))+3))
    return (1+tsum(1/a))/mp.sqrt(a)-1

def delta(k,y):
    a=k*k*y
    if a<mp.mpf('0.5'):
        return -1+(1/mp.sqrt(a))*tsum(1/a)
    return tsum(a)-1/mp.sqrt(a)

def entry(d,e):
    l=math.lcm(d,e)
    g=mp.mpf(math.gcd(d,e)-1)/(d*e)
    def small(u):
        if not u:return -(1-mp.mpf(1)/d)*(1-mp.mpf(1)/e)
        y=u**4;c=1/mp.sqrt(y)
        a,b,h=delta(d,y),delta(e,y),delta(1,y)
        return delta(l,y)+(c*h/(d*e)-c*a/e-c*b/d-a*b)/(c+h)
    def big(u):
        y=u**4
        # beyond this the omitted contribution is minuscule: exploratory only
        if y>30:return mp.mpf(0)
        return tsum(l*l*y)-tsum(d*d*y)*tsum(e*e*y)/tsum(y)
    r=4*mp.quad(small,[0,mp.mpf('.03'),mp.mpf('.1'),mp.mpf('.3'),mp.mpf('.6'),1])
    r+=4*mp.quad(big,[1,mp.mpf('1.3'),mp.mpf('1.8'),mp.mpf('2.4')])-4*g
    return r

indices=[2,3,5,7]
rows=[[entry(d,e) for e in indices] for d in indices]
M=mp.matrix(rows)
res={'classification':'NUMERICAL exploratory, not certified','dps':mp.mp.dps,'indices':indices,
'R':[[str(x) for x in row] for row in rows], 'eigen_R':[str(x) for x in mp.eigsy(M,eigvals_only=True)]}
Path(__file__).with_name('probe_primes.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
