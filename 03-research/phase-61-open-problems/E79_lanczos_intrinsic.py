"""
N1 (Fase 2.3.F-CLOSE-II) — JACOBI INTRINSECA del operador de Weil REAL via Lanczos.

E75/E77 perturbaron la Jacobi prolata DESNUDA de Connes (Prop 3.5) -> fallo.
E76 inyecto modos seno EXTERNOS -> error O(1) destruyo el residuo e^{-cL}.
Aqui: Lanczos EXACTO (mpmath dps>=40) sobre la matriz A de Weil (base Fourier ideal idx),
SIN base externa. Lanczos = reduccion ortogonal -> tridiagonal T (alpha_n diag, beta_n offdiag)
con espectro = espectro de A. Es la Jacobi INTRINSECA del operador real.

Pregunta-mecanismo (medida, no asumida): el ORDEN DE CRECIMIENTO de alpha_n, beta_n codifica
escalera lineal (8n+1, gaps ~const, alpha_n ~ n) vs cuadratica ((k+1)^2, alpha_n ~ n^2).
  - Connes desnudo (Prop 3.5): b_n = -8n^2-2n-3/4 + 2*pi*lam^2*(8n+1) -> DOMINA el termino lineal
    de escala 2*pi*lam^2*8n  =>  espectro lineal 8n+1.
  - QW real: ¿la Jacobi de Lanczos crece distinto (cuadratico) en el fondo confinado?
Tests: (1) Lanczos REPRODUCE el espectro e^{-cL} (estable donde E76 fallo).
       (2) crecimiento de alpha_n, beta_n (orden p).  (3) comparar con Connes desnudo. (4) DH.
"""
import sys, mpmath as mp
from engine_cache import get_matrices, doob_spectrum


def lanczos(A, q0, m):
    """Lanczos con reortogonalizacion COMPLETA (mpmath). Devuelve alpha[], beta[], Q (cols)."""
    n = A.rows
    Q = []
    q = q0 / mp.sqrt((q0.T * q0)[0])
    Q.append(q)
    alpha = []; beta = []
    qprev = mp.zeros(n, 1); b = mp.mpf(0)
    for j in range(m):
        Aq = A * Q[j]
        a = (Q[j].T * Aq)[0]
        alpha.append(a)
        r = Aq - a * Q[j] - (b * qprev if j > 0 else mp.zeros(n, 1))
        # reortogonalizacion completa (estabilidad)
        for qi in Q:
            c = (qi.T * r)[0]
            r = r - c * qi
        b = mp.sqrt((r.T * r)[0])
        if b < mp.mpf(10) ** (-mp.mp.dps + 5) or j == m - 1:
            break
        beta.append(b)
        qprev = Q[j]
        Q.append(r / b)
    return alpha, beta, Q


def jacobi_spectrum(alpha, beta):
    m = len(alpha)
    T = mp.zeros(m)
    for i in range(m):
        T[i, i] = alpha[i]
        if i < len(beta):
            T[i, i + 1] = beta[i]; T[i + 1, i] = beta[i]
    E, _ = mp.eigsy(T)
    ev = sorted(float(E[i]) for i in range(m))
    return ev


def connes_bare(lam, m):
    L2 = 2 * mp.pi * mp.mpf(lam) ** 2
    b = [-8 * n * n - 2 * n - mp.mpf(3) / 4 + L2 * (8 * n + 1) for n in range(m)]
    a = [mp.mpf(1) / 4 * mp.sqrt((4 * n + 1) * (4 * n + 2) * (4 * n + 3) * (4 * n + 4)) for n in range(m - 1)]
    return b, a


def growth_order(seq):
    """ajuste log|seq_n - seq_0| ~ p log n para n>=1 (orden de crecimiento)."""
    import math
    xs = []; ys = []
    base = seq[0]
    for n in range(2, len(seq)):
        d = abs(seq[n] - base)
        if d > 0:
            xs.append(math.log(n)); ys.append(math.log(d))
    if len(xs) < 2:
        return float('nan')
    k = len(xs); sx = sum(xs); sy = sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    return (k * sxy - sx * sy) / (k * sxx - sx * sx)


def run(lam, N, kind='zeta'):
    Larch, Lpr, A, L, idx = get_matrices(lam, N, kind, dps=40)
    n = A.rows
    # vector ciclico de AMBAS paridades (par: const 1 ; impar: rampa lineal) para alcanzar
    # la escalera COMPLETA (k+1)^2 = 1,4,9,16,25 (no solo el sub-sector par 1,9,25).
    q0 = mp.matrix([[mp.mpf(1) + mp.mpf('0.7') * (2 * i - (n - 1))] for i in range(n)])
    m = n  # Krylov completo
    alpha, beta, Q = lanczos(A, q0, m)
    ev_lan = jacobi_spectrum(alpha, beta)
    # espectro directo para verificar reproduccion
    d = doob_spectrum(lam, N, kind, dps=40, nlow=6)
    eps = [float(x) for x in d['eps'][:6]]
    ev_lo = sorted(ev_lan)[:6]
    rep_err = max(abs(ev_lo[k] - eps[k]) / (abs(eps[k]) + 1e-300) for k in range(6))
    print(f"\n{'='*72}\n{kind} lam={lam} N={N} L={L:.3f}  (dim={n}, {len(alpha)} coef Lanczos)")
    print(f"  (1) Lanczos reproduce espectro? rep_err(low6 rel)={rep_err:.2e} "
          f"=> {'SI (estable, alcanza e^-cL)' if rep_err < 1e-3 else 'NO'}")
    print(f"      ratios espectro Lanczos eps_k/eps_0 = "
          f"{[round(ev_lo[k]/ev_lo[0],3) for k in range(6)]}  target (k+1)^2")
    pa = growth_order([float(x) for x in alpha])
    pb = growth_order([float(x) for x in beta]) if len(beta) > 3 else float('nan')
    print(f"  (2) crecimiento Lanczos: alpha_n ~ n^{pa:+.2f}   beta_n ~ n^{pb:+.2f}")
    print(f"      alpha[:5]={[round(float(x),3) for x in alpha[:5]]}")
    print(f"      beta[:5] ={[round(float(x),3) for x in beta[:5]]}")
    # Connes desnudo, mismo m
    cb, ca = connes_bare(lam, len(alpha))
    pca = growth_order([float(x) for x in cb])
    print(f"  (3) Connes desnudo b_n ~ n^{pca:+.2f} (esperado ~1 lineal por escala 2pi lam^2 8n)")
    return {'rep_err': rep_err, 'pa': pa, 'pb': pb, 'ratios': [ev_lo[k]/ev_lo[0] for k in range(6)]}


if __name__ == '__main__':
    lams = [(7.0, 14), (9.0, 16), (11.0, 18)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    print("N1 — Jacobi intrinseca via Lanczos exacto sobre A de Weil")
    for lam, N in lams:
        run(lam, N, 'zeta')
    print("\n" + "=" * 72 + "\nFALSADOR DH:")
    run(7.0, 14, 'DH')
