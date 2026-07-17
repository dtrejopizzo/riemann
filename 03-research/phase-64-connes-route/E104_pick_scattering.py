"""
E104 — Connes' Section 7 test: Pick-matrix passivity of the SHIFTED scattering family.

Theta_omega(z) = xi(1/2+omega+iz) / xi(1/2+omega-iz),  omega>0.
On the real z-axis |Theta_omega|=1 (inner boundary). In the UHP:
  - pole of Theta_omega at z = -gamma + i(beta-1/2-omega) for a zero rho=beta+i gamma.
  - on-line (beta=1/2): pole at Im z = -omega < 0 (LHP) for all omega>0 => Schur down to omega=0.
  - off-line (beta>1/2): pole crosses into the UHP once omega < beta-1/2 => Schur FAILS there.
So passivity of Theta_omega as omega \downarrow 0 is RH. The PICK MATRIX
  P_ij = (1 - Theta(z_i) conj(Theta(z_j))) / (2 pi i (conj(z_j) - z_i)),  z_i in UHP,
is PSD  <=>  Theta is Schur/inner (interior passivity; STRONGER than edge/boundary contractivity:
it sees interior poles). Test min eig of P as omega decreases, for zeta and a planted-off-line-zero
falsifier (DH-type: functional equation kept, off-line zeros added).

Prediction (Connes): zeta Pick-PSD down to omega=0 (marginal); falsifier fails at omega ~ beta-1/2.
Honesty: mpmath dps=30; this validates the criterion + its falsifiability, NOT a proof of RH.
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 30


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_off(s, betas):
    """plant off-line zeros: multiply xi by factors giving zeros at b+i g0 and the functional-eq /
    conjugate partners (keeps xi(s)=xi(1-s) and reality). betas = list of (beta, gamma0)."""
    f = xi(s)
    for (b, g0) in betas:
        for s0 in (mp.mpf(b) + 1j * mp.mpf(g0), mp.mpf(b) - 1j * mp.mpf(g0),
                   (1 - mp.mpf(b)) + 1j * mp.mpf(g0), (1 - mp.mpf(b)) - 1j * mp.mpf(g0)):
            f = f * (s - s0)
    return f


def Theta(xifun, omega, z):
    a = mp.mpf('0.5') + mp.mpf(omega) + 1j * z
    b = mp.mpf('0.5') + mp.mpf(omega) - 1j * z
    return xifun(a) / xifun(b)


def pick_mineig(xifun, omega, pts):
    n = len(pts)
    Th = [Theta(xifun, omega, z) for z in pts]
    P = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(n):
            num = 1 - Th[i] * mp.conj(Th[j])
            den = 2 * mp.pi * 1j * (mp.conj(pts[j]) - pts[i])
            P[i, j] = complex(num / den)
    P = (P + P.conj().T) / 2
    return float(np.linalg.eigvalsh(P).min())


if __name__ == '__main__':
    # test points in the UHP, spread over the first ~10 zero ordinates
    pts = [mp.mpf(x) + 1j * mp.mpf(y) for x in (6, 12, 18, 24, 30, 36, 42) for y in ('0.5', '1.5')]
    omegas = [1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.01]

    print("E104 — Pick-matrix passivity of Theta_omega (Connes Sec.7). PSD <=> Schur/inner (sees poles).")
    print(f"  {len(pts)} test points in UHP; min eig of Pick matrix (>=0 => passive):\n")

    print("(1) zeta:  expect Pick-PSD down to omega=0 (marginal)")
    print(f"   {'omega':>7} {'min eig Pick':>16}")
    for om in omegas:
        me = pick_mineig(xi, om, pts)
        print(f"   {om:7.2f} {me:16.3e}  {'PSD' if me > -1e-9 else 'FAILS (pole in UHP)'}")

    print("\n(2) falsifier: planted off-line zeros at beta=0.80 (gamma0=20) -> expect FAIL for omega<0.30")
    betas = [(0.80, 20.0)]
    xio = lambda s: xi_off(s, betas)
    print(f"   {'omega':>7} {'min eig Pick':>16}")
    for om in omegas:
        me = pick_mineig(xio, om, pts)
        print(f"   {om:7.2f} {me:16.3e}  {'PSD' if me > -1e-9 else 'FAILS (off-line pole in UHP)'}")
    print("\n  predicted threshold: off-line pole enters UHP at omega = beta-1/2 = 0.30.")
