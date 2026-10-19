# 104_75 — Hard transition in \(\log X\), poissonization, and the Bessel gate

**Result.** The Fermi mean of `104_69` can be replaced, without losing
the equivalence with RH, by a one-sided density statement for the
prime--pole real block. A fully explicit choice is

\[
 B_X=\sqrt{\log(X+e)},\qquad
 \Delta_X(B_X)={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le B_X\}}.                 \tag{1}
\]

Then

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Delta_X(B_X)\longrightarrow0.}                          \tag{2}
\]

With the diagonal \(\varepsilon_X=e^{-X/100}\), (2) is exactly equivalent to

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)-B_X
 \right\}}\longrightarrow0,                              \tag{3}
\]

where

\[
 Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).                                   \tag{4}
\]

Thus the missing input is not an additive \(O(1)\) bound for each
degree: (3) is the exact hard layer of Fermi. §2.1 weakens it even
further: it suffices to exclude, in logarithmic density, overshoots of
size \(e^{\sqrt X}\).

The same frontier admits a poissonized version, localized at degrees
\(n=t+O(\sqrt t)\). In that coordinate the **first linear mean** of the
prime--Laguerre coefficients has a closed Bessel transform. The
off-line quartet shows, however, that this linear mean does not
control the transition: its poissonized linear mean tends to \(4\),
while its Fermi detector tends to \(1/4\). Therefore Abel, Borel,
Nörlund--Rice, or the Bessel identity, used only at first order, do
not prove (3).

This document identifies the minimal input that remains on the
\(\log X\) route and closes off the linear poissonized attack. It does
not prove (3), A1, or RH.

**No internal duplication.** `104_62` studies the Fourier
representation of the logistic function and its microfrequency;
`104_63`, a dyadic quadratic energy; `104_69`, the finite diagonal in
logarithmic mean; and `104_73`, the Bernstein representation of the
pressure ratio. Here the new pieces are the moving hard level
(10)--(22), the poissonized localization, and the exact Bessel--Fermi
contrast (38)/(42).

---

## 1. Exact hard layer of the Fermi mean

Set

\[
 x_n=\lambda_n+\log(n+1),\qquad
 a_n={1\over1+e^{x_n}},\qquad
 \mathfrak F(X)={1\over H_X}\sum_{n\le X}{a_n\over n}.   \tag{5}
\]

For \(B\ge0\), define

\[
 \Delta_X(B)={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{x_n\le B\}}.                              \tag{6}
\]

**Lemma 1.1 (transition sandwich).** For all \(X\) and \(B\ge0\),

\[
 \boxed{{1\over2}\Delta_X(0)\le\mathfrak F(X)
 \le\Delta_X(B)+e^{-B}.}                                 \tag{7}
\]

Moreover,

\[
 \boxed{
 \mathfrak F(X)\to0
 \quad\Longleftrightarrow\quad
 \text{there exists }B_X\to\infty\text{ with }\Delta_X(B_X)\to0.} \tag{8}
\]

**Proof.** If \(x\le0\), then
\((1+e^x)^{-1}\ge1/2\). If \(x>B\), then
\((1+e^x)^{-1}\le e^{-x}\le e^{-B}\). This proves (7).

The right-to-left implication in (8) follows from (7). For the
converse, fix an integer \(k\ge1\). On \(x_n\le k\),

\[
 a_n\ge{1\over1+e^k},
 \qquad \Delta_X(k)\le(1+e^k)\mathfrak F(X)\longrightarrow0. \tag{9}
\]

Choose an increasing \(X_k\) such that
\(\Delta_X(k)\le1/k\) for \(X\ge X_k\), and set \(B_X=k\) on
\([X_k,X_{k+1})\). Then \(B_X\to\infty\) and
\(\Delta_X(B_X)\to0\). \(\square\)

The lemma separates two questions that the smooth form mixes
together: the value of the logistic function far from its transition
is harmless; all the content lies in the density of the degrees that
cross the level \(x_n=B\).

---

## 2. An explicit moving level

The criterion does not need to choose \(B_X\) after knowing the
sequence.

**Theorem 2.1.** Let \(B_X\ge0\) be any function such that

\[
 B_X\longrightarrow\infty,
 \qquad B_X=o(\log X).                                    \tag{10}
\]

Then

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Delta_X(B_X)\longrightarrow0.}                         \tag{11}
\]

In particular, the choice in (1) works.

**Proof.** Under RH, \(\lambda_n\ge0\). Therefore

\[
 x_n\le B_X\quad\Longrightarrow\quad
 n+1\le e^{B_X}.
\]

Hence

\[
 \Delta_X(B_X)
 \le {H_{\lfloor e^{B_X}\rfloor}\over H_X}
 \le {B_X+O(1)\over\log X+O(1)}\longrightarrow0.          \tag{12}
\]

If RH is false, `104_56` gives \(c>0\), \(R>1\), and a set
\(D\) of logarithmic density \(d>0\) such that

\[
 \lambda_n\le-cR^n\qquad(n\in D)                          \tag{13}
\]

from a fixed index on. Set

\[
 Y_X=\left\lceil{3\log\log(X+e^e)\over\log R}\right\rceil. \tag{14}
\]

For \(n\in D\cap[Y_X,X]\), (10), (13), and
\(R^{Y_X}\ge\{\log(X+e^e)\}^3\) give, for large \(X\),

\[
 x_n\le-cR^n+\log(X+1)\le B_X.                            \tag{15}
\]

The harmonic mass removed by \(n<Y_X\) is
\(H_{Y_X}=O(\log\log\log X)=o(H_X)\). Hence

\[
 \liminf_{X\to\infty}\Delta_X(B_X)\ge d>0,              \tag{16}
\]

contradicting the limit in (11). \(\square\)

The proof only uses the exponential, positive-density signature of an
exterior zero. It does not use coefficient-by-coefficient positivity
of Li in the non-RH direction.

### 2.1 An even weaker gate: tolerance \(e^{\sqrt X}\)

To prove RH it is not even necessary to control the Fermi transition.
Fix \(0<\alpha<1\), set \(S_X=e^{X^\alpha}\), and define

\[
 \Omega_X^{(\alpha)}
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le-S_X\}}.                \tag{16a}
\]

Then

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Omega_X^{(\alpha)}\longrightarrow0.}                  \tag{16b}
\]

Under RH the indicator is identically zero. If RH is false, take
\(D,c,R\) as in (13) and choose \(K>1/\log R\). For
\(n\in D\cap[KX^\alpha,X]\),

\[
 cR^n\ge 2e^{X^\alpha}+\log(X+1)                         \tag{16c}
\]

from some \(X\) on. The logarithmic density of \(D\) gives

\[
 {1\over H_X}\sum_{\substack{KX^\alpha\le n\le X\\n\in D}}{1\over n}
 \longrightarrow d(1-\alpha)>0.                          \tag{16d}
\]

By (13), these indices are counted in (16a), which proves the opposite
direction.

The concrete choice \(\alpha=1/2\) shows the true weakness of the
input: it suffices to exclude, in logarithmic density, prime--pole
overshoots of size \(e^{\sqrt X}\). There is no need to decide the
sign or obtain an additive error \(O(1)\) in the transition strip.

---

## 3. Diagonal translation to the real weights \(\Lambda(m)\)

Use `104_69`,

\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)-Q_{n,\varepsilon},
 \qquad \varepsilon_X=e^{-X/100}.                         \tag{17}
\]

There it is proved, with \(\eta=1/100-\log(200/199)>0\) and a constant
\(M_0=M_{199/200}<\infty\),

\[
 \delta_X:=\sup_{n\le X}
 |\lambda_{n,\varepsilon_X}-\lambda_n|
 \le2M_0Xe^{-\eta X}\longrightarrow0.                    \tag{18}
\]

Define \(x_{n,\varepsilon}=\lambda_{n,\varepsilon}+\log(n+1)\) and

\[
 \Delta_{X,\varepsilon}(B)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{x_{n,\varepsilon}\le B\}}.              \tag{19}
\]

For large \(X\), \(\delta_X<1\), and therefore

\[
 \boxed{
 \Delta_X(B-1)\le\Delta_{X,\varepsilon_X}(B)
 \le\Delta_X(B+1).}                                      \tag{20}
\]

If \(B_X\) satisfies (10), so do \(B_X\pm1\). Theorem
2.1 and (20) prove

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \Delta_{X,\varepsilon_X}(B_X)\longrightarrow0.}        \tag{21}
\]

The statement is a logical equivalence of the two criteria, not the
false estimate
\(\Delta_{X,\varepsilon_X}(B_X)-\Delta_X(B_X)\to0\): a hard indicator
is not Lipschitz and may have mass exactly at the transition. The two
inclusions at levels \(B_X\pm1\), together with the "for every level
satisfying (10)" quantifier of Theorem 2.1, are precisely what avoids
that illegitimate jump.

Finally,

\[
 x_{n,\varepsilon_X}\le B_X
 \quad\Longleftrightarrow\quad
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)-B_X,                    \tag{22}
\]

which proves (3). For each \(X\), (4) converges absolutely. The target
(3) keeps the pole, Gamma, primes, and prime powers together in a
single signed comparison; only afterward does it count the degrees
that violate it.

The even weaker variant of (16b) has the arithmetic form

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}
 \right\}}\longrightarrow0.}                            \tag{22a}
\]

The equivalence with RH follows from (16b), but, since the observable
is a hard indicator, it is not enough to informally compare the error
\(o(1)\) with the size of the threshold. Set \(S_X=e^{\sqrt X}\), and
denote by

\[
 \Omega_X(S)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le-S\}},
\]

and by \(\Omega_{X,\varepsilon_X}(S)\) the same expression with
\(\lambda_{n,\varepsilon_X}\). When \(\delta_X<1\), (18) gives

\[
 \boxed{
 \Omega_X(S_X+1)
 \le \Omega_{X,\varepsilon_X}(S_X)
 \le \Omega_X(S_X-1).}                                  \tag{22b}
\]

Under RH, \(\lambda_n\ge0\), and the three events are empty for large
\(X\). If RH is false, use (13) on the set \(D\), and fix
\(K>1/\log R\). For
\(n\in D\cap[K\sqrt X,X]\), both \(S_X+1\) and \(S_X-1\) are
negligible compared with \(cR^n\). By partial summation and the natural
density \(d\) of \(D\),

\[
 {1\over H_X}\sum_{\substack{K\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                           \tag{22c}
\]

Therefore both ends of (22b) have positive lower limit under non-RH,
and the central observable tends to zero if and only if RH holds. This
rigorously proves the diagonal lift of (16b). Between (3) and (22a),
the second is the logically weaker arithmetic target.

---

## 4. Localized poissonization of the same gate

Let \(N_t\sim\mathrm{Pois}(t)\) and define

\[
 \mathfrak P(t)=e^{-t}\sum_{n\ge1}{t^n\over n!}
 {1\over1+(n+1)e^{\lambda_n}}.                            \tag{23}
\]

**Theorem 4.1.** One has

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak P(t)\longrightarrow0.}                        \tag{24}
\]

**Proof.** Under RH, the summand is at most \(1/(n+2)\), so that

\[
 0\le\mathfrak P(t)
 \le\mathbb E{1\over N_t+1}
 ={1-e^{-t}\over t}\longrightarrow0.                     \tag{25}
\]

Suppose RH false and use the syndetic set \(D\) of (13), with gaps at
most \(M_D\). On \(D\), the summand of (23) tends uniformly to one in
the tail. In the window

\[
 J_t=[t-2\sqrt t,t+2\sqrt t]\cap\mathbb N,                \tag{26}
\]

the ratio between two Poisson masses separated by at most \(M_D\)
tends uniformly to one. Split \(J_t\) into blocks of \(M_D\) integers
and choose an element of \(D\) in each block. Since

\[
 \mathbb P(N_t\in J_t)\ge {3\over4}                       \tag{27}
\]

by Chebyshev, and the two edge fragments have mass \(o(1)\), there
exists \(c_{M_D}>0\) such that

\[
 \liminf_{t\to\infty}\mathbb P(N_t\in D)\ge c_{M_D}.   \tag{28}
\]

Therefore \(\liminf\mathfrak P(t)\ge c_{M_D}>0\). \(\square\)

The same proof, replacing the logistic function by the indicator,
gives for any \(B_t\to\infty\), \(B_t=o(\log t)\),

\[
 \boxed{
 \mathrm {RH}\Longleftrightarrow
 e^{-t}\sum_{n\ge1}{t^n\over n!}
 {\bf1}_{\{\lambda_n+\log(n+1)\le B_t\}}
 \longrightarrow0.}                                      \tag{29}
\]

In the RH direction, the event forces
\(N_t\le e^{B_t}=t^{o(1)}\), whose probability tends to zero. In the
opposite direction, the event contains \(D\cap J_t\) for large \(t\).

### 4.1 A single Euler diagonal

Set

\[
 K_t=\lceil2t\rceil,
 \qquad \varepsilon_t=e^{-K_t/100},                       \tag{30}
\]

and truncate (23) at \(1\le n\le K_t\), replacing
\(\lambda_n\) by \(\lambda_{n,\varepsilon_t}\). Call the result
\(\mathfrak P_{\rm diag}(t)\). From (18), applied with \(X=K_t\), and
from the \(1/4\)-Lipschitz property of the logistic function,

\[
 |\mathfrak P_{\rm diag}(t)-\mathfrak P(t)|
 \le {M_0\over2}K_te^{-\eta K_t}
 +\mathbb P(N_t>K_t).                                     \tag{31}
\]

The Chernoff bound

\[
 \mathbb P(N_t\ge2t)\le(e/4)^t                            \tag{32}
\]

makes (31) tend to zero. For the hard detector, define

\[
 \mathfrak D_{\rm diag}(t,B)
 =e^{-t}\sum_{1\le n\le K_t}{t^n\over n!}
 {\bf1}_{\{\lambda_{n,\varepsilon_t}+\log(n+1)\le B\}}.
 \tag{32a}
\]

When the uniform error of (18) is less than one,

\[
 \mathfrak D(t,B-1)-\mathbb P(N_t>K_t)
 \le\mathfrak D_{\rm diag}(t,B)
 \le\mathfrak D(t,B+1),                                  \tag{32b}
\]

where \(\mathfrak D(t,B)\) denotes the infinite sum of (29) at level
\(B\). Since \(B_t\pm1\) still satisfies the hypotheses of (29), the
diagonal hard detector is also equivalent to RH. Thus (24) and (29)
admit a finite outer sum and a single absolutely convergent Euler
series for each \(t\).

---

## 5. The linear Bessel transform

Poissonization does exactly simplify the **first moment** of the
prime--Laguerre block. For \(u>0\),

\[
 \boxed{
 \sum_{n\ge1}{t^n\over n!}L_{n-1}^{(1)}(u)
 =e^t\sqrt{t\over u}\,J_1(2\sqrt{tu}).}                  \tag{33}
\]

The value at \(u=0\) is understood by continuity. The identity follows
by comparing the series

\[
 J_1(2\sqrt{tu})
 =\sum_{j\ge0}{(-1)^j(tu)^{j+1/2}\over j!(j+1)!}.         \tag{34}
\]

For \(\varepsilon>0\), absolute convergence allows interchanging sums
to obtain

\[
\boxed{
 e^{-t}\sum_{n\ge1}{t^n\over n!}Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 \sqrt{t\over\log m}\,
 J_1(2\sqrt{t\log m}).}                                  \tag{35}
\]

Here the convergence needed for the interchange is not deduced from a
Bessel cancellation. Indeed, setting \(u=\log m\), the finite Laguerre
expansion gives

\[
 \sum_{n\ge1}{t^n\over n!}|L_{n-1}^{(1)}(u)|
 \le e^t\sqrt{t\over u}\,I_1(2\sqrt{tu})
 \le C_t e^{2\sqrt{tu}}.
\]

For every \(\varepsilon>0\), the inequality
\(2\sqrt{tu}\le(\varepsilon/2)u+2t/\varepsilon\) then reduces the
absolute double series to a constant times
\(\sum_m\Lambda(m)m^{-1-\varepsilon/2}<\infty\). Hence (35) is a
legitimate identity of absolutely convergent series, not a formal
rearrangement.

The pole also sums exactly. From the binomial definition,

\[
 p_n(\varepsilon)=1-\left(1-{1\over\varepsilon}\right)^n
 =1+(-1)^{n-1}\left({1-\varepsilon\over\varepsilon}\right)^n,
\]

and therefore

\[
 \boxed{
 e^{-t}\sum_{n\ge1}{t^n\over n!}p_n(\varepsilon)
 =1-e^{-t/\varepsilon}.}                                  \tag{36}
\]

Equations (35)--(36) give a closed, fully arithmetic linear transform.
They do not give a bound for the indicator of (29): the operation
\(x\mapsto{\bf1}_{x\le B}\), or its Fermi smoothing, is applied
**before** averaging.

---

## 6. Exact no-go for the first moment

Consider the rational quartet

\[
 q_n=4-2\mathrm{Re}\,\{w^n+w^{-n}\},
 \qquad w=2i.                                             \tag{37}
\]

Its poissonized linear mean has the exact formula

\[
\boxed{
 e^{-t}\sum_{n\ge1}{q_nt^n\over n!}
 =4-2\mathrm{Re}\,\left\{
 e^{(w-1)t}+e^{(w^{-1}-1)t}\right}\longrightarrow4.}    \tag{38}
\]

By contrast, with

\[
 a_n^q={1\over1+(n+1)e^{q_n}},                            \tag{39}
\]

one has

\[
 a_n^q\longrightarrow
 \begin{cases}
 1,&n\equiv0\pmod4,\\
 0,&n\not\equiv0\pmod4.
 \end{cases}                                              \tag{40}
\]

The root-of-unity filter formula gives

\[
 \mathbb P(N_t\equiv r\!\!\pmod4)
 ={1\over4}\sum_{j=0}^3i^{-rj}e^{t(i^j-1)}\longrightarrow{1\over4}. \tag{41}
\]

Consequently,

\[
 \boxed{e^{-t}\sum_{n\ge1}{a_n^qt^n\over n!}
 \longrightarrow{1\over4}.}                              \tag{42}
\]

The extremely permissive gate (16a) also rejects the quartet. For
\(\alpha=1/2\), only the class \(n\equiv0\pmod4\) contributes, and the
condition holds from \(n=(1/\log2+o(1))\sqrt X\) on. By harmonic
summation,

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{q_n+\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow{1\over8}.}                              \tag{42a}
\]

Indeed, the multiples of four contribute
\(\frac14\{\log X-\frac12\log X+O(1)\}\), and the other three classes
do not cross the threshold.

The contrast (38)/(42) is the requested falsifier: the first Bessel
mean is positive, bounded, and asymptotically harmless, while one
quarter of the degrees crosses the transition by an exponential
distance. Therefore no Tauberian inference based **solely on a bound
or an asymptotic of that first mean** can go from (35), or from an
equivalent linear Nörlund--Rice continuation, to (29) without an
additional one-sided hypothesis. This does not claim that the full
transform, known exactly for every \(t\), loses information: like any
exponential transform of a sequence of admissible growth, it can be
inverted coefficient by coefficient. The no-go concerns precisely the
first-order use.

This does not refute a new nonlinear identity acting directly on the
paired block. It specifies what its output must be: (3), or its
poissonized version (29).

---

## 7. Verdict

**Proved:** the sandwich (7), the explicit moving level (11), its
exact diagonal lift (21)--(22), the poissonized criterion (24)/(29),
the finite diagonal (31), the Bessel transform (35), the pole (36),
and the falsifier (38)--(42).

**Real reduction:** it is no longer necessary to control
\(Q_{n,\varepsilon}-A_n-p_n(\varepsilon)\) with error \(O(1)\) for
each \(n\). The exact layer is (3), but to prove RH the much weaker
target (22a) suffices: overshoots larger than \(e^{\sqrt X}\) must
occupy zero logarithmic density.

**No-go:** the first linear mean, even though it has the exact Bessel
identity, does not control that density. The missing piece is a
one-sided large-deviation inequality for the full prime--pole
difference, even at the extremely permissive level (22a). A
second-moment bound at the correct scale, for example

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 \left(
 Q_{n,\varepsilon_X}-A_n-p_n(\varepsilon_X)-\log(n+1)
 \right)_+^2
 =o(e^{2\sqrt X}),
\]

would suffice by Chebyshev, but `104_63` proves that
bare Parseval/Christoffel--Darboux again requires the same signed
cancellation.

**Not proved:** (3), (29), A1, or RH.

---

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 poisson_logx_hard_transition_check.py
```

The checker verifies (33), (36), (38), the equidistribution of the
classes modulo four, the Fermi limit of the quartet, and the
approximation to the deep limit \(1/8\) of (42a).
