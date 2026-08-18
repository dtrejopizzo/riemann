# A1 variational energy form

## Purpose

This note rewrites the compact A1 core as a finite variational problem.  The
goal is not to rename the missing sign, but to isolate exactly what an
Euler--Gamma energy proof would have to supply.

The output is:

1. an exact signed-measure normal form for the compact core;
2. a Schur--Friedrichs variational identity;
3. a precise non-tautological energy theorem which would imply A1;
4. the missing lemma.  The lemma is not proved here, so A1 is not closed.

## Compact signed measure

Fix \(n\ge8\), write
\[
  T=T_n,\qquad X=e^T,\qquad L_n(u)=L_{n-1}^{(1)}(u),
\]
and put
\[
  E(y)=\psi(y)-y,\qquad A_n=\lambda_n^{\rm arch}>0.
\]
The A1 quantity is
\[
  C_n(T)
  =
  -n+\int_1^X E(y)f'_{n,0}(y)\,dy+{3\over4}A_n.
\tag{1}
\]

From the integration-by-parts normal form in
`113_MELLIN_COBORDER_NORMAL_FORM.md`,
\[
\begin{aligned}
 C_n(T)
 &=
 -n+E(X)X^{-1}L_n(T)
 -\sum_{m\le X}{\Lambda(m)\over m}L_n(\log m)  \\
 &\quad+\int_0^T L_n(u)\,du
 +{3\over4}A_n .
\end{aligned}
\tag{2}
\]
Thus define the finite signed measure
\[
  d\mu_T(u)
  =
  1_{[0,T]}(u)\,du
  -
  \sum_{m\le X}{\Lambda(m)\over m}\,\delta_{\log m}(du)
  +
  E(X)X^{-1}\delta_T(du),
\tag{3}
\]
with the same endpoint convention as the Stieltjes/Perron convention used in
the phase.  Then
\[
  \boxed{
  C_n(T)
  =
  -n+{3\over4}A_n+\int L_n(u)\,d\mu_T(u).
  }
\tag{4}
\]

This is finite.  It contains the prime-pole cancellation before any absolute
values are introduced.

## Abstract Friedrichs variational identity

Let \(H\) be a positive definite Hermitian matrix, \(v\) a column vector and
\(a\in\mathbb R\).  Define the affine quadratic energy
\[
  \mathcal E_{H,v,a}(\eta)
  =
  a+2\operatorname{Re}\langle \eta,v\rangle
  +\langle \eta,H\eta\rangle .
\tag{5}
\]
Completing the square gives
\[
  \inf_\eta \mathcal E_{H,v,a}(\eta)
  =
  a-\langle v,H^{-1}v\rangle .
\tag{6}
\]
Equivalently,
\[
  \inf_\eta \mathcal E_{H,v,a}(\eta)
  =
  {\det\begin{pmatrix}H&v\\v^*&a\end{pmatrix}\over\det H}.
\tag{7}
\]

Therefore the compact A1 inequality \(C_n(T)\ge0\) is equivalent, for any
triple satisfying
\[
  C_n(T)=a-\langle v,H^{-1}v\rangle,
\tag{8}
\]
to the nonnegativity of the minimum of \(\mathcal E_{H,v,a}\).

This equivalence alone has no proof force.  If \(H,v,a\) are chosen after
\(C_n(T)\) is known, (8) is only a coordinate change.  A real proof must
construct \(H,v,a\) from Euler--Gamma data and prove
\[
  \mathcal E_{H,v,a}(\eta)\ge0\qquad\hbox{for all }\eta
\tag{9}
\]
before using (8).

## Variational A1 theorem

The non-tautological variational theorem capable of closing A1 is the
following.

For every \(n\ge8\), construct finite-dimensional data
\[
  H_{n,T}>0,\qquad v_{n,T},\qquad a_{n,T}\in\mathbb R
\]
from the completed Euler--Gamma package, the pole-prime pairing and the A0
cutoff \(T=T_n\), such that:

1. the Schur--Friedrichs identity is exact,
   \[
     C_n(T)
     =
     a_{n,T}
     -
     \langle v_{n,T},H_{n,T}^{-1}v_{n,T}\rangle;
   \tag{10}
   \]
2. the affine energy is nonnegative,
   \[
     a_{n,T}
     +2\operatorname{Re}\langle \eta,v_{n,T}\rangle
     +\langle \eta,H_{n,T}\eta\rangle
     \ge0
     \qquad(\hbox{all }\eta).
   \tag{11}
   \]

Then (6), (10) and (11) give
\[
  C_n(T_n)\ge0\qquad(n\ge8),
\]
which is A1.  Combined with A0 and the finite certificate, this implies the
Li inequalities in the already recorded assembly theorem.

The theorem is stronger than bare A1 because it asks for a positive energy
structure, not merely for the single scalar sign.

## Mellin candidate for the base energy

The exact Mellin normal form supplies the natural candidate.  For any
polynomial \(q\) define
\[
  P_{q,T}(s)=\int_0^T e^{-su}q(u)\,du .
\tag{12}
\]
For \(q=L_n\), this is \(P_{n,T}\) in
`113_MELLIN_COBORDER_NORMAL_FORM.md`.

The prime block is
\[
  {1\over2\pi i}
  \int_{c-i\infty}^{c+i\infty}
  -{\zeta'\over\zeta}(1+s)P_{q,T}(s)\,ds,
  \qquad c>0.
\tag{13}
\]
After recombining the pole and Gamma terms, the completed logarithmic
derivative gives the symmetrized kernel
\[
  F(s)={\xi'\over\xi}(1+s).
\tag{14}
\]
A Herglotz-type energy would come from the positive-definiteness of
\[
  K_F(s,t)
  =
  {F(s)+\overline{F(t)}\over s+\overline t}
\tag{15}
\]
on the Mellin transforms \(P_{q,T}\), after the explicit pole, endpoint and
Gamma residues have been separated in the same finite convention as (2).

Concretely, the desired construction would choose a finite test space
\[
  V_{n,T}\subset \{P_{q,T}:q\in\mathbb C[u],\ \deg q\le n-1\}
\]
and define \(H_{n,T}\), \(v_{n,T}\), \(a_{n,T}\) by the completed kernel
\(K_F\) plus the explicit residue terms, so that the Schur complement is
exactly (4).

The contour algebra needed for such an identity is the same algebra already
closed in the Mellin-coborder normal form.  The new requirement is not the
identity; it is positivity of the completed kernel on the chosen finite test
space.

## Missing lemma

The precise missing input is:

**Euler--Gamma coercive Schur lemma.**  For each \(n\ge8\) and A0 cutoff
\(T_n\), the pole-prime-Gamma symmetrization of the completed Mellin kernel
admits a finite Friedrichs decomposition
\[
  C_n(T_n)
  =
  a_{n,T_n}
  -
  \langle v_{n,T_n},H_{n,T_n}^{-1}v_{n,T_n}\rangle
\]
such that the associated affine energy is nonnegative for all variations:
\[
  a_{n,T_n}
  +2\operatorname{Re}\langle \eta,v_{n,T_n}\rangle
  +\langle \eta,H_{n,T_n}\eta\rangle
  \ge0 .
\tag{16}
\]
The positivity must be proved from the Euler product, the Gamma factor, the
functional equation and the finite cutoff construction, before interpreting
the result through the zero divisor or Li positivity.

This lemma is exactly the variational version of the symmetrized Mellin
boundary positivity gate in `124_A1_GATE_IMPLICATION_GRAPH.md`.  It is also
the non-tautological part of the bordered-current route: the Schur complement
formula is automatic, while coercivity of the completed energy is the
force-RH step.

## Why this does not close A1

The kernel \(K_F\) in (15) is positive if \(F\) is a right-half-plane
Herglotz function.  Establishing that positivity for the completed
zeta-specific \(F\), in a form strong enough to survive the pole-prime
pairing and yield (16), would force the same boundary support phenomenon as
the positive-measure/de Branges/Pick gates.  It cannot be obtained merely by
contour shifting or by the formal identity \(\xi(s)=\xi(1-s)\).

Thus the variational form is a sharpened target, not a proof.  It identifies
the missing step as a coercive Euler--Gamma energy theorem for the
symmetrized completed Mellin kernel.

## Status

Normal form closed.  A1 remains open.

The exact live theorem is the Euler--Gamma coercive Schur lemma above.  If it
is proved, then A1 follows immediately by the variational minimum principle.
Without it, the energy language is only an equivalent Schur-complement
rewriting of the signed compact inequality.
