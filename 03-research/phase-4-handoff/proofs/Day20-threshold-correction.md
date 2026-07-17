# Day 20 — The threshold push has a vacuous step; the corrected local analysis points to UNCONDITIONAL B-2

The referee pushed to a concrete threshold: $|E_g|\le C_d\frac{\sqrt{V(d,T)}}{P}\mathfrak t_+$, computed
$V_{\mathrm{diag}}\sim T\log T$, concluded the diagonal alone fails and a strong off-diagonal (Montgomery)
cancellation is needed ($V\ll(\log T)^2$). **Verification (very careful — "muy serio"): the global
Cauchy–Schwarz step is VACUOUS**, so that threshold is an *artifact*, not the real requirement. The
**corrected local analysis** shows B-2 needs only $E_g=O(\mathfrak t_+)$ (finite constant), which holds
**unconditionally** (Selberg + zero-density), with **Montgomery not needed**. So the likely status is
*better* than an RH-reformulation: **plausibly an unconditional B-2**. **This Day-20 claim now itself needs
the hard audit.** **Tags:** ✅ rigorous (the error) · ◆ strong-but-to-audit · ⬜.

---

## 1. The error: the global $\sqrt{V(d,T)}$ Cauchy–Schwarz is vacuous ❌
The referee's chain $|E_g|\le\frac1{2\pi}\|\widehat g\|_2\sqrt{V(d,T)}$ uses the **global** discrepancy
$D_T(\alpha)=\sum_{\gamma\le T}e^{i\alpha\gamma}-\int_0^T e^{i\alpha t}\rho$ — *all* zeros from height $0$ to
$T$. For a localizer $F$ centered at height $T_0$ ($\|F\|_2=1$), $\|\widehat g\|_2=\sqrt{2\pi}\|F\|_4^2=O(1)$
(Nikolskii), while $V_{\mathrm{diag}}=4dN(T)\sim\frac{2d}{\pi}T\log T$, so
$$
|E_g|\le O(1)\cdot\sqrt{T\log T},\qquad \mathfrak t_+\sim\rho\sim\log T_0,\qquad \frac{|E_g|}{\mathfrak t_+}\lesssim\frac{\sqrt{T_0\log T_0}}{\log T_0}=\sqrt{\tfrac{T_0}{\log T_0}}\to\infty .
$$
**The bound gives $|E_g|\le\infty\cdot\mathfrak t_+$ — vacuous.** Cause: the localizer's phase $e^{i\alpha T_0}$
correlates with only a sliver of $D_T$; Cauchy–Schwarz against the *whole* $D_T$ throws the localization
away. **So "$V(d,T)$ global" is the wrong object, and the demand "$V\ll(\log T)^2$ / Montgomery off-diagonal
cancellation" is an artifact of this lossy step — not the real requirement.**

---

## 2. The right object is local; B-2 needs $O(\mathfrak t_+)$, not $o(\mathfrak t_+)$ ✅
$E_g=\sum_\gamma|F(\gamma)|^2-\int|F|^2\rho=\int|F|^2\,dS$ (with $S=N-\bar N$). Integrate by parts and use
**Bernstein** ($\int|(|F|^2)'|\le2\|F'\|_2\|F\|_2\le2d\|F\|_2^2$ for $F\in PW_d$) and the **unconditional**
$S=O(\log)$:
$$
|E_g|=\Big|\int (|F|^2)'\,S\Big|\le \big(\sup_{\mathrm{loc}}|S|\big)\!\int|(|F|^2)'|\ \le\ 2d\,(\log T_0)\,\|F\|_2^2\ =\ O(\mathfrak t_+),
$$
since $\mathfrak t_+\asymp\rho\|F\|_2^2\sim\tfrac{\log T_0}{2\pi}\|F\|_2^2$ (over-sampling main term). **The $\log T_0$
from $S$ cancels the $\rho\sim\log T_0$ in $\mathfrak t_+$** — a finite ratio $O(d)$, **unconditional**.

**Crucial point both Day 18 and the referee missed:** B-2 (semiboundedness, finite bottom) requires only
$E_g=O(\mathfrak t_+)$ (**finite** constant), **not** $o(\mathfrak t_+)$ (sharp equidistribution). The
"$S=O(\log)$ insufficient" of Day 18 was about getting $o(1)$ — which we do **not** need. The finite
constant suffices, and it is unconditional.

---

## 3. The off-line part: $\kappa(b)\le e^d$ uniformly + zero-density ⟹ finite constant ◆
In the band-limited class $PW_d$ ($d>\tfrac12$): every off-line zero has $|b|=|\beta-\tfrac12|<\tfrac12<d$, so
the vertical amplification is **uniformly bounded**, $\kappa(b)=e^{2d|b|}<e^{d}$ — **no deep-zero blowup**
(the Days 9–15 strip-edge danger is removed by band-limiting). By the quadrature (both sums $\asymp$
density$\times$integral),
$$
\widetilde{\mathfrak t}_-=\sum_{\mathrm{off}}|F(\gamma+ib)|^2\ \asymp\ \rho_{\mathrm{off}}\!\int|F(\cdot+ib)|^2\ \le\ e^{d}\,\frac{\rho_{\mathrm{off}}}{\rho}\,\mathfrak t_+ + O(\mathfrak t_+)\ \le\ C\,\mathfrak t_+,
$$
$C$ **finite** (since $\rho_{\mathrm{off}}\le\rho$ by **classical, unconditional** zero-density). Hence in
$H_+\cong\ell^2(\{\gamma\})$:
$$
\boxed{\ \mathfrak t\ \ge\ (1-4C)\,\|\cdot\|^2_{H_+}\quad(\text{finite bottom})\ \Longrightarrow\ \text{B-2 — plausibly UNCONDITIONAL.}\ }
$$
RH remains the **sign** of the bottom (CL.2), unproven.

---

## 4. Answer to "reformulation of RH, or what?"
**Probably better than a reformulation.** The referee's bet (60% RH-reformulation via Montgomery) rested on
the **vacuous** global bound. With the corrected local bound:
- B-2's real requirement is $E_g=O(\mathfrak t_+)$ (finite), met **unconditionally** by **Selberg
  ($S=O(\log)$) + Bernstein + classical zero-density** — **Montgomery pair correlation is NOT needed.**
- So the likely outcome is the **§6 prize**: an **unconditional, faithful, semibounded realization of the
  Weil operator** (B-2), RH-independent — *not* a mere RH-equivalence.
- **RH itself is untouched** (it is the sign of the now-finite bottom). So this would prove B (the
  realization) unconditionally, leaving RH = the sign — exactly the program's stated, RH-independent goal.

**Revised scenario probabilities (my estimate, vs the referee's):**
| outcome | referee | Day-20 corrected |
|---|---|---|
| RH-reformulation (Montgomery needed) | 60% | ~20% |
| **unconditional B-2 (the §6 prize)** | 30% | **~60%** (the local bound looks unconditional) |
| new explicit-formula identity / surprise | 10% | ~20% |

---

## 5. MANDATORY next step: audit *this* (Day 20) before believing it
Per the 20-day discipline — every pillar gets the hostile audit, *especially* an optimistic one. The points
**I** would attack in Day-20:
1. **IBP boundary/tail terms.** $F\in PW_d$ has **non-compact** support (decays $\sim1/t$). Verify
   $[|F|^2 S]_{\pm\infty}\to0$ and the tail $\int_{|t-T_0|>R}|(|F|^2)'||S|$ is genuinely lower order — *not*
   hand-waved.
2. **The off-line quadrature, exactly.** $\widetilde{\mathfrak t}_-=\sum_{\mathrm{off}}|F(\gamma_\rho+ib_\rho)|^2$
   samples at the off-line ordinates with *varying* $b_\rho$; the single-$b$ quadrature is a simplification.
   Redo with the 2D off-line measure and confirm $\rho_{\mathrm{off}}\le\rho$ + zero-density really gives the
   finite constant (and that off-line discrepancy $E_-$ is $O(\mathfrak t_+)$, not larger).
3. **Is the constant $C$ useful?** $C\sim e^d>1$ gives a finite but possibly very negative bottom $1-4C$.
   Finite is enough for B-2 *as semiboundedness*; but check nothing downstream (the sign$=$RH statement)
   secretly needs $C<1$.
4. **Coercivity $\mathfrak t_+\gtrsim\|\cdot\|^2$** (so $H_+$ is a genuine space, $\mathcal T_+$ invertible) —
   re-confirm unconditional for the over-dense zeros in $PW_d$.

**Net (Day 20).** The referee's threshold push contained a **vacuous global Cauchy–Schwarz**; correcting it
to the local IBP+Bernstein+Selberg bound shows B-2 needs only a **finite-constant** quadrature comparison,
which is **unconditional** (no Montgomery). So the program likely lands on **unconditional B-2** (a faithful
semibounded Weil realization, RH-independent — the §6 prize), *not* an RH-reformulation. **But this is now
the load-bearing optimistic claim and must survive its own hostile audit (§5) before being written as a
theorem.** Next: execute that audit, points 1–4.
