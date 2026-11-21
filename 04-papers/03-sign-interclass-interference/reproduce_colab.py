# =============================================================================
#  On the sign of inter-class interference in Dirichlet partial sums
#  Computations for the paper (self-contained, no external data).
#
#  Produces:
#    * the decile means of r by decile of |D|          (Observation 4.1, Table 1)
#    * the sample statistics of r, X and E quoted in Sections 3 and 4
#    * the same profile for the random completely multiplicative control
#    * the values at the point t = 150000                        (Remark 5.1)
#    * the figure rbar_vs_quantile.{pdf,png}                        (Figure 1)
#
#  Requirements: numpy, matplotlib.  All arithmetic is in double precision.
# =============================================================================

import numpy as np

CFG = dict(
    N            = 100_000,         # length of the Dirichlet partial sum
    T_LO         = 100_000.0,       # sample window [T_LO, T_LO + WIN_WIDTH)
    WIN_WIDTH    = 3000.0,
    N_BANDS      = 10,              # deciles of |D|
    SEEDS        = [42, 137, 271, 314, 577],   # random multiplicative control
    POINT_T      = 150_000.0,       # the point of Section 5
    POINT_HALFWIDTH = 50.0,         # neighbourhood [POINT_T - 50, POINT_T + 50)
    N_ALT        = 150_000,         # second length used at POINT_T
)


# ---- 1. smallest prime factor and omega(n) ---------------------------------
def spf_array(N):
    """Smallest prime factor of n for 2 <= n <= N (entries 0, 1 are 0)."""
    spf = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if spf[p] == 0:
            seg = spf[p::p]
            seg[seg == 0] = p
    return spf


def omega_array(N, spf=None):
    """omega(n) = number of distinct prime factors of n, 0 <= n <= N."""
    if spf is None:
        spf = spf_array(N)
    omega = np.zeros(N + 1, dtype=np.int64)
    for n in range(2, N + 1):
        p = spf[n]
        m = n // p
        omega[n] = omega[m] + (1 if m % p else 0)
    return omega


# ---- 2. coefficients -------------------------------------------------------
def coeffs_zeta(N):
    a = np.ones(N + 1, dtype=np.complex128)
    a[0] = 0.0
    return a


def coeffs_random_mult(N, seed):
    """a_p = exp(i theta_p), theta_p i.i.d. uniform on [0, 2 pi), drawn in
    increasing order of p, and a_{mn} = a_m a_n for all m, n."""
    rng = np.random.default_rng(seed)
    spf = spf_array(N)
    a = np.zeros(N + 1, dtype=np.complex128)
    a[1] = 1.0
    for n in range(2, N + 1):
        p = spf[n]
        if p == n:
            a[n] = np.exp(1j * rng.uniform(0, 2 * np.pi))
        else:
            a[n] = a[n // p] * a[p]
    return a


# ---- 3. class sums S_k(t), D, E and r --------------------------------------
class Engine:
    """Evaluates the class sums of sum_{n<=N} a_n n^{-1/2-it}."""

    def __init__(self, a, N):
        omega = omega_array(N)[1:]
        n = np.arange(1, N + 1, dtype=np.float64)
        order = np.argsort(omega, kind="stable")       # group n by omega(n)
        self.N = N
        self.logn = np.log(n)[order]
        self.coef = (a[1:] * n ** -0.5)[order]
        counts = np.bincount(omega)
        self.bounds = np.concatenate(([0], np.cumsum(counts)))
        self.K = len(counts)                           # number of classes

    def classes(self, t):
        term = self.coef * np.exp(-1j * t * self.logn)
        b = self.bounds
        return np.array([term[b[k]:b[k + 1]].sum() for k in range(self.K)])

    def point(self, t):
        """Return (r, |D|, E) at t."""
        S = self.classes(t)
        D2 = abs(S.sum()) ** 2
        E = float(np.sum(np.abs(S) ** 2))
        return (D2 - E) / E, np.sqrt(D2), E

    def sample(self, ts):
        out = np.array([self.point(t) for t in ts])
        return out[:, 0], out[:, 1], out[:, 2]


def zero_crossing(q, y):
    """Abscissa where the piecewise linear interpolant of (q, y) vanishes."""
    i = np.where(np.diff(np.sign(y)) != 0)[0][0]
    return q[i] - y[i] * (q[i + 1] - q[i]) / (y[i + 1] - y[i])


# ---- 4. decile profile on the sample window --------------------------------
def analyse(eng, label, cfg=CFG, full=False):
    N = eng.N
    dt = 2 * np.pi / np.log(N)
    ts = np.arange(cfg["T_LO"], cfg["T_LO"] + cfg["WIN_WIDTH"], dt)
    r, D, E = eng.sample(ts)

    order = np.argsort(D)
    bands = np.array_split(order, cfg["N_BANDS"])
    rbar = np.array([r[b].mean() for b in bands])
    q = (np.arange(cfg["N_BANDS"]) + 0.5) / cfg["N_BANDS"]

    print(f"\n=== {label}  (N={N}, {len(ts)} points, "
          f"t in [{ts[0]:.0f}, {ts[-1]:.2f}], classes K={eng.K}) ===")
    print("  band   mean r   mean E")
    for qq, b in zip(q, bands):
        print(f"  {qq:4.2f}  {r[b].mean():+.4f}  {E[b].mean():8.3f}")
    print(f"  lowest decile : mean r = {r[bands[0]].mean():+.4f}, "
          f"fraction r<0 = {(r[bands[0]] < 0).mean():.3f}")
    print(f"  highest decile: mean r = {r[bands[-1]].mean():+.4f}, "
          f"fraction r>0 = {(r[bands[-1]] > 0).mean():.3f}")
    print(f"  band means increasing: {bool(np.all(np.diff(rbar) > 0))}; "
          f"sign change (linear interpolation) at q = {zero_crossing(q, rbar):.3f}")
    if full:
        top50 = order[-50:]
        X = D ** 2 - E
        print(f"  50 largest |D|: mean r = {r[top50].mean():+.4f}, "
              f"fraction r>0 = {(r[top50] > 0).mean():.2f}")
        print(f"  whole sample: r in [{r.min():+.4f}, {r.max():+.4f}], "
              f"mean r = {r.mean():+.4f}, median r = {np.median(r):+.4f}, "
              f"fraction r<0 = {(r < 0).mean():.3f}")
        print(f"  whole sample: mean X = {X.mean():+.3f}, mean E = {E.mean():.3f}, "
              f"mean |D|^2 = {(D ** 2).mean():.3f}")
        print(f"  E in [{E.min():.3f}, {E.max():.2f}], sd(E)/mean(E) = "
              f"{E.std() / E.mean():.3f}")
    return q, rbar


# ---- 5. the point t = 150000 -----------------------------------------------
def point_test(eng, cfg=CFG):
    t0 = cfg["POINT_T"]
    N = eng.N
    r0, D0, E0 = eng.point(t0)
    print(f"\n=== t = {t0:.0f}, N = {N} ===")
    print(f"  |D| = {D0:.4f}, E = {E0:.4f}, r = {r0:+.4f}")

    # nearest local minimum of |D|
    fine = np.arange(t0 - 1.0, t0 + 1.0, 1e-3)
    rf, Df, _ = eng.sample(fine)
    j = np.argmin(Df)
    print(f"  on [t0-1, t0+1]: min |D| = {Df[j]:.4f} at t = {fine[j]:.3f} "
          f"(r = {rf[j]:+.4f}); r ranges over [{rf.min():+.3f}, {rf.max():+.3f}]")

    # neighbourhood sample of spacing 2 pi / log N
    dt = 2 * np.pi / np.log(N)
    loc = np.arange(t0 - cfg["POINT_HALFWIDTH"], t0 + cfg["POINT_HALFWIDTH"], dt)
    rl, Dl, _ = eng.sample(loc)
    top = np.array_split(np.argsort(Dl), cfg["N_BANDS"])[-1]
    print(f"  neighbourhood sample: {len(loc)} points; fraction with |D| smaller "
          f"than at t0 = {(Dl < D0).mean():.3f}")
    print(f"  neighbourhood top decile of |D|: mean r = {rl[top].mean():+.4f}")


# ---- 6. run ----------------------------------------------------------------
if __name__ == "__main__":
    N = CFG["N"]

    eng_z = Engine(coeffs_zeta(N), N)
    qz, rz = analyse(eng_z, "zeta", full=True)
    point_test(eng_z)

    N2 = CFG["N_ALT"]
    r2, D2, E2 = Engine(coeffs_zeta(N2), N2).point(CFG["POINT_T"])
    print(f"\n=== t = {CFG['POINT_T']:.0f}, N = {N2} ===")
    print(f"  |D| = {D2:.4f}, E = {E2:.4f}, r = {r2:+.4f}")

    rbars = []
    for s in CFG["SEEDS"]:
        q, rb = analyse(Engine(coeffs_random_mult(N, s), N),
                        f"random multiplicative, seed {s}")
        rbars.append(rb)
    rbars = np.array(rbars)
    r_mean, r_sd = rbars.mean(axis=0), rbars.std(axis=0)
    print("\n=== random multiplicative control, five seeds ===")
    print("  band   mean     s.d.")
    for qq, m, s in zip(qz, r_mean, r_sd):
        print(f"  {qq:4.2f}  {m:+.4f}  {s:.4f}")
    print(f"  mean over the sample (average of the band means) = {r_mean.mean():+.4f}")
    print(f"  sign change (linear interpolation) at q = {zero_crossing(qz, r_mean):.3f}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        q0 = zero_crossing(qz, rz)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.axhline(0, color="gray", lw=0.8)
        ax.axvline(q0, color="black", lw=0.8, ls=":")
        ax.plot(qz, rz, "o-", color="C0", label=r"$\zeta$")
        ax.errorbar(qz, r_mean, yerr=r_sd, fmt="s--", color="C1", capsize=2,
                    label=r"random mult. (mean $\pm$ s.d., 5 seeds)")
        ax.annotate(rf"sign change at $q\approx{q0:.2f}$", (q0 + 0.01, -0.5),
                    fontsize=8)
        ax.set_xlabel(r"decile of $|D_F|$ (band midpoint $q$)")
        ax.set_ylabel(r"$\bar r(q)$")
        ax.legend(loc="upper left")
        fig.tight_layout()
        fig.savefig("rbar_vs_quantile.png", dpi=300)
        fig.savefig("rbar_vs_quantile.pdf")
        print("\nSaved rbar_vs_quantile.png and rbar_vs_quantile.pdf")
    except Exception as e:
        print("plot skipped:", e)
