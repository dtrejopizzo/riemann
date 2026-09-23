import math,sys,numpy as np
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round3')
import track1 as t
T=math.log(2)
print("fine scan gamma0 in [188,212], a=0.45, om3",flush=True)
for g0 in np.arange(188.,212.01,1.0):
    l,K=t.lmin_Q_om(T,0.45,float(g0),om_mult=3.)
    print("  g0=%6.1f K=%4d lminQ=%+.5e %s"%(g0,K,l,"NEG" if l<0 else ""),flush=True)
print("large-gamma spot checks (a=0.45, om3):",flush=True)
for g0 in (400.,410.,420.,430.,700.,710.,720.,1500.,1510.):
    l,K=t.lmin_Q_om(T,0.45,g0,om_mult=3.)
    print("  g0=%7.1f K=%4d lminQ=%+.5e %s"%(g0,K,l,"NEG" if l<0 else ""),flush=True)
