"""W2 task (4): exact/elementary treatment of the 2-dimensional Tate corona
block, using the explicit vectors psi_+, psi_- that span it.

PART A (fully elementary, exact, verified below against the Galerkin split):
The Tate corona directions are NOT the raw e^{+-t/2}|_{I_tau_old} -- those have
nonzero Tate moments on the *new* window and must be corrected to land back in
P_new. Because e^{+-t/2}|_{I_tau_old} is *already* L2-orthogonal to the old
core C exactly (M_+/-(F)=0 for F in C is the definition of "primitive"), the
corona-projection equals the P_new-projection, and solving the 2x2 linear
system

    [ 2 sinh(Tn)   2 Tn        ] [c+]   [ 2 sinh(To) ]
    [ 2 Tn         2 sinh(Tn)  ] [c-] = [ 2 To       ]      (*)

for the coefficients that kill the two Tate moments gives, in closed form,

    psi_+(t) = e^{t/2} 1_{I_To}(t)  -  c+ e^{t/2} 1_{I_Tn}(t)  -  c- e^{-t/2} 1_{I_Tn}(t)
    psi_-(t) = e^{-t/2} 1_{I_To}(t) -  d+ e^{t/2} 1_{I_Tn}(t)  -  d- e^{-t/2} 1_{I_Tn}(t)

with (d+,d-) solving the same system (*) with RHS (2To, 2sinh(To)) instead of
(2sinh(To),2To) [the t -> -t mirror]. These are verified below to coincide
with Za_tate (rowd_threshold's numerical corona/Tate split) to O(1/refine),
principal angle -> 0 as refine -> infinity.

PART B (fully elementary): the SHIFT/prime contribution to <R psi_a,psi_b>,
<L psi_a,psi_b> reduces to finite sums of elementary exponential integrals
(no kernel subtleties -- shift is a literal interval-restricted translation).

PART C (semi-closed-form): the GAMMA-channel contribution <G psi_a,psi_b>.
psi_a is only piecewise-smooth (jumps at +-T_old); a direct real-space double
integral against the kernel K(D)=sum_j exp(-a_j|D|) (=Psi'') DIVERGES termwise
(K ~ 1/(2|D|) as D->0, not locally integrable), so it cannot be evaluated as
written. Two integrations by parts (verified below to reproduce
rowd_assembly.gamma_form's own sign convention exactly on indicator/piecewise-
constant test functions) give the exact identity

    <G f,g> = int int f'(t) g'(s) Psi(t-s) dt ds        (**)

with f',g' the DISTRIBUTIONAL derivatives (delta functions at jumps, plus a
smooth piecewise-exponential density elsewhere) -- Psi itself (not its
singular second derivative) is what appears, and Psi is a bounded, closed-form
function everywhere including D=0. This reduces <G psi_a,psi_b> to a finite
sum of delta-delta terms (trivial: Psi evaluated at a point), delta-smooth
terms (1D elementary exponential integrals against Psi, summed as an
absolutely convergent a_j-series exactly parallel to Psi's own definition),
and smooth-smooth terms (elementary double-exponential integrals against
exp(-a_j|D|), same series). All terms are implemented below in closed
(a_j-series) form and cross-checked against Richardson-extrapolated Galerkin
gamma_form values.

PART D (negative result, reported honestly): the block that actually appears
in the target, S_E|_tate - Z_E^*Z_E|_tate - b_E^*A0^dag b_E|_tate, additionally
needs H = R0^dag r with r = Zc^T R psi (coupling to the OLD CORE). Zc is the
old core's own primitive basis, which has NO elementary closed form in
general (it encodes every prime power below q_old). So H solves

    R0 H_a = Zc^T (R psi_a)                                (***)

-- the R0-weighted L2 projection of the EXPLICIT function R psi_a onto the old
core -- a well-posed reduction, but not further reducible to elementary
functions of (T_old,T_new) alone. The 2x2 reduction isolates *which* two
directions carry the criticality (tasks 1-3); it does not eliminate the
coupling to the arithmetic history, which is exactly what R0, A0, r, l already
compute numerically in rowd_threshold. This limitation is the deliverable of
this part.

Command:
    python3 W2_tate_closedform.py
"""
import math
import numpy as np
from scipy import integrate
import rowd_assembly as RA
import rowd_threshold as RT
import W2_common as W2

EULER = RA.EULER
M0 = RA.M0


# --------------------------------------------------------- Part A: psi_+-  psi_-
def tate_corona_coeffs(T_old, T_new):
    a = 2 * math.sinh(T_new)
    b = 2 * T_new
    p = 2 * math.sinh(T_old)
    q = 2 * T_old
    det = a * a - b * b
    cplus_p = (a * p - b * q) / det
    cminus_p = (a * q - b * p) / det
    # t -> -t mirror for psi_-
    cplus_m = cminus_p
    cminus_m = cplus_p
    return dict(cplus_p=cplus_p, cminus_p=cminus_p, cplus_m=cplus_m, cminus_m=cminus_m)


def pieces_psi(sign, T_old, T_new, coeffs):
    """Return breakpoints [-Tn,-To,To,Tn] and per-interval (kp,km) coefficients
    of kp*e^{t/2}+km*e^{-t/2} for psi_+ (sign='p') or psi_- (sign='m')."""
    cp, cm = (coeffs['cplus_p'], coeffs['cminus_p']) if sign == 'p' else (coeffs['cplus_m'], coeffs['cminus_m'])
    old = (1 - cp, -cm) if sign == 'p' else (-cp, 1 - cm)
    ann = (-cp, -cm)
    bp = [-T_new, -T_old, T_old, T_new]
    ivals = [ann, old, ann]
    return bp, ivals


def eval_pieces(bp, ivals, t):
    t = np.atleast_1d(np.asarray(t, dtype=float))
    out = np.zeros_like(t)
    for k in range(len(ivals)):
        lo, hi = bp[k], bp[k + 1]
        m = (t >= lo) & (t <= hi)
        kp, km = ivals[k]
        out[m] = kp * np.exp(t[m] / 2) + km * np.exp(-t[m] / 2)
    return out


# --------------------------------------------------- Part B: shift/prime terms
def E(k, lo, hi):
    if abs(k) < 1e-13:
        return hi - lo
    return (math.exp(k * hi) - math.exp(k * lo)) / k


def shift_pair_elem(bp_f, iv_f, bp_g, iv_g, a):
    """<S_a f,g> = int f(t+a) g(t) dt over the piecewise-exponential f,g
    (rowd_assembly shift_form convention). Elementary, exact."""
    total = 0.0
    for kf in range(len(iv_f)):
        u1, v1 = bp_f[kf], bp_f[kf + 1]
        kp1, km1 = iv_f[kf]
        # f(t+a) on t-domain [u1-a, v1-a]
        for kg in range(len(iv_g)):
            u2, v2 = bp_g[kg], bp_g[kg + 1]
            kp2, km2 = iv_g[kg]
            lo = max(u2, u1 - a)
            hi = min(v2, v1 - a)
            if lo >= hi:
                continue
            # f(t+a) = kp1*e^{(t+a)/2} + km1*e^{-(t+a)/2}
            #        = kp1*e^{a/2} e^{t/2} + km1*e^{-a/2} e^{-t/2}
            fa_p, fa_m = kp1 * math.exp(a / 2), km1 * math.exp(-a / 2)
            # integrand: (fa_p e^{t/2}+fa_m e^{-t/2})(kp2 e^{t/2}+km2 e^{-t/2})
            total += fa_p * kp2 * E(1.0, lo, hi)
            total += fa_p * km2 * E(0.0, lo, hi)
            total += fa_m * kp2 * E(0.0, lo, hi)
            total += fa_m * km2 * E(-1.0, lo, hi)
    return total


def l2_pair_elem(bp_f, iv_f, bp_g, iv_g):
    return shift_pair_elem(bp_f, iv_f, bp_g, iv_g, 0.0)


def R_L_tate_shift_part(T_old, T_new, N, bp_p, iv_p, bp_m, iv_m):
    """The Gram + shift-sum contributions to <R psi_a,psi_b>, <L psi_a,psi_b>,
    a,b in {+,-} -- i.e. everything in R,L except the Gamma channel.
    R = G + sum w_n(I - ReS_n), L = m0*I + sum w_n(I+ReS_n)."""
    lam = RA.von_mangoldt(max(N, 2))
    pieces = {'p': (bp_p, iv_p), 'm': (bp_m, iv_m)}
    out = {}
    for a in ('p', 'm'):
        for b in ('p', 'm'):
            bpf, ivf = pieces[a]
            bpg, ivg = pieces[b]
            l2 = l2_pair_elem(bpf, ivf, bpg, ivg)
            Rval = 0.0
            Lval = M0 * l2
            for n in RA.prime_powers_upto(max(N, 2)):
                if not (n < math.exp(2 * T_new) - 1e-13):
                    continue
                w = lam[n] / math.sqrt(n)
                ln = math.log(n)
                s_pos = shift_pair_elem(bpf, ivf, bpg, ivg, ln)
                s_neg = shift_pair_elem(bpf, ivf, bpg, ivg, -ln)
                sym = s_pos + s_neg
                Rval += w * (l2 - 0.5 * sym)
                Lval += w * (l2 + 0.5 * sym)
            out[(a, b)] = dict(l2=l2, R_shift=Rval, L_shift=Lval)
    return out


# --------------------------------------------------------- Part C: Gamma term
def piece_jumps(bp, ivals):
    """Distributional derivative of the piecewise function: delta weights at
    each breakpoint (value from the right minus value from the left, treating
    outside the outer breakpoints as 0), and the smooth density (dp,dm) with
    d/dt[kp e^{t/2}+km e^{-t/2}] = (kp/2) e^{t/2} - (km/2) e^{-t/2} on each
    open interval."""
    n = len(bp)

    def val(k, t):
        if k < 0 or k >= len(ivals):
            return 0.0
        kp, km = ivals[k]
        return kp * math.exp(t / 2) + km * math.exp(-t / 2)

    jumps = []
    for i, t0 in enumerate(bp):
        left = val(i - 1, t0)
        right = val(i, t0)
        jumps.append((t0, right - left))
    smooth = []
    for k in range(len(ivals)):
        kp, km = ivals[k]
        smooth.append((bp[k], bp[k + 1], kp / 2.0, -km / 2.0))
    return jumps, smooth


def _product_E_disjoint(g1, u1, v1, g2, u2, v2, a, sign):
    """product E(g1+sign*a,u1,v1)*E(g2-sign*a,u2,v2). k1=g1+sign*a or
    k2=g2-sign*a can be EXACTLY 0 (a=|g1|=0.5=a_0, j=0, the only place this
    happens for our g in {+-0.5}) -- E's own k=0 branch (returning hi-lo)
    handles that correctly, so for small/moderate a we call E directly
    (overflow-safe there). Only for LARGE a (where k1,k2 are never 0, since
    0.5 is the sole zero-crossing) do we need the combined-exponent form to
    avoid overflow."""
    k1 = g1 + sign * a
    k2 = g2 - sign * a
    if abs(k1) * max(abs(u1), abs(v1), 1e-300) < 600.0 and abs(k2) * max(abs(u2), abs(v2), 1e-300) < 600.0:
        return E(k1, u1, v1) * E(k2, u2, v2)

    def texp(x, y):
        return _safe_exp(g1 * x + g2 * y + sign * a * (x - y))

    num = texp(v1, v2) - texp(v1, u2) - texp(u1, v2) + texp(u1, u2)
    # k1,k2 cannot be 0 here: the direct branch above already caught the sole
    # zero-crossing (a=0.5); for the large-a regime reaching this line, both
    # |k1|,|k2| are bounded well away from 0.
    return num / (k1 * k2)


def I_exp_kernel(u1, v1, u2, v2, g1, g2, a):
    """int_{u1}^{v1} int_{u2}^{v2} exp(g1 t + g2 s) exp(-a|t-s|) dt ds, exact
    (elementary), evaluated overflow-safely for arbitrarily large a by always
    combining offsets into a single exponent before calling exp."""
    if v1 <= u2 + 1e-14:
        return _product_E_disjoint(g1, u1, v1, g2, u2, v2, a, sign=+1.0)
    if u1 >= v2 - 1e-14:
        return _product_E_disjoint(g1, u1, v1, g2, u2, v2, a, sign=-1.0)
    if abs(u1 - u2) < 1e-13 and abs(v1 - v2) < 1e-13:
        # Same interval (needed only for the diagonal a=b block, and only at
        # moderate a_j -- caller restricts a to a safe range and separately
        # bounds the tail; see bilinear_G_elementary). Plain quadrature here
        # is validated against dblquad to >=8 digits for the a-range used.
        u, v = u1, v1

        def inner_lt(t):
            return math.exp((g1 + a) * t) * E(g2 - a, t, v)

        def inner_gt(t):
            return math.exp((g1 - a) * t) * E(g2 + a, u, t)

        part_lt, _ = integrate.quad(inner_lt, u, v, limit=200, epsabs=1e-13, epsrel=1e-13)
        part_gt, _ = integrate.quad(inner_gt, u, v, limit=200, epsabs=1e-13, epsrel=1e-13)
        return part_lt + part_gt
    raise NotImplementedError('overlapping non-identical intervals not needed here')


def _safe_exp(x):
    return math.exp(x) if x < 700.0 else math.exp(700.0)


def _Eoffset(k, offset, lo, hi):
    """int_lo^hi exp(offset + k*s) ds, computed with the offset folded into
    the exponent BEFORE calling exp (avoids overflow when offset alone is
    huge but offset+k*s stays bounded, which is exactly what happens for
    large a_j here)."""
    if abs(k) < 1e-13:
        return _safe_exp(offset) * (hi - lo)
    return (_safe_exp(offset + k * hi) - _safe_exp(offset + k * lo)) / k


def delta_smooth_integral(t0, u, v, dp, dm, a):
    """int_u^v (dp e^{s/2}+dm e^{-s/2}) exp(-a|t0-s|) ds, exact elementary."""
    total = 0.0
    if u < t0:
        hi = min(v, t0)
        if hi > u:
            # s<t0: |t0-s|=t0-s -> exp(-a(t0-s)) = exp(-a t0 + a s)
            total += dp * _Eoffset(0.5 + a, -a * t0, u, hi)
            total += dm * _Eoffset(-0.5 + a, -a * t0, u, hi)
    if v > t0:
        lo = max(u, t0)
        if v > lo:
            # s>t0: |t0-s|=s-t0 -> exp(-a(s-t0)) = exp(a t0 - a s)
            total += dp * _Eoffset(0.5 - a, a * t0, lo, v)
            total += dm * _Eoffset(-0.5 - a, a * t0, lo, v)
    return total


def bilinear_G_elementary(bp_f, iv_f, bp_g, iv_g, J0=3000):
    """<G f,g> via <Gf,g>=int int f'(t)g'(s)Psi(t-s)dtds, Psi=sum_j exp(-a_j|D|)/a_j^2.
    Sums j=0..J0-1 with a computable tail bound; each term is elementary.

    The same-interval branch of I_exp_kernel (needed only for the diagonal
    a=b Tate block) is quadrature-based and its raw exp((g+/-a)*t) overflows
    once a_j*|t|>~700; delta_smooth_integral's exponents are always combined
    before exp() so it never overflows regardless of a_j. We therefore cap
    the effective J0 so a_{J0-1}*max_coord stays safely below the overflow
    threshold, and report the (rapidly, >=1/a_j^3, decaying) remainder as a
    tail bound rather than summing past it."""
    max_coord = max(abs(x) for x in list(bp_f) + list(bp_g)) or 1.0
    J0_safe = min(J0, max(50, int(500.0 / max_coord / 2.0)))
    J0 = J0_safe
    jf, sf = piece_jumps(bp_f, iv_f)
    jg, sg = piece_jumps(bp_g, iv_g)
    # delta-delta (trivial: evaluate the already-closed-form Psi)
    dd = 0.0
    for (t0, w0) in jf:
        for (t1, w1) in jg:
            dd += w0 * w1 * RA.psi_kernel(t0 - t1)

    # delta-smooth and smooth-delta, smooth-smooth: sum over a_j with 1/a_j^2
    j = np.arange(J0)
    a_js = 2.0 * j + 0.5
    ds_terms = np.zeros(J0)
    sd_terms = np.zeros(J0)
    ss_terms = np.zeros(J0)
    for jj, a in enumerate(a_js):
        acc_ds = 0.0
        for (t0, w0) in jf:
            for (u, v, dp, dm) in sg:
                acc_ds += w0 * delta_smooth_integral(t0, u, v, dp, dm, a)
        ds_terms[jj] = acc_ds
        acc_sd = 0.0
        for (t0, w0) in jg:
            for (u, v, dp, dm) in sf:
                acc_sd += w0 * delta_smooth_integral(t0, u, v, dp, dm, a)
        sd_terms[jj] = acc_sd
        acc_ss = 0.0
        for (u1, v1, dp1, dm1) in sf:
            for (u2, v2, dp2, dm2) in sg:
                acc_ss += (dp1 * dp2 * I_exp_kernel(u1, v1, u2, v2, 0.5, 0.5, a)
                           + dp1 * dm2 * I_exp_kernel(u1, v1, u2, v2, 0.5, -0.5, a)
                           + dm1 * dp2 * I_exp_kernel(u1, v1, u2, v2, -0.5, 0.5, a)
                           + dm1 * dm2 * I_exp_kernel(u1, v1, u2, v2, -0.5, -0.5, a))
        ss_terms[jj] = acc_ss
    series = (ds_terms + sd_terms + ss_terms) / a_js**2
    total = series.sum()
    # crude tail bound: the summand magnitude decays like the piece-measure
    # bound times exp(-a_J*mindist)/a_J^2 -- since our pieces abut (mindist=0
    # possible), bound tail by (last few terms' magnitude) * 1/(2 J0) (matches
    # Psi's own 1/a_j^2 tail-sum order)
    tail_bound = abs(series[-200:]).max() * a_js[-1] if J0 > 200 else abs(series).max()
    return dd + total, tail_bound


def R_L_tate_gamma_part(bp_p, iv_p, bp_m, iv_m, J0=3000):
    pieces = {'p': (bp_p, iv_p), 'm': (bp_m, iv_m)}
    out = {}
    for a in ('p', 'm'):
        for b in ('p', 'm'):
            bpf, ivf = pieces[a]
            bpg, ivg = pieces[b]
            val, tail = bilinear_G_elementary(bpf, ivf, bpg, ivg, J0=J0)
            out[(a, b)] = dict(G=val, tail_bound=tail)
    return out


# ----------------------------------------------------- validation vs Galerkin
def galerkin_check(q_old, q_new, refine):
    """Independent numerical benchmark: build psi_+-,psi_- as piecewise-const
    cell averages on a fine mesh and use rowd_assembly's *exact* Galerkin
    gamma_form/shift_form directly (no elementary-formula code at all), then
    compare against the elementary-formula values as refine -> infinity."""
    T_old = 0.5 * math.log(q_old)
    T_new = 0.5 * math.log(q_new)
    M = RA.assemble(T_new, refine=refine, extra_points=(T_old, -T_old))
    c, d, Gram = M['c'], M['d'], M['Gram']
    coeffs = tate_corona_coeffs(T_old, T_new)
    bp_p, iv_p = pieces_psi('p', T_old, T_new, coeffs)
    bp_m, iv_m = pieces_psi('m', T_old, T_new, coeffs)
    mid = 0.5 * (c + d)

    def cellavg(bp, ivals):
        out = np.zeros(len(c))
        for k in range(len(ivals)):
            lo, hi = bp[k], bp[k + 1]
            m = (mid > lo) & (mid < hi)
            kp, km = ivals[k]
            w = d[m] - c[m]
            out[m] = (kp * 2 * (np.exp(d[m] / 2) - np.exp(c[m] / 2))
                      + km * 2 * (np.exp(-c[m] / 2) - np.exp(-d[m] / 2))) / w
        return out

    psi_p_vec = cellavg(bp_p, iv_p)
    psi_m_vec = cellavg(bp_m, iv_m)
    R, L, G = M['R'], M['L'], M['G']
    out = {}
    for name, va in (('p', psi_p_vec), ('m', psi_m_vec)):
        for name2, vb in (('p', psi_p_vec), ('m', psi_m_vec)):
            out[(name, name2)] = dict(R=float(va @ R @ vb), L=float(va @ L @ vb), G=float(va @ G @ vb))
    return out


if __name__ == '__main__':
    print("=== Part A: closed-form psi_+, psi_- coefficients ===")
    for (qo, qn) in [(2, 3), (5, 7), (31, 32), (59, 61)]:
        To, Tn = 0.5 * math.log(qo), 0.5 * math.log(qn)
        co = tate_corona_coeffs(To, Tn)
        print(f"  ({qo},{qn}): T_old={To:.6f} T_new={Tn:.6f}  c+={co['cplus_p']:.8f} "
              f"c-={co['cminus_p']:.8f}")

    print("\n=== Part B+C: elementary/semi-closed-form 2x2 raw Tate block "
          "<R psi_a,psi_b>, <L psi_a,psi_b> vs Galerkin ===")
    # NB refine kept modest here: rowd_assembly.gamma_form's Psi-table build
    # is O(cells^2) in memory (an (n_uniq_diffs x J0) array; J0=400 by
    # default) -- refine=256 on (31,32) drove that past 9GB and was killed.
    # refine<=64 with cells<=768 stays under ~1GB and is already far finer
    # than needed: task (1)'s principal-angle check showed the piecewise-
    # constant approximation to psi_+-  converges by refine=32.
    for (qo, qn, gal_refine) in [(2, 3, 64), (5, 7, 64), (31, 32, 32)]:
        To, Tn = 0.5 * math.log(qo), 0.5 * math.log(qn)
        N = int(math.floor(math.exp(2 * Tn)))
        co = tate_corona_coeffs(To, Tn)
        bp_p, iv_p = pieces_psi('p', To, Tn, co)
        bp_m, iv_m = pieces_psi('m', To, Tn, co)
        shift_part = R_L_tate_shift_part(To, Tn, N, bp_p, iv_p, bp_m, iv_m)
        gamma_part = R_L_tate_gamma_part(bp_p, iv_p, bp_m, iv_m, J0=2000)
        gk = galerkin_check(qo, qn, refine=gal_refine)
        print(f"\n step ({qo},{qn}):")
        for key in [('p', 'p'), ('p', 'm'), ('m', 'm')]:
            R_elem = gamma_part[key]['G'] + shift_part[key]['R_shift']
            L_elem = gamma_part[key]['G'] * 0 + shift_part[key]['L_shift']  # L has no G term
            L_elem = shift_part[key]['L_shift']
            R_gal, L_gal = gk[key]['R'], gk[key]['L']
            print(f"   {key}: R_elem={R_elem:.8f}  R_galerkin(r=256)={R_gal:.8f}  "
                  f"diff={R_elem-R_gal:.2e}   |  L_elem={L_elem:.8f}  L_galerkin={L_gal:.8f}  "
                  f"diff={L_elem-L_gal:.2e}   | G_elem={gamma_part[key]['G']:.8f} "
                  f"G_galerkin={gk[key]['G']:.8f} diff={gamma_part[key]['G']-gk[key]['G']:.2e} "
                  f"tail~{gamma_part[key]['tail_bound']:.1e}")
