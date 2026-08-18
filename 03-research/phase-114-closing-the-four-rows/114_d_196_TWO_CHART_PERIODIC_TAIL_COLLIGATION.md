# D.196 — Two-chart periodic-tail colligation and its boundary inertia

## Verdict

The exact two-chart conservative dilation of a prime Poisson operator can be
constructed, but its boundary variables are not the two scalar Tate jets.
For \(a=\log p\), they are two entire periodic modules

\[
 \mathcal B_p^+=L^2(C_p),\qquad
 \mathcal B_p^-=L^2(C_p),qquad C_p=\mathbb R/a\mathbb Z.  \tag{0.1}
\]

The scalar moments \(M_+,M_-\) are one functional on each module.  A
primitive test can therefore have both moments zero while carrying nonzero
incoming and outgoing Poisson tails.

At the positive Markov level, the fiber covariance \(r^{|i-j|}\) has a
nearest-neighbour precision and an exact two-boundary Schur complement with
positive feedthrough

\[
 d_rI_2,qquad d_r={r^2\over(1-r)^2}>0.                    \tag{0.2}
\]

At the arithmetic-character level, however,

\[
 P_r(z)-1={1\over1-rz}+{1\over1-rz^{-1}}-2              \tag{0.3}
\]

has critical pole residues of opposite signs.  The two-chart residue form
has inertia \((\infty,\infty)\) on
\(\mathcal B_p^+\oplus\mathcal B_p^-\), and still has that inertia after
removing the two scalar moments.

Adding the positive Gamma jump channel yields exactly the adelic energy
\(\mathcal E_P\) of D.195.  Conservation with sharp constant one after
primitive shorting is

\[
 \mathcal E_P\ge A_PI,                                    \tag{0.4}
\]

not an automatic consequence of the local colligations.  Thus the
two-chart construction is complete and source-defined, but the scalar
primitive quotient is too small to turn its boundary form positive.  No
paper file is modified.

## 1. Zak decomposition at one prime

Fix \(p\), set

\[
 a=\log p,qquad r=p^{-1/2},qquad c={1+r\over1-r}.         \tag{1.1}
\]

The Zak decomposition is the unitary

\[
 \mathcal Z_p:L^2(\mathbb R)\xrightarrow\sim
 L^2([0,a),du;\ell^2(\mathbb Z)),
 \qquad (\mathcal Z_pF)_u(j)=F(u+ja).                     \tag{1.2}
\]

Translation by \(a\) becomes the bilateral shift in \(j\).  The normalized
Poisson Markov operator of D.195 acts fiberwise by

\[
 (K_rf)_j={1\over c}\sum_{\ell\in\mathbb Z}
 r^{|j-\ell|}f_\ell.                                      \tag{1.3}
\]

For a finitely supported fiber sequence define its two boundary transforms

\[
 b_+(f)=\sum_{\ell\in\mathbb Z}r^{-\ell}f_\ell,qquad
 b_-(f)=\sum_{\ell\in\mathbb Z}r^{\ell}f_\ell.             \tag{1.4}
\]

As \(u\) varies, these are functions on \([0,a)\), hence elements of the
two modules (0.1).

## 2. Exact tails

If \(f_\ell=0\) outside \(L\le\ell\le R\), then (1.3) gives exactly

\[
 (K_rf)_j=
 \begin{cases}
 c^{-1}r^j b_+(f),&j>R,\\
 c^{-1}r^{-j}b_-(f),&j<L.
 \end{cases}                                               \tag{2.1}
\]

Thus no information beyond \(b_+\) and \(b_-\) is needed to reconstruct
both infinite tails.  Conversely, arbitrary boundary functions occur by
taking \(f\) supported at \(j=0\).  Hence (0.1) is the minimal exact
two-chart tail space.

The two Tate moments are

\[
 \begin{aligned}
 M_+(F)&=\int_0^a e^{u/2}b_+(f_u)\,du,\\
 M_-(F)&=\int_0^a e^{-u/2}b_-(f_u)\,du.
 \end{aligned}                                             \tag{2.2}
\]

Indeed \(e^{ja/2}=r^{-j}\) and \(e^{-ja/2}=r^j\).  Formula (2.2) proves
that the scalar jets are quotient functionals of the periodic tail modules,
not the modules themselves.

Choose a nonzero \(h\in L^2([0,a))\) orthogonal to both
\(e^{u/2}\) and \(e^{-u/2}\), and put \(f_u(0)=h(u)\), \(f_u(j)=0\) for
\(j\ne0\).  Then

\[
 M_+(F)=M_-(F)=0,qquad b_+(f_u)=b_-(f_u)=h(u)\ne0.        \tag{2.3}
\]

This is an explicit infinite-dimensional strengthening of the rank
argument in D.190.

## 3. Positive Markov colligation and Schur complement

On a finite integer interval \(J_N=\{-N,\ldots,N\}\), let

\[
 (G_N)_{ij}={r^{|i-j|}\over c}.                            \tag{3.1}
\]

This is the compression of the full Markov covariance.  Direct multiplication
gives

\[
 G_N^{-1}={c\over1-r^2}
 \begin{pmatrix}
 1&-r&&&\\
 -r&1+r^2&-r&&\\
 &\ddots&\ddots&\ddots&\\
 &&-r&1+r^2&-r\\
 &&&-r&1
 \end{pmatrix}.                                           \tag{3.2}
\]

The compression of the full-line precision is

\[
 Q_N={c\over1-r^2}
 \begin{pmatrix}
 1+r^2&-r&&&\\
 -r&1+r^2&-r&&\\
 &\ddots&\ddots&\ddots&\\
 &&-r&1+r^2&-r\\
 &&&-r&1+r^2
 \end{pmatrix}.                                           \tag{3.3}
\]

Therefore

\[
 \boxed{Q_N-G_N^{-1}
 =d_r\bigl(|-N\rangle\langle-N|+|N\rangle\langle N|\bigr),
 \quad d_r={cr^2\over1-r^2}={r^2\over(1-r)^2}.}           \tag{3.4}
\]

Equation (3.2) is precisely the Schur complement of the two exterior
half-lines in the full precision (3.3).  Formula (3.4) is its positive
boundary feedthrough.  Fiberwise over \(u\), it gives the conservative
Gaussian/Markov colligation with boundary space
\(\mathcal B_p^+\oplus\mathcal B_p^-\).

This is a real success: support and all geometric tails are retained with
sharp constant one at the **positive covariance** level.

## 4. The arithmetic Laurent realization and its inertia

The unnormalized Poisson symbol is

\[
 P_r(z)=\sum_{k\in\mathbb Z}r^{|k|}z^k
 ={1-r^2\over(1-rz)(1-rz^{-1})}.                           \tag{4.1}
\]

Equivalently,

\[
 P_r(z)=\frac1{1-rz}+\frac1{1-rz^{-1}}-1,                 \tag{4.2}
\]

which proves (0.3).  The critical Tate evaluations are the two poles
\(z=r^{-1}\) and \(z=r\).  Their residues are

\[
 \operatorname {Res}_{z=r^{-1}}P_r(z)=-r^{-1},
 \qquad
 \operatorname {Res}_{z=r}P_r(z)=r.                       \tag{4.3}
\]

Thus the natural residue/feedthrough form on the two chart variables is,
up to a common positive normalization,

\[
 J_{p,\partial}=
 \begin{pmatrix}r&0\\0&-r^{-1}\end{pmatrix}.             \tag{4.4}
\]

It has one positive and one negative direction in every periodic fiber.
After tensoring with \(L^2(C_p)\),

\[
 \operatorname {inertia}(J_{p,\partial})=(\infty,\infty). \tag{4.5}
\]

Imposing (2.2) removes at most one dimension from each chart.  The
orthogonal complements of the two exponential functions remain
infinite-dimensional, so the primitive boundary form still has inertia
\((\infty,\infty)\).

This reconciles the two local pictures:

* the covariance/precision colligation (3.4) is positive;
* subtracting the diagonal to form the arithmetic character \(P_r-I\)
  exposes the hyperbolic two-chart residue (4.4).

The former proves complete positivity; the latter is the signed relative
trace that must be compared with Gamma.

## 5. Unitary state-space chart

For completeness, each one-sided chart is generated by the scalar unitary
colligation

\[
 \mathcal U_r=
 \begin{pmatrix}
 r&\sqrt{1-r^2}\\
 \sqrt{1-r^2}&-r
 \end{pmatrix},
 \qquad \mathcal U_r^*\mathcal U_r=I.                     \tag{5.1}
\]

Its transfer function is the Blaschke factor

\[
 \Theta_r(z)={z-r\over1-rz}.                              \tag{5.2}
\]

The observability vector of (5.1) is
\(\sqrt{1-r^2}(I-rU)^{-1}\), whose Gramian is (4.1) on the unit circle.
Pairing (5.1) with its reflected chart gives the conservative realization
of Sections 3--4.  The state colligations are Hilbert unitary; the arithmetic
residue pairing between their critical poles is Krein with signature (4.5).

Thus local unitarity does not imply positivity of the paired arithmetic
feedthrough.

## 6. Coupling the Gamma channel

The complete Gamma energy is the positive jump form

\[
 L_\infty=\int_0^\infty
 {e^{-r/2}\over1-e^{-2r}}
 (I-S_r)^*(I-S_r)\,dr\ge0.                                \tag{6.1}
\]

It has its own zero-extension/exterior boundary colligation, also positive.
Adding it to the positive prime precisions gives exactly

\[
 \mathcal E_P=L_\infty
 +\sum_{p\in P}\log p\,c_p(I-M_p)\ge0.                   \tag{6.2}
\]

The full arithmetic form remains

\[
 B_P=A_PI-\mathcal E_P,qquad
 A_P=m_0+\sum_{p\in P}\log p(c_p-1).                       \tag{6.3}
\]

Hence an adelic conservative colligation with the desired constant one on
the primitive source exists exactly when

\[
 \mathcal E_P-A_PI\ge0
 \quad\text{on }\ker M_+\cap\ker M_-.                     \tag{6.4}
\]

The positive local feedthroughs (3.4) and (6.1) prove that the left side of
(6.2) is a Dirichlet energy.  They do not prove the lower bound by the load
\(A_P\).  Shorting only the two scalar jets leaves the infinite boundary
modules of (2.3), so the local conservation laws cannot collapse (6.4) to a
two-dimensional calculation.

Equation (6.4) is the exact unit annular shorted-capacity theorem isolated
in D.169--D.190.  Its truth is row D.

## 7. Consequence and next admissible move

The requested two-chart dilation has now been built and fully typed:

\[
 \text{bulk }L^2(\mathbb R)
 \longrightarrow
 \text{bulk}\oplus L^2(C_p)^+\oplus L^2(C_p)^-.           \tag{7.1}
\]

It preserves all tails, prime powers, and the exact Tate quotient maps.
What fails is not existence of a conservative local colligation.  It is the
claim that the two scalar jets exhaust its boundary state.

A further construction must therefore glue the **full periodic boundary
modules** across primes and Gamma before taking the two scalar Tate
quotient.  The only possible gain over (6.4) would come from orthogonality or
cancellation between these full modules imposed by the A periodic Kunneth
category.  Treating them as an orthogonal direct sum leaves the inertia
(4.5) unchanged and cannot close D.

## 8. Reproducible certificate

The script `114_d_196_two_chart_periodic_tail_verify.py` checks:

1. the exact two tail formulas (2.1);
2. primitive scalar moments with nonzero periodic tail functions;
3. the inverse covariance and feedthrough (3.2)--(3.4);
4. the opposite Laurent residues (4.3);
5. persistence of positive and negative boundary directions after removing
   two scalar moment vectors.
