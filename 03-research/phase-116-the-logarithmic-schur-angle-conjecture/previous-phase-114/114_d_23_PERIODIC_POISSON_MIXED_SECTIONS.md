# Row (d): exact periodic Poisson realization of all finite contacts

## Status

This note constructs the finite-place part of the mixed section map which
was missing from row (a).  Every complete prime-power tower is the
difference between a positive Poisson section norm on the periodic fibre
and its torsor norm.  The construction is exact, monoidal at the translation
level, and uses no zero.  Together with the Hardy oscillator comparison it
places all terms of the row-(d) form in one signed periodic boundary module.
The remaining theorem is the global two-trace frame inequality.

## 1. A single periodic tower

Let

\[
 U_p=S_{\log p}\quad\text{on }L^2(\mathbb R),
 \qquad r_p=p^{-1/2}.                                  \tag{1}
\]

For `0<r<1` and a unitary `U`, define the operator Poisson kernel

\[
 P_r(U)=\sum_{k\in\mathbb Z}r^{|k|}U^k
 =(1-r^2)(I-rU)^{-1}(I-rU^*)^{-1}.                    \tag{2}
\]

The series converges in operator norm and (2) proves `P_r(U)>0`.

### Theorem 1.1 (prime-tower section identity)

For every `F in L^2(R)`,

\[
 2\sum_{k\ge1}\frac{\log p}{p^{k/2}}
       \operatorname{Re}\langle F,S_{k\log p}F\rangle
 =\log p\left(
   \langle F,P_{p^{-1/2}}(U_p)F\rangle-\|F\|^2
             \right).                                \tag{3}
\]

### Proof

Expand the norm-convergent series in (2).  The `k=0` term is `||F||^2`;
the terms `k` and `-k` are conjugate because `U_p` is unitary.  Subtract
the zero term and multiply by `log p`.

Equation (3) retains every exponent `k`; the fact that the reduced contact
mass is always `log p` appears as the common scalar multiplying the Poisson
depth `p^{-k/2}`.

## 2. Actual periodic sections

The unitary `U_p` is the deck translation of the cover

\[
 \mathbb R\longrightarrow C_p=\mathbb R/(\log p)\mathbb Z.           \tag{4}
\]

The positive square root in (2) defines the periodic Poisson section map

\[
 \mathcal J_pF=P_{p^{-1/2}}(U_p)^{1/2}F.              \tag{5}
\]

Then (3) is

\[
 K_p(F,F)=\log p\bigl(\|\mathcal J_pF\|^2-\|F\|^2\bigr).             \tag{6}
\]

Thus the negative summand is not an ad hoc metric: it is the norm of the
same section before Poisson extension, i.e. the graded torsor boundary
norm.  Formula (5) is functorial for translations and conjugation and is
intrinsic to the periodic fibre with its central radius `p^{-1/2}`.

On the Fourier side, (2) is the classical positive Poisson kernel

\[
 \frac{1-p^{-1}}
 {|1-p^{-1/2}e^{-i\tau\log p}|^2}.                    \tag{7}
\]

No claim is made that the sum of (7) over all primes converges pointwise;
the paired physical-space formula is the correct domain.

## 3. Cofinal finite-place module

For a finite set of primes `P`, define

\[
 \mathcal J_PF=(\sqrt{\log p}\,\mathcal J_pF)_{p\in P},
 \qquad
 \mathcal T_PF=(\sqrt{\log p}\,F)_{p\in P}.          \tag{8}
\]

Then

\[
 K_P(F,F)=\|\mathcal J_PF\|^2-\|\mathcal T_PF\|^2.  \tag{9}
\]

If `F` is compactly supported, the correlation in (3) vanishes once
`k log p` exceeds its support diameter.  Although the two norms in (9)
diverge separately as `P` grows, their paired difference stabilizes in the
same cofinal sense as the finite contact of row (c).  Hence (9) defines a
renormalized difference object, not two independent infinite Hilbert norms.

## 4. Addition of the real boundary

Let `partial_infty` be the oscillator derivation of
`114_d_17_ARCHIMEDEAN_OSCILLATOR_BOUNDARY_MODULE.md`.  Its monoidal Hardy
origin and character comparison are proved in
`114_d_22_HARDY_DILATION_CHARACTER_COMPARISON.md`.  The forced real term is

\[
 G_\infty(F,F)=m_0\|F\|^2-\|\partial_\infty F\|^2.   \tag{10}
\]

Combining (9)--(10) gives the exact signed mixed-section identity

\[
 B_{\rm nuc}(F,F)=
 \|\mathcal J_PF\|^2+m_0\|F\|^2
 -\|\mathcal T_PF\|^2-\|\partial_\infty F\|^2       \tag{11}
\]

for every cofinal cutoff containing the active correlations.  Every map in
(11) is defined from periodic sections, torsor metrics or the real Hardy
boundary before the comparison with row (c).  Theorem 1.1 and the Hardy
character theorem prove that the comparison is term by term exact.

## 5. Exact remaining Hodge theorem

Put

\[
 \mathcal S_PF=(\mathcal J_PF,\sqrt{m_0}F),
 \qquad
 \mathcal B_PF=(\mathcal T_PF,\partial_\infty F).      \tag{12}
\]

Then row (d) is precisely

\[
 \|\mathcal S_PF\|\le\|\mathcal B_PF\|
 \quad\text{if}\quad
 \int e^{t/2}F(t)dt=\int e^{-t/2}F(t)dt=0.            \tag{13}
\]

The significance of (13) is categorical: it is now a contraction between
two section/boundary functors on the same periodic--Hardy carrier, rather
than an unexplained sign of a distribution.  Its equality case would be
strict because the oscillator tail and the periodic Poisson maps separate
compactly supported sections.

What is not yet proved is the contraction (13).  It cannot be obtained by
taking norms prime by prime; the obstruction catalogue proves that the
necessary cancellation is global.  A successful proof must construct a
single nonlocal natural transformation

\[
 \mathfrak C:\mathcal B|_{\ker(d_+,d_-)}
       \longrightarrow\mathcal S,
 \qquad \|\mathfrak C\|\le1,                          \tag{14}
\]

with `mathfrak C B F=S F`.  Formula (14), if constructed from the periodic
Yoneda multiplication and Tate duality, is the sought Hodge--Rosati map.
Choosing it by polar decomposition of the already evaluated form would be
circular.

