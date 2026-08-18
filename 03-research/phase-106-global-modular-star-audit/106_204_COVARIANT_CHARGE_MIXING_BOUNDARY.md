# 106.204 — The covariant charge-mixing boundary

## 1. Purpose

The complete-return boundary of 106.203 has the correct finite Hodge
Gram mass, but its raw sum identifies rows with different scale
generators.  The ((p,k))-row carries

\[
 A-\ell_{p,k},\qquad \ell_{p,k}=k\log p,
\tag{1}
\]

whereas the common archimedean boundary carries (A).  A scalar sum of
these rows is not equivariant.  This note constructs the missing
intertwiner explicitly.  It yields one common regression for every
prime, preserves all charge phases, and produces the diagonal law

\[
 \bigl(\kappa_\infty+m_\Gamma(A-\ell_{p,k})\bigr)^{-1}
\tag{2}
\]

without discarding the off-diagonal prime--prime terms.

No zero or sign of the Weil form is used.

## 2. Spectral translations of the Cauchy coefficient module

Use the spectral model of the coefficient space from 106.199,

\[
 \mathscr K_C=L^2(\mathbb R,w_C(\gamma)\,d\gamma),
 \qquad
 w_C(\gamma)=\frac1{2\pi(\gamma^2+1/4)},
 \qquad
 (AF)(\gamma)=\gamma F(\gamma).
\tag{3}
\]

For \(\ell\in\mathbb R\), define

\[
 \boxed{
 (S_\ell F)(\gamma)
 =\left(\frac{w_C(\gamma+\ell)}{w_C(\gamma)}\right)^{1/2}
   F(\gamma+\ell).}
\tag{4}
\]

### Theorem 2.1 — Exact decharging unitary

The operators (S_\ell) form a strongly continuous unitary group and

\[
 \boxed{
 S_\ell(A-\ell I)=AS_\ell,
 \qquad
 S_\ell e^{it(A-\ell I)}=e^{itA}S_\ell.}
\tag{5}
\]

For every bounded Borel function (f),

\[
 \boxed{S_\ell^*f(A)S_\ell=f(A-\ell I).}
\tag{6}
\]

#### Proof

Changing variables \(\eta=\gamma+\ell\) in (4) gives

\[
 \begin{aligned}
 \|S_\ell F\|^2
 &=\int_{\mathbb R}
   \frac{w_C(\gamma+\ell)}{w_C(\gamma)}
   |F(\gamma+\ell)|^2w_C(\gamma)\,d\gamma\\
 &=\int_{\mathbb R}|F(\eta)|^2w_C(\eta)\,d\eta.
 \end{aligned}
\tag{7}
\]

The Radon--Nikodym factors telescope, so

\[
 S_\ell S_m=S_{\ell+m},\qquad S_\ell^{-1}=S_{-\ell}.
\tag{8}
\]

Strong continuity follows first on compactly supported continuous
functions and then by density and the common unitary bound.  Finally,

\[
 \begin{aligned}
 S_\ell(A-\ell I)F(\gamma)
 &=\left(\frac{w_C(\gamma+\ell)}{w_C(\gamma)}\right)^{1/2}
   ((\gamma+\ell)-\ell)F(\gamma+\ell)\\
 &=\gamma(S_\ell F)(\gamma),
 \end{aligned}
\tag{9}
\]

which proves (5).  The spectral calculus gives (6). \(\square\)

The density in (3) is not an obstruction: it is equivalent to Lebesgue
measure, and the Radon--Nikodym factor in (4) is exactly what makes
spectral translation unitary.

## 3. Why the raw charged sum cannot be equivariant

Let (I) contain two distinct positive lengths and let the (i)-th
source row carry (e^{it(A-\ell_i)}).  Consider the raw row

\[
 R_0(x_i)_{i\in I}=\sum_{i\in I}\alpha_i x_i,
 \qquad \alpha_i\ne0.
\tag{10}
\]

### Proposition 3.1 — Static charge identification obstruction

There is no common boundary action (e^{itA}) for which (10) is an
intertwiner.

#### Proof

If (R_0\bigoplus_i e^{it(A-\ell_i)}=e^{itA}R_0), apply the identity to
a vector supported only in row (i).  Cancellation of (e^{itA})
gives

\[
 \alpha_i e^{-it\ell_i}x=\alpha_i x
\tag{11}
\]

for every (t,x), impossible for \(\ell_i>0\). \(\square\)

Thus the spectral transports in (4) are not optional normalization
factors.  They are forced by equivariance.

## 4. The corrected complete-return boundary

Let

\[
 I_X=\{(p,k):p^k\le X\},\qquad
 \ell_{p,k}=k\log p,
\tag{12}
\]

and retain

\[
 c_p=\frac{2\pi}{\log p},\qquad
 \alpha_{p,k}=\sqrt{\frac{\log p}{c_p}}p^{-k/2},\qquad
 w_{p,k}=c_p\alpha_{p,k}^2=\frac{\log p}{p^k}.
\tag{13}
\]

Take

\[
 \mathscr V_X=\bigoplus_{(p,k)\in I_X}
 H^1(E_p;\mathbb R)\widehat\otimes\mathscr K_C
\tag{14}
\]

with the Tate forms of 106.203.  On the ((p,k))-copy the normalized
scale action is (e^{it(A-\ell_{p,k})}).  For

\[
 v=\sum_{p,k}(a_{p,k}\otimes x_{p,k}
              +b_{p,k}\otimes y_{p,k}),
\tag{15}
\]

define

\[
 \boxed{
 \begin{aligned}
 R_X^{\rm cov}v
   &=\sum_{p,k}\alpha_{p,k}S_{\ell_{p,k}}y_{p,k},\\
 R_X^{\rm cov}J_Xv
   &=\sum_{p,k}c_p\alpha_{p,k}S_{\ell_{p,k}}x_{p,k}.
 \end{aligned}}
\tag{16}
\]

### Theorem 4.1 — One equivariant boundary for all charges

The row (16) intertwines the direct sum of charged source actions with
the single boundary action (e^{itA}).  Its Hodge-conjugate generic
plane is

\[
 \boxed{
 \Gamma_X^{\rm cov}(F_0,F_1)
 =\sum_{p,k}\alpha_{p,k}
 \left(
 a_{p,k}\otimes S_{\ell_{p,k}}^*F_0
 +c_pb_{p,k}\otimes S_{\ell_{p,k}}^*F_1
 \right).}
\tag{17}
\]

Writing

\[
 \partial_{T,X}^{\rm cov}v
 =(R_X^{\rm cov}J_Xv,R_X^{\rm cov}v),
\tag{18}
\]

one has

\[
 \boxed{
 (\Gamma_X^{\rm cov})^*=\partial_{T,X}^{\rm cov},
 \qquad
 (\Gamma_X^{\rm cov})^*\Gamma_X^{\rm cov}=C_XI,
 \qquad
 C_X=\sum_{p^k\le X}\frac{\log p}{p^k}.}
\tag{19}
\]

Moreover

\[
 J_X\Gamma_X^{\rm cov}=\Gamma_X^{\rm cov}J_{\rm bd},
 \qquad
 \partial_{T,X}^{\rm cov}J_X
 =J_{\rm bd}\partial_{T,X}^{\rm cov}.
\tag{20}
\]

#### Proof

Equation (5), applied row by row, proves scale equivariance of (16).
For the adjoint, the Tate metric gives

\[
 \begin{aligned}
 \langle\Gamma_X^{\rm cov}(F_0,F_1),v\rangle
 &=\sum_{p,k}c_p\alpha_{p,k}
   \langle S_{\ell_{p,k}}^*F_0,x_{p,k}\rangle\\
 &\quad+\sum_{p,k}\alpha_{p,k}
   \langle S_{\ell_{p,k}}^*F_1,y_{p,k}\rangle\\
 &=\langle(F_0,F_1),\partial_{T,X}^{\rm cov}v\rangle.
 \end{aligned}
\tag{21}
\]

Since every (S_\ell) is unitary, applying the adjoint to (17) gives
\(\sum c_p\alpha_{p,k}^2=C_X\) on both boundary components.  The Hodge
identities are termwise. \(\square\)

## 5. The genuinely joint Gamma--Euler Schur metric

Put

\[
 K_\Gamma=\kappa_\infty I+m_\Gamma(A)\succeq\kappa_\infty I.
\tag{22}
\]

Glue (18) to the adjoint of the complete Gamma boundary row exactly as
in 106.198.  The minimum representative over the archimedean variable
has metric

\[
 \boxed{
 \begin{aligned}
 g_X^{\rm cov}(v,w)
 &=g_X(v,w)\\
 &\quad+\langle K_\Gamma^{-1}R_X^{\rm cov}J_Xv,
                         R_X^{\rm cov}J_Xw\rangle\\
 &\quad+\langle K_\Gamma^{-1}R_X^{\rm cov}v,
                         R_X^{\rm cov}w\rangle.
 \end{aligned}}
\tag{23}
\]

It is positive definite, Hodge invariant, and scale invariant.  Its
single-row diagonal compression is exactly

\[
 \boxed{
 S_{\ell_{p,k}}^*K_\Gamma^{-1}S_{\ell_{p,k}}
 =\bigl(\kappa_\infty+m_\Gamma(A-\ell_{p,k})\bigr)^{-1}.}
\tag{24}
\]

For two different rows (i,j\), the cross compliance is

\[
 \boxed{S_{\ell_i}^*K_\Gamma^{-1}S_{\ell_j}.}
\tag{25}
\]

Thus (23) realizes the shifted diagonal law of 106.200 but does not
replace the off-diagonal arithmetic phases by absolute values.  The
same common regression is used for every prime.

#### Proof

The Schur calculation is Theorem 4.1 of 106.198 with (18) as its
boundary row.  Positivity follows from (22); (20) gives Hodge invariance;
and Theorem 4.1 gives scale equivariance.  Equation (24) is (6) with
\(f=(\kappa_\infty+m_\Gamma)^{-1}\).  Expanding the two boundary sums
in (23) gives (25). \(\square\)

## 6. Cofinal compatibility and the finite-part chain identity

For (X\le Y\), extension by zero preserves (16), hence (23).  Therefore
the maps

\[
 (\mathbb P_X^{\rm cov},g_X^{\rm cov},J_X)
 \hookrightarrow
 (\mathbb P_Y^{\rm cov},g_Y^{\rm cov},J_Y)
\tag{26}
\]

are polarized isometries and define a canonical Hilbert direct limit.

The common-plus-residual decomposition of 106.202 must now be read in
the decharged frame.  Namely, a generic row has the form

\[
 F_{p,k}=S_{\ell_{p,k}}^*F+r_{p,k},
 \qquad
 S_{\ell_{p,k}}F_{p,k}=F+S_{\ell_{p,k}}r_{p,k}.
\tag{27}
\]

Unitary transport leaves all weights (w_{p,k}) unchanged.  Hence the
common finite-part coefficient still cancels exactly, while every
decharged residual remains with its literal weight.  Corollary 5.1 of
106.202 therefore survives the covariance correction.

## 7. What is now constructed and what remains

The correction closes a real gap in the source object:

* distinct charge generators are transported to one boundary frame;
* the common regression is genuinely scale equivariant;
* the complete-return Gram mass is unchanged;
* the shifted Gamma law follows by conjugation rather than assertion;
* all off-diagonal prime phases remain in the Schur metric;
* cofinal polarized isometries and the nuclear finite-part identity are
  retained.

The remaining statement is still descent faithfulness:

\[
 \boxed{
 (D_Q^{\rm cov})^{-1}
 \left(
  \overline{D_Q^{\rm cov}(\mathcal V)}^{\,\mathbb P_\infty^{\rm cov}}
 \right)=\mathcal V.}
\tag{28}
\]

Unlike the raw formula in 106.203, (28) is now attached to an actual
equivariant Hilbert map.  Proving (28), rather than defining the source
polarization, is the remaining force-bearing theorem.
