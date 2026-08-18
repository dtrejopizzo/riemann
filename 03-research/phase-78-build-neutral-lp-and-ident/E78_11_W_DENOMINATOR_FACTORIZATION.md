# E78.11 - Denominator factorization through the shell-resolvent geometry

**Run:** 2026-07-18.
**Scope:** IDENT, fixed-L finite front.

## 1. Purpose

E78.8 showed that the denominator `1+W` is huge in the zeta build and safely
nonzero in the planted build, but it did not explain *why*.  This note links
that denominator back to the exact shell-resolvent factors already isolated in
Phase 77.

## 2. Exact identity

From P76.041:

```text
T(z)=F(z)/(z-d_b),                    F(z)=1+W(z).            (DF-1)
```

From E77.5f / E77.5aa:

```text
T(z)=t0(z)-corr(z)=t0(z)(1-theta(z)),
theta(z)=corr(z)/t0(z).                                      (DF-2)
```

Combining `(DF-1)` and `(DF-2)` gives the exact factorization

```text
1+W(z) = (z-d_b) t0(z) (1-theta(z)).                        (DF-3)
```

This identity is exact for every finite section.

## 3. Consequence

The large-denominator geometry from E78.10 is not a mysterious feature of the
two-generator package.  It is the same shell geometry already present in Phase
77, now written in the `W` coordinate:

```text
large |1+W|
 = large |z-d_b|
   * |t0|
   * |1-theta|.                                             (DF-4)
```

So any explanation of the zeta quotient-delta must pass through the old exact
factors:

```text
t0      (core anchor),
1-theta (active Schur anchor).                              (DF-5)
```

## 4. Probe

Companion:

```text
E78_11_w_denominator_factor_probe.py
E78_11_w_denominator_factor_results.json
```

The probe verifies `(DF-3)` directly on the safe ladder and records the factor
magnitudes.

## 5. Status

## 5. Audit

The factorization probe verifies `(DF-3)` to roundoff on the short safe ladder.
Representative rows, choosing the safe sample where `|F|=|1+W|` is minimal:

### Zeta

```text
N= 8:  |1+W| = 7.10e5,   |z-d_b| = 14.34,
       |T|   = 4.95e4,   |1-theta| = 3.27e-1.

N=10:  |1+W| = 1.68e6,   |z-d_b| = 17.79,
       |T|   = 9.44e4,   |1-theta| = 2.67e-1.
```

### Planted build

```text
N= 8:  |1+W| = 2.05e1,   |z-d_b| = 14.34,
       |T|   = 1.43,     |1-theta| = 2.30.

N=10:  |1+W| = 6.64,     |z-d_b| = 17.79,
       |T|   = 3.73e-1,  |1-theta| = 4.98.
```

Maximum reconstruction errors:

```text
zeta:   2.91e-38, 1.25e-33;
plant:  4.62e-60, 3.74e-60.
```

So `(DF-3)` is numerically certified.

## 6. Reading

This explains the denominator geometry very cleanly.

In the zeta build:

```text
|1-theta| is small-to-moderate (< 1),
but |T| is huge,
so the product (z-d_b) T = 1+W is enormous.
```

In the planted build:

```text
|1-theta| is large,
but |T| is tiny-to-moderate,
so the product stays modest.
```

Therefore the huge zeta denominator is **not** caused by a large `|1-theta|`.
It is the shell-transfer amplification `|T|` (equivalently `|t0(1-theta)|`)
that dominates.

This is a useful correction to the naive picture:

```text
the Phase-77 near-anchor law explains part of the regime,
but the real denominator amplification in W-coordinates is carried mainly by
the transfer scale T, not by the magnitude of 1-theta alone.
```

## 7. Consequence

The live front can now be expressed entirely in exact shell terms:

```text
W-QUOTIENT-DELTA
 = Delta[T'/T] up to the fixed boundary pole
```

and

```text
1+W = (z-d_b) t0 (1-theta).
```

So the remaining arithmetic difficulty is not an unexplained large denominator.
It is the signed interaction among:

```text
the large transfer scale T,
the near-anchor factor 1-theta,
and the quotient defect Delta[T'/T].
```

This keeps the Phase-78 front aligned with the exact Phase-77 shell geometry.

## 8. Status

```text
proved:
  exact factorization 1+W = (z-d_b)t0(1-theta);

observed:
  the zeta denominator is huge mainly because |T| is huge while |1-theta| stays
  below 1 on the tested rows;

observed:
  the planted build has large |1-theta| but small/moderate |T|, so |1+W| stays
  modest;

clarified:
  the large-denominator geometry of IDENT is a shell-transfer amplification,
  not a standalone denominator-zero phenomenon and not a large-|1-theta|
  phenomenon by itself;

next:
  fold this into the live front and search for an exact shell law governing the
  transfer-scale amplification together with the quotient defect.
```
