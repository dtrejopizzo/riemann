"""
N2 (Fase 2.3.F-CLOSE-II) — CERTIFICADO ROBUSTO via traza de calor / zeta espectral.

Idea: los 8 atajos previos atacaron eigenvalores INDIVIDUALES (fragiles, residuo e^{-cL}).
Las SUMAS espectrales son estables. La escalera Dirichlet (k+1)^2 tiene invariantes exactos:
  - zeta espectral   Z(s) = sum_k mu_k^{-s}   ->  sum_k (k+1)^{-2s}   (mu_k = eps_k/eps_0)
  - traza de calor   Theta(t) = sum_k e^{-mu_k t}  ->  sum_k e^{-(k+1)^2 t}
Test: que Z(s)/Theta(t) del QW-Doob reproduzcan los invariantes (k+1)^2 ASINTOTICAMENTE en
lambda, y con que TASA (extrapolable en 1/L). Falsador DH debe FALLAR.

Robustez: mu_k son O(1) (1,4,9,...) a ~15 digitos aunque eps_k ~ 1e-20; la traza agrega las
desviaciones por-modo en UN numero cuya tendencia en lambda extrapolamos.
"""
import sys, mpmath as mp
from engine_cache import doob_spectrum

K = 5            # modos bajos usados (la escalera Dirichlet vive en el fondo del espectro)
SVALS = [1.0, 2.0, 3.0]
TVALS = [0.3, 0.7, 1.5]


def ideal_zeta(s, K):
    return sum((k + 1) ** (-2.0 * s) for k in range(K))


def ideal_heat(t, K):
    return sum(mp.e ** (-(k + 1) ** 2 * t) for k in range(K))


def analyze(lam, N, kind='zeta'):
    d = doob_spectrum(lam, N, kind, dps=40, nlow=K)
    mu = [float(d['ratios'][k]) for k in range(K)]     # mu_0=1, mu_1~4, ...
    L = d['L']
    ladder_err = max(abs(mu[k] - (k + 1) ** 2) / (k + 1) ** 2 for k in range(K))
    Z = {s: sum(mu[k] ** (-s) for k in range(K)) for s in SVALS}
    Zid = {s: ideal_zeta(s, K) for s in SVALS}
    zerr = {s: abs(Z[s] - Zid[s]) / Zid[s] for s in SVALS}
    Th = {t: sum(mp.e ** (-mu[k] * t) for k in range(K)) for t in TVALS}
    Thid = {t: float(ideal_heat(t, K)) for t in TVALS}
    therr = {t: abs(Th[t] - Thid[t]) / Thid[t] for t in TVALS}
    return {'lam': lam, 'L': L, 'mu': mu, 'ladder_err': ladder_err,
            'zerr': zerr, 'therr': therr, 'Z': Z, 'Zid': Zid}


def richardson(Ls, errs):
    """ajuste log(err) = log c - p*log L  -> pendiente p (tasa de decaimiento en 1/L^p)."""
    import math
    xs = [math.log(L) for L in Ls]; ys = [math.log(e) for e in errs]
    n = len(xs); sx = sum(xs); sy = sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    p = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    return -p  # err ~ L^{-p_pos}


if __name__ == '__main__':
    lams = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    print("=" * 78)
    print("N2 — zeta espectral / traza de calor. mu_k = eps_k/eps_0 -> target (k+1)^2")
    print("=" * 78)
    rows = []
    for lam, N in lams:
        r = analyze(lam, N, 'zeta')
        rows.append(r)
        print(f"\nlam={lam:>5} L={r['L']:.3f}  mu={[round(x,3) for x in r['mu']]}")
        print(f"   ladder_err(max rel)={r['ladder_err']:.4f}")
        print(f"   Z(s) err: " + "  ".join(f"s={s}:{r['zerr'][s]:.4f}" for s in SVALS))
        print(f"   Theta(t) err: " + "  ".join(f"t={t}:{r['therr'][t]:.4f}" for t in TVALS))
    # extrapolacion de tasa en 1/L de los errores agregados
    Ls = [r['L'] for r in rows]
    print("\n" + "-" * 78)
    print("TASA de decaimiento del error agregado en 1/L  (err ~ L^{-p}, p>0 => converge):")
    print(f"   ladder_err:   p = {richardson(Ls, [r['ladder_err'] for r in rows]):+.2f}")
    for s in SVALS:
        print(f"   Z(s={s}) err:  p = {richardson(Ls, [r['zerr'][s] for r in rows]):+.2f}")
    for t in TVALS:
        print(f"   Theta(t={t}) err: p = {richardson(Ls, [r['therr'][t] for r in rows]):+.2f}")
    # falsador DH
    print("\n" + "=" * 78 + "\nFALSADOR DH (debe FALLAR: ladder_err grande, no converge):")
    dh = analyze(7.0, 14, 'DH')
    print(f"   DH lam=7: mu={[round(x,3) for x in dh['mu']]}  ladder_err={dh['ladder_err']:.4f}")
    print(f"   DH Z(s) err: " + "  ".join(f"s={s}:{dh['zerr'][s]:.4f}" for s in SVALS))
