# 106.48 — Local Riesz determinants and the constrained cluster trace

## Purpose

Document 106.47 proves that the shorted ordinary-prime--Gamma generator has
only discrete spectrum of finite multiplicity below the threshold \(1/2\).
This note constructs the resulting local determinant without using a finite
Euler product or importing the zero divisor of Xi. It then rewrites the sign
of a subthreshold spectral cluster as an exact three-point expression in the
literal edge measure.

The determinant exists unconditionally. Its nonvanishing is not obtained
for free: it is equivalent to a projection-constrained curvature inequality.
The important reduction is that the admissible kernels are not arbitrary
Hankel coefficient arrays. They are finite-rank orthogonal projections which
commute with the complete generator and annihilate the exact radical.

## 1. The local spectral determinant

Let

\[
 \mathcal H_\perp=(\mathbf 1\oplus\mathcal R)^\perp,
 \qquad L_\perp=L|_{\mathcal H_\perp}.
\]

Fix a compact interval \(J=[a,b]\Subset(0,1/2)\) whose endpoints are not
eigenvalues, and set

\[
 P_J=\mathbf1_J(L_\perp),\qquad H_J=P_J\mathcal H_\perp.
\]

By 106.47, \(H_J\) is finite dimensional. Choose \(z_0<0\) and define

\[
 \boxed{
 D_J(z)=\det_{H_J}\!\left(
 I_{H_J}-(z-z_0)(L_\perp|_{H_J}-z_0)^{-1}
 \right).}                                           \tag{1}
\]

### Theorem 1 — Exact local characteristic function

If the eigenvalues in \(J\), repeated according to multiplicity, are
\(\lambda_1,\ldots,\lambda_m\), then

\[
 \boxed{
 D_J(z)=\prod_{k=1}^m\frac{\lambda_k-z}{\lambda_k-z_0}.} \tag{2}
\]

Consequently \(D_J(z_0)=1\), its zeros are exactly the subthreshold
eigenvalues in \(J\), and

\[
 -\partial_z\log D_J(z)
 =\operatorname {Tr}_{H_J}(L_\perp|_{H_J}-z)^{-1}.   \tag{3}
\]

#### Proof

The spectral theorem diagonalizes the finite-dimensional self-adjoint
operator \(L_\perp|_{H_J}\). Formulae (2)--(3) follow by taking the ordinary
determinant and logarithmic derivative in that eigenbasis. □

This is not the forbidden finite Euler determinant of 106.00. It is the
spectral determinant of the already completed self-adjoint generator, on a
finite Riesz block supplied by 106.47.

## 2. The cluster curvature trace

For every finite-rank spectral projection \(P=P_J\), define

\[
 \mathfrak T(P)
 =\operatorname {Tr}(PL_\perp^2)
 -\frac12\operatorname {Tr}(PL_\perp).               \tag{4}
\]

### Theorem 2 — Exact sign alternative

For \(P=P_J\),

\[
 \boxed{
 \mathfrak T(P)=
 \sum_{\lambda_k\in J}\lambda_k(\lambda_k-1/2).}    \tag{5}
\]

Hence \(P\ne0\) implies \(\mathfrak T(P)<0\). Conversely, absence of
subthreshold spectrum is equivalent to

\[
 \boxed{
 \mathfrak T(P)\ge0
 \quad\hbox{for every finite-rank spectral projection }
 P\subset\mathcal H_\perp.}                          \tag{6}
\]

#### Proof

Equation (5) is the spectral theorem applied to the polynomial
\(x(x-1/2)\). If a subthreshold eigenvalue exists, take \(J\) small enough
to isolate its finite cluster and obtain a negative trace. The converse is
immediate. □

Unlike the scalar inequality for every test vector, (6) only asks for the
trace on finite-dimensional *reducing* subspaces. This restriction is
force-bearing and must be retained below.

## 3. Projection-kernel identities

Let \(q_1,\ldots,q_m\) be an orthonormal eigenbasis of \(H_J\), and put

\[
 \Pi(x,y)=\sum_{k=1}^m q_k(x)\overline{q_k(y)}.       \tag{7}
\]

Then, in the natural \(L^2\)-kernel sense,

\[
\begin{aligned}
 \Pi(y,x)&=\overline{\Pi(x,y)},\\
 \int\Pi(x,z)\Pi(z,y)\,d\mu_K(z)&=\Pi(x,y),\\
 L_x\Pi(x,y)&=L_y\Pi(x,y),                           \tag{8}\\
 \int\Pi(x,y)r_j(y)\,d\mu_K(y)&=0\qquad(j\ge0).
\end{aligned}
\]

The third identity uses that \(P_J\) commutes with \(L\). The fourth uses
the exact threshold identity \(Lr_j=\frac12(r_j-\mu_K(r_j))\): spectral
subspaces in \(J\Subset(0,1/2)\) are orthogonal to constants and to every
radical mode.

Disintegrate the symmetric edge measure of 106.46 by

\[
 2\,d\mathfrak j(x,y)=d\mu_K(x)\,J_x(dy).             \tag{9}
\]

Thus

\[
 (Lf)(x)=\int(f(x)-f(y))\,J_x(dy).                   \tag{10}
\]

### Theorem 3 — Literal three-point trace formula

The two traces in (4) are

\[
\begin{aligned}
 \operatorname {Tr}(PL)
 &=\frac12\int d\mu_K(x)\int J_x(dy)
 \{\Pi(x,x)+\Pi(y,y)-2\operatorname {Re}\Pi(x,y)\}, \tag{11}\\
 \operatorname {Tr}(PL^2)
 &=\int d\mu_K(x)\iint J_x(dy)J_x(dz)\\
 &\quad\times\{\Pi(x,x)-\Pi(x,z)-\Pi(y,x)+\Pi(y,z)\}. \tag{12}
\end{aligned}
\]

The right side of (12) is real, although its displayed integrand need not
be real pointwise.

#### Proof

First truncate the Gamma displacement to
\(\varepsilon\le |x-y|\le\varepsilon^{-1}\) and the prime sum to
\(n\le N\). The resulting jump kernel has finite rate, so every integral
below is absolutely convergent. For (11), sum the symmetrized energy
identity over the orthonormal basis. For (12), use (10) and the finite-rank
identity

\[
\begin{aligned}
 &\sum_{k=1}^m
 (q_k(x)-q_k(y))
 \overline{(q_k(x)-q_k(z))}\\
 &\qquad=\Pi(x,x)-\Pi(x,z)-\Pi(y,x)+\Pi(y,z).         \tag{13}
\end{aligned}
\]

Integrating (13) against
\(d\mu_K(x)J_x(dy)J_x(dz)\) gives
\(\sum_k\|Lq_k\|^2=\operatorname {Tr}(PL^2)\).
Remove the two cutoffs in the graph norm of \(L\). This is legitimate
because a bounded spectral subspace lies in \(\operatorname {Dom}L\);
the small Gamma differences cancel its \(u^{-1}\) singularity, while the
theta factor dominates the large-displacement and prime-power tails. □

Combining (4), (11), and (12) gives a completely source-side formula for
\(\mathfrak T(P)\). Every literal prime power and the complete Gamma measure
occur inside the same double current before a sign is requested.

## 4. Where the arithmetic curvature enters

In the prime--prime part of (12), the same-orientation compositions of
displacements produce the convolution coefficient
\((\Lambda*\Lambda)(n)\). The displacement derivation (equivalently, the
rate-variation/commutator contribution in the spatial representation)
produces \(\delta\Lambda(n)=\Lambda(n)\log n\). Only after those pieces are
combined does one obtain the nonnegative Riccati jet

\[
 j_2(n)=\delta\Lambda(n)+(\Lambda*\Lambda)(n)
       =(\mu*\log^2)(n)\ge0.                         \tag{14}
\]

Opposite orientations produce ratio channels; prime--Gamma compositions
produce mixed continuous-discrete channels. Therefore (14) controls only
one component of (12). The missing sign is precisely the sign after these
components, the polar centering, and the \(\Pi(y,z)\) interference term have
been assembled.

The tower counterexample 106.40(15)--(16) does not settle this restricted
problem. Its coefficient array is arbitrary and need not be the kernel of
an orthogonal projection satisfying all four identities (8). Conversely,
cyclic positivity (14) alone does not prove (6), because it does not control
the mixed and ratio channels.

Thus the next exact theorem is the following projection-constrained lift:

> **Cluster-current inequality.** For every finite-rank projection kernel
> \(\Pi\) satisfying (8), the three-point expression obtained from
> (11)--(12) is nonnegative.

By Theorem 2 this statement excludes every isolated bound state in
\((0,1/2)\). Together with the essential-threshold theorem of 106.47 it
would prove the complementary spectral floor. No determinant convergence
or zero-location premise remains in its formulation.

## 5. Gate and next calculation

The local determinant has now been constructed, but taking its existence as
its nonvanishing would be circular. Likewise, replacing \(\Pi\) by an
arbitrary positive kernel throws away the commutation equation in (8) and
returns to the false unrestricted Hankel lift.

The next calculation must apply \(L_x\Pi=L_y\Pi\) to the ratio and mixed
terms of (12), seeking an exact cancellation with the Gamma and polar parts.
A successful identity must leave only sums with coefficient \(j_2\ge0\),
squares of crossing currents, and zero radical terms. If an uncancelled
signed term remains, it is the precise new obstruction rather than an
unspecified determinant sign.
