# D.79 supplement — finite low-block capacity and directed Schur reduction

## Lemma

Let `H=L direct-sum K`, with `dim L=r<infinity`, and write

\[
 A_0=\begin{pmatrix}A&B^*\\B&D\end{pmatrix},
 \qquad D\ge gI_K,                                      \tag{1}
\]

where `A=A^*` and `g>0`.  Let `R>=0`.  For `0<eta<g` put

\[
 h=g-\eta,
 \qquad A_{\rm eff}=A-\eta^{-1}B^*B.                  \tag{2}
\]

Define the shorted capacity of `R+hQ_L` onto `L` by

\[
 C_h(L;R)
 =\left[P_L(R+hI)^{-1}P_L\big|_L\right]^{-1}-hI_L.     \tag{3}
\]

If

\[
 \boxed{A_{\rm eff}+C_h(L;R)>0,}                       \tag{4}
\]

then `A_0+R>0`.

### Proof

For `x in L`, `y in K`, Young's inequality gives

\[
 2\mathrm{Re}\,\langle Bx,y\rangle
 \ge-\eta^{-1}\|Bx\|^2-\eta\|y\|^2.                 \tag{5}
\]

Thus

\[
 A_0\ge A_{\rm eff}\oplus hI_K.                       \tag{6}
\]

The shorted operator of `R+hQ_L` to `L` is (3), by the
finite-dimensional Schur-complement/resolvent formula.  Shorting the
right hand side of

\[
 A_0+R\ge A_{\rm eff}\oplus0+(R+hQ_L)                  \tag{7}
\]

therefore gives (4).  Positivity of the shorted operator and positivity
on the complementary block prove strict positivity of (7), hence of
`A_0+R`.

## Positive-deficit matrix form

Set

\[
 \Delta_h={1\over h}I_L-
 P_L(R+hI)^{-1}P_L\big|_L.                              \tag{8}
\]

Then `0<=h Delta_h<I` and

\[
 \boxed{C_h=h^2\Delta_h(I-h\Delta_h)^{-1}.}            \tag{9}
\]

For a nonnegative translation-invariant multiplier `r_R(tau)` and an
orthonormal basis `v_1,...,v_r` of `L`,

\[
 (\Delta_h)_{ij}={1\over2\pi}\int_{\mathbb R}
 \overline{\widehat v_i(\tau)}\widehat v_j(\tau)
 {r_R(\tau)\over h(h+r_R(\tau))}\,d\tau.              \tag{10}
\]

Unlike the scalar case, one may not simply discard the frequency tail
entrywise.  A directed finite-interval matrix lower bound is obtained by
forming its positive Gram integral and proving a Loewner lower bound by
interval `LDL^*`.  Formula (9) is operator monotone on
`0<=h Delta<I`, so such a lower bound propagates to the capacity.

For `r=1`, (3), (8), and (9) reduce exactly to the preceding directed
capacity--Feshbach lemma.

