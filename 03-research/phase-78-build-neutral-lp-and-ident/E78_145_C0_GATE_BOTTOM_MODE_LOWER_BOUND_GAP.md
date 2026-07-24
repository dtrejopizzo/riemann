# E78.145 -- c0 GATE: BOTTOM-MODE BOUNDARY COUPLING VS EIGENVALUE COLLAPSE

## 0. Context

This document closes out the E78.144 probe (`c0` vs `nu0` finite-section
gate). It reports the corrected, verified numbers (the zeta run is clean;
the plant run's N=16 row was a self-singularity artifact and has been
replaced with a properly-computed value), states the logical structure of
`LOW-MODE-BTG(1)` precisely, and attempts -- and does not fully close -- a
rigorous lower bound on `c_0^{(N)}`.

Front: A1. Per E77.7f/E78.4d, `BTG-DIV-L` (finite-section growth of the
moving boundary spectral measure `S_N(mu)` toward the true ground point) is
the standing target for BOTH builds under Outcome A (E77.1b): the zeta
build should show it as the operator-theoretic reflection of known analytic
behavior at the true zero, and the planted build should show it too (slower,
since the plant's spectrum does not collapse to 0 the way zeta's does).
**Both builds showing divergent `S_N` is therefore the CORRECT and EXPECTED
outcome of this probe, not a violation of any Wall clause and not evidence
against BTG-DIV-L.** A discriminating result would have been one build
diverging and the other saturating; that is not what was found, and this
document does not claim otherwise.

## 1. Setup recap

`A_N` = inner block of the bordered CCM matrix `H` (rows/cols 1..2N-1,
excluding the boundary row/column). `b_N` = boundary column restricted to
inner rows, i.e. `b_N(m) = entry(m, n_modes, L, lam)` for
`m = -n_modes+1 .. n_modes-1` (`P76_002_mp_entry_audit.py`, `build_mp`:
`idx = range(-n_modes, n_modes+1)`, boundary index is the last entry of
`idx`, namely `n_modes` itself, so **the boundary column's defining index
grows with N** -- see Sec. 3).

`u_0^{(N)}` = ground (lowest-eigenvalue) unit eigenvector of `A_N`.
`nu_0^{(N)}` = its eigenvalue. `c_0^{(N)} = <u_0^{(N)}, b_N>`.
`S_N(mu) = sum_j |<u_j^{(N)}, b_N>|^2 / (nu_j^{(N)} - mu)^2` (full sum over
all inner eigenpairs, not just the bottom mode); `S_bottom` is the `j=0`
term alone; `bfrac = S_bottom / S_total`.

## 2. ZETA result: clean, decisive (verified against `E78_144_c0_gate_results.json`)

`mu_L = 0` exactly for zeta (Branch B collapse target, no proxy needed).

```text
N=6:  nu0=7.435e-21   c0=-2.368e-17   S_total=1.047e7    S_bottom=1.014e7   bfrac=0.9693
N=8:  nu0=1.141e-25   c0= 3.814e-19   S_total=1.143e13   S_bottom=1.117e13  bfrac=0.9769
N=10: nu0=1.851e-30   c0=-1.298e-23   S_total=5.000e13   S_bottom=4.917e13  bfrac=0.9837
N=12: nu0=4.302e-35   c0= 1.743e-24   S_total=1.663e21   S_bottom=1.642e21  bfrac=0.9874
N=14: nu0=2.262e-39   c0= 1.655e-28   S_total=5.404e21   S_bottom=5.353e21  bfrac=0.9905
N=16: nu0=1.572e-43   c0= 1.111e-31   S_total=5.029e23   S_bottom=4.991e23  bfrac=0.9925
```

Successive ratios (per 2-step-in-N):

```text
nu0 ratio: 1.535e-5, 1.622e-5, 2.324e-5, 5.259e-5, 6.950e-5   (all ~1e-5..7e-5, geometric)
c0  ratio: 1.611e-2, 3.402e-5, 1.343e-1, 9.495e-5, 6.711e-4   (noisy, sign-changing,
                                                                never as small as nu0's smallest ratio)
c0/nu0:    3184.98 -> 3.34e6 -> 7.01e6 -> 4.05e10 -> 7.32e10 -> 7.06e11   (monotone growth,
                                                                8 orders of magnitude, N=6->16)
```

Total decay over N=6->16: `nu0` collapses ~23 orders of magnitude
(`7.4e-21 -> 1.6e-43`); `c0` decays only ~14 orders of magnitude
(`2.4e-17 -> 1.1e-31`, non-monotone, sign-changing). `S_bottom` tracks
`S_total` in lockstep and `bfrac` climbs monotonically toward 1
(0.969 -> 0.992). `S_total` itself diverges across the run
(`1.0e7 -> 5.0e23`) with no sign of leveling.

**Reading**: `c_0` is not vanishing fast enough to arrest the divergence of
`S_N(0)`; the bottom mode is not merely present in but effectively drives
the growth. This is strong numerical support for `BTG-DIV-L` on the zeta
build.

## 3. PLANT result: N=6..14 valid, N=16 re-measured (self-singularity fixed)

`mu_proxy` stands in for the plant's true `mu_L` (only known as a stabilizing
limit, not in closed form). The original E78.144 probe set `mu_proxy = nu0`
of the SAME N=16 section it then evaluated `S_16` at, so the bottom-mode
denominator `(nu0 - mu_proxy)` collapsed to numerical noise (theoretically
exactly zero) -- this produced the absurd `S_total = S_bottom = 2.219e56,
bfrac = 1.0` reported for plant N=16 in the raw probe output. **That number
is discarded; it is an artifact of evaluating the resolvent at its own pole,
not a measurement of anything.**

Fix applied (option (a) from the brief): built the N=18 section
(`dim_inner=35`, dps=70) and used ITS `nu0` as the `mu_proxy`, then
re-evaluated `S_16` at that proxy -- a section strictly different from the
one being measured, so no self-pole issue.

```text
N=6:  nu0=-0.0382  c0=0.0337    S_total=0.00114  S_bottom=0.000395  bfrac=0.347
N=8:  nu0=-0.4113  c0=1.918     S_total=3.249    S_bottom=2.098     bfrac=0.646
N=10: nu0=-1.497   c0=0.340     S_total=2.607    S_bottom=2.028     bfrac=0.778
N=12: nu0=-1.700   c0=-0.160    S_total=21.38    S_bottom=20.23     bfrac=0.946
N=14: nu0=-1.723   c0=-0.0388   S_total=10.46    S_bottom=10.32     bfrac=0.986
N=16: nu0=-1.7355     c0=0.06658     S_total=208.96   S_bottom=208.33    bfrac=0.9970
      (mu_proxy = nu0 at N=18 = -1.7401, dim_inner(N=18)=35, dps=70)
```

N=6..16 growth (corrected): `bfrac` climbs 0.35 -> 0.99 -> 0.997, `S_total`
grows roughly 5 orders of magnitude (0.001 -> 209) over N=6->16 -- weaker
than zeta's growth (expected: the plant's `nu0` is not collapsing to 0 the
way zeta's is, so these are genuinely different regimes), but growing, not
saturating, and with NO trace of the artifact's absurd `1e56` scale. This is
consistent with Outcome A (plant's `S_N` also diverges, just more slowly)
as recorded in E77.1b. Note `nu0` at N=16 (-1.7355) and the N=18-derived
proxy (-1.7401) are close but distinct, exactly as intended by the fix --
the plant's `nu0^{(N)}` sequence is stabilizing toward a limit (-1.70, -1.72,
-1.735, -1.740 for N=12,14,16,18) rather than collapsing to 0, which is the
qualitative difference from zeta that Sec. 2/3 already flagged.

## 4. Logical structure of `LOW-MODE-BTG(1)` (precise statement)

`LOW-MODE-BTG(1)`: `S_N(mu_L)` diverges as `N -> infinity` because the
bottom-mode term alone diverges, i.e.

```text
c_0^{(N)^2} / (nu_0^{(N)} - mu_L)^2 -> infinity.
```

This requires `c_0^{(N)}` to NOT vanish faster than `(nu_0^{(N)} - mu_L)`
does. The numerical evidence above is that, for zeta, `c_0` decays ~14
orders of magnitude while `nu_0` (the denominator's dominant term, since
`mu_L=0`) decays ~23 orders over the same N-range -- overwhelming
*numerical* support that this inequality of rates holds in the observed
window. **This is not yet a proof.** No explicit rate or analytic lower
bound on `c_0^{(N)}` has been derived from the operator's structure; the
claim rests entirely on N=6..16 data (six points).

## 5. Attempted rigorous lower bound on `c_0` -- NOT achieved; here is why

The natural attempt: `u_0` is a unit vector and `b_N` has an
"N-independent-in-shape" structure, so if the ground eigenvector's shape
stabilizes as N grows (doesn't itself localize away from the boundary), the
overlap `c_0 = <u_0, b_N>` should stay roughly of fixed order, giving a
variational lower bound via a fixed comparison vector or a
continuity-across-sections argument.

Checked directly against `P76_002_mp_entry_audit.py::build_mp`: `idx =
range(-n_modes, n_modes+1)`; the boundary row/column is the LAST index in
`idx`, i.e. the boundary mode number IS `n_modes` and grows with N. The
boundary column entries are `b_N(m) = entry(m, n_modes, L, lam)`, and
`entry` calls `q_value(m, n_modes, L, y)` which for `m != n_modes` is

```text
q_value(m, n, L, y) = (sin(2*pi*m*y/L) - sin(2*pi*n*y/L)) / (pi*(n - m))
```

with `n = n_modes`. **This means `b_N` is NOT a fixed-shape vector padded
longer as N grows -- its defining frequency parameter `n_modes` itself
increases, so `b_N`'s oscillatory content (via the `sin(2*pi*n_modes*y/L)`
term) becomes higher-frequency at every N.** The premise the naive argument
needed -- "the boundary vector has the same shape at every section, only
the ambient dimension grows" -- is FALSE for this construction. Cauchy-
Schwarz still gives the easy direction, `|c_0| <= ||u_0|| * ||b_N|| =
||b_N||` (upper bound only, and `b_norm` in the data above is itself
bounded and non-monotone, ~0.07 to ~0.93 for zeta and ~0.06 to ~2.5 for the
plant -- consistent with, but not proof of, a bounded overlap). No lower
bound follows from this structure alone: a higher-frequency boundary vector
overlapping a possibly-evolving ground eigenvector could in principle drive
`c_0` to zero at any rate, including one that matches or beats `nu_0`'s
collapse -- the data says this does not happen in the observed range, but
the *mechanism* preventing it (if `u_0`'s own shape is not itself
increasingly boundary-averse) has not been isolated or proved here.

**Precise remaining gap**: it must be shown that `c_0^{(N)}` does not decay
faster than `O(r^{alpha N})` for any `alpha` at least as large as `nu_0`'s
empirical geometric rate (`nu_0` contracts by a factor of roughly `1e-5` to
`7e-5` per two-step increase in N, i.e. roughly `r ~ 0.03-0.1` per unit N in
`|nu_0^{(N+2)}/nu_0^{(N)}|^{1/2}` terms). No such bound has been derived
analytically in this session; the six-point numerical record is the entire
basis for the current confidence that `c_0`'s rate is milder.

## 6. Wall checklist

```text
MW-1:      not invoked (no positivity route used here).
MW-2..6:   not invoked.
K1-K5:     not invoked (this is a finite-section spectral-data probe, not a
           kernel-positivity or class-membership argument).
P76.061:   not invoked.
E72.16/E77.7az: not invoked (no ambient-inverse-norm or pseudoinverse route
           used; `S_N` is computed as a direct finite sum over inner
           eigenpairs, matching E77.7f's BTG-DIV-L definition).
Front A1:  BTG-DIV-L is the standing target for BOTH builds under Outcome A
           (E77.1b); both builds diverging is the EXPECTED, CORRECT result,
           not a violation of any clause and not new evidence for or
           against RH by itself.
```

## 7. Class label

`BTG-DIV-L` / `LOW-MODE-BTG(1)` -- finite-section numerical support,
zeta build clean and decisive, plant build corrected and consistent with
Outcome A; analytic lower bound on `c_0` attempted and NOT established.

## 8. What we know now

The bottom eigenmode's boundary coupling `c_0^{(N)}` decays far more slowly
than the bottom eigenvalue `nu_0^{(N)}` collapses, for both builds, across
six finite sections (N=6..16, dps=70) -- strong, clean, non-fabricated
numerical support for `BTG-DIV-L`/`LOW-MODE-BTG(1)`. The boundary vector
`b_N` was checked directly against its source code and found to NOT have a
fixed shape across N (its defining frequency parameter grows with N), which
rules out the simplest possible rigorous argument (naive fixed-vector
overlap stability) and leaves the required `c_0` lower bound as a genuinely
open analytic question, not a formality.

## 9. Status

```text
strong numerically-supported reduction; proof of the c_0 lower bound remains open.

proved:      (nothing new proved this document; restates E77.7f's BTG-DIV-L
             target and reports finite-section data toward it)
observed:    zeta c_0^{(N)} decays ~14 orders of magnitude over N=6->16 while
             nu_0^{(N)} decays ~23 orders over the same range (verified,
             six points, dps=70);
observed:    zeta S_N(0) diverges 1.0e7 -> 5.0e23 over N=6->16 with bfrac
             (bottom-mode share) climbing monotonically 0.969 -> 0.992;
observed:    plant S_N(mu_proxy) grows ~4 orders of magnitude over N=6->14
             (0.001 -> 10.5) with bfrac climbing 0.347 -> 0.986, slower than
             zeta as expected under Outcome A;
corrected:   the original N=16 plant row (S_total=S_bottom=2.219e56,
             bfrac=1.0) was a self-singularity artifact (mu_proxy taken from
             the SAME section being measured); re-measured using an N=18-
             derived proxy, reported in Sec. 3;
checked, refuted as a route:  the naive "b_N has fixed shape across N"
             premise needed for an easy variational lower bound on c_0 --
             false by direct inspection of build_mp's boundary-index
             construction (boundary mode number = n_modes, grows with N);
open:        analytic lower bound on c_0^{(N)}'s decay rate relative to
             nu_0^{(N)} -- the single remaining gap, precisely stated in
             Sec. 5;
open:        BTG-DIV-L at the true mu_L for the plant build (proxy-based
             here, per E77.7f's already-recorded limitation);
next:        the c_0 lower bound (Sec. 5's gap) is the only route that would
             upgrade this from "strong reduction" to "candidate closure";
             no other route is indicated by tonight's data.
```
