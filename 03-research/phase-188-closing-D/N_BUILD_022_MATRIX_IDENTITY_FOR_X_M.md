# N_BUILD_022 — Matrix identities for A_M: the exact one-sided divisor identity Δ = Z⁻¹LZ − L (corpus-known as R162_903 B2.1), its spectral
# consequence, and the corrected sampling defect and exact enlargement for X_M

Pen and paper. Index set {1,…,M}. Matrices (all lower-unitriangular-type on the divisibility order, closed under taking divisors):
Z_{mk} := 1_{k|m}(m/k)^{−½} (integer comb), Z⁻¹_{mk} = 1_{k|m}μ(m/k)(m/k)^{−½}, Δ_{mk} := 1_{k|m}Λ(m/k)(m/k)^{−½} (Div, one-sided),
L := diag(log m). X_M := [Ξ_{F₀}(log m − log k)], Ξ_{F₀}(d) = Σ_n v_n c₀(log n − d) (N_014; main term 0 by Tate).

## Corpus check
R162_903 Thm 3.2 and line 66: Z X̂ Z⁻¹ = X̂ + M_T(Λ) (compressed operators on L²(I_T), X̂ = position), "every polynomial identity among Z, Z⁻¹, M_T(Λ), X̂
follows from Z = exp M_T(Λ/log) and [X̂, M_T(α)] = −M_T(α log)"; L2_028 §2 (A_M = Arch − Div − Near), L2_029, L2_030 (Near as shifted
convolution), N_005/006 (𝔄_T, Möbius transport), N_018 (meta-theorem), N_021 (Prop 1: Near = Ξ-kernel). L2_BUILD_031 not present at writing.
**The divisor identity of §1 is the integer-matrix form of R162_903's B2.1 — corpus-known.** New: §2 (spectral consequence on ℓ²{1..M}),
§3 (sampling defect, corrected by212-90/93; the universal NO-GO is withdrawn), §4 (Bohr symbol).

## 1. The exact divisor identity (PROVED; = R162_903 B2.1 in matrix form)
(ZΔ)_{mk} = Σ_{k|j|m}(m/j)^{−½}Λ(j/k)(j/k)^{−½} = (m/k)^{−½}Σ_{d|m/k}Λ(d) = (m/k)^{−½}log(m/k) = ([L, Z])_{mk}.
So **ZΔ = [L, Z], i.e. Δ = Z⁻¹LZ − L**, exactly, for every M (the index set is divisor-closed, so truncation commutes with products). This is
1*Λ = log at the matrix level, non-class: it holds for Λ only (Möbius inversion over ℕ; a falsifier a ≠ Λ gives Δ_a ≠ Z⁻¹LZ − L).

## 2. Spectral consequence (PROVED, new in this form)
Δ + L = Z⁻¹LZ is similar to L: its eigenvalues are exactly log 1, log 2, …, log M (each once). In particular tr Δ = 0 and
det(Δ + L − λ) = Π_{m≤M}(log m − λ). Write D_sym := ½(Δ + Δᵀ). For real s,
⟨s, D_sym s⟩ = ⟨s, Z⁻¹LZ s⟩ − ⟨s, L s⟩. **Normalization correction (phase211, root/casos, 2026-11-05):** D_sym is NOT the Div_M of Paper47. There v_n=2Λ(n)/sqrt(n), V_M=2Δ and Div_M=½(V_M+V_Mᵀ)=Δ+Δᵀ=2D_sym. Thus the divisor quadratic form in Paper47 is twice the displayed identity. At M=2 its off-diagonal entry is log(2)/sqrt(2), whereas D_sym has log(2)/(2sqrt(2)). The one-sided commutator identity and its spectral consequence are unchanged; no paper is edited. No sign follows: the numerical range of the non-normal Z⁻¹LZ is not confined to
[0, log M] (Z is far from unitary: ‖Z‖ ≍ Σ n^{−½}-type growth), consistent with L2_029 (the Paper47 Div symbol ranges over Σ_p[−2log p/(√p+1), 2log p/(√p−1)]; for D_sym divide these endpoints by2).

## 3. Sampling defect: corrected scope (PROVED identities; sign OPEN)

For the real, even autocorrelation used here, the continuous Möbius transport is:

    Ξ(d)=2Σ_a μ(a)a^(−1/2) Ł(d−log a),
    Ł(e)=Σ_b (log b)b^(−1/2)c₀(e−log b).

Sampling the convolution and multiplying the sampled matrices are different operations: the latter only retains divisors of the row index. In the oriented normalization of entries212-90 and212-93 of `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, write K=X_M/2 for the sampled Λ kernel, L_samp for the sampled logarithmic kernel, and D=K−Z^(−1)L_samp. L_samp is distinct from the diagonal L in §§1–2. If c₀ is supported in[−R,R], the exact defect is

    D_mk=Σ_n d_m(n)n^(−1/2)c₀(log(m/(kn))),
    d_m(n)=Λ(n)−1_(gcd(m,n)=1)log n−Λ(gcd(m,n)).

Only finitely many terms contribute. This formula resolves the previously unspecified index set. D must not be identified with the whole Near term, and the assertion that its vanishing is equivalent to the absence of near-coincidences is withdrawn.

Indeed, put N=ceil(exp(R)M), choose q=lcm(1,…,N), and set J e_m=e_(qm). Entry212-93 proves

    J*K_(qM)J=K_M,    J*D_(qM)J=0,
    K_M=J*Z_(qM)^(−1)(L_samp)_(qM)J.

The intermediate indices of this product must be retained; compression of a product is not generally the product of the compressions. The index also gives the sufficient squarefree choice q=Π_(p≤N/2)p for N≥4, and q=1 for N≤3.

Thus the former universal NO-GO is withdrawn: failure of the original sampled product is not an impossibility of exact representation after enlargement. These identities do not prove positivity of K or of the complete form, and do not provide the missing comparison with its archimedean part. The oriented K is not by itself the full matrix of Paper47; both orientations and their normalization are retained in212-93.

## 4. Bohr-diagonal symbol on multiplicatively structured vectors (PROVED)
For s_m = m^{−iθ}a_m: sᴴX_M s = (1/2π)∫ Ξ̂(φ)|Σ_m a_m m^{i(φ−θ)}|²dφ with Ξ̂ = F̂₀²·(comb symbol), i.e. the pairing of σ_∞F̂₀² with a Dirichlet
polynomial modulus squared — Theorem S again (024/025). On the Bohr torus with INDEPENDENT phases θ_p (characters of ℚ_{>0}) only Div is diagonal
(L2_028 §2(c)); Near and Arch live on the one-parameter diagonal θ_p = θ log p. So multiplicative structure buys diagonalization of Div only.

## Self-review
1. §1: divisor-closedness of {1..M} — if j | m ≤ M then j ≤ M: yes; so the truncated product equals the truncation of the infinite product. Correct.
2. §1 novelty: identical in content to R162_903 B2.1 (Z X̂ Z⁻¹ = X̂ + M_T(Λ), there with the opposite conjugation convention); recorded.
3. §2: similarity Z⁻¹LZ ~ L exact; eigenvalues log m. Trivial but correct; no sign.
4. §3: corrected using212-90/93. The explicit gcd formula gives the sampling defect; it is not the whole Near term. The former universal NO-GO and the claimed equivalence of vanishing are withdrawn. Exact enlargement is available; the sign comparison remains OPEN.
5. Coordination: no use of L2_031 (absent); no overlap with residue-balanced restriction.
No sign contact; no negative value certified.
