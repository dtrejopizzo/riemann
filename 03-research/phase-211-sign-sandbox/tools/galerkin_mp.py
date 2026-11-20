"""Multiprecision Galerkin matrices for the window form a_T (phase 211).  NUMERICAL tool.

Basis: Dirichlet sines e_k(t) = sin(k*pi*(t+T)/(2T))/sqrt(T), k = 1..N, on I_T = (-T, T),
orthonormal in L^2(I_T).  k odd -> e_k even; k even -> e_k odd.  Both forms preserve parity.

Archimedean form (Levy form, Paper 47 lem:K):
    Arch(F,G) = C_0 <F,G> + int_0^inf (c(0) - c^sym(u)) K(u) du,
    K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)),  C_0 = psi(1/4) - log(pi),
with c^sym the symmetrised cross-correlation of two basis sines, written in closed form.
All entries reduce to three families of one-dimensional integrals over [0, 2T]
    S_k = int K sin(a_k u),  D1_k = int K (1 - cos a_k u),  D2_k = int K u cos(a_k u),
(a_k = k pi / 2T) plus the exact tail int_{2T}^inf K.  The integrands are analytic on [0, 2T]
(the 1/u pole of K is cancelled), so composite Gauss-Legendre converges geometrically; the
error is estimated by recomputing with 1.5x as many panels and 8 more nodes per panel.
Comb form: Pi(F,G) = sum_n v_n c^sym(log n), exact closed form (no quadrature).
"""
import math, pickle, os, time, hashlib
import mpmath as mp
import numpy as np

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')

# ---------------------------------------------------------------- combs
def _Lam(n):
    for p in range(2, int(math.isqrt(n)) + 1):
        if n % p == 0:
            m = n
            while m % p == 0: m //= p
            return p if m == 1 else 0
    return n  # n prime

def lambda_comb(T):
    """True comb: all prime powers n with log n < 2T; atoms (log n, v_n = 2 Lambda(n)/sqrt n) as mpf."""
    out = []
    n = 2
    while mp.log(n) < 2 * mp.mpf(T):
        p = _Lam(n)
        if p: out.append((mp.log(n), 2 * mp.log(p) / mp.sqrt(n)))
        n += 1
    return out

# ---------------------------------------------------------------- quadrature
_GL = {}
def gl_nodes(n):
    key = (n, mp.mp.prec)
    if key in _GL: return _GL[key]
    xs, ws = [], []
    for i in range(1, n + 1):
        x = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (n + mp.mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp; x -= dx
            if abs(dx) < mp.mpf(2) ** (-mp.mp.prec + 4): break
        p0, p1 = mp.mpf(1), x
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
        dp = n * (x * p1 - p0) / (x * x - 1)
        xs.append(x); ws.append(2 / ((1 - x * x) * dp * dp))
    _GL[key] = (xs, ws); return xs, ws

def Kfun(u): return 1 / (2 * mp.sinh(u / 2)) + 1 / (2 * mp.cosh(u / 2))
def Ktail(x): return -mp.log(mp.tanh(x / 4)) + mp.pi - 2 * mp.atan(mp.exp(x / 2))

def _moments(T, N, panels, nodes):
    L = 2 * mp.mpf(T); xs, ws = gl_nodes(nodes)
    al = [k * mp.pi / L for k in range(1, N + 1)]
    S = [mp.mpf(0)] * N; D1 = [mp.mpf(0)] * N; D2 = [mp.mpf(0)] * N
    h = L / panels
    for p in range(panels):
        a = p * h
        for x, w in zip(xs, ws):
            u = a + h * (x + 1) / 2; wk = w * h / 2 * Kfun(u)
            c1, s1 = mp.cos(al[0] * u), mp.sin(al[0] * u)
            c, s = c1, s1
            for k in range(N):
                if k:  # rotation recurrence (guard digits absorb drift)
                    c, s = c * c1 - s * s1, s * c1 + c * s1
                S[k] += wk * s
                D1[k] += wk * (2 * mp.sin(al[k] * u / 2) ** 2 if k < 3 else 1 - c)
                D2[k] += wk * u * c
    return S, D1, D2

def _c_sym(j, k, u, L, al):
    """symmetrised cross-correlation of e_j, e_k (1-based) at lag 0 <= u <= L."""
    if u >= L: return mp.mpf(0)
    aj, ak = al[j - 1], al[k - 1]
    if j == k:
        return ((L - u) * mp.cos(ak * u) + mp.sin(ak * u) / ak) / L
    if (j + k) % 2: return mp.mpf(0)
    return 2 / L * (aj * mp.sin(ak * u) - ak * mp.sin(aj * u)) / (aj * aj - ak * ak)

# ---------------------------------------------------------------- builders
def build(T, N, dps=40, comb=None, panels=None, nodes=30, errcheck=True, cache=True, verbose=True):
    """Return dict with Arch, Pi (mp.matrix NxN), A, B (mp.matrix Nx1), err_arch (estimated
    max abs entry error of Arch), timing.  comb: list of (x, v); default lambda_comb(T)."""
    tag = None
    with mp.workdps(dps + 20):
        T = mp.mpf(T)
        if comb is None: comb = lambda_comb(T); cname = 'Lambda'
        else: cname = hashlib.md5(repr([(mp.nstr(x, 30), mp.nstr(v, 30)) for x, v in comb]).encode()).hexdigest()[:10]
        tag = f"T{mp.nstr(T, 17)}_N{N}_d{dps}_{cname}.pkl"
        fn = os.path.join(CACHE, tag)
        if cache and os.path.exists(fn):
            D = pickle.load(open(fn, 'rb'))
            return _from_strings(D, dps)
        t0 = time.time()
        L = 2 * T; al = [k * mp.pi / L for k in range(1, N + 1)]
        if panels is None: panels = N // 2 + 8
        S, D1, D2 = _moments(T, N, panels, nodes)
        err = None
        if errcheck:
            S2, D12, D22 = _moments(T, N, (3 * panels) // 2, nodes + 8)
            err = max(max(abs(a - b) for a, b in zip(X, Y)) for X, Y in ((S, S2), (D1, D12), (D2, D22)))
            err = err * (1 + 2 * N)  # crude propagation through the entry formulas
        C0 = mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi); tail = Ktail(L)
        Ar = mp.matrix(N, N); Pi = mp.matrix(N, N)
        for j in range(1, N + 1):
            aj = al[j - 1]
            Ar[j - 1, j - 1] = C0 + tail + D1[j - 1] + D2[j - 1] / L - S[j - 1] / (aj * L)
            for k in range(j + 1, N + 1):
                if (j + k) % 2: continue
                ak = al[k - 1]
                v = -2 / L * (aj * S[k - 1] - ak * S[j - 1]) / (aj * aj - ak * ak)
                Ar[j - 1, k - 1] = Ar[k - 1, j - 1] = v
        for j in range(1, N + 1):
            for k in range(j, N + 1):
                v = mp.fsum(w * _c_sym(j, k, x, L, al) for x, w in comb)
                Pi[j - 1, k - 1] = Pi[k - 1, j - 1] = v
        A = mp.matrix(N, 1); B = mp.matrix(N, 1); sT = 1 / mp.sqrt(T)
        for k in range(1, N + 1):
            a = al[k - 1]; sg = (-1) ** k
            A[k - 1] = sT * mp.exp(-T / 2) * a * (1 - sg * mp.exp(T)) / (mp.mpf(1) / 4 + a * a)
            B[k - 1] = sT * mp.exp(T / 2) * a * (1 - sg * mp.exp(-T)) / (mp.mpf(1) / 4 + a * a)
        D = dict(T=T, N=N, dps=dps, Arch=Ar, Pi=Pi, A=A, B=B, err_arch=err, comb=comb,
                 time=time.time() - t0, panels=panels, nodes=nodes)
        if verbose: print(f"[build] T={mp.nstr(T,8)} N={N} dps={dps}: {D['time']:.1f}s, est. Arch error {mp.nstr(err,3) if err is not None else '-'}")
        if cache:
            os.makedirs(CACHE, exist_ok=True)
            pickle.dump(_to_strings(D), open(fn, 'wb'))
        return _from_strings(_to_strings(D), dps)

def _to_strings(D):
    s = lambda x: mp.nstr(x, mp.mp.dps, strip_zeros=False)
    M = lambda X: [[s(X[i, j]) for j in range(X.cols)] for i in range(X.rows)]
    out = {k: v for k, v in D.items() if k not in ('Arch', 'Pi', 'A', 'B', 'comb', 'T', 'err_arch')}
    out.update(T=s(D['T']), Arch=M(D['Arch']), Pi=M(D['Pi']), A=M(D['A']), B=M(D['B']),
               comb=[(s(x), s(v)) for x, v in D['comb']], err_arch=s(D['err_arch']) if D['err_arch'] is not None else None)
    return out

def _from_strings(D, dps):
    with mp.workdps(dps + 20):
        f = mp.mpf
        out = dict(D)
        for k in ('Arch', 'Pi', 'A', 'B'): out[k] = mp.matrix([[f(x) for x in r] for r in D[k]])
        out['T'] = f(D['T']); out['comb'] = [(f(x), f(v)) for x, v in D['comb']]
        out['err_arch'] = f(D['err_arch']) if D['err_arch'] is not None else None
    return out

# ---------------------------------------------------------------- P_T and sectors
def sector_basis(D, par):
    """Orthonormal basis (N x m) of P_T intersected with the parity sector ('ev' or 'odd')."""
    N = D['N']; ks = [k for k in range(1, N + 1) if (k % 2 == 1) == (par == 'ev')]
    r = [D['A'][k - 1] + (1 if par == 'ev' else -1) * D['B'][k - 1] for k in ks]
    nr = mp.sqrt(mp.fsum(x * x for x in r)); r = [x / nr for x in r]
    w = list(r); w[0] -= 1; nw = mp.sqrt(mp.fsum(x * x for x in w))
    m = len(ks); Q = mp.matrix(N, m - 1)
    for c in range(1, m):     # column c of Householder H = I - 2 w w^T / |w|^2
        for i in range(m):
            Q[ks[i] - 1, c - 1] = (1 if i == c else 0) - 2 * w[i] * w[c] / nw ** 2
    return Q

def projector(D):
    """Orthogonal projector (N x N) onto P_T in the Galerkin space."""
    with mp.workdps(D['dps'] + 20):
        Q = sector_basis(D, 'ev'); R = sector_basis(D, 'odd')
        return Q * Q.T + R * R.T

def _restrict(D, par, mu=1):
    Q = sector_basis(D, par); M = D['Arch'] - mu * D['Pi']
    return Q, Q.T * M * Q

def bottom_eigs(D, par, k=5, mu=1):
    """Bottom k eigenpairs of (Arch - mu*Pi) on P_T, sector par.  Returns (eigs, vectors in e_k coords)."""
    with mp.workdps(D['dps'] + 20):
        Q, M = _restrict(D, par, mu)
        E, V = mp.eigsy(M)
        idx = sorted(range(len(E)), key=lambda i: E[i])[:k]
        return [E[i] for i in idx], [Q * V[:, i] for i in idx], [E[i] for i in sorted(range(len(E)), key=lambda i: E[i])]

def lambda_A(D):
    """lambda_A(T) Galerkin value (an upper bound for the true infimum, up to Arch error) + parity."""
    res = {}
    for par in ('ev', 'odd'):
        e, v, allE = bottom_eigs(D, par, k=1); res[par] = (e[0], v[0], allE)
    par = min(res, key=lambda p: res[p][0])
    return res[par][0], par, res

def _np(M): return np.array([[float(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])

def theta(D, tol=None):
    with mp.workdps(D['dps'] + 20): return _theta(D, tol)

def _theta(D, tol=None):
    """Theta_T = max_mu lambda_min(Arch - mu Pi on P_T) and maximiser c*.  Concave in mu:
    double-precision golden bracket, then golden section in multiprecision."""
    QE = sector_basis(D, 'ev'); QO = sector_basis(D, 'odd')
    blocks = [(QE.T * D['Arch'] * QE, QE.T * D['Pi'] * QE), (QO.T * D['Arch'] * QO, QO.T * D['Pi'] * QO)]
    nb = [(_np(a), _np(p)) for a, p in blocks]
    fd = lambda mu: min(np.linalg.eigvalsh(a - mu * p)[0] for a, p in nb)
    g = np.linspace(-5, 5, 401); i = int(np.argmax([fd(x) for x in g]))
    lo, hi = mp.mpf(g[max(i - 1, 0)]), mp.mpf(g[min(i + 1, 400)])
    def fm(mu): return min(min(mp.eigsy(a - mu * p, eigvals_only=True)) for a, p in blocks)
    # the maximum is typically a kink (two crossing branches): the value error is about
    # slope * tol, so tol must be far below the target resolution of Theta.
    tol = tol or mp.mpf(10) ** (-(D['dps'] * 3) // 4)
    gr = (mp.sqrt(5) - 1) / 2; x1 = hi - gr * (hi - lo); x2 = lo + gr * (hi - lo); f1, f2 = fm(x1), fm(x2)
    while hi - lo > tol:
        if f1 > f2: hi, x2, f2 = x2, x1, f1; x1 = hi - gr * (hi - lo); f1 = fm(x1)
        else: lo, x1, f1 = x1, x2, f2; x2 = lo + gr * (hi - lo); f2 = fm(x2)
    c = (lo + hi) / 2; fc = fm(c)
    f1m = fm(mp.mpf(1))          # the true comb, mu = 1, is always checked
    return (fc, c) if fc >= f1m else (f1m, mp.mpf(1))

def principal_angles(U, V):
    """Principal angles (radians, ascending) between column spans of mp matrices U, V
    (computed at the current mp precision; call inside mp.workdps)."""
    qu = mp.qr(U)[0][:, :U.cols]; qv = mp.qr(V)[0][:, :V.cols]
    s = mp.svd_r(qu.T * qv, compute_uv=False)
    return sorted(mp.acos(min(mp.mpf(1), x)) for x in s)

def cluster(eigs, thr): return sum(1 for e in eigs if e < thr)

def margin_bound(T): return 4e9 * T * math.exp(-15.449 * T)
