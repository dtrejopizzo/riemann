# P124.012 -- causal storage reduces the seam gate to one scalar surplus

## Status

`PROVED REDUCTION / NO SIGN.`  The phase-120 causal storage identity gives
an exact scalar equality at first contact.  It does not prove seam
vanishing, but it identifies the minimal scalar condition which would force
it.

## 1. Storage notation

Let `F=L_0G` be a compact primitive source in the window `I_T`.  Use the
phase-120 universal half-line field

\[
        \mathfrak h_F(t,\ell)=e^{-\ell/2}F(t-\ell),\qquad \ell\ge0,
\]

and the prime-cell output

\[
 E_{p,T}\mathfrak h
 =\left(
  \sqrt{1-p^{-1}}\mathbf1_{[-T,T-\log p]}B_p\mathfrak h,\,
  \mathbf1_{[T-\log p,T]}B_p\mathfrak h
  \right).
\]

Put

\[
        a_p=\log p,\qquad
        \theta_T=\sum_{p\in S_T}a_p,\qquad
        w_p^2={a_p\over\theta_T},
\]

and

\[
        \overline E_T=\sum_{p\in S_T}w_p^2E_{p,T},\qquad
        \mathcal K_T^{\rm seam}\mathfrak h
        =\bigl(w_p(E_{p,T}-\overline E_T)\mathfrak h\bigr)_p .
\]

The exact ANOVA identity is

\[
 \sum_{p\in S_T}a_p\|E_{p,T}\mathfrak h\|^2
 =\theta_T\|\overline E_T\mathfrak h\|^2
  +\theta_T\|\mathcal K_T^{\rm seam}\mathfrak h\|^2.       \tag{1.1}
\]

## 2. The scalar surplus

Define the coherent storage surplus

\[
\boxed{
\begin{aligned}
 \mathcal C_T(F)
 :={}&\mathcal D_\Gamma(F)+(\theta_T-m_0)\|F\|^2
      +\mathcal S_{\Gamma,\rm prim}^+(G)\\
 &-\theta_T\|\overline E_T\mathfrak h_F\|^2 .
\end{aligned}}                                             \tag{2.1}
\]

Here `D_Gamma` and `S_Gamma,prim^+` are the causal Gamma bulk and primitive
terminal storage of P3_CAUSAL_PRIMITIVE_STORAGE_IDENTITY.

The phase-120 global storage balance and (1.1) give the exact identity

\[
\boxed{
 \mathfrak q_T(F)
 =\mathcal C_T(F)
  -\theta_T\|\mathcal K_T^{\rm seam}\mathfrak h_F\|^2,
}                                                          \tag{2.2}
\]

where

\[
        \mathfrak q_T(F)=\operatorname{Re}\langle F,Z_T(D)F\rangle
\]

is the same finite-window scalar form represented by the signed causal
impedance.

Indeed, P3_CAUSAL (3.1) gives

\[
\mathfrak q_T(F)
=\mathcal D_\Gamma(F)+(\theta_T-m_0)\|F\|^2
 +\mathcal S_{\Gamma,\rm prim}^+(G)
 -\sum_{p\in S_T}a_p\|E_{p,T}\mathfrak h_F\|^2,
\]

and substituting (1.1) is exactly (2.2).

## 3. First-contact scalar gate

At first contact,

\[
        F\in\mathcal P_T,\qquad L_TF=0,\qquad \mathfrak q_T(F)=0.
\]

Therefore (2.2) becomes

\[
\boxed{
 \mathcal C_T(F)
 =\theta_T\|\mathcal K_T^{\rm seam}\mathfrak h_F\|^2\ge0.
}                                                          \tag{3.1}
\]

Consequently the following conditions are equivalent on the first-contact
kernel:

\[
\boxed{
 \mathcal K_T^{\rm seam}\mathfrak h_F=0
 \quad\Longleftrightarrow\quad
 \mathcal C_T(F)=0
 \quad\Longleftrightarrow\quad
 \mathcal C_T(F)\le0 .
}                                                          \tag{3.2}
\]

This is the minimal scalar condition supplied by the causal storage
identity.  Any proof of the one-sided estimate

\[
        \mathcal C_T(F)\le0                              \tag{3.3}
\]

on first-contact states would force seam zero.  Then
P121_TRANSVERSE_SEAM_FIRST_CELL_RIGIDITY gives `F=0`, and every scalar
collar functional such as `J_+(F)` vanishes.

## 4. What the identity does not prove

The storage calculation alone proves (3.1), not (3.3).  It rewrites the
transverse seam norm as the coherent surplus, but supplies no upper sign for
that surplus.

This is distinct from the phase-120 oriented completion target

\[
 \mathcal C_T(F)
 =\theta_T\|\mathcal K_T^{\rm seam}\mathfrak h_F\|^2
  +\|\mathcal Q_TG\|^2,
\]

which would prove a global square but would not itself imply seam vanishing
at equality.  The equality-state seam route needs the sharper scalar
estimate (3.3), derived from the unsupertraced Euler source rather than from
the completed square.

Thus the new target isolated by causal storage is exactly:

\[
\boxed{
 L_TF=0,\ F\in\mathcal P_T
 \quad\Longrightarrow\quad
 \mathcal C_T(F)\le0.
}
\]

No such sign is proved here.
