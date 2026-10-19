# H1⁻: 𝔪_{T0}(χ_ev)=𝔄_ev(χ_ev)/‖χ_ev‖² (ζ, arquimediana+peine, sin polar) por intervalos (python-flint arb).
# χ=cosh(t/2)1_{[−T,T]} ⇒ c(u)=sinh(T−u/2)+(T−u/2)cosh(u/2) exacto. Integral ∫_0^{2T}(c0−c)K: [0,ε] acotado por ε(1+ε/2)·sup|c'|,
# grilla geométrica (razón 1+1e-3) en [ε,0.05] y uniforme en [0.05,2T]; enclosure arb por subintervalo.
from flint import arb,ctx
import json
ctx.prec=120
def run(T,eps=arb('1e-12')):
    c=lambda u: (T-u/2).sinh()+(T-u/2)*(u/2).cosh()
    K=lambda u: 1/(2*(u/2).sinh())+1/(2*(u/2).cosh())
    C0=-arb.const_euler()-arb.pi()/2-3*arb(2).log()-arb.pi().log(); tail=((T/2).cosh()/(T/2).sinh()).log()+2*(-T).exp().atan()
    c0=c(arb(0)); S=arb(0); edges=[eps]
    while edges[-1]<arb('0.05'): edges.append(edges[-1]*arb('1.001'))
    n=40000; a=edges[-1]; h=(2*T-a)/n; edges+= [a+h*(k+1) for k in range(n)]
    for lo,hi in zip(edges[:-1],edges[1:]):
        w=hi-lo; U=(lo+hi)/2+arb(0,(w/2).upper()); S+=(c0-c(U))*K(U)*w
    S+=arb(0,(eps*(1+eps/2)*(T.cosh()+T+1)).upper())
    comb=arb(0)
    if T>arb(2).log()/2: comb=2*arb(2).log()/arb(2).sqrt()*c(arb(2).log())
    return (C0*c0+S+c0*tail-comb)/c0
out={}
for Ts,T in [('0.12',arb('0.12')),('0.5',arb('0.5')),('1/2log3',arb(3).log()/2)]:
    v=run(T); out[Ts]=dict(value=v.str(15),certified_negative=bool(v<0)); print(Ts,v.str(15),'NEG CERT' if v<0 else 'not certified',flush=True)
json.dump(out,open('WT_H1_interval.json','w'),indent=1)
