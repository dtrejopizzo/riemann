# Phase 118 — Closure

**Closed:** 2026-08-17. Continued in
`phase-119-what-a-finite-compression-certifies/`.

## What this phase set out to do

Phase 117 killed the Gamma–Tate *source* route (`c_N < 1` at every threshold,
decaying like `(log N)^-0.6`) and redirected effort to the **exact** threshold
condition, in the output-defect metric where it carries constant one:

    S_E - Z_E^*Z_E - b_E^*A_0^dag b_E >= 0        (equivalently ||Theta_N|| <= 1)

Phase 118's goal was to prove that inequality outright.

## Why it is closing without proving it

The phase derived, and then verified numerically, what the operator `A_T`
actually is. For `F` real, supported in `I_T`, and primitive (`M_±F = 0`):

    <A_T F, F>  =  sum_rho h(gamma_rho),     h(tau) = Fhat(tau)Fhat(-tau)

summed over the nontrivial zeros of zeta. Three collapses make it exact rather
than approximate:

1. The pole terms of Weil's explicit formula are `h(±i/2) = M_+F · M_-F`, which
   vanish **because** `F` is primitive. That is what the two Tate moments do.
2. `psi(1/4) = -(gamma + pi/2 + 3 log 2)` — verified to 30 digits — so
   `Re psi(1/4 + i tau/2) - log pi == g_Gamma(tau) - m_0` identically. The
   constant `m_0` was never a normalization choice; it is the archimedean
   constant of the explicit formula, forced.
3. The autocorrelation `g(u) = int F(t+u)F(t)dt` is supported in `(-2T,2T)`, so
   the prime sum terminates at `n < e^{2T}` **exactly**. The paper's truncation
   loses nothing.

**Verified** (`scripts/W5_highprec.log`) at `T = 0.6, 1.2, 2.0, 3.0` against
cached zeta zeros: relative agreement `5.4e-11` to `1.6e-9`. The log also shows
the mechanism — at `T=3.0` the Gamma term `-0.037905513926` and the prime term
`-0.037905515879` cancel to nine digits, and the residue `~2e-9` *is* the zero
sum.

**Consequence.** The row-(d) inequality is localized Weil positivity on the
primitive space. Positivity of Weil's Hermitian form on all of `C_c^2(R)` is
classically *equivalent* to RH (Weil 1952; Yoshida 1992; Bombieri 2000), and the
union over `T` of functions supported in `I_T` is `C_c^2(R)`. So
"`A_T >= 0` for every `T`" is not a route to RH — it **is** RH.

No reformulation internal to the operator theory — factorization, Schur
complement, defect operators, scattering — can close it, because none of them
adds arithmetic input. Phase 118's target is therefore unreachable as posed, and
the phase closes rather than continuing to spend against it.

This is the same kind of result as phase 117's `c_N < 1` and the unconditional
scalar no-go: a route eliminated with certainty, which is worth more than an
open question left ambiguous.

## What it achieved

1. **The identity above**, derived and verified — the phase's main product. It
   also validates the whole construction: three things that could have been
   design choices (the constant `m_0`, the primitive space, the truncation)
   turn out to be forced.
2. **The balanced factorization verified independently** (`W3_SCATTERING.md`).
   `X^*X = R`, `Y^*Y = L`, `X^*X - Y^*Y = A` to `~1e-12` at all 19 prime-power
   thresholds up to 37, by a code path sharing nothing with `rowd_assembly`
   beyond the mesh; and `I - Phi^*Phi` agrees between the two routes to 9
   significant digits.
3. **Structural candidates for the scattering operator killed**: Toeplitz in
   `log n` and Hankel in `log n` both refuted (`R^2 <= 0.16`); block-diagonal
   over places excluded; no explicit `Psi` with `I - Phi^*Phi = Psi^*Psi` found.
   A coordinator heuristic — that the archimedean channel carries the load —
   was **refuted by measurement**: its share *falls* with the threshold
   (`0.70 -> 0.59 -> 0.44`), and the near-null direction is *less*
   archimedean-dominated than the safer ones beside it.
   Also measured: the finite-finite block is *dipped*, not peaked, on the
   diagonal `n=m`, in 100% of rows tested.
4. **The log-2 certificate reproduced and diagnosed** (`W4_CERTIFIED_RANGE.md`).
   All 5 SHA-256 pins verify; Tier 1 reproduces every quoted number in 0.109s;
   two Arb steps independently re-derived. What limits the endpoint is **not**
   numerical — precision has 5x headroom (39 bits suffice against 192 pinned)
   and tail quadrature 10x — but the genuine smallness of the Feshbach gap
   `h = 0.0012` around one near-null direction. Extending to `(1/2)log 5`
   requires the two cross-coupling terms (`kappa`, `C_D`) that phase 114
   attempted and retracted: unfinished analytic work, not more compute.
5. **`lambda_min(A_0) -> 0` measured directly** under refinement (to `5.4e-8`
   at refine 512), confirming the corpus's O3 "no spectral gap".

## What is left unresolved, and carried into phase 119

- **A two-route discrepancy in the assembly** (`PROOF_ARCHITECTURE.md` §2,
  "UNRESOLVED"). Two computations of the same `<A_T F,F>` for piecewise-constant
  `F` differ by 2%-8%, with a nearly constant absolute offset `~-2.2e-3`. The
  coordinator verified `psi_kernel` against 30-digit `mpmath` (machine precision)
  and re-derived the four-point Gamma formula as algebraically exact, so
  `rowd_assembly` should involve no approximation at all; the suspicion is that
  the new cross-validation script truncates the Gamma integral. **Not checked.**
  Phase 119 computes trace moments with this assembly, so this must be settled
  first.
- **Whether `lam_min_norm` converges to a positive limit or to zero.** At
  refine 512 the one step whose `A_0` stays well conditioned converges to a
  positive limit while the ill-conditioned ones appear to decay; the
  high-precision recomputation that would decide it did not finish. Moot for
  phase 118's purpose, but the data and the high-precision library
  (`scripts/W1_hp_*`) are on disk.
- **W1, W2 and W5 were stopped by session limits without writing reports.**
  Their scripts and result files survive in `scripts/`, including
  `W5_zeros_cache.json` (425 zeta zeros) and `W2_tate_closedform.py`.

## Status not promoted

RH is not proved. Row (d) is not closed. The strongest unconditional theorem is
unchanged: `A_T >= 0` for all `0 < T <= log 2`. Paper 42 was not modified during
this phase.
