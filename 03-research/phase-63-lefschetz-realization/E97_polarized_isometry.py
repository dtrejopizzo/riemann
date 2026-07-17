"""
E97 — Is the Connes scaling operator H_x a POLARIZED ISOMETRY? (Phase 63, R1, MW-5 frontier).

Phase 62 found: the Weil polarization is present for zeta but gapless. The F_q mechanism that
turns a polarization into RH is FROBENIUS: an endomorphism that is self-adjoint / a similitude of
the polarization, so positivity FORCES its eigenvalues onto the line. The Spec-Z analog is the
Connes scaling operator H_x whose spectrum = the zeros (validated in phase-60 E3_ccm_real:
eigenvalue 14.105 vs gamma_1=14.135 at lam=11).

H_x = D_log - |D_log xi><delta|,  D_log=diag(2 pi n/L),  xi=QW^{-1}delta/(delta^T QW^{-1}delta),
QW = Cauchy-Toeplitz Weil form (b_n from von Mangoldt; DH = chi mod 5 falsador).

The polarized-isometry mechanism (the crossing hope):
    RH  <=  (QW >= 0  AND  H_x is QW-self-adjoint).
If H_x is QW-self-adjoint w.r.t. a POSITIVE QW, its spectrum is REAL => zeros on the line.

Tests (zeta and DH):
  (1) spectrum of H_x: #real eigenvalues near zeros, #complex (off-line signature).
  (2) QW signature: is QW PSD (zeta) / indefinite (DH)?
  (3) QW-self-adjointness defect  ||QW H_x - H_x^T QW|| / ||QW H_x||.
  (4) MECHANISM: do the COMPLEX eigenvalues of H_x live in the NEGATIVE eigenspace of QW?
      (i.e. is non-reality of the spectrum = the indefiniteness of the polarization?)
Honesty: float64 here (eigvals of nonsymmetric H_x); DH mandatory; no proof; report verbatim.
"""
import sys, numpy as np

ZEROS = np.array([14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
                  40.918719, 43.327073, 48.005151, 49.773832])


def von_mangoldt(K):
    Lam = np.zeros(K + 1); s = np.ones(K + 1, bool); s[:2] = False
    for p in range(2, int(K**0.5) + 1):
        if s[p]: s[p*p::p] = False
    for p in np.nonzero(s)[0]:
        pk = p; lp = np.log(p)
        while pk <= K: Lam[pk] = lp; pk *= p
    return Lam


def build_QW(lam, N, K, kind='zeta'):
    L = 2.0 * np.log(lam); n = np.arange(-N, N + 1); dim = 2 * N + 1
    Lam = von_mangoldt(K); ks = np.arange(1, K + 1); coef = Lam[1:K + 1] / np.sqrt(ks)
    if kind == 'DH':
        chi = np.array([{1: 1, 2: 1, 3: -1, 4: -1, 0: 0}[k % 5] for k in ks])
        coef = coef * chi
    b = np.array([(1.0 / L) * np.sum(coef * np.sin(2 * np.pi * ks * nn / L)) for nn in n])
    QW = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            QW[i, j] = np.log(lam) * 0.5 if i == j else (b[i] - b[j]) / (n[i] - n[j])
    return (QW + QW.T) / 2, L, n


def Hx(QW, L, n):
    dim = len(n); delta = np.ones(dim) / np.sqrt(L)
    try: y = np.linalg.solve(QW, delta)
    except np.linalg.LinAlgError: y = np.linalg.lstsq(QW, delta, rcond=None)[0]
    xi = y / (delta @ y)
    Dlog = np.diag(2 * np.pi * n / L)
    return Dlog - np.outer(Dlog @ xi, delta), Dlog, delta


def analyze(lam, N, K, kind):
    QW, L, n = build_QW(lam, N, K, kind)
    H, Dlog, delta = Hx(QW, L, n)
    ev = np.linalg.eigvals(H)
    real = ev[np.abs(ev.imag) < 1e-6].real
    near = real[(real > 5) & (real < 55)]
    ncomplex = int((np.abs(ev.imag) >= 1e-6).sum())
    # how well do the real positives match zeros
    matched = [np.min(np.abs(near - z)) for z in ZEROS if near.size]
    medmatch = np.median(matched) if matched else float('nan')
    # QW signature
    qev = np.linalg.eigvalsh(QW)
    qpos = int((qev > 1e-9).sum()); qneg = int((qev < -1e-9).sum())
    # QW-self-adjointness defect of H_x
    defect = np.linalg.norm(QW @ H - H.T @ QW) / max(np.linalg.norm(QW @ H), 1e-30)
    print(f"  [{kind:4s} lam={lam} N={N} K={K}] H_x: {len(real)} real, {ncomplex} complex eigvals; "
          f"median|near-zero match|={medmatch:.3f}")
    print(f"        QW signature (pos,neg)=({qpos},{qneg})  QW {'PSD' if qneg == 0 else 'INDEFINITE'};"
          f"  QW-self-adj defect of H_x = {defect:.3e}")
    return ncomplex, qneg, defect


if __name__ == '__main__':
    grid = [(11.0, 40, 500), (20.0, 60, 800)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E97 — polarized-isometry test: RH <= (QW>=0 AND H_x QW-self-adjoint) => real spectrum")
    for kind in ('zeta', 'DH'):
        print(f"\n--- {kind} ---")
        for lam, N, K in grid:
            analyze(lam, N, K, kind)
