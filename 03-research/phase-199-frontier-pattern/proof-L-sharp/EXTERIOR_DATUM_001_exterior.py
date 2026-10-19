# EXTERIOR_DATUM_001 step 1: ROUGH_COMPLEMENT_001_exterior.py (= TEST_BRIDGE pipeline, M=28 min-leak gauge with the two Tate
# constraints φ(0)=0, ∫f=0) run on p = g*_50 ONLY, with extra columns that decompose its exterior datum ρ_p:
#  'p' full; 'filler' inner gauge part alone; 'pro04' = ã0ψ0+ã4ψ4 (ã = p's own prolate coefficients, = 1.106/−1.822) on all of
#  [−λ,λ]; 'pro8+' = Σ_{8≤k≤56} ã_kψ_k; 'pro_inner' = full prolate part restricted to |u|<1/λ; 'filler_free' = min-leak filler
#  WITHOUT the Tate constraints; plus node values for the jump analysis. Output ed1/exterior_decomp.json.
# ROUGH_COMPLEMENT_001 step 2: TEST_BRIDGE_001_exterior.py unchanged except input/output paths (vectors δ, p from rc/pvecs.pkl).
# TEST_BRIDGE_001 step 3: exterior data ρ_h(ω) = r_h(λω) (ω ≥ 1) of Legendre vectors h (g* and the edge vectors p_J),
# through the MORI15 pipeline: Möbius inverse f1 on [1/λ,λ] (MECH Prop 3.1), minimal-leak gauge (M=28 even Legendre family on
# |u|<1/λ, constraints φ(0)=0, ∫f=0) = Π within the family (U_001 Thm U.2.1), direct Fourier quadrature, arb.
# Linear in h, so v* = g* − f*(λ)p_J is assembled afterwards. Output: ω-grid, ρ values (strings), leaks.
import json,sys,os,time,pickle,math
from pathlib import Path
from flint import arb,arb_mat,ctx
SP=Path(os.environ['SP']); OUT=SP/'tb'; DATA=Path(__file__).parent/'MORI15_EXTREMAL_001_data'
ctx.prec=400
OMX=float(os.environ.get('OMX','24')); NP=int(os.environ.get('NP','500')); DOM=float(os.environ.get('DOM','0.002'))
Js=['p']
t0=time.time()
mu=15; N=1664; I=list(range(0,N,2)); d=len(I)
L=arb(mu).log()/2; lam=arb(mu).sqrt(); pi=arb.pi(); c=2*pi*mu
E=json.load(open(DATA/'p0_eig.json')); PV=pickle.load(open(SP/'rc'/'pvecs.pkl','rb')); OUT=SP/'ed1'
vecs=[[arb(x) for x in PV['pvecs']['p']]]
names=['p']; nv=1
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
# unconstrained min-leak filler (drop the two Tate rows)
Hf=arb_mat(M,M); rf=arb_mat(M,1)
for i in range(M):
    for j in range(M): Hf[i,j]=H[i,j]
    rf[i,0]=rhs[i,0]
solf=Hf.solve(rf)
res['tate_multipliers']=[sol[M,0].str(20),sol[M+1,0].str(20)]
# p's edge and jump data: p(T) and f1 just inside/outside the Möbius points λ/m
pT=sum(Cm[j,0] for j in range(N)); res['p(T)']=pT.str(25)
ctx.prec=240
om=[1+DOM*i for i in range(int((OMX-1)/DOM)+1)]
ak=[atot[k][0] for k in range(K)]
nodes=[];wts=[]
cols=['p','inner_res','pro04','pro8+','tate_shift']   # inner_res = filler − (all-k prolate part) on |u|<1/λ; tate_shift = unconstrained − constrained filler
outer_u=[u for lo,hi,us,wu,fv in pieces for u in us]
PSo=psimat([u/lam for u in outer_u]); idx=0
for lo,hi,us,wu,fv in pieces:
    for u,w,f in zip(us,wu,fv):
        p04=(ak[0]*PSo[idx,0]+ak[2]*PSo[idx,2])/lam.sqrt(); p8=sum(ak[k]*PSo[idx,k] for k in range(4,29,2))/lam.sqrt()
        nodes.append(u); wts.append([2*w*f[0],arb(0),2*w*p04,2*w*p8,arb(0)]); idx+=1
PSi=psimat([y/lam/lam for y in ys])
for r,(y,w) in enumerate(zip(ys,wy)):
    u=y/lam; phi=sum(sol[i,0]*QV[r][i] for i in range(M)); phf=sum(solf[i,0]*QV[r][i] for i in range(M))
    p04=(ak[0]*PSi[r,0]+ak[2]*PSi[r,2])/lam.sqrt(); p8=sum(ak[k]*PSi[r,k] for k in range(4,29,2))/lam.sqrt()
    pin=sum(ak[k]*PSi[r,k] for k in range(K))/lam.sqrt()
    # NB filler φ is the function value itself (pipeline weight w/λ·φ); prolate value ψ^λ = PS/√λ
    nodes.append(u); wts.append([w/lam*phi,w/lam*(phi-pin),w/lam*p04,w/lam*p8,w/lam*(phf-phi)])
# junction values at u=1/λ: filler vs f1 (outer, extrapolated by the last piece's interpolant is avoided: evaluate f1 directly)
def f1at(u):
    s=arb(0)
    for mm in range(1,15):
        if mob[mm] and mm*u<lam: s+=mob[mm]/(mm*u).sqrt()*gvals([(mm*u).log()])[0,0]
    return s
ui=1/lam; yi=arb(1)
Pq=[arb(1),yi]
for m in range(1,2*M): Pq.append((((2*m+1)*yi*Pq[m]-m*Pq[m-1])/(m+1)))
qv1=[Pq[2*i]*(arb(4*i+1)/2).sqrt() for i in range(M)]
res['filler(1/λ−)']=(sum(sol[i,0]*qv1[i] for i in range(M))/lam.sqrt()).str(20)  # NB: the filler value is φ itself (no λ^{-1/2}); the analysis multiplies back by √λ
res['filler_free(1/λ−)']=(sum(solf[i,0]*qv1[i] for i in range(M))/lam.sqrt()).str(20)
res['f1(1/λ+)']=f1at(ui*(1+arb(1e-30))).str(20)
eps=arb(10)**-25
res['jumps_lam_over_m']={m:[f1at(lam/m*(1-eps)).str(20),f1at(lam/m*(1+eps)).str(20)] for m in range(1,15)}
PSe=psimat([arb(1),1/lam/lam])
res['pro_all(λ)']=(sum(ak[k]*PSe[0,k] for k in range(K))/lam.sqrt()).str(20)
res['pro_all(1/λ)']=(sum(ak[k]*PSe[1,k] for k in range(K))/lam.sqrt()).str(20)
res['pro04(λ)']=((ak[0]*PSe[0,0]+ak[2]*PSe[0,2])/lam.sqrt()).str(20)
print(json.dumps({k:v for k,v in res.items() if k not in ('leak_bilinear','a_k','one_minus_lam')}),flush=True)
Wm=arb_mat(wts); twopilam=2*pi*lam
rows=[]
for o in om:
    rows.append([(twopilam*arb(o)*u).cos() for u in nodes])
    if len(rows)==500 or o==om[-1]:
        R=arb_mat(rows)*Wm
        res.setdefault('rho',[]).extend([[R[i,q].mid().str(25,radius=False) for q in range(len(cols))] for i in range(R.nrows())])
        rows=[]; print('omega',o,time.time()-t0,flush=True)
res['omega']=om; res['cols']=cols
json.dump(res,open(OUT/f'exterior_decomp_v2_OMX{int(OMX)}_NP{NP}.json','w'))
print('done',time.time()-t0)
