# E77 Autonomous Continuation Plan

## Current Sharp Endpoint

Omega7 is not closed yet.  The current reduced object is

```text
SHELL-REG
```

obtained after:

```text
E77.5e SHELL-CANCEL anatomy
E77.5f exact 2x2 shell Schur resolvent
```

The exact identity now available is:

```text
T_b(z) = t0(z) - tau(z) Sigma^{-1} kappa
T_b'(z) = t0'(z) - tau'(z) Sigma^{-1} kappa.
```

The live problem is not to prove the shell term or its safe derivative is
always small.  Planted builds can also have small shell-log derivative
windows.  The live problem is to prove signed regularity and Cauchy
coherence for

```text
theta_N(z) = tau_N(z) Sigma_N^{-1} kappa_N / t0_N(z)
```

so that

```text
Delta_N log(1 - theta_N(z))
```

has a summable envelope after coupling to the explicit external tail.

## Binding Restrictions

No step may use:

```text
zero locations, except the required planted falsifier;
Weil positivity;
ambient inverse norm estimates;
pseudoinverses;
absolute estimates before signed cancellation;
point-local Christoffel/zero filters;
arithmetic outside absolute convergence in Re(s)>1.
```

Every new claim needs:

```text
one theorem-grade .md statement;
one .py probe with real multiprecision data;
zeta vs planted comparison;
an explicit falsifier verdict.
```

## E77.5g - Schur Phase Increment Probe

Build:

```text
E77_5g_schur_phase_increment_probe.py
E77_5G_SCHUR_PHASE_INCREMENT.md
```

Measure for zeta and planted:

```text
theta_N(z)
log(1 - theta_N(z))
Delta_N log(1 - theta_N(z))
2 Re(i Delta_N log(1 - theta_N(i sigma)))
```

Compare against:

```text
section-lag delta from E77.5d;
shell update from E77.5e;
external tail increment.
```

Accept if zeta shows coherent signed phase increments with decreasing
envelope and planted fails by phase jumps, branch instability, or
non-coherent correction/core geometry.

If E77.5g fails, record an autopsy and reduce to the exact failing finite
quantity: phase branch, Sigma conditioning, kappa alignment, or tau phase.

Status: completed in `E77_5G_SCHUR_PHASE_INCREMENT.md`.  It autopsies
safe-derivative smallness as falsifier-neutral and reduces the target to:

```text
THETA-REG:
  theta_N=tau_N Sigma_N^{-1}kappa_N/t0_N is Cauchy with a summable
  envelope on sigma-compacts.
```

## E77.5h - Regularity Decomposition

E77.5g separated zeta/planted at the `Delta theta` level.  Decompose
`theta_N` into:

```text
tau geometry;
Sigma 2x2 spectral data;
kappa shell source;
t0 core transfer.
```

Probe which factor carries the regularity:

```text
E77_5h_schur_factor_regularizer_probe.py
E77_5H_SCHUR_FACTOR_REGULARIZER.md
```

Status: completed in `E77_5H_SCHUR_FACTOR_REGULARIZER.md`.  The naive
factorwise theorem is refuted: zeta `Delta theta` is small only after large
three-term cancellation, with cancellation index up to `1.6e5`.

The desired theorem is now the coupled replacement:

```text
SCHUR-COCYCLE:
  sup_{sigma in K}
  |(Delta tau)v_N c_N + tau_M(Delta v)c_N + tau_M v_M(Delta c)|
  <= envelope_N,
  sum_N envelope_N < infinity.
```

The planted build must fail the same coupled theorem.  The three summands
must remain coupled until after signed cancellation.

## E77.5i - Schur-Cocycle Symbolic Source

Derive the three-term cocycle from the finite Loewner/cell identities,
without estimating the factors separately:

```text
Delta tau, Delta(Sigma^{-1}kappa), Delta(1/t0)
```

must be rewritten as one signed cell object.  Candidate target:

```text
COCYCLE-CELL:
  SCHUR-COCYCLE equals a finite paired cell/Gamma-prime residual whose
  leading terms cancel for zeta and not for planted.
```

Build:

```text
E77_5i_schur_cocycle_cell_probe.py
E77_5I_SCHUR_COCYCLE_CELL.md
```

Status: completed in `E77_5I_SCHUR_COCYCLE_CELL.md`.  The pair-reduction
route is refuted: zeta's best two-term pair remains `49x--6241x` larger
than the final `Delta theta`.  The cancellation is genuinely ternary.

## E77.5j - Consecutive Schur Complement Cell Residual

Derive `A+B+C` without splitting it into factors or pairs.  Compare the
two consecutive shell Schur complements before inversion:

```text
S_N = C_N - U_N^T A_N^{-1} U_N,
k_N = g_shell,N - U_N^T A_N^{-1} g_core,N,
t_N(z)=1/(z-d_b)-r_core,N A_N^{-1}g_core,N,
```

and express

```text
theta_N-theta_{N+2}
```

as one finite residual produced by adding/removing the shell pair.  Target:

```text
TERNARY-CELL-CANCEL:
  A+B+C = paired finite cell residual with a signed leading cancellation.
```

Build:

```text
E77_5j_consecutive_schur_cell_probe.py
E77_5J_CONSECUTIVE_SCHUR_CELL.md
```

Status: completed as `E77_5J_BOUNDARY_SHELL_COUPLING.md`.  The pure shell
update was refuted: `N -> N+2` inserts four interior nodes
`{-N-1,-N,N,N+1}` and moves the boundary `N -> N+2`.  For zeta the
boundary pole shift is an active fraction of `Delta theta`; for planted it
is negligible relative to the O(1) instability.

Reduced target:

```text
BOUNDARY-SHELL-CELL:
  derive the moving-boundary/four-node update as one finite Loewner/cell
  residual with signed leading cancellation.
```

## E77.5k - Moving-Boundary Four-Node Identity

Build:

```text
E77_5k_moving_boundary_four_node_probe.py
E77_5K_MOVING_BOUNDARY_FOUR_NODE.md
```

Required identity target:

```text
theta_N - theta_{N+2}
 = paired Cauchy evaluation of one update residual generated by
   {-N-1,-N,N,N+1} plus boundary move N -> N+2.
```

The proof must assemble the update before inversion/absolute values.

Status: completed in `E77_5K_MOVING_BOUNDARY_FOUR_NODE.md`.  The
common-core transfer identity is exact, but `theta_common` is
partition-dependent and therefore not the correct endpoint coordinate.

Reduced target:

```text
LOGT-CELL:
  derive the moving-boundary/four-node update for log T_N or T_N'/T_N
  directly, without choosing a theta coordinate.
```

## E77.5l - Safe Log-Transfer Cell Update

Build:

```text
E77_5l_logt_cell_update_probe.py
E77_5L_LOGT_CELL_UPDATE.md
```

Target:

```text
Delta_N 2 Re(i T_N'(i sigma)/T_N(i sigma))
```

must be expressed by the common-core moving-boundary block and compared to
the section-lag deltas from E77.5d/e.  This is the first partition-invariant
candidate for a summable envelope.

Status: completed in `E77_5L_LOGT_CELL_UPDATE.md`.  The invariant
reconstruction is exact.  The reduced target is:

```text
LOG-EXT-RATIO:
  prove a signed expansion for Delta external - Delta logT.
```

## E77.5m - Signed Log/External Residual

Build:

```text
E77_5m_log_ext_ratio_probe.py
E77_5M_LOG_EXT_RATIO.md
```

Measure and model:

```text
R_N(sigma)=Delta external_N(sigma)-Delta logT_N(sigma)
R_N/Delta external_N
N^p R_N
```

The target is an explicit cell/Gamma-prime residual expansion whose leading
coefficient is zeta-coherent and planted-failing.

Status: completed in `E77_5M_LOG_EXT_RATIO.md`.  The raw residual is not
summable yet; zeta shows an apparent leading `1/N` term.

Reduced target:

```text
LEAD-1/N-CANCEL:
  identify and remove/prove cancellation of the leading coefficient in
  N(Delta external - Delta logT).
```

## E77.5n - Leading Coefficient Audit

Build:

```text
E77_5n_lead_1_over_n_cancel_probe.py
E77_5N_LEAD_1_OVER_N_CANCEL.md
```

Measure by sigma, not only max rows:

```text
C_N(sigma)=N R_N(sigma),
Delta C_N(sigma),
candidate sigma profile from external tail asymptotics.
```

If `C_N(sigma)` stabilizes, name its finite cell coefficient.  If it does
not, autopsy and reduce to the true coefficient object.

Status: completed in `E77_5N_LEAD_1_OVER_N_CANCEL.md`.  `C_N(sigma)` is
positive and smooth for zeta, but it still drifts; a fixed leading
coefficient closure is not licensed.

Reduced target:

```text
PROFILE-DRIFT-CANCEL:
  derive and cancel the signed drift C_N(sigma)-C_{N+2}(sigma).
```

## E77.5o - Profile Drift Probe

Build:

```text
E77_5o_profile_drift_probe.py
E77_5O_PROFILE_DRIFT_CANCEL.md
```

Measure:

```text
D_N(sigma)=C_N(sigma)-C_{N+2}(sigma),
N D_N(sigma),
sigma-profile ratios,
zeta/planted drift signs.
```

If `D_N` is summable or admits a next leading cancellation, proceed.

Status: completed in `E77_5O_PROFILE_DRIFT_CANCEL.md`.  The raw drift is
not yet negligible; zeta has a visible `N^-2`-scale drift coefficient.

Reduced target:

```text
SECOND-COEFF-CANCEL:
  identify and cancel the next coefficient in the drift profile.
```

## E77.5p - Second Coefficient Audit

Build:

```text
E77_5p_second_coeff_probe.py
E77_5P_SECOND_COEFF_CANCEL.md
```

Measure:

```text
Q_N(sigma)=N^2(C_N(sigma)-C_{N+2}(sigma)),
Delta Q_N(sigma),
candidate sigma profile.
```

If `Q_N` stabilizes, derive the finite cell coefficient.  If it drifts,
name the next object without extrapolation.

Status: completed in `E77_5P_SECOND_COEFF_CANCEL.md`.  A single second
coefficient is refuted; adjacent even steps oscillate.

Reduced target:

```text
MOD4-DRIFT-SPLIT:
  split C_N, D_N, and Q_N by N mod 4 and test each profile separately.
```

## E77.5q - Mod-4 Drift Split

Build:

```text
E77_5q_mod4_drift_split_probe.py
E77_5Q_MOD4_DRIFT_SPLIT.md
```

Measure:

```text
C_N(sigma), D_N(sigma), Q_N(sigma)
on N=0 mod 4 and N=2 mod 4 separately.
```

If each subsequence stabilizes, derive the parity profiles from the
moving-boundary mesh.  Otherwise name the next scaling object.

Status: completed in `E77_5Q_MOD4_DRIFT_SPLIT.md`.  The split is a genuine
reduction: the zeta `N=0 mod 4` branch stabilizes much better, while
`N=2 mod 4` retains a late spike.

Reduced target:

```text
MOD2-SPIKE-CELL:
  explain the N=2 mod 4 spike or remove it by the correct physical
  boundary scaling.
```

## E77.5r - Mod-2 Spike / Physical Boundary Scaling

Build:

```text
E77_5r_mod2_spike_boundary_scaling_probe.py
E77_5R_MOD2_SPIKE_BOUNDARY_SCALING.md
```

Measure:

```text
d_N = 2*pi*N/L,
Q_N as a function of d_N rather than N,
separate N=0 mod 4 and N=2 mod 4 profiles.
```

If physical scaling removes the spike, derive the corresponding mesh-cell
coefficient.  If not, name the next obstruction.

Status: completed in `E77_5R_MOD2_SPIKE_BOUNDARY_SCALING.md`.  Physical
boundary scaling does not remove the spike at fixed lambda.

Reduced target:

```text
LOEWNER-PARITY-CELL:
  derive the mod0/mod2 branch difference from the finite Loewner/cell
  parity of the moving-boundary update.
```

## E77.5s - Loewner Parity Cell

Build:

```text
E77_5s_loewner_parity_cell_probe.py
E77_5S_LOEWNER_PARITY_CELL.md
```

Measure:

```text
inserted-node signs and sine-symbol values,
Loewner four-node parity packages,
correlation with mod0 stable branch vs mod2 spike.
```

If the parity package explains the spike, derive the cancellation theorem.

Status: completed in `E77_5S_LOEWNER_PARITY_CELL.md`.  Raw four-node
sine-symbol parity is refuted; the spike requires Cauchy/resolvent weights.

Reduced target:

```text
WEIGHTED-PARITY-CELL:
  compute the weighted active-block parity package from the common-core
  resolvent and safe Cauchy row.
```

## E77.5t - Weighted Parity Cell

Build:

```text
E77_5t_weighted_parity_cell_probe.py
E77_5T_WEIGHTED_PARITY_CELL.md
```

Measure:

```text
weighted inserted-node sources,
safe Cauchy row weights,
common-core resolvent weights,
correlation with Q_N mod0/mod2 branches.
```

Status: completed in `E77_5T_WEIGHTED_PARITY_CELL.md`.  Absolute weighted
magnitude is refuted; the coherent zeta object is the normalized
odd/inserted ratio.

Reduced target:

```text
ODD-RATIO-LAW:
  model the weighted |odd|/|inserted| ratio and its contribution to Q_N.
```

## E77.5u - Odd Ratio Law

Build:

```text
E77_5u_odd_ratio_law_probe.py
E77_5U_ODD_RATIO_LAW.md
```

Measure:

```text
Q_N versus weighted odd/inserted ratio,
residual after fitting ratio profile,
zeta/planted failure of same profile.
```

Status: completed in `E77_5U_ODD_RATIO_LAW.md`.  The ratio law explains the
stable zeta `N=0 mod 4` branch but not the `N=2 mod 4` spike.

Reduced target:

```text
MOD2-MISSING-WEIGHT:
  test old-boundary/outer/old-shell ratios and complex phase on the mod2
  branch.
```

## E77.5v - Missing Weighted Observable

Build:

```text
E77_5v_missing_weight_probe.py
E77_5V_MISSING_WEIGHT.md
```

Measure:

```text
Q_N versus old-boundary/inserted,
Q_N versus outer/inserted,
Q_N versus old-shell/inserted,
Q_N versus complex phase of weighted odd package.
```

Status: completed in `E77_5V_MISSING_WEIGHT.md`.  Scalar weighted ratios are
insufficient; the next object must keep the complex active vector.

Reduced target:

```text
COMPLEX-ACTIVE-VECTOR-LAW:
  compare full complex active contribution vectors by mod branch.
```

## E77.5w - Complex Active Vector Law

Build:

```text
E77_5w_complex_active_vector_probe.py
E77_5W_COMPLEX_ACTIVE_VECTOR_LAW.md
```

Measure:

```text
phase-aligned active vectors,
left/right inserted-node phase gaps,
vector distances between mod0 stable branch and mod2 spike branch.
```

Status: completed in `E77_5W_COMPLEX_ACTIVE_VECTOR_LAW.md`.  The direct
state law is refuted: in zeta the phase-aligned vectors become closer exactly
where the `N=18` mod2 spike appears.  The planted falsifier breaks the regular
transport, so the next object is not the vector location but its signed
curvature.

Reduced target:

```text
ACTIVE-VECTOR-CURVATURE:
  measure first and second differences of the phase-aligned active-vector
  path and test signed curvature against Q_N.
```

## E77.5x - Active Vector Curvature

Build:

```text
E77_5x_active_vector_curvature_probe.py
E77_5X_ACTIVE_VECTOR_CURVATURE.md
```

Measure:

```text
branch tangent vectors,
second differences within each mod4 branch,
cross-mod acceleration defects,
signed Hermitian curvature against the inserted anchor.
```

Accept only if the zeta law predicts the mod2 spike and the planted build
breaks it.

Status: completed in `E77_5X_ACTIVE_VECTOR_CURVATURE.md`.  Branch tangents
and simple Hermitian curvature are refuted as direct carriers of the mod2
`Q_N` spike.  Zeta vector transport is smooth, but the scalar spike lives in
the functional applied to the Schur response, not in the vector geometry
alone.

Reduced target:

```text
Q-FUNCTIONAL-IDENTITY:
  derive the exact finite scalar identity expressing Q_N from the active
  Schur cell, the external log-tail increment, and the inserted-anchor
  normalization.
```

## E77.5y - Q Functional Identity

Build:

```text
E77_5y_q_functional_identity_probe.py
E77_5Y_Q_FUNCTIONAL_IDENTITY.md
```

Measure:

```text
exact reconstruction of Q_N from logT/external residuals,
active-cell contribution to the reconstructed scalar,
remainder after subtracting active-cell functional,
zeta versus planted falsifier.
```

The goal is theorem-grade algebra, not a fitted observable.  The probe must
compare two independent computations: the `E77.5q` drift definition of `Q_N`
and the `E77.5l/E77.5m` log-transfer residual formula.

Status: completed in `E77_5Y_Q_FUNCTIONAL_IDENTITY.md`.  The exact identity

```text
Q_N = Q_ext,N - Q_logT,N
```

reconstructs the independent E77.5q drift values to roundoff.  The external
component is build-independent, so the only surviving discriminant is the
signed coupling of the Schur log-transfer functional to that external
profile.  The planted build breaks this coupling.

Reduced target:

```text
LOGT-EXT-COUPLING:
  prove that Q_logT,N tracks the build-independent external second profile
  with the zeta residual and that planted/off-line builds fail the same
  coupling.
```

## E77.5z - LogT External Coupling

Build:

```text
E77_5z_logt_ext_coupling_probe.py
E77_5Z_LOGT_EXT_COUPLING.md
```

Measure:

```text
A_N = Q_logT,N / Q_ext,N,
signed coupling defect Q_ext,N - Q_logT,N,
mod4 branch profiles of A_N,
sigma-profile stability,
zeta versus planted break point.
```

This is the last scalar layer before returning to the Schur cell formula for
`logT`.  If this layer is still too coarse, derive the coupling directly
from the six-node Schur response and name the exact residual slot.

Status: completed in `E77_5Z_LOGT_EXT_COUPLING.md`.  The scalar coupling
distinguishes zeta from the planted build, and the zeta mod0 branch is
coherent.  It fails as a closure theorem on the live mod2 branch: the ratio
crosses through 1 and then drops at the spike.  The next object must be the
local Schur formula for `Q_logT,N`.

Reduced target:

```text
SCHUR-LOGT-FUNCTIONAL:
  expand Q_logT,N using T=t0-corr, Tp=t0p-corrp, and the six-node Schur
  response; isolate the mod2 anchor-crossing term.
```

## E77.5aa - Schur LogT Functional

Build:

```text
E77_5aa_schur_logt_functional_probe.py
E77_5AA_SCHUR_LOGT_FUNCTIONAL.md
```

Measure:

```text
exact reconstruction of Delta logT from T=t0-corr,
separate t0-only / corr-only / mixed logarithmic components,
which component carries the mod2 anchor crossing,
zeta versus planted falsifier.
```

No Taylor truncation may be treated as proof.  If using a Taylor expansion,
record the exact remainder and verify reconstruction independently.

Status: completed in `E77_5AA_SCHUR_LOGT_FUNCTIONAL.md`.  The exact
decomposition

```text
Tp/T = t0p/t0 - theta'/(1-theta)
Q_logT = Q_t0 + Q_theta
```

reconstructs the independent `Q_logT` component to roundoff.  In zeta,
`Q_theta` carries the main profile and `|1-theta|` approaches zero
coherently; the planted build is outside that anchor regime.

Reduced target:

```text
ANCHOR-DENOMINATOR-LAW:
  prove the controlled zeta approach of 1-theta_N to zero and the signed
  theta-prime profile that produces Q_theta.
```

## E77.5ab - Anchor Denominator Law

Build:

```text
E77_5ab_anchor_denominator_law_probe.py
E77_5AB_ANCHOR_DENOMINATOR_LAW.md
```

Measure:

```text
complex phase and magnitude of 1-theta,
N-scaling of |1-theta| on both mod4 branches,
theta-prime/(1-theta) signed profile,
zeta versus planted anchor-regime failure.
```

If the law holds, combine it with the build-independent `Q_ext` profile.  If
it fails, name the exact residual in the theta-prime numerator.

Status: completed in `E77_5AB_ANCHOR_DENOMINATOR_LAW.md`.  Zeta enters a
near-anchor regime while the planted build does not, but a simple
`|1-theta|` magnitude or power law is insufficient.  The signed object must
keep numerator and denominator coupled.

Reduced target:

```text
THETA-LOGDERIV-COUPLING:
  control -theta'/(1-theta) directly, including phase, numerator, and
  denominator together.
```

## E77.5ac - Theta Log-Derivative Coupling

Build:

```text
E77_5ac_theta_logderiv_coupling_probe.py
E77_5AC_THETA_LOGDERIV_COUPLING.md
```

Measure:

```text
complex theta, theta', and -theta'/(1-theta),
signed safe scalar contribution,
Q_theta branch profiles,
mod2 residual after subtracting the build-independent external profile,
zeta versus planted falsifier.
```

This is the current smallest finite Schur object.

Status: completed in `E77_5AC_THETA_LOGDERIV_COUPLING.md`.  The coupled
object

```text
u=-theta'/(1-theta)
```

separates zeta from the planted build by phase: zeta lies near the positive
imaginary axis, while the plant lies near the negative real axis.  Magnitude
diagnostics alone are refuted.  The live target is now the finite phase
sector law for `u`.

Reduced target:

```text
U-PHASE-LAW:
  prove that the zeta Schur/cell algebra keeps u in the signed sector near
  +i with quantitative drift small enough for the Q_theta envelope.
```

## E77.5ad - U Phase Law

Build:

```text
E77_5ad_u_phase_law_probe.py
E77_5AD_U_PHASE_LAW.md
```

Measure:

```text
sector margin Re(u), Im(u), and arg(u)-pi/2,
mod4 branch phase drift,
Q_theta defect after sector-normalized model,
zeta versus planted sector exit.
```

No analytic filter or zero-location input is allowed; the sector must come
from finite Schur/cell identities.

Status: completed in `E77_5AD_U_PHASE_LAW.md`.  Zeta stays in the upper
vertical sector `Im(u)>|Re(u)|` on the tested rows and the planted build
exits it decisively.  The signed vertical model is accurate for zeta and
fails for planted.  The missing theorem is a finite sector certificate.

Reduced target:

```text
SECTOR-CERTIFICATE:
  express Im(u)-|Re(u)| in finite Schur/cell algebra and prove a positive
  lower certificate on the zeta cofinal path.
```

## E77.5ae - Sector Certificate

Build:

```text
E77_5ae_sector_certificate_probe.py
E77_5AE_SECTOR_CERTIFICATE.md
```

Measure:

```text
exact real/imag formulas for u from theta and theta',
polynomial/rational numerator of Im(u)-|Re(u)| or cone-equivalent
Im(u)^2-Re(u)^2 with Im(u)>0,
zeta versus planted sign certificate,
mod2 residual if certificate fails.
```

Use the cone-equivalent signed pair

```text
Im(u)>0,
Im(u)^2-Re(u)^2>0
```

to avoid absolute-value algebra.

Status: completed in `E77_5AE_SECTOR_CERTIFICATE.md`.  Zeta satisfies the
cone pair on the tested rows and planted fails it.  The raw cone numerator
decays too quickly to serve as a uniform lower certificate; the robust object
is the normalized cone margin.

Reduced target:

```text
NORMALIZED-SECTOR-MARGIN:
  prove a positive lower bound for
  (Im(u)^2-Re(u)^2)/|u|^2
  from finite Schur/cell algebra.
```

## E77.5af - Normalized Sector Margin

Build:

```text
E77_5af_normalized_sector_margin_probe.py
E77_5AF_NORMALIZED_SECTOR_MARGIN.md
```

Measure:

```text
normalized cone margin by sigma/mod4,
branch drift and worst-case row,
relation to vertical-model error,
zeta versus planted falsifier.
```

If the normalized margin remains bounded away from zero on zeta and negative
on planted, formulate the finite certificate theorem.  If it drifts to zero,
name the exact phase-drift residual.

Status: completed in `E77_5AF_NORMALIZED_SECTOR_MARGIN.md`.  The normalized
margin separates zeta and planted strongly.  In the tested window zeta stays
above `0.750616233`; planted is negative.  The next theorem-grade target is
a concrete lower bound.

Reduced target:

```text
MARGIN-LOWER-BOUND:
  prove M_N(sigma) >= 1/2 for the zeta cofinal path, or find the exact row
  or residual where that threshold fails.
```

## E77.5ag - Margin Lower Bound

Build:

```text
E77_5ag_margin_lower_bound_probe.py
E77_5AG_MARGIN_LOWER_BOUND.md
```

Measure:

```text
larger zeta windows for worst branch sigma=1 mod2,
interval/check precision sensitivity,
plant threshold failure,
candidate algebraic certificate for M_N-1/2.
```

This is the current finite certificate gate before any delta-envelope claim.

Status: completed in `E77_5AG_MARGIN_LOWER_BOUND.md`.  The candidate
threshold `M_N>=1/2` survives the extended weakest zeta branch
`sigma=1.0` through `N=22`; the planted build fails immediately.  The
threshold is equivalent to a finite quadratic cone.

Reduced target:

```text
QUADRATIC-CONE-CERTIFICATE:
  prove Im(u)>0 and Im(u)^2-3Re(u)^2>=0 from explicit finite Schur/cell
  rational forms.
```

## E77.5ah - Quadratic Cone Certificate

Build:

```text
E77_5ah_quadratic_cone_certificate_probe.py
E77_5AH_QUADRATIC_CONE_CERTIFICATE.md
```

Measure:

```text
explicit real rational forms for u=-theta'/(1-theta),
sign of Im(u),
sign of Im(u)^2-3Re(u)^2,
source term decomposition into theta/theta' real-imag pieces,
zeta versus planted sign failure.
```

If the signs reduce to a smaller numerator residual, name it explicitly.

Status: completed in `E77_5AH_QUADRATIC_CONE_CERTIFICATE.md`.  The threshold
`M>=1/2` is reduced to explicit rational numerators

```text
S=pB-qA,
C=S^2-3(pA+qB)^2.
```

Zeta has `S>0`, `C>=0` on the extended sigma=1 window; planted fails `C`.
The live problem is the sign of these finite Schur/cell numerators.

Reduced target:

```text
CONE-NUMERATOR-SIGN:
  prove S>0 and C>=0, or isolate the mod2 dip residual in C.
```

## Program Reset After E77.5ah

The cone/sign chain E77.5d--E77.5ah is archived as a detector because proving
its positive margin re-enters MW-1/MW-4.  It is not a live proof target.

E77.6 replaces the joint-rate search with the proved diagonal implication:

```text
FIXED-L-WEYL + SAFE-GAMMA-IDENT + OUTER-LIMIT
=> SR-LOG-2SCALE along N(L)/L -> infinity.
```

See `E77_6_ITERATED_LIMIT_IDENT.md` and
`PHASE_77_MISSION_UPDATED.md`.  The live order is now:

```text
E77.7: R2 compact-tail autopsied by the nondecaying coefficient (AT-1);
E77.7b: MU-LIMIT + DIR-MU-FREEZE before direct block growth;
E77.7c: min-max proved conditional on OP-REALIZATION; fixed real-interval
        contraction autopsied by resonance valleys;
E77.7d: OP-REALIZATION and MU-LIMIT closed via an unbounded logarithmic
        diagonal plus bounded discrete-Hilbert commutator remainder;
E77.7e: paired gap anatomy measured; overlap smallness loses to gap collapse.
        Bypass freezing and prove FIXED-MU-BLOCK-GROWTH directly.
E77.7f: compact resolvent forces correction of the old kernel-trivial LP
        wording.  One fixed coupling is refuted; prove moving spectral
        boundary-trace divergence BTG-DIV-L instead.
E77.8: SAFE-GAMMA-IDENT, OUTER-LIMIT, and the common radical diagonal;
audit: plant must first break at SAFE-GAMMA-IDENT/OUTER-LIMIT;
assembly: SAFE-LIMIT-POINT => SAFE-PROLATE-BRIDGE => SR-SAFE => Omega7.
```

## Stop Conditions

Stop only if one of these happens:

```text
Omega7 closes through the assembly chain;
a theorem-grade falsifier kills SHELL-REG and names the next finite object;
Phase 77 reaches the phase-length limit and opens Phase 78 with the sharpest
endpoint preserved.
```
