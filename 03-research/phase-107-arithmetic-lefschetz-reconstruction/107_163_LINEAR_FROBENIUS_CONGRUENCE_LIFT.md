# 107.163 -- Linear lift of the rational Frobenius congruences

## 1. Source correspondence

For coprime positive integers \(n,m\), Connes--Consani's rational
Frobenius correspondence is induced on the square by

\[
 \mu\circ\mathrm{Fr}_{n,m}:
 q^a\otimes q^b\longmapsto q^{na+mb}.
 \tag{1.1}
\]

This is Proposition 6.11 of *Geometry of the arithmetic site*.  At a
prime \(p\), put \(H_p=\mathbb Z[1/p]\) and form the integral monoid
algebras

\[
 A_p=\mathbb Z[H_p^+\times H_p^+],
 \qquad B_p=\mathbb Z[H_p^+].
\]

On the enriched unreduced monomial support, the source operation (1.1)
has the canonical abelian lift

\[
 \Lambda_{n,m}:A_p\longrightarrow B_p,qquad
 X^aY^b\longmapsto T^{na+mb}.
 \tag{1.2}
\]

It is a ring homomorphism and therefore induces a morphism of
Eilenberg--MacLane modules.  On positive supports, taking the least
weighted exponent after (1.2) recovers exactly the tropical morphism
of (1.1).  No target correspondence has been added.

## 2. Exact kernel

**Theorem.**  The kernel of (1.2) is the binomial ideal

\[
 \ker\Lambda_{n,m}
 =\left(
 X^{m/p^k}-Y^{n/p^k}:k\ge0
 \right).
 \tag{2.1}
\]

**Proof.**  Group a polynomial in \(A_p\) according to the common
weight \(na+mb\).  It lies in the kernel exactly when the sum of its
coefficients on every weight fiber is zero.  Hence the kernel is
generated additively by differences of monomials with equal weight.

If

\[
 na+mb=na'+mb',
\]

then, because \((n,m)=1\), there is \(t\in H_p\) such that

\[
 (a-a',b-b')=(mt,-nt).
\]

Indeed Bezout expresses \(t\) as an integral combination of
\(mt,nt\), both of which lie in \(H_p\).  After removing the common
nonnegative monomial factor, the resulting binomial is

\[
 X^{mt}-Y^{nt},\qquad t\in H_p^+.
\]

Write \(t=c p^j\), with \(c\ge1\), \(j\in\mathbb Z\).  If \(j=-k<0\),
the difference is divisible by
\(X^{m/p^k}-Y^{n/p^k}\); if \(j\ge0\), it is divisible by the
\(k=0\) generator.  This proves containment in the right side of
(2.1).  The reverse containment follows directly from (1.2). \(\square\)

For \(n=m=1\), (2.1) is the lifted diagonal.  General \((n,m)\) gives
the rational Frobenius graph/congruence.

## 3. Finite-depth form

At denominator depth \(R\), use

\[
 H_{p,R}^+=p^{-R}\mathbb Z_{\ge0}.
\]

Then

\[
 \ker\Lambda_{n,m,R}
 =\left(X^{m/p^R}-Y^{n/p^R}\right).
 \tag{3.1}
\]

Every equal-weight pair differs by an integral multiple of
\((m/p^R,-n/p^R)\), so the same proof gives (3.1).  The transition
\(R\to R+1\) sends

\[
 X^{m/p^R}-Y^{n/p^R}
 =A^p-B^p
 =(A-B)(A^{p-1}+\cdots+B^{p-1}),
\]

where \(A=X^{m/p^{R+1}}\), \(B=Y^{n/p^{R+1}}\).  Thus the finite-level
ideals form the ascending system

\[
 I_R\subsetneq I_{R+1},
 \qquad \varinjlim_R I_R=\ker\Lambda_{n,m}.
 \tag{3.2}
\]

The inclusion is strict: in the quotient by \(I_R\), the two
\(p\)-th roots represented by \(A,B\) need not coincide even though
their \(p\)-th powers do.  Equivalently, a lattice pair at depth
\(R+1\) differing by the primitive step \((m,-n)\) is not connected
by steps \((pm,-pn)\) coming from \(I_R\).

This is the equation-level counterpart of 107_153--107_154: bilateral
Frobenius cannot close at one finite level, but every fixed-depth
correspondence has one exact equation and the full relation is recovered
by a directed colimit.

## 4. Bounded-module compatibility

On coefficient \(\ell^1\) balls, \(\Lambda_{n,m,R}\) is contractive:
colliding monomials add coefficients, so

\[
 \|\Lambda_{n,m,R}(f)\|_1\le\|f\|_1.
\]

It therefore defines a morphism of the bounded
\(\mathbb S[\pm1]\)-modules used in 107_150 and 107_154.  Its kernel is
a bounded submodule, so it is admissible as a differential or incidence
map in the tolerance construction of 107_151.

This closes the local algebraic-lift problem for rational Frobenius
congruences.  It does not construct the global Cech cover, prove descent
across the Scaling Site, define intersections, or prove Riemann--Roch.
It also does not descend additively through Newton-polygon reduction;
107_164 proves that every such descent is zero.  The present lift lives
upstairs on monomial support, with the reduced Newton polygon retained
only as a non-additive tropical shadow.

## 5. Falsifier

The verifier uses the actual prime atlas \(2,3,5,7,11\), four coprime
pairs \((n,m)\), and depths through \(R=4\).  On finite boxes it checks
that translates of the deepest-root relation span every equal-weight
kernel fiber.  It then omits that root and verifies that the shallower
relation fails.  Consequently the program can return `NO` both for an
incorrect kernel and for an unjustified fixed-level Frobenius closure.
