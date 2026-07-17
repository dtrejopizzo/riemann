# Problem B-2 — Semiboundedness of the Weil form (the crux)

**Goal.** Decide whether $\mathcal T$ (Result A.0) admits a self-adjoint realization **bounded below
by a finite constant**, *without* assuming RH. Via Friedrichs this is:
$$
\boxed{\ \exists\,C>-\infty:\quad \mathfrak t(g,g)=\langle g,\mathcal T g\rangle\ \ge\ -C\,\|g\|^2\quad\forall\,g\in\mathcal D\ }\qquad(\mathrm{SB})
$$
on the admissible class $\mathcal D$ (Gaussian-localized, strip-analytic width $>\tfrac12$; see A1 §3.2).
RH is the special case $C=0$; (SB) only asks for $C$ finite. This file sets up the analysis, proves the
free part is bounded below, proves the prime form converges, and then **identifies precisely why soft
methods cannot close (SB)** — pinning the difficulty to one explicit arithmetic inequality.

Imports A.0 verbatim: $\mathcal T=\Omega(D)+\Pi-2\sum_{n}\frac{\Lambda(n)}{\sqrt n}\mathrm{Re}\,T_{\log n}$,
$\;\mathfrak t=\mathfrak a+\mathfrak q-\mathfrak p$.

---

## 1. Strategy: KLMN / relative form-boundedness
The textbook route to (SB) for "free $+$ perturbation" forms is the **KLMN theorem**: if the free form
$\mathfrak a$ is bounded below and closed, and the perturbation $\mathfrak p$ is **$\mathfrak a$-form-bounded**
with relative bound $b<1$,
$$
|\mathfrak p(g)|\ \le\ b\,\mathfrak a(g)\ +\ K\,\|g\|^2\qquad(b<1),\tag{KLMN}
$$
then $\mathfrak a-\mathfrak p$ is bounded below (by $-K/(1-b)$ roughly) and defines a self-adjoint
operator. So the program is: (i) $\mathfrak a$ bounded below ✅; (ii) try to prove (KLMN) for the prime
form $\mathfrak p$. We will find (ii) **provably fails** — and that failure *is* the main result of this
file, because it tells the team exactly what kind of input is required.

---

## 2. The free part is bounded below (Result B2.1)
$\mathfrak a(g)=\frac1{2\pi}\int|\widehat g(r)|^2\Omega(r)\,dr=\langle g,\Omega(D)g\rangle$ with
$\Omega(r)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}2)-\log\pi$. Since $\Omega(D)$ is a real Fourier
multiplier, it is self-adjoint with $\operatorname{spec}=\overline{\operatorname{ran}\Omega}$. From
digamma asymptotics $\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}2)=\log\tfrac{|r|}2+O(r^{-2})\to+\infty$, and
$\Omega$ attains its minimum near $r=0$:
$$
\Omega(0)=\psi(\tfrac14)-\log\pi=-\gamma_E-3\log2-\tfrac\pi2-\log\pi\approx-5.37 .
$$
Hence $\Omega(D)\ge\Omega_{\min}\approx-5.37>-\infty$ and $\mathfrak a(g)\ge\Omega_{\min}\|g\|^2$. ✅

**Crucial caveat for KLMN:** the free part grows only **logarithmically** ($\Omega(r)\sim\log|r|$). It
is bounded below but provides almost no "coercivity." Keep this in view — it is exactly why the
perturbation will overwhelm it.

---

## 3. The prime form converges on the admissible class (Result B2.2)
$\mathfrak p(g)=2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\mathrm{Re}\,(g\star\tilde g)(\log n)$. For
$g\in\mathcal S$, $\,w:=g\star\tilde g\in\mathcal S$, so $|w(\log n)|\le C_M(1+\log n)^{-M}$ for every $M$.
With $\Lambda(n)/\sqrt n\le (\log n)/\sqrt n$,
$$
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}|w(\log n)|\ \le\ C_M\sum_{n\ge2}\frac{\log n}{\sqrt n\,(1+\log n)^{M}}<\infty\quad(M\ge1).
$$
So $\mathfrak p(g)$ is absolutely convergent on $\mathcal S$ (a fortiori on $\mathcal D$). ✅ **The form
$\mathfrak t$ needs no cutoff to be defined** — confirming A1 §1.3.

---

## 4. Naive KLMN provably fails (Result B2.3 — the Day-0 obstruction)
We show $\mathfrak p$ is **not** $\mathfrak a$-form-bounded with any relative bound — indeed not
$\mathfrak a$-bounded at all in the sense (KLMN). Idea: exhibit a family $g_\lambda\in\mathcal D$,
$\|g_\lambda\|=1$, along which $\mathfrak p(g_\lambda)\to+\infty$ while $\mathfrak a(g_\lambda)$ stays
$O(\log\lambda)$ — so no inequality $\mathfrak p\le b\,\mathfrak a+K$ can hold.

**Construction.** Let $\widehat g_\lambda$ concentrate near $r=0$ at width $1/\lambda$ in frequency, i.e.
$g_\lambda(u)=\lambda^{-1/2}\phi(u/\lambda)$ **spreads** in $u$ over scale $\lambda$ (uncertainty). Then:
- *Archimedean:* $\widehat g_\lambda$ supported near $r=0$ where $\Omega\approx\Omega_{\min}$ plus the
  $\log$ tail; $\mathfrak a(g_\lambda)=O(\log\lambda)$ (slow, from the logarithmic growth of $\Omega$).
- *Prime:* $w_\lambda=g_\lambda\star\tilde g_\lambda$ is spread over $|u|\lesssim\lambda$ with height
  $O(1)$, so it overlaps **all** primes with $\log n\lesssim\lambda$, i.e. $n\lesssim e^{\lambda}$:
$$
\mathfrak p(g_\lambda)\ \approx\ 2\!\!\sum_{n\lesssim e^{\lambda}}\!\frac{\Lambda(n)}{\sqrt n}\,w_\lambda(\log n)
\ \sim\ 2\!\!\int_0^{\lambda}\!\! e^{t/2}w_\lambda(t)\,dt\ \times(\text{PNT density }1)\ \longrightarrow\ \infty
$$
growing like a positive power of $e^{\lambda/2}$ — **exponentially faster** than $\mathfrak a=O(\log\lambda)$.
(The Chebyshev/PNT sum $\sum_{n\le N}\Lambda(n)n^{-1/2}\sim 2\sqrt N$ is the engine: the prime form can be
made $\sim\sqrt{N}=e^{\lambda/2}$ while the free form barely moves.)

**Conclusion (B2.3).** No $b<1$, no $b<\infty$ works in (KLMN): $\mathfrak p/\mathfrak a$ is unbounded.
**Soft perturbation theory cannot deliver (SB).** $\square$

> **Interpretation — this is the whole point.** The negative (prime) part of the Weil form is, in the
> crude pointwise sense, *vastly larger* than the positive archimedean part. If the primes behaved
> "randomly" with this density, $\mathfrak t$ would be **unbounded below** and (SB) — hence B-2 and the
> whole faithful-ladder dream — would be **false**. That (SB) is nonetheless expected to hold can only
> be due to **cancellation**: the signed sum $\sum\Lambda(n)n^{-1/2}\mathrm{Re}\,T_{\log n}$ must enjoy
> massive oscillatory cancellation that the absolute-value bound above destroys. **That cancellation is
> precisely the distribution of the zeros.** This *derives* the §3.3 claim "B-2 lives at zero-density
> level" — it is now a mechanism, not a guess.

---

## 5. The residual frontier — corrected to form level (Result B2.4)

> **Day-1 correction (two referee alerts, both conceded).** The Day-0 draft of this section wrote
> $\mathfrak p(g)=\frac1{2\pi}\int|\widehat g|^2\Phi$ with $\Phi(r)=2\sum\Lambda(n)n^{-1/2}\cos(r\log n)$
> and then spoke of $\inf_r(\Omega-\Phi)$. **That is illegitimate** and is retracted. Two reasons, the
> second deeper than the first.

### 5.1 $\Phi$ is not a function — not even a tempered distribution (fixes Alert 1)
The prime measure $\nu=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(\delta_{\log n}+\delta_{-\log n})$ has, by
PNT, total mass $\asymp e^{t/2}$ on each unit interval $[t,t+1]$ (density $e^{t}/t$ times weight
$t\,e^{-t/2}$). Hence $\nu$ is **not a tempered measure** and $\Phi=\widehat\nu$ is **not a tempered
distribution**. The pairing $\langle|\widehat g|^2,\Phi\rangle$ exists **only** because, for $g\in\mathcal D$,
$|\widehat g|^2$ is the FT of $w=g\star\tilde g$ which decays like $e^{-(1+2\epsilon)\cdot\frac12|t|}$ —
fast enough to integrate against $\nu$'s $e^{t/2}$ growth. This is the **same strip-width-$>\tfrac12$
class** the pole forced in A1 §3.2: the two constraints are one and the same. Consequently:
$$
\boxed{\ \mathfrak t(g,g)=\frac1{2\pi}\,\big\langle\,|\widehat g|^2\,,\,\Omega-\Phi\,\big\rangle+\mathfrak q(g)\quad\text{is a \emph{distributional pairing} on }\mathcal D,\ \text{not a pointwise integral.}\ }
$$
There is **no** $\inf_r(\Omega-\Phi)$: the symbol is not a function. Any rigorous statement must stay at
the level of the form acting on the cone $\{|\widehat g|^2:g\in\mathcal D\}$ of nonnegative functions of
positive type (the Weil/Bombieri cone), never a pointwise symbol bound.

### 5.2 The clean form is the zero-counting pairing
By the explicit formula itself, $\Omega-\Phi$ (plus the pole) **is** $2\pi$ times the zero-counting
distribution: $\mathfrak t(g,g)=\sum_\rho|\widehat g(\gamma_\rho)|^2$ with analytic continuation of
$\widehat g$ to the strip. A real zero contributes a genuine $|\cdot|^2\ge0$; an off-line quartet
$\{\,a\pm ib,\,-a\pm ib\,\}$ ($b=\beta-\tfrac12\neq0$) contributes the **indefinite**
$$
2\,\mathrm{Re}\big[\widehat g(a-ib)\,\overline{\widehat g(a+ib)}\big]\qquad(\text{this is P7-A's rank-2 }A(\gamma)).
$$
So $(\mathrm{SB})\iff \sum_\rho|\widehat g(\gamma_\rho)|^2\ge -C\|g\|^2$ on $\mathcal D$ — a statement about
the **geometry of the zeros and the boundedness of strip point-evaluations**, not a multiplier estimate.

### 5.3 The real obstruction: off-axis point-evaluation is unbounded on $L^2$ (fixes Alert 2)
"Finitely many off-line zeros $\Rightarrow$ (SB)" is **not** a corollary, and here is the precise gap.
The quartet term's factors
$$
\widehat g(a\pm ib)=\int_{\mathbb R} g(u)\,e^{\mp bu}\,e^{-iau}\,du
$$
are point-evaluations of $\widehat g$ **off the real axis**. On $\mathcal H=L^2(\mathbb R,du)$ these are
**unbounded functionals** ($e^{\mp bu}\notin L^2(\mathbb R)$): there is no $C$ with $|\widehat g(a\pm ib)|\le C\|g\|_{L^2}$.
Hence even a **single** off-line quartet yields an *a-priori unbounded indefinite* quadratic form, and
finiteness of the off-line set gives **no** lower bound by itself. The Day-0 claim is downgraded to a
working conjecture; the actual content of (SB) is whether the chosen Hilbert-space **norm** controls
these strip evaluations.

### 5.4 The norm *is* the entanglement (refines A.0 and §3.3) — the Day-1 finding
The choice of $\|\cdot\|$ is **irrelevant** to the algebraic identity (Problem A, a Gram-matrix tautology)
but **decisive** for B-2:
- with the naive $L^2(\mathbb R,du)$ norm, strip point-evaluations are unbounded, so the off-line
  indefinite terms are unbounded and (SB) **plausibly collapses to RH** (the bad branch: $B\iff$ RH, no
  separation — exactly the "entanglement" feared in §3.3);
- (SB) **genuinely weaker than RH** *requires* a weighted norm in which $\mathrm{ev}_{a\pm ib}$,
  $|b|<\tfrac12$, is **bounded** — i.e. a **reproducing-kernel (de Branges) space** $H(E)$.

So Connes' $L^2_\delta$ weight is **not cosmetic for B**: the weight is precisely what tames the
$e^{t/2}$ / strip growth and makes point-evaluations bounded. **This is the exact meeting point of
Problem B and Problem D:** the de Branges structure function $E$ *supplies the norm* in which B-2 is even
well-posed. *Correction to the Day-0 "no free $\delta$":* there is no free parameter for identity A; for
B-2 the **norm/weight is a genuine, decisive choice**, and fixing it correctly is half of B-2.

### 5.5 Open problem B2.4 (restated correctly)
⬜ **(B2.4a) — the well-posedness half.** Identify the Hilbert-space norm (weight, or de Branges $E=E_{T_0,\sigma}$)
in which the off-line point-evaluations $\mathrm{ev}_{a\pm ib}$ ($|b|<\tfrac12$) are bounded and the form
$\mathfrak t$ is closable. *This is literally Problem D step (i).*

⬜ **(B2.4b) — the inequality half.** In that norm, prove
$\sum_\rho|\widehat g(\gamma_\rho)|^2\ge -C\|g\|_{H(E)}^2$ on $\mathcal D$ **under a concrete zero-density
hypothesis** $N(\sigma,T)\ll T^{1-\delta(\sigma)}$, and find the weakest density input that suffices.

---

## 6. Status and next actions on B-2

| Step | Statement | Status |
|---|---|---|
| B2.1 | $\Omega(D)\ge\Omega_{\min}\approx-5.37$ on $L^2$ | ✅ |
| B2.2 | prime form converges on $\mathcal D$ | ✅ |
| B2.3 | naive KLMN fails — soft methods cannot give (SB) | ✅ |
| B2.4a | (SB) is ill-posed in $L^2$: off-axis point-eval unbounded ⟹ need a weighted/de Branges norm | ✅ (obstruction proved); ⬜ (find the norm) |
| B2.4b | in that norm, $\sum_\rho|\widehat g(\gamma_\rho)|^2\ge -C\|g\|^2$ under a zero-density hypothesis | ⬜ open (the crux) |

**Net (Day 1).** Two corrections turned into the day's real result: (i) the prime functional is **not**
a pointwise symbol ($\nu$ non-tempered), so (SB) must be stated as a distributional pairing on the
positive-type cone; (ii) off-axis point-evaluations are **unbounded on $L^2$**, so even one off-line zero
makes the form a-priori unbounded — *finiteness alone proves nothing*. The consequence is the sharpest
statement so far of the entanglement:
> **The choice of Hilbert-space norm — invisible to Problem A — is what decides whether B-2 is strictly
> weaker than RH or collapses into it. The genuine-weakening branch lives in a de Branges space $H(E)$.
> B and D are therefore the same problem viewed twice.**

**Next actions on B-2.**
1. **Merge with D.** Work B2.4a *as* de Branges step (i): construct $E_{T_0,\sigma}$ whose reproducing
   kernel makes strip point-evaluations bounded; this is now on the critical path for B, not an
   alternative route.
2. **Bombieri**, *Remarks on Weil's quadratic functional* — he works the form on a space where these
   evaluations are bounded; extract his norm and compare to $H(E)$.
3. **v10 reframed (honest).** "Measure $\inf_r(\Omega-\Phi_X)$" is **only heuristic** (no such $\inf$).
   The rigorous computational probe is at the form level: estimate
   $\inf\{\mathfrak t(g,g)/\|g\|_{H(E)}^2\}$ over the finite localizer family in a *candidate* weighted
   norm, and test **sensitivity to the weight** — a direct experiment on the §5.4 dichotomy.
