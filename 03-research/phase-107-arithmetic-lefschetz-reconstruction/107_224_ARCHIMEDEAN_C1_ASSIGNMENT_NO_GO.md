# 107.224 -- The archimedean divisor cannot be stored in an integral Chern class

## 1. Additivity requirement

The Arakelov divisor group contains the direct summand

\[
 \mathbb R\{\infty\}.
\]

Any line-bundle realization compatible with tensor product must induce
an additive first-Chern-class map

\[
 c_1:\mathbb R\{\infty\}
 \longrightarrow H^2(X,\mathbb Z).
 \tag{1.1}
\]

For the periodic torus and its cellular model,
\(H^2(X,\mathbb Z)\cong\mathbb Z\).  More generally the same argument
applies to every finitely generated Neron--Severi target.

## 2. Divisibility no-go

### Theorem 2.1

Every group homomorphism from \((\mathbb R,+)\) to a finitely generated
abelian group is zero.

### Proof

The image of a divisible group is divisible.  A finitely generated
abelian group has no nonzero divisible subgroup: its free part has no
element divisible by every positive integer and its torsion part is
finite.  Hence the image is zero. \(\square\)

Consequently

\[
 c_1(a\{\infty\})=0
 \qquad\text{for every }a\in\mathbb R.
 \tag{2.1}
\]

This is not changed by passing from one torus to a finite product or to
the finite-rank Neron--Severi group of a proper arithmetic surface.

## 3. Conflict with integer RR variation

The published Connes--Consani dimensions vary along the same real
summand.  For example, with

\[
 D_a=a\{\infty\},\qquad n=\lfloor e^a\rfloor,
\]

one has

\[
 \dim H^0(D_a)=\lceil\log_3(2n+1)\rceil
\]

when \(a\ge0\), while \(H^1(D_a)\) has dimension zero.  Thus the Euler
dimension changes even though (2.1) forces the algebraic/topological
Chern class to remain fixed.

### Corollary 3.1

The archimedean contribution to a Phase 107 divisor cannot be encoded
additively in a finite-rank algebraic or topological Chern class.  Its
variation must reside in a metric, Green function, mass bound, or
tolerance relation.

This proves the load-bearing prediction of 107_00 Section 20 for the
real divisor direction, rather than merely treating it as a design
preference.

## 4. Scope

Finite-prime coefficients of an Arakelov divisor are integral and are
not killed by this theorem.  They may contribute algebraic vertical
classes.  The result only separates the archimedean real summand.

It also does not construct the required metric.  The next admissible
object is a metrized flat character complex whose tolerance radius or
Green datum depends on \(a\), and whose integer Euler dimension is the
CC formula.  Assigning an integer Chern number by rounding \(a\) is not
admissible because it breaks tensor-product additivity.

## 5. Falsifier

`107_224_archimedean_c1_assignment_no_go.py` evaluates the exact CC
dimension on fixed divisor radii and rejects both the raw dimension and
its zero-normalized version as additive maps to \(\mathbb Z\).  It also
checks finite divisibility constraints: any proposed image of
\(1\{\infty\}\) must be divisible by all tested integers, forcing zero
inside the fixed finite-rank lattice window.  The theorem supplies the
unbounded conclusion.

