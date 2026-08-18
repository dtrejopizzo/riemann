# 106.44 — The PNT tail threshold and the arithmetic resonance equation

## Purpose

The full generator of 106.41 is nonnegative, but nonnegativity does not
explain why its spectrum should avoid the interval \((0,1/2)\).  This note
locates the number \(1/2\) directly on the ordinary-prime side.  The prime
measure is decomposed, exactly, as

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}
 =e^{t/2}\,dt+d\omega(t),
 \qquad
 d\omega(t)=e^{-t/2}\,d\bigl(\psi(e^t)-e^t\bigr).       \tag{1}
\]

The continuum part has an exact tail action.  On every even centered
multiplier of at most exponential growth it is \(\frac12 I\), modulo a
double-exponentially small tail.  The Gamma channel is exponentially
smaller there.  Consequently a subthreshold state can only be produced by
one coherent resonance of the literal signed discrepancy \(d\omega\).

This is an operator statement.  It does not insert a formula over zeros and
does not replace the ordinary weights by a model.

## 1. Exact prime-continuum decomposition

Let

\[
 c=c_K=\frac12,\qquad h(x)=\cosh(x/2),                 \tag{2}
\]

and denote by \(L_p\) the prime part of the generator in 106.41(7).  Thus

\[
\begin{aligned}
 (L_pq)(x)=\frac{c}{h(x)}\int_{(0,\infty)}
 &\{K(x-t)[q(x)-q(x-t)]\\
 &+K(x+t)[q(x)-q(x+t)]\}\,d\nu_p(t),                 \tag{3}
\end{aligned}
\]

where

\[
 d\nu_p(t)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
             \delta_{\log n}(dt)
          =e^{-t/2}\,d\psi(e^t).                     \tag{4}
\]

Put

\[
 d\nu_0(t)=e^{t/2}\,dt,
 \qquad d\omega(t)=d\nu_p(t)-d\nu_0(t).              \tag{5}
\]

Since \(d(e^t)=e^t\,dt\), (1) follows exactly.  Let \(L_0\) and
\(R_\psi\) be the operators obtained from (3) by replacing \(d\nu_p\)
with \(d\nu_0\) and \(d\omega\), respectively.  Then, on the common form
core,

\[
 \boxed{L_p=L_0+R_\psi.}                              \tag{6}
\]

No prime-number-theorem estimate is used in (6).

## 2. Closed form of the continuum operator

For a function for which the following integrals converge, changes of
variable \(y=x-t\) and \(y=x+t\) give

\[
\boxed{
\begin{aligned}
 (L_0q)(x)=\frac{c}{h(x)}\Bigg[&e^{x/2}
   \int_{-\infty}^{x}e^{-y/2}K(y)[q(x)-q(y)]\,dy\\
 &+e^{-x/2}
   \int_x^\infty e^{y/2}K(y)[q(x)-q(y)]\,dy\Bigg].    \tag{7}
\end{aligned}}
\]

The diagonal mass in the first integral is

\[
 \int_{\mathbb R}e^{-y/2}K(y)\,dy
 =\int_{\mathbb R}\cosh(y/2)K(y)\,dy=c=\frac12,      \tag{8}
\]

because \(K\) is even.  Thus the spectral number \(1/2\) is already
encoded in the PNT continuum and the polar normalization; it is not an
externally chosen comparison constant.

### Theorem 1 — Exact continuum tail threshold

Assume that \(q\) is even, centered in \(L^2(\mu_K)\), and satisfies
\(|q(x)|\le C\exp(A|x|)\) for some finite \(A\).  Then, for every
\(B>0\),

\[
 \boxed{(L_0q)(x)=\frac12q(x)+O_{q,B}(e^{-Bx})
        \qquad(x\to+\infty).}                         \tag{9}
\]

The same statement holds at \(-\infty\) by evenness.

#### Proof

Centering and evenness imply

\[
\begin{aligned}
 0=c\int q\,d\mu_K
 &=\int h(y)K(y)q(y)\,dy\\
 &=\int e^{-y/2}K(y)q(y)\,dy,                         \tag{10}
\end{aligned}
\]

because the integral of \(\sinh(y/2)K(y)q(y)\) vanishes.  Introduce

\[
\begin{aligned}
 A_-(x)&=\int_{-\infty}^xe^{-y/2}K(y)\,dy,&
 B_-(x)&=\int_{-\infty}^xe^{-y/2}K(y)q(y)\,dy,\\
 A_+(x)&=\int_x^\infty e^{y/2}K(y)\,dy,&
 B_+(x)&=\int_x^\infty e^{y/2}K(y)q(y)\,dy.
                                                               \tag{11}
\end{aligned}
\]

Equation (8) and (10) give

\[
 A_-(x)=c-\int_x^\infty e^{-y/2}K(y)\,dy,
 \qquad
 B_-(x)=-\int_x^\infty e^{-y/2}K(y)q(y)\,dy.          \tag{12}
\]

Riemann's theta formula for \(K\) gives, for every \(D>0\),

\[
 K(y)(1+|q(y)|)=O_{q,D}(e^{-Dy})\qquad(y\to+\infty). \tag{13}
\]

Substitute (11)--(12) in (7).  The coefficient of \(q(x)\) is

\[
 \frac{c e^{x/2}}{h(x)}A_-(x)
 +\frac{c e^{-x/2}}{h(x)}A_+(x)
 =2c^2+O_B(e^{-Bx})=\frac12+O_B(e^{-Bx}),             \tag{14}
\]

while every term containing \(B_-\), \(B_+\), or a tail in (12) is
\(O_{q,B}(e^{-Bx})\), again by (13).  This proves (9). \(\square\)

## 3. Gamma is not the tail threshold

Let \(L_\Gamma\) denote the continuous Gamma part of 106.41(7), whose
jump density is

\[
 g(t)=\frac{e^{-t/2}}{1-e^{-2t}}.                     \tag{15}
\]

### Theorem 2 — Gamma tail decay

Under the assumptions of Theorem 1, and assuming the same exponential
growth bound for the first derivative of \(q\),

\[
 \boxed{(L_\Gamma q)(x)
 =O_q\bigl(e^{-x}(1+|q(x)|)\bigr)+O_{q,B}(e^{-Bx})}
 \qquad(x\to+\infty)                                 \tag{16}
\]

for every fixed \(B>0\), after increasing the implicit constant in the
second term.

#### Proof

Split the backward integral into \(0<t<x/2\), \(x/2<t<3x/2\), and
\(t>3x/2\).  In the first range both translated theta factors lie in a
double-exponential tail.  In the middle range \(g(t)=O(e^{-t/2})\), and
the outside factor is \(c/h(x)=O(e^{-x/2})\), giving
\(O_q(e^{-x}(1+|q(x)|))\) after the substitution \(y=x-t\).  In the
last range the same two exponentials give that bound, while the translated theta kernel
controls the remaining \(y\)-integral.  The forward integral is smaller:
\(K(x+t)\) is double-exponentially decreasing uniformly in \(t>0\).
The singularity \(g(t)=1/(2t)+O(1)\) at zero is cancelled by
\(q(x)-q(x\pm t)=O_q(t)\) on the smooth core.  Closure gives (16) on the
stated tail class. \(\square\)

Thus Gamma is essential to the global identity and to the small-jump form,
but it does not create the asymptotic value \(1/2\).

## 4. The exact arithmetic resonance equation

The discrepancy operator in (6) is

\[
\boxed{
\begin{aligned}
 (R_\psi q)(x)=\frac{c}{h(x)}
 \int_{(0,\infty)}&\{K(x-t)[q(x)-q(x-t)]\\
 &+K(x+t)[q(x)-q(x+t)]\}
 e^{-t/2}\,dE(t),                                    \tag{17}
\end{aligned}}
\]

where

\[
 E(t)=\psi(e^t)-e^t.                                  \tag{18}
\]

Formula (17) retains the prime jumps and the negative continuous drift in
one Stieltjes integral.  In particular it is not an absolute PNT error
bound.

### Corollary 3 — Necessary resonance for a subthreshold state

Let \(q\) satisfy the assumptions of Theorem 1 and the eigenvalue equation

\[
 (L_0+R_\psi+L_\Gamma)q=\lambda q,
 \qquad 0<\lambda<\frac12.                            \tag{19}
\]

Then

\[
 \boxed{R_\psi q(x)=-(\tfrac12-\lambda)q(x)
        +O_q\bigl(e^{-x}(1+|q(x)|)\bigr)
        +O_{q,B}(e^{-Bx}).}                            \tag{20}
\]

Hence the open interval \((0,1/2)\) is not produced by the continuum or
by Gamma.  It is equivalent, at the level of a bound state, to a coherent
negative feedback of the literal ordinary-prime discrepancy on both tails.

#### Proof

Subtract (9) and (16) from (19). \(\square\)

## 5. Interaction with radical shorting

On the exact shorted complement, 106.43 gives

\[
 F=hq,
 \qquad F*K=0.                                        \tag{21}
\]

Consequently a subthreshold state must satisfy simultaneously the two
equations

\[
\boxed{
 F*K=0,
 \qquad
 R_\psi(F/h)=-(\tfrac12-\lambda)F/h
 +O(e^{-|x|}(1+|F/h|))+O_B(e^{-B|x|})
 \quad\text{in both tails}.}                          \tag{22}
\]

The first is a global mean-periodicity constraint fixed by Riemann's theta
kernel.  The second is a one-sided arithmetic resonance constraint fixed by
the actual von Mangoldt weights.  Neither condition alone excludes a
subthreshold state; their incompatibility is the remaining theorem.

For an elementary mean-periodic mode

\[
 F_z(x)=\cos(zx),\qquad q_z(x)=\frac{\cos(zx)}{h(x)}, \tag{23}
\]

with \(z=\gamma+i\eta\) and \(|\eta|<1/2\), one has

\[
 |q_z(x)|\asymp e^{-(1/2-|\eta|)x}
\quad\text{along a relatively dense sequence of }x.  \tag{24}
\]

Thus (20) requires the smoothed prime discrepancy to reproduce the same
frequency \(\gamma\) and the same exponential rate.  A pointwise PNT
remainder, which is only subexponentially small after relative
normalization, cannot decide (20): it is larger than the exponentially
decaying right side of (24).  The needed estimate must use the signed
phase in (17) and the convolution equation (21) together.

## 6. The new closing target

The preceding calculation identifies a non-circular form of the desired
arithmetic statement.

> **Tail-resonance exclusion.**  There is no nonzero even centered
> \(q\) in the full form domain, with a regular exponential tail of rate
> strictly below one, such that \((hq)*K=0\) and, for some
> \(\delta>0\),
> \[
>  R_\psi q=-\delta q+o(q)
> \]
> in both tails.

If this statement is proved, Corollary 3 excludes every eigenvalue in
\((0,1/2)\).  Conversely, any subthreshold eigenfunction supplies such a
resonance with \(\delta=1/2-\lambda\).

The gain over the unrestricted Poincare formulation is that the number
\(1/2\) and the possible defect are now separated algebraically:

\[
 \boxed{\text{PNT continuum}=\tfrac12 I,
 \qquad \text{Gamma}=o(1),
 \qquad \text{only }d(\psi(e^t)-e^t)\text{ can bind}.} \tag{25}
\]

The next calculation must act on (17) under (21), before taking any
absolute value.  Positivity of \(\Lambda\) by itself is insufficient,
because it is destroyed by the exact subtraction in (1); the additional
usable structure is the multiplicative relation
\(\Lambda=-\mu*\log\), equivalently the spatial Möbius--theta identities
of 106.40.
