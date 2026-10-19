# R186.007 — Similarity A_S = E A_∞ E⁻¹, or a new spectrum? Spectral theory of A_S = P F_S P, S = {∞,2}

Model of R186.003: L²(ℝ₊, du), P = 1_{(0,λ]}(u), λ = ½ in the computations.

## Status

| # | Statement | Label |
|---|---|---|
| 1 | F_S = E F_∞ E⁻¹ is unitary: in Mellin (Re s = ½), F_∞ composed with the multiplier (1−2^{−(1−s)})/(1−2^{−s}), of modulus 1 at s = ½+it | PROVED |
| 2 | Grouped kernel: E_K F_∞ E⁻¹ has kernel G_K = Σ_{k=0}^{K} (2c_k − c_{k−1}), c_k := cos(2π2^k ux); G_K = Σ_{k=0}^K c_k − c_{−1} + c_K. Symmetric; A_S self-adjoint | PROVED |
| 3 | A_K := P E_K F_∞ E⁻¹ P → A_S in operator norm, ‖A_S − A_K‖ ≤ (1+2^{−1/2}) Σ_{k>K} 2^{−k/2} | PROVED |
| 4 | **A_S is compact** (norm limit of HS operators) | PROVED |
| 5 | **A_S is not Hilbert–Schmidt** (hence not trace class); Σ λ_n² = ∞ | PROVED |
| 6 | **The similarity A_S = E A_∞ E⁻¹ is FALSE**: P E P = E P but P E ≠ E P; the defect is P E (1−P) F_∞ P E⁻¹ P ≠ 0 | PROVED |
| 7 | Spectrum of A_S (λ = ½): 0.987, −0.509, 0.29, −0.26, 0.18, −0.17, … ; squares 0.974, 0.26, 0.08 | NUMERICAL (first 2 converged ±0.003/±0.01; the rest not converged in N) |
| 8 | Eigenvalue counting function of A_S (Landau–Widom-type law) | OPEN |

Verdict: the similarity hypothesis is false; the spectrum of P F_S P is genuinely new (non-archimedean), and
the numbers of R186.006 §6 were qualitatively correct; its "1.013 > 1" and the drift in K came from truncating
Σ_{k≤K} c_k (which includes a term c_K of norm ≈ ½ that does not tend to 0 in norm), not from the operator.

## 1. Formula and unitarity

D_a g(u) := g(au). In L²(ℝ₊,du), Mellin on Re s = ½: D_2 ↔ multiplication by 2^{−s} (|·| = 2^{−1/2}), E = Σ_{k≥0} D_{2^k} ↔ (1−2^{−s})⁻¹, E⁻¹ = 1 − D_2 (both bounded, ‖E‖ ≤ (1−2^{−1/2})⁻¹). F_∞ (kernel 2cos 2πux, unitary) exchanges s ↔ 1−s; hence F_∞ D_2 F_∞ = ½D_{1/2} = D_2^*, F_∞ E F_∞ = E^*, and
 F_S = E F_∞ E⁻¹ = F_∞ (E^* E⁻¹),
with E^*E⁻¹ the multiplier (1−2^{−(1−s)})/(1−2^{−s}) — at s = ½+it, a quotient of two conjugates: |·| = 1. Unitary. (This corrects the "?" : E is not unitary but E^*E⁻¹ is.) PROVED.

Kernel: ∫ 2cos(2π2^k uy)(f(y) − f(2y)) dy = ∫ [2c_k − c_{k−1}](u,y) f(y) dy. Summing k ≤ K: G_K as in the table. The grouped form is the correct one: the terms 2c_k − c_{k−1} correspond to P D_{2^k} F_∞ E⁻¹ P, of norm ≤ 2^{−k/2}(1+2^{−1/2}). (NUMERICAL: the measured norms of these terms decay with ratio 0.707 = 2^{−1/2}, k = 6…12.) The series "Σ_{k≥0} c_k − c_{−1}" of R186.006 only makes sense distributionally; its truncation differs from G_K by −c_K, and P c_K P is (½)×(an archimedean band operator with c ∝ 2^Kλ²), of norm → ½, not → 0.

## 2. Compactness (PROVED)

A_K has a bounded kernel on (0,λ]², hence is HS, in particular compact. By §1, ‖A_S − A_K‖ → 0 geometrically. The set of compact operators is norm-closed: A_S is compact. (This confirms the claim of R186.006 by another route.)

## 3. A_S is not Hilbert–Schmidt (PROVED)

Suppose A_S is HS with kernel κ ∈ L²((0,λ]²). For Φ of trace class (smooth kernel on the closed square), ⟨A,Φ⟩_HS = Tr(AΦ^*) is continuous in A for the operator norm; hence ⟨κ,φ⟩ = lim_K ∫∫ G_K φ̄ for smooth φ.
Fix χ ∈ C_c^∞((δ, λ−δ)²), ∫∫χ ≠ 0, and φ_m := c_m χ (m ≥ 1).
- L² side: φ_m → 0 weakly in L² (Riemann–Lebesgue), so ⟨κ,φ_m⟩ → 0.
- Kernel side: ∫∫ G_K φ_m = Σ_{j=0}^{K} ∫∫c_jc_mχ − ∫∫c_{−1}c_mχ + ∫∫c_Kc_mχ. With c_jc_m = ½[cos 2π(2^j−2^m)ux + cos 2π(2^j+2^m)ux] and non-stationary phase in u (∂_u = 2πbx, x ≥ δ): ∫∫χ cos(2πbux) = O_N((bδ)^{−N}). For j ≠ m, b ≥ 2^{max(j,m)−1}; the term j = m gives ½∫∫χ + O(2^{−mN}). Letting K → ∞ (the term c_K vanishes by Riemann–Lebesgue): ⟨κ,φ_m⟩ = ½∫∫χ + O(2^{−m}).
Contradiction for large m. ∎ Hence Σ_n λ_n(A_S)² = ∞: eigenvalue decay slower than n^{−1/2} on average (in contrast with the super-exponential Slepian decay). This proves the OPEN "L1^ang" of R186.006 in a strong negative sense.

## 4. The similarity fails (PROVED) — exact point

A_S = P E F_∞ E⁻¹ P. Correct: E⁻¹P = P E⁻¹ P ((D_2Pg)(u) lives at u ≤ λ/2) and P E P = E P (dilations by 2^k ≥ 1 do not push the support out of (0,λ]). **False: P E = E P.** (P E g)(u) = Σ_k g(2^k u) for u ≤ λ reads g at 2^k u > λ: P E(1−P) ≠ 0. Hence
 A_S = E A_∞ E⁻¹|_{L²(0,λ]} + P E (1−P) F_∞ P E⁻¹ P.
Alternative proof without computation: E A_∞ E⁻¹ is similar to a trace-class operator, hence trace class; A_S is not HS (§3); the defect is nonzero. Moreover E A_∞ E⁻¹ is not self-adjoint, while A_S is. The second summand is exactly the "outside the box" contribution (1−P)F_∞P brought back into (0,λ] by the dyadic dilations: that is where the prime 2 enters.
Relation to CCM (Thm isosonin): θ_S/η_S = E does send the archimedean Sonin space to the semilocal Sonin space (kernels ran(1−P)∩ran(1−P̂) — subspaces, not compressed operators), but it does not intertwine the compressed operators P F P. There is no contradiction with R186.002 §2.2.

## 5. Spectrum (NUMERICAL)

Galerkin in the orthonormal Legendre basis of L²(0,½], N ≤ 40, entries ∫∫ φ_iφ_j c_k by Gauss–Legendre with ≥ 8·2^kλ² + 200 nodes (machine-exact), terms grouped k ≤ K, K = 8, 10, 12 (script in scratchpad s2.py).

| N\K | λ₁ | λ₂ | λ₃ | λ₄ |
|---|---|---|---|---|
| 40/8 | 0.98150 | −0.51854 | 0.2936 | −0.2642 |
| 40/10 | 0.98567 | −0.51144 | 0.2881 | −0.2572 |
| 40/12 | 0.98691 | −0.50893 | 0.2871 | −0.2560 |
| 30/12 | 0.98679 | −0.50729 | 0.2746 | −0.2504 |
| 20/12 | 0.98640 | −0.50421 | 0.2495 | −0.2252 |

Tail in K: Weyl gives |Δλ| ≤ 1.71·Σ_{k>12}2^{−k/2} ≈ 0.02 (crude bound); the observed drift K=10→12 is 1.2·10⁻³ in λ₁, ratio ≈ ½ every 2 steps: λ₁ ≈ 0.988 ± 0.003, λ₂ ≈ −0.507 ± 0.01. λ₃, λ₄ grow with N (expected symptom of non-HS): only a lower bound ≈ 0.29. Archimedean (same code, kernel 2c_0): 0.8851, −0.1066, 1.47·10⁻³, −7.7·10⁻⁶ (squares 0.783, 1.1·10⁻², 2.2·10⁻⁶ = R186.006). Semilocal squares 0.976, 0.257, ≥0.08: agree with R186.006 (0.96, 0.27, 0.09).

## 6. Consequence for the toolbox

- There exists a "semilocal band operator" with a new spectrum: compact, self-adjoint, not HS, with λ₁ ≈ 0.988 > 0.885 archimedean. The prediction ("only the metric E^*E changes") is false for the compressed operators; it is true for the Sonin subspaces (§4).
- No regular differential operator with discrete spectrum of polynomial growth ≥ n^{1/2+ε} can have P F_S P as a decreasing monotone function with square-summable decay: the Slepian analogue (a commuting prolate operator) must have a much denser spectrum or fail to exist — consistent with the metaplectic NO-GO of R186.006.
- OPEN: counting law #{|λ_n| > θ} (≍ log of something, or a power?); alternating signs observed (λ_{2j−1} > 0 > λ_{2j}); general S: §§1–4 hold word for word with E = ∏_p (1−D_p)⁻¹ (multiplier ∏(1−p^{−s})⁻¹), since only unitarity of the quotient was used, P E P = E P, E⁻¹P = PE⁻¹P (for finite S, E⁻¹ = ∏(1−D_p), dilations by p ≥ 1) and the lacunary argument (for several primes the terms are c_n with n in the multiplicative set ⟨S⟩, still with separation |n−m| ≥ 1 but not lacunary: §3 needs the cross sums revisited — OPEN for |S∖∞| ≥ 2).

## Audit notes

1. §3 uses ⟨κ,φ⟩ = lim ∫∫G_Kφ̄: justify that Φ_m (kernel c_mχ, smooth with compact support) is trace class — yes (C^∞ kernel on a square ⟹ trace class).
2. Is exchanging K → ∞ before m → ∞ legitimate? For fixed m the limit in K exists (operator norm) and the estimate O(2^{−m}) is uniform in K.
3. Normalizations: if F_∞ had kernel cos instead of 2cos, everything rescales; the check that A_∞ reproduces 0.783 (=R186.006) fixes the normalization.
4. The non-convergence in N of λ₃,λ₄ has not been quantified; do not cite those values without a bound.
5. nothing here touches the sign of row D.

## Note (R186_094)

* Multiplier of §1 inverted: correct is (1−2^{−s})/(1−2^{−(1−s)}). §6 on differentials: HEURISTIC. Counting: ARGUED.

## Note (R186_020)

* The compactness of (1−P)uP is CC arXiv:2008.10974 (Thm 2.1, 4.4); the non-HS result is ours. Cite it.
