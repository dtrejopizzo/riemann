# Phase 16 · The MSZ resonance pairing is definite (Bochner) — Route A's pairing hits CAP

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
This document does three things at once: (i) arbiter-tests the French researcher's Maass–Selberg–Zagier (MSZ)
proposal for Pillar 2, (ii) executes the bilinear resonance pairing I proposed, (iii) verifies the Phase-4
connection. All three converge on one verdict: **the natural resonance pairing on the modular surface is
definite (Bochner-positive), not the indefinite Weil form $Q$ — Route A's pairing reproduces the program's
wrong-sign capstone (CAP).** French proposal: **Pillar 2 REJECTED.**

---

## 1. Arbiter test of the French MSZ proposal
The proposal claims (its "Theorem"): the Gram matrix of Eisenstein residues $\Psi_\rho=\operatorname{Res}_{s=\rho/2}E(s)$
in the MSZ pairing is **diagonal** with signs $\varepsilon_\rho=\operatorname{sign}(\operatorname{Im}\rho)$ ($+1$
on-line, $-1$ off-line) and index $\kappa$, reproducing $Q$. **Red flag (pre-computation):**
$\operatorname{sign}(\operatorname{Im}\rho)=\operatorname{sign}(\gamma_\rho)$ distinguishes $\gamma>0$ from $\gamma<0$
(complex-conjugate zeros), **not** on-line from off-line — an off-line zero with $\gamma>0$ still has
$\operatorname{sign}(\operatorname{Im}\rho)=+1$. So the proposed $\varepsilon_\rho$ cannot be the $\kappa$-detector.

**Executed (correcting their Step-2 formula, which omitted the divergence).** In the cusp, $\Psi_\rho\sim R_\rho
y^{1-\rho/2}$, $R_\rho=\operatorname{Res}_{s=\rho/2}\varphi=\xi(\rho-1)/(2\xi'(\rho))$. The regularized pairing is the
Hadamard finite part of a divergent integral:
$$
\langle\Psi_\rho,\Psi_\sigma\rangle_{\mathrm{MSZ}}=R_\rho\overline{R_\sigma}\cdot\mathrm{FP}_{T\to\infty}\!\int_1^T
y^{-1/2+i(\gamma_\sigma-\gamma_\rho)/2}\frac{dy}{y}\cdot y
= -\,\frac{R_\rho\overline{R_\sigma}}{\tfrac12-i(\gamma_\rho-\gamma_\sigma)/2}.
$$
*(The integral diverges as $T^{1/2}$ — the resonances are not $L^2$ — and the $T^{1/2}$ is dropped: the finite part is
regularization-dependent.)* Results (`pillar2_MSZ_gram.py`, `pillar2_MSZ_signature.py`, $R=8$ zeros):

- **NOT diagonal:** off/diagonal ratio $=0.38$ ($O(1)$, not $\sim0$). The matrix is the **Hilbert/Cauchy kernel**
  $-R_\rho\overline{R_\sigma}/(\tfrac12-i(\gamma_\rho-\gamma_\sigma)/2)$. The diagonality "Theorem" **fails**.
- **Diagonal all one sign** ($-$), independent of any on/off-line distinction $\Rightarrow$ not $\varepsilon_\rho$.
- **Signature constant:** all $8$ eigenvalues $<0$ ($-1.165,\dots,-0.303$). The form is **negative-definite**.

**Why negative-definite:** $G=-D\,K\,D^*$ with $D=\operatorname{diag}(R_\rho)$ and $K_{\rho\sigma}=1/(\tfrac12-i
(\gamma_\rho-\gamma_\sigma)/2)$ a **positive-definite (Bochner) kernel** ($1/(c-i(x-y))=\int_0^\infty e^{-ct}e^{ixt}
\overline{e^{iyt}}\,dt$). So $G\preceq0$ **regardless of RH** — constant signature, $\kappa$ undetectable.

**Verdict: French proposal — Pillar 2 REJECTED.** The MSZ pairing is not diagonal, not $\varepsilon_\rho$-signed, has
constant (negative-definite) signature, and is regularization-dependent. It is **not** the Weil form $Q$.

## 2. The bilinear pairing I proposed — same answer
The computation above **is** the bilinear resonance pairing. Its content: the natural Eisenstein/resonance pairing is
the **Bochner-positive Hilbert kernel**, a *definite* form. The Weil form $Q$ is *indefinite* (index $\kappa$, the
off-line count). A definite Bochner form **cannot** carry $\kappa$. So the pairing does not reproduce $Q$.

## 3. The Phase-4 connection — confirmed
Two fingerprints tie Route A's pairing to the Phase-4 / CAP walls:
- **Non-$L^2$ / over-sampling (Phase 4, Days 9–15):** the pairing required dropping a divergent $T^{1/2}$ — the
  resonances are not $L^2$, exactly the Phase-4 de Branges non-$L^2$/regularization issue. Route A's *weights* are
  non-trivial ($|R_\rho|=O(1)$, M9/03), but its *pairing* is the regularization-dependent Hilbert kernel — back in the
  Phase-4 difficulty.
- **Bochner positivity = CAP (Attempt 2 / P13):** the kernel $1/(\tfrac12-i\Delta)$ is positive-definite, giving a
  *definite* form (a lower bound), never the indefinite/upper-sign $Q$. This is the program's **wrong-sign capstone**
  (every available positive structure is one-sided; $Q$'s indefiniteness is the missing piece), now reproduced on the
  modular surface.

---

## Net result for Route A (honest)
- **Pillar 1 (spectrum):** zeros present as scattering resonances ✓ (partial: resonances, not clean $L^2$ spectrum).
- **Pillar 2 (pairing):** the **natural resonance pairing is definite (Bochner), not the indefinite $Q$** — it does
  not carry $\kappa$, and is regularization-dependent. **The MSZ route to Pillar 2 fails, and it fails by CAP.**

So even the only live route hits the wrong-sign capstone at the pairing level: the modular surface supplies the zeros,
but its natural (regularized) pairing is the one-sided positive form, not Weil's indefinite $Q$. To realize $Q$ one
needs an *indefinite* pairing on the resonances — and the program has shown across Phases 4–15 that the indefiniteness
($=\kappa=$ RH) does not come from any Bochner-positive/definite structure. The resonance realization, to give $Q$,
must supply the indefiniteness from outside the MSZ/Bochner pairing — which is the same open core (CAP/SURF), now
located inside Route A.

**Status:** Route A's natural pairing REJECTED (CAP). The zeros are in the modular surface; the indefinite $Q$ is not
in its regularized pairing. No crossing. The wall is the same wrong-sign capstone, reached from the $GL_2$ side.
