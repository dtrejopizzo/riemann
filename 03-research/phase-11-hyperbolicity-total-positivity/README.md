# Phase 11 — Hyperbolicity, Jensen polynomials, and stable-polynomial machinery

The phase tests a route new to the programme: the Pólya–Jensen criterion recasts the target as real-rootedness
(hyperbolicity) of the Jensen polynomials J^{d,n} built from the Taylor coefficients of Ξ(t)=ξ(½+it), and asks
whether modern stable-polynomial and interlacing machinery (Marcus–Spielman–Srivastava, Borcea–Brändén) — which
proves real-rootedness without an apparent quadratic-form positivity — can escape the "wrong-sign capstone"
found in earlier phases (that every unconditional handle on the problem is a lower-bound-oriented positivity,
while the target needs an upper constraint).

## Results
- M11.1 (referenced as the grounding computation): working numerical verification of hyperbolicity for small Jensen polynomials. NUMERICAL.
- M11.2: the Jensen polynomials of Ξ interlace in both shift and degree directions throughout the tested range, meeting the precondition for the MSS largest-root machinery; the correct underlying positivity is identified as total positivity of a Toeplitz matrix built from the coefficient sequence b(k)=(-1)^k a(k) (a Pólya-frequency-sequence condition), not Hankel/quadratic-form positivity as first (incorrectly) tried. NUMERICAL / corrected characterization.
- M11.3: the Jensen shift n→n+1 corresponds to differentiation of Ξ, a Borcea–Brändén stability preserver that preserves the Laguerre–Pólya class for any such function, not specifically for ζ; a control comparison against cos(t) (a non-arithmetic Laguerre–Pólya function) shows the same interlacing/hyperbolicity behavior, demonstrating the preserver mechanism is arithmetic-blind. PROVED/ARGUED (arithmetic-blindness).
- M11.4–M11.5 (decisive test): real-rootedness of each Jensen polynomial is exactly the positive-semidefiniteness of its Hermite (Hankel power-sum) form; the MSS interlacing method itself rests on real-stability of determinants built from PSD matrices (Borcea–Brändén). So the apparently "positivity-free" interlacing mechanism is PSD-founded at root. PROVED (equivalence to Hermite-form PSD). Numerically confirmed positive-definite at d≤4 (d=5 entries dismissed as numerical artifacts of ill-conditioning, cross-checked by direct root-finding in M11.1).
- Final verdict: the wrong-sign capstone holds even in this, the most modern paradigm tested — hyperbolicity reduces to a positivity (total positivity / real-stability / Hermite form), so the route does not escape the capstone. NO-GO (route does not cross the capstone).
- Durable byproducts: the identity b(k)=m_{2k}/(2k)! linking Jensen coefficients to even moments of the de Bruijn–Newman kernel Φ; a reformulation of the target as total positivity of a Pólya-frequency sequence / real-stability in the Borcea–Brändén/MSS language; explicit identification of the preserver's arithmetic-blindness and the PSD foundation of the method. PROVED/ARGUED as stated.

## Documents
- `PLAN-RH-PHASE11-hyperbolicity-route.md` — the Pólya–Jensen reframing and rationale for why this route might escape the capstone.
- `M11.2-verdict-interlacing-total-positivity.md` — interlacing structure and the corrected total-positivity characterization.
- `M11.3-verdict-preserver-blind-MSS-pivot.md` — the shift preserver and its arithmetic-blindness, with the cos(t) control.
- `M11.4-5-verdict-capstone-holds-richest-positivity.md` — the decisive Hermite-form equivalence and final capstone verdict.
- `experiments/` — scripts computing Jensen polynomials, interlacing tests, the shift-preserver comparison, and the Hermite-form capstone test.

## Relation to other phases
Explicitly framed as the eighth of several independent tests of the same "wrong-sign capstone" found in earlier phases (including the cohomological route of phase 10); confirms the capstone from what the documents describe as the most sophisticated angle tried to that point.
