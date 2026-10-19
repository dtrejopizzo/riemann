# Phase 16 — Constructing the SURF witness variety: triage, resonances, and the indefinite object

Phase 15 established that constructing an Arakelov witness variety 𝒳 (with a realization isomorphism
to the zero-carrying Kreĭn space) would imply RH. This phase's one task is to construct 𝒳, under a
strict acceptance specification (SURF spec sheet: a candidate must predict the zeros, not use them
as input). It triages three candidate geometric routes, drives the surviving one (the GL₂/Eisenstein
modular surface) through its pairing test, and then widens the search for any geometry carrying an
indefinite (Kreĭn/Pontryagin) pairing with the zeros as spectrum.

## Results

- SURF acceptance specification (four pillars: trace test, pairing test, integer grading, new Hodge index) fixed, with two corrections to the submitted spec logged — **working definition**, not itself a result.
- Pillar-1 triage of three candidate routes: Route C (global prismatic) **REJECTED** (Frobenius spectrum is local Satake, not the global zeros); Route B (δ/𝔽₁) **UNTESTABLE** (no constructed cohomology exists yet); Route A (GL₂/Eisenstein modular surface) **SURVIVES** (zeros provably appear as scattering resonances at Re(s)=1/4).
- Pillar-2 prototype on Route A: the regularized Maass–Selberg pairing genuinely carries the zeros and is indefinite and independent of them, but only as resonances, not L² eigenvectors — realization as a genuine Kreĭn space is the identified open core.
- Resonance residue weights are shown non-trivial, O(1), not decaying (**PROVED**), but the residue sign is **PROVED** not to be the sought κ-detector.
- An external Maass–Selberg–Zagier pairing proposal for Pillar 2 is audited and **REJECTED**: its proposed sign function does not distinguish on-line from off-line zeros, and the corrected computation shows the natural resonance pairing is Bochner-positive (definite), reproducing the program's wrong-sign capstone rather than Weil's indefinite form.
- Theorem: the modular-surface resonance pairing is negative-definite for every configuration of zeros (on- or off-line) — **PROVED** — so the off-line index κ is structurally absent from it, independent of RH; this closes Pillar 2 for Route A.
- A broader hunt for any geometry with intrinsic indefinite (Lorentzian/Pontryagin) signature carrying the zeros: a principle is established (indefinite signature is necessary) and a naive Lorentzian modification is shown to still fail (its sign is β-blind) — **NO-GO** within the structures tried; no indefinite geometric object found on the modular surface in any signature.
- The indefinite object is identified as already known: the de Branges/Pontryagin space H(E_ξ), with multiplication-by-z as Frobenius (spectrum = zeros) and Pontryagin index κ = off-line count — **PROVED** to genuinely detect κ by construction; proving κ=0 is exactly RH and equals the standing wrong-sign capstone (no new positivity supplied).
- Clean reformulation: RH ⟺ Re(ξ'/ξ(σ+iτ)) > 0 for σ > 1/2 (ξ'/ξ Herglotz in the right half-plane), with the unconditional boundary fact Re(ξ'/ξ)=0 on the critical line (functional equation alone, no RH) — **PROVED** as an equivalence; RH-equivalent, not a crossing.
- Self-adjoint/Weyl-function construction realizing this Herglotz criterion is set up precisely with two unconditional ingredients (unit residues, zero boundary value); the reality of its poles is identified as exactly the open step, reducing to the same uniform pair-correlation (RFB) frontier as prior phases — **OPEN**, explicitly not fabricated as solved.

## Documents

- `00-SURF-SPEC-SHEET.md` — acceptance criteria for the witness variety.
- `01-pillar1-triage-three-routes.md` — rejects Routes B and C, selects Route A.
- `02-pillar2-prototype-resonance-wall.md`, `03-residue-pairing-nontrivial.md` — Route A pairing prototypes.
- `04-MSZ-pairing-hits-CAP.md`, `05-resonance-pairing-definite-THEOREM.md` — audit of an external pairing proposal and the definiteness theorem closing Route A.
- `06-hunt-indefinite-object.md` — search for any indefinite geometry on the modular surface; negative result.
- `07-pontryagin-the-indefinite-object.md` — identification of H(E_ξ) as the (already known) indefinite object.
- `08-debranges-herglotz-clean-criterion.md`, `09-self-adjoint-construction.md` — the Herglotz reformulation and its self-adjoint-operator construction, ending at the RFB/uniform-pair-correlation frontier.
- `experiments/` — supporting numerical computations (Maass–Selberg density and residue-pairing verification).

## Relation to other phases

Direct continuation of phase 15's M9/M10 "construct the witness variety" directive; its final open step (uniform pair correlation / RFB) ties back to Phase 4's Problem B, and the de Branges/Pontryagin identification connects to P16 from an earlier phase.
