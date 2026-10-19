# 104_60 — Nonlinear degree-barrier criterion

**Result.** The syndetic criterion of `104_56` allows weakening the front
much further than "\(D_n>0\) in density one." Let

\[
 D_n:=4\lambda_n-A_n,
 \qquad A_n>0\quad(n\ge150),                         \tag{1}
\]

and let \(b_n>0\) be any subexponential scale:

\[
 \log b_n=o(n).                                      \tag{2}
\]

Then RH is equivalent to the deep excursions
\(D_n\le-b_n\) having lower density zero. It is even equivalent to finding
**one** sequence of consecutive intervals, increasingly longer and farther
out, on which the saturated barrier

\[
 \boxed{
 H_{n,b}:={(-D_n)_+\over b_n+(-D_n)_+}}             \tag{3}
\]

vanishes on average. This does not prove that the real barrier tends to
zero and hence does not prove RH. It does rigorously change the arithmetic
theorem that would suffice to prove: it is no longer necessary to obtain a
sign, a proportional margin, or even a polynomial bound for every degree.
It suffices to exclude, in local average, a positive density of negative
excursions larger than a scale as large as

\[
 b_n=\exp\!\left({n\over\log\log(n+e^e)}\right).     \tag{4}
\]

The construction is nonlinear, one-sided and saturated. It falls outside
both the linear averages of `104_17` and the classification of additive
polynomial identities of `104_53`.

---

## 1. Dominant input and why the scale can be almost exponential

Theorem 3.1 of `104_56` proves the following. If RH is false, there exist
\(R>1\), \(c>0\), an integer \(L\ge1\), a syndetic set
\(\mathcal S\subset\mathbb N\) with gaps at most \(L\), and \(n_0\),
such that

\[
 \boxed{
 D_n\le-cR^n\qquad(n\in\mathcal S,\ n\ge n_0).}    \tag{5}
\]

Indeed, there it is proved that
\(\lambda_n\le-c_0R^n\) on a syndetic set of returns; since
\(A_n=O(n\log n)\), (5) follows by shrinking \(c_0\) and increasing \(n_0\).

If (2) holds and \(a=\log R>0\), then, for \(n\) sufficiently large,

\[
 b_n\le e^{an/2},\qquad {cR^n\over b_n}\longrightarrow\infty. \tag{6}
\]

This is the conceptual gain: a falsity of RH does not produce only a
small violation of (1), but excursions of a fixed exponential rate on a
set with bounded gaps. Any barrier of rate \(o(n)\) ends up negligible
against them.

---

## 2. Deep-excursion criterion

For \(E_b:=\{n\ge150:D_n\le-b_n\}\), write

\[
 \underline d(E_b)
 :=\liminf_{N\to\infty}{1\over N}\#(E_b\cap[1,N]). \tag{7}
\]

**Theorem 2.1 (lower-density corollary of the Bombieri–Lagarias
modes).** For every positive
sequence \(b_n\) satisfying (2), the following are equivalent:

1. RH;
2. \(\underline d(E_b)=0\);
3. there exist consecutive integer intervals \(I_j\), with
   \(\min I_j\to\infty\) and \(|I_j|\to\infty\), such that

   \[
   {1\over|I_j|}\#(E_b\cap I_j)\longrightarrow0.    \tag{8}
   \]

**Proof.** Under RH,
\(\lambda_n=A_n+O(\sqrt n\log n)\), so
\(D_n=3A_n+O(\sqrt n\log n)>0\) for all sufficiently large \(n\).
So \(E_b\) is finite and 2 and 3 hold.

Now suppose RH is false. By (5)--(6), after increasing \(n_0\),

\[
 \mathcal S\cap[n_0,\infty)\subset E_b.             \tag{9}
\]

Every interval of \(L\) integers contains an element of \(\mathcal S\).
Hence

\[
 \#(E_b\cap[M+1,M+H])\ge {H\over L}-2             \tag{10}
\]

for \(M\ge n_0\). Equation (10) gives
\(\underline d(E_b)\ge1/L>0\) and forbids (8) for any sequence of
intervals whose length tends to infinity. \(\square\)

Condition 2 is notably weaker than zero natural density: it only
requires a subsequence of initial scales where the proportion approaches
zero. Condition 3 is even more local: it allows choosing the intervals.
Syndeticity of the obstruction is what makes these relaxations
sufficient.

---

## 3. Saturated barrier: a nonlinear average equivalent to RH

Define \(H_{n,b}\) by (3). We have

\[
 0\le H_{n,b}<1,\qquad
 H_{n,b}=0\iff D_n\ge0.                             \tag{11}
\]

However we will not require each term to vanish.

**Theorem 3.1 (nonlinear interval barrier).** Fixing any
scale (2), the following are equivalent:

1. RH;
2. \(\displaystyle
   \liminf_{N\to\infty}{1\over N}\sum_{n=150}^NH_{n,b}=0\);
3. there exist intervals \(I_j\) as in Theorem 2.1 such that

   \[
   \boxed{
   {1\over|I_j|}\sum_{n\in I_j}H_{n,b}\longrightarrow0.} \tag{12}
   \]

**Proof.** Under RH, (11) is eventually zero. If RH is false,
(5)--(6) give, uniformly for \(n\in\mathcal S\) and \(n\to\infty\),

\[
 H_{n,b}\ge {cR^n\over b_n+cR^n}\longrightarrow1. \tag{13}
\]

Hence \(H_{n,b}\ge1/2\) on the tail of \(\mathcal S\). Combining this
with (10), every average over a long and distant interval has
lower limit at least \(1/(2L)\). The same holds for the initial
averages. This contradicts 2 or 3. \(\square\)

The theorem remains valid if (3) is replaced by any saturation function
\(\Phi((-D_n)_+/b_n)\) with
\(\Phi(0)=0\) and \(\Phi(x)\to\ell>0\) as \(x\to\infty\).

A smooth version is logistic. If

\[
 \mathcal L_{n,\tau}:={1\over1+\exp(\tau D_n/b_n)}, \tag{14}
\]

then RH is equivalent to the existence of intervals \(I_j\) as above and
numbers \(\tau_j\to\infty\) for which the average of
\(\mathcal L_{n,\tau_j}\) over \(I_j\) tends to zero. Under RH,
\(D_n/b_n\) can tend to zero if \(b_n\) is huge, so in this
formulation \(\tau_j\) must be chosen after the interval, e.g.
so that
\(\tau_j\min_{n\in I_j}D_n/b_n\to\infty\). This choice exists because
the minimum is positive on a tail. Under non-RH, (13) forces the
logistic to one on the syndetic set, whatever \(\tau_j\ge1\) is.

The rational barrier (3) is preferable: it contains no such auxiliary
quantifier and already delivers the exact equivalence.

---

## 4. Translation to the real arithmetic block

To avoid the historical clash of the letter \(B_n\), set

\[
 \mathscr P_n:=A_n-\lambda_n.                       \tag{15}
\]

This is the full prime–Laguerre functional, with pole, Gamma, prime
powers, and boundary terms reassembled before estimating. From (1),

\[
 -D_n=4\mathscr P_n-3A_n.                           \tag{16}
\]

The new sufficient arithmetic theorem can be stated with no zeros:

> **Boundary 104_60.** For some sequence \(b_n=e^{o(n)}\), construct
> integer intervals \(I_j\) with
> \(\min I_j,|I_j|\to\infty\) and prove
> \[
> \boxed{
> {1\over|I_j|}\sum_{n\in I_j}
> {\bigl(4\mathscr P_n-3A_n\bigr)_+
>  \over
>  b_n+\bigl(4\mathscr P_n-3A_n\bigr)_+}
> \longrightarrow0.}                               \tag{17}
> \]

By Theorem 3.1, (17) proves RH. Unlike the previous front, (17)
simultaneously allows:

* bad degrees, even in a proportion not controlled a priori;
* frequent polynomial or subexponential deficits;
* absence of a uniform coefficient-by-coefficient bound;
* an almost-exponential scale \(b_n\) like (4).

It only forbids excursions of a fixed exponential rate occupying a
positive local density. That is exactly the signature left by any
zero off the line.

The layer identity

\[
 {x_+\over1+x_+}
 =\int_0^\infty{\mathbf1_{\{x>t\}}\over(1+t)^2}\,dt \tag{18}
\]

shows that (17) is an integrated bound for the exceedance densities

\[
 4\mathscr P_n-3A_n>t b_n.                         \tag{19}
\]

Thus a real route toward (17) would be a large-deviation inequality
**one-sided in the index \(n\)** for the complete prime functional. A
linear average of \(\mathscr P_n\) does not suffice.

---

## 5. Audit against `104_17` and `104_53`

### 5.1 It is not Abel–Fejér nor a linear window

`104_17` proves that partial sums, triangular averages, and Abel
positivity can hide exponentially negative coefficients. Operation (3)
does the opposite:

1. it discards the positive part, which cannot compensate for a failure;
2. it divides by the amplitude so that a single huge spike does not
   substitute for a density of spikes;
3. it averages only after those two operations.

Hence it cannot be recovered from a linear average. Replacing (3) by
\(( -D_n)_+\) would give a valid but much stronger criterion: it would
lose the saturation and go back to paying the exponential amplitude that
the density criterion does not need.

### 5.2 It is not an additive polynomial identity

`104_53` classifies polynomials in moments that are additive within a
fixed degree. The map

\[
 x\longmapsto{x_+\over b+x_+}                      \tag{20}
\]

is not polynomial, is not additive, and is applied to the sequence of
degrees after exactly reassembling \(\mathscr P_n\). No polynomial can
reproduce (20) over the whole line: (20) vanishes on a half-line and
saturates on the other. Approximating it on a compact set also fails to
control the falsifier, whose argument grows like \(R^n\).

This places (17) outside the classification theorem. It does not mean
`104_53` supplies (17): the one-sided arithmetic inequality remains
entirely open.

### 5.3 Jensen does not recover the sign

The barrier is flat for \(x\le0\) and concave for \(x>0\), with a change
of slope at zero. It is neither globally convex nor globally concave. So
there is no Jensen transfer from
\(\sum_{n\in I}\mathscr P_n\). This gap is necessary: a bound obtained
only from the first average would fall back into `104_17`.

---

## 6. Exact off-line falsifier

Use the rational quadruple of `104_17`, for which

\[
 w=2i,\qquad
 Q_n=4-2\mathrm{Re}(w^n+w^{-n}),\qquad
 D_n^{\mathcal O}=4Q_n.                            \tag{21}
\]

Then

\[
 D_n^{\mathcal O}<0\iff n\equiv0\pmod4,            \tag{22}
\]

and, on that class,

\[
 -D_n^{\mathcal O}\asymp2^n.                       \tag{23}
\]

For any \(b_n=e^{o(n)}\), the corresponding barrier tends to one
on \(n\equiv0\pmod4\) and is zero on the other three classes. Hence

\[
 \boxed{
 {1\over N}\sum_{n\le N}
 {(-D_n^{\mathcal O})_+\over
  b_n+(-D_n^{\mathcal O})_+}\longrightarrow{1\over4}.} \tag{24}
\]

The mechanism does not "pass" the target for the off-line divisor: it
rejects it with exact density \(1/4\). In particular it passes the
falsifier that the positive Abel averages of `104_17` do not pass.

---

## 7. What was obtained and what remains open

It is proved that:

1. the term-by-term positive margin can be replaced by the absence, in
   lower density, of excursions deeper than **any** prefixed
   subexponential scale;
2. a single sequence of good intervals suffices, not the whole half-line;
3. the saturated barrier (17) is an exact, nonlinear criterion that
   passes the off-line quadruple and does not belong to the families
   ruled out by `104_17` or `104_53`.

Not proved:

\[
 \text{the arithmetic estimate (17) for the real weights }\Lambda(m).
\]

That is now a strictly weaker front than term-by-term A1. The new
object is not another positive identity: it is a one-sided, saturated,
degree-local large deviation, applied to the complete prime functional
before any compensation between signs is allowed.

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 nonlinear_degree_barrier_check.py
```

The checker uses `Fraction`. It verifies (21)--(24) for the rational
quadruple, the bad class mod four, and exact barrier bounds with
polynomial normalization. It does not certify (17) for zeta.
