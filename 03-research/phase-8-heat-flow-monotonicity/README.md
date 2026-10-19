# Phase 8 — Heat-flow monotonicity: the de Bruijn–Newman Coulomb gas as a dynamical attack

The phase asks whether the de Bruijn–Newman heat flow, viewed as a Coulomb gas on the zeros coupled to
the program's band-limited Carleson detector, can supply a Lyapunov-style dynamical argument for RH
(the critical line as a stable attractor). It triages three outside suggestions (PT-symmetry/Hilbert–Pólya,
lattice/SVP geometry, noncommutative-geometry entropy), builds a seed numerical coupling, proves a clean
monotonicity theorem, and then attacks the hard (backward-in-time) direction down to its sharpest
quantitative form.

## Results
- Triage of three outside suggestions: PT-symmetry/dissipative Hilbert–Pólya is identified as the
  already-known Hilbert–Pólya wall in different dress; lattice/SVP geometry is shown to be a likely dead
  end because Epstein zeta functions generically violate RH, confirming that multiplicativity (the Euler
  product), not geometry, is the discriminant; NCG/partition-function entropy reduces to the same
  finite-place obstruction found in phase-7c: ARGUED, no new path from any of the three as stated.
- Seed coupling (Gate A): real ζ zeros give Carleson constant $C(t=0) = 0.998033$, marginally below 1;
  an injected off-line pair is correctly detected ($C>1$) and shown to heal under the forward heat flow
  (critical line as attractor, confirmed numerically): NUMERICAL.
- Gate B monotonicity theorem: under the forward de Bruijn–Newman flow, the off-line-ness
  $\mathcal L = \sum_j (\mathrm{Im}\,z_j)^2$ is a strict Lyapunov function, $\dot{\mathcal L} \le 0$,
  with an explicit sum-of-squares formula: PROVED (unconditional, verified against finite-difference
  integration). Byproduct: a height bound $|\mathrm{Im}\,z| \le \sqrt{2\Lambda}$ on any RH-violating
  zero, using Polymath15's $\Lambda \le 0.2$: PROVED.
- Why Gate B does not prove RH: two sharp, verified obstructions — (1) the needed direction is backward
  in time, where $\mathcal L$ only gives the trivial inequality $\mathcal L(0) \ge 0$; (2) the identity is
  arithmetic-blind: it holds for arbitrary conjugate-symmetric configurations, so a pure-ODE Lyapunov
  argument cannot single out ζ: PROVED (both obstructions, verified).
- Rodgers–Tao-coupled attack: shows the heat-flow path reduces exactly to the upper tail of the pair
  correlation, uniformly in height — the lower tail ($\Lambda \ge 0$) is Rodgers–Tao's proved result, but
  the needed upper tail (no anomalously tight zero clustering) is OPEN and RH-conditional, identified with
  the already-known sine-kernel/pair-correlation wall: ARGUED/NUMERICAL (real-zero gap data shown).
- Upper-tail quantitative attack: reformulates the target as control of the single worst (tightest) pair's
  backward collision time $t_c$, uniformly in height; measures $t_c$ for real ζ zeros and finds that while
  $|t_c|$ shrinks in absolute units with height, the normalized quantity $t_c/s^2$ (mean-spacing units)
  clusters near a universal negative constant $\approx -0.02$, consistent with GUE/sine-kernel
  predictions: NUMERICAL (suggestive, based on few data points, not a proved law).

## Documents
- `PLAN-RH-PHASE8-heat-flow.md` — triage of the three outside suggestions and the design of the heat-flow path.
- `SEED-results-and-candid-caveat.md` — Gate A seed coupling and its candid limitation (forward direction only).
- `GATE-B-verdict-sixth-language.md` — the Lyapunov monotonicity theorem and the two obstructions to using it for RH.
- `RT-coupled-verdict.md` — reduction of the flow to the upper tail of pair correlation.
- `UPPER-TAIL-verdict.md` — sharpest quantitative form of the upper-tail target and its numerical measurement.
- `experiments/` — numerical scripts backing each result (`heatflow_seed.py`, `gateB_lyapunov.py`, `rt_statistics_coupled.py`, `upper_tail_backward.py`).

## Relation to other phases
Builds on the band-limited Carleson detector of `phase-7-weil-carleson-sine-kernel` as its coupling
instrument; its conclusion (the wall is the upper tail of pair correlation) identifies the same
obstruction class as the sine-kernel bridge found there.
