# R145.000 — Blueprint, phase 145: the function-field model of the row-D frame

`R144_005`, `ROW-D-SYNTHESIS-PHASES-135-144.md` (§3 β, with the predicted answer and the acceptance test),
`R142_001` §§D.31–D.32 (frame defect theorem, Lemma D.31.4, Restatement D.32.1: Hartshorne V.1.6/V.1.8/V.1.9),
`R143_001` §D.34 (trace cone, 12.3-B4), Paper 47 §§11–12, Paper 45 §§9–11, Paper 44 (Frob_n, Sh_Z), Paper 43
(carrier, rulings). Corpus check: `CORPUS_CHECK_R145.md` (read first; reuse; do not reopen).*

Standing rules as before; here the falsifier protocol is inverted: the model is a **solved case** (Weil's
theorem), so every arithmetic statement transcribed must become a *true* statement about a curve, and every
step where the transcription breaks or the truth value changes is a finding.

## Purpose and acceptance test
**Predicted answer (recorded in advance):** on a curve `C/F_q`, Riemann–Roch on `C×C` is a theorem, so the
frame defect theorem (no `h⁰` with (a),(b′),(c)) will **fail** there — geometry has `h⁰`. The phase is judged
**only** on whether the comparison **names the ingredient** the arithmetic frame lacks, precisely enough to
scope phase 146 (α): what object plays "sections" / "linear systems", what cone plays "effective", why its
trace cone is not thin (the analogue of `s₁` is `1`), and which axiom of the arithmetic frame prevents it.
A phase that only confirms the prediction without naming the ingredient has failed.

## D.41 — The model
Fix `C/F_q` smooth projective, genus `g`, function field `F = F_q(C)`, zeta `Z_C(T)`, `ξ_C(s) := q^{gs}…`
(completed, functional equation `s ↔ 1−s`, zeros `ρ` with `Re ρ = ½` — Weil). Build, step by step and with
the same names, the frame's objects:
1. **Carrier and Weil class.** The idele class group of `F` modulo the analogue of `S`-units: `C_F ≅ Z × (compact)`
   (degree map to `Z` instead of `R`): the radial variable is **discrete**, `t ∈ (log q)Z`. `D^W_C` :=
   real functions on `Z` with decay `q^{−(1+ε)|n|}` (state the exact class). `Φ_E(s) := Σ_n E(n) q^{(s−½)n}`,
   a Laurent series in `T = q^{−s}` — **periodic in `Im s`** with period `2π/log q`. Record every place where
   discreteness/periodicity changes a statement of Paper 47 §11.
2. **Explicit formula and the form.** Weil's explicit formula for `C` (finite sum over zeros `ρ` mod the
   period); `I_∞^C(E,F) := Φ_E(0)Φ_F(1)+Φ_E(1)Φ_F(0) − Σ_ρ Φ_E(ρ)Φ_F(1−ρ)` over the `2g` zeros. Check: is it
   the intersection form on `C×C` restricted to the classes `E ↦ (divisor built from E)`? Make the dictionary
   `E ↦ D_E ∈ Div(C×C) ⊗ R` explicit (fibres `F_1, F_2`, diagonal, graphs of Frobenius powers `Γ_{q^n}` ↔
   translates), and prove or refute `I_∞^C(E,F) = −(D_E · D_F)` or the correct sign/normalization.
3. **Canonical class.** `K_C` with `Φ_{K_C} = ξ_C`: the Pólya-type kernel is now a finite Laurent
   polynomial (since `ξ_C` is a polynomial in `T` up to the factor); is `K_C ≥ 0`? (Weil: `Z_C` has
   nonnegative coefficients — the point counts — so probably yes.) `deg K_C`, `I_∞^C(K_C,K_C)`, rulings.
4. **Effective cone and the defect theorem.** `𝓔_C := {E ≥ 0}` (pointwise on `Z`). **Run Lemma D.31.4**:
   for `E' ≥ 0` and a zero `ρ = ½+iγ`, `|Re(e^{iθ}Φ_{E'}(ρ))| ≤ ½ s_C(γ,θ) deg E'` with
   `s_C := sup_{n∈Z} |cos(γ n log q + θ)|/cosh(n log q/2)`. **Here `n = 0` is in the sample set**, so `s_C ≥ |cos θ|`
   and for `θ = 0`, `s_C = 1`. Is the defect theorem's mechanism (the `s < 1` gap) present or absent in the
   model? Compute `s_C` for the zeros of a specific curve (e.g. an elliptic curve over `F_2` or `F_3`, `g = 1`,
   zeros `q^{−ρ} = α^{−1}` with `|α| = √q`) and run the D.31.10-type witness `E = tF₀ + dK_C`. Decide:
   does "no `h⁰` with (a),(b′),(c)" hold in the model or not? (Prediction: it fails — `h⁰` exists.)
5. **The geometric `h⁰` in the frame's terms.** `h⁰_C(E) := dim H⁰(C×C, O(D_E))` (or `log_q` of it) for
   integral `D_E`. Verify (a), (b′), (c) with the frame's normalization (`χ = χ(O_{C×C}) = (1−g)²`? compute
   with RR on `C×C`: `χ(O(D)) = ½D·(D−K_{C×C}) + χ(O)`). Identify **what (b′) is in the model**: `h⁰(D) > 0 ⟹
   D` effective — literally true, because `h⁰` counts sections. So the model's effective cone is
   `{D : h⁰(D) > 0}` = the cone of classes with **a section**, NOT `{E ≥ 0 pointwise}`. Compare the two cones
   in the model: is `{E ≥ 0 on Z}` strictly smaller than `{D_E has a section}`? By how much (this is the
   model's `s_C`)? **This comparison is the deliverable.**
6. **The trace cone in the model.** `t_n^C(E) := I_∞^C(E, τ_n g)`; `B4_C`; is `B4_C` (mod radical) equal to
   the section cone, the pointwise cone, or neither? Where does the Frobenius correspondence `Γ_q`
   (Euler product / multiplicativity) enter the section cone's description?

## D.42 — Naming the ingredient
From D.41.5–6, state in one labelled paragraph: the arithmetic frame's "effective" = pointwise nonnegativity
corresponds in the model to [X]; the model's effective cone (sections) corresponds to [Y]; the arithmetic
analogue of [Y] would be [Z] — an object on `C_S` / `D^W` defined without zeros — and it does / does not
exist in rows A–C (check Paper 43's presented complexes, `Sh_Z`, `H⁰_Z` of Paper 47 §13, CC's `H⁰(D) = Q ∩ 𝒪(D)`).
State exactly which axiom (A1–A9) or which structural feature (discrete vs continuous radial variable;
periodicity; finiteness of the zero set; positivity of point counts; the Frobenius correspondence as a
genuine morphism) makes [Z] available in the model and unavailable arithmetically. If [Z] is identifiable,
write the **construction problem (P145)** for phase 146: build [Z] arithmetically, or build the pairing `J`
of option α whose positivity is [Z]'s shadow.

## D.43 — Synthesis input
One page: prediction confirmed or not; the named ingredient; (P145); what T1/T2 say about it (must use the
Euler product; must be field-uniform; must fail for `Ξ_a`, `Ξ_Q`).

## Deliverables and rounds
`R145_001_ROUND1.md` (D.41 complete with the dictionary and the `s_C` computation for one explicit
curve; D.42; D.43; corpus check per idea; paper-facing; open list; label), README; audit `R145_002`,
repairs, confirmation, `R145_005`. Scripts only to compute `s_C` and point counts for the explicit curve
(`--fast`, margin).

## Warnings
* Everything in the model is classical (Weil, Hartshorne V, Serre, Hindry–Silverman for the intersection
  theory on `C×C`); cite precisely; label CLASSICAL, not PROVED.
* Do not "prove RH for curves" again; the model's job is comparison. Do not let the discrete variable hide
  a mismatch: record each one.
* The acceptance test is the named ingredient. If none can be named, say so and say why — that too decides
  phase 146.

## Corpus consequences (binding; from `CORPUS_CHECK_R145.md`)
* Reuse as PROVED-IN-REPOSITORY, do not rebuild: phase-63 `R3-VERDICT` (Frobenius / Poincaré-duality
  polarization over `F_q`); phase-125 `A125.009` (graph → `C×C` dictionary; gap: non-invertible Frobenius not
  covered — close that gap here); phase-119 `weil_case.py` (Weil-number generator; use for the explicit curve).
* Import verbatim the arithmetic side of the comparison (`s₁ = 0.99846 < 1`, R142/R144); build only the
  `F_q` side (`s_C`, section cone vs pointwise cone).
* Phase-113 doc 11 records an arithmetic sections-functor **no-go** — read it before D.42 and state exactly
  what it excludes and what it leaves open (this is where [Z] must be placed).
* MAP_5 line 12: CC 2205.01391 has no self-intersection / Hodge-index statement — confirmed gap; do not
  attribute one.
* Do not open option α (item 6) here; hand to phase 146 with the sign-corrected statement.
* Record note: the "phase-41 Doc 125 tropical toy" cited in the phase-136 map and later files
  is **not found** under phase-41 in the current tree (nearest: phase-43 doc 130 Deninger toy, circular; phase-63
  E99). Treat those citations as stale until located; do not lean on them.
* Several exact doc numbers cited by earlier phases (phase-33 docs 74/80, phase-107 doc 241, phase-39 doc
  119) are not found; phase-39 doc 120 (CC source inventory) is found and usable.
