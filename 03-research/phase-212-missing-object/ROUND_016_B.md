# Round 16, memo B — KMS states on algebras where the sum and the product of ℕ act together

Idea put through the gate: obtain the sign of `a_T` as `φ(x*x)`, or as a derivative or boundary value of expressions of that type, for a KMS state `φ` of a C*-dynamical system in which `+` and `·` of ℕ act together: Bost–Connes `(ℚ⋊ℚ_+^*, ℤ⋊1)`, the Toeplitz algebra `𝒯(ℕ⋊ℕ^×)` of Laca–Raeburn, Cuntz's `𝒬_ℕ` and the Cuntz–Li ring algebras.

**Verdict: repetition.** The seed appears almost literally in the corpus and the branch stops at the cross-check. This memo leaves three new short observations: §2 shows why the concrete proposal cannot work, §3 corrects the analysis of the control `c = 2` and §4 points out the only point that remains unexcluded. There is no construction.

## 0. Four-point filter

1. **Closest antecedent, read in primary sources.**
   - `03-research/phase-193-creation-campaign/CA_E_000_SEEDS.md`, §E1: «KMS phase transitions beyond Bost–Connes (Laca–Raeburn Toeplitz algebra of ℕ⋊ℕ^×; Cuntz–Li ring algebras)». It was DISCARDED because KMS positivity holds only for real `β`, by O11 (Beurling), by (R)(2) (the Γ factor is missing) and for being a retry of 114_d_116.
   - `03-research/phase-114-closing-the-four-rows/114_d_116_KMS_MODULAR_CONTACT_AUDIT.md` (Bost–Connes). Its conclusions:
     - the Gibbs state is trace class only for `β > 1`;
     - the modular variance has coefficient `Λ log n` and not `Λ`;
     - time invariance diagonalizes the two-point matrix;
     - the Γ determinant is missing.
   - Other antecedents:
     - `phase-67-quantum-q-index/E67_8_RESULTS.md`: semigroup isometries detect divisibility and not logarithmic distance.
     - `159 G1` (cell 4H): Bost–Connes, Borger/Witt, DEAD.
     - `G8H` Thm U: the core flow is the same for ζ, Beurling and Bost–Connes.
     - R9-04 and P51-2: the partition function is ζ(β).
     - Index README, front E of phase 193: «KMS beyond Bost–Connes … dead».
   - `AUDIT_PHASE193_CERTAINTY.md`, row 12: the discard of E1 is «CIRC on O11; "real β only" ARG». That is, the Beurling part of the discard was circular.
2. **What the prompt proposes as new.** Two things:
   - the exact mixed relation `v_p s = s^p v_p` as the place where Beurling fails (this answers precisely the CIRC O11 clause);
   - the smoothed element `x_F = ∫F(t)σ_t(y)dt`.
3. **Does it avoid the difficulty?** Only partly:
   - it does answer O11, because Beurling has no ring and hence no mixed relation;
   - it does not answer the diagonality of 114_d_116 nor (R)(2);
   - §2 proves that the smoothed bilinear form lives in the wrong dual variable;
   - §3 proves that the ring structure does not break `c = 2`.
4. **Global connection.** One would need an identity `a_T(F) = φ(x_F*x_F) + (remainder ≥ 0)` valid for all `T`. §2 discards the KMS two-point form. No candidate identity remains.

## 1. Cross-check: what was done and which class closed each thing

| Object | Place | Closure |
|---|---|---|
| Bost–Connes Gibbs, `H ε_n = log n ε_n`, mean energy `Σ Λ n^{−β}` | 114_d_116 | NO-GO of the KMS covariance class: diagonal two-point, variance with `Λ log n`, `β = ½` of type III |
| `𝒯(ℕ⋊ℕ^×)`, Cuntz–Li, phase transition | CA_E_000 E1 | DISCARD: real `β`, O11 (CIRC), (R)(2) |
| Bost–Connes, Witt, scaling site | 159 G1, G1_B5_R3–R5 | DEAD (walls OT-5′, installation) |
| Isometries of `ℕ^×` (Cuntz semigroup), Haar | phase-67 E67.4 and E67.8 | NO-GO: orthogonality destroys interference; divisibility is read |
| III_1 core flow | G8H, Thm U | DEAD (F3: the same for Beurling and Bost–Connes) |
| Adele class space (`ℚ⋊ℚ^*` on `𝔸`) | phases 158 and 159 | reformulation of row D, not closure |
| Tomita, Araki/Petz, Golden–Thompson | front E of 193 | dead |

## 2. Lemma V (dual variable). PROVED

**Statement.** Let `(A, σ)` be any C*-dynamical system, `φ` a `σ`-invariant state (in particular, a KMS_β state), `y ∈ A`, and `x_F = ∫F(t)σ_t(y)dt`. Then there exists a finite positive measure `μ_y` on ℝ such that

`φ(x_F* x_F) = ∫ |F̂(ξ)|² dμ_y(ξ)`.

In the Bost–Connes system, with `y = Σ a_n μ_n` and the Gibbs state, one has `μ_y = Σ |a_n|² n^{−β} δ_{log n}`. Hence

`φ(x_F* x_F) = Σ |a_n|² n^{−β} |F̂(log n)|²`.

**Proof.**
1. By invariance, the two-point function `g(u) = φ(y* σ_u(y))` is positive definite.
2. By Bochner, `g = μ̂_y`.
3. Integrating against `F(t)F(s)` gives the general formula.
4. In Bost–Connes, invariance makes the `μ_n` of different energy orthogonal, which is exactly what 114_d_116 observes.

**Consequence.** Smoothing the dynamics evaluates `|F̂|²` at the frequencies `log n`. The prime part of `a_T` is `Σ v_n c_F(log n)` and evaluates the autocorrelation at the delays `log n`. They are Fourier transforms of each other. If the prime part is written in frequency, one gets `∫|F̂|² Σ v_n cos(ξ log n) dξ/2π`. That density is not positive, so it is not the `μ_y` of any invariant state.

The kernel `Σ a_n n^{i(s−t)}` suggested by the prompt is therefore in the wrong variable. Passing from one variable to the other requires the explicit formula, i.e. the spectral side, and reconstruction from that side is already closed in the corpus (phase 155, reverse track). This subsumes the diagonality observation of 114_d_116 and extends it to every invariant state and every `y`.

**Restriction of the lemma.** It holds for the class «quadratic form in `F` of type `φ(x_F*x_F)` with `x_F` a smoothing of the dynamics». It does not exclude an `x_F` depending on `F` in another way, for example via the additive shift `s`. That case remains open in §4.

## 3. The control `c = 2`: correction and lemma. PROVED

**Correction.** The prompt suggested that `c = 2` was a rescaling of `β` via `H ↦ 2H`. This is false: `2H` has spectrum `log n²`, which moves the positions and does not double the weight. The correct model of `ζ(β)²` is the tensor product system.

**Lemma A (ring `ℤ×ℤ`).** The `ax+b` algebra of the ring `R = ℤ×ℤ` is `𝒯(ℕ⋊ℕ^×) ⊗ 𝒯(ℕ⋊ℕ^×)`, with:
- additive group `ℤ²`;
- multiplicative monoid `(ℕ^×)²` acting coordinatewise;
- energy `log(mn)`.

Its mixed relations `v s = s^p v` hold exactly in each coordinate, its partition function is `ζ(β)²` (or `ζ(β−1)²` in the Toeplitz version) and `−∂_β log Z = Σ 2Λ(n) n^{−β}`.

**Proof.** It follows from Laca–Raeburn universality in each factor (CITED), taking the tensor product of the Gibbs states.

**Consequence: «sum and product» does not break `c = 2`.** Consider a certificate whose sign uses only four ingredients:
- positivity of states;
- ring relations `+/·`;
- KMS;
- the identification of the weight with `−∂_β log Z_R`.

Applied to `R = ℤ×ℤ`, that certificate produces the form with weight `2Λ`. By Lemma T of round 13, it then proves something false.

**What does separate `c = 2`.** If the archimedean term is also read from the ring (`R⊗ℝ = ℝ²`, factor `Γ_ℝ²`), the ring `ℤ×ℤ` produces `2a_T` and not the control. The control is `Arch − 2·primes`, and no ring realizes it: the rank of `R⊗ℝ` is 1 and the weight is 2, and those two do not match. Therefore, the only sign lever against `c = 2` within this class is to couple the Γ factor with the weight through the rank of the additive group.

- **Deletion of one prime power (PROVED).** `ζ(s)·exp(−p^{−ks}/k)` does not have non-negative integer coefficients. It is not the partition function of any semigroup, so no ring system realizes it.
- **Beurling (ARGUED).** There is no ring, and hence no `s` with `v_p s = s^p v_p`. This repairs the CIRC O11 clause for this class, but is not enough by itself.

## 4. What remains unexcluded, and without a written object

The cross-check of §3 says what would be needed: a single object that reads the Γ factor and the Euler weight in one step, through the rank of the additive group. In this class, that object is the action of `ℚ⋊ℚ_+^*` on `𝔸` with its real place. That is the adele class space, which phases 158 and 159 already closed as a reformulation. Hence it is not built.

Nor are the `x_F` built with the additive shift `s` instead of the smoothing of `σ` excluded. §2 does not cover them. But no identity connecting `φ(x_F*x_F)` with `c_F(log n)` is available. It remains OPEN and without candidate.

**Question about `P_T` (ARGUED, without identity).** The conditions `∫F e^{±t/2} = 0` are equivalent to `F̂(∓i/2) = 0`, i.e. to annihilating `x_F` continued to imaginary time `∓i/2`. This corresponds to the edge of the KMS strip for `β = 1`, where the Gibbs state dies by the pole. No identification of `P_T` as the kernel of two pole functionals in the GNS space leading to a sign was found.

## 5. What an independent check must rederive

- Lemma V.
- Lemma A: that `𝒯(ℕ⋊ℕ^×)^{⊗2}` is the `ax+b` algebra of `ℤ×ℤ` with weight `2Λ`.
- The argument that `exp(−p^{−ks}/k)` breaks integrality.
