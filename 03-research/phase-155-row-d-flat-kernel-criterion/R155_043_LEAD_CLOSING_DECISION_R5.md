# R155_043 — Lead closing decision, round 5 (5a/5b) (2026-09-22)

Inputs: R155_039/042 (Birman–Schwinger, Theorem J, Lemma N, Prop G), R155_040/041 (Kreĭn extension problem). Rules as before.

## 1. Labels of record
| statement | label |
|---|---|
| KEP(T) formulated for the explicit-formula distribution g; Lemma: polar kernel has signature (1,1) | PROVED |
| Thm 1: a flat-top certificate gives an a.c. solution; strict c > 0 gives a continuum | PROVED |
| Thm 2: KEP(T) solvable ⟹ λ^W_T ≥ 0 (C_c^∞ form core) | PROVED |
| Thm 3 (dichotomy): λ^W_T > 0 ⟹ indeterminate ⟹ λ^W_T ≥ 0; **RH ⟺ KEP(T) indeterminate ∀T** | PROVED |
| Unconditional: λ^W_T > 0 for T ≤ 0.8 by Zhu (complete form) ⟹ KEP(T) indeterminate for all T ≤ 0.8 | PROVED given Zhu (cited, not re-verified) |
| Theorem C does NOT give a complete-form certificate (β ≠ (2,0); defect 5.9e−3 ≫ c); it certifies the primitive form | PROVED (correction of a loose reading; Paper 47's claims were already correct) |
| Thm 4: for finite symmetric Z, μ_Z is the unique finite positive symmetric solution (no decay/product hypothesis); thm:finZ follows | PROVED (strengthens thm:finZ) |
| Remark 2.5 of R155_014 ("Kreĭn indeterminacy for ζ") | RH-EQUIVALENT (not an obstruction to remove); P5 CLOSED as a route |
| Birman–Schwinger for (H1) | CLOSED NEGATIVE (M₊ gapless; tr M₋ = 4.495774·T; CLR unavailable in d = 1) |
| Theorem J: n₋(Γ_T) ≥ ⌈2Tτ₀/π⌉ − 1, n₋(A_∞|P_T) ≥ ⌈2Tτ₀/π⌉ − 3 (Dirichlet modes + Jensen on the concave φ + φ(τ₀²) = −C₀); vacuous on P_T at ½log3 and log 2; with the min–max upper bound, n₋ = 4.004·T + O(log T) | PROVED |
| Any T₂ in (H1) satisfies T₂ ≤ 2π/τ₀ = 0.9989426 | PROVED |
| Theorem J′ (concavity gives only ceilings) | REMARK (unformalised) |
| Lemma N (one-sided overlap formula for the shift forms); Prop G (sign forcing beyond T + max nodes) | PROVED |
| The 76 % cancellation π₁₃ = +0.1866 − 0.1410 is nodal: log 2, log 3 straddle the third zero of I(a) (1.0225 at log 2; 0.9139 at 0.62; 0.9584 at 0.65); forced-sign threshold 1.1717, log 3 misses by 6.65 %; F* has nodes ±0.3152 | DIAGNOSTIC (structure PROVED, numbers diagnostic) |
| (H1) n₋(A_∞|P_T) = 1 on (T*_{∞,P}, T₂] | HYPOTHESIS; 0 ≤ n₋(A_∞|P_{log2}) ≤ 47 PROVED |

Row-D label unchanged. Endpoint of record unchanged. No sign for ζ beyond log 2. No value of inf W at log 2 asserted.

## 2. What round 5 changed
1. The Kreĭn reading is now a theorem and an equivalence: RH ⟺ the window data of the explicit formula admit more than one
   positive extension at every width. Unconditionally true up to width 0.8 (Zhu). The finite-universe theorem (thm:finZ) is
   the determinate case, now in its sharpest form (Thm 4). This closes P5: indeterminacy is not a lever, it is RH itself.
2. The 2-plane positivity at log 2 has an archimedean explanation: the primes 2 and 3 enter with opposite signs because
   their logarithms fall on opposite sides of a node fixed by the archimedean ground state. The "why" of the cancellation is
   nodal geometry, not arithmetic. Whether the same holds for the full even Schur complement (infinitely many modes) is OPEN.
3. (H1) is bounded on both sides but not decided; exactly one negative direction is DIAGNOSTIC and can hold at most up to 0.999.
4. Correction of a loose reading in the record (not in Paper 47): only the primitive form is certified at ½log3 by Theorem C;
   the complete form there is positive by Zhu.

## 3. State of the path (R155_031) after rounds 4–5
P1 negative (edge, not primes). P2: E₇ certified; nodal mechanism found; full S_even OPEN. P3: bounds 0 ≤ n₋ ≤ 47 at log 2,
exactly-1 open. P4 closed (disjoint). P5 closed (RH-equivalent). Remaining: P6 (alignment-band arithmetic lower bound; likely
RH-equivalent — owner decision), P7 (D-HS kill tests; negatives only). New candidate from round 5: **P8 — nodal criterion for
the even Schur complement**: express S_even's positivity as a condition on the relative position of {log n} and the nodes of
the archimedean eigenvectors (Lemma N generalised to all e_{2k+1}); if the nodal pattern of the archimedean basis is explicit
(prolate-like), this is the first formulation where the prime positions enter D through a geometric inequality. Pure math,
one round.

## 4. Round 6 orders
(a) P8 as above (Lemma N for all even modes; nodal positions of e_{2k+1} vs log 2, log 3; the sign pattern of the Π_T matrix
    predicted from nodes alone; compare with the computed π_ij table of R155_032).
(b) Owner decision on P6/P7.
Scripts of rounds 3–5 live in `scripts/r3a..r5a` at the REPO ROOT (not inside the phase); recorded here for reproduction.
