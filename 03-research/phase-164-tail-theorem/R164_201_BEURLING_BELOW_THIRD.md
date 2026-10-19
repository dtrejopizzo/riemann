# R164_201: The discrete Beurling frontier BF_θ^disc below θ = 1/3 (Line L2, grid cell 5G)

Pure mathematics, no numerics. Sources: R164_000 §2; R163_803 (Theorem C, with the R163_891 fixes); R163_101 §5
(the analytic NO-GO); R163_102; R163_1001 Thm O.4; Paper 48 Problem 6 and thm:BFdisc. Gate 1, Row D and (★_cell) stay **OPEN**.

## Status table

| # | Statement | Label |
|---|---|---|
| 1 | Where 1/3 enters Theorem C: only in the E_p = 2 term Σ_p ε_{p,1}² p^{−2a} of Lemma 3, through the **linear** chaos γ_p = ε_{p,1}p^{−a} | PROVED (it is a reading of R163_803) |
| 2 | Lemma W: in the necklace class every rounding (independent, dependent, negatively correlated, deterministic or greedy, with any integer b_{p,1}) has \|ε_{p,1}\| ≥ ‖p^a‖ (distance to ℤ), and Σ_{p≤P}‖p^a‖²p^{−2a} ≫ P^{1−2a}/log P for a < ½ | PROVED (the first part); PROVED-CITED (the second part: equidistribution of p^c mod 1, Vinogradov, cited from memory, flagged) |
| 3 | Theorem L (lattice obstruction, power form): every system in the class 𝒦_θ with θ < 1/3 has counting error Ω(x^{θ+δ(θ)−ε}) in mean square, with δ(θ) > 0 | PROVED (by the proof in §3, audit pass done: R164_291, PROVED after R1–R2) |
| 4 | Theorem L* (full form): the error is Ω(x^{(1−θ)/2−ε}) ≥ x^{1/3} in mean square, for every rounding | ARGUED (exact gap: §3.5) |
| 5 | L2a as posed, i.e. beating 1/3 by changing the rounding of the Witt counts | **CLOSED NEGATIVE**: PROVED in power form, ARGUED in sharp form |
| 6 | 1/3 is a true threshold for the Witt-lattice construction, not an artifact of the moment method | ARGUED (PROVED as "the error exponent is > θ") |
| 7 | 1/3 is a threshold for all discrete systems | OPEN; no theorem in the record or here forces it |
| 8 | L2b first lemma: the integrality-defect inequality (§4) | PROVED inside 𝒦_θ; it does **not** give any zero information |
| 9 | Paper 48 Problem 6 for θ₀ ≤ 1/3 | OPEN; sharpening "any counterexample must lie outside 𝒦_θ" is ARGUED (rests on L\*). Theorem L shows the error exponent cannot reach θ (δ(θ) = θ(1−3θ)/(5−3θ)) but does NOT give an x^{1/3} floor |

**Decision (mandatory).** The evidence supports **neither** L2a (the construction) **nor** L2b (θ < θ₀ ⇒ RH) as posed.

- L2a fails for the reason the proposal hoped to remove. The obstruction is an L² lower bound (Bessel against the sawtooth family). It holds for **every** choice of integers, so no correlation structure among the ε can help.
- L2b gets a genuine first lemma that uses integrality. That lemma bounds the counting error **below** in terms of the rounding defect. It says nothing about where the zeros are, so it does not give RH for anything.

Net: the 1/3 barrier is real for the only construction family in the record. It is a theorem about the construction class, not about discrete systems. Problem 6 below 1/3 stays OPEN. The corollary "integrality is sign-blind for every θ > 0" is **not** obtained.

## 1. Where 1/3 enters Theorem C

Notation as in R163_803: a = θ/(1−θ), w = (s−θ)/(1−θ), X = x^{1−θ}, and ζ_𝒫(s) = ζ(w)F(w)G(w) = ζ(w)H(w), where H = Σγ_m m^{−w}. Then

  N_𝒫(x) = (1−θ)x Σ_{m≤X} γ_m/m + ζ(−a)Σ_{m≤X} γ_m m^a + x^θ T(X),  with T(X) = Σ_{m≤X} γ_m Φ(X/m).

The exponent 1/3 enters only through Σ_p p^{−2a}, the E_p = 2 term of Lemma 3. The dominant piece is the linear term T_1(X) = Σ_{p≤X} ε_{p,1}p^{−a}Φ(X/p). The higher chaos (j ≥ 2, k ≥ 2) converges for every a > 0.

So the question "artifact or threshold" is exactly this: can the integer choice b_{p,1}, and hence ε_p := b_{p,1} − p^a, make T_1(X) ≪ X^{ε} although Σ_p ε_p²p^{−2a} = ∞? Random signs cannot, since the variance is the true size. The issue is deterministic or negatively correlated choices.

**Why negative correlation looks plausible at first, and where it fails.** Greedy rounding (choose b_p so that S(y) = Σ_{p≤y}ε_p p^{−a} stays in [−1,1]) is always possible.
- It makes L(w) = Σε_p p^{−a−w} converge for Re w > 0. So the zeros of ζ(w) on Re w = ½ survive. **PROVED**, by partial summation; R, F and the higher-order part of G converge absolutely for Re w > ½ − a.
- It controls T_1 on the range p > X/J, where p ↦ Φ(X/p) has bounded variation on each of the O(J) monotonicity intervals.
- It does nothing on p ≤ X/J. There p ↦ ψ(X/p) oscillates, and the family {p ↦ ψ(X/p)}_X is too rich for one sequence to have low discrepancy against all of its members. §3 makes this precise.

## 2. The class 𝒦_θ and Lemma W

**Definition.** Fix θ ∈ (0, 1/3), so 0 < a < ½. Then 𝒦_θ(C) is the set of discrete systems whose generalized primes lie only at the points v_{p,k} = p^{k/(1−θ)}, with integer multiplicities b_{p,k} ≥ 0 and |b_{p,k} − c_{p,k}(p^a)| ≤ C. Here c_k is the Witt/necklace count of R163_803 §1.

The class contains every rounding of Theorem C: independent, dependent or deterministic, and the greedy rounding of §1. It also allows rounding to any integer within distance C, not only to the floor or the ceiling.

**Lemma W.**
- (i) In 𝒦_θ, γ_p = ε_p p^{−a} with ε_p = b_{p,1} − p^a ∈ ℤ − p^a. Hence |ε_p| ≥ ‖p^a‖.
- (ii) There is a C′ with |γ_{p^j}| ≤ C′(1+η)^j p^{−ja}.
- (iii) H(1) = Σγ_m/m converges absolutely. For every p, the local factor H_p(1) = Σ_j γ_{p^j}p^{−j} equals 1 + ε_p p^{−1−a} + O(p^{−2−2a}), uniformly over the class.
- (iv) Σ_{m≤X}|γ_m| ≪ X^{1−a+ε}.

*Proof.*
- (i) is R163_803 Lemma 1(ii), which holds verbatim for any integer b_{p,1}.
- (ii) and (iii) follow from R163_803 Lemma 1(iii), with |ε| ≤ C in place of |ε| < 1. The binomial majorant becomes (1−z^k)^{−C}, which is still a fixed series analytic in |z| < 1.
- (iv) follows from (ii) and Rankin's trick.

For the bound on Σ_{p≤P}‖p^a‖²p^{−2a}: the set {p : ‖p^a‖ ≥ ¼} ∩ [P, 2P] is a union of ≍ P^a intervals, each of length ≍ P^{1−a} > P^{1/2}. By equidistribution of p^c mod 1 for 0 < c < 1 (Vinogradov; cited from memory, FLAGGED for verification), a positive proportion of the primes in [P, 2P] have ‖p^a‖ ≥ ¼. **PROVED-CITED.** ∎

## 3. Theorem L

Work in the X-variable. Write A(X) = Σ_{n≤X} h_n for the counting function on the lattice, so that h_n is the integer mass at n^{1/(1−θ)}. Write M(X) = cX^{1+a} with c = H(1)/(1+a), and E = A − M. In the x-variable, N_𝒫(x) − ρx = E(X).

> **Theorem L.** Let θ ∈ (0, 1/3), 𝒫 ∈ 𝒦_θ(C), κ < a/(5/2+a), and Y → ∞. Then
>   (1/Y)∫_Y^{2Y}|E(X)|²dX ≫ Y^{2a}·P^{1−2a}/log P,  with P = Y^κ.
> In particular (mean square ⇒ Ω, not conversely), N_𝒫(x) − ρx is not O(x^{θ+δ}) for any δ < (1−θ)κ(½−a). The error exponent of every system in 𝒦_θ is strictly larger than θ.

*Proof.*

**3.1 The test functions.** Let φ_p(X) = ψ(X/p) and Ψ_p(X) = ∫_Y^X φ_p. Then Ψ_p = p(B({X/p}) − B({Y/p})), with B(t) = (t²−t)/2.

Integrate by parts against the step function A and the smooth function M. The boundary terms combine into E(·)Ψ_p(·) = O(p·sup|E|). This gives

  ⟨E, φ_p⟩ := ∫_Y^{2Y}Eφ_p = −p[Σ_{Y<n≤2Y} h_n B({n/p}) − ∫_Y^{2Y}M′B({X/p})dX] + O(p sup_{[Y,2Y]}|E|).

(Repair R1, R164_291.) Let R² = (1/Y)∫_Y^{2Y}|E|². By Chebyshev, |E| > 4R on a set of measure ≤ Y/16, so there are Y₁ ∈ [Y, 5Y/4] and Y₂ ∈ [7Y/4, 2Y] with |E(Y_i)| ≤ 4R. Run §§3.1–3.4 on [Y₁, Y₂] with Ψ_p based at Y₁; the boundary term is O(pR), ΔM ≍ Y^{1+a}, and the Gram estimates are unchanged. Below, "sup|E|" in the O-terms means this O(R).

**3.2 Residue distribution.** Split the masses on (Y, 2Y] into the residue classes r mod p, with fractions f_r of ΔM = M(2Y) − M(Y).
- **Class 0.** By Lemma W(iii), the density of masses with p ∤ n is (1−1/p)/H_p(1). Hence f_0 = 1/p + η_p with η_p = ε_p p^{−1−a}(1−1/p) + O(p^{−2−2a}). The error comes from the truncated Euler–Maclaurin formula for S_a^{(p)} and Lemma W(iv), and is ≪ pY^{1+ε}.
- **Nonzero classes.** These are uniform up to the twisted sums A_χ(Y) = Σ_{n≤Y}h_nχ(n) = Σ_m g_mχ(m)Σ_{d≤Y/m}d^aχ(d). By Pólya–Vinogradov and partial summation, A_χ(Y) ≪ √p log p·Y^aΣ_{m≤Y}|γ_m| ≪ p^{1/2+ε}Y^{1+ε}, using Lemma W(iv).

**3.3 The main term.** We have (1/p)Σ_r B(r/p) = −1/12 + 1/(12p²) and B(0) = 0. A direct computation gives

  Σ_r f_r B(r/p) − ∫_0^1 B = 1/(12p²) + η_p(p+1)/(12p).

Hence

  ⟨E, φ_p⟩ = −(ΔM/12)[ε_p p^{−a}(1−p^{−2}) + 1/p + O(p^{−1−2a})] + O(p^{5/2+ε}Y^{1+ε}) + O(p²Y^a) + O(p sup|E|).

Here ΔM ≍ Y^{1+a}. This is the finite-window form of Franel's identity ∫ψ(t/m)ψ(t/n) = gcd(m,n)²/(12mn) applied to E.

**3.4 Bessel.** The Gram matrix on [Y, 2Y] has entries ∫φ_pφ_q = Y/(12pq) + O(pq) and diagonal Y/12 + O(p). For P³ = o(Y) its top eigenvalue is ≤ Y/4. So

  ‖E‖² ≥ (4/Y)Σ_{p≤P}|⟨E,φ_p⟩|².

Keep only the primes with ‖p^a‖ ≥ ¼, so |ε_p| ≥ ¼ by Lemma W(i). For these, 1/p = o(p^{−a}). For p ≤ P = Y^κ with κ < a/(5/2+a), the O-terms are o(Y^{1+a}p^{−a}). Therefore

  ‖E‖²/Y ≫ Y^{2a}Σ_{p≤P,‖p^a‖≥¼}p^{−2a} ≫ Y^{2a}P^{1−2a}/log P,

by Lemma W. Finally X^a = x^θ. ∎

**3.5 Theorem L\* and the exact gap.** With P = Y^{1−ε}, the same computation gives E_rms ≫ Y^{a+(1−ε)(½−a)} = Y^{½−ε′}, which is x^{(1−θ)/2−ε′} ≥ x^{1/3}. This matches Theorem C's random upper bound max(θ, (1−θ)/2), so the barrier would be sharp.

The only missing input is that the masses h_n are equidistributed among the residues mod p with error o(Y^{1+a}p^{−1−a}) for p up to Y^{1−ε}, at least on average over p. Lemma W(iv) gives this only for p ≤ Y^{a/(5/2+a)}. A large-sieve average over the moduli would reach about Y^{1/2}, giving E_rms ≫ Y^{a+(½−a)/2}. This is ARGUED and not written out. The full range needs square-root cancellation in Σ h_nχ(n), which is close to the statement itself. Status: **ARGUED**.

## 4. L2b: the first lemma, and why it does not reach RH

**Lemma D (integrality defect inequality, PROVED in 𝒦_θ).** The proof of Theorem L gives

  mean square of (N − ρx) on [x, 2x]  ≫  x^{2θ}·[Σ_{p≤P}‖p^a‖²p^{−2a} − K],  P ≤ Y^κ,

with K an absolute constant (O(Σ_p p^{−2})); the −K is needed because the 1/p term of §3.3 can cancel ε_p p^{−a} for small p (repair R2, R164_291).

The left side is the variation of N − ρx. The right side is the integrality defect of the linear prime multiplicities. The inequality uses integrality exactly through ‖p^a‖, as R163_101 §5 requires of any such statement.

**Tests.**
- **ζ_θ (extended class).** Its masses are p^a, so ε ≡ 0 and the defect is 0. Lemma D is empty, which is consistent with N_θ = (1−θ)x + O(x^θ). Discreteness alone excludes ζ_θ, but Lemma D does not use the zeros.
- **Theorem C, θ > 1/3.** The defect sum converges, so the lower bound is ≍ x^{2θ}. This is consistent with the upper bound x^{θ+ε}.
- **Theorem C at θ < 1/3, any rounding.** Lemma D forbids error x^{θ+δ}. This is Theorem L.

**Why this is not a step towards "θ < θ₀ ⇒ RH".** Lemma D is a lower bound on the error that holds whatever the zeros are. It needs the lattice structure: rounded p^a at affine images of the rational primes. A system outside 𝒦_θ has no ε_p to measure. Converting it into zero information would require the converse, that every discrete system with small error comes from a lattice rounding. The record gives no reason for that. Hilberdink/Révész (max(α, β) ≥ ½ for discrete systems) is consistent with RH-type zeros and forces nothing off the line. So the first lemma of L2b exists, but the second lemma (a zero-forcing inequality) cannot be formulated from it. **L2b is closed at the first lemma.**

## 5. What remains (Problem 6 below 1/3)

- **O164.201a (OPEN).** Find a discrete system with error O(x^{θ′}), θ′ ≤ 1/3, and a zero with β > ½. By Theorem L\* (ARGUED; Theorem L alone gives only that the exponent exceeds θ), it cannot be a bounded rounding of the Witt counts of an affine image of ζ.
  - Candidates must be "off-lattice". One option is to put the fractional masses {p^a} on new points (a DMV-type continuous→discrete transport). That approach is currently capped at x^{1/2} in the literature (DMV; Broucke–Debruyne–Vindas).
  - Another option is a base other than ζ(w) with integral local q_p. This forces a ∈ ℤ, i.e. θ ≥ ½. **PROVED**: q_p v_p^{−s} = p^{−w} with w affine forces q_p = p^c with constant c = a.
- **O164.201b (ARGUED → PROVED target).** Theorem L\*, via a large-sieve average over the moduli p in §3.5.
- **Boundary.** Quadratic Dedekind zetas sit at θ = 1/3 (with GRH expected), and ζ sits at θ = 0. No discrete example with off-line zeros is known below 1/3.

## Grid cell 5G (append to the master grid)

`5G | BF_θ^disc below 1/3 | L2a (re-rounding the Witt counts) CLOSED NEGATIVE: Theorem L PROVED (error exponent > θ for every rounding in 𝒦_θ), L* ARGUED (≥ (1−θ)/2 ≥ 1/3; gap = residue equidistribution of h_n mod p for p ≤ Y^{1−ε}) | L2b: Lemma D (integrality defect inequality) PROVED, zero-blind ⇒ no RH step | Problem 6 for θ₀ ≤ 1/3 OPEN; "counterexample must be off-lattice" ARGUED (via L*) | R164_201`

## Ledger

| Item | Label |
|---|---|
| 1/3 enters Theorem C only via Σ_p ε_{p,1}²p^{−2a} | PROVED |
| Greedy rounding keeps the zeros of ζ(w) on Re w = ½ (L converges for Re w > 0) | PROVED |
| \|ε_p\| ≥ ‖p^a‖ for every integer choice | PROVED |
| Positive proportion of p with ‖p^a‖ ≥ ¼ | PROVED-CITED (Vinogradov, from memory, flagged) |
| Theorem L (power form; δ(θ) = θ(1−3θ)/(5−3θ)) | PROVED after repairs R1, R2 (R164_291) |
| Repair R3 (even characters only) improves κ to < a/(2+a) | PROVED per R164_291, optional |
| Theorem L\* (sharp (1−θ)/2) | ARGUED |
| Lemma D (with −K, P ≤ Y^κ) | PROVED in 𝒦_θ |
| Integral base q_p forces θ ≥ ½ | PROVED |
| "Integrality is sign-blind for every θ > 0" | NOT OBTAINED (OPEN) |
| "θ < θ₀ ⇒ RH" for some θ₀ > 0 | OPEN; no route from Lemma D |
| Problem 6, θ₀ ≤ 1/3 | OPEN |
