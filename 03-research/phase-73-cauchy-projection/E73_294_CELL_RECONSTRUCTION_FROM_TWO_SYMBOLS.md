# E73.294 - Cell reconstruction from the two-symbol form

Date: 2026-07-16.

## 1. Purpose

E73.293 left the endpoint in the two-symbol Loewner form:

```text
q[ M_{W^even}-(1/(iL))Lambda_{W^odd}^{full} ]R_wxi_L=O_M(L^(-M)).
```

This note proves that the two-symbol operator is exactly the original finite
CCM cell operator `Q_y` before the Gamma-prime functional is applied.  Thus the
two-symbol normal form is not a new shortcut; it is the closed-weight
reconstruction of `CELL-CTM`.

## 2. Pointwise symbol identity

For a fixed `y`, define

```text
W_y^even(d)=e^(idy)+e^(-idy)=2cos(dy),
W_y^odd(d)=e^(idy)-e^(-idy)=2i sin(dy).
```

Let `D=diag(d_j)` and define the full Loewner matrix

```text
Lambda_y(j,b)=
  (W_y^odd(d_j)-W_y^odd(d_b))/(d_j-d_b),   j != b,
  d/dd W_y^odd(d)|_{d=d_j},                j=b.
```

Then

```text
M_{W_y^even}-(1/(iL))Lambda_y = Q_y.        (CELL-2SYM)
```

Here `Q_y` is the CCM cell matrix:

```text
Q_y(j,j)=2(1-y/L)cos(d_jy),

Q_y(j,b)=(sin(d_jy)-sin(d_by))/(pi(n_b-n_j)),  j != b,
```

with `d_j=2*pi*n_j/L`.

## 3. Proof

On the diagonal,

```text
Lambda_y(j,j)=d/dd(2i sin(dy))|_{d=d_j}
             =2iy cos(d_jy).
```

Therefore

```text
2cos(d_jy)-(1/(iL))2iycos(d_jy)
=2(1-y/L)cos(d_jy)
=Q_y(j,j).
```

Off the diagonal,

```text
Lambda_y(j,b)
=2i(sin(d_jy)-sin(d_by))/(d_j-d_b).
```

Since

```text
d_j-d_b=2*pi(n_j-n_b)/L,
```

we get

```text
-(1/(iL))Lambda_y(j,b)
=-(1/(iL)) * 2i(sin(d_jy)-sin(d_by))/(d_j-d_b)
=(sin(d_jy)-sin(d_by))/(pi(n_b-n_j))
=Q_y(j,b).
```

This proves `CELL-2SYM`.

## 4. Applying the Gamma-prime functional

The closed weights are exactly the Gamma-prime functional applied to the
frequency symbols:

```text
W^even_j = F_L[W_y^even(d_j)],
W^odd_j  = F_L[W_y^odd(d_j)].
```

Linearity gives

```text
M_{W^even}-(1/(iL))Lambda_{W^odd}^{full}
= F_L[Q_y]
= H_L.                                          (H-2SYM)
```

Modulo the constant gauge already isolated in E73.287--E73.291, pairing with
`eta=R_wxi_L` gives

```text
q[ M_{W^even}-(1/(iL))Lambda_{W^odd}^{full} ]eta
= qH_Leta.
```

Thus the two-symbol theorem is exactly `CELL-CTM`:

```text
F_L[y -> qQ_yR_wxi_L]=O_M(L^(-M)).
```

## 5. Numerical certification

`E73_294_cell_reconstruction_probe.py` checks `CELL-2SYM` pointwise for
several values of `y/L`, `lambda`, and Cauchy rows.

Representative output:

```text
 lam     L gamma row y/L opRel rowRel
  12   4.970   14.13   0  0.17 3.0e-16 4.2e-16
  16   5.545   21.02   1  0.83 1.1e-15 1.2e-15
  20   5.991   21.02   0  1.00 2.3e-15 2.2e-15
```

The identity is pointwise algebraic; the numerical probe only catches sign and
normalization errors.

## 6. Consequence

The endpoint has now been fully unified:

```text
two-symbol Loewner form
= finite CCM cell form
= closed frequency-weight form
= Schur-commutator row
= master scalar S_{a,w,L}.
```

Therefore no further algebraic reformulation of the kernel is expected to
create cancellation by itself.  The remaining theorem is exactly:

```text
Directional Cell Eigenline Cancellation:
F_L[y -> q_aQ_yR_wxi_L]=O_M(L^(-M)).
```

Equivalently:

```text
q_a[H_L,P_w]xi_L=O_M(L^(-M)).
```

This is the irreducible finite identity at the current endpoint.

## 7. Program audit

Older Phase 72 work already had cell and Loewner commutator identities.  The
new contribution here is not another commutator estimate; it is the exact
identification:

```text
closed two-symbol weights reconstruct Q_y pointwise.
```

This rules out the false one-symbol Loewner route of E73.293 and confirms that
the only remaining difficulty is the signed Gamma-prime/eigenline pairing, not
an unaccounted algebraic term.

## 8. Status

```text
proved: pointwise CELL-2SYM identity;
proved: two-symbol normal form equals CELL-CTM after applying F_L;
verified: signs/factors numerically at roundoff;
open: prove Directional Cell Eigenline Cancellation uniformly.
```
