# 104_45 — Crossed divisor–Gamma Stein and the signed tail kernel

**Role.** Execute the only successor left open by `104_43` and
`104_44`: compare the size-biased arithmetic law and the continuous
Gamma–exponential split **within a single identity**, before applying an
energy or an inequality. The coupling can be built exactly. Moreover, its
first-order local Stein representation is canonical: it does not depend
on how the two laws are coupled.

The result is not the sought one-sided bound. The canonical kernel is

\[
 K_s(x)=\sum_{\log m>x}{\Lambda(m)\over m^s}
        -{e^{-(s-1)x}\over s-1},                              \tag{1}
\]

and it changes sign even before and after the first prime atom.
Integrating it against the derivative of the Laguerre test, the operator
exactly recomposes

\[
 \mathcal B_{n,s}\longrightarrow B_n=A_n-\lambda_n.          \tag{2}
\]

Hence a one-sided bound strong enough for this operator is
**equivalent to**, not a precursor of,

\[
 B_n\le {1501\over2002}A_n.                                  \tag{3}
\]

Obtaining (3) by choice of coupling, transport order, Stein-kernel
positivity, or an automatic local cross energy is ruled out. What remains
alive is a nonlocal inequality specific to the correlation between (1) and
the real Laguerre test. This document proves neither (3), A1, nor RH.

## 0. Internal non-duplication audit

`104_24` builds the completed Stein–Mecke generator and proves that its
jump measure is already signed before \(\log2\); it does not couple the
two laws. `104_29` cuts that generator at \(\log2\) and shows that the
recomposition is exactly the sought margin. `104_43` discovers the
size-biased factorization \(DN'\), the divisor selector, and the
Efron–Stein divergence when applied to each channel separately. `104_44`
adds the Markov transport, its zero gap, and the joint mean identity (its
(25b)).

What remained to be checked was whether a **crossed** coupling, after
equalizing the prime and polar masses, could preserve the cancellation
and create coercivity. The new, narrow content of this document is: the
equalization (13), the coupling-independence of the kernel (21), its
arithmetic falsifier (29), and the exact symbolic cancellation (40). No
bibliographic novelty is claimed for Stein theory, size-bias, or optimal
transport.

## 1. The two complete factorizations

Fix

\[
 s=1+\varepsilon>1,\qquad
 \mathcal L_s=-{\zeta'\over\zeta}(s),\qquad
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q}.                   \tag{4}
\]

The joint arithmetic law of `104_43` is

\[
 \mathbb Q_s(D=d,N'=k)
 ={\Lambda(d)(dk)^{-s}\over-\zeta'(s)},\qquad d\ge2, k\ge1.\tag{5}
\]

Its coordinates are independent, \(D\) has the normalized von Mangoldt
law, and \(N'\) has the zeta law. The product \(DN'\) has the law biased
by \(\log N\), and, conditioned on \(DN'=n\),

\[
 \mathbb P(D=d\mid DN'=n)
 ={\Lambda(d)\over\log n}{\bf1}_{d\mid n}.                   \tag{6}
\]

In additive coordinates write

\[
 Y=\log D,\qquad X=\log N',\qquad S=Y+X.                     \tag{7}
\]

The polar comparator likewise preserves its two coordinates. Let

\[
 Y_0,X_0\stackrel{\rm ind}{\sim}\mathrm{Exp}(\varepsilon),
 \qquad S_0=Y_0+X_0\sim\Gamma(2,\varepsilon).                \tag{8}
\]

Conditioned on \(S_0=u\), \(Y_0\) is uniform on \([0,u]\). So, for

\[
 (\mathsf K_sf)(n)={1\over\log n}
       \sum_{d\mid n}\Lambda(d)f(\log d),\qquad
 (\mathsf Cf)(u)={1\over u}\int_0^u f(x)\,dx,                \tag{9}
\]

with the extension \(\mathsf Cf(0)=f(0)\), one has

\[
 \mathbb E[f(Y)\mid S]=\mathsf K_sf(e^S),\qquad
 \mathbb E[f(Y_0)\mid S_0]=\mathsf Cf(S_0).                 \tag{10}
\]

Equations (5)–(10) keep together every prime, every prime power, the zeta
cofactor, and the two coordinates of the Gamma split. Here
\(\Gamma(2,\varepsilon)\) is the probabilistic Gamma obtained by
size-biasing the exponential pole. The archimedean Gamma factor of the
completed function has not been omitted: its exact contribution is the
block \(A_n\) on the right-hand side of (3). The identity
\(B_n=A_n-\lambda_n\) isolates precisely the prime–pole block that must be
compared against that \(A_n\).

## 2. Exact mass equalization and crossed coupling

The prime–pole difference to be estimated is

\[
 \mathfrak M_\varepsilon(f)
 :=\sum_{m\ge2}{\Lambda(m)\over m^s}f(\log m)
    -\int_0^\infty e^{-\varepsilon x}f(x)\,dx.               \tag{11}
\]

By the Laurent expansion,

\[
 \varepsilon\mathcal L_s=1-\gamma\varepsilon+O(\varepsilon^2).
                                                                    \tag{12}
\]

In fact,

\[
 0<\varepsilon\mathcal L_s<1\qquad(\varepsilon>0).          \tag{12a}
\]

The first inequality is immediate, and the second is equivalent to
\(R(\varepsilon)<0\), proved for every \(\varepsilon>0\) in (40a) below.
Hence, with no restriction on \(\varepsilon\), we add a cemetery state
\(\partial=(0,0)\) to the arithmetic law and define

\[
 \widehat{\mathbb Q}_s
 =\varepsilon\mathcal L_s\,\mathbb Q_s
  +(1-\varepsilon\mathcal L_s)\delta_\partial.               \tag{13}
\]

This is a probability, as is the law \(\mathbb Q_\varepsilon^0\) of the
pair \((Y_0,X_0)\). Let \(\Pi_s\) be **any** coupling between (13) and
\(\mathbb Q_\varepsilon^0\); at the cemetery state we set
\(Y=X=S=0\). Then

\[
\boxed{
 \mathfrak M_\varepsilon(f)
 =R(\varepsilon)f(0)
  +{1\over\varepsilon}\,
     \mathbb E_{\Pi_s}\{f(Y)-f(Y_0)\}.}                     \tag{14}
\]

**Proof.** The first marginal of \(\Pi_s\) gives

\[
 {1\over\varepsilon}\mathbb E f(Y)
 =\sum_{m\ge2}{\Lambda(m)\over m^s}f(\log m)
  +(\varepsilon^{-1}-\mathcal L_s)f(0),                      \tag{15}
\]

while the second gives

\[
 {1\over\varepsilon}\mathbb E f(Y_0)
 =\int_0^\infty e^{-\varepsilon x}f(x)\,dx.                 \tag{16}
\]

Since \(\varepsilon^{-1}-\mathcal L_s=-R(\varepsilon)\), (15)–(16) prove
(14). \(\square\)

The same identity can explicitly keep both totals. On the additive total
variable define

\[
 \widehat{\mathsf K}_sf(0)=f(0),\qquad
 \widehat{\mathsf K}_sf(u)=\mathsf K_sf(e^u)\quad(u>0).
\]

Then

\[
\boxed{
 \mathfrak M_\varepsilon(f)
 =R(\varepsilon)f(0)
 +{1\over\varepsilon}\mathbb E_{\Pi_s}
 \{\widehat{\mathsf K}_sf(S)-\mathsf Cf(S_0)\}.}            \tag{17}
\]

This is the crossed Stein identity at the divisor–cofactor/Gamma–split
level. Neither of the two energies has been estimated separately.

## 3. The crossed Stein kernel is canonical

For a \(C^1\) function of polynomial growth,

\[
 f(a)-f(b)=(a-b)\int_0^1f'(b+u(a-b))\,du.                    \tag{18}
\]

Define the oriented occupation measure

\[
 \Theta_{s,\Pi}(B)
 ={1\over\varepsilon}\mathbb E_{\Pi_s}
 \left[(Y-Y_0)\int_0^1
 {\mathbf 1}_B(Y_0+u(Y-Y_0))\,du\right].                    \tag{19}
\]

For \(\varepsilon>0\), both marginals have moments of every order: on the
arithmetic side this is absolute convergence of the derivatives of the
Dirichlet series at \(s>1\). Hence (19) has the moments needed for
polynomial tests, and Fubini in (18)–(20) is justified.

Then (14) becomes

\[
 \mathfrak M_\varepsilon(f)
 =R(\varepsilon)f(0)+\int_0^\infty f'(x)\Theta_{s,\Pi}(dx). \tag{20}
\]

The apparent freedom in choosing \(\Pi_s\) disappears entirely:

**Theorem 3.1 (uniqueness of the crossed kernel).** For every coupling
\(\Pi_s\), measure (19) is absolutely continuous on \((0,\infty)\) and

\[
\boxed{
 \Theta_{s,\Pi}(dx)=K_s(x)\,dx,
 \quad
 K_s(x)=\sum_{\log m>x}{\Lambda(m)\over m^s}
       -{e^{-\varepsilon x}\over\varepsilon}.}              \tag{21}
\]

In particular, (21) is the only first-order local measure that can
represent (14) for all test functions.

**Proof.** The oriented density of a segment \([b,a]\) is

\[
 {\bf1}_{b<x<a}-{\bf1}_{a<x<b}
 ={\mathbf 1}_{a>x}-{\mathbf 1}_{b>x}.                       \tag{22}
\]

Averaging (22) in (19) uses only the marginals:

\[
 {1\over\varepsilon}
 \{\mathbb P(Y>x)-\mathbb P(Y_0>x)\}.
\]

For \(x>0\), the cemetery contributes nothing,

\[
 \mathbb P(Y>x)
 =\varepsilon\sum_{\log m>x}{\Lambda(m)\over m^s},
 \qquad \mathbb P(Y_0>x)=e^{-\varepsilon x},                \tag{23}
\]

giving (21). Uniqueness follows by testing against compactly supported
derivatives. \(\square\)

So neither the monotone coupling, nor the optimal one, nor an
\(n\)-dependent one can change the first-order Stein kernel: all of them
produce (21).

## 4. Arithmetic falsifier: three signs around \(\log2\)

Kernel (21) has no fixed sign for the **real** zeta weights. Let
\(a=\log2\). For \(0<x<a\),

\[
 K_s(x)=R(\varepsilon)+{1-e^{-\varepsilon x}\over\varepsilon}.
                                                                    \tag{24}
\]

Using \(R(\varepsilon)\to-\gamma\), one obtains

\[
 \lim_{\varepsilon\downarrow0}K_s(0+)=-\gamma<0,            \tag{25}
\]

\[
 \lim_{\varepsilon\downarrow0}K_s(a-)=\log2-\gamma>0.      \tag{26}
\]

Crossing the atom \(m=2\), (21) jumps downward by
\((\log2)2^{-s}\), so that

\[
 \lim_{\varepsilon\downarrow0}K_s(a+)
 ={\log2\over2}-\gamma<0.                                   \tag{27}
\]

The signs are rigorous, e.g. from the elementary bounds

\[
 {1\over2}<\gamma<{3\over5},
 \qquad {2\over3}<\log2<1.                                  \tag{28}
\]

To fix that (28) is not a numerical input: the integral comparison gives
\(H_N-\log(N+1)<\gamma<H_N-\log N\). With \(N=6\), the bound
\(\log7<39/20\) (the first seven terms of \(e^{39/20}\) already sum to
\(35844308849/5120000000>7\)) proves \(\gamma>1/2\). With \(N=25\), the
first 27 positive terms of

\[
 \log25=2\sum_{j\ge0}{(12/13)^{2j+1}\over2j+1}
\]

rationally exceed \(H_{25}-3/5\), proving
\(\gamma<3/5\). Finally the same series with argument \(1/3\) gives
\(\log2>2/3\), while \(\log2=\int_1^2dx/x<1\).

Indeed, (26) exceeds \(2/3-3/5=1/15\), while (27) is less than
\(1/2-1/2=0\). By continuity, for every sufficiently small
\(\varepsilon>0\) the kernel exhibits the pattern

\[
 \boxed{K_s(0+)<0,\qquad K_s(a-)>0,\qquad K_s(a+)<0.}        \tag{29}
\]

This refutes, within the real arithmetic, positivity of the crossed
kernel, a monotone order between the selectors, and any coercivity
obtained solely from a pointwise sign of \(\Theta_{s,\Pi}\).

The arithmetic content of \(K_s\) can also be seen without probability.
If \(E(u)=\psi(e^u)-e^u\), Stieltjes integration by parts gives, away
from the atoms and with the corresponding one-sided limits at them,

\[
 \boxed{
 K_s(x)=-e^{-sx}E(x)+s\int_x^\infty e^{-su}E(u)\,du.}        \tag{29a}
\]

So the crossed kernel is exactly a smoothed tail of the PNT error. Using a
pointwise bound on (29a) loses the phase, while keeping its complete sign
leads to the Laguerre correlation of the next section.

## 5. Specialization to the Laguerre vector and exact equivalence

Let \(n\ge2\) and

\[
 f_{n,s}(x)=L_{n-1}^{(1)}(sx),\qquad f_{n,s}(0)=n.            \tag{30}
\]

The derivative is

\[
 f'_{n,s}(x)=-sL_{n-2}^{(2)}(sx).                            \tag{31}
\]

The complete form of `104_41` and `104_44` satisfies

\[
 \mathcal B_{n,s}=s\mathfrak M_\varepsilon(f_{n,s}),
 \qquad \lim_{s\downarrow1}\mathcal B_{n,s}=B_n.           \tag{32}
\]

Applying (20)–(21), we obtain the exact crossed Stein identity

\[
\boxed{
 \mathcal B_{n,s}
 =snR(\varepsilon)
 -s^2\int_0^\infty L_{n-2}^{(2)}(sx)K_s(x)\,dx.}             \tag{33}
\]

There is no absolute value in (33); every \(p^k\), the pole, and the
Laguerre phase remain coupled. However, (33) is an exact integration by
parts of (11), not an inequality.

With

\[
 \kappa={1501\over2002},                                    \tag{34}
\]

the bound that would close Phase 104 is, by (32)–(33), exactly

\[
\boxed{
 \lim_{\varepsilon\downarrow0}
 \left\{snR(\varepsilon)
 -s^2\int_0^\infty L_{n-2}^{(2)}(sx)K_s(x)\,dx\right\}
 \le\kappa A_n.}                                            \tag{35}
\]

But the left-hand side of (35) is \(B_n\). So (35) is equivalent to
(3), and it cannot be recorded as an intermediate lemma.

The coupling form shows the same equivalence even more directly:

\[
\boxed{
 \lim_{\varepsilon\downarrow0}{s\over\varepsilon}
 \mathbb E_{\Pi_s}
 \{f_{n,s}(Y)-f_{n,s}(Y_0)\}
 \le \kappa A_n+n\gamma.}                                  \tag{36}
\]

By (14), (36) holds if and only if (3) holds. Changing the coupling
changes neither the expectation nor kernel (21).

## 6. Transform audit: the operator recomposes \(R\)

The decomposition of (17) makes visible where any apparent gain cancels.
Add and subtract \(\mathsf Cf(S)\). For
\(f_t(x)=e^{-tx}\), define

\[
 A_s(t)={1-\zeta(s+t)/\zeta(s)\over t},
 \quad A_s(0)=\mathcal L_s.                                  \tag{37}
\]

The divisor–uniform selector defect has symbol

\[
 \Sigma_s(t)=\mathcal L_{s+t}-A_s(t),                        \tag{38}
\]

while the transport between the augmented arithmetic total and
\(\Gamma(2,\varepsilon)\) has symbol

\[
 \Tau_s(t)=A_s(t)-R(\varepsilon)-{1\over\varepsilon+t}.      \tag{39}
\]

The cemetery term of (14) contributes \(R(\varepsilon)\). Hence

\[
\boxed{
 R(\varepsilon)+\Sigma_s(t)+\Tau_s(t)
 =\mathcal L_{s+t}-{1\over\varepsilon+t}
 =R(\varepsilon+t).}                                        \tag{40}
\]

So, even before specializing to Laguerre, the crossed Stein identity
recomposes the exact scalar generating function of `104_03`. Estimating
(38) and (39) separately destroys the cancellation of \(A_s(t)\); keeping
them together gives (40). Here there is indeed a genuine one-sided
conclusion within the exponential subclass. By the Alzer–Kwong theorem
recorded in `104_18` §5,

\[
 F(s)=(s-1)\zeta(s)
 \quad\hbox{is strictly increasing for }s>1,
\]

one has

\[
 M_\Lambda(1+q)={F'(1+q)\over F(1+q)}>0,
 \qquad R(q)=-M_\Lambda(1+q)<0 \quad(q>0).                \tag{40a}
\]

Hence \(\mathfrak M_\varepsilon(e^{-t\,\cdot})=R(\varepsilon+t)<0\)
for every \(t\ge0\). By positive mixtures, the same inequality holds for
every completely monotone test function for which Fubini is justified.

This Laplace-side order cannot be promoted to complete monotonicity of
\(-R\). Indeed, set

\[
 \mathscr M(q):=-R(q)
 ={1\over q}-\sum_{m\ge2}{\Lambda(m)\over m^{1+q}}.
\]

For every integer \(j\ge0\), absolute differentiation gives

\[
 \boxed{
 (-1)^j\mathscr M^{(j)}(q)
 ={j!\over q^{j+1}}
 -\sum_{m\ge2}{\Lambda(m)(\log m)^j\over m^{1+q}}.}         \tag{40b}
\]

Take \(j=32\) and \(q=32/\log2\). The single atom \(m=2\) of the sum is

\[
 { (\log2)^{33}\over2e^{32}},
 \qquad {32!\over q^{33}}
 ={32!(\log2)^{33}\over32^{33}}.                            \tag{40c}
\]

The comparison is exact, with no rationalization of \(\log2\): from
\(e<68/25\) and

\[
 32^{33}25^{32}>2\cdot32!\,68^{32}
\]

it follows that \(32^{33}>2\cdot32!e^{32}\). By (40b)–(40c),

\[
 \boxed{\mathscr M^{(32)}(32/\log2)<0,}                     \tag{40d}
\]

contrary to the sign required by Bernstein's theorem. So, not even
\(-R\) is completely monotone. Moreover, even a positive Laplace
representation would not fix the sign of its pairing with \(L_n\), which
changes sign. Differentiating (40) and recombining it binomially exactly
recomposes the coefficients \(B_n\), not a bound for them. The one-sided
conclusion (40a) is genuine, but it does not reach the polynomial cone
needed for (35).

## 7. Off-line structural falsifier

Keeping a complete coupling does not license an automatic probabilistic
inequality. For \(a>0\), consider

\[
 Z_a(s)=\zeta(s+a)\zeta(s-a),\qquad
 X_a(s)=\xi(s+a)\xi(s-a).                                   \tag{41}
\]

In the half-plane \(\Re s>1+a\), the Dirichlet series of \(Z_a\) has
positive coefficients and

\[
 -{Z_a'\over Z_a}(s)
 =\sum_{m\ge2}{2\Lambda(m)\cosh(a\log m)\over m^s}.         \tag{42}
\]

If \(Z_a(s)=\sum b_a(n)n^{-s}\), then the formal identity
\(-Z_a'=(-Z_a'/Z_a)Z_a\) gives

\[
 b_a(n)\log n
 =\sum_{d\mid n}2\Lambda(d)\cosh(a\log d)\,b_a(n/d).       \tag{43}
\]

Hence (5)–(23), with their corresponding weights, their two poles, and
their Gamma factors, are reproduced for \(X_a\) within that half-plane:
there is size-biased factorization, a positive divisor selector, a
continuous split, and crossed Stein. This claim is local to the domain
where the two polar rates are positive; it does not postulate a positive
probabilistic coupling all the way to the line of symmetry. However,
\(X_a\) has zeros at
\(1/2\pm a+i\gamma\), off that line.

Hence an inference based solely on weight positivity, size-biased
factorization, coupling, Jensen, the segment identity, and Gamma splits
would also apply to falsifier (41). A valid proof of (35) must use an
additional quantitative property specific to

\[
 \Lambda(p^k)=\log p,                                        \tag{44}
\]

capable of correlating the sign changes of (21) with those of the
Laguerre function. The falsifier does not refute an inequality that
genuinely uses (44); it refutes the claim that the crossed Stein
formalism, by itself, supplies the sign.

## 8. Decision

Proved unconditionally:

1. the equal-mass coupling (13)–(17), preserving the
   divisor–cofactor and Gamma–split structure;
2. the canonical local Stein representation (20)–(21), independent of
   the coupling;
3. the real three-sign pattern (29) around the first prime;
4. the exact Laguerre identity (33);
5. the complete recomposition of symbol \(R\) in (40), together with
   the one-sided sign \(R(q)<0\) on exponential tests.

Ruled out:

```text
choosing a better coupling -> positive Stein kernel;
divisor/uniform transport order -> one-sided bound;
automatic local crossed energy -> proportional margin;
separating selector and total -> gain (A_s cancels exactly);
using only positivity/factorization/Gamma -> closure (falsifier X_a).
```

Remains open, with no further reduction:

\[
 \int_0^\infty L_{n-2}^{(2)}(sx)K_s(x)\,dx
 \quad\hbox{with its complete sign},                          \tag{45}
\]

uniformly in \(n\ge150\) as \(s\downarrow1\) is removed. By (33), the
inequality required for (45) is exactly (3), not an already-obtained
weaker condition.

## 9. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 crossed_divisor_gamma_stein_gate_check.py
```

The checker uses only integers and `Fraction`. It verifies the oriented
segment identity, the Laguerre derivative (31), the formal cancellation
(40), the rational implications of the signs (28)–(29), the
complete-non-monotonicity certificate (40c)–(40d), and the abstract
convolution identity underlying (43). It evaluates neither zeta, A1, nor
RH.
</content>
