# E79.113 - The proxy structure survives ladder extension to N=26, but the zeta remainder does not converge

**Scope:** `DISCRIMINANT`, falsification test of E79.108-E79.112.
**Class:** REDUCCION GENUINA (with two negative sub-findings and one naming defect).

> **ERRATUM (E79.115).** Two corrections to this document.
>
> 1. The dps control in s.2 was run only at `N<=18`. It is NOT evidence that
>    `dps=70` is adequate at larger `N`, and s.2 should not be read as
>    settling the precision question for the ladder generally. E79.115 shows
>    `dps=70` fails from `N=28` onward. All rows of THIS document are
>    `N<=26` and lie inside the valid range (`N=26` verified STABLE at
>    `8.9e-13`), so **the numbers here stand**.
> 2. The s.4(b) claim that the zeta relative gap is "drifting upward, not
>    converging" does not survive continuation. At converged precision
>    (`dps>=110`) the sequence FALLS over `N=28,30,32,34`
>    (`0.1282, 0.1119, 0.0946, 0.0730`) before rising again at `N=36`.
>    The honest statement is that `|gap/alpha|` oscillates in roughly
>    `0.03-0.16` with no established trend. See E79.115 s.5.

## 1. Why this note was necessary

E79.108 through E79.112 are five consecutive documents with **no companion
probe**. Every one of them re-reads the same two frozen result files,

```text
E79_90_escape_balance_split_results.json,
E79_101_outlier_escape_agreement_results.json,                         (113-1)
```

whose ladder is six rows, `N = 8,10,12,14,16,18`.

On that fixed six-row dataset the claims grew progressively finer:

```text
E79.110: the proxy captures ~94% of alpha_N,
E79.111: the remainder is small and crosses sign exactly once,
E79.112: the crossing sits at N ~ 13.41, "near the middle".            (113-2)
```

A single sign change in a six-element sequence, interpolated to three
significant figures, is not by itself evidence of "a fairly rigid finite
geometry" (E79.112 s.4). It is equally what a smooth function with one zero
looks like at low resolution, and what noise looks like at low resolution.
The phase discipline requires a probe per milestone; that requirement had
lapsed for five documents in a row.

E79.113 therefore recomputes every ingredient **from scratch in one place** and
extends the ladder to `N = 26`, on all three builds.

## 2. Method

`E79_113_proxy_ladder_extension_probe.py` rebuilds `K_N` directly and computes

```text
alpha_N := [outlier_abs - escape_scale - mean_d] / second_abs,
proxy_N := 1/sqrt(outlier_fraction) - mesh_radius/second_abs,
gap_N   := alpha_N - proxy_N,                                          (113-3)
```

for `N = 8,10,...,26`, `lambda = 6`, `dps = 70`, on `zeta`,
`plant_gamma1_beta030`, `plant_gamma2_beta030`. It depends on no frozen file.

### Stability controls (run before interpreting anything)

The finite-section metrics were checked to be invariant to the two free
parameters of the harness:

```text
max_n=18 dps=60 -> zeta gaps = +0.01963,+0.01746,+0.00617,+0.03416,+0.03849,+0.03463
max_n=26 dps=60 -> identical
max_n=18 dps=70 -> identical                                           (113-4)
```

So sectioning from a larger parent does not perturb the smaller rows, and 60
vs 70 digits is not load-bearing. The ladder extension is legitimate.

### Anchor reproduction

With the E79.105 convention for `mean_d` (see s.5), the recomputed `N=8..18`
rows reproduce the published values exactly:

```text
E79.111 published: -0.0108, -0.0108, -0.0205, +0.0085, +0.0142, +0.0116
E79.113 recomputed: -0.010803, -0.010799, -0.020462, +0.008541,
                    +0.014243, +0.011645                               (113-5)
```

and both planted sign patterns reproduce as well
(`plant_gamma1 = (+,-,-,-,-,-)`, `plant_gamma2 = (+,+,-,-,-,-)`).

**So E79.108-E79.112 were arithmetically correct despite having no probe.**
That is worth stating plainly: the defect in those documents was procedural,
not numerical.

## 3. Result - what survives

### The zeta single crossing is real, not a six-row artifact

On the full ten-row ladder the zeta sign pattern is

```text
- - - + + + + + + +                                                    (113-6)
```

with exactly **one** sign change, interpolated at

```text
N_cross ~ 13.41,                                                       (113-7)
```

unchanged from E79.112. Four rows that E79.112 never saw (`N=20,22,24,26`) all
came in positive and did not re-cross. This is the main positive content of
E79.113: the claim was falsifiable, it was tested, and it held.

### The amplitude separation persists

```text
build                  mean|gap|  mean|gap/alpha| (8-18)  (20-26)
zeta                     0.01625        0.0631            0.0668
plant_gamma1_beta030     0.15667       31.4438            2.8040
plant_gamma2_beta030     0.31871        1.1036            1.6509      (113-8)
```

The zeta ladder stays at the `~6-7%` relative level on rows the earlier
documents never saw, while both plants stay one to two orders above it. The
discriminating power of the proxy does not decay with `N` over this range.

## 4. Result - what does NOT survive

### (a) The crossing count is not a discriminant at all

All three builds have **exactly one** sign change on the extended ladder:

```text
zeta         : ---+++++++    1 crossing at N ~ 13.41,
plant_gamma1 : +---------    1 crossing at N ~  9.59,
plant_gamma2 : ++--------    1 crossing at N ~ 11.62.                  (113-9)
```

E79.111 half-conceded this (`111-10`); E79.113 settles it. Crossing count
carries **zero** discriminant content. Only amplitude separates the builds.
E79.112's framing "mid-ladder crossing + genuinely secondary amplitude"
(`112-12`) should be read as one real criterion and one decorative one.

### (b) The zeta remainder is drifting upward, not converging

This is the genuinely new negative finding. The zeta relative gap by row:

```text
N     :   8      10     12     14     16     18     20     22     24     26
|g/a| : 0.0694 0.0555 0.1130 0.0371 0.0579 0.0455 0.0303 0.0717 0.0787 0.0867
                                                                      (113-10)
```

From `N=20` onward the sequence is **monotone increasing**:

```text
0.0303 -> 0.0717 -> 0.0787 -> 0.0867.                                 (113-11)
```

The ladder-mean is stable (`0.0631` short, `0.0646` full) only because early
rows cancel against late ones. The tail is not settling toward zero; it is
climbing back toward the `N=12` level and past it.

So the hope implicit in E79.110-E79.112 -- that the subtraction proxy is an
asymptotically exact description of `alpha_N` whose remainder shrinks -- is
**not supported**. On the audited range the proxy is a good *finite-window*
approximation that is slowly degrading, not a limit.

This does not damage the DISCRIMINANT use of the proxy, which needs only
separation at finite `N`, and separation is intact (`113-8`). It does damage
any attempt to promote the proxy into an identity.

## 5. Naming defect found in the alpha definition

Every document from E79.105 onward writes the residual coefficient as

```text
alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs.       (113-12)
```

The notation `mean(d)` is wrong. The inner index set is symmetric, so the
arithmetic mean of the `d` vector is **identically zero**:

```text
sum_j d_j / len(d) = 0 for every audited row.                         (113-13)
```

The quantity actually used by `E79_105_two_scale_outlier_law_probe.py`, and
inherited silently by E79.106-E79.112, is

```text
mean_d = pi*(N-1)/lambda,                                             (113-14)
```

which is a mesh-spacing scale, not a mean of `d`. Taking the definition at
face value produces a completely different (and all-positive, non-crossing)
gap sequence -- which is how this was caught.

```text
Recommendation: rename the quantity to mesh_scale_N := pi*(N-1)/lambda
in all downstream work. The numbers in E79.105-E79.112 are unaffected;
only the name is wrong.                                               (113-15)
```

## 6. Status

```text
proved     : nothing new (this is a numerical audit).
observed   : zeta single crossing at N ~ 13.41 SURVIVES extension to N=26;
             amplitude separation zeta vs plants persists to N=26;
             zeta relative gap DRIFTS UP monotonically over N=20..26.
refuted    : crossing count as a discriminant (all three builds cross once);
             the implicit claim that the proxy remainder is converging.
open       : why the zeta amplitude regime is entered at all (unchanged
             live burden from E79.110/113-13);
             whether the N>=20 upward drift continues or turns over.
next       : extend to N=32-36 to decide the drift question before any
             further refinement of the proxy. If the drift continues, the
             residual-coherence branch is a finite-window phenomenon and
             should be labelled as such rather than refined further.
```

## 7. Wall checklist

```text
K1-K5      : OK. No ambient inverse-norm, no local inverse assembly, no
             absolute ceiling before cancellation, no point-local evaluator,
             no endpoint identity from scalar determinants.
E72.16     : N/A. This is the DISCRIMINANT branch, where build separation is
             REQUIRED and admissible; no convergence claim is made here.
zero loc.  : OK. No zero LOCATION enters. Only spectral data of K_N
             (outlier_abs, second_abs, escape_scale, mesh_radius) and the
             mesh scale pi*(N-1)/lambda.
MW-1..6    : OK. No positivity route, no per-prime or local-to-global
             assembly.
probe      : PRESENT (E79_113_proxy_ladder_extension_probe.py +
             _results.json), restoring the per-milestone discipline that
             lapsed across E79.108-E79.112.
```

## 8. Consequence

After E79.113 the residual-coherence branch stands as:

```text
On the audited window N=8..26 the zeta residual coefficient is described by
  alpha_N ~= 1/sqrt(outlier_fraction) - mesh_radius/second_abs
to ~6-7% relative, with a single sign crossing at N ~ 13.41, while both
planted controls miss that amplitude regime by one to two orders.

The description is a finite-window fit, NOT a convergent one: its relative
error rises monotonically over the last four rows.                    (113-16)
```

The honest next object is the drift question in `113-11`, not another
refinement of the proxy formula.
