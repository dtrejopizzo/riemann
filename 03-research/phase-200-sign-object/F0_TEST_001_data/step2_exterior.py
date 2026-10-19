# F0_TEST_001 step 2: exterior datum r* = Ff*|_(λ,∞) of Mori's μ=15 even extremal, same conventions as
# MORI15_EXTREMAL_001_prolate_M28.py (Möbius inverse f1 on [1/λ,λ], min-leak gauge M=28 even Legendre on |u|<1/λ with
# constraints φ(0)=0, ∫f=0, 81 prolates c=30π), but with dense Gauss-Legendre nodes so that ρ(ω)=r*(λω) is resolved
# up to ω = OMX.  arb 400 bits for f, 256 bits for the Fourier sums.  NUMERICO.
import json,os,time,math,sys
from pathlib import Path
from multiprocessing import Pool
import numpy as np
from flint import arb,arb_mat,ctx
ctx.prec=400
DATA=Path('/home/trabajo/Documentos/research/riemann/03-research/phase-199-frontier-pattern/proof-L-sharp/MORI15_EXTREMAL_001_data')
OUT=Path(__file__).resolve().parent
OMX=float(os.environ.get('OMX','60')); DOM=float(os.environ.get('DOM','0.0025')); FAC=float(os.environ.get('FAC','0.65'))
E=json.load(open(DATA/'p0_eig.json')); V=[arb(arb(x).mid()) for x in E['vectors'][0]]
N=1664; mu=15; L=arb(mu).log()/2; lam=arb(mu).sqrt(); pi=arb.pi(); c=2*pi*mu
coef=[arb(0)]*N
for t,j in enumerate(range(0,N,2)): coef[j]=V[t]*(arb(2*j+1)/(2*L)).sqrt()
mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]
def g_at(x):
    s_=(x/L).mid(); P0,P1=arb(1),s_; s=coef[0]
    for n in range(1,N-1):
        P0,P1=P1,(((2*n+1)*s_*P1-n*P0)/(n+1)).mid()
        if n%2==1: s+=coef[n+1]*P1
    return s
def f1_str(us):
    ctx.prec=400; out=[]
    for u in us:
        u=arb(u); s=arb(0)
        for mm in range(1,15):
            if mob[mm] and mm*u<lam: s+=mob[mm]*g_at((mm*u).log())/(mm*u).sqrt()
        out.append(s.str(70,radius=False))
    return out
def gl(n):
    xs=[];ws=[]
    for k in range(n):
        x,w=arb.legendre_p_root(n,k,weight=True); xs.append(x); ws.append(w)
    return xs,ws
def pmap(P,fn,items,chunks=200):
    ch=[items[i::chunks] for i in range(chunks)]
    R=P.map(fn,ch); res=[None]*len(items)
    for i,r in enumerate(R):
        for k,v in enumerate(r): res[i+k*chunks]=v
    return res
def rho_chunk(args):
    oms,=args; ctx.prec=int(os.environ.get('RPREC','256'))
    nodes=json.load(open(OUT/('nodes%s.json'%os.environ.get('NTAG','')))); U=[arb(u) for u in nodes['u']]; W=[arb(w) for w in nodes['wf']]
    tp=2*arb.pi()*arb(15).sqrt(); out=[]
    for om in oms:
        z=tp*arb(om); out.append(sum(w*(z*u).cos() for u,w in zip(U,W)).str(int(os.environ.get("RDIG","30")),radius=False))
    return out
if __name__=='__main__':
    t0=time.time(); P=Pool(20)
    stage=sys.argv[1]
    if stage=='gauge':
        NPF=os.environ.get('NP'); pieces=[]
        allu=[]
        for m in range(1,15):
            lo=lam/(m+1); hi=lam/m; h=(hi-lo)/2; cc=(hi+lo)/2
            NP=int(NPF) if NPF else int(1.1*1930*math.log((m+1)/m))+200
            xs,ws=gl(NP)
            us=[cc+h*x for x in xs]; wu=[w*h for w in ws]; pieces.append((us,wu)); allu+= [u.str(80,radius=False) for u in us]
        fv=pmap(P,f1_str,allu); fv=[arb(x) for x in fv]; print('f1 gauge nodes',time.time()-t0,flush=True)
        # prolates (verbatim conventions of MORI15_EXTREMAL_001_prolate_M28.py)
        n=300; diag=[];off=[]
        for t in range(n):
            j=2*t
            diag.append(arb(j*(j+1))+c*c*(2*j*(j+1)-1)/((2*j+3)*(2*j-1)))
            off.append(c*c*(j+2)*(j+1)/((2*j+3)*(arb((2*j+1)*(2*j+5))).sqrt()))
        Md=np.diag([float(x) for x in diag])+np.diag([float(x) for x in off[:-1]],1)+np.diag([float(x) for x in off[:-1]],-1)
        evd,evecd=np.linalg.eigh(Md)
        def thomas(sig,rhs):
            a=[off[t-1] for t in range(1,n)]; b=[diag[t]-sig for t in range(n)]; cc=[off[t] for t in range(n-1)]
            cp=[arb(0)]*n; dp=[arb(0)]*n; cp[0]=cc[0]/b[0]; dp[0]=rhs[0]/b[0]
            for i in range(1,n):
                den=b[i]-a[i-1]*cp[i-1]; cp[i]=(cc[i]/den) if i<n-1 else arb(0); dp[i]=(rhs[i]-a[i-1]*dp[i-1])/den
            x=[arb(0)]*n; x[n-1]=dp[n-1]
            for i in range(n-2,-1,-1): x[i]=dp[i]-cp[i]*x[i+1]
            return x
        P0h=[((-1)**t)*arb.fac_ui(2*t)/(arb(2)**(2*t)*arb.fac_ui(t)**2) for t in range(n)]
        nf=[(arb(4*t+1)/2).sqrt() for t in range(n)]
        betas=[];lamk=[]
        for kk in range(81):
            sig=arb(evd[kk])*(1+arb(1e-9)); x=[arb(evecd[t,kk]) for t in range(n)]
            for it in range(14):
                x=thomas(sig,x); nr=sum(a*a for a in x).sqrt(); x=[(a/nr).mid() for a in x]
            if x[0]<0: x=[-a for a in x]
            psi0=sum(x[t]*nf[t]*P0h[t] for t in range(n)); muk=arb(2).sqrt()*x[0]/psi0
            betas.append(x); lamk.append(c/(2*pi)*muk*muk)
        K=81; Bm=arb_mat([[betas[q][t]*nf[t] for q in range(K)] for t in range(n)])
        def psirow(y):
            y=y.mid(); Pl=[arb(1),y]
            for m in range(1,2*n-1): Pl.append((((2*m+1)*y*Pl[m]-m*Pl[m-1])/(m+1)).mid())
            return [Pl[2*t] for t in range(n)]
        print('prolates',time.time()-t0,flush=True)
        a=[arb(0)]*K; k0=0
        allu_a=[u for us,wu in pieces for u in us]; allw=[w for us,wu in pieces for w in wu]
        PS=arb_mat([psirow(u/lam) for u in allu_a])*Bm
        for i,(u,w) in enumerate(zip(allu_a,allw)):
            for k in range(K): a[k]+=2*w*fv[i]*PS[i,k]/lam.sqrt()
        M=28; ys,wy=gl(240); PSg=arb_mat([psirow(y/lam/lam) for y in ys])*Bm
        B=[[arb(0)]*M for _ in range(K)]
        for r,(y,w) in enumerate(zip(ys,wy)):
            yy=y.mid(); Pq=[arb(1),yy]
            for m in range(1,2*M): Pq.append((((2*m+1)*yy*Pq[m]-m*Pq[m-1])/(m+1)).mid())
            qv=[Pq[2*i]*(arb(4*i+1)/2).sqrt() for i in range(M)]
            for k in range(K):
                for i in range(M): B[k][i]+=w/lam*PSg[r,k]*qv[i]/lam.sqrt()
        Dk=[1-l for l in lamk]
        q0=[(arb(4*i+1)/2).sqrt()*(((-1)**i)*arb.fac_ui(2*i)/(arb(2)**(2*i)*arb.fac_ui(i)**2)) for i in range(M)]
        qint=[arb(2).sqrt()/lam if i==0 else arb(0) for i in range(M)]
        int_f1=sum(w*f for w,f in zip(allw,fv)); norm_f1=sum(w*f*f for w,f in zip(allw,fv))
        H=arb_mat(M+2,M+2); rhs=arb_mat(M+2,1)
        for i in range(M):
            for j in range(M): H[i,j]=(arb(1)/lam if i==j else arb(0))+sum(B[k][i]*(Dk[k]-1)*B[k][j] for k in range(K))
            rhs[i,0]=-sum(a[k]*(Dk[k]-1)*B[k][i] for k in range(K))
            H[i,M]=q0[i];H[M,i]=q0[i];H[i,M+1]=qint[i];H[M+1,i]=qint[i]
        rhs[M,0]=0; rhs[M+1,0]=-2*int_f1
        sol=H.solve(rhs); beta=[sol[i,0] for i in range(M)]
        atot=[a[k]+sum(B[k][i]*beta[i] for i in range(M)) for k in range(K)]
        normf2=2*norm_f1+sum(b*b/lam for b in beta)
        leak=sum(atot[k]**2*Dk[k] for k in range(K))+(normf2-sum(x*x for x in atot))
        res={'beta':[b.str(70,radius=False) for b in beta],'a_k':[x.str(40,radius=False) for x in atot],
             'one_minus_lam':[d.str(20,radius=False) for d in Dk],'leak_min':leak.str(20),'norm2_f':normf2.str(30),
             'betas_prolate':[[b.str(60,radius=False) for b in bb] for bb in betas]}
        json.dump(res,open(OUT/('gauge%s.json'%os.environ.get('GTAG','')),'w')); print('gauge',res['leak_min'],res['a_k'][:3],res['beta'][:3],time.time()-t0)
    if stage=='nodes':
        G=json.load(open(OUT/('gauge%s.json'%os.environ.get('GTAG','')))); beta=[arb(b) for b in G['beta']]; M=len(beta)
        U=[];WF=[]; allu=[];allw=[]
        for m in range(1,15):
            lo=lam/(m+1); hi=lam/m; h=(hi-lo)/2; cc=(hi+lo)/2
            ph=2*math.pi*15*OMX/(m*(m+1))+1930*math.log((m+1)/m)
            nm=int(FAC*ph)+200; xs,ws=gl(nm)
            allu+=[(cc+h*x) for x in xs]; allw+=[2*w*h for w in ws]
        fv=pmap(P,f1_str,[u.str(80,radius=False) for u in allu]); print('f1 dense',len(allu),time.time()-t0,flush=True)
        U=[u.str(70,radius=False) for u in allu]; WF=[(w*arb(f)).str(70,radius=False) for w,f in zip(allw,fv)]
        nfil=int(FAC*2*math.pi*15*OMX/15)+300; ys,wy=gl(nfil)
        for y,w in zip(ys,wy):
            yy=y.mid(); Pq=[arb(1),yy]
            for mm in range(1,2*M): Pq.append((((2*mm+1)*yy*Pq[mm]-mm*Pq[mm-1])/(mm+1)).mid())
            phi=sum(beta[i]*Pq[2*i]*(arb(4*i+1)/2).sqrt() for i in range(M))
            U.append((y/lam).str(70,radius=False)); WF.append((w/lam*phi).str(70,radius=False))
        WW=[w.str(70,radius=False) for w in allw]+[(w/lam).str(70,radius=False) for w in wy]
        FF=list(fv)+[None]*len(ys)
        json.dump({'u':U,'wf':WF,'w':WW,'OMX':OMX,'FAC':FAC},open(OUT/('nodes%s.json'%os.environ.get('NTAG','')),'w')); print('nodes',len(U),time.time()-t0)
    if stage=='rho':
        OM0=float(os.environ.get('OM0','1'))
        oms=[OM0+DOM*i for i in range(int(round((OMX-OM0)/DOM))+1)]
        tag=os.environ.get('TAG','')
        ch=[[oms[i::400]] for i in range(400)]
        R=P.map(rho_chunk,ch); rv=[None]*len(oms)
        for i,r in enumerate(R):
            for k,v in enumerate(r): rv[i+k*400]=v
        json.dump({'omega0':OM0,'dom':DOM,'rho':rv},open(OUT/f'rho{tag}.json','w')); print('rho',len(oms),time.time()-t0)
    if stage=='rhosig':
        # caustic layer omega in [1,2]: grid uniform in sigma=sqrt(omega-1)
        DS=float(os.environ.get('DS','0.0005')); sig=[DS*i for i in range(int(round(1/DS))+1)]
        oms=[(arb(1)+arb(x)**2).str(60,radius=False) for x in sig]
        ch=[[oms[i::100]] for i in range(100)]
        R=P.map(rho_chunk,ch); rv=[None]*len(oms)
        for i,r in enumerate(R):
            for k,v in enumerate(r): rv[i+k*100]=v
        json.dump({'dsig':DS,'rho':rv},open(OUT/'rho_sigma.json','w')); print('rhosig',len(oms),time.time()-t0)
    if stage=='parseval':
        # leak = ||f||^2 - int_{-lam}^{lam} |Ff|^2 = ||f||^2 - 2 lam int_0^1 rho^2 d omega, both at >=256 bits
        ctx.prec=400
        nd=json.load(open(OUT/'nodes.json')); W=[arb(w) for w in nd['w']]; WF=[arb(x) for x in nd['wf']]
        nf2=sum(wf*wf/w for w,wf in zip(W,WF))
        NQ=int(os.environ.get('NQP','160')); xs,ws=gl(NQ)
        oms=[((1+x)/2).str(80,radius=False) for x in xs]
        ch=[[oms[i::20]] for i in range(20)]
        R=P.map(rho_chunk,ch); rv=[None]*NQ
        for i,r in enumerate(R):
            for k,v in enumerate(r): rv[i+k*20]=v
        ein=2*lam*sum(w/2*arb(r)**2 for w,r in zip(ws,rv))
        print('||f||^2',nf2.str(80,radius=False)); print('E_in',ein.str(80,radius=False)); print('leak',(nf2-ein).str(20))
    if stage=='check':
        oms=[float(x) for x in sys.argv[2:]]
        print(oms, rho_chunk(([*oms],)))
