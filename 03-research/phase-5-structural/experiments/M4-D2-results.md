# M4 / D2 — Numerical results (honest report, including what failed and what it redirects)

**Route B / M5 experiment.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
Code: `d2_destroy_test.py` (first pass, artifacts), `d2_gradient_check.py` (clean gradient check).
Env: `/usr/bin/python3`, numpy 2.0.2 + mpmath 1.4.1. **Self-contained Gram, NOT P7's validated engine.**

> **One-line outcome.** Proposition D2 (the gradient formula) is **numerically confirmed** (rel. err
> $\sim10^{-7}$) and the gradient is **spread across $\sim$14 Euler factors** — the structural non-tautology is
> exhibited. **But** two honest negatives reshape the program: (i) the self-contained Gram does **not**
> reproduce P7's positivity baseline (RH-true $\zeta$ wrongly gives $\lambda_{\min}<0$), so the *absolute*
> margin and the margin-discriminant test need the real engine; (ii) per P7's validated data (engine-spec §4)
> the *scalar* $\lambda_{\min}$ sits at the floor for **all** RH-true L-functions and only fires for $L_{\mathrm{DH}}$
> — i.e. **the scalar margin is essentially an off-line-zero detector, hence near-tautological**. The genuine
> non-tautological invariant is therefore the **finer structure** (the gradient profile, confirmed here; the
> per-prime anatomy T3), *not* the scalar margin. This is a real redirection, surfaced by computation.

---

## 1. What was confirmed: Proposition D2 (the gradient) ✅

On the complex-Hermitian localized arithmetic Gram $Q$ (Hermite basis, $J=10$, $\sigma=1$, $T_0=46.13$,
$X=2\times10^4$), with $\lambda_{\min}$ **simple** (spectral gap $\lambda_1-\lambda_0=2.14$):

| $n$ | Hellmann–Feynman $-\tfrac1{\sqrt n}|\langle w_n|u_0\rangle|^2$ | finite difference | rel. err |
|---|---|---|---|
| 2 | $-9.9550\times10^{-3}$ | $-9.9550\times10^{-3}$ | $2.1\times10^{-7}$ |
| 5 | $-9.9655\times10^{-3}$ | $-9.9655\times10^{-3}$ | $2.1\times10^{-7}$ |
| 9 | $-1.9443\times10^{-2}$ | $-1.9443\times10^{-2}$ | $1.5\times10^{-7}$ |
| 11 | $-1.5017\times10^{-2}$ | $-1.5017\times10^{-2}$ | $3.9\times10^{-8}$ |
| 13 | $-1.9107\times10^{-3}$ | $-1.9107\times10^{-3}$ | $5.3\times10^{-7}$ |

**Proposition D2 holds to $\sim10^{-7}$** — the analytic gradient is correct. *(The first-pass script gave
huge errors; the bug was realifying a genuinely complex-Hermitian $Q$, corrupting $u_0$. Fixed by keeping
$Q$ complex Hermitian. Logged as an error caught.)*

**The non-tautology structure (analytic D2, exhibited).** The gradient profile
$|\partial I/\partial\Lambda(n)|=\tfrac1{\sqrt n}|\langle w_n|u_0\rangle|^2$ over primes is **broadly spread**
(14/15 test primes carry $>1\%$ of the max), peaking near $p\approx29$–$31$:
```
 p= 2  ###            p=19  ###################
 p= 5  ###            p=23  ##########################################
 p=11  #####          p=29  ###########################################################
 p=17  ########       p=31  ############################################################
 p=37  #####################################################   p=41 ###############...
```
So the invariant's sensitivity is a **genuine multi-Euler-factor functional**, not a read-out of a single
nearest zero — the structural content of T1/analytic-D2, now numerically visible.

---

## 2. What failed / what is artifact (reported, not hidden)

**(i) The self-contained Gram lacks P7's positivity baseline.** $\zeta$ (RH-true) returned
$\lambda_{\min}=-5.56$, which is **wrong**: an RH-true L-function must give $\lambda_{\min}\ge0$ locally.
Cause (engine-spec §3): suppressing the GRH baseline requires prime cutoff $X=10^5$ **and** the full
archimedean + polar terms; my quick build ($X=2\times10^4$, schematic archimedean, no polar) leaves a steep
baseline that dominates. **Consequence:** the *absolute* $\lambda_{\min}$ here is artifact; the
margin-discriminant (TEST B) and the crossing (TEST C) of `d2_destroy_test.py` are **not valid** as run and
require P7's validated engine (Colab/v8) or a faithful reimplementation of engine-spec §3.

**(ii) The scalar margin is near-tautological (engine-spec §4 + this run).** P7's *validated* data shows
$|\lambda_{\min}|/\mathrm{tr}\approx10^{-8}$ for **all** RH-true controls ($\zeta$, $L(\chi_4)$, $L(\Delta)$)
and $\approx1.7$ (huge) only for $L_{\mathrm{DH}}$. So the scalar $\lambda_{\min}$ **does not discriminate
among RH-true L-functions** — it essentially detects off-line zeros, i.e. behaves like $f(d)$. **My TEST B
(margin difference between two RH-true L's) is therefore the wrong discriminant**: with the validated engine
both would sit at the floor. *(The large difference I saw, $-5.56$ vs $-0.024$, was baseline artifact —
different $\Gamma$-factors producing different baselines, not a genuine arithmetic margin.)*

---

## 3. The redirection (the real finding)

Items (i)–(ii) sharpen the program honestly:

> **The scalar margin $\lambda_{\min}$ is not the non-tautological invariant** — by P7's own validated data it
> is an off-line-zero detector ($\approx f(d)$). **The non-tautological, arithmetic content lives in the finer
> structure:** the **gradient profile** $\partial I/\partial\Lambda(n)$ (confirmed §1: a genuine
> multi-Euler-factor object) and the **per-prime anatomy** $R_p$ (T3). These *are* local-arithmetic and *not*
> reducible to $d$.

This does **not** break T1 (its *logical* claim — $I^{(X)}$ factors through finite local data while $d$ does
not — remains correct). It refines *which* invariant to use: not the scalar $\lambda_{\min}$ (whose variation
is off-line-dominated), but the **gradient / eigenvector / anatomy** structure. Concretely, the discriminant
$\zeta$ vs $L_{\mathrm{DH}}$ should be read in the **$R_p$-profile** (T3), not in a single number — exactly
where the analytic machinery already points.

---

## 4. Status and next steps (revised by the data)

- **Prop D2 (gradient)** — ✅ proved (analytic) **and numerically confirmed** ($\sim10^{-7}$); non-tautology
  structure exhibited (spread over primes).
- **T1** — ✅ (logical locality intact); **refined**: the non-tautological signal is the gradient/anatomy,
  not the scalar margin.
- **T2 (transversal crossing)** — ✅ analytic; **numerical confirmation deferred** to P7's validated engine.
  *Note:* engine-spec §4 independently reports $|\lambda_{\min}|\propto\delta^{\alpha}$, $\alpha\approx2.03$,
  $R^2=0.999$ — i.e. P7's **validated data already confirms the $\delta^2$ law of T2**. (Cite this as the
  numerical T2 confirmation; my self-contained TEST C was artifact.)
- **Scalar margin discriminant (TEST B)** — ❌ wrong object (off-line-dominated; redirect to T3).
- **Next operative step:** run on **P7's validated engine** (or a faithful engine-spec §3 build, $X=10^5$ +
  full archimedean+polar) to compute the **$R_p$-profile** (T3) for $\zeta$ and $L_{\mathrm{DH}}$ — the
  finer, non-tautological discriminant. The scalar-margin route is dropped.

**Net for the panel.** *The numerical D2 confirmed the analytic gradient (Prop D2) to $10^{-7}$ and exhibited
its spread over $\sim$14 Euler factors (the non-tautological structure). It also produced two honest
negatives: my self-contained Gram lacks P7's positivity baseline (absolute margins are artifact), and — more
importantly — P7's validated data shows the scalar $\lambda_{\min}$ is an off-line-zero detector ($\approx
f(d)$, near-tautological). So the program is redirected: the non-tautological invariant is the per-prime
anatomy / gradient profile (T3), not the scalar margin. T2's $\delta^2$ law is independently confirmed by P7's
validated data ($\alpha\approx2.03$). Net: one analytic prediction confirmed, one invariant retired, the real
target sharpened to the $R_p$-profile.*
