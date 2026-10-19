# Phase 60 — E5: the L_DH violator. RESULTS (honest, inconclusive) **Code:** `E5_ldh_violator.py`, `E5b_*`, `E5c_dispersion_profile.py` ## Objective
Test the map to RH (Link 2): the CCM operator is self-adjoint -> spectrum always REAL;
L_DH has an OFF-line zero (85.699+0.3085i), which a real eigenvalue cannot match -> the
convergence MUST break. We were looking for the numerical witness of "convergence <=> RH". ## What was built (real, first in the program)
- CCM engine parametrized in Fourier form (a, conductor, coefficients, pole).
- CCM operator for **L_DH**: archimedean a=3/4, conductor 5, no pole (f entire), coefficients b(n) = -f'/f (dense support over all n), κ_DH=0.284079.
- **ζ gate PASSES** in the new engine: exact root 14.1347 and, at height 85, the on-line zero of ζ 84.7355 reproduced (disp 3e-4 over N=44..60). ## Decisive result: NEGATIVE / inconclusive **E5b** (convergence in N of the eigenvalue): L_DH disperses 0.13 at H=85.7 vs ~0.03 in the control
H=48 — worse, but the control did not level off. **E5c** (dispersion profile vs height, the clean test): the dispersion of L_DH **has NO
peak localized at the off-line zeros (85.7, 114)**. It grows **smoothly and monotonically with height**
(0.005 at H=24 -> 0.1 at H=80 -> 16 at H=120). At H=84,86 it is 0.04, *lower* than at H=74-80. By pre-registered criterion: smooth growth with H = resolution/truncation, **not** a signature
of the off-line zero. **The numerical witness of "convergence <=> RH" is NOT established at λ=3.7.** ## Caveats that invalidate a strong conclusion (declared)
1. **λ=3.7 too small for L_DH:** b(n) dense truncated at n<=13 is crude; this explains the smooth degradation with height. The region H>100 is directly unresolved.
2. ~~a=3/4 NOT validated~~ **CLOSED (E5d):** the archimedean a=3/4 was validated on L(χ_-4) (odd real character mod 4, Euler, RH-true): zeros 6.0209, 10.2438, 12.9881, 16.3426 reproduced to ~1e-6 (limited by the reference values, not the engine). Therefore the L_DH operator uses a CORRECT archimedean factor and the negative result of E5 is real.
3. **Metric probably wrong:** by Thm 1.1(iii) the off-line zero would be a MISSING eigenvalue (invisible to the real spectrum), not one of high dispersion. Correct diagnostic: |ξ̂_{λ,N}(85.699+0.3085i)| (which cannot vanish) vs Ξ_DH(there)=0, and its non-convergence to 0. ## State of the map after E5
- Mathematical mechanism **intact as a theorem** (Hurwitz + Thm 1.1(iii)): approximants with only real roots do not converge to Ξ_DH (complex zero). Does not depend on the experiment.
- Numerical demonstration of the mechanism: **open**. Requires (a) validating a=3/4 on L(χ4); (b) large λ with L_DH resolved up to H~85 (large arithmetic sums + mpmath); (c) the complex-determinant diagnostic (E6), not the dispersion. ## Honest assessment
There was no victory. The correct instrument was built and the decisive experiment came out
inconclusive at accessible parameters, with a validation caveat (a=3/4) that had to be closed
before any claim. The real next step is E6 (complex determinant) after
validating a=3/4 — not continuing to force the dispersion metric.
