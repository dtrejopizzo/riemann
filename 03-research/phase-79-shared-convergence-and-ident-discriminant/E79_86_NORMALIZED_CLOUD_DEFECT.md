# E79.86 - A normalized cloud-defect quotient is the first quantitative predictor of coherence defect

**Scope:** `DISCRIMINANT`, first quantitative compression of the bridge from
E79.85 to the sign structure of `M_N`.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** combining the
two geometric ingredients of E79.85 into one normalized quotient,

```text
D_N := (mean pair defect of the outlier-removed cloud) / outlier_fraction, (86-1)
```

produces the first simple quantitative proxy that tracks the coherence defect

```text
delta_coh := 1 - coh_N = 1 - Pxpos/total.                               (86-2)
```

On the audited rows, zeta sits in a tiny `D_N ~ 10^-3` regime, while the
planted controls are an order of magnitude or more larger except where the
coherence defect itself nearly vanishes.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / IDENT side only.
MW-3:  respected. No per-prime/local-to-global assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform gap hypothesis.
K1-K5: respected. Pure compression of already-audited finite quantities.
E72.16/E77.7az: respected. IDENT-side discriminant reduction only.
Circularity: respected. Uses only E79.83 and E79.85 outputs.
```

## 1. Why this is the right next compression

E79.85 left the live bridge in a two-part geometric form:

```text
one sharply separated outlier
+ low-defect approximately symmetric remaining cloud.                    (86-3)
```

The next candid question is whether those two ingredients can be compressed
into a single finite quantity that already predicts the defect of coherence in
`M_N`.

The cheapest such quantity is the ratio

```text
D_N = mean_pair_defect / outlier_fraction,                              (86-4)
```

which is small exactly when:

```text
- the internal cloud is symmetric, and
- the farthest outlier is well separated.                               (86-5)
```

## 2. Data used

No new heavy build is needed here. The note combines:

```text
- coherence_fraction from E79.83,
- outlier_fraction and mean_pair_defect from E79.85.                    (86-6)
```

On the shared audited rows `N=8,10` for all three builds, and `N=12` as an
auxiliary check, one gets:

```text
zeta:
  N= 8: D_N ~ 1.28e-3,  delta_coh ~ 1.1e-16,
  N=10: D_N ~ 1.60e-3,  delta_coh = 0,                                 (86-7)

plant gamma1:
  N= 8: D_N ~ 1.07e-1,  delta_coh ~ 2.60e-1,
  N=10: D_N ~ 1.44e-2,  delta_coh ~ 4.41e-1,                           (86-8)

plant gamma2:
  N= 8: D_N ~ 3.86e-2,  delta_coh ~ 9.45e-1,
  N=10: D_N ~ 1.96e-1,  delta_coh ~ 3.12e-1.                           (86-9)
```

The auxiliary `N=12` rows are also informative:

```text
zeta:          D_N ~ 1.19e-3,  delta_coh ~ 1.4e-15,
plant gamma1:  D_N ~ 1.02e-2,  delta_coh ~ 4.22e-1,
plant gamma2:  D_N ~ 1.36e-2,  delta_coh ~ 2.28e-4.                    (86-10)
```

## 3. Reading

This is not yet a theorem, but it is the first quantitative compression that
behaves the right way.

### Strong one-sided signal

On the audited rows,

```text
D_N ~ 10^-3  =>  coherence defect is essentially zero.                  (86-11)
```

That is exactly the zeta regime, and no planted row reaches it.

### Candid caveat

The converse is not yet forced in this small audit. In particular, the planted
row

```text
gamma2, N=12                                                            (86-12)
```

has a very small coherence defect while still sitting at

```text
D_N ~ 1.36e-2,                                                          (86-13)
```

well above the zeta scale.

So the candid interpretation is:

```text
very small D_N is a strong sufficient signal for coherence on the audited
ladder, but not yet an if-and-only-if criterion.                        (86-14)
```

That is already useful, because it tells us what quantitative regime zeta
occupies and the planted controls do not.

## 4. Consequence

After E79.86, the bridge from E79.85 to the sign structure of `M_N` can be
phrased more sharply:

```text
if the cloud-symmetry regime is strong enough to push
  D_N = mean_pair_defect / outlier_fraction
down to the 10^-3 scale,
then the coherence defect collapses to numerical zero on the audited ladder. (86-15)
```

So the live burden is no longer to connect two vague geometric features to
coherence. It is to explain why the zeta-side mechanism drives this normalized
cloud-defect quotient to the tiny scale `10^-3`, whereas the off-line planted
controls do not.

## 5. Status

```text
proved by finite audit:
  the normalized cloud-defect quotient D_N is the first simple quantitative
  predictor of coherence defect extracted from the E79.83-E79.85 chain;

clarified:
  tiny D_N (~10^-3) is a strong one-sided signature of coherence on the
  audited ladder;

caveat:
  the present data do not support an iff statement; one planted row shows
  small coherence defect without entering the zeta-scale D_N regime;

reduced:
  the next discriminant question to explaining the tiny-scale zeta regime of
  D_N rather than the full raw cloud geometry;

next:
  test whether D_N can be derived directly from residual balance, or whether
  one more geometric correction is needed to explain the exceptional planted
  row.
```
