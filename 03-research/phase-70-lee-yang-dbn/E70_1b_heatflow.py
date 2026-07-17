"""
E70.1b -- de Bruijn-Newman heat flow, with the oscillatory integral resolved and validated.
"""
import mpmath as mp
mp.mp.dps = 20

def Phi(u, nmax=40):
    e4=mp.e**(4*u); e5=mp.e**(5*u); e9=mp.e**(9*u); s=mp.mpf(0)
    for n in range(1,nmax+1):
        term=(2*mp.pi**2*n**4*e9 - 3*mp.pi*n**2*e5)*mp.e**(-mp.pi*n**2*e4)
        s+=term
        if abs(term)<mp.mpf(10)**(-30) and n>3: break
    return s

# Phi decays like exp(-pi e^{4u}) -> negligible beyond u~2. Resolve cos(tu) with fine nodes.
def Xi_lambda(t, lam, U=2.4, npts=None):
    t=mp.mpf(t); lam=mp.mpf(lam)
    if npts is None: npts=max(40, int(float(t)*U/mp.pi*4))  # ~4 nodes per oscillation
    pts=[U*k/npts for k in range(npts+1)]
    f=lambda u: mp.e**(lam*u*u)*Phi(u)*mp.cos(t*u)
    return 2*mp.quad(f, pts)

if __name__=="__main__":
    print("VALIDATION: Xi_0(t) should vanish at Riemann zeros 14.1347, 21.022, 25.011, 30.425:\n")
    for t in (14.134725,21.022040,25.010858,30.424876,17.0):
        v=Xi_lambda(t,0)
        tag="~ZERO" if abs(v)<abs(Xi_lambda(17.0,0))*0.05 else ""
        print(f"   Xi_0({t}) = {mp.nstr(v,6):>14}   {tag}")
    print("\nreal-zero count of Xi_lambda in t in [10,40] vs lambda:")
    def count(lam,t0=10,t1=40,step=0.2):
        prev=None; c=0; zs=[]
        t=mp.mpf(t0)
        while t<=t1:
            v=Xi_lambda(t,lam)
            if prev is not None and mp.sign(v)!=mp.sign(prev):
                try: zs.append(float(mp.findroot(lambda x:Xi_lambda(x,lam),t-step/2)))
                except: pass
                c+=1
            prev=v; t+=step
        return c,zs
    print("  lambda   #real zeros in [10,40]   zeros")
    for lam in (0.3,0.0,-0.2,-0.5):
        c,zs=count(mp.mpf(str(lam)))
        print(f"  {lam:+.2f}     {c:2d}   " + ", ".join(f"{z:.2f}" for z in zs[:7]))
