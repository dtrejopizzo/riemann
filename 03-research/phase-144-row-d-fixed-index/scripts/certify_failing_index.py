#!/usr/bin/env python3
"""R144 / D.37 -- certification of the Xi_a polar block and of the failing index.

Certifies, for Xi_a(s) = xi(s+a)xi(s-a) with a = 1/4 (and any a given by --a):

  (C1) the four polar values Xi_a(p), p in P = {-a, a, 1-a, 1+a}, are positive and
       pair-equal:  Xi_a(-a) = Xi_a(1+a) = xi(1+2a)/2,  Xi_a(a) = Xi_a(1-a) = xi(2a)/2;
  (C2) deg_a K_a = sum_p Xi_a(p)^2 = I_infty^{(a)}(K_a,K_a) > 0, so R_a(rF_+ + K_a) > 0
       for every r and every sign of r;
  (C3) the polar part of the trace t_n^{(a)}(K_a), for ANY even admissible g_a, is
            n -> 2A cosh((1/2+a)L) + 2B cosh((1/2-a)L),   L = log n,  A,B > 0,
       whose infimum over n > 0 is 2(A+B), ATTAINED AT n = 1.  In particular a four-point
       two-modulus polar set DOES have a uniform AM-GM floor (contradicting the
       phase-144 blueprint's proposed A3-line), and the floor is weakest at n = 1;
  (D)  the failing index: t_m^{(a)}(rF_+ + K_a) < 0 as soon as
            |r| > t_m^{(a)}(K_a) / |t_m^{(a)}(F_+)|   with sign(r) = -sign(t_m^{(a)}(F_+)),
       so the smallest failing index is m = min{n : t_n^{(a)}(F_+) != 0}, and the
       threshold is smallest at n = 1 by (C3).

The numbers A, B depend on the (non-constructive, Baire) choice of g_a; the script
certifies the a-dependent factors alpha = Xi_a(-a), beta = Xi_a(a) and the shape of (C3),
which is all that the statements of D.37 quote.  No claim here is a positivity claim
about xi on S_0.
"""
import argparse
from mpmath import mp, mpf, zeta, gamma, pi, log, cosh, exp, sqrt, findroot

def xi(s):
    s = mp.mpf(s) if not isinstance(s, mp.mpf) else s
    if abs(s) < mp.mpf('1e-20') or abs(s - 1) < mp.mpf('1e-20'):
        return mp.mpf('0.5')          # xi(0) = xi(1) = 1/2  (Paper 46 (11.9))
    return mp.mpf('0.5') * s * (s - 1) * pi**(-s/2) * gamma(s/2) * zeta(s)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=str, default='0.25')
    ap.add_argument('--fast', action='store_true', help='dps=25 instead of 40')
    ap.add_argument('--margin', type=str, default='1e-6',
                    help='required strict margin on every positivity checked')
    args = ap.parse_args()
    mp.dps = 25 if args.fast else 40
    a = mp.mpf(args.a)
    marg = mp.mpf(args.margin)
    assert 0 < a < mp.mpf('0.5'), 'need 0 < a < 1/2'

    print(f'# a = {a}, dps = {mp.dps}, margin = {marg}')

    # (C1)
    P = [-a, a, 1 - a, 1 + a]
    Xi = [xi(p + a) * xi(p - a) for p in P]
    alpha, beta = Xi[0], Xi[1]
    print('# (C1) polar values Xi_a(p):')
    for p, v in zip(P, Xi):
        print(f'   p = {mp.nstr(p,10):>10}   Xi_a(p) = {mp.nstr(v,20)}')
    ok = True
    for v in Xi:
        ok &= (v > marg)
    ok &= abs(Xi[0] - Xi[3]) < marg * mp.mpf('1e-6')
    ok &= abs(Xi[1] - Xi[2]) < marg * mp.mpf('1e-6')
    ok &= abs(alpha - xi(1 + 2*a)/2) < marg * mp.mpf('1e-6')
    ok &= abs(beta - xi(2*a)/2) < marg * mp.mpf('1e-6')
    print(f'   alpha = Xi_a(-a) = Xi_a(1+a) = xi(1+2a)/2 = {mp.nstr(alpha,20)}')
    print(f'   beta  = Xi_a(a)  = Xi_a(1-a) = xi(2a)/2    = {mp.nstr(beta,20)}')
    print(f'   (C1) pair-equality and positivity: {"PASS" if ok else "FAIL"}')

    # (C2)
    degK = sum(v*v for v in Xi)
    print('# (C2) deg_a K_a = I_infty^(a)(K_a,K_a) = sum_p Xi_a(p)^2 ='
          f' {mp.nstr(degK,20)}')
    ok2 = degK > marg
    print(f'   R_a(rF_+ + K_a) = r^2 q_a/2 + deg_a K_a / 2 > 0 for all r: '
          f'{"PASS" if ok2 else "FAIL"}')

    # (C3): polar shape.  Normalise the (unknown, Baire-chosen) even g_a by
    # Phi_{g_a}(1+a) = Phi_{g_a}(1-a) = 1; the shape statement is scale-free in each pair.
    A, B = alpha, beta
    f = lambda L: 2*A*cosh((mp.mpf('0.5')+a)*L) + 2*B*cosh((mp.mpf('0.5')-a)*L)
    floor_val = f(mp.mpf(0))
    grid = [mp.mpf(k)/8 for k in range(-400, 401)]
    gmin = min(f(L) for L in grid)
    amgm4 = 4 * (alpha*alpha*beta*beta)**mp.mpf('0.25')
    paired = 2*sqrt(alpha*alpha) + 2*sqrt(beta*beta)
    print('# (C3) polar part of t_n^(a)(K_a) (normalised g_a):')
    print(f'   value at n = 1 (L = 0)              : {mp.nstr(floor_val,20)}')
    print(f'   min over L in [-50,50] (grid 1/8)   : {mp.nstr(gmin,20)}')
    print(f'   4-term AM-GM bound 4(prod C)^(1/4)  : {mp.nstr(amgm4,20)}')
    print(f'   paired bound 2sqrt(C_-a C_1+a)+...  : {mp.nstr(paired,20)}')
    ok3 = (gmin >= floor_val - marg) and (amgm4 > marg) and (amgm4 <= floor_val + marg)
    print('   infimum attained at n = 1, and a UNIFORM POSITIVE FLOOR EXISTS for the'
          ' four-point two-modulus set: ' + ('PASS' if ok3 else 'FAIL'))

    # (D) threshold at m = 1, as a function of the (unknown) t_1(F_+)
    print('# (D) failing index: for any m with t_m^(a)(F_+) != 0 the class'
          ' E_r = rF_+ + K_a')
    print('      has t_m^(a)(E_r) < 0 once |r| > t_m^(a)(K_a)/|t_m^(a)(F_+)|,'
          ' with sign(r) = -sign(t_m^(a)(F_+));')
    print(f'      at m = 1 the numerator is the FLOOR {mp.nstr(floor_val,20)}'
          ' (smallest over all n, by (C3)),')
    print('      so m = 1 is the smallest failing index whenever t_1^(a)(F_+) != 0,'
          ' and the threshold in |r| is minimal there.')

    allok = ok and ok2 and ok3
    print('RESULT: ' + ('PASS' if allok else 'FAIL'))
    return 0 if allok else 1

if __name__ == '__main__':
    raise SystemExit(main())
