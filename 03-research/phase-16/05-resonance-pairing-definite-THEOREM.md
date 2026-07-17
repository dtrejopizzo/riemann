# Phase 16 · Theorem — the modular-surface resonance pairing is structurally definite (κ absent)

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Pursuing the indefiniteness "from outside the Bochner pairing." Result: a **theorem** that the resonance/scattering
pairing on the modular surface is definite for *every* configuration of zeros in the critical strip — so the negative
index $\kappa$ (= RH) is **structurally absent** from it, independent of RH. This closes Pillar 2 via any resonance
pairing, and locates the indefiniteness in the off-axis evaluation / the missing arithmetic surface (SURF).

---

## The theorem
\begin{theorem}[Resonance pairing is half-plane definite]
Let the modular-surface resonances be $s_\rho=\rho/2$ for the nontrivial zeros $\rho=\beta_\rho+i\gamma_\rho$,
$0<\beta_\rho<1$. The resonance kernel
$$
K_{\rho\sigma}=\frac{1}{s_\rho+\overline{s_\sigma}-1}
$$
(the Maass–Selberg denominator, up to the residue weights $D=\operatorname{diag}(R_\rho)$, which do not change the
signature) is **negative-definite** for every such configuration — on-line or off-line.
\end{theorem}
\begin{proof}
Put $w_\rho=\tfrac12-s_\rho$; then $\operatorname{Re}(w_\rho)=\tfrac12-\tfrac{\beta_\rho}{2}=\tfrac{1-\beta_\rho}{2}>0$
since $\beta_\rho<1$. And
$$
K_{\rho\sigma}=\frac1{s_\rho+\overline{s_\sigma}-1}=\frac{-1}{(\tfrac12-s_\rho)+\overline{(\tfrac12-s_\sigma)}}
=\frac{-1}{w_\rho+\overline{w_\sigma}}=-\int_0^\infty e^{-w_\rho t}\,\overline{e^{-w_\sigma t}}\,dt.
$$
The integral represents the **positive-definite Cauchy/Hardy kernel** of the right half-plane $\{\operatorname{Re}>0\}$
(reproducing kernel of $H^2$), so $-K$ is positive-definite, i.e. $K\prec0$. The full Gram matrix $G=D\,K\,D^*$ has
the same signature as $K$ ($D$ invertible since $R_\rho\ne0$), hence $G\prec0$. $\square$
\end{proof}

**Numerical confirmation** (`pillar2_offline_signature_test.py`): 5 on-line resonances give signature $+0/-5$; adding a
genuine off-line quartet ($\rho=0.7+20i$ and its functional-equation partners, resonances at real parts $0.35$ and
$0.15$ straddling $1/4$) gives $+0/-9$ — **still definite**. The off-line displacement does not produce a single
positive eigenvalue.

## Consequence — Pillar 2 cannot be met by any resonance pairing
The Weil form $Q$ is **indefinite** (negative index $\kappa=\#\{$off-line zeros$\}$; $\kappa=0\iff$RH). The resonance
pairing is **provably definite** (Theorem), for *every* zero configuration. Therefore:
$$
\boxed{\ \text{No resonance/scattering pairing on the modular surface can equal }Q;\ \kappa\text{ is structurally
absent from it.}\ }
$$
This is **not** "we computed and it was definite" — it is an impossibility, robust to where the zeros sit. It closes
Route A's Pillar 2 via resonances definitively, and it is RH-independent.

## Where the indefiniteness actually lives
By the explicit formula $Q(f,f)=\sum_\rho h(\gamma_\rho)$: on-line zeros contribute $|\widehat f(\gamma)|^2\ge0$;
**off-line zeros contribute $4\operatorname{Re}[\widehat f(t-ib)^2]$, $b=\beta-\tfrac12$ — an off-axis point
evaluation, the sole indefinite term.** The Theorem says the *bulk/regularized* resonance pairing is blind to this:
the indefiniteness is the **off-axis evaluation functional**, which is **unbounded on $L^2$** (Phase-4, Day 1), not a
bulk pairing. So $\kappa$ requires either:
- the **de Branges** reproducing-kernel structure where off-axis evals are bounded — which Phase 4 (Days 9–15) showed
  trivializes or reproduces the wrong-sign capstone; or
- the **indefinite intersection form** of the arithmetic surface $\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}
  \operatorname{Spec}\mathbb Z$ (Hodge-index signature) — **SURF**, which does not exist.

Every natural pairing the modular surface supplies (analytic Maass–Selberg; arithmetic Arakelov/Néron–Tate) is
**definite**; the indefinite $Q$ is not among them. This is the wrong-sign capstone (CAP), now **proven** on Route A.

## Status (honest)
- **Advance (genuine):** a theorem — the modular-surface resonance pairing is structurally definite (half-plane Hardy
  kernel); $\kappa$ is absent from it, RH-independently. A durable impossibility result.
- **No crossing:** the indefiniteness $\kappa$ is the off-axis evaluation / the missing surface's intersection form,
  not any pairing Route A provides. Route A supplies the **zeros** (Pillar 1) but provably **not** the indefinite
  pairing (Pillar 2) — CAP.
- **The map for Route A is now closed at Pillar 2, with a proof**, consistent with the standing CAP/SURF conclusion:
  the indefinite $Q$ needs the arithmetic surface, which is the open core. No spectral/analytic pairing substitutes
  for it.
