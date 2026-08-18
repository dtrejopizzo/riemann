# 108.11 — The global assembly is locally integrable: Stage 1 closes distributionally

## 0. The point

108_08 proved that the two analytically continued halves $A(a)$ and $B(a)$
have logarithmic singularities that **reinforce** at $a=\tfrac12$, so the
*pointwise* value there does not exist.

108_05 Corollary 4.1 had already established that the *pointwise* value is
**not** what Stage 1 asks for:

> "any extension of $\mathfrak T_S$ to $\mathcal G$ cannot be number-valued.
> The correct target is **measure-valued on the abscissa**."

These two statements are compatible.  This note proves the second one is
achieved: $A+B$ is locally integrable on the open strip, hence defines a
distribution — a Radon measure of order $0$ — which is exactly the target.

No zero of $\xi$ enters any definition.

## 1. Setting

From 108_06 and 108_08, with $a$ real in $(0,1)$,

\[
 A(a)=\sum_p\frac{p^{-a}}{1-p^{-a}}
 =\sum_{N\ge1}\frac{\varphi(N)}{N}\log\zeta(Na),
 \qquad
 B(a)=A(1-a),
\]

the middle expression being the analytic continuation.  Its singularities
come from the pole of $\zeta$ at $1$: the term $N$ is singular exactly when
$Na=1$.  Hence

\[
 \mathcal S:=\Big\{\tfrac1N:N\ge2\Big\}\ \cup\ \Big\{1-\tfrac1M:M\ge2\Big\},
\]

with $\tfrac12$ the unique common point (108_08).

## 2. Three elementary facts

> ### Lemma 2.1 (the singular set is discrete in the open strip)
> For every $\delta\in(0,\tfrac12)$, $\mathcal S\cap[\delta,1-\delta]$ is
> finite, of cardinality $\le 2/\delta$.  $\mathcal S$ accumulates only at
> $0$ and $1$.

**Proof.** $\tfrac1N\ge\delta$ forces $N\le1/\delta$, and $1-\tfrac1M\le1-\delta$
forces $M\le1/\delta$. $\square$

Verified: counts $1,3,7,17,37,197,1997$ at $\delta=0.4,\dots,0.001$.

> ### Lemma 2.2 (logarithms are locally integrable)
> $\displaystyle\int_{-h}^{h}\big|\log|x|\big|\,dx=2h(1-\log h)<\infty$,
> and this tends to $0$ as $h\to0$.

**Proof.** Direct antiderivative. $\square$

Verified to $10^{-6}$ relative at four scales.

> ### Lemma 2.3 (the tail is regular and geometrically small)
> On $[\delta,1-\delta]$ only finitely many $N$ satisfy $Na\le1$.  For the
> rest, $\log\zeta(Na)\to0$ geometrically:
> $\log\zeta(s)\cdot2^{s}\to1$ as $s\to\infty$, with error decaying at rate
> $\log\tfrac32$.

**Proof.** $\log\zeta(s)=2^{-s}+3^{-s}+O(4^{-s})$, so
$\log\zeta(s)2^{s}=1+(3/2)^{-s}+O((2)^{-s})$. $\square$

Verified threshold-free: fitted decay rate $-0.4173$ against the theoretical
$-\log\tfrac32=-0.4055$.

## 3. The theorem

> ### Theorem 3.1
> $A+B\in L^1_{\rm loc}\big((0,1)\big)$.  Consequently $A+B$ defines a
> distribution of order $0$ — a Radon measure — on the open strip.

**Proof.**  Fix a compact $K=[\delta,1-\delta]\subset(0,1)$.

By Lemma 2.3 there is $N_0=\lceil1/\delta\rceil$ such that for $N>N_0$ the
term $\tfrac{\varphi(N)}N\log\zeta(Na)$ is continuous on $K$ and bounded by
$C\,2^{-N\delta}$; the tail therefore converges uniformly on $K$ to a
continuous function.

The finitely many terms $N\le N_0$ are continuous on $K$ except at the points
$a=1/N\in K$, where the simple pole of $\zeta$ gives
$\log\zeta(Na)=-\log\big(N(a-\tfrac1N)\big)+O(1)$, i.e. a logarithmic
singularity.  The same applies to $B$ at the points $1-\tfrac1M$.

By Lemma 2.1 there are finitely many such points in $K$.  Around each, the
singular part is a constant multiple of $\log|a-s_0|$, integrable by
Lemma 2.2; away from them the function is continuous, hence bounded on the
compact complement.

A finite sum of locally integrable functions is locally integrable, so
$A+B\in L^1(K)$.  As $K$ was arbitrary, $A+B\in L^1_{\rm loc}((0,1))$. $\square$

> ### Corollary 3.2 (Stage 1, distributional form)
> For $g$ a test function, the assignment
> \[
>  \varphi\;\longmapsto\;\int_0^1 \varphi(a)\,c_g(a)\,
>  \Big[W_\infty(f_a)+A(a)+B(a)+\textstyle\sum_p C_p\Big]\,da
> \]
> is well defined for every $\varphi\in C_c^\infty((0,1))$, **except** for the
> constant $\sum_p C_p$, which is not treated here (§4).

## 4. What is and is not closed

**Closed.** Pointwise divergence at $a=\tfrac12$ (108_08) and local
integrability (Theorem 3.1) are simultaneously true and not in conflict:
verified explicitly — the pointwise values $3.91,6.21,8.52,10.82$ grow
without bound as $h\to0$ while the integral over $[\tfrac12-h,\tfrac12+h]$
stays below $1$ and shrinks to $0$.

The $a$-dependent part of the global assembly therefore exists as a
distribution on $(0,1)$, which is the target named in 108_05 Cor 4.1.

**Not closed, and this is a genuine gap in Stage 1.**

1. **The constant $\sum_p C_p$.**  $C_p=\int'_{\mathbb Z_p^\times}
   d^\times u/|1-u|_p$ is $a$-independent (108_06 Thm 3.1), so it does not
   affect the singularity analysis — but its sum over all $p$ is neither
   computed nor shown to converge anywhere in this program.  Until it is,
   the global object is determined only up to an undetermined constant, and
   possibly a divergent one.
2. **Complex $a$.**  Everything above is for real $a\in(0,1)$.  For complex
   $a$ the singularity structure of the continuation involves the zeros of
   $\zeta$, which the source rule forbids using in a definition.
3. **The comparison with the zero side** remains untouched.
4. **Whether this distribution is the right one** for the program — i.e.
   whether it pairs correctly with the constructions of 107_239–107_241 — is
   not established.

## 5. Status of Stage 1

| component | status |
|---|---|
| finite local terms | closed (108_06) |
| archimedean local term | closed, $\pi\cot(\pi a/2)$ (108_07) |
| semilocal, $S$ finite | closed |
| global, pointwise | **impossible** at $a=\tfrac12$ (108_08) |
| global, distributional, $a$-dependent part | **closed here** (Thm 3.1) |
| global, the constant $\sum_p C_p$ | **open** |

Stage 1 is therefore **substantially but not fully closed**: the
$a$-dependent part of the measure-valued extension exists and is proved; the
additive constant is not controlled.

`ROW_A_STATUS` remains `partial`.  Nothing here bears on RH.

## 6. Verifier

`108_11_global_assembly_locally_integrable.py` checks: finiteness of
$\mathcal S$ on seven compacts with counts $\sim2/\delta$ and accumulation
only at the endpoints; the exact primitive $2h(1-\log h)$ at four scales;
the geometric tail via a threshold-free fit of the decay rate against
$\log\tfrac32$; finiteness of the number of $N$ with $Na\le1$; finiteness and
shrinkage of the integral across $a=\tfrac12$; and the explicit coexistence
of pointwise divergence with integral finiteness.
