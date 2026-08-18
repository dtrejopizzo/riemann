# 106.194 — Finite root-graph torsion and the von Mangoldt coefficient

## 1. Purpose

The preceding operator constructions reproduce the prime coefficient as
a covariance or a Green kernel.  This note gives a different, genuinely
finite geometric realization.  On the cyclic graph of roots of order
\(N\), the reduced Laplacian is positive and its pseudodeterminant is
\(N^2\).  Passing through one layer

\[
 mp^{k-1}\longrightarrow mp^k                              \tag{1}
\]

therefore has logarithmic torsion \(\log p\), while the normalized
intersection of the embedded old root stratum with the new generic state
is \(p^{-k/2}\).  Their product is exactly

\[
 \frac{\Lambda(p^k)}{p^{k/2}}.                             \tag{2}
\]

This constructs the finite-place coefficient from a positive root graph
and a relative determinant, without invoking the explicit formula or any
zero.

## 2. The cyclic root Laplacian

For \(N\ge2\), let

\[
 R_N=\mathbb Z/N\mathbb Z                                  \tag{3}
\]

and let \(T_N\) be translation by one on \(\ell^2(R_N)\).  Define

\[
 \Delta_N=2I-T_N-T_N^*.                                    \tag{4}
\]

Its quadratic form is

\[
 \langle f,\Delta_Nf\rangle
 =\sum_{j\in R_N}|f(j+1)-f(j)|^2\ge0,                     \tag{5}
\]

with kernel the constants.  Write \(\det'\Delta_N\) for the product of
its nonzero eigenvalues.

### Theorem 2.1 — Exact root-graph determinant

\[
 \boxed{\det'\Delta_N=N^2.}                                \tag{6}
\]

#### Proof

The Fourier characters of \(R_N\) diagonalize (4), with eigenvalues

\[
 \lambda_j
 =2-e^{2\pi ij/N}-e^{-2\pi ij/N}
 =|1-e^{2\pi ij/N}|^2,qquad 0\le j<N.                    \tag{7}
\]

The eigenvalue at \(j=0\) is zero.  Since

\[
 \prod_{j=1}^{N-1}(1-e^{2\pi ij/N})=N,                    \tag{8}
\]

taking the squared modulus proves (6). \(\square\)

## 3. Relative torsion of one prime layer

Fix \(m\ge2\), a prime \(p\), and \(k\ge1\).  Define the half-logarithmic
relative torsion

\[
 \mathcal T_{m,p,k}
 =\frac12\log
   \frac{\det'\Delta_{mp^k}}
        {\det'\Delta_{mp^{k-1}}}.                          \tag{9}
\]

### Theorem 3.1 — Every prime-power layer has torsion \(\log p\)

\[
 \boxed{\mathcal T_{m,p,k}=\log p.}                        \tag{10}
\]

#### Proof

Substitution of (6) in (9) gives

\[
 \mathcal T_{m,p,k}
 =\frac12\log\frac{m^2p^{2k}}{m^2p^{2k-2}}
 =\log p.                                                   \tag{11}
\]

The result is independent of the auxiliary level \(m\). \(\square\)

The use of the one-step ratio in (9) is essential: the full ratio from
\(m\) to \(mp^k\) is \(k\log p\), whereas the von Mangoldt weight of
each individual layer \(p^k\) is \(\log p\).

## 4. The midpoint intersection coefficient

Inside \(R_{mp^k}\), let

\[
 H_{m,k}=p^kR_m
 =\{0,p^k,2p^k,\ldots,(m-1)p^k\}.                         \tag{12}
\]

Let

\[
 \omega_{mp^k}=(mp^k)^{-1/2}\mathbf1_{R_{mp^k}},
 \qquad
 \eta_{m,k}=m^{-1/2}\mathbf1_{H_{m,k}}.                   \tag{13}
\]

Both are unit vectors.

### Theorem 4.1 — Exact root-stratum overlap

\[
 \boxed{
 \langle\omega_{mp^k},\eta_{m,k}\rangle=p^{-k/2}.}         \tag{14}
\]

#### Proof

The subgroup (12) has exactly \(m\) elements.  Therefore

\[
 \langle\omega_{mp^k},\eta_{m,k}\rangle
 =\frac{m}{\sqrt{mp^k}\sqrt m}=p^{-k/2}.                  \tag{15}
\]

\(\square\)

This is the finite-root version of the index coefficient
\(\langle\Omega,V_{p^k}\Omega\rangle=p^{-k/2}\) in 106.164.

## 5. Exact geometric von Mangoldt identity

Combining Theorems 3.1 and 4.1 gives

\[
 \boxed{
 \mathcal T_{m,p,k}
 \langle\omega_{mp^k},\eta_{m,k}\rangle
 =\frac{\log p}{p^{k/2}}
 =\frac{\Lambda(p^k)}{\sqrt{p^k}}.}                        \tag{16}
\]

Thus for every compactly supported logarithmic test \(c\),

\[
 \sum_{p,k\ge1}
 c(k\log p)\,
 \mathcal T_{m,p,k}
 \langle\omega_{mp^k},\eta_{m,k}\rangle
 =\sum_{p,k\ge1}\frac{\log p}{p^{k/2}}c(k\log p).        \tag{17}
\]

The right side is exactly the ordinary finite-place distribution in the
Weil formula.  Equation (17) has been obtained from:

1. positivity of a finite graph Laplacian;
2. relative determinant torsion between consecutive root levels;
3. normalized intersection of a closed root stratum with the generic
   root state.

## 6. Polarization at finite level

Let

\[
 H_N^0=\mathbf1^perp\subset\ell^2(R_N).                   \tag{18}
\]

On the real double \(H_N^0\oplus H_N^0\), define

\[
 J_N(x,y)=(-y,x),
 \qquad
 g_N((x,y),(u,v))
 =\langle\Delta_Nx,u\rangle+\langle\Delta_Ny,v\rangle.   \tag{19}
\]

Then \(g_N\) is positive definite and

\[
 \Omega_N(z,w)=-g_N(z,J_Nw)                                \tag{20}
\]

is alternating and nondegenerate.  Hence every finite root level carries
a canonical positive degree-one polarization, and its determinant-line
increment supplies the exact arithmetic mass (10).

### Theorem 6.1 — Functoriality under root coverings

Let (M\mid N), put (q=N/M), and let

\[
 \pi_{N,M}:R_N\longrightarrow R_M,
 \qquad y\longmapsto y\pmod M.                            \tag{21}
\]

The normalized pullback

\[
 P_{M,N}:\ell^2(R_M)\longrightarrow\ell^2(R_N),
 \qquad
 (P_{M,N}f)(y)=q^{-1/2}f(\pi_{N,M}(y))                    \tag{22}
\]

is an isometry and satisfies

\[
 P_{N,L}P_{M,N}=P_{M,L},
 \qquad
 \Delta_NP_{M,N}=P_{M,N}\Delta_M                         \tag{23}
\]

whenever (M\mid N\mid L).  It maps normalized constants to normalized
constants and therefore restricts to an isometric polarized embedding

\[
 P_{M,N}^{(1)}=P_{M,N}\oplus P_{M,N}:
 (H_M^0\oplus H_M^0,g_M,J_M)\hookrightarrow
 (H_N^0\oplus H_N^0,g_N,J_N).                            \tag{24}
\]

Moreover, (P_{M,N}H_M^0) is reducing for \(\Delta_N\), and the
determinant of the orthogonal new-root complement is

\[
 \boxed{
 \det\!\left(\Delta_N\big|_{(P_{M,N}H_M^0)^\perp}
       \right)=q^2.}                                     \tag{25}
\]

Consequently the half-log determinant of the relative layer is
\(\log q\), and is \(\log p\) for a one-prime covering \(N=Mp\).

#### Proof

Every fiber of (21) has \(q\) elements, so

\[
 \|P_{M,N}f\|^2
 =q^{-1}\sum_{y\in R_N}|f(y\bmod M)|^2
 =\sum_{x\in R_M}|f(x)|^2.                               \tag{26}
\]

The first identity in (23) follows by multiplying the two normalization
factors.  Translation by one commutes with reduction modulo \(M\), hence
\(T_NP_{M,N}=P_{M,N}T_M\); (4) gives the second identity.  Since
\(P_{M,N}(M^{-1/2}\mathbf1)=N^{-1/2}\mathbf1\), the reduced spaces are
preserved.  Equations (19), (23), and the definition of \(J_N\) then give

\[
 g_N(P_{M,N}^{(1)}z,P_{M,N}^{(1)}w)=g_M(z,w),
 \qquad
 J_NP_{M,N}^{(1)}=P_{M,N}^{(1)}J_M.                       \tag{27}
\]

Because \(\Delta_N\) is self-adjoint and its action on the range of
\(P_{M,N}\) is unitarily equivalent to \(\Delta_M\), that range is
reducing.  Multiplicativity of determinants across the resulting
orthogonal decomposition, followed by Theorem 2.1, yields

\[
 \det\!\left(\Delta_N\big|_{(P_{M,N}H_M^0)^\perp}\right)
 =\frac{\det'\Delta_N}{\det'\Delta_M}
 =\frac{N^2}{M^2}=q^2.                                   \tag{28}
\]

This proves (25) and all assertions. \(\square\)

The covering pullback (22) and the closed-stratum vector (13) are two
different root correspondences.  The former transports the polarized
old level functorially; the latter supplies the Gysin-type intersection
factor \(p^{-k/2}\).  Keeping both is what separates the torsion
\(\log p\) from the incidence coefficient in (16).

## 7. What is and is not obtained

Equation (16) is a new finite-place intersection identity, but it does
not yet identify the inductive limit of (19) with CCM degree one.  The
root-covering compatibility is now supplied by Theorem 6.1.  Two global
compatibility problems remain:

1. the archimedean fiber must provide the Gamma determinant and the polar
   \(H^0/H^2\) boundary in the same relative determinant category;
2. the resulting global relative intersection form must descend through
   the CCM restriction cone and agree with the alternating form already
   constructed in 106.181--106.182.

Generic graph positivity alone cannot prove that final identification;
the matrix-tree countermodel recorded in Paper 41 remains applicable to
an arbitrary network.  The force of (16) is narrower: it supplies an
exact geometric origin for both factors of the literal von Mangoldt
coefficient on the actual finite root tower.

## 8. Status

Proved without RH or zero input:

* positive cyclic-root Laplacians and their exact pseudodeterminants;
* the relative torsion \(\log p\) of every prime-power layer;
* the root-stratum intersection coefficient \(p^{-k/2}\);
* the combined identity \(\Lambda(p^k)/\sqrt{p^k}\);
* a canonical positive polarization at every finite root level;
* functorial polarized embeddings under every root covering, with exact
  relative determinant \(q^2\).

Still required:

* the archimedean Gamma/polar determinant fiber;
* global relative descent and comparison with the CCM form.
