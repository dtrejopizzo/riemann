# D.36 — Poisson-lift divisibility audit

## 1. Purpose

D.35 isolates a valid non-circular sign mechanism: a Poisson lift whose
range lies in a support projection turns the desired form into the negative
of a Hilbert--Schmidt norm.  This note tests the most direct candidate for
that lift and proves that it cannot cover the full primitive test space.

## 2. The semilocal summation multiplier

For a finite set of places `S` containing infinity, let `M_S` be the
positive integers prime to the finite primes in `S`, and define formally

\[
 E_S(f)(x)=|x|^{1/2}\sum_{m\in M_S}f(mx).              \tag{2.1}
\]

On the critical Mellin line, whenever both sides are initially absolutely
convergent and then by continuation on the Bruhat--Schwartz domain,

\[
 \mathcal M(E_Sf)(\tau)
 =L_S(\tau)\mathcal M f(\tau),                       \tag{2.2}
\]

where

\[
 L_S(\tau)=\zeta(1/2-i\tau)
     \prod_{p\in S\setminus\{\infty\}}
       (1-p^{-1/2+i\tau}).                           \tag{2.3}
\]

### Proof

The change of variables `y=mx` gives a factor `m^(-1/2+i tau)` in the
Mellin transform.  Summing over integers prime to the finite primes of `S`
gives

\[
 \sum_{m\in M_S}m^{-1/2+i\tau}
 =\zeta(1/2-i\tau)
   \prod_{p\in S\setminus\{\infty\}}
      (1-p^{-1/2+i\tau}),
\]

with the sign of `tau` fixed by the Mellin convention.  This is (2.2).

## 3. Direct surjectivity is impossible

Suppose the lift in D.35 were obtained by solving

\[
 E_S(f_F)=F                                             \tag{3.1}
\]

in the central Mellin representation for every primitive compactly
supported `F`.  Then (2.2) forces

\[
 \mathcal M f_F(\tau)=
       \frac{\widehat F(\tau)}{L_S(\tau)}.             \tag{3.2}
\]

The two primitive equations only give

\[
 \widehat F(i/2)=\widehat F(-i/2)=0.                  \tag{3.3}
\]

They impose no vanishing at the nontrivial zeros of the factor in (2.3).
For any fixed nontrivial zero `rho=1/2-i tau_rho`, evaluation
`F -> widehat F(tau_rho)` is a nonzero continuous functional on
`C_c^infinity`; its restriction to the codimension-two space (3.3) is not
identically zero.  Indeed, three sufficiently small translates of one bump
give three independent exponential evaluations, so two linear moment
conditions can be imposed while leaving the third evaluation nonzero.

Choose such an `F`.  Then (3.2) has a pole at `tau_rho` and cannot be the
Mellin transform of a Bruhat--Schwartz or compact-potential vector.  Hence
the direct summation map `E_S` is not surjective onto the primitive test
space.

This argument does not depend on whether `tau_rho` is real.  Even if all
zeros were on the critical line, a generic primitive test would not vanish
at them.

## 4. Consequence for the compression route

The operator in D.35 cannot be defined by simply dividing every primitive
test section by `L_S`.  Such a construction would either:

1. exclude precisely the tests which detect the spectral cokernel;
2. introduce meromorphic vectors outside the Hilbert domain; or
3. choose a regularized inverse whose residues already depend on the zero
   divisor.

All three options fail the required comparison contract.

The correct Poisson object must therefore retain both the range and the
cokernel of `E_S`.  The range supplies the positive compression identity;
the cokernel is exactly where the global spectral contribution lives.
Turning that cokernel into a positive Hilbert module with self-adjoint
scaling, while preserving the row-C trace, is not automatic: off-line
spectral parameters would produce nonunitary characters.  Proving that the
cokernel admits the required polarized Hilbert realization is another
form of the row-D Hodge theorem, not a construction available before it.

## 5. Surviving use of Poisson duality

The audit does not discard Poisson duality.  It shows the correct role it
can play:

* construct the support/range summand and its negative-square identity;
* identify the two Tate boundary maps without choices;
* compare the remaining quotient with the mixed cohomology of A--C;
* prove a new polarization theorem on that quotient independently of its
  spectrum.

Thus the next viable construction is a polarized **range--cokernel
triangle**, not a global right inverse of `E_S`.

