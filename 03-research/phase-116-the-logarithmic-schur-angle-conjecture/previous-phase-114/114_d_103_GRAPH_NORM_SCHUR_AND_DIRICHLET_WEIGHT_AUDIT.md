# D.103 — Graph-norm Schur complement and Dirichlet-weight audit

## Status

The positive graph metric built from periodic source norm and
Fourier--Poisson target norm has an explicit finite-cutoff Schur
complement.  It is positive, but its arithmetic coefficients are Gram
coefficients of the zeta summation matrix: they count common multiples.
They are not the logarithmic Euler/contact coefficients.  Already at the
first mixed support, the graph Gram couples `2` and `3`, whereas
`Lambda(6)=0`; along one prime it distinguishes `p` from `p^2`, whereas
`Lambda(p)=Lambda(p^2)`.

The mismatch cannot be repaired by a positive diagonal Dirichlet/Gamma
weight.  Positive weighted common-multiple sums retain mixed-prime terms.
The unique weight obtained by forcing the desired contact is a conjugate
of the contact operator by the inverse zeta matrix; it imports `B_nuc` and
need not be positive.

There is also no uniform cofinal Hilbert inverse.  The inverse of the
finite zeta matrix is the Mobius matrix, and its first column has squared
norm equal to the number of squarefree integers below the cutoff.  Hence
the inverse norms diverge and the smallest singular values tend to zero.
Graph regularization can make each finite Schur complement positive, but
it either collapses the faithful cokernel as the regularization is removed
or changes the row-C character.

Thus the naive Hodge graph norm does not yield the exact `p^k+Gamma`
cohomology metric.  A successful weight must be non-diagonal and globally
Euler--Gamma coupled; deriving its positivity without defining it from the
completed contact remains the missing theorem.

No RH statement or desired sign is assumed.  The paper is not modified.

## 1. Finite graph metric and its Schur complement

Let `Z_N:E_N->F_N` be a finite Poisson/zeta summation map, let `P_N>0` be
the periodic source metric and `W_N>0` the Fourier target metric.  On a
source vector `x` and target vector `y` put

\[
 \mathcal G_N(x,y)
 =\langle x,P_Nx\rangle
  +\langle y-Z_Nx,W_N(y-Z_Nx)\rangle.                     \tag{1.1}
\]

Minimizing over `x` gives

\[
 x_y=(P_N+Z_N^*W_NZ_N)^{-1}Z_N^*W_Ny                    \tag{1.2}
\]

and the positive effective target form

\[
 \boxed{
 S_N=W_N-W_NZ_N(P_N+Z_N^*W_NZ_N)^{-1}Z_N^*W_N\ge0.}     \tag{1.3}
\]

For `P_N=0` and closed injective range this becomes the weighted
orthogonal quotient projection

\[
 Q_N=I-Z_N(Z_N^*W_NZ_N)^{-1}Z_N^*W_N.                    \tag{1.4}
\]

If `Z_N` is square and invertible, (1.4) is zero: the finite algebraic
cokernel disappears.  Keeping `P_N>0` prevents collapse but changes the
complex by a Tikhonov mass.  Formula (1.3) is a generic positive Schur
complement; exact contact coefficients are not automatic.

## 2. Zeta matrix versus logarithmic contact

On the finite divisor poset `{1,...,N}`, the zeta summation matrix is

\[
 (Z_N)_{m,n}=1_{n\mid m}.                                 \tag{2.1}
\]

For the unweighted target metric,

\[
 (Z_N^*Z_N)_{i,j}
 =\#\{m\le N:\mathrm{lcm}(i,j)\mid m\}
 =\left\lfloor{N\over\mathrm{lcm}(i,j)}\right\rfloor.
                                                                    \tag{2.2}
\]

This is a common-multiple kernel.  By contrast, the row-B/C reduced
contact convolution is supported on prime powers:

\[
 k(n)=\Lambda(n),
 \qquad k(p^r)=\log p,
 \qquad k(n)=0\text{ if }n\text{ has two primes}.          \tag{2.3}
\]

At `N>=6`, (2.2) gives

\[
 (Z_N^*Z_N)_{2,3}=\lfloor N/6\rfloor>0,                  \tag{2.4}
\]

while the corresponding mixed contact has `Lambda(6)=0`.  Along one
prime, at `N=4`,

\[
 (Z_4^*Z_4)_{1,2}=2,
 \qquad (Z_4^*Z_4)_{1,4}=1,                              \tag{2.5}
\]

whereas

\[
 \Lambda(2)=\Lambda(4)=\log2.                             \tag{2.6}
\]

Thus the graph norm fails both defining properties of the reduced
contact: mixed-prime annihilation and prime-power idempotence.  This is a
term-by-term mismatch before any limit.

The reason is structural.  `Z^*Z` is quadratic in the summation operator;
the contact is the logarithmic derivative

\[
 Z\partial(Z^{-1})=\sum_{n\ge2}\Lambda(n)U_n.             \tag{2.7}
\]

A positive graph Gram does not perform the derivation in (2.7).

## 3. Positive diagonal weights cannot repair the support

Let `W_N=diag(w_1,...,w_N)` with every `w_m>=0`.  Then

\[
 (Z_N^*W_NZ_N)_{i,j}
 =\sum_{\substack{m\le N\\\mathrm{lcm}(i,j)\mid m}}w_m.
                                                                    \tag{3.1}
\]

For distinct primes `p,q`, this is a sum of nonnegative weights on
multiples of `pq`.  It can vanish for every cutoff only by killing all
those target weights.  Doing so simultaneously for all pairs removes a
cofinal part of the arithmetic target and is incompatible with a faithful
scaling representation.

Likewise

\[
 \sum_{p\mid m}w_m\ge\sum_{p^2\mid m}w_m,                 \tag{3.2}
\]

with strict inequality whenever a positive weight occurs on a number
divisible by `p` but not `p^2`.  It cannot reproduce equal nonzero masses
for all `p^k`.

The Gamma weight acts in the archimedean direct summand.  A positive direct
sum cannot cancel the finite mixed coefficient (2.4); cancellation would
require a signed cross-place metric, the very global polarization sought
in row D.

## 4. The forced exact weight is circular

At a finite cutoff where `Z_N` is invertible, suppose one prescribes an
exact Hermitian contact matrix `K_N` and asks for

\[
 Z_N^*W_NZ_N=K_N.                                        \tag{4.1}
\]

There is a unique solution,

\[
 \boxed{W_N=Z_N^{-*}K_NZ_N^{-1}.}                         \tag{4.2}
\]

If `K_N` is the D.32 prime--Gamma contact, (4.2) defines the target metric
from the form whose positivity must be proved.  Congruence preserves
inertia, so `W_N` is positive exactly when `K_N` is positive.  Formula
(4.2) is therefore a change of coordinates, not a Hodge construction.

The same circularity applies to a non-diagonal cofinal weight defined by
solving the Schur equation (1.3) for a desired quotient form.

## 5. Singular-value obstruction to the cofinal inverse

The inverse of (2.1) is the Mobius matrix

\[
 (Z_N^{-1})_{m,n}=1_{n\mid m}\,\mu(m/n).                  \tag{5.1}
\]

Its first column is

\[
 (\mu(1),\mu(2),\ldots,\mu(N))^T.                        \tag{5.2}
\]

Hence

\[
 \|Z_N^{-1}\|^2
 \ge\sum_{n\le N}\mu(n)^2=:Q(N),                        \tag{5.3}
\]

the number of squarefree integers up to `N`.  Since every prime is
squarefree and there are infinitely many primes,

\[
 Q(N)\longrightarrow\infty,
 \qquad
 \sigma_{\min}(Z_N)\le Q(N)^{-1/2}\longrightarrow0.      \tag{5.4}
\]

Thus the inverses of the finite range maps are not uniformly bounded in
the naive Hilbert metrics.  This is the arithmetic finite-section version
of the dense nonclosed critical range in D.102.

There is also no uniform bound on `Z_N`: its first column contains `N`
ones, so

\[
 \|Z_N\|\ge\sqrt N.                                      \tag{5.5}
\]

Consequently the unweighted graph norms do not form a uniformly equivalent
cofinal Hilbert system.

## 6. Scaling and Real covariance

On the full Frechet multiplier spaces, `Z` commutes with the scaling
semigroup because all `U_n` commute.  Finite divisor cutoffs break this
covariance at the boundary: multiplication by `p` exits the cutoff and
must be projected away.  The graph metrics (1.1) therefore acquire
cutoff-dependent boundary defects.

Weights which make all central half-density shifts unitary are constrained
by a Haar covariance relation.  Rapidly decaying weights can make `Z`
Hilbert--Schmidt, but then scaling is not unitary and the adjoint action no
longer gives the self-dual coefficient `n^(-1/2)`.  Haar-type weights retain
the central adjoint but do not remove the Mobius inverse growth (5.3).

The Fourier--Real identity `ZF=JZ` holds on the Frechet primitive core.  A
graph completion preserves it only if the source and target weights are
Fourier-dual.  None of the positive diagonal weights satisfying that
condition changes the common-multiple support (3.1).

## 7. Character audit

The algebraic nuclear character of the Frechet quotient is stable under
the exact closed-range construction.  Replacing its topology by the graph
completion (1.1) has two possible outcomes:

1. as `P_N->0`, the square invertible finite sections have zero quotient,
   matching the collapse of the dense `L^2` range;
2. with `P_N>0`, the Schur complement is nonzero but is a regularized
   target form whose coefficients are those of (1.3), not the logarithmic
   character (2.7).

No uniform trace-class comparison identifies the resulting Hilbert trace
with Meyer's nuclear trace.  Such an identification would have to prove
the exact D.32 coefficients and the Gamma finite part; it is not implied by
positivity of `S_N`.

## 8. Outcome and next weight candidate

The naive graph metric is positive for a generic Hilbert-complex reason,
but it fails the arithmetic character test.  Positive diagonal
Dirichlet/Gamma weights cannot fix the failure.

The next candidate must use a canonical **logarithmic connection metric**,
not `Z^*Z`: differentiate a positive two-parameter graph metric in the
normal direction and retain the Quillen connection of D.94.  D.94 already
shows that its first variation is exactly `B_nuc`; the new question is
whether a second, independently positive bulk energy makes that first
variation negative on the primitive tangent.  Convexity of an arbitrary
determinant metric will not suffice, because the local normal connection
changes sign.  The candidate must exploit joint convexity of the
Fourier--Poisson graph and the two Tate boundary conditions before taking
the derivative.

