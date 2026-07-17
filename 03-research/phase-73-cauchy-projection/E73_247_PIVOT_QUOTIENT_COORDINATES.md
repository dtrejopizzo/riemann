# E73.247 - Physical pivot coordinates for the quotient defect

## 1. Why E73.246 is not yet enough

E73.246 showed that the quotient defect packet

```text
D_Q =
[
  delta_{gamma_1,0}
  delta_{gamma_1,1}
  delta_{gamma_2,0}
  delta_{gamma_2,1}
]
```

has stable rank `4` in the trusted windows.  An SVD basis proves that a finite
coordinate chart exists, but it is not yet a symbolic object.

The next step is to replace the SVD chart by physical coordinates on the
Fourier grid.

## 2. Pivot coordinate identity

Let `J` be a pivot set of four frequency indices such that the square matrix

```text
D_J = D_Q[:,J]
```

is invertible.  Then for any vector `xi`,

```text
D_Q xi = D_J z_J
```

where

```text
z_J = D_J^{-1}D_Q xi.
```

Splitting `xi=(xi_J,xi_R)` gives the explicit coordinate formula

```text
z_J = xi_J + T_J xi_R,
T_J = D_J^{-1}D_Q[:,R].
```

Thus the quotient divisibility statement is equivalent to:

```text
PIV-QUOT-DIV:
z_J(L,w)=O_M(L^-M)
```

provided `D_J` has only polynomially bad condition number.

## 3. Why this is different from the forbidden rowspace route

E72.352 showed that adding arbitrary rows from `Row(E)` is defect-invariant and
cannot repair the scalar obstruction.  Here we do not add such rows.

The construction is:

```text
1. form the fixed DD-local quotient defect delta_a;
2. stack the quotient rows D_Q;
3. choose physical columns J of D_Q;
4. rewrite the existing pairing through those columns.
```

The object to prove small is the physical quotient coordinate:

```text
z_J = xi_J + T_J xi_R.
```

This is an algebraizable cancellation statement in the actual finite CCM data,
not an ambient rowspace projection.

## 4. Current analytic target

The next symbolic theorem should identify the pivot set `J(L,w)` and prove:

```text
1. det D_Q[:,J] is nonzero with polynomial lower bound;
2. ||D_Q[:,J]^{-1}D_Q[:,R]|| grows at most polynomially;
3. xi_J + D_Q[:,J]^{-1}D_Q[:,R] xi_R = O_M(L^-M).
```

This is the strongest concrete version so far of the finite scalar
resonance-annihilation statement.

## 5. Status

```text
proved algebraically:
  CURV-QUOT-DIV <=> PIV-QUOT-DIV when D_Q[:,J] is invertible with polynomial
  condition.

observed:
  column-pivoted QR produces physical pivot sets with moderate condition
  exponents and rapidly small z_J in the tested windows.

open:
  symbolic pivot selection and proof of z_J cancellation.
```
