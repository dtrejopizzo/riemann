# E78.80 - The audited weighted normalized shell derivative is compatible with a constant envelope

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.79 isolated the pointwise target

```text
WEIGHTED-NORMALIZED-SAFEDELTA:
  N * (-SAFEDELTA_N(i sigma)) / A_N <= M(sigma).       (CWS-1)
```

This note audits the simplest possible refinement:

```text
can M(sigma) be taken essentially constant
on the currently certified sigma window?                (CWS-2)
```

## 2. Probe audit

Companion:

```text
E78_80_constant_weighted_safedelta_probe.py
E78_80_constant_weighted_safedelta_results.json
```

Using the common zeta ladder `sigma in {1.0,3.0}`, `N=8,10,12,14,16,18`, the
probe evaluates

```text
Y_N(sigma) := N * (-SAFEDELTA_N(i sigma)) / A_N.       (CWS-3)
```

The global statistics are:

```text
min    = 1.2578e-1,
median = 1.8560e-1,
max    = 3.2034e-1.                                    (CWS-4)
```

So the whole audited front is already contained in the constant band

```text
Y_N(sigma) <= 0.321                                    (CWS-5)
```

with a very small observed sigma effect.

## 3. Sigma-stability

At fixed `N`, the two audited sigma slices are extremely close:

```text
N= 8:  Y(3.0)/Y(1.0) ≈ 0.9573
N=10:  Y(3.0)/Y(1.0) ≈ 0.9672
N=12:  Y(3.0)/Y(1.0) ≈ 0.9825
N=14:  Y(3.0)/Y(1.0) ≈ 0.9835
N=16:  Y(3.0)/Y(1.0) ≈ 0.9904
N=18:  Y(3.0)/Y(1.0) ≈ 0.9910.                         (CWS-6)
```

So on every common audited row,

```text
Y_N(3.0) < Y_N(1.0),                                   (CWS-7)
```

and the difference shrinks with `N`.

This is strong evidence that the dominant burden is the `N` weight itself; the
residual sigma dependence may be harmless on the current safe compact.

## 4. Consequence

This suggests a sharper candidate:

```text
CONSTANT-WEIGHTED-SAFEDELTA:
  N * (-SAFEDELTA_N(i sigma)) / A_N <= M_*             (CWS-8)
```

for a constant `M_*` on the safe sigma compact.

If that were proved with, say, any

```text
M_* < +infinity,                                        (CWS-9)
```

then E78.79 and E78.78 would immediately give

```text
TAIL_N(sigma_0,sigma) / A_N
 <= M_* (\sigma-\sigma_0) / (2N),                      (CWS-10)
```

which is already an explicit `O(1/N)` coupling law.

So the radial front sharpens once more:

```text
WEIGHTED-NORMALIZED-SAFEDELTA
<=
CONSTANT-WEIGHTED-SAFEDELTA.                           (CWS-11)
```

## 5. Candid reading

This note does **not** prove that a constant envelope is true cofinally.

It proves only that, on the current audited window, one does not yet need a
complicated sigma profile: a flat envelope already covers every certified row.

That is enough to justify trying the constant version first before introducing a
more elaborate `M(sigma)`.

## 6. Status

```text
observed:
  all audited zeta rows satisfy N*(-SAFEDELTA)/A <= 0.321;

observed:
  at fixed N the sigma=3.0 slice is uniformly below the sigma=1.0 slice and
  approaches it as N grows;

clarified:
  the simplest viable next target is the constant-envelope version
  CONSTANT-WEIGHTED-SAFEDELTA;

reduced:
  WEIGHTED-NORMALIZED-SAFEDELTA to the candidate constant law
  N*(-SAFEDELTA)/A <= M_* on the safe compact.
```
