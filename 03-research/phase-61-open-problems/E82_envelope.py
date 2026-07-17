"""
Cierre N2/N3: ¿la AMPLITUD de la oscilacion aritmetica del residuo (k+1)^2 DECAE con lambda?
Si el envelope |mu_k-(k+1)^2| decae aunque oscile, la afinidad asintotica (en media) se sostiene.
Reune todos los lambda (construye los que falten, cacheados) y reporta el envelope + N1 rep_err.
"""
import mpmath as mp
from engine_cache import doob_spectrum

LAMS = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
K = 5

print("lam    L     mu_1   mu_3    |dev mu1|  |dev mu3|  ladder_err")
rows = []
for lam, N in LAMS:
    try:
        d = doob_spectrum(lam, N, 'zeta', dps=40, nlow=K)
    except Exception as e:
        print(f"{lam}: FALTA cache ({e})"); continue
    mu = [float(d['ratios'][k]) for k in range(K)]
    d1 = abs(mu[1] - 4); d3 = abs(mu[3] - 16)
    le = max(abs(mu[k] - (k + 1) ** 2) / (k + 1) ** 2 for k in range(K))
    L = d['L']
    rows.append((lam, L, mu[1], mu[3], d1, d3, le))
    print(f"{lam:>4} {L:5.2f}  {mu[1]:.3f}  {mu[3]:.3f}   {d1:.4f}    {d3:.4f}    {le:.4f}")

if len(rows) >= 4:
    import math
    Ls = [r[1] for r in rows]
    for name, idx in [("|dev mu1|", 4), ("|dev mu3|", 5), ("ladder_err", 6)]:
        ys = [math.log(max(r[idx], 1e-9)) for r in rows]
        xs = [math.log(L) for L in Ls]
        n = len(xs); sx = sum(xs); sy = sum(ys)
        sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
        p = -(n * sxy - sx * sy) / (n * sxx - sx * sx)
        print(f"  envelope {name}: ~ L^-{p:.2f}  ({'DECAE' if p>0.3 else 'PLANO/oscila'})")
