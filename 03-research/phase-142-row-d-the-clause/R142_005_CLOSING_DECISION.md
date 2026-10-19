# R142.005 — Closing decision, phase 142 (the clause (b′)⁺ and the frame defect)

R142_002 (audit: D.31.12 STANDS; 0 FATAL), R142_003 (ledger), R142_004 (confirmation: all repairs in
place; §D.32 audited, J1–J10). Independent checks: closed-form recomputation of the witness (`R(E) = 10.006`,
`t|Φ_{F₀}(ρ₁)| = 199.7248 > 199.6920`, `W_F = 9π` exactly, rulings `200 ± 10⁻³⁹⁰`), `s₁ = 0.99846016…` at
`u* = 0.11099`; Paper 46 record note entered at Theorem 12.3; ASCII map `ROW-D-MAP-b.md`.*

## 1. Result of record

**Theorem D.31.12 (given (X19): `ρ₁` simple and on the line).** No function `h⁰` on `D^W` satisfies
(a), (b′), (c) of Paper 46 Theorem 12.3 for `ξ`, for any `χ`. Hence Theorem 12.3's hypothesis is
unsatisfiable; the theorem keeps its label and loses its use. Same for every admissible `Z` with a simple
isolated on-line zero (`ξ_K` verbatim). Mechanism: Lemma D.31.4 (cosh bound for effective classes,
`s(γ,θ) < 1`) against `h⁰ ≥ R` on `deg > 1` forced by (b′) + Thm 11.13 + (c) + Serre symmetry; explicit
witness of degree 400. Computer-assisted only through (X19); simplicity of `ρ₁` is load-bearing
(at multiplicity 2 the refutation fails).

Also of record: (C4.1) FALSE; `C_X` of Thm 11.14(ii) is the support function of the effective cone
(`≤` half); Beurling–Malliavin row cross-referenced to phase-33 doc 85; O-17 stays closed; O-18 closed
negatively; D.31.14(i) withdrawn (aligned rays only); D.31.2(ii) completeness withdrawn to CLAIM.

## 2. Diagnosis (Restatement D.32.1, confirmed with Hartshorne V.1.6/V.1.8/V.1.9, Lazarsfeld §2.2)
The arithmetic frame transports the Hodge-index half of surface theory with the geometric constant
(`I_∞(E,E) ≤ (deg E)²/I_∞(2K,2K)`), and fails the effectivity half (`D² > 0, D·H > 0 ⟹ nD` effective)
with deficit exactly `s(γ,θ) < 1`: it keeps the intersection theory of `C×C` and discards its linear
systems. Effectivity as pointwise nonnegativity of one radial density is too thin a cone.

## 3. The two horns, as audited
* **Horn A** (weaken (c)): Thm 12.3 invokes (c) exactly once, at degree 0 (partner degree 1), and (b′) at
  degrees 0 and 1; so a defect `Δ` with `Δ(0) = Δ(1) = 0` leaves the proof intact and the `¼m²` growth
  survives. Strongest admissible `Δ(d) = max(0, (d²/4)(1 − s_*²) − d/4)`. The degree gate fails (c′) at
  `E = dK`; the (★)-gate satisfies (c′) only under RH — the blocker is **O-18′** (sufficiency half of the
  moment problem), not the small circularity (A3). J1: gate by *primitive* test classes.
* **Horn B** (enlarge effectivity): Thm D.32.4 reduces any candidate cone with `deg > 0` and finite
  bounded-density constant to the single inequality `C'_{F₀} ≥ G` (equality suffices, J4). Candidates
  B1 (`G ⋆ G^∨`), B2 (`Φ ≥ 0` on the line), B3 (hull of translates of `K`), B5 (completions) fail or gain
  nothing. **B4 = classes with nonnegative Frobenius traces**: J3 shows the whole witness family lies in
  B4 (`t_n(E) ≥ (d − 2tG)√(Φ_g(0)Φ_g(1)) > 0` since `2tG = 399.45 < 400`), so **B4 passes the D.32.4
  test**; it is the only candidate reading A8. Caveats (J2): B4 ⊇ `𝓝_∞`, so (T1) must be read mod `𝓝_∞`;
  `𝓔 ⊂ B4` is unproved and probably false (B4 is a *different* cone, not an enlargement).

## 4. Decision
Phase 142 closed; row D label unchanged; the phase-135 formulation is retired as a route. Phase 143
order (auditor's, adopted): **(0) settle O-19** — compute `s_* := inf_{γ,θ} s(γ,θ)` over the zeros (is it
`0`? that is a third outcome gating both horns); **(1) Horn B / B4** — first the decidable zero-free
question *is there a primitive `F ∉ 𝓝_∞` with `t_n(F) ≥ 0` for all `n`?* (yes kills the horn; no is a
theorem), then (T2) for B4 and a transfer theorem 12.3-B4; **(2) Horn A** carried as secondary with the
primitive gate and O-18′ named as its blocker. Paper-facing: record note at Thm 12.3 entered; §D.31–D.32
as Paper 46 Part III material (P46-26…); the (X19) import.
