# R168_103 — The small-y regime (O167.101.2)

*Phase 168. Inputs: R167_101 (Thm A, Lemma O, Prop E), R167_291, R165_102 (Det±, Lemma 4.10 of R163_401), R163_401 §4.8 (I1), R163_115, R163_702 (K_H).*
*Notation: quartet ρ* = ½ ± δ + iγ*, δ = δ*, Λ = log(γ*/2π), y = δΛ, y₀ = 2.1773 (lattice threshold). Witness G real on ℝ, entire of exponential type τ (= T in the R167 normalisation), ‖G‖_∞ = M. Node = real zero of G.*

## 0. Status

**OPEN. No label change for (★_cell).** Results:
- Lemma 2 (PROVED): a negative quartet forces a node of G near γ*.
- (★_loc) (PROVED reduction): local (★_cell) in this regime reduces to one on-line zero at distance ≳ δ inside the cell.
- (P_gap) (OPEN): the needed input. It is a pointwise anti-clustering/anti-gap statement around a hypothetical off-line zero. RH implies it, nothing unconditional gives it, and M_m violates it freely.

## 1. What classical inputs give. PROVED-CITED

- γ* ≤ H = 3·10¹²: there is no quartet (Platt–Trudgian 2021).
- Zero-free regions (dlVP, Vinogradov–Korobov) bound σ away from **1**. So they give an **upper** bound δ ≤ ½ − c/(log γ)^{2/3+o(1)} and say nothing for small δ. *(A draft of this memo used them to empty the small-y regime. That was a direction error, and it is withdrawn.)*
- Zero-density near the line (Selberg, N(σ,T) ≪ T^{1−(σ−½)/4} log T): quartets with y = O(1) are rare but not absent. This is useless for a single witness.

## 2. A negative quartet forces a nearby node. PROVED

Write t_q = γ* + iδ (the conjugate case is symmetric). Since G is real on ℝ,
Re G(t_q) = Σ_{k even} G^{(k)}(γ*)(iδ)^k/k!, Im G(t_q) = Σ_{k odd} (…).
By Bernstein, |G^{(k)}| ≤ τ^k M on ℝ. Hence

  |Re G(t_q) − G(γ*)| ≤ M(cosh τδ − 1),  |Im G(t_q) − δG′(γ*)| ≤ M(sinh τδ − τδ).

**Lemma 2 (quartet sign).** Re G(t_q)² = (Re G)² − (Im G)². So Re G(t_q)² < 0 implies
  |G(γ*)| < δ|G′(γ*)| + M·ε(τδ), ε(u) := e^u − 1 − u.
If moreover |G′(γ*)| ≥ 4τ²M r with r := 2(δ + Mε(τδ)/|G′(γ*)|), then G has a node x₀ with |x₀ − γ*| ≤ r.

*Proof.* The first claim is the remainder bounds above. For the second: on [γ*−r, γ*+r] we have |G′(x) − G′(γ*)| ≤ τ²M r ≤ |G′(γ*)|/4. So G is strictly monotone there with |G′| ≥ ¾|G′(γ*)|. It moves by at least ¾ r|G′(γ*)| > |G(γ*)| on each side, so it changes sign. ∎

**Remark 2a (size of τδ in the regime).** Det+ places contact at T ≤ T_L + 0.226. In the model T_L ≈ πρ with ρ = Λ/2π, so τ ≈ Λ/2 and τδ ≈ y/2 ∈ (0, 1.09). Then:
- For y ≪ 1, ε(τδ) = O(y²) and Lemma 2 gives |x₀ − γ*| ≤ 2δ(1+o(1)). This is the task's picture, and it is PROVED.
- For y near y₀, ε(1.09) ≈ 0.88. The node lies within O(1/τ) = O(1/Λ) of γ*. That is the **mean-spacing scale**, so the pinning carries no information beyond "the quartet sits in some cell". This scaling is ARGUED (it uses the model T_L).
- Degenerate case |G′(γ*)| < 4τ²Mr: G has a near-double zero at γ*, and the quartet's negative mass is ≤ (δ|G′| + Mε)² = O(M²(τδ)²·…). The bookkeeping is the same as in §3.

## 3. What (★_cell) requires in the narrow window. PROVED (reduction)

Fix T ∈ [T_L − C, T_L + 0.226], a window of bounded length (Det+, PROVED-CITED R165). Let I be the node cell of G containing γ*. Locally the quartet's negative mass is ≤ 2(δ|G′(x₀)| + Mε)². Near x₀, on-line zeros contribute G(γ)² ≥ ¾²G′(x₀)²(γ−x₀)² for |γ−x₀| ≤ r_*, where r_* = |G′(x₀)|/(4τ²M). So **local** (★_cell) holds as soon as

 (★_loc) Σ_{γ on-line, |γ−x₀| ≤ r_*} (γ − x₀)² ≥ (32/9)(δ + Mε(τδ)/|G′(x₀)|)².

In the deep regime y ≪ 1 this reads: **at least one on-line zero at distance ≥ 1.9δ from x₀, inside the cell.** This is exactly R163_401 (I1) with the local count. PROVED as a sufficient condition. It is not necessary: other cells can pay (the global form).

## 4. The needed input and its logical strength

**(P_gap)** For every off-line zero ρ* with δΛ < y₀ and γ* > H, the interval |x − γ*| ≤ c₁/Λ contains an on-line zero γ with |γ − γ*| ≥ c₂ δ (with c₁, c₂ absolute; c₂ ≈ 4 suffices in the deep regime).

There are two ways (★_loc) can fail:
(i) **empty cell**: no on-line zero within O(1/Λ). This is a large gap of length ≳ (const)·(mean spacing);
(ii) **clustering**: all on-line zeros of the cell lie within ≈ 2δ of γ*.

Counting cannot exclude either one. By Trudgian, N(t+h) − N(t) = (h/2π)Λ + O(|S|) with |S(t)| ≤ 0.112 log t + 0.278 log log t + 2.51 (PROVED-CITED). So in |x − γ*| ≤ 2δ the count is y/π + O(log γ*). Clustering of O(log γ/log log γ) zeros is not excluded. Gaps of length ≫ 1/Λ near a *given* point are not excluded either: unconditionally one only knows large gaps occur *somewhere* (Selberg and successors). Nothing is known at a prescribed point.

**Logical strength.** RH ⇒ (P_gap) vacuously, so (P_gap) is no stronger than RH. But (P_gap) is a statement about zeros in an O(1/Λ) neighbourhood of a *hypothetical* off-line zero. Every unconditional local tool (argument principle, Jensen, S(t) bounds, Selberg's moments of S) is blind to the on/off-line distinction at scale δ ≪ 1/Λ·O(1). The reason: these tools control counts in rectangles of width ≳ 1/log γ in σ, and the quartet lies inside such a rectangle. Combined with §3 and the rest of the R167 chain, (P_gap) would exclude every quartet with y < y₀. That is a "zero-free strip near the critical line" of width y₀/log γ, of a kind no known method produces (zero-free regions live near σ = 1). Status: **OPEN, and as hard as an anti-concentration theorem for zeros at the line, which is not known in any form.** It is not shown equivalent to RH.

Pair-correlation (Montgomery, under RH) is unusable: it is conditional on RH and statistical, not pointwise.

## 5. Falsifier M_m

M_m keeps ζ's on-line zeros and inserts a quartet at an arbitrary (γ, δ). It can put the quartet into a large gap, giving failure (i), or next to an existing tight pair, giving failure (ii). Sufficiently tight pairs/gaps occur among ζ's actual zeros (numerically, and Lehmer pairs exist). So M_m violates (P_gap) at will, while all inputs of R167 (Lemma O, Det±, the S(t) bound away from the insertion) remain available to it up to O(1) changes in S near the insertion. Therefore **any proof in this regime must use a property of ζ's on-line zeros near γ* that ties them to the off-line zero.** No such property is known; the only ζ-specific link (Euler product ⇒ zero-free region) acts near σ = 1 and gives nothing at small δ (§1). Wall confirmed.

## 6. Ledger

| item | label |
|---|---|
| draft claim "zero-free regions empty small-y" | **WITHDRAWN** (direction error) |
| γ* ≤ 3·10¹² empty | PROVED-CITED (Platt–Trudgian) |
| Lemma 2 (negative quartet ⇒ node within r of γ*, explicit remainder ε(τδ)) | PROVED |
| Rem 2a: τδ ≈ y/2, so pinning is O(δ) only for y ≪ 1, and O(1/Λ) near y₀ | ARGUED (model T_L) |
| (★_loc) sufficient for local (★_cell); in the deep regime it is "one on-line zero at distance ≥ 1.9δ in the cell" | PROVED (sufficiency) |
| counting does not exclude clustering or empty cells | PROVED-CITED (Trudgian S(t)) |
| (P_gap) | OPEN; implied by RH; not known to imply RH alone |
| M_m violates (P_gap) freely | PROVED (construction) |
| (★_cell) in the small-y regime | **OPEN**, unchanged |

## 7. Wall

The small-y regime does not open up from the on-line side. The witness's sign at the quartet is decided at the O(1/Λ) scale of single zero spacings, where unconditional theory knows only counts with O(log t) error. The needed statement (P_gap) is a pointwise anti-clustering/anti-gap property **around a hypothetical off-line zero**. The falsifier M_m violates it by free insertion, and no ζ-specific mechanism near σ = ½ is known. O167.101.2 stays OPEN with a sharper statement: O167.101.2 ⟸ (P_gap) + R167 chain.

Residue: **O168.103.1** — find any ζ-specific coupling between an off-line zero and its on-line neighbours at scale 1/log γ (e.g. via the Hadamard-product effect on ξ′/ξ near γ*, i.e. how an off-line pair shifts the on-line zeros nearby). This is the only route not falsified by M_m, since M_m's insertion does not move the neighbours.
