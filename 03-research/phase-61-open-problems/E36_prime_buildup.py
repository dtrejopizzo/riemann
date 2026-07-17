"""
E36: ¿como marginalizan los primos? mu_0 agregando primos uno a uno.
Tesis: polo+arquimediano (P - R) = presupuesto positivo grande; los primos (-Q)
lo consumen. RH = los primos (Euler, multiplicativos) consumen JUSTO hasta 0+ sin
pasarse al negativo. Para ζ: descenso ordenado a +e^{-21}. Para DH (no polo, coef
oscilantes): el balance no aterriza en >=0.
Tambien: signatura de cada forma de un solo primo Q_p (¿sign-definida?).
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

def archmat(L,lam,N,even,C):
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
            A[a,b]=-R; A[b,a]=-R   # -R (la pieza arquimediana en A=P-R-Q)
    return A
def polemat(L,N):
    dim=2*N+1; idx=list(range(-N,N+1)); P=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L)
            v=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L]); P[a,b]=v; P[b,a]=v
    return P
def primemat_upto(L,N,Lam,Mmax):
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0)
            for k in range(2,Mmax+1):
                if Lam[k]!=0: s+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
            Q[a,b]=-s; Q[b,a]=-s   # -Q
    return Q
def mineig(M):
    E,_=mp.eigsy(M); return min(E[i] for i in range(M.rows))

lam,N='7.0',14; lamf=float(lam); L=2*mp.log(mp.mpf(lam)); mx=int(lamf**2)
C0=LOG4PI+GAMMA
Lz=vm_zeta(mx); Ld=vm_DH(mx)

print(f"lambda={lam} N={N} (primos hasta {mx})\n")
# ZETA: polo + arch, luego restar primos acumulando
Parch_z = polemat(L,N) + archmat(L,lamf,N,True,C0)   # P - R  (sin primos)
print("ZETA:  P-R (sin primos), mu_0 =", mp.nstr(mineig(Parch_z),5), " <- presupuesto")
for M in [2,3,5,7,11,19,29,49]:
    Q=primemat_upto(L,N,Lz,M)
    print(f"   + primos<= {M:2d}:  mu_0 = {mp.nstr(mineig(Parch_z+Q),5)}")
# DH: sin polo + arch_impar, restar primos DH acumulando
arch_d = archmat(L,lamf,N,False,C0)   # -R (sin polo)
print("\nDH:    -R (sin polo, sin primos), mu_0 =", mp.nstr(mineig(arch_d),5))
for M in [2,3,5,7,11,19,29,49]:
    Q=primemat_upto(L,N,Ld,M)
    print(f"   + primos<= {M:2d}:  mu_0 = {mp.nstr(mineig(arch_d+Q),5)}")
