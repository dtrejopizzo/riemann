"""
PASO DECISIVO RH-neutralidad: ¿la FORMA (ratios (k+1)^2 + modos de Fourier bajos pequenos) esta
fijada por la estructura SUAVE/PNT, o necesita la fluctuacion fina de primos (los ceros)?

Descomposicion (explicit formula / PNT mean field):
  PRIME_mn = sum_{n<=lam^2} Lambda(n) n^{-1/2} q(log n)
           ~ PNT ~ int_1^{lam^2} t^{-1/2} q(log t) dt = int_0^L e^{u/2} q(u) du =: PRIME_smooth_mn
  PRIME - PRIME_smooth = fluctuacion de CEROS (Weil).
Construyo A_smooth = ARCH - PRIME_smooth (SUAVE, sin primos/ceros), Doob-conjugo por su estado
base, extraigo C_smooth y sus modos de Fourier bajos. Comparo con el operador VERDADERO.

LECTURA:
  - si A_smooth da escalera (k+1)^2 + modos bajos pequenos como el verdadero
        => la FORMA es RH-NEUTRAL (la fija el balance suave/PNT; los primos solo anaden ruido
           de alta frecuencia que promedia). 2.3.F-Loc' demostrable via PNT.  CERRABLE.
  - si A_smooth NO da la escalera (ratios rotos / estado base no positivo)
        => los primos finos (ceros) son esenciales para la forma = wall-adjacent.
"""
import sys, numpy as np, mpmath as mp
from engine_cache import get_matrices, doob_spectrum, recon_grid, extract_C

mp.mp.dps = 40
# q_func y parts_entry ya quedan definidos al importar engine_cache (exec de E70)
import engine_cache as EC


def prime_smooth_matrix(idx, L):
    """PRIME_smooth_mn = int_0^L e^{u/2} q_mn(u) du   (mean-field PNT de la suma de von Mangoldt)."""
    dim = len(idx)
    M = mp.zeros(dim)
    Lm = mp.mpf(L)
    for a in range(dim):
        for b in range(a, dim):
            q = EC.q_func(idx[a], idx[b], Lm)
            val = mp.quad(lambda u: mp.e ** (u / 2) * q(u), [0, Lm])
            M[a, b] = val; M[b, a] = val
    return M


def low_fourier_of_operator(A, idx, L, label):
    """Doob-conjuga A por su estado base, extrae C(theta) y modos de Fourier bajos. Robusto."""
    dim = len(idx)
    E, V = mp.eigsy(A)
    order = sorted(range(dim), key=lambda j: float(E[j]))
    eps = [float(E[order[k]]) for k in range(min(6, dim))]
    ratios = [eps[k] / eps[0] for k in range(min(6, dim))]

    def gm(k):
        c = np.array([float(V[i, order[k]]) for i in range(dim)])
        return recon_grid(c, idx, L)
    ys, u0 = gm(0)
    pos = np.mean(u0 > 0)
    if u0[len(ys) // 2] < 0:
        u0 = -u0
    ground_positive = (np.min(u0) > -1e-6 * np.max(np.abs(u0)))  # estado base no cambia de signo?
    _, f1 = gm(1)
    a0 = np.max(np.abs(u0)); w = u0 ** 2
    e1 = eps[1] - eps[0]
    v1 = np.where(np.abs(u0) > 1e-9 * a0, f1 / np.where(np.abs(u0) > 1e-12, u0, 1e-12), 0.0)
    C = extract_C(ys, w, v1, e1, None)
    ct = np.full_like(u0, np.nan); safe = np.abs(u0) > 1e-9 * a0
    ct[safe] = np.clip(0.5 * f1[safe] / u0[safe], -1.0, 1.0)
    th = np.arccos(ct)
    inner = (np.abs(u0) > 0.30 * a0) & np.isfinite(C) & np.isfinite(th)
    thb = th[inner]; Cb = C[inner]
    srt = np.argsort(thb); thb, Cb = thb[srt], Cb[srt]
    eta = Cb / np.mean(Cb) - 1.0
    t0, t1 = thb.min(), thb.max()
    tu = np.linspace(t0, t1, 2000); eu = np.interp(tu, thb, eta)
    s = (tu - t0) / (t1 - t0) * np.pi
    cj = [abs(np.trapz(eu * np.cos(2 * j * s), s) * 2 / np.pi) for j in (1, 2, 3)]
    print(f"  [{label}] eps0={eps[0]:+.3e}  estado_base_positivo={ground_positive}  "
          f"ratios={[round(r,3) for r in ratios]}")
    print(f"           modos Fourier bajos |hat(2,4,6)| = {[round(x,4) for x in cj]}  (target ~0)")
    return ratios, cj, ground_positive


def run(lam, N):
    print(f"\n{'='*72}\nlam={lam} N={N}")
    Larch, Lpr, A_true, L, idx = get_matrices(lam, N, 'zeta', dps=40)
    # operador verdadero
    low_fourier_of_operator(A_true, idx, L, "VERDADERO  ARCH-PRIME")
    # operador PNT-suave
    Psm = prime_smooth_matrix(idx, L)
    A_smooth = Larch - Psm
    low_fourier_of_operator(A_smooth, idx, L, "PNT-SUAVE  ARCH-PRIME_smooth")
    # cuanto difiere el prime suave del verdadero (norma relativa)
    diff = mp.mpf(0); tot = mp.mpf(0)
    for a in range(len(idx)):
        for b in range(len(idx)):
            diff += abs(Lpr[a, b] - Psm[a, b]); tot += abs(Lpr[a, b])
    print(f"  ||PRIME - PRIME_smooth|| / ||PRIME|| = {float(diff/tot):.3f}  (fluctuacion de ceros)")


if __name__ == '__main__':
    lams = [(7.0, 14), (11.0, 18), (15.0, 20)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    print("E84 — RH-neutralidad de la FORMA: operador verdadero vs PNT-suave (sin primos/ceros)")
    for lam, N in lams:
        run(lam, N)
