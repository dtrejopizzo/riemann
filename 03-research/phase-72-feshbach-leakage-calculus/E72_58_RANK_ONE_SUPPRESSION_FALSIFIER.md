# E72.58 -- Falsifier for literal rank-one endpoint suppression

**Date:** 2026-07-08.
**Role:** correct E72.56. The endpoint rank-one term exists, but it is not suppressed by
`<v,1><1,k>` being small.

## 0. Diagnostic

For the `Lambda`-weighted endpoint channel, the product

```text
|<v_{x,s},1><1,k_x>|
```

is not small in the tested finite windows:

```text
x=36:   2.82e-1
x=64:   1.83e-1
x=100:  2.29e-1
x=144:  3.15e-1
x=196:  2.26e-1
```

The rank-one leading contribution is often comparable to or larger than the final endpoint scalar
channel.

## 1. Consequence

The target:

```text
<v_{x,s},1><1,k_x> -> 0
```

is false in the current normalization and cannot be the proof mechanism.

The endpoint rank-one term must instead be treated as part of the PNT/model main term. It is not
something that vanishes before main-term subtraction.

## 2. Correct interpretation of E72.56

E72.56 remains useful because:

```text
Q_x(L-r)=(2r/L)J+higher.
```

But this says:

```text
the leading endpoint layer is low-rank and should be absorbed by the continuous model.
```

It does **not** say:

```text
the leading endpoint layer is small by itself.
```

## 3. Correct next object

The scalar endpoint discrepancy must be measured after subtracting the continuous model:

```text
D_x(s;z)
 = sum_{n<=x} Lambda(n)(n/x)^z n^(-1/2)a(log n)
   - int_1^x (u/x)^z u^(-1/2)a(log u)du.
```

Only `D_x`, not the raw prime endpoint sum, is the post-main object relevant to scalar WRL.

## 4. Status

```text
falsified: literal rank-one endpoint suppression;
corrected: rank-one endpoint term belongs to model-main matching;
open: measure/prove smallness of the post-main scalar endpoint discrepancy D_x.
```
