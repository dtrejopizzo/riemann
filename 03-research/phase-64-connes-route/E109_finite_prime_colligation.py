"""
E109 — Connes Sec.7.2: finite-prime colligation truncation + normal-convergence criterion.

Criterion (Montel): if the finite-prime approximants Theta_{<=P,omega} are Schur (passive) and
converge locally uniformly on C_+ to Theta_omega as P->infinity, the limit is Schur, hence (at omega=0)
RH. Two regimes:
  (1) SAFE omega>1/2 (in the convergence strip Im z<omega-1/2): truncation should be passive (Pick-PSD)
      and converge to Theta_omega.
  (2) CRITICAL omega=0: does the scalar truncation Theta_{<=P,0} converge / stay Pick-PSD?
      Connes' prediction: the SCALAR product does NOT converge nicely in the critical region (scalar
      local factors are not individually inner) -> the matrix colligation is needed. Test honestly.

Theta_{<=P,omega}(z) = Theta_inf(z) * prod_{p<=P} Theta_p(z),  Theta_p=(1-a p^{iz})/(1-a p^{-iz}),
a=p^{-(1/2+omega)}, Theta_inf=G(s_+)/G(s_-). (Closed-form factors = analytic continuation; the
'convergence' is genuine only in the strip per Connes audit 0.2.)
Honesty: mpmath dps=25; report convergence error and Pick min-eig vs P and omega.
"""
import mpmath as mp
mp.mp.dps = 25


def G(s):
    return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)


def xi(s):
    return G(s)*mp.zeta(s)


def Theta_full(omega, z):
    return xi(mp.mpf('0.5')+omega+1j*z)/xi(mp.mpf('0.5')+omega-1j*z)


def Theta_inf(omega, z):
    return G(mp.mpf('0.5')+omega+1j*z)/G(mp.mpf('0.5')+omega-1j*z)


def Theta_p(p, omega, z):
    a = mp.mpf(p)**(-(mp.mpf('0.5')+omega))
    return (1-a*mp.mpf(p)**(1j*z))/(1-a*mp.mpf(p)**(-1j*z))


def primes(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j]=False
    return [i for i in range(2, n+1) if s[i]]


def Theta_trunc(omega, z, P):
    v = Theta_inf(omega, z)
    for p in primes(P): v *= Theta_p(p, omega, z)
    return v


def pick_min(thfun, pts):
    import numpy as np
    n = len(pts); Th = [thfun(z) for z in pts]
    M = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(n):
            M[i, j] = complex((1-Th[i]*mp.conj(Th[j]))/(2*mp.pi*1j*(mp.conj(pts[j])-pts[i])))
    M = (M+M.conj().T)/2
    return float(np.linalg.eigvalsh(M).min())


if __name__ == '__main__':
    print("E109 — finite-prime truncation: passivity + convergence to Theta_omega.\n")

    print("(1) SAFE omega=1.0, points IN strip (Im z<0.5): convergence + Pick-PSD vs P")
    om = mp.mpf('1.0'); pts = [mp.mpf(x)+1j*mp.mpf('0.3') for x in (10, 16, 22, 28)]
    full = {z: Theta_full(om, z) for z in pts}
    for P in [20, 100, 500, 2000]:
        err = max(abs(Theta_trunc(om, z, P)-full[z]) for z in pts)
        mn = pick_min(lambda z: Theta_trunc(om, z, P), pts)
        print(f"   P={P:5d}: max|trunc-full|={float(err):.3e}  Pick min eig={mn:+.3e} {'PSD' if mn>-1e-9 else 'NEG'}")

    print("\n(2) CRITICAL omega=0.0, points near zero ordinates: does scalar truncation converge / stay Schur?")
    om = mp.mpf('0'); pts = [mp.mpf(g)+1j*mp.mpf('0.5') for g in (14.13, 21.02, 25.01)]
    full = {z: Theta_full(om, z) for z in pts}
    for P in [20, 100, 500, 2000, 8000]:
        err = max(abs(Theta_trunc(om, z, P)-full[z]) for z in pts)
        mn = pick_min(lambda z: Theta_trunc(om, z, P), pts)
        print(f"   P={P:5d}: max|trunc-full|={float(err):.3e}  Pick min eig={mn:+.3e} {'PSD' if mn>-1e-9 else 'NEG'}")
    print("   (full Theta_0 is Pick-PSD for zeta -- E104; question is whether the scalar truncation gets there)")
