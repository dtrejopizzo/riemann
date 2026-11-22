# L2_BUILD_004 — Localization of 𝔞_T by a partition of unity: exact identity, criticality, NO-GO (expanded)

## Corpus check (whole corpus)
- 03-research/phase-106-global-modular-star-audit/106_47, 106_59: a "nonlocal IMS identity" for the
  Weil form is already used (localized Birman–Schwinger gate); 106_59 concludes "a proof cannot be
  obtained from IMS localization or the PNT tail floor alone".
- 03-research/phase-121-negative-witness-rigidity/OPTION_MATRIX.md, P121_FIVE_NONCIRCULARITY_AUDITS:
  "minimal-span radical localization ... the nonlocal IMS cross term has no sign on a sign-changing
  state; signing it is the primitive gap in localized form — rejected absent a new Euler-specific
  cut identity".
- phase-116 CANDIDATE_LOG_SCHUR_THEOREM l.97 mentions IMS/commutator localization as an option.
- Paper 46 rem:coer-nogo (sharp blocks, Hilbert constant).
Verdict: §1 (identity) is a REPEAT of 106.47 in substance; §2 (primes are pure coupling below log 2),
§3 (two-sided O(1) criticality) and §4 (explicit Tate-free NO-GO threshold T_loc via 1_{I_T}) are not
found in the corpus in this form. The route as a whole is a repeat of P121's rejected option; it is
kept only as a record of these three sharpened facts.

Idea: replace sharp Tate blocks (whose coupling has Hilbert norm π/2, rem:coer-nogo) by a smooth
partition and an exact localization identity. Corpus: no prior use for 𝔞_T of an IMS-type identity
(grep "IMS", "partition of unity", "localization formula" in phases 160–188 and Paper 46).

## 0. The Lévy form (from lem:K)
By eq:m, m(τ) = C_0 + ∫_0^∞(1 − cos τu)K(u)du with K > 0, K(u) = u^{-1} + O(1) (u↓0),
K(u) ≤ u^{-1} + ½ (proof of prop:archneg). For F ∈ L²(ℝ) in the form domain,
  𝔞_∞(F) := (1/2π)∫m|F̂|² = C_0‖F‖² + ¼∬_{ℝ²}|F(x) − F(y)|² K(|x−y|) dx dy.   (0.1)
*Proof.* (1/2π)∫(1 − cos τu)|F̂|²dτ = 𝓕(0) − Re𝓕(u) and ∫|F(y+u) − F(y)|²dy = 2𝓕(0) − 2Re𝓕(u);
integrate against K over u > 0 and use evenness (Tonelli: all integrands ≥ 0). ∎
And 𝔞_T = 𝔞_∞ + Π_T, Π_T(F) = −Σ_{n∈N_T} v_n Re𝓕(log n).

## 1. Localization identity (PROVED)
Let χ_j (j ∈ J, finite) be real Lipschitz functions with Σ_jχ_j² ≡ 1 on I_T. Put G_j = χ_jF,
ω̃(x,y) := Σ_j(χ_j(x) − χ_j(y))² ∈ [0, 2·#{j: χ_j(x)≠0 or χ_j(y)≠0}]. For F ∈ L²(I_T) in the form domain:
  𝔞_∞(F) = Σ_j 𝔞_∞(G_j) − ¼∬ ω̃(x,y) K(|x−y|) Re F(x)F̄(y) dx dy.   (1.1)
*Proof.* Pointwise, Σ_j|G_j(x) − G_j(y)|² = |F(x)|²Σχ_j(x)² + |F(y)|²Σχ_j(y)² − 2Σχ_j(x)χ_j(y)Re F(x)F̄(y),
and 2Σχ_j(x)χ_j(y) = Σχ_j(x)² + Σχ_j(y)² − ω̃(x,y). Where F(x)F̄(y) ≠ 0 both x, y ∈ I_T, where
Σχ_j² = 1; where F(x) = 0 or F(y) = 0 the cross term vanishes and |F(x)|²Σχ_j(x)² = |F(x)|² wherever
F(x) ≠ 0. Hence |F(x) − F(y)|² = Σ_j|G_j(x) − G_j(y)|² − ω̃(x,y)Re F(x)F̄(y) for all x,y. Integrate
against ¼K(|x−y|): the left side and each Σ_j term are finite by (0.1) (G_j is in the form domain:
|G_j(x)−G_j(y)|² ≤ 2|F(x)−F(y)|² + 2Lip(χ_j)²|x−y|²|F(y)|², and ∫_{|u|≤1}u²K < ∞), so the remaining term is
absolutely convergent; Σ_j C_0‖G_j‖² = C_0‖F‖². ∎

## 2. Primes are pure coupling (PROVED)
If every supp χ_j is an interval of length < log 2, then for n ∈ N_T (n ≥ 2):
Re𝓕_{G_j}(log n) = 0 for every j, and ω̃(x, x − log n) = Σχ_j(x)² + Σχ_j(x − log n)² = 2 for x, x−log n ∈ I_T.
Hence
  𝔞_T(F) = Σ_j 𝔞_∞(G_j) − ¼∬ ω̃(x,y) Re F(x)F̄(y) d𝒦(x − y) dy,   𝒦 := K(|u|)du + Σ_{n∈N_T} v_n(δ_{log n} + δ_{−log n}).   (2.1)
*Proof.* χ_j(x)χ_j(x − log n) = 0 since |supp χ_j| < log 2 ≤ log n, so 𝓕_{G_j}(log n) = 0 and the two
terms χ_j(x)χ_j(x−log n) in ω̃ vanish. The prime part of (2.1) is ¼·Σv_n·2·[∫2ReF(y+log n)F̄(y)dy] ... i.e.
¼·Σ_n v_n·(2+2)Re𝓕(log n) = Σ v_n Re𝓕(log n) = −Π_T(F) (each delta gives ∫ω̃ ReF(y±log n)F̄(y)dy = 2Re𝓕(log n)). ∎

## 3. Exact criticality (PROVED to O(1))
Fix ℓ ∈ (0, 1/e], and the partition of ℝ into intervals of length ℓ with transitions of width
ρ = ℓ/4: χ_j = cos/sin of a linear ramp across each transition, so Σχ_j² = 1, |χ_j'| ≤ π/(2ρ), at most
two χ_j are nonzero at any point, supp χ_j has length ℓ + ρ < log 2.
(a) Local lower bound. For G supported on an interval of length ℓ' = ℓ + ρ ≤ 5ℓ/4 and Ω > 0:
|Ĝ(τ)| ≤ ‖G‖₁ ≤ √ℓ'‖G‖, so (1/2π)∫_{|τ|≤Ω}|Ĝ|² ≤ (Ωℓ'/π)‖G‖². With Lemma 2 of 001 (m ≥ log(2+|τ|) − κ):
𝔞_∞(G) ≥ log(2+Ω)(1 − Ωℓ'/π)‖G‖² − κ‖G‖². Taking Ω = 1/(ℓ'L), L = log(1/ℓ'):
  𝔞_∞(G) ≥ (L − log L − 1/π − κ)‖G‖².
(b) Coupling upper bound (Schur test). For fixed x, ∫ω̃(x,y)K(|x−y|)dy ≤ ∫_{|u|≤ρ}2(π/(2ρ))²·2u²(u^{-1}+½)du
+ 2∫_{|u|>ρ}... ≤ C₁ + 2·2∫_ρ^∞K(u)du, using ω̃ ≤ 2(π/2ρ)²·2u² for |u| ≤ ρ (≤ 4 terms... at most 4
indices, each (Δχ)² ≤ (π/2ρ)²u²; we keep the crude 4(π/2ρ)²u²) and ω̃ ≤ 4 for |u| > ρ (at most 4
indices nonzero at x or y, Σ(Δχ)² ≤ Σχ_j(x)² + Σχ_j(y)² ... ≤ 2·(1+1) = 4 by (a−b)² ≤ 2a²+2b²).
Better: ω̃ = 2 − 2Σχ_j(x)χ_j(y) ≤ 2 + 2 = 4 always, and = 2 when no index is common. With
∫_ρ^∞K = log coth(ρ/4) + 2arctan e^{−ρ/2} ≤ log(4/ρ) + ρ/12 + π/2 (elementary: coth z ≤ 1/z + z/3):
  |¼∬ω̃K ReFF̄| ≤ ¼ sup_x∫ω̃K dy ‖F‖² ≤ (2 log(1/ρ) + C₂)‖F‖² ;
with the exact value ω̃ = 2 off common supports one gets, for x in the middle third of a block,
¼∫ω̃K dy = ½[∫_{d₁}^∞K + ∫_{d₂}^∞K] + O(1) = ½[log(1/d₁) + log(1/d₂)] + O(1) with d₁ + d₂ ≍ ℓ, i.e.
log(1/ℓ) + O(1); and sup_x ≤ ½log(1/ρ) + ½log(1/ℓ) + O(1) = log(1/ℓ) + O(1) since ρ = ℓ/4.
So the Schur-test value is log(1/ℓ) + O(1) from above and below (lower bound at the block midpoint).
(c) Conclusion: local gain log(1/ℓ) − loglog(1/ℓ) − O(1), coupling cost log(1/ℓ) + O(1): the
leading logarithms cancel exactly (scale criticality of the 1/u kernel), and the net is
−loglog(1/ℓ) − O(1) < 0 for ℓ small. The O(1) constants are explicit but the net is negative for
every admissible ℓ in the range where (a) applies.

## 4. NO-GO (PROVED) for Tate-free localization chains
Declared class 𝒞_loc: lower bounds for 𝔞_T on P_T of the form Σ_j(lower bound for 𝔞_∞(G_j)) −
(bound for the coupling term of (2.1)), in which no step uses A(F) = B(F) = 0. Such a bound is a lower
bound for 𝔞_T on all of L²(I_T) ∩ D_T.
**Claim.** For T > T_loc := (8 + π²/12)/(2|C_0|) (< 0.822), the bottom of 𝔞_T on L²(I_T) is negative;
hence no member of 𝒞_loc certifies any such window.
*Proof.* F_T := (2T)^{-1/2}1_{I_T}, ‖F_T‖ = 1. In (0.1), |F_T(x) − F_T(y)|² = 1/(2T) iff exactly one
of x, y lies in I_T, so
¼∬|F_T(x)−F_T(y)|²K = (1/4T)∫_{I_T}∫_{ℝ∖I_T}K(|x−y|)dy dx = (1/4T)∫_{−T}^{T}[∫_{T−x}^∞K + ∫_{T+x}^∞K]dx
= (1/2T)∫_0^{2T}∫_s^∞K(u)du ds = (1/2T)∫_0^∞ min(u,2T)K(u)du ≤ (1/2T)∫_0^∞uK(u)du.
By lem:K, ∫_0^∞uK = 2Σ_{k≥0}(2k+½)^{−2} = 8 + 2Σ_{k≥1}(2k+½)^{−2} < 8 + 2Σ_{k≥1}(2k)^{−2} = 8 + π²/12.
So 𝔞_∞(F_T) < C_0 + (8 + π²/12)/(2T) < 0 for T > T_loc. Since F_T ≥ 0, 𝓕_T ≥ 0 and
Π_T(F_T) = −Σv_n𝓕_T(log n) ≤ 0. Hence 𝔞_T(F_T) < 0. ∎
Numerics-free arithmetic: C_0 = −5.3721… (lem:K), 8 + π²/12 < 8.83, T_loc < 8.83/10.74 < 0.822.
For ½log5 < T ≤ T_loc the same conclusion for the archimedean part follows from prop:archneg (CITED,
interval arithmetic, test function F_odd(t) = t); whether 𝔞_T itself is negative on L²(I_T) there
needs the sign of Π_T(F_odd), not examined: OPEN, minor).

## 5. Review
- §1, §2: exact, complete. The earlier sketch's appeal to "commutation" is replaced by the pointwise
  identity. PROVED.
- §3: (a) is complete. (b) the upper bound with crude constant is complete; the two-sided
  "log(1/ℓ)+O(1)" is proved by the midpoint/near-edge evaluation using ω̃ = 2 off common supports,
  with O(1) from K = 1/u + O(1). PROVED to O(1). §3(c) is a statement about these estimates only.
- §4: corrected from the first draft: the NO-GO is that Tate-free chains bound the L²(I_T)
  bottom, which is negative; PROVED for T > T_loc (< 0.822) by the test function 1_{I_T} (positive
  autocorrelation, so primes only help the falsifier). (L2) concerns T > ½log5 = 0.8047; the gap
  (0.8047, T_loc] is OPEN (minor).
- Lesson: any localization must keep the Tate conditions, which are global (two functionals on all
  of I_T). This is why thm:coer-schur works with block-Tate conditions.
