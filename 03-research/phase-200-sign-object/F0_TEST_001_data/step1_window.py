# F0_TEST_001 step 1: independent re-evaluation of Mori's Galerkin value Q = v(A+J)v on g* (mu=15, even), NUMERICO.
# Q_gal = arch_Omega + gamma*(||v||^2 - band_Omega) + pole - comb   (A = gamma I - C_p, J = arch_Omega - gamma*band + pole + U, U ~ 1e-800)
# arch_Omega = (1/pi) int_0^Omega a(t)|Fg|^2, band_Omega = (1/pi) int_0^Omega |Fg|^2, Omega = 736, gamma = 74/16.
# Fg(t) = sum_j c_j * 2L (-1)^{j/2} j_j(L t)  (even j),  c_j = v_j sqrt((2j+1)/2L).   arb, 420 bits.
import json,sys,os,time
from pathlib import Path
from multiprocessing import Pool
from flint import arb,acb,ctx
ctx.prec=420
DATA=Path('/home/trabajo/Documentos/research/riemann/03-research/phase-199-frontier-pattern/proof-L-sharp/MORI15_EXTREMAL_001_data')
E=json.load(open(DATA/'p0_eig.json')); V=[arb(x) for x in E['vectors'][0]]
N=1664; mu=15; L=arb(mu).log()/2
J=list(range(0,N,2))
C=[V[t]*(arb(2*j+1)/(2*L)).sqrt()*2*L*(1 if (j//2)%2==0 else -1) for t,j in enumerate(J)]
def Fg(t):
    # Miller downward recurrence for spherical Bessel j_n(z), normalised by sum (2n+1) j_n^2 = 1
    z=(L*t).mid(); top=max(N,int(float(z.mid())))+400
    a,b=arb(0),arb(10)**-300; js=[None]*(top+2); js[top+1]=a; js[top]=b
    for n in range(top,0,-1):
        js[n-1]=((2*n+1)/z*js[n]-js[n+1]).mid()
    S=sum((2*n+1)*js[n]*js[n] for n in range(top+1)); sc=1/S.sqrt()
    if js[0]*z.sin()<0: sc=-sc
    return sc*sum(c*js[j] for c,j in zip(C,J))
def gl(n):
    out=[]
    for k in range(n):
        x,w=arb.legendre_p_root(n,k,weight=True); out.append((x,w))
    return out
NQ=int(os.environ.get('NQ','100'))
G=gl(NQ)
ends=[0,0.125,0.25,0.5,1,2,4]+list(range(8,737,4))
lpi=arb.pi().log()
def panel(k):
    ctx.prec=420
    lo=arb(ends[k]);hi=arb(ends[k+1]);h=(hi-lo)/2;c=(hi+lo)/2;pa=arb(0);pb=arb(0)
    for x,w in G:
        t=c+h*x; F=Fg(t); F2=F*F
        a=acb(arb(1)/4,t/2).digamma().real-lpi
        pa+=w*a*F2; pb+=w*F2
    return (pa*h/arb.pi()).str(100,radius=False),(pb*h/arb.pi()).str(100,radius=False)
if __name__=='__main__':
    t0=time.time()
    with Pool(20) as P: res=P.map(panel,range(len(ends)-1))
    arch=sum(arb(a) for a,b in res); band=sum(arb(b) for a,b in res)
    # pole and comb by Gauss-Legendre in x (exact for the polynomial products)
    norm2=sum(v*v for v in V)
    out={'NQ':NQ,'arch_Omega':arch.str(90,radius=False),'band_Omega':band.str(90,radius=False),'norm2':norm2.str(90,radius=False),
         'gamma(norm2-band)':((arb(74)/16)*(norm2-band)).str(30,radius=False),'time':time.time()-t0}
    json.dump(out,open(f'step1_arch_NQ{NQ}.json','w'),indent=1); print(out)
