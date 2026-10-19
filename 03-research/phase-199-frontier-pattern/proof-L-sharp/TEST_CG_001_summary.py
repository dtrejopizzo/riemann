# TEST_CG_001 compact table: python3 TEST_CG_001_summary.py OUT.npz [J list]; env CG_CUT (Gram cutoff, default 1e-11)
import sys, os, numpy as np
sys.argv=[sys.argv[0]]+sys.argv[1:]
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'TEST_CG_001_analysis.py')).read().split('print("mu",mu')[0]
exec(src)
print("# mu=%g  cut=%g   C0 contour vs line rel.diff at T=2000: %.1e"%(mu,CUT,np.abs(forms(2000,'c')[4]-forms(2000,'l')[4]).max()/np.abs(forms(2000,'c')[4]).max()))
print("J  proj T    dim  minQQ    maxQQ    min(-QGG) max(-QGG) minS      maxS     theta   rkFG(1e-2) P⊥2    P⊥4   maxrel|QQ-(-QGG)|")
for Ju in Juse:
  for proj in (True,False):
    if not proj and Ju!=Juse[0]: continue
    U=basis(Ju,proj)
    for T in (500,1000,2000):
        QQ,QGG,S,QF,C0=forms(T); eQ=ev(QQ,U); eG=ev(-QGG,U); eS=ev(S,U)
        g=sym(U.T@(-QGG)@U); e,v=np.linalg.eigh(g)
        th=np.nan
        if e.min()>0: L=v/np.sqrt(e); th=np.abs(np.linalg.eigvalsh(sym(L.T@U.T@S@U@L))).max()
        M=U.T@sym(QF-C0.T)@U; sv=np.linalg.svd(M,compute_uv=False); rk=(sv>1e-2*sv[0]).sum()
        Pf=np.array([A,B,d['R1'],d['FL1']])@U; r=[]
        for k in (2,4):
            uu,ss,vt=np.linalg.svd(Pf[:k]); Pp=np.eye(U.shape[1])-vt[:k].T@vt[:k]; r.append(np.linalg.norm(Pp@M@Pp,2)/np.linalg.norm(M,2))
        print("%-2d %-4s %-5d %-4d %-8.5f %-8.5f %-9.5f %-9.5f %-9.5f %-8.5f %-7.4f %-10d %-6.3f %-6.3f %.3f"%(Ju,'y' if proj else 'n',T,U.shape[1],eQ[0],eQ[-1],eG[0],eG[-1],eS[0],eS[-1],th,rk,r[0],r[1],np.abs(eQ/eG-1).max()))
