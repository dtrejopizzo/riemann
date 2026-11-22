# R160_010: round 1, compact summary

Sources: the panel reports R160_PA..PE_R1.md, each covering a subset of memos with all five lenses.

Round 1 has 18 memos. M11 was not written and M12 is partial; both are deferred. **No memo reached G1 or G2.** No
memo was accepted as complete. The highest score was 3/10 (C3).

## Verdicts
| memo | status | score | fatal point for the objective | what survives (new, correct) |
|---|---|---|---|---|
| C1 lamination | PARTIAL_NEW | 2 | Thm Z: with one pole, at most one pair of L²-zeros (OT-1/OT-2 fail) | Thm P (holomorphic polarization without compactness), Prop Φ, Thm R, Thm Z, Cor Z2/Z3, Thm S |
| C2 prolate boundary triples | PARTIAL_NEW | 1.5 | Thm E: every extension is prime-free, archimedean only; Thm A(iv) FALSE (not load-bearing) | 4-torus of 𝔉-invariant extensions, Weyl functions, Thm C zero-blindness |
| C3 Meyer H¹ | PARTIAL_NEW | 3 | sign = off-line part 𝔬 = 0 = E1; Thm H: every continuous Θ-compatible positive form has the off-line blocks in its radical | Thm A (I = J unconditionally), Thm B (H¹_alg dense), Thm C (Hodge ⋆ continuous), Thms D, E, G, H |
| C4 Witt / W(R) | RESTATEMENT | 0.15 | the "Coulomb identity" is Weil's archimedean term | Thm A, Prop C.4 (negative) |
| C5 genus extremality | PARTIAL_NEW | 0.3 | every positivity statement is EQUIV or void | — |
| C6 Sh_Z | PARTIAL_NEW | 0.35 | the sign step is RH | Thm Q: B_∞(T₀) ⟺ RH (bookkeeping) |
| C7 Huh / Doc 125 | PARTIAL_NEW | 0.35 | (HR-T) is RH; "Problem 25.13 solved" overstated | — |
| C8 ε-phase | RESTATEMENT | 1 | Thm 1 holds verbatim for Λχ₂ and Ξ_a; Thm 5 has a margin | — |
| M1 Problem B family | PARTIAL_NEW | 0.3 | surviving branch = E3 | Thms L, Σ: both candidates of prob:B dead |
| M2 variational | PARTIAL_NEW | 0.3 | 𝒱_T and V*_T are prime-blind (the same for Λχ₂) | Thm 4.5 |
| M3 Thm A at large T | PARTIAL_NEW | 0.2 | the target is E1; Prop 5's inference does not follow | — |
| M4 polar capacity | PARTIAL_NEW | 0.4 | the residual is E5, O-1 is E2 | Thm A (radical), Thm B, Prop E (separates ζ from the comb models) |
| M5 Gaussian correlation | PARTIAL_NEW | 0.1 | LP-152 is a dead class; the identities hold for DH/Epstein/Ξ_a | Prop 3.3 |
| M6 self-scale | PARTIAL_NEW | 0.2 | O-M6.1 is E1 on the odd box | Thm D (a correction of the record), Thm E |
| M7 bilinear | RESTATEMENT | 0.07 | Thm 4 is eq:form rewritten | Thms 1–3, 5 (operator calculus, notation) |
| M8 two-variable Schur | PARTIAL_NEW | 0.15 | the plus sign is the sign of a square, so the form is sterile | Thm A, B(iii), Prop C, Thm D (negative) |
| M9 amplification | PARTIAL_NEW | 0.08 | no form and no sign | Cor A1 |
| M10 Doob / CD(0,∞) | PARTIAL_NEW | 0.22 | O1 = RH | T4 (curvature cap ¼), Lemma 4.1 |

## Structural lesson of round 1
The panel's most frequent objection: **every identity holds verbatim for Λχ₂, Ξ_a, DH or the comb models.** The
routes that failed never contained a line that uses a ζ-specific datum (P47 T2: A3 together with A7/A8/A9;
unimodularity; the exact Λ(2)).

On the object side, two theorems pin down what a future carrier must violate:
* C1 Thm Z: holomorphic flows with one pole carry at most one pair of zeros;
* C3 Thm H: continuous Θ-compatible positive forms are blind to off-line zeros.

A carrier must therefore be **non-holomorphic up to isotopy (a failure of Torelli)** or carry a **non-homogeneous
positivity**. Neither class has a candidate on record.

## Round 2 (5 memos): routes chosen
| id | route | source |
|---|---|---|
| D1 | construct a Torelli-failing Hodge-preserving lamination (the first non-excluded carrier), or prove the lamination Teichmüller lemma that closes the Deninger–Singhof L² route | C1 OS-1, PA lead 1 |
| D2 | construct a NON-homogeneous positive structure on Meyer's H¹ (the exact hypothesis Thm H says an object must violate), with the transfer clause to W_T | C3 Thm H, PA lead 2 |
| D3 | the exact per-window converse for ζ at T > 0.8: under RD_T, W_*(Y_1) ≥ ⟨(𝔞_T\|P_T)^{-1}b_T, b_T⟩, radical-based | M4 O-2, PC lead 1 |
| D4 | a separating-datum mechanism: a positivity statement whose load-bearing line provably fails for Λχ₂, Ξ_a, DH and the comb models at once (P47 T2: A3 + A7/A8/A9, unimodularity, exact Λ(2)) | the structural lesson above |
| D5 | the spectral picture of A_T on L²(I_T): λ₀ = −(1+o(1))e^T, F*_T → φ_ev (pole/Perron direction); then the second eigenvalue on the complement, where the sign lives | PB lead 3 |
