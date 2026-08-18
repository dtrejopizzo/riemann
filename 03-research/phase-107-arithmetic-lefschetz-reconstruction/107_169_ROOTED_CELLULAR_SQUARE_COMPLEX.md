# 107.169 -- A rooted cellular square complex with controlled mass

## 1. Finite rooted level

Let \(L=L_T\) be the visible rooted order of 107_157--107_159.  Define

\[
 R_L=\mathbb Z[x,y]/(x^L-1,y^L-1).
\]

As an abelian group, \(R_L\) is free on
\(x^a y^b\), \(0\le a,b<L\).  It is the cellular translation algebra
of the \(L\times L\) subdivision of a two-torus.  Consider the chain
complex

\[
 0\longrightarrow C_2=R_L
 \xrightarrow{\partial_2}C_1=R_L^2
 \xrightarrow{\partial_1}C_0=R_L
 \longrightarrow0,
 \tag{1.1}
\]

where

\[
 \partial_2(f)=((1-y)f,(x-1)f),
\]

and

\[
 \partial_1(a,b)=(x-1)a+(y-1)b.
\]

Commutativity gives

\[
 \partial_1\partial_2(f)
 =(x-1)(1-y)f+(y-1)(x-1)f=0.
\]

This is the ordinary integral cellular complex of the torus, written
without enumerating its cells.

## 2. Cohomological amplitude

**Theorem.**  The homology of (1.1) is

\[
 H_0\cong\mathbb Z,
 \qquad H_1\cong\mathbb Z^2,
 \qquad H_2\cong\mathbb Z,
 \tag{2.1}
\]

and vanishes outside degrees \(0,1,2\).

This follows either from the cellular identification or by Fourier
decomposition over \(\mathbb C\).  At a character
\((\zeta,\eta)\in\mu_L^2\), (1.1) is the Koszul complex of
\((\zeta-1,\eta-1)\), which is acyclic unless
\((\zeta,\eta)=(1,1)\).  At the trivial character both differentials
vanish, leaving dimensions \((1,2,1)\).  Integral cellular homology is
torsion-free, giving (2.1).

By 107_167, this is the cohomology of the periodic foliated product.
Thus (1.1) is an integral, finite-level cohomological model of its
constant-coefficient three-term complex.

## 3. Uniform mass control

Give every \(R_L\) its coefficient \(\ell^1\) norm.  Translation by
\(x\) or \(y\) is an isometry, hence

\[
 \|\partial_2 f\|_1\le4\|f\|_1,
 \qquad
 \|\partial_1(a,b)\|_1\le2(\|a\|_1+\|b\|_1).
 \tag{3.1}
\]

The constants are independent of \(L\).  Therefore (1.1) restricts to
a complex of bounded \(\mathbb S[\pm1]\)-modules after multiplying the
successive mass radii by the fixed factors in (3.1).  This avoids the
unbounded Fourier multiplier of 107_168.

## 4. Directed subdivision without enumeration

Suppose \(L'=dL\).  Let

\[
 \phi:R_L\longrightarrow R_{L'},
 \qquad x\mapsto x'^d,\quad y\mapsto y'^d,
\]

and put

\[
 S_x=1+x'+\cdots+x'^{d-1},
 \qquad S_y=1+y'+\cdots+y'^{d-1}.
\]

The cellular subdivision chain map is

\[
 F_0(f)=\phi(f),
\]

\[
 F_1(a,b)=(S_x\phi(a),S_y\phi(b)),
\]

\[
 F_2(f)=S_xS_y\phi(f).
 \tag{4.1}
\]

The identities

\[
 (x'-1)S_x=x'^d-1,
 \qquad (y'-1)S_y=y'^d-1
\]

prove \(\partial F=F\partial\) in both degrees.  Composition of
subdivisions follows from the corresponding factorization of geometric
sums.  Each \(F\) induces the identity under the canonical
identification (2.1), so homology stabilizes at every level.

All expressions in (4.1) are represented by \((L,d)\) and geometric
sums.  The construction never enumerates the \(L^2\) cells; this is
essential because \(L_T\) is already intractable at \(T=5\).

## 5. Relation to Phase 107

The complex supplies four previously missing properties at once:

1. genuine amplitude \([0,2]\) from geometry, not truncation;
2. integral differentials compatible with \(\mathbb S[\pm1]\);
3. uniform coefficient-mass bounds;
4. canonical transitions along the rooted levels.

Its dual cochain complex can therefore be fed into the tolerance
construction of 107_151.

It must not be used as the divisor intersection ring.  Its ordinary
cohomology has \(H^4=0\), so all products of degree-two Chern classes
vanish; 107_170 gives an explicit contradiction with Paper 0.

This still treats constant coefficients.  To obtain the divisor
cohomology required for RR, one must twist (1.1) by the enriched support
module of 107_165 and prove that the diagonal/Frobenius root ideals of
107_163 define compatible cellular local systems.  Serre duality,
intersection theory, and RR remain open.

## 6. Falsifier

The verifier builds exact cellular matrices for several real rooted
levels, computes their homology, and separately checks the symbolic
subdivision identities for nontrivial divisibilities.  It can return
`NO` for a sign error, a wrong Betti number, or a non-chain transition.
