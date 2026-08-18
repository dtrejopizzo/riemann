# Turán--Riccati coupling: exact identity and moment-level obstruction

## Purpose

This note keeps the completed theta measure intact and tests the coupled
quantity
\[
 T(s)=\xi(s)\xi''(s)-\xi'(s)^2.
\]
It derives the exact coefficient relation between its positive pullback and
the regularised Li coefficients.  The relation supplies true low-order
inequalities, but the same premises hold for the finite off-line measure
from `103_15`; hence they cannot yield an RH proof by themselves.

## 1. Positivity before the conformal pullback

Use the positive even base measure from `103_15`, writing, up to an
irrelevant positive normalisation,
\[
 \xi(s)=\int_{\mathbb R}e^{(s-1/2)u}\,d\mu_0(u).
\]
For real \(s>1/2\), symmetrisation gives
\[
 \boxed{
 T(s)={1\over2}\iint_{\mathbb R^2}(u-v)^2
 e^{(s-1/2)(u+v)}d\mu_0(u)d\mu_0(v)>0.}                              \tag{1}
\]
The measure in \(W=u+v\), weighted by \((u-v)^2\), is positive and even.
Pairing \(W\) with \(-W\) shows directly that
\[
 T^{(k)}(s)>0\qquad(k\ge0,\ s>1/2).                                \tag{2}
\]

## 2. Exact Riccati identity in the disk

Fix \(a=1+\varepsilon>1\), put \(s(z)=a/(1-z)\), and normalize
\[
 H(z)={\xi(s(z))\over\xi(a)},\qquad
 L(z)={H'(z)\over H(z)}=\sum_{m\ge1}\lambda_m(\varepsilon)z^{m-1}.
\]
Since \(L=(\xi'/\xi)(s)s'\), differentiation and
\(s''/s'=2/(1-z)\) give
\[
 L'-{2\over1-z}L
 =\left({\xi''\over\xi}-\left({\xi'\over\xi}\right)^2\right)(s)
 (s')^2.
\]
Equivalently,
\[
 \boxed{
 P_a(z):={a^2T(s(z))\over\xi(a)^2}
 =(1-z)^4H(z)^2
 \left(L'(z)-{2\over1-z}L(z)\right).}                              \tag{3}
\]
By (2), the Taylor coefficients of \(P_a\) are strictly positive: first
expand \(T(a+w)\) with positive derivatives and then substitute
\(w=az/(1-z)\), which has positive coefficients.

## 3. The first three coefficient inequalities

Put
\[
 r_n=n\lambda_{n+1}(\varepsilon)-2\sum_{j=1}^n\lambda_j(\varepsilon).
\]
Then \(R(z):=L'-2L/(1-z)=\sum_{n\ge1}r_nz^{n-1}\).  If
\(P_a(z)=\sum_{j\ge0}p_jz^j\), (3) gives
\[
 p_0=r_1,
\]
\[
 p_1=r_2+(2b_1-4)r_1,
\]
\[
 p_2=r_3+(2b_1-4)r_2+
       (2b_2+b_1^2-8b_1+6)r_1,                                      \tag{4}
\]
where \(H=1+b_1z+b_2z^2+\cdots\).  In particular
\[
 b_1=\lambda_1,\qquad b_2={\lambda_2+\lambda_1^2\over2},
\]
so (4) is an explicit set of inequalities involving respectively
\(\lambda_2\), \(\lambda_3\), and \(\lambda_4\).  For example,
\[
 p_0=\lambda_2-2\lambda_1>0.                                      \tag{5}
\]
Equations (3)--(5) are exact; no zero location, prime estimate, or limiting
interchange is used.

They do not yield an induction for the \(\lambda_n\).  Solving (3) for
\(R\) requires division by \((1-z)^4H^2\).  Although \(H\) has positive
coefficients, the coefficients of both \((1-z)^{-4}\) and \(H^{-2}\)
interact with signs after this division; `103_15` already proves that even
the stronger log-convexity condition that would control such an inverse is
false.  Thus positivity of \(p_j\) does not determine the sign of \(r_j\),
and hence does not determine the next \(\lambda_{j+1}\).

## 4. Off-line audit

Take the finite positive even measure \(\nu_q\) of `103_15` and its
transform \(X_q(s)\).  The double-integral proof (1)--(2), and hence the
positive-coefficient identity (3), apply verbatim with \(\xi\) replaced by
\(X_q\).  But `103_15` proves that \(X_q\) has zeros off the critical line
for every \(0<q<1/2\).

Therefore a proof using only the positivity of \(T\), its derivatives,
the Riccati identity, and ordinary Hankel/Turán variance inequalities would
also apply to \(X_q\) and cannot establish RH.  These statements are
second-moment information for the tilted theta measure.  A successful
coupling would need an arithmetic property not shared by \(\nu_q\), for
example a nontrivial use of the Euler factors beyond the positive moment
identities.

## Status

The Riccati/Turán coupling is exact and gives the valid inequalities (4)--(5),
but it is not an A1 induction.  The finite off-line measure is an algebraic
counterexample to any conclusion drawn solely from this moment-level
positivity.
