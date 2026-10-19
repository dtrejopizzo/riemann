# R168_203 — Local Laguerre inequality at a hypothetical quartet (residue O168.103.1)

*Phase 168. Inputs: R168_103 (Lemma 2, (★_loc), (P_gap), M_m), R168_190 (note: the mechanism must be non-linear in ξ′/ξ), R166_502 / E70_12 (Riccati = Selberg ⇒ E1).*
*Notation: Ξ(t) = ξ(½+it), real and even on ℝ, entire of order 1. Quartet ½ ± δ + iγ ⇒ zeros of Ξ at t = ±γ ± iδ. Λ = log(γ/2π), y = δΛ. Laguerre expression L(t) := Ξ′(t)² − Ξ(t)Ξ″(t).*

## 0. Status

**OPEN. No label change for (★_cell). The answer to the posed question is NEGATIVE.** In the small-y regime, "(★_cell) fails" and "local Laguerre failure near γ" are **not equivalent**. They are logically independent conditions on the on-line zeros near γ: (★_loc) asks for a zero **far** from the node (≥ 1.9δ, inside the cell), and local Laguerre positivity asks for a zero **near** γ (≤ 0.495δ, or a symmetric pair within δ). All four combinations occur in M_m-type configurations (§4). The sign of L at one height is the sign of a **linear** functional of the zero measure, −(log Ξ)″ = Σ_ρ 1/(t−t_ρ)². So the Riccati/Selberg non-linearity does not reach the sign, and the single-height wall (E1) stands (§5).

## 1. Corpus check (mandatory). What was tried with Laguerre and why it died

| source | content | outcome |
|---|---|---|
| `phase-28-four-fronts/07-lp-class-rh.md` Thm 1, Cor 1, Prop 3, Q28.2 | RH ⟺ Ξ ∈ LP (de Bruijn 1950). The "curvature criterion" RH ⟺ (log Ξ)″ < 0 off the zeros. The complex-pair term 2(b²−u²)/(u²+b²)² is computed, and Q28.2 asks whether (ξ′/ξ)′ > 0 on the line follows from the functional equation and the Euler product | **this is the global form of the present question.** Died as "Wall A": the Euler product is the only extra input, and none acts at σ = ½. NB: the converse half of Thm 1 is stated too fast. A positive pair term does not by itself make the total positive. §3 below shows that a single on-line zero can mask the pair, so the first Laguerre inequality alone is **not** equivalent to LP (Prop L4) |
| `phase-136 MAP_1` NG-B6, CIR-4 | Turán inequalities for ξ₀ as a constraint | CIRCULAR / EQUIVALENT-TO-RH: they are consequences of LP |
| `phase-136 MAP_1` LP-112 | sequential self-approximation of ζ on a fixed disc | OPEN, unrelated to Laguerre inequalities despite the name (Laguerre–Pólya rigidity) |
| `phase-138 CORPUS_CHECK_R138` §9 | LP / Jensen / Turán / Li / Keiper | "do not reopen as an unconditional sign route". Phase 103 (theta-kernel Jensen minors, ~40 no-gos) and phase 104 continued it without closing |
| `phase-101 E101_076` | jet Wronskian ⇒ "classical LP/Jensen criteria, therefore RH-equivalent" | restatement |
| `phase-103` / R160 survey | A1 reduced to one "Chebyshev–Laguerre inequality" (an explicit-formula area inequality, Laguerre kernel in the Fourier sense) | needs square-root cancellation of Σ e^{ρu}/ρ²: an E1-type wall |
| `phase-33/70`, `phase-36/107`, `phase-38/114,118`, `phase-64 FACE-C*`, `AUDIT-structure-function-death` | the "Wronskian" hits are orthogonal-polynomial or canonical-system Wronskians (det Y ≡ 1, F_n = −1/(a_n P_n P_{n+1} m)) | **not** the Laguerre expression of ξ. No relevant prior attempt |
| R166_502 / E70_12 | Riccati identity of V = Z⁻¹δZ = Selberg's identity Λ log + Λ*Λ = μ*log² | E1 ("no free lunch"), stated globally |

**Novelty of this memo**: the corpus had only the **global** criterion (phase 28) and its Fourier-side relatives. No prior document compares the **local** Laguerre expression at a quartet with the witness condition (★_loc), or computes the masking thresholds. Those comparisons are new here. Their outcome is negative.

## 2. Classical results. PROVED-CITED

- (C1) Ξ ∈ LP ⟺ RH (de Bruijn 1950; Pólya). For f ∈ LP, every Laguerre inequality holds: L₁(f) = f′² − ff″ ≥ 0 on ℝ, and more generally L_n(f)(x) = Σ_{k=0}^{2n} (−1)^{n+k} C(2n,k) f^{(k)}(x) f^{(2n−k)}(x) ≥ 0 (Jensen; Pólya–Schur).
- (C2) Converse with the **whole family**: for real entire f of genus ≤ 1 (in a suitable class containing Ξ), f ∈ LP ⟺ L_n(f)(x) ≥ 0 ∀n ≥ 1, ∀x ∈ ℝ (Csordas–Varga, Adv. Appl. Math. 11 (1990); Csordas–Vishnyakova 2013 for the generalized Laguerre inequalities; Dimitrov 1998 for higher-order Turán). *I am citing the exact hypotheses from memory and have not re-verified them here.* The first inequality alone does **not** suffice (Prop L4).
- (C3) Unconditional Laguerre/Turán facts for ξ live on the **Fourier side**: log-concavity of the kernel Φ, Turán inequalities for the Taylor coefficients (Csordas–Norfolk–Varga 1986), hyperbolicity of shifted Jensen polynomials for large shift (Griffin–Ono–Rolen–Zagier 2019). All of them are global/averaged statements at t ≈ 0 in Taylor variables, not at height γ. Λ_dBN ≥ 0 (Rodgers–Tao 2020). Lehmer pairs are near-violations of on-line stability (Csordas–Smith–Varga 1994).

## 3. Theorems

**Theorem L1 (exact local formula). PROVED.** With t_ρ := −i(ρ−½),
 L(t) = Ξ(t)² · Σ_ρ 1/(t − t_ρ)²  (t ∈ ℝ, Ξ(t) ≠ 0),
with an absolutely convergent sum and no exponential-factor term. For the quartet, with u = t − γ, the near pair contributes
 Q(u) = 2(u² − δ²)/(u² + δ²)²,
which is negative exactly for |u| < δ and has minimum −2/δ² at u = 0. The mirror pair at −γ contributes O(γ⁻²).
*Proof.* Ξ is even with Ξ(0) ≠ 0 and Σ|t_ρ|⁻² < ∞, so Ξ(t) = Ξ(0)Π_{pairs}(1 − t²/t_ρ²) is genus 0 in t². Then L/Ξ² = −(log Ξ)″, and the product is differentiated termwise. Finally Re[(u−iδ)⁻² + (u+iδ)⁻²] = 2(u²−δ²)/(u²+δ²)². ∎
So sign L(t) = sign of D(t) := Σ_on 1/(t−γ_j)² + Q(t−γ) + B(t), where B collects all other off-line pairs and the mirror. On-line terms are > 0. Each other pair contributes ≤ 1/|t−t_ρ|² (since Re z⁻² ≤ |z|⁻²).

**Prop L2 (empty neighbourhood ⇒ local Laguerre failure). PROVED (constants via Trudgian).** Let S* := 0.112 log γ + 0.278 log log γ + 2.51 (Trudgian's bound for |S|). Suppose no zero other than the quartet has |t_ρ − γ| ≤ h. Then
 D(γ) ≤ 2Λ/(πh) + (2S* + 1)/h² − 2/δ² + O(γ⁻²).
Hence L(γ) < 0 as soon as 2Λ/(πh) + (2S*+1)/h² < 2/δ².
*Proof.* Let n(x) := #{ρ ≠ quartet: |Re t_ρ − γ| ≤ x}. Riemann–von Mangoldt gives n(x) ≤ xΛ/π + 2S* + 1 for x ≤ γ/2, and the tail beyond γ/2 contributes O(1/γ). Partial summation: Σ_{|t_ρ−γ|>h} |t_ρ−γ|⁻² ≤ ∫_h^∞ 2n(x)x⁻³ dx ≤ 2Λ/(πh) + (2S*+1)/h². ∎
*Scale.* With S* ≈ 0.112Λ the condition holds for h ≳ 0.34·y·Λ^{−1/2} together with h ≳ (y²/π)/Λ. So an on-line-zero-free disc of radius ≫ max(δ√Λ, δy) around γ forces L(γ) < 0. The R168_103 empty-cell mode (i) (radius ≍ 1/Λ) satisfies this whenever y ≪ Λ^{−1/2}. In the rest of the small-y range it does so under the ARGUED model of local spacing (S of size O(1) locally), which reduces the condition to h ≥ c/Λ with y² < πc.

**Prop L3 (masking thresholds). PROVED** (zero background, δ = 1 after scaling). min_u [Σ_on (u−d_j)⁻² + Q(u)] ≥ 0 holds:
 (a) for one on-line zero at offset d, iff |d| ≤ d* ≈ 0.4947δ (numerical root, bisection on a fine grid). The case d = 0 is exact: u⁻² + Q(u) ≥ 0 ⟺ 1 + 3v⁴ ≥ 0 with v = u/δ.
 (b) for a symmetric pair at γ ± d, iff d ≤ δ exactly. At u = 0 we need 2/d² ≥ 2/δ². At d = δ the inequality for all u is (1+v²)³ ≥ (1−v²)³.
A positive background B only lowers the thresholds' necessity, which is to say masking becomes easier.

**Prop L4 (the first Laguerre inequality does not see a quartet). PROVED.** f(t) = (t² + δ²) sin(πt) is real and entire of order 1. It has non-real zeros ±iδ for every δ > 0, yet f′² − ff″ ≥ 0 on all of ℝ.
*Proof.* −(log f)″ = π²/sin²(πt) + Q(t). Since |sin πt| ≤ π|t|, we have π²/sin²(πt) ≥ t⁻², and t⁻² + Q(t) ≥ 0 by L3(a) with d = 0. ∎
The same masking works inside M_m: insert the quartet at the ordinate of an existing on-line zero of ζ. Then L ≥ 0 near γ, up to the background, which only helps.

## 4. Relation to (★_cell) in the small-y regime. Answer: NOT equivalent (PROVED at the level of configurations)

In the deep regime y ≪ 1, R168_103 gives: the node x₀ satisfies |x₀ − γ| ≤ 2δ(1+o(1)), and (★_loc) is satisfied by **one on-line zero at distance ≥ 1.9δ from x₀ inside the cell**. Local Laguerre positivity on |u| < δ (Prop L3, small background) needs a zero within ≈ 0.495δ of the minimiser, or a pair within δ, or k zeros with Σ d_j⁻² ≳ 2/δ². The four combinations, each realisable by M_m (free insertion next to ζ's zeros):

| configuration near γ | (★_loc) | local Laguerre |
|---|---|---|
| empty cell (mode (i)) | fails | **fails** (L2) |
| one zero at ≈ 3δ, cell otherwise empty | holds | fails (3δ > d*) |
| tight cluster within 0.4δ of γ, nothing else in cell (mode (ii)) | fails | **holds** (L3) |
| one zero at ≈ 0.3δ and one at ≈ 3δ | holds | holds |

Consequences:
- (★_cell)-failure in the small-y regime ⇏ local Laguerre failure, and the converse fails too. The conjectured equivalence is **false**. The overlap is exactly mode (i), the empty cell: there both fail, and M_m's quartet does carry a Laguerre failure (consistent).
- Mode (ii), clustering, is invisible to L₁. This is the Lehmer-pair phenomenon of (C3): a near-double on-line zero masks the quartet.
- So even a hypothetical proof of the local L₁ ≥ 0 near γ would exclude only mode (i). Mode (ii) would remain, and closing it needs higher L_n (C2) or (P_gap) itself. Note: L₁ ≥ 0 everywhere would not imply RH anyway (Prop L4), so it is strictly weaker than RH, and strictly weaker than what (★_cell) needs.

## 5. Euler-product input at one height. Wall (E1, single height). ARGUED, with PROVED components

- **Sign linearity (PROVED).** sign L(t) = sign Σ_ρ (t−t_ρ)⁻² (Theorem L1). The factor Ξ² ≥ 0 carries all the non-linearity and none of the sign. So the sign question is a linear functional of the zero measure: the second derivative of the explicit formula. That is E1, as R168_190's note predicted.
- **Riccati = Selberg (PROVED, classical).** Ξ″/Ξ = (Ξ′/Ξ)′ + (Ξ′/Ξ)². The Dirichlet coefficients satisfy (ζ″/ζ) − (ζ′/ζ)² = (ζ′/ζ)′, i.e. μ*log² − Λ*Λ = Λ·log (Selberg). L/Ξ² = −(Ξ′/Ξ)′ is the **difference** of the two non-linear terms, and that difference is linear again (Λ·log). So the local form inherits exactly the E70_12 verdict. Localising to one height does not help: localisation changes the test function, not the linearity.
- **Resolution count (ARGUED).** At height γ, D(t) is dominated (size ≍ Λ² to δ⁻²) by zeros within O(δ). Any Euler-product expression (approximate functional equation, mollified or smoothed prime sums of length X) reproduces the zero sum only at resolution 1/log X. Resolving scale δ needs log X ≳ δ⁻¹, i.e. X ≳ γ^{1/y}, far beyond the convergent or mean-value range. At that resolution the prime side *is* the zero side, through the explicit formula. Nothing sign-carrying survives at a single height, which is the same wall as R168_102 (U) and R168_101 (class DMV).
- **Falsifier.** Davenport–Heilbronn-type functions satisfy the functional equation, have off-line zeros, and obey every on-line-zero statistic used here. The Euler product is the only distinguishing input, and no known use of it acts at σ = ½ at resolution δ.

## 6. Ledger

| item | label |
|---|---|
| Corpus: global Laguerre/curvature criterion = phase 28 (Q28.2, Wall A); NG-B6/CIR-4; R138 §9 "do not reopen"; phase-33/36/38/64 "Wronskian" hits unrelated | checked |
| (C1) LP ⇒ all L_n ≥ 0; RH ⟺ Ξ ∈ LP | PROVED-CITED |
| (C2) LP ⟺ all L_n ≥ 0 (Csordas–Varga et al.) | PROVED-CITED (hypotheses quoted from memory) |
| Theorem L1 exact local formula, quartet term Q(u) | PROVED |
| Prop L2 empty disc of radius ≫ max(δ√Λ, δy) ⇒ L(γ) < 0 | PROVED |
| L2 at radius c/Λ (empty-cell mode (i)) for all y < √(πc) | ARGUED (local-spacing model) |
| Prop L3 masking thresholds 0.4947δ (single, numerical) / δ (symmetric pair, exact) | PROVED (L3(a) constant numerical) |
| Prop L4 first Laguerre inequality ≠ LP; (t²+δ²)sin πt | PROVED |
| phase-28-four-fronts Thm 1 converse ("pair positive ⇒ convex") | **incomplete as stated**; global RH ⟺ LP is still correct by (C1) |
| (★_cell)-small-y ⟺ local Laguerre failure | **FALSE** (independent; §4 table) |
| overlap = empty-cell mode (i); clustering mode (ii) invisible to L₁ | PROVED (configurations) |
| Euler-product control of local L at one height | none. sign linear ⇒ E1; Riccati = Selberg ⇒ E70_12 verdict; ARGUED resolution wall |
| (★_cell) | **OPEN**, unchanged |

## 7. Wall

The non-linearity in the Laguerre expression sits entirely in the factor Ξ² ≥ 0. Its sign is the linear zero sum Σ(t−t_ρ)⁻², and the Riccati route only re-derives Selberg's identity, whose sign-relevant part is linear (Λ·log). Locally, L₁ tests "is there an on-line zero **near** γ", while the witness needs "is there an on-line zero **far** from the node in the cell". The two coincide only on empty cells. O168.103.1 remains OPEN. The Laguerre/Wronskian sub-route is **closed negative**: it is not equivalent to the witness condition, it is blind to clustering, and it is E1 at a single height.
