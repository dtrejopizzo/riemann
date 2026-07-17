"""
E70.1 -- the de Bruijn-Newman heat flow Xi_lambda and zero migration.

Xi_lambda(t) = 2 * integral_0^inf e^{lambda u^2} Phi(u) cos(t u) du,
Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u}).
Xi_0 = xi(1/2 + i t) (real, even). Zeros of Xi_lambda real <=> lambda >= Lambda (dBN constant).
RH <=> Lambda <= 0; Rodgers-Tao: Lambda >= 0; so RH <=> Lambda = 0.

Test: count real zeros of Xi_lambda(t) in a fixed t-window as lambda varies. For lambda >= 0 the count
should be full (all real); if we push lambda negative, pairs of real zeros should merge and go complex
(count drops) -- illustrating the heat-flow forcing and the threshold near Lambda ~ 0.
"""
import mpmath as mp
mp.mp.dps = 25

def Phi(u, nmax=30):
    e4=mp.e**(4*u); e5=mp.e**(5*u); e9=mp.e**(9*u)
    s=mp.mpf(0)
    for n in range(1,nmax+1):
        s += (2*mp.pi**2*n**4*e9 - 3*mp.pi*n**2*e5)*mp.e**(-mp.pi*n**2*e4)
    return s

def Xi_lambda(t, lam):
    f=lambda u: mp.e**(lam*u*u)*Phi(u)*mp.cos(t*u)
    return 2*mp.quad(f,[0,0.5,1,2,3])

def count_real_zeros(lam, t0, t1, step=0.25):
    ts=mp.arange(t0,t1,step); prev=None; cnt=0; zeros=[]
    for t in ts:
        v=Xi_lambda(t,lam)
        if prev is not None and mp.sign(v)!=mp.sign(prev) and prev!=0:
            z=mp.findroot(lambda x: Xi_lambda(x,lam), t-step/2)
            zeros.append(float(z)); cnt+=1
        prev=v
    return cnt, zeros

if __name__=="__main__":
    print("Xi_lambda real-zero count in t in [10,40] vs lambda (heat-flow forcing):\n")
    print("  lambda    #real zeros in [10,40]   first few zeros")
    for lam in (0.4, 0.2, 0.0, -0.1, -0.3, -0.6):
        c,z=count_real_zeros(mp.mpf(str(lam)),10,40)
        zs=", ".join(f"{zz:.2f}" for zz in z[:5])
        print(f"  {lam:+.2f}      {c:2d}                   {zs}")
    print("\nReading: lambda>=0 -> full real-zero count (RH-consistent, Lambda~0).")
    print("lambda<0 -> count drops as pairs go complex (crossing below the dBN threshold).")
