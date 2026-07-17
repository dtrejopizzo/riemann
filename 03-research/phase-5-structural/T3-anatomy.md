# T3 — The anatomy theorem: the per-prime decomposition of the localized Weil margin (analytic)

**Route B / M5, pure-theory milestone T3.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
Foundation: $Q_{\mathrm{arith}}(L)=A_\infty-\sum_n\frac{\Lambda_L(n)}{\sqrt n}w_nw_n^*$ (P7; setup of
`M5-T1-T2-proofs.md` §0). Motivation: the numerical D2 (`experiments/M4-D2-results.md`) **retired the scalar
margin** (near-tautological off-line detector) and identified the **gradient/anatomy profile** as the
surviving non-tautological invariant. Per the advisor's ordering: **formalize T3 first, build the validated
engine after** — so the engine measures the surviving object $\{R_p\}$, not the degraded scalar.

> **What T3 establishes (this file, analytic).** An **exact** decomposition of the localized Weil margin into
> an archimedean term and a sum of per-prime contributions, $\lambda_{\min}=R_\infty-\sum_p R_p$; its
> reformulation as a **mass problem** over prime log-frequencies, $\lambda_{\min}=\min_{\|u\|=1}[R_\infty(u)-\|\mu_u\|]$;
> and the identity **gradient $=$ anatomy density**, which makes the D2-confirmed gradient *literally* the
> anatomy profile. **What T3 does NOT yet establish:** any *deep* structural statement about the profile (a
> sum rule beyond the trivial one, a concentration theorem, a relation to the local Euler data) — that is the
> open content (T3-open), and the honest target of the validated-engine phase.

---

## 1. T3.1 — The exact anatomy identity

Let $u_0$ be a unit minimal eigenvector of $Q:=Q_{\mathrm{arith}}^{(X)}(L)$, $\lambda_{\min}=\langle u_0,Qu_0\rangle$.
Write $\widehat{u}(x):=\sum_i u_i\,\widehat{\phi_i}(x)=\langle u,w_x\rangle$ for the frequency content of $u$ at
log-frequency $x$ (so $(w_n)_i=\widehat{\phi_i}(\log n)$, $\widehat u(\log n)=\langle u,w_n\rangle$).

> **Theorem T3.1 (anatomy identity).** With
> $$
> R_\infty(u):=\langle u,A_\infty u\rangle,\qquad
> R_p(u):=\sum_{k\ge1}\frac{\Lambda_L(p^k)}{\sqrt{p^k}}\,\big|\widehat u(k\log p)\big|^2,
> $$
> one has the **exact** (non-perturbative) decomposition
> $$
> \boxed{\ \lambda_{\min}\ =\ R_\infty(u_0)\ -\ \sum_p R_p(u_0).\ }
> $$

**Proof.** $\lambda_{\min}=\langle u_0,A_\infty u_0\rangle-\sum_n\frac{\Lambda_L(n)}{\sqrt n}|\langle u_0,w_n\rangle|^2$
by (0.1). Group $n=p^k$ by prime $p$ and use $\langle u_0,w_{p^k}\rangle=\widehat{u_0}(k\log p)$. $\square$

This is a Rayleigh decomposition: it is *exact* and *clarifying* (it localizes the margin onto primes) but it
is not, by itself, deep — $u_0$ is the joint minimizer, so the $R_p$ are evaluated at the unstable direction,
not free parameters. The content is *where the mass sits*, addressed next.

---

## 2. T3.2 — The margin as a mass problem over prime log-frequencies

For an L-function with non-negative coefficients ($\Lambda_L\ge0$, e.g. $\zeta$; for general $L$ take the
Hermitian/real part), define the **anatomy measure** of a unit vector $u$ on $(0,\infty)$:
$$
\mu_u\ :=\ \sum_{n\ge2}\frac{\Lambda_L(n)}{\sqrt n}\,\big|\widehat u(\log n)\big|^2\,\delta_{\log n}
\ \ge 0,\qquad \|\mu_u\|=\mu_u\big((0,\infty)\big)=\sum_p R_p(u).
$$

> **Corollary T3.2 (variational/mass form).**
> $$
> \lambda_{\min}\ =\ \min_{\|u\|=1}\Big[\,R_\infty(u)\ -\ \|\mu_u\|\,\Big],
> $$
> i.e. the minimal eigenvector is the unit direction that **maximizes the prime-mass $\|\mu_u\|$ net of the
> archimedean cost $R_\infty(u)$**. In particular $\lambda_{\min}<0\iff$ there is a unit direction whose
> prime-mass exceeds its archimedean form.

**Reading.** The localized positivity is a **competition**: the archimedean form $R_\infty$ (the CC manifest
square, $\succeq0$) versus the prime-mass $\|\mu_u\|$. For an RH-true $L$ the validated engine reports
$\lambda_{\min}\approx0^+$ (floor): the competition is *exactly balanced at the top of the spectrum*. This is
the precise, zero-independent meaning of "ζ is locally Weil-positive": **no unit direction lets the primes
out-mass the archimedean square** — and it is *tight*.

---

## 3. T3.3 — Gradient $=$ anatomy density (the D2 result IS the profile)

> **Proposition T3.3.** The D2 gradient is the density of the anatomy measure w.r.t. the coefficients:
> $$
> \frac{\partial\lambda_{\min}}{\partial\Lambda_L(n)}\ =\ -\frac{1}{\sqrt n}\big|\widehat{u_0}(\log n)\big|^2
> \ =\ -\,\frac{d\mu_{u_0}}{d\big(\Lambda_L(n)\big)}\Big|_{\log n}.
> $$

**Proof.** Prop. D2 (Hellmann–Feynman, `M5-T1-T2-proofs.md` §3) gives the first equality; the second is the
definition of $\mu_u$. $\square$

> **Consequence (what the experiment actually measured).** The numerically confirmed gradient profile
> (M4-D2-results §1, spread over $\sim$14 primes) **is** the anatomy density $d\mu_{u_0}$. So the destroy-test
> did not merely confirm a derivative — it **measured the surviving invariant** (the anatomy profile) directly.
> The retired scalar $\lambda_{\min}$ is just the *total* $R_\infty-\|\mu_{u_0}\|$; the *profile* $\{R_p\}$ is
> the richer, non-tautological object.

---

## 4. T3.4 — The observed band: honest separation of basis vs arithmetic

The anatomy density is $\big|\widehat{u_0}(\log p)\big|^2=\big|\sum_{k<J}(u_0)_k\,\widehat{\phi_k}(\log p)\big|^2$.
For the **Hermite basis** $\phi_k\leftrightarrow h_k(\sigma\,\cdot)$ (Fourier eigenfunctions), each
$\widehat{\phi_k}(x)\propto h_k(\sigma x)$ is supported, classically, on $|x|\lesssim x_J:=\sqrt{2J-1}/\sigma$
(the Hermite turning point). Hence:

> **Observation T3.4 (basis envelope vs internal structure).** The anatomy density has an **outer cutoff**
> $\log p\lesssim x_J=\sqrt{2J-1}/\sigma$ that is a **property of the basis, not the arithmetic** (for
> $J=10,\sigma=1$: $x_J\approx4.4$). The observed band $\log p\approx3.3$–$3.7$ sits just inside this edge,
> reflecting that $u_0$ is dominated by the **highest Hermite modes** (whose outer lobe lives there). **Any
> claim of arithmetic ("geometric") structure must be made *relative to this envelope*, and requires (i) the
> validated engine** (the present $u_0$ is from an un-baseline-suppressed Gram, so its detailed shape is
> provisional, M4-D2-results §2) **and (ii) ideally the Slepian basis** (a sharp time-band cutoff, replacing
> the soft Hermite turning point with a clean envelope). Until then, the band's *location* is basis-set; only
> its *internal modulation* could be arithmetic, and that is unproven.

This is the disciplined version of the advisor's "geometric band": **kept as a lead, demoted from a finding.**

---

## 5. T3.5 — The discriminant target, and what is genuinely open (T3-open)

The surviving non-tautological invariant is the **anatomy profile**
$$
\mathcal R(L):=\big(R_2(u_0),R_3(u_0),R_5(u_0),\dots\big)\quad\text{(equivalently the density }d\mu_{u_0}).
$$
The classification discriminant is $\mathcal R(\zeta)$ vs $\mathcal R(L_{\mathrm{DH}})$ — the **profile
difference**, computed on the validated engine. T3.1–T3.3 make this object exact and tie it to the confirmed
gradient; T3.4 controls the basis envelope.

> **T3-open (the genuinely deep targets — not yet proved).**
> 1. **A non-trivial sum rule / concentration theorem:** does $\mu_{u_0}$ concentrate (beyond the basis
>    envelope) at an arithmetically meaningful frequency set as $T_0\to\infty$? (A theorem here would turn the
>    "band" into arithmetic geometry.)
> 2. **Profile $\Rightarrow$ Euler-data relation:** express $R_p(u_0)$ in terms of the local factor
>    $L_p$ and the window data, isolating *which* feature of $L_p$ (the coefficient $a_p$, its argument, the
>    Ramanujan bound $|a_p|\le2$) controls $R_p$.
> 3. **The discriminant theorem (T4 seed):** a profile statistic $\Phi(\mathcal R)$ with
>    $\Phi(\mathcal R(\zeta))\le1<\Phi(\mathcal R(L_{\mathrm{DH}}))$, proved for a structural sub-class.
>
> These are the real content; T3.1–T3.4 are the rigorous scaffolding that makes them well-posed.

---

## 6. Phasing (advisor's ordering, adopted)

- **Phase 1 (done, this file):** formalize T3 — the exact identity (T3.1), the mass form (T3.2), gradient $=$
  density (T3.3), basis-vs-arithmetic separation (T3.4), the open targets (T3.5).
- **Phase 2 (next, analytic):** push T3-open #2 (the $R_p\leftrightarrow L_p$ relation) — analytic, no engine
  needed; and re-derive the profile in the **Slepian basis** to remove the Hermite envelope ambiguity.
- **Phase 3 (after):** build the **validated engine** (engine-spec §3: $X=10^5$, full archimedean+polar) to
  measure $\mathcal R(\zeta)$ vs $\mathcal R(L_{\mathrm{DH}})$ — the surviving object, not the retired scalar.

**Net for the panel.** *T3 makes the surviving invariant exact: the localized Weil margin decomposes as
$\lambda_{\min}=R_\infty-\sum_p R_p$, equivalently a mass competition between the archimedean square and the
prime-frequency mass $\mu_{u_0}$; the D2-confirmed gradient is literally the anatomy density $d\mu_{u_0}$. The
observed prime band is shown to be basis-enveloped (Hermite turning point) with only its internal modulation
possibly arithmetic — demoted from finding to lead, pending the validated engine and the Slepian basis. The
deep content (a concentration theorem; the $R_p\leftrightarrow$ Euler-factor relation; a profile discriminant
$\Phi$) is now well-posed and is the program's forward target — pursued analytically before the engine, so the
engine measures the surviving anatomy profile rather than rescuing the retired scalar.*

---

### Status
- T3.1 anatomy identity — ✅ proved (exact Rayleigh decomposition).
- T3.2 mass/variational form — ✅ proved.
- T3.3 gradient = anatomy density — ✅ proved (via D2).
- T3.4 basis-vs-arithmetic (band) — ✅ honest separation; band demoted to lead.
- T3.5 / T3-open — ⬜ the deep targets (concentration; $R_p\leftrightarrow L_p$; discriminant $\Phi$).
- Phase 2 (Slepian re-derivation + $R_p\leftrightarrow L_p$) — ⬜ next, analytic.
