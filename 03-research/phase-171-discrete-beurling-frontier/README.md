# Phase 171 — Discrete Beurling frontier: a counterexample with integer multiplicities

Phase attacks whether class-level regularity of a counting function (N(x) = cx + O(x^θ), θ < 1/2,
with integer prime/integer multiplicities) alone could force zeros to the critical line. It builds
a concrete, deterministic (non-random-seed) discrete Beurling system specializing the earlier
randomized construction of phase 163, to test whether integrality closes the gap left by that
earlier result.

## Results

- A discrete generalized-Beurling system with nonnegative-integer multiplicities, N_P(x) = cx + O(x^{2/5}) (in fact O(x^{83/208})), whose zeta function has infinitely many zeros at Re s = 11/16 > 1/2 — **PROVED** (explicit deterministic construction, no random seed).
- This specializes the discrete theorem `BFdisc` of phase 163 (λ = 3/8) and removes the ambiguity between an ε-loss exponent and a genuinely fixed exponent below 1/2.
- No theorem (B) obtained for θ₀ ≤ 1/3: the construction does not extend to push the counterexample exponent that low — **OPEN** in that range.
- Consequence for row D: every route based solely on class-level regularity N(x) = cx + O(x^θ), even with integer multiplicities and θ < 1/2, is closed — row D must depend on the individual datum of ζ, not on that class — **stated as a corollary of the PROVED counterexample**.

## Documents

- `R171_FINAL.md` — full construction, prior-corpus audit against phases 163/164/167, neutral audit (independent verification of the construction), and the row-D consequence.

## Relation to other phases

Specializes and sharpens the randomized discrete construction of phase 163 (`R163_803`, audited in `R163_891`); its closing consequence is probed further in phase 172.
