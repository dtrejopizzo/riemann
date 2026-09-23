"""R156_001: explicit odd witness for the prime-free model at T = (1/2)log 3.
F(t) = t on (-T,T).  Computes A_inf(F) = C0|F|^2 + int_0^inf (|F|^2 - c_F(u))K(u)du - 2 s(F)^2
(i) to high precision (mpmath quadrature, DIAGNOSTIC), and
(ii) an elementary UPPER bound using K(u) <= 1/u + 1/2 on (0,2T) and exact closed forms for
     C0 = -gamma - pi/2 - 3log2 - log pi, the tail int_{2T}^inf K = log coth(T/2) + pi - 2 arctan e^T,
     and s(F) = int t sinh(t/2) dt.  All integrals in (ii) are of polynomials: exact (sympy), then evaluated."""
import sympy as sp, mpmath as mp
mp.mp.dps = 40
u, t = sp.symbols('u t', real=True)
T = sp.log(3) / 2
F = t
c = sp.integrate(F * F.subs(t, t - u), (t, u - T, T))       # c_F(u), 0<=u<=2T
c0 = sp.simplify(c.subs(u, 0))
g = sp.expand(c0 - c)                                        # >= 0, polynomial, g(0)=0
s = sp.integrate(F * sp.sinh(t / 2), (t, -T, T))
C0 = -sp.EulerGamma - sp.pi / 2 - 3 * sp.log(2) - sp.log(sp.pi)
tail = sp.log(1 / sp.tanh(T / 2)) + sp.pi - 2 * sp.atan(sp.exp(T))
# (i) high precision
gf = sp.lambdify(u, g, 'mpmath')
Kf = lambda x: 1 / (2 * mp.sinh(x / 2)) + 1 / (2 * mp.cosh(x / 2))
Tn = mp.log(3) / 2
lev_body = mp.quad(lambda x: gf(x) * Kf(x), [0, Tn, 2 * Tn])
val = sp.N(C0 * c0 + c0 * tail - 2 * s**2, 40) + lev_body
print("||F||^2 =", sp.N(c0, 15), "  s(F) =", sp.N(s, 15))
print("A_inf(F)            (mpmath) =", mp.nstr(val, 15), "  ratio to ||F||^2 =", mp.nstr(val / sp.N(c0, 40), 10))
# (ii) elementary upper bound: int_0^{2T} g(u)(1/u + 1/2) du, exact
up_body = sp.integrate(sp.expand(g / u) + g / 2, (u, 0, 2 * T))
ub = sp.N(C0 * c0 + c0 * tail - 2 * s**2 + up_body, 30)
print("elementary upper bound on A_inf(F) =", ub)
print("exact upper-bound expression (sympy):", sp.simplify(C0 * c0 + c0 * tail - 2 * s**2 + up_body))
