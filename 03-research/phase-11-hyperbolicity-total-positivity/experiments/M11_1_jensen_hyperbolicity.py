#!/usr/bin/env python3
"""
Phase 11 / M11.1 — the hyperbolicity (Jensen-polynomial / stable-polynomial) route.

RH  <=>  Xi(t)=xi(1/2+it) is in the Laguerre-Polya class (all real zeros)
     <=>  every Jensen polynomial J^{d,n}(X) = sum_{j=0}^d C(d,j) a(n+j) X^j  is HYPERBOLIC (real-rooted),
where {a(k)} are the (normalized) Taylor coefficients of Xi (Griffin-Ono-Rolen-Zagier, PNAS 2019).

This is REAL-ROOTEDNESS, not a quadratic-form positivity -> a DIFFERENT kind of argument (interlacing /
stability preservers, Borcea-Branden, Marcus-Spielman-Srivastava) that plausibly escapes the wrong-sign
capstone by a new route.

M11.1 (grounding): compute a(k) = Xi^{(2k)}(0)/(2k)!  (Xi is even), build Jensen polynomials, verify they
are hyperbolic, and look at the interlacing structure / the approach to Hermite (the GORZ phenomenon).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

# Riemann xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s); Xi(t)=xi(1/2+it) is even, real on R.
def Xi(t):
    s = mp.mpf('0.5') + 1j*t
    return (mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)).real

def xi_taylor_even(M):
    """a(k) = Xi^{(2k)}(0)/(2k)!  for k=0..M-1, via mpmath Taylor at 0 (order 2M)."""
    c = mp.taylor(Xi, 0, 2*M)          # coefficients c_m of Xi(t)=sum c_m t^m ; odd ones ~0
    a = [c[2*k] for k in range(M)]      # even Taylor coefficients = a(k)
    return a

def jensen_poly(a, d, n):
    """J^{d,n}(X) = sum_{j=0}^d binom(d,j) a(n+j) X^j ; return numpy real coeffs (low->high)."""
    return np.array([float(mp.binomial(d,j)*a[n+j]) for j in range(d+1)], float)

def is_hyperbolic(coeffs):
    """all roots real? (coeffs low->high). returns (bool, max |Im root|)."""
    r = np.roots(coeffs[::-1])
    return (np.max(np.abs(r.imag)) < 1e-6*max(1,np.max(np.abs(r))), np.max(np.abs(r.imag)))

if __name__ == "__main__":
    print("="*78)
    print(" M11.1 — Jensen polynomials of the Riemann Xi: hyperbolicity (RH <=> all hyperbolic)")
    print("="*78)
    M = 11
    print(" computing Xi Taylor coefficients a(k)=Xi^{(2k)}(0)/(2k)! ...")
    a = xi_taylor_even(M)
    print(" first few a(k):")
    for k in range(6):
        print("   a(%d) = %s"%(k, mp.nstr(a[k], 8)))
    # sign pattern: for Laguerre-Polya (RH), the a(k) should be a Polya frequency / log-concave-ish sequence
    print("\n sign(a(k)) (k=0..%d):"%(M-1))
    print("  ", [int(mp.sign(a[k])) for k in range(M)])
    # Turan / log-concavity check: a(k)^2 - a(k-1)a(k+1) (Laguerre-Polya needs Turan >=0)
    print(" Turan a(k)^2 - a(k-1)a(k+1) >= 0 (Laguerre-Polya necessary):")
    print("  ", [float(a[k]**2 - a[k-1]*a[k+1] > 0) for k in range(1,M-1)])

    print("\n Hyperbolicity of Jensen polynomials J^{d,n} (real-rooted => consistent with RH):")
    print("   d    n     hyperbolic?   max|Im root|")
    for d in [2,3,4,5]:
        for n in [0,2,5,10,20]:
            if n+d >= M: continue
            cf = jensen_poly(a, d, n)
            hyp, mi = is_hyperbolic(cf)
            print("   %d   %2d      %-5s        %.2e"%(d,n,str(hyp),mi))
    print("\n  -> GORZ: for each fixed d, hyperbolic for all large n; roots -> Hermite H_d (GUE). RH = ALL hyperbolic.")
    print("     The open part is UNIFORMITY in d -- the target for stable-polynomial / interlacing machinery.")
    print("="*78)
