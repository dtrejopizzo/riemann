# 106.42 — Threshold oscillation gate

## Purpose

The first explicit even threshold state

\[
r_1=K''/K,
\]

has exactly the shape expected of a first nonconstant even mode: it is
negative at the origin and has one positive-half-line crossing. This suggests
an oscillation-theorem proof of the quotient floor in 106.41. The present
note checks the load-bearing hypothesis before using that argument.

The classical total-positivity route does not apply. The failure is already
forced by the exact Gamma density, independently of any truncation or model
Euler product.

## 1. Strict reverse minor of the Gamma kernel

Put

\[
g(u)=\frac{e^{-u/2}}{1-e^{-2u}},\qquad u>0.           \tag{1}
\]

Then

\[
(\log g)''(u)=\frac{4e^{2u}}{(e^{2u}-1)^2}>0.         \tag{2}
\]

Thus \(g\) is strictly logarithmically convex. For \(t>\varepsilon>0\),
take

\[
x_1=0,quad x_2=\varepsilon,quad
y_1=t,quad y_2=t+\varepsilon.
\]

The ordered two-by-two minor of the translation kernel is

\[
\begin{aligned}
\det
\begin{pmatrix}
g(|x_1-y_1|)&g(|x_1-y_2|)\\
g(|x_2-y_1|)&g(|x_2-y_2|)
\end{pmatrix}
&=g(t)^2-g(t-\varepsilon)g(t+\varepsilon)\\
&<0.                                                   \tag{3}
\end{aligned}
\]

Multiplication by the positive row and column factors contributed by
\(K\), \(h\), and the Doob transform does not change this sign.

### Proposition 1 — No TP2 oscillation closure

Neither the Gamma jump kernel nor the short-time off-diagonal kernel of the
full ordinary-prime--Gamma semigroup is TP2.

#### Proof

Equation (3) proves the first assertion. Choose the four points away from
every hypersurface \(|x-y|=\log n\). At those entries the prime atoms do not
contribute to the first off-diagonal coefficient of the short-time kernel.
Its minor is therefore \(t_{m time}^2\) times the strictly negative minor
in (3), plus \(o(t_{m time}^2)\). It remains negative for sufficiently
small positive time. \(\square\)

Consequently the usual Karlin--Gantmacher variation-diminishing theorem
cannot be used to declare \(r_1\) the first even excited state. This result
does not refute the quotient floor: it only prevents importing an
oscillation ordering whose hypothesis is false.

## 2. Surviving use of the threshold state

The exact eigen-equation

\[
Lr_1=\frac12(r_1-\mu_K(r_1))                           \tag{4}
\]

still supplies the sharp upper bound \(\lambda_{\rm gap}\le1/2\). Any lower
bound must use the orthogonality conditions of 106.41(5) or a signed
factorization of the integrated curvature. Nodal counting without a
variation-diminishing kernel does not order the spectrum.

The next admissible target remains the full constrained curvature form

\[
\|Lq\|^2-\frac12\langle q,Lq\rangle,
\qquad q\perp1\oplus\mathcal R,                       \tag{5}
\]

with the ordinary arithmetic jet
\(j_2=\delta\Lambda+\Lambda*\Lambda\), Gamma and the polar term combined
before estimating their sign.
