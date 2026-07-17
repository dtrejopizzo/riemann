"""
E106 — Connes Section 1: the canonical de Branges kernel positivity (the crossing object).

E_kappa(z) = Xi'(z) - i kappa Xi(z),   Xi(z)=xi(1/2+iz),  kappa>0.
Since Xi is real on R: E_kappa^#(z) = conj(E_kappa(conj z)) = Xi'(z) + i kappa Xi(z).
de Branges reproducing kernel:
   K_kappa(z,w) = [ E_kappa(z) conj(E_kappa(w)) - E_kappa^#(z) conj(E_kappa^#(w)) ] / [2 pi i (conj(w)-z)].
Diagonal: K_kappa(z,z) = (|E_kappa(z)|^2 - |E_kappa^#(z)|^2)/(4 pi Im z), so
   K_kappa(z,z) >= 0  <=>  |E_kappa(z)| >= |E_kappa^#(z)|  (Im z>0)  <=>  E_kappa Hermite-Biehler.
Theorem (de Branges):  RH  <=>  E_kappa is HB  <=>  K_kappa is a positive (Gram) kernel.

Test (high precision, dps=40): Gram matrix [K_kappa(z_i,z_j)] over points z_i in C_+ near the zero
ordinates; min eig >= 0 ?
  (1) zeta: expect PSD (marginal -- zeta sits at the boundary).
  (2) planted off-line zero: expect FAIL (E_kappa not HB).
Honesty: faithful-but-marginal detector (RH-equivalent), NOT a proof. Confirms Connes' canonical
crossing object behaves correctly on the genuine function.
"""
import mpmath as mp
mp.mp.dps = 40


def xi(s):
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_logderiv(s):
    return 1/s + 1/(s - 1) - mp.log(mp.pi)/2 + mp.psi(0, s/2)/2 + mp.zeta(s, derivative=1)/mp.zeta(s)


def make_Xi(betas=None):
    """Xi(z)=xi(1/2+iz) and Xi'(z); optionally plant off-line zeros (keeps func. eq + reality)."""
    def polyfac(s):
        f = mp.mpf(1); df_over_f = mp.mpf(0)
        if betas:
            for (b, g0) in betas:
                for s0 in (mp.mpf(b)+1j*mp.mpf(g0), mp.mpf(b)-1j*mp.mpf(g0),
                           (1-mp.mpf(b))+1j*mp.mpf(g0), (1-mp.mpf(b))-1j*mp.mpf(g0)):
                    f *= (s - s0); df_over_f += 1/(s - s0)
        return f, df_over_f
    def Xi(z):
        s = mp.mpf('0.5') + 1j*z; f, _ = polyfac(s); return xi(s)*f
    def Xip(z):
        s = mp.mpf('0.5') + 1j*z; f, dff = polyfac(s)
        # d/dz [xi(s)f(s)] = i * (xi*f)*(xi'/xi + f'/f)
        return 1j * xi(s)*f * (xi_logderiv(s) + dff)
    return Xi, Xip


def gram_mineig(Xi, Xip, kappa, pts):
    n = len(pts)
    Ek = [Xip(z) - 1j*kappa*Xi(z) for z in pts]
    Eks = [Xip(z) + 1j*kappa*Xi(z) for z in pts]   # E^#(z) at z in C_+
    # K(z_i,z_j) = (Ek_i conj(Ek_j) - Eks_i conj(Eks_j)) / (2 pi i (conj(z_j)-z_i))
    R = mp.zeros(2*n)
    for i in range(n):
        for j in range(n):
            num = Ek[i]*mp.conj(Ek[j]) - Eks[i]*mp.conj(Eks[j])
            den = 2*mp.pi*1j*(mp.conj(pts[j]) - pts[i])
            v = num/den
            re, im = mp.re(v), mp.im(v)
            R[i, j] = re; R[n+i, n+j] = re; R[i, n+j] = -im; R[n+i, j] = im
    R = (R + R.T)/2
    E, _ = mp.eigsy(R)
    ev = [float(E[k]) for k in range(2*n)]
    return min(ev), max(ev)


if __name__ == '__main__':
    gammas = [14.134725, 21.022040, 25.010858, 30.424876]
    pts = [mp.mpf(g) + 1j*mp.mpf(y) for g in gammas for y in ('0.3', '0.8')]
    print("E106 — de Branges kernel K_kappa positivity for E_kappa=Xi'-i kappa Xi (Connes Sec.1)")
    print(f"  {len(pts)} points near zero ordinates; min eig of Gram (dps=40):\n")

    for kappa in [mp.mpf('1.0'), mp.mpf('5.0'), mp.mpf('20.0')]:
        Xi, Xip = make_Xi()
        mn, mx = gram_mineig(Xi, Xip, kappa, pts)
        print(f"  (1) zeta  kappa={float(kappa):4.0f}: min={mn:+.3e} max={mx:.3e} rel={mn/mx:+.2e}"
              f"  {'PSD' if mn > -1e-25*mx else 'NEG'}")
    print()
    for kappa in [mp.mpf('1.0'), mp.mpf('5.0')]:
        Xio, Xiop = make_Xi(betas=[(0.80, 20.0)])
        mn, mx = gram_mineig(Xio, Xiop, kappa, pts)
        print(f"  (2) off-line(beta=.8) kappa={float(kappa):4.0f}: min={mn:+.3e} max={mx:.3e}"
              f"  {'PSD' if mn > -1e-25*mx else 'FAILS (E_kappa not HB)'}")
