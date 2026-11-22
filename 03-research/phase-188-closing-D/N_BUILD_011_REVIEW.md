# N_BUILD_011 — Review (independent referee, pen and paper)

Checked against Paper 46 main.tex (window form, P_T, prop:P, cor:Tarch l.2484, lem:wit-conc l.6937) and N_BUILD_001 (A),(B),(E).

## Sign of the polar term (crux) — CONFIRMED
Form 𝔞_T^{(λ)} = 𝔞_∞ − ∫Re c_F dλ (comb with minus sign). On P_T, N_BUILD_001 (A): ∫₀^{2T} c_F·2e^{u/2}du = −𝔭(F) ≤ 0.
Hence ρ_κ contributes −(−κ𝔭) = +κ𝔭 ≥ 0. Cross-check: κ = 1 reproduces N_BUILD_001 (B), m^♯ = m + 1/(¼+τ²); and the
main term of Λ is ρ_1 (dψ = dy, 2y^{-1/2}dy = 2e^{u/2}du). Consistent.

## Claim 1 (Pos convex; §1(i)) — CONFIRMED
b_T(λ) = inf over F of functionals affine in λ ⇒ concave; superlevel sets convex; intersection over T convex.
§1(ii) CONFIRMED. §1(iii) CONFIRMED (c_G ≥ 0 since g ≥ 0, the (1/16)c_G term enters favourably; c₀ depends on g, "absolute" = fixed g).

## Claim 2 (Theorem 1) — CONFIRMED, with a cosmetic FIX
Identity: exact (affine in λ, Plancherel). (⇐) trivial; uniform η_κ: on {m<0}, g_κ ≥ (κ−κ*)/(¼+τ²) ≥ (κ−κ*)/(¼+τ₀²);
on {m ≥ 0}, g_κ > 0, continuous, → ∞; inf > 0. b_T ≥ η_κ uniformly in T (Plancherel normalisation (1/2π)∫|F̂|² = ‖F‖²). OK.
(⇒): lem:wit-conc needs p continuous, even, polynomial growth: g_κ qualifies; F_T^γ ∈ P_T (§17, two integrations by parts),
so the Tate constraints are respected by construction; γ = 0 via the dilated family of §1(iii)/N_BUILD_001(E)(iii). OK.
κ* finite, κ* ≥ |C₀|/4 ≈ 1.343 > 1 consistent with m^♯(0) = C₀+4 < 0. OK.
FIX (cosmetic): self-review item 2 is garbled ("tends to 0 as |τ| → τ₀⁺? no —…"); replace by the argument above.

## Claim 3 (Corollary 2) — FIX (factor 2)
The removed piece is ∫₀^{log x₀} Re c_F·2κe^{u/2}du, |c_F| ≤ ‖F‖², and ∫₀^{log x₀}2e^{u/2}du = 4(√x₀−1).
Correct bound: b_T(λ_B) ≥ η_κ − 4κ(√x₀−1); hypothesis must read 4κ(√x₀−1) < η_κ. The conclusion (Pos ∋ λ_B for x₀ close to 1)
survives. Small-T case: for 2T ≤ log x₀ the comb is void in the window and b_T = λ_{∞,P}(T) > 0 iff T < T*_{∞,P} ∈ [0.58,0.60]
(cor:Tarch) — CONFIRMED; for T > ½log x₀ the main bound applies, so all T are covered. "Valid Beurling system" remains CITED and
is not used by the inequality.

## Claim 4 (Proposition 3) — CONFIRMED, minor FIX
Affinity in λ gives form(λ_t) = (1−t)form(ρ_κ) + t form(Λ) = (1/2π)∫g_{κ_t}|F̂|² − t𝓕_T. Concave t ↦ b_T(λ_t); it is also usc
(inf of affine), hence continuous on [0,1] including t = 1, so {b ≥ 0} = [0,t*] and Λ ∈ Pos_T ⟺ t* = 1 (needs this usc remark, add it).
|𝓕_T| ≤ (A_T+4)‖F‖² OK. FIX: the displayed intermediate bound "(1−t)η_κ − t(A_T+4)" omits the t(C₀+4) term; correct is
b_T(λ_t) ≥ (1−t)η_κ − t(A_T + 4 + |C₀+4|), which gives the stated final t* bound. Label: reformulation, as declared.

## Claim 5 (novelty) — CONFIRMED (corpus-relative)
grep 03-research, 04-papers for κ*, e^{u/2}du, "positive for all T", Beurling+positive: hits (R163_101, R164_102, R167_103,
R186_033/035) use 2∫Φe^{u/2} only as the PNT main term or Beurling systems as falsifiers; no prior construction of a comb with
b_T ≥ 0 ∀T and no threshold κ*. Novelty of Theorem 1/Cor 2 within the corpus stands. Mathematically elementary (one-line from (A)).

## Claim 6 (barriers) — CONFIRMED
Family is in the comb parameter, not in T: W-fam (window families) does not apply. Flowdet applies to any flow near t*(T); §4 is
correctly labelled a positive-start reformulation. No statement about Λ is made; no sign contact for Λ.

## Summary
Sign convention correct. Theorem 1 PROVED. Corollary 2 PROVED after FIX 2κ → 4κ. Proposition 3 PROVED after minor FIX
(intermediate bound; usc remark). §5 OPEN as stated. No downgrade.
