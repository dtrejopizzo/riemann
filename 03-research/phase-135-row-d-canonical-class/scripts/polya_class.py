#!/usr/bin/env python3
"""polya_class.py -- phase 135, task D.6(ii).

Checks on the canonical class K (Polya's kernel), Phi_K = xi:

  C1  K is even:  K(t) = K(-t) from the literal series on both sides.
  C2  K > 0 on a grid of [-2,2] (Polya's positivity, CLASSICAL; checked, not proved).
  C3  Phi_K(s) = xi(s) at s = 0, 1, 1/2, 3/2, 1/2+10i.
  C4  Phi_K(0) = Phi_K(1) = xi(0) = xi(1) = 1/2, so M(K) = (1/2,1/2) and deg K = 1.
  C5  int K = Phi_K(1/2) = xi(1/2) = 0.4971207782...
  C6  the explicit formula of Paper 45 (9.6a) holds for the NON-compactly
      supported test h = K, both sides computed independently:
         sum_rho Phi_K(rho) = 0   (each term is xi(rho) = 0)
         Phi_K(0)+Phi_K(1) + ARCH - PRIME = 0 ,
      hence T_infty(K) = PRIME - ARCH = 1.
  C7  I_infty(K,K) = 2 Phi_K(0)Phi_K(1) - sum_rho xi(rho)xi(1-rho) = 1/2, checked
      against the geometric side for h = K*K.

NUMERICS ILLUSTRATE AND FALSIFY; THEY PROVE NOTHING.  NO SIGN IS CLAIMED.
"""
import argparse
import sys

import mpmath as mp

from r135_common import K, Kraw, xi, arch_term, prime_term

TOL = mp.mpf('1e-18')


def run(check):
    mp.mp.dps = 25
    ok = True
    out = []

    def rec(name, got, want, tol=TOL):
        nonlocal ok
        d = abs(mp.mpmathify(got) - mp.mpmathify(want))
        good = d <= tol
        ok = ok and good
        out.append("%-46s %-26s %-26s %-10s %s" %
                   (name, mp.nstr(got, 15), mp.nstr(want, 15), mp.nstr(d, 3),
                    "ok" if good else "FAIL"))

    print("== C1  evenness of K (literal series at +t and -t) ==")
    for t in ['0.3', '0.5', '1.0']:
        rec("K(%s) - K(-%s)" % (t, t), Kraw(t, 120) - Kraw('-' + t, 120), 0, mp.mpf('1e-25'))
    print("\n".join(out)); out.clear()

    print("\n== C2  K > 0 on a grid (Polya; CLASSICAL, checked not proved) ==")
    vals = [(mp.mpf(i) / 20, K(mp.mpf(i) / 20)) for i in range(-40, 41)]
    mn = min(v for _, v in vals)
    pos = mn > 0
    ok = ok and pos
    print("  grid t = -2.0(0.05)2.0 :  min K = %s   %s" %
          (mp.nstr(mn, 8), "ok (all > 0)" if pos else "FAIL"))
    print("  K(0) = %s   K(0.5) = %s   K(1) = %s   K(2) = %s" %
          (mp.nstr(K(0), 10), mp.nstr(K('0.5'), 10), mp.nstr(K(1), 10), mp.nstr(K(2), 10)))

    print("\n== C3/C4/C5  Phi_K = xi ==")
    for s in [mp.mpf(0), mp.mpf(1), mp.mpf(1) / 2, mp.mpf(3) / 2, mp.mpf(1) / 2 + 10j]:
        v = mp.quad(lambda t: K(t) * mp.e ** ((s - mp.mpf(1) / 2) * t), [-3, -1, 0, 1, 3])
        rec("Phi_K(%s)" % mp.nstr(s, 6), v, xi(s), mp.mpf('1e-15'))
    print("\n".join(out)); out.clear()
    degK = xi(0) + xi(1)
    rec("deg K = Phi_K(0)+Phi_K(1)", degK, 1)
    rec("int K = Phi_K(1/2) = xi(1/2)", mp.quad(lambda t: K(t), [-3, -1, 0, 1, 3]),
        xi(mp.mpf(1) / 2), mp.mpf('1e-15'))
    rec("I_infty(K,K) = 2 Phi_K(0)Phi_K(1)", 2 * xi(0) * xi(1), mp.mpf(1) / 2)
    print("\n".join(out)); out.clear()

    print("\n== C6  explicit formula (Paper 45 (9.6a)) for the test h = K ==")
    Xi = lambda tau: mp.re(xi(mp.mpf(1) / 2 + 1j * tau))
    arch = arch_term(Xi, tau_max=200)
    pr = prime_term(lambda t: K(t), 60)
    print("  ARCH  = %s" % mp.nstr(arch, 16))
    print("  PRIME = %s" % mp.nstr(pr, 16))
    rec("Phi_K(0)+Phi_K(1)+ARCH-PRIME  (= sum_rho xi(rho) = 0)", 1 + arch - pr, 0, mp.mpf('1e-20'))
    rec("T_infty(K) = PRIME - ARCH", pr - arch, 1, mp.mpf('1e-20'))
    print("\n".join(out)); out.clear()

    print("\n== C7  explicit formula for h = K*K, giving I_infty(K,K) ==")
    KK = lambda t: mp.quad(lambda u: K(u) * K(mp.mpmathify(t) - u), [-3, -1, 0, 1, 3])
    Xi2 = lambda tau: mp.re(xi(mp.mpf(1) / 2 + 1j * tau)) ** 2
    arch2 = arch_term(Xi2, tau_max=200)
    pr2 = prime_term(KK, 40)
    print("  ARCH  = %s" % mp.nstr(arch2, 16))
    print("  PRIME = %s" % mp.nstr(pr2, 16))
    rec("I_infty(K,K) = PRIME - ARCH", pr2 - arch2, mp.mpf(1) / 2, mp.mpf('1e-13'))
    print("\n".join(out)); out.clear()

    print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
    return 0 if ok or not check else 1


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='exit non-zero unless every printed check passes')
    a = ap.parse_args()
    sys.exit(run(a.check))
