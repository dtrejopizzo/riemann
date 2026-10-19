# R166_101 — Node-weight singularity: does the 1/δ² of an off-line pole beat the prime-side node weights?

Phase 166 (ω-closure). Inputs: R165_202 §3 (Cauchy identity 3.1, Lemma 3.5), R165_201 Thm 2 / Cor 2.2, R163_401 §2.4(iii)–(iv),
Lemma 3.1–3.3, §4.4; R163_801 Thm 5 (M_m). Corpus check: the conclusion below is anticipated, in heuristic form, by the
Remark after R163_401 §4.4 ("the node quadrature is blind to δ to first order"). This memo gives it as a theorem with
constants and identifies the exact step where the proposed chain fails.

## Status table

| # | statement | label |
|---|---|---|
| 1.1 | (Z) as a fixed-point system: arg g_q = Θ(X;t_q) = Σ_{x∈X} arctan(δ_q/(x−γ_q)) (mod π), X = real zeros of S_X | PROVED (restatement of R163_401 Lemma 3.3 + R165_202 Thm 3.1) |
| 1.2 | (Z) alone admits solutions with a negative quartet at a contact | PROVED-CITED (M_m, R163_801 Thm 5 + (3.1)); E1 |
| 2.1 | **No pole singularity at nodes.** For every node x₀ and every t = γ−iδ: \|G(t)/(t−x₀)\| ≤ e^{T\|δ\|}‖G′‖_∞ ≤ T e^{T\|δ\|}‖G‖_∞ | PROVED |
| 2.2 | Hence the quartet contribution to d_{x₀}=S′(x₀) is bounded uniformly in δ: \|2Re[g²/(t−x₀)²]\| ≤ 2T²e^{2Tδ}‖G‖²_∞ ≤ 4T³e^{2Tδ}‖F‖₂² | PROVED |
| 2.3 | Local form: quartet term at x₀ = 2G′(x₀)²Re(1+u)², \|u\| ≤ M₂r/(2\|G′(x₀)\|), r=\|t−x₀\|: same order as one on-line zero in the cell | PROVED (= R163_401 §4.4) |
| 2.4 | The proposed lower bound "d_x ≳ \|g\|²/δ²" is FALSE at every node; the 1/δ² of Lemma 3.5 is attained only at ξ=γ_q, and if ξ=γ_q is a node then \|g\|² = δ²G′(γ_q)²(1+O(δ)) | PROVED |
| 2.5 | The LP lower bound \|g\| ≥ \|G(γ_q)\| holds, but \|G(γ_q)\| ≤ ‖G′‖_∞ dist(γ_q,X); the anomaly \|G(γ_q)\|²/δ² is large only if dist(γ_q,X) ≫ δ, and then no node sees 1/δ² | PROVED |
| 2.6 | Failing step of the mechanism is on the ZERO side (E1); the prime-side/atomic separator (β_m of M_m) is never reached | PROVED |
| (★_cell), row D | | OPEN (unchanged) |

## §1 The zero-side system (Z)

Notation as in R165_202 §3: F a real, parity-definite, real-rooted witness at T = T_c, G = F̂ or −iF̂ (real, Laguerre–Pólya:
Lemma 3.1(a) of R163_401 gives G = c z^m Π(1−z²/x²), genus ≤ 1, real zeros), X its nodes,
S(z) = Σ_ρ G(t_ρ)²/(t_ρ−z) (λ = 0), S(x) = 0, S′(x) = d_x ≥ 0 on X.

**1.1 (fixed-point form). PROVED.** By R163_401 Lemma 3.3, arg g_q ≡ Θ(X;t_q) := Σ_x arctan(δ_q/(x−γ_q)) (mod π). The
node x₀ nearest γ_q contributes arctan(δ_q/(x₀−γ_q)), which is the "ω-term": writing x₀−γ_q = (ω − ½)·ℓ_cell up to the
cell normalisation of R165_201, its contribution is the explicit function π/2 − arctan((x₀−γ_q)/δ_q); all other nodes give
Φ_Z + Ψ_out (R165_201 Cor 2.2). Since X is the zero set of S_X and S_X depends on g_q only through g_q² (and g_q through X),
(Z) is the fixed-point system X = Z(S_X), arg g_q = Θ(X;t_q). Nothing more explicit than this is claimed: ω(g,Γ_loc) is
defined implicitly by S_X(x₀) = 0, i.e. S_on(x₀) = −S_off(x₀); solving for x₀ near γ_q requires S_on′ ≫ |S_off′| on the cell
(R165_202 Thm 3.3), which is exactly what fails in the δ-core (Lemma 3.5). So "ω = ω(g,Γ_loc) explicitly" is OPEN in general and
not needed below.

**1.2 (no obstruction from (Z) alone). PROVED-CITED, E1.** M_m has ζ's zero set and a first contact (R163_801 Thm 5). Its
witness satisfies (Z) verbatim (R165_202 §4.2). By (3.1) of R163_401, P_+ + 4Σ_q Re g_q² = 0, so either P_+ > 0 and some
quartet is negative, or P_+ = 0 and Σ_q Re g_q² = 0 (some quartet ≤ 0). Hence (Z) has a solution with a non-positive
quartet; no closure can come from (Z) alone. (This is the expected answer.)

## §2 The coupling S′(x) = d_x and the size of the quartet term

**Theorem 2.1 (no pole singularity at nodes). PROVED.** Let x₀ ∈ X and t ∈ ℂ, |Im t| = δ. Then
  |G(t)/(t − x₀)| ≤ e^{Tδ} ‖G′‖_{L^∞(ℝ)} ≤ T e^{Tδ} ‖G‖_{L^∞(ℝ)},  ‖G‖_∞ ≤ ‖F‖_{L¹} ≤ (2T)^{1/2}‖F‖₂.
*Proof.* Q(z) := G(z)/(z−x₀) is entire (G(x₀) = 0) of exponential type ≤ T. On ℝ, by the mean value theorem,
|Q(u)| = |G(u)−G(x₀)|/|u−x₀| ≤ ‖G′‖_∞, so Q is bounded on ℝ. Phragmén–Lindelöf in each half-plane (Levin, Lecture 6;
CITED) gives |Q(u+iy)| ≤ ‖Q‖_{L^∞(ℝ)} e^{T|y|}. Bernstein's inequality for bounded functions of type T: ‖G′‖_∞ ≤ T‖G‖_∞
(CITED). Finally |F̂(u)| ≤ ‖F‖₁ and Cauchy–Schwarz on [−T,T]. ∎

**Corollary 2.2. PROVED.** The quartet's terms in d_{x₀} = S′(x₀) = Σ_ρ g_ρ²/(t_ρ−x₀)² satisfy
  |2Re[g_q²/(t_q−x₀)²]| ≤ 2|Q(t_q)|² ≤ 2T²e^{2Tδ_q}‖G‖²_∞ ≤ 4T³e^{2Tδ_q}‖F‖₂²,
uniformly in δ_q ∈ (0,½). (The partners −t_q, −t̄_q give the same bound at −x₀; they are at distance ≥ 2γ_q from x₀.)
So the off-line pole produces **no** δ-singularity in any node weight. ∎

**2.3 (local form). PROVED** (R163_401 §4.4, re-derived from 2.1). With r = |t_q−x₀|, Taylor at x₀:
g_q/(t_q−x₀) = G′(x₀)(1+u), |u| ≤ M₂r/(2|G′(x₀)|), M₂ ≤ T²e^{Tr}‖G‖_∞. So the quartet term equals 2G′(x₀)²Re(1+u)²,
and in w_{x₀} = d_{x₀}/G′(x₀)² it contributes 2Re(1+u)² ∈ [2(1−|u|)²−4|u|², 2(1+|u|)²] — the weight of two on-line zeros
of the cell, independent of δ to first order.

**2.4 (the proposed lower bound is false). PROVED.** Lemma 3.5 of R165_202 is correct as stated: at ξ = γ_q the pair
contributes −2Re(g²)/δ² = +2|Re g²|/δ² for negative mass (sign checked: t−ξ = −iδ, (t−ξ)² = −δ², so 2Re[g²/(−δ²)]). But
S′ = d only at nodes. If γ_q ∈ X then g_q = G(γ_q−iδ) = −iδG′(γ_q)(1+O(M₂δ/|G′|)), so g_q² = −δ²G′(γ_q)²(1+O(δ)) (θ = π, the
lattice case R165_202 §4.1) and the term is 2|g|²/δ² = 2G′(γ_q)²(1+O(δ)) — bounded. If γ_q ∉ X, the nearest node is at
r ≥ dist(γ_q,X) and Cor 2.2 applies. In both cases d_x ≳ |g|²/δ² fails; the correct statement is d_x ≥ (quartet term)
≍ G′(x₀)².

**2.5 (the LP bound does not help). PROVED.** For G in the Laguerre–Pólya class, |G(γ−iδ)|² = G(γ)²Π_x(1+δ²/(x−γ)²) ≥ G(γ)²
(PROVED, from the product). But G(γ_q)² ≤ ‖G′‖²_∞ dist(γ_q,X)². The ratio G(γ_q)²/δ² is large only when dist(γ_q,X) ≫ δ,
i.e. only when no node lies in the δ-core, and then every node sees the pole at distance r ≫ δ, with term ≤ 2|Q(t_q)|²
(Cor 2.2). The "anomalous d_x ≳ |F̂′(x)|²dist(x,γ*)²/δ²" asked for in the task is therefore false: the exact value is
|F̂′(x)|²·|1+u|²·(dist² + δ²)/(dist² + δ²) = |F̂′(x)|²|1+u|², because |g|² ≈ G′(x)²(dist² + δ²), not G′²dist².

**2.6 (where the chain stops). PROVED.** The intended chain was
  (P) d_x ≤ B(window, atomic Λ)   vs   (Z) d_x ≥ c|g|²/δ².
The second inequality is false (2.4–2.5), and its failure uses only Thm 3.1, Lemma 3.1(a) and Thm 2.1 — all zero-side,
E1 statements that hold equally for M_m and f_t. The witness *vanishes at the node adjacent to the pole*, and the factor
(t−x₀) in g cancels the Cauchy denominator exactly. Consequently the upper bound (P) is never tested: whatever B(window) is
(Chebyshev-type Σ_{n<e^{2T}}Λ(n)/√n ≍ e^{T}, or M_m's non-atomic β_m), both sides are O(T²e^{2Tδ}‖G‖²_∞), and the separator
"atomic vs β_m" is not reached. This is the node-level instance of R160_X_C1 Thm Q / W3 (Blaschke-blind forms) and of the
R163_401 §4.4 Remark, now with constants.

**What survives.** Only the *phase* of the quartet term (Re(1+u)², i.e. arg of the second-order Taylor correction u, which
carries δ through M₂r) is δ-sensitive; its size is O(M₂r/|G′|) relative to the main term. Any coupling of (P) and (Z)
must therefore be a second-order (curvature) statement, not a singularity statement. OPEN, no candidate inequality.

## Ledger

- PROVED: 1.1 (fixed-point restatement), 2.1 (no pole singularity, constants), 2.2, 2.4 (sign check of Lemma 3.5 and its
  correct node value), 2.5 (LP bound collapses), 2.6 (failing step identified).
- PROVED-CITED: 1.2 (M_m solves (Z) with a non-positive quartet), Phragmén–Lindelöf, Bernstein.
- OPEN: explicit ω(g,Γ_loc) inside the δ-core; second-order coupling (P)↔(Z); (★_cell); row D.
- Mechanism "1/δ² Cauchy singularity vs bounded prime-side node weights": **DEAD**, killer E1 (zero-side cancellation
  g = (t−x₀)G′(x₀)(1+u)); it dies before any prime-side input is used.

## Grid cells

- **7A** (zero side × one window): +PROVED-TOOL 2.1–2.5. Route "off-line pole forces anomalous node weight": DEAD [E1].
- **2A** (prime side × one window, node identity 2.4(iv)): no new bound needed; the atomic bound B(window) is never
  engaged, since the zero-side lower bound is O(1). Mark: UNTESTED-BY-THIS-ROUTE, no change.
- **6A** (coupling / Problem A): +note: any (P)–(Z) coupling at nodes must be second order in the Taylor remainder u
  (δ enters only via M₂r/|G′|). OPEN.
