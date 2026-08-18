# E79.3j - The normalized edge profile is not a simple decaying law

**Scope:** `GAP-Z` only, normalized-depth anatomy of the active edge.  
**Class:** AUTOPSIA UTIL + REDUCCION FRANCA.  
**What we know after this document that we did not know before:** when edge
depth is normalized by the active width `m_theta(N)`, the zeta-side profile is
not a simple monotone decay from the boundary inward. Instead it develops a
broad high plateau in the middle of the active edge, with substantial decay only
near the deepest part.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. Convergence-side anatomy only.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

After E79.3i the candid next question was:

```text
even if the effective width stays linear, does the active edge have a stronger
intrinsic shape when depth is measured relatively, as u = r / m_theta(N)?  (T-1)
```

If the normalized profile decayed sharply as `u -> 1`, that could still hide a
meaningful gain beyond the crude width count.

## 2. Probe

Companion files:

```text
E79_3J_NORMALIZED_EDGE_PROFILE_PROBE.py
E79_3J_normalized_edge_profile_results.json
```

For each active edge of thickness `m_theta(N)`, the probe indexes shells by

```text
u = r / m_theta(N),   0 <= u <= 1,                                       (T-2)
```

and records the `N^2`-scaled shell amplitude normalized by the peak shell inside
the same edge. The data are then binned in `u`-windows `0.0, 0.1, ..., 0.9`.

So the object under inspection is the mean normalized profile

```text
Profile_theta(u) = mean over N of [ N^2 |EDGE_{N,r}| / peak_N ].         (T-3)
```

## 3. Result: zeta shows a broad interior plateau, not a boundary-decay law

At `sigma = 1`, for the `theta = 0.9` edge, the aggregate zeta profile is:

```text
u = 0.0   0.4257
u = 0.1   0.6734
u = 0.2   0.7587
u = 0.3   0.8995
u = 0.4   0.9347
u = 0.5   0.9512
u = 0.6   0.8745
u = 0.7   0.8483
u = 0.8   0.6683
u = 0.9   0.5585
```

For the tighter `theta = 0.99` edge, the same picture sharpens:

```text
u = 0.0   0.4332
u = 0.1   0.6862
u = 0.2   0.8487
u = 0.3   0.9365
u = 0.4   0.9372
u = 0.5   0.8672
u = 0.6   0.7414
u = 0.7   0.5064
u = 0.8   0.3040
u = 0.9   0.1436
```

This is the key structural fact:

```text
the normalized zeta-side edge profile is not a simple monotone decay from the
boundary. It rises from the outermost shell into a broad high plateau, and only
then decays near the deepest part of the active edge.                    (T-4)
```

So the edge is not "front-loaded" in the naive sense. A substantial part of the
middle of the active edge still carries near-peak shell weight.

## 4. Reading

This is the candid autopsy of the normalized-depth idea:

```text
normalizing depth by m_theta does reveal structure,
but not the kind of structure that immediately yields a strong gain.      (T-5)
```

What it gives is a **hump/plateau profile**, not a sharp one-sided decay law.
That matters because it rules out another tempting shortcut:

```text
the missing summability gain is not simply coming from the deep part of the
edge becoming negligible in normalized depth coordinates.                (T-6)
```

There is real decay, but it only becomes pronounced late in the edge, especially
for the `0.99` layer.

## 5. Plant remains non-structural

The planted build again fails to produce a coherent comparison profile. Its
aggregate normalized bins are highly irregular, with weight concentrated in a
few isolated regions depending on where `m_theta` collapsed.

So the normalized-profile story reinforces the same qualitative split:

```text
zeta has a coherent edge shape;
plant does not carry a comparable normalized geometry.                   (T-7)
```

## 6. Consequence

The live object sharpens again, but in a slightly sobering way:

```text
COMMON-GAP-Z
  = [linear effective edge width]
    x [local N^-2 shell profile with a broad interior plateau]
    + [tiny interior correction].                                        (T-8)
```

This is more precise than E79.3i. It says not only that the width stays
effectively linear, but also that the normalized shell profile does not collapse
fast enough across most of the edge to change the exponent on its own.

So the candid remaining places to search narrow further:

```text
1. cancellations across neighboring shells,
2. oscillatory structure not visible in absolute-value profiles,
3. coupling of the plateau region with the tiny interior correction.     (T-9)
```

## 7. Status

```text
proved by probe:
  the normalized zeta-side edge profile has a broad plateau and is not a
  simple boundary-to-interior decay law;

observed:
  strong decay appears only near the deepest part of the active edge,
  especially for the tighter 99% layer;

reduced:
  the missing summability gain cannot be attributed to a naive monotone
  normalized-depth profile either;

open:
  identify a stronger mechanism than width discount or normalized-profile
  decay, most likely involving cancellations or sign structure between shells;

next:
  inspect signed or block-cancelled shell aggregates rather than absolute-value
  shell profiles.
```
