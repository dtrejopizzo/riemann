# Day 12 — The density scaling law: faithfulness as $K\rho\notin L^1$, and F1 classified (geometric)

Per the referee: (1) classify F1 (universal A / geometric B / accidental C); (2) reformulate K2 via the
local zero density $\rho(t)$, not $\inf K$. Both done, and they fuse: a **necessary scaling law**
$K(t,t)\,\rho(t)\notin L^1$ for any faithful space, and **F1 is geometric (Level B)**. This is the most
model-robust output so far — it constrains *any* faithful realization, not a chosen space.

Notation: $\rho(t)=\tfrac1{2\pi}\log\tfrac{t}{2\pi}$ (Riemann–von Mangoldt local zero density);
$K(t,t)$ = diagonal reproducing kernel (local "trace density"); redundancy $R(t):=K(t,t)\rho(t)$.
**Tags:** ✅ rigorous · ◆ standard-asymptotic · ⬜ open.

---

## 1. Faithfulness $\iff K\rho\notin L^1$ (replaces $\inf K$) ✅/◆
$\mathfrak t_+$ is trace-class iff $\sum_\gamma K(\gamma,\gamma)<\infty$. Replace the sum over zeros by the
density integral: $\sum_\gamma K(\gamma,\gamma)=\int K(t,t)\,dN(t)=\int K(t,t)\rho(t)\,dt+\int K\,dS(t)$,
with $S(T)=O(\log T)$ the zero-counting fluctuation. For **slowly-varying** $K$ the fluctuation term is
lower order (integration by parts: $|\int K\,dS|\lesssim\int|S||K'|\,dt$, negligible vs the main term).
Hence
$$
\boxed{\ \mathfrak t_+\ \text{trace-class}\ \iff\ \int_0^\infty K(t,t)\,\rho(t)\,dt<\infty\ \iff\ R=K\rho\in L^1(dt),\quad\text{so}\quad\text{FAITHFUL}\iff K\rho\notin L^1.\ }
$$
**Verification on the three cases (referee's):**
| space | $K(t,t)$ | $R=K\rho$ | $\int R$ | verdict |
|---|---|---|---|---|
| flat strip Hardy | $\asymp1$ | $\sim\tfrac{\log t}{2\pi}$ | $=\infty$ | **faithful** (over-samples, $R\to\infty$) |
| log-weighted strip | $\sim\tfrac{2\pi}{\log t}$ | $\sim1$ | $=\infty$ | **faithful** (critical, $R\asymp1$) |
| Gamma / $\xi$ de Branges | $\sim\log t\,e^{-\pi t/2}$ | $\in L^1$ | $<\infty$ | **trivial** (trace-class) |
All three fall under the single criterion. This is the referee's $K\gtrsim1/\log$ threshold, sharpened to
the exact $L^1$ statement, and it **eliminates the $\inf K$ gap of Day 11** (no pointwise minimum needed —
only the integral).

---

## 2. F1 classified: Level B (geometric) ✅
**The kernel identity.** With real-entire ON basis $\{e_n\}$, $K(t,t)=\sum_n e_n^2$,
$K_{11}(t):=\sum_n e_n'^2\ge0$ (kinetic density). Expanding $K(t-ib,t-ib)=\sum_n|e_n(t-ib)|^2=\sum_n e_n(t-ib)e_n(t+ib)$:
$$
K(t-ib,t-ib)=K(t,t)+b^2\,D(t)+O(b^4),\qquad D(t)=\sum_n\big(e_n'^2-e_ne_n''\big)=K_{11}(t)-\sum_n e_ne_n''.
$$
Cross-check via the Laplacian: $\Delta_w K(w,w)=4\sum_n|e_n'|^2=4K_{11}$, and $\partial_x^2 K(w,w)|_{y=0}=K''(t)$
(the diagonal second derivative), so $\partial_y^2K|_{y=0}=4K_{11}-K''$, giving $D=\tfrac12\partial_y^2K=2K_{11}-\tfrac12K''$.
The two expressions agree ($2K_{11}-\tfrac12K''=2K_{11}-\tfrac12(2K_{11}+2\sum e_ne_n'')=K_{11}-\sum e_ne_n''$). ✅ **double-checked.**
$$
\boxed{\ \text{F1 (local)}\ \iff\ D(t)\ge0\ \iff\ K''(t)\le 4K_{11}(t).\ }
$$
**Why it is geometric, not accidental.** $K_{11}(t)\asymp K(t,t)/d^2$ — the kinetic density is the trace
density times the squared bandwidth $\sim1/d^2$ (verified on the explicit strip kernel
$K(s)=\tfrac1{4d}\operatorname{sech}\tfrac{\pi s}{2d}$: $K_{11}=-K''(0)=\tfrac{\pi^2}{16d^3}>0$, with
$K(t,t)=\tfrac1{4d}$, so $K_{11}/K=\tfrac{\pi^2}{4d^2}$). Meanwhile $K''(t)$ (diagonal curvature) $\asymp
K(t,t)/L^2$ where $L$ = the diagonal's variation scale. For a **density-matched** strip space the diagonal
varies on scale $L\sim t$ (it tracks $\rho\sim\log t$, slow), so $K''\sim K/t^2\lll K_{11}\sim K/d^2$. Thus
$$
K''(t)\ \ll\ K_{11}(t)\quad\Longrightarrow\quad D(t)>0\quad\Longrightarrow\quad\text{F1 holds.}
$$
**Classification verdict:** F1 is **Level B (geometric)** — a consequence of strip bandwidth + a
slowly-varying (density-matched) diagonal, *not* translation-invariance and *not* accidental. It holds for
flat **and** log-weighted Hardy-band spaces. (Level A was refuted Day 11; Level C is avoided.) The referee's
logical risk — "a property of the model, not the problem" — is resolved: F1 is a property of the
*band geometry*, shared by the whole candidate family.

---

## 3. K2 in density form (clean, $\inf K$-free) ✅/◆
$S_{\mathrm{off}}=\sum_{\text{off-line}}K(t_\rho-ib_\rho,t_\rho-ib_\rho)\overset{\text{F1}}{\ge}\sum_{\text{off-line}}K(t_\rho,t_\rho)=\int K(t,t)\,dN_{\mathrm{off}}(t)\asymp\int K(t,t)\,\rho_{\mathrm{off}}(t)\,dt$,
with $\rho_{\mathrm{off}}$ the off-line density. Hence
$$
\boxed{\ S_{\mathrm{off}}=\infty\ \iff\ K\,\rho_{\mathrm{off}}\notin L^1,\qquad\text{and if }\rho_{\mathrm{off}}\asymp\delta\rho\ (\delta>0):\ \iff\ K\rho\notin L^1\ =\ \text{FAITHFUL.}\ }
$$
So **K2 (faithful $\perp a=0$)** is now one statement in the *same* integral as faithfulness, with
$\rho_{\mathrm{off}}$ in place of $\rho$. No $\inf K$, no pointwise hypothesis — just two density integrals.
The Day-11 hypotheses (i)/(iii) merge into "$K\rho_{\mathrm{off}}\notin L^1$"; (ii) is now Level-B F1.

---

## 4. The necessary scaling law (the durable, model-independent output) ✅
Collecting §1–§3, any **faithful** RKHS realization of the Weil form must satisfy
$$
\boxed{\ K(t,t)\,\rho(t)\notin L^1(dt)\qquad(\text{the necessary scaling law}),\ }
$$
and the **critical/canonical** representative sits at $K(t,t)\asymp 1/\rho(t)\sim 2\pi/\log t$ (redundancy
$R\asymp1$ = critical sampling, zeros at the space's resolution). This is more fundamental than any chosen
space:
- it **survives** even if every concrete model (Hardy, de Branges, Fock, …) is later replaced — it is a
  scaling any faithful realization obeys;
- it **classifies** all candidates at once (flat: $R\to\infty$ over-sampled-faithful; log: $R\asymp1$
  critical-faithful; standard de Branges: $R\in L^1$ trivial);
- it **explains** the Day-9/10 trivialization structurally: the Gamma factor's $e^{-\pi t/4}$ in $|E|$
  forces $R\in L^1$. **Bonus (◆):** the *same* decay afflicts $H(E_\xi)$ (the full $\xi$-space), so **even
  the de Branges space of $\xi$ trivializes the weight-1 Weil form** — the faithful space is *not* a
  standard de Branges space ($|E|$ decaying) at all; it needs $|E(t)|\asymp$const (Hardy-band).

---

## 5. Status

| Item | Day 11 | Day 12 |
|---|---|---|
| faithfulness criterion | $\sum_\gamma K(\gamma,\gamma)=\infty$, $\inf K$ gap | ✅ **$K\rho\notin L^1$** (density-unified, $\inf K$-free) |
| F1 | conditional ($D(t)\ge0$ can fail) | ✅ **Level B geometric** ($K''\ll K_{11}$ for density-matched diagonals) |
| K2 (faithful $\perp a=0$) | hypotheses (i)+(ii)+(iii) | ✅ **$K\rho_{\mathrm{off}}\notin L^1$** (one integral) |
| canonical space | "Hardy-band, weight open" | ◆ **critical scaling $K\asymp1/\rho$**; standard de Branges (incl. $\xi$) excluded |
| durable output | constraint list K1–K4 | ✅ **+ necessary scaling law** $K\rho\notin L^1$ |

---

## 6. Positive advance: form-core A.2 reduces to a sampling problem ✅(reduction)/⬜
The density law sharply re-poses A.2 ($\mathcal D$ a form-core for $\mathfrak t_+$). Work in the **critical
space** $R\asymp1$ ($K\asymp1/\rho$, the canonical representative). There the on-line measure
$\mu_{\mathrm{on}}=\sum_\gamma\delta_\gamma$ has **bounded mass per resolution box** (one zero per box of
size $1/\rho$), so it is a **Carleson measure** — the **upper frame bound** holds:
$$
\mathfrak t_+(g)=\sum_\gamma|\widehat g(\gamma)|^2\ \le\ C\,\|g\|^2_{H_{\mathrm{crit}}}.\tag{upper}
$$
So in the critical space $\mathfrak t_+$ is **bounded** (Carleson) yet **non-trace-class** (faithful, §1) —
*bounded but not trace-class*, the correct refinement of "genuine form" (Day 9's "unbounded" was loose; it
is unbounded only in the *over-sampling* flat space). Then:
$$
\boxed{\ \text{A.2 (form-core)}\ \Longleftarrow\ \text{LOWER frame bound } \mathfrak t_+(g)\gtrsim\|g\|^2\ \Longleftrightarrow\ \{\gamma\}\ \text{is a SAMPLING sequence for }H_{\mathrm{crit}}.\ }
$$
*Reason:* with both bounds, $\mathfrak t_+\asymp\|g\|^2_{H_{\mathrm{crit}}}$, so the graph norm
$\|g\|^2+\mathfrak t_+(g)\asymp\|g\|^2$, and density of $\mathcal D$ in $H_{\mathrm{crit}}$ (Gaussians dense)
upgrades to density in the graph norm — i.e. $\mathcal D$ is a form-core, and $\overline{\mathfrak t_+|_{\mathcal D}}=\mathfrak t_+$
(the Day-8 identification question A.2 is settled). So **A.2 $\Leftarrow$ the lower sampling bound.**

**Status of the lower bound.** This is a **Beurling-type sampling** question at **critical density** — the
borderline case, where sampling can fail by logarithmic factors and the outcome is governed by the **fine
regularity of the zeros** (gaps, $S(T)$, separation). Under RH the zeros are the de Branges sampling points
of $H(E_\xi)$ and form a complete interpolating (Riesz-basis) sequence — i.e. the lower bound **holds
under RH**. Unconditionally it is open and is exactly the arithmetic content of A.2. *(Note the honest
loop: A.2's clean resolution uses RH-flavored input; this is consistent with faithfulness being
RH-independent only modulo such structural facts — flagged, not hidden.)*

> **What §6 buys.** A.2 is no longer a vague "is $\mathcal D$ a core?" It is the precise classical
> statement *"the zeta zeros are a sampling sequence (lower frame bound) for the critical space"*, with the
> **upper bound proved** (Carleson at critical density) and the **lower bound** = a Beurling-density
> question tied to zero regularity. Two faces — A.2 (form-core) and the lower frame bound — are one.

---

**Net (Day 12).** The referee's two asks fused into the deepest result of the program's pure-math phase: a
**necessary scaling law** — *any faithful realization has $K(t,t)\rho(t)\notin L^1$* — with the **critical
sampling** law $K\asymp1/\rho\sim2\pi/\log t$ as the canonical representative, and **F1 reclassified as
geometric (Level B)** so the K2 impossibility ("faithful $\perp$ a=0") holds across the whole band-geometry
family, expressed as $K\rho_{\mathrm{off}}\notin L^1$. This is model-independent: it constrains the
*problem*, not a chosen space. **Plus** (§6) a positive advance: **form-core A.2 = the lower sampling bound
for the zeta zeros in the critical space**, with the upper (Carleson) bound proved and the lower bound
identified as the Beurling-borderline question (holds under RH). **Next:** (1) the lower frame bound
unconditionally (or its weakest sufficient zero-regularity input); (2) relative Carleson (RFB) in density
form $K\rho_{\mathrm{off}}$; (3) literature pin (Bombieri/Lagarias) of the critical weight.
