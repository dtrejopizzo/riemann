# 106.186 — The Euler--Bohr kernel and the real-scale obstruction

## 1. Purpose

Document 106.185 shows that a scale-invariant Hilbert majorant cannot be
diagonal in the dense arithmetic orbit coordinates.  The next canonical
candidate is nonlocal: retain one independent phase for every prime and
use the product of the local Poisson states.

This note constructs that kernel exactly.  It is positive definite and
reproduces every local coefficient \(p^{-|k|/2}\).  It also proves a sharp
obstruction: the associated unitary representation of the discrete
arithmetic scale group cannot extend strongly continuously to the real
scaling flow.  Thus the Euler product and the archimedean flow cannot be
glued by a single stationary scalar covariance.  The Cauchy path dilation
of 106.154 avoids this obstruction by using different increment
observables, but its positive Hilbert completion still has zero reduced
CCM cokernel.

## 2. The arithmetic scale group and its compact dual

Let

\[
 G=\log\mathbb Q_+^\times
   \simeq\bigoplus_{p\ {m prime}}\mathbb Z,                \tag{1}
\]

where the coordinate of \(g=\log q\) at \(p\) is \(v_p(q)\).  Its
compact Pontryagin dual is

\[
 \widehat G=\prod_p\mathbb T.                               \tag{2}
\]

For \(r_p=p^{-1/2}\), let \(\mu_{r_p}\) be the Poisson probability
measure on \(\mathbb T\), characterized by

\[
 \int_{\mathbb T}z^k\,d\mu_{r_p}(z)=r_p^{|k|}
 =p^{-|k|/2}.                                                \tag{3}
\]

Kolmogorov's product theorem gives the probability measure

\[
 \mu_E=\bigotimes_p\mu_{p^{-1/2}}                            \tag{4}
\]

on \(\widehat G\).

## 3. Exact positive Euler kernel

For \(g=\log q\in G\), define

\[
 \boxed{
 K_E(g)=\int_{\widehat G}\chi(g)\,d\mu_E(\chi)
       =\prod_p p^{-|v_p(q)|/2}.}                            \tag{5}
\]

The product is finite because \(q\) has finite prime support.

### Theorem 3.1 — Positivity and exact local moments

The function \(K_E:G\to(0,1]\) is positive definite.  For every prime
\(p\) and \(k\in\mathbb Z\),

\[
 \boxed{K_E(k\log p)=p^{-|k|/2}.}                           \tag{6}
\]

More generally, for \(q=\prod_pp^{n_p}\),

\[
 K_E(\log q)=\prod_pp^{-|n_p|/2}.                           \tag{7}
\]

#### Proof

Equation (5) is the Fourier transform of the positive probability measure
\(\mu_E\) on \(\widehat G\), hence is positive definite by the elementary
Bochner theorem for discrete abelian groups.  Equations (6)--(7) follow
from independence and (3). \(\square\)

Equivalently, on \(L^2(\widehat G,\mu_E)\) define

\[
 (U_gF)(\chi)=\chi(g)F(\chi),\qquad \mathbf1(\chi)=1.       \tag{8}
\]

Then \(U\) is a unitary representation of \(G\), \(\mathbf1\) is cyclic
for the coordinate algebra, and

\[
 K_E(g)=\langle U_g\mathbf1,\mathbf1\rangle.                \tag{9}
\]

This is a source-defined nonlocal positive kernel.  It contains the full
Euler independence rather than only one prime at a time.

## 4. Failure of real-scale continuity

The group \(G\) is also a dense subgroup of \(\mathbb R\) through its
logarithmic embedding.  These two topologies on \(G\) are incompatible
for \(K_E\).

### Theorem 4.1 — No strongly continuous real extension

The unitary representation (8) has no strongly continuous extension to a
unitary representation of \((\mathbb R,+)\) whose restriction to \(G\)
is \(U\).  In fact, \(K_E\) is discontinuous at the identity for the real
topology on \(G\).

#### Proof

Take

\[
 g_n=\log\frac{n+1}{n}.                                     \tag{10}
\]

Then \(g_n\in G\) and \(g_n\to0\) in \(\mathbb R\).  Since
\(\gcd(n,n+1)=1\), formula (5) gives

\[
 K_E(g_n)
 =\prod_p p^{-\frac12|v_p(n+1)-v_p(n)|}
 =\frac1{\sqrt{n(n+1)}}\longrightarrow0.                   \tag{11}
\]

But \(K_E(0)=1\).  Thus \(K_E\) is not continuous at zero.  If a
strongly continuous extension \(\widetilde U_t\) existed, every matrix
coefficient
\(t\mapsto\langle\widetilde U_t\mathbf1,\mathbf1\rangle\)
would be continuous, contradicting (9)--(11). \(\square\)

### Corollary 4.2 — The independent Euler phases are almost never real characters

The characters of \(G\) which extend continuously to \(\mathbb R\) are

\[
 \chi_\xi(\log q)=q^{i\xi},\qquad \xi\in\mathbb R.          \tag{12}
\]

The measure \(\mu_E\) cannot be supported on this one-parameter family.

#### Proof

Every continuous character of \(\mathbb R\) has the form
\(t\mapsto e^{i\xi t}\), giving (12).  If \(\mu_E\) were supported on
these characters, its Fourier transform (5) would be continuous in the
real topology, contrary to Theorem 4.1. \(\square\)

## 5. Why a positive scalar correction cannot repair the jump

Let \(K_c\) be any positive-definite function on \(\mathbb R\), restricted
to \(G\), and let \(a>0\).  Then

\[
 K=K_c+aK_E                                                    \tag{13}
\]

is still discontinuous at zero in the real topology: along (10),

\[
 K(g_n)\longrightarrow K_c(0),
 \qquad K(0)=K_c(0)+a.                                      \tag{14}
\]

Hence adding a positive archimedean covariance cannot cancel the Euler
jump.  Cancellation requires a signed or graded coupling before the final
positive polarization.  A direct orthogonal sum of positive Euler and
Gamma sectors is insufficient.

This explains structurally why the Fourier--Weyl construction must first
live in a relative mixed complex: the prime, Gamma, and polar pieces have
to interact through its differential and boundary form before a positive
degree-one metric can emerge.

## 6. Comparison with the Cauchy path dilation

The stationary circular Cauchy process of 106.154 has a strongly
continuous real shift.  It realizes a prime coefficient through the
increment at time \(\log p\):

\[
 \mathbf E\,e^{ik(X_{t+\log p}-X_t)}=p^{-|k|/2}.            \tag{15}
\]

It does not assign one fixed character \(\chi\) to all primes.  The
increment over \(\log q\) depends on the real sum of lengths, whereas
\(K_E\) depends on the total variation of the prime valuation vector.
For example,

\[
 e^{-\frac12|\log(p/r)|}
 \ne (pr)^{-1/2}\quad(p\ne r).                              \tag{16}
\]

Thus 106.154 and the Euler--Bohr kernel solve different compatibility
problems:

* the path dilation preserves real-scale continuity and each individual
  prime tower;
* the Euler--Bohr kernel preserves simultaneous independence of all prime
  coordinates.

The missing polarization cannot be obtained by identifying these two
objects.  It needs a relative differential whose signed boundary coupling
turns the first object into the arithmetic trace of the second without
destroying real-scale continuity.

## 7. Consequence for the global polarization

Theorem 4.1 gives a new necessary design condition.  A successful
non-geometric majorant cannot be a stationary scalar kernel that encodes
the independent Euler product directly.  It must instead use at least one
of the following genuinely richer structures:

1. a graded/super Hilbert complex in which the discontinuous Euler sector
   cancels against boundary channels before cohomology;
2. a nonstationary path-space kernel whose different prime observations
   are distinct increment subspaces;
3. a source-side intersection product coupling finite and archimedean
   fibers before the scale action descends.

The first two have already been constructed at chain/coefficient level in
106.154--106.156.  What remains is not their local positivity, but a
torsion-sensitive degree-one descent which retains the nonreduced CCM
classes.

## 8. Status

Proved without RH or zero input:

* the canonical nonlocal Euler--Bohr positive kernel;
* exact reproduction of all prime-power coefficients;
* impossibility of extending its discrete scale representation to the
  strongly continuous real scaling flow;
* impossibility of repairing the discontinuity by adding a positive
  continuous scalar covariance.

Still required:

* a graded boundary coupling or source-side intersection pairing whose
  cohomology is both positive and faithful on the nonreduced CCM degree
  one.
