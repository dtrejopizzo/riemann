# K12_DAMPED_001 — (Ω_{t₀}): the damped comb is the chord toward ρ_κ, not the line cΛ; Lemma E.2 resolved (limsup form empty, liminf form ⟺ (E_γ)); K12 → TRANSFER on packets (phase 204j)

Pure mathematics; numerical only on already-recorded data (NUMERICAL).
Notation from N_BUILD_011/012 (phase 188): P_T, 𝔞_T = 𝔞^♯ − 𝓕_T (window form of Λ, 𝔞^♯ = G_1, 𝓕_T
Chebyshev fluctuation), m, m^♯ = m + 1/(¼+τ²), C₀ = m(0) = −2ζ′/ζ(½) = −5.37218…, g_κ = m + κ/(¼+τ²),
G_κ(F) = (1/2π)∫g_κ|F̂|², κ* = sup_{m<0}(−m)(¼+τ²) ≥ |C₀|/4 ≈ 1.343, η_κ = inf g_κ > 0 for κ > κ*.

## 0. Index and corpus check

grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` and `03-research/` for «Ω_{t», «t_∞», «damped comb», «tΛ», «cΛ»,
«Lema E.2», «N_013», «E_γ», «cor:Tarch», «O4ε», «λ_{∞,P}», «Danskin». Findings:
- 06_ **R3** (Ω_{t₀}) OPEN, with dead sub-routes N_012 (decomposition, NO-GO), N_013 (packets, CONDITIONAL collapse),
  N_014 (two-copy families, ARGUED; Thm A "Ξ unbounded ⇒ t_∞ = 0"), N_015 (Thm L, NO-GO of Λ ≥ 0).
- 04_ l.178 (N_012: "weaker but not separable"), 06_ **R5** (E_γ), TRACT_E_PHASES_001 §3.2 (K12, Lemma E.2), README l.599.
- AUDIT_203_001: line cΛ, λ_A(0·Λ) = λ_{∞,P}(T) < 0 for T ≥ 0.60 (P46 cor:Tarch), slope −0.063 at c = 1 at ½log15,
  (1+ε)Λ < 0 for ε > 8·10⁻⁶⁹; Danskin only gives upper bounds.
- "Lemma E.2" does not appear attacked in any memo; "damped comb" only in TRACT_E. **New reason, written out** (required
  against cΛ): the object of K12 is NOT cΛ (see §1); the family λ_t = (1−t)ρ_κ + tΛ starts at an *interior* point of Pos
  (b_T(0) ≥ η_κ > 0 uniform in T, N_011 PROVED), while cΛ starts at 0 ∉ Pos_T for T ≥ 0.60. AUDIT_203's falsifier does
  not apply. Against N_013, the new reason was that of TRACT_E §3.2(e): "the slack (1−t)G_κ could contradict
  criticality." §3 of this memo shows that it does **not** contradict it: the collapse of N_013 does not depend on the
  value of the limit but on its existence.

## 1. Task 1: exact definition; relation to the line cΛ

**Definition (N_BUILD_011 Prop 3, N_BUILD_012 §1; PROVED as a reformulation).** Fix κ > κ*, let ρ_κ be the continuous
comb of density κ·2e^{u/2} (main term multiplied by κ; the main part of Λ is ρ_1). For t ∈ [0,1]:
 λ_t := (1−t)ρ_κ + tΛ,  𝔞_t(F) := 𝔞_T^{(λ_t)}(F) = (1−t)G_κ(F) + t·𝔞_T(F),  b_T(t) := inf_{F∈P_T, ‖F‖=1} 𝔞_t(F).
(The identity uses that the form is affine in the comb with the archimedean part of coefficient (1−t)+t = 1.)
 t*(T) := sup{t ∈ [0,1] : b_T(t) ≥ 0},  t_∞ := lim_{T→∞} t*(T)  (exists: t* non-increasing in T, N_012 §1(a)).
 **(Ω_{t₀})**: t_∞ > 0; equivalently (N_012 §2, PROVED) S := sup_{T, F∈P_T} [𝓕_T(F) − 𝔞^♯(F)]₊ / G_κ(F) < ∞,
 with t_∞ ≥ 1/(1+S).

**Relation to cΛ.** cΛ = (1−c)·0 + cΛ is the chord from the null comb, whose form is the pure archimedean one with
bottom λ_{∞,P}(T) < 0 for T ≥ 0.60 (cor:Tarch). λ_t is the chord from ρ_κ, with bottom ≥ η_κ > 0 for every T. The two
chords are distinct and λ_t − tΛ = (1−t)ρ_κ: **K12's damped comb is tΛ plus a fraction (1−t) of the reinforced main
term κ > κ*** — not a global factor. Hence:
- AUDIT_203 (c ↦ λ_A(cΛ) negative at c = 0, interior maximum, ≈ 0 at c = 1) **does not falsify K12**: it is not about λ_t.
- The chord cΛ is λ_t with κ = 0 < κ*, which is explicitly excluded from the definition (ρ_0 ∉ Pos).
- For λ_t, concavity (b_T is an infimum of affine functions in t, PROVED) gives {b_T ≥ 0} = [0, t*(T)] — an interval
  containing 0 for every T. There is no "small negative t" regime: b_T(t) ≥ (1−t)η_κ − t(A_T + 4 + |C₀+4|) > 0 for
  small t (N_011 §4). The "for all T" statement is meaningful and nonempty at each T; what is open is the
  *uniformity* t*(T) ≥ t₀.

Conclusion §1: the premise of the brief (K12 = λ_A(tΛ) ≥ 0) is incorrect; K12 damps *toward ρ_κ*. Consistent.

## 2. Task 2: weaker than D — verification

(i) D ⇒ (Ω_{t₀}): D at T gives b_T(1) ≥ 0; with b_T(0) ≥ η_κ and concavity, b_T ≥ 0 on [0,1], t*(T) = 1 ∀T, t_∞ = 1 > 0. PROVED.
(ii) Trichotomy (N_012 §1(c), PROVED; re-verified): D ⟺ t_∞ = 1. (⇐): if D fails at T₀ with F₀, 𝔞_{T₀}(F₀) = −c < 0;
since P_{T₀} ⊂ P_T for T ≥ T₀ and the form of F₀ does not depend on T, 𝔞_t(F₀) = (1−t)G_κ(F₀) − tc < 0 for
t > t₁ = G_κ(F₀)/(G_κ(F₀)+c) < 1, hence t_∞ ≤ t₁ < 1. ∎
(iii) "Strictly weaker": what is PROVED is that (Ω_{t₀}) is implied by D and that t_∞ ∈ (0,1) is not excluded by any
argument on record. **Label correction:** "strictly weaker" in the sense that *no converse implication is known* is
correct; in the sense of "there exists an admissible comb with t_∞ ∈ (0,1)" it is given by the following
**Lemma 2.1 (PROVED, new).** Let δ be a finite modification of the comb (finite support, bounded weights). Then
(Ω_{t₀}) for Λ ⟺ (Ω_{t₀}) for Λ + δ.
*Proof.* |⟨δ, c_F⟩| ≤ ‖δ‖₁·sup|c_F| ≤ ‖δ‖₁ ‖F‖² ≤ (‖δ‖₁/η_κ) G_κ(F). So S changes by at most ‖δ‖₁/η_κ. ∎
Consequence: if (Ω_{t₀}) holds for Λ, it holds for Λ + cδ_N with c > 0 large, and those combs violate D on finite
windows (cor:void/thm:finmod); for them t_∞ ∈ (0,1). Thus "strictly weaker" is PROVED as a statement about the class
of combs (conditional only on (Ω_{t₀}) holding for some comb, which is true for ρ_{κ′}, κ′ > κ*, N_011 Cor 2, plus
finite modifications). Exact Λ enters (Ω_{t₀}) **only in the tail**: it is a tail statement, insensitive to cor:void.

## 3. Task 3: Lemma E.2 — exact statement and resolution

TRACT_E §3.2(f) states: for κ > κ*, t < 1 and concentrating packets F_T = F_T^γ (‖F_T‖ = 1),
 limsup_T 𝔞_t(F_T) ≥ (1−t)·c(κ,γ) > 0.
Two versions must be separated; only one is relevant for (Ω_{t₀}) (which calls for *infima*, i.e. liminf).

**Step 1 (PROVED, lem:wit-conc).** G_κ(F_T) → g_κ(γ) ≥ η_κ and 𝔞^♯(F_T) → m^♯(γ).
**Step 2 (N_013 §1, PROVED with CITED inputs).** If the smoothed means of Re Σ2Λ(n)n^{−½−iγ} (scale T) converge,
𝓕_T(F_T) → m^♯(γ), so 𝔞_T(F_T) → 0 and
 lim_T 𝔞_t(F_T) = (1−t)·g_κ(γ).
**Step 3 (N_013 §2, CITED Hardy–Riesz + ARGUED contour).** If they do not converge, 𝔞_T(F_T) oscillates with
amplitude growing exponentially in T and with both signs: limsup = +∞, liminf = −∞.

**Proposition 3.1 (limsup version).** limsup_T 𝔞_t(F_T) ≥ (1−t)g_κ(γ) for every t < 1. CONDITIONAL (on N_013 §2; in
the convergent case PROVED). **Empty**: it holds on both branches, so it distinguishes nothing and is not an input
for (Ω_{t₀}).

**Proposition 3.2 (liminf version; the relevant one).** For fixed t ∈ (0,1):
 liminf_T 𝔞_t(F_T^γ) ≥ (1−t)·g_κ(γ) > 0 ⟺ (E_γ) ⟺ (E_γ, C) for any C ≥ 0.
*Proof.* 𝔞_t(F_T) = (1−t)G_κ(F_T) − t[𝓕_T − 𝔞^♯](F_T). That liminf 𝔞_t(F_T) > −∞ is equivalent to
limsup[𝓕_T − 𝔞^♯](F_T) ≤ ((1−t)/t)g_κ(γ) + o(1), which is (E_γ, C) with C = (1−t)/t (N_013 normalization). By N_013
Thm 3 (CONDITIONAL), (E_γ, C) ⟺ (E_γ), and in that case we are in the convergent branch (Step 2), which gives the
exact value. ∎
Label: **CONDITIONAL** (same CITED/ARGUED inputs as N_013 §2–§3).

**Reading.** TRACT_E's hypothesis ("if ρ_κ's contribution exceeds m^♯(γ), the collapse for t < 1 leaves slack
(1−t)δ(γ) and would contradict criticality") is **false as a mechanism**: in the convergent branch the slack exists
(Step 2) and contradicts nothing — criticality belongs to 𝔞_T, and (1−t)g_κ is added on top; in the divergent branch
the slack is O(1) and the divergence is e^{2T(β−½)}·(…): no constant absorbs it. **The collapse of N_013 is a
convergence/divergence dichotomy, not an equality of values, and the margin O(1−t) does not act on the dichotomy.**
Hence Lemma E.2 is resolved: limsup form PROVED-empty/CONDITIONAL; liminf form ⟺ (E_γ) (CONDITIONAL). The collapse of
N_013 **does apply** to every t < 1.

**Corollary 3.3 (CONDITIONAL).** (Ω_{t₀}) ⇒ (E_γ) for every γ ∈ ℝ.
*Proof.* t_∞ > 0 ⇒ for t₀ < t_∞, 𝔞_{t₀}(F) ≥ 0 on all of P_T ⇒ liminf 𝔞_{t₀}(F_T^γ) ≥ 0 > −∞ ⇒ Prop 3.2. ∎
Thus K12 contains the entire family {(E_γ)}_γ, each one critical and each of the strength of R5. The other admissible
directions of R3 (non-convergent spectral measure families, N_013 §5) are not touched here.

**Where exact Λ / filters enter.** (a) Finite modifications (cor:void): they pass (Lemma 2.1) — consistent, K12 is a
tail statement. (b) cΛ, c ≠ 1: the chord (1−t)ρ_κ + tcΛ coincides with that of Λ except for the mass of the main
term; in packets this shifts the limit by t(c−1)·(1/(¼+γ²) − …) bounded, so the packet criterion does not separate it
from Λ (ARGUED); it is not a falsifier of anything. (c) Epstein / Davenport–Heilbronn: they have the divergent branch
at the frequencies associated with their off-line zeros, so, by the mechanism of Step 3, t_∞ = 0 for them (ARGUED,
same contour as N_013 §2). That is: K12 discriminates between ζ and DH/Epstein exactly through N_013's branch, which
is the same information as (E_γ).

## 4. Task 4: the (E_γ)/N_013 blockage and whether O(1−t) evades it

What it is: N_013 Thm 3, (E_γ, C) ⟺ (E_γ) ∀C, because (E_γ, C) with finite C excludes the divergent branch and in the
convergent branch the limit is exactly m^♯(γ) (boundary value of Re ξ′/ξ = 0 on the line, CITED). Why CONDITIONAL: the
implication "summability at one point ⇒ summability in the half-plane" is CITED (Hardy–Riesz) and the description of
the divergence (exponential amplitude, both signs) is ARGUED (contour shift not written out).
Does O(1−t) evade it? **No** (Prop 3.2). The margin O(1−t) does evade W2/thm:margin and Cor 2′ *as a statement* (with
(Ω_{t₀}), b_T(t₀/2) ≥ ½η_κ·(…) uniform; ARGUED that Cor 2′ does not apply because its hypothesis λ_T ≤ exp(−e^{2T})
fails), but the current blockage is not W2 but packet criticality, and that is not quantitative: it is binary.
Closing N_013's conditional (writing out the contour) **would worsen** K12, not improve it: it would turn Cor 3.3 into
PROVED.

## 5. Task 5: input for D — honest assessment

b_T(t) is concave in t (PROVED). From b_T(t₀) ≥ 0 and b_T(0) ≥ η_κ, concavity gives b_T ≥ 0 on [0,t₀] (already known)
and, at t = 1, only the **upper** bound b_T(1) ≤ b_T(t₀) + (1−t₀)b_T′(t₀⁺) (supergradient). No lower bound at 1
follows from data at t₀: this is exactly the phenomenon of INVENT Theorem 2.3 / AUDIT_203 §1 (Danskin: tangents bound
from above; lower bounds only come from chords, and the chord through t = 1 needs b_T(1)). Counterexample in
principle: Λ + cδ_N (Lemma 2.1) satisfies (Ω_{t₀}) if Λ satisfies it and violates D. **Hence (Ω_{t₀}) ⇏ D, and no
"interpolation t₀ → 1" using only (Ω_{t₀}) + concavity + properties stable under finite modification can close D
(PROVED, by Lemma 2.1).**
What a proved K12 would contribute (honest list):
1. Corollary A′ of N_014 with a constant: limsup_d Ξ_{F₀}(d) ≤ 2(1/t_∞ − 1)G_κ(F₀) + 2𝔞(F₀) for every profile
   (one-sided exponent-½ bound on the local Chebyshev fluctuation), PROVED given K12.
2. (E_γ) for every γ (Cor 3.3, CONDITIONAL) — which is itself an open residue (R5).
3. A nondegenerate margin uniform at t₀/2 — useful only if a later rigidity argument (K10/K11, Lemma E.1) can start
   from an interior point; no such argument is on record.
None of the three implies D; 1–2 are necessary consequences of D already on record. **Input for D: null as an
implication; K12 is a "weaker than D" residue whose packet-level content is (E_γ) ∀γ.**

## 6. Task 6: NUMERICAL test at Mori μ = 15 (T = ½log15), only recorded data

Data: λ_A(Λ) ≤ 4.98·10⁻⁷⁰ on g*, λ_A(Λ) ≥ 0 certified (Mori, CITED); Σ v_n c_{g*}(log n) = ΣΛ(n)s_n ≈ 0.063
(AUDIT_203 §2); λ_{∞,P}(T) ≥ C₀ = −5.372 (decreasing to C₀, P46).
(a) Chord cΛ (the one in the brief; NOT K12). Danskin (upper) and chord (lower):
| t | upper λ_A(Λ)+(1−t)0.063 | lower (1−t)C₀ + t·0 |
|---|---|---|
| 0.5 | 3.15·10⁻² | −2.69 |
| 0.9 | 6.3·10⁻³ | −0.537 |
| 0.99 | 6.3·10⁻⁴ | −5.37·10⁻² |
| 0.999 | 6.3·10⁻⁵ | −5.37·10⁻³ |
The sign of λ_A(tΛ) is not determined by existing data; NUMERICAL, irrelevant for K12.
(b) K12's chord (λ_t). Concavity + b_T(0) ≥ η_κ + b_T(1) ≥ 0 (Mori): b_T(t) ≥ (1−t)η_κ > 0 at all four t, that is,
t*(½log15) = 1. This is CITED+PROVED but trivial: at every certified T ≤ ½log15, t*(T) = 1. The test gives no
information about t_∞ (a tail statement, Lemma 2.1). No new numerics are needed.

## 7. Verdict and labels

| statement | label |
|---|---|
| (Ω_{t₀}) damps toward ρ_κ (κ > κ*), not by a global factor; AUDIT_203 does not falsify it | PROVED (reading of N_011/012 definitions) |
| D ⇒ (Ω_{t₀}); D ⟺ t_∞ = 1 | PROVED |
| Lemma 2.1: (Ω_{t₀}) stable under finite modifications; ⇒ strictly weaker, ⇏ D | PROVED (new) |
| Lemma E.2, limsup form | CONDITIONAL, empty |
| Lemma E.2, liminf form ⟺ (E_γ) (Prop 3.2) | CONDITIONAL (N_013 inputs) |
| (Ω_{t₀}) ⇒ (E_γ) ∀γ (Cor 3.3) | CONDITIONAL |
| margin O(1−t) evades W2/Cor 2′ | ARGUED; irrelevant: the blockage is binary |
| interpolation t₀ → 1 as input for D | NO-GO (Lemma 2.1 + concavity) |
| (Ω_{t₀}) for ζ | OPEN |
| Mori ½log15: cΛ indeterminate; λ_t with t*=1 | NUMERICAL / CITED |

**Verdict.** K12 is not a new route toward D: it is an open residue (R3) weaker than D whose packet-level content is
exactly {(E_γ)}_γ; the margin (1−t) does not break N_013's criticality and interpolation toward D is impossible by
stability under finite modifications. TRAT of K12: **YES → TRANSFER** (to R5 on packets; R3 remains open only on
non-convergent spectral measure families, N_013 §5, with no input for D).

## Entry for the index (06_ R3 / README)

> K12_DAMPED_001 (phase 204j): (Ω_{t₀}) damps toward ρ_κ (κ>κ*), it is not the line cΛ (AUDIT_203 does not apply).
> Lemma 2.1 PROVED: (Ω_{t₀}) stable under finite modifications ⇒ ⇏ D; interpolation t₀→1 NO-GO. Lemma E.2: limsup form
> empty, liminf form ⟺ (E_γ) (CONDITIONAL, N_013); (Ω_{t₀}) ⇒ (E_γ) ∀γ. The margin O(1−t) does not act on the
> convergence/divergence dichotomy. K12: TRANSFER (R5 on packets); R3 only alive on non-convergent spectra, null input.
