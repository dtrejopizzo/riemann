# Phase 124 — Direct first-contact route

Status: **ACTIVE EXPLORATION; no new positivity theorem proved.**
This phase audits the direct first-contact route; this opening
does not prove RH.

This phase investigates the direct analytic route selected in the
[September 8 plan](../../05-meta-and-planning/ABCD-CLOSURE-PLAN/PRIORITY_PLAN.md).
Its goal is to exclude a nonzero primitive first-contact state by an
arithmetic identity or inequality, without first completing the geometric
theory A/B/C. The papers remain untouched.

The starting point is the existing strict base window, compact
first-contact theorem and source equations. Their established domains and
corrections are retained. Opening this phase does not revalidate every
inherited result or promote a conditional reduction to a proof.

## Exact target

For every finite support window T, prove

```
q_T(F) = -B_nuc,T(F,F) >= 0
```

on the existing primitive form domain. Its two constraints, in the
balanced additive convention, are

```
integral exp(t/2) F(t) dt = integral exp(-t/2) F(t) dt = 0.
```

The inherited first-contact theorem reduces a failure after the certified
window to a nonzero parity state F at T_* with q_(T_*) nonnegative and
F in its radical. The missing task is an arithmetic exclusion of that
state, not another proof that a defect detects it.

## Minimal dependencies

| Input | Source | Exact role |
|---|---|---|
| Strict base window | [P123.036](../phase-123-weil-strength-abc/P123_036_D_NORMALIZATION_AND_ENDPOINT_REPLAY.md) and the certificate it references | Starting positivity through T = log 2; no extension to the retracted log-5 claim. |
| Attainment | [P122.002](../phase-122-row-d-integrity-and-construction/P122_002_FIRST_CONTACT_COMPACTNESS_THEOREM.md) | A later failure produces an attained first-contact radical, including channel births. |
| Source equations | [Literal state system](../phase-120-global-polarization/P3_LITERAL_STATE_SYSTEM.md) | Coupled Gamma and prime states with their signed on-shell action. |
| Validity of rigidity inputs | [P122.008](../phase-122-row-d-integrity-and-construction/P122_008_PHASE121_LOAD_BEARING_AUDIT.md) | Distinguishes detection from the missing vanishing theorem. |
| Sufficient exclusion mechanism | [P122.020](../phase-122-row-d-integrity-and-construction/P122_020_TWO_GATE_D_CLOSURE_CRITERION.md) | Critical transmission plus prime-seam matching would exclude first contact. |
| Exact endpoint and flux | [P122.029](../phase-122-row-d-integrity-and-construction/P122_029_LIONS_MAGENES_TRANSMISSION_AUDIT.md), [P122.028](../phase-122-row-d-integrity-and-construction/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md) | The boundary condition and effective energy are already known. Neither is automatically zero. |

## What changes here

A direct analytic proof may establish a consequence specifically for a
first-contact minimizer. It does not have to construct a determinant
correspondence or a larger category of horizontal objects first. Those
requirements belong to the geometric construction route.

The first-contact hypotheses may be used in a contradiction argument:
they are consequences of an assumed failure, not an assumption of global
RH. However, the desired transmission or matching must be DEMONSTRATED
from the actual arithmetic operator and these hypotheses. Postulating it
would leave the proof conditional.

R/S remain one sufficient route, not mandatory axioms for every possible
analytic proof. An independent uniform signed inequality that proves the
target is also admissible. Neither route retroactively completes A.

See [PLAN.md](PLAN.md) for the first attack, acceptance criteria and stopping
rules for unsuccessful candidates. This phase starts with an execution
specification; it contains no new proof of the missing arithmetic law yet.

## Current review

[P124.003](P124_003_REVIEW_AND_NEXT_STEP.md) records the current review:
[P124.004](P124_004_WINDOW_VARIATION.md) is an obstruction unless its
left/right threshold and `Q`-domain differentiability issues are repaired;
[P124.005](P124_005_ARITHMETIC_COLLAR.md) gives the useful residual
`rho_(+,T)` for `J_+(F)`; and
[P124.006](P124_006_RETARD_RANGE_ATTACK.md) matches local jumps but leaves
the interior residual `-P_T A_T h`.  [P124.007](P124_007_VIRIAL_COLLAR_ATTACK.md)
and [P124.008](P124_008_NULL_REGULARITY.md) add obstructions: the projected
virial cancels in the Tate defect, and log-elliptic regularity gives no
Sobolev gain across `H^(1/2)`.  The selected next line is a critical
D.240 support-to-primitive shorting estimate for
`A_T(F)=-<rho_(+,T),F>`; [P124.009](P124_009_SUPPORT_LEAKAGE_EQUALITY.md)
shows leakage factorization plus the Tate `1/2` bound does not provide it,
and [P124.010](P124_010_TOEPLITZ_LEAKAGE_TEST.md) shows the one-prime
Toeplitz test still needs an external centering not realized by the
support-anomaly family.

## New coordinate

[P124.013](P124_013_ENTIRE_FORM_AND_SHIELDING_DICHOTOMY.md) rewrites the whole
row-(d) target in the entire-function variable
`Phi_F(s)=int F(t)e^{(s-1/2)t}dt`.  The two Tate moments become the values
`Phi_F(1)`, `Phi_F(0)`, so the primitive space is the interpolation condition
`Phi(0)=Phi(1)=0`, and Weil's functional is `sum_rho Phi(rho)Phi(1-rho)`.  In
that coordinate the unconstrained Weil form is a bordered form whose (1,1)
block is `L_T` and whose crossblock is exactly the Tate collar
`rho_{+,T}`.  The resulting dichotomy is: at the first contact of the
primitive form, either Gate R holds, or the unconstrained form is already
indefinite there ("shielding").  Hence Gate R follows from the
constraint-free inequality `Sigma(T)=B_T-X_T^*L_T^{-1}X_T >= 0` for `T<T_q`,
which contains no unknown minimizer.

[P124.014](P124_014_FALSIFIER_GATE_SEPARATION.md) runs the shifted-pair
falsifier `Xi_a(s)=xi(s+a)xi(s-a)`, whose first contact is a genuine object
because its zeros are off the critical line.  Both gates fail there, and
shielding is observed.  This refutes the reading of Gate R as a structural
theorem of the functional-equation class: R needs the same unimodular local
roots that S needs.

## Standing methodological note (`[phase 134]`)

Recorded from §9.3 of an earlier draft of Paper 47 (the passage is not in the current
version of that paper) and from
the independent re-runs in `R134_002_AUDIT_ROUND1.md` §§4, 6.  It does not
retract any result of this phase; it fixes how this phase's numbers may be
read.

1. **Galerkin eigenvalues here are variational upper bounds.**
   `p124_lab.assemble` builds *exact* form matrices on the piecewise-constant
   space of `rowd_assembly.build_mesh`, which is a **subspace** of the test
   space, with the primitive constraint imposed exactly inside it.  Hence the
   computed `lambda_min(L_T)` is `>=` the true infimum; and `Sigma(T)` is
   itself an infimum over `P_T`, so the same applies to it.  **A negative
   computed eigenvalue certifies a genuine negative direction; a positive one
   certifies nothing.**  Evidence: for `zeta` at `T = 1.7`,
   `lambda_min(L_T) = 2.93, 1.99, 1.23, 0.84, 0.61` (`x 10^-2`) at
   `refine = 2,...,6`, decreasing at every step; at `T = 0.72`,
   `lambda_min(Sigma) = 2.585, 1.327, 1.189, 0.925, 0.789` (`x 10^-2`) over
   the same sweep.  Consequence: the `zeta` "control" of P124.014 Section 3 is
   incapable **by construction** of supporting a conclusion about `zeta`.
2. **Scope.**  This concerns the double-precision Galerkin scans of phases 118
   and 124 only.  It does **not** touch the interval-arithmetic `T = log 2`
   endpoint certificate replayed in P123.036.
3. **P124.014's `Xi_a` first-contact brackets are not resolution-stable**; see
   the `[phase 134]` note in P124_014 Section 3.  Its qualitative conclusions
   are unaffected, because they rest on negative eigenvalues.
4. **P124.013 Corollary 3.3**: the `liminf` criterion *is* invariant at a
   finite `T_*`; the *value* `lambda_min Sigma(T)` is not a congruence
   invariant and must not be quoted across bases or papers.  Carry (3.2),
   `Sigma(T) >= 0`.  See the `[phase 134]` note there.
5. **Paper 47 Theorem 7.1** supplies the structural reason for the
   `zeta`/`Xi_a` separation this phase observed: `Xi_a`'s local contacts are
   not the shell volumes `vol(p^k Z_p^x) = log p`, so its would-be Frobenius
   satisfies `F_n * F_n^dagger = (n^a + n^-a) Delta^(n)` and is **not** a
   partial isometry — it fails Paper 44 Theorem 3ter.6, before any comparison.

## Other files in this folder

- `P124_001_JOINT_VARIATION.md` — Joint Gamma--Euler variation.
- `P124_002_TRANSMISSION_ATTACK.md` — Superseded transmission note.
- `P124_011_SCHUR_COLLAR_REDUCTION.md` — Schur reduction of the Tate collar at first contact.
- `P124_012_CAUSAL_STORAGE_SCALAR_SEAM_GATE.md` — Causal storage reduces the seam gate to one scalar surplus.
- `scripts/` — supporting scripts (3 files).
