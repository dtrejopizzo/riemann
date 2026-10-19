# Phase 110 — Does ξ-divisibility supply row (d)'s principal subspace?

Row (d) needs Riemann–Roch, which needs a principal subspace 𝒫 contained in the radical of the
zero-free corner pairing I_∂ (whose radical consists of functions vanishing at 0, at 1, and at every
zero of ξ). The programme's source rule forbids defining 𝒫 using a zero of ξ but allows using ξ
itself, so the phase tests the one compatible candidate: ξ-divisibility, 𝒫 ⊆ {f̂ = ξ·ĝ}, for which
vanishing at the zeros of ξ is automatic. Three tasks: test the existing graded-family witnesses,
characterize the ξ-divisible class, and check the obstruction found is not RH in disguise.

## Results
- The graded family's existing principal witnesses (phase 108) are not ξ-divisible: they have no ordinary Mellin transform, only a Dirac-mass "transform," a category mismatch with ξ·ĝ (an entire function). PROVED.
- No nonzero function in the corner pairing's actual admissible (compactly supported) test class is ξ-divisible at all: {f̂ = ξĝ} ∩ (admissible class) = {0}, because ξ has order 1 but infinite exponential type on the real axis, while any compactly supported transform has finite type. PROVED — NO-GO for the route, within the admissible class as currently defined.
- The ξ-divisible class is nonempty in an absolute sense once the test class is relaxed to Schwartz data (explicit Gaussian example constructed and verified). PROVED (existence outside the admissible class).
- The obstruction is traced to the Γ-factor's growth, not to ζ or to the location of any zero: deleting ζ's zero structure from ξ's defining product leaves the obstruction unchanged, while replacing the Γ-factor destroys it. PROVED — explicitly not RH in disguise, and not a circular definition (pre-registered non-vacuous test).
- Consolidated verdict: ξ-divisibility does not deliver row (d)'s principal subspace within the pairing's current admissible domain; the one door left open (not pursued here) is enlarging that domain beyond compact support. NO-GO (for this route), with a named open alternative.

## Documents
- `110_00_PHASE_110_PLAN.md` — the three tasks and source-rule framing.
- `110_01_THE_GRADED_FAMILY_IS_NOT_XI_DIVISIBLE.md` (+ `.py`) — Task 1.
- `110_02_WHAT_XI_DIVISIBILITY_REQUIRES.md` (+ `.py`) — Task 2, the order/type obstruction and the Gaussian counterexample.
- `110_03_IS_THIS_RH_IN_DISGUISE.md` (+ `.py`) — Task 3, the counterfactual-substitution audit.
- `110_99_PHASE_110_SUMMARY.md`, `110_99_verify_all.py` — consolidated verdict and full verifier re-run.

## Relation to other phases
Builds directly on phase 108's graded family and its radical/principal-subspace framework; closes the ξ-divisibility route for row (d) and names "enlarge the admissible test class" as the open door for later phases.
