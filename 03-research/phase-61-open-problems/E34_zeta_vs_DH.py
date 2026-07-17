"""
E34: VIA (a) — comparacion zeta vs DH en framework IDENTICO (el control del muro).
Mismo codigo, mismas convenciones. Diferencias FIELES unicamente:
  - polo: zeta tiene W02=int q*2cosh(y/2) (polos s=0,1); DH entera -> W02=0.
  - primos: Lambda(n) [zeta]  vs  Lambda_DH(n) [DH, exacto E31].
  - arquimediano: peso e^{+y/2} (zeta, par a=0, psi(1/4)) vs e^{-y/2} (DH, impar a=1, psi(3/4)).
Test: ¿zeta da eps_0 ~ 0+ y DH da eps_0 < 0?  -> el engine DETECTA el muro (no ciego).
Robustez: barrido del constante arquimediano C (eps_0 shiftea lineal); ver donde cruza 0.
"""
import mpmath as mp
mp.mp.dps = 40
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi); LOG5 = mp.log(5)
kappa = (mp.sqrt(10-2*mp.sqrt(5)) - 2)/(mp.sqrt(5)-1)

def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def a_dh(n): return [mp.mpf(0), mp.mpf(1), kappa, -kappa, mp.mpf(-1)][n % 5]
def Lam_zeta(mx):
    L=[mp.mpf(0)]*(mx+1); sv=[True]*(mx+1)
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pm=p
            while pm<=mx: L[pm]=lp; pm*=p
    return L
def Lam_DH(mx):
    c=[mp.mpf(0)]*(mx+1)
    for n in range(1,mx+1):
        s=mp.log(n)*a_dh(n); d=2
        while d<=n:
            if n%d==0: s-=a_dh(d)*c[n//d]
            d+=1
        c[n]=s
    return c

def entry(m,n,L,lam,Lam,C,even,pole):
    q=q_func(m,n,L); q0=q(mp.mpf(0))
    w = (lambda y: mp.e**(y/2)) if even else (lambda y: mp.e**(-y/2))
    def wr(y):
        if y<mp.mpf('1e-10'): y=mp.mpf('1e-10')
        return (w(y)*q(y)-q0)/(2*mp.sinh(y))
    WR = C*q0/2 + mp.quad(wr,[0,L]) + q0*mp.log(mp.tanh(L/2))/2
    arith=mp.mpf(0); mx=int(lam*lam)
    for k in range(2,mx+1):
        if Lam[k]!=0: arith += Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
    if pole:
        W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)),[0,L])
        return W02 - WR - arith
    else:
        return - WR - arith

def spec(lam_f, N, mode, C, pole=None):
    lam=mp.mpf(lam_f); L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1))
    mx=int(lam*lam)
    Lam = Lam_zeta(mx) if mode=='zeta' else Lam_DH(mx)
    even = (mode=='zeta')
    if pole is None: pole = (mode=='zeta')  # zeta tiene polo, DH no
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=entry(idx[a],idx[b],L,lam,Lam,C,even,pole); M[a,b]=v; M[b,a]=v
    E,_=mp.eigsy(M); return sorted([E[i] for i in range(dim)])

lam='7.0'; N=14
Cz = (GAMMA+LOG4PI)   # coef correcto (E11: (log4pi+gamma)*q0/2 -> C=log4pi+gamma)
print(f"=== VIA (a): zeta vs DH, framework identico, lambda={lam} N={N} ===")
print(f"constante arquimediana base C_zeta = log(4pi)+gamma = {mp.nstr(Cz,6)}\n")

ez = spec(lam,N,'zeta',Cz)
print(f"ZETA (C={mp.nstr(Cz,5)}): eps_0={mp.nstr(ez[0],5)}  eps[:4]={[mp.nstr(e,4) for e in ez[:4]]}")
print(f"   -> deberia ser ~e^-21 (control: framework reproduce E11)  signo: {'+' if ez[0]>0 else 'NEG'}\n")

ed0 = spec(lam,N,'DH',Cz)
print(f"DH  (C={mp.nstr(Cz,5)}, =MISMO que zeta): eps_0={mp.nstr(ed0[0],5)}  signo: {'+' if ed0[0]>0 else 'NEGATIVO (detecta!)'}")
ed1 = spec(lam,N,'DH',Cz+2*LOG5)
print(f"DH  (C={mp.nstr(Cz+2*LOG5,5)}, +2log5 conductor): eps_0={mp.nstr(ed1[0],5)}  signo: {'+' if ed1[0]>0 else 'NEGATIVO (detecta!)'}")

# TEST DEL MECANISMO: zeta SIN polo (W02=0) -- ¿la positividad viene del polo?
eznp = spec(lam,N,'zeta',Cz,pole=False)
print(f"\nMECANISMO: ZETA SIN polo (W02=0), C={mp.nstr(Cz,5)}: eps_0={mp.nstr(eznp[0],5)}  signo: {'+' if eznp[0]>0 else 'NEGATIVO'}")
print(f"   (si <0: el POLO s=1 / termino principal PNT es la fuente de la positividad de Weil)")

print("\nrobustez: eps_0(DH) vs constante C (cruza 0 en C*):")
for C in [mp.mpf('1.0'), mp.mpf('2.0'), Cz, Cz+LOG5, Cz+2*LOG5, mp.mpf('7.0')]:
    e=spec(lam,N,'DH',C)
    print(f"  C={mp.nstr(C,5)}: eps_0={mp.nstr(e[0],4)}")
