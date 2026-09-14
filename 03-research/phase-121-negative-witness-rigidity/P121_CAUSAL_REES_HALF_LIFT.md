# P121 -- the causal half-lift of the first-contact equation

## Status

This note constructs, before scalar supertrace, a canonical oriented Rees
deformation of the localized prime--Gamma operator.  Its two coefficients
are the causal and anticausal halves of the same source operator; no square
root, inverse of the primitive compression, or assumed sign is used.  This
is a Rees lift of the **localized operator**.  It must not be identified
with the global Poisson/Rees normal whose inactive-prime tame coordinates
define `c^(1)`; Section 5 proves the distinction.

The collar integral evaluated in
`P121_RESOLVED_TATE_COLLAR_INTEGRAL.md` splits accordingly into two closed
potentials.  At a parity first-contact state the scalar equation annihilates
the same-parity primitive component of the causal output.  The logarithmic
Rees derivative is exactly the remaining opposite-parity primitive
component.  Thus the local lift exists canonically, but first contact by
itself neither makes its local normal zero nor supplies the global `K_2`
normal.

## 1. The causal half

Work first on the compact smooth core, with zero extension outside
`I_T=(-T,T)`.  Put

\[
 c_\Gamma(u)={e^{-u/2}\over1-e^{-2u}},\qquad
 B_{T,+}=\sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}S_{\log n}.
                                                               \tag{1.1}
\]

Define the oriented causal form operator

\[
 \boxed{
 \mathscr C_T
 =2\int_0^\infty c_\Gamma(u)(I-S_u)\,du
   -m_0I-2B_{T,+}.}                                      \tag{1.2}
\]

The integral is understood as the standard closed one-sided Levy form; on
the compact smooth core it is literal.  Let `R` denote reflection,
`(RF)(t)=F(-t)`.  Since

\[
 RS_uR=S_{-u},\qquad RB_{T,+}R=B_{T,-},                    \tag{1.3}
\]

one has

\[
 \mathscr C_T^*=R\mathscr C_TR.                            \tag{1.4}
\]

### Theorem 1.1 -- exact causal splitting

The complete localized operator is the real part of its causal half:

\[
 \boxed{
 \mathscr A_T={\mathscr C_T+\mathscr C_T^*\over2}.}        \tag{1.5}
\]

#### Proof

The average of the two Gamma halves is

\[
 \int_0^\infty c_\Gamma(u)(2I-S_u-S_{-u})du=G_{\Gamma,T}.
\]

The average of `-2B_(T,+)` and its adjoint is
`-B_(T,+)-B_(T,-)`, and the scalar term remains `-m_0I`.
These are exactly the three terms defining `mathscr A_T`.  QED.

## 2. The canonical Rees deformation

For `z in C^x` define

\[
 \boxed{
 \mathscr A_T(z)
 ={1\over2}\left(z\mathscr C_T+z^{-1}\mathscr C_T^*\right).} \tag{2.1}
\]

Then

\[
 \mathscr A_T(1)=\mathscr A_T,\qquad
 \left.z{d\over dz}\mathscr A_T(z)\right|_{z=1}
 ={\mathscr C_T-\mathscr C_T^*\over2}.                    \tag{2.2}
\]

Thus evaluation at `z=1` is the scalar augmentation and its logarithmic
normal is the oriented difference.  The construction is made directly
from the source translations and the one-sided Gamma Levy operator; it is
not chosen to fit a first-contact vector.

Reflection acts on the formal family by

\[
 R\mathscr A_T(z)R=\mathscr A_T(z^{-1}).                   \tag{2.3}
\]

For `|z|=1`, `mathscr A_T(z)` is self-adjoint.  This is the
operator-level version of the universal character
`z^(-1)r_+ + z r_-` in
`P121_CENTRAL_JET_ORIENTATION_BRIDGE.md`.

## 3. The evaluated collar splits into its orientations

Assume that `F` is Tate primitive.  Define

\[
\begin{aligned}
 J_{\sigma}^{\to}(F)
 :={}&\int_0^{2T}c_\Gamma(u)e^{\sigma u/2}
             R_{\sigma,u}(F)du\\
 &+\sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
       e^{\sigma\log(n)/2}R_{\sigma,\log n}(F),\\
 J_{\sigma}^{\leftarrow}(F)
 :={}&\int_0^{2T}c_\Gamma(u)e^{-\sigma u/2}
             L_{\sigma,u}(F)du\\
 &+\sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
       e^{-\sigma\log(n)/2}L_{\sigma,\log n}(F).
                                                               \tag{3.1}
\end{aligned}
\]

The one-translation collar identity gives

\[
 \boxed{
 M_\sigma(\mathscr C_TF)=2J_\sigma^{\to}(F),\qquad
 M_\sigma(\mathscr C_T^*F)=2J_\sigma^{\leftarrow}(F).}    \tag{3.2}
\]

Consequently

\[
 J_\sigma(F)=J_\sigma^{\to}(F)+J_\sigma^{\leftarrow}(F), \tag{3.3}
\]

which recovers the scalar current of the exact collar localization.

For `sigma=+1`, Fubini evaluates the two halves separately:

\[
\begin{aligned}
 J_+^{\to}(F)
 &=\int_{-T}^{T}e^{t/2}F(t)
   [A_T(T-t)+\Theta_T(T-t)]dt,\\
 J_+^{\leftarrow}(F)
 &=\int_{-T}^{T}e^{t/2}F(t)
   [B_T(T+t)+H_T(T+t)]dt.                         \tag{3.4}
\end{aligned}
\]

Here `A_T,B_T,Theta_T,H_T` are the explicit logarithmic and Chebyshev
tails in `P121_RESOLVED_TATE_COLLAR_INTEGRAL.md`.  Hence the resolved
potential has the canonical orientation split

\[
 \Phi_{+,T}=\Phi_{+,T}^{\to}+\Phi_{+,T}^{\leftarrow}.       \tag{3.5}
\]

The corresponding `sigma=-1` formulas follow by reflection.  In
particular, the Rees normal is the **difference** of two already evaluated
potentials; scalar augmentation is their sum.

## 4. What first contact kills automatically

Let `Q_T` be the projection onto the two Tate modes and put `P_T=I-Q_T`.
Both projections commute with reflection.  For a parity sign `epsilon`
write

\[
 E_\epsilon={1\over2}(I+\epsilon R).                       \tag{4.1}
\]

### Theorem 4.1 -- parity transversality of the Rees normal

Suppose

\[
 F=P_TF,\qquad RF=\epsilon F,\qquad
 P_T\mathscr A_TF=0.                                      \tag{4.2}
\]

Then

\[
 \boxed{P_TE_\epsilon\mathscr C_TF=0}                     \tag{4.3}
\]

and

\[
 \boxed{
 P_T\left.z{d\over dz}\mathscr A_T(z)F\right|_{z=1}
 =P_TE_{-\epsilon}\mathscr C_TF.}                         \tag{4.4}
\]

Thus the oriented normal of a first-contact state is purely primitive of
parity opposite to the source.

#### Proof

By (1.4) and parity,

\[
 \mathscr C_T^*F=R\mathscr C_TRF
 =\epsilon R\mathscr C_TF.                                \tag{4.5}
\]

Equations (1.5) and (4.2) give

\[
 0=P_T\mathscr A_TF
  ={1\over2}P_T(I+\epsilon R)\mathscr C_TF
  =P_TE_\epsilon\mathscr C_TF,                            \tag{4.6}
\]

which is (4.3).  Similarly, (2.2) and (4.5) give

\[
 P_T{\mathscr C_T-\mathscr C_T^*\over2}F
 ={1\over2}P_T(I-\epsilon R)\mathscr C_TF
 =P_TE_{-\epsilon}\mathscr C_TF.                          \tag{4.7}
\]

QED.

### Corollary 4.2 -- exact form of the missing lift

On the first-contact branch, the following are equivalent:

\[
\begin{aligned}
 &P_T\left.z{d\over dz}\mathscr A_T(z)F\right|_{z=1}=0,\\
 &P_T\mathscr C_TF=0,\\
 &\mathscr C_TF\text{ belongs to the two-dimensional Tate space}.
                                                               \tag{4.8}
\end{aligned}
\]

The implication from the first line to the second uses (4.3), which has
already killed the complementary parity component.  Therefore the desired
oriented lift is no longer an unspecified equality of two copies: it is
exactly the vanishing of the explicit opposite-parity causal output in
(4.4).

## 5. Local Rees is not the global `K_2` normal

The source-defined Poisson/Rees normal constructed in
`P121_REES_POISSON_NORMAL_COMPLEX.md` is evaluated by the local logarithmic
connection before augmentation.  Under the already proved relative `K_2`
comparison, its tame component at `(p,k)` is

\[
 c^{(1)}_{p,k}(F)
 =K_F\left(-{1\over2}+{2\pi i k\over\log p}\right).        \tag{5.1}
\]

The local family (2.1) and the global Poisson/Rees normal agree on their
active scalar augmentation, but they are not the same normal object.  The
reason is exact.  If

\[
 p>e^{2T},                                                   \tag{5.2}
\]

then every translation `S_(j log p)` and its adjoint vanish after
compression to `I_T`.  Hence neither `C_T`, `C_T^*` nor any coefficient of
`A_T(z)` contains the place `p`.  Nevertheless the global tame coordinate
is (5.1), and it need not vanish.

### Proposition 5.1 -- inactive-prime separation

For every `T>0`, every inactive prime `p>e^(2T)` and every `k!=0`, there is
a Tate-primitive source `F in C_c^infty(I_T)` such that the localized
`p`-channel is zero while

\[
 c^{(1)}_{p,k}(F)\ne0.                                     \tag{5.3}
\]

#### Proof

The localized `p`-channel is zero for every source by (5.2).  Evaluation at
`lambda_(p,k)` is the nonzero continuous functional

\[
 F\longmapsto\int_{-T}^{T}
 e^{(1/2-2\pi i k/\log p)t}F(t)dt.                          \tag{5.4}
\]

Its representing exponential is not in the span of the two Tate
exponentials because `k!=0`.  Therefore its restriction to the common
kernel of the two Tate moments is nonzero.  Density of
`C_c^infty(I_T)` in that codimension-two kernel gives a smooth primitive
`F` on which (5.4) is nonzero.  QED.

Consequently there is no map from the localized causal Rees normal in
(4.4), using only its place-labelled localized coefficients, to the
cofinal family (5.1).  In particular, the implication

\[
 P_TE_{-\epsilon}\mathscr C_TF=0
 \quad\Longrightarrow\quad c^{(1)}(F)=0                    \tag{5.5}
\]

is not established and is false as an object-level consequence of local
compression.  The missing theorem remains the global statement

\[
 \boxed{
 F\text{ satisfies first contact}
 \Longrightarrow
 \nabla_pZ^{-1}\nu_{\rm Pois}(F)
 \text{ is unramified for cofinally many inactive }p.}     \tag{5.6}
\]

This is precisely the global pre-supertrace lift already isolated in
`P121_REES_POISSON_NORMAL_COMPLEX.md`; the evaluated finite collar and the
localized causal normal do not imply it.

## 6. Causality and reflection do not kill the local normal

There is a two-cell countermodel to any attempt to deduce (5.2) only from
triangular causality, reflection and positivity of the scalar real part.
Let

\[
 R=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 C=a\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad a>0.       \tag{6.1}
\]

Then `C` is lower triangular with real diagonal and

\[
 RCR=C^*,\qquad
 A={C+C^*\over2}
  =a\begin{pmatrix}1&1\\1&1\end{pmatrix}\ge0.             \tag{6.2}
\]

For the odd vector `f=(1,-1)^t`,

\[
 Af=0,\qquad Cf=a(1,1)^t\ne0.                              \tag{6.3}
\]

Thus the scalar first-contact kernel is odd while its causal output is a
nonzero even vector, exactly the parity-transverse configuration of
Theorem 4.1.  The example obeys the causal/Real identities but has no Euler
divisor or relative `K_2` localization.  Consequently vanishing of the
opposite-parity local output, if true for the physical source, cannot be a
formal theorem about causal reflected operators.  Even such vanishing
would still need the separate global lift (5.6) before it could imply
`c^(1)=0`.

## 7. Ledger

```text
canonical causal half C_T                            CONSTRUCTED
A_T=(C_T+C_T*)/2                                    PROVED
source-defined Rees deformation A_T(z)              CONSTRUCTED
two oriented collar halves                          EVALUATED EXACTLY
same-parity primitive causal output at first contact ZERO, PROVED
Rees normal = opposite-parity primitive output      PROVED
opposite-parity local output vanishes                OPEN
local normal determines inactive c^(1)              FALSE, PROP. 5.1
global pre-supertrace unramified lift                OPEN (5.6)
c^(1), global square, row (d)                        OPEN
```
