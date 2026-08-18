# D.155 — Three-moment Krylov graph reduction

> **Correction (D.166).**  The block identities (1.2), (2.4), and (2.5)
> are valid for the true compressed moments
> \(H_j=S^*(P_TM_{r_T}P_T)^jS\).  Formula (3.1) below instead computes
> \(S^*M_{r_T}^jS\) and omits the time--Tate projector between successive
> multipliers.  Therefore (3.1), and every numerical graph assembled from
> it for \(j\ge2\), is not a certificate for the primitive operator.
> The directed D.162--D.163 integrations certify ambient multiplier moments
> only.  True graph data must reapply \(P_T\) after every multiplication.

## Verdict

The preconditioned Feshbach certificate of D.154 does not require repeated
application of the complete operator to an arbitrary numerical frame.  If
the auxiliary graph is chosen inside the range of the exact coupling
(C=QAS), its graph matrix and its complete squared residual are rational
expressions in only three high-block moments

\[
 M_j=C^*D^jC,\qquad j=0,1,2.                            \tag{0.1}
\]

Moreover, these are recovered from the four full moments
(H_j=S^*A^jS), (1\le j\le4).  Thus all powers (p^k) and the Gamma
factor remain combined inside the same multiplier before the Feshbach
shorting.

A floating Fourier audit at (T=\frac12\log5), using a rank-70 range
graph, gives a conservative preconditioned lower eigenvalue

\[
 3.07336\times10^{-12}>0.                              \tag{0.2}
\]

The audit is not a proof of the endpoint.  It selects a well-conditioned
directed computation: enclose (H_1,\ldots,H_4), freeze a dyadic range
matrix, and verify one interval congruence.  No paper file is modified.

## 1. Recovering the high moments from full moments

Let (S:\mathbb C^n\to W) be an orthonormal synthesis and decompose

\[
 A=\begin{pmatrix}B&C^*\\C&D\end{pmatrix},
 \qquad B=S^*AS,
 \qquad H_j=S^*A^jS.                                   \tag{1.1}
\]

Expansion of block paths gives

\[
\begin{aligned}
 M_0={}&H_2-B^2,\\
 M_1={}&H_3-B^3-BM_0-M_0B,\\
 M_2={}&H_4-B^4-B^2M_0-BM_0B-M_0B^2-M_0^2
          -BM_1-M_1B.                                  \tag{1.2}
\end{aligned}
\]

Every equality in (1.2) is an operator identity; no truncation or spectral
sign is involved.

## 2. A range graph and its exact residual

Freeze a full-column matrix (R\in\mathbb C^{n\times k}) and synthesize

\[
 Y=CR.                                                  \tag{2.1}
\]

The three matrices needed for the Galerkin equation are

\[
 G_Y=R^*M_0R,
 \qquad D_Y=R^*M_1R,
 \qquad C_Y=R^*M_0.                                    \tag{2.2}
\]

Assume (D_Y>0) and put

\[
 Z=D_Y^{-1}C_Y,
 \qquad X=YZ.                                          \tag{2.3}
\]

Then the finite graph part of the Schur complement is

\[
 \mathcal S_Y=B-C_Y^*D_Y^{-1}C_Y,                     \tag{2.4}
\]

and, for the exact residual (\mathcal R=C-DX),

\[
\boxed{
 \mathcal R^*\mathcal R
 =M_0-M_1RZ-Z^*R^*M_1+Z^*R^*M_2RZ.}                   \tag{2.5}
\]

Equations (2.4)--(2.5), together with (D\ge\delta I), yield the entirely
finite sufficient condition

\[
 \boxed{
 \mathcal S_Y-\delta^{-1}\mathcal R^*\mathcal R\ge0.} \tag{2.6}
\]

This is D.154 with a graph whose residual is expressed without applying
(A) to a nonpolynomial trial function.

## 3. Joint-multiplier moment formula

For the zero extension of a primitive column (s_i\) on ([-T,T]), use the
unitary Fourier transform.  The complete full moments are

\[
 (H_j)_{ab}
 ={1\over2\pi}\int_{\mathbb R}
 r_T(\tau)^j\widehat{s_a}(\tau)
 \overline{\widehat{s_b}(\tau)}\,d\tau,               \tag{3.1}
\]

where

\[
 r_T(\tau)=\mathrm{Re}\,\psi
 \left({1\over4}+{i\tau\over2}\right)-\log\pi
 -2\sum_{p^k\le e^{2T}}{\log p\over p^{k/2}}
       \cos(k\tau\log p).                             \tag{3.2}
\]

Thus (3.1) contains all active prime powers and Gamma pointwise, before
raising the multiplier to a power.  For a normalized Legendre column,

\[
 \widehat\phi_m(\tau)
 =\sqrt{2T(2m+1)}\,(-i)^m j_m(T\tau),                  \tag{3.3}
\]

so (3.1) is a one-dimensional directed special-function integral.  The
tail is integrable for each (j\le4).  Formula (3.3), rather than sampled
Fourier data, is the required source for the interval enclosure.

## 4. Selection audit

The non-directed audit used:

* (2^{18}) Fourier nodes on a periodic box of length (64);
* the exact two-moment projection on the spatial grid;
* the 168-dimensional constrained Legendre frame of D.148;
* the first 70 left singular directions of (C=QAS);
* the already certified complement constant (\delta=0.218).

The first eigenvalues of the graph shorting were

\[
 3.07652548\,10^{-12},\quad
 6.13419208\,10^{-10},\quad
 3.08482068\,10^{-7},\quad
 3.06716163\,10^{-5},                                  \tag{4.1}
\]

and after subtracting (\delta^{-1}\mathcal R^*\mathcal R),

\[
 3.07336902\,10^{-12},\quad
 6.12528046\,10^{-10},\quad
 3.08221914\,10^{-7},\quad
 3.06335334\,10^{-5}.                                  \tag{4.2}
\]

The audit therefore leaves a factor of roughly (10^2) between the
required (10^{-14})-scale entry enclosure and the final smallest margin.
It also confirms that the large unweighted residual is harmless after the
joint multiplier is preconditioned.

## 5. Directed obligation

To turn (4.2) into a theorem, the range matrix (R) must be rounded to
explicit dyadic rationals and the following must be evaluated with outward
rounding:

1. the four matrices (3.1);
2. the three identities (1.2);
3. the solve (2.3) and residual (2.5);
4. a final preconditioned Gershgorin congruence for (2.6).

`114_d_155_three_moment_graph_verify.py` checks (1.2), (2.4), and (2.5)
against a direct finite-dimensional block calculation.
