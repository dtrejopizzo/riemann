"""
(a) Teorema del cono amplio (monotonia de kappa) + (E) Maslov/flujo espectral.
kappa(P)=#autovalores<0 de A^{(P)}=P-R-Q_{p<=P}. Agregar primo p: A->A-Q_p.
Delta-kappa = flujo espectral (autovalores que cruzan 0) en ese paso.
Tesis: para p>pico (~lambda), el flujo es unidireccional (kappa solo baja) -> cono amplio.
Computo: por primo, (signatura de Q_p), Delta-kappa, y correlacion con log p vs L/2.
"""
import mpmath as mp
mp.mp.dps = 30
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
def build(lam_str,N):
    lam=mp.mpf(lam_str); L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1)); mx=int(lam*lam)
    Lam=vm_zeta(mx); C=LOG4PI+GAMMA; half=mp.mpf('1')/2
    PR=mp.zeros(dim)
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
    def Qp(p):
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
    return PR,Qp,primes,L
def kap(M):
    E,_=mp.eigsy(M); return sum(1 for i in range(M.rows) if E[i]<-mp.mpf('1e-16'))
def sigp(M):
    E,_=mp.eigsy(M); ev=[E[i] for i in range(M.rows)]
    return sum(1 for e in ev if e>1e-14), sum(1 for e in ev if e<-1e-14)

for lam,N in [('7.0',12),('9.0',13)]:
    PR,Qp,primes,L=build(lam,N); Lf=float(L)
    print(f"\n=== lambda={lam} N={N} L={Lf:.3f} (L/2={Lf/2:.3f}, lambda={float(lam):.1f}) ===")
    acc=PR.copy(); prevk=kap(acc); peakk=prevk; peakp=None
    print("  primo | log p | <L/2? | sig(Q_p)=(pos,neg) | kappa | flujo Dk")
    for p in primes:
        Q=Qp(p); sp,sn=sigp(Q); acc=acc-Q; k=kap(acc); dk=k-prevk
        if k>peakk: peakk=k; peakp=p
        rel='IN ' if mp.log(p)<Lf/2 else 'OUT'
        print(f"   {p:2d}  | {float(mp.log(p)):.2f}  | {rel}   | ({sp:2d},{sn:2d})           | {k:2d}   | {dk:+d}")
        prevk=k
    # net spectral flow
    print(f"  pico kappa={peakk} en p={peakp}; net spectral flow (P-R -> full) = {k-kap(PR)}")
    # verificar: post-pico, todos los Dk <=0 ?  (monotonia del cono amplio)
