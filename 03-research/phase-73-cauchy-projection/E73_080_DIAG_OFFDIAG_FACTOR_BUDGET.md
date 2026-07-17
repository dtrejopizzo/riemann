# E73.080 - Diagonal/off-diagonal factor budget

## 1. Purpose

E73.078 reduces the complete-mesh budget to:

```text
sum_k W_k
sum_w ( |A_L(z_k,w)||H_0(w)| + |B_L(z_k,w)||H_0(-w)| )
<= C L^-5.
```

E73.077 shows that the largest coefficients occur near equal heights.  Since the evaluation point
has `Re z=sigma>0` while zero-window nodes have `Re w=0`, there is no true pole.  This note records
both the crude uniform bound and the optional height-near/far split.

## 2. Coefficient scale

Recall

```text
A_L(z,w)
= i[(e^(wL)-1)+e^(zL)(e^(-wL)-1)]/(w-z),
```

and

```text
B_L(z,w)
= -i[e^(zL)(e^(wL)-1)+(e^(-wL)-1)]/(w+z).
```

On the critical zero-node window `w=i gamma`, `|e^(wL)|=1`.  For `z=sigma+i tau` with fixed
`sigma>0`,

```text
|A_L(z,w)| <= C e^(sigma L)/|w-z|,
|B_L(z,w)| <= C e^(sigma L)/|w+z|.
```

This bound is crude but explicit.

## 3. Uniform shifted-strip bound

If `Re z=sigma>0` and `Re w=0`, then

```text
|w-z|>=sigma,
|w+z|>=sigma.
```

Consequently:

```text
|A_L(z,w)|+|B_L(z,w)| <= C_sigma e^(sigma L).          (1)
```

This gives the simple sufficient estimate:

```text
UNIFORM-FACTOR:
sum_k W_k e^(sigma L)
sum_{w in Z_T/+-} ( |H_0(w)|+|H_0(-w)| )
<= C L^-5.                                           (2)
```

This avoids a fake singular diagonal.  It is the preferred analytic target when the shifted
evaluation line has fixed `sigma`.

## 4. Optional height-near split

Fix a separation scale

```text
Delta_L=L^-q
```

with `q>=0`.  For each FAR3 node `z_k`, define:

```text
D_k={w in Z_T/+- : |Im w-Im z_k|<=Delta_L or |Im w+Im z_k|<=Delta_L},
O_k=(Z_T/+-)\D_k.
```

The factor budget splits as:

```text
CoeffBudget_k=DiagBudget_k+OffBudget_k.
```

## 5. Off-height sufficient estimate

On `O_k`,

```text
|A_L(z_k,w)|+|B_L(z_k,w)| <= C e^(sigma L) Delta_L^-1.
```

Thus

```text
OffBudget_k
<= C e^(sigma L) Delta_L^-1
sum_{w in O_k} ( |H_0(w)|+|H_0(-w)| ).               (1)
```

Therefore an off-diagonal theorem sufficient for the main budget is:

```text
OFF-FACTOR:
sum_k W_k e^(sigma L) Delta_L^-1
sum_{w in O_k} ( |H_0(w)|+|H_0(-w)| )
<= C L^-5.
```

## 6. Near-height sufficient estimate

The near-height set contains only the resonant height nodes.  The direct target is:

```text
NEAR-FACTOR:
sum_k W_k
sum_{w in D_k}
( |A_L(z_k,w)||H_0(w)|+|B_L(z_k,w)||H_0(-w)| )
<= C L^-5.
```

This should use the fixed shifted-line gap `|w-z|>=sigma`, not a removable diagonal argument.

## 7. Current endpoint

The complete-mesh factor budget follows from:

```text
UNIFORM-FACTOR => FACTOR-MAIN-5.
```

Alternatively:

```text
NEAR-FACTOR + OFF-FACTOR => FACTOR-MAIN-5.
```

Together with `TAIL-NODAL-5`, either route gives:

```text
FACTOR-MAIN-5 + TAIL-NODAL-5 => BALANCED-PACKET-ROW-5 => scalar WRL.
```

## 8. Status

```text
proved: no true diagonal singularity on shifted line Re z=sigma>0;
reduced: FACTOR-MAIN-5 to UNIFORM-FACTOR, or to NEAR/OFF factor estimates;
open: prove the corresponding nodal H_0 budget uniformly.
```
