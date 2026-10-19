# R186_053 — The two-sector symbol: it does not exist as a pointwise object; what does exist is the two-sector Schur reduction with automatic coercivity

Phase 186, round 26. Paper 47, grid and crossword are not touched. Script: `r053_sector.py` (`python3 r053_sector.py [ABCD]`, ≈ 10 min; imports `r052_nyquist.py`). Read in full and re-derived:
R186_052 (Thm 1.2, 2.1–2.4, 2.6, §5.2, §8), `r052_nyquist.py`, R186_117 §0–3; walls: R186_044 (Thm 2, (L-W)), R186_045 (table §4,
W-loc), R186_115 §4, R186_051 (Prop. 2.2, 4.5), grid log 25–40.

## 0. Verdict

1. **The "2×2 matrix symbol on the circle" does not exist (PROVED, §1).** In the basis where H is diagonal (the dual variable
 θ ∈ 𝕋 is θ = πt/T: **it is x-space**, L²(I_T) itself), D_e and HᵀD_oH are *convolutions* (explicit kernels: Lemma 1.2), not
 multiplications; D_e and HᵀD_oH do not commute, so there is no common diagonalizing basis. The only pointwise writing is in the index k:
 diag(s_{2j}, s_{2l+1}) with the **non-local** constraint c′ = Hc; "symbol ≥ 0 almost everywhere" is exactly the circulant cone
 {s_k ≥ 0} of R186_052 §3.3, which fails in every window (also by parity, §1.4, NUMERICAL) and is not necessary. On the
 W-loc question: a pointwise criterion in θ does not exist as an object; the pointwise criterion in k is a pointwise functional of σ and falls under
 R186_051 Prop. 2.2/4.5 and W-loc. **It does not escape.** The structure is not "Toeplitz + Hankel": both sectors are difference-kernel
 forms (Toeplitz on the interval) with the reflection u ↦ 2T − u; the only "Hankel" thing is the annihilator (−1)^{j+j′} (R186_052 §2.6).
2. **What does have its own theory (new, PROVED, §2): the two-sector Schur reduction.** Since each sector is diagonal in its own
 basis, the negative part of each has finite rank *in its basis* and the complement N_η^⊥ of the modes with sample < η is
 **automatically coercive with an explicit constant** c_η = ½(s₊^e + s₊^o) (Theorem 2.1; no (L-W) ever needs to be proved; compare
 R186_044 (iv), where coercivity of the prolate complement was OPEN). Consequence (Cor. 2.2): a **sufficient certificate
 computable from the two sequences**, S_η^low := 𝔞_{NN} − X*X/c_η ⪰ 0 on N_η (a d_η × d_η matrix of absolutely convergent sums
 of the samples: no inversion, no operator eigenvalue), with S_η^low ≤ S_η^exact and S_η^exact ≻ 0 ⟺ D_T.
3. **NUMERICAL (§3).** S_η^low certifies the Nyquist Galerkin model at ½log3 (η = 0.3, d = 7: +6.7·10⁻⁴ against λ = 9.8·10⁻⁴),
 log 2 (η = 1, d = 29: +8.9·10⁻⁸ against 9.8·10⁻⁸) and ½log5 (η = 1.5, d = 59: +2.96·10⁻¹² against 3.1·10⁻¹²); it is **stable as the
 complement grows**, Jb = 50 → 800 (monotone decreasing, PROVED that S^low(∞) ≤ S^low(Jb); differences 4·10⁻¹⁰ → 2·10⁻¹⁰ at log 2) and
 negative for M₁ (−1.67·10⁻⁶, as it should be). **But the needed threshold η grows with T** (0.3 / 0.6 / 1.5): the loss S^exact − S^low is the
 energy of 𝔞h* outside N_η, fixed in η, against λ_A doubly exponential: the dimension d_η(T) of the certificate grows at least like
 λ_A^{−1/p}. This is the form of W-det in this basis. Certified windows: only those already certified in Paper 47.
4. **Side finding to audit (NUMERICAL, §3.4):** the Fourier–Nyquist Galerkin with Tate gives upper bounds **below** the
 corpus reference values: λ_A(log 2) ≤ 9.83·10⁻⁸ (Jb = 800; reference r043/r117: 1.042·10⁻⁷) and λ_A(½log5) ≤ 3.09·10⁻¹²
 (reference 3.84·10⁻¹²; at the double-precision floor). Both are Galerkin upper bounds; either the Legendre basis was not
 converged to 6–20%, or the Nyquist matrix has a bias not captured by the analytic tail (§3.3). Requested: audit against r117.
5. **Contact with the sign: none.** No new window; no lower bound of λ_A for T > ½log5. Row D: OPEN.

## 1. The object: H, the dual variable, and why there is no pointwise symbol

R186_052 conventions: ω_k = kπ/2T, s_k = s_T(ω_k) (truncated Lévy), e_j = e^{ijπt/T}/√(2T) (periodic), e′_l = e^{i(l+½)πt/T}/√(2T)
(antiperiodic), c_j = ⟨e_j, F⟩, c′_l = ⟨e′_l, F⟩, H_{lj} = ⟨e′_l, e_j⟩ = h_{l−j}, h_m = sinc(m + ½) = 2(−1)^m/(π(2m+1)).
𝔞_T = ½[s(D_per) + s(D_anti)] = ½(D_e + HᵀD_oH) in the basis {e_j} (R186_052 Thm 2.2–2.3).

**Lemma 1.1 (structure of H; PROVED, elementary).** (i) H is unitary (Parseval in the two bases). (ii) Σ_m h_m e^{−imθ} = e^{iθ/2} for
θ ∈ (−π, π) (jump at θ = ±π): H is the Toeplitz operator with symbol e^{iθ/2}, the "square root of the shift"; H² = S
(shift by one: (H²)_n = δ_{n,−1}). (iii) In the identification ℓ²(ℤ) ∋ c ↔ Σ c_j e^{ijθ}, **θ = πt/T**: the "eigenbasis
of H" is x-space, and H is multiplication by e^{iπt/2T} (which carries e_j to e′_j). (iv) HᵀD_anti conjugation: e^{−iπt/2T}D_anti e^{iπt/2T}
= D_per + π/2T; hence s(D_anti) = M s(D_per + π/2T) M*, M = e^{iπt/2T}: the two sectors are s of the same operator shifted by half a
step, conjugated by the fixed unitary M. *Verified:* (H²)_n = 1.000000 at n = −1, |·| ≤ 10⁻⁶ at n = −2, 0, 1 (L = 2·10⁵); multiplier
to 2·10⁻⁵ (§5 A). ∎

**Lemma 1.2 (kernel of the sectors; PROVED).** Let c_{jj′}(u) := ⟨e_j, (τ_u)_{I_T} e_{j′}⟩ be the symmetrized autocorrelation form
(the one from R186_052's `fourier_matrix`). For a single-atom symbol s(τ) = cos(τu₀), 0 < u₀ < 2T:
 ⟨e_j, cos(u₀D_per) e_{j′}⟩ = c_{jj′}(u₀) + c_{jj′}(2T − u₀) = cos(ω_{2j}u₀) δ_{jj′}, ⟨e_j, cos(u₀D_anti) e_{j′}⟩ = c_{jj′}(u₀) − c_{jj′}(2T − u₀).
By linearity in μ_T: with k_𝔞(u) = κδ₀ − μ⁺(u) the difference kernel of 𝔞_T (μ⁺ = K du + Σv_nδ_{log n} ≥ 0 on (0, 2T)):
 kernel of s(D_per) = k_𝔞(u) − μ⁺(2T − u), kernel of s(D_anti) = k_𝔞(u) + μ⁺(2T − u) (u = |t − t′| ∈ (0, 2T)).
*Proof.* e^{iuD_θ} is the translation with phase jump e^{iθ} at the boundary (R186_052 Thm 2.2); the wrapped term is the translation
by u − 2T, i.e. the kernel at |t − t′| = 2T − u with sign e^{iθ} = ±1. ∎ *Verified* entrywise against Σ_l cos(ω_{2l+1}u₀)h_{l−j}h_{l−j′}
(L = 10⁵): 2·10⁻¹², 2·10⁻¹⁵, 9·10⁻¹² at u₀ = 0.4, log 2, 1.1 (§5 A). It is Thm 2.4 (Δ_F) of R186_052 written as a kernel.
*Reading.* In the dual variable θ = πt/T, D_e is convolution (on ℝ/2Tℤ) by the symmetrized measure ½[k_𝔞(u) + k_𝔞(2T − u)] and HᵀD_oH
is M* ∘ convolution by ½ e^{−iπu/2T}[k_𝔞(u) − k_𝔞(2T − u)] ∘ M, whose phase cancels against M*M except for the **sign in the wrap-around region**
|t − t′| > T. Both are **convolution** operators, not multiplication operators. Sum = k_𝔞 without wrapping: a tautology.

**Prop. 1.3 (no pointwise symbol exists; PROVED).** There is no orthonormal basis of L²(I_T) in which 𝔞_T, s(D_per) and s(D_anti) are
simultaneously multiplications, nor one in which the form is "s_e(θ)·(something) + s_o(θ)·(something)" with s_e, s_o functions of θ.
*Proof.* [s(D_per), s(D_anti)] ≠ 0 (e.g. e_0: s(D_per)e_0 = s_0e_0, s(D_anti)e_0 = Σ_l s_{2l+1}h_l e′_l is not a multiple of e_0 because
(s_{2l+1})_l is not constant); two operators that do not commute are not multiplications in the same basis. And "s_e(θ)·(something)" with "something"
a fixed form would be a multiplication by s_e. ∎ The honest 2×2 writing is on the doubled circle: s(D_{𝕋_{4T}}) ≅ ½[[D_e + HᵀD_oH,
D_e − HᵀD_oH],[D_e − HᵀD_oH, D_e + HᵀD_oH]] on L²(I_T) ⊕ L²(I_T + 2T), unitarily ≅ D_e ⊕ HᵀD_oH: positivity of the whole block is
{s_k ≥ 0 ∀k} (circle), that of D_T is positivity of the (1,1) block (half-circle). It is R186_052 Thm 2.1 in block form.

**1.4 The only pointwise object and its failure (NUMERICAL; r053 B).** diag(s_{2j}, s_{2l+1}) ≥ 0 ⟺ s_k ≥ 0 ∀k. Minima by parity (k ≤ 4000):
| T | ζ: min even (k) | min odd (k) | negative even / odd | M₁(0.01) even / odd | M₁(0.1) |
|---|---|---|---|---|---|
| ½log3 | −3.988 (0) | −0.627 (3) | {0} / {1,3} | −3.887 / −0.787; {0} / {1,3} | same |
| log 2 | −5.595 (0) | −0.676 (5) | {0,8,20} / {1,3,5} | −5.211 / −1.750; same | same |
| ½log5 | −6.511 (0) | −1.516 (9) | {0,14} / {1,3,5,9,23} | −6.900 / −2.230; {0,4,6,14} / {3,9,23} | same |
(s_0 is the primitive symbol at τ = 0: the pole is absorbed by Tate; with Tate's β, R186_052 §3.3: still < 0.) ζ and M₁ have the same pattern
at log 2 and ½log3. **NO-GO** for the pointwise criterion, both by failure and by lack of necessity (D_T is true in these windows with s_k < 0).
**W-loc.** A "pointwise in θ" criterion is a statement about the kernel k(t, t′) at a point: no pointwise statement about a difference
kernel decides positivity of the form on an interval (the atoms −v_nδ_{log n} make k_𝔞 pointwise indefinite in every window).
The pointwise criterion in k is a pointwise functional of σ: R186_051 Prop. 2.2 (margin ≤ (2δT)²/3) and Prop. 4.5 (no bounded functional of σ
implies D). **Verdict: full θ-aliasing creates no new object; it does not escape W-loc.**

## 2. The theory that does exist: two-sector Schur reduction (PROVED)

Notation. For η ∈ ℝ: N_e(η) := {j : s_{2j} < η}, N_o(η) := {l : s_{2l+1} < η} (finite: s_k = log k + O(1), R186_117 §3);
N_η := span{e_j : j ∈ N_e} + span{e′_l : l ∈ N_o} ⊂ L²(I_T) (dim d_η ≤ |N_e| + |N_o|); N′_η := P_𝒫 N_η ⊂ 𝒫_T; 𝒞_η := 𝒫_T ∩ N_η^⊥;
s₊^e(η) := min{s_{2j} : s_{2j} ≥ η}, s₊^o(η) := min{s_{2l+1} : s_{2l+1} ≥ η}, **c_η := ½(s₊^e + s₊^o) ≥ η**.

**Theorem 2.1 (automatic coercivity of the complement).** For every F ∈ N_η^⊥ (in particular F ∈ 𝒞_η): 𝔞_T(F) ≥ c_η‖F‖².
*Proof.* F ⊥ e_j (j ∈ N_e) ⟹ ⟨F, s(D_per)F⟩ = Σ_{j∉N_e} s_{2j}|c_j|² ≥ s₊^e Σ_j|c_j|² = s₊^e‖F‖² (Parseval in {e_j}); F ⊥ e′_l (l ∈ N_o) ⟹
⟨F, s(D_anti)F⟩ ≥ s₊^o‖F‖² (Parseval in {e′_l}); average. ∎ (Also holds in any Galerkin model P_J with N_η replaced by P_J N_η:
F ∈ ran P_J ⊥ P_Je′_l ⟹ F ⊥ e′_l.) *Verified:* λ_min(𝔞|𝒞_η) ≥ c_η in the 50 cases of §3 (e.g. 1.72 ≥ 0.67 at log 2, η = 0.6).

**Theorem 2.2 (two-sector Schur; exact).** 𝔞_T ≥ 0 on 𝒫_T ⟺ S_η := 𝔞_{N′N′} − X*(𝔞|𝒞_η)⁻¹X ⪰ 0 on N′_η, with X := P_{𝒞_η}𝔞|_{N′_η};
and then λ_A ≤ λ_min(S_η). *Proof.* Haynsworth with 𝔞|𝒞_η ≥ c_η > 0 (Thm 2.1); 𝔞x ∈ L² for x ∈ N_η (‖𝔞e′_l‖² = ¼Σ_j(s_{2j} + s_{2l+1})²h²_{l−j}
≍ Σ log²j/j² < ∞). ∎ It is the structure of R186_044 Thm 2 with the prolate block replaced by N_η **and the (L-W) condition proved
for free** (Thm 2.1); inherits, as there: the exact S_η requires (𝔞|𝒞_η)⁻¹.

**Corollary 2.3 (certificate from the sequences).** S_η^low := 𝔞_{N′N′} − X*X/c_η ⪯ S_η. Hence **S_η^low ⪰ 0 ⟹ D_T**. All entries of
S_η^low are explicit, absolutely convergent sums of the samples: 𝔞_{N′N′} ∋ ½(s_{2j}δ + Σ_l s_{2l+1}h_{l−j}h_{l−j′}),
½(s_{2l+1} + s_{2j})h_{l−j}, ½(Σ_j s_{2j}h_{l−j}h_{l′−j} + s_{2l+1}δ); X*X = ⟨𝔞x, 𝔞y⟩ − ⟨𝔞x, P_{N′}𝔞y⟩ − (Tate projection), with ⟨𝔞e′_l, 𝔞e′_{l′}⟩ =
¼[(HD_e²Hᵀ)_{ll′} + (s_{2l+1} + s_{2l′+1})(HD_eHᵀ)_{ll′} + s_{2l+1}s_{2l′+1}δ_{ll′}] and similarly (H Hᵀ = I). **No operator eigenvalue, no
inversion**: the decision is the λ_min of an explicit d_η × d_η matrix. *Proof.* (𝔞|𝒞)⁻¹ ≤ c_η⁻¹ ⟹ X*(𝔞|𝒞)⁻¹X ≤ X*X/c_η. ∎
**Lemma 2.4 (monotonicity in the model).** In the Galerkin model P_J (Nyquist, |j| ≤ J) with the same N_η: S_η^low(J) ≥ S_η^low(∞) and S_η^low(J) is
decreasing in J. *Proof.* X*X(J) = ‖P_{𝒞∩ranP_J}𝔞x‖² ≤ ‖P_𝒞𝔞x‖². ∎ Hence **S_η^low(J) < 0 for some J refutes the certificate; S_η^low(J) > 0
does not prove it until the tail is controlled** (what is observed is geometric convergence, §3.2).
**Lemma 2.5 (where it is lost).** If h* = x + r with x = P_{N′}h*, r ∈ 𝒞_η, then Xx = λ_A r − P_𝒞𝔞r and the loss in the critical direction is
S_η(x) − S_η^low(x) ≤ ‖λ_Ar − P_𝒞𝔞r‖²/c_η ≈ ‖𝔞r‖²/c_η. *Proof.* P_𝒫𝔞h* = λ_Ah*. ∎ The loss is the **energy of 𝔞h* outside N_η**, a quantity
of h* (not of σ): fixed in η, does not decrease with T, while λ_A does. This is the reason for §3.3.

## 3. Numerics (r053 C, D; NUMERICAL)

**3.1 Exact Fourier Galerkin (quadrature, J = 24, exact Tate; `fourier_matrix` from r052).** λ_J = +9.79·10⁻⁴ / +1.306·10⁻⁷ / +4.45·10⁻¹²
(½log3 / log 2 / ½log5; match R186_052 §8 C).
| T | η | d_η (even, odd) | c_η | λ_min(𝔞\|𝒞_η) | λ_min(S_η) | λ_min(S_η^low) |
|---|---|---|---|---|---|---|
| ½log3 | 0 | 5 (1, 4) | 0.565 | 0.811 | +9.82·10⁻⁴ | −6.2·10⁻³ |
| ½log3 | 0.3 | 7 (3, 4) | 0.743 | 1.227 | +9.79·10⁻⁴ | **+6.7·10⁻⁴** |
| ½log3 | 1.0 | 19 (9, 10) | 1.113 | 1.948 | +9.79·10⁻⁴ | +9.64·10⁻⁴ |
| log 2 | 0.3 | 13 (7, 6) | 0.423 | 0.916 | +1.306·10⁻⁷ | −0.124 |
| log 2 | 0.6 | 21 (13, 8) | 0.674 | 1.725 | +1.306·10⁻⁷ | **+8.7·10⁻⁸** |
| log 2 | 1.0 | 29 (17, 12) | 1.088 | 1.862 | +1.306·10⁻⁷ | +1.247·10⁻⁷ |
| ½log5 | 0.6 | 25 (13, 12) | 0.742 | 1.711 | +4.45·10⁻¹² | −4.6·10⁻⁴ |
| ½log5 | 1.0 | 31 (15, 16) | 1.199 | 1.840 | +4.45·10⁻¹² | −5.1·10⁻¹² |
| ½log5 | 1.5 | 45 (19, 26) | 1.594 | 2.247 | +4.45·10⁻¹² | **+4.45·10⁻¹²** |
| log 2, M₁ δ=0.01 | 1.0 | 27 | 1.154 | 1.834 | −1.645·10⁻⁶ | −1.651·10⁻⁶ |
| log 2, M₁ δ=0.1 | 1.0 | 27 | 1.158 | 1.834 | −1.392·10⁻³ | −1.424·10⁻³ |
λ_min(S_η) = λ_J to 4 digits in every case (exact Thm 2.2); S^low goes from failing badly (small η: loss ‖X‖²/c_η ~ 1)
to reproducing λ_J to 95–99% (η ≥ 1 at log 2, η ≥ 1.5 at ½log5). It fails for M₁, as it should (S^low ≤ S = λ < 0).

**3.2 Growth of the complement (Nyquist matrix ½(D_e + HᵀD_oH), |j| ≤ Jb, L = 2·10⁵ odd modes).**
| T | Jb | λ_Jb | S^low(η=0.6) | S^low(η=1) | S^low(η=1.5) | S^low(η=2.5) |
|---|---|---|---|---|---|---|
| ½log3 | 50 / 100 / 200 / 400 / 800 | 9.520 / 9.466 / 9.453 / 9.449 / 9.448 ·10⁻⁴ | 7.20 / 7.10 / 7.07 / 7.06 / 7.06 ·10⁻⁴ | 9.34 / 9.28 / 9.26 / 9.26 / 9.25 ·10⁻⁴ | 9.49 / 9.43 / 9.42 / 9.41 / 9.41 ·10⁻⁴ | 9.518 / 9.463 / 9.449 / 9.444 / 9.442 ·10⁻⁴ |
| log 2 | 50 / 100 / 200 / 400 / 800 | 10.47 / 9.964 / 9.861 / 9.837 / 9.831 ·10⁻⁸ | 4.59 / 3.30 / 2.74 / 2.46 / 2.32 ·10⁻⁸ | 9.68 / 9.12 / 8.98 / 8.93 / 8.92 ·10⁻⁸ | 10.32 / 9.78 / 9.66 / 9.62 / 9.61 ·10⁻⁸ | 10.47 / 9.955 / 9.847 / 9.820 / 9.811 ·10⁻⁸ |
Monotone decreasing in Jb (Lemma 2.4), with successive differences 5.6, 1.4, 0.45, 0.19 ·10⁻⁹ (log 2, η = 1): geometric convergence of ratio
≈ 0.35–0.4; extrapolated limit ≈ 8.91·10⁻⁸ > 0 (≈ 0.91 λ). At ½log3 (η = 1): limit ≈ 9.25·10⁻⁴ = 0.98 λ. **The certificate is not destroyed
as the complement grows**: the loss is in the critical direction (Lemma 2.5) and is small because h* is almost entirely in N_η.
With the analytic tail of the odd modes (½τ_L(−1)^{j+j′}, τ_L = 1.3·10⁻⁵, §5 D′): λ_Jb changes by +10⁻¹¹ (⟨h*, (−1)^j⟩² ≈ 0; annihilator R186_052 §2.6).
½log5 with tail (Jb = 100 / 400): λ_Jb = 3.28 / 3.09 ·10⁻¹²; S^low(η=1) = −5.8 / −7.4 ·10⁻⁹ (fails), S^low(1.5) = 3.14 / 2.96 ·10⁻¹²,
S^low(2.5) = 3.28 / 3.09 ·10⁻¹² (d = 147 / 169). M₁(0.01, Jb = 100): λ = −1.662·10⁻⁶, S^low(1) = −1.669·10⁻⁶.

**3.3 The threshold grows with T (the form of W-det here).** Smallest observed η with S^low > 0: 0.3 (½log3, d = 7), 0.6 (log 2, d = 21),
1.5 (½log5, d = 57–59). Relative loss (S − S^low)/λ at η = 1: 0.02 / 0.09 / 1.9·10³. By Lemma 2.5 the loss at fixed η is ‖𝔞r_η‖²/c_η
with r_η the part of h* outside N_η — an O(1)-scaled quantity of h*, independent of λ_A — and λ_A ≈ exp(−13e^{2T}) (phase-187).
Hence d_η(T) must grow until the energy of h* outside the first ~d_η Nyquist modes is < λ_Ac_η: with decay K^{−p}
of that energy, d ≳ λ_A^{−1/p}: **doubly exponential in T**. The certificate is finite per window but not uniform: it is not a route
to "∀T". And the condition "S^low ⪰ 0" is the λ_min of a matrix: it is not a first-order criterion in σ (consistent with W-lin, R186_045 Lemma T′).

**3.4 Discrepancy with the reference values (to be audited).** Nyquist–Fourier Galerkin with Tate (Jb = 800): λ_A(½log3) ≤ 9.448·10⁻⁴
(ref. 9.486·10⁻⁴), λ_A(log 2) ≤ 9.831·10⁻⁸ (ref. 1.042·10⁻⁷, r043/r117 Legendre), λ_A(½log5) ≤ 3.09·10⁻¹² (ref. 3.84·10⁻¹²; double-
precision floor ≈ 10⁻¹⁴ at 800×800). The quadrature Galerkin (3.1, J = 24) and the Nyquist one (J = 24, 50) agree with each other to 4 digits and
decrease monotonically in J; the odd tail does not explain it (+10⁻¹¹). If the Nyquist matrix is exact (R186_052 Thm 2.3, verified to
3.5·10⁻⁶ per entry), **the Legendre reference values are upper bounds not converged to 0.4% / 6% / 20%** and the corrected values
are the ones above. No sign changes; the constant of the phase-187 law changes in the third digit. OPEN until audited.

## 4. Honesty, falsifiers, what was NOT obtained

- **What is new as a statement.** Lemma 1.1 (iv) (the sectors are s(D) and M s(D + π/2T) M*), Lemma 1.2 (kernels of the sectors, verified
 to 10⁻¹²), Prop. 1.3 (no pointwise symbol exists), Theorem 2.1 (automatic coercivity with constant c_η = ½(s₊^e + s₊^o)), Thm 2.2, Cor. 2.3
 (certificate S_η^low from the sequences), Lemmas 2.4–2.5. Prior grep in phase-186 and Paper 47: "automatic coercivity|s₊^e|two
 sectors|two-sector|N_η" do not appear; the closest Schur reduction is R186_044 Thm 2 (prolates, (L-W) OPEN) and R186_025 Thm B
 (high-pass coercivity with a Poincaré constant). Here coercivity is free from the two-basis structure.
- **What is refuted.** Question 1 (pointwise 2×2 matrix symbol in θ): NO-GO PROVED (Prop. 1.3) + NUMERICAL (1.4).
 "Toeplitz + Hankel": no; both sectors are Toeplitz on the interval (Lemma 1.2). "Escapes W-loc": no (§1.4).
- **What was not obtained.** No lower bound of λ_A in an uncertified window; no uniformity in T (§3.3); the exact certificate
 S_η needs (𝔞|𝒞_η)⁻¹ (inherited, as in R186_044); S_η^low is computable but its dimension grows like λ_A^{−1/p}. No property of the
 sequences separates ζ from M₁ except through S_η^low (which is the λ_min of a d × d matrix, not a first-order functional).
- **Falsifiers.** (F1) If λ_min(𝔞|𝒞_η) < c_η in some case, Thm 2.1 would be false: 50/50 satisfy it. (F2) If λ_min(S_η) ≠ λ_J to 4 digits,
 Thm 2.2 (Haynsworth) would be implemented wrong: it matches in every case. (F3) If S^low(Jb) increased in Jb, Lemma 2.4 would be false: it decreases in
 40/40 consecutive pairs. (F4) If S^low(η = 1, log 2) became negative for some Jb ≤ 800: it does not (8.92·10⁻⁸ at Jb = 800);
 a larger Jb making it negative would refute the extrapolation of §3.2. (F5) Lemma 1.2: 10⁻¹² at three u₀. (F6) §3.4: if the Legendre
 Galerkin with large N (r117) comes down to ≤ 9.83·10⁻⁸, the discrepancy is convergence; if not, there is a bias in the Nyquist matrix
 (to be sought in the treatment of |l| > L: the non-alternating tail is O(Jb/L)·τ_L ≈ 5·10⁻⁸ per entry at j ~ Jb).
- **Contact with the sign: none.** Row D: OPEN.

## 5. Self-checks (NUMERICAL; `r053_sector.py`)

A. H² = S to 10⁻⁶ (L = 2·10⁵); multiplier e^{iθ/2} to 2·10⁻⁵ (Gibbs tail); Lemma 1.2 entrywise (J = 6, L = 10⁵): 2.2·10⁻¹², 1.7·10⁻¹⁵,
 9.4·10⁻¹² (u₀ = 0.4, log 2, 1.1); even sector exact to 10⁻¹⁵.
B. Minima by parity in three windows, ζ and M₁ (δ = 0.01, 0.1), k ≤ 4000 (table 1.4).
C. Quadrature Galerkin J = 24 (`fourier_matrix` from r052, composite GL, 3000 nodes; |Im M| ≤ 3·10⁻¹⁵), 𝒫_T via real QR of (Re a, Im a)
 (b = ā, M real: the complex minimum over 𝒫 is the real one over {Σc_jRe a_j = Σc_jIm a_j = 0}); N′_η via QR of the projected vectors;
 complement via full QR; Haynsworth with `solve`. A first attempt with complex Qᵀ gave λ_J = −3.4 (conjugation error), corrected.
D. Nyquist matrix (`nyquist_matrix` from r052, L = 2·10⁵, chunks of 5·10⁴), Jb = 50–800; D′: analytic tail τ_L = (2/π²)Σ_{l>L}s_{2l+1}/l²
 (sum up to 2·10⁷ + integral), added as ½τ_L(−1)^{j+j′}: effect +10⁻¹¹ on λ_Jb. Total time ≈ 10 min.

## 6. Labels

| statement | label |
|---|---|
| Lemma 1.1 (H: multiplier e^{iθ/2}, H² = S, θ = πt/T, sectors conjugate via M) | PROVED |
| Lemma 1.2 (kernels of the sectors: reflection u ↦ 2T − u with sign ∓) | PROVED; verified 10⁻¹² |
| Prop. 1.3 (no pointwise matrix symbol exists; the 2×2 writing is the doubled circle) | PROVED |
| 1.4 pointwise criterion in k = circulant cone: fails by parity for ζ and M₁; does not escape W-loc | NO-GO (NUMERICAL + R186_051 Prop. 2.2/4.5) |
| Theorem 2.1 (automatic coercivity, c_η = ½(s₊^e + s₊^o)) | PROVED; verified 50/50 |
| Theorem 2.2 (exact two-sector Schur), Lemma 2.4, Lemma 2.5 | PROVED |
| Cor. 2.3 (S_η^low ⪰ 0 ⟹ D_T; entries = explicit sums of samples) | PROVED |
| §3.1–3.2 S^low certifies the Galerkin model at ½log3, log 2, ½log5 and converges in Jb | NUMERICAL (extrapolated limit; no tail bound) |
| §3.3 increasing η(T), d_η ≳ λ_A^{−1/p} | ARGUED (Lemma 2.5 PROVED + phase-187 law CONJECTURE) |
| §3.4 λ_A(log 2) ≤ 9.83·10⁻⁸ < reference 1.042·10⁻⁷ | NUMERICAL, OPEN (to be audited against r117) |
| Row D | OPEN; contact with the sign: none |
