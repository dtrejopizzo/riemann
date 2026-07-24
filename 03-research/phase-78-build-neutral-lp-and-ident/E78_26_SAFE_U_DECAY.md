# E78.26 - `SAFE-U-WEIGHTED-MONOTONICITY` is strict decay of `A_N = N Delta safe_u_N`

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.25 reduced the sign target to

```text
SAFE-U-WEIGHTED-MONOTONICITY:
  N Delta safe_u_N > (N+2) Delta safe_u_{N+2}.           (SD-1)
```

This note just names the one-dimensional sequence that this inequality is
really about.

## 2. Exact reformulation

Define

```text
A_N := N Delta safe_u_N.                                  (SD-2)
```

Then `(SD-1)` becomes

```text
A_N > A_{N+2}.                                            (SD-3)
```

So E78.25 is exactly:

```text
SAFE-U-DECAY:
  the real sequence A_N = N Delta safe_u_N decays strictly
  along the zeta cofinal path.                            (SD-4)
```

Combined with E78.25,

```text
SAFE-U-DECAY
=> SAFE-U-WEIGHTED-MONOTONICITY
=> SAFE-U-CURVATURE-SIGN
=> THETA-SIGN-STABILITY.                                  (SD-5)
```

This is not a new theorem; it is the cleanest exact repackaging of the current
sign front.

## 3. Probe audit

Companion:

```text
E78_26_safe_u_decay_probe.py
E78_26_safe_u_decay_results.json
```

The probe computes `A_N` and checks strict decay step by step.

### Zeta

On the audited `sigma in {1,3}` ladder:

```text
strict decay count      = 12
strict decay fails      = 0.                              (SD-6)
```

Representative values:

```text
sigma=1.0:
  A_8  = 0.254731
  A_10 = 0.206073
  A_12 = 0.168553
  A_14 = 0.144619
  A_16 = 0.122692
  A_18 = 0.108070

sigma=3.0:
  A_8  = 0.734086
  A_10 = 0.602062
  A_12 = 0.496087
  A_14 = 0.427707
  A_16 = 0.363953
  A_18 = 0.321295.                                        (SD-7)
```

So the zeta target is now a plain strict decay law for a positive real
sequence.

### Planted build

The planted build breaks that decay after the sign change:

```text
strict decay count      = 8
strict decay fails      = 4.                              (SD-8)
```

Representative failures:

```text
sigma=1.0:
  A_14 = -0.0143062
  A_16 = -0.00747292     (not decreasing)
  A_18 =  0.00342125     (not decreasing)

sigma=3.0:
  A_14 = -0.00750306
  A_16 = -0.00460212     (not decreasing)
  A_18 =  0.0168641.     (not decreasing)                (SD-9)
```

So the falsifier fails exactly as this reformulation predicts: once `A_N`
stops decaying, the sign front collapses.

## 4. Honest reading

This is a very strong simplification of the live sign target.

Instead of asking for positivity of a compressed curvature coefficient, we now
ask for:

```text
strict decay of one explicit real scalar sequence A_N.    (SD-10)
```

That is likely the best theorem-grade form reached so far for the sign side of
IDENT.

It still does **not** prove the decay theorem. But it tells us exactly what to
prove next, with no extra baggage.

## 5. Status

```text
proved:
  SAFE-U-WEIGHTED-MONOTONICITY is exactly strict decay of
  A_N = N Delta safe_u_N;

observed:
  zeta satisfies strict decay on the audited ladder;

observed:
  the planted build fails strict decay exactly where the sign front breaks;

reduced:
  the sign side of IDENT to the one-dimensional target SAFE-U-DECAY;

next:
  derive strict decay of A_N from the u-sector law plus a quantitative
  envelope for Delta safe_u on the zeta path.
```
