# D.59 — An explicit coercive primitive gap at the first prime threshold

## 1. Purpose and result

D.58 reduced the startup problem at

\[
 T_2={\log2\over2}                                       \tag{1.1}
\]

to a finite seed, but did not certify its sign.  This note proves the sign
directly, without a Galerkin approximation.  The Gamma density is expanded
into elementary exponential resolvents, whose first parity eigenvalues and
eigenfunctions are known from a second-order boundary problem.

The result is the explicit source-side estimate

\[
 \boxed{
 QW_{T_2}(F,F)\geq \gamma_2\|F\|_2^2,
 \qquad F\in\ker M_+\cap\ker M_-,
 \qquad \gamma_2>0.0409.}                                 \tag{1.2}
\]

At the endpoint the `p=2` translated supports meet only in a null set, so
(1.2) is the complete form, not a Gamma-only approximation.  No zeta zero,
RH, Sonin strictness or floating spectral sample is used.

## 2. Exponential-resolvent decomposition

Put

\[
 b_j=2j+\tfrac12,
 \qquad
 w_\infty(r)={e^{-r/2}\over1-e^{-2r}}
             =\sum_{j=0}^\infty e^{-b_jr}.                \tag{2.1}
\]

For a zero-extended function on `[-T,T]`, define

\[
 \mathcal E_b(F)=\int_0^\infty e^{-br}
                   \|F-S_rF\|_2^2dr.                     \tag{2.2}
\]

Tonelli and the translation-correlation identity give

\[
 L_{\infty,T}(F,F)=\sum_{j\geq0}\mathcal E_{b_j}(F),      \tag{2.3}
\]

\[
 \mathcal E_b(F)={2\over b}\|F\|_2^2
 -\langle K_{b,T}F,F\rangle,                              \tag{2.4}
\]

where

\[
 (K_{b,T}F)(x)=\int_{-T}^T e^{-b|x-y|}F(y)dy.             \tag{2.5}
\]

The full-line convolution norm is `2/b`; hence

\[
 0<K_{b,T}\leq {2\over b}I,
 \qquad \mathcal E_b\geq0.                               \tag{2.6}
\]

The prime-free direct operator is

\[
 B_T=\Gamma_T=m_0I-L_{\infty,T},
 \qquad m_0=\log\pi-\psi(1/4).                            \tag{2.7}
\]

## 3. Exact eigenvalues of the resolvent kernel

If `K_(b,T)f=lambda f`, differentiation of (2.5) away from the diagonal
and the endpoint identities give

\[
 f''+\mu^2f=0,
 \qquad \lambda={2b\over b^2+\mu^2},                     \tag{3.1}
\]

\[
 f'(-T)=bf(-T),qquad f'(T)=-bf(T).                       \tag{3.2}
\]

In the odd channel the largest eigenvalue is

\[
 \lambda_{j,o}={2b_j\over b_j^2+\mu_{j,o}^2},
 \qquad \mu_{j,o}={x_{j,o}\over T},                      \tag{3.3}
\]

where `x_(j,o)` is the unique root in `(pi/2,pi)` of

\[
 x\cot x=-b_jT.                                           \tag{3.4}
\]

In the even channel the first two eigenvalues are

\[
 \lambda_{j,e,k}={2b_j\over b_j^2+\mu_{j,e,k}^2},
 \qquad \mu_{j,e,k}={x_{j,e,k}\over T},\quad k=0,1,      \tag{3.5}
\]

where

\[
 x_{j,e,0}\tan x_{j,e,0}=b_jT,\quad 0<x_{j,e,0}<\pi/2,  \tag{3.6}
\]

\[
 x_{j,e,1}\tan x_{j,e,1}=b_jT,quad
 \pi<x_{j,e,1}<3\pi/2.                                   \tag{3.7}
\]

The uniqueness assertions follow from strict monotonicity on the displayed
branches.  The normalized first even eigenfunction is proportional to
`cos(mu_(j,e,0)t)`.

## 4. Odd coercivity

For every odd `F`, (3.3) and the max--min principle give

\[
 \mathcal E_{b_j}(F)\geq d_{j,o}\|F\|_2^2,
 \qquad
 d_{j,o}:={2\over b_j}-\lambda_{j,o}.                     \tag{4.1}
\]

At `T=T_2`, directed evaluation of the first twenty uniquely bracketed
roots in (3.4) gives

\[
 \sum_{j=0}^{19}d_{j,o}>5.41313,                           \tag{4.2}
\]

whereas

\[
 m_0=\log\pi+\gamma+{\pi\over2}+3\log2<5.372184.          \tag{4.3}
\]

All omitted terms in (2.3) are nonnegative.  Therefore

\[
 L_{\infty,T_2}(F,F)-m_0\|F\|_2^2
 >0.040946\|F\|_2^2                                      \tag{4.4}
\]

for every odd `F`.  This bound does not even use the odd Tate moment.

## 5. Even coercivity after the Tate ruling

Let

\[
 h(t)=\cosh(t/2),qquad
 \|h\|_2^2=T+\sinh T.                                    \tag{5.1}
\]

For an even primitive function, the two Tate conditions coincide and read

\[
 \langle F,h\rangle=0.                                   \tag{5.2}
\]

Let `phi_j` be the normalized first even eigenfunction of `K_(b_j,T)` and
put

\[
 r_j={\langle h,\cos(\mu_{j,e,0}t)\rangle
 \over\|h\|_2\,\|\cos(\mu_{j,e,0}t)\|_2}.                \tag{5.3}
\]

The entries are elementary:

\[
 \|\cos(\mu t)\|_2^2=T+{\sin(2\mu T)\over2\mu},          \tag{5.4}
\]

\[
 \langle h,\cos(\mu t)\rangle
 ={2\left(\frac12\sinh(T/2)\cos(\mu T)
 +\mu\cosh(T/2)\sin(\mu T)\right)
 \over\mu^2+1/4}.                                        \tag{5.5}
\]

Since `F` is orthogonal to `h`,

\[
 |\langle F,\phi_j\rangle|^2
 \leq(1-r_j^2)\|F\|_2^2.                                \tag{5.6}
\]

The remaining even eigenvalues of `K_(b_j,T)` are at most
`lambda_(j,e,1)`.  Hence

\[
 \langle K_{b_j,T}F,F\rangle
 \leq\left[\lambda_{j,e,1}
 +(\lambda_{j,e,0}-\lambda_{j,e,1})(1-r_j^2)\right]
 \|F\|_2^2.                                               \tag{5.7}
\]

Define

\[
 d_{j,e}={2\over b_j}-\lambda_{j,e,1}
 -(\lambda_{j,e,0}-\lambda_{j,e,1})(1-r_j^2).             \tag{5.8}
\]

At `T=T_2`, directed evaluation of only the first five pairs of roots in
(3.6)--(3.7) gives

\[
 \sum_{j=0}^{4}d_{j,e}>5.45749.                            \tag{5.9}
\]

Together with (4.3) and nonnegativity of the omitted channels,

\[
 L_{\infty,T_2}(F,F)-m_0\|F\|_2^2
 >0.085306\|F\|_2^2                                      \tag{5.10}
\]

for every even `F` satisfying (5.2).

## 6. Rational certification of the constants

The numerical-looking inequalities (4.2), (4.3) and (5.9) are finite
rational certificates:

1. enclose `pi` by Machin's formula and alternating arctangent series;
2. enclose `log 2` by the positive atanh series (D.57(2.5));
3. enclose Euler's constant by harmonic-number remainder bounds;
4. bisect each monotone equation (3.4), (3.6), (3.7) using Taylor bounds
   for sine and cosine with alternating remainders;
5. substitute the resulting rational intervals into (4.1) and (5.3)--(5.8)
   with outward rounding.

The safety margins `4.09e-2` and `8.53e-2` are over four orders of
magnitude larger than the `10^(-6)` endpoint enclosures needed for the
displayed bounds.  The accompanying verifier reproduces the brackets at
high precision; the proof is the finite directed procedure above, not an
assumption based on the printed decimals.

## 7. Assembly of the primitive gap

Reflection diagonalizes `L_(infty,T_2)`.  For
`F=F_e+F_o` in the two-ruling primitive space, (4.4) and (5.10) give

\[
 -B_{T_2}(F,F)=L_{\infty,T_2}(F,F)-m_0\|F\|_2^2
 >0.040946\|F\|_2^2.                                     \tag{7.1}
\]

At `2T_2=log 2`,

\[
 \langle F,S_{\log2}F\rangle=0                           \tag{7.2}
\]

for every zero-extended `L^2([-T_2,T_2])` function, because the two
supports overlap only in one point.  All larger prime-power shifts are
disjoint.  Thus the finite-place part is zero at the endpoint.

Finally, the polar rank-two block vanishes on the primitive space, so
D.49 gives

\[
 QW_{T_2}(F,F)=-B_{T_2}(F,F).                             \tag{7.3}
\]

Equations (7.1)--(7.3) prove Theorem (1.2).

## 8. Consequence for the interval engine

D.57 no longer starts from a semidefinite datum.  It starts from the
explicit margin

\[
 \gamma_2=0.0409.                                        \tag{8.1}
\]

The entering `p=2` hinge is indefinite, but its compressed form is
continuous relative to the Gamma form under the moving-window transport.
Equivalently, the finite Feshbach matrices of D.57 have bounded one-sided
derivative.  Therefore the margin-over-derivative lemma supplies a genuine
number `h_2>0` such that

\[
 QW_T>0\quad\text{on the primitive space for}
 \quad T_2\leq T<T_2+h_2.                                 \tag{8.2}
\]

Computing a convenient rational lower bound for `h_2` is the next
certification step.  Its existence and the nonzero seed are now proved.

## 9. Status

Closed here:

* the equality/kernel problem at the prime-free endpoint;
* an explicit coercive gap in both parity channels;
* exact inclusion of the threshold `p=2` term;
* the startup obstruction of D.57.

Still open globally is propagation through every later prime-power cell.
No global row-D or RH conclusion is asserted in this note.
