"""W3 task (3): place-indexed block structure of Phi = Y_T X_T^dagger.

Builds the EXPLICIT channel-blocked matrices (Gamma channel + antisymmetric
contacts J_{n,-} for X; constant channel + symmetric contacts J_{n,+} for Y),
restricts to P_T, forms Phi = Y X^dagger via SVD pseudoinverse at a fixed
rtol, and slices Phi into blocks indexed by (row channel in {const, sym_n},
col channel in {Gamma, ant_m}).  Reports the matrix of block operator norms
||Phi[row,col]||_2, and tests two concrete structural candidates against the
finite-finite part B[n,m] = ||Phi[sym_n, ant_m]||:

  (i)  Toeplitz-in-log:  B[n,m] ~ f(log n - log m)   (decay in the shift)
  (ii) Hankel-in-log:    B[n,m] ~ f(log n + log m)
  (iii) rank-one + diagonal:  B ~ u v^T + diag(d)   (best rank-1 fit of the
        off-diagonal part, relative Frobenius error reported)

Run:  python3 W3_task3b_blocks.py
"""
import math
import numpy as np
import W3_build_xy as W3

THRESHOLDS = [8, 17, 37]
REFINE = 8
RTOL = 1e-10


def build_explicit_phi(q, refine=REFINE, rtol=RTOL):
    T = 0.5 * math.log(q)
    ch = W3.build_channels(T, refine=refine)
    Z = W3.primitive_basis(ch['Tate'], ch['Gram'])
    rc = W3.restrict_channels(ch, Z)
    ns = rc['ns']

    col_blocks = [('Gamma', rc['Xg_P'])] + [(f'ant_{n}', rc['ant_P'][n]) for n in ns]
    row_blocks = [('const', rc['Y0_P'])] + [(f'sym_{n}', rc['sym_P'][n]) for n in ns]

    Xmat = np.vstack([B for _, B in col_blocks])
    Ymat = np.vstack([B for _, B in row_blocks])

    col_sizes = [B.shape[0] for _, B in col_blocks]
    row_sizes = [B.shape[0] for _, B in row_blocks]
    col_off = np.concatenate([[0], np.cumsum(col_sizes)])
    row_off = np.concatenate([[0], np.cumsum(row_sizes)])

    U, S, Vt = np.linalg.svd(Xmat, full_matrices=False)
    keep = S > rtol * S.max()
    k = int(keep.sum())
    Xdag = (Vt[:k].T * (1.0 / S[:k])) @ U[:, :k].T
    Phi = Ymat @ Xdag

    col_names = [nm for nm, _ in col_blocks]
    row_names = [nm for nm, _ in row_blocks]
    return dict(T=T, q=q, ns=ns, Phi=Phi, col_off=col_off, row_off=row_off,
                col_names=col_names, row_names=row_names, rank_X=k,
                dimP=Xmat.shape[1], rows_X=Xmat.shape[0], rows_Y=Ymat.shape[0])


def block_norm_matrix(res):
    Phi = res['Phi']
    ro, co = res['row_off'], res['col_off']
    nr, nc = len(res['row_names']), len(res['col_names'])
    B = np.zeros((nr, nc))
    for i in range(nr):
        for j in range(nc):
            blk = Phi[ro[i]:ro[i+1], co[j]:co[j+1]]
            B[i, j] = np.linalg.norm(blk, 2) if blk.size else 0.0
    return B


def print_block_matrix(res, B):
    names_r = res['row_names']
    names_c = res['col_names']
    print(f"\n=== q={res['q']} T={res['T']:.4f}  rank(X)={res['rank_X']}/{res['dimP']} "
          f"rows_X={res['rows_X']} rows_Y={res['rows_Y']} ===")
    header = "        " + "".join(f"{c:>9}" for c in names_c)
    print(header)
    for i, rn in enumerate(names_r):
        row = "".join(f"{B[i,j]:9.4f}" for j in range(len(names_c)))
        print(f"{rn:>8}{row}")


def channel_split_norms(res):
    """Operator norm of Phi restricted to just the Gamma column (all rows)
    vs restricted to just the finite/antisymmetric columns (all rows), and
    of the full Phi, on the SAME domain Ran(X) codomain split (these are
    genuinely orthogonal column-subspaces of codomain(X) by construction)."""
    Phi = res['Phi']
    co = res['col_off']
    full_norm = float(np.linalg.norm(Phi, 2))
    gamma_only = Phi[:, co[0]:co[1]]
    finite_only = Phi[:, co[1]:]
    return dict(full=full_norm,
                gamma_only=float(np.linalg.norm(gamma_only, 2)),
                finite_only=float(np.linalg.norm(finite_only, 2)),
                gamma_fro_frac=float(np.linalg.norm(gamma_only, 'fro')**2 /
                                      max(np.linalg.norm(Phi, 'fro')**2, 1e-300)))


def structural_fits(res, B):
    ns = res['ns']
    n_arr = np.array(ns, dtype=float)
    logn = np.log(n_arr)
    # finite-finite block: rows 1..end (sym_n), cols 1..end (ant_m)
    Bff = B[1:, 1:]
    gamma_col = B[1:, 0]     # ||Phi[sym_n, Gamma]||  -- wait Gamma is a col of X; there's no
    # "Gamma row" since Y has no Gamma channel. The archimedean-load question is instead:
    # compare column 'Gamma' is NOT present in row-space; the natural "how much does the
    # archimedean channel carry" question is answered by comparing row 'const' (which faces
    # the Gamma column with weight B[0,0]) against B[0,1:] (const vs ant_m) and by comparing
    # column sums / operator norms restricted to the Gamma column vs finite columns.
    const_row = B[0, :]     # const channel against {Gamma, ant_n...}

    out = dict(const_row=const_row.tolist(), col_names=res['col_names'])

    if len(ns) >= 3:
        # (i) Toeplitz-in-log test: correlate log(Bff) with |logn_i - logn_j|
        LI, LJ = np.meshgrid(logn, logn, indexing='ij')
        D = np.abs(LI - LJ)
        S = LI + LJ
        mask = Bff > 0
        y = np.log(Bff[mask])
        xT = D[mask]
        xH = S[mask]
        # simple linear fits log B = a + b*x
        def linfit(x, y):
            A = np.vstack([x, np.ones_like(x)]).T
            coef, res_, rank_, sv_ = np.linalg.lstsq(A, y, rcond=None)
            pred = A @ coef
            ss_res = np.sum((y - pred) ** 2)
            ss_tot = np.sum((y - y.mean()) ** 2)
            r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float('nan')
            return coef, r2
        coefT, r2T = linfit(xT, y)
        coefH, r2H = linfit(xH, y)
        out['toeplitz_fit'] = dict(slope=float(coefT[0]), intercept=float(coefT[1]), r2=float(r2T))
        out['hankel_fit'] = dict(slope=float(coefH[0]), intercept=float(coefH[1]), r2=float(r2H))

        # (iii) rank-one + diagonal fit of Bff
        d = np.diag(Bff).copy()
        offBff = Bff - np.diag(d)
        U, Sv, Vt = np.linalg.svd(offBff)
        rank1 = Sv[0] * np.outer(U[:, 0], Vt[0, :])
        resid = offBff - rank1
        rel_err = np.linalg.norm(resid, 'fro') / max(np.linalg.norm(offBff, 'fro'), 1e-300)
        out['rank1_plus_diag_relerr'] = float(rel_err)
        out['rank1_explained_var_frac'] = float(1 - rel_err ** 2)
        out['offdiag_fro'] = float(np.linalg.norm(offBff, 'fro'))
        out['Bff_fro'] = float(np.linalg.norm(Bff, 'fro'))
        # diagonal-suppression check: is diag(Bff) below its row neighbours?
        diag_below_neighbor = []
        for i in range(len(ns)):
            row = Bff[i].copy()
            dv = row[i]
            row[i] = -np.inf
            diag_below_neighbor.append(bool(dv < row.max()))
        out['diag_below_max_neighbor_frac'] = float(np.mean(diag_below_neighbor))
    return out


def run():
    results = {}
    for q in THRESHOLDS:
        res = build_explicit_phi(q)
        B = block_norm_matrix(res)
        print_block_matrix(res, B)
        fits = structural_fits(res, B)
        csn = channel_split_norms(res)
        print(f"  const-row block norms {res['col_names']}: "
              f"{[f'{x:.4f}' for x in fits['const_row']]}")
        print(f"  ||Phi||={csn['full']:.4f}  ||Phi[:,Gamma-col]||={csn['gamma_only']:.4f}  "
              f"||Phi[:,finite-cols]||={csn['finite_only']:.4f}  "
              f"Gamma frac of ||Phi||_F^2={csn['gamma_fro_frac']:.4f}")
        if 'toeplitz_fit' in fits:
            tf, hf = fits['toeplitz_fit'], fits['hankel_fit']
            print(f"  Toeplitz-in-log fit: log B ~ {tf['slope']:.4f}*|dlogn| + {tf['intercept']:.4f}"
                  f"  R^2={tf['r2']:.4f}")
            print(f"  Hankel-in-log   fit: log B ~ {hf['slope']:.4f}*(sumlogn) + {hf['intercept']:.4f}"
                  f"  R^2={hf['r2']:.4f}")
            print(f"  rank-1+diag fit of finite-finite block: relative Frobenius error="
                  f"{fits['rank1_plus_diag_relerr']:.4f}  (explained-variance fraction="
                  f"{fits['rank1_explained_var_frac']:.4f})  "
                  f"(||offdiag||_F={fits['offdiag_fro']:.4f}, ||Bff||_F={fits['Bff_fro']:.4f})")
            print(f"  diagonal(n=m) below max row-neighbour in {fits['diag_below_max_neighbor_frac']*100:.0f}% "
                  f"of rows (n=m entry is NOT the largest in its row)")
        results[q] = dict(B=B.tolist(), row_names=res['row_names'],
                           col_names=res['col_names'], fits=fits)
    return results


if __name__ == '__main__':
    run()
