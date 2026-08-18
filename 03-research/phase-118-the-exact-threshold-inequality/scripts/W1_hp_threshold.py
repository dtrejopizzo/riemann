"""High-precision threshold-block construction and both criticality routes.
Built on W1_hp_lib.py.  Does not import or modify rowd_threshold.py; the
block algebra below is transcribed independently from SPEC.md / PROOF_
ARCHITECTURE.md / main.tex (thm:exactstep, eq:newdSchurTarget,
thm:newdRegularizedStep) so that agreement with the float64 code is a real
cross-check, not shared code.

Route 1 ("direct"): eigendecompose A0 (mp.eigsy) once; from it build both
  (a) the cutoff pseudo-inverse A0^dag with a stated rtol (matches
      rowd_threshold._psd_pinv exactly), and
  (b) the exact eps-regularized penalty pen(eps) = b_E^T(A0+eps)^{-1}b_E for
      a sequence of eps, using the SAME eigenvalues/eigenvectors (no new
      solves needed -- this is just a different linear combination of the
      same spectral data), so its eps->0 limit can be compared to (a).
R0 and S_E are treated as nonsingular (mp.lu_solve), per RESUME.md (a).

Route 2 ("regularized", thm:newdRegularizedStep): builds D_0, Q_c, D_E from
R0 and S_E's OWN eigendecompositions (never touches A0 or its eigen-
decomposition) and regularizes the near-singular D_0 via mp.lu_solve at a
sequence of eps, matching the theorem's C_eps literally.  This is the
independent cross-check requested in the task.
"""
import math
import mpmath as mp
import W1_hp_lib as L


def _mm(A, B):
    return A * B


def _blk(F, U, V):
    return U.transpose() * F * V


def threshold_blocks_mp(q_old, q_new, refine, rtol_null=None):
    T_old = mp.mpf(0.5) * mp.log(q_old)
    T_new = mp.mpf(0.5) * mp.log(q_new)
    M = L.assemble_mp(T_new, refine, extra_points=(T_old, -T_old))
    c, d, Gram = M['c'], M['d'], M['Gram']
    n = M['n']

    Znew = L.svd_nullspace(M['Tate'], rtol=rtol_null)  # n x dimP
    dimP = Znew.cols

    mid = [(c[i] + d[i]) / 2 for i in range(n)]
    inside_idx = [i for i in range(n) if -T_old < mid[i] < T_old]
    ninside = len(inside_idx)
    Esup = mp.matrix(n, ninside)
    for k, i in enumerate(inside_idx):
        Esup[i, k] = 1

    TateEsup = M['Tate'] * Esup  # 2 x ninside
    nsp = L.svd_nullspace(TateEsup, rtol=rtol_null)  # ninside x dimC
    Zc = Esup * nsp  # n x dimC
    dimC = Zc.cols

    Gc = Zc.transpose() * Gram * Zc  # dimC x dimC
    ZcTGram = Zc.transpose() * Gram  # dimC x n
    RHS = ZcTGram * Znew  # dimC x dimP  (solve(Gc, Zc^T Gram Znew))
    sol = L.mat_solve(Gc, RHS)  # dimC x dimP
    resid = Znew - Zc * sol  # n x dimP

    Gr = resid.transpose() * Gram * resid  # dimP x dimP, rank dimA
    wGr, VGr = mp.eigsy(Gr)
    wmax = max(wGr)
    keep = [i for i in range(len(wGr)) if wGr[i] > mp.mpf(10) ** (-(mp.mp.dps - 8)) * wmax]
    dimA = len(keep)
    Za_pre = resid * mp.matrix([[VGr[i, j] for j in keep] for i in range(VGr.rows)])
    Za = mp.matrix(n, dimA)
    for jj, i in enumerate(keep):
        s = 1 / mp.sqrt(wGr[i])
        for r in range(n):
            Za[r, jj] = Za_pre[r, jj] * s

    R, Lm, A = M['R'], M['L'], M['A']
    out = dict(T_old=T_old, T_new=T_new, q_old=q_old, q_new=q_new,
               cells=n, dimP=dimP, dimC=dimC, dimA=dimA, M=M, Zc=Zc, Za=Za)
    out['R0'] = _blk(R, Zc, Zc)
    out['L0'] = _blk(Lm, Zc, Zc)
    out['r'] = _blk(R, Zc, Za)
    out['l'] = _blk(Lm, Zc, Za)
    out['RE'] = _blk(R, Za, Za)
    out['LE'] = _blk(Lm, Za, Za)
    out['A0'] = out['R0'] - out['L0']
    out['Anew'] = out['RE'] - out['LE']
    out['B'] = _blk(A, Zc, Za)
    return out


def _sym(M):
    return (M + M.transpose()) / 2


def route1_direct(bk, rtol_A0=mp.mpf('1e-11'), eps_list=()):
    """Direct target route.  Eigendecomposes R0, A0, S_E (each once).
    Returns dict with: cutoff-based lam_min_norm (matches rowd_threshold
    exactly, at rtol_A0), plus lam_min_norm(eps) for each eps in eps_list
    computed from A0's spectral data, plus diagnostics (minA0, minR0,
    minSE, ranks)."""
    R0, L0, r, l = bk['R0'], bk['L0'], bk['r'], bk['l']
    RE, LE, A0 = bk['RE'], bk['LE'], bk['A0']
    dimC, dimA = bk['dimC'], bk['dimA']

    # H = R0^{-1} r  (R0 treated as nonsingular)
    H = L.mat_solve(_sym(R0), r)
    S_E = RE - r.transpose() * H
    ZtZ = LE - l.transpose() * H - H.transpose() * l + H.transpose() * L0 * H
    b_E = L0 * H - l
    S_cutoffbase = S_E - ZtZ  # add -pen(eps) below

    wA, VA = mp.eigsy(_sym(A0))
    minA0 = min(wA)
    maxA0 = max(wA)

    # cutoff pinv (matches rowd_threshold._psd_pinv with rtol_A0)
    keepA = [i for i in range(dimC) if wA[i] > rtol_A0 * max(maxA0, mp.mpf('1e-300'))]
    # project b_E onto eigenbasis: bproj = VA^T b_E  (dimC x dimA)
    bproj = VA.transpose() * b_E
    pen_cut = mp.matrix(dimA, dimA)
    for i in keepA:
        col = mp.matrix([bproj[i, j] for j in range(dimA)])
        pen_cut += (1 / wA[i]) * (col * col.transpose())
    S_cut = S_cutoffbase - pen_cut

    # eps-regularized pen(eps), same spectral data, exact formula
    pens_eps = {}
    for eps in eps_list:
        pen_e = mp.matrix(dimA, dimA)
        for i in range(dimC):
            col = mp.matrix([bproj[i, j] for j in range(dimA)])
            pen_e += (1 / (wA[i] + eps)) * (col * col.transpose())
        pens_eps[eps] = S_cutoffbase - pen_e

    # normalization by S_E
    wSE, VSE = mp.eigsy(_sym(S_E))
    minSE = min(wSE)
    maxSE = max(wSE)
    rtol_SE = mp.mpf(10) ** (-(mp.mp.dps - 8))
    keepSE = [i for i in range(dimA) if wSE[i] > rtol_SE * max(maxSE, mp.mpf('1e-300'))]
    rankSE = len(keepSE)
    isqSE = mp.matrix(dimA, dimA)
    for i in keepSE:
        vi = mp.matrix([VSE[k, i] for k in range(dimA)])
        isqSE += (1 / mp.sqrt(wSE[i])) * (vi * vi.transpose())

    def lam_min_of(Smat):
        Snorm = isqSE * Smat * isqSE
        w = mp.eigsy(_sym(Snorm), eigvals_only=True)
        wl = sorted(w)
        wl = wl[-rankSE:] if rankSE < len(wl) else wl
        return min(wl)

    lam_cut = lam_min_of(S_cut)
    lam_eps = {eps: lam_min_of(pens_eps[eps]) for eps in eps_list}

    return dict(lam_min_norm_cutoff=lam_cut, lam_min_norm_eps=lam_eps,
                minA0=minA0, maxA0=maxA0, minSE=minSE, maxSE=maxSE,
                rankSE=rankSE, dimA=dimA, dimC=dimC, wA0_sorted=sorted(wA))


def diagnostic_Hc_correction(bk, eps_list):
    """Diagnostic only (not one of the two reported routes): checks the
    algebraic identity b_E = (r-l) - A0 H (eq:newdOppositeResidual) against
    Q_c = R0^{-1/2}(r-l)S_E^{-1/2} and H_c = R0^{-1/2} r S_E^{-1/2}
    (H_c as in the paragraph preceding thm:newdRegularizedStep), by testing
    whether pen_normalized := (Q_c - D_0 H_c)^T (D_0+eps)^{-1} (Q_c-D_0 H_c)
    -- i.e. literally regularizing b_E's own normalized form, NOT Q_c alone
    -- converges to S_E^{-1/2} b_E^T A0^dag b_E S_E^{-1/2} (route1's pen,
    normalized).  Used to localize the route1/route2 numerical disagreement:
    does it come from the missing H_c cross term, or from something else?"""
    R0, L0, r, l = bk['R0'], bk['L0'], bk['r'], bk['l']
    RE, LE = bk['RE'], bk['LE']
    dimC, dimA = bk['dimC'], bk['dimA']

    wR, VR = mp.eigsy(_sym(R0))
    rtolR = mp.mpf(10) ** (-(mp.mp.dps - 8))
    Rh = mp.matrix(dimC, dimC)
    for i in range(dimC):
        if wR[i] > rtolR * max(wR):
            vi = mp.matrix([VR[k, i] for k in range(dimC)])
            Rh += (1 / mp.sqrt(wR[i])) * (vi * vi.transpose())

    S_E = RE - r.transpose() * L.mat_solve(_sym(R0), r)
    wS, VS = mp.eigsy(_sym(S_E))
    rtolS = mp.mpf(10) ** (-(mp.mp.dps - 8))
    Sh = mp.matrix(dimA, dimA)
    for i in range(dimA):
        if wS[i] > rtolS * max(wS):
            vi = mp.matrix([VS[k, i] for k in range(dimA)])
            Sh += (1 / mp.sqrt(wS[i])) * (vi * vi.transpose())

    T0 = Rh * L0 * Rh
    D0 = _sym(mp.eye(dimC) - T0)
    Qc = Rh * (r - l) * Sh
    Hc = Rh * r * Sh
    bN = Qc - D0 * Hc

    out = {}
    for eps in eps_list:
        Deps = D0 + eps * mp.eye(dimC)
        X = L.mat_solve(Deps, bN)
        pen_n = bN.transpose() * X
        out[eps] = pen_n
    return out


def route2_regularized(bk, eps_list):
    """thm:newdRegularizedStep's C_eps route.  Uses R0 and S_E's own
    eigendecompositions; never touches A0.  Returns lam_min(C_eps) for each
    eps (smallest eigenvalue, via eigsy eigvals_only), which per the theorem
    should agree with route1's lam_min_norm(eps) in the limit eps->0."""
    R0, L0, r, l = bk['R0'], bk['L0'], bk['r'], bk['l']
    RE, LE = bk['RE'], bk['LE']
    dimC, dimA = bk['dimC'], bk['dimA']

    wR, VR = mp.eigsy(_sym(R0))
    minR0, maxR0 = min(wR), max(wR)
    rtolR = mp.mpf(10) ** (-(mp.mp.dps - 8))
    # R0 assumed nonsingular; still guard with a cutoff for the sqrt
    Rh = mp.matrix(dimC, dimC)   # R0^{-1/2}
    for i in range(dimC):
        if wR[i] > rtolR * max(maxR0, mp.mpf('1e-300')):
            vi = mp.matrix([VR[k, i] for k in range(dimC)])
            Rh += (1 / mp.sqrt(wR[i])) * (vi * vi.transpose())

    wS, VS = mp.eigsy(_sym(bk['RE'] - r.transpose() * L.mat_solve(_sym(R0), r)))
    minSE, maxSE = min(wS), max(wS)
    rtolS = mp.mpf(10) ** (-(mp.mp.dps - 8))
    Sh = mp.matrix(dimA, dimA)   # S_E^{-1/2}
    for i in range(dimA):
        if wS[i] > rtolS * max(maxSE, mp.mpf('1e-300')):
            vi = mp.matrix([VS[k, i] for k in range(dimA)])
            Sh += (1 / mp.sqrt(wS[i])) * (vi * vi.transpose())

    T0 = Rh * L0 * Rh
    D0 = mp.eye(dimC) - T0
    D0 = _sym(D0)
    wD0 = mp.eigsy(D0, eigvals_only=True)
    minD0 = min(wD0)

    Qc = Rh * (r - l) * Sh
    DE = mp.eye(dimA) - Sh * LE * Sh
    DE = _sym(DE)

    out = {}
    for eps in eps_list:
        Deps = D0 + eps * mp.eye(dimC)
        X = L.mat_solve(Deps, Qc)   # dimC x dimA
        Ceps = DE - Qc.transpose() * X
        Ceps = _sym(Ceps)
        w = mp.eigsy(Ceps, eigvals_only=True)
        out[eps] = min(w)
    return dict(lam_min_Ceps=out, minR0=minR0, maxR0=maxR0,
                minSE=minSE, maxSE=maxSE, minD0=minD0)
