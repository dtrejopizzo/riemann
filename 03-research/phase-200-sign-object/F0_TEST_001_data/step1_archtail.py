# F0_TEST_001 step 1c: archimedean tail beyond Omega=736 of the TRUE form W_T(g*) (not in Mori's Galerkin value):
# tail = (1/pi) int_736^TMAX a|Fg|^2 by Bessel series (arb), plus model beyond TMAX fitted from t^2|Fg|^2 averages. NUMERICO.
import json,os,time,math
from multiprocessing import Pool
from flint import arb,acb,ctx
import step1_window as s
TMAX=int(os.environ.get('TMAX','12000')); W=4; NQ=36
G=s.gl(NQ); lpi=arb.pi().log()
def panel(lo):
    ctx.prec=300; s.ctx.prec=300
    lo=arb(lo);h=arb(W)/2;c=lo+h;pa=arb(0);pe=arb(0);pt=arb(0)
    for x,w in G:
        t=c+h*x; F=s.Fg(t); F2=F*F; a=acb(arb(1)/4,t/2).digamma().real-lpi
        pa+=w*a*F2; pe+=w*F2; pt+=w*F2*t*t
    return float((pa*h/arb.pi()).mid()),float((pe*h/arb.pi()).mid()),float((pt*h/arb.pi()).mid())
if __name__=='__main__':
    t0=time.time(); los=list(range(736,TMAX,W))
    with Pool(20) as P: R=P.map(panel,los,chunksize=4)
    arch=sum(r[0] for r in R); en=sum(r[1] for r in R)
    # t^2|F|^2 average over last 1000 -> K; model tail (1/pi) int_TMAX^inf a(t) K/t^2 dt with a ~ log(t/2) - log pi
    last=[r[2]/W for lo,r in zip(los,R) if lo>=TMAX-2000]; Kpi=sum(last)/len(last)   # = (1/pi) <t^2 |F|^2>
    a_T=math.log(TMAX/2)-math.log(math.pi)
    model=Kpi*(a_T+1)/TMAX
    out={'TMAX':TMAX,'arch(736,TMAX)':arch,'energy(736,TMAX)':en,'(1/pi)<t^2|F|^2> last 2000':Kpi,
         'model tail beyond TMAX':model,'per-1000 t^2|F|^2/pi':[sum(r[2] for lo,r in zip(los,R) if k<=lo<k+1000)/1000 for k in range(736,TMAX,1000)],
         'time':time.time()-t0}
    json.dump(out,open(f'step1_archtail_T{TMAX}.json','w'),indent=1); print(out)
