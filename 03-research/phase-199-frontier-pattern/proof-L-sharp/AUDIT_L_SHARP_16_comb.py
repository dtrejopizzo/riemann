import json,mpmath as mp
from sympy import mobius, divisors
mp.mp.dps=60
mu=15;N=1664;L=mp.log(mu)/2
E=json.load(open('MORI15_EXTREMAL_001_data/p0_eig.json'))
v=E['vectors'][0]
C=[mp.mpf(str(x))*mp.sqrt(mp.mpf(2*j+1)/(2*L)) for x,j in zip(v,range(0,N,2))]
def g(x):
    if abs(x)>=L: return mp.mpf(0)
    xi=x/L;P0,P1=mp.mpf(1),xi;s=C[0]
    for n in range(1,N-1):
        P0,P1=P1,((2*n+1)*xi*P1-n*P0)/(n+1)
        if (n+1)%2==0: s+=C[(n+1)//2]*P1
    return s
def c(n): return sum(int(mobius(m)) for m in divisors(n) if m<mu)
print('g(0)=',mp.nstr(g(0),6),'max|g| approx', max(abs(g(mp.mpf(t)/10)) for t in range(-13,14)))
tab={n:c(n) for n in range(15,40)};print(tab)
for x in [L+mp.mpf('0.05'),L+mp.mpf('0.5'),L+1,L+2]:
    terms=[(n,c(n)*n**-0.5*g(x-mp.log(n))) for n in range(mu,int(mp.e**(x+L))+2) if c(n)!=0]
    S=sum(t for _,t in terms); M=max(abs(t) for _,t in terms) if terms else 0
    print(mp.nstr(x,4),'comb sum',mp.nstr(S,6),'max term',mp.nstr(M,6),'#',len(terms))
