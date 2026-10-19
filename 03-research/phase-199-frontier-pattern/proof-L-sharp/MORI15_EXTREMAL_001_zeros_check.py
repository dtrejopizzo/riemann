# Check (zero data used ONLY as a consistency check, not as a mechanism input): Fg*(γ) at the first zeros.
import json,os,sys
from flint import arb,acb,ctx
import mpmath as mp
D=os.environ['SP']+'/mori15'; p=int(sys.argv[1]); ctx.prec=420
E=json.load(open(f'{D}/p{p}_eig.json')); v=[arb(x) for x in E['vectors'][0]]
N=1664;L=arb(15).log()/2
norm=[(arb(2*j+1)/(2*L)).sqrt() for j in range(N)]
coef=[arb(0)]*N
for t,j in enumerate(range(p,N,2)): coef[j]=v[t]*norm[j]
def g_at(x):
    xi=(x/L).mid(); P0,P1=arb(1),xi; s=coef[0]*P0+coef[1]*P1
    for n in range(1,N-1):
        P0,P1=P1,(((2*n+1)*xi*P1-n*P0)/(n+1)).mid(); s+=coef[n+1]*P1
    return s
NQ=1700; xs=[];ws=[]
for k in range(NQ):
    x,w=arb.legendre_p_root(NQ,k,weight=True); xs.append(x); ws.append(w)
gx=[g_at(L*x) for x in xs]
def F(t):
    t=arb(t)
    if p==0: return sum(w*gg*(L*x*t).cos() for x,w,gg in zip(xs,ws,gx))*L
    return sum(w*gg*(L*x*t).sin() for x,w,gg in zip(xs,ws,gx))*L
mp.mp.dps=70
out=[]
for n in range(1,31):
    z=mp.zetazero(n).imag
    f=F(str(z)); out.append((n,float(z),f.str(8)))
    print(n,float(z),f.str(8),flush=True)
# also at non-zeros for comparison
for t in [1,3,5,8,10,12,16,18,20,30,50,100]:
    print('t=',t,F(t).str(8))
json.dump(out,open(f'{D}/p{p}_zeros_check.json','w'))
