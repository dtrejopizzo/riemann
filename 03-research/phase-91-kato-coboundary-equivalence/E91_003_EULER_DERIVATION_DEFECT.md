# E91.003 - Euler gauge derivation defect

## 1. Gauge identity on a general vector

Let `Z` be the finite Euler unit, `M=Z^(-1)`, and `delta` the scale
derivation.  Put

```text
A=Z^(-1)delta Z.                                     (1.1)
```

For an arbitrary module vector `v`, let

```text
w=(Z-I)v.                                            (1.2)
```

The Leibniz rule gives

```text
Z^(-1)delta w
 =Av+(I-Z^(-1))delta v.                              (1.3)
```

Hence

```text
Av
 =Z^(-1)delta[(Z-I)v]
  -(I-Z^(-1))delta v.                                (1.4)
```

The second term is the Euler derivation defect.

### Proof

Expand

```text
delta[(Z-I)v]
 =(delta Z)v+(Z-I)delta v
```

and multiply by `Z^{-1}`. `QED`

## 2. Symmetric prime matrix

For `H_P=A+A^*`, applying (1.4) and its adjoint produces an explicit gauge
term plus the two derivation defects associated with `v`.  Therefore the
formal Euler identity yields an inverse-free candidate for
`QH_Pv` only after these defects are retained.

If `delta v=0`, the first defect vanishes.  This is exactly the hypothesis
used by the algebraic ground-vector identity of E83.001.

## 3. Physical obstruction

In the interval representation, `delta` is multiplication by the position
operator `X`.  Its kernel in `L^2(0,L)` is trivial:

```text
Xv=0 and v in L^2(0,L) imply v=0.                    (3.1)
```

Thus a nonzero physical resonant vector cannot satisfy `delta v=0`.  The
distributional endpoint mass does satisfy `X delta_0=0`, which explains why
the endpoint module closes the algebraic source construction but does not
automatically integrate the physical resonant line.

## 4. Status

```text
proved:
  exact Euler derivation defect;
  impossibility of eliminating it by a nonzero physical ground vector;

closed as a route:
  direct integration of the resonant line by the ground-vector gauge identity;

open:
  safe reduced control of the derivation defect after the endpoint source is
  transported into the physical complement.
```

