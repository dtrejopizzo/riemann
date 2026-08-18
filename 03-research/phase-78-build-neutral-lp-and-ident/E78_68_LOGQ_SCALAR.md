# E78.68 - The old-old shell numerator is exactly a radial-plus-wrapped-phase log-q gain

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.67 reduced the live shell numerator to

```text
PAIRNUM_N = |q_N|^2 Re(1-exp(-Delta ell_N)),             (LQS-1)
```

on the old-old chain, where

```text
q_N = 1-theta_old(N),
Delta ell_N = log q_N - log q_{N+2}.                     (LQS-2)
```

This note scalarizes the remaining sign content without splitting the object.

## 2. Exact scalar identity

Write

```text
Delta ell_N = a_N + i b_N,
a_N := Re Delta ell_N,
b_N := Im Delta ell_N.                                   (LQS-3)
```

Then

```text
exp(-Delta ell_N) = exp(-a_N) (cos b_N - i sin b_N),     (LQS-4)
```

so taking real parts in `(LQS-1)` yields the exact scalar form

```text
PAIRNUM_N
 = |q_N|^2 [ 1 - exp(-a_N) cos b_N ].                    (LQS-5)
```

Therefore the sign of the old-old shell numerator is controlled exactly by the
single scalar gain

```text
LOGQ-GAIN_N := 1 - exp(-Re Delta ell_N) cos(Im Delta ell_N). (LQS-6)
```

No approximation has been used.

## 3. Structural reading

`LOGQ-GAIN_N` separates the two geometric ingredients of the old-old log update:

```text
radial part:   exp(-Re Delta ell_N),
angular part:  cos(Im Delta ell_N).                      (LQS-7)
```

But the target is still one coupled scalar. The note does **not** replace it by
independent bounds on these two pieces.

It only shows that the shell numerator is positive exactly when the wrapped
logarithmic update gains enough real contraction to beat any angular loss.

## 4. Probe audit

Companion:

```text
E78_68_logq_scalar_probe.py
E78_68_logq_scalar_results.json
```

The scalar reconstruction `(LQS-5)` holds to roundoff on the common certified
ladder:

```text
zeta:   max reconstruction error <= 3.47e-18,
plant:  max reconstruction error <= 1.42e-14.            (LQS-8)
```

### Zeta

Across the audited zeta ladder:

```text
Re Delta ell_N:
  min = 8.142e-2,  median = 1.370e-1,  max = 2.202e-1

|wrapped Im Delta ell_N|:
  min = 4.816e-5,  median = 8.393e-4,  max = 1.220e-3

LOGQ-GAIN_N:
  min = 7.463e-2,  median = 1.280e-1,  max = 1.976e-1.  (LQS-9)
```

So on zeta the old-old log update is in a clean regime:

```text
positive radial gain,
phase extremely close to 2 pi Z,
strictly positive scalar gain.                           (LQS-10)
```

### Planted build

Across the audited planted ladder:

```text
Re Delta ell_N:
  min = -1.398,  median = -2.937e-1,  max = 1.247

|wrapped Im Delta ell_N|:
  min = 1.011e-2,  median = 6.352e-2,  max = 1.414e-1

LOGQ-GAIN_N:
  min = -2.569,  median = -2.656e-1,  max = 7.130e-1.   (LQS-11)
```

So the planted build loses the zeta regime already at this exact scalar level:
the radial part can reverse sign, the phase is not comparably tiny, and the
combined scalar gain changes sign.

## 5. Consequence

This is a real reduction of the live object:

```text
OLD-OLD-LOGQ-CONTRACTION
<=>
LOGQ-GAIN-SIGN:
  prove that 1-exp(-Re Delta ell_N) cos(Im Delta ell_N)
  stays positive on the zeta cofinal path.               (LQS-12)
```

It is still one coupled scalar, but now the exact content of the sign problem is
fully explicit.

## 6. Candid reading

This does not prove positivity yet. What it does is remove all remaining
ambiguity about what positivity means on the old-old logarithmic front.

The next admissible theorem-grade step is to derive the zeta-side positivity of
`LOGQ-GAIN_N` from the invariant `LOGT-CELL` update, not by appealing to the
numerical table alone.

## 7. Status

```text
proved:
  PAIRNUM_N = |q_N|^2 [1-exp(-Re Delta ell_N) cos(Im Delta ell_N)] exactly on
  the old-old chain;

observed:
  zeta lies in a regime of positive Re Delta ell_N and extremely small wrapped
  phase, yielding positive scalar gain on every audited row;

observed:
  the planted build loses that regime and the scalar gain changes sign;

reduced:
  OLD-OLD-LOGQ-CONTRACTION to the exact scalar target LOGQ-GAIN-SIGN.
```
