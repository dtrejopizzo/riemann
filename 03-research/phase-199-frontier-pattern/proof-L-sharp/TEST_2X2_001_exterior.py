# TEST_2X2_001 step 2: ROUGH_COMPLEMENT_001_exterior.py (= TEST_BRIDGE_001 pipeline) unchanged except input/output paths:
# vectors p_J, δ_J (J = 1,2,3,5,10,20,50) from t2x2_pvecs.pkl (written by TEST_2X2_001_galerkin.py).
# through the MORI15 pipeline: Möbius inverse f1 on [1/λ,λ] (MECH Prop 3.1), minimal-leak gauge (M=28 even Legendre family on
# |u|<1/λ, constraints φ(0)=0, ∫f=0) = Π within the family (U_001 Thm U.2.1), direct Fourier quadrature, arb.
# Linear in h, so v* = g* − f*(λ)p_J is assembled afterwards. Output: ω-grid, ρ values (strings), leaks.
import json,sys,os,time,pickle,math
from pathlib import Path
from flint import arb,arb_mat,ctx
SP=Path(os.environ['SP']); OUT=SP/'tb'; DATA=Path(__file__).parent/'MORI15_EXTREMAL_001_data'
ctx.prec=400
OMX=float(os.environ.get('OMX','24')); NP=int(os.environ.get('NP','500')); DOM=float(os.environ.get('DOM','0.002'))
Js=[(x if not x.isdigit() else int(x)) for x in os.environ.get('JS','1,3,12,glob').split(',')]
t0=time.time()
mu=15; N=1664; I=list(range(0,N,2)); d=len(I)
L=arb(mu).log()/2; lam=arb(mu).sqrt(); pi=arb.pi(); c=2*pi*mu
E=json.load(open(DATA/'p0_eig.json')); PV=pickle.load(open(SP/'t2x2_pvecs.pkl','rb')); OUT=SP/'t2x2'; OUT.mkdir(exist_ok=True)
vecs=[[arb(x) for x in E['vectors'][0]]]+[[arb(x) for x in PV['pvecs'][J]] for J in Js]
names=['g*']+[f'v_{J}' for J in Js]; nv=len(vecs)
Cm=arb_mat(N,nv)   # monomial-free: coefficients of P_j(x/L)
for q,v in enumerate(vecs):
    for t,j in enumerate(I): Cm[j,q]=v[t]*(arb(2*j+1)/(2*L)).sqrt()
def gvals(xs):
    rows=[]
    for x in xs:
        xi=(x/L).mid(); P0,P1=arb(1),xi; row=[P0,P1]
        for n in range(1,N-1):
            P0,P1=P1,(((2*n+1)*xi*P1-n*P0)/(n+1)).mid(); row.append(P1)
        rows.append(row)
    return arb_mat(rows)*Cm
def gl(n):
    xs=[];ws=[]
    for k in range(n):
        x,w=arb.legendre_p_root(n,k,weight=True); xs.append(x); ws.append(w)
    return xs,ws
mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]
xs,ws=gl(NP)
pieces=[]
for m in range(1,15):
    lo=lam/(m+1); hi=lam/m; half=(hi-lo)/2; cen=(hi+lo)/2
    us=[cen+half*x for x in xs]; wu=[w*half for w in ws]
    pts=[];own=[]
    for qi,u in enumerate(us):
        for mm in range(1,m+1):
            if mob[mm]: pts.append((mm*u).log()); own.append((qi,mm,u))
    GV=gvals(pts)
    fv=[[arb(0)]*nv for _ in us]
    for r,(qi,mm,u) in enumerate(own):
        s=mob[mm]/(mm*u).sqrt()
        for q in range(nv): fv[qi][q]+=s*GV[r,q]
    pieces.append((lo,hi,us,wu,fv)); print('piece',m,time.time()-t0,flush=True)
# prolates (81 even, as MORI15) for the gauge least squares
n=300
diag=[];off=[]
for t in range(n):
    j=2*t
    diag.append(arb(j*(j+1))+c*c*(2*j*(j+1)-1)/((2*j+3)*(2*j-1)))
    off.append(c*c*(j+2)*(j+1)/((2*j+3)*(arb((2*j+1)*(2*j+5))).sqrt()))
import numpy as np
Md=np.diag([float(x) for x in diag])+np.diag([float(x) for x in off[:-1]],1)+np.diag([float(x) for x in off[:-1]],-1)
evd,evecd=np.linalg.eigh(Md)
def thomas(sig,rhs):
    a=[off[t-1] for t in range(1,n)]; b=[diag[t]-sig for t in range(n)]; cc=[off[t] for t in range(n-1)]
    cp=[arb(0)]*n; dp=[arb(0)]*n
    cp[0]=cc[0]/b[0]; dp[0]=rhs[0]/b[0]
    for i in range(1,n):
        den=b[i]-a[i-1]*cp[i-1]
        cp[i]=(cc[i]/den) if i<n-1 else arb(0); dp[i]=(rhs[i]-a[i-1]*dp[i-1])/den
    x=[arb(0)]*n; x[n-1]=dp[n-1]
    for i in range(n-2,-1,-1): x[i]=dp[i]-cp[i]*x[i+1]
    return x
P0h=[((-1)**t)*arb.fac_ui(2*t)/(arb(2)**(2*t)*arb.fac_ui(t)**2) for t in range(n)]
nf=[(arb(4*t+1)/2).sqrt() for t in range(n)]
KMAX=160; betas=[];lamk=[]
for kk in range(KMAX//2+1):
    sig=arb(evd[kk])*(1+arb(1e-9)); x=[arb(evecd[t,kk]) for t in range(n)]
    for it in range(14):
        x=thomas(sig,x); nr=sum(a*a for a in x).sqrt(); x=[(a/nr).mid() for a in x]
    if x[0]<0: x=[-a for a in x]
    psi0=sum(x[t]*nf[t]*P0h[t] for t in range(n)); muk=arb(2).sqrt()*x[0]/psi0
    betas.append(x); lamk.append(c/(2*pi)*muk*muk)
K=len(betas); Bm=arb_mat([[betas[q][t]*nf[t] for q in range(K)] for t in range(n)])
def psimat(ys):
    rows=[]
    for y in ys:
        y=y.mid(); P=[arb(1),y]
        for m in range(1,2*n-1): P.append((((2*m+1)*y*P[m]-m*P[m-1])/(m+1)).mid())
        rows.append([P[2*t] for t in range(n)])
    return arb_mat(rows)*Bm
a=[[arb(0)]*nv for _ in range(K)]
for lo,hi,us,wu,fv in pieces:
    PS=psimat([u/lam for u in us])
    for i,(u,w) in enumerate(zip(us,wu)):
        for k in range(K):
            s=2*w*PS[i,k]/lam.sqrt()
            for q in range(nv): a[k][q]+=s*fv[i][q]
print('proj',time.time()-t0,flush=True)
M=28; ys,wy=gl(240)
PSg=psimat([y/lam/lam for y in ys])
B=[[arb(0)]*M for _ in range(K)]; QV=[]
for r,(y,w) in enumerate(zip(ys,wy)):
    yy=y.mid(); Pq=[arb(1),yy]
    for m in range(1,2*M): Pq.append((((2*m+1)*yy*Pq[m]-m*Pq[m-1])/(m+1)).mid())
    qv=[Pq[2*i]*(arb(4*i+1)/2).sqrt() for i in range(M)]; QV.append(qv)
    for k in range(K):
        for i in range(M): B[k][i]+=w/lam*PSg[r,k]*qv[i]/lam.sqrt()
Dk=[1-l for l in lamk]
q0=[(arb(4*i+1)/2).sqrt()*(((-1)**i)*arb.fac_ui(2*i)/(arb(2)**(2*i)*arb.fac_ui(i)**2)) for i in range(M)]
qint=[arb(2).sqrt()/lam if i==0 else arb(0) for i in range(M)]
H=arb_mat(M+2,M+2)
for i in range(M):
    for j in range(M):
        H[i,j]=(arb(1)/lam if i==j else arb(0))+sum(B[k][i]*(Dk[k]-1)*B[k][j] for k in range(K))
    H[i,M]=q0[i];H[M,i]=q0[i];H[i,M+1]=qint[i];H[M+1,i]=qint[i]
rhs=arb_mat(M+2,nv); res={'names':names,'Js':Js}
for q in range(nv):
    int_f1=sum(sum(w*f[q] for w,f in zip(wu,fv)) for _,_,_,wu,fv in pieces)
    for i in range(M): rhs[i,q]=-sum(a[k][q]*(Dk[k]-1)*B[k][i] for k in range(K))
    rhs[M,q]=0; rhs[M+1,q]=-2*int_f1
sol=H.solve(rhs)
# full quadratic leak functional (bilinear) for later recombination: leak(h) = Σ_k ã_k² D_k + (‖f‖² − Σ ã_k²)
atot=[[a[k][q]+sum(B[k][i]*sol[i,q] for i in range(M)) for q in range(nv)] for k in range(K)]
nf1=[[sum(sum(w*f[p]*f[q] for w,f in zip(wu,fv)) for _,_,_,wu,fv in pieces) for q in range(nv)] for p in range(nv)]
LK=[[ (2*nf1[p][q]+sum(sol[i,p]*sol[i,q] for i in range(M))/lam
      +sum(atot[k][p]*atot[k][q]*(Dk[k]-1) for k in range(K))).str(30) for q in range(nv)] for p in range(nv)]
res['leak_bilinear']=LK
res['a_k']=[[atot[k][q].str(25) for q in range(nv)] for k in range(K)]
res['one_minus_lam']=[x.str(15) for x in Dk]
print('gauge',time.time()-t0,flush=True)
# exterior datum on ω-grid, prec 220 suffices (|integrand| ≤ O(1), target 1e-45 absolute)
ctx.prec=240
om=[1+DOM*i for i in range(int((OMX-1)/DOM)+1)]
nodes=[];wts=[]
for lo,hi,us,wu,fv in pieces:
    for u,w,f in zip(us,wu,fv): nodes.append(u); wts.append([2*w*f[q] for q in range(nv)])
for r,(y,w) in enumerate(zip(ys,wy)):
    u=y/lam; phi=[sum(sol[i,q]*QV[r][i] for i in range(M)) for q in range(nv)]
    nodes.append(u); wts.append([w/lam*phi[q] for q in range(nv)])
Wm=arb_mat(wts); twopilam=2*pi*lam
rows=[]
for o in om:
    rows.append([(twopilam*arb(o)*u).cos() for u in nodes])
    if len(rows)==500 or o==om[-1]:
        R=arb_mat(rows)*Wm
        res.setdefault('rho',[]).extend([[R[i,q].mid().str(25,radius=False) for q in range(nv)] for i in range(R.nrows())])
        rows=[]; print('omega',o,time.time()-t0,flush=True)
res['omega']=om
json.dump(res,open(OUT/f'exterior_OMX{int(OMX)}_NP{NP}.json','w'))
print('done',time.time()-t0)
