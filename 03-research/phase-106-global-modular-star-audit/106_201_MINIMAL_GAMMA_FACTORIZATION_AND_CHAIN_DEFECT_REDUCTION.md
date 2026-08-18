# 106.201 — Minimal Gamma factorization and reduction of the chain defect

## 1. Purpose

The chain defect in 106.200 compares the actual archimedean CCM
localization with the charged Gamma row.  The nonzero-frequency part was
known only through equality of quadratic forms.  A quadratic-form identity
does not imply literal equality inside two preassigned Hilbert targets,
but it does imply something exactly sufficient for a pushout: the two
minimal gradient realizations are uniquely unitarily equivalent.

This note proves that statement and applies it to the complete
charge-shifted Gamma energy.  After the canonical unitary identification,
the nonzero-frequency component of the chain defect vanishes.  The only
remaining component is the scalar primitive/repeated-winding finite-part
row.  Document 106.172 proves that row on the common Hardy sector; its
extension to the full nuclear generic-length module is the next exact
calculation.

## 2. Uniqueness of a minimal Gram factorization

Let \(D\) be a complex vector space and let

\[
 G_j:D\longrightarrow H_j,
 \qquad j=1,2,
\tag{1}
\]

be linear maps into Hilbert spaces.  Call the realization minimal if

\[
 H_j=\overline{\operatorname {span}G_j(D)}.
\tag{2}
\]

### Theorem 2.1 — Minimal factorization uniqueness

Assume

\[
 \boxed{
 \langle G_1x,G_1y\rangle_{H_1}
 =\langle G_2x,G_2y\rangle_{H_2}
 \quad(x,y\in D).}
\tag{3}
\]

Then there is a unique unitary

\[
 \boxed{U:H_1\longrightarrow H_2,
 \qquad UG_1=G_2.}
\tag{4}
\]

#### Proof

On the algebraic span of \(G_1(D)\), set

\[
 U_0\!\left(\sum_jG_1x_j\right)=\sum_jG_2x_j.
\tag{5}
\]

Equation (3) shows that the squared norm of either side of (5) is the same
double Gram sum.  Hence a zero presentation on the left has zero image on
the right, so \(U_0\) is well defined and isometric.  Minimality makes its
initial and final spans dense.  It therefore extends to a unitary (4).
The intertwining identity holds on \(D\), and density proves uniqueness.
\(\square\)

The theorem is the Hilbert-space uniqueness of the minimal Kolmogorov
decomposition of a positive kernel.  No positivity of the CCM Rosati form
is involved; only the already positive local Gamma Green form is used.

## 3. The canonical CCM Gamma gradient

Let \(\mathscr D_Q\) be the common smooth core of the total charge
generator

\[
 A_Q=A-L_Q
\tag{6}
\]

from 106.200.  Define the positive sesquilinear form

\[
 \begin{aligned}
 \mathfrak e_{\Gamma,Q}(F,G)
 =2\int_0^\infty g_\Gamma(u)
 \langle(I-e^{iuA_Q})F,(I-e^{iuA_Q})G\rangle\,du.
 \end{aligned}
\tag{7}
\]

The charge twist is a unitary character on each fiber.  Therefore the
local Green calculation of 106.176 applies fiber by fiber and gives the
archimedean CCM difference energy with Mellin frequency
\(\gamma-\log q\).

Form the pre-Hilbert quotient

\[
 \mathscr D_Q/\ker\mathfrak e_{\Gamma,Q}
\tag{8}
\]

and let \(H_{\Gamma,Q}^{\rm CCM}\) be its completion.  Denote the
canonical map by

\[
 \delta_{\Gamma,Q}^{\rm CCM}:\mathscr D_Q
 \longrightarrow H_{\Gamma,Q}^{\rm CCM}.
\tag{9}
\]

By construction,

\[
 \langle\delta_{\Gamma,Q}^{\rm CCM}F,
        \delta_{\Gamma,Q}^{\rm CCM}G\rangle
 =\mathfrak e_{\Gamma,Q}(F,G).
\tag{10}
\]

## 4. Identification with the explicit charged gradient

The explicit map of 106.200 is

\[
 (\mathcal G_{\Gamma,Q}F)(u)
 =\sqrt{2g_\Gamma(u)}(I-e^{iuA_Q})F.
\tag{11}
\]

Let

\[
 H_{\Gamma,Q}^{\rm exp}
 =\overline{\operatorname {Ran}\mathcal G_{\Gamma,Q}}
 \subset L^2((0,\infty),du;\mathscr K_Q).
\tag{12}
\]

### Theorem 4.1 — Canonical unitary Gamma comparison

There is a unique unitary

\[
 \boxed{
 U_{\Gamma,Q}:H_{\Gamma,Q}^{\rm CCM}
 \longrightarrow H_{\Gamma,Q}^{\rm exp}}
\tag{13}
\]

such that

\[
 \boxed{
 U_{\Gamma,Q}\delta_{\Gamma,Q}^{\rm CCM}
 =\mathcal G_{\Gamma,Q}.}
\tag{14}
\]

It intertwines the Hodge coefficient structure, normalized real scaling,
and every charge operator commuting with \(A_Q\).

#### Proof

Equations (7), (10), and (11) give

\[
 \langle\delta_{\Gamma,Q}^{\rm CCM}F,
        \delta_{\Gamma,Q}^{\rm CCM}G\rangle
 =\langle\mathcal G_{\Gamma,Q}F,
        \mathcal G_{\Gamma,Q}G\rangle.
\tag{15}
\]

Both targets are minimal by (9) and (12), so Theorem 2.1 gives (13)--(14).
Any symmetry commuting with \(A_Q\) preserves the common Gram form (7).
Applying the uniqueness clause in Theorem 2.1 to the two possible
intertwiners proves covariance. \(\square\)

This theorem is stronger than equality of multipliers: it identifies the
complete minimal boundary Hilbert modules and their group actions.

## 5. Reduction of the complete archimedean defect

Split the full archimedean row into its zero-mode finite-part component and
its nonzero Gamma gradient:

\[
 L_\infty^{\rm CCM}
 =L_{\rm fp}^{\rm CCM}\oplus
   \delta_{\Gamma,Q}^{\rm CCM},
 \qquad
 \mathbb B_{\infty,Q}
 =B_\infty\oplus\mathcal G_{\Gamma,Q}.
\tag{16}
\]

Conjugate the first target by
\(I\oplus U_{\Gamma,Q}\).  Theorem 4.1 makes the nonzero-frequency rows
identical.  Hence the chain defect of 106.200(22) becomes

\[
 \boxed{
 \Delta_{\Gamma,S}
 \simeq
 \Delta_{{\rm fp},S}\oplus0,
 \qquad
 \Delta_{{\rm fp},S}
 :=L_{\rm fp}^{\rm CCM}\rho_S^\natural-B_\infty\eta_S.}
\tag{17}
\]

The symbol \(\simeq\) means equality after the canonical unitary change
of minimal Gamma realization.  Orthogonal cokernels and their Schur
metrics are unchanged by this unitary change of target.

### Corollary 5.1 — The Gamma spin is no longer an open chain component

The image of \(\Delta_{\Gamma,S}\) in the charged co-diagonal cokernel
vanishes if and only if the image of \(\Delta_{{\rm fp},S}\) vanishes.

#### Proof

The unitary in (13) maps the nonzero-frequency component of one
co-diagonal row exactly to the other and leaves the finite-part component
unchanged.  It therefore induces a unitary of the corresponding
cokernels.  Equation (17) proves the assertion. \(\square\)

## 6. The remaining finite-part extension

On the common Hardy boundary sector, 106.172 proves

\[
 \operatorname {FP}_{s\downarrow1/2}\|B_sF\|^2
 +\|B_\infty F\|^2=0,
 \qquad
 B_\infty^*B_\infty=\kappa_\infty I.
\tag{18}
\]

By polarization, (18) identifies the Gram form of the finite-part row on
that sector.  What it does not prove is that the full nuclear
generic-length boundary of an arbitrary CCM restriction vector factors
through one common coefficient \(\eta_S\).  The remaining identity is

\[
 \boxed{
 L_{\rm fp}^{\rm CCM}\rho_S^\natural
 =B_\infty\eta_S
 \quad\text{in the co-diagonal quotient}.}
\tag{19}
\]

Unlike the Gamma gradient, this cannot be obtained from local form
uniqueness until the full finite-part Gram form has been computed on
independent prime-power boundary data.  Equation (19) is therefore the
single finite-level chain calculation left before the cofinal closure
gate of 106.200(24).

## 7. Status

Proved without RH or zero input:

* uniqueness of every minimal Hilbert factorization of a positive Green
  kernel;
* the canonical CCM Gamma gradient as a form completion;
* unitary equivalence of that gradient with the explicit
  charge-shifted Gamma connection;
* compatibility of the unitary with Hodge, scaling, and charge symmetries;
* elimination of the complete nonzero Gamma component from the chain
  defect.

Still required:

* the full nuclear primitive/repeated-winding finite-part identity (19),
  extending 106.172 beyond the common Hardy diagonal;
* the charged cofinal Hilbert-closure identity 106.200(24);
* bounded weak nondegeneracy of the descended CCM alternating form.
