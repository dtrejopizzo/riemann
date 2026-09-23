"""R154 round 2, script 3: the Kwasnicki phase shift.

Formula used (Kwasnicki, Studia Math. 206 (2011) 211-271, "Spectral analysis of subordinate
Brownian motions on the half-line", Thm 1.1 / eq. (1.5); same object as the constant
(2-alpha)*pi/8 of Kulczycki-Kwasnicki-Malecki-Stos 2010 for the alpha-stable case):

   theta(mu) = (1/pi) PV int_0^infty  mu/(mu^2 - s^2) * log( (psi(s) - psi(mu))/(s^2 - mu^2) ) ds

with psi the (even, CBF-type) Levy exponent, psi(xi) = phi(xi^2).  Two-term eigenvalue law on
(-T,T):   lambda_n ~ psi(mu_n),  mu_n = (n*pi/2 - theta(mu_n))/T,  error O(1/n).

TEST 1: psi(xi)=|xi|^alpha must give theta = (2-alpha)*pi/8 for every alpha in (0,2].
TEST 2: Cauchy process (alpha=1) on (-1,1): lambda_n vs the literature values
        1.157773, 2.754795, 4.316730, 5.892243 (KKMS 2010, Table 1).
"""
import math, numpy as np
from scipy.special import psi as dg
from scipy.integrate import quad

def theta(psi, mu, dpsi=None, lim=200):
    """PV integral; the integrand is regular at s=mu (log -> log(psi'(mu)/(2mu)))."""
    def f(s):
        if abs(s-mu) < 1e-7:
            d = dpsi(mu) if dpsi else (psi(mu+1e-5)-psi(mu-1e-5))/2e-5
            g = math.log(d/(2*mu))
        else:
            g = math.log((psi(s)-psi(mu))/(s*s-mu*mu))
        return g
    # split:  int mu/(s^2-mu^2) * g(s) ds ; PV handled by writing g(s) = g(mu) + (g(s)-g(mu))
    # and using PV int_0^inf mu/(s^2-mu^2) ds = 0.
    gm = f(mu)
    def h(s): return mu*(f(s)-gm)/(mu*mu-s*s)
    tot = 0.0
    pts = [0, mu/2, mu, 2*mu, 5*mu, 20*mu, 200*mu, 1e4*mu, 1e7*mu]
    for a, b in zip(pts[:-1], pts[1:]):
        tot += quad(h, a, b, limit=400)[0]
    return tot/math.pi

print("TEST 1: alpha-stable, theta should be (2-alpha)*pi/8")
for al in (0.5, 1.0, 1.5, 1.9, 2.0):
    ps = lambda s, al=al: s**al
    dp = lambda s, al=al: al*s**(al-1)
    for mu in (1.0, 3.7):
        t = theta(ps, mu, dp)
        print(f"  alpha={al} mu={mu}: theta={t:.8f}  target={(2-al)*math.pi/8:.8f}  err={t-(2-al)*math.pi/8:.2e}")

print("TEST 2: Cauchy on (-1,1), two-term law lambda_n = n*pi/2 - pi/8")
lit = [1.157773, 2.754795, 4.316730, 5.892243]
for n, lv in enumerate(lit, 1):
    pred = n*math.pi/2 - math.pi/8
    print(f"  n={n}: law={pred:.6f} true={lv:.6f} err={pred-lv:+.5f} rel={abs(pred-lv)/lv:.2e}")

# ---- our phi ----
PSI0 = float(dg(0.25))
def psi_ours(s): return float(np.real(dg(0.25+0.5j*s))) - PSI0
def dpsi_ours(s, h=1e-5): return (psi_ours(s+h)-psi_ours(s-h))/(2*h)

print("\nOUR phi: theta(mu)")
for mu in (2.0, 4.0, 6.8, 10.0, 20.0, 50.0):
    print(f"  mu={mu}: theta={theta(psi_ours, mu, dpsi_ours):.8f}")

print("\nTwo-term prediction for the killed archimedean process on (-T,T)")
for T in (0.5*math.log(3), math.log(2)):
    for n in (1,2,3,4,5,6):
        mu = n*math.pi/(2*T)
        for _ in range(40):
            mu = (n*math.pi/2 - theta(psi_ours, mu, dpsi_ours))/T
        print(f"  T={T:.6f} n={n}: mu_n={mu:.6f} theta={theta(psi_ours,mu,dpsi_ours):.6f} lambda_n~{psi_ours(mu):.8f}")

print("\nComparison with Galerkin (K=700, taumax=2e4) killed-process eigenvalues")
TRUE = {0.5*math.log(3): [3.536519,4.990222,5.492692,5.838735,6.086964,6.290469],
        math.log(2):     [3.243610,4.749750,5.258975,5.605308,5.854046,6.057595]}
for T, tv in TRUE.items():
    for n in range(1, 7):
        mu = n*math.pi/(2*T)
        for _ in range(60):
            mu = max(1e-3, (n*math.pi/2 - theta(psi_ours, mu, dpsi_ours))/T)
        lam = psi_ours(mu)
        print(f"  T={T:.6f} n={n}: theta={theta(psi_ours,mu,dpsi_ours):.6f} mu_n={mu:.6f} "
              f"law={lam:.6f} true={tv[n-1]:.6f} err={lam-tv[n-1]:+.6f} rel={abs(lam-tv[n-1])/tv[n-1]:.2e}")
