# Universal cutoff gate audit

## Purpose

The fixed-cutoff generating function would become much more useful if a
single finite cutoff \(T\) could replace all \(T_n\).  This document records
what the current A0 theorem can and cannot provide.

The conclusion is precise:

- the A0 theorem gives \(T_n\) after \(n\) is fixed;
- the A0 sufficient condition cannot give a finite universal cutoff for all
  \(n\);
- a universal cutoff route remains viable only if it proves a new signed
  theorem beyond A0.

## A0 cutoff condition

The A0 theorem assumes a PNT envelope
\[
  |\psi(e^u)-e^u|\le A e^u\exp(-\eta(u))
  \qquad(u\ge U_0),
\]
with \(\eta\) increasing and \(\eta(u)/\log(1+u)\to\infty\).

For each \(n\ge8\), it chooses \(T(n)\ge U_0\) so that, for all
\(u\ge T(n)\),
\[
  \eta(u)\ge
  (n+1)\log(1+u)
  +
  \log {12A n^2\over B_n},
\tag{1}
\]
where
\[
  0<B_n\le \lambda_n^{\rm arch}.
\]

Then
\[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T(n)}}^\infty
  (\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{\rm arch}.
\tag{2}
\]

## No universal cutoff from this A0 mechanism

Assume one tries to choose a single finite \(T_\ast\ge U_0\) satisfying
(1) for every \(n\ge8\).  Evaluating (1) at \(u=T_\ast\) would require
\[
  \eta(T_\ast)\ge
  (n+1)\log(1+T_\ast)
  +
  \log {12A n^2\over B_n}
  \qquad(n\ge8).
\tag{3}
\]

For any fixed \(T_\ast>0\), the term
\[
  (n+1)\log(1+T_\ast)
\]
is linear in \(n\), while \(\eta(T_\ast)\) is fixed.  In the phase-102
archimedean split one has only subexponential archimedean growth; in
particular admissible lower bounds \(B_n\le\lambda_n^{\rm arch}\) cannot
cancel this linear growth exponentially.  Thus (3) fails for all sufficiently
large \(n\).

Therefore the current A0 proof cannot supply a universal finite cutoff.
It is intrinsically an \(n\)-after-\(n\) tail theorem.

## What this does not prove

This is not a theorem that no universal signed cutoff can exist.  It proves
only that the existing A0 absolute-tail mechanism cannot provide one.

A different theorem could still prove, for a fixed \(T_\ast\),
\[
  K_n(T_\ast)+{3\over4}\lambda_n^{\rm arch}\ge0
  \qquad(n\ge8),
\tag{4}
\]
and then control the remaining tail by a signed argument.  But that would be
a new A1-level theorem, not a consequence of A0.

## Relation to the fixed-cutoff generating function

The fixed-cutoff function
\[
  \mathcal C_T(z)=
  \sum_{n\ge1}
  \left(K_n(T)+{3\over4}\lambda_n^{\rm arch}\right)z^n
\]
is an exact analytic object for each fixed \(T\).  If there were a single
A0-admissible \(T_\ast\) for all \(n\ge8\), coefficient positivity of
\(\mathcal C_{T_\ast}\) would be a natural compact route to A1.

But A0 supplies only \(T_n\).  Hence the actual A1 sequence
\[
  K_n(T_n)+{3\over4}\lambda_n^{\rm arch}
\]
is not the coefficient sequence of one fixed \(\mathcal C_T\).  A
coefficient-positivity proof must therefore add one of:

1. a new universal signed cutoff theorem;
2. uniform positivity of \(\mathcal C_T\) over all admissible \(T\);
3. a positive transform that encodes the moving sequence \(T_n\);
4. a one-sided tail theorem replacing the absolute A0 tail.

## Eliminated class

The following proof pattern is eliminated:

1. derive the fixed-cutoff generating function;
2. prove or conjecture positivity of its coefficients for a single finite
   \(T\);
3. infer A1 for the A0 cutoffs \(T_n\).

Step 3 is invalid unless the dependence on \(T_n\) is handled by one of the
four additional theorems above.

## Status

Closed as an audit of the universal-cutoff gate.  The fixed-cutoff route
remains viable only with a new signed theorem controlling the cutoff
dependence.
