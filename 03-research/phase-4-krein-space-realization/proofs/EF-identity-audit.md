# Audit of EF-id — the explicit-formula identity that the Day-5 retraction rests on

**Why this file.** The Day-5 retraction of BR.1 put all logical weight on the identity
$\mathfrak t(g,g)=\sum_\rho h(\gamma_\rho)$. Given the project's history (objects mis-stated by sloppy
truncation/notation: $\Phi$ on Day 1, the prime blow-up on Days 0/4), this new pillar must be **audited
before anything is built on it**. The referee posed three precise questions; this file answers each.
**Verdict up front:** EF-id is **unconditional on the dense core $\mathcal D$** (✅), but two corrections
to how it was stated are mandatory — the RHS is **indefinite, not positive** (Q2), and its behavior under
**closure in $H(E_\gamma)$ is open** (Q1).

**Tags:** ✅ rigorous/classical · ⬜ open.

---

## The precise statement (notation pinned)
Let $g$ be real and even with $\widehat g(r)=\int g(u)e^{-iru}du$. Define the **entire extension** of
$|\widehat g|^2$:
$$
h(r):=\widehat g(r)\,\widehat g^*(r),\qquad \widehat g^*(r):=\overline{\widehat g(\bar r)} .
$$
For real $r$, $h(r)=|\widehat g(r)|^2\ge0$. The Riemann–Weil explicit formula is
$$
\boxed{\ \sum_\rho h(\gamma_\rho)\;=\;\frac1{2\pi}\!\int_{\mathbb R}|\widehat g(r)|^2\,\Omega(r)\,dr\;+\;h(\tfrac i2)+h(-\tfrac i2)\;-\;2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,(g\star\tilde g)(\log n)\ }\tag{EF}
$$
i.e. $\displaystyle\sum_\rho h(\gamma_\rho)=\mathfrak a(g)+\mathfrak q(g)-\mathfrak p(g)=:\mathfrak t(g,g)$,
the sum over all nontrivial zeros $\rho=\tfrac12+i\gamma_\rho$. **(EF) is the definition of $\mathfrak t$
via its zero side; the right side is its arithmetic side.**

---

## Q2 — Is $\sum_\rho h(\gamma_\rho)$ positive? **NO.** (the notation correction)
Split the zeros:
- **On-line** $\rho=\tfrac12+i\gamma$, $\gamma\in\mathbb R$: $\;h(\gamma)=|\widehat g(\gamma)|^2\ \ge0$.
- **Off-line** quartet $\rho=\beta+it$ and its $\{1-\beta,\ \bar\rho,\ 1-\bar\rho\}$ partners — ordinates
  $\{t-ib,\,t+ib,\,-t-ib,\,-t+ib\}$, $b=\beta-\tfrac12\neq0$. For real-even $g$ (so $\widehat g$ is
  *real-entire*, $\widehat g^*=\widehat g$, $\widehat g(\bar z)=\overline{\widehat g(z)}$):
  $$
  \sum_{\text{quartet}}h=2\widehat g(t-ib)^2+2\widehat g(t+ib)^2=4\,\mathrm{Re}\big[\widehat g(t-ib)^2\big].
  $$
  This is **real but indefinite** (the real part of a square), and it is built from the **off-axis
  evaluation** $\widehat g(t-ib)$ — the Day-1 object.

Therefore
$$
\boxed{\ \mathfrak t(g,g)=\underbrace{\sum_{\text{on-line}}|\widehat g(\gamma)|^2}_{\ge0}\ +\ \underbrace{\sum_{\text{off-line quartets}}4\,\mathrm{Re}[\widehat g(t-ib)^2]}_{\text{indefinite}}\ }
$$
$$
\mathrm{RH}\iff\text{no off-line quartets}\iff\text{every term is }|\widehat g(\gamma)|^2\ge0\iff\mathfrak t\succeq0 .
$$
**Correction logged:** the Day-5 shorthand "$\sum_\rho|\widehat g(\gamma_\rho)|^2$" is valid **only** if
RH holds; in general the off-line terms are $4\,\mathrm{Re}[\widehat g(t-ib)^2]$, indefinite. Positivity is
**not** automatic — it *is* RH. (This is just Weil's criterion, recovered cleanly.)

---

## Q3 — What does RH assume *inside* the identity? **Nothing.** (Case A)
(EF) is a **theorem, unconditional**: it relates the sum over the *actual* zeros (wherever they lie) to
the arithmetic side, with no positivity or RH input. RH enters **only** in evaluating the *sign* of the
(unconditional) RHS, via the off-line terms. Consequences for how we may use it:
- ✅ **Legitimate:** using (EF) to **refute BR.1**. BR.1 was a claim on the *prime* side ($\mathfrak p\sim\sqrt N$);
  (EF) re-expresses $\mathfrak p=\mathfrak a+\mathfrak q-\sum_\rho h(\gamma_\rho)$, and for a smooth bump
  at generic real $T_0$ the zero side is finite (counts $O(\varepsilon\log T_0)$ on-line zeros, no off-line
  ones in the RH-true controls). So $\mathfrak p$ is finite — the $\sqrt N$ was a truncation artifact. The
  refutation is valid because (EF) is unconditional.
- ❌ **Illegitimate:** reading (EF) as $\mathfrak t\succeq0$. That step *is* RH; never use it.

So the retraction's logic stands: an **unconditional** identity exposes the **conditional-convergence
truncation** error. No circularity.

---

## Q1 — On what domain does (EF) hold? (the real frontier)
| Test class | Status of (EF) | Why |
|---|---|---|
| $C_c^\infty(\mathbb R)$ (compact support) | ✅ unconditional, classical | $\widehat g$ entire of exp. type ⟹ $g\star\tilde g$ compactly supported ⟹ **prime sum finite**; zero sum converges paired by $\pm\gamma$ (Weil/Bombieri) |
| $\mathcal D$ (Gaussian-localized, strip width $>\tfrac12$) | ✅ unconditional | $\widehat g$ Gaussian on horizontal lines ⟹ zero sum **absolutely** convergent (Gaussian decay beats $\log$ density); pole evals $\widehat g(\pm i/2)$ finite (strip $>\tfrac12$); prime sum abs. conv. (B2.2) |
| closure $\overline{\mathcal D}^{\,H(E_\gamma)}$ | ⬜ **OPEN** | (EF) holds on the dense core; whether the identity **and the sign** survive completion is the closability/spectral question |

**This is where the remaining content lives** (the referee's deep point). An identity valid on a dense
core need not control the closure: the bottom of the closed form can sit strictly below the core infimum
if a singular part appears. So:
$$
\boxed{\ \text{EF-id is }✅\text{ on the dense core }\mathcal D;\quad\text{its survival under }H(E_\gamma)\text{-closure is the open crux (closability).}\ }
$$

---

## Verdict and consequences
1. **EF-id survives the audit** — as an **unconditional identity on the dense core $\mathcal D$**. It is a
   genuine pillar, not another truncation artifact. ✅
2. **Two corrections are now permanent:** (Q2) the RHS is the **indefinite** decomposition above, *not*
   a sum of squares — positivity is RH; (Q1) validity is **core-level**, with the closure open.
3. **The B-2 question, restated exactly on the audited identity:**
   $$
   \text{B-2 in }H(E_\gamma):\quad \inf_{g\in\mathcal D,\ \|g\|_{H(E)}=1}\Big[\sum_{\text{on-line}}|\widehat g(\gamma)|^2+\sum_{\text{off-line}}4\,\mathrm{Re}[\widehat g(t-ib)^2]\Big]\ \overset{?}{>}\ -\infty .
   $$
   The on-line part is $\ge0$; the **off-line part** is where boundedness-below is at stake, each term a
   **bounded** $H(E_\gamma)$-evaluation (DB.3) ⟹ the question is whether the **sum over off-line zeros**
   converges — a **zero-density** statement (§3.3). Clean, phantom-free, and unconditional on $\mathcal D$.
4. **Open sub-task created:** prove (or refute) that (EF) and the sign extend from $\mathcal D$ to the
   $H(E_\gamma)$-closure. Until then, all spectral conclusions are *core-level* and must say so.

**Net.** The new pillar is sound but was mis-stated in two ways now fixed. The single genuinely open
analytic question has sharpened to: **does the explicit-formula identity survive closure in
$H(E_\gamma)$, and is the off-line-zero sum bounded below there?** — a zero-density problem on a verified
unconditional foundation. This is the first formulation in the Day 0–6 sequence that has survived a
deliberate hard audit without a retraction.
