# 104_43 — Size-bias zeta, divisor selector, and the martingale gate

**Role.** Exploit the special identity

\[
 \log n=\sum_{d\mid n}\Lambda(d)
\]

before separating primes, prime powers, and the pole. The zeta law has an
exact size-biased factorization: biasing by \(\log N\) gives
\(N^\star=DN'\), where \(N'\) again has the zeta law and \(D\) has exactly
the weights \(\Lambda(d)d^{-s}\). Conditioned on
\(N^\star=n\), the divisor \(D\) is chosen with probability
\(\Lambda(d)/\log n\). The polar comparator is the continuous
factorization \(\Gamma(2,\varepsilon)=\mathrm{Exp}(\varepsilon)+
\mathrm{Exp}(\varepsilon)\), whose conditioned selector is uniform on the
logarithmic interval.

The factorization is exact and simultaneously preserves every prime power
and every other prime. However:

1. the divisor selector neither dominates nor is dominated by the uniform
   selector, already for the linear test function and the real integers
   \(2\) and \(30\);
2. comparing the two selected laws via the Laplace transform gives
   **exactly**
   \(R(t)=-\zeta'/\zeta(1+t)-1/t\), that is, the already-open scalar gate;
3. Efron–Stein applied separately to the zeta law loses the Abel
   cancellation: for the Laguerre test of degree \(n-1\), its energy
   diverges at least like
   \(\{\binom{2n-2}{n-1}-1\}\varepsilon^{-2n+2}\).

Hence closing the margin via conditional order, data processing, or a
separately applied positive tensorized energy is ruled out. Not ruled out
is a **signed, coupled** inequality specific to the divisor-selector
versus uniform-selector difference; by the transform identity, producing
it would be precisely new arithmetic content. This document proves
neither \(H_n\ge0\), nor A1, nor RH.

The normalization of the front is

\[
 H_n=\lambda_n-{501\over2002}A_n,
 \qquad
 {2002\over501}H_n=r_*\lambda_n-A_n,
 \qquad r_*={2002\over501}.                                   \tag{0}
\]

Hence a one-sided bound for the completed generator with exponent
\(r_*\) would close the target; none of the contractions proved below
supplies that bound.

## 1. Internal non-duplication audit

`104_16` already proves that the positive Jordan cocycle loses its sign
when paired with the pole. `104_20` preserves complete towers, but its
local square is not a norm. `104_21` builds the global compound-Poisson
law and its Mecke identity. `104_24` applies Stein–Mecke to the completed
cocycle and obtains a signed generator. `104_29` shows that splitting at
\(\log2\) exactly recomposes the sought margin.

What was not written in those documents is the size-biased disintegration
over the **product integer** \(N^\star\), with the kernel

\[
 K(n,d)={\Lambda(d)\over\log n}{\bf1}_{d\mid n},                 \tag{1}
\]

nor its exact comparison with the uniform split of the pole. The identity
is the divisor version of Mecke's formula, not an additional source of
positivity. No bibliographic novelty is claimed for general size-bias
theory or for Efron–Stein.

## 2. Zeta law and exact size-biased factorization

Fix \(s=1+\varepsilon>1\) and let

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad m\ge1.           \tag{2}
\]

In the Euler product,

\[
 N=\prod_p p^{K_p},\qquad
 \mathbb P(K_p=k)=(1-p^{-s})p^{-ks},\quad k\ge0,               \tag{3}
\]

and the \(K_p\) are independent. Set

\[
 \mathfrak m(s):=\mathbb E_s\log N
 =-{\zeta'\over\zeta}(s)
 =\sum_{d\ge2}{\Lambda(d)\over d^s}>0.                         \tag{4}
\]

The law biased by \(\log N\) is

\[
 \mathbb P_s^\star(N^\star=m)
 ={(\log m)m^{-s}\over-\zeta'(s)},\qquad m\ge2.               \tag{5}
\]

**Theorem 2.1 (divisor–cofactor factorization).** Let independently

\[
 \mathbb P_s(D=d)={\Lambda(d)d^{-s}\over\mathfrak m(s)},
 \qquad
 \mathbb P_s(N'=k)={k^{-s}\over\zeta(s)}.                     \tag{6}
\]

Then

\[
 \boxed{N^\star\ \buildrel d\over=\ DN'.}                    \tag{7}
\]

Moreover, for each \(n\ge2\),

\[
 \boxed{
 \mathbb P(D=d\mid DN'=n)
 ={\Lambda(d)\over\log n}{\bf1}_{d\mid n}.}                  \tag{8}
\]

*Proof.* The joint mass at \((d,k)\) is

\[
 {\Lambda(d)d^{-s}\over\mathfrak m(s)}
 {k^{-s}\over\zeta(s)}
 ={\Lambda(d)(dk)^{-s}\over-\zeta'(s)}.                       \tag{9}
\]

Summing (9) over \(dk=n\) and using
\(\sum_{d\mid n}\Lambda(d)=\log n\) produces (5) and (7).
Dividing (9) by the resulting mass at \(n\) produces (8). \(\square\)

In additive coordinates,

\[
 X=\log N',\qquad Y=\log D,\qquad S=\log N^\star=X+Y,          \tag{10}
\]

with \(X\) and \(Y\) independent. All the interaction between distinct
primes remains inside the law of \(S\); nothing has been grouped tower by
tower or had absolute values taken.

## 3. Polar comparator and uniform selector

Let \(Y_0\sim\mathrm{Exp}(\varepsilon)\). Its value-bias is
\(S_0^\star\sim\Gamma(2,\varepsilon)\), and it admits the factorization

\[
 S_0^\star=Y_0+Y_0',                             \tag{11}
\]

with two independent exponentials of rate \(\varepsilon\). Conditioned on
\(S_0^\star=x\), the selected variable \(Y_0\) is uniform on
\([0,x]\). Hence the continuous analogue of (1) is

\[
 (Uf)(x)={1\over x}\int_0^x f(y)\,dy.                         \tag{12}
\]

On the arithmetic side, if \(L=\log n\), (8) gives

\[
 (Kf)(n)={1\over L}\sum_{d\mid n}\Lambda(d)f(\log d).        \tag{13}
\]

The two mean-preservation identities are

\[
 \mathbb E_s^\star Kf(N^\star)=\mathbb E_s f(Y),
 \qquad
 \mathbb E\,Uf(S_0^\star)=\mathbb E f(Y_0).                   \tag{14}
\]

Conditional Jensen gives data processing, e.g.

\[
 \mathrm{Var}_{\mathbb P_s^\star}(Kf)
 \le \mathrm{Var}_{\mathbb P_s(D)}(f),                 \tag{15}
\]

and the analogous inequality for \(U\). It is a contraction of the
centered part. The constant — the mean of \(f\) — passes unchanged
through (14), and that is precisely the component appearing in the
prime–pole sum. Hence (15), by itself, cannot fix its sign.

## 4. The discrete selector has no one-sided order

The failure occurs before using any Laguerre function. For \(f(y)=y\), if
\(n=\prod_p p^{a_p}\) and \(L=\log n\), then

\[
 (Kf)(n)
 ={1\over2L}\sum_{p^{a_p}\parallel n}
     a_p(a_p+1)(\log p)^2,\qquad
 (Uf)(L)={L\over2}.                                             \tag{16}
\]

Consequently,

\[
 \boxed{
 2L\{(Kf)(n)-(Uf)(L)\}
 =\sum_p a_p(a_p+1)(\log p)^2-L^2.}                            \tag{17}
\]

For \(n=2\), (17) equals \((\log2)^2>0\). For \(n=30\), write
\(a=\log2\), \(b=\log3\), \(c=\log5\). The right-hand side is

\[
 a^2+b^2+c^2-2ab-2ac-2bc=(a+b-c)^2-4ab<0.                     \tag{18}
\]

The last inequality is not numerical: since

\[
 0<a+b-c=\log(6/5)<\log2=a,
\]

one has

\[
 (a+b-c)^2-4ab<a^2-4ab=a(a-4b)<0.                             \tag{19}
\]

Hence there is no coupling conditioned on \(S=L\) that always places the
selected divisor above the uniform one, nor one that always places it
below. In particular, both conditional stochastic orders fail, as does
any convex order already ordering linear functions. A global comparison,
after averaging over \(n\), is not refuted by (18); it would need
cancellation between different factorizations.

## 5. The marginal comparison is exactly \(R\)

For a polynomial test function \(f\), define the paired prime–pole
functional

\[
 \mathfrak M_\varepsilon(f)
 :=\mathfrak m(1+\varepsilon)\,\mathbb E f(Y)
   -{1\over\varepsilon}\mathbb E f(Y_0).                       \tag{20}
\]

By (6) and the exponential density,

\[
 \boxed{
 \mathfrak M_\varepsilon(f)
 =\sum_{d\ge2}{\Lambda(d)\over d^{1+\varepsilon}}f(\log d)
  -\int_0^\infty e^{-\varepsilon x}f(x)\,dx.}                 \tag{21}
\]

Taking \(f_t(x)=e^{-tx}\), one obtains

\[
\begin{aligned}
 \mathfrak M_\varepsilon(f_t)
 &=\mathfrak m(1+\varepsilon+t)-{1\over\varepsilon+t}\\
 &=\boxed{R(\varepsilon+t)},                                  \tag{22}
\end{aligned}
\]

where

\[
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q}.                   \tag{23}
\]

This identifies, with no remainder, the error of the size-biased
coupling. If

\[
 L_n(x)=\sum_{j=0}^n{n\choose j}{(-x)^j\over j!},              \tag{24}
\]

differentiating (22) at \(t=0\) gives

\[
 \boxed{
 \mathfrak M_\varepsilon(L_n)
 =\sum_{j=0}^n{n\choose j}{R^{(j)}(\varepsilon)\over j!}.}     \tag{25}
\]

In the limit \(\varepsilon\downarrow0\), (25) is exactly the binomial
coefficient \(C_n\) of `104_03`, and

\[
 C_n=\Delta A_n-\Delta\lambda_n.                              \tag{26}
\]

Using \(L_{n-1}^{(1)}-n\) in (21), and adding the explicit Gamma density,
gives the compensated generator of `104_29`. So the divisor
disintegration does not replace the gate: its comparison error is its own
exact scalar generating function.

## 6. Quantitative Efron–Stein stop-gate

Independence (3) allows a genuine tensorized energy. Let
\(K_p'\) be an independent copy of \(K_p\), let

\[
 X_\varepsilon=\log N,\qquad
 X_\varepsilon^{(p)}
 =X_\varepsilon-(\log p)K_p+(\log p)K_p',                     \tag{27}
\]

and define

\[
 \mathcal E_\varepsilon(f)
 ={1\over2}\sum_p\mathbb E
  \{f(X_\varepsilon)-f(X_\varepsilon^{(p)})\}^2.             \tag{28}
\]

For every fixed polynomial, the series converges when \(\varepsilon>0\),
and Efron–Stein, first over a finite number of primes and then by limit,
gives

\[
 \mathrm{Var}\,f(X_\varepsilon)
 \le\mathcal E_\varepsilon(f).                               \tag{29}
\]

The Laurent expansion of zeta at one implies, for each \(k\ge1\),

\[
 \mathbb E X_\varepsilon^k
 ={(-1)^k\zeta^{(k)}(1+\varepsilon)\over
    \zeta(1+\varepsilon)}
 =k!\,\varepsilon^{-k}\{1+O_k(\varepsilon)\}.                \tag{30}
\]

Set

\[
 \varphi_n(x)=L_{n-1}^{(1)}(x)-n,\qquad d=n-1.                 \tag{31}
\]

Its leading coefficient is \((-1)^d/d!\). Using (30) in the two leading
moments,

\[
 \boxed{
 \mathrm{Var}\,\varphi_n(X_\varepsilon)
 =\left\{{2d\choose d}-1+O_n(\varepsilon)\right\}
   \varepsilon^{-2d}.}                                        \tag{32}
\]

By (29), the positive energy (28) is at least of the order of (32). For
every \(n\ge2\), and in particular for \(n\ge150\), it diverges as the
regulator is removed. The exponential comparator has the same leading
scale. The prime–pole difference of (21), by contrast, has a finite Abel
limit by (22).

So applying Cauchy–Schwarz/Poincaré to each channel before subtracting
them exchanges a finite object for two energies of size
\(\varepsilon^{-2n+2}\). This is not a constant-factor loss: it eliminates
the cancellation that defines the functional. This argument does not rule
out a **cross** energy built from a coupling of the two laws; (18) proves
that the cross coupling cannot be based on a monotone order of the
canonical selector.

### 6.1. The scaling \(L_n(\varepsilon x)\) does not recover the coefficient

There is an apparent escape from (32): under the zeta law,
\(\varepsilon X_\varepsilon\) converges with all its moments to a
rate-one exponential. Hence a scaled test such as
\(L_n(\varepsilon x)\) has bounded norm. But (22) shows exactly what
information is retained:

\[
 \boxed{
 \mathfrak M_\varepsilon\bigl(L_n(\varepsilon\,\cdot)\bigr)
 =\sum_{j=0}^n{n\choose j}{\varepsilon^jR^{(j)}(\varepsilon)\over j!}.}
                                                                    \tag{33}
\]

Since \(R\) is analytic at zero, (33) tends to \(R(0)\); if the constant
term of the test is subtracted, it tends to zero. The undamped
coefficient, by contrast, is

\[
 C_n=\sum_{j=0}^n{n\choose j}{R^{(j)}(0)\over j!}.                \tag{34}
\]

In (33), the diagonal carrying \(R^{(j)}\) carries the factor
\(\varepsilon^j\). Inverting that triangular transform to recover the
order-\(n\) jet requires a factor \(\varepsilon^{-n}\); squaring it brings
back \(\varepsilon^{-2n}\), the energy scale of the unscaled test of the
same degree. So the scaled test controls an Abel/triangular average, not
the individual coefficient.

This is consistent with three earlier stop-gates: `104_17` proves that
Abel positivity does not control the coefficients; `104_18` proves that
keeping a finite correlated shift returns to the same \(C_n\) when the
regulator is removed; `104_31` localizes the loss of observability upon
inverting the flow in \(\varepsilon\). No no-go is claimed here for every
\(\varepsilon\)-dependent family of tests, only for the direct rescue via
the scaling that keeps the energy bounded.

## 7. Off-line falsifier

The generic probabilistic machinery likewise does not by itself single
out the critical line. For \(a>0\), the Euler part of

\[
 X_a(s)=\xi(s+a)\xi(s-a)                                      \tag{35}
\]

is the product of two independent zeta laws, with geometric exponents of
parameters \(p^{-(s+a)}\) and \(p^{-(s-a)}\). Its logarithmic derivative
has positive weights

\[
 2\Lambda(m)\cosh(a\log m),                                  \tag{36}
\]

and admits the same size-bias identities, an analogous selector with
those weights, data processing, and Efron–Stein. However, as `104_16`
proves, \(X_a\) has zeros off its line of symmetry.

Hence an inference using only geometric independence, jump positivity,
and a tensorized inequality would also apply to falsifier (35). A valid
proof must quantitatively use the exact weights
\(\Lambda(p^k)=\log p\) in the **signed difference** (21), and must stop
being valid when they are replaced by (36).

## 8. Decision and successor

Proved unconditionally:

1. the exact size-biased factorization (7)–(8);
2. its polar comparator as a uniform split (11)–(12);
3. data processing with no loss of primes (15);
4. the real sign change of the selector versus the uniform one
   (17)–(19);
5. the exact identity of the error with \(R\) (22)–(26);
6. the scale loss of the separated Efron–Stein energy (32).

Ruled out:

```text
one-sided order divisor <-> uniform;
data processing of the mean -> prime-pole sign;
Poincare/Efron--Stein over separated channels -> finite Abel limit;
generic positive tensorization -> margin H_n.
```

The only successor this coordinate leaves alive is a signed cross
inequality for

\[
 \mathfrak m(1+\varepsilon)\,\mathbb E f(Y)
 -\varepsilon^{-1}\mathbb E f(Y_0),                            \tag{37}
\]

with \(f=L_{n-1}^{(1)}-n\), keeping afterward the Gamma term and the Abel
limit. By (22), that inequality must supply information that is not a
mere probabilistic contraction: the transform of (37) on exponential
tests is already \(R\) in size-biased coordinates.

## 9. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 zeta_size_bias_martingale_gate_check.py
```

The checker uses integer arithmetic and `Fraction`. It verifies the formal
identity of the divisor selector, the opposite signs of (17) at \(2\) and
\(30\), and the integer constants of (32) for \(2\le n\le50\). It evaluates
neither zeta, A1, nor RH.
</content>
