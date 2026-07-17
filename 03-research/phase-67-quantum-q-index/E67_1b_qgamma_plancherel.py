"""
E67.1b -- q-Gamma / Plancherel archimedean matching.

This tests the correction suggested by the E67.1 residual:

  single SU(1,1) coherent kernel  ->  leading Szego term only;
  q-Gamma / Plancherel c-function ->  full Gamma/polygamma archimedean factor.

We compare the q-Gamma deformation

  psi_q(x) = d/dx log Gamma_q(x)

against the exact P52 archimedean input

  h_A(z) = i[-(1/s + 1/(s-1)) + 1/2 log(pi) - 1/2 psi(s/2)],
  s = 1/2 + i z,

including the polar s(s-1) factor used by h8lab.py. This is zeta-free:
only Gamma_q/Gamma and the polar factor appear.

The test has two levels:
  (F) function-level convergence h_A,q(z0) -> h_A(z0);
  (J) jet/matrix convergence pick_jet(h_A,q) -> A_N.
"""
import os
import sys
import math
import numpy as np
import mpmath as mp

PROGRAM_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
H8 = os.path.join(PROGRAM_ROOT, "04-papers", "P52-riemann-proof-audit")
sys.path.insert(0, H8)
import h8lab as H  # noqa: E402

mp.mp.dps = 70


def mp_to_np(M):
    return np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)], dtype=np.complex128)


def q_polygamma(m, x, q, safety=50):
    """m-th x-derivative of psi_q(x) for 0<q<1.

    psi_q(x) = -log(1-q) + log(q) * sum_{r>=1} q^{r x}/(1-q^r)
    psi_q^{(m)}(x) = log(q)^{m+1} * sum_{r>=1} r^m q^{r x}/(1-q^r), m>=1.

    Uses a deterministic cutoff sized to the saddle r~m/((1-q)Re x) and the tail decay.
    """
    q = mp.mpf(q)
    L = mp.log(q)
    xr = max(mp.mpf("0.05"), mp.re(x))
    a = -L * xr
    # Enough to include the saddle for derivative order m and make exp(-a R) tiny.
    R = int(max(2000, (m + safety) / float(a)))
    total = mp.mpc(0)
    qr = q
    # Direct recurrence avoids repeated q**r in the real denominator.
    for r in range(1, R + 1):
        term = (r ** m) * mp.e**(L * r * x) / (1 - qr)
        total += term
        qr *= q
    if m == 0:
        return -mp.log(1 - q) + L * total
    return (L ** (m + 1)) * total


def hA_q_taylor(z0, M, q):
    """Taylor coeffs of q-Gamma-deformed h_A,q(z), order 0..M."""
    s0 = mp.mpf(1) / 2 + mp.j * z0
    x0 = s0 / 2
    out = []
    for p in range(M + 1):
        if p == 0:
            f = -(1 / s0 + 1 / (s0 - 1)) + mp.log(mp.pi) / 2 - q_polygamma(0, x0, q) / 2
            out.append(mp.j * f)
        else:
            pole_der = -((-1) ** p) * mp.factorial(p) / s0 ** (p + 1)
            pole_der += -((-1) ** p) * mp.factorial(p) / (s0 - 1) ** (p + 1)
            gamma_der = -mp.mpf("0.5") * (mp.mpf("0.5") ** p) * q_polygamma(p, x0, q)
            f_der = pole_der + gamma_der
            out.append((mp.j ** (p + 1)) * f_der / mp.factorial(p))
    return out


def rel_frob(A, B):
    return float(np.linalg.norm(A - B, "fro") / np.linalg.norm(A, "fro"))


def function_test(t0, y, qs):
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    exact = H.hA_taylor(z0, 0)[0]
    print(f"\n(F) function test at z0={t0}-i{y}")
    print(f"  exact h_A={mp.nstr(exact, 18)}")
    for q in qs:
        approx = hA_q_taylor(z0, 0, mp.mpf(str(q)))[0]
        err = abs(approx - exact) / max(mp.mpf(1), abs(exact))
        print(f"  q={q:<7} rel={mp.nstr(err, 8)}  h_A,q={mp.nstr(approx, 18)}")


def matrix_test(t0, y, N, qs):
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    hA = H.hA_taylor(z0, 2 * N + 4)
    A_exact = mp_to_np(H.herm(H.pick_jet(hA, z0, N)))
    print(f"\n(J) matrix test at z0={t0}-i{y}, N={N}")
    for q in qs:
        hq = hA_q_taylor(z0, 2 * N + 4, mp.mpf(str(q)))
        A_q = mp_to_np(H.herm(H.pick_jet(hq, z0, N)))
        print(f"  q={q:<7} relFrob={rel_frob(A_exact, A_q):.3e}")


def main():
    print(__doc__, flush=True)
    print("=" * 88)
    print("Exact source:", os.path.join(H8, "h8lab.py"))
    print("q-polygamma is computed from the Gamma_q logarithmic derivative series.")
    print("=" * 88)

    # q close to 1; 0.995 is already enough to show convergence without extreme cost.
    qs = ["0.90", "0.97", "0.99", "0.995"]

    for t0 in (10.0, 100.0, 1000.0):
        function_test(t0, 1.0, qs)

    for t0 in (10.0, 100.0):
        for N in (2, 4, 6):
            matrix_test(t0, 1.0, N, qs)

    print("\nVerdict guide:")
    print("  PASS if rel errors decrease monotonically as q->1 and reach the q-truncation floor.")
    print("  This closes the archimedean sector conceptually: Gamma_q/Plancherel gives full h_A,")
    print("  while E67.1's single coherent kernel was only the leading Szego term.")


if __name__ == "__main__":
    main()

