"""R153 Q1 -- the Xi_a falsifier form A_T^{(a)} on P_T^{(a)}, at T = log2 and T = (1/2)log3.

Uses the corpus operator assembly rowd_assembly.assemble (phase 118) unmodified:
    <A_T F,F> = <G_Gamma F,F> - m_0 ||F||^2 - sum_n (Lambda(n)/sqrt n) <(S_{log n}+S_{-log n})F,F>

Theorem A (proved in the report):  for F supported in I_T,
    <A_T^{(a)} F,F> = 2[ <A_T u,u> - <A_T w,w> ],   u = cosh(at)F,  w = sinh(at)F,
and F in P_T^{(a)} (four moments Phi_F(p)=0, p in {-a,a,1-a,1+a}) <=> u,w in P_T.

Discretisation: piecewise-constant basis on the phase-118 mesh; cosh/sinh are
replaced by their exact cell averages (second order).  DIAGNOSTIC-NUMERIC.

Run: python3 r153_q1_xi_a.py
"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    "../../phase-118-the-exact-threshold-inequality/scripts")))
import rowd_assembly as RA
import scipy.linalg as sla


def cell_avg_exp(c, d, beta):
    """(1/(d-c)) int_c^d e^{beta t} dt, beta may be 0."""
    if beta == 0:
        return np.ones_like(c)
    return (np.exp(beta*d) - np.exp(beta*c)) / (beta*(d-c))


def moments(c, d, betas):
    """rows: int_c^d e^{beta t} dt over each cell."""
    rows = []
    for b in betas:
        if b == 0:
            rows.append(d-c)
        else:
            rows.append((np.exp(b*d)-np.exp(b*c))/b)
    return np.array(rows)


def constrained_min(M, Gram, C):
    """min of x^T M x / x^T Gram x subject to C x = 0 ; returns (lam_min, argmin)."""
    Z = sla.null_space(C)
    Mz = Z.T @ M @ Z
    Gz = Z.T @ Gram @ Z
    Mz = 0.5*(Mz+Mz.T); Gz = 0.5*(Gz+Gz.T)
    w, V = sla.eigh(Mz, Gz)
    return w, Z @ V


def run(T, refine, a_list, label):
    D = RA.assemble(T, refine=refine)
    c, d, A, Gram = D['c'], D['d'], D['A'], D['Gram']
    # --- validation: xi itself, P_T = ker M_- cap ker M_+
    C2 = moments(c, d, [-0.5, 0.5])
    w2, V2 = constrained_min(A, Gram, C2)
    print(f"[{label}] T={T:.6f} refine={refine} cells={len(c)}")
    print(f"   VALIDATION lambda_min(A_T|P_T) = {w2[0]: .6e}   next = {w2[1]: .6e}  (DIAGNOSTIC-NUMERIC)")
    v1 = V2[:, 0]
    nrm = math.sqrt(v1 @ Gram @ v1); v1 = v1/nrm
    # parity of v1
    par = float(v1 @ (Gram @ v1[::-1])) / float(v1 @ Gram @ v1)
    print(f"   v1 parity overlap <v1,v1(-t)>/||v1||^2 = {par: .4f}  (+1 even, -1 odd)")
    # --- Q1: Xi_a
    for a in a_list:
        ch = cell_avg_exp(c, d, 0)*0  # placeholder
        ch = 0.5*(cell_avg_exp(c, d, a) + cell_avg_exp(c, d, -a))
        sh = 0.5*(cell_avg_exp(c, d, a) - cell_avg_exp(c, d, -a))
        Du, Dw = np.diag(ch), np.diag(sh)
        Ma = 2.0*(Du @ A @ Du - Dw @ A @ Dw)
        C4 = moments(c, d, [-0.5-a, -0.5+a, 0.5-a, 0.5+a])
        wa, Va = constrained_min(Ma, Gram, C4)
        # also: value of the two pieces at the minimiser
        x = Va[:, 0]; x = x/math.sqrt(x @ Gram @ x)
        uu = (Du@x) @ A @ (Du@x); ww = (Dw@x) @ A @ (Dw@x)
        print(f"   a={a:.4f}  lambda_min(A_T^(a)|P_T^(a)) = {wa[0]: .6e}"
              f"   [<Au,u>={uu: .3e}, <Aw,w>={ww: .3e}]")
    print()


if __name__ == "__main__":
    A_LIST = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.49]
    for ref in (4, 8, 16):
        run(math.log(2), ref, A_LIST, "log2")
    for ref in (4, 8, 16):
        run(0.5*math.log(3), ref, A_LIST, "half-log3")
