# Locate the Type I point: zero in s2 of h(s2) = <u2,phi^>(T_*(s2,s3)) at fixed s3. UNCERTIFIED float.
import sys, numpy as np
from scipy.optimize import brentq
from t2001_typeI_search import data
K=int(sys.argv[1]); s3=float(sys.argv[2]); lo,hi=float(sys.argv[3]),float(sys.argv[4])
Tg=np.round(np.arange(0.30,1.2001,0.004),4)
def Tstar(s2):
    for j in range(len(Tg)-1):
        if data(Tg[j],K,s2,s3)['lam']>0 and data(Tg[j+1],K,s2,s3)['lam']<=0:
            return brentq(lambda T: data(T,K,s2,s3)['lam'],Tg[j],Tg[j+1],xtol=1e-13)
h=lambda s2: data(Tstar(s2),K,s2,s3)['ov']
sc=brentq(h,lo,hi,xtol=1e-12); Tc=Tstar(sc); d=data(Tc,K,sc,s3)
e=1e-4; dm=data(Tc-e,K,sc,s3); dp=data(Tc+e,K,sc,s3)
print(f"| {K} | {s3} | {sc:.8f} | {Tc:.8f} | {d['lam']:+.1e} | {d['mu2']:+.2e} | {d['ov']:+.1e} | {d['g0']:+.4f} | {d['mu1']:+.4f} | {d['mu3']:+.4f} | "
      f"{dm['Nm']}/{dp['Nm']} | {dm['lam']:+.2e}/{dp['lam']:+.2e} | {(dp['mu2']-dm['mu2'])/(2*e):+.3f} | {(dp['ov']-dm['ov'])/(2*e):+.4f} | {dm['f0']:+.4f}/{dp['f0']:+.4f} |",flush=True)
