# R170_864 — Incidence--Poisson gluing: the admissible normal does not contain K2

## 0. Result

R170_863 builds a positive incidence cell whose arithmetic anchor
is null and whose normal jet is

\[
 H_- =\mathcal A^{\rm raw}-K_- .                           \tag{0.1}
\]

The physical PC uses that cell with negative sign. Its oriented normal is

\[
 \mathcal N_H:=-H_-=-\mathcal A^{\rm raw}+K_-.             \tag{0.2}
\]

The Poisson--`X` jet simultaneously contains

\[
 \mathcal N_X:=-K_-.                                       \tag{0.3}
\]

Upon gluing both cells along their Chebyshev face,

\[
 \boxed{\mathcal N_X+\mathcal N_H=-\mathcal A^{\rm raw}.} \tag{0.4}
\]

The reflected orientation satisfies the same law:

\[
 \boxed{-JK_-\mathscr F-JH_-\mathscr F
       =-J\mathcal A^{\rm raw}\mathscr F.}                 \tag{0.5}

Therefore the divisor anchor is genuine, but it leaves neither a `K2` jet nor
a Selberg term in the full PC complex. The required Green map
must act on the reduced ledger of R170_856(3.5). Applying it only to the
incidence normal would repeat exactly the invalid separation of
R170_855.

## 1. The two cells

The hyperbolic cell is the relation

\[
 H(r,q)=L(r)S(q)-K(r,q).                                   \tag{1.1}

Its antidiagonal derivative is

\[
 H_- =\dot LS-L\dot S-K_-
     =\mathcal A^{\rm raw}-K_-.                            \tag{1.2}

R170_863 realizes the interior block of (1.1) as the boundary of the
incidence vector `e_Lambda(r,q;F)`. Positivity belongs to the Laplacian
of that boundary; the PC orientation is `-H`, giving (0.2).

The Poisson cell is obtained from the identity prior to the
hyperbolic substitution

\[
 \{X_r,E(r,q)\}\mathscr F_r
 =S(q)\mathcal M_r-K(r,q)-JK(r,q)\mathscr F_r.             \tag{1.3}

Its jet contains

\[
 -K_- -JK_-\mathscr F-JK\dot{\mathscr F},                 \tag{1.4}

in addition to `S dot M-dot S M`. The first two pieces of (1.4) are the
faces that are glued to (0.2) and its reflection.

## 2. Gluing along the Chebyshev face

Formally introduce a common face `C_K` with two oriented inclusions:

\[
 \iota_X(C_K)=-K_-,\qquad \iota_H(C_K)=+K_-.               \tag{2.1}

The algebraic pushout of the two cells identifies those copies. The
boundary of the glued object is the sum of boundaries and the interior
face cancels:

\[
 (-K_-)+(-\mathcal A^{\rm raw}+K_-)
 =-\mathcal A^{\rm raw}.                                  \tag{2.2}

A topological realization of the pushout is not needed for (2.2): it is the
exact operator ledger of R170_856(3.3). The language of cells only
records which terms are internal faces and which reach the physical boundary.

The same identification after `J` and `mathscr F` gives (0.5). Since the
gluing occurs before compression, every copy of the atoms of
`K_-` also cancels distribution by distribution.

## 3. Full normal of the PC complex

After gluing, the PC derivative is

\[
\begin{aligned}
 \mathcal N_{PC}={}&S\dot{\mathcal M}-\dot S\mathcal M\\
 &-\dot L^*E\mathscr F-L^*E_-\mathscr F-L^*E\dot{\mathscr F}\\
 &-J\mathcal A^{\rm raw}\mathscr F
   -JK\dot{\mathscr F}-JH\dot{\mathscr F}
   -\mathcal A^{\rm raw}.                                 \tag{3.1}
\end{aligned}

This is exactly R170_856(3.5). The tail `H`, the Fourier jet, the
archimedean multiplier and both orientations are exterior faces;
they are not eliminated in the Chebyshev gluing.

After compression and Möbius extraction, the additional boundary is

\[
 \mathcal R_{\rm cross}
 +\mathcal P^{\rm comb}_{N,T}
 +B_\mu P\mathcal P_{C,A},                                \tag{3.2}

by R170_856(11.2). Hence the admissible normal for a Green map is the
pair `(N_PC, boundary (3.2))`, not `H_-` in isolation.

## 4. What survives from the incidence anchor

The anchor `e_Lambda in ker Delta_{M,N}` of R170_863 survives as an
exact arithmetic substructure:

* it certifies that face `K` is indeed interior for `k<=N`;
* it distinguishes `Lambda` from every modification in `[1,N]`;
* it explains why no divisor defect remains in the complete fibers.

What does not survive is its normal `A_raw-K_-` as a separate physical
observable. The gluing sends that normal to `-A_raw` together with the Poisson cell.

Thus unique factorization provides an **exact gluing condition**, not
a terminal positive energy. The new law must use that condition when
comparing the exterior boundary of (3.1)--(3.2) with the Tate anchor, without
reopening the internal face.

## 5. Corrected Green target

Let `mathfrak L_T(f)=mathfrak W_K(f)+Theta_ext(f)` be the functional of
R170_862. The correct target is a typed linear map

\[
 \mathfrak G_T^{\rm glue}:
 (\mathcal N_{PC},\mathcal R_{\rm cross},
  \mathcal P^{\rm comb},B_\mu P\mathcal P_{C,A})
 \longrightarrow\mathbb R                                 \tag{5.1}

such that

\[
 \boxed{
 \mathfrak G_T^{\rm glue}(f)=\mathfrak L_T(f).}            \tag{5.2}

The graded Green identity of R170_854 already gives a reading of (5.2), but not
its vanishing. To close it, the incidence null anchor must be extended to
a null anchor of the glued complex whose second component is the
exterior--Tate port of R170_862. That extension is now the only part not
yet built of the anchor mechanism.

## 6. Status

```text
hyperbolic normal H_-=A_raw-K_-                            PROVED
Poisson normal contains -K_- in both orientations          PROVED
gluing cancels all K_-                                     PROVED
glued normal matches R170_856(3.5)                         PROVED
incidence anchor distinguishes Lambda                      RETAINED
isolated incidence normal is a physical observable         REFUTED
null extension of the anchor to the exterior--Tate port     OPEN
exterior law / VIR--LB / D                                 OPEN
```
