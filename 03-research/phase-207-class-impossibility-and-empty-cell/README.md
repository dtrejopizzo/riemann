# Phase 207 — (1) Class impossibility theorem; (2) The empty-cell object

do both.
1. **Class impossibility.** Convert Φ200′ and the barriers (lem:transfer, Theorem X, BARRIER_D1 Thm 4, B_P from TOOLS_204U,
   quartets, thm:sos) into ONE theorem: "no continuous sign step on Λ, at weight n^{−1/2}, that uses the FE only as symmetry,
   can be positive on the polar orthogonal (the node from phase 206)". A tool, not a closure: it says what shape the object
   of (2) CANNOT have.
2. **Invent the empty-cell object** (SYNTHESIS §4 (ii); RIGID_001 Lemma N): a structure with positivity at weight n^{−1/2}
   and native symmetry s ↔ 1−s, in the same step. Known extremes: Helson's multiplicative Hilbert matrix (weight ½, no FE);
   automorphic norms (native FE, weight 1). A problem in its own right, without the window form in front.

Memos: CLASS_*.md (lead 1), CELL_*.md (lead 2), AUDIT_207_*.md.

## AUDIT_207_001 verdict
- Lead 1: Theorem A = P46 thm:geo-tv + cor:margin1 (CITED, tautological dichotomy; (H_ev) PROVED; (H_N) OPEN, min–max gives
  μ_N ≥ μ_∞). Theorem B = C2 at the node (PROVED, not new). Lemma 5: signature (1,1) in the even sector. (O1-iii) determinants/
  moments = W-det/W-mom (retry forbidden). Structural corrections: quartets and f_t do not falsify the node; with 𝔪 fixed the
  F coordinate has no falsifier ⇒ Φ200′ at the node = "E with 𝔪 fixed".
- Lead 2: Lemma G = classical Gonek; new reading: the J part of every weight-½ form = multiplicative Hankel Σ w(2πN)(a∗a)(N);
  with a = Λ and w ≥ 0 trivial and inherited (NO-GO, Lemma 207.A); with w indefinite and no mechanism, the main term falls
  outside the node's band (ARGUED). The node's window is not J-stable (PROVED).
- **Live gate (the only one):** premises that are a theorem only for log-derivatives of L with Euler product over ALL primes
  (not inherited by a_P), with margin ≤ e^{−15.449T}. No candidate. Row D OPEN.

## Other files in this folder

- `CELL_001.md` — Lead 2 of phase 207: the empty-cell object.
- `CLASS_001.md` — Lead 1 (phase 207): class impossibility theorem for the node's sign step.
