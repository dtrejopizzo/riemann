# Round 2, candidate A — The exterior tail of the hyperbola as a sum of squares: selection memo

Notation of `../phase-211-sign-sandbox/STATEMENT_001.md` and of P47 §sec:firstcontact (thm:PCfinite,
eq:Gammaenergy, eq:collar, eq:Qbalance, prop:GEgap). Fix T > 0, integers M ≥ N ≥ e^{2T}, L ≥ 1, and

    a_m = 2m + ½,  s_m = a_m + ½ = 2m + 1,  b_m = √a_m e^{−a_m(T+δ)},
    e_m^±(t) = e^{∓a_m t} 1_{I_T}(t),   μ_m^±(F) = ⟨F, e_m^±⟩,   α_m^±(F) = b_m μ_m^±(F),
    Σ_L = 𝒪_L*𝒪_L + J𝒪_L*𝒪_L J = Σ_{m≤L} b_m² ( |e_m^+⟩⟨e_m^+| + |e_m^−⟩⟨e_m^−| ),
    H_{M,N} = Σ_{N<k≤MN} h(k) k^{−1/2} τ_{log k},   h(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) ≥ 0,
    C(F) = Re⟨H_{M,N} 𝓕F, Σ_L F⟩      (the tail pairing of R170_816 (3)).

This memo does not construct. It contains the cross-check, a short lemma that decides the selection, and the verdict.

## Cross-check

### (1) Closest antecedent

a. `phase-170-global-prime-inequality/R170_816` §§2–7: exact output Φ = B − C on window
   vectors; C only with a two-sided bound; §4 falsifies «h(k) ≥ 0 ⟹ pairing ≥ 0»; §6 separates the
   channel d = 2 and two Fourier correlations without sign remain. `R170_819`–`821`: at two scales, the same
   coefficients h(k), ΔH without sign. `R170_837` §4 (cell incompatibility: the detector D_Δ comes
   from the moment cell, the tail comes from another), Theorem 5.1 (common residue = closure), (6.7)
   (after recombining K_N = L_MS_N − H the form is independent of the weight). `R170_835` Prop. 4.1 and §9:
   «universal factorization by R_L with L finite: FALSE; restricted to the radical: exists a posteriori»
   (its proof is not used here). `R170_841` §4.2: the canonical positive completion is second
   order and even; it does not orient. `R170_870`: odd boundary class versus even data.
b. **Direct sum in k already attempted.** `phase-161-row-d-sum-product-square/R161_030`–`034`
   (index, catalogue 04, rows G4C-R161_030-032, G4C-R161_033-034, G4C-R161_035-038, G8B-161):
   oriented divisor variance with squares indexed by the fibres k = de and weights Λ(d);
   `R161_033` withdraws the realization: (PC) sums in k coherently, and passing to the direct sum
   Σ_k ‖·‖² erases the Gram terms between distinct k; `R161_037`–`039`: the missing saturation
   is the final statement, with a matrix countermodel to its being automatic. P47 rem:returnremarks
   records the same («the variance of a sum labelled by divisor paths is not the norm of
   the coherent sum in k»).
c. **Squares with non-negative arithmetic weights on exterior functionals already written.**
   P47 eq:Qbalance: c_{N,L}(F) = Σ_{m≤L} d_{m,N} |(𝒪_LF)_m|², d_{m,N} = Σ_{n≤N} Λ(n) n^{−s_m};
   eq:Qspectral: Q_{N,L} is negative on every eigenvector with λ ≥ 0 and admits no representation as a sum
   of squares on P_T; eq:equivgate: the return inequality is the conclusion. `R161_071`–`072`,
   `R161_081`: the balance recomposes the equation and holds for arbitrary non-negative weights.
d. Phase 212: `ROUND_001_A` §4, `REVIEW_001_ABD` §4 (R1–R4), LEDGER K1.

The phrase «no memo attempted to write it literally as Σ_{k>N} h(k)|ℓ_k(F)|²» is exact only for
the incomplete fibres k > N with weight h(k). For the complete fibres k ≤ N with weights Λ(d), log k, the
conversion into a direct sum over k is the route R161_030–039, closed in the index. The candidate changes
the range of k and the weight; the recorded obstacle (coherence in k, two distinct vectors in the
pairing) depends on neither.

### (2) New object or claim

The ℓ_k were sought. There are exactly three ways to obtain squares from C, and none is a
sign step.

**(D1) Diagonal in Gamma moments.** The only functionals of F supported in the window that the
structure offers with index k are

    ℓ_k(F) = ( b_m k^{−s_m/2} μ_m^+(F) )_{m≤L} ∈ ℂ^L,     ‖ℓ_k(F)‖² = Σ_{m≤L} b_m² k^{−s_m} |μ_m^+(F)|²

(the vector 𝒪_L of the translate of F by log k, with the factor k^{−1/2}). With them the exact identity holds
(PROVED: it is Λ∗1 = log read on the Dirichlet series of the coefficients of L_MS_N − S′_N
at s = s_m)

    Σ_{N<k≤MN} h(k) ‖ℓ_k(F)‖² = ⟨𝒪_LF, ( D_{M,L} Z_{N,L} − Z^{log}_{N,L} ) 𝒪_LF⟩,           (1)
    Z_{N,L} = diag(Σ_{n≤N} n^{−s_m}),   Z^{log}_{N,L} = diag(Σ_{n≤N} (log n) n^{−s_m}).

It is the family of squares of c_{N,L} of P47 eq:Qbalance (the same ℓ_n, weight Λ(n) instead of h(k)).
It is not C: the difference C − (diagonal form) is a cross term, and the following Lemma proves it is
indefinite on P_T for any choice of diagonal coefficients.

**(D2) Coherent square by change of test.** Replacing Σ_L by an adapted test, W = P_T H𝓕,
gives Re⟨H𝓕F, WF⟩ = ‖P_T H_{M,N}𝓕F‖² ≥ 0. It is a square of the coherent sum in k, not
Σ_k h(k)|ℓ_k|²; it loses the moment cell that produces D_Δ (R170_837 §4) and has no written
relation with a_T. It is the coherent/direct gap of R161_033.

**(D3) Polarization.** Re ᾱβ = ¼(|α+β|² − |α−β|²): difference of squares, generic.

**Lemma (PROVED; class: forms C − ⟨α, Bα⟩ with test Σ_L, L finite, arbitrary non-negative weights).**
Let w(k) ≥ 0, not all zero, with finite support in k > N, H^w = Σ w(k) k^{−1/2} τ_{log k},
C^w(F) = Re⟨H^w𝓕F, Σ_LF⟩, and let B be any 2L × 2L Hermitian matrix. Then the form
F ↦ C^w(F) − ⟨α(F), Bα(F)⟩, α = (α_m^±)_{m≤L}, is not semidefinite (of either sign) on P_T.
In particular, for no system of functionals ℓ_k factoring through the moments
μ_m^±, m ≤ L, and no form ρ ≥ 0 on P_T, does ±C = Σ_k h(k)|ℓ_k(F)|² + ρ(F) hold on P_T; and each
summand Re⟨τ_{log k}𝓕F, Σ_LF⟩ is indefinite on P_T.

*Proof.* Since 𝓕* = 𝓕 on L², C^w(F) = Re Σ_{m,±} \overline{α_m^±(F)} β_m^±(F), with
β_m^±(F) = b_m⟨F, φ_m^±⟩, φ_m^± = 1_{I_T} 𝓕 (H^w)* e_m^±.
(i) If q(F) = Re⟨α(F), β′(F)⟩ is semidefinite on a subspace V with α(V) = ℂ^{2L}, then
β′ = B′α on V: for F ∈ V with α(F) = 0 we have q(F) = 0, hence F is in the radical of q on V, and the
polar form gives ⟨α(G), β′(F)⟩ = 0 for every G ∈ V, that is β′(F) = 0. On V = P_T surjectivity
holds because the exponentials e^{±a_m t}, e^{±t/2} are linearly independent on I_T.
(ii) Applied to β′ = β − Bα: each φ_m^± would coincide on I_T with a combination of e_j^±, j ≤ L, and of
e^{±t/2}. In the coordinate x = e^t, F(t) = e^{t/2}f(x), one has (H^w)*e_m^± = e^{t/2}g(x) with
g(x) = Σ_k w(k) k^{−1/2±a_m} x^{∓a_m−1/2} 1_{(ke^{−T}, ke^{T})}(x), bounded, compactly supported in
(0,∞), non-negative and non-zero; and φ_m^± = e^{t/2} ĝ(e^t) on I_T, with ĝ the cosine transform of g. The
condition says that ĝ coincides on (e^{−T}, e^{T}) with a Laurent polynomial in ξ (powers
ξ^{−2j−1}, ξ^{2j}, 1, ξ^{−1}). ĝ is entire, hence the equality extends to ℂ∖{0} and the Laurent
polynomial is a polynomial; ĝ is bounded on ℝ and tends to 0, hence it is zero, and g = 0. Contradiction. ∎

**Remark (PROVED; exact reformulation, without sign).** With L = ∞ the factorization does exist and is
explicit. ĝ is entire and even, ĝ(ξ) = Σ_{j≥0} γ_j ξ^{2j} ∫g x^{2j}dx, γ_j = 2(−1)^j(2π)^{2j}/(2j)!
(self-dual normalization e^{−2πixξ}); the term j = 0 gives the Tate vector e^{t/2} and vanishes on
P_T. For real F ∈ P_T,

    ⟨F, φ_m^+⟩ = Σ_{j≥1} γ_j Θ_j σ_{j−m}(T) μ_j^−(F),                                         (2)
    Θ_j = Σ_{N<k≤MN} h(k) k^{2j},    σ_r(T) = sinh(2rT)/r  (σ_0 = 2T),

and analogously for φ_m^− with 2 sinh((2m+2j+1)T)/(2m+2j+1). The series converges absolutely. Thus C is
a Hermitian form in the sequence of Gamma moments, with an explicit matrix whose columns alternate in
sign with j (factor (−1)^j) and in which the arithmetic enters only through the power sums Θ_j, that
is through the Dirichlet polynomial of the tail at the points s = −2j, dual to the s_m. This is the
exact form of «explicit ℓ_k»: there is no index k with squares; there is an alternating matrix in (m, j).
What remains to be written, and was not found, is an operation that signs that matrix together with the blocks
of E_N and of Tate.

### (3) Why the change would avoid the difficulty of the antecedent

It does not avoid it.

- **Coherence in k (R161_033, rem:returnremarks, REVIEW_001_ABD R3).** The Lemma shows that the
  obstacle is already present in a single k: each summand is indefinite. Passing from complete to incomplete fibres
  and from log k to h(k) changes nothing of what the Lemma uses (only w ≥ 0, w ≠ 0).
- **Genericity in the weight (R170_837 (6.7); LEDGER K1).** (1) and (2) hold for every weight, with the
  added interior defect; the Lemma holds for every w ≥ 0. Nothing in (D1)–(D3) uses Λ∗1 = log before
  recombining except to cancel the block k ≤ N, which is the linear use already recorded (RULES_AVOID I2).
- **Parity (R170_870).** The three conversions are quadratic and even, so the parity
  objection does not reach them directly; but what remains unsigned is the cross term between α and the
  part of β that does not factor through α, whose sign on the radical is what R170_837 Thm. 5.1 and P47
  eq:equivgate identify with the conclusion. No operation that orients it is available; the
  candidate does not evade R170_870, it merely does not get as far as it.
- **Requested operation non-linear in F.** None was found. The operations that depend on F
  (choosing the test, L or the phase according to F) give (D2) or per-vector statements on the radical, where the
  factorization exists a posteriori (R170_835) and constructing it is the closure.

### (4) Connection with global positivity on P_T

There is no identity that gives it. thm:PCfinite is an identity on the line with non-local test
z = S_N𝓕g; for a_M(F, z) to be a_T(F) one needs z = F, which has no solution with g in the window
(REVIEW_001_ABD §4.1). The only written connection is on the radical of a contact window
(R170_816 (3), (11)), and there it additionally requires signing B together with C. By the Lemma, an identity (G) whose
remainder contains the tail as Σ_k h(k)|ℓ_k|² with ℓ_k in moments of order ≤ L does not exist on P_T; the
L = ∞ version is the alternating matrix (2).

### (5) Lines that break for cΛ and a_P

There is no sign step to submit to the battery; what happens with the written identities is recorded.

- cΛ: in (1) the interior block (c − 1) Σ_{k≤N} (log k) ‖ℓ_k(F)‖² appears. The equality breaks for
  c ≠ 1, but for c > 1 the left side is still a sum of squares with non-negative weights: the
  positivity does not break. It is restriction K1 reproduced; (1) cannot be a sign step.
- a_P with P > N: the interior block is −Σ_{k≤N} (log k) ‖ℓ_k(F)‖² (all divisors erased); the
  equality and the sign break. But (1) is not tied to a_T, so this certifies nothing.
- The Lemma and (2) hold for every non-negative weight: they survive the whole battery. By rule 6 that
  disqualifies them as a mechanism; they are obstruction and reformulation.

The cross-check identifies repetition (R161_030–039; P47 eq:Qbalance–eq:equivgate; R170_816, 835, 837) and
there is no sign mechanism to write. The memo ends here.

## Result

**No new mechanism.** In addition, NO-GO with class (PROVED, Lemma): on P_T, with the moment test
Σ_L of finite L and any non-negative weight on k > N, the tail is not ± (sum of squares in moments
of order ≤ L plus a non-negative remainder), not even for a single k, and no diagonal correction in
those moments makes it semidefinite.

## What was proved

- Identity (1) (PROVED): the only sum Σ_{k>N} h(k)‖ℓ_k‖² with explicit ℓ_k is diagonal in 𝒪_LF and
  coincides with the family c_{N,L} of P47.
- Lemma (PROVED): indefiniteness of C − ⟨α, Bα⟩ on P_T for every B, L finite, w ≥ 0.
- Remark (2) (PROVED): with L = ∞, C is an explicit form in the Gamma moments, alternating in j,
  with the arithmetic in Θ_j = Σ_{k>N} h(k)k^{2j}. Exact reformulation; carries no sign.

## What failed and why

- The literal conversion into Σ_k h(k)|ℓ_k|² fails because the exterior functionals
  F ↦ ⟨τ_{log k}𝓕F, e_m^±⟩ do not factor through a finite number of Gamma moments (analyticity of ĝ),
  and with all the moments they factor with coefficients of alternating sign.
- The passage to a direct sum in k is the route R161_030–039 with another range and another weight; the
  recorded reason for the failure does not depend on them.
- No operation non-linear in F was found that diagonalizes the pair (𝓕F, Σ_LF); the available ones change
  the test and lose the D_Δ cell, or are a posteriori on the radical.
- There is no identity connecting any of these forms with a_T on all of P_T.

## Concrete next step

Do not relaunch «tail as squares» in any variant of range of k, weight or finite-rank test.
Record in the index (catalogue 04, next to G4C-R161_030-034) and in the grid the Lemma as a class NO-GO
and row K1 of the LEDGER as closed in the finite-L formulation. The only thing left not
excluded is the complete matrix (2): a future candidate would have to present, before deriving, an
exact identity that adds (2) to the blocks of E_N and of Tate in the same moment basis and whose
interior block (the coefficients δ_a(k)k^{2j}, k ≤ N, which for Λ are zero) enters with sign opposite
to the exterior one; without that written operation there is no candidate.
