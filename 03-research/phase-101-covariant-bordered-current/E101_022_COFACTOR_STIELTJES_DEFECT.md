# E101.022 - Cofactor Stieltjes defect

## 1. Direct endpoint current

Let

```text
s=1/2+sigma,
x=sigma^2.                                           (1.1)
```

For the complete finite core bilateral characteristic, with the exact external
product of E101.025 removed, E94.004 defines

```text
D_(L,N)(s)
 =partial_s log C_(L,N)(s)-H_L(s),                   (1.2)
```

where `H_L=partial_s log E_L` is the independent finite Euler--Gamma current.

Define

```text
g_(L,N)(x)
 ={1/(2 sigma)}partial_s log C_(L,N)(s),             (1.3)

g_(E,L)(x)
 ={1/(2 sigma)}H_L(s).                               (1.4)
```

Then the exact Stieltjes defect is

```text
g_(L,N)(x)-g_(E,L)(x)
 =D_(L,N)(s)/(2 sigma).                              (1.5)
```

## 2. Independent limit

E80.002 gives, locally uniformly for `s>1`,

```text
g_(E,L)(x)->g_Xi(x).                                 (2.1)
```

Therefore

```text
COFACTOR-STIELTJES-IDENT:
D_(L_alpha,N_alpha)(1/2+sqrt(x))->0                 (2.2)
```

on any determining safe set is equivalent to `STIELTJES-IDENT` there.

## 3. Explicit cofactor formula

By E94.001--E94.004, the first term in (1.2) is

```text
partial_s log A_(L,N)(s)
 +i P_(L,N)'(i sigma)/P_(L,N)(i sigma)
 -i P_(L,N)'(-i sigma)/P_(L,N)(-i sigma).            (3.1)
```

Here `P` is the polynomial two-generator bordered numerator, and the explicit
factor `A_(L,N)` contains the exact hyperbolic and external-mesh corrections.
Thus every
term in (1.5) is a direct endpoint cofactor or an independent Euler--Gamma
quantity.  No deformation parameter, characteristic branch, level velocity,
shell split or inner inverse is required in the statement.

## 4. Relation to the covariant current

The covariant deformation of E101.005 is an exact proof coordinate for (1.5):
integrating its signed residual from the archimedean endpoint to the full
Gamma--prime endpoint recovers `D_(L,N)`.  It is not an additional hypothesis.

## 5. Status

```text
proved:
  exact cofactor Stieltjes defect;
  direct endpoint formulation of the discriminant;
  equivalence with the integrated covariant current;

open:
  COFACTOR-STIELTJES-IDENT on a determining safe set.
```
