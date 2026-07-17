# MW-5 crossing attempt — V₊ positivity margin (E95, E96): NO-GO, the wall confirmed

**Date:** 2026-06-26 · Phase 62 · follows E94 (quaternionic Hodge–Riemann positivity present but gapless).

## Goal

E94 found ζ's Weil matrix is positive-semidefinite on V₊ but **gapless** (margin → 0). The crossing
question: can the V₊ positivity be given a uniform `e^{−cL}` gap from the **prime/Euler side**,
with no zero locations? If the cascade rate `c` is prime-derivable and the positivity non-circular,
that would cross the master wall.

## E95 — origin of the cascade

- **Cascade rate is a λ-independent structural constant** for ζ: ≈ **1.40 log10/step** (~25× per
  mode) across λ=7…21. DH has no clean cascade (rate ~0.2, erratic).
- **No near-cancellation:** `(‖Larch|₊‖+‖Lprime|₊‖)/‖A|₊‖ ≈ 1.7–2.4` (order 1). ζ's PSD-ness is
  **intrinsic**, not a delicate subtraction. Good — but it means the smallness of the deep modes is
  a real spectral fact of `A|V₊`, not numerical.
- `ev_min` itself is erratic (hits the numerical floor); the **rate** is the robust quantity.

→ The cascade *shape* (rate) is structural/prime-like, but this does **not** explain the PSD-ness
(why there are no negatives). The rate is not the obstacle; the sign is.

## E96 — is it an Euler comparison?

Tested `A|V₊ ⪰ 0 ⟺ max μ ≤ 1` for the generalized eigenproblem `Lprime x = μ Larch x`.

- **Correction:** `Larch` is **not** identical for ζ and DH (max|diff| = 1.6; DH has a different
  conductor/Γ-factor). So the clean "same archimedean, compare prime forms" mechanism does not hold.
- **Result:** `max μ = 1.0000` **exactly** for ζ at every λ; DH gives `max μ ∈ [6.4, 13.5]`.
  So ζ is *exactly marginal* (PSD with a zero mode), DH badly violates. But the ζ kernel is large
  and grows (5→12 modes), so **many μ pile up at 1 from below** — the gapless cascade re-expressed
  in μ-space.

## Verdict — NO-GO: every reformulation is a gapless marginal detector = the master wall

Three independent reformulations of the positivity were tried in Phase 62:

| route | quantity | ζ | DH | status |
|-------|----------|---|----|--------|
| C1 Cesàro | `b_bulk(λ)` bounded | yes | grows | RH-equivalent (off-line → growth) |
| E94 Hodge–Riemann | `A|V₊ ⪰ 0` | yes (gapless) | indefinite | detector, gapless |
| E96 Euler/μ | `max μ ≤ 1` | =1 exactly | >1 | detector, marginal |

All three are **faithful detectors** (hold ⟺ RH; DH always fails) and all three are **gapless /
marginal** — the positivity sits exactly at zero margin, with the deep modes cascading to it. This
is the master wall (`ε₀(λ) ≥ 0`, Step 12) seen from three sides. None supplies a zero-free lower
bound, because at the margin the distinction "PSD vs not" *is* the distinction "zeros on line vs
not" — proving the margin ≥ 0 with a gap is proving RH.

**The crossing fails for the structural reason the program has documented as the master wall:**
the finite-window object carries the correct positive structure marginally, but giving it a uniform
gap requires the input that only a genuine cohomological realization over Spec ℤ (MW-5,
Connes–Consani arithmetic site / Deninger's conjectural Weil cohomology) would provide — and that
realization is exactly what does not yet exist. Numerics cannot manufacture it.

**No false victory:** μ_max=1 and `A|V₊⪰0` for ζ are real and reproducible, but they are marginal
detectors, not a proof. Phase 62 closes here: the Cesàro and Hodge–Riemann levers are exhausted as
*proof* routes. Recommendation: open a new phase to plan a genuinely different road (the geometric
realization frontier, or a different object), since brute-force on the finite window keeps
returning the same gapless wall.
