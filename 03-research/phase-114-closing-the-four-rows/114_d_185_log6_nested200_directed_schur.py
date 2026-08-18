#!/usr/bin/env python3
"""Directed V200 hierarchy at T=log(6)/2 with exact moving Tate jets."""
import importlib.util,os
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
ctx.dps=int(os.environ.get('D185_DPS','1900'));N=200;NL=170;K=5;NF=NL-2
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('d147',HERE/'114_d_147_hurwitz_gamma_arb.py')
d147=importlib.util.module_from_spec(sp);sp.loader.exec_module(d147)
T=arb(6).log()/2;gamma=d147.exact_gamma_block(N,ctx.dps,T)

def ball(c,r):
 rr=np.nextafter(float(r),np.inf)+abs(np.spacing(float(c)))/2+np.nextafter(0.,1.)
 return arb(repr(float(c)),repr(float(rr)))
ct=np.load(os.environ.get('D185_CONTACT','/tmp/d185_contacts6_arb.npz'))
assert ct['C'].shape==(N,N) and int(ct['endpoint'])==6
m0=arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log();A=arb_mat(N,N)
for i in range(N):
 for j in range(N):
  A[i,j]=gamma[i,j]+ball(ct['C'][i,j],ct['R'][i,j])
  if i==j:A[i,j]-=m0
ac=np.array([[float(A[i,j].mid()) for j in range(N)] for i in range(N)])
ar=np.array([[float(A[i,j].rad())+abs(np.spacing(float(A[i,j].mid())))/2
              for j in range(N)] for i in range(N)])
np.savez(os.environ.get('D185_ASAVE','/tmp/t6_complete_operator_legendre.npz'),C=ac,R=ar)

def tate(n,sgn):
 k=T/2;integ=(2*arb.pi()/k).sqrt()*k.bessel_i(arb(2*n+1)/2)
 if sgn<0 and n%2:integ=-integ
 return (T*arb(2*n+1)/2).sqrt()*integ
gp=[tate(n,1) for n in range(N)];gm=[tate(n,-1) for n in range(N)]
H=arb_mat([[gp[0],gp[1]],[gm[0],gm[1]]]);R=arb_mat([[gp[j] for j in range(2,N)],[gm[j] for j in range(2,N)]])
M=-(H.inv()*R);Z=arb_mat(N,N-2)
for i in range(2):
 for j in range(N-2):Z[i,j]=M[i,j]
for j in range(N-2):Z[j+2,j]=1
def sub(X,r0,r1,c0,c1):return arb_mat([[X[i,j] for j in range(c0,c1)] for i in range(r0,r1)])
ZL=sub(Z,0,N,0,NF);YR=sub(Z,0,N,NF,N-2)
GL=ZL.transpose()*ZL;Y=YR-ZL*(GL.inv()*(ZL.transpose()*YR))

# Reuse only the T-independent tail coordinates of the selected dangerous
# frame; rows 0,1 are recomputed by the exact T6 Tate graph.
src=np.load('/tmp/d160_flat_arb_columns5_300.npz');TailD=arb_mat(NF,K)
for i in range(NF):
 for j in range(K):TailD[i,j]=ball(src['C'][i+2,j],src['R'][i+2,j])
D=ZL*TailD
sel=np.load('/tmp/d158_flat20_selection.npz')['safe'];assert sel.shape==(NL,NF-K)
Tail=arb_mat([[arb(repr(float(sel[i+2,j]))) for j in range(NF-K)] for i in range(NF)])
S0=ZL*Tail;GD=D.transpose()*D;S=S0-D*(GD.inv()*(D.transpose()*S0))

def cen(X):return np.array([[float(X[i,j].mid()) for j in range(X.ncols())] for i in range(X.nrows())])
def certify(X,name):
 c=cen(X);c=(c+c.T)/2;e=np.linalg.eigvalsh(c);print(name,'centre eig first=',e[:6],flush=True);assert e[0]>0
 L=np.linalg.cholesky(c);P0=np.linalg.inv(L.T);P=arb_mat([[arb(repr(float(P0[i,j]))) for j in range(len(c))] for i in range(len(c))]);Q=P.transpose()*X*P
 mar=[Q[i,i]-sum((abs(Q[i,j]) for j in range(len(c)) if j!=i),arb(0)) for i in range(len(c))]
 print(name,'Gersh=',min(mar,key=lambda x:float(x.lower())),flush=True);assert all(x.lower()>0 for x in mar)

AYY=Y.transpose()*A*Y;certify(AYY,'shell30')
F=arb_mat(N,NF)
for i in range(N):
 for j in range(K):F[i,j]=D[i,j]
 for j in range(NF-K):F[i,j+K]=S[i,j]
AFL=F.transpose()*A*F;AFY=F.transpose()*A*Y
Klow=AFL-AFY*(AYY.inv()*AFY.transpose())
Kss=sub(Klow,K,NF,K,NF);certify(Kss,'safe163')
Kdd=sub(Klow,0,K,0,K);Kds=sub(Klow,0,K,K,NF)
Kfinal=Kdd-Kds*(Kss.inv()*Kds.transpose())
Cs=-(Kss.inv()*Kds.transpose());Xlow=D+S*Cs
Cy=-(AYY.inv()*(Y.transpose()*A*Xlow));Xgraph=Xlow+Y*Cy
XC=cen(Xgraph);XR=np.array([[float(Xgraph[i,j].rad()) for j in range(K)] for i in range(N)])
XR=np.nextafter(XR+np.abs(np.spacing(XC))/2,np.inf)
KC=cen(Kfinal);KR=np.array([[float(Kfinal[i,j].rad()) for j in range(K)] for i in range(K)])
KR=np.nextafter(KR+np.abs(np.spacing(KC))/2,np.inf)
evals,evecs=np.linalg.eigh((KC+KC.T)/2)
print('final5 finite M200 centre eig=',evals,flush=True)
ray=[];WC=[];WR=[];primitive=[]
for col in range(2):
 v=arb_mat([[arb(repr(float(evecs[i,col]))) ] for i in range(K)])
 rq=(v.transpose()*Kfinal*v)[0,0]/(v.transpose()*v)[0,0]
 ray.append((str(rq.lower()),str(rq.upper())))
 w=Xgraph*v
 WC.append([float(w[i,0].mid()) for i in range(N)])
 WR.append([float(w[i,0].rad())+abs(np.spacing(float(w[i,0].mid())))/2 for i in range(N)])
 primitive.append((str((arb_mat([gp])*w)[0,0]),str((arb_mat([gm])*w)[0,0])))
 print('negative witness',col,'directed Rayleigh=',rq,'Tate residuals=',primitive[-1],flush=True)
np.savez(os.environ.get('D185_SAVE','/tmp/d185_log6_directed_graph.npz'),
 C=XC,R=XR,K=KC,KR=KR,eigenvalues=evals,eigenvectors=evecs,
 witness_C=np.array(WC).T,witness_R=np.array(WR).T,
 rayleigh=np.array(ray),primitive=np.array(primitive))
assert evals[0]<0 and arb(ray[0][1])<0
print('D185 T=log(6)/2: finite hierarchy has a rigorously negative witness; endpoint positivity FAILS')
