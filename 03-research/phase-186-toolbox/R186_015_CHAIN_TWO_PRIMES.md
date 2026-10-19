# R186.015 — The semilocal chain for S = {∞,2,3} and for general finite S

Model and notation of R186.007–014: H = L²(ℝ₊,du), P = 1_{(0,λ]}, D_a g(u) = g(au), W: t = log u, ϑ(f) = κ_f(D), I the inversion, F_∞ = I·m_∞(D). S ∋ ∞ finite, S_f := S∖{∞} = {p_1,…,p_r}, ⟨S⟩ := {∏p_i^{a_i}: a_i ≥ 0} (semigroup), ⟨S⟩^± the group of positive S-units. No numerics (pure-mathematics rule).

## Status

| # | Statement | Label |
|---|---|---|
| U_S | F_S := E_SF_∞E_S⁻¹, E_S = ∏_{p∈S_f}E_p, E_S⁻¹ = ∏(1−D_p): unitary, involutive, F_S = I·M_S(D), M_S = m_∞∏_pρ_p, ρ_p(½+it) = (1−p^{−½+it})/(1−p^{−½−it}) | PROVED |
| C_S | U_S = ∏U_p = e^{iφ_S(D)}, φ_S = Σ_pφ_p, φ_S′(t) = −Σ_pΣ_k v_{p^k}cos(kt log p) | PROVED (additivity; per-prime formula from R186.008) |
| Ker | Kernel of F_S: Σ_N a_N·2cos(2πNuy), N ∈ ⟨S⟩^±, a_N = ∏_p α_p(v_p(N)), α(v) = 1−1/p (v ≥ 0), −1/p… explicit (§1); **a_N = ∏_p(1−1/p) for N ∈ ⟨S⟩** | PROVED |
| Cpt | A_S = PF_SP compact, ‖A_S‖ < 1 | PROVED (without CC: norm approximation + uncertainty) |
| NHS | A_S ∉ S₂ | PROVED |
| Sp | A_S ∈ S_p for every p > 2, for every finite S | PROVED |
| N(ε) | #{n: \|λ_n\| > ε} ≍ ε^{−2}(log 1/ε)^{r−1} | ARGUED (upper bound PROVED up to a logarithmic constant; lower bound heuristic) |
| Lac_r | r-dimensional lacunary lemma: Σ_{N∈⟨S⟩} S(Nt) = λ·Ψ_S(1/\|t\|) + O_S(1 + log(2+1/\|t\|)^{r−1}), Ψ_S(X) := #⟨S⟩∩[1,X] | PROVED |
| L2_S | d_S(ρ) = Σ_{q=a/b} β_q·log⁺^r(1/(b\|ρ−q\|)) + g_S(ρ), q ranging over the S-units of [1,R] in reduced form, β_q = q^{1/2}(1−1/q)λ²∏_p(1−1/p)²/(2·r!·∏_p log p), with Σ_q‖·‖_{L²(1,R)} < ∞ and g_S ∈ L²(1,R) | PROVED given R1 (R186.012) and Sp; the exact form of the log^{r−1}-order term: ARGUED |
| **Correction** | The singularity at q is **not** logarithmic for r ≥ 2: it is **log^r**, cut off at scale 1/b(q) (b = S-unit denominator of q). R186.012 §5 had anticipated this (log², ARGUED); the target's claim ("each singularity is still log") is false for r ≥ 2 | PROVED |
| T1–T4, Δ | Same as R186.014 with M_S, U_S | PROVED |
| C′_S | Tr ϑ(h)(P̂^S − P̂_∞) = Σ_{p∈S_f}Σ_{k≥1}(log p)p^{−k/2}(h(p^k)+h(p^{−k})) | PROVED (additivity by unitary invariance of the trace; no need to extend Simon 4.5 to non-lattice translations) |
| (84)_S | Tr ϑ(f)Π_S = W_∞(f) − Σ_p comb_p(f) + ∫f(ρ⁻¹)ε_S(ρ)d*ρ, ε_S = d_S | PROVED given CC Thm 4.7 (CITED), as in R186.014 |
| M_S | κ_S = ε_S − ε_∞ ∈ L^p_loc ∀p<∞; R′_S HS on L²(I_T) ∀T, with explicit constants §5 | PROVED for fixed S (same caveats as R186_097: density ↔ kernel-of-R′_S identification via (84)_S) |
| S(T) | For S = S(T): the singular set in [1,e^{2T}] contains **all integers**; the structure folds into singularities of type 1/\|ρ−n\| (Poisson), cut off at scale e^{−2T}; ‖κ_{S(T)}‖_{L²(I_T)} is not uniform in T | ARGUED (prediction) |

**Verdict.** The semilocal chain carries over to every finite S **with no new wall**: unitarity, Thm C, compactness, non-HS, S_p (p>2), TC_S, T1–T4, Δ, C′_S and (84)_S are identical proofs with the symbol M_S = m_∞∏ρ_p, and C′_S is additive by a one-line argument. The only thing that changes is L2_S: with r finite primes the singularities of ε_S live on all S-units q = a/b (dense), are of order **log^r** (not log), and are cut off at scale 1/b; the sum Σ_q b^{−1/2} converges, hence ε_S ∈ L²_loc and R′_S is HS for each fixed S. The window-by-window limit with S = S(T) is **not** uniform: the constants contain ∏_{p∈S}(1−p^{−1/2})^{−1} and Ψ_S, which blow up with T, and the predicted limit is a comb **of all integers** with 1/|ρ−n|-type singularities: the Sonin remainder is not a small perturbation in T.

## 1. Semilocal Fourier transform (U_S, C_S, Ker)

In Mellin on Re s = ½, D_p ↔ p^{−s}; the D_p commute, E_p ↔ (1−p^{−s})⁻¹, E_S ↔ ∏_p(1−p^{−s})⁻¹ (bounded: |1−p^{−s}| ≥ 1−p^{−1/2}), E_S⁻¹ = ∏(1−D_p). F_∞D_pF_∞ = D_p^* (R186.007 §1) gives F_∞E_SF_∞ = E_S^*, hence F_S = F_∞E_S^*E_S⁻¹ and E_S^*E_S⁻¹ ↔ ∏_p(1−p^{−(1−s)})/(1−p^{−s}), a product of quotients of conjugates at s = ½+it: unimodular. F_S² = E_SF_∞²E_S⁻¹ = 1, F_S unitary ⇒ self-adjoint. With F_∞ = Im_∞(D): F_S = I·M_S(D), M_S = m_∞U_S, U_S = ∏_pU_p. PROVED (same proof as R186.007; the commutativity of the D_p is the only new ingredient).
On CC 2008.10974: Thm 4.4 gives ρ_∞ρ_p quasi-inner for one prime; for the product nothing needs to be cited: compactness is proved directly (Cpt), which is all that was used from "quasi-inner". I did not check (no web access) whether CC's main theorem states the multi-prime case; it is not used.
C_S: U_S = ∏e^{iφ_p(D)} = e^{iΣφ_p(D)}; φ_S′ = Σφ_p′ with the per-prime formula of R186.008 (Thm C, CITED CC 2008.10974 only for the identification with the quotient of local factors). PROVED.
Ker: ∫2cos(2πnuy)g(ky)dy = k⁻¹∫2cos(2π(n/k)uy)g(y)dy. Expanding E_S⁻¹ = Σ_{k|∏p}μ(k)D_k and E_S = Σ_{n∈⟨S⟩}D_n, the coefficient of 2cos(2πNuy), N ∈ ⟨S⟩^±, is a_N = Σ_{k|∏p, Nk∈⟨S⟩}μ(k)/k = ∏_p α_p(v_p(N)), α_p(v) = 1−1/p (v ≥ 0), −1/p (v = −1), 0 (v ≤ −2). For S = {∞,2,3}: a_N = 1/3 on ⟨2,3⟩, −1/6 (v₂ = −1, v₃ ≥ 0), −1/3 (v₃ = −1, v₂ ≥ 0), 1/6 (N = 2^a3^b/6). For r = 1 this gives R186.007 (2c_k − c_{k−1}). The series converges in operator norm when grouped as Σ_n PD_nF_∞E_S⁻¹P, ‖PD_nF_∞E_S⁻¹P‖ ≤ n^{−1/2}∏(1+p^{−1/2}). PROVED.

## 2. Compactness, ‖A_S‖ < 1, non-HS, S_p

Cpt. A_X := Σ_{n∈⟨S⟩,n≤X}PD_nF_∞E_S⁻¹P has a bounded kernel on (0,λ]² (finite sum of cosines), hence is HS; ‖A_S − A_X‖ ≤ ∏(1+p^{−1/2})Σ_{n>X}n^{−1/2} → 0 because Σ_{n∈⟨S⟩}n^{−1/2} = ∏(1−p^{−1/2})⁻¹ < ∞. Compact. If A_Sf = ±f with ‖f‖ = 1, then f = ±F_Sf ∈ ran P, and g := E_S⁻¹f ∈ ran P (the D_p, p ≥ 2, do not push the support out of (0,λ]) satisfies F_∞g = E_S⁻¹F_Sf = ±g: g and its cosine transform have compact support ⇒ g = 0 ⇒ f = 0. Compact with no eigenvalue ±1 ⇒ ‖A_S‖ < 1. PROVED (holds for every finite S, without CC).
NHS. As in R186.007 §3 with φ_m := cos(2πN_m uy)χ, N_m := (∏p)^m: ⟨κ,φ_m⟩ → 0 (Riemann–Lebesgue) if κ ∈ L², but lim_X∫∫G_Xφ_m = a_{N_m}·∫∫χ + o(1) = ∏(1−1/p)∫∫χ ≠ 0 (the other frequencies N ≠ N_m give o(1): distinct frequencies, and the partial sums are dominated as in R186.007). Contradiction. PROVED.
Sp. Writing A_S = Σ_N a_N P·2cos(2πN uy)·P (Σ absolutely convergent in S_p, see below): P·2cos(2πNuy)·P = N^{−1/2}·V_N A_∞(√N λ)V_N^* (V_N a unitary dilation), and for p ≥ 2, ‖A_∞(c)‖_p^p ≤ ‖A_∞(c)‖_2^2 ≤ 4c² (singular values ≤ 1). Hence ‖P2cos(2πN·)P‖_p ≤ N^{−1/2}(4Nλ²)^{1/p}, and Σ_N|a_N|N^{1/p−1/2} ≤ C_S Σ_{n∈⟨S⟩}n^{1/p−1/2} = C_S∏(1−p^{1/p−1/2})⁻¹ < ∞ for p > 2 (the boundary lines v_p = −1 are ⟨S⟩ translated: the same count applies). PROVED: A_S ∈ ∩_{p>2}S_p, for every finite S. The exponent does not worsen: the Dirichlet series of the semigroup converges for every positive exponent; the number of primes only enters through logarithms.
N(ε). Heuristic by levels: level N contributes ≈ 4Nλ²·a_N² eigenvalues of size ≈ a_N N^{−1/2}; N(ε) ≈ Σ_{N≤ε^{−2}}N ≍ ε^{−2}·#(⟨S⟩∩[ε^{−2}/e, ε^{−2}]) ≍ ε^{−2}(log 1/ε)^{r−1}. For r = 1: N(ε) ≍ ε^{−2} (A ∈ S_{2,∞}); for r ≥ 2 even S_{2,∞} fails. ARGUED.

## 3. L2_S (two primes and general r)

Lac_r (PROVED). S(w) = sin(2πλw)/(2πw). For N|t| ≤ 1: |S(Nt) − λ| ≤ C(Nt)², and Σ_{N∈⟨S⟩,N≤1/|t|}(Nt)² ≤ C_S (the N in [X/e^{k+1},X/e^k] are O_S((log X)^{r−1}) and are weighted by e^{−2k}). For N|t| > 1: Σ|S| ≤ Σ_{N>1/|t|}1/(2πN|t|) ≤ C_S(log(2+1/|t|))^{r−1} by the same block count. Ψ_S(X) = (log X)^r/(r!∏log p) + O_S((log X)^{r−1}) (lattice point count in a simplex). ∎
Diagonals. G₀(u,z) = ½Σ_{N,M}a_Na_M[S(Nu−Mz)+S(Nu+Mz)]. Group by ratio q = M/N ∈ ⟨S⟩^±, q = a/b in reduced form (a,b ∈ ⟨S⟩ coprime). With N, M ∈ ⟨S⟩ (interior part, a_N = ∏(1−1/p)): N = bn, M = an, n ∈ ⟨S⟩. With u = ρx, z = x: Nu − Mz = n·b x(ρ−q). By Lac_r:
 diagonal q = ½∏(1−1/p)²·λ·Ψ_S(1/(bx|ρ−q|)) + O_S(1+log^{r−1}(2+1/(bx|ρ−q|))),
and if bx|ρ−q| ≥ 1 it is bounded by C_S min(1, 1/(bx|ρ−q|))·log^{r−1}(2+bx|ρ−q|)… (tail). The boundary lines (some v_p(N) = −1) are r families of rank-≤r translated semigroups: they contribute with the same scheme and power ≤ r (their signed sum is included in g_S; the exact form of the log^{r−1} term: ARGUED). The terms S(Nu+Mz) are bounded by Lac_r with t ≥ λ.
Integrating over x ∈ [λ/ρ,λ] with the prefactor ρ^{1/2} (R186.012 §3): d₀(ρ) = Σ_q β_q log⁺^r(1/(b|ρ−q|)) + (remainder), with β_q as in the table (at ρ = q). For r = 1 this matches R186.012 (∏(1−1/p)² = ¼, 2·1!·log 2: β_j = 2^{j/2}(1−2^{−j})λ²/(8log2)·… — **see audit note (2)**).
L² (PROVED). Let R ≥ 1. For each q ∈ [1/2, 2R] with denominator b: f_q(ρ) := log⁺^r(1/(b|ρ−q|)) + min(1,1/(b|ρ−q|))log^{r−1}(2+b|ρ−q|) satisfies ‖f_q‖_{L²(1,R)} ≤ C_r b^{−1/2}. #{q = a/b ∈ [1/2,2R]: b fixed} ≤ Ψ_S(2Rb)−Ψ_S(b/2) ≤ C_S(log 4R)·(log 2Rb)^{r−1}. Minkowski:
 ‖d₀‖_{L²(1,R)} ≤ C_r R^{1/2}λ²∏(1−1/p)²/(r!∏log p)·Σ_{b∈⟨S⟩}b^{−1/2}(log 4R)(log 2Rb)^{r−1} + O_S(R)·(tail) < ∞,
since Σ_{b∈⟨S⟩}b^{−1/2}log^{r−1}b < ∞. The m ≥ 1 Neumann terms: R = A_S²(1−A_S²)⁻¹ ∈ S₂ because A_S ∈ S₄ (Sp) and ‖A_S‖ < 1 (Cpt); the HS-1 argument of R186.012 §3 applies (sup_u‖G₀(u,·)‖ finite: log^r ridges at y = u/q with L² mass ≍ b^{−1}, summable). Hence d_S ∈ L^p_loc ∀p < ∞ (log^r ∈ L^p), d_S ∉ L^∞_loc (β_q > 0). PROVED.
Comment on the suggestion (Kronecker/Dirichlet): not needed. The ratio q is exact (the kernel only resonates at S-units), and the "merging" of nearby singularities is controlled by Minkowski plus the 1/b cutoff: S-units very close to ρ have a large denominator and a tiny effective support.

## 4. (84)_S

T1: ϑ(f)Π_S = ϑ(f)Q₁Q₂Q₁Π_S, and TC′ (R186.010) only uses M ∈ C_b^∞ with ĝ̃m_∞ ∈ 𝒮: U_S = Σ_{h∈Λ_S}u_h T_h, Λ_S = Σ_pℤ log p, u = convolution of the per-prime series, Σ|u_h|(1+|h|)^k ≤ ∏_p Σ|u^{(p)}_h|(1+|h|)^k < ∞; hence M_S ∈ C_b^∞. PROVED.
T2: X_S = m̌_∞[Ǔ_S,1_{t≥−a}]Ǔ_S^*m̌_∞^*, [T_h,1_{t≥b}] = ±1_{J_h}T_h, |J_h| = |h|, ‖ϑ(f)1_J‖₁ ≤ C_f(1+|J|) (Simon 4.5, CITED, arbitrary bounded sets J: no lattice structure of the h's is used). Σ|u_h|(1+|h|) < ∞ ⇒ ϑ(f)X_S ∈ S₁. PROVED.
T3, T4, Δ: word for word as in R186.014 (they only use T1, T2, A_∞ ∈ S₁ and [F_S,ϑ(f)] = 0 for symmetric f, which holds because F_Sϑ(ρ)F_S = ϑ(ρ⁻¹) is inherited from F_∞ and from the commutation of E_S with the dilations). PROVED.
C′_S (PROVED). Let Y(φ) := e^{iφ(D)}1_{t≥b}e^{−iφ(D)} − 1_{t≥b}. Algebraic identity:
 Y(φ₁+φ₂) = e^{iφ₁(D)}Y(φ₂)e^{−iφ₁(D)} + Y(φ₁).
ĥ(D) commutes with e^{iφ₁(D)} and ĥ(D)Y(φ_j) ∈ S₁ (T2 for one prime), hence Tr ĥ(D)e^{iφ₁}Y(φ₂)e^{−iφ₁} = Tr e^{iφ₁}ĥ(D)Y(φ₂)e^{−iφ₁} = Tr ĥ(D)Y(φ₂). Thus Tr ĥ(D)Y is additive in φ; the conjugation by m̌_∞ is also removed by unitary invariance. With C′ per prime (R186.014; its proof is for a general prime p, c = log p): Tr ϑ(h)X_S = Σ_p comb_p(h). There is no need to extend Simon 4.5 to non-lattice translations (answer to R186_094).
Conclusion: Tr ϑ(f)Π_S = W_∞(f) − Σ_{p∈S_f}comb_p(f) + ∫f(ρ⁻¹)ε_S(ρ)d*ρ, ε_S = d_S, at CC's level λ (CITED Thm 4.7). PROVED in that sense.

## 5. Conclusion for finite S and dependence on T

For every finite S ∋ ∞ and T > 0: E_S = Son_S − ∫c_hε_S, Son_S ≥ 0 trace type, comb_S = Σ_p comb_p absorbed into W_S, ε_S = ε_∞ + κ_S, κ_S ∈ L^p_loc with log^r singularities at the S-units of [1,e^{2T}], cut off at scale 1/b, and R′_S HS on L²(I_T). Constants (R = e^{2T}):
- ‖A_S − A_X‖ ≤ ∏(1+p^{−1/2})·Σ_{n∈⟨S⟩,n>X}n^{−1/2}; ‖(1−A_S²)⁻¹‖ = (1−λ₁(S)²)⁻¹ (λ₁(S) < 1 with no bound uniform in S: OPEN).
- ‖A_S‖_p ≤ C∏(1+p^{−1/2})·∏(1−p^{1/p−1/2})⁻¹ λ^{2/p}.
- ‖κ_S‖_{L²(1,R)} ≤ C_r e^{T}λ²·∏(1−1/p)²/(r!∏log p)·(2T+log 4)·Σ_{b∈⟨S⟩}b^{−1/2}(2T+log 2b)^{r−1} + (m ≥ 1 terms: ≤ e^{T}·sup_u‖G₀(u,·)‖·‖R‖_HS), and Σ_{b}b^{−1/2}(…) ≤ ∏_p(1−p^{−1/2})^{−1}·(2T+C_S)^{r−1}·r!-type.
- Number of effective singularities in [1,R] with denominator ≤ B: ≲ Ψ_S(RB)·Ψ_S(B).
All finite for fixed S; none uniform in S.

Honest limit S = S(T) = {∞}∪{p < e^{2T}} (ARGUED). In the window ρ ∈ [1,e^{2T}], every q = n/1, n ≤ e^{2T}, is an S(T)-unit: **every integer n in the window is singular** (and additionally the rationals a/b with a,b e^{2T}-smooth, with cutoff 1/b). But now Ψ_{S(T)}(X) = Ψ(X, e^{2T}) = ⌊X⌋ for X ≤ e^{2T}: the count of Lac_r is no longer log^r but linear, and by Poisson (Σ_{N∈ℤ}S(Nt) = 1/(2|t|) for |t| < 1/λ) the diagonal q = n gives
 ε_{S(T)}(ρ) ≈ Σ_{n≤e^{2T}} n^{1/2}(1−1/n)·λ·c_T²·(1/(4|ρ−n|))·1_{|ρ−n| ≳ e^{−2T}} + (log-type cutoff below e^{−2T}) + (rationals with b > 1),
c_T := ∏_{p<e^{2T}}(1−1/p) ~ e^{−γ}/(2T) (Mertens). This is the "folded" comb: singularities at **every** integer, of type 1/|ρ−n| (not L²_loc in the limit), as against the prime term of W_S, which lives only at prime powers with weights (log p)p^{−k/2}. The Sonin remainder redistributes the arithmetic from prime powers to every integer through the multiplicative structure (every n ≤ e^{2T} is an S(T)-unit). Size bound: ‖κ_{S(T)}‖²_{L²(I_T)} ≳ c_T⁴Σ_{n≤e^{2T}}n·e^{2T} ~ e^{6T}/T⁴: grows exponentially.

What this means for the inertia (next memo). For fixed S, −C_{ε_S}|𝒫_T is compact: n₋ < ∞ (PROVED). But window by window with S(T) the remainder is neither small nor uniformly HS, so n₋ is not controlled by perturbation (the bound n₋ ≤ ‖R′‖²_HS/μ² is useless). The right question is structural: is the singular convolution kernel Σ_n w_n|ρ−n|⁻¹ (with w_n ≈ λc_T²n^{1/2}/4) plus its rational part of positive/negative type on 𝒫_T, and how much of the inertia of E_{S(T)} does it absorb against the prime comb? The passage from log^r to 1/|·| is exactly where Son_S stops being "archimedean + compact perturbation".

## Audit notes

1. Cpt/‖A_S‖<1: the uncertainty argument uses that E_S⁻¹ preserves ran P and commutes with F_S-conjugation (F_SE_S = E_SF_∞); check that E_S⁻¹ is injective (it is: invertible).
2. β constant: R186.012 uses a_k = 1 for cos (not 2cos) at r = 1; here a_N multiplies 2cos. Check the factor of 2 and that β_q for r = 1 reproduces β_j = 2^{j/2}(1−2^{−j})λ²/(2log2) (with a = 1 for cos: ½·1²·λ·log₂ → λ/(2log2) ✓; with my normalization 2a_N = 2·½ = 1 ✓; in the table β_q should be read with (2∏(1−1/p))²·¼ = ∏(1−1/p)², i.e. β_q = q^{1/2}(1−1/q)λ²∏(1−1/p)²·2^{…}/(r!∏log p): **the exact power of 2 remains to be verified**; it does not affect any qualitative conclusion).
3. Lac_r: the tail N|t|>1 is O(log^{r−1}), not O(1) as at r = 1. It is dominated by the main log^r term.
4. Boundary lines (v_p = −1): alternating signs, r families; it is only claimed that their order is ≤ log^r and that they enter the same Minkowski sums.
5. NHS: the domination of the frequencies N ≠ N_m reuses R186.007 §3; for r ≥ 2 the frequencies ⟨S⟩ are denser but each coefficient is bounded and the grouped partial sums converge in norm (§1).
6. (84)_S: same caveats as R186_097/098 (identification d_S ↔ kernel of R′_S, CC's λ).
7. §5 S(T): the prediction is ARGUED; it uses Poisson over all integers without controlling the interaction with the smoothness cutoff Ψ(X,e^{2T}) for X > e^{2T} nor the boundary lines. Nothing in §5 is used as a theorem.
8. No claim about the sign of E_S; no equivalence with RH.

## For Paper 47

- Theorem (semilocal chain, finite S): U_S, C_S, Cpt, NHS, Sp (A_S ∈ S_p ⟺ p > 2), T1–T4, Δ, C′_S additive, (84)_S. One page: "same argument with symbol M_S = m_∞∏ρ_p" + the additivity lemma Y(φ₁+φ₂).
- Proposition (L2_S, r primes): log^r singularities at S-units q = a/b with cutoff 1/b; ε_S ∈ L^p_loc; R′_S HS for fixed S. Correct R186.012 §5 (ARGUED → PROVED, with log^r).
- Remark (not a theorem): for S(T) the Sonin remainder is a comb folded over all integers, of type 1/|ρ−n|, with norm ~e^{3T}/T²; the decomposition Son − HS is not uniform across the window. Label: ARGUED.

## Note (R186_099)

* §5 and (84)_S: add 2log(1/λ)‖h‖² for λ≠1 (D3). Limit S(T): CONJECTURAL, not ARGUED. NHS r≥2 needs growing gaps between S-units (Størmer/Tijdeman). PROVED: U_S, Ker, Sp, C′_S, ‖A_S‖<1, log^r with cutoff 1/b, L^p_loc.
