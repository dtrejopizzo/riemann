# E79.64 - The first-shell correction is better read as a relative boundary deficit than as a raw shell value

**Scope:** `GAP-Z` only, invariant reading of the one-shell correction isolated in
E79.63.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the best local
correction is not the raw first-shell value `edge0` itself, but its deficit
relative to the active-edge intensity scale. Equivalently, the strongest current
correction coordinate is `edge0 / intensity` (or `1 - edge0 / intensity`), which
outperforms raw `edge0` under leave-one-out.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only already-audited shell/profile observables.
E72.16/E77.7az: respected. This is a scalar-law refinement, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this check matters

E79.63 localized the residual correction to the first terminal shell:

```text
|rho_N| ~ affine(profile_slope, intensity) + one first-shell correction.   (64-1)
```

But the natural invariant question remained open:

```text
is the correction the raw shell value,
or the shell's deficit relative to the active-edge scale?                  (64-2)
```

This note resolves that first-pass ambiguity.

## 2. Probe

The comparison was run directly against the same baseline predictor

```text
affine(profile_slope, intensity),                                          (64-3)
```

adding one correction coordinate at a time. Besides raw `edge0`, the tested
defect forms were:

```text
def_avg    = intensity - edge0,
rel_avg    = (intensity - edge0) / intensity,
ratio0avg  = edge0 / intensity,                                            (64-4)
```

along with analogous peak and short-plateau deficits for control.

## 3. Result

The best leave-one-out performer is now the **relative** first-shell deficit:

```text
ratio0avg = edge0 / intensity
or equivalently
rel_avg   = 1 - edge0 / intensity.                                         (64-5)
```

Numerically:

```text
baseline slope + intensity         -> LOO max ~ 0.656
+ raw edge0                         -> LOO max ~ 0.290
+ ratio0avg (or rel_avg)           -> LOO max ~ 0.261.                     (64-6)
```

So the boundary correction becomes stronger, not weaker, when we divide out the
active-edge intensity scale.

Controls confirm that this is not a generic “normalize anything” effect:

```text
peak-relative defect     -> ~0.468
plateau-relative defect  -> much worse
raw broader averages     -> ~0.409 and above.                              (64-7)
```

So the signal is specific to the first shell relative to the **mean active-edge
intensity**, not just relative to any larger benchmark.

## 4. Reading

This gives the first invariant version of the correction:

```text
the first terminal shell is too small compared with the active-edge intensity,
and the size of that relative deficit carries the missing scalar information.  (64-8)
```

That is a cleaner statement than “edge0 helps,” because it is stable under the
obvious rescaling of the whole edge profile.

## 5. Consequence

After E79.64, the best current scalar law is:

```text
|rho_N| ~ affine(
    profile_slope,
    active-edge intensity,
    first-shell relative deficit
).                                                                         (64-9)
```

So the next candid target is no longer to hunt another raw shell coordinate,
but to understand whether that relative deficit already appears elsewhere as a
one-step endpoint defect in the common-cloud bookkeeping.

## 6. Status

```text
proved by probe:
  the best current one-shell correction is the first-shell deficit relative to
  the active-edge intensity scale, not the raw first-shell value itself;

reduced:
  the boundary correction from a raw local datum to a scale-free relative
  defect;

open:
  identify the shell-algebra meaning of that relative boundary defect;

next:
  compare `edge0 / intensity` and `1 - edge0 / intensity` to one-step endpoint
  defects or prefix deficits already present in the E79.3f/E79.3g bookkeeping.
```
