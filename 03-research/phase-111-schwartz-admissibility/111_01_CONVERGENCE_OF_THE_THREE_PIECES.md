# 111.01 — Convergence of the three pieces on Schwartz data

Conventions and the classes $\mathcal S(\mathbb R)$, $\mathcal S_\eta$,
$\mathcal S_{>1}$ are as fixed in 111\_00 §1. Throughout, $f,g$ denote real,
non-negative-domain test functions with $\tilde f,\tilde g\in\mathcal
S(\mathbb R)$ (or a named subclass), and
$$I_\partial(D_f,D_g)=\widehat f(0)\overline{\widehat g(0)}
+\widehat f(1)\overline{\widehat g(1)}-\sum_\rho\widehat f(\rho)\overline{\widehat g(\rho)}$$
is the evaluated form quoted from 107\_240 Theorem D / the phase prompt. The
task is to determine, piece by piece, on what class of $f,g$ each of the
three groups of terms is even a finite number.

## 1. The polar terms $\widehat f(0)\overline{\widehat g(0)}+\widehat f(1)\overline{\widehat g(1)}$

### Lemma 111.1.1 ($w=0$ is free)

For every $\tilde f\in\mathcal S(\mathbb R)$, $\widehat f(0)=\int\tilde
f(x)\,dx$ converges absolutely.

**Proof.** $\mathcal S(\mathbb R)\subset L^1(\mathbb R)$: taking $N=2$ in the
Schwartz seminorms gives $|\tilde f(x)|\le C_2(1+x^2)^{-1}$, integrable.
$\square$

So the $w=0$ half of the polar terms needs nothing beyond bare Schwartz
class. $w=1$ is a different story.

### Lemma 111.1.2 ($w=1$ is *not* free on bare Schwartz class)

There exists $\tilde f\in\mathcal S(\mathbb R)$ with $\widehat f(1)=\int
\tilde f(x)e^{-x}dx$ divergent.

**Proof.** Take $\tilde f(x)=\operatorname{sech}(x)=2/(e^x+e^{-x})$: smooth,
and every derivative decays exponentially (hence faster than every
polynomial), so $\tilde f\in\mathcal S(\mathbb R)$. As $x\to-\infty$,
$\tilde f(x)=2/(e^x+e^{-x})\sim 2e^{x}$, so $\tilde f(x)e^{-x}\to2$: the
integrand does not tend to $0$ on the ray $x\to-\infty$, so
$\int_{-\infty}^0\tilde f(x)e^{-x}dx$ diverges (to $+\infty$). $\square$

This is not a pathology invented for the occasion: $\operatorname{sech}$ is
one of the best-behaved Schwartz functions there is (it is the density of
the logistic/hyperbolic-secant distribution, real-analytic, everywhere
positive). The mechanism is exactly the one flagged in Remark 111.0.1 —
Schwartz decay controls polynomial weight, not exponential weight, and
$e^{-wx}$ for $\operatorname{Re}(w)>0$ grows exponentially as $x\to-\infty$.

### Theorem 111.1.3 (the polar terms exist on $\mathcal S_{>1}$, and are sharp there)

If $\tilde f,\tilde g\in\mathcal S_\eta$ for some $\eta>1$, then
$\widehat f(w),\widehat g(w)$ extend to holomorphic functions on the strip
$|\operatorname{Re}w|<\eta\supset[0,1]$, and in particular $\widehat f(0),
\widehat f(1),\widehat g(0),\widehat g(1)$ are finite; the polar terms are a
well-defined complex number. The threshold $\eta=1$ is sharp: $\eta=1$
(not $>1$) already fails, by Lemma 111.1.2 applied with a function whose
decay rate is exactly $1$ (e.g. $\operatorname{sech}$, rate exactly $1$
since $\operatorname{sech}(x)\sim2e^{-|x|}$).

**Proof.** For $|\operatorname{Re}w|=\sigma_0<\eta$, pick $\eta'$ with
$\sigma_0<\eta'<\eta$; membership in $\mathcal S_\eta$ gives $|\tilde
f(x)|\le C_0 e^{-\eta|x|}\le C_0e^{-\eta'|x|}$, so
$|\tilde f(x)e^{-wx}|\le C_0e^{-\eta'|x|+\sigma_0|x|}=C_0e^{-(\eta'-\sigma_0)|x|}$,
integrable; dominated convergence and Morera's theorem give holomorphy on
$|\operatorname{Re}w|<\eta$. Since $\eta>1\Rightarrow[0,1]\subset(-\eta,\eta)$,
evaluation at $w=0,1$ is legitimate. Sharpness is Lemma 111.1.2 (rate exactly
$1$, the boundary case, already fails at $w=1$). $\square$

## 2. The zero sum $\sum_\rho\widehat f(\rho)\overline{\widehat g(\rho)}$

### Lemma 111.1.4 (rapid decay on vertical lines in the strip)

If $\tilde f\in\mathcal S_\eta$, $\eta>1$, then for every integer $N\ge0$
there is $C_N$ with
$$|\widehat f(\sigma+i\tau)|\le C_N(1+|\tau|)^{-N}\qquad\text{uniformly for }0\le\sigma\le1,\ \tau\in\mathbb R.$$

**Proof.** Integration by parts $N$ times (legitimate: $\tilde f\in
\mathcal S_\eta\subset\mathcal S(\mathbb R)$ is smooth with all derivatives
again in $\mathcal S_\eta$, since differentiating does not affect the
exponential-weight bound, only possibly the polynomial one, which is
absorbed by redefining $C_N$) gives
$$w^N\widehat f(w)=\int(-1)^N\tilde f^{(N)}(x)e^{-wx}dx,$$
using that boundary terms vanish (exponential decay kills every polynomial
growth of $e^{-wx}$ at $x\to\pm\infty$ for $|\operatorname{Re}w|<\eta$). The
right side is bounded, by Theorem 111.1.3's argument applied to $\tilde
f^{(N)}$, uniformly for $\sigma\in[0,1]\subset(-\eta,\eta)$: call the bound
$M_N$. So $|w|^N|\widehat f(w)|\le M_N$, and for $|\tau|\ge1$, $|w|\ge|\tau|$,
giving $|\widehat f(\sigma+i\tau)|\le M_N|\tau|^{-N}$; combined with the
uniform bound $M_0$ on the whole strip (Theorem 111.1.3) this gives the
stated bound (adjusting constants for $|\tau|<1$). $\square$

### Theorem 111.1.5 (the zero sum converges absolutely on $\mathcal S_{>1}$)

If $\tilde f,\tilde g\in\mathcal S_\eta$, $\eta>1$, then
$\sum_\rho|\widehat f(\rho)\overline{\widehat g(\rho)}|<\infty$, the sum
being over zeros $\rho=\beta+i\gamma$ of $\xi$ with multiplicity.

**Proof.** By Lemma 111.1.4 with $N=2$ applied to both $f,g$:
$|\widehat f(\rho)\overline{\widehat g(\rho)}|\le C_2^{(f)}C_2^{(g)}(1+|\gamma|)^{-4}$,
using $0\le\beta\le1$. Group zeros by $|\gamma|\in[T,T+1)$: by the
Riemann–von Mangoldt formula (quoted, unconditional: $N(T)\sim(T/2\pi)\log T$
counts zeros with $0<\gamma\le T$), the count in each unit interval is
$O(\log T)$, so
$$\sum_\rho|\widehat f(\rho)\overline{\widehat g(\rho)}|
\ \le\ C\sum_{T=1}^\infty O(\log T)\cdot(1+T)^{-4}\ <\ \infty,$$
the series converging since $\log T/T^4\to0$ fast enough
($\sum T^{-2}\log T$ already converges; $N=2$ was overkill by a wide margin
— Schwartz decay gives every $N$, so in fact the sum converges "faster than
any inverse power of the truncation", not merely absolutely). $\square$

**This margin is exactly why the zero sum was never the delicate piece.**
Every genuine Schwartz function (with the mild exponential-decay addendum
needed just to *exist* at the strip endpoints, Theorem 111.1.3) beats the
zero density by an enormous margin ($N$ arbitrary vs. $N=2$ needed). The
delicate piece is entirely the polar terms (§1) and the trace (§3).

## 3. The defining trace $\mathfrak T(h)=\lim_\Lambda(\mathrm{Tr}(\theta(h)R_\Lambda)-2h(1)\log\Lambda)$

This piece cannot be analyzed from first principles here: the operator
definitions of $\theta$, $R_\Lambda$, and the trace are not contained in
either of the two files this phase is permitted to read (107\_240,
110\_02), and the phase's rules forbid opening further files. What *is*
available is the counterterm's shape, quoted in the prompt: it is
$2h(1)\log\Lambda$ — proportional to $h$'s value at the group identity, with
no dependence on any other feature of $h$.

### A notational ambiguity, flagged before use

"$h(1)$" in $2h(1)\log\Lambda$ could a priori mean either (a) $\tilde h(0)$,
the literal value of $h$ at the group identity $r=1$ (the reading that
matches phase 108's $\varphi_0$ language directly, pursued as the primary
reading in 111\_02), or (b) $\widehat h(1)$, the Mellin transform evaluated
at the pole of $\zeta$ (the reading matched by Zagier-type
renormalized-inner-product constructions, where a truncated Eisenstein/
continuous-spectrum contribution produces a $\log\Lambda$ divergence whose
coefficient is a transform value at a fixed point, not a function value).
Neither of the two files this phase may read disambiguates this, and the
phase does not have license to guess at unread operator definitions to
settle it. 111\_02 §1 shows the two readings are **not** in tension: both
lead to the same conclusion (no forced vanishing), by different routes. The
remainder of this section proceeds under reading (b), since it is the one
that makes the counterterm's coefficient structurally match a term already
present in the evaluated formula:

* The counterterm's coefficient, under reading (b), is exactly $\widehat
  h(1)$'s companion in the evaluated formula: the "separate theorem" (quoted,
  not re-derived) states $\mathfrak T(h)=\widehat h(0)+\widehat h(1)
  -\sum_\rho\widehat h(\rho)$. A regularization whose counterterm is built
  expressly around $h(1)$ and whose closed form has $\widehat h(1)$ as one
  of exactly three terms is not a coincidence of notation: the counterterm
  is designed to cancel *precisely* the divergence that the identity-shell
  contributes, and nothing else. This is architecture, not proof — see
  Assumption T below. (Under reading (a), $\tilde h(0)$ is simply a finite
  number for every Schwartz $h$ — no convergence question arises for the
  counterterm's *definition* at all, and Assumption T reduces to the bare
  claim that the fixed counterterm, whatever its coefficient literally is,
  captures the *entire* divergence of the truncated trace. The argument
  below goes through verbatim with "$\widehat h(1)$" read as "the
  counterterm's coefficient, whatever it is" if reading (a) is intended.)
* Given that architecture, finiteness of $\mathfrak T(h)$ for a given $h$
  reduces to two independently-checkable conditions: (a) $\widehat h(1)$
  exists as a finite number (§1, needs $\eta>1$), and (b) whatever residual
  dependence of $\mathrm{Tr}(\theta(h)R_\Lambda)$ on $h$'s full profile (not
  just $h(1)$) remains after subtracting the counterterm itself converges as
  $\Lambda\to\infty$. Condition (a) is Theorem 111.1.3. Condition (b) is
  where the two-file restriction bites.

### Assumption T (named, flagged, not proved here)

> The identity $\mathfrak T(h)=\widehat h(0)+\widehat h(1)-\sum_\rho\widehat
> h(\rho)$, established (via Weil's explicit formula, per the quoted
> "separate theorem") presumably first for compactly-supported $h$, is
> proved by a mechanism (Mellin/contour manipulation matching a truncated
> spectral side against a truncated arithmetic side) that depends on $h$
> only through the existence and decay of $\widehat h$ on the strip
> $0\le\operatorname{Re}(w)\le1$ — not on $h$ having compact support *per
> se*. Under this assumption, the identity extends verbatim to every
> $h=\tilde f\star\widetilde{\tilde g}$ with $\tilde f,\tilde g\in
> \mathcal S_\eta$, $\eta>1$, and Theorems 111.1.3 and 111.1.5 (which show
> the right-hand side is a finite, absolutely convergent number for such
> $h$) transfer that finiteness to the left-hand side, i.e. the limit
> defining $\mathfrak T(h)$ exists.

This is stated as an assumption, not a theorem, because it is a claim about
the convergence rate of $\mathrm{Tr}(\theta(h)R_\Lambda)$ as an operator
trace, which is not visible from the two files this phase may read. It is
exactly Refutation R3 of 111\_00 §2: **if Assumption T is false** — if the
truncated trace has a divergence the fixed counterterm cannot see once $h$
stops being compactly supported — the trace-side limit can fail to exist
even though the Weil-formula right-hand side (§§1–2 above) is manifestly
finite, and d1 would be dead by that route regardless of what Tasks 2–3
show. This is registered candidly as the single largest residual risk of
the phase's conclusion, not smoothed over.

## 4. Scope

**Proved here:**
* Lemma 111.1.1: $\widehat f(0)$ exists for every Schwartz $f$.
* Lemma 111.1.2: $\widehat f(1)$ does **not** exist for every Schwartz $f$ —
  explicit counterexample ($\operatorname{sech}$).
* Theorem 111.1.3: both polar terms exist, and are holomorphic in a strip
  around $[0,1]$, once $\tilde f,\tilde g\in\mathcal S_\eta$ for some
  $\eta>1$; $\eta=1$ is sharp (fails).
* Lemma 111.1.4, Theorem 111.1.5: the zero sum converges absolutely on the
  same class $\mathcal S_{>1}$, with enormous margin over the
  Riemann–von Mangoldt density.

**Read from source, not re-derived:** the evaluated formula
$I_\partial=\widehat f(0)\overline{\widehat g(0)}+\widehat f(1)\overline{\widehat
g(1)}-\sum_\rho\widehat f(\rho)\overline{\widehat g(\rho)}$ (107\_240
Theorem D / phase prompt); the Riemann–von Mangoldt asymptotic
$N(T)\sim(T/2\pi)\log T$ (classical, unconditional, cited).

**Verified numerically:** Lemma 111.1.2's divergence and Theorem 111.1.3's
convergence, contrasted on a matched pair ($\operatorname{sech}$, rate
exactly $1$, diverges; $\operatorname{sech}^2$, rate $2$, converges), under
truncation refinement; Theorem 111.1.5's absolute convergence for actual
zeros (via `mp.zetazero`), contrasted against a synthetic harmonic-density
control that diverges, to show the check is not vacuous; the
Riemann–von Mangoldt density itself, checked against actual zero locations
with shrinking relative error.

**Not established, and explicitly not claimed:** Assumption T (§3) — the
transfer of the trace-side identity from compactly-supported to
$\mathcal S_{>1}$ test data. This is the one open piece of Task 1, isolated
rather than assumed away, and it is exactly Refutation R3.

## 5. Verifier

`111_01_convergence_of_the_three_pieces.py` checks: (1) $\widehat f(1)$
diverges under refinement for $\operatorname{sech}$ (rate $1$) and
converges (to a stable value, matching a closed form) for
$\operatorname{sech}^2$ (rate $2$), directly testing Lemma 111.1.2 /
Theorem 111.1.3's sharp threshold; (2) $\widehat f(0)$ converges for a
Schwartz function with *no* exponential decay at all
($e^{-\sqrt{|x|}}$-type), confirming Lemma 111.1.1 needs nothing beyond bare
Schwartz class while (1)'s $w=1$ case genuinely needs more; (3) the zero-sum
partial sums for the $\xi$-divisible Gaussian pair of 110\_02 Example 110.2.6
stabilize (Cauchy criterion) as more zeros (via `mp.zetazero`) are included,
against a synthetic control sequence with only harmonic decay that diverges;
(4) the Riemann–von Mangoldt count is checked against actual zero locations
with relative error shrinking as $T$ grows.
