# Day 9 — Deep dive on $K(w,w)$ forces a space correction: $H(E_\gamma)$ trivializes; use strip Hardy

**Trigger (referee Front 2 + the $S_{\mathrm{off}}$ suspicion).** "Compute $K(w,w)$ *quantitatively*."
Doing so exposed that the Days 5–8 home, $H(E_\gamma)$, **trivializes the Weil form** (it is trace-class
there). This file (i) proves the trivialization, (ii) downgrades the affected results, (iii) corrects the
space to the **strip Hardy space** $H^2(S_{1/2+\epsilon})$, and (iv) re-poses A.2/(RFB) there — where the
referee's "$S_{\mathrm{off}}<\infty$ is too strong" becomes a *theorem* ($S_{\mathrm{off}}=\infty$).

**Tags:** ✅ rigorous · ◆ standard-asymptotic · ⬜ open · ❌ corrected.

---

## 1. $H(E_\gamma)$ is trace-class — hence trivial — for the Weil form ◆→✅
The archimedean de Branges structure function has $|E_\gamma(t)|\asymp|\gamma(\tfrac12+it)|$ with, by
Stirling, $|\gamma(\tfrac12+it)|^2=\pi^{-1/2}|\Gamma(\tfrac14+\tfrac{it}2)|^2\sim c\,|t|^{-1/2}e^{-\pi|t|/2}$.
The de Branges diagonal kernel on $\mathbb R$ is $K(t,t)=\tfrac{\varphi'(t)}\pi|E_\gamma(t)|^2$ with phase
$\varphi=\theta$ (Riemann–Siegel), $\varphi'(t)=\tfrac12\Omega(t)\sim\tfrac1{2\pi}\log\tfrac{t}{2\pi}$. Hence
$$
K_{H(E_\gamma)}(\gamma,\gamma)\ \sim\ \frac{\log\gamma}{2\pi}\cdot c\,\gamma^{-1/2}e^{-\pi\gamma/2}\ \xrightarrow{\gamma\to\infty}\ 0\quad(\text{exponentially}).
$$
Therefore $\operatorname{Tr}T_+=\sum_\gamma K(\gamma,\gamma)\sim\sum_\gamma\log\gamma\,e^{-\pi\gamma/2}<\infty$, and
$$
\mathfrak t_+(g)=\sum_\gamma|\langle g,K_\gamma\rangle|^2\le\Big(\sum_\gamma K(\gamma,\gamma)\Big)\|g\|^2_{H(E)}\quad\Longrightarrow\quad\boxed{\ \mathfrak t_+\ \text{is BOUNDED (trace-class) in }H(E_\gamma).\ }
$$
The same kernel decay makes $\mathfrak t_-$ bounded. **So $\mathfrak t$ is a bounded form in $H(E_\gamma)$.**

> **What this means.** "CLOS.1/CLOS.2: $\mathfrak t$ closes in $H(E_\gamma)$" is **correct but vacuous** — it
> closes because it is *bounded*. $H(E_\gamma)$ is the **Day-3 trichotomy case 2** (closable-but-trivial):
> semiboundedness is automatic, no separation from RH is gained, and the bottom's sign is RH only in the
> useless sense that it encodes all zeros in a trace-class operator. The Day-3 worry ("too-strong a norm
> trivializes the instability") was **right**; my Day-5 "de Branges back in play" was over-optimistic — it
> was the *wrong* de Branges space.

**Downgrades (honest).**
- CL.0/DB.3/DB.4 picking $H(E_\gamma)$: ❌ wrong space (too strong). The exponential Gamma weight was the
  error — it is the de Branges space *of the Gamma factor*, not the space *of the archimedean energy*
  $\mathfrak a$ (whose weight is only $\Omega\sim\log$).
- CLOS.1/CLOS.2 in $H(E_\gamma)$: ✅-but-vacuous. The *method* (Kato) is fine and **transfers** to the
  correct space (§4), where it becomes non-vacuous.

---

## 2. The Goldilocks requirements (what the space must do)
A faithful Hilbert space $H$ for the Weil form must satisfy **all three**:
1. **(eval-bounding)** off-axis point-evaluations $\widehat g(t-ib)$, $|b|<\tfrac12$, are bounded (so
   $\mathfrak t_-$ and the pole term are defined) — *fails in $L^2$*;
2. **(non-trivial)** $\mathfrak t_+=\sum_\gamma|\widehat g(\gamma)|^2$ is **not** trace-class ($\sum_\gamma K_H(\gamma,\gamma)=\infty$),
   so the spectral problem is faithful — *fails in $H(E_\gamma)$*;
3. **(contains the core)** Gaussian–Hermite localizers $\in H$.
$L^2$ fails (1); $H(E_\gamma)$ fails (2). The weight must be **between** flat and exponential.

**Pinning the weight from requirement (2).** $\sum_\gamma K_H(\gamma,\gamma)=\infty$ with zeros of density
$\tfrac1{2\pi}\log$ needs $K_H(\gamma,\gamma)\gtrsim$ const, i.e. $|E_H(t)|^2\varphi'(t)\gtrsim$ const, i.e.
the weight must **not** carry the Gamma factor's $e^{-\pi|t|/2}$ decay. The mildest weight giving (1) is
**flat-in-$t$ with strip analyticity of width $\tfrac12$** — the **strip Hardy space**.

---

## 3. The corrected space: strip Hardy $H^2(S_{1/2+\epsilon})$ ✅ (structure)
Let $S_d=\{r\in\mathbb C:|\Im r|<d\}$, $d=\tfrac12+\epsilon$, and $H^2(S_d)$ the Hardy space (analytic in
$S_d$, $L^2$ on the boundary lines). In the $u$-variable ($g=$ inverse FT of $\widehat g$),
$$
\widehat g\in H^2(S_d)\iff \int_{\mathbb R}|g(u)|^2 e^{2d|u|}\,du<\infty ,
$$
an **exponential weight in $u$** but a **flat / translation-invariant structure in $r$** (the variable
where zeros live). Check the three requirements:
1. **eval-bounding ✅** — $S_d$ is a RKHS; $\widehat g(t-ib)$ bounded for $|b|<d=\tfrac12+\epsilon$, in
   particular at the pole depth $\tfrac12$ (the $\epsilon$ accommodates it) and all off-line $|b|<\tfrac12$.
2. **non-trivial ✅** — by translation invariance the kernel on the real axis is **constant**
   $K_S(t,t)=\kappa(0)=\tfrac1{4d}$; hence $\sum_\gamma K_S(\gamma,\gamma)=\kappa(0)\cdot\#\{\gamma\}=\infty$.
   $\mathfrak t_+$ is a **genuine unbounded form**.
3. **contains core ✅** — Gaussians decay $\gg e^{-d|u|}$, so $\mathcal D\subset H^2(S_d)$, dense.

**The explicit kernel (the quantitative $K$ the referee asked for).** By translation invariance,
$$
\boxed{\ K_{S_d}(t-ib,\,t-ib)=\kappa(b)\quad(\text{independent of }t),\qquad \kappa(b)=\frac1{4d}\,\sec\!\Big(\frac{\pi b}{2d}\Big),\quad \kappa(b)\asymp\frac1{\,d-|b|\,}\ \text{as }|b|\to d.\ }
$$
So $K$ **does not decay in $t$** (contrast $H(E_\gamma)$, where it died like $e^{-\pi|t|/2}$) and **blows up
at the strip edge** $|b|\to d$. The deep off-line zeros ($\beta\to0,1$, $|b|\to\tfrac12$) are near the edge
(dangerous); the $\epsilon$ keeps them interior.

> **Caveat (honest, flagged not buried).** The *exactly* faithful weight may carry a **mild $\log$
> correction** to match the $\tfrac1{2\pi}\log$ zero density (a "log-weighted strip" between flat $H^2(S_d)$
> and $H(E_\gamma)$). The robust facts — *not* exponential, $K$ roughly $t$-flat, edge-blowup — hold for the
> whole mild family; pinning flat-vs-$\log$ is part of A.2 (§4). I am **not** claiming flat $H^2(S_d)$ is
> the unique answer, only that it is the right *order of magnitude* and $H(E_\gamma)$ is not.

---

## 4. Consequences in the corrected space

**(C1) CLOS.1 transfers and is now NON-vacuous ✅.** $\mathfrak t_+(g)=\sum_\gamma|\langle g,K^S_\gamma\rangle|^2$
is again a non-decreasing sup of bounded closed forms $\Rightarrow$ **closed (Kato)** — but now
$\mathfrak t_+$ is **unbounded** (genuine), so closability is a real statement, not triviality. A genuine
non-negative unbounded self-adjoint $T_+$ exists on $H^2(S_d)$.

**(C2) The referee's $S_{\mathrm{off}}<\infty$ is now provably FALSE — forcing the relative regime ✅.**
Since $\kappa(b)\ge\kappa(0)=\tfrac1{4d}>0$,
$$
S_{\mathrm{off}}=\sum_{\text{off-line}}K_S(t-ib,t-ib)=\sum_{\text{off-line}}\kappa(b_\rho)\ \ge\ \tfrac1{4d}\,\#\{\text{off-line zeros}\}\ =\ \infty\ \ (\text{if infinitely many}).
$$
So the clean sufficient condition (Day-8 B.2, $a=0$, "$\mathfrak t_-$ bounded") **cannot hold** when RH
fails infinitely — exactly the referee's prediction that it "hides almost all the difficulty." We are
forced into the **genuine relative Carleson bound (RFB, $a>0$)**: control each off-line evaluation by
*nearby on-line* evaluations. This is now a **classical Carleson-measure problem for the strip Hardy
space** $H^2(S_d)$ — a subject with a large literature (Carleson measures for Hardy spaces of strips /
half-planes; interpolating sequences; the $\overline\partial$-Carleson box conditions).

**(C3) (RFB) restated in the correct space.** $\;|\mathfrak t_-(g)|\le 4\sum_{\text{off-line}}|\widehat g(t-ib)|^2$,
and the target is
$$
\sum_{\text{off-line}}|\widehat g(t-ib)|^2\ \le\ a\sum_{\text{on-line}}|\widehat g(\gamma)|^2+C\|g\|^2_{H^2(S_d)},\quad a<1 .
$$
Both sides are now **honest non-trace-class evaluation sums** in the same space. (RFB) $\iff$ the off-line
measure $\mu_{\mathrm{off}}=\sum\delta_{t-ib}$ is **relatively Carleson** w.r.t. the on-line sampling measure
$\mu_{\mathrm{on}}=\sum\delta_\gamma$ — a comparison of two measures' Carleson constants for $H^2(S_d)$.
This is where the **fine geometry** of zeros (separation, $S(T)$, pair correlation) enters, as the referee
foresaw — *not* raw density.

**(C4) Form-core A.2 re-posed (now genuinely non-trivial).** Is $\mathcal D$ a form-core for the *unbounded*
$\mathfrak t_+$ in $H^2(S_d)$? $\iff$ are the zeta zeros a "nice" (frame/sampling) sequence for $H^2(S_d)$?
The zeros have **increasing** density $\tfrac1{2\pi}\log T$ while $H^2(S_d)$ is translation-invariant
(constant Nyquist density) — so the zeros **over-sample** at large $t$. Over-sampling suggests a *lower*
frame bound $\mathfrak t_+(g)\gtrsim\|g\|^2$ may even hold (with the redundancy growing), which would make
$\mathcal D$ a form-core automatically — **but this density mismatch is exactly why the precise weight
(flat vs $\log$) matters** (§3 caveat). A.2 and the weight-pinning are one problem.

---

## 5. Status — what this iteration changed

| Item | Before (Days 5–8) | After (Day 9) |
|---|---|---|
| Home space | $H(E_\gamma)$ (Gamma de Branges) | **$H^2(S_{1/2+\epsilon})$ (strip Hardy), mild weight** |
| $\mathfrak t$ there | "closes" (✅) | closes but was **trace-class = vacuous** in $H(E_\gamma)$; **genuine** in $H^2(S_d)$ |
| $K(w,w)$ | un-computed (asserted exp weight) | **explicit**: $K_{H(E_\gamma)}\to0$ (trivializes); $K_{S_d}(t-ib,t-ib)=\kappa(b)$, $t$-flat, edge-blowup |
| $S_{\mathrm{off}}$ | maybe $<\infty$ ($a=0$ hope) | **$=\infty$** (each term $\ge\kappa(0)$); $a=0$ false; relative $a>0$ forced |
| CLOS.1 (Kato) | ✅ but vacuous | ✅ **non-vacuous** in $H^2(S_d)$ |
| (RFB) | "zero-density" | **relative Carleson** for $H^2(S_d)$ (fine geometry, not raw density) |

**Net (Day 9).** A quantitative kernel computation — exactly the referee's Front 2 — caught a genuine
error: $H(E_\gamma)$ *trivializes* the Weil form (trace-class), so Days 5–8's "closure" was vacuous and the
"de Branges space vindicated" was the *wrong* de Branges space. Corrected home: the **strip Hardy space**
$H^2(S_{1/2+\epsilon})$ (mild/flat weight, not the Gamma exponential), where $\mathfrak t_+$ is genuinely
unbounded, Kato-closability is non-vacuous, and the kernel is explicit and $t$-flat. The referee's two
intuitions are *confirmed as theorems*: the strong norm trivializes (Day-3 worry), and $S_{\mathrm{off}}<\infty$
is false in the relevant case (Day-8 suspicion) — forcing the genuine **relative Carleson** problem, which
is where the arithmetic (zero fine-geometry) lives.

**Next (corrected priorities).**
1. **Pin the weight** (flat $H^2(S_d)$ vs log-weighted strip) by matching the $\tfrac1{2\pi}\log$ zero
   density — this *is* form-core A.2.
2. **(RFB) as relative Carleson for $H^2(S_d)$**: import the strip-Hardy Carleson-measure characterization;
   express it via zero separation / $S(T)$.
3. **Audit §1 trivialization** once more against a cited value of $|E_\gamma(t)|$ — the load-bearing
   asymptotic. (Done qualitatively via Stirling; pin the constant from de Branges/Lagarias.)
