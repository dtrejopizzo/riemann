# Audit of the P7 → T2 → D2 → T3 → T4 structural line: does it collapse to a known barrier?

**Author: David Alejandro Trejo Pizzo · 2026-06-05.**
The audit's directive: of the program's branches, the only one possibly not yet forced to collapse into a known
barrier is the original **structural / arithmetic-Weil-form** line (P7, T2, D2, T3, T4). Audit it: is there an
object here that is *not* reducible to {a prime sum, a power of $\zeta$, a value-statistic, a known spectral
identity}? This is that audit, performed honestly, object by object — with one correction the auditor should
have: **this line was, in fact, already pushed to its reduction** (it became P11/P13), and the audit makes the
collapse explicit and traces it to the square-root barrier (N8). One genuinely un-reduced object survives, but
it is RH-*independent*.

---

## 0. What the line is

- **P7** — the localized arithmetic Weil form $Q=A_\Phi-P_F$ (archimedean Gram minus prime Gram), with bottom
  eigenvalue $\lambda_{\min}(Q)$ and ground state $u_0$; $\mathrm{RH}\Leftrightarrow$ local positivity.
- **T2** — the transversal forced transition (the $\delta^2$ law: an off-line zero forces $\lambda_{\min}<0$).
- **D2** — the analytic gradient $\partial\lambda_{\min}/\partial\Lambda(n)=-n^{-1/2}|\widehat{u_0}(\log n)|^2$.
- **T3** — the anatomy $\lambda_{\min}=R_\infty-\sum_p R_p$, $R_p=\sum_k p^{-k/2}|\widehat{u_0}(\log p^k)|^2$.
- **T4** — the Carleson/Bessel reformulation: positivity $\Leftrightarrow$ the prime measure is Carleson $\le1$.

## 1. The object is the positivity itself — the one nonlinear, individual-resolving tool

The whole line is built on $\lambda_{\min}(Q)\ge0$, i.e. the **positivity** of the Weil form. By N8, this is
exactly the kind of tool that *can* force absence (unlike the linear/aggregate prime sums): it is a
**quadratic / nonlinear** functional of the zeros, $Q=\sum_{\rho\in\text{window}}|f(\gamma_\rho)|^2$ (the
zero-side Gram), whose sign resolves an individual off-line zero (T2: the $\delta^2$ forced negativity). So the
line is **not** a fifth kind of object: it is the **positivity / wrong-sign-capstone side** of the wall — the
single nonlinear, absence-capable tool — and its content is the *sign* of $\lambda_{\min}$, which is RH.

## 2. Each object reduces (the audit, step by step)

- **D2 (the gradient).** $\partial\lambda_{\min}/\partial\Lambda(n)=-n^{-1/2}|\widehat{u_0}(\log n)|^2$ depends on
  the **ground state** $u_0$, which is the minimizer of $Q$ — for RH-true $\zeta$ it is the **zero-interpolating
  function** (it vanishes at the window's zeros). So $u_0$, and hence the gradient, is **determined by the
  zeros**; via the explicit formula it reduces to the **prime sum**. (It is nonlinear in the arithmetic, but
  through the eigenvector, not through a new variable.)
- **T3 (the anatomy).** $\lambda_{\min}=R_\infty-\sum_pR_p$ decomposes the bottom by prime; each $R_p$ is built
  from $\widehat{u_0}(\log p^k)$ — again the ground state at prime-power frequencies, **determined by the zeros**.
  The per-prime $G_p$ was already shown indefinite (**N1**): the decomposition exists but supplies no per-prime
  positivity. Reduces to the zeros / the cross-place prime structure.
- **T4 (the Carleson reformulation).** Positivity $\Leftrightarrow$ Carleson constant $\le1$. This is **exactly
  P11**: the band-limited Weil–Carleson constant $C(d,T_0)=\lambda_{\max}(P_F,A_\Phi)$, audited to
  **N3** (saturation $C\equiv1$, prime incoherence buys zero margin), **B1** (second order $=$ the sine-kernel /
  pair correlation), **N4** (the Connes prolate bridge). And **P13** computed $\lambda_{\min}(G)=\tfrac{\pi^2}6\beta_{\min}^2$:
  the localized-Weil bottom **is** the squared minimum normalized gap.
- **P7/T2 (the detector and the $\delta^2$ law).** The forced negativity is the zero-side Gram going indefinite
  when a zero is off the line — the Weil criterion localized; reduces to the zeros.

## 3. The collapse, traced to the square-root barrier

Assembling: $\lambda_{\min}(\text{localized Weil})=$ the regularized Hodge gap $=\tfrac{\pi^2}6\beta_{\min}^2$
(P13) $=$ the closest-pair / gap-universality quantity (the pair correlation, B1) $=$ controlled, ultimately, by
the **same prime-sum cancellation** whose square-root control is RH (**N8**). So:

> **The P7 structural line collapses to the wall — on the positivity side.** It is the one nonlinear,
> individual-resolving (absence-capable) tool, but its content is the **sign of $\lambda_{\min}$**, which is the
> **wrong-sign capstone**; and quantitatively $\lambda_{\min}=\tfrac{\pi^2}6\beta_{\min}^2$ ties it to the
> pair-correlation / gap-universality, i.e. the **square-root barrier (N8)**. It is not a fifth kind of object;
> it is the capstone, the core of the wall, viewed locally.

So **all branches now converge to the same wall**: the prime-count (ω) branch was self-referential (M14.3); the
linear exact tools (Littlewood, Motohashi) give density (N8); and the structural/positivity branch (P7) is the
capstone itself, reducing to the same square-root barrier through $\lambda_{\min}=\tfrac{\pi^2}6\beta_{\min}^2$.
The auditor's instinct was right to check it; the honest outcome is that it, too, collapses — completing the map.

## 4. The one genuinely un-reduced object — and why it does not help RH

There **is** an object in the line that does not reduce to the four barriers: **Conjecture B2** — *a factorizing
localized-Weil anatomy $\Leftrightarrow$ an Euler product*. This is a statement about the **classification of
$L$-functions** (the prime-*identity* / multiplicative structure), distinguishing $\zeta$ (Euler product) from
$L_{\mathrm{DH}}$ (none). It is genuinely new and not obviously reducible — **but it is RH-independent**: it
concerns *which* $L$-functions are multiplicative, not *where* their zeros lie. Like P14, it is real mathematics
that does not advance RH. (And the Euler-product structure it characterizes *is* $\zeta$ itself; using it for the
zeros routes through the explicit formula $=$ the prime sum $=$ N8.)

## 5. Verdict

- The P7 → T2 → D2 → T3 → T4 line **collapses** to the wall, on the **positivity/capstone side**, quantitatively
  the square-root barrier ($\lambda_{\min}=\tfrac{\pi^2}6\beta_{\min}^2$). It was, in effect, already audited as
  P11/P13/N1–N4; this makes the collapse and its destination explicit.
- **No fifth kind of object exists** in the program: every branch reduces to {prime sum / cancellation,
  $\zeta$-power / self-referential, value-statistic, known spectral identity}, i.e. to the one wall, now mapped
  from five sides (positivity, dynamics, probability, cohomology, cancellation).
- The single un-reduced object (Conjecture B2) is **RH-independent** — classification, not location of zeros.
- **Honest consequence:** the program has now audited *every* branch to the same wall. There is no remaining
  un-collapsed RH-directed line. The frontier is the square-root / upper-cancellation barrier itself, for which
  no available mechanism — including the structural/positivity one — provides an unconditional handle.
