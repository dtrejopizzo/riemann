# E79.62 - A third coordinate can nearly close the zeta ladder, but robustness distinguishes centroid from the first shell

**Scope:** `GAP-Z` only, audit of the first one-coordinate correction beyond the
current best predictor `profile_slope + intensity`.  
**Class:** REDUCCION GENUINA + robustness audit.  
**What we know after this document that we did not know before:** one extra
low-order coordinate can nearly close the audited zeta ladder, but not all such
coordinates are equally trustworthy. `centroid` gives the cleanest in-sample
closure, while the first-shell coordinate `edge0` behaves more robustly under
leave-one-out.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only already-audited profile and shell observables.
E72.16/E77.7az: respected. This is a finite scalar-law audit, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this audit is needed

E79.61 left the scalar front in a very narrow place:

```text
best current law:
  |rho_N| ~ affine(profile_slope, intensity),
with max relative error about 6% on the audited zeta ladder.             (62-1)
```

So the honest next question is no longer whether the law is low-dimensional,
but which **single** correction coordinate is the right one.

Two natural candidates are:

```text
- centroid: a global profile-shape correction;
- edge0:    the first terminal shell, i.e. the most local intensity datum. (62-2)
```

## 2. Probe

Companion files:

```text
E79_62_THIRD_COORDINATE_AUDIT_probe.py
E79_62_third_coordinate_audit_results.json
```

The probe compares three models:

```text
1. slope + intensity                           [E79.61 baseline]
2. slope + intensity + centroid
3. slope + intensity + edge0.                                                 (62-3)
```

For each one it records:

```text
- in-sample max relative error on the audited zeta ladder;
- leave-one-out max and mean relative error.                                  (62-4)
```

## 3. Result

The in-sample picture is striking:

```text
slope + intensity                 -> 5.86%
slope + intensity + centroid      -> 1.24%
slope + intensity + edge0         -> 1.06%.                                  (62-5)
```

So one extra coordinate really can almost close the current audited ladder.

But the leave-one-out audit separates the two candidates sharply.

For `centroid`:

```text
LOO max relative error  ~ 55.0%
LOO mean relative error ~ 15.1%.                                             (62-6)
```

For `edge0`:

```text
LOO max relative error  ~ 29.0%
LOO mean relative error ~  9.2%.                                             (62-7)
```

So `centroid` wins on raw interpolation, but `edge0` generalizes much better on
the tiny available ladder.

## 4. Reading

This is exactly the distinction we needed.

The zeta-side scalar law is now clearly **one correction coordinate away** from
closing the audited ladder. But the first candidate that closes it best
(`centroid`) also behaves more like a flexible interpolator. The first-shell
coordinate closes slightly less well in sample, but is materially more stable
under leave-one-out.

So the honest interpretation is:

```text
the residual after E79.61 is localizable,
and its most trustworthy current carrier is the first terminal shell,
not the broad centroid alone.                                              (62-8)
```

## 5. Consequence

After E79.62, the next admissible target is not "try arbitrary third
coordinates." It is narrower:

```text
understand why edge0 corrects the slope+intensity law,
and whether that correction can be rewritten as a more invariant
one-shell/one-step boundary statistic.                                     (62-9)
```

This keeps the scalar law close to the shell algebra that phase 79 has already
been using, instead of drifting into soft geometric interpolation.

## 6. Status

```text
proved by probe:
  one extra low-order coordinate can reduce the current zeta-side predictor
  error from about 6% to about 1% on the audited ladder;

observed:
  centroid gives the sharpest in-sample closure, but edge0 is substantially
  more robust under leave-one-out;

reduced:
  the remaining scalar-law burden to understanding a one-shell correction to
  the current shape-plus-intensity law;

open:
  identify the invariant form of that edge0 correction, if it is real;

next:
  compare edge0 against neighboring shell data and short one-step boundary
  statistics to see whether the correction is genuinely local or merely a proxy
  for one broader moment.
```
