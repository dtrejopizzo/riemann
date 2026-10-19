# 104_68 — Deterministic block criterion and prime–Laguerre polymer

**Result.** The abstract existence of good blocks from `104_61` can be
replaced by a fully deterministic sequence:

\[
 I_L=\{L^2,L^2+1,\ldots,L^2+L-1\}.                         \tag{1}
\]

Define

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},
 \qquad
 P_L=\prod_{n\in I_L}(1-a_n).                              \tag{2}
\]

Then

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \sum_{n\in I_L}a_n\longrightarrow0
 \quad\Longleftrightarrow\quad
 P_L\longrightarrow1.}                                     \tag{3}
\]

If RH is false the opposite dichotomy occurs:

\[
 \liminf_{L\to\infty}\sum_{n\in I_L}a_n\geq1,
 \qquad P_L\longrightarrow0.                               \tag{4}
\]

The inverse of \(P_L\) has an exact finite-polymer expansion and a
prime–Laguerre lift that keeps the pole, archimedean block, primes, and
prime powers together. Moreover, the regulator can be diagonalized with
the window: a single sequence of absolutely convergent Euler products is
obtained, with no interior limit. The expansion does not yet deliver a
bound: it is a gas without interactions whose partition function again
factors degree by degree. All the difficulty remains inside the paired
activity of each degree. This document proves (3)--(4), not A1 nor RH.

---

## 1. Why deterministic windows suffice

Set

\[
 x_n=\lambda_n+\log(n+1),\qquad
 z_n=e^{-x_n}={e^{-\lambda_n}\over n+1}.                    \tag{5}
\]

Then

\[
 a_n={z_n\over1+z_n},\qquad
 1-a_n={1\over1+z_n}
 ={1\over1+e^{-(\lambda_n+\log(n+1))}}.                    \tag{6}
\]

### 1.1 RH direction

Under RH, \(\lambda_n\geq0\), so

\[
 0\leq a_n\leq{1\over n+2},\qquad
 0\leq z_n\leq{1\over n+1}.                               \tag{7}
\]

Since \(|I_L|=L\) and \(n\geq L^2\) in (1),

\[
 \boxed{
 \sum_{n\in I_L}a_n
 \leq{L\over L^2+2}\leq{1\over L}.}                      \tag{8}
\]

For numbers \(0\leq a_n<1\),

\[
 1-\sum_{n\in I_L}a_n
 \leq\prod_{n\in I_L}(1-a_n)\leq1.                       \tag{9}
\]

Equations (8)--(9) give \(P_L\to1\).

### 1.2 Non-RH direction

If RH is false, `104_56` produces \(R>1\), \(c>0\), an integer \(M\) and
a syndetic set \(D\), after a prefix, such that

\[
 \lambda_n\leq-cR^n\qquad(n\in D).                         \tag{10}
\]

Every sufficiently distant interval of \(M\) integers contains an
element of \(D\). Hence, for every sufficiently large \(L\geq M\) there
exists

\[
 d_L\in I_L\cap D.                                         \tag{11}
\]

At that index,

\[
 1-a_{d_L}
 ={(d_L+1)e^{\lambda_{d_L}}
   \over1+(d_L+1)e^{\lambda_{d_L}}}
 \leq(d_L+1)e^{-cR^{d_L}}\longrightarrow0,                 \tag{12}
\]

and hence \(a_{d_L}\to1\). It follows that

\[
 \sum_{n\in I_L}a_n\geq a_{d_L}\longrightarrow1
 \quad\text{from below},                                   \tag{13}
\]

while

\[
 0<P_L\leq1-a_{d_L}\longrightarrow0.                      \tag{14}
\]

This proves (4) and the reverse implications of (3). No subsequence
adapted to the zeros is chosen: the quadratic windows (1) automatically
intercept any syndetic set.

The power two is not essential. The same proof holds for any
deterministic family of consecutive intervals \(J_k\) satisfying

\[
 |J_k|\longrightarrow\infty,\qquad
 { |J_k|\over\min J_k}\longrightarrow0.                    \tag{14a}
\]

The first condition intercepts every syndetic set under non-RH; the
second makes \(\sum_{n\in J_k}(n+2)^{-1}=o(1)\) under RH. Choice (1) is
the simplest integer normalization and avoids any adaptive parameter.

### 1.3 Internal equivalence between sum and product

The equivalence of the two limits of (3) uses no Li coefficients. From
(6),

\[
 -\log P_L=\sum_{n\in I_L}\log(1+z_n),                     \tag{15}
\]

and for \(z\geq0\),

\[
 {z\over1+z}\leq\log(1+z)\leq z.                          \tag{16}
\]

So

\[
 \sum_{n\in I_L}a_n\leq-\log P_L.                         \tag{17}
\]

The implication \(P_L\to1\Rightarrow\sum a_n\to0\) follows from (17);
the other already follows from (9). The logistic normalization hides no
spike: a single \(a_n\to1\) forces the product to zero.

---

## 2. Exact polymer expansion

By (5)--(6),

\[
 \boxed{
 P_L^{-1}
 =\prod_{n\in I_L}(1+z_n)
 =\sum_{S\subseteq I_L}
 \exp\!\left(-\sum_{n\in S}
 \{\lambda_n+\log(n+1)\}\right).}                         \tag{18}
\]

The empty set contributes one. If the activity of a polymer
\(S\) is defined by

\[
 Z(S)=\prod_{n\in S}{e^{-\lambda_n}\over n+1},             \tag{19}
\]

(18) is the partition function of a lattice gas with occupation zero or
one. All weights are positive. Under RH, (7) gives

\[
 0\leq P_L^{-1}-1
 \leq\exp\!\left(\sum_{n\in I_L}z_n\right)-1
 \leq e^{1/L}-1.                                           \tag{20}
\]

If RH is false, the site \(d_L\) of (11) has

\[
 z_{d_L}\geq{e^{cR^{d_L}}\over d_L+1},                    \tag{21}
\]

so \(P_L^{-1}\geq1+z_{d_L}\to\infty\).

---

## 3. Regulated prime–Laguerre lift

Use the convention of `104_61`:

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 ={}&A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 ={}&\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}&\longrightarrow\lambda_n.
                                                               \tag{22}
\end{aligned}
\]

For \(\varepsilon>0\), set

\[
 z_{n,\varepsilon}
 ={e^{-A_n-p_n(\varepsilon)}\over n+1}
 \prod_{m\geq2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right).                             \tag{23}
\]

The product converges absolutely in the logarithm and
\(z_{n,\varepsilon}=e^{-\lambda_{n,\varepsilon}}/(n+1)\).
Since \(I_L\) and its power set are finite for each \(L\), one can
pass to the boundary term by term:

\[
\boxed{
\begin{aligned}
 P_L^{-1}
 =\lim_{\varepsilon\downarrow0}
 \sum_{S\subseteq I_L}
 &{\exp\!\left(-\sum_{n\in S}
       \{A_n+p_n(\varepsilon)\}\right)
  \over\prod_{n\in S}(n+1)}\\
 &\times\prod_{m\geq2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon}}
 \sum_{n\in S}L_{n-1}^{(1)}(\log m)\right).
                                                               \tag{24}
\end{aligned}}
\]

Equation (24) keeps, for each polymer, the pole, the archimedean
block, all the primes, and all the prime powers together until after
summing the degrees of the polymer. The order of limits is binding:

\[
 \varepsilon\downarrow0\quad\text{with }L\text{ fixed},
 \qquad\text{then }L\to\infty.                           \tag{25}
\]

No uniformity allowing them to be swapped has been proved.

### 3.1 Single diagonal for the quadratic windows

The Cauchy estimate of `104_66` removes the double limit of (25). Set

\[
 N_L=L^2+L-1,\qquad \varepsilon_L=e^{-N_L/100},
 \qquad r={199\over200},
 \qquad \eta={1\over100}-\log{200\over199}>0.              \tag{25a}
\]

There is a fixed constant \(M=M_{199/200}<\infty\) such that, for
sufficiently large \(L\) and every \(n\in I_L\),

\[
 |\lambda_{n,\varepsilon_L}-\lambda_n|
 \le 2MN_Le^{-\eta N_L}=:\delta_L.                        \tag{25b}
\]

Define

\[
 a_{n,\varepsilon_L}={1\over1+(n+1)e^{\lambda_{n,\varepsilon_L}}},
 \qquad
 P_{L,\varepsilon_L}=\prod_{n\in I_L}(1-a_{n,\varepsilon_L}). \tag{25c}
\]

The logistic is \(1/4\)-Lipschitz. Moreover, for vectors with
coordinates in \([0,1]\), the difference of their products is bounded
by the sum of the coordinate-wise differences. Hence

\[
\begin{aligned}
 \left|\sum_{n\in I_L}a_{n,\varepsilon_L}
       -\sum_{n\in I_L}a_n\right|
 &\le {L\delta_L\over4},\\
 |P_{L,\varepsilon_L}-P_L|
 &\le {L\delta_L\over4},
\end{aligned}                                             \tag{25d}
\]

and the right-hand side tends exponentially to zero. Consequently,

\[
\boxed{
 \mathrm {RH}
 \Longleftrightarrow
 \sum_{n\in I_L}a_{n,\varepsilon_L}\longrightarrow0
 \Longleftrightarrow
 P_{L,\varepsilon_L}\longrightarrow1.}                   \tag{25e}
\]

For each \(L\), the formula with no interior limit is

\[
\boxed{
 P_{L,\varepsilon_L}^{-1}
 =\sum_{S\subseteq I_L}
 {e^{-\sum_{n\in S}(A_n+p_n(\varepsilon_L))}
  \over\prod_{n\in S}(n+1)}
 \prod_{m\ge2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon_L}}
 \sum_{n\in S}L_{n-1}^{(1)}(\log m)\right).}             \tag{25f}
\]

The sum over \(S\) is finite and each Euler product converges absolutely.
The diagonal (25a) does not prove (25e); it only places the exact
criterion inside a single convergent arithmetic family.

---

## 4. Audit: the polymer creates no new arithmetic interaction

Despite the sum over subsets, (18) is a gas **without interaction**:

\[
 \log P_L^{-1}=\sum_{n\in I_L}\log(1+z_n).                 \tag{26}
\]

The cross terms of (18) are exactly products of individual activities;
they disappear upon taking the logarithm. There is no reserve connected
across degrees that could pay for a bad site. This distinguishes (24)
from a genuine cluster expansion with signed interaction.

Moreover, all the terms of (18) are positive. An upper bound
\(P_L^{-1}=1+o(1)\) already forces each activity to be small:

\[
 0\leq z_n\leq P_L^{-1}-1\qquad(n\in I_L).                \tag{27}
\]

In particular, (20) cannot be obtained by canceling distinct polymers.
The only available cancellation is the internal one of (23), between
\(p_n(\varepsilon)\) and the Mangoldt sum, before exponentiating.

For fixed \(n\), both parts have size \(\varepsilon^{-n}\). Separating
the factors of (23) produces exponents of that size and loses the
finite part, as already quantified by `104_61` and `104_63`. Grouping
several degrees into \(S\) does not change this fact: the maximum degree
of \(S\) dominates the divergence if the channels are estimated
separately.

Hence (24) contributes a **deterministic target**, but not a bounding
mechanism. Proving from (24) that

\[
 \boxed{P_L^{-1}=1+o(1)}                                    \tag{28}
\]

is exactly the new formulation sufficient for RH.

---

## 5. Off-line falsifier

For the rational quadruple of `104_17`,

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\}.            \tag{29}
\]

Every interval of four integers contains a \(d\equiv0\pmod4\), and at
that index \(-Q_d\geq2^d\). Hence, for every \(L\geq4\), there is
\(d_L\in I_L\) such that

\[
 1-a_{d_L}
 \leq(d_L+1)e^{-2^{d_L}},\qquad
 P_L\leq(d_L+1)e^{-2^{d_L}}\longrightarrow0.               \tag{30}
\]

The deterministic criterion rejects the quadruple in **every** large
window, not just on average or on a subsequence.

---

## 6. Verdict

**Proved.** The deterministic criterion (3), the strong dichotomy (4),
the polymer expansion (18), the prime–Laguerre lift (24), the single
diagonal (25e)--(25f), and the falsifier (30).

**Gain.** There is no longer an existential selector of intervals: the
explicit family \([L^2,L^2+L-1]\) suffices. The target is a positive
scalar limit, \(P_L^{-1}\to1\), with an exact finite arithmetic
expansion.

**No-go.** The polymer is non-interacting. The positivity of its
activities prevents canceling subsets, and the factorization returns
the difficulty to each paired prime–pole activity. Presenting (18) as a
new interaction would be incorrect.

**Not proved.** (28) for the real weights \(\Lambda(m)\), a new block of
coefficients, A1, or RH.

---

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 deterministic_block_polymer_check.py
```

The checker uses `Fraction`. It verifies the RH model bound (8), the
identities (6), (9), (15)--(18) for rational activities, that every
\(I_L\) with \(L\geq4\) intercepts the bad class of the quadruple, and
the exact bound \(-Q_d\geq2^d\). It also checks the telescoping product
inequality used in (25d) and the decay of the diagonal envelope. It does
not certify the arithmetic limit (28).
