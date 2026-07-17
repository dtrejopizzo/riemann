# Day 11 — Audit of the Day-10 theorem (the new pillar), and its density-adapted reconstruction

The Day-10 "space-independent theorem" (faithful $\Rightarrow S_{\mathrm{off}}=\infty$) became the new
logical bottleneck, so it gets the same hard audit as the kernel formula. **Two gaps found** — one in F2
(the referee's catch), one in F1 (found here). The theorem is **not** space-independent; it holds for
**translation-invariant / reflection-symmetric faithful spaces** (the candidate class) and reconstructs in
a **density-adapted** form covering the log-weighted candidates. Net: an honest **impossibility result with
explicit hypotheses**, not a universal claim.

**Tags:** ✅ rigorous · ◆ conditional · ❌ retracted-overclaim · ⬜ open.

---

## 1. Gap in F2 (the referee's catch) — CONCEDED ❌
Day-10 claimed: $\mathfrak t_+$ non-trace-class ($\sum_\gamma K(\gamma,\gamma)=\infty$, "faithful")
$\Rightarrow \inf_t K(t,t)=:c>0$. **False.** Counterexample (referee): $K(t,t)\sim\tfrac1{\log t}$. With
zeros $\gamma_n\sim\tfrac{2\pi n}{\log n}$ ($\log\gamma_n\sim\log n$),
$$
\sum_\gamma K(\gamma,\gamma)\sim\sum_n\frac1{\log\gamma_n}\sim\sum_n\frac1{\log n}=\infty\ \ (\text{faithful}),\qquad\text{yet}\quad\inf_t K(t,t)=0 .
$$
(In fact faithfulness is very weak: $K(t,t)\gtrsim t^{-1}$ suffices, since $\sum_n\gamma_n^{-\epsilon}$
converges only for $\epsilon>1$.) So the only solid one-liner is
$$
\boxed{\ \inf_t K(t,t)>0\ \Longrightarrow\ S_{\mathrm{off}}=\infty\ }\qquad(\text{not "faithful}\Rightarrow\text{"}).
$$

---

## 2. Gap in F1 — found in audit, also conditional ◆
F1 was "$K(t-ib,t-ib)\ge K(t,t)$." Audit via the real-entire ON basis $\{e_n\}$ ($e_n$ real on $\mathbb R$,
so $\overline{e_n(t-ib)}=e_n(t+ib)$):
$$
|e_n(t-ib)|^2=e_n(t-ib)e_n(t+ib)=e_n(t)^2+b^2\big(e_n'(t)^2-e_n(t)e_n''(t)\big)+O(b^4),
$$
$$
K(t-ib,t-ib)=K(t,t)+b^2\,D(t)+O(b^4),\qquad D(t):=\sum_n\big(e_n'(t)^2-e_n(t)e_n''(t)\big).
$$
**$D(t)$ need not be $\ge0$.** A single basis function with $e'(t)=0$, $e''(t)>0$ gives $D=-e(t)e''(t)<0$,
so $|e(t-ib)|^2<|e(t)|^2$: the off-axis evaluation is *smaller*. **So F1 is not universal** — it depends on
the space's fine structure.

**Where F1 *does* hold (rigorously):** **translation-invariant** spaces. There $K(t-ib,t-ib)=\kappa(b)$,
and $\kappa$ is **convex** ($\kappa''\ge0$ from subharmonicity of $w\mapsto K(w,w)=\sum_n|e_n(w)|^2$,
$\Delta K=4\sum_n|e_n'|^2\ge0$, no $t$-dependence $\Rightarrow\partial_b^2\kappa\ge0$) and **even**
($\kappa(-b)=\kappa(b)$ by reflection), hence minimized at $b=0$: $\kappa(b)\ge\kappa(0)$. ✅ (For flat
strip Hardy, explicitly $\kappa(b)=\tfrac1{4d}\sec\tfrac{\pi b}{2d}$, increasing.) So F1 ✅ for the
translation-invariant candidate; ◆ (needs $D(t)\ge0$) in general.

---

## 3. The reconstructed theorem (density-adapted, covers the candidates) ✅/◆

**Theorem (Day 11).** Let $H$ be an RKHS of strip-analytic functions with bounded off-axis evaluations,
real-entire ON basis, and suppose:
- **(i) density-adapted faithfulness:** $K(t,t)\ge \dfrac{c}{\log(2+|t|)}$ for some $c>0$;
- **(ii) F1:** $K(t-ib,t-ib)\ge K(t,t)$ (e.g. $H$ translation-invariant, §2);
- **(iii) off-line zeros not super-sparse:** $\sum_{\text{off-line }\rho}\dfrac1{\log(2+t_\rho)}=\infty$
  (holds whenever they are a positive proportion, density $\asymp\log T$).

Then
$$
S_{\mathrm{off}}=\sum_{\text{off-line}}K(t_\rho-ib_\rho,t_\rho-ib_\rho)\ \overset{(ii)}{\ge}\ \sum_{\text{off-line}}K(t_\rho,t_\rho)\ \overset{(i)}{\ge}\ c\sum_{\text{off-line}}\frac1{\log(2+t_\rho)}\ \overset{(iii)}{=}\ \infty .
$$
Hence **$a=0$ ($\mathfrak t_-$ bounded) is impossible** and the relative Carleson ($a>0$) bound is forced.

**Checks on the hypotheses:**
- (i) holds for **flat strip Hardy** ($K=\kappa(0)=$const$\ge c/\log$ ✓) and **log-weighted strip**
  ($K\sim1/\log$ ✓ borderline) — both candidate faithful spaces. *(i) is a mild extra regularity beyond
  bare faithfulness; it is exactly the referee's $K\gtrsim1/\log$ threshold.*
- (ii) ✅ for translation-invariant; ◆ for log-weighted (a mild perturbation — to verify $D(t)\ge0$ there).
- (iii) is the honest restriction: a *genuine* RH violation (positive proportion off-line) gives it; a
  super-sparse off-line set is a near-RH world where the question is nearly moot.

---

## 4. The meta-frame: structural constraints / impossibility (the referee's point) ✅
The durable output of Days 9–11 is **not** a space, but a growing list of **constraints any faithful RKHS
realization of the Weil form must satisfy** — impossibility results, which survive model changes better
than positive constructions:

| # | Constraint (what CANNOT happen) | Status |
|---|---|---|
| K1 | **trivializing $\perp$ faithful**: if $\sum_\gamma K(\gamma,\gamma)<\infty$ the space is vacuous (Day 9) | ✅ |
| K2 | **faithful $\perp$ $a=0$** (under F1 + off-line positive proportion): can't have both a genuine form and the easy bound (Day 10–11) | ◆ (hypotheses explicit) |
| K3 | **Gamma–de-Branges family excluded**: $E\sim\gamma$ trivializes, $E\sim1/\gamma$ eval-uncontrolled (Day 10) | ◆ |
| K4 | **strong-norm $\perp$ non-trivial**: too-strong weight ⟹ trace-class ⟹ trivial (Day 3 worry, Day 9 proof) | ✅ |

$$
\boxed{\ \text{The faithful space lives in a narrow window, and inside it the relative-Carleson difficulty is unavoidable.}\ }
$$

---

## 5. Status — what the audit changed

| Claim | Day 10 | Day 11 (audited) |
|---|---|---|
| faithful $\Rightarrow\inf K>0$ | used | ❌ **false** ($1/\log$ counterexample) |
| solid implication | "faithful $\Rightarrow S_{\mathrm{off}}=\infty$" | ✅ only **$\inf K>0\Rightarrow S_{\mathrm{off}}=\infty$** |
| F1 $K(t-ib,..)\ge K(t,t)$ | asserted general | ◆ **only translation-invariant/symmetric** ($D(t)\ge0$ can fail) |
| space-independence | claimed | ❌ **depends on structure**; clean for the candidate class |
| reconstructed thm | — | ✅/◆ density-adapted (i)+(ii)+(iii) $\Rightarrow S_{\mathrm{off}}=\infty$ |
| impossibility frame | implicit | ✅ explicit constraint list K1–K4 |

**Net (Day 11).** The referee was right to demand a hard audit of the new pillar: **both** F1 and F2 had
gaps, so the Day-10 "space-independent theorem" is downgraded to a **density-adapted impossibility result
with explicit hypotheses (i)–(iii)** — which still covers the candidate Hardy-band spaces and still forces
the relative-Carleson difficulty. The genuine, durable gain is the **constraint list K1–K4**: a faithful
realization must thread a narrow window, and inside it the arithmetic (relative Carleson) cannot be dodged.
**Next:** (1) verify (ii)/$D(t)\ge0$ for the log-weighted strip; (2) the over-sampling lower-frame-bound
(form-core A.2), now the natural next positive step; (3) literature pin of the weight (Bombieri/Lagarias).
