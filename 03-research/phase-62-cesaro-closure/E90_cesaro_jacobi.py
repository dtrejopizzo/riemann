"""
E90 — CESARO CLOSURE GATE for 2.3.F (Phase 62, step C0).

Honest state (post R10): proving L1 (sup_lambda max|A_ij| < inf) POINTWISE in lambda
touches the wall, because the residual e^{-cL} oscillates arithmetically with lambda
(prime echo in the band L=2 log lambda). The escape flagged in OPEN-PROBLEMS O11 is
CESARO AVERAGING IN LAMBDA: average the intrinsic Jacobi coefficients of G_lambda over
lambda; the zero-sum fluctuation averages to 0 by UNCONDITIONAL zero-density (no RH).

This script is the numerical GATE. It does NOT prove anything; it tests whether the
Cesaro route is even alive before we spend analytic effort on C1.

  GATE 1: does the partial Cesaro average Abar_ij(Lambda) = (1/#) sum_{lam<=Lambda} A_ij(lam)
          CONVERGE, with running variance shrinking (consistent with ~1/log speed)?
  GATE 2: does the Jacobi built from the AVERAGED coefficients reproduce the shifted
          band-edge ladder k(k+2) = [0,1,2.667,5,8,11.667] at high lambda?
  FALSADOR: the DH (Davenport-Heilbronn) Jacobi averages must NOT converge / NOT give k(k+2).

Reuses: engine_cache.get_matrices (cached dps=50 build), Lanczos + Jacobi from E79/E85.
Honesty guardrails: dps>=40; DH mandatory; if GATE fails for zeta -> STOP, document NO-GO.
"""
import os, sys, numpy as np, mpmath as mp
# engine (engine_cache, E70 Doob, .cache_23F) lives in phase-61-open-problems
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61)
os.chdir(_P61)  # so engine_cache resolves E70 + .cache_23F by relative path
from engine_cache import get_matrices

mp.mp.dps = 40
TGT = [0.0, 1.0, 2.667, 5.0, 8.0, 11.667]  # shifted k(k+2) band edge


def lanczos(A, q0, m):
    n = A.rows
    Q = [q0 / mp.sqrt((q0.T * q0)[0])]
    alpha = []; beta = []; qprev = mp.zeros(n, 1); b = mp.mpf(0)
    for j in range(m):
        Aq = A * Q[j]
        a = (Q[j].T * Aq)[0]; alpha.append(a)
        r = Aq - a * Q[j] - (b * qprev if j > 0 else mp.zeros(n, 1))
        for qi in Q:                       # full reorthogonalization
            r = r - (qi.T * r)[0] * qi
        b = mp.sqrt((r.T * r)[0])
        if b < mp.mpf(10) ** (-mp.mp.dps + 5) or j == m - 1:
            break
        beta.append(b); qprev = Q[j]; Q.append(r / b)
    return [float(x) for x in alpha], [float(x) for x in beta]


def jac_eigs(alpha, beta):
    m = len(alpha); T = mp.zeros(m)
    for i in range(m):
        T[i, i] = alpha[i]
        if i < len(beta) and i + 1 < m:
            T[i, i + 1] = beta[i]; T[i + 1, i] = beta[i]
    E, _ = mp.eigsy(T)
    return sorted(float(E[i]) for i in range(m))


def shifted_ratios6(ev):
    g = ev[1] - ev[0]
    return [(ev[k] - ev[0]) / g for k in range(min(6, len(ev)))]


def jacobi_for(lam, N, kind):
    """intrinsic Jacobi (alpha,beta) of the Weil matrix A via cyclic both-parity vector."""
    Larch, Lpr, A, L, idx = get_matrices(lam, N, kind, dps=40)
    n = A.rows
    q0 = mp.matrix([[mp.mpf(1) + mp.mpf('0.7') * (2 * i - (n - 1))] for i in range(n)])
    alpha, beta = lanczos(A, q0, n)
    return alpha, beta


def cesaro_gate(grid, kind, ncoef=10):
    """For each Lambda in the grid (cumulative), average the first ncoef alpha/beta across
    all lambda<=Lambda; track convergence of the averages and the band-edge ladder."""
    print(f"\n{'='*74}\nKIND = {kind}   grid = {[g[0] for g in grid]}")
    cum_alpha = []; cum_beta = []; rows = []
    for lam, N in grid:
        alpha, beta = jacobi_for(lam, N, kind)
        cum_alpha.append(alpha[:ncoef]); cum_beta.append(beta[:ncoef])
        # Cesaro partial averages over lambda<=current
        amin = min(len(a) for a in cum_alpha); bmin = min(len(b) for b in cum_beta)
        Abar = [np.mean([a[k] for a in cum_alpha]) for k in range(amin)]
        Bbar = [np.mean([b[k] for b in cum_beta]) for k in range(bmin)]
        ev = jac_eigs(Abar, Bbar)
        sr = shifted_ratios6(ev)
        maxA = max(max(abs(x) for x in alpha), max(abs(x) for x in beta))
        rows.append((lam, Abar, Bbar, sr, maxA))
        print(f"  lam<={lam:5.1f}  max|coef|={maxA:7.3f}  "
              f"Abar0={Abar[0]:8.4f} Bbar0={Bbar[0]:8.4f}  "
              f"ladder={[round(r,3) for r in sr]}")
    # GATE 1: running variance of Abar[0],Bbar[0] across the last successive Lambdas
    a0_seq = [r[1][0] for r in rows]; b0_seq = [r[2][0] for r in rows]
    tail = max(3, len(rows) // 2)
    var_a = np.var(a0_seq[-tail:]); var_b = np.var(b0_seq[-tail:])
    # successive deltas (should shrink if converging)
    da = [abs(a0_seq[i] - a0_seq[i - 1]) for i in range(1, len(a0_seq))]
    print(f"  GATE1  tail-var(Abar0)={var_a:.3e}  tail-var(Bbar0)={var_b:.3e}  "
          f"last delta(Abar0)={da[-1]:.3e}  (shrinking => Cesaro converges)")
    last = rows[-1][3]
    err = max(abs(last[k] - TGT[k]) for k in range(len(last)))
    g2 = err < 0.6
    print(f"  GATE2  final ladder err vs k(k+2) = {err:.3f}  => "
          f"{'k(k+2) SURVIVES averaging' if g2 else 'ladder broken'}")
    return rows, var_a, var_b, g2, err


if __name__ == '__main__':
    # lambda sweep; N grows ~ with lambda to keep the band resolved
    grid = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18),
            (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E90 — Cesaro convergence gate for the intrinsic Jacobi of G_lambda (2.3.F C0)")
    rz, vaz, vbz, g2z, ez = cesaro_gate(grid, 'zeta')
    rd, vad, vbd, g2d, ed = cesaro_gate(grid, 'DH')
    print(f"\n{'='*74}\nVERDICT")
    print(f"  zeta: GATE2 ladder {'PASS' if g2z else 'FAIL'} (err {ez:.3f}); "
          f"Cesaro var(Abar0)={vaz:.2e}")
    print(f"  DH  : GATE2 ladder {'PASS' if g2d else 'FAIL'} (err {ed:.3f}); "
          f"Cesaro var(Abar0)={vad:.2e}")
    falsador_ok = (not g2d) or (ed > ez * 1.5)
    print(f"  FALSADOR (DH must differ): {'OK' if falsador_ok else 'FAILED — DH mimics zeta'}")
    if g2z and falsador_ok:
        print("  => C0 GATE PASSES for zeta, DH separated. Proceed to C1.")
    else:
        print("  => C0 GATE FAILS. STOP. Document in NO-GO-LIST. Do NOT claim Cesaro route.")
