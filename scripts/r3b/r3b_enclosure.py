"""Phase 155 round 3B: rigorous interval enclosure of a beta-uniform NEGATIVE
test-kernel ceiling at the TWO-PRIME windows T = 0.68 and T = log 2.

Same ingredients as scripts/r2_a_enclosure.py (R155_004 section 2.3):
  C0 = psi(1/4) - log pi = -gamma - pi/2 - 3 log 2 - log pi   (Gauss digamma),
  m(tau) = C0 + sum_{k<K} t_k + R,  t_k = tau^2/(a_k(tau^2+4a_k^2)), a_k = k+1/4,
  R = sum_{k>=K} t_k in [L-E, L], L = (1/2)log(1+tau^2/(4A^2)), A = K-1/4,
  E = (1/24)|t'(A)| = (1/24) tau^2(tau^2+12A^2)/(tau^2 A + 4A^3)^2     (Lemma 2.2),
  sigma_T = m - v_2 cos(tau log 2) - v_3 cos(tau log 3)   (contact set {2,3}),
  ghat_0, ghat_1 in closed form,  phi = |sum_k q_k e^{i k d tau}|^2 >= 0,
  int_W phi = P ||q||^2 exactly.

The ONE change from r2_a_enclosure.py is the quadrature.  Composite Simpson with the
crude 4th-derivative bound would need ~1e5 nodes here (|a| ~ 1e-5 instead of 1e-3 and
P = 110.8 instead of 45.75).  We use instead composite GAUSS-LEGENDRE of order p on
N panels of width H = P/N, with the classical remainder per panel

    |E_panel| <= H^(2p+1) (p!)^4 / ( (2p+1) ((2p)!)^3 ) * sup |f^(2p)| ,

and sup|f^(2p)| from the same Leibniz/Bernstein bounds as R155_004 section 2.3(iii),
extended to order 2p:
    |m^(j)| <= 2^-j j! zeta(j+1,1/4) <= 2^-j j! (4^(j+1) + zeta(j+1))
    |(v_n cos(tau log n))^(j)| <= v_n (log n)^j
    |ghat_0^(j)| <= 2 cosh T (2T)^(j+1)/(j+1),  |ghat_1^(j)| <= 2 sinh T (2T)^(j+2)/(j+2)
    |phi^(j)| <= (d(M-1))^j sum_l |gamma_l| <= (d(M-1))^j (sum_k |q_k|)^2
and for j = 0, |m| <= max(|C0|, m(tau_max)) (m even, increasing in |tau|), the second
entry being itself enclosed by the interval m() above.

Gauss-Legendre nodes/weights are computed at mp.dps = 60 and widened by 1e-45 before
entering the interval arithmetic; the residual |P_p(x)| at each returned node is printed
(it is < 1e-55), so the widened interval provably contains the true node, and the
quadrature-sum enclosure is valid for the exact rule.

Usage: python3 r3b_enclosure.py <Tname> <M> [ntau] [p] [H]
       Tname in {0.68, log2}   (any float expression also accepted)
"""
import sys, json, time, math
sys.path.insert(0, '/home/trabajo/Documentos/research/riemann/03-research/phase-155-row-d-flat-kernel-criterion/scripts')
import numpy as np
from mpmath import iv, mp, mpf, legendre, findroot, zeta as mpzeta
from scipy.linalg import toeplitz
from scipy.optimize import minimize
import tk_common as tk

iv.dps = 30
mp.dps = 60

TNAMES = {'0.68': 0.68, 'log2': float(np.log(2.0))}
# a priori beta box, Theorem B constants recomputed for these T (r3b_beta_box.json)
BBOX = {'0.68': 1.90e4, 'log2': 1.71e4}


# ------------------------------------------------------------------ double precision stage
def find_pair(T, M, ntau, B, nfft=1 << 16, rsub=3, nfine=1 << 20, ncand=1):
    parts = tk.make_S_parts(T)[:3]
    P = np.pi * M / T
    grid = np.linspace(-2.2 * P, 0.2 * P, ntau)
    MT = [[toeplitz(np.conj(c), c) for c in tk.coeff_families(T, M, t0, nfft, parts)] for t0 in grid]
    f = lambda b: -min(np.linalg.eigvalsh(Ms[0] + b[0] * Ms[1] + b[1] * Ms[2])[0] for Ms in MT)
    best = None
    for st in ([2.0, 0.0], [2.0, -0.02]):
        r = minimize(f, st, method='Nelder-Mead',
                     options={'xatol': 1e-9, 'fatol': 1e-14, 'maxiter': 400})
        if best is None or -r.fun > best[0]:
            best = (-r.fun, r.x)
    ceil_val, beta = best
    vals = [np.linalg.eigvalsh(Ms[0] + beta[0] * Ms[1] + beta[1] * Ms[2])[0] for Ms in MT]
    order = list(np.argsort(vals))
    # scan candidate period placements in increasing order of lambda_min: for each,
    # minimise the *predicted bound* a + B(|b0|+|b1|) over the span of the rsub lowest
    # eigenvectors, and keep the best.  (Only the argmin tau0 is used when it already
    # gives b = 0; when the minimax has two active tau0 it does not, and another
    # placement usually does.  Any (tau0,q) is a valid certificate of the bound.)
    r = min(rsub, M)
    best_all = None
    for i in order[:min(ncand, len(order))]:
        t0 = float(grid[i])
        C0m, C1m, C2m = [toeplitz(np.conj(c), c)
                         for c in tk.coeff_families(T, M, t0, nfine, parts)]
        w, V = np.linalg.eigh(C0m + beta[0] * C1m + beta[1] * C2m)
        U = V[:, :r]
        A0 = U.conj().T @ C0m @ U; A1 = U.conj().T @ C1m @ U; A2 = U.conj().T @ C2m @ U

        def obj(x):
            z = x[:r] + 1j * x[r:]
            nn = np.vdot(z, z).real
            if nn < 1e-12:
                return 1e9
            return (np.vdot(z, A0 @ z).real + B * (abs(np.vdot(z, A1 @ z).real)
                    + abs(np.vdot(z, A2 @ z).real))) / nn
        bb = None
        for seed in range(10):
            x0 = np.zeros(2 * r); x0[0] = 1.0
            if seed:
                x0 = np.random.default_rng(seed).standard_normal(2 * r)
            rr = minimize(obj, x0, method='Nelder-Mead',
                          options={'maxiter': 6000, 'maxfev': 6000,
                                   'xatol': 1e-13, 'fatol': 1e-18})
            if bb is None or rr.fun < bb.fun:
                bb = rr
        if best_all is None or bb.fun < best_all[0]:
            best_all = (bb.fun, t0, U, bb)
    _, t0, U, bb = best_all
    z = bb.x[:r] + 1j * bb.x[r:]
    q = U @ (z / np.linalg.norm(z))
    q = q / np.exp(1j * np.angle(q[np.argmax(np.abs(q))]))
    q = q / np.linalg.norm(q)
    return t0, np.round(q.real, 15), np.round(q.imag, 15), beta, ceil_val


# ------------------------------------------------------------------ interval machinery
def ivf(x):
    return iv.mpf(repr(float(x)))


def make_env(T_expr, M, K=100):
    T = T_expr
    d = 2 * T / M
    P = 2 * iv.pi / d
    a2T = 2 * T
    C0 = -iv.euler - iv.pi / 2 - 3 * iv.log(iv.mpf(2)) - iv.log(iv.pi)
    log2 = iv.log(iv.mpf(2)); log3 = iv.log(iv.mpf(3))
    v2 = 2 * log2 / iv.sqrt(iv.mpf(2))
    v3 = 2 * log3 / iv.sqrt(iv.mpf(3))
    A = iv.mpf(K) - iv.mpf(1) / 4
    ak = [iv.mpf(k) + iv.mpf(1) / 4 for k in range(K)]
    ak4 = [4 * a * a for a in ak]
    ehalf = iv.exp(a2T / 2); emhalf = 1 / ehalf

    def m(t):
        t2 = t * t
        s = C0
        for a, a4 in zip(ak, ak4):
            s = s + t2 / (a * (t2 + a4))
        L = iv.log(1 + t2 / (4 * A * A)) / 2
        E = t2 * (t2 + 12 * A * A) / ((t2 * A + 4 * A ** 3) ** 2) / 24
        return s + iv.mpf([(L - E).a, L.b])

    def sigma(t):
        return m(t) - v2 * iv.cos(t * log2) - v3 * iv.cos(t * log3)

    def gs(t):
        c = iv.cos(t * a2T); s = iv.sin(t * a2T); t2 = t * t
        out = []
        for sg, E in ((iv.mpf(1) / 2, ehalf), (-iv.mpf(1) / 2, emhalf)):
            D = sg * sg + t2
            I = (E * (sg * c + t * s) - sg) / D
            num = a2T * E * (sg * c + t * s) + E * c - 1
            dI = num / D - 2 * sg * (E * (sg * c + t * s) - sg) / D ** 2
            out.append((I, dI))
        return out[0][0] + out[1][0], out[0][1] - out[1][1]

    return dict(T=T, d=d, P=P, m=m, sigma=sigma, gs=gs, C0=C0, v2=v2, v3=v3,
                log2=log2, log3=log3, a2T=a2T, K=K)


def phi_maker(env, qr, qi, M):
    d = env['d']
    QR = [ivf(x) for x in qr]; QI = [ivf(x) for x in qi]

    def phi(t):
        c1 = iv.cos(d * t); s1 = iv.sin(d * t)
        ck = iv.mpf(1); sk = iv.mpf(0)
        re = iv.mpf(0); im = iv.mpf(0)
        for k in range(M):
            re = re + QR[k] * ck - QI[k] * sk
            im = im + QR[k] * sk + QI[k] * ck
            ck, sk = ck * c1 - sk * s1, sk * c1 + ck * s1
        return re * re + im * im
    return phi


# ------------------------------------------------------------------ Gauss-Legendre
def gauss_legendre(p):
    """p-point Gauss-Legendre nodes/weights on [-1,1] at mp.dps = 60.
    Double-precision nodes (numpy) are Newton-refined against mp's Legendre P_p;
    returns also max |P_p(x_i)| (the residual) and |sum w_i - 2|."""
    x0, _ = np.polynomial.legendre.leggauss(p)
    xs, ws, res = [], [], 0.0
    for xi in x0:
        x = mpf(repr(float(xi)))
        for _ in range(60):
            f = legendre(p, x)
            dP = p * (x * legendre(p, x) - legendre(p - 1, x)) / (x * x - 1)
            dx = f / dP
            x = x - dx
            if abs(dx) < mpf('1e-55'):
                break
        dP = p * (x * legendre(p, x) - legendre(p - 1, x)) / (x * x - 1)
        xs.append(x); ws.append(2 / ((1 - x * x) * dP ** 2))
        res = max(res, abs(float(legendre(p, x))))
    wsum = float(abs(sum(ws) - 2))
    return xs, ws, max(res, wsum)


# ------------------------------------------------------------------ derivative bounds
def zeta_quarter_ub(j):
    return float(4 ** j) + float(mpzeta(j))


def deriv_bounds(T, M, qr, qi, n, m0):
    """returns (C_sigma, C_g0, C_g1) = upper bounds on sup |(X phi)^(n)|."""
    Sq = sum(abs(complex(a, b)) for a, b in zip(qr, qi))
    Gam = Sq * Sq
    dd = 2.0 * T / M
    Phi = [Gam * (dd * (M - 1)) ** j for j in range(n + 1)]
    mb = [m0] + [2.0 ** (-j) * math.factorial(j) * zeta_quarter_ub(j + 1) for j in range(1, n + 1)]
    v2 = 2 * np.log(2) / np.sqrt(2.0); v3 = 2 * np.log(3) / np.sqrt(3.0)
    l2 = np.log(2.0); l3 = np.log(3.0)
    sig = [mb[j] + v2 * l2 ** j + v3 * l3 ** j for j in range(n + 1)]
    a = 2 * T; chT = math.cosh(T); shT = math.sinh(T)
    g0 = [2 * chT * a ** (j + 1) / (j + 1) for j in range(n + 1)]
    g1 = [2 * shT * a ** (j + 2) / (j + 2) for j in range(n + 1)]
    C = lambda X: sum(math.comb(n, j) * X[n - j] * Phi[j] for j in range(n + 1))
    return C(sig), C(g0), C(g1), Gam


def gl_const(p):
    """(p!)^4 / ((2p+1) ((2p)!)^3), as a float (computed in mp to avoid overflow)."""
    return float(mp.factorial(p) ** 4 / ((2 * p + 1) * mp.factorial(2 * p) ** 3))


# ------------------------------------------------------------------ main
def run(tname, M, ntau=121, p=6, H=0.1, K=100, rsub=3, ncand=1):
    T = TNAMES.get(tname, None)
    if T is None:
        T = float(eval(tname))
    B = BBOX.get(tname, 1.9e4)
    t_all = time.time()
    t0f, qr, qi, beta, ceil_d = find_pair(T, M, ntau, B, rsub=rsub, ncand=ncand)
    t_dp = time.time() - t_all

    Tiv = iv.log(iv.mpf(2)) if tname == 'log2' else ivf(T)
    env = make_env(Tiv, M, K)
    phi = phi_maker(env, qr, qi, M)
    P = env['P']; lo = ivf(t0f)
    N = int(math.ceil(float(P.b) / H))
    Hiv = P / N
    tau_max = abs(t0f) + float(P.b)
    # |m| bound: m even, increasing in |tau|  =>  |m| <= max(|C0|, m(tau_max))
    m0 = max(abs(float(env['C0'].a)), abs(float(env['m'](ivf(tau_max)).b))) + 1e-9
    n = 2 * p
    Cs, Cg0, Cg1, Gam = deriv_bounds(T, M, qr, qi, n, m0)
    K_gl = gl_const(p)
    Hf = float(Hiv.b)
    err = lambda C: N * Hf ** (n + 1) * K_gl * C
    es, e0, e1 = err(Cs), err(Cg0), err(Cg1)

    xs, ws, res = gauss_legendre(p)
    XS = [iv.mpf([mp.nstr(x - mpf('1e-45'), 50), mp.nstr(x + mpf('1e-45'), 50)]) for x in xs]
    WS = [iv.mpf([mp.nstr(w - mpf('1e-45'), 50), mp.nstr(w + mpf('1e-45'), 50)]) for w in ws]

    t_q = time.time()
    Is = iv.mpf(0); I0 = iv.mpf(0); I1 = iv.mpf(0)
    half = Hiv / 2
    for jp in range(N):
        c = lo + (2 * jp + 1) * half
        for x, w in zip(XS, WS):
            t = c + half * x
            ph = phi(t)
            g0v, g1v = env['gs'](t)
            Is = Is + w * env['sigma'](t) * ph
            I0 = I0 + w * g0v * ph
            I1 = I1 + w * g1v * ph
    Is = Is * half; I0 = I0 * half; I1 = I1 * half
    t_quad = time.time() - t_q

    Is = Is + iv.mpf([-es, es]); I0 = I0 + iv.mpf([-e0, e0]); I1 = I1 + iv.mpf([-e1, e1])
    nrm2 = sum(ivf(x) * ivf(x) + ivf(y) * ivf(y) for x, y in zip(qr, qi))
    den = P * nrm2
    aI, b0I, b1I = Is / den, I0 / den, I1 / den
    bnd = aI + (abs(b0I) + abs(b1I)) * iv.mpf(repr(B))

    out = dict(T_name=tname, T=T, M=M, ntau=ntau, rsub=rsub, ncand=ncand, p=p, H=Hf, N_panels=N, K=K, B=B,
               tau0=t0f, q_re=list(map(float, qr)), q_im=list(map(float, qi)),
               beta_search=list(map(float, beta)), ceil_double=float(ceil_d),
               gl_residual=res, m0=m0, Gam=Gam,
               C_sigma=Cs, C_g0=Cg0, C_g1=Cg1, gl_const=K_gl,
               err_sigma=es, err_g0=e0, err_g1=e1,
               a=[float(aI.a), float(aI.b)], b0=[float(b0I.a), float(b0I.b)],
               b1=[float(b1I.a), float(b1I.b)],
               ceiling_upper_bound=float(bnd.b),
               sec_double=t_dp, sec_quad=t_quad, sec_total=time.time() - t_all)
    print(json.dumps(out, indent=1))
    return out


if __name__ == '__main__':
    tname = sys.argv[1]; M = int(sys.argv[2])
    ntau = int(sys.argv[3]) if len(sys.argv) > 3 else 121
    p = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    H = float(sys.argv[5]) if len(sys.argv) > 5 else 0.1
    rsub = int(sys.argv[6]) if len(sys.argv) > 6 else 3
    ncand = int(sys.argv[7]) if len(sys.argv) > 7 else 1
    r = run(tname, M, ntau, p, H, rsub=rsub, ncand=ncand)
    json.dump(r, open(f'r3b_enclosure_{tname}_M{M}.json', 'w'), indent=1)
