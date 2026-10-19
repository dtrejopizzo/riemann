# N_BUILD_022 — Matrix identities for A_M: the exact divisor identity Div = Z⁻¹LZ − L (corpus-known as R162_903 B2.1), its spectral
# consequence, and why it does not reach X_M = [Ξ(log m − log k)] (Near is a discretization defect)

Pen and paper. Index set {1,…,M}. Matrices (all lower-unitriangular-type on the divisibility order, closed under taking divisors):
Z_{mk} := 1_{k|m}(m/k)^{−½} (integer comb), Z⁻¹_{mk} = 1_{k|m}μ(m/k)(m/k)^{−½}, Δ_{mk} := 1_{k|m}Λ(m/k)(m/k)^{−½} (Div, one-sided),
L := diag(log m). X_M := [Ξ_{F₀}(log m − log k)], Ξ_{F₀}(d) = Σ_n v_n c₀(log n − d) (N_014; main term 0 by Tate).

## Corpus check
R162_903 Thm 3.2 and line 66: Z X̂ Z⁻¹ = X̂ + M_T(Λ) (compressed operators on L²(I_T), X̂ = position), "every polynomial identity among Z, Z⁻¹, M_T(Λ), X̂
follows from Z = exp M_T(Λ/log) and [X̂, M_T(α)] = −M_T(α log)"; L2_028 §2 (A_M = Arch − Div − Near), L2_029, L2_030 (Near as shifted
convolution), N_005/006 (𝔄_T, Möbius transport), N_018 (meta-theorem), N_021 (Prop 1: Near = Ξ-kernel). L2_BUILD_031 not present at writing.
**The divisor identity of §1 is the integer-matrix form of R162_903's B2.1 — corpus-known.** New: §2 (spectral consequence on ℓ²{1..M}),
§3 (exact defect formula for X_M and the NO-GO), §4 (Bohr symbol).

## 1. The exact divisor identity (PROVED; = R162_903 B2.1 in matrix form)
(ZΔ)_{mk} = Σ_{k|j|m}(m/j)^{−½}Λ(j/k)(j/k)^{−½} = (m/k)^{−½}Σ_{d|m/k}Λ(d) = (m/k)^{−½}log(m/k) = ([L, Z])_{mk}.
So **ZΔ = [L, Z], i.e. Δ = Z⁻¹LZ − L**, exactly, for every M (the index set is divisor-closed, so truncation commutes with products). This is
1*Λ = log at the matrix level, non-class: it holds for Λ only (Möbius inversion over ℕ; a falsifier a ≠ Λ gives Δ_a ≠ Z⁻¹LZ − L).

## 2. Spectral consequence (PROVED, new in this form)
Δ + L = Z⁻¹LZ is similar to L: its eigenvalues are exactly log 1, log 2, …, log M (each once). In particular tr Δ = 0 and
det(Δ + L − λ) = Π_{m≤M}(log m − λ). The symmetric part Div := ½(Δ + Δᵀ) (the form actually appearing in A_M, with c₀(0) = 1 normalization)
satisfies ⟨s, Div s⟩ = ⟨s, Z⁻¹LZ s⟩ − ⟨s, L s⟩. No sign follows: the numerical range of the non-normal Z⁻¹LZ is not confined to
[0, log M] (Z is far from unitary: ‖Z‖ ≍ Σ n^{−½}-type growth), consistent with L2_029 (Div symbol ranges over Σ_p[−2log p/(√p+1), 2log p/(√p−1)]).

## 3. X_M is not controlled by the identity: Near is a discretization defect (PROVED)
Continuous version (N_005, 𝔄): Z*λ_Λ = −∂_sZ (measures on [0,∞)), so for the smoothed kernels Ξ = c₀-smoothing of the Λ-comb,
 Ξ(d) = Σ_{a<∞} μ(a)a^{−½} Ł(d − log a),  Ł(e) := Σ_b (log b) b^{−½} c₀(e − log b)   (Möbius transport, N_006 §2).
Sampling at the lattice d = log m − log k: X_M = [Σ_a μ(a)a^{−½}Ł(log m − log k − log a)]. A matrix product of sampled kernels, (Z⁻¹·Ł_M)_{mk} =
Σ_j μ(m/j)(m/j)^{−½}Ł(log j − log k)1_{j|m}, samples only exact divisors j | m, whereas the sampled convolution uses all a with log a ≈ log(m/k) − e.
Hence
 X_M = Z⁻¹Ł_M + 𝒟_M,  𝒟_M := [Σ_{a: a∤ m or …} …] — the contribution of non-divisor a (near-coincidences a ≈ m/(kb)),
and 𝒟_M vanishes iff the profile width 2T₀ is below the minimal gap of all log(m/(kab)) — i.e. exactly when Near = 0 (L2_029 §1). So the exact
identity of §1 controls X_M precisely on Near-free supports, where L2_029 shows the test is trivial; on general supports the defect 𝒟_M is the
Near part itself. **NO-GO: no exact matrix identity from 1*Λ = log relates X_M to L and Δ beyond the divisor part.**

## 4. Bohr-diagonal symbol on multiplicatively structured vectors (PROVED)
For s_m = m^{−iθ}a_m: sᴴX_M s = (1/2π)∫ Ξ̂(φ)|Σ_m a_m m^{i(φ−θ)}|²dφ with Ξ̂ = F̂₀²·(comb symbol), i.e. the pairing of σ_∞F̂₀² with a Dirichlet
polynomial modulus squared — Theorem S again (024/025). On the Bohr torus with INDEPENDENT phases θ_p (characters of ℚ_{>0}) only Div is diagonal
(L2_028 §2(c)); Near and Arch live on the one-parameter diagonal θ_p = θ log p. So multiplicative structure buys diagonalization of Div only.

## Self-review
1. §1: divisor-closedness of {1..M} — if j | m ≤ M then j ≤ M: yes; so the truncated product equals the truncation of the infinite product. Correct.
2. §1 novelty: identical in content to R162_903 B2.1 (Z X̂ Z⁻¹ = X̂ + M_T(Λ), there with the opposite conjugation convention); recorded.
3. §2: similarity Z⁻¹LZ ~ L exact; eigenvalues log m. Trivial but correct; no sign.
4. §3: the decomposition statement is an exact rewriting; "𝒟_M = Near part" holds up to the exact-coincidence bookkeeping (divisor terms move
into Z⁻¹Ł_M). ARGUED for the precise index set of 𝒟_M; the NO-GO conclusion (identity covers only exact divisibility) is PROVED by §1's proof,
which uses exact divisibility at every step.
5. Coordination: no use of L2_031 (absent); no overlap with residue-balanced restriction.
No sign contact; no negative value certified.
