# Phase 64 audit (2026-06-28)

Critical re-check of all Connes-route results. Headline: the **qualitative picture is robust; the
marginal-positivity claims require high precision** (float64 is insufficient for the edge).

| exp | claim | audit verdict |
|-----|-------|---------------|
| E100 (A) | ζ Jacobi bounded, DH grows | holds qualitatively (bulk means: ζ≈0, DH≈+0.4); individual coeffs noisy (already flagged) |
| E101 (B) | ζ `μ_max=1`, DH drifts `λ^{2β−1}` | reproduces; ζ shows small `μ_max=1.031` excess at λ=11 →0 at λ=21 (**float64/finite-window artifact**, not a real violation); DH drift robust |
| E103 (C) | `φ=Ξ'/Ξ` Herglotz ⟺ RH | reproduces exactly: arch-only FAILS (+0.98), full ζ Herglotz (−0.009), off-line breaks (+9.55). Solid |
| **E104 (round 2)** | ζ Pick-PSD to ω=0; off-line fails at ω=β−½ | **CORRECTED**: float64 Pick eig is noise (cond ~1e16, min/max ≈ −1e-16). **High-precision dps=40 confirms genuine PSD** for ζ (min eig +5.4e-8→+3.1e-9 down to ω=0.01). Claim upheld; **dps≥30 required**. Threshold ω*=β−½ robust at any precision |
| E105 | Tate factorization ω>½, passive product | reproduces; refinement (passivity collective/matrix-level) stands |

## Main lessons

1. **Precision discipline:** the edge/marginal positivity for ζ is *genuine but small* (`~1e-7`–`1e-9`
   relative) and **float64 cannot resolve it** — the Pick/edge matrices are conditioned ~1e16 at the
   boundary. All marginal-positivity claims must be checked at **dps≥30**. The off-line *failures* are
   O(1) and robust at any precision.
2. **No over-claim survives:** every positive result for ζ is *marginal* (boundary `μ_max=1` / Herglotz
   with `max Im φ`≈0 / Pick min eig `~1e-8`), consistent with ζ sitting exactly at the de Branges
   boundary — i.e. these are faithful **detectors**, not proofs. This is stated everywhere; the audit
   found no place where a marginal result was mistaken for a strict one (after the E104 correction).
3. **Falsifier integrity:** DH / planted-off-line-zero breaks every test with O(1) margin and at the
   predicted location (ω=β−½, growth `λ^{2β−1}`), confirming the tests are genuinely discriminating.

## Net

The Connes-route findings stand after audit, with one precision correction (E104). The route is
validated end-to-end as a **faithful, falsifiable, marginal** criterion; the RH-strength step remains
the adelic passive-colligation continuation to ω=0 (theory). Nothing committed.
