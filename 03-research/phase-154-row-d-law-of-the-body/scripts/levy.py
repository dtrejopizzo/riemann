"""R154 script 1: the Levy (window) decomposition of the archimedean symbol.

m(tau) = Re psi(1/4+i tau/2) - log pi
K(u)   = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2))       (u>0)
Claim L: m(tau) = C0 + int_0^inf (1-cos(tau u)) K(u) du,  C0 = psi(1/4)-log pi.
Claim R: R(T) := int_{2T}^inf K = log coth(T/2) + pi - 2 arctan(e^T).
Claim A: for ||F||=1 supported in (-T,T), with Phi = autocorrelation,
   <A_T F,F> = C0 + R(T) - [ sum_n v_n Phi(a_n) - E_T(Phi) ],  E_T(Phi)=int_0^{2T}(1-Phi)K.
"""
import math, sys
import mpmath as mp
import numpy as np
sys.path.insert(0, '/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core

mp.mp.dps = 30
K = lambda u: 1/(2*mp.sinh(u/2)) + 1/(2*mp.cosh(u/2))
C0 = mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi)
m = lambda tau: mp.re(mp.digamma(mp.mpf(1)/4 + 1j*tau/2)) - mp.log(mp.pi)

print("C0 =", mp.nstr(C0, 15))
print("--- Claim L (Levy representation) ---")
for tau in [0.5, 1, 3, 7, 20, 100]:
    lhs = m(tau)
    rhs = C0 + mp.quad(lambda u: (1-mp.cos(tau*u))*K(u), [0, 1/mp.mpf(tau), 10/mp.mpf(tau), 50, mp.inf])
    print(f" tau={tau:6}  m={mp.nstr(lhs,15)}  Levy={mp.nstr(rhs,15)}  diff={mp.nstr(lhs-rhs,3)}")

print("--- Claim R (window tail, closed form) ---")
for T in [0.5*math.log(3), math.log(2), 0.5*math.log(5), 1.7]:
    num = mp.quad(K, [2*T, 2*T+1, 20, mp.inf])
    cf = mp.log(mp.coth(mp.mpf(T)/2)) + mp.pi - 2*mp.atan(mp.e**T)
    print(f" T={T:.6f}  numeric={mp.nstr(num,15)}  closed={mp.nstr(cf,15)}  diff={mp.nstr(num-cf,3)}")
print("  R(log2) vs log3+pi-2atan2 :", mp.nstr(mp.log(3)+mp.pi-2*mp.atan(2),15))
print("  R(.5log3) vs log(2+sqrt3)+pi-2pi/3 :", mp.nstr(mp.log(2+mp.sqrt(3))+mp.pi-2*mp.pi/3,15))

print("--- Claim A (exact identity, Galerkin test vectors) ---")
def phi_of(T, Kdim, c, u):
    """autocorrelation at lag u of the sine-basis vector c (normalised)."""
    S = core.shift_matrix(T, Kdim, u)
    return float(c @ S @ c)

def check(T, Kdim=160, contacts=None, seed=0):
    if contacts is None:
        contacts = [n for n in (2,3,4,5) if n < math.exp(2*T)-1e-13]
    v = {n: 2*core.wgt(n) for n in contacts}
    B = core.Body(T, Kdim, contacts=contacts, constrained=True)
    rng = np.random.default_rng(seed)
    tests = []
    lam, Fmin = B.eig(1.0, {n: -v[n] for n in contacts}, 'min')
    tests.append(('min', Fmin, lam))
    for j in range(2):
        z = rng.standard_normal(B.Z.shape[1]); F = B.Z @ z
        M = B.op(1.0, {n: -v[n] for n in contacts})
        q = float(z @ M @ z)/float(z @ B.G @ z)
        tests.append((f'rand{j}', F, q))
    for name, F, q in tests:
        nrm = math.sqrt(float(F @ F) * T)
        c = F/nrm
        # E_T = int_0^{2L}(1-Phi)K ; Phi from exact shift matrices
        L = 2*T
        nodes, wts = np.polynomial.legendre.leggauss(40)
        edges = np.concatenate([np.linspace(0, 0.05*L, 9), np.linspace(0.05*L, L, 25)[1:]])
        E = 0.0
        for lo, hi in zip(edges[:-1], edges[1:]):
            uu = 0.5*(hi-lo)*nodes + 0.5*(hi+lo); ww = 0.5*(hi-lo)*wts
            for u, w in zip(uu, ww):
                E += w*(1-phi_of(T, F.size, c, u))*float(K(u))
        RT = float(mp.log(mp.coth(mp.mpf(T)/2)) + mp.pi - 2*mp.atan(mp.e**T))
        Lam = sum(v[n]*phi_of(T, F.size, c, math.log(n)) for n in contacts) - E
        pred = float(C0) + RT - Lam
        print(f" T={T:.6f} {name:6} <A F,F>={q: .10f}  C0+R-Lambda={pred: .10f}  diff={q-pred: .2e}   E_T={E:.6f} Lambda={Lam:.6f}")

check(0.5*math.log(3))
check(math.log(2))
