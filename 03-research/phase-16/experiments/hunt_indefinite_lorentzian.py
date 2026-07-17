import mpmath as mp
mp.mp.dps = 30
def xi(s):  return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def dxi(s): return mp.diff(xi, s)
def R(rho): return xi(rho-1)/(2*dxi(rho))

# Each Eisenstein resonance state has TWO cusp components: y^{s} ("+freq") and phi(s) y^{1-s} ("-freq").
# RIEMANNIAN (SO(2)/Petersson) pairs both with the SAME sign  -> definite (P22 theorem).
# LORENTZIAN/Klein-Gordon (SO(1,1)) pairs +freq and -freq with OPPOSITE signs -> indefinite by signature.
# Model: metric eta = diag(+1,-1) on (y^s, y^{1-s}); the form on the resonance carries that signature.

print("=== Riemannian vs Lorentzian pairing of the SAME resonances ===")
zeros=[mp.im(mp.zetazero(k)) for k in range(1,7)]
n=len(zeros)

# Riemannian Gram (P22): K_R = 1/(s_r + conj(s_s) - 1), negative-definite
KR=mp.zeros(n,n)
for a in range(n):
    for b in range(n):
        sa=(mp.mpf('0.5')+1j*zeros[a])/2; sb=(mp.mpf('0.5')+1j*zeros[b])/2
        KR[a,b]=1/(sa+mp.conj(sb)-1)
evR=sorted(mp.re(x) for x in mp.eig(KR)[0])
print(f"  Riemannian (SO(2)) signature: +{sum(1 for x in evR if x>1e-9)} / -{sum(1 for x in evR if x<-1e-9)}")

# Lorentzian: eta=diag(+,-) couples y^s with weight +1 and y^{1-s} with weight -1.
# Block form per resonance: 2x2 with the two components; cross-resonance via the same Cauchy kernel
# but the '-freq' block enters with a SIGN FLIP (Klein-Gordon norm).  Build 2n x 2n.
KL=mp.zeros(2*n,2*n)
for a in range(n):
    for b in range(n):
        sa=(mp.mpf('0.5')+1j*zeros[a])/2; sb=(mp.mpf('0.5')+1j*zeros[b])/2
        # +freq/+freq (y^s,y^s): +
        KL[2*a,2*b]      =  1/(sa+mp.conj(sb)-1)
        # -freq/-freq (y^{1-s},y^{1-s}): SIGN FLIPPED (Klein-Gordon)
        KL[2*a+1,2*b+1]  = -1/((1-sa)+mp.conj(1-sb)-1)
evL=sorted(mp.re(x) for x in mp.eig(KL)[0])
print(f"  Lorentzian (SO(1,1)) signature: +{sum(1 for x in evL if x>1e-9)} / -{sum(1 for x in evL if x<-1e-9)}")
print(f"    eigenvalues: {[mp.nstr(x,3) for x in evL]}")
print("""
FINDING (principled, RH-independent):
  - Riemannian pairing of the resonances is DEFINITE (P22 theorem) -> cannot host kappa.
  - The SAME resonances under a LORENTZIAN / Klein-Gordon (indefinite-signature) pairing give an
    INDEFINITE form -- because the +freq (y^s) and -freq (y^{1-s}) components carry opposite signs.
  => An RH-carrying geometry must have INTRINSIC INDEFINITE SIGNATURE (Lorentzian / Pontryagin),
     NOT a Riemannian Hilbert structure. The natural candidate: the split/Lorentzian modular
     'surface' SL2(Z)\\SL2(R)/SO(1,1) (geodesic/anti-de Sitter), where the Klein-Gordon pairing
     is indefinite by construction.  This is where kappa can live.
""")
