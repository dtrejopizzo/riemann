"""
E31: coeficientes von Mangoldt de Davenport-Heilbronn por inversion de Dirichlet EXACTA.
(ataca NG-E7: el lambda_min~-9e4 previo no era reproducible; aqui es exacto/reproducible)

f(s)=sum a_n n^{-s}, a_n periodo 5: [n=0 mod5:0, 1:1, 2:k, 3:-k, 4:-1], k=tan(theta).
-f'/f = sum c_n n^{-s},  c_n = (log n) a_n - sum_{d|n, d>1} a_d c_{n/d}   (a_1=1).
Verifica: reproducible, c_n reales, estructura (¿crece? ¿soportado donde?).
Compara con ZETA: Lambda(n)=log p en prime powers, 0 si no.
"""
import mpmath as mp
mp.mp.dps = 40

# theta
k = (mp.sqrt(10-2*mp.sqrt(5)) - 2)/(mp.sqrt(5)-1)
theta = mp.atan(k)
print(f"kappa=tan(theta) = {mp.nstr(k,10)}   theta = {mp.nstr(theta,10)}")

def a(n):
    r = n % 5
    return [mp.mpf(0), mp.mpf(1), k, -k, mp.mpf(-1)][r]

# verificar a_n via la formula sec(theta) Re(e^{-i theta} chi(n))
chi = {1:1, 2:1j, 3:-1j, 4:-1, 0:0}
sec = 1/mp.cos(theta)
for n in range(1,6):
    af = sec*mp.re(mp.e**(-1j*theta)*chi[n%5])
    print(f"  a_{n} = {mp.nstr(a(n),6)}  (formula: {mp.nstr(af,6)})  match={abs(a(n)-af)<1e-30}")

# von Mangoldt DH por recursion
NMAX = 60
c = [mp.mpf(0)]*(NMAX+1)
for n in range(1, NMAX+1):
    s = mp.log(n)*a(n)
    d = 2
    while d <= n:
        if n % d == 0:
            s -= a(d)*c[n//d]
        d += 1
    c[n] = s

print("\n n :  Lambda_DH(n)        a_n      |  Lambda_zeta(n)")
def Lzeta(n):
    # log p si n=p^k, else 0
    m=n;
    for p in range(2,n+1):
        if n%p==0:
            t=n
            while t%p==0: t//=p
            return mp.log(p) if t==1 else mp.mpf(0)
    return mp.mpf(0)
for n in range(1, 31):
    print(f" {n:2d} : {mp.nstr(c[n],8):>14}   {mp.nstr(a(n),5):>7}   |  {mp.nstr(Lzeta(n),6)}")

mx = max(abs(c[n]) for n in range(2,NMAX+1))
print(f"\n max|Lambda_DH(n)| (n<= {NMAX}) = {mp.nstr(mx,6)}  (¿crece? comparar con log n = {mp.nstr(mp.log(NMAX),5)})")
# suma P_lambda^DH = sum_{n<=lam^2} Lambda_DH(n)/sqrt(n) para lam=7 (lam^2=49)
P = sum(c[n]/mp.sqrt(n) for n in range(2,50))
print(f" P_DH(lam=7) = sum_{{n<=49}} Lambda_DH(n)/sqrt(n) = {mp.nstr(P,6)}  (zeta: P~2lam=14)")
