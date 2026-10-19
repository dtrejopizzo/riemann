"""A_M = Arch - Div - Near for a comb nu = sum_x w_x delta_x on a lattice of points x_1<...<x_M (default: log m, m<=M).
Entries: B(x_m-x_k) = Arch(x_m-x_k) - 1/2 sum_x w_x [c0(x-(x_m-x_k)) + c0(x+(x_m-x_k))].
Div = exact coincidences x = x_m-x_k (|.|<tol), Near = the rest with |x-(x_m-x_k)|<2T0.  (Paper 47 prop:AM(iii).)
For the Lambda comb on log N the x+(x_m-x_k) term never contributes (x>=log2>2T0)."""
import numpy as np
from scipy import sparse
from profile import Profile

def primes_upto(n):
    s = np.ones(n+1, bool); s[:2] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def lambda_comb(nmax, delete_below=None, amp2=0.0, perturb=None):
    """atoms (log n, v_n=2 Lambda(n)/sqrt n), n<=nmax. delete_below=P deletes primes <P (a_P).
    amp2: add c to v_2.  perturb=(n0, factor) multiplies v_{n0} by factor."""
    pos, w, ns = [], [], []
    for p in primes_upto(nmax):
        if delete_below is not None and p < delete_below: continue
        q = p
        while q <= nmax:
            pos.append(np.log(q)); w.append(2*np.log(p)/np.sqrt(q)); ns.append(q); q *= p
    pos, w, ns = np.array(pos), np.array(w), np.array(ns)
    if amp2:
        w[ns == 2] += amp2
    if perturb is not None:
        n0, fac = perturb
        w[ns == n0] *= fac
    o = np.argsort(pos)
    return pos[o], w[o], ns[o]

def poisson_comb(xmax, kappa=1.0, seed=0):
    """Poisson process on (log2, xmax) with intensity kappa e^u/u, weights 2x e^{-x/2} (Paper 47 thm:poisson)."""
    rng = np.random.default_rng(seed)
    u0, u1 = np.log(2.0), xmax
    # thinning from intensity bound kappa e^u / u0  -> uniform in e^u coordinates: use inverse of e^u
    # Lambda_bound(u) = kappa e^u/u0 ; sample y uniform in e^{u0}..e^{u1} with rate kappa/u0
    lam = kappa/u0
    nmean = lam*(np.exp(u1) - np.exp(u0))
    n = rng.poisson(nmean)
    y = rng.uniform(np.exp(u0), np.exp(u1), n)
    u = np.log(y)
    keep = rng.uniform(size=n) < (u0/u)
    x = np.sort(u[keep])
    return x, 2*x*np.exp(-x/2), None

def beurling_comb(nmax, jitter=0.02, seed=0, nq=None):
    """generalised primes q_j = p_j e^{eps_j}, eps_j uniform(-jitter,jitter); weights 2 log q q^{-a/2} on powers."""
    rng = np.random.default_rng(seed)
    ps = primes_upto(nmax)
    qs = ps*np.exp(rng.uniform(-jitter, jitter, len(ps)))
    pos, w = [], []
    for q in qs:
        qa = q
        while qa <= nmax:
            pos.append(np.log(qa)); w.append(2*np.log(q)/np.sqrt(qa)); qa *= q
    pos, w = np.array(pos), np.array(w); o = np.argsort(pos)
    return pos[o], w[o], qs

def beurling_integers(qs, M):
    """all products of generalised primes qs (with repetition) <= M, sorted (the lattice of the Beurling system)."""
    qs = np.sort(qs[qs <= M])
    out = [1.0]
    for q in qs:
        new = []
        for v in out:
            t = v*q
            while t <= M:
                new.append(t); t *= q
        out.extend(new)
    return np.sort(np.array(out))

class AM:
    def __init__(self, P: Profile, lattice, pos, w, tol=1e-9, extra_kernel=None):
        """lattice: sorted array of lattice points x_m; (pos,w): comb atoms. extra_kernel(d) adds a Toeplitz term (M1 model)."""
        self.P, self.x, self.pos, self.w = P, np.asarray(lattice, float), pos, w
        M = len(self.x); self.M = M
        T0 = P.T0
        D = self.x[:, None] - self.x[None, :]
        self.Arch = P.arch(D)
        rows, cols, vals, drows, dcols, dvals = [], [], [], [], [], []
        self.triples = []   # (atom index, k index, m index, d) for mass accounting
        for ai, (xa, wa) in enumerate(zip(pos, w)):
            if xa > self.x[-1] - self.x[0] + 2*T0: break
            lo = np.searchsorted(self.x, self.x + xa - 2*T0, 'right')
            hi = np.searchsorted(self.x, self.x + xa + 2*T0, 'left')
            cnt = hi - lo
            if cnt.sum() == 0: continue
            k = np.repeat(np.arange(M), cnt)
            m = np.concatenate([np.arange(l, h) for l, h in zip(lo, hi) if h > l])
            d = xa - (self.x[m] - self.x[k])
            ex = np.abs(d) < tol
            if ex.any():
                drows.append(m[ex]); dcols.append(k[ex]); dvals.append(np.full(ex.sum(), 0.5*wa))
            ne = ~ex
            if ne.any():
                rows.append(m[ne]); cols.append(k[ne]); vals.append(0.5*wa*P.c0(d[ne]))
                self.triples.append((ai, k[ne], m[ne], d[ne]))
        def tosym(r, c, v):
            if not r: return np.zeros((M, M))
            r, c, v = np.concatenate(r), np.concatenate(c), np.concatenate(v)
            S = sparse.coo_matrix((v, (r, c)), shape=(M, M)).toarray()
            return S + S.T
        self.Div = tosym(drows, dcols, dvals)
        self.Near = tosym(rows, cols, vals)
        self.A = self.Arch - self.Div - self.Near
        if extra_kernel is not None:
            self.Extra = extra_kernel(D)
            self.A = self.A + self.Extra
        self.Gram = P.c0(D)

    def eig(self, which='A'):
        X = getattr(self, which)
        return np.linalg.eigh(X)

    def summary(self):
        lam, V = np.linalg.eigh(self.A)
        v = V[:, 0]
        normA = np.abs(lam).max()
        return dict(M=self.M, lam_min=lam[0], lam_max=lam[-1], normA=normA,
                    floor=2.2e-16*normA*self.M, vec=v,
                    Arch_v=float(v @ self.Arch @ v), Div_v=float(v @ self.Div @ v), Near_v=float(v @ self.Near @ v),
                    Gram_v=float(v @ self.Gram @ v), n_neg=int((lam < -2.2e-16*normA*self.M).sum()), lam=lam)
