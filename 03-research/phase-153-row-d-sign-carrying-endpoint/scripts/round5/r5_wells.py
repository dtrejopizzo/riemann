import numpy as np
from scipy.special import digamma
from scipy.optimize import brentq
from scipy.integrate import quad
exec(open('/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round5/r5_minorant.py').read().split('def report')[0])
def wells(T,a=0.0,label=''):
    W,sig,rho,S=make(T,a)
    g=np.linspace(1e-9,300,3000001); v=sig(g)
    idx=np.where(np.sign(v[:-1])*np.sign(v[1:])<0)[0]
    rts=[brentq(sig,g[i],g[i+1],xtol=1e-13) for i in idx]
    print(f"\n### T={label} a={a}: terms {[(n,round(w,6))for n,w in W]} 2S={2*S:.6f} sigma(0)={sig(0.0):.6f}")
    print(f" pi/(2T)={np.pi/(2*T):.6f}   tau_0(first root)={rts[0]:.6f}   tau_0*T={rts[0]*T:.6f} (vs pi/2={np.pi/2:.6f})")
    # tau_1 : unique root of arch(tau)=2S
    arch=lambda t: np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
    t1=brentq(lambda t: arch(t)-2*S,0.1,1e6)
    print(f" tau_1 (arch=2S, proven monotone) = {t1:.6f}   last sign change = {rts[-1]:.6f}")
    edges=[0.0]+rts+[t1]
    print(" wells/bands (sign, interval, extremum of sigma, |int sigma|):")
    for i in range(len(edges)-1):
        l,r=edges[i],edges[i+1]
        if r-l<1e-6: continue
        xs=np.linspace(l,r,4001); ys=sig(xs)
        s='NEG' if ys.mean()<0 else 'pos'
        ex=ys.min() if s=='NEG' else ys.max()
        I=np.trapz(ys,xs)
        print(f"   {s} [{l:8.4f},{r:8.4f}] ext={ex:9.5f} int={I:10.5f}")
    return rts,t1,S
for T,lab in [(0.5*np.log(2),'0.5log2'),(0.5*np.log(3),'0.5log3'),(np.log(2),'log2')]:
    wells(T,0.0,lab)
wells(np.log(2),0.45,'log2')
wells(np.log(2),0.30,'log2')
# tau_0 * T across T
print("\n--- tau_0(T)*T vs pi/2 (pi/2=1.570796); tau_0 depends on T only through which prime powers are present")
for T in [0.4,0.5,0.5493061,0.6,0.65,0.6898,0.6931472,0.72,0.8047190,0.9,0.9729551]:
    W,sig,rho,S=make(T)
    g=np.linspace(1e-9,20,200001); v=sig(g)
    i=np.where(np.sign(v[:-1])*np.sign(v[1:])<0)[0][0]
    r=brentq(sig,g[i],g[i+1])
    print(f" T={T:.7f} nterms={len(W)} tau_0={r:.6f} tau_0*T={r*T:.6f} {'OK' if r*T<=np.pi/2 else 'EXCEEDS'}")
