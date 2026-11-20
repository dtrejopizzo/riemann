import os; HERE=os.path.dirname(os.path.abspath(__file__))
exec(open(''+HERE+'/tail.py').read())
def bottom(top):
    I=[a for a in range(len(kH)) if kH[a]<=top]; d=DH[I]; sq=1/np.sqrt(d)
    Gh=GH[np.ix_(I,I)]*sq[:,None]*sq[None,:]; Ch=Cb[I]*sq[:,None]; Jh=Jn[I]*sq[:,None]
    Qx=sl.null_space(np.hstack([Ch,Jh]).T); E,V=np.linalg.eigh(Qx.T@Gh@Qx); v=Qx@V[:,0]
    return I, v*sq, E[0], v@Gh@v
res={}
for top in [56,64,72,80,88,96]:
    I,b,e0,chk=bottom(top)
    u=sum(b[j]*U[kH[i]] for j,i in enumerate(I)); nu=2*np.trapz(u**2*s,t)
    ch,A,C,At=ledger(u,60); Ns=np.array([x[0] for x in ch]); lN=np.log(Ns)
    B=A-(lN[:,None]+lN[None,:])*C; W=B.sum()
    dg=np.diag(B); off=W-dg.sum()
    # split off-diagonal: archimedean vs comb
    offA=A.sum()-np.trace(A); offC=-((lN[:,None]+lN[None,:])*C).sum()+np.trace((2*lN[:,None]*np.eye(len(Ns)))*C)
    mN=np.diag(A)/np.diag(C)
    J1=ch[0][2]; jt=(1/np.pi)*J1**2  # scale of jump term
    m12=np.trapz((u**2*s)[(s<2*lam)],t[(s<2*lam)])*2/nu
    print(f"K={top} galerkin {e0:.4f} direct {W:.4f} ratio {e0/W:.4f} |u|^2 {nu:.4f} | B11 {dg[0]:.4f} B22 {dg[1]:.4f} sum_{{N>=3}} diag {dg[2:].sum():.4f} | offdiag arch {offA:.4f} comb {offC:.4f} | |F1|^2 {C[0,0]:.4f} <m>_1 {mN[0]:.3f} <m>_2 {mN[1]:.3f} | J1^2 {J1**2:.4f} | mass(lam,2lam) {m12:.3f}",flush=True)
    res[top]=dict(b=b,u=u,B=B,A=A,C=C,Ns=Ns)
pickle.dump(res,open(''+HERE+'/res2.pkl','wb'))
