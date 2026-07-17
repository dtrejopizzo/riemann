"""
E35: aislar el mecanismo Euler vs off-line en el signo de mu_lambda.
Mantengo el FRAMEWORK fijo y varío piezas, para ver QUE controla el signo:
  - coeficientes: Lambda(n) [Euler, >=0]  vs  Lambda_DH(n) [oscilante]  vs |Lambda_DH(n)|
  - polo: presente (zeta) / ausente (DH)
  - arquimediano: par e^{+u/2} (zeta) / impar e^{-u/2} (DH)
Combinaciones clave:
  (1) zeta puro: polo + arch_par + Lambda            -> +e^{-21} (RH)
  (2) HIBRIDO  : polo + arch_par + Lambda_DH         -> ¿rompe la positividad con polo?
  (3) HIBRIDO+ : polo + arch_par + |Lambda_DH|       -> ¿coef positivos restauran?
  (4) DH fiel  : sin polo + arch_impar + Lambda_DH   -> -1.6
  (5) DH |.|   : sin polo + arch_impar + |Lambda_DH| -> ¿coef positivos ayudan sin polo?
"""
import mpmath as mp
mp.mp.dps = 40
GAMMA=mp.euler; LOG4PI=mp.log(4*mp.pi); LOG5=mp.log(5)

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

def entry(m,n,L,lam,Lam,C,even,pole):
    q=q_kernel(m,n,L); q0=q(mp.mpf(0)); half=mp.mpf('1')/2
    w=(lambda u:mp.e**(u/2)) if even else (lambda u:mp.e**(-u/2))
    def ig(u):
        if u<mp.mpf('1e-12'):
            h=mp.mpf('1e-8'); return ((q(h)-q0)/h+(half if even else -half)*q0)/2
        return (w(u)*q(u)-q0)/(2*mp.sinh(u))
    R=C*q0/2+mp.quad(ig,[0,L])+q0*mp.log(mp.tanh(L/2))/2
    Q=mp.mpf(0); mx=int(lam*lam)
    for k in range(2,mx+1):
        if Lam[k]!=0: Q+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
    P=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L]) if pole else mp.mpf(0)
    return P-R-Q

def mu0(lam_str,N,Lam,C,even,pole):
    lam=mp.mpf(lam_str); L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1))
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=entry(idx[a],idx[b],L,lam,Lam,C,even,pole); M[a,b]=v; M[b,a]=v
    E,_=mp.eigsy(M); return min(E[i] for i in range(dim))

lam,N='7.0',14; mx=int(float(lam)**2)
C0=LOG4PI+GAMMA
Lz=vm_zeta(mx); Ld=vm_DH(mx); Lda=[abs(x) for x in Ld]

print(f"lambda={lam} N={N}  C=log4pi+gamma={mp.nstr(C0,5)}\n")
print("(1) ZETA puro      [polo + arch_par + Lambda]      :", mp.nstr(mu0(lam,N,Lz,C0,True,True),5))
print("(2) HIBRIDO        [polo + arch_par + Lambda_DH]   :", mp.nstr(mu0(lam,N,Ld,C0,True,True),5))
print("(3) HIBRIDO |.|    [polo + arch_par + |Lambda_DH|] :", mp.nstr(mu0(lam,N,Lda,C0,True,True),5))
print("(4) DH fiel        [sinpolo + arch_imp + Lambda_DH]:", mp.nstr(mu0(lam,N,Ld,C0,False,False),5))
print("(5) DH |.|         [sinpolo + arch_imp + |Lam_DH|] :", mp.nstr(mu0(lam,N,Lda,C0,False,False),5))
print("(6) ZETA sin polo  [sinpolo + arch_par + Lambda]   :", mp.nstr(mu0(lam,N,Lz,C0,True,False),5))
