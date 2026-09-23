# R152.005 — Lead closing decision, phase 152 round 0 (two never-analyzed non-positivity mechanisms)

*Lead: Fable 5.1, 2026-09-19. Record: `R152_000`, `R152_001` (feasibility), `R152_002` (hostile audit). Labels below
govern.*

## 1. Verdicts of record

**Headline (auditor, accepted): "no route found; no impossibility proved."** The builder's DEAD verdicts are
overstated on both sides.

| item | label | basis |
|---|---|---|
| A. Prop A.1 (Maass–Selberg gives exactly the absolute-convergence region = MW-2) | PROVED | |
| A. Prop A.2 (Riemann–von Mangoldt density on `Re s = ¼` defeats any Bourgain–Dyatlov gap `β > ¼`) | PROVED but **non-binding**: `β = ¼` *is* RH and `β < ¼` a quasi-RH; the mechanism asks the right question and has no machinery (δ = 1, cusp, `P(½) > 0`) | `R152_002` |
| A. **Prop A.4** (Gauss-map branch series `Σ n^{−2s}` has abscissa `Re s = ½`; on `(¼,½)` the transfer operator exists only as Mayer's meromorphic continuation; the *branch-sum* Dolgopyat route dies) | **PROVED — best result of the round**; "MW-2 in dynamical form" | |
| A. Cor A.5 (UNI not even stateable on `(¼,½)`) | **WITHDRAWN** as overreach: on the disc Banach space `L_s` is a holomorphic nuclear family, `‖L_s^n‖` and `det(1−L_s)` are well posed, a Dolgopyat-shape bound is stateable; no theorem can forbid it without disproving RH | `R152_002` |
| A. Q3 (Hecke non-concentration of resonant states `E*(z,ρ/2)`) | asserted by builder; auditor's independent obstruction: for `σ ≠ ½` the Hecke eigenvalue `p^{σ−½±iτ}` is unbounded in `p`, so entropy/temperedness arguments lose their hypothesis exactly in the case to be excluded — **OBSTRUCTION (argument, not theorem)** | |
| A. Corpus: "phase 16 Route A covers this" | **OVERSTATED**: doc 01 has the `s = ρ/2` dictionary; doc 05's negative-definite pairing `K_{ρσ} = 1/(s_ρ + s̄_σ − 1)` is a pairing statement, not a resonance gap | |
| B. Dictionary B.1 (`{k log p}` = integer points of the `p`-branches of `M(Z)`) | RESTATEMENT (record in Paper 44 as a remark) | |
| B. Prop B.2 (tree energy of the atomic measure is test-function-independent) | PROVED, vacuous | |
| B. Prop B.3 (a tree pairing is a function of the meet, the Weil form of the difference; tree potential theory is per-branch and blind to the cross-place coupling) | **PROVED, scoped to trees** — kills `M(Z)`, not `A^{1,an}_Z` | |
| B. Q6 ("no Frobenius" via Thm 22.17) | **CATEGORY ERROR** as argued (Thm 22.17 is about schemes; `End(M(Z))` contains the exponent flow); conclusion likely right, to be re-proved in the right category | `R152_002` |
| FATAL | not triggered (two checks) | |

**Row D: no label, no sign.**

## 2. What the round leaves formulated (new to the corpus, not restatements)

* **(P152.1)** A Dolgopyat-shape bound for the *continued* Mayer operator on `Re s ∈ (¼, ½)` via the Lewis–Zagier
  three-term equation `ψ(x) = ψ(x+1) + (x+1)^{−2s}ψ(x/(x+1))`: a uniform-in-`|t|` contraction estimate for
  `L_s^n` on the disc space would give a resonance-free strip, i.e. a zero-free strip for `ζ(2s)`. Gate: fails
  the archimedean gate g3 as stated (the Gamma factor is invisible to the three-term equation). Status: an honest
  open problem of the right logical shape (upper bound, non-positivity), with no method; FATAL rule if claimed.
* **(P152.2)** A difference kernel on the Berkovich line `A^{1,an}_Z` (a group object with a genuine archimedean
  fibre), so that Prop B.3's hypothesis fails and the Weil kernel could be an energy there. **Cheap decisive
  test**: does the constructed measure `μ_f` notice a Beurling system (Euler product without `+`)? If not, it
  is blind to the `+` and cannot carry the sign (T3-type gate). Status: a construction question, one round.
* **(P152.3)** Hygiene: re-prove "no Frobenius on `M(Z)`" in the analytic category.

## 3. Decision

Phase 152 round 0 **CLOSED**: no route to the sign found; no impossibility proved; Prop A.4 and Prop B.3 are the
results of record; (P152.1)–(P152.3) recorded as open. The two mechanisms are the first non-positivity
candidates in the corpus that survive a hostile pass as *open problems of the right shape* rather than as
restatements — but with no method attached. **Recommendation:** run one bounded round only on the cheap test of
(P152.2) (Beurling blindness), and record (P152.1) in Paper 46 §28.3 as an open item; do not open a construction
phase on either without a method. Paper 46 §28.4: no new reopening clause. Paper 44: one remark (Dictionary B.1).
