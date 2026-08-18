# E79.60 - A tiny profile-moment predictor for the modal-ray amplitude exists on the zeta ladder, but it is still approximate

**Scope:** `GAP-Z` only, first explicit predictor law for the scalar modal-ray
amplitude `rho_N`.  
**Class:** REDUCCION GENUINA + candid limit of the current ladder.  
**What we know after this document that we did not know before:** a one-moment
profile law already predicts `|rho_N|` moderately well on the audited zeta
ladder, and adding a second moment improves it slightly. But the law is still
approximate, not rigid, and it does not extend as a cross-build predictor.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the already-audited modal amplitude and profile moments.
E72.16/E77.7az: respected. This is a non-forcing scalar-law audit.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why build the predictor now

E79.59 reduced the candidate family for `|rho_N|` to a tiny set of profile
moments:

```text
front_back_gap,
profile_slope,
profile_centroid.                                                        (60-1)
```

The next candid question is no longer "which family?" but:

```text
does one of these already give an explicit scalar law,
or do we really need at least two moments?                               (60-2)
```

## 2. Probe

Companion files:

```text
E79_60_PROFILE_MOMENT_PREDICTOR_probe.py
E79_60_profile_moment_predictor_results.json
```

The probe fits three zeta-side affine predictors for `|rho_N|`:

```text
1. gap_only:       |rho_N| ~ a + b * front_back_gap
2. slope_only:     |rho_N| ~ a + b * profile_slope
3. gap_plus_slope: |rho_N| ~ a + b1 * front_back_gap + b2 * profile_slope. (60-3)
```

It records in-sample max relative error / RMS error on the audited zeta ladder,
and also evaluates the resulting zeta fit on the planted build as a diagnostic.

## 3. Result

The one-moment fits already do something real:

```text
gap_only     max relative error ~ 13.8%
slope_only   max relative error ~ 14.8%.                                 (60-4)
```

So one scalar moment is already capturing a nontrivial share of the amplitude
law.

Adding the second moment helps, but only a little:

```text
gap_plus_slope   max relative error ~ 9.6%.                              (60-5)
```

That is a genuine improvement, but not a collapse to roundoff or to the
sub-percent regime seen earlier for the modal ray direction itself.

So the present picture is:

```text
the modal amplitude is short-law-like,
but not yet rigidly one- or two-moment closed.                           (60-6)
```

The planted diagnostic is also informative. When the zeta-side predictor is
evaluated on the planted build, it outputs small O(10^-2) amplitudes on most
rows while the true plant amplitudes remain wildly larger on the hard sections.
So this moment law is clearly not a build-universal identity.

That is the right kind of failure: on the convergence side we are isolating a
zeta-side scalar regularity, not forcing a cross-build theorem that would
violate the attribution gate.

## 4. Reading

This is the first explicit scalar law for the post-E79.55 front.

It is not the final law, but it is a real reduction:

```text
from "some hidden scalar attached to the edge"
to "roughly a two-moment affine functional of the normalized edge profile." (60-7)
```

The small improvement from one to two moments also matters: it suggests the
front/back imbalance and the internal tilt are complementary, not redundant.

## 5. Consequence

After E79.60, the candid next target is narrower again:

```text
either add one final low-order profile coordinate,
or normalize the existing moments by the active-edge intensity so that the
two-moment law becomes sharper.                                          (60-8)
```

The current evidence does **not** justify claiming that `rho_N` is already fully
closed by a single moment, but it does justify treating the scalar-law search
as a very low-dimensional problem.

## 6. Status

```text
proved by probe:
  explicit one-moment and two-moment affine predictors for |rho_N| exist on
  the audited zeta ladder, with the best current law using
  front_back_gap + profile_slope;

observed:
  the two-moment fit improves over each one-moment fit, but only modestly;

reduced:
  the scalar-law search for rho_N to a tiny low-dimensional moment fit problem;

open:
  determine whether one further normalization or one further low-order moment
  closes the remaining ~10% predictor error;

next:
  test intensity-normalized versions of the same profile moments, and audit
  whether the remaining error is concentrated on one hard row or spread across
  the ladder.
```
