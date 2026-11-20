# Round 13, memo B: the weight as the equality case of a positivity (Gram, Schur, completed square)

## 0. Proposal examined

Rounds 6–12 leave an observation, without the rank of a theorem. The objects with a manifest sign do not see the weight:
the Sonin square, the ratio channel `∫ĝ|A|²`, the leakage squares, the lattice discrepancies and the
logarithmic uncertainty. The objects that see the weight have no sign: the product channel `∫ĝ Re A²`, the
boundary commutator, the hyperbola tail and the prime part of Sonin. The only piece that sees the exact weight is
(PC) of R161_001 Thm. 3.1:

  `S_N A_M 𝓕 = {X,E_N} − L_M^*E_N − J H_{M,N} − H_{M,N}𝓕`,

and it sees it as an equality that breaks (interior defect `δ_a(k) = Σ_{d|k}a(d) − log k`).

The proposal is to combine a signed blind object with an unsigned one that sees the weight, so that the weight
enters as the **equality case** of a positivity. Formats examined:

- (a) Gram, Cauchy–Schwarz or Schur complement `[[Q1,B],[B*,Q2]] ⪰ 0`, with `Q1`, `Q2` blind and `B` carrying
  the weight.
- (b) Completed square `‖u − Lv‖²`, with `L` the von Mangoldt operator.
- (c) Interpolation in `c`, Lemma S and duality.

## 1. Strict primary-source cross-check (before deriving)

| Format | Closest antecedent (read) | Result of the cross-check |
|---|---|---|
| (a) Schur with arithmetic cross block | **R170_861** §§0–1 (factorization (0.3)): if `A − D*G⁻¹D = H` with `G > 0`, the extension is a triangular congruence of `H ⊕ G`, and its positivity is that of `H`. The explicit application is to `D ∈ {E, H_{M,N}, S(q)A(r), 𝒞_PC}`. See also `ANNEX_170_FILES_3.md` T1/T4 and `RULES_AVOID` I5. | Literal repetition: «placing `H_{M,N}` in the cross block creates no energy». |
| (a) Cauchy–Schwarz with `Λ∗1 = log` | R170_841 §4.2 (`RULES_AVOID` I2): with the probability `Λ(d)/log k` one gets `|β_Λ|² ≤ (log k)Σ_Λ`. | The bound is even and `β_Λ` is odd (`β(12) < 0`). Repetition. |
| (a) Inverted version, Lorentzian determinant | Phase 135 (Hodge transfer, conditional on `h⁰`); R160_C7_R1 §§5–6 (`RULES_AVOID` M1, N1). | The Lorentzian class reduces to the original statement (Prop. 6.2). |
| (a) 2×2 Turán-type or Pfaffian determinants | POWER_RECIPROCAL_PFAFFIANS_083, POWER_FOUR_TURAN_084 (memory of rejected selections, the project rules). | The Pfaffian product is negative. Repetition. |
| (a) Gram of layers | POWER_GRAM_SLICES_OBSTRUCTION, ANNEX_211_GRAM_HYPERBOLIC (`RULES_AVOID` D16). | Gram of Λ-free layers. Repetition. |
| (b) Completed square | R170_854 §6.3 (every completion by squares of the graded current is indefinite or gives the ratio channel); R170_860–861 (congruence); `RULES_AVOID` I5 (`Σ(Λ(n)/√n)‖F − U_nF‖²` leaves a divergent constant); I2 (`γ = Λ log − Λ∗Λ` collides with Selberg, 850–851); Q3 / R161_034. | Repetition. |
| Linear term of (a) and (b) | (OR) of R161_002 §2: `Re⟨R F, S_N𝓕F⟩ = ⟨A_M G, S_N^*S_N G⟩`. Its positivity on all of `L²` is the problem itself. | Oriented L161.3 remains OPEN (`RULES_AVOID` U2). This format does not close it (§2). |
| (c) | Interpolation `a_c` affine in the weight: blind (`RULES_AVOID` B8, W-lin). Duality `Θ_T = max_c λ_A`: B10. Lemma S: reformulates the sign as existence of a multiplier (B3). Douglas: EQUIV (R161_002 §4). | Repetition. |

The cross-checks already give repetition in all three formats. So that the stop is precise, and not merely textual, §2
proves the common reason in the most general format (a).

## 2. Why the «equality case» does not transport a sign

**Lemma 1 (block dichotomy; PROVED).** Let `𝕳 = [[Q1, B],[B*, Q2]]` on `P_T ⊕ 𝒦`, with `Q2 ≥ g_0 > 0`, and
suppose `Q1 − B Q2⁻¹ B* = a_T`.

- (i) If the positivity of `𝕳` is proved by writing `𝕳 = V*V` with `V = [u, v]` built from `F`,
  then `a_T(F) = ‖(1 − Π_v)u(F)‖²`, where `Π_v` is the projection onto the range of `v`.
- (ii) If `𝕳 ⪰ 0` is not proved in this way, then `𝕳 ⪰ 0` is equivalent to `a_T ⪰ 0` (R170_861 (0.3)).

*Proof.* (ii) is (0.3). For (i), the Schur complement of a Gram is the square of the residue of the
orthogonal projection: `‖u‖² − ⟨u, v(v*v)⁻¹v*u⟩ = ‖(1 − Π_v)u‖²`. ∎

In case (i), the format is a factorization `a_T = ‖w‖²` with `w = (1 − Π_v)u`. It is the Douglas
factorization (EQUIV) unless `w` has its own formula, and its sign is that of a single square, valid for every weight.

**Lemma 2 (homogeneity; PROVED).** Write `u = u_0 + u_Λ`, with `u_0` free of `Λ` and `u_Λ` linear in the weight, and
suppose `v` free of `Λ`. Under `Λ ↦ cΛ`, the signed side equals `A_0 + 2cX + c²Y`, with
`Y = ‖(1 − Π_v)u_Λ‖²`. On the other hand, `a_T(cΛ) = Arch − cP` is affine in `c`.

- The identity for all `c` requires `Y = 0`. Then `X = 0` and the weight disappears.
- The identity at `c = 1` alone requires `Y = Arch − P − A_0 − 2X`. The quadratic term in the weight has to
  coincide with a linear expression.

*Proof.* Expand the square. `Y = 0` implies `(1 − Π_v)u_Λ = 0`, and then the cross term vanishes. ∎

Thus (a) with affine `B` reduces to (b). With linear `B` it is even in `Λ`: it is the analogue of Thm. 1.1 of R161_002, and
the global inversion `Λ ↦ −Λ` leaves the signed side unchanged.

**Lemma 3 (the quadratic term is the ratio channel; PROVED).** For `L_M = Σ_{d≤M} Λ(d) d^{−1/2} τ_{log d}`:

- the coefficient of `τ_{log(a/b)}` in `L_M^*L_M`, with `gcd(a,b) = 1` and `a, b > 1`, is `Λ(a)Λ(b)/√(ab)` (with
  `a, b ≤ M`);
- the coefficient at `r = 1` is `Σ_{n≤M} Λ(n)²/n`, which diverges like `½ log² M`.

*Proof.* One needs `ak` and `bk` to be prime powers with `a`, `b` coprime. If `k > 1`, then `k = p^i` and
`a`, `b` would be powers of `p`, against coprimality. Hence `k = 1`. ∎

Therefore the term `L*L` of (b) contains no divisor sum `Σ_{d|k}Λ(d)`. The relation
`Λ∗1 = log` governs the products `L S_N`, i.e. the support of `H_{M,N}`, and not the ratios. The premise of
(b), «identify `L*L` by applying `Λ∗1 = log` twice», is false. What appears is the ratio channel of Q3
with the divergent constant of I5.

**Checks (rule R3-i).**

- **With `c = 2`.** `‖(1 − Π_v)u‖² ≥ 0` still holds, because it is a square of vectors for every weight. If
  battery E (CITED) gives a negative direction of `a_T(2Λ)`, what fails is the equality.
- **With deletion of a prime power.** Same case: the square is indifferent.
- **With Beurling.** `L*L` and the square remain defined; only `E_N` is missing, and it does not enter the signed side.

No named signed step ceases to be `≥ 0` under these checks: the signed side is blind by construction.
**Scope correction:** this does not exclude a proof for Λ. Only the identification
with a_T may fail in the check. A Gram with its own formula and an exact identification proved without assuming the
target sign would be a valid certificate. Positivity transfers to the falsifier only when
the whole chain of equality and inequality survives, including the additional terms.
In branch (ii), the only signed step is `a_T ⪰ 0` itself. To invert the block one needs `Q2⁻¹`. If
`Q2` contains the form, it is J3; if `Q2` is Λ-free, one falls into (i) or into the congruence of R170_861.

**Tests of R161_002 §6.** Formally they do not apply, because no variant passes the gate. In format (b):

- The inversion test of `Λ(2)` changes `Y` in the ratios `2/q`, of quadratic order. It does not change the
  interior defect `−2 log 2` at `k = 2`, which lives in the products.
- The two-point test requires the linear coefficient `2 log 2/√2`, which only contributes `X`, the pairing (OR).

## 3. Verdict

- **Concrete formats examined: repetition, no new candidate.** The general exclusion of
  every Gram, Schur or completed-square identity with a positive definite side for every weight is withdrawn.
  Lemmas 1(i)–(ii) exclude neither an independent construction nor a Λ-specific identity.
  In the concrete operator L_M of Lemma 3, the quadratic term in `Λ` is
  the ratio channel, where `Λ∗1 = log` does not act (Lemma 3). Patterns B3, B9 and J3.
- **Labels.** Lemmas 1–3: PROVED. Antecedents R170_841, R170_854, R170_861, R160_C7_R1, R161_002 and memos
  083/084: CITED. Breakdown under `c = 2` only in the equality: PROVED, conditional on battery E (CITED). Global
  sign of `a_T`: OPEN.
- **Operation that would reopen the class.** A `𝕳 ⪰ 0`, Gram or not presented as Gram, with its own formula and with
  independently proved positivity, together with the full identity of its Schur complement with a_Λ.
  Under `c = 2` that identity may fail; failure of the positivity of the block is not required. The only
  known source candidate is the infinitely divisible or Pick class (`RULES_AVOID` M4, ARGUED), and an
  explicit `𝕳` is missing. I do not propose it.
