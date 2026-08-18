# E78.83 - The weighted safe-delta target is exactly a quotient law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.79-E78.82 promoted the weighted shell object

```text
Y_N(sigma) := N * (-SAFEDELTA_N(i sigma)) / A_N,       (WQL-1)
```

with

```text
A_N := N Delta safe_u_N.                               (WQL-2)
```

This note records the exact simplification hidden in those definitions: the
weight `N` cancels completely.

## 2. Exact quotient identity

Substituting `(WQL-2)` into `(WQL-1)` gives

```text
Y_N(sigma)
 = N * (-SAFEDELTA_N(i sigma)) / (N Delta safe_u_N)
 = (-SAFEDELTA_N(i sigma)) / Delta safe_u_N.           (WQL-3)
```

So the current weighted-safe-delta object is **exactly** the quotient

```text
WEIGHTED-QUOTIENT-LAW:
  Y_N(sigma) = (-SAFEDELTA_N(i sigma)) / Delta safe_u_N. (WQL-4)
```

Nothing else remains in it: no extra `N`-geometry, no hidden scale factor.

## 3. Consequence for the chain

This sharpens the radial front substantially. The target

```text
WEIGHTED-NORMALIZED-SAFEDELTA:
  Y_N(sigma) <= M                                         (WQL-5)
```

is equivalent to

```text
SAFEDELTA-SAFEU-QUOTIENT:
  (-SAFEDELTA_N(i sigma)) / Delta safe_u_N <= M.         (WQL-6)
```

Hence the whole weighted branch refactors as

```text
SAFEDELTA-SAFEU-QUOTIENT
=> WEIGHTED-NORMALIZED-SAFEDELTA
=> NORMALIZED-SAFEDELTA-AVERAGE
=> SAFEU-TAIL-COUPLING.                                  (WQL-7)
```

This is a genuine reduction because the numerator and denominator are both
native one-step objects already present in the certified front:

```text
-SAFEDELTA_N   from E77.5g,
Delta safe_u_N from E77.5ac / E78.24-E78.33.           (WQL-8)
```

## 4. Probe audit

Companion:

```text
E78_83_weighted_quotient_probe.py
E78_83_weighted_quotient_results.json
```

The probe reconstructs `(WQL-3)` directly on the common audited ladder.

Reconstruction is exact to roundoff:

```text
max quotient identity error < 1e-16.                    (WQL-9)
```

Representative rows:

```text
sigma=1.0:
  N= 8  Y = 0.320335 = 0.0101999 / 0.0318414
  N=18  Y = 0.126929 = 0.0007621 / 0.00600388

sigma=3.0:
  N= 8  Y = 0.306657 = 0.0281391 / 0.0917608
  N=18  Y = 0.125781 = 0.00224516 / 0.0178497.         (WQL-10)
```

So the weighted-safe-delta front is not merely *like* a quotient law. It is one.

## 5. Candid reading

This note does not prove a uniform bound on the quotient `(WQL-6)`.

What it proves is that the burden has been localized exactly:

```text
the radial weighted front is a comparison between
the radial safe derivative and the shell safe_u drift.  (WQL-11)
```

That is strictly sharper than carrying `N*(-SAFEDELTA)/A` as an opaque object.

## 6. Status

```text
proved:
  the weighted-safe-delta object is exactly the quotient
  (-SAFEDELTA_N)/Delta safe_u_N;

proved:
  the quotient identity reconstructs to roundoff on the common audited ladder;

reduced:
  WEIGHTED-NORMALIZED-SAFEDELTA to the simpler one-step target
  SAFEDELTA-SAFEU-QUOTIENT.
```
