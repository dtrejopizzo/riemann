# N_BUILD_008 — The archimedean-relative order: reduces to the excluded relative-bound class (NO-GO)

Pen and paper. Proposal from N_BUILD_007: order ν ≼ ν′ iff ⟨ν′ − ν, c_F⟩ ≥ −θ𝔞^♯(F) (θ < 1), and a θ-contraction
property of ρ = M^{−1}*B (M^{−1} = δ₀ − e^{−u/2}du, N_BUILD_007 §0) iterated in Z^{−1} = Σ(−ρ)^{*j}*M^{−1}.

## Corpus check
Paper 46: thm:posext (exterior measures, inf-of-symbol bound), lem:half (|c_F(a)| ≤ ½ for a > T, optimal on P_T),
rem:coer-nogo(a) (coupling of adjacent blocks has norm exactly π, Hilbert inequality; operator-norm route excluded),
thm:margin (λ_A → 0⁺ at most like the explicit B(T,k)). Grid W-lin ("linear bounds in a fixed frame", Paper 46
§subsec:bar-lin). These exclude KLMN-type relative bounds |comb| ≤ θ·(arch) + C with θ < 1 as proofs of the sign.
The question set by the coordinator: does applying the relative bound to the Möbius resolvent ρ instead of the comb, and
iterating, escape that class? Answer below: no.

## 1. A relative bound can never give the sign where 𝔞^♯ is negative (PROVED)
Let 𝔮 be any form on P_T ∩ D_T with |𝔮(F)| ≤ θ·𝔞^♯_+(F) + C‖F‖² for some θ < 1, C ≥ 0, where 𝔞^♯_+ := 𝔞^♯ + |C₀+4|‖·‖²
≥ 0 (𝔞^♯ itself is not positive). Then 𝔞^♯ − 𝔮 ≥ (1−θ)𝔞^♯ − (θ|C₀+4| + C)‖·‖², whose bottom is ≤ (1−θ)λ^♯(T) − θ|C₀+4| − C,
and λ^♯(T) → C₀+4 < 0 (N_BUILD_001 (E)(iii)). So for T ≥ T^♯ (λ^♯(T) < 0) such a bound yields a NEGATIVE lower bound,
never 𝔞_T ≥ 0. Applied with 𝔮 = 𝓕_T (the fluctuation, 𝔞_T = 𝔞^♯ − 𝓕_T): **no KLMN-type relative bound decides the sign**
(this is W-lin/thm:margin in polar-free form; it also explains why the optimal constants π (rem:coer-nogo(a)) and ½
(lem:half) are irrelevant to the sign: even θ = 0 fails, since then C ≥ 0 must still be paid by 𝔞^♯ < 0).

## 2. Moving the relative bound to ρ does not escape (PROVED)
(a) Non-propagation. ⟨ρ*ν, c_F⟩ = ⟨ν, ρ^∨⋆c_F⟩ and ρ^∨⋆c_F (Möbius/shift-transported test) is not in the cone 𝒦_T^c
(N_BUILD_007 §1(iv): shifts leave the cone). Hence a bound |⟨ρ, c_F⟩| ≤ θ𝔞^♯_+(F) + C‖F‖² gives no bound for ⟨ρ^{*j}, c_F⟩:
the iteration is not controlled by θ^j. A relative order is not an algebra order on 𝔄_T.
(b) The constant reappears in the sum. Whatever is proved for the iterates, the sum Σ_j(−ρ)^{*j}*M^{−1} * L is the comb
(N_BUILD_006 §2) up to the main term; so any relative bound obtained by summing gives |𝓕_T| ≤ θ′𝔞^♯_+ + C′, i.e. falls
under §1 with 𝔮 = 𝓕_T. Moreover θ′ < 1 is impossible uniformly: on the lem:half-type multi-bump tests (bumps at
positions whose pairwise lags hit many log n), 𝔞^♯_+ grows only like log(1/ε)·‖F‖² while the comb pairing reaches the
sum of the hit weights, unbounded in T (N_BUILD_001 (F): sup 𝓕_T ≥ A_T − 4 on the unit sphere). So the iterated object
inherits the full relative constant of the comb — the π/2-type obstruction (indeed a T-growing one) reappears in the
sum. ∎
**NO-GO (PROVED): the archimedean-relative order, on ρ or on the comb, reduces to the excluded relative-bound class.**

## 3. What is left (honest state of (N))
Every route of N_BUILD_003–008 is now inside a declared class: sieve (W-tail, prop:wit-sens), reflection (sector
exchange), Selberg symmetry (C_PNT-type), Euler product alone (partial products/powers), cone-monotone iteration
(order-indefinite ρ), relative bounds (W-lin/§1). The exact objects that survive all falsifiers are:
 (N^♯) 𝓕_T(F) ≤ 𝔞^♯(F) on P_T (θ = 1, C = 0 — an exact inequality, not a relative bound), and its algebra form
 (Ω_μ) in 𝔄_T: ⟨2(Z^{−1}*L) − main, c_F⟩ ≤ 𝔞^♯(F), with Z the integer comb (ℤ-integrality, N_BUILD_006 §1 controls the
 additive half) and Z^{−1} the Möbius comb (exact multiplicativity).
Only a θ = 1, C = 0 statement can work, i.e. an exact certificate: write the window measure as (positive-definite
measure) + (Tate annihilator) (Kreĭn/Bochner; R186_052 Thm 3.3, CONDITIONAL mod (−1)^k).

## 4. Next construction (stated precisely)
Sum-of-squares certificate in 𝔄_T built from the factorization Z = M + B: seek measures g_i with
 window measure = Σ_i g_i ⋆ g_i^∨ (on [−2T, 2T]) + α·cosh(u/2) + β·u sinh(u/2),
where g_i are built from Z^{±1}, M^{±1} truncated (finite, explicit Dirichlet-type combs). Squares are in 𝒦_T^* by
Bochner (⟨g⋆g^∨, c_F⟩ = (1/2π)∫|ĝ|²|F̂|² ≥ 0). This is θ = 1, C = 0 by construction, escapes W-lin; W-det/W-mom must be
checked against the number of squares. First test (pen and paper): T = ½log 3 (contacts 2, 3 only), where the corpus
has a certified positive value (Theorem C), to see whether an Euler-factor SOS exists at all.

## Self-review
1. §1: uses 𝔞^♯_+ because 𝔞^♯ is not ≥ 0; with any other positive reference form (e.g. 𝔞^♯ + κ, κ ≥ |C₀+4|) the same
computation gives bottom ≤ (1−θ)λ^♯ − θκ − C < 0. Correct; T^♯ finite by N_BUILD_001(E)(iii).
2. §2(a) is a non-implication (no theorem that iterates fail), stated as such; §2(b) is the real NO-GO, via §1 and
N_BUILD_001(F). Correct.
3. §4: SOS certificates of this shape are the dual-certificate theory of Paper 46 (thm:Z, flat-top weights) in other
clothing; the novelty must be the Euler-factor choice of g_i. Not yet shown non-trivial. Labelled OPEN.
No sign contact; no negative value.
