import math, numpy as np, track1 as t
g=np.load('zeros600.npy')
print('--- Table 1: g0=gamma_1=%.6f, vary a (om_mult 4 and 6) ---'%g[0],flush=True)
for a in (0.0,0.05,0.10,0.20,0.30,0.45,0.49):
    v4=t.tstar_om(a,g[0],om_mult=4.); v6=t.tstar_om(a,g[0],om_mult=6.)
    print(' a=%.2f  T*=%.5f (om4)  %.5f (om6)'%(a,v4,v6),flush=True)
print('--- Table 2: a=0.30, vary gamma_0 ---',flush=True)
for k in (1,2,5,10,25,50,100,200,400):
    g0=g[k-1]
    v=t.tstar_om(0.30,g0,om_mult=4.,hi=6.0)
    v0=t.tstar_om(0.0,g0,om_mult=4.,hi=6.0)
    print(' gamma_%d=%10.4f  T*(0.30)=%s  T*(0)=%s   0.5*log(g0/2pi)=%.4f  log(g0)=%.4f'%(
        k,g0,('%.5f'%v if v else 'none'),('%.5f'%v0 if v0 else 'none'),0.5*math.log(g0/(2*math.pi)),math.log(g0)),flush=True)
