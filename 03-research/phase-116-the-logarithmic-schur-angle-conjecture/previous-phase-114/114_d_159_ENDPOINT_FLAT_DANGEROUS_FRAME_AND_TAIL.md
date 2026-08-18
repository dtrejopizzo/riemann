# D.159 — Endpoint-flat dangerous frame and rigorous Fourier tail

## Verdict

The delicate five-dimensional coordinate block can be chosen inside an
endpoint-flat polynomial subspace without losing the safe finite gap.  This
removes the slow (1/|\tau|) Fourier tail which made a direct interval
moment calculation impractical.

For (N=170), (m=20), define

\[
 \mathcal E_{m,N}=
 \left\{(T^2-t^2)^mP(t):\deg P\le N-1-2m\right\}.       \tag{0.1}
\]

Every (F\in\mathcal E_{m,N}) satisfies

\[
 F^{(r)}(\pm T)=0,\qquad0\le r<m.                      \tag{0.2}
\]

The floating selector on
(\mathcal E_{20,170}\cap\ker M_-\cap\ker M_+) gives five low
directions.  Their orthogonal complement inside (V_{170}) has finite
compression gap

\[
 5.851597\times10^{-2}.                                \tag{0.3}

\]

Thus they may replace the original non-flat eigenvector selector in the
hierarchical congruence of D.157.  The replacement is only a frozen change
of coordinates; it does not restrict the primitive test space.

For every (1\le j\le4), the omitted joint-multiplier moment above a
cutoff (R\ge150) has the explicit bound (3.5) below.  With (m=20) and
(R=4096), the floating size estimate for the worst (j=4) tail is below
(1.1\times10^{-27}).  The final certificate must replace the derivative
norm in that estimate by its Arb upper endpoint.

No paper file is modified.

## 1. Exact flat subspace

Multiplication by ((T^2-t^2)^m) is injective on polynomials of degree at
most (N-1-2m).  Hence

\[
 \dim\mathcal E_{m,N}=N-2m.                            \tag{1.1}
\]

The factor has a zero of order (m) at both endpoints, which proves
(0.2).  Intersecting with the two independent Tate moments leaves dimension

\[
 N-2m-2.                                               \tag{1.2}
\]

For (N=170,m=20), this is 128, more than enough to choose the five
dangerous coordinates.

The basis used for stable numerical selection is

\[
 (1-u^2)^m C_k^{2m+1/2}(u),\qquad u=t/T,               \tag{1.3}
\]

where \(C_k^{2m+1/2}\) is the Gegenbauer polynomial.  These columns are
orthogonal in unweighted \(L^2[-1,1]\), because their product contains the
Gegenbauer weight \((1-u^2)^{2m}\).  Formula (1.3) retains the endpoint
factor symbolically.  It must not be replaced by a
binary64-expanded Legendre polynomial when certifying (0.2).

## 2. Selection audit

After imposing both Tate moments, the first five Ritz values in the flat
subspace are

\[
\begin{aligned}
 &3.03528\times10^{-11},\quad
 6.29201\times10^{-9},\quad
 2.36788\times10^{-6},\\
 &1.60173\times10^{-4},\quad
 1.23023\times10^{-2}.                                 \tag{2.1}
\end{aligned}

The smallest singular values between their span and the first five
ordinary constrained Ritz directions are, in descending order,

\[
 1,quad1,quad0.99999994,quad0.99937048,quad0.99597231.          \tag{2.2}
\]

Completing these five flat columns to a basis of (V_{170}), the safe
finite compression begins with

\[
 0.05851597,quad0.59459908,quad0.75699550,quad0.84847720.        \tag{2.3}
\]

These are selection data only.  In the directed calculation the
Gegenbauer coefficients are rounded to exact dyadics, the two Tate
coordinates are eliminated by Arb, and (2.3) is replaced by a Gershgorin
congruence.

## 3. Tail theorem

Repeated integration by parts and (0.2) give, for real (\tau\ne0),

\[
 |\widehat F(\tau)|
 \le {\|F^{(m)}\|_{L^1(-T,T)}\over|\tau|^m}
 \le {\sqrt{2T}\,\|F^{(m)}\|_2\over|\tau|^m}.          \tag{3.1}
\]

For the complete endpoint multiplier

\[
 r_T(\tau)=\operatorname {Re}\psi
 \left({1\over4}+{i\tau\over2}\right)-\log\pi
 -2\sum_{n=2,3,4}{\Lambda(n)\over\sqrt n}
 \cos(\tau\log n),                                    \tag{3.2}
\]

the same directed digamma remainder used in D.91 and the triangle
inequality imply, for (\tau\ge150),

\[
 |r_T(\tau)|\le\log\tau+5.                            \tag{3.3}

\]

Indeed, the three doubled contact amplitudes sum to less than (2.95),
(log\pi<1.15), and the (1/(2z)) plus digamma remainder contributes
less than (0.01); the constant five is outwardly generous.

For (a=2m>1), (L=\log R+5), and an integer (j\ge0), direct
integration after (\tau=Re^x) gives

\[
 \int_R^\infty{(\log\tau+5)^j\over\tau^{a}}\,d\tau
 =R^{1-a}\sum_{\ell=0}^j
 {j\choose\ell}{L^{j-\ell}\ell!\over(a-1)^{\ell+1}}. \tag{3.4}

Combining (3.1)--(3.4), the two-sided Fourier moment tail is bounded by

\[
\boxed{
 {2T\|F^{(m)}\|_2^2\over\pi}
 R^{1-2m}\sum_{\ell=0}^j
 {j\choose\ell}{(\log R+5)^{j-\ell}\ell!
 \over(2m-1)^{\ell+1}}.}                              \tag{3.5}


The same formula polarizes to a cross moment by Cauchy--Schwarz, using the
geometric mean of the two diagonal tail bounds.

## 4. Consequence for the directed computation

The finite interval ([0,4096]) is integrated with the analytic Arb
Fourier representation of D.158.  The tail is then inserted as a symmetric
ball using (3.5).  Because the five dangerous columns retain the factor in
(0.1), no cancellation of huge endpoint derivatives is used to justify the
tail.

`114_d_159_endpoint_flat_tail_verify.py` checks the exact vanishing,
dimension count, integral identity (3.4), and the quoted numerical tail
scale.
