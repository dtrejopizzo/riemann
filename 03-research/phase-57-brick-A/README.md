# Phase 57 — Brick A: the desingularized Dirichlet energy and barrier #4

The phase attempts one specific unexplored route named in phase-55/56 (Doc 173's successor idea) to
improve the unconditional second-order energy bound $E(T) \ll T/\log T$ (rung 176.P1 / GAP-180.1): the
desingularized Dirichlet energy $\mathcal D_R(T) = \iint |\zeta'/\zeta|^2$ of $\log|\zeta|$, excluding
small disks around the zeros, hoping that the positivity of this energy (unlike the earlier
sign-blind moments of $\log|\zeta|$) could isolate the off-line signal $\sum b^2$.

## Results
- Exact desingularized Green-energy identity (Theorem 183.1): the regularized self-energy of each
  zero in the Dirichlet energy is $2\pi\log(1/R) + O(1)$, essentially the same for on-line and off-line
  zeros: PROVED.
- Self-energy is blind to the off-line height b at first order (Prop 183.2): the off signal
  $\sum b^2$ is only a subleading correction, drowned by the total zero count: PROVED — identifies why
  the route fails to improve the envelope.
- Boundary/interior asymmetry does not survive (Prop 183.3): the hoped-for distinction between on-line
  (boundary) and off-line (interior) zero contributions is only an O(1) constant, not an order of
  magnitude, so it cannot separate the off-line mass: PROVED (refutes the phase's working hypothesis).
- Unconditional Selberg anchor (Prop 183.4): the second moment of $\zeta'/\zeta$ is unconditionally
  controlled only for σ > 1; on the critical line it anchors via Selberg's classical second-moment
  theorem, but that does not control the self-energy term needed here: CITED/stated.
- Overall verdict: the route escapes the earlier "sign blindness" obstruction (barrier from Doc 180)
  because the Dirichlet energy is positive, but falls into a new, structurally different obstruction
  ("population blindness": every zero counts equally regardless of its distance from the line),
  named barrier #4 of the Phase A wall: NO-GO, with the exact bound reproduced as $E(T) \ll T/\log T$
  (no improvement). The minimal residual statement needed to go further — a renormalization weighting
  zeros by $b^2$ rather than uniformly — is isolated as GAP-183.1: OPEN.

## Documents
- `183-desingularized-dirichlet-energy-identity-the-selberg.md` — the full construction, the exact identity, and barrier #4.

## Relation to other phases
Attacks the pivot left open by `phase-56-two-towers` (GAP-180.1); its outcome (barrier #4, GAP-183.1)
is reviewed in the full audit of `phase-58-full-audit`.
