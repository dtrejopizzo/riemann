# P124.010 -- Toeplitz leakage test for one Euler factor

Status: `ONE-SIDED FACTOR TELESCOPES / TWO-SIDED TOEPLITZ COUNTERMODEL`.

This note tests whether the abstract countermodel of P124.009 disappears
once the support anomaly is forced to come from an Euler shift symbol.  It
does not disappear for the first nontrivial two-sided Toeplitz factor.  A
single causal factor has zero Tate collar anomaly by orientation, but the
symmetric one-prime time factor admits a primitive first-contact kernel
after scalar centering while the Tate collar pairing is nonzero.

The conclusion is only a model obstruction.  It does not falsify the full
arithmetic Gamma-plus-all-primes operator; it says that the one-factor
Toeplitz support calculus and the two Tate moments are still insufficient.

## 1. One causal Euler factor telescopes

Let `S` be the bilateral shift on `ell^2(Z)`, `(Sf)_j=f_{j-1}`, and let
`P` be the interval projection onto `{0,...,m-1}` with `N=I-P`.  For the
causal D.240 convention

\[
        \eta_r=(I-rS)^{-1},\qquad \theta_r^*=I-rS,
        \qquad 0<r<1,                               \tag{1.1}
\]

one has `theta_r^* eta_r=I`.  If `f` is supported in `P`, then `eta_r f`
can leak only to the right of the interval.  Applying `I-rS` to that
right exterior tail cannot move it back into `P`.  Hence

\[
        P\theta_r^*N\eta_rP=0.                      \tag{1.2}
\]

The same statement holds for the opposite causal orientation.  Thus a
short one-sided factor may have an exterior score, but it has no D.240
Tate collar `dot D` to test.  It is not a countermodel to `rho`.

## 2. Two-sided one-prime Toeplitz factor

The first nonzero model is the symmetric one-prime factor

\[
        \eta_r=(I-rS)^{-1}(I-rS^{-1})^{-1},
        \qquad
        \theta_r^*=(I-rS)(I-rS^{-1}),               \tag{2.1}
\]

so again `theta_r^* eta_r=I` exactly.  The convolution kernel of `eta_r` is

\[
        k_n={r^{|n|}\over 1-r^2}.                   \tag{2.2}
\]

Since `theta_r^*=(1+r^2)I-rS-rS^{-1}`, only the two exterior neighbor
values can return to the interval.  Therefore, for `f in P ell^2`,

\[
\boxed{
\begin{aligned}
        (D_rf)_0
        &=-{r^2\over1-r^2}\sum_{j=0}^{m-1}r^j f_j,\\
        (D_rf)_{m-1}
        &=-{r^2\over1-r^2}\sum_{j=0}^{m-1}r^{m-1-j}f_j,\\
        (D_rf)_i&=0\qquad(0<i<m-1),
\end{aligned}}                                      \tag{2.3}
\]

where

\[
        D_r=P\theta_r^*N\eta_rP.                    \tag{2.4}
\]

Thus the anomaly is exactly rank at most two and is carried by the two
geometric Tate moments

\[
        \tau_+=(1,r,r^2,\ldots,r^{m-1}),
        \qquad
        \tau_-=(r^{m-1},\ldots,r^2,r,1).            \tag{2.5}
\]

Use the Euler parameter derivative `dot = d/dsigma` with `r=e^{-sigma}`,
so `dot D=-r dD/dr`.  The localized dual-pairing derivative is `-dot D`;
its Hermitian score is

\[
        S_r={-\dot D_r-\dot D_r^*\over2}.           \tag{2.6}
\]

The primitive subspace is

\[
        \mathcal P_r=\{f:\langle f,\tau_+\rangle
        =\langle f,\tau_-\rangle=0\}.               \tag{2.7}
\]

## 3. Concrete finite cell at `m=5`, `r=1/2`

For `m=5`, `r=1/2`, take the symmetric primitive basis

\[
        b_1=(4,0,-17,0,4),
        \qquad b_2=(0,2,-5,2,0).                   \tag{3.1}
\]

Both vectors are orthogonal to

\[
        \tau_+=(1,1/2,1/4,1/8,1/16),
        \qquad
        \tau_-=(1/16,1/8,1/4,1/2,1).               \tag{3.2}
\]

The derivative of the support anomaly is

\[
\dot D=
\begin{pmatrix}
8/9&11/18&7/18&17/72&5/36\\
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0\\
5/36&17/72&7/18&11/18&8/9
\end{pmatrix}.                                      \tag{3.3}
\]

Restricting the Hermitian score `S=(-dot D-dot D^*)/2` to
`span{b_1,b_2}` gives the Gram matrix and score matrix

\[
        G=\begin{pmatrix}321&85\\85&33\end{pmatrix},
        \qquad
        H=\begin{pmatrix}20&1\\1&0\end{pmatrix}.   \tag{3.4}
\]

The generalized eigenvalues are the roots of

\[
        3368\lambda^2-490\lambda-1=0.              \tag{3.5}
\]

Let

\[
        \lambda_-={490-\sqrt{253572}\over6736}<0.  \tag{3.6}
\]

Center the score at first contact by

\[
        L:=S-\lambda_- I
        \quad\text{on }\mathcal P_r.               \tag{3.7}
\]

Then `L>=0` on this primitive two-dimensional cell, and its kernel is
spanned by

\[
        F_-= (1-85\lambda_-)b_1+(321\lambda_- -20)b_2. \tag{3.8}
\]

This is the finite Toeplitz analogue of a first-contact minimizer:

\[
        F_-\in\mathcal P_r,
        \qquad LF_-=0,
        \qquad L\ge0.                              \tag{3.9}
\]

The Tate collar pairing is nevertheless nonzero.  Directly,

\[
        \begin{pmatrix}
        \langle\dot D b_1,\tau_+\rangle\\
        \langle\dot D b_2,\tau_+\rangle
        \end{pmatrix}
        =
        \begin{pmatrix}
        -85/32\\ -17/64
        \end{pmatrix},                              \tag{3.10}
\]

and hence

\[
\boxed{
        \langle\dot D F_-,\tau_+\rangle
        ={17(529\lambda_-+10)\over64}\ne0.}
        \tag{3.11}
\]

Numerically this unnormalized value is approximately `2.3733969874`.  The
normalization of `F_-` is irrelevant: the point is that the collar
functional does not vanish on the centered first-contact kernel.

## 4. What this proves and what it does not prove

The scalar centering in (3.7) is standing in for the missing normalization
channels of the real operator: the Gamma contribution, `m0`, and the full
finite-place sum.  Without such centering, the one-prime symmetric score in
this cell is not itself a first-contact form; its primitive restriction has
a negative eigenvalue.  After centering at that eigenvalue, it satisfies the
abstract first-contact conditions exactly.

Thus the tested implication fails at the Toeplitz support level:

\[
        \theta^*\eta=I,
        \quad D=P\theta^*N\eta P,
        \quad \text{two Tate moments},
        \quad L\ge0,
        \quad LF=0
        \quad\nRightarrow\quad
        \langle\dot D F,\tau_+\rangle=0
\]

is false for the concrete matrices above.

This isolates the remaining possible source of a positive identity.  It
cannot come from a single causal factor, nor from the rank-two anomaly of a
single symmetric Toeplitz factor plus the Tate moments.  A proof of collar
cancellation must use a genuinely additional arithmetic input: interaction
with the Gamma term, multiple prime-power shifts, or the full D.190
shorted block rather than the rank-two boundary return alone.
