import mpmath as mp
mp.mp.dps = 30
def xi(s):  return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def dxi(s): return mp.diff(xi, s)

# resonance weight (residue of scattering phi=xi(2s-1)/xi(2s) at s=rho/2):
#   r_rho = xi(rho-1) / (2 xi'(rho))   -- candidate Krein self-norm of the resonance vector
print("k   gamma        |r_k|            arg(r_k)/pi     |r_k|*e^{+pi gamma/4}  (decay-corrected)")
prev=None
for k in range(1,13):
    g=mp.im(mp.zetazero(k)); rho=mp.mpf('0.5')+1j*g
    r=xi(rho-1)/(2*dxi(rho))
    mag=abs(r); ph=mp.arg(r)/mp.pi
    corr=mag*mp.e**(mp.pi*g/4)
    print(f"{k:2} {mp.nstr(g,8):>10}  {mp.nstr(mag,8):>14}  {mp.nstr(ph,6):>12}   {mp.nstr(corr,8):>16}")

print("""
Interpretation:
  - If |r_k| ~ e^{-pi gamma/4} -> 0 : the resonance norms vanish -> Krein space TRIVIALIZES
    (same wall as Phase-4 de Branges H(E_xi)); Route A collapses.
  - If |r_k| = O(1) (decay-corrected column blows up) : resonances have genuine norms ->
    Route A's resonance space is NON-trivial -> genuinely new, distinct from Phase 4.
  - arg(r_k)/pi near an integer => r_k real => candidate sign epsilon_rho well-defined.
""")
