import math,sys,numpy as np
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round3')
import track1 as t
g=np.load('/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round3/zeros600.npy')
print("gamma_100 =",g[99])
for a in (0.0,0.30,0.45):
    v=t.tstar_om(a,g[99],om_mult=4.,hi=3.0)
    print("  T*(%.2f, gamma_100) = %.5f   cosh(2aT)=%.4f"%(a,v,math.cosh(2*a*v)))
print("=== gamma0^max bracket at T=log2, a=0.45 and a=0")
T=math.log(2)
for g0 in (150.,180.,200.,210.,250.):
    for a in (0.0,0.45):
        l,K=t.lmin_Q_om(T,a,g0,om_mult=3.0)
        print("   g0=%6.1f a=%.2f K=%4d lminQ=%+.5e"%(g0,a,K,l))
