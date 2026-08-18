# 105_05 — Nodal flux, Bregman local time, and the literal-Mangoldt resonance gate

## Result

Let (R=log X), and define the normalized zero-free Euler
approximant

\[
 L_R(s)=
 \sum_{\log m\le R}{\Lambda(m)\over\log m}
       (m^{-s}-m^{-1})
 +\int_0^R {1-e^{(1-s)r}\over r}\,dr,                 \tag{1}
\]

\[
 u_R(t)=\Re L_R(\tfrac12+it),
 \qquad
 d\nu(t)={dt\over2\pi(t^2+1/4)},
 \qquad
 M_R=\int_{\mathbb R}(-u_R(t))_+\,d\nu(t).            \tag{2}
\]

The apparent singularity in (1) at (r=0) is removable.  Since

\[
 \int_{\mathbb R}\cos(tr)\,d\nu(t)=e^{-r/2},          \tag{3}
\]

one has (int u_R,d\nu=0), and hence (M_R) is also the positive
logarithmic mass of the approximant.

Three exact statements are proved below.

1.  The target has the free-boundary representation

    \[
    \boxed{
    M_R={1\over2\pi}
    \int_{\Gamma_R}
    \log\left|{s\over s-1}\right|
    \left|
      \sum_{m\le e^R}\Lambda(m)m^{-s}
      -\int_1^{e^R}x^{-s}\,dx
    \right|d\mathcal H^1(s),}                         \tag{4}
    \]

    where

    \[
      \Gamma_R=\{s:\Re s>\tfrac12,\ \Re L_R(s)=0\}. \tag{5}
    \]

2.  Smoothing the hinge controls the complete nonlinear crossing cost.
    If

    \[
      \phi_\delta(x)=\delta\log(1+e^{-x/\delta}),
    \]

    then, with the notation introduced in Section 3,

    \[
    \boxed{
    M_R\le
    \delta\log2+left|\int_{(0,R]}G_\delta(r)\,dC(r)\right|
    +{\log R+O(1)\over16\delta}.}                     \tag{6}
    \]

    Thus the Bregman/local-time part is only logarithmic.

3.  The remaining linear term in (6) cannot be controlled from a
    bounded prime-number-theorem clock, a Vinogradov--Korobov envelope,
    positivity of all atoms, and logarithmic quadratic variation.  A
    positive prime-density-scale atomic model satisfying all those
    properties has

    \[
      M_R\gg {\exp\{R/2-\eta(R)\}\over R^2},           \tag{7}
    \]

    with (eta(R)) of Vinogradov--Korobov size.

Consequently the surviving theorem is sharply identified: one must rule
out fixed logarithmic-frequency resonance for the **literal** atoms
(Lambda(p^k)=\log p).  Neither the linear renewal identity
(Lambda*\mathbf 1=\log) nor the quadratic crossing estimate does so.
This document does not prove that non-resonance statement and therefore
does not prove RH.

## 1. The exact prime--continuous clock

Put

\[
 Q_r(s)={1-e^{(1-s)r}\over r},
 \qquad
 q_r(t)=\Re Q_r(\tfrac12+it)
 ={1-e^{r/2}\cos(tr)\over r}.                          \tag{8}
\]

Between prime-power nodes,

\[
 \partial_R L_R(s)=Q_R(s).                             \tag{9}
\]

At (r=\log m), the jump of (1) is

\[
 \Delta L_r(s)
 ={\Lambda(m)\over\log m}(m^{-s}-m^{-1})
 =-{\Lambda(m)\over m}Q_r(s).                         \tag{10}
\]

Hence (1) is the single coupled Stieltjes integral

\[
 L_R(s)=\int_{(0,R]}Q_r(s)\,dC(r),                    \tag{11}
\]

\[
 dC(r)=dr-
 \sum_{m\ge2}{\Lambda(m)\over m}\,
 \delta_{\log m}(dr),
 \qquad
 C(R)=R-\sum_{m\le e^R}{\Lambda(m)\over m}.          \tag{12}
\]

The prime number theorem gives (C(R)\to\gamma).  Formula (11), rather
than a separated prime and pole estimate, is the correct starting point.

## 2. Free-boundary formula

Use

\[
 z={s-1\over s},\qquad s={1\over1-z},
 \qquad \ell_R(z)=L_R\!\left({1\over1-z}\right).     \tag{13}
\]

The disk boundary is the critical line, normalized Lebesgue measure on
the boundary is exactly (d\nu), and (ell_R(0)=0).  Set

\[
 v_R(z)=(-\Re\ell_R(z))_+.
\]

Distributionally,

\[
 \Delta v_R=
 |\ell_R'(z)|\,
 \mathcal H^1\!\restriction_{\{\Re\ell_R=0\}}.       \tag{14}
\]

Critical nodal points are isolated unless (ell_R) is constant and
carry no (mathcal H^1)-mass.  Green's formula in the disk, using
(v_R(0)=0), gives

\[
 \int_{\partial\mathbb D}v_R\,dm
 ={1\over2\pi}\int_{\{\Re\ell_R=0\}}
 \log{1\over|z|}\,|\ell_R'(z)|\,d\mathcal H^1(z).     \tag{15}
\]

Now

\[
 -\partial_sL_R(s)=
 \sum_{m\le e^R}\Lambda(m)m^{-s}
 -\int_1^{e^R}x^{-s}\,dx,                             \tag{16}
\]

and the Jacobians cancel:

\[
 |\ell_R'(z)|\,d\mathcal H^1(z)
 =|\partial_sL_R(s)|\,d\mathcal H^1(s).               \tag{17}
\]

Equations (13)--(17) prove (4).

There is also an oriented form.  On every regular nodal arc orient by
increasing (Im L_R).  If

\[
 P_R'(s)={L_R(s)\over s(s-1)},                         \tag{18}
\]

then integration by parts along the nodal network yields

\[
 M_R={1\over2\pi}\Im
 \sum_C\{P_R(b_C)-P_R(a_C)\}.                         \tag{19}
\]

The apparent pole at (s=1) in (18) is removable because (L_R(1)=0).
Formula (19) does not create cancellation: the phase orientation is the
positive boundary orientation of every component of
({\Re L_R<0}).  Conjugate branches add, and critical vertices merely
reconnect arcs.  By the maximum principle every negative component meets
the critical boundary.  Cauchy's theorem therefore transports its
interior flux back to its own negative boundary interval, which is the
original contribution to (M_R).

## 3. Exact smoothed-hinge estimate

For (delta>0), define

\[
 \mathcal M_\delta(R)=\int\phi_\delta(u_R(t))\,d\nu(t),
 \qquad
 G_\delta(r)=\int\phi_\delta'(u_{r-}(t))q_r(t)\,d\nu(t).
                                                                    \tag{20}
\]

The elementary bounds

\[
 x_-\le\phi_\delta(x)\le x_-+\delta\log2,
 \quad -1\le\phi_\delta'\le0,
 \quad 0\le\phi_\delta''\le{1\over4\delta}          \tag{21}
\]

will be used without discarding any prime--continuous cross term.
Between atoms, (9) gives

\[
 d\mathcal M_\delta(r)=G_\delta(r)\,dr.               \tag{22}
\]

At (r=\log m), put (b_m=\Lambda(m)/m).  Taylor's formula with
nonnegative Bregman remainder gives

\[
 \mathcal M_\delta(r+)-\mathcal M_\delta(r-)
 =-b_mG_\delta(r)+E_{m,\delta},                        \tag{23}
\]

\[
 0\le E_{m,\delta}
 \le {b_m^2\over8\delta}\int q_r(t)^2\,d\nu(t).      \tag{24}
\]

The Cauchy characteristic function (3) gives the exact norm

\[
 \int q_r(t)^2\,d\nu(t)={e^r-1\over2r^2}.            \tag{25}
\]

For (m=p^k), (Lambda(m)/\log m=1/k), so

\[
 b_m^2\|q_{\log m}\|_2^2
 ={1-m^{-1}\over2k^2m}.                               \tag{26}
\]

Mertens' theorem for the primes and absolute convergence of the
higher-power contribution imply

\[
 \sum_{p^k\le e^R}b_{p^k}^2\|q_{\log p^k}\|_2^2
 ={1\over2}\log R+O(1).                               \tag{27}
\]

Summing (22)--(24), using (mathcal M_\delta(0)=\delta\log2) and
(M_R\le\mathcal M_\delta(R)), proves (6).

Thus the nonlinear crossing cost is not the critical loss.  The only
uncontrolled quantity in (6) is the adaptive linear correlation

\[
 \int_{(0,R]}G_\delta(r)\,dC(r).                       \tag{28}
\]

Integration by parts and the VK estimate for (C(r)-\gamma) give only
the envelope

\[
 \exp\{R/2-\eta(R)\}\operatorname{poly}(R),           \tag{29}
\]

because (|q_R|_2\asymp e^{R/2}/R).  The next section
shows that this loss is structural for the stated inputs.

## 4. Positive atomic resonance countermodel

Fix (omega>0) and (0<\varepsilon<1).  First consider the positive
continuous intensity

\[
 dA_*(r)=(1-\varepsilon\cos(\omega r))\,dr,
 \qquad dC_*(r)=dr-dA_*(r)
 =\varepsilon\cos(\omega r)\,dr.                      \tag{30}
\]

Its cumulative clock is bounded.  Nevertheless, at (t=\omega),

\[
 \int_1^Rq_r(\omega)\,dC_*(r)
 =\varepsilon\int_1^R
 {1-e^{r/2}\cos^2(\omega r)\over r}\,dr
 \le-c_\omega\varepsilon{e^{R/2}\over R}.            \tag{31}
\]

The same bound, with a smaller constant, holds on a (t)-interval of
length (c/R).  Since the Cauchy density is positive there,

\[
 \int(-u_R)_+\,d\nu\gg {e^{R/2}\over R^2}.            \tag{32}
\]

This model can be atomized at the prime-density scale.  Choose a mesh

\[
 r_{j+1}-r_j=r_je^{-r_j},
 \qquad
 a_j=\int_{r_j}^{r_{j+1}}
       (1-\varepsilon\cos(\omega r))\,dr>0,            \tag{33}
\]

and replace (dA_*) by (sum_ja_j\delta_{r_j}).  Standard quadrature
on each cell gives a total (O(1)) error in (31), uniformly for (t)
in a compact neighborhood of (omega).  Moreover,

\[
 \sum_{r_j\le R}a_j^2\|q_{r_j}\|_2^2=O(\log R),       \tag{34}
\]

and the cumulative clock remains bounded.  Therefore (32) survives in
a positive atomic model with the same atom density, atom size, and
quadratic-variation scales as the prime-power clock.

Finally replace the constant (arepsilon) by a smooth decreasing

\[
 \varepsilon(r)=e^{-\eta(r)},
 \qquad
 \eta(r)=c r^{3/5}(\log r)^{-1/5}.                    \tag{35}
\]

The model now has a VK-scale relative PNT envelope, while the resonant
calculation gives (7).  Positivity, PNT/VK, bounded cumulative clock and
the logarithmic Bregman budget are therefore jointly insufficient.

## 5. Exact surviving obligation

Equation (6) shows that a successful proof may use the smoothed hinge,
but it must establish a literal-Mangoldt non-resonance estimate such as

\[
 \boxed{
 \left|\int_{(0,R]}G_\delta(r)\,dC_\Lambda(r)\right|
 =e^{o(R)}}                                             \tag{36}
\]

for a choice (delta=e^{o(R)}), where (G_\delta) is the adaptive
selector generated by the same (u_R), not an arbitrary test.  The
countermodel proves that (36) cannot be inferred from a PNT envelope or
from quadratic variation.  The convolution identity
(Lambda*\mathbf1=\log) cancels the non-adaptive linear clock, but
deconvolving it divides by (zeta) and reinstates precisely the possible
off-line zeros.

Thus the open mathematical content is no longer the local-time term: it
is the adaptive, fixed-frequency non-resonance of the ordinary-prime
clock.  Establishing (36), with a quantitative bridge to the Deep or Li
criterion, is the remaining proof obligation.

## 6. Vaughan and Heath--Brown do not supply (36)

There is an exact reason that the standard bilinear decompositions stop
at the same boundary.  For

\[
 \mathcal M_D(t)=\sum_{n\le D}{\mu(n)\over n^{1/2+it}},
 \qquad M(x)=\sum_{n\le x}\mu(n),                      \tag{37}
\]

the Cauchy kernel (3) gives

\[
\begin{aligned}
 \|\mathcal M_D\|_{L^2(\nu)}^2
 &=\sum_{m,n\le D}{\mu(m)\mu(n)\over\max(m,n)}\\
 &= {M(D)^2\over D}
   +\sum_{n<D}{M(n)^2\over n(n+1)}.                   \tag{38}
\end{aligned}
\]

The second equality follows from

\[
 {1\over\max(m,n)}
 =\sum_{k\ge\max(m,n)}{1\over k(k+1)}.                \tag{39}
\]

Consequently

\[
 \|\mathcal M_D\|_2^2=D^{o(1)}
 \quad\Longleftrightarrow\quad
 M(D)=D^{1/2+o(1)},                                    \tag{40}
\]

and the assertion on the right is itself equivalent to RH.  The best
unconditional VK/Mertens input gives only

\[
 \|\mathcal M_D\|_2
 \le D^{1/2}\exp\{-\eta(\log D)\}\operatorname{polylog}(D). \tag{41}
\]

Applying Vaughan's identity to the linear term in (6) is exact, but a
Type-II coefficient contains

\[
 \phi_\delta'\bigl(u_{\log(dr)^-}(t)\bigr),            \tag{42}
\]

which depends jointly on the product (dr) and on the complete prime
prefix below it.  Thus the adaptive coefficient does not factor into a
(d)-polynomial and an (r)-polynomial.  Replacing (42) by its bound
(|\phi_\delta'|\le1) forces the Gram norm (38).  On a balanced block
(DE\asymp e^R), the resulting scale is

\[
 \exp\{R/2-o(R)\},                                     \tag{43}
\]

not (e^{o(R)}).  A fixed-order Heath--Brown identity merely replaces
this by finitely many factors whose lengths still multiply to (e^R).
A growing-order identity creates more pieces but no new independent
frequency variable: all phases remain functions of the single sum of
the logarithms.

Therefore Type I/II mean values prove (36) only if one imports the
Mertens energy (40), or if one finds a new estimate that preserves and
uses the self-consistency (42).  The first option assumes an RH-equivalent
input; the second remains open.
