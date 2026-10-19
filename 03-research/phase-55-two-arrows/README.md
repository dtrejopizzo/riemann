# Phase 55 — Two arrows: structural representation and dynamics of the off-line energy I

The phase pursues two complementary programs for the off-line energy $I(0^+) = \sum_j b_j^2$
(RH $\iff I = 0$): Problem A, representing $I$ as a natural arithmetic/analytic functional so that its
finiteness becomes a membership question rather than a zero-localization question; and Problem B,
studying the forward/backward de Bruijn–Newman dynamics of $I$ directly (coercivity, collision budget,
takeoff rates) without attempting to prove positivity.

## Results
- Shadow–signal obstruction (Doc 173, Thm 173.A): in any class of holomorphic zero-sum representations,
  the quadratic weight on $b^2$ is forced to be integrable (no admissible constant or $1/\gamma$ weight
  reachable), explaining the $T/\log T$ ceiling as intrinsic to holomorphy: PROVED.
- Green–Littlewood identity (Doc 173, Thm 173.C): an exact unconditional identity expressing $I(T)$ as
  an area integral of $\log|\zeta|$ over the half-band plus a boundary flux term: PROVED.
- Membership formulation (Doc 173, Prop 173.E): RH $\iff$ a Green-potential $L^2$ norm is finite, but
  the norm is degenerate (only takes values $0$ or $\infty$) because of infinite self-energy of the
  zero atoms: PROVED, identified as an obstruction rather than a solution.
- Non-coercivity of the de Bruijn–Newman dissipation (Doc 174, Prop 174.1): an explicit isolated
  quadruple configuration shows $D \ge cI$ fails for any constant $c$: PROVED (counterexample); the
  document maps which dynamical properties can and cannot carry a proof of finiteness of $I$ in the
  pure Pólya class (general class counterexamples exist; any proof needs the arithmetic initial data
  of $\zeta$).
- Energy dichotomy (Doc 175, Thm 175.2): the self-approximation property LP-112 of $\zeta$ implies
  $I \in \{0, \infty\}$, with an unconditional quantitative rate on how rare the witnessing
  self-approximations are: PROVED CONDITIONAL on LP-112 (an open hypothesis from an earlier phase);
  gives a strictly weaker architecture $\mathrm{RH} \Leftarrow (I < \infty) \wedge \mathrm{LP\text{-}112}$
  than the earlier cardinality-based one.
- Attack on Problem A via Green–Littlewood (Doc 176): the half-band integral's Cesàro mean is shown to
  always converge unconditionally, turning Problem A into the finiteness of a provably-existing limit,
  with RH corresponding to the exact value $-\pi/8$: PROVED (classical machinery, new exactness of
  statement); an explicit unconditional lower bound on the sign is given, while the matching upper
  bound remains exactly Problem A: OPEN.
- Hermite takeoff constant (Doc 177): decides GAP-174.B by computing the exact self-similar
  (Hermite-polynomial) backward takeoff profile of a multiple real-zero collision, refuting the
  conjectured constant $2k$ for cluster size $n \ge 3$ and replacing it with an exact value: PROVED.

## Documents
- `173-structural-representation-of-sum-rules.md` — Problem A: shadow–signal obstruction and the Green–Littlewood representation.
- `174-coercivity-forward-extinction-and-the-backward-structure.md` — Problem B: coercivity counterexample and dynamical map.
- `175-energy-dichotomy-lp-112-i-0.md` — the energy dichotomy conditional on LP-112.
- `176-attack-on-problem-a-via-green-littlewood.md` — Cesàro-limit reformulation of Problem A.
- `177-gap-174-b-decided-the-hermite-takeoff.md` — exact Hermite takeoff constant, closing GAP-174.B.

## Relation to other phases
Builds on the balance law and energy envelope of `phase-54-index-dynamics`; its open gaps (LP-112, the
upper bound in the Cesàro-limit reformulation) and its backward-dynamics map feed `phase-56-two-towers`.
