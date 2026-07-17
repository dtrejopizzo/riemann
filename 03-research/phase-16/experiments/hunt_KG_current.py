import mpmath as mp
mp.mp.dps = 30
# Klein-Gordon / symplectic current of two Eisenstein modes f=y^{1-s_rho}, g=y^{1-s_sigma}
# on a Cauchy surface y=const (Lorentzian SO(1,1) invariant pairing):
#   j = i ( conj(f) d/dy g - g d/dy conj(f) ) integrated over x  =>  amplitude (conj(s_rho)-s_sigma)
# DIAGONAL KG self-norm: amplitude = i*(conj(s_rho)-s_rho) = i*(-2i Im s_rho) = 2 Im(s_rho) = gamma_rho
print("=== Klein-Gordon current self-norm of the resonance modes (Lorentzian SO(1,1)) ===")
print("    KG-norm(rho) proportional to i*(conj(s_rho)-s_rho) = 2 Im(s_rho) = gamma_rho")
print("    -> depends ONLY on gamma (=Im), NOT on beta (=Re). Test off-line sensitivity:\n")
def kg_norm(beta,gam):
    s=(mp.mpf(beta)+1j*mp.mpf(gam))/2          # resonance s=rho/2
    return mp.re(1j*(mp.conj(s)-s))            # = Im part contribution = gamma/2 ... beta-independent
print("  vary beta at fixed gamma=20 (synthetic off-line test):")
for beta in ['0.30','0.40','0.50','0.60','0.70']:
    print(f"    beta={beta}: KG-norm={mp.nstr(kg_norm(beta,'20'),6)}  (sign {'+' if kg_norm(beta,'20')>0 else '-'})")
print("\n  vary gamma at fixed beta=0.5 (on-line):")
for gam in ['14.13','-14.13','21.02','-21.02']:
    print(f"    gamma={gam}: KG-norm={mp.nstr(kg_norm('0.5',gam),6)}")
print("""
RESULT (honest):
  The Klein-Gordon current self-norm is proportional to gamma (= Im s), and is COMPLETELY
  BLIND to beta (= Re s): identical for beta=0.3 and beta=0.7 at fixed gamma.
  => The Lorentzian SO(1,1) pairing detects upper/lower (gamma sign = conjugate symmetry),
     NOT on/off-line (beta = 1/2). It does NOT detect kappa.
  Across ALL natural Eisenstein pairings -- Petersson (definite, ~1-beta), bilinear Krein
  (~1/(1-beta)), Klein-Gordon current (~gamma, beta-blind) -- NONE produces the off-line
  detector (beta - 1/2). The Lorentzian lead does not rescue it.
""")
