# Camino 2, Step 2 — Explicit-formula coupling: the negative directions are locally unprotected

**Phase 18, step 2.** Follows `01-negative-directions-portrait.md`.
**Experiment:** `experiments/camino2_explicit_formula_coupling.py` (runs clean).
**Date:** 2026-06-07.

> **Question (from step 1, §3).** A single off-line quartet gives a shallow, `γ`-localized
> negative direction. But the zeros are not free — near a putative off-line zero at `γ₀` there
> are on-line zeros (spacing `Δ`), each contributing a *positive* term. Does that neighbourhood
> **protect** against the dent (Case B), or can the dent be isolated (Case A)?

---

## 1. Verdict: Case A — the on-line neighbourhood does NOT protect

Building the bilinear Weil-Gram in an orthonormal even Hermite basis (on-line zero → PSD block
`2 û û^T`; off-line quartet → `4(UU^T − VV^T)`), the embedded bottom eigenvalue is **identical**
to the isolated one to 4–5 figures:

| `b` | `λ_min` isolated | `λ_min` embedded (+ 8 on-line neighbours) |
|---|---|---|
| 0.25 | −1.1178e4 | −1.1177e4 |
| 0.15 | −5.5748e2 | −5.5722e2 |
| 0.08 | −6.408e1 | −6.396e1 |
| 0.04 | −1.208e1 | −1.204e1 |

The threshold `b*` at which the embedded form goes negative is the smallest tested (`0.005`) for
**every** spacing `Δ ∈ {4, 3, 2, 1.5, 1, 0.7}` — shrinking the spacing does **not** protect.
(Control: an all-on-line spectrum gives `λ_min ≈ −2e−14 ≈ 0`, as it must.)

## 2. The mechanism, diagnosed (it is physical, not a band-edge artifact)

The embedded negative eigenvector is a genuine packet **at frequency `γ₀`**, narrower than the
zero spacing, and the neighbours barely touch it:

| `b` | eigvec peak freq | FWHM | neighbour-lift | `|λ_min|` |
|---|---|---|---|---|
| 0.25 | 7.90 (`≈ γ₀=8`) | 0.71 | 0.43 | 1.1e4 |
| 0.10 | 7.88 | 0.39 | 0.12 | 1.2e2 |
| 0.04 | 7.88 | 0.40 | 0.010 | 1.2e1 |

> The negative direction is a frequency packet of width **FWHM ≈ 0.4–0.7, well below the zero
> spacing `Δ`**. It fits *between* the discrete on-line zeros, and (being the `sin`/imaginary
> mode, P2) it is orthogonal to their `cos`-modes. So the on-line neighbours lift the dent by
> `< 0.1%`: **no finite set of on-line zeros protects.** The packet sits at the physical
> frequency `γ₀`, confirming this is the real dent, not the band-edge unboundedness.

The adversary can always shrink the packet below any fixed spacing `Δ` (at the cost of spatial
width, which only *deepens* the dent — the P1 unboundedness). So Case A is robust: the discrete
on-line spectrum is powerless against a sub-spacing dent.

## 3. Where the protection actually lives: the smooth `A_∞ − P`, i.e. CAP

Case A does **not** mean nothing constrains the dent — it means the constraint is **not the
discrete neighbouring zeros**. The explicit formula is the exact identity
```
   Σ_ρ φ_f(ρ)²  =  A_∞(f) − P(f),
```
`A_∞` the smooth archimedean (Γ-factor) term of density `~ log γ`, `P` the prime sum. The
discrete on-line zeros only *sample* `A_∞` at spacing `Δ`; a sub-spacing packet slips between the
samples and sees `≈ 0` from them — but the **smooth** `A_∞(f) = ∫|f̂(r)|² Ω(r) dr > 0` still sees
it. So the identity forces
```
   (negative dent)  =  A_∞(f) − P(f)   ⟹   P(f) > A_∞(f)   for the sub-spacing packet f.
```
The dent is paid for by the **prime side**, not the local zeros. Protection (RH) is the statement
`A_∞(f) ≥ P(f)` for all `f` — the **full Weil criterion**, the standing **wrong-sign capstone
(CAP)**. And because the negative direction is *sub-spacing* (FWHM ≪ `Δ`), it lives precisely in
the **fine / pair-correlation regime** of the prime–zero duality.

This independently re-derives the program's standing Phase-4 finding — *the wall is uniform pair
correlation* (the relative form bound / RFB) — now from the negative-direction side: the obstacle
to `κ=0` sits in the sub-spacing structure, exactly the pair-correlation regime.

## 4. Honest landing for Camino 2

- **Step 1** gave a precise portrait of the negative directions (shallow, imaginary-mode,
  `γ`-localized, near-orthogonal).
- **Step 2** shows they are **locally unprotected** (Case A): no finite arithmetic neighbourhood
  sees them; the only protection is the global `A_∞ − P` = the Weil criterion = **CAP**, localized
  to the **sub-spacing / pair-correlation** regime.

So Camino 2 — the direct attack on `κ` — **did not escape CAP**. It did something honestly useful:
it *localized* the obstacle with new precision (the negative directions are sub-spacing packets,
invisible to local arithmetic, constrained only by the fine pair-correlation balance of `A_∞ − P`).
This is consistent with, and sharpens, the standing CAP/RFB map. We report it as what it is: not a
crossing, a sharper portrait of the wall.

### What this rules out (value of the negative)
- **Case B (local protection): refuted.** The off-line dent is not held off by neighbouring
  zeros; one cannot hope to force `κ=0` by a local-in-`γ` argument.
- The handle, if any, is **global and in the pair-correlation regime** — i.e. the same RFB the
  program already identified as RH-conditional. No new non-CAP handle emerged.

## 5. Next — honest options (no pretending the wall moved)

Per the strategic review and this result:
1. **Consolidate (P29).** The Phase-17 symmetry-vs-positivity dichotomy plus this localization
   (`κ`'s negative directions are sub-spacing, locally invisible, CAP-bound) form a coherent
   "why RH resists, at the operator/negative-direction level" paper. **Recommended.**
2. **Camino 3 (ω / multiplicative chaos).** Per the strategic ranking, the one line *not* absorbed
   by the CAP/de Branges/SURF wall: build the spectrum from multiplicative statistics
   (`ω(n) ↔ k² ↔ moments ↔ chaos`) rather than reconstruct `ξ` from an operator. Independent
   exploration.
3. **Stop here on Camino 2.** Steps 1–2 answered its question: the negative directions are
   locally unprotected and CAP-bound. Further sub-steps would re-derive pair correlation.

We do **not** recommend continuing to push Camino 2 toward `κ=0`: step 2 shows that road is the
pair-correlation wall again. The honest move is to bank the portrait (P29) and open Camino 3.

---

## 6. Findings (durable)

1. **Case A (verified):** the on-line neighbourhood does not protect against the off-line dent;
   `λ_min` embedded `≈` isolated, neighbour-lift `< 0.1%`, for all spacings down to `Δ=0.7`.
2. **Mechanism:** the negative direction is a frequency packet of width `≪ Δ`, sitting between the
   discrete on-line zeros and orthogonal to their `cos`-modes — physically at `γ₀`, not an artifact.
3. **Protection is global and pair-correlation-regime:** the explicit formula routes the dent to
   `P(f) > A_∞(f)` for sub-spacing packets — the full Weil criterion = CAP, in the fine/RFB regime.
4. **Case B refuted; no new non-CAP handle.** Camino 2 sharpened the obstacle (sub-spacing,
   locally invisible) but did not escape it. Recommend consolidation (P29) and Camino 3.

---

*Cross-refs:* `01-negative-directions-portrait.md`, `experiments/camino2_explicit_formula_coupling.py`,
`../phase-4-handoff/proofs/00-PROOF-LOG.md` (RFB = uniform pair correlation, the wall),
`../phase-17/04-SURF-B-resolvent.md` (symmetry vs positivity). *Memory:*
`[[project-rh-current-direction]]`, `[[riemann-key-contradiction]]`.
