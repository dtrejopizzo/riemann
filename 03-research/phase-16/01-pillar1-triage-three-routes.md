# Phase 16 · Pillar-1 triage of the three candidate routes

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
The arbiter's first job: run each candidate $\mathcal X$ through **Pillar 1** (the spectrum/trace filter) — the fast
rejection test. A route is REJECTED if it cannot carry a Frobenius whose spectrum is $\{\gamma_\rho\}$; it survives
only if the zeros genuinely appear. Result: **C rejected, B untestable (no object yet), A survives** — A is the only
live route, and it survives because the zeros provably appear in the $GL_2$ Eisenstein spectrum.

---

## Route C (global prismatic) — **REJECTED at Pillar 1**
By M6: prismatic/TC packages the **local** Frobenius $\{\varphi_p\}$ into a monoid action; the crystalline/prismatic
Frobenius eigenvalues are the **local Satake** $\alpha_{i,p}$ (for $\zeta$, trivially $1$ — the anatomy $s_k(p)=1$),
**not** the global zeros. No single global endomorphism with $\operatorname{spec}=\{\gamma_\rho\}$ exists (the global
Sen generator fails: Frobenius $\to$ $L$-factors, Sen $\to$ Hodge–Tate weights, not interchangeable). **Fails
Requirement 1.1 (no Frobenius with the zero-spectrum).** Rejected. *(M6.)*

## Route B ($\delta$ / $\mathbb F_1$, Spec $\mathbb Z\times_{\mathbb F_1}$Spec $\mathbb Z$) — **UNTESTABLE (pre-Pillar-1)**
There is no constructed cohomology with a Frobenius to test: "$\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}
\operatorname{Spec}\mathbb Z$" is not yet a scheme carrying a Weil cohomology. The available operators — the
$\delta$-Frobenius / Adams operations $\psi_p$ of Borger's $\Lambda$-ring structure — act with **integer Adams-weight
eigenvalues (local data)**, not the global $\gamma_\rho$. One cannot compute a test-function trace of a non-existent
object. **Status: pre-Pillar-1 — the wall is foundational (build the global $\delta$-cohomology, intersection theory,
and diagonal $[\Delta]$ first).** Not rejected, but nothing to verify yet.

## Route A (Shimura $GL_2$ / Eisenstein) — **SURVIVES Pillar-1 triage (zeros provably present)**
On the modular surface $X=SL_2(\mathbb Z)\backslash\mathbb H$ the real-analytic Eisenstein series $E(z,s)$ has constant
term $y^s+\varphi(s)y^{1-s}$ with **scattering determinant**
$$
\varphi(s)=\frac{\xi(2s-1)}{\xi(2s)},\qquad \xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$
**The $\zeta$-zeros are the poles of $\varphi$** (resonances of the continuous spectrum): poles $\iff\xi(2s)=0\iff
2s=\rho\iff s=\rho/2=\tfrac14+i\gamma/2$. **Verified** (`experiments/pillar1_route_A_scattering.py`): $|\varphi|$
blows up to $\sim5\times10^5$ at $s=\tfrac14+i\gamma_k/2$ (vs $\sim1$ off-resonance) for the first zeros, with
$\xi(2s)=0$ to $10^{-28}$. **The zeros genuinely live in the $GL_2$ geometry.**

**Pillar 1 — PARTIAL (not rejected, not fully met).** The zeros appear, but as **poles of a $1\times1$ scattering
matrix on a continuous spectrum**, not yet as a clean **simple** Frobenius spectrum on a finite-type cohomology; and
the same surface also carries the **cuspidal (Maass) spectrum** = wrong eigenvalues. The open sub-tasks:
1. **Discretize** the Eisenstein/continuous spectrum so the zeros become a clean Frobenius spectrum
   $\operatorname{spec}(\mathrm{Frob})=\{\gamma_\rho\}$ on a cohomology $H^1_{\mathrm{Eis,prim}}$ (isolate from the
   cuspidal part).
2. **Pillar 2 (a point in A's favor):** the natural pairing on the Eisenstein part is the **regularized
   Maass–Selberg / Zagier inner product**, which involves $\varphi'/\varphi$ and is **indefinite** — exactly the
   signature $(1,\infty)$ Pillar 2.2 demands (and *not* an unconditionally-definite height pairing, so it survives the
   heights filter, unlike the naive Arakelov route D2). Whether it equals $Q$ is the open test.
3. **Pillar 4:** a new arithmetic Hodge index for $H^1_{\mathrm{Eis,prim}}$ — **not** Yuan–Zhang (Correction 2).

---

## Triage verdict
| Route | Pillar 1 | Status |
|---|---|---|
| **C** prismatic global | Frobenius is local Satake, no global zero-spectrum (M6) | **REJECTED** |
| **B** $\delta$/$\mathbb F_1$ | no constructed cohomology; $\psi_p$ = local integer weights | **UNTESTABLE** (foundations) |
| **A** $GL_2$/Eisenstein | **zeros provably present** as scattering resonances $s=\rho/2$ (verified) | **SURVIVES** — the only live route |

**Directive:** concentrate on **Route A**. The zeros are in the geometry; the wall is the **Beilinson realization** —
discretize the Eisenstein spectrum to a clean Frobenius $H^1_{\mathrm{Eis,prim}}$, show its regularized (indefinite)
pairing equals $Q$, and prove a new Hodge index there. Next prototype: test whether the Eisenstein special values /
residues at $s=\rho/2$ assemble into a space carrying $Q$ (Pillar-2 prototype), and write the regularized pairing
explicitly. Routes B/C are not the place to spend effort now (B has no object; C is rejected).
