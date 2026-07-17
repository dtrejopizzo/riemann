"""
PASO DECISIVO hacia la prueba analitica de 2.3.F-Loc.

REFORMULACION: los ratios (k+1)^2 NO dependen de toda la oscilacion del multiplicador de Doob
C_lambda, solo de sus MODOS DE FOURIER BAJOS en la coordenada portadora theta. Por perturbacion
a 1er orden en el marco portador (G = -d^2/dtheta^2 con C=c(1+eta)):
   delta(e_k)/e_k ~ <eta> + (1/2) eta_hat(2(k+1)),
asi que el ratio e_k/e_1 solo ve eta_hat(2j), j pequeno (el promedio <eta> se cancela).

=> 2.3.F-Loc' (lo que hay que probar): eta_hat(2j) -> 0 (j=1,2,3) cuando lambda->inf, EN MEDIA.
Esto es MUCHO mas debil que "eta->0 puntual" (N3, que se queda plano por la fluctuacion
aritmetica de alta frecuencia). Aqui medimos los modos BAJOS, que es lo unico que controla
los ratios. Si decaen aunque el std puntual no -> 2.3.F-Loc probado en el sentido que importa.

Comparamos:  std puntual de eta  (N3, esperado plano)  vs  |eta_hat(2j)| j=1,2,3 (esperado: decae?).
Falsador DH (debe NO decaer / ser grande).
"""
import sys, numpy as np, mpmath as mp
from engine_cache import doob_spectrum, recon_grid, extract_C

NTH = 2000  # grilla en theta


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

    # coordenada portadora theta(y) desde u0 ~ sin(theta): theta = arccos via f1/u0 = 2 cos theta
    ct = np.full_like(u0, np.nan)
    safe = np.abs(u0) > 1e-9 * a0
    ct[safe] = np.clip(0.5 * f1[safe] / u0[safe], -1.0, 1.0)
    th = np.arccos(ct)  # in [0,pi]

    # bulk: donde C es finito y u0 no esta en nodo
    inner = (np.abs(u0) > 0.30 * a0) & np.isfinite(C) & np.isfinite(th)
    thb = th[inner]; Cb = C[inner]
    # ordenar por theta y quedarnos con rango monotono
    srt = np.argsort(thb)
    thb, Cb = thb[srt], Cb[srt]
    # eta = C/mean - 1
    cmean = np.mean(Cb)
    eta = Cb / cmean - 1.0
    return thb, eta, L


def low_fourier(thb, eta, jmax=3):
    """coeficientes eta_hat(2j) = (2/pi) int_0^pi eta(theta) cos(2 j theta) dtheta, via interp uniforme."""
    # interpolar a grilla uniforme en [thb.min, thb.max] reescalada a [0,pi]
    t0, t1 = thb.min(), thb.max()
    tu = np.linspace(t0, t1, NTH)
    eu = np.interp(tu, thb, eta)
    # reescalar el intervalo bulk a [0,pi] (Dirichlet del bulk)
    s = (tu - t0) / (t1 - t0) * np.pi
    out = []
    for j in range(1, jmax + 1):
        cj = np.trapz(eu * np.cos(2 * j * s), s) * (2.0 / np.pi)
        out.append(cj)
    std = np.std(eu)
    return out, std


def run(lams, kind='zeta'):
    print(f"\n{'='*72}\nkind={kind}: modos de Fourier bajos del multiplicador vs std puntual")
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
        print(f"  TASA std(eta) puntual ~ L^-{rate([r[2] for r in rows]):.2f}  (N3: esperado ~plano)")
        for j in range(3):
            p = rate([abs(r[3][j]) for r in rows])
            print(f"  TASA |hat(2*{j+1})|     ~ L^-{p:+.2f}  {'<<< DECAE (controla el ratio!)' if p > 0.4 else '(no decae claro)'}")
    return rows


if __name__ == '__main__':
    lams = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    run(lams, 'zeta')
    run([(7.0, 14)], 'DH')
