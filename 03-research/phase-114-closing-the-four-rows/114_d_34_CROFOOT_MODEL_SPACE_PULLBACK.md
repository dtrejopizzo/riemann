# D.34 — Crofoot model-space pullback of the finite contact

## 1. Local theorem

Let `theta` be an inner function on the upper half-plane (or disk), let
`0<r<1`, and put

\[
 \beta=b_r\circ\theta,qquad
 c_r(\theta)=\frac{\sqrt{1-r^2}}{1-r\theta}.           \tag{1.1}
\]

The Crofoot transform

\[
 C_r:K_\theta\longrightarrow K_\beta,qquad
 C_rf=c_r(\theta)f                                   \tag{1.2}
\]

is unitary.

### Proof

For the model-space kernel

\[
 k_w^\theta(z)=\frac{1-\overline{\theta(w)}\theta(z)}
                     {1-\bar wz}                     \tag{1.3}
\]

(or its conformally equivalent upper-half-plane formula), direct
substitution gives

\[
 \frac{1-|\beta(z)|^2}{1-|\theta(z)|^2}
 =\frac{1-r^2}{|1-r\theta(z)|^2},                     \tag{1.4}
\]

and, off the diagonal,

\[
 k_w^\beta(z)=c_r(\theta(z))
       \overline{c_r(\theta(w))}\,k_w^\theta(z).      \tag{1.5}
\]

Thus the adjoint of multiplication by `c_r(theta)` sends the kernel at
`w` in `K_beta` to the kernel at `w` in `K_theta`.  Equation (1.5)
preserves every Gram matrix.  Since kernel vectors span densely in both
model spaces, the multiplier extends to a surjective isometry, proving
(1.2).

For a prime `p`, take

\[
 \theta_p(\tau)=e^{i\tau\log p},\qquad r_p=p^{-1/2}.  \tag{1.6}
\]

Then the boundary multiplier in (1.1) is exactly

\[
 c_{r_p}(\theta_p(\tau))
 =\frac{\sqrt{1-p^{-1}}}{1-p^{-1/2}e^{i\tau\log p}},  \tag{1.7}
\]

the Fourier multiplier of the periodic Poisson operator `A_p` of D.32.
Thus the local section map is intrinsically a Crofoot unitary between the
Tate winding model space and the Frobenius characteristic model space.

## 2. Finite product assembly

Order a finite set `P={p_1,...,p_N}` and write

\[
 \theta_j=\theta_{p_j},\qquad
 \beta_j=b_{r_{p_j}}\circ\theta_j,qquad
 Z_P=\prod_j\theta_j,\qquad B_P=\prod_j\beta_j.       \tag{2.1}
\]

The standard product decomposition of model spaces is

\[
 K_{Z_P}=\bigoplus_{j=1}^N
   \left(\prod_{i<j}\theta_i\right)K_{\theta_j},qquad
 K_{B_P}=\bigoplus_{j=1}^N
   \left(\prod_{i<j}\beta_i\right)K_{\beta_j}.        \tag{2.2}
\]

Multiplication by inner prefixes is unitary.  Hence the block map

\[
 \mathcal C_P:\left(\prod_{i<j}\theta_i\right)f_j
 \longmapsto
 \left(\prod_{i<j}\beta_i\right)C_{r_{p_j}}f_j       \tag{2.3}
\]

is a source-defined unitary `K_(Z_P) -> K_(B_P)`.  Changing the order only
changes the orthogonal factorization, not the two product inner functions
or their phase densities.

For completeness, (2.2) follows by induction from
`K_(alpha beta)=K_alpha direct-sum alpha K_beta`: multiplication by an
inner function is an isometry, and `K_alpha` is perpendicular to
`alpha H^2`.  Applying the local unitary (1.2) on each orthogonal block
then proves (2.3).

## 3. Hilbert--Schmidt contact identity

Let `Theta` be a meromorphic inner function and let `k_x^Theta` denote its
boundary reproducing kernel.  For an orthonormal basis `(e_j)` of
`K_Theta`,

\[
 \sum_j|e_j(x)|^2=\|k_x^\Theta\|^2
 =\frac1{2\pi}\frac1i\frac d{dx}\log\Theta(x),       \tag{3.1}
\]

with the standard upper-half-plane normalization.  Tonelli therefore gives,
for every multiplier `g` for which either side is finite,

\[
 \|M_g:K_\Theta\to L^2(\mathbb R)\|_{\rm HS}^2
 =\frac1{2\pi}\int_{\mathbb R}|g(x)|^2
       \frac1i\frac d{dx}\log\Theta(x)\,dx.          \tag{3.2}
\]

Indeed, choose an orthonormal basis `(e_j)` and apply Tonelli to
`|g(x)|^2 sum_j|e_j(x)|^2`.  Parseval for the reproducing kernel gives
the first equality in (3.1), and the boundary Julia--Caratheodory identity
gives the second.  This proves (3.2) without interchanging signed traces.

Apply (3.2) to `B_P` and `Z_P`, and take `g=widehat F`.  D.33(4.2)--(4.5)
then give the exact finite-place pullback

\[
 \boxed{
 K_P(F,F)=
 \|M_{\widehat F}:K_{B_P}\to L^2\|_{\rm HS}^2
 -\|M_{\widehat F}:K_{Z_P}\to L^2\|_{\rm HS}^2.}    \tag{3.3}
\]

Expanding the phase densities in (3.3) is precisely the sum over every
`p^k`; no prime-power truncation has been made.

Formula (3.3) is the model-space version of the periodic norm identity in
D.32.  It also explains why the existence of the unitary `mathcal C_P` does
not make the two Hilbert--Schmidt norms equal: `mathcal C_P` is unitary
between the model spaces but is multiplication by the non-unimodular
Crofoot factors when viewed in the common boundary `L^2`.

## 4. The two jets in the same analytic coordinate

For compactly supported `F`, `widehat F` is entire and

\[
 M_+(F)=\widehat F(i/2),\qquad M_-(F)=\widehat F(-i/2).               \tag{4.1}
\]

The points `+i/2` and `-i/2` are also the common zero/pole points of the
local scattering ratios

\[
 \frac{\beta_p(\tau)}{\theta_p(\tau)}
 =\frac{1-p^{-1/2}e^{-i\tau\log p}}
        {1-p^{-1/2}e^{ i\tau\log p}}.                \tag{4.2}
\]

Thus the two ruling moments and the local Hardy defects now live in the
same Fourier--Laplace coordinate.  This is the exact two-jet comparison
which was only heuristic in D.31.

## 5. Gamma-coupled Hodge gate

The Gamma oscillator adds

\[
 m_0\|F\|^2-\|\partial_\infty F\|^2                 \tag{5.1}
\]

to (3.3).  Consequently D.32 becomes a difference of a positive
Hilbert--Schmidt model-space norm plus the constant Gamma line, and the
torsor model-space norm plus the oscillator boundary norm.

The required theorem is no longer an unidentified pullback.  It is the
following concrete compression statement: for each support cutoff `Q`, the
adelic Poisson transform must induce, on multipliers satisfying (4.1)=0, a
contraction from the `Z_(P_Q)`--oscillator boundary module to the
`B_(P_Q)`--constant module, intertwining multiplication by `widehat F`.
The Crofoot maps (2.3) give all finite local blocks and the Fourier--Gamma
operator gives the real block.  What remains is to prove that their
Poisson gluing has norm at most one uniformly in `Q`.

This formulation neither invokes the zero divisor nor defines the
contraction from the sign of (3.3).  It also shows precisely why local
unitarity alone is insufficient: contractivity is a theorem about the
two-jet **gluing/compression**, not about any individual place.
