# R170_870 — The boundary-augmented class is odd; minimality is even

## 0. Result

R170_869 reduces the exterior defect to the linear map

\[
 \beta_{\rm phys}:Z_T:=\ker H_T\longrightarrow\mathbb R,
 \qquad
 \beta_{\rm phys}(F)=g_\epsilon\Delta^{\rm Tate}(F).       \tag{0.1}
\]

First-contact minimality controls quadratic forms on
`Z_T`, in particular

\[
 B_T:=Z_T\dot H_TZ_T\preceq0                              \tag{0.2}

under REG/C1. That data is even in `F`; (0.1) is odd:

\[
 \beta_{\rm phys}(-F)=-\beta_{\rm phys}(F).               \tag{0.3}

Hence no consequence that uses only the spectral tangent cone,
eigenvalues, or quadratic diagonals can assign a nontrivial one-sided sign
to `beta_phys`. A bound

\[
 \beta_{\rm phys}(F)\ge0\quad(F\in Z_T)                   \tag{0.4}

already immediately implies `beta_phys=0`, by applying it to `-F`. It is not a
weaker lemma than the exterior law: it is exactly the exterior law.

An abstract independence theorem is also proved: for any first-contact
family and any linear functional `beta in Z_T^*`, one can add a
boundary-augmented port carrying that class without changing the
physical operator, its minimality, or the arithmetic line of R170_866. Hence
the inputs currently proved do not determine (0.1). What is missing is an
odd coupling identity, specific to the arithmetic port.

## 1. Parity under sign change

At a fixed parity, R170_856(8.7) gives

\[
 \beta_{\rm phys}(F)
 =(b,P\dot AF)-(h,P\mathcal C F)-\rho_Fg_\epsilon.         \tag{1.1}

The maps `F mapsto P dot A F`, `F mapsto P C F` and
`F mapsto rho_F` are linear. This proves (0.3).

By contrast, for any self-adjoint form `V`,

\[
 (-F,V(-F))=(F,VF).                                       \tag{1.2}

Membership in the radical, the norm, parity, the eigenvalue equation,
and the property of maximizing the virial are also invariant under
`F mapsto -F`.

## 2. Trivial dual cone lemma

**Lemma 2.1.** Let `Z` be a real vector space and `beta in Z^*`. The
following are equivalent:

1. `beta(F)>=0` for all `F in Z`;
2. `beta(F)<=0` for all `F in Z`;
3. `beta=0`.

**Proof.** If 1 holds, apply it to `-F` to get
`-beta(F)>=0`, hence `beta(F)=0`. The rest is immediate. QED.

Hence the dual cone of the full linear space `Z` is `{0}`. To
obtain a non-tautological one-sided inequality one would need to select
a proper cone `Z_+ subset Z` that does not simultaneously contain `F` and `-F`.

Spectral minimality does not provide such a cone: it selects a line of
eigenvectors, not an orientation of that line.

## 3. A phase normalization is not a law

One might try to fix the sign via

\[
 (u_T,F)>0                                                   \tag{3.1}

for some observer `u_T`. This only works when `(u_T,F) ne0` and
depends on an additional choice. Even then, proving
`beta_phys(F)>=0` for the oriented representative does not by itself imply
an operator identity; it is an inequality on a section of the
double cover of radical lines.

The natural candidates `u_T=b,h,q` are precisely the ports whose
compatibility is open. Using them to orient `F` and then attributing
that orientation to minimality would circularly introduce the
coupling being sought.

If the radical has dimension greater than one, a single normalization
`(u_T,F)>0` selects a hemisphere, but does not control vectors
orthogonal to `u_T`; nor does it produce a linear law vanishing on all of `Z_T`.

## 4. Boundary-augmented independence theorem

Let `H_s` be any `C1` family on a space `mathfrak P` satisfying

\[
 H_0\ge0,\qquad Z=\ker H_0\ne0,\qquad H_s\ge0\ (s<0).       \tag{4.1}

Let also `mathscr D_N` be the arithmetic map of R170_866. Fix an
arbitrary functional

\[
 \beta\in Z^*.                                             \tag{4.2}

Enlarge only the **output record**, not the physical operator, by defining

\[
 \ell_\beta((a,c)\otimes F)
 :=Q\boldsymbol{\mathscr D}_N((a,c)\otimes F)+c\beta(ZF),  \tag{4.3}

with any `Q`. Then:

* `H_s`, its spectrum, radical, and tangent cone do not change;
* the arithmetic line `R(Lambda,1)` does not change;
* every identity factored through `D_N` remains;
* the boundary-augmented class of `ell_beta` on the null line is exactly
  `beta`.

Thus the structures proved up through R170_869 are compatible with
any odd class on the radical. They cannot determine that it is zero.

This theorem does not claim that every `beta` comes from the physical zeta
port. It claims that, to single out that port, an additional identity
is needed linking it to `H_s`; that link is not contained in minimality nor
in the coefficient complex.

## 5. Minimal form of the new law

An admissible law must build a bilinear pairing

\[
 \mathfrak C_T:Z_T\times\mathcal B_T\longrightarrow\mathbb R
                                                                    \tag{5.1}
\]

with a canonical boundary vector `e_T in mathcal B_T` such that

\[
 \beta_{\rm phys}(F)=\mathfrak C_T(F,e_T),                 \tag{5.2}

and an independent reason for

\[
 \mathfrak C_T(F,e_T)=0.                                  \tag{5.3}

There are two possible mechanisms:

1. `e_T` belongs to a second radical of a common positive form, as
   in R170_862;
2. an odd arithmetic symmetry sends `e_T` to `-e_T` while leaving `F` and the
   form invariant, forcing (5.3).

The ordinary reflection `J` only fixes parity and does not change the port
that way; multiplicative phases are pure gauge by R170_501. Hence
the symmetry in item 2, if it exists, must act jointly on integer
factorization and on the exterior port.

## 6. Why antisymmetry alone does not kill the flow

A quantity odd under `L <-> S` is not zero in the physical system, because
the system distinguishes the factors: `L` carries `Lambda` and `S` carries
`mathbf1`. The involution sends the system to its opposite orientation, it does
not leave it pointwise fixed.

To force vanishing one would need an additional identification between the
two orientations in the boundary-augmented port. Full commutativity gives that
identification after forgetting the intermediate point, but the cut
turns it exactly into (3.5), not into `Phi_ext=0`.

Likewise, (3.5) holds for many general weights and does not by itself use
`a=Lambda`. The specificity enters by requiring that both orientations
share the same Chebyshev column `log` at every cut.

## 7. Remaining minimal bilateral law

Define the full PC flow `Phi_PC` by adding to (4.4) the reflected, polar, and
Tate terms of the R170_856 ledger. The sought law can now be
formulated as

\[
 \boxed{
 \operatorname{Res}_{(\Lambda,1)}\Phi_{PC}(F)=0
 \quad(F\in\ker H_T),}                                    \tag{7.1}

where `Res_(Lambda,1)` is the quotient class of R170_869.

Equation (7.1) is exactly `beta_phys(F)=0`, but it adds structure:
its principal representative is the odd flow of the factor-swap
cycle. A new proof must show that the interior identification
(3.5), together with minimality, extends the involution to the Tate port.

No such extension is claimed here.

## 8. Status

```text
beta_phys is linear/odd in F                               PROVED
minimality and the virial are quadratic/even                PROVED
one-sided sign of beta on all of Z is equivalent to beta=0  PROVED
phase normalization from the port                           CIRCULAR / PARTIAL
abstract independence of the boundary-augmented class        PROVED
minimality + coefficient algebra => beta=0                   REFUTED
odd coupling or common second radical                        NECESSARY / OPEN
VIR--LB / D                                                  OPEN
```
