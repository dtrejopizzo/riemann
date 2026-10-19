# R183.010 — The central--tangent transversal defect

## 0. Result

D.247's coligation and the semilocal central state can be assembled in two ways. The direct sum preserves an isometry but does not contain the score. Superposition in a single channel contains the score and produces a single transversal defect. All quadratic terms cancel exactly by D.247.

This identity algebraically realizes a prior cancellation of the white
light. However, the audit distinguishes two central states: the
vector \(\Sigma_S\) used here and the **dual** state required by D.245.
This file's defect recovers the coordinate \(x_p\), but not the
resolvent containing all powers \(p^k\). Hence it is not yet
D.245's full pairing.

## 1. Finite data

Fix a finite set of primes \(S\). Use

\[
 \Sigma_S=\bigotimes_{p\in S}\sigma_p,
 \qquad
 \mathcal E_\pm c=\sum_{p\in S}c_pe_{p,\pm}.        \tag{1.1}
\]

Let \(J\) be R183.009's diagonal operator,

\[
             (Jc)_p=J_pc_p,
 \qquad J_p=\sqrt{2\over\log p}.                   \tag{1.2}
\]

Apply D.247's conservative identity to the source vector \(Jc\):

\[
 \|\mathcal E_-(Jc)\|^2+A_S|x^*Jc|^2
 =\|\mathcal E_+(Jc)\|^2
  +A_S\sum_p|x_pJ_pc_p|^2.                          \tag{1.3}
\]

## 2. Two superposed columns

For \(\alpha\in\mathbb C\) and \(c\in\mathbb C^S\), define

\[
 \mathfrak C_S(\alpha,c)=
 \begin{pmatrix}
  \alpha\Sigma_S+\mathcal E_-(Jc)\\
  \sqrt{A_S}\,x^*Jc
 \end{pmatrix},                                     \tag{2.1}
\]

\[
 \mathfrak T_S(\alpha,c)=
 \begin{pmatrix}
  \alpha\Sigma_S+\mathcal E_+(Jc)\\
  \sqrt{A_S}\,(x_pJ_pc_p)_{p\in S}
 \end{pmatrix}.                                     \tag{2.2}
\]

The superposition occurs in the first component. Since \(\Sigma_S\) is Fourier-even and \(e_{p,-}\) is Fourier-odd,

\[
             \langle\Sigma_S,\mathcal E_-(Jc)\rangle=0. \tag{2.3}
\]

By contrast,

\[
 \langle\Sigma_S,e_{p,+}\rangle
 =A_Sx_p.                                            \tag{2.4}
\]

The last formula follows from D.244(1.7)--(2.4): the spectator factor is \(A_S/a_p\) and \(b_p/a_p=x_p\).

## 3. Transversal defect identity

### Theorem 3. `PROVED`

\[
 \boxed{
 \|\mathfrak T_S(\alpha,c)\|^2
 -\|\mathfrak C_S(\alpha,c)\|^2
 =2A_S\operatorname{Re}
   \left(\overline\alpha\sum_{p\in S}x_pJ_pc_p\right).} \tag{3.1}
\]

**Proof.** Expand both norms. The terms \(|\alpha|^2\|\Sigma_S\|^2\) cancel. The input transversal term is zero by (2.3). The difference of the remaining quadratic terms is zero by (1.3). Only the output transversal term remains, and (2.4) gives (3.1). \(\square\)

No inequality has been used.

## 4. Relation to the score and the duality defect

By R183.009,

\[
 J_p^2{\|d_{p,+}\|^2\over a_p}=-x_p.               \tag{4.1}
\]

The right-hand side of (3.1) contains the local coordinate \(x_p\). D.245's full prime score is, by contrast,

\[
 \operatorname{score}_p=2d_{p,+}(h_p^*)^{-1},
 \qquad h_p=1-p^{-1/2}U_p.                          \tag{4.2}
\]

The second factor is the dual Euler state
\(\eta_p=(h_p^*)^{-1}\), while \(\Sigma_S\) contains the direct
central state \(h_p\). They are biorthogonal, \(h_p^*\eta_p=1\), but
they are neither the same vector nor do they have the same norm.

Inserting only the orbit coordinate

\[
 c_p=\sum_{k\ge1}p^{-k/2}a_{p^k},                  \tag{4.3}
\]

does not replace \(h_p\) by \(\eta_p\). Hence (3.1) has not been
identified with the operator

\[
 \sum_{p\in S}\sum_{k\ge1}{\log p\over p^{k/2}}
       (U_p^k+U_p^{*k}).                            \tag{4.4}
\]

Equality with (4.4) requires keeping the dual state inside the
column. This is an additional step, not a diagonal congruence.

## 5. What the white light cancellation achieved

In columns (2.1)--(2.2), the central state \(\alpha\Sigma_S\) is identical on input and output. Its norm, responsible for the white-light residue, cancels before any limit is taken. The tangent squares and the degree/contact ports cancel by conservation (1.3). The only remaining term is the central--tangent interference.

Thus (3.1) meets the structural requirement of cancelling the common
central state within the columns, but it pays for that cancellation by
using the direct state on both sides. It still does not cancel the white
light of the dual column that produces the full score.

But a difference of norms of columns that are isometric except for a transversal term still has no sign. Obtaining one requires an extended coligation turning \(\mathfrak C_S\) into \(\mathfrak T_S\) via a contraction over the semilocal support class.

## 6. Resulting global target

First, an extended column must be built containing simultaneously
the biorthogonal pair \((h_p,(h_p^*)^{-1})\), whose Gram matrix remains
positive. Only afterward can D.246's archimedean channel be attached. If
those full columns exist, the required transport theorem is:

\[
 \boxed{
 \Pi_{T,\mathrm{Tate}}\mathfrak T_{S,\infty}C_h
 =\Theta_{q,h}\,
   \Pi_{T,\mathrm{Tate}}\mathfrak C_{S,\infty}C_h,
 \qquad \|\Theta_{q,h}\|\le1,}                    \tag{6.1}
\]

with \(S=S(q)\) and \(\operatorname{supp}h\subset(-T,T)\). The map \(\Theta_{q,h}\) must be built via R183.004's Poisson--Möbius factorization.

If the dual extension exists and (6.1) holds with the indicated
orientation, D.245--D.246 and the semilocal trace identify their
difference with Weil's form. Then D is closed. Column (2.1)--(2.2), without
that extension, is not enough.

## 7. Logical status

* Superposed columns (2.1)--(2.2): **CONSTRUCTED** at the finite level.
* Cancellation of white light within the columns: **PROVED**.
* Transversal identity (3.1): **PROVED**.
* Identification of the defect with the coordinate \(x_p\): **PROVED**.
* Identification of (3.1) with the full Eulerian score: **FALSE**;
  the resolvent dual state is missing.
* Dual pairing that does produce the score: **PROVED** in D.245.
* Positive Hilbertian column containing both direct and dual: **OPEN**.
* Contractive semilocal transport (6.1): **OPEN**.
* Row D: **OPEN**.
