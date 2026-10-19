# 104_101 — Exact gap coordinate, convexity, and composition gate

## Result

Set

\[
 L(x)=\int_2^x{dt\over\log t},\qquad
 \mathcal E_\pi(N)=\sum_{m=2}^N
 {\{\pi(m)-L(m)\}^2\over m(m+1)}.
 \tag{1}
\]

If \(p_k\) is the \(k\)-th prime and
\(g_k=p_{k+1}-p_k\), define

\[
 c_k=k-L(p_k),\qquad
 \ell_{k,r}=L(p_k+r)-L(p_k)\quad(0\le r\le g_k).
 \tag{2}
\]

Then, with

\[
 R_k(N)=\min\{g_k-1,N-p_k\},
 \tag{3}
\]

one has the exact finite identity

\[
 \boxed{
 \mathcal E_\pi(N)=
 \sum_{p_k\le N}\sum_{r=0}^{R_k(N)}
 {\{c_k-\ell_{k,r}\}^2
  \over(p_k+r)(p_k+r+1)}.}
 \tag{4}
\]

The endpoint values satisfy the recurrence

\[
 \boxed{c_{k+1}=c_k+1-\ell_{k,g_k}.}
 \tag{5}
\]

On a complete cell, set

\[
 w_{k,r}={1\over(p_k+r)(p_k+r+1)},\quad
 W_k=\sum_{r=0}^{g_k-1}w_{k,r}
 ={1\over p_k}-{1\over p_{k+1}},
 \tag{6}
\]

\[
 \bar\ell_k={1\over W_k}\sum_{r=0}^{g_k-1}w_{k,r}\ell_{k,r},\qquad
 V_k=\sum_{r=0}^{g_k-1}w_{k,r}
       (\ell_{k,r}-\bar\ell_k)^2.
 \tag{7}
\]

The cell's contribution is

\[
 \boxed{
 \mathcal E_k=W_k(c_k-\bar\ell_k)^2+V_k.}
 \tag{8}
\]

This is the exact variational form. It is strictly convex in
\(c_k\), but the convexity produces a **minimum**, not an upper bound.
The term that remains to be controlled is the accumulated error \(c_k\), and (5)
shows that this requires cancellation among the biases of many gaps.

The condition "non-primes are composite" does not supply that
cancellation through a convex relaxation. There is an exact dichotomy:

* imposing simultaneously "everything selected is prime" and "everything omitted
  is composite" leaves a feasible set of a single point, the literal prime
  sequence;
* the natural relaxation that preserves any fixed wheel, PNT density, and
  logarithmic gaps admits \(0\)-\(1\) sequences with polynomial
  energy.

More precisely, for every fixed integer \(W\ge2\), every
\(1/2<\beta<1\), and every \(c>0\), there exists a sequence
\(a_n\in\{0,1\}\) such that, writing

\[
 A(x)=\sum_{n\le x}a_n,\qquad
 S(x)=\sum_{2\le n\le x}{1\over\log n},
 \tag{9}
\]

one has

\[
 a_n=1\Longrightarrow(n,W)=1,\qquad
 A(x)=S(x)+cx^\beta+O_{W,\beta,c}(1),
 \tag{10}
\]

and the consecutive gaps of the support are \(O_{W,\beta,c}(\log x)\).
However,

\[
 \boxed{
 \sum_{m\le N}{\{A(m)-S(m)\}^2\over m(m+1)}
 ={c^2\over2\beta-1}N^{2\beta-1}+O_{W,\beta,c}(1).}
 \tag{11}
\]

Since \(S(x)-L(x)\) is bounded, (11) also holds with \(L\). Moreover,
\(x^\beta=o(xe^{-C(\log x)^{3/5}(\log\log x)^{-1/5}})\); so the
model satisfies PNT and any ordinary Vinogradov–Korobov-type envelope,
despite violating the \(N^{o(1)}\) target.

**Verdict.** Rewriting the energy in gaps is exact and useful: it localizes
the obstacle in the accumulated walk (5). But cellular convexity together with
a fixed wheel, PNT/VK, and even \(O(\log x)\) gaps does not force subpolynomial
energy. `104_99` separately covers the stable sieves at level
\(x^{1-\eta}\). The full composition does not yield a new variational
region: it already identifies the prime sequence and returns exactly the
original problem. This is not a universal no-go for every prime-specific
inequality. This document does not prove (1) bounded,
Deep-\(\Lambda\), A1, or RH.

---

## 1. Derivation of the gap identity

If \(p_k\le m<p_{k+1}\), then \(\pi(m)=k\). Writing
\(m=p_k+r\),

\[
 \pi(m)-L(m)
 =k-L(p_k)-\{L(p_k+r)-L(p_k)\}
 =c_k-\ell_{k,r}.
 \tag{12}
\]

The cells \([p_k,p_{k+1}-1]\) partition the integers \(m\ge2\).
Truncating them at \(N\) proves (4). At the next endpoint,

\[
 c_{k+1}
 =k+1-L(p_{k+1})
 =c_k+1-\{L(p_{k+1})-L(p_k)\},
 \tag{13}
\]

which is (5).

The sum of the weights telescopes:

\[
 W_k=\sum_{m=p_k}^{p_{k+1}-1}
 \left({1\over m}-{1\over m+1}\right)
 ={1\over p_k}-{1\over p_{k+1}}.
 \tag{14}
\]

Finally, expanding around the weighted mean gives

\[
 \sum_rw_{k,r}(c_k-\ell_{k,r})^2
 =W_k(c_k-\bar\ell_k)^2
  +\sum_rw_{k,r}(\ell_{k,r}-\bar\ell_k)^2,
 \tag{15}
\]

because the cross term vanishes. This proves (8).

There is a fully discrete version, closer to `104_93`. Set

\[
 d_k=k-S(p_k),\qquad
 h_{k,r}=\sum_{j=1}^r{1\over\log(p_k+j)}.
 \tag{16}
\]

Then (4)–(8) hold with \((c,\ell)\) replaced by \((d,h)\), and

\[
 d_{k+1}=d_k+1-h_{k,g_k}.
 \tag{17}
\]

In particular \(1-h_{k,g_k}\) is the normalized, centered gap; the
endpoint \(d_k\) is its accumulated sum, not a convex function of a single
gap.

## 2. What convexity does say

For \(p_k,p_{k+1}\) fixed, (8) attains its minimum at
\(c_k=\bar\ell_k\), and the minimum is \(V_k\ge0\). Consequently

\[
 \mathcal E_k\ge V_k.
 \tag{18}
\]

The direction is opposite to what is needed. An upper bound requires
controlling \(|c_k-\bar\ell_k|\). By (5), this amounts to controlling

\[
 c_1+\sum_{i<k}\{1-\ell_{i,g_i}\}.
 \tag{19}
\]

Knowing that every interior integer of the cell has a divisor imposes no
sign on (19), nor does it pair the biases of distinct cells. The
inclusion–exclusion that keeps all those divisors is precisely the
complete Eratosthenes identity of `104_99`; truncating it loses the
parity information, and no additional convex inequality appears.

## 3. \(0\)-\(1\) falsifier with wheel and logarithmic gaps

Fix \(W,\beta,c\) as above and define

\[
 F(m)=S(m)+cm^\beta.
 \tag{20}
\]

Enumerate, from a sufficiently large point, the integers coprime to
\(W\):

\[
 r_1<r_2<\cdots,\qquad(r_j,W)=1.
 \tag{21}
\]

One has \(r_{j+1}-r_j\le W\). Moreover,

\[
 F(r_{j+1})-F(r_j)
 \le {W\over\log(r_j+1)}+c\beta W r_j^{\beta-1}=o(1).
 \tag{22}
\]

After raising the starting point, (22) is less than one. Define

\[
 a_{r_j}=\lfloor F(r_j)\rfloor-\lfloor F(r_{j-1})\rfloor,\qquad
 a_n=0\quad(n\notin\{r_j\}).
 \tag{23}
\]

Then \(a_n\in\{0,1\}\). If \(r(x)\) is the largest candidate not exceeding
\(x\), telescoping (23) gives

\[
 A(x)=\lfloor F(r(x))\rfloor+C.
 \tag{24}
\]

Since \(0\le x-r(x)<W\), (22) and (24) prove (10). To see the size of
the support gaps, take \(y=x+3\log x+W\). For \(x\) large,

\[
 F(y-W)-F(x)
 \ge {y-W-x\over\log y}>2.
 \tag{25}
\]

There is a candidate between \(y-W\) and \(y\); by (23), the floor must
jump before \(y\). Thus every support gap starting near \(x\) is
\(O(\log x)\).

From (10),

\[
 A(m)-S(m)=cm^\beta+O(1).
 \tag{26}
\]

Since \(1/2<\beta<1\), the cross terms are summable and

\[
\begin{aligned}
 \sum_{m\le N}{\{A(m)-S(m)\}^2\over m(m+1)}
 &=c^2\sum_{m\le N}m^{2\beta-2}+O(1)\\
 &={c^2\over2\beta-1}N^{2\beta-1}+O(1),
\end{aligned}
\tag{27}
\]

which proves (11).

This falsifier does not claim its points are primes: it proves
exactly that every relaxation that only sees a finite wheel, density, and
gaps is too loose.

## 4. Why the full composition leaves no room for variation

For \(n\ge2\), let \(q_n=\mathbf1_{\mathbb P}(n)\). The elementary factorization gives

\[
 \boxed{
 q_n=\prod_{p\le\sqrt n}(1-\mathbf1_{p\mid n}).}
 \tag{28}
\]

Let \(a_n\in\{0,1\}\). The two exact implications are

\[
 a_n=1\Longrightarrow q_n=1 \quad(a_n\le q_n),
 \qquad
 a_n=0\Longrightarrow q_n=0 \quad(a_n\ge q_n).
 \tag{29}
\]

Imposing both gives \(a_n=q_n\) coordinate by coordinate. The feasible
polytope is the singleton \(\{q\}\); therefore no variational comparison
exists with another configuration that preserves the exact composition.
Evaluating a nontrivial inequality on that singleton is already estimating
the literal prime sequence.

Each half of (29), even accompanied by PNT, is insufficient. This can be
seen without probabilistic models:

* add to all the primes a subsequence of even composite integers whose
  counting function is
  \(C(x)\sim x/\log^2x\). Then every omitted integer is composite and
  \(A^+(x)-L(x)\sim x/\log^2x\);
* delete the primes with indices
  \(k_j=\lfloor j\log j\rfloor\). The amount deleted up to \(x\) is
  \(D(x)\sim\pi(x)/\log\pi(x)\sim x/\log^2x\). Then every selected point
  is prime and
  \(A^-(x)-L(x)\sim-x/\log^2x\).

In both cases PNT remains valid, but

\[
 \sum_{m\le N}{\{A^\pm(m)-L(m)\}^2\over m(m+1)}
 \sim {N\over\log^4N},
 \tag{30}
\]

which is not \(N^{o(1)}\). For the first case, one can pick the even
point \(2j\) each time the floor of \(2j/\log^2(2j)\) increases; this
gives \(C(x)=x/\log^2x+O(1)\). The elementary inversion of
\(j\log j\) proves the asymptotics of the second case. PNT with a
zero-free region gives \(\pi(x)-L(x)=o(x/\log^A x)\) for every \(A\), so
it cannot cancel the added terms.

## 5. Non-duplication audit

`104_93` proves the max identity for the increments
\((\Lambda(n)-1)/\log n\) and the energy equivalence with RH.
`104_94` eliminates the proper prime powers. `104_99` keeps the full
inclusion–exclusion and proves the level-\(x^{1-\eta}\) no-go
via the sequences \(1\pm\lambda_L\).

The additional content of this document is different and narrower:

1. the exact cellular identity (4)–(5) over consecutive gaps;
2. the quadratic completion (8), which decides the direction of
   convexity;
3. the **\(0\)-\(1\)** falsifier (10)–(11), with an arbitrary fixed wheel,
   PNT/VK, and \(O(\log x)\) gaps;
4. the singleton dichotomy (28)–(29) and the PNT falsifiers for each
   one-sided relaxation.

It is not claimed as new that an incomplete sieve does not characterize
the primes, nor is the parity barrier. The new result within the phase is
pinpointing exactly why gap convexity does not give the bound of
`104_93`.

## 6. Reproduction

From `tools/`:

```bash
python3 prime_gap_energy_variational_check.py
```

The checker numerically verifies, up to \(N=200000\), (4), (8), and the
telescoping (6). It then builds the model (23) with
\(W=30\), \(\beta=3/4\), checking support, bounded tracking, and
logarithmic gaps up to \(10^6\). The asymptotic proof is (20)–(27), not an
inference from the finite range.
</content>
