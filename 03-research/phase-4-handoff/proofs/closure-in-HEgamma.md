# Closure of the Weil form in $H(E_\gamma)$ — the first positive result (Day 7)

**The question (referee's priority).** Does the Weil form $\mathfrak t$, defined on the dense core
$\mathcal D$, **close** in $H(E_\gamma)$? A closability obstruction here would suspend everything
downstream; conversely, "$\mathfrak t_{\mathcal D}$ is closable in $H(E_\gamma)$" is the first Phase-4
result that genuinely changes the mathematical state — it turns the program into the study of a concrete
*closed* form with a legitimate self-adjoint operator.

This file answers it. **Verdict:** closability **holds unconditionally in the RH-true world** (CLOS.2),
via a classical theorem (CLOS.1); in the RH-false world it, *and* semiboundedness, both reduce to **one**
clean KLMN inequality (CLOS.3) — which is a zero-density comparison of off-line vs on-line zeros, in the
correct geometry. **Tags:** ✅ rigorous/classical · ⬜ open.

Built on the audited identity (`EF-identity-audit.md`):
$$
\mathfrak t(g,g)=\underbrace{\sum_{\text{on-line}}|\widehat g(\gamma)|^2}_{\mathfrak t_+\ \ge0}\ +\ \underbrace{\sum_{\text{off-line quartets}}4\,\mathrm{Re}[\widehat g(t-ib)^2]}_{\mathfrak t_-\ \text{indefinite}},\qquad g\in\mathcal D .
$$

---

## CLOS.1 — the on-line part $\mathfrak t_+$ is closed (Kato monotone convergence) ✅
In $H(E_\gamma)$ point evaluations are bounded: $\widehat g(\gamma)=\langle g,K_\gamma\rangle_{H(E)}$ with
$K_\gamma$ the reproducing kernel (DB.3). So
$$
\mathfrak t_+(g)=\sum_{\gamma}\big|\langle g,K_\gamma\rangle_{H(E)}\big|^2=\lim_{N\uparrow\infty}\ \mathfrak t_+^{(N)}(g),\qquad
\mathfrak t_+^{(N)}(g):=\sum_{|\gamma|\le N}|\langle g,K_\gamma\rangle|^2 .
$$
Each $\mathfrak t_+^{(N)}$ is a **finite** sum of bounded non-negative rank-one forms — hence bounded,
everywhere-defined, and **closed**. The sequence is **non-decreasing** in $N$. By **Kato's monotone
convergence theorem for forms** (Kato, *Perturbation Theory*, Thm VIII.3.13a; Simon), the supremum
$$
\mathfrak t_+=\sup_N\mathfrak t_+^{(N)}\quad\text{is a CLOSED non-negative form}
$$
on its natural domain $D(\mathfrak t_+)=\{g\in H(E_\gamma):\sum_\gamma|\widehat g(\gamma)|^2<\infty\}$. Since
$\mathcal D\subseteq D(\mathfrak t_+)$ (Gaussian decay of $\widehat g$ beats the $\tfrac1{2\pi}\log$ density
of zeros), $\mathfrak t_+|_{\mathcal D}$ is **closable** (the closed $\mathfrak t_+$ is a closed extension).
✅ *No arithmetic input; pure form theory + DB.3.*

> ⚠️ **CORRECTION (Day 8 audit).** An earlier version claimed "closure $=\mathfrak t_+$ because $\mathcal D$
> is dense." That is **wrong**: density in $H(E_\gamma)$ is **not** form-core-ness. What is rigorous is
> only that $\mathfrak t_+|_{\mathcal D}$ is **closable** (so a non-negative s.a. operator
> $\overline{T_+}$ exists). Whether $\overline{\mathfrak t_+|_{\mathcal D}}=\mathfrak t_+$ — i.e. whether
> $\mathcal D$ is a **form-core** ($\overline{\mathcal D}^{\,\|\cdot\|_{\mathfrak t_+}}=D(\mathfrak t_+)$,
> $\|g\|^2_{\mathfrak t_+}=\|g\|^2_{H(E)}+\mathfrak t_+(g)$) — is **OPEN**. If it fails, the operator from
> the core is a *proper restriction* of the maximal $T_+$ and its spectrum may differ. See
> `CLOS1-audit-and-RFB.md` Part A. **Existence of a legitimate closed form/operator from the core survives;
> identification with the maximal/zero-indexed $T_+$ does not (yet).**

> **What CLOS.1 delivers.** A bona-fide **non-negative self-adjoint operator $T_+\ge0$ on $H(E_\gamma)$**
> whose form is $\mathfrak t_+$ — the "on-line Weil operator" — exists **unconditionally**. This is B-1
> made concrete in the right space, *plus* the positive half of B-2, with no hypotheses.

---

## CLOS.2 — under RH, the full form is closable (unconditional in the control world) ✅
If RH holds (in particular for every GRH control the program uses — $\zeta$, $L(\chi_4)$, $L(\Delta)$),
there are **no off-line zeros**, so $\mathfrak t_-=0$ and $\mathfrak t=\mathfrak t_+$. By CLOS.1,
$$
\boxed{\ \text{RH}\ \Longrightarrow\ \mathfrak t\ \text{is closed/closable in }H(E_\gamma),\ \text{with }\inf\operatorname{spec}=\inf\mathfrak t_+/\|\cdot\|^2\ \ge0.\ }
$$
So in the world the numerics actually live in, the Weil form **has a legitimate self-adjoint, bounded-below
(by $0$) realization in $H(E_\gamma)$.** The de Branges geometry is *vindicated* as the correct home — the
Day-1 $L^2$ pathology is gone (DB.3) and the form closes (Kato). The chain/Fock detours were unnecessary.

---

## CLOS.3 — the RH-false residual: closability + semiboundedness from ONE inequality ⬜
The only nontrivial case is RH-false (off-line zeros present). There $\mathfrak t=\mathfrak t_++\mathfrak t_-$,
and **both** closability **and** semiboundedness follow at once from a single relative-form-bound:
$$
\boxed{\ \exists\,a<1,\ C:\qquad |\mathfrak t_-(g)|\ \le\ a\,\mathfrak t_+(g)\ +\ C\|g\|^2_{H(E)}\quad\text{on }\mathcal D.\ }\tag{RFB}
$$
- **(RFB) $\Rightarrow$ closable:** KLMN — $\mathfrak t_-$ is $\mathfrak t_+$-form-bounded with bound $<1$, so
  $\mathfrak t_++\mathfrak t_-$ is closed (Kato/KLMN).
- **(RFB) $\Rightarrow$ semibounded:** $\mathfrak t=\mathfrak t_++\mathfrak t_-\ge(1-a)\mathfrak t_+-C\|g\|^2\ge-C\|g\|^2$
  (since $\mathfrak t_+\ge0$). **B-2 settled in one stroke.**

So **(RFB) is the single remaining analytic target of Problem B.** Note its content:
$$
\mathfrak t_-(g)=\sum_{\text{off-line}}4\,\mathrm{Re}[\widehat g(t-ib)^2],\qquad \mathfrak t_+(g)=\sum_{\text{on-line}}|\widehat g(\gamma)|^2 .
$$
(RFB) is literally **"the off-line-zero contribution is controlled by the on-line-zero contribution"** —
a **zero-density comparison**. Each off-line term is a *bounded* $H(E_\gamma)$-evaluation (DB.3), so the
sum's size is governed by **how many off-line zeros there are and how close to the line** — i.e. a
zero-density / zero-free-region input. This **re-derives §3.3's "B-2 lives at the zero-density tier"
from an independent route** (relative form-boundedness, not the retracted prime argument). Two independent
derivations now agree.

**Why this KLMN can succeed where Day-0's failed.** The Day-0 KLMN (B2.3) tried to bound the *prime* form
by the *archimedean* form in $L^2$ and failed (and the failure argument was itself a truncation artifact,
retracted Day 5). (RFB) is a different inequality entirely: it bounds the *off-line-zero* form by the
*on-line-zero* form, **in $H(E_\gamma)$ where both are sums of bounded evaluations**. The geometry now
*helps* (DB.3 makes every term finite); the only question is summing them.

---

## Status and the sharpened map of Problem B

| Step | Statement | Status |
|---|---|---|
| B-1 | self-adjoint realization exists (von Neumann conjugation) | ✅ unconditional |
| CLOS.1 | $\mathfrak t_+$ closed; $T_+\ge0$ exists on $H(E_\gamma)$ | ✅ (Kato + DB.3) |
| CLOS.2 | RH $\Rightarrow$ $\mathfrak t$ closable, $\inf\operatorname{spec}\ge0$ | ✅ unconditional in RH-world |
| CLOS.3 = (RFB) | $|\mathfrak t_-|\le a\,\mathfrak t_++C\|\cdot\|^2$, $a<1$ $\Rightarrow$ closable **and** semibounded | ⬜ **the single open target** |
| (RFB) content | a zero-density comparison of off-line vs on-line zeros | = §3.3, re-derived |

**Net (Day 7).** The closure question — the referee's priority, and the place history says surprises hide
— came back **positive**: $\mathfrak t_+$ is closed by a named classical theorem, and under RH the full
form closes unconditionally. So $H(E_\gamma)$ is a *legitimate* home and the program now studies a
concrete closed form with a real self-adjoint operator $T_+$. The entire remaining difficulty of Problem B
has funnelled into the **single inequality (RFB)** — a KLMN-shaped, zero-density comparison of off-line to
on-line zero contributions, posed in the geometry where every term is finite. This is the first Phase-4
result that changes the mathematical state, exactly as the referee predicted closability would.

**Next.**
1. **Attack (RFB)** as a zero-density statement: bound $\sum_{\text{off-line}}|\widehat g(t-ib)^2|$ by
   $a\sum_{\text{on-line}}|\widehat g(\gamma)|^2 + C\|g\|^2$ using a zero-free-region / density hypothesis;
   find the weakest density input giving $a<1$.
2. **Cross-check with Bombieri** *Remarks on Weil's quadratic functional* — his semiboundedness analysis
   should be (RFB) in his normalization.
3. **Audit CLOS.1's use of Kato** (verify the monotone-convergence hypotheses against our exact forms) and
   confirm $\mathcal D$ is a form-core — the new load-bearing step, per the project's audit discipline.
