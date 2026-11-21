#!/usr/bin/env python3
"""
reproduce.py

Computations for the paper
  "The omega-class decomposition of Dirichlet polynomials:
   elementary bounds and computations"
by David Alejandro Trejo Pizzo.

For each N in N_LIST the script evaluates the class sums

    S_k(t;N) = sum_{2 <= n <= N, omega(n) = k} n^{-1/2-it},   k = 1..K_N,

on the full grid t_j = N/10 + j*dt, dt = pi/log N, t_j <= N (no thinning),
and then refines the largest local maxima of |S_k|^2 and of 1+r between grid
points.  All numbers in the tables of the paper, the four figures and the
file results/computation_results.json are produced by this script.

Usage:
    python3 reproduce.py                 # all four N, writes figures/ and results/
    python3 reproduce.py --quick         # N = 10^4 only
    python3 reproduce.py --out DIR       # write figures/ and results/ under DIR
    python3 reproduce.py --validate      # also compare with 50-digit mpmath and
                                         # compute zeta near the Liouville point
    python3 reproduce.py --from-json     # keep the class-sum results already in
                                         # results/computation_results.json; redo
                                         # only the Liouville part and the figures

Dependencies: numpy, matplotlib (figures), mpmath (only for --validate).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import argparse
import json
import math
import time
from multiprocessing import Pool

import numpy as np

N_LIST = [10_000, 50_000, 100_000, 150_000]
CHUNK = 48            # t-values per block
N_CAND = 40           # local maxima refined per quantity
PEAK_FRACTION = 0.01  # fraction of grid points counted as "large values of |D|"
LIOUVILLE_N = 100_000
LIOUVILLE_T = 7563.5


# ---------------------------------------------------------------- arithmetic
def omega_arrays(N):
    """omega(n) (distinct prime factors) and Omega(n) (with multiplicity), 0..N."""
    omega = np.zeros(N + 1, dtype=np.int32)
    Omega = np.zeros(N + 1, dtype=np.int32)
    sieve = np.ones(N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, N + 1):
        if sieve[p]:
            sieve[p * p::p] = False
            omega[p::p] += 1
            q = p
            while q <= N:
                Omega[q::q] += 1
                q *= p
    return omega, Omega


# -------------------------------------------------------------- class sums
_G = {}


def _setup(N):
    omega, _ = omega_arrays(N)
    n = np.arange(2, N + 1)
    om = omega[2:]
    K = int(om.max())
    logn = np.log(n.astype(np.float64))
    W = np.zeros((N - 1, K))
    W[np.arange(N - 1), om - 1] = n.astype(np.float64) ** -0.5
    _G.clear()
    _G.update(N=N, n=n, om=om, K=K, logn=logn, W=W)
    return K


def class_sums(ts):
    """Array of shape (len(ts), K): S_k(t;N) for the N of the last _setup."""
    ts = np.atleast_1d(np.asarray(ts, dtype=np.float64))
    out = np.empty((len(ts), _G["K"]), dtype=np.complex128)
    for a in range(0, len(ts), CHUNK):
        ph = np.outer(ts[a:a + CHUNK], _G["logn"])
        out[a:a + CHUNK] = np.cos(ph) @ _G["W"] - 1j * (np.sin(ph) @ _G["W"])
    return out


def _refine(job):
    """Maximise q(t) on [t0-dt, t0+dt] by three successive 17-point zooms.

    q is |S_k|^2 for kind = k-1 >= 0 and 1+r for kind = -1."""
    kind, t0, dt = job
    lo, hi = t0 - dt, t0 + dt
    best_t, best_v = t0, -1.0
    for _ in range(3):
        ts = np.linspace(lo, hi, 17)
        S = class_sums(ts)
        P = np.abs(S) ** 2
        q = np.abs(S.sum(axis=1)) ** 2 / P.sum(axis=1) if kind < 0 else P[:, kind]
        i = int(q.argmax())
        if q[i] > best_v:
            best_t, best_v = float(ts[i]), float(q[i])
        h = (hi - lo) / 16
        lo, hi = best_t - h, best_t + h
    return kind, best_t, best_v


def _local_maxima(q, count):
    """Indices of the `count` largest local maxima of the sequence q."""
    inner = np.where((q[1:-1] >= q[:-2]) & (q[1:-1] >= q[2:]))[0] + 1
    cand = np.concatenate([inner, [0, len(q) - 1]])
    return cand[np.argsort(q[cand])[::-1][:count]]


def run_N(N, pool_size):
    t_start = time.time()
    K = _setup(N)
    dt = math.pi / math.log(N)
    J = int(math.floor(0.9 * N / dt))
    ts = N / 10.0 + dt * np.arange(J + 1)
    blocks = [ts[a:a + 20 * CHUNK] for a in range(0, len(ts), 20 * CHUNK)]
    with Pool(pool_size) as pool:          # forked after _setup: workers share _G
        S = np.concatenate(pool.map(class_sums, blocks))
        P = np.abs(S) ** 2
        E = P.sum(axis=1)
        D2 = np.abs(S.sum(axis=1)) ** 2
        one_r = D2 / E
        jobs = [(k, float(ts[i]), dt) for k in range(K) for i in _local_maxima(P[:, k], N_CAND)]
        jobs += [(-1, float(ts[i]), dt) for i in _local_maxima(one_r, N_CAND)]
        refined = pool.map(_refine, jobs, chunksize=4)

    best = {}
    for kind, t, v in refined:
        if kind not in best or v > best[kind][1]:
            best[kind] = (t, v)

    n = _G["n"]
    om = _G["om"]
    per_class = {}
    for k in range(K):
        i = int(P[:, k].argmax())
        per_class[str(k + 1)] = dict(
            count=int((om == k + 1).sum()),
            sum_inverse=float((1.0 / n[om == k + 1]).sum()),
            mean=float(P[:, k].mean()),
            max_grid=float(P[i, k]),
            t_max_grid=float(ts[i]),
            max_refined=float(best[k][1]),
            t_max_refined=float(best[k][0]),
            peak_to_mean=float(best[k][1] / P[:, k].mean()),
        )
    kstar = max(range(K), key=lambda k: best[k][1])
    B = best[kstar][1]
    top = np.argsort(D2)[::-1][:max(1, int(PEAK_FRACTION * len(ts)))]
    res = dict(
        N=N, K_N=K, dt=dt, n_t=len(ts), t_first=float(ts[0]), t_last=float(ts[-1]),
        B=B, B_grid=float(P.max()), k_star=kstar + 1,
        alpha_B=math.log(B) / math.log(N),
        c_B=math.log(B) / math.log(math.log(N)),
        max_1pr_grid=float(one_r.max()), max_1pr=float(best[-1][1]),
        t_max_1pr=float(best[-1][0]),
        mean_1pr=float(one_r.mean()),
        mean_D2=float(D2.mean()), mean_E=float(E.mean()),
        mean_1pr_large_D=float(one_r[top].mean()),
        min_1pr_large_D=float(one_r[top].min()),
        threshold_large_D=float(D2[top].min()),
        # grid means of the three parts of |D|^4 = (E + X)^2, X = |D|^2 - E
        fourth_moment=dict(
            mean_D4=float((D2 ** 2).mean()),
            same_class=float((P ** 2).sum(axis=1).mean()),
            products_of_two_classes=float((E ** 2 - (P ** 2).sum(axis=1)).mean()),
            remainder=float((D2 ** 2 - E ** 2).mean()),
        ),
        per_class=per_class,
    )
    if N == N_LIST[-1] or len(N_LIST) == 1:
        res["size_bins"] = {str(k + 1): size_bins(k, best[k][0]) for k in (1, 2) if k < K}
        # values of every class at the point where S_3 is largest
        if K >= 3:
            Sp = class_sums([best[2][0]])[0]
            res["classes_at_S3_peak"] = dict(
                t=best[2][0], abs2=[float(abs(z) ** 2) for z in Sp],
                one_plus_r=float(abs(Sp.sum()) ** 2 / (np.abs(Sp) ** 2).sum()))
    res["runtime_s"] = time.time() - t_start
    return res


def size_bins(k, t):
    """Contributions to S_{k+1}(t;N) of the ranges [10^j, 10^{j+1})."""
    n, om, N = _G["n"], _G["om"], _G["N"]
    terms = n.astype(np.float64) ** -0.5 * np.exp(-1j * t * _G["logn"])
    edges = [1] + [10 ** j for j in range(1, 12) if 10 ** j <= N] + [N + 1]
    rows = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (om == k + 1) & (n >= lo) & (n < hi)
        if m.any():
            c = terms[m].sum()
            rows.append(dict(lo=int(lo), hi=int(hi - 1 if hi == N + 1 else hi),
                             closed=bool(hi == N + 1), count=int(m.sum()),
                             abs=float(abs(c)), arg=float(np.angle(c)),
                             re=float(c.real), im=float(c.imag)))
    total = sum(complex(r["re"], r["im"]) for r in rows)
    return dict(
        t=float(t), bins=rows, abs2=float(abs(total) ** 2),
        sum_abs=float(sum(r["abs"] for r in rows)),
        sum_abs2=float(sum(r["abs"] ** 2 for r in rows)),
        resultant_length=float(abs(total) / sum(r["abs"] for r in rows)),
        ratio_to_sum_of_squares=float(abs(total) ** 2 / sum(r["abs"] ** 2 for r in rows)),
    )


# ---------------------------------------------------------------- Liouville
def liouville(N, t):
    omega, Omega = omega_arrays(N)
    n = np.arange(1, N + 1)
    lam = (-1.0) ** Omega[1:]
    terms = lam * n.astype(np.float64) ** -0.5 * np.exp(-1j * t * np.log(n))
    by_Omega = [terms[Omega[1:] == j].sum() for j in range(0, int(Omega.max()) + 1)]
    by_omega = [terms[omega[1:] == j].sum() for j in range(0, int(omega.max()) + 1)]
    D = terms.sum()
    return dict(
        N=N, t=t, abs_D=float(abs(D)), abs_D_from_2=float(abs(D - terms[0])),
        rms=float(math.sqrt((1.0 / n).sum())),
        ratio_to_sum_abs_Omega_classes=float(abs(D) / sum(abs(z) for z in by_Omega)),
        ratio_to_sum_abs_omega_classes=float(abs(D) / sum(abs(z) for z in by_omega)),
    )


# --------------------------------------------------------------- validation
def validate(N=10_000, points=3):
    import mpmath as mp
    mp.mp.dps = 50
    _setup(N)
    rng = np.random.default_rng(0)
    errs = []
    for t in rng.uniform(N / 10, N, points):
        approx = class_sums([t])[0].sum()
        ref = mp.fsum(mp.power(m, mp.mpc(-0.5, -float(t))) for m in range(2, N + 1))
        errs.append(float(abs(complex(ref) - approx)))
    return dict(N=N, max_abs_error=max(errs))


def zeta_near(t, half_width=1.5, step=0.01):
    """Zeros of zeta(1/2+iu) for |u-t| <= half_width (sign changes of Hardy's Z),
    and the values |zeta(1/2+it)|, |zeta(1+2it)/zeta(1/2+it)|."""
    import mpmath as mp
    mp.mp.dps = 20
    us = [t - half_width + step * i for i in range(int(round(2 * half_width / step)) + 1)]
    zs = [mp.siegelz(u) for u in us]
    zeros = [float(mp.findroot(mp.siegelz, (u, u + step), solver="anderson"))
             for u, a, b in zip(us, zs, zs[1:]) if a * b < 0]
    z = mp.zeta(mp.mpc(0.5, t))
    return dict(t=t, zeros=zeros, abs_zeta=float(abs(z)),
                abs_zeta2s_over_zeta=float(abs(mp.zeta(mp.mpc(1, 2 * t)) / z)))


# ------------------------------------------------------------------ figures
def figures(results, outdir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 10, "savefig.dpi": 300, "savefig.bbox": "tight"})
    os.makedirs(outdir, exist_ok=True)

    def save(fig, name):
        fig.savefig(os.path.join(outdir, name + ".pdf"))
        fig.savefig(os.path.join(outdir, name + ".png"))
        plt.close(fig)

    Ns = [r["N"] for r in results]

    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.plot(Ns, [r["alpha_B"] for r in results], "o-", color="k")
    for r in results:
        ax.annotate(f"$k^*={r['k_star']}$", (r["N"], r["alpha_B"]),
                    textcoords="offset points", xytext=(0, 7), ha="center", fontsize=9)
    ax.axhline(0.5, ls=":", color="gray")
    ax.axhline(13 / 42, ls="--", color="gray")
    ax.text(Ns[0], 0.505, r"$\alpha=1/2$", fontsize=8, va="bottom")
    ax.text(Ns[0], 13 / 42 + 0.005, r"$\alpha=13/42$", fontsize=8, va="bottom")
    ax.set_xscale("log")
    ax.set_xlim(Ns[0] * 0.75, Ns[-1] * 1.35)
    ax.set_ylim(0.28, 0.54)
    ax.set_xlabel("$N$")
    ax.set_ylabel(r"$\log B/\log N$")
    save(fig, "fig1_alpha_B_trend")

    if all("3" in r["per_class"] for r in results):
        fig, ax = plt.subplots(figsize=(5.6, 3.6))
        for k, mk in (("2", "o-"), ("3", "s--")):
            ax.plot(Ns, [r["per_class"][k]["max_refined"] for r in results], mk,
                    label=rf"$k={k}$")
        ax.set_xscale("log")
        ax.set_xlabel("$N$")
        ax.set_ylabel(r"largest value found of $|S_k(t;N)|^2$")
        ax.legend(frameon=False)
        save(fig, "fig2_crossover")

    r = results[-1]
    ks = sorted(r["per_class"], key=int)
    x = np.arange(len(ks))
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.bar(x - 0.2, [r["per_class"][k]["mean"] for k in ks], 0.4, label="grid mean",
           color="0.65")
    ax.bar(x + 0.2, [r["per_class"][k]["max_refined"] for k in ks], 0.4,
           label="largest value found", color="0.25")
    ax.plot(x, [r["per_class"][k]["sum_inverse"] for k in ks], "k_", ms=14,
            label=r"$\sum_{\omega(n)=k} 1/n$")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(ks)
    ax.set_xlabel("$k$")
    ax.set_ylabel(r"$|S_k(t;N)|^2$")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "fig3_peak_to_mean")

    if "size_bins" in r and "3" in r["size_bins"]:
        sb = r["size_bins"]["3"]
        fig, ax = plt.subplots(figsize=(4.6, 4.6))
        z = 0j
        pts = [z]
        for j, b in enumerate(sb["bins"]):
            c = complex(b["re"], b["im"])
            ax.annotate("", xy=((z + c).real, (z + c).imag), xytext=(z.real, z.imag),
                        arrowprops=dict(arrowstyle="->", color=f"C{j}", lw=1.8))
            ket = "]" if b["closed"] else ")"
            ax.plot([], [], color=f"C{j}", label=f"[{b['lo']:g}, {b['hi']:g}{ket}")
            z += c
            pts.append(z)
        ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color="k", lw=1.2, ls="--"))
        ax.plot([], [], "k--", label="$S_3$")
        xs = [p.real for p in pts]
        ys = [p.imag for p in pts]
        span = max(max(xs) - min(xs), max(ys) - min(ys)) * 0.6
        cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
        ax.set_xlim(cx - span, cx + span)
        ax.set_ylim(cy - span, cy + span)
        ax.set_aspect("equal")
        ax.axhline(0, color="0.8", lw=0.6)
        ax.axvline(0, color="0.8", lw=0.6)
        ax.set_xlabel("Re")
        ax.set_ylabel("Im")
        ax.legend(frameon=False, fontsize=8, loc="best")
        save(fig, "fig4_resonance")


# --------------------------------------------------------------------- main
def main():
    global N_LIST
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="N = 10^4 only")
    ap.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--no-figures", action="store_true")
    ap.add_argument("--from-json", action="store_true",
                    help="reuse the class-sum results of an earlier run")
    args = ap.parse_args()
    if args.quick:
        N_LIST = [10_000]
    json_path = os.path.join(args.out, "results", "computation_results.json")

    results = []
    if args.from_json:
        with open(json_path) as f:
            results = json.load(f)["results"]
    for N in ([] if args.from_json else N_LIST):
        r = run_N(N, args.workers)
        results.append(r)
        print(f"N={N}: K_N={r['K_N']} grid points={r['n_t']} B>={r['B']:.2f} "
              f"(grid {r['B_grid']:.2f}) k*={r['k_star']} alpha_B={r['alpha_B']:.4f} "
              f"max(1+r)={r['max_1pr']:.3f} (grid {r['max_1pr_grid']:.3f}) "
              f"[{r['runtime_s']:.0f} s]", flush=True)
        for k, c in r["per_class"].items():
            print(f"   k={k}: count={c['count']:6d} sum 1/n={c['sum_inverse']:.4f} "
                  f"mean={c['mean']:.4f} max={c['max_refined']:.2f} "
                  f"(grid {c['max_grid']:.2f}) at t={c['t_max_refined']:.3f}")

    out = dict(grid="t_j = N/10 + j*pi/log(N), t_j <= N; maxima refined between grid points",
               results=results,
               liouville=liouville(LIOUVILLE_N, LIOUVILLE_T))
    print("Liouville:", out["liouville"])
    if args.validate:
        out["validation"] = validate()
        out["zeta_near_liouville_point"] = zeta_near(LIOUVILLE_T)
        print("validation:", out["validation"])
        print("zeta:", out["zeta_near_liouville_point"])

    os.makedirs(os.path.join(args.out, "results"), exist_ok=True)
    with open(json_path, "w") as f:
        json.dump(out, f, indent=1)
    if not args.no_figures:
        figures(results, os.path.join(args.out, "figures"))


if __name__ == "__main__":
    main()
