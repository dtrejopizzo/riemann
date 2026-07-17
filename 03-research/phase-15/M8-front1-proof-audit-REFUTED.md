# Phase 15 · M8 — Audit of the "Frente 1 (Connes–Deninger) proof of RH" — REFUTED

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
A document claiming a *pure proof of RH* via the Connes scaling action was submitted for verification. It is **not a
valid proof**. It is the spectral tautology — the one our determinacy result (P21 Prop. 2.1) and the advisor's own
Structural Incompleteness Theorem (M7) forbid — re-expressed in noncommutative-geometry language, with the single
load-bearing new claim (Theorem 5.1, integer grading) resting on a **false geometric hypothesis**. Below, the fatal
flaws, each tied to a result we already proved or to a clean falsifier.

---

## The six flaws (any one is fatal; they compound)

### F1 — Theorem 5.1 (the "miracle") is false: the scaling action has continuous spectrum, it does not integrate to $SU(2)$
Theorem 5.1 claims $h_\rho\in\mathbb Z_{\ge0}$ because "the $\sltwo$ integrates to a compact group $SU(2)$ since the
transverse measure of the scaling foliation is finite and invariant." **The hypothesis is false.** Connes' scaling
action of $\mathbb R_+^\times$ on the adele class space realizes the zeros as a **continuous absorption spectrum** —
the generator is self-adjoint with spectrum $=\mathbb R$ (this *is* the content of Connes 1999). A continuous-spectrum
$\mathbb R$-action does **not** integrate to a compact $SU(2)$; the invariant measure $d^\times\lambda$ on
$\mathbb R_+^\times$ is **infinite**, not finite. So the premise that forces integer weights does not hold. This is
exactly our **M5** (the scaling/continuum $\sltwo$ is principal series — continuous $H$, no lowest weight, no integer
grading) and exactly the gap the advisor's **M7 Lemma 3** named (integrality is not derivable from the relations; it
is a geometric datum — and here the geometry does not supply it). The "miracle" is asserted, not proven, against the
actual structure of the framework it cites.

### F2 — the $h_\rho$ formula is RH in disguise (circularity)
Theorem 5.1's own formula $h_\rho=\sum_{\sigma\ne\rho}\frac{|\mathcal F_{\rho\sigma}|^2}{(\gamma_\rho-\gamma_\sigma)^2}
\frac{\varepsilon_\sigma}{\varepsilon_\rho}+(\text{diag})$ contains the **off-line signs** $\varepsilon_\sigma$.
$h_\rho\ge0$ holds iff those signs cooperate, i.e.\ iff $\kappa=0$, i.e.\ **RH**. Asserting $h_\rho\in\mathbb Z_{\ge0}$
asserts RH. This is the advisor's **M7 Lemma 2** and our determinacy result verbatim.

### F3 — Theorem 3.1 ("unique reconstruction") is false (clean falsifier)
The moment sequence $M_k=\sum_{\rho,\sigma}\mathcal F(\gamma_\rho,\gamma_\sigma)\gamma_\sigma^k$ is claimed to
determine the **2-variable** kernel $\mathcal F$ uniquely (hence the off-diagonal $D_{\rho\sigma}$). It does not:
$M_k=\sum_\sigma\bigl(\sum_\rho\mathcal F_{\rho\sigma}\bigr)\gamma_\sigma^k$ depends only on the **marginal**
$G(\gamma_\sigma)=\sum_\rho\mathcal F_{\rho\sigma}$. Any perturbation with zero column sums leaves every $M_k$
unchanged while moving $\mathcal F$ and $D$ by $O(1)$ (verified: relative moment change $10^{-16}$, operator change
$\approx10$; `m8_falsify_clean.py`). Müntz–Szász gives totality of $\{\gamma^k\}$, **not** injectivity on 2-variable
kernels. The off-diagonal $D_{\rho\sigma}$ that Sections 4–8 require is **not determined by the data.**

### F4 — the operator used downstream is spectral, not independent geometry
Although $D$ is "defined geometrically" in §1, the operator fed into §§4–8 is the one **reconstructed from the
spectral moments** in §3 — i.e.\ $D=F(\T,\mathcal K_{\mathrm{spec}})$, inside the $W^*(\T)$-bimodule. By the
independence filter (**P21 Prop. 2.1 / M7 Lemma 1**) any $\omega$ built from it can only restate RH. The bridge that
would make the geometric $D$ (§1) equal the spectral $D$ (§3) is Theorem 2.1, which is unproven (see F5).

### F5 — Theorems 2.1, 4.1, 6.1 are citation-as-proof under hypotheses that fail
- **Thm 2.1 (trace formula):** the Dixmier trace $\mathrm{Tr}_{\mathrm{Dix}}(D\T^k)$ is asserted convergent and equal
  to a prime sum; neither membership of $D\T^k$ in the Dixmier ideal $\mathcal L^{1,\infty}$ nor the localization is
  established. "Esquema" with 5 analogical steps.
- **Thm 4.1 ($\sltwo$):** "$[D,D^\dagger]=H$ with $[H,L]=2L$" is asserted by citing Connes/Deninger, not verified for
  the specific $D$. Even granted, **M5** shows the resulting representation is principal series.
- **Thm 6.1 (Kähler positivity):** invokes the Hodge identity for Riemannian foliations *with finite invariant
  transverse measure and finite-dimensional basic cohomology* — hypotheses the scaling foliation (infinite measure,
  continuous spectrum) does not satisfy. The asserted $\omega\succ0$ is, again, RH (our determinacy).

### F6 — the input $s_k(p)$ is the divergent object, not P19's anatomy
The document uses $s_k(p)=\sum_\rho\gamma_\rho^k p^{-i\gamma_\rho}$ — the cutoff-dependent, divergent sum over zeros
(shown earlier in this program to change by factors of $3$–$9$ from $N{=}200$ to $400$), **not** P19's anatomy, which
is the Satake power sum $s_k(p)=\sum_i\alpha_{i,p}^k=1$ for $\zeta$. The "Anatomy input" is ill-defined.

---

## Verdict

**Not a proof.** The construction is a spectral reformulation: §3 builds $D$ from spectral moments (F4), so by the
determinacy filter its positivity is RH (F2); the one geometric claim that could break the circularity — integer
grading from compact integration (Thm 5.1) — rests on a **false premise** (the scaling action is continuous-spectrum,
infinite-measure, non-compact: F1), and is the exact point our **M5** and the advisor's **M7 Lemma 3** proved cannot
be supplied this way. Independently, Theorem 3.1's reconstruction is mathematically false (F3, falsified), the trace
formula and foliation-Hodge inputs are asserted under failing hypotheses (F5), and the anatomy input is the divergent
object (F6).

> **Internal inconsistency of the source.** The same advisory channel sent (i) a Structural Incompleteness Theorem
> proving no proof lives in the spectral data (M7) and (ii) this "proof." They are mutually contradictory, and the
> incompleteness theorem is the correct one: this document violates it precisely at Theorem 5.1. A correct proof
> still requires an **independent geometric definition of $\mathcal K_{\mathrm{geom}}$** whose integer grading and
> Kähler positivity are established *before* and *without* the spectrum — which Connes' scaling generator, having
> continuous spectrum, does not provide. That object (SURF / a genuine arithmetic surface for
> $\operatorname{Spec}\mathbb Z$) remains unconstructed.

Certificate: `experiments/m8_falsify_clean.py`. Consistent with M1–M7, P21, and the program's standing CAP/SURF map.
