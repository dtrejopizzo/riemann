# Phase 105 — A1 geometry and the Deep limit

## Objective

Make the surviving RH-equivalent targets visually and algebraically
unambiguous before opening another proof mechanism.

The phase starts from two distinct statements:

\[
 J_n(T_n)\le q_n\qquad(n\ge150)                           \tag{A1}
\]

and

\[
 \Omega_X\longrightarrow0.                               \tag{Deep}
\]

A1 is a family of barriers indexed by (n). Deep is a literal limit.
Either one, with the exact bridges inherited from Phases 103--104, is
sufficient to close RH. Neither is assumed.

## Documents

| Document | Role |
|---|---|
| `105_00_A1_AND_DEEP_LIMIT_VISUAL_MAP.md` | visual definition of A1, the forbidden region, the Deep limit, and what is actual data versus a theorem scenario |
| `105_01_PRIME_ZERO_A1_PIPELINE.md` | intuitive causal map from the prime staircase to the signed Laguerre area, the critical-line frequencies and the off-line exponential mode |

| `105_02_OFF_LINE_ZERO_EXPONENTIAL_THEOREM.md` | exact quartet law and global proof that any off-line zero forces exponential growth in the full Li sequence |
| `105_03_BLOCK_SPECTRAL_RADIUS_THEOREM.md` | exact \(L^2\)-scale block spectral radius, its RH equivalence, and the coupled ordinary-prime selector identity |
| `105_04_PREFIX_COMPRESSION_AND_DELTA_TARGET.md` | lossless reduction from all sign selectors to consecutive prefixes and the exact \(\Delta\)--Laguerre inequality; records the Sturm and Hardy residue stop-gates |
| `105_05_NODAL_FLUX_AND_BREGMAN_RESONANCE_GATE.md` | exact free-boundary flux formula for the BSY negative mass; the smoothed hinge reduces every nonlinear crossing cost to \(O(\log R/\delta)\), while a positive VK-scale atomic falsifier isolates the surviving literal-Mangoldt non-resonance term |

## Reproduction

```bash
cd 03-research/phase-105-a1-geometry-and-deep-limit
python3 tools/a1_limit_visualization.py
python3 tools/prime_zero_a1_pipeline.py
python3 tools/off_line_quartet_check.py
python3 tools/fir_window_bank_check.py
```

This creates

* `assets/a1_and_deep_limit.svg`;
* `assets/prime_zero_a1_pipeline.svg`;
* `assets/a1_and_deep_limit_data.csv`.

The PNG is rendered from the SVG with ImageMagick and is not an
independent computation.

## Status

Phase 105 has started. The figure is explanatory and diagnostic. It is
not a finite verification of A1 and is not evidence that the unknown part
of the cumulative integral remains below its barrier. The zero-side
implication

\[
 \neg\mathrm{RH}\Longrightarrow
 \limsup_n|\lambda_n|^{1/n}>1
\]

is proved in `105_02`. The prime-side subexponential bound remains open.
Document `105_03` sharpens the block formulation to

\[
 \lim_{L\to\infty}
 \left(1+\sum_{n=L^2}^{L^2+L-1}|\lambda_n|\right)^{1/L^2}
 =\max\left\{1,\max_\rho\left|1-\rho^{-1}\right|\right\}.
\]

It also expresses the block norm as an exact supremum over signed
Laguerre selectors against the coupled continuum--von-Mangoldt
discrepancy. Therefore a bound \(\exp\{o(L^2)\}\) is precisely equivalent
to RH; the uniform literal-prime selector estimate is the remaining
unproved step. Document `105_04` compresses that selector without
exponential loss: it is enough to control the \(L\) consecutive prefix
sums. After exact Abel summation, the surviving target is

\[
 \max_{0\le j<L}\left|
 \int_0^\infty
 \bigl(L_{L^2+j-2}^{(3)}(u)-L_{L^2-3}^{(3)}(u)\bigr)
 \left(\gamma-u+\sum_{m\le e^u}\frac{\Lambda(m)}m\right)du
 \right|=\exp\{o(L^2)\}.
\]

This estimate remains unproved and is equivalent to RH. The natural
Sturm energy and Hardy/outer boundary norms do not supply it: both lose
exactly the interior-zero residue.

Document `105_05` studies the same obstruction through the zero-free Euler
approximants.  It proves the exact nodal-flux identity

\[
 \int(-u_R)_+d\nu={1\over2\pi}\int_{\Re L_R=0}
 \log\left|{s\over s-1}\right||\partial_sL_R(s)|\,d\mathcal H^1(s),
\]

and an exact smoothed-hinge bound.  The complete Bregman crossing cost is
only logarithmic, but the adaptive linear correlation can still resonate
at size \(\exp\{R/2-\eta(R)\}\).  A positive atomic countermodel realizes
that loss while retaining a VK-scale PNT envelope and logarithmic quadratic
variation.  Hence the next input must be a non-resonance inequality using
the literal values \(\Lambda(p^k)=\log p\); positivity, PNT, renewal and
quadratic variation do not imply it.
The FIR/window development is written as Paper 38 in
`04-papers/38-li-fir-stability/main.tex`; its exact algebraic checks are in
`tools/fir_window_bank_check.py`.
