# Phase 178 — Fermionic interference and the sign gate

Tests whether a connected (CAR-algebra) fermionic cumulant between two "prime channels," or an
affine-commutator (Robertson-type) variant, can supply the fixed sign still missing from the
Euler–Poisson construction, after Petz recovery (phase 177) failed to do so.

## Results

- Among positive even gauge-invariant states on CAR(C²), the connected two-mode cumulant κ_ω(N₁,N₂) takes positive, negative, and zero values on explicit states — **PROVED** (Theorem 1): the obstruction already occurs for two fermionic modes and is independent of analytic details of the Weil form, so no fixed sign can come from this connected cumulant alone.
- The full (non-connected) covariance is positive — **PROVED** — but gives no oriented prime term — **REFUTED** as a source of orientation.
- The affine commutator produces the correct log p coefficient (citing P122_024) — **PROVED** — but the Robertson-type construction does not preserve the orientation of that commutator (real skew-symmetric structure forces the relevant expectation to vanish, or complex conjugation flips it) — **REFUTED**.
- Consequence stated as a necessary condition for any future mechanism: a successful interference mechanism cannot get its sign merely from state positivity, a connected cumulant, or a two-observable Gram determinant; it must prove an arithmetic restriction on the admissible joint state (excluding the anticorrelated state ρ₋) while retaining an oriented commutator term, using Λ⋆1 = log and Poisson–Tate jointly — status of that restriction: **OPEN**.
- No conclusion about row D is claimed either way.

## Documents

- `R178_FINAL.md` — the two-mode cumulant theorem and explicit counterexample states, the affine-commutator analysis, and a status map of what is proved/refuted/open.

## Relation to other phases

Follows phase 177's Petz-recovery NO-GO; its "necessary condition" for a sign mechanism is the direct premise tested (and found NO-GO, via a chain-complex nilpotence argument) in phase 179.
