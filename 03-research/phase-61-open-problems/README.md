# Phase 61 — Open problems: closing the CCM reduction chain down to the wall

This phase takes the CCM (Connes–Consani–Moscovici) spectral-triple reduction of RH built in
phase-60 and works systematically through its twelve-step proof outline, closing every RH-neutral
(unconditional) loose end with finite, named work, while isolating exactly which step is equivalent to
RH itself. A large bank of numerical experiments (`E10`–`E96`) backs each closure, and several rounds of
outside mathematical review (`respuestas-matematicos.md`, `respuesta4.md`, correspondence with named
mathematicians) independently confirm which pieces are closable and which are not. A companion detector paper
and open-problems inventory track the state of each sub-problem.

## Results
- O1 (archimedean normalization), O2 (tail beyond the horizon), O3 (boundary amplification / harmonic
  measure): CLOSED, with fully explicit, reproducible proofs (term-by-term Tate-constant
  identification; a uniform incomplete-gamma tail lemma; an explicit harmonic-measure evaluation).
- O4 (archimedean = scattering, no closed orbits, Step 10.3): CLOSED modulo a named standard input
  (Birman–Krein spectral shift / Duistermaat–Guillemin trace formula for a non-trapping symbol),
  upgraded from "argued" to a rigorous argument citing standard scattering theory.
- O5 (uniformity of the spectral gap, Step 2 — the central knot together with O11): the raw
  perturbative routes (archimedean-skeleton perturbation; free Dirichlet box with sine eigenmodes) are
  REFUTED by explicit counterexamples and numerical mismatch. The correct limit operator is identified
  via a Doob transform (dividing by the positive ground state), whose Mosco limit is the Dirichlet
  Laplacian on $[0,\pi]$ with weight $\sin^2\theta$, giving eigenvalue ratios $k(k+2)$: PROVED modulo one
  isolated technical lemma (2.3.F, a scale-free Feshbach/Schur-complement convergence statement),
  verified numerically to high precision (gap ratios matching $(k+1)^2$ to percent-level accuracy across
  λ ∈ [7,21]); the raw-moments route is shown NOT to work by counterexample.
- O6 / O6-bis (closed form and fine oscillation law of the prolate overlap integral $I_n(L)$): CLOSED
  with full proof (exact Jacobi-matrix identity; stationary-phase derivation of the asymptotic law via
  Meixner–Pollaczek orthogonal polynomials), verified numerically to relative error $\le 3\times10^{-4}$.
- Step 2.3.F-Loc (bounded-coefficient closure of the intrinsic Jacobi operator): shown to be RH-neutral
  (an unconditional statement about the positive Doob-transformed operator $G_\lambda$, independent of
  the sign of $\varepsilon_0$); three new attack fronts (intrinsic Lanczos, spectral-zeta/heat-trace,
  Liouville–Green) each give positive numerical confirmation of the bounded-coefficient, quadratic-band-edge
  mechanism; the band-edge closure (Doc R10) proves the limiting ratio law for the averaged bulk
  coefficients with Dirichlet ends: PROVED (unconditional) for the averaged model, NUMERICAL confirmation
  for the full intrinsic operator.
- Outside review (`respuestas-matematicos.md`): an independent mathematician, after verifying the cited CCM
  and Connes–van Suijlekom source theorems are real and say what is claimed, confirms the same
  division — O1–O3 fully closable, O4/O6/O7 closable with named standard inputs, O11's functional-analytic
  content can be stated precisely, but explicitly refuses to "close" O5 (full uniformity), O9, or O10,
  identifying O10 ($\varepsilon_0 \ge 0$ for all λ) as exactly the Riemann Hypothesis and proving instead,
  rigorously, why the program as stated cannot reach it from the marginality theorem alone.
- Overall state: steps 1, 3, 4, 5, 6, 7, 8, 10 proved/closed; step 2 proved at finite λ (numerical
  uniformity) with the remaining rigorous gap isolated to Lemma 2.3.F; steps 9 and its sub-parts largely
  closed; steps 11 and 12 remain OPEN, with step 12 ($\varepsilon_0 \ge 0\ \forall\lambda$) identified as
  the exact RH-equivalent wall of the whole construction.

## Documents
- `OPEN-PROBLEMS.md` — the master inventory of open sub-problems (O1–O12) against the twelve-step chain.
- `WALL-EULER-LEMMA.md` — precise statement of the remaining wall via the quaternionic/Deninger structure, for external review.
- `R9_three_new_fronts_RESULTS.md`, `R10_bandedge_closure.md` — the Lanczos/spectral-zeta/Liouville-Green fronts and the band-edge closure of Step 2.3.F-Loc.
- `respuestas-matematicos.md`, `respuestas3.md`, `respuesta4.md` — independent outside mathematical review of which sub-problems are genuinely closable.
- `RH-PROOF-PAPER.md`/`.tex`/`.pdf`, `DETECTOR-PAPER.tex`/`.pdf` — consolidated write-ups of the chain and the numerical detector.
- `E20`–`E96` scripts, `detector_engine.py`, `engine_cache.py`, `_build_high.py` — the numerical engines backing every closure and measurement above.
- `papers-cierre-2.3/` — reference papers (prolate/Slepian, Meixner–Pollaczek) used in the O6/2.3 closures.

## Relation to other phases
Directly continues `phase-60-discriminant`'s CCM reduction chain and three-part audit; the isolated wall
(step 12, $\varepsilon_0 \ge 0\ \forall\lambda$) is the same RH-equivalent core identified by the
phase-60 audit, now sharpened to a single scalar sign question.


Also present: `E87b_prime_mechanism.py.bak`, a backup copy of an earlier version of the E87b script.
