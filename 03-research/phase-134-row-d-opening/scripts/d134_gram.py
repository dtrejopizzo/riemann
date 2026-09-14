"""Phase 134, row D opening: the Gram matrix of the SMEARED UNIT-AVERAGED
Frobenius family under I_infinity, and its inertia on the primitive subspace.

Objects (all imported by number; nothing here is a proof):

  Paper 45 Lemma 5.1a    the radial trace with NO support hypothesis, c = 0:
                         T(Gamma_h) = sum_n Lambda(n) n^{-1/2}[h(log n)+h(-log n)]
                                      + (1/2pi) int hhat(-tau) What_infty(0,tau) dtau.
                         THIS is what defines the entries below, at every eps.
  Paper 44 Thm 8bis.1e   the INTERPRETATION of the entries as the Gram form of
                         Frob * Delta^rad -- valid only for eps < eps_0(A,S)
                         and 0 not in supp(h_m * h_n^dagger), i.e. eps = O(1/N).
                         NOT satisfied at any (N,eps) of the reported tables.
  Paper 44 (3bis.9)      W_fin = sum_{p,k} (log p) p^{-k/2} (delta_{+klogp}
                                            + delta_{-klogp}),
                         omega_inf = K(|t|) dt,  K(t)=e^{-t/2}/(1-e^{-2t}).
  Paper 43 (14.1)        I_A(F,F) = (1/2pi) int |F^(tau)|^2 (That(tau)+c),
                         c = 0 (Paper 45 Cor 9.6a).
  Paper 44 (8bis.9)      primitivity  <=>  lambda_-(Gamma_g)=lambda_+(Gamma_g)=0.

Convention.  h_n(t) = phi_eps(t - log n) with phi_eps(t) = eps^{-1} Lam(t/eps),
Lam the unit triangle; then h_m * h_n^dagger (t) = psi_eps(t - Delta_{mn}),
Delta_{mn} = log m - log n, psi_eps(t) = eps^{-1} B4(t/eps), B4 the cubic
B-spline, and  psi_eps^(tau) = sinc(eps tau/2)^4.

The FINITE half is evaluated in t-space (a finite sum: psi_eps is compactly
supported).  The ARCHIMEDEAN half is evaluated in tau-space against the
archimedean symbol -- which is Lemma 5.1a's second term, and is what makes the
m = n diagonal finite even though int K(|t|) psi_eps(t) dt diverges.  Its
asymptotics are  (c_phi/eps)(-log(1/eps) + C_phi),  c_phi = |phi_1|_{L2}^2:
Paper 44 Thm 8bis.2 carried WITH its ||phi||^2/eps factor.  (Paper 46
Remark 5.9(3): the normalization-free form -log(1/eps)+gamma+log 4pi applies to
the L2-NORMALIZED profile, not to the unit-mass profile used here.)

Models:
  zeta : w_n = Lambda(n)/sqrt(n),  omegahat(tau) = log pi - Re psi(1/4+i tau/2)
  xi_a : Xi_a(s) = xi(s+a) xi(s-a),
         w_n = Lambda(n)(n^a + n^{-a})/sqrt(n),
         omegahat_a(tau) = 2 log pi - Re psi(1/4 + a/2 + i tau/2)
                                    - Re psi(1/4 - a/2 + i tau/2).
  (a = 0 degenerates to twice the zeta data, as it must: Xi_0 = xi^2.)

Range of validity: the archimedean integrand oscillates on a scale 1/eps and
the adaptive quadrature reaches its subdivision limit below eps ~ 0.01.  Do
not report values at eps < 0.01 from this script; the small-eps regime is
described by Paper 46 Theorem 5.8, not by this quadrature.

NUMERICS ILLUSTRATE AND FALSIFY.  THEY PROVE NOTHING.
"""
import argparse
import math

import numpy as np
from scipy.special import digamma
from scipy.integrate import quad



# ------------------------------------------------------------------ arithmetic
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


# ------------------------------------------------------------------- profiles
def B4(x):
    """Cubic B-spline: autocorrelation of the unit triangle.  int B4 = 1."""
    x = np.abs(np.asarray(x, dtype=float))
    out = np.zeros_like(x)
    m1 = x <= 1.0
    m2 = (x > 1.0) & (x < 2.0)
    out[m1] = 2.0 / 3.0 - x[m1] ** 2 + x[m1] ** 3 / 2.0
    out[m2] = (2.0 - x[m2]) ** 3 / 6.0
    return out


def psi_eps(t, eps):
    return B4(np.asarray(t) / eps) / eps


def sinc4(x):
    x = np.asarray(x, dtype=float)
    s = np.where(np.abs(x) < 1e-12, 1.0 - x ** 2 / 6.0, np.sin(x) / np.where(x == 0, 1.0, x))
    return s ** 4


# --------------------------------------------------------------------- models
class Model:
    def __init__(self, name, weights_fn, omega_hat, tate_exponents):
        self.name = name
        self.weights_fn = weights_fn        # N -> array w[0..N]
        self.omega_hat = omega_hat          # tau -> archimedean symbol
        self.tate_exponents = tate_exponents


def model_zeta():
    def w(N):
        lam = np.array(von_mangoldt(N))
        n = np.arange(N + 1, dtype=float)
        out = np.zeros(N + 1)
        out[2:] = lam[2:] / np.sqrt(n[2:])
        return out

    def om(tau):
        return math.log(math.pi) - np.real(digamma(0.25 + 0.5j * np.asarray(tau)))

    return Model("zeta", w, om, [0.5, -0.5])


def model_xi_a(a):
    if not (0.0 <= a < 0.5):
        raise ValueError("need 0 <= a < 1/2")

    def w(N):
        lam = np.array(von_mangoldt(N))
        n = np.arange(N + 1, dtype=float)
        out = np.zeros(N + 1)
        out[2:] = lam[2:] * (n[2:] ** a + n[2:] ** (-a)) / np.sqrt(n[2:])
        return out

    def om(tau):
        tau = np.asarray(tau)
        return (2 * math.log(math.pi)
                - np.real(digamma(0.25 + a / 2 + 0.5j * tau))
                - np.real(digamma(0.25 - a / 2 + 0.5j * tau)))

    return Model("xi_a[a=%g]" % a, w, om,
                 [0.5 + a, 0.5 - a, -0.5 - a, -0.5 + a])


# ------------------------------------------------------------- the Gram matrix
def arch_entry(model, delta, eps, tau_max=None, npts=None):
    """(1/2pi) int omegahat(tau) sinc^4(eps tau/2) cos(tau delta) dtau.

    The archimedean half of (8bis.6) read through Paper 43 (14.1).  For
    delta != 0 and eps -> 0 this converges to K(|delta|); for delta = 0 it is
    the regularized self-pairing of Thm 8bis.2, ~ -log(1/eps) + gamma + log 4pi.
    """
    if tau_max is None:
        tau_max = 300.0 / eps
    f = lambda tau: model.omega_hat(tau) * sinc4(eps * tau / 2.0) * math.cos(tau * delta)
    val = 0.0
    # break the integration at the zeros of sinc and at the cosine scale
    step = max(2 * math.pi / eps, 1.0)
    lo = 0.0
    while lo < tau_max:
        hi = min(lo + step, tau_max)
        v, _ = quad(f, lo, hi, limit=400, epsabs=1e-11, epsrel=1e-10)
        val += v
        lo = hi
    return val / math.pi          # (1/2pi) * 2 * int_0^infty


def gram(model, N, eps, verbose=False):
    labels = list(range(2, N + 1))
    k = len(labels)
    logs = np.array([math.log(n) for n in labels])
    # finite half: atoms of W_fin against psi_eps
    Nat = int(math.exp(logs[-1] - logs[0] + 2 * eps)) + 2
    w = model.weights_fn(max(Nat, 3))
    atoms = [(math.log(n), w[n]) for n in range(2, len(w)) if w[n] != 0.0]
    D = logs[:, None] - logs[None, :]
    G = np.zeros((k, k))
    for lg, wn in atoms:
        G += wn * (psi_eps(D - lg, eps) + psi_eps(D + lg, eps))
    # archimedean half: one quadrature per distinct |Delta|
    uniq = np.unique(np.round(np.abs(D), 12))
    tab = {u: arch_entry(model, u, eps) for u in uniq.tolist()}
    A = np.vectorize(lambda x: tab[round(abs(x), 12)])(D)
    G = G + A
    G = 0.5 * (G + G.T)
    if verbose:
        # reference: (c_phi/eps)(-log(1/eps) + C_phi), c_phi = 2/3 for the
        # triangle; C_phi fitted at 2.00 for the zeta model (Paper 46 Rem 5.9(3)).
        print("   diag[arch] = %+.6f   ((2/3eps)(-log(1/eps)+2.00) = %+.6f)"
              % (tab[0.0], (2.0 / 3.0 / eps) * (-math.log(1.0 / eps) + 2.00)))
    return G, labels


def primitive_compression(G, labels, model):
    """Compress to {c : sum_n c_n n^u = 0 for every Tate exponent u}."""
    n = np.array(labels, dtype=float)
    C = np.vstack([n ** u for u in model.tate_exponents])
    u_, s_, vt = np.linalg.svd(C)
    r = int(np.sum(s_ > 1e-12 * s_.max()))
    Z = vt[r:].T                       # orthonormal basis of the null space
    if Z.shape[1] == 0:
        return np.zeros((0, 0)), r
    Gp = Z.T @ G @ Z
    return 0.5 * (Gp + Gp.T), r


def inertia(M, tol=1e-10):
    if M.size == 0:
        return (0, 0, 0), float('nan'), float('nan')
    ev = np.linalg.eigvalsh(M)
    sc = max(abs(ev).max(), 1e-300)
    npos = int(np.sum(ev > tol * sc))
    nneg = int(np.sum(ev < -tol * sc))
    return (npos, len(ev) - npos - nneg, nneg), float(ev.min()), float(ev.max())


# ----------------------------------------------------------------- diagnostics
def K_zeta(t):
    return math.exp(-t / 2) / (1 - math.exp(-2 * t))


def check_kernel_limit(model):
    """Off-diagonal entries must approach W_fin({Delta}) + K_model(|Delta|)."""
    print("-- check: off-diagonal -> W_fin + K as eps -> 0  (model %s)" % model.name)
    for (m, n) in [(3, 2), (4, 2), (5, 3)]:
        d = math.log(m) - math.log(n)
        w = model.weights_fn(16)
        atom = 0.0
        for j in range(2, 16):
            if abs(math.log(j) - abs(d)) < 1e-12:
                atom = w[j]
        for eps in (0.05, 0.02, 0.01):
            a = arch_entry(model, d, eps)
            print("   (m,n)=(%d,%d) Delta=%.5f eps=%.3f  arch=%+.6f  atom=%+.6f"
                  % (m, n, d, eps, a, atom))
        print("   reference K(|Delta|) = %+.6f" % K_zeta(abs(d)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="zeta", choices=["zeta", "xi_a"])
    ap.add_argument("--a", type=float, default=0.35)
    ap.add_argument("--N", type=int, nargs="+", default=[10, 30, 60])
    ap.add_argument("--eps", type=float, nargs="+", default=[0.5, 0.2, 0.05])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    model = model_zeta() if args.model == "zeta" else model_xi_a(args.a)
    print("model = %s;  Tate exponents = %s" % (model.name, model.tate_exponents))
    if args.check:
        check_kernel_limit(model)
        print()

    print("%4s %7s | %5s %-16s | %-16s | %s"
          % ("N", "eps", "dimP", "inertia(+,0,-) G^prim", "lam_min/lam_max",
             "full G inertia"))
    for N in args.N:
        for eps in args.eps:
            G, labels = gram(model, N, eps)
            Gp, rank = primitive_compression(G, labels, model)
            inp, lmin, lmax = inertia(Gp)
            inf_, flmin, flmax = inertia(G)
            print("%4d %7.3f | %5d %-16s | %+8.3e/%+8.3e | %s"
                  % (N, eps, Gp.shape[0], str(inp), lmin, lmax, str(inf_)))
    print("\nNumerics illustrate and falsify; they prove nothing.")


if __name__ == "__main__":
    main()
