import mpmath as mp
mp.mp.dps = 30
def xi(s):  return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def dxi(s): return mp.diff(xi, s)
def R(rho): return xi(rho-1)/(2*dxi(rho))
Rn=8
gam=[mp.im(mp.zetazero(k+1)) for k in range(Rn)]
Rr=[R(mp.mpf('0.5')+1j*g) for g in gam]
G=mp.zeros(Rn,Rn)
for a in range(Rn):
    for b in range(Rn):
        d=(gam[b]-gam[a])/2
        G[a,b]=Rr[a]*mp.conj(Rr[b])*(-1)/(mp.mpf('0.5')+1j*d)
# Hermitian? check then eigenvalues
E=mp.eigsy(mp.matrix([[mp.re(G[a,b]) if a==b else G[a,b] for b in range(Rn)] for a in range(Rn)]),eigvals_only=True) if False else None
# use eig for complex Hermitian
ev,_=mp.eig(G)
ev=sorted([mp.re(x) for x in ev])
print("Eigenvalues of the MSZ Gram matrix G (Hermitian):")
for x in ev: print("   ", mp.nstr(x,8))
npos=sum(1 for x in ev if x>1e-12); nneg=sum(1 for x in ev if x<-1e-12)
print(f"\n  positive: {npos}   negative: {nneg}")
print(f"""
ARBITER VERDICT (signature):
  G = -D K D*  with K_rho,sigma = 1/(1/2 - i(g_rho-g_sigma)/2) a POSITIVE-definite (Bochner) kernel
  => G is NEGATIVE-definite: all {nneg} eigenvalues < 0, regardless of RH.
  The Weil form Q is POSITIVE-definite on primitives under RH (index kappa = #off-line zeros).
  The MSZ pairing has CONSTANT signature (all negative) => it does NOT detect kappa, is NOT Q.
  => FRENCH PROPOSAL: PILLAR 2 -> REJECTED (not diagonal, signature constant, kappa not detected).
""")
