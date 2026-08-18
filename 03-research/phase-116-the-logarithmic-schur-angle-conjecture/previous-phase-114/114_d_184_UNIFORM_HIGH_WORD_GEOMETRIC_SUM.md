# D.184 — Uniform geometric sum for the exact high-word sector

## Verdict

The high spectral sector can be summed uniformly in the return depth; no
fixed-\(k\) asymptotic is required.  Choose

\[
 R=N^c,\qquad c={4\over5},\qquad \eta={1\over100},
 \qquad a_N=(1-\eta)h_{5/4}(R).                      \tag{0.1}
\]

Let

\[
 b_N^2=V_N+H_N,qquad
 V_N=\sum_{n\le N}{\Lambda(n)^2\over n},qquad
 H_N={\Lambda_2(N)\over\sqrt N}.                    \tag{0.2}
\]

Then

\[
 z_N^2:={b_N^2\over a_N^2}\longrightarrow
 {1\over2c^2(1-\eta)^2}=0.79711\ldots<1.            \tag{0.3}
\]

Consequently there are \(N_0\) and \(0<\rho<1\) such that every
all-high word of arbitrary depth \(k\) satisfies

\[
 \boxed{
 \|\mathcal B_NG_{{\rm hi},N}\mathcal B_N\cdots
       G_{{\rm hi},N}\mathcal B_N\|
 \le b_N z_N^{k-1}\le b_N\rho^{k-1},
 \qquad N\ge N_0.}                                  \tag{0.4}
\]

Here \(G_{{\rm hi},N}\) is the exact high part of the complete reference
Green operator, not the Gamma-only inverse.  It contains Gamma and every
\(p^j\), and

\[
 \|G_{{\rm hi},N}\|\le a_N^{-1}.                   \tag{0.5}
\]

Thus

\[
 \boxed{
 \sum_{k\ge1}b_N^{-2}
 \|\mathcal B_NG_{{\rm hi},N}\cdots
 G_{{\rm hi},N}\mathcal B_N\|^2
 \le{1\over1-\rho^2}.}                              \tag{0.6}
\]

This proves uniform summability for obligation (1) of the D.181 residual
split.  It does not by itself prove the unit Schur-capacity budget.  If
\(y_{\rm hi}\) is the normalized initial/terminal load, the corresponding
estimate is

\[
 \boxed{\operatorname {Cap}_{\rm hi}
 \le {\|y_{\rm hi}\|^2\over1-\rho^2}.}              \tag{0.6a}
\]

To conclude contractivity this quantity, the low contribution and their
cross term must still sum to at most one.  The geometric sum is about
\(4.9\) at the limiting constant (0.3), so mere summability cannot replace
that load budget.

The estimate is deliberately cruder than D.183: the latter retains the
superfactorial Witt simplex, but only had a fixed-depth asymptotic
available.  Equation (0.4) instead uses the exact one-layer Gram at every
occurrence and is therefore uniform for all
\(0\le k\le\lfloor\log_2N\rfloor\), indeed for all \(k\ge1\).

The threshold is sharp for this geometric method.  If

\[
 c\le {1\over\sqrt2(1-\eta)},                       \tag{0.7}
\]

then \(\liminf z_N\ge1\), so a proof based only on multiplying the exact
one-layer norm and the high inverse norm cannot converge.  The choice
(0.1) lies strictly above (0.7) while keeping the low rank sublinear:

\[
 \operatorname {rank}F_N
 \le {2TR\over\pi\eta}+2
 =O(N^{4/5}\log N).                                  \tag{0.8}
\]

## 1. Exact one-layer norm

D.164 proves on every integer cell

\[
 \mathcal B_N^*\mathcal B_N=
 \begin{pmatrix}V_N&H_N\\H_N&V_N\end{pmatrix}\otimes I,
 \qquad \|\mathcal B_N\|^2=V_N+H_N.                \tag{1.1}
\]

This includes all active prime powers.  No asymptotic is used in (1.1).
Moreover \(0\le H_N\le V_N\).

## 2. Exact high inverse

Use the actual spectral low projection of the ambient complete reference,

\[
 E_{<a_N}=\mathbf1_{(0,a_N)}(\overline{\mathcal R}_T),
 \qquad E_{\ge a_N}=I-E_{<a_N}.                     \tag{2.1}
\]

D.180--D.181 prove

\[
 \operatorname {rank}E_{<a_N}\le{2TR\over\pi\eta}, \tag{2.2}
\]

and functional calculus gives

\[
 G_{{\rm hi},N}
 =\overline{\mathcal R}_T^{-1}E_{\ge a_N},
 \qquad\|G_{{\rm hi},N}\|\le a_N^{-1}.             \tag{2.3}
\]

Imposing the two Tate moments changes the Green operator by rank at most
two.  Assign that correction to \(F_N\), not to \(G_{{\rm hi},N}\).  This
proves (0.5) and (0.8).

The semigroup split of D.181 is compatible with (2.3): on the high
spectral space its localized and residual terms recombine to the single
operator \(G_{{\rm hi},N}\).  Hence the binomial factor
\((1+e^{-1})^k\) must not be introduced.  It would be an artefact of
estimating two pieces separately after they have already recombined by
functional calculus.

## 3. Uniform geometric word estimate

An all-high word with \(k\) boundary layers contains \(k-1\) high Green
operators.  Submultiplicativity, (1.1), and (2.3) give directly

\[
 \|\mathcal B_NG_{{\rm hi},N}\mathcal B_N\cdots
 G_{{\rm hi},N}\mathcal B_N\|
 \le b_N^k a_N^{-(k-1)}=b_Nz_N^{k-1}.               \tag{3.1}
\]

This proof is insensitive to noncommutation and is uniform in \(k\).  It
also remains true if the layers act between different copies of the same
left/right boundary channel space, since every copy has the same exact
Gram (1.1).

## 4. Asymptotic constant and strict margin

The prime number theorem and partial summation give

\[
 V_N={1\over2}(\log N)^2+O(\log N),                 \tag{4.1}
\]

while the divisor bound applied to \(\Lambda_2(N)\) gives

\[
 H_N=o((\log N)^2).                                  \tag{4.2}
\]

The Gamma asymptotic is

\[
 h_{5/4}(N^c)=c\log N+O(1).                         \tag{4.3}
\]

Equations (4.1)--(4.3) prove

\[
 z_N^2={\tfrac12+o(1)\over c^2(1-\eta)^2},          \tag{4.4}
\]

which is (0.3).  For \(c=4/5\), \(\eta=1/100\), the limit is

\[
 {1\over2(16/25)(99/100)^2}=0.797112\ldots.         \tag{4.5}
\]

Choose any \(\rho^2\) strictly between (4.5) and one.  Then
\(z_N\le\rho\) for all \(N\ge N_0\), and summing (3.1) proves (0.6).
Applied to an initial load \(y_{\rm hi}\), the same calculation proves
(0.6a), not a unit bound unless the load has the required remaining size.

## 5. Exact remaining obligation

Words meeting \(F_N\) are not covered by (0.4).  Their range has dimension
\(O(N^{4/5}\log N)\), but a rank bound alone gives no smallness.  The load
on this block is the complete centered discrepancy \(E_N\), the endpoint
Volterra term, and the two Tate correction vectors.  Obligation (2) is to
prove the joint budget

\[
 {\|y_{\rm hi}\|^2\over1-\rho^2}
 +\operatorname {Cap}_{\rm lo}
 +\operatorname {Cap}_{\rm cross}\le1,              \tag{5.1}
\]

uniformly in \(N\), with the cross term estimated in the same Green
metric.  No assertion that rank alone or geometric summability proves
(5.1) is made.
