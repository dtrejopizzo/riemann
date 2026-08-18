# 106.104 — The theta-divisor current normal form

## 1. Purpose and verdict

The complete theta lift of 106.38 and 106.65 keeps every ordinary-prime
edge, but its prime-power index and its theta index remain separate.  This
note performs a different exact regrouping.  The theta atom at the endpoint
farther from the origin is used as the outer index.  For a fixed integer
theta atom \(b\), the prime-power translations which reach it are precisely
the prime-power divisors of \(b\).  Their total incoming weight is

\[
 \sum_{n\mid b}\Lambda(n)=\log b.
 \tag{1}
\]

Consequently the full ordinary-prime energy admits an exact orthogonal
decomposition into a divisor current and a divisor dispersion.  This
regrouping retains the divisible, nondivisible/fractional and central
crossing channels of 106.38; Gamma and the polar threshold remain coupled
through the signed continuous displacement measure.

The identity is rigorous and globally signed.  It does not by itself prove
the physical surplus.  In fact, the divisor dispersion is strictly positive
on an exact radical multiplier, so a proof which keeps only the averaged
divisor current necessarily loses sharpness.  Any successful use of the
normal form must retain the current and its dispersion jointly with Gamma
and the pole.

No zero location is used below.

## 2. Theta scaling in the farther-endpoint coordinate

Retain the continuous theta atoms

\[
 k_m(x)=m^{-1/2}k_1(x+\log m),
 \qquad K(x)=\sum_{m\geq1}k_m(x)\quad(x\geq0).
 \tag{2}
\]

For \(n\geq2\), direct substitution gives the two identities

\[
 \boxed{
 k_m(y+\log n)=\sqrt n\,k_{nm}(y),
 \qquad
 k_m(\log n-x)=\sqrt n\,k_{nm}(-x).}
 \tag{3}
\]

The second identity will only be used for \(0\leq x\leq\log n\).  On this
domain \(nm e^{-x}\geq m\geq1\), and hence every atom on its right-hand side
is positive.  Thus all changes in summation order below are justified by
Tonelli's theorem.

For an even multiplier \(r\), put

\[
 \Delta_n^+r(y)=r(y+\log n)-r(y),
 \qquad
 \Delta_{n,x}^-r=r(\log n-x)-r(x).
 \tag{4}
\]

The superscripts refer respectively to same-side and central-crossing
edges.

## 3. Exact reindexing of the ordinary-prime form

Write

\[
 \mathscr E_p(r)
 =\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
   \mathcal J_{\log n}(r).
 \tag{5}
\]

The exact fold of 106.66 gives

\[
\begin{aligned}
 \mathscr E_p^{\rm ss}(r)
 &=2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
   \int_0^\infty K(y+\log n)K(y)
       |\Delta_n^+r(y)|^2\,dy,\\
 \mathscr E_p^{\rm ctr}(r)
 &=\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
   \int_0^{\log n}K(x)K(\log n-x)
       |\Delta_{n,x}^-r|^2\,dx,
\end{aligned}
\tag{6}
\]

and \(\mathscr E_p=\mathscr E_p^{\rm ss}+\mathscr E_p^{\rm ctr}\).

### Theorem 1 — Farther-theta-index reindexing

For every even multiplier in the full-kernel form domain,

\[
\boxed{
\begin{aligned}
 \mathscr E_p^{\rm ss}(r)
 &=2\int_0^\infty K(y)
   \sum_{b\geq2} k_b(y)
   \sum_{\substack{n\mid b\\ n\geq2}}
       \Lambda(n)|\Delta_n^+r(y)|^2\,dy,\\
 \mathscr E_p^{\rm ctr}(r)
 &=\int_0^\infty K(x)
   \sum_{b\geq2} k_b(-x)
   \sum_{\substack{n\mid b\\ \log n\geq x}}
       \Lambda(n)|\Delta_{n,x}^-r|^2\,dx.
\end{aligned}}
\tag{7}
\]

In the second line a summand is present only when \(\Lambda(n)>0\); in
particular \(b\geq n\geq e^x\), so the displayed theta atom is positive.

#### Proof

Expand the farther endpoint in the first line of (6).  By (3),

\[
 \frac{\Lambda(n)}{\sqrt n}K(y+\log n)
 =\Lambda(n)\sum_{m\geq1}k_{nm}(y).
 \tag{8}
\]

Set \(b=nm\) and regroup the nonnegative summands.  This gives the first
line of (7).  Likewise,

\[
 \frac{\Lambda(n)}{\sqrt n}K(\log n-x)
 =\Lambda(n)\sum_{m\geq1}k_{nm}(-x).
 \tag{9}
\]

The integration condition \(0\leq x\leq\log n\) becomes
\(\log n\geq x\).  Setting \(b=nm\) gives the second line.  No theta atom
has been discarded in either calculation.  \(\square\)

Formula (7) is another exact realization of all three prime channels in
106.38.  The earlier divisible/fractional split fixes the near endpoint
and compares integer with rational theta indices.  Formula (7) instead
fixes the farther integer endpoint \(b\).  These are two coordinate systems
on the same full edge measure.

## 4. Divisor currents and their exact dispersions

For \(b\geq2\), define the complete incoming degree

\[
 \ell_b=\sum_{n\mid b}\Lambda(n)=\log b
 \tag{10}
\]

and, for \(0\leq x\leq\log b\), the active central degree

\[
 \ell_b(x)=
 \sum_{\substack{n\mid b\\ \log n\geq x}}\Lambda(n).
 \tag{11}
\]

Terms with \(\ell_b(x)=0\) are omitted.  Define the signed divisor currents

\[
\begin{aligned}
 D_b^+r(y)
 &=\frac1{\log b}
   \sum_{n\mid b}\Lambda(n)\Delta_n^+r(y),\\
 D_{b,x}^-r
 &=\frac1{\ell_b(x)}
   \sum_{\substack{n\mid b\\\log n\geq x}}
      \Lambda(n)\Delta_{n,x}^-r.
\end{aligned}
\tag{12}
\]

Their conditional dispersions are

\[
\begin{aligned}
 V_b^+(r;y)
 &=\frac1{2\log b}
   \sum_{n,m\mid b}\Lambda(n)\Lambda(m)
   |r(y+\log n)-r(y+\log m)|^2,\\
 V_{b,x}^-(r)
 &=\frac1{2\ell_b(x)}
   \sum_{\substack{n,m\mid b\\
          \log n,\log m\geq x}}
   \Lambda(n)\Lambda(m)
   |r(\log n-x)-r(\log m-x)|^2.
\end{aligned}
\tag{13}
\]

The convention \(\Lambda(1)=0\) is understood in (10)--(13).

### Theorem 2 — Exact theta-divisor current decomposition

One has

\[
\boxed{
\begin{aligned}
 \mathscr E_p^{\rm ss}(r)
 &=2\int_0^\infty K(y)\sum_{b\geq2}k_b(y)
   \left\{\log b\,|D_b^+r(y)|^2+V_b^+(r;y)\right\}dy,\\
 \mathscr E_p^{\rm ctr}(r)
 &=\int_0^\infty K(x)\sum_{b\geq2}k_b(-x)
   \left\{\ell_b(x)|D_{b,x}^-r|^2+V_{b,x}^-(r)\right\}dx.
\end{aligned}}
\tag{14}
\]

#### Proof

For positive weights \(w_j\), \(W=\sum_jw_j\), and vectors \(z_j\) in a
complex Hilbert space, the finite weighted ANOVA identity is

\[
 \sum_jw_j|z_j|^2
 =W\left|\frac1W\sum_jw_jz_j\right|^2
  +\frac1{2W}\sum_{j,k}w_jw_k|z_j-z_k|^2.
 \tag{15}
\]

Apply (15) to the inner sums in (7).  In the same-side line use (10); in
the central line use (11).  This gives (14).  \(\square\)

The terms \(V_b^+\) and \(V_{b,x}^-\) are genuine cross-prime-power
interactions.  They are not sums of independent single-tower cumulants:
for a theta endpoint divisible by powers of several primes, (13) compares
all corresponding translated spatial values before any absolute estimate.

## 5. The globally signed physical normal form

Put

\[
 d\kappa(u)=
 \left\{\frac{e^{-u/2}}{1-e^{-2u}}-2\cosh(u/2)\right\}du.
 \tag{16}
\]

Combining Theorem 2 with the exact common-displacement identity of 106.66
gives the following normal form.

### Corollary 3 — Prime, Gamma and pole before a sign estimate

For every even multiplier in the full-kernel form domain,

\[
\boxed{
\begin{aligned}
 QW(Kr,Kr)
={}&\int_0^\infty\mathcal J_u(r)\,d\kappa(u)\\
 &+2\int_0^\infty K(y)\sum_{b\geq2}k_b(y)
   \left\{\log b\,|D_b^+r(y)|^2+V_b^+(r;y)\right\}dy\\
 &+\int_0^\infty K(x)\sum_{b\geq2}k_b(-x)
   \left\{\ell_b(x)|D_{b,x}^-r|^2+V_{b,x}^-(r)\right\}dx.
\end{aligned}}
\tag{17}
\]

Equivalently, (17) is the exact pairing

\[
 QW(Kr,Kr)=\int_0^\infty\mathcal J_u(r)\,d\sigma(u)
 \tag{18}
\]

of 106.66, with every ordinary von Mangoldt atom resolved by its farther
theta endpoint and by its complete divisor covariance.  Thus Gamma, the
pole, all prime powers, the nondivisible theta indices and the central
crossing region are present simultaneously in (17).

The continuous measure \(d\kappa\) is signed.  Therefore (17) is not a
sum-of-squares proof of \(QW\geq0\); it is a signed normal form in which the
only unsquared part is precisely the jointly completed Gamma--pole channel.

## 6. Radical annihilation and the current-only obstruction

For the exact radical multipliers

\[
 r_j=K^{(2j)}/K,
 \tag{19}
\]

the full-kernel identity gives

\[
 QW(Kr_j,Kr_j)=0.
 \tag{20}
\]

Hence (17) gives an exact cancellation of the signed continuous channel
against all four nonnegative divisor pieces.  This immediately tests any
attempt to retain only the averaged currents.

### Proposition 4 — Divisor averaging alone cannot be sharp

For every ordinary prime \(p\), the same-side dispersion at the theta atom
\(b=p^2\) is

\[
 \boxed{
 V_{p^2}^+(r;y)
 =\frac{\log p}{2}
   |r(y+\log p)-r(y+2\log p)|^2.}
 \tag{21}
\]

In particular,

\[
 \int_0^\infty K(y)k_{p^2}(y)V_{p^2}^+(r_j;y)\,dy>0
 \tag{22}
\]

for every nonconstant radical multiplier \(r_j\).  Consequently, replacing
the complete prime form in (14) by its current-square parts alone produces
a strictly negative defect on \(r_j\) after the unchanged Gamma--pole
channel is added.  Such a current-only estimate cannot prove the sharp
physical surplus.

#### Proof

The prime-power divisors of \(p^2\) carrying nonzero von Mangoldt weight are
\(p\) and \(p^2\), both with weight \(\log p\).  Formula (21) follows from
(13).  If (22) vanished, analyticity and positivity of \(Kk_{p^2}\) would
give

\[
 r_j(y+\log p)=r_j(y+2\log p)
 \quad(y\geq0).
\]

Analytic continuation would make \(r_j\) periodic with period \(\log p\).
The theta asymptotics used in 106.65 show that every nonconstant
\(K^{(2j)}/K\) is unbounded at \(+\infty\), so this is impossible.  Thus
(22) is strict.  Finally, (20) says that the continuous signed channel
cancels the complete prime form.  Deleting the strictly positive
dispersion while leaving that channel unchanged makes the resulting value
strictly negative.  \(\square\)

This is stronger than the observation that Jensen may lose a constant.
It identifies the exact missing quantity: the cross-divisor dispersion in
(13) is load-bearing on the equality family.

## 7. Consequence for the heat and hybrid rows

For a positive heat or hybrid trace-class state
\(\Gamma_t=\sum_j\gamma_j|r_j\rangle\langle r_j|\), integrate (17) against
the spectral weights \(\gamma_j\).  Tonelli's theorem applies to every
nonnegative divisor term, and the signed continuous term is assembled by
the common cutoff used in 106.102.  This gives the exact trace version of
(17), whose left side is

\[
 \mathrm{Tr}\,\{(A-\tfrac12I)\Gamma_t\}.
 \tag{23}
\]

Therefore the cofinal signed heat-alignment lemma of 106.102 is equivalent
to proving that the right side of the trace-lifted (17) is
\(-o(\mathrm{Tr}\,\Gamma_t)\) from below along an unbounded sequence.
The divisor identity (1) does not supply that sign automatically: it
orthogonally resolves the full literal prime contribution, and Proposition
4 proves that both its current and dispersion pieces must remain coupled
to Gamma and the pole.

## 8. Status

Proved here:

* the exact farther-theta-index reindexing (7);
* the exact divisor-current and cross-divisor-dispersion identity (14);
* the globally signed ordinary-prime--Gamma--pole normal form (17);
* strict load-bearing of the cross-divisor dispersion on the radical
  equality family.

Not proved here:

\[
 QW(Kr,Kr)\geq0
\]

on the physical complement, or its cofinal heat-state version.  The new
normal form shows that a successor must estimate the continuous signed
channel against the divisor current and the cross-divisor dispersion
jointly.  A contraction using only the averaged current is rigorously
excluded by Proposition 4.
