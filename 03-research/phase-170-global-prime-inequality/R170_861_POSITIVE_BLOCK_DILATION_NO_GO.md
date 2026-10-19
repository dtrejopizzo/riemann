# R170_861 — Every positive dilation with physical Schur is pure congruence

> **Correction R170_862 (homogeneity).** The Schur classification of
> this record is correct. Proposal (6.3), however, cannot
> be interpreted as a uniform identity in `f`: its left-hand side is
> quadratic and `mathfrak W_K+Theta_ext` is linear in the contact vector.
> R170_862 proves that the residue must occupy a bordered mixed block. For
> positivity to force its vanishing, the boundary anchor must also
> belong to the kernel; that is an additional condition not yet constructed.

## 0. Result

R170_860 requires a two-dimensional self-adjoint family whose arithmetic leg
is not a congruence of the physical operator. The most natural construction
is to add an auxiliary space and place PC, the integer comb, or the
exterior port in the cross blocks. This record classifies that possibility.

Let

\[
 \mathbb H=
 \begin{pmatrix}A&D^*\\D&G\end{pmatrix},\qquad G>0,         \tag{0.1}
\]

and suppose that its Schur complement is exactly the physical operator

\[
 A-D^*G^{-1}D=H.                                           \tag{0.2}
\]

Then

\[
 \boxed{
 \mathbb H=
 \begin{pmatrix}I&D^*G^{-1}\\0&I\end{pmatrix}
 \begin{pmatrix}H&0\\0&G\end{pmatrix}
 \begin{pmatrix}I&0\\G^{-1}D&I\end{pmatrix}.}            \tag{0.3}

Therefore the extension is a triangular congruence of `H direct-sum G`.
Its kernel, its positivity, and every variation of the auxiliary blocks with
fixed Schur are pure transport. They cannot generate the second arithmetic
connection required in R170_860.

The conclusion is strong: a positive Hilbert extension can only have new
curvature if its Schur complement `S(r,q)` changes with the comb
scale. But then a new positivity law must be proved for `S(r,q)`; the
known minimality controls only `S(r,1)=H_r`. The sign problem is not solved by
adding the auxiliary space: it is transferred entirely to the Schur.

## 1. Exact factorization

Work first with bounded operators and `G>=g_0I>0`. Multiplying the
three factors of (0.3) gives

\[
 \begin{pmatrix}
 H+D^*G^{-1}D&D^*\\D&G
 \end{pmatrix}.                                            \tag{1.1}

By (0.2), `A=H+D^*G^{-1}D`, and (1.1) coincides with (0.1).
The triangular factors are adjoint and invertible. In particular,

\[
 \mathbb H\ge0\quad\Longleftrightarrow\quad H\ge0,         \tag{1.2}
\]

and

\[
 \boxed{
 \ker\mathbb H
 =\left\{\binom{f}{-G^{-1}Df}:f\in\ker H\right\}.}       \tag{1.3}

For closed forms the same proof holds under the usual hypotheses:
`G` has a bounded inverse on the auxiliary space, `D` is bounded relative
to the form norms, and the triangular factors preserve the domains.
(0.3) is not asserted outside those conditions.

## 2. Two-parameter family

Now let

\[
 \mathbb H(r,q)=
 \begin{pmatrix}A(r,q)&D(r,q)^*\\D(r,q)&G(r,q)\end{pmatrix},
 \qquad G(r,q)>0,                                          \tag{2.1}
\]

a `C1` family. Define

\[
 S(r,q)=A(r,q)-D(r,q)^*G(r,q)^{-1}D(r,q).                  \tag{2.2}

If

\[
 S(r,q)=H(r)                                                \tag{2.3}

in a neighborhood, factorization (0.3) depends smoothly on `(r,q)`
and trivializes the entire `q` direction. In particular:

* `mathbb H(r,q)>=0` if and only if `H(r)>=0`;
* the radical is the graph (1.3);
* varying the comb inside `D` or `G` only moves that graph;
* any connection computed from that graph changes by the triangular
  gauge and leaves invariant the defect `Theta_ext` of R170_859.

This class includes an exact completion of the square: placing a
PC expression in `D` and adding `D^*G^{-1}D` to block `A` keeps the physical
Schur, but identity (0.3) shows that no new energy appeared.

## 3. If the coupling switches off at the physical fiber

Another natural proposal requires

\[
 D(r,1)=0,\qquad A(r,1)=H(r).                               \tag{3.1}

Then, writing `u=q-1`,

\[
 D(r,q)=uD_1(r)+O(u^2),                                    \tag{3.2}

and

\[
 D(r,q)^*G(r,q)^{-1}D(r,q)
 =u^2D_1(r)^*G(r,1)^{-1}D_1(r)+O(u^3).                    \tag{3.3}

Therefore the auxiliary coupling does not contribute to the first
derivative in `q` nor to the mixed derivative `partial_r partial_q` at `q=1`. The
first-order antidiagonal curvature containing the Wronskian cannot
arise from a cross block that vanishes at the physical fiber.

To obtain a first-order contribution one must take `D(r,1) ne 0`.
If its Schur is compensated to preserve `H(r)`, one returns to (0.3). If it is not
compensated, the physical fiber is no longer `H(r)`.

## 4. Semidefinite auxiliary block

If `G>=0` has a kernel, positivity of `mathbb H` forces the range
condition

\[
 \operatorname{Ran}D\subseteq\operatorname{Ran}G^{1/2}.    \tag{4.1}

On the support of `G`, the generalized complement is

\[
 S=A-D^*G^\dagger D,                                      \tag{4.2}

with `G^dagger` the Moore--Penrose inverse. Under closed range and the
domain conditions, the same triangular elimination holds on that
support; the additional kernel of `G` decouples. It produces no
signed curvature between `r` and `q`.

Allowing (4.1) to fail destroys the positivity of the block. Allowing an
indefinite `G` preserves a symplectic or Krein orientation, but there is no
longer a Hilbert order to which minimality can be applied. This is the
dichotomy observed in the graded realization of R170_854.

## 5. Application to PC and to the integer comb

Consider any of the choices

\[
 D(r,q)\in\{E(r,q),\ H_{M,N}(r,q),\ S(q)A(r),\
              \mathcal C_{PC}(r,q)\}.                      \tag{5.1}

If (5.1) is placed in a positive matrix with lower block `G>0`, there are
two options:

1. add `D^*G^{-1}D` above so that the Schur remains `H(r)`;
   then (0.3) shows that the construction is pure congruence;
2. do not add it; then the physical Schur becomes
   `H(r)-D^*G^{-1}D`, a different form whose positivity is a new
   global inequality.

The second option contains Hermitian squares and is insensitive to the
linear orientation of `D`; moreover it generates the quotient products
already flagged by the comb-ratio no-go. It cannot be declared a repair of
Ward--PC without first proving its new Schur inequality.

The exact identity `Lambda*1=log` can simplify `D`, but it does not alter
factorization (0.3). Therefore exact arithmetic does not break this algebraic
no-go.

## 6. What class remains alive

A second non-congruent self-adjoint connection must make the Schur vary

\[
 S(r,q)=H(r)+\mathcal R(r,q),\qquad \mathcal R(r,1)=0,       \tag{6.1}

with

\[
 \partial_q\mathcal R(r,1)\ne0.                            \tag{6.2}

A first attempt would be to prove, using the exact integers, a
one-sided law for `mathcal R` compatible with positivity prior to
contact, and to relate

\[
 \langle f,\partial_q\mathcal R(1,1)f\rangle
 \quad\hbox{or its typed polarization}\quad
 =\mathfrak W_K(f)+\Theta_{\rm ext}(f).                    \tag{6.3}

The literal equality in (6.3) has the wrong homogeneity: the diagonal
is quadratic in `f`, while the exterior defect is linear. R170_862
replaces it with a mixed polarization against a boundary anchor.

But `mathcal R` cannot be `D^*G^{-1}D` with `D(r,1)=0`, by (3.3), nor
a conjugation/congruence, by R170_860 and §2. It must be a
linear, self-adjoint, and specifically arithmetic term that already includes the
ports of R170_856.

Equations (6.1)--(6.2) isolate the only class not excluded by this memo;
R170_862 gives the correctly homogeneous bordered specification.

## 7. Status

```text
triangular factorization (0.3)                            PROVED
positivity and kernel of the extension                     PROVED
fixed physical Schur implies pure-gauge q direction         PROVED
coupling D(r,1)=0 contributes a first q jet                REFUTED
semidefinite extension evades the factorization            NO, under closed range
indefinite extension preserves Hilbert minimality          FALSE
linear arithmetic deformation R(r,q) of the Schur           OPEN CLASS
diagonal (6.3) uniformly encodes the residue                REFUTED R170_862
exterior identity / VIR--LB / D                             OPEN
```
