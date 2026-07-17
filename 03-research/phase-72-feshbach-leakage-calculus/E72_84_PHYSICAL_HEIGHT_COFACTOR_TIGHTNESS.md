# E72.84 -- Physical-height cofactor tightness

**Date:** 2026-07-09.
**Role:** correct E72.83 by replacing fixed Fourier-index tightness with the stable physical-height
tightness.

## 0. Correction to E72.83

E72.83 observed that, for `s=10+0.2i` in the tested windows, the dual cofactor vector:

```text
g_{x,s}=B_xC_E^(-1)B_x^*r_s^even
```

had most of its mass in `|n|<=16`.

That observation is useful but the fixed-index formulation is not the invariant limit statement.
The mesh variable is:

```text
d_n = 2pi n/L.
```

For fixed spectral height `s`, the Cauchy source:

```text
r_s^even(n)=s/(s^2-d_n^2)
```

is organized by physical height `d_n`, not by the index `n`. A fixed physical height corresponds to
`n=O(L)`. Therefore the right compactness statement must use `|d_n|`, not fixed `|n|`.

## 1. Physical tightness statement

For a height cutoff `H`, define:

```text
Pi_{>H}^{phys}g := 1_{|d_n|>H}g_n.
```

The corrected theorem candidate is:

```text
Physical dual cofactor tightness (PDCT):
For every compact s-window K in the admissible strip,

lim_{H->infty} limsup_{x->infty} sup_{s in K}
  ||Pi_{>H}^{phys}g_{x,s}||^2 / ||g_{x,s}||^2 = 0.             (PDCT)
```

This is the stable replacement for the fixed-index statement in E72.83.

## 2. Numerical evidence

The companion script:

```text
E72_84_dual_cofactor_physical_tightness_probe.py
```

tests several `s` values and reports mass below physical-height cutoffs.

Representative output:

```text
lambda=20, N=40:
       s  E|d|<=4  E|d|<=8  E|d|<=12  E|d|<=18  E|d|<=24
     2.0    0.974    0.984     0.987     0.991     0.992
     5.0    0.080    0.966     0.968     0.975     0.977
    10.0    0.026    0.072     0.956     0.992     0.996
    15.0    0.016    0.023     0.042     0.972     0.988

lambda=24, N=48:
     2.0    0.952    0.956     0.957     0.958     0.958
     5.0    0.084    0.990     0.993     0.993     0.994
    10.0    0.010    0.037     0.987     0.997     0.998
    15.0    0.004    0.010     0.026     0.989     0.998
```

Interpretation:

```text
for s near height T, the cofactor mass is concentrated in a physical band slightly above T.
```

This is exactly what the Cauchy source predicts.

## 3. Consequence for root transport

E72.81 becomes:

```text
i C_{g,k}(tau_j)
-(exp(i tau_jL)-1)L^(-1)C_{g,1}(tau_j)M_k(tau_j) -> 0.
```

Under `(PDCT)`, for every compact `s`-window and every `epsilon>0`, choose `H` so that the physical
tail of `g_{x,s}` is `epsilon` uniformly. Then the transport reduces to the finite physical-height
band:

```text
|d_n|<=H.
```

The number of modes in this band still grows like `L`, but the spectral height support is fixed. This
is the correct finite-dimensional limit object: a fixed physical window sampled by a finer CCM mesh.

## 4. Proof route

Let:

```text
P_H := 1_{|d_n|<=H},
T_H := I-P_H.
```

The equation for `g` is:

```text
C_E g = Q_even r_s^even.
```

Splitting low/high physical height gives:

```text
T_H g
 = (T_H C_E T_H)^(-1)T_HQ_even r_s^even
   - (T_H C_E T_H)^(-1)T_H C_E P_H g.                         (BT)
```

Thus `(PDCT)` follows from two estimates:

```text
source tail:       ||T_HQ_even r_s^even|| -> 0 as H->infty,
block decoupling:  ||(T_HC_ET_H)^(-1)T_HC_EP_H|| -> 0 as H->infty,
```

uniformly for large `x` and `s` in compact windows.

The source tail is elementary from `r_s^even(n)=O(d_n^-2)`. The remaining theorem is therefore the
physical high/low decoupling of the pole-relative even complement.

## 5. Status

```text
corrected: fixed-index DCTight is replaced by physical-height PDCT;
observed:  PDCT matches the finite harness for several s-heights;
open:      prove the high/low block decoupling estimate in (BT).
```
