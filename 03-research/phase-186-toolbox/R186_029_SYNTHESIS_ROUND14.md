# R186_029 — Synthesis of round 14 and decision of the front for round 15

Phase 186, decision round (not a construction round).
Read: README (rounds 1–14), R186_103–106, R186_028, R186_027, R186_021/102, master grid (log 13–26, §3, §4, §6, §7),
crossword (phase 186 addendum, §4.1), R185_005 (§1.3, §2.1, §3), DRAFT_SECTION_COERCIVITY_REDUCTION, Paper 47 prop:P,
note to Connes (08-sent, §6). Paper 47, grid and crossword are not touched.

---

## 1. Diagnosis: why every reduction of round 14 inherits thm:margin

**Lemma H (inheritance of the margin; PROVED, linear algebra).** Let λ_A(T) = inf{𝔞_T(F)/‖F‖² : F ∈ 𝒫_T}. Let Q_T be a
quadratic form on a space H_T obtained from 𝔞_T by any of the following operations, with constants a_T, b_T > 0
that depend only on the basis and not on the sign:
 (i) congruence Q_T = Φ*𝔞_TΦ with Φ: H_T → 𝒫_T bijective, ‖Φ‖, ‖Φ⁻¹‖ < ∞ (change of basis: Legendre, piecewise Tate,
 proper basis of A_∞, Gram matrix G_k of R186_026);
 (ii) restriction to a subspace E ⊂ 𝒫_T plus Schur complement over 𝒱 = E^⊥ with 𝔞_T|𝒱 ≥ c > 0
 (R186_019/024/025: S_{T,k});
 (iii) finite-rank modification with inertia accounting (Sylvester, Haynsworth, Sherman–Morrison; R186_026 L2.4,
 R186_028 Thm 1.2/2.1, R186_106 (★));
 (iv) relative quotient against a fixed positive part: ρ*(T) = sup C/Son_S (R186_101/021).
Then λ_min(Q_T) ∈ [a_T λ_A(T), b_T λ_A(T)] in cases (i)–(ii) (Rayleigh and the sandwich
min(c, λ_S)/(1+‖K‖)² ≤ λ_A ≤ min(c, λ_S) of R186_100/105, eq:coer-sandwich), the sign passes through exactly at (iii) with
all the T-dependence inside 𝔞_T⁻¹ (minimum positive eigenvalue ≍ λ_A; R186_028 §3), and 1 − ρ*(T) ≤ λ_A/λ_min(Son_S|𝒫_T)
in (iv). Since λ_A(T) ≤ exp(−e^{(2−ε)T}) (thm:margin, Theorem M, wall W2), **every constructive proof of the reduced
statement must decide a sign of size ≤ b_T·exp(−e^{(2−ε)T}): the reduced statement is D by window under another name.**
*Proof.* (i) Rayleigh with ‖Φ‖. (ii) 𝔞_T(e + v) ≥ 𝔞_T(e) − 2|𝔞_T(e,v)| + c‖v‖² and optimization over v; the other
inequality is the restriction. (iii) inertia invariant under congruence; the scalar criterion is ℓᵀ𝔞_T⁻¹ℓ. (iv) E_S =
Son_S − C ≥ λ_A‖·‖² ⟹ C/Son_S ≤ 1 − λ_A/Son_S. ∎

**Reading against the corpus.** Lemma H is the "per window" face of two already-proved facts: (a) the finite- and
infinite-dimensional circularity of R185_001/003 (every exclusion by linear functionals factors through a single test
and is the statement itself), assembled in BR (R185_005) for class 𝔐; (b) W11′ (R184_015): every decomposition
W_T = Pos + Δ_T with Δ_T := W_T − Pos has positivity itself as the lower half. The four reductions of round 14
(alignment law AL-k, Schur k ≍ T, piecewise Tate Gram matrix, rank-one/scalar criterion) are of types (i)–(iii);
R186_103/104/106 verified this case by case. **What survives as real gain:** Thm A/B (archimedean coercivity with
Tate, rate log(1/τ) with constant), K₁, the π norm of the coupling, the exact reduction λ_A(T) > 0 ⟺ S_{T,k} ≻ 0, the
exact index by sectors (Thm 1.2 of 028) and the spectrum of the Haynsworth block (Thm 2.1): PROVED tools, none with a
sign.

**What type of reduction escapes Lemma H.** Exactly those that are not of type (i)–(iv):
 (α) **T-free statements**: objects of the semilocal chain at the λ level (D0: λ does not depend on the window): A_S,
 F_S, Π_S, ε_S, the gap 1 − ‖A_S‖². Their theorems inherit nothing; what inherits is the final step
 "Son_{S(T)} ≥ C in 𝒫_T".
 (β) **exact decompositions with zero remainder** (infinite sum of squares with no negative term). For a single
 window this is a dual certificate (Paper 47 def:W/def:PD); uniform in T it collapses into thm:Z (the certificate is
 the explicit formula on flat-top tests). The semilocal chain is of the "positive − compact" type, not zero remainder.
 (γ) **statements nonlinear in F** (S2 of grid §7): structure of the minimizer h*_T, nodes, real-rooted witness. This
 is the (★_cell)/(TC) branch, outside 𝔐 (R185_005 O1), with the requirements (i)–(iii) of R166_190 and wall W-jet.
 (δ) **continuity/first-contact arguments in T** (phase 162 Gate 1): do not inherit λ_A but do inherit (N′) (R166_802).

---

## 2. Fronts with a defined object: mandatory evaluation (a)–(f)

Format: statement · does it inherit? · cost · corpus closure check.

**(a) W_T ≥ c on the WHOLE of L²(I_T) with β₀ = 2 exact.**
Statement: there exists a certificate (ν, 2, 0) with value c > 0 for T ∈ (½log2, ½log5] (prop:P of Paper 47: it is
the only normalization that bounds W_T on the whole of L²). **Inherits, and worse:** by (★) of R186_106 and
prop:polarcap, W_T ≥ 0 on L²(I_T) ⟺ D(T) ∧ 𝔤_ev(T) ≥ 0 ∧ 𝔤_odd(T) ≥ 0 (PROVED, two lines: W_e = 𝔞_e + u_eu_eᵀ,
W_o = 𝔞_o − u_ou_oᵀ), and 𝔤_ev ≍ λ_W‖h_ev‖² with λ_W ≪ λ_A (5.5e-8 vs 9.5e-4 at ½log3; 1e-12 vs 1.3e-7 at 0.69;
NUMERICAL R186_106 §2.2(d)). It is D plus two scalar inequalities of even smaller margin; as an intermediate goal it
is **harder, not easier**. Cost of stating it: zero (already done). Check: not closed; T ≤ ½log2 PROVED-CITED (CC Thm
6.11); for T > ½log2 Paper 47 only has thm:C with β₀ = 2.0026 (𝒫_T) and thm:log5A (𝒫_T). As a problem with no Tate
restriction it is the Kreĭn extension problem of Paper 47 §KEP: it is not a new object. **Verdict: NO as a front;
record the equivalence.**

**(b) OPEN inequality of R186_021: sup_{𝒫_T}[(ΔC − ΔSon)/E_∞] < 1, T ∈ [½log2, ½log3].**
Statement among three explicit forms (ΔC = ∫c_h κ_S with κ_S PROVED in L2_S; ΔSon via Halmos/Thm C′; E_∞ = CC's
primitive archimedean form). **Inherits** (R186_102: it is E_S ≻ 0 identically; real margin 0.65% at ½log3 and
E_∞ ≻ 0 only up to ≈ 0.58, where the inequality ceases to be well posed). The only thing not inherited is a short
stretch: with the crude bound |ΔC| ≤ ‖h‖²·‖κ_S‖_{L¹(1,e^{2T})} and λ_A(½log2) = 0.547, there is a T₁ > ½log2
(estimate: T₁ ≲ 0.40, because ΔC(s₀) ≈ 0.24 > λ_A(0.45) = 0.066) where D is proved *analytically by the semilocal
mechanism*, without a certificate. Cost: medium (needs a boundary bound on c_h near a = log 2 for h ∈ 𝒫_T;
CONDITIONAL until it is proved). Check: not closed; R185_008 closed a different partition (gap_∞ = 0.084 < 0.490 at
½log3), not this one; it belongs to the "by norms" class that R186_104 declared NO-GO beyond small T. **Verdict:
reserve, as a theorem of limited scope (T ≤ T₁).**

**(c) Lower bound of the Sonin mass in terms of an F that "sees" the comb (note to Connes §6, questions 1–2).**
Statement: Son_S(h) = ‖Π_S ϑ(g)‖²_HS ≥ Q_S(h) with Q_S an explicit quadratic form in F that contains the term of the
prime 2. **Inherits**: any useful Q_S ≤ Son_S must satisfy Q_S(u_T) ≥ C(u_T) = ρ*(T)·Son_S(u_T), i.e. be exact to
precision 1 − ρ*(T) ≍ λ_A/Son_S (Lemma H (iv)); the only Q_S that satisfies this ∀T is the identity
Son_S = 𝔞_T + ∫c_h ε_S. Check: OPEN (note to Connes); the precedent R183_029 (r_p = ρ_E − μ_D, lower bound μ_D ≤ C
OPEN) lives in the two-edge model, which R186_096 declared "measures something else". **Verdict: remains an external
question; not a front of its own.**

**(d) S(T) increasing in the semilocal chain; Λ law of R183_029; non-perturbative remainder (R186_015 §5, ARGUED).**
Statement: for S = S(T) = {∞} ∪ {p < e^{2T}} (finite for each T, so the chain of R186_015 applies as is and the whole
comb is absorbed by the additive C′_S), the density ε_{S(T)} on [1, e^{2T}] is a *folded* comb over **every** integer
n ≤ e^{2T} (each n is an S(T)-unit), with singularities of type 1/|ρ−n| cut off at scale e^{−2T}, weights
w_n ≈ λc_T²n^{1/2}(1−1/n)/4, c_T = ∏_{p<e^{2T}}(1−1/p), and ‖κ_{S(T)}‖ ~ e^{3T}/T² (ARGUED; R186_099/015 downgrade it
to CONJECTURAL in the limiting form). **Does not inherit** as a statement: it is the exact description of an object
at the λ level, without a sign (type (α) of §1); the subsequent sign step does inherit (R186_013: Son_S absorbs
infinitely many small directions; wall W-Sonin). What distinguishes it from everything else in the toolbox: it is the
only object where the Euler product of the whole window enters **before** any approximation (S7 of grid §7), and
through the multiplicative structure (S-units, smooth numbers Ψ(X, e^{2T})), not through "Λ ≥ 0 + support". Cost:
medium-high (lacunary lemma on the semigroup of S-units; log^{r−1} term in composites; Ψ → ⌊X⌋ step with control of
the boundary lines). Check: not closed; R186_015 §5 is ARGUED and R186_097/099 explicitly ask for the log^{r−1} term
and the S(T) limit. **Verdict: front.**

**(e) Outside 𝔐 per R185_005 §1.3 without NO-GO.**
 (O1) unbounded-type tests: (TC) and (★_cell) OPEN (phase 164; R166_190 (i)–(iii); W-jet). No NO-GO, but every route
 must name how it satisfies (i)–(iii); it inherits (N′), not λ_A. Very high cost; no new object since phase 169.
 (O2) zero-side inputs with Euler: "prove too much" (I6) or fall into I11; not toolbox.
 (O4) operator objects: W10 (no MW-5/h⁰ carrier). Halmos's angle operator A_S and Π_S (R186_006–009) are *real*
 operator objects built without postulating positivity: the positivity they give (Son_S ≥ 0) is tautological and the
 sign of D lives in the remainder. Residue with a statement: R157_004 O4 (Kreĭn datum at the first crossing, 7E) and
 R153_005 Thm A uniform in T (4E), never attacked (grid §6 item 59). Question 3 of the note to Connes (differential
 operator commuting with P and P̂^S): NO-GO for −𝔰²+λ²N_S and for every L + κX (R186_003/006).
 (O5) atoms outside L ∪ D ∪ C ∪ Q: exhaustiveness ARGUED; no candidate in the corpus.

**(f) Others found.**
 • Thm 4.1 of R186_026 (jump kernel 𝒢_T, conditional positivity of a 2×2 matrix kernel over finite configurations):
 PROVED reformulation, type (i) of Lemma H; inherits. OPEN only as a tool.
 • PROVED observation of 028 not yet exploited: for 0.12 ≤ T ≤ ½log5, 𝔞_T ≥ 0 on ker ℓ_ev (a single Tate condition)
 and λ_A(odd) ≫ λ_A(even) by 2–3 orders; the deficit is entirely even. Reduces the work to the even sector, but
 inherits (it is D-even).
 • Landau–Widom bilateral law (Zhu, NUMERICAL/ARGUED): a *lower* bound λ_A(T) ≥ exp(−e^{(2+ε)T}) ∀T would be D with
 quantitative content and would not inherit (it is the margin proved from below); but there is no mechanism in the
 corpus that produces doubly exponential numbers with a sign except prolate tails, and R186_021 shows that the small
 size lives in 1 − ρ*, not in a prolate tail. No object: not a front.
 • Grid §6 unattacked: I6 (3A), G2_B6_R5 Prop C (6E), O166.501.1 (7B), O164.601.1 (7F), O202.1 (6C): all on the
 witness or class side; none with a constructible object in one round.
 • NUMERICAL byproducts for the grid (not edited here): A_∞ = Γ + pole indefinite from T ≈ 0.37 (odd)/0.41 (even);
 0.4608 is only the certified bound (W11); n₋(Γ|𝒫) passes 1 → 2 at T ≈ 0.8026.

---

## 3. Recommendation

**Front of round 15: (d) — folding theorem of the semilocal chain, without T.**
The only toolbox front with a defined object, OPEN with content, that (i) is not a rewriting by window (Lemma H does
not apply), (ii) brings in the multiplicative arithmetic of the whole window, and (iii) is a prerequisite for any
answer to (c) and for the whole inertia of −C_{ε_{S(T)}} (R186_013). No sign is promised: the object is constructed.

*First concrete statement to prove (not numerical).* **Proposition P (composite coefficient).** Let
S = {∞} ∪ {p ≤ P}, r = |S| − 1, λ fixed. For every S-unit q = a/b ∈ [1,R] in reduced form, κ_S has at ρ = q the
expansion
 κ_S(ρ) = β_q log^r(1/(b|ρ−q|)) + β′_q log^{r−1}(1/(b|ρ−q|)) + O(log^{r−2}),
with β_q the formula of R186_015 (PROVED) and **β′_q explicit**: the sum over the r boundary families of the
S-unit semigroup (one per prime, v_p(N) = −1) from the lacunary lemma, each with the constant of the r − 1 case
multiplied by the weight of the missing prime. Corollary to be proved next: summing over q = n ≤ R with b = 1 and
letting P → R, the log^r part reorganizes into Σ_{n≤R} w_n(R)·φ(ρ − n) with
w_n = λc_P² n^{1/2}(1−1/n)/4 + O(c_P²/log R) (from ARGUED to PROVED; Poisson over Σ_N S(Nt) = 1/(2|t|)).
*Falsifier that kills Proposition P.* S = {∞,2,3}, λ = 1, ρ near 6 = 2·3 (with a check at ρ = 4 = 2²): if the
measured order of the singularity is not log² (but log), or if the log² coefficient differs from
β_6 = 6^{1/2}(5/6)λ²(1/2)²(2/3)²/(2·2!·log2·log3) by more than 5% on the converged grid of R186_012 (error < 1%),
the folding law is false and the front closes. Structural falsifier of the corollary: if the limiting weights at
n = 4 and n = 6 do not scale like n^{1/2}(1−1/n), Poisson folding is not the mechanism.
**Reserve: restricted (b) — theorem T₁.** Statement: there exists an explicit T₁ > ½log2 such that for
T ∈ [½log2, T₁], 𝔞_T ≥ (λ_A^{prim,∞}(T) − ‖κ_S‖_{L¹} · B_T)‖h‖² > 0 on 𝒫_T, with B_T the boundary constant of c_h at
a = log 2 (to be proved: |c_h(a)| ≤ B_T‖h‖²(2T − |a|)^{1/2} for h ∈ 𝒫_T in the form domain). It is D proved by
mechanism (not by certificate) one stretch beyond CC; falsifier: if B_T does not exist uniformly (h concentrated at
the boundary with 𝔞_T bounded) or if ‖κ_S‖_{L¹} > 0.5 already at T = 0.36, there is no stretch. It inherits the
margin from T₁ on: it is declared a result of limited scope, not a route.

**What is not done in round 15:** (a) (equivalence recorded; harder than D), AL-k/Schur/Gram/rank-one (types (i)–(iii)
of Lemma H), (c) as a construction (external question), and every route of type (γ)/(δ) without a new object that
names how it satisfies R166_190 (i)–(iii).

*No contact with the sign in round 14. Row D: OPEN.*
