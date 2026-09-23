import math,sys,numpy as np,scipy.linalg as sla
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core
T=math.log(2);Kd=120;L=2*T
Mo=core.moments(T,Kd,[-0.5,0.5])
def mom(F):  # A(beta)=int F e^{beta t}
    return Mo@F
def phi_ints(F):
    nodes,w=np.polynomial.legendre.leggauss(400)
    u=0.5*L*(nodes+1); ww=0.5*L*w
    ph=np.array([F@core.shift_matrix(T,Kd,uu)@F for uu in u])
    ph/= (F@(np.eye(Kd)*T)@F)
    I0=2*np.sum(ww*ph*np.cosh(u/2))   # int over |u|<2T of Phi cosh
    I1=2*np.sum(ww*ph*u*np.sinh(u/2))
    return I0,I1
rng=np.random.default_rng(1)
Zp=sla.null_space(Mo); Zm=sla.null_space(Mo[0:1])
for nm,Z in [('P_T',Zp),('kerM- only',Zm)]:
    F=Z@rng.standard_normal(Z.shape[1])
    print(nm,"moments",mom(F),"  int Phi cosh =%.3e  int Phi u sinh =%.3e"%phi_ints(F))
