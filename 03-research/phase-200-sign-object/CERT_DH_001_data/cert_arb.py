#!/usr/bin/env python3
"""CERT_DH_001: rigorous (arb ball arithmetic, python-flint) evaluation of a^DH_T(F)/||F||^2 for ONE explicit test F in P_T.
F(t) = G(t/T), G = G0 + lam1*x (+ lam0) with G0 in Q[x] exact (dyadic Legendre coefficients -> exact monomials) and
lam1 (lam0) solved in balls from int F sinh(t/2) = 0 (int F cosh(t/2) = 0), so F lies EXACTLY in P_T (the true lam is in the ball).
  a^DH_T(F) = C0 c(0) + int_0^{2T}(c(0)-c(u))K(u)du + c(0) int_{2T}^inf K - sum_{2<=n<e^{2T}} (2 b_n/sqrt n) c(log n),
  c(u) = int F(t)F(t-u)dt = T*P(u/T), P(s) = int_{-1}^{1} G(x)G(x-s)dx  (exact Q-polynomial pieces, Taylor in s),
  C0 = log5 - log pi - gamma + pi/2 - 3log2,  K(u) = 2 sum_k e^{-a_k u}, a_k = 2k+3/2,
  M_r := int_0^{2T} u^r K = r! 2^{-r} zeta(r+1,3/4) - 2 sum_k Gamma(r+1, 2T a_k)/a_k^{r+1}  (k-sum truncated with explicit bound),
  b_n: -F'/F = sum b_n n^{-s}, b_n = a_n log n - sum_{d|n,1<d<n} a_d b_{n/d}, a_n = Re chi(n) + kappa Im chi(n).
Usage: cert_arb.py vec.json Tnum Tden DENBITS PREC"""
import sys, json
from flint import arb, fmpq, fmpq_poly, ctx
from fractions import Fraction
X = fmpq_poly([0, 1])
def cross(A, B):  # P_{A,B}(s) = int_{s-1}^{1} A(x) B(x-s) dx, s in [0,2], exact; B(x-s) = sum_k (-s)^k B^(k)(x)/k!
    out = fmpq_poly(0); Bk = B; fact = 1; S1 = X - 1
    for k in range(B.degree() + 1):
        H = (A * Bk).integral(); term = (H(fmpq(1)) - H(S1)) * fmpq(1, fact)
        out += term * fmpq_poly([0, -1]) ** k
        Bk = Bk.derivative(); fact *= (k + 1)
    return out
def exp_moment(G, c):  # int_{-1}^{1} G(x) e^{cx} dx = sum_k (-1)^k [G^(k)(x) e^{cx}]_{-1}^{1} / c^{k+1}  (exact finite sum)
    s = arb(0); D = G; k = 0; ep, em = c.exp(), (-c).exp()
    while not D.is_zero():
        s += (-1) ** k * (arb(D(fmpq(1))) * ep - arb(D(fmpq(-1))) * em) / c ** (k + 1); D = D.derivative(); k += 1
    return s
def peval(P, x):  # Horner in arb
    v = arb(0)
    for c in reversed(P.coeffs()): v = v * x + arb(c)
    return v
def main():
    vec = json.load(open(sys.argv[1])); T = fmpq(int(sys.argv[2]), int(sys.argv[3])); nb = int(sys.argv[4]); ctx.prec = int(sys.argv[5])
    Ta = arb(T); sector = vec['sector']; den = 2 ** nb
    leg = {int(j): Fraction(round(c * den), den) for j, c in vec['leg'].items()}
    G0 = fmpq_poly(0)
    for j, c in leg.items():
        if j in (0, 1): continue      # P_0, P_1 directions are re-solved from the moment conditions
        G0 += fmpq(c.numerator, c.denominator) * fmpq_poly.legendre_p(j)
    half = Ta / 2
    # odd part constraint (sinh) -> lam1 ; even part (cosh) -> lam0  [odd/even parts decouple]
    G0o = fmpq_poly([c if i % 2 else 0 for i, c in enumerate(G0.coeffs())]); G0e = G0 - G0o
    sh = lambda Gp: (exp_moment(Gp, half) - exp_moment(Gp, -half)) / 2
    ch = lambda Gp: (exp_moment(Gp, half) + exp_moment(Gp, -half)) / 2
    lam1 = -sh(G0o) / sh(X); lam0 = (-ch(G0e) / ch(fmpq_poly(1))) if sector.startswith('full') else arb(0)
    one = fmpq_poly(1)
    pieces = {('0', '0'): cross(G0, G0), ('0', 'x'): cross(G0, X) + cross(X, G0), ('x', 'x'): cross(X, X)}
    if sector.startswith('full'):
        pieces.update({('0', '1'): cross(G0, one) + cross(one, G0), ('1', '1'): cross(one, one), ('1', 'x'): cross(one, X) + cross(X, one)})
    w = {('0', '0'): arb(1), ('0', 'x'): lam1, ('x', 'x'): lam1 ** 2, ('0', '1'): lam0, ('1', '1'): lam0 ** 2, ('1', 'x'): lam0 * lam1}
    R = max(P.degree() for P in pieces.values())
    p = [arb(0)] * (R + 1)   # coefficients of P(s) in arb
    for key, P in pieces.items():
        for r, c in enumerate(P.coeffs()): p[r] += w[key] * arb(c)
    # --- constants
    C0 = arb(5).log() - arb.pi().log() - arb.const_euler() + arb.pi() / 2 - 3 * arb(2).log()
    ak = lambda k: arb(2 * k) + arb(3) / 2
    K1 = 200; tail = sum((2 * (-2 * Ta * ak(k)).exp() / ak(k) for k in range(K1)), arb(0))
    rem = 2 * (-2 * Ta * ak(K1)).exp() / (ak(K1) * (1 - (-4 * Ta).exp())); tail += arb(0, rem.upper())
    # --- Levy moments M_r, r = 1..R
    M = [None]
    for r in range(1, R + 1):
        full = arb.gamma(arb(r + 1)) * arb(2) ** (-r) * arb.zeta(arb(r + 1), arb(3) / 4)
        up = arb(0); k = 0
        while True:
            x = 2 * Ta * ak(k)
            if x > 2 * (r + 1) and k > 0:
                # remainder sum_{j>=k} Gamma(r+1,x_j)/a_j^{r+1} <= sum 2 x_j^r e^{-x_j}/a_j^{r+1} = 2 (2T)^r sum e^{-x_j}/a_j
                #   <= 2 (2T)^r e^{-x_k} / (a_k (1 - e^{-4T}))   [Gamma(r+1,x) <= 2 x^r e^{-x} for x >= 2(r+1)]
                b = 2 * (2 * Ta) ** r * (-x).exp() / (ak(k) * (1 - (-4 * Ta).exp()))
                if b.upper() < arb(2) ** (-ctx.prec): up += arb(0, b.upper()); break
            up += arb.gamma_upper(x, arb(r + 1)) / ak(k) ** (r + 1); k += 1
        M.append(full - 2 * up)
    # --- comb
    nmax = int((2 * Ta).exp().upper().floor().unique_fmpz()) + 1
    s5 = arb(5).sqrt(); kap = ((10 - 2 * s5).sqrt() - 2) / (s5 - 1)
    CHI = {1: (1, 0), 2: (0, 1), 3: (0, -1), 4: (-1, 0), 0: (0, 0)}
    a = lambda n: arb(CHI[n % 5][0]) + kap * CHI[n % 5][1]
    bn = {}; cont = []
    for n in range(2, nmax + 1):
        bn[n] = a(n) * arb(n).log() - sum((a(d) * bn[n // d] for d in range(2, n) if n % d == 0), arb(0))
        ln = arb(n).log()
        if ln < 2 * Ta: cont.append(n)
        else: assert ln > 2 * Ta, 'undecided contact'
    c0 = Ta * p[0]
    levy = -sum((Ta * p[r] * M[r] / Ta ** r for r in range(1, R + 1)), arb(0))
    def pval(sv):
        v = arb(0)
        for c in reversed(p): v = v * sv + c
        return v
    comb = sum((2 * bn[n] / arb(n).sqrt() * Ta * pval(arb(n).log() / Ta) for n in cont), arb(0))
    Q = (C0 * c0 + levy + c0 * tail - comb) / c0
    print(f"T={T} sector={sector} N={vec['N']} DENBITS={nb} prec={ctx.prec} #contacts={len(cont)} (n<={max(cont)})")
    print(f"  float64 Galerkin bottom: {vec['galerkin_float64']:.6e}")
    print(f"  lam1 = {lam1.str(10)}  lam0 = {lam0.str(10)}  ||F||^2 = {c0.str(15)}")
    print(f"  pieces/||F||^2: C0 {C0.str(12)}  levy+tail {((levy + c0 * tail) / c0).str(12)}  comb {(comb / c0).str(12)}")
    print(f"  CERT a^DH_T(F)/||F||^2 = {Q.str(15, radius=True)}   upper = {Q.upper().str(10)}   ->",
          'NEGATIVE: PROVED' if Q < 0 else 'NOT CERTIFIED')
    json.dump({'T': str(T), 'sector': sector, 'DENBITS': nb, 'legendre_numerators': {j: c.numerator for j, c in leg.items() if j > 1}},
              open(sys.argv[1].replace('.json', f'_witness_den2^{nb}.json'), 'w'))
main()
