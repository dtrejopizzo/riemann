# Phase 109 — One-sided pairing: does it carry a zero-determined radical?

Phase 108 found the two-sided Tate pairing unconditionally wrecked by the identity shell, while
the one-sided sum over positive shells k≥1 assembles cleanly to −ζ'/ζ(s). Phase 109 bilinearizes
that surviving one-sided object and tests a single hypothesis: does the resulting pairing's radical
come out zero-determined (the Stage-0 shape from phase 107), which would open a route to unifying
rows (a)–(d)?

## Results
- A genuine bilinear one-sided pairing B(f,g)=Σ_n Λ(n)f(n)g(n) exists: absolutely convergent, bilinear, symmetric, not Hermitian, and recovers the phase-108 one-sided sum. PROVED.
- The radical of B is prime-power-determined (rad B = {f : f(p^k)=0 ∀p,k}), neither zero-determined nor Γ-determined; explicit witness F=sin(πx) lies in the radical with Mellin transform zero-free on all of ξ's zero set. PROVED — hypothesis REFUTED.
- Signature computation was skipped per the phase's own pre-registered gate, since Step 2 already failed; the only available invariant (n₊=∞, n₋=0 from Λ(n)>0) is unconditionally true and carries no information about ξ's zeros. OPEN/content-free, not pursued.
- Correction on re-checking: the original "forced, no free parameter" claim about the pairing was overstated; only a single rank-one square per functional is forced, not the diagonal assembly. A stronger, kernel-independent version of the refutation is then proved (109_04): for every kernel supported on prime powers, the witness F=sin(πx) still lies in the radical, and its Mellin transform has constant modulus on the critical line. PROVED.
- Diagnosis of why the hypothesis could not have held: "poles at the zeros" in the assembled Dirichlet series and "the pairing detects the zeros" are statements about opposite sides of the Mellin transform; the zeros live in the continuation, not in the coefficients Λ(n). ARGUED.

## Documents
- `109_00_PHASE_109_PLAN.md` — restates the phase-108 diagnosis and the hypothesis being tested.
- `109_01_THE_ONE_SIDED_PAIRING.md` (+ `.py` verifier) — construction and properties of B.
- `109_02_THE_RADICAL.md` (+ `.py` verifier) — radical computation and the sin(πx) refutation witness.
- `109_03_THE_SIGNATURE.md` — records why the signature step is skipped/content-free.
- `109_04_THE_COEFFICIENT_SIDE_IS_BLIND.md` (+ `.py`) — correction on re-checking, kernel-independent refutation and the corrected target for row (a).
- `109_99_PHASE_109_SUMMARY.md` (+ verifier) — full verdict table and anti-circularity audit.

## Relation to other phases
Directly continues phase 108 (inherits the one-sided assembly −ζ'/ζ and the phase-107 Stage-0 pairing shape used as the test hypothesis); concludes by resetting the target for row (a) to a continuation-side, non-symmetrized, zero-free-by-definition pairing, for later phases to pursue.
