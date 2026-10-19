# Phase 205, Piece 5: compressions of 𝔪 (archimedean) and of the comb in the Dirichlet sine basis s_k(x)=sin(πk(x+T)/2T), k=1..N.
# mpmath dps 40. 𝔪 = (C0+κ_T)·c(0) + ∫_0^{2T}(c(0)−c(u))K(u)du  (P47 eq:Aform, Lévy);  C = −Σ_{log n<2T} v_n c(log n), v_n=2Λ_X(n)/√n.
# Symmetrized c_{kk'}(u), c_{kk'}(u)=∫_{−T}^{T−u}s_k(x)s_{k'}(x+u)dx  — CLOSED FORM (a=πk/2T, b=πk'/2T, L=2T−u):
#   a≠b: ½[(sin((a−b)L−bu)+sin(bu))/(a−b) − (sin((a+b)L+bu)−sin(bu))/(a+b)]
#   a=b: ½[L cos(bu) − (sin(2bL+bu)−sin(bu))/(2b)]
# Toeplitz−Hankel reading: term (a−b) (Toeplitz, frequency difference) − term (a+b) (Hankel). NUMERICAL.
import mpmath as mp, json, sys
from fractions import Fraction as Fr
from multiprocessing import Pool
mp.mp.dps=40
LQ=json.load(open('/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/LEMMA_E_EPSTEIN_001_data/lambdaQ_exact.json'))
def Lam(n):
    from sympy import factorint
    f=factorint(n); return mp.log(list(f)[0]) if len(f)==1 else mp.mpf(0)
def LamQ(n):
    d=LQ.get(str(n)); return mp.fsum(mp.mpf(Fr(q).numerator)/Fr(q).denominator*mp.log(int(p)) for p,q in d.items()) if d else mp.mpf(0)
def LamP2(n):
    from sympy import factorint
    f=factorint(n); return mp.log(list(f)[0]) if len(f)==1 and list(f)[0]!=2 else mp.mpf(0)
ARCH={'zeta':(mp.digamma(0.25)-mp.log(mp.pi),lambda u:1/(2*mp.sinh(u/2))+1/(2*mp.cosh(u/2)),lambda T:mp.log(mp.coth(T/2))+2*mp.atan(mp.exp(-T))),
      'epstein':(mp.log(20)-2*mp.euler-6*mp.log(2)-2*mp.log(mp.pi),lambda u:1/mp.sinh(u/2),lambda T:2*mp.log(mp.coth(T/2)))}
COMB={'zeta':('zeta',Lam),'epstein':('epstein',LamQ),'aP2':('zeta',LamP2)}
def cfun(k,kp,u,T):
    a=mp.pi*k/(2*T); b=mp.pi*kp/(2*T); L=2*T-u
    if k==kp: return (L*mp.cos(b*u)-(mp.sin(2*b*L+b*u)-mp.sin(b*u))/(2*b))/2
    return ((mp.sin((a-b)*L-b*u)+mp.sin(b*u))/(a-b)-(mp.sin((a+b)*L+b*u)-mp.sin(b*u))/(a+b))/2
def csym(k,kp,u,T): return (cfun(k,kp,u,T)+cfun(kp,k,u,T))/2
def run(args):
    key,Ts,T,N=args; mp.mp.dps=40; archname,lam=COMB[key]; C0,K,tail=ARCH[archname]
    ks=list(range(1,N+1)); n=len(ks); c0=mp.matrix(n,n)
    for i,k in enumerate(ks): c0[i,i]=T
    Mm=c0*(C0+tail(T))
    xs,ws=mp.gauss_legendre_nodes(60) if hasattr(mp,'gauss_legendre_nodes') else (None,None)
    import numpy as np
    gx,gw=np.polynomial.legendre.leggauss(int(__import__("os").environ.get("NGL","60")))
    panels=[(0,T/8),(T/8,T/2),(T/2,T),(T,3*T/2),(3*T/2,2*T)]
    for lo,hi in panels:
        lo=mp.mpf(lo);hi=mp.mpf(hi)
        for x,w in zip(gx,gw):
            u=(lo+hi)/2+(hi-lo)/2*mp.mpf(x); wu=mp.mpf(w)*(hi-lo)/2*K(u)
            for i,k in enumerate(ks):
                for j in range(i,n):
                    v=(c0[i,j]-csym(k,ks[j],u,T))*wu; Mm[i,j]+=v
                    if j!=i: Mm[j,i]+=v
    Cm=mp.matrix(n,n); m=2
    while mp.log(m)<2*T:
        L_=lam(m)
        if L_!=0:
            vn=2*L_/mp.sqrt(m)
            for i,k in enumerate(ks):
                for j in range(n): Cm[i,j]-=vn*csym(k,ks[j],mp.log(m),T)
        m+=1
    # quadrature check of the closed form at one entry
    chk=None
    if n>=3:
        u0=mp.log(2) if mp.log(2)<2*T else T/2
        num=mp.quad(lambda x: mp.sin(mp.pi*1*(x+T)/(2*T))*mp.sin(mp.pi*3*(x+u0+T)/(2*T)),[-T,T-u0])
        chk=mp.nstr(abs(num-cfun(1,3,u0,T))/abs(num),5)
    chi=[mp.quad(lambda x: mp.cosh(x/2)*mp.sin(mp.pi*k*(x+T)/(2*T)),[-T,T])/mp.sqrt(T) for k in ks]
    res={'family':key,'T':Ts,'N':N,'closedform_relerr':chk}
    for sec,idx in (('ev',[i for i,k in enumerate(ks) if k%2==1]),('odd',[i for i,k in enumerate(ks) if k%2==0]),('all',list(range(n)))):
        if not idx: continue
        sub=lambda Mx: mp.matrix([[Mx[i,j]/T for j in idx] for i in idx])  # orthonormal basis s_k/√T
        Ms=sub(Mm); As=sub(Mm+Cm)
        Em,_=mp.eigsy(Ms); Ea,Va=mp.eigsy(As)
        d={'n-_m':sum(1 for e in Em if e<0),'n-_A':sum(1 for e in Ea if e<0),'eigmin_A':mp.nstr(min(Ea),12),
           'eigs_A_neg':[mp.nstr(e,8) for e in Ea if e<0],'eigs_m_neg':[mp.nstr(e,6) for e in Em if e<0]}
        if sec=='ev':
            p=mp.matrix([chi[i] for i in idx]); imin=min(range(len(Ea)),key=lambda t:Ea[t]); v=Va[:,imin]
            d['cos(v_min,chi_ev)']=mp.nstr(abs(sum(v[t]*p[t] for t in range(len(idx))))/mp.norm(p),10)
            d['v_min']=[mp.nstr(v[t],6) for t in range(len(idx))]
        res[sec]=d
    print(json.dumps({k:v for k,v in res.items()}),flush=True); return res
if __name__=='__main__':
    t0=mp.mpf('6.28983598883690')
    Tlist=[('1/2log3',mp.log(3)/2),('1',mp.mpf(1)),('1/2log5',mp.log(5)/2),('1/2log15',mp.log(15)/2),('2',mp.mpf(2)),('3',mp.mpf(3))]
    jobs=[]
    for Ts,T in Tlist:
        NT=int(mp.ceil(2*T*t0/mp.pi))-1
        for mult in (1,2,4):
            for key in ('zeta','epstein','aP2'): jobs.append((key,Ts,T,NT*mult))
    jobs.sort(key=lambda j:-j[3])
    with Pool(20) as P: R=P.map(run,jobs)
    json.dump(R,open('P205_sine_compressions.json','w'),indent=1)
