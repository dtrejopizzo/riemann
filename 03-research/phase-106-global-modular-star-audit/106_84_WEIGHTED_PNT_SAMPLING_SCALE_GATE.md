# 106.84 — Weighted PNT sampling and the theta-scale gate

## Purpose and conclusion

The scalar midpoint target of 106.81 asks whether the adaptive signed
residual \(q^*\) keeps enough ordinary-prime response before the Riemann
theta overlap becomes too small.  This note proves the part of that
statement which follows from exponential-polynomial sampling and the prime
number theorem.

Fix a finite elementary spectral block \(\mathcal Z\), including confluent
jets of order at most \(J\), and suppose

\[
 |\operatorname {Im}z|\le b<\frac12
 \qquad(z\in\mathcal Z).                           \tag{1}
\]

For every fixed relative width \(\delta>0\), there are effective constants
\(c_{\mathcal Z,\delta}>0\) and
\(X_{\mathcal Z,\delta}<\infty\) such that, for every \(q\) in the block
and every \(X\ge X_{\mathcal Z,\delta}\),

\[
 \boxed{
 \sum_{X<p\le(1+\delta)X}\log p\,
 |A_p(q)+\rho_p(q)|^2
 \ge
 c_{\mathcal Z,\delta}
 X^{1-b}(1+\log X)^{-2J}\|q\|_{\rm coeff}^2.}     \tag{2}
\]

Thus the actual ordinary primes sample every fixed residual block with a
quantitative lower bound; this is stronger than qualitative
nonvanishing.  Inserting the physical theta strength

\[
 \beta_p=C_\Xi^2\pi^3(\log p)p^2e^{-2\pi p}
 (1+p^{-1/2})^{-2}                                \tag{3}
\]

gives

\[
 \boxed{
 \sum_{X<p\le(1+\delta)X}\beta_p
 |A_p(q)+\rho_p(q)|^2
 \ge
 c'_{\mathcal Z,\delta}
 X^{3-b}(1+\log X)^{-2J}
 e^{-2\pi(1+\delta)X}\|q\|_{\rm coeff}^2.}       \tag{4}
\]

The old-mode denominator in the regularized crossing certificate obeys

\[
 \boxed{
 \|S_0\|^2
 \le C_{\mathcal Z}
 X^{2+b}(1+\log X)^{2J+1}e^{-2\pi X}.}            \tag{5}
\]

Equations (4)--(5) give a completely finite sufficient crossing test.
They also expose the exact scale obstruction of this method.  The natural
theta tail begins at scale \(e^{-2\pi X}\), whereas locating the phase
energy only somewhere in a relative PNT block costs

\[
 e^{-2\pi(1+\delta)X}
 =e^{-2\pi X}\,e^{-2\pi\delta X}.                \tag{6}
\]

The extra \(e^{-2\pi\delta X}\) is not recovered by Remez or Turan
inequalities on the same relative interval: those inequalities redistribute
exponential-polynomial mass inside the interval, while the theta weight
changes exponentially in the ordinary-prime variable.  Consequently the
result proves finite quantitative sampling, but it does not by itself show
that the sampled energy exceeds the signed Schur deficit.  Closing the row
requires either a tail-matched bound for that particular deficit, or a
short-window estimate tied to the first available prime responses of the
adaptive residual.

## 1. Prior-route audit

The following earlier results are directly relevant.

* Phase 25 and Phase 37 audit Turan power sums as detectors of an
  exponential mode.  They do not provide a theta-weighted lower frame
  bound.
* Phase 47 proves that irrational prime phases do not give a uniform
  unweighted Riesz lower bound.  Near collisions persist at arbitrarily
  high frequency.
* Document 106.73 proves the exact midpoint asymptotic, the strength (3),
  and the upper tail
  \(O((\log X)X^{2+b}e^{-2\pi X})\) on a fixed block.  It also shows that
  Vandermonde nonvanishing alone cannot cancel the theta envelope.
* Document 106.82 proves that a fixed finite collection of scalar midpoint
  rows cannot control every vector in a negative space of larger index.
  The present theorem instead applies to a fixed finite spectral block and
  uses a whole relative interval of ordinary primes.
* Document 106.83 identifies the special adaptive direction and its
  matched-filter certificate.  The estimate below can be inserted into
  that certificate, but it does not use the adaptive normal equation and
  hence cannot compare its output with the deficit automatically.

The new statement here is the ordinary-prime lower mean-square estimate
(2), including confluent jets and the additive midpoint error, followed by
the exact conversion to the physical theta scale in (4).

## 2. The leading exponential polynomial

Use coefficient coordinates in the elementary mode basis

\[
 \chi_{z,k}(t)=\partial_z^k
 \left(\frac{\cos(zt)}{\cosh(t/2)}\right),
 \qquad 0\le k\le J.                              \tag{7}
\]

For an un-jetted mode, 106.73 gives

\[
 A_p(z)=2z\sin(zt_p)+\tanh(t_p/2)\cos(zt_p),
 \qquad t_p=\frac12\log p.                       \tag{8}
\]

Replace \(\tanh(t/2)\) temporarily by \(1\), and put

\[
 \widetilde A(z,t)=2z\sin(zt)+\cos(zt).           \tag{9}
\]

Its exponential form is

\[
 \widetilde A(z,t)
 =\frac{1-2iz}{2}e^{izt}
  +\frac{1+2iz}{2}e^{-izt}.                       \tag{10}
\]

Neither coefficient in (10) vanishes in the open strip
\(|\operatorname {Im}z|<1/2\).  Differentiating in \(z\) shows that the
map from the mode and jet coefficients of \(q\) to the coefficients of

\[
 F_q(t):=\widetilde A(q,t)                        \tag{11}
\]

is triangular on every confluent block, with nonzero diagonal.  It is
therefore invertible.  In particular,

\[
 F_q(t)=\sum_{\nu=1}^{r}P_\nu(t)e^{\lambda_\nu t},
 \qquad
 \deg P_\nu\le J,
 \qquad
 -b\le\operatorname {Re}\lambda_\nu\le b,       \tag{12}
\]

where the \(\lambda_\nu\) are the distinct values \(iz\) and \(-iz\),
with the prescribed confluence.  Moreover there is an explicit constant
\(s_{\mathcal Z}>0\), the least singular value of this finite triangular
coefficient map, such that

\[
 \|\operatorname {coeff}(F_q)\|
 \ge s_{\mathcal Z}\|q\|_{\rm coeff}.            \tag{13}
\]

The exact response differs from (11) in two ways.  First,

\[
 \tanh(t_p/2)-1=-\frac{2}{\sqrt p+1}.             \tag{14}
\]

Second, the normalized aperture calculation of 106.81 gives the additive
error \(\rho_p\).  Equations (1), (14), and the jet derivatives imply the
uniform estimate

\[
 \boxed{
 |A_p(q)+\rho_p(q)-F_q(t_p)|
 \le C_{\mathcal Z}
 p^{(b-1)/2}(1+\log p)^J\|q\|_{\rm coeff}.}       \tag{15}
\]

The \(p^{b/2-1}\) aperture error is smaller than the term displayed in
(15); the loss \(p^{-1/2}\) comes from (14).

## 3. A finite confluent Gram on a relative interval

For each exponent \(\lambda_\nu\) and \(0\le k\le J_\nu\), define

\[
 g_{\nu,k}(s)
 =s^{\lambda_\nu/2}\left(\frac12\log s\right)^k,
 \qquad 1\le s\le1+\delta.                       \tag{16}
\]

After duplicate exponent--jet pairs have been removed, these functions
are linearly independent.  Their continuous Gram matrix

\[
 \mathcal G_{\mathcal Z,\delta}
 =\left[
 \int_1^{1+\delta}
 g_{\nu,k}(s)\overline{g_{\mu,l}(s)}\,ds
 \right]_{(\nu,k),(\mu,l)}                       \tag{17}
\]

is therefore positive definite.  Put

\[
 \gamma_{\mathcal Z,\delta}
 :=\lambda_{\min}(\mathcal G_{\mathcal Z,\delta})>0. \tag{18}
\]

This is a finite, explicitly computable constant.  It incorporates all
frequency gaps and all confluent jets; no separation hypothesis is hidden
in (18).

Write \(p=Xs\).  Expanding

\[
 P_\nu\left(\frac12\log X+\frac12\log s\right)
 X^{\lambda_\nu/2}s^{\lambda_\nu/2}              \tag{19}
\]

in the basis (16) defines an invertible block-triangular coefficient map
\(\mathcal T_X\).  Its diagonal contains \(X^{\lambda_\nu/2}\), and the
inverse polynomial translation has degree at most \(J\).  Hence there is
an explicit \(C_{\mathcal Z,J}\ge1\) such that

\[
 \boxed{
 s_{\min}(\mathcal T_X)
 \ge C_{\mathcal Z,J}^{-1}
 X^{-b/2}(1+\log X)^{-J}.}                       \tag{20}
\]

Combining (13) and (20), the coefficient vector \(d_X(q)\) of
\(F_q(\tfrac12\log(Xs))\) in (16) satisfies

\[
 \|d_X(q)\|
 \ge s_{\mathcal Z}C_{\mathcal Z,J}^{-1}
 X^{-b/2}(1+\log X)^{-J}\|q\|_{\rm coeff}.       \tag{21}
\]

## 4. Ordinary-prime sampling by PNT

Let

\[
 d\vartheta(x)=\sum_p\log p\,\delta_p.           \tag{22}
\]

The prime number theorem says that the rescaled measures

\[
 \frac1X\,d\vartheta(Xs)
\]

converge weakly to \(ds\) on every fixed compact subinterval of
\((0,\infty)\).  Applied to the finitely many products in (17), this gives

\[
 \frac1X\sum_{X<p\le(1+\delta)X}\log p\,
 \mathbf g(p/X)\mathbf g(p/X)^*
 \longrightarrow\mathcal G_{\mathcal Z,\delta}. \tag{23}
\]

Consequently there is a finite \(X_{\rm PNT}\) such that the matrix on
the left of (23) is bounded below by
\(\tfrac12\gamma_{\mathcal Z,\delta}I\).

The threshold is effective once an effective PNT error is fixed.  More
precisely, if

\[
 E_\vartheta(X,\delta)
 :=\sup_{X\le y\le(1+\delta)X}
 \frac{|\vartheta(y)-y|}{X},                     \tag{24}
\]

then integration by parts bounds the operator-norm error in (23) by

\[
 C(\mathcal Z,J,\delta)E_\vartheta(X,\delta).     \tag{25}
\]

It is enough to take \(X_{\rm PNT}\) so that (25) is at most
\(\gamma_{\mathcal Z,\delta}/2\).  Thus all constants in the argument are
finite matrix constants plus one declared effective PNT error.

Using (21) in (23) proves

\[
 \sum_{X<p\le(1+\delta)X}\log p\,|F_q(t_p)|^2
 \ge c_0X^{1-b}(1+\log X)^{-2J}
 \|q\|_{\rm coeff}^2,                            \tag{26}
\]

where one may take

\[
 c_0=\frac{\gamma_{\mathcal Z,\delta}}{2}
 \frac{s_{\mathcal Z}^2}{C_{\mathcal Z,J}^2}.   \tag{27}
\]

## 5. Absorbing the exact aperture error

From (15), the squared error over the same prime block is at most

\[
\begin{aligned}
 &\sum_{X<p\le(1+\delta)X}\log p\,
 |A_p(q)+\rho_p(q)-F_q(t_p)|^2\\
 &\qquad\le
 C_1X^b(1+\log X)^{2J}\|q\|_{\rm coeff}^2.       \tag{28}
\end{aligned}
\]

Here it is enough to use
\(\vartheta((1+\delta)X)-\vartheta(X)=O_\delta(X)\).
Because \(b<1/2\),

\[
 \frac{X^b(1+\log X)^{2J}}
 {X^{1-b}(1+\log X)^{-2J}}
 =X^{2b-1}(1+\log X)^{4J}\longrightarrow0.       \tag{29}
\]

Choose \(X_{\rm err}\) so that the square root of (28) is at most one
half of the square root of (26).  The reverse triangle inequality in the
weighted prime \(\ell^2\) space then gives (2), for example with

\[
 c_{\mathcal Z,\delta}=c_0/4,                    \tag{30}
\]

once \(X\ge\max(X_{\rm PNT},X_{\rm err})\).

This is where the strict strip margin in (1) is used quantitatively.  At
the boundary \(b=1/2\), the power saving in (29) disappears.

## 6. Conversion to the physical theta scale

For \(p\in(X,(1+\delta)X]\), equation (3) gives

\[
 \beta_p
 \ge c_\Xi(\log p)X^2e^{-2\pi(1+\delta)X},
 \qquad
 c_\Xi=C_\Xi^2\pi^3(1+2^{-1/2})^{-2}.           \tag{31}
\]

Multiplying (2) by the common lower factor in (31) proves (4), with

\[
 c'_{\mathcal Z,\delta}=c_\Xi c_{\mathcal Z,\delta}. \tag{32}
\]

For the old-mode matrix in 106.81, the fixed-block pointwise upper bound

\[
 |A_p(\phi_j)+\rho_p(\phi_j)|
 \le C_{\mathcal Z}p^{b/2}(1+\log p)^J           \tag{33}
\]

and \(\|S_0\|^2\le\|S_0\|_{\rm HS}^2\) give

\[
\begin{aligned}
 \|S_0\|^2
 &\le C_{\mathcal Z}
 \sum_{p>X}(\log p)p^{2+b}
 (1+\log p)^{2J}e^{-2\pi p}\\
 &\le C'_{\mathcal Z}
 X^{2+b}(1+\log X)^{2J+1}e^{-2\pi X},           \tag{34}
\end{aligned}
\]

which proves (5).  The last estimate follows by enlarging the prime sum
to the integers and applying the elementary exponential-tail bound.

### Corollary 1 — Explicit finite crossing test

Let \(A\succ0\) and let \(q^*\) be the negative adaptive residual at a
finite head, with \(\sigma_0<0\).  The relative prime block

\[
 \mathcal P_X=\{p:X<p\le(1+\delta)X\}            \tag{35}
\]

crosses the row whenever

\[
 \boxed{
 \frac{
 c'_{\mathcal Z,\delta}
 X^{3-b}(1+\log X)^{-2J}e^{-2\pi(1+\delta)X}
 \|q^*\|_{\rm coeff}^2}
 {1+
 C'_{\mathcal Z}\lambda_{\min}(A)^{-1}
 X^{2+b}(1+\log X)^{2J+1}e^{-2\pi X}}
 >-\sigma_0.}                                    \tag{36}
\]

#### Proof

Insert (4) and (5) in the regularized scalar certificate 106.81(30).
\(\square\)

All quantities in (36) are finite and computable from the selected
spectral block, the preceding positive matrix, a fixed PNT error, and the
ordinary primes in (35).  No zero-location hypothesis is used.

## 7. The scale comparison

On the same fixed spectral block, 106.73 gives the theta-tail upper scale

\[
 \sum_{p\ge X}\beta_p
 |A_p(q)+\rho_p(q)|^2
 \le C_{\mathcal Z}
 (1+\log X)^{2J+1}X^{2+b}e^{-2\pi X}
 \|q\|_{\rm coeff}^2.                            \tag{37}
\]

The lower bound produced by relative-interval sampling is, up to powers
of \(X\) and \(\log X\),

\[
 e^{-2\pi(1+\delta)X}.                            \tag{38}
\]

Therefore the exponential ratio between the proved lower scale and the
available tail scale is

\[
 \boxed{e^{-2\pi\delta X}.}                      \tag{39}
\]

This is the exact envelope mismatch of the PNT/Remez attack.  Taking a
smaller fixed \(\delta\) changes its constant but does not remove it as
\(X\to\infty\).  Allowing \(\delta=\delta(X)\downarrow0\) would require a
prime mean-square theorem on shrinking intervals with enough uniformity
to preserve the confluent Gram (17).  Even the standard effective-PNT
shrinking scales have \(X\delta(X)\to\infty\); the theta conversion then
still loses \(e^{-2\pi X\delta(X)}\).

Remez and Turan estimates do not alter this conclusion when used after
(23).  They can prove that an exponential polynomial is large on a subset
of a logarithmic interval, or at one of finitely many phase locations.
They do not force that location into the \(O(1)\) ordinary-prime window on
which \(e^{-2\pi p}\) is comparable to its value at the first prime.

This does not prove that (36) fails for the adaptive Riemann residual.
It proves precisely what additional information is needed to make this
attack close:

1. a short-window lower estimate for the actual responses of \(q^*\) at
   the first available ordinary primes;
2. or a bound showing that \(-\sigma_0\) is already no larger than the
   right side of (4);
3. or a use of the adaptive source equation 106.83(8) which couples those
   two quantities before the theta envelope is estimated.

The PNT supplies finite quantitative sampling.  The unresolved statement
is the tail-matched adaptive comparison, not observability or
exponential-polynomial nonvanishing.
