# Row (d): cross-place Cauchy incidence and the prime-tower defect

## Status

The archimedean oscillator supplies a canonical incidence matrix between
finite prime-power positions and real modes.  This note proves its strict
sign regularity and locates its only critical divergence.  The resulting
Green Gram couples distinct primes, but the full prime-power towers retain
extra positive directions; those directions are the next local target.

## 1. Incidence matrix

For `k>=0` and `n>=2` put

\[
 M_{k,n}=n^{-(k+1/4)}
       =\exp(-(k+\tfrac14)\log n).                    \tag{1}
\]

This is the matrix of the oscillator heat modes against the arithmetic
displacements.  It depends on the actual positions `log n`, not only on
their masses.

### Proposition 1.1 (strict sign regularity)

For increasing sequences `k_1<...<k_r` and `n_1<...<n_r`, every minor

\[
 \det(M_{k_i,n_j})_{i,j=1}^r
\]

is nonzero and has sign `(-1)^{r(r-1)/2}`.  Equivalently, reversing the
order of the arithmetic columns makes (1) strictly totally positive.

### Proof

Put `x_j=1/n_j`, so `0<x_r<...<x_1<1`.  Factor
`x_j^{1/4}` from column `j`.  The remaining determinant is

\[
 \det(x_j^{k_i})_{i,j}.
\]

It is a generalized Vandermonde determinant.  For increasing nonnegative
integer exponents it equals the ordinary Vandermonde in the `x_j` times a
Schur polynomial with nonnegative coefficients, and the latter is strictly
positive on positive arguments.  The `x_j` occur in decreasing order, so
the Vandermonde has sign `(-1)^{r(r-1)/2}`.

This does not contradict the failure of `TP_2` for the Euler convolution
blocks: (1) is a cross-place incidence matrix, not a local Euler factor.

## 2. Cauchy--Stieltjes Gram

Summing the oscillator modes gives

\[
 (M^*M)_{m,n}
 =\sum_{k\ge0}(mn)^{-(k+1/4)}
 =\frac{(mn)^{-1/4}}{1-(mn)^{-1}}.                  \tag{2}
\]

After normalizing each column to norm one, put `x_n=1/n`.  The correlation
kernel is

\[
 C(m,n)=
 \frac{\sqrt{(1-x_m^2)(1-x_n^2)}}{1-x_mx_n}.        \tag{3}
\]

Writing `x_n=tanh a_n` gives the transparent form

\[
 C(m,n)=\operatorname{sech}(a_m-a_n).                \tag{4}
\]

Thus the oscillator produces a canonical positive, infinite-rank Green
Gram linking all finite places.  Formula (2) is the discrete
Cauchy--Stieltjes shadow of the heat trace in the archimedean boundary
module.

## 3. Criticality

Weight a prime-power column by the square root of its contact conductance
`c_n=Lambda(n)/sqrt(n)`.  Its squared contribution in oscillator row `k`
is

\[
 c_n|M_{k,n}|^2
 =\frac{\Lambda(n)}{n^{2k+1}}.                       \tag{5}
\]

### Proposition 3.1

For every `k>=1`, the sum of (5) over `n` converges absolutely.  For
`k=0` it is

\[
 \sum_{n\ge2}\frac{\Lambda(n)}n,
\]

which diverges.  Hence deleting the lowest oscillator row makes the
cross-place incidence Hilbert--Schmidt, while the lowest row is exactly the
critical renormalized channel.

### Proof

For `k>=1`, use `Lambda(n)<=log n` and convergence of
`sum (log n)n^{-3}`.  For `k=0`, Chebyshev's lower estimate for
`psi(x)=sum_{n<=x}Lambda(n)` and partial summation give logarithmic
divergence.  No RH-strength estimate is used.

The critical row cannot be discarded: it carries the polar/ruling
renormalization.  It must be paired with the two boundary traces before a
norm is taken.

## 4. The prime-tower defect

For one label per prime, the reduced contact is diagonal.  Equations
(3)--(4) then give a compelling Lorentzian finite model: the normalized
Green Gram minus the identity has one large collective direction and
negative relative directions in all arithmetic cuts tested so far.  This
observation is diagnostic only until a uniform inertia theorem is proved.

The actual correspondence theory contains every `p^j`.  On one prime
tower the reduced contact matrix is the rank-one block

\[
 L_p=(\log p)\mathbf1\mathbf1^t,                     \tag{6}
\]

whereas the oscillator columns in (1) distinguish `p,p^2,...`.  Therefore
the candidate difference

\[
 \bigl(\sqrt{\log p\log q}\,C(p^i,q^j)\bigr)
 -\bigoplus_p L_p                                    \tag{7}

\]

has nontrivial internal tower directions.  Direct finite calculations show
that (7) is not Lorentzian as stated; no sign claim is made from those
calculations.

This failure is structural.  The reduced contact forgets `j`, while the
Green incidence must remember the displacement `j log p`.  The metrized
torsor in row (b) is the only already constructed object which retains this
integer.  Consequently the next required object is a negative tower
Laplacian derived from the torsor filtration, not an arbitrary correction
to (7).  It must be compared with the exact Gamma Gram before any Hodge
signature is asserted.

