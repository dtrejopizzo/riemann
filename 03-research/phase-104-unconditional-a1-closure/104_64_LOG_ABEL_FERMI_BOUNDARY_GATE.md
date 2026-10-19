# 104_64 — Logarithmic Abel and doubly logarithmic Fermi layer gate

**Status.** The Fermi average of `104_61` can be Abelized without
losing or gaining content: for the bounded term, zero Cesàro logarithmic
average and zero Abel logarithmic average are equivalent. This allows
inserting the exact prime–Laguerre product into an infinite, still
bounded, outer sum, and reduces the target to a single radial
approximation.

Abelization does not prove the limit. The off-line rational quadruple
produces a new quantitative obstruction: its negative Fermi correction is
spread uniformly over the scale

\[
 \alpha={\log\log(1/s)\over\log(1/h)},\qquad q=e^{-h},
 \quad 0\leq\alpha\leq1.
\]

Controlling frequencies only up to \(s=\exp(-h^{-\alpha})\), with
\(\alpha<1\) fixed, lets a positive proportion of the bad class's
correction escape. To capture all of it one must reach
\(s=\exp(-c/h)\). The conclusion is a **stop-gate** for a truncated
Abel–Fourier transfer; it is not a no-go for a new cancellation that
simultaneously preserves all classes and all arithmetic channels.

**Attribution.** The equivalence between the logarithmic Cesàro and
Abel methods belongs to classical summability theory; see Bingham–Gashi,
[DOI 10.1016/j.jmaa.2014.08.031](https://doi.org/10.1016/j.jmaa.2014.08.031).
Here only the positive zero-limit specialization is proved directly and
applied to the Li–Fermi detector. No novelty is claimed for the
summability theorem.

---

## 1. The Fermi criterion in Abel coordinates

Fix \(t>0\), and write

\[
 b_n=\log(n+1),\qquad
 a_n={1\over1+\exp(t(\lambda_n+b_n))},\qquad 0\leq a_n\leq1.
 \tag{1}
\]

For \(X\geq1\) and \(h>0\), define

\[
 S(X)=\sum_{n\leq X}{a_n\over n},\qquad
 H_X=\sum_{n\leq X}{1\over n},
 \tag{2}
\]

\[
 L(h)=\sum_{n\geq1}{e^{-hn}\over n}
      =-\log(1-e^{-h}),\qquad
 \mathfrak A_t(h)={1\over L(h)}
 \sum_{n\geq1}{e^{-hn}a_n\over n}.
 \tag{3}
\]

**Theorem 1.1 (Abel–Cesàro for the bounded detector).** We have

\[
 \boxed{
 {S(X)\over H_X}\longrightarrow0
 \quad\Longleftrightarrow\quad
 \mathfrak A_t(h)\longrightarrow0\quad(h\downarrow0).}
 \tag{4}
\]

Moreover, for the Li coefficients,

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \liminf_{h\downarrow0}\mathfrak A_t(h)=0.}
 \tag{5}
\]

**Proof.** Suppose first that \(S(X)=o(\log X)\). Abel summation
gives

\[
 \sum_{n\geq1}{e^{-hn}a_n\over n}
 =(1-e^{-h})\sum_{N\geq1}e^{-hN}S(N).
 \tag{6}
\]

Given \(\epsilon>0\), the prefix where
\(S(N)\leq\epsilon\log N\) is not yet known contributes \(O_\epsilon(h)\).
On the rest one uses

\[
 (1-e^{-h})\sum_{N\geq1}e^{-hN}\log(N+1)
 =\log(1/h)+O(1),
 \tag{7}
\]

while \(L(h)=\log(1/h)+O(h)\). This proves the forward implication of
(4).

Conversely, take \(h=1/X\). For \(n\leq X\),
\(e^{-hn}\geq e^{-1}\), and hence

\[
 S(X)\leq e\,L(1/X)\mathfrak A_t(1/X).
 \tag{8}
\]

Since \(L(1/X)\sim H_X\), the other implication follows.

Under RH, \(\lambda_n\geq0\), so
\(a_n\leq(n+1)^{-t}\), and the numerator of (3) stays bounded as
\(h\downarrow0\). So \(\mathfrak A_t(h)\to0\). If RH is false, Theorem
3.1 of `104_56` gives a set \(D\) of natural density
\(d>0\) on which \(a_n\to1\). Partial summation gives

\[
 \liminf_{h\downarrow0}{1\over L(h)}
 \sum_{n\in D}{e^{-hn}\over n}=d,
 \tag{9}
\]

and hence \(\liminf\mathfrak A_t(h)\geq d>0\). This proves (5).
\(\square\)

In particular, to prove RH it suffices to find **one** sequence
\(h_j\downarrow0\) along which \(\mathfrak A_t(h_j)\to0\). This is a
genuine reduction of the quantifier, but not an estimate of the average.
The sequence can be prescribed: for example,

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak A_t(2^{-j})\longrightarrow0\quad(j\to\infty).}
 \tag{9a}
\]

There is no hidden favorable later selection in (9a): under
\(\neg\mathrm {RH}\), the lower bound of (9) holds uniformly as
\(h\downarrow0\), and hence over any prescribed sequence.

---

## 2. Exact prime–Laguerre form of the Abel average

Use the paired regularization of `104_61`:

\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)
 -\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),
 \qquad
 \lambda_{n,\varepsilon}\to\lambda_n.
 \tag{10}
\]

Since the logistic lies between zero and one and
\(\sum e^{-hn}/n=L(h)<\infty\), dominated convergence gives the identity

\[
\boxed{
\begin{aligned}
 \mathfrak A_t(h)
 =\lim_{\varepsilon\downarrow0}{1\over L(h)}
 \sum_{n\geq1}{e^{-hn}\over n}
 \Bigg[1+e^{t(A_n+b_n+p_n(\varepsilon))}
 \prod_{m\geq2}\exp\!\left(
 -{t\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right)\Bigg]^{-1}.
\end{aligned}}
 \tag{11}
\]

For each \(\varepsilon>0\), the inner product converges absolutely.
Equation (11) keeps the pole, the archimedean block, the primes, and
the prime powers together until after applying the nonlinearity. Unlike
`104_61`, (20c), the outer sum is already infinite; passing to the
boundary is legitimate precisely because the observable is bounded.

There is also a unitary version. For \(N<\infty\), set

\[
 \mathcal C_{h,N,\varepsilon}(s)
 ={1\over L(h)}\sum_{n\leq N}{e^{-hn}\over n}
 e^{ist(\lambda_{n,\varepsilon}+b_n)}.
 \tag{12}
\]

The Fourier formula of `104_62` implies, with the order of limits as
written,

\[
 \boxed{
 \mathfrak A_t(h)
 ={1\over2}-\lim_{N\to\infty}\lim_{\varepsilon\downarrow0}
 \int_0^\infty
 {\mathrm{Im}\,\mathcal C_{h,N,\varepsilon}(s)
  \over\sinh(\pi s)}\,ds.}
 \tag{13}
\]

In (12), each exponential carries the unitary prime–Laguerre product of
`104_62`, (8). In (13) the boundary
\(\varepsilon\downarrow0\), the infinite sum, and \(s\downarrow0\) are
not interchanged: that interchange is exactly the layer audited next.

---

## 3. Off-line quadruple and the nested-layer law

Use the exact falsifier

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\}.
 \tag{14}
\]

If \(4\mid n\), define

\[
 Y_n=-\{Q_n+\log(n+1)\}
 =2(2^n+2^{-n})-4-\log(n+1).
 \tag{15}
\]

For \(n\geq4\), \(Y_n\geq2^n\). Let

\[
 J_n(\delta)=\int_\delta^\infty
 {\sin(stY_n)\over\sinh(\pi s)}\,ds.
 \tag{16}
\]

The full integral satisfies

\[
 J_n(0)={1\over2}\tanh{tY_n\over2}\longrightarrow{1\over2}.
 \tag{17}
\]

Moreover,

\[
 \left|J_n(\delta)\right|\leq1,
 \tag{18}
\]

because, if \(\delta tY_n\leq1\), the amount subtracted from (17) is an
integral of modulus at most \(tY_n\delta/\pi\), and, if
\(\delta tY_n>1\), integration by parts from `104_62`, (15), gives
\(2/(tY_n\sinh(\pi\delta))<2/\pi\).

For \(0<\alpha<1\), set

\[
 \delta_\alpha(h)=\exp(-h^{-\alpha})
 \tag{19}
\]

and consider only the Fourier correction of the negative class:

\[
 T_\alpha(h)={1\over L(h)}
 \sum_{\substack{n\geq4\\4\mid n}}{e^{-hn}\over n}
 J_n(\delta_\alpha(h)).
 \tag{20}
\]

**Theorem 3.1 (doubly logarithmic layer law).** For every
\(0<\alpha<1\),

\[
 \boxed{T_\alpha(h)\longrightarrow{\alpha\over8}
 \qquad(h\downarrow0).}
 \tag{21}
\]

The boundary values, understood as limits, are \(0\) for
\(\alpha=0\) and \(1/8\) for \(\alpha=1\).
In particular, the discarded window \(0<s<\delta_\alpha(h)\) contains
exactly the complementary proportion:

\[
 {1\over L(h)}
 \sum_{\substack{n\geq4\\4\mid n}}{e^{-hn}\over n}
 \{J_n(0)-J_n(\delta_\alpha(h))\}
 \longrightarrow {1-\alpha\over8}.
 \tag{21a}
\]

**Proof.** For \(0<\beta\leq1\), the progression \(4\mid n\) satisfies

\[
 {1\over L(h)}\sum_{\substack{n\leq h^{-\beta}\\4\mid n}}
 {e^{-hn}\over n}\longrightarrow{\beta\over4}.
 \tag{22}
\]

If \(\beta<1\), this follows from \(e^{-hn}=1+o(1)\) uniformly in the
range and from the harmonic sum over a progression; for \(\beta=1\), the
tail with \(n\asymp h^{-1}\) only changes the \(O(1)\) term, not the
coefficient of \(\log(1/h)\).

Fix \(0<\eta<\min(\alpha,1-\alpha)\). Uniformly for
\(n\leq h^{-(\alpha-\eta)}\), one has

\[
 \delta_\alpha(h)tY_n
 \leq\exp\{-h^{-\alpha}+O(h^{-(\alpha-\eta)})\}\longrightarrow0,
 \tag{23}
\]

so \(J_n(\delta_\alpha(h))=1/2+o(1)\), except for a prefix of normalized
weight zero. Uniformly for
\(n\geq h^{-(\alpha+\eta)}\), the integration-by-parts bound gives

\[
 |J_n(\delta_\alpha(h))|
 \leq {2\over\pi tY_n\delta_\alpha(h)}=o(1).
 \tag{24}
\]

By (18), the intermediate strip costs at most

\[
 {1\over4}\{(\alpha+\eta)-(\alpha-\eta)\}+o(1)
 ={\eta\over2}+o(1).
 \tag{25}
\]

The part up to \(h^{-(\alpha-\eta)}\) contributes
\((\alpha-\eta)/8+o(1)\). Since \(J_n(\delta)\) has no fixed sign, the
intermediate strip must also be subtracted in the lower bound. Equations
(22)--(25) give precisely

\[
 {\alpha-\eta\over8}-{\eta\over2}+o(1)
 \leq T_\alpha(h)\leq
 {\alpha-\eta\over8}+{\eta\over2}+o(1).
\]

Letting \(\eta\downarrow0\) gives (21). For \(\alpha=0\),
\(\delta_0=e^{-1}\) is fixed and integration by parts bounds the
numerator of (20), so the ratio tends to zero. For
\(\alpha=1\), the range \(n\leq h^{-(1-\eta)}\) contributes
\((1-\eta)/8+o(1)\); the remaining strip up to the Abel scale
\(n\asymp h^{-1}\) has normalized harmonic mass at most
\(\eta/4+o(1)\), and the tail \(n\gg h^{-1}\) contributes \(O(1/L(h))\).
Letting \(\eta\downarrow0\) gives \(1/8\). \(\square\)

Equivalently, the correction is distributed uniformly in the
coordinate

\[
 \alpha={\log\log(1/s)\over\log(1/h)}.
 \tag{26}
\]

A bound controlling only \(s\geq h^B\) corresponds to
\(\alpha\to0\) and asymptotically sees no part of (20). To capture
all of the bad class's correction one must reach
\(\alpha=1\), i.e. \(s=\exp(-c/h)\) on the Abel scale.

---

## 4. What cancels and what does not in the complete quadruple

Law (21) deliberately refers to the class \(n\equiv0\pmod4\). In the
complete quadruple,

\[
 \begin{array}{c|c|c}
 n\bmod4&Q_n&[1+e^{t(Q_n+b_n)}]^{-1}\\ \hline
 0&-2^{n+1}+O(\log n)&1+o(1)\\
 1,3&4&(n+1)^{-t}(1+o(1))\\
 2&+2^{n+1}+O(\log n)&o(1).
 \end{array}
 \tag{27}
\]

Hence the Abel average of the falsifier satisfies

\[
 \boxed{
 {1\over L(h)}\sum_{n\geq1}{e^{-hn}\over n}
 {1\over1+e^{t(Q_n+b_n)}}\longrightarrow{1\over4}.}
 \tag{28}
\]

Indeed, classes \(1,3\) give a convergent series, class \(2\)
gives \(O(1)\), and the deficit from one in class \(0\) is also
summable. The numerator is therefore

\[
 \sum_{4\mid n}{e^{-hn}\over n}+O_t(1)
 =-{1\over4}\log(1-e^{-4h})+O_t(1)
 ={1\over4}L(h)+O_t(1).
 \tag{28a}
\]

The microfrequency corrections of classes \(0\) and \(2\) obey the
same law (21) with opposite signs within the Fourier formula; they
cancel in the complete average. This cancellation matters: (21) does
not authorize separating classes, zeros, or channels in a proof for
zeta. What it does prove is that any argument discarding the region
\(s<\exp(-h^{-\alpha})\) **before** proving that cancellation loses an
order-one quantity on an admissible falsifier.

Thus Abelization does not turn (11) into a linear estimate, nor does it
allow using the radial continuation of `104_17`. The quadruple has a
positive linear Abel germ, a \(1/4\) Fermi average, and a nested
nonlinear layer extending to \(e^{-c/h}\).

---

## 5. Verdict

**Proved.** The Abel–Cesàro equivalence (4), the subsequence
criterion (5), the exact prime–Laguerre Abel form (11), the unitary
formula with the order of limits made explicit (13), the layer
law (21), and the off-line value (28).

**Gain.** The target can be sought over a single radial sequence
\(h_j\downarrow0\), and the outer arithmetic observable can be made
infinite without losing dominated convergence. The correct variable for
a low-frequency audit is doubly logarithmic, not \(s\), nor
\(s/h\), nor the fixed diagonal rate of `104_62`.

**Not proved.** An upper bound for (11), the vanishing of
\(\mathfrak A_t(h)\), A1, or RH. Layer (21) shows that a truncated
frequency estimate needs a uniform cancellation before truncating; it
does not construct that cancellation for the real weights \(\Lambda(m)\).

---

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 log_abel_fermi_boundary_check.py
```

The checker numerically illustrates the trend to the limit \(1/4\) of
(28), the harmonic law (22), and the approximation of (21) via the exact
transition \(J_n(0)=\tfrac12\tanh(tY_n/2)\). The limit proofs are
in the text; sampling is not used as a certificate.
