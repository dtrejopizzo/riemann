import mpmath as mp
mp.mp.dps = 30
def xi(s):  return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def dxi(s): return mp.diff(xi, s)

print("=== (A) Audit the scientist's formula  G_rr = (1/2) xi(rho-1)/xi'(rho-1) ===")
print("    claim: real, sign +1 on-line / -1 off-line")
for k in range(1,6):
    g=mp.im(mp.zetazero(k)); rho=mp.mpf('0.5')+1j*g
    val=mp.mpf('0.5')*xi(rho-1)/dxi(rho-1)
    print(f"  on-line gamma={mp.nstr(g,7)}: val={mp.nstr(val,6)}  (real? Im={mp.nstr(mp.im(val),3)})")
print("  => val is COMPLEX (nonzero Im) => 'sign' is ill-defined. The real-sign claim fails.")

print("\n=== (B) The derivation error: is S'(rho/2) = xi'(rho-1)/xi'(rho)? ===")
print("    phi has a POLE at s=rho/2, so phi'(rho/2) must DIVERGE, not equal a finite ratio.")
g=mp.im(mp.zetazero(1)); rho=mp.mpf('0.5')+1j*g
for eps in ['1e-3','1e-4','1e-5']:
    s=rho/2+mp.mpf(eps)
    dphi=mp.diff(lambda z: xi(2*z-1)/xi(2*z), s)
    print(f"  |phi'(rho/2 + {eps})| = {mp.nstr(abs(dphi),6)}  (blows up => S'(rho/2)=infinity)")
print(f"  claimed finite value xi'(rho-1)/xi'(rho) = {mp.nstr(abs(dxi(rho-1)/dxi(rho)),6)}  -- WRONG (phi'->inf).")

print("\n=== (C) The PROPER bilinear Krein self-norm: B = -R_rho R_rhobar/(s_rho+s_rhobar-1) ===")
print("    pairs rho with its conjugate rho-bar (the -gamma zero); this IS real. Does it detect kappa?")
def R(rho): return xi(rho-1)/(2*dxi(rho))
def Bnorm(beta,gam):
    rho=mp.mpf(beta)+1j*mp.mpf(gam); rhob=mp.mpf(beta)-1j*mp.mpf(gam)
    sr=rho/2; srb=rhob/2
    return -R(rho)*R(rhob)/(sr+srb-1)   # denominator = beta-1
print("  on-line (beta=1/2):")
for k in range(1,5):
    g=mp.im(mp.zetazero(k)); b=Bnorm('0.5',g)
    print(f"    gamma={mp.nstr(g,7)}: B={mp.nstr(b,6)}  sign={'+' if mp.re(b)>0 else '-'}")
print("  OFF-line synthetic (beta != 1/2) -- the scientist's kappa test:")
for beta in ['0.40','0.49','0.51','0.60','0.70']:
    b=Bnorm(beta,'20.5')
    print(f"    beta={beta}, gamma=20.5: B={mp.nstr(b,6)}  sign={'+' if mp.re(b)>0 else '-'}")
print("""
  B = -|R|^2/(beta-1) = |R|^2/(1-beta) > 0 for ALL beta in (0,1) -- on-line AND off-line.
  => the bilinear Krein self-norm is sign-DEFINITE throughout the strip; does NOT detect kappa.
  Same structural reason as the impossibility theorem: 1-beta>0 throughout 0<beta<1.
""")
