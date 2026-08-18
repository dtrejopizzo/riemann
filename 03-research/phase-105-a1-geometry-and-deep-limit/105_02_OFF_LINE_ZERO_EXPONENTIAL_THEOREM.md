# 105_02 — Off-line zeros force exponential Li modes

## Purpose

This document proves the zero-side assertion represented in panel 4 of
105_01: a critical-line zero produces a bounded oscillatory Li mode, whereas
an off-line zero produces an exponentially growing oscillatory mode. It also
proves that the exponential growth cannot be cancelled permanently by the
other zeros.

This is the first half of the proposed contradiction. The second half would
be an unconditional subexponential bound derived from the ordinary prime
weights.

## 1. The Cayley modulus identity

Let \(\rho=\beta+i\gamma\) be a nontrivial zero and put

\[
 w_\rho:=1-{1\over\rho}={\rho-1\over\rho}.
\]

Then

\[
 |w_\rho|^2
 ={(\beta-1)^2+\gamma^2\over\beta^2+\gamma^2}
 =1+{1-2\beta\over|\rho|^2}.                              \tag{1}
\]

Consequently,

\[
 |w_\rho|=1\iff\beta={1\over2},\qquad
 |w_\rho|<1\iff\beta>{1\over2}.                          \tag{2}
\]

The functional equation and conjugation place

\[
 \rho,\quad \bar\rho,\quad1-\rho,\quad1-\bar\rho          \tag{3}
\]

in the same zero orbit. Their Cayley transforms are

\[
 w,\quad\bar w,\quad\bar w^{-1},\quad w^{-1}.             \tag{4}
\]

## 2. Exact quartet law

Assume \(\beta>1/2\) and write

\[
 w=e^{-a+i\theta},\qquad a=-\log|w|>0.                    \tag{5}
\]

The Li contribution of the symmetric quartet (3) is

\[
\begin{aligned}
 Q_n(\rho)
  &=4-\left(w^n+\bar w^n+w^{-n}+\bar w^{-n}\right)\\
  &=\boxed{4-4\cosh(na)\cos(n\theta)}.                    \tag{6}
\end{aligned}
\]

Thus its envelope has exponential scale \(e^{an}\). More precisely, returns
of the rotation \(n\theta\pmod{2\pi}\) to
\((-\pi/3,\pi/3)\) give \(\cos(n\theta)\ge1/2\), and hence

\[
 Q_n(\rho)\le4-2\cosh(na)\le4-e^{an}.                    \tag{7}
\]

Those returns occur infinitely often. They are periodic when
\(\theta/(2\pi)\) is rational and syndetic when it is irrational, by
minimality of an irrational circle rotation. Therefore a single off-line
quartet has exponentially large excursions.

If \(\beta=1/2\), then \(a=0\). The formal quartet coalesces into two copies
of the conjugate pair and

\[
 Q_n(\rho)=4-4\cos(n\theta)\in[0,8].                       \tag{8}
\]

The actual conjugate-pair contribution is half of (8), hence lies in
\([0,4]\). This is the bounded blue curve in panel 4.

## 3. Permanent cancellation by other zeros is impossible

The quartet calculation alone concerns one orbit. The following argument
handles the complete Li coefficient and all possible cancellations.

Let

\[
 G(z):=z{d\over dz}\log\xi\!\left({1\over1-z}\right)
      =\sum_{n\ge1}\lambda_nz^n.                          \tag{9}
\]

The change of variables \(s=(1-z)^{-1}\) maps the unit disk onto
\(\Re s>1/2\). A zero \(\rho\) is mapped to

\[
 z=w_\rho=1-{1\over\rho}.                                \tag{10}
\]

If \(\rho\) has multiplicity \(m_\rho\), the logarithmic derivative in
(9) gives a simple pole at \(w_\rho\) with nonzero residue

\[
 \mathop{\mathrm{Res}}_{z=w_\rho}G(z)=m_\rho w_\rho.        \tag{11}
\]

Hence no coincident zero can remove the pole: multiplicities add with the
same sign.

Suppose RH is false. By the functional equation there is a zero with
\(\beta>1/2\), so (2) gives a pole of \(G\) strictly inside the unit disk.
Define

\[
 r_0:=\min_{\Re\rho>1/2}|w_\rho|<1.                       \tag{12}
\]

The minimum exists because \(|w_\rho|\to1\) as
\(|\Im\rho|\to\infty\). Equation (11) shows that the radius of convergence
of (9) is exactly \(r_0\). Cauchy--Hadamard therefore yields

\[
 \boxed{\limsup_{n\to\infty}|\lambda_n|^{1/n}=r_0^{-1}>1.} \tag{13}
\]

This already proves unavoidable exponential growth of the full sequence.
For an explicit dominant-mode form, let \(W_0\) be the finite set of poles
with modulus \(r_0\), and choose \(r_1\) strictly between \(r_0\) and the
next pole modulus. Subtracting the principal parts in (11) gives

\[
 \lambda_n
 =-\sum_{w\in W_0}m_w w^{-n}+O(r_1^{-n})
 =-r_0^{-n}P(n)+O(r_1^{-n}),                              \tag{14}
\]

where

\[
 P(n)=\sum_{w\in W_0}m_w e^{-in\arg w}                   \tag{15}
\]

is a nonzero finite trigonometric sum. After equal phases are grouped, its
Cesaro mean square is positive:

\[
 \lim_{N\to\infty}{1\over N}\sum_{n=1}^N|P(n)|^2
 =\sum_j M_j^2>0.                                         \tag{16}
\]

Thus \(|P(n)|\) is bounded below on an infinite subsequence, and (14)
again gives exponential excursions. This proves directly that interference
among equally dominant zeros cannot suppress the exponential scale for all
degrees.

## 4. Exact conclusion and remaining implication

The proved implication is

\[
 \boxed{\neg\mathrm{RH}
 \quad\Longrightarrow\quad
 \limsup_{n\to\infty}|\lambda_n|^{1/n}>1.}                \tag{17}
\]

Equivalently,

\[
 \boxed{\limsup_{n\to\infty}|\lambda_n|^{1/n}\le1
 \quad\Longrightarrow\quad\mathrm{RH}.}                  \tag{18}
\]

Accordingly, the remaining prime-side target is the unconditional bound

\[
 \limsup_{n\to\infty}|\lambda_n|^{1/n}\le1               \tag{19}
\]

for the actual coefficients generated by the ordinary weights
\(\Lambda(m)\). Establishing (19) would complete the contradiction and prove
RH. It is not established in this document.

## 5. Reproduction check

    cd 03-research/phase-105-a1-geometry-and-deep-limit
    python3 tools/off_line_quartet_check.py

The checker compares the direct four-term orbit sum with (6) and verifies
the bounded critical-line formula. It is a diagnostic check of the algebra,
not a substitute for the proof above.
