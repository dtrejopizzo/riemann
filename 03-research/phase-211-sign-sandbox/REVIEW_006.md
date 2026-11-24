# Review 006: rounds 008_E and 008_C against Paper 46 and standard prolate theory

Scope. ROUND_008_E and ROUND_008_C, checked against Paper 46 (04-papers/46-row-d-sign-radial-intersection-form/main.tex: eq:symbol, eq:W,
the definitions of λ_A and λ_W on 𝒟_T, def:ext, lem:ext-mob, thm:ext-half, prop:ext-gauge, prob:ext-L, prop:ext-consol,
thm:ext-margin, lem:ext-hf, lem:monoT, lem:contA, lem:compact) and against the standard theory of the prolate spheroidal
functions (Slepian–Pollak, Landau–Widom, Fuchs). No equivalence of the window statement (★) with any other statement is
invoked. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. Verdicts on PROVED claims: CONFIRMED (key
step named) / REFUTED / DOWNGRADE. "L.n" = line n of the memo under review.

Independent computations made for this review (scratch only): Nyström discretisation of the sinc kernel sin c(x−y)/π(x−y)
on [−1, 1] (300 Gauss–Legendre nodes, double precision), giving 1 − χ_0(2) = 0.11944008 (Slepian's χ_0(2) = 0.88056
reproduced), 1 − χ_6(6π) = 7.522·10⁻⁶, 1 − χ_8(6π) = 1.2743·10⁻³, 1 − χ_8(2π·3.39) = 3.612·10⁻⁵; hence κ₆(½log3) =
9.46·10⁻⁴/7.52·10⁻⁶ = 126 and κ₈(½log3) = 0.742, κ₈(0.61) = 0.98 (memo: 126, 0.74, 0.96). Arithmetic re-check of the
table of ROUND_008_C §5 (ratios −λ′/λ, 8πe^{2T}, law values, |λ′|/|Arch′|) at T = 0.7, 1.0, 1.2: all reproduce.

---------------------------------------------------------------------------------------------------------------------
## 1. ROUND_008_E

**§1.1 the exact defect (L.42–47).** CONFIRMED. The identity dχ_k/dc = 2χ_k ψ_k(1)²/c with ψ_k of unit norm in L²(−1, 1)
is the standard Slepian derivative formula, so ∂_c log χ_k = 2ψ_k(1)²/c is correctly normalised; the convention c = 2π·λ·λ
for the self-dual square [−λ, λ] × [−λ, λ] under ℱf(ξ) = ∫f e^{−2πixξ} agrees with thm:ext-margin, and 2c = 4πN gives the
rate e^{−4πN}. The value χ_0(2) = 0.88056 is reproduced above. The leading asymptotic 4√π c^{1/2}e^{−2c} is the one
cited in thm:ext-margin; the first-correction coefficient −7/(16c) is not checked here (the four ratios quoted are
consistent with a coefficient between 0.44 and 0.5) and nothing depends on it. The table entry 1 − χ_0(6π) = 1.27·10⁻¹⁵
agrees with the asymptotic times the quoted correction.

**§1.2–1.4 data, fit, index 8 (L.49–98).** NUMERICAL, correctly labelled. The κ₆ and κ₈ entries at the two smallest
windows are reproduced by the independent computation. The reading "index 8 = 2·4 constraints" (L.94–98) is an
interpretation; its proved content is only the upper-bound count of Proposition 3.3 (see below).

**§2 test functions and Ritz block (L.100–156).** NUMERICAL, correctly labelled. Two remarks. (a) The parity statement
(L.144–146) is exact only at the level Φ_f(−x) = Φ_{ℱf}(x) for admissible f (Poisson, def:ext); the transfer to "ℱ-even
prolates" uses ℱ(ψ_k1) = i^k√χ_k ψ_k on the band, which fails off the band by O((1 − χ_k)^{1/2}); so "only ψ_0, ψ_4, ψ_8
enter" is a numerical statement at precision 10⁻⁴ (L.144), not a structural one; ARGUED. (b) The explanation in L.116–120
of why PEψ_0 fails is ARGUED and plausible: P removes the L²-orthogonal projection of span{e^{±x/2}}, not the two Poisson
correction terms.

**Theorem 3.1 (L.170–193), exterior upper bound.** CONFIRMED, with the label to be read "PROVED, given thm:ext-half,
itself given Guo2026 Lemmas 4.2–4.4 and Thm 4.5". Hypotheses: 𝒜⁺_T ⊂ admissible (def:ext asks even, support in [−λ, λ], C²,
f(0) = ℱf(0) = f(λ) = 0; 𝒜⁺_T adds f′(λ) = 0), so thm:ext-half is used inside its hypotheses. Every constant checked:
(a) ‖r(n·)‖_{L²(W,∞)} = n^{−1/2}‖r‖_{L²(nW,∞)} ≤ n^{−3/2}W^{−1}L₁, Σ n^{−3/2} = ζ(3/2), and ∫|Ψ̌|²dy = ∫|ρ|²dw under w = e^y
(Ψ̌(y) = e^{y/2}ρ(e^y) is exactly Zr of def:ext). (b) Ψ̌′ = ½Ψ̌ + e^{3y/2}ρ′(e^y), ∫e^{3y}|ρ′(e^y)|²dy = ∫w²|ρ′|²dw, and
∫_λ^∞ w²|r′(nw)|²dw ≤ n^{−5}λ^{−2}L₂², so ‖wρ′‖ ≤ ζ(3/2)L₂/λ. (c) Under the convention F̂(τ) = ∫F e^{iτt} of eq:symbol,
|ê|² = (1 + τ²)^{−1} for e = e^{−(y−T)}1_{y>T}, Plancherel has the factor 1/2π, m ≤ log(2 + |τ|) + C_∞ (m = Re ψ(¼ + iτ/2) −
log π), and J² = −∫(Ψ̌²)′ ≤ 2‖Ψ̌‖‖Ψ̌′‖. (d) With 𝒲 as in def:ext the comb is −Σ v_n c_Ψ(log n), v_n = 2Λ(n)/√n, so
Σ v_n n^{−1} = 2(−ζ′/ζ)(3/2), as written. (e) ∫_X^∞|r| ≤ X^{−1/2}L₁ by Cauchy–Schwarz; ∫Ψ̌e^{y/2} = ∫ρ dw, ∫Ψ̌e^{−y/2} = ∫ρ dw/w.
One inaccuracy without consequence: L.163–164 says ξ²r ∈ L², which is not needed; what is used is ξr ∈ L² (f′ ∈ L²) and
ξ²r′ ∈ L² ((xf)″ ∈ L², which needs (xf)′ continuous at ±λ, i.e. f′(λ) = 0: this is the reason for the extra edge
condition, and it is correctly built into 𝒜⁺_T).

**Corollary 3.2 (L.195–200).** CONFIRMED. Key step: ‖E^{−1}‖ ≤ 2√N (lem:ext-mob) and λ^{−2}·4N = 4. Ef lies in 𝒟_T (it is
bounded and piecewise C¹; a jump at −T has finite log energy), and A(Ef) = B(Ef) = 0 puts it in P_T ∩ 𝒟_T, which is the
set over which Paper 46 takes λ_A.

**Proposition 3.3 (L.202–216), index count.** CONFIRMED as stated. (i) Four linear functionals f(0), ℱf(0), A(Ef), B(Ef)
on a space of dimension ≥ 5 have a nonzero common kernel; (ii) two functionals on dimension ≥ 3. Correction to (ii): the
memo defines λ_W over a "core" and then repairs to the form-domain closure (L.209–211); Paper 46 defines λ_W directly as
the infimum over 𝒟_T (eq:W and the display after it), so Ef ∈ 𝒟_T suffices and the repair is unnecessary; with the
memo's own definition the repair is supplied by the density statement inside thm:ext-margin. On the question asked:
the count is right as an upper-bound count. For even f there are exactly four constraints for λ_A (two admissibility, two
Tate) and two for λ_W, so a test space of even edge-regular functions of dimension 5, resp. 3, is the minimum that the
argument needs; with V = span of (tapered) ψ_0, ψ_2, …, ψ_{2d−2} the worst leakage in V is 1 − χ_{2d−2}, giving indices 8
and 4. The parity refinement (L.215–216: {ψ_0, ψ_4, ψ_8} with two constraints) is consistent with this count (the
ℱ-odd pair ψ_2, ψ_6 absorbs the two antisymmetric combinations) but is ARGUED, by §2 remark (a). The sentence "the count
is the whole content of the indices 8 and 4" (L.213) is an interpretation: the count proves nothing about a lower bound
with index 8, and the indices are attained only through Lemma 3.4.

**Lemma 3.4 (L.218–232).** ARGUED, correctly labelled. Two points to add to the "what is missing" list: the taper width
1/λ is of the same order as the edge scale λ/c of ψ_j in unnormalised units, so the C₂λ² and C₃λ³ derivative costs enter
L₂ at full strength and the exponent b must absorb them; and the tapered functions are no longer doubly orthogonal, so
the cross terms between η_λψ_i and η_λψ_j in the weighted leakage must be bounded, not only the diagonal.

**Corollary 3.5 (L.234–237).** CONDITIONAL on Lemma 3.4, correctly labelled. The ratio (1 − χ_k)/(1 − χ_0) ≍ (8^k/k!)c^k is
the Fuchs asymptotic and holds only as c → ∞; at c = 6π it is off by a factor of about 7 for k = 8 (asymptotic κ₈(½log3)
would be 0.11, exact 0.74), which is absorbed in C′ but should be stated.

**Proposition 4.2 (L.252–256).** CONFIRMED (transfer, CONDITIONAL on eq:ext-L). Key step: thm:ext-margin already contains
the passage from the core to 𝒟_T, and λ_A ≥ λ_W because the forms agree on P_T.

**Lemma 4.3 (L.261–265).** CONFIRMED. Key step: D(f) = D(f_<) + D(f_≥) ≥ d_q‖f_≥‖² (D diagonal) and ‖f_<‖ ≤
‖(C|_{H_<})^{−1}‖‖C‖‖f_≥‖. The application (L.266–275) is correctly CONDITIONAL on the conditioning κ_C(T): ℱf(0), A(Ef),
B(Ef) are L²-continuous and gauge-invariant, the leakage is diagonal in the prolates of [−λ, λ] (complete there), and the
next even index after {0, 2, 4} is 6. The statement "the gauge costs exactly the f(0) constraint" is ARGUED (it shows that
this method stops at 6, not that index 8 is unreachable from below).

**L.277–287 (prolate reading of the lower half).** ARGUED. The sentence "(eq:ext-L) holds numerically with A_0 = 0 and
κ ≈ 1 on the low block" compares W_T with the leakage of the raw representative, which majorises ℓ; the direction is right
(W ≥ κ·leak implies W ≥ κ·ℓ) but the raw ψ_k are not admissible, so the comparison is NUMERICAL on non-admissible vectors.

**Identity (5.1) (L.291–296).** CONFIRMED, and tautological: with thm:ext-half it reads W^w_T(Ef) = W_T(Ef) + 𝒫_{Λ−w}[Ef],
which is the definition of W^w on the window. It carries no information beyond Theorem 3.1.

**Proposition 5.1 (L.298–301).** CONFIRMED for the two inequalities (a^w_T = a_T + 𝒫_{Λ−w} on P_T; evaluate at F★, take the
infimum; lower bound by the operator norm). DOWNGRADE of the last clause: "for w = cΛ the law survives only for
|1 − c|·|Π_T(F★)| ≤ λ_A + ε" follows from the upper bound only when (1 − c)Π_T(F★) < 0, i.e. for c > 1 since Π_T(F★) > 0
(0.0331, 0.0152 at T = 1, 1.2). For c < 1 the upper bound gives no negativity at F★; the negativity for c < 1 in the
table (L.307–310) comes from other block vectors and is NUMERICAL.

**Falsifier table and test (L.303–325).** NUMERICAL, correctly labelled; the logic of the falsifier test is sound (the
proved upper bounds are Λ-specific through Poisson summation and Λ ∗ 1 = log, and no sign step is claimed).

**Question: is anything PROVED that uses thm:ext-half outside its hypotheses?** No. Theorem 3.1, Corollary 3.2 and
Proposition 3.3 apply thm:ext-half only to f ∈ 𝒜⁺_T ⊂ admissible. Ef itself is not required to be in the core. Identity
(5.1) and Proposition 5.1 do not need thm:ext-half (5.1 is the definition of W^w). §2 applies E to raw prolates, which are
not admissible, but only in NUMERICAL statements, and the memo itself notes that thm:ext-half does not apply there.

Summary for 008_E. CONFIRMED: §1.1 normalisation, Theorem 3.1 (given thm:ext-half / Guo2026), Corollary 3.2, Proposition
3.3 (as an upper-bound count; (ii) simplified by Paper 46's definition of λ_W), Proposition 4.2, Lemma 4.3, identity
(5.1) (tautological), Proposition 5.1 inequalities. DOWNGRADE: last clause of Proposition 5.1 to c > 1 (c < 1 NUMERICAL);
parity statement of §2.2(ii)/(iii) to ARGUED + NUMERICAL. REFUTED: none.

---------------------------------------------------------------------------------------------------------------------
## 2. ROUND_008_C

**(1.1) (L.48–53).** CONFIRMED. For X in the form domain write X = X_P + A(X)p_A + B(X)p_B with X_P ∈ P_T ∩ 𝒟_T (the Tate
exponentials lie in 𝒟_T); the Euler–Lagrange equation handles X_P, the Riesz definition handles 𝒯_T, and the cross terms
vanish because F ⊥ 𝒯_T and ρ_F ∈ 𝒯_T ⊥ X_P.

**Lemma 1.2 (L.58–60).** CONFIRMED. Key step: Re ψ(x + iy) − ψ(x) = Σ_k y²/((k + x)((k + x)² + y²)), increasing in y² for
x = ¼; m in eq:symbol is exactly Re ψ(¼ + iτ/2) − log π, so m′ ≥ 0 on [0, ∞) and τm′(τ) ≥ 0 on ℝ (m even); τm′ → 1 and
τ(τm′)′ = O(τ^{−1}) at infinity, both continuous, so M₁, M₂ < ∞.

**Theorem 1 (L.76–114).** (a) CONFIRMED under (R_F). Key steps: Arch(U_rF) = (1/2π)∫m(τ/r)|F̂|², c_{U_rF}(u) = c_F(u/r);
c_F(2T − ε) = εF(T⁻)F(−T⁺) + o(ε) gives the fold +s⁺·2Tv_{n₀}FF inside Π, hence −h⁺φ in a; A(U_rF) = r^{1/2}∫F(e^{rt/2} −
e^{t/2}) = sA₁ + O(s²) and B(U_rF) = sB₁ + O(s²) with the stated signs of A₁, B₁; the repair costs −2s[A₁a(F, p_A) +
B₁a(F, p_B)] = −sτ(F). The only continuity input, a_{rT}(U_rF, p_A^{(rT)}) → a_T(F, p_A), holds because U_r^{−1}p_A^{(rT)} − p_A^{(T)}
is O(s) in sup norm with jumps of size O(s) at ±T, whose log energy is O(s²). (b) CONFIRMED: the right Dini bound is the
infimum over F of the right side, the left one the supremum; the h < 0 branch has no fold. (c) CONDITIONAL on (U),
correctly labelled, with two repairs. First, the proof (L.110–112) writes the lower bound as "−max 𝒱^♯/T − max φ", which
does not match the upper bound −max(𝒱^♯/T + φ); the argument actually gives −(𝒱^♯(F)/T + φ(F)) at the limit F, which is
≥ −max(𝒱^♯/T + φ), and that is what closes the equality (with the fold of the dilation from T_k to T supplied by the
continuity of φ in (U)). Second, the "iff" of L.85 is DOWNGRADED: at a contact threshold with an eigenspace containing
vectors with φ < 0 (odd or mixed parity), max(𝒱^♯/T + φ) = min 𝒱^♯/T is possible without 𝒱^♯ constant and φ ≡ 0; off
contact thresholds (φ ≡ 0) the "iff" and the concave-corner statement are correct.
Label remark: (R_E) is not known for the true minimiser (L.66–67), so "PROVED under (R_E)" is CONDITIONAL in substance; the
memo says so.

**Corollary 2.2 (L.116–119).** CONFIRMED (under (R_E)). Key step: lem:monoT makes every left difference quotient ≤ 0, so
D₋λ ≤ 0, and (b) gives D₋λ ≥ −𝒱^♯(F)/T for each F. The fold signs follow from F(−T⁺) = ±F(T⁻).

**Proposition 2.3 (L.121–126).** CONFIRMED. (i) zero extension preserves A, B and a (lem:monoT); (ii) is Step 2 of Theorem 1
(under (R_F)); (iii) is a description of (3.1). Label: (ii) inherits (R_F).

**Proposition 3 (L.139–158).** The algebra is CONFIRMED: a_T(G♯) − λ′‖G♯‖² equals 𝔈_h exactly, using ⟨F, R⟩ = ‖R‖²,
⟨F, q⟩ = ⟨G, q⟩, a_T = a_{T′} on functions supported in I_T, and |A(R)| ≤ e^{T′/2}(2h)^{1/2}‖R‖. DOWNGRADE of the headline
label: the header (L.139, "PROVED; no regularity of F") and §0(iii)(a) ("regularity-free") contradict L.157–158. The step
G = F·1_{I_T} ∈ 𝒟_T is the restriction property for the log-order Lévy form, PROVED only when F is bounded near ±T (the
killing weight ≍ log(1/dist) is then integrable) and ARGUED otherwise; boundedness of the minimiser near ±T is not known
(R186_036 §4). Correct label: CONDITIONAL on the minimiser at T + h being bounded near ±T (or on the restriction property).
Also needed and unstated: G♯ ≠ 0 (true for h small since ‖R‖, ‖q‖ → 0).

**Corollary 3.1 (L.160–164).** CONFIRMED conditionally (under (R_E) and the hypothesis of Proposition 3); ‖R‖ → 0 follows
from L²-precompactness of the minimisers at T + h (lem:compact, lem:contA).

**§3 Hadamard reading (L.166–173).** ARGUED, correctly labelled; the boundary decay F ≍ θ(log 1/δ)^{−1/2} is stated as
quoted from memory and must not be used downstream.

**Proposition 4 (L.177–187), discrete Grönwall.** The statement is CONFIRMED; the proof as written is DEFECTIVE and must
be replaced. The step "since λ_A is non-increasing, the inequality holds on [T₁, T₁ + h] up to o(h)" (L.183–184) uses
monotonicity in the wrong direction: for S ∈ (T₁, T₁ + h) one only has λ_A(S) ≥ λ_A(T₁ + h), while the target
L(S) − ε(S − T₀) is larger than its value at T₁ + h, and for S close to T₁ the available bound λ_A(T₁) − C(T₁)λ_A(T₁)h does
not dominate it when equality holds at T₁. Repair: put u(T) = λ_A(T)exp(∫_{T₀}^T C). Where λ_A > 0, (EB_C) gives, along
the admissible sequence h_k ↓ 0, λ_A(T + h_k)(1 + C(T)h_k + o(h_k)) ≥ λ_A(T), and exp(∫_T^{T+h}C) = 1 + C(T)h + o(h)
(C continuous), so u(T + h_k) ≥ u(T)(1 + o(h_k)); whence the upper right Dini derivative of u is ≥ 0. u is continuous (lem:contA);
a continuous function whose upper right Dini derivative is ≥ 0 at every point is non-decreasing (classical; apply it to
u + εT, whose upper right Dini derivative is ≥ ε > 0, and pass to the supremum of the set where u + εT ≥ u(T₀) + εT₀).
Run this on the maximal interval [T₀, T₂) on which λ_A > 0; u ≥ u(T₀) > 0 there, so λ_A(T₂) > 0 by continuity, and T₂ = ∞.
With this proof the statement holds exactly as written (only continuity of λ_A is used).

**Proposition 5 (L.189–203).** (i) DOWNGRADE of the wording, not of the content. What is proved is one direction:
(★) strict on [T₀, ∞) plus local Lipschitz continuity of λ_A implies (EB_C) for some continuous C; the converse direction
is Proposition 4, which gives (★) but not Lipschitz continuity. So "(EB_C) is (★) plus local Lipschitz" (L.192) is a
sandwich, not an identification; and local Lipschitz continuity of λ_A is itself not known (Theorem 1 gives one-sided
bounds only under (R_E)). Notation: the quantity limsup_{h↓0}(λ(T) − λ(T + h))/(hλ(T + h)) is minus the lower right
logarithmic Dini derivative, not D₋. (ii) CONFIRMED: at the first zero T_c the right side of (EB_C) is (Ch + o(h))λ_w(T_c + h)
< 0 for small h while the left side is −λ_w(T_c + h) > 0 (monotonicity holds for every weight, by zero extension).
(iii) The first sentence is CONFIRMED under (R_E) (on E_T, 0 ≤ 𝒱^♯ ≤ TCλ_A forces λ_A ≥ 0); the Euler-step reading is
ARGUED, correctly labelled.

**Proposition 6 (L.255–263).** CONFIRMED conditionally (under (R_E), simple bottom, and the hypothesis of Proposition 3):
it is Theorem 1(c) for one-dimensional E_T plus Corollary 3.1.

**§4 answer and §6 reading (L.205–212, L.265–274).** The NO-GO for the Grönwall route in the window variable is a
restatement NO-GO and coincides with the recorded class 𝒦_H (H_001) and R186_038 α.3; the memo re-examined it with a stated
new reason (Tate multipliers, eigenspaces, absolute continuity, measured constant), which satisfies the index rule. The
claim "no structured weaker statement exists" (L.210–212, L.313) is ARGUED, not proved. The identification
C_T = 2c·C_c with c = 2πe^{2T}, so 8πe^{2T} ↔ 2 (L.32–35), is CONFIRMED arithmetic.

**§5 numerics (L.214–251).** NUMERICAL, correctly labelled; the reported ratios reproduce. The T = 1.1 row is unconverged
(acknowledged). The Hellmann–Feynman agreement checks the variation formula inside the Galerkin model only, where (R_E)
holds trivially and the fold is invisible; it is not evidence for (R_E) for the true minimiser (the memo says so, L.239–241).

Summary for 008_C. CONFIRMED: (1.1), Lemma 1.2, Theorem 1(a)(b) under (R_E), Corollary 2.2, Proposition 2.3, the algebra of
Proposition 3, Corollary 3.1 (conditional), Proposition 4 (statement; proof replaced above), Proposition 5(ii), 5(iii)
first sentence, Proposition 6 (conditional). DOWNGRADE: Theorem 1(c) "iff" at contact thresholds; Proposition 3 header to
CONDITIONAL on boundedness of the minimiser near ±T; Proposition 5(i) from identification to one-sided implication.
DEFECTIVE PROOF (statement survives): Proposition 4. REFUTED: none.

---------------------------------------------------------------------------------------------------------------------
## 3. NO-GO register

- 008_E: upper half of the margin law with the single test function PEψ_0 — NO-GO, NUMERICAL (quotient 0.12–0.26 at
  T = 0.8–1.2, angle 63–75°); confirmed as numerical, mechanism ARGUED.
- 008_E: robustness of the margin law under w = cΛ — first-order failure PROVED for c > 1 (Proposition 5.1 at F★),
  NUMERICAL for c < 1, a_P and finite modifications.
- 008_E: lower-half index improvement by constrained leakage (Lemma 4.3 route) stops at index 6 — ARGUED (the gauge removes
  f(0) = 0); conditional on polynomial conditioning κ_C(T), OPEN.
- 008_C: Grönwall in the window variable (D ≤ Cλ_A, (EB_C), (VE_C)) — NO-GO as restatement, already in class 𝒦_H; with
  C = 8πe^{2T}(1 + o(1)) the inequality (EB_C) is OPEN and stronger than (★).
- 008_C: weaker structured version of the Grönwall inequality — ARGUED absent (ratio of two cancellations at relative
  precision C·T·λ_A).

Open items passed on. Lemma 3.4 of 008_E (archimedean; include cross terms of tapered prolates and taper-derivative costs);
(R_E) and boundedness of the minimiser near ±T for 008_C; polynomial conditioning κ_C(T); eq:ext-L.
