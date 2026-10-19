import mpmath as mp
mp.mp.dps = 30
logpi = mp.log(mp.pi)
Psi = lambda r: mp.re(mp.digamma(mp.mpf('0.25')+1j*mp.mpf(r)/2)) - logpi

# von Mangoldt via smallest-prime-factor sieve
def vonmangoldt_list(nmax):
    spf=list(range(nmax+1))
    i=2
    while i*i<=nmax:
        if spf[i]==i:
            for j in range(i*i,nmax+1,i): 
                if spf[j]==j: spf[j]=i
        i+=1
    Lam=[mp.mpf(0)]*(nmax+1)
    for n in range(2,nmax+1):
        p=spf[n]; m=n
        while m%p==0: m//=p
        if m==1: Lam[n]=mp.log(p)   # n is a prime power
    return Lam

NMAX=20000
Lam=vonmangoldt_list(NMAX)

# precompute zeros once
NZ=300
ZEROS=[mp.im(mp.zetazero(k)) for k in range(1,NZ+1)]

def run(sig):
    sig=mp.mpf(sig)
    h = lambda r: (r**2+mp.mpf('0.25'))**2 * mp.e**(-r**2/sig**2)
    g = lambda u: (1/(2*mp.pi))*mp.quad(lambda r: h(r)*mp.cos(u*r), [-mp.inf,0,mp.inf])
    Q = mp.fsum(2*h(gk) for gk in ZEROS)
    A = (1/(2*mp.pi))*mp.quad(lambda r: h(r)*Psi(r), [-mp.inf,-6.29,0,6.29,mp.inf])
    P = mp.fsum(2*(Lam[n]/mp.sqrt(n))*g(mp.log(n)) for n in range(2,NMAX+1) if Lam[n]!=0)
    return Q,A,P

print(f"{'sigma':>6} {'Q=sum h(g)':>15} {'A_inf':>15} {'P(primes)':>15} {'A-P':>15} {'Q-(A-P)':>12}")
for s in ['2','3','4']:
    Q,A,P=run(s)
    print(f"{s:>6} {mp.nstr(Q,9):>15} {mp.nstr(A,9):>15} {mp.nstr(P,9):>15} {mp.nstr(A-P,9):>15} {mp.nstr(Q-(A-P),6):>12}")
