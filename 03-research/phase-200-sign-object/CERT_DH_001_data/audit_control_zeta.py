# AUDIT_200_CERTDH_001: zeta control, same template (explore_leg) with K_{1/4}, C0=psi(1/4)-log pi, comb Lambda(n). NUMERICAL.
import numpy as np, explore_leg as E
from sympy import factorint
def bL(nmax):
    b={}
    for n in range(2,nmax+1):
        f=factorint(n); b[n]=float(np.log(list(f)[0])) if len(f)==1 else 0.0
    return b
E.bcoef=bL; E.C0=E.digamma(0.25)-np.log(np.pi); E.K=lambda u:2*np.exp(-0.5*u)/(-np.expm1(-2*u))
_f=E.form
def form(T,N,comb='DH'):
    G,A=_f(T,N,comb); old=sum(2*np.exp(-2*T*(2*k+1.5))/(2*k+1.5) for k in range(200)); new=sum(2*np.exp(-2*T*(2*k+.5))/(2*k+.5) for k in range(200))
    return G,A+(new-old)*G
E.form=form
for T in (0.5*np.log(5),1.0,1.8):
    for sec in ('odd','full'):
        e0,v,es=E.bottom(T,60,sec); print('zeta',sec,60,round(T,4),'lowest:',' '.join('%.4e'%x for x in es),flush=True)
