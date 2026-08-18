# D.117 — Source-derived Lindblad form, Gamma jumps and the Tate jets

## Verdict

The A--B--C contact data do define, at every finite arithmetic cutoff, a
canonical completely positive jump dynamics.  Its Dirichlet form is exactly
the positive boundary differential constructed in D.111, with every prime
power and the complete quarter-shift Gamma density.  No von Mangoldt weight
is inserted at this stage: the rate of the jump by \(\log p^k\) is the product
of the reduced A--B contact \(\log p\) and the D.110 Green eigenvalue
\(p^{-k/2}\).

This construction does **not** prove row D.  It gives a precise obstruction:

1. the global arithmetic jump measure has infinite mass at infinity and is
   not a Levy measure;
2. the finite-cutoff Markov kernel consists of translation-invariant vectors,
   not of the two Tate jets;
3. the Gamma jump form is well defined on Fourier vectors but the two Tate
   exponentials lie outside its exponential-moment domain;
4. subtracting the divergent contact mass produces the completed
   explicit-formula operator, but destroys Markov contractivity; and
5. detailed balance supplies positivity of the unshifted difference form,
   not the sharp lower bound on the two-jet primitive quotient.

Thus a source-defined Lindblad realization exists and recovers the exact
positive term preceding \(B_{\rm nuc}\).  Its desired quotient contraction is
again exactly the still-required row-D inequality.

## 1. Source-derived arithmetic rates

For \(n=p^k\), let

\[
 a_n=\log n=k\log p,
 \qquad
 w_n=(\log p)p^{-k/2}={\Lambda(n)\over\sqrt n}.       \tag{1.1}
\]

The two factors in \(w_n\) have already been obtained independently:

* \(\log p\) is the determinant degree of the reduced prime contact, derived
  both from the two prime rulings of A and from the cyclotomic Witt contact of
  B;
* \(p^{-k/2}\) is the \(k\)-th Green eigenvalue of the ordered residuation
  frame in D.110 (equivalently the OS/Szego contraction of D.114).

The cyclotomic contact is zero when \(n\) is not a prime power.  Consequently
the source-defined atomic measure at cutoff \(X\) is

\[
 \nu_{{\rm fin},X}
   =\sum_{\substack{p^k\leq X\\k\geq1}}
       {\log p\over p^{k/2}}\,\delta_{k\log p}.        \tag{1.2}
\]

Formula (1.2) is therefore a consequence of A--B--D.110, not a definition
using the analytic von Mangoldt function.

## 2. The finite-cutoff completely positive dynamics

Let \(S_aF(t)=F(t-a)\) on \(L^2(\mathbb R,dt)\).  The symmetric jump generator
associated with (1.2) is

\[
 L_{{\rm fin},X}
  =\sum_{p^k\leq X}w_{p^k}
     (2I-S_{a_{p^k}}-S_{-a_{p^k}}).                  \tag{2.1}
\]

Each summand is \((I-S_a)^*(I-S_a)\), hence \(L_{{\rm fin},X}\geq0\), and

\[
 \langle F,L_{{\rm fin},X}F\rangle
 =\sum_{p^k\leq X}{\Lambda(p^k)\over\sqrt{p^k}}
       \|F-S_{\log p^k}F\|_2^2.                       \tag{2.2}
\]

Equivalently, on bounded functions the conservative generator

\[
 (\mathcal A_{{\rm fin},X}f)(t)
 =\sum_{p^k\leq X}w_{p^k}
   \bigl(f(t+a_{p^k})+f(t-a_{p^k})-2f(t)\bigr)        \tag{2.3}
\]

generates a compound-Poisson Markov semigroup.  On the commutative
von Neumann algebra \(L^\infty(\mathbb R)\), every Markov map is completely
positive.  More concretely, if

\[
 A_X=\sum_{p^k\leq X}w_{p^k},
\]

then \(e^{t\mathcal A_{{\rm fin},X}}\) is the norm-convergent exponential of
a positive linear combination of translation automorphisms and preserves
the unit.  Hence complete positivity here is elementary and does not invoke
the desired inequality.

## 3. The Gamma oscillator is a positive infinite-activity jump form

Put

\[
 g_\infty(r)={e^{-r/2}\over1-e^{-2r}},\qquad r>0.     \tag{3.1}
\]

The quarter-shift oscillator in A gives (3.1) from its heat trace; it is not
chosen to match the completed zeta factor.  Since

\[
 g_\infty(r)\sim{1\over2r}\quad(r\downarrow0),
 \qquad
 g_\infty(r)\sim e^{-r/2}\quad(r\to\infty),
\]

one has

\[
 \int_0^\infty \min(1,r^2)g_\infty(r)\,dr<\infty.    \tag{3.2}
\]

Thus the symmetric measure with density \(g_\infty(|r|)/2\) is a genuine
Levy measure.  Its positive generator is

\[
 L_\infty F
 =\int_0^\infty g_\infty(r)
       (2I-S_r-S_{-r})F\,dr,                          \tag{3.3}
\]

in quadratic-form sense, and

\[
 \langle F,L_\infty F\rangle
 =\int_0^\infty g_\infty(r)\|F-S_rF\|_2^2\,dr.       \tag{3.4}
\]

On the Fourier vector of frequency \(\tau\), its symbol is

\[
\begin{aligned}
 \ell_\infty(\tau)
 &=2\int_0^\infty g_\infty(r)(1-\cos\tau r)\,dr\\
 &=\mathrm{Re}\,\psi\!\left({1\over4}+{i\tau\over2}\right)
      -\psi\!\left({1\over4}\right)\geq0.           \tag{3.5}
\end{aligned}
\]

The second equality follows by substituting \(u=2r\) in the standard
integral difference formula for the digamma function.  Hence (3.3) contains
the full Gamma term, not merely an asymptotic or a finite collection of
oscillator modes.

## 4. Exact completed Dirichlet form

At cutoff \(X\), set

\[
 L_X=L_{{\rm fin},X}+L_\infty.                        \tag{4.1}
\]

Then D.111's differential satisfies the exact identity

\[
 \|\partial_XF\|^2=\langle F,L_XF\rangle.             \tag{4.2}
\]

Writing

\[
 m_0=\log\pi-\psi(1/4),                               \tag{4.3}
\]

the explicit boundary expansion gives

\[
 \boxed{
 B_{{\rm nuc},X}(F,F)
  =(2A_X+m_0)\|F\|^2-\langle F,L_XF\rangle.}          \tag{4.4}
\]

This is the requested pullback comparison at the level of forms: all
prime powers enter (2.2), all Gamma modes enter (3.4), and the residual
scalar is precisely the completed contact mass.  Equation (4.4) is an exact
identity, but its right-hand side is a difference of positive forms.

The identification of the two jets with the primitive moments is literal.
On a symmetric window \(I_T=[-T,T]\), put

\[
 h_-(t)=e^{-t/2},\qquad h_+(t)=e^{t/2},
 \qquad M_\pm(F)=\langle F,h_\pm\rangle.               \tag{4.5}
\]

Under the central logarithmic change of variables these are the two Tate
evaluations \(\widehat f(0)\) and \(\widehat f(1)\), equivalently the
Fourier--Laplace jets at \(-i/2\) and \(i/2\).  Their Gram matrix is

\[
 G_T=\begin{pmatrix}2\sinh T&2T\\2T&2\sinh T\end{pmatrix}>0. \tag{4.6}
\]

If \(H_T(a,b)=ah_-+bh_+\), then

\[
 P_T=I-H_TG_T^{-1}H_T^*                               \tag{4.7}
\]

is the canonical orthogonal projection onto the primitive space.  Thus the
precise pullback statement is

\[
 \boxed{
 B_{{\rm nuc},X}^{\rm prim}
 =P_T^*\bigl((2A_X+m_0)I-L_X\bigr)P_T.}               \tag{4.8}
\]

There is no omitted prime, exponent or real mode in (4.8): substituting
(2.1) and (3.3) expands its second term into every \(p^k\) with coefficient
\((\log p)p^{-k/2}\) and the complete Gamma integral (3.4).

On the primitive subspace

\[
 \mathcal P=\ker(M_-,M_+),                             \tag{4.9}
\]

row D is therefore equivalent to

\[
 L_X|_{\mathcal P}\geq(2A_X+m_0)I_{\mathcal P}.       \tag{4.10}
\]

Complete positivity of \(e^{-tL_X}\) proves only \(L_X\geq0\).  It does not
imply the much stronger shifted estimate (4.10).

## 5. Harmonic states are not the two Tate jets

For finite \(X\), equality in the positive form gives

\[
 F\in\ker L_X
 \Longrightarrow
 S_{\log p^k}F=F\quad(p^k\leq X),
 \quad
 S_rF=F\quad\text{for a.e. }r>0.                      \tag{5.1}
\]

The Gamma condition already implies that \(F\) is translation invariant;
thus the distributional harmonic vectors are constants, and there is no
nonzero harmonic vector in \(L^2(\mathbb R)\).  The two Tate jets

\[
 h_-(t)=e^{-t/2},\qquad h_+(t)=e^{t/2}                \tag{5.2}
\]

are neither translation invariant nor \(L^2\).

There is a stronger Gamma obstruction.  Formally inserting \(h_+\) into
(3.3) requires

\[
 \int_0^\infty g_\infty(r)
   \bigl(2-e^{r/2}-e^{-r/2}\bigr)\,dr.                \tag{5.3}
\]

But the integrand tends to \(-1\) (up to the harmless normalization fixed
in (3.3)) as \(r\to\infty\).  Hence (5.3) diverges.  The same holds for
\(h_-\).  The two jets are boundary functionals selected by Poisson/Tate
duality; they are not harmonic states in the domain of the positive Gamma
Lindbladian.

This also explains why a ground-state/Doob transform cannot solve the
problem canonically.  A transform by one positive jet can make that one
boundary vector harmonic after renormalization, but no single conservative
transform makes both reciprocal jets into invariant probability states.

## 6. Failure of the global arithmetic Levy limit

The full arithmetic atomic measure would be

\[
 \nu_{\rm fin}
 =\sum_{p,k\geq1}{\log p\over p^{k/2}}\,
       \delta_{k\log p}.                              \tag{6.1}
\]

A Levy measure on \(\mathbb R\) must have finite mass outside every
neighbourhood of zero.  Here

\[
 \nu_{\rm fin}([1,\infty))
 \geq\sum_{p\geq3}{\log p\over\sqrt p}=\infty.        \tag{6.2}
\]

For instance, the divergence follows from the prime number theorem by
partial summation (and equivalently from the pole of
\(-\zeta'/\zeta(s)\) at \(s=1\)).  Therefore (6.1) is not a Levy measure.

The failure is visible directly on every nonzero compactly supported
\(F\).  When \(\log n\) exceeds the diameter of its support,

\[
 \|F-S_{\log n}F\|^2=2\|F\|^2,
\]

so

\[
 \langle F,L_{{\rm fin},X}F\rangle
 =2A_X\|F\|^2+O_F(1)\longrightarrow\infty.           \tag{6.3}
\]

The completed explicit formula exists only after subtracting this
divergent scalar mass.  At finite cutoff this gives

\[
 \widetilde L_X=L_X-(2A_X+m_0)I.                     \tag{6.4}
\]

Although scalar renormalization preserves positivity of individual kernels
as linear maps after multiplying by a positive scalar, it destroys the
unital contraction/Markov normalization and supplies no uniform lower
bound.  In fact

\[
 B_{{\rm nuc},X}(F,F)=-\langle F,\widetilde L_XF\rangle. \tag{6.5}
\]

Thus the signed completed form appears exactly at the step where the
global conservative Lindblad interpretation ceases to exist.

## 7. Detailed balance and the product formula

Lebesgue measure makes every translation reversible, so \(L_X\) satisfies
detailed balance.  This forces self-adjointness and the positivity of
(4.2).  It does not determine a lower spectral edge after restriction to
\(\mathcal P\).

Indeed the Fourier multiplier of \(L_X\) is continuous and vanishes at
\(\tau=0\).  Hence the unconditioned dynamics on \(\mathbb R\) has no
positive spectral gap.  Imposing the two Tate moments is a codimension-two
condition; neither reversibility nor a product formula fixes the norm of
the resulting Schur complement.  That norm is the Calderon/Douglas
contraction isolated in D.112.

The product formula correctly fixes the two boundary jets and the scalar
counterterm in (4.4).  It does not convert the divergent positive jump
measure into a conservative global process, nor does it imply (4.10).

## 8. Exact conclusion

The CP/Lindblad route yields a genuine new structural identification:

\[
 \boxed{
 \text{A--B contact}\times\text{D.110 Green depth}
 \;\oplus\;\text{Gamma oscillator}
 \;=\;\partial_X^*\partial_X.}
\]

Together with the two Tate moment map, its pullback is exactly
\(B_{{\rm nuc},X}\) by (4.8).  What it does **not** yield is positivity of
that pullback.  The desired assertion is the sharp, renormalized spectral
estimate (4.10), not complete positivity of the unrenormalized generator.

Therefore this route validates every local coefficient and every Gamma
mode without circularity, but does not close row D.
