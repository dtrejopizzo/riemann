"""
FASE 3: preservacion monotona de Hermite-Biehler.
A_lambda >=0 <=> E_lambda HB; kappa(P)=#autovalores<0 de A^{(p<=P)} mide no-HB-ness (kappa=0<=>HB).
Escalera FINA kappa(P) primo por primo: que primos rompen HB (kappa sube) y cuales la restauran.
Hipotesis: existe P* tal que para P>P* el sanado es MONOTONO (kappa solo baja) -> lema nuevo.
A^{(P)} = P_pole - R_arch - Q_{primos<=P}.  (intermedio; el exacto es P=lambda^2)
"""
import mpmath as mp
mp.mp.dps = 35
GAMMA=mp.euler; LOG4PI=mp.log(4*mp.pi)
def q_kernel(m,n,L):
    if m==n: return lambda u: 2*(1-u/L)*mp.cos(2*mp.pi*n*u/L)
    c=1/(mp.pi*(n-m)); return lambda u:(mp.sin(2*mp.pi*m*u/L)-mp.sin(2*mp.pi*n*u/L))*c
def vm_zeta(mx):
    L=[mp.mpf(0)]*(mx+1); sv=[True]*(mx+1)
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pw=p
            while pw<=mx: L[pw]=lp; pw*=p
    return L
def pieces(lam_str,N):
    lam=mp.mpf(lam_str); L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1)); mx=int(lam*lam)
    Lam=vm_zeta(mx); C=LOG4PI+GAMMA; half=mp.mpf('1')/2
    PR=mp.zeros(dim)   # P_pole - R_arch
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); q0=q(mp.mpf(0))
            def ig(u):
                if u<mp.mpf('1e-12'):
                    h=mp.mpf('1e-8'); return ((q(h)-q0)/h+half*q0)/2
                return (mp.e**(u/2)*q(u)-q0)/(2*mp.sinh(u))
            R=C*q0/2+mp.quad(ig,[0,L])+q0*mp.log(mp.tanh(L/2))/2
            P=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L])
            PR[a,b]=P-R; PR[b,a]=P-R
    def Qp_single(p):  # forma de un solo primo p (todas sus potencias <=mx)
        Q=mp.zeros(dim)
        for a in range(dim):
            for b in range(a,dim):
                q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0); pw=p
                while pw<=mx:
                    if Lam[pw]!=0: s+=Lam[pw]*(mp.mpf(pw)**mp.mpf('-0.5'))*q(mp.log(pw))
                    pw*=p
                Q[a,b]=s; Q[b,a]=s
        return Q
    primes=[p for p in range(2,mx+1) if Lam[p]!=0 and all(p%d for d in range(2,int(p**0.5)+1))]
    return PR,{p:Qp_single(p) for p in primes},primes,L
def kappa(M):
    E,_=mp.eigsy(M); return sum(1 for i in range(M.rows) if E[i]<-mp.mpf('1e-16'))

for lam,N in [('7.0',12),('9.0',14)]:
    PR,Qps,primes,L=pieces(lam,N)
    print(f"\nlambda={lam} N={N} L={mp.nstr(L,4)}  primos: {primes}")
    acc=PR.copy(); print(f"  P_pole - R_arch (sin primos): kappa={kappa(acc)}")
    seq=[]
    prevk=kappa(acc)
    for p in primes:
        acc=acc-Qps[p]; k=kappa(acc); arrow='UP ' if k>prevk else ('dn ' if k<prevk else '== ')
        seq.append(k); print(f"  + primo {p:2d} (log p={mp.nstr(mp.log(p),3)}): kappa={k}  {arrow}{'<-rompe HB' if k>prevk else ('<-restaura' if k<prevk else '')}")
        prevk=k
    # detectar P* (monotonia final)
    peak=max(range(len(seq)),key=lambda i:seq[i])
    mono_tail=all(seq[i]>=seq[i+1] for i in range(peak,len(seq)-1))
    print(f"  pico en primo {primes[peak]} (kappa={seq[peak]}); cola post-pico monotona-decreciente? {mono_tail}")
    print(f"  final kappa={seq[-1]} (=0 <=> HB <=> RH a esta lambda)")
