# 104_47 — Size-biased homotopy flux and the exact residue gate

**Status.** The homotopy \(a\downarrow1\) of `104_41` and the exact
divisor selector of `104_43` are combined with no separation of primes,
prime powers, or the pole. The result is a closed differential law and a
signed flux formula:

\[
 \boxed{
 a\,\partial_a\mathcal B_{n,a}
 =n\{\mathcal B_{n+1,a}-\mathcal B_{n,a}\}.}
 \tag{1}
\]

In size-biased coordinates, the density of this flux is exactly the
difference between the von Mangoldt divisor selector and the uniform
polar selector, jointly tested against \(L_n\). The selector does not
depend on \(a\); all the dependence of the homotopy lies in the two
exponentially tilted laws and in the test's scale.

The identity does not close the margin. Integrating it from a Euler point
\(a_0\ge4\) down to \(1\), the one-sided inequality the flux needs is
**equivalent**, with no remainder, to

\[
 H_n=\lambda_n-{501\over2002}A_n\ge0.                       \tag{2}
\]

Zero for zero, the value at the critical endpoint is the Euler value
minus the integrated flux; that reconstruction is exactly the residue
crossing the Hardy circle. The rational quartet of `104_41` leaves the
critical phase unchanged and produces in the flux a quantity of size
\(2^{152}\). Hence the size-biased selector correctly localizes where the
new arithmetic input should enter, but does not manufacture it.

Ruled out is the mechanism "differentiate in \(a\), apply only
Markov/Jensen to the selector, and close the flux with a generic
inequality." Not ruled out is a signed inequality that essentially uses
the special rigidity

\[
 \Lambda(p^k)=\log p                                                   \tag{3}
\]

across every tower at once. This document proves neither (2), A1, nor
RH.

## 1. Non-duplication audit

`104_18` correlates a Jordan shift \(u=c\varepsilon\) with
\(\varepsilon\downarrow0\); its limit is the adjacent cost
\(C_n=\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime}\). Here there is no
Jordan shift: the geometric parameter
\(s=a/(1-z)\) of the complete homotopy is differentiated.

`104_31` transports a fixed test backward via the generator
\(-M_x\) and proves the domain collision at \(\varepsilon=1/2\). In (1)
the test is simultaneously scaled as \(P_n(ax)\), so no inverse semigroup
on a Hilbert space is postulated. The obstruction that appears is
different: the flux exactly couples degrees \(n\) and \(n+1\).

`104_43` builds the size-biased selector for a fixed \(a>1\), and `104_44`
studies its Markov contraction and the cost of rescaling Laguerre. Neither
the zero gap nor the exponential scaling cost is repeated. What is new
here is keeping the selector throughout \(a\downarrow1\), computing its
flux law, and comparing it zero for zero with the residue term of
`104_41`.

The Abel coefficient tail of `104_41` (4a) is likewise not reinverted:
(1) is a differential identity before any Tauberian inference is
attempted.

## 2. The two selectors throughout the homotopy

Let \(a>1\), \(\varepsilon=a-1\), and write

\[
 \mathfrak m(a)=-{\zeta'(a)\over\zeta(a)}
 =\sum_{d\ge2}{\Lambda(d)\over d^a}.                         \tag{4}
\]

Let \(D_a,N_a'\) be independent with

\[
 \mathbb P(D_a=d)={\Lambda(d)d^{-a}\over\mathfrak m(a)},
 \qquad
 \mathbb P(N_a'=k)={k^{-a}\over\zeta(a)},                    \tag{5}
\]

and \(N_a^*=D_aN_a'\). By `104_43`,

\[
 \mathbb P(D_a=d\mid N_a^*=N)
 ={\Lambda(d)\over\log N}{\bf1}_{d\mid N}.                  \tag{6}
\]

Denote this kernel by \(K\). Importantly, \(K\) does not depend on
\(a\): varying \(a\) only exponentially tilts the law of the product.

In the polar channel, let \(Y_a,Y_a'\) be independent exponentials of
rate \(\varepsilon\), and \(S_a^*=Y_a+Y_a'\). Conditioned on
\(S_a^*=x\), \(Y_a\) is uniform on \([0,x]\); write

\[
 (Uf)(x)={1\over x}\int_0^x f(y)\,dy.                        \tag{7}
\]

\(U\) is likewise independent of \(a\). Let

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad f_{n,a}(x)=P_n(ax).           \tag{8}
\]

The complete form of `104_41` then admits the disintegration

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{n,a}
  =a\bigg\{&\mathfrak m(a)
       \mathbb E\big[(Kf_{n,a})(N_a^*)\big]\\
    &-{1\over\varepsilon}
       \mathbb E\big[(Uf_{n,a})(S_a^*)\big]\bigg\}.
 \end{aligned}}                                             \tag{9}
\]

Indeed, the conditional expectations of (9) recover, respectively, the
law of \(D_a\) and that of \(Y_a\). Hence (9) is exactly

\[
 a\sum_{d\ge2}{\Lambda(d)\over d^a}P_n(a\log d)
 -a\int_0^\infty e^{-(a-1)x}P_n(ax)\,dx.                    \tag{10}
\]

No modulus was taken, and both selectors remain within the same
difference. Moreover,

\[
 \lim_{a\downarrow1}\mathcal B_{n,a}=B_n=A_n-\lambda_n.     \tag{11}
\]

## 3. Exact differential law

The elementary identity governing the flux is

\[
 \boxed{
 P_n(x)+xP_n'(x)-xP_n(x)=nL_n(x)
 =n\{P_{n+1}(x)-P_n(x)\}.}                                  \tag{12}
\]

Consequently, for \(y\ge0\),

\[
 a{d\over da}\{a e^{-ay}P_n(ay)\}
 =n\{a e^{-ay}P_{n+1}(ay)-a e^{-ay}P_n(ay)\}.              \tag{13}
\]

Multiplying (13) by \(e^y\) gives the same identity with
\(e^{-(a-1)y}\), the polar weight. For \(a\ge1+\delta>1\), the series and
integrals of (10), together with all their derivatives, converge
absolutely. Differentiation term by term is therefore legitimate, giving
(1).

The degree difference explicitly preserves the two selectors. If

\[
 \ell_{n,a}(x)=L_n(ax),                                      \tag{14}
\]

then

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{n+1,a}-\mathcal B_{n,a}
 =a\bigg\{&\mathfrak m(a)
       \mathbb E[(K\ell_{n,a})(N_a^*)]\\
   &-{1\over\varepsilon}
       \mathbb E[(U\ell_{n,a})(S_a^*)]\bigg\}.
 \end{aligned}}                                             \tag{15}
\]

So the homotopy's derivative introduces no unknown auxiliary quantity: it
introduces exactly the signed divisor-versus-uniform comparison against
the next Laguerre function.

## 4. The missing flux theorem is exactly \(H_n\ge0\)

Fix \(a_0\ge4\) and define, keeping the difference joined,

\[
 \begin{aligned}
 \mathscr J_{n}(a_0):={}&n\lim_{\delta\downarrow0}
 \int_{1+\delta}^{a_0}
 \bigg\{\mathfrak m(a)
       \mathbb E[(K\ell_{n,a})(N_a^*)]\\
 &\hspace{38mm}-{1\over a-1}
       \mathbb E[(U\ell_{n,a})(S_a^*)]\bigg\}\,da.
                                                               \tag{16}
 \end{aligned}
\]

The limit of the two terms separately is not used. Integrating (1) and
using (11),

\[
 \boxed{\mathscr J_n(a_0)=\mathcal B_{n,a_0}-B_n.}           \tag{17}
\]

Set

\[
 \kappa={1501\over2002}.
\]

Since \(H_n=\kappa A_n-B_n\), (17) gives the exact equivalence

\[
 \boxed{
 H_n\ge0
 \quad\Longleftrightarrow\quad
 \mathscr J_n(a_0)\ge\mathcal B_{n,a_0}-\kappa A_n.}        \tag{18}
\]

The phase bound of `104_41`,
\(|\mathcal B_{n,a_0}|\le3n\), controls the Euler extreme. All the
RH-strength content remains in the integrated sign of (16). In
particular, a flux inequality proving (18) would be a valid closure; but
(18) proves it is not a free consequence of having found the differential
law.

Separating channels is likewise inadmissible. The polar part of (10) is

\[
 \mathcal Q_{n,a}
 :=a\int_0^\infty e^{-(a-1)x}P_n(ax)\,dx
 =1-\left({-1\over a-1}\right)^n.                           \tag{19}
\]

By (11), the prime part has the same leading divergence as (19) as
\(a\) decreases to one. Each channel has size \((a-1)^{-n}\), while their
difference has a finite limit. Applying Markov or Jensen before the
subtraction destroys exactly the cancellation that defines (16).

## 5. Integrating the flux does not make the weights positive

For \(a_1>1\), the prime channel of (16) can be integrated term by
term. Identity

\[
 {d\over dx}\{e^{-x}L_n^{(-1)}(x)\}=-e^{-x}L_n(x)           \tag{20}
\]

gives

\[
 \begin{aligned}
 &\int_{a_1}^{a_0}{\Lambda(d)\over d^a}L_n(a\log d)\,da\\
 &\quad={\Lambda(d)\over\log d}
 \left\{d^{-a_1}L_n^{(-1)}(a_1\log d)
       -d^{-a_0}L_n^{(-1)}(a_0\log d)\right\}.              \tag{21}
 \end{aligned}
\]

Here

\[
 {\Lambda(p^k)\over\log(p^k)}={1\over k},                  \tag{22}
\]

so the homotopy does exactly reveal the prime towers, with no
majorizing. But

\[
 L_n^{(-1)}(x)=-{x\over n}L_{n-1}^{(1)}(x)                  \tag{23}
\]

changes sign \(n-1\) times on \((0,\infty)\). Hence the positive
coefficients \(1/k\) of (22) produce no term-by-term sign. As
\(a_1\downarrow1\), the channels of (21) and (19) diverge, and only their
renormalized difference converges. The exact integration reorganizes the
gate; it does not turn it into positivity.

## 6. The quartet is reconstructed via a flux pulse

Let

\[
 \rho={4+2i\over5},\qquad
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\},       \tag{24}
\]

and \(Q_\rho(s)=\prod_{\eta\in\mathcal O(\rho)}(s-\eta)\). For
each zero set

\[
 z_{\eta,a}=1-{a\over\eta}.                                 \tag{25}
\]

The contribution of \(Q_\rho\) to the homotopy coefficient is

\[
 \boxed{
 q_{n,a}:=-n[z^n]\log Q_\rho\!\left({a\over1-z}\right)
 =\sum_{\eta\in\mathcal O(\rho)}(z_{\eta,a}^{-n}-1).}       \tag{26}
\]

Each summand satisfies the same law as (1):

\[
 a\,\partial_a q_{n,a}=n(q_{n+1,a}-q_{n,a}).                \tag{27}
\]

For \(a_0=4\), every \(z_{\eta,4}\) lies outside the unit disc. Reaching
\(a=1\), the four values are

\[
 {i\over2},\quad-{i\over2},\quad-2i,\quad2i.                \tag{28}
\]

Hence, for \(n=152\),

\[
 \boxed{q_{152,1}=2(2^{152}+2^{-152})-4>2^{153}-4.}         \tag{29}
\]

Its integrated flux is, exactly,

\[
 152\int_1^4{q_{153,a}-q_{152,a}\over a}\,da
 =q_{152,4}-q_{152,1}.                                      \tag{30}
\]

The right-hand side contains the negative exponential pulse preventing
transport of an upper bound from \(a=4\). At the same time,
\(Q_\rho(1/2+it)>0\), so multiplying the completed function by
\(Q_\rho^M\) does not change its phase on the critical line. Equations
(26)–(30) identify the residue of `104_41` as the exact combination
"Euler extreme minus flux," not as the isolated flux nor as a boundary
error: \(q_{n,1}=q_{n,4}-(q_{n,4}-q_{n,1})\).

The quartet does not preserve selector (6), so an inequality that
genuinely uses the exact weights can and must reject it. What (30)
refutes is closing the homotopy using only its differential law and the
phase at the extreme.

## 7. Why generic size-biased positivity is not enough either

There is a falsifier preserving the entire generic probabilistic
machinery. Let \(0<c<1/2\) and

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c)
       =\sum_{n\ge1}{a_c(n)\over n^s},\qquad a_c(n)>0.       \tag{31}
\]

Its logarithmic derivative has positive weights

\[
 -{Z_c'(s)\over Z_c(s)}
 =\sum_{d\ge2}{\omega_c(d)\over d^s},\qquad
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0.                  \tag{32}
\]

Comparing coefficients in \(-Z_c'=(-Z_c'/Z_c)Z_c\) gives

\[
 (\log n)a_c(n)=\sum_{d\mid n}\omega_c(d)a_c(n/d).          \tag{33}
\]

So the law of \(Z_c\) has the same size-biased factorization, with fixed
selector

\[
 K_c(n,d)={\omega_c(d)a_c(n/d)\over(\log n)a_c(n)}
             {\bf1}_{d\mid n}.                              \tag{34}
\]

It also satisfies differential law (1), which is an identity of the
composition \(a/(1-z)\), on its Euler domain \(a>1+c\). This refutes
inferences using only local positivity/Markov on that domain; it does not
claim that the model preserves a positive probabilistic law throughout
the whole path \(a\downarrow1\). However,
\(\xi(s+c)\xi(s-c)\) has zeros on both sides of its line of symmetry. So
weight positivity, size-biased factorization, the Markov property,
selector invariance under tilting, and the flux law cannot, by
themselves, imply the margin.

The property that (32) loses and (3) preserves is the exact constancy of
the weight along each prime tower. A future inequality must use that
rigidity quantitatively; using only \(\omega(d)\ge0\) would repeat the
falsifier.

## 8. Verdict

Proved unconditionally:

1. the complete disintegration (9), with \(K\) and \(U\) independent of
   the homotopy;
2. the exact differential law (1) and its signed density (15);
3. the exact flux–margin equivalence (18);
4. the integrated tower formula (21)–(23);
5. the zero-for-zero reconstruction of the residue via Euler extreme and
   flux pulse (26)–(30);
6. that the generic size-biased machinery also exists for the off-line
   falsifier (31)–(34).

Ruled out:

```text
safe phase at a>=4
+ differential law in a
+ Markov/Jensen for the selector
=> proportional bound at a=1.
```

The minimal successor is a lower bound for the **already coupled**
functional of (16), valid for the exact weights
\(\Lambda(p^k)=\log p\), uniform in \(n\ge150\), and false when they are
replaced by (32). By (18), that is not an auxiliary technical lemma: it
is precisely the new arithmetic theorem that would close A1.

## 9. Reproducible verification

The file
`tools/size_bias_homotopy_flux_gate_check.py` uses only integers and
`Fraction`. It checks:

* the polynomial identities (12), (20), and (23);
* the exact polar flux (19);
* the zero-for-zero law (27) in Gaussian rationals;
* the four points (28), exact identity (29), and the pulse's size;
* that every point of the quartet lies outside the circle at \(a=4\).

Reproduced with

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 size_bias_homotopy_flux_gate_check.py
```
</content>
