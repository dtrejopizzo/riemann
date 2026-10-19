import mpmath as mp
mp.mp.dps = 25
def xi(s): return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def phi(s): return xi(2*s-1)/xi(2*s)
def xilog(s): return mp.diff(lambda z: mp.log(xi(z)), s)      # xi'/xi
# scattering phase derivative on the line s=1/2+it (the continuous-spectrum density)
def dlogphi(t):
    s=mp.mpf('0.5')+1j*t
    return mp.diff(lambda z: mp.log(phi(z)), s)

print("=== (1) -phi'/phi on the line = -2[xi'/xi(2s-1) - xi'/xi(2s)]  (the modular-surface explicit formula) ===")
for t in [5,10,20,30]:
    s=mp.mpf('0.5')+1j*t
    direct = -dlogphi(t)
    viaxi  = -2*(xilog(2*s-1) - xilog(2*s))
    print(f"  t={t:4}: -phi'/phi (num) = {mp.nstr(direct,8)}   via xi'/xi = {mp.nstr(viaxi,8)}   match={abs(direct-viaxi)<1e-6}")

print("\n=== (2) WHERE the zeros live: resonances at s=rho/2=1/4+i gamma/2 (Re=1/4), OFF the L^2 spectrum ===")
print("    L^2 spectrum of the modular Laplacian: continuous on Re(s)=1/2 + discrete Maass (Re=1/2).")
for k in [1,2,3]:
    g=mp.im(mp.zetazero(k))
    print(f"    gamma_{k}={mp.nstr(g,8)}: resonance at s=1/4+i*{mp.nstr(g/2,7)}  -> Re(s)=0.25  (NOT 0.5)")
print("    => the zeros are NOT honest L^2 eigenvectors; they are resonances (poles of phi).")

print("\n=== (3) the density -phi'/phi is REAL and INDEFINITE in its fluctuation (Weyl term + zero oscillation) ===")
for t in [10,14.13,15,21,25]:
    s=mp.mpf('0.5')+1j*t
    val=mp.re(-dlogphi(t))
    weyl=mp.re(-2*(mp.log(mp.pi)) + 2*mp.re(mp.digamma(mp.mpf('0.5')+1j*t)))  # smooth ~ 2 log(t)-ish
    print(f"    t={t:6}: -phi'/phi = {mp.nstr(val,7):>12}   (smooth Weyl ~ {mp.nstr(weyl,6)}; fluctuation = zeros)")
