# Phase 16 · Hunting the indefinite object — the principle, and an honest negative

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
P22 proved the modular-surface resonance pairing is definite (half-plane Hardy kernel). The hunt: find a geometry
whose natural pairing is *indefinite* and carries the zeros, so that $\kappa$ (the off-line index $=$ RH) can live in
it. Result: a **principle** (the geometry must have intrinsic indefinite signature — Lorentzian/Pontryagin, not
Riemannian), an **honest negative** (a naive Lorentzian modification of the modular resonances stays definite), and a
short list of genuine candidate geometries with rationale. No indefinite object found; the *type* is characterized.

---

## The principle (solid, from P22)
P22's definiteness came from the kernel $1/(s_\rho+\overline{s_\sigma}-1)$ being the Cauchy/Hardy reproducing kernel
of a half-plane — a consequence of the modular surface being **Riemannian** ($K=SO(2)$, positive-definite Petersson
inner product). The conjugate $\overline{s_\sigma}$ forces the half-plane and hence definiteness.

> **Principle.** A geometry whose $L^2$/Petersson structure is a Hilbert space (Riemannian, $SO(2)$) yields a
> *definite* resonance pairing and cannot host $\kappa$. **An RH-carrying form requires a geometry with intrinsic
> indefinite signature** — a Lorentzian ($SO(1,1)$) / Kre\u\i n / Pontryagin structure, where a positive- and a
> negative-norm sector coexist. This is consistent with the program: the Weil form $Q$ is Kre\u\i n (indefinite);
> M2's ample cone is the hyperbolic plane $\mathrm{II}_{1,1}$; P16 is the Pontryagin index.

## The honest negative (a naive Lorentzian modification fails)
Tested whether replacing the Riemannian Petersson pairing by a **Klein–Gordon** one — splitting each Eisenstein
resonance into its $y^s$ ("$+$frequency") and $y^{1-s}$ ("$-$frequency") cusp components and assigning them opposite
signs — produces an indefinite form on the modular resonances. **It does not:** the $2n\times2n$ Gram matrix is still
sign-definite ($+0/-12$ for $6$ zeros; `hunt_indefinite_lorentzian.py`). The reason: both the $+$ and $-$ frequency
blocks reduce to half-plane Hardy kernels (the $y^{1-s}$ component sits at $\Real(1/2-s)=1/4>0$ too), so the naive
sign-flip joins two definite blocks rather than creating a genuine $(+,-)$ signature. **Manufacturing the
indefiniteness is not a trivial modification of the modular surface.** Honest: the indefinite object is *not* in hand.

## Genuine candidate geometries (with rationale, for the next phase)
1. **The Lorentzian / split modular space $SL_2(\mathbb Z)\backslash SL_2(\mathbb R)/SO(1,1)$** (the space of geodesics
   / an anti-de Sitter analogue). Here the invariant pairing is the Klein–Gordon / wave-operator form, **indefinite by
   the signature of the symmetric space** — not by an ad hoc sign-flip. The same scattering $\varphi$ should carry the
   zeros, but with a genuinely indefinite inner product. *Rationale: the indefiniteness is structural (geometry's
   signature), the one ingredient P22 shows is required and the modular surface lacks.* The open task is to build the
   $SO(1,1)$ spectral theory and check the resonance signature.
2. **The de Branges / Pontryagin space $H(E)$ with $E$ the structure function of $\zeta$** (P16's object). The
   Pontryagin index $\kappa$ = number of zeros of $E$ in the wrong half-plane = off-line zeros, **by construction**.
   This is the canonical latent-indefinite object; the open part is its geometric realization (carrying a Frobenius).
3. **Deninger's foliated dynamical system** with an indefinite leafwise form — the conjectural geometry where the flow
   has the zeros as spectrum and the cohomology pairing is indefinite. Conjectural, not computable yet.

## The Lorentzian lead, executed — also fails (the decisive negative)
Computed the genuine Lorentzian $SO(1,1)$ pairing: the **Klein--Gordon symplectic current** of two Eisenstein modes
$f=y^{1-s_\rho}$, $g=y^{1-s_\sigma}$ on a Cauchy surface $y=\mathrm{const}$,
$j=i(\bar f\,\partial_y g-g\,\partial_y\bar f)$. Its diagonal self-norm is
\[
\mathrm{KG\text{-}norm}(\rho)\ \propto\ i(\overline{s_\rho}-s_\rho)=2\,\Imag(s_\rho)=\gamma_\rho .
\]
**It depends only on $\gamma$ ($=\Imag$), and is completely blind to $\beta$ ($=\Real$)** — identical ($=20.0$) for
$\beta=0.3$ and $\beta=0.7$ at fixed $\gamma$ (`hunt_KG_current.py`). The Lorentzian pairing detects upper/lower
($\sgn\gamma$ = complex-conjugate symmetry), **not** on/off-line ($\beta=\tfrac12$). It does **not** detect $\kappa$.

**The unified negative.** Across all three natural Eisenstein pairings the off-line detector $(\beta-\tfrac12)$ is
never produced:
\[
\text{Petersson (Riemannian)}\sim(1-\beta)\ \text{[definite]};\quad
\text{bilinear Kre\u\i n}\sim\tfrac1{1-\beta}\ \text{[definite]};\quad
\text{Klein--Gordon (Lorentzian)}\sim\gamma\ \text{[}\beta\text{-blind]}.
\]
None is the off-line measure. The $\kappa$-detector $(\beta-\tfrac12)$ is robustly **not a pairing of resonances** —
it is the off-axis evaluation functional (P22), which no bulk or Cauchy-surface pairing on the modular surface, in any
signature, realizes.

## Status (honest)
- **Found:** a structural principle (indefinite signature is necessary, P22), **and** a unified negative — the
  off-line detector $(\beta-\tfrac12)$ is produced by *no* natural Eisenstein pairing (Riemannian, bilinear, or
  Lorentzian). The Lorentzian lead, executed, is $\beta$-blind ($\propto\gamma$).
- **Not found:** the indefinite object. The modular surface, in *any* signature, cannot carry the off-line index via
  a resonance pairing. The indefiniteness genuinely lies outside it — in the off-axis evaluation / the missing
  arithmetic surface (SURF).
- **Honest terminus of the geometric hunt on the modular surface:** Route A supplies the zeros (Pillar 1) but
  provably not the indefinite $Q$ (Pillar 2), now confirmed across Riemannian and Lorentzian structures. The genuine
  indefinite object — Pontryagin $H(E)$ with a *Frobenius*, or Deninger's foliated cohomology, or SURF — is not on
  the modular surface and is the open core, not a computation in hand.
