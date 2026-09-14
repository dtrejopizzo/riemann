#!/usr/bin/env python3
"""canonical_pairings.py -- phase 135, tasks D.6(ii),(iv), D.7(i).

Every pairing below is computed TWICE and compared:

  * the GEOMETRIC side, I_infty(F,G) = <F * G^vee, W_fin + omega_infty>,
    evaluated as PRIME - ARCH of Paper 45 (9.6a) -- this is the definition,
    and it mentions no zero of zeta;
  * the RULING side predicted by the theorems of Paper 46 section 11.

Checks:
  P1  I_infty(F,K) = (1/2) deg F,  for F a bump (deg > 0) and for F = Pi(bump)
      (primitive, deg 0, so the prediction is exactly 0).
  P2  I_infty(F, tau_{log n} K) = (1/2)(n^{1/2}Phi_F(0) + n^{-1/2}Phi_F(1)),
      n = 2,3,4: the Frobenius acts on K through the rulings only, with
      weights n^{+-1/2}.
  P3  the comparison identity (9.9) on a primitive compactly supported F,
      geometric side against the zero sum over the first NZ zeta zeros
      (mpmath.zetazero).  THIS IS A TEST OF AN IDENTITY, NOT EVIDENCE FOR A SIGN.
  P4  Pi K and tau_{log 2} Pi K lie in the radical: I_infty(Pi K, F) = 0 and
      I_infty(tau_{log2} Pi K, F) = 0 on the test functions of P1-P2.

[phase 135, R135_004]  REWRITTEN.  The round-1 version nested mpmath
quadratures inside one another: the archimedean integral was a tanh-sinh rule
over [-80,80] whose integrand carried the oscillatory factor n^{-i tau} of a
translate and was itself a tanh-sinh quadrature.  That rule does not resolve an
oscillation of period 2 pi / log n, which is why P2 failed by 0.6 at n = 4, and
the nesting is why the run exceeded 2400 s.  Here the tau-integral and the
t-integrals are fixed composite Gauss-Legendre panels (exponentially accurate
for analytic integrands, and panel width 1 resolves the oscillation), the
zeta-dependent node data Xi(tau) and Re psi(1/4+i tau/2) - log pi are computed
once in mpmath at 25 digits, and the rest is float64.  `--fast` shrinks the
panel counts.

NUMERICS ILLUSTRATE AND FALSIFY; THEY PROVE NOTHING.  NO SIGN IS CLAIMED.
"""
import argparse
import sys

import mpmath as mp
import numpy as np

from r135_common import Kf, PiKf, bumpf, Pibumpf, gl_panels, vonmangoldt, xi

TMAX = 70.0
TMAX3 = 400.0       # P3 has no Xi(tau) damping; see the comment there          # Xi(tau) ~ e^{-pi|tau|/4}: 4e-24 at tau = 70
NPRIME = 160         # prime sum cut-off; a translate by log n shifts the effective
                     # cut-off by a factor n, so this must clear e^{2.5} * max n


def node_data(ntau, order, tmax=TMAX, want_xi=True):
    """tau-nodes, weights, and the zeta-dependent factors, from mpmath."""
    tau, w = gl_panels(-tmax, tmax, ntau, order)
    mp.mp.dps = 25
    Xi = np.zeros_like(tau)
    Wt = np.empty_like(tau)
    for j, t in enumerate(tau):
        if want_xi:
            Xi[j] = float(mp.re(xi(mp.mpf(1) / 2 + 1j * mp.mpf(float(t)))))
        Wt[j] = float(mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * mp.mpf(float(t)) / 2))
                      - mp.log(mp.pi))
    return tau, w, Xi, Wt


class Test:
    """A real even compactly supported test F, with Phi_F on the critical line
    precomputed at the tau-nodes."""

    def __init__(self, name, f, tau, nt, order):
        self.name = name
        t, w = gl_panels(-1.0, 1.0, nt, order)
        self.t, self.w, self.v = t, w, f(t)
        # Phi_F(1/2 + i tau) = int F(t) e^{i tau t} dt
        self.Phi = (self.w * self.v) @ np.exp(1j * np.outer(t, tau))
        self.Phi0 = float((self.w * self.v) @ np.exp(-0.5 * t))
        self.Phi1 = float((self.w * self.v) @ np.exp(0.5 * t))

    def h(self, x, G):
        """(F * G^vee)(x) = int F(u) G(u-x) du."""
        x = np.atleast_1d(np.asarray(x, dtype=float))
        return np.array([float((self.w * self.v) @ G(self.t - xx)) for xx in x])


def geometric(F, G, symbol, tau, w, Xi, Wt):
    """PRIME - ARCH for h = F * G^vee, where symbol(tau) = Phi_G(1/2 - i tau)
    divided by Xi(tau) (a pure phase times a polynomial)."""
    hhat = F.Phi * symbol * Xi
    arch = float(np.sum(w * hhat.real * Wt)) / (2 * np.pi)
    ns = [n for n in range(2, NPRIME + 1) if vonmangoldt(n) != 0]
    logs = np.array([float(mp.log(n)) for n in ns])
    hp = F.h(logs, G) + F.h(-logs, G)
    pr = float(sum(float(vonmangoldt(n)) * n ** -0.5 * hp[i] for i, n in enumerate(ns)))
    return pr - arch, pr, arch


def run(check, fast):
    ntau, otau, nt, ot = (70, 20, 48, 24) if fast else (140, 24, 96, 28)
    nt3 = 96 if fast else 160
    NZ = 60 if fast else 120
    ok = True
    rows = []

    def rec(name, got, want, tol):
        nonlocal ok
        d = abs(got - want)
        good = d <= tol
        ok = ok and good
        rows.append("%-52s %-22s %-22s %-9s %s" %
                    (name, "%.12g" % got, "%.12g" % want, "%.2e" % d,
                     "ok" if good else "FAIL"))

    tau, w, Xi, Wt = node_data(ntau, otau)
    tests = [Test('bump', bumpf, tau, nt, ot), Test('Pi(bump)', Pibumpf, tau, nt, ot)]

    print("== test classes (%s mode: %d x %d tau-panels, %d x %d t-panels) ==" %
          ("fast" if fast else "full", ntau, otau, nt, ot))
    for F in tests:
        print("  %-10s  Phi(0) = %-16.10g Phi(1) = %-16.10g deg = %.10g" %
              (F.name, F.Phi0, F.Phi1, F.Phi0 + F.Phi1))
    pk = Test('Pi K', PiKf, tau, nt, ot)
    print("  Pi K     :  Phi(0) = %-16.4g Phi(1) = %-16.4g deg = %.4g"
          % (pk.Phi0, pk.Phi1, pk.Phi0 + pk.Phi1))

    one = np.ones_like(tau, dtype=complex)

    # ---- P1 ---------------------------------------------------------------
    print("\n== P1  I_infty(F,K) = (1/2) deg F  (geometric side vs ruling side) ==")
    for F in tests:
        got, pr, ar = geometric(F, Kf, one, tau, w, Xi, Wt)
        want = (F.Phi0 + F.Phi1) / 2
        rec("I_infty(%s, K)" % F.name, got, want, 1e-12)
    print("\n".join(rows)); rows.clear()

    # ---- P2 ---------------------------------------------------------------
    print("\n== P2  I_infty(F, tau_{log n} K): ruling weights n^{+-1/2} ==")
    for n in [2, 3, 4]:
        a = np.log(n)
        # Phi_{tau_a K}(1/2 - i tau) = e^{-i tau a} Xi(tau)
        sym = np.exp(-1j * tau * a)
        G = (lambda a: (lambda x: Kf(x - a)))(a)
        for F in tests:
            got, pr, ar = geometric(F, G, sym, tau, w, Xi, Wt)
            want = (np.sqrt(n) * F.Phi0 + F.Phi1 / np.sqrt(n)) / 2
            rec("I_infty(%s, tau_{log %d} K)" % (F.name, n), got, want, 1e-12)
    print("\n".join(rows)); rows.clear()

    # ---- P4 ---------------------------------------------------------------
    print("\n== P4  Pi K and tau_{log 2} Pi K are in the radical N_infty ==")
    for lab, a in [('Pi K', 0.0), ('tau_{log 2} Pi K', float(np.log(2)))]:
        # Phi_{tau_a Pi K}(1/2 - i tau) = e^{-i tau a}(1/4 + tau^2) Xi(tau)
        sym = np.exp(-1j * tau * a) * (0.25 + tau ** 2)
        G = (lambda a: (lambda x: PiKf(x - a)))(a)
        for F in tests:
            got, pr, ar = geometric(F, G, sym, tau, w, Xi, Wt)
            rec("I_infty(%s, %s)" % (lab, F.name), got, 0.0, 1e-11)
    print("\n".join(rows)); rows.clear()

    # ---- P3 ---------------------------------------------------------------
    print("\n== P3  comparison identity (9.9) on the primitive test Pi(bump) ==")
    print("   (a TEST of an identity; zeros are used nowhere else)")
    # h = F * F^vee has hhat = |Phi_F|^2 and carries NO factor Xi(tau), so the
    # archimedean integral needs a far longer tau-range than P1/P2: |Phi_bump|
    # decays only like exp(-c sqrt(tau)) and is multiplied by (1/4+tau^2)^2.
    tau3, w3, _, Wt3 = node_data(int(TMAX3), 24, tmax=TMAX3, want_xi=False)
    Fp = Test('Pi(bump)', Pibumpf, tau3, nt3, 28)
    hhat = np.abs(Fp.Phi) ** 2
    arch = float(np.sum(w3 * hhat * Wt3)) / (2 * np.pi)
    ns = [n for n in range(2, NPRIME + 1) if vonmangoldt(n) != 0]
    logs = np.array([float(np.log(n)) for n in ns])
    hv = Fp.h(logs, Pibumpf) + Fp.h(-logs, Pibumpf)
    pr = float(sum(float(vonmangoldt(n)) * n ** -0.5 * hv[i] for i, n in enumerate(ns)))
    geo = pr - arch
    mp.mp.dps = 25
    zs = 0.0
    for j in range(1, NZ + 1):
        r = mp.zetazero(j)
        e1 = np.exp(complex(r - mp.mpf(1) / 2) * Fp.t)
        e2 = np.exp(complex(mp.mpf(1) / 2 - r) * Fp.t)
        zs += 2 * (((Fp.w * Fp.v) @ e1) * ((Fp.w * Fp.v) @ e2)).real
    print("  geometric side  I_infty = %.12g   (PRIME = %.10g, ARCH = %.10g)"
          % (geo, pr, arch))
    print("  -sum_rho (first %d pairs)  = %.12g" % (NZ, -zs))
    print("  difference (tail of the zero sum) = %.4g   (relative %.2e)"
          % (geo + zs, abs(geo + zs) / abs(geo)))
    tail_ok = abs(geo + zs) < 1e-3 * abs(geo)
    ok = ok and tail_ok
    print("  %s" % ("ok (tail below 1e-3 relative)" if tail_ok else "FAIL"))

    print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
    return 0 if ok or not check else 1


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--fast', action='store_true',
                    help='coarser panels and fewer zeros; finishes in seconds')
    a = ap.parse_args()
    sys.exit(run(a.check, a.fast))
