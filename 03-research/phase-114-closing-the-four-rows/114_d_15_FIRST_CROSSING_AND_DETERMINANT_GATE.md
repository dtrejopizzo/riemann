# Row (d): first crossing and determinant gate

## 1. Fixed-window realization

Let `U_T:L^2(-T,T)->L^2(-1,1)` be the unitary rescaling

\[
 (U_TF)(u)=T^{1/2}F(Tu).
\]

Under this map the ruling constraints become orthogonality to

\[
 r_{T,+}(u)=e^{Tu/2},\qquad r_{T,-}(u)=e^{-Tu/2}.
\]

For every `T>0` these vectors are linearly independent.  Their Gram matrix
depends analytically on `T`, so the orthogonal projection `P_T` onto their
common kernel is norm-continuous locally on `(0,infinity)`.

The finite contact terms become truncated translations by `log(n)/T`.
Only the finitely many `n <= exp(2T)` have overlapping support.  At a
threshold `log(n)=2T` the correlation is zero, and translation continuity
shows that the new term enters continuously.

The archimedean form has fixed-window multiplier

\[
 m_\infty(\sigma/T).
\]

On every compact `T`-interval its closed form domain is the same logarithmic
Sobolev space, because

\[
 1+|m_\infty(\sigma/T)|\asymp 1+\log(1+|\sigma|)
\]

uniformly there.  Dominated convergence gives continuous dependence in
the common form norm.

## Theorem 1 (continuity of the Hodge margin)

The constrained top eigenvalue of `B_nuc` on `L^2(-T,T)` is attained and
depends continuously on `T>0`.  Equivalently, the Hodge margin `eta(T)` of
the sharp-Poincare formulation is continuous.  It is also nonincreasing by
zero-extension.

### Proof

After `U_T`, the archimedean forms are a locally form-norm-continuous family
with common domain.  Translation is norm-continuous from this logarithmic
form domain to `L^2`: in Fourier variables, split at a large `R` and use

\[
 \sup_\tau\frac{|e^{i\tau h}-1|^2}
 {1+\log(1+|\tau|)}\longrightarrow0\qquad(h\to0).
\]

Thus the contact contribution, a locally finite sum of translations, is
form-norm-continuous; threshold terms tend to zero because the overlap of
the two compact intervals tends to a null set.  Composing with the
norm-continuous finite-codimensional
projections `P_T` gives a continuous family of closed upper-bounded forms
with compact form-domain embedding.  The min--max principle for the largest
eigenvalue gives continuity.  Zero-extension gives monotonicity exactly as
in the sharp-Poincare theorem.

## 2. The first-crossing criterion

Small-window positivity is known for the localized Weil form and can also
be obtained from domination by the logarithmic gamma energy.  Therefore,
if row (d) fails, continuity and monotonicity produce a first `T_0>0` with

\[
 \eta(T_0)=0.
\]

At that window there is a nonzero constrained minimizer `F_0` satisfying

\[
 \bigl(L_{T_0,X}-(2A_X+m_0)\bigr)F_0
 =\alpha e^{t/2}+\beta e^{-t/2},                   \tag{2.1}
\]

with exterior value zero and both ruling moments zero.

Consequently row (d) is equivalent to exclusion of nonzero solutions of
(2.1) at every window, together with the already known small-window sign.
This is a genuine boundary-value formulation containing no zero of `xi`.

It is not yet a proof: excluding (2.1) is the sharp global step.

## 3. Why an ordinary Fredholm determinant is unavailable

The gamma part has symbol

\[
 d_\infty(\tau)=\log(1+|\tau|)+O(1).
\]

On a bounded interval its eigenvalues grow at most logarithmically,

\[
 \lambda_k\le C_T\log(1+k).                         \tag{3.1}
\]

Indeed, take the span of the first `k` Dirichlet sine modes.  On this span
the `H^1` norm is at most `C_T k` times the `L^2` norm.  Concavity of the
logarithm and Plancherel give

\[
 \int\log(1+|\tau|)|\widehat F(\tau)|^2d\tau
 \le C\log(1+k)\|F\|_2^2.
\]

The finitely many prime translations are bounded forms.  The min--max
principle proves (3.1); imposing two moment equations only changes the
index by at most two.

Its resolvent is compact, but (3.1) forces its singular values to satisfy

\[
 s_k((L+c)^{-1})\ge\frac1{C'_T\log(1+k)}.
\]

Hence the resolvent is not in any Schatten class `S_p`, `p<infinity`:

\[
 \sum_k s_k^p=\infty
\]

for every finite `p`.  The bounded prime-translation perturbation composed
with this resolvent is therefore not automatically trace class (or even
Schatten), and the usual determinant `det(I+K)` is not defined from the
available estimates.

Likewise, the naive spectral zeta series

\[
 \sum_k\lambda_k^{-s}
 \asymp\sum_k(\log k)^{-s}
\]

diverges for every complex `s` with finite real part.  Thus the standard
zeta-regularized determinant is not obtained by the usual initial
half-plane of convergence.

The finite determinants used in spectral-triple truncations remain valid,
but passage to a determinant detecting the first crossing requires a new
relative cancellation or a stronger ideal furnished by the geometry.
Assuming convergence/nonvanishing of such a determinant without proving
that cancellation simply replaces the Poincare gate by an equivalent
determinant gate.

## 4. Surviving route

The first-crossing formulation is useful because it reduces D to uniqueness
for one explicit nonlocal boundary equation.  A valid closure may prove
uniqueness by a geometric maximum/oscillation principle or by constructing
a relative determinant whose existence and nonvanishing follow from a
positive boundary object.  Neither the compact-resolvent statement alone
nor an unproved determinant limit supplies that result.
