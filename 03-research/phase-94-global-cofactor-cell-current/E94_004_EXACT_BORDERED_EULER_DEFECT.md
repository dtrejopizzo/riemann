# E94.004 - Exact bordered Euler defect

## 1. Complete finite current

Let `A_(L,N)(s)` denote the explicit hyperbolic, moving-boundary and external
mesh factor in E81.002.  With `u=s-1/2`, define

```text
J_(L,N)(s)
 =partial_s log A_(L,N)(s)
  +i P'_(L,N)(iu)/P_(L,N)(iu)
  -i P'_(L,N)(-iu)/P_(L,N)(-iu).                     (1.1)
```

Because `P=Delta N` and `Delta` is independent of `z`, equation (1.1) is
exactly

```text
partial_s log C_(L,N)(s).                             (1.2)
```

## 2. Independent Euler current

The independent finite product satisfies

```text
partial_s log E_L(s)=H_L(s).                         (2.1)
```

Therefore the direct bordered defect is

```text
D_(L,N)(s)=J_(L,N)(s)-H_L(s).                        (2.2)
```

Substitution of E94.003(2.1) gives a completely explicit cofactor formula for
`D_(L,N)` involving only

```text
Delta,
C,
T,
U_z,V_z,
U'_z,V'_z,
the explicit factor A_(L,N),
the independent current H_L.                         (2.3)
```

No inverse of the CCM block occurs.

## 3. Exact remaining theorem

The logarithmic form of `DIRECT-BORDERED-ANCHOR` is

```text
COFACTOR-CELL-ANCHOR:
D_(L_alpha,N_alpha)(s)->0                            (3.1)
```

locally uniformly on `Re s>1` along one resolved directed family, together
with one safe normalization.

By E80.003 and E93.002,

```text
COFACTOR-CELL-ANCHOR
 =>DIRECT-BORDERED-ANCHOR
 =>Omega7.                                            (3.2)
```

## 4. Separation of roles

The displacement identity has closed the algebraic conversion from the
bordered determinant to two cofactor generators.  It has not evaluated their
joint cofinal limit.  The force-bearing assertion is precisely the signed
cancellation in (3.1).

## 5. Status

```text
proved:
  exact cofactor formula for the complete finite defect;
  equivalence of its local vanishing with the direct logarithmic anchor;

open:
  COFACTOR-CELL-ANCHOR.
```

