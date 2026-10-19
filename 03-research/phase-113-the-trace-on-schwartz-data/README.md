# Phase 113 — The trace on Schwartz data, and the four-row ledger

Phase 111 found all convergence questions for the corner pairing fine on Schwartz data but flagged
that the finite-place stabilization used to define the renormalized trace does not exist there. This
phase builds the trace directly for Schwartz data by summing local integrals over all places, then
uses the resulting structure to push through as much of row (d)'s Riemann–Roch programme (six
requirements d0–d5, plus the vanishing of the canonical class K) as the construction allows.

## Results
- The identity-value condition h(1)=0 from phase 108 is shown to be a canonical-scheme-agreement condition rather than a forced constraint, and then shown unnecessary once the pairing is rewritten in a canonical Weil decomposition on a balanced profile class D. PROVED.
- A commutative Frobenius *-algebra (D/rad, ⋆, *, τ) is built: a zero-free trace τ with 𝔰(x,y)=τ(x⋆y*); two rulings realized by explicit functions (Riemann's Φ±2Φ'); a Z-valued degree map; an effective cone; and the canonical class K=0. PROVED.
- Requirement d0 (degree map killing the radical) and d5 (effective cone) are built. PROVED.
- Requirement d1's analytic half is closed: rad I_∂ equals the χ-ideal, χ(s)=s(s−1)ξ(s). PROVED.
- Requirement d2 (a polarization H with H²>0): H²=2, H effective. PROVED.
- Requirement d3 (Riemann–Roch with a quadratic D² term): proved impossible inside D, since the divisor group is a complex vector space under which the effective cone is scaling-stable (h⁰(nD)=h⁰(D) for all n, checked at n=2,5,100). NO-GO.
- Requirement d4 (Serre duality / h² vanishing): built unconditionally, including discharging an interpolation gap via an explicit closed-form construction. PROVED.
- Three independent obstructions (O1–O3) are proved, each showing there is no lattice structure inside D: scaling-stability of the effective cone (O1), divergence of the pairing on point masses δ_n (O2), and absence of any spectral gap on D°\rad (O3). PROVED (each a standalone no-go, closing different possible escape routes).
- The remaining requirement — an effectivity statement (E°) together with a Hodge-index inequality on H^⊥ — is left OPEN; the documents identify it as equivalent to a classical, long-standing conjecture about the location of ζ's zeros. That equivalence itself is not elaborated here per standing project rule; (E°) is reported strictly as OPEN.
- Numerical cross-check: Weil positivity measured directly from the primes at four probes agrees with the construction to ≤4e-15. NUMERICAL (consistency check only).

## Documents
- `113_00_PHASE_113_PLAN.md` — the single remaining analytic gap in d1 and the pre-registered refutation criteria.
- `113_01`–`113_04` (+ `.py`) — the identity-value condition, prime-sum convergence, trace well-definedness, and the d1 construction-gap verdict.
- `113_05`–`113_09` (+ `.py`) — canonical conventions, the Weil decomposition, the class D, the identity functional as a norm, the two rulings and the index engine, and the radical/χ-ideal identification.
- `113_10`–`113_12` (+ `.py`) — the degree map and effective cone, the impossibility of d3 inside D, the trace/duality/K=0 results, and the effectivity/Hodge-index statement left open.
- `113_13`–`113_14` (+ `.py`) — the three obstructions O1–O3, and the discharge of two analytic gaps (separating family, interpolation).
- `113_15_THE_FOUR_ROW_LEDGER.md` (+ `.py`) — the audited status of every requirement, with mechanical citation checking.
- `113_99_PHASE_113_SUMMARY.md`, `113_99_verify_all.py` — consolidated verdict and full verifier suite.

## Relation to other phases
Directly continues phases 110–111 (resolves the trace-construction gap phase 111 flagged); builds on phase 108's graded family and phase 107's divisor/pairing framework; closes d0, d2, d4, d5 and K=0 as new results, closes d3 as impossible inside the class D, and leaves d1's remaining effectivity statement open for later phases, with the obstructions O1–O3 constraining what any future integral/lattice structure (rows a, b) would need to supply.
