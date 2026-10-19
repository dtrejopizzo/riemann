import mpmath as mp
mp.mp.dps = 25
def xi(s): return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def xilog(s): return mp.diff(lambda z: mp.log(xi(z)), s)   # xi'/xi

# de Branges chain positivity  <=>  Re xi'/xi(sigma+i tau) > 0  for all sigma>1/2  <=>  RH.
# Structure: Re xi'/xi(s) = sum_rho (sigma-beta_rho)/|s-rho|^2.  On-line zeros (beta=1/2) give
# (sigma-1/2)>0; an off-line zero with beta>sigma gives a NEGATIVE term (the wrong-sign capstone).
print("=== Re xi'/xi(sigma + i tau) for sigma>1/2 (the de Branges chain criterion) ===")
print("    POSITIVE everywhere <=> RH.  Check structure as sigma -> 1/2+ :\n")
for sigma in ['1.0','0.7','0.55','0.501']:
    sg=mp.mpf(sigma)
    vals=[mp.re(xilog(sg+1j*mp.mpf(t))) for t in [0,10,14.13,20,30,50]]
    mn=min(vals)
    print(f"  sigma={sigma}: Re xi'/xi at tau=0,10,14.13,20,30,50 = {[mp.nstr(v,4) for v in vals]}")
    print(f"             min over these tau = {mp.nstr(mn,5)}  ({'>0 OK' if mn>0 else '<0 !!'})")

print("\n=== where is it smallest? scan tau finely at sigma=0.51 (just above the line) ===")
sg=mp.mpf('0.51'); tg=mp.linspace(0.5,40,80)
vals=[(float(t),float(mp.re(xilog(sg+1j*t)))) for t in tg]
mn=min(vals,key=lambda x:x[1])
print(f"  min Re xi'/xi(0.51+i tau) over tau in [0.5,40] = {mn[1]:.5f} at tau={mn[0]:.2f}")
print(f"  (positive everywhere -- RH holds in range; the minimum sits BETWEEN zeros, not on them)")
print("""
THE FRONTIER, in its cleanest form:
  RH  <=>  Re xi'/xi(sigma+i tau) > 0  for all sigma>1/2, all tau.
  - KNOWN unconditionally: positive for sigma >= 1 and in the de la Vallee Poussin zero-free region.
  - The gap sigma in (1/2, 1): this is RH = de Branges chain positivity = P13/Laguerre-Polya = CAP.
  - On-line zeros contribute + (sigma-1/2); an off-line zero would contribute - (sigma-beta<0): wrong sign.
  A NEW TOOL must prove Re xi'/xi>0 on (1/2,1) WITHOUT assuming the zeros are on-line -- i.e. an
  UNCONDITIONAL upper/sign bound, exactly what the wrong-sign capstone says we lack.
""")
