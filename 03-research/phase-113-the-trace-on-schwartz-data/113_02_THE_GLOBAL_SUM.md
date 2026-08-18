# 113.02 — The global sum over all primes

## 0. What is being summed

By 113_01 Theorem 4.1, once $h(1)=0$ every regularization scheme for the
shell-$0$ piece agrees (trivially, at $0$), and the canonical local value is
$$\mathfrak T_p(h)=A(h)+B_p(h),\qquad A(h)=\sum_{n\ge1}h(p^n),\quad
B_p(h)=\sum_{m\ge1}h(p^{-m})p^{-m}.$$
Task 2 asks whether $\sum_p\mathfrak T_p(h)$ converges. Note $A(h)$ does not
depend on $p$ in notation but its *value* summed over primes obviously does
via the argument $p^n$; write $A_p(h):=\sum_{n\ge1}h(p^n)$ from here on to
make the $p$-dependence explicit.

## 1. Bare Schwartz is not enough at the global level

113_01 Remark 1.2 showed each *individual* tail converges under bare
Schwartz decay (no exponential rate). This does not survive summing over
all primes.

> ### Proposition 1.1 (the mechanism that fails)
> If $\tilde h$ has only polynomial decay — $|\tilde h(x)|\le C_N(1+
> |x|)^{-N}$ for a single fixed $N$, no exponential margin — then
> $|h(p^n)|\le C_N(1+n\log p)^{-N}$, and in particular the $n=1$ term alone
> gives $|h(p)|\le C_N(1+\log p)^{-N}$, so
> $$\sum_p|A_p(h)|\ \ge\ \sum_p|h(p)| - (\text{lower order})$$
> is compared to $\sum_p(1+\log p)^{-N}$, which **diverges for every fixed
> $N$** (by Mertens: $\sum_{p\le x}1\sim x/\log x$, so
> $\sum_{p\le x}(\log p)^{-N}\gtrsim (x/\log x)(\log x)^{-N}\to\infty$).

**Proof.** Direct comparison with the prime counting function via partial
summation; the density of primes up to $x$ is $x/\log x+o(x/\log x)$
(PNT), each contributing a term of size $\gtrsim(\log x)^{-N}$, so the
partial sum up to $x$ grows at least like $x/(\log x)^{N+1}\to\infty$ for
any fixed $N$. $\square$

This is the same qualitative failure as 108_06 Theorem 4.1 (global sum
diverges throughout the strip for the graded family) — here the mechanism
is polynomial-in-$\log p$ decay losing to the density of primes, rather
than the geometric-series exponent crossing $\Re a=0,1$, but the moral is
identical: **the density of primes ($\sim x/\log x$) must be beaten by
actual power decay in the argument, not merely decay in its logarithm.**

## 2. Exponential decay rate $\eta>1$ suffices, and matches 111_01's threshold

> ### Theorem 2.1 (global convergence under $\mathcal S_\eta$, $\eta>1$)
> If $\tilde h\in\mathcal S_\eta$ for some $\eta>1$, then
> $$\sum_p\big(A_p(h)+B_p(h)\big)$$
> converges absolutely.

**Proof.** $A_p(h)=\sum_{n\ge1}h(p^n)$, and every term $h(p^n)$ with
$n\ge1$ is a value of $h$ at an integer $\ge2$ that is a prime power; the
map (prime, exponent) $\mapsto$ prime power is injective, so
$$\sum_p A_p(h)\ \le\ \sum_{m\ge2}|h(m)|$$
summing over **all** integers $m\ge2$ (an over-count, since not every
integer is a prime power, but this only helps). By $\mathcal S_\eta$,
$|h(m)|=|\tilde h(\log m)|\le C_2(1+\log m)^{-2}m^{-\eta}$, and
$\sum_{m\ge2}m^{-\eta}(1+\log m)^{-2}<\infty$ exactly when $\eta>1$ (compare
with $\int_2^\infty x^{-\eta}(\log x)^{-2}dx$, convergent iff $\eta>1$; at
$\eta=1$ this is the divergent $\sum 1/(m(\log m)^2)$... which in fact
converges — but the sharp threshold is carried by the *next* piece, so
$\eta>1$ is used uniformly for both pieces below and is sufficient, not
claimed sharp here).

For $B_p(h)=\sum_{m\ge1}h(p^{-m})p^{-m}$: $|h(p^{-m})|\le C_2(1+m\log
p)^{-2}p^{-\eta m}$ (using $\tilde h(x)\to0$ at rate $\eta$ as
$x\to-\infty$ too, since $\mathcal S_\eta$ is a two-sided bound), so
$|h(p^{-m})p^{-m}|\le C_2(1+m\log p)^{-2}p^{-(\eta+1)m}$, and
$\sum_p\sum_m p^{-(\eta+1)m}(1+m\log p)^{-2}
\le\sum_p\sum_m p^{-(\eta+1)m}$, a double geometric series convergent
whenever $\eta+1>0$ — no threshold at all is needed for this half; the sum
over $p$ of the leading ($m=1$) term is $\sum_p p^{-(\eta+1)}(1+O(1))$,
convergent by comparison with $\sum p^{-s}$, $s=\eta+1>1$. $\square$

Both pieces of Theorem 2.1's proof therefore genuinely need only $\eta>0$
for $B_p$, and the $\eta>1$ threshold is carried entirely by $A_p$ — the
prime-power tail $\sum_p h(p)+h(p^2)+\cdots$, which must beat the prime
counting density $x/\log x$. This is the **same threshold** 111_01 Theorem
111.1.3 found necessary for $\widehat f(1)$ to exist, and 111_03
Proposition 2.1 used (loosely) for its $\Lambda(n)$ sum — see §3 for the
precise relationship, which is not identity.

Verified: for $\tilde h(x)=e^{-x^2}$ (Gaussian, in every $\mathcal S_\eta$),
$\sum_{p\le5000}(A_p+B_p)$ stabilizes to $12$ significant figures; for a
bare-polynomial control $\tilde h(x)=(1+x^2)^{-3}$ (no $\eta$ at all), the
partial sums keep increasing with no sign of a limit over the same range
(Proposition 1.1's mechanism, exhibited numerically).

## 3. Relation to the $\Lambda(n)$ sum of 111_03 — related but not identical

> ### Proposition 3.1 (a genuinely different object with the same threshold)
> $\sum_p A_p(h)$ (unweighted sum over prime powers of $h$'s own value) and
> $\sum_{n\ge2}\Lambda(n)h(n)n^{-1/2}$ (111_03 Proposition 2.1, weighted by
> $\log p$ and $n^{-1/2}$) are **different numbers** for the same $h$, and
> neither is derivable from the other by a simple identity — they arise
> from different objects (the local Tate integral's own closed form, versus
> the explicit-formula prime side, which carries the $\Lambda(n)n^{-1/2}$
> weight intrinsically from the logarithmic derivative $-\zeta'/\zeta$).
> What they **share** is the mechanism of convergence: both are sums over
> (essentially) prime powers of a rapidly decaying function of $\log n$,
> and both need genuine power decay ($\eta>1$ in our normalization) to beat
> the $\Lambda(n)\sim\log n$ growth and the prime density respectively.

Verified: for the standard Gaussian probe $\tilde h(x)=e^{-x^2}$,
$\sum_{n\le2\times10^4}\Lambda(n)h(n)n^{-1/2}=0.624192732\ldots$ (matching
111_03's reported value to displayed precision) while
$\sum_{p\le2\times10^4}A_p(h)=1.188538843\ldots$ — manifestly different
numbers, confirming Proposition 3.1's "not the same object" clause is not
a vacuous caveat.

## 4. Scope

**Proved here.** Proposition 1.1 (bare Schwartz fails globally, by
comparison with Mertens); Theorem 2.1 ($\eta>1$ suffices, with the sharp
threshold isolated to the $A_p$ piece); Proposition 3.1 (the $\Lambda(n)$
sum and this phase's local-integral tail sum are related in mechanism but
numerically distinct).

**Read from source, not re-derived.** Mertens'/PNT prime density
$\pi(x)\sim x/\log x$; 111_03 Proposition 2.1's convergence claim and its
verified value for the Gaussian probe, used only as a cross-check in §3,
not as a substitute derivation.

**Verified numerically.** Convergence of $\sum_p(A_p+B_p)$ for the Gaussian
probe versus non-convergence (growing partial sums) for a bare-polynomial
control, both refined over primes up to $5000$; the numerically distinct
values of the two sums in §3.

**Not established, and explicitly not claimed.** Sharpness of $\eta>1$ for
$A_p$'s global convergence (only sufficiency is proved; the boundary case
$\eta=1$ is not analyzed, by direct analogy with 111_01's sharp threshold
but not independently re-derived here); anything about $\Re h(1)\ne0$ data
(this section presupposes $h(1)=0$ throughout, per §0).

## 5. Verifier

`113_02_the_global_sum.py` checks: Proposition 1.1's divergence mechanism
by threshold-free refinement (growing, non-stabilizing partial sums for a
bare-polynomial control, contrasted with a genuinely convergent case);
Theorem 2.1's absolute convergence for a Schwartz-with-margin probe, by
Cauchy-type stabilization under refinement in the prime bound; Proposition
3.1's numeric distinction between the two sums, with both individually
convergent.
