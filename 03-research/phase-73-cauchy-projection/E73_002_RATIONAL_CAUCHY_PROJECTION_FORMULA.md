# E73.002 - Rational formula for the Cauchy projection

## 1. Purpose

E73.001 isolates the finite projection

```text
H_O=C_OO^(-1)C_OKG_K.
```

This note removes the matrix inverse.  The vector `H_O` is the residue vector of a finite rational
interpolant to the critical-line Cauchy packet

```text
Q_K(s):=sum_{k in K_L} G_K(k)/(s+k).
```

Thus `NAT-PROJ` is an explicit residue bound for a rational interpolation problem.

## 2. Interpolation equation

The projection equation is

```text
sum_{b in O_L} H_b/(a+b)
= sum_{k in K_L} G_K(k)/(a+k),
a in O_L.                                            (1)
```

Equivalently, with

```text
H(s):=sum_{b in O_L} H_b/(s+b),
Q_K(s):=sum_{k in K_L} G_K(k)/(s+k),
```

we have

```text
H(a)=Q_K(a),             a in O_L.                    (2)
```

The sign convention differs from E73.001 only by whether the projection is moved to the left or right
side of the nodal equation; `NAT-PROJ` uses the absolute size of the same vector.

## 3. Rational Lagrange formula

Let

```text
D_O(s):=prod_{b in O_L}(s+b).
```

Then

```text
H(s)=N(s)/D_O(s),
```

where `deg N < |O_L|`.  From (2),

```text
N(a)=Q_K(a)D_O(a),        a in O_L.                   (3)
```

Let

```text
ell_a(s):=prod_{c in O_L, c != a} (s-c)/(a-c)
```

be the ordinary polynomial Lagrange basis at the off-line nodes.  Then

```text
N(s)=sum_{a in O_L} Q_K(a)D_O(a) ell_a(s).            (4)
```

The residue at the pole `s=-b` is

```text
H_b=Res_{s=-b} H(s)
   = N(-b)/D_O'(-b).                                  (5)
```

Combining (4)--(5),

```text
H_b=
  1/D_O'(-b)
  sum_{a in O_L} Q_K(a)D_O(a) ell_a(-b).              (6)
```

This is the explicit finite formula for `C_OO^(-1)C_OKG_K`.

## 4. Kernel form

Since

```text
Q_K(a)=sum_{k in K_L} G_K(k)/(a+k),
```

we can write

```text
H_b=sum_{k in K_L} Pi(b,k)G_K(k),                     (7)
```

with the explicit kernel

```text
Pi(b,k):=
  1/D_O'(-b)
  sum_{a in O_L}
     D_O(a) ell_a(-b) /(a+k).                         (8)
```

Thus `NAT-PROJ` is:

```text
max_{b in O_L} e^(Re b L)
 |sum_{k in K_L} Pi(b,k)G_K(k)| <= L^B.               (9)
```

## 5. Residue interpretation

Define the rational interpolation error

```text
E(s):=Q_K(s)-H(s).
```

Then

```text
E(a)=0,        a in O_L,
```

and the off-line projection vector is exactly the negative residue data needed to cancel the poles of
the rational interpolant at `s=-O_L`.

Therefore the remaining problem is not generic linear algebra.  It is:

```text
the residues at -O_L of the rational interpolant of Q_K through O_L are exponentially small.
```

## 6. Status

```text
proved: C_OO^(-1)C_OKG_K has the explicit residue formula (6)--(8);
reduced: NAT-PROJ to exponential smallness of rational interpolation residues;
next: insert the divided-difference form of G_K into Pi(b,k).
```
