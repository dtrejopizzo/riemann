# E78.28 - Geometric-envelope form of the `safe_u` sign front

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.27 sharpened the sign-side target to the contraction law

```text
rho_N := A_{N+2}/A_N <= rho_* < 1,                        (SG-1)
```

for

```text
A_N := N Delta safe_u_N.                                  (SG-2)
```

But for theorem use we really need the full positive geometric envelope

```text
0 < A_{N+2} <= rho_* A_N.                                 (SG-3)
```

This note names that exact target and audits it on the certified rows.

## 2. Exact target

Define:

```text
SAFE-U-GEOMETRIC-ENVELOPE:
  there exists rho_* < 1 such that

    0 < A_{N+2} <= rho_* A_N

  on the zeta cofinal path.                               (SG-4)
```

This is strictly stronger than E78.27, because it bundles:

```text
- positivity of A_N,
- contraction of A_{N+2}/A_N.                             (SG-5)
```

Therefore

```text
SAFE-U-GEOMETRIC-ENVELOPE
=> SAFE-U-CONTRACTION
=> SAFE-U-DECAY
=> THETA-SIGN-STABILITY.                                  (SG-6)
```

## 3. Probe audit

Companion:

```text
E78_28_safe_u_geometric_envelope_probe.py
E78_28_safe_u_geometric_envelope_results.json
```

### Zeta

On the audited `sigma in {1,3}` ladder:

```text
positive-envelope count      = 12
positive-envelope fails      = 0
observed rho_*               = 0.9122297392646584.        (SG-7)
```

So every audited zeta step satisfies

```text
0 < A_{N+2} <= 0.91223 A_N.                               (SG-8)
```

Representative rows:

```text
sigma=1.0:
  A_8  = 0.254731, A_10 = 0.206073, ratio = 0.808984
  A_16 = 0.122692, A_18 = 0.108070, ratio = 0.880819

sigma=3.0:
  A_8  = 0.734086, A_10 = 0.602062, ratio = 0.820152
  A_18 = 0.321295, A_20 = 0.293095, ratio = 0.912230.     (SG-9)
```

### Planted build

The plant fails the geometric envelope by losing positivity, not only by
failing contraction:

```text
positive-envelope count      = 8
positive-envelope fails      = 4.                          (SG-10)
```

Typical failures:

```text
sigma=1.0:
  A_12 =  0.0208620, A_14 = -0.0143062   (sign loss)
  A_14 = -0.0143062, A_16 = -0.00747292  (not positive)

sigma=3.0:
  A_12 =  0.0536114, A_14 = -0.00750306  (sign loss)
  A_16 = -0.00460212, A_18 =  0.0168641  (sign flip).     (SG-11)
```

So the falsifier breaks the stronger envelope exactly by oscillating across
zero.

## 4. Consequence

This is now the strongest honest one-dimensional target on the sign side of
IDENT:

```text
prove a positive geometric envelope for A_N = N Delta safe_u_N. (SG-12)
```

That is better than mere monotonicity because it carries immediate summability
and a quantitative rate.

## 5. Honest reading

This note does **not** prove the theorem-grade envelope.  It only shows that
the audited zeta rows already satisfy a clean geometric pattern with a visible
candidate constant around `0.913`, while the planted build fails by sign loss.

That is exactly the kind of reduced target worth carrying forward:

```text
explicit, quantitative, one-dimensional, and falsifier-sensitive. (SG-13)
```

## 6. Status

```text
proved:
  SAFE-U-GEOMETRIC-ENVELOPE is the exact strengthened form of the current
  sign-side target;

observed:
  all audited zeta rows satisfy 0 < A_{N+2} <= 0.91223 A_N;

observed:
  the planted build fails the envelope by losing positivity and oscillating
  across zero;

reduced:
  the sign side of IDENT from SAFE-U-CONTRACTION to SAFE-U-GEOMETRIC-ENVELOPE;

next:
  seek a theorem-grade derivation of the geometric envelope from the u-sector
  law plus exact shell updates for safe_u.
```
