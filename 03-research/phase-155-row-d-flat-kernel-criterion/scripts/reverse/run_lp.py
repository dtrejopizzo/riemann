"""run_lp.py -- TASK 1: the true dual from the zeros.

For each window T, maximise c subject to
    f^known_w(tau_i) = sum_{|gamma|<=Gmax} what(tau_i-gamma) >= c   on a tau-grid,
over flat-top weights w = 1_[-2T,2T] + sum_k x_k e^{-s_k(|u|-2T)}.
THE LP NEVER SEES THE PRIMES.   Everything produced here is DIAGNOSTIC.
usage: python3 run_lp.py [outfile.json]
"""
import numpy as np, json, sys, time
from scipy.optimize import linprog
import revlib as R

TS = [("0.5log3", 0.5*np.log(3.0)), ("0.58", 0.58), ("0.62", 0.62),
      ("0.65", 0.65), ("log2", np.log(2.0)), ("0.75", 0.75), ("0.80", 0.80)]
VARIANTS = [("free", None), ("C0", 0), ("C1", 1)]   # 0 = w cont., 1 = w in C^1
LBOUND = 20.0
DTAU = 0.02

def solve(Bz, Az, mode, L=LBOUND, svals=None):
    nS, nT = Az.shape
    # vars [p(nS), q(nS), c]
    n = 2*nS + 1
    A_ub = np.zeros((nT+1, n)); b_ub = np.zeros(nT+1)
    A_ub[:nT, :nS] = -Az.T; A_ub[:nT, nS:2*nS] = Az.T; A_ub[:nT, -1] = 1.0
    b_ub[:nT] = Bz
    A_ub[nT, :2*nS] = 1.0; b_ub[nT] = L
    Aeq = []; beq = []
    if mode is not None:
        Aeq.append(np.concatenate([np.ones(nS), -np.ones(nS), [0.]])); beq.append(1.0)
    if mode == 1:
        Aeq.append(np.concatenate([svals, -svals, [0.]])); beq.append(0.0)
    c = np.zeros(n); c[-1] = -1.0
    bnds = [(0, None)]*(2*nS) + [(None, None)]
    r = linprog(c, A_ub=A_ub, b_ub=b_ub,
                A_eq=np.array(Aeq) if Aeq else None,
                b_eq=np.array(beq) if beq else None,
                bounds=bnds, method="highs")
    if not r.success:
        return None, None
    x = r.x[:nS] - r.x[nS:2*nS]
    return r.x[-1], x

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "lp_results.json"
    gam = R.load_zeros()
    svals = R.basis(48)
    res = {"Gmax": float(gam[-1]), "nzeros": len(gam), "svals": svals.tolist(),
           "dtau": DTAU, "L": LBOUND, "runs": []}
    for name, T in TS:
        A_T = R.A_const(T)
        taumax = min(2*np.pi*np.exp(A_T), 200.0)
        tau = np.arange(0.0, taumax + 1e-9, DTAU)
        t0 = time.time()
        Bz, Az = R.zero_side_matrix(tau, T, svals, gam)
        tz = time.time()-t0
        rec = {"name": name, "T": T, "A_T": A_T, "taumax": taumax,
               "ngrid": len(tau), "t_zero": tz, "variants": {}}
        for vn, mode in VARIANTS:
            t0 = time.time()
            c, x = solve(Bz, Az, mode, svals=svals)
            if c is None:
                rec["variants"][vn] = {"status": "infeasible"}; continue
            f = Bz + x @ Az
            # shape diagnostics
            mass = float(np.sum(x/svals))          # int_{2T}^inf w  (one side)
            dec = float(-np.sum(x/svals)/np.sum(x)) if abs(np.sum(x)) > 1e-12 else np.nan
            # effective decay scale = first moment / mass of |x_k|/s_k
            wmass = np.abs(x)/svals
            escale = float(np.sum(wmass/svals)/np.sum(wmass))
            rec["variants"][vn] = {
                "c": float(c), "x": x.tolist(), "sumx": float(np.sum(x)),
                "sum_sx": float(np.sum(svals*x)), "l1": float(np.abs(x).sum()),
                "tail_mass": mass, "eff_decay_scale": escale,
                "fmin": float(f.min()), "argmin": float(tau[np.argmin(f)]),
                "npos": int((x > 1e-9).sum()), "nneg": int((x < -1e-9).sum()),
                "t_lp": time.time()-t0,
                "contacts": [float(tau[i]) for i in np.nonzero(
                    (f < c + 1e-5) & np.r_[True, f[1:] <= f[:-1]] &
                    np.r_[f[:-1] <= f[1:], True])[0]],
            }
            print(f"{name:8s} {vn:4s} c={c: .6e} fmin={f.min(): .6e} "
                  f"l1={np.abs(x).sum():.3f} mass={mass:+.4f} "
                  f"escale={escale:.4f} argmin={tau[np.argmin(f)]:.2f}", flush=True)
        res["runs"].append(rec)
    json.dump(res, open(out, "w"))
    print("wrote", out)

if __name__ == "__main__":
    main()
