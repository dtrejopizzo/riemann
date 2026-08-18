# E94.002 - Inverse-free boundary displacement polynomial

## 1. Cell identities

Let

```text
D=diag(d_j),
s=(S_L(d_j))_j,
q=D1-d_b1.                                           (1.1)
```

For the inner block and the raw boundary column, the rank-two displacement
law and its boundary entry are

```text
[D,M]=-(2/L)(s1^T-1s^T),                             (1.2)

(D-d_bI)b=-(2/L)(s-S_b1).                            (1.3)
```

The scalar shift in `M` commutes with `D`, so it does not change (1.2).

## 2. Cofactor variables

Use `Delta,y` from E94.001 and define

```text
C=Delta-1^Ty,
S=s^Ty,
A=(D-d_bI)y.                                         (2.1)
```

### Theorem 2.1

The residue vector `A` satisfies

```text
M A
 =-(2/L)[C s+(S-Delta S_b)1].                        (2.2)
```

### Proof

The adjugate identity gives

```text
My=Delta b.                                          (2.3)
```

Using `MD=DM-[D,M]`,

```text
M(D-d_bI)y
 =(D-d_bI)My-[D,M]y.                                 (2.4)
```

Insert (2.3), then (1.2)--(1.3):

```text
M A
 =-(2Delta/L)(s-S_b1)
  +(2/L)[s(1^Ty)-1(s^Ty)]

 =-(2/L)[(Delta-1^Ty)s+(S-Delta S_b)1].              (2.5)
```

This is (2.2). `QED`

## 3. Fully polynomial form

Define the adjugate generators

```text
U=adj(M)s,
V=adj(M)1,
T=S-Delta S_b.                                       (3.1)
```

Multiplication of (2.2) by `adj(M)` gives

```text
Delta A=-(2/L)(C U+T V).                             (3.2)
```

Equation (3.2) is valid even when `Delta=0`; it is an identity of cofactors.
For invertible `M`, division by `Delta^2` recovers the two-generator inverse
formula of P76.041 and E81.004.

## 4. Status

```text
proved:
  exact raw-boundary displacement identity;
  inverse-free two-generator equation;
  polynomial continuation through Delta=0.
```

