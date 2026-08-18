# 106.61 — Nonlinear mean-periodic amplification gate

## Purpose

The exact radical complement of 106.43 is

\[
 F*K=0,\qquad \widehat K(z)=\Xi(z)=\xi\!\left(\frac12+iz\right).
 \tag{1}
\]

A hypothetical off-axis frequency has a nonzero exponential rate.  This
suggests amplifying that rate by products or tensor powers, and then applying
the spatial Möbius--theta inverse of 106.40.  This note tests that proposal
without using a zero-location hypothesis.

There is an exact dichotomy.  Translation-invariant linear operations,
including every finite Möbius/Jordan jet, preserve the mean-periodic
frequency but cannot amplify its real exponential rate.  Pointwise products
do amplify the rate, but they add frequencies and therefore leave the
mean-periodic complement.  Moreover, the spatial Möbius inverse is singular
on precisely a hypothetical off-axis frequency: the formal interchange
needed to infer \(F*k_1=0\) fails by a divergent squarefree series, and the
regularized Dirichlet symbol has a pole at the same zero.

Thus this nonlinear route does not prove the complementary floor.  The
result is a proved gate: any successful nonlinear operation must preserve
the complete prime--Gamma form by a mechanism other than pointwise
multiplication or a translation multiplier.

## 1. Internal non-duplication audit

The following earlier results are binding.

* 104.16 proves the positivity of the complete Jordan hierarchy
  \(j_k=\mu*\log^k\), its loss of sign after polar completion, and the
  off-axis falsifier \(\xi(s+a)\xi(s-a)\).
* Phases 36 and 44 prove that abstract Krein tensor powers amplify the
  negative index but do not produce an independent arithmetic bound.
* E101.096 proves that unrestricted products create all-pairs frequencies
  and squared multiplicities rather than the same-zero divisor.
* 106.40 proves the spatial Möbius--theta identity, and 106.43 identifies
  the exact complement with (1).

What is proved below, in the present normalization, is the missing
compatibility calculation between those two last facts: nonlinear powers
escape the zero divisor, while Möbius inversion becomes singular on it.

## 2. Products of mean-periodic exponential polynomials

Use the Fourier convention

\[
 \widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx.
 \tag{2}
\]

The double-exponential decay of \(K\) makes its convolution with every
finite exponential polynomial well defined at all frequencies in the
critical strip.  Since \(K\) is even,

\[
 (e^{iz\cdot}*K)(t)=e^{izt}\Xi(z).
 \tag{3}
\]

### Proposition 1 — Exact Minkowski-sum criterion

Let

\[
 F(x)=\sum_{j=1}^r c_j e^{iz_jx},\qquad
 G(x)=\sum_{\ell=1}^s d_\ell e^{iw_\ell x}
 \tag{4}
\]

be finite exponential polynomials.  Then

\[
 ((FG)*K)(t)
 =\sum_{\nu}
   \left(\sum_{z_j+w_\ell=\nu}c_jd_\ell\right)
   \Xi(\nu)e^{i\nu t}.
 \tag{5}
\]

Consequently \(FG\) is mean-periodic for \(K\) if and only if, for every
resulting frequency \(\nu\), either its aggregated coefficient vanishes or
\(\Xi(\nu)=0\).

#### Proof

Multiply (4), group equal frequencies, and apply (3).  Distinct
exponentials are linearly independent, which gives the final equivalence.
\(\square\)

The zero divisor is therefore not an algebra under pointwise
multiplication.  It would have to be closed under the relevant Minkowski
sums for such a closure to hold.

### Theorem 2 — Tail amplification necessarily exits the complement

Suppose provisionally that

\[
 \rho=\frac12+a+i\gamma,\qquad 0<a<\frac12,
 \tag{6}
\]

is a zero of \(\xi\), and put

\[
 z_0=\gamma-ia,
 \qquad F_{z_0}(x)=\cos(z_0x).
 \tag{7}
\]

Then \(F_{z_0}*K=0\).  However, for every integer \(k\) with
\(ka>1/2\),

\[
 \boxed{F_{z_0}^{\,k}*K\ne0.}
 \tag{8}
\]

#### Proof

The first assertion follows from

\[
 \Xi(z_0)=\xi\!\left(\frac12+iz_0\right)=\xi(\rho)=0
 \tag{9}
\]

and the evenness of \(\Xi\).  On the other hand,

\[
 \cos(z_0x)^k
 =2^{-k}\sum_{j=0}^k\binom{k}{j}
      e^{i(k-2j)z_0x}.                                \tag{10}
\]

The top frequency \(kz_0\) has nonzero coefficient \(2^{-k}\).  Its
completed-zeta argument is

\[
 \frac12+ikz_0=\frac12+ka+ik\gamma,
 \tag{11}
\]

whose real part is greater than one.  The completed zeta function has no
zero there.  Hence \(\Xi(kz_0)\ne0\).  In (5) the exponential with
frequency \(kz_0\) cannot cancel against any other term, proving (8).
\(\square\)

The exponential rate of \(F_{z_0}\) is \(a\), while that of its \(k\)-th
power is \(ka\).  Theorem 2 says that the first time multiplication
amplifies the rate beyond the critical half-width, it has already destroyed
the exact equation (1).

## 3. Tensor powers and the diagonal map

The multivariable tensor

\[
 \mathcal F_k(x_1,\ldots,x_k)=\prod_{j=1}^kF_{z_0}(x_j)
 \tag{12}
\]

is annihilated by convolution with \(K\) in each separate coordinate.
Thus tensoring does preserve the coordinatewise mean-periodic equations.
The desired amplification, however, occurs only after diagonal restriction:

\[
 (\operatorname{Diag}\mathcal F_k)(x)
 =\mathcal F_k(x,\ldots,x)=F_{z_0}(x)^k.              \tag{13}
\]

By Theorem 2 this diagonal is not in the one-variable complement for
\(ka>1/2\).  Therefore

\[
 \operatorname{Diag}\circ(K*_{x_j})
 \ne (K*)\circ\operatorname{Diag}.                   \tag{14}
\]

The tensor construction stores the original frequency in separate
variables; the diagonal adds the frequencies and loses the annihilating
factor.  This is the exact one-variable obstruction, not a dimension-count
heuristic.

## 4. Linear Jordan jets cannot amplify a tail

Every translation multiplier

\[
 T=\sum_m c_mS_{\log m},\qquad S_bf(x)=f(x+b),        \tag{15}
\]

acts diagonally on an exponential:

\[
 T(e^{izx})=\left(\sum_m c_mm^{iz}\right)e^{izx},    \tag{16}
\]

whenever the scalar series is defined.  Hence translations, the Möbius
connection, and every finite \(j_k=\mu*\log^k\) jet preserve \(z\) and
therefore preserve \(|\operatorname{Im}z|\).  They can change an amplitude
or create a pole, but cannot increase the tail exponent.

This yields a sharp preservation--amplification dichotomy for finite
exponential polynomials:

\[
 \begin{array}{c|c|c}
 \text{operation}&\text{keeps the zero frequency}&
                   \text{amplifies }|\operatorname{Im}z|\\ \hline
 \text{translation/Jordan multiplier}&\text{yes}&\text{no}\\
 \text{pointwise product/diagonal tensor}&\text{no in general}&\text{yes}.
 \end{array}                                         \tag{17}
\]

The next section shows that the apparent exception---applying the full
Möbius inverse after (1)---is singular at exactly the relevant frequency.

## 5. The Möbius--theta inverse is singular on a zero mode

Use the primitive theta atom of 106.40,

\[
 k_1(x)=\pi e^{5x/2}(2\pi e^{2x}-3)e^{-\pi e^{2x}},
 \qquad
 K=\sum_{m\ge1}m^{-1/2}S_{\log m}k_1.                \tag{18}
\]

The standard theta functional equation identifies the raw series in (18)
with the even kernel \(K\) also on the negative half-line (106.31 used only
the positive half-line to make termwise positivity visible).  For every
fixed real \(x\), that series and the doubly indexed Möbius inversion series
converge absolutely.  Divisor regrouping therefore gives on the full real
line

\[
 \sum_{d\ge1}\frac{\mu(d)}{\sqrt d}
 S_{\log d}K=k_1.                                    \tag{19}
\]

This extends the pointwise statement of 106.40 from the positive half-line;
local uniformity follows from the Gaussian factor
\(e^{-\pi e^{2x}m^2}\).

The transform of the primitive atom is explicit:

\[
 \boxed{
 \widehat{k_1}(z)
 =\frac12\pi^{-1/4+iz/2}
   \left(-\frac12-iz\right)
   \Gamma\!\left(\frac54-\frac{iz}{2}\right).}
 \tag{20}
\]

Indeed, substitute \(y=\pi e^{2x}\) in (2).  The remaining integral is

\[
 2\Gamma\!\left(\frac94-\frac{iz}{2}\right)
 -3\Gamma\!\left(\frac54-\frac{iz}{2}\right)
 =\left(-\frac12-iz\right)
  \Gamma\!\left(\frac54-\frac{iz}{2}\right).       \tag{21}
\]

In particular \(\widehat{k_1}(\pm z_0)\ne0\) for every nontrivial-zeta
frequency \(z_0\).

It is tempting to apply (19) to \(F_{z_0}*K=0\) and conclude
\(F_{z_0}*k_1=0\), contradicting (20).  The required interchange is not
valid.  It already fails absolutely on the complex elementary component
\(F(x)=e^{iz_0x}\).  With \(z_0=\gamma-ia\), a change of variable gives

\[
 \begin{aligned}
 &\sum_{d\ge1}\frac{|\mu(d)|}{\sqrt d}
 \int_{\mathbb R}|e^{iz_0x}|
       |K(x-t+\log d)|\,dx\\
 &\qquad =C_{K,a,t}
 \sum_{d\ge1}\frac{|\mu(d)|}{d^{1/2+a}}=\infty,
 \end{aligned}                                       \tag{22}
\]

because \(0<a<1/2\) and squarefree integers have positive density.  The
opposite elementary component diverges at least as strongly.  Thus Fubini
cannot move the Möbius inverse through the convolution on an off-axis mode.

### Proposition 3 — The regularized inverse has the same zero singularity

For \(\varepsilon>0\), define

\[
 M_\varepsilon
 =\sum_{d\ge1}\mu(d)d^{-1/2-\varepsilon}S_{\log d}.
 \tag{23}
\]

Then pointwise, locally uniformly on \(\mathbb R\),

\[
 M_\varepsilon K
 =\sum_{\ell\ge1}\frac{a_\varepsilon(\ell)}{\sqrt\ell}
 S_{\log\ell}k_1,
 \qquad
 a_\varepsilon(\ell)
 =\prod_{p\mid\ell}(1-p^{-\varepsilon})\in[0,1],    \tag{24}
\]

and

\[
 M_\varepsilon K\longrightarrow k_1
 \quad(\varepsilon\downarrow0).                     \tag{25}
\]

In the initial half-plane of absolute convergence, followed by meromorphic
continuation, its transform is

\[
 \boxed{
 \widehat{M_\varepsilon K}(w)
 =\widehat{k_1}(w)
   \frac{\zeta(1/2-iw)}{\zeta(1/2+\varepsilon-iw)}.}
 \tag{26}
\]

At \(w=-z_0\), the numerator is \(\zeta(\rho)=0\), while
\(\zeta(\rho+\varepsilon)\ne0\) for every sufficiently small
\(\varepsilon>0\).  Hence the continued value in (26) is zero for all such
\(\varepsilon\), whereas (20) gives
\(\widehat{k_1}(-z_0)\ne0\) at the pointwise limit (25).

#### Proof

Group \(\ell=dm\) in \(M_\varepsilon K\).  The inner divisor sum is

\[
 \sum_{d\mid\ell}\mu(d)d^{-\varepsilon}
 =\prod_{p\mid\ell}(1-p^{-\varepsilon}),             \tag{27}
\]

which proves (24).  Dominated convergence, using \(0\le a_\varepsilon\le1\)
and the double-exponential large-\(\ell\) decay of the theta atom, proves
(25).  Finally

\[
 \sum_{\ell\ge1}\frac{a_\varepsilon(\ell)}{\ell^s}
 =\frac{\zeta(s)}{\zeta(s+\varepsilon)},             \tag{28}
\]

which gives (26).  The zero \(\rho\) is isolated, so the denominator has no
zero on \(\rho+(0,\varepsilon_0)\) after decreasing \(\varepsilon_0\).
\(\square\)

Proposition 3 displays the obstruction exactly.  Local kernel convergence
does not control the complex exponential moment selected by an off-axis
mode.  At \(\varepsilon=0\), the quotient in (26) is the indeterminate
\(0/0\) whose removable value is one; for every \(\varepsilon>0\), it is
zero.  Equivalently, the formal inverse symbol

\[
 \sum_{d\ge1}\frac{\mu(d)}{d^{1/2+iz_0+\varepsilon}}
 =\frac1{\zeta(\rho+\varepsilon)}                    \tag{29}
\]

blows like a negative power of \(\varepsilon\), according to the
multiplicity of \(\rho\).

The higher Jordan jets do not remove this singularity.  Their Dirichlet
symbols are derivatives of zeta quotients and are meromorphic at \(\rho\);
coefficient positivity is available only in their half-plane of absolute
convergence.  Continuing them to \(\rho\) loses that order, exactly as
proved independently in 104.16.

## 6. Countermodel boundary

The completed family already recorded in 104.16,

\[
 X_a(s)=\xi(s+a)\xi(s-a),                             \tag{30}
\]

has the same reflection symmetry, explicit off-axis zeros, positive
logarithmic Euler weights

\[
 2\Lambda(m)\cosh(a\log m)>0,                        \tag{31}
\]

and a product of two positive Jordan hierarchies in the safe half-plane.
Thus reflection, conjugation, positivity of every \(j_k\), and nonlinear
tensoring do not by themselves contradict an off-axis divisor.  A proof for
the ordinary weights must use their full globally matched prime--Gamma--pole
placement, not merely membership in this positive hierarchy.

## 7. Verdict and surviving target

The proposed nonlinear route closes as a no-go with exact witnesses:

1. linear Möbius/Jordan operations preserve the frequency and do not
   amplify the tail;
2. pointwise powers amplify the tail but necessarily leave the radical
   complement once the exponent crosses the critical half-width;
3. tensor powers retain mean periodicity only before diagonal restriction;
4. the Möbius--theta inverse cannot be interchanged with the zero-mode
   convolution, and its Dirichlet symbol is singular at that same mode.

No contradiction with a hypothetical subthreshold eigenstate follows from
these operations.  The surviving theorem remains global: exclude the
negative two-ended matching channel using the joint ordinary-prime--Gamma--
polar curvature before projecting to a pointwise product or applying a
singular inverse.  Equivalently, one must prove the finite-cluster trace sign
of 106.48--106.51 (or the nonvanishing of the compatible Evans determinant
of 106.58) by a new jointly shorted inequality.

This document proves an obstruction, not RH.
