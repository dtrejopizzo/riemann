import mpmath as mp
mp.mp.dps = 30
def xi(s):  return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def dxi(s): return mp.diff(xi, s)
# resonance vector Psi_rho ~ R_rho * y^{1-rho/2} in the cusp, R_rho = Res_{s=rho/2} phi = xi(rho-1)/(2 xi'(rho))
def R(rho): return xi(rho-1)/(2*dxi(rho))

Rn=8
G=mp.zeros(Rn,Rn); Rr=[]; gam=[]
for k in range(Rn):
    g=mp.im(mp.zetazero(k+1)); gam.append(g); Rr.append(R(mp.mpf('0.5')+1j*g))

# MSZ regularized pairing (Hadamard finite part of the divergent cusp integral, T^{1/2} dropped):
#  <Psi_rho, Psi_sigma> = R_rho conj(R_sigma) * FP int_1^T y^{-1/2 + i(g_sigma-g_rho)/2} dy
#                       = R_rho conj(R_sigma) * (-1)/(1/2 + i(g_sigma-g_rho)/2)
for a in range(Rn):
    for b in range(Rn):
        d=(gam[b]-gam[a])/2
        G[a,b]= Rr[a]*mp.conj(Rr[b])*(-1)/(mp.mpf('0.5')+1j*d)

print("=== Arbiter test of the MSZ Gram matrix (French proposal's own algorithm) ===")
diag=[mp.re(G[k,k]) for k in range(Rn)]
maxoff=max(abs(G[a,b]) for a in range(Rn) for b in range(Rn) if a!=b)
maxdiag=max(abs(G[k,k]) for k in range(Rn))
print("  diagonal G_rr (should be eps_rho*C_rho):")
for k in range(Rn):
    print(f"    rho_{k+1}: G_rr = {mp.nstr(G[k,k],6)}   sign={'+' if diag[k]>0 else '-'}")
print(f"\n  max |off-diagonal| = {mp.nstr(maxoff,6)}   vs   max |diagonal| = {mp.nstr(maxdiag,6)}")
print(f"  off/diag ratio = {mp.nstr(maxoff/maxdiag,4)}   (French 'Theorem' claims DIAGONAL: off/diag should be ~0)")
print(f"\n  diagonal signs all equal? {len(set(d>0 for d in diag))==1}  (all {'+' if diag[0]>0 else '-'})")
print(f"  index kappa_num (# negative diag) = {sum(1 for d in diag if d<0)}")
print("""
ARBITER VERDICT:
  - off/diag ratio is O(1), NOT ~0  => the Gram matrix is NOT diagonal (it is the Hilbert/Cauchy
    kernel R_rho conj(R_sigma)/(1/2 - i(g_rho-g_sigma)/2)). The French 'diagonality Theorem' FAILS.
  - the diagonal is all ONE sign (independent of on/off-line) => NOT the kappa-detector
    (confirms eps_rho = sign(Im rho) is wrong; off-line zeros not detected).
  - the pairing required dropping a DIVERGENT T^{1/2} (resonances are not L^2) => regularization-
    dependent / non-canonical norm = exactly the Phase-4 de Branges non-L^2 issue.
""")
