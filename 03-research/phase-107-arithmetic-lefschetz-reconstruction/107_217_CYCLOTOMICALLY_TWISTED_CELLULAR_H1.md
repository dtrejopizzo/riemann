# 107.217 -- Integral H1 of the cyclotomically twisted rooted square

## 1. The twisted finite-level complex

Let \(O\) be a Dedekind domain and let \(a,b\in O\).  The rank-one
local system on the rooted cellular torus with horizontal and vertical
monodromies \(1+a\) and \(1+b\) has Koszul complex

\[
 0\longrightarrow O
 \xrightarrow{d_2}O^2
 \xrightarrow{d_1}O
 \longrightarrow0,
 \tag{1.1}
\]

where

\[
 d_2(c)=(-bc,ac),\qquad d_1(x,y)=ax+by.
 \tag{1.2}
\]

The identity \(d_1d_2=0\) is integral and preserves the two rulings.  For
\(O=\mathbb Z[\zeta_n]\), put

\[
 a=\zeta_n^u-1,\qquad b=\zeta_n^v-1.
 \tag{1.3}
\]

This is the character twist of the constant cellular complex in
107_169; it is not a postulated cohomology group.

## 2. Exact cohomology theorem

Set \(I=(a,b)\).  If \((a,b)\ne(0,0)\), then

\[
 H^0\cong O/I,
 \qquad
 H^1\cong I^{-1}/O,
 \qquad
 H^2=0.
 \tag{2.1}
\]

Here degrees are written cohomologically; reversing (1.1) gives the
same three underlying groups as cellular homology.

### Proof

The image of \(d_1\) is \(I\), giving \(H^0=O/I\).  Since \(O\) is a
domain and one of \(a,b\) is nonzero, \(d_2\) is injective, so
\(H^2=0\).

Every syzygy \((x,y)\) of \((a,b)\) has the form

\[
 (x,y)=(-bc,ac),
 \qquad c\in I^{-1}
 =\{c\in\mathrm{Frac}(O):ca,cb\in O\}.
\]

Under this identification, \(\mathrm{im}\,d_2\) is the submodule
with \(c\in O\).  Hence \(H^1=I^{-1}/O\), proving (2.1).

Both finite groups have the same cardinal:

\[
 |H^0|=|H^1|=\mathrm{N}(I).
 \tag{2.2}
\]

For the trivial character \(a=b=0\), both differentials vanish and

\[
 (H^0,H^1,H^2)=(O,O^2,O),
 \tag{2.3}
\]

recovering the untwisted \((1,2,1)\) amplitude of 107_167 and 107_169.

## 3. Cyclotomic torsion criterion

Let

\[
 d=\gcd(u,v,n),\qquad m=n/d.
\]

The elementary cyclotomic ideal identity gives

\[
 I=(1-\zeta_n^d).
 \tag{3.1}
\]

Consequently

\[
 \mathrm{N}(I)
 =\Phi_m(1)^{\varphi(n)/\varphi(m)}.
 \tag{3.2}
\]

Since

\[
 \Phi_m(1)=
 \begin{cases}
  \ell,&m=\ell^k\text{ is a prime power},\\
  1,&m>1\text{ has at least two prime divisors},
 \end{cases}
\]

the nontrivial twisted complex is integrally acyclic exactly when the
effective character order \(m\) is not a prime power.  At prime-power
order, equal finite torsion survives in degrees zero and one.

This phenomenon is invisible over \(\mathbb C\), where every nontrivial
character summand is acyclic.  It is precisely an integral middle
cohomology contribution, not an extra free Betti class.

## 4. Consequence for row (a)

The finite rooted square now has a proved, nonconstant coefficient
\(H^1\) calculation.  It corrects the over-simple Fourier statement
that all nontrivial characters may simply be discarded: they are
rationally contractible but can carry arithmetic torsion.

This does not yet construct the divisor sheaves \(O(D)\), the transition
maps on these torsion groups under every rooted-level enlargement, or
the integer dimension of the resulting tolerance cohomology.  Those are
the remaining steps before this calculation can repair the missing
middle term in the Connes--Consani square.

## 5. Falsifier

`107_217_cyclotomically_twisted_cellular_h1.sage` constructs actual
cyclotomic integer rings, represents multiplication by
\(\zeta_n^u-1\) and \(\zeta_n^v-1\) as integral matrices, and asks Sage
for the homology of the resulting chain complex.  It compares both
torsion orders with the independently computed ideal norm and (3.2).
A sign-mutated differential must fail the chain condition.

