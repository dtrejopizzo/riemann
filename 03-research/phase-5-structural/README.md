# Phase 5 — Structural comparisons and the arithmetic-invariant classification program

Starting from the Kreĭn-space template of phase-4, this phase asks two kinds of question: (i) how
does the P8-style operator relate to the Connes–Consani archimedean angular operator and to the de
Branges structure-function framework (same obstruction, or genuinely different objects)? and (ii)
can a per-prime "anatomy" decomposition of the localized Weil margin yield an arithmetic invariant
that separates RH-consistent from RH-violating L-functions, independent of zero positions?

## Results
- Connes–Consani comparison: both $K_{\mathrm{P8}}$ and $K_{\mathrm{CC}}$ instantiate the same
  abstract Kreĭn positivity template, but admit no natural zero-independent unitary identification;
  P8's no-go does **not** transport to the Connes residual, leaving it a live attack surface:
  PROVED/ARGUED (panel-revised wording).
- De Branges comparison: the chain-of-subspaces mechanism gives the same Kreĭn template via a
  different route; its positivity certificate is itself equivalent to the sign question, and
  proposed unconditional substitutes were historically REFUTED (Conrey–Li); the de Branges chain
  ordering matches P8's height/Nyquist sampling ladder: ARGUED (structural observation only).
- Semi-local Connes residual (B2): the prolate-function bridge is superficial between CC and the
  global band-limited setting but real between CC and the localized (Hermite–Gauss) detector P7;
  the semi-local residual positivity is the genuine open frontier and band-limited tools can at
  best sharpen, not close, the operator-norm estimate: ARGUED/OPEN.
- M5 classification program: proves the "tautology objection" is already resolved on the
  construction's own terms (T1), giving a path of theorem-targets T1–T4 for an arithmetic invariant
  built from Euler/Γ-factor data: PROVED (T1, T2 anti-tautology/forced-transition results) /
  CONDITIONAL and OPEN for the remaining targets.
- Anatomy theorem (T3): exact decomposition of the localized Weil margin into an archimedean term
  and per-prime contributions, with gradient = anatomy density: PROVED. Deeper structural statements
  about the profile are OPEN.
- Phase 2 (anatomy vs Euler factor): to leading order the anatomy profile factorizes as
  $R_p \approx a_p W(\log p)$ (largely a reparametrization), but higher-frequency corrections probe
  the full local factor and factorizability itself tracks the Euler product (one direction PROVED;
  the converse is a CONJECTURE, not proved).
- T4-seed: two genuine structural inequalities (a Bessel/Carleson frame bound; concavity and
  monotonicity of $\lambda_{\min}$ in prime masses with an extremal reduction) that are natural in
  anatomy coordinates and opaque in $\{a_p\}$: PROVED; neither breaks the sign barrier.

## Documents
- `B3.1-connes-comparison.md`, `B3.2-de-branges-comparison.md` — comparisons to Connes–Consani and de Branges.
- `B2-semilocal-residual.md` — the semi-local residual and prolate-bridge question.
- `M5-classification-pure-theory.md`, `M5-T1-T2-proofs.md` — the classification program and its first proved theorems.
- `T3-anatomy.md`, `Phase2-Rp-Euler.md`, `T4-seed.md` — the per-prime anatomy decomposition and its structural content.
- `experiments/` — numerical engines and results (`M4-D2-results.md`, `Phase3-results.md`) probing the margin and anatomy profile.

## Relation to other phases
Builds directly on `phase-4-handoff` (the Kreĭn template, P8/Thm C no-go, P7 localized detector);
feeds the classification program (M5) that continues in later phases.
