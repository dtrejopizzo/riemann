import mpmath as mp
mp.mp.dps = 30
def xi(s):  return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def dxi(s): return mp.diff(xi, s)
def resid(rho): return xi(rho-1)/(2*dxi(rho))   # residue of scattering at s=rho/2

print("=== Re(r_rho) for on-line zeros (RH true here): consistent sign? ===")
allneg=True
for k in range(1,16):
    g=mp.im(mp.zetazero(k)); rho=mp.mpf('0.5')+1j*g
    r=resid(rho); re=mp.re(r)
    allneg &= (re<0)
    print(f"  k={k:2} gamma={mp.nstr(g,7):>9}: Re(r)={mp.nstr(re,7):>11}  Im(r)={mp.nstr(mp.im(r),7):>11}")
print("  ALL Re(r_rho) < 0 :", allneg, " (consistent sign => candidate definite Krein form => RH-consistent in range)")

print("\n=== Sensitivity probe: is the sign of Re(r) tied to beta=1/2? move the test point off-line ===")
print("    (evaluate the SAME analytic weight r(s0)=xi(s0-1)/(2 xi'(s0)) at s0=beta+i*gamma_1, vary beta)")
g1=mp.im(mp.zetazero(1))
for beta in ['0.30','0.40','0.50','0.60','0.70']:
    s0=mp.mpf(beta)+1j*g1
    r=resid(s0)
    print(f"    beta={beta}: Re(r)={mp.nstr(mp.re(r),7):>11}  (sign {'-' if mp.re(r)<0 else '+'})")
print("""
    NOTE: only beta=1/2 is a true resonance (xi(2s0)=0); the others are not zeros, so this is a
    heuristic probe of the analytic weight's sign-stability, NOT a real off-line resonance.
""")
