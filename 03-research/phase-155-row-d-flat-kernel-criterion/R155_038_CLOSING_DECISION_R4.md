# R155_038 — Closing decision, round 4 (4a/4b/4c) and corpus synthesis

Inputs: R155_031 (corpus synthesis, PATH-TO-D), R155_032/036 (even Schur at log 2), R155_033/037 (Problem A on the
archimedean form; (H1)), R155_034/035 (Li dictionary), R155_030 (arXiv novelty check). Rules as in R155_010/018/029.

## 1. Labels of record
| statement | label |
|---|---|
| W_{log2} positive definite on E_k = span{e₁,…,e_{2k−1}}, k ≤ 7, certified minima 3.42e−2 … 6.57e−6 (interval Cholesky); E₅ at 0.62, 0.65 | PROVED (machine-verified). Finite-dimensional subspaces only. |
| Schur coupling b = P_V Π_T F* is purely prime; Π_T = −Σ v_n Re(R_T τ_{log n} R_T), not compact; |π_ij| ≤ A_T, row-ℓ² ≤ A_T² | PROVED |
| π₁₃ = +0.187 − 0.141 (atoms 2 and 3 cancel 76 %); with atom 2 alone the 2-plane is indefinite | DIAGNOSTIC |
| **Any numerical value of inf W at log 2 (e.g. "≈10⁻⁶", "≈10⁻⁷") — WITHDRAWN**: Rayleigh–Ritz upper bounds unstabilised in N (k=8: 9.94e−7 at N=18 vs 3.38e−5 at N=36; bottom falls with N). Caveat propagated to R155_023/026/029 and Paper 46. Theorem C's ½log3 lower bound unaffected. | WITHDRAWN |
| Theorem AL (lattice sampling of a flat-top certificate is (D)-feasible with loss O(M^{−r}); hypothesis: C^{r−1} contact at 2T⁺ and w → 1 at U⁻) | PROVED |
| Cor AL′: at fixed w the lattice is not the deficit; the deficit is the continuous problem, non-attained (thm:O, v = 0 included): the primes are not necessary for the obstruction | PROVED (as restated) |
| "D = O(M⁻²) refuted; D ≍ M⁻¹"; V_r ↑ ∞ | DIAGNOSTIC |
| Theorem R∞ (Δ_∞ = Δ − 2A_T), valid where λ^{∞,P} > 0 | PROVED |
| Prop NC: n₋(A_∞|P_T) ≤ 68.51·T (37/47/54 at ½log3/log2/0.80) via time–band limiting; prolate count 4/5/5 | PROVED (bound) / DIAGNOSTIC (prolate count); (H1) n₋ = 1 stays HYPOTHESIS |
| Thm L1: λ_n = Σ_ρ Φ_n(γ_ρ), Φ_n = 1 − cos(nθ) ≥ 0, w_n = −½e^{−|u|/2}L_n′(|u|) | PROVED |
| Thm L2: w_n ∉ W_T ∀ n, T (ŵ_n ≥ 0; decay exactly e^{−|u|/2}; no flat top); sharp: divergent prime sum, λ_n is the zero half only | PROVED |
| L4a: the {2,3} sub-comb Li sequence is eventually positive (unconditional); L4b: under RH it differs from λ_n by o(n log n) | PROVED / PROVED under RH |
| Li positivity numerics "almost entirely archimedean" (n ≲ 10⁵) | INTERPRETIVE |
| Nyman–Beurling ↔ dual certificates | HEURISTIC; no theorem; P4 CLOSED as a route |

Row-D label unchanged. Endpoint of record unchanged: λ_min(A_{½log3}) ≥ 8.8577e−5. Proved value at log 2 in one direction (thm:w11)
and positive definiteness on E₇ (this round). No sign for ζ beyond log 2; no value of inf W at log 2 is asserted.

## 2. What round 4 established about the construction of D
1. At log 2, positivity is certified on the first seven even archimedean modes; the obstruction is never captured by a fixed
 number of modes — the Galerkin bottom always sits at the last mode of the truncation. The obstruction is infinite-dimensional
 in the archimedean eigenbasis (consistent with thm:O / the edge mechanism), and the 2-plane positivity already needs the
 76 % cancellation between the atoms of 2 and 3. Positivity at log 2 is made by the primes cancelling each other, in the
 direction the archimedean form leaves open.
2. Problem A: the lattice is never the deficit (Theorem AL); the deficit is the continuous edge problem, present with no
 primes at all (thm:O with v = 0). A class-dependent LOWER bound with a rate does not exist by the route tried;
 D ≍ M⁻¹ is the diagnostic target.
3. Li/Keiper is a termwise-positive kernel outside the flat-top class; it certifies nothing per window and the Li
 analogue of Theorem SC fails for a normalisation reason (m⁻¹ subcritical vs m^{−1/2} critical). Papers 36 and 47 are
 now in one language and the answer is "disjoint".
4. Corpus synthesis (R155_031): phases 154–155 are a new coordinate system on the phase-136 wall (Theorem Z makes a
 certificate = ψ(x) − x ≪ x^{½+ε}, wall W4); what is new is that the wall is finite and decidable per window, located in
 [2πe^{2T}, 2πe^{A_T}], with the proved role flip of the primes at T*_{∞,P}. Remaining work is arithmetic.

## 3. Path (from R155_031 §4, updated by round 4)
P1 Problem A lower bound: STRUCTURAL NEGATIVE recorded; only the M⁻¹ rate remains as a target (diagnostic).
P2 even Schur complement: PROVED on E₇; obstruction infinite-dimensional — next is an analytic identity for S_even's
 ground state, or acceptance that finite truncations cannot close it.
P3 (H1): bound 68.51·T proved; exactly 1 needs a Birman–Schwinger count with the variable symbol m — one round.
P4 Li dictionary: CLOSED (disjoint classes).
P5 Kreĭn indeterminacy for ζ; P6 alignment-band arithmetic lower bound (likely RH-equivalent); P7 D-HS kill tests (negatives).
Round 5 orders: (i) Birman–Schwinger for (H1) with explicit T₂; (ii) analytic structure of S_even at log 2 — express the
Schur complement on the even sector as A_∞ + (prime shifts) − (rank-one prime coupling) and look for an identity that
makes the atom-2/atom-3 cancellation structural rather than numerical (the "why" of the 76 %); (iii) P5 Kreĭn
indeterminacy as a theorem (turns finZ into a dichotomy); (iv) Decisions on P6/P7.
