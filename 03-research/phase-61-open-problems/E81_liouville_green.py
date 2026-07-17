"""
N3 (Fase 2.3.F-CLOSE-II) — portadora theta(y) via Liouville-Green + extrapolacion de tasa 1/L.

2.3.F-Loc <=> theta(y) AFIN en y cuando lambda->inf  (f_k ~ sin((k+1)theta), u_0 ~ sin theta).
E78 mostro que las prolatas CLASICAS no sirven; aqui construimos la portadora ESPECIFICA-QW
por dos vias independientes y medimos su no-linealidad y su TASA de decaimiento en 1/L:

  (a) via MODOS medidos:   cos theta(y) = (f_1/u_0)/2     [U_1(cos t)=2cos t, Chebyshev]
  (b) via LIOUVILLE-GREEN:  theta(y) = int_0^y sqrt(w/C) dy'  (coord que aplana G a -d^2/dtheta^2)
      con w=u_0^2 y C el multiplicador MEDIDO (extract_C de E70), NO asumido.

Test: residuo de afinidad (no-linealidad de theta vs y) por lambda; ajuste residuo ~ L^{-p}
(Richardson). p>0 limpio => afinidad asintotica es LEY DERIVABLE (estilo Teorema 9.5). DH falla.
"""
import sys, numpy as np, mpmath as mp
from engine_cache import doob_spectrum, recon_grid, extract_C


def carrier_from_modes(ys, u0, f1):
    a0 = np.max(np.abs(u0))
    inner = np.abs(u0) > 0.30 * a0
    ct = np.full_like(u0, np.nan)
    safe = np.abs(u0) > 1e-9 * a0
    ct[safe] = 0.5 * f1[safe] / u0[safe]
    ct = np.clip(ct, -1.0, 1.0)
    th = np.arccos(ct)
    return th, inner


def affinity_residual(yb, thb):
    """no-linealidad de theta(y): residuo RMS del mejor ajuste lineal, normalizado al rango."""
    A = np.vstack([yb, np.ones_like(yb)]).T
    coef, *_ = np.linalg.lstsq(A, thb, rcond=None)
    fit = A @ coef
    rng = thb.max() - thb.min()
    return np.sqrt(np.mean((thb - fit) ** 2)) / (rng + 1e-300)


def run(lam, N, kind='zeta'):
    d = doob_spectrum(lam, N, kind, dps=40, nlow=4)
    V, order, idx, L = d['V'], d['order'], d['idx'], d['L']
    dim = d['dim']

    def gridmode(k):
        c = np.array([float(V[i, order[k]]) for i in range(dim)])
        return recon_grid(c, idx, L)
    ys, u0 = gridmode(0)
    if u0[len(ys) // 2] < 0:
        u0 = -u0
    _, f1 = gridmode(1)
    # alinear signo de f1 para que cos theta sea coherente
    th_m, inner = carrier_from_modes(ys, u0, f1)
    yb = ys[inner]; thb = th_m[inner]
    # ordenar monotono y limpiar nan
    m = np.isfinite(thb)
    yb, thb = yb[m], thb[m]
    res_modes = affinity_residual(yb, thb)

    # (b) Liouville-Green con C medido
    w = u0 ** 2
    e1 = float(d['eps'][1] - d['eps'][0])
    v1 = np.where(np.abs(u0) > 1e-9 * np.max(np.abs(u0)), f1 / np.where(np.abs(u0) > 1e-12, u0, 1e-12), 0.0)
    C = extract_C(ys, w, v1, e1, inner)
    ratio = np.where((np.abs(C) > 0) & np.isfinite(C), w / np.abs(C), np.nan)
    integ = np.sqrt(np.clip(ratio, 0, None))
    integ[~np.isfinite(integ)] = 0.0
    dy = ys[1] - ys[0]
    th_lg = np.concatenate([[0], np.cumsum(0.5 * (integ[1:] + integ[:-1]) * dy)])
    thb2 = th_lg[inner]; yb2 = ys[inner]
    mm = np.isfinite(thb2)
    res_lg = affinity_residual(yb2[mm], thb2[mm])

    print(f"  {kind} lam={lam:>5} L={L:.3f}: residuo afinidad theta  "
          f"modos={res_modes*100:.2f}%   Liouville-Green={res_lg*100:.2f}%")
    return {'lam': lam, 'L': L, 'res_modes': res_modes, 'res_lg': res_lg}


def rate(Ls, errs):
    import math
    xs = [math.log(L) for L in Ls]; ys = [math.log(max(e, 1e-12)) for e in errs]
    n = len(xs); sx = sum(xs); sy = sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    return -(n * sxy - sx * sy) / (n * sxx - sx * sx)


if __name__ == '__main__':
    lams = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    print("N3 — portadora theta(y): afinidad y tasa en 1/L\n" + "=" * 72)
    rows = [run(lam, N, 'zeta') for lam, N in lams]
    Ls = [r['L'] for r in rows]
    print("-" * 72)
    print(f"  TASA residuo modos       ~ L^-{rate(Ls, [r['res_modes'] for r in rows]):.2f}")
    print(f"  TASA residuo Liouville-G ~ L^-{rate(Ls, [r['res_lg'] for r in rows]):.2f}")
    print("=" * 72 + "\nFALSADOR DH (no debe aplanar / no debe seguir ley 1/L):")
    run(7.0, 14, 'DH')
