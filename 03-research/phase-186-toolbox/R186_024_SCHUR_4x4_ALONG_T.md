# R186_024 — The edge-mode secular problem along T: is the 𝒱 ⊕ E reduction stable?

Phase 186. Sources: R186_019 (Thm 3.1, exact Schur at ½log3), R186_100 (editor's note), R186_023 (growing rank), R155_026 (Schur reduction at log 2), Paper 46 (eq:form, thm:A, lem:K, thm:S(iii), thm:margin, lem:contA).
Script: `r024_schur.py` (standalone). Form computed **in x-space** with Paper 46's Lévy formula from thm:A: 𝔞_T(F) = C₀‖F‖² + ∫₀^∞(‖F‖² − 𝒞F(u))K(u)du − Σ_{n∈𝒩_T} v_n 𝒞F(log n), K(u) = 2e^{−u/2}/(1−e^{−2u}), tail ∫_{2T}^∞K in closed form (thm:S iii). No oscillatory integrands; piecewise Gauss quadrature (exact on polynomials); orthonormal Legendre basis per block (allows jumps). Reproduces R186_019 at ½log3 to 4 digits (λ_W 9.45e-4, c 0.5735, λ_S 1.174e-3, min G_EE 0.1142). Double precision verified against mpmath (25 digits) at 0.78 and ½log5 with the same N: agreement to 0.06%. All figures are NUMERICAL except where marked PROVED.

## Status

**Two-part verdict.**

1. **The R186_019 reduction with fixed E of dimension 4 (orbit blocks J, M, J′) is NOT stable in T** (NUMERICAL, the deciding number): c(T) = min 𝔞_T|𝒱 drops from 0.906 (T = 0.48) to **0.013** (T = 0.69), and at T = log 2 the decomposition changes (5 blocks, dim E = 8). With three equal thirds c drops from 1.44 to 0.16. A fixed-dimension E does not absorb the entire drop: consistent with R186_023 (growing rank).

2. **The reduction IS stable on [½log2, ½log5] if the number k of blocks is allowed to grow** (NUMERICAL): with k equal blocks (dim E = 2k−2), across the whole grid c ≥ 0.44 (k=5), ≥ 0.59 (k=7), ≥ 0.81 (k=9), ≥ 0.99 (k=11), ≥ 1.24 (k=13), while λ_min(W|𝒫_T) drops from 2·10⁻¹ to 3·10⁻¹². The secular S carries the entire drop: **λ_min(S)/λ_min(W) ∈ [1.00, 1.09]** for k ≥ 5. Moreover, the near-kernel h*_T has **99–99.9% of its mass in E** = span{e^{±x/2}1_B} ∩ 𝒫_T: the minimizer is, to that precision, a piecewise Tate exponential. The exact reason for the growth in k: each block with its Tate contributes exactly the archimedean background of a single window of half-length T/k (PROVED, §1.3), and that background is only large if T/k is small. Hence the correct finite target per window is (L1)+(L2) with k ≍ T/τ₀, dim E = O(T), not a uniform 4×4.

3. **(L1) splits into three pieces, two PROVED and one OPEN in pure harmonic analysis** (§3): c(T) ≥ c_∞(T/k) − ‖𝒦₁‖_{𝒱_k} − 𝒜_T/2, where c_∞(τ) is the primitive archimedean background of a single window (no primes), 𝒦₁ is the archimedean coupling between blocks with the **reduced** kernel K₁ = K − 2e^{−u/2} (the per-block Tate conditions exactly cancel the dominant Lévy term; PROVED), and 𝒜_T/2 is the crude prime bound (PROVED). Numerically ‖𝒦₁‖_{𝒱_k} ≈ 0.74 **independent of T and k**, and with k = 13 the split inequality holds across the whole grid (minimum margin 0.056 at ½log5; k = 15 gives more slack).

**No sign contact:** λ_min(W|𝒫_T) > 0 at every T on the grid, down to 3.15·10⁻¹² at ½log5 (Galerkin upper bound, N = 18; confirmed by mpmath). No negative value, certified or not.

## 1. The decomposition 𝒱 ⊕ E_T for general T (PROVED)

**1.1 Orbit blocks.** Let ℓ = log 2. For ½log2 < T < ℓ: J = (−T, T−ℓ), M = (T−ℓ, ℓ−T), J′ = (ℓ−T, T), with |J| = 2T−ℓ, |M| = 2ℓ−2T. Lemma 1.1 of R186_019 holds literally for every T in that range (its proof does not use T = ½log3): the prime 2 is the swap τ on L²(J)⊕L²(J′) and zero on L²(M). As T → ½log2 the blocks J, J′ disappear (𝒱 = 𝒫_T, E = 0); as T → ℓ, M disappears. For ℓ ≤ T < 3ℓ/2 the ℓ-shift orbits give **five** blocks (−T, T−2ℓ), (T−2ℓ, ℓ−T), (ℓ−T, T−ℓ), (T−ℓ, 2ℓ−T), (2ℓ−T, T), with two orbit types (length 3 and 2). The primes 3 (T > ½log3) and 4 (T > ℓ) do not respect the blocks: they are couplings, each with norm ≤ v_n/2.

**1.2 𝒱, E and the dimension.** For any partition of I_T into blocks B₁,…,B_k: 𝒱_k := ⊕_B {h ∈ L²(B): ∫_B h e^{±x/2} = 0}, E_k := 𝒫_T ⊖ 𝒱_k = span{e^{±x/2}1_B} ∩ 𝒫_T, dim E_k = 2k − 2 (the two global Tate relations). Proof: Thm 3.1 of R186_019, which only uses that within each block the orthogonal complement of the kernel of the two functionals is span{e^{±x/2}|_B}. For the orbit blocks, dim E = 4 (T < ℓ) and 8 (T ≥ ℓ). The Schur reduction λ_min(W|𝒫_T) > 0 ⟺ S = G_EE − G_E𝒱 G_𝒱𝒱^{−1} G_𝒱E ≻ 0 (if c = min 𝔞_T|𝒱 > 0) is algebra, with the refinements of R186_100 (form domain, Lax–Milgram, λ_min(W) ≥ min(c, λ_S)/(1+‖K‖)², ≤ λ_S).

**1.3 Sectors = single windows (PROVED).** 𝔞_∞ (archimedean part) depends on F only through its autocorrelation, so it is translation-invariant; the Tate condition ∫h e^{±x/2} = 0 is multiplied by e^{±a/2} under translation, so its kernel is invariant. Hence min 𝔞_∞ over the sector of a block of length a with its Tate condition is c_∞(a/2) := λ_min(𝔞_∞|𝒫_{a/2}), the primitive archimedean background of a single window. Checked to 4 digits (2.2722 vs 2.272 at τ = 0.0619; 1.9044 vs 1.904 at τ = 0.0894). For orbit blocks with T < ℓ, no prime falls inside a block (|J| = 2T−ℓ < ℓ), so also min 𝔞_T|sector(J) = c_∞(T − ℓ/2).

**1.4 The Tate conditions cancel the dominant coupling term (PROVED).** For F_B ∈ 𝒱 on block B and F_{B′} on B′ to the left, the cross term of 𝔞_∞ is −∫∫F_B(x)F_{B′}(y)K(x−y)dxdy. Since K(u) = 2e^{−u/2} + K₁(u), K₁(u) := 2e^{−5u/2}/(1−e^{−2u}), and 2e^{−(x−y)/2} = 2e^{−x/2}e^{y/2} is rank one and is killed by the Tate condition of either block, the coupling on 𝒱 has kernel K₁. Properties: K₁(u) ≤ 1/u (sup u·K₁ = 1 as u→0), K₁(u) ≤ 2e^{−5u/2}/(1−e^{−2u}) (decays like e^{−5u/2}). The 1/u kernel between adjacent intervals is scale-invariant, which explains why ‖𝒦₁‖_{𝒱_k} does not depend on k or T (§2.3).

**1.5 T-dependence of G_EE, G_E𝒱.** The entries of G_EE are 𝔞_T(e^{εx/2}1_B, e^{ε′y/2}1_{B′}): autocorrelations of exponentials over intervals (piecewise exponential-linear in u) integrated against K = 2Σ_j e^{−(2j+½)u} and evaluated at log n: closed form as digamma-type series at the block endpoints; they depend on T only through the block endpoints and the tail log coth(T/2) + π − 2 arctan e^T. They were not written out explicitly (not needed for the verdict). G_E𝒱 has no useful closed form: it involves the resolvent on 𝒱.

## 2. Numbers

**2.1 Orbit blocks (N = 14 per block; N = 18 changes λ_W < 3%, c < 0.2%).** S(T) = {n: log n < 2T}: {2} up to ½log3, {2,3} up to ℓ, {2,3,4} up to ½log5.

| T | dim E | λ_min(W\|𝒫_T) | c = min 𝔞_T\|𝒱 | c_∞ (𝒱, no primes) | ‖P\|𝒱‖ | λ_min(S) | λ_S/λ_W | min G_EE | ‖K‖ | ‖P_E h*‖² | ‖𝒦₁‖_𝒱 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.36 | 4 | 4.78e-1 | 0.586 | 0.586 | 0.490 | 1.37e+0 | 2.86 | 1.806 | 0.68 | 0.10 | 0.50 |
| 0.40 | 4 | 2.25e-1 | 0.710 | 0.711 | 0.490 | 3.30e-1 | 1.46 | 0.688 | 0.64 | 0.61 | 0.69 |
| 0.44 | 4 | 8.66e-2 | 0.840 | 0.848 | 0.490 | 1.06e-1 | 1.22 | 0.371 | 0.52 | 0.81 | 0.76 |
| 0.48 | 4 | 2.60e-2 | 0.906 | 0.997 | 0.490 | 2.98e-2 | 1.15 | 0.246 | 0.44 | 0.87 | 0.79 |
| 0.52 | 4 | 4.45e-3 | 0.717 | 1.110 | 0.490 | 5.19e-3 | 1.17 | 0.186 | 0.44 | 0.86 | 0.81 |
| ½log3 | 4 | 9.45e-4 | 0.574 | 1.042 | 0.490 | 1.17e-3 | 1.24 | 0.114 | 0.52 | 0.81 | 0.81 |
| 0.58 | 4 | 2.10e-4 | 0.324 | 0.922 | 0.820 | 2.87e-4 | 1.36 | 0.150 | 0.90 | 0.73 | 0.80 |
| 0.62 | 4 | 1.87e-5 | 0.145 | 0.770 | 0.871 | 2.99e-5 | 1.60 | 0.128 | 2.09 | 0.63 | 0.78 |
| 0.66 | 4 | 1.25e-6 | 0.065 | 0.624 | 0.871 | 2.44e-6 | 1.96 | 0.174 | 4.32 | 0.51 | 0.70 |
| 0.69 | 4 | 1.35e-7 | **0.013** | 0.486 | 0.890 | 3.12e-7 | 2.31 | 0.232 | 14.6 | 0.43 | 0.50 |
| 0.70 | 8 | 5.91e-8 | 0.022 | 0.510 | 0.888 | 1.32e-7 | 2.24 | 0.191 | 10.4 | 0.45 | 0.52 |
| 0.72 | 8 | 1.02e-8 | 0.055 | 0.599 | 0.890 | 1.99e-8 | 1.94 | 0.121 | 5.54 | 0.52 | 0.67 |
| 0.75 | 8 | 7.91e-10 | 0.101 | 0.708 | 0.990 | 1.27e-9 | 1.61 | 0.062 | 3.87 | 0.62 | 0.75 |
| 0.78 | 8 | 4.19e-11 | 0.156 | 0.815 | 1.131 | 5.76e-11 | 1.38 | 0.029 | 2.97 | 0.73 | 0.79 |
| ½log5 | 8 | 3.24e-12 | 0.191 | 0.905 | 1.188 | 4.05e-12 | 1.25 | 0.014 | 2.47 | 0.80 | 0.81 |

Readings: (i) λ_S ≈ λ_W always (ratio 1.15–2.9), the secular carries the drop; (ii) c is not stable: it drops 70× between 0.48 and 0.69 (and 2000× relative to λ_W: the drop is **shared**); the drop in c coincides with the blow-up of ‖K‖ = ‖G_𝒱𝒱^{−1}G_𝒱E‖ (0.44 → 14.6): 𝒱 itself acquires a near-null direction; (iii) ‖P|𝒱‖ = 0.490 = √2ℓ/2 exactly while S(T) = {2} (swap norm, PROVED), and grows to 0.89 and 1.19 with primes 3 and 4 (crude bounds 1.124 and 1.471). mpmath (25 digits, N = 12): 0.78 → λ_W 4.630e-11, λ_S 6.368e-11; ½log5 → λ_W 3.367e-12, λ_S 4.207e-12; double with N = 12 gives 4.630e-11 / 6.368e-11 and 3.369e-12 / 4.211e-12. Double precision is reliable across the whole range; the differences with N are Galerkin convergence (upper bounds). Comparison with R186_023 (6.4e-12 at ½log5, basis vanishing at the endpoints): our basis with jumps gives a smaller upper bound, 3.15e-12 (N = 18).

**2.2 Partitions into k equal blocks (dim E = 2k−2; N = 12; k = 3 does not converge for T ≥ 0.72).** Entries: c(T) and, in parentheses, λ_S/λ_W.

| T | k=3 | k=5 | k=7 | k=9 | k=11 | k=13 |
|---|---|---|---|---|---|---|
| 0.44 | 1.073 (1.10) | 1.407 (1.02) | 1.719 (1.006) | 1.969 (1.002) | 2.256 | 2.611 |
| 0.52 | 0.718 (1.17) | 1.319 (1.01) | 1.639 (1.004) | 1.713 (1.000) | 2.062 | — |
| ½log3 | 0.670 (1.20) | 1.233 (1.01) | 1.464 (1.004) | 1.833 (1.001) | 1.864 | 2.205 |
| 0.58 | 0.675 (1.22) | 0.978 (1.01) | 1.410 (1.005) | 1.599 (1.005) | 1.680 | — |
| 0.62 | 0.532 (1.23) | 0.953 (1.01) | 1.207 (1.01) | 1.233 (1.00) | 1.681 | 1.725 |
| 0.66 | 0.221 (1.25) | 0.769 (1.02) | 1.120 (1.01) | 1.289 (1.00) | 1.553 | — |
| 0.69 | 0.162 (1.26) | 0.590 (1.03) | 0.905 (1.01) | 1.177 (1.01) | 1.478 | 1.520 |
| 0.72 | (n.c.) | 0.622 (1.04) | 0.973 (1.01) | 1.112 (1.00) | 1.383 | 1.483 |
| 0.78 | (n.c.) | 0.445 (1.07) | 0.645 (1.01) | 0.810 (1.00) | 1.096 | 1.311 |
| ½log5 | (n.c.) | 0.494 (1.09) | 0.592 (1.01) | 0.859 (1.00) | 0.991 | 1.241 |

λ_W is independent of the partition (as it should be), 3.13–3.21e-12 at ½log5 for k = 5…13. For fixed k, c(T) decreases slowly with T (at k = 9: 1.97 → 0.86 over the whole range, factor 2.3, versus 10¹¹ in λ_W); for fixed T, c grows with k. This is what §1.3 says: c ≤ c_∞(T/k) − (coupling), and c_∞(τ) ≈ log(1/τ) − 0.5 for τ ∈ [0.03, 0.09] (2.35 at 0.057, 2.97 at 0.031: difference 0.62 = log(0.057/0.031) to 1%). **Conclusion:** the reduction is stable over any bounded range of T with k ≍ T/τ₀, and that is why on [½log2, ½log5] k = 5 suffices (c ≥ 0.44) or k = 9 (c ≥ 0.81).

**2.3 The three pieces of (L1) (k equal blocks, N = 10).** sec_∞ = c_∞(T/k) (§1.3); ‖𝒦₁‖ = norm of the archimedean coupling between blocks on 𝒱_k (§1.4); 𝒜_T/2 = 0.490 / 1.124 / 1.471 over the three contact ranges.

| T | k | sec_∞ = c_∞(T/k) | ‖𝒦₁‖_𝒱 | 𝒜_T/2 | sec_∞ − ‖𝒦₁‖ − 𝒜_T/2 | c medido | ‖P_E h*‖² |
|---|---|---|---|---|---|---|---|
| 0.40 | 13 | 2.971 | 0.745 | 0.490 | +1.736 | 2.611 | 0.998 |
| ½log3 | 13 | 2.654 | 0.745 | 0.490 | +1.419 | 2.205 | 1.000 |
| 0.62 | 13 | 2.533 | 0.745 | 1.124 | +0.664 | 1.725 | 0.999 |
| 0.69 | 13 | 2.426 | 0.745 | 1.124 | +0.557 | 1.520 | 0.999 |
| 0.72 | 13 | 2.383 | 0.745 | 1.471 | +0.167 | 1.483 | 0.999 |
| 0.78 | 13 | 2.303 | 0.745 | 1.471 | +0.087 | 1.311 | 0.999 |
| ½log5 | 13 | 2.272 | 0.745 | 1.471 | **+0.056** | 1.241 | 0.999 |
| ½log5 | 11 | 2.105 | 0.743 | 1.471 | −0.109 | 0.992 | 0.998 |
| ½log5 | 9 | 1.904 | 0.742 | 1.471 | −0.309 | 0.859 | 0.995 |
| ½log5 | 7 | 1.653 | 0.738 | 1.471 | −0.556 | 0.592 | 0.990 |

‖𝒦₁‖_𝒱 = 0.738 (k=7), 0.742 (k=9), 0.744 (k=11), 0.745 (k=13), across all T: a constant. The split bound is positive on the whole grid with k = 13 (and, with comfortable margin, with k = 15–17); with the fine measured ‖P|𝒱‖ (≈1.2 instead of 1.471), k = 9 already suffices.

## 3. Statements (L1), (L2) and a proof proposal

**(L2) [NUMERICAL on the grid; OPEN as a proof].** For k = 5 equal blocks and all T ∈ [½log2, ½log5], S_T := G_EE − G_E𝒱 G_𝒱𝒱^{−1} G_𝒱E (8×8, E = span{e^{±x/2}1_B} ∩ 𝒫_T) satisfies λ_min(S_T) ≥ λ_min(W|𝒫_T) > 0, with λ_min(S_T) ∈ [3.5·10⁻¹², 0.1]. There is no simplification in precision (R186_100): certifying S_T ≻ 0 at ½log5 requires the resolvent on 𝒱 with relative error 10⁻¹² — the same as certifying W directly. The gain is structural: the near-kernel lives in E (99.5% with k = 9), so **the positivity of W is, to precision 10⁻³, a statement about piecewise Tate exponentials**. Interval certification is realistic for T ≤ 0.6 (λ ≥ 10⁻⁵) with N ≈ 12 per block and the R185_093 tail applied to G_𝒱𝒱 (gap c ≥ 0.44 → cheap tail). OPEN.

**(L1) [the decomposition is PROVED; two of the three pieces are OPEN].** Let k ≥ 1, 𝒱_k as in §1.2. Then, for all T,

 min 𝔞_T|𝒱_k ≥ c_∞(T/k) − ‖𝒦₁‖_{𝒱_k} − 𝒜_T/2,

where (a) c_∞(τ) = λ_min(𝔞_∞|𝒫_τ) [PROVED to be the sectoral minimum, §1.3; its value is NUMERICAL: ≈ log(1/τ) − 0.5 for τ ≤ 0.09; an explicit lower bound is OPEN, but it is a problem about **a short prime-free window**: 𝔞_∞ ≥ C₀ + (Lévy) with Lévy ≥ ∫(1−cos τu)K over the Fourier mass of 𝒫_τ at |s| ≳ 1/τ, i.e. of the type lem:mbounds in Paper 46 / Bombieri 2000 Thm 3]; (b) ‖𝒦₁‖_{𝒱_k} = norm of the quadratic form −Σ_{B≠B′}∫∫F_B F_{B′}K₁(|x−y|) on 𝒱_k [PROVED that the kernel is K₁ = K − 2e^{−u/2}; NUMERICAL ‖𝒦₁‖ ≈ 0.74; bound ≤ 0.8 OPEN]; (c) ‖P|𝒱_k‖ ≤ Σ_{n∈𝒩_T} v_n/2 = 𝒜_T/2 [PROVED: |𝒞F(log n)| ≤ ‖F‖² by Cauchy–Schwarz]. With k = 13 the right-hand side is ≥ 0.056 across the whole grid (NUMERICAL); with k ≍ T/τ₀ and c_∞(τ₀) > 0.75 + 𝒜_T/2 the bound is positive in any range where 𝒜_T/2 ≤ c_∞(τ₀) − 0.75; since 𝒜_T grows (≈ 2e^{T}) and c_∞(τ) ≈ log(1/τ), this requires τ₀ ≈ e^{−𝒜_T/2}: k grows **exponentially** in T. Only in the declared range is it a reasonable finite target (k ≤ 17).

**Proposed proof of (L1) via the archimedean route (what remains to be done):**
1. c_∞(τ) ≥ log(1/τ) − C₁ for τ ≤ 0.1, with explicit C₁ (≈ 0.5 per §2.2). Tools: lem:mbounds (m(s) ≥ log(|s|/2π) − C), an uncertainty bound on 𝒫_τ (a function ⊥ e^{±x/2} on an interval of length 2τ has Fourier mass ≥ ½ at |s| ≥ c/τ: a Nazarov/Turán-type inequality, or directly from the second moment), and 𝔞_∞ ≥ C₀ + ∫(1−cos τ u)K. OPEN but standard.
2. ‖𝒦₁‖_{𝒱_k} ≤ 0.8. The kernel K₁ ≤ 1/u between adjacent intervals is of Hilbert type (norm π with no constraints: insufficient, 2π > c_∞). The Tate condition must be used: on a short block e^{±x/2} ≈ 1 ± x/2, so F_B ⊥ {1, x} approximately, and the Hilbert operator between adjacent intervals restricted to functions with zero mean and zero first moment has norm much smaller than π (scale dilation makes it independent of k and T: the measured 0.74 is presumably the exact norm of the limiting operator with kernel 1/u on Tate-orthogonal functions on adjacent blocks, computable as a spectral problem for a single geometry). Non-adjacent blocks contribute ≤ 2e^{−5d/2}·(Schur test) with d ≥ 2T/k. OPEN, pure harmonic analysis, no primes.
3. Crude prime bound, PROVED. (Optional refinement: on 𝒱_k the prime-2 term has norm exactly √2ℓ/2 while |J| < ℓ, and shifts log n > block length only couple distinct blocks, which would allow subtracting their low-rank part too; not needed in the declared range with k = 13.)

If 1–2 are proved, (L1) becomes PROVED on [½log2, ½log5] with k = 13, and the positivity per window reduces to the 24×24 (L2).

## 4. Connections with the corpus

- **R186_019 / R186_100:** Thm 3.1 still holds (PROVED as algebra) and extends to any partition and any T (§1.2); its CONDITIONAL (L1) does not hold with a uniform margin for the orbit blocks (c → 0.013 as T → ℓ), but does hold with k ≍ T/τ₀ equal blocks. The "couplings necessary for positivity" point of R186_019 §3 is sharpened: what is necessary is the coupling **through E** (h* ∈ E); on 𝒱 the couplings only cost ‖𝒦₁‖ ≈ 0.74 and nothing more.
- **R186_023:** the growing-rank law reappears here as k ≍ T/τ₀ (dim E = O(T) in a bounded range, exponential in T in general): compatible, and it gives an **explicit, non-spectral** basis (e^{±x/2}1_B) for the fragile direction, which the archimedean-mode basis of R186_023 did not provide.
- **R155_026 (Schur at log 2):** same structure "huge Schur correction, 1% cancellation"; there the basis was spectral and of dimension ≤ 47 on a window ≥ log 2 (outside the range here).
- **Paper 46 thm:margin:** λ_W ≤ 𝓑(T,k) → 0 forces that, with E fixed, c or λ_S decay; §2 shows that **both** decay with E fixed and that only λ_S decays with k ≍ T. lem:contA (continuity of λ_A in T) is consistent with the tables (λ_W continuous across T = ℓ where the orbit partition changes: 1.35e-7 → 5.9e-8). thm:A/lem:K/thm:S(iii) are exactly what the script implements; no new definitions.
- **Zhu 2026 (0.8) / Paper 46 §log5:** no new sign claim is made; the λ_W values in the table are Galerkin upper bounds, not certificates.

## Audit notes

- All λ values are Galerkin values (upper bounds on infima over subspaces); c and λ_S depend on the subspace of 𝒱, E is exact in the continuum and approximate in the basis (E is built as span{P_B e^{±x/2}} with P_B the projection onto the block's polynomials). Convergence: N = 14 vs 18 changes λ_W ≤ 3%, c ≤ 0.2%, λ_S ≤ 3%.
- Precision: double vs mpmath 25 digits agree to 0.06% at ½log5 (λ ~ 3·10⁻¹²). No interval arithmetic is used; nothing certifies the sign.
- The constancy of ‖𝒦₁‖ ≈ 0.74 was measured for k ∈ {7,…,13}, T ∈ [0.40, 0.805]; in the orbit blocks it varies (0.5–0.81) because the blocks are unequal. This is a scaling fact about the 1/u kernel, not proved.
- "c_∞(τ) ≈ log(1/τ) − 0.5" is a two-point fit; no asymptotic claim is made.
- The margin 0.056 (k = 13, ½log5) is fine; with the crude prime bound 1.471 and ‖𝒦₁‖ = 0.745, the 2.272 value of c_∞(0.0619) carries 0.2% Galerkin error, which is sufficient. For a statement with slack, use k = 15–17 (c_∞(T/15) ≈ 2.42 at ½log5, margin ≈ 0.2).
- k=3 equal blocks for T ≥ 0.72 with N = 12 does not converge (λ_W = 1.1e-10 versus 3.2e-12): marked n.c. and not used.
- No equivalence between row D and other statements is used; positivity is assumed true and its proof is sought.

## For Paper 46

- Can be integrated as a structural observation (NUMERICAL + two PROVED lemmas) alongside thm:C/lem:contA: (i) §1.3 (sectors with Tate = primitive background of a single window, by translation invariance); (ii) §1.4 (the per-block Tate conditions cancel the 2e^{−u/2} term of the Lévy kernel; the residual coupling has kernel K₁ ≤ 1/u); (iii) the near-kernel of W_T is, to 99%, a combination of e^{±x/2}1_B (k = 5…13 blocks). First verify against eq:form, thm:A and lem:K (what is implemented is exactly that).
- Do not integrate "uniform 4×4 reduction": NO-GO (c → 0.013). Do not integrate any sign claim.
- Labels: §1.1–1.4 PROVED; tables NUMERICAL; (L1) decomposition PROVED, pieces (a),(b) OPEN, (c) PROVED; (L2) OPEN; fixed-E reduction NO-GO (deciding number: c(0.69) = 0.013 with dim E = 4; c(½log5) = 0.0014 n.c. / 0.16 with equal thirds).
