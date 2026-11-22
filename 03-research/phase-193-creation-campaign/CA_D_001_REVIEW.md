# CA_D_001 — Review
Checked vs P46 prop:shape-phase (σ_T = 2Θ′, Z_T real), def. of P_T (F̂(±i/2) = 0), eq:symbol; EI_003; CA_B_001/002 reviews. Pen and paper, line by line.

## Verdict
**Theorem 1, Theorem 1′, Corollary 1.1: CONFIRMED PROVED (re-derived below). Theorem 1″: PROVED under its listed hypotheses. As a sign step for row D: EXCLUDED (O10, O12 survive by Theorem 1″; (R)(10),(11)) — the memo says so itself. Not REF-D (a different form). This is the first PROVED, zero-free, Euler×FE×pole-joint positivity of the campaign: ENDORSED as a tool and index entry.** Two minor FIXes, one consequence for front B.

## 1. Re-derivation
| step | check |
|---|---|
| phase | e^{iθ}ζ(½+iτ) real; 1/Z_{<X}(½+iτ) = e^{−C_X}e^{+iS_X}, S_X = ΣΛ(n)n^{−½}sin(τ log n)/log n. So Θ = θ − S_X makes e^{iΘ}Z_X real, and Θ′ = θ′ − ΣΛ(n)n^{−½}cos(τ log n) = ½m − ½Σv_n cos = ½σ_T ✓ (θ′ = ½m) |
| Lemma 1 | Z_X − 1 = X^{−s}H + κ_X X^{1−s}/(s−1); H regular at 1, polynomial growth on Re s ≥ ½ (W = 1/Z_{<X} absolutely convergent at σ = ½ ✓; convexity bound ✓), bounded as σ→∞ by the Euler gap ✓; half-plane Paley–Wiener–Schwartz ✓ (orientation: Re s>½ ⟺ Im τ<0, e^{−iτu} bounded for u ≥ 0 ✓). Pole term = transform of −κ_X e^{u/2}1_{u<2T} ✓ (computed) |
| Lemma 2 | Re(Ḡ·iG′) = φ′r²; iG′ = (ug)ˇ; Parseval ✓ |
| Thm 1(a) | Ê = (E(−·))ˇ, even ⇒ same; convolution supports ✓; for u ≤ T and |w| ≤ T, u − w ≤ 2T so the cutoff is inactive and (E∗μ_−)(u) = −κ_X e^{u/2}Ê(i/2) = 0 by Tate ✓ (Ê(i/2) = ½(F̂(i/2)+F̂(−i/2))) |
| Thm 1(b)–(d) | Ê real, Ô imaginary, g real; ∫uE² = 0 (E² even), cross term 0 (supports) ✓; cross term Re(Ê·Ô̄) = 0 ✓; Plancherel ‖g‖² = ‖E‖² + ‖R‖² ✓ |
| Cor 1.1 | (i) from ρ_F ≥ 0 ✓; (ii) rearrangement ✓; T < ½log2: Z_X = ζ, Θ = θ ✓ |
| Thm 1′ | (e^{v/2}1_{v<2T})^{∗j} = e^{u/2}(2jT−u)^{j−1}/(j−1)! on u<2jT ✓; for u ≤ (2j−1)T the integrand is e^{−w/2}·(poly of degree j−1 in w) ⇒ killed by F̂^{(l)}(i/2) = 0, l < j ≤ k ✓; Lemma 2 with φ = kΘ ⇒ factor 1/k ✓ |
| §4 central cell | |τ log n| ≤ π/4 ⇒ cos ≥ 1/√2 ✓; |ζ| ≤ |s|/|s−1| + 2|s| ≈ 2.55 ✓ |

## 2. FIXes
1. Thm 1″ for O7 (quartets): the quartet factor is a polynomial/rational factor in s, not a Dirichlet series; multiplication by a polynomial in s is a differential operator in u and preserves supports, so the support argument likely survives, but Lemma 1's growth/pole hypotheses must be re-checked for the model of def:quartetmodel. Keep ARGUED (as labelled).
2. §4 (4.1): 𝒵F = g_F is supported in [−T,∞), outside the window; "𝔞_T(𝒵F)" is the symbol form on L²(ℝ), not the window form on P_T. Say so (the memo nearly does).

## 3. Modifications / (R) / REF-D / retry
O10 (Epstein/DH), O12 (ζ_K): survive (Thm 1″) ⇒ EXCLUDED as the sign step. O1–O6 (no FE): Lemma 2 gives a different symbol (memo §3(c)) — destroyed, but irrelevant given O10/O12. (R)(2),(4) met; (R)(1),(10),(11) not met at the sign step. Not REF-D. Retry: none found (closest EI_002/CA_B_001, different weight and a proved sign).
**Consequence for front B (endorsed):** CA_B_001 §4's ARGUED claim "the sign of a |ζ|²-weighted window form is zero geometry" is too broad: with weight |F̂|²|ζ/Z_{<X}|² on primitive tests the sign is PROVED zero-free. Scope CA_B_001 §4 to its frozen weight F̂₀²|Z_{<X}|² (non-primitive profile).
