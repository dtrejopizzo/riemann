"""
R11 / angulo NUEVO: la escalera (k+1)^2 como LEY DE WEYL 1D del operador Sturm-Liouville de Doob.

Hecho robusto (clasico): para -(C v')' con peso w y Dirichlet en [a,b], los ratios de autovalores
bajos -> m^2 (Weyl) para CUALQUIER C positivo acotado (0 < c- <= C <= c+). NO hace falta C->const,
solo ELIPTICIDAD UNIFORME. Y C_lambda >= 0 esta PROBADO (positividad de G_lambda, R1).

Tests:
  (W1) Reconstruir el operador SL 1D  L v = -(1/w)(C w v')'  con el C_lambda y w MEDIDOS (engine),
       Dirichlet en el bulk; resolver. ¿ratios -> m^2 = (k+1)^2? Si SI: la escalera ES la ley de
       Weyl del operador medido (no hay contenido oculto mas alla de C,w).
  (W2) ELIPTICIDAD: min y max de C_lambda/<C_lambda> en el bulk vs lambda. ¿min acotado lejos de 0
       uniformemente? Si SI: la unica hipotesis que falta es RH-neutral (elipticidad), y por Weyl
       la escalera se sigue. Si min->0: el operador degenera (posible reconexion al muro).
  (W3) prediccion de homogeneizacion: media armonica C_h=(<1/C>)^{-1} y longitud optica
       T=int sqrt(w/C) -> autoval Weyl m^2 pi^2 / T^2 (escala) y ratios m^2.
Falsador DH.
"""
import sys, numpy as np, mpmath as mp
from engine_cache import doob_spectrum, recon_grid, extract_C


def sl_eigs(yb, Cb, wb, nmodes=6):
    """autovalores de L v = -(1/w) d/dy(C w dv/dy) con Dirichlet en los extremos del bulk."""
    n = len(yb); dy = yb[1] - yb[0]
    # C,w en medios puntos
    Cm = 0.5 * (Cb[1:] + Cb[:-1]); wm = 0.5 * (wb[1:] + wb[:-1])
    a = Cm * wm  # flujo en i+1/2
    # operador interior (Dirichlet: nodos 1..n-2 libres, 0 y n-1 = 0)
    N = n - 2
    L = np.zeros((N, N))
    for k in range(N):
        i = k + 1
        diag = (a[i - 1] + a[i]) / (dy * dy * wb[i])
        L[k, k] = diag
        if k > 0:
            L[k, k - 1] = -a[i - 1] / (dy * dy * wb[i])
        if k < N - 1:
            L[k, k + 1] = -a[i] / (dy * dy * wb[i])
    ev = np.linalg.eigvals(L)
    ev = np.sort(ev[np.isreal(ev)].real)
    ev = ev[ev > 0]
    return ev[:nmodes]


def run(lam, N, kind='zeta'):
    d = doob_spectrum(lam, N, kind, dps=40, nlow=4)
    V, order, idx, L, dim = d['V'], d['order'], d['idx'], d['L'], d['dim']

    def gm(k):
        c = np.array([float(V[i, order[k]]) for i in range(dim)])
        return recon_grid(c, idx, L)
    ys, u0 = gm(0)
    if u0[len(ys) // 2] < 0:
        u0 = -u0
    _, f1 = gm(1)
    a0 = np.max(np.abs(u0)); w = u0 ** 2
    e1 = float(d['eps'][1] - d['eps'][0])
    v1 = np.where(np.abs(u0) > 1e-9 * a0, f1 / np.where(np.abs(u0) > 1e-12, u0, 1e-12), 0.0)
    C = extract_C(ys, w, v1, None, None) if False else extract_C(ys, w, v1, e1, None)

    inner = (np.abs(u0) > 0.30 * a0) & np.isfinite(C) & (C > 0)
    # bulk contiguo
    idxs = np.where(inner)[0]
    if len(idxs) < 8:
        print(f"  lam={lam}: bulk corto"); return
    lo, hi = idxs.min(), idxs.max()
    sl = slice(lo, hi + 1)
    yb, Cb, wb = ys[sl], C[sl], w[sl]
    # limpiar nan/neg en Cb por interpolacion
    bad = ~np.isfinite(Cb) | (Cb <= 0)
    if bad.any():
        good = ~bad
        Cb = np.interp(yb, yb[good], Cb[good])
    cmean = np.mean(Cb)
    cmin, cmax = np.min(Cb) / cmean, np.max(Cb) / cmean

    # (W1) Weyl: ratios del SL reconstruido
    ev = sl_eigs(yb, Cb, wb)
    ratios = [ev[k] / ev[0] for k in range(len(ev))] if len(ev) >= 2 else []
    # true ratios
    true_r = [float(d['eps'][k] - d['eps'][0]) / e1 for k in range(1, 4)]  # (e_k)/(e_1), target k(k+2)? no
    true_abs = [float(d['ratios'][k]) for k in range(min(6, len(d['ratios'])))]

    print(f"\n{kind} lam={lam} L={L:.2f}")
    print(f"  (W1) SL reconstruido (C,w medidos) ratios lambda_m/lambda_1 = "
          f"{[round(r,3) for r in ratios]}  target m^2=1,4,9,16,25")
    print(f"       (escalera VERDADERA eps_k/eps_0 = {[round(r,3) for r in true_abs]})")
    print(f"  (W2) ELIPTICIDAD: C/<C> in bulk  min={cmin:.3f}  max={cmax:.3f}  "
          f"=> {'ELIPTICO (acotado lejos de 0)' if cmin > 0.15 else 'DEGENERA (min->0)'}")
    return cmin, cmax, ratios


if __name__ == '__main__':
    lams = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    print("E86 — escalera (k+1)^2 = ley de Weyl 1D del operador SL de Doob (C,w medidos)")
    res = []
    for lam, N in lams:
        r = run(lam, N, 'zeta')
        if r:
            res.append((lam, r[0]))
    print("\nELIPTICIDAD min(C/<C>) vs lambda:", [(l, round(c, 3)) for l, c in res])
    print("\nFALSADOR DH:")
    run(7.0, 14, 'DH')
