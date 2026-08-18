# 106.126 — Local Paley--Wiener observability and the spatial-escape gate

## 1. Purpose and verdict

Document 106.123 proves that every normalized subthreshold eigenstate of
the complete ordinary-prime--Gamma operator has a uniform local second
logarithmic Fourier moment.  The remaining compactness question is spatial:
can the exact mean-periodic equation

\[
 F*K=0,
 \qquad F=hq,
 \tag{1}
\]

prevent a normalized even state from escaping simultaneously to the two
tails?

This note gives a definitive answer at the level of mean periodicity and
local regularity.

1. On every bounded symmetric open set, the elementary modes and
   multiplicity jets at the complete zero divisor of \(\Xi\) are dense in
   the local second-logarithmic Sobolev topology.  The proof is a
   Paley--Wiener zero-counting argument: an annihilator would have \(O(T)\)
   zeros, whereas the \(\Xi\) divisor, counted with multiplicity, has
   \(\asymp T\log T\) zeros.
2. Consequently there is no bounded-window unique-continuation or
   central-observability inequality for (1).  Exact mean-periodic
   exponential polynomials can be arbitrarily small on a central window
   while approximating an arbitrary profile on a disjoint window.
3. More strongly, there is a sequence of normalized, real-even, exact
   mean-periodic graph-domain vectors whose mass escapes bilaterally and
   whose localized second-logarithmic norms tend to zero on every fixed
   compact set.
4. This sequence is not asserted to be a Weyl sequence for the physical
   operator.  Its global prime--Gamma graph norms need not be bounded.
   Upgrading it to

   \[
     \|(A-\tfrac12)q_j\|\longrightarrow0
     \tag{2}
   \]

   is exactly the unresolved threshold form-synthesis problem.  Thus the
   physical eigen-equation, not mean periodicity or local ellipticity,
   must supply any proof of uniform spatial tightness.

The conclusion is sharp.  The ultraviolet escape of 106.120 is removed
for actual eigenstates by 106.123, but the proposed replacement by an
\(\Xi\)-specific local observability theorem is false.

## 2. Semantic audit

This route was checked against the earlier Paley--Wiener and synthesis
work before being developed.

* Phase 15 studies the archimedean multiplier and the arithmetic Hodge
  sign.  Its spectral support is in the Fourier coordinate of the physical
  test, not in the mean-periodic divisor coordinate used below.
* 106.11 constructs compact Paley--Wiener tests which isolate a prescribed
  off-line orbit.  It does not study completeness of the full \(\Xi\)
  divisor on bounded spatial windows.
* 106.30 proves that quantitative cyclic approximation of off-line
  evaluations has the wrong radius-dependent conditioning.
* 106.43 proves the exact equation (1) and identifies its elementary zero
  modes.
* 106.69 shows that the vertical half-shift identity for
  \(\widehat{K/h}\) does not control the horizontal Toeplitz--Hankel Gram
  matrix.
* 106.70 proves compact-open mean-periodic synthesis but separates it from
  weighted \(L^2\), form and graph synthesis.  Nonzero translations are
  unbounded in the physical weighted space.
* 106.121 proves that complete radical projection preserves upper
  logarithmic compactness but supplies no lower frame.
* 106.123 gains the second logarithmic moment for actual eigenstates and
  isolates spatial threshold tightness as the remaining compactness issue.

The new statement is the local universality theorem in Section 4 and its
normalized bilateral escape consequence in Section 6.  It strengthens
compact-open synthesis locally, but it does not cross the global weighted
form gate of 106.70.

## 3. Local second-logarithmic space and elementary modes

Put

\[
 \ell(\xi)=1+\log^2(2+|\xi|)
 \tag{3}
\]

and let \(\mathsf H_{\log^2}(\mathbb R)\) be the Hilbert space with norm

\[
 \|f\|_{\mathsf H_{\log^2}}^2
 =\int_{\mathbb R}\ell(\xi)|\widehat f(\xi)|^2\,d\xi.
 \tag{4}
\]

For a bounded open set \(U\), the restriction space
\(\mathsf H_{\log^2}(U)\) is equipped with the quotient norm over all
global extensions.  Multiplication by a compactly supported smooth
function is bounded on this space.  This follows from

\[
 \log(2+|\xi|)
 \leq \log(2+|\eta|)+\log(2+|\xi-\eta|)
 \tag{5}
\]

and convolution with a Schwartz Fourier transform.

Let \(\mathcal Z_\Xi\) be the complete zero divisor of

\[
 \Xi(z)=\xi(\tfrac12+iz).
 \tag{6}
\]

If \(z\) has multiplicity \(m_z\), put

\[
 E_{z,k}(x)=\partial_z^k\cos(zx),
 \qquad 0\leq k<m_z.
 \tag{7}
\]

Let \(\mathcal E_\Xi\) be their algebraic span, with conjugate and
\(z\mapsto-z\) orbits combined so that real-even functions form the real
subspace \(\mathcal E_\Xi^{\mathbb R}\).  Every element of
\(\mathcal E_\Xi\) satisfies

\[
 E*K=0.
 \tag{8}
\]

The multiplicity jets in (7) are essential.  They allow the argument to
use the Riemann--von Mangoldt count with multiplicity and require no
simplicity assumption.  A pure-cosine statement would require a separate
lower bound for the number of distinct zeros.

## 4. Local universality of the complete \(\Xi\) divisor

### Theorem 1 — Second-logarithmic local density

For every bounded symmetric open set \(U\subset\mathbb R\),

\[
 \boxed{
 \overline{\mathcal E_\Xi^{\mathbb R}|_U}
 ^{\,\mathsf H_{\log^2}(U)}
 =\mathsf H_{\log^2}(U)_{\rm even}^{\mathbb R}.}
 \tag{9}
\]

The complex version holds without taking real orbit combinations.

#### Proof

Suppose that the complex closure in (9) were proper.  Hahn--Banach would
give a nonzero continuous functional \(u\) on
\(\mathsf H_{\log^2}(U)\) annihilating every restricted mode (7).  By the
duality of restriction spaces, \(u\) is a distribution supported in
\(\overline U\).  Every compactly supported distribution has finite
order, so its Fourier--Laplace transform

\[
 A(z)=\langle u,e^{-izx}\rangle
 \tag{10}
\]

is entire and satisfies, for some \(R,N,C<\infty\),

\[
 |A(z)|\leq C(1+|z|)^N e^{R|\operatorname {Im}z|}.
 \tag{11}
\]

Annihilation of (7), together with the conjugation and reflection
symmetries of the divisor, says that \(A\) vanishes at every zero of
\(\Xi\) with at least the same multiplicity.  Pairing with
\(\partial_z^k e^{izx}\) gives the corresponding derivative of \(A\);
passing between exponentials and cosines is legitimate on the even
subspace.

If \(A\not\equiv0\), Jensen's formula, centered at a point where \(A\) is
nonzero, and (11) give

\[
 n_A(r)=O(r+\log r),
 \tag{12}
\]

with multiplicity.  On the other hand, Riemann--von Mangoldt in the
coordinate (6) gives

\[
 n_\Xi(r)
 =\frac r\pi\log\frac r{2\pi e}+O(\log r).
 \tag{13}
\]

Equations (12)--(13) are incompatible with divisibility by the complete
\(\Xi\) divisor.  Hence \(A\equiv0\).  Fourier injectivity for compactly
supported distributions gives \(u=0\), a contradiction.  This proves
complex density.  Conjugation invariance of the space and divisor gives
the real-even statement by taking real orbit combinations. \(\square\)

The proof uses only the zero count, functional-equation symmetries and the
exact convolution equation.  It does not assume that any zero is on the
critical line.

## 5. Exact failure of bounded-window observability

Let \(I,J\) be disjoint bounded symmetric open sets, and let
\(0\ne\phi\in C_c^\infty(J)\) be real and even.  Apply Theorem 1 on
\(U=I\cup J\) to the function which is zero on \(I\) and equal to
\(\phi\) on \(J\).  There are \(E_\nu\in\mathcal E_\Xi^{\mathbb R}\)
such that

\[
 \|E_\nu\|_{\mathsf H_{\log^2}(I)}\longrightarrow0,
 \qquad
 \|E_\nu-\phi\|_{\mathsf H_{\log^2}(J)}
 \longrightarrow0.
 \tag{14}
\]

### Corollary 2 — No local unique-continuation constant

There is no finite \(C=C(I,J)\) for which

\[
 \|E\|_{L^2(J)}
 \leq C\|E\|_{\mathsf H_{\log^2}(I)}
 \tag{15}
\]

holds for every \(E\in\mathcal E_\Xi^{\mathbb R}\).  The same conclusion
holds if the left side is measured with any smooth positive weight on
\(J\).

#### Proof

For the sequence (14), the left side of (15) tends to
\(\|\phi\|_{L^2(J)}>0\), while the right side tends to zero.  Smooth
positive weights are equivalent to Lebesgue measure on the fixed bounded
set \(J\). \(\square\)

Thus the overabundance of \(\Xi\) frequencies has the opposite effect from
the proposed central observability: on every bounded set, exact
mean-periodic modes are locally universal.

## 6. A normalized bilateral spatial-escape sequence

Recall the unitary coordinate change

\[
 q=F/h,
 \qquad
 \|q\|_{L^2(\mu_K)}=\|F\|_{L^2(\omega_K)},
 \qquad
 d\omega_K=\frac{K}{c_Kh}\,dx.
 \tag{16}
\]

Choose \(R_j\uparrow\infty\), put

\[
 I_j=(-R_j,R_j),
 \qquad
 J_j=(R_j+1,R_j+2)\cup(-R_j-2,-R_j-1),
 \tag{17}
\]

and choose a real-even \(\phi_j\in C_c^\infty(J_j)\) normalized by

\[
 \|\phi_j\|_{L^2(\omega_K;J_j)}=1.
 \tag{18}
\]

On the bounded set \(I_j\cup J_j\), the physical weight is smooth and
strictly positive.  Theorem 1 permits a choice
\(E_j\in\mathcal E_\Xi^{\mathbb R}\) such that

\[
 \|E_j\|_{\mathsf H_{\log^2}(I_j)}\leq\varepsilon_j,
 \qquad
 \|E_j-\phi_j\|_{L^2(\omega_K;J_j)}\leq\frac14,
 \tag{19}
\]

where \(\varepsilon_j>0\) may be chosen arbitrarily small.  In particular,

\[
 \|E_j\|_{L^2(\omega_K)}
 \geq\|E_j\|_{L^2(\omega_K;J_j)}\geq\frac34.
 \tag{20}
\]

Define

\[
 q_j=\frac{E_j/h}{\|E_j\|_{L^2(\omega_K)}}.
 \tag{21}
\]

By choosing \(\varepsilon_j\) smaller than the finitely many
norm-equivalence constants in (19), one obtains:

### Theorem 3 — Mean-periodic bilateral escape with local log regularity

There is a sequence \((q_j)\) such that

\[
 \boxed{
 \begin{aligned}
 &q_j\in(\mathbf1\oplus\mathcal R)^\perp\cap D(A),
 \qquad q_j\text{ real and even},
 \qquad \|q_j\|_{L^2(\mu_K)}=1,\\
 &(hq_j)*K=0,\\
 &\|q_j\|_{L^2(\mu_K;[-R_j,R_j])}\longrightarrow0,\\
 &\int\log^2(2+|\xi|)
       |\widehat{\chi q_j}(\xi)|^2\,d\xi
       \longrightarrow0
       \quad\text{for every }\chi\in C_c^\infty(\mathbb R).
 \end{aligned}}
 \tag{22}
\]

Consequently

\[
 \int_{R_j}^{\infty}|q_j|^2\,d\mu_K
 \longrightarrow\frac12,
 \qquad
 \int_{-\infty}^{-R_j}|q_j|^2\,d\mu_K
 \longrightarrow\frac12.
 \tag{23}
\]

#### Proof

The first assertions in (22) follow from (8), the exact equivalence of
106.43 and graph-domain membership of every finite elementary mode in
106.70.  Equations (19)--(21), local equivalence of the measures, and the
lower bound (20) give the central \(L^2\) limit after choosing
\(\varepsilon_j\downarrow0\) sufficiently fast.

For fixed \(\chi\), one has \(\operatorname {supp}\chi\subset I_j\) for
all large \(j\).  Multiplication by \(\chi/h\) is bounded in the local
space (4), so (19)--(21) give the last limit in (22).  Finally, both
\(q_j\) and \(\mu_K\) are even.  The two tails therefore have equal mass;
normalization and central escape give (23). \(\square\)

This is stronger than a translated-bump heuristic: every vector obeys the
exact Riemann mean-periodic equation and lies in the physical graph domain.
It also shows that the local estimate proved for eigenstates in 106.123 is
fully compatible with bilateral spatial escape.

## 7. Why this is not a physical Weyl sequence

The construction controls the restriction of \(q_j\) to every fixed
compact set.  It does not control

\[
 \|Aq_j\|,
 \qquad
 \mathscr E_K(q_j),
 \qquad
 \|(A-\tfrac12)q_j\|.
 \tag{24}
\]

The finite zero blocks needed for local approximation may have rapidly
growing frequencies and conditioning constants.  Gamma energy charges
those frequencies, while the prime form contains every literal
translation \(\log p^k\).  None of these global costs is visible in the
bounded-window density proof.

Accordingly, calling (22) a Weyl sequence would be incorrect.  The upgrade

\[
 \boxed{
 \text{(22)}\quad+\quad
 \|(A-\tfrac12)q_j\|\to0}
 \tag{25}
\]

is precisely the weighted graph/form synthesis and threshold-resonance
problem separated in 106.70 and 106.123.  It would imply
\(1/2\in\sigma_{\rm ess}(A|_{(1\oplus\mathcal R)^\perp})\).
Conversely, Weyl's criterion and the local compactness of 106.47 would
produce a spatially escaping sequence satisfying (25) if that threshold
belongs to the essential spectrum.  The existing theorem proves only that
the essential spectrum has no point below \(1/2\).

## 8. What the actual eigen-equation would have to add

Let

\[
 \mathcal B
 =\{q:Aq=\alpha q,\ 0<\alpha<1/2,\ \|q\|=1,\
       q\perp\mathbf1\oplus\mathcal R\}.
 \tag{26}
\]

Fixed-gap finite rank from 106.47 and local second-log compactness from
106.123 imply the following exact alternative.

### Proposition 4 — Eigenstate observability alternative

The following statements are equivalent.

1. There are \(R<\infty\) and \(c_R>0\) such that

   \[
    \|\chi_Rq\|_{L^2(\mu_K)}\geq c_R
    \qquad(q\in\mathcal B).
    \tag{27}
   \]

2. No sequence \(q_j\in\mathcal B\) has

   \[
    \alpha_j\uparrow\frac12,
    \qquad
    q_j\longrightarrow0\text{ in }L^2_{\rm loc}.
    \tag{28}
   \]

#### Proof

Failure of (27) for every \(R\), followed by a diagonal choice, gives a
normalized sequence converging locally to zero.  If a subsequence of its
eigenvalues stayed below \(1/2-\delta\), it would lie in the finite-rank
spectral space
\(\operatorname {Ran}\mathbf1_{(0,1/2-\delta]}(A)\), whose unit sphere is
compact and cannot converge locally to zero.  Thus (28) follows.  The
converse is immediate. \(\square\)

Theorem 3 shows that neither mean periodicity nor the local estimate of
106.123 can prove (27).  The only unused hypothesis in Proposition 4 is
the full global eigen-equation with the literal prime--Gamma operator.

One sufficient, stronger statement would be the threshold resolvent
estimate

\[
 \boxed{
 \|q\|_{L^2(\mu_K)}
 \leq C\bigl(\|(A-\tfrac12)q\|_{L^2(\mu_K)}
             +\|\chi_Rq\|_{L^2(\mu_K)}\bigr),
 \quad
 q\in(\mathbf1\oplus\mathcal R)^\perp\cap D(A).}
 \tag{29}
\]

Estimate (29) would exclude every threshold Weyl sequence.  A weaker
version only on \(\mathcal B\) would already prove (27).  Neither estimate
can follow from the divisor alone by Corollary 2 and Theorem 3.

Thus the surviving physical surplus is localized more sharply: it is a
global threshold-resolvent or eigenstate-observability estimate for the
complete literal prime--Gamma operator after exact radical anti-shorting.
Local Paley--Wiener uniqueness, local ellipticity and mean periodicity have
now been exhausted.
