# R186_004 — L-TB1.0: the Kreĭn flow across the first threshold (½log2, ½log3]

Phase 186, TB-1, lemma L-TB1.0.
Sources: R186_000 §2.1 and TB-1; R185_006 (symbol identity); R183_030/032; G2_B5_R1 (de Branges objects).
Numerical (control only, scratchpad `kf.py`, no intervals): Legendre basis, quadrature in s up to 4·10⁴.

## Status

**Verdict.** L-TB1.0 remains **reduced, not proved**. There are three structural findings PROVED that correct the
framing of TB-1a:

1. **(PROVED) No jump: the window symbol is a single one.** For every T, W_T is the Wiener–Hopf truncation
 to L²(I_T) of a **single** symbol θ_∞ = m − Σ_n v_n cos(s log n), in the sense of forms. The term n acts
 identically zero on L²(I_T) while log n ≥ 2T (edge lemma), and its effect for 2T > log n is controlled
 by the overlap length 2T − log n. The jump map 𝒥_n of TB-1a is **the identity**: the Kreĭn data are continuous in T.
 The prime enters the Kreĭn datum (the function k = θ̌ restricted to (−2T, 2T)) as an atom at the
 **edge** of the autocorrelation interval, with no jump in the form.
2. **(PROVED) Monotonicity.** λ(T) := inf{W_T(h)/‖h‖² : h ∈ 𝒫_T} is non-increasing and continuous in T. Consequently,
 "the system does not explode in (½log2, ½log3]" is exactly equivalent to λ(½log3) > 0. This is a single-T statement.
 No forward differential inequality in T adds information: Q = λ decreases, and what must be bounded is the
 endpoint. **The flow is not a tool for L-TB1.0**; at most it reorganizes the problem at fixed T.
3. **(PROVED) Exact pairwise reduction.** With J = [−T, T−log2], J′ = J + log2 and the middle segment
 M = [T−log2, log2−T], the symmetric sector h = φ + φ(·−log2) (supp φ ⊂ J) has the form of a **multiplier**
 (1/2π)∫θ(s)·4cos²(s log2/2)|φ̂|² ds, and the antisymmetric one the same with 4sin². The Tate restrictions on h
 are equivalent to φ̂(±i/2) = 0, because 1 + 2^{∓1/2} ≠ 0.

**NUMERICAL finding that displaces the proposed mechanism.** Each sector separately, with its own Tate
restrictions, is **very** positive at T = ½log3. The symmetric sector has min ≈ 1.187‖φ‖², the antisymmetric
≈ 3.152‖φ‖² and the middle segment M ≈ 1.428. The complete form W_T on 𝒫_T instead has λ ≈ 9.5·10⁻⁴ (matches
R185_006), and A_∞ has ≈ 0.0825 (matches R185_006). Hence **the near-kernel does not live in the pair sector**: it
is produced by the **coupling** between sectors, with the Tate restrictions distributed between them. Without Tate,
the symmetric sector is indefinite (min ≈ −3.14) and so is M (≈ −0.31). The uncertainty mechanism (short interval
⟹ spectral mass outside the negative band) is correct **within** each sector, but it is not what decides the sign
of W_T.

**Where the analysis stops.** The crude prolate bound does not even prove the pair sector. With L = log(3/2) and
s₀ = 3.305 one has c = Ls₀/2 = 0.669 and λ₀(c) = 0.406 (NUMERICAL). The negative part is bounded by
4·6.352·0.406 ≈ 10.3‖φ‖², against a real minimum of 1.19. The exact profile of θ is needed. For the complete form,
the finite reduction of R185_006 Thm 3.2 is still the route (dim ≤ 47, interval arithmetic). The archimedean
part (gap_∞ > 0 at ½log3) also remains NUMERICAL.

## 1. Definitions and edge lemma

Let 𝒫_T = {h ∈ L²(I_T) real : ĥ(±i/2) = 0}, with I_T = [−T, T]. Let b_n(h) := ∫ h(x)h(x+log n) dx. By Plancherel,
(1/2π)∫|ĥ|² cos(s log n) ds = b_n(h).

**Lemma 1.1 (edge lemma; PROVED).** If supp h ⊂ I_T and log n ≥ 2T, then b_n(h) = 0. If log n < 2T, then
b_n(h) = ∫_{−T}^{T−log n} h(x)h(x+log n) dx and |b_n(h)| ≤ ‖h|_{J_n}‖·‖h|_{J_n+log n}‖, where |J_n| = 2T − log n.
*Proof.* The integrand vanishes unless x and x+log n are both in I_T, i.e. x ∈ [−T, T−log n]. For
log n ≥ 2T that set has measure zero. The bound is Cauchy–Schwarz. ∎

**Corollary 1.2 (PROVED).** With the symbol identity of R185_006 §1 (PROVED for T ≤ ½log3), the same form
W_T(h) = (1/2π)∫|ĥ|²θ, with θ = m − √2 log2 cos(s log2), holds for **every** T ≤ ½log3, also for T ≤ ½log2:
there the prime term is null by Lemma 1.1. In general W_T(h) = A_∞(h) − Σ_{log n<2T} v_n b_n(h). It is the
truncation of the single symbol θ_∞ in the sense of forms: the terms with log n ≥ 2T vanish by themselves. For each
fixed h, T ↦ W_T(h) is constant as T grows and supp h stays fixed. The only dependence on T is the domain. For h
varying with T, the contribution of prime n at T = T_n⁺ is O(‖h|_{J_n}‖·‖h‖), with |J_n| → 0, and there is no jump.

**Kreĭn data (CITED, Kreĭn 1940s; Kreĭn–Langer for the indefinite case; de Branges, *Hilbert spaces of entire
functions*, ch. 2 and 6).** Let k be the even distribution with k̂ = θ_∞. The Kreĭn extension problem on (−2T, 2T)
only uses k|_{(−2T,2T)}, which contains the atoms −½v_n(δ_{log n} + δ_{−log n}) with log n < 2T. As long as the
form is positive definite on L²(I_T) (in G2_B5_R1 the complete form, without Tate), its spaces form an isometric
chain of de Branges spaces ℋ(E_T) with canonical system JY′ = zHY, H ≥ 0 (PROVED in G2_B5_R1, recorded in R186_000
TB-1). By Lemma 1.1, H and the monodromy M_T depend continuously on T through T_n: **𝒥_n = id**. The "jump law"
requested is therefore the following: the primes enter as atoms at the edge of the autocorrelation interval, and
their effect appears through the Kreĭn growth formula (resolvent at the edge), not through a Christoffel/Uvarov
transformation.

**Warning for TB-1b.** For the complete form on L²(I_T) without Tate, θ(0) < 0 forces the form to be indefinite
for large T. Without the restrictions, at T = ½log3 the sector M already gives −0.31 (NUMERICAL). The positive
canonical system of G2_B5_R1 lives up to its own T*. The object relevant to row D is the **compression to 𝒫_T**,
which is not a Toeplitz truncation but one of codimension 2. Its Kreĭn theory is that of a chain with two pointwise
restrictions at z = ±i/2 (de Branges space with two prescribed zeros in the division: ℋ_T ⊖ span{K_T(·, ±i/2)}).
This is CONDITIONAL on writing out the chain: no cited reference covers it as such.

## 2. The invariant Q(T)

**Proposition 2.1 (monotonicity; PROVED).** If T < T′, then 𝒫_T ⊂ 𝒫_{T′} (by extension by zero) and
W_{T′}|_{𝒫_T} = W_T (Corollary 1.2). Hence λ(T′) ≤ λ(T). The continuity of λ is lem:contA of Paper 47 (PROVED).

Consequently, the only Q that satisfies (a)–(d) with exact sign is λ(T), or its matrix version: the
inertia of the compression to 𝒫_T, which is constant while λ > 0. For (b): Q is monotone, but **in the wrong
direction**. (d) holds: the variation at the onset of the prime is O(√(2T − log n)) in the bound of Lemma 1.1, and
the real variation is even smaller. (c) holds by definition. Hence the flow theorem "Q(½log2) > 0 and
dQ/dT ≥ −c·Q" cannot be stronger than bounding Q(½log3) directly: it is equivalent to it, because λ is
non-increasing. A Grönwall inequality would need to bound ∫λ′, which is the same problem with one fewer scalar.

**Hadamard formula (OPEN in this context).** For continuous kernels, λ′(T) is expressed with the values at ±T of
the eigenfunction and of the Tate Lagrange multipliers. Here k has a singular part (θ ~ log|s|), and the
eigenfunction may be singular at the edge. The formula is not written down as PROVED.

## 3. Pair sector

**Proposition 3.1 (PROVED).** Let ½log2 < T ≤ ½log3, J = [−T, T−log2] and L = |J| = 2T − log2 ≤ log(3/2) = 0.405.
For φ ∈ L²(J) and h_± = φ ± φ(·−log2), where supp h_± ⊂ I_T and the second copy sits in J + log2:
- (i) W_T(h_±) = (1/2π)∫θ(s)·|1 ± e^{−is log2}|²|φ̂(s)|² ds, with |1 + e^{−is log2}|² = 4cos²(s log2/2) and
 |1 − e^{−is log2}|² = 4sin²(s log2/2);
- (ii) h_± ∈ 𝒫_T ⟺ φ̂(±i/2) = 0. Indeed, ĥ_±(z) = φ̂(z)(1 ± e^{−iz log2}), and at z = ±i/2 the factor equals
 1 ± 2^{∓1/2} ≠ 0.

*Proof.* (i) is the symbol identity applied to h_±. (ii) is a direct computation. ∎

**Sign correction with respect.** In the symmetric sector, b_2(h_+) = ‖φ‖² > 0 and the contribution of the
prime is −√2 log2‖φ‖², the unfavorable one. The factor 4cos² does not kill the low frequencies, where θ < 0. The
target is right about this, and that is why the symmetric sector without Tate is negative (min ≈ −3.14‖φ‖²,
NUMERICAL).

**Prolate bound (NO-GO for the crude route, NUMERICAL constants).** Let P_{s₀} be the projector onto the band |s| < s₀ = 3.305.
For supp φ in an interval of length L one has ‖P_{s₀}φ‖² ≤ λ₀(c)‖φ‖² with c = Ls₀/2 (Slepian–Landau–Pollak,
CITED). At T = ½log3, c = 0.669 and λ₀ = 0.406. Since θ ≥ θ(0) = −6.352 (PROVED, R185_006), the negative part of (i)
is bounded by 4·6.352·0.406 = 10.3‖φ‖². The positive part admits no comparable lower bound without knowing the
profile of θ·4cos², which vanishes at s = π/log2 = 4.53. **It does not close.** A useful bound needs: (1) using Tate
(φ̂(±i/2) = 0) inside the concentration estimate, i.e. the prolate with two restrictions; (2) using the
profile θ(s) ≥ m(s) − 0.98 piecewise, with m increasing (CITED digamma monotonicity). It is a low-dimensional
check: the prolate eigenvalues drop to 0.02 at the second mode, so there are two or three relevant modes. It is
feasible with intervals, but it has not been done here.

**Actual values (NUMERICAL, T = ½log3, Legendre N = 8–16, stable to 10⁻⁴).**

| sector (with its own Tate) | min / ‖φ‖² | without Tate |
|---|---|---|
| symmetric, symbol θ·4cos² | 1.187 | −3.139 |
| antisymmetric, symbol θ·4sin² | 3.152 | — |
| middle segment M, symbol θ (= A_∞ there) | 1.428 | −0.314 |
| **complete W_T on 𝒫_T** | **9.5·10⁻⁴** | — |
| A_∞ on 𝒫_T | 0.0825 | — |

**Reading.** The target located the difficulty in the low-frequency symmetric pairs. The data say something
else: with Tate, that sector has margin 1.19. The 10⁻³ cancellation is due to the fact that 𝒫_T does **not**
decompose as a direct sum of the sectors with their own Tate. The two Tate conditions are global: the near-kernel
uses components in J, J′ and M that violate Tate separately and satisfy it jointly. It is a codimension-2
phenomenon plus coupling, consistent with the alignment h(x) ↔ h(x+log2) of R185_006. What must be controlled is
the 3×3 coupling matrix of blocks (J, M, J′) restricted to the complement of the sectoral restrictions. Its
singular parts are, at most, four directions: two restrictions per sector minus the two global ones. With that,
**L-TB1.0 is reduced to a small-dimensional Schur matrix (≤ 4 edge modes) plus three sectors with margin
≥ 1.19**. This is a more concrete target than the dim-47 secular one of R185_006 Thm 3.2. The reduction itself is
CONDITIONAL: the cross blocks J–M and M–J′ must be written out and bounded; they have a kernel k(x−y) singular at
the common point of the intervals.

## 4. Archimedean part

"A_∞ > 0 on 𝒫_T up to T₁ ≈ 0.596" remains NUMERICAL (0.0825 at ½log3). The CC route (K_I at |I| = log2) +
Weyl/interlacing gives at most gap_∞ > 0, which is not enough (R185_006 §2, NO-GO). This was not proved here.

## 5. Falsifier M_m

On the window T ≤ ½log3, M_m has the same Γ and the same primes, and hence **the same form** W_T (R184_004
Thm 4: the forms coincide below the first off-line contact). Every proof of L-TB1.0 holds for M_m, and
that is correct: M_m is also positive there. The falsifier does not discriminate in L-TB1.0. It is only mandatory
for the statement ∀T, i.e. for (γ) of TB-1b. What must be recorded is that, by Proposition 2.1, any
flow invariant on a single symbol θ_∞ is non-increasing and monotone. **Part (β) of TB-1b (the archimedean flow
preserves 𝒦_Euler) cannot be a monotonicity property of λ.** It has to be a condition on the **shape** of the
de Branges chain, for example the factorization of the Weyl function, which M_m must violate at some T. This
remains OPEN.

## Audit notes

- Lemma 1.1 and Corollary 1.2 rest on the symbol identity of R185_006 §1, which must be checked against the
 definition of W in Paper 47 (def:W, eq:nuw), including the C₀ constant and pole terms. It was taken as PROVED here.
- "𝒥_n = id" is a statement about the form. If TB-1a was thinking of the monodromy of a **positive** canonical
 system, that system only exists while the complete form (without Tate) is positive. Its T* may be < ½log3, and
 the sector M without Tate is already negative at ½log3. Check with G2_B5_R1 which form it used ("the complete
 form" is ambiguous).
- The figures in the §3 table have no intervals. The quadrature is truncated at s = 4·10⁴, with a small
 ∫log s/s² tail. Stability checked in N.
- The reduction to "≤ 4 edge modes" is heuristic in the count. The kernel of A_∞ is singular on the diagonal, and
 the cross blocks between adjacent intervals are not trace class. They may not be effectively finite rank.

## For Paper 47

- Add, alongside the symbol identity (if R185_006 is integrated), the observation of Corollary 1.2: there is a
 single symbol θ_∞ and W_T is its truncation. The prime thresholds are edge atoms, not jumps. λ(T) is
 non-increasing (Proposition 2.1, trivial with lem:contA).
- Do not integrate the pair sector as a positivity mechanism: the data show that the margin is in the
 coupling.
- Labels: Lemma 1.1, Cor 1.2, Prop 2.1, Prop 3.1 PROVED. 𝒥_n = id PROVED (at the level of forms). Table §3
 NUMERICAL. Crude prolate route NO-GO. Reduction to edge-mode Schur CONDITIONAL. L-TB1.0 OPEN.

## Note (R186_092)

* PROVED: Lemma 1.1, Cor 1.2 (T ≤ ½log3), Prop 2.1, Prop 3.1. "𝒥_n = id" at the level of forms; continuity of the Hamiltonian/monodromy → CONDITIONAL. Table reproduced (kf.py); sectoral minima normalized by ‖φ‖² (= ½‖h‖²). The "key finding" J/M/J′ is heuristic; Schur CONDITIONAL.
