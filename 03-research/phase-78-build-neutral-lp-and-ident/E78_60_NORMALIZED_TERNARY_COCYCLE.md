# E78.60 - The denominator core is a normalized ternary cocycle, and the ternarity survives normalization

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.59 proved the exact bridge

```text
w_N = -Delta theta_N / (1-theta_N).                       (NTC-1)
```

Phase 77 had already proved that

```text
Delta theta_N = A_N + B_N + C_N,                         (NTC-2)
```

with genuinely ternary cancellation (E77.5i). The natural question is whether
dividing by `1-theta_N` simplifies that obstruction.

## 2. Exact normalized cocycle

Substituting E77.5i into E78.59 gives the exact identity

```text
w_N
 = -(A_N + B_N + C_N)/(1-theta_N)
 = A^*_N + B^*_N + C^*_N,                                (NTC-3)
```

where

```text
A^*_N := -A_N/(1-theta_N),
B^*_N := -B_N/(1-theta_N),
C^*_N := -C_N/(1-theta_N).                               (NTC-4)
```

So the denominator core is exactly a **normalized ternary cocycle**. There is
no denominator-only residue left over.

## 3. Audit on the common certified ladder

The overlap between the certified Phase-77 cocycle data and the Phase-78
`w_N` data is the short safe ladder

```text
sigma in {1.0, 3.0},   N in {8,10,12,14,16,18,20}.       (NTC-5)
```

On that common ladder, the normalization `(NTC-4)` was audited directly from

```text
E77_5i_schur_cocycle_cell_results.json
E77_5ac_theta_logderiv_coupling_{zeta,plant}.json.       (NTC-6)
```

### Exactness

The identity `(NTC-3)` holds to roundoff on the common ladder.

### Zeta

Representative normalized part-to-total ratios:

```text
N= 8, sigma=1.0:  max(|A^*|,|B^*|,|C^*|)/|w_N| = 9.289e2
N=10, sigma=3.0:  max(|A^*|,|B^*|,|C^*|)/|w_N| = 1.630e5
N=12, sigma=1.0:  max(|A^*|,|B^*|,|C^*|)/|w_N| = 3.409e3
N=20, sigma=3.0:  max(|A^*|,|B^*|,|C^*|)/|w_N| = 1.461e4. (NTC-7)
```

Across the common audited zeta ladder:

```text
median max normalized part / |w_N| = 5.992e3
max                                 = 1.630e5.           (NTC-8)
```

Even the best normalized pair remains huge:

```text
min normalized pair / |w_N| = 4.911e1
median                       = 3.385e3
max                          = 1.630e5.                  (NTC-9)
```

So on zeta the normalization by `1-theta_N` does **not** dissolve the ternary
obstruction. The three-term cancellation remains enormous relative to the final
normalized update `w_N`.

### Planted build

Representative normalized part-to-total ratios:

```text
N= 8, sigma=1.0:  max normalized part / |w_N| = 1.272
N=10, sigma=3.0:  max normalized part / |w_N| = 13.108
N=12, sigma=1.0:  max normalized part / |w_N| = 2.872
N=20, sigma=3.0:  max normalized part / |w_N| = 0.894.   (NTC-10)
```

Across the common planted ladder:

```text
median max normalized part / |w_N| = 8.939e-1
max                                 = 1.311e1.           (NTC-11)
```

So the plant again lacks the zeta-style giant ternary cancellation profile.

## 4. Consequence

This yields the candid live object after E78.59:

```text
NORMALIZED-TERNARY-CANCEL:
  prove a signed shell law for
  -(A_N + B_N + C_N)/(1-theta_N),                        (NTC-12)
```

and do so **without** splitting into absolute term bounds or pairwise
cancellation. The Phase-77 obstruction survives normalization intact.

This is a genuine reduction in the sense of admissibility:

```text
denominator fixed point
=> normalized ternary cocycle target.                    (NTC-13)
```

## 5. Candid reading

This note is both a reduction and an autopsy.

Reduction:
the denominator front is now completely handed off to one coupled normalized
`Delta theta` cocycle.

Autopsy:
normalizing by `1-theta_N` does **not** make pairwise or factorwise arguments
any safer. The zeta cancellation remains genuinely ternary even after
normalization.

So the next proof step must keep the three cocycle terms coupled all the way to
the normalized object.

## 6. Status

```text
proved:
  w_N is exactly the normalized ternary cocycle
  -(A_N+B_N+C_N)/(1-theta_N);

observed:
  on the common audited zeta ladder, the normalized parts and normalized pairs
  remain huge compared with |w_N|, so ternary cancellation survives
  normalization;

observed:
  the planted build does not reproduce that same giant normalized ternary
  profile;

reduced:
  further denominator progress to NORMALIZED-TERNARY-CANCEL;

next:
  derive the normalized cocycle as one coupled finite cell/Loewner object, or
  isolate which signed combination inside the ternary cocycle controls
  Re(w_N).
```
