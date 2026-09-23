import math,sys,numpy as np,scipy.linalg as sla
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core
T=math.log(2);Kd=200
Z=sla.null_space(core.moments(T,Kd,[-0.5,0.5]))
G=Z.T@(np.eye(Kd)*T)@Z
v2,v3=2*core.wgt(2),2*core.wgt(3)
print("v2,v3,sum",v2,v3,v2+v3)
B=Z.T@(v2*core.shift_matrix(T,Kd,math.log(2))+v3*core.shift_matrix(T,Kd,math.log(3)))@Z
w=sla.eigh(B,G,eigvals_only=True)
print("joint max on P_T:",w[-1])
# unconstrained
Bu=v2*core.shift_matrix(T,Kd,math.log(2))+v3*core.shift_matrix(T,Kd,math.log(3))
print("joint max unconstrained L2(-T,T):",sla.eigh(Bu,np.eye(Kd)*T,eigvals_only=True)[-1])
M0=Z.T@core.gamma_matrix(T,Kd)@Z
x0min=sla.eigh(M0,G,eigvals_only=True)[0]
print("min x0 =",x0min," minE =",x0min-(-5.372183419225666))
print("sum check: joint+(-x0min) =",0.9009276162618641-x0min)
