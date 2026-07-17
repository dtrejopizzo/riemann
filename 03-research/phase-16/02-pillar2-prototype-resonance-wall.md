# Phase 16 · Pillar-2 prototype (Route A) — the Eisenstein pairing carries the zeros, but they are resonances

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Pillar-1 triage left Route A ($GL_2$/Eisenstein) as the only live route (zeros present as scattering resonances).
The Pillar-2 prototype tests whether the natural Eisenstein pairing reproduces the Weil form $Q$. Result: the
regularized Maass–Selberg pairing **genuinely contains the zeros** (its density is the modular-surface explicit
formula), is **indefinite** (passes 2.2), and is **independent** of the zeros (passes P21) — but the zeros enter as
**resonances at $\operatorname{Re}(s)=1/4$, not $L^2$ eigenvectors**, so there is no honest Gram matrix on a discrete
zero-basis. Pillars 1 and 2 both reduce to a single open core: **realize the resonances as a Kreĭn space** (the
Beilinson realization), now located precisely.

---

## What was computed (`experiments/pillar2_maass_selberg.py`)
1. **The Eisenstein density is the modular-surface explicit formula.** On the continuous spectrum $s=\tfrac12+it$,
   the Maass–Selberg density is the scattering phase derivative
   $$
   -\frac{\varphi'}{\varphi}\Big(\tfrac12+it\Big)=-2\Big[\tfrac{\xi'}{\xi}(2s-1)-\tfrac{\xi'}{\xi}(2s)\Big],
   $$
   verified to $10^{-25}$. Since $\xi'/\xi$ has the $\zeta$-zeros as poles (Hadamard $\xi'/\xi(2s)=\sum_\rho\frac1{2s-\rho}+\cdots$),
   **the zeros govern the density.** This is the explicit formula of the modular surface. The scattering matrix
   $\varphi=\xi(2s-1)/\xi(2s)$ is defined from $GL_2$ representation theory alone — **no zeros used as input** ⟹ passes
   the independence filter (P21).
2. **The density is real and indefinite (in its fluctuation).** $-\varphi'/\varphi$ oscillates around the smooth Weyl
   term (e.g. $0.84$ at $t=14.13$ vs Weyl $3.0$; $5.1$ at $t=15$ vs $3.1$) — the fluctuation **is** the zeros. The
   pairing is therefore signature-$(1,\infty)$-type, **passing Pillar 2.2 and the heights filter** (it is not an
   unconditionally positive-definite height pairing — unlike the naive Arakelov route D2).
3. **The zeros are resonances, not $L^2$ eigenvectors.** They sit at $s=\rho/2=\tfrac14+i\gamma/2$, i.e.
   $\operatorname{Re}(s)=1/4$, **off** the $L^2$ spectrum of the modular Laplacian (continuous on $\operatorname{Re}=1/2$
   plus discrete Maass at $\operatorname{Re}=1/2$). They are poles of the meromorphically-continued scattering matrix.

## Arbiter verdict on Route A
Pillars 1 and 2 are **structurally met but not realized**, and both collapse to one wall:

| Pillar | Status on Route A |
|---|---|
| 1 (spectrum) | zeros present as resonances $s=\rho/2$ (verified); but not a clean *simple $L^2$ Frobenius spectrum* — entangled with the continuum + Maass |
| 2 (pairing) | the Maass–Selberg density is indefinite, independent, and carries the zeros; but it lives on the continuous line, **no Gram matrix on a discrete zero-basis** |
| 2.2 / heights filter | **passed** (indefinite, not a height pairing) |
| independence (P21) | **passed** ($\varphi$ is pure $GL_2$, zeros are output) |

> **The single open core (Beilinson realization, located precisely):** realize the resonances $\{s=\rho/2\}$ (poles of
> $\varphi$) as honest vectors of a Kreĭn/Pontryagin space $H^1_{\mathrm{Eis,prim}}$, with $\operatorname{Frob}$ of
> spectrum $\{\gamma_\rho\}$ and the regularized pairing equal to $Q$ (signs $\varepsilon_\rho$, negative index
> $\kappa$). Then Pillar 1 (clean spectrum) and Pillar 2 (Gram $=Q$) both close, and only the new Hodge index
> (Pillar 4) remains.

## Why this is the right, honest terminus of the prototype
- Route A **does not fail**: it concentrates the *entire* difficulty of RH into one well-defined, recognized problem —
  the **resonance realization** of the $\zeta$-zeros on the modular surface. The zeros provably appear; the pairing is
  provably indefinite and independent; only their realization as a Hilbert/Kreĭn space is missing.
- That the zeros are **resonances, not eigenvalues**, is exactly why Hilbert–Pólya has not been realized this way
  (Zagier; quantum-chaos literature on the modular surface). It is a recognized wall, not a technical gap.
- This sharpens M10's one-directional theorem to a concrete locus: $\exists$ resonance realization (Kreĭn space of the
  modular-surface resonances with pairing $Q$) $\Rightarrow$ Pillars 1–2 $\Rightarrow$ (with a new Hodge index)
  $\Rightarrow$ RH. The converse is still the open Hilbert–Pólya dream.

## Next options (honest)
1. **Consolidate** Phase-16 (the triage + this prototype) into a short note/paper: *"RH via the modular surface reduces
   to the Kreĭn realization of the $\zeta$-resonances"* — a clean conditional result with the three rejection filters.
2. **A Route-A-only Lise Science probe** aimed at the resonance realization (complex scaling / Pontryagin space of
   resonances; the regularized residue pairing $\operatorname{Res}_{s=\rho/2}\varphi$ as candidate $\varepsilon_\rho$),
   with the heights/independence/citation filters as gates.
3. **Stop**: the map is complete and the wall is located precisely; no non-circular passage is in hand, and the honest
   state is "$\exists$ resonance realization $\Rightarrow$ RH", open.
