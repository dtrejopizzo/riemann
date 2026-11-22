# R186_035 — The negative archimedean cone of the PNT-window identity: NO-GO of "(★₃₃) on the cone"

Phase 186. Labels PROVED / CITED / CONDITIONAL / OPEN / NO-GO / NUMERICAL.
Sources: R186_033 (Lemma 1; = Paper 46 rem:Cheb/eq:Cheb per R186_109, accepted), R186_109 (audit, in progress),
R186_024 (piecewise Tate modes, K₁), R186_032 (Ω specification), Paper 46 thm:A, lem:K, def:PD,
thm:parityschur, lem:contA. Standalone script: `r035_cone.py` (Legendre Galerkin N = 60 in x-space, same
discretization as r033/r024; ≈ 45 s). Every number is NUMERICAL unless otherwise marked.

**Verdict in one line.** The cone 𝒞_T is characterized (Lemmas 2.1–2.3), but the claim — "on the cone the
inequality requires an O(1) margin" — is FALSE: by the S-lemma, inf{𝔞_T(F): F ∈ 𝒫_T, 𝔟₀(F) ≤ 0, ‖F‖ = 1} is
3.8·10⁻² (T = 0.62), 1.3·10⁻⁴ (log 2), ≤ 3.4·10⁻⁸ (½log5), ≈ 10³λ_A and decreasing super-exponentially; the
minimum is attained on the boundary {𝔟₀ = 0} at distance ≤ 0.03 from h*, not in the extreme direction e₋. Confirms
R186_109 §3 with an independent computation. **(★₃₃)-on-the-cone: NO-GO as a route.** Idea (i) (monotonicity of
Φe^{−u/2}) is vacuous in 𝒦_prim (Lemma 3.2, PROVED). **No contact with the sign.**

---

## 1. Notation

For F ∈ 𝒫_T, Φ = 𝒞_F, with K₁ = K − 2e^{−u/2} ≥ 0 (lem:K) and C₀ + 4 = −1.37218:
 𝔟₀(F) := (C₀+4)Φ(0) + Lev_{K₁}(Φ) (archimedean background without the k = 0 Lévy term),
 E_ψ(Φ) := 2∫₀^{2T}Φ(u)e^{u/2}du − Σ_{n<e^{2T}} v_nΦ(log n) = 2∫₁^{e^{2T}}x^{−1/2}Φ(log x) d(x − ψ(x)),
 𝔞_T(F) = 𝔟₀(F) + E_ψ(Φ) (R186_033 Lemma 1 = Paper 46 eq:Cheb + lem:K; CITED).
Cone: 𝒞_T := {F ∈ 𝒫_T : 𝔟₀(F) < 0}; (★₃₃) ⟺ 𝔞_T ≥ 0 ⟺ E_ψ ≥ −𝔟₀ on 𝒫_T. On 𝒫_T it also holds that
𝔟₀ = Γ_T − E_exp with Γ_T the full archimedean form and E_exp = 2∫₀^{2T}Φe^{u/2} (PROVED: Lev_{2e^{−u/2}} =
4Φ(0) − 2∫₀^∞Φe^{−u/2} and ∫₀^∞Φe^{−u/2} = −∫₀^{2T}Φe^{u/2} by ∫_ℝΦcosh(u/2) = 0).

## 2. Characterization of 𝒞_T (task 1)

**Lemma 2.1 (inertia; NUMERICAL on the grid, stable in N).** n₋(𝔟₀|𝒫_T) = 0 for T ≤ 0.61, = 1 on [0.62, 0.85],
= 2 on [0.9, 1.1], = 3 on [1.2, 1.3], = 4 on [1.4, 1.6]: grows ≈ linearly, one new direction every ≈ 0.2 in T.
𝒞_T is therefore the (double) negative cone of a form with n₋ negative directions: for T ≤ 0.85 it is a
"circular cone" around ±e₋ (e₋ := eigenvector of λ_min(𝔟₀|𝒫_T)); it is not a subspace.

| T | n₋ | λ_min(𝔟₀\|𝒫_T) = −sup_{𝒞_T}[1.372Φ(0) − Lev_{K₁}]/‖F‖² | λ₂(𝔟₀) | 𝔞_T(e₋) | E_ψ(e₋) | E_exp(e₋) | E_prime(e₋) | ⟨e₋,h*⟩² |
|---|---|---|---|---|---|---|---|---|
| 0.60 | 0 | +0.028 | 0.310 | 0.077 | +0.049 | −0.035 | +0.084 | 0.81 |
| 0.62 | 1 | −0.003 | 0.278 | 0.061 | +0.064 | −0.037 | +0.101 | 0.77 |
| log 2 | 1 | −0.108 | 0.171 | 0.032 | +0.140 | −0.047 | +0.186 | 0.62 |
| 0.75 | 1 | −0.180 | 0.095 | 0.026 | +0.206 | −0.055 | +0.261 | 0.52 |
| ½log5 | 1 | **−0.245** | 0.028 | 0.045 | +0.289 | −0.063 | +0.352 | 0.44 |
| 0.9 | 2 | −0.345 | −0.077 | 0.015 | +0.360 | −0.079 | +0.439 | 0.32 |
| 1.0 | 2 | **−0.437** | −0.175 | 0.026 | +0.463 | −0.098 | +0.561 | (0.56)† |

† T ≥ 0.9 is below the precision floor of λ_A (R186_023/103); h* is not reliable there, 𝔟₀ and e₋ are (O(1) form).

Reading. (a) sup_{𝒞_T}𝔟/‖F‖² = 0.245 at ½log5 and 0.437 at T = 1 (answer to task 1). (b) In the extreme
direction the arithmetic is positive, but by a margin of only 𝔞_T(e₋) = 0.03–0.06, and E_ψ(e₋) > 0 comes
**entirely from the prime term** E_prime(e₋) = −Σv_nΦ_{e₋}(log n) > 0 (Φ_{e₋}(log n) < 0: e₋ has its
negative lobe over the contacts, min Φ/Φ(0) = −0.64); E_exp(e₋) is negative. This corrects the reading of
R186_033 §3.2: it is not "the measure d(x − ψ)" in bulk, it is the comb with Φ negative at log n.
(c) **Lemma 2.2 (piecewise Tate modes; NUMERICAL).** e₋ has 98.8% (k = 5) and 99.8% (k = 9) of its mass in
E_k = span{e^{±x/2}1_B} ∩ 𝒫_T (R186_024 §1.2), exactly as h* (99.0%, 99.8%), **independently of T
on [0.6, 1.2]**. e₋ is, to that precision, a piecewise Tate exponential; ⟨e₋,h*⟩² drops from 0.81 to 0.44 on
[0.60, ½log5]: h* moves away from 𝒞_T as T grows in the reliable range, and 𝔟₀(h*) = 0.147 → 0.091 decreases ≈ 0.27/unit T
(linear extrapolation: h* would enter 𝒞_T around T ≈ 1.1; beyond precision, OPEN).
(d) **Lemma 2.3 (parity; NUMERICAL).** h*, e₋ and the boundary minimizer F_𝒞 (§4) are 100% even; the second
eigenvector h₂ of 𝔞_T|𝒫_T is odd with λ₂ = 1.9·10⁻⁴ (0.65), 1.1·10⁻⁵ (log 2), 6.4·10⁻¹⁰ (½log5): λ₂/λ_A ≈ 80–200,
consistent with thm:parityschur(o) (orthogonal sectors) and with n₋(Γ|𝒫) = 2 odd at T ≈ 0.80 (R186_028).

## 3. (★₃₃) on the cone as an explicit inequality; ideas (i)–(ii) (task 2)

**Lemma 3.1 (Stieltjes integration by parts; PROVED).** Let φ(u) := Φ(u)e^{−u/2} and
R₁(u) := e^u − 1 − ψ(e^u). Then, for every Φ ∈ 𝒦_prim (continuous Φ, Φ(2T) = 0 suffices),
 E_ψ(Φ) = −2∫₀^{2T} R₁(u) φ′(u) du.
*Proof.* E_ψ = 2∫₁^{e^{2T}} g d(x − ψ) with g(x) = x^{−1/2}Φ(log x) continuous and of bounded variation; by parts,
2[g·(x − ψ)]₁^{e^{2T}} − 2∫(x − ψ)g′dx. At e^{2T}, g = 0; at x = 1, (x − ψ)g = Φ(0) (ψ(1) = 0, x − ψ(1) = 1: this
boundary term is **not** zero). So E_ψ = −2Φ(0) − 2∫₀^{2T}(e^u − ψ(e^u))φ′du = −2∫₀^{2T}(e^u − 1 − ψ(e^u))φ′du,
using ∫₀^{2T}φ′ = φ(2T) − φ(0) = −Φ(0). ∎ (Verified: quadrature vs direct form to 4·10⁻⁴ with 4000 nodes.)
**Properties of R₁ (PROVED by finite computation):** R₁(0) = 0, R₁ ≥ 0 on [0, log 5), R₁ < 0 on [log 5, log 5.094] and
again on [log 7, log 7.04], [log 11, ·] (ψ(5) = 4.094 > 4; ψ(7) = 6.04 > 6; ψ(11) = 11.33 > 11);
max_{[0,2T]}R₁ = 1.307 (T ≤ log 2), 1.515 (T ≤ ½log5). The stretch R₁ ≥ 0 ends exactly at x = 5.

**Lemma 3.2 (the monotone class is empty; PROVED).** There is no Φ ∈ 𝒦_prim with φ = Φe^{−u/2} non-increasing on [0, 2T].
*Proof.* Φ(0) > 0 and ∫_ℝΦcosh(u/2) = 0 force Φ < 0 at some u₀ ∈ (0, 2T); since φ(2T) = 0 > φ(u₀), φ increases on
(u₀, 2T). ∎ So idea (i) (Hermite–Hadamard/monotonicity: E_ψ ≥ 0 if φ decreases) **has no
domain** in the primitive class; in fact min Φ/Φ(0) ≈ −0.64 in both e₋ and h*: the negative lobe is
structural (it is the price Tate pays), not a small oscillation.

**Idea (ii) (Φ = Φ_mon + Φ_osc, the oscillating part pays Lévy): quantitative NO-GO.** From Lemma 3.1,
 E_ψ ≥ −2·max R₁·TV⁺(φ), TV⁺(φ) := positive variation of φ on [0, 2T] (PROVED),
and TV⁺(φ)/Φ(0) = 0.58–0.64 at e₋ and 0.65–0.67 at h* (NUMERICAL): the bound is ≥ −1.9Φ(0), useless against
−𝔟₀ ≤ 0.245Φ(0). There is no version with R₁min > 0 to save it (R₁(0) = 0). The only way to get E_ψ ≥ −𝔟₀ on
the cone is the relative position of the drops of φ (where R₁ is large, just before log n) and the rises
(where R₁ is small, just after log n): it is exactly the structure of 𝒞_F at the contacts, not a
monotonicity statement. The explicit "three-quantity" form of (★₃₃) on the cone is, then,
 2∫R₁(φ′)⁻ − 2∫R₁(φ′)⁺ ≥ 1.372Φ(0) − Lev_{K₁}(Φ),
and no monotonicity/convexity inequality decides it. **Exact obstruction point: §4, with the number.**

## 4. The number that decides: infimum of 𝔞_T over the closed cone (task 3)

**Lemma 4.1 (S-lemma; PROVED in finite dimension, CITED Yakubovich/Pólya–Dines for two real forms with a strictly
feasible point, which exists for T ≥ 0.62).** If λ_min(𝔞_T|𝒫_T) ≥ 0,
 c_𝒞(T) := inf{𝔞_T(F): F ∈ 𝒫_T, ‖F‖ = 1, 𝔟₀(F) ≤ 0} = max_{t ≥ 0} λ_min(𝔞_T + t𝔟₀ | 𝒫_T) = max_{s ≥ 1} λ_min(s𝔟₀ + E_ψ | 𝒫_T).
Equivalently: "𝔞_T ≥ 0 on 𝒞_T" ⟺ ∃ s ≥ 1 with s𝔟₀ + E_ψ ⪰ 0 on 𝒫_T. (The function s ↦ μ(s) is concave;
μ(1) = λ_A; μ(s) → −∞.) For the complementary part, {𝔟₀ ≥ 0}: inf = max_{s ≤ 1}μ(s) = λ_A for T ≥ 0.62
(μ(0.9) = −0.03 … −0.15 < 0 across the whole grid): **the complement of the cone is NOT trivial**: it contains h*
(𝔟₀(h*) = +0.09 … +0.15 > 0, R186_033 §3.2) and there E_ψ(h*) = −𝔟₀(h*) + λ_A < 0. The claim "outside the cone
it's trivial" is false: outside the cone (★₃₃) requires E_ψ ≥ −𝔟₀ with both sides negative, and that is the whole problem.

**Table (NUMERICAL, N = 60; fine optimization in t; matches R186_109 §3 to 3 digits).**

| T | λ_A | c_𝒞(T) = inf_{𝔟₀≤0}𝔞_T | t* | c_𝒞/λ_A | 𝔟₀(F_𝒞) | ⟨F_𝒞,h*⟩² | ⟨F_𝒞,e₋⟩² | 𝔞_T(e₋) |
|---|---|---|---|---|---|---|---|---|
| 0.62 | 1.84e-5 | 3.79e-2 | ≥ 3 | 2056 | +2e-4 | — | — | 0.061 |
| 0.64 | 4.62e-6 | 6.20e-3 | 0.21 | 1342 | 8e-9 | — | — | — |
| 0.65 | 2.32e-6 | 2.99e-3 | 0.083 | 1288 | 2e-8 | 0.894 | 0.927 | 0.040 |
| 0.66 | 1.21e-6 | 1.46e-3 | 0.036 | 1212 | 2e-8 | — | — | — |
| log 2 | 1.01e-7 | 1.30e-4 | 0.0029 | 1284 | 5e-7 | 0.938 | 0.824 | 0.032 |
| 0.75 | 7.55e-10 | 1.46e-6 | ≈0 | 1931 | 5e-5 | 0.958 | 0.694 | 0.026 |
| ½log5 | 3.31e-12 | ≤ 3.4e-8 (floor) | ≈0 | ≲10⁴ | −0.061 | 0.971 | 0.576 | 0.045 |
| 1.0 | (floor) | ≤ 4.7e-9 | ≈0 | — | −0.349 | — | — | 0.026 |

Reading. (1) **The margin on the cone is c_𝒞 ≈ 10³λ_A**, super-exponentially small (log 2: 1.3·10⁻⁴; ½log5:
≲ 10⁻⁸), not O(1). (2) **It hides at the boundary** {𝔟₀ = 0}: the minimizer F_𝒞 has 𝔟₀(F_𝒞) = 0 to 10⁻⁷ for
T ≤ 0.75, E_ψ(F_𝒞) = c_𝒞, and is a perturbation of h* (⟨F_𝒞,h*⟩² = 0.89 → 0.97). Exact mechanism: 𝔞_T(h* + θG)
= λ_A + θ²𝔞_T(G) + O(θλ_A) and 𝔟₀(h* + θG) = 𝔟₀(h*) + 2θ𝔟₀(h*,G) + θ²𝔟₀(G); reaching 𝔟₀ = 0 costs θ ≈ 0.03 and
𝔞_T ≈ θ²𝔞_T(G) with G in the even sector of 𝔞_T, where the low eigenvalues are ≈ λ_A, 10²λ_A, 10⁵λ_A (Lemma 2.3):
c_𝒞/λ_A ≈ 10³ is the scale of the even spectrum of 𝔞_T, not a geometric constant. (3) **At ½log5 and T = 1 the
cone minimizer is already in the interior** (𝔟₀(F_𝒞) = −0.06, −0.35) with 𝔞_T ≤ 3·10⁻⁸, 5·10⁻⁹: for T ≳ 0.8 the cone
contains its own near-minimizers; the boundary ceases to be the hiding place and the cone itself is the problem.
(4) The extreme direction e₋ **does not** decide anything: 𝔞_T(e₋) ≈ 0.03–0.06 is the only stretch with
"O(1)" margin (actually 1–5% of |𝔟₀(e₋)|), and it is a measure-zero subset of the cone.

**Corollary 4.2 (does it close anything "without going through the margin"? NO).** Positivity on 𝒞_T ⟹ nothing about
𝒫_T∖𝒞_T (that's where h* lives for T ≤ 0.8); positivity on 𝒫_T∖𝒞_T = D by window in full (the infimum λ_A is
attained there). And positivity on 𝒞_T itself is a statement of precision 10³λ_A: **it inherits the margin** (it is
a case of the ARGUED Lemma H of R186_029/107: restriction to a cone = restriction + inertia). lem:contA
(continuity of λ_A in T) does not help: the problematic boundary is in F (the set {𝔟₀ = 0} ⊂ 𝒫_T), not in T, and
a continuity inequality with O(1) constants does not cross a 10⁻⁸ margin.

## 5. What remains PROVED and has lemma value

- **Lemma 3.1**: E_ψ(Φ) = −2∫₀^{2T}R₁φ′, R₁ = e^u − 1 − ψ(e^u) ≥ 0 on [0, log 5) (correction of the boundary term
 at x = 1; positive Stieltjes form of the arithmetic term **exactly up to x = 5**, where ψ(5) > 4).
- **Lemma 3.2**: no Φ ∈ 𝒦_prim has Φe^{−u/2} monotone; the negative lobe (≈ −0.64Φ(0)) is mandatory.
- **Lemma 4.1**: S-lemma for the cone; "𝔞_T ≥ 0 on 𝒞_T" ⟺ ∃ s ≥ 1 with s𝔟₀ + E_ψ ⪰ 0 on 𝒫_T; non-trivial complement.
- **Identity** 𝔟₀ = Γ_T − E_exp on 𝒫_T (§1).
- NUMERICAL: Lemmas 2.1–2.3 (increasing inertia ≈ 1 per 0.2 in T; e₋ and h* at 99.8% in piecewise Tate k = 9, uniform
 in T; parity sectors with λ₂/λ_A ≈ 10²).

## 6. Honest balance

- **NO-GO (★₃₃)-on-the-cone as a route**: margin c_𝒞 ≈ 10³λ_A at the boundary {𝔟₀ = 0} next to h* (T ≤ 0.8) and in
 the interior of the cone (T ≥ ½log5); idea (i) empty (Lemma 3.2); idea (ii) loses ≥ 1.9Φ(0). Confirms R186_109.
- **Falsified**: "O(1) margin on the cone" and "outside the cone it's trivial". Both false, with a number.
- **No contact with the sign**: no negative value of 𝔞_T (the −3·10⁻⁹/−2·10⁻⁷ from the optimizer at ½log5 and T = 1
 are noise below the 10⁻⁸ floor of the O(1) form with N = 60; the upper bounds in the table are direct Rayleigh
 quotients, reliable). Paper 46, grid and crossword are not touched.
- OPEN residue (does not deserve a round): if 𝔟₀(h*_T) changes sign (≈ T ≈ 1.1 by linear extrapolation), the
 minimizer enters 𝒞_T and the "archimedean vs arithmetic" hierarchy of R186_033 §3 reverses; deciding this requires
 precision beyond doubling (R186_023/103).
