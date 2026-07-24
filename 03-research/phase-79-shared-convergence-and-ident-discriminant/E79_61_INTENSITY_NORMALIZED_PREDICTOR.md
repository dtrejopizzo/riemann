# E79.61 - Intensity normalization sharpens the modal-amplitude predictor, and the planted diagnostic must be read with its own profile

**Scope:** `GAP-Z` only, corrected cross-build diagnostic plus the first
intensity-normalized refinement of the profile-moment predictor.  
**Class:** REDUCCION GENUINA + correction.  
**What we know after this document that we did not know before:** the planted
diagnostic for E79.60 must be evaluated on the planted profile itself, not on
zeta-side moments. Once corrected, the cross-build failure remains real. More
importantly, adding active-edge intensity as a coordinate sharpens the zeta-side
predictor substantially, down to about `6%` max relative error.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only already-audited edge/profile observables.
E72.16/E77.7az: respected. This is a non-forcing diagnostic refinement.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this note is needed

E79.60 did two useful things:

```text
1. it showed that a two-moment zeta-side predictor exists;
2. it suggested that the remaining burden might be a missing intensity
   normalization.                                                         (61-1)
```

But there was also one bookkeeping correction to make explicit:

```text
the planted diagnostic has to be evaluated using the planted profile moments,
not the zeta-side ones.                                                   (61-2)
```

So this note does both jobs together.

## 2. Probe

Companion files:

```text
E79_61_INTENSITY_NORMALIZED_PREDICTOR_probe.py
E79_61_intensity_normalized_predictor_results.json
```

For each build the probe recomputes the sigma=`1.0`, `90%` active-edge moments
from its own normalized profile:

```text
gap,
slope,
intensity = avg_N2_shell_90,
gap / intensity,
slope / intensity.                                                       (61-3)
```

It then fits zeta-side affine predictors and evaluates them on both builds:

```text
- gap + slope                          [baseline from E79.60]
- gap + intensity
- slope + intensity
- gap/intensity + slope/intensity.                                        (61-4)
```

## 3. Result

The correction does not change the qualitative cross-build story:

```text
the zeta-trained laws still fail dramatically on the planted build when read on
the planted profile itself.                                               (61-5)
```

So the earlier conclusion survives, now on the right evidence.

The refinement is the real gain. Compared to the E79.60 baseline

```text
gap + slope   -> max relative error ~ 9.6%,                              (61-6)
```

the intensity-augmented predictors improve clearly:

```text
gap + intensity      -> ~ 6.37%
slope + intensity    -> ~ 5.86%
gap + slope + intensity -> ~ 6.08%.                                      (61-7)
```

So the best current law is not the pure shape pair from E79.60, but

```text
|rho_N| ~ affine( profile_slope, active-edge intensity ).                (61-8)
```

Interestingly, the intensity-normalized ratios

```text
gap/intensity, slope/intensity                                            (61-9)
```

do **not** help by themselves: that fit stays near the old `~9.6%` level. So
the winning structure is additive coupling of shape and intensity, not simply
dividing one by the other.

## 4. Reading

This sharpens the scalar-law search one more notch.

The current best picture is:

```text
the modal amplitude is governed by
  one shape coordinate (best: slope)
  + one intensity coordinate,
not by shape alone and not by a naive ratio law.                         (61-10)
```

That is a more informative statement than "two moments help." It tells us what
kind of two moments matter.

## 5. Consequence

After E79.61, the live target gets narrower again:

```text
either sharpen the affine (slope, intensity) law slightly,
or explain the remaining ~6% by one last low-order correction concentrated on
the hard zeta rows.                                                       (61-11)
```

The next admissible refinement is therefore not a new family of descriptors,
but a local correction to the current best pair.

## 6. Status

```text
proved by probe:
  the planted diagnostic for the profile-moment law must be read on the
  planted profile itself, and under that correction the zeta-trained laws still
  fail strongly on the planted build;

proved by probe:
  adding active-edge intensity to the predictor sharpens the zeta-side fit
  from about 10% max relative error to about 6%;

reduced:
  the scalar-law search for rho_N to a shape-plus-intensity affine law, with
  profile_slope + intensity the best current two-coordinate predictor;

open:
  explain the remaining ~6% zeta-side error;

next:
  localize the residual of the `(profile_slope, intensity)` predictor row by
  row and test whether a single extra correction coordinate removes the last
  hard row.
```
