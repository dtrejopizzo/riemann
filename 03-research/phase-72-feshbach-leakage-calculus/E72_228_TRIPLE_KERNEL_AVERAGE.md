# E72.228 - Triple kernel average

## Purpose

E72.227 showed that the high-block cubic sign is not cellwise. This probe asks whether the continuous
triple kernel

```text
T(u,v,w)=Tr(M_u M_v M_w)
```

is pointwise nonnegative on the high cube `(0.60,1]^3`, which would imply HOC3 for any positive
measure on that cube.

## Diagnostic

Script:

```text
E72_228_triple_kernel_sign_probe.py
```

Output:

```text
E72.228 triple kernel sign probe
T(u,v,w)=Tr(M_u M_v M_w), where M_u is the Hermitian compressed one-sided cell
High HOC3 wants weighted sum of T over high cube >=0
lam block minT maxT negFrac meanT worst_u worst_v worst_w
 12     0 -1.264305e-03 +1.625061e-04 0.875 -2.232547e-04 0.050 0.050 0.050
 12     1 -1.337391e-04 +9.626536e-05 0.604 +3.686122e-06 0.620 0.620 0.671
 16     0 -2.989801e-04 +3.049021e-04 0.773 -5.454996e-05 0.050 0.286 0.050
 16     1 -2.522086e-05 +2.260655e-05 0.664 +1.180267e-06 0.826 0.826 0.826
 24     0 -2.048358e-04 +1.658916e-05 0.963 -2.622079e-05 0.050 0.050 0.050
 24     1 -7.582601e-06 +8.378559e-06 0.633 +3.264433e-07 0.774 0.774 0.774
 32     0 -8.500220e-05 +1.494463e-05 0.639 -5.082954e-06 0.050 0.050 0.050
 32     1 -3.344741e-06 +2.342212e-06 0.566 +1.060496e-07 0.877 0.877 0.877
```

## Reading

Pointwise positivity fails on the high cube:

```text
min T < 0,
negFrac > 0.
```

However the unweighted grid average on the high cube is positive in all tested windows:

```text
mean_{u,v,w in high} T(u,v,w) > 0.
```

This matches HOC3 after the sign convention `A_n=-beta_n M_n`: the high cubic is negative precisely
when the positive weighted average of `T` is positive.

## Consequence

The valid proof target is not:

```text
T(u,v,w) >= 0 pointwise.
```

It is an averaged positivity theorem:

```text
int_{[0.60,1]^3} T(u,v,w) dmu_L(u)dmu_L(v)dmu_L(w) >= 0,
```

for the discrete positive prime-power measure

```text
dmu_L = sum_{0.60L < log n <= L} (Lambda(n)/sqrt(n)) delta_{log n/L}.
```

This is still zero-free in formulation. The arithmetic enters only as a positive measure on the high
window.
