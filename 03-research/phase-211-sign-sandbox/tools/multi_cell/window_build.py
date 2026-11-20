# Build and cache the R-cell complete form split by comb atom:  Q(w) = Q0 - sum_n w_n Q_n  (n prime power < R),
# Q0 = D^T Arch D + a b^T + b a^T,  Q_n = D^T Pi_n D,  Pi_n = v_n c^sym(log n),  D = sum_{N<R} N^{-1/2} tau_{log N} (cell transfer),
# plus the four transported constraints C and the gauge form L (as cellRg_mp.py). usage: R Nb T J dps [NQ]
import sys, time, os, pickle, mpmath as mp
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-211-sign-sandbox/tools')
import galerkin_mp as Gm
R=int(sys.argv[1]); Nb=int(sys.argv[2]); T=mp.mpf(sys.argv[3]); J=int(sys.argv[4]); dps=int(sys.argv[5])
NQ=int(sys.argv[6]) if len(sys.argv)>6 else 160
OUT=f"/tmp/phase211/r21/split_{R}_{Nb}_{sys.argv[3]}_{J}_{dps}_{NQ}.pkl"
mp.mp.dps=dps; t0=time.time()
ell=mp.log(R); h=ell/2
Dd=Gm.build(h,Nb,dps=dps,verbose=False,cache=True,errcheck=False); mp.mp.dps=dps
Arch=Dd['Arch']; L_=2*h; al=[k*mp.pi/L_ for k in range(1,Nb+1)]
atoms=[(n,Gm._Lam(n)) for n in range(2,R) if Gm._Lam(n)]
Pin={}
for n,p in atoms:
    v=2*mp.log(p)/mp.sqrt(n); M=mp.matrix(Nb,Nb)
    for j in range(1,Nb+1):
        for k in range(j,Nb+1): M[j-1,k-1]=M[k-1,j-1]=v*Gm._c_sym(j,k,mp.log(n),L_,al)
    Pin[n]=M
# consistency with the Lambda comb
Ptot=sum((Pin[n] for n in Pin),mp.matrix(Nb,Nb)) if Pin else mp.matrix(Nb,Nb)
print('Pi consistency',mp.nstr(mp.mnorm(Ptot-Dd['Pi'],1),3),flush=True)
nodes={}
def GL(n):
    if n not in nodes:
        from flint import arb, ctx
        ctx.prec=int(mp.mp.prec)+20
        nodes[n]=[(mp.mpf(x.mid().str(mp.mp.dps+5,radius=False)),mp.mpf(w.mid().str(mp.mp.dps+5,radius=False))) for x,w in (arb.legendre_p_root(n,k,weight=True) for k in range(n))]
    return nodes[n]
def quad_nodes(a,b,n): return [((a+b)/2+(b-a)/2*x,(b-a)/2*w) for x,w in GL(n)]
e=lambda k,z: mp.sin(k*mp.pi*(z+h)/ell)/mp.sqrt(h)
Tm=mp.matrix(Nb,Nb)
for N in range(1,R):
    lN=mp.log(N)
    for z,w in quad_nodes(-h+lN,h,NQ):
        Ei=[e(k,z) for k in range(1,Nb+1)]; Ej=[e(k,z-lN) for k in range(1,Nb+1)]
        c=w/mp.sqrt(N)
        for i in range(Nb):
            for j in range(Nb): Tm[i,j]+=c*Ei[i]*Ej[j]
print('Tm',round(time.time()-t0),flush=True)
ZN=quad_nodes(-h,h,NQ); EZ=[[e(k,z) for k in range(1,Nb+1)] for z,w in ZN]
def proj(fn):
    v=mp.matrix(Nb,1)
    for (z,w),Ez in zip(ZN,EZ):
        fz=fn(z)*w
        for k in range(Nb): v[k]+=Ez[k]*fz
    return v
lam=mp.exp(T); xw=lambda z: z-T-h
a_=Tm.T*proj(lambda z: mp.exp(xw(z)/2)); b_=Tm.T*proj(lambda z: mp.exp(-xw(z)/2))
Q0=Tm.T*Arch*Tm+a_*b_.T+b_*a_.T
Qn={n:Tm.T*Pin[n]*Tm for n in Pin}
ns=[n for n in range(1,50) if n*mp.exp(-T)<lam]
def I_(xi,a,b): return 2*(mp.sin(2*mp.pi*xi*b)-mp.sin(2*mp.pi*xi*a))/(2*mp.pi*xi)
def Il(xi,a,b): return 2*(mp.ci(2*mp.pi*xi*b)-mp.ci(2*mp.pi*xi*a))
def wfun(key,z):
    xi=mp.exp(-xw(z)); wt=mp.sqrt(xi)
    if key=='f0': return 2*wt
    if key=='flam': return 2*mp.cos(2*mp.pi*lam*xi)*wt
    if key=='A': return wt*mp.fsum(I_(xi,n*mp.exp(-T),min(n*mp.exp(T),lam))/n for n in ns)
    if key=='B': return wt*mp.fsum(Il(xi,n*mp.exp(-T),min(n*mp.exp(T),lam)) for n in ns)
C=mp.matrix(Nb,4)
for i,k in enumerate(['f0','flam','A','B']):
    v=proj(lambda z: wfun(k,z))
    for j in range(Nb): C[j,i]=v[j]
SN=quad_nodes(mp.mpf(0),mp.mpf(1),NQ)
phi=[[(1-s*s)**3*s*s*mp.legendre(2*i,s) for s,w in SN] for i in range(J)]
ints=[mp.fsum(p[q]*SN[q][1] for q in range(NQ)) for p in phi]
phi=[[phi[i][q]-ints[i]/ints[0]*phi[0][q] for q in range(NQ)] for i in range(1,J)]; Jg=J-1
def ghat(xi):
    cs=[mp.cos(2*mp.pi*xi*s/lam)*w for s,w in SN]
    return [2/lam*mp.fsum(p[q]*cs[q] for q in range(NQ)) for p in phi]
Cg=mp.matrix(Nb,Jg)
for (z,w),Ez in zip(ZN,EZ):
    xi=mp.exp(-xw(z)); g=ghat(xi); f=mp.sqrt(xi)*w
    for j in range(Jg):
        gj=g[j]*f
        for k in range(Nb): Cg[k,j]+=Ez[k]*gj
G=mp.matrix(Jg,Jg)
for i in range(Jg):
    for j in range(i,Jg): G[i,j]=G[j,i]=mp.fsum(phi[i][q]*phi[j][q]*SN[q][1] for q in range(NQ))/lam
for xi,w in quad_nodes(mp.mpf(0),lam,NQ):
    g=ghat(xi)
    for i in range(Jg):
        for j in range(i,Jg): G[i,j]-=w*g[i]*g[j]
for i in range(Jg):
    for j in range(i): G[i,j]=G[j,i]
L=mp.eye(Nb)-Cg*mp.inverse(G)*Cg.T
tos=lambda M_: [[mp.nstr(M_[i,j],dps+5) for j in range(M_.cols)] for i in range(M_.rows)]
pickle.dump({'Q0':tos(Q0),'Qn':{n:tos(Qn[n]) for n in Qn},'C':tos(C),'L':tos(L),'Tm':tos(Tm),'dps':dps},open(OUT,'wb'))
print('saved',OUT,round(time.time()-t0),flush=True)
