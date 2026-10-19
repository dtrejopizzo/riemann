# Phase 111 — Does the corner pairing converge on Schwartz-class data?

Phase 110 showed the ξ-divisible class is empty inside the compactly-supported test class (ADM), but
exhibited a Schwartz-class (non-compact) witness. Phase 111 asks whether the corner pairing I_∂ itself
(its polar terms, zero sum, and prime sum) still makes sense once the test class is widened to Schwartz
data, which is needed to keep requirement d1 (Riemann–Roch via a principal subspace) alive.

## Results
- Polar terms f̂(0), f̂(1) exist under explicit decay conditions on Schwartz data. PROVED.
- The zero sum Σ_ρ f̂(ρ)ḡ(ρ) converges absolutely on Schwartz data, by a large margin. PROVED.
- The prime sum Σ_n Λ(n)h(n)n^{-1/2} converges. PROVED.
- Phase 108's identity-shell finiteness constraint does not carry over to this setting, because the trace is renormalized differently here. ARGUED.
- The ξ-divisible class intersected with the convergent class is nonempty, modulo two linear conditions. PROVED.
- The structural reason both phases are consistent: ξ's growth is governed entirely by Γ (not ζ) and runs in opposite directions on the real axis versus the critical line — divergence along the real axis (kills compact support, phase 110) and convergence along the critical line (keeps the zero sum convergent here); both rates verified numerically against the closed-form predictions. PROVED, with numerical confirmation.
- The trace functional 𝔗, as currently constructed on a finite set of places tied to compact support, is not directly available on Schwartz data, since every prime power contributes for Schwartz h; the needed replacement (a convergence-based construction instead of finite-place stabilization) is identified but not built. OPEN (named as a construction task, not an obstruction).
- Headline verdict: "d1 is alive" — nothing found in this phase closes the Schwartz-class route; phase 110's impossibility and phase 111's convergence are different features of the same function, not in tension. PROVED (for the stated convergence claims) / OPEN (for the full construction of 𝔗).

## Documents
- `111_00_PHASE_111_PLAN.md` — the single question and its relation to phase 110.
- `111_01_CONVERGENCE_OF_THE_THREE_PIECES.md` (+ `.py`) — polar, zero-sum, prime-sum convergence.
- `111_02_THE_TWO_DIRECTIONS.md` (+ `.py`) — why phase 108's constraint does not carry over.
- `111_03_VERDICT.md` (+ `.py`) — the ξ-divisible ∩ convergent class, the open 𝔗-construction item, and the final verdict table.
- `111_99_PHASE_111_SUMMARY.md` — consolidated verdict, numerics, and confirmation against phase 107's own open-items list.

## Relation to other phases
Directly follows phase 110 (reopens the route phase 110 closed only for compactly-supported data); confirms against phase 107's own "still open" list that its remaining item matches requirements d1, d3, d4, d5 of the backward map; leaves the 𝔗-construction on Schwartz data as the next concrete task.
