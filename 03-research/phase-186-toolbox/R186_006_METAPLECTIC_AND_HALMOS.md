# R186.006 — Metaplectic candidate and Halmos construction (S = {∞,2})

Pure mathematics; one NUMERICAL computation marked as such (not converged).
Sources: [CCM] arXiv 2310.18423v2 (`mainc2m24fine.tex`): Prop groundstate (eq. etas/essl, (iii) F_S∘η_S = η_S∘F_∞), def soninsemiloc, Prop groundstatedual; [CM] PNAS 2022; R186.002, R186.003.
Script: `scratchpad/halmos.py`.

## Status

| # | Statement | Label |
|---|---|---|
| 1 | Archimedean mechanism: W_λ = −∂(λ²−x²)∂ + (2πλx)² commutes with P_λ via the coefficient that vanishes at ±λ, and with F (hence with P̂_λ) because **F W_λ F⁻¹ = W_λ** (identity ∂x²∂ = x∂²x) | PROVED |
| 2 | **Formula for F_S in the u-model**: F_S = E F_∞ E⁻¹, E g(u) = Σ_{k≥0} g(2^k u), E⁻¹g(u) = g(u) − g(2u); kernel F_S f(u) = ∫_0^∞ [Σ_{k≥0} cos(2π2^k ux) − cos(πux)] f(x) dx; F_S unitary, self-adjoint, F_S² = 1, F_S h_S = h_S | PROVED |
| 3 | X := F_S u² F_S⁻¹ = E·(−∂²/4π²)(1 − 3Σ_{k≥1}2^{−k}D_{−k})·E⁻¹ (D_m g(u) = g(2^m u)): **non-local**, with outward leakage 2^{|m|}I of coefficient −(12/7)8^{m}·(−1/4π²), m ≤ −1 | PROVED |
| 4 | **NO-GO**: W^{mp} = −𝔰² + κλ²π(u² + X) + const does not commute with P^S_λ for any λ > 0, κ ∈ ℝ (and by F_S-invariance neither with P̂^S_λ). Stronger: L + κX with L any local differential operator and κ ≠ 0 never commutes | PROVED |
| 5 | P^S_λ F_S P^S_λ is compact (norm limit of compacts); P P̂ P = (P F_S P)² compact, with no eigenvalue 1 | PROVED |
| 6 | Halmos operator W_S^{ang} := f(P P̂ P ⊕ (1−P)(1−P̂)(1−P) …) commutes with P and P̂ by construction; exists for every S | PROVED (tautological) |
| 7 | P F_S P is not Hilbert–Schmidt (HS² of the truncation k ≤ K grows as (K+1)λ²/2) | OPEN (sketch in §5) |
| 8 | Spectrum of P P̂ P for S = {∞,2}: decay much slower than the archimedean one (λ=½: ≈0.96, 0.27, 0.09 vs 0.78, 0.011, 2·10⁻⁶) | NUMERICAL (not converged in K) |
| 9 | Does any 2nd-order differential operator in u commute with P^S_λ and P̂^S_λ? | OPEN |

## 1. Archimedean mechanism (PROVED)

W_λ = −λ²∂² + ∂x²∂ + 4π²λ²x² on L²(ℝ). [W_λ, P_λ] = 0: the boundary term of Green's lemma is
(λ² − x²)(fg′ − f′g)|_{±λ} = 0. Fourier: F∂F⁻¹ = 2πix, Fx²F⁻¹ = −∂²/4π². Then
F(−λ²∂²)F⁻¹ = 4π²λ²x², F(4π²λ²x²)F⁻¹ = −λ²∂², F(∂x²∂)F⁻¹ = x∂²x, and x∂²x f = x²f″ + 2xf′ = ∂x²∂ f.
Hence FW_λF⁻¹ = W_λ, and [W_λ, P̂_λ] = F[W_λ, P_λ]F⁻¹ = 0. The two commutations have different
mechanisms: **locality + vanishing boundary coefficient** (P) and **Fourier self-duality** (P̂).

## 2. F_S in the u-model (PROVED)

Model of R186.003: L²(X_S)^{K_S} ≅ L²(ℝ₊, du), h(u) = value at (1, u) of the domain ℤ₂^*×ℝ₊^*.
By [CCM eq. etas]: η_S f (1×u) = Σ_{k≥0} f(2^k u), i.e. **η_S = E** in the u-model (on L²(ℝ)^{ev} ≅ L²(ℝ₊, 2du)… the normalization of E is irrelevant for commutators). E = Σ 2^{−k/2}δ_k with δ_k unitary, ‖E‖ ≤ (1−2^{−1/2})⁻¹; E⁻¹ = 1 − D_1 (telescoping: Σ_k f(2^k u) − Σ_k f(2^{k+1}u) = f(u)); in Mellin, E is the multiplier L_2(½ − is), bounded with bounded inverse.
[CCM Prop groundstate (iii)]: F_S∘η_S = η_S∘F_∞ and η_S is a bounded bijection ⟹ **F_S = E F_∞ E⁻¹**.
Unitarity: in Mellin, F_∞ = (s ↦ −s)∘γ(s); E F E⁻¹ multiplies by L_2(½−is)/L_2(½+is)·γ, of modulus 1. F_S² = E F² E⁻¹ = 1, hence F_S = F_S* (matches R186.002 Lemma 2.1, F_S = (−1)^{N_S}).
Kernel: (F E⁻¹f)(ξ) = ∫ f(x)[2cos(2πξx) − cos(πξx)]dx; applying E and reindexing,
 **F_S f(u) = ∫_0^∞ K_S(u,x) f(x) dx, K_S(u,x) = Σ_{k≥0} cos(2π2^k ux) − cos(πux)** (symmetric; lacunary series, in a distributional sense).
Check: with ∫_0^∞ cos(2πax)e^{−πb²x²}dx = e^{−πa²/b²}/(2b), F_S h_S = Σ_{m≥0} e^{−π4^m u²} + Σ_{m<0}(2^m − 2^m)(…) = h_S. ✓

## 3. X = F_S u² F_S⁻¹ and the NO-GO (PROVED)

(a) E⁻¹u²E g = u²Eg(u) − 4u²Eg(2u) = u²(1 − 3Σ_{k≥1}D_k)g.
(b) F D_k F⁻¹ = 2^{−k}D_{−k}, F u² F⁻¹ = −∂²/4π². Hence X = E·(−∂²/4π²)(1 − 3Σ_{k≥1}2^{−k}D_{−k})·E⁻¹.
(c) Let f ∈ C_c^∞(I), I = [a,b] ⊂ (λ/2, λ), b < 2a; φ := f″. Using Σ_{k≥1}2^{−k}(D_{−k} − D_{1−k}) = −½ + Σ_{k≥1}2^{−k−1}D_{−k} and ∂²D_m = 4^m D_m∂²:
 X f = −(1/4π²) Σ_m c_m D_m φ, c_m = (5/2)[m≥0] − 4[m≥1] − (3/2)Σ_{k≥max(1,−m)} 8^{−k}.
 For m ≤ −1: **c_m = −(12/7)8^{m} ≠ 0**. The supports 2^{−m}I are pairwise disjoint.
(d) Take g ∈ C_c^∞(2I), 2I ⊂ (λ, 2λ), g = φ(u/2). Pf = f, Pg = 0, and −𝔰², u² are local with disjoint supports:
 ⟨[W^{mp}, P^S_λ] f, g⟩ = ⟨W^{mp} f, g⟩ = κλ²π·(3/(56π²))·∫ f″(u/2)² du = (3κλ²/56π)‖f″(·/2)‖² ≠ 0 if κ ≠ 0.
 If κ = 0, W = −𝔰² and [−𝔰², P] has the boundary term λ²(fg′ − f′g)(λ) ≢ 0 (R186.003 §2). **NO-GO ∎**
The same argument holds for L + κX with L any differential operator: the D_{−1} leakage is invisible to L.
By F_S W^{mp} F_S = W^{mp} (F_S² = 1, F_S𝔰F_S = −𝔰), it also fails to commute with P̂^S_λ.

Structural cause: the semilocal Fourier transform mixes the scales 2^m; the part m < 0 **dilates the support outward**, and no boundary coefficient (at λ or at 2^{−k}λ) can compensate for a disjoint-support contribution. The statement's conjecture ("boundaries at 2^{−k}λ that might cancel") is weaker than what actually happens: no cancellation is possible because the defect is not a boundary defect but a support defect.

## 4. Halmos (PROVED existence)

P := P^S_λ, P̂ := F_S P F_S. (i) P F_S P = Σ_k P δ_k-terms: P E F P = Σ_k 2^{−k/2}δ_k P_{2^kλ} F P_λ, each term Hilbert–Schmidt (kernel bounded on [0,2^kλ]×[0,λ]) and the series norm-convergent; P E⁻¹ P = E⁻¹P (E⁻¹ preserves support in (0,λ]). Hence P F_S P = (P E F P)(E⁻¹ P) is compact, and P P̂ P = (P F_S P)² is compact (F_S self-adjoint).
(ii) No eigenvalue 1: Pf = f and P̂f = f ⟹ E⁻¹f and F E⁻¹f = E⁻¹F_S f supported in (0,λ] ⟹ E⁻¹f = 0 (Paley–Wiener) ⟹ f = 0.
(iii) Two-subspaces theorem (Halmos): outside the trivial summands, (P, P̂) is unitarily ⊕ of 2×2 pairs with angle θ, cos²θ ∈ σ(P P̂ P). Any Borel function of the angle operator commutes with P and P̂. Thus W_S^{ang} exists for every S, with eigenfunctions = eigenfunctions of P P̂ P (in the case S = {∞}, by Slepian, these are the prolate functions). Its kernel ran(1−P)∩ran(1−P̂) is son_λ(X_S) [CCM def soninsemiloc], infinite-dimensional [CCM Thm isosonin].
This is tautological: the real question is whether W_S^{ang} admits a **differential** realization (CCM).

## 5. Spectrum (NUMERICAL, not converged) and non-HS sketch

Gauss–Legendre Nyström (n ≤ 5000) of the kernel K_S truncated to k ≤ K, eigenvalues of (PF_SP)²:
| λ | S | μ₀ | μ₁ | μ₂ | μ₃ |
|---|---|---|---|---|---|
| ½ | ∞ | 0.7834 | 1.14e−2 | 2.2e−6 | 5.9e−11 |
| ½ | {∞,2}, K=9 | 0.9489 | 0.2681 | 0.0858 | 0.0699 |
| ½ | {∞,2}, K=10 | 0.9598 | 0.2654 | 0.0882 | 0.0718 |
| 1 | ∞ | 0.99994 | 0.9594 | 0.2747 | 3.5e−3 |
| 1 | {∞,2}, K=10 | 0.9940 | 0.9833 | 0.3805 | 0.3106 |
Drift in K of order 10⁻²: qualitative only (at K = 6, 1.013 > 1 appears, a truncation artifact). Qualitative conclusion: **the primes change the spectrum drastically**; the Slepian super-exponential decay disappears.
Sketch (OPEN): ‖P K_S^{(K)} P‖²_HS = Σ_k ∫∫cos²(2π2^kux) + cross terms = (K+1)λ²/2 + O(1), since ∫_0^λ∫_0^λ cos(cux) = Si(cλ²)/c = O(1/c). If this is shown to pass to the limit, P P̂ P is compact but **not trace class**: no regular Sturm–Liouville operator with P P̂ P as a function of it could have the archimedean asymptotics.

## Next lemma

L1^{ang}: decide whether P F_S P is Hilbert–Schmidt (§5) and, if not, compute the counting law #{μ_n > ε}. If it grows like log(1/ε)·(number of scales 2^k with 2^kλ² ≳ 1), no 2nd-order differential operator with discrete Sturm–Liouville-type spectrum can have P P̂ P as a monotone function of it ⟹ NO-GO for a "differential semilocal prolate" in the sense of Slepian. Item 9 remains OPEN.

## Audit notes

1. η_S = E in the u-model: check [CCM eq. etas] and that the factor u^{1/2} of w_S has been absorbed when working with du (R186.003 §1). The constants of E/F (factor 2 of L²(ℝ)^{ev}) only rescale; they do not affect "≠ 0".
2. F_S = EFE⁻¹ requires η_S to be a bounded bijection on L²(X_S)^{K_S}: see the multiplier L_2(½−is), bounded below by (1+2^{−1/2})⁻¹.
3. §3(c): recompute c_{−1} = −3/14; the exact constant is irrelevant, it suffices that c_m ≠ 0 for some m < 0, and the disjointness of supports (b < 2a).
4. The NO-GO is for the form u² + F_S u² F_S⁻¹ (the one suggested by CCM l. 270 / §metasect). This does not exclude the full Weil representation of Mp(SL₂(𝔸_S)) with other generators; but any F_S-conjugate generator of a multiplier inherits the outward leakage.
5. Halmos: trivial existence; no claim of differentiability or sign. The numbers in §5 are not converged.

## Note (R186_093)

* Correct du measure (CCM (42)–(46)); F_S = E F_∞ E⁻¹ correct and unitary (multiplier γ·L₂(½−is)/L₂(½+is)); kernel: norm limit of truncations over P, not distributional; the memo's truncation leaves a spurious O(2^{−K/2}) term (the 1.013). FALSE similarity: PF_SP = E_λ(PF_∞P)E_λ⁻¹ + R·E_λ⁻¹ with R = PE(1−P)F_∞P ≠ 0. **Theorem PROVED: PF_SP is not Hilbert–Schmidt** (item 7). Numerics recomputed: μ₀ → 0.974, μ₂ = 0.09147, μ₄ = 0.04592. Item 9 (differential operator commuting with P and P̂) OPEN.
