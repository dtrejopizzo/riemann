# 106.203 — The complete-return charged Tate boundary

> **Covariance correction.**  The finite Hodge and Gram identities in
> Sections 2--3 are correct in a fixed boundary frame.  As originally
> written, however, (6)--(8) identify coefficient fibers carrying the
> distinct generators (A-k\log p) without first transporting them to
> one spectral frame.  Consequently the claimed scale equivariance in
> Sections 4--5, and the fiberwise reading (18), do not follow from the
> displayed raw sum.  Document 106.204 supplies the missing unitary
> spectral translations (S_{k\log p}), replaces (R_X) by the
> covariant row \(\sum\alpha_{p,k}S_{k\log p}y_{p,k}\), and proves the
> corrected cofinal pushout.  All uses of the charged boundary below are
> to be read through that corrected row.
>
> Document 106.205 subsequently proves that the resulting ordinary
> Hilbert direct limit is purely absolutely continuous and therefore
> cannot receive CCM's discrete resonant eigenclasses faithfully.  Thus
> the kernel identity in Section 6 is false for this completion; a
> resonant nuclear/derived completion is required instead.

## 1. Purpose

Document 106.200 constructs the charge-shifted Gamma connection but leaves
the finite boundary map denoted abstractly by \(R_{S,Q}\).  To analyze the
cofinal closure, every return layer must be explicit.  This note constructs
that map and proves its Hodge and Gram identities.

For the \(k\)-fold return of the prime orbit \(p\), the amplitude is forced
by two already established quantities: the Hodge norm
\(c_p=2\pi/\log p\) of the Tate curve and the critical overlap
\(p^{-k/2}\).  The result is

\[
 \alpha_{p,k}=\sqrt{\frac{\log p}{c_p}}p^{-k/2},
 \qquad
 c_p\alpha_{p,k}^2=\frac{\log p}{p^k}.
\tag{1}
\]

Thus the complete boundary Gram mass is literally the norm-square tower
used in 106.202.

## 2. The finite complete-return module

For \(X\geq2\), let

\[
 I_X=\{(p,k):p\text{ prime},\ k\geq1,\ p^k\leq X\}.
\tag{2}
\]

For each \((p,k)\in I_X\), take a copy of the harmonic Tate plane
\(H^1(E_p;\mathbb R)\) with basis \(a_{p,k},b_{p,k}\).  Its forms are

\[
 \begin{aligned}
 J_pa_{p,k}&=c_pb_{p,k},
 &J_pb_{p,k}&=-c_p^{-1}a_{p,k},\\
 g_p(a_{p,k},a_{p,k})&=c_p,
 &g_p(b_{p,k},b_{p,k})&=c_p^{-1}.
 \end{aligned}
\tag{3}
\]

Let \(\mathscr K_Q\) be the charged coefficient module of 106.200 and put

\[
 \mathscr V_X
 =\bigoplus_{(p,k)\in I_X}
   H^1(E_p;\mathbb R)\widehat\otimes\mathscr K_Q.
\tag{4}
\]

The direct-sum metric and complex structure are denoted by \(g_X,J_X\).
For

\[
 v=\sum_{(p,k)\in I_X}
   \bigl(a_{p,k}\otimes x_{p,k}
        +b_{p,k}\otimes y_{p,k}\bigr),
\tag{5}
\]

define the complete-return boundary row

\[
 \boxed{
 R_Xv=\sum_{(p,k)\in I_X}\alpha_{p,k}y_{p,k}.}
\tag{6}
\]

Then

\[
 \boxed{
 R_XJ_Xv
 =\sum_{(p,k)\in I_X}c_p\alpha_{p,k}x_{p,k}.}
\tag{7}
\]

The charge operator acts on the \((p,k)\)-copy by

\[
 L_Q|_{p,k}=k\log p.
\tag{8}
\]

Hence the joint Gamma frequency there is
\(\gamma-k\log p\), exactly as required by 106.200(9).

## 3. The generic complete-return Hodge plane

Define

\[
 \boxed{
 \Gamma_X(F_0,F_1)
 =\sum_{(p,k)\in I_X}\alpha_{p,k}
  \bigl(a_{p,k}\otimes F_0+c_pb_{p,k}\otimes F_1\bigr).}
\tag{9}
\]

Let

\[
 C_X=\sum_{(p,k)\in I_X}c_p\alpha_{p,k}^2
 =\sum_{(p,k)\in I_X}\frac{\log p}{p^k}.
\tag{10}
\]

### Theorem 3.1 — Exact complete-return boundary Gram operator

With

\[
 \partial_{T,X}v=(R_XJ_Xv,R_Xv),
\tag{11}
\]

one has

\[
 \boxed{
 \Gamma_X^*=\partial_{T,X},
 \qquad
 \Gamma_X^*\Gamma_X=C_XI,}
\tag{12}
\]

and

\[
 \boxed{
 J_X\Gamma_X(F_0,F_1)=\Gamma_X(-F_1,F_0),
 \qquad
 \partial_{T,X}J_X=J_{\rm bd}\partial_{T,X}.}
\tag{13}
\]

#### Proof

For (5), the direct-sum Hodge metric gives

\[
 \begin{aligned}
 \langle\Gamma_X(F_0,F_1),v\rangle
 &=\sum_{p,k}c_p\alpha_{p,k}\langle F_0,x_{p,k}\rangle
  +\sum_{p,k}\alpha_{p,k}\langle F_1,y_{p,k}\rangle\\
 &=\langle(F_0,F_1),(R_XJ_Xv,R_Xv)\rangle.
 \end{aligned}
\tag{14}
\]

This proves the adjoint identity.  Applying (14) to (9) and using (1)
gives (10)--(12).  Equation (3) applied termwise gives (13). \(\square\)

Every return number remains a holonomy/charge label; no disconnected
Euler product is being added.  The first Eulerian projector of 106.174
has already selected these connected return symbols.

## 4. Charged operator-valued pushout with no abstract row

Let

\[
 K_{\Gamma,Q}=\kappa_\infty I+m_\Gamma(A-L_Q)
\tag{15}
\]

and \(\mathbb B_{\infty,Q}\) be the boundary row of 106.200.  The
complete-return pushout is

\[
 \boxed{
 \mathbb P_X
 =\ker\left(
   \partial_{T,X}\oplus
   (\mathbb B_{\infty,Q}^{(1)})^*
 \right).}
\tag{16}
\]

### Theorem 4.1 — Literal complete-return Schur metric

After minimum-norm shorting, \(\mathbb P_X\) is the graph over
\(\mathscr V_X\) with metric

\[
 \boxed{
 \begin{aligned}
 g_{\mathbb P,X}(v,w)
 &=g_X(v,w)\\
 &\quad+\langle K_{\Gamma,Q}^{-1}R_XJ_Xv,R_XJ_Xw\rangle\\
 &\quad+\langle K_{\Gamma,Q}^{-1}R_Xv,R_Xw\rangle.
 \end{aligned}}
\tag{17}
\]

It is positive definite, \(J_X\)-invariant, and normalized-scale
invariant.  Its common boundary compliance on the \((p,k,\gamma)\) fiber
is

\[
 \boxed{
 \bigl(\kappa_\infty
       +m_\Gamma(\gamma-k\log p)\bigr)^{-1}.}
\tag{18}
\]

#### Proof

Insert the explicit row (6)--(7) into Theorem 5.1 of 106.200.  Strict
positivity of (15) gives the graph and (17).  Equations (13) exchange the
two boundary terms, proving Hodge invariance.  The charge law (8) inserted
in (15) gives (18). \(\square\)

## 5. Cofinal compatibility

If \(X\leq Y\), extension by zero gives

\[
 \iota_{X,Y}:\mathscr V_X\longrightarrow\mathscr V_Y.
\tag{19}
\]

It preserves \(g_X,J_X,R_X\), and \(R_XJ_X\).  Therefore it induces a
polarized isometry

\[
 \boxed{
 \mathbb P_X\hookrightarrow\mathbb P_Y.}
\tag{20}
\]

The algebraic direct limit and its Hilbert completion are consequently
defined without an unspecified charge-mixing map:

\[
 \boxed{
 \mathbb P_{\infty,Q}
 =\overline{\varinjlim_X\mathbb P_X}.}
\tag{21}
\]

The boundary row is unbounded in the raw direct-sum metric because
\(C_X\to\infty\), but is bounded by definition in the graph metric (17).
Thus the completion retains the two generic boundary values instead of
forgetting them as in 106.169.

## 6. Exact closure gate

Let \(D_X\) be the finite relative cone map after the defect cancellation
of 106.201--106.202.  The maps are compatible with (20), so they define
an algebraic map

\[
 D_\infty:H^1_{\rm CCM,alg}\longrightarrow\mathbb P_{\infty,Q}.
\tag{22}
\]

The remaining identity is now attached to the explicit norm (17):

\[
 \boxed{
 \ker D_\infty
 =\overline{\mathrm{Ran}\,\rho^\natural}^{\,\rm CCM}.}
\tag{23}
\]

Equivalently, if a CCM test vector has complete-return localizations whose
distance to the co-diagonal ranges tends to zero in (17), then it already
belongs to the closed CCM restriction range.  There is no longer an
undefined \(R_{S,Q}\) or unspecified Gamma phase in this statement.

## 7. Status

Proved without RH or zero input:

* the literal amplitude \(\alpha_{p,k}\) of every return layer;
* the complete charged Tate boundary map and its Hodge conjugate;
* the exact Gram mass \(\sum_{p,k}(\log p)/p^k\);
* the charged generic Hodge plane and its adjoint;
* the full operator-valued Schur metric with phase
  \(\gamma-k\log p\);
* cofinal polarized isometries and the explicit Hilbert completion.

Still required:

* the kernel/closure identity (23).

By Theorem 8.1 of 106.200, (23) is sufficient to pull the complete
positive polarization back to the existing CCM degree one.
