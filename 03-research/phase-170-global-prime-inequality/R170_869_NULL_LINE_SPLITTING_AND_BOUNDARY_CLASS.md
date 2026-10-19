# R170_869 — Universal splitting: every novelty lives on the Lambda line

## 0. Result

R170_868 proves that every linear row annihilating the line
`K_N=R(Lambda,1)` factors through `mathscr D_N`. Here all
rows are classified, without requiring that they annihilate `K_N`.

Let `Y` be a vector space and

\[
 \ell:(\mathbb R^N\oplus\mathbb R)\otimes\mathcal H
 \longrightarrow Y                                        \tag{0.1}
\]

linear. Then there exists a unique decomposition

\[
 \boxed{
 \ell((a,c)\otimes F)
 =Q\bigl(\boldsymbol{\mathscr D}_N((a,c)\otimes F)\bigr)
  +c\,\beta_\ell(F),}                                     \tag{0.2}

where

\[
 \boxed{\beta_\ell(F):=\ell((\Lambda,1)\otimes F).}       \tag{0.3}

The first part contains every divisor defect and every factored PC
extension. The second is a single boundary class supported on the
null arithmetic line. No linear identity derived from
`Lambda*1=log` determines `beta_ell`: that identity only says that the
first part vanishes on the line.

For the physical functional of R170_856--859, the scalar class is

\[
 \boxed{\beta_{\rm phys}(F)
 =g_\epsilon\Delta^{\rm Tate}(F)
 =\mathfrak W_K(F)+\Theta_{\rm ext}(F).}                   \tag{0.4}

Thus the exterior problem is exactly the vanishing of the boundary class
in the quotient by all factored identities. PC, Möbius and the
incidence determine the normal representative `Q`, but they are algebraically
silent about (0.4). Minimality must act directly on that
class.

## 1. Canonical section of the defect

Write

\[
 \mathscr D_N=W_N(U_Na-c\log),                             \tag{1.1}
\]

where `W_N=diag(k^{-1/2})` and `U_Na=a*1`. Both `W_N,U_N` are
invertible. Define a right section

\[
 \sigma_N(v):=(U_N^{-1}W_N^{-1}v,0).                       \tag{1.2}
\]

Then

\[
 \mathscr D_N\sigma_N(v)=v.                               \tag{1.3}

For `x=(a,c)`, set `v=mathscr D_Nx`. Since

\[
 \mathscr D_N(x-\sigma_N(v))=0,                            \tag{1.4}

Theorem 2.1 of R170_866 gives

\[
 x-\sigma_N(v)=t(\Lambda,1).                              \tag{1.5}

The last coordinate of `sigma_N(v)` is zero, so `t=c`. Hence
one obtains the canonical decomposition

\[
 \boxed{x=\sigma_N(\mathscr D_Nx)+c(\Lambda,1).}           \tag{1.6}

## 2. Proof of (0.2)

Tensor (1.6) with `F` and apply `ell`:

\[
\begin{aligned}
 \ell(x\otimes F)
 ={}&\ell(\sigma_N(\boldsymbol{\mathscr D}_N(x\otimes F)))\\
 &+c\,\ell((\Lambda,1)\otimes F).                         \tag{2.1}
\end{aligned}

Define

\[
 Q:=\ell\circ(\sigma_N\otimes I).                         \tag{2.2}

With (0.3), equation (2.1) is (0.2). The section (1.2) fixes the
uniqueness of `Q`; `beta_ell` is intrinsic because it is the restriction of
`ell` to the kernel.

A different choice of section changes `Q` by a row taking values in the
boundary class, but does not change (0.3). Hence `beta_ell` is the
coordinate-independent quantity.

## 3. Quotient of linear extensions

Let `Hom(E,Y)` be the space of linear rows on
`E=(R^N direct-sum R) tensor H`, and let

\[
 \mathcal I_D:=\{Q\boldsymbol{\mathscr D}_N:Q\text{ linear}\}. 
                                                                    \tag{3.1}
\]

Restriction to the kernel induces an isomorphism

\[
 \boxed{
 \operatorname{Hom}(E,Y)/\mathcal I_D
 \simeq\operatorname{Hom}(\mathcal H,Y),}                 \tag{3.2}
\]

sending the class of `ell` to `beta_ell`. This is the exact sequence

\[
 0\longrightarrow\mathcal I_D
 \longrightarrow\operatorname{Hom}(E,Y)
 \xrightarrow{\operatorname{res}_{K_N}}\operatorname{Hom}(\mathcal H,Y)
 \longrightarrow0.                                       \tag{3.3}

The last arrow is surjective: given any `beta`, the row
`ell_beta((a,c) tensor F)=c beta(F)` realizes it.

Hence there is no purely algebraic obstruction to any value of
the exterior class. Arithmetic fixes the subspace it lives in, but not its
value.

## 4. Identification of the physical class

At a parity, R170_856 gives the linear functional

\[
 \mathfrak L_T(F)
 =(b,P\dot AF)-(h,P\mathcal C F)-\rho_Fg_\epsilon.         \tag{4.1}

R170_859 proves, under REG/C1, the gauge-invariant form

\[
 \mathfrak L_T(F)=\mathfrak W_K(F)+\Theta_{\rm ext}(F).    \tag{4.2}

Define a boundary-augmented row `ell_phys` on the homogenized
coefficients so that its restriction to `(Lambda,1) tensor F` is (4.1), while its
components off the line are written via the homogeneous PC of
R170_867. Then (0.2) takes the form

\[
 \ell_{\rm phys}((a,c)\otimes F)
 =Q_{PC}\boldsymbol{\mathscr D}_N((a,c)\otimes F)
  +c\mathfrak L_T(F).                                      \tag{4.3}

The first summand contains the divisor defect. For `a=Lambda,c=1`
it vanishes and exactly `mathfrak L_T(F)` remains.

Thus any attempt to show (4.1)=0 by manipulating only the first
summand is circular: it works in the ideal `I_D`, while the
sought-after quantity is the quotient class.

## 5. Exact entry point of minimality

First-contact minimality is not a coefficient identity.
It acts on the vector `F` selected by

\[
 H_T\ge0,\qquad F\in\ker H_T,\qquad PAF=\rho_Fb.           \tag{5.1}

Hence it is the only available datum that can restrict the map

\[
 \beta_{\rm phys}:\ker H_T\longrightarrow\mathbb R.        \tag{5.2}

R170_857 shows that minimality fixes the sign of the diagonal block
`Z dot H Z`, while (5.2) is a boundary-augmented connection. The remaining
problem can be stated without PC:

> **Boundary class law.** The linear map (5.2) vanishes on the
> vector or radical subspace selected from the right.

To prove it one must build a relation between the tangent cone of
positive forms in (5.1) and the quotient class (3.2). Any relation
factoring through `D_N` is zero in the quotient and cannot do this.

## 6. Falsifiers

The decomposition (0.2) holds for any coefficient system if one
replaces its corresponding null line. What is specific to `Lambda` is that
the line is `(Lambda,1)` with respect to the fixed target `log`.

For DH/DMV or a finite modification:

* `mathscr D_N(a,1) ne0`, so the normal term `Q D_N` appears;
* its first contact may have a different, nonzero boundary-augmented class;
* there is no reason for the cancellation between the two terms of (0.2)
  to reproduce the law intended for `Lambda`.

A valid proof must use simultaneously that the normal term
vanishes exactly for `Lambda` and that minimality kills the remaining
class. Using only one of these two facts does not pass F1/F3.

## 7. Status

```text
splitting x=sigma(Dx)+c(Lambda,1)                          PROVED
classification ell=Q D+c beta_ell                          PROVED
beta_ell is the intrinsic restriction to the null line     PROVED
quotient Hom/I_D = Hom(H,Y)                                PROVED
physical class beta_phys = g Delta_Tate                    IDENTIFIED
PC/Möbius determine beta_phys                              REFUTED
minimality => beta_phys=0                                  OPEN LAW
VIR--LB / D                                                OPEN
```
