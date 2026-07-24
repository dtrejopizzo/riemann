# E78.87 - Sigma monotonicity would reduce the modulus quotient to the left endpoint

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.85 and E78.86 reduced the endpoint quotient to

```text
MODULUS-QUOTIENT
+ ALPHA-SMALLNESS.                                       (MQE-1)
```

The denominator side is now a one-scalar problem. This note records the exact
payoff of proving the remaining sigma monotonicity on the modulus side.

## 2. Exact transfer

Define

```text
M_N(sigma)
 := (-SAFEDELTA_N(i sigma)) / modulus_term_N.           (MQE-2)
```

Assume the monotonicity statement

```text
SIGMA-MONOTONE-MODULUS-QUOTIENT:
  M_N(sigma) decreases in sigma on the safe compact.    (MQE-3)
```

Then on any compact interval

```text
sigma in [sigma_L, sigma_R],    sigma_L > 0,            (MQE-4)
```

we obtain the exact endpoint reduction

```text
M_N(sigma) <= M_N(sigma_L).                             (MQE-5)
```

So the full modulus branch reduces to the single-slice target

```text
LEFT-ENDPOINT-MODULUS-QUOTIENT:
  M_N(sigma_L) <= C_*.                                  (MQE-6)
```

Combined with E78.86 this gives

```text
SIGMA-MONOTONE-MODULUS-QUOTIENT
+ LEFT-ENDPOINT-MODULUS-QUOTIENT
+ ALPHA-SMALLNESS
=> SECTOR-SIZE-QUOTIENT.                                (MQE-7)
```

That is a genuine reduction: the two-variable modulus front collapses to one
endpoint slice, leaving only one scalar denominator correction.

## 3. Probe audit

Companion:

```text
E78_87_modulus_quotient_endpoint_probe.py
E78_87_modulus_quotient_endpoint_results.json
```

Using the currently certified common audit from E78.85:

```text
sigma_L = 1.0,
sigma_R = 3.0.                                          (MQE-8)
```

Across all audited pairs, the modulus quotient decreases:

```text
M_N(3.0) <= M_N(1.0)    for every audited N.            (MQE-9)
```

Representative rows:

```text
N= 8:   M_8(1.0)=0.320100,   M_8(3.0)=0.306630
N=20:   M_20(1.0)=0.112374,  M_20(3.0)=0.096774.        (MQE-10)
```

On the endpoint slice itself:

```text
M_N(1.0)
  min    = 0.112374,
  median = 0.184207,
  max    = 0.320100,                                    (MQE-11)
```

with worst audited row

```text
N=8,   M_8(1.0)=0.32009971629837736.                    (MQE-12)
```

## 4. Consequence

The modulus branch now has the same clean logical shape as E78.82:

```text
1. prove sigma monotonicity of M_N(sigma),
2. prove the left-endpoint bound M_N(sigma_L) <= C_*.   (MQE-13)
```

No further sigma bookkeeping remains once `(MQE-3)` is proved.

## 5. Honest reading

This note does **not** prove `SIGMA-MONOTONE-MODULUS-QUOTIENT`.

What it proves is that such a theorem would immediately collapse the modulus
front to a single slice, and that the current certified ladder is fully
compatible with that reduction.

So the live modulus-side object is now explicit:

```text
LEFT-ENDPOINT-MODULUS-QUOTIENT
+ SIGMA-MONOTONE-MODULUS-QUOTIENT.                      (MQE-14)
```

## 6. Status

```text
proved:
  sigma monotonicity of the modulus quotient would reduce the whole modulus
  branch to the left endpoint exactly;

observed:
  on the currently certified zeta ladder M_N(3.0) <= M_N(1.0) for every
  audited N;

observed:
  the worst current audited modulus quotient is
  M_8(1.0)=0.32009971629837736;

reduced:
  MODULUS-QUOTIENT to
  SIGMA-MONOTONE-MODULUS-QUOTIENT + LEFT-ENDPOINT-MODULUS-QUOTIENT;

next:
  seek an exact derivative or shell formula for M_N(sigma) on the safe axis,
  now that the denominator side has been localized separately.
```
