# P121 -- exact Tate-collar localization of first contact

## Status

This note proves an elementary exact identity for the two scalar Tate
components of a hypothetical first-contact equation.  After pairing with
the two Tate characters, every translated interior term disappears and only
the left and right boundary collars remain.  At a prime power `n=p^k`, the
balanced coefficient `Lambda(n)/sqrt(n)` becomes exactly `Lambda(n)` at one
edge and `Lambda(n)/n` at the other.

Thus the two Lagrange multipliers at first contact are determined entirely
by two explicit scalar boundary currents through an invertible **crossed
Tate pairing matrix**.  This matrix must not be confused with the positive
Gram matrix of the two Tate characters.  This is a localization theorem,
not yet a proof that those currents vanish; the global square remains open.

## 1. Operators and the three distinct meanings of boundary

Put `I_T=(-T,T)` and extend every `F in L^2(I_T)` by zero to the real line.
For `a>0` define

\[
 (S_aF)(t)=F(t-a),\qquad (S_{-a}F)(t)=F(t+a),
 \qquad t\in I_T.                                  \tag{1.1}
\]

The complete localized Weil operator is

\[
 \mathscr A_T=G_{\Gamma,T}-m_0I-B_{T,+}-B_{T,-},   \tag{1.2}
\]

where

\[
 \begin{aligned}
 B_{T,+}F&=\sum_{2\le n<e^{2T}}
       {\Lambda(n)\over\sqrt n}\,S_{\log n}F,\\
 B_{T,-}F&=\sum_{2\le n<e^{2T}}
       {\Lambda(n)\over\sqrt n}\,S_{-\log n}F.
 \end{aligned}                                     \tag{1.3}
\]

These are the two oriented prime translations.  They must not be confused
with the two Tate characters

\[
 \phi_+(t)=e^{t/2},\qquad \phi_-(t)=e^{-t/2},       \tag{1.4}
\]

nor with the prime-cylinder seam traces of phase 120.  In the first-contact
equation the two scalar boundary terms are precisely

\[
 \mathscr A_TF=\alpha\phi_-+\beta\phi_+ .           \tag{1.5}
\]

They occur because the primitive compression kills the span of
`phi_+,phi_-`.

## 2. Exact collar identity for one translation

For `sigma in {+1,-1}` put

\[
 M_\sigma(F)=\int_{-T}^T e^{\sigma t/2}F(t)\,dt.    \tag{2.1}
\]

For `0<a<2T` define the right and left collar moments

\[
 \begin{aligned}
 R_{\sigma,a}(F)&=\int_{T-a}^{T}e^{\sigma t/2}F(t)\,dt,\\
 L_{\sigma,a}(F)&=\int_{-T}^{-T+a}e^{\sigma t/2}F(t)\,dt.
 \end{aligned}                                     \tag{2.2}
\]

### Lemma 2.1 -- translation becomes boundary

If `M_sigma(F)=0`, then

\[
 \boxed{
 \begin{aligned}
 M_\sigma(S_aF)&=-e^{\sigma a/2}R_{\sigma,a}(F),\\
 M_\sigma(S_{-a}F)&=-e^{-\sigma a/2}L_{\sigma,a}(F).
 \end{aligned}}                                    \tag{2.3}
\]

#### Proof

Changing variables `u=t-a` and using the zero extension gives

\[
 M_\sigma(S_aF)
 =e^{\sigma a/2}\int_{-T}^{T-a}e^{\sigma u/2}F(u)\,du.
\]

The full integral on `(-T,T)` is zero, so the last integral is minus its
right collar.  The second identity follows in the same way after the change
`u=t+a`.  No estimate is used.

## 3. The arithmetic simplification

Let `a_n=log n` and `w_n=Lambda(n)/sqrt(n)`.  Applying (2.3) termwise gives

\[
 \boxed{
 \begin{aligned}
 M_+(B_{T,+}F+B_{T,-}F)
 &=-\sum_{2\le n<e^{2T}}
   \left[\Lambda(n)R_{+,a_n}(F)
        +{\Lambda(n)\over n}L_{+,a_n}(F)\right],\\
 M_-(B_{T,+}F+B_{T,-}F)
 &=-\sum_{2\le n<e^{2T}}
   \left[{\Lambda(n)\over n}R_{-,a_n}(F)
        +\Lambda(n)L_{-,a_n}(F)\right].
 \end{aligned}}                                    \tag{3.1}
\]

The square-root normalization has disappeared:

\[
 w_ne^{a_n/2}=\Lambda(n),\qquad
 w_ne^{-a_n/2}={\Lambda(n)\over n}.                 \tag{3.2}
\]

For `n=p^k`, this reads `Lambda(n)=log p`; the coefficient is independent
of `k` at the near edge and is `(log p)p^{-k}` at the opposite edge.

## 4. Gamma is the continuous version of the same collar current

The positive Gamma multiplier has the exact Levy representation

\[
 g_\Gamma(\tau)
 =\int_0^\infty c_\Gamma(u)|1-e^{-i\tau u}|^2\,du,
 \qquad
 c_\Gamma(u)={e^{-u/2}\over1-e^{-2u}}.              \tag{4.1}
\]

Consequently, on the zero-extended window,

\[
 G_{\Gamma,T}
 =\int_0^\infty c_\Gamma(u)(2I-S_u-S_{-u})\,du     \tag{4.2}
\]

in quadratic-form sense.  If both Tate moments of `F` vanish, (2.3) yields

\[
 \boxed{
 M_\sigma(G_{\Gamma,T}F)
 =\int_0^{2T}c_\Gamma(u)
   \left[e^{\sigma u/2}R_{\sigma,u}(F)
        +e^{-\sigma u/2}L_{\sigma,u}(F)\right]du.} \tag{4.3}
\]

The upper limit may be written `2T`, because both translations vanish for
`u>=2T` and the primitive `2I` term has zero Tate moment.

Thus Gamma and the prime powers produce one and the same type of object:
a continuous collar current plus a discrete collar current.

## 5. Exact two-by-two boundary system at first contact

Define

\[
 \begin{aligned}
 J_\sigma(F):={}&
 \int_0^{2T}c_\Gamma(u)
   \left[e^{\sigma u/2}R_{\sigma,u}(F)
        +e^{-\sigma u/2}L_{\sigma,u}(F)\right]du\\
 &+\sum_{2\le n<e^{2T}}w_n
   \left[e^{\sigma a_n/2}R_{\sigma,a_n}(F)
        +e^{-\sigma a_n/2}L_{\sigma,a_n}(F)\right].
                                                               \tag{5.1}
 \end{aligned}
\]

The `-m_0I` term has zero Tate moment on a primitive vector.  Therefore
(3.1)--(4.3) prove

\[
 M_\sigma(\mathscr A_TF)=J_\sigma(F).              \tag{5.2}
\]

If `F` is a first-contact vector and (1.5) holds, then

\[
 \boxed{
 \begin{pmatrix}
  2T&2\sinh T\\
  2\sinh T&2T
 \end{pmatrix}
 \binom{\alpha}{\beta}
 =
 \binom{J_+(F)}{J_-(F)}.}                           \tag{5.3}
\]

Here the ordering follows from
`M_+(alpha phi_-+beta phi_+)=2T alpha+2sinh(T) beta`.
The determinant is `4(T^2-sinh^2 T)`, nonzero for `T>0`, so `alpha,beta`
are uniquely and explicitly determined by the collar current.

The matrix in (5.3) is indefinite: its parity eigenvalues are

\[
 2(T+\sinh T)>0,\qquad 2(T-\sinh T)<0.              \tag{5.3a}
\]

It is not the Tate Gram.  In the ordered basis `(phi_-,phi_+)`, the genuine
positive Gram matrix is

\[
 G_T=2\begin{pmatrix}\sinh T&T\\T&\sinh T\end{pmatrix}>0. \tag{5.3b}
\]

The matrix in (5.3) is `G_TC`, where
`C=((0,1),(1,0))` exchanges the two orientations; its invertibility, not
positivity, is what determines the multipliers.

If `F(-t)=epsilon F(t)`, then

\[
 L_{\sigma,u}(F)=\varepsilon R_{-\sigma,u}(F),
 \qquad J_-(F)=\varepsilon J_+(F),                 \tag{5.4}
\]

and (5.3) reduces to one scalar equation.  Equivalently,

\[
 \varepsilon=+1:\ \alpha=\beta,
 \qquad
 \varepsilon=-1:\ \alpha=-\beta.                 \tag{5.5}
\]

## 6. Consequence and exact remaining task

The first-contact forcing is not an independent bulk defect.  It is the
image, under the invertible crossed Tate pairing matrix, of the single
parity-reduced collar current (5.1).  Therefore the multiplier vanishes
exactly when

\[
 J_\varepsilon(F)=0.                                \tag{6.1}
\]

This gives a narrower elementary target than an operator factorization:
derive cancellation of the continuous Gamma collar current against the
discrete `Lambda`/`Lambda/n` collar current from the uncompressed equality
law.  Equation (6.1) is not asserted here.  Assuming it would merely rename
the missing sign; proving it from a source identity independent of
`mathscr A_T>=0` would remove the complete two-Tate forcing and leave the
homogeneous first-contact equation.
