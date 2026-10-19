# σ̃(ω)=σ_g(λω)=2∫_{1/λ}^{λ} 𝗉(v)cos(2πλωv)dv, 𝗉(v)=v^{-1/2}g*(log v)  (P47 thm:ext-lattice; even extension). Double precision
# (no hay cancelación: 𝗉=O(1)); g* desde p0_eig.json (832 modos pares de Legendre en [−T,T]). NUMÉRICO.
import json,math,numpy as np
from numpy.polynomial import legendre as Lg
D='/home/trabajo/Documentos/research/riemann/03-research/phase-199-frontier-pattern/proof-L-sharp/MORI15_EXTREMAL_001_data/'
E=json.load(open(D+'p0_eig.json')); V=np.array([float(x) for x in E['vectors'][0]])
mu=15; T=math.log(mu)/2; lam=math.sqrt(mu)
c=np.zeros(1664); 
for t,j in enumerate(range(0,1664,2)): c[j]=V[t]*math.sqrt((2*j+1)/(2*T))
def g(x): return Lg.legval(x/T,c)
def p(v): return g(np.log(v))/np.sqrt(v)
if __name__=='__main__':
    # check vs arb values at a few points
    from flint import arb,ctx
    ctx.prec=400
    coef=[arb(0)]*1664
    for t,j in enumerate(range(0,1664,2)): coef[j]=arb(arb(E['vectors'][0][t]).mid())*(arb(2*j+1)/(2*arb(15).log()/2)).sqrt()
    def g_arb(x):
        L=arb(15).log()/2; s_=x/L; P0,P1=arb(1),s_; s=coef[0]
        for n in range(1,1663):
            P0,P1=P1,((2*n+1)*s_*P1-n*P0)/(n+1)
            if n%2==1: s+=coef[n+1]*P1
        return s
    for x in [0.0,0.3,0.9,1.2,1.35,T]:
        print(x,g(x),g_arb(arb(x)).str(15))
