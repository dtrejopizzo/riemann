# R147.005 — Closing decision, phase 147: the Galois group ring as the missing `+`

`R147_002` (audit R1: ACCEPT WITH REPAIRS, 6 MAJOR), `R147_003` (round 2 + Corrections D1–D20),
`R147_004` (audit R2: Part A ACCEPT, Part B 7 MAJOR), `R147_003b` (round 3, document of record for
Part B), `R147_004b` (confirmation: ACCEPT with C1–C7; final corrections ordered, see §5).*

## 1. The question and the answer

**Question:** the missing ingredient of row D is an additive ring of correspondences
(the `+`) that `Spec Z` does not have (phase 146). Can `Z[Gal(K/Q)]`, acting on `Spec O_K × Spec O_K`,
supply it?

**Answer: yes on the graded carrier, and it changes nothing at the zeros of `ζ`.** Three theorems carry
the decision.

1. **Collapse on the radial carrier** (Lemma D.50.2, corrected M4 of R147_002 → "the radial realization
   `R(Γ_σ) = id` on `D^W`"). `PROVED`. Every `σ ∈ Gal(K/Q)` preserves the idele modulus; the frame's Weil
   carrier `D^W` consists of functions of `log|x|` alone; hence every Galois correspondence acts as the
   identity there and `Z[G]` acts through its augmentation. The cone, the intersection numbers and the
   `h⁰` candidates of Papers 46 §§11–19 do not see `G`. `Ξ_a`-uniform (no `G`).
2. **The graded carrier supplies the `+`** (`R147_003b` §R3, Theorems D.55.2′–D.55.8′). `PROVED`,
   unconditional for abelian `L/F`. On `𝒟_L = ⊕_χ D^W ⊗ C` graded by conjugate packets (phase 139
   D.20.2, finding H5), with `I^{(K)}(E,F) = Σ_χ I^{[χ]}(E_χ, F_χ̄)`, the form is bilinear, symmetric and
   real; `Γ_σ` acts by `(χ(σ))_χ`, is an isometry, and `I(Γ_σE, Γ_τF) = Σ_χ χ(στ⁻¹) I^{[χ]}(E_χ,F_χ̄)` —
   the blueprint's formula, with the character table entering the intersection numbers exactly as
   predicted. The correct cone `𝓒` is the isotypic image of nonnegative `C_c^∞(R × G)` tests: it is
   `Z[G]`-stable, satisfies the degree gate (degrees and rulings live only in the `χ = 1` slot, because
   `Ξ_χ̄(1−ρ) = 0`), strictly contains `ι(𝓔^∞)`, and contains classes with coordinate `χ(g) = −1` — the
   exact arithmetic analogue of the model's `[Γ_i] = ½[Γ_π] − ½[Δ] − F_1 + F_2` on `E/F_5`. Its support
   function is `S(γ,θ,m) = max_{k<m} s(γ, θ − 2πk/m)`, `m = ord χ`, and `σ(γ,m) := min_θ S < 1` for every
   finite `m` (lower bounds `0.99846 (m=1) → 0.99961 (m=4) → 0.99996 (m=12)`; `d₀` thresholds `324.96 →
   ≥1294 → ≥11313`, grid values are lower bounds).
3. **The `G`-invariant sector is the trivial slot** (Theorem D.55.9′, restated per `R147_004b` C1: the
   `χ = 1` slot of `𝓒` is exactly `𝓔^∞` because `f_1 = Σ_g f(·,g) ≥ 0`). `PROVED`. Consequently, at
   every zero of `ζ_F` the support-function constant is `s(γ,θ)`, unchanged, for every abelian `L/F`, every
   tower and every `m`. The frame defect theorem (Paper 46 Thm 19.23) for `ξ` stands verbatim.

**Reading of record.** The `+` exists, is built, and lives entirely in the non-trivial isotypic sectors,
i.e. at the zeros of the `L(s,χ)`, `χ ≠ 1`. The zeros of `ζ` live in the `G`-invariant sector, where the
group ring acts trivially. This is the round-1 collapse seen one level up: norm-one translations commute
with the radial projection. **The Galois ring cannot move the sign of `ζ`. Thread closed on the negative,
by Theorem D.55.9′ alone.**

## 2. What was refuted, withdrawn or corrected (record)
* Blueprint expectation "the character table enters the intersection numbers" — REFUTED on `D^W`
  (collapse), CONFIRMED on `𝒟_L` (packet grading). Both stand, on different carriers.
* Round-1 "discovery" `K ∈ 𝓔` — already Paper 46 Def–Thm 11.7(i); withdrawn as a result.
* "Effective class with zeros right of 1 via Epstein" — replaced by the trivial witness
  `E = 3e^{−t²} + e^{−(t−log 2)²}` (`Φ_E` vanishes on `Re s = ½ + log 3/log 2`); the Epstein grid is
  illustration only; O-47.2 closed (R139_004 H4).
* "Kills the horn *enlarge the effective cone*" — non sequitur, withdrawn (the horn is about the support
  function).
* "First support function in row D to reach 1" (`S(γ,π/2,m) = 1` for `4 | m`) — withdrawn: `s(γ,0) = 1`
  always (Paper 46 (19.2)); the statement says only that the `μ_m`-orbit of `π/2` meets `πZ`, the
  direction the defect theorem never uses. FATAL flag raised and cleared on this ground.
* "The defect theorem may choose `θ`" — withdrawn; no `L(s,χ)` analogue of Def 19.19–Thm 19.23 exists
  (O-47.7).
* `dim H⁰ ≤ 1` on `𝒟_L` and "multiplicity is the missing object" — downgraded to a remark and withdrawn
  as a slogan; `(Z[G]E)^G` is not (4a)'s sections functor.
* `cos(π/m)` lemma — value is `cos(π/m)` (`m` even ≥ 4), `cos(π/(2m))` (`m` odd ≥ 3), argmin `d/2`.
* `deg K_L = 1` over any base — false (`deg K_{Q_𝔄} = ½`, imaginary quadratic); C2.
* Epstein (Theorem D.55.10): the principal Epstein class is the trace `t(Γ_{𝔄⁻¹}K_{H/K})` of a graded
  class under a non-isometric projection; `t(𝓒) ⊆ 𝓔` (M6 corrected), and `K_H ∉ closure(𝓒)` (PROVED for `x²+ky²`, `k` large; CERTIFIED for the listed `D`). This is where the Epstein falsifier belongs: a sum of `L`'s, not a product.
* By-product (CLASSICAL-RESTATEMENT): `Σ_{σ≠1} #Fix(σ) = log|d_K| = Σ_χ χ(1) log 𝔣(χ)` (Hilbert's
  different formula + conductor–discriminant); character table enters through conductors, not zero sums.
* F-147-1: closed form (145.10) of phase 145 needs an `n = −1` exclusion; the record curve is unaffected.

## 3. Falsifiers
* `Ξ_a`: no Galois structure; `𝒟 = D^W`; everything collapses to round 1. The construction separates
  `ξ_L` from `Ξ_a`, but by D.55.9′ the separation is invisible at the zeros of the trivial slot.
* `Ξ_Q`: Theorem D.55.10 — the Epstein class is not in `𝓒`; it is the trace of a graded class.
* `ζ_K`: uniform in towers (constant unchanged at a fixed zero; monotone in the divisibility order).

## 4. What remains open (not closed by this phase)
* **O-47.7** — the `χ ≠ 1` sectors: a `ζ_F`-frame theorem consumes all zeros of `ξ_L = ∏_χ Λ(s,χ)`, so
  the enlarged constants `σ(γ,m)` at `L`-zeros *would* matter to a transfer theorem for `ζ_L`; and there
  is no `L(s,χ)`-analogue of Thm 19.23 (its witness `F_0` is odd, tied to `θ = π/2`).
* **O-47.8** — non-abelian `L/F` (`χ(1) > 1`; D.20.2 conditional on Artin holomorphy there).
* **O-47.1′** — an explicit formula on the genuinely non-radial sector of `C_{F,S}` beyond the finite
  abelian quotients (Hecke characters of infinite order).
* **O-47.3′** — (4a) on `𝒟_L`: whether any sections functor with `m²`-growth exists on the graded carrier.

## 5. Row-D consequence and next step
Phases 145–147 have now named and tested the missing ingredient three times: `Spec Z` has no ring of
correspondences (146); where a ring exists (Galois), it is invisible on the radial carrier (147.1); where
a carrier sees it (graded), it acts away from the zeros of `ζ` (147.3). The obstruction is stable under
every enlargement tried: **the sign of `ζ` lives in the `G`-invariant, radial, trivial-character sector,
and every additive structure available from Galois theory acts trivially there.** Any further "more
correspondences" proposal (Hecke, Borger, `F₁`, CC) must first show it does not commute with the radial
projection; the phase supplies that test.

Final corrections C1–C9 (`R147_004b`) applied and verified by the blueprint (D.55.9′ now has a numbered
statement and complete proof in `R147_003b` §R3.3; `deg K_L = 1` restricted to `F = Q`; `K_H ∉ closure(𝓒)`
proved/certified by route). This decision is unconditional. No label in the corpus changes. Row D: **no label, no sign**.
Recommendation: pause construction here; the next phase, if any, should attack O-47.7 (a defect
theorem for `L(s,χ)` in a `θ`-family) only if a `ζ_L`-frame theorem is judged worth having, or
close row D at the map and record Phases 134–147 in Paper 46 Part IV.
