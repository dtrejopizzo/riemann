"""
E37: signaturas (numero de autovalores negativos) -> estructura de Pontryagin.
Tesis del plan: kappa = #autovalores negativos = #ceros off-line (x2); cada primo
aporta a lo sumo una estructura definida. Para zeta (RH): 0 negativos. Para DH:
negativos ligados a los off-line. Tambien signatura de las piezas P, R, Q, Q_p.
"""
import mpmath as mp
mp.mp.dps = 40
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
def vm_DH(mx):
    kap=(mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
    a=lambda n:[mp.mpf(0),mp.mpf(1),kap,-kap,mp.mpf(-1)][n%5]
    c=[mp.mpf(0)]*(mx+1)
    for n in range(1,mx+1):
        s=mp.log(n)*a(n); d=2
        while d<=n:
            if n%d==0: s-=a(d)*c[n//d]
            d+=1
        c[n]=s
    return c
def archmat(L,N,even,C):
    dim=2*N+1; idx=list(range(-N,N+1)); half=mp.mpf('1')/2
    w=(lambda u:mp.e**(u/2)) if even else (lambda u:mp.e**(-u/2))
    A=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); q0=q(mp.mpf(0))
            def ig(u):
                if u<mp.mpf('1e-12'):
                    h=mp.mpf('1e-8'); return ((q(h)-q0)/h+(half if even else -half)*q0)/2
                return (w(u)*q(u)-q0)/(2*mp.sinh(u))
            R=C*q0/2+mp.quad(ig,[0,L])+q0*mp.log(mp.tanh(L/2))/2
            A[a,b]=R; A[b,a]=R
    return A
def polemat(L,N):
    dim=2*N+1; idx=list(range(-N,N+1)); P=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L)
            v=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L]); P[a,b]=v; P[b,a]=v
    return P
def primemat(L,N,Lam,plist):
    """forma de un conjunto de primos plist (todas sus potencias <=e^L)."""
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim); mx=int(mp.e**L)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0)
            for p in plist:
                pw=p
                while pw<=mx:
                    if Lam[pw]!=0: s+=Lam[pw]*(mp.mpf(pw)**mp.mpf('-0.5'))*q(mp.log(pw))
                    pw*=p
            Q[a,b]=s; Q[b,a]=s
    return Q
def sig(M):
    E,_=mp.eigsy(M); ev=sorted([E[i] for i in range(M.rows)])
    neg=sum(1 for e in ev if e<-mp.mpf('1e-25'))
    return neg, mp.nstr(ev[0],4), mp.nstr(ev[-1],4)

lam,N='7.0',14; L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2); C0=LOG4PI+GAMMA
Lz=vm_zeta(mx); Ld=vm_DH(mx)
primes=[p for p in range(2,mx+1) if Lz[p]!=0 and all(p%d for d in range(2,int(p**0.5)+1))]

P=polemat(L,N); Rz=archmat(L,N,True,C0); Rd=archmat(L,N,False,C0)
print(f"lambda={lam} N={N} dim={2*N+1}  (neg = #autovalores < 0)\n")
print("PIEZAS:")
print("  P (polo)        : neg,min,max =", sig(P))
print("  R (arch zeta)   : neg,min,max =", sig(Rz))
Qz=primemat(L,N,Lz,primes); Qd=primemat(L,N,Ld,primes)
print("  Q (primos zeta) : neg,min,max =", sig(Qz))
print("\nFORMA COMPLETA:")
print("  A_zeta = P - R - Q          : neg,min,max =", sig(P-Rz-Qz), " (RH: esperar 0 neg)")
print("  A_DH   = -R_imp - Q_DH      : neg,min,max =", sig(-Rd-Qd))
print("\nPOR PRIMO (Q_p de zeta, forma de un solo primo):")
for p in primes[:6]:
    print(f"  Q_{p}: neg,min,max =", sig(primemat(L,N,Lz,[p])))
print("\nA_zeta agregando primos (signatura):")
acc=P-Rz
for kk,p in enumerate(primes):
    acc=acc-primemat(L,N,Lz,[p])
    if p in [2,3,7,19,43] or p==primes[-1]:
        print(f"  primos<= {p:2d}: ", sig(acc))
