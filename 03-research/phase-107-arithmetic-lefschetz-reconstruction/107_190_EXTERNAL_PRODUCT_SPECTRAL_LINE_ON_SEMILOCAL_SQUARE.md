# 107.190 -- External product of the spectral determinant line on the semilocal square

## 1. The square that is actually used

Let \(\mathcal B\) be the semilocal basis of
\(X=\operatorname{Spec}\mathbb Z\), with objects

\[
 U_S=X\setminus S
\]

for finite sets \(S\) of rational primes.  We use the product site
\(\mathcal B^\square=\mathcal B\times\mathcal B\), whose basic objects
are \(U_S\boxtimes U_T\).  This is not the relative scheme product
\(X\times_X X=X\), and it is not being declared to be the missing
Connes--Consani absolute surface.

Put

\[
 \mathcal H=\{s\in\mathbb C:\Re(s)>1\},\qquad
 A_2=\mathcal O(\mathcal H^2),
 \qquad z_p(s)=(1-p^{-s})^{-1}.
\]

## 2. External-product line

On a basic product define

\[
 \mathscr L^\square(U_S\boxtimes U_T)=A_2 e_{S,T}.
\]

For \(S\subset S'\) and \(T\subset T'\), set

\[
 r_{S,T}^{S',T'}(f e_{S,T})=
 f\prod_{p\in S'\setminus S}z_p(s_1)
  \prod_{q\in T'\setminus T}z_q(s_2)e_{S',T'}.
 \tag{2.1}
\]

The two coordinate restrictions commute.  If

\[
 g_{S,T}(s_1,s_2)=
 \prod_{p\in S}z_p(s_1)\prod_{q\in T}z_q(s_2),
\]

then the frame change

\[
 \phi_{S,T}(f e_{S,T})=f/g_{S,T}
 \tag{2.2}
\]

turns every map (2.1) into the identity.  Consequently the presheaf is
a rank-one sheaf on the product semilocal site.  This proves all
rectangle Cech equalizers, not merely the transition cocycle: after
(2.2), descent is descent for the constant line.

Thus

\[
 \mathscr L^\square\simeq
 \operatorname{pr}_1^*\mathscr L\otimes
 \operatorname{pr}_2^*\mathscr L
 \tag{2.3}
\]

on \(\mathcal B^\square\).

## 3. Canonical section

Write

\[
 Z_\infty(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

The chartwise elements

\[
 \sigma_{S,T}=
 Z_\infty(s_1)Z_\infty(s_2)g_{S,T}(s_1,s_2)e_{S,T}
 \tag{3.1}
\]

are compatible with (2.1).  Their cofinal generic value is

\[
 \sigma_{\eta,\eta}(s_1,s_2)=\xi(s_1)\xi(s_2).
 \tag{3.2}
\]

This is the external product of the curve-level determinant section,
not a two-variable zeta function introduced by definition.

## 4. Diagonal pullback

The spatial diagonal has

\[
 \delta^{-1}(U_S\boxtimes U_T)=U_{S\cup T},
\]

and the spectral diagonal is \(s\mapsto(s,s)\).  Functoriality of
external products gives

\[
 \delta^*\mathscr L^\square\simeq\mathscr L^{\otimes2},
 \qquad
 \delta^*\sigma_{\eta,\eta}(s)=\xi(s)^2.
 \tag{4.1}
\]

On the chart \((S,T)\), the accumulated finite factor is

\[
 g_S(s)g_T(s).
 \tag{4.2}
\]

If a prime belongs to both sets it occurs twice, exactly as tensor
squaring requires.  Different presentations with the same union are
identified by the unit transition maps; one must not replace (4.2) by
\(g_{S\cup T}\), which would erase tensor multiplicity.

## 5. Rational-Frobenius spectral specialization

For coprime \(n,m>0\), the analytic map

\[
 \iota_{n,m}:\mathcal H\longrightarrow\mathcal H^2,
 \qquad s\longmapsto(ns,ms)
\]

pulls the local factor to

\[
 z_p(ns)z_p(ms)
 ={1\over(1-p^{-ns})(1-p^{-ms})},
 \tag{5.1}
\]

and the completed generic section to

\[
 \xi(ns)\xi(ms).
 \tag{5.2}
\]

This is compatible with the two spectral weights of the source square,
but it is **not** the algebraic correspondence
\(\Lambda_{n,m}:X^aY^b\mapsto T^{na+mb}\) of `107_163`.  In particular,
(5.1) is generally not \(z_p((n+m)s)\).  Therefore spectral
specialization alone does not construct the graph class, its diagonal
intersection, or a top-degree trace.

## 6. Exact scope

The result constructs the external-product determinant line and its
diagonal pullback on an actual product site.  It closes the sheaf-theoretic
square descent problem for this spectral line.

It does not construct:

1. a proper two-dimensional arithmetic or absolute space;
2. a codimension-one diagonal or Frobenius cycle;
3. a Deligne pairing or top class;
4. a Green current on that square;
5. an intersection number or Hodge-index form.

The next load-bearing problem is therefore a top-degree pairing that
retains the uncancelled local inverse-Euler terms.  Additional tensor
products of the present line cannot solve that problem by themselves.

## 7. Falsifier

The verifier tests two-dimensional restriction functoriality, commuting
row/column maps, Cech equalizers in each coordinate, diagonal tensor
multiplicity, canonical-section compatibility, and the distinction
between (5.1) and a fictitious \(z_p((n+m)s)\).  It can return `NO` for
any failed descent or for accidental collapse of the two spectral
weights.
