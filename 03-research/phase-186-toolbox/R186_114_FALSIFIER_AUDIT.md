# R186_114 — Audit of the falsifiers M_m and f_t (and of their use as a closure criterion)

Phase 186, round 19. Audit. «also verify whether the falsifiers work
well; I don't want us to miss the solution because we blindly trusted something; re-verify everything».
Paper 46, grid and crossword are not touched. Minimal numerics (three control recomputations, session scratchpad).

Read line by line: grid §3–§4 and log 7–31; R163_801 §5–§7 (Thm 5, Prop 5.1); R162_2501 §1–§3 (model ξ_m, Prop 1, Thm 3);
R163_901 (status table, Prop 1.1–1.2, Lem 2.1, Thm F items 1–4 with proof, Cor F, §3); R163_991 §0, §3.3–3.5; R186_036
Theorem 3 + Cor 3.1–3.2; R186_110 §1.3; R186_111 §3.4; R186_039 §0–§1; R185_003 §0; R185_005 §1.3, §2.1, §3; R164_601 table
of falsifiers and Thm 3.1; R166_501 Thm A; R166_801 Thm 7C; R186_034 Thm 3.1; R186_026 Thm 3.3; R186_028 §0; R163_603 T5.2;
PATTERN_REPORT §3; CONSTRAINTS_FOR_PATTERN §3; `r187_mm.py` and `r187_campaign.py` (build_form, sigma, params, run_window);
`DATA_MM_FALSIFIER.csv`, `DATA_100_WINDOWS.csv`; `r043_wh.py` (header and block (6)); Paper 46 lem:roughEF, eq:Aform,
eq:Kprim, prop:weak; Paper 48 §falsifiers (l.436–447).

## 0. Verdict on one screen

| object | definition | real status | maximum defect | verdict |
|---|---|---|---|---|
| **M_m** (R163_801 Thm 5; R162_2501 §1) | ξ·∏R_j; window form 𝔞_T + ∫c_F β_m, β_m = Σ4cos(γ_ju)cosh(δ_ju) | PROVED as a form object (no Euler, no Dirichlet series); primitive witness PROVED (R162_2501 Prop 1, F ∈ 𝒫_T imposed); `r187_mm.py` correct (sign, factor 8 = 2·4, symmetry) | MINOR ×3 (two different definitions in the record; the "−Cδ²" reading from PATTERN_REPORT is incorrect; "reproduces ζ with δ→0" is false: the limit is ζ with a triple zero at γ₁) | **WORKS.** It only refutes *methods*; all the uses reviewed are of method |
| **f_t** (R163_901 Thm F) | ζ + t·g, g a general Dirichlet series over m/√M; exact EF of ζ; no Euler | Thm F.1–F.4 PROVED (mod. the explicit formula CITED). Coincidence with ζ **exact** for T ≤ T₁ = ½log λ₁. F.4 proves W ⋡ 0 on the **full L²(I_T)**, not on 𝒫_T. Primitive witness (λ_A^{f_t} < 0 for some T): **ARGUED** (R186_110 correct). Here: **CONDITIONAL** on (Z-strip) "all zeros of Λ_t in 0 < Re s < 1" (Lemma A, §2.4, new) — and F.4 allows zeros in σ > 1 | MAJOR ×1 (label of the closures that use the primitive witness) | **WORKS for the full Weil form; CONDITIONAL for the declared row D (𝒫_T).** Closures affected in §3.3 |
| DH, BFdisc, Λ̃, b_θ, ℕ∪√2ℕ, R=L(u,χ) | §4 | PROVED/CITED; none intervenes in the truncated Wiener–Hopf route (R186_042/043) | — | no objection |

**No FATAL finding.** No route from log 13–31 was closed *solely* by a falsifier without a transfer theorem; but four
closures cite the primitive witness of f_t as PROVED when it is ARGUED (§3.3) and move to CONDITIONAL. There is also a
systematic wording defect (statements vs. proofs, §1.2) already flagged by R186_110 and still present in the grid (entry 29),
in CONSTRAINTS §3.1 and in PATTERN_REPORT §3.4. **None of this reopens a route closed by proof of impossibility;
none of this closes a route that was open.** Row D: OPEN, unchanged.

---

## 1. M_m

### 1.1 (a) Is the perturbed form that of a function in the declared class? Own derivation

Paper 46 conventions: Φ_F(s) = ∫F(t)e^{(s−½)t}dt; c_F(u) = ∫F(t)F(t−u)dt (even for real F);
lem:roughEF: Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = 2Φ_F(0)Φ_F(1) + 𝔞_T(F), and on 𝒫_T the polar term vanishes.

*Quartet term.* For ρ = ½ + z, Φ_F(½+z)Φ_F(½−z) = ∫∫F(t)F(t′)e^{z(t−t′)}dt dt′ = ∫c_F(u)e^{zu}du.
The quartet {½ ± δ ± iγ} is z ∈ {δ+iγ, δ−iγ, −δ+iγ, −δ−iγ}; Σ e^{zu} = (e^{δu}+e^{−δu})(e^{iγu}+e^{−iγu}) = 4cos(γu)cosh(δu).
Each zero ρ of the quartet contributes Φ_F(ρ)Φ_F(1−ρ) once in the sum over zeros, and 1−ρ is also in the quartet, so the
quartet contributes exactly Σ_{z} ∫c_F e^{zu} = ∫c_F(u)·4cos(γu)cosh(δu)du. **Sign + and factor 4: correct** (matches
"4Re(AB)" from R162_2501 Prop 1 and R163_801 Thm 5(a)). For real even F, A = Φ_F(½+z) = Φ_F(½−z) = B and
Q(F) = 4Re(A²) = 4(a² − δ²b²) + O(δ⁴), a = ∫F cosh(δt)cos(γt) → F̂(γ), b = ∫F sinh(δt)sin(γt)/δ → ∫F·t·sin(γt). **This
fixes the mechanism of the negative sign: F̂(γ₁) ≈ 0 with ∫F t sin(γ₁t) ≠ 0** (a node of the minimizer at γ₁), and explains the
δ² scale observed (§1.3).

*What object is M_m.* There are **two definitions in the record**: (i) R163_801 Thm 5: M_m = ξ·∏R_j with R_j a "rational
factor of the quartet", but Q_m contains only the four added zeros: R_j acts as a **polynomial** of degree 4; (ii) R162_2501 §1:
ξ_m = ξ·∏(quartet)/∏(2m zeros on the line at height > H_PT), with Δ_T = Σ4Re(A_jB_j) − Σ2|Φ_F(½+iγ_k⁰)|². Both are
entire of order 1, real, with exact EF; **neither has an Euler product nor a Dirichlet series**: their "prime side"
is *by definition* the sum over zeros (lem:roughEF applied to the set of zeros). M_m is an object of **form**, not an
L-function: the class is "zero sets with a zero-side identity, integer multiplicities and EF". `r187_mm.py`
implements (i) (without the −2|Φ|² terms). Grid §4 cites (ii) ("R162_2501b") and Paper 48 l.436 says "rational factors". MINOR:
unify the definition (the (i) is the one executed; (ii) only changes κ and the extra negative weights, not the verdicts).

*Code verification.* `build_form`: A0 = ∫_0^{2T}(I − Cmat(u))K(u)du + (tail + C₀)I is the Lévy energy eq:Aform
with c_F(u) = c_F(−u); Pr −= Cmat(log n)·2log p/√n is −Σv_n c_F(log n) with v_n = 2Λ(n)/√n (sign − of eq:Aform ✓);
Cmat(u) integrates F(y)F(y−u) over y ∈ (u−T, T) with Legendre mirror φ_l(−y) = (−1)^l φ_l(y) ✓. M₁ patch:
Q += Cmat(u)·8cos(γ₁u)cosh(δu)·w over u ∈ (0,2T) = ∫_{−2T}^{2T}c_F·4cos cosh (even integrand) ✓ factor 8 correct;
symbol σ^M = σ_T + β̂ with closed form verified against quadrature (selfcheck reproduced: 0.362063523762). **Correct.**

### 1.2 (b) Is M_m a legitimate falsifier for row D on the declared carrier?

Row D is stated for **ζ alone**: λ_A(T) = min spec 𝔞_T|𝒫_T built with the Λ of ζ (eq:Aform). So neither M_m nor
f_t can refute *statements* about ζ; they can only refute *proof schemes* (transfer: "any deduction that uses of
ζ only properties shared with X holds for X, and X has λ_A < 0"). Under the project's premise (positivity is true),
"P(ζ) ⟹ D" is materially true for every true P: the sentence "P does not imply D because M_m/f_t satisfies P" only makes
sense as "there is no proof of D from P and from class properties".

Use-by-use review:

| use | wording | reading | verdict |
|---|---|---|---|
| R162_2501 Thm 3 | "If an argument proves 𝒫 ∧ κ<∞ ⟹ κ=0, then applied to M_m…" | about arguments | valid |
| R163_801 Thm 5(c), Prop 4.1 | "no identity or Gram-matrix property of §§1–4 can force (A-loc): it would force it for M_m" | about proofs | valid |
| R163_603 T5.2 | "no argument whose inputs are … excludes the witness" | about arguments | valid |
| R166_501 Thm A | "if H excludes f_t and M_m then H uses Λ beyond the window" | about classes of hypotheses | valid |
| R166_801 Thm 7C | "holds verbatim for M_m and f_t; no contradiction possible" | about identities | valid (see §3.3 for f_t) |
| R164_601 Thm 3.1 + table | "the inequality… is satisfied by M_m, so it cannot exclude a first contact" | consistency of a true inequality with a quartet | valid (does not say the inequality is false) |
| R184_015 Thm 2 (W11′) | "P invariant under X ↦ M_m (blind)" | about proofs | valid |
| R186_036 Theorem 3(a) | "no P ∈ 𝔉 valid for ζ **implies** λ_A ≥ 0 ∀T" | **about statements** | **invalid wording** (R186_110 MAJOR (i); correct as transfer) |
| grid entry 29 (W-fam) | "no functional of the family {λ_A(T′)} decides D" | ambiguous | audit 110's bracket bounds it; still needs rewriting as transfer |
| CONSTRAINTS §3.1 | "no statement P about {λ_A(T′)} valid for ζ implies λ_A(T) ≥ 0 ∀T" | about statements | same invalid wording; §3.2 already declares it a "wording defect" |
| PATTERN_REPORT §3.4 | "no law or observable of this report implies positivity" | about statements | MINOR (the laws are NUMERICAL/CONJECTURE; correct as "there is no proof from them") |
| grid §4 row M_m | "refutes: route (a) of C_B, every class argument" | about arguments | valid |
| crossword I3, I11 | "every proof that uses only…" | about proofs | valid |

**No use discards a true inequality for ζ as false.** The only defect is one of formulation (wording MAJOR,
reparable, already identified by R186_110 and not repaired in the grid/CONSTRAINTS/PATTERN_REPORT).

### 1.3 (c) Does `r187_mm.py` reproduce λ_A of ζ as δ → 0? Is the negative sign real?

**The δ → 0 limit of M₁ is NOT ζ.** It is ξ·(s−½−iγ₁)²(s−½+iγ₁)²: ζ with the zero at ½ ± iγ₁ of multiplicity 3, whose form is
𝔞_T + 4|Φ_F(½+iγ₁)|² ≥ 𝔞_T. So λ_A^{M₁}(δ→0) ≥ λ_A^ζ, with excess 4F̂*(γ₁)² ≤ 4λ_A (the minimizer F* has
Σ_γ|F̂*(γ)|² = λ_A, lem:roughEF). The observed difference is not "∼δ²" because it has **three sources**: (1) +4F̂*(γ₁)² independent
of δ; (2) −4δ²(∫F* t sin γ₁t)² + O(δ⁴) (§1.1), negative; (3) different Galerkin M between the ζ and M₁ runs
(68/72 at ½log3, 73/75 at 0.61, 78/79 at 0.67, 95/90 at ½log5): the Galerkin value is a decreasing upper bound in M.
The PATTERN_REPORT's sentence "the only difference ζ/M₁ is the term −Cδ²" is **incorrect** (MINOR: it does not change the verdict
of the test, it reinforces it: as δ → 0, M₁ is *above* ζ and still shares the whole pattern).

Control recomputation (same `flint`/arb stack, different `M_override` and `extra_digits`; scratchpad `audit_mm.csv`):

| T | δ | record (M, dps) | recomputation (M, dps) | ζ at the **same** M | reading |
|---|---|---|---|---|---|
| ½log3 | 10⁻⁶ | — | **+9.48028e-4** (72, 38) | 9.461469e-4 (72) | M₁ − ζ = **+1.9e-6 > 0**: term (1), as predicted by §1.1; not −Cδ² |
| ½log5 | 10⁻⁶ | 3.162138e-12 (95, 43) | **3.164191e-12** (90, 43) | 3.176069e-12 (90) | M₁ − ζ = −1.2e-14: term (2) dominates because F̂*(γ₁)² ≤ λ_A/4 ≈ 10⁻¹² and (∫F* t sin γ₁t)² ≈ 3·10⁻³ |
| log 2 | 0.1 | −1.522270e-3 (81, 39), n₋=2 | **−1.512936e-3** (60, 49), n₋=2 | 9.86e-8 | sign robust in M and precision |
| log 2 | 0.3 | −2.849109e-2 (81, 39), n₋=2 | **−2.847154e-2** (50, 49), n₋=2 | 9.86e-8 | same; ratio 0.3/0.1 ≈ 18.8 (δ² plus higher orders, 2δT = 0.42) |

The negative sign at δ = 0.1/0.3 is **structural, not an artifact**: by Rayleigh λ_A^{M₁} ≤ 𝔞_T(F*) + 4Re Φ_{F*}(½+z)² and with a
node of F* at γ₁ the second term is −4δ²b² < 0 (perturbative regime, not the e^{2δT} regime of R162_2501 Prop 1). The arb
balls enclose the algebra; the Gauss panel-quadrature error is not enclosed: label **NUMERICAL** (not "certified").

---

## 2. f_t and non-identifiability

### 2.1 What Thm F exactly says (reading of the proof)

- f_t = ζ + t·g, g(s) = Σ_{m>R}c(m)(m/√M)^{−s}, c even real self-dual under the DFT of ℤ/M with c(r) = 0 for |r| ≤ R (Lem 2.1,
 PROVED; finite instance of Bochner/Kahane–Mandelbrojt, CITED). **Class:** general Dirichlet series over the semigroup
 generated by ℕ and {m/√M}; **exact EF** Λ_t(s) = Λ_t(1−s) with π^{−s/2}Γ(s/2); pole of ζ; real coefficients; **no Euler
 product**; −f′/f with coefficients b_t(λ) of both signs (Σc = 0).
- **Coincidence:** b_t(λ) = Λ(λ) for every frequency λ < λ₁ = m₁/√M (formal in the ring of generalized series; g/ζ and
 log(1+tg/ζ) have frequencies ≥ λ₁). So W^{f_t}_T = W^ζ_T **exactly** for T ≤ ½log λ₁ (the atom λ₁ enters at
 |u| = 2T where c_F(±2T) = 0). Reproduced. PROVED mod. the explicit Weil/Barner formula for generalized series (CITED).
- **Zeros outside:** F.4 proves Q(η) < 0 with φ = φ₀ + η τ_aφ₀ ∈ L²(I_T), T = ½log λ₁ + ε, Q = sum over zeros of Λ_t;
 so there exists t_ρ ∉ ℝ. Reproduced. The produced zero **may have σ > 1** (text of F.4 and R163_991 §3.4(iii)): without Euler
 nothing prevents it. The F.4 witness is for the **full Weil form** (includes the polar term 2Φ(0)Φ(1)): it is not in 𝒫_T.

### 2.2 Does the conclusion depend on f_t being admissible in the declared carrier?

Yes, in the sense of §1.2: f_t is not ζ, so it only refutes proof schemes. But there is a second, finer point: the declared
row D is λ_A ≥ 0 **over 𝒫_T** (eq:Kprim), and what F.4 gives for f_t is W^{f_t}_T ⋡ 0 over **L²(I_T)**. R186_028 proves that
for ζ itself n₋(𝔞_T|L²(I_T)) = 1 (the pole) with no primitive contact: negativity in L² ⇏ negativity in 𝒫_T. Therefore
"f_t has a witness" in the sense needed by Theorem 3(a) of R186_036 ("λ_A^{f_t}(T) < 0 for some T") **is not proved in
the record**: R163_901 Cor F labels it ARGUED (real-rooted witness of R163_501 transferred), R163_991 §3.5 accepts ARGUED,
R186_110 §1.3(ii) flags it. R186_111 §3.4 is right that "shares h*_T, 𝒱_T for T < T₁" is PROVED, but **conflates
"T_c(f_t) ≤ T₁ + ε PROVED" (full form) with the primitive witness**: these are distinct objects.

### 2.3 What is PROVED without the primitive witness

- R163_901 §3(i): "no argument with the listed inputs proves W_T ⪰ 0 ∀T **over PW_T**" — PROVED (F.4 suffices), but it is
 the L² formulation, not the declared one.
- W3′ (5A via f_t), R166_501 Thm A(a), R164_601 (f_t's "sign fails" row: atoms of both signs, Lem 2.1 rem. (a)),
 R166_802/R167 when they only use "f_t ∉ H": they do not need the primitive witness. PROVED.

### 2.4 Lemma A (auditor): from the full witness to the primitive witness. CONDITIONAL on (Z-strip)

**Lemma A.** Let f be a function with exact EF of ζ, pole of ζ, zero-side identity (lem:roughEF for f) and
**(Z-strip): all zeros of Λ_f lie in 0 < Re s < 1**. If there exists φ ∈ L²(I_{T₀}) with Z(φ) := Σ_ρ Φ_φ(ρ)Φ_φ(1−ρ) < 0,
then λ_A^f(T′) < 0 for all sufficiently large T′.

*Proof (full outline).* Let G = a e^{t/2}1_{[T′−w,T′]} + b e^{−t/2}1_{[−T′,−T′+w]} with (a,b) solving
Φ_{φ+G}(0) = Φ_{φ+G}(1) = 0 (2×2 system with diagonal e^{T′}(1−e^{−w}) and off-diagonal w: a ≈ −Φ_φ(1)e^{−T′}/(1−e^{−w}),
b ≈ −Φ_φ(0)e^{−T′}/(1−e^{−w})); then φ+G ∈ 𝒫_{T′} and ‖G‖² ≍ e^{−T′} → 0. Z is a fixed quadratic form (sum over zeros,
independent of T′): Z(φ+G) = Z(φ) + 2Z(φ,G) + Z(G). For ρ = ½+β+iγ: |Φ_G(ρ)| ≤ C e^{(|β|−½)T′}/(1+|γ|) (integration by
parts in each piece), which is ≤ C/(1+|γ|) uniformly and → 0 term by term **if and only if |β| < ½** (both pieces: one
needs Re ρ < 1, the other Re ρ > 0). Majorant C/(1+|γ|)² summable over zeros of density log γ; |Φ_φ(ρ)| of fast decay
in γ (φ ∈ C_c^∞ piecewise). Dominated convergence: Z(G) → 0 and Z(φ,G) → 0. So 𝔞_{T′}(φ+G) = Z(φ+G) → Z(φ) < 0. ∎

*Consequences.* (1) For **ζ** (Z-strip) is the Re s = 1 zero-free line theorem (PROVED): the two formulations of
row D ("W_T ≥ 0 on L²(I_T) ∀T" and "λ_A ≥ 0 on 𝒫_T ∀T") **coincide** (⟸ trivial; ⟹ by Lemma A). (2) For **f_t**, F.4 does not
guarantee (Z-strip) (the zero can be at σ > 1), and in fact for large |t| ζ = −tg in σ > 1 is not excluded by any
bound (|ζ| ≥ ζ(2σ)/ζ(σ) → 0 as σ → 1⁺). Alternative without (Z-strip): the construction of R162_2501 Prop 1 (test concentrated at a
zero of maximal real part) works if the sup of |Re ρ − ½| is **attained** at a zero; for a general almost-periodic
(Bohr) Dirichlet series that is not guaranteed. **Primitive witness of f_t: CONDITIONAL on (Z-strip) or on "attained sup";
in general OPEN.** I see no obstruction (I agree with R163_991), but it is not a theorem.

### 2.5 Does "explicit" include an ARGUED falsifier?

No. A
falsifier whose decisive property (λ_A < 0 for some T) is ARGUED is not explicit for the declared property; it is
explicit for the full form (F.4 PROVED). The entries that close using the primitive witness of f_t move to CONDITIONAL (§3.3).

---

## 3. Does any falsifier close something that could be the solution?

### 3.1 Review method

For each closure of log 13–31 and of the walls W-lin, W-det, W-fam, W-pat, BR that invokes M_m or f_t: (A) is it "the method does not
distinguish" (valid) or "the statement is false" (invalid)? (B) is there a written transfer theorem or only the falsifier?
(C) which property of the falsifier does it use and with what label?

### 3.2 Table

| closure | invokes | type (A) | transfer (B) | property used (C) | verdict |
|---|---|---|---|---|---|
| log 16: C_B by inertia NO-GO (R184_004 Cor 5, class 𝒜) | M_m | method | Cor 5 PROVED ("𝒜 valid ⟹ κ(ζ)=∞") | same blocks, rank ≤ 6m; λ_A^{M_m} → −∞ (Prop 1 PROVED) | valid |
| log 18: W11′ (R184_015 Thm 2) | M_m | method | Thm 2 PROVED | invariance of P under X ↦ M_m | valid |
| log 27: **W-lin** (R186_026 Thm 3.3, R186_031, R155 Lemma R) | none | impossibility in class (linear certificates in a fixed basis) | PROVED | — | valid; **does not depend on falsifiers** |
| log 28: **W-det** (R186_034 Thm 3.1) | none | impossibility in class (determinants with O(1) multiplicative error) | PROVED elementary (Rayleigh) | — | valid; does not depend on falsifiers; reserved exception (Landau–Widom law) |
| log 29: **W-fam** (R186_036 Theorem 3) | f_t (a), M_m (c) | method (poorly worded as a statement) | Theorem 3 = transfer | (a) **primitive witness of f_t: ARGUED**; (c) M_m shares qualitatives: PROVED for monotonicity/continuity, ARGUED for Thm M | **CONDITIONAL** (on (Z-strip)/Cor F); also "NO-GO within 𝔉" withdrawn by R186_110 (bilateral laws OPEN) |
| log 31: **W-pat** ("quantitative corollary of W-fam/Thm F") | M₁ executed, f_t declared | method (class property) | inherits Theorem 3 | M₁: NUMERICAL (robust, §1.3); f_t: ARGUED witness | the M₁ part is valid as a class test (NUMERICAL); the f_t part is **CONDITIONAL** |
| **BR** (R185_005) | M_m/f_t only in (c) class observation and in §3 (I11) | impossibility relative to 𝔐 | PROVED relative to 𝔐 mod. ρ1′, ρ2, exhaustiveness ARGUED | does not depend on M_m/f_t | no objection by falsifiers. **Separate note (MAJOR):** the "Conclusion" of §2.1 invokes "D is equivalent to RH on the declared carrier (cluster E1, I1)", not permitted; the barrier must be rewritten without that phrase (its content in (a)/(b)/(c) does not need it except for the words "weaker than RH") |
| 7C (R166_801 Thm 7C, log 12) | M_m, f_t | method | Thm 7C PROVED for "configurations with a witness" | for f_t it assumes "its witness in T_c" | valid for M_m; for f_t **CONDITIONAL** (witness in the R163 sense, ARGUED) — the closure of 7C stands on M_m alone |
| I9 (R166_501 Thm A) | f_t, M_m | hypothesis classes | PROVED | only "f_t ∉ H", "M_m ∉ H" (hypothesis (iii)) | valid |
| I11 (★_cell) | f_t | method | — | witness of f_t ARGUED (already flagged) | CONDITIONAL (already labeled) |
| I14 (R164_601 Thm 3.1) | M_m with window | consistency | PROVED (logic) | the inequality holds for every zero set | valid |
| R163_901 §3(i) | f_t | method | PROVED | F.4 (full form) | valid for "W_T ⪰ 0 on PW_T"; for 𝒫_T, CONDITIONAL (Lemma A) |
| CONSTRAINTS §3.1 / PATTERN_REPORT §3.3 | f_t | statement (wording) | inherits Theorem 3 | "f_t … has a witness" | CONDITIONAL + fix wording |
| R186_039 §0.4, §3.1 | f_t, M_m | descriptive | — | "λ_A^{f_t} = λ_A^ζ + θ\|t\|C(T)": ARGUED; "Q_m ≍ −e^{2δT}": PROVED by R162_2501 Prop 1 (not ARGUED as the memo says) | labels to correct (one in each direction) |

### 3.3 Closures that move to CONDITIONAL (on the primitive witness of f_t: (Z-strip) or Cor F)

1. **W-fam / R186_036 Theorem 3(a)** and grid entry 29 ("via family at closed T").
2. **W-pat** (grid entry 31) in its f_t part ("no finite range [0,T_max] would do it"); the M₁ part remains NUMERICAL.
3. **R166_801 Thm 7C applied to f_t** (the closure of 7C stands on M_m, whose witness is PROVED: 7C stays closed).
4. **R163_901 §3(i) read as the declared row D** (over 𝒫_T); as a statement over PW_T it remains PROVED.
5. CONSTRAINTS_FOR_PATTERN §3.1 and PATTERN_REPORT §3.3 (inherit 1).

**None of these routes reopens as a route to D**: in all of them M_m gives the same method closure (witness PROVED) except
where the point is "exact coincidence on a finite window", which only f_t provides. What remains open for this
reason is exactly what R186_110 already isolated: **the bilateral asymptotic laws** (out of reach of f_t by
construction and not shared by M_m). No route is closed **solely** by a falsifier without a written transfer.

### 3.4 Operational advice (without touching the grid)

- Rewrite Theorem 3(a) and W-fam/W-pat as transfer theorems ("there is no proof of D that uses of ζ only P ∈ 𝔉
 and the qualitative properties") and label them CONDITIONAL until the primitive witness of f_t is proved.
- To close the condition: either prove (Z-strip) for some f_t from F.4 (it suffices to have an f_t with zeros outside *and* no
 zeros in Re s ≥ 1, e.g. with |t| in the range where |t g| < ζ(2σ)/ζ(σ) in σ ≥ 1 + η and a separate argument in 1 < σ < 1+η), or prove "attained
 sup". Both remain pending for a future round.
- Unify the definition of M_m (polynomial vs. rational) and correct the "−Cδ²" sentence in PATTERN_REPORT.

---

## 4. The other falsifiers (one line each)

| falsifier | definition | status | used in the truncated Wiener–Hopf route (R186_042/043)? |
|---|---|---|---|
| **DH** (Davenport–Heilbronn) | combination of L(s,χ) with exact EF and zeros outside; no Euler | CITED (classical) | no |
| **BFdisc** / P_171 (R163_803, R171_FINAL) | discrete Beurling system with N = cx + O(x^θ), θ ∈ (1/3, ½), Beurling RH false | PROVED (audit R163_891 applied) | no |
| **Λ̃** (R162_2601 Thm Λ̃) | positive atomic weights Λ̃(n) = 1 − Σ2Re n^{ρ_j−1} at {±log n} that reproduce part E under H(m) | PROVED | no |
| **b_θ** (R167_102 Thm B/B′) | Λ·½(1+cos(γ log n + arg W + θ)): 0 ≤ b_θ ≤ Λ, twisted sum of size X^{1/2} | Thm B PROVED (bilateral); B′ unilateral with VK at height 2γ: PROVED with citation; Thm D (after Perron) ARGUED | no |
| **ℕ ∪ √2·ℕ** (R184_005 N1/N2; R163_102 Lemma S) | root substitution; discrete Beurling with N = ρx + O(1) and the zeros of ζ | PROVED (explicit counterexample; sup R ≈ 2.00 NUMERICAL up to 10⁶) | no |
| **R = L(u,χ)** (R184_014 Prop B.3, Cor B.3′) | relaxed class with ε_p bounded at every Witt level, without integrality | PROVED | no |

In the current route (sign = extreme eigenvalue of W_T(σ₊ − σ₋/β)|𝒫_T at the inertia crossing) the only falsifier that
intervenes is **M₁** (`r043_wh.py` block (6): reproduces −1.52e-3, n₋ = 2 at log 2 with standalone code — second
independent implementation, consistent with §1.3). None of the six above applies to the W_T form of ζ on 𝒫_T
(they are models of Λ, not of the form), and none was used to close anything in R186_042/043.

---

## 5. Summary of defects

| # | severity | where | what | action |
|---|---|---|---|---|
| 1 | **MAJOR** | R186_036 Theorem 3(a); grid 29 (W-fam); grid 31 (W-pat, f_t part); R166_801 (f_t); R163_901 §3(i) read on 𝒫_T; CONSTRAINTS §3.1; PATTERN_REPORT §3.3 | primitive witness of f_t cited as PROVED/"mod. Thm F CITED"; it is ARGUED (Cor F) and here CONDITIONAL on (Z-strip) | relabel CONDITIONAL; task §3.4 |
| 2 | MAJOR (wording) | R186_036 Theorem 3(a); grid 29; CONSTRAINTS §3.1; PATTERN_REPORT §3.4 | "no P … implies D" (about statements) instead of transfer (about proofs) | rewrite |
| 3 | MAJOR | R185_005 §2.1 "Conclusion" | invokes the D–RH equivalence, not permitted | rewrite BR's conclusion |
| 4 | MINOR | PATTERN_REPORT §3.4 | "the only difference ζ/M₁ is −Cδ²"; the δ→0 limit of M₁ is not ζ; comparison at different M | correct text; formula of §1.1/§1.3 |
| 5 | MINOR | R163_801 Thm 5 vs R162_2501 §1 vs Paper 48 l.436 | two definitions of M_m (polynomial / rational) | unify (the one executed is the polynomial one) |
| 6 | MINOR | R186_039 §0.4 | "Q_m ≍ −e^{2δT} ARGUED" — it is PROVED (R162_2501 Prop 1) | relabel |
| 7 | MINOR | `DATA_MM_FALSIFIER.csv`, PATTERN_REPORT | "certified" for values with unenclosed Gauss quadrature | NUMERICAL |

**Contact with the sign: none.** Row D: OPEN. No symbol in the grid changes because of this audit; the relabelings of
§3.3 are for the editor of the grid and of the crossword.
