# E96.002 - Cellwise Jacobian expansion

## 1. Prime directions

The finite prime matrix is

```text
H_P
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)Q_(log n).                        (1.1)
```

Each full cell `Q_y` induces a bordered direction `B_y` in `P` and the
corresponding full direction in `chi`.  Let

```text
delta_y P,
delta_y chi                                           (1.2)
```

denote the directional derivatives obtained by adding that cell with positive
sign.

Since the deformation subtracts `tH_P`,

```text
partial_t P
 =-sum_n Lambda(n)n^(-1/2)delta_(log n)P,             (1.3)

partial_t chi
 =-sum_n Lambda(n)n^(-1/2)delta_(log n)chi.           (1.4)
```

## 2. Cell Jacobian

Define

```text
J_y(P,chi)
 =(delta_y P)(partial_mu chi)
  -(partial_mu P)(delta_y chi).                       (2.1)
```

Then the characteristic Jacobian of E95.002 has the exact expansion

```text
Jac(P,chi)
 =-sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)J_(log n)(P,chi).                 (2.2)
```

### Proof

Insert (1.3)--(1.4) into

```text
Jac(P,chi)
 =(partial_tP)(partial_mu chi)
  -(partial_muP)(partial_t chi)
```

and use linearity. `QED`

## 3. Significance

Equation (2.2) is an exact finite von Mangoldt expansion of the nonlinear
moving-level numerator.  The nonlinearity remains in the common determinant
data `P,chi`; it has not been distributed among separate prime systems.

## 4. Status

```text
proved:
  exact cellwise expansion of the characteristic Jacobian;
  preservation of the full moving-level coupling.
```

