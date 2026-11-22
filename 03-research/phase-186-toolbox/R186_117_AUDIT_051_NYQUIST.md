# R186_117 — Audit of Theorem 4.1 of R186_051 ("Nyquist identity"): own derivation, aliasing of the archimedean part, numerical reproduction, novelty

Phase 186. Object: R186_051 §4, Theorem 4.1 (a)–(d), Cor. 4.2 insofar as it depends on it,
§6(E), §7.3. Own code: `r117_nyquist_check.py` (not importing anything from r043/r051: own sieve, own Legendre basis, exact F̂
via spherical Bessel F̂(τ) = Σ_j h_j 2T i^j j_j(τT), c_F by exact Gauss–Legendre, L_T(ω) = Cin(2Tω) + ∫(1−cos)K_reg; ≈ 1 min).
Paper 46, grid and crossword are not touched.

## 0. Verdict

**ACCEPT WITH CORRECTIONS (MAJOR-1, MINOR-1..4). No FATAL.** Theorem 4.1 is correct as stated, **because
its s_T is not the symbol σ_T of Paper 46 eq:symbol but the symbol with the Lévy measure truncated to [0, 2T]**:
s_T = σ_T + ∫_{2T}^∞ cos(τu)K(u)du. With s_T the four identities (a)–(d) are exact (Poisson/Shannon on c_F, support
[−2T, 2T]); with σ_T (i.e. with m(ω_k) on the grid) the Nyquist sum is **not** the form: the alias term is
 Alias_T(F) := 𝔞_T(F) − (1/4T)Σ_k|F̂(ω_k)|²σ_T(ω_k) = Σ_{j≥1}∫_{−2T}^{2T} c_F(v)K(4Tj − v)dv
 = Σ_{j≥1}Σ_{m≥0} 2e^{−(2m+½)4Tj}·Φ_F(2m+1)·Φ_F(−2m), Φ_F(s) := ∫F(t)e^{(s−½)t}dt,
whose first term (m = 0, j = 1) is 2e^{−2T}A(F)B(F) and **vanishes exactly on 𝒫_T**; the next one, 2e^{−10T}Φ_F(5/2)Φ_F(−5/2),
does not vanish and equals +3.7·10⁻⁴ (½log3), +1.2·10⁻⁴ (log 2), +4.7·10⁻⁵ (½log5) at h*: **48% of λ_A at ½log3, 1.3·10³ λ_A at log 2,
10⁷ λ_A at ½log5**. With the symbol of Paper 46 on the grid, h*'s "Nyquist sum" at log 2 is −1.32·10⁻⁴ < 0 with λ_A = +1.04·10⁻⁷:
a false witness. It is the term that any "algebra of D_T" built on samples of m must treat separately; with s_T it is
absorbed exactly and there is nothing to treat. The memo does it right (it uses s_T), but the goal and the reading "the form sees the symbol
on the grid" must say **s_T, not σ_T** (MAJOR-1: the memo writes "s_T = symbol with the truncated Lévy measure" only in §0.5 and
in the parenthetical of (d); in Cor. 4.2, §4 "What is missing" and §8 it uses "s_T" and "σ_T" as if the former were the paper's symbol).

## 1. Own derivation (PROVED; fixes the memo's proof at one point)

Paper 46 conventions: F̂(τ) = ∫F e^{iτt}, c_F(u) = ∫F(t)F̄(t−u)dt, ĉ_F = |F̂|², supp c_F ⊂ [−2T, 2T], c_F(±2T) = 0, c_F continuous.
Let ν be a finite **even** measure with supp ν ⊂ [−2T, 2T] and no atoms at ±2T. Then φ := c_F * ν is continuous, supp φ ⊂ [−4T, 4T],
φ(±4T) = 0, and φ̂ = |F̂|²·ν̂ with ν̂ real. Poisson with step Δ = π/2T (period 2π/Δ = 4T on the u side): if Σ_k|φ̂(kΔ)| < ∞,
 Σ_{k∈ℤ} φ̂(kΔ) = (2π/Δ)Σ_{j∈ℤ} φ(4Tj) = 4T·φ(0) = 4T∫c_F dν (the j ≠ 0 terms fall outside the support or on the boundary where φ = 0).
So (1/4T)Σ_k|F̂(ω_k)|² ν̂(ω_k) = ∫c_F dν. [Base identity]
- (b): ν = δ₀. This is Shannon/Parseval for |F̂|² ∈ PW_{2T}: Σ_k|F̂(kπ/2T)|² = 4T‖F‖² (×2 oversampling of F̂ ∈ PW_T). Classical.
- (a): ν = Σ_n v_n½(δ_{log n} + δ_{−log n}); ν̂ = P_T. Classical (band-limited: log n < 2T).
- (c): ν = even part of η_T; ν̂ = Re η̂_T; −∫c_F dη_T = E_ψ and −Re η̂_T/(4T) = 𝒞₀. ✓.
- (d): **here the memo's proof has a gap**: it applies the base identity to μ = ½K(|u|)1_{|u|<2T}du, which **is not finite**
 (K(u) ~ 1/u at 0) and whose μ̂ does not exist; the aside "it has finite mass against c_F(0) − c_F(u) ~ u²" is not a Poisson
 argument (and c_F(0) − c_F(u) ~ u² only if F ∈ H¹; for a Legendre F with a jump at ±T it is ~ u). Repair (two lines): μ_ε := ½K(|u|)1_{ε<|u|<2T},
 finite; base identity + (b): (1/4T)Σ_k|F̂(ω_k)|²∫(1−cos ω_k u)dμ_ε = ∫(c_F(0) − c_F(u))dμ_ε. Both integrands are ≥ 0 and grow
 as ε decreases (1 − cos ≥ 0; c_F(0) − c_F(u) = ½‖F − F(·−u)‖² ≥ 0): monotone convergence on both sides gives
 (1/4T)Σ_k|F̂(ω_k)|²L_T(ω_k) = ∫₀^{2T}(c_F(0) − c_F(u))K(u)du ∈ [0, ∞], L_T(τ) := ∫₀^{2T}(1−cos τu)K(u)du, **with no regularity hypothesis**.
 With eq:m (m = C₀ + ∫₀^∞(1−cos τu)K) and thm:A (eq:Aform) we get (d) with s_T = C₀ + ∫_{2T}^∞K + L_T − P_T = σ_T + ∫_{2T}^∞cos(τu)K(u)du.
 Verified numerically: s_T − σ_T = ∫_{2T}^∞cos K (closed form (−1)^kΣ_m 2e^{−(4m+1)T}(2m+½)/((2m+½)² + ω_k²)) to 5·10⁻¹⁴ for k ≤ 2·10⁵.
- **Alias of m.** The base identity with ν_j := ½K(|u|)1_{|u|>2T} (finite, ν̂ = ∫_{2T}^∞cos(τu)K(u)du) gives the j ≠ 0 Poisson terms
 (supp c_F * ν_j ⊄ [−4T, 4T]): (1/4T)Σ_k|F̂(ω_k)|²∫_{2T}^∞cos(ω_k u)K(u)du = Σ_{j≥1}∫c_F(v)K(4Tj − v)dv, and K(x) = 2Σ_m e^{−(2m+½)x} gives
 the Tate moment expansion of §0. It is exactly "m is not band-limited": the part of the Lévy measure outside
 [−2T, 2T] produces aliasing; the part inside does not. Verified: direct sum vs. closed form identical to 4 digits on 12 vectors.

## 2. Numerical reproduction (NUMERICAL; M = 40, 3 windows × {h*, 3 random vectors of 𝒫_T}, K = 2·10³/2·10⁴/2·10⁵)

Own λ_A: 9.4858·10⁻⁴, 1.0421·10⁻⁷, 3.887·10⁻¹² (memo: 9.486·10⁻⁴, 1.042·10⁻⁷, 3.84·10⁻¹²; ok). Errors |truncated sum − exact|:

| window | vector | (a) comb, K=2e4 / 2e5 | (b) norm, 2e5 | (c) E_ψ, 2e5 | (d) with s_T, 2e5 | σ_T alias (Paper 46) | 2e^{−10T}Φ(5/2)Φ(−5/2) |
|---|---|---|---|---|---|---|---|
| ½log3 | h* | 1.3e−12 / 3e−15 | 2.6e−9 | 1.4e−13 | 3.2e−8 | **+4.54e−4** (λ_A = 9.49e−4) | +3.68e−4 |
| ½log3 | random 1–3 | 6e−8…2e−9 / 3e−12…2e−11 | 1.3e−5…2.8e−5 | 3e−9…2e−8 | 1.6e−4…2.0e−3 | −8.7e−7, +7.5e−5, +3.0e−5 | −5.6e−7, +5.8e−5, +2.3e−5 |
| log 2 | h* | 1e−15 / 3e−16 | 1e−12 | 2e−16 | 1.2e−11 | **+1.32e−4** (λ_A = 1.04e−7) | +1.23e−4 |
| log 2 | random 1–3 | 1e−7…7e−10 / 1e−9…7e−11 | 1.3e−5…1.6e−4 | 4e−9…3e−8 | 1.5e−4…2.0e−3 | −8.1e−7, +5.7e−5, +2.3e−5 | −7.0e−7, +5.1e−5, +2.1e−5 |
| ½log5 | h* | 4e−16 / 4e−16 | 4e−15 | 2e−16 | 1.6e−14 | **+4.88e−5** (λ_A = 3.9e−12) | +4.73e−5 |
| ½log5 | random 1–3 | 5e−8…2e−9 / 5e−10…8e−11 | 1.3e−5…1.6e−4 | 5e−9…4e−8 | 1.5e−4…1.9e−3 | −7.0e−7, +4.3e−5, +1.8e−5 | −6.6e−7, +4.0e−5, +1.6e−5 |

Readings. (i) **The memo's "10⁻⁸ in 12 tests" is only the comb part (a)** (its `part_D`: 4 windows × {h*, 2 random} = 12,
only Σv_n c_F(log n)); I reproduce it: 10⁻⁸…10⁻¹⁵ already at K = 2·10⁴ (P_T bounded and oscillatory: the tail Σ_{k>K} cancels). (ii) The
full form (d) with s_T is exact but converges like Σ_{k>K} log k/k² ≈ log K/K for a generic F of 𝒫_T (jump at ±T: |F̂(ω_k)|² ~ C/k²):
error 10⁻⁴…2·10⁻³ at K = 2·10⁵, **not 10⁻⁸**; the memo only tests it on h* (`part_E`, K = 2·10⁴ + asymptotic tail from k = 400) and
says "3–4 digits of λ_A": correct for h* (|ĥ*(ω_k)|² ~ C/k⁴ because h*(±T) ≈ 0: F(T)² = 2·10⁻³, 7·10⁻⁷, 3·10⁻¹¹), and the asymptotic
"log ω + c" used for the tail of L_T is crude (L_T(ω) = log(2Tω) + γ + ∫K_reg + O(1/ω²) on the grid; I give it exactly in the script).
(iii) **The alias is aliasless**: with s_T there is no alias term at all (error 10⁻¹⁴ for h* at ½log5); with σ_T there is the one from §0, never
negligible against λ_A. (iv) Reproduced: s_T < 0 at 3, 6, 7, 15 grid points (k ≤ 400) in the four windows; σ_T < 0 at
3, 6, 7, 14 (the term ∫_{2T}^∞cos K changes one point at ½log7).

## 3. Absolute convergence (point 3; PROVED)

s_T(ω_k) = log k + O(1), so Σ_k|F̂(ω_k)|²log(2 + k) < ∞ is needed. The memo asks for "F̂ ∈ C¹, f′ ∈ L¹" (F̂ is entire, so the
first is vacuous) and leaves it as sufficient. The correct and stronger statement: for G entire of exponential type τ the local Plancherel–Pólya
inequality |G(x)|² ≤ C_τ∫_{x−1}^{x+1}|G|² holds (subharmonicity of |G|² + type bound; standard CITED). With G = F̂ (type T):
Σ_k|F̂(ω_k)|²log(2 + |ω_k|) ≤ C∫|F̂(τ)|²log(3 + |τ|)dτ, finite **exactly on the domain of the form** of Paper 46 eq:form.
So the sum (d) converges absolutely for every F in the form's domain, and (a)–(c) for every F ∈ L²(I_T) (bounded kernels,
Σ|F̂(ω_k)|² = 4T‖F‖²). Numerical: Σ_k|F̂(ω_k)|²|s_T(ω_k)| stabilizes (h*: 0.612781/0.612782/0.612783 at K = 2e3/2e4/2e5; random vectors:
tail Σ_{k>10⁵}|F̂|²log k ≈ 10⁻⁴…2·10⁻³, convergent). Tail of an F with a jump: ≍ (F(T)² + F(−T)²)(2T/π)²·log K/K. For F ∉ domain
of the form (c_F(0) − c_F(u) not integrable against K) both sides are +∞ and (d) still holds in [0, ∞] by the monotone convergence of §1.

## 4. Novelty (point 4)

Grep "Nyquist|Shannon|sampling|muestreo|Poisson|Bernstein grid|Plancherel–Pólya" (03-research, 04-papers, 05-meta):
- Paper 46 thm:A already says the form is C₀‖F‖² + Lev(c_F) − Σv_n c_F(log n) and (l. 150) that "all T-dependence of the
 archimedean part is the elementary tail" ∫_{2T}^∞K: **the truncation of m that makes Theorem 4.1 exact is already in the paper**.
 Paper 46 uses Poisson (thm:Z, l. 2096, 2256–2260, thm:PCfinite) on the zero side and on the entire comb side, not on c_F over the grid π/2T.
- R186_113 §5(iii) (audit of R186_041) already noted: "Shannon/Boas sampling formulas, Plancherel–Pólya: exact identities with
 nodes of density ≥ T/π and positive weights for PW_T, but with Lebesgue measure, not with (σ_T − λ)dτ". That observation is
 **incorrect in one detail that Theorem 4.1 corrects**: with the weight s_T (not σ_T) the sampling formula **is** exact, because the
 truncated Lévy measure + comb + δ₀ is supported on [−2T, 2T]. That is the only new contribution: a one-line statement
 (base identity of §1 applied to thm:A), not a tool.
- R155 "Bernstein grid lemma" (Paper 46 lem:bern) is a different thing: a bound on the minimum of a band-limited function by its minimum on a
 grid; it is not an identity. R186_026 (piecewise Tate Gram) does not use sampling. Phase-33 (completeness of exponentials) and phase-78
 mention Shannon only as the Shannon number. **Nothing in the corpus states (d) with s_T**: new as a statement, classical as content
 (Whittaker–Kotelnikov–Shannon for |F̂|² ∈ PW_{2T}, or Poisson for c_F * ν with supp ⊂ (−4T, 4T)).
- **What is NOT new, nor content**: "the form does not see σ_T on any continuum" (§4 *Reading*) is a sentence with no content: ∫σ_T|F̂|²/2π
 and (1/4T)Σ s_T(ω_k)|F̂(ω_k)|² are two representations of the same functional; the cone of admissible sample vectors
 {(|F̂(ω_k)|²)_k : F ∈ 𝒫_T} is exactly that of the Nyquist samples of {|F̂|²} and is neither smaller nor more tractable (it is the same
 extremal problem; the memo acknowledges this in "(F1) … circular"). Theorem 4.1 does not change the status of any grid cell.

## 5. List

**FATAL** — none.
**MAJOR**
- M1. Identification of the symbol. s_T ≠ σ_T (Paper 46 eq:symbol); the difference ∫_{2T}^∞cos(τu)K(u)du produces on the grid the alias of §0,
 which on 𝒫_T equals Σ_{j≥1}Σ_{m≥1}2e^{−(2m+½)4Tj}Φ_F(2m+1)Φ_F(−2m) (the m = 0 term vanishes because A(F)B(F) = 0) and is ≥ 0.48λ_A at ½log3,
 10³λ_A at log 2, 10⁷λ_A at ½log5 (h*). Every sentence in §0.5, Cor. 4.2, §4 "What is missing", target Theorem 5.2 and §8 that says "symbol"
 must say "truncated symbol s_T"; in particular 5.2 "equivalently Σ_kΦ̂(kπ/2T)s_T(kπ/2T) ≥ 0" is correct only with s_T and
 **false with σ_T** (h* at log 2 gives −1.3·10⁻⁴ with σ_T). What is written is correct; what is missing is to say so at every use.
**MINOR**
- m1. Proof of (d): Poisson applied to an infinite measure (K ~ 1/u); repaired via μ_ε and monotone convergence (§1), which also
 removes the hypothesis "F̂ ∈ C¹, |F̂|² ∈ L¹, f′ ∈ L¹" and gives (d) in [0, ∞] for every F ∈ L²(I_T), with absolute convergence on the domain
 of the form (§3, local Plancherel–Pólya).
- m2. "Verified to 10⁻⁸ in 12 tests" refers to (a) (comb) only; (d) is verified only on h* (4 tests, K = 2·10⁴ + asymptotic
 tail) to 3–4 digits of λ_A; for a generic F of 𝒫_T the sum (d) truncated at 2·10⁵ has error 10⁻⁴…2·10⁻³ (tail log K/K).
 Rewrite §7.3 accordingly. The tail of L_T in `part_EF` ("log ω + c_as" fitted at k ∈ [381, 400]) can be given exactly:
 L_T(ω_k) = γ + log(2Tω_k) − Ci(2Tω_k) + ∫₀^{2T}K_reg − [(−1)^kK_reg′(2T) − K_reg′(0)]/ω_k² + O(ω_k⁻⁴).
- m3. "New in the corpus as a tool (grep: Shannon only as the Shannon number)": the memo's grep missed R186_113 §5(iii)
 and Paper 46 l. 150/thm:A; correct label: **PROVED, a Shannon reformulation of thm:A; new as a statement, not as a tool**.
- m4. §4's *Reading* ("the form does not see σ_T on any continuum", "exact energy version on windows of width π/T"): withdraw or
 rewrite as "equivalent discrete representation"; there is no new information in the samples (§4 of this review).

## 6. Labels

| statement | label after review |
|---|---|
| Theorem 4.1 (a),(b),(c) | PROVED (classical: Shannon/Poisson on c_F; band-limited kernels) |
| Theorem 4.1 (d) with s_T (truncated Lévy) | PROVED with the repaired proof of §1; valid in [0, ∞] ∀F ∈ L²(I_T), absolutely convergent on the domain of the form |
| Theorem 4.1 (d) with σ_T of Paper 46 | **FALSE**: alias Σ_{j≥1}∫c_F(v)K(4Tj − v)dv, on 𝒫_T = Σ_{j,m≥1}2e^{−(2m+½)4Tj}Φ_F(2m+1)Φ_F(−2m); h*: +4.5e−4 / +1.3e−4 / +4.9e−5 |
| "10⁻⁸ in 12 tests" | NUMERICAL, only (a); (d) 3–4 digits only on h* |
| Novelty | new statement in the corpus; content = thm:A + Shannon; corrects the note from R186_113 §5(iii) |
| Row D | unchanged (OPEN); no grid cell changes |
