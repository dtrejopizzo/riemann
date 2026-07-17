# Phase 0.B — Cartography of the truncation lemma (first pass)

**The advisor's question:** is the truncation lemma *technical* (provable by harmonic analysis +
unconditional results) or *RH in disguise*? **First-pass answer: the truncation lemma proper is
very likely TECHNICAL and unconditional; the RH-equivalent content lives in a *separate*
ingredient (global positivity, = the plan's (LB)), which we already isolate.** This is good news —
it means Front B of Lise Science run 8 is a real harmonic-analysis problem, not a reformulation. Below is
the reasoning; it must be confirmed by the v8 numerics (Front C) and an expert.

---

## 1. Decompose the truncation error by side

From 0.A.1, the truncation discrepancy of $Q$ comes from three tails:
$$Q - Q_{\text{complete}} \;=\; \underbrace{(\text{zero-sum tail})}_{|\gamma|>H}
\;-\;\underbrace{(\text{prime-sum tail})}_{n>X}\;-\;\underbrace{(\text{archimedean tail})}_{\text{integral}} .$$
Treat each separately. The test functions $\varphi_j\star\tilde\varphi_k$ are Hermite–Gauss:
localized at $T_0$, width $\sigma$, dimension up to $J$, with **super-polynomial (Gaussian-type)
decay** in both the time variable $u$ and the spectral variable $r$.

### 1a. Prime-sum tail — UNCONDITIONALLY benign
$g=\varphi_j\star\tilde\varphi_k$ has **effectively bounded support** in $u$: the Hermite–Gauss
window of width $\sigma$ and order $J$ is concentrated on $|u|\lesssim \sigma\sqrt{2J{+}1}=:U$.
Hence $g(\log n)$ is negligible for $\log n \gg U$, i.e. $n\gg e^{U}$. So
$$\sum_{n>X}\frac{\Lambda(n)}{\sqrt n}\,g(\log n) \ \text{ is super-polynomially small once } X>e^{U}.$$
**No hypothesis needed.** This matches the engine finding that a prime cutoff $X=10^5$ (with full
archimedean) suffices and a short cutoff $10^3$ fails: the failure is *under-resolving the support
of $g$*, not a number-theoretic obstruction. ✅ technical, unconditional.

### 1b. Archimedean tail — computable, no obstruction
$A(g)=\frac1{2\pi}\int h(r)\,\Omega(r)\,dr$ with $\Omega(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}{2})-\log\pi$,
$\Omega(r)=O(\log|r|)$. Since $h=\hat g$ is Gaussian-localized at $T_0$, the integrand decays
super-polynomially; the tail past any cutoff is explicitly bounded. ✅ technical, unconditional.

### 1c. Zero-sum tail — THE substantive one
$$\sum_{|\gamma-T_0|>W} h(\gamma), \qquad h=\hat{(\varphi_j\star\tilde\varphi_k)} \ \text{ Gaussian-localized at } T_0 .$$
Bound it by (density of zeros) × (Gaussian tail of $h$). The zero-counting function is
$$N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\qquad\text{(Riemann–von Mangoldt, UNCONDITIONAL)},$$
so the local density near height $T_0$ is $\tfrac1{2\pi}\log T_0$, **unconditionally**, and this
counts *all* nontrivial zeros regardless of real part. Therefore
$$\Big|\sum_{|\gamma-T_0|>W} h(\gamma)\Big|\ \le\ \Big(\tfrac{1}{2\pi}\log T_0 + o(\log T_0)\Big)\!\int_{|r-T_0|>W}\!|h(r)|\,dr
\ +\ (\text{contribution of any off-line }\gamma),$$
and the Gaussian integral is explicit. For the **GRH-consistent controls** (no off-line zeros, $h(\gamma)$
real-argument Gaussian) this is an **unconditional, explicit bound** → the baseline floor
$\eta(T_0,\sigma,J,X,H)$ is controllable without any hypothesis. ✅ technical — *subject to §2*.

---

## 2. The one place uniformity could bite: the $J$-dependence

The catch the advisor would press on: as $J$ grows, Hermite functions oscillate more and their
spectral transforms develop heavier (though still super-exponentially bounded) tails. The signal
amplifies super-polynomially ($\log|\lambda_{\min}|\approx 0.569\,J\log J$); the **question is
whether the zero-sum tail bound stays below the signal *uniformly in $J$*.**

- The Hermite tail constant grows like $\sim C^{J}$ or $J!$-type — fast, but the explicit-formula
  identity means the *complete* sum is exact, so the tail is the difference of two large
  quantities; controlling it needs an **explicit, $J$-uniform** Hermite-tail-vs-zero-density
  estimate. This is exactly the lemma Front B must prove.
- This is a **harmonic-analysis estimate** (Gaussian/Hermite tails against a $\log T$ density),
  **not** a statement about where the zeros are. So it is plausibly **technical**.
- The empirical evidence (≈90 orders of magnitude signal-to-baseline separation at $J=20$, baseline
  at the numerical floor) strongly suggests the margin does *not* close — i.e. the uniform bound
  exists. Front C of v8 will measure exactly this.

**Provisional verdict:** the truncation lemma reduces to a **$J$-uniform Hermite-tail vs
Riemann–von Mangoldt-density estimate** — unconditional harmonic analysis, no RH inside. ⚠ confirm
the $J$-uniformity numerically (v8 Front C) and with an analyst.

---

## 3. Implication table (first pass — to be filled by v8 Front C + expert)

| Known result | Controls | Implies the truncation lemma? | Confidence |
|---|---|---|---|
| **Riemann–von Mangoldt** $N(T)$ | zero density near $T_0$ (all zeros) | **the zero-sum tail bound — YES, unconditional** | high (classical) |
| Explicit Hermite/Gaussian tail bounds | the test-function tails | prime + archimedean + spectral tails | high |
| Vinogradov–Korobov zero-free region | a zero-free strip near $\sigma=1$ | not needed for the tail; sharpens constants only | medium |
| Lindelöf | $\zeta$ growth on the line | not needed for truncation (only for global size of $Z$) | medium |
| Zero-density $N(\sigma,T)$ | # zeros off the line | not needed if we only bound the GRH-control baseline | medium |
| **(LB): $B\succeq0$ for $\zeta$'s arithmetic** | global positivity | **this is RH itself — NOT the truncation lemma** | high |

**Key separation made precise:** the truncation lemma (Front B) ≠ the positivity (LB). The former
is plausibly unconditional harmonic analysis; the latter is RH. The advisor's worry ("the lemma
hides RH") applies to **(LB), which we already flag as RH-equivalent**, not to the truncation
control. *If this holds up, Front A's detector theorem becomes UNCONDITIONAL — a real, publishable
result independent of RH.*

---

## 4. What this commissions

- **v8 Front C** must verify the §2 $J$-uniformity empirically: does $\eta(T_0,\sigma,J)$ stay below
  the forced-negativity floor $c(\delta,\sigma,J)$ across the whole $J$-range? If yes → technical
  verdict confirmed.
- **Expert check** (Phase 4 early): is the $J$-uniform Hermite-tail vs von-Mangoldt-density estimate
  in the literature, or genuinely open-but-provable? Nearest: explicit-formula error analysis
  (Iwaniec–Kowalski §5), Hermite-function tail asymptotics.
- **If §2 fails** (margin closes at large $J$): the lemma becomes conditional/hypothesis-strength,
  and we reframe Front A's theorem honestly. Even then it is publishable as conditional.

**Bottom line of 0.B:** the cautious-case the advisor feared — "all your effort funnels into a lemma
that is secretly RH" — appears **not** to apply to the *truncation* lemma. The RH-equivalent content
is cleanly quarantined in (LB). That is the most reassuring possible first-pass result, and it makes
the v8 Front-A detector theorem a realistic *unconditional* target.
