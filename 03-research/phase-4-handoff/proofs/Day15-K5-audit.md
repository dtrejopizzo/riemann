# Day 15 — Audit of K5/T2: the Carleson step conflated two invariants ($R=K\rho$ vs $P=\rho\ell$)

Per the referee: audit K5 (the Day-14 claim $R\asymp1\Rightarrow\mu$ Carleson $\Rightarrow\mathfrak t$
bounded $\Rightarrow$ B-2 vacuous) **before** treating it as a pillar. The audit follows the referee's own
three-step recipe (define an intrinsic scale $\ell$; relate it to $R$; deduce Carleson). **Finding: K5's
Carleson step is wrong** — it used the trace-density invariant $R=K\rho$ where the Carleson property is
governed by a *different* invariant $P=\rho\ell$ (points per resolution cell). The Day-14 genuine-space
conclusion survives, but via the corrected reason. **Tags:** ✅ rigorous · ❌ corrected · ⬜ open.

---

## 1. The intrinsic resolution scale (referee's step 1) ✅
For a RKHS, the kernel's **coherence length** at $t$ is
$$
\ell(t):=\sqrt{\frac{K(t,t)}{K_{11}(t)}},\qquad K_{11}(t)=\sum_n e_n'(t)^2=\partial_t\partial_{t'}K\big|_{\mathrm{diag}} ,
$$
because $K(t,t')=K(t,t)\big(1-\tfrac12 (t'-t)^2 K_{11}/K+\cdots\big)$ decorrelates on scale $\ell$. This is
the space's effective sample spacing (Nyquist length). **Computed for Hardy-band** $H^2(S_d)$
($K(s)=\tfrac1{4d}\operatorname{sech}\tfrac{\pi s}{2d}$): $K=\tfrac1{4d}$, $K_{11}=\tfrac{\pi^2}{16d^3}$, so
$$
\boxed{\ \ell(t)=\sqrt{\tfrac{1/4d}{\pi^2/16d^3}}=\tfrac{2d}{\pi}\asymp d\quad(\text{constant in }t).\ }
$$
For any **slowly-varying weight** on the width-$d$ strip (varying on scale $\gg d$, e.g. the "critical"
$K\sim1/\log t$), $K_{11}\asymp K/d^2$ still holds (bandwidth set by the strip width, not the weight), so
$\ell\asymp d$ **regardless of the weight**.

---

## 2. The correct Carleson invariant is $P=\rho\ell$, not $R=K\rho$ (referee's step 2) ✅
A discrete measure of horizontal density $\rho(t)$ and coherence length $\ell(t)$ is **Carleson** iff the
mass per coherence cell is bounded:
$$
\boxed{\ \mu\ \text{Carleson}\iff P(t):=\rho(t)\,\ell(t)\ \text{bounded}.\ }
$$
Relate to $R$: $R=K\rho$, $P=\rho\sqrt{K/K_{11}}$, so $R/P=\sqrt{K K_{11}}\asymp K/d$ (Hardy-band), i.e.
$P\asymp R\,d/K$. **They are different invariants** and coincide only when $K\asymp d\asymp$const (the flat
case). In particular, for the "critical" weight $K\sim1/\log t$ (Day-14's supposed T2 space):
$$
R=K\rho\asymp1\quad\text{but}\quad P=\rho\ell\asymp \rho\,d\sim d\log t\to\infty .
$$
So **$R\asymp1$ does NOT give $P$ bounded** — the critical-weight space has $P\to\infty$, i.e. it
**over-samples and $\mu$ is NOT Carleson**. The Day-14 step "$R\asymp1\Rightarrow\mu$ Carleson" is **false**;
it conflated the trace-density scaling $R$ with the sampling invariant $P$. *(The referee's exact concern.)*

---

## 3. Consequence: every eval-bounding strip space over-samples (referee's step 3) ✅
Bounded off-axis evaluations at depth $\tfrac12$ require strip half-width $d\ge\tfrac12$ (else the depth-$\tfrac12$
kernel diverges). Hence $\ell\asymp d\gtrsim\tfrac12$ is **bounded below**, so
$$
P(t)=\rho(t)\,\ell(t)\ \gtrsim\ \tfrac12\,\rho(t)\sim\tfrac{\log t}{4\pi}\ \to\ \infty .
$$
$$
\boxed{\ \text{Any width-}d\ge\tfrac12\text{ strip-Hardy space (any weight) OVER-samples: }\mathfrak t_+\ \text{is UNBOUNDED. No T2 there.}\ }
$$
So **T2 (a bounded, Carleson, faithful space) does not occur within the eval-bounding Hardy-band family.**
The only Carleson ($P\asymp1$) spaces are **resolution-shrinking** ($\ell\sim1/\rho\sim1/\log$), i.e. with
growing phase density $\varphi'\sim\log$ — the **de Branges** spaces (Gamma, $\xi$). But there $|E|$ decays
($e^{-\pi t/4}$) $\Rightarrow$ **T1 (trace-class)** (Day 9). A genuine T2 (Carleson **and** non-trace-class)
would need $\varphi'\sim\log$ together with $|E|\asymp$const — and the **Hermite–Biehler phase–amplitude
relation** ties $\log|E|$ to $\varphi$, so whether such an $E$ exists is **not established**. T2 probably
**collapses into T1** (resolution-shrinking forces $|E|$ decay).

---

## 4. Verdict on K5, and what survives

| claim | Day 14 | Day 15 (audited) |
|---|---|---|
| $R\asymp1\Rightarrow\mu$ Carleson | used | ❌ **false** — Carleson governed by $P=\rho\ell$, not $R=K\rho$ |
| T2 (bounded $\mathfrak t$, B-2 vacuous) as a separate triviality | asserted (K5) | ◆ **not established**; no T2 among eval-bounding spaces; likely collapses into T1 |
| genuine space = over-sampling Hardy-band | ✅ (via "critical is T2") | ✅ **survives, corrected reason**: $\ell\gtrsim\tfrac12$ const $\Rightarrow P\to\infty$ for *all* eval-bounding strip spaces |
| $\mathfrak t_+$ unbounded in the genuine space | ✅ | ✅ (unchanged) |
| DENS.1 (faithful $\iff K\rho\notin L^1$) | — | ✅ **unaffected** (it is about $R$/trace-class T1, the correct invariant for that question) |

**Two invariants, cleanly separated (the durable gain):**
$$
\underbrace{R=K(t,t)\,\rho(t)}_{\text{trace-class / T1: }R\in L^1}\qquad\text{vs}\qquad\underbrace{P=\rho(t)\,\ell(t)}_{\text{Carleson / boundedness: }P\ \text{bounded}},\qquad \ell=\sqrt{K/K_{11}} .
$$
Day-14 used $R$ where $P$ was needed. With $P$, the picture is *cleaner than Day 14 claimed*: every
admissible (eval-bounding) space **over-samples** ($P\to\infty$, because $\ell\ge\tfrac12$), so
$\mathfrak t_+$ is **always unbounded** and the genuine-space conclusion is **forced**, not contingent on a
T2 dichotomy. The "critical scaling $K\asymp1/\rho$" (Days 12–13) is a *trace-density* normalization,
**not** critical sampling — that terminology is corrected.

---

## 5. Net (Day 15)
The referee's audit of K5 was right and found a genuine conflation: **K5's "$R\asymp1\Rightarrow$ Carleson"
is false**, because Carleson is controlled by $P=\rho\ell$ (resolution), not $R=K\rho$ (trace density), and
for any eval-bounding strip space $\ell\gtrsim\tfrac12$ forces $P\to\infty$ (always over-sampling). So **T2
is not a separate triviality** within the admissible family (it would require a resolution-shrinking,
non-trace-class space, blocked by the HB phase–amplitude relation; likely collapses to T1). The Day-14
**conclusion survives with a stronger, cleaner justification**: the genuine faithful space is over-sampling
Hardy-band **necessarily** ($\ell\ge\tfrac12$), $\mathfrak t_+$ unbounded, B-2 genuine. The durable output is
the **clean separation of two invariants** $R$ (trace-class) and $P$ (Carleson), which Day-14 had merged.
**K5 downgraded** ◆; **the over-sampling characterization upgraded** to forced.

**Next:** with the geometry corrected, return to **RFB** ($\mathfrak t_-\lesssim\mathfrak t_+$, both
over-dense) — the relative comparison where separation / $S(T)$ / pair correlation finally enter (referee
Priority 2). Defer F1 (Priority 3).
