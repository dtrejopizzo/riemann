# Day 14 — Audit of the "A.2 ⟺ lower frame bound" reduction: a second triviality found

Per the referee (Priority 1): before attacking the lower frame bound, audit the **reduction** itself
(A.2 $\Leftarrow$ lower frame bound, Day-12 §6) for a "Day-10 hole." **A real hole is found.** The Day-12 §6
reduction was carried out in the **critical space** ($R=K\rho\asymp1$), where A.2 is automatic — but there
the *whole* Weil form is **bounded**, so **B-2 is vacuous** (a *second* triviality, distinct from the
Day-9 trace-class one). The genuine faithful space is **over-sampling** ($R\to\infty$), and there A.2
(form-core for an *unbounded* $\mathfrak t_+$) is **not** the frame bound.

**Tags:** ✅ rigorous · ◆ standard · ❌ corrected · ⬜ open.

---

## 1. The hole: form-core is automatic in the critical space — but B-2 is vacuous there ❌
**Form-core from the upper bound alone.** If $\mu_{\mathrm{on}}=\sum_\gamma\delta_\gamma$ is **Carleson**
(critical density, one zero per resolution box), then $\mathfrak t_+(g)=\sum_\gamma|\widehat g(\gamma)|^2\le C\|g\|^2$
is **bounded**, so $D(\mathfrak t_+)=H$ and the graph norm $\|g\|^2_H+\mathfrak t_+(g)\asymp\|g\|^2_H$. Density
of $\mathcal D$ in $H$ then upgrades to graph-norm density: **$\mathcal D$ is a form-core automatically — the
lower frame bound is NOT needed.** So the Day-12 §6 reduction "A.2 $\Leftarrow$ lower frame bound" is, in
the critical space, vacuously true (A.2 holds from the upper bound).

**But the same boundedness kills B-2.** The off-line measure $\mu_{\mathrm{off}}=\sum\delta_{t-ib}$ has the
*same* (critical) horizontal density as $\mu_{\mathrm{on}}$, with depths $|b|<\tfrac12$ bounded away from the
strip edge $d=\tfrac12+\epsilon$. Hence $\mu_{\mathrm{off}}$ is **also Carleson** $\Rightarrow$ $\mathfrak t_-$
**bounded** $\Rightarrow$ $\mathfrak t=\mathfrak t_+-\mathfrak t_-$ is a **bounded** form. Then
$$
\boxed{\ \mathfrak t\ \text{bounded}\ \Longrightarrow\ \inf\operatorname{spec}\in(-\infty,\infty)\ \text{automatically}\ \Longrightarrow\ \text{B-2 is VACUOUS.}\ }
$$
**This is a second triviality (T2), distinct from trace-class (T1, Day 9):**
| | condition | what collapses |
|---|---|---|
| **T1** (Day 9) | $K\rho\in L^1$ ($\mu$ "trace-class") | $\mathfrak t_+$ compact; faithfulness fails |
| **T2** (Day 14) | $\mu$ Carleson, $R=K\rho$ **bounded** | $\mathfrak t$ bounded; **B-2 vacuous** (semiboundedness automatic) |
The critical space $R\asymp1$ — which Days 12–13 treated as *canonical* — is **T2-trivial.** The referee's
Priority-1 audit caught it.

---

## 2. The correction: genuine B-2 lives in the OVER-sampling regime $R\to\infty$ ✅
B-2 ("$\mathfrak t$ bounded **below** by a finite constant") is a non-trivial question only if $\mathfrak t$
can be **unbounded below** a priori, i.e. $\mathfrak t_-$ unbounded, i.e. $\mu_{\mathrm{off}}$ **not Carleson**,
i.e. off-line zeros **over-sample**. For a positive proportion of off-line zeros (density $\asymp\rho$) this
is the same as the on-line measure over-sampling:
$$
\boxed{\ \text{genuine (non-vacuous) B-2}\ \iff\ R(t)=K(t,t)\rho(t)\to\infty\ \ (\text{over-sampling, }\mu\text{ not Carleson}).\ }
$$
**Sharpened faithfulness ladder** (three regimes, two trivial):
| regime | $R=K\rho$ | $\mathfrak t_\pm$ | B-2 |
|---|---|---|---|
| trace-class (Gamma, std de Branges) | $\in L^1$ | compact | T1-trivial |
| critical (log-weighted, $K\asymp1/\rho$) | $\asymp1$ (bounded) | **bounded** | **T2-trivial (Day 14)** |
| **over-sampling (flat Hardy, $K\asymp$const)** | $\to\infty$ | **unbounded** | **genuine** |
So the genuine space is **flat (or sub-critical-weight) Hardy-band**, where $R\sim\log t\to\infty$. The
"critical scaling law $K\asymp1/\rho$" highlighted Days 12–13 is the **boundary of T2-triviality**, *not*
the canonical faithful space — an honest reversal.

> **Note on the necessary scaling law.** "faithful $\Rightarrow K\rho\notin L^1$" (DENS.1) is still correct
> as a *necessary* condition, but it is not *sufficient* for genuine B-2: the critical case $R\asymp1$
> satisfies $K\rho\notin L^1$ yet is T2-trivial. The sufficient (genuine) condition is the strictly stronger
> $R\to\infty$.

---

## 3. In the over-sampling space, A.2 ≠ the lower frame bound (the reduction corrected) ✅
With $R\to\infty$, $\mu_{\mathrm{on}}$ is **not** Carleson, so $\mathfrak t_+$ is **unbounded**:
$D(\mathfrak t_+)\subsetneq H$, graph norm strictly stronger. The three properties now **separate**:
- **upper frame bound (Carleson):** $\mathfrak t_+\lesssim\|\cdot\|^2$ — **FAILS** (over-dense).
- **lower frame bound (coercivity):** $\mathfrak t_+\gtrsim\|\cdot\|^2$ — plausibly **holds** (over-sampling
  gives more than enough samples), making $T_+\ge c>0$ invertible. *This is about coercivity, not core-ness.*
- **form-core A.2:** $\mathcal D$ dense in $D(\mathfrak t_+)$ (graph norm) — a **separate** question, not
  implied by either frame bound.

So the Day-12 §6 reduction "A.2 $\Leftarrow$ lower frame bound" is **wrong in the genuine space**: it
conflated form-core with coercivity. Corrected statement:
$$
\boxed{\ \text{In the over-sampling space: A.2 (form-core) and the lower frame bound (coercivity) are DISTINCT; neither implies the other directly.}\ }
$$
A.2 must be attacked as a genuine **density/core** question (is $\mathcal D$ a core for the unbounded
zeta-sampling operator $T_+$?), e.g. via showing $T_+$-graph approximation of localizers — *not* via a
frame inequality.

---

## 4. New impossibility constraint (K5) and the corrected map
Add to the K1–K4 list (Day 11):
- **K5 (bounded $\perp$ genuine B-2):** if $R=K\rho$ is **bounded** ($\mu$ Carleson), the Weil form is
  bounded and B-2 is vacuous. So genuine B-2 forces $R\to\infty$ (over-sampling). ✅

The corrected dependency (Problem B):
```
   faithful realization
        │   R = K(t,t)ρ(t)  must → ∞   (K5: bounded ⇒ B-2 vacuous; T1: ∈L¹ ⇒ trace-class)
        ▼
   over-sampling Hardy-band (flat, |E|≍const)
        │
        ├──►  A.2 (form-core for UNBOUNDED 𝔱₊)   ⬜  [≠ lower frame bound]
        │
        └──►  B-2 = RFB (𝔱₋ rel. bounded by 𝔱₊)  ⬜  both over-dense; relative Carleson
        │
        ▼
   sign of inf spec(𝒯) = RH
```

---

## 4½. Priority-2 first step: in the over-sampling space, COERCIVITY is the easy part ✅(reduction)
A bonus from the correction: the **lower frame bound** $\mathfrak t_+(g)\gtrsim\|g\|^2$ (coercivity of
$T_+$) is actually **the easy property** in the over-sampling space. By Beurling-type sampling theory, a
real sequence is a *set of sampling* (lower bound) once its **lower Beurling density exceeds the space's
Nyquist density**. The zeros have density $\rho(t)\sim\log t\to\infty$, exceeding any fixed Nyquist
$\sim1/d$ for large $t$ — so they over-sample and the lower bound holds at large $t$, modulo a
**finite-dimensional correction** at low $t$ (the sparse region below $\gamma_1\approx14.13$, finitely many
"gaps"). Hence
$$
\boxed{\ \text{coercivity }T_+\ge c>0\ \text{holds in the over-sampling space (over-dense zeros), modulo a finite-rank low-}t\text{ correction.}\ }
$$
With coercivity, the graph norm $\asymp\mathfrak t_+$, so **A.2 (form-core)** reduces to: *is $\mathcal D$
dense in the sampling norm $\big(\sum_\gamma|\widehat g(\gamma)|^2\big)^{1/2}$?* — a density question, and
**B-2 (RFB)** simplifies to $\mathfrak t_-\lesssim\mathfrak t_+$, i.e. the **off-line over-dense measure is
dominated by the on-line over-dense measure** (relative density/Carleson comparison). So the genuine
difficulty is **not** coercivity; it is (a) form-core density and (b) the off-line$\le$on-line relative
bound — both governed by the *fine* zero geometry (separation, $S(T)$, pair correlation), as the referee
foresaw. *(This identifies which classical input enters: not Beurling density alone — that gives coercivity
for free — but the finer comparison/regularity for RFB and form-core.)*

---

## 5. Status

| Item | Before (Day 12–13) | After (Day 14 audit) |
|---|---|---|
| canonical faithful space | critical $R\asymp1$ | ❌ **T2-trivial**; genuine is **over-sampling $R\to\infty$** |
| A.2 $\Leftarrow$ lower frame bound | claimed (Day-12 §6) | ❌ **only in T2-trivial critical space**; in genuine space A.2 ≠ frame bound |
| B-2 in critical space | "reduces to RFB" | ❌ **vacuous** ($\mathfrak t$ bounded) |
| faithfulness for B-2 | $K\rho\notin L^1$ | ✅ necessary; **genuine B-2 needs $R\to\infty$** (strictly stronger) |
| constraint list | K1–K4 | ✅ **+K5** (bounded $\perp$ genuine B-2) |

**Net (Day 14).** The referee's Priority-1 audit of the reduction was exactly right and found a real hole:
the Day-12 §6 "A.2 $\Leftarrow$ lower frame bound" was done in the **critical space**, which turns out to be
a **second triviality (T2): the Weil form is bounded there, so B-2 is vacuous.** The genuine faithful space
is **over-sampling** ($R=K\rho\to\infty$, flat Hardy-band), where $\mathfrak t_\pm$ are unbounded, B-2 is a
real question (RFB), and **A.2 (form-core) separates from the lower frame bound** (the latter is
coercivity, not core-ness). New constraint **K5** (bounded $\perp$ genuine B-2). The durable scaling
insight survives but is sharpened: *a genuine realization must over-compensate the zero density,
$R=K\rho\to\infty$* — critical sampling is exactly the boundary where the problem goes vacuous.

**Next (corrected priorities, per referee Priority 2):** in the over-sampling space, identify the **minimal
zero-regularity hypothesis** (separation / Beurling lower density / $S(T)$ / pair correlation) that gives
either (a) the lower frame bound (coercivity of $T_+$) or (b) form-core A.2 — now correctly distinguished.
Defer F1 (referee Priority 3).
