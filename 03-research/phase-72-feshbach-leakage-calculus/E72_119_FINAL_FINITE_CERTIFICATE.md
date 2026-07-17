# E72.119 -- Final finite certificate for Phase 72

**Date:** 2026-07-09.
**Role:** package the current Phase 72 endpoint as one finite checklist.

## 0. Certificate data

Fix:

```text
physical band H,
bad-subspace rank q,
finite root-height window T,
compact Cauchy window K.
```

For each finite CCM window `x`, construct:

```text
D_x, k_x, xi_x, B_x, C_E,
finite roots tau_j<=T,
post-main frequency packets Y_x(tau_j),
mass row m_x,
shorted pushforward R_x,
bad subspace U_x=[mass direction, first q right singular directions].
```

All objects are finite matrices/vectors.

## 1. The four scalar/determinantal quantities

### Cauchy physical tail

```text
CCGD_x(H,K)
 := sup_{s in K}
    a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
    / a_x(s)^*C_E^(-2)a_x(s).                              (C)
```

### BNORM scalars

```text
MNorm_x(H,T)  := sup_{tau_j<=T} ||m_x||||Y_x(tau_j)||,
S1Norm_x(H,T) := sup_{tau_j<=T} sigma_1(R_x)||Y_x(tau_j)||,
SqNorm_x(H,T) := sup_{tau_j<=T} sigma_{q+1}(R_x)||Y_x(tau_j)||.   (N)
```

### Gram determinant saturation

Let:

```text
G_x=U_x^*U_x,
G_x[Y_j]=[G_x,U_x^*Y_j;Y_j^*U_x,Y_j^*Y_j].
```

Define:

```text
Sat_x(H,q,T)
 := inf_{tau_j<=T} det(G_x[Y_j])/(det(G_x)||Y_j||^2).        (S)
```

The final non-tail orthogonality condition is:

```text
Sat_x(H,q,T)->1.
```

## 2. Final finite certificate

### Theorem 72.119

Assume:

```text
(C-FIN)
lim_{H->infty}limsup_{x->infty} CCGD_x(H,K)=0,

(N-FIN)
MNorm_x(H,T)+S1Norm_x(H,T)+SqNorm_x(H,T)=O(1)
for each fixed H,T,

(S-FIN)
Sat_x(H,q,T)->1
for each fixed H,T.
```

Assume the corresponding one `s`-derivative estimates required in E72.68.  Then scalar WRL resonance
annihilation follows:

```text
x^rho L_x(s;x)-int_1^x u^rho partial_uL_x(s;u)du -> 0.
```

Consequently the Phase 72 Mellin spectral-divisibility route closes the terminal `Omega_7` criterion
provided the standard finite CCM spectral convergence input is available.

### Proof

`(S-FIN)` is exactly `GBORTH` by E72.117.  `(N-FIN)` is exactly `BNORM` by E72.118.  Hence E72.116
gives:

```text
MOP and DQF.
```

E72.113 gives post-main finite-band root transport from `MOP + DQF`.  `(C-FIN)` removes the physical
Cauchy tail through E72.87--E72.98.  E72.105 gives post-main HPAC divisibility, and E72.68 gives
scalar WRL resonance annihilation. `QED`

## 3. Master probe

The companion script:

```text
E72_119_final_certificate_probe.py
```

prints all finite quantities in one table for `q=3`, `H=8`, root window `T=6`, and Cauchy point
`s=5+0.2i`.

Representative output:

```text
E72.119 final finite certificate probe q=3, H=8, s=5+0.2i
 lam   N roots    CCGD     GraphN    MNorm     S1Norm    SqNorm   GBORTHsat  Bproj
   6  18     3 1.05e-02 1.15e+00  7.50e-01  9.87e-01  1.13e-01    0.97542 1.57e-01
   8  24     4 1.72e-02 1.09e+00  6.47e-01  1.11e+00  1.62e-01    0.98379 1.27e-01
  10  28     3 3.87e-02 1.52e+00  5.38e-01  8.62e-01  1.21e-01    0.99146 9.24e-02
  12  32     4 2.56e-02 2.07e+00  6.04e-01  1.04e+00  1.35e-01    0.99605 6.29e-02
  14  36     4 1.17e-02 1.01e+00  3.26e-01  6.35e-01  7.42e-02    0.99658 5.85e-02
```

This is not a proof of the limiting estimates, but it verifies that the current finite certificate is
well-formed and numerically non-vacuous.

## 4. Current mathematical endpoint

Phase 72 is now reduced to proving:

```text
C-FIN,
N-FIN,
S-FIN.
```

These are:

```text
one physical-tail quadratic ratio,
three scalar norm bounds,
one Gram determinant saturation.
```

Every term is finite and explicitly computable from CCM/Loewner-Feshbach data and the post-main
Chebyshev discrepancy.  No absolute HPAC background, root-current subtraction, or limiting zeta zero is
hidden in the statement.

E72.120 gives a simpler sufficient replacement for `C-FIN`:

```text
CGE:
Graph_x(s)=||Dg_{x,s}||^2/||g_{x,s}||^2=O_K(1).
```

Since `CCGD_x(H,s)<=H^(-2)Graph_x(s)`, the final checklist may equivalently be attacked as:

```text
CGE,
N-FIN,
S-FIN.
```

## 5. Status

```text
proved: C-FIN + N-FIN + S-FIN imply scalar WRL annihilation;
achieved: single finite checklist for the current Phase 72 endpoint;
open:   prove the three limiting estimates uniformly.
```
