"""
E108 — Krein-Langer negative-square index (Connes round 3): the sharp RH index.

Connes: the right index is NOT mu_max=1 (boundary norm-one) but the KREIN-LANGER negative-square
count of the interior kernel:
   ind_-(K_S) = #{poles of S in C_+}  (counted with multiplicity),
and for the shifted scattering S=Theta_omega, UHP poles are exactly off-line zeros rho=beta+i gamma
with beta-1/2 > omega. So
   RH  <=>  ind_-(K_{Theta_omega}) = 0  for all omega>0.
This is strictly stronger than boundary edge contractivity (mu_max=1) -- it SEES the interior
off-line spectrum, invisible to boundary modulus.

Geometry (planted off-line zero at beta, ordinate gamma0; factors at beta±i gamma0 and (1-beta)±i gamma0):
  Theta_omega gets UHP poles at  z = ±gamma0 + i(beta-1/2-omega)   (the beta±i gamma0 zeros),
  i.e. 2 UHP poles once omega < beta-1/2  (the (1-beta) partners give LHP poles, don't count).
So a single planted off-line beta contributes ind_- = 2 (sampling near both ±gamma0).

Test (dps=40): count NEGATIVE eigenvalues of the Pick/Gram matrix of Theta_omega.
  (1) zeta: ind_- = 0 for any omega (RH-consistent).
  (2) k planted off-line zeros: ind_- = 2k once omega < min(beta)-1/2, with points sampling the poles.
Honesty: this is the faithful theorem-level detector; ind_-=0 for zeta is RH (still a criterion).
"""
import mpmath as mp
mp.mp.dps = 40


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def offfac(s, betas):
    f = mp.mpf(1)
    for (b, g0) in betas:
        for s0 in (mp.mpf(b)+1j*mp.mpf(g0), mp.mpf(b)-1j*mp.mpf(g0),
                   (1-mp.mpf(b))+1j*mp.mpf(g0), (1-mp.mpf(b))-1j*mp.mpf(g0)):
            f *= (s - s0)
    return f


def Theta(omega, z, betas=None):
    sp = mp.mpf('0.5')+omega+1j*z; sm = mp.mpf('0.5')+omega-1j*z
    n, d = xi(sp), xi(sm)
    if betas: n *= offfac(sp, betas); d *= offfac(sm, betas)
    return n/d


def neg_squares(omega, pts, betas=None, tol=1e-12):
    n = len(pts); Th = [Theta(omega, z, betas) for z in pts]
    R = mp.zeros(2*n)
    for i in range(n):
        for j in range(n):
            v = (1 - Th[i]*mp.conj(Th[j]))/(2*mp.pi*1j*(mp.conj(pts[j])-pts[i]))
            re, im = mp.re(v), mp.im(v)
            R[i, j] = re; R[n+i, n+j] = re; R[i, n+j] = -im; R[n+i, j] = im
    R = (R+R.T)/2
    E, _ = mp.eigsy(R)
    ev = sorted(float(E[k]) for k in range(2*n))
    mx = max(abs(x) for x in ev)
    # Hermitian neg-squares = (#negative real-embedding eigenvalues)/2
    nneg = sum(1 for x in ev if x < -tol*mx) // 2
    return nneg, ev[0]/mx


if __name__ == '__main__':
    print("E108 — Krein-Langer negative-square index of K_{Theta_omega} (Connes round 3).")
    print("  ind_- = #UHP poles = #off-line zeros (sampled). RH <=> ind_-=0 for all omega.\n")
    omega = mp.mpf('0.1')

    # (1) zeta: sample broadly; expect ind_-=0
    ptsz = [mp.mpf(g)+1j*mp.mpf(y) for g in (14,21,25,30,37) for y in ('0.3','0.8')]
    nz, r = neg_squares(omega, ptsz)
    print(f"(1) zeta (omega={float(omega)}, 10 pts): ind_- = {nz}   (expect 0)   rel min eig={r:+.2e}")

    # (2) planted off-line zeros: sample NEAR each pole at (±gamma0, beta-1/2-omega)
    print("\n(2) planted off-line zeros (sample near the UHP poles at ±gamma0):")
    for betas in ([(0.80, 20.0)], [(0.80, 20.0), (0.75, 33.0)], [(0.80, 20.0), (0.75, 33.0), (0.85, 45.0)]):
        pts = []
        for (b, g0) in betas:
            h = b - 0.5 - float(omega)   # pole height
            for g in (g0, -g0):
                for dy in (0.6, 1.0, 1.5):
                    pts.append(mp.mpf(g) + 1j*mp.mpf(h*dy))
        nneg, r = neg_squares(omega, pts, betas=betas)
        print(f"   {len(betas)} off-line zero(s) beta={[b for b,_ in betas]}: ind_- = {nneg}  "
              f"(expect {2*len(betas)})  {'MATCH' if nneg == 2*len(betas) else 'mismatch'}")
