# 106.188 — A nuclear Euler trace domain for Kronecker restriction

## 1. Purpose

The Kronecker restriction of 106.187 is not closable from the unweighted
Euler--Bohr space to the continuous Cauchy spectral space.  This note
constructs a stronger source domain directly from prime valuations.

The construction uses the total multiplicative variation of a rational
number.  Its partition function is an elementary Euler product, and it
makes the restriction Hilbert--Schmidt.  The resulting operator has dense,
nonclosed range and therefore gives a concrete positive torsion object
rather than a zero reduced cokernel.  It has exact covariance under
translation of the Kronecker spectral parameter and uses no zeta zero.
Section 5 separates that covariance from the actual CCM scaling action;
the latter remains only discrete on the coefficient domain.

## 2. Multiplicative variation

Index the character group of the prime torus by

\[
 \mathbf n=(n_p)_p\in\bigoplus_p\mathbb Z,\qquad
 q(\mathbf n)=\prod_pp^{n_p}.                               \tag{1}
\]

Define

\[
 L(\mathbf n)=\log q(\mathbf n)=\sum_pn_p\log p             \tag{2}
\]

and the Euler variation

\[
 \boxed{
 \ell_E(\mathbf n)=\sum_p|n_p|\log p.}                      \tag{3}
\]

If \(q=a/b\) in lowest terms, then

\[
 \ell_E(q)=\log a+\log b=\log(ab),\qquad
 |\log q|\le\ell_E(q).                                     \tag{4}
\]

### Lemma 2.1 — Exact variation partition function

For \(s>1\),

\[
 \boxed{
 Z_E(s):=\sum_{\mathbf n}e^{-s\ell_E(\mathbf n)}
 =\prod_p\frac{1+p^{-s}}{1-p^{-s}}
 =\frac{\zeta(s)^2}{\zeta(2s)}<\infty.}                    \tag{5}
\]

#### Proof

Finite support of \(\mathbf n\) and monotone convergence give

\[
 \sum_{\mathbf n}e^{-s\ell_E(\mathbf n)}
 =\prod_p\left(\sum_{k\in\mathbb Z}p^{-s|k|}\right)
 =\prod_p\frac{1+p^{-s}}{1-p^{-s}}.                         \tag{6}
\]

Since \((1+x)/(1-x)=(1-x^2)/(1-x)^2\), Euler products give the last
identity in (5).  Convergence follows for \(s>1\). \(\square\)

Only the absolutely convergent Euler product is used in this lemma.

## 3. The Hilbert scale and its nuclear core

Fix

\[
 c>\frac12.                                                  \tag{7}
\]

For \(m\ge0\), define

\[
 \mathscr H_m^{(c)}=
 \left\{a=(a_{\mathbf n}):
 \|a\|_{m,c}^2
 =\sum_{\mathbf n}|a_{\mathbf n}|^2
    e^{2mc\ell_E(\mathbf n)}<\infty\right\}.               \tag{8}
\]

Let

\[
 \boxed{
 \mathscr D_E^{(c)}=\bigcap_{m\ge0}\mathscr H_m^{(c)}}      \tag{9}
\]

with its projective-limit topology.

### Theorem 3.1 — Nuclearity

The Fréchet space \(\mathscr D_E^{(c)}\) is nuclear.  More precisely,
every inclusion

\[
 \mathscr H_{m+1}^{(c)}\hookrightarrow\mathscr H_m^{(c)}   \tag{10}
\]

is Hilbert--Schmidt.

#### Proof

Relative to the normalized coordinate bases, the singular value at
\(\mathbf n\) of (10) is \(e^{-c\ell_E(\mathbf n)}\).  Its squared
Hilbert--Schmidt norm is

\[
 \sum_{\mathbf n}e^{-2c\ell_E(\mathbf n)}=Z_E(2c)<\infty    \tag{11}
\]

by Lemma 2.1 and \(2c>1\).  A countably Hilbert projective limit with
Hilbert--Schmidt bonding maps is nuclear. \(\square\)

## 4. Closed Kronecker trace on the weighted domain

Let \(\nu_C\) be the Cauchy probability measure of 106.187.  On finitely
supported sequences define

\[
 (\mathcal R_ca)(\xi)
 =\sum_{\mathbf n}a_{\mathbf n}e^{i\xi L(\mathbf n)}.        \tag{12}
\]

### Theorem 4.1 — Hilbert--Schmidt restriction

The map (12) extends uniquely to a Hilbert--Schmidt operator

\[
 \boxed{
 \mathcal R_c:\mathscr H_1^{(c)}
 \longrightarrow L^2(\mathbb R,\nu_C).}                    \tag{13}
\]

It satisfies

\[
 \|\mathcal R_c\|_{\mathfrak S_2}^2=Z_E(2c).               \tag{14}
\]

#### Proof

The vectors

\[
 e_{\mathbf n}^{(c)}=e^{-c\ell_E(\mathbf n)}\delta_{\mathbf n}
                                                                    \tag{15}
\]

form an orthonormal basis of \(\mathscr H_1^{(c)}\).  Since
\(|e^{i\xi L(\mathbf n)}|=1\),

\[
 \|\mathcal R_ce_{\mathbf n}^{(c)}\|_{L^2(\nu_C)}^2
 =e^{-2c\ell_E(\mathbf n)}.                                 \tag{16}
\]

Summing (16) and using (11) proves (13)--(14). \(\square\)

Thus the same algebraic restriction which was nonclosable in the flat
Euler norm becomes compact and closed after source-side nuclear
regularization.

### Proposition 4.2 — Smooth trace on the nuclear core

For every \(k\ge0\), termwise differentiation gives a continuous map

\[
 \partial_\xi^k\mathcal R_c:
 \mathscr D_E^{(c)}\longrightarrow L^2(\nu_C),              \tag{17}
\]

with

\[
 \partial_\xi^k(\mathcal R_ca)(\xi)
 =\sum_{\mathbf n}(iL(\mathbf n))^k
   a_{\mathbf n}e^{i\xi L(\mathbf n)}.                      \tag{18}
\]

#### Proof

By (4), \(|L(\mathbf n)|^k\le\ell_E(\mathbf n)^k\).  For every
\(\varepsilon>0\), the polynomial factor is bounded by
\(C_{k,\varepsilon}e^{\varepsilon\ell_E(\mathbf n)}\).  Choose two
successive Hilbert weights in (9) with exponential gap larger than
\(\varepsilon\), and repeat the Hilbert--Schmidt calculation of Theorem
4.1. \(\square\)

## 5. Kronecker-parameter covariance versus CCM scaling

Define on coefficient sequences

\[
 (V_ta)_{\mathbf n}=e^{itL(\mathbf n)}a_{\mathbf n},
 \qquad t\in\mathbb R,                                      \tag{19}
\]

and on the target

\[
 (S_tf)(\xi)=f(\xi+t).                                      \tag{20}
\]

### Theorem 5.1 — Strongly continuous parameter covariance

For every \(m\), \(V_t\) is a strongly continuous unitary group on
\(\mathscr H_m^{(c)}\) and preserves \(\mathscr D_E^{(c)}\).  The
translations \(S_t\) form a strongly continuous group of bounded
operators on \(L^2(\nu_C)\), and

\[
 \boxed{
 \mathcal R_cV_t=S_t\mathcal R_c.}                          \tag{21}
\]

#### Proof

The multiplier in (19) has modulus one, so it preserves every norm (8).
Strong continuity follows by dominated convergence on the coefficient
sum.  Equation (21) is the termwise identity

\[
 \sum_{\mathbf n}a_{\mathbf n}e^{itL(\mathbf n)}
 e^{i\xi L(\mathbf n)}
 =\sum_{\mathbf n}a_{\mathbf n}e^{i(\xi+t)L(\mathbf n)}.    \tag{22}
\]

For fixed \(t\), boundedness of \(S_t\) follows because the Cauchy density
\(w_C(\xi)\) satisfies

\[
 \sup_{\xi\in\mathbb R}
 \frac{w_C(\xi-t)}{w_C(\xi)}<\infty.                         \tag{22a}
\]

Strong continuity follows first on compactly supported continuous
functions and then by density.  Equation (21) extends from finite
sequences by boundedness. \(\square\)

The target translations are not unitary for the Cauchy metric.  The
unitary translation group on the same \(L^2\) space is

\[
 (\widetilde S_tf)(\xi)
 =\left(\frac{w_C(\xi+t)}{w_C(\xi)}\right)^{1/2}f(\xi+t).
                                                                    \tag{22b}
\]

The Radon--Nikodym factor in (22b) is nonconstant, so
\(\mathcal R_cV_t=\widetilde S_t\mathcal R_c\) is false.

More importantly, \(S_t\) translates the spectral parameter \(\xi\); it
is not the CCM scaling representation.  Scaling acts in Mellin spectral
coordinates by

\[
 (M_tf)(\xi)=e^{it\xi}f(\xi),                                \tag{22c}
\]

which is unitary for every spectral measure.  For
\(\mathbf r\in\bigoplus_p\mathbb Z\), define the coefficient shift

\[
 (W_{\mathbf r}a)_{\mathbf n}=a_{\mathbf n-\mathbf r}.       \tag{22d}
\]

Then

\[
 \boxed{
 \mathcal R_cW_{\mathbf r}
 =M_{L(\mathbf r)}\mathcal R_c.}                             \tag{22e}
\]

The reverse triangle inequality for \(\ell_E\) shows that
\(W_{\mathbf r}\) is bounded and invertible on every
\(\mathscr H_m^{(c)}\), with norm at most
\(e^{mc\ell_E(\mathbf r)}\).  It is unitary only for \(m=0\), precisely
the flat norm in which restriction is not closable.  Moreover there is no
coefficient shift corresponding to a general \(t\in\mathbb R\setminus G\),
because \(G+t\ne G\).

Thus the nuclear domain repairs closability at the exact price of losing
unitary continuous CCM scaling.  The two defects are dual:

\[
 \begin{array}{c|c|c}
 \text{source norm}&\text{Kronecker restriction}&\text{CCM scale}\\ \hline
 m=0&\text{not closable}&\text{unitary for }G\\
 m\ge1&\text{Hilbert--Schmidt}&\text{bounded, nonunitary for }G
 \end{array}                                                  \tag{22f}
\]

and neither row extends the coefficient shifts to all of \(\mathbb R\).

## 6. Dense nonclosed range: a positive torsion object

### Theorem 6.1 — Exact range type

The operator \(\mathcal R_c\) has infinite-dimensional dense, nonclosed
range in \(L^2(\nu_C)\).

#### Proof

Its range contains every exponential
\(\xi\mapsto e^{ig\xi}\), \(g\in G\).  If
\(h\in L^2(\nu_C)\) is orthogonal to all of them, the finite complex
measure \(h\,d\nu_C\) has Fourier transform zero on the dense subgroup
\(G\).  The transform is continuous, hence zero on all of \(\mathbb R\).
Uniqueness of Fourier transforms of finite measures gives \(h=0\).
Thus the range is dense.

Theorem 4.1 makes \(\mathcal R_c\) compact, and its range is
infinite-dimensional because the exponentials with distinct frequencies
are linearly independent.  A compact operator with closed range has
finite-dimensional range.  Therefore the range is not closed. \(\square\)

Consequently

\[
 \boxed{
 \mathbb T_{\mathcal R_c}
 =\bigl(\mathscr H_1^{(c)}
   \mathop{\longrightarrow}^{\mathcal R_c}L^2(\nu_C)\bigr)} \tag{23}
\]

is an explicit extended Hilbert torsion object.  Its reduced Hilbert
cokernel is zero, but its graph and singular-value filtration are nonzero.
Unlike the object of 106.166, it is defined entirely from prime valuations
and the real Cauchy scale law, not from \(\Xi\).

## 7. Positive double and the scaling defect

Take two copies of the graph Hilbert space and put

\[
 J(u_0,u_1)=(-u_1,u_0),\qquad
 \Omega(u,v)=g(Ju,v),                                       \tag{24}
\]

where \(g\) is the direct-sum graph metric.  Then

\[
 J^2=-I,\qquad
 \Omega(u,Jv)=g(u,v)>0,                                     \tag{25}
\]

and \(J\) is a positive compatible complex structure on the doubled graph.
The parameter-translation action induced by (19)--(20) commutes
algebraically with \(J\), but it is not unitary for the graph metric.
The actual scaling action (22c) is unitary on the target, while its
coefficient lifts (22d) are nonunitary and exist only for the dense
subgroup \(G\).

This supplies a positive, source-defined torsion double, but not yet a
real-scale-equivariant polarization of CCM degree one.  The relative
Gamma/polar construction must simultaneously retain the nuclear trace
regularity and produce a unitary extension of (22e) to all real scales.

## 8. What remains for CCM descent

The construction closes the closability problem isolated in 106.187: the
source domain is nuclear, the Kronecker restriction is compact, and its
range is dense nonclosed.  It also converts the scale problem into the
explicit incompatibility table (22f).

It does not yet identify its torsion cokernel with the CCM cyclic cokernel.
Two additional structures are required:

1. the Gamma and polar boundary maps must be added to \(\mathcal R_c\) in
   the relative Fourier--Weyl mixed complex so that the discrete bounded
   shifts (22d) descend to the unitary real action (22c);
2. the resulting Green boundary form must agree with the already descended
   alternating form \(\Omega_{\rm CCM}\) and be strongly nondegenerate in
   the graph metric.

The first is now a concrete operator-extension problem rather than an
unspecified search for a norm.  The finite-prime part and its cofinal
regularity have explicit formulas (3), (8), and (12).

## 9. Status

Proved without RH or zero input:

* the exact Euler-variation partition function;
* a nuclear prime-support-sensitive source domain;
* Hilbert--Schmidt and smooth Kronecker restriction;
* exact Kronecker-parameter covariance, exact discrete scaling
  intertwining, and the explicit obstruction to unitary real scaling;
* dense nonclosed range and the resulting positive torsion object;
* a compatible positive doubled graph form.

Still required:

* insertion of the Gamma/polar boundary into the relative mixed-complex
  differential and construction of the unitary real-scale extension;
* identification of the resulting degree-one torsion object with the
  nonreduced CCM cokernel;
* bounded strong nondegeneracy of the descended CCM alternating form.
