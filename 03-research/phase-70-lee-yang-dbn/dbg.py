import mpmath as mp
mp.mp.dps=25
def Phi(u,nmax=60):
    e4=mp.e**(4*u);e5=mp.e**(5*u);e9=mp.e**(9*u);s=mp.mpf(0)
    for n in range(1,nmax+1):
        s+=(2*mp.pi**2*n**4*e9-3*mp.pi*n**2*e5)*mp.e**(-mp.pi*n**2*e4)
    return s
def MyXi(t):
    # very fine oscillatory quad up to U where Phi negligible (~1.5)
    return 2*mp.quadosc(lambda u: Phi(u)*mp.cos(t*u), [0, mp.inf], omega=t)
def xiXi(t):
    s=mp.mpf('0.5')+1j*t
    return (0.5*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)).real
print(" t     MyXi(t)        xi(1/2+it)     ratio")
for t in (14.0,14.134725,16.0,18.0,21.02204,25.0):
    a=MyXi(mp.mpf(str(t))); b=xiXi(mp.mpf(str(t)))
    print(f"{t:7.3f}  {mp.nstr(a,6):>12}  {mp.nstr(b,6):>12}  {mp.nstr(a/b,5) if b!=0 else 'inf'}")
