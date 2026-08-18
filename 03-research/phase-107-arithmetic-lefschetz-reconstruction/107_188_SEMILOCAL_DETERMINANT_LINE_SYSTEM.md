# 107.188 -- A determinant-line system on the semilocal basis of Spec Z

## 1. Semilocal index category

The 2026 arithmetic-Jacobian paper uses finite sets of places
\(S\ni\infty\) and the semilocal spaces
\(\mathbb A_S=\prod_{v\in S}\mathbb Q_v\).  If \(S\subset T\), passage
from \(S\) to \(T\) adds the local factors indexed by \(T\setminus S\).

For a finite set \(S_f\) of rational primes, define the determinant line

\[
 \Lambda_S
 =\Lambda_\infty\otimes
 \bigotimes_{p\in S_f}\det C_p^\bullet(s)^{-1},
 \tag{1.1}
\]

where \(C_p^\bullet(s)\) is the twisted orbit complex of `107_185` and
\(\Lambda_\infty\) is the regularized number-operator determinant line
of `107_186` together with the degree-zero/two factors.

On the half-plane \(\Re(s)>1\), every local complex is acyclic and
carries the canonical torsion section

\[
 z_p(s)=(1-p^{-s})^{-1}.
\]

## 2. Transition maps

For \(S\subset T\), define

\[
 \rho_{S,T}:\Lambda_S\longrightarrow\Lambda_T,
 \qquad
 v\longmapsto v\otimes
 \bigotimes_{p\in T_f\setminus S_f}z_p(s).
 \tag{2.1}
\]

Associativity of tensor product gives the exact cocycle

\[
 \rho_{T,U}\circ\rho_{S,T}=\rho_{S,U}
 \qquad(S\subset T\subset U).
 \tag{2.2}
\]

Thus \(\{\Lambda_S,\rho_{S,T}\}\) is a directed determinant-line system
on the actual semilocal indexing category, not a collection of unrelated
finite products.

## 3. Canonical sections and cofinal limit

The canonical section at level \(S\) is

\[
 Z_S(s)
 ={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)
 \prod_{p\in S_f}(1-p^{-s})^{-1}.
 \tag{3.1}
\]

It satisfies

\[
 Z_T(s)=\rho_{S,T}Z_S(s).
\]

Along the cofinal family \(S(P)=\{p:p\le P\}\), absolute convergence
gives

\[
 \lim_{P\to\infty}Z_{S(P)}(s)=\xi(s)
 \qquad(\Re s>1).
 \tag{3.2}
\]

The completed orbit determinant of `107_187` is therefore the canonical
cofinal section of this line system.

## 4. Result and sheaf boundary

This constructs the determinant package on every finite semilocal chart
and all restriction/extension transitions between such charts.  It is
the first global object in this route that simultaneously uses:

1. Deninger's real prime orbits;
2. Connes--Consani's semilocal indexing by finite sets of places;
3. the archimedean regularized determinant;
4. the completed zeta section.

It is not yet a determinant-line **sheaf on the absolute square**.  That
promotion requires proving descent with the crossed-product structure
sheaf, identifying the generic-point white-light subtraction, and
constructing a metric/Deligne pairing.  No such promotion is claimed.

## 5. Falsifier

The verifier fixes nested and nonnested real prime sets, checks every
transition ratio and triple cocycle at real and complex spectral
parameters, and checks monotone cofinal convergence to \(\xi(s)\) on
the real axis.  Any atlas-dependent transition or failed cocycle returns
`VERDICT: NO`.
