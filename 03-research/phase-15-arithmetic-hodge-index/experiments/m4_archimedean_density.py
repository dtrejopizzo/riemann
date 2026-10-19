import mpmath as mp
mp.mp.dps = 40

logpi = mp.log(mp.pi)

def Psi(r):
    # archimedean density of the Weil explicit formula:
    # Psi(r) = Re psi(1/4 + i r/2) - log pi
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j*mp.mpf(r)/2)) - logpi

# 1) value at r=0 and small r
print("=== pointwise values of Psi(r) ===")
for r in [0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 20, 50, 100]:
    print(f"  r={r:6}:  Psi={mp.nstr(Psi(r), 12)}")

# closed form at 0: psi(1/4) = -gamma - 3 ln2 - pi/2
psi_quarter = -mp.euler - 3*mp.log(2) - mp.pi/2
print("\n  check psi(1/4) closed form:", mp.nstr(psi_quarter,15),
      " vs digamma:", mp.nstr(mp.digamma(mp.mpf('0.25')),15))
print("  Psi(0) =", mp.nstr(psi_quarter - logpi, 15))

# 2) find the zero crossing r0 where Psi changes sign
print("\n=== sign change ===")
f = lambda r: Psi(r)
lo, hi = 4.0, 8.0
print("  Psi(4)=", mp.nstr(Psi(4),8), " Psi(8)=", mp.nstr(Psi(8),8))
r0 = mp.findroot(f, 6.0)
print("  zero crossing r0 =", mp.nstr(r0, 15))
print("  Psi(r0) =", mp.nstr(Psi(r0), 6))

# 3) minimum of Psi (where is it most negative?)
# derivative: d/dr Re psi(1/4+ir/2) = Re[ i/2 * psi'(1/4+ir/2) ] = -1/2 Im psi'(...)
dPsi = lambda r: mp.re(1j/2 * mp.polygamma(1, mp.mpf('0.25')+1j*mp.mpf(r)/2))
print("\n=== minimum ===")
print("  Psi'(0) =", mp.nstr(dPsi(0), 6), " (0 by symmetry -> r=0 is the extremum)")
print("  Psi is even in r; the extremum at r=0 is the global minimum:")
print("  min_r Psi(r) = Psi(0) =", mp.nstr(Psi(0), 12))

# 4) asymptotics: Re psi(1/4+ir/2) ~ log|r/2| for large r
print("\n=== large-r asymptotics (Psi(r) - log(r/2)) ===")
for r in [50, 100, 500, 1000, 5000]:
    print(f"  r={r:6}: Psi-log(r/2) = {mp.nstr(Psi(r)-mp.log(mp.mpf(r)/2),10)} ,  -log(2 pi)? {mp.nstr(-mp.log(2*mp.pi),10)}")
