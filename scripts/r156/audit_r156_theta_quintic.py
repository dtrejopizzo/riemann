"""R156_004 (hostile audit): interval-arithmetic re-verification of the odd-quintic witness of R156_001 Thm 3.3(ii).

T = (1/2) log 3, N_T = {2}, v_2 = 2 log 2 / sqrt 2.  One-contact family a_theta = Lambda - (1-theta) Lambda(2) 1_{n=2},
    W_theta(F) := A_inf(F) + theta * Pi(F),   Pi(F) = -v_2 c_F(log 2)      (P47 sec:archstr: W_T = A_inf + Pi_T).
Witness F = t + b3 t^3 + b5 t^5, b3 = -2634299/500000, b5 = 1919331/250000 (exact rationals).
Upper bound U0(F) >= A_inf(F): K(u) <= 1/u + 1/2 on (0,2T) against g = c_F(0) - c_F(u) >= 0 (Cauchy-Schwarz);
tail int_{2T}^inf K = log coth(T/2) + 2 arctan(e^{-T}); C0 = -gamma - pi/2 - 3log2 - log pi; odd F: 2AB = -2 s(F)^2.
Claims checked: U0 <= -0.0061378, Pi(F) = +0.0075328..., hence U0 + theta*Pi < 0 for every theta <= 0.8148.
Also re-checks the bare witness F = t (theta < 0.4741).
Method: sympy produces c_F(u) as an exact polynomial in (u, T) with rational coefficients, the integral
int_0^{2T} g(u)(1/u + 1/2) du as an exact polynomial in T, and s(F) as an exact combination of T^k cosh(T/2),
T^k sinh(T/2); each is then evaluated with T = iv.log(3)/2 in mpmath interval arithmetic (outward rounding).
Also a DIAGNOSTIC mpmath evaluation of the exact A_inf(F) (true Levy density) for comparison.  Runtime < 60 s.
"""
import sympy as sp
import mpmath as mp
from mpmath import iv

iv.dps = 50

def iv_atan_small(y, nterms=400):
    s = iv.mpf(0)
    for k in range(nterms):
        s += (-1) ** k * y ** (2 * k + 1) / (2 * k + 1)
    return s + iv.mpf([-1, 1]) * y ** (2 * nterms + 1) / (2 * nterms + 1)

t, u, T = sp.symbols('t u T', positive=True)

def pieces(F):
    c = sp.expand(sp.integrate(sp.expand(F * F.subs(t, t - u)), (t, u - T, T)))   # c_F(u), 0 <= u <= 2T
    c0 = sp.expand(c.subs(u, 0))
    g = sp.expand(c0 - c)
    assert sp.expand(g.subs(u, 0)) == 0
    body = sp.expand(sp.integrate(sp.expand(sp.cancel(g / u) + g / 2), (u, 0, 2 * T)))
    s = sp.expand(sp.integrate(sp.expand(F * (sp.exp(t / 2) - sp.exp(-t / 2)) / 2), (t, -T, T)))
    return c, c0, g, body, s

def ev(expr, env):
    # exact recursive interval evaluation of a sympy expression; rationals are converted exactly
    if expr.is_Rational:
        return iv.mpf(int(expr.p)) / iv.mpf(int(expr.q))
    if expr.is_Symbol:
        return env[expr]
    if expr.is_Add:
        r = iv.mpf(0)
        for a in expr.args: r += ev(a, env)
        return r
    if expr.is_Mul:
        r = iv.mpf(1)
        for a in expr.args: r *= ev(a, env)
        return r
    if expr.is_Pow:
        b, e = expr.args
        if e.is_Integer:
            return ev(b, env) ** int(e)
        if e == sp.Rational(1, 2):
            return iv.sqrt(ev(b, env))
        if e == sp.Rational(-1, 2):
            return 1 / iv.sqrt(ev(b, env))
    if isinstance(expr, sp.exp):
        return iv.exp(ev(expr.args[0], env))
    if isinstance(expr, sp.log):
        return iv.log(ev(expr.args[0], env))
    raise ValueError(f"unhandled {expr!r}")

def to_iv(expr, Tiv):
    return ev(sp.expand(expr), {T: Tiv})

Tiv = iv.log(3) / 2
C0 = -iv.euler - iv.pi / 2 - 3 * iv.log(2) - iv.log(iv.pi)
eT = iv.exp(Tiv)
tail = iv.log((eT + 1) / (eT - 1)) + 2 * iv_atan_small(iv.exp(-Tiv))
v2 = 2 * iv.log(2) / iv.sqrt(2)
L2 = iv.log(2)

for name, F in [("quintic", t - sp.Rational(2634299, 500000) * t**3 + sp.Rational(1919331, 250000) * t**5), ("F = t", t)]:
    c, c0, g, body, s = pieces(F)
    # sanity: g >= 0 on [0,2T] is Cauchy-Schwarz; spot-check numerically
    gnum = sp.lambdify((u, T), g, 'mpmath'); Tn = mp.log(3) / 2
    assert min(gnum(Tn * k / 50, Tn) for k in range(101)) >= -1e-30
    c0i = to_iv(c0, Tiv); bodyi = to_iv(body, Tiv); si = to_iv(s, Tiv)
    U0 = c0i * (C0 + tail) + bodyi - 2 * si ** 2
    # Pi(F) = -v2 c_F(log 2): substitute u = log 2 (log 2 < 2T) and evaluate in intervals
    Pi = -v2 * ev(c, {u: L2, T: Tiv})
    print(f"[{name}]  ||F||^2 in {c0i}")
    print(f"   U0 (upper bound on A_inf(F)) in {U0}")
    print(f"   Pi(F) = -v2 c_F(log 2)       in {Pi}")
    ratio = -U0 / Pi
    print(f"   -U0/Pi in {ratio}   (W_theta(F) < 0 for all theta below the lower end)")
    for th in ['0.8148', '0.4741']:
        val = U0 + iv.mpf(th) * Pi
        print(f"   U0 + {th}*Pi in {val}   negative: {val.b < 0}")
    # DIAGNOSTIC: exact A_inf with the true K (mpmath quadrature, not interval)
    mp.mp.dps = 30
    Kf = lambda x: 1 / (2 * mp.sinh(x / 2)) + 1 / (2 * mp.cosh(x / 2))
    lev = mp.quad(lambda x: gnum(x, Tn) * Kf(x), [0, Tn, 2 * Tn])
    exact = sp.lambdify((T,), c0 * (sp.log(1 / sp.tanh(T / 2)) + sp.pi - 2 * sp.atan(sp.exp(T))) - 2 * s**2, 'mpmath')(Tn) \
        + sp.lambdify((T,), c0, 'mpmath')(Tn) * (mp.digamma(0.25) - mp.log(mp.pi)) + lev
    print(f"   DIAGNOSTIC exact A_inf(F) = {mp.nstr(exact, 12)}")
