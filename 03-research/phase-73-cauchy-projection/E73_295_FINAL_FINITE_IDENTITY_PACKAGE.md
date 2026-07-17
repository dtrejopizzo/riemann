# E73.295 - Final finite identity package

Date: 2026-07-16.

## 1. Purpose

E73.294 shows that the two-symbol closed-weight operator reconstructs the CCM
cell `Q_y` pointwise.  E73.259 gives the reduced-adjugate detector for the
same scalar theorem.  This note packages the current endpoint as one finite
identity, with all equivalent forms explicitly tied together.

This is not a proof of `Omega7`.  It is the finite algebraic form that any
proof must force.

## 2. Objects

Let

```text
H_L=F_L[Q_y],
H_L xi_L=mu_L xi_L,
Q=Q_w,
P=Q^*(QQ^*)^(-1)Q,
R=I-P,
q=q_a.
```

Define the principal row

```text
rho_{a,w}=qH_LR.
```

The master scalar is

```text
S_{a,w,L}=rho_{a,w}xi_L.
```

## 3. Equivalent finite forms

The endpoint has the following equivalent forms.

### Cell form

```text
S_{a,w,L}=F_L[y -> qQ_yRxi_L].
```

### Two-symbol form

Using E73.294,

```text
Q_y=M_{2cos(dy)}-(1/(iL))Lambda_{2i sin(dy)}^{full}.
```

Therefore

```text
S_{a,w,L}
=q[ M_{W^even}-(1/(iL))Lambda_{W^odd}^{full} ]Rxi_L.
```

### Schur-commutator form

Since `qR=0`,

```text
S_{a,w,L}=qH_LRxi_L=-q[H_L,P]xi_L.
```

### Reduced-adjugate form

Let

```text
E_L=H_L-mu_LI.
```

If `mu_L` is simple, the reduced adjugate satisfies

```text
Adj_red(E_L)=c_L xi_Lxi_L^*,
```

where

```text
c_L=prod_{lambda_j != mu_L}(lambda_j-mu_L).
```

Hence

```text
rho_{a,w}Adj_red(E_L)
=c_L(rho_{a,w}xi_L)xi_L^*.
```

Thus

```text
|S_{a,w,L}|
= ||rho_{a,w}Adj_red(E_L)|| / ||Adj_red(E_L)||.  (ADJ-NORM)
```

The phase-free finite identity to prove is:

```text
FINAL-ETA-ADJ:
||qH_L(I-P_w)Adj_red(H_L-mu_LI)||
<= A_M L^(-M)||Adj_red(H_L-mu_LI)||.
```

## 4. What is verified numerically

`E73_295_final_finite_identity_probe.py` compares:

```text
1. qH_LR_wxi_L;
2. -q[H_L,P_w]xi_L;
3. the closed-weight kernel pairing;
4. the normalized reduced-adjugate defect.
```

Representative output:

```text
 lam     L gamma row qHRB commB kernB adjB errCommB errKernB errAdjB
  12   4.970   14.13   0 -20.83 -20.81 -20.89 -20.83    -22.80    -22.34  -430.82
  16   5.545   21.02   0 -18.18 -18.18 -18.13 -18.18    -21.19    -19.61  -403.27
  20   5.991   21.02   0 -17.66 -17.66 -18.95 -17.66    -24.28    -17.61  -385.84
```

The commutator and adjugate columns match the master scalar at numerical
floor.  The closed-weight kernel column is less stable in double precision
because it evaluates a highly cancelled scalar through truncated closed
weight series and constant gauges.  The exact two-symbol/cell identity is
therefore certified separately by E73.294, where the vector identity is
pointwise and at roundoff.

## 5. Anti-tautology boundary

`FINAL-ETA-ADJ` is a detector, not a forcer.  It must not be proved by:

```text
1. constructing Adj_red from the known numerical xi_L and declaring the
   normalized defect small;
2. projecting rho into Row(E_L);
3. using Q_wxi_L as an already-small input;
4. taking row norms or absolute cell sums.
```

Those routes were rejected in E73.253--E73.266 and E73.277--E73.281.

The only admissible proof is an independent estimate from the explicit
Gamma-prime entries of `H_L`, equivalently from the signed cell packet

```text
y -> qQ_yR_wxi_L.
```

## 6. Current endpoint

The Phase 72/73 scalar WRL gate is now reduced to the finite identity:

```text
For every admissible row/window and every M,

||qH_L(I-P_w)Adj_red(H_L-mu_LI)||
<= A_M L^(-M)||Adj_red(H_L-mu_LI)||.
```

Equivalently:

```text
F_L[y -> qQ_yR_wxi_L]=O_M(L^(-M)).
```

This is the cleanest finite algebraic formulation currently available.

## 7. Status

```text
proved: cell, two-symbol, commutator, and adjugate forms are equivalent;
verified: commutator and adjugate identities numerically;
verified separately: two-symbol cell reconstruction at roundoff;
open: prove FINAL-ETA-ADJ / Directional Cell Eigenline Cancellation from
      explicit Gamma-prime entries.
```
