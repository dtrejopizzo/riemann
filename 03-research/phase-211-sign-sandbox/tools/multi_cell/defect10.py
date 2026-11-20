# transport defect on the measured high-block bottom vectors (T=0.8, res2.pkl of ROUND_016_B)
import os,sys,pickle,numpy as np, scipy.special as sp
TD='/home/trabajo/Documentos/research/riemann/03-research/phase-211-sign-sandbox/tools/tail_direct'
os.environ.setdefault('NPZ','fake.npz')
src=open('tail10.py').read()
exec(src)
RES=pickle.load(open(os.environ.get('RES',TD+'/res2.pkl'),'rb'))
Tv=T
def weights(xi):
    I=lambda a,b: 2*(np.sin(2*np.pi*xi*b)-np.sin(2*np.pi*xi*a))/(2*np.pi*xi)
    Il=lambda a,b: 2*(sp.sici(2*np.pi*xi*b)[1]-sp.sici(2*np.pi*xi*a)[1])
    ns=[n for n in range(1,50) if n*np.exp(-Tv)<lam]
    return {'f0':2*np.ones_like(xi),'flam':2*np.cos(2*np.pi*lam*xi),
     'A':sum(I(n*np.exp(-Tv),min(n*np.exp(Tv),lam))/n for n in ns),
     'B':sum(Il(n*np.exp(-Tv),min(n*np.exp(Tv),lam)) for n in ns)}
cell=s<2*lam; Wt=weights(s)
for K,r in RES.items():
    u=r['u']; nu=np.trapz(u**2*s,t)        # = |F1|^2 (half-line)
    uc=u*cell; nc=np.trapz(uc**2*s,t)
    ch,A_,C_,_=ledger(u,60); lN=np.log([q[0] for q in ch]); B=A_-(lN[:,None]+lN[None,:])*C_
    PA,PB=polar(u); Wex=B.sum()+2*PA*PB
    chc,Ac,Cc,_=ledger(uc,1); Qc=Ac[0,0]
    # transported functionals on the first-cell part F1^cell: <F,w> = int u w dxi
    c=np.array([np.trapz(uc*Wt[k]*s,t) for k in Wt]); Wm=np.array([[np.trapz(Wt[a]*Wt[b]*s*s**0*(1/s)*s,t) for b in Wt] for a in Wt])
    # Gram of weights in L2(dx) on the cell: <w_a,w_b> = int xi w_a w_b dx = int w_a w_b dxi ; in t: ds = s dt
    Gw=np.array([[np.trapz((Wt[a]*Wt[b]*s)[cell],t[cell]) for b in Wt] for a in Wt])
    dist2=c@np.linalg.solve(Gw,c)
    print(f"K={K}: tail-mass beyond 2lam {1-nc/nu:.4f} | W_exact(Tu)+2AB={Wex:.5f} (polar {2*PA*PB:.1e}) | Q[F1cell]={Qc:.5f} | defect value {(Wex-Qc)/nu:+.5f} (per |F1|^2) | Rayleigh exact {Wex/nu:.4f} cell {Qc/nc:.4f} | transported constraints on F1cell: cos {np.round(c/np.sqrt(np.diag(Gw)*nc),4)} dist(F,V)/|F|={np.sqrt(dist2/nc):.4f}",flush=True)
