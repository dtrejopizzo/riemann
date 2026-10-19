# P123.009 — local excess Lefschetz--Riemann--Roch

## Status

`PROVED-IN-REPOSITORY` on the algebraic Bruhat--Schwartz kernel core for
every nonidentity rational dilation.

The theorem constructs the derived diagonal-contact complex at one local
stratum, its based determinant line, the half-density correction, the local
Lefschetz number, dagger symmetry and cyclicity on the declared domain.

`OPEN` at the identity dilation and for infinite sums.  The former is the
renormalized generic-orbit term of the imported semilocal theorem; the
latter is a summability problem for row C.  No arithmetic family or
von Mangoldt weight occurs below.

## 1. Graph against diagonal

Fix a place `v` and a rational `q>0`, `q!=1`, viewed in `Q_v^times`.  On the
additive local transverse space

```text
Q_v
```

consider the graph of `x -> q^-1 x` and the diagonal.  Their intersection
is the origin.  At a place `v`, the normal comparison is the one-dimensional
map

```text
d_(v,q):N_v -> N_v,
d_(v,q)=1-q^-1.                                      (1.1)
```

Define the two-term excess complex

```text
C_(v,q)=[N_v --(1-q^-1)--> N_v].                     (1.2)
```

It is acyclic because `q!=1`.  Its determinant is initially a based
one-dimensional `Q_v`-line.  Apply the standard absolute-value realization
of a based local line, sending a scalar `a` to the positive real norm
`|a|_v`.  The inverse realized determinant line has a canonical torsion
basis `s_(v,q)` with norm

```text
||s_(v,q)||=|1-q^-1|_v^(-1).                         (1.3)
```

This is an actual determinant of a perfect acyclic local complex.  The
inverse appears because a fixed-point formula uses the inverse Euler class
of the normal complex.

## 2. Half-density line

The unitary scaling operator of P123.006 is

```text
(V_q xi)(x)=|q|_v^(-1/2)xi(q^-1 x).
```

Let `H_(v,q)` be the based real half-density line with distinguished basis
of norm `|q|_v^(-1/2)`.  Define the local Lefschetz line

```text
L_(v,q)^Lef=H_(v,q) tensor E_(v,q).                  (2.1)
```

Its distinguished basis has norm

```text
a_v(q)=|q|_v^(-1/2)/|1-q^-1|_v
      =|q|_v^(1/2)/|q-1|_v.                          (2.2)
```

## 3. Local RR equality

For `f in S(Q_v)`, the kernel of `M_f V_q` is

```text
k_(f,q)(x,y)=f(x)|q|_v^(-1/2) delta(y-q^-1 x).
```

### Theorem 3.1 — local excess Lefschetz--RR

The distributional diagonal trace is the coefficient of the canonical
basis of (2.1):

```text
Tr_dist,v(M_f V_q)=f(0)a_v(q)
                  =f(0)|q|_v^(-1/2)/|1-q^-1|_v.      (3.1)
```

### Proof

Pulling the kernel to the diagonal gives

```text
f(x)|q|_v^(-1/2)delta((1-q^-1)x).
```

At every local field, scaling of Haar delta gives

```text
delta((1-q^-1)x)=|1-q^-1|_v^(-1)delta(x).             (3.2)
```

Evaluation at the unique fixed point yields (3.1).  Equations
(1.3)--(2.2) identify the same scalar as the torsion basis of the
half-density-corrected inverse excess determinant.  QED.

This proves an equality between a diagonal kernel trace and a determinant
of its derived normal contact.  It is not a declaration that their two
previously computed numbers are “intersection” by definition.

## 4. Dagger and cyclicity

Equation (2.2) is invariant under inversion:

```text
a_v(q^-1)=a_v(q).                                    (4.1)
```

Indeed `|1-q|_v=|q|_v|1-q^-1|_v`.  Together with
`(fU_q)^dagger=alpha_(q^-1)(conjugate(f))U_(q^-1)` and
`alpha_(q^-1)(f)(0)=f(0)`, this gives

```text
Tr_dist,v(K^dagger)=conjugate(Tr_dist,v(K)).          (4.2)
```

For algebraic kernels `fU_q,gU_r` with `qr!=1`, both cyclic products have
label `qr` and coefficient value `f(0)g(0)` at the fixed point.  Hence

```text
Tr_dist,v((fU_q)(gU_r))
 =Tr_dist,v((gU_r)(fU_q)).                            (4.3)
```

Linearity proves cyclicity for finite sums whenever the identity-label
coefficient vanishes in the products being traced.  Products with an
identity coefficient belong to the renormalized domain and are not
silently covered by this theorem.

## 5. Local products are not semilocal sums

If `v` is a finite place with

```text
|q|_v=|1-q|_v=1,
```

then the raw local factor in (2.2) is one.  Tensoring raw local excess lines
therefore has an eventually unit-norm restricted product.

This product statement must not be confused with the semilocal trace
formula.  A trace on the quotient by `S`-units is a **sum** of local-stratum
Lefschetz numbers, not the fixed-point determinant of the Cartesian product
of all transverse fields.  Its determinant is obtained by exponentiating
that sum, as in P123.012, rather than by identifying the sum with the
product of the raw numbers `a_v(q)`.  Compact-support stabilization belongs
to the semilocal test `h`, not to an isolated delta label `q`.

## 6. Relation with the Tate realization

P123.008 retains two formal tangent characters for an internal rational
gauge label,

```text
D_q=diag(q^(-1/2),q^(1/2))
```

and its Rosati operation sends `q` to `q^-1`.  The line `H_(v,q)` has the
same algebraic half-density normalization for a local external scaling.
P123.013 shows that these labels are not the same arrow on the quotient;
the comparison here is of the normal representation only.  The complex
(1.2) is the local derived excess omitted by ordinary coefficient base
change.

Thus the bridge has three source-defined layers:

```text
kernel fU_q
  -> Tate fiber D_q
  -> normal excess [N --(1-q^-1)--> N]
  -> determinant Lefschetz number f(0)a_S(q).
```

No contact mass has been appended to the label.

## 7. What is now closed, and what is not

For finite off-identity mixed kernels, A now has a genuine local RR package:

1. graph composition and dagger in P123.006;
2. a two-character internal Tate coefficient model in P123.008;
3. a perfect derived diagonal-contact complex;
4. determinant compatibility with the diagonal distribution;
5. cyclicity and dagger reality on each local stratum.

The full A.8 gate remains open for exactly two reasons:

```text
q=1:       nonproper fixed locus -> generic-orbit renormalization;
infinite F: determinant tensor product -> summability/completion.
```

The first is treated by the relative trace-class determinant of P123.012.
The second is deliberately assigned to the A/C summability boundary.
Consequently this note supplies the local geometric excess input without
claiming that a product of local torsion lines is already the semilocal
trace determinant.
