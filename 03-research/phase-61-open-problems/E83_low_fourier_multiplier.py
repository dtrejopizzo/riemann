"""
DECISIVE STEP toward the analytic proof of 2.3.F-Loc.

REFORMULATION: the ratios (k+1)^2 do NOT depend on the whole oscillation of the Doob
multiplier C_lambda, only on its LOW FOURIER MODES in the carrier coordinate theta. By
1st-order perturbation in the carrier frame (G = -d^2/dtheta^2 with C=c(1+eta)):
   delta(e_k)/e_k ~ <eta> + (1/2) eta_hat(2(k+1)),
so the ratio e_k/e_1 only sees eta_hat(2j), small j (the average <eta> cancels out).

=> 2.3.F-Loc' (what needs to be proved): eta_hat(2j) -> 0 (j=1,2,3) as lambda->inf, ON AVERAGE.
This is MUCH weaker than "eta->0 pointwise" (N3, which stays flat due to the high-frequency
arithmetic fluctuation). Here we measure the LOW modes, which is the only thing controlling
the ratios. If they decay even though the pointwise std does not -> 2.3.F-Loc proved in the
sense that matters.

We compare: pointwise std of eta (N3, expected flat) vs |eta_hat(2j)| j=1,2,3 (expected: decays?).
Falsifier DH (must NOT decay / must be large).
"""
import sys, numpy as np, mpmath as mp
from engine_cache import doob_spectrum, recon_grid, extract_C

NTH = 2000  # grid in theta


def get_eta_in_theta(lam, N, kind='zeta'):
    d = doob_spectrum(lam, N, kind, dps=40, nlow=3)
    V, order, idx, L, dim = d['V'], d['order'], d['idx'], d['L'], d['dim']

    def gm(k):
        c = np.array([float(V[i, order[k]]) for i in range(dim)])
        return recon_grid(c, idx, L)
    ys, u0 = gm(0)
    if u0[len(ys) // 2] < 0:
        u0 = -u0
    _, f1 = gm(1)
    a0 = np.max(np.abs(u0))
    w = u0 ** 2
    e1 = float(d['eps'][1] - d['eps'][0])
    v1 = np.where(np.abs(u0) > 1e-9 * a0, f1 / np.where(np.abs(u0) > 1e-12, u0, 1e-12), 0.0)
    C = extract_C(ys, w, v1, e1, None)

    # carrier coordinate theta(y) from u0 ~ sin(theta): theta = arccos via f1/u0 = 2 cos theta
    ct = np.full_like(u0, np.nan)
    safe = np.abs(u0) > 1e-9 * a0
    ct[safe] = np.clip(0.5 * f1[safe] / u0[safe], -1.0, 1.0)
    th = np.arccos(ct)  # in [0,pi]

    # bulk: where C is finite and u0 is not at a node
    inner = (np.abs(u0) > 0.30 * a0) & np.isfinite(C) & np.isfinite(th)
    thb = th[inner]; Cb = C[inner]
    # sort by theta and keep the monotone range
    srt = np.argsort(thb)
    thb, Cb = thb[srt], Cb[srt]
    # eta = C/mean - 1
    cmean = np.mean(Cb)
    eta = Cb / cmean - 1.0
    return thb, eta, L


def low_fourier(thb, eta, jmax=3):
    """coefficients eta_hat(2j) = (2/pi) int_0^pi eta(theta) cos(2 j theta) dtheta, via uniform interpolation."""
    # interpolate to a uniform grid on [thb.min, thb.max] rescaled to [0,pi]
    t0, t1 = thb.min(), thb.max()
    tu = np.linspace(t0, t1, NTH)
    eu = np.interp(tu, thb, eta)
    # rescale the bulk interval to [0,pi] (bulk Dirichlet)
    s = (tu - t0) / (t1 - t0) * np.pi
    out = []
    for j in range(1, jmax + 1):
        cj = np.trapz(eu * np.cos(2 * j * s), s) * (2.0 / np.pi)
        out.append(cj)
    std = np.std(eu)
    return out, std


def run(lams, kind='zeta'):
    print(f"\n{'='*72}\nkind={kind}: low Fourier modes of the multiplier vs pointwise std")
    print(f"{'lam':>5} {'L':>5} {'std(eta)':>9} | {'|c1|=hat(2)':>11} {'|c2|=hat(4)':>11} {'|c3|=hat(6)':>11}")
    rows = []
    for lam, N in lams:
        thb, eta, L = get_eta_in_theta(lam, N, kind)
        cj, std = low_fourier(thb, eta)
        rows.append((lam, L, std, cj))
        print(f"{lam:>5} {L:>5.2f} {std:>9.4f} | {abs(cj[0]):>11.4f} {abs(cj[1]):>11.4f} {abs(cj[2]):>11.4f}")
    if len(rows) >= 4 and kind == 'zeta':
        import math
        Ls = [r[1] for r in rows]
        def rate(vals):
            xs = [math.log(L) for L in Ls]; ys = [math.log(max(v, 1e-9)) for v in vals]
            n = len(xs); sx = sum(xs); sy = sum(ys); sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
            return -(n * sxy - sx * sy) / (n * sxx - sx * sx)
        print("-" * 72)
        print(f"  RATE std(eta) pointwise ~ L^-{rate([r[2] for r in rows]):.2f}  (N3: expected ~flat)")
        for j in range(3):
            p = rate([abs(r[3][j]) for r in rows])
            print(f"  RATE |hat(2*{j+1})|     ~ L^-{p:+.2f}  {'<<< DECAYS (controls the ratio!)' if p > 0.4 else '(no clear decay)'}")
    return rows


if __name__ == '__main__':
    lams = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    run(lams, 'zeta')
    run([(7.0, 14)], 'DH')
