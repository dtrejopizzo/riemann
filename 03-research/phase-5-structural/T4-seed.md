# T4-seed — Does positivity become *structural* in the anatomy coordinates? Two genuine inequalities natural in $\{R_p\}$, opaque in $\{a_p\}$

**Route B / M5, the T4 seed (analytic, no engine).** Author: David Alejandro Trejo Pizzo · 2026-06-03.
Follows Phase 2 (`Phase2-Rp-Euler.md`). The advisor's survival test, taken literally.

> **The test (advisor's precise reformulation).** It is not enough that $\lambda_{\min}=F(\{R_p\})$; if also
> $\lambda_{\min}=G(\{a_p\})$ and $R_p=\mathcal T(a_p)$, the coordinate change gained nothing. **The anatomy
> earns its keep iff some inequality or monotonicity is *natural* in $\{R_p\}$ and *opaque* in $\{a_p\}$.**
>
> **Result.** Two such structures exist and are proved below: **(I)** positivity is a **Bessel/Carleson bound**
> on a weighted prime-frequency measure in the archimedean metric (a frame-theoretic condition, manifestly
> structural, opaque in $a_p$) — with the *finite* bound (B-2) unconditional and the bound $\le1$ being RH;
> **(II)** $\lambda_{\min}$ is **concave and coordinate-wise monotone** in the prime masses, giving an
> **extremal reduction** (positivity of a whole box-class $\Leftrightarrow$ positivity at a single extremal
> object) — a structural inequality with no natural counterpart in $a_p$-coordinates. **Neither breaks the
> sign wall** (the Bessel-$\le1$ / the extremal check remain local-RH); both make positivity *structural*,
> which is exactly "the anatomy earns its keep."

---

## 0. Recall

$Q(L)=A_\infty-\sum_n\frac{\Lambda_L(n)}{\sqrt n}w_nw_n^*$, $A_\infty\succeq0$ (the CC manifest square),
$(w_n)_i=\widehat\phi_i(\log n)$, $\lambda_{\min}=\lambda_{\min}(Q)$; positivity (local Weil) $\iff\lambda_{\min}\ge0\iff Q\succeq0$.

---

## I. Positivity $=$ a Bessel / Carleson bound (the structural reformulation)

$Q\succeq0\iff \sum_n\frac{\Lambda_L(n)}{\sqrt n}w_nw_n^*\ \preceq\ A_\infty$. Factor the archimedean square
$A_\infty=B^*B$ ($B$ explicit, $B\succ0$ on its range; the Sonin/de Branges metric). Then:

> **Theorem T4-I (Bessel form).** With normalized prime-frequency vectors $\widetilde w_n:=B^{-*}w_n$,
> $$
> \lambda_{\min}(Q)\ge0\ \iff\ \sum_n\frac{\Lambda_L(n)}{\sqrt n}\,\big|\langle\widetilde w_n,\,\xi\rangle\big|^2\ \le\ \|\xi\|^2\quad\forall\xi,
> $$
> i.e. **the weighted system $\big\{(\Lambda_L(n)/\sqrt n)^{1/2}\,\widetilde w_n\big\}_n$ is a Bessel system with
> bound $\le1$** in the archimedean metric. Equivalently, the **prime measure**
> $\nu_L:=\sum_n\frac{\Lambda_L(n)}{\sqrt n}\delta_{\log n}$ is a **Carleson measure** (bound $\le1$) for the
> band-limited window space in the $B$-metric.

> **Proposition T4-I' (the finite bound is unconditional — B-2 reappears).** For an L-function with the
> Ramanujan bound $|a_{p^k}|\le(k+1)$ (Deligne for $\mathrm{GL}(2)$; trivially for $\zeta$, Dirichlet),
> $$
> \sum_n\frac{|\Lambda_L(n)|}{\sqrt n}\,\|\widetilde w_n\|^2\ \le\ C_{B,\,\mathrm{window}}\ <\ \infty,
> $$
> so the Bessel bound is **finite**: the prime measure is *always* Carleson with **some** finite constant.

**Proof of T4-I'.** $|\Lambda_L(p^k)|\le(k+1)\log p$; $\|\widetilde w_{p^k}\|^2=O(|\widehat{\,\cdot\,}|^2$ at
$k\log p)$ is window-localized (rapid decay in $k\log p$ off the window), and $\sum_{p,k}\frac{(k+1)\log p}{p^{k/2}}\cdot(\text{window})<\infty$
by the $p^{-k/2}$ decay. $\square$

**Reading (this is the program's wall, re-expressed and *localized to the anatomy*).** Positivity is a
**Carleson/Bessel** condition on the prime measure $\nu_L$ in the archimedean Sonin metric — *the exact
structure of the original B-2 / Days-14–22 analysis*, now per-L and local. The **finite** Carleson bound is
unconditional (Ramanujan $\Rightarrow$ B-2); the bound being **$\le1$** is local Weil positivity (local RH).
This is a genuine answer to the survival test: positivity is a **frame-theoretic inequality** on the prime
frequencies — manifestly structural, and **opaque** in the raw coefficients $\{a_p\}$ (which carry no
metric/Bessel structure on their own).

---

## II. Concavity + monotonicity $\Rightarrow$ an extremal reduction (a structural inequality)

> **Theorem T4-II (concavity, monotonicity, extremal reduction).** View $\lambda_{\min}$ as a function of the
> coefficient vector $\Lambda=\{\Lambda_L(n)\}_{n\le X}$.
> 1. **Concave:** $\Lambda\mapsto\lambda_{\min}(Q(\Lambda))$ is **concave** (a min of linear functionals of an
>    affine matrix family).
> 2. **Monotone:** on the non-negative orthant $\Lambda_n\ge0$, $\lambda_{\min}$ is **coordinate-wise
>    non-increasing** (increasing $\Lambda_n$ subtracts a PSD rank-one; Weyl).
> 3. **Extremal reduction:** on a box $\mathcal B=\{0\le\Lambda_n\le c_n\}$, the minimum is attained at the
>    **all-upper corner** $\Lambda_n\equiv c_n$:
>    $$
>    \min_{L\in\mathcal B}\lambda_{\min}(Q(L))\ =\ \lambda_{\min}\big(Q(\text{corner})\big).
>    $$
>    Hence **local Weil positivity holds throughout $\mathcal B$ iff it holds at the single extremal object.**

**Proof.** (1) $\lambda_{\min}(M)=\min_{\|u\|=1}\langle u,Mu\rangle$ is concave in $M$; $Q(\Lambda)$ is affine
in $\Lambda$; concave$\circ$affine is concave. (2) $\partial Q/\partial\Lambda_n=-\tfrac1{\sqrt n}w_nw_n^*\preceq0$,
and $\lambda_{\min}(M-\text{PSD})\le\lambda_{\min}(M)$ (Weyl). (3) A concave function on a compact convex set
attains its minimum at an extreme point (vertex of $\mathcal B$); coordinate-wise non-increasing singles out
the all-upper vertex. $\square$

**The extremal object (the reduction is the theorem; corner-positivity is a separate problem).** With the
$\mathrm{GL}(2)$-tempered box $c_{p^k}=2\log p$ (i.e. $a_{p^k}\in[0,2]$), the corner $a_{p^k}\equiv2$ is the
**Eisenstein/$\zeta^2$ point** ($\alpha_p=\beta_p=1$): indeed $-(\zeta^2)'/\zeta^2=2\sum_n\Lambda(n)n^{-s}$, so
$\Lambda_{\zeta^2}(p^k)=2\log p$. **What T4-II proves is the *reduction*: positivity on the box $\iff$
positivity of the corner object.** Whether the corner is itself positive is a *separate* statement we do
**not** prove here (it would, for $\zeta^2$, follow from RH for $\zeta$, but we do not invoke
RH$\Rightarrow Q\succeq0$ as established — that equivalence is exactly the program's open core). **Statement
for an external reader:** *the extremal reduction shows box-positivity reduces to corner-positivity; for the
tempered non-negative box the corner is $\zeta^2$.* The reduction is the result; the corner's positivity is
left open.

**Reading.** T4-II is a structural inequality (a **concavity + monotonicity**) that is *natural* in the mass
picture — $\lambda_{\min}$ is concave & monotone in the **prime masses** $\Lambda_n$ — and **opaque** in
$\{a_p\}$: in $a_p$-coordinates there is no reason to "check the extreme corner," because the sign-oscillation
of genuine $a_p$ hides the monotone structure. The anatomy/mass coordinates expose it.

**Honest scope.** The box class $a_{p^k}\in[0,2]$ is **artificial** (genuine primitive L-functions have
sign-oscillating $a_p$; this is precisely the advisor-sanctioned artificial class). The reduction is to **one
check** (it does not *prove* the extreme is positive beyond the $\zeta^2$ remark, which is itself local-RH for
$\zeta$). It is **local** (windowed), not global RH. But it is a *genuine non-trivial structural inequality*
appearing naturally in $\{R_p\}$ — the survival test, passed in the artificial class.

---

## III. The standalone candidate: Theorem C (stability), restated for the panel

Independently of RH, **Theorem C** (Phase 2) is the most likely durable result:
$$
\Lambda_L(n)=\Lambda_{L'}(n)\ (n\le P)\ \Longrightarrow\ \big\|\mathcal R(L)-\mathcal R(L')\big\|\le C\,e^{-\alpha(\log P)^2},\quad\alpha\approx\sigma^2/8 .
$$
It says the **localized anatomy is an exponentially-stable local-arithmetic fingerprint** of an L-function —
a clean statement that survives even if the RH classification fails. Flagged as the **autonomous theorem** to
foreground.

---

## IV. Verdict: does the program survive the T4 filter?

> **Yes — in the precise sense the advisor demanded, and no more.** Positivity *is* structural in the anatomy
> coordinates: **(I)** a Bessel/Carleson bound on the prime measure (frame-theoretic, opaque in $a_p$), and
> **(II)** a concavity/monotonicity extremal reduction (opaque in $a_p$). These are genuine inequalities
> natural in $\{R_p\}$. **But the sign wall is unmoved:** the Bessel bound $\le1$ (I) and the extremal
> positivity check (II) are each local Weil positivity = local RH. So the anatomy *reformulates* positivity
> as a frame/Carleson condition and *organizes* it (concavity, extremal reduction) — it **earns its keep as
> structure**, but does not, and by the program's repeated lesson cannot, supply the sign.

**This is consistent with everything since P8:** magnitude/structure is available unconditionally (the finite
Bessel bound = B-2); the sign ($\le1$) is RH. The anatomy coordinates make that dichotomy *crisper* (a
Carleson measure, a concave functional) but do not cross it.

**What this hands Phase 3.** A sharp, falsifiable target for the validated engine: **measure the Bessel/
Carleson constant of $\nu_\zeta$ vs $\nu_{L_{\mathrm{DH}}}$** in the archimedean metric (T4-I), and **test
Conjecture B2** (does a robustly factorizing/Carleson-$\le1$ profile track the Euler product?). The engine now
has a clean mathematical objective — not rescuing a scalar, but measuring a Carleson constant and a
factorization, the two structures T4 identified.

---

### Status
- T4-I (positivity $=$ Bessel/Carleson $\le1$; finite bound unconditional) — ✅ proved.
- T4-I' (finite Carleson bound from Ramanujan) — ✅ proved.
- T4-II (concavity + monotonicity + extremal reduction on the box) — ✅ proved; artificial class; local.
- Theorem C (stability) — ✅ (Phase 2); flagged as the autonomous candidate theorem.
- The sign ($\le1$ / extremal positivity) — ⬜ unmoved = local RH (as expected).
- Conjecture B2 (factorization $\Rightarrow$ Euler) — ⬜ open; a Phase-3 measurement target.
- **Phase 3** (validated engine: Carleson constant $\zeta$ vs $L_{\mathrm{DH}}$, band test, Conj. B2) — ⬜ next.
