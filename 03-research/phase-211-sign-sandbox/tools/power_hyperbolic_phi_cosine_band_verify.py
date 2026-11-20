"""Certify the explicit bilateral Phi cosine integral is negative on [17,41/2].

192-bit Arb integration; four theta modes on [0,2]; 48 frequency Taylor
coefficients centered at 75/4; sixteen exact Bernstein intervals.  The
infinite theta tail, temporal tail and frequency Taylor remainder are all
included before the sign gate.  Only the explicit Phi series is evaluated.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
from flint import arb, acb, ctx

BITS, MODES, TERMS, OMEGA_PANELS, T_PANELS = 192, 4, 48, 16, 8
DEGREE = TERMS-1
ctx.prec = BITS


def ball(q):
    q = F(q)
    return arb(q.numerator)/q.denominator


pi = arb.pi()
assert pi > 3 and pi < 4
assert arb(3).exp() > 20
assert arb(1).exp() > ball(F(8, 3))

# For real t>=0, every omitted mode is bounded by
# 2*pi^2*n^4*exp(9t/2-pi*n^2*exp(2t)) <=32*n^4*exp(-3n^2).
# The upper envelope decreases with t.  From n=5 the term ratio is <1/2.
assert F(9, 2)-2*3*25 < 0
assert F(6, 5)**4/20**11 < F(1, 2)
E_THETA = F(256*5**4, 20**25)  # 2 * length[0,2] * complete modal tail

# At t=2, Y=pi*exp(4)>3*20*(8/3)=160.
# For X>=160, sum n^4 exp(-n^2 X)<=2 exp(-X).
# Substitution X=pi exp(2t) gives integral_2^inf Phi <=4Y^2 exp(-Y).
# Y^2 exp(-Y) is decreasing and exp(160)>2^160.  Include both real tails.
assert 3*20*F(8, 3) == 160
assert F(16, 20**3) < F(1, 2)
assert 160**2+2*160+2 < 2*160**2
E_TIME = F(8*160**2, 2**160)

# An elementary L1 bound, independent of any transform identity:
# 2*integral Phi <=2*sum(4n^2+3)exp(-3n^2)
# <=14exp(-3)/(1-4exp(-6))<56/63<1.
# The substitution v=exp(2t), v^(5/4)<=v^2 proves the first inequality.
assert 2+F(2, 3) < 3
assert 4+3 <= 4*(4+3)
assert F(14, 16)/(1-F(4, 16**2)) == F(56, 63) < 1
# Taylor about 75/4: |omega-75/4|<=7/4, t<=2.  The real cosine
# derivatives have modulus <=1.  The factor10 is deliberately generous.
E_OMEGA = 10*F(7, 2)**TERMS/factorial(TERMS)
E_TOTAL = E_THETA+E_TIME+E_OMEGA
assert E_THETA < F(1, 10**26)
assert E_TIME < F(1, 10**42)
assert E_OMEGA < F(1, 10**32)
assert E_TOTAL < F(1, 10**26)

OMEGA0 = ball(F(75, 4))
imag = acb(0, 1)
TOL = ball(F(1, 2**160))


def phi4(z):
    # A finite sum of entire functions: the analytic flag in acb.integral
    # needs no branch handling.  The missing infinite sum is paid above.
    y = pi*(2*z).exp()
    return pi*(5*z/2).exp()*sum(
        (n*n*(2*n*n*y-3)*(-n*n*y).exp()
         for n in range(1, MODES+1)), acb(0))


print('Fixed Phi cosine band certificate: bits=192 theta_modes=4', flush=True)
print('t=[0,2], eight fixed subintervals; omega=[17,41/2]', flush=True)
print('Frequency Taylor degree=47; Bernstein intervals=16', flush=True)
print('PASS analytic infinite-tail and Taylor-remainder gates', flush=True)
coeff = []
for k in range(TERMS):
    def integrand(z, analytic, order=k):
        return phi4(z)*z**order*(imag*OMEGA0*z).exp()/factorial(order)

    moment = acb(0)
    for j in range(T_PANELS):
        moment += acb.integral(
            integrand, acb(ball(F(j, 4))), acb(ball(F(j+1, 4))),
            rel_tol=TOL, abs_tol=TOL,
            deg_limit=64, eval_limit=100000, depth_limit=20)
    assert moment.is_finite(), ('inconclusive integral', k, moment)
    # The factor2 makes these coefficients BILATERAL throughout.
    ck = 2*(imag**k*moment).real
    assert ck.upper()-ck.lower() < ball(F(1, 2**140)), (
        'inconclusive coefficient enclosure', k, ck)
    coeff.append(ck)
    if (k+1) % 12 == 0:
        print('PASS enclosed frequency coefficients:', k+1, flush=True)

# Convert the same global Taylor polynomial to Bernstein form on each
# rational subinterval.  Every Bernstein coefficient is a certified ball.
# This is coverage of one declared band, not sampling of frequencies.
worst = None
for panel in range(OMEGA_PANELS):
    left = -F(7, 4)+F(7*panel, 32)
    width = F(7, 32)
    local = []
    for j in range(TERMS):
        local.append(ball(width**j)*sum(
            (coeff[k]*ball(comb(k, j)*left**(k-j))
             for k in range(j, TERMS)), arb(0)))
    for j in range(TERMS):
        bern = sum((local[k]*ball(F(comb(j, k), comb(DEGREE, k)))
                    for k in range(j+1)), arb(0))
        upper = bern+ball(E_TOTAL)
        assert upper < -ball(F(1, 10**8)), (
            'inconclusive Bernstein sign', panel, j, upper)
        if worst is None or upper.upper() > worst:
            worst = upper.upper()

print('PASS all 16 Bernstein intervals, including every remainder', flush=True)
print('Certified bilateral upper bound throughout band:', worst, flush=True)
print('Infinite theta error:', ball(E_THETA), flush=True)
print('Infinite temporal error:', ball(E_TIME), flush=True)
print('Frequency Taylor error:', ball(E_OMEGA), flush=True)
print('SHA256:', sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)
print('FULL PASS: integral_R Phi(t)cos(omega*t)dt < -1/10^8', flush=True)
print('For every real omega in [17,41/2]; explicit theta series only.', flush=True)
print('Scope: this fixed band and the comparator obstruction; no global sign.', flush=True)
