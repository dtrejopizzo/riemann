# E72.315 -- Mesh sine-product reduction of SQB

**Purpose.** Split the sine-quotient bound `SQB` of E72.314 into a standard Fourier-mesh product
estimate and a genuine numerator estimate.

The conclusion is that the denominator is not the hard part.

## 1. Mesh notation

Let the finite pole-even mesh be

```text
d_m=2pi m/L,        |m|<=M_L,
```

and set the corresponding `z`-mesh

```text
z_m=-i d_m=-2pi i m/L.
```

The Cauchy denominator in the shifted variable is, up to a harmless power of `i`,

```text
D_x(iz)=prod_{|m|<=M_L}(z-z_m).
```

The endpoint factor has the same zero lattice:

```text
1-e^(zL)=0  iff  z=2pi i n/L.
```

Since the mesh is symmetric in `m`, this is the same lattice.

## 2. Canonical normalization

Define the normalized finite mesh quotient

```text
S_L(z)
:= (1-e^(zL)) / [ -L prod_{0<|m|<=M_L}(1-z/z_m) ].
```

The factor `-L` is chosen so that the zero at `z=0` is normalized correctly:

```text
1-e^(zL)=-Lz+O(z^2).
```

Using the canonical product for `sinh`,

```text
1-e^(zL)
= -Lz e^(zL/2) prod_{n>=1}(1+z^2L^2/(4pi^2 n^2)),
```

one gets

```text
S_L(z)
= e^(zL/2)
   prod_{n>M_L}(1+z^2L^2/(4pi^2 n^2)).                    (1)
```

This is an exact identity after the chosen finite normalization.

## 3. Compact strip bound

Fix `sigma,H` and assume the mesh cutoff satisfies

```text
M_L >= c_H L
```

so that the finite mesh covers the physical compact height window. For

```text
|Re z|<=sigma,        |Im z|<=H,
```

the tail product in (1) obeys

```text
prod_{n>M_L}|1+z^2L^2/(4pi^2 n^2)|
<= C_{sigma,H}.
```

Indeed,

```text
sum_{n>M_L} |z|^2 L^2/n^2 <= C_{sigma,H} L^2/M_L <= C_{sigma,H}L,
```

and under the physical scaling `M_L comparable to L^2` this is uniformly bounded; under the weaker
scaling `M_L comparable to L` it contributes at worst `exp(C_{sigma,H}L)`.

Thus the denominator half of `SQB` is completely explicit:

```text
(1-e^(zL))/D_x(iz)
= known sine quotient * known normalization.                (2)
```

No zeta arithmetic is hidden in (2).

## 4. Reduced numerator target

Write

```text
C_x(iz)=P_x(iz)/D_x(iz).
```

Then

```text
(1-e^(zL))C_x(iz)
= P_x(iz) * (1-e^(zL))/D_x(iz).                            (3)
```

After applying the explicit product estimate (2), `SQB` reduces to a numerator growth theorem:

```text
NUM-GROW:
|P_x(iz)| <= A_{sigma,H} L^B |D_x(iz)/(1-e^(zL))|
```

or, in normalized product coordinates,

```text
|normalized P_x(iz)| <= A_{sigma,H} L^B.
```

This is the only nonstandard part of `SQB`.

## 5. The next theorem is numerator control

The finite numerator is

```text
P_x(w)=sum_m xi_m prod_{n != m}(w-d_n).
```

Equivalently, after dividing by the mesh denominator,

```text
C_x(w)=sum_m xi_m/(w-d_m).
```

So `NUM-GROW` is a statement about the residues `xi_m`: the actual CCM ground vector must be
regular enough that its Cauchy transform, multiplied by the exact sine zero factor, has only
polynomial growth in fixed shifted strips.

This is the correct analytic object. It is not a statement about eigenvalues of a finite matrix.

## 6. Status

```text
proved: the endpoint factor is the canonical sine product for the Fourier mesh;
reduced: SQB to a numerator growth bound after explicit mesh normalization;
open:   prove NUM-GROW from the pole-even CCM ground-vector equation.
```

The next step is to use the finite eigenvector equation for `xi` to prove regularity of its Cauchy
transform.
