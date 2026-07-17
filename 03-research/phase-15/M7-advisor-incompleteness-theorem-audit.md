# Phase 15 · M7 — Audit of the advisor's "Structural Incompleteness Theorem" (convergent confirmation)

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
An external advisor sent a pure-mathematics "incompleteness theorem" for the Anatomy–Kreĭn–Hodge program: *no proof
of RH exists within the current spectral data; the missing object is a geometric correspondence
$\mathcal K_{\mathrm{geom}}$ independent of the spectrum.* This document audits it lemma by lemma. **Verdict: correct,
and it independently re-derives our Phase-15 conclusion (M1–M6, P21).** One lemma (Lemma 2) has a correct conclusion
but a non-rigorous sub-proof (it reuses the discredited Gershgorin schema); we have a cleaner argument. Lemma 3 is
*literally* our Lefschetz dichotomy (M5). The bottom line matches our standing CAP/SURF map exactly.

---

## 1. Lemma-by-lemma audit and mapping to our results

| Advisor's lemma | Status | Our result it matches |
|---|---|---|
| **L1 (Spectral Abyss):** any $L$ built from $(\T,Q,J,\{s_k(p)\})$ is $F(\T,\mathcal K_{\mathrm{spec}})$, analytic in $\Gamma$. | ✅ correct | The **independence filter** (P21 Prop. 2.1 / M4 §0): spectral $L\in W^*(\T)$. $\T,Q,J$ are diagonal in the eigenbasis; anything built from them lies in the bimodule over $W^*(\T)$. |
| **L2 (Attempt-8 rigorized):** $\omega_{\mathrm{spec}}\succ0\iff$ RH. | ⚠️ conclusion ✅, **proof not rigorous** | The **determinacy** result (P21 Prop. 2.1, Attempt 8). But the advisor's steps 5–6 (Gershgorin domination, "the negative term cannot be compensated") **assume the conclusion** — they are the very $L=K/(\gamma_\rho-\gamma_\sigma)$ + Gershgorin schema we rejected earlier. The clean reason is **diagonality**, not Gershgorin (see §2). |
| **L3 (Integrality is definition, not consequence):** $h_\rho\in\mathbb Z$ ⟺ the $\sltwo$ integrates to a compact/discrete-series group = an ample polarization; it does **not** follow from the commutation relations. | ✅ correct | **Exactly the Lefschetz dichotomy (M5).** Our M4.2 built the principal-series $\sltwo$ (continuous $H$); M5 proved no Hodge–Riemann/lowest-weight form on it. The advisor's "integrates to $SU(2)$" = our "lowest-weight/integer grading," and his "geometric property not algebraic" = our "needs the ample class, LI-forbidden on the zeros." |
| **L4 (Yuan–Zhang inapplicable):** no $\mathcal X$ with $H^1_{\mathrm{arith}}(\mathcal X)\cong\HW^{\mathrm{prim}}$; YZ controls $\widehat{\mathrm{Pic}}^0$ (weight 0, heights), not weight-1 zeros. | ✅ correct | **Attempt 6 + M6.** Cites our own Attempt 6; M6 confirmed prismatically (Frobenius = local Satake/anatomy, weight grading is local & trivial for $\zeta$). |
| **Final Theorem:** no proof of RH in the current program; M3 is a reduction, not a proof. | ✅ correct | Our entire Phase-15 conclusion. |
| **Corollary:** the missing object is $\mathcal K_{\mathrm{geom}}\in\mathrm{Corr}^1(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z)$, postulated from geometry, not derived from anatomy. | ✅ correct (with one refinement, §3) | **SURF / Deninger–Connes–Consani**, the standing wall (M5/M6). |

## 2. The one soft spot: Lemma 2's proof (and the clean replacement)

The advisor's L2 writes $L_{\rho\sigma}=\mathcal K_{\rho\sigma}/(\gamma_\rho-\gamma_\sigma)$ and argues positivity by
Gershgorin diagonal dominance, concluding (step 5) that an off-line $\varepsilon_{\rho_0}=-1$ "cannot be compensated
without violating LI or convergence." **That step asserts the conclusion**: whether the negative term is compensated
is precisely RH. It is the same Gershgorin-positivity move from the team's earlier "proof schema" that we rejected as
circular.

**The conclusion is nonetheless right, for a cleaner reason — diagonality (our P21 Prop. 2.1).** In the eigenbasis
$\{e_\rho\}$, $Q=\mathrm{diag}(\varepsilon_\rho)$ and $J=\mathrm{diag}(\pm i)$. The *only* $(1,1)$-form compatible with
$(J,Q)$ is $\omega=Q(J\cdot,\cdot)$, whose positivity is $\varepsilon_\rho=+1\,\forall\rho$ = RH by the Weil
criterion. For a general spectral $L\in W^*(\T)$, the definiteness of $Q(JL\cdot,\cdot)$ is a function of the same
diagonal data $(\varepsilon_\rho,\gamma_\rho)$ and so cannot be **independent input** constraining the
$\varepsilon_\rho$ — it can only track, never force, the signature of $Q$. No Gershgorin/compensation argument is
needed, and none that assumes the answer should be used.

## 3. The refinement of the corollary: Frente 3 is the circular one

The advisor lists three fronts to build $\mathcal K_{\mathrm{geom}}$. Our filter + his own L3 sharpen the verdict:

- **Frente 1 (NCG/Connes — scaling generator on the adele class space)** and **Frente 2 (Shimura/Beilinson —
  $\widehat c_1(\mathcal L_{\mathrm{Eis}})$ on Borel–Serre)** are **genuine geometry**: $\mathcal K_{\mathrm{geom}}$ is
  defined *outside* the spectral algebra. These are the live targets — they can, in principle, supply an $L\notin
  W^*(\T)$ whose integrality comes from the geometry.
- **Frente 3 ("the unique operator satisfying $\sltwo$, $[\T,L]=\mathcal K$, *and* $h_\rho\in\mathbb Z$")** is
  **exactly the circular path** L1+L2 forbid: by **L3**, the integrality $h_\rho\in\mathbb Z$ is **not** an equation
  one can impose algebraically on a spectral $L$ — it is the geometric (ample/compact-integration) datum. Demanding
  it on a spectral construction is demanding RH. Frente 3 *alone* is not new math; it only becomes well-posed once
  Frente 1 or 2 supplies the geometric $\mathcal K_{\mathrm{geom}}$ whose grading is *then* found to be integral.

So the operative conclusion is **sharper** than the advisor's: only Frentes 1–2 (independent geometry) are live;
Frente 3 is the spectral tautology under a new name.

## 4. Status

- **Convergent confirmation.** An independent advisor re-derived our Phase-15 result: RH has **no proof inside the
  spectral data**; the obstruction is the geometric correspondence $\mathcal K_{\mathrm{geom}}$ over
  $\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$ (SURF/Deninger), independent of the
  spectrum. His L3 is our Lefschetz dichotomy (M5); his L4 is our Attempt 6 / M6; his final theorem is our standing
  map.
- **One correction logged:** L2's Gershgorin sub-proof is non-rigorous (assumes the conclusion); the determinacy
  result holds for the cleaner reason (diagonality, P21 Prop. 2.1).
- **One refinement logged:** Frente 3 (pure-algebra $\sltwo$ + imposed integrality) is the circular path his own L3
  forbids; only Frentes 1–2 (Connes scaling generator; Beilinson/Eisenstein class) are genuine new math.
- **No change of state.** This does not move us closer to or further from RH; it confirms, from a second independent
  derivation, exactly where the wall is and that new effort must be **geometric construction of
  $\mathcal K_{\mathrm{geom}}$**, not further spectral reformulation.
