"""R186_030 — decide la clase B (certificados duales (nu,2,0) con nu >= 0, 'Bochner'):
(1) valor sup_{nu>=0} inf_tau f por LP discreto (cota orientativa);
(2) cota superior RIGUROSA (modulo cuadratura) por tests primales relajados
    Phi = e^{-a u^2} - b e^{-beta u^2}, Phi^ >= 0, Phi <= 0 en |u| >= 2T.
Convenciones de Paper 47: m = Re psi(1/4+i tau/2) - log pi, C0 = psi(1/4) - log pi,
K(u) = 2e^{3u/2}/(e^{2u}-1), v_n = 2 Lambda(n)/sqrt n, g0^ = 2 int_0^{2T} cosh(u/2) cos(tau u).
"""
import numpy as np
from scipy.special import psi
from scipy.integrate import quad
from scipy.optimize import linprog
from sympy import factorint

def m(t):
    return np.real(psi(0.25 + 0.5j*np.asarray(t, dtype=float))) - np.log(np.pi)
C0 = float(psi(0.25)) - np.log(np.pi)
def K(u): return 2*np.exp(-u/2)/(1-np.exp(-2*u))   # = 2e^{3u/2}/(e^{2u}-1), forma estable
def contacts(T):
    out = []
    for n in range(2, int(np.exp(2*T))+2):
        if np.log(n) < 2*T:
            f = factorint(n)
            if len(f) == 1:
                p = list(f)[0]; out.append((n, 2*np.log(p)/np.sqrt(n)))
    return out
def g0hat(t, T):
    t = np.asarray(t, float); u = np.linspace(0, 2*T, 4001)
    return 2*np.trapz(np.cosh(u/2)[None,:]*np.cos(np.outer(t, u)), u, axis=1)
def khat(t, T, N):
    return m(t) - sum(v*np.cos(t*np.log(n)) for n, v in N) + 2*g0hat(t, T)

def lp_classB(T, N, umax=30.0, nu=600, tmax=200.0, nt=6000, signed=False):
    us = np.linspace(2*T, umax, nu); ts = np.linspace(0, tmax, nt)
    kh = khat(ts, T, N); C = np.cos(np.outer(ts, us))
    # vars: a_j (nu), c ; maximize c  s.t. kh + C a - c >= 0
    if signed:
        A = np.hstack([-C, C, np.ones((nt,1))]); nv = 2*nu+1
        bounds = [(0, None)]*(2*nu) + [(None, None)]
    else:
        A = np.hstack([-C, np.ones((nt,1))]); nv = nu+1
        bounds = [(0, None)]*nu + [(None, None)]
    cvec = np.zeros(nv); cvec[-1] = -1
    r = linprog(cvec, A_ub=A, b_ub=kh, bounds=bounds, method='highs')
    return -r.fun, r

def test_value(T, N, al, be, b):
    """Phi = e^{-al u^2} - b e^{-be u^2}; returns (value/Phi(0), feasibility checks)."""
    Phi = lambda u: np.exp(-al*u*u) - b*np.exp(-be*u*u)
    Phi0 = 1 - b
    assert al > be and b <= np.sqrt(be/al) + 1e-15      # Phi^ >= 0
    u = np.linspace(2*T, 2*T+60, 200001); feas = Phi(u).max() <= 1e-14  # Phi <= 0 outside
    lev = quad(lambda x: (Phi0 - Phi(x))*K(x), 0, np.inf, limit=400)[0]
    pol = 2*quad(lambda x: Phi(x)*np.cosh(x/2), -2*T, 2*T, limit=200)[0]
    val = C0*Phi0 + lev - sum(v*Phi(np.log(n)) for n, v in N) + pol
    return val/Phi0, feas, lev/Phi0, pol/Phi0

if __name__ == "__main__":
    for T in (0.5*np.log(3), np.log(2)+1e-3, 0.5*np.log(5)):
        N = contacts(T); A = sum(v for _, v in N)
        Delta = -C0 + A - 8*np.sinh(T)
        print(f"\nT={T:.6f}  N_T={[n for n,_ in N]}  A_T={A:.6f}  khat(0)=-Delta={-Delta:.6f}")
        cB, _ = lp_classB(T, N); cS, _ = lp_classB(T, N, signed=True)
        print(f"  LP (rejilla, orientativo): clase B nu>=0: {cB:.6f} ; nu con signo: {cS:.6f}")
        best = None
        for be in np.linspace(0.05, 3, 60):
            for ratio in (1.5, 2, 3, 5, 8):
                al = ratio*be
                for frac in (1.0, 0.9, 0.7, 0.5):
                    b = frac*np.sqrt(be/al)
                    v, feas, lev, pol = test_value(T, N, al, be, b)
                    if feas and (best is None or v < best[0]): best = (v, al, be, b, lev, pol)
        print(f"  cota sup rigurosa (test 2-gaussiano): valor={best[0]:.6f} con alpha={best[1]:.4f} beta={best[2]:.4f} b={best[3]:.4f}  [Lev={best[4]:.4f}, polar={best[5]:.4f}]")
