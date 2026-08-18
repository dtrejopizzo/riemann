# A1 kernel factorization attempt: canonical trivial zeros and square no-go

## Verdict

This note tests three possible sources of a positive, non-circular
factorization of

\[
 D_n=2\lambda_n-\lambda_n^{\rm arch}
\]

or of its first difference: the trivial-zero factors of
\(h(t)=\log(t\zeta(1+t))\), a positive mixture of logarithmic factors, and
a phase-averaged square of the von Mangoldt Dirichlet series.

None gives the missing sign.  Two exact obstructions are proved.

1.  The apparently positive contribution
    \(1-(1-1/a)^n\) of a trivial zero is not summable over the trivial
    zeros.  After the mandatory genus-one normalization its convergent
    contribution is
    \[
      1-(1-1/a)^n-n/a<0\qquad(n\ge2).
    \]
2.  No representation of \(h\), up to an affine function, as a positive
    mixture of the factors \(\log(1+tx)\) can exist.  An explicit exact
    certificate is
    \[
      h^{(101)}(100/\log2)<0,
    \]
    whereas every such positive mixture would make this derivative
    nonnegative.

The von Mangoldt series itself is an exact Hilbert-space square, but the
Laguerre pullback is not positivity preserving; already its \(n=1\)
image is strictly negative for \(a\ge1/\log2\).  These statements rule out
the corresponding factorization mechanisms, not A1.  No assertion of A1
or RH is made.

## 1. The canonical trivial-zero calculation

Put

\[
 q(t)=t\zeta(1+t),\qquad h(t)=\log q(t).
\tag{1}
\]

The pole at \(t=0\) is removable, \(q(0)=1\), and the trivial zeros of
\(q\) are

\[
 t=-a,\qquad a=3,5,7,\ldots .
\tag{2}
\]

Since \(q\) is an entire function of order one, the canonical factor
belonging to the zero \(-a\) is

\[
 E_1(-t/a)=(1+t/a)e^{-t/a}.
\tag{3}
\]

For \(|t|<a\), its logarithm is

\[
 \log E_1(-t/a)
 =\log(1+t/a)-t/a
 =\sum_{k\ge2}{(-1)^{k+1}\over k a^k}t^k.
\tag{4}
\]

Recall the exact binomial transform used for the prime part,

\[
 P_n=n\sum_{k=1}^n {n-1\choose k-1}p_k,
 \qquad h(t)=\sum_{k\ge1}p_kt^k.
\tag{5}
\]

Using \(\frac nk{n-1\choose k-1}={n\choose k}\), the contribution of
(3) to (5) is therefore

\[
 \begin{aligned}
 \tau_n(a)
 &=\sum_{k=2}^n(-1)^{k+1}{n\choose k}a^{-k}\\
 &=1-(1-1/a)^n-{n\over a}.
 \end{aligned}
\tag{6}
\]

For \(n\ge2\) and \(a>1\), strict Bernoulli convexity gives
\((1-1/a)^n>1-n/a\).  Hence

\[
 \boxed{\quad \tau_n(a)<0\quad(n\ge2).\quad}
\tag{7}
\]

Moreover \(\tau_n(a)=O_n(a^{-2})\), directly from the finite sum in
(6), so

\[
 T_n^{\rm triv}:=\sum_{a=3,5,7,\ldots}\tau_n(a)
\tag{8}
\]

converges absolutely and is strictly negative for every \(n\ge2\).

This sign is easy to miss if the exponential in (3) is dropped.  The
uncanonical factor \(1+t/a\) would contribute

\[
 \sigma_n(a)=1-(1-1/a)^n>0.
\tag{9}
\]

But \(\sigma_n(a)=n/a+O_n(a^{-2})\), and consequently its sum over odd
\(a\) diverges.  The divergent linear part cannot be assigned to the
trivial zeros one at a time.  The genus-one exponential subtracts exactly
\(n/a\) and changes the sign from (9) to (7).  Thus (9) is not a valid
positive margin in the infinite product.

The interaction with the archimedean term can also be written exactly.
Let

\[
 c={\gamma+\log(4\pi)\over2}.
\]

The odd-index formula already proved in the phase is

\[
 A_n=1-cn+\sum_{\ell\ \mathrm{odd}}
 \left((1-1/\ell)^n-1+{n\over\ell}\right).
\tag{10}
\]

The \(\ell=1\) summand equals \(n-1\).  For every odd \(\ell\ge3\), the
summand is \(-\tau_n(\ell)\).  Therefore

\[
 \boxed{\quad A_n=n(1-c)-T_n^{\rm triv}.\quad}
\tag{11}
\]

In particular, the canonical trivial-zero block in \(P_n\) does not add
a hidden positive reserve to \(A_n+2P_n\): after (11) one copy of the
strictly negative block (8) remains.  Any allocation based on (9) instead
merely moves a divergent linear quantity between the canonical
exponential and the zero factors.

## 2. Exact obstruction to a positive logarithmic mixture

The preceding calculation suggests the more flexible ansatz

\[
 h(t)=\alpha+\beta t+
 \int_{(0,\infty)}\bigl(\log(1+tx)-c(t,x)\bigr)\,d\mu(x),
\tag{12}
\]

where \(\mu\ge0\), and where \(c(t,x)\) is affine in \(t\) and supplies
whatever genus-one subtraction is needed.  Assume only the local
integrability required to differentiate (12) 101 times at the point in
question.  Since the affine terms disappear, (12) necessarily implies

\[
 (-1)^k h^{(k+1)}(t)
 =k!\int_{(0,\infty)}{x^{k+1}\over(1+tx)^{k+1}}\,d\mu(x)\ge0
 \quad(k\ge1,t>0).
\tag{13}
\]

The actual Euler series gives an exact contradiction.  For \(t>0\),
absolute convergence permits arbitrary fixed differentiation and yields

\[
 h'(t)={1\over t}+{\zeta'\over\zeta}(1+t)
 ={1\over t}-\sum_{m\ge2}{\Lambda(m)\over m^{1+t}},
\tag{14}
\]

and hence

\[
 (-1)^k h^{(k+1)}(t)
 ={k!\over t^{k+1}}-
 \sum_{m\ge2}{\Lambda(m)(\log m)^k\over m^{1+t}}.
\tag{15}
\]

Take \(k=100\) and \(t_0=100/\log2\).  Retaining only the \(m=2\)
term in the nonnegative sum gives

\[
 h^{(101)}(t_0)
 \le (\log2)^{101}
 \left({100!\over100^{101}}-{e^{-100}\over2}\right).
\tag{16}
\]

For completeness, the bracket is strictly negative by an elementary
factorial estimate.  Concavity of \(\log x\) implies, on summing the
trapezoid lower bounds on \([j,j+1]\),

\[
 \int_1^k\log x\,dx
 \ge\sum_{j=2}^{k-1}\log j+{1\over2}\log k.
\]

Adding \(\log k\) and exponentiating gives

\[
 k!\le e\,k^{k+1/2}e^{-k}.
\tag{17}
\]

Also \(e<3\), since
\(e=1+1+\sum_{j\ge2}1/j!<2+\sum_{j\ge2}2^{1-j}=3\).
At \(k=100\), (17) therefore gives

\[
 {100!\over100^{101}}
 \le {e\over10}e^{-100}
 <{1\over2}e^{-100}.
\tag{18}
\]

Equations (16)--(18) prove the promised exact certificate

\[
 \boxed{\quad h^{(101)}(100/\log2)<0.\quad}
\tag{19}
\]

This contradicts (13), whose sign is positive because \(k=100\).  Thus no
positive logarithmic-factor mixture (12), canonical or uncanonical, can
represent the actual completed pole--prime germ.

There is an equivalent variation-measure interpretation.  Equation (14)
is the Laplace transform of the signed, locally finite measure

\[
 d\nu(u)=du-\sum_{m\ge2}{\Lambda(m)\over m}\,\delta_{\log m}(du).
\tag{20}
\]

It contains the negative atom \(-\frac{\log2}{2}\delta_{\log2}\).
Formula (19) is a quantitative way of concentrating a Laplace moment near
that atom.  Therefore the pole--prime collision cannot be turned into a
positive measure merely by rewriting its Laplace transform.  Integrating
(20) once may still exploit its oriented cumulative discrepancy, but it
does not produce the all-order total positivity required by (12).

## 3. The actual von Mangoldt series is a square, but the pullback is signed

Let \(a>1\), and put

\[
 F(a)=\sum_{m\ge2}\Lambda(m)m^{-a}.
\tag{21}
\]

On the finite torus with independent coordinates \(\omega_m\), define

\[
 Q_{M,a}(\omega)=
 \sum_{2\le m\le M}\sqrt{\Lambda(m)}\,m^{-a/2}\omega_m.
\tag{22}
\]

Orthogonality of the characters gives the exact positive quadratic
identity

\[
 \int |Q_{M,a}|^2d\omega
 =\sum_{2\le m\le M}\Lambda(m)m^{-a}.
\tag{23}
\]

Monotone convergence sends (23) to (21).  Thus lack of a square for the
bare Dirichlet series is not the obstruction.

The conformal coefficient extraction applies instead the Laguerre
operator

\[
 \begin{aligned}
 S_n(a)
 &:=\sum_{m\ge2}{\Lambda(m)\over m^a}L_n(a\log m)\\
 &=\sum_{k=0}^n{n\choose k}{a^k\over k!}F^{(k)}(a).
 \end{aligned}
\tag{24}
\]

Absolute convergence justifies the second equality.  This operator is not
positivity preserving, even on the exact square (23).  Since
\(L_1(x)=1-x\), for every \(a\ge1/\log2\),

\[
 S_1(a)=\sum_{m\ge2}{\Lambda(m)\over m^a}(1-a\log m)<0.
\tag{25}
\]

Indeed every summand is nonpositive and, for example, the \(m=3\) summand
is strictly negative.  This is an exact sign certificate, with no
numerical approximation.

In the completed flow of `103_53`, \(-2aS_n(a)\) must still be combined
with the pole and Gamma blocks.  Therefore (25) does not decide the sign
of \(D_{n+1}(a)-D_n(a)\); it proves precisely that averaging phases to
make the prime series a square *before* the Laguerre pullback cannot supply
the desired completed positivity.

## 4. Surviving target and circularity audit

The three tests leave only a signed, completed comparison.

* The positive uncanonical trivial-zero terms are divergent; the
  convergent canonical terms have the opposite sign.
* A positive mixture of logarithmic factors is excluded by (19).
* A genuine von Mangoldt Hilbert-space square is destroyed by the exact
  Laguerre operator, as (25) shows.

None of these no-go statements permits replacing \(\Lambda(m)\) by an
envelope or by arbitrary support weights.  The live object remains the
paired pole--prime--Gamma expression from `103_53` or, equivalently, the
completed Abel first-difference identity from `103_56`.  A successful
factorization would have to couple those three blocks before taking a
positive part and must evade the explicit derivative and kernel tests
above.  Producing that coupling would prove an RH-strength statement; it
has not been obtained here.
