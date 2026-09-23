import math,sys,numpy as np,scipy.linalg as sla
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core
def run(T,Kd=160):
    contacts=[n for n in (2,3,4,5) if n<math.exp(2*T)-1e-13]
    v={n:2*core.wgt(n) for n in contacts}
    G0=np.eye(Kd)*T
    Gam=core.gamma_matrix(T,Kd)
    Sh={n:core.shift_matrix(T,Kd,math.log(n)) for n in contacts}
    Mfull=Gam-sum(v[n]*Sh[n] for n in contacts)
    Mo=core.moments(T,Kd,[-0.5,0.5])
    out={}
    for name,rows in [('P_T(both)',Mo),('kerM- only',Mo[0:1]),('kerM+ only',Mo[1:2]),('unconstrained',None)]:
        Z=np.eye(Kd) if rows is None else sla.null_space(rows)
        A=Z.T@Mfull@Z; B=Z.T@G0@Z
        w=sla.eigh(A,B,eigvals_only=True)
        out[name]=w[0]
    print(f"T={T:.6f}",{k:f"{x: .6e}" for k,x in out.items()})
run(0.5*math.log(3)); run(math.log(2))
