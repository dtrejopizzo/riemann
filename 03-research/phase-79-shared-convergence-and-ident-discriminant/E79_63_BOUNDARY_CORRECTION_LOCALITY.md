# E79.63 - The residual correction is genuinely first-shell local, not a broad terminal average

**Scope:** `GAP-Z` only, locality audit for the one-coordinate correction beyond
the current shape-plus-intensity law.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the best
correction to `profile_slope + intensity` is genuinely concentrated at the first
terminal shell. Nearby shells, short terminal averages, and simple difference or
ratio statistics all perform materially worse under leave-one-out.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only shell observables already extracted in phase 79.
E72.16/E77.7az: respected. This is a local scalar-law audit, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this is the right next check

E79.62 showed that one extra coordinate can almost close the audited zeta
ladder, and that the most trustworthy current candidate is

```text
edge0 = first terminal shell.                                            (63-1)
```

But that still leaves an ambiguity:

```text
is edge0 really the object,
or is it just a proxy for a slightly broader terminal statistic?          (63-2)
```

This note resolves that by comparing `edge0` against its nearest competitors.

## 2. Probe

Companion files:

```text
E79_63_BOUNDARY_CORRECTION_LOCALITY_probe.py
E79_63_boundary_correction_locality_results.json
```

Starting from the baseline predictor

```text
|rho_N| ~ affine(profile_slope, intensity),                              (63-3)
```

the probe adds one extra local coordinate at a time:

```text
edge0, edge1, edge2,
(edge0+edge1)/2, (edge1+edge2)/2, (edge0+edge1+edge2)/3,
edge1-edge0, edge2-edge1,
edge1/edge0, edge2/edge1,
edge0+edge1.                                                             (63-4)
```

For each it records:

```text
- in-sample max relative error;
- leave-one-out max and mean relative error.                             (63-5)
```

## 3. Result

`edge0` wins the robustness audit.

Among the tested corrections, the best leave-one-out max relative errors are:

```text
edge0         -> 0.290
(edge0+edge1)/2 and edge0+edge1  -> 0.409
(edge0+edge1+edge2)/3            -> 0.421
edge2         -> 0.450
edge1         -> 0.475.                                                   (63-6)
```

The local differences and ratios are worse again, with the ratio `edge1/edge0`
especially unstable.

So the conclusion is not just "some boundary statistic helps." It is much
sharper:

```text
the correction is strongest at the very first shell,
and broadening it immediately hurts out-of-sample stability.             (63-7)
```

## 4. Reading

This is the right kind of locality result.

If `edge0` were merely standing in for a broad terminal average, then
`(edge0+edge1)/2`, `edge0+edge1`, or `(edge0+edge1+edge2)/3` would have matched
or improved its leave-one-out performance. They do not. The signal decays as
soon as the correction is smeared inward.

So the residual after the `profile_slope + intensity` law is best read as a
**boundary-point correction**, not as another diffuse profile moment.

## 5. Consequence

After E79.63, the scalar-law front is narrower again:

```text
|rho_N| ~ affine(profile_slope, intensity) + one first-shell correction.  (63-8)
```

The next candid task is therefore not to search wider neighborhoods, but to
identify the invariant meaning of that first-shell term:

```text
is edge0 itself canonical,
or does it reduce to a one-step boundary defect already present elsewhere in
the phase-79 shell algebra?                                               (63-9)
```

## 6. Status

```text
proved by probe:
  the one-coordinate correction is genuinely first-shell local; replacing
  edge0 by adjacent shells, short boundary averages, or simple differences /
  ratios worsens the leave-one-out audit;

reduced:
  the scalar-law correction from a vague "boundary statistic" to a concrete
  first-shell correction;

open:
  identify the invariant shell-algebra meaning of edge0;

next:
  compare edge0 against one-step boundary defects or normalized endpoint
  residuals already present in the phase-79 common-cloud bookkeeping.
```
