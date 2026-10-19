# R186_030 — Structural dual certificate with β₀ = 2: classification and obstruction

Phase 186, round 15 (front 1 of R186_107 §3). Paper 47, grid and crossword are not touched. Standalone script:
`r030_class_B.py` (NUMERICAL, only to decide §3).

Prior check (cited in the text): Paper 47 def:W (l.1107), eq:nuw, thm:Z (l.1122), lem:Rrig + cor:nontermwise
(l.1249–1283, "Lemma R"), thm:C (l.917), lem:mbounds (l.689), lem:K/eq:m (l.267–273), thm:SC (l.2040), thm:AL (l.2201),
cor:mono (l.361), thm:log5W (l.4162), app:li; R155_010 (closure of the reverse track; Theorem SC, Theorem N);
R185_006 (symbol identity θ = m − v₂cos at ½log3; NO-GO of Archimedean-then-norm); R186_001 (Thm NG: Gram matrix of
translates = Bochner, not positivity); R186_019 (couplings between blocks necessary); R185_001/003 (circularity: only
touches statements about Λ, does not apply to dual certificates); R186_029 §(β) and R186_107 §3.

## 0. Verdict in one line

**"f_w ≥ 0 by identity" is, for w ∈ 𝒲_cl, the same as "f_w ≥ 0"" (Thm 1: every certification is a
Fejér–Riesz–Szegő factorization and conversely), so the content of the front is whether the
factorization is *explicit*. Of the three explicit mechanisms, (Z) zeros is closed by lem:Rrig/cor:nontermwise,
(P) primes reduces to (Z) (Thm 2), and (A) archimedean/Bochner —the only one with its own object— is **NO-GO in its
positive-measure form (class B, Thm 3: PROVED at ½log3 and ½log5 with value ≤ −0.13; NUMERICAL at log2⁺) and remains
OPEN only in its mixed form (signed measure), which is exactly the numerical certificate of thm:C.** No contact
with the sign.**

## 1. What "by identity" means (Paper 47 language)

Fix T and w ∈ 𝒲_cl. By thm:Z(i),

 f_w(τ) = m(τ) + B_w(τ), B_w := 2ĝ₀ − Σ_{n∈𝒩_T} v_n cos(τ log n) + ν̂_w, (1.1)

with m = C₀ + φ(τ²) = C₀ + ∫₀^∞ 2 sin²(τu/2) K(u) du (eq:m, lem:K) and B_w bounded, B_w = \hat{β_w} with

 β_w = 2cosh(u/2)·1_{|u|<2T} du − ½Σ_{n∈𝒩_T} v_n (δ_{log n}+δ_{−log n}) + ν_w, ν_w from eq:nuw, supp ⊂ {|u| ≥ 2T}. (1.2)

**Def 1.1 (certificate by identity).** (ν_w, 2, 0) is *structural* if there exists an explicit family
{g_j} ⊂ L²(ℝ) (finite, or indexed by a continuous parameter with an explicit measure) and a constant c such that
f_w(τ) − c = Σ_j |ĝ_j(τ)|² (resp. ∫|ĝ_s(τ)|² dσ(s)) as an identity of functions, without evaluating f_w.
This is the "zero remainder" notion (β) of R186_029 §5, corrected by R186_107 1d: what distinguishes the route is
the verification, not the value.

**Thm 1 (Szegő tautology; PROVED).** Let w ∈ 𝒲_cl^reg. (i) If f_w ≥ c on ℝ then f_w − c = |E|² with E analytic in a
strip, an outer function (f_w is real-analytic in |Im τ| < ½ with poles at ±i/2, 5i/2,… inherited from ψ; it grows
like log|τ|, and ∫ log⁺(f_w − c)/(1+τ²) < ∞; the Szegő condition holds except if f_w − c has a real zero of infinite
order, which is impossible by analyticity). (ii) Conversely every identity f_w − c = Σ|ĝ_j|² gives f_w ≥ c.
(iii) No E is entire of exponential type (f_w is not entire). (iv) The sum of squares is never finite with
g_j ∈ L²: H_w := \check{f_w} = (C₀+∫K)δ₀ − ½K(|u|)du + β_w is not a function (K ~ 1/u at 0), and a finite sum of
autocorrelations g_j∗g̃_j is continuous.
*Consequence:* "by identity" is not a narrower class than "f_w ≥ c"; it is a class of *presentations*.
The only non-tautological thing is the mechanism that produces the g_j. There are three.

## 2. The three mechanisms against the corpus

| Mechanism | Identity sought | Status | Theorem |
|---|---|---|---|
| (Z) zeros | f_w = Σ_ρ ŵ(τ−γ_ρ) with ŵ ≥ 0 (each term a square) | **NO-GO** | lem:Rrig: no continuous w ∈ L¹ with w ≡ 1 on [−2T,2T] has ŵ ≥ 0; cor:nontermwise. Independent of T>0. |
| (P) primes / Euler | close Σ_n v_n w(log n)cos(τ log n) in closed form with a sign (Euler product, −Re ζ′/ζ) | **NO-GO by reduction to (Z)** | Thm 2 below |
| (A) archimedean / Bochner | f_w = m + \hat{β_w} with β_w ≥ 0 (class B), or reorganization m ≥ bound + Fejér on the cosine | **class B: NO-GO (Thm 3: PROVED ½log3, ½log5; NUMERICAL log2⁺)**; mixed form: OPEN = thm:C | Thm 3 below |

**Thm 2 (the prime side is the zero side; PROVED).** Let w ∈ 𝒲_cl^reg. Every closed form of the prime part coming
from the Euler product has the shape Σ_n Λ(n) n^{−1/2} ω(log n) cos(τ log n) with ω such that
Σ_n Λ(n) n^{−1/2}|ω(log n)| < ∞, i.e. it is \hat{(ω·comb)}; applying the explicit formula (thm:Z(ii)) to ω cos(τ·),
that function is Σ_ρ ω̂(τ−γ_ρ) minus the archimedean and polar terms of ω. If ω = w (flat top), this is (Z) and
fails by lem:Rrig. If ω ≠ w on 𝒩_T (e.g. ω(u) = e^{−σ|u|}, Poisson, ω̂ ≥ 0, the Li–Keiper mechanism, app:li), then
f_w = [Σ_ρ ω̂(τ−γ_ρ) + (archimedean and polar of w−ω)] + Σ_{n∈𝒩_T} v_n (ω(log n) − 1) cos(τ log n): the residual
trigonometric polynomial has negative coefficients (ω < 1 on the comb) and its sum at τ = 0 is −Σ v_n(1−ω(log n)),
which no term absorbs individually; positivity again amounts to cancellation, not identity. Thus (P) adds no new
mechanism beyond (Z): the only "Euler product with a sign" is Poisson positivity, excluded in 𝒲_cl.

## 3. Mechanism (A): simplest candidate and point of obstruction

**3.1 Accounting at τ = 0 (PROVED, exact).** From (1.1), for every w ∈ 𝒲_cl:

 f_w(0) = C₀ − 𝖠_T + 8 sinh T + ν_w(ℝ) = −Δ(T) + ν_w(ℝ), Δ(T) := −C₀ + 𝖠_T − 8 sinh T. (3.1)

| T | 𝒩_T | 𝖠_T | 8 sinh T | Δ(T) |
|---|---|---|---|---|
| ½log3 = 0.549306 | {2} | 0.980258 | 4.618802 | **1.733639** |
| log2 + 10⁻³ | {2,3,4} | 2.941974 | 6.00600 | 2.30415 |
| ½log5 = 0.804719 | {2,3,4} | 2.941974 | 7.155418 | 1.158739 |

So **every** certification of value c ≥ 0 needs net mass ν_w(ℝ) ≥ Δ(T) > 0 outside the window. Check against thm:C:
ν̂(0) = 1.7337 = Δ(½log3) + 6·10⁻⁵ — Paper 47's numerical certificate is *tight at τ = 0* (as well as at 17.645 and
37.8): f(0) ≈ c. The deficit −C₀ = 5.372 (the same number as thm:SC) is what the SOS identity must produce, and the
two pieces with their own sign identity only partly do so: m = C₀ + (continuous squares) contributes −5.372 at
τ=0; the comb contributes −𝖠_T; the polar term 2ĝ₀(0) = 8 sinh T; the remainder is ν_w.

**3.2 Bochner candidate (class B).** The only way for \hat{ν_w} to have a sign *by identity* is for ν_w ≥ 0 as a
measure (then ν̂_w is positive definite and |ν̂_w| ≤ ν_w(ℝ)). In terms of w: 0 ≤ w ≤ 1 outside the window and
w(log n) = 0 for every n > e^{2T} (the *comb-vanishing* condition of thm:AL; the atoms −½v_n w(log n) do not cancel
with densities). At ½log3 the simplest candidate is w = 1 on [−log3, log3], w = 0 at log n (n ≥ 4), 0 ≤ w ≤ 1,
and f_w = θ + 2ĝ₀ + ν̂_w with θ = m − v₂cos(τ log2) the Wiener–Hopf form of R185_006 (θ(0) = −6.352).

**Thm 3 (NO-GO of class B; PROVED at ½log3 and ½log5 with elementary verifiable quadrature; OPEN at log2+10⁻³).**
*Statement.* For T ∈ {½log3, ½log5} (and, NUMERICAL by LP, log2+10⁻³) there is no (ν, 2, 0) with ν ≥ 0,
supp ν ⊂ {|u| ≥ 2T}, and f = σ_T + ν̂ + 2ĝ₀ ≥ 0 on ℝ. Moreover sup_{ν≥0} inf_τ f ≤ −κ(T) with κ > 0 explicit.
*Method (weak duality, pure mathematics).* If μ is an even probability measure with Φ := μ̌ ≤ 0 on |u| ≥ 2T,
then for every ν ≥ 0: inf f ≤ ∫f dμ = ∫k̂ dμ + ∫Φ dν ≤ ∫k̂ dμ, with k̂ = m − Σ v_n cos(τ log n) + 2ĝ₀ and
 ∫k̂ dμ = C₀ + ∫₀^∞(1 − Φ)K − Σ_{𝒩_T} v_n Φ(log n) + 2∫_{−2T}^{2T} Φ cosh(u/2), Φ(0) = 1.
*Explicit admissible tests.* Φ = [e^{−αu²} − b e^{−βu²}]/(1−b) with α > β, b ≤ √(β/α) (⇒ Φ̂ ≥ 0, Bochner),
b ≥ e^{−4T²(α−β)} (⇒ Φ ≤ 0 on |u| ≥ 2T). Non-empty family (α = 2β, β ≥ log√2/(4T²) = 0.287 at ½log3).
*Numbers.* (NUMERICAL, `r030_class_B.py`) discrete LP on a grid (ν ≥ 0 on 600 atoms in [2T, 30], τ ∈ [0,200]):
sup inf f = **−0.3005** (½log3), **−0.2789** (log2+10⁻³), **−0.5317** (½log5); the same LP with *signed* ν gives
−0.0049 / −0.0075 / −0.0749 (coarse grid; the true value is λ_W > 0, thm:C/thm:log5W — the grid does not resolve
10⁻⁴ and does not aim to). The two-order jump between ν ≥ 0 and signed ν is the **exact obstruction**: the
certificate needs negative mass outside the window. **Rigorous upper bound (2-Gaussian test, elementary quadrature of
smooth integrands; appendix):** sup_{ν≥0} inf f ≤ ∫k̂ dμ = **−0.1377** at ½log3 (α=2.312, β=1.926, b=0.913),
**−0.1284** at ½log5 (α=1.068, β=0.890, b=0.913); at log2+10⁻³ the best test in the family gives +0.00003 (does not
decide; the LP gives −0.28, so the 2-Gaussian family is too rigid there, not the statement). Decomposition at ½log3:
C₀ = −5.372, Lévy +4.594, comb +0.365 (Φ(log2) < 0: the test *rewards* the prime), polar +0.275.
*What decides it.* With ν ≥ 0, ν̂(τ) ≤ ν(ℝ) =: N and N ≥ Δ(T) by (3.1); but at the τ where 2ĝ₀ < 0 (first negative
lobe, τ ∈ (π/2T, π/T) = (2.86, 5.72) at ½log3) k̂ ≈ −0.5 and a positive ν supported on u ≥ 2T = 1.10 has ν̂ < 0 there
for atoms near 2T (cos(τu) < 0 for τu ∈ (π/2, 3π/2)): the mass that fixes τ = 0 spoils the first lobe. This is the
dual version of R186_019 ("the couplings are not a perturbation: they are necessary").

**3.3 Fejér on the cosine (the suggestion).** "increasing m + zero-mean cosine with period 2π/log2" produces
inequalities of the type m(τ) − v₂cos(τ log2) ≥ m(τ − π/log2) − v₂ for τ ≥ π/log2, which lose v₂ = 0.98 and the
growth of m over one period (≤ log(1 + π/(τ log2))). On the body [0, 3.3] where θ < 0 this bound gives nothing
(θ(0) = −6.35 is the global minimum). What the suggestion does prove by identity is the **tail**: with
lem:mbounds(ii)–(iii), f_w ≥ 0 for |τ| ≥ τ_* := 2π exp(𝖠_T + ‖ν_w‖_TV + 2|ĝ₀|_∞ + 1) (PROVED, it is the routine of
thm:C/lem:F1). The body [0, τ_*] is irreducible by this mechanism.

## 4. Structural NO-GO (statement of the excluded class)

**Thm 4 (excluded class; PROVED in (i)–(ii), (iii) PROVED at ½log3, ½log5; NUMERICAL at log2⁺).** Let T > ½log2 and
w ∈ 𝒲_cl.
(i) There is no presentation of f_w ≥ c as a sum of squares indexed by the zeros (ŵ ≥ 0): lem:Rrig.
(ii) There is no presentation of the prime part as a function of known sign via the Euler product without going
through (i): Thm 2.
(iii) There is no presentation with β_w − (atoms of 𝒩_T) ≥ 0, i.e. ν_w ≥ 0 (Bochner on the polar/outer-prime side),
for T ∈ {½log3, log2⁺, ½log5}: Thm 3.
(iv) What remains outside the class: signed ν_w, i.e. exactly the certificates of thm:C (437 atoms,
‖ν‖_TV = 90.75 against ν(ℝ) = 1.73: the negative part is 52× the net mass). Its positivity is, by Thm 1, an outer
factorization |E|² whose E has no known closed form; the only verification available is evaluation (interval
arithmetic). **Front 1 of R186_107 closes as a structural NO-GO in the precise sense (i)–(iii); the "identity" route
coincides with the numerical route at (iv).**

What is not claimed: nothing about T > ½log5, nothing about the sign of λ_W outside the record (thm:C, thm:log5W,
cor:KEP08), no equivalence with external statements. Audit falsifier (Gram matrix of {cos(τ log n)} against m): not
used; the obstruction was located earlier, in the outer negative mass, with the number Δ(T) and the LP.

## 5. Residues

(Appendix: result of the 2-Gaussian test incorporated in §3.2; labels updated.)

- (R30.1) Close Thm 3 at log2+10⁻³ with a richer Φ test (3 Gaussians or Φ = ĥ-type) — the LP indicates margin −0.28.
- (R30.2) Intermediate class: ν = ν⁺ − ν⁻ with ν⁻ *finite and explicit* (e.g. atoms at log n, n > e^{2T}, with
 w(log n) > 0) and ν⁺ a density: does a certificate exist with ν⁻ of ≤ k atoms? This is the question of
 thm:AL/Theorem N (R155_010: M ≤ 8 impossible at ½log3) seen from the sign of the atoms; OPEN, decidable by LP with
 cardinality.
