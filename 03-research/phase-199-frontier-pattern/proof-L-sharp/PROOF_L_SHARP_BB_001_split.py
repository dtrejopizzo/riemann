# BB_001 step 1 (NUMÉRICO, arb 400 bits, existing data only): split Mori's even form G = sym(A+J) at μ=15 into
# comb C = γI − sym(A) (γ = 74/16; C is the compressed prime comb Σ_n 2Λ(n)n^{-1/2}(S_{log n}+S_{-log n})/2) and
# archimedean+pole part Ar = sym(J) + γI (so G = Ar − C). Apply to p = g*_50 (V_50 projection) and δ = g* − p (ROUGH_COMPLEMENT).
# Outputs Q-projections (Q = L²-projector onto V_50^⊥) of G p, C p, Ar p, and the vectors, to 60 digits, for step 2.
import json,os,pickle,time
from pathlib import Path
from flint import arb,arb_mat,ctx
SP=Path(os.environ['SP']); OUT=SP/'bb'; ctx.prec=400; t0=time.time()
N=1664; I=list(range(0,N,2)); d=len(I); gam=arb(74)/16
G=arb_mat([[arb(x) for x in row] for row in pickle.load(open(SP/'tb'/'G_even.pkl','rb'))]); print('G',time.time()-t0,flush=True)
A=json.load(open(SP/'mori15'/'p0_A_mid.json'))
As=arb_mat(d,d)
for i in range(d):
    for j in range(i,d):
        s=(arb(A[i][j])+arb(A[j][i]))/2; As[i,j]=s; As[j,i]=s
del A; print('A',time.time()-t0,flush=True)
C=-As
for i in range(d): C[i,i]+=gam
P=pickle.load(open(SP/'rc'/'pvecs.pkl','rb'))['pvecs']
p=arb_mat([[arb(x)] for x in P['p']]); dl=arb_mat([[arb(x)] for x in P['delta']])
R=pickle.load(open(SP/'tb'/'rungs_QF1.5.pkl','rb')); ks=R['ks']; J=50
Bk=arb_mat([[arb(x) for x in row] for row in R['coef']]); psi0={k:arb(R['info'][k]['psi0']) for k in ks}
Bas=arb_mat(d,J)
for j in range(1,J+1):
    r=psi0[ks[j]]/psi0[0]
    for i in range(d): Bas[i,j-1]=Bk[i,j]-r*Bk[i,0]
M=Bas.transpose()*Bas
def Q(v): return v-Bas*M.solve(Bas.transpose()*v)
Gp=G*p; Cp=C*p; Arp=Gp+Cp; Gd=G*dl; Cd=C*dl
out={}
for nm,v in (('Gp',Gp),('Cp',Cp),('Arp',Arp),('Gd',Gd),('Cd',Cd)):
    qv=Q(v); out[nm]=[v[i,0].mid().str(60,radius=False) for i in range(d)]; out['Q'+nm]=[qv[i,0].mid().str(60,radius=False) for i in range(d)]
    print(nm,'|v|',(v.transpose()*v)[0,0].sqrt().str(8),'|Qv|',(qv.transpose()*qv)[0,0].sqrt().str(8),flush=True)
out['pCp']=(p.transpose()*Cp)[0,0].str(30); out['dCd']=(dl.transpose()*Cd)[0,0].str(30); out['pCd']=(p.transpose()*Cd)[0,0].str(30)
out['pGp']=(p.transpose()*Gp)[0,0].str(30); out['dGd']=(dl.transpose()*Gd)[0,0].str(30)
json.dump(out,open(OUT/'split.json','w'))
import numpy as np
np.save(OUT/'G.npy',np.array([[float(G[i,j].mid().str(20,radius=False)) for j in range(d)] for i in range(d)]))
np.save(OUT/'C.npy',np.array([[float(C[i,j].mid().str(20,radius=False)) for j in range(d)] for i in range(d)]))
np.save(OUT/'Bas.npy',np.array([[float(Bas[i,j].mid().str(20,radius=False)) for j in range(J)] for i in range(d)]))
print('done',time.time()-t0)
