# 114.a.146 — The RR scale is a polarization modulus

## 1. Setup

Let `D_pr` be the finite-support two-ruling prime lattice, with intrinsic
boundary degrees

\[
 d_i(x)=\sum_p x_{p,i}\log p.
\]

An admissible interpolation calibration `kappa` consists of all the data
needed to run the all-ray construction: its ordered exponent family, strict
prime window, least-admissible-prime convention, coordinate order and a
positive retained-coordinate coefficient `c_kappa`.  The construction then
gives

\[
 F_\kappa(x)=c_\kappa d_1(x)d_2(x),
\]

with polarized form

\[
 B_\kappa(x,y)=c_\kappa
 \bigl(d_1(x)d_2(y)+d_2(x)d_1(y)\bigr).
\]

The canonical contact form is

\[
 C_\Lambda(x,y)=\sum_p
 (x_{p,1}y_{p,2}+x_{p,2}y_{p,1})\log p,
\]

and `G_kappa=B_kappa-C_Lambda`.

## 2. Exact classification

### Theorem 2.1

Two calibrated RR biextensions are isometric by an isometry preserving the
distinguished generators if and only if their coefficients agree:

\[
 \mathcal E_{RR,\kappa}\simeq\mathcal E_{RR,\kappa'}
 \quad\Longleftrightarrow\quad c_\kappa=c_{\kappa'}.
\]

The same statement holds for the Green quotients after the canonical contact
factor is fixed.

### Proof

If the coefficients agree, the norm formulas agree on every pair, and the
generator-preserving identity is an isometry compatible with the
biextension laws.

Conversely, evaluate the logarithmic norm on `e_(p,1),e_(q,2)`.  A
generator-preserving isometry gives

\[
 c_\kappa\log p\log q=c_{\kappa'}\log p\log q.
\]

Since the logarithms are nonzero, the coefficients agree.  Subtracting the
same contact norm proves the Green statement.  QED.

### Corollary 2.2

The carrier, prime Cartier lattice, boundary degree and finite contact do
not determine the RR or Green scale.  The scale is a genuine one-dimensional
modulus.

This is stronger than observing that one proof used a convenient number.
The admissible families with exponents `beta^r`, `beta=3^j`, produce the
distinct values

\[
 c_\beta={1\over2\log\beta}.
\]

Therefore no theorem using only the already constructed carrier, degrees and
contact can call one of these biextensions canonical.

## 3. Mathematically complete reformulation

Define a **polarized row-A object** to be the pair

\[
 (\mathscr Y_A,\kappa),
\]

where `kappa` is an admissible calibration.  Its RR determinant limit,
contact determinant, Green quotient and real numerical RR space are then
fully determined.  Principal transport is by the canonical metric on global
fractions; the only residual global units are `+-1`, and the odd evaluation
exponents make the determinant norm independent of that transport.

For every `c_kappa>0`, the real numerical quotient is the hyperbolic plane
of `a145`, so the Hodge-index statement is independent of the modulus.

This closes the **polarized** construction without pretending the
polarization is supplied by the unpolarized square.  The stronger assertion
that the bare square carries a canonical RR/Green polarization remains a
separate existence/uniqueness problem.

## 4. Why Tate scalar rigidity does not remove the modulus

The Tate-style telescoping theorem available in the programme says that a
real-valued functional on the rational Witt ring which is Frobenius weight
one and stays at uniformly bounded distance from Mahler measure equals
Mahler measure.  Its proved corollary explicitly makes no assertion about a
Green function, diagonal regularization or intersection pairing.  It cannot
compare two coefficients in Theorem 2.1 and therefore cannot select
`c_kappa`.

