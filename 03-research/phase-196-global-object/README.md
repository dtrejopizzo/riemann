# Phase 196 — the missing global object

Mandate: invent a GLOBAL object that sees the primes `n < e^{2T}` and the functional equation at once, does not split
over places, keeps the additive structure of ℤ, couples to `𝔞_T` on `𝒫_T` by an exact/one-sided relation that is not a dual
certificate, has free ℤ-specific positivity, and separates Λ from `a_P`, `cΛ`, Beurling. Memos (no audit yet).

| file | object | outcome |
|---|---|---|
| `INV_V_001_HEISENBERG_HECKE_WINDOW_AND_SHA_FORM.md` | algebra `𝔅 = C*(τ_1, M_1, δ_n)` on `L²(ℝ)` (rational Heisenberg ⋊ ℚ^×); Ш-form on Hecke vectors | 𝔅 non-factorizable (PROVED); `𝔞_T` an exact vector state (PROVED); Ш-positivity = Schur product of Euler factors of `ζ(1+iu)` (PROVED): Poisson on ℤ read through Mellin *is* the Euler product at σ=1. NO-GO 𝒦_Ш. |
| `INV_V_002_AFFINE_NEAR_COINCIDENCE_AND_CHEBYSHEV_TRANSFER.md` | affine near-coincidence form `𝔄ff_T` (shifts `0<|a|<e^T(1+1/n)`); Hecke–Chebyshev transfer `V^*Ш = 2 log|x|·Ш` | exact split `𝔞_T = A_∞ + ½𝔄ff − ½Re⟨Vf,f⟩_Ш` (PROVED, non-diagonal); transfer separates Λ from all falsifiers (PROVED) but **Chebyshev rigidity** (PROVED): exact transfer forces rank one ⇒ no Hermitian lift. Residues (G1) approximate eigen-kernels OPEN, (G2) affine one-sided inequality REF-D/OPEN. |

No sign. Index entry: `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md`, section "Fase 196".
- `AUDIT_196.md` (+ `audit196_v2_split_check.py`, NUMÉRICO): V1.1/V1.3a/V2.1/V2.3/V2.4 PROVED (V2.1 checked 1e−12 at T=0.6); V2.2(c) FALSE (split and transfer hold for every lattice αℤ); V1.4 subsumed (B″/I2); G2 = 𝔞_T≥0 rearranged; G1 inside N_018∪I4. No sign.
