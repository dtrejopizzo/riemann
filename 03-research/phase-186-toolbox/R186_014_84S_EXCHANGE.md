# R186.014 — (84)_S: trace/series exchange and semilocal diagonal cancellation, S = {∞,2}

Model and notation of R186.009/010/012: H = L²(ℝ₊,du), P = 1_{(0,λ]}, F ∈ {F_∞, F_S} a self-adjoint unitary involution with Fϑ(ρ)F = ϑ(ρ⁻¹) (L0), F_S = I·M(D), M = m_∞U (R186.010 R), P̂_F = FPF, Q₁ = 1−P, Q₂^F = 1−P̂_F, A_F = PFP, Π_F = orthogonal projection onto ran Q₁ ∩ ran Q₂^F (Sonin), X := P̂_S − P̂_∞.
## Status

| # | Statement | Label |
|---|---|---|
| T1 | ϑ(f)Π_F ∈ S₁ and ϑ(f)N_F ∈ S₁ for all f ∈ C_c^∞(ℝ*₊), N_F := Σλ_n²\|ζ_n⟩⟨ζ_n\| | PROVED (given TC′, R186.010) |
| T2 | ϑ(f)X ∈ S₁; Θ₀₁ := Pϑ(f)(1−P), Θ₁₀ := (1−P)ϑ(f)P ∈ S₁; A_∞ ∈ S₁ | PROVED (Simon, Trace Ideals Thm 4.5, CITED) |
| T3 | **Pϑ(f)P·A_S² ∈ S₁**, hence Σ_nλ_n²⟨ξ_n\|ϑ(f)ξ_n⟩ converges absolutely even though Σλ_n² = ∞ | PROVED |
| T4 | **Halmos series**: E_F(f) := Σ_n τ_n(⟨ξ_n\|ϑ(f)ζ_n⟩ + ⟨ζ_n\|ϑ(f)ξ_n⟩), τ_n = λ_n(1−λ_n²)^{−1/2}, converges absolutely for every f ∈ C_c^∞; E_S(f) = ∫f(ρ⁻¹)d_S(ρ)d*ρ with d_S ∈ L^p_loc from R186.012 | PROVED (identification with d_S: R186.012 R1 + R186.097) |
| **Δ** | **Tr ϑ(f)Π_S − E_S(f) = Tr ϑ(f)Π_∞ − E_∞(f) − comb₂(f)**, comb₂(f) := Tr ϑ(f)X = Σ_{k≥1} log2·2^{−k/2}(f(2^k)+f(2^{−k})) (C′) | **PROVED** (all λ; no CV_S) |
| **(84)_S** | Tr ϑ(f)Π_S = W_S(f) + ∫f(ρ⁻¹)ε_S(ρ)d*ρ, W_S := W_∞ − comb₂, ε_S := d_S | **PROVED** given CC Thm 4.7 (CITED) at CC's level λ; for other λ see audit note (4) |
| Cor | κ_S := ε_S − ε_∞ is an L^p_loc function (no longer a definition by difference); R′_S = −C_{ε_S} HS on L²(I_T) ∀T | PROVED (R186.012 L2_S + (84)_S) |
| Step 1 | Route via θ_S / G⁻¹ | unnecessary (T1 has a one-line proof); not used |

**Verdict.** (84)_S is **PROVED** for S = {∞,2}. The CC (89)–(90) diagonal cancellation is replaced by an argument with no conditional convergence: (i) CC's per-n identity (87) is exact for symmetric f because then [F,ϑ(f)] = 0; (ii) the four series (ξ diagonal, two cross terms, ζ diagonal) are **each individually absolutely convergent**, because each is the trace, in an orthonormal basis, of a trace-class operator. The new piece is T3: the semilocal ξ diagonal Σλ_n²⟨ξ_n|ϑ(f)ξ_n⟩ converges absolutely **despite** Σλ_n² = ∞, because Pϑ(f)P(A_S² − A_∞²) is the compression of ϑ(f)X (trace class: the comb is a geometric sum of translations) and A_∞ is trace class. CV_S is no longer a hypothesis: series (84)_S converges absolutely **against every test**, and its density is d_S.

## 0. Blocks

H = H₀ ⊕ H₁, H₀ = ran P, H₁ = ran(1−P). F = [[A, B^*],[B, C]], B = (1−P)FP. F² = 1 gives A² + B^*B = 1_{H₀}, BA + CB = 0, BB^* + C² = 1_{H₁}. {ξ_n} a real orthonormal basis of H₀ of eigenvectors of A (A compact self-adjoint real: F_∞ is the cosine, U = e^{iφ(D)} with φ odd is real), |λ_n| ≤ λ₁ < 1 (R186.007/009). s_n := (1−λ_n²)^{1/2} > 0, ζ_n := Bξ_n/s_n: real orthonormal in H₁ and Fξ_n = λ_nξ_n + s_nζ_n; B^*ζ_n = s_nξ_n; the closure of span{ζ_n} is (ker B^*)^⊥ ∩ H₁. Halmos (R186.009 D, PROVED):
 Q₁Q₂Q₁ = C² = 1_{H₁} − BB^*, Π_F = 1_{H₁} − Σ_n|ζ_n⟩⟨ζ_n|, N_F := Q₁Q₂Q₁ − Π_F = Σ_nλ_n²|ζ_n⟩⟨ζ_n|.
Blocks of P̂ = FPF: P̂ = [[A², AB^*],[BA, BB^*]]. Blocks of ϑ(f): Θ₀₀, Θ₀₁, Θ₁₀, Θ₁₁.
Coefficients: a_n(f) = ⟨ξ_n|ϑ(f)ξ_n⟩, z_n(f) = ⟨ζ_n|ϑ(f)ζ_n⟩, c_n(f) = ⟨ξ_n|ϑ(f)ζ_n⟩, c′_n(f) = ⟨ζ_n|ϑ(f)ξ_n⟩.

Fact used repeatedly (trace in an adapted basis): if T ∈ S₁, Tr T = Σ_e⟨e|Te⟩ in **any** orthonormal basis, with absolute convergence (Σ|⟨e|Te⟩| ≤ ‖T‖₁).

## 1. T1 (PROVED)

ran Π_F ⊂ ran Q₁ ∩ ran Q₂ ⇒ Q₁Q₂Q₁Π_F = Π_F. Hence ϑ(f)Π_F = [ϑ(f)Q₁Q₂Q₁]·Π_F ∈ S₁ by TC′ (R186.010; S = ∅ is the archimedean case). ϑ(f)N_F = ϑ(f)Q₁Q₂Q₁ − ϑ(f)Π_F ∈ S₁. In the basis {ξ_n} ∪ {ζ_n} ∪ (orthonormal basis of ker B^* ∩ H₁):
 Tr ϑ(f)N_F = Σ_nλ_n² z_n(f) (absolutely convergent). (1.1)
This is CC's (90) in rigorous form; it does not require Σλ_n² < ∞. ∎
(Remark: the route via θ_S and G⁻¹ is correct in spirit but unnecessary; also c = (1−2^{−1/2})² is the lower bound of |L₂|², not used.)

## 2. T2 (PROVED)

In the variable t = log u (W unitary), ϑ(f) = κ_f(D), κ_f ∈ 𝒮 (f ∈ C_c^∞), and its kernel k_f ∈ C_c^∞. Simon, Trace Ideals, Thm 4.5 (CITED): g(x)h(−i∇) ∈ S₁ if g,h ∈ ℓ¹(L²)(ℝ), with ‖·‖₁ ≤ C‖g‖_{ℓ¹L²}‖h‖_{ℓ¹L²}.
(a) Θ₀₁, Θ₁₀: if supp k_f ⊂ [−L,L], Θ₀₁ = 1_{[a−L,a]}ϑ(f)1_{(a,a+L]}, a compression of ϑ(f)1_J ∈ S₁ (J bounded). Θ₁₀ likewise.
(b) ϑ(f)X: with F = IM(D), M̌(s) := M(−s): P̂_F = M̌(D)1_{t≥−a}M̌(D)^*. Since M̌_S = m̌_∞Ǔ: X = m̌_∞[Ǔ, 1_{t≥−a}]Ǔ^*m̌_∞^*. Ǔ(D) = Σ_n u_n T_{h_n}, h_n = ±nc, c = log 2, Σ|u_n|(1+|n|) < ∞ (R186.008 §4). [T_h, 1_{t≥b}] = ±1_{J_h}T_h, |J_h| = |h|. ϑ(f) commutes with m̌_∞(D). Hence
 ‖ϑ(f)X‖₁ ≤ Σ_n|u_n|·‖ϑ(f)1_{J_{h_n}}‖₁ ≤ C_f Σ_n|u_n|(|n|c + 2) < ∞.
(c) A_∞ ∈ S₁: kernel 2cos(2πux) on (0,λ]²; cos(2πux) = Σ_k(−1)^k(2πux)^{2k}/(2k)! is a sum of rank-one terms with Σ_k(2π)^{2k}λ^{4k+1}/(2k)! < ∞ in nuclear norm. ∎

## 3. T3 (PROVED)

Pϑ(f)XP ∈ S₁ (T2b) and Pϑ(f)XP = Θ₀₀X₀₀ + Θ₀₁X₁₀ with Θ₀₁ ∈ S₁; hence Θ₀₀X₀₀ = Θ₀₀(A_S² − A_∞²) ∈ S₁. With Θ₀₀A_∞² ∈ S₁ (T2c): **Θ₀₀A_S² ∈ S₁**, and in the basis {ξ_n^S}: Tr Θ₀₀A_S² = Σ_nλ_n²a_n(f), absolutely convergent. ∎
(Does not contradict R186.009 Prop. d: that result is about L^∞-unboundedness of the density; T3 is finiteness against each smooth test.)

## 4. The cross series and T4 (PROVED)

Θ₀₁BA ∈ S₁ (on H₀), BAξ_n = λ_ns_nζ_n ⇒ Tr Θ₀₁BA = Σλ_ns_nc_n(f). Θ₁₀AB^* ∈ S₁ (on H₁), AB^*ζ_n = λ_ns_nξ_n, AB^* = 0 on ker B^* ⇒ Tr Θ₁₀AB^* = Σλ_ns_nc′_n(f). Both absolutely convergent.
G := BA(1−A²)^{−1} (bounded, ‖G‖ ≤ λ₁/(1−λ₁²)), Gξ_n = τ_nζ_n. E⁺_F(f) := Tr(Θ₀₁G) = Σ_nτ_nc_n(f) and Tr(Θ₁₀G^*) = Σ_nτ_nc′_n(f): absolutely convergent. For real f, c′_n(f) = c_n(f̃), f̃(ρ) := f(ρ⁻¹) (real vectors and kernels, ϑ(f)^* = ϑ(f̃)); hence E_F(f) = E⁺_F(f) + E⁺_F(f̃), extended linearly to every f.
Identification: E⁺_S(f) = Tr(Θ₀₁G) is **exactly** the pairing Tr(K_fG) of R186.012 R1 as accepted in R186.097 (K_f the kernel of Pϑ(f)(1−P)); hence E_S(f) = ∫f(ρ⁻¹)d_S(ρ)d*ρ, d_S ∈ L^p_loc ∀p < ∞ (L2_S, Lp). For F_∞: the τ_n are summable (super-exponential λ(n), CC) and |⟨ξ_n|ϑ(ρ)ζ_n⟩| ≤ 1 give uniform convergence of CC's (84); Fubini ⇒ E_∞(f) = ∫f(ρ⁻¹)ε_∞(ρ)d*ρ. ∎

## 5. Per-n identity and Φ_F = E_F (PROVED, real symmetric f)

Let f be real with f̃ = f. Then Fϑ(f)F = ϑ(f̃) = ϑ(f): **[F,ϑ(f)] = 0**. For each n: a_n = ⟨ξ_n|Fϑ(f)Fξ_n⟩ = ⟨Fξ_n|ϑ(f)Fξ_n⟩ = λ_n²a_n + λ_ns_n(c_n+c′_n) + s_n²z_n, hence (s_n > 0)
 z_n = a_n − τ_n(c_n + c′_n) (CC (87), exact, not summed). (5.1)
Define Φ_F(f) := Tr Θ₀₀A² + Tr Θ₀₁BA + Tr Θ₁₀AB^* − Tr ϑ(f)N_F: all four terms exist (T3 for F_S, T2c for F_∞, §4, T1) and are absolutely convergent series in n; summing term by term (legitimate) and using (5.1):
 λ²a + λs(c+c′) − λ²z = (c+c′)(λs + λ²τ) = τ(c+c′) (CC note 8),
 **Φ_F(f) = Σ_nτ_n(c_n+c′_n) = E_F(f).** (5.2)
This is the semilocal diagonal cancellation (CC (89)–(90)): the term λ²a_n of the ξ diagonal cancels exactly against the λ²z_n of N_F, term by term, between absolutely convergent series. ∎

## 6. Δ (PROVED)

Q₁Q₂^SQ₁ − Q₁Q₂^∞Q₁ = −(1−P)X(1−P), and ϑ(f)(1−P)X(1−P) ∈ S₁ (difference of two TC′ terms). (1−P)X(1−P) = X − XP − PX(1−P); ϑ(f)X, ϑ(f)XP ∈ S₁ (T2b), hence ϑ(f)PX(1−P) ∈ S₁. Traces in a basis adapted to H₀ ⊕ H₁:
 Tr ϑ(f)XP = Tr Θ₀₀X₀₀ + Tr Θ₀₁X₁₀, Tr ϑ(f)PX(1−P) = Tr Θ₁₀X₀₁,
with X₀₀ = A_S² − A_∞², X₁₀ = B_SA_S − B_∞A_∞, X₀₁ = A_SB_S^* − A_∞B_∞^*; each of the six summands is S₁ individually (T3, T2a). With Π_F = Q₁Q₂Q₁ − N_F and T1:
 Tr ϑ(f)(Π_S − Π_∞) = −Tr ϑ(f)X + [Φ_S(f) − Φ_∞(f)] = −comb₂(f) + E_S(f) − E_∞(f)
for real symmetric f, by (5.2) and C′ (R186.008, PROVED). If f real and f̃ = −f: Tr ϑ(f)Π_F = Tr ϑ(f)FΠ_FF = Tr(Fϑ(f)FΠ_F) = −Tr ϑ(f)Π_F = 0 (FΠ_F = Π_FF: Sonin is F-invariant), E_F(f) = 0, comb₂(f) = 0: Δ holds trivially. Every f ∈ C_c^∞ is a linear combination of a real symmetric and an antisymmetric part; both sides are linear. ∎

## 7. (84)_S (PROVED given CC Thm 4.7)

CC Thm 4.7 (CITED): Tr ϑ(f)Π_∞ = W_∞(f) + ∫f(ρ⁻¹)ε_∞(ρ)d*ρ = W_∞(f) + E_∞(f) (§4). Substituting into Δ:
 **Tr ϑ(f)Π_S = W_∞(f) − comb₂(f) + ∫f(ρ⁻¹)d_S(ρ)d*ρ, f ∈ C_c^∞(ℝ*₊).**
With f = g*g^*: Son_S(g) = W_S(f) + ∫f(ρ⁻¹)ε_S(ρ)d*ρ, ε_S = d_S. Consequences: Δ is now a theorem (κ_S = d_S − ε_∞ ∈ L^p_loc, with ε_∞ continuous); by R186.012 L2_S (log⁺ ∈ L²_loc), R′_S = −C_{ε_S} is HS on L²(I_T) for every T (L1′/(E′_loc), not the microlocal (M) of R183_029); n₋(−C_{ε_S}|𝒫_T) < ∞ ∀T. Nothing about the sign.

## Audit notes

1. §5: the symmetrization is essential: (5.1) uses [F,ϑ(f)] = 0, which only holds for f̃ = f. The reduction to real symmetric f (§6) uses: reality of F_S (multiplier of the factor-of-2 conjugate under t ↦ −t), the real basis {ξ_n}, and FΠ_F = Π_FF.
2. T3 is the delicate point: check Pϑ(f)XP = Θ₀₀X₀₀ + Θ₀₁X₁₀ (inserting 1 = P + (1−P) between ϑ(f) and X) and that A_∞ ∈ S₁ in the normalization of R186.007 (kernel 2cos 2πux on (0,λ]²).
3. T2b: Σ|u_n|(1+|n|) < ∞ with u_n from R186.008 §4; the translation sign convention does not affect |J_h| = |h|.
4. CC Thm 4.7 is stated for Sonin S(1,1) on L²(ℝ)^ev (CC (43), (53), (83)). Δ holds for **every** λ without CC; (84)_S in absolute form requires CC 4.7 at the level λ used (λ = ½ in R186.007, λ in R186.012). If λ ≠ CC's level, read W_∞^{(λ)} := Tr ϑ(f)Π_∞ − E_∞(f) (CC (43) at level λ, not checked here): the relative statement Δ and all corollaries about ε_S, κ_S, R′_S are independent of this point.
5. Normalization of comb₂ = C′ with the ϑ(h) convention of R186.008; compare the sign with the prime term of R183_018 (W_S = W_∞ − comb₂ per R186.008 §3/§4 remark 3).
6. CV_S is not used, nor pointwise convergence of series (84)_S, nor the edge-mass bound: the series converges absolutely against every test (it is the trace of an S₁ operator in an orthonormal basis), and the density is d_S by R186.012 R1.
7. No equivalence with RH is claimed, nor anything about the sign of E_S.

## For Paper 46

Proposition (semilocal Sonin formula, S = {∞,2}). For f ∈ C_c^∞(ℝ*₊), ϑ(f)Π_S is trace class and Tr ϑ(f)Π_S = W_∞(f) − Σ_{k≥1}log2·2^{−k/2}(f(2^k)+f(2^{−k})) + ∫f(ρ⁻¹)ε_S(ρ)d*ρ, with ε_S(ρ) = Σ_nλ_n(1−λ_n²)^{−1/2}⟨ξ_n|ϑ(ρ⁻¹)ζ_n⟩ (ρ ≥ 1, symmetric), a series absolutely convergent against every test, of density ε_S ∈ L^p_loc ∀p < ∞. One-page proof: §1 (T1), §2–3 (T3: compression of ϑ(f)X), §5 (per-n identity with [F,ϑ(f)] = 0), §6. Labels: Δ PROVED; (84)_S PROVED given CC Thm 4.7 (CITED); R′_S HS ∀T PROVED. No equivalence with RH.

## Note (R186_098)

* Δ (relative) PROVED ∀λ with no CV_S. (84)_S absolute and "R′_S HS ∀T" PROVED given CC Thm 4.7 at level λ=½ (CITED, range of λ not checked; write out the dictionary L²(ℝ)^ev ↔ L²(ℝ₊,du): √2, kernel 2cos2πux, convention ϑ, f(ρ) vs f(ρ⁻¹)). −C_{κ_S} HS ∀T unconditional. T1–T4, §5, Δ, sign of comb₂ verified. MINOR: d_S(ρ) := d_S(ρ⁻¹) for ρ<1; distributional identification R1; remove the remark about c; Dixmier–Malliavin CITED.

## Note (Paper 46 CHECK_TABLE II)

* N1: CC Thm 4.7 is for S(1,1) = λ=1, not λ=½; the absolute form of (84)_S and its corollary hold only at λ=1; for λ≠1, CONDITIONAL. N3: "−C_{ε_S} compact ⇒ n₋<∞" does not follow; only n₋(𝔞_T − Son_S + δ‖·‖²) < ∞ ∀δ>0. N4: E_S = 𝔞_T only if T<½log3.

## Note (R186_017)

* Absolute form of (84)_S at every level λ: Tr ϑ(f)Π_{S(λ,λ)} = W_∞(f) + 2log(1/λ)f(1) + ∫fε_λ (D3). N1 is resolved this way; λ=½ valid with the extra term.
