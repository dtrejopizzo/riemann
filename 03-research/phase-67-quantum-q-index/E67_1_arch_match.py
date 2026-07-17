"""
E67.1 -- archimedean matching test for Phase 67.

Goal
----
Compare the exact P52 archimedean Pick jet A_N from h8lab.py against the q->1
coherent-kernel model of the positive discrete series of SU(1,1).

This is a kill-test, not a proof:
  PASS would mean the archimedean side of CAND-67 is real at the matrix level.
  FAIL means the naive discrete-series coherent kernel is only a leading/local model.

Allowed freedoms in this test
-----------------------------
The coherent model is allowed:
  * exponent alpha > 0, with alpha=2k for a positive discrete series parameter k;
  * a local coordinate rescaling tau^(j+k);
  * one positive scalar c.

It is NOT allowed to fit entries independently, use zeta/prime data, or use the
prime Pick jet P_lambda. The comparison is purely archimedean.
"""
import os
import sys
import math
import numpy as np
import mpmath as mp
from scipy.special import gammaln

PROGRAM_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
H8 = os.path.join(PROGRAM_ROOT, "04-papers", "P52-riemann-proof-audit")
sys.path.insert(0, H8)
import h8lab as H  # noqa: E402

mp.mp.dps = 80


def mp_to_np(M):
    return np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)], dtype=np.complex128)


def candidate_kernel(N, y, alpha, tau):
    """Taylor-coefficient Gram of the half-plane coherent kernel.

    K_alpha[j,k] = exp(i*pi*alpha/2) (-1)^k (alpha)_{j+k}/(j! k!)
                   (2 i y)^(-alpha-j-k) tau^(j+k)

    For alpha=1, tau=1 this reduces exactly to h8lab.G_exact(N,y).
    """
    K = np.zeros((N, N), dtype=np.complex128)
    phase = np.exp(0.5j * np.pi * alpha)
    denom0 = 2j * float(y)
    for j in range(N):
        for k in range(N):
            coeff = math.exp(gammaln(alpha + j + k) - gammaln(alpha) - gammaln(j + 1) - gammaln(k + 1))
            K[j, k] = phase * ((-1) ** k) * coeff * (denom0 ** (-alpha - j - k)) * (tau ** (j + k))
    return 0.5 * (K + K.conj().T)


def best_scalar_residual(A, K):
    """Return best positive real scalar c and relative Frobenius residual ||A-cK||/||A||."""
    num = float(np.real(np.vdot(K, A)))
    den = float(np.real(np.vdot(K, K)))
    c = max(0.0, num / den) if den > 0 else 0.0
    res = np.linalg.norm(A - c * K, "fro") / np.linalg.norm(A, "fro")
    return c, float(res)


def condition_number(M):
    vals = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
    return float(vals[-1] / vals[0]), float(vals[0]), float(vals[-1])


def fit_grid(A, N, y, alpha_grid, tau_grid):
    best = None
    for alpha in alpha_grid:
        for tau in tau_grid:
            K = candidate_kernel(N, y, alpha, tau)
            # Skip non-PD numerical pathologies.
            try:
                eigs = np.linalg.eigvalsh(K)
            except np.linalg.LinAlgError:
                continue
            if eigs[0] <= 0:
                continue
            c, res = best_scalar_residual(A, K)
            item = (res, c, alpha, tau, eigs[0], eigs[-1])
            if best is None or item < best:
                best = item
    return best


def refine_fit(A, N, y, alpha0, tau0):
    # Lightweight coordinate refinement around the coarse winner.
    alpha_grid = np.linspace(max(0.05, alpha0 * 0.75), alpha0 * 1.25, 101)
    tau_grid = np.exp(np.linspace(np.log(tau0) - 0.35, np.log(tau0) + 0.35, 101))
    return fit_grid(A, N, y, alpha_grid, tau_grid)


def run_case(t0, y, N):
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    # Use only the archimedean Taylor coefficients. H.arithmetic_jets also builds
    # the prime side through high zeta derivatives, which is irrelevant here and
    # very slow at large t0.
    hA = H.hA_taylor(z0, 2 * N + 4)
    A_mp = H.herm(H.pick_jet(hA, z0, N))
    A = mp_to_np(A_mp)

    # Baseline: exact Hardy/Szego reference Gram from h8lab (alpha=1, tau=1).
    G = mp_to_np(H.G_exact(N, mp.mpf(str(y))))
    cG, resG = best_scalar_residual(A, G)

    # Discrete-series coherent family: alpha and local scale tau.
    # Optimize only at small N; the baseline alpha=1 already tests the q->1
    # positive-discrete-series kernel and is the relevant Phase-66 calibration.
    refined = None
    if N <= 8:
        alpha_grid = np.linspace(0.5, 2.0, 61)
        tau_grid = np.exp(np.linspace(np.log(0.5), np.log(2.0), 61))
        coarse = fit_grid(A, N, y, alpha_grid, tau_grid)
        refined = refine_fit(A, N, y, coarse[2], coarse[3]) if coarse else None

    condA, minA, maxA = condition_number(A)
    print(
        f"t0={t0:>8g} y={y:g} N={N:2d} | "
        f"A eig min/max={minA:.3e}/{maxA:.3e} cond={condA:.3e}"
    , flush=True)
    expected = math.log(float(t0) / (2 * math.pi))
    print(
        f"  baseline alpha=1,tau=1: c={cG:.8e} relFrob={resG:.3e} "
        f"(log(t0/2pi)={expected:.8e}, c/log={cG/expected:.8f})",
        flush=True,
    )
    if refined:
        res, c, alpha, tau, kmin, kmax = refined
        print(
            f"  best coherent kernel : c={c:.8e} alpha={alpha:.6g} "
            f"tau={tau:.6g} relFrob={res:.3e} Kcond={kmax/kmin:.3e}"
        , flush=True)
    return resG, refined


def main():
    print(__doc__, flush=True)
    print("=" * 88, flush=True)
    print("Exact A_N source:", os.path.join(H8, "h8lab.py"), flush=True)
    print("Candidate family: q->1 SU(1,1) positive-discrete-series coherent kernel", flush=True)
    print("PASS heuristic: relFrob should fall toward high precision for the correct model.", flush=True)
    print("FAIL heuristic: stable nonzero residual means only leading/Szego behavior is matched.", flush=True)
    print("=" * 88, flush=True)

    cases = []
    for t0 in (100.0, 1000.0, 1.0e6):
        for N in (2, 4, 8, 12, 16, 20, 24):
            cases.append((t0, 1.0, N))

    summary = []
    for t0, y, N in cases:
        resG, refined = run_case(t0, y, N)
        if refined:
            summary.append((t0, N, resG, refined[0], refined[2], refined[3]))
        else:
            summary.append((t0, N, resG, float("nan"), float("nan"), float("nan")))

    print("\n" + "=" * 88, flush=True)
    print("SUMMARY", flush=True)
    print("  t0        N   baseline_res   best_res     best_alpha   best_tau", flush=True)
    for t0, N, resG, res, alpha, tau in summary:
        print(f"  {t0:8.0f} {N:3d}   {resG:12.3e} {res:12.3e} {alpha:12.6g} {tau:10.6g}", flush=True)

    worst_baseline = max(row[2] for row in summary)
    best_available = [row[3] for row in summary if not math.isnan(row[3])]
    worst_best = max(best_available) if best_available else float("nan")
    print("\nVerdict:", flush=True)
    if worst_baseline < 1e-8:
        print("  PASS: coherent SU(1,1) kernel matches A_N at matrix level in this grid.")
    elif worst_baseline < 1e-2:
        print("  PARTIAL/LEADING: alpha=1 coherent kernel matches the Szego leading term very well,")
        print("  with scalar c=log(t0/2pi), but the residual is not zero. This is not E67.1 exact matching.")
    else:
        print("  FAIL: naive coherent SU(1,1) kernel does not reproduce exact P52 A_N.")
        print("  It may be only the leading Szego/Bergman approximation; QSC-exist cannot start from it unchanged.")


if __name__ == "__main__":
    main()
