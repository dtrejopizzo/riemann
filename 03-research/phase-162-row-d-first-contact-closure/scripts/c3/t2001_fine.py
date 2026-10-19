# fine s2-scan across s2=1 at fixed s3: first zeros T_*(lam), T_m(mu2) and <u2,phi^> there. UNCERTIFIED.
import sys, numpy as np
from scipy.optimize import brentq
from t2001_typeI_search import data
K=int(sys.argv[1]); s3=float(sys.argv[2]); S2=[float(x) for x in sys.argv[3].split(",")]
Tg=np.round(np.arange(0.30,1.2001,0.004),4)
def fz(key,s2):
    for j in range(len(Tg)-1):
        a=data(Tg[j],K,s2,s3)[key]; b=data(Tg[j+1],K,s2,s3)[key]
        if a>0 and b<=0: return brentq(lambda T: data(T,K,s2,s3)[key],Tg[j],Tg[j+1],xtol=1e-12)
    return None
print("| s2 | s3 | K | T_* | mu2(T_*) | <u2,phi^>(T_*) | r2 | g(0) | T_mu2 | <u2,phi^>(T_mu2) | T_mu2-T_* |")
for s2 in S2:
    Ts=fz('lam',s2); Tm=fz('mu2',s2)
    a=data(Ts,K,s2,s3) if Ts else None; b=data(Tm,K,s2,s3) if Tm else None
    print(f"| {s2} | {s3} | {K} | {Ts:.7f} | {a['mu2']:+.3e} | {a['ov']:+.3e} | {a['r2']:.2e} | {a['g0']:+.4f} | {Tm:.7f} | {b['ov']:+.3e} | {Tm-Ts:.2e} |" if Ts and Tm else f"| {s2} | {s3} | {K} | {Ts} | - | - | - | - | {Tm} | - | - |",flush=True)
