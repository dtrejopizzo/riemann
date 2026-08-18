# E78.142 - `SOURCE-L2-BOUND` numerical gate: refuted on the audited ladder

**Run:** 2026-07-21.
**Scope:** front B only, live object `SOURCE-L2-BOUND(L,eta)` from E78.136.
**Class:** AUTOPSIA theorem-grade.
**What we know after this doc that we did not know before:** the required
cofinal bound `||y_b(mu)||_2 <= B_{L,eta}` is FALSE on the audited ladder, for
BOTH builds, at `mu=0` (already inside `|mu|<=eta` for every `eta>0`), and the
blowup is not a borderline/precision artifact — it is a clean, dramatic,
monotone-geometric divergence spanning many orders of magnitude. The
mechanism differs between the two builds (spectral-floor collapse for zeta,
an as-yet-unidentified accumulation for plant), but the empirical verdict is
the same: `SOURCE-L2-BOUND` cannot be closed as currently stated.

## 0. Wall checklist

```text
MW-1:  respected. No positivity/Weil-form target appears; this is a raw
       linear-algebra norm measurement.
MW-2:  respected. Inside the fixed-L / Re(s)>1 arithmetic front (build_mp,
       lambda=6, L=6, standard ladder N=6..16).
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No wrong-sign lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral-gap hypothesis is assumed; this document
       measures the consequence of the ABSENCE of a gap (E78.137 Branch B) on
       a specific downstream quantity, and separately documents that the gap's
       presence (plant) does not by itself save the target either.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient bordered-inverse norm is promoted as a proof step; this
       probe MEASURES the ambient inverse-squared-type norm precisely because
       the reduction chain (E78.101-E78.136) asked whether it stays bounded.
P76.061: respected. No inversion of the full logarithmic quotient is claimed;
         this is an audit of one already-isolated finite object, `y_b`.
E72.16/E77.7az: respected. This is front B; build separation is admissible.
       Here both builds fail the target, so no separation is claimed as a
       closure signal, only as an observation (Section 4).
```

## 1. Exact target under test

E78.136 reduced the derivative-specific burden `SAFE-Y-BOUND` to:

```text
SOURCE-L2-BOUND(L,eta):
  there exist B_{L,eta}, N_0 such that
  ||y_b(mu)||_2 <= B_{L,eta}
  for all N>=N_0 and |mu|<=eta.                                    (Y-15, E78.136)
```

where, per E78.103 `(D-11)-(D-16)` (confirmed by direct reading, not assumed):

```text
A = A_N(mu) = H_{L,N}^{inner} - mu I,           (inner block only, per E78.137 G-1)
u = A^-1 s,   v = A^-1 1,
g = R_b (s - s_b 1)                              (mu-independent),
c_b = A^-1 g,
a_b = 2/L + 4(v^T g)/L^2,   b_b = -2 s_b/L - 4(u^T g)/L^2,
h_b = a_b u + b_b v,
alpha_b = 4 (v^T c_b)/L^2,   beta_b = -4 (u^T c_b)/L^2,
y_b  solves  A y_b = h_b + alpha_b s + beta_b 1.                    (D-16)
```

**Correction of the assumed identification in the task brief:** `y_b` is
*not* literally `A_N(mu)^{-2} b_N` for a single fixed vector `b_N`. It is a
more elaborate coupled object: two solves of `A^{-1}` produce `u,v,c_b`
(hence effectively one power of `A^{-1}` acting on `mu`-independent data),
these feed two scalar coefficients `a_b,b_b,alpha_b,beta_b`, which build the
inhomogeneous right-hand side `h_b + alpha_b s + beta_b 1`, and `y_b` is one
further `A^{-1}` solve against *that* right-hand side. So `y_b` is generated
by an effective **two-fold composition of `A^{-1}`** with intermediate
nonlinear (bilinear) coupling through `alpha_b,beta_b`, not a clean
`A^{-2} b`. This matters: it means `||y_b||` is not simply controlled by
`||A^{-1}||^2 ||b||` for one fixed `b}`; the intermediate vectors `u,v,c_b`
also enter the final right-hand side, so any bound has to control the whole
coupled package, not one Neumann series.

`mu_N` in E78.99 `MU-DIR(L,K)` is confirmed (Section 2) to be the same
intrinsic object as E78.137's gate: the ground eigenvalue `nu_0^{(N)}` of the
inner block `A_N(0)`.

## 2. Probe and cross-check

Companion files:

```text
E78_142_source_l2_bound_gate_probe.py
E78_142_source_l2_bound_gate_results.json
```

The probe builds `A_N(mu) = A_N - mu I` (inner block `H[1:-1,1:-1]`, never the
bordered `H` — cross-checked below) via `build_mp` from
`P76_002_mp_entry_audit.py`, exactly reusing the E78.104 machinery, and
evaluates `||y_b(mu)||_2` at `mu=0` and at `mu = nu_0^{(N)}/2` (the midpoint
of `[0,mu_N]`, chosen instead of `mu_N` itself because `mu_N` is by
definition an eigenvalue of `A_N(0)`, so `A_N(mu_N)` is exactly singular).
`L=6`, `lambda=6`, `dps=60`, `N=6,8,10,12,14,16`, both builds.

**Cross-check against E78.137:** at `L=6,N=16`, zeta, this probe's `nu0`
reads `1.572263996555498337e-43`; E78.137's corrected, independently-run
probe reports `nu0 = 1.5722639965554983388e-43` at the same `L,N`. These
agree to the digits both probes report. This confirms the inner-block
convention `(G-1)` is used correctly here (the exact bug named in E78.137
Section 1 — diagonalizing the full bordered `H` instead of `H[1:-1,1:-1]` —
is not present in this probe).

### Zeta (genuine build), `L=6`, `dps=60`

```text
N= 6: nu0=7.43e-21   ||y_b(0)||=4.58e+24   ||y_b(nu0/2)||=1.83e+25
N= 8: nu0=1.14e-25   ||y_b(0)||=4.15e+32   ||y_b(nu0/2)||=1.66e+33
N=10: nu0=1.85e-30   ||y_b(0)||=6.70e+37   ||y_b(nu0/2)||=2.68e+38
N=12: nu0=4.30e-35   ||y_b(0)||=2.00e+46   ||y_b(nu0/2)||=7.98e+46
N=14: nu0=2.26e-39   ||y_b(0)||=7.98e+50   ||y_b(nu0/2)||=3.19e+51
N=16: nu0=1.57e-43   ||y_b(0)||=1.27e+56   ||y_b(nu0/2)||=5.06e+56          (E-1)
```

### Plant (falsifier), `L=6`, `dps=60`

```text
N= 6: nu0=-3.82e-2   ||y_b(0)||=1.30e+23
N= 8: nu0=-4.11e-1   ||y_b(0)||=2.36e+31
N=10: nu0=-1.497      ||y_b(0)||=1.53e+33
N=12: nu0=-1.700      ||y_b(0)||=1.86e+40
N=14: nu0=-1.723      ||y_b(0)||=1.21e+44
N=16: nu0=-1.736      ||y_b(0)||=2.96e+48                                  (E-2)
```

(Both rows match, to the digits shown, the `y_norm` column already present
in `E78_104_coupled_dmu_burden_results.json` at `N=6,8,10,12`; this probe
extends the same measurement to `N=14,16` and to the midpoint `mu`.)

## 3. Reading

```text
1. ||y_b(0)||_2 grows WITHOUT BOUND on the audited ladder for BOTH builds.
   For zeta it grows by roughly 5-8 orders of magnitude per two-step
   increase in N (24 -> 32 -> 37 -> 46 -> 50 -> 56, in log10, across
   N=6..16). For plant it grows comparably (23 -> 31 -> 33 -> 40 -> 44 -> 48
   in log10).

2. At mu=nu0/2, closer to the collapsing floor, ||y_b|| for zeta is
   consistently about 4x larger than at mu=0 -- consistent with, but not
   solely explained by, approach to the singular point A_N(mu_N).

3. For zeta the mechanism has a clean spectral explanation available: nu0
   collapses geometrically to 0 (Branch B, E78.137), so ||A_N(0)^{-1}||
   itself blows up like 1/nu0, and y_b is generated by an EFFECTIVE
   two-fold application of A^{-1} (Section 1), so a naive Neumann-series
   estimate would predict growth on the order of 1/nu0^2. The observed
   growth is large but somewhat SLOWER than 1/nu0^2 (e.g. N=14->16:
   1/nu0 grows by a factor ~1.44e4, 1/nu0^2 by ~2.1e8, but ||y_b|| grows by
   only ~1.6e5) -- so there IS partial overlap decay (the source vectors
   s,1,g are not maximally aligned with the collapsing ground mode), exactly
   the compensating mechanism the task brief anticipated as "plausible."
   But the compensation is only PARTIAL: it slows the blowup from a
   quadratic-in-1/nu0 rate to something closer to 1/nu0^1.2-1.4 empirically,
   not enough to produce a bounded limit.

4. For plant, nu0 does NOT collapse -- it stabilizes at an order-one
   negative value (-1.74 at N=16, matching E78.1/E78.3/E78.137). Yet
   ||y_b(0)|| STILL blows up, at a comparable rate to zeta. This means the
   mechanism named in (3) -- collapsing ground eigenvalue -- is NOT the sole
   or even the dominant driver of the blowup. Something in the coupled
   generator package (most likely the bilinear feedback through
   alpha_b, beta_b, which are built from c_b = A^{-1}g and then themselves
   scale the right-hand side of the FINAL solve for y_b) grows with N even
   when A_N(mu) stays uniformly well-conditioned. This is a genuinely new
   finding not visible in E78.104 (which only tabulated N up to 12 and did
   not track nu0 alongside y_b in the same table).                          (E-3)
```

## 4. Consequence: why this is a refutation, not a stall

`SOURCE-L2-BOUND(L,eta)` requires a single finite `B_{L,eta}` with
`||y_b(mu)||_2 <= B_{L,eta}` for ALL sufficiently large `N`. The data in
`(E-1)`-`(E-2)` shows `||y_b(0)||_2` increasing by more than 30 orders of
magnitude across `N=6..16` at a fixed `L=6`, with no sign of leveling off —
for both builds. No finite `B_{6,eta}` can dominate this sequence. Since
`mu=0` lies in `|mu|<=eta` for every `eta>0`, `SOURCE-L2-BOUND(6,eta)` is
**false** for every `eta>0`, on the audited ladder.

This is decisive enough that no amount of additional precision (`dps`)
changes the verdict: the growth is many orders of magnitude per step, far
beyond what could be a `dps=60` rounding artifact (which would show as noise
at the 60th significant digit, not a clean 5-8-decade-per-step trend, and the
`nu0` cross-check against E78.137's independently-computed values already
confirms the linear algebra is being done correctly on the correct operator).

Therefore the entire reduction chain

```text
E78.101 -> E78.103 -> E78.104 -> E78.134 -> E78.135 -> E78.136 -> SOURCE-L2-BOUND
```

terminates here: `SOURCE-L2-BOUND` is refuted as stated, on the exact ladder
the chain itself uses to justify "candidate closure — pending review" at
every prior step. This is not a new front-B build-separation signal (Section
0, E72.16/E77.7az) — the failure is IDENTICAL in character for zeta and
plant, so it is not the kind of value-level discriminant the falsifier
methodology looks for; it is a plain, build-neutral algebraic blowup in the
generator package itself.

## 5. Exact obstruction, named precisely

```text
The bound SOURCE-L2-BOUND(L,eta) requires y_b(mu) to stay ||.||_2-bounded as
N -> infinity. But y_b solves A_N(mu) y_b = h_b + alpha_b s + beta_b 1, where
h_b, alpha_b, beta_b are themselves built from u=A^-1 s, v=A^-1 1,
c_b=A^-1 g -- i.e. y_b is generated by an EFFECTIVE SECOND application of
A_N(mu)^{-1} to data that is not mu-independent-and-fixed but already grows
with N through the first application. For zeta this compounds with the
Branch-B collapse of nu_0^{(N)} -> 0 (E78.137); for plant, where there is NO
such collapse, it still occurs, which shows the blowup is not reducible to
the ground-eigenvalue story alone -- there is a second, currently
unidentified source of growth intrinsic to the (u,v,c_b) -> (alpha_b,beta_b)
-> y_b bilinear coupling itself.                                            (F-1)
```

The task's proposed rescue mechanisms do not apply as hoped:

```text
1. "mu bounded away from 0 by a fixed amount independent of N" -- does not
   help: at mu=0 (as safely away from the floor as one can choose an
   interior point of a shrinking-in-principle box) the blowup already
   occurs for zeta, and for plant there is no floor to be away from at all,
   yet the blowup still occurs.

2. "Combes-Thomas-type exponential localization of b_N's overlap with the
   near-zero eigenspace" -- this was the anticipated compensating
   mechanism, and Section 3 point 3 shows it IS partially present for zeta
   (the observed growth rate is slower than the naive 1/nu0^2 prediction),
   but it is not strong enough to produce boundedness, and it does not even
   apply to the plant case where there is no near-zero eigenspace to be
   localized away from.                                                     (F-2)
```

## 6. Next live object

The refutation is local to the specific coupled-generator construction of
`y_b` from E78.103. It does not refute `MU-DIR(L,K)`, `PAIRED-DMU-LOCAL`, or
`DMU-COUPLED-GENERATOR` directly — it refutes one specific sufficient route
to them (`SAFE-Y-BOUND` via a uniform `l2` bound on this particular `y_b`).
Two candid next moves, neither attempted in this document:

```text
1. Return above E78.135/E78.136 and ask whether SAFE-H-BOUND + SAFE-Y-BOUND
   can be replaced by a direct bound on the COMBINED quantity
   partial_mu(F_b'/F_b) (E78.104 (L-1)) that exploits CANCELLATION between
   the numerator and denominator branches of that quotient, rather than
   bounding y_b (and hence Y_b, Y_b^bd, Y_b') in isolation. The raw
   |Y_b'|/|F_b| term in (L-5) uses |F_b| in the denominator, and E78.104
   showed F_b itself stays large (min|F_b| ~ 1e3-1e10 on the same ladder,
   (L-10)-(L-11)); a bound of the FORM |Y_b'/F_b| directly, without first
   passing through the triangle inequality that separates Y_b' from F_b,
   might have enough cancellation to survive even though ||y_b||_2 alone
   does not.  This is untested here and is the most promising surviving
   route.

2. Autopsy the second growth mechanism (F-1) directly: track alpha_b, beta_b
   and c_b's growth rate against N independently of nu0, for the plant
   build specifically (where there is no spectral-floor story available),
   to identify what IS driving that blowup.                                 (N-1)
```

## 7. Status

```text
class: PROBE-VERIFIED REFUTATION (of SOURCE-L2-BOUND as stated, on the exact
       ladder its own reduction chain used to claim candidate status).

status: REFUTED on the audited ladder (L=6, N=6..16, dps=60, both builds);
        not merely "unresolved" or "stalled".

proved (by direct computation, cross-checked against E78.104 and E78.137):
  ||y_b(0)||_2 grows by more than 30 orders of magnitude across N=6..16 for
  BOTH the zeta and planted builds at L=6, with no sign of leveling off, so
  no finite B_{6,eta} can bound it cofinally;

confirmed:
  the inner-block convention A_N=H[1:-1,1:-1] is used correctly (nu0
  cross-checked digit-for-digit against E78.137's independently-computed,
  bug-corrected values at L=6,N=16);

corrected (relative to the task's working hypothesis):
  y_b is NOT literally A_N(mu)^{-2} b_N for one fixed vector; it is
  generated by an effective two-fold A^{-1} composition with an
  intermediate bilinear coupling (alpha_b,beta_b built from c_b), and this
  coupling itself appears to carry a second, build-independent source of
  growth beyond the ground-eigenvalue collapse (Section 3 point 4);

partially confirmed:
  for zeta, the observed growth rate of ||y_b|| is slower than the naive
  1/nu0^2 Neumann-series prediction, showing the anticipated overlap-decay
  compensation IS present but is NOT strong enough to produce boundedness;

refuted:
  SOURCE-L2-BOUND(L,eta) via a uniform ||y_b||_2 bound, as the route to
  SAFE-Y-BOUND, DMU-COUPLED-GENERATOR, PAIRED-DMU-LOCAL, and hence MU-DIR;

not refuted (out of scope of this document):
  MU-DIR, DMU-COUPLED-GENERATOR, or PAIRED-DMU-LOCAL themselves -- only this
  one sufficient sub-route to them, isolated across E78.101-E78.136, fails;

next:
  attack partial_mu(F_b'/F_b) directly via cancellation between numerator
  and denominator (N-1.1), since F_b itself is confirmed large and
  non-collapsing on the same ladder where y_b blows up; or autopsy the
  second (non-spectral) growth source in the (u,v,c_b)->(alpha_b,beta_b)
  coupling, visible cleanly in the plant data where no spectral floor
  exists to blame (N-1.2).
```
