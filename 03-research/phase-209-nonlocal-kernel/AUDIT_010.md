# AUDIT_010 — Spectral moment needed to compress D_n

2026-10-19. Independent check. LINK_010_SPECTRAL_REGULARITY read.
**Verdict: PROVED the lower bound and the exclusion of the class with finite spectral moment s. General unitary compression of D_n OPEN. Target D active.**

## 1. Corpus and new question

Targeted search in the index for regularity, spectral moments, fractional domains and continuity; review of LINK009 and of module007, besides the already recorded distinction with the non-interpolation of Paper44. This moment condition is not identified in the consulted entries. That does not declare global priority.

The difference of class is written: D_n is kept unnormalised, compression WITHOUT semigroup law is allowed and an explicit hypothesis on the spectral measure of JA is added. The obstruction for V_n is not illegitimately transferred nor are values at all rationals used as if already fixed.

## 2. Increments of the finite observable

Let S be the prime support of A and L even, divisible by all those primes. With n=1+kL and m=n+L:

- n and m are coprime to each prime of S.
- gcd(n,m)=gcd(n,L)=1.
- Dividing N by n or m does not change the valuations of S, so D_nA=X_nA and D_mA=X_mA.

Independence of the valuations gives

    E_s|D_nA−D_mA|²
      =a[n^(−s)+m^(−s)−2(nm)^(−s)], a=E_s|A|²>0.

The identity is also valid for complex A, because the cross product contains |A|². The Gaussian component of the distance is nonnegative. With h=log(m/n), nh→L and m/n→1, while n^s(nm)^(−s)=m^(−s)→0. Thus the announced lower limit is exactly ≥2κa/L^s>0.

No extra Gaussian regularity is needed. As an optional stronger control, its contribution divided by h^s tends to zero: from 007, ||TD_nA||≤n^(−(s+1)/2)sqrt(Π(A)), and analogously for m. Hence the full normalised distance actually has limit 2κa/L^s. The written liminf version is sufficient and correct.

## 3. Compression and spectral theorem

For fixed bounded maps P,J and C₀ unitary U(t)=exp(itB),

    ||D_mA−D_nA||≤||P||·||(U(h)−I)JA||.

Only unitarity and the law of the ambient GROUP are used. A semigroup law for the compressions or P=J* is not presupposed. Equality at n=1 forces PJ=I in a realisation, but the argument does not need to exploit it.

If ∫|λ|^s dμ_A<∞, for 0<s<2 one has

    |exp(ihλ)−1|²/|h|^s≤4|λ|^s.

The quotient tends to zero for each λ because 2−s>0. Dominated convergence gives ||(U(h)−I)JA||²/|h|^s→0, contradicting the positive lower limit. All exponents and the domination constant are correct.

The equivalence with JA∉Dom(|B|^(s/2)) has the exact order: the square of the norm of |B|^(s/2) contains |λ|^s. At α=1/4 the absolute moment 1/2 is required and Dom(|B|^(1/4)) is excluded, not Dom(|B|^(1/2)) as equivalent.

## 4. What remains open

The necessary condition is strong: EACH nonzero algebraic observable must have an image with infinite moment s in a hypothetical compression. It does not prove that such a compression is impossible. Strong continuity only requires the differences to tend to zero without a rate; it allows the irregular behaviour needed here.

Nor has it been proved that the smooth tests of Q_T, under a link not yet built, must correspond to some of those images JA with finite spectral regularity. That implication requires an explicit map and domain. The result cannot be used as a barrier for all realisations of Q_T.

**Necessary condition approved. General compression OPEN; no form or trace of Q_T constructed.**
