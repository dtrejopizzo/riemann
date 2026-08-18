# Row (d): exact Dirichlet reduction of the primitive inequality

## 1. Logarithmic coordinates

Let

\[
 (f\star g)(x)=\int_0^\infty f(y)g(x/y)\,d^*y,
 \qquad
 f^\vee(x)=x^{-1}\overline{f(x^{-1})},
\]

and put

\[
 F(t)=e^{t/2}f(e^t),\qquad
 (S_aF)(t)=F(t-a).
\]

The map `f -> F` is the central-line unitary change of variables.  The two
ruling moments become

\[
 \widehat f(0)=\int_{\mathbb R}F(t)e^{-t/2}\,dt,
 \qquad
 \widehat f(1)=\int_{\mathbb R}F(t)e^{t/2}\,dt.
\]

Thus the primitive test space is carried to

\[
 \mathcal P=
 \left\{F\in C_c^\infty(\mathbb R):
 \int F(t)e^{-t/2}dt=\int F(t)e^{t/2}dt=0\right\}.
\]

## 2. The finite contact is a graph energy plus a mass term

### Proposition

For `n >= 2`, `a=log n`, and `h=f star f^vee`, one has

\[
 h(n)+n^{-1}h(n^{-1})
 =2n^{-1/2}\operatorname{Re}\langle F,S_aF\rangle_{L^2(\mathbb R)}.
\]

Consequently, if

\[
 c_n=\frac{\Lambda(n)}{\sqrt n},\qquad
 A_X=\sum_{2\le n\le X}c_n,
\]

and `log X` is at least the diameter of `supp(F)`, then the finite part of
the nuclear intersection is exactly

\[
 K(f,f)=2A_X\|F\|_2^2-
 \sum_{2\le n\le X}c_n\|F-S_{\log n}F\|_2^2. \tag{2.1}
\]

### Proof

Direct substitution gives

\[
\begin{aligned}
 h(n)
 &=n^{-1}\int_0^\infty y f(y)\overline{f(y/n)}\,d^*y\\
 &=n^{-1/2}\int_{\mathbb R}F(t)\overline{F(t-\log n)}\,dt,
\end{aligned}
\]

and similarly

\[
 n^{-1}h(n^{-1})
 =n^{-1/2}\int_{\mathbb R}F(t)
                 \overline{F(t+\log n)}\,dt.
\]

The two integrals are complex conjugates.  The unitary translation identity

\[
 2\operatorname{Re}\langle F,S_aF\rangle
 =2\|F\|_2^2-\|F-S_aF\|_2^2
\]

proves (2.1).  If `log n` exceeds the support diameter, the correlation is
zero and the two terms on the right cancel.  Hence the formula is independent
of which sufficiently large `X` is used.  This also proves that all sums in
(2.1) are finite on the stated domain.

The second term in (2.1) is the negative of the Dirichlet form of the
weighted translation graph with edges `log n` and weights `c_n>0`.

## 3. The archimedean term is also mass minus Dirichlet energy

Use the Fourier convention for which Plancherel reads

\[
 \|F\|_2^2=\frac1{2\pi}\int_{\mathbb R}|\widehat F(\tau)|^2d\tau.
\]

The archimedean multiplier already obtained from the Fourier finite part is

\[
 m_\infty(\tau)=\log\pi-
 \operatorname{Re}\psi\left(\frac14+\frac{i\tau}{2}\right).
\]

Put `a_j=j+1/4`,

\[
 m_0=\log\pi-\psi(1/4),
 \qquad
 \widehat{R_jF}(\tau)=
 \frac{\tau}{\sqrt{4a_j^2+\tau^2}}\widehat F(\tau).
\]

The digamma series gives the pointwise identity

\[
 m_\infty(\tau)
 =m_0-\sum_{j=0}^\infty
 \frac{1}{a_j}\frac{\tau^2}{4a_j^2+\tau^2}.
\]

All summands after `m_0` are nonnegative.  Monotone convergence and
Plancherel therefore give the exact quadratic-form identity

\[
 G_\infty(f,f)=m_0\|F\|_2^2-
 \sum_{j=0}^\infty\frac1{a_j}\|R_jF\|_2^2. \tag{3.1}
\]

For a fixed smooth compactly supported `F` the series is finite as a
quadratic form: near infinity the summand is `O(a_j^{-3})` after using
`tau^2/(4a_j^2+tau^2) <= tau^2/(4a_j^2)` and the finiteness of
`||F'||_2`.

## 4. The exact remaining inequality

Combining (2.1) and (3.1) yields

\[
\begin{aligned}
 B_{\rm nuc}(f,f)
 ={}&(2A_X+m_0)\|F\|_2^2\\
 &-\sum_{2\le n\le X}c_n
          \|F-S_{\log n}F\|_2^2
 -\sum_{j=0}^\infty\frac1{a_j}\|R_jF\|_2^2. \tag{4.1}
\end{aligned}
\]

Therefore row (d) is exactly the following nonlocal Poincare inequality:

\[
 (2A_X+m_0)\|F\|_2^2
 \le
 \sum_{2\le n\le X}c_n\|F-S_{\log n}F\|_2^2
 +\sum_{j=0}^\infty\frac1{a_j}\|R_jF\|_2^2, \tag{4.2}
\]

for every `F in P` and every sufficiently large `X`.

This reduction uses only the prime contact formula, the Tate involution and
the independently fixed archimedean Fourier finite part.  It does not use a
zero of `xi` or a spectral sign.

Equation (4.2) is not yet a proof: after comparison with row (c), its validity
for all primitive tests is equivalent to RH.  Its value is that it identifies
the missing geometric statement without spectral language.  A valid closure
must construct a compactified graph/tropical object whose ordinary Poincare
or Hodge theorem proves (4.2), including the precise mass `2A_X+m_0`, rather
than assuming (4.2) when defining that object.

## 5. Ground-state/Doob acceptance test

An `A^*A` or Doob-transform proof is non-circular only if it supplies, before
using `B_nuc`, operators `A_X` on a geometrically defined completion such
that

\[
 \|A_XF\|^2=
 \sum_{2\le n\le X}c_n\|F-S_{\log n}F\|_2^2
 +\sum_{j\ge0}\frac1{a_j}\|R_jF\|_2^2
 -(2A_X+m_0)\|F\|_2^2
\]

on `P`, with a closed nonnegative right-hand side established from the
construction.  Defining `A_X` as the square root of the displayed form is
invalid: existence of that square root is precisely (4.2).  Likewise, the
formal exponentials `e^{t/2}` and `e^{-t/2}` are not in `L^2(R)`; treating
them as ground states requires a rigged-space domain and a proved boundary
identity, not only the two moment equations.
