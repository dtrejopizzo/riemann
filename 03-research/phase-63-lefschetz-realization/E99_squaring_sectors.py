"""
E99 — the SQUARING lever: is the J-LINEAR sector of the polarization GAPPED? (Phase 63, R6).

R1: the scaling generator D=diag(2 pi n/L) (spectrum carries the zeros via H_x) ANTI-commutes with
the quaternionic J (symbol odd in n). Antilinear = wrong type for Frobenius. BUT D anti-commuting
with J means D^2 COMMUTES with J: D^2 is J-LINEAR, spectrum = gamma^2, and
    RH (gamma real)  <=>  gamma^2 >= 0  <=>  D^2 >= 0 on the right space.
So squaring moves the zeros from the antilinear sector to the J-LINEAR sector. The crossing hope:
maybe the gapless e^{-cL} cascade of the polarization (Phase 62) lives only in the ANTILINEAR/odd
directions, and the J-LINEAR/even sector — where D^2 and any Frobenius live — is GAPPED.

Decompose the space by parity P (e_n <-> e_{-n}; even=cos, odd=sin). J and D interchange/relate the
sectors. Test, for the polarization A (engine Weil form) and the V_+ form:
  (1) gap of A restricted to the EVEN (J-linear) sector vs the ODD sector — is even gapped?
  (2) is D^2 self-adjoint w.r.t. the even-sector form, and is that form positive with a GAP?
  (3) DH falsador: even sector must NOT be cleanly gapped / positive.
If the even sector is genuinely gapped for zeta and not DH => a real lead (squaring crosses sector).
If even sector is ALSO gapless => squaring does not help; wall confirmed once more. Honest either way.
"""
import os, sys, numpy as np
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices

import mpmath as mp
mp.mp.dps = 40


def to_np(M, dim):
    return np.array([[float(M[i, j]) for j in range(dim)] for i in range(dim)])


def parity_sectors(idx):
    """orthonormal even (cos) and odd (sin) combinations of e_n, e_{-n}; n=0 is even."""
    N = max(idx); cols_even = []; cols_odd = []
    dim = len(idx)
    def e(n):
        v = np.zeros(dim); v[idx.index(n)] = 1.0; return v
    cols_even.append(e(0))
    for n in range(1, N + 1):
        cols_even.append((e(n) + e(-n)) / np.sqrt(2))
        cols_odd.append((e(n) - e(-n)) / np.sqrt(2))
    return np.array(cols_even).T, np.array(cols_odd).T


def gap_report(H, label):
    ev = np.sort(np.linalg.eigvalsh((H + H.T) / 2))
    pos = ev[ev > 1e-12]
    nneg = int((ev < -1e-12).sum())
    # spectral gap = smallest |nonzero eigenvalue| relative to largest
    relgap = (pos.min() / pos.max()) if pos.size else float('nan')
    print(f"    {label}: dim={len(ev)} (pos,neg)=({len(pos)},{nneg}) "
          f"min+={pos.min() if pos.size else 0:.2e} max={pos.max() if pos.size else 0:.2f} "
          f"relgap={relgap:.2e} {'PSD' if nneg==0 else 'INDEF'}")
    return relgap, nneg


def run(lam, N, kind):
    La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40)
    dim = len(idx)
    Anp = to_np(A, dim)
    Ev, Od = parity_sectors(idx)
    print(f"\n[{kind} lam={lam} N={N}]")
    # (1) polarization A restricted to even (J-linear) vs odd sectors
    Ae = Ev.T @ Anp @ Ev
    Ao = Od.T @ Anp @ Od
    ge, ne = gap_report(Ae, "A | EVEN (J-linear)")
    go, no = gap_report(Ao, "A | ODD  (antilinear)")
    # (2) D^2 in even sector, self-adjointness wrt Ae, spectrum
    D = np.diag([2 * np.pi * n / L for n in idx])
    D2 = D @ D
    D2e = Ev.T @ D2 @ Ev
    defect = np.linalg.norm(Ae @ D2e - D2e.T @ Ae) / max(np.linalg.norm(Ae @ D2e), 1e-30)
    print(f"    D^2|even self-adj defect wrt A|even = {defect:.2e}  "
          f"(D^2 is J-linear: spectrum ~ gamma^2 >=0 <=> RH)")
    return ge, ne, go, no


if __name__ == '__main__':
    grid = [(11.0, 18), (15.0, 20), (21.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E99 — squaring lever: is the J-LINEAR (even) sector of the polarization GAPPED?")
    for kind in ('zeta', 'DH'):
        for lam, N in grid:
            run(lam, N, kind)
