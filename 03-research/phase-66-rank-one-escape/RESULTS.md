# Phase 66 — results log

## D1 (sharp dichotomy) — status: analytic content sound; clean numeric needs the faithful K_P

**What is sound (below RH, the easy direction ¬RH ⟹ unbounded escape):**
- An off-line zero ρ=β+iγ (β>½) is a *second escape direction* with growth λ^{2β-1}. This RATE is
  already validated in phase-64 **E101** (DH drift λ^{2β-1}, past-edge mass grows) and E107/E108.
- The sharp-dichotomy claim (boundedness ⟺ RH, no partial regime) rests on the off-line escape
  direction being **orthogonal to the pole direction H**, so P_prim (which removes only H) cannot
  absorb it. This is the phase-64 §5 framing ("second escape direction"); a fully rigorous proof of the
  orthogonality is the genuine new content and is NOT yet nailed.

**What failed / is inconclusive:**
- **E110** (`E110_escape_dichotomy.py`): a crude proxy — local Θ-Gram at a single height λ, with
  "remove pole = drop the top eigenvalue". Fit exponents came out noisy (ζ: +0.23, off-line β=0.7:
  −0.05) instead of ~0 and ~0.40. **Reason:** a single-height local Gram does not measure the
  cumulative escape norm sup_P‖P_prim K_P P_prim‖, and dropping the top eigenvalue is not the rank-one
  projection P_prim = I − |H⟩⟨H|/⟨H,H⟩. Proxy withdrawn as a measurement of D1. Not committed.

**Correct next step:** build the FAITHFUL canonical Gram
K_P = ∫ Y_P* dH_P Y_P (phase-64 `CANONICAL-FOUNDATION.md`, von Mangoldt Hamiltonian dH_p≥0), identify
the pole direction H explicitly, and measure the largest eigenvalue of P_prim K_P P_prim vs P for ζ
(bounded?) vs a planted off-line zero (growth λ^{2β-1}?). This is the real D2 detector; D1's clean
confirmation falls out of it.

**RESOLVED (E111, `E111_escape_norm.py`, `E111_RESULTS.md`):** built with the validated E101 proxy
(generalized spectrum L_pr x = μ L_arch x, mass past μ=1), pole direction H identified as the top
L_arch eigenvector (overlaps DC mode n=0 by 0.95–0.97; its mass grows ≈ linearly in log λ, matching
Tr K_P ~ ½(log P)²). Sanity check reproduces E101 digit-for-digit.
- **ζ: bounded.** After removing H, μ_max_prim ≡ 1.0000; N(P) at an O(0.1) float64 noise floor,
  fit exponent −0.05.
- **DH control: unbounded (fails as required).** N(P) grows 4.36 → 10.12 over λ=8→22. **Key structural
  confirmation for D1:** μ_max is essentially UNCHANGED by P_prim (5.356→5.357), i.e. the off-line
  escape direction is **orthogonal to the pole H** — P_prim cannot absorb it. This is exactly the
  sharp-dichotomy mechanism.
- Caveat: exponent not reliably pinned by the proxy (0.41–0.76, grid-dependent; μ_max saturates near
  10–11 for λ≥16 = finite-window ceiling). Only the **boundedness-vs-unbounded dichotomy** is robust.
  Proxy + criterion, not a proof; faithful transfer-matrix K_P remains the correct (unattempted) build.

## D3 (face A → MW-2) — done, see `D3-large-sieve-gap.md`
Face (A) = uniform sup-boundedness of the primitive partial sums of −ζ'/ζ on the critical line
(L∞-in-ξ, critical exponent); the classical large sieve gives only the mean square (= the pole/H
channel). The sup-vs-mean gap is MW-2. Faces (A),(C) → MW-2; face (B) → MW-5.

## Phase 66 net
CAND-1 sidesteps MW-1 (positivity is free) but its rank-one escape crux maps, on all three faces, to
the master walls (A,C→MW-2; B→MW-5). Genuinely below-RH content produced: **D1** (sharp dichotomy, the
easy direction, with the off-line ⊥ pole orthogonality numerically confirmed), **D2** (faithful-proxy
escape detector: ζ bounded / DH unbounded, robust), **D3** (precise identification face A = MW-2). These
are criteria/mappings, not a proof. The escape theorem itself remains RH-strength (phase-64, unbroken).

## Honest meta-note
The escape theorem itself is RH (phase-64, all three faces). Phase 66 targets only the below-RH pieces:
D1 easy direction (¬RH⟹unbounded, sharpness), D2 faithful detector, D3 large-sieve gap. Anything that
turns into MW-1 (positivity) or MW-5 (arithmetic site, face B) is logged and dropped.
