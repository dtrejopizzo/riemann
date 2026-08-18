# D.242 — Isolated Sonin self-duality and the exact tangent anomaly

## Verdict

The \(\sigma\)-dependent Euler multipliers of D.240 form an exact analytic
Hilbert-metric path, but they do **not** come from a differentiable family of
self-Fourier local Sonin vectors.  At a finite prime the self-Fourier vector
is isolated and occurs exactly at \(\sigma=\frac12\).

Consequently the proposed localized dual-Euler curvature theorem cannot be
deduced by differentiating a family of Sonin-space isomorphisms: the cited
semilocal Sonin theorem supplies the isomorphism only at the central
normalization.  The first failure of self-duality is nevertheless an
explicit source vector.  This is the correct new boundary channel to test
against the D.190 Douglas residual.

No zero, spectral sign, or RH input is used.

## 1. Radial shell calculation

Let \(\epsilon_j\) be the characteristic function of

\[
 \{x\in\mathbb Q_p:|x|_p=p^j\}.
\]

With the self-dual additive character and Haar measure, the local Fourier
transform satisfies

\[
 \mathcal F_p\epsilon_j
 =p^j(1-p^{-1})\sum_{k\geq0}\epsilon_{-j-k}
   -p^{j-1}\epsilon_{-j+1}.                         \tag{1.1}
\]

For a scalar \(c\), put

\[
 v_c=\epsilon_0-c\epsilon_1.                        \tag{1.2}
\]

Using (1.1) at \(j=0,1\) and collecting shells gives the exact identity

\[
 \boxed{
 \mathcal F_pv_c-v_c
 =(c-p^{-1})\,w_p,
 \qquad
 w_p=\epsilon_0+\epsilon_1
       -(p-1)\sum_{j\leq-1}\epsilon_j .
 }                                                   \tag{1.3}
\]

In particular,

\[
 \mathcal F_pv_c=v_c
 \quad\Longleftrightarrow\quad c=p^{-1}.             \tag{1.4}
\]

This recovers the unique radial Sonin generator
\(\sigma_p=\epsilon_0-p^{-1}\epsilon_1\) of the primary semilocal
construction.

### Proof of (1.3)

Formula (1.1) gives

\[
 \begin{aligned}
 \mathcal F_p\epsilon_0
  &=(1-p^{-1})\sum_{j\leq0}\epsilon_j-p^{-1}\epsilon_1,\\
 \mathcal F_p\epsilon_1
  &=(p-1)\sum_{j\leq-1}\epsilon_j-\epsilon_0.
 \end{aligned}
\]

Subtracting \(\epsilon_0-c\epsilon_1\), the coefficient on every
\(j\leq-1\) shell is
\((p-1)(p^{-1}-c)\), while the coefficients of both
\(\epsilon_0\) and \(\epsilon_1\) are \(c-p^{-1}\).  This is (1.3).

## 2. The Euler deformation

The multiplicative Fourier image of \(v_c\) has numerator

\[
 1-cp^{1/2}p^{-i\tau}.                              \tag{2.1}
\]

To obtain the inverse Euler numerator

\[
 1-p^{-\sigma-i\tau},                              \tag{2.2}
\]

one must take

\[
 c(\sigma)=p^{-\sigma-1/2}.                        \tag{2.3}
\]

Equations (1.4) and (2.3) prove

\[
 \mathcal F_pv_{c(\sigma)}=v_{c(\sigma)}
 \quad\Longleftrightarrow\quad \sigma=\frac12.      \tag{2.4}
\]

Thus the analytic deformation used to compute the logarithmic score leaves
the self-Fourier Sonin locus immediately on either side of the critical
point.

Differentiating (1.3) at \(\sigma=\frac12\) gives the exact tangent anomaly

\[
 \boxed{
 \left.\partial_\sigma
   (\mathcal F_pv_{c(\sigma)}-v_{c(\sigma)})
 \right|_{\sigma=1/2}
 =-\frac{\log p}{p}\,w_p .
 }                                                   \tag{2.5}
\]

The vector \(w_p\) belongs to \(L^2(\mathbb Q_p)\).  With
\(\mathrm{vol}(\mathbb Z_p)=1\),

\[
 \|w_p\|_2^2=2(p-1),\qquad
 \left\|{\log p\over p}w_p\right\|_2^2
 ={2(p-1)(\log p)^2\over p^2}.                     \tag{2.6}
\]

Indeed the shell volumes are
\(\mathrm{vol}(\epsilon_j)=(1-p^{-1})p^j\), and
\(\sum_{j\leq-1}p^j=(p-1)^{-1}\).

There is an additional exact orthogonality which will be needed in the
boundary comparison.  Differentiating (1.3) with respect to \(c\), or
applying \(\mathcal F_p\) twice, gives

\[
 \mathcal F_pw_p=-w_p.                              \tag{2.7}
\]

Thus \(\sigma_p\) and \(w_p\) belong respectively to the \(+1\) and
\(-1\) Fourier eigenspaces, and

\[
 \langle\sigma_p,w_p\rangle=0.                     \tag{2.8}
\]

For the tensor product over a finite set \(S\), the summands of
\(\dot{\mathfrak a}_S\) in (4.1) are mutually orthogonal before the adelic
quotient and support compression.  Indeed two distinct summands contain,
at one prime, the orthogonal pair \((w_p,\sigma_p)\).  Hence

\[
 \|\dot{\mathfrak a}_S\|_2^2
 =\sum_{p\in S}{2(p-1)(\log p)^2\over p^2}
   \prod_{\substack{q\in S\\q\ne p}}\|\sigma_q\|_2^2. \tag{2.9}
\]

Here the same shell-volume calculation gives

\[
 \|\sigma_q\|_2^2
 =(1-q^{-1})+q^{-2}(q-1)=1-q^{-2}.                 \tag{2.10}
\]

The loss of this orthogonality after quotient and support cutoff is
therefore a precisely located boundary effect, rather than an ambiguity in
the local prime channels.

### Multiplicative image of the anomaly

For a radial vector \(\sum_j a_j\epsilon_j\), the quotient map followed by
the multiplicative Fourier transform has multiplier

\[
 \sum_j a_jp^{j(1/2-i\tau)}.                        \tag{2.11}
\]

Apply this to \(w_p\).  With
\(z=p^{-1/2-i\tau}\) and
\(\bar z=p^{-1/2+i\tau}\), geometric summation gives

\[
 \begin{aligned}
 W_p(\tau)
 &=1+pz-(p-1){\bar z\over1-\bar z}\\
 &={p(z-\bar z)\over1-\bar z}.                     \tag{2.12}
 \end{aligned}
\]

The simplification uses \(z\bar z=p^{-1}\).  Therefore the multiplicative
image of the tangent anomaly in (2.5) is

\[
 \boxed{
 -{\log p\over p}W_p(\tau)
 ={\log p\over\sqrt p}\,
 {p^{i\tau}-p^{-i\tau}\over
  1-p^{-1/2+i\tau}} .
 }                                                   \tag{2.13}
\]

Thus the anomaly is a rational Euler-resolvent filter with an
antisymmetric boundary numerator.  It is built from the same denominator
\((I-p^{-1/2}S_{\log p})^{-1}\) as the one-state factors of D.237.  The
new information is that this filter is forced by the first failure of
additive self-duality, rather than chosen from a spectral factorization.

Let \(U_p\) denote multiplication by \(p^{i\tau}\) and
\(r=p^{-1/2}\).  If \(W_{p,-}\) is the exact antisymmetric feature of
D.237,

\[
 W_{p,-}=c_{p,-}(I-rU_p)^{-1}(I-U_p),
 \qquad
 c_{p,-}^2={(\log p)r(1+r)\over2(1-r)},
\]

then (2.13) is equivalently

\[
 \boxed{
 \mathfrak A_p
 =-{\log p\,r\over c_{p,-}}\,
 W_{p,-}(I+U_p^*).
 }                                                   \tag{2.14}
\]

This follows from
\(U_p-U_p^*=-(I-U_p)(I+U_p^*)\).  Hence its Gram is an
explicit postprocessing of the already proved antisymmetric tower Gram.

There is also a normalization warning.  The score form is first order in
\(\log p\), whereas the unnormalized anomaly Gram is quadratic in
\(\log p\).  Thus the raw Gram
\(\mathfrak A_p^*\mathfrak A_p\) cannot by itself be the D.190
first-order born score under a uniform rescaling of one local prime
channel.  A successful defect identity must use the natural tangent/Fisher
normalization (or a cross term with the central self-dual vector), not
simply square (2.13).  This eliminates one more tempting but incorrectly
scaled factorization.

## 3. Consequence for the D.240 route

The primary Sonin theorem proves, at the central normalization,

\[
 \theta_S:\mathfrak S_\lambda(\mathbb R)
 \xrightarrow{\sim}\mathfrak S_\lambda(X_S),
 \qquad
 \mathcal F_S\theta_S=\theta_S\mathcal F_\infty ,
                                                               \tag{3.1}
\]

using the self-Fourier tensor
\(\bigotimes_{p\in S}\sigma_p\).  Formula (2.4) proves that replacing the
central inverse Euler numerator by its \(\sigma\)-deformation does not
produce another map satisfying (3.1).  Therefore:

* the metric derivative identity D.240(3.4) remains valid;
* the dual Euler pairing identity remains valid as a multiplier identity;
* semilocal Sonin stability cannot by itself assign a sign to that
  derivative;
* any source-level first-variation proof must include the anomaly vectors
  \(w_p\), rather than treating the self-Fourier relation as persistent in
  \(\sigma\).

This is not merely a missing continuity argument.  The conductor of a
self-dual \(p\)-adic additive character is discrete, and (1.4) proves the
failure already in the two-shell radial calculation.

## 4. Reduced candidate

Let

\[
 \dot{\mathfrak a}_S
 =\sum_{p\in S}
 \sigma_{S\setminus\{p\}}\otimes
 \left(-{\log p\over p}w_p\right)                  \tag{4.1}
\]

be the derivative of the failure of the tensor local vector to be
self-Fourier.  Equation (4.1) is source-defined, uses the additive
self-duality of \(\mathbb Q_p\), and has one explicit channel per prime.

The next admissible comparison is:

> Compress the Poisson/Fourier boundary transport generated by
> \(\dot{\mathfrak a}_S\) to the old/born support decomposition, include the
> archimedean derivative, and determine whether its Gram is exactly
> \[
> B_E-X_{OE}^*A_O^\dagger X_{OE}.
> \]

If the equality holds, it proves the sharp Douglas gate by a source-level
square.  If a residual remains, that residual—not generic Sonin
monotonicity—is the next mathematical obstruction.

The norm estimate (2.6) alone cannot prove the comparison: it loses the
critical cancellation and has no reason to deliver the sharp constant one.

## 5. Classification

* Fourier formula (1.3): **PROVED IDENTITY**.
* Uniqueness of the self-Fourier coefficient (1.4): **PROVED**.
* Isolation of the central Euler normalization (2.4): **PROVED**.
* Tangent anomaly (2.5) and its norm (2.6): **PROVED**.
* Fourier parity, orthogonality and tensor norm (2.7)--(2.9):
  **PROVED**.
* Multiplicative anomaly filter (2.11)--(2.13): **PROVED IDENTITY**.
* A differentiable family of self-Fourier Sonin embeddings realizing the
  \(\sigma\)-metric path: **FALSE** for the natural Euler deformation.
* Identification of the anomaly Gram with the D.190 residual:
  **OPEN**.
* Row D: **OPEN**.
