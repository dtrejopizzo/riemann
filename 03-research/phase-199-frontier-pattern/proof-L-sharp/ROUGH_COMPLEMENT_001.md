# ROUGH_COMPLEMENT_001 — the rough complement δ = g* − g*_50 of Mori's even extremal at μ = 15 (NUMÉRICO)

Phase 199, analyst. , no zero
datum is used, **Everything quantitative is NUMÉRICO** on existing data only (Mori VIII μ = 15 even
form G = sym(A+J), 832 modes; MORI15 g*; TEST_BRIDGE rungs QF 1.5; same exterior pipeline, ω ≤ 48, 900 nodes/cell, M = 28
min-leak gauge). No new certification.
Scripts: `ROUGH_COMPLEMENT_001_{galerkin,jumps,exterior,analysis}.py`; outputs `ROUGH_COMPLEMENT_001_data/`.
Units: W* = W(g*) = 4.7634661·10⁻⁷⁰ (‖g*‖ = 1); p := g*_50 (L²(I)-projection on V_50), δ := g* − p.

**Outcome.**
1. **Exact split (arb, 400 bits):** W(p) = 1.232495 W*, 2W(p,δ) = −0.464990 W*, W(δ) = +0.232495 W* (sum 1 to 20 digits).
   The cross term is **forced**: W(p,δ) = −W(δ) + λ*‖δ‖² (PROVED, Gg* = λ*g*, δ ⊥ V_50 ∋ p), and λ*‖δ‖² = 4.6·10⁻⁷¹ W* is
   invisible. So W* = W(p) − W(δ) + O(W*‖δ‖²): any L²-projection split of the eigenvector has cross = −self-term of δ.
   W-cosine W(p,δ)/√(W(p)W(δ)) = −0.434. (The earlier 1.29 / −0.52 / +0.23 values correspond to J ≈ 1–20; at J = 50 the values are
   1.23 / −0.46 / +0.23.)
2. **δ is a bulk rough vector, not an edge/jump datum and not a layer object.** Legendre degree 100–400 carries 78 % of ‖δ‖²
   (peak at degree 246), 1.8 % in the last band (no pile-up at the truncation N); 95 % of δ lies in G-eigenvalues [1,10)
   (Rayleigh 2.395). In x it is spread uniformly: rms 4.1·10⁻³⁶ at every distance from the 14 Möbius jump points x_n = ±log(λ/n)
   (no Gibbs peaks; jumps of g* would be ~10⁻³⁴); |x| > 0.99T holds 0.54 % of the mass. Edge: δ(T) = −2.55·10⁻³⁵ = 0.18 g*(T)
   (this is the f_J(λ)/f* = 0.82 defect), = 3.75‖δ‖, below the generic 13.6‖δ‖ for that degree band.
   Exterior: ρ_δ has 2.8 % of its one-sided mass in ω ∈ (1,2) (0.36 % in (1, s₂ = 1.118)), 29 % in [2,4), 65 % in [4,48],
   3.8 % beyond; its min-gauge leak is 91 % non-prolate and its prolate part sits at k > 60 (beyond the plunge 4μ). 
3. **The (1,2) correlation is carried mainly by p, amplified by the cross term.** g*'s pair (1,2) = −1.529 W* =
   p (−0.952) + 2·cross (−0.493) + δ (−0.084): 62 % / 32 % / 6 %. Ratios (1,2)/X₁₁: p −0.350, δ −0.351, g* −0.479; the cross
   term moves the ratio from −0.35 to −0.48. Theorem C's single-tail bound is 0.054: p alone exceeds it ×6.5.
4. **Λ-sensitivity (comb part −(log m + log n)⟨φ_m,φ_n⟩, = ∂_κ of the exterior form under uniform κ-scaling):** total
   p −0.494, 2·cross +0.382, δ −0.165 ⇒ g* −0.277 W*. Per unit own value δ is the most comb-weighted piece (−0.71 vs p −0.40),
   because it lives in the cells ω ≥ 2 (diagonal comb −2∫H₁ρ²: δ −0.246, p −1.575, g* −1.974); but the arithmetic weight of
   g* is dominated by p and partly cancelled by the cross term. δ does **not** carry "the arithmetic" alone.
5. **Conjecture (RC), §5.** With the forced identity, the extremal reads W* = W(p) − W(δ); positivity of the minimizer is the
   inequality W(δ_J) < W(p_J), measured W(δ)/W(p) = 0.189 (J = 50), 0.209 (J = 15). A non-circular cross bound
   |W(p,δ)| ≤ θ′√(S(p)S(δ)) with the positive majorant S = λ∫𝔴|ρ|² measures θ′ = 0.156; positivity needs θ′ < 0.49; L′♯ at
   g* forces κμ^{−A} ≤ W*/ℓ* = 0.564, so "κ ≈ 1" is impossible at μ = 15 in the A = 0 normalization (flag).
No sign of row D claimed. L′♯ OPEN; row D OPEN.

## 0. Corpus / index check
Read: TEST_BRIDGE_001 (§2 P1, §4, §5), AUDIT_L_SHARP_10 (§3 K5, constraint 22), PROOF_L_SHARP_Z_001 (§5, §7.1), MORI15_EXTREMAL_001,
PRECHECK_T1_001, BRIDGE_001 (P0a, P1, P2), Y_001 Cor Y.9. Index README phase-199 block (l.467–476): the rough complement is
recorded only as "unattributed / OPEN" (TEST_BRIDGE, AUDIT_10). Not a retry: first decomposition of W along g* = p + δ, first
exterior datum of δ, first per-piece dilate/comb split.

## 1. Split and spectrum (`_galerkin.py`, arb 400 bits; `_jumps.py`, double on δ's O(10⁻³⁶) coefficients)
| quantity | value |
|---|---|
| ‖δ‖² | 4.623818·10⁻⁷¹ |
| W(p)/W*, W(p,δ)/W*, W(δ)/W* | 1.232495, −0.232495, 0.232495 (radii ≤ 2·10⁻¹³) |
| W(g*,δ) | 0 within radius (= λ*‖δ‖², 10⁻¹⁴⁰ scale) |
| Rayleigh(δ) | 2.395168 (double cross-check 2.395168) |
| Legendre energy of δ by degree | 0–50: 1.5 %, 50–100: 4.9 %, 100–200: 27.5 %, 200–400: 50.2 %, 400–800: 11.3 %, 800–1200: 2.8 %, 1200–1664: 1.8 % |
| G-eigen content of δ | λ ∈ [0.1,1): 4.6 %, [1,10): 95.4 %, < 10⁻² : 3·10⁻⁶ |
| δ x-mass | |x| > 0.5T: 58 %, > 0.9T: 6.8 %, > 0.99T: 0.54 % (uniform measure: 50 / 10 / 1 %) |
| δ vs jump points | rms 4.5, 4.1, 3.9, 4.4·10⁻³⁶ at distance [0,0.002), [0.002,0.01), [0.01,0.03), [0.03,0.1) T |
| δ(T), δ′(T) | −2.55·10⁻³⁵, −3.7·10⁻³¹ (interior |δ′| ~ 1.5·10⁻³³: Legendre P′_n(1) endpoint growth, not a jump) |
| odd sector (p1) | tail ‖coef_{j≥400}‖/√W: odd 0.148, even 0.172 — same rough floor at scale √W in both parities |
Reading (4): δ is not a jump/edge datum (no Gibbs localization; edge value below generic) and the comparable floor in the odd
sector makes a parity-projection artefact of the even sector unlikely (weak evidence, two vectors). Physical vs Galerkin is
still not decided (needs N ≠ 832); the spectrum decaying before N argues mildly against a pure truncation artefact.

## 2. Exterior datum ρ_δ (`_exterior.py` = TEST_BRIDGE pipeline, linear; check ρ_{g*} − ρ_p − ρ_δ = 0 to machine precision)
| piece | one-sided mass (×10⁻⁷⁰) | (1,1.01) | (1,s₂) | (1,2) | [2,4) | [4,48] | >48 | leak non-prolate | S_layer/W* | S_{≥2}/W* |
|---|---|---|---|---|---|---|---|---|---|---|
| g* | 1.0895 | 4.5 % | 13.8 % | 41.5 % | 21.7 % | 36.1 % | 0.8 % | 43 % | 1.221 | 3.995 |
| p | 0.9276 | 5.3 % | 16.3 % | 48.8 % | 17.8 % | 32.1 % | 1.3 % | 35 % | 1.223 | 3.021 |
| δ | 0.0869 | 0.01 % | 0.36 % | 2.8 % | 28.8 % | 64.7 % | 3.8 % | 91 % | 0.007 | 0.516 |
ω-spectrum of ωρ(ω) on [2,48] (all frequencies ≤ c, as they must be): δ has 42 % below c/8 and 8.3 / 5.4 / 4.1 / 4.6 % at
c/2, c/3, c/5, c/7 (±3 %), 1.1 % at c; p has 63 % below c/8, 8.7 % at c. The band-edge frequency c (prolate/edge content) is
weak in δ; δ is dominated by low frequencies (interior support of its Möbius inverse) and the c/n lines (interior jump points
u = λ/n of the Möbius inverse).

## 3. Dilate decomposition per piece (`_analysis.py`; X_mn as TEST_BRIDGE §1; cross = ½(X^{g*} − X^{pp} − X^{δδ}); W* units)
| piece | Σ X (ext) | Galerkin | X₁₁ | Σ diag | off-diag | (1,2) | (1,3) | (1,4) | (1,5) | non-res | comb (log) part |
|---|---|---|---|---|---|---|---|---|---|---|---|
| pp | 1.327 | 1.232 | 2.718 | 3.300 | −1.973 | −0.952 | −0.653 | +0.108 | −0.342 | −0.018 | −0.494 |
| pδ (bilinear) | −0.229 | −0.232 | 0.117 | 0.165 | −0.394 | −0.247 | −0.124 | +0.041 | −0.057 | −0.006 | +0.191 |
| δδ | 0.233 | 0.232 | 0.240 | 0.339 | −0.106 | −0.084 | −0.043 | +0.011 | −0.017 | +0.031 | −0.165 |
| g* | 1.102 | 1 | 3.193 | 3.969 | −2.867 | −1.529 | −0.943 | +0.199 | −0.474 | +0.001 | −0.277 |
(g* = pp + 2pδ + δδ; ext/Galerkin closure +7.7 % (pp), −1.5 % (pδ), +0.3 % (δδ), +10 % (g*; all three are off-core since
f(λ) ≠ 0, where I1 is not an identity — AUDIT_10.) Correlations X₁ₙ/√(X₁₁Xₙₙ): p −0.43 / −0.49 / −0.63 (n = 2, 3, 5);
δ −0.32 / −0.26 / −0.30; g* −0.56 / −0.58 / −0.75. The archimedean (Θ_∞) part dominates every (1,n) pair in all three pieces
(pδ: −0.307, −0.180, −0.107 at n = 2, 3, 5).
**Comb pieces (n = 2, 3, 4, 5, 7):** diag (n,n): pp −0.261, −0.218, −0.168, −0.135, −0.096; 2·pδ −0.048, −0.038, −0.022, −0.011,
−0.006; δδ −0.046, −0.043, −0.032, −0.023, −0.015. Pair (1,n): pp +0.233, +0.288, −0.085, +0.284, +0.233; 2·pδ +0.120, +0.112,
−0.055, +0.099, +0.045; δδ +0.021, +0.020, −0.008, +0.015, +0.006. **Answer to (3):** the arithmetic (comb) content is mostly in
p; δ's share is ≈ 10–20 % per prime, and the cross term enters with the opposite sign to p's diagonal comb.
**Answer to (2):** the −0.48 (1,2) correlation of g* is 2/3 p and 1/3 cross term; the cross term is what lifts p's −0.35 to −0.48.

## 4. Edge vs parity (question 4)
δ(T)/g*(T) = 0.18 = 1 − f_J(λ)/f*(λ): the edge defect of the rung span is inherited by δ, but δ is not concentrated there
(mass at |x| > 0.99T 0.54 %, edge value 3.75‖δ‖ vs generic 13.6‖δ‖). Not a jump datum in x (§1). The odd extremal has the
same relative rough floor (§1, last row). Verdict: **bulk rough vector at Legendre degree ≈ 250 with O(1) Rayleigh, exterior
in ω ≥ 2, non-prolate**; AUDIT_10's hypothesis "δ = edge/jump datum" is not supported (NUMÉRICO, one μ).

## 5. Conjecture (RC) "prolate + rough" — precise form with measured numbers (OPEN)
Exact (PROVED, linear algebra): for the eigenvector g* and any split g* = p + δ with p the L²-projection on a subspace V,
W(p,δ) = −W(δ) + λ*‖δ‖², hence W(g*) = W(p) − W(δ) + 2λ*‖δ‖². The trivial bound W(p+δ) ≥ W(p) − 2|W(p,δ)| + W(δ) is an
equality-up-to-sign here and carries no information.
- *Flag.* Cauchy–Schwarz |W(p,δ)|² ≤ W(p)W(δ) presupposes W ≥ 0 on span{p,δ} — circular. The measured W-cosine −0.434 is a
  number, not a usable hypothesis.
- **(RC) Conjecture.** For the low rung block V_J (J ≥ J₀(μ)) and every admissible g = p + δ (p ∈ V_J, δ ⊥ V_J):
  (i) W(p) ≥ a·S(p) on V_J (P1-type coercivity; measured W(p)/S(p) = 0.29), (ii) W(δ) ≥ b·S(δ) on V_J^⊥ (measured 0.44),
  (iii) |W(p,δ)| ≤ θ′√(S(p)S(δ)) with θ′ < √(ab) (measured θ′ = 0.156 < √(0.29·0.44) = 0.36),
  where S = λ∫𝔴|ρ|² ≥ 0 (non-circular majorant). Then (AM–GM) W(g) ≥ (1 − θ′/√(ab))·(a S(p) + b S(δ)) > 0, and with ℓ ≤ 2S/log 2μ (ARGUED: needs 𝔴 ≥ log 2μ on
  every cell, Lemma B.0 type, and S(g) ≤ 2(S(p)+S(δ))) this gives L′♯ with κμ^{−A} ≍ ¼(1 − θ′/√(ab))·min(a,b)·log 2μ. Measured at g*: margin 1 − 0.156/0.36 ≈ 0.57.
- In leak units: |W(p,δ)| = 0.504√(ℓ(p)ℓ(δ)) (ℓ(p) = 1.508, ℓ(δ) = 0.141, ℓ(g*) = 1.772 W*); W/ℓ = 0.82 (p), 1.65 (δ), 0.564 (g*).
- *Flag on "κ ≈ 1".* L′♯ at g* itself requires κμ^{−A} ≤ W*/ℓ* = 0.564 at μ = 15; κ ≈ 1 with A = 0 is excluded by the
  data. The relevant question is the μ-trend of θ′ and of (i)–(ii) (only μ = 15 available).
- (iii) is the new object: a cross-dilate inequality between the smooth rung block and its rough complement. Its numerical
  content at μ = 15 is dominated by the archimedean (1,2), (1,3) pairs (§3).

## 6. Labels
NUMÉRICO: all tables (μ = 15, Galerkin data, M = 28 gauge, ω ≤ 48 + tail bracket). PROVED: the forced-cross identity (§5).
OPEN: (RC); physical vs Galerkin origin of δ; μ-trend. Falsified (NUMÉRICO): "δ carries the (1,2) deficit" and "δ is the
edge/jump datum". **Do not retry:** attributing the resonant deficit or the Λ-content of g* to δ alone; using
|W(p,δ)| ≤ √(W(p)W(δ)) as a step (circular). No sign claimed. L′♯ OPEN; row D OPEN.
