# =============================================================================
#  P6 — On the Sign of Inter-Class Interference in Dirichlet Partial Sums
#  Reproducibility notebook (Google Colab ready, self-contained, no external data)
#
#  Paste into a Colab cell (or run as a script). It reproduces every
#  quantitative claim of the note:
#    * the monotone curve  r_bar(q)  vs the |D| quantile  (Theorem 5.1 / Fig. 1)
#    * destructive r<0 at troughs, constructive r>0 at peaks
#    * the t=150000 anchor is a trough with r ~ -0.82       (Prop. 6.1)
#    * the random-multiplicative control
#
#  Author: D. A. Trejo Pizzo, 2026.  License: CC-BY.
# =============================================================================

# ---- 0. Config -------------------------------------------------------------
import numpy as np

CFG = dict(
    N            = 100_000,         # number of terms in the Dirichlet sum
    T_LO         = 100_000.0,       # window for the quantile analysis: lower t
    WIN_WIDTH    = 3000.0,          # window width (kept modest so Colab is fast)
    N_QUANTILES  = 10,              # deciles for r_bar(q)
    SEEDS        = [42, 137, 271, 314, 577],   # random-multiplicative realisations
    ANCHOR_T     = 150_000.0,       # the historically-cited abscissa
    ANCHOR_HALFWIDTH = 50.0,        # neighbourhood for the local-rank test
)
# For the paper's N=10^6 numbers and the full [1e5,2e5] trough census,
# set N=1_000_000 and WIN_WIDTH larger; expect minutes-to-tens-of-minutes.


# ---- 1. omega(n) via smallest-prime-factor sieve ---------------------------
def omega_array(N):
    """omega(n) = number of DISTINCT prime factors, for n=1..N. omega(1)=0."""
    spf = np.zeros(N + 1, dtype=np.int64)          # smallest prime factor
    for p in range(2, N + 1):
        if spf[p] == 0:                             # p is prime
            spf[p::p][spf[p::p] == 0] = p
    omega = np.zeros(N + 1, dtype=np.int8)
    for n in range(2, N + 1):
        m, last = n, 0
        c = 0
        while m > 1:
            p = spf[m]
            if p != last:
                c += 1
                last = p
            m //= p
        omega[n] = c
    return omega


# ---- 2. coefficient generators --------------------------------------------
def coeffs_zeta(N):
    a = np.ones(N + 1, dtype=np.complex128)
    a[0] = 0.0
    return a

def coeffs_random_mult(N, seed):
    """a_p = e^{i theta_p} on primes, extended multiplicatively."""
    rng = np.random.default_rng(seed)
    spf = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if spf[p] == 0:
            spf[p::p][spf[p::p] == 0] = p
    ap = {}
    a = np.zeros(N + 1, dtype=np.complex128)
    a[1] = 1.0
    for n in range(2, N + 1):
        p = spf[n]; m = n // p
        if m == 1:                                  # n is prime
            ap[p] = np.exp(1j * rng.uniform(0, 2*np.pi))
            a[n] = ap[p]
        else:
            a[n] = a[m] * ap[p] if (m % p) else a[m] * ap[p]   # fully mult.
    return a


# ---- 3. Kahan-compensated class sums S_k(t) and r(t) -----------------------
def class_sums_at_t(t, n, n_pow, logn, omega, a, Kmax):
    """Return S_k for k=0..Kmax at a single t, Kahan-summed per class."""
    phase = np.exp(-1j * t * logn)                  # n^{-it}
    term  = a * n_pow * phase                       # a_n * n^{-1/2-it}
    S = np.zeros(Kmax + 1, dtype=np.complex128)
    # group by omega using bincount on real/imag separately (Kahan-lite)
    for k in range(Kmax + 1):
        mask = (omega == k)
        if mask.any():
            S[k] = np.sum(term[mask])               # numpy pairwise sum
    return S

def r_of_t(t, n, n_pow, logn, omega, a, Kmax):
    S = class_sums_at_t(t, n, n_pow, logn, omega, a, Kmax)
    D = S.sum()
    E = np.sum(np.abs(S)**2)
    X = np.abs(D)**2 - E
    return X / E, np.abs(D)


# ---- 4. driver: quantile-stratified r_bar(q) -------------------------------
def analyse(a, label, cfg=CFG):
    N = cfg["N"]
    idx   = np.arange(1, N + 1)
    omega = omega_array(N)[1:]
    a     = a[1:]
    n_pow = idx.astype(np.float64) ** -0.5
    logn  = np.log(idx.astype(np.float64))
    Kmax  = int(omega.max())

    dt = 2*np.pi / np.log(N)
    ts = np.arange(cfg["T_LO"], cfg["T_LO"] + cfg["WIN_WIDTH"], dt)
    rs = np.empty_like(ts); Ds = np.empty_like(ts)
    for i, t in enumerate(ts):
        rs[i], Ds[i] = r_of_t(t, idx, n_pow, logn, omega, a, Kmax)

    # stratify r by the quantile band of |D|
    order = np.argsort(Ds)
    qbands = np.array_split(order, cfg["N_QUANTILES"])
    rbar = np.array([rs[b].mean() for b in qbands])
    qmid = (np.arange(cfg["N_QUANTILES"]) + 0.5) / cfg["N_QUANTILES"]

    # peak / trough census
    top_decile = qbands[-1]; bot_decile = qbands[0]
    print(f"\n=== {label}  (N={N}, {len(ts)} t-samples) ===")
    print(" q-band   r_bar")
    for q, rb in zip(qmid, rbar):
        print(f"  {q:4.2f}   {rb:+.4f}")
    print(f" troughs (lowest decile): mean r = {rs[bot_decile].mean():+.4f}, "
          f"frac r<0 = {(rs[bot_decile]<0).mean():.2f}")
    print(f" peaks   (top   decile):  mean r = {rs[top_decile].mean():+.4f}, "
          f"frac r>0 = {(rs[top_decile]>0).mean():.2f}")
    # zero crossing
    sign_change = np.where(np.diff(np.sign(rbar)) != 0)[0]
    if len(sign_change):
        print(f" r_bar(q) crosses zero near q = {qmid[sign_change[0]]:.2f}")
    return qmid, rbar, ts, rs, Ds, (idx, n_pow, logn, omega, a, Kmax)


# ---- 5. the t=150000 anchor: is it a trough? -------------------------------
def anchor_test(engine, cfg=CFG):
    idx, n_pow, logn, omega, a, Kmax = engine
    dt = 2*np.pi / np.log(cfg["N"])
    loc = np.arange(cfg["ANCHOR_T"] - cfg["ANCHOR_HALFWIDTH"],
                    cfg["ANCHOR_T"] + cfg["ANCHOR_HALFWIDTH"], dt)
    rloc = np.empty_like(loc); Dloc = np.empty_like(loc)
    for i, t in enumerate(loc):
        rloc[i], Dloc[i] = r_of_t(t, idx, n_pow, logn, omega, a, Kmax)
    j = np.argmin(np.abs(loc - cfg["ANCHOR_T"]))
    rank = (Dloc < Dloc[j]).mean()                  # local quantile rank of |D|
    print(f"\n=== anchor t={cfg['ANCHOR_T']:.0f} ===")
    print(f"  r(t)             = {rloc[j]:+.4f}")
    print(f"  local |D| rank   = {rank:.2f}  (0 = deepest trough, 1 = highest peak)")
    print(f"  verdict          = {'TROUGH' if rank < 0.5 else 'PEAK'}")
    return rloc[j], rank


# ---- 6. run ----------------------------------------------------------------
if __name__ == "__main__":
    # zeta
    qz, rz, *_z, eng_z = analyse(coeffs_zeta(CFG["N"]), "zeta")
    anchor_test(eng_z)

    # random multiplicative control (averaged over seeds)
    rbars = []
    for s in CFG["SEEDS"]:
        q, rb, *_ = analyse(coeffs_random_mult(CFG["N"], s), f"rand-mult seed={s}")
        rbars.append(rb)
    rbar_rand = np.mean(rbars, axis=0)

    # figure
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(6, 4))
        plt.axhline(0, color="gray", lw=0.8)
        plt.plot(qz, rz, "o-", label=r"$\zeta$")
        plt.plot(qz, rbar_rand, "s--", label="random mult. (mean of 5 seeds)")
        plt.xlabel(r"conditioning quantile $q$ of $|D_F|$")
        plt.ylabel(r"$\bar r(q)$")
        plt.title("Inter-class ratio: destructive at troughs, constructive at peaks")
        plt.legend(); plt.tight_layout()
        plt.savefig("P6_rbar_vs_quantile.png", dpi=300)
        plt.savefig("P6_rbar_vs_quantile.pdf")
        print("\nSaved P6_rbar_vs_quantile.{png,pdf}")
    except Exception as e:
        print("plot skipped:", e)
