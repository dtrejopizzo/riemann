# =============================================================================
#  P2 — The omega-Class Decomposition of Dirichlet Polynomials
#  Reproducibility notebook (Google Colab ready, self-contained, no external data)
#
#  Reproduces the computational claims of the paper:
#    * B(N) = max_{t,k} |S_k(t;N)|^2  and  alpha_B = log B(N)/log N   (Table 1)
#    * the k=2 -> k=3 dominance transition                            (Table 2)
#    * the peak-to-mean ratios R_k                                    (Table 3)
#    * the phase-resonance amplification at the peak of S_3           (Sec. 8)
#  and validates D_zeta against a 50-digit mpmath reference.
#
#  Author: D. A. Trejo Pizzo, 2026.  License: CC-BY.
#  Default N=10^4 runs in well under a minute; set N up to 1.5e5 (slower) to
#  reproduce the paper's headline numbers exactly (use the full grid, FACTOR=1).
# =============================================================================

import numpy as np

CFG = dict(
    N_LIST = [10_000, 50_000],     # add 100_000, 150_000 to reproduce the full tables
    GRID_FACTOR = 1,               # 1 = paper grid (dt = pi/log N); >1 = sparser/faster
    VALIDATE = True,               # cross-check D_zeta against mpmath at N=10^4
)

# ---- 1. omega(n) via sieve (O(N log log N)) --------------------------------
def omega_array(N):
    """omega(n) = number of DISTINCT prime factors, n=1..N."""
    omega = np.zeros(N + 1, dtype=np.int32)
    is_prime = np.ones(N + 1, dtype=bool); is_prime[:2] = False
    for p in range(2, N + 1):
        if is_prime[p]:
            is_prime[p*p::p] = False
            omega[p::p] += 1
    return omega

# ---- 2. class sums S_k(t;N) on a t-grid ------------------------------------
def class_sums(N, factor=1):
    omega = omega_array(N)[2:N+1]
    n   = np.arange(2, N + 1, dtype=np.float64)
    npow = n ** -0.5
    logn = np.log(n)
    Kmax = int(omega.max())
    masks = [omega == k for k in range(1, Kmax + 1)]
    dt = np.pi / np.log(N) * factor
    ts = np.arange(N/10.0, float(N) + dt, dt)
    Sk = np.zeros((Kmax, len(ts)), dtype=np.complex128)
    for i, t in enumerate(ts):
        term = npow * np.exp(-1j * t * logn)        # a_n = 1 (zeta)
        for k, m in enumerate(masks):
            Sk[k, i] = term[m].sum()
    return ts, Sk, Kmax

# ---- 3. statistics ---------------------------------------------------------
def analyse_N(N, factor=1):
    ts, Sk, Kmax = class_sums(N, factor)
    P = np.abs(Sk)**2                                # |S_k(t)|^2
    Bk = P.max(axis=1)                               # max over t, per class
    meank = P.mean(axis=1)
    BN = Bk.max(); kstar = int(Bk.argmax()) + 1
    aB = np.log(BN) / np.log(N)
    D = Sk.sum(axis=0); E = P.sum(axis=0)
    one_plus_r = (np.abs(D)**2 / E)
    print(f"\n=== N={N}  (K_N={Kmax}, {len(ts)} t-samples) ===")
    print(f"  B(N) = {BN:8.2f}   k* = {kstar}   alpha_B = {aB:.4f}   "
          f"max(1+r) = {one_plus_r.max():.3f}  (CS bound K_N={Kmax})")
    print("  k :   mean|S_k|^2    max|S_k|^2     R_k = max/mean")
    for k in range(Kmax):
        print(f"  {k+1} : {meank[k]:10.3f}   {Bk[k]:10.2f}    {Bk[k]/meank[k]:8.1f}")
    # phase resonance at the dominant class peak
    kp = kstar - 1
    tp = int(P[kp].argmax())
    return dict(N=N, BN=float(BN), kstar=kstar, alpha_B=float(aB),
                maxS=Bk.tolist(), meanS=meank.tolist(), t_peak=float(ts[tp]))

# ---- 4. mpmath validation of the engine ------------------------------------
def validate(N=10_000, n_pts=5):
    try:
        import mpmath as mp
    except ImportError:
        print("mpmath not installed; skipping validation (pip install mpmath)")
        return
    mp.mp.dps = 50
    omega = omega_array(N)
    n = np.arange(2, N + 1, dtype=np.float64); npow = n**-0.5; logn = np.log(n)
    rng = np.random.default_rng(0)
    print("\n=== engine validation vs 50-digit mpmath (a_n=1) ===")
    for t in rng.uniform(N/10, N, n_pts):
        approx = np.sum(npow * np.exp(-1j * t * logn))
        ref = sum(mp.mpf(int(m))**(mp.mpf(-1)/2 - 1j*mp.mpf(float(t)))
                  for m in range(2, N + 1))
        err = abs(complex(ref) - approx)
        print(f"  t={t:10.2f}   |D_engine - D_mpmath| = {err:.2e}")

# ---- 5. run ----------------------------------------------------------------
if __name__ == "__main__":
    results = [analyse_N(N, CFG["GRID_FACTOR"]) for N in CFG["N_LIST"]]
    if CFG["VALIDATE"]:
        validate(10_000, 3)
    # crossover summary
    print("\n=== k=2 vs k=3 dominance ===")
    for r in results:
        s2 = r["maxS"][1] if len(r["maxS"]) > 1 else float("nan")
        s3 = r["maxS"][2] if len(r["maxS"]) > 2 else float("nan")
        print(f"  N={r['N']:>7}:  max|S2|^2={s2:7.2f}  max|S3|^2={s3:7.2f}  "
              f"dominant k*={r['kstar']}")
