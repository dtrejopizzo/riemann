"""Coordinator check: is <A_T F,F> = sum_rho h(gamma_rho) ?

Claim (derived, to be tested).  For F real, supported in I_T=(-T,T), PRIMITIVE
(M_-F = M_+F = 0 with M_± F = int F(t) e^{±t/2} dt), put
    Fhat(tau) = int F(t) e^{i tau t} dt ,  h(tau) = Fhat(tau) Fhat(-tau).
Then Weil's explicit formula reads exactly

    sum_rho h(gamma_rho)  =  <G_Gamma F,F> - m_0 ||F||^2
                              - 2 sum_n w_n Re<S_{log n} F,F>
                          =  <A_T F, F>,

because  Re psi(1/4+i tau/2) - log pi = g_Gamma(tau) - m_0  identically
(psi(1/4) = -gamma - pi/2 - 3 log 2), and the two pole terms h(±i/2) = M_+F M_-F
vanish by primitivity.  Under RH every gamma_rho is real and h(gamma_rho)=|Fhat|^2>=0.

run:  python3 W0_weil_identity.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import polygamma
import mpmath as mp

EULER = 0.5772156649015328606
M0 = math.log(math.pi) + EULER + math.pi/2 + 3*math.log(2)

T = 1.2                      # window half-width
NZ = 600                     # number of zeta zeros used

# ---- a smooth primitive test function on (-T,T) ------------------------------
# base bumps, then remove the two Tate moments to land in P_T
def bumps(t):
    x = t / T
    b = np.where(np.abs(x) < 1, (1 - x**2)**3, 0.0)
    return np.vstack([b, b*x, b*x*x])

def moments(coef):
    f = lambda t, k: bumps(np.array([t]))[k, 0]
    mm = [quad(lambda t: f(t, k)*math.exp(-t/2), -T, T, limit=200)[0] for k in range(3)]
    mp_ = [quad(lambda t: f(t, k)*math.exp(+t/2), -T, T, limit=200)[0] for k in range(3)]
    return np.array(mm), np.array(mp_)

mm, mpp = moments(None)
# coefficients c with c.mm = 0, c.mpp = 0  -> 1-dim solution in R^3
Mt = np.vstack([mm, mpp])
_, _, vt = np.linalg.svd(Mt)
c = vt[-1]
print("Tate moments of F:  M_- = %.3e   M_+ = %.3e" % (c @ mm, c @ mpp))

F = lambda t: float(c @ bumps(np.array([t]))[:, 0])

def Fhat(tau):
    """int F(t) e^{i tau t} dt, real part only needed (F even? not necessarily)."""
    re = quad(lambda t: F(t)*math.cos(tau*t), -T, T, limit=400)[0]
    im = quad(lambda t: F(t)*math.sin(tau*t), -T, T, limit=400)[0]
    return complex(re, im)

def habs(tau):
    z = Fhat(tau)
    return abs(z)**2                      # = Fhat(tau)Fhat(-tau) for real F

nrm2 = quad(lambda t: F(t)**2, -T, T, limit=400)[0]
print("||F||^2 = %.10f" % nrm2)

# ---- left-hand side: the operator ------------------------------------------
def g_gamma(tau):
    return float(mp.re(mp.digamma(mp.mpf('0.25') + 1j*tau/2)) - mp.digamma(mp.mpf('0.25')))

gam = quad(lambda tau: g_gamma(tau)*habs(tau), 0, 400, limit=600)[0] * 2/(2*math.pi)
print("<G_Gamma F,F> = %.10f" % gam)

def autocorr(a):
    return quad(lambda t: F(t)*F(t+a), -T, T-a if a > 0 else T, limit=400)[0]

def vm(N):
    lam = [0.0]*(N+1); s = [True]*(N+1)
    for p in range(2, N+1):
        if s[p]:
            for m in range(p*p, N+1, p): s[m] = False
            q, lp = p, math.log(p)
            while q <= N: lam[q] = lp; q *= p
    return lam

Nmax = int(math.exp(2*T))
lam = vm(max(Nmax, 2))
prime_sum = 0.0
for n in range(2, Nmax+1):
    if lam[n] > 0 and math.log(n) < 2*T:
        w = lam[n]/math.sqrt(n)
        prime_sum += w * autocorr(math.log(n))
print("window N < e^{2T} = %.4f ; contacts used: %s"
      % (math.exp(2*T), [n for n in range(2, Nmax+1) if lam[n] > 0 and math.log(n) < 2*T]))

LHS = gam - M0*nrm2 - 2*prime_sum
print("\nLHS  <A_T F,F> = %.12f" % LHS)

# ---- right-hand side: sum over zeta zeros -----------------------------------
mp.mp.dps = 20
tot = 0.0
gammas = []
for k in range(1, NZ+1):
    g = float(mp.im(mp.zetazero(k)))
    gammas.append(g)
    tot += 2*habs(g)                      # rho and conjugate
    if k in (1, 5, 20, 100, 300, 600):
        print("  after %4d zeros (gamma=%9.3f): partial = %.12f" % (k, g, tot))
print("\nRHS  sum_rho h(gamma_rho) = %.12f   (%d zeros, up to gamma=%.1f)"
      % (tot, NZ, gammas[-1]))
print("difference = %.3e    relative = %.3e" % (LHS-tot, (LHS-tot)/abs(LHS)))
