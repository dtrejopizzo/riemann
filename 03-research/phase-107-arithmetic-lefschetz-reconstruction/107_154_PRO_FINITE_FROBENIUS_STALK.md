# 107.154 -- A pro-finite-dimensional Frobenius realization of the absolute stalk

## 1. Construction

The no-go of 107_153 forbids a nonconstant finite-dimensional submodule
on which local Frobenius is an automorphism.  It does not forbid
Frobenius maps between finite levels.

Every nonzero exponent \(a\in\mathbb Z[1/p]_+\) has a unique expression

\[
 a=c\,p^j,\qquad c\in\mathbb Z_{>0},\quad p\nmid c,\quad j\in\mathbb Z.
\]

For \(A\ge1\) and \(R\ge0\), define

\[
 M_p(A,R)=\{0\}\cup
 \{c\,p^j:1\le c\le A,\ p\nmid c,\ -R\le j\le R\}.
\]

Let \(L_p(A,R)\) be the free abelian group on the monomials
\(\{T^a:a\in M_p(A,R)\}\), and let

\[
 E_p(A,R;n)=
 \left\{
 \sum_{a\in M_p(A,R)}x_aT^a:
 \sum_a|x_a|\le n
 \right\}.
\]

This is the bounded \(\mathbb S[\pm1]\)-module
\(\|H L_p(A,R)\|_n\).

## 2. Frobenius between levels

Multiplication and division of exponents by \(p\) define isometric maps

\[
 \varphi_p^{\pm1}:
 E_p(A,R;n)\longrightarrow E_p(A,R+1;n).
\]

They preserve coefficient mass exactly.  They are not endomorphisms of
a fixed finite level, in agreement with 107_153.

For \(A\le A'\) and \(R\le R'\), basis inclusion gives an isometric
transition map

\[
 E_p(A,R;n)\hookrightarrow E_p(A',R';n).
\]

The filtered colimit is exactly the bounded coefficient-mass module in
the full additive stalk:

\[
 \varinjlim_{A,R}E_p(A,R;n)
 =
 \left\{f\in\mathbb Z[T^{\mathbb Z[1/p]_+}]:
 \|f\|_1\le n\right\}.
\]

Indeed every polynomial has finite exponent support, and therefore
lies in one \(M_p(A,R)\).

## 3. Finite dimension at every level

Put

\[
 d_p(A,R)
 =
 1+\bigl(A-\lfloor A/p\rfloor\bigr)(2R+1).
\]

This is the rank of \(L_p(A,R)\).  The higher-rank dimension theorem of
107_146 gives

\[
 d_p(A,R)
 \le
 \dim_{\mathbb S[\pm1]}E_p(A,R;n)
 \le
 d_p(A,R)\left\lceil\log_2(n+1)\right\rceil.
\]

The lower bound is ordinary rank: the radius-\(n\) ball contains every
basis vector when \(n\ge1\).  At \(n=1\), equality holds:

\[
 \dim_{\mathbb S[\pm1]}E_p(A,R;1)=d_p(A,R).
\]

The mass used here is not provisional.  By 107_150, the projective
tensor norm inherited from the published CC \(\ell^1\) factors is the
entrywise \(\ell^1\) norm.  The trace/nuclear norm belongs instead to
Euclidean factors and is not the mass of this construction.

Exact calculations suggest the sharper formula

\[
 \dim_{\mathbb S[\pm1]} M_d(n)
 =d\left\lceil\log_2(n+1)\right\rceil,
 \qquad d\ge2.
 \tag{3.1}
\]

It has been verified for \(d=2\), \(1\le n\le6\); for \(d=3\),
\(1\le n\le3\); and for \(d=4\), \(1\le n\le2\).  It is a conjecture,
not an input to any result in this note.  Rank one is genuinely
exceptional: the CC formula is
\(\lceil\log_3(2n+1)\rceil\), and (3.1) already fails at \(n=4\).

## 4. The square and two rulings

Use the basis

\[
 M_p(A,R)\times M_p(A,R)
\]

for the square module \(E_p^\square(A,R;n)\).  Its rank is
\(d_p(A,R)^2\).  The two Frobenius maps

\[
 \varphi_{\mathrm v}(a,b)=(pa,b),
 \qquad
 \varphi_{\mathrm h}(a,b)=(a,pb)
\]

and their inverses map level \(R\) isometrically to level \(R+1\).
They commute exactly.  This supplies two distinct finite-level rulings
and a diagonal Frobenius action
\(\varphi_\Delta=\varphi_{\mathrm v}\varphi_{\mathrm h}\).

## 5. What is and is not solved

This is an actual bounded-module realization of every finite collection
of local Frobenius iterates.  It avoids the false requirement that a
single finite level be invariant under bilateral Frobenius.

It does not yet prove stabilization of cohomology for a fixed divisor
under enlargement of \((A,R)\), construct the additional global glue
between the prime sectors, or construct a proper global square.
The published prime-chart restrictions cannot provide that glue by
107_161.  Those are now the exact descent conditions.  In particular, a Riemann--Roch theorem
must use divisor-controlled submodules whose cohomology stabilizes; it
cannot take the dimension of the full filtered colimit, which is
infinite by 107_152.

**Later correction (107_228--107_229).**  Stabilization is not the
correct requirement for the full periodic \(H^0\): its published
continuous dimension requires unbounded filtered dimensions. Moreover,
the rectangular \((A,R)\) levels above have zero density after the
normalization \(p^{-R}\). They remain an exhaustive algebraic
filtration, but continuous-dimension calculations must use the
simultaneous real/\(p\)-adic norm-adapted levels of 107_229.
