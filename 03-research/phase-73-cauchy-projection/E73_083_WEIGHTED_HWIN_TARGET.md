# E73.083 - Weighted HWIN target

## 1. Purpose

E73.082 shows that the blind estimate

```text
sum_{w in Z_T/+-} ( |H_0(w)|+|H_0(-w)| )
```

is not the sharp final object for large windows.  The budget must retain the actual coefficient
weights from the exact pair divisibility.

## 2. Definition

For a FAR3 evaluation node `z_k`, define:

```text
HWIN_k
:= sum_{w in Z_T/+-}
   ( |A_L(z_k,w)||H_0(w)| + |B_L(z_k,w)||H_0(-w)| ).
```

This is exactly `CoeffBudget_k` from E73.078.

## 3. Weighted theorem

The complete-mesh main budget follows from:

```text
WEIGHTED-HWIN-5:
sum_{gamma_k in FAR3(A,L)} W_k(A,L) HWIN_k
<= C L^-5.
```

This is sharper than `UNIFORM-FACTOR`, because it does not replace the coefficients by their crude
uniform upper bound.

## 4. Why this is the right endpoint

E73.075 gives exact divisibility:

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

Therefore `HWIN_k` is not an invented majorant.  It is the exact separated absolute budget of the
complete-mesh pair packet at the finite nodal window.

E73.082 shows why a blind window sum is too coarse.  The coefficient-weighted version keeps:

```text
1. FAR3 evaluation nodes;
2. actual shifted-line denominators;
3. actual phase factors e^(wL), e^(zL);
4. actual Cauchy divisor values.
```

## 5. Updated route

The current route is:

```text
WEIGHTED-HWIN-5 + TAIL-NODAL-5 + Tail_3<=C_tail L^-9
=> BUD-5/9
=> WCS
=> scalar WRL.
```

## 6. Remaining theorem

The remaining theorem is now finite and explicit:

```text
prove WEIGHTED-HWIN-5 uniformly for the natural-height finite CCM data.
```

All objects are computable from:

```text
d_n, xi_n, L, FAR3(A,L), Z_T, A_L, B_L.
```

## 7. Status

```text
proved: exact pair-divisor formula supplies HWIN_k;
observed: blind window H_0 sum is too crude in larger windows;
open: prove WEIGHTED-HWIN-5 uniformly.
```
