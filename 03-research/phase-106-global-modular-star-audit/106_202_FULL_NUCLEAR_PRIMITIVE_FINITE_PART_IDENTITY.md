# 106.202 — The full nuclear primitive finite-part identity

## 1. Purpose

Document 106.172 proves primitive--Gamma cancellation when every prime
row carries the same Hardy coefficient.  A vector in the restricted
adelic product has a more precise structure: it consists of one common
generic coefficient plus finitely many local deviations; the nuclear
completion permits rapidly summable deviations.

This note computes the matched finite part on that complete
generic-plus-residual module.  The common divergence cancels exactly
against the Gamma constant and every repeated prime winding.  All local
deviations remain as an absolutely convergent Euler form.  Consequently
the finite-part component of the chain defect in 106.201 vanishes on the
restricted-product core and on its natural nuclear completion.

No sign of the resulting residual form is asserted or needed here.

## 2. The generic-plus-residual boundary module

Let \(\mathscr K\) be the common coefficient Hilbert space.  For
\(p\) prime and \(k\geq1\), put

\[
 w_{p,k}={\log p\over p^k}.
\tag{1}
\]

Define the residual space \(\mathscr R_{\rm nuc}\) to consist of families
\(r=(r_{p,k})\subset\mathscr K\) for which

\[
 \boxed{
 \|r\|_{\mathscr R}
 :=\sum_{p,k}w_{p,k}\|r_{p,k}\|
 +\left(\sum_{p,k}w_{p,k}\|r_{p,k}\|^2\right)^{1/2}
 <\infty.}
\tag{2}
\]

The algebraic restricted-product core, where only finitely many
\(r_{p,k}\) are nonzero, is dense.  A boundary vector is a pair

\[
 \boxed{(F,r)\in\mathscr K\oplus\mathscr R_{\rm nuc},}
\tag{3}
\]

representing the local rows

\[
 F_{p,k}=F+r_{p,k}.
\tag{4}
\]

The decomposition (4) is the linearized restricted-product
decomposition: \(F\) is the common spherical/generic component and
\(r_{p,k}\) records local modifications.

## 3. The matched regularized form

For \(s>1/2\), set

\[
 a_p(s)=(\log p)p^{-2s},
 \qquad
 C_s=\sum_pa_p(s).
\tag{5}
\]

For \(x=(F,r)\) and \(y=(G,z)\), define

\[
 \begin{aligned}
 \mathfrak Q_s(x,y)
 &=\sum_pa_p(s)
   \langle F+r_{p,1},G+z_{p,1}\rangle\\
 &\quad+\gamma\langle F,G\rangle\\
 &\quad+\sum_p\sum_{k\geq2}w_{p,k}
   \langle F+r_{p,k},G+z_{p,k}\rangle .
 \end{aligned}
\tag{6}
\]

The first line is the Abel-regularized primitive layer.  The second is the
Gamma finite line, and the third contains all repeated windings.  For
\(s>1/2\), (6) converges absolutely on (3):
\(a_p(s)\leq w_{p,1}\), and (2) controls both cross terms and residual
products.

Retain

\[
 \kappa_\infty
 =\gamma+\sum_p\sum_{k\geq2}w_{p,k}.
\tag{7}
\]

Document 106.172 proves

\[
 \mathrm{FP}_{s\downarrow1/2}C_s=-\kappa_\infty.
\tag{8}
\]

## 4. Exact full finite part

### Theorem 4.1 — Generic cancellation and residual stabilization

For every \(x=(F,r)\), \(y=(G,z)\) in (3), the finite part of (6)
exists and equals

\[
 \boxed{
 \begin{aligned}
 \mathrm{FP}_{s\downarrow1/2}\mathfrak Q_s(x,y)
 &=\sum_p\sum_{k\geq1}w_{p,k}
 \bigl(
   \langle r_{p,k},G\rangle
  +\langle F,z_{p,k}\rangle
  +\langle r_{p,k},z_{p,k}\rangle
 \bigr).
 \end{aligned}}
\tag{9}
\]

In particular, on the common generic diagonal,

\[
 \boxed{
 \mathrm{FP}_{s\downarrow1/2}
 \mathfrak Q_s((F,0),(G,0))=0.}
\tag{10}
\]

The convergence in (9) is absolute and the resulting sesquilinear form is
continuous on \(\mathscr K\oplus\mathscr R_{\rm nuc}\).

#### Proof

Expand the primitive line in (6):

\[
 \begin{aligned}
 &C_s\langle F,G\rangle\\
 &\quad+\sum_pa_p(s)
 \bigl(
  \langle r_{p,1},G\rangle
 +\langle F,z_{p,1}\rangle
 +\langle r_{p,1},z_{p,1}\rangle
 \bigr).
 \end{aligned}
\tag{11}
\]

Expand the repeated-winding line in the same way.  The complete
coefficient of \(\langle F,G\rangle\) is

\[
 C_s+\gamma+\sum_{p,k\geq2}w_{p,k}.
\tag{12}
\]

Its finite part is zero by (7)--(8).  For every residual term,
\(a_p(s)\to w_{p,1}\).  The summable majorants in (2), together with
Cauchy--Schwarz for the double-residual term, permit dominated convergence.
This gives (9).  Absolute convergence and continuity follow from

\[
 \begin{aligned}
 \sum_{p,k}w_{p,k}|\langle r_{p,k},G\rangle|
 &\leq\|G\|\sum_{p,k}w_{p,k}\|r_{p,k}\|,\\
 \sum_{p,k}w_{p,k}|\langle r_{p,k},z_{p,k}\rangle|
 &\leq
 \left(\sum w_{p,k}\|r_{p,k}\|^2\right)^{1/2}
 \left(\sum w_{p,k}\|z_{p,k}\|^2\right)^{1/2}.
 \end{aligned}
\tag{13}
\]

Taking \(r=z=0\) proves (10). \(\square\)

## 5. Boundary interpretation

The common component in (12) consists of two opposite rows:

* the finite part of the primitive plane has Gram operator
  \(-\kappa_\infty I\);
* the Gamma plus repeated-winding row \(B_\infty\) has Gram operator
  \(+\kappa_\infty I\).

Thus (10) is the bilinear extension of 106.172(17).  Formula (9) shows
what happens away from the common diagonal: the common terms still cancel,
while every deviation remains with its literal von Mangoldt weight.  Those
terms belong to the connected Euler localization and must not be moved
into the Gamma counterspace.

Let \(\eta\) extract the common component \(F\) in (3), and let
\(\mathrm{res}(F,r)=r\).  On the algebraic restricted-product
core, the full boundary localization therefore decomposes as

\[
 \boxed{
 \mathrm{Loc}_{\rm bd}(F,r)
 =d_{\rm bd}\eta(F,r)
  +\mathrm{Loc}_{\rm Euler}(r),}
\tag{14}
\]

where \(d_{\rm bd}\) is the co-diagonal primitive--Gamma row.  Equation
(14) is an equality before taking a norm: the first term carries the
common coordinate and the second the finite local deviations.

### Corollary 5.1 — Vanishing of the finite-part chain defect

On the algebraic restricted-product boundary core, and by continuity on
\(\mathscr K\oplus\mathscr R_{\rm nuc}\), the finite-part defect of
106.201(17) has zero class in the co-diagonal cokernel:

\[
 \boxed{[\Delta_{{\rm fp},S}]=0.}
\tag{15}
\]

#### Proof

The common part of (14) lies in the image of the co-diagonal by definition
and hence has zero cokernel class.  The residual part is retained in the
Euler coordinate on both sides of the comparison, with the identical
weights (1), as shown by (9).  Their difference is zero.  Continuity from
(13) gives the nuclear extension. \(\square\)

Combining Corollary 5.1 with Corollary 5.1 of 106.201 removes the complete
finite-level chain defect, up to the identification of the actual CCM
generic boundary with the restricted-product decomposition (3)--(4).
On the algebraic adelic core that identification is canonical; on the
Meyer completion it is the continuous extension furnished by (2).

## 6. What this closes and what it does not

The theorem closes:

* the extension of the scalar identity of 106.172 to independent local
  deviations;
* exact cancellation of the common primitive divergence;
* retention of every residual prime-power coefficient;
* the finite-level co-diagonal chain identity, after the unitary Gamma
  identification of 106.201.

It does not prove that the induced map on the completed CCM cokernel is
faithful.  That is the cofinal Hilbert-closure identity 106.200(24).  Nor
does it identify the new metric with the fixed Rosati metric; the latter
identification is unnecessary on the alternative-polarization branch by
Theorem 8.1 of 106.200.

## 7. Status

Proved without RH or zero input:

* a complete nuclear generic-plus-residual boundary module;
* the exact matched finite part on that module;
* bilinear primitive--Gamma--repeated-winding cancellation;
* absolute convergence and continuity of every residual term;
* vanishing of the finite-part chain defect in the co-diagonal cokernel.

Still required:

* the charged cofinal Hilbert-closure identity 106.200(24).
