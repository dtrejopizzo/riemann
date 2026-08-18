# D.79 supplement — capacity with the positive complement retained

## Status

This note records an exact strengthening of the rank-one tail-capacity
test.  The usual estimate using the Gamma remainder alone discards the
positive spectral complement of the finite block.  Retaining that
complement gives the correct one-dimensional Schur capacity.

No sign of the Weil form is assumed.

## Lemma

Let `A_0` be self-adjoint and suppose it has exactly one negative
eigendirection:

\[
 A_0=\lambda |v\rangle\langle v|+A_+,
 \qquad \lambda<0,\quad \|v\|=1,
 \quad A_+\geq0,\quad A_+v=0.                           \tag{1}
\]

Let `R>=0`, put `B=A_++R`, and assume that `v` belongs to the form range
of `B^(1/2)` and

\[
 I_B:=\langle v,B^{-1}v\rangle<\infty                  \tag{2}
\]

in the quadratic-form (or Moore--Penrose) sense.  Then

\[
 \boxed{A_0+R\geq0\quad\hbox{if}\quad I_B^{-1}\geq-\lambda.}
                                                                  \tag{3}
\]

### Proof

Cauchy--Schwarz in the `B` form gives, for every `x`,

\[
 |\langle v,x\rangle|^2
 =|\langle B^{-1/2}v,B^{1/2}x\rangle|^2
 \leq I_B\langle x,Bx\rangle .                         \tag{4}
\]

Thus

\[
 B\geq I_B^{-1}|v\rangle\langle v|.                    \tag{5}
\]

Using `A_0+R=lambda |v><v|+B`, (5) proves (3).

## Why this is stronger than tail-only capacity

If `I_R=<v,R^{-1}v>` is finite, then `B=A_++R>=R` and inverse order gives

\[
 I_B\leq I_R,\qquad I_B^{-1}\geq I_R^{-1}.             \tag{6}
\]

The inequality is generally strict.  The positive gap of `A_+` suppresses
the directions into which `R` could otherwise move the negative vector.
Equivalently, `I_B^{-1}` is the exact Schur complement of `B` onto
`span(v)`, while `I_R^{-1}` is the Schur complement after the entire
positive finite block has been thrown away.

## Compression-safe version

Let `P` be a closed-subspace projection and let `B>0` on the ambient
space.  The shorted-operator inequality is

\[
 PBP\big|_{PH}\geq
 \left(PB^{-1}P\big|_{PH}\right)^{-1}.                 \tag{7}
\]

It follows from (4), first for one vector and then by polarization/duality.
Consequently an ambient inverse-form upper bound may be used to obtain a
valid lower capacity for the compressed problem.  This is the direction
needed in a full-space Feshbach certificate.

Moment penalties may be included in `A_+` because they vanish identically
on the exact primitive subspace.  They must not be used to replace the
primitive constraint outside that subspace.

The finite-dimensional identity and the strict improvement over the
tail-only capacity are checked in
`114_d_79_positive_complement_capacity_verify.py`.

