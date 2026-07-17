import mpmath as mp
mp.mp.dps = 25
def xi(s): return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def xilog(s): return mp.diff(lambda z: mp.log(xi(z)), s)

print("=== Re xi'/xi(1/2 + i tau) -- is it identically 0 ON the critical line? ===")
for t in [1,5,10,14.13,20,30,50,100]:
    v=xilog(mp.mpf('0.5')+1j*mp.mpf(t))
    print(f"  tau={t:6}: xi'/xi = {mp.nstr(v,8)}   Re = {mp.nstr(mp.re(v),4)}")
print("""
  => Re xi'/xi(1/2+i tau) = 0 for ALL tau, UNCONDITIONALLY.
  PROOF (functional equation only): xi(s)=xi(1-s) => xi'/xi(s) = -xi'/xi(1-s).
  On s=1/2+i tau: 1-s = 1/2-i tau = conj(s), and xi real-coeff => xi'/xi(conj s)=conj(xi'/xi(s)).
  So xi'/xi(s) = -conj(xi'/xi(s)) => Re xi'/xi(s)=0.  No RH used.
""")

print("=== The clean criterion + the obstruction ===")
print("""  RH  <=>  Re xi'/xi(sigma+i tau) > 0  for all sigma>1/2.
  - Boundary value Re xi'/xi = 0 on sigma=1/2 is UNCONDITIONAL (above).
  - Re xi'/xi is HARMONIC in sigma>1/2 AWAY FROM ZEROS (xi'/xi meromorphic, poles at zeros).
  - IF no zeros in sigma>1/2 (RH): harmonic, =0 on boundary, ->+ at sigma=infty (Gamma factor)
    => Re xi'/xi > 0 by the minimum principle.  RH ==> positivity.
  - An OFF-LINE zero rho0 (beta0>1/2) is an INTERIOR POLE of xi'/xi: near it Re xi'/xi ~ (sigma-beta0)/|.|^2
    takes BOTH signs => positivity FAILS.  So positivity <=> no interior zeros <=> RH (clean equivalence).
  THE OBSTRUCTION (precise): the minimum principle needs NO interior poles = RH. A new tool must
  rule out interior poles using only the unconditional boundary value (=0) + behavior at infinity --
  i.e. a Phragmen-Lindelof / harmonic-measure argument that survives possible interior singularities.
  That is exactly the open core; it is the wrong-sign capstone in harmonic-function form.
""")
