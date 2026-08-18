# E94.003 - Polynomial two-generator numerator

## 1. Cauchy transforms

For the adjugate generators of E94.002, set

```text
U_z=sum_j U_j/(z-d_j),
V_z=sum_j V_j/(z-d_j).                                (1.1)
```

Since `q_j=d_j-d_b`, E94.001 becomes

```text
N(z)=C-sum_j A_j/(z-d_j).                            (1.2)
```

Multiply (1.2) by `Delta` and use E94.002(3.2).

### Theorem 1.1

The projectively equivalent numerator

```text
P(z)=Delta N(z)                                      (1.3)
```

satisfies

```text
P(z)
 =Delta C+(2/L)[C U_z+T V_z],                        (1.4)

P'(z)
 =(2/L)[C U'_z+T V'_z].                              (1.5)
```

### Proof

Equation (3.2) of E94.002 gives

```text
-sum_j Delta A_j/(z-d_j)
 =(2/L)[C U_z+T V_z],                                (1.6)
```

which proves (1.4).  Differentiate (1.4); all coefficients are independent
of `z`, proving (1.5). `QED`

## 2. Exact logarithmic quotient

Where `P(z)` is nonzero,

```text
P'(z)/P(z)
 ={(2/L)[C U'_z+T V'_z]}
  /{Delta C+(2/L)[C U_z+T V_z]}.                     (2.1)
```

This is the polynomial version of the coupled two-generator quotient.  It
retains numerator and denominator together and is meaningful in every
projective chart in which their common cofactor scale has been removed.

## 3. Singular sections

If `Delta=0`, both sides of `P=Delta N` can vanish.  The canonical endpoint
object is the first nonzero coefficient in their common parameter expansion,
or equivalently the projective class of the coefficient vector in (1.4).
No division by `Delta` is permitted at such a section.

## 4. Status

```text
proved:
  exact polynomial two-generator numerator;
  exact inverse-free logarithmic quotient;
  projective prescription at singular sections.
```

