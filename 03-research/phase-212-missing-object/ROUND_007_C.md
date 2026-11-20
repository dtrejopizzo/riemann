# Round 7, item C — nonlinear relation in the weight between convolution and window

Phase notation: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real supported in
I = [−T,T], F ∈ P_T. Write F̂(ξ) = ∫F(t)e^{−iξt}dt and g_F = c_F ∗ c_F (additive convolution), so that
ĝ_F = |F̂|⁴ and supp g_F ⊂ [−4T,4T].

## 0. Four-point filter

**(1) Closest antecedent, read in primary sources.**
`phase-161-*/R161_033_COHERENT_TO_DIRECT_SUM_GAP.md` §§2, 5A, 7 (exit A: Parseval/Naimark dilation with
labels k, never built) and, above all, `R161_034_MELLIN_GRAM_AND_PRODUCT_RATIO_COLLISION.md` §0–1: the cross
Gram of the labels diagonalizes exactly in Mellin frequency and splits into same-orientation terms,
which depend on k/l, and opposite-orientation terms, which depend on kl («ratio channel» and «product
channel», already isolated in phase 106). RULES_AVOID K2, K3, L3 (BARRIER_D2_001), J2; 211
`POWER_GLOBAL_ROUTE_REVIEW.md`, «Extensión factorial antes de resonancia» (products of distinct frequencies
kept before completing squares).

**(2) Proposed object.** The dilation of exit A with the rule «the contact of mn is the composition of the
contacts of m and n», i.e. the bilinear form in the weight
Π_T(F) = Σ_{m,n} Λ(m)Λ(n)(mn)^{−1/2} g_F(log mn),
which via Λ ∗ Λ = μ ∗ log² − Λ·log returns to an expression of degree one in Λ plus a weight-independent term.

**(3) Does it avoid the difficulty of the antecedent?** No. §2 of this note proves that the product channel that sees
log m + log n = log(mn) is exactly the opposite-orientation one of R161_034 and has no sign; the channel that
has a manifest sign is the ratio one, which does not compose with divisor incidence. It is the same
product–ratio collision. **Cross-check: repetition of R161_034 / phase 106 (K2–K3).** The construction is stopped; what
follows only pins down precisely why, and the operation that would reopen it.

**(4) Connection with global positivity.** The only candidate identity would be
a_T(F) = α·Q_T(F) + R_T(F) with Q_T the ratio channel (≥ 0) and R_T the remainder; the global sign remains entirely in R_T
(pattern J2/L3). There is no connecting inequality.

## 1. The two possible compositions (PROVED)

Let a = (a_n) be real with finite support, A(ξ) = Σ_n a_n n^{−1/2} n^{iξ}. Since g_F(u) = (2π)^{−1}∫|F̂(ξ)|⁴e^{iξu}dξ:

(1.1) Σ_{m,n} a_m a_n (mn)^{−1/2} g_F(log m − log n) = (2π)^{−1}∫|F̂|⁴ |A(ξ)|² dξ ≥ 0.

(1.2) Σ_{m,n} a_m a_n (mn)^{−1/2} g_F(log m + log n) = (2π)^{−1}∫|F̂|⁴ A(ξ)² dξ = (2π)^{−1}∫|F̂|⁴ Re A(ξ)² dξ,

the last equality because F is real (|F̂|⁴ even) and A(−ξ) = conj A(ξ). Formal verification: substitute the
representation of g_F and interchange the finite sum with the integral.

(1.3) Re A² has no sign: with a supported on a single n, (1.2) equals a_n² n^{−1} g_F(2 log n), and g_F can be
negative at 2 log n (F = bump·cos(ωt) with ω·2log n ≡ π gives g_F(2 log n) < 0 for a narrow bump). Hence the
additive composition of contacts log m + log n only appears in a **holomorphic** form (A², not |A|²).

## 2. The product channel via convolution (PROVED except for the cited identity)

With a = Λ and Selberg's identity Λ·log + Λ ∗ Λ = μ ∗ log² (CITED, classical):

(2.1) Π_T(F) = Σ_k (Λ∗Λ)(k) k^{−1/2} g_F(log k) = Σ_k (μ∗log²)(k) k^{−1/2} g_F(log k) − Σ_k Λ(k) log k · k^{−1/2} g_F(log k).

Finite sum: k ≤ e^{4T}. It is exact, nonlinear in the weight (degree 2 on the left) and uses the convolution. But
by (1.2)–(1.3) the left side is ∫|F̂|⁴ Re D², with no sign. And it does not involve c_F at log n, but g_F at log k with
weight Λ·log: it does not contain a_T as a summand.

## 3. The ratio channel and the falsifiers

Q_T(F) := Σ_{m,n} Λ(m)Λ(n)(mn)^{−1/2} g_F(log(m/n)) ≥ 0 by (1.1). Any identity
a_T = αQ_T + R_T (α > 0) leaves the sign in R_T:
- **cΛ, c = 2:** Q_T(2Λ) = 4Q_T(Λ) ≥ 0 remains nonnegative; R_T(2Λ) = Arch − 2·comb − 4αQ_T. The term that
  ceases to be ≥ 0 is R_T, not Q_T: the sign mechanism is not in the new object. (ARGUED as a reading;
  the part «Q_T ≥ 0 for all c» is PROVED.)
- **Deletion of a prime power / Beurling weight:** Q_T ≥ 0 still holds (it is a square for
  every real weight); it does not distinguish. The product channel (2.1) does break (Λ'∗Λ' ≠ μ∗log² − Λ'log), but with no
  sign to lose.

Conclusion: the channel with a sign is blind to arithmetic; the arithmetic channel has no sign. It is the dichotomy of
R161_034 / phase 106, here in the form of a two-line lemma (1.1)–(1.2).

## 4. Other variants discarded in the cross-check

- Degree-two square that sums (K2, R161_030): term ½ΣΣΛ(d)Λ(e)‖m_d − m_e‖², generic in the weight.
- Quadratic divisor defect required for every weight: goal with margin (L3, BARRIER_D2_001).
- Products of distinct frequencies kept before completing squares: 211 «Extensión factorial».
- Sieve weights (Selberg Λ_R) as test: L2, they do not raise the degree.

## 5. Explicit operation that would reopen

An identity, with its own formula, expressing the product channel (2.1) **compressed to the window** (with the
boundary of [−T,T] and the restriction P_T) as a compressed ratio channel plus a boundary concomitant with a named
sign — i.e. one that converts Re D² into |D|² using Λ ∗ 1 = log and the functional equation of the archimedean
factor (the multiplier u_∞ of R161_034 (1.1), which interchanges orientations) — and whose remainder fails in
sign for c = 2 in a named term. Without that identity, the dilation of exit A contributes no mechanism.
It is the requirement of R161_034 §0 («compressed ratio channel = boundary concomitant»), not a novelty.

## 6. List of claims

| # | Claim | Label |
|---|---|---|
| 1 | (1.1): ratio channel = ∫|F̂|⁴|A|² ≥ 0 | PROVED |
| 2 | (1.2): product channel = ∫|F̂|⁴ Re A², holomorphic form | PROVED |
| 3 | (1.3): the product channel has no sign | PROVED |
| 4 | Selberg identity Λ·log + Λ∗Λ = μ∗log² | CITED |
| 5 | (2.1): exact reduction of the product channel to degree one plus a weight-free term | PROVED (given 4) |
| 6 | Q_T ≥ 0 for every real weight, including cΛ, deletion and Beurling | PROVED |
| 7 | The dilation of exit A (composed contacts of mn) falls into the product–ratio collision | NO-GO (repetition of R161_034 / phase 106, K2–K3) |
| 8 | Every identity a_T = αQ_T + R_T leaves the sign entirely in R_T | ARGUED (pattern J2/L3) |
| 9 | Reopening operation of §5 | OPEN |
