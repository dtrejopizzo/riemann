# 106.07 — Curvature rigidity and the sharp variational gate

## Purpose

This note audits the proposed global estimate

\[
 \partial_z^2\log\frac{\widehat\phi_L(z)}{\widehat k_L(z)}
 \longrightarrow 0.
 \tag{1}
\]

There are two rigorous conclusions.

1. In the even sector, (1) is not weaker than locally uniform
   ground/model transform convergence.  Once one scalar normalization is
   fixed, the two statements are equivalent on every common zero-free
   domain.
2. The relative curvature counts the difference of zero divisors by a
   contour integral.  Since every true ground transform has only real
   zeros, (1), together with the CCM model limit
   \(\widehat k_L\to\Xi\), excludes every non-real zero of \(\Xi\).

Thus (1) is a valid closure theorem, but it is force-bearing: proving it
unconditionally proves RH.  Real-rootedness, compact resolvent,
interlacing, or a model Rayleigh excess tending to zero do not imply (1)
without a quantitative ground-line selection estimate.  A sharp abstract
countermodel is given below.

Throughout, logarithmic curvature means the globally defined meromorphic
function

\[
 \mathcal K_F(z):=\left(\frac{F'}F\right)'(z).
 \tag{2}
\]

No choice of a logarithm is needed in (2).

## 1. Affine rigidity of logarithmic curvature

### Theorem 1 — Local curvature/transform equivalence

Let \(\Omega\subset\mathbb C\) be a simply connected domain, and let
\(F_j,G_j\) be holomorphic and zero-free on \(\Omega\).  The following are
equivalent.

1. \(\mathcal K_{F_j}-\mathcal K_{G_j}\to0\) locally uniformly on
   \(\Omega\).
2. There exist \(a_j,b_j\in\mathbb C\) such that

   \[
    e^{-a_j-b_jz}\frac{F_j(z)}{G_j(z)}\longrightarrow1
    \tag{3}
   \]

   locally uniformly on \(\Omega\).

If \(0\in\Omega\), the functions are even, and they are normalized by

\[
 F_j(0)=G_j(0)\ne0,
 \tag{4}
\]

then one can take \(a_j=b_j=0\).  Consequently,

\[
 \boxed{
 \mathcal K_{F_j}-\mathcal K_{G_j}\to0
 \quad\Longleftrightarrow\quad
 F_j/G_j\to1
 }
 \tag{5}
\]

locally uniformly on \(\Omega\).

### Proof

Choose a holomorphic logarithm

\[
 H_j=\log(F_j/G_j)
 \tag{6}
\]

on \(\Omega\).  Fix \(z_0\in\Omega\) and put

\[
 A_j(z)=H_j(z_0)+(z-z_0)H_j'(z_0).
 \tag{7}
\]

On every compact \(K\Subset\Omega\), choose a larger compact connected
set containing \(K\), \(z_0\), and paths of uniformly bounded length from
\(z_0\) to each point of \(K\).  Two integrations along these paths give

\[
 \sup_{z\in K}|H_j(z)-A_j(z)|
 \le C_K\sup_{z\in K'}|H_j''(z)|.
 \tag{8}
\]

Therefore \(H_j''\to0\) locally uniformly if and only if
\(H_j-A_j\to0\) locally uniformly.  Exponentiation proves (3), with
\(b_j=H_j'(z_0)\) and \(a_j=H_j(z_0)-z_0H_j'(z_0)\).  The converse follows
from Cauchy's estimates applied to the logarithm of the left side of (3).

Under (4), choose the logarithm with \(H_j(0)=0\).  Evenness gives
\(H_j'(0)=0\).  Hence the affine function (7) is identically zero and
(5) follows.  \(\square\)

### Consequence for the CCM ground state

Put

\[
 F_L=\widehat\phi_L,
 \qquad G_L=\widehat k_L.
 \tag{9}
\]

Both source functions are even.  On any common zero-free domain containing
the origin, normalize \(F_L(0)=G_L(0)\).  The target (1) is then exactly

\[
 \widehat\phi_L/\widehat k_L\longrightarrow1.
 \tag{10}
\]

Thus passing from transforms to second logarithmic derivatives removes an
irrelevant affine normalization, but it does not remove the CCM
ground/model approximation problem.

## 2. Curvature is an exact zero-divisor observable

### Lemma 2 — Contour zero count

Let \(F\) be holomorphic in a neighbourhood of the closure of a bounded
Jordan domain \(D\), with no zero on \(C=\partial D\).  For any
\(z_*\in\mathbb C\),

\[
 \boxed{
 N_F(D)
 =-\frac1{2\pi i}\int_C (z-z_*)\mathcal K_F(z)\,dz,
 }
 \tag{11}
\]

where \(N_F(D)\) counts zeros with multiplicity.

### Proof

At a zero \(a\) of multiplicity \(m\),

\[
 \mathcal K_F(z)=-\frac{m}{(z-a)^2}+O(1).
 \tag{12}
\]

The residue of \((z-z_*)\mathcal K_F(z)\) at \(a\) is \(-m\).
Summing residues proves (11).  \(\square\)

### Theorem 3 — Divisor rigidity and the RH consequence

Assume:

1. every \(F_L=\widehat\phi_L\) has only real zeros;
2. \(G_L=\widehat k_L\to\Xi\) locally uniformly;
3. on every fixed smooth contour avoiding the zeros of \(F_L\) and \(G_L\),

   \[
    \mathcal K_{F_L}-\mathcal K_{G_L}\longrightarrow0
    \tag{13}
   \]

   uniformly.

Then every zero of \(\Xi\) is real.

### Proof

Suppose that \(\Xi\) has a non-real zero \(\zeta\) of multiplicity \(m\).
Choose a closed disk \(D\) centred at \(\zeta\), disjoint from the real
axis, whose boundary contains no zero of \(\Xi\), and containing no other
zero of \(\Xi\).  By local uniform convergence and Rouché's theorem,

\[
 N_{G_L}(D)=m
 \tag{14}
\]

for all sufficiently large \(L\).  Since all zeros of \(F_L\) are real,

\[
 N_{F_L}(D)=0.
 \tag{15}
\]

Apply Lemma 2 to \(F_L\) and \(G_L\) on \(C=\partial D\).  Uniform
convergence in (13) gives

\[
 N_{F_L}(D)-N_{G_L}(D)\longrightarrow0.
 \tag{16}
\]

The left side equals \(-m\) for all sufficiently large \(L\), a
contradiction.  Hence \(\Xi\) has no non-real zero.  \(\square\)

This proof does not require a branch of either logarithm and is unaffected
by zeros inside the contour.  It shows directly that the proposed
curvature limit carries the complete zero-location content.

## 3. Cauchy-transform form

If \(F\) is an even Cartwright function with real nonzero zeros
\(\{\pm x_j\}\), counted with multiplicity, Hadamard factorization gives

\[
 \mathcal K_F(z)
 =-\sum_j\left(\frac1{(z-x_j)^2}+\frac1{(z+x_j)^2}\right),
 \tag{17}
\]

locally uniformly off the real zero set.  The affine exponential factor
has disappeared.  Therefore (1) is precisely convergence of the second
Cauchy transforms of the two zero divisors.  On the positive imaginary
axis,

\[
 \mathcal K_F(iy)
 =-2\sum_j\frac{x_j^2-y^2}{(x_j^2+y^2)^2}.
 \tag{18}
\]

Real-rootedness says that the divisor measure in (17) is positive and
supported on \(\mathbb R\); it supplies no identification of that measure.
The missing theorem is exactly the identification of its Cauchy transform
with the divisor of \(\Xi\).

Equivalently, \(-F'/F\) is a Herglotz function in the upper half-plane.
Convergence of its derivative determines it only up to an additive
constant; evenness and normalization at the origin remove that constant.
This is the Pick/de Branges version of Theorem 1, not an additional source
of arithmetic information.

## 4. Sharp variational sufficient condition

Let \(A_L\) be the continuum semilocal Weil operator in the even sector,
with simple unit ground state \(\phi_L\) and first two even eigenvalues

\[
 \epsilon_{0,L}<\epsilon_{1,L},
 \qquad g_L=\epsilon_{1,L}-\epsilon_{0,L}>0.
 \tag{19}
\]

Normalize the projected model \(q_L=k_L/\|k_L\|_2\), and put

\[
 R_L=\langle A_Lq_L,q_L\rangle.
 \tag{20}
\]

Expansion in an eigenbasis gives

\[
 1-|\langle q_L,\phi_L\rangle|^2
 \le\frac{R_L-\epsilon_{0,L}}{g_L},
 \tag{21}
\]

and hence, after choosing the phase,

\[
 \|q_L-e^{i\vartheta_L}\phi_L\|_2
 \le
 \left(\frac{2(R_L-\epsilon_{0,L})}{g_L}\right)^{1/2}.
 \tag{22}
\]

For \(B>0\), Cauchy--Schwarz on
\([\lambda^{-1},\lambda]\), \(L=2\log\lambda\), gives

\[
 \sup_{|\Im z|\le B}
 |\widehat q_L(z)-e^{i\vartheta_L}\widehat\phi_L(z)|
 \le
 W_{L,B}
 \left(\frac{2(R_L-\epsilon_{0,L})}{g_L}\right)^{1/2},
 \tag{23}
\]

where

\[
 W_{L,B}
 =\left(\frac{\lambda^{2B}-\lambda^{-2B}}{2B}\right)^{1/2}
 \quad(B>0),
 \qquad W_{L,0}=L^{1/2}.
 \tag{24}
\]

 Together with the relative-error transfer lemma of 106.06, this proves
(1) on a compact \(K\) whenever, on a slightly larger zero-free compact,

\[
 \boxed{
 \frac{\|k_L\|_2W_{L,B}}{\inf|\widehat k_L|}
 \left(\frac{R_L-\epsilon_{0,L}}{g_L}\right)^{1/2}
 \longrightarrow0,
 }
 \tag{25}
\]

with the projection-tail term included if \(q_L\) is a finite projection.
This is the curvature-specialized form of the weighted ground/gap gate
already isolated in E101.095.  Neither compact resolvent nor the fact that
\(R_L-\epsilon_{0,L}\to0\) controls the quotient in (25).

## 5. Exact Weil-radical bifurcation

The explicit formula gives a second, source-specific description of the
gate.  Let \(k\) be Riemann's full kernel, so that

\[
 \widehat k=\Xi.
 \tag{26}
\]

The zero-side polarization of the Weil form is absolutely convergent when
one entry is \(k\).  Since \(\widehat k\) vanishes on the complete
nontrivial divisor, one has

\[
 \boxed{QW(k,g)=0}
 \tag{27}
\]

for every admissible \(g\).  Extend \(k_L\) by zero outside its support and
put \(e_L=k_L-k\).  If \(A_L\phi_L=\epsilon_{0,L}\phi_L\), then

\[
 \boxed{
 \epsilon_{0,L}\langle\phi_L,k_L\rangle
   =QW(\phi_L,k_L)
   =QW(\phi_L,e_L),
 }
 \tag{28}
\]

and, by (27),

\[
 \boxed{QW(k_L,k_L)=QW(e_L,e_L).}
 \tag{29}
\]

Thus a small source residual proves only that the product

\[
 |\epsilon_{0,L}|\,|\langle\phi_L,k_L\rangle|
 \tag{30}
\]

is small.  It does not decide between a near-zero least eigenvalue and a
ground state asymptotically orthogonal to the model.

This alternative is not an artefact of abstract operator theory.  In the
additive coordinate, let \(z_0=x_0+ia\), \(a\ne0\), be a hypothetical
non-real zero of \(\Xi\).  The Paley--Wiener evaluation vector on
\([-L/2,L/2]\) is

\[
 K_{L,z_0}(x)=e^{i\overline{z_0}x},
 \qquad
 \|K_{L,z_0}\|_2^2=\frac{\sinh(|a|L)}{|a|}.
 \tag{31}
\]

For the truncated full kernel,

\[
 \langle P_Lk,K_{L,z_0}\rangle
 =\widehat{P_Lk}(z_0)\longrightarrow\Xi(z_0)=0.
 \tag{32}
\]

Hence the normalized evaluation direction becomes exponentially
orthogonal to the model.  This is exactly the geometry by which an
off-line negative sector can coexist with the near-radical model branch.

There is also no one-dimensional-radical theorem available for free.  The
even functions \(\partial_x^{2m}k\) are admissible and satisfy

\[
 \widehat{\partial_x^{2m}k}(z)=(-1)^mz^{2m}\Xi(z),
 \qquad QW(\partial_x^{2m}k,g)=0.
 \tag{33}
\]

Consequently the full Weil radical, whenever represented on this natural
domain, contains infinitely many even directions.  The finite least-state
selection has to be proved; radicality alone cannot select \(k\).

## 6. Sharp abstract countermodel

The quotient by the gap in (25) cannot be removed by abstract spectral
theory.

Let \(\mathcal H=L^2([-1,1])^{\rm even}\).  Choose the normalized functions

\[
 \phi(x)=2^{-1/2},
 \qquad
 k(x)=c(1-|x|),
 \tag{34}
\]

where \(c\) normalizes \(k\).  Their Fourier transforms are nonzero scalar
multiples of

\[
 \widehat\phi(z)=\frac{\sin z}{z},
 \qquad
 \widehat k(z)=\left(\frac{\sin(z/2)}{z/2}\right)^2.
 \tag{35}
\]

Both are even entire functions of exponential type and have only real
zeros, but

\[
 \partial_z^2\log(\widehat\phi/\widehat k)\not\equiv0.
 \tag{36}
\]

Let

\[
 e_1=\frac{k-\langle\phi,k\rangle\phi}
 {\|k-\langle\phi,k\rangle\phi\|}
 \tag{37}
\]

and complete \(\{\phi,e_1\}\) to an orthonormal basis
\(\{\phi,e_1,e_2,\ldots\}\).  For any sequence \(\delta_L\downarrow0\),
define a self-adjoint compact-resolvent operator by

\[
 A_L\phi=0,
 \qquad A_Le_1=\delta_Le_1,
 \qquad A_Le_j=j e_j\quad(j\ge2).
 \tag{38}
\]

Then:

- \(\phi\) is the simple even ground state;
- the resolvent is compact;
- \(k\) is an increasingly accurate quasimode:

  \[
   \|(A_L-\langle A_Lk,k\rangle)k\|\longrightarrow0,
   \qquad
   R_L-\epsilon_{0,L}\longrightarrow0;
 \tag{39}
  \]

- nevertheless, the distance from \(k\) to the ground line is a fixed
  positive number, and the curvature difference (36) does not tend to
  zero.

Indeed,

\[
 \frac{R_L-\epsilon_{0,L}}{g_L}
 =|\langle k,e_1\rangle|^2,
 \tag{40}
\]

which is independent of \(L\).  The small Rayleigh excess is exactly
cancelled by the collapsing gap.

This model does not reproduce the arithmetic Weil kernel and therefore is
not a counterexample to the desired arithmetic theorem.  Its precise role
is to rule out every derivation of (1) that uses only compact resolvent,
simple-even ground structure, real-rootedness, and vanishing unscaled
quasimode error.

## 7. Binding conclusion

The global target has the following exact status.

\[
\begin{array}{c}
 \partial_z^2\log(\widehat\phi_L/\widehat k_L)\to0
 \\
 \Updownarrow\quad\text{(even sector, scalar normalization)}
 \\
 \widehat\phi_L/\widehat k_L\to1
 \quad\text{on common zero-free domains},
\end{array}
\tag{41}
\]

and its contour values force convergence of zero divisors.  Since
\(\widehat k_L\to\Xi\) and the ground transforms are real-rooted, (1)
implies RH.

The remaining admissible proof must therefore use a quantitative property
specific to the ordinary-prime Weil operator.  In variational coordinates,
one sufficient form is (25); in divisor coordinates, it is convergence of
the second Cauchy transforms (17).  Qualitative compactness, interlacing,
Pick/Herglotz structure, or an unscaled small residual cannot supply that
identification.

## Status

Proved here:

- affine rigidity of logarithmic curvature;
- equivalence with normalized transform convergence in the even sector;
- the contour formula counting the relative zero divisor;
- the direct implication of the curvature target to RH;
- the sharp Rayleigh-excess/gap sufficient condition;
- the exact Weil-radical residual identity and its ground/orthogonality
  bifurcation;
- an abstract compact-resolvent countermodel showing that the gap quotient
  cannot be omitted.

Not proved here:

- the arithmetic estimate (25), or an equivalent direct second-Cauchy
  transform estimate for the actual ordinary-prime Weil ground states.
