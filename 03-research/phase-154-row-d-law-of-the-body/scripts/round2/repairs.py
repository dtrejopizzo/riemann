"""R154 round 2, script 4: repairs R1, R3, R4 and the zero count of the symbol (C1 index)."""
import math, sys, numpy as np, scipy.linalg as sla
sys.path.insert(0, '/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core
from scipy.special import psi as dg
C0 = float(np.real(dg(0.25))) - math.log(math.pi)

def cF(F, T, K, u):
    """autocorrelation at u of F = sum F_k sin(k pi (t+T)/L) on (-T,T), by quadrature."""
    L = 2*T; x = np.linspace(-T, T, 20001); dx = x[1]-x[0]
    ph = lambda t: np.sum([F[k-1]*np.sin(k*math.pi*(t+T)/L) for k in range(1, K+1)], axis=0)
    f = ph(x); g = np.where(np.abs(x-u) <= T, ph(np.clip(x-u, -T, T)), 0.0)
    return np.trapz(f*g, x)

print("R1: the two moment conditions on Phi = c_F")
for T, contacts in ((0.5*math.log(3), [2]), (math.log(2), [2, 3])):
    for mode, betas in (("P_T (both)", [-0.5, 0.5]), ("ker M_- only", [0.5])):
        K = 120; L = 2*T
        Z = sla.null_space(core.moments(T, K, betas))
        G = Z.T @ (np.eye(K)*T) @ Z
        M0 = Z.T @ core.gamma_matrix(T, K) @ Z
        A = M0.copy()
        for n in contacts: A = A - 2*core.wgt(n)*(Z.T @ core.shift_matrix(T, K, math.log(n)) @ Z)
        w, V = sla.eigh(A, G); F = Z @ V[:, 0]; F /= math.sqrt(float(V[:,0] @ G @ V[:,0]))
        us = np.linspace(-L+1e-9, L-1e-9, 4001)
        Ph = np.array([cF(F, T, K, u) for u in us])
        i0 = np.trapz(Ph*np.cosh(us/2), us); i1 = np.trapz(Ph*us*np.sinh(us/2), us)
        print(f"  T={T:.5f} {mode}: lambda={w[0]:.8e}  int Phi cosh={i0:.3e}  int Phi u sinh={i1:.3e}"
              f"   Lambda_T = C0-lambda = {C0-w[0]:.8f}")

print("\nR4: joint truncated contact maximum  max{sum v_n Phi(log n)} and min E")
for T, contacts in ((0.5*math.log(3), [2]), (math.log(2), [2, 3])):
    K = 200
    B = core.Body(T, K, contacts)
    v = {n: 2*math.log(n)/math.sqrt(n) for n in contacts}
    top = B.eig(0.0, {n: v[n] for n in contacts}, 'max')[0]
    minE = B.eig(1.0, {n: 0.0 for n in contacts}, 'min')[0] - C0
    print(f"  T={T:.5f}: max sum v_n Phi(log n) = {top:.7f}   sum v_n = {sum(v.values()):.7f}"
          f"   min E = {minE:.7f}")

print("\nC1: sign changes of the symbol sigma(tau) = m(tau) - sum v_n cos(tau log n)  (Krein index datum)")
for T, contacts in ((0.5*math.log(3), [2]), (math.log(2), [2, 3])):
    v = {n: 2*math.log(n)/math.sqrt(n) for n in contacts}
    t = np.linspace(1e-6, 400, 4000001)
    s = np.real(dg(0.25+0.5j*t)) - math.log(math.pi) - sum(v[n]*np.cos(t*math.log(n)) for n in contacts)
    z = np.where(np.diff(np.sign(s)))[0]
    print(f"  T={T:.5f}: sigma(0)={C0-sum(v.values()):.6f}, {len(z)} sign changes on (0,400), "
          f"largest at tau={t[z[-1]] if len(z) else 0:.4f}; sigma>0 beyond it")
