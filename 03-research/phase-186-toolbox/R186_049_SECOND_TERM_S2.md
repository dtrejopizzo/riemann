# R186_049 — S2's second term (new negativity seen by the old prolates): exact formulation, numbers in three windows, M₁ test and verdict

Phase 186, round 23. Paper 47,
the grid and the crossword are not touched. Self-contained script: `r049_N2.py` (M = 48, 12 s; copies the definitions of eq:symbol/eq:form/prop:band/Tate as
r046, does not import results). Read: README rounds 20–22; R186_046 (§1 Lemma 1.1, §3 Prop. 3.1, §5.3 two-term statement),
R186_116 (§2: 046's c_W was an artifact; NO-GO of the converse via κ² ≫ c_E c_W), R186_048 (Lemma 3.1, fission/deformation/ex nihilo,
Table 3.3), R186_044 Thm 2, R186_047 (L-W), R186_042 (sub-Shannon sea), Paper 47 lem:roughEF, prop:negtrace.

## 0. Verdict

1. **Exact formulation (§2).** With Neg^{new}_T := R σ_T⁻ 1_{U_T∖U₀}(D) R and 𝔞^{(U₀)}_T := 𝔞_T + Neg^{new}_T (the symbol with the new
 negativity removed): λ_A(T) ≥ 0 ⟺ [𝔞^{(U₀)}|𝒫_T ⪰ 0] ∧ [β_new := max_{𝒫_T} Neg^{new}(F)/𝔞^{(U₀)}(F) ≤ 1] (Prop. 2.1, PROVED, trivial).
 The first bracket is "(N′) as an operator statement" (cancellation on U₀ + positivity of the rest); the second is N2 in the only form
 that implies the sign. The requested "o(1)" version — ν(T₀,T) := λ_max(Π₀ Neg^{new} Π₀) on V₀^P ≤ ε with ε < λ_min(𝔞^{(U₀)}) — **implies
 λ_A ≥ 0 only if required over the whole of 𝒫_T** (Weyl, Prop. 2.2), and in that form its hypothesis is false by a factor of 2–17 in every
 window; restricted to V₀^P (the form asked for) **implies nothing**, by the NO-GO of R186_046 Prop. 3.1 with κ²/(c_E c_W) =
 10³–10⁵ (sticking point: the coupling, identical to round 21's).
2. **Numbers (§3, NUMERICAL, stable at M = 40/48/56 to 4 digits).** ν = 0.256 (½log3 → ½log5), 0.071 (log 2 → ½log5), 0.315 (½log5 →
 ½log7), 0.240 (½log3 → log 2): **O(1), not o(1)**. Rigorous bound "sup σ⁻ × old prolate leakage" = 0.40/0.13/0.46/0.33 (factor
 1.3–1.8). **It is dominated by fission/growth adjacent to U₀**: at ½log3 → ½log5 the piece (4.24, 6.46) (fission product,
 R186_048 §3) contributes 0.245 of 0.256; at log 2 → ½log5 every piece is growth of old components; at ½log5 → ½log7
 the three growth pieces at τ < 12.4 give 0.20/0.29/0.23 and the distant ex nihilo ones ≤ 0.06, decreasing with distance
 like sinc leakage (10⁻² at τ ≈ 17, 10⁻³ at 27, 10⁻⁵ at 108). **So N2 is not "outside U₀": it is internal growth seen by
 the prolates themselves, and the condition collapses to λ_A** (Prop. 2.1).
3. **Decay (§3.3).** With T₀ = ½log3 fixed, ν = 0.24, 0.26, 0.39, 0.40, 0.17, 0.07 at T = log 2, ½log5, ½log7, ½log9, 1.25, 1.4: it rises
 up to ½log9 and only decreases afterward. What decays is the Slepian leakage 1 − λ₀ of the **non-polar** old prolates (0.53 → 0.036);
 the two polar prolates (component (0, 3.3)) have 65–95% of their mass outside 𝒫_T and, **projected onto 𝒫_T, their leakage to the
 new pieces is 0.06–0.5 (polynomial, tail of e^{±t/2}), not the 10⁻⁴ exponential leakage of the unprojected prolate**; multiplied by
 the growing sup σ_T⁻ ≍ e^T, ν on V₀^P has no reason to → 0. Lemma 3.4 (PROVED mod. CITED): on V₀ without projection ν₀ ≲
 16√(πc) e^{T(1−|J|_min)} → 0; this is pure Slepian (no input from Λ) and does not touch the sign.
4. **M₁ (§4): N2 is blind to the sign.** ν(M₁, δ) at ½log3 → log 2 = 0.3907, 0.3907, 0.3907, 0.3908, 0.3923 for δ = 0.002, 0.004, 0.01,
 0.03, 0.1 while λ_A(M₁) = +3.3·10⁻⁸, −1.8·10⁻⁷, −1.7·10⁻⁶, −4.7·10⁻⁵, −1.5·10⁻³ (crossing δ_A ≈ 0.0025): **ν does not change in the 4th
 digit when the sign changes**; likewise at log 2 → ½log5 (ν = 0.1139 at δ = 10⁻⁵ with λ_A > 0 and at δ = 10⁻³ with λ_A < 0). ν(M₁) > ν(ζ)
 (0.39 vs 0.24; 0.115 vs 0.071) for geometric reasons (U₀^{M₁} has one more component at (17.2, 19.4) already at ½log3), not because of the sign.
 M₁ **satisfies** (N′)-operator (λ_min 𝔞^{(U₀)} = 0.28, 9·10⁻⁴, 0.085 > 0) and **fails only β_new ≤ 1** (1 − β_new = −5·10⁻³, −4.5, −1.3·10⁻²);
 for ζ, 1 − β_new = 2.2·10⁻¹¹, 7.6·10⁻¹¹, 1.4·10⁻¹³, 4.9·10⁻⁷ = λ_A/𝔞^{(U₀)}(h*): **it inherits exactly**. Conclusion:
 N2 is honest but the sign returns wholly to the pencil (β_new), which is row D; **R186_046 §5.3's two-term condition is not
 a new object**: its first term holds with margin O(10⁻²…10⁻¹) for both ζ and M₁, and its second term is either false
 (O(1) at finite T), or vacuous (Slepian, T → ∞ with no projection), or exactly D (β_new).
5. **Contact with the sign: none.** Nothing here bounds λ_A from below with its own margin. Row D: OPEN. Ω's S2 stays as it was,
 with the reading corrected: there is no "second term with no analogue in the corpus"; the analogue is R186_042 Thm 2.1's Kreĭn pencil with
 the old/new partition instead of Pos/Neg.

## 1. Framework and own verifications

Notation (Paper 47 eq:symbol/eq:form; copied in `r049_N2.py`): σ_T(τ) = m(τ) − Σ_{log n<2T} v_n cos(τ log n), v_n = 2Λ(n)/√n;
𝔞_T(F) = (1/2π)∫σ_T|F̂|², F ∈ L²(I_T); 𝒫_T = {∫F e^{±t/2} = 0}; λ_A(T) = min 𝔞_T|𝒫_T, h*_T the minimizer. U₀ := {σ_{T₀} < 0}, U_T :=
{σ_T < 0} (τ > 0, symmetric, finite unions, prop:band). R186_046 §1's boundary convention (at T = ½log p, p is not yet contact).
- Neg^{new}_T := R σ_T⁻1_{U_T∖U₀}(D) R (negativity outside U₀: components disjoint from U₀ and pieces of old components
 protruding from U₀), Neg^{old}_T := R σ_T⁻1_{U_T∩U₀}(D) R, 𝔞^{(U₀)}_T := Pos_T − Neg^{old}_T = 𝔞_T + Neg^{new}_T.
- V₀ := span{ψ_i^±} with ψ_i^± the per-parity index-0 prolate of S_{E_i} = R 1_{±J_i}(D) R, J_i a component of U₀, **in the window
 I_T** (the old prolates at the new T); V₀^P := P_{𝒫_T}V₀ (as R186_044 §2), Π₀ its projector, dim 2·#comp(U₀).
- ν(T₀,T) := λ_max(Π₀ Neg^{new}_T Π₀) = max{Neg^{new}(F) : F ∈ V₀^P, ‖F‖ = 1}; ν_cross := ‖Π₀ Neg^{new} (1−Π₀)|_{𝒫_T}‖.
- β_new := max_{F∈𝒫_T} Neg^{new}(F)/𝔞^{(U₀)}(F) (Kreĭn pencil, defined if 𝔞^{(U₀)}|𝒫_T ≻ 0).
Verifications:
- λ_A = 1.028·10⁻⁷ (log 2; R186_046: 1.03·10⁻⁷), 3.65·10⁻¹² (½log5, M = 48; R186_046: 3.65·10⁻¹²; M = 40: 3.85·10⁻¹², M = 56: 3.29·10⁻¹²:
 decreasing variational bound in M, as it must); ½log7: 3.6·10⁻¹⁴ = M = 48's floor (only "≈ 0"). M₁(0.1, log 2): −1.503·10⁻³
 (R186_114 M = 60: −1.513·10⁻³; R186_044 M = 40: −1.474·10⁻³); M₁(0.01, log 2): −1.660·10⁻⁶ (R186_044: −1.660·10⁻⁶) ✓.
- Negative sets: U⁺_{½log3} = (0, 3.305) ∪ (6.945, 10.531); U⁺_{½log5}: 8 comp. with zeros 1.982, 4.237, 6.458, 8.738, 11.293, …,
 108.95; U⁺_{log2}: 6 comp.; U⁺_{½log7}: 17 — identical to R186_046/048 ✓.
- R186_046's 70%: Neg(h*) in (4.24, 6.46) = 0.158, total Neg(h*) = 0.165 + 0.059 = 0.224 → 70.4% (R186_048: 70.3%) ✓.
- Identity 𝔞_T = 𝔞^{(U₀)} − Neg^{new}: implemented as a matrix sum (Nnew by quadrature in τ over the pieces, 𝔞_T in
 x-form); x-vs-τ check inherited from r043/r046 (1.4·10⁻⁴). λ_min(𝔞^{(U₀)} − Neg^{new}) = λ_A by construction.
- "sup × leakage" bound: Neg^{new} ⪯ Σ_p s_p S_p (s_p = sup_p σ_T⁻, multiplier order) ⇒ ν ≤ λ_max(Π₀ Σ s_p S_p Π₀): verified
 in every row (ratio 1.3–1.8) ✓. Stability in M (½log3 → ½log5): ν = 0.25635 at M = 40, 48, 56; log 2 → ½log5: 0.07123 ✓.
- Nyquist 0.8M/T ≈ 48 (½log5), 39 (½log7): the pieces at τ > 60 are not resolved; their contribution to ν is ≤ 10⁻³ (table §3) and to
 Neg(h*) ≤ 10⁻¹²: they affect no conclusion. ‖Neg^{new}|𝒫_T‖ does depend on M at log 2 → ½log5 (0.073/0.076/0.100 at 40/48/56,
 from the piece at 62): used only as "≫ λ_min 𝔞^{(U₀)}".

## 2. Precise formulation of N2 and the implication

**Prop. 2.1 (exact two terms; PROVED, elementary).** Let T₀ < T. Neg^{new}_T ⪰ 0 (compressed ≥ 0 multiplier). Then
 λ_A(T) ≥ 0 ⟺ 𝔞^{(U₀)}_T|𝒫_T ⪰ Neg^{new}_T|𝒫_T ⟺ [𝔞^{(U₀)}_T|𝒫_T ⪰ 0] ∧ [β_new ≤ 1],
and if 𝔞^{(U₀)}|𝒫_T ≻ 0, with u* the pencil's maximizer: λ_A/𝔞^{(U₀)}(u*) ≤ 1 − β_new ≤ λ_A/𝔞^{(U₀)}(h*) (the first because 𝔞_T(u*) =
(1−β_new)𝔞^{(U₀)}(u*) ≥ λ_A, the second by taking F = h* in the pencil); with a number, 1 − β_new = λ_A/𝔞^{(U₀)}(h*) to every digit (§3.2). *Proof.* 𝔞_T = 𝔞^{(U₀)} −
Neg^{new} is a multiplier identity (σ_T = σ_T 1_{(U_T∖U₀)^c} − σ_T⁻1_{U_T∖U₀}); the pencil (Neg^{new}, 𝔞^{(U₀)}) with 𝔞^{(U₀)} ≻ 0
is Kreĭn's (R186_042 Thm 2.1 with the old/new partition). ∎
Reading the two terms: (i) 𝔞^{(U₀)} ⪰ 0 says "the symbol whose only negativity is U₀'s (cancelled or not by the new
primes) is positive on 𝒫_T": this is (N′)/R183_031 Thm 1 in operator form, plus the positivity of the rest of σ_T; it is σ-computable and
**has its own margin** (λ_min = 0.03–0.19). (ii) β_new ≤ 1 is N2 in the only form that decides: how much new negativity the
old positive form can support. **It inherits** (Lemma T′ of R186_045: continuous functional of 𝔞_T; with a number, 1 − β_new = λ_A/𝔞^{(U₀)}(h*)).

**Prop. 2.2 ("o(1)" version; PROVED, Weyl).** If λ_min(𝔞^{(U₀)}|𝒫_T) ≥ c and ‖Neg^{new}|𝒫_T‖ ≤ ε < c, then λ_A(T) ≥ c − ε > 0. ∎
Hypothesis with a number (table §3): c = 0.032/0.017/0.048/0.19 against ε = 0.55/0.076/0.38/0.37: **false by a factor of 2–17 in every
window**. The new negativity is O(1) in norm on 𝒫_T (like its mass, R186_048 Lemma 2.2) and the old form does not dominate it.

**Prop. 2.3 (version restricted to V₀^P; NO-GO with a number).** Let E := V₀^P, W := 𝒫_T ⊖ E, c_E := λ_min(𝔞_T|E) =
λ_min(𝔞^{(U₀)}|E − Π₀Neg^{new}Π₀) ≥ c_E^{old} − ν, c_W := λ_min(𝔞_T|W), κ := ‖𝔞_T|_{E×W}‖. (R186_046 Prop. 3.1:) λ_A ≥ c′ > 0 ⟸ c_E > 0 ∧
c_W > 0 ∧ κ² < c_E c_W. A bound ν ≤ ε only improves c_E (in fact c_E^{old} − ν = 0.088 − 0.256 < 0 at ½log3 → ½log5: it does not even give
c_E > 0; the real c_E, +2.0·10⁻³, is positive by internal cancellation, not by dominance). And even though c_E > 0 (yes: 2.0·10⁻³, 1.1·10⁻⁴,
1.6·10⁻⁵, 1.0·10⁻³) and c_W > 0 (1.3·10⁻³, 1.14, 0.72, 0.40): κ = 0.75, 0.61, 1.02, 0.81 and κ²/(c_E c_W) = 2·10⁵, 3·10³, 9·10⁴, 2·10³. **Sticking
point: the V₀^P–W coupling** (exact: 1 − ρ_T = 1.3·10⁻¹⁰, 5.9·10⁻¹⁰, 1.4·10⁻¹², 9.6·10⁻⁵, inherits). It is the same wall as R186_046 §3
(corrected by R186_116) with V₀^P instead of E_η: W-loc. Also ν_cross = ‖Π₀Neg^{new}(1−Π₀)‖ = 0.11/0.016/0.15/0.12: the new
negativity couples E and W at the same order it has within E.

**Answer to task 1.** N2 implies λ_A ≥ 0 only in the form of Prop. 2.1 (β_new ≤ 1, inherits) or Prop. 2.2 (over all of 𝒫_T, hypothesis
false). In the "seen by the old prolates" form (Prop. 2.3) it does not imply: NO-GO with constants, obstruction = κ.

## 3. ν in the windows: values, per-piece breakdown, dependence on T

**Table 3.1 (ζ, M = 48).** New pieces = connected components of U_T∖U₀; "growth" = a piece of a component of U_T intersecting U₀
(deformation/growth), "disj." = a component of U_T disjoint from U₀ (ex nihilo or a displaced fission product, R186_048).

| T₀ → T | λ_A | ν | sup×leakage bound | ν per piece (τ; type) | new / U₀ Neg(h*) | λ_min 𝔞^{(U₀)} | ‖Neg^{new}‖ | 1 − β_new |
|---|---|---|---|---|---|---|---|---|
| ½log3 → ½log5 | 3.7e-12 | **0.256** | 0.395 | 0.245 (4.2–6.5; disj., fission of (6.9,10.5)); 0.029 (10.5–11.3; growth); 0.020 (16.5–18.8; disj.); 0.004 (27); 0.001 (45); 4e-4 (63); 1e-5 (108) | 0.165 / 0.059 | 0.032 | 0.547 | 2.2e-11 |
| log 2 → ½log5 | 3.7e-12 | **0.071** | 0.125 | 0.056 (4.2–4.8; growth); 0.063 (8.7–9.7; growth); 0.018 (18.5–18.8); 0.041 (27.0–27.6); 0.035 (44.8–45.1); 0.006; 0.001 (63; disj.); 3e-5 (108) | 0.048 / 0.176 | 0.017 | 0.076 | 7.6e-11 |
| ½log5 → ½log7 | ≈ 0 | **0.315** | 0.460 | 0.197 (3.4–4.2; growth); 0.293 (7.0–8.7; growth); 0.230 (11.3–12.4; growth); 0.015; 0.034; 0.017 (22.6–23.7; disj.); 0.061 (26.7–27.0); 0.013 (34.5–35.9; disj.); 0.074 (46.3–46.9); 0.038 (62.1–62.6); rest ≤ 0.018 | 0.249 / 0.070 | 0.048 | 0.376 | 1.4e-13 |
| ½log3 → log 2 | 1.0e-7 | **0.240** | 0.334 | 0.232 (4.8–6.9; growth); 0.156 (10.5–12.0; growth); 0.058 (16.3–18.5; disj.); 0.001 (27.6); 6e-4 (45) | 0.209 / 0.038 | 0.189 | 0.368 | 4.9e-7 |

Reading. (a) **ν is O(1)** in all four windows, and of the same order as the negativity h* has outside U₀ (ν ≥ Neg(h*)^{new}·(h*'s mass
in V₀^P) by Rayleigh; mass 0.979–0.9999). (b) **Fission/growth dominance**: the pieces adjacent to U₀ (τ < 12.5,
distance 0 or < 1) carry 95% (½log3 → ½log5), 100% (log 2 → ½log5, no new ones with mass), 90% (½log5 → ½log7) of ν; the
true ex nihilo ones (16–110) contribute 10⁻²…10⁻⁵, in proportion to the old prolate's sinc leakage to the piece (the script's
"max leakage" column: 8.8·10⁻² at 4.2–6.5, 4.7·10⁻³ at 16.5, 2.0·10⁻³ at 27, 3.4·10⁻⁴ at 45, 3.7·10⁻⁵ at 108). **Confirms R186_048**: the
negativity that matters is inherited (fission + deformation), not born, and "outside U₀" is the wrong name for "the old component
that split and moved." (c) ν is not "new primes" in any arithmetic sense: the piece (4.24, 6.46) is σ_{½log5} = m − v₂cos −
v₃cos − v₄cos where the cosines of 2 and 3 (old and new) weigh the same; the "new" label is bookkeeping, not causal.

**3.2 Where the sign ends up in the old/new partition.** 1 − β_new = 2.2·10⁻¹¹, 7.6·10⁻¹¹, 1.4·10⁻¹³, 4.9·10⁻⁷ = λ_A/𝔞^{(U₀)}(h*) (𝔞^{(U₀)}(h*)
= λ_A + Neg(h*)^{new} = 0.165, 0.048, 0.249, 0.209). The first term (𝔞^{(U₀)} ≻ 0) has its own margin of 0.03–0.19 and holds with no
fine cancellation; **all the fineness is in the pencil**: ζ supports exactly (to 10⁻¹¹) as much new negativity as its old form can
bear. It is R186_040/044's three-term cancellation written as old/new instead of V/W. Prop. 2.1 is exact, carries no
sign, and is not σ-computable with a margin (W-loc).

**3.3 Dependence on T (T₀ = ½log3 fixed; NUMERICAL, M = 48; at T ≥ 1.25 Nyquist 0.8M/T ≈ 27–31, the unresolved distant pieces
weigh < 10⁻³ in ν).**

| T | log 2 | ½log5 | ½log7 | ½log9 | 1.25 | 1.4 | 1.6 |
|---|---|---|---|---|---|---|---|
| ν | 0.240 | 0.256 | 0.393 | 0.401 | 0.175 | 0.073 | ≈ 0.08 |
| sup×leakage bound | 0.334 | 0.395 | 0.601 | 0.551 | 0.336 | 0.111 | — |
| 1 − λ₀ (even polar, odd polar, J₁ even, J₁ odd) |.077.53.34.30 |.043.40.22.29 |.017.23.19.15 |.008.14.12.13 |.003.073.078.086 |.0013.036.061.047 |.0004.013.027.032 |
| sup σ_T⁻ in new pieces / Σv_n | 1.07 / 2.3 | 1.53 / 2.9 | 1.95 / 4.4 | 2.47 / 6.3 | 3.24 / 8.5 | 3.43 / 10.3 | 3.94 / 14.3 |
| leakage to new pieces of the even polar: ψ unprojected / P_𝒫ψ | 9e-3 / 0.40 | 7e-3 / 0.38 | 7e-3 / 0.42 | 4e-3 / 0.33 | 2e-3 / 0.18 | 5e-4 / 0.087 | 1e-4 / 0.063 |
| new Neg(h*) | 0.209 | 0.165 | 0.119 | 0.145 | 0.243 | 0.315 | — |

Reading. (a) ν **grows** up to ½log9 (more new pieces, sup σ⁻ ↑) and only decays afterward, slowly (0.40 → 0.08 between T = 1.1 and
1.6): what governs it is sup σ_T⁻ (↑ like e^T: Σv_n ≍ 4e^T) × Slepian leakage (↓ like e^{−T|J|}). (b) The polar prolates (component
(0, 3.3)) have 65–95% of their mass outside 𝒫_T; **projected**, their leakage to the new pieces is 0.06–0.4 — two orders larger than
the unprojected prolate's — because P_𝒫ψ contains e^{±t/2}'s tail, whose spectral density decays like 1/τ² (polynomial, not
exponential). It is the same fact as R186_044 §3.1 (polar mode 98% outside 𝒫_T) seen from the leakage side. Consequence: **on V₀^P, ν
is not o(1) via Slepian**; the polynomial leakage × sup σ⁻ ≍ e^T does not tend to 0 in any regime proved here (at T = 1.6 it is still 0.08).
(c) h* shifts its negativity toward the new pieces (0.12 → 0.32 between ½log7 and 1.4): R186_048 Table 3.3's migration continues.

**Lemma 3.4 (ν without projection, asymptotic; PROVED mod. CITED Slepian).** Let ν₀(T₀,T) := max_{V₀, ‖F‖=1} Neg^{new}(F) (without P_𝒫). Then
ν₀ ≤ sup_{U_T∖U₀} σ_T⁻ · max_i (1 − λ₀^{(i)}(T)) ≤ (Σ_{log n<2T} v_n + sup|m|)·max_i 4√(πc_i) e^{−2c_i}(1+o(1)), c_i = T|J_i|/2 (Slepian–
Landau–Pollak, CITED: 1 − λ₀(c) ~ 4√(πc)e^{−2c}). With Σ_{n≤x}Λ(n)/√n ~ 2√x (CITED, PNT) and |J_i| ≥ |J|_min: ν₀ ≲ 16√(πc) e^{T(1−|J|_min)} →
0 if |J|_min > 1 (for U_{½log3}: 3.3, 3.6). *Proof.* Neg^{new} ⪯ s·S_{U₀^c} and ⟨ψ_i, S_{U₀^c}ψ_i⟩ = 1 − ⟨ψ_i, S_{U₀}ψ_i⟩ ≤ 1 − λ₀^{(i)}; for
combinations, the ψ_i of distinct components are not orthogonal, but V₀ has fixed dimension and each one's leakage bounds that of the
combination up to a factor ≤ dim V₀ (Cauchy–Schwarz). ∎ **Content**: zero arithmetic (only that Σv_n grows like e^T) and zero sign.
It is the reason "N2 = o(1)" looks natural asymptotically: it is the prolates' concentration, not a property of Λ. And in
the relevant form (V₀^P, within 𝒫_T) it does not even hold (3.3(b)).

## 4. M₁ test (quartet at γ₁; blind regime δ_A ≈ 0.0025 < δ < δ_V ≈ 0.034 and δ = 0.1)

**Table 4.1 (M = 48; U₀^{M₁} = {σ^{M₁}_{T₀} < 0} with the quartet already present at T₀).**

| window | δ | λ_A(M₁) | ν | sup×leakage bound | new / U₀ Neg(h*) | λ_min 𝔞^{(U₀)} | 1 − β_new | c_E (V₀^P) | c_E of 𝔞^{(U₀)} |
|---|---|---|---|---|---|---|---|---|---|
| ½log3 → log 2 | 0.002 | **+3.3e-8** | 0.3907 | 0.5952 | — | 0.283 | +9.7e-8 | +7.3e-4 | 0.296 |
| | 0.004 | −1.8e-7 | 0.3907 | 0.5952 | — | 0.283 | −5.1e-7 | +7.3e-4 | 0.296 |
| | 0.01 | −1.7e-6 | 0.3907 | 0.5953 | 0.341 / 0.107 | 0.283 | −4.9e-6 | +7.2e-4 | 0.296 |
| | 0.03 | −4.7e-5 | 0.3908 | 0.5955 | 0.307 / 0.199 | 0.282 | −1.5e-4 | +6.8e-4 | 0.296 |
| | 0.1 | −1.5e-3 | 0.3923 | 0.5978 | 0.291 / 0.427 | 0.281 | −5.2e-3 | +1.4e-4 | 0.295 |
| ζ (same window) | — | +1.0e-7 | 0.2396 | 0.3342 | 0.209 / 0.038 | 0.189 | +4.9e-7 | +1.0e-3 | 0.196 |
| log 2 → ½log5 | 1e-5 | **+2.5e-12** | 0.1139 | 0.1535 | — | 3.9e-3 | +5.2e-11 | +5.9e-5 | 4.7e-3 |
| | 1e-3 | −4.5e-8 | 0.1139 | 0.1535 | — | 3.9e-3 | −6.1e-6 | +5.9e-5 | 4.7e-3 |
| | 0.1 | −5.0e-3 | 0.1148 | 0.1543 | 0.019 / 0.680 | 9.3e-4 | −4.5 | −3.5e-3 | 1.9e-3 |
| ζ (same window) | — | +3.7e-12 | 0.0712 | 0.1251 | 0.048 / 0.176 | 0.017 | +7.6e-11 | +1.1e-4 | 2.8e-2 |
| ½log3 → ½log5 | 0.1 | −5.0e-3 | 0.3263 | 0.4687 | 0.378 / 0.320 | 0.085 | −1.3e-2 | −1.1e-4 | 0.103 |

Reading. (a) **ν is independent of δ to 4 digits across the sign change** (0.3907 for δ = 0.002 with λ_A > 0 and for δ = 0.01
with λ_A < 0; 0.1139 for δ = 10⁻⁵ and 10⁻³ at ½log5): the quartet changes σ by O(δ²) in the new pieces and ν does not see it. **N2 is not a
discriminator**: it does not distinguish M₁ from ζ in any regime, neither "with O(1) margin" nor without it. (b) ν(M₁) > ν(ζ) (0.39 vs 0.24, 0.115 vs 0.071)
is geometric: U₀^{M₁} has one more component ((17.2, 19.4), created by bhat already at T₀) and its components are wider (0.2 in τ);
the difference stays identical when λ_A(M₁) > 0. (c) **M₁ satisfies the first term** (𝔞^{(U₀)} ≻ 0 with margin 0.28, 3.9·10⁻³,
0.085, the same order as ζ; and c_E^{old} on V₀^P: 0.296 vs ζ's 0.196) **and fails only β_new ≤ 1**: M₁'s sign is in the pencil
(new negativity against old form), exactly where ζ's is. It is R186_044 §3's reading ("M₁'s sign is in G")
in the old/new partition. (d) c_E on V₀^P (the #comp rank condition with the old prolates) is positive for M₁ at δ ≤ 0.1
at ½log3 → log 2 and only becomes negative in the ½log5 windows at δ = 0.1: a detection threshold like R186_044/115's δ_V.

**Answer to task 3.** The first case holds: M₁ satisfies N2 (in any of its forms with its own margin) and fails
only (N′)+pencil. So **N2 is honest but not new**: the sign stays in the term that is row D. There is no candidate theorem ∀T
of the form "property of Λ ⇒ new negativity invisible from the old prolates": (i) the visible new negativity is the
fission/growth kind at distance 0 from U₀ (there is no scale separation to exploit: the piece (4.24, 6.46) is glued to the zero at 4.24
that the old component (6.9, 10.5) had at 6.95 before splitting); (ii) the "log n vs π/T separation" does not come into play: ν depends on
sup σ⁻ (all primes, old and new, alike) and on Slepian leakage; (iii) Weyl (R186_046 §4.2) prevents a new prime from
having a definite sign in any piece. The only universal thing is Lemma 3.4 (Slepian), with no arithmetic.

## 5. Honesty: inheritance and what remains ∀T

5.1 **Inheritance.** Prop. 2.1 is exact: its margin 1 − β_new = λ_A/𝔞^{(U₀)}(h*) inherits (Lemma T′). Prop. 2.2 does not inherit but its hypothesis
is false in every window (factor 2–17) and, by 3.3, will remain so as long as sup σ⁻·projected leakage ≫ λ_min 𝔞^{(U₀)}; no
T has been found where it holds. Prop. 2.3 does not imply. ν has its own margin (O(1), stable in M) but **carries
no sign information** (§4(a)): it is this memo's only new quantity and it is blind. Lemma 3.4 does not inherit and has no sign.
5.2 **What remains of S2 ∀T after this memo.** R186_046 §5.3's "two-term condition" is rewritten as follows, with no new
object: X_∞(T₀) ⟺ [𝔞^{(U₀)}_T ⪰ 0 on 𝒫_T, ∀T > T₀] ∧ [β_new(T₀,T) ≤ 1, ∀T > T₀]. The first bracket is (N′) in operator form and
holds with margin O(10⁻²…10⁻¹) in every window, for both ζ and M₁ — **if someone proves it ∀T, it does not touch the sign**. The
second is row D with the old/new partition (inherits). The object "new negativity outside U₀ seen by the old prolates,
o(1)" **does not exist as an independent condition**: it is O(1) at finite T (dominated by fission/growth glued to U₀), it is pure
Slepian asymptotically without projection (Lemma 3.4), and on V₀^P it does not even decay because of Tate's polynomial tail (3.3(b)).
What remains OPEN is what was already OPEN: no σ-computable quantity with its own margin decides β_new < 1 (W-loc, W-mom, Lemma T′).
5.3 **What it does contribute.** (i) The old/new partition of the form (Prop. 2.1) as an exact reformulation, with the first term
σ-computable with its own margin in the four windows: a candidate "Prop. (old/new split)" statement for Paper 47 **only** as
structure (equivalent to R186_042 Thm 2.1), never as a criterion. (ii) The "sup × leakage" bound (ν ≤ λ_max Π₀Σs_pS_pΠ₀) tight to a factor of
1.3–1.8: useful for bounding Neg on prolate subspaces without solving the form (same family as R186_047 Lemma 2). (iii) The fact
that Tate's projection makes the polar prolates' leakage polynomial (3.3(b)): relevant for any attempt at (L-W) ∀T
(R186_047 §4.3) — the Slepian bounds for the polar component must be taken on P_𝒫ψ, not on ψ.
5.4 **Labels.** Prop. 2.1 PROVED (identity + Kreĭn); Prop. 2.2 PROVED with a NUMERICALLY false hypothesis; Prop. 2.3 NO-GO with a number
(same wall as R186_046 Prop. 3.1/R186_116); Tables 3.1, 3.3, 4.1 NUMERICAL (M = 48, stable at 40/56; ½log7 and T ≥ 1.25 with partial
Nyquist, declared); Lemma 3.4 PROVED mod. CITED (Slepian, PNT); §4's conclusion "N2 blind to the sign" NUMERICAL (5 values of δ on both
sides of δ_A, two windows). Row D: OPEN. No grid symbol changes; Ω's S2: OPEN, with the second term **eliminated as an
independent object** (reduced to β_new = D).

## 6. Audit notes

- ν is computed as λ_max of a compression of an ⪰ 0 operator to a subspace **inside 𝒫_T** (Q = orth(P_𝒫 V₀), QR with absolute threshold
 10⁻⁸ on 2·#comp full-rank columns; verified dim = 2·#comp in every row): there is no R186_116 §2.1 artifact
 (there W had M−2 rank-deficient columns); c_W ≥ λ_A ≥ 0 holds in every row (1.3·10⁻³ ≥ 3.7·10⁻¹² etc.).
- The pieces of U_T∖U₀ are obtained by exact interval difference (zeros via brentq to 10⁻¹²); "growth/disjoint" is by
 intersection with U₀, not by R186_046 §6's center heuristic.
- Nyquist: at T ≥ 1.25 (table 3.3) and at ½log7 there are unresolved pieces; their weight in ν is ≤ 10⁻³ (per-piece column). ‖Neg^{new}|𝒫_T‖
 (Prop. 2.2) does vary with M (0.073–0.100 at log 2 → ½log5): used only as ≫ λ_min 𝔞^{(U₀)} (0.017).
- Lemma 3.4: the factor ≤ dim V₀ from the non-orthogonality of prolates of distinct components is crude but sufficient for o(1); the
 Slepian asymptotic is CITED, not re-derived; the bound with Σv_n ~ 4e^T uses the PNT (CITED). Not used in any sign
 conclusion.
- ν's "independence of δ" is to 4 digits and is exact in the sense that the quartet modifies σ_T by O(δ²) except in the pieces
 (9.7, 12) and (16.3, 18.5) flanking γ₁ (R186_044 §3.2), where s_p does change (2.03 → 2.04): the effect on ν is 10⁻⁴.
- No equivalence with other statements is used; "(N′)" appears only as the name of R183_031 Thm 1 and is replaced here by
 the operator condition 𝔞^{(U₀)} ⪰ 0, which is σ-computable and mentions no zeros.
