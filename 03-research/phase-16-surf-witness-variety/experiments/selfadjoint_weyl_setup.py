import mpmath as mp
mp.mp.dps = 25
def xi(s): return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def xilog(s): return mp.diff(lambda z: mp.log(xi(z)), s)

# TARGET: a self-adjoint operator H with Weyl/m-function m(z) such that the poles of m are the
# zeta zeros gamma_rho (real <=> RH).  Candidate Weyl function (rotated to the spectral variable z,
# s = 1/2 + i z so that sigma>1/2 <-> Im z>0):
#   m(z) := (1/i) * xi'/xi(1/2 + i z).
# Then: Herglotz in Im z>0 (Re xi'/xi>0 in sigma>1/2) <=> m maps upper half-plane to upper half-plane
#       <=> m is the Weyl function of a SELF-ADJOINT operator (de Branges / Krein).
def m(z): return (1/1j)*xilog(mp.mpf('0.5')+1j*z)

print("=== Candidate Weyl function m(z) = (1/i) xi'/xi(1/2+iz):  poles at z=gamma_rho, real <=> RH ===")
print("    Nevanlinna/Herglotz test: Im m(z) >= 0 for Im z>0  <=>  m is a self-adjoint Weyl function.")
for z in [1+1j, 5+0.5j, 14+0.3j, 20+1j]:
    z=mp.mpc(z); v=m(z)
    print(f"  z={z}:  m={mp.nstr(v,6)}   Im m={mp.nstr(mp.im(v),5)}  ({'>=0 OK' if mp.im(v)>=-1e-9 else '<0'})")
print("    (Im m = Re xi'/xi(sigma+i tau)/1 with sigma=1/2+Im z>1/2: positive in range = RH holds here.)")

print("""
=== The construction, precisely ===
  m(z)=(1/i)xi'/xi(1/2+iz) is a real-on-vertical-lines meromorphic function with:
   - poles exactly at z=gamma_rho (the zeta zeros, in the z-variable);
   - residues +1 at each pole (xi'/xi has residue +1 at each zero);
   - Im m = 0 on the REAL z-axis (the unconditional boundary identity, P23 Thm) -- the spectral axis.
  By the Nevanlinna/Krein-de Branges theorem, m is the Weyl m-function of a SELF-ADJOINT operator
  (equivalently a canonical system dY/dx = z J H(x) Y, H(x)>=0) IF AND ONLY IF Im m(z)>=0 for Im z>0,
  i.e. IF AND ONLY IF the poles {gamma_rho} are REAL <=> RH.

  Two routes to build the operator:
   (A) INVERSE spectral (from the zeros): build the canonical system H(x) from the measure
       sum_rho delta_{gamma_rho} via Krein/Gelfand-Levitan. CIRCULAR: assumes the gamma_rho real.
   (B) FORWARD (from the primes): build the operator from the explicit formula (Phase-4 operator
       T = Omega(D)+Pi-2 sum Lambda(n)/sqrt n Re T_{log n}); its Weyl function is m. Self-adjoint
       realization EXISTS (von Neumann, Phase-4 B-1); REAL spectrum / semibounded = Phase-4 B-2 = RH.

  => Constructing the operator NON-circularly = route (B) = Phase-4 Problem B = B-2 (semiboundedness)
     = the relative-form-bound / uniform pair-correlation input = the program's frontier (RH-conditional
     or sub-RH). The Herglotz framing adds the clean boundary identity (Im m=0 on the axis) but the
     interior positivity (Im m>=0) is exactly RH.
""")
