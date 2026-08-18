"""W3 (row d, scattering question): explicit finite-dimensional realizations of
X_T, Y_T with X_T^*X_T = R_T, Y_T^*Y_T = L_T, built channel-by-channel in the
piecewise-constant Galerkin space of rowd_assembly.py.

    X_T F = ( G_{Gamma,T}^{1/2} F ,  ( sqrt(w_n) J_{n,-} F )_n )
    Y_T F = ( sqrt(m_0) F        ,  ( sqrt(w_n) J_{n,+} F )_n )
    J_{a,pm} F = ( Ftilde(.+a) pm Ftilde ) / sqrt(2)

Realization of J_{a,pm}: build the "enlarged mesh" = original cell edges union
shifted-by-(-a) edges (so both Ftilde and Ftilde(.+a) are piecewise constant on
it), represent both as 0/1 embedding matrices scaled by sqrt(cell length) (an
L2-orthonormal codomain basis), and take (Shift +- ZeroExt)/sqrt(2).  This is
verified below (see W3_task1_verify.py) to reproduce shift_form()'s form
matrices to machine precision:  J_{a,-}^*J_{a,-} = Gram - 0.5(S+S^T),
J_{a,+}^*J_{a,+} = Gram + 0.5(S+S^T), matching rowd_assembly.assemble()'s R,L
accumulation exactly.

The Gamma channel has no elementary explicit L^2(R) realization available in
this codebase (Psi is only known as a truncated series / closed form on the
mesh, not an explicit Fourier synthesis), so G_{Gamma,T}^{1/2} is realized as
the ABSTRACT symmetric PSD square root of the assembled Gram form G (exact
matrix identity Xg^T Xg = G by construction; this does not claim any
particular physical codomain for the Gamma channel beyond "some Hilbert
space", which is all Douglas' lemma needs).

No file outside this phase directory is touched; rowd_assembly.py and
rowd_threshold.py are read-only imports, never modified.
"""
import math
import numpy as np
import rowd_assembly as RA


def enlarged_embed(c, d, a):
    """Enlarged-mesh embedding matrices for shift a.

    Returns (ce, de, ZeroExt_hat, Shift_hat), each an (M,) / (M,N) array,
    N = len(c).  ZeroExt_hat @ u are the L2-orthonormal-basis coefficients of
    Ftilde on the enlarged mesh; Shift_hat @ u those of Ftilde(.+a).
    """
    edges = np.concatenate([c, d, c - a, d - a])
    edges = np.unique(np.round(edges, 12))
    ce, de = edges[:-1], edges[1:]
    mid = 0.5 * (ce + de)
    inside0 = (mid[:, None] > c[None, :]) & (mid[:, None] < d[None, :])
    insideS = ((mid + a)[:, None] > c[None, :]) & ((mid + a)[:, None] < d[None, :])
    Dn = np.sqrt(de - ce)
    ZeroExt = Dn[:, None] * inside0.astype(float)
    Shift = Dn[:, None] * insideS.astype(float)
    return ce, de, ZeroExt, Shift


def psd_sqrt(M, clip=True):
    """Symmetric PSD square root via eigh; clips tiny negative eigenvalues
    (roundoff) to zero if clip=True."""
    w, V = np.linalg.eigh(0.5 * (M + M.T))
    if clip:
        w = np.clip(w, 0.0, None)
    return (V * np.sqrt(w)) @ V.T


def build_channels(T, refine=4):
    """Assemble all channel blocks of X_T, Y_T on the FULL mesh (not yet
    restricted to P_T).  Returns a dict with the mesh, R/L/A from
    rowd_assembly, the Gamma/const blocks, and per-n antisymmetric/symmetric
    blocks together with the enlarged-mesh cell edges (for structure work)."""
    M = RA.assemble(T, refine=refine)
    c, d, Gram, G, R, L, A = M['c'], M['d'], M['Gram'], M['G'], M['R'], M['L'], M['A']
    N = len(c)

    Xg = psd_sqrt(G)                                   # Gamma channel, N x N
    Y0 = math.sqrt(RA.M0) * np.diag(np.sqrt(d - c))     # constant channel, N x N

    Nmax = M['N']
    lam = RA.von_mangoldt(max(Nmax, 2))
    ns = [n for n in RA.prime_powers_upto(max(Nmax, 2)) if n < math.exp(2 * T) - 1e-13]

    ant, sym, edges, ws = {}, {}, {}, {}
    for n in ns:
        w = lam[n] / math.sqrt(n)
        a = math.log(n)
        ce, de, Z0, Sh = enlarged_embed(c, d, a)
        ant[n] = math.sqrt(w) * (Sh - Z0) / math.sqrt(2)
        sym[n] = math.sqrt(w) * (Sh + Z0) / math.sqrt(2)
        edges[n] = (ce, de)
        ws[n] = w

    return dict(T=T, refine=refine, c=c, d=d, Gram=Gram, G=G, R=R, L=L, A=A,
                Tate=M['Tate'], N=N, ns=ns, Xg=Xg, Y0=Y0, ant=ant, sym=sym,
                edges=edges, ws=ws)


def stack_blocks(blocks):
    """Vertically stack a list of (Mi,N) blocks sharing N columns."""
    return np.vstack(blocks)


def verify_full(ch):
    """X^T X vs R, Y^T Y vs L, difference vs A -- all on the full mesh."""
    Xblocks = [ch['Xg']] + [ch['ant'][n] for n in ch['ns']]
    Yblocks = [ch['Y0']] + [ch['sym'][n] for n in ch['ns']]
    XtX = sum(B.T @ B for B in Xblocks)
    YtY = sum(B.T @ B for B in Yblocks)
    R, L, A = ch['R'], ch['L'], ch['A']
    return dict(
        resid_XtX_R=float(np.abs(XtX - R).max()), scale_R=float(np.abs(R).max()),
        resid_YtY_L=float(np.abs(YtY - L).max()), scale_L=float(np.abs(L).max()),
        resid_diff_A=float(np.abs((XtX - YtY) - A).max()), scale_A=float(np.abs(A).max()),
        XtX=XtX, YtY=YtY)


def primitive_basis(Tate, Gram, rtol=1e-11):
    """Gram-orthonormal basis Z of P_T = ker(Tate): Z^T Gram Z = I_dimP."""
    u, s, vt = np.linalg.svd(Tate)
    k = int(np.sum(s > rtol * max(s.max(), 1e-300)))
    Zraw = vt[k:].T
    Gq = Zraw.T @ Gram @ Zraw
    wq, Vq = np.linalg.eigh(0.5 * (Gq + Gq.T))
    keep = wq > 1e-12 * max(wq.max(), 1e-300)
    Gq_isqrt = (Vq[:, keep] * (1.0 / np.sqrt(wq[keep]))) @ Vq[:, keep].T
    return Zraw @ Gq_isqrt


def restrict_channels(ch, Z):
    """Restrict all X_T, Y_T blocks to the primitive space P_T via basis Z
    (columns L2-orthonormal in the Gram metric, so restricted blocks are
    honest matrices w.r.t. Euclidean domain coordinates)."""
    Xg_P = ch['Xg'] @ Z
    Y0_P = ch['Y0'] @ Z
    ant_P = {n: ch['ant'][n] @ Z for n in ch['ns']}
    sym_P = {n: ch['sym'][n] @ Z for n in ch['ns']}
    R_P = Z.T @ ch['R'] @ Z
    L_P = Z.T @ ch['L'] @ Z
    A_P = Z.T @ ch['A'] @ Z
    return dict(Xg_P=Xg_P, Y0_P=Y0_P, ant_P=ant_P, sym_P=sym_P,
                R_P=R_P, L_P=L_P, A_P=A_P, ns=ch['ns'], dimP=Z.shape[1])
