# 107.198 -- A one-way dynamic shift has trivial Fredholm determinant

## 1. Natural weighted shift

Let \(H=\ell^2(\mathbb Z_{\ge1})\), with number operator
\(Ne_n=ne_n\), and let

\[
 Se_n=e_{n+1}.
\]

For \(|q|<1\), the dynamically weighted shift

\[
 A_q=q^N S
 \tag{1.1}
\]

is trace class: its singular values are \(|q|^{n+1}\), whose sum is
finite.

## 2. Determinant theorem

For every \(k\ge1\), \(A_q^k\) raises number degree by \(k\).
Consequently every diagonal matrix coefficient vanishes and

\[
 \mathrm{Tr}(A_q^k)=0.
 \tag{2.1}
\]

The Fredholm determinant expansion therefore gives

\[
 \det_{\mathrm F}(1-A_q)
 =\exp\left(-\sum_{k\ge1}
 {\mathrm{Tr}(A_q^k)\over k}\right)=1.
 \tag{2.2}
\]

The same proof applies to the weighted backward shift
\(S^*q^N\): every positive power strictly lowers degree wherever it is
nonzero and has zero trace.

## 3. No-go theorem

**Theorem.**  A superconnection perturbation whose only off-diagonal
dynamic term is one oriented weighted shift cannot produce the local
determinant \(1-q\), its inverse Euler factor, or the Green connection
of 107_196.

**Proof.**  Its Fredholm determinant contribution is identically one by
(2.2), whereas \(1-q\ne1\) for \(0<|q|<1\). \(\square\)

The missing factor appears only when the quotient mode contributes a
diagonal eigenvalue \(q\), or when bidirectional couplings create
closed degree paths with nonzero traces.  Inserting \(qP_{e_1}\) by
hand would reproduce \(1-q\), but merely reinstates the target quotient
already identified in 107_196.

## 4. Consequence

Combining 107_197 and the present result:

1. the diagonal orthogonal splitting has zero Bott--Chern anomaly;
2. the simplest off-diagonal one-way dynamics has determinant one.

A nontrivial secondary realization must therefore contain a derived
closed loop between the quotient and tail, a boundary eta term, or a
geometrically forced diagonal curvature.  That structure must come from
the ambient prime-orbit normal dynamics, not from the Fock filtration
alone.

## 5. Exact scope

This does not exclude bidirectional Dirac-type superconnections,
Toeplitz boundary extensions, or nonnormal weighted shifts with closed
cycles.  It closes only pure raising or pure lowering perturbations.

## 6. Falsifier

The verifier builds actual finite truncations for
\(q=p^{-s}\), using primes \(2,3,5,7,11\), real/complex \(s\), and
dimensions through \(64\).  Every upper and lower triangular
determinant must equal one.  It checks trace powers directly and requires
a diagonal rank-one mutation to produce \(1-q\), so the gate can
distinguish the missing quotient term.
