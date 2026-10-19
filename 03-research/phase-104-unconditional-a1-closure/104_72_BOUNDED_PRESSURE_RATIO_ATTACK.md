# 104_72 — Bounded pressure ratio and transition gate

**Result.** For \(\tau>0\), the observable

\[
 g_\tau(x)
 ={1\over\tau}\{\log(1+e^{-x})
 -\log(1+e^{-(x+\tau)})\}
 ={1\over\tau}\int_0^\tau {ds\over1+e^{x+s}}              \tag{1}
\]

lies in \([0,1]\), tends to zero as \(x\to+\infty\) and to one as
\(x\to-\infty\). On the deterministic windows

\[
 I_L=\{L^2,L^2+1,\ldots,L^2+L-1\},                        \tag{2}
\]

if \(x_n=\lambda_n+\log(n+1)\) and

\[
 G_L=\sum_{n\in I_L}g_\tau(x_n),                          \tag{3}
\]

then

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 G_L\longrightarrow0.}                                    \tag{4}
\]

The exponential of \(\tau G_L\) is a ratio of two partitions:

\[
 \boxed{e^{\tau G_L}
 =\prod_{n\in I_L}{1+z_n\over1+e^{-\tau}z_n},\qquad
 z_n={e^{-\lambda_n}\over n+1}.}                          \tag{5}
\]

Each factor lies between \(1\) and \(e^\tau\). So astronomically large
activities saturate instead of exploding.

This is a real quantitative advantage over `104_71`. There, a single
activity \(z_n=e^{-\lambda_n}/(n+1)\) can make the partition grow like
\(e^{-\lambda_n}\); here the same site contributes at most \(e^\tau\).
That is why (5) exactly preserves the density relaxation: it counts how
many sites enter the bad phase, without reweighting their exponential
depth again.

Saturation does not remove the prime–pole conditioning. The transition
occurs when \(z_n\asymp1\), and deciding which side it is on requires
knowing \(Q_{n,\varepsilon}-\{A_n+p_n(\varepsilon)+\log(n+1)\}\) with
additive error \(O(1)\). Its two large terms have size
\(\exp(X^2/100+o(1))\) on the diagonal of 104_69. The bounded ratio
still requires, in that strip, relative precision
\(\exp(-X^2/100+O(1))\).

This document proves the criterion, its diagonal lift, and the
separation no-go. It does not prove that \(G_L\to0\) for zeta, A1, or
RH.

---

## 1. Elementary pressure properties

Set \(q=e^{-\tau}\in(0,1)\) and \(z=e^{-x}\). Then

\[
 g_\tau(x)={1\over\tau}\log{1+z\over1+qz}.                 \tag{6}
\]

Since

\[
 1\le {1+z\over1+qz}\le{1\over q}=e^\tau,
\]

we get \(0\le g_\tau\le1\). Moreover,

\[
 g_\tau(x)\le {1\over\tau}\log(1+z)\le {z\over\tau}.
 \tag{7}
\]

The sensitivity with respect to \(\log z=-x\) is

\[
 {d\over d\log z}\log{1+z\over1+qz}
 ={(1-q)z\over(1+z)(1+qz)}.                               \tag{8}
\]

The maximum is attained at \(z=q^{-1/2}=e^{\tau/2}\), and equals

\[
 \max_{z>0}{(1-q)z\over(1+z)(1+qz)}
 =\tanh{\tau\over4}.                                      \tag{9}
\]

Hence

\[
 |g_\tau'(x)|\le{\tanh(\tau/4)\over\tau}< {1\over4}.
 \tag{10}
\]

The derivative tends to zero at both ends. All the sign information
lives in a strip of width \(O_\tau(1)\) around
\(x=-\tau/2\), or equivalently \(z=e^{\tau/2}\).

---

## 2. Window criterion

**Theorem 2.1.** (4) holds. More precisely:

* under RH,
  \[
   0\le G_L\le {L\over\tau(L^2+1)}=O_\tau(L^{-1});         \tag{11}
  \]
* if RH is false, there exist \(M<\infty\) and \(L_0\) such that
  \[
   \liminf_{L\to\infty}{G_L\over L}\ge {1\over M}>0.       \tag{12}
  \]

**Proof.** Under RH, \(\lambda_n\ge0\), so
\(z_n\le1/(n+1)\). Equations (2) and (7) give

\[
 G_L\le {1\over\tau}\sum_{n\in I_L}{1\over n+1}
 \le {L\over\tau(L^2+1)}.
\]

If RH is false, 104_56 provides \(c>0\), \(R>1\), a
syndetic set \(D\), and a gap bound \(M\), such that
\(\lambda_n\le-cR^n\) on \(D\). Every subinterval of \(M\) integers in
\(I_L\) contains a \(d\in D\). At those indices,

\[
 x_d\le-cR^d+\log(d+1)\longrightarrow-\infty,
\qquad g_\tau(x_d)\longrightarrow1.                       \tag{13}
\]

Splitting \(I_L\) into \(\lfloor L/M\rfloor\) disjoint subintervals,
for every \(\delta>0\) and all sufficiently large \(L\) one gets
\(G_L\ge(1-\delta)\lfloor L/M\rfloor\). Dividing by \(L\) and then
letting \(\delta\downarrow0\) proves (12). In particular
\(\liminf G_L\ge1\), and (4) follows.
\(\square\)

Ratio (5) is obtained by summing (6). From \(0\le g_\tau\le1\),

\[
 1\le e^{\tau G_L}\le e^{\tau L}.                         \tag{14}
\]

Under RH the ratio tends to one. Under non-RH it grows at least like
\(\exp\{(\tau/M+o(1))L\}\).

---

## 3. Prime–Laguerre lift with a single diagonal

Let

\[
 X_L=L^2+L-1,\qquad
 \varepsilon_L=e^{-X_L/100}.                              \tag{15}
\]

For \(L\ge8\), \(X_L\ge70\), so
\(\varepsilon_L\le1/2\). Use

\[
\begin{aligned}
 \lambda_{n,\varepsilon_L}
 &=A_n+p_n(\varepsilon_L)-Q_{n,\varepsilon_L},\\
 Q_{n,\varepsilon_L}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon_L}}
 L_{n-1}^{(1)}(\log m).
\end{aligned}                                             \tag{16}
\]

With

\[
 r={199\over200},\qquad
 \eta={1\over100}-\log{200\over199}>0,\qquad
 M_0=M_{199/200},
\]

104_66 gives, uniformly for \(n\in I_L\),

\[
 |\lambda_{n,\varepsilon_L}-\lambda_n|
 \le2M_0X_Le^{-\eta X_L}.                                 \tag{17}
\]

Define \(x_{n,\varepsilon_L}=
\lambda_{n,\varepsilon_L}+\log(n+1)\) and

\[
 G_{L,\varepsilon_L}
 =\sum_{n\in I_L}g_\tau(x_{n,\varepsilon_L}).              \tag{18}
\]

By (10) and (17),

\[
 \boxed{
 |G_{L,\varepsilon_L}-G_L|
 \le {2M_0L X_L\tanh(\tau/4)\over\tau}
 e^{-\eta X_L}\longrightarrow0.}                         \tag{19}
\]

So RH is also equivalent to \(G_{L,\varepsilon_L}\to0\).

Set

\[
 z_{n,\varepsilon_L}
 ={e^{-A_n-p_n(\varepsilon_L)}\over n+1}
 \prod_{m\ge2}\exp\!\left(
 {\Lambda(m)\over m^{1+\varepsilon_L}}
 L_{n-1}^{(1)}(\log m)\right).                            \tag{20}
\]

For each \(L\), the product converges absolutely and
\(z_{n,\varepsilon_L}=e^{-\lambda_{n,\varepsilon_L}}/(n+1)>0\).
The exact regulated ratio is

\[
\boxed{
 e^{\tau G_{L,\varepsilon_L}}
 =\prod_{n\in I_L}
 {1+z_{n,\varepsilon_L}
  \over1+e^{-\tau}z_{n,\varepsilon_L}}.}                  \tag{21}
\]

There is no internal limit \(\varepsilon\downarrow0\). Each factor of
(21) stays in \([1,e^\tau]\), even when the activity of (20) is huge.

---

## 4. Does the bounded ratio improve the conditioning?

### 4.1 What does improve relative to `104_71`

The partition of `104_71` contains the unbounded factor \(1+z_n\). An
excursion \(-\lambda_n\asymp R^n\) produces a factor of order
\(\exp(R^n)\), so depth and frequency get mixed. Instead,

\[
 {1+z_n\over1+e^{-\tau}z_n}\longrightarrow e^\tau
 \qquad(z_n\to\infty).                                  \tag{22a}
\]

A deep bad site and an even deeper one have the same asymptotic cost.
That is why the ratio's growth is linear in the number of bad sites on
a logarithmic scale, as shown by (12) and (31), instead of being
dominated by the worst excursion. This improvement is what allows using
the density/syndeticity conclusion of `104_56` without again requiring
an individual bound on \(e^{-\lambda_n}\).

### 4.2 What does not improve: the paired transition

Write

\[
 C_{n,\varepsilon}
 =A_n+p_n(\varepsilon)+\log(n+1),\qquad
 Q=Q_{n,\varepsilon}.
\]

Then

\[
 z_{n,\varepsilon}=e^{Q-C_{n,\varepsilon}},
\]

and the factor of (21) can be written without a separate activity:

\[
 \mathcal R_\tau(C,Q)
 ={e^C+e^Q\over e^C+e^{-\tau}e^Q}
 ={1+e^{Q-C}\over1+e^{-\tau}e^{Q-C}}.                    \tag{22}
\]

The common translation disappears:

\[
 \mathcal R_\tau(C+T,Q+T)=\mathcal R_\tau(C,Q).            \tag{23}
\]

This explains the saturation, but also locates the missing
information: only the signed difference

\[
 Q-C=-\{\lambda_{n,\varepsilon}+\log(n+1)\}.               \tag{24}
\]

matters.

**Lemma 4.1 (separation instability).** For \(a>0\) and any
\(T\in\mathbb R\),

\[
\begin{aligned}
 \mathcal R_\tau(T,T-a)
 &={1+e^{-a}\over1+e^{-\tau-a}}\longrightarrow1,\\
 \mathcal R_\tau(T,T+a)
 &={1+e^{a}\over1+e^{a-\tau}}\longrightarrow e^\tau
\end{aligned}
 \qquad(a\to\infty).                                      \tag{25}
\]

The two input pairs differ only by \(2a\) in coordinate \(Q\),
regardless of the common size \(T\). If \(|T|\to\infty\) and
\(a=o(|T|)\), their relative perturbation tends to zero while the
outputs remain separated by \(e^\tau-1+o(1)\).

On diagonal (15), at \(n=X_L\),

\[
 \log|p_n(\varepsilon_L)-1|
 ={X_L^2\over100}+o(1).                                   \tag{26}
\]

The prime channel has the same dominant term and (24) is its finite
difference. Taking, for example, \(a=X_L\), the lemma shows that
distinguishing between the two saturated zones requires relative
precision

\[
 \boxed{\exp\{-X_L^2/100+O(\log X_L)\}.}                   \tag{27}
\]

To resolve the transition strip itself, \(Q-C=O_\tau(1)\), the cost is
even

\[
 \boxed{\exp\{-X_L^2/100+O(1)\}.}                          \tag{28}
\]

The ratio cancels the **value** of an activity already identified as
huge, but does not allow deciding whether it is huge or tiny without
first knowing the sign of the complete difference. Taking moduli or
bounding \(C\) and \(Q\) separately does not determine (22).

This is a no-go for channel separation. It does not rule out a signed
identity that directly estimates \(Q-C\) or the complete product (21).

---

## 5. Falsifier quadruple

For

\[
 Q_n^{\mathrm{off}}
 =4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\},              \tag{29}
\]

one has

\[
 g_\tau(Q_n^{\mathrm{off}}+\log(n+1))
 \longrightarrow
 \begin{cases}
 1,&n\equiv0\pmod4,\\
 0,&n\not\equiv0\pmod4.
 \end{cases}                                               \tag{30}
\]

Every block \(I_L\) contains \(L/4+O(1)\) multiples of four. Hence

\[
 \boxed{
 {G_L^{\mathrm{off}}\over L}\longrightarrow{1\over4},
 \qquad
 e^{\tau G_L^{\mathrm{off}}}
 =\exp\{(\tau/4+o(1))L\}.}                                \tag{31}
\]

The ratio stays within the ceiling \(e^{\tau L}\), but quantitatively
rejects the off-line divisor.

---

## 6. Verdict

**Proved:** criterion (4), linear dichotomy (11)--(12), bounded ratio
(5)/(14), diagonal lift (19)--(21), separation lemma (25)--(28), and
quadruple (31).

**Gain:** replacing the positive partition by a pressure ratio removes
the exterior explosion of large activities and produces uniformly
bounded factors.

**No-go:** the transition depends exclusively on the complete
prime–pole difference. Subsequent saturation does not reduce the
precision needed to decide its sign.

**Not proved:** \(G_L\to0\) from the real weights \(\Lambda(m)\), A1,
or RH.

---

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 bounded_pressure_ratio_check.py
```

The checker verifies (1), the bounds on each factor, the sensitivity
maximum, the dichotomy of Lemma 4.1, the quadruple, and the diagonal
scale. The asymptotic theorems are proved in the text.
