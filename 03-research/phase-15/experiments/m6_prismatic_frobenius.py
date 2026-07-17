import mpmath as mp
mp.mp.dps = 20
# What does the prismatic / crystalline Frobenius compute for zeta?
# Fact (Bhatt-Scholze): prismatic Frobenius eigenvalues on H^* = crystalline Frob eigenvalues
#   = the LOCAL Satake parameters alpha_{i,p} of the L-factor at p (good reduction).
# For zeta_Q: local factor (1-p^{-s})^{-1} => single Satake param alpha_p = 1.
# => anatomy power sums s_k(p) = sum_i alpha_{i,p}^k = 1 for ALL p,k  (P19, trivial).
print("Prismatic/crystalline Frobenius content for zeta = local Satake = P19 anatomy:")
for p in [2,3,5,7,11,13]:
    alpha = mp.mpf(1)                  # single Satake parameter for zeta
    sk = [alpha**k for k in range(1,6)]
    print(f"  p={p:3}: alpha_p=1  s_k(p)=", [int(x) for x in sk], " (Hodge-Tate weight integer, monodromy N=0: good reduction)")

print("""
=> The prismatic Frobenius eigenvalues are the LOCAL data (Satake = 1 for zeta),
   carrying an INTEGER Hodge-Tate/monodromy grading -- but that grading lives on
   the LOCAL p-adic Hodge structure (weights), and for zeta it is TRIVIAL
   (everywhere good reduction, Tate motive, nilpotent monodromy N=0).
""")

# The global zeros are a DIFFERENT object: the spectral side of the explicit formula.
# Local Frobenius (primes/Satake) and zeros are dual, related by the explicit formula,
# NOT equal. Confirm the zeros are not local Frobenius eigenvalues (they are global).
print("Global zeros (spectral side) -- NOT prismatic Frobenius eigenvalues:")
print("  first gammas:", [mp.nstr(mp.im(mp.zetazero(k)),8) for k in range(1,5)])
print("""
Verdict: prismatic cohomology supplies the integer-graded Lefschetz the dichotomy
lacked -- but LOCALLY, on the weight grading of the anatomy, where for zeta it is
trivial. It does NOT supply the GLOBAL zero-carrying cohomology over Spec Z whose
Frobenius eigenvalues are the gamma's. Assembling that = SURF/Deninger, unchanged.
""")
