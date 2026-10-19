# Paper 45 — Row C: the explicit formula on row A's declared carrier

**Files.** [main.tex](main.tex) / [main.pdf](main.pdf) — the paper of record.
[main.md](main.md) — the older working draft; its numbering (9.4, 9.6, 9bis.2′,
10.4, …) and some of its material are **not** in the tex. Every theorem
number below is a **tex** number. Repair log:
[REPAIRS.md](REPAIRS.md).

## Status

* **Label.** `ROW C: WEIL-STRENGTH-COMPLETE` on the declared carrier, granted
  in phase 132 (R132.007; PLAN.md). The earlier README line "label not
  claimed" referred to round 2 of phase 132 and is superseded.
* **Clause C.2** is met in a **reinterpreted** form only: the two Tate terms
  are the functionals `M = (λ_-, λ_+)` into the hyperbolic plane `(B_T, β_T)`,
  and the polar packet is `β_T(M,M)`; no cohomological (Meyer-type)
  realization is built or used. This is now stated in the tex (paragraph
  "How clause C.2 is met", §2).
* **Adversarial audit ** (`AUDIT_44_45`): row C closes. Citation defects
  D-C1 (Haar of `C_S` vs local measure), D-C2 (duplicated `log p`), D-C3
  (dangling citation), D-C4 (over-citation of Paper 44) repaired; the
  archimedean term is stated for sign-even tests in line with Paper 43's
   convention. No theorem statement changed.

## Main results (tex numbering)

| Result | Content |
|---|---|
| Lem 4.2 | trace of a radial class (Thm A) |
| Thm 7.1 | polar packet `2Φ_F(0)Φ_F(1) = β_T(M,M)` (with the ruling swap) |
| Thm 8.4, Cor 8.5 | the explicit formula, proved without moving a contour across zeros (Thm B) |
| Lem 9.2, Thm 9.3 | comparison: `I_∞(Γ_F,Γ_F) = β_T(M,M) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ)` in the colimit, and at a fixed chart inside the window (Thm C) |
| Cor 9.4 | `c = 0` is the unique constant for which the identity holds (Thm D) |
| Thm 9.6 | limit symbols (exact eventual constancy) |
| Thm 10.3, Cor 10.6, Prop 10.7 | Tate residues: `|S_f|+1, 0` at a chart, `1, 1` in the continuation (Thm E); Mertens import |
| Thm 11.3 | primitive tests suffice (Thm F) |
| Thm 12.2 | `𝒩_∩ = 0` on the radial sector at a fixed chart (Thm G) |
| Appendix (E1)–(E8) | named classical inputs |

## md/tex divergence (flagged)

Not in the tex, so not to be cited as results of Paper 45: the form
`B_nuc` and the identity `I_A([K_F],[K_G]) = B_nuc(F,G)`, the clause ledger
(§14 of `main.md`), the withdrawal ledger (§13), the distributional
Theorem 9.6′ and the remarks 9bis.2b/9bis.3 of `main.md`.

## What this paper does not claim

No sign and no positivity statement; no statement on the location of zeros of
`ζ` beyond the explicit formula and the sufficiency argument of §11.

## Numerical record

[`verify_132_explicit_formula.py`](../../03-research/phase-132-row-c-closure/scripts/verify_132_explicit_formula.py)
— 26/26 checks (illustration only; no proof uses it).

## History

Phase-132 status blocks and the  readability note are in git
history; construction and audit records in `03-research/phase-132-row-c-closure/`.

* **Alignment with repaired Paper 43.** Citations of Paper 43 use its
  repaired tex numbering (Conv 6.6, 6.11; Thm 6.7; Thm 11.6; Mertens = Thm A.1,
  auxiliary appendix). No result of this paper depends on the hypothesis
  (Exc_σ) of Paper 43; see REPAIRS.md.
