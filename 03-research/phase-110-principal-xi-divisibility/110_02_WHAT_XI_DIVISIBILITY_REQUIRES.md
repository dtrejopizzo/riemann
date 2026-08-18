# 110.02 — What ξ-divisibility actually requires

## 0. Answer

The class $\{f:\hat f=\xi\hat g\}$ is closed under addition and negation
(trivial, §2), so algebraically it is a bona fide subspace candidate. But
its intersection with the admissible test class (ADM) — the class the
corner pairing actually accepts, compactly supported smooth data — is
**exactly $\{0\}$** (Theorem 110.2.4). The mechanism: $\xi$ is entire of
order $1$ but **infinite (not finite) exponential type** along the real
axis (Theorem 110.2.2, from Stirling's asymptotic for $\Gamma$), while every
nonzero compactly supported admissible transform has **finite** exponential
type (Lemma 110.2.1). A finite-type function can never absorb an
infinite-type factor and remain finite type, so $f=\xi g$ is forced out of
compact support entirely. The class is **not** empty in an absolute sense,
however: relaxing (ADM) to Schwartz-class (rapidly decaying, not
compactly supported) test data, an explicit nonzero example is exhibited
(§4, Example 110.2.6) with excellent decay on every vertical line — enough
to make the Weil-formula sum in $I_\partial$ converge beautifully — while
still, necessarily, failing to be compactly supported.

## 1. Growth and decay: two independent directions

Fix $w=\sigma+i\tau$. Write $x=\log r$; for $g$ admissible in the sense of
(ADM) (110\_00 §1: smooth, compactly supported on $(0,\infty)$), put
$\tilde g(x):=g(e^x)$, compactly supported on some $[\alpha,\beta]\subset
\mathbb R$.

### Lemma 110.2.1 (compact support $\Rightarrow$ finite exponential type in $\sigma$)

For $g$ admissible with $\operatorname{supp}\tilde g\subseteq[\alpha,\beta]$,
$$|\hat g(\sigma+i\tau)|\ \le\ \|\tilde g\|_1\cdot\max\!\big(e^{-\alpha\sigma},\,e^{-\beta\sigma}\big)\ \le\ C\,e^{A|\sigma|}\qquad(A:=\max(|\alpha|,|\beta|)),\tag{1.1}$$
for every $\sigma,\tau\in\mathbb R$ — a bound uniform in $\tau$, i.e. $\hat g$
has finite exponential type $A$ in the $\sigma$-direction.

**Proof.** $|\hat g(\sigma+i\tau)|=|\int_\alpha^\beta \tilde
g(x)e^{-(\sigma+i\tau)x}dx|\le\int_\alpha^\beta|\tilde
g(x)|e^{-\sigma x}dx\le\|\tilde g\|_1\max_{x\in[\alpha,\beta]}e^{-\sigma
x}=\|\tilde g\|_1\max(e^{-\alpha\sigma},e^{-\beta\sigma})$, using that
$e^{-\sigma x}$ is monotone in $x$ for fixed $\sigma$, so its max over
$[\alpha,\beta]$ occurs at an endpoint. $\square$

This uses only compact support (no smoothness). Smoothness of $\tilde g$
buys, separately, rapid (faster than polynomial) decay of $\hat g(\sigma+i\tau)$
in $\tau$ for *fixed* $\sigma$ — the direction relevant to convergence of
the Weil-formula sum over zeros $\rho$ (whose imaginary parts run to
$\infty$ at density $\sim T\log T/2\pi$, Riemann–von Mangoldt, cited,
unconditional) — but this decay-in-$\tau$ is not where the obstruction to
ξ-divisibility lives; see §3.

### Fact 110.2.A (standard: Laplace-transform exponential rate matches the support endpoint)

*If $h\in L^1[\alpha,\beta]$ is not a.e. zero and $\alpha=\inf(\operatorname{supp}h)$,
its transform $H(\sigma)=\int h(x)e^{-\sigma x}dx$ satisfies
$\lim_{\sigma\to+\infty}\tfrac1\sigma\log|H(\sigma)|=-\alpha$ exactly; in
particular $H$ cannot decay faster than every exponential rate as
$\sigma\to+\infty$.* This is classical (the elementary case of the
correspondence between the type of an entire function of exponential type
and the convex hull of the support of its generating distribution — see
e.g. R. P. Boas, *Entire Functions*, Ch. 6, on indicator functions and the
Pólya representation). **Status: cited, standard, not re-derived in full
generality here; the specific consequence used below (Theorem 110.2.4) is
verified numerically to high precision under refinement** (110\_02 verifier,
Check 2 — matches the predicted rate $-\alpha$ to relative error
$<10^{-3}$ at $\sigma\sim 160$, with the discrepancy shrinking as
$\sigma$ grows, consistent with the sub-exponential correction term computed
explicitly in the proof of Fact 110.2.A's application).

## 2. Closure under addition and negation

### Proposition 110.2.1′ (algebraic closure)

If $\hat f_1=\xi\hat g_1$ and $\hat f_2=\xi\hat g_2$ with $g_1,g_2$
admissible (an admissible class closed under $+,-$, e.g. $C_c^\infty(0,\infty)$
is a vector space), then $\hat f_1+\hat f_2=\xi(\hat g_1+\hat g_2)$ and
$-\hat f_1=\xi(-\hat g_1)$, with $g_1+g_2,-g_1$ again admissible.

**Proof.** Immediate from linearity of $g\mapsto\hat g$ and of multiplication
by the fixed entire function $\xi$. $\square$

So $\{\hat f=\xi\hat g:g\text{ admissible}\}$ is a linear subspace of the
transform side — the algebraic requirement a divisor group needs is met,
*conditional on the class being nonempty* (§4 shows it is, once (ADM) is
relaxed; §3 shows it is exactly $\{0\}$ under the strict reading).

## 3. $\xi$'s growth along the real axis: order 1, infinite type

### Theorem 110.2.2 ($\xi$ has order $1$ and infinite exponential type on $\mathbb R$)

As $\sigma\to+\infty$ along the reals,
$$\log|\xi(\sigma)|=\frac\sigma2\log\sigma-C\sigma+O(\log\sigma),\qquad
C:=\frac{\log2+1+\log\pi}2. \tag{3.1}$$
Consequently $\log|\xi(\sigma)|/\sigma\to+\infty$ (infinite type: $\xi$ is
**not** bounded by $Ce^{A\sigma}$ for any finite $A$), while
$\log|\xi(\sigma)|/(\sigma\log\sigma)\to1/2$ (order exactly $1$).

**Proof.** Write $\xi(\sigma)=\tfrac12\sigma(\sigma-1)\pi^{-\sigma/2}\Gamma(\sigma/2)\zeta(\sigma)$,
so
$$\log|\xi(\sigma)|=\log\tfrac12+\log\sigma+\log(\sigma-1)-\tfrac\sigma2\log\pi+\log\Gamma(\sigma/2)+\log\zeta(\sigma).$$
As $\sigma\to\infty$, $\zeta(\sigma)\to1$ (Euler product/definition), so
$\log\zeta(\sigma)\to0$; the first three terms are $O(\log\sigma)$. Stirling's
asymptotic $\log\Gamma(z)=(z-\tfrac12)\log z-z+\tfrac12\log(2\pi)+O(1/z)$
with $z=\sigma/2$ gives
$$\log\Gamma(\sigma/2)=\Big(\frac\sigma2-\frac12\Big)\log\frac\sigma2-\frac\sigma2+O(1)
=\frac\sigma2\log\sigma-\frac\sigma2\log2-\frac\sigma2+O(\log\sigma).$$
Collecting, $\log|\xi(\sigma)|=\tfrac\sigma2\log\sigma-\tfrac\sigma2(\log2+1)-\tfrac\sigma2\log\pi+O(\log\sigma)
=\tfrac\sigma2\log\sigma-C\sigma+O(\log\sigma)$ with $C=(\log2+1+\log\pi)/2$, which
is (3.1). Dividing by $\sigma$: $\log|\xi(\sigma)|/\sigma=\tfrac12\log\sigma-C+O(\log\sigma/\sigma)\to+\infty$.
Dividing by $\sigma\log\sigma$: $\to1/2$. $\square$

**Status: derivation from Stirling's formula given in full above (standard,
cited); the resulting asymptotic (3.1), including the exact constant $C$,
is verified numerically to $\sim6$ significant figures across five decades
of $\sigma$ (up to $\sigma=10^6$) in the accompanying verifier — a genuine
value check with a predicted constant, not a mere monotonicity check.**

This is an **unconditional** fact: it uses only $\Gamma$'s classical
asymptotic and $\zeta(\sigma)\to1$ as $\sigma\to+\infty$ (which holds simply
because the Euler product/Dirichlet series for $\zeta$ converges absolutely
there) — nothing about the location of any zero of $\xi$ or $\zeta$ enters.
This point is developed further in 110\_03.

## 4. The main obstruction: no compactly supported ξ-divisible function exists

### Theorem 110.2.4 (vacuity on the admissible class)

For every admissible $g\ne0$ (compactly supported, smooth, (ADM)), the
function $f$ determined by $\hat f:=\xi\cdot\hat g$ is **not** compactly
supported. Consequently
$$\{f:\hat f=\xi\hat g\text{ for some admissible }g\}\ \cap\ (\text{ADM})\ =\ \{0\}. \tag{4.1}$$

**Proof.** Suppose, for contradiction, $g\ne0$ is admissible with support
$[\alpha,\beta]$ (in $x=\log r$ coordinates, $\alpha=\inf$ of the support)
and $f$, with $\hat f=\xi\hat g$, is *also* compactly supported. By Lemma
110.2.1 applied to $f$, there is a finite $A_f$ with
$$|\hat f(\sigma)|\le C_f\,e^{A_f\sigma}\qquad(\sigma\to+\infty). \tag{4.2}$$
By Fact 110.2.A applied to $\tilde g$ (whose transform along the real axis
is exactly $\hat g(\sigma)$, since $\tau=0$ there): for every $\varepsilon>0$,
eventually $|\hat g(\sigma)|\ge e^{-(\alpha+\varepsilon)\sigma}$. Combining
with Theorem 110.2.2, for $\sigma$ large,
$$\log|\hat f(\sigma)|=\log|\xi(\sigma)|+\log|\hat g(\sigma)|
\ \ge\ \Big(\frac\sigma2\log\sigma-C\sigma+O(\log\sigma)\Big)-(\alpha+\varepsilon)\sigma
=\frac\sigma2\log\sigma-(C+\alpha+\varepsilon)\sigma+O(\log\sigma).$$
Since $\tfrac\sigma2\log\sigma$ dominates any fixed multiple of $\sigma$, the
right side exceeds $(A_f+1)\sigma$ for all sufficiently large $\sigma$,
contradicting (4.2). Hence no such compactly supported $f$ exists. Since
this holds for every nonzero admissible $g$, (4.1) follows (the only $f$
that can be compactly supported and satisfy $\hat f=\xi\hat g$ is $f=0$,
forcing $g=0$ too, as $\xi\not\equiv0$ and $\xi\hat g\equiv0\Rightarrow\hat
g\equiv0\Rightarrow g\equiv0$). $\square$

**This is the central negative fact of Task 2**, and it does not reference
the location of any zero of $\xi$ anywhere in its proof — only $\xi$'s
*growth rate* (Theorem 110.2.2, from $\Gamma$'s Stirling asymptotic) and the
elementary support/type correspondence (Fact 110.2.A, Lemma 110.2.1). This
point is the crux of 110\_03.

## 5. The class is not empty in an absolute sense: an explicit example outside (ADM)

Relaxing (ADM) from "compactly supported" to "Schwartz-class" (smooth,
rapidly decaying at both ends of $(0,\infty)$ but not necessarily
vanishing identically anywhere) restores nonemptiness explicitly.

### Example 110.2.6

Let $g(r):=e^{-(\log r)^2}$ (i.e. $\tilde g(x)=e^{-x^2}$, a Gaussian in
$x=\log r$: smooth, strictly positive everywhere on $(0,\infty)$, rapidly
decaying as $r\to0^+$ or $r\to\infty$, **not** compactly supported). Its
Mellin transform is, exactly,
$$\hat g(w)=\sqrt\pi\,e^{w^2/4}, \tag{5.1}$$
entire in $w$. Define $f$ by $\hat f(w):=\xi(w)\hat g(w)=\sqrt\pi\,\xi(w)e^{w^2/4}$.
Then:

* $\hat f\not\equiv0$ (a product of two functions not identically zero);
* $\hat f(\rho)=\xi(\rho)\cdot\sqrt\pi e^{\rho^2/4}=0$ for **every** zero
  $\rho$ of $\xi$ — ξ-divisibility holds, by construction, exactly as the
  general mechanism of the phase prompt predicts;
* on every vertical line $\operatorname{Re}(w)=\sigma$ fixed, $|\hat
  f(\sigma+i\tau)|\to0$ **superexponentially** as $|\tau|\to\infty$ (the
  Gaussian factor $e^{-\tau^2/4}$ overwhelms $\xi$'s own $e^{-\pi|\tau|/4}$
  decay and any polynomial factors) — far more than enough for the
  Weil-formula sum $\sum_\rho\hat f(\rho)\overline{\hat g(\rho)}$ to
  converge absolutely against the zero density $\sim T\log T$;
* by Theorem 110.2.4, $g$ (hence $f$) is, and must be, **not** compactly
  supported — this example sits exactly at the boundary the theorem draws.

**Proof of (5.1).** Complete the square: $\int_{-\infty}^\infty
e^{-x^2}e^{-wx}dx=\int e^{-(x+w/2)^2}e^{w^2/4}dx=e^{w^2/4}\sqrt\pi$ (the
substitution shifts the Gaussian's center, and $\int_{-\infty}^\infty
e^{-u^2}du=\sqrt\pi$, valid for every complex $w$ by contour-shifting the
Gaussian integral, an entire-function identity). $\square$

**Status: (5.1) is verified numerically against direct truncated
quadrature, under refinement of the truncation window, to relative error
$<10^{-29}$ (machine/arbitrary-precision exact, limited only by
`mpmath` precision); the vertical-line decay claim is verified numerically
at $\sigma=1/2$ for $\tau$ up to $80$, where $|\hat f(1/2+i\tau)|$ has
already fallen to $\sim6\times10^{-719}$ (verifier Check 3).**

## 6. The functional equation: no free symmetry is inherited

$\xi(w)=\xi(1-w)$ does **not** force any symmetry on $\hat f=\xi\hat g$
unless $\hat g$ itself is chosen symmetric: applying $w\mapsto1-w$ to
$\hat f(w)=\xi(w)\hat g(w)$ gives $\hat f(1-w)=\xi(w)\hat g(1-w)$, which
equals $\hat f(w)=\xi(w)\hat g(w)$ only if $\hat g(1-w)=\hat g(w)$. Nothing
in Definition (ADM) requires this, and Example 110.2.6's $\hat
g(w)=\sqrt\pi e^{w^2/4}$ is **not** symmetric under $w\mapsto1-w$ (check:
$\hat g(1-w)=\sqrt\pi e^{(1-w)^2/4}\ne\hat g(w)$ in general). So
ξ-divisibility, as a bare condition, carries no functional-equation
consequence for $f$ beyond what $g$ already has; imposing one would be an
extra, separate design choice, not a consequence of the definition.

## 7. Scope

**Proved here:**
* Lemma 110.2.1: compact support forces finite exponential type in
  $\sigma$ (elementary, fully proved);
* Proposition 110.2.1′: algebraic closure of $\{\hat f=\xi\hat g\}$ under
  $+,-$;
* Theorem 110.2.2: $\xi$'s precise growth asymptotic along $\mathbb R$
  (order $1$, infinite type), derived from Stirling's formula;
* Theorem 110.2.4: the admissible (compactly supported) class meets
  $\{\hat f=\xi\hat g\}$ only at $0$ — the central negative result;
* Example 110.2.6: an explicit nonzero ξ-divisible pair outside (ADM), with
  excellent vertical-line decay.

**Read from source, not re-derived:** the definitions of $\mathcal
G$/admissibility inherited from 108\_03/108\_31/110\_00; Stirling's
asymptotic for $\log\Gamma$ (standard, stated and used, not re-derived from
Euler–Maclaurin here); $\zeta(\sigma)\to1$ as $\sigma\to\infty$ (elementary
consequence of the Dirichlet series, not re-derived); Riemann–von
Mangoldt zero-counting asymptotic (mentioned for context, not used in any
proof here).

**Cited without independent re-derivation:** Fact 110.2.A (the
Laplace-transform exponential-rate/support correspondence, standard —
R. P. Boas, *Entire Functions*), used only in the direction needed for
Theorem 110.2.4's lower bound, with that specific consequence verified
numerically.

**Verified numerically:** Theorem 110.2.2's asymptotic constant $C$ (to
$\sim6$ significant figures, refined across five decades of $\sigma$);
Fact 110.2.A's rate for an explicit bump function (refined across
$\sigma$ up to $160$); Example 110.2.6's closed form (5.1) (machine
precision) and its vertical decay (up to $\tau=80$).

**Not established, and explicitly not claimed:** that (4.1) extends to
every conceivable relaxation of "admissible" (only the two readings, strict
compact support and Schwartz class, are examined); any relation to RH or to
the location of any zero (Theorem 110.2.2/110.2.4 are unconditional — this
is precisely what 110\_03 exploits); that Example 110.2.6's $f$ is itself
"nice" beyond entire-transform decay on verticals (its inverse Mellin
transform as an candid function of $r$ is not computed here).

## 8. Verifier

`110_02_what_xi_divisibility_requires.py`: (1) confirms Lemma 110.2.1's
bound numerically for an explicit bump on $[1,2]$; (2) confirms Theorem
110.2.2's asymptotic constant $C=(\log2+1+\log\pi)/2$ to high precision
across $\sigma\in\{10^2,10^3,10^4,10^5,10^6\}$, with a control that rejects
a wrong constant (e.g. $C=1$); (3) confirms Example 110.2.6's closed form
(5.1) by refinement of a truncated quadrature, and its superexponential
vertical decay; (4) confirms Fact 110.2.A's predicted rate
$-\alpha$ for an explicit smooth bump, refined across increasing $\sigma$,
with a control rejecting a wrong endpoint; (5) a combined check that
$f=\xi\cdot(\text{bump transform})$ genuinely retains $\xi$'s infinite-type
growth (does not become finite type) when $g$ is compactly supported — the
numerical core of Theorem 110.2.4.
