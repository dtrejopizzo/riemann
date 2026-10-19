"""R162_303 / C3: certified lower bound for the primitive truncated Weil form at T = (1/2) log 5.

Ball arithmetic (Arb via python-flint, vendored in phase-118).  Every number that enters the
certificate is an arb ball; every truncation is bounded in closed form.

Form:  a_T(F) = (1/2pi) int s(tau) |F^(tau)|^2 dtau,  s = m - sum_{n in N_T} v_n cos(tau log n),
       m(tau) = Re psi(1/4 + i tau/2) - log pi,  v_n = 2 Lambda(n)/sqrt n,  N_T = {2,3,4}.
Minorant (frequency truncation, no chords):  s_under = s on |tau| <= tauN,  s_under = s_inf beyond,
       s_inf <= m(tauN) - sum v_n  (m increasing, Paper 47 lem:mbounds(i)), hence s_under <= s.
       Write s_under = s_inf - g,  g = (s_inf - s) 1_{|tau|<tauN}  (indefinite, bounded).
Then  a_T - mu >= b_mu := (s_inf - mu) I - G,  G = Q_T g(D) Q_T.
Legendre basis e_l = sqrt((2l+1)/2T) P_l(t/T);  for l-i even
   G_il = (2T/pi) sqrt((2i+1)(2l+1)) (-1)^{(l-i)/2} int_0^tauN g(tau) j_i(tau T) j_l(tau T) dtau.
The integral is Gauss-Legendre on panels of length h with the analytic (Bernstein-ellipse) error
bound |I - I_N| <= L (64/15) M rho^{-2N} / (rho^2 - 1)  (Trefethen 2008, Thm 4.5), M = sup of the
integrand on the ellipse, bounded by  |j_n(z)| <= exp|Im z|  and an Arb enclosure of psi on a box.
Schur/Haynsworth step (Paper 47 prop:haynsworth, adapted to indefinite G, see memo R162_303 §3).
"""
import sys, time, json
sys.path.insert(0, '/home/trabajo/Documentos/research/riemann/03-research/'
                   'phase-118-the-exact-threshold-inequality/vendor/rowd-flint')
from flint import arb, acb, arb_mat, ctx

PREC = int(sys.argv[5]) if len(sys.argv) > 5 else 320
ctx.prec = PREC


def ball(mid, rad):
    return arb(mid, rad)


def run(T, primes, tauN, K, K2, N, h, rho, mus, par, tag, out=None):
    t0 = time.time()
    PI = arb.pi()
    LOGPI = PI.log()
    V = {}
    for n in primes:                     # n -> (v_n, log n)
        # Lambda(n): n is a prime power p^k
        p = min(q for q in range(2, n + 1) if n % q == 0)
        V[n] = (2 * arb(p).log() / arb(n).sqrt(), arb(n).log())
    SV = sum((v for v, _ in V.values()), arb(0))

    def psi_abs(w):
        # |psi(w)| on a box with Re w > 0, via psi(w) = psi(w+8) - sum_{k<8} 1/(w+k)
        # for u = w+8 (Re u >= 8): psi(u) = log u - 1/(2u) - int_0^inf k(t) e^{-ut} dt with
        # |k(t)| = |1/(e^t-1) - 1/t + 1/2| <= t/12, so
        # |psi(u)| <= log|u| + pi/2 + 1/(2 Re u) + 1/(12 (Re u)^2).
        u = w + 8
        rlo = arb(u.real.lower()); rhi = arb(u.real.upper())
        ihi = arb(abs(u.imag).upper())
        assert rlo > 1
        tot = ((rhi * rhi + ihi * ihi).sqrt()).log() + arb.pi() / 2 + 1 / (2 * rlo) + 1 / (12 * rlo * rlo)
        for k in range(8):
            relo = arb((w.real + k).lower())      # |w+k| >= Re(w+k) >= relo > 0
            assert relo > 0
            tot += 1 / relo
        return tot

    def m_of(tau):                       # real tau (arb)
        z = acb(arb(1) / 4, tau / 2)
        return z.digamma().real - LOGPI

    mN = m_of(arb(tauN))
    s_inf_ball = mN - SV
    # choose s_inf exactly (a dyadic) below the certified lower end
    s_inf = arb(s_inf_ball.lower()) - arb(2) ** (-PREC // 2)
    assert s_inf < s_inf_ball
    C0 = m_of(arb(0))
    # omega_+ >= sup (s_inf - s)_+ ,  omega_- >= sup (s - s_inf)_+  on [0,tauN]
    om_p = (s_inf - C0 + SV).upper()
    om_m = (mN + SV - s_inf).upper()
    om_p, om_m = arb(om_p), arb(om_m)

    rows = list(range(par, K2, 2))           # parity rows l < K2
    nE = len([l for l in rows if l < K])
    # Gauss-Legendre nodes/weights on [-1,1], rigorous
    GL = [arb.legendre_p_root(N, k, weight=True) for k in range(N)]
    rho_a = arb(rho)
    L = arb(h) / 2
    eta = L * (rho_a - 1 / rho_a) / 2        # max |Im| on the ellipse
    Rmaj = L * (rho_a + 1 / rho_a) / 2       # ellipse inside disk of this radius
    assert Rmaj < arb(1) / 2
    npan = int(round(tauN / h))
    assert abs(npan * h - tauN) < 1e-12
    Gacc = arb_mat(len(rows), len(rows))
    qerr = arb(0)                            # sum over panels of the error bound on int g j_i j_l
    chunk = 16
    jb = (2 * arb(T) * eta).exp()           # |j_i j_l| <= exp(2 T eta) on the ellipse
    for p0 in range(0, npan, chunk):
        cols = []
        for p in range(p0, min(npan, p0 + chunk)):
            c0 = arb(h) * p + L
            # error bound on this panel
            box = acb(arb(1) / 4 + arb(0, Rmaj.upper() / 2 + 1e-30), c0 / 2 + arb(0, Rmaj.upper() / 2 + 1e-30))
            box2 = acb(arb(1) / 4 + arb(0, Rmaj.upper() / 2 + 1e-30), -c0 / 2 + arb(0, Rmaj.upper() / 2 + 1e-30))
            mabs = (psi_abs(box) + psi_abs(box2)) / 2 + LOGPI
            cabs = sum(((v * (lg * eta).cosh()) for v, lg in V.values()), arb(0))
            M = (abs(s_inf) + mabs + cabs) * jb
            e = L * arb(64) / 15 * M * rho_a ** (-2 * N) / (rho_a ** 2 - 1)
            if not e.is_finite(): print("NaN panel", p, mabs, cabs, M, e)
            qerr += arb(e.upper())
            for (x, w) in GL:
                tau = c0 + L * x
                s = m_of(tau) - sum((v * (tau * lg).cos() for v, lg in V.values()), arb(0))
                g = s_inf - s
                cols.append((tau, L * w * g))
        J = arb_mat(len(rows), len(cols))
        Jw = arb_mat(len(rows), len(cols))
        for c, (tau, wg) in enumerate(cols):
            x = tau * T
            for r, l in enumerate(rows):
                jl = (PI / (2 * x)).sqrt() * x.bessel_j(arb(l) + arb(1) / 2)
                assert jl.rad() < arb(10) ** (-60), ('wide Bessel ball', l, x)
                J[r, c] = jl
                Jw[r, c] = jl * wg
        Gacc += Jw * J.transpose()
        print(f'  panels {p0}-{p0+chunk} done {time.time()-t0:.0f}s', flush=True)
    # assemble G_il
    nR = len(rows)
    G = [[None] * nR for _ in range(nR)]
    for a, i in enumerate(rows):
        for b, l in enumerate(rows):
            sg = 1 if ((l - i) // 2) % 2 == 0 else -1
            fac = 2 * arb(T) / PI * (arb((2 * i + 1) * (2 * l + 1))).sqrt() * sg
            G[a][b] = fac * (Gacc[a, b] + arb(0, qerr.upper()))
    # chi_l = <e_l, chi_par> = sqrt((2l+1)/2T) 2T i_l(T/2),  i_l(x) = sqrt(pi/2x) I_{l+1/2}(x)
    xh = arb(T) / 2
    chi = [((2 * l + 1) / (2 * arb(T))).sqrt() * 2 * arb(T) * (PI / (2 * xh)).sqrt()
           * xh.bessel_i(arb(l) + arb(1) / 2) for l in rows]
    chinorm2 = arb(T).sinh() + (arb(T) if par == 0 else -arb(T))
    # Lambda*_k(c) = (2/pi) sum_{j>=k} c^{2j+1}/((2j+1)!!)^2  (cor:P1), geometric tail
    cst = arb(T) * tauN

    def Lam_star(k):
        # term_j = c^{2j+1}/((2j+1)!!)^2
        df = arb(1)
        for q in range(1, 2 * k + 2, 2):
            df *= q
        term = cst ** (2 * k + 1) / df ** 2
        tot = arb(0)
        j = k
        while True:
            tot += term
            ratio = cst ** 2 / arb((2 * j + 3) ** 2)
            term = term * ratio
            j += 1
            if ratio < arb(1) / 2 and term < tot * arb(2) ** (-PREC):
                break
        # remaining tail <= term / (1 - ratio) <= 2 term (ratio decreasing in j)
        tot += arb(0, (2 * term).upper())
        return 2 / PI * tot
    LamK = Lam_star(K)
    LamK2 = Lam_star(K2)
    results = []
    for mu in mus:
        mu = arb(mu)
        qY = s_inf - mu - om_p * LamK
        assert qY > 0, 'q_Y not positive'
        beta = (om_p + om_m) * LamK2.sqrt()
        # ||P_{>=K2} chi||^2 = ||chi||^2 - sum_{l<K2, par} chi_l^2
        PK2chi2 = chinorm2 - sum((c * c for c in chi), arb(0))
        PK2chi_up = arb(max(PK2chi2.upper(), 0)).sqrt()
        PYchi2 = chinorm2 - sum((chi[a] * chi[a] for a in range(nE)), arb(0))
        E = range(nE)
        Y1 = range(nE, nR)
        # R matrix on E + xi
        d = nE
        R = [[None] * (d + 1) for _ in range(d + 1)]
        for a in E:
            for b in range(a, d):
                gram = sum((G[a][c] * G[b][c] for c in Y1), arb(0)) + arb(0, (beta * beta).upper())
                val = -G[a][b] - gram / qY
                if a == b:
                    val += s_inf - mu
                R[a][b] = R[b][a] = val
            cross = sum((G[a][c] * chi[c] for c in Y1), arb(0)) + arb(0, (beta * PK2chi_up).upper())
            R[a][d] = R[d][a] = chi[a] + cross / qY
        # R_xixi = -||P_Y chi||^2/q_Y <= 0.  Replacing it by the more negative -delta' (delta' >= its
        # certified modulus) lowers R, so n_-(R) <= n_-(R') and it suffices to certify R'.
        dup = arb((PYchi2 / qY).upper())
        R[d][d] = -dup
        assert R[d][d] < 0
        # Inertia of R.  Exact congruence by P = diag(H,1), H a floating-point Householder matrix
        # (entries exact binary64 numbers) sending the midpoint of r = R_{X,xi} to a multiple of e_0.
        # H is invertible because ||H^T H - I||_inf < 1 (checked in balls).  Order the coordinates
        # (t = H-coordinate 0, xi | y = H-coordinates 1..d-1).  The 2x2 block B on (t,xi) has
        # det B < 0 (certified), so inertia(B) = (1,1), and by Haynsworth
        # inertia(R) = (1,1) + inertia(S),  S = R'_yy - R'_{y,(t,xi)} B^{-1} R'_{(t,xi),y}.
        # If S is certified positive definite (interval Cholesky), then n_-(R) = 1.
        import numpy as np
        rmid = np.array([float(R[a][d].mid()) for a in range(d)])
        v = rmid.copy(); v[0] += np.sign(rmid[0]) * np.linalg.norm(rmid)
        Hf = np.eye(d) - 2.0 * np.outer(v, v) / np.dot(v, v)
        H = arb_mat(d, d, [arb(float(Hf[i, j])) for i in range(d) for j in range(d)])
        HtH = H.transpose() * H
        offmax = max(sum(abs(HtH[i, j] - (1 if i == j else 0)) for j in range(d)).upper() for i in range(d))
        assert arb(offmax) < 1, 'H not certified invertible'
        Rxx = arb_mat(d, d, [R[a][b] for a in range(d) for b in range(d)])
        rx = arb_mat(d, 1, [R[a][d] for a in range(d)])
        Rp = H.transpose() * Rxx * H
        rp = H.transpose() * rx
        Btt, Btx, Bxx = Rp[0, 0], rp[0, 0], R[d][d]
        detB = Btt * Bxx - Btx * Btx
        assert detB < 0, 'det B not certified negative'
        # B^{-1} = (1/det) [[Bxx, -Btx], [-Btx, Btt]]
        i_tt, i_tx, i_xx = Bxx / detB, -Btx / detB, Btt / detB
        n = d - 1
        A = [[None] * n for _ in range(n)]
        for a in range(n):
            ua, wa = Rp[a + 1, 0], rp[a + 1, 0]
            for b in range(a, n):
                ub, wb = Rp[b + 1, 0], rp[b + 1, 0]
                corr = ua * ub * i_tt + (ua * wb + wa * ub) * i_tx + wa * wb * i_xx
                A[a][b] = A[b][a] = Rp[a + 1, b + 1] - corr
        if mu == 0:   # diagnostic dump (not part of the certificate): midpoint of S at mu = 0
            json.dump([[A[a][b].mid().str(40, radius=False) for b in range(n)] for a in range(n)],
                      open(f'S_mid_{tag}.json', 'w'))
        piv = []
        ok = True
        for k in range(n):
            pk = A[k][k]
            piv.append(pk)
            if not pk > 0:
                ok = False
                break
            for i in range(k + 1, n):
                f = A[i][k] / pk
                for j in range(k + 1, i + 1):
                    A[i][j] = A[i][j] - f * A[j][k]
                    A[j][i] = A[i][j]
        C = None
        minpiv = min(piv, key=lambda x: float(x.mid()))
        res = dict(tag=tag, T=str(T), primes=primes, tauN=tauN, K=K, K2=K2, N=N, h=h, rho=rho,
                   prec=PREC, par=par, mu=str(mu), dimE=d,
                   s_inf=s_inf.str(20), m_tauN=mN.str(20), omega_plus=om_p.str(10),
                   omega_minus=om_m.str(10), quad_err_per_entry_raw=qerr.str(5),
                   LamStar_K=LamK.str(5), LamStar_K2=LamK2.str(5), qY=qY.str(15),
                   beta=beta.str(5), R_xixi=R[d][d].str(10),
                   max_rad_R=max(float(R[a][b].rad()) for a in range(d + 1) for b in range(d + 1)),
                   cholesky_ok=ok, n_pivots=len(piv), min_pivot=minpiv.str(10),
                   last_pivots=[p.str(8) for p in piv[-3:]], seconds=time.time() - t0)
        print(json.dumps(res, indent=1))
        if False:
            json.dump(res, open(out, 'w'), indent=1)
        results.append(res)
    if out:
        json.dump(results, open(out, "w"), indent=1)
    return results


if __name__ == '__main__':
    import math
    which = sys.argv[1]           # 'log5' or 'log3test'
    par = int(sys.argv[2])
    mus = sys.argv[3].split(',')
    tauN = float(sys.argv[4])
    K = int(sys.argv[6]) if len(sys.argv) > 6 else None
    K2 = int(sys.argv[7]) if len(sys.argv) > 7 else None
    N = int(sys.argv[8]) if len(sys.argv) > 8 else 46
    if which == 'log5':
        T = arb(5).log() / 2
        primes = [2, 3, 4]
    else:
        T = arb(3).log() / 2
        primes = [2]
    run(T, primes, tauN, K, K2, N, 0.5, 3.2, mus, par, f'{which}_par{par}_tauN{tauN}',
        out=f'c3_{which}_par{par}_tauN{int(tauN)}_K{K}_N{N}.json')
