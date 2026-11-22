# L2_BUILD_018 — Review

Reviewed with pen and paper against Paper 46 §2–3, N_BUILD_001 (A), and N_BUILD_011 plus its review.

## 1. Reduction (★): CONFIRMED, with one FIX in the conventions
- N_BUILD_011 defines 𝔞^λ_T = 𝔞_∞ − ∫_{(0,2T)} Re c_F dλ and 𝔞^{ρ_κ}_T = (1/2π)∫g_κ|F̂|² on P_T ∩ D_T (via N_BUILD_001 (A): ∫₀^{2T}2κe^{u/2}Re c_F = −κ𝔭). Write ν = ρ_κ + (ν − ρ_κ). Then Re c_F(u) = (1/2π)∫cos(τu)|F̂|² and Fubini give 𝔞^ν_T = (1/2π)∫[g_κ − Re E]|F̂|², with E = ∫e^{iτu}d(ν−ρ_κ) on the window. The factor is right, and the cos convention matches Re of exp. No boundary or polar term is missing: the polar term is already inside g_κ via (A), and that step uses the P_T constraint. A pointwise bound Re E ≤ g_κ − η is sufficient.
- FIX (harmless): N_BUILD_011 uses the open interval (0,2T), but the build writes [0,2T). The trapezoid atom at u = 0 (weight κh) is therefore not seen by the form. Removing it changes the form by +κh‖F‖² ≥ 0, so every lower bound still holds. Either define ν on (0,∞) or state this explicitly. The atom at 2T is invisible because c_F(2T) = 0 by continuity and support. Pointwise E then changes by an oscillating term whose pairing with |F̂|² is 0, so the build's choice is legitimate.

## 2. Lemma 1: CONFIRMED
- The geometric sum plus half-endpoints gives (h/2)coth(hw/2)(e^{wb} − e^{wa}). The integral is (e^{wb} − e^{wa})/w. The error formula is exact.
- (i) Here z = hw/2 = h/4 + ihτ/2, so Re z = h/4 > 0 for all real τ, and |coth z| ≤ coth(Re z). Using coth x ≤ 1/x + x/3 and |1/w| ≤ 2 gives the bound 4 + h²/24. Correct.
- (ii) The Mittag-Leffler expansion z coth z − 1 = Σ 2z²/(z² + π²k²) holds for every z off the poles ±iπk. The bound needs |z|² ≤ π²/4, i.e. |z| ≤ π/2. Then |z² + π²k²| ≥ π²k² − π²/4 ≥ ¾π²k², and the constant is (8/(3π²))(π²/6) = 4/9. |w| ≤ π/h is exactly |z| ≤ π/2, and that disk stays a distance ≥ π/2 from the nearest pole (±iπ). This is enough. Final constant (2/9)κ(e^{b/2}+e^{a/2})h²|w|: correct.

## 3. Theorem A: CONFIRMED
- Low band: |E| ≤ (2π/9)κ(e^T+1)h ≤ η/8 by (a), which is even better than the stated η/4.
- High band: |w| > π/h gives |τ| ≥ π/h − ½ ≥ π/(2h) (needs h ≤ π). Then m ≥ log(1/(4h)) − 1 (from lem:mbounds(ii); the correction terms are tiny). With (b): m − |E| ≥ 0.9κ(e^T+1) + η − 0.7 ≥ η, because 0.9·1.34·2 > 0.7.
- Conclusion: the true constant is ≥ ¾η ≥ η/2. The scale h ≍ ½exp(−9κ(e^T+1) − η − 1) is correct. The condition 2T ∈ hℕ is a restriction on T, which Theorem B removes.

## 4. Theorem B: CONFIRMED after a FIX of one constant
- Low band: (2/9)κ(e^{j+1}+e^j)h_j²(π/h_j) ≤ (4π/9)κe^{j+1}h_j ≤ η2^{−j−4} by (H1). The sum is ≤ η/8.
- Band i: the blocks j ≥ i are in regime (ii) because |w| ≤ π/h_i ≤ π/h_j (H3). The coarse blocks give 8.1·(1+e^{−1})·Σ_{j<i}e^{j+1} ≤ 8.1·1.368·1.582 e^i = 17.5e^i ≤ 18κe^i. (H2) at i−1 gives m ≥ 30κe^i + η − log 2 − 1 + 1, i.e. the stated value. The margin 12κe^i ≥ 16 ≫ 0.7 holds. The bands cover ℝ because h_i → 0, which (H2) forces.
- Partial block, FIX: the leftover consists of the half-atom correction at b′ (≤ κe^T h_J) plus density on [b′,2T) (≤ 2κe^T h_J). Together this is ≤ 3–4κe^{J+1}h_J ≤ (9/π)η2^{−J−4}. That is ≤ η/16 only for J ≥ 2. For J = 0, 1 it is ≤ 0.18η, not η/16. The margins absorb it: the low band gives ≥ η − 0.125η − 0.18η ≥ η/2, and the high bands are similar. The claim ≥ (η/4)‖F‖² survives. Replace "η/16" with "(9/π)η2^{−J−4} ≤ 0.18η".
- Shared endpoint 2J: when 2T > 2J both halves are inside the window, and when b′ = 2J the correction term covers it. Both cases are correct. Small T (J = 0, a partial block 0) is covered by the same estimate. The η/4 is uniform in T.

## 5. Novelty and scope: CONFIRMED novelty; DOWNGRADE §"What ℤ-primes lack" (b)–(c)
- I grepped 03-research and 05-meta for trapezoid, coth, atomic comb, and Pos. The only coth hits are unrelated (R186_105 thm:S(iii), R184_006/092). R167_103 Thm S is a class transfer of sieve bounds and has no positivity construction. BFdisc and ℕ∪√2ℕ are falsifiers. No atomic comb in Pos appears in the record. Theorem B is new.
- (a) is a correct comparison (κ = 1 < κ*). (b) and (c) are heuristic: "quadrature cannot be the mechanism" and "the sign must come from P_T-correlation" are not proved. Relabel (b) and (c) as HEURISTIC/OPEN, not PROVED. One more point: with κ = 1 < κ*, the symbol is negative somewhere, so pointwise positivity of (★) fails for ζ. This part is PROVED. It does not prove which mechanism must replace it.

## Verdict
Lemma 1, Theorem A and Theorem B are PROVED, with two cosmetic FIXes: the (0,2T) versus [0,2T) atom at 0, and the η/16 constant becoming 0.18η. The arithmetic-content section (b)–(c) is DOWNGRADED to HEURISTIC. No sign contact for ζ.
