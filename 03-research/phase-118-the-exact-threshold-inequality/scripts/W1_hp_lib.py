"""High-precision (mpmath) reimplementation of rowd_assembly.py + rowd_threshold.py,
built from scratch in closed form (no reuse of float64 arithmetic), for W1's
criticality question (RESUME.md item c-NEW).

Does NOT import or modify rowd_assembly.py / rowd_threshold.py.  Every matrix
entry here is assembled directly from mpmath high-precision primitives:
  - mesh breakpoints via mp.log, exact linspace subdivision;
  - shift_form / Gram: exact interval-overlap arithmetic (max/min), no series;
  - Gamma kernel Psi(D) = sum_j exp(-a_j|D|)/a_j^2 (a_j=2j+1/2): the D=0 value
    is the closed form (1/4) zeta(2,1/4) (Hurwitz zeta; equals (1/4)psi'(1/4),
    matching rowd_assembly's polygamma(1,.25) call); D>0 values are summed
    directly term-by-term with a multiplicative recurrence (avoids one exp()
    call per term) to a working tolerance tied to the working precision, with
    NO Euler-Maclaurin truncation -- this is the "just sum more terms" route
    the phase brief asks for, and it is checked against rowd_assembly's
    Euler-Maclaurin value in W1_hp_validate.py.
  - Tate moments: closed-form exp integrals.

Numerically-sensitive linear algebra policy (this is the point of the file):
  - R0, S_E, and the corona Gram matrix are treated as genuinely nonsingular
    (matches the float64 pinv-sweep finding in RESUME.md (a), which found A0
    -- not R0/S_E -- is the only near-singular block): solved via mp.lu_solve
    or mp.cholesky, not via a truncated pseudo-inverse.  This is far cheaper
    than mp.eigsy and, because these blocks are well conditioned, no less
    accurate.
  - A0 is the one block treated as possibly near-singular.  Its full
    eigendecomposition (mp.eigsy) IS computed (this is the expensive,
    load-bearing step) and used two ways:
      (i)  a cutoff pseudo-inverse, matching rowd_threshold._psd_pinv exactly
           (rtol on eigenvalues), for direct comparison to the float64 code;
      (ii) the exact eps-regularized penalty pen(eps) = b^T (A0+eps)^{-1} b,
           computed from the SAME eigendecomposition (cheap: no new solves),
           to see the eps->0 limit and monotonicity.
  - The independent cross-check (thm:newdRegularizedStep's C_eps, using D_0,
    Q_c, D_E) is built from R0 and S_E's OWN eigendecompositions (needed to
    form R0^{-1/2}, S_E^{-1/2} once) and then regularizes D_0 via mp.lu_solve
    at each eps -- never forming or eigendecomposing A0 at all.  Agreement
    between this route and the A0-pinv route, computed independently, is the
    strongest evidence available.

Run nothing on import; this is a library.  See W1_hp_validate.py, W1_hp_run.py.
"""
import math
import mpmath as mp


# ------------------------------------------------------------- constants ---
def m0_const():
    return mp.log(mp.pi) + mp.euler + mp.pi / 2 + 3 * mp.log(2)


# ---------------------------------------------------------------- sieve ---
def von_mangoldt(N):
    lam = [0.0] * (N + 1)
    sieve = [True] * (N + 1)
    for p in range(2, N + 1):
        if sieve[p]:
            for m in range(p * p, N + 1, p):
                sieve[m] = False
            q, lp = p, math.log(p)
            while q <= N:
                lam[q] = lp
                q *= p
    return lam


def prime_powers_upto(N):
    lam = von_mangoldt(N)
    return [n for n in range(2, N + 1) if lam[n] > 0]


# ------------------------------------------------------------ Gamma kernel
def _psi_at_zero():
    return mp.zeta(2, mp.mpf(1) / 4) / 4


def _psi_direct(D, tol=None):
    """Psi(D) = sum_{j>=0} exp(-a_j D)/a_j^2, a_j=2j+1/2, D>0, by direct
    term-by-term summation using a multiplicative recurrence between
    consecutive terms (avoids repeated exp() calls).  Terms are positive and
    strictly decreasing, so summing until term < tol is a valid stopping
    rule."""
    if tol is None:
        tol = mp.mpf(10) ** (-(mp.mp.dps + 12))
    r = mp.e ** (-2 * D)
    a = mp.mpf('0.5')
    term = mp.e ** (-a * D) / a ** 2
    s = term
    it = 0
    max_it = 20_000_000
    while term > tol:
        a_new = a + 2
        term = term * r * (a / a_new) ** 2
        a = a_new
        s += term
        it += 1
        if it > max_it:
            raise RuntimeError(f"psi_direct did not converge for D={D} after {it} terms")
    return s, it


def psi_kernel_mp(D):
    if D == 0:
        return _psi_at_zero()
    s, _ = _psi_direct(D)
    return s


def make_psi_table(deltas, keydigits=None):
    """deltas: iterable of mpf (already |.|).  Returns dict keyed by a
    rounded-string key -> mpf value, and the key function to look values up.
    Caches by unique value so each distinct |D| is summed once."""
    if keydigits is None:
        keydigits = max(15, mp.mp.dps - 5)

    def key(x):
        return mp.nstr(x, keydigits, strip_zeros=False)

    uniq = {}
    for d in deltas:
        k = key(d)
        if k not in uniq:
            uniq[k] = d
    tab = {}
    for k, d in uniq.items():
        tab[k] = psi_kernel_mp(d)
    return tab, key


# ------------------------------------------------------------------- mesh
def build_mesh_mp(T, extra_points, refine):
    """T: mpf.  extra_points: iterable of mpf.  Returns (c,d) as python lists
    of mpf, matching rowd_assembly.build_mesh's breakpoint set and ordering
    logic exactly (log of prime powers, T, 0, extras), each interval cut into
    `refine` equal mpf sub-cells."""
    Tf = float(T)
    N = int(math.floor(math.exp(2 * Tf)))
    pts = {(-T), T, mp.mpf(0)}
    for n in prime_powers_upto(max(N, 2)):
        ln = mp.log(n)
        for s in (1, -1):
            x = s * ln
            if -T < x < T:
                pts.add(x)
    for x in extra_points:
        if -T < x < T:
            pts.add(x)
    base = sorted(pts)
    edges = []
    for lo, hi in zip(base[:-1], base[1:]):
        step = (hi - lo) / refine
        for k in range(refine):
            edges.append(lo + k * step)
    edges.append(base[-1])
    c = edges[:-1]
    d = edges[1:]
    return c, d, N


# ---------------------------------------------------------------- matrices
def gram_matrix_mp(c, d):
    n = len(c)
    G = mp.matrix(n, n)
    for i in range(n):
        G[i, i] = d[i] - c[i]
    return G


def shift_form_mp(c, d, a):
    n = len(c)
    S = mp.matrix(n, n)
    for i in range(n):
        ci, di = c[i], d[i]
        for j in range(n):
            lo = max(ci, c[j] - a)
            hi = min(di, d[j] - a)
            v = hi - lo
            if v > 0:
                S[i, j] = v
    return S


def gamma_form_mp(c, d):
    n = len(c)
    allD = []
    for i in range(n):
        for j in range(n):
            allD.append(abs(c[i] - c[j]))
            allD.append(abs(c[i] - d[j]))
            allD.append(abs(d[i] - c[j]))
            allD.append(abs(d[i] - d[j]))
    tab, key = make_psi_table(allD)

    def P(i, j, X):
        return tab[key(abs(X))]

    G = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            G[i, j] = (tab[key(abs(c[i] - c[j]))] - tab[key(abs(c[i] - d[j]))]
                       - tab[key(abs(d[i] - c[j]))] + tab[key(abs(d[i] - d[j]))])
    return G


def tate_moments_mp(c, d):
    n = len(c)
    M = mp.matrix(2, n)
    for i in range(n):
        M[0, i] = 2 * (mp.e ** (-c[i] / 2) - mp.e ** (-d[i] / 2))
        M[1, i] = 2 * (mp.e ** (d[i] / 2) - mp.e ** (c[i] / 2))
    return M


def assemble_mp(T, refine, extra_points=()):
    c, d, N = build_mesh_mp(T, extra_points, refine)
    n = len(c)
    G = gamma_form_mp(c, d)
    Gram = gram_matrix_mp(c, d)
    M0 = m0_const()
    R = mp.matrix(G)
    L = M0 * Gram
    A = G - M0 * Gram
    lam = von_mangoldt(max(N, 2))
    Tf = float(T)
    for p in prime_powers_upto(max(N, 2)):
        if not (p < math.exp(2 * Tf) - 1e-13):
            continue
        w = mp.mpf(lam[p]) / mp.sqrt(p)
        S = shift_form_mp(c, d, mp.log(p))
        sym = S + S.transpose()
        A -= w * sym
        R += w * (Gram - mp.mpf('0.5') * sym)
        L += w * (Gram + mp.mpf('0.5') * sym)
    return dict(c=c, d=d, Gram=Gram, G=G, R=R, L=L, A=A,
                Tate=tate_moments_mp(c, d), T=T, N=N, n=n)


# --------------------------------------------------------- linear algebra
def eigsy_full(M, eigvals_only=False):
    return mp.eigsy(M, eigvals_only=eigvals_only)


def svd_nullspace(M, rtol=None):
    """M: m x n mpf matrix.  Returns an n x k matrix whose columns are an
    orthonormal basis of the (numerical) nullspace of M, via full SVD."""
    m, n = M.rows, M.cols
    if rtol is None:
        rtol = mp.mpf(10) ** (-(mp.mp.dps - 8))
    U, S, V = mp.svd_r(M, full_matrices=True)
    smax = max(S) if len(S) else mp.mpf(0)
    k = sum(1 for s in S if s > rtol * smax)
    # V has shape min(m,n) x n when full_matrices=False; need full V (n x n)
    Vt = V  # rows of V are right singular vectors (n-dim), full_matrices=True -> n x n
    ns_rows = Vt.rows
    cols = []
    for i in range(k, ns_rows):
        cols.append(i)
    if not cols:
        return mp.matrix(n, 0)
    Nn = mp.matrix(n, len(cols))
    for jj, i in enumerate(cols):
        for c in range(n):
            Nn[c, jj] = Vt[i, c]
    return Nn


def mat_solve(A, B):
    """Solve A X = B for X (A square, B same #rows), via LU.  B may be a
    matrix (multiple RHS) -- looped column by column since mpmath's lu_solve
    expects a vector-like RHS reliably across versions."""
    if isinstance(B, mp.matrix) and B.cols > 1:
        X = mp.matrix(A.cols, B.cols)
        lu = mp.lu(A)
        for j in range(B.cols):
            col = mp.matrix([B[i, j] for i in range(B.rows)])
            xj = mp.lu_solve(A, col)
            for i in range(A.cols):
                X[i, j] = xj[i]
        return X
    else:
        return mp.lu_solve(A, B)


def cholesky_whiten(Gr, rtol=None):
    """Gr: symmetric PD (assumed full rank) k x k Gram matrix.  Returns L
    (lower Cholesky factor) so that inv(L) applied to a k-vector maps the Gr
    metric to the identity metric.  Falls back to eigsy-based whitening if
    Cholesky fails (Gr not numerically PD to the working precision)."""
    try:
        L = mp.cholesky(Gr)
        return ('chol', L)
    except Exception:
        w, V = mp.eigsy(Gr)
        return ('eig', (w, V))


def transpose(M):
    return M.transpose()
