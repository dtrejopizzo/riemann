# R186.017 — CC dictionary (83) ↔ window and resolution of C1

Input: R186.016 C1/C2, CHECK_TABLE II N1, CC (arXiv 2006.13771) §1, Prop. 2.2, (43), Def. 4.4, Thm 4.7, Thm 1. Scripts (scratchpad, not versioned): `r186_017.py` (δ_b, Ω_b, check ω ≡ 0), `r186_017b.py` (corrected test), with `r183_030_inertia.py`, `r186_013.py` and the ε grids from R186.016.

## Status

| # | Statement | Label |
|---|---|---|
| D0 | The level λ is **not** tied to the window. CC (83) holds for **every** f ∈ C_c^∞(ℝ*₊) with the fixed Sonin S(1,1); the support [2^{−1/2},2^{1/2}] of CC Thm 1 is a hypothesis of *inequality* (4), not of (83). The reading "λ = e^T" (λ = √3 for ½log3) is incorrect | PROVED (reading of CC, Thm 1 / Thm 4.7 lines) |
| D1 | u-model at λ = 1 = CC S(1,1) exactly: L²(ℝ)^ev with ⟨·,·⟩ = ∫_0^∞ (CC (16)) = L²(ℝ₊,du), even F_eR = kernel 2cos(2πux), no √2 factor. Control: eigenvalues of A_∞ at λ = 1: 0.99997, −0.97948, 0.52409, −0.05898 = λ(n) from CC; δ_1(1) = 2.2374848 = CC Obs. 4.6 | PROVED + NUMERICAL |
| D2 | Test convention: g(ρ) = h(log ρ), f = g*g^*, f(e^x) = c_h(x) = ∫h(y)h(y+x)dy, f̂(t) = \|ĥ(t)\|², f(1) = ‖h‖²_{L²(dx)}. CC W_∞(f) = −∫fτ = (1/2π)∫f̂·2θ′ = (1/2π)∫m\|ĥ\|², m = Re ψ(¼+is/2) − log π: **identical** to the window's archimedean term (r183_030). ∫f(ρ⁻¹)ε(ρ)d*ρ = ∫_ℝ c_h(a)ε(e^{\|a\|})da (= Cmat). There is no 2π discrepancy in the window; C2 (if R183_026 Prop 2.1 writes m/2π as the symbol of the *same* form (1/2π)∫\|ĥ\|²·σ) is a typographical error in that proposition, not in the chain | PROVED |
| **D3** | **Dictionary at level λ** (b = λ²): for f ∈ C_c^∞(ℝ*₊), Tr ϑ(f)Π_{S(λ,λ)} = W_∞(f) + **2 log(1/λ)·f(1)** + ∫f(ρ⁻¹)ε_λ(ρ)d*ρ, with ε_λ the Halmos series (84) of the pair (1_{u≤λ}, F) (the one `cvl.py` computes). Semilocal (via the Δ of R186.014, valid ∀λ): Son_S^{(λ)}(h) = E_S(h) + 2log(1/λ)‖h‖² + ∫c_hε_S^{(λ)}, E_S = W_∞ − comb₂ = the window's form | PROVED (§1); the identity Ω_b = δ_b − δ_1 also verified to machine precision |
| D4 | Scaling law (Λ) of R183_029 recovered: ε′_b = ε_λ − ε_1, coefficient log(1/b) = 2log(1/λ). The term L_λ is exactly L_λ(h) = 2log(1/λ)‖h‖² (no density part: ω_λ ≡ 0) | PROVED |
| **C1** | **Resolved: APPARENT INCONSISTENCY = omitted term 2log(1/λ)‖h‖² (= 1.3863 at λ = ½).** With D3: min Son_S^{(½)} in 𝒫_{½log3} = +1.236 (before −0.150); Son_S^{(½)}(h*) = 9.9e-4 + 1.3863 − 0.1424 = **+1.245**; all tests ≥ 0 (table §2) | NUMERICAL (M = 16, 20, 24, stable to 2e-3) |
| C1′ | Independent test of W (monotonicity): S(½,½) ≅ S(1,¼) ⊃ S(1,1) ⇒ Son^{(½)} − Son^{(1)} ⪰ 0 ⇔ 2log2·I + C_{ε^{(½)}_∞} − C_{ε^{(1)}_∞} ⪰ 0: min = +1.198 (½log3), +1.372 (0.45), +1.387 (½log2). Without the 2log2 term it would be −0.19 < 0: the term is necessary and sufficient for consistency | NUMERICAL |
| C1″ | CC level λ = 1 (no extra term), archimedean: min(W_∞ + C_{ε_∞^{(1)}}) = +0.014 (½log3), +0.047 (0.45), +0.183 (½log2) ≥ 0: CC (83) reproduced in window conventions | NUMERICAL |
| L1 | Semilocal at λ = 1: A_S has two eigenvalues ±0.994…0.999 not converged at (n,K) = (4000,9)…(8000,11) (with and without FIX closure); τ_n ~ 10–30, ε_S^{(1)} unreliable. Not used | OPEN (numerical) |
| N1 | CHECK_TABLE N1 is now resolved: absolute (84)_S holds at every λ with W_∞ ↦ W_∞ + 2log(1/λ)δ_1 (δ_1 = evaluation at ρ = 1). R186.098 ("λ = ½") was not wrong at the level but in omitting the term | PROVED (D3) |
| Abs | Sign-contact question at ½log3: Son_S(h*) = 1.245 versus remainder R(h*) = 2log2‖h*‖² + ∫c_{h*}ε_S = 1.244; E_S(h*) = 9.9e-4 is their difference. It is the identity, not an absorption: there is no sign contact | NUMERICAL; no sign claim |

**Verdict: CONSISTENT.** The chain E_S = Son_S − ∫c_hε_S is false for λ ≠ 1; the correct one is E_S = Son_S^{(λ)} − 2log(1/λ)‖h‖² − ∫c_hε_S^{(λ)}. The C1 failure of R186.016 was exclusively this term (not a 2π, not ρ^{1/2}, not the comb, not f(ρ) vs f(ρ⁻¹)). Once corrected, Son_S ≥ 0 in every case, with monotonicity in λ verified independently of W.

## 1. Proof of D3

CC notation in L²(ℝ)^ev, ⟨·,·⟩ = ∫_0^∞; P_c := 1_{|x|≥c}, P̂_b := F1_{|p|≥b}F; ϑ(μ)ξ(v) = μ^{−1/2}ξ(v/μ). Π_{S(λ,λ)} = projection onto ran P_λ ∩ ran P̂_λ.

(a) Conjugation. ϑ(μ)P_cϑ(μ)^* = P_{μc}, ϑ(μ)P̂_bϑ(μ)^* = P̂_{b/μ}. With μ = 1/λ: (P_λ,P̂_λ) ↦ (P_1,P̂_b), b = λ²; ϑ(f) commutes with ϑ(μ), so all traces are computed for the pair (P_1,P̂_b). (This is D0: S(λ,λ) = ϑ(λ)S(1,λ²), not a dilation of S(1,1).)

(b) Halmos at level λ (R186.014 §5 with F = F_eR, which holds for any pair): Tr ϑ(f)Π = Tr ϑ(f)P_1P̂_bP_1 − ∫f(ρ⁻¹)δ_b(ρ)d*ρ + ∫f(ρ⁻¹)ε_λ(ρ)d*ρ, with δ_b(ρ) := Tr ϑ(ρ⁻¹)(1−P̂_b)(1−P_1) (CC (63) at level b). By CC Prop 2.2(i) with Δ = [0,1]×[0,b] and ∫_{[0,1]²}φ(xy) = ∫_0^1φ(t)(−log t)dt, ∫_0^1cos(2πat)(−log t)dt = Si(2πa)/(2πa):
 δ_b(ρ) = (ρ^{1/2}/π)[Si(2πb(ρ+1))/(ρ+1) + Si(2πb(ρ−1))/(ρ−1)], ρ ≥ 1, symmetric.
(b = 1 is CC (49).)

(c) Step from b to 1 (b < 1; b > 1 symmetric with signs flipped). P̂_b = P̂_1 + J_b, J_b := F1_{b≤|p|<1}F. By CC (43): Tr ϑ(f)P_1P̂_1P_1 = W_∞(f) + ∫fδ_1. What remains is Tr ϑ(f)P_1J_bP_1. In the variable t = log x (unitary ξ ↦ e^{t/2}ξ(e^t)), ϑ(f) is convolution with f(e^a) and J_b has kernel e^{(s+t)/2}·4∫_b^1cos(2πpe^s)cos(2πpe^t)dp. Integrating over p and over c = e^t ≥ c_0 = max(1,e^{−a}):
 Tr ϑ(f)P_1J_bP_1 = ∫ da f(e^a) ∫_{c_0}^∞ [H_a(c) − bH_a(bc)] dc, H_a(c) = e^{a/2}Σ_± sin(2πcq_±)/(πq_±c), q_± = e^a ∓ 1.
The double integral is not absolutely convergent near a = 0; integrating first over a, ∫da f(e^a)H_a(c) = f(1)/c + O(c^{−2}), and the Frullani argument gives ∫_{c_0}^∞(H(c) − bH(bc))dc = log(1/b)·f(1) + [pointwise part]. Result:
 Tr ϑ(f)P_1J_bP_1 = log(1/b)f(1) + ∫f(e^a)Ω_b(a)da, Ω_b(a) = (e^{a/2}/π)Σ_±[Si(2πb\|q_±\|c_0) − Si(2π\|q_±\|c_0)]/\|q_±\|.
For a ≥ 0 (c_0 = 1) **Ω_b(a) = δ_b(e^a) − δ_1(e^a) term by term** (compare with (b)); symmetry a ↦ −a checked. (Also verified numerically: ω := Ω_b + δ_1 − δ_b = 0 ± 2e-16 for a ∈ [0,1.09].)

(d) Summing (b)+(c): the δ's cancel, leaving Tr ϑ(f)Π_{S(λ,λ)} = W_∞(f) + log(1/b)f(1) + ∫fε_λ = W_∞(f) + 2log(1/λ)f(1) + ∫fε_λ. Semilocal: Δ (R186.014, ∀λ) subtracts comb₂ and replaces ε_∞^{(λ)} with ε_S^{(λ)}. ∎

Delicate point for the audit: the a/c interchange in (c) (Frullani). The constant log(1/b) agrees with the scaling law (Λ) of R183_029 derived by another route and with the numerical requirement of C1′.

## 2. Numbers (NUMERICAL; L²(h) metric, primitive constraint cp, basis from r183_030; ε truncated to |a| ≤ 1.098)

| T | M | min E_S | arq λ=1: min(W+C₁) | arq λ=½ antes / con D3 | monotonía min(2log2 + C_½ − C₁) | S λ=½ antes / con D3 | ∫c_{h*}ε_S^{(½)} | Son_S(h*) |
|---|---|---|---|---|---|---|---|---|
| ½log2 | 24 | 0.549 | +0.183 | +0.494 / +1.880 | +1.387 | +0.486 / +1.873 | −0.062 | +1.873 |
| 0.45 | 24 | 0.068 | +0.047 | +0.186 / +1.572 | +1.372 | −0.034 / +1.352 | −0.101 | +1.353 |
| ½log3 | 16 | 1.05e-3 | +0.0142 | −0.0715 / +1.315 | +1.201 | −0.1500 / +1.2362 | −0.1422 | +1.2451 |
| ½log3 | 20 | 1.02e-3 | +0.0141 | −0.0731 / +1.313 | +1.199 | −0.1502 / +1.2361 | −0.1423 | +1.2451 |
| ½log3 | 24 | 9.9e-4 | +0.0140 | −0.0742 / +1.312 | +1.198 | −0.1504 / +1.2359 | −0.1424 | +1.2449 |

Remark: at h*, ∫c_{h*}ε_∞^{(½)} = −0.1280 and ∫c_{h*}ε_∞^{(1)} = −0.1281: the density part of (Λ) is nearly zero at h*; the entire level difference is 2log2‖h‖².

## Audit notes

1. D3 (c): check the order interchange (Frullani) and the sign for b > 1. The identity Ω_b = δ_b − δ_1 is algebraic once the Ω_b formula is accepted.
2. D2: if R183_026 Prop 2.1 uses σ_Son = m/2π + ε̂ as the symbol relative to (1/2π)∫|ĥ|², it is off by 2π; re-audit only its consequence "ε̂ > 0 at |s| < 6.29" (not used in this note).
3. Tests C1–C1″ are positivity tests; the only quantitative test of the constant is C1′ (needs ≥ 0.19) plus agreement with (Λ). An exact test would require Son via a route independent of (83) (e.g. Galerkin of the truncated Sonin space), not done.
4. λ = 1 semilocal not computed (L1): |λ₁(A_S)| → ~1 makes ε_S^{(1)} ill-conditioned; λ = ½ is the numerically reliable level and D3 legitimizes it.
5. No sign claim about E_S; "absorption" at h* is the identity.

## For Paper 47

Proposition (level dictionary): Tr ϑ(f)Π_{S(λ,λ)} = W_∞(f) + 2log(1/λ)f(1) + ∫f(ρ⁻¹)ε_λ(ρ)d*ρ, and semilocally with −comb₂ and ε_S^{(λ)}. Resolves N1: absolute (84)_S holds at every λ with this term. Withdraw the chain "E_S = Son_S − ∫c_hε_S" for λ ≠ 1 and the C1 conclusion of R186.016.

## Note (R186_099)

* D3 PROVED from the record for 0<λ≤1 (S(λ,λ)≅S(1,λ²) + (Λ) with b=λ²); the Frullani step is not rigorous, it remains as a verification. λ>1 OPEN. D0, D1 PROVED. R183_026 Prop 2.1 should read ε̂ ≥ −m.
