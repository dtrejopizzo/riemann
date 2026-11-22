# Round 19 B — The tail reduction (i)+(ii): density of the E-image, and why the comb-robust margin is a representative effect

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_018_B and Paper 46 §sec:ext: λ = e^T, N = λ², admissible f (even,
supp ⊂ [−λ, λ], C², f(0) = ℱf(0) = f(λ) = 0), E the summation map, Φ_f(x) = e^{x/2}Σ_n f(ne^x), Ψ_f = Φ_f 1_{(−∞,−T)}, gauge
𝒢_T = {φ admissible, supp φ ⊂ [−1/λ, 1/λ]}, 𝒲̂ = 𝒜_∞ − 𝒞 + 𝒯 the complete form on the line (comb over all prime powers),
𝒲̂^c = 𝒜_∞ − c𝒞 + 𝒯, 𝒜𝒫 := 𝒜_∞ + 𝒯 (archimedean-plus-polar form), m(τ) = Re ψ(¼ + iτ/2) − log π.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

The reduction under examination: (i) a_T(Ef) = 𝒲̂[Ψ_f] for admissible f with Ef ∈ P_T (PROVED, ROUND_001_B Cor 1.2);
(ii) 𝒲̂[Ψ] ≥ 0 for every admissible Poisson tail Ψ; then a_T ≥ 0 on E(admissible) ∩ P_T. ROUND_018_B observed that on the
tested tails (E-images of prolate spans, prolate representatives) 𝒲̂^c ≥ 0 for every c ∈ [0, 3.5].

## 0. Corpus check
Read: ROUND_001_B (Thm 1.1 radical lemma, Cor 1.2, Prop 1.3 defect, Prop 1.5 fibre dependence ARGUED), ROUND_015_A Thm 3.1,
ROUND_016_B Lemma 2.1, ROUND_017_A, ROUND_018_B; Paper 46 lem:ext-mob, prop:ext-gauge, prob:ext-L, prop:ext-consol
(eq:ext-starstar), form-core statement (main.tex 1832); phase 199 proof-L-sharp: E_001 Thm E.2, X_001 Thm B, C_001,
S_001, MM_001 ("lossless loop; passivity margin = W_T itself"); index rows P211-15A/15B/16B/17A/18B.
What is already in the corpus. (a) Surjectivity of E from admissible data onto the core is lem:ext-mob (Möbius bijection
on [1/λ, λ], free gauge on (0, 1/λ)). (b) "(★) in exterior coordinates" is prop:ext-consol: eq:ext-starstar with κ = 0 is
literally statement (ii). (c) MM_001: the loop is lossless on the line; any margin is W_T itself. (d) ROUND_001_B Prop 1.5:
for c ≠ 1 the c-exterior value is not a function of g (reduction PROVED, sign of 𝒜𝒫[Φ_φ] ARGUED for one sign only).
What is new here. Theorem 2.1 below: 𝒜𝒫 restricted to gauge radicals Φ_φ takes BOTH signs (explicit constructions, the
negative one with value → m(0)ζ(½)²‖η‖² ≈ −11.46‖η‖²), hence for EVERY c ≠ 1 the form 𝒲̂^c is unbounded below on the
admissible tails of EVERY fibre E^{−1}(g). This converts the ARGUED Prop 1.5 into a PROVED statement for all c ≠ 1 (both
sides) and closes the "crude comb-robust bound" route for (ii) proposed after ROUND_018_B. No indexed route is retried:
the question (is the comb-robustness of 18B a property of the class of admissible tails?) is new; the answer re-locates
it inside MM_001's circle, and the memo says so.

## 1. Task (2) first: what (ii) covers — density (PROVED, essentially CITED)

**Proposition 1.1 (E(admissible) contains the core of P_T).** For every G ∈ C_c^∞(I_T) ∩ P_T there is an admissible f
with Ef = G; the set of such f is f_0 + 𝒢_T.
*Proof.* lem:ext-mob of Paper 46 (CITED); self-contained version: put g(u) = u^{−1/2}G(log u) on (1/λ, λ), and
f(u) = Σ_{d < λ/u} μ(d) g(du) for u ∈ [1/λ, λ] (finite sum, C^∞, vanishing near λ because supp G is compact in I_T). For
u ∈ (1/λ, λ), Σ_n f(nu) = Σ_k g(ku)Σ_{d|k}μ(d) = g(u), and only arguments ≥ 1/λ occur, so Ef = G whatever f is on (0, 1/λ).
Choose f on [0, 1/λ] in C^∞, glued C^∞ at 1/λ, vanishing near 0, with ∫f = 0 (one bump); even extension. Two such f differ
by an even C² function supported in [−1/λ, 1/λ] with value 0 at 0 and integral 0, i.e. by 𝒢_T. ∎

**Corollary 1.2 ((ii) on the class is (★); PROVED).** C_c^∞(I_T) is a form core of a_T (Paper 46 main.tex 1832, CITED); since
A, B are continuous on the form domain and nonzero on C_c^∞(I_T), C_c^∞(I_T) ∩ P_T is a core of a_T|_{P_T} (correct a core
sequence by fixed C_c^∞ functions dual to A, B). a_T is continuous in the form norm. Hence
  (★) at T ⟺ 𝒲̂[Ψ_f] ≥ 0 for every admissible f with Ef ∈ P_T ∩ C_c^∞(I_T).
So (i)+(ii) ⟹ (★) is correct, and there is NO surjectivity obstruction: positivity on a form-dense subset suffices, and the
E-image of admissible data contains a form core. Answer to the specific items:
- parity piece of ROUND_017_A (P): its directions lie in P_T, are form-limits of core elements, and every core element is an
  E-image (Prop 1.1). ROUND_018_B §5 "not reached" refers to E-images of PROLATE spans, not to E(admissible). The preimage of
  a parity direction is the Möbius function of §1 plus a gauge choice; nothing is missing.
- gauge: is the fibre; 𝒲̂[Ψ_f] is constant on it (prop:ext-gauge; ROUND_001_B Thm 1.1). Not an obstruction for (★).
- edge f(λ) ≠ 0: corresponds to G(T−) ≠ 0, excluded from the core; covered by density.
**Comparison with prob:ext-L.** (ii) over the class is eq:ext-starstar with κ = 0 (prop:ext-consol). prob:ext-L is strictly
stronger: it asks for a quantitative margin κN^{−A₀}ℓ(g) (gauge-minimised leakage), which gives λ^W_T > 0 uniformly
(thm:ext-margin); (ii) gives only ≥ 0, i.e. exactly (★). Thus "(ii) + density" is not a weakening of the open problem
that avoids its difficulty: it is (★) itself in exterior coordinates (a restatement; REF-D in the corpus' language).
The obstruction is therefore not density; it is (ii).

## 2. Task (1): can (ii) be proved by a comb-robust ("crude, large-margin") argument? NO (PROVED)

The robust format suggested by the data is: bound 𝒞[Ψ] ≤ κ‖Ψ‖²-type (shifts by log n ≥ log 2 meet only the deep small
part of the tail) and 𝒜_∞[Ψ] + 𝒯[Ψ] ≥ m_eff‖Ψ‖² with m_eff > κ; any argument of this kind, if valid on the class, proves
𝒲̂^c ≥ 0 for all c in a neighbourhood of 1 (indeed for c ≤ m_eff/κ). The following theorem shows that no such statement
holds on the class of admissible tails for any c ≠ 1.

**Theorem 2.1 (gauge radicals see 𝒜𝒫 with both signs).** Fix T > 0. (a) There are φ_R ∈ 𝒢_T, R → ∞, with B(Φ_{φ_R}) = 0 and
  𝒜𝒫[Φ_{φ_R}] → m(0)ζ(½)²‖η‖²  (= −5.3722 · 2.13264 · ‖η‖² = −11.457‖η‖² < 0).
(b) There are φ′_R ∈ 𝒢_T with B(Φ_{φ′_R}) = 0 and 𝒜𝒫[Φ_{φ′_R}] → m(10)|ζ(½ + 10i)|²‖η‖² = 0.46429·2.40000‖η‖² = 1.114‖η‖² > 0.
*Proof.* Let η ∈ C_c^∞(−1, 1), real, ‖η‖ = 1, vanishing to infinite order at ±1. Put u₀ = −T − 2R,
h_R(u) = R^{−1/2}η((u − u₀)/R) (support (−T − 3R, −T − R)), and φ(y) = y^{−1/2}h(log y) for y > 0, even extension. Then φ is
C^∞ with support in [e^{−T−3R}, e^{−T−R}] ⊂ (0, 1/λ), so φ(0) = 0; the constraints ∫φ = ∫h e^{u/2}du = 0 and
B := ∫φ dy/y ∝ ∫h e^{−u/2}du = 0 are imposed by subtracting αχ_r + βχ_l with fixed unit bumps χ_r, χ_l sitting at the right
and left ends of the support (unit length). The 2×2 system is diagonally dominant (off-diagonal ratio O(e^{−R})), and the
right-hand sides relative to the diagonal are R^{1/2}∫η(v)e^{∓R(v∓1)/2}dv = O(R^{−K}) for every K (infinite-order vanishing at
±1). So the correction has L² norm and m-weighted norm O(R^{−K}). The corrected φ lies in 𝒢_T.
Φ_φ is supported in (−∞, −T] (ne^x ≥ e^x > 1/λ for x > −T), is rapidly decaying at −∞ (Poisson: Φ_φ(x) = e^{−x/2}Σ_{k≥1}ℱφ(ke^{−x})
since ℱφ(0) = 0), and Φ̃_φ(s) = ζ(s)Mφ(s), Mφ entire (ROUND_001_B §1.0 argument, with Mφ(1) = 0). On Re s = ½,
Φ̂_φ(τ) = ζ(½ + iτ)ĥ(−τ). Since B(Φ_φ) = Φ̃_φ(0) = ζ(0)Mφ(0) = 0, the polar term 2A B vanishes, and
  𝒜𝒫[Φ_φ] = (1/2π)∫ m(τ)|ζ(½ + iτ)|²|ĥ_R(τ)|² dτ (+ O(R^{−K})).
|ĥ_R(τ)|² = R|η̂(Rτ)|² is an approximate identity of mass 2π‖η‖² concentrating at τ = 0, and m|ζ(½+i·)|² is continuous of
polynomial growth while η̂ is Schwartz; hence the limit m(0)ζ(½)²‖η‖². For (b) use h_R(u)·√2 cos(10u): the mass splits
equally at τ = ±10, limit m(10)|ζ(½+10i)|²‖η‖²·(½ + ½)/1 = m(10)|ζ(½+10i)|²‖η‖² (each of the two peaks carries ½‖η‖² after the √2 normalisation), positive. The numerical values are
point evaluations of ψ and ζ (computed: m(0) = −5.37218, ζ(½)² = 2.13264, m(10) = 0.46429, |ζ(½+10i)|² = 2.40000); only
their signs are used. ∎ (No zero of anything is used; the only ζ-inputs are ζ(0) = −½, two point values, and the
continuation Φ̃_φ = ζMφ already in ROUND_001_B.)

**Corollary 2.2 (𝒲̂^c is unbounded below on every fibre, every c ≠ 1; PROVED).** For every admissible f and every c ≠ 1,
  inf_{φ ∈ 𝒢_T} 𝒲̂^c[Ψ_{f+φ}] = −∞.
*Proof.* Ψ_{f+tφ} = Ψ_f + tΦ_φ (support of Φ_φ). 𝒲̂^c = 𝒲̂ + (1 − c)𝒞, and Φ_φ is 𝒲̂-radical (Thm 1.1 of ROUND_001_B), so
𝒞(Φ_φ, ·) = 𝒜𝒫(Φ_φ, ·) and 𝒲̂^c[Ψ_f + tΦ_φ] = 𝒲̂[Ψ_f] + (1 − c)(𝒞[Ψ_f] + 2t𝒜𝒫(Ψ_f, Φ_φ) + t²𝒜𝒫[Φ_φ]). Take φ from
Thm 2.1(b) if c > 1, from (a) if c < 1: the t²-coefficient is negative. ∎
(This is ROUND_001_B Prop 1.5 made PROVED, with both signs.)

**Corollary 2.3 (NO-GO: comb-robust proofs of (ii) on the class).** No inequality of the form
  𝒜_∞[Ψ] + 𝒯[Ψ] − c𝒞[Ψ] ≥ 0 for all admissible tails Ψ
holds for any c ≠ 1. Equivalently: on the class of admissible tails, 𝒜𝒫 − c𝒞 is unbounded below for c < 1 and for c > 1; c = 1 is the only weight at which it is semi-bounded at all. Any proof of
(ii) must therefore use the exact equality c = 1 on the gauge directions — that is, the radical identity Φ_φ ∈ rad 𝒲̂,
which is again the Λ-specific input (Λ ∗ 1 = log + functional equation). The "margin up to c ≈ 3.5" of ROUND_018_B is a
property of the chosen representative (the prolate combination itself, with its specific small-y profile), not of the
class: along the gauge line through that representative the margin is −∞ for every c ≠ 1. PROVED.
**Mechanism.** The data mechanism "comb shifts reach only the deep small part of the tail" is defeated exactly by gauge
tails: a gauge radical Φ_φ lives entirely in the deep part (support ≤ −T − R), may be low-frequency (where m < 0), and
has arbitrary size. The comb and the archimedean form balance on it exactly (𝒞 = 𝒜𝒫 on it), so it is invisible to 𝒲̂
and fatal to every weighted variant.

**What a robust argument could still target (OPEN, stated precisely).** A gauge-fixed section s: G ↦ f_G (e.g. the
representative minimising dist(r_f, 𝒢̄_T), i.e. the one realising ℓ(g)) and the statement
  (ii_s) 𝒲̂^c[Ψ_{f_G}] ≥ 0 for all G ∈ core ∩ P_T, c ∈ [0, c₁], some c₁ > 1.
At c = 1 it is (★) (fibre invariance); for c ≠ 1 it says nothing about a^c_T (identity (i) fails), so it passes rule 4(a)
formally through (i). Whether (ii_s) holds is OPEN. Two observations limit it: (α) the gauge-tail span {Φ_φ} is plausibly
dense in L²(−∞, −T) (Möbius inversion of any tail profile on (0, 1/λ) is a finite sum pointwise; regularity at 0 is the
only constraint; ARGUED), so a section minimising an L²-type quantity has inf‖Ψ‖ = 0 on each fibre while 𝒲̂ stays fixed —
𝒲̂ is not bounded by ‖Ψ‖² on the class, and any section must be chosen in a norm in which the radical is closed; the
natural one is the leakage metric of prob:ext-L, so (ii_s) with c₁ > 1 is a margin statement of the same type as
eq:ext-starstar (a quantitative leakage coercivity). (β) MM_001: on the line the archimedean part and the collapsed comb
cancel exactly (lossless loop); a margin for c ≠ 1 on a section is a passivity margin of that loop restricted to the
section, i.e. W_T itself measured on the section. ARGUED: (ii_s) is prob:ext-L in a different gauge, not a weaker problem.

## 3. Task (3): falsifier consistency
(a) cΛ: (i) fails (ROUND_001_B Prop 1.3, defect (1 − c)(𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f])); (ii) "holds" for cΛ only on prolate representatives (18B), and fails on the class (Cor 2.2).
Consistent, and sharper than stated in the task: the comb-robustness of (ii) is not a property of (ii).
(b) a_P, (c) Beurling, (d) finite modification: (i) fails (Prop 1.3 of ROUND_001_B for (b), (d); no Poisson summation /
functional equation for (c)); the analogue of Cor 2.2 for w ≠ Λ: 𝒲̂^w = 𝒲̂ + 𝒫_{Λ−w}, and on gauge radicals 𝒫_{Λ−w}[Φ_φ]
is a comb pairing of deep low/high-frequency gauge tails; for (d) with e finitely supported, 𝒫_e[Φ_φ] = Σ_{n∈supp e}
2e(n)n^{−½}c_{Φ_φ}(log n), which by the dilate construction of Thm 2.1 (choose η with c_η(log n) of prescribed sign at the
finitely many lags, R fixed) takes both signs: ARGUED. The reduction (i)+(ii) ⟹ (★) is not a sign step by itself; it
transmits whatever sign (ii) has, and (ii) on the class is (★).

## Result
PIVOT, with one PROVED NO-GO.
- The implication (i)+(ii) ⟹ (★) is correct and complete: E(admissible) contains the form core C_c^∞(I_T) ∩ P_T
  (lem:ext-mob, Prop 1.1), so positivity on E-images suffices by continuity, and there is no surjectivity obstruction
  (parity piece, gauge, edge all covered). But (ii) over the class of admissible tails is (★) itself in exterior
  coordinates (prop:ext-consol with κ = 0); prob:ext-L is the strictly stronger margin version.
- (ii) has NO comb margin on the class: for every c ≠ 1, 𝒲̂^c is unbounded below on every gauge fibre (Thm 2.1, Cor 2.2).
  The c ∈ [0, 3.5] robustness of ROUND_018_B is a representative effect. NO-GO (class: comb-robust / weighted
  "archimedean coercivity beats the overlapping comb" bounds for (ii) on the full class of admissible Poisson tails).

### What was proved
- Prop 1.1 / Cor 1.2: E(admissible) ⊇ C_c^∞(I_T) ∩ P_T (re-proof of lem:ext-mob), and (★) ⟺ (ii) on core E-images.
- Thm 2.1: gauge radicals Φ_φ with B = 0 and 𝒜𝒫[Φ_φ] → −11.457‖η‖² (low frequency, deep support) and → +1.114‖η‖² > 0
  (frequency 10); zero-free proof.
- Cor 2.2: inf over the gauge fibre of 𝒲̂^c[Ψ] is −∞ for every c ≠ 1 (ROUND_001_B Prop 1.5 upgraded to PROVED, both signs).
- Cor 2.3: no inequality 𝒜_∞ + 𝒯 − c𝒞 ≥ 0 on admissible tails for c ≠ 1; any proof of (ii) must use the radical identity on
  gauge directions.

### What failed and why
The proposed crude proof of (ii) (decay of Ψ beyond its first cell + Schur bound 𝒞 ≤ (sup weight)·(overlap) +
archimedean coercivity m_eff > κ). It fails at the first step: the decay hypothesis ‖Ψ‖ on the deep part ≤ θ‖Ψ‖ on the first
cell is false on the class (add tΦ_φ with Φ_φ supported below −T − R: the deep mass is arbitrary), and the archimedean
coercivity is false on the class (m(0) < 0 at the low frequencies that deep gauge tails can carry). Both are restored
only modulo the gauge, where the only available control is the exact radical identity — c = 1 exactly.

### Next concrete step
Fix the gauge by the leakage-minimising representative r_f ⊥ 𝒢̄_T (prop:ext-gauge) and test (ii_s) numerically at
T = 0.8: compute 𝒲̂^c on the ℓ-minimising tails of the 18B E-image space (gauge rank ≥ 30) for c ∈ [0.5, 2]. If the
c-margin survives on that section, (ii_s) is a well-posed robust target equivalent to a leakage inequality and must be
compared term by term with eq:ext-starstar; if it collapses toward c = 1 as the gauge rank grows, the exterior route has
no robust form and every sign must sit in the identity (radical lemma) — record that as the closure of the tail-form line.

## Index row and ledger line
Index (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md): row P211-19B. Ledger (LEDGER.md): line C41.
