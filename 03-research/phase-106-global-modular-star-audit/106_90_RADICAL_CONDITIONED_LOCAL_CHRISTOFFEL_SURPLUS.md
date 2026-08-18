# 106.90 — Radical-conditioned local Christoffel surplus

## Purpose and conclusion

Document 106.87 proves a local midpoint Christoffel bound before the
completed radical is removed.  Document 106.89 gives the exact adaptive
gain after the finite radical anti-short.  This note combines those two
statements without dropping the radical correction.

Let (V_M) be a finite elementary even zero-mode and multiplicity-jet
space of the kind used in 106.70, 106.73, and 106.87, and let

\[
 V_M=V_{M-1}\oplus\operatorname {span}\{\phi_M\},
 \qquad
 \mathcal R_J=\operatorname {span}\{r_1,\ldots,r_J\},             \tag{1}
\]

where

\[
 r_j=\frac{K^{(2j)}}K-4^{-j}.
\]

The elementary-space hypothesis is used in the analytic continuation and
large-(x) argument below.  The statement is not being asserted for an
arbitrary abstract form-core Galerkin space without those properties.

Assume that the preceding block of the finite maximal-radical anti-short
is positive definite, and write its negative new-mode pivot as

\[
 \widehat\sigma_X=-\delta_J<0.                                  \tag{2}
\]

If \(q_J^*\in\phi_M+V_{M-1}\) is its adaptive residual and \(V\) is the
complete omitted ordinary-prime-power feature, then the radical-conditioned
gain has the exact variational form

\[
 \boxed{
 G_J=\inf_{d\in V_{M-1},\ r\in\mathcal R_J}
 \left\{
   \widehat{\mathcal A}(d,d)
   +\|V(q_J^*+d+r)\|^2
 \right\}.}                                                       \tag{3}
\]

For a displacement \(u>0\) and aperture \(W>0\), let

\[
 \kappa_{M,J}(u,W)
 :=\inf_{q\in\phi_M+V_{M-1}+\mathcal R_J}
 \mathcal J_{u,W}(q,q).                                         \tag{4}
\]

The main local result is

\[
 \boxed{
 \kappa_{M,J}(u,W)
 =\frac{\det G_{M,J}(u,W)}{\det G_{M-1,J}(u,W)}>0.}              \tag{5}
\]

Here \(G_{M,J}\) is the local midpoint Gram on
\(V_M\oplus\mathcal R_J\), and \(G_{M-1,J}\) is its principal Gram on
\(V_{M-1}\oplus\mathcal R_J\).  Consequently every finite omitted block
\(\mathcal B\) gives the unconditional lower bound

\[
 \boxed{
 G_J\ge
 \sum_{n\in\mathcal B}
 \frac{\Lambda(n)}{\sqrt n}\,
 \kappa_{M,J}(\log n,W_n).}                                    \tag{6}
\]

Thus the desired finite directional-energy statement follows as soon as
one finds a finite block for which

\[
 \boxed{
 \sum_{n\in\mathcal B}
 \frac{\Lambda(n)}{\sqrt n}\,
 \kappa_{M,J}(\log n,W_n)>\delta_J.}                            \tag{7}
\]

Condition (7) is a rigorous finite sufficient crossing certificate.  It
does not follow from positivity alone.  The cofinal Christoffel sum is
positive and convergent, but the still-unproved strict comparison is

\[
 \boxed{
 \sum_{n>X}
 \frac{\Lambda(n)}{\sqrt n}\,
 \kappa_{M,J}(\log n,W_n)>\delta_J.}                            \tag{8}
\]

If (8) holds, a finite block satisfying (7) exists before the remaining
theta envelope becomes negligible.  If (8) fails, this particular sum of
separate local minima does not close the row, although the stronger joint
block Christoffel constant or the exact gain \(G_J\) can still do so.

## 1. Literal tail features and the anti-shorted old form

For every omitted prime power \(n=p^k>X\), put

\[
 w_n=\frac{\Lambda(n)}{\sqrt n},
 \qquad u_n=\log n,                                               \tag{9}
\]

and define the literal atom

\[
 \mathcal J_{u}(q,s)
 =\int_{\mathbb R}K(x)K(x-u)
 \{q(x)-q(x-u)\}
 \overline{\{s(x)-s(x-u)\}}\,dx.                               \tag{10}
\]

The complete omitted-tail feature \(V\) is normalized so that

\[
 \|Vq\|^2
 =\sum_{n>X}w_n\mathcal J_{u_n}(q,q).                            \tag{11}
\]

Let \(\Phi:\mathbb C^{M-1}\to V_{M-1}\) be the old-mode coordinate
map, and let \(\Psi:\mathbb C^J\to\mathcal R_J\) be the radical
coordinate map.  In the notation of 106.89,

\[
 U=V\Phi,
 \qquad W_R=V\Psi,
 \qquad
 \Pi_J=I-W_R(W_R^*W_R)^{-1}W_R^*.                              \tag{12}
\]

The matrix \(W_R^*W_R\) is positive definite by strict tail positivity
on every finite radical space.  Hence

\[
 \|\Pi_Jy\|^2
 =\inf_{r\in\mathcal R_J}\|y+Vr\|^2                           \tag{13}
\]

for every tail vector \(y\).  Let \(\widehat A\succ0\) be the preceding
old-mode matrix after the radical anti-short, and define

\[
 \widehat{\mathcal A}(\Phi\alpha,\Phi\beta)
 :=\alpha^*\widehat A\beta.                                    \tag{14}
\]

This is a positive-definite form on \(V_{M-1}\).

### Theorem 1 — Exact joint variational formula

The radical-conditioned adaptive gain is given by (3).

#### Proof

The exact adaptive identity of 106.89 is

\[
 G_J
 =\inf_{\alpha\in\mathbb C^{M-1}}
 \left\{
  \alpha^*\widehat A\alpha
  +\|\Pi_JV(q_J^*-\Phi\alpha)\|^2
 \right\}.                                                       \tag{15}
\]

Apply (13) with \(y=V(q_J^*-\Phi\alpha)\).  Then change variables
\(d=-\Phi\alpha\).  Since \(V_{M-1}\) is a vector space and the form in
(14) is quadratic,

\[
\begin{aligned}
 G_J
 &=\inf_{\alpha,\ r}
 \left\{
  \alpha^*\widehat A\alpha
  +\|V(q_J^*-\Phi\alpha+r)\|^2
 \right\}\\
 &=\inf_{d\in V_{M-1},\ r\in\mathcal R_J}
 \left\{
  \widehat{\mathcal A}(d,d)
  +\|V(q_J^*+d+r)\|^2
 \right\}.
\end{aligned}                                                     \tag{16}
\]

This proves (3).  Notice that the same radical correction \(r\) acts on
all omitted atoms.  It is not permissible to minimize independently in
the radical at each atom. \(\square\)

## 2. The radical-conditioned midpoint form

Put \(t=u/2\).  For \(W>0\), define

\[
\begin{aligned}
 \mathcal J_{u,W}(q,s)
 :=\int_{-W}^{W}&K(t+y)K(t-y)\\
 &\times\{q(t+y)-q(t-y)\}
 \overline{\{s(t+y)-s(t-y)\}}\,dy.
\end{aligned}                                                     \tag{17}
\]

Since \(K>0\),

\[
 0\le\mathcal J_{u,W}(q,q)\le\mathcal J_u(q,q).                \tag{18}
\]

All vectors in \(V_M\oplus\mathcal R_J\) are even and real analytic on
the real axis.  Two distinct asymptotic types occur:

* every \(v\in V_M\) is a finite sum of polynomial-exponential zero
  modes and satisfies \(v(x)\to0\) as \(x\to+\infty\);
* if \(0\ne r=\sum_{j=1}^Jc_jr_j\) and \(j_0\) is the largest index
  with \(c_{j_0}\ne0\), then the leading \(m=1\) theta term makes
  \(r(x)\) a nonconstant polynomial in \(e^{2x}\) to leading order,
  with its highest term supplied uniquely by \(r_{j_0}\).

These facts also prove

\[
 V_M\cap\mathcal R_J=\{0\}.                                    \tag{19}
\]

Indeed, a decaying finite zero-mode combination cannot equal a nonzero
radical combination with the stated leading growth.  Thus a basis of
\(V_M\), followed by \(r_1,\ldots,r_J\), is linearly independent.

### Lemma 2 — Local injectivity including the radical

For every \(u,W>0\),

\[
 \boxed{
 q\in V_M\oplus\mathcal R_J,
 \quad\mathcal J_{u,W}(q,q)=0
 \quad\Longrightarrow\quad q=0.}                               \tag{20}
\]

#### Proof

The integrand in (17) is nonnegative and its weight is strictly positive.
Therefore

\[
 q(t+y)=q(t-y)                                                   \tag{21}
\]

for almost every \(y\in(-W,W)\).  Real analyticity extends (21) first to
that entire interval and then to every real \(y\).  Hence \(q\) is
invariant under reflection about \(t\).  Evenness makes it invariant
under reflection about zero.  Composing the two reflections gives

\[
 q(x+u)=q(x)\qquad(x\in\mathbb R).                              \tag{22}
\]

Write \(q=v+r\), with \(v\in V_M\) and \(r\in\mathcal R_J\).  If
\(r\ne0\), its highest theta-polynomial term grows as \(x\to+\infty\),
while \(v(x)\to0\).  Such a function cannot be periodic, contradicting
(22).  Thus \(r=0\).  Now \(q=v\) is periodic and tends to zero at
\(+\infty\).  For every fixed \(x\),

\[
 q(x)=q(x+ku)\longrightarrow0
\]

as \(k\to\infty\), so \(q=0\). \(\square\)

The proof uses one physical displacement and an arbitrarily small open
midpoint aperture.  No prime-density theorem is involved.

## 3. The conditioned Christoffel determinant

Choose the ordered basis

\[
 \mathcal B_{M,J}
 =(\phi_1,\ldots,\phi_{M-1},r_1,\ldots,r_J;\phi_M)              \tag{23}
\]

of \(V_M\oplus\mathcal R_J\), and let \(G_{M,J}(u,W)\) be the Gram
matrix of (17) in this basis.  Let \(G_{M-1,J}(u,W)\) be the leading
principal block corresponding to \(V_{M-1}\oplus\mathcal R_J\).
Lemma 2 and the linear independence above imply

\[
 G_{M,J}(u,W)\succ0,
 \qquad G_{M-1,J}(u,W)\succ0.                                  \tag{24}
\]

Write

\[
 G_{M,J}(u,W)
 =\begin{pmatrix}G_{M-1,J}&g\\g^*&h\end{pmatrix}.              \tag{25}
\]

### Theorem 3 — Radical-conditioned local Christoffel bound

The constant in (4) satisfies (5).  In particular it is strictly
positive for every \(u,W>0\).

#### Proof

Every member of the affine class in (4) has coordinate vector
\((c,1)^T\) in (23).  Therefore

\[
 \mathcal J_{u,W}(q,q)
 =c^*G_{M-1,J}c+2\operatorname {Re}(c^*g)+h.                    \tag{26}
\]

Its unique minimum occurs at

\[
 c=-G_{M-1,J}^{-1}g
\]

and equals

\[
 h-g^*G_{M-1,J}^{-1}g
 =\frac{\det G_{M,J}}{\det G_{M-1,J}}.                          \tag{27}
\]

The value is positive because it is the Schur complement of a principal
block of the positive-definite matrix in (24). \(\square\)

The radical is inside the minimizing affine class in (4).  Thus (5) is
not the unconditioned constant of 106.87 with a posterior projection; it
is the local distance after allowing the radical to imitate the new mode.

## 4. Finite blocks and a stronger joint determinant

Let \(\mathcal B\) be any finite set of omitted prime powers.  Allow an
aperture \(W_n>0\) for each \(n\in\mathcal B\).  From (3), (11), and
(18), for every \(d,r\),

\[
\begin{aligned}
 &\widehat{\mathcal A}(d,d)
  +\|V(q_J^*+d+r)\|^2\\
 &\qquad\ge
 \sum_{n\in\mathcal B}w_n
 \mathcal J_{u_n,W_n}(q_J^*+d+r,q_J^*+d+r).
\end{aligned}                                                     \tag{28}
\]

Because \(q_J^*\in\phi_M+V_{M-1}\), varying \(d\) and \(r\) makes the
last argument range over the full affine class
\(\phi_M+V_{M-1}+\mathcal R_J\).  Taking the infimum and using
\(\inf_x\sum_na_n(x)\ge\sum_n\inf_xa_n(x)\) for nonnegative functions
gives

\[
\begin{aligned}
 G_J
 &\ge\inf_{q\in\phi_M+V_{M-1}+\mathcal R_J}
 \sum_{n\in\mathcal B}w_n\mathcal J_{u_n,W_n}(q,q)\\
 &\ge\sum_{n\in\mathcal B}w_n
 \inf_{q\in\phi_M+V_{M-1}+\mathcal R_J}
 \mathcal J_{u_n,W_n}(q,q)\\
 &=\sum_{n\in\mathcal B}w_n\kappa_{M,J}(u_n,W_n).
\end{aligned}                                                     \tag{29}
\]

This proves (6).

There is a stronger computable block constant.  Define

\[
 G_{M,J}^{\mathcal B}
 :=\sum_{n\in\mathcal B}w_nG_{M,J}(u_n,W_n),                    \tag{30}
\]

and let \(G_{M-1,J}^{\mathcal B}\) be its old-plus-radical principal
block.  It is positive definite, and the same Schur argument gives

\[
 \kappa_{M,J}^{\mathcal B}
 :=\frac{\det G_{M,J}^{\mathcal B}}
         {\det G_{M-1,J}^{\mathcal B}}
 =\inf_{q\in\phi_M+V_{M-1}+\mathcal R_J}
 \sum_{n\in\mathcal B}w_n\mathcal J_{u_n,W_n}(q,q).            \tag{31}
\]

Thus

\[
 \boxed{
 G_J\ge\kappa_{M,J}^{\mathcal B}
 \ge\sum_{n\in\mathcal B}w_n\kappa_{M,J}(u_n,W_n).}           \tag{32}
\]

The first inequality retains the fact that one common old-mode and
radical correction must fit every atom.  The second deliberately forgets
that incompatibility and is therefore weaker.

### Corollary 4 — Finite local crossing certificate

If either

\[
 \kappa_{M,J}^{\mathcal B}>\delta_J                              \tag{33}
\]

or the more elementary condition (7) holds, then

\[
 G_J>\delta_J,
\]

so the completed anti-shorted pivot is positive.  Cofinal monotone
convergence then supplies a finite ordinary-prime-power cutoff at which
the anti-shorted pivot is already positive.

The cutoff furnished by cofinal convergence need not be the largest atom
of \(\mathcal B\), because (3) uses the complete radical projection.  The
certificate is nevertheless finite: it consists of the finitely many
local Gram matrices in (30), and strictness is stable under sufficiently
large finite truncation of the remaining tail.

## 5. Cofinal sum and the theta envelope

For fixed \(M,J\), choose any apertures \(W_n>0\), and define

\[
 S_{M,J,X}^{\mathrm{loc}}
 :=\sum_{n>X}w_n\kappa_{M,J}(u_n,W_n).            \tag{34}
\]

Every term is strictly positive.  The series converges, because the zero
old-mode and radical correction is admissible in (4), so

\[
 0<\kappa_{M,J}(u_n,W_n)
 \le\mathcal J_{u_n,W_n}(\phi_M,\phi_M)
 \le\mathcal J_{u_n}(\phi_M,\phi_M),             \tag{35}
\]

and the last terms sum to the finite theta-tail energy of \(\phi_M\).
Moreover, for a finite-mode block the standard theta-overlap estimate
gives a superexponentially decreasing majorant for the remainder of (34).

Let

\[
 S(Y)=\sum_{X<n\le Y}w_n\kappa_{M,J}(u_n,W_n).                  \tag{36}
\]

Then \(S(Y)\uparrow S_{M,J,X}^{\mathrm{loc}}\).  Therefore

\[
 S_{M,J,X}^{\mathrm{loc}}>\delta_J                              \tag{37}
\]

is equivalent to the existence of a finite \(Y\) for which

\[
 S(Y)>\delta_J.                                                   \tag{38}
\]

This is the precise sense in which enough local directional energy must
be captured before the theta envelope decays: a strict surplus in the
cofinal sum is automatically witnessed by finitely many prime powers.

What has not been proved is (37).  The identities above give only

\[
 0<S_{M,J,X}^{\mathrm{loc}}\le G_J,
 \qquad
 G_J-\delta_J=\sigma_\infty.                                    \tag{39}
\]

Thus (37) is a sufficient inequality stronger than the exact completed
sign \(G_J>\delta_J\).  It may fail because separate atomwise minimizers
can vary with \(n\), even when the joint block constant in (31) succeeds.
The exact remaining hierarchy is

\[
 \boxed{
 \begin{array}{c}
 S_{M,J,X}^{\mathrm{loc}}>\delta_J
 \ \Longrightarrow\ 
 \sup_{\mathcal B\Subset\{n>X\}}
 \kappa_{M,J}^{\mathcal B}>\delta_J\\[2mm]
 \ \Longrightarrow\ G_J>\delta_J
 \ \Longleftrightarrow\ \sigma_\infty>0.
 \end{array}}                                                     \tag{40}
\]

The first implication is the new finite local route.  The reverse
implications are not formal and are not claimed.

## 6. Ledger entry

The finite radical no longer destroys the midpoint argument: the local
literal feature is injective on
\(V_M\oplus\mathcal R_J\), and its affine Schur complement gives the
strict determinant (5).  The complete adaptive gain is exactly the joint
old-mode/radical variational problem (3), so every finite block contributes
the rigorous amount in (6), with the stronger joint determinant (31).

The unresolved statement is now quantitative and scalar for each fixed
triple \((M,J,X)\): prove either the cofinal local surplus (37), a joint
finite-block surplus (33), or directly the exact matched-filter surplus
of 106.89.  Positivity and theta summability guarantee a finite witness
after a strict surplus exists; they do not manufacture the surplus.
