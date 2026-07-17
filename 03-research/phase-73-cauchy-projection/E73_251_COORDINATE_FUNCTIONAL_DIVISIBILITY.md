# E73.251 - Coordinate functional divisibility

## 1. Purpose

E73.249--E73.250 separated the nondegeneracy side of the maximal-minor
coordinate route.  The remaining RH-strength statement is:

```text
MAXMIN-PIV-DIV:
z_{J_*}=O_M(L^-M).
```

This note opens `z_{J_*}` as explicit linear functionals on the spectral vector
`xi_L`.

## 2. Coordinate functionals

Let

```text
J_* in argmax_{|J|=4}|det D_Q[:,J]|
```

and write

```text
D_J = D_Q[:,J_*],        R = complement of J_*.
```

Then:

```text
z_{J_*}=D_J^{-1}D_Q xi_L.
```

Define the coordinate functional matrix:

```text
M_J := D_J^{-1}D_Q.
```

Then:

```text
z_j = m_j xi_L,
```

where `m_j` is the `j`-th row of `M_J`.

Equivalently:

```text
m_j = e_j on the pivot columns + transfer row on the remaining columns.
```

## 3. Rowspace certificate form

Since

```text
E xi_L = 0,       E=H_L-mu_L I,
```

one has:

```text
m_j xi_L = 0
```

whenever `m_j in Row(E)`.  Thus the divisibility target can be written as:

```text
COORD-ROW-DIV:
dist(m_j, Row(E)) = O_M(L^-M)
```

for the four coordinate functionals `m_j`.

This is an exact certificate form, not a proof by itself.  The rowspace
membership must be derived from the explicit DD-local quotient formula for
`D_Q`, not from a full pseudoinverse or an after-the-fact adjugate fit.

## 4. Why absolute estimates cannot close it

The audit computes:

```text
absCeil_j = sum_n |m_j(n) xi_L(n)|.
```

The ratio

```text
absCeil_j / |m_j xi_L|
```

has large polynomial exponent.  Therefore the smallness of `z_j` is a signed
spectral cancellation, not an absolute-value bound.

Endpoint moments also do not explain the cancellation: the raw moments

```text
sum_n m_j(n),       sum_n n m_j(n)
```

are not small enough to carry the observed divisibility.

## 5. New endpoint

The current finite route is:

```text
QROW-INDEP      => GRAM-NONDEG => MAXMIN-NONDEG,
COORD-ROW-DIV   => MAXMIN-PIV-DIV,
MAXMIN-NONDEG + MAXMIN-PIV-DIV => CURV-QUOT-DIV.
```

The hard statement is now:

```text
Derive COORD-ROW-DIV for M_J=D_J^{-1}D_Q from the DD-local quotient
construction.
```

That is the sharpened finite spectral Mellin divisibility problem.

## 6. Status

```text
proved algebraically:
  MAXMIN-PIV-DIV is equivalent to m_j xi_L=O_M(L^-M);
  m_j xi_L is controlled by rowspace distance to E.

observed:
  absolute ceilings are much larger than m_j xi_L;
  endpoint moments are not the cancellation source.

open:
  prove COORD-ROW-DIV structurally from the finite DD-local quotient formula.
```
