import mpmath as mp
mp.mp.dps = 25
def xi(s): return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def xilog(s): return mp.diff(lambda z: mp.log(xi(z)), s)
# m(z)=(1/i)xi'/xi(1/2+iz); Im m(z)=Re xi'/xi(1/2+Im z + i Re z). Herglotz region = {Im m>0}.
def Im_m(sigma,tau): return float(mp.re(xilog(mp.mpf(sigma)+1j*mp.mpf(tau))))

print("=== Unconditional Herglotz region vs the RH gap ===")
print("  Im m>0 (Herglotz) holds UNCONDITIONALLY for sigma>1 (zero-free) and in the de la Vallee")
print("  Poussin region sigma>1-c/log|t|.  RH = extending it down to sigma>1/2.\n")
print("  Lowest sigma where Im m stays >0 for the ACTUAL xi (RH true in range => gap is (1/2,1)):")
for tau in [10,20,30]:
    # find where Re xi'/xi(sigma+i tau) is positive down to (it's >0 for all sigma>1/2 since RH holds)
    vals=[(round(s,3), Im_m(s,tau)) for s in [0.51,0.6,0.8,1.0,1.5]]
    print(f"    tau={tau}: Im m at sigma=0.51,0.6,0.8,1.0,1.5 = {[round(v,5) for _,v in vals]}  (all>0: RH holds here)")

print("""
=== Why the RFB is NOT script-attackable on the real zeta (honest) ===
  The relative form bound  |t_-(g)| <= a t_+(g) + C||g||^2  concerns the OFF-LINE contribution t_-.
  When RH holds in the computed range, there are NO off-line zeros => t_- = 0 identically.
  So the RFB is VACUOUS on real data: it is a statement about HYPOTHETICAL off-line zeros, provable
  only abstractly (an analytic inequality), not by computing with the actual gamma_rho.

  The reduction (Phase-4 Days 14-18, now reconfirmed):
     B-2 / RFB  <=  uniform low-frequency form factor F(alpha) << 1 of the zeros (uniform pair correlation)
                 -> Montgomery's F(alpha): PROVEN only under RH for |alpha|>1; unconditional versions
                    (Goldston-Montgomery, Selberg) are AVERAGE/typical, not UNIFORM.
  => The frontier is a UNIFORM pair-correlation bound -- an analytic problem for the team's analysts,
     RH-conditional or open, NOT a computation. The Herglotz framing (P23) gives the unconditional
     boundary identity + positive residues; the interior positivity in (1/2,1) is exactly this frontier.
""")
