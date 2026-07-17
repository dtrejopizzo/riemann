# E73.101 - Scope audit after the unified verifier

## 1. What is closed

The Mellin spectral divisibility required by the scalar WRL route is closed at the algebraic packet
level:

```text
Pair_z^infty(w)
= A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

Thus:

```text
Pair_z^infty(w) in (H_0(w),H_0(-w)).
```

The actual finite packet differs from the complete mesh by the explicit tail nodal operator:

```text
Lcal(B_z^tail)= -2i/L sum_w wG_x(w)R_M(z,w),
```

with rational kernel bounds from E72.392.  Therefore the finite packet is controlled by:

```text
TAIL-LC-BUD.
```

The outside high zero tail beyond the natural height is also closed:

```text
OUT-HIGH        [E72.394].
```

## 2. What is reduced to a finite verifier

The full finite scalar-WRL gate is:

```text
GATE-73
= LOCK-COMP-BUD
+ TAIL-LC-BUD
+ OUT-FAR
+ FAR3-MAIN-RAT.
```

E73.099 proves:

```text
GATE-73 => scalar WRL.
```

E73.100 verifies all four gates in the tested finite natural-height boxes.

## 3. What is not yet proved

The following uniform theorem remains open:

```text
Uniform GATE-73:
there exist constants independent of the natural-height cluster box A
such that GATE-73(A,L) holds for all sufficiently large L.
```

This uniform theorem is exactly where the remaining arithmetic difficulty lives.

## 4. Why this is progress

Earlier formulations still had hidden analytic objects:

```text
Cauchy inverses;
Mellin packet divisibility;
finite Fourier tail;
outside zero tail;
rowspace distance.
```

After E73.100, the live objects are only:

```text
finite rational functions P_x/D_x;
finite Cauchy roots Div(P_x);
elementary Hermite/mesh weights W_k;
explicit polynomial tail factors L^2/M^2;
finite FAR-selected critical rows.
```

This is the promised finite, falsifiable certificate form for the Phase 72 route.

## 5. Next mathematical target

Since E73.100 identifies `FAR3-MAIN-RAT` as the limiting gate, the next analytic theorem should
attack:

```text
sum_{gamma_k in D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
<= C_main L^-5
```

uniformly over natural-height cluster boxes.
