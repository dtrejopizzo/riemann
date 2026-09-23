"""FATAL check: at the certified window T = log 2, is lmin(Q_T) >= 0 for large gamma_0?
If lmin >= 0 the configuration (a,gamma_0) is NOT excluded by the log-2 window."""
import math, numpy as np, track1 as t
T=math.log(2)
print('T = log 2 = %.6f ; a = 0.45 (max leverage), cosh(2aT)=%.4f'%(T,math.cosh(2*0.45*T)),flush=True)
for g0 in (100.,200.,300.,500.,1000.,2000.):
    row=[]
    for om in (2.0,3.0):
        l,K=t.lmin_Q_om(T,0.45,g0,om_mult=om)
        row.append('om%.0f(K=%d): %+.4e'%(om,K,l))
    print(' g0=%8.1f  lminQ = '%g0+'   '.join(row)+'   [log(g0/2pi)=%.3f]'%math.log(g0/(2*math.pi)),flush=True)
