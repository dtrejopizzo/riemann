# Möbius inverse of g* -> f1 on [1/λ,λ]; prolate (c=2πμ) decomposition; minimal-gauge leakage (finite family);
# exterior datum ρ*(ω)=r*(λω) on (1,∞). All in arb, 400 bits.
import json,sys,os,time,math
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
D=Path(os.environ['SP'])/'mori15'
p=int(sys.argv[1]); ctx.prec=400
E=json.load(open(D/f'p{p}_eig.json')); v=[arb(x) for x in E['vectors'][0]]
N=1664; I=list(range(p,N,2)); mu=15
L=arb(mu).log()/2; lam=arb(mu).sqrt(); pi=arb.pi(); c=2*pi*mu
norm=[(arb(2*j+1)/(2*L)).sqrt() for j in range(N)]
coef=[arb(0)]*N
for t,j in enumerate(I): coef[j]=v[t]*norm[j]
def g_at(x):
    xi=(x/L).mid(); P0,P1=arb(1),xi; s=coef[0]*P0+coef[1]*P1
    for n in range(1,N-1):
        P0,P1=P1,(((2*n+1)*xi*P1-n*P0)/(n+1)).mid(); s+=coef[n+1]*P1
    return s
def gl(n):
    xs=[];ws=[]
    for k in range(n):
        x,w=arb.legendre_p_root(n,k,weight=True); xs.append(x); ws.append(w)
    return xs,ws
t0=time.time()
out={'parity':p}
gT=g_at(L); out['g(T)']=gT.str(30); out['g(0)']=g_at(arb(0)).str(30)
# ---- Möbius inverse on pieces [λ/(m+1), λ/m]
mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]  # μ(m), m=0..15
NP=300; xs,ws=gl(NP)
pieces=[]  # (lo,hi,nodes,weights,f1 values)
for m in range(1,15):
    lo=lam/(m+1); hi=lam/m; half=(hi-lo)/2; cen=(hi+lo)/2
    us=[cen+half*x for x in xs]; wu=[w*half for w in ws]
    fv=[]
    for u in us:
        s=arb(0)
        for mm in range(1,m+1):
            if mob[mm]: s+=mob[mm]*g_at((mm*u).log())/(mm*u).sqrt()
        fv.append(s)
    pieces.append((lo,hi,us,wu,fv))
    print('piece',m,time.time()-t0,flush=True)
norm_f1=sum(sum(w*f*f for w,f in zip(wu,fv)) for _,_,_,wu,fv in pieces)
out['norm2_f1_onesided']=norm_f1.str(30)
# behaviour near 1/λ and λ: evaluate f1 at a few points
def f1_at(u):
    s=arb(0)
    for mm in range(1,16):
        if mob[mm] and mm*u<=lam: s+=mob[mm]*g_at((mm*u).log())/(mm*u).sqrt()
    return s
samp={}
for q in [1.0000001,1.001,1.01,1.05,1.1,1.2,1.5,2,3,5,8,10,12,14,14.9,14.99]:
    samp[str(q)]=f1_at(lam/arb(15)*q).str(20)  # u = q/λ
out['f1_samples(u=q/λ)']=samp
# jump sizes at breakpoints λ/m: μ(m) g(T)/√λ
out['jump_at_lam_over_m = mu(m) g(T)/sqrt(lam)']=(gT/lam.sqrt()).str(20)
# ---- prolates: even block tridiagonal (normalized Legendre), size n
n=300
diag=[];off=[]
for t in range(n):
    j=2*t
    diag.append(arb(j*(j+1))+c*c*(2*j*(j+1)-1)/((2*j+3)*(2*j-1)))
    off.append(c*c*(j+2)*(j+1)/((2*j+3)*((2*j+1)*(2*j+5))**0.5) if False else c*c*(j+2)*(j+1)/((2*j+3)*(arb((2*j+1)*(2*j+5))).sqrt()))
import numpy.linalg as la
Md=np.diag([float(x) for x in diag])+np.diag([float(x) for x in off[:-1]],1)+np.diag([float(x) for x in off[:-1]],-1)
evd,evecd=la.eigh(Md)
KMAX=160  # even k up to 160 -> 81 prolates
def thomas(sig,rhs):
    # solve (Tri - sig) x = rhs
    a=[off[t-1] for t in range(1,n)]; b=[diag[t]-sig for t in range(n)]; cc=[off[t] for t in range(n-1)]
    cp=[arb(0)]*n; dp=[arb(0)]*n
    cp[0]=cc[0]/b[0]; dp[0]=rhs[0]/b[0]
    for i in range(1,n):
        den=b[i]-a[i-1]*cp[i-1]
        cp[i]=(cc[i]/den) if i<n-1 else arb(0); dp[i]=(rhs[i]-a[i-1]*dp[i-1])/den
    x=[arb(0)]*n; x[n-1]=dp[n-1]
    for i in range(n-2,-1,-1): x[i]=dp[i]-cp[i]*x[i+1]
    return x
P0h=[]  # P_j(0) for even j
for t in range(n):
    j=2*t
    P0h.append(((-1)**t)*arb.fac_ui(j)/(arb(2)**j*arb.fac_ui(t)**2))
betas=[];chis=[];lamk=[];
for kk in range(KMAX//2+1):
    sig=arb(evd[kk])*(1+arb(1e-9)) if True else 0
    x=[arb(evecd[t,kk]) for t in range(n)]
    for it in range(14):
        x=thomas(sig,x); nr=sum(a*a for a in x).sqrt(); x=[(a/nr).mid() for a in x]
    # Rayleigh for chi
    Tx=[diag[t]*x[t]+(off[t-1]*x[t-1] if t>0 else 0)+(off[t]*x[t+1] if t<n-1 else 0) for t in range(n)]
    chi=sum(a*b for a,b in zip(x,Tx))
    if x[0]<0: x=[-a for a in x]
    psi0=sum(x[t]*(arb(2*(2*t))+1).sqrt()/arb(2).sqrt()*P0h[t] for t in range(n))  # sqrt(j+1/2) P_j(0)
    muk=arb(2).sqrt()*x[0]/psi0
    lk=c/(2*pi)*muk*muk
    betas.append(x);chis.append(chi);lamk.append(lk)
print('prolates',time.time()-t0,flush=True)
out['prolate_eigs']={str(2*kk):{'chi_ode':chis[kk].str(20),'lambda_k':lamk[kk].str(25),'1-lambda_k':(1-lamk[kk]).str(15)} for kk in range(0,12)}
out['1-lambda_k_all']=[(1-lamk[kk]).str(8) for kk in range(KMAX//2+1)]
# prolate values at nodes: psi_k(y)=Σ β_j sqrt(j+1/2) P_j(y)
def legvals_even(y):
    y=y.mid(); P=[arb(1),y]; 
    for m in range(1,2*n-1): P.append((((2*m+1)*y*P[m]-m*P[m-1])/(m+1)).mid())
    return [P[2*t]*(arb(2*(2*t))+1).sqrt()/arb(2).sqrt() for t in range(n)]
def psi_all(y):
    Pv=legvals_even(y)
    return [sum(b*pv for b,pv in zip(beta,Pv)) for beta in betas]
# projections of f1 (two-sided, even) on ψ_k^λ(u)=λ^{-1/2}ψ_k(u/λ)
K=len(betas); a=[arb(0)]*K
for lo,hi,us,wu,fv in pieces:
    for u,w,f in zip(us,wu,fv):
        pv=psi_all(u/lam)
        for k in range(K): a[k]+=2*w*f*pv[k]/lam.sqrt()
print('proj',time.time()-t0,flush=True)
# gauge family: even normalized Legendre q_i(λu), i<M, on |u|<1/λ
M=16; ys,wy=gl(200)
B=[[arb(0)]*M for _ in range(K)]; 
for y,w in zip(ys,wy):
    u=y/lam; pv=psi_all(u/lam)
    y=y.mid(); Pq=[arb(1),y]
    for m in range(1,2*M): Pq.append((((2*m+1)*y*Pq[m]-m*Pq[m-1])/(m+1)).mid())
    qv=[Pq[2*i]*(arb(4*i+1)/2).sqrt() for i in range(M)]
    for k in range(K):
        for i in range(M): B[k][i]+=w/lam*pv[k]*qv[i]/lam.sqrt()
Q=[[(arb(1)/lam if i==j else arb(0)) for j in range(M)] for i in range(M)]
Dk=[1-l for l in lamk]
# objective: leak(β)=Σ_k (a_k+Bβ)_k² D_k + [2‖f1‖² + βᵀQβ − Σ_k (a_k+Bβ)_k²]  (modes beyond K counted with weight 1)
# = const + 2 aᵀ(D−1)Bβ + βᵀ(Bᵀ(D−1)B+Q)β. Constraints: φ(0)=Σβ_i q_i(0)=0, ∫f=0: 2∫f1 + Σβ_i ∫q_i(λu)du=0.
int_f1=sum(sum(w*f for w,f in zip(wu,fv)) for _,_,_,wu,fv in pieces)
q0=[(arb(4*i+1)/2).sqrt()*(((-1)**i)*arb.fac_ui(2*i)/(arb(2)**(2*i)*arb.fac_ui(i)**2)) for i in range(M)]
qint=[arb(2).sqrt()/lam if i==0 else arb(0) for i in range(M)]
H=arb_mat(M+2,M+2); rhs=arb_mat(M+2,1)
for i in range(M):
    for j in range(M):
        H[i,j]=Q[i][j]+sum(B[k][i]*(Dk[k]-1)*B[k][j] for k in range(K))
    rhs[i,0]=-sum(a[k]*(Dk[k]-1)*B[k][i] for k in range(K))
    H[i,M]=q0[i];H[M,i]=q0[i];H[i,M+1]=qint[i];H[M+1,i]=qint[i]
rhs[M,0]=0; rhs[M+1,0]=-2*int_f1
sol=H.solve(rhs); beta=[sol[i,0] for i in range(M)]
atot=[a[k]+sum(B[k][i]*beta[i] for i in range(M)) for k in range(K)]
normf2=2*norm_f1+sum(b*b/lam for b in beta)
def leak_of(acoef,nf2):
    return sum(acoef[k]**2*Dk[k] for k in range(K))+(nf2-sum(acoef[k]**2 for k in range(K)))
leak0=leak_of(a,2*norm_f1); leakm=leak_of(atot,normf2)
out['int_f1_onesided']=int_f1.str(20); out['gauge_beta']=[b.str(15) for b in beta]
out['a_k_nogauge']=[x.str(20) for x in a[:30]]; out['a_k_mingauge']=[x.str(20) for x in atot[:30]]
out['norm2_f_total']=normf2.str(30); out['sum a_k^2 (K modes)']=sum(x*x for x in atot).str(30)
out['leak_nogauge']=leak0.str(20); out['leak_mingauge(M=16 family)']=leakm.str(20)
out['leak_terms_mingauge']=[(atot[k]**2*Dk[k]).str(10) for k in range(K)]
Qval=arb(E['rayleigh_bottom'].split('+/-')[0].strip('[ '))
out['Q(g*)']=Qval.str(20); out['kappa_emp = Q/leak_min']=(Qval/leakm).str(15)
out['Q/(1-lambda_k)']={str(2*kk):(Qval/Dk[kk]).str(10) for kk in range(6)}
sd=sum(atot[k]**2 for k in range(K) if (2*k)%4==0); ad=sum(atot[k]**2 for k in range(K) if (2*k)%4==2)
out['selfdual_mass(k≡0 mod4)']=sd.str(20); out['antiselfdual_mass(k≡2 mod4)']=ad.str(20)
out['leak_selfdual']=sum(atot[k]**2*Dk[k] for k in range(K) if (2*k)%4==0).str(12)
out['leak_antiselfdual']=sum(atot[k]**2*Dk[k] for k in range(K) if (2*k)%4==2).str(12)
print('gauge+leak',time.time()-t0,flush=True)
# exterior datum ρ(ω)=r(λω)=∫f(u)e^{-2πiλωu}du = 2∫_0^λ f(u)cos(2πλωu)du (even f), direct quadrature
def rho(om):
    s=arb(0)
    for lo,hi,us,wu,fv in pieces:
        s+=sum(w*f*(2*pi*lam*om*u).cos() for u,w,f in zip(us,wu,fv))
    s=2*s
    # gauge part (two-sided already)
    for y,w in zip(ys,wy):
        u=y/lam
        y=y.mid(); Pq=[arb(1),y]
        for m in range(1,2*M): Pq.append((((2*m+1)*y*Pq[m]-m*Pq[m-1])/(m+1)).mid())
        phi=sum(beta[i]*Pq[2*i]*(arb(4*i+1)/2).sqrt() for i in range(M))
        s+=w/lam*phi*(2*pi*lam*om*u).cos()
    return s
grid=[1+0.002*i for i in range(0,400)]+[1.8+0.01*i for i in range(0,221)]
rv=[]
for om in grid:
    rv.append(rho(arb(om)).str(12))
out['rho_grid']={'omega':grid,'rho':rv}
# prolate-series cross-check: ρ(ω)=λ^{1/2} Σ a_k (−1)^{k/2} |μ_k| ψ_k(ω)
for om in [1.0,1.05,1.2,1.5]:
    pv=psi_all(arb(om))
    val=lam.sqrt()*sum(atot[k]*((-1)**k)*(lamk[k]*2*pi/c).sqrt()*pv[k] for k in range(K))
    out[f'rho_series_check_{om}']=val.str(12)
# band interior: check ρ (=f̂) inside band at ω=0.5 (should be O(1)); and f̂(0)
out['fhat(0)']=rho(arb(0)).str(12); out['fhat(0.5λ)']=rho(arb(0.5)).str(12)
json.dump(out,open(D/f'p{p}_prolate.json','w'),indent=1)
print('done',time.time()-t0)
