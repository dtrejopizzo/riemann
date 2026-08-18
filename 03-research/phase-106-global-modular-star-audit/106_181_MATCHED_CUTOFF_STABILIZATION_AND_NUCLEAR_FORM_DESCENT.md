# 106.181 — Matched-cutoff stabilization and nuclear form descent

## 1. Purpose

The full-return Green decomposition contains two opposite scalar terms
\(+C_Xh(0)\) and \(-C_Xh(0)\). Taken separately they diverge as the
prime cutoff grows, which suggests a finite-part ambiguity. On the CCM
test core, however, the two terms arise with the same cutoff and cancel
before any limit is taken. The remaining prime sum is finite for a
compactly supported logarithmic correlation and therefore stabilizes
exactly.

This note proves that matched-cutoff stabilization, its compatibility
with weight-one scaling, and the consequent descent of the joined form
through the closed CCM restriction range. Combined with the
Dirichlet-normalized Julia graph of 106.179, it proves equality of the
joined graph/boundary form with the CCM Rosati form on the nuclear
quotient.

The theorem is a descent and normalization result. It does not prove
that the descended boundary-corrected form is positive.

## 2. The compact logarithmic correlation core

Let \(\mathscr D_c\subset\mathbf S(C_{\mathbb Q})\) be the usual dense
subspace which is smooth in the real scaling variable, finite under the
compact-character decomposition, and compactly supported in
\(u=\log|x|\). Let \(f,g\in\mathscr D_c\) and put

\[
 h_{f,g}=f*g^\sharp.
\tag{1}
\]

Convolution preserves compact logarithmic support up to Minkowski sum.
Consequently there is \(L=L(f,g)<\infty\) such that the fixed-orbit
coefficient of \(h_{f,g}\) vanishes for
\(|u|>L\).

For \(X\ge2\), let

\[
 I_X=\{(p,k):k\ne0,\ p^{|k|}\le X\},
 \qquad
 w_{p,k}=(\log p)p^{-|k|/2},
\tag{2}
\]

and define

\[
 C_X=\sum_{(p,k)\in I_X}w_{p,k},
 \qquad
 A_X(h)=\sum_{(p,k)\in I_X}w_{p,k}h(k\log p).
\tag{3}
\]

Let \(\mathcal P_\infty(h)\) denote the already joined archimedean and
polar functional in the completed CCM trace formula. It is not split
into independently regularized scalar pieces below.

The finite-prime Green energy and its generic boundary are

\[
 \mathcal E_X(h)=C_Xh(0)-A_X(h),
 \qquad
 \mathcal B_X(h)=\mathcal P_\infty(h)-C_Xh(0).
\tag{4}
\]

Thus

\[
 \boxed{
 \mathcal E_X(h)+\mathcal B_X(h)
 =\mathcal P_\infty(h)-A_X(h).}
\tag{5}
\]

Equation (5) is an identity at every finite cutoff.

## 3. Exact stabilization

### Theorem 3.1 — Matched-cutoff cancellation

If the logarithmic fixed-orbit coefficient of \(h\) is supported in
\([-L,L]\), then for every \(X\ge e^L\),

\[
 \boxed{
 \mathcal E_X(h)+\mathcal B_X(h)
 =\mathcal P_\infty(h)
  -\sum_{p,k\ne0}w_{p,k}h(k\log p),}
\tag{6}
\]

and the right-hand side is a finite sum independent of \(X\).

#### Proof

The scalar terms in (4) cancel algebraically for every \(X\), giving
(5). If \(p^{|k|}>e^L\), then \(|k|\log p>L\), so the corresponding
fixed-orbit coefficient vanishes. Hence no return added after
\(X=e^L\) changes \(A_X(h)\). This proves (6). \(\square\)

The theorem excludes a scheme parameter on the compact core. A scalar
ambiguity appears only if different cutoffs are imposed on the two terms
of (4). Such a mismatch is not the CCM Green identity and is not used in
the construction.

## 4. Exact Julia realization of the stabilized form

Let \(T_X=A_X/C_X\) be the self-adjoint return contraction acting in the
translation representation, and let \(\iota_{-,X}\) be its negative
Julia graph. Theorem 4.1 of 106.179 gives

\[
 g_{D,X}(\iota_{-,X}f,\iota_{-,X}g)
 =\mathcal E_X(h_{f,g}).
\tag{7}
\]

Combining (5) and (7) yields

\[
 \boxed{
 g_{D,X}(\iota_{-,X}f,\iota_{-,X}g)
 +\mathcal B_X(h_{f,g})
 =\mathcal P_\infty(h_{f,g})-A_X(h_{f,g}).}
\tag{8}
\]

For \(X\ge e^{L(f,g)}\), (8) is independent of the cutoff. Thus the
singular graph and the vanishing Dirichlet weight are used only at finite
level, where their product is the closed energy (7); no cofinal operator
limit of \(T_X\) is required.

## 5. Scaling covariance without an anomaly

Let \(L_a\) be the CCM scaling action. Equations 106.157(15)--(16) give

\[
 h_{L_af,L_ag}=|a|h_{f,g}.
\tag{9}
\]

In particular its logarithmic support is unchanged. Both sides of (8)
therefore obey

\[
 \boxed{
 \mathfrak H(L_af,L_ag)=|a|\mathfrak H(f,g),}
\tag{10}
\]

where \(\mathfrak H\) denotes the stabilized value in (8).

There is no inhomogeneous scale anomaly in the joined form. The
individual scalar pieces have opposite cutoff dependence, but their
matched sum cancels before scaling is applied. Proposition 5.1 of
106.180 remains relevant: covariance alone would not fix a deliberately
introduced scalar mismatch. Equation (5), not covariance, prevents such
a mismatch.

## 6. Descent through the CCM restriction range

Let

\[
 \rho:\mathscr S(\mathcal G_{\mathbb Q})_0
 \longrightarrow\mathbf S(C_{\mathbb Q})
\tag{11}
\]

be the CCM reduction/summation morphism, and let \(\mathcal V\) be its
range. The CCM vanishing identity states

\[
 \tau(v*h)=0
 \qquad(v\in\mathcal V).
\tag{12}
\]

The explicit formula on the compact core identifies

\[
 \tau(h)=\mathcal P_\infty(h)
 -\sum_{p,k\ne0}w_{p,k}h(k\log p).
\tag{13}
\]

By Theorem 3.1 and (8),

\[
 \boxed{
 \mathfrak H(f,g)=\tau(f*g^\sharp).}
\tag{14}
\]

### Theorem 6.1 — Nuclear form descent

The joined Dirichlet-graph/boundary form \(\mathfrak H\) vanishes when
either argument lies in \(\mathcal V\), extends continuously to the CCM
Schwartz/Meyer completion, and induces on

\[
 \mathcal Z=\mathbf S(C_{\mathbb Q})/\overline{\mathcal V}
\tag{15}
\]

exactly the Rosati pseudo-polarization

\[
 \boxed{
 \mathfrak H([f],[g])
 =\mathfrak h_{\rm Ros}([f],[g])
 =\tau(f*g^\sharp).}
\tag{16}
\]

#### Proof

Equation (14) and the vanishing property (12) prove descent on the compact
core. The CCM trace functional, convolution, and \(\sharp\) are
continuous in the Schwartz/Meyer topology. Hence (14) has a unique
continuous extension, vanishes on \(\overline{\mathcal V}\), and defines
a form on (15). Definition 106.157(7) is the last expression in (16),
so the descended forms coincide. \(\square\)

This descent retains the nonreduced topology: it uses continuity of the
distributional trace on the nuclear quotient, not a reduced Hilbert
closure. The dense-jet embedding of 106.175 supplies a faithful
coordinate observation of the same quotient.

## 7. What remains after form descent

The following parts are now fixed:

* the negative Julia branch;
* the unique local Dirichlet normalization;
* the matched cofinal prescription;
* weight-one covariance;
* descent through the closed CCM range;
* equality of the descended joined form with the CCM Rosati form.

What is not proved by Theorem 6.1 is

\[
 \operatorname {Re}\mathfrak H([f],[f])\ge0.
\tag{17}
\]

The local graph term in (8) is positive, but the joined boundary term is
not separately positive. A complete global polarization still requires
a boundary Hodge factorization of the **already descended** form (16),
not another choice of cutoff or another comparison with Rosati.

Equivalently, one must construct on the relative graph/boundary complex
a compatible star whose positive metric has (16) as its Hermitian
intersection form. This is the remaining force-bearing theorem.

## 8. Status

Proved without RH or zero input:

* exact cancellation of the two scalar cutoff terms;
* finite stabilization on the compact logarithmic core;
* exact weight-one scaling covariance of the stabilized form;
* torsion-sensitive descent of the joined form through the CCM range;
* equality of that descended form with the global CCM Rosati pairing.

Still required:

* a positive boundary Hodge factorization of the descended form;
* verification of (17), and hence the full global polarization.
