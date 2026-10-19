import mpmath as mp
mp.mp.dps = 25
# SL2(Z) modular surface: real-analytic Eisenstein series E(z,s) constant term = y^s + phi(s) y^{1-s},
# scattering determinant  phi(s) = xi(2s-1)/xi(2s),  xi(s)=(1/2)s(s-1) pi^{-s/2} Gamma(s/2) zeta(s).
# CLAIM (Pillar 1, Route A): the zeta zeros appear as the POLES of phi (resonances of the continuous
# spectrum): poles of phi <=> zeros of xi(2s) <=> 2s=rho <=> s = rho/2 = 1/4 + i gamma/2.
def xi(s):
    return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def phi(s):
    return xi(2*s-1)/xi(2*s)

print("Route A — GL2 scattering determinant phi(s)=xi(2s-1)/xi(2s); poles should sit at s=rho/2.")
for k in range(1,5):
    g=mp.im(mp.zetazero(k))
    s_pole = mp.mpf('0.25') + 1j*g/2           # candidate resonance = zero/2
    # show |phi| blows up: evaluate slightly off the pole
    near = abs(phi(s_pole + mp.mpf('1e-6')))
    far  = abs(phi(mp.mpf('0.25') + 1j*(g/2+1)))   # away from any zero
    print(f"  zero gamma_{k}={mp.nstr(g,8):>11}: |phi| near s=1/4+i g/2 = {mp.nstr(near,6):>12} ;  |phi| off-resonance = {mp.nstr(far,6)}")
    print(f"      check xi(2s)=xi(1/2+i gamma_{k}) = {mp.nstr(xi(mp.mpf('0.5')+1j*g),4)}  (=0 => pole confirmed)")
print()
print("=> The zeta zeros ARE present in the GL2 continuous (Eisenstein) spectrum, as scattering")
print("   resonances at s = rho/2. Pillar 1 PARTIALLY met: zeros appear, but (a) as poles of a")
print("   1x1 scattering matrix on a CONTINUOUS spectrum, not a clean simple Frobenius spectrum,")
print("   and (b) the same surface also carries the CUSPIDAL (Maass) spectrum = wrong eigenvalues.")
