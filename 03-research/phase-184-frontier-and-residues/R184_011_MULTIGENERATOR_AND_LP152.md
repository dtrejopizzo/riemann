# R184_011 — Residues (6F) of the grid: multigenerator rigidity (G2_B7_R5) and LP-152

*Phase 184, pure mathematics, no numerics.
OPEN / NO-GO. RH is not asserted, nor the closure of D. What was read: G2_B7_R5 complete, G2_B7_R4 (Prop S, Thm P), R160_S5 §3.2–3.3,
R160_M5_R1 §0, grid R162_2300 (§3 walls, §4 falsifiers, §6 item 59, part4/part6 jsonl).*

## State

* **LP-152: already closed. Grid item 59 is out of date.** The `R160_M5_R1` entry of the JSON (part6) marks it
  **DEAD [F3: DH, Epstein, Ξ_a]**, as a supersession of `R160_S2 §3.2`. R160_M5_R1, Cor 2.4 (PROVED), identifies it
  exactly: **LP-152(τ₀) ⟺ no zeros in the open Lorentz cone `C(τ₀) = {½+δ+iγ : δ > |γ−τ₀|}`**, i.e.,
  local RH. It therefore falls under exclusion (b) of the task: it is ⟺ RH, even if localized. I do not re-attack it.
* **Multigenerator rigidity (Q_mg): reduced, falsified in a model, NO-GO as a route to D.**
  1. **Prop 3.1 (PROVED).** Q_mg is true if RH is false. It is logically independent of "Λ ∈ 𝒮".
  2. **Thm 3.2 (PROVED under RH, with one CITED input).** Q_mg is equivalent to a single self-contained lemma (Q\*) about
     Carathéodory functions: *there is no tempered real Dirichlet series `B ≠ 0` with
     `Re B ≤ Re ξ'/ξ` in `Re s > ½`*.
  3. **Thm 3.3 (PROVED).** On the Type I curve, the analogue of Q\* is **false**: the model admits nonzero
     perturbations of positive density. In the product model of two curves with `log q₁/log q₂ ∉ ℚ` it is also false, already with
     **two generators**.
  4. **Cor 3.4.** No proof of Q\* can be uniform over the field. It must use data specific to ζ (either the unbounded
     density of zeros or the non-periodicity of the zeros, which is on the zero side, of Li–Radziwiłł type).
* **Verdict on D:** it does not move it. Q\* is rigidity at the vertex (uniqueness of Λ within its tempered fiber), and D
  asks whether the vertex is admissible. No resolution of Q\* changes the label of D. Row D: **OPEN**, unchanged.

---

## 1. The statements, verbatim and in context

### 1.1 G2_B7_R5 — multigenerator rigidity (03-research/phase-159-row-d-two-front-construction/G2_B7_R5.md §4)

**Objects** (record conventions, R5 §1):
* a comb `a : ℕ_{≥2} → ℝ`;
* `u_a = k_∞ + 2cosh(u/2) − Σ_n a(n)n^{−½}(δ_{log n}+δ_{−log n})`;
* for a perturbation `b`: `β_b = Σ b_n n^{−½}(δ_{log n}+δ_{−log n})` and `D_b = β̂_b`;
* `𝒯_abs = {b : Σ_{n≤x}|b_n|n^{−½} ≤ C(1+log x)^N}`;
* `𝒮^W`, `𝒮^A`: positivity ∀T, in complete or primitive form;
* `Γ_ζ` and `μ_Λ = Σ m_γ δ_γ`.

Under RH: `Λ+b ∈ 𝒮^W ⟺ D_b ≤ 2πμ_Λ` (R5 §8, convention check).

**Table R5 §4, open row (verbatim):** "`≥ 2` independent generators, `d⁺(b) > 0` | **OPEN** | needs: no
positive-density crystalline coupling of `±log⟨S⟩`-spectrum to `Γ_ζ`".

**Form of the statement (verbatim):** "Under RH, is there a positive atomic measure `α` on `Γ_ζ`, with `α({γ}) ≤ 2πm_γ`
and positive upper density, and a positive measure `σ`, such that `α − σ` has Fourier support in `±log(ℕ_{≥2})`?"

**OPEN subquestion:** the case `σ = c·Lebesgue`, i.e., a positive Fourier quasicrystal with spectrum in
`{0} ∪ ±log ℕ`.

**What is already closed around it:**
* Thm R′: `ℓ¹_w` or `𝒯_meas`;
* Cor M0: `o(log x)`;
* Thm M: `d⁺ = 0`;
* Thm P: one generator; uses Li–Radziwiłł (LR), which is on the zero side.

**What would follow for D (R5 §5, verbatim):** "**Not a mechanism.** No lower bound on `λ^A_T(Λ)` …". The only thing it would give is
that Λ is the only ∀T-positive point of `Λ + 𝒯_abs`.

### 1.2 LP-152 (R160_S2 §3.2; Doc 152; closed in R160_M5_R1)

**Objects:**
* `S_T(τ)`, the Gaussian prime correlation at one frequency;
* exact identity with forced sign (152.E);
* "needs upper bound at one frequency".

**Closure:** R160_M5_R1 §0. There is a heat-flow form `S = P + R_on + R_off`, and Cor 2.4 gives LP-152(τ₀) ⟺ local RH in
the cone `C(τ₀)`. Thm 4.2 gives the signless class falsifier. JSON part6, `R160_M5_R1`: **DEAD, F3:DH, Epstein, Xi_a**,
"identities hold for falsifiers".

**What would follow for D:** nothing beyond localized RH. It is wall **(N′)** of grid §3, in Gaussian form.

---

## 2. Corpus check (rule) and cell

* Grep for `G2_B7_R5|multigenerador|multigenerator|Cesàro progression`. It appears only in the sources and the
  inventories: phase 159 (G2_B7_R4/R5, mentions in G2_P*), R160_001_BRIEF, R160_S5 §3.3 item "multi-generator rigidity … OPEN",
  R160_C6_R1 (mention), R166_404 and R168_001 (inventories), and the grid with its backups.
* **No file after phase 159 attacks it.** The live residue is exactly the OPEN row of R5 §4.
* Grep for `LP-152`: it appears in the grid and in `R160_M5_R1`, which closes it. Grid item 59 (§6) needs to be
  cleaned up; it still lists it as OPEN; rule §8.3 already treats it as settled (supersedes_or_dup in the JSON).
* Cell 6F ◧: starts from the live residue, which is the OPEN row.

**Walls that Q_mg would need to evade, and why it might:**

| wall | why it might evade it | why it still doesn't move D |
|---|---|---|
| **E1** | It is not a nodal identity. It is an inequality on a fiber. | — |
| **W3 (class blindness)** | It does not evade it: Thm 3.3 shows that the Type I curve satisfies the negation. | Any argument must use something that separates ℚ from 𝔽_q(C). |
| **W-identification** | A global separator (zero density ∼ log t, non-periodicity) identifies ζ and gives no sign information. | See §4. |
| **"margins in the witness → 0 (Theorem M)"** (Dichotomy, §3) | Q_mg *is* a margin statement on the fiber. This is the wall that contains it. | It is rigidity, not positivity. |
| **(N)** | Any `Λ+b ∈ 𝒮` with `b ∈ 𝒯` implies RH, so Q_mg is vacuously true without RH. | Prop 3.1. |

---

## 3. Attack on Q_mg

### Prop 3.1 (logical position; PROVED)

Let `Q_mg`: "for all `b ∈ 𝒯_abs∖{0}`, `Λ+b ∉ 𝒮^W ∪ 𝒮^A`". Then:
* (i) `¬RH ⟹ Q_mg`;
* (ii) `Q_mg` does not imply `Λ ∈ 𝒮^W`, nor the converse;
* (iii) `Q_mg ∧ (Λ ∈ 𝒮^W)` ⟺ `𝒮^W ∩ (Λ+𝒯_abs) = {Λ}`.

*Proof.*
* (i): by (N) (G2_B9_R3, Thm N(i)), `Λ+b ∈ 𝒮` with `b ∈ 𝒯` implies RH.
* (ii): by (i), `Q_mg` holds in the ¬RH scenario, where `Λ ∉ 𝒮`. In the other direction, `Λ ∈ 𝒮` is RH, and under RH `Q_mg`
  is OPEN, so it does not follow.
* (iii): it is the definition. ∎

**Reading.** D asks whether the vertex Λ is admissible. Q_mg asks whether it is isolated in its tempered fiber. They are
orthogonal: neither answer fixes the other.

### Thm 3.2 (Carathéodory reformulation; PROVED under RH, with one CITED input)

For real `b ∈ 𝒯_abs`, let `B_b(s) := Σ_{n≥2} b_n n^{−s}`.
* `B_b` converges absolutely in `Re s > ½`, because `Σ_{n≤x}|b_n|n^{−½}` is polylogarithmic and partial summation suffices.
* It is bounded in `Re s ≥ ½+δ` and tends to 0 as `Re s → ∞`.
* As boundary values in `𝒮′`: `D_b(τ) = B_b(½+iτ) + B_b(½−iτ) = 2 Re B_b(½+iτ)`. This is the direct computation of
  `β̂_b` with `φ̂(τ) = ∫φ e^{iτu}`.

Under RH:
```
Λ + b ∈ 𝒮^W   ⟺   Re( ξ'/ξ(s) − B_b(s) ) ≥ 0   for all Re s > ½ .
```
Therefore, under RH, Q_mg (complete form) ⟺

> **(Q\*)** *There is no real Dirichlet series `B = Σ_{n≥2} b_n n^{−s}`, `B ≠ 0`, with
> `Σ_{n≤x}|b_n|n^{−½} = (log x)^{O(1)}`, such that `ξ'/ξ − B` is a Carathéodory function (real part ≥ 0) in the
> half-plane `Re s > ½`.*

*Proof.*
1. **The ξ'/ξ term.** Under RH, the paired Hadamard product gives
   `Re ξ'/ξ(½+δ+it) = Σ_γ m_γ δ/(δ²+(t−γ)²)`, the Poisson integral of `πμ_Λ`. This is standard.
2. **The B term.** `Re B_b(½+δ+it)` is harmonic, bounded for `δ ≥ δ₀`, with growth at most polylogarithmic
   as `δ ↓ 0` (trivial bound from the partial sum) and limit 0 as `δ → ∞`. By Nevanlinna in the half-plane (tempered
   growth, no linear term because `B → 0`), it is the Poisson integral of its boundary value `D_b/2`.
3. **Positivity.** `Re(ξ'/ξ − B)` is the Poisson integral of `πμ_Λ − D_b/2`. A Poisson integral is ≥ 0 throughout
   the half-plane if and only if the boundary distribution is a positive measure (Herglotz; a tempered distribution with
   positive Poisson is a positive measure).
4. **Closure.** `πμ_Λ − D_b/2 ≥ 0 ⟺ D_b ≤ 2πμ_Λ ⟺ Λ+b ∈ 𝒮^W` (R5 §8). ∎

*CITED input, only for the reading and not for the proof:* RH ⟺ `Re ξ'/ξ > 0` in `Re s > ½` (Lagarias 1999, from memory;
not used). With it, D is "B = 0 is admissible" and (Q\*) is "only B = 0".

*Why it is useful:* (Q\*) mentions no windows `T`, no `𝒮^A`, no measures on `Γ_ζ`. It is a self-contained question about
functions in the half-plane.

**Translation of Thm M.** An atom `a_γ > 0` of `D_b` corresponds to `B` having, at `½+iγ`, a boundary singularity
of simple-pole type with residue `a_γ/π ≤ m_γ`. In other words, `B` is a "fraction" of ξ'/ξ concentrated on a
subset of the zeros of positive density and proportion → 0.

### Thm 3.3 (the analogue of (Q\*) is false on the Type I curve and on the product of two curves; PROVED)

**(a) One curve.** Let `C/𝔽_q` be of genus `g ≥ 1`, with zeros `½ + iγ`, periodic of period `ω_q = 2π/log q` (Weil;
`2g` zeros per period) and measure `μ_C`. The comb lives on `{q^k}`.

For `0 < ε ≤ 1`, define `b` by:
```
b_{q^k} q^{−k/2} := −ε Σ_{j=1}^{2g} (α_j/√q)^k ,
```
and `b = 0` off the powers of `q`.

* `|b_{q^k}|q^{−k/2} ≤ 2gε`, so `b ∈ 𝒯_abs`.
* `b ≠ 0`.
* `D_b = ε(2πμ_C − 2πρ_C)`, with `ρ_C = g log q/π` the constant mean density. It is the periodic Fourier series of
  `μ_C` without the constant term.
* Then `û_{Λ_C+b} = 2π[(1−ε)μ_C + ερ_C] ≥ 0`, and `Λ_C+b` is positive for every `T`.
* `d⁺(b) = 2εg log q > 0`. It matches Thm M: `2gε ≤ 2d⁺`.

**(b) Two generators.** Let `Z = Z_{C₁}(q₁^{−s})Z_{C₂}(q₂^{−s})` with `log q₁/log q₂ ∉ ℚ`. Adding the constructions of
(a) gives `b ≠ 0` on `⟨q₁⟩ ∪ ⟨q₂⟩` with `d⁺ > 0` and `D_b ≤ 2πμ_Z`. That is, **multigenerator rigidity false at
positive density**.

*Proof.*
1. Explicit formula for the curve: the Fourier coefficients of `μ_C` at `k log q` are `Σ_j(α_j/√q)^k`, all of
   modulus 1 by Weil (CITED: Weil 1948).
2. Positivity is read off directly on the spectral side. The polar part (`q^k+1`) cancels with `N_k` inside
   `Σα_j^k = q^k+1−N_k`. That is why `b` is tempered.
3. For (b), the zero measures add and the comb supports are disjoint, except for coincidences `q₁^a = q₂^b`,
   which irrationality excludes. ∎

**Key observation.** The mechanism of Thm 3.3 has two ingredients:
* the *whole* zero measure, minus its density, is quasi-periodic with spectrum on the comb and bounded coefficients;
* there is **finite** zero density.

In ℚ, `μ_Λ − ρ` (with `ρ = (2π)^{−1}log(|t|/2π)`) has coefficients `Λ(n)n^{−½}`, which are **not** tempered, and it
also carries the polar term `2cosh(u/2)`, which is not a comb on `log ℕ`. It is the polar/integer wall from phase 150 (T5). That is
why the construction `b = −ε·(full comb)` does not transfer. But that only excludes the *full fiber*, not a
positive-density subset of proportion → 0.

### Cor 3.4 (NO-GO for field-uniform proofs; PROVED from 3.3)

Any argument for (Q\*) that uses only:
* explicit formula;
* Weil positivity;
* support on a multiplicative semigroup;
* temperedness;
* integer arithmetic (Lemma C, Thm M);

also applies to the model of 3.3(a) or (b), and there the conclusion is false. Therefore, (Q\*) needs at least one of:
* **(i)** that the zero density of ζ be unbounded, together with some law of the form "a tempered Dirichlet series
  cannot have boundary singularities on a set of zeros of positive density and proportion → 0";
* **(ii)** the non-periodicity of the zeros, in the form (LR) or in a stronger multigenerator form (zero side,
  objection P2 of R4).

**Residual self-contained lemma (OPEN; it is (Q\*) restricted to the part that 3.3 does not kill):**

> **(L-184.011)** Under RH: if `B` is a real tempered Dirichlet series in `Re s>½` with `Re B ≤ Re ξ'/ξ`, then
> the set `Γ_B = {γ : D_b({γ})>0}` has upper density 0.

By Thm M, (L-184.011) ⟹ `B = 0`, and conversely. Thus (Q\*) ⟺ (L-184.011) under RH.

Size remark (HEURISTIC): Bessel for Bohr coefficients gives `Σ_{|γ|≤X} a_γ² ≲ X` under bounded translation of
`β_b`. This is compatible with `a_γ ≍ (log γ)^{−1/2}` at all zeros. Bessel alone does not close it: I checked it by
Cauchy–Schwarz, which gives `O(X√log X)` against the lower bound `≥ cX`.

### Battery of falsifiers (grid §4), logically

| falsifier | does it satisfy the analogue statement (Q\*)? |
|---|---|
| **DH, Epstein, Ξ_a, Beurling DMV/Zhang, M_m, f_t** | Yes, **vacuously**. They have zeros off the line, and the analogue of (N) makes the fiber empty. That is why (Q\*) does not distinguish them from ζ: the statement is "RH ⟹ …". |
| **deletion, κ/finmod** | They are concrete `b`'s, not fiber models. They are excluded by Thm R′, M0, Thm M (`d⁺=0`) or Thm P (one generator). They do not falsify (Q\*). |
| **Λχ₂ (under GRH)** | Same status as ζ: analogue OPEN. The zero density is also `∼ log t`, so it does not separate. |
| **Type I curve** | **No: the analogue is FALSE** (Thm 3.3a). The product of two curves (3.3b) falsifies it with two generators. |
| **Λ̃** | Undecided. No claim: I did not check whether Λ̃ has zeros off the line. |
| **b_θ** | `b_θ − Λ` has the size of Λ and is not tempered, so it lies outside `𝒯_abs`. Does not apply. |

---

## 4. Honest verdict on D

1. **LP-152:** already DEAD (R160_M5_R1), ⟺ local RH. Out of scope under rule (b). Grid §6 item 59 should
   withdraw it.
2. **Multigenerator rigidity:**
   * reduced to a self-contained lemma, (Q\*) ⟺ (L-184.011) (under RH, PROVED);
   * NO-GO for any field-uniform proof (Cor 3.4, with the Type I falsifier from the grid);
   * **undecided**.
3. **Does not move D.** By Prop 3.1, Q_mg is vacuously true without RH and logically independent of `Λ ∈ 𝒮`. Any
   proof of (Q\*) falls into the wall "margins in the witness → 0 (Theorem M)": it is rigidity at the vertex, not admissibility
   of the vertex.
4. **Proposal for the grid:** 6F, item 59.
   * G2_B7_R5 → "reduced to (L-184.011); NO-GO as a route to D [Prop 3.1; W3 via Type I]";
   * LP-152 → withdraw (negative FACT, R160_M5_R1).
5. Row D: **OPEN**, unchanged.

---

## For the audit

1. **Thm 3.2, step 2.** The Poisson representation of `Re B_b` requires `B_b` to be tempered near the line. It is
   requested to verify the Nevanlinna theorem in the half-plane for functions with polylogarithmic growth as `δ ↓ 0`
   (the boundary is tempered in `𝒮′`) and the absence of a `cσ` term. If it fails, Thm 3.2 is left as "⟸" only.
2. **Thm 3.2, step 1.** The paired Poisson of ξ'/ξ under RH is used. Check the factor π, which is the convention
   `D_b ≤ 2πμ_Λ` of R5 §8.
3. **Thm 3.3.** Please verify:
   * the normalization `D_b = 2πε(μ_C − ρ_C)` against the coefficients `Σ(α_j/√q)^k`;
   * the constant `ρ_C = g log q/π`;
   * the sign of `b` per the convention of `u_a`;
   * that model 3.3(b) (product of two curves with distinct `q`) is only a **comb model**, not an L-function
     of a global field. If it is not accepted as a falsifier, 3.3(a) (one generator) remains, which only reproduces
     Prop S of R4 in the function field.
4. **Cor 3.4.** "Any argument using only …" is a class statement. It is rigorous for the listed ingredients,
   because the model satisfies all of them. It does not cover unlisted ingredients.
5. **Lagarias 1999** is cited from memory and is **not load-bearing**.
6. **Item 59:** confirm against the JSON part6 that `R160_M5_R1` supersedes LP-152. That is what the field
   `supersedes_or_dup` says.
