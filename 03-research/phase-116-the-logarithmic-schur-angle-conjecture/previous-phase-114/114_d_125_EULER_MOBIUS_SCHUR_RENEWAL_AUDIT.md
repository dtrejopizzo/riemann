# D.125 — Euler--Möbius renewal and the arithmetic Schur complement

## Verdict

There is an exact source-derived renewal identity for the central contact:

\[
 {\Lambda\over\sqrt{\cdot}}
 = {\mu\over\sqrt{\cdot}}*{\log\over\sqrt{\cdot}}.     \tag{0.1}
\]

Equivalently, on every finite divisibility truncation, the contact operator
is the logarithmic commutator

\[
 C_N=[D,Z_N]Z_N^{-1}.                                   \tag{0.2}
\]

This identifies algebraically how all previous Euler contacts feed the new
block.  It does not turn the contact into a positive square.  The canonical
Schur square built from (0.2) is \(C_N^*C_N\), quadratic in the von Mangoldt
coefficients, whereas row D contains the Hermitian linear term
\(C_N+C_N^*\).

Moreover the finite Möbius inverses are not uniformly bounded at the
central normalization: their first column already has squared norm
\(\sum_{n\le N}\mu(n)^2/n\), which diverges.  Thus the algebraic finite
renewal cannot be passed to a bounded cofinal Hilbert inverse.  This
obstruction is coefficient-theoretic and does not use a zero divisor.

Consequently Euler--Möbius renewal improves the typing of the multiscale
Schur problem but does not prove its positivity.  A positive-real
factorization of the linear logarithmic derivative is precisely the missing
row-D/Herglotz assertion.

## 1. Normalized Dirichlet convolution

Let

\[
 z(n)=n^{-1/2},\qquad
 m(n)=\mu(n)n^{-1/2},\qquad
 \ell(n)=(\log n)n^{-1/2}.                              \tag{1.1}
\]

Under Dirichlet convolution,

\[
 z*m=\delta_1.                                          \tag{1.2}
\]

The elementary identity

\[
 \log n=\sum_{d\mid n}\Lambda(d)                       \tag{1.3}
\]

and Möbius inversion give

\[
 (m*\ell)(n)
 ={1\over\sqrt n}\sum_{d\mid n}\mu(d)\log(n/d)
 ={\Lambda(n)\over\sqrt n}.                            \tag{1.4}
\]

Thus (0.1) contains every prime power with coefficient
\((\log p)p^{-k/2}\) and vanishes on integers having at least two distinct
prime factors, exactly as required by A--B.

## 2. Finite logarithmic commutator

On the finite divisibility poset \(1\le n\le N\), let

\[
 (Z_Nf)(n)=\sum_{d\mid n}{1\over\sqrt d}f(n/d),        \tag{2.1}
\]

and let \(D\) be multiplication by \(\log n\).  The matrix \(Z_N\) is
triangular with diagonal one, and

\[
 Z_N^{-1}=M_N,
 \qquad
 (M_Nf)(n)=\sum_{d\mid n}{\mu(d)\over\sqrt d}f(n/d).   \tag{2.2}
\]

The derivation rule gives

\[
 ([D,Z_N]f)(n)
 =\sum_{d\mid n}{\log d\over\sqrt d}f(n/d).           \tag{2.3}
\]

Therefore

\[
 \boxed{C_N=[D,Z_N]M_N}                                \tag{2.4}
\]

is convolution by \(\Lambda(n)/\sqrt n\).  Applying the annulus
representation \(\delta_n\mapsto S_{\log n}\) sends (2.4) to the exact
prime-power contact operator used in D.117--D.124.

## 3. Why the natural Schur square has the wrong degree

Let

\[
 A_N=Z_N^*Z_N,
 \qquad B_N=Z_N^*[D,Z_N]M_N.                            \tag{3.1}
\]

Eliminating the positive \(A_N\) block produces expressions of the form

\[
 B_N^*A_N^{-1}B_N.                                     \tag{3.2}
\]

After cancelling \(Z_N\), every such canonical expression is a positive
Gram square of the logarithmic derivative, hence contains

\[
 C_N^*C_N,                                               \tag{3.3}
\]

not the desired linear Hermitian contact

\[
 C_N+C_N^*.                                              \tag{3.4}
\]

Coefficientwise, (3.3) is an autocorrelation of von Mangoldt weights and
contains products \(\Lambda(m)\Lambda(n)\).  Formula (3.4) contains one
copy of each reduced contact.  No cancellation of a positive square changes
this polynomial degree without inserting an additional indefinite channel.

This is the cumulant/covariance distinction: the logarithmic derivative is
an Euler cumulant, while a Hilbert Schur complement is a covariance square.

## 4. Local positivity already forbids a universal contact square

If the contact functional itself were a positive convolution square, its
Gram kernel on \(\{\delta_1,\delta_p\}\) would be positive.  Instead it is

\[
 \begin{pmatrix}
 0&\log p\\
 \log p&\log p
 \end{pmatrix},                                         \tag{4.1}
\]

with determinant \(- (\log p)^2\).  Hence no placewise Hilbert square can
realize the linear contact.  The completed Gamma term and the two primitive
moments must participate before a global sign can exist.

The renewal identity (2.4) does not alter (4.1); it merely writes the same
indefinite functional as a commutator times a Möbius inverse.

## 5. The Möbius inverse is not cofinally bounded

Apply \(M_N\) to the basis vector at \(1\).  Its entries are

\[
 (M_Ne_1)(n)={\mu(n)\over\sqrt n}.                      \tag{5.1}
\]

Therefore

\[
 \|M_N\|^2\ge\|M_Ne_1\|^2
 =\sum_{n\le N}{\mu(n)^2\over n}.                       \tag{5.2}
\]

The squarefree integers have positive elementary density, and partial
summation yields

\[
 \sum_{n\le N}{\mu(n)^2\over n}
 ={6\over\pi^2}\log N+O(1).                            \tag{5.3}
\]

Thus

\[
 \|M_N\|\gg\sqrt{\log N}.                              \tag{5.4}
\]

There is no uniformly bounded Hilbert inverse obtained by taking the
directed limit of the finite triangular matrices.  Equation (5.4) uses no
information about nontrivial zeta zeros.

The nuclear/Frechet row-C inverse can still be used algebraically on its
natural domain, but it cannot be inserted as a bounded \(A^\dagger\) in the
row-D Schur complement without an additional closed-range theorem.

## 6. Positive-real factorization is exactly the missing assertion

For a bounded operator \(C\), the Hermitian contact \(C+C^*\) admits a
Hilbert positive-real realization precisely when its real part has the
required sign.  Equivalently, its Cayley transform is contractive on the
relevant primitive space.  Applied to the logarithmic derivative (2.4),
this is the operator form of the Herglotz/de Branges criterion isolated in
D.121.

Hence proposing a positive state-space realization of (2.4), or a bounded
outer spectral factor for (3.4), assumes the missing positivity.  Euler
factorization determines \(C_N\), but not the sign of its real part after
the Gamma and polar renormalizations.

## 7. Consequence for the annulus capacity

In the D.124 annulus coordinates, \(Z_N\) sums all divisor refinements of a
boundary contact and \(M_N\) performs inclusion--exclusion.  Substitution
of (2.4) into the core/annulus block gives an exact algebraic formula for
\(B^*A^\dagger B\) at every finite cutoff.  But:

1. its Hilbert square is quadratic in \(C_N\);
2. the desired entering block is linear in \(C_N\);
3. the Möbius inverse has no uniform bounded limit; and
4. changing the coefficient metric to subtract the unwanted square is a
   Krein construction whose primitive positivity is D.

Therefore there is no source-derived renewal square which automatically
absorbs the new batch.

## 8. Conclusion

The Euler--Möbius calculation supplies the exact renewal identity

\[
 \boxed{
 {\Lambda\over\sqrt{\cdot}}
 ={\mu\over\sqrt{\cdot}}*{\log\over\sqrt{\cdot}},
 \qquad C_N=[D,Z_N]Z_N^{-1}.}
\]

It is valuable because it organizes all prime powers and all earlier
contacts without reference to zeros.  Nevertheless, logarithmic derivatives
are linear cumulants, whereas positive Schur complements are quadratic
Gram objects.  The natural square has the wrong coefficient degree, and the
central Möbius inverse is unbounded cofinally.

The remaining theorem is a positive-real factorization of the **completed**
logarithmic derivative on the two-jet primitive space.  That factorization
is equivalent to row D rather than a consequence of Euler inversion.

