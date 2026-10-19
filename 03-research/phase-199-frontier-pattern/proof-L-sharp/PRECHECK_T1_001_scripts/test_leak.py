import numpy as np, mpmath as mp, sys
from prol import prolates; from ext import Ext
mu=int(sys.argv[1]); o,c=prolates(mu); c=float(c)
for k in (4,):
    v=o[k]; E=Ext(float(v['chi']),c,6*c)
    t=E.t; y=E.spl(t); 
    # ∫_1^Ω y² by trapezoid on fine grid + tail |B|^2/(2Ω)
    I=np.trapz(y*y,t)+abs(E.B)**2/(2*E.Om)
    lhs=v['lam']*v['psi1']**2*I*2
    print(k,'1-lam',mp.nstr(v['one_minus'],10),' 2λ_k ψ(1)²∫y² =',mp.nstr(lhs,10),' ratio',mp.nstr(lhs/v['one_minus'],10),'Bspread',E.Bspread,'B',E.B)
