import numpy as np, mpmath as mp, sys
mu=float(sys.argv[1]); TM=float(sys.argv[2]); dt=float(sys.argv[3]); N=int(sys.argv[4])
# basis g_k(t)=t^2(mu^2-t^2)^3 t^{2k}, combos with int g=0 handled later via pole functionals
tg,wg=np.polynomial.legendre.leggauss(400); tt=(tg+1)/2*mu; wt=wg*mu/2
K=10
def ghat(X,k):  # even g: 2 int_0^mu g cos(2pi X t)
    g=tt**2*(mu**2-tt**2)**3*np.cos(k*np.pi*tt/mu)/mu**8
    return 2*np.cos(2*np.pi*np.outer(X,tt))@(g*wt)
gx,gw=np.polynomial.legendre.leggauss(int(sys.argv[5]))
Xs=[];Ws=[]
for n in range(1,N+1):
    Xs.append(n+(gx+1)/2);Ws.append(gw/2)
Xs=np.array(Xs);Ws=np.array(Ws)
rho=np.array([ghat(Xs.ravel(),k).reshape(Xs.shape) for k in range(K)])
nrm=np.sqrt(np.einsum('knm,nm->k',rho**2,Ws)); rho=rho/nrm[:,None,None]
ns=np.arange(1,N+1)
def pieces(s):
    s=np.atleast_1d(s).astype(complex)
    out=[]
    lX=np.log(Xs)
    Fs=[];FL=[];Rs=[]
    for sv in s:
        I=np.einsum('knm,nm->kn',rho,Ws*np.exp(-sv*lX))   # K,N
        Z=np.cumsum(ns**(sv-1.0)); L=np.cumsum(ns**(sv-1.0)*np.log(ns))
        Fs.append(I@Z);FL.append(I@L);Rs.append(I.sum(1))
    return np.array(Fs).T,np.array(FL).T,np.array(Rs).T
tau=np.arange(dt/2,TM,dt); s=0.5+1j*tau
F,FL,R=pieces(s)
z1=np.array([complex(mp.zeta(1-x)) for x in s]); zp1=np.array([complex(mp.zeta(1-x,derivative=1)) for x in s])
Th=np.array([float(mp.re(mp.digamma(0.25+0.5j*t)))-np.log(np.pi) for t in tau])
F0=z1*R; F0L=-zp1*R; G=F-F0; GL=FL-F0L
def Qf(U,UL,V,VL):
    m=(Th*(np.conj(U)[:,None,:]*V[None]).real-(np.conj(U)[:,None,:]*VL[None]).real-(np.conj(UL)[:,None,:]*V[None]).real)
    M=2*m.sum(-1)*dt/(2*np.pi); return (M+M.T)/2 if U is V else M
QF=Qf(F,FL,F,FL); QG=Qf(G,GL,G,GL); C=Qf(F0,F0L,G,GL); Cs=(C+C.T)/2; Q00=Qf(F0,F0L,F0,F0L)
F1,FL1,R1=pieces(np.array([1.0])); F0_,FL0,R0=pieces(np.array([1e-9]))
A=F1[:,0].real;B=F0_[:,0].real
# R'(0): numerical
_,_,Rp=pieces(np.array([1e-5])); _,_,Rm=pieces(np.array([-1e-5])); Rd=((Rp-Rm)/2e-5)[:,0].real
P=np.outer(A,B); Qfull=QF+P+P.T
np.set_printoptions(precision=4,linewidth=150)
print("max|Q00|",abs(Q00).max(),"scale",abs(QF).max())
print("eig Qfull",np.linalg.eigvalsh(Qfull))
print("eig QG",np.linalg.eigvalsh(QG))
# pole functionals: A,B,rho0=R(0),R(1),R'(0),G(1)=A+R(1)/2
Pm=np.array([A,B,R0[:,0].real,R1[:,0].real,Rd])
U,S,Vt=np.linalg.svd(Pm); Kb=Vt[len(S):].T
print("sv pole",S, "dimK",Kb.shape[1])
for nm,M in [("Qfull|K",Qfull),("QG|K",QG),("2C|K",2*Cs)]:
    print(nm,np.linalg.eigvalsh(Kb.T@M@Kb))
# generalized: ratio 2C vs QG on K
MG=Kb.T@QG@Kb; MC=Kb.T@(2*Cs)@Kb
w,V=np.linalg.eigh(MG)
print("QG|K eig",w)
if w.min()>0:
    L=V/np.sqrt(w); print("eig QG^-1/2 2C QG^-1/2 on K", np.linalg.eigvalsh(L.T@MC@L))
# identity check: Q(F0,F) vs residue form
CF=Qf(F0,F0L,F,FL)
print("diag Q(F0,G)",np.diag(C)," diag Q(F0,F)",np.diag(CF))
print("½R(1)B",0.5*R1[:,0].real*B, " R(0)[log2pi A+FL(1)]",R0[:,0].real*(np.log(2*np.pi)*A+FL1[:,0].real))
np.savez('out_%g.npz'%mu,QF=QF,QG=QG,C=C,A=A,B=B,R0=R0,R1=R1,Rd=Rd,FL1=FL1)

QFG=C+QG  # C[i,j]=Q(F0_i,G_j); Q(F_i,G_j)=C+QG
FL1v=FL1[:,0].real
Pm2=np.array([A,B,R0[:,0].real,R1[:,0].real,Rd,FL1v])
for k in [2,4,6]:
  U_,S_,Vt_=np.linalg.svd(Pm2[:k] if k<6 else Pm2); Pp=np.eye(K)-Vt_[:len(S_)].T@Vt_[:len(S_)]
  for nm,M in [("Q(F,G)",QFG),("Q(F0,G)",C)]:
    print(k,nm,"|P⊥ M P⊥|/|M| =",np.linalg.norm(Pp@M@Pp,2)/np.linalg.norm(M,2))
print("sv Q(F,G)",np.linalg.svd(QFG,compute_uv=False))
print("sv QF",np.linalg.eigvalsh(QF)); print("2AB eig",np.linalg.eigvalsh(P+P.T))
print("|Q(F,G)|/|QF|",np.linalg.norm(QFG,2)/np.linalg.norm(QF,2))
Qs=(QFG+QFG.T)
print("eig -QG",np.linalg.eigvalsh(-QG)); print("eig 2symQ(F,G)",np.linalg.eigvalsh(Qs)); 
print("eig -QG+2symQFG",np.linalg.eigvalsh(-QG+Qs)); print("eig -QG+2symQFG+2AB (=Qfull)",np.linalg.eigvalsh(-QG+Qs+P+P.T))
