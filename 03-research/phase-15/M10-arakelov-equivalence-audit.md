# Phase 15 · M10 — Audit of the advisor "Arakelov–RH equivalence" theorem

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
The team submitted a "final rigorous theorem": RH ⟺ existence of an Arakelov witness variety $\mathcal X$ (a regular
arithmetic variety with an ample class and a realization isomorphism $\Phi: H^1_{\mathrm{arith}}(\mathcal X)_{\mathrm{prim}}
\xrightarrow{\sim}\HW^{\mathrm{prim}}$ intertwining Frobenius with $\T$ and the Arakelov pairing with $Q$ — "Axiom 3").
**Verdict: the operational conclusion is correct and matches M9/Attempt 6; but the claimed biconditional is
overstated. The forward direction ($\mathcal X\Rightarrow$ RH) is a correct near-tautology; the reverse (RH $\Rightarrow
\mathcal X$) is NOT rigorous and may be false. The honest statement is one-directional.**

---

## Part I ($\mathcal X\Rightarrow$ RH) — correct, but near-tautological (= Attempt 5)
Granting Axiom 3, Yuan–Zhang / Faltings–Hriljac give $\langle x,x\rangle_{\mathrm{Ar}}>0$ on primitives; transport by
$\Phi$ gives $Q\succ0$ on $\Pi^\perp$; hence $\kappa=0$, RH. This is valid **but all the content sits in Axiom 3**: it
assumes $\HW^{\mathrm{prim}}$ is isometric to exactly the space where the arithmetic Hodge index is definite (the
codim-1 adelic line bundles / $\widehat{\mathrm{Pic}}^0$). Whether such an isometry can exist — i.e. whether the
**zeros** are the relevant Arakelov eigenvalues rather than the **heights** — is precisely Attempt 6 / the unbuilt
surface (SURF). So Part I restates, rigorously, what Attempt 5 already established: *the Hodge index theorem exists;
the obstruction is the witness variety.* Correct, not new.

## Part II (RH $\Rightarrow\mathcal X$) — NOT rigorous, and possibly false
The argument: RH $\Rightarrow Q\succeq0\Rightarrow$ (M3) an integer-graded hard-Lefschetz $\sltwo$ with $\omega\succ0
\Rightarrow$ a polarized weight-1 Hodge structure $\Rightarrow$ (realization philosophy / Standard Conjectures) a
motive $M/\mathbb Q\Rightarrow$ a regular model $\mathcal X$. Three defects:

1. **Conflates $Q\succeq0$ with "integer-graded $\sltwo$ exists."** M3 gives RH $\iff Q\succeq0$; the *hard-Lefschetz*
   version (RH $\Rightarrow$ an integer-graded $\sltwo$ raising operator exists on $\HW^{\mathrm{prim}}$) is **not**
   proven and directly conflicts with the **Lefschetz dichotomy (M5)**: on the LI zero-spectrum no integer-graded
   $\sltwo$ exists, RH or not. So step 1–2 assumes a structure we proved cannot live on the spectral model.

2. **Applies finite-dimensional motivic realization to an infinite-dimensional object.** $\HW^{\mathrm{prim}}$ is
   infinite-dimensional with Frobenius spectrum $=\{\gamma_\rho\}$ (dense, conjecturally LI / transcendental). The
   realization philosophy (Standard Conjectures, Fontaine–Mazur, Nori) is about **finite-dimensional** motives; no
   finite motive has the $\zeta$-zeros as Frobenius eigenvalues (they are not Weil numbers of any variety). Asserting
   "the polarized structure defines a motive" therefore **assumes precisely the open problem** (that the zeros are
   motivic Frobenius eigenvalues) — it is mildly circular.

3. **Deepest: the zeros may have no geometric realization at all.** It is an open possibility that RH is true while
   the zeros are the spectrum of a **non-geometric / non-motivic** operator (a Hilbert–Pólya operator with no
   underlying variety). In that case RH holds and $\mathcal X$ **does not exist** — so the implication RH $\Rightarrow
   \mathcal X$ would be **false**. Nothing in M1–M9 rules this out; M5/M6 (continuous spectrum, local-not-global,
   no integer grading) are weak evidence *against* a classical geometric realization.

**Consequence.** The biconditional "RH $\iff\mathcal X$" is **not** established. What is true and useful is the
**one-directional sufficient condition**:
$$
\boxed{\ \exists\,\mathcal X\ \text{(witness variety, Axiom 3)}\ \Longrightarrow\ \RH.\ }
$$
The converse is a heuristic expectation (the Hilbert–Pólya/Deninger dream), not a theorem, and possibly false.

## Why this matters operationally
- **Do lean on:** $\mathcal X\Rightarrow$ RH. Constructing the witness variety would prove RH. This is a legitimate,
  well-defined proof strategy — the state of the art (Deninger/Connes–Consani made precise), and exactly the Route-A
  target from M9.
- **Do NOT lean on:** "RH $\Rightarrow\mathcal X$, so $\mathcal X$ must exist." That guarantee is not real. If the
  geometric route proves intractable, it does not follow that we are missing an existing object; the zeros may simply
  not be geometric, and RH (if true) would then need a non-geometric proof — which is where the analytic side of the
  program (the sub-RH results P17, the localized Weil form) remains the honest fallback.

## Bottom line
The team's directive — *stop writing "proofs of RH"; the one task is to construct $\mathcal X$ (the Beilinson
realization of the $\zeta$-zeros) via Shimura/$GL_2$, $\delta$-geometry/$\mathbb F_1$, or the cyclotomic/Eisenstein
tower* — is **correct and well-aimed**, and matches M9's "next probe = Route A deep." The only correction: it is a
**sufficient** strategy ($\mathcal X\Rightarrow$ RH), not a proven equivalence; the reverse direction is the
Hilbert–Pólya conjecture, open and possibly false. Build $\mathcal X$ to prove RH — but without the false comfort
that its existence is guaranteed.
