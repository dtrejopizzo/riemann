# 106.43 — The mean-periodic radical complement

## Purpose

Document 106.41 expresses the source complement by the conditions

\[
\int q(x)h(x)K^{(2j)}(x)\,dx=0\qquad(j\geq0).        \tag{1}
\]

For even multipliers these conditions have a stronger interpretation. They
are the Taylor coefficients of one convolution equation. The radical
complement is therefore a mean-periodic space whose frequencies belong to
the zero divisor of \(\Xi\). This is an exact structural statement, not a
zero-location assumption.

## 1. From shorting moments to a convolution equation

Put

\[
F(x)=h(x)q(x),
\qquad
\mathcal C_F(t)=\int_{\mathbb R}F(x)K(x-t)\,dx.       \tag{2}
\]

Initially assume that \(q\) is even and compactly supported. Then
\(\mathcal C_F\) is real analytic, differentiation under the integral is
valid to every order, and

\[
\mathcal C_F^{(m)}(0)=(-1)^m\int F(x)K^{(m)}(x)\,dx. \tag{3}
\]

Because \(F\) and \(K\) are even, \(\mathcal C_F\) is even. Hence its odd
derivatives vanish automatically, while (1) annihilates all its even
derivatives.

### Theorem 1 — No compactly supported complement vector

If an even compactly supported multiplier satisfies (1), then \(q=0\).

#### Proof

Equations (1)--(3) show that every derivative of \(\mathcal C_F\) at zero
vanishes. Real analyticity gives \(\mathcal C_F=0\) on an interval, and
analytic continuation gives

\[
F*K=0.                                                 \tag{4}
\]

Since \(F\) is compactly supported, its Fourier transform is entire. Taking
Fourier transforms in (4) gives on the real axis

\[
\widehat F(t)\Xi(t)=0.                                \tag{5}
\]

The real zeros of the nonzero entire function \(\Xi\) are discrete, so
\(\widehat F\) vanishes on a nonempty open subset of the real axis. The
identity theorem gives \(\widehat F\equiv0\), hence \(F=0\), and positivity
of \(h\) gives \(q=0\). \(\square\)

Thus the nontrivial projection of a compact test onto the radical complement
is necessarily noncompact. This is why a compact-support canonical path
cannot see the exact shorted block.

## 2. Mean-periodic extension

Let \(\mathscr A_K\) be the even functions or distributions \(F\) for which
the convolution in (2) is defined and analytic under translation by \(K\).
The argument above, without the compact-support conclusion, proves:

### Theorem 2 — Mean-periodic complement equation

For \(F=hq\in\mathscr A_K\),

\[
q\perp1\oplus\mathcal R
\quad\Longleftrightarrow\quad
\boxed{F*K=0}.                                        \tag{6}
\]

The forward implication uses (1)--(3). The reverse implication follows by
differentiating (6) at the origin.

In Fourier language, (6) is

\[
\Xi\,\widehat F=0                                    \tag{7}
\]

in the corresponding distributional multiplier sense. Consequently the
exponential monomials in the mean-periodic spectrum have frequencies among
the zeros of \(\Xi\). For a simple zero \(z\), the even elementary solution
is

\[
F_z(x)=\cos(zx),
\qquad q_z(x)=\frac{\cos(zx)}{h(x)},                  \tag{8}
\]

recovering the explicit modes of 106.39. Multiple zeros add the usual
polynomial factors in \(x\).

No assertion that all zeros are real is used in (6)--(8). A nonreal zero
simply produces an exponentially modulated mean-periodic mode, still allowed
by the double-exponential \(K\)-weighted Hilbert space.

## 3. Exact form of the remaining frame theorem

The complementary contraction is now a frame inequality on the
mean-periodic solution space:

\[
\boxed{
\frac12\|F/h\|_{L^2(\mu_K)}^2
\leq\mathscr E_K(F/h),
\qquad F*K=0,quad \mu_K(F/h)=0.}                     \tag{9}
\]

For finite exponential polynomials this becomes a matrix inequality indexed
by a finite subset of the zero divisor. Proving it by diagonal estimates is
insufficient: arbitrarily close frequencies can make the exponential basis
ill-conditioned. The required estimate must therefore be a Gram inequality
for the complete ordinary-prime--Gamma energy, not a sum of one-frequency
bounds.

Equation (9) is the exact spectral-synthesis version of the source-side
contraction. Its advantage over a direct zero sum is that every entry of its
Gram matrix still has the physical representation (7) of 106.41 with the
literal weights \(\Lambda(n)\), the Gamma density and the theta kernel.
