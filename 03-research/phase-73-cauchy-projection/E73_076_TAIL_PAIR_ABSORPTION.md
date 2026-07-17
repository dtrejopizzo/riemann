# E73.076 - Tail pair absorption

## 1. Purpose

E73.075 proves the exact complete-mesh divisibility:

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

The actual finite packet is

```text
Pair_z^M(w)=Pair_z^infty(w)-Pair_z^tail(w).
```

This note records how the remaining tail is already controlled by the Phase 72 tail absorption
identity.

## 2. Tail as a nodal operator

E72.391 proves the exact identity

```text
Lcal(B_z^tail)
= -2i/L sum_w w G_x(w) R_M(z,w),                     (1)
```

where

```text
R_M(z,w)
:= sum_{|m|>M} (1-e^(zL))/[(iz-d_m)(w^2+d_m^2)].
```

Thus the finite Fourier tail is not an independent spectral object.  It is a linear operator on the
same nodal vector:

```text
{G_x(w)}.
```

## 3. Kernel size

E72.392 proves that for compact shifted windows away from mesh collisions,

```text
|R_M(z,w)| <= C_K e^(Re z L)L^3/M^2.
```

Therefore the tail operator coefficient in (1) satisfies

```text
|(-2i/L)wR_M(z,w)| <= C_K e^(Re z L)L^2/M^2.          (2)
```

At polynomial active cutoff

```text
M>=L^(1+epsilon),
```

this is lower order relative to the maximal Cauchy block.

## 4. Combined divisibility picture

For the transformed packet route, the two pieces now have different but compatible mechanisms:

```text
complete mesh:
  exact ideal membership (H_0(w),H_0(-w));

finite tail:
  explicit nodal operator on G_x(w), lower order after maximal-block scaling.
```

Thus `BALANCED-PACKET-ROW-5` reduces to the same finite nodal suppression statement already used by
the natural-height Cauchy projection system:

```text
NODAL-DIV:
G_x(w) is suppressed on the dangerous finite zero window with the FAR3 weighted budget.
```

## 5. Updated endpoint

The current Phase 73 core can now be stated as:

```text
EXACT-PAIR-DIV + TAIL-ABSORB + FAR3-NODAL-BUDGET
=> BALANCED-PACKET-ROW-5
=> ROW-MAIN-5
=> scalar WRL.
```

Here:

```text
EXACT-PAIR-DIV is proved in E73.075;
TAIL-ABSORB is E72.391--E72.392;
FAR3-NODAL-BUDGET is the remaining finite weighted nodal budget.
```

## 6. What remains

The remaining theorem is no longer a hidden Mellin divisibility statement.  It is the finite weighted
nodal budget:

```text
FAR3-NODAL-BUDGET:
the nodal values G_x(w) appearing in the tail operator and in the Cauchy divisor satisfy the
weighted L^-5/L^-9 FAR3 budget.
```

This is exactly the same budget schema as E73.056--E73.058, now with the complete-mesh packet
divisibility proved algebraically.

## 7. Status

```text
proved: complete-mesh pair divisibility;
imported: finite Fourier tail is lower-order nodal operator;
reduced: packet Mellin spectral divisibility to FAR3-NODAL-BUDGET;
open: prove the uniform FAR3 nodal budget.
```
