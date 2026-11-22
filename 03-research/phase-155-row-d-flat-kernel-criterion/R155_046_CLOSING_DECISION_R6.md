# R155_046 — Closing decision, round 6 (6a: nodal criterion P8)

Inputs: R155_044 (amended per R155_045). Rules as before.

## 1. Labels of record
| statement | label |
|---|---|
| Prop N1: ground state of Γ_T on L²(I_T) simple, strictly positive (pure-jump Dirichlet form + killing) | PROVED |
| Prop N2: {e^{±u/2}} Chebyshev system ⇒ every nonzero F ∈ P_T changes sign ≥ 2 times (cause of "F* ≥ 0 refuted") | PROVED |
| Thm N3: K completely monotone ⇒ log-convex ⇒ not PF₂ ⇒ Karlin oscillation route closed for the kernel; semigroup t ≥ 1 OPEN; p_t ≍ |x|^{t−1} | PROVED (kernel half) / HEURISTIC (semigroup) |
| Thm N4 (even sector): λ^{even}_{k+1}(A_∞|P_T^{even}) ≤ m((2k+3)π/2T) = log k + O(1) | PROVED |
| Arena corollary: N*(T) ≥ ⌊Tτ_*/π − ½⌋; N* ≥ 12 at log 2, ≥ 2 at ½log3 (lem:mbounds(ii) at exact frequencies); N*(T) ≳ 2Te^{A_T}/π, doubly exponential in T | PROVED |
| Consequence: no fixed finite truncation in the archimedean basis decides the even Schur complement; E₇ sits inside a ≥ 12-mode arena — the structural reason for the R155_032 withdrawal | PROVED |
| Sign rule from nodes: 100 % of |J| ≥ 0.10 entries (88.7–95.9 % of mass), failures on the small near-cancelling ones; k-th even mode has k nodes, interlacing (k ≤ 8) | DIAGNOSTIC / CONJECTURE N-Sturm |
| Nodal criterion for the FULL S_even | NOT ATTAINABLE by this route (log-slow tail); P8 CLOSED as a route, kept as a diagnostic law |

Row-D label unchanged. Endpoint unchanged. No sign for ζ beyond log 2. No value of inf W at log 2 asserted.

## 2. What round 6 established
The obstruction at log 2 lives in an arena of at least twelve even archimedean modes (doubly exponential in T), because the
archimedean gaps grow only like log k while the prime form is bounded and non-compact. The nodes of the archimedean basis
decide the dominant signs of the prime matrix; the arithmetic content sits exactly in the small entries the nodes leave
undecided. Together with rounds 4–5: positivity at log 2 = a cancellation among ≥ 12 modes, nodal in its coarse structure,
arithmetic in its fine structure, never term-by-term, never finite.

## 3. State of the path after rounds 4–6
P1 negative (edge). P2 partial (E₇ proved; full S_even infinite-dimensional by N4). P3 bounded (0 ≤ n₋ ≤ 47 at log 2; T₂ ≤ 0.999).
P4 closed. P5 closed (RH-equivalent). P8 closed as route. Remaining: P6 (alignment-band arithmetic lower bound 
decision; likely RH-equivalent), P7 (D-HS kill tests — negatives only), and the one live analytic lever named by three
rounds independently: an explicit **prolate concentration floor** for the archimedean form (a lower bound on how much
spectral mass a window-supported F must carry above τ₀), which would (i) sharpen n₋ to the true value, (ii) give the first
class-dependent LOWER bound (Problem A) on the archimedean form, (iii) bound the arena from above.

## 4. Round 7 orders (pending Decisions on P6/P7)
(a) Prolate concentration floor: literature (Landau–Pollak–Slepian, Bonami–Karoui explicit bounds — import into 00-references),
 then the theorem for the archimedean symbol via the concave φ: a floor needs a spread bound of |F̂|² beyond τ₀ for
 F ∈ P_T, i.e. an uncertainty inequality on the window with the Tate constraints. Pure math.
(b) Consolidation: Paper 46 now 51+ pp.; a TeX review R2 of the whole paper before any further additions.
Scripts of rounds 3–6 live at repo-root `scripts/r3a..r6a`.
