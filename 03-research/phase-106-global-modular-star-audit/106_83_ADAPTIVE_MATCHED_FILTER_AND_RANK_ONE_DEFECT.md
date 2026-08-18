# 106.83 — Adaptive matched filters and the rank-one resolvent defect

## Purpose and conclusion

Documents 106.80--106.82 isolate one adaptive negative direction rather
than an arbitrary negative subspace.  This note extracts the additional
algebra carried by that direction.

Let

\[
 H_0=\begin{pmatrix}A&c\\c^*&h\end{pmatrix},
 \qquad A\succ0,
 \qquad
 \sigma_0=h-c^*A^{-1}c=-\delta<0.                 \tag{1}
\]

For a finite literal prime block, let \(U\) be the old-mode observation
map, \(v\) the new-mode observation, and

\[
 a=A^{-1}c,\qquad r=v-Ua.                         \tag{2}
\]

The exact block gain is

\[
 \Delta=r^*(I+UA^{-1}U^*)^{-1}r.                 \tag{3}
\]

Two new exact reductions follow.

First, if \(S=[\,U\ \ v\,]\), then

\[
 \boxed{
 UA^{-1}U^*-SH_0^{-1}S^*
 =\frac{rr^*}{\delta}\succeq0.}                  \tag{4}
\]

Thus the difference between the positive old regression and the full
indefinite regression is a positive rank-one operator.  Crossing is the
dimensionless trace condition

\[
 \boxed{
 \sigma_0+\Delta>0
 \quad\Longleftrightarrow\quad
 \mathrm{Tr}\,\!\left[
 (I+UA^{-1}U^*)^{-1}\frac{rr^*}{\delta}
 \right]>1.}                                    \tag{5}
\]

Second, the gain has a matched-filter variational formula.  Every
nonzero observation-space vector \(\omega\) gives

\[
 \boxed{
 \Delta\ge
 \frac{|\langle\omega,r\rangle|^2}
 {\|\omega\|^2+\|A^{-1/2}U^*\omega\|^2}.}        \tag{6}
\]

Taking \(\omega=v\) produces a completely explicit one-filter
certificate.  It retains a substantial part of the exact gain in the
stable finite diagnostics and crosses every displayed negative row.

The result does not yet prove the cofinal arithmetic inequality.  It
removes another unnecessary demand: one need not construct a full prime
frame or invert the observation covariance.  It is enough to exhibit one
literal prime-block combiner whose new-mode response dominates its
\(A^{-1}\)-priced leakage and the scalar deficit.

## 1. Equations satisfied by the adaptive residual

In the ordered basis
\((\phi_1,\ldots,\phi_{M-1},\phi_M)\), put

\[
 x_*=\binom{-a}{1},
 \qquad
 q^*=\sum_{j=1}^M(x_*)_j\phi_j.                  \tag{7}
\]

### Proposition 1 — Source equation and regression budget

The adaptive residual satisfies

\[
 \boxed{H_0x_*=\sigma_0e_M,}                     \tag{8}
\]

and hence

\[
 \boxed{
 \mathcal A_0(w,q^*)
 =\sigma_0\,\overline{\ell_M(w)}
 \qquad(w\in V_M),}                              \tag{9}
\]

where \(\ell_M\) is the last coefficient functional.  In particular,

\[
 \mathcal A_0(w,q^*)=0\quad(w\in V_{M-1}),       \tag{10}
\]

\[
 \mathcal A_0(q^*,q^*)=\sigma_0=-\delta,         \tag{11}
\]

and

\[
 \mathcal A_0(q^*+w,q^*+w)
 =-\delta+\mathcal A_0(w,w)
 \quad(w\in V_{M-1}).                            \tag{12}
\]

Moreover,

\[
 \boxed{
 a^*Aa=c^*A^{-1}c=h+\delta.}                     \tag{13}
\]

#### Proof

The first \(M-1\) entries of \(H_0x_*\) are
\(-Aa+c=0\), while the last entry is
\(h-c^*a=\sigma_0\).  This proves (8), and (9)--(12)
follow by polarization.  Equation (13) follows from (1). \(\square\)

For the literal finite head, (11) reads

\[
 \boxed{
 \delta
 =\frac12\|q^*\|_{\mu_K}^2-\mathscr E_\Gamma(q^*)
 -\sum_{p^k\le X_0}\frac{\log p}{p^{k/2}}
   \mathcal J_{k\log p}(q^*).}                  \tag{14}
\]

Thus the deficit is already a jointly centered prime--Gamma quantity.

## 2. The rank-one resolvent-defect identity

### Theorem 2 — Positive rank-one defect

Identity (4) holds.

#### Proof

Block inversion of (1) gives

\[
 H_0^{-1}
 =
 \begin{pmatrix}
 A^{-1}+aa^*/\sigma_0&-a/\sigma_0\\
 -a^*/\sigma_0&1/\sigma_0
 \end{pmatrix}.                                  \tag{15}
\]

Multiplying on the left and right by \(S=[\,U\ \ v\,]\) and \(S^*\)
gives

\[
\begin{aligned}
 SH_0^{-1}S^*
 &=UA^{-1}U^*
   +\frac{(Ua-v)(Ua-v)^*}{\sigma_0}\\
 &=UA^{-1}U^*-\frac{rr^*}{\delta}.
\end{aligned}                                    \tag{16}
\]

Rearrangement proves (4). \(\square\)

Put

\[
 B=UA^{-1}U^*,
 \qquad
 C=B-SH_0^{-1}S^*=\frac{rr^*}{\delta}.           \tag{17}
\]

Then

\[
 \Delta
 =\delta\,\mathrm{Tr}((I+B)^{-1}C),       \tag{18}
\]

which proves (5).  The directional estimate of 106.81 gives the
dimensionless sufficient condition

\[
 \boxed{
 (\mathrm{Tr}\,C)^2
 >\mathrm{Tr}\,C+\mathrm{Tr}(BC).}   \tag{19}
\]

Indeed, substituting
\(\mathrm{Tr}\,C=\|r\|^2/\delta\) and
\(\mathrm{Tr}(BC)=
\|A^{-1/2}U^*r\|^2/\delta\)
reduces (19) to

\[
 \|r\|^4>
 \delta\bigl(\|r\|^2+\|A^{-1/2}U^*r\|^2\bigr).   \tag{20}
\]

## 3. Matched-filter duality

### Theorem 3 — One-combiner lower bound

For every nonzero observation vector \(\omega\), (6) holds.

#### Proof

For \(M_B=I+UA^{-1}U^*\succ0\), Cauchy--Schwarz gives

\[
 |\langle\omega,r\rangle|^2
 =|\langle M_B^{1/2}\omega,M_B^{-1/2}r\rangle|^2
 \le
 \langle\omega,M_B\omega\rangle
 \langle r,M_B^{-1}r\rangle.                    \tag{21}
\]

The second factor is \(\Delta\), and

\[
 \langle\omega,M_B\omega\rangle
 =\|\omega\|^2+\|A^{-1/2}U^*\omega\|^2.
\]

Division proves (6).  Equality is attained for
\(\omega=(I+B)^{-1}r\). \(\square\)

Let

\[
 T=UA^{-1/2},
 \qquad
 z=A^{1/2}a,
 \qquad
 \|z\|^2=h+\delta.                               \tag{22}
\]

Since \(r=v-Tz\), the triangle inequality in (6) yields

\[
 \boxed{
 \Delta\ge
 \frac{
 \bigl(
 |\langle\omega,v\rangle|
 -\sqrt{h+\delta}\,\|T^*\omega\|
 \bigr)_+^2}
 {\|\omega\|^2+\|T^*\omega\|^2}.}                \tag{23}
\]

Consequently a block crosses whenever one can construct \(\omega\) with

\[
 \boxed{
 |\langle\omega,v\rangle|
 >
 \sqrt{h+\delta}\,\|T^*\omega\|
 +\sqrt{\delta\bigl(\|\omega\|^2+\|T^*\omega\|^2\bigr)}.}       \tag{24}
\]

This is the precise prime-block matched-filter target.

## 4. The explicit new-mode filter

Choose \(\omega=v\), and write

\[
 e=\|v\|^2,
 \qquad
 p=U^*v.                                          \tag{25}
\]

Equation (6) becomes

\[
 \boxed{
 \Delta\ge
 \Delta_{\rm new}
 :=
 \frac{|e-p^*a|^2}{e+p^*A^{-1}p}.}               \tag{26}
\]

Therefore the elementary scalar inequality

\[
 \boxed{
 |e-p^*A^{-1}c|^2
 >
 \delta\bigl(e+p^*A^{-1}p\bigr)}                 \tag{27}
\]

is sufficient for a finite crossing.

For the projected midpoint block of 106.81,

\[
 v_p=-\sqrt{\beta_p}
 \{A_p(\phi_M)+\rho_p(\phi_M)\},                 \tag{28}
\]

and the entries of \(p\) are the corresponding weighted correlations
with the old mode rows.  Hence every term in (27) is a finite sum with the
literal ordinary-prime weights.

## 5. Diagnostic

The script

\[
\texttt{python3 tools/augmented\_gain\_spectral\_diagnostic.py
--dx 0.0005 --span 20}
\]

evaluates (26) using the complete finite-block displacement Grams.  The
following rows are floating-point diagnostics, not interval
certificates.

\[
\begin{array}{c|c|r|r|r|r}
M&X_0\to X_1&-\sigma_0&\Delta&
\Delta_{\rm new}&\Delta_{\rm new}/\Delta\\ \hline
4&1\to2&2.105\,10^{-1}&3.944\,10^{-1}&
2.172\,10^{-1}&0.551\\
7&2\to3&1.343\,10^{-2}&8.648\,10^{-2}&
5.020\,10^{-2}&0.580\\
12&3\to4&2.290\,10^{-2}&5.014\,10^{-2}&
4.014\,10^{-2}&0.801\\
16&4\to5&1.316\,10^{-2}&2.551\,10^{-2}&
1.815\,10^{-2}&0.711
\end{array}                                                    \tag{29}
\]

The explicit new-mode filter crosses in all four stable negative rows.
It is weaker than the adaptive residual filter of 106.81, but requires
only the scalar block data \(e,p,A,c\).

## 6. Exact block-strength flow

Scale the new block by \(t\in[0,1]\):

\[
\begin{aligned}
 A_t&=A+tU^*U,& c_t&=c+tU^*v,\\
 h_t&=h+t\|v\|^2,& a_t&=A_t^{-1}c_t,\\
 r_t&=v-Ua_t,&
 \sigma_t&=h_t-c_t^*A_t^{-1}c_t.
\end{aligned}                                                   \tag{30}
\]

Direct differentiation gives

\[
 \boxed{
 a_t'=A_t^{-1}U^*r_t,
 \qquad
 r_t'=-UA_t^{-1}U^*r_t,}                         \tag{31}
\]

\[
 \boxed{
 \sigma_t'=\|r_t\|^2,
 \qquad
 \sigma_t''=-2\|A_t^{-1/2}U^*r_t\|^2\le0.}       \tag{32}
\]

Thus the innovation is increasing and concave in block strength.  Its
exact increment is

\[
 \boxed{
 \sigma_1-\sigma_0
 =\int_0^1\|r_t\|^2\,dt
 =r^*(I+UA^{-1}U^*)^{-1}r.}                     \tag{33}
\]

The curvature in (32) is quadratic in the prime observation map.  Its
literal expansion is a positive two-index Gram form, but the two indices
remain separate: the kernel contains the preceding resolvent \(A_t^{-1}\)
and does not collapse to a Dirichlet-convolution fibre indexed by a product
\(mn\).  Thus (32) does **not** by itself identify the curvature with
\(\Lambda*\Lambda\), nor does coefficientwise positivity of
\(j_2=\delta\Lambda+\Lambda*\Lambda\) determine its sign relative to the
linear deficit.  The exact Stieltjes reduction and this distinction are
recorded in 106.85.

## 7. Remaining arithmetic theorem

The construction has reduced the next step to either of two explicit
inequalities for a suitable finite ordinary-prime block:

\[
 \|r\|^4>
 \delta\bigl(\|r\|^2+\|A^{-1/2}U^*r\|^2\bigr),    \tag{34}
\]

or the stronger-to-check but simpler new-mode certificate (27).

Both preserve:

* the adaptive normal equation (9);
* the already accumulated prime--Gamma coercivity \(A\);
* the literal theta apertures and all ordinary-prime weights;
* the signed deficit \(\delta\) before taking an absolute value.

The next calculation must control the adaptive spectral measure of
\(UA^{-1}U^*\) against the deficit identity (14).  Coefficient positivity
of \(j_2\) by itself is not enough; the required statement is a signed
adaptive scalar inequality after the prime, Gamma, and threshold
contributions have been centered jointly.
