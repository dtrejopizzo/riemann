# high-precision version of cellRg.py: R-cell complete form vs l_g on transported constraints. usage: R Nb T J c dps
import sys, time, mpmath as mp
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-211-sign-sandbox/tools')
import galerkin_mp as Gm
mp.mp.dps=int(sys.argv[6]); R=int(sys.argv[1]); Nb=int(sys.argv[2]); T=mp.mpf(sys.argv[3]); J=int(sys.argv[4]); cc=mp.mpf(sys.argv[5]); dps=int(sys.argv[6])
t0=time.time()
ell=mp.log(R); Dd=Gm.build(ell/2,Nb,dps=dps,verbose=False,cache=True,errcheck=False)
mp.mp.dps=dps
W=Dd['Arch']-cc*Dd['Pi']
def gl(a,b,n):
    xs,ws=zip(*[(x,w) for x,w in mp.gauss_legendre_nodes(n)]) if False else (None,None)
nodes={}
def GL(n):
    if n not in nodes:
        from flint import arb, ctx
        ctx.prec=int(mp.mp.prec)+20
        r=[]
        for k in range(n):
            x,w=arb.legendre_p_root(n,k,weight=True)
            r.append((mp.mpf(x.mid().str(mp.mp.dps+5,radius=False)),mp.mpf(w.mid().str(mp.mp.dps+5,radius=False))))
        nodes[n]=r
    return nodes[n]
def quad_nodes(a,b,n):
    return [((a+b)/2+(b-a)/2*x,(b-a)/2*w) for x,w in GL(n)]
h=ell/2
e=lambda k,z: mp.sin(k*mp.pi*(z+h)/ell)/mp.sqrt(h)
NQ=int(sys.argv[7]) if len(sys.argv)>7 else 160
# T operator: (Tm)_{ij} = sum_N N^{-1/2} int_{-h+logN}^{h} e_i(z) e_j(z-logN) dz
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
def proj(fn):  # vector <e_k, fn>
    v=mp.matrix(Nb,1)
    for (z,w),Ez in zip(ZN,EZ):
        fz=fn(z)*w
        for k in range(Nb): v[k]+=Ez[k]*fz
    return v
lam=mp.exp(T)
xw=lambda z: z-T-h
a_=Tm.T*proj(lambda z: mp.exp(xw(z)/2)); b_=Tm.T*proj(lambda z: mp.exp(-xw(z)/2))
Q=Tm.T*W*Tm+a_*b_.T+b_*a_.T
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
Qf,_=mp.qr(C,mode='full'); Vn=Qf[:,4:Nb]
print('constraints',round(time.time()-t0),flush=True)
# gauge: phi_i(s)=(1-s^2)^3 s^2 P_{2i}(s), s=lam*y in (0,1), i<J ; combos with int phi = 0
SN=quad_nodes(mp.mpf(0),mp.mpf(1),NQ)
phi=[[ (1-s*s)**3*s*s*mp.legendre(2*i,s) for s,w in SN] for i in range(J)]
ints=[mp.fsum(p[q]*SN[q][1] for q in range(NQ)) for p in phi]
phi=[[phi[i][q]-ints[i]/ints[0]*phi[0][q] for q in range(NQ)] for i in range(1,J)]; Jg=J-1
def ghat(xi):  # 2 int_0^{1/lam} phi(lam y) cos(2 pi xi y) dy = (2/lam) int_0^1 phi(s) cos(2 pi xi s/lam) ds
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
print('gauge',round(time.time()-t0),'cond G',mp.nstr(max(mp.eigsy(G)[0])/min(mp.eigsy(G)[0]),3),flush=True)
L=mp.eye(Nb)-Cg*mp.inverse(G)*Cg.T
A=Vn.T*Q*Vn; B=Vn.T*L*Vn
Lc=mp.cholesky(B); Li=mp.inverse(Lc); M=Li*A*Li.T; M=(M+M.T)/2
ev=sorted(mp.eigsy(M)[0]); eA=sorted(mp.eigsy((A+A.T)/2)[0]); eB=sorted(mp.eigsy((B+B.T)/2)[0])
print(f"MP R={R} T={T} Nb={Nb} J={J} c={cc} dps={dps}: Q/|F|^2 on V {[mp.nstr(x,4) for x in eA[:3]]} | l_g/|F|^2 on V min {mp.nstr(eB[0],4)} | Q/l_g {[mp.nstr(x,5) for x in ev[:3]]} | (lam/2)kappa={mp.nstr(lam/2*ev[0],5)} | {round(time.time()-t0)}s",flush=True)
