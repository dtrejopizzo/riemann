# Phase 70 -- Lee-Yang / de Bruijn-Newman heat-flow forcing of Omega_7

**Opened:** 2026-07-07. Direction suggested by arXiv:2511.11199 (RH as DQPTs) -- specifically its
Lee-Yang analogy, which the paper notes but does not exploit for a proof.

## The idea (a forcer, not a restatement)

Statistical mechanics has THEOREMS (Lee-Yang circle, Lieb-Sokal) that FORCE partition-function zeros
onto a curve by POSITIVITY. Applied to zeta, this is the de Bruijn-Newman framework:

```
Xi_lambda(t) = integral e^{lambda u^2} Phi(u) cos(t u) du,   Phi = the Riemann kernel,
Xi_0(t) = Xi(t) = xi(1/2 + i t).
```

`Xi_lambda` has ONLY real zeros iff `lambda >= Lambda` (de Bruijn-Newman constant). Facts:
- de Bruijn: all zeros real for `lambda >= 1/2`.
- Newman: threshold `Lambda` exists, `Lambda <= 1/2`.
- **RH <=> Lambda <= 0** (since `Xi_0 = xi`).
- **Rodgers-Tao 2018: Lambda >= 0.** Hence **RH <=> Lambda = 0**.

This is a genuine forcing mechanism: the heat flow (`lambda` increasing) is a Lee-Yang deformation that
DRIVES zeros to the real axis. It is distinct from Hilbert-Polya (spectrum) and Bost-Connes (KMS).

## Connection to our Omega_7

Our gauge-free terminal object (E69.1): `Omega_7 <=> Im N(z) >= 0 on Im z > 0 <=> all z_rho real <=>
xi in Laguerre-Polya`. The de Bruijn-Newman heat flow is exactly the dynamics that forces that reality.
The closure question:

> Does the terminal defect `A_N - P_lambda` (or `Im N`) have a MONOTONICITY under the heat flow that,
> combined with `Lambda >= 0` (Rodgers-Tao), forces `Lambda <= 0` -- hence `Lambda = 0` = RH?

If the flow improves the defect positivity monotonically and Rodgers-Tao pins `Lambda >= 0`, the closure
lives at the meeting point `Lambda = 0`.

## Plan

1. **E70.1** Build `Xi_lambda(t)`; verify the dBN picture (zeros real for `lambda >= 0`; complex pairs
   form for `lambda < 0`), via real-zero counting in a window vs `lambda`.
2. **E70.2** Nevanlinna under the flow: `N_lambda = -Xi_lambda'/Xi_lambda`; test whether `Im N_lambda`
   is MONOTONE in `lambda` (the heat-flow improves positivity) -- the forcer's monotonicity.
3. **E70.3** Connect to the exact terminal defect: is `ind_-(A_N - P_lambda)` monotone under the flow?
   A monotone-to-0 flow + `Lambda >= 0` would be the forcing structure.
4. **Falsifier:** a planted off-line zero must correspond to `Lambda > 0` locally; the flow must NOT
   remove a genuine off-line zero at `lambda = 0` if it is there.

## Closure document

- [OMEGA7_CLOSURE_PROGRAM.md](OMEGA7_CLOSURE_PROGRAM.md) — post-Phase-70 synthesis: the complete
  proof architecture for closing `Omega_7`, reducing the remaining work to the arithmetic q-resolvent
  / Herglotz majorization identity.
- [E70_3_QRESOLVENT_IDENTITY_RESOLUTION.md](E70_3_QRESOLVENT_IDENTITY_RESOLUTION.md) — resolves the
  q-resolvent identity: it is exactly finite `Omega_7` unless an independent Euler/Gamma/fusion
  evaluation of the resolvent trace is supplied.
- [E70_4_AHM_WEIL_REDUCTION.md](E70_4_AHM_WEIL_REDUCTION.md) — pushes AHM to its exact mathematical
  endpoint: Cauchy-Weil positivity, i.e. Weil positivity on Cauchy test squares.
- [E70_5_HARDY_AUTOCORRELATION_FORM.md](E70_5_HARDY_AUTOCORRELATION_FORM.md) — rewrites the remaining
  AHM/Weil statement as a concrete Hardy autocorrelation inequality sampled at `log n`.
- [E70_6_PARTIAL_SUMMATION_BARRIER.md](E70_6_PARTIAL_SUMMATION_BARRIER.md) — attacks the Hardy-Euler
  inequality by partial summation and isolates the exact RH-strength prime-error cancellation estimate.
- [E70_7_GLOBAL_CANCELLATION_REQUIREMENT.md](E70_7_GLOBAL_CANCELLATION_REQUIREMENT.md) — rules out the
  per-prime/local-positive route; AHM must be proved by global cross-prime cancellation.
- [E70_8_ABEL_BOUNDARY_LOSS.md](E70_8_ABEL_BOUNDARY_LOSS.md) — Abel-regularized Euler positivity
  reduces to critical boundary stability, again equivalent to the missing `Lambda<=0` direction.
- [E70_9_WIENER_HOPF_FACTOR_TARGET.md](E70_9_WIENER_HOPF_FACTOR_TARGET.md) — formulates the remaining
  constructive proof shape: a non-circular Euler-Gamma cross-term factorization
  `A-T_Lambda=D^*D`.
- [E70_10_DIRICHLET_SQUARE_OBSTRUCTION.md](E70_10_DIRICHLET_SQUARE_OBSTRUCTION.md) — tests the naive
  Dirichlet-shift square and proves it manufactures Euler ratio-comb terms `log(n/m)`; any viable
  factor must cancel the Euler square by a grading/quotient rather than by an ordinary Hilbert square.
- [E70_11_MOBIUS_CONNECTION_IDENTITY.md](E70_11_MOBIUS_CONNECTION_IDENTITY.md) — replaces fitted prime
  coefficients by the canonical identity `V_Lambda = Z^{-1}delta Z`, i.e. `Lambda = mu * log` inside
  the semigroup shift algebra; the remaining open theorem becomes Euler-Mobius connection
  dissipativity relative to the Gamma/polar form.
- [E70_12_RICCATI_CURVATURE_TEST.md](E70_12_RICCATI_CURVATURE_TEST.md) — computes the Riccati identity
  `delta(Z^{-1}delta Z)+(Z^{-1}delta Z)^2=Z^{-1}delta^2Z`; it closes the internal Euler curvature but
  shows that the missing sign is exactly the Gamma-Euler dissipativity theorem.

## Honesty contract

Carried from Phase 67-69. The dBN framework is real and active (Rodgers-Tao); the NEW work is connecting
its monotonicity to our terminal defect. No fabricated closure; audit the audits. If the flow gives only
`Lambda >= 0` again (the known half), say so -- the closure needs the other half (`Lambda <= 0`).
