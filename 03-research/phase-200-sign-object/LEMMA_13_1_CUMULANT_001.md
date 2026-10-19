# LEMMA_13_1_CUMULANT_001: Lemma 13.1, the full cumulant form

Phase 200, round 14.
Scripts: `LEMMA_13_1_CUMULANT_001_data/witness.py` (T = 8/5 witness → c(u), h(γ) = ĉ(γ)), `lemma13.py` (defect,
normalization check against ζ, off-line zero search, modulated symbol, real Jensen) and `offline_known.py`
(contribution of LEMMA_E's zeros). Outputs: `lemma13_out.txt` and `offline_known_out.txt`.
Row D and L′♯ are treated as an independent
target; no equivalence with anything is invoked here, not even for ζ_K, Hecke L-functions, or Epstein.

## 0. Summary (≤ 250 words)

**Lemma 13.1 (structural refutation, PROVED).** In the principal class, the defect 𝔇_T = 𝔞^{Q₁} − h⁻¹Σ_χ𝔞^{L_χ}
on P_T is a **pure finite comb**: the conductor, Lévy, and polar terms cancel exactly, and its
frequencies log n are distinct, with n ≥ 2 and no diagonal term. Every nonzero form of that type is **indefinite on P_T**
(modulation argument plus Riemann–Lebesgue). Therefore no Jensen, convexity, or
concavity inequality exists for the window form under arithmetic averages of Euler products with the same Γ, for any h and any T
after the first contact. The sign 𝔇 < 0 observed in the two calibrators is a property of the witness, not a theorem.
**Real Jensen (PROVED):** log E_χ e^{y_χ(σ)} ≥ 0 for σ > 1. **Does not transfer (PROVED):** the transfer would require
weights w_g completely monotone in log n, and by Bernstein's theorem none has compact support.
**Zero side (CITED + PROVED):** 𝔇 = Σ_{ρ(Z)} ĉ(γ_ρ) − h⁻¹Σ_χΣ_{ρ(L_χ)} ĉ(γ_ρ), and the poles contribute exactly 0 on P_T.
**Test (ii) (NUMERICAL, D = −20, T = 8/5):** normalization verified against ζ (400 zeros: 1.93442 versus the template 1.93504).
The two known off-line zero quadruples contribute **−0.7925 = 22.8 %** of 𝔇 = −3.4791 (the one at t = 15.67 alone
contributes −0.709, because ĉ(t ± 0.433i) is not positive). The remaining 77 % is the difference of the other zeros, and that reading
is a rewriting of the comb, blind to the sign (REF-D).
**(iii)** For ζ (h = 1), 𝔇 ≡ 0. The lemma is a tool or class calibrator and gives no information about the sign of ζ.

## 1. Corpus and index

I grepped `05-meta-and-planning/ROUTES-TRIED-INDEX/` for "cumulant," "generating function," "log E," "class group," "Hecke,"
"principal class," "Jensen," "convexity," "log-convex," and "Hölder." What is relevant:
- LEMMA_12_1_H3_001 (README l. 543) leaves alive the object "𝒦 = full log E e^{y} (Lemma 13.1 OPEN)" and declares NO-GO the sign
  of 𝒬^{(h)} (order 2). Here there is no retry of 𝒬: the full 𝒦 is attacked, which is the residue that record left alive.
- COSH_DEFECT_001: the order-2 Hankel is indefinite in g (numerical). What is new in this round is a proof of indefiniteness
  of the **full** defect, for every h and every T, independent of order.
- G6C-R178 (CAR cumulant, DEAD) is a fermionic cumulant of a different object and is not this one.
- Jensen: L22/L50/MW-7/P33-10/INV_P_001 P4 treat Jensen polynomials, hyperbolicity, Jensen-δ, and subharmonic Jensen
  means. None treats the Jensen inequality for a finite measure on Ĉl applied to arithmetic averages of
  Hecke L-functions. The explicit new reason is that the object is the cumulant generating function of the uniform measure
  on Ĉl, and the question is whether its convexity passes to the window form. The answer is negative, with proof (§3).
- R186-PNTcone (log-convexity of λ_A, FALSE) treats a different object and its conclusion is consistent with this one.
- "Hölder" appears only in INV_E_001 (Hölder–Ostrowski hypertranscendence), which is unrelated.

## 2. Framework

Z = Z_{Q₁} = (w/h)Σ_χ L_χ with L_χ = L(s,χ), all with factor Γ_ℝ(s)Γ_ℝ(s+1) and conductor |D|. ζ_K = L_{χ₀} has poles at
0 and 1, and the other L_χ are entire. ℓ_χ = log L_χ, ℓ̄ = h⁻¹Σℓ_χ, y_χ = ℓ_χ − ℓ̄, 𝒦 = log E_χ e^{y_χ}. By Lemma 12.1
(PROVED), Λ_Z = Λ̄ + Λ_def with Λ_def(n) = log n·[n^{−s}]𝒦.

Template (P47 eq:Aform, Lemma E §1.3): for F ∈ P_T = {F ∈ L²(I_T) : ∫F e^{±t/2} = 0}, c = c_F (autocorrelation,
supported on [−2T, 2T], c(0) = ‖F‖²),
  𝔞^L(F) = C₀‖F‖² + ∫₀^{2T}(c(0)−c(u))du/sinh(u/2) + 2c(0)log coth(T/2) − Σ_{log n<2T} 2Λ_L(n)n^{−½}c(log n).
C₀ and the Lévy kernel depend only on (Γ, conductor) and are identical for Z and for each L_χ. Therefore (PROVED)
  **𝔇_T(F) := 𝔞^Z(F) − h⁻¹Σ_χ 𝔞^{L_χ}(F) = −Σ_{2 ≤ n < e^{2T}} a_n c_F(log n),  a_n := 2Λ_def(n) n^{−½}.**   (2.1)
It is a finite comb: it has no diagonal, no Lévy term, no conductor term, and no polar term.

**Dynamic weights (PROVED, trivial).** −Z′/Z = Σ_χ p_χ(s)(−L_χ′/L_χ) with p_χ = (w/h)L_χ/Z and Σ_χ p_χ ≡ 1. For real σ > 1,
each L_χ's coefficients are real (class L with χ and χ̄ joined, LEMMA_12_1 §2.1) and each L_χ(σ) > 0 by the Euler
product, so p_χ(σ) ∈ (0,1) and −Z′/Z(σ) is a convex combination: min_χ ≤ −Z′/Z(σ) ≤ max_χ. On the critical line the p_χ are
complex and depend on s, so Λ_Z is not an average of the Λ_χ with fixed weights, and 𝔞^Z is not an average of forms. The
cumulant expansion (Lemma 12.1) is the exact form of that "dynamically weighted average."

## 3. Lemma 13.1

**Lemma 13.1 (PROVED).** Let C₀ be the principal class and T > 0 such that there exists n < e^{2T} with Λ_def(n) ≠ 0. Then the quadratic
form F ↦ 𝔇_T(F) is **indefinite** on P_T: there exist F₊, F₋ ∈ P_T with 𝔇_T(F₊) > 0 > 𝔇_T(F₋). More precisely, if F₀ = 1_{I_T},
  lim sup_{λ→∞} 𝔇_T(F_λ)/‖F_λ‖² = sup_λ φ(λ) > 0,  lim inf = inf_λ φ(λ) < 0,
  φ(λ) := −(2T)⁻¹ Σ_n a_n (2T − log n) cos(λ log n),
where F_λ is the orthogonal projection onto P_T of F₀(t)cos(λt).

*Proof.* (1) Riemann–Lebesgue: ∫F₀(t)cos(λt)e^{±t/2}dt → 0. The projection onto P_T (which has codimension 2) changes
F₀cos(λ·) by o(1) in L², and 𝔇_T is a bounded form on L²(I_T), because |c_F(ℓ)| ≤ ‖F‖² and the comb is finite. Hence
𝔇_T(F_λ) = 𝔇_T(F₀cos λ·) + o(1) and ‖F_λ‖² = T + o(1).
(2) c_{F₀cosλ}(ℓ) = ∫F₀(t)F₀(t+ℓ)cos(λt)cos(λ(t+ℓ))dt = ½cos(λℓ)(2T−ℓ) + ½∫_{I_T∩(I_T−ℓ)} cos(λ(2t+ℓ))dt, and the last term
is O(1/λ). So 𝔇_T(F₀cosλ·)/T → φ(λ) + o(1), with the ‖·‖² ≈ T normalization absorbed into the constant (2T)⁻¹.
(3) The frequencies log n are distinct and φ contains at least one nonzero coefficient, because 2T − log n > 0 at the contact where
Λ_def(n) ≠ 0. φ is a nonzero real trigonometric polynomial with zero Bohr mean (no constant term, because n ≥ 2).
Such a polynomial takes values > 0 and < 0: if φ ≥ 0, zero mean plus continuity force φ ≡ 0, and independence of the cos(λℓ_n)
for distinct ℓ_n gives a_n ≡ 0, a contradiction. By almost-periodicity, these values recur for arbitrarily large λ.
Combining with (1) and (2) yields F_± for large λ. ∎

**Corollary 13.2 (PROVED).** For no h ≥ 2, no D, and no T after the first contact does "𝔞^{Q₁} ≤ 𝔞̄" or
"𝔞^{Q₁} ≥ 𝔞̄" hold on P_T. Nor does any concavity or convexity inequality of the window form under arithmetic
averages of Euler products with the same (Γ, conductor). For h = 2 (D = −20), Λ_def(6) = 2log 6 − 0 ≠ 0, and log 6 < 2T
when T > 0.896. For h = 3 (D = −23) the first contact is n = 4. The observations 𝔇 = −3.479 (h = 2) and −0.532 (h = 3)
at T = 8/5 are **of the witness**: LEMMA_E's witness was optimized to minimize 𝔞^Q, and that is why it aligns with the
negative direction of 𝔇.

*Comment on the non-principal class.* There Λ_C contains the constant log m_C, and (2.1) acquires the diagonal term
−2log m_C·‖F‖². Hence the limit symbol is −2log m_C + (zero-mean polynomial), and the proof only gives indefiniteness if
the polynomial's amplitude exceeds 2log m_C. For Q₂ (D = −23) the sign depends on the data (OPEN, not computed).

**Proposition 13.3 (real Jensen and non-transfer, PROVED).**
(a) For real σ > 1, y_χ(σ) ∈ ℝ and 𝒦(σ) = log E_χ e^{y_χ(σ)} ≥ E_χ y_χ(σ) = 0 (Jensen, convexity of exp). Equality holds
only if all y_χ(σ) are equal. Equivalently, Z(σ) ≥ w·Π_χ L_χ(σ)^{1/h} (arithmetic mean ≥ geometric mean:
the arithmetic mean of positive real L's dominates their geometric mean, which is the L_θ of Theorem S).
(b) Let κ(n) = [n^{−s}]𝒦. The family of inequalities "Σκ(n)n^{−σ} ≥ 0 for all σ > 1" implies Σκ(n)v(n) ≥ 0 exactly
for weights v(n) = ∫_{(1,∞)} n^{−σ}dμ(σ) with μ ≥ 0, and only for those within this family. The window weight is
v_g(n) = log n·n^{−½}c(log n). If v_g = ∫n^{−σ}dμ, then u ↦ u e^{−u/2}c(u) would be completely monotone for u > 0 and, by
Bernstein's theorem, the Laplace transform of μ ≥ 0, which is real-analytic for u > 0. Since c vanishes for u > 2T, it would follow that μ = 0.
**No nonzero compactly supported window inherits the Jensen sign.** ∎
(c) The same holds for Hölder convexity in the mixing variable. The function θ ↦ log Σ_χ θ_χ L_χ(σ) is concave in the
weights θ (C-θ: it is convexity in θ, filtered), and its derivative at the window is again an indefinite comb by Lemma 13.1.

**Answer to the target's question.** The full cumulant form has no uniform sign structure in g beyond what
its order 2 already has: both are zero-mean finite combs and are therefore indefinite. The only sign structure of
𝒦, Jensen on the real axis, lives in a cone of weights (completely monotone ones) that is disjoint from the windows.

## 4. Zero side and test (ii)

**Proposition 13.4 (CITED: Weil's explicit formula for L-functions with FE and finitely many poles; PROVED: cancellations).** For F ∈ P_T,
with ĉ(γ) := ∫c(u)e^{iγu}du (for real γ, ĉ = |F̂|² ≥ 0; for complex γ it is entire and even),
  𝔇_T(F) = Σ_{ρ: Z(ρ)=0} ĉ(γ_ρ) − h⁻¹Σ_χ Σ_{ρ: L_χ(ρ)=0} ĉ(γ_ρ),  ρ = ½ + iγ_ρ,  nontrivial zeros with multiplicity.
The poles contribute **exactly 0**: the poles of Z and ζ_K at 0 and 1 give ĉ(±i/2) = |∫F e^{±t/2}|² = 0 on P_T (Tate
conditions). This holds even though the pole of Z has order 1 and that of the average h⁻¹·(order of ζ_K) has "order 1/h": the
order difference is also multiplied by zero.
Each sum converges absolutely because ĉ = O(γ^{−2}). The identity is comb (2.1)'s explicit formula, so the
"zero side" is a rewriting of 𝔇's data and gives no new information about its sign (REF-D, blind).

**Normalization (NUMERICAL).** The same ĉ summed over the first 400 zeros of ζ (±γ) gives 1.93442 (50: 1.93105; 200: 1.93382),
against the template for ζ (C₀ = −5.37218, Lévy +5.86243, comb +1.44479) = **1.93504**. Convergence is monotone toward
the template value, and the residue (6·10⁻⁴) is the zero tail. The normalization ĉ = Σ_ρ is confirmed.
(The smoothed-density tail estimate printed by the script overestimates, because the trapezoid does not average the oscillation
of ĉ; I discard it.)

**Off-line zeros of Z_Q, D = −20, T = 8/5 (NUMERICAL).** A quadruple {ρ, 1−ρ̄, ρ̄, 1−ρ} with ρ = ½ + δ + it contributes
2[ĉ(t−iδ) + ĉ(t+iδ)] = 4∫c(u)cos(tu)cosh(δu)du, which has no fixed sign. The same four zeros placed on the line at
heights ±t would contribute 4ĉ(t) ≥ 0.

| zero (LEMMA_E) | δ | quadruple | on-line equivalent | excess |
|---|---|---|---|---|
| 0.932970 + 15.668250i | 0.433 | **−0.709151** | +0.016635 | −0.7258 |
| 0.937667 + 29.983395i | 0.438 | **−0.083338** | +0.007627 | −0.0910 |
| known total | | **−0.792489** | | |

This is **22.8 %** of 𝔇 = −3.479097, which I reproduced from comb (2.1) in the script, matching COSH_DEFECT.
**Higher zeros.** |ĉ(t ± iδ)| ≤ 1.5·10⁻³ for t ≥ 40 and ≤ 1.3·10⁻⁴ for t ≥ 100, with δ ≈ 0.43. LEMMA_E (argcount) certifies
that there are no zeros in [0.52, 1.6] × [0.1, 30] other than the two in the table. The Newton search above 30 is in
`lemma13_out.txt` (§4′, below). Even with several quadruples in [30, 60], their total contribution stays |·| ≲ 10⁻². Estimate:
off-line contribution = −0.79 ± 0.02 (NUMERICAL, not rigorous: there is no certified count above t = 30 nor
for 0.5 < σ < 0.52).

**Breakdown (NUMERICAL).** 𝔇 = −3.479 = (poles) 0 + (off-line quadruples) ≈ −0.79 + (rest) ≈ −2.69. The rest is
Σ_{zeros of Z with Re = ½} ĉ − h⁻¹Σ_χΣ_{ρ(L_χ)} ĉ. One must be honest about what this means:
- That rest is **not** "a zero-density deficit on the line" in any independent sense. Z and the average have the
  same leading counting term (same Γ and conductor) and the same total number of zeros up to O(log t). The difference is
  in the fine positions, i.e., in each function's S(t) terms, and by the explicit formula those S(t) tested
  against ĉ are exactly comb Λ_def. Writing −2.69 as a "density deficit" is rewriting (2.1) from the zero side:
  blind (REF-D). Moreover, Z has 4 off-line zeros for |t| < 30 that the average does not have, and the total count still forces
  Z to have 4 fewer zeros on the line somewhere nearby. That only redistributes ĉ among zero classes, which is
  exactly what the "excess" column measures.
- The −0.726 excess of the t = 15.67 quadruple is the part unambiguously attributable to "being off the line," and includes the factor
  cosh(δu) in ĉ. It is large because ĉ(15.67) is nearly zero (0.0040: minimum of the witness's |F̂|²) while
  ∫c cos(tu)(cosh(δu)−1) is not. The optimized witness concentrates its spectrum far from t ≈ 15.7, and the quadruple "shows up" via
  the cosh deformation.
- Conclusion of test (ii): the target's hypothesis, "off-line zeros are high up, ĉ decays and they do not contribute," is **false in the
  witness**: they contribute 23 % and with the same sign. The alternative "𝔇 < 0 is a density fact on the line" is not
  a new statement, because the remaining 77 % is the comb seen from the other side. Neither reading gives a sign.

## 4′. Search for zeros above t = 30 (output of `lemma13.py`, NUMERICAL)

The grid Newton search (0.505 < σ < 2.5, t < 60; not certified) found 5 more quadruples:
0.6969+36.374i (+0.0036), 0.8232+44.000i (−0.0007), 0.6349+46.758i (+0.0009), 0.5974+52.743i (+0.0017),
0.8112+58.508i (+0.0024). **Total off-line with t < 60: −0.7846 (22.6 % of 𝔇).** The higher zeros do not change
the conclusion. Real Jensen verified: log cosh y(σ) = 0.808, 0.376, 0.133, 0.021 at σ = 1.2, 1.5, 2, 3.

## 5. Filters

- **C-pol (nothing via moments A, B):** passes. The polar terms are exactly 0 on P_T (Prop. 13.4) and are not used.
- **C-data (nothing that is an equality between data):** Lemma 13.1 is not an equality, it is a proven indefiniteness. Prop. 13.4
  **is** an equality between data (comb = zero side): I record it as a rewriting and do not ask it for a sign.
- **C-hom (nothing quadratic in θ):** passes. Lemma 13.1 is linear in the comb and quadratic in F, not in θ.
- **C-θ (nothing linear or convex in θ):** Prop. 13.3(c) (Hölder convexity in the mixing weights) falls under C-θ, and I
  explicitly discard it as a sign source. Lemma 13.1 confirms why it falls: its derivative at the window is a
  zero-mean comb.
- **REF-D:** the zero side (§4) and the "density on the line" reading are REF-D/blind. Lemma 13.1 is not REF-D: it is a
  proven structural NO-GO on a declared class of methods.

## 6. (iii) What does this teach for ζ?

For ζ there is no class group (h = 1): y ≡ 0, 𝒦 ≡ 0, and 𝔇 ≡ 0. Lemma 13.1 is a theorem about **Epstein/classes**: it says
the class defect of any principal form is a perturbation by a pure, indefinite comb, whose sign on a given
witness depends entirely on the witness. As a tool it serves to:
(a) calibrate C-E′: any sign argument for 𝔞 that "passes" to the arithmetic average Z_{Q₁} and does not distinguish 𝔞^{Q₁} from 𝔞̄
must fail at some F, because the difference is indefinite. A falsifier built like Epstein attacks exactly that
direction.
(b) mechanically explain why Epstein breaks at T ≈ 1.58: the witness finds the negative direction of comb 𝔇,
which for h = 2 is dominated by the composite contact n = 6, and an off-line quadruple pushes in the same direction.
It says nothing about the sign of 𝔞^ζ, and I do not claim it does.

## 7. Labels

- **PROVED:** (2.1) pure comb; dynamic weights and convex combination at real σ > 1; **Lemma 13.1** (indefiniteness of 𝔇_T on
  P_T, every h, principal class, T after the first contact); Cor. 13.2; Prop. 13.3 (real Jensen; non-transfer by
  Bernstein); polar cancellation in Prop. 13.4.
- **CITED:** Weil's explicit formula (Prop. 13.4); Hecke; existence of off-line zeros (Davenport–Heilbronn).
- **NUMERICAL:** limit symbol φ(λ) (D = −20, T = 8/5, contacts 4, 6, 9, 14, 16, 21) with max +3.262, min −3.398, and mean 3·10⁻⁴ for λ ∈ [0, 300] (Lemma 13.1 visible in the data); 𝔇 = −3.4791; normalization against ζ (1.93442 versus 1.93504); quadruples −0.7092, −0.0833 (22.8 %); bounds on complex
  ĉ; modulated symbol (output (4) of `lemma13.py`).
- **ARGUED:** the readings in §4 (excess via cosh deformation, "density" = rewriting); §6(b).
- **NO-GO:** Jensen, convexity, or concavity inequality for the window form under arithmetic averages with the same Γ;
  sign of the full 𝒦 as a functional of g; transfer of real Jensen to compactly supported windows.
- **OPEN:** sign of 𝔇 in the non-principal class (there is a diagonal −2log m_C); L′♯; row D.

## 8. New restriction

**Restriction (13.1):** the difference between the window form of a combination of L-functions with the same (Γ, conductor) and
any fixed average of their forms is a finite comb with no diagonal, and is therefore indefinite on P_T. No sign lemma
can rely on "convexity, concavity, Jensen, or Hölder under mixing of L-functions with the same Γ." An observed sign of that
difference on a witness is a property of the witness. The positivities at real σ > 1 (Jensen or AM–GM) do not pass to
compactly supported windows (Bernstein).

## 9. Entry for the index (ROUTES-TRIED-INDEX)

- **LEMMA_13_1_CUMULANT_001 (round 14, full cumulant form):** 𝔇_T = 𝔞^{Q₁} − 𝔞̄ is a pure finite comb (conductor,
  Lévy, and poles cancel) ⇒ **indefinite on P_T for every h, D, and T after the first contact (PROVED, modulation + R–L)**:
  NO-GO for Jensen, convexity, or Hölder of the window form under arithmetic averages of L-functions with the same Γ. Real Jensen
  𝒦(σ) ≥ 0 PROVED but does not transfer (Bernstein: completely monotone weights have no compact support). Zero side
  CITED (poles = exactly 0 on P_T); NUM D = −20, T = 8/5: the off-line quadruples contribute −0.79 (22.8 %) of −3.479.
  The rest, "density deficit," is the comb rewritten (REF-D). For ζ, 𝔇 ≡ 0: it is a C-E′ calibration tool
  and gives no sign. Do not retry the sign of 𝒦 or of 𝒬 as a functional of g.

## 10. Next lemma

**Lemma 14.1 (proposed): relative pencil (𝔞̄, 𝔇) on the non-principal class and on the cone {𝔞̄ ≤ ε}.** Since 𝔇 is indefinite, the
only surviving sign question is relative: inf{𝔇(F) : F ∈ P_T, ‖F‖ = 1, 𝔞̄(F) ≤ ε}. This is the generalized eigenvalue
of the pencil, and measures how much of the near-null cone of the Euler average points toward the negative direction of the class comb. It needs to be
computed for h = 2, 3, together with the sign of the symbol −2log m_C + φ in the non-principal class (Q₂, D = −23), where the
diagonal breaks Lemma 13.1. New reason versus COSH_DEFECT and LEMMA_12_1: the object is the restricted pencil and not 𝒬 or 𝒦
in isolation. Before launching it, grep the index for "pencil," "generalized eigenvalue," and "near-null cone."
