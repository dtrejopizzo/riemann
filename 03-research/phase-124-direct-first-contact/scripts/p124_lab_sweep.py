"""P124.014 sweep: locate the first contact of the primitive form q_T and
measure, at that window, the Tate collar (Gate R) and the prime seam (Gate S).

For a model with zeros off the critical line (xi_a, a>0) the first contact is a
GENUINE object: q_T must lose its sign at some finite T, and the null state is
computable.  The falsifier models of P122_D_SPECIFICATION section 5 have never
been run against the gate quantities before; this script does that.

Usage:
    python3 p124_lab_sweep.py --model zeta
    python3 p124_lab_sweep.py --model xi_a --a 0.3
    python3 p124_lab_sweep.py --model dh
"""
import argparse
import json
import math
import time

import numpy as np

import p124_lab as P


# ------------------------------------------------------------- gate functionals
def collar_columns(asm, bl):
    """The primitive collar columns rho_u = P_T A_T phi_u, in Z coordinates.

    By P124.005 (3.4) the Tate collar current is J_u(F) = <rho_u, F>; here it is
    computed directly from the assembled operator rather than from the closed
    form of Phi_{u,T}, so no separate normalization convention enters.
    """
    Z, Y, A = bl['Z'], bl['Y'], asm['A']
    return Z.T @ A @ Y                     # (dimP, k)


def seam_energy(asm, F):
    """Pairwise seam energies ||(E_p - E_q) h_F||^2 / log(q/p) of P122.028 (4.2).

    E_{p,T} h_F is assembled from the universal causal field of
    P3_CAUSAL_PRIMITIVE_STORAGE_IDENTITY (4.41)/(4.46):
        B_p h_F(t) = sum_{j>=0} p^{-j/2} F(t - j log p),
        E_{p,T} h = ( sqrt(1-1/p) 1_{[-T,T-log p]} B_p h ,  1_{[T-log p,T]} B_p h ).
    F is a cell-coefficient vector in the piecewise-constant basis.
    """
    c, d, T = asm['c'], asm['d'], asm['T']
    mid, wid = 0.5 * (c + d), d - c
    primes = sorted({int(n ** (1.0 / k)) if False else n
                     for n in asm['ns']
                     if all(n % m for m in range(2, int(math.isqrt(n)) + 1))})
    out = {}
    Bp = {}
    for p in primes:
        lp = math.log(p)
        vals = np.zeros_like(mid)
        j = 0
        while j * lp <= 2 * T + 1e-12:
            # value of F at t - j*log p, piecewise constant lookup
            tt = mid - j * lp
            idx = np.searchsorted(c, tt, side='right') - 1
            inside = (idx >= 0) & (idx < len(c)) & (tt >= c[np.clip(idx, 0, len(c) - 1)]) \
                     & (tt <= d[np.clip(idx, 0, len(c) - 1)])
            v = np.where(inside, F[np.clip(idx, 0, len(c) - 1)], 0.0)
            vals += p ** (-j / 2.0) * v
            j += 1
        Bp[p] = vals
    for p in primes:
        lp = math.log(p)
        s = math.sqrt(1.0 - 1.0 / p)
        mask_bulk = mid <= T - lp
        Bp[p] = np.where(mask_bulk, s * Bp[p], Bp[p])
    for i, p in enumerate(primes):
        for q in primes[i + 1:]:
            diff = Bp[p] - Bp[q]
            out[(p, q)] = float(np.sum(wid * diff ** 2) / math.log(q / p))
    return out, primes


def window_report(model, T, refine):
    asm = P.assemble(model, T, refine=refine)
    bl = P.blocks(asm)
    L, X, B = bl['L'], bl['X'], bl['B']
    wL = np.linalg.eigvalsh(L)
    rec = dict(T=T, dim=int(asm['A'].shape[0]), dimP=bl['dimP'], k=bl['k'],
               n_primes=len(asm['ns']), lam_min_L=float(wL.min()))
    if bl['k']:
        S, kern, lmin, nsmall = P.schur(L, X, B)
        wS = np.linalg.eigvalsh(S)
        full = np.block([[L, X], [X.T, B]])
        rec.update(sigma_eigs=[float(v) for v in wS],
                   sigma_min=float(wS.min()),
                   ker_proj_X=float(kern),
                   lam_min_W=float(np.linalg.eigvalsh(full).min()),
                   B_eigs=[float(v) for v in np.linalg.eigvalsh(B)])
        rho = collar_columns(asm, bl)
        v = np.linalg.eigh(L)[1][:, 0]
        Ju = rho.T @ v
        rec.update(J_on_lowest=[float(x) for x in Ju],
                   J_norm_on_lowest=float(np.linalg.norm(Ju)),
                   rho_norms=[float(np.linalg.norm(rho[:, j])) for j in range(rho.shape[1])])
    else:
        rec.update(lam_min_W=float(wL.min()))
    return asm, bl, rec


def bisect_first_contact(model, lo, hi, refine, tol=2e-3, maxit=18):
    """First T where lam_min(L_T) crosses zero, assuming >0 at lo and <0 at hi."""
    for _ in range(maxit):
        if hi - lo < tol:
            break
        mid = 0.5 * (lo + hi)
        _, _, r = window_report(model, mid, refine)
        if r['lam_min_L'] > 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="zeta", choices=["zeta", "xi_a", "dh"])
    ap.add_argument("--a", type=float, default=0.3)
    ap.add_argument("--refine", type=int, default=3)
    ap.add_argument("--tmin", type=float, default=0.70)
    ap.add_argument("--tmax", type=float, default=2.30)
    ap.add_argument("--steps", type=int, default=17)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    model = P.model_xi_a(args.a) if args.model == "xi_a" else P.MODELS[args.model]()
    print(f"model = {model.name}   refine = {args.refine}")
    print(f"{'T':>7} {'dim':>5} {'dimP':>5} {'lam_min(L)':>13} {'lam_min(W)':>13}"
          f" {'sigma_min':>13} {'||Pi_ker X||':>13} {'|J| lowest':>12}")
    rows = []
    t0 = time.time()
    for T in np.linspace(args.tmin, args.tmax, args.steps):
        _, _, r = window_report(model, float(T), args.refine)
        rows.append(r)
        print(f"{r['T']:7.4f} {r['dim']:5d} {r['dimP']:5d} {r['lam_min_L']:13.6e}"
              f" {r['lam_min_W']:13.6e} {r.get('sigma_min', float('nan')):13.6e}"
              f" {r.get('ker_proj_X', float('nan')):13.3e}"
              f" {r.get('J_norm_on_lowest', float('nan')):12.4e}")
    print(f"elapsed {time.time()-t0:.1f}s")

    neg = [r for r in rows if r['lam_min_L'] < 0]
    out = dict(model=model.name, refine=args.refine, rows=rows)
    if neg and rows[0]['lam_min_L'] > 0:
        i = rows.index(neg[0])
        lo, hi = bisect_first_contact(model, rows[i - 1]['T'], rows[i]['T'], args.refine)
        print(f"\nfirst contact of the PRIMITIVE form bracketed: T* in [{lo:.4f},{hi:.4f}]")
        asm, bl, r = window_report(model, hi, args.refine)
        L, X = bl['L'], bl['X']
        w, V = np.linalg.eigh(L)
        Fstar = V[:, 0]
        rho = collar_columns(asm, bl)
        J = rho.T @ Fstar
        Fphys = bl['Z'] @ Fstar
        gram = asm['Gram']
        nrm = math.sqrt(float(Fphys @ gram @ Fphys))
        seam, primes = seam_energy(asm, Fphys / nrm)
        print(f"  at T={hi:.4f}: lam_min(L)={w[0]:.6e}, ||F*||=1")
        print(f"  GATE R  collar J_u(F*) = {np.array2string(J, precision=6)}"
              f"   |J|={np.linalg.norm(J):.6e}")
        print(f"  GATE R  ||Pi_ker X|| = {r.get('ker_proj_X'):.6e}")
        print(f"  GATE S  seam energies ||(E_p-E_q)h||^2/log(q/p):")
        for (p, q), val in sorted(seam.items()):
            print(f"            ({p},{q}) -> {val:.6e}")
        out.update(T_star=[lo, hi],
                   gateR_J=[float(x) for x in J],
                   gateR_absJ=float(np.linalg.norm(J)),
                   gateR_ker_proj=float(r.get('ker_proj_X', float('nan'))),
                   gateS_seam={f"{p},{q}": v for (p, q), v in seam.items()})
    else:
        print("\nno sign change of the primitive form in the scanned range")

    if args.out:
        with open(args.out, "w") as f:
            json.dump(out, f, indent=1)
        print("wrote", args.out)


if __name__ == "__main__":
    main()
