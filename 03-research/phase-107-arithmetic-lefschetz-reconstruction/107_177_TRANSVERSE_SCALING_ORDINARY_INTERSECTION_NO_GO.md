# 107.177 -- Transverse scaling is not an ordinary arithmetic intersection

## 1. The local graph

Fix a prime \(p\), let \(u\in\mathbb Z_p^\times\), and consider the
scaling map on the transverse affine line

\[
 m_u:\mathbb A^1\longrightarrow\mathbb A^1,qquad x\longmapsto ux.
\]

In \(\mathbb A^1\times\mathbb A^1\), its graph and the diagonal have
equations

\[
 y=ux,qquad y=x.
\]

Over \(\mathbb Q_p\), if \(u\neq1\), their local intersection algebra at
the origin is

\[
 \mathbb Q_p[[x]]/((u-1)x)\simeq\mathbb Q_p.
\]

Hence the ordinary algebraic intersection multiplicity is always

\[
 i_0(\Gamma_{m_u},\Delta)=1.
 \tag{1.1}
\]

## 2. The distributional weight varies

The local term in the published trace formula is not (1.1), but

\[
 L_p(u)={1\over|1-u|_p}.
 \tag{2.1}
\]

For \(u=1+p^k\), \(k\ge1\),

\[
 L_p(1+p^k)=p^k.
 \tag{2.2}
\]

Thus ordinary generic intersection remains 1 while the required weight
ranges through \(p,p^2,p^3,\ldots\).  Formula (2.1) is the inverse
determinant of \(1-dm_u\), as in an equivariant or distributional
Lefschetz formula; it is not a cycle-intersection multiplicity.

## 3. Integral closure produces excess intersection

Taking the same equations over \(\mathbb Z_p\) gives

\[
 \mathbb Z_p[x,y]/(y-x,y-ux)
 \simeq\mathbb Z_p[x]/((u-1)x).
 \tag{3.1}
\]

When \(u=1+p^k\), reduction modulo \(p\) turns (3.1) into

\[
 \mathbb F_p[x],
\]

because the two graphs coincide on the entire special transverse line.
The integral intersection is therefore not finite or proper: it has a
vertical excess component.  Its generic fibre still has the single
transverse point of multiplicity 1.

This rules out a second possible shortcut.  Passing from the generic
intersection to the integral model does not automatically turn 1 into
\(p^k\); it destroys properness instead.

## 4. Exact consequence

Combining `107_176` and the calculation above:

1. translation on a smooth group has no proper fixed intersection;
2. transverse scaling has a proper generic intersection of constant
   multiplicity 1;
3. its integral closure acquires excess vertical intersection whenever
   the distributional weight is nontrivial;
4. the desired \(p^k\) is an equivariant inverse determinant.

Therefore row (c) cannot identify the published local trace with an
ordinary graph--diagonal intersection.  A viable construction must
define an **equivariant excess-intersection class** or a derived/localized
trace on the monoidal boundary and prove that its numerical realization
is (2.1).  This extra structure must subsequently admit a global
bilinear pairing before arithmetic Hodge index can be invoked.

This is a no-go for ordinary intersections, not for an equivariant
intersection theory.

## 5. Falsifier

The verifier constructs the actual graph and diagonal ideals for
\(p=2,3,5,7,11\) and \(1\le k\le4\).  It checks that every generic
intersection has length one, every special fibre has dimension one, and
the required weights are the distinct exact integers \(p^k\).  Any
ordinary intersection recovering those weights returns `VERDICT: NO`.
