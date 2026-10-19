# Evaluate the pieces of Mori's form Q = W_T (with pole) on the bottom Galerkin vector v* (parity p), in arb.
# Conventions: L = ½ log 15, basis φ_j = sqrt((2j+1)/(2L)) P_j(x/L); g(x) = Σ v_j φ_j(x);
# Q(g) = (1/π)∫_0^∞ a(t)|Fg(t)|² dt + 2(∫g cosh(x/2))² − 2(∫g sinh(x/2))² − 2Σ_{n<μ} Λ(n)n^{-1/2} c_g(log n),
# c_g(a) = ∫ g(x) g(x+a) dx,  a(t) = Re ψ(¼+it/2) − log π.
import json,sys,os,time,math
from pathlib import Path
from flint import arb,acb,arb_mat,ctx
D=Path(os.environ['SP'])/'mori15'
p=int(sys.argv[1]); ctx.prec=420
E=json.load(open(D/f'p{p}_eig.json')); v=[arb(x) for x in E['vectors'][0]]
N=1664; d=len(v); I=list(range(p,N,2)); mu=15
L=arb(mu).log()/2; gam=arb(74)/16
norm=[(arb(2*j+1)/(2*L)).sqrt() for j in range(N)]
coef=[arb(0)]*N
for t,j in enumerate(I): coef[j]=v[t]*norm[j]
def g_at(x):
    xi=(x/L).mid(); P0,P1=arb(1),xi; s=coef[0]*P0+coef[1]*P1
    for n in range(1,N-1):
        P0,P1=P1,(((2*n+1)*xi*P1-n*P0)/(n+1)).mid(); s+=coef[n+1]*P1
    return s
NQ=1700
xs=[];ws=[]
for k in range(NQ):
    x,w=arb.legendre_p_root(NQ,k,weight=True); xs.append(x); ws.append(w)
def integrate(lo,hi,fn):
    half=(hi-lo)/2;cen=(hi+lo)/2
    return sum(w*fn(cen+half*x) for x,w in zip(xs,ws))*half
t0=time.time()
# g on the standard nodes
gx=[g_at(L*x) for x in xs]; print('g eval',time.time()-t0,flush=True)
norm2=sum(w*gg*gg for w,gg in zip(ws,gx))*L
Ac=sum(w*gg*(L*x/2).cosh() for x,w,gg in zip(xs,ws,gx))*L
As=sum(w*gg*(L*x/2).sinh() for x,w,gg in zip(xs,ws,gx))*L
pole=2*Ac*Ac-2*As*As
out={'parity':p,'norm2':norm2.str(40),'A_cosh':Ac.str(40),'A_sinh':As.str(40),'pole':pole.str(40),
     'A_plus':(Ac+As).str(40),'B_minus':(Ac-As).str(40)}
# correlation at lag a (0<=a<2L): ∫_{-L}^{L-a} g(x) g(x+a) dx
def corr(a):
    if a>=2*L: return arb(0)
    return integrate(-L,L-a,lambda x:g_at(x)*g_at(x+a))
vm={2:2,3:3,4:2,5:5,7:7,8:2,9:3,11:11,13:13}
prime_terms={}; tot=arb(0)
for n,pp in vm.items():
    c=corr(arb(n).log()); wn=2*arb(pp).log()/arb(n).sqrt(); prime_terms[n]={'c_g(log n)':c.str(40),'weight 2Λ/√n':wn.str(20),'term':(wn*c).str(40)}
    tot+=wn*c; print('prime',n,time.time()-t0,flush=True)
out['prime_terms']=prime_terms; out['prime_total']=tot.str(50)
# ratio lags
lags={}
for m in range(1,16):
    for n in range(1,m):
        if math.gcd(m,n)==1 and math.log(m/n)<2*float(L):
            lags[f'{m}/{n}']=corr(arb(m).log()-arb(n).log()).str(30)
out['corr_ratio_lags']=lags; out['corr_0']=norm2.str(40)
print('lags',time.time()-t0,flush=True)
# matrices on v
A=json.load(open(D/f'p{p}_A_mid.json')); J=json.load(open(D/f'p{p}_J_mid.json'))
vA=sum(v[i]*sum(arb(A[i][j])*v[j] for j in range(d)) for i in range(d))
vJ=sum(v[i]*sum(arb(J[i][j])*v[j] for j in range(d)) for i in range(d))
out['vAv']=vA.str(60); out['vJv']=vJ.str(60); out['Q=v(A+J)v']=(vA+vJ).str(60)
out['prime_from_A (gamma*norm2 - vAv)']=(gam*norm2-vA).str(60)
out['archOmega_from_J (vJv - pole + gamma*norm2)']=(vJ-pole+gam*norm2).str(60)
# Fourier transform on t-panels, archimedean integrals
ends=[0,0.5]+[2**k for k in range(0,7)]+list(range(128,736,64))+[736]+[800,1000,1500,2000,3000]
nq=224; txs=[];tws=[]
for k in range(nq):
    x,w=arb.legendre_p_root(nq,k,weight=True); txs.append(x); tws.append(w)
cosx=None
arch=arb(0);atil=arb(0);pole_int=arb(0);energy=arb(0);archtail=arb(0); panels=[]
lpi=arb.pi().log()
for lo,hi in zip(ends,ends[1:]):
    lo=arb(lo);hi=arb(hi);half=(hi-lo)/2;cen=(hi+lo)/2; pa=arb(0);pe=arb(0)
    for xt,wt in zip(txs,tws):
        t=cen+half*xt
        if p==0: F=sum(w*gg*(L*x*t).cos() for x,w,gg in zip(xs,ws,gx))*L
        else:    F=sum(w*gg*(L*x*t).sin() for x,w,gg in zip(xs,ws,gx))*L
        F2=F*F; z=acb(arb(1)/4,t/2); a=z.digamma().real-lpi; at=(z+1).digamma().real-lpi
        wgt=wt*half/arb.pi()
        pa+=wgt*a*F2; pe+=wgt*F2; atil+=wgt*at*F2; pole_int+=wgt*F2/(arb(1)/4+t*t)
    panels.append({'t':[float(lo),float(hi)],'arch':pa.str(15),'energy':pe.str(15)})
    if float(hi)<=736: arch+=pa
    else: archtail+=pa
    energy+=pe
    print('panel',float(lo),float(hi),time.time()-t0,flush=True)
out['panels']=panels
out['arch_Omega_direct']=arch.str(50); out['arch_tail_beyond_Omega']=archtail.str(20); out['energy_total(≈norm2)']=energy.str(40)
out['atilde_form']=atil.str(50); out['int exp(-|a|/2)c_g = (1/2π)∫|F|²/(1/4+t²)']=pole_int.str(50)
out['cheb_main 2∫_1^μ t^{-1/2}c_g(log t)dt = pole - that']=(pole-pole_int).str(50)
out['R_Lambda = prime_total - cheb_main']=(tot-(pole-pole_int)).str(50)
out['Q_from_pieces = arch+tail+pole-prime']=(arch+archtail+pole-tot).str(50)
json.dump(out,open(D/f'p{p}_pieces.json','w'),indent=1)
print('done',time.time()-t0)
