# 107.161 -- Cross-prime restriction no-go for the published CC pullback sheaf

## 1. Input fixed before the calculation

Let \(X=\mathrm{Spec}\,\mathbb Z\), and let \(\mathcal S\) be the
sheaf used by Connes--Consani to define the geometric morphism from
\(X\) to the arithmetic site.  Their definition gives

\[
 \mathcal S_p=H(p)^+=\mathbb Z[1/p]_+,
 \qquad \mathcal S_\eta=\{0\},
 \tag{1.1}
\]

and, for every nonempty open \(U\subset X\),

\[
 \Gamma(U,\mathcal S)=
 \left\{(\xi_p)_{p\in U}:\xi_p\in H(p)^+,
 \ \xi_p\ne0\text{ for only finitely many }p\right\}.
 \tag{1.2}
\]

Restrictions are the evident deletion of coordinates.  These statements
are Definition 4.1 and the paragraph preceding it in Connes--Consani,
*The arithmetic site*, arXiv:1502.05580v1.  Proposition 4.2 gives the
corresponding signed statement for \(\Theta^*(\mathcal O)\), with generic
stalk \(\mathbb B\).

## 2. The no-go

**Theorem.**  If \(p\ne q\) are finite primes, the restriction diagram
of \(\mathcal S\) contains no nonzero transition from the \(p\)-stalk
to the \(q\)-stalk.  More strongly, arbitrary values
\(a\in H(p)^+\) and \(b\in H(q)^+\) extend simultaneously to a section
on every open containing \(p,q\), without a compatibility equation
between \(a\) and \(b\).  Therefore nontrivial cross-prime coupling
cannot be reconstructed from the restriction maps of \(\mathcal S\)
alone.

**Proof.**  Define a section by \(\xi_p=a\), \(\xi_q=b\), and
\(\xi_\ell=0\) at every other closed point.  It satisfies (1.2), so the
two values are independent.  Choose a cofinite open \(V\) containing
neither \(p\) nor \(q\), and put

\[
 U_p=V\cup\{p\},\qquad U_q=V\cup\{q\}.
\]

On the overlap \(U_p\cap U_q=V\), both one-prime sections restrict to
zero.  Their only common generization is \(\eta\), whose stalk is zero
by (1.1).  Distinct closed points of \(\mathrm{Spec}\,\mathbb Z\)
are incomparable under specialization, so there is no further stalk
transition.  Hence the complete restriction datum relating the two
one-prime sectors is zero.  A nonzero relation between them would be
additional structure, not a consequence of this sheaf. \(\square\)

The same conclusion holds for the finite-valued part of
\(\Theta^*(\mathcal O)\): its restrictions delete prime coordinates,
while its generic finite value is zero.  The separate constant
\(-\infty\) section does not couple finite prime values.

## 3. Consequence for the square

The local pro-Frobenius levels of 107_154 can descend prime by prime,
but their CC restriction maps alone cannot create a global incidence,
metric, or intersection term involving two distinct primes.  Such a
term must enter through additional global geometry.  The adelic and
archimedean coordinates in the Scaling Site, the arithmetic
Abel--Jacobi construction, and Morishita's bridge are possible sources;
this theorem does not choose among them.

This is a scoped no-go.  It does not say that a global square cannot
exist, nor that every sheaf constructed from \(\mathcal S\) remains a
direct sum.  It says exactly that prime-chart restrictions in the
published pullback sheaf do not supply the missing glue.  Consequently
the next row-(a) construction must exhibit and verify an additional
cross-prime gluing morphism; it cannot list ``restrictions between
primes'' as if they were already present in \(\Theta^*(\mathcal O)\).

## 4. Falsifier

The verifier reads the published TeX source, checks that the two defining
properties are actually present, and evaluates the restriction diagram
on the fixed real primes \(2,3,5,7,11\).  It also runs a negative-control
candidate with a nonzero generic channel; that candidate must be
rejected.  Thus the program can return `VERDICT: NO` if either the source
input or the claimed restriction mechanism changes.
