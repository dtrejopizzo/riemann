# R186_041 — Degree-0 functionals in F: the nodal measure of the minimizer and Λ beyond the window

Phase 186, round 19.
CONDITIONAL / OPEN / NO-GO / NUMERICAL (+ ARGUED when the proof is not written out). Paper 46, grid and
crossword are not touched. Standalone script: `r041_node_measure.py` (imports r034_det.py; ≈ 6 min).

Read: README 186 rounds 14–18; R186_111 §1.4 (degree 0 omitted from the trilemma); R186_032 §4 (Ω: S1–S6); R186_038 (Lemma 0,
α.1, γ.1); R186_036 Lemma 2 and Theorem 3; R186_040 §1.2 (centroids 7→14, alternating parity, vanishing at zeros ≤ T*);
R186_022/103/034 (peak of ĥ*, zeros of σ); R165_202 1.1–1.10, 2.1, 3.1 (nodes, Gauss quadrature, Cauchy
identity); R165_201 Thm 2–3; R166_501 (G),(N); R185_005 §1.3 (O1/O2); Paper 46 eq:symbol, eq:form, eq:Aform, eq:Kprim,
def:PD, def:W/eq:nuw, thm:Z, lem:monoT, lem:roughEF, prop:band, prop:align, prop:negtrace.

## 0. One-line verdict

**No contact with the sign.** The degree-0 object that S2 requires exists and is here constructed: the **Gauss nodal
measure** μ_X = Σ_{x∈X_T} w_x δ_x of the minimizer h*_T (nodes X_T of G = ĥ*_T, weights w_x ≥ 0), which is the optimal
dual certificate of window T in the measure sense, and whose transform μ̌_X(u) = Σ w_x cos(xu) is the only function
"of the nodes" that Λ outside the window can touch (Lemma 2: strip 2T < |u| < 2T′). Three new facts, one PROVED and
two NUMERICAL: (1) Lemma 1 (Gauss–Kreĭn): 𝔞_T − λ_A = Σ_x w_x|F̂(x)|² on V_X = cl span{H_x} ⊂ 𝒫_T; (2) **below
T* = 2πe^{2T} the nodes of ĥ*_T are the zeros of ζ and the weights equal w_γ = 1.0000** (½log5: 14.135, 21.022, 25.011,
30.425, 32.935, 37.587; w = 1, 1, 1, 1, 1, 1.0004): the window's nodal measure, computed purely from σ_T, is the
low-height zero measure; (3) **μ̌_X has atoms of mass −v_n/2 at ±log n for n < e^{2T}** (log 2: −2.08 measured vs
−2.10 model; log 3: −2.55 vs −2.60): the nodes "know" the window's primes. **But** every degree-0 statement that
couples μ_X with Λ on (2T, 2T′) and bounds λ_A(T′) is either the identity of Lemma 2 (no sign), or the inequality
A′ = D(T′) on the subsampled subspace V₀ (a consequence of D: violates (c)), or an alignment condition whose dominant
term is polar (R186_038 γ.1) and which M_m and f_t share (violates S6). The missing input is exactly **the deviation
of Λ on (2T, 2T′), at the node frequencies, relative to the polar term**: this is not window data and does not come
out of sieve theory or Perron's formula; in the corpus it exists only as the zero side (O2 of R185_005). (i) alignment
of future primes: numerically FALSIFIED as a universal inequality (mixed signs) and vacuous as Ω.
(ii) interlacing of nodes of ĥ*_T / zeros of σ_{T′}: NO-GO (no Sturm structure: the remainder r̂ is not band-limited;
Cauchy on the bundle inherits; phase 165 already closed interlacing with zeros of ζ as non-decisive). Nothing changes in D.

## 1. Object: the Gauss nodal measure

**Framework.** T > 0, I_T = (−T,T), F ∈ L²(I_T), F̂(τ) = ∫F e^{iτt}, c_F autocorrelation (support [−2T,2T]),
𝔞_T(F) = (1/2π)∫σ_T|F̂|², σ_T = m − Σ_{𝒩_T}v_n cos(τ log n), 𝒫_T = {A(F) = B(F) = 0} = {F̂(±i/2) = 0},
λ := λ_A(T) = min 𝔞_T over the sphere of 𝒫_T, h* = h*_T minimizer, G = ĥ* (even: real; odd: −iĥ* real).
Standing hypotheses (H): λ simple, h* real-rooted with simple nodes (R165_202 1.6: PROVED if λ simple). X = X_T =
{x : G(x) = 0} ⊂ ℝ, symmetric. H_x := inverse transform of G/(z−x); **H_x ∈ 𝒫_T** because Ĥ_x(±i/2) =
G(±i/2)/(±i/2−x) = 0 (the Lagrange multipliers never appear; this is not stated in R165_202 2.1). Explicit formula:
H_x(t) = −i e^{−ixt}∫_{−T}^t h*(s)e^{ixs}ds, supported in I_T because G(x) = 0 (PROVED, one line).
V_X := cl span{H_x : x ∈ X} ⊂ 𝒫_T. Weights: w_x := (𝔞_T − λ)(H_x)/|G′(x)|² ≥ 0.

**Lemma 1 (Gauss–Kreĭn; PROVED on V_X).** Under (H): (a) (𝔞_T − λ)(H_x, H_y) = 0 for x ≠ y (R165_202 2.1: K̂ =
G/((z−x)(z−y)) ∈ 𝒫_T and h* is an eigenvector); (b) for every F ∈ V_X, 𝔞_T(F) − λ‖F‖² = Σ_{x∈X} w_x|F̂(x)|², i.e.
**the symbol (σ_T − λ)dτ/2π and the discrete positive measure μ_X = Σ w_x δ_x represent the same form on V_X**;
(c) μ_X is a feasible dual point in the measure sense: with ν_X := (μ_X − (σ_T − λ)dτ/2π)^∨ one has
f := σ_T + 2π ν̂_X = λ + 2πμ_X ≥ λ, and ν̌_X annihilates {c_F : F ∈ V_X}; if V_X = 𝒫_T, then supp ν_X ⊂ {|u| ≥ 2T}
modulo span{cosh(u/2), u sinh(u/2)} (the exact annihilator, §1.1) and **μ_X is the optimal dual certificate of def:PD**
(value λ_A, strong duality attained in measures). (d) For 0 < |u| < 2T, as distributions over the space of
autocorrelations of V_X:
 μ̌_X(u) = Σ_x w_x cos(xu) = −½K(|u|) − Σ_{n∈𝒩_T}(v_n/2)(δ_{log n} + δ_{−log n}) + a cosh(u/2) + b u sinh(u/2),
with K the Lévy kernel of Paper 46 (K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2))).
*Proof of (d).* For F, F′ ∈ V_X, polarizing (b): ∫(F∗F̃′)[σ_T^∨ − λδ₀ − μ̌_X] = 0, with σ_T^∨ = C₀δ₀ − ½K(|u|) −
Σ(v_n/2)δ_{±log n} (eq:Aform). The annihilator of {F∗F̃′ : F, F′ ∈ 𝒫_T} on (−2T,2T) is that of the d's with Toeplitz
operator T_d(𝒫_T) ⊂ 𝒫_T^⊥ = span{e^{±t/2}}: finite rank ⟹ d is an exponential polynomial, and the rank condition
forces d ∈ span{e^{±u/2}, u e^{±u/2}}, even: span{cosh(u/2), u sinh(u/2)} (§1.1). ∎

**1.1 The annihilator (PROVED).** If d(t−s) has finite rank on I_T then d is an exponential polynomial (finite-dimensional
translation-invariant spaces are generated by exponential monomials, standard). A term c e^{λt}(t−s)^m e^{−λs} applied
to F ∈ 𝒫_T must land in span{e^{±t/2}}: this forces λ = ±½ and m ≤ 1, and for m = 1 the term t e^{λt}∫e^{−λs}F = 0 by
the Tate constraint. Conversely d = u e^{±u/2} and e^{±u/2} work. ∎

**1.2 Completeness (COMP): V_X = 𝒫_T. OPEN; partially negative NUMERICAL evidence.** Argument in favor (ARGUED):
if F ⊥ V_X in L² then the Hilbert transform of F̄G (type 2T) vanishes on X; decomposing into analytic parts,
F̄G = −Hφ with φ₊ = e^{iTτ}ψ, ψ ∈ PW_T vanishing on X; if {ψ ∈ PW_T : ψ|_X = 0} = span{G} (holds when
G ≍ 1/τ, i.e. h*(±T) ≠ 0), F ∉ L². The argument fails if h*(T) = 0 (at ½log5, h*(T) = −4·10⁻⁶: G decays faster and
G·τ^j ∈ L² are functions of PW_T vanishing on X: the defect is ≥ the number of such j). **Numerics (M = 50/70/100 stable):**
exact quadrature to 10⁻³ on a mid-band test (peak τ ≈ 30); on low-pass tests (1−(t/T)²)⁴P_j(t/T) the nodal sum
captures 64–99% of (𝔞−λ)(F); the eigenvalues of the defect on 12 low-pass tests are O(1) of both signs:
**this is not a defect of rank ≤ 2**. Node-density deficit on (0,130): 1.7–2.3 (no node in (0, γ₁)). Honest reading:
Lemma 1 holds on V_X; that V_X = 𝒫_T is not proved and the data suggest the nodal representation leaves out a
low-frequency subspace. What follows is stated on V_X (where the object is exact).

**1.3 New numerical facts (NUMERICAL, M = 70, X = 120).**
| T | λ_A | nodes < T* | w at those nodes | final spacing vs π/T | atom log 2 (measured / model / without atom) | atom log 3 | log 4 |
|---|---|---|---|---|---|---|---|
| ½log3 | 9.46e-4 | 14.147 (γ₁ = 14.135; T* = 18.9) | 1.0025 | 5.58 / 5.72 | −2.09 / −2.13 / +1.13 | — | — |
| log 2 | 1.00e-7 | 14.135, 21.022, 25.012 (T* = 25.1) | 1.0000, 1.0001, 1.0003 | 4.52 / 4.53 | −2.08 / −2.10 / +1.16 | −2.55 / −2.60 / +1.61 | — |
| ½log5 | 3.2e-12 | 14.135, 21.022, 25.011, 30.425, 32.935, 37.587 (T* = 31.4) | 1, 1, 1, 1, 1, 1.0004 | 3.71 / 3.90 | −2.08 / −2.09 / +1.17 | −2.55 / −2.61 / +1.61 | −0.34 / −0.44 / +1.87 |
("model" = −½K − atoms smoothed with a Gaussian ε = 0.06 + adjusted Tate term; a = 2.00, 1.99, 2.02 across the three
windows: **the coefficient of cosh(u/2) is 2 = β₀ of Paper 46's certificate**, consistent with def:PD.) Orthogonality
(a): 10⁻⁷, 10⁻⁸, 10⁻¹². No non-real zeros of G on [0.3,118]×[−1.5,1.5] (argument principle): real-rootedness
confirmed across the three windows.

**Reading of "nodes = zeros, weight 1."** lem:roughEF gives 𝔞_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ); at heights where the zeros
are on the line and simple (CITED, verified up to 3·10¹²), a zero contributes |F̂(γ)|²: the zero measure Σδ_γ
represents 𝔞_T (λ = 0) and the nodal measure represents 𝔞_T − λ_A with λ_A ≈ 10⁻¹²; the coincidence node = γ_k, w = 1
below T* is the "Gauss quadrature" version of R186_112/040 (head block = low-zero sampling). It is not a theorem
(two measures representing the same form on V_X need not be unique: Kreĭn indeterminate, phase 155 round 5);
it is the same fact with one extra number: **the weight**. Beyond T* the nodes separate from the zeros (40.925 vs
40.919; 43.341 vs 43.327) and the weight rises to 2.5–3.2: there the nodal measure is no longer the zero measure.

## 2. Candidate A: the exact coupling nodes ↔ Λ beyond the window

**Lemma 2 (strip decomposition; PROVED on V_X-pairs, CONDITIONAL (COMP) on 𝒫_{T′}).** Let T′ > T and
F ∈ 𝒫_{T′} with c_F in the space where Lemma 1(d) holds (if (COMP), all of 𝒫_{T′}). Then
 𝔞_{T′}(F) − λ_A(T)‖F‖² = Σ_{x∈X_T} w_x|F̂(x)|² + ∫_{2T<|u|<2T′} c_F(u) η̌_T(u) du − Σ_{2T≤log n<2T′} v_n c_F(log n),
with η̌_T(u) := μ̌_X(u) + ½K(|u|) − a cosh(u/2) − b u sinh(u/2) (the "allied window": an explicit function of X_T, w).
*Proof.* 𝔞_{T′}(F) = ∫c_F σ_{T′}^∨; σ_{T′}^∨ = σ_T^∨ − Σ_new(v_n/2)δ_{±log n}; on |u| < 2T substitute σ_T^∨ −
λδ₀ by μ̌_X + Tate correction (Lemma 1(d)); on |u| ≥ 2T, σ_T^∨ = −½K(|u|) has no atoms; regroup. ∎
Consequences: (i) with F = h*_T this recovers lem:monoT (λ_A(T′) ≤ λ_A(T)) with the loss localized in the strip term
(c_{h*} = 0 there: loss 0, as it should be; the real loss of λ_A comes from F ∉ 𝒫_T); (ii) on the subsampled subspace
V₀ := {F = h*_T ∗ k : k ∈ L²(I_{T′−T})} (F̂ = G·k̂ vanishes on X_T) the nodal sum is 0 and
 𝔞_{T′}(F) − λ_A(T)‖F‖² = ∫∫[η̌_T − Σ_new v_n δ_{log n}](u) c_{h*}(u−s) c_k(s) du ds:
**the sign on V₀ is decided by the boundary of c_{h*} (c_{h*}(2T−ε) ≈ ε h*(T)h*(−T), R162_407 Prop 4.3 / Lemma α.1)
paired with [allied window − new atoms]**; in the limit T′ ↓ ½log n₀ with a single new prime this gives exactly
the fold of R186_036 Lemma 2, Δλ′ = −2v_{n₀}h*(T)h*(−T) (consistency; PROVED as a formal limit).

**Candidate inequality A′ (what S2 would ask for).** "For every T′ ∈ (T, T + Δ] and every c = c_k, k ∈ L²(I_{T′−T}):
∫∫[η̌_T − Σ_new v_n δ_{log n}](u) c_{h*}(u−s) c(s) ≥ −λ_A(T)‖h*∗k‖²". Verification (a)–(e):
- (a) degree 0 in F: yes (η̌_T depends on X_T, w; c_{h*} on normalized h*; k is a test variable, not F).
- (b) Λ(n) with log n > 2T at the nodes: yes, Σ_new v_n ∫c_{h*}(log n − s)c(s)ds, and η̌_T(log n) = Σ_x w_x cos(x log n)
 + ½K(log n) − Tate **is literally the S2 nodal alignment sum** when c ≈ δ.
- (c) not an identity / not a consequence of D: **NO.** A′ ⟺ 𝔞_{T′} ≥ λ_A(T)·(…) ≥ 0 on V₀ ⟸ D(T′). It is D restricted to
 a subspace, with window T "precomputed." Same as R186_038 α.3 and R186_029 Lemma H: true-if-D.
- (d) input neither sieve nor Perron: the decisive quantity is Σ_new v_n cos(x log n) for x ∈ X_T, over a finite strip.
 For small Δ these are finitely many numbers (no theorem; a computation). For large Δ, by R186_038 γ.1 (explicit
 formula with test e^{−u/2}φ cos(xu)), Σ v_n φ(log n)cos(x log n) = 2∫e^{u/2}φ cos(xu) + O(zeros): the polar term
 dominates and is **universal** (shared by M_m, f_t, Beurling DMV). What distinguishes ζ is the remainder
 Σ_ρ φ̃(t_ρ ∓ x), the zero side.
- (e) implies/bounds λ_A(T′): only on V₀; on the complement Σ w_x|F̂(x)|² > 0 enters, but so does c_F in the strip.
- Admission S6: η̌_T is window-T data (a function of σ_T, λ_A(T), constraints): M_m and f_t share it for T < T₁
 (R163_901 Thm F.3). **A′ does not separate.** S6 fails, so it is not Ω.
**Verdict A:** Lemma 1 and Lemma 2 are tools (PROVED on V_X); A′ is NO-GO as a route (= D on V₀). What Lemma 2
contributes is the **exact form of box S2**: the only channel through which Λ ∉ window touches the nodes is the
strip, through η̌_T; any Ω must be a statement about Σ_x w_x cos(x log n) − [polar] for log n > 2T
that is not window data. With "nodes = zeros below T*" (§1.3) this reads: Σ_{γ≤T*} cos(γ log n) + (nodal tail)
against the tail of Λ: the zero side. It lies outside 𝔐 (O2) and outside what this memo can prove.

## 3. Candidate B: interlacing of nodes of ĥ*_T / zeros of σ_{T′} (item (ii))

**NO-GO (reasoned, no numerics).** (1) There is no Sturm structure: the eigenvalue equation in τ is (σ_T − λ)G =
r̂ with r = [(σ_T(D) − λ)h*]|_{|t|>T} (supported on T < |t| < 3T plus a Lévy tail), **r̂ is not band-limited** and
there is no second-order differential equation whose zeros can be compared. (2) The zeros of σ_{T′} (finitely many, on
[0, τ^lo(A)], prop:band) vs nodes of ĥ*_T (infinitely many, density T/π): only a local statement on the band is
possible; at ½log5 the zeros of σ_{2,3,4} (1.98, 4.24, 6.46, 8.74, 11.29, 16.5, 18.8, 27.0, 28.6, …) and the nodes
(14.1, 21.0, 25.0, 30.4, 32.9, …) **do not interlace** (four zeros of σ before the first node). (3) Cauchy interlacing
of the bundle (Neg, Pos) is for finite compressions and inherits the margin (R186_026 Thm 3.3, R186_028). (4)
Cross-check with phase 165: R165_201 Thm 2 (phase identity, exact) and Thm 3(a) (perfect interlacing with both signs:
"interlacing ⇏ sign"); R165_202 3.3 (local interlacing of nodes/zeros of ζ) is proved only under S_on′ > |S_off′|,
and R165_190 closed the geometric branch. None of that uses zeros of σ. (5) What is true and PROVED: the zeros of
σ_{T′} see Λ beyond 2T, but the minimizer h*_T does not see them (lem:monoT: 𝔞_{T′}(h*_T) = 𝔞_T(h*_T)); an interlacing
between X_T and Z(σ_{T′}) would be a condition about window-T′ numbers (M_m shares it) with no consequence for
λ_A(T′). **No first lemma.**

## 4. Candidate C: alignment of future primes at present nodes (item (i))

**Falsifier (NUMERICAL):** cos(x log n) at the first 8 nodes of ĥ*_T for future n has mixed signs in
every window (½log5, n = 5: −0.73, −0.75, −0.83, +0.27, −0.92, −0.69, −0.99, +0.80; n = 7: −0.72, −1.00, −0.03,
−0.88, +0.31, −0.63, −0.46, −0.88), and the weighted sum Σ_x w_x cos(x log n) (smoothed) changes sign with n (½log3:
−3.2, +0.6, −2.2, −1.4, −0.6 for n = 3, 4, 5, 7, 8; ½log5: −2.6, −2.4, +0.5, +0.3, −1.6 for 5, 7, 8, 9, 11). **No
universal alignment inequality exists**; prop:align speaks of the negative set of σ (arcs cos(τ log p) > 0 for
τ > τ_a), not of the nodes of ĥ*, and at the nodes below T* what is being read is cos(γ_k log n) with γ_k zeros of ζ:
the "alignment" of the low zeros with the future primes is exactly the zero side of γ.1. **Law of motion:**
R165_202 1.8 (ẋ_j = −(1/T)[x_j + Ĝ(x_j)/G′(x_j)], ARGUED) has no prime term at the nodes: a new prime enters the form
only through the boundary strips (1.2) and in the minimizer through h*(±T) (Lemma α.1, R186_036 Lemma 2); the nodes
below T* **do not move** when a prime enters (they are the zeros: 14.135 at log 2 and ½log5 to 10⁻⁴), while the upper
ones do (40.925 → …). Reading: a prime's entry moves the nodal tail (frequency 2T, universal) and leaves the head
(zeros) fixed. A statement "the nodes move toward cos(x log n) > 0" is false at the head and vacuous at the tail. **NO-GO.**

## 5. Others (item (iii)), briefly

- Phase/harmonic measure of the nodal set (R166_501 (G), R165_201 Thm 2): this is the zero side (phases of ζ), not of Λ.
- Twisted Dirichlet sum at the nodes Σ_{n>e^{2T}}Λ(n)n^{−½−ix}φ: by the explicit formula with test e^{−u/2}φcos(xu)
 it is polar + Σ_ρ φ̃(t_ρ ∓ x): at x = γ_k (nodes below T*) the term ρ = ½ + iγ_k gives φ̃(0) = ∫φ: **the node
 "resonates" with its own zero**. This is an identity (explicit formula at the point γ_k), with no sign: it fails (c).
- Moment/Kreĭn reformulation (phase 155 round 5, R157_004 O4): Lemma 1 is its constructive version (the N-extremal
 extension of (σ_T − λ)^∨|_{(−2T,2T)} is μ_X). It proves nothing new about the indeterminacy.

## 6. Table, falsifiers, residues

| object | label | S1 | S2 | S3 | S6 | verdict |
|---|---|---|---|---|---|---|
| H_x ∈ 𝒫_T; explicit formula for H_x | PROVED | — | — | — | — | tool |
| Lemma 1 (a),(b) on V_X; (d) on (−2T,2T) | PROVED | degree 0 | no | — | — | tool (Gauss–Kreĭn) |
| (COMP) V_X = 𝒫_T | OPEN; NUMERICAL 64–99% in low-pass | | | | | hypothesis |
| nodes = zeros, w = 1 below T*; atoms −v_n/2 at log n; a = 2 | NUMERICAL | | | | | record |
| Lemma 2 (strip) | PROVED on V_X-pairs | degree 0 | yes | — | — | exact form of S2 |
| A′ | NO-GO (= D on V₀; S6 fails) | yes | yes | no | fails | closed route |
| B interlacing | NO-GO (no Sturm; do not interlace) | | | | | closed |
| C alignment | FALSIFIED (mixed signs) | | | | | closed |

**Proposed falsifiers.** (F1) (COMP): exhibit F ∈ 𝒫_T, F̂ of effective support in (γ₁, X), with
(𝔞−λ)(F) ≠ 2Σ_{x>0}w_x|F̂(x)|² by more than 1% with M ≥ 100 (today: mid-band test 0.1%; low-pass up to 36%: the
discrepancy is confined to low frequency). (F2) "nodes = zeros below T*": a window with a node below T* at
distance > 10⁻² from every γ_k or a weight w ≠ 1 ± 10⁻³ there (T = 0.9, 1.0 in mp, as in R186_040). (F3) Lemma 1(d):
an atom at log n with mass ≠ −v_n/2 by more than 5% (today 1–3% at log 2, log 3; 23% at log 4 with v₄ = log 2 small).

**Residues.** R41.1: prove (COMP) or compute the exact defect (= {G·τ^j} ∩ L², j ≥ 1, when h*(T) = 0?). R41.2:
theorem "nodes below T* = zeros" as a statement conditional on lem:roughEF + uniqueness of the representing measure
on [0, T*] (Kreĭn determinate at low height): this would be PROVED-CITED and would explain R186_040 without numerics;
it does not touch the sign. R41.3: box S2 is **formulated** (Σ_x w_x cos(x log n) − polar, log n > 2T, x ∈ X_T) and
**left blank** as an input: it is the zero side (O2) by §2(d).

**Contact with the sign: none.** λ_A > 0 in all three windows by Galerkin (known upper bounds); nothing here
bounds λ_A(T′) from below.
