# P122.002 — compactly whitened first-contact theorem

## Status

`PROVED-IN-REPOSITORY`, conditional only on the already recorded certified
strict base window.  This note supplies the missing infinite-dimensional
attainment argument identified in P122.001.

The point is that a prime-power translation born at the edge of a window is
not norm-continuous on raw `L2`.  It is norm-continuous after precomposition
with the compact inclusion of the logarithmic Gamma form domain.  That is
the topology used by the Birman--Schwinger operator.

## 1. Fixed-window realization

Let

\[
 (U_Tf)(t)=T^{-1/2}f(t/T),\qquad -T<t<T,
\]

so that `U_T` is unitary from `L2(-1,1)` to `L2(-T,T)`.  Pull every form
back by `U_T`.  If

\[
 h(\tau)=\operatorname {Re}\psi(5/4+i\tau/2)-\psi(5/4),
\]

the pulled-back Gamma form is

\[
 \mathcal H_T(f)=\int_{\mathbb R}h(\xi/T)|\widehat f(\xi)|^2d\xi. \tag{1.1}
\]

On every compact interval `J compact-subset (0,infinity)`, these forms have
the common domain

\[
 \mathcal Q=\left\{f:\int\log(2+|\xi|)|\widehat f(\xi)|^2d\xi<\infty\right\}. \tag{1.2}
\]

Their form norms are uniformly equivalent on `J`.

Indeed `h(tau)=log(1+|tau|)+O(1)`.  Moreover
`sup_tau |tau h'(tau)|<infinity`: on compact `tau` this is continuity, and
at infinity it follows from the standard trigamma asymptotic
`psi'(z)=z^(-1)+O(|z|^(-2))` in the fixed right half-plane.  Therefore

\[
 \sup_{\xi\in\mathbb R}|h(\xi/T)-h(\xi/S)|
 \le C_J|\log(T/S)|.                                  \tag{1.3}
\]

In particular `T -> H_T` is norm-continuous as a form on `Q`.

The embedding

\[
 \iota:\mathcal Q\longrightarrow L^2(-1,1)             \tag{1.4}
\]

is compact: bounded form norm gives uniformly small Fourier tails, and the
bounded-frequency pieces are precompact on a bounded interval.

## 2. Compact-upgrade lemma

### Lemma 2.1

Let `C:E->H` be compact and let `B_s:H->K` be uniformly bounded near `s_0`.
If `B_s -> B_(s_0)` strongly, then

\[
 \|(B_s-B_{s_0})C\|_{E\to K}\longrightarrow0.          \tag{2.1}
\]

#### Proof

Approximate `C` in norm by a finite-rank operator `C_N`.  Strong convergence
is uniform on the finite-dimensional range of `C_N`; uniform boundedness
controls `(B_s-B_(s_0))(C-C_N)`.  First let `s->s_0`, then `N->infinity`.
QED.

For `0<=alpha<=2`, extend by zero to `L2(-1,1)` the maps

\[
 J_{\alpha,\pm}f(x)=2^{-1/2}
 \mathbf1_{[-1,1-\alpha]}(x)[f(x+\alpha)\pm f(x)]. \tag{2.2}
\]

Translations and interval cutoffs show that `J_(alpha,+/-)` are uniformly
bounded and strongly continuous in `alpha`; at `alpha=2` they converge
strongly to zero.  Lemma 2.1 gives

\[
 \|[J_{\alpha,\pm}-J_{\alpha_0,\pm}]\iota\|_{\mathcal Q\to L^2}
 \longrightarrow0.                                      \tag{2.3}
\]

For a prime power `n`, `alpha_n(T)=log(n)/T`.  Hence (2.3) proves norm
continuity of every whitened prime channel, including at its birth
`log(n)=2T`.  Only finitely many channels occur locally in `T`, so their
weighted sum is norm-continuous.

The pulled-back resolvent kernel has kernel

\[
 T e^{-T|x-y|/2},                                      \tag{2.4}
\]

which is norm-continuous on `L2(-1,1)` (even in Hilbert--Schmidt norm) for
`T` in a compact interval.  The scalar beta channel is constant.

## 3. Moving Tate space

After pullback, the two Tate functionals are nonzero scalar multiples of

\[
 \ell_{T,\pm}(f)=\int_{-1}^{1}e^{\pm Tx/2}f(x)dx.       \tag{3.1}
\]

Their representing vectors depend smoothly on `T`, and their Gram matrix
is invertible for every `T>0`.  Thus the orthogonal projections `P_T` onto

\[
 \mathcal P_T=\ker\ell_{T,+}\cap\ker\ell_{T,-}          \tag{3.2}
\]

are norm-continuous on `L2`.  Their finite-rank corrections have smooth
range and are also norm-continuous on `Q`.

Locally there is consequently a norm-continuous family of invertible maps

\[
 V_T:\mathcal P_{T_0}\cap\mathcal Q
       \longrightarrow\mathcal P_T\cap\mathcal Q,       \tag{3.3}
\]

with `V_(T_0)=I`; for example use the standard polar intertwiner of two
nearby projections.  This reduces the moving constraint to one fixed form
domain.

## 4. Continuity of the generalized compact operator

On the primitive space use the phase-114 decomposition

\[
 q_T=-B_{\rm nuc,T}^{\rm prim}
     =\mathcal R_T-\mathcal W_T^*\mathcal W_T,           \tag{4.1}
\]

where

\[
 \mathcal R_T=\mathcal H_T+
 \sum_{p^k<e^{2T}}{\log p\over p^{k/2}}J_{p^k,-}^*J_{p^k,-}. \tag{4.2}
\]

The Gamma form is coercive on every fixed bounded window and has compact
form-domain embedding.  Sections 1--3 imply, after conjugation by `V_T`,
that the reference forms are locally uniformly coercive, have a common
domain, and are norm-continuous there.  The load forms
`W_T^*W_T` are compact relative to that domain and norm-continuous.

By the representation theorem for uniformly coercive forms, the associated
Riesz maps and their inverse square roots vary continuously between the
form space and its anti-dual.  Equivalently, the generalized compact
operators

\[
 K_T=\mathcal R_T^{-1/2}\mathcal W_T^*\mathcal W_T
             \mathcal R_T^{-1/2}                         \tag{4.3}
\]

(transported to one fixed primitive Hilbert space) vary in operator norm.
Each `K_T` is positive and compact.  Consequently

\[
 \kappa(T):=\|K_T\|
 =\sup_{0\ne F\in\mathcal P_T}
 {\|\mathcal W_TF\|^2\over\mathcal R_T(F,F)}            \tag{4.4}
\]

is continuous on `(0,infinity)`, including every prime-power threshold.

No raw-`L2` norm continuity of a newborn translation was used.

## 5. First-contact theorem

### Theorem 5.1

Assume there is a certified `T_0>0` for which

\[
 q_{T_0}(F)>0\qquad(0\ne F\in\mathcal P_{T_0}),          \tag{5.1}
\]

and suppose row (d) fails at some finite `T_1>T_0`.  Then there are
`T_* in (T_0,T_1)` and `0 ne F_* in P_(T_*) cap Q` such that

\[
 q_{T_*}\ge0,\qquad
 q_{T_*}(F_*,F_*)=0,\qquad
 P_{T_*}\mathscr A_{T_*}P_{T_*}F_*=0.                   \tag{5.2}
\]

The vector can be chosen with definite reflection parity.

#### Proof

By (4.1)--(4.4), (5.1) says `kappa(T_0)<1`, while failure at `T_1` says
`kappa(T_1)>1`.  Continuity supplies a first `T_*` with
`kappa(T_*)=1` and `kappa(T)<=1` up to that point.  Since `K_(T_*)` is
compact and positive, its nonzero norm is an eigenvalue.  Let `u_*` be a
unit eigenvector with `K_(T_*)u_*=u_*` and put
`F_*=mathcal R_(T_*)^(-1/2)u_*`.  Equations (4.1) and (4.4) give (5.2); polarization
of the nonnegative closed form turns zero quadratic value into membership
in its operator kernel.  Reflection commutes with every term and with the
Tate projection, so the kernel splits into even and odd parts; one nonzero
part supplies the stated parity vector.  QED.

### Corollary 5.2 — application to the programme

The interval certificate summarized in phase 118, W4, proves a strictly
positive full-space margin at `T_0=log 2`, not merely finite Galerkin
positivity.  Therefore any later failure of row (d) produces the
first-contact state used conditionally throughout phase 121.

The conclusion is an attainment theorem only.  It supplies no vanishing of
the oriented residue and no sign beyond the first contact.

The later-retracted D.181 claim at `T=(1/2)log5` is not a dependency; see
P122.004.  The base used here is only the surviving `T=log2` certificate.

## 6. Resolution of P122.001

The concern in P122.001 was valid for the raw compact-kernel description:
strong convergence alone does not control a spectral edge.  The additional
fact needed there is the compact Gamma form embedding.  Lemma 2.1 upgrades
the moving/born channels to norm continuity in the whitened topology, and
compactness of `K_T` makes its top eigenvalue attained at level one.

Thus the first-contact implication is now supported by an explicit proof,
provided the cited strict base certificate remains valid under the separate
certificate audit.
