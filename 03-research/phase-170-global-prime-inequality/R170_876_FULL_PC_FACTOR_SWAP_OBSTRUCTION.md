# R170_876 — Obstruction to the factor swap of the full PC port

> **Audit R170_877.** The physical defect (2.2) and its jet (4.2) are
> correct. The derivation defect `Omega_N` of §3 exists when comparing
> the branches, but does not survive PC: it cancels exactly against the
> difference of the two hyperbolas `H`. Hence `Omega_N` must not be
> incorporated as a new boundary residue. The effective obstruction is
> the swap-even jet of (4.2), plus the fact that the swapped causal
> extraction does not exist because `PL_N^*P` is not invertible.

## 0. Result

The factor swap of R170_871 is an exact symmetry of the
causal hyperbola, but not of the physical first-contact operator. With

\[
 S=S_N,\qquad L=L_M,\qquad
 A_L=\mathcal M-(L+L^*),\qquad K=K_N,\qquad H_L=LS-K,
                                                               \tag{0.1}
\]

the swap \(\sigma(L,S)=(S,L)\) satisfies

\[
 \sigma(H_L)=SL-K=LS-K=H_L,                               \tag{0.2}
\]

but

\[
 \sigma(A_L)=A_S:=\mathcal M-(S+S^*)\ne A_L.             \tag{0.3}
\]

Hence the extension proposed in R170_874(3.1)--(3.2) cannot be
a pure involution that simultaneously swaps the factors and fixes
the physical datum. It needs a connection term compensating

\[
 \boxed{A_S-A_L=(L+L^*)-(S+S^*).}                         \tag{0.4}
\]

This is a strict reduction: the sought law must be a **covariant/affine**
naturality, not a linear equivariance of the swap.

## 1. The hyperbola and the Chebyshev column are invariant

On the full space, the causal sums commute:

\[
 LS=SL.                                                    \tag{1.1}
\]

Moreover the Chebyshev column is common to both orientations because

\[
 \sum_{dm=k}\Lambda(d)=\sum_{dm=k}\Lambda(m)=\log k.      \tag{1.2}
\]

Thus \(K\) stays fixed and (0.2) is exact. This explains why the route
cycle of R170_871 exists and why its full observation vanishes.

The conclusion stops there: PC does not depend only on \(H_L\). Its
physical side is

\[
 S A_L\mathscr F.                                         \tag{1.3}
\]

After the swap one obtains

\[
 L A_S\mathscr F,                                         \tag{1.4}
\]

which is not (1.3).

## 2. Exact defect of the physical side

Before applying Fourier, subtract the two oriented sides:

\[
\begin{aligned}
 \mathfrak O_{L,S}
 &:=SA_L-LA_S\\
 &=S\mathcal M-L\mathcal M
   -SL-SL^*+LS+LS^*.
                                                               \tag{2.1}
\end{aligned}
\]

Since \(SL=LS\), the direct causal products cancel and one is left with

\[
 \boxed{
 \mathfrak O_{L,S}
 =(S-L)\mathcal M+LS^*-SL^*.}                              \tag{2.2}
\]

The first term is archimedean--Euler; the second is the defect of
the reflected orientation. Neither belongs to the symmetric hyperbola
\(LS-K\). After compression, (2.2) further generates its support, Tate, and
exterior concomitants.

Identity (2.2) shows exactly why the antisymmetry of the raw flow
cannot be extended by `-1` over the boundary without correction: the
operator whose radical equation selects `F` also changes.

## 3. The swap does not preserve the PC derivation

The PC identity distinguishes the integer leg via its commutator with
`X`:

\[
 -[X,S_N]=K_N^{(1)}
 :=\sum_{n\le N}{\log n\over\sqrt n}\tau_{\log n}.          \tag{3.1}
\]

The factor swap sends it to

\[
 -[X,L_N]=K_N^{(\Lambda,1)}
 :=\sum_{n\le N}{\Lambda(n)\log n\over\sqrt n}
                   \tau_{\log n},                          \tag{3.2}
\]

which is not `K_N^(1)`: it is the prime virial force. Although `LS` is
invariant and its full coefficient uses `Lambda*1=log`, the pair
`(product,derivation)` is not. The swap is not an automorphism of PC
with `X` fixed.

The derivation defect

\[
 \boxed{\Omega_N:=K_N^{(\Lambda,1)}-K_N^{(1)}}             \tag{3.3}
\]

appears before summing all PC terms. However R170_877 proves that it
cancels exactly against the difference of the two hyperbolas. It helps
explain why the second jet of R170_856 must be kept, but it does not
constitute an additional boundary class.

## 4. Antidiagonal jet

To compare both orientations use

\[
 \mathfrak O(r,q)=S(q)A_L(r)-L(r)A_S(q),
 \qquad \partial_-\mathfrak O|_{1,1}.                     \tag{4.1}
\]

The product rule gives exactly

\[
\begin{aligned}
 \partial_-\mathfrak O|_{1,1}
 ={}&(S+L)\dot{\mathcal M}-(\dot L+\dot S)\mathcal M\\
 &+\dot L S^*-S\dot L^*-L\dot S^*+\dot S L^*.
                                                               \tag{4.2}
\end{aligned}
\]

Here the Gamma leg uses the scale of the corresponding orientation; that is
why the two terms with \(\dot{\mathcal M}\) add up. After using the
Tate--Beckner relation, these are the families of terms R170_848 and
R170_856 record as archimedean, adjoint orientation, polar, and
moving connection. The result is the connection cocycle required to
compare the two orientations; `Omega_N` has already cancelled on the full
Poisson side.

## 5. Minimal covariant law

Let \(\Phi_{\rm ext}(L,S)\) be the odd flow of R170_871 and let
\(\Gamma_{L,S}\) be the full port induced by (2.2), including the
polar term and the Tate connection in the order of R170_856. The admissible
form of the law is no longer \(\widehat J\Phi=-\Phi\) outright, but

\[
 \boxed{
 \widehat J\,\mathcal E_L(F)
 -\mathcal E_S(\widehat JF)
 =\Gamma_{L,S}(F).}                                       \tag{5.1}
\]

The necessary sign equality would then be a statement about the
boundary-augmented class of

\[
 \Phi_{\rm ext}(L,S)+\Gamma_{L,S},                         \tag{5.2}
\]

not about \(\Phi_{\rm ext}\) alone. R170_856 already contains a ledger of the
terms of \(\Gamma\); what remains is to prove that its physical class is exactly
\(-\beta_{\rm phys}\), or that (5.2) vanishes by minimality.

Postulating (5.1) by defining \(\Gamma\) as the difference would be circular.
The acceptance criterion is to obtain it term by term from two-scale PC,
with (2.2) as the physical side and the terms
`H_M,N`, `K_N`, `C_N` as the Poisson side.

## 6. Consequence for R170_874

The criterion R170_874(3.1)--(3.2) was sufficient, but too strong:
a pure involution that fixes the physical datum is incompatible with (0.3).
Its independence conclusion remains valid. The constructive target is replaced
by the covariant law (5.1), whose cocycle cannot be eliminated.

## 7. Status

```text
swap fixes LS, K and H=LS-K                               PROVED
swap fixes A_L and the physical datum                     REFUTED
swap preserves the PC derivation X                        REFUTED
derivation defect Omega_N                                 COMPUTED / CANCELS IN PC
exact physical defect SA_L-LA_S, equation (2.2)           PROVED
archimedean/reflected nature of the defect                LOCATED
pure equivariance proposed in R170_874                    DISCARDED
covariant law with cocycle Gamma_L,S                      FORMULATED
literal derivation of its boundary class from PC-ren       OPEN
VIR--LB / D                                               OPEN
```
