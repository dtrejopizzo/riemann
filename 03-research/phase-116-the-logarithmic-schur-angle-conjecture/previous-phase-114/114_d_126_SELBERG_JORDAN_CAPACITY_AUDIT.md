# D.126 — Selberg's identity and the positive Jordan covariance

## Verdict

Selberg's second-order identity is exact in the central normalization:

\[
 {1\over\sqrt n}(\mu*\log^2)(n)
 ={\Lambda(n)\log n+(\Lambda*\Lambda)(n)\over\sqrt n}. \tag{0.1}
\]

The two terms are the derivative and square pieces of the logarithmic
contact.  By themselves they still do not form a Hilbert square of the
linear completed contact.

There is, however, a stronger positive structure behind (0.1).  For every
\(t>0\), the Jordan function

\[
 J_t(n)=(\mu*\operatorname{id}_t)(n)
 =n^t\prod_{p\mid n}(1-p^{-t})                          \tag{0.2}
\]

has a positive Hankel kernel \(J_t(mn)\).  Shorting this kernel by the unit
and differentiating at \(t=0\) gives exactly

\[
 \Lambda(mn),                                           \tag{0.3}
\]

and after central congruence, \(\Lambda(mn)/\sqrt{mn}\).
Thus the reduced A--B contact is a genuine infinitesimal Schur capacity,
not merely an engineered positive coefficient.

This is real progress, but it does not yet close D.  The Jordan capacity
lives on the divisibility/Hankel coefficient space.  The annulus operator
uses additive logarithmic translations and the completed Gamma term with a
relative sign.  A bounded functor carrying the Jordan covariance to the
annulus Schur complement, including Gamma and the two jets, has not been
constructed.  Assuming it is contractive would be the missing inequality.

## 1. Selberg's identity from the logarithmic derivation

Let \(Z\) denote convolution by the constant-one Dirichlet series and let
\(\delta\) be the logarithmic derivation.  Put

\[
 C=(\delta Z)Z^{-1}.                                    \tag{1.1}
\]

Then \(C\) is convolution by \(\Lambda\), and

\[
 (\delta^2Z)Z^{-1}=\delta C+C^2.                       \tag{1.2}
\]

Coefficient comparison gives

\[
 \boxed{
 (\mu*\log^2)(n)
 =\Lambda(n)\log n+(\Lambda*\Lambda)(n).}             \tag{1.3}
\]

Multiplicative central weighting is compatible with Dirichlet convolution,
so division by \(\sqrt n\) gives (0.1).

Both terms on the right of (1.3) are coefficientwise nonnegative.  But
\(C^2\) is same-orientation Dirichlet composition, not the adjoint square
\(C^*C\) required by a Hilbert Schur complement.

## 2. The Jordan family

For \(t>0\), define (0.2).  It is multiplicative, and at a prime power

\[
 J_t(p^k)=p^{kt}-p^{(k-1)t}.                            \tag{2.1}
\]

Writing \(x=p^t>1\), the local moment sequence is

\[
 a_0=1,
 \qquad a_k=(x-1)x^{k-1}\quad(k\ge1).                 \tag{2.2}
\]

It is represented by the positive two-point measure

\[
 \nu_{p,t}=x^{-1}\delta_0+(1-x^{-1})\delta_x,          \tag{2.3}
\]

because \(\int y^k\,d\nu_{p,t}=a_k\).  Taking tensor products over the
finitely many primes occurring in a finite set of integers gives

\[
 \boxed{
 K_t(m,n)=J_t(mn)\ge 0}                                \tag{2.4}
\]

as a positive semidefinite kernel.

Central normalization is the congruence

\[
 K_t^{\rm cen}(m,n)={J_t(mn)\over\sqrt{mn}},            \tag{2.5}
\]

so it remains positive.

## 3. Shorting the unit produces the reduced contact

Since \(J_t(1)=1\), the Schur complement of the unit row and column is

\[
 S_t(m,n)=J_t(mn)-J_t(m)J_t(n),
 \qquad m,n>1.                                         \tag{3.1}
\]

It is positive semidefinite for every \(t>0\), being the covariance kernel
of the monomials in the product probability measure from Section 2.

For \(r>1\), formula (0.2) shows

\[
 J_t(r)=
 \begin{cases}
  t\log p+O(t^2),&r=p^k,\\
  O(t^{\omega(r)}),&\omega(r)\ge2.
 \end{cases}                                           \tag{3.2}
\]

Therefore

\[
 \boxed{
 \lim_{t\downarrow0}{S_t(m,n)\over t}=\Lambda(mn).}   \tag{3.3}
\]

The product term in (3.1) is \(O(t^2)\) for \(m,n>1\).  Limits of positive
kernels are positive, hence \(\Lambda(mn)\) is positive on the reduced
nonunit sector.  It splits as one rank-one block for each prime, exactly
matching the reduced contact geometry.

At one prime,

\[
 {1\over t}S_t(p^i,p^j)\longrightarrow\log p          \tag{3.4}
\]

for all \(i,j\ge1\); for different primes the limit is zero.

## 4. Selberg is the second infinitesimal capacity

Expanding (0.2) to second order yields

\[
 J_t(n)=t\Lambda(n)
 +{t^2\over2}(\mu*\log^2)(n)+O(t^3)                   \tag{4.1}
\]

when \(n\) is a prime power, while the same formula with vanishing first
term holds generally.  Substitution of (1.3) gives

\[
 J_t(n)=t\Lambda(n)
 +{t^2\over2}\bigl(\Lambda(n)\log n
                      +(\Lambda*\Lambda)(n)\bigr)
 +O(t^3).                                               \tag{4.2}
\]

For the covariance (3.1), the second coefficient also subtracts
\(\Lambda(m)\Lambda(n)\).  Positivity of \(S_t\) therefore supplies a
hierarchy: the first contact kernel is positive, and on its nullspace the
second Selberg covariance is positive.

This is the correct second-order Schur interpretation of Selberg's identity.

## 5. Why the raw second-order functional is still indefinite at the unit

Let

\[
 s(n)=\Lambda(n)\log n+(\Lambda*\Lambda)(n).           \tag{5.1}
\]

Then \(s(1)=0\), \(s(p)=(\log p)^2\), and
\(s(p^2)=3(\log p)^2\).  The raw Hankel matrix on \(\{1,p\}\) is

\[
 (\log p)^2
 \begin{pmatrix}0&1\\1&3\end{pmatrix},              \tag{5.2}
\]

whose determinant is negative.  Thus (1.3) itself is not a positive
functional before the unit is shorted.  The positive object is the full
Jordan kernel followed by its Schur complement, not an isolated derivative
coefficient.

## 6. Relation to the annulus Schur capacity

The D.124 annulus contact is a representation of the reduced kernel through
logarithmic translations.  Formula (3.3) suggests the desired construction:

1. represent the positive Jordan covariance \(S_t\) on the cumulative
   prime-depth boundary module;
2. transport it through the ordered-residuation/annulus landing map;
3. include an archimedean Jordan factor for the Gamma oscillator;
4. short the two Tate boundary vectors; and
5. take the derivative at \(t=0\).

Steps 1 and the finite arithmetic part of 2 are source-defined.  What is not
proved is that the landing map is contractive uniformly in \(t\) and the
cofinal cutoff, nor that the Gamma relative term is the derivative of a
positive factor compatible with the same shorting.

Without those statements, (3.3) proves positivity of the local reduced
contact but not the completed form \(-B_{\rm nuc}\).  The latter contains
the difference between arithmetic and Gamma/polar channels isolated in
D.117.

## 7. Higher-order identities

The full family is more informative than any fixed derivative:

\[
 J_t=\mu*e^{t\log}.                                     \tag{7.1}
\]

Its \(r\)-th derivative at zero is \(\mu*\log^r\), and the logarithmic
derivation expresses it as a Bell polynomial in
\(\Lambda,\delta\Lambda,\ldots\).  Every finite derivative alone has a
zero unit coefficient and hence an indefinite raw \(\{1,p\}\) Hankel
matrix.  Positivity is retained only by the untruncated exponential family
and Schur shorting.

Therefore going to third or higher Selberg identities without preserving
the full Jordan kernel cannot solve the sign problem.  The correct next
object is an archimedean/completed Jordan covariance, not a higher isolated
coefficient.

## 8. Conclusion

Selberg's identity reveals a nontrivial positive capacity mechanism:

\[
 \boxed{
 S_t(m,n)=J_t(mn)-J_t(m)J_t(n)\ge0,
 \qquad
 t^{-1}S_t(m,n)\to\Lambda(mn).}
\]

This gives an unconditional, zero-free construction of the reduced
prime-power contact as an infinitesimal Schur complement.  It also explains
the positive combination \(\Lambda\log+\Lambda*\Lambda\) at second order.

The remaining obstruction is now narrower: construct a completed
prime--Gamma Jordan covariance whose annulus landing is uniformly
contractive and whose two-jet shorted derivative is \(-B_{\rm nuc}\).  The
finite Euler factor has the required positivity; the archimedean relative
factor and the cofinal landing estimate remain to be established.
