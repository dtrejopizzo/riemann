# Phase 79 - The shared convergence lemma (GAP-Z) and the IDENT discriminant

**Opened:** 2026-07-22. Continues `phase-78-build-neutral-lp-and-ident/`.

## Why this phase exists

Phase 78 (with the program author's spectral-shift reformulation) collapsed the
program's diffuse open frontier into **two precisely-stated analytic objects**
and closed/reduced the rest. Everything now hangs on:

```text
(H1) GAP-Z        -- the shared CONVERGENCE lemma (build-neutral).
(H2) DISCRIMINANT -- the arithmetic identification where the plant must fail.
```

Phase 79 attacks exactly these two, and assembles the conditional theorem they
feed. No other object is primitive anymore.

## Entry state (what phase 78 established -- read before starting)

Proved / verified (with documents):

```text
- Spectral-shift identities (E78.152, verified to 1e-37; kappa_j REAL):
    T_N'/T_N = Tr(zI-K_N)^{-1} - Tr(zI-D)^{-1} - 1/(z-d_{b,N}),
    D=diag(d_j), d_j=2pi n_j/L, x=A_N^{-1} b, q_j=d_j-d_{b,N}, c=1-sum x_j,
    K_N = D + (1/c) x q^T,  d_{b,N}=2pi N/L  (MOVING boundary, E78.7 erratum).
  This K_N object is INDEPENDENT of the target Gamma/cell derivative -- it
  escapes the projective-flatness circularity (E78.150).
- Three-way decomposition (E78.157, exact):
    g_{N+2}-g_N = ZERO + MESH + BND,  g_N=2Re(i (log T_N)'(i sigma)).
    MESH = O(sigma/N^2)  PROVED, build-neutral (bit-identical both builds);
    BND  = O(sigma/N^3)  PROVED, build-neutral;
    ZERO = Poisson sum over spec(K_N), the SOLE build-dependent piece.
- Point 7 (OUTER-LIMIT): CLOSED conditional on point 6's identity (E78.151, via
    P76.039 theorem-grade Euler tail).
- Point 2 (Weyl response): ambiguity CLOSED (residue-normalized response,
    E78.151); existence numerically validated via PROJECTIVE-SOURCE-CONVERGENCE
    (E78.156), which sidesteps BOTH the c_0 lower bound (E78.146) and ground-state
    simplicity. Cauchy-row separation reduces uniqueness to (I-3) (E77.7i).
```

Honest corrections carried in (do NOT re-tread):

```text
- E78.7 WL-7 false: boundary pole does not cancel (d_{b,N} moves); increment is
  O(N^-2), summable, kept explicit.
- E78.150: relative projective flatness against an INTEGRATED primitive is a
  reformulation, NOT independent forcing (Borel-Caratheodory both ways). Only an
  INDEPENDENT cell object (the K_N determinant/Schur form) counts -- which E78.152
  supplies.
- E78.154: the "single stable escaped eigenvalue avatar" was RETRACTED. K_N's
  whole spectrum is a near-symmetric real cloud pushed outside the mesh (c small);
  the far outlier is negligible to the transfer (E78.155).
- E78.157: the clean N^-2 of the OBSERVABLE is carried by the rigorous MESH term.
  The hard build-dependent piece ZERO is SLOWER: N^2*ZERO rises (zeta 0.28->0.66
  over N=8..24, p~1.2 borderline; plant wanders ~2). "Clean N^-2 per piece" is dead.
```

## The exact conditional chain and the two holes

```text
[ GAP-Z ]  ==> convergence halves of points 2, 5, 6 (one lemma, E78.156 unification)
[ DISCRIMINANT ] ==> SAFE-GAMMA-IDENT arithmetic identification (plant fails)
GAP-Z + DISCRIMINANT ==> IDENT (fixed-L Weyl + safe-gamma-ident + outer-limit)
IDENT + LP + RDP-SHELL + (PROLATE+WEIL-TAIL) ==> SAFE-LIMIT-POINT ==> ... ==> Omega7 ==> RH
```

Phase 79 owns GAP-Z, DISCRIMINANT, and their assembly into IDENT. LP and the
Front-C pairing remain separate tracks (status note at the end).

---

## HOLE 1 -- GAP-Z (the shared convergence lemma)

**Statement.** On safe compacta `K subset (1/2, infinity)`, both builds,

```text
GAP-Z:  ZERO(sigma) = sum_{kappa in spec K_{N+2}} 2 sigma/(kappa^2+sigma^2)
                    - sum_{kappa in spec K_N}     2 sigma/(kappa^2+sigma^2)
        is summable in N, locally uniformly in sigma.
```

If GAP-Z holds, then `sum_N |g_{N+2}-g_N| < infinity` (MESH, BND already O(N^-2),
O(N^-3)), so the fixed-L log-transfer converges -> convergence halves of points
2, 5, 6 all CLOSE.

**No-go constraints established (do not attempt):**
```text
(W1) A crude |ZERO| = O(N^-2) bound is FALSE (ZERO ~ N^-1.2 observed).
(W2) Herglotz/interlacing is dead (E78.148, residues sign-mixed). "Clean N^-2 per
     piece" is dead. The live object is the RATE of spectral-cloud convergence.
```

**Key structural handle.** The `kappa_j` are the real roots of the secular
equation (from `F_N=0`, `F_N = c - sum_j r_j/(z-d_j)`):

```text
SEC:  sum_j r_j/(z - d_j) = c,   r_j = q_j x_j = (d_j - d_{b,N}) x_j  (real).
```

`c` is tiny for zeta (~1e-7..1e-10), so `kappa_j ~ roots of sum_j r_j/(z-d_j)=0`.
The Poisson kernel weights the NEAR-ORIGIN roots most; `ZERO` is the movement of
those roots under `N -> N+2`. The residues `r_j` sample arithmetic data through
`x_j=(A_N^{-1} b)_j`, and on the safe axis `s=1/2+sigma>1` the arithmetic series
converge ABSOLUTELY (P76.039, theorem-grade).

### Milestones

**E79.1 -- Nail the ZERO exponent (DECISIVE, do this first).**
Extend `ZERO(sigma)` to N=40+ (dps 70-80), multiple sigma, both builds. Fit the
true asymptotic form: is it `N^{-p}` with a fixed `p>1` (summable), `N^{-1}
polylog`, or marginal `~N^{-1}` (NOT summable)? This decides whether GAP-Z is even
TRUE. If ZERO is marginal/non-summable, that is a MAJOR finding (finite-section
convergence is conditional) and reshapes everything -- report it loudly. Probe:
Richardson/López-type extrapolation on `N^p ZERO`; report `p` with error bars.

Current gate status (E79.1 partial, honest):

```text
- dps=50 is NOT admissible for the extended run: it generates a fake zeta-side
  blow-up starting at N=20, contradicting the certified E78.157b anchor.
- dps=60 is stable through N=24 and reproduces the Phase-78 anchor exactly for
  both builds.
- On that stable range, zeta remains consistent with a borderline summable law
  p just above 1; there is still no evidence for clean N^-2 per piece and still
  no evidence for genuine non-summability.
- The mechanical bottleneck is raw build_mp cost, not the ZERO post-processing.
```

**E79.2 -- Exact near-origin-root representation of ZERO.**
Prove `ZERO = sum_{roots near 0} [P(kappa^{(N+2)}) - P(kappa^{(N)})] + (far tail,
proved small)`. Pair each near-origin root of section N with its section-(N+2)
partner (roots are real; use the secular-equation continuity in the added modes).
Deliver `ZERO = sum_r P'(kappa_r) delta kappa_r + O(...)`, delta kappa_r = root
displacement. This turns GAP-Z into a root-displacement sum.

Current gate status (E79.2 first autopsy):

```text
- The naive finite-packet version is FALSE as a useful reduction.
- On the zeta side, the first few roots nearest the origin freeze extremely
  fast and contribute essentially nothing to ZERO beyond the earliest steps.
- So the live content is not a fixed finite near-origin packet; it sits in a
  cofinal cloud/tail. Any honest E79.3 route must be cloud-level or use a
  packet whose width grows with N.
```

**E79.3 -- Arithmetic bound on root displacement (route D, the live handle).**
Bound `delta kappa_r` (near-origin root movement N->N+2) by the added-mode
contribution to SEC: the new modes at scale ~N change `sum_j r_j/(z-d_j)` by
`r_{new}/(z - d_{new})` with `d_{new} ~ 2 pi N/L` and `r_{new} = (d_{new}-d_b)
x_{new}`. Use absolute Euler convergence (P76.039) to bound `x_{new}` and hence
`delta kappa_r`. Target: a rigorous `|ZERO| <= C(K)/N^p`, `p>1`, matching E79.1's
measured exponent. This is the genuine open analytic problem; if the honest
outcome is a borderline `p=1` with a log, state it exactly.

Current gate status after E79.2/E79.3a:

```text
- Not a fixed finite packet near the origin (E79.2).
- Not even a narrow cofinal packet ordered by |kappa|: on the zeta side,
  capturing 50% of ZERO already needs about 80%-85% of the common cloud, and
  90% needs essentially the whole common cloud (E79.3a).
- The honest surviving decomposition is:
     ZERO = common-cloud displacement + explicit extra-root contribution.
- The extra-root contribution is the easy part numerically: on both builds it is
  compatible with a clean N^-2 law, so the hard content localizes to the
  common-cloud displacement term (E79.3b).
- Inside the common-cloud term, the zeta side is outer-shell heavy, but not by
  any fixed shell width: the last 8 common shells carry ~99% at N=8 but only
  ~67% by N=16, so the honest geometry is a GROWING outer layer plus interior
  remainder, not a fixed-width edge law (E79.3c).
- That outer layer can now be quantified more sharply: on the zeta side the
  shell thickness needed to capture 50%, 90%, 99% of ZERO^common grows only
  slowly (m50 = 4,4,5,6,7 and m90 = 7,8,9,10,11 across N=8..16), far below the
  full common-cloud dimensions 15,19,23,27,31. So the live object is now a
  slowly growing outer layer plus an interior remainder (E79.3d).
- That reduction sharpens once more after removing the minimal outer layer:
  on the zeta side the leftover interior remainder after the 99% layer is
  already below 1% of the common-cloud total on the whole audited ladder.
  So the honest surviving object is a slowly growing outer layer plus a tiny
  interior correction, not two comparably-sized pieces (E79.3e).
- The outer layer itself now has a concrete local form: for fixed depth from
  the edge, the zeta-side shell coefficients are compatible with a stable
  N^-2-scaled profile, while the planted build has no comparable collapse.
  So the live common-cloud object sharpens again to a local N^-2 shell law on
  a slowly growing outer edge plus a tiny interior correction (E79.3f).
- The borderline size of that object now has a concrete mechanism: on the zeta
  side, `N |ZERO^common|` is numerically explained by
  `[active edge width ~ cN] x [one shell ~ const/N^2]`. So the surviving
  problem is no longer why the exponent is near `1`, but where the extra gain
  must come from to beat this raw edge budget (E79.3g).
- That edge-budget mechanism survives the extended ladder through `N=24`:
  `N |ZERO^common|` stays in a narrow band, the budget proxy keeps tracking it,
  and the relative active width `m90/N` does not drift upward. So the
  borderline edge budget is not a short-ladder artifact anymore (E79.3h).
- Replacing the raw shell count by an effective width does give a real discount,
  but only by a moderate constant factor: on the zeta side the effective width
  is typically about `0.76 m90` (or about `0.64 m99`), still linear in `N`.
  So the missing summability gain is not hiding in a dramatic collapse from raw
  width to effective width (E79.3i).
- Normalizing depth by the active width also does not produce a quick escape:
  the zeta-side edge profile is not a simple monotone decay from the boundary
  inward, but a broad plateau through much of the active edge, with strong
  decay only near the deepest part. So the missing gain is unlikely to come
  from a naive normalized-depth profile either (E79.3j).
- Local signed cancellation also fails as an escape hatch: on the zeta side the
  active edge is essentially fully coherent in sign at pair and size-4 block
  scales, with only a small alternating-sum reduction. So the missing gain is
  not hiding in short-range shell-by-shell oscillation either (E79.3k).
- The first nontrivial global scale match appears elsewhere: the deepest quarter
  of the active 99% edge enters the same scale as `ZERO^extra`, while the tiny
  interior remainder stays far too small to be the relevant partner. So the
  next honest coupling object is `deep edge tail <-> extra-root`, not
  `deep edge tail <-> remainder` (E79.3l).
- That coupling is real in the signed sense: the observable `Q4 - ZERO^extra`
  can become very small and shows the first genuine global cancellation seen so
  far, but the effect is not yet uniform across the audited ladder. So the live
  task is now to find the right deep-tail normalization or mesoscopic cut that
  stabilizes this cancellation (E79.3m).
- A mesoscopic tail sweep improves that picture: much shorter terminal tails,
  around 20%-30% of the active 99% edge, pair with `ZERO^extra` far better than
  the crude last quartile. But no single fixed fraction is yet uniformly
  optimal, so the next task is to find the intrinsic rule that selects the
  correct short tail non-resonantly (E79.3n).
- A natural intrinsic candidate already failed: selecting the terminal tail by
  cumulative absolute edge mass performs systematically worse than the best
  length-based mesoscopic tail. So the right selector is not "how much mass is
  in the tail", but something more geometric or scale-matched (E79.3o).
- A geometric selector by profile height is more promising but still incomplete:
  a threshold around `tau ~ 0.4` repeatedly marks a plausible deep-tail onset,
  yet it does not uniformly beat the best fixed-fraction mesoscopic tail. So the
  right intrinsic selector likely needs a second matching condition, not just a
  raw profile threshold (E79.3p).
- A first hybrid rule confirms that the onset marker is real but incomplete:
  using `tau ~ 0.4` plus a short admissible window recovers some of the best
  deep-tail / extra-root cancellations, but still does not uniformly dominate
  the pure length sweep. So the missing ingredient now looks like an adaptive
  window rule layered on top of the geometric onset (E79.3q).
- That adaptive window rule can now be written as an internal optimization:
  starting from the `tau ~ 0.4` onset, choose the terminal suffix that best
  matches `ZERO^extra` in signed scale. This formalizes the hybrid selector, but
  still does not uniformly beat the pure length sweep, so one more structural
  ingredient is still missing (E79.3r).
- A simple shortness penalty does not supply that missing ingredient: adding a
  linear penalty in tail length leaves the selected tau-onset tails unchanged on
  the audited zeta ladder. So the remaining ambiguity is not "too long vs too
  short", but which already-short tail is structurally correct (E79.3s).
- A naive local slope trigger also fails to settle that ambiguity: it mostly
  reproduces the same short tails as the hybrid rule, but can over-cut and
  destroy the cancellation. So the missing selector ingredient is not a
  one-step drop condition either (E79.3t).
- Mesoscopic smoothing of that same suffix geometry also fails: a short
  height-plus-slope window score always collapses back to the same 2-shell tail
  on the audited zeta ladder. It fixes the worst one-shell slope misfire, but
  loses the good longer selections at `N=10` and `N=14`, so the missing
  ingredient is not just a 2-4 shell averaging of the same local signals
  either (E79.3u).
- The first genuinely better non-suffix object is now on the table: a union of
  two short terminal blocks beats every contiguous suffix family tested so far,
  and it is exactly what resolves the hard zeta-side cases `N=12` and `N=16`.
  So the live deep-edge / extra-root coupling object is no longer "which short
  suffix?", but "which tiny terminal packet geometry?" (E79.3v).
- That packet geometry can be reduced again: on the audited zeta ladder the
  two-block object collapses to a tiny sparse packet on the last few shells,
  often of support size `1` or `2`. This is the smallest common-cloud object
  reached so far, though it is still not a clean discriminant because the plant
  also shows strong sparse-packet matches at low `N` (E79.3w).
- The cheapest intrinsic explanations for that packet are now ruled out:
  neither terminal amplitude ranking nor ranking by the largest local drops
  recovers the sparse support except in isolated cases. So the live object is
  not determined by any one-point terminal score; the next candidate has to be
  a slightly richer terminal moment or short-pattern statistic (E79.3x).
- A fixed tiny motif catalog is also too rigid: patterns like `111`, `101`, or
  a distinguished singleton inside the last 4-6 shells do not recover the
  sparse packet on the hard zeta-side cases. So the live object is not a fixed
  terminal motif either; it needs a more elastic terminal statistic
  (E79.3y).
- Terminal cumulative-mass quantiles are still too monotone: they recover the
  sparse packet only in the isolated `N=12` zeta case and miss the harder
  `N=14,16` geometry. So the live object is not governed by a simple cumulative
  mass rule either; what remains must be a more relational terminal statistic
  (E79.3z).
- Simple terminal barycenters fail in essentially the same way: they recover
  the isolated `N=12` singleton but still miss the harder `N=14,16` geometry.
  So the live object is not a center-of-mass rule with a first dispersion
  correction either; the next candidate has to be explicitly non-monotone and
  pattern-sensitive (E79.40).
- A greedy non-monotone selector with explicit proximity repulsion also fails:
  it collapses back to the same wrong singleton choices in the hard zeta-side
  cases and does not recover the disconnected `N=16` support. So the live
  object is not a simple local-peak selector with adjacency penalty either
  (E79.41).
- A short relational energy on supports of size at most 3 also fails: even with
  an explicit separation bonus, it still misses the hard zeta-side cases and
  does not recover the sparse packet benchmark. So the live object is not
  governed by any simple low-complexity support energy of that kind either
  (E79.42).
- Once ZERO^extra is allowed into the objective directly, the zeta-side packet
  is almost completely reconstructible by raw coupled matching alone. But every
  winning rule uses zero geometric penalty, so the remaining difficulty is no
  longer finding a packet at all; it is understanding whether any nontrivial
  universal refinement of raw coupled matching exists (E79.43).
- Strengthening the selector to one common support across
  sigma in {0.75,1.0,1.5,2.0} does not break that degeneracy: on the audited
  zeta ladder the very same supports from E79.43 remain optimal for both mean
  and max multisigma mismatch, and nonzero block-count / support-size penalties
  still never win. So the raw coupled packet is not a one-sigma accident;
  the next honest refinement has to be richer than these small geometric
  penalties (E79.44).
- Peeling the best multisigma packet also does not uncover a second packet:
  on the audited ladder, for both builds, the optimal second support inside the
  same terminal-window grammar is the empty set. So the first raw packet is not
  just the first item in a longer packet expansion; within this grammar it is
  the only packet-level object, and the residual front must now be formulated
  differently (E79.45).
- The zeta-side packet sequence also resists the simplest support-only transport
  laws: no fixed rule of the form "shift by -1/0/1 and add/remove a tiny
  permanent set" reproduces the audited local support sequence, and the best
  such rule misses every transition. So the next transport object, if it
  exists, has to use signed shell weights or residual data, not support
  combinatorics alone (E79.46).
- After fixing the first raw packet, the remaining mismatch already behaves like
  a smooth one-parameter sigma profile on the zeta side: every audited zeta row
  is monotone in sigma with small normalized curvature, while the planted build
  loses that regularity on the hard sections N=8,10,14. So the next honest
  object past the packet is a residual sigma-profile law, not another support
  law (E79.47).
- That residual profile sharpens further: on the audited zeta ladder it is
  already very well captured by a least-squares affine function of sigma
  (normalized max error about 0.004-0.033), while the planted hard sections
  N=8,10,14 have much larger affine error (about 0.23-0.50). So the next live
  object can be named more concretely as an affine sigma-profile with
  section-dependent coefficients (E79.48).
- The first transport law inside that affine profile already closes on the zeta
  side: the residual slope satisfies an N^-1 band with N|a_N| in the narrow
  range 0.0278-0.0388, while the planted hard rows sit far outside that scale.
  So the residual burden has now shifted from the slope to the intercept / the
  right centered-sigma parametrization of the affine law (E79.49).
- The centered-sigma escape route is now dead: sweeping sigma0 in
  a_N (sigma-sigma0) + c_N(sigma0) does not stabilize the zeta-side level at
  all. The best zeta band already occurs at the left edge sigma0=0.75, and every
  more central choice is worse. So the level burden is real, not a coordinate
  artifact (E79.50).
- Subtracting the ladder mean does not rescue that level burden either: the
  zeta-side deviations N|dc_N| after mean subtraction are still dominated by the
  same hard rows N=10 and N=16, and the absolute deviation band actually gets
  worse rather than better. So the residual level is shaped, not merely shifted,
  and the next honest ansatz is a richer residual template rather than another
  normalization trick (E79.51).
- That richer ansatz is now on the table and it works strikingly well on the
  audited zeta ladder: adding one fixed quadratic mode in sigma to the affine
  residual template drives the zeta fitting error down to about 1e-6-1e-5 and
  leaves a curvature coefficient with N^2|g_N| on the modest scale
  0.096-0.185, while the planted hard rows remain far outside that regime. So
  the residual side has now effectively reduced to a primitive packet plus a
  transported slope and one fixed curvature mode (E79.52).
- The transport scale of that curvature mode is now identified and it is even
  cleaner than the naive guess: the best audited band is N|g_N|, not N^2|g_N|.
  On the zeta side N|g_N| stays in the narrow range 0.0101-0.0141, while every
  tested power leaves the planted hard rows wildly off-scale. So both the slope
  and the curvature mode now transport on the same N^-1 scale, and the
  unresolved residual burden has been pushed almost entirely into the level term
  (E79.53).
- A stronger compression attempt then fails in an informative way: freezing the
  zeta-side transported means for the slope and curvature modes does NOT reduce
  the residual to a single per-section level. So the right next object is not a
  scalar ladder on top of two global constants, but the sectionwise N-dependence
  of the transported coefficient pair itself (E79.54).
- That coefficient pair now collapses much further than E79.54 suggested: on
  the audited zeta ladder `(N a_N, N g_N)` lies on a single signed ray through
  the origin to sub-percent relative error, with
  `|N a_N|/|N g_N| ~ 2.75`, while the planted build shows no comparable
  one-ray geometry. So the live burden is no longer a genuinely 2-parameter
  transport law; it has reduced to one scalar amplitude along a fixed modal ray
  plus a tiny transverse defect (E79.55).
- The first post-ray audit is also now done: the scalar amplitude along that
  modal ray is indeed the live burden, because it does NOT collapse further to
  a trivial constant-scale or tiny sign law on the audited zeta ladder. So the
  right next object is no longer the ray direction, but the intrinsic scalar
  law behind `rho_N` and its relation to the terminal packet / edge geometry
  already isolated earlier in the phase (E79.56).
- That comparison has now been made at the first honest level: `rho_N` is not
  simply the first-packet mismatch or the sparse packet / extra-root residue
  under another name. There is only moderate anticorrelation, not rowwise
  identification. So the packet front and the modal-ray front remain adjacent
  but genuinely distinct, and the next target must compare `rho_N` to more
  primitive shell observables rather than to already-compressed packet scores
  (E79.57).
- That primitive comparison now exists too: `rho_N` is not controlled by crude
  edge size variables like total common mass, raw active width, or effective
  width. Its strongest audited link is instead to edge intensity, especially
  the average `N^2` shell size on the active 90% edge. So the next scalar-law
  target has narrowed from generic edge geometry to signed or weighted
  edge-intensity moments (E79.58).
- That moment audit is now partly resolved: `rho_N` correlates more strongly
  with global moments of the normalized edge profile than with local
  alternating cancellation. The best audited candidates are the front-vs-back
  gap, the profile slope, and the profile centroid. So the next scalar-law
  target is no longer "some intensity statistic", but a tiny explicit family of
  profile moments (E79.59).
- The first explicit predictor is now on the table: one-moment affine laws in
  `front_back_gap` or `profile_slope` already capture a real fraction of
  `|rho_N|`, and the two-moment law `front_back_gap + profile_slope` improves
  further to about 10% max relative error on the audited zeta ladder. So the
  scalar-law search is now genuinely low-dimensional, but not yet closed
  (E79.60).
- That predictor has now been sharpened and cleaned up: the planted diagnostic
  must be evaluated on the planted profile itself, and under that correction
  the cross-build failure remains. On the zeta side, the best current law is no
  longer pure shape, but an affine pair `profile_slope + active-edge intensity`,
  which lowers the audited max relative error to about 6%. So the remaining
  burden is now a small correction to a shape-plus-intensity law, not a search
  over new families of observables (E79.61).
- The first one-coordinate correction has now been audited too: a third
  coordinate can almost close the audited zeta ladder, but robustness matters.
  `centroid` is the sharpest interpolant, while the first terminal shell
  `edge0` is the more stable correction under leave-one-out. So the next target
  is not a generic third moment, but the invariant meaning of a one-shell
  correction to the current `profile_slope + intensity` law (E79.62).
- That locality question is now resolved at first pass: the correction is
  genuinely first-shell local. Neighboring shells, short boundary averages, and
  simple first differences / ratios all perform worse under leave-one-out than
  `edge0` itself. So the live question is no longer whether the correction is
  broad or local, but what invariant shell-algebra object `edge0` is actually
  measuring (E79.63).
- That invariant reading is now sharper too: the correction is better captured
  by the first-shell value relative to the active-edge intensity scale than by
  the raw shell value itself. So the live object is no longer plain `edge0`,
  but a scale-free first-shell deficit `1 - edge0/intensity` attached to the
  common-cloud boundary (E79.64).
- That scale-free defect already has a natural bookkeeping home: on the audited
  zeta ladder it is almost perfectly aligned with the shortest cumulative edge
  prefix data from E79.3f. So the correction front is no longer an isolated
  shell anomaly, but a prefix-deficit coordinate in the existing common-cloud
  algebra (E79.65).
- The final ambiguity in that side branch is now resolved too: the prefix
  reading is geometrically correct, but the usable predictor coordinate is not
  any raw prefix fraction or raw prefix-gap increment. The coordinate that
  preserves the best audited stability is the scale-matched first-prefix defect
  `edge0/intensity` (equivalently `1-edge0/intensity`). So this branch is now
  reduced as far as the current ladder honestly allows, and the natural next
  move is to treat it as descriptive support rather than keep mining nearby
  scalar variants (E79.66).
- The main common-cloud front also tightened again: the sparse terminal packet
  from E79.3w is not a one-sigma fluke. On the audited zeta ladder, exactly the
  same best sparse support is selected at `sigma=1` and `sigma=2` in every
  tested section, while the plant shows no comparable transport rigidity. So the
  live common-cloud object is no longer merely a sparse packet, but a
  sigma-transported sparse packet; the next honest burden is to recover that
  support by an intrinsic terminal statistic rather than subset search
  (E79.67).
- That next burden is now sharper by exclusion too: a fairly broad family of
  cheap sigma-aware one-point selectors built from local shell size, one-step
  drop, local curvature, and mild tail bias still misses the transported sparse
  support in every audited zeta section. So the missing support rule is not a
  local prominence score with sigma coupling; it has to be genuinely relational,
  capable of preferring late and even disconnected terminal support (E79.68).
- The first relational compression is now on the table: once support is chosen
  by cumulative matching to `ZERO^extra` across `sigma=1,2`, the transported
  sparse packet always lies inside a tiny family of candidates
  (terminal suffix, bounded-gap pair, short triple), and this family recovers
  the exact zeta-side support in all audited sections. The only remaining
  ambiguity is internal to that family, most visibly at `N=10`, where the best
  global cumulative matcher is a suffix while the transported sparse packet is a
  singleton. So the next honest burden is to resolve that branch ambiguity with
  one intrinsic relational selector rather than broad subset search (E79.69).
- That branch ambiguity is now reduced again: a single linear penalized score on
  the E79.69 tiny family already selects the correct audited zeta-side support
  in all five cases, including the hard `N=10` singleton. So the live burden is
  no longer to choose among suffix/pair/triple by hand, but to explain why that
  specific tradeoff between mismatch, support size, span, disconnectedness, and
  terminal depth is structurally the right one rather than just sweep-discovered
  (E79.70).
- That tradeoff is now more than a single lucky tuple: in a local box around the
  E79.70 coefficients there is a substantial region of exact `5/5` solutions,
  all preserving the same sign pattern
  `cardinality < 0`, `span > 0`, `gaps < 0`, `start > 0`. So the live burden is
  no longer "find coefficients", but explain this stable gain-vs-cost sign
  pattern structurally and normalize it into a more invariant selector (E79.71).
- That normalization is now done, and it corrects the reading of the selector:
  because `span = card + gaps`, the E79.70 rule collapses exactly to
  `mismatch - 0.22 card + 0.14 gaps + 0.36 start`, still with exact `5/5`
  audited recovery and a substantial exact local box (`276/6048` points). So
  the live selector is no longer a five-term fit and it does NOT contain a
  disconnectedness bonus in normalized form. The honest reduced content is:
  mismatch, a mild support-size reward, a mild spread/disconnectedness cost,
  and a stronger terminal-delay cost. The next burden is to derive that reduced
  gain-vs-cost law structurally rather than by coefficient sweep (E79.72).
- That structural reading can now be sharpened one step further: the normalized
  selector is exactly `mismatch + surcharge`, where the surcharge depends only
  on support geometry and is dominated by terminal delay. In particular, the
  hard `N=10` branch is no longer mysterious: the later suffix wins on raw
  mismatch, but its advantage is too small to pay the extra geometric
  surcharge, so the singleton survives. The live burden is therefore not to fit
  more coefficients, but to derive this depth-complexity surcharge from the
  common-cloud / extra-root coupling itself (E79.73).
- The cheapest constructive interpretation of that surcharge is now dead:
  the normalized selector is not generated by a naive one-step shell
  acceptance rule. A free greedy descent collapses to the very first active
  shell in every audited zeta row (`0/5` exact), while a terminal-anchored
  greedy grows all the way to the full active edge (`0/5` exact). So the
  failure is structural and comes from opposite pieces of the score: the start
  penalty dominates before any packet geometry forms, while terminal anchoring
  lets the cardinality reward overfill the packet. The next honest burden is
  therefore no longer a raw shellwise selector, but a mesoscopic two-stage
  rule: first choose the right anchor/family geometry, then apply the
  mismatch-versus-surcharge comparison there (E79.74).
- That mesoscopic family can now be shrunk once more before any fitted score is
  used: in the plane `(mismatch, surcharge)`, one member of the
  suffix/pair/triple family is already Pareto-dominated on every audited zeta
  row, so the live branch is never genuinely ternary. After removing the
  dominated point, the selector is choosing between at most two frontier
  packets: a mismatch-efficient compact packet and a geometry-cheaper sparse
  packet. So the next honest burden is not to derive a 3-way family rule, but
  to explain the choice along this 2-point frontier (E79.75).
- That 2-point frontier already scalarizes almost completely: on the genuine
  tradeoff rows, the winner is determined exactly by whether the mismatch gain
  per unit surcharge increase is above or below `1`. So the live selector is
  now no longer a multi-parameter family score at all; after removing
  dominated points, it is a unit-threshold comparison on a 2-point frontier,
  with only the degenerate rows collapsing to pure mismatch or exact support
  duplication (E79.76).
- The mismatch side of that frontier rule now collapses once more: on the
  genuine tradeoff rows, each frontier candidate carries an almost
  sigma-independent signed excess factor `eps` relative to `ZERO^extra`, with
  rigidity defects at or below about `1e-3` on the audited ladder. So the
  two-sigma mismatch is no longer best read as a separate max over sampled
  sigmas; it is already the absolute value of one mesoscopic overshoot scalar
  attached to the packet. The live burden is therefore sharper again: explain
  why reducing `|eps|` trades against surcharge at unit rate (E79.77).
- The geometric side has now been audited just as hard, and the contrast is
  sharp: unlike the mismatch side, the surcharge does not collapse to one
  scalar on the genuine tradeoff rows. It has an exact two-mode decomposition
  `0.36(start-card) + 0.14 span`, and different rows activate different mixes
  of those modes (`N=10` mixed with opposite signs, `N=12` mixed in the other
  direction, `N=16` pure anchor-minus-mass). So the easiest hope is dead:
  E79.76 is not a one-variable balance law on both sides. The honest remaining
  burden is asymmetric: one scalar `|eps|` on the mismatch side traded against
  an exact two-mode geometric cost at unit rate (E79.78).
- The coefficient-forcing question is now also settled in the honest direction:
  the audited frontier rows do not determine the geometric weights uniquely.
  They only cut out an open cone in coefficient space, given on the live rows
  by inequalities like `-a+3b > 0.02078`, `2a-3b < 0.33072`, and
  `a < 0.37860`. In the coarse audited box `a,b in {0.00,...,0.80}`, there are
  `2793` admissible pairs, and `(0.36,0.14)` is just one interior point. So
  the next honest burden is no longer "recover these coefficients from the
  winner data", but identify the extra normalization or exact packet identity
  that selects this point inside the admissible cone (E79.79).
- A simple robustness principle also fails to pick the current point. On the
  same audited cone, the maximin margin point is `(0.00,0.14)`, not
  `(0.36,0.14)`, and its minimum decision buffer is vastly larger. So the
  current coefficients are not being selected by crude cone robustness either.
  If `(0.36,0.14)` is canonical, that canonicity has to come from a sharper
  exact structure than winner preservation or max-margin tuning (E79.80).
- The remaining degenerate rows also add no new selection information. `N=14`
  is a literal support duplicate, and `N=8` is already degenerate in the exact
  geometric coordinates `(start-card, span)`, so every geometric functional of
  the form `a(start-card)+b span` gives the same value there. Thus the
  canonicity of `(0.36,0.14)` does not come from the frontier bookkeeping at
  all: not from winner data, not from max-margin robustness, and not from the
  degenerate rows. If there is a genuine normalization left, it has to come
  from an earlier scalar law or from an exact identity outside the extracted
  packet frontier itself (E79.81).
- That remaining scalar-law hope is now closed too. The earlier branch
  E79.58-E79.66 really does reduce the zeta-side modal amplitude, but in a
  different coordinate family: `profile_slope`, active-edge intensity, and the
  scale-matched first-prefix defect. Its fitted coefficients move with the
  predictor gauge and do not numerically or structurally inherit the geometric
  two-mode point `(0.36,0.14)`. So the geometric point is not selected by the
  early scalar branch either. The honest possibilities left are: an exact
  identity outside the frontier bookkeeping, a sharper normalization still not
  named, or the conclusion that only the admissible cone is structural
  (E79.82).
- The first direct progress on the discriminant core is now written down too.
  The closure defect `c_N = 1 - sum x_j` is not a nice monotone convergence
  law, but it is a robust zeta-only smallness regime: on the audited
  `N=8..18`, `lambda=6`, `dps=60` ladder, zeta has `|c_N|` between about
  `3.9e-7` and `2.0e-10` and cloud coherence essentially `1`, while two
  distinct planted off-line controls have `|c_N| = O(1)` or larger and lose
  that coherence. So E79.5 should now be read as codimension-one near-closure,
  and the live burden sharpens to explaining structurally why small `|c_N|`
  travels with `M_N * x` single-signedness (E79.83).
- The first bridge candidate between those two fingerprints is now named too.
  In the exact secular package `sum_j r_j/(z-d_j)=c_N`, `r_j=q_jx_j`, the
  zeta ladder does not show one-signed residues; it shows something sharper:
  near-perfect balance of positive and negative residue mass. On
  `N=8,10,12`, the zeta ratios `|sum r|/sum|r|` are about
  `5.8e-12, 2.7e-14, 1.5e-16`, with positive/negative absolute masses in
  essentially exact balance, while two off-line planted controls fail that
  balance strongly. So the live discriminant front is no longer the loose pair
  `(small |c_N|, coherence)` but the sharper triple
  `(small |c_N|, residual balance, coherence)` (E79.84).
- That bridge now survives one more contact test too, but in a slightly more
  refined form than "plain symmetry". The zeta ladder shows a stable regime of
  one sharply separated farthest outlier together with a low-defect `+-`
  symmetric remaining cloud. The planted off-line controls can imitate one part
  of that picture on an isolated row, but not the conjunction across the
  audited ladder. So the live discriminant chain is sharper again:
  `(small |c_N|, residual balance, cloud symmetry regime, coherence)`.
  The next honest burden is no longer to guess another scalar signature, but
  to explain why this paired cloud geometry forces the odd/coherent cumulative
  profile `M_N` (E79.85).
- That geometric bridge now has a first quantitative compression too. If one
  defines
  `D_N = (mean pair defect of the outlier-removed cloud)/outlier_fraction`,
  then zeta sits on the tiny scale `D_N ~ 10^-3` exactly where the coherence
  defect collapses to numerical zero, while the planted controls stay an order
  of magnitude or more above that scale except for one resonant row. So the
  next honest burden is sharper again: explain why the zeta mechanism drives
  this normalized cloud-defect quotient to the tiny `10^-3` regime, and whether
  one more geometric correction is needed to account for the exceptional
  planted row (E79.86).
- That exceptional planted row is now understood well enough to stop it from
  polluting the target. It is not a hidden copy of the zeta mechanism. At the
  resonant row `plant gamma2, N=12`, one has huge `|c|`, completely one-signed
  residues (`R_net=1`, `R_pm=0`), and only weak outlier separation
  (`outlier_fraction ~ 1.16`), yet the outlier-removed cloud is internally very
  symmetric and the coherence defect becomes tiny. So the row is a genuine
  cloud-only resonance: cloud symmetry by itself can create isolated
  near-coherence, but it does not recover the zeta-side conjunction
  `(small |c_N|, residual balance, sharp outlier separation)`. The live
  discriminant object is therefore that conjunction, not `D_N` alone and not
  "cloud symmetry implies coherence" in full generality (E79.87).
- That correction is now operational too. A simple audited conjunction
  `CLOSE + BAL + GEOM`, meaning small `|c_N|`, near-perfect residual balance,
  and zeta-scale cloud geometry (`outlier_fraction > 5`, `D_N < 5e-3`), is
  passed by all audited zeta rows and by neither planted control. In
  particular, the cloud-only resonant row `plant gamma2, N=12` is excluded for
  exactly the right reason: it mimics inner cloud symmetry locally, but fails
  closure, fails balance, and never enters the sharp-outlier regime. So the
  next honest burden is now even sharper: derive the geometric regime from the
  closure-plus-balance side, not from `D_N` alone (E79.88).
- That next reduction now survives the longer audited ladder too. Extending the
  same predicates to `N=8..18`, every audited row with `CLOSE + BAL` also has
  the zeta-side geometry predicate `GEOM`, while neither planted control ever
  enters the premise regime. So, at least on the current finite ladder, the
  geometry is no longer independent data: the live burden sharpens once more to
  the candidate implication `CLOSE + BAL => GEOM`, i.e. derive the sharp-outlier
  / tiny-`D_N` cloud directly from closure plus residual balance, or name the
  first finite obstruction if that implication breaks beyond the audited range
  (E79.89).
- That implication now has a first mechanism-level split too. On the audited
  long ladder, `CLOSE` has no counterexample to a strong rank-one escape scale
  `|(q^T x)/c| / mesh_radius >> 1`, `BAL` has no counterexample to low
  internal pair defect, and every audited `GEOM` row is already covered by
  that split pair. The cloud-only planted resonance behaves exactly as this
  picture predicts: it can imitate the low-defect half, but not the strong
  escape half. So the live burden sharpens again from the compound implication
  `CLOSE + BAL => GEOM` to the more elementary pair
  `CLOSE => STRONG_ESCAPE` and `BAL => LOW_DEFECT` (E79.90).
- The first of those two elementary implications now has a direct audited
  explanation too. On the main audited ladder, the zeta-side strong escape is
  not driven by a huge numerator `q^T x`: in mesh units the numerator stays
  tiny, while `|c|` collapses to `1e-7..1e-10`, and that denominator collapse
  is what forces `|(q^T x)/c| / mesh_radius` into the `10^2` range. The planted
  main control shows the opposite profile: a much larger numerator scale but
  no small-`c` collapse, and consequently no strong escape. So the live front
  inside `CLOSE => STRONG_ESCAPE` is now reduced again from a two-sided ratio
  problem to the sharper denominator-driven question (E79.91).
- But that denominator-driven reading now needs one precise correction: a mere
  upper regularity statement on the numerator is too weak to force strong
  escape. Since `escape_ratio = (|q^T x|/mesh_radius)/|c|`, an upper bound on
  `|q^T x|/mesh_radius` says nothing by itself about largeness of the quotient,
  and the audited zeta ladder already shows that the numerator does shrink by
  several orders of magnitude. So the missing content is not "numerator tame"
  in the sense of an upper ceiling, but a relative non-collapse statement:
  the numerator shrinks much more slowly than `|c|` does (E79.94).
- That relative-noncollapse wording is itself now sharpened. A direct audit of
  the certified E79.91 rows shows that on the zeta ladder the numerator and
  `|c|` often collapse by comparable section-to-section factors; what stays
  organized is not a vague exponent gap, but the quotient
  `escape_ratio = (|q^T x|/mesh_radius)/|c|` itself. In zeta that quotient sits
  on a large stable plateau around `10^2`, while the planted main control stays
  order-one. So the live escape-side object is no longer "numerator shrinks
  slower than c" but the sharper plateau question: why does the quotient lock
  onto a large zeta-side scale at all (E79.95)?
- That plateau now has an exact finite name. Using only the already certified
  E79.90/E79.91 ladders, one gets the identity
  `escape_ratio = escape_scale / mesh_radius = (|q^T x|/|c|)/mesh_radius`
  row by row to roundoff. So the plateau is exactly the normalized rank-one
  escape scale already latent in the finite package, not an abstract quotient
  with no internal interpretation. Moreover, the E78.155 predictor
  `kappa_hat = |q^T x|/|c| + mean(d)` differs from this by only about
  `0.22%-0.26%` on zeta, but by `18%-39%` on the planted main control. This
  places zeta in a genuine rank-one escape regime and sharpens the live burden
  once more: explain why the normalized rank-one escape scale stabilizes at a
  large zeta-side constant instead of staying order-one (E79.96).
- That canonical escape object now couples directly back to the cloud geometry.
  A derived audit of the same certified long ladder shows that on zeta
  `escape_ratio * sqrt(D_N)` stays in a narrow band around `4.65`, with only
  about `7%` relative spread, i.e.
  `escape_ratio ~ const / sqrt(D_N)` all along the honest ladder. Both planted
  controls fail to enter that regime. So the escape and geometry halves are no
  longer two unrelated miracles: on the audited zeta side they are locked by a
  square-root scale law. This sharpens the live burden again from "explain a
  large escape plateau" to "explain the zeta-side coupling
  escape_ratio ~ const/sqrt(D_N)" or name the first structural obstruction
  (E79.97).
- That check now has its first honest negative answer too: the square-root law
  does **not** come from the balance side alone. On the planted main control,
  the residual balance improves steadily and `D_N` shrinks, yet the coupled
  quantity `escape_ratio * sqrt(D_N)` stays around `0.10-0.20`, still smaller
  than zeta by factors of roughly `20x-45x`. So `BAL` is too weak not only for
  `LOW_DEFECT` (E79.92), but also for the stronger E79.97 coupling law. The
  live arithmetic burden therefore remains on the closure / rank-one escape
  side, not on balance by itself (E79.98).
- The same coupled law has now been decomposed once more, and the internal
  pair-defect term is not the load-bearing piece either. Since
  `D_N = mean_pair_defect / outlier_fraction` exactly, E79.97 can be rewritten
  as `escape_ratio * sqrt(mean_pair_defect/outlier_fraction) ~ const_zeta`.
  But the planted main control eventually has `mean_pair_defect` even smaller
  than zeta while still staying far outside the zeta-side escape regime. So
  the discriminating content of E79.97 is not "tiny pair defect" by itself; it
  sits chiefly in the coupling between escape and outlier separation. This
  sharpens the live burden again to the smaller object
  `escape_ratio / sqrt(outlier_fraction)`, i.e. the escape-outlier coupling
  (E79.99).
- That smaller object now has its first direct spectral reading on certified
  data. On the shared audited ladder `N=8,10,12`, the zeta build already
  satisfies `outlier_abs / escape_scale = 1.0136, 1.0205, 1.0179`, so the
  rank-one escape scale agrees with the actual farthest spectral outlier of
  `K_N` to within about `2%`. Therefore, on that shared subladder,
  `escape_ratio / sqrt(outlier_fraction)` is already the same, up to the same
  tiny error, as
  `sqrt(outlier_abs * second_abs) / mesh_radius`: the geometric mean of the two
  largest spectral scales, normalized by the mesh. The planted controls do not
  share this rigidity. So the live object has now acquired a bona fide
  spectral interpretation, albeit currently only on the shared audited rows
  (E79.100).
- That scope caveat has now been partially removed. Extending the minimal cloud
  audit to `N=18` shows that on zeta
  `outlier_abs / escape_scale = 1.0136, 1.0205, 1.0179, 1.0246, 1.0224, 1.0296`,
  so the rank-one escape scale keeps tracking the actual farthest spectral
  outlier of `K_N` to within about `3%` on the whole audited zeta ladder. The
  planted controls still do not share that rigidity. So the spectral reading is
  no longer just a shared-subladder curiosity: on the audited zeta ladder, the
  live burden now sharpens to explaining the lock
  `escape_scale ~= outlier_abs` itself (E79.101).
- Once that lock is granted, the remaining spectral burden localizes again.
  Reading the same E79.101 audit one step further shows that
  `second_abs / mesh_radius` is already enough to separate the honest ladder
  from both planted controls by more than an order of magnitude:
  zeta lives at `~9.8..13.0`, while the planted builds stay near `~1`.
  So after factoring out the outlier lock, the genuinely new partner in the
  spectral reading is the second spectral scale itself. This sharpens the live
  burden again to explaining the zeta-side linear growth regime of
  `second_abs / mesh_radius` (E79.102).
- That reduction now has its own honest correction. Auditing the derived ratio
  `(second_abs / mesh_radius) / outlier_fraction` shows that it stays order-one
  on the audited ladder for zeta and for the planted controls alike. So the
  E79.102 second-scale signal is not behaving like a genuinely new primitive
  invariant: it is mostly repackaging the older outlier-fraction geometry.
  After the outlier lock `escape_scale ~= outlier_abs`, the genuinely new burden
  therefore sharpens again to explaining the large zeta-side regime of
  `outlier_fraction` itself (`~10..14` versus `~1` on the planted builds),
  rather than the second scale as an independent mystery (E79.103).
- That last sharpening was still one step too pessimistic. There is an exact
  identity
  `outlier_fraction = (outlier_abs / (mesh_radius * spectral_reading))^2`,
  so once `outlier_abs` and `spectral_reading` are fixed from the same certified
  cloud, `outlier_fraction` is already determined and is not an additional
  primitive invariant. Combining this with the zeta-side lock from E79.101 gives
  `outlier_fraction ~= (escape_ratio / spectral_reading)^2`, with exactly the
  lock error transported through the square: on zeta the reconstruction error is
  only about `4%-6%`, while the planted controls fail badly because the lock
  fails badly there too. So after E79.104 the honest surviving burden is not a
  new scalar `outlier_fraction` on top of the lock, but the lock package itself:
  the zeta-only rigidity `escape_scale ~= outlier_abs` inside the shared
  spectral-reading geometry.
- That lock package itself now has a finer internal reading. Removing the
  deterministic E78.155 shift `mean(d)` from the audited outlier leaves a
  residual which, on zeta, already aligns closely with the second spectral
  scale: the local coefficients
  `[outlier_abs - escape_scale - mean(d)] / second_abs` stay in the positive
  band `0.156..0.256`, and the affine law
  `outlier_abs ~= escape_scale + mean(d) + 0.23 second_abs`
  predicts the audited zeta outlier to within about `0.6%`. The planted
  controls do not share this regime: their corresponding coefficients are not
  rigid and may change sign, and the same zeta-fitted law misses them by about
  `20%-44%`. So after E79.105 the honest live burden sharpens again from the
  bare lock `escape_scale ~= outlier_abs` to a more structured two-scale
  question: why the residual after `escape_scale + mean(d)` is a coherent
  positive multiple of `second_abs` on zeta.
- The immediate inheritance check now says this coefficient is not secretly one
  of the old one-scale invariants in disguise. Auditing the obvious candidates
  `1/outlier_fraction`, `mesh_radius/second_abs`, `spectral_reading/escape_ratio`,
  and `1/sqrt(outlier_fraction)` shows zeta-side mean absolute errors around
  `0.09-0.18` against the E79.105 coefficient, so none of them is remotely
  canonical. The only near-match on zeta,
  `spectral_reading/escape_ratio - mesh_radius/second_abs`, is already a
  genuinely composite two-scale quantity and still fails badly on the planted
  controls. So after E79.106 the honest picture is that the E79.105 residual
  coefficient remains a genuinely two-scale coherence object, not a hidden
  one-scalar invariant.
- That said, E79.106 was not the end of the story. Auditing a small family of
  genuinely biescalar proxies shows that the zeta-side coefficient is not
  arbitrary either: the narrow best family is subtraction-shaped, led by
  `spectral_reading/escape_ratio - mesh_radius/second_abs` and two close
  normalizations of it, all with zeta-side mean absolute error around
  `0.011-0.013`, while weaker multiplicative or mean-shift variants miss by
  about `0.069`. The planted controls still do not share that regime. So after
  E79.107 the honest live burden sharpens once more: not merely "a biescalar
  coherence object", but specifically why the residual coefficient almost
  collapses onto a subtraction-shaped spectral-minus-mesh proxy on zeta.
- That proxy family is now cleaner than E79.107 first made it look. The two
  best forms,
  `spectral_reading/escape_ratio - mesh_radius/second_abs` and
  `1/sqrt(outlier_fraction) - mesh_radius/second_abs`,
  are not independent candidates at all: by the exact E79.104 lock identity
  they differ by precisely
  `[(outlier_abs/escape_scale)-1] / sqrt(outlier_fraction)`, i.e. by the same
  transported outlier-lock defect already tracked elsewhere. On the audited
  zeta ladder that gap is only about `1.4%-3.0%`, while the planted controls
  fail badly where the lock fails. So after E79.108 the residual-coherence
  object sharpens again to a single subtraction-shaped proxy, not a loose
  family:
  `1/sqrt(outlier_fraction) - mesh_radius/second_abs`
  (equivalently `spectral_reading/escape_ratio - mesh_radius/second_abs` once
  the lock language is preferred).
- The next scalar correction hope now failed honestly. Auditing the remaining
  proxy gap against the obvious candidates `outlier_over_escape - 1`,
  `mesh_radius/second_abs`, and `mean(d)/second_abs` shows no stable law even
  on zeta: the ratios keep substantial spread and change sign along the audited
  ladder, and the planted controls are even less organized. So after E79.109
  the subtraction-shaped proxy itself remains the sharp object, but its
  leftover error is not yet reducible to one more elementary scalar factor.
- Even so, that leftover error is already clearly secondary on the honest
  ladder. Normalizing by the full residual coefficient shows that on zeta the
  subtraction proxy
  `1/sqrt(outlier_fraction) - mesh_radius/second_abs`
  already captures about `94%-111%` of `alpha_N`, with mean relative gap only
  about `6.3%` and worst audited relative gap about `11.3%`. The planted
  controls do not share that regime at all. So after E79.110 the live burden is
  sharper again: explain why the zeta-side residual coefficient is almost
  entirely exhausted by the subtraction proxy, with only a genuinely secondary
  remainder.
- That secondary remainder is now more organized than a generic error term.
  On the audited zeta ladder the proxy gap stays tiny in absolute value
  (mean `~0.0127`, max `~0.0205`) and changes sign exactly once, with pattern
  `(-,-,-,+,+,+)`: the proxy first slightly overshoots and then slightly
  undershoots `alpha_N`. The planted controls can also show a single crossing,
  but only at much larger absolute scale (`~0.17` and `~0.40` mean absolute
  gap respectively). So after E79.111 the honest object sharpens again: the
  zeta-side residual coefficient is exhausted by the subtraction proxy up to a
  tiny single-crossing remainder, not just an unspecified small error.
- That remainder geometry is now a bit sharper still. On zeta the unique
  crossing occurs between `N=12` and `N=14`, with linear crossing location
  `N ~ 13.4`, i.e. near the middle of the audited honest ladder rather than at
  a boundary row. And in absolute scale the hierarchy is now explicit:
  `mean |gap| ~ 0.0127` versus `mean |proxy| ~ 0.2119` and
  `mean |alpha| ~ 0.2106`, so the remainder is smaller by roughly a factor of
  `~16x`. The planted controls cross earlier and at far larger gap scale. So
  after E79.112 the current best finite reading is:
  `alpha_N = (1/sqrt(outlier_fraction) - mesh_radius/second_abs) +`
  a tiny mid-ladder single-crossing remainder.
- The second half of the tentative split does **not** survive the same level of
  scrutiny. A direct audit of the E79.90 section data shows multiple planted
  rows with low internal pair defect but only weak balance, or no balance at
  all. So `BAL => LOW_DEFECT` is too strong and should not be pursued as a
  theorem target. The honest asymmetric picture is now: the escape half is
  genuinely constrained by closure, while low defect by itself is too permissive
  and carries no arithmetic content without the escape half attached
  (E79.92).
- That asymmetry can now be stated positively too. On the audited ladder,
  `STRONG_ESCAPE` already acts as a clean sufficient signature of the honest
  zeta-side route: every audited strong-escape row is zeta and already lies in
  `GEOM`, while the only converse failure on the coherence side is the planted
  cloud-only resonance `gamma2, 12->14` that was already understood in E79.87.
  So the escape mechanism should now be pursued as a sufficient forcing route,
  not as a biconditional classifier of every finite near-coherence event
  (E79.93).
```

**E79.4 -- Assembly (if E79.3 closes).**
`GAP-Z proved => SHARED-N2-LEMMA => convergence halves of points 2, 5, 6 closed`.
Write the exact statement and the three downstream consequences. Update the ledger
to mark those convergence halves PROVED (build-neutral).

---

## HOLE 2 -- the IDENT arithmetic DISCRIMINANT

**The point-6 content that is NOT convergence.** Fixed-L convergence is
build-neutral (both builds converge -- Outcome A). SAFE-GAMMA-IDENT additionally
requires the fixed-L limit to be the ARITHMETIC object `2 Xi'/Xi`, and the plant
must FAIL this. That failure is the RH-content. Phase-78 isolated three coupled
fingerprints of the separation (all build-discriminating, all admissible in IDENT
per E77.7az):

```text
- c = 1 - sum x_j = F_N(infinity) -> 0 for zeta (1e-7..1e-10), O(1) for plant.
- M_N * x single-signed (coherent spectral shift) for zeta; sign-mixed for plant
  (E78.154 -- this survived the retraction, it is solid).
- BOUND=TRUE tight (zeta) vs loose (plant) (E78.153).
```

### Milestones

**E79.5 -- c -> 0 as the operator signature of on-line alignment.**
`c = 1 - 1^T A_N^{-1} b_N`. Characterize `c_N -> 0` (equivalently `1^T A_N^{-1}
b_N -> 1`) as a codimension-one arithmetic condition, and prove it holds for zeta
and FAILS (c bounded away from the critical value) for the plant. Connect `c -> 0`
to the true zero on the line vs the plant's off-line zero. This is the cleanest
candidate for the discriminant's core. Probe: `c_N` trajectory to large N, both
builds, plus the analytic identity for `1^T A_N^{-1} b_N`.

**E79.6 -- single-signedness <=> on-line, and it is what IDENT needs.**
Prove: `M_N * x single-signed` (coherence of the spectral-shift cloud) is
equivalent to the fixed-L limit being the on-line arithmetic derivative, and the
plant's off-line zero forces sign-mixing. Tie coherence to `c -> 0` and to the
secular-equation residue signs. Target: `coherence <=> SAFE-GAMMA-IDENT`, plant
provably incoherent. This is the genuine NEW-mathematics milestone; it may need a
new invariant (a "coherence functional" of the residue cloud).

**E79.7 -- non-circularity + falsifiers for the discriminant.**
Random-symbol control (must be incoherent), a SECOND planted off-line zero at a
different height (must be incoherent), and the on-line zeta (coherent). Audit
against E72.16/E77.7az: the discriminant lives in IDENT where separation is
REQUIRED, but confirm no zero-LOCATION is smuggled into the forcing step -- only
on/off-line-ness through the arithmetic data.

---

## ASSEMBLY

**E79.8 -- the conditional IDENT theorem.**
State and prove: `GAP-Z (E79.4) + DISCRIMINANT (E79.6) => SAFE-GAMMA-IDENT =>
IDENT`. Combine with point 7 (already conditional-closed) and point 2 (existence
via projective convergence, uniqueness via source-selection) to record exactly
which sub-clauses of the master chain are then discharged, and which remain (LP
front, Front-C pairing).

**E79.9 -- if IDENT closes: the LP/Front-C status pass.**
Re-audit LP (points 1,3,4) and the pairing (points 8,9,10) against the new
spectral-shift machinery. In particular test whether the K_N / projective-source
apparatus also delivers the LP endpoint (SAFE-LIMIT-POINT) without the separate
BTG c_0 lower bound (E78.146) -- the projective-source route (E78.156) already
sidesteps c_0 for point 2 and may do so for LP.

---

## Non-circularity kill-tests (inherited, mandatory)

```text
- K1-K5 (E72.7): no ambient inverse-norm, no local inverse assembly, no absolute
  ceilings before cancellation, no point-local evaluators, no endpoint identity
  from scalar determinants.
- E72.16 / E77.7az: for the CONVERGENCE claims (GAP-Z, points 2/5/6 convergence),
  ANY order-one build separation is inadmissible -- these MUST be build-neutral.
  For the DISCRIMINANT (H2), separation is REQUIRED and admissible, but no zero
  LOCATION may enter the forcing step -- only on/off-line-ness via arithmetic data.
- MW-1..6: no positivity route, no per-prime/local-to-global assembly.
```

## Discipline

```text
- Both builds every run (zeta planted=None; plant planted=("14.134725141734693790",
  "0.30","5.0")). dps >= 60 (70-80 for exponent fits).
- Inner block A_N = H[1:-1,1:-1]; boundary column H[1:-1,-1]; NEVER the full H.
- Reuse verified machinery: build_mp (P76_002), right_transfer_data /
  two_generator_data (E77_3c), transfer/transfer_prime (P76_018/035),
  nu_atoms/w_sup (E78_153), the K_N builder (E78_152).
- Reproduce a published anchor before trusting any probe (e.g. E78.153
  zeta 8->10 BOUND = 0.0814831; E78.157 decomposition closes to 1e-37).
- Every milestone: numbered E79_x doc + companion .py probe + _results.json;
  ```text``` status block (proved/observed/refuted/open/next); Wall checklist;
  Class label (REDUCCION GENUINA / AUTOPSIA / PRUEBA COFINAL). No LaTeX.
- Distinguish PROVED from NUMERICALLY-OBSERVED at every step. A false closure is
  worse than an honest open problem.
- Phase-size ceiling ~100-150 docs; open phase-80 if exceeded.
```

## Exit criteria

```text
Phase 79 ends when EITHER
 (a) GAP-Z is proved (E79.4) AND the DISCRIMINANT is proved (E79.6) => SAFE-GAMMA-
     IDENT closes => IDENT closes; then the program stands on LP + Front-C only; OR
 (b) a theorem-grade obstruction is found for GAP-Z or the DISCRIMINANT (e.g.
     E79.1 shows ZERO non-summable, or the plant proves coherent), with an autopsy
     naming the next finite object; OR
 (c) the phase reaches ~E79.150 and hands a precise frontier to phase 80.
```

## First move

Run **E79.1** (nail the ZERO exponent to N=40+). It is decisive and cheap: it
tells you whether GAP-Z is TRUE (summable) before any proof effort, and whether
the whole finite-section convergence is safe or marginal. Everything downstream
depends on that number.
