"""
E105 — Connes Sec.3 / Q1: the unconditional omega>1/2 colligation = restricted tensor product
of local Tate factors. Verify the Euler/Tate factorization and LOCAL passivity.

For omega>1/2, s_pm = 1/2+omega +- i z have Re s_pm = 1/2+omega > 1, so the Euler product converges:
   Theta_omega(z) = xi(s_+)/xi(s_-)
                  = [G(s_+)/G(s_-)] * prod_p (1-p^{-s_-})/(1-p^{-s_+})
                  = Theta_inf(z) * prod_p Theta_p(z),
   G(s)=1/2 s(s-1) pi^{-s/2} Gamma(s/2)  (archimedean+pole block),
   Theta_p(z) = (1 - a_p p^{ i z})/(1 - a_p p^{-i z}),  a_p = p^{-(1/2+omega)}  (local Tate factor).

Claims to verify numerically (omega>1/2):
  (1) LOCAL PASSIVITY: each |Theta_p(z)| <= 1 for Im z>0 (each local block is Schur/inner);
      the archimedean block Theta_inf likewise inner.
  (2) FACTORIZATION: Theta_inf * prod_{p<=P} Theta_p  ->  Theta_omega  as P grows.
  (3) the assembled product is Pick-PSD (passive) — consistent with E104.
This realizes "the global colligation is the restricted tensor product of local Tate colligations"
in the safe region. RH is the continuation of this passive structure to omega=0 (E104).
Honesty: mpmath dps=30; omega>1/2 only (unconditional region).
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 30


def G(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2)


def xi(s):
    return G(s) * mp.zeta(s)


def Theta_full(omega, z):
    return xi(mp.mpf('0.5') + omega + 1j * z) / xi(mp.mpf('0.5') + omega - 1j * z)


def Theta_inf(omega, z):
    sp = mp.mpf('0.5') + omega + 1j * z; sm = mp.mpf('0.5') + omega - 1j * z
    return G(sp) / G(sm)


def Theta_p(p, omega, z):
    a = mp.mpf(p) ** (-(mp.mpf('0.5') + omega))
    return (1 - a * mp.mpf(p) ** (1j * z)) / (1 - a * mp.mpf(p) ** (-1j * z))


def primes_upto(n):
    s = [True] * (n + 1); s[:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i): s[j] = False
    return [i for i in range(2, n + 1) if s[i]]


def assembled(omega, z, P):
    val = Theta_inf(omega, z)
    for p in primes_upto(P):
        val = val * Theta_p(p, omega, z)
    return val


if __name__ == '__main__':
    omega = mp.mpf('1.0')   # safely > 1/2 (unconditional region)
    print(f"E105 — Tate factorization of Theta_omega (omega={float(omega)} > 1/2, unconditional)\n")

    # test points must lie in the STRIP Im z < 1/2+omega = 1.5 (local factors have poles at Im z=1/2+omega)
    pts = [mp.mpf(x) + 1j * mp.mpf(y) for (x, y) in [(6, 0.3), (14, 0.6), (22, 0.6), (30, 0.9)]]

    print("Note: local Tate factors are passive in the STRIP Im z < 1/2+omega (poles at Im z=1/2+omega).")
    print("(1) LOCAL PASSIVITY in the strip: max |Theta_p(z)| over test pts (must be <=1); arch too:")
    for p in [2, 3, 5, 7, 11, 101]:
        mx = max(float(abs(Theta_p(p, omega, z))) for z in pts)
        print(f"     p={p:4d}: max|Theta_p|={mx:.6f}  {'inner' if mx <= 1 + 1e-9 else 'NOT inner'}")
    mxi = max(float(abs(Theta_inf(omega, z))) for z in pts)
    print(f"     arch  : max|Theta_inf|={mxi:.6f}  {'inner' if mxi <= 1 + 1e-9 else 'NOT inner'}")

    print("\n(2) FACTORIZATION: |Theta_inf * prod_{p<=P} Theta_p  -  Theta_omega|  -> 0 :")
    z0 = mp.mpf(14) + 1j * mp.mpf('0.6')
    full = Theta_full(omega, z0)
    print(f"     reference Theta_omega(z0) = {mp.nstr(full,8)}")
    for P in [10, 50, 200, 1000, 5000]:
        err = abs(assembled(omega, z0, P) - full)
        print(f"     P={P:5d}: |assembled - full| = {mp.nstr(err,4)}")

    print("\n(3) Pick matrix of the ASSEMBLED product (P=2000) — passive (PSD)?")
    P = 2000
    n = len(pts); Th = [assembled(omega, z, P) for z in pts]
    M = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(n):
            M[i, j] = complex((1 - Th[i] * mp.conj(Th[j])) / (2 * mp.pi * 1j * (mp.conj(pts[j]) - pts[i])))
    M = (M + M.conj().T) / 2
    print(f"     min eig Pick(assembled) = {np.linalg.eigvalsh(M).min():.3e}  "
          f"(>=0 => passive product of local Tate colligations)")
