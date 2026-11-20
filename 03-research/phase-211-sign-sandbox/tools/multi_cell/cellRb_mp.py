# R-cell complete form vs l_g with the band-concentration constraint family S_theta (top eigenspace of the PW type-2pi lam concentration operator in the cell basis). usage: R Nb T J c dps NQ thetas(comma)
import sys, time, mpmath as mp
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-211-sign-sandbox/tools')
import galerkin_mp as Gm
mp.mp.dps=int(sys.argv[6]); R=int(sys.argv[1]); Nb=int(sys.argv[2]); T=mp.mpf(sys.argv[3]); J=int(sys.argv[4]); cc=mp.mpf(sys.argv[5]); dps=int(sys.argv[6])
t0=time.time()
import os, pickle
CF=f"/tmp/phase211/r19/cache_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_{sys.argv[6]}.pkl"
if os.path.exists(CF):
    dd=pickle.load(open(CF,'rb')); mp.mp.dps=dps
    tomp=lambda rows: mp.matrix([[mp.mpf(x) for x in r] for r in rows])
    Q=tomp(dd['Q']); C=tomp(dd['C']); L=tomp(dd['L']); lam=mp.exp(T); h=mp.log(R)/2; ell=mp.log(R)
    print('loaded cache',flush=True)
else:

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

    tos=lambda M_: [[mp.nstr(M_[i,j],dps+5) for j in range(M_.cols)] for i in range(M_.rows)]
    pickle.dump({'Q':tos(Q),'C':tos(C),'L':tos(L)},open(CF,'wb'))
import numpy as np
thetas=[float(t) for t in sys.argv[8].split(',')] if len(sys.argv)>8 else [0.0,0.5,0.9,0.99]
# concentration matrix in the cell basis: psi_k(xi)=xi^{-1/2} e_k(T+h-log xi), orthonormal in L2(lam,R lam)
lf=float(lam); hf=float(h); ellf=float(ell); Tf=float(T)
xn,xw_=np.polynomial.legendre.leggauss(int(400+300*R*lf))
xs=lf+(R-1)*lf*(xn+1)/2; ws=(R-1)*lf*xw_/2
zz=Tf+hf-np.log(xs)
Psi=np.array([np.sin(k*np.pi*(zz+hf)/ellf)/np.sqrt(hf)/np.sqrt(xs) for k in range(1,Nb+1)])  # Nb x n
d=xs[:,None]-xs[None,:]; s=xs[:,None]+xs[None,:]
Kb=2*lf*np.sinc(2*lf*d)+2*lf*np.sinc(2*lf*s)   # sin(2 pi lam t)/(pi t) = 2 lam sinc(2 lam t)
Pw=Psi*ws[None,:]; Bc=Pw@Kb@Pw.T; Bc=(Bc+Bc.T)/2
cb,Ub=np.linalg.eigh(Bc)
print('band: Gram check',np.abs(Pw@Psi.T-np.eye(Nb)).max(),'conc eigs top',np.round(cb[::-1][:3],4),'#>=0.5:',int((cb>=0.5).sum()),'#>=0.99',int((cb>=0.99).sum()),flush=True)
def mpmat(a): 
    M_=mp.matrix(a.shape[0],a.shape[1])
    for i in range(a.shape[0]):
        for j in range(a.shape[1]): M_[i,j]=mp.mpf(float(a[i,j]))
    return M_
Qs=(Q+Q.T)/2; Ls=(L+L.T)/2
for th in thetas:
    U=Ub[:,cb>=th]; s_=U.shape[1]
    if s_<=5: print(f'theta={th}: dim {s_} too small'); continue
    Um=mpmat(U); CU=Um.T*C
    Qf2,_=mp.qr(CU,mode='full'); Vb=Um*Qf2[:,4:s_]
    A=Vb.T*Qs*Vb; Bm=Vb.T*Ls*Vb
    Lc=mp.cholesky((Bm+Bm.T)/2); Li=mp.inverse(Lc); M=Li*A*Li.T; M=(M+M.T)/2
    E_,V_=mp.eigsy(M); idx=sorted(range(len(E_)),key=lambda i:E_[i])
    ev=[E_[i] for i in idx]; y=Li.T*V_[:,idx[0]]; v=Vb*y
    vn=np.array([float(v[i]) for i in range(Nb)]); vn/=np.linalg.norm(vn)
    eA=sorted(mp.eigsy((A+A.T)/2)[0]); eB=sorted(mp.eigsy((Bm+Bm.T)/2)[0])
    print(f"MPB R={R} T={T} Nb={Nb} J={J} c={cc} dps={dps} theta={th} dim={s_}: Q/|F|^2 min {mp.nstr(eA[0],4)} | l_g/|F|^2 min {mp.nstr(eB[0],4)} | Q/l_g {[mp.nstr(x,5) for x in ev[:3]]} | out-of-band frac of bottom {1-vn@Bc@vn:.3e} | {round(time.time()-t0)}s",flush=True)

# cone version: ||(1-P_band)u||^2 <= eps ||u||^2 ; trace the frontier by the penalty Q + mu (I - Bc) against l_g on V
if os.environ.get('BCMP'):
    # concentration matrix in ball arithmetic: Bc_kl = int_0^lam c_k(x) c_l(x) dx, c_k(x) = 2 int_J psi_k(xi) cos(2 pi x xi) dxi (composite GL)
    from flint import arb, arb_mat, ctx
    ctx.prec=int(3.4*dps)+60
    NP=int(os.environ.get('NPAN','60')); NG=30
    gn=[arb.legendre_p_root(NG,k,weight=True) for k in range(NG)]
    def comp(a,b):
        out=[]
        for q in range(NP):
            lo=a+(b-a)*q/NP; hi=a+(b-a)*(q+1)/NP
            for x_,w_ in gn: out.append(((lo+hi)/2+(hi-lo)/2*x_,(hi-lo)/2*w_))
        return out
    lamA=arb(sys.argv[3]).exp(); ellA=arb(R).log(); hA=ellA/2; TA=arb(sys.argv[3])
    XI=comp(lamA,R*lamA); XX=comp(arb(0),lamA); n1=len(XI); n2=len(XX)
    PsiW=arb_mat(Nb,n1)
    for j,(xi_,w_) in enumerate(XI):
        zz_=TA+hA-xi_.log(); f_=w_*2/(hA.sqrt()*xi_.sqrt())
        for k in range(1,Nb+1): PsiW[k-1,j]=(arb(k)*arb.pi()*(zz_+hA)/ellA).sin()*f_
    Cm=arb_mat(n1,n2)
    for i,(xi_,_) in enumerate(XI):
        for j,(x_,_) in enumerate(XX): Cm[i,j]=(2*arb.pi()*x_*xi_).cos()
    Ck=PsiW*Cm
    for j,(x_,w_) in enumerate(XX):
        r=w_.sqrt()
        for k in range(Nb): Ck[k,j]=Ck[k,j]*r
    BA=Ck*Ck.transpose()
    Bm_=mp.matrix(Nb,Nb)
    for i in range(Nb):
        for j in range(Nb): Bm_[i,j]=mp.mpf(BA[i,j].mid().str(dps+5,radius=False))
    print('Bc in ball arithmetic: max radius',max(float(BA[i,j].rad()) for i in range(Nb) for j in range(Nb)),' max |Bc_mp - Bc_double|',max(abs(float(Bm_[i,j])-Bc[i,j]) for i in range(Nb) for j in range(Nb)),flush=True)
else:
    Bm_=mpmat(Bc)
Pen=mp.eye(Nb)-Bm_; Pen=(Pen+Pen.T)/2
print('min eig of penalty',mp.nstr(min(mp.eigsy(Pen)[0]),4),flush=True)
Qf,_=mp.qr(C,mode="full"); Vn=Qf[:,4:Nb]
A0=Vn.T*Qs*Vn; L0=Vn.T*Ls*Vn; P0=Vn.T*Pen*Vn
Lc=mp.cholesky((L0+L0.T)/2); Li=mp.inverse(Lc)
mus=[float(x) for x in os.environ.get('MUS','1e-14,1e-12,1e-10,1e-8,1e-6,1e-4,1e-2,1').split(',')]
for mu in mus:
    M=Li*(A0+mp.mpf(mu)*P0)*Li.T; M=(M+M.T)/2
    E_,V_=mp.eigsy(M); i0=min(range(len(E_)),key=lambda i:E_[i]); y=Li.T*V_[:,i0]
    qv=(y.T*A0*y)[0]; lv=(y.T*L0*y)[0]; pv=(y.T*P0*y)[0]; nv=(y.T*y)[0]
    print(f"PEN R={R} T={T} Nb={Nb} mu={mu:.0e}: bottom Q/l_g={mp.nstr(qv/lv,5)}  out-of-band eps={mp.nstr(pv/nv,4)}  Q/|F|^2={mp.nstr(qv/nv,4)} l_g/|F|^2={mp.nstr(lv/nv,4)}",flush=True)
