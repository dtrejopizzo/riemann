# Phase 179 — The common-radical chain gate

Phase 178 showed a connected scalar correlation retains orientation but has no fixed sign, while a
full covariance has a sign but no orientation. This phase tests the remaining proposal: make the
"exterior Tate port" the boundary map of a genuine two-term chain complex (an Euler differential and
a Poisson/divisor-incidence differential glued by a transmission map), so that the desired vanishing
law would follow automatically from the algebraic identity "boundary of boundary = 0."

## Results

- Chain-gate identity (Theorem 1): the square of the total (mapping-cone) differential has a single possibly-nonzero off-diagonal block equal to d_C L₁ − L₀ d_P; it vanishes exactly when the transmission maps L₀, L₁ satisfy a chain-map equation — **PROVED**.
- Nilpotence is not automatic from merely adjoining the divisor-incidence complex: defining L₁ to force the desired physical identity does not imply the chain-map equation, and conversely imposing the chain-map equation on the range of d_P leaves the kernel (where the first-contact vector lives) unconstrained (Proposition 2) — **PROVED**; naive total-complex construction is **NO-GO**.
- The pure affine factor-swap (order-two cocycle) alternative is cohomologically trivial: every such cocycle is a coboundary, removable by recentering, so it supplies no new sign-bearing invariant unless the recentering also preserves the physical fiber, which an earlier result (R170_876) shows it does not — **PROVED** (Theorem 3); this branch is closed.
- The canonical Koszul–Clifford/Bochner-superconnection realization of the required maps (from phase 114) is audited and shown not to prove the chain-map equation: its Real-trace component reduces to the same open anti-invariant sign already identified in phase 114 — **REFUTED** as a route to CG1–CG2.
- Falsifier/orientation checks: the construction is correctly selective against finite modifications and Davenport–Heilbronn (no compatible Euler incidence anchor), and against the discrete Beurling system P₁₇₁ (no ordinary additive Poisson differential) — **PROVED**; unlike a Laplacian the construction retains orientation, which was Phase 178's gap.
- Overall status: the pre-spectral construction of transmission maps L₀, L₁ satisfying the chain-map equation and the physical-identification equation is the single remaining open object; **OPEN**. Row D / the vanishing law R_L F = 0 remains **OPEN**.

## Documents

- `R179_CHAIN_GATE.md` — the chain-gate identity and its proof, the first-contact specialization, the affine-cocycle triviality theorem, the audit of the phase-114 Koszul–Clifford/superconnection realization, falsifier tests, and a final status table.

## Relation to other phases

Direct continuation of phase 178 (addresses its stated necessary condition); cites phase 170 (R170_866/869/876) for the divisor-incidence differential and the physical odd boundary law, and phase 114 for the Koszul–Clifford/Bochner-superconnection construction it rules out.
