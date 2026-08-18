# D.195 — Contact-GNS Poisson dilation and the Tate-jet defect

## Verdict

Tensoring the positive reduced-contact algebra of D.194 with the physical
translations gives an exact completely positive local dilation containing
all powers \(p^k\).  For

\[
 r_p=p^{-1/2},\qquad U_p=S_{\log p},                       \tag{0.1}
\]

the Poisson feature operator is

\[
 A_p=\sqrt{1-r_p^2}(I-r_pU_p)^{-1},                       \tag{0.2}
\]

and

\[
 A_p^*A_p=I+\sum_{k\ne0}r_p^{|k|}U_p^k.                  \tag{0.3}
\]

Thus \(\tau_\Lambda(e_p)=\log p\) supplies the exact contact mass and
(0.3) supplies every \(p^k\) with the central factor \(p^{-|k|/2}\).

The normalized operator

\[
 C_p=c_p^{-1/2}A_p,qquad c_p={1+r_p\over1-r_p},           \tag{0.4}
\]

is a contraction, and \(M_p=C_p^*C_p\) is the symmetric Poisson Markov
operator.  But the arithmetic term is not its Markov defect:

\[
 \boxed{A_p^*A_p-I=(c_p-1)I-c_p(I-M_p).}                  \tag{0.5}
\]

After adding Gamma, the complete form is a scalar load minus a positive
Dirichlet generator.  Complete positivity proves only nonnegativity of the
generator; the required spectral-gap lower bound on the two-jet primitive
space is exactly row D.

There is an earlier categorical failure as well.  The full Poisson Markov
operator has critical geometric tails and does not preserve the domain of
the two Tate moments.  Window compression restores bounded support but loses
unitality and the moment kernel; projecting back to the moment kernel is not
positivity preserving.  Hence the local CP dilation cannot simultaneously
be unital, supported and two-jet preserving.

This identifies the exact defect without taking a logarithm or trace.  No
paper file is modified.

## 1. Positive contact coefficients

Recall the reduced-contact algebra

\[
 \mathcal A_\Lambda=c_{00}(\mathbb P),\qquad
 e_pe_q=\delta_{pq}e_p,qquad
 \tau_\Lambda(e_p)=\log p.                               \tag{1.1}
\]

It is a positive semifinite commutative algebra.  For \(n=p^k\), the
contact label is \(e_p\), independent of \(k\); incompatible prime supports
multiply to zero.  Thus the arithmetic reduction and positivity are already
encoded before adding translations.

Let \(H=L^2(\mathbb R,dt)\).  For each prime, \(U_p=S_{\log p}\) is unitary.
The tensor product

\[
 H\widehat\otimes L^2(\mathcal A_\Lambda,\tau_\Lambda)    \tag{1.2}
\]

keeps the translation dynamics and the contact trace in separate, positive
factors.

## 2. Exact Poisson feature map

For any unitary \(U\) and \(0<r<1\), the Neumann series gives

\[
 A_r=\sqrt{1-r^2}\sum_{j\ge0}r^jU^j.                       \tag{2.1}
\]

Multiplying the two convergent series yields

\[
 \begin{aligned}
 A_r^*A_r
 &=(1-r^2)\sum_{i,j\ge0}r^{i+j}U^{j-i}\\
 &=\sum_{k\in\mathbb Z}r^{|k|}U^k.                       \tag{2.2}
 \end{aligned}
\]

Applying (2.2) to (0.1) proves (0.3).  Consequently

\[
 \tau_\Lambda(e_p)\langle F,(A_p^*A_p-I)G\rangle
 =\log p\sum_{k\ne0}p^{-|k|/2}
   \langle F,S_{k\log p}G\rangle.                         \tag{2.3}
\]

Equation (2.3) is the entire finite-place term of row C for \(p\), with no
prime-power truncation.

The spectral maximum of the Poisson kernel is

\[
 \|A_r\|^2={1+r\over1-r}=c_r.                             \tag{2.4}
\]

Hence \(C_r=c_r^{-1/2}A_r\) is a contraction and

\[
 M_r=C_r^*C_r={1\over c_r}\sum_{k\in\mathbb Z}r^{|k|}U^k,
 \qquad0\le M_r\le I.                                    \tag{2.5}
\]

The coefficients

\[
 \pi_r(k)={r^{|k|}\over c_r}                              \tag{2.6}
\]

sum to one.  Thus (2.5) is the symmetric geometric random-walk operator.
Equivalently, conjugation by the shifts with probabilities (2.6) defines
the random-unitary channel

\[
 \Phi_r(X)=\sum_{k\in\mathbb Z}\pi_r(k)U^kXU^{-k},         \tag{2.7}
\]

which is completely positive, unital and trace preserving.  This is the
requested source-defined CP dilation.

## 3. The exact scalar-load defect

Equations (2.2)--(2.5) give, before any trace,

\[
 A_r^*A_r-I=(c_r-1)I-c_r(I-M_r).                           \tag{3.1}
\]

The second term is a positive Markov Dirichlet defect because
\(0\le M_r\le I\).  The first term has the opposite sign and is nonzero:

\[
 c_r-1={2r\over1-r}>0.                                    \tag{3.2}
\]

Therefore complete positivity does not imply
\(A_r^*A_r-I\le0\).  Indeed its Fourier multiplier is the Poisson kernel
minus one and has both signs.

For a finite active prime set \(P\), row C's quadratic form can be written
exactly as

\[
 B_P=A_PI-\mathcal E_P,                                   \tag{3.3}
\]

where

\[
 \begin{aligned}
 A_P&=m_0+\sum_{p\in P}\log p\,(c_p-1),\\
 \mathcal E_P&=L_\infty+\sum_{p\in P}\log p\,c_p(I-M_p),\\
 L_\infty&=\partial_\infty^*\partial_\infty\ge0.
 \end{aligned}                                            \tag{3.4}
\]

Here \(m_0=\log\pi-\psi(1/4)\) and \(L_\infty\) is the complete Gamma
jump generator.  Formula (3.3) is simply (2.3) plus the Gamma term, so it
contains no sign assumption.

On a fixed compact support, primes whose displacement exceeds the window
cancel internally between the two terms of (3.1); they are not discarded.
Thus (3.3) is interpreted as the stabilized relative form of D.73.

The desired primitive inequality is

\[
 \boxed{\mathcal E_P\ge A_PI
 \quad\text{on }\ker M_+\cap\ker M_-.}                     \tag{3.5}
\]

Complete positivity yields only \(\mathcal E_P\ge0\).  The gap (3.5) is
exactly the global Poincare/shorted-capacity statement equivalent to row D.

## 4. Why the full CP map does not preserve the Tate jets

Let \(a=\log p\), \(r=e^{-a/2}\), and write

\[
 M_pF={1\over c_p}\sum_{k\in\mathbb Z}r^{|k|}S_{ka}F.     \tag{4.1}
\]

Take a nonzero compactly supported \(F\).  For all sufficiently separated
positive shifts, the supports in (4.1) are disjoint, and

\[
 \int e^{t/2}|S_{ka}F(t)|\,dt
 =e^{ka/2}\int e^{t/2}|F(t)|\,dt.                          \tag{4.2}
\]

Multiplication by the coefficient \(r^k=e^{-ka/2}\) cancels the exponential
factor exactly.  Hence every sufficiently large \(k\) contributes the same
positive amount to the weighted absolute moment, and

\[
 \int e^{t/2}|M_pF(t)|\,dt=\infty.                         \tag{4.3}
\]

The negative tail similarly makes the \(e^{-t/2}\) absolute moment
diverge.  Thus \(M_p\) does not map the natural two-Tate moment domain into
itself.

If \(M_+(F)=M_-(F)=0\), every individual shifted signed moment is zero.
But (4.3) still prevents the infinite series from defining a vector in the
domain of those unbounded functionals.  Termwise cancellation is not jet
preservation in the completed category.

This critical divergence is not accidental: the central torsor weight
\(p^{-k/2}\) lies exactly at the exponential-moment boundary.

## 5. Window compression and primitive projection

Let \(P_T\) be multiplication by \(1_{[-T,T]}\).  The compression

\[
 M_{p,T}=P_TM_pP_T                                       \tag{5.1}
\]

is a positive contraction and is support preserving.  But it is only
sub-Markov:

\[
 M_{p,T}\mathbf1\ne\mathbf1                              \tag{5.2}
\]

near the boundary.  More importantly, truncation destroys the exact shift
law for the moments, so generally

\[
 M_{p,T}(\ker M_+\cap\ker M_-)
 \not\subseteq\ker M_+\cap\ker M_-.                       \tag{5.3}
\]

One may restore (5.3) algebraically by the orthogonal projection \(\Pi_T\)
onto the two-moment kernel.  But \(\Pi_T\) subtracts signed multiples of
\(e^{t/2}\) and \(e^{-t/2}\); it is not positivity preserving and does not
define a unital CP map on the function algebra.  The compressed candidate

\[
 \Pi_TM_{p,T}\Pi_T                                       \tag{5.4}
\]

therefore loses the source CP structure used in Section 2.

The discrepancy in (5.3) is the one-prime component of the cross-window
boundary covariance computed in D.77 and D.190.

## 6. The Schur-multiplier alternative

The sequence \(\varphi_r(k)=r^{|k|}\) is positive definite on \(\mathbb Z\).
Therefore

\[
 \mathfrak S_r([x_{ij}])=[r^{|i-j|}x_{ij}]                 \tag{6.1}
\]

is a completely positive unital Schur multiplier.  It preserves the matrix
trace and contracts the Hilbert--Schmidt norm.

This does not change the conclusion.  Its positive defect has coefficients
\(1-r^{|i-j|}\), whereas the arithmetic contact in (2.3) has coefficients
\(r^{|k|}\) with the diagonal removed.  Recovering (2.3) requires

\[
 \mathfrak S_r-\mathrm{Diag},                       \tag{6.2}
\]

which is not completely positive and is the matrix version of the scalar
load (3.1).  The CP Schur dilation therefore packages the coefficients but
does not supply their required sign.

## 7. Exact outcome

The contact-GNS/Poisson construction satisfies:

* exact reduced prime support through \(\mathcal A_\Lambda\);
* every power \(p^k\) with its central weight;
* a positive Stinespring/CP dilation at every prime;
* the complete positive Gamma generator;
* exact relative recombination into \(B_{\rm nuc}\).

It fails the simultaneous target in two precise places:

1. uncompressed CP maps do not preserve the two-jet domain;
2. after support/jet repair, the remaining inequality is the gap (3.5), not
   a consequence of CP unitality.

Thus no trace or logarithm was used to manufacture a sign.  The next
admissible improvement must be a **two-chart conservative dilation** whose
state space includes the Tate boundary variables, so that the critical
tails are stored rather than discarded, and whose Schur complement on the
zero-jet sector yields (3.5) with constant one.

## 8. Reproducible certificate

The script `114_d_195_contact_gns_poisson_cp_verify.py` checks:

1. (0.3)--(0.5) for finite cyclic unitaries;
2. positivity and contractivity of \(M_r\);
3. linear divergence of the critical weighted tails;
4. loss of unitality and both moments after zero-extension compression;
5. positivity/unitality of the Schur multiplier and failure of its
   diagonal-removed version to remain positive.
