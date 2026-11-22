# R186_045 — Synthesis after round 20: what global object in T, computable from σ = (m, Λ|𝒩_T) and not from h*, can carry the sign?

Phase 186, decision round (not a construction round). Labels
PROVED / CITED / CONDITIONAL / OPEN / NO-GO / NUMERICAL (+ ARGUED). Paper 46, the grid and the crossword are not touched.
Read: README rounds 14–20; R186_042/043/044, audits 114/115; R186_004 (Kreĭn flow), R186_028, R186_034 (Thm 3.1,
W-det), R186_036 (Lemma 2, Theorem 3), R186_032 (Ω); grid log 25–34 and §3; R185_005B; phase-187 PATTERN_REPORT and
CONSTRAINTS (1.11–1.12, 2.1–2.5, 3.1); R183_031 (Thm 1 and prolate NO-GO); R183_016; R183_018 Thm 5.1; R185_001; Paper 46
lem:roughEF, prop:negtrace, lem:monoT, lem:contA. Script: `r045_moments.py` (self-contained on top of `r034_det.py`; 1 min).

## 0. Verdict in five lines

1. **(a) Flow in β/T: NO-GO as a shortcut.** Every closed equation for β*(T) (or for λ_A(T)) has as its coefficient the
 boundary value of the resolvent kernel, which is Σ_j φ_j(T)²/μ_j, dominated by h*(T)²/λ_A: Hadamard/Kreĭn hand back h*. Determining the
 chain in T from σ is Kreĭn's inverse problem: it amounts to solving every window. (§1)
2. **(b) Tension T → ∞: it is not a tension, it is lem:roughEF.** The limit of W_T on a fixed F is exact and does not depend on T
 (R186_004 Cor 1.2); the "limit symbol" is not a function but the zero measure. The property X that forces truncated positivity
 ∀T from σ is exactly R183_031 Thm 1 + (N′): gap density → 0 at rate πN₀/T, i.e.
 one-sided inequalities on Λ beyond the window at the frequencies of U_{T₀}. X cannot be proved from (m, Λ)
 without the zero side (W-sieve, (N′), R183_031 prolate NO-GO). Theorem X written in §2 (PROVED mod. CITED). (§2)
3. **(c) Pencil moments: exact criterion, inherited margin; NO-GO as a route, decisive NUMERICAL.** m_k = Tr(B^k) is
 σ-computable and β_max ≤ m_k^{1/k} is exact, but k* = min{k : m_k < 1} = 20, 10⁵, 10¹⁰ (½log3, log 2, ½log5) and at k* the
 margin 1 − m_k^{1/k} = 1 − β_max to every digit. For k ≤ 6, m_k^{1/k} ∈ [1.06, 6.7]. Chebyshev–Markov/Samuelson do not
 improve on m_2^{1/2} (unit weights, n → ∞). **Lemma T (PROVED):** every universal order-k moment criterion has
 margin ≤ k(1 − β_max) = kλ_A/Pos(h*). This is R186_034's generating function D_B(s) = exp(−Σ s^k m_k/k): Thm 3.1 already covered it. (§3)
4. **(d) Other global objects:** the determinant D_B (= (c)), the Szegő/Fisher–Hartwig coefficients (W-det), the
 λ_A(T′) laws (W-fam), the window observables (W-pat), the nodal measure (R186_113: = lem:roughEF). There is no global
 object in the corpus, not yet attacked, that is σ-computable and has its own margin. (§4)
5. **Honest answer to the single question: none with a margin.** Candidate theorem (§5, Lemma T + Lemma T′): *every
 continuous functional of the form 𝔞_T|𝒫_T — in particular every function of a finite number of traces — that decides the sign for all
 symbols of the class has margin ≤ L·λ_A*, with L its Lipschitz constant. The sign is indeed a function of the moments
 (D_B), but without margin: the only σ-computable object carrying the sign is the entire form. **Round 21 recommendation: a
 single front, (L-W) from R186_044 §5(iv) (coercivity of the prolate complement), which is constructive, is not inherited, and makes
 PROVED the reduction "D per window ⟺ ρ_T < 1 in dim 2·#comp"; reserve: Theorem X (§2) written as a tail lemma of
 Λ at the frequencies of U_{T₀}, to quantify (N′) per window.** Contact with the sign: none.

## 1. (a) The flow in β and in T

**1.1 What is already PROVED.** λ_A(T) is non-increasing and continuous (lem:monoT, lem:contA; R186_004 Prop 2.1): the flow runs in the
bad direction, and "the system does not blow up on (T₀, T₁]" ⟺ λ_A(T₁) > 0 (R186_004 §2: no Grönwall adds information). The
primes enter as boundary atoms of the Kreĭn datum k|_{(−2T,2T)}, with no jump (𝒥_n = id, R186_004 Lemma 1.1); the fold
at ½log n is −2v_n h*(T)h*(−T) (R186_036 Lemma 2, CONDITIONAL (REG); CONSTRAINTS 1.11–1.12), a functional of h*.
β*(T) := β_max(T) = 1 − λ_A/Pos(h*) (R186_042 Thm 2.1) inherits the same dependence.

**1.2 A closed equation for β*(T) without h*?** The only closed equation in T for Wiener–Hopf truncations is Kreĭn's trace
formula (CITED; Kreĭn 1955, Gohberg–Kreĭn ch. IV; Dyson form for convolution kernels):
 d/dT log det(W_T(σ)) = 2·Γ_T(T, T),
with Γ_T the resolvent kernel of W_T at the vertex (in Galerkin: ∂_T log det = Tr(W_T⁻¹ ∂_T W_T)). Since
Γ_T(T,T) = Σ_j φ_j(T)²/μ_j (φ_j eigenfunctions, μ_j eigenvalues), near contact the j = 1 term is h*(T)²/λ_A, and the
"closed equation" is Hadamard's rewritten: **it hands back h*, it does not avoid it**. With Tate (codimension 2) the de Branges
chain carries two prescribed zeros at ±i/2 (R186_004 §1, CONDITIONAL) and the formula also carries the Lagrange multipliers.
**Lemma 1.1 (PROVED, elementary).** If D(T) := det(𝔞_T|𝒫_T) (Galerkin) and λ_A(T) > 0, then −d/dT log D(T) =
Σ_j 𝒱_T(φ_j)/(Tμ_j) with 𝒱_T the form of CONSTRAINTS 1.11; the j = 1 term equals 𝒱_T(h*)/(Tλ_A) and dominates at contact.
*Proof.* Hellmann–Feynman per eigenvalue + logarithm of the product. ∎
**1.3 The global alternative:** write the chain's canonical system JY′ = zH(T)Y (G2_B5_R1, CITED de Branges) with H
determined by σ. Determining H from the symbol is Kreĭn's inverse spectral problem: its solution **is** the resolved family
{W_T}_T (Gelfand–Levitan–Kreĭn: H is obtained from the resolvents at the vertex). There is no equation for β*(T) that
avoids the chain's data, and those data are the h*_T. **NO-GO as a route** (label: exact reformulation with no margin;
falls under W-lin(b)/W-det for the same reason: boundary term = functional of the minimizer). Cross-check: R186_004 (Hadamard OPEN),
R186_036 Lemma 2, R165_202 §1.4, CONSTRAINTS 1.11; nothing new to prove.

## 2. (b) The limit T → ∞ as a theorem

**2.1 Correcting the premise.** "W_∞(σ_β) is pure convolution with spectrum = range of σ_β, negative ∀β" assumes σ_T converges
to a function. It does not: Σ_n v_n cos(τ log n) with v_n = 2Λ(n)/√n diverges (Σ Λ(n)/√n = ∞). Instead, for fixed F with compact support,
W_T(F) is **constant** in T once 2T ≥ |supp c_F| (R186_004 Cor 1.2) and equals Σ_ρ Φ_F(ρ)Φ_F(1−ρ) (lem:roughEF, PROVED): the
"limit symbol" is the zero measure, not a function. Truncated positivity ∀T is in tension with nothing: it is the positivity
of that measure on |F̂|² for every F of compact support. And β*(T) ↑ 1 (Thm M, CONSTRAINTS 1.6): the crossing approaches 1 without crossing it.

**2.2 Theorem X (PROVED mod. CITED).** Let T₀ be fixed, U₀ := {σ_{T₀} < 0} (finite union of intervals, prop:band) and, for T > T₀,
𝔞_T = W_T(σ_{T₀}) + Δ_{T₀,T}, with Δ_{T₀,T}(F) = −Σ_{e^{2T₀} ≤ n < e^{2T}} v_n c_F(log n) (R186_004 Cor 1.2: exact identity).
(i) (CITED Landau–Widom; R183_018 Thm 5.1 for the Sonin analogue) n₋(W_T(σ_{T₀})|𝒫_T) = (T/π)|U₀| + O(log T).
(ii) If λ_A(T) ≥ 0 ∀T, then for every T > T₀ the form Δ_{T₀,T} is ≥ 0 on a subspace of 𝒫_T of dimension
≥ (T/π)|U₀| − O(log T) − 0 (interlacing: n₋(𝔞_T) = 0 ⇒ n₋(Δ) ≥ … by Weyl on the negative subspace of W_T(σ_{T₀}));
more precisely, on the negative subspace E₋ of W_T(σ_{T₀}): Δ_{T₀,T}(F) ≥ −W_T(σ_{T₀})(F) > 0 for F ∈ E₋ ∖ 0.
(iii) E₋ is made of frequency packets concentrated on U₀ (window-T prolates), so (ii) says: **the sums
Σ_{e^{2T₀}≤n<e^{2T}} v_n cos(τ log n), averaged at resolution π/T for each τ ∈ U₀, are ≤ −σ_{T₀}(τ)·(1 + o(1)) < 0**, i.e.
Λ beyond the window must cancel σ_{T₀} on U₀ with the exact sign and magnitude (quantitatively: the σ₋ mass on U₀, which is
Tr(Neg_{T₀})·π/T₀ by prop:negtrace, R186_112 §2.3).
*Proof.* (i) is the Landau–Widom law for piecewise symbols with negative set U₀ (CITED; Tate costs ≤ 2 directions).
(ii) is min–max. (iii) is the spectral description of E₋ (Slepian; CITED) and the identity Δ = (1/2π)∫(σ_T − σ_{T₀})|F̂|². ∎
**2.3 X as a property of (m, Λ).** X = "spectral density of σ_T → 0 in the gap and on every compact away from the zeros": it is
R183_031 Thm 1 (PROVED under bounded inertia, with N₀′ counting zeros off the line) and the per-frequency form of (N′)
(R166_802). **Is it provable directly from (m, Λ)?** Not with the corpus's tools: R183_031 §0 (prolate NO-GO: the
only source that distinguishes bands is the prime part of σ, whose window-resolution smoothing is the sum over zeros);
W-sieve (R167_102): positivity + support + upper bounds never go one-sidedly below ½; (N′) demands the exact strength of
the zero's absence at each frequency of U₀. The "strongest and verifiable" thing X admits: (iii) is quantitative and per-window;
its verification for T ≤ ½log5 is NUMERICAL and is the same as n₋ = 0 (adds nothing). **Theorem X: PROVED as a reformulation; X as
input from σ: OPEN (= S2 of Ω, R186_032 §4; blank box, confirmed).** Falsifier: M₁ satisfies X below its
contact and violates it afterward (its Λ_{M₁} carries the quartet); f_t agrees with ζ up to ½log λ₁: X per window is class-blind.

## 3. (c) Pencil moments: evaluation with a number

**3.1 Objects.** B := Pos_T^{−1/2} Neg_T Pos_T^{−1/2}|𝒫_T ≥ 0, trace class (Neg_T trace, prop:negtrace; Pos_T ≥ c_P > 0, R186_034);
β_j = spec B; m_k := Tr(B^k) = Σ_j β_j^k. m_1 = Tr(Pos⁻¹Neg) requires the inverse of Pos_T (Wiener–Hopf factorization of σ₊:
σ-computable, CITED Kreĭn/Gohberg), not the extremal problem: **the moments are global objects of σ**, as requested.
Tr(Neg_T) = (2T/2π)∫σ₋ (exact; r034: 0.5034 on 𝒫_T at ½log3, 3.0016 at ½log5 includes the Tate cutoff).
**3.2 Moment criterion (PROVED, elementary).** β_max ≤ m_k^{1/k} ∀k, with m_k^{1/k} ↓ β_max; and β_max < 1 ⟺ ∃k: m_k < 1 (B trace:
Σβ_j^k → 0 if β_max < 1). Every "Chebyshev–Markov-type" bound for the maximum of a distribution with unit weights on [0, β_max]
and n atoms reduces to m_k^{1/k} as n → ∞ (Samuelson: m_1/n + √((n−1)/n·(m_2 − m_1²/n)) → m_2^{1/2}); with weights ≥ 1 no
bound from m_1..m_k goes below m_k^{1/k} (a single atom β = m_k^{1/k} is admissible). **Corpus cross-check:** never attempted as
such (grep "momento|moment|Tr(|traza": R183_013/016 compare traces of other operators; R185_001 zero "moments"); but
D_B(s) = det(1 − sB) = exp(−Σ_k s^k m_k/k) is the generating function of the m_k, and **R186_034 Thm 3.1 (inheritance of every
continuous determinantal functional) already covers it**: the moment criterion is W-det as a power series.
**3.3 Numbers (r045_moments.py, M = 40, Galerkin–Legendre, same constructions as r034/r044; NUMERICAL).**

| T | #comp | λ_A | 1−β_max | next β_j | m_1 … m_6 | m_6^{1/6} | k* = min{k: m_k<1} | 1−m_{k*}^{1/k*} |
|---|---|---|---|---|---|---|---|---|
| ½log3 | 2 | 9.49e-4 | 4.23e-3 | 0.875, 0.032, 0.003 | 1.906, 1.758, 1.657, 1.569, 1.492, 1.423 | 1.061 | 20 | 6.2e-4 |
| log 2 | 6 | 1.04e-7 | 4.23e-7 | 1−4.6e-5, 0.9936, 0.854 | 4.541, 3.848, 3.638, 3.517, 3.426, 3.351 | 1.223 | 10⁵ | 3.2e-7 |
| ½log5 | 8 | 3.86e-12 | 1.72e-11 | 1−3.8e-9, 1−1e-6, 0.99991, 0.9949 | 6.718, 5.866, 5.623, 5.498, 5.408, 5.335 | 1.322 | 10¹⁰ | 1.72e-11 |

Reading: (i) with k ≤ 6 the bound is > 1 by a factor of 1.06–6.7: **it does not bound β_max < 1**; (ii) k* grows like
ln(K_δ)/(1 − β_2) with β_2 the second crossing (odd sector: 1 − β_2 = λ_A(od)/Pos, CONSTRAINTS 1.13), i.e. k* ≈ #comp is false
by 1–9 orders of magnitude: the number of nearly balanced crossings is K_δ = N(T*) ± 1 (CONSTRAINTS 2.1), not #comp, and all of them sit at
10⁻⁵…10⁻⁹ from 1; (iii) at k* the margin is exactly 1 − β_max = λ_A/Pos(h*): **it fully inherits** (and requires evaluating m_{k*} to
precision k*(1 − β_max), which is ≈ 10⁻¹ relative at ½log5 only because k* ≈ 1/(1−β_max)).
**3.4 Lemma T (PROVED).** Let Φ(m_1,…,m_k) be a universal criterion (Φ < 1 ⇒ β_max < 1 for every trace-class B ≥ 0). Then, for
every B with β_max < 1, the point m(B) is at most (k(1−β_max))·(1+o(1)) from the set {m(B′) : β_max(B′) ≥ 1} in each
coordinate. *Proof.* B′ := B + (1 − β_max)vv^T with v the eigenvector of β_max: β_max(B′) = 1 and |m_j(B′) − m_j(B)| =
|1 − β_max^j| ≤ j(1 − β_max). ∎ (Verified in the script: 4.23e-3·j, 4.23e-7·j, 1.72e-11·j.) Consequence: no
continuous function of a finite number of moments decides the sign with margin larger than (Lipschitz constant)·k·λ_A/Pos(h*).
**Lemma T′ (PROVED, same proof).** The same for any continuous functional of the form 𝔞_T|𝒫_T (not only traces): the
perturbation 𝔞_T − λ_A·⟨·,h*⟩h* is admissible as a form and has zero sign. It is W-lin(b) in one line.
**Honest caveat.** Lemma T/T′ speak of **universal** criteria (valid for every form). A criterion valid only within the
class of symbols (m, Λ) with Λ ≥ 0 on log ℕ is not excluded by them: the perturbation B′ does not in general come from an
admissible symbol, and M₁ (admissible) is O(1) from ζ in form norm (positive part 4|Φ_c|², R186_044 §4.3: ‖ΔA_VW‖ = 0.70 at
δ = 0.01). But a class criterion falls under W3/W3′/W-identification (grid §3) and, by R186_044 §4.3(d), in the blind regime the
ζ/M₁ difference is λ_A(ζ) < 4δ²|ĥ*′(γ₁)|²: the family δ ↦ M₁(δ) crosses the sign at δ_A with a form derivative of 8δ_A|Φ_s|² = O(δ_A),
so a continuous class criterion has margin ≤ L·O(δ_A·ε) at M₁(δ_A) and at ζ whatever margin its constant gives it: there is no
contradiction, but no object either: **no class criterion is formulated in the corpus** (Ω S4, blank).
**Falsifier:** the criterion m_k < 1 is exact: it passes M₁(δ < δ_A) and fails M₁(δ > δ_A) only if evaluated at precision λ_A —
it satisfies the requirement by inheritance, not by structure. **Verdict (c): NO-GO as a route; PROVED as a reformulation
(D_B series); NUMERICAL: k* = 20 / 10⁵ / 10¹⁰.**

## 4. (d) Other σ-computable global objects

| object | σ-computable | own margin | closure |
|---|---|---|---|
| D_B(s), det(𝔞|𝒫)/det(Pos|𝒫), Szegő/Kac–Akhiezer/Fisher–Hartwig coefficients | yes | no: the leading term does not decide; the sign lives in the prolate overlap (plunge) | R186_034 Thm 3.1/§4, W-det; R186_042 (no plateau) |
| det(1 + Neg_T) and its asymptotics | yes | blind to the sign (bulk) | R186_034 Thm 4.1 |
| functionals of the family {λ_A(T′)} (L, derivatives, laws) | no (λ_A) | — | R186_036 Thm 3, W-fam (CONDITIONAL on f_t) |
| window observables (K_δ, staircase, peak, parity) | yes | shared with M₁ | phase-187, W-pat |
| nodal measure μ_X / Gauss quadrature | no (ĥ* nodes) | = lem:roughEF | R186_041/113 |
| PNT-window identity, cone (★₃₃) | yes | c/λ_A ≈ 10³ constant | R186_033/035 |
| inertia/index (n₋(𝔞|L²) = 1, polar capacities 𝔤_par) | yes | 𝔤_ev ≍ λ_W‖h_ev‖²: inherits | R186_028 Prop 3.1 |
| prolate block H_T, ρ_T (Schur) | H_T yes; ρ_T no | λ_min(H_T) blind at scale δ_A < δ < δ_V; 1−ρ_T inherits | R186_044 Thm 2, W-loc |
| pencil moments m_k, Lemma T | yes | ≤ kλ_A/Pos(h*) | §3 (new, closes the box) |

No box in grid §6 ("never attempted") names a σ-computable global object with a margin that is not in this table.
**Conclusion (d):** the corpus points to none; the table is complete with respect to phases 183–187.

## 5. Candidate theorem and recommendation

**Candidate theorem ("the sign is not a function of any finite number of traces with a margin").** *For every k and every
universal criterion Φ of the moments m_1,…,m_k of B (or, by Lemma T′, every continuous functional of 𝔞_T|𝒫_T), Φ's margin on ζ is
≤ L_Φ·k·λ_A(T)/Pos(h*_T). The sign is a function of the moments (D_B(s) ≠ 0 on [0,1]) but only to precision λ_A.* PROVED (Lemmas
T, T′; one line each). Sticking point for the strong version (class criteria): the corpus has no admissible family
of symbols connecting ζ to a negative one at distance O(λ_A) in form norm (M₁ is at O(1) because of its positive part); building
that family — or proving it does not exist in the class — is the only new content this question leaves, and it is a question of class
(W-identification), not of object. Not recommended as a front.

**Recommendation for round 21 (ONE front + reserve).**
- **Front: (L-W)** (R186_044 §5(iv)): λ_min(𝔞_T|W_T) ≥ c(T) > 0 with W_T = 𝒫_T ⊖ P_𝒫 span{component prolates}. First
 lemma (not numerical): *Lemma W1.* For F ∈ W_T, ‖1_{U_T}(D)R_T F‖² ≤ (1 − λ₀(S_{J_i}))·‖F‖² in each component (index-1 prolate
 instead of index-0: Landau–Pollak CITED), hence Neg_T(F) ≤ max_i σ₋|_{J_i}·Σ_i(1 − λ₀^{(i)})‖F‖² + cross leakage; coercivity
 follows if Pos_T(F) ≥ c_P‖F‖² (R186_034) exceeds that sum. It is the mechanics of R186_025 Lemma 2.1/Thm B with prolates instead of
 Tate exponentials; already favorable NUMERICAL (λ_min(A_WW) = 0.70–1.37). Result if it closes: PROVED reduction "D per window
 ⟺ ρ_T < 1 in dimension 2·#comp" with an explicit A_WW ≥ c; it does not touch the sign (ρ_T inherits), but leaves the problem in finite
 dimension with every block σ-computable except the Schur one. Falsifier: M₁(δ) shares W_T and A_WW (R186_044 table:
 λ_min(A_WW) = 1.63 for M₁): (L-W) must also hold for M₁ — and it does; the sign stays in ρ_T, as it should. Risk: the cross
 leakages Σ_{k≠i}⟨ψ_i, S_k ψ_j⟩ (R186_115 §2) are not Gershgorin; they must be bounded by the sinc overlap at scale 1/(T·dist).
- **Reserve: Theorem X (§2.2)** as a per-window lemma with constants: quantify, for T ≤ ½log5, how much of the σ₋ mass on
 U_{T₀} the new primes cancel (it is Ω's S2 written as an inequality on Λ at the frequencies of U_{T₀}, with the
 exact identity Δ_{T₀,T}). It does not carry the sign; it fixes the exact input (N′) demands per window. Only if (L-W) closes first.

**Contact with the sign: none** (everything PROVED here — Lemma 1.1, Theorem X, the moment criterion, Lemmas T/T′ — is
exact reformulation or inheritance). Row D: OPEN.

## 6. Audit notes
- Theorem X(i) uses Landau–Widom for a piecewise symbol with Tate: the O(log T) and the ≤ 2 loss from Tate are CITED/elementary;
 (iii) describes E₋ via Slepian prolates: concentration "on U₀" is at resolution π/T, not pointwise.
- Lemma T assumes B ≥ 0 trace class and v normalized; in Galerkin it is verified to 10⁻¹⁶. Lemma T′ does not claim B′ comes from an
 admissible symbol (caveat §3.4): it is not used to exclude class criteria.
- k* at log 2 and ½log5 is estimated with the Galerkin M = 40 β_j (clipped to [0,1]; β_j < 10⁻¹⁶ ignored): order of magnitude, not
 exact value; 1 − β_2 = 4.6e-5 (log 2) and 3.8e-9 (½log5) are the odd-sector crossings (R186_028 table: λ_A(od) = 1.1e-5, 6.4e-10).
- No equivalence with other statements is used; "zeros" appears only via lem:roughEF (identity) and R183_031 (CITED).
