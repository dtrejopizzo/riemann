# AUDIT_008 — Ambient inversion, adjoint and graph domain

2026-10-19. Independent check. CONSTRUCTOR_008 read in full.
**Verdict: PROVED lemmas1–4 with elementary proofs included. Closability and invariance of the module OPEN. Full D active.**

## 1. Corpus and change of object

The unitary inversion of a weighted L² is standard and is not a new source of sign. The new reason of the memo is to compute its EXACT conjugation on G_n of the already built kernel −R, with its non-homogeneous measure, and to audit the concrete completion. This does not reopen the sector/carrier mirrors of phase199 nor introduce a new abstract norm of Q_T. The memo correctly keeps these distinctions.

## 2. Ambient involution and defect

The density of a unitary inversion satisfies

    a(y)²=ρ(1/y)/(y²ρ(y))=y^(−2α)τ(1/y)/τ(y).

Hence the formula for U is correct; a(y)a(1/y)=1, its norm is preserved and U is self-adjoint involutive. For α=1/4, the factor y^(−1/4) cancels exactly with the root of the √y of Poisson, producing sqrt((1−m(y))/τ(y)). The denominator is not eliminated nor is U identified with an operation on the arithmetic component.

The direct conjugation gives the coefficient

    n^(−α) sqrt[τ(n²/y)τ(y/n²)/(τ(1/y)τ(y))].

This is b_n(y) times G_n*, with b_n²=r(y/n²)/r(y). The product M_bG_n* makes sense on the whole image G_n*(L_α): the formula coincides pointwise with the bounded operator U G_n U. It is not necessary for M_b alone to be bounded; no such claim is made.

For h(x)=logτ(e^x), the already approved strict concavity gives that h(x)+h(−x) is even and strictly decreasing in |x|. The comparison of |log y−2log n| with |log y| correctly proves b_n<1 for y<n, =1 for y=n and >1 for y>n. The defect changes orientation. Only the naive equality U G_n U=G_n* for THIS ambient inversion is excluded; no NO-GO is claimed for other realisations or involutions.

## 3. The closure is not automatically a graph

The closure of the image A↦(√κ A,TA) in a Hilbert product exists, but this does not prove injectivity of its first projection. The presence of vertical components and the closability of T are questions distinct from the existence of that closure. The memo does not assume either of them resolved.

Although P_s and the Gaussian probabilities on integers have very different measurable supports, that observation alone does not prove non-closability of an operator that integrates in y with a singular weight. A sequence with appropriate convergence or a complete argument on the domain of the adjoint is needed. None is presented without proof.

## 4. The sequence of primorial exclusions

Each A_L is a finite Haar-centred divisibility polynomial. The formula for its arithmetic norm is exact:

    E_s|A_L|²=δ_{s,L}−2δ_Lδ_{s,L}+δ_L²→0,

since 0≤δ_{s,L}≤δ_L→0. For fixed y, the Gaussian sum is dominated and the indicator of integers without primes ≤L converges to 1_{|N|=1}. Thus T A_L→2e^(−πy)/τ(y) pointwise. This limit belongs to L_α: it is O(√y) at zero and tends to 1 at infinity, where τ decreases exponentially.

The pointwise convergence is NOT strong in L_α. For y∈[1/L,2/L], every allowed positive integer except 1 exceeds L. The tail is uniformly O(L exp(−cL)); Poisson gives τ(y) comparable to √L. Thus the mean of the indicator is O(L^(−1/2)). The elementary bound δ_L≥e^(−2)/(1+log²L) implies |TA_L|≥δ_L/2 on that interval for large L. Integrating the density produces

    ||TA_L||²≥c_α δ_L² L^(1/2−α)→∞.

The final proof does not need Mertens. To verify its elementary bound, write P_L(t)=Π_{p≤L}(1−p^(−t))^(−1), ε=1/log²L. The logarithmic series gives

    log[P_L(1)/P_L(1+ε)]≤εΣ_{p≤L}log p/(p−1)
       ≤ε log L (1+log L)<2  (L≥3).

Moreover P_L(1+ε)≤ζ(1+ε)≤1+1/ε by integral comparison. Thus δ_L=P_L(1)^(−1)≥e^(−2)/(1+log²L). On the other hand P_L(1) contains the harmonic sum of n≤floor(L), hence δ_L≤1/H_floor(L)→0. Both bounds and their directions are correct; they suffice for all the convergences and divergences used. The divergence only rules out THIS sequence as a vertical strong-limit argument. It neither proves closability nor prevents other sequences.

## 5. Final scope

The three ambient formulas and the diagnosis of the sequence are approved. It was not proved that U preserves the closed image of 007, nor an intertwining with a compensating arithmetic operation, nor a trace or form on all tests of Q_T. The ambient adjoint must not be imported to the module without reducibility or computation of the corresponding compression.

**Domain auxiliary resolved within the written scope; closability/invariance and Q_T link OPEN. Target D not met.**
