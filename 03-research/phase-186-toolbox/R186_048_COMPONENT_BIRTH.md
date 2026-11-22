# R186_048 — Birth of negative components and migration of the minimizer: exact geometry, invisibility at the instant of entry, cost of the new prime, and why the perturbative argument does not close

Phase 186, round 22. Paper 46,
the grid and the crossword are not touched. Self-contained script: `r048_birth.py` (M = 40/48, ≈ 30 s + 60 s for part E; `python3 r048_birth.py [fast|E]`).
Read: R186_046 §0.3(iii), §3.2, §6 (70% in [4.24, 6.46]); R186_042 (sub-Shannon sea); R186_043 §3 (Lemma M0, M0-slope),
§5–§7 (transfer, M₁); R186_044 Thm 2, Lemma P; R186_047 (L-W); R186_036 Lemma 2 (fold, CONDITIONAL (REG)); R165_202 1.4–1.5;
R186_022 (peak of h*); Paper 46 eq:symbol/eq:form, prop:band, lem:contA, lem:monoT; grid log 25–36 (W-lin, W-det, W-fam, W-pat,
W-loc, W-mom). Nothing already closed is repeated: there is no local criterion on σ here, nor a functional of the family; the object is the entry
dynamics of each prime power and its exact cost.

## 0. Verdict

1. **Geometry (§2, PROVED from σ alone).** When n enters at T_n = ½log n the symbol jumps σ_{T_n⁻} → σ_{T_n⁻} − v_n cos(τ log n).
 A new negative component is a connected component of {σ_{T_n⁻} < v_n cos(τ log n)} disjoint from U_{T_n⁻}; it is born with **mass
 O(1)** (0.15–1.6 at n = 3, 5, 7; not → 0) and with **Shannon number < ½** (Lemma 2.3, PROVED: a component ex nihilo fits in a
 positive half-period of the cosine, |J| < π/log n ⇒ N_J(T_n) < T_n/log n = ½; measured 0.10–0.43). There are **three types** of creation:
 ex nihilo (at a positive local minimum of σ_{T_n⁻} aligned with cos ≈ 1), **fission** (an old component split in two by
 a positive lobe of the new cosine) and deformation. **Law**: the only law is the criterion itself; among the candidate local minima
 (0 < σ_{T_n⁻} < v_n), the one born is exactly the one with max(v_n cos − σ_{T_n⁻}) > 0 (tautology), and neither "lowest frequency" (fails at
 n = 4, 8, 9) nor "deepest minimum" (fails at n = 4, 5, 8) predicts it; the alignment cos(τ_min·log n) is Weyl-equidistributed
 (R186_046 §4.2) ⇒ **there is no arithmetic law for which candidate is born**. What does hold: new low-frequency components
 (τ < 12) only by fission (n = 3: [4.8, 7.3]; n = 5: [7.0, 8.8]) or, for the first time ex nihilo, at n = 7 ([8.98, 10.36], mass 0.45).
2. **Invisibility at the instant of entry (Lemma 2.2, PROVED, elementary).** 𝔞_{T_n}⁺ ≡ 𝔞_{T_n}⁻ on L²(I_{T_n}): for every F,
 ∫cos(τ log n)|F̂|² = 2π c_F(log n) = 0 because log n = 2T_n lies at the boundary of c_F's support. The new component **captures
 nothing** at birth — neither locally nor through coupling: its negative lobe cancels exactly against the positive lobes
 of the same cosine **for every F, to every order**. Consequence: λ_A and h* are continuous at T_n (lem:contA), and "the fraction of Neg(h*)
 in new components" jumps at T_n (it is bookkeeping: 2.6% at n = 3 with the same vector). The premise "mass → 0 at
 birth" is false in σ; what → 0 is the **visibility** c_F(log n) (Lemma 2.4: |c_F(log n)| ≤ ‖F‖²_{boundary strips of width
 2ε}, ε = T − T_n, PROVED; matches to a factor of 2–3 at h*).
3. **Migration (§3, NUMERICAL).** h* **does not** move to the ex nihilo components: its negative mass in them goes 2.5% → 0.7% over
 (T_3, T_4), 0.0% over (T_4, T_5) and (T_5, T_7) (they lie at τ ≥ 16, outside the 6.9–7.5 peak of |ĥ*|²). **The 70% of R186_046 in
 [4.24, 6.46] is not a born component: it is a fission product** — genealogy: (6.945, 10.531) ∈ U_{½log3} (ex nihilo at n = 2,
 adjacent to m's zero at 6.29) → split by 3 into (4.816, 7.272) + (9.666, 11.966) → deformed by 4 into (4.237, 6.458); reproduced:
 0.1577/0.2244 = 70.3%. At ½log7 (λ_A at the 10⁻¹⁴ floor of M = 48: h* not resolved) the bookkeeping suggests the peak jumps from
 6.5 to 9.5 toward the ex nihilo [8.98, 10.36]: **not claimed** (NUMERICAL, unresolved).
4. **The sign after creation (§4): the perturbative argument does NOT close.** The exact cost of the new prime D(ε) := λ_A^{without n}(T_n+ε)
 − λ_A(T_n+ε) grows as ε^{1.2–1.5} (not ε¹: R186_036 Lemma 2's fold is not seen; h*(±T_n) = −0.048, −8·10⁻⁴, ≈ 0 at n = 3, 4, 5)
 and **exhausts the inherited margin λ_A(T_n) at ε* ≈ 0.037, 0.02, 0.006** (n = 3, 4, 5), i.e. at 25%, 18%, 4% of the interval
 until the next birth (0.144, 0.112, 0.168). Beyond ε* the new prime costs 7–10⁴ times λ_A and positivity is sustained by the
 global reorganization of h* (the full problem). The only margin available is λ_A(T_n): **it inherits**. The local M0-slope
 threshold (T_c(J) = √(2b₁/(0.7·mass)), from σ) gives "no component crosses before ½log7" (T_c ≥ 0.87 ≫ T_next
 in every case) while λ_A falls from 10⁻³ to 10⁻²¹: **the σ-computable threshold does not govern the sign** (W-loc, seen from birth onward).
5. **Falsifier (§5).** M₁(δ = 0.1) has the same births as ζ at log 2 (ex nihilo at 62.6 and 108.5, plus one of mass 0.005
 at 35.2) and changes sign at T ≈ 0.573 ∈ (T_3, T_4) = (0.549, 0.693), **between boundaries, not at one**: exactly where the
 perturbative argument already says nothing. Consistent with 4.
6. **Contact with the sign: none.** Row D: OPEN. Nothing here bounds λ_A from below with its own margin.

## 1. Framework and own verifications

Notation (Paper 46): σ_T(τ) = m(τ) − Σ_{log n < 2T} v_n cos(τ log n), v_n = 2Λ(n)/√n; 𝔞_T(F) = (1/2π)∫σ_T|F̂|² = C₀‖F‖² + Lev(c_F)
− Σ v_n c_F(log n) (eq:Aform), c_F(u) = ∫F(t)F(t−u)dt, supp c_F ⊂ [−2T, 2T]; 𝒫_T = {A(F) = B(F) = 0}; λ_A(T) = min 𝔞_T|𝒫_T; h*_T
unit minimizer. Boundary convention (R186_046 §1): at T = T_n exactly, n is not yet contact; σ_{T_n⁻} := without n, σ_{T_n⁺} := with n.
U_T := {σ_T < 0} ∩ [0, ∞) (finite union, prop:band). Neg(h*)|_J := (1/2π)∫_{±J} σ_T⁻|ĥ*|². "New" := a component of U_{T_n⁺}
disjoint from U_{T_n⁻} (overlap criterion; differs from R186_046 §6's center-based heuristic, see §3).
- λ_A: 9.4858·10⁻⁴ (½log3, M = 40; R186_043: 9.4858·10⁻⁴), 1.0421·10⁻⁷ (log 2; R186_046: 1.03·10⁻⁷), 3.65·10⁻¹² (½log5, M = 48;
 R186_046: 3.65·10⁻¹²); at ½log7, 3.6·10⁻¹⁴ = floor (R187 mp: 10⁻²¹): used only as "unresolved".
- Lemma 2.2 with a number: max|A_{T_n}⁺ − A_{T_n}⁻| = 0 (exact in arithmetic: C(log n) = 0 because the integration interval is empty).
- Negative sets: U_{½log3}, U_{log2} (6 comp.), U_{½log5} (8 comp., zeros 1.982, 4.237, 6.458, 8.738, 11.293, …, 108.95)
 identical to R186_034/043/046; U_{½log7}: 17 comp.; U_{½log8}: 29; U_{½log9}: 30 (up to τ = 250).
- Mass·T/π = component's Shannon number: the new ones at n = 3: N = 0.392, 0.241, 0.171 (= T_n|J|/π) < ½ (Lemma 2.3).
- 70% of R186_046: 0.1577/0.2244 = 70.3% in [4.24, 6.46] with M = 48 (R186_046: 0.159/0.225, M = 48). ✓
- First order of D(ε) = v_n c_{h*}(log n) (Hellmann–Feynman): D/first order = 0.85, 0.79, 0.72, 0.57 (n = 3, ε = 0.002 … 0.016):
 the first order overestimates, as expected for a negative perturbation of a minimum (second order ≤ 0). ✓
- Strip bound (Lemma 2.4) ≥ |v_n c_{h*}(log n)| at every point (ratio 2–12). ✓
- M₁(δ = 0.1, log 2): −1.474·10⁻³, n₋ = 2 (R186_043: −1.474·10⁻³ with M = 40). ✓

## 2. Geometry of creation (from σ alone)

**Lemma 2.1 (exact criterion; PROVED, trivial).** U_{T_n⁺} = {σ_{T_n⁻} < v_n cos(τ log n)}. A component J of U_{T_n⁺} is new
(J ∩ U_{T_n⁻} = ∅) if and only if σ_{T_n⁻} ≥ 0 on J, and then cos(τ log n) > σ_{T_n⁻}(τ)/v_n ≥ 0 on J. Necessary condition: J
contains a point with σ_{T_n⁻} < v_n, and every new J contains (or borders) a local minimum of σ_{T_n⁻} with value in (0, v_n), except
at n = 2 (σ_{T_2⁻} = m is monotone: the new (6.945, 10.531) is born adjacent to m's zero at 6.29). ∎

**Prop. 2.2 (types of creation; PROVED as a classification, NUMERICAL in the table).** For J ∈ U_{T_n⁺}: *ex nihilo* if J ∩ U_{T_n⁻}
= ∅; *fission* if the K ∈ U_{T_n⁻} intersecting J also intersects another J′ ∈ U_{T_n⁺} (K splits); *deformed* otherwise. Table (τ < 70):

| n | T_n | v_n | ex nihilo (J; mass; N_J) | fission | candidates (local min. 0 < σ⁻ < v_n) → born |
|---|---|---|---|---|---|
| 2 | 0.347 | 0.980 | (6.945, 10.531); 1.454; 0.396 | — | — (m monotone) |
| 3 | 0.549 | 1.269 | (16.25, 18.49); 1.556; 0.392 · (27.56, 28.94); 0.369; 0.241 · (45.15, 46.13); 0.151; 0.171 | (6.945,10.531) → (4.82,7.27)+(9.67,11.97) | 5 → 2 |
| 4 | 0.693 | 0.693 | (62.62, 63.78); 0.394; 0.256 · (108.5, 108.95); 0.026; 0.101 | — | 4 → 2 (the deepest, 34.7 with σ⁻ = 0.09, cos = −0.56: not born) |
| 5 | 0.805 | 1.440 | (22.60, 23.74); 0.620; 0.291 · (34.47, 35.93); 1.167; 0.374 · 6 more at τ ≥ 73 | (8.74,11.29) → (7.03,8.80)+(10.58,12.35) | 14 → 4 |
| 7 | 0.973 | 1.471 | **(8.98, 10.36); 0.451; 0.426** · (38.6, 39.4); 0.294 · (51.0, 51.6); 0.153 · (54.3, 55.3); 0.728 · (57.9, 58.5); 0.226 · 6 more | (15.97,19.28) → (15.54,16.98)+(18.40,19.76) | 21 → 6 |
| 8 | 1.040 | 0.490 | (190.4, 190.7); 0.034; 0.115 · (132.4, 132.5); 3·10⁻⁴ | — | 8 → 1 |
| 9 | 1.099 | 0.732 | (154.4, 155.0); 0.141 · (222.6, 223.1); 0.207 · (226.0, 226.5); 0.129 | — | 7 → 3 |

Mass decomposition of an ex nihilo component: mass = ∫_J v_n cos − ∫_J σ_{T_n⁻} (e.g. n = 3, [16.25, 18.49]: 2.118 − 0.562 = 1.556):
the new mass is of order v_n·|J| ≈ v_n·π/log n, **O(1) at birth**, not small.

**Lemma 2.3 (birth Shannon number < ½; PROVED).** Every ex nihilo component J of U_{T_n⁺} satisfies N_J(T_n) := T_n|J|/π < ½.
*Proof.* By Lemma 2.1, cos(τ log n) > 0 on J and J is connected, so J is contained in a positive half-period of the cosine, of
length π/log n; hence |J| < π/log n and N_J(T_n) < T_n/log n = ½. ∎ (Measured: maximum 0.426 at n = 7.) It is the birth
version of R186_042's "sub-Shannon sea" (there N_i ≤ 0.95 measured for every component; here < ½ proved for those that are born).
Fission components do not obey the bound (they inherit the mother's length) and are the only low-frequency ones up to n = 7.

**Obs. 2.4 (a law?; NUMERICAL + negative PROVED).** Among the candidates (local minima of σ_{T_n⁻} with 0 < σ⁻ < v_n), the exact subset
born is the one with max_{neighborhood}(v_n cos(τ log n) − σ_{T_n⁻}) > 0 — this is the criterion, not an additional law. (i) "The one with
lowest frequency is born": fails at n = 4 (34.7 no, 63.0 yes), 8, 9. (ii) "The deepest one is born": fails at n = 4, 5 (91.0 with σ⁻ =
0.03 is not born: cos = −0.42), 8. (iii) "The most aligned one is born": tautological. The alignment at candidate τ_min is cos(τ_min log n),
and the τ_min of U_{T_n⁻} lie at distance < δ/log 2 from 2πk/log 2 (prop:align), so cos(τ_min log n) ≈ cos(2πk·log n/log 2) is
Weyl-equidistributed in k (R186_046 §4.2, PROVED): **which candidate is born obeys no simple arithmetic law**; only Lemma 2.3's
bound and the mass ≈ v_n·(half-period) are universal.

## 3. Migration of the minimizer (NUMERICAL, M = 40/48)

**Lemma 3.1 (invisibility at birth; PROVED).** For every F ∈ L²(I_{T_n}): (1/2π)∫cos(τ log n)|F̂|²dτ = c_F(log n) = 0,
because c_F is supported on [−2T_n, 2T_n], is continuous, and log n = 2T_n. Hence 𝔞_{T_n}⁺(F) = 𝔞_{T_n}⁻(F), λ_A(T_n⁺) = λ_A(T_n⁻),
h*_{T_n⁺} = h*_{T_n⁻}. ∎ Reading: the new negative lobe (mass O(1), Lemma 2.2) cancels **exactly** against the positive lobes
of the same cosine as seen by |F̂|², for every F, with no approximation. That is why "Neg(h*) in new components" jumps at T_n with
nothing actually changing: n = 3: 0 → 0.0065 (2.6% of 0.2467) with the same vector; n = 4, 5: 0 → 0 (the new ones are at τ ≥ 62); n = 7: 0 →
0.0637 (27.7%, in [8.98, 10.36]), but h*_{½log7} is not resolved (λ_A at the floor).

**Lemma 3.2 (visibility bound; PROVED).** Let T = T_n + ε, u = log n = 2T − 2ε. Then c_F(u) = ∫_{−T}^{−T+2ε} F(t)F(t+u)dt and
|c_F(log n)| ≤ ‖F·1_{[−T,−T+2ε]}‖·‖F·1_{[T−2ε,T]}‖ ≤ ½(‖F‖²_{left strip} + ‖F‖²_{right strip}) =: ‖F‖²_{edge,ε}. ∎ The new prime only
sees F's mass in the two boundary strips of width 2ε: it is a **time-domain** quantity, not a local datum of σ.
For F antisymmetric and concentrated in the strips, c_F(log n) → −½‖F‖² and the term −v_n c_F = +v_n/2 > 0: the new prime **helps**
in the odd boundary sector and **costs** in the even one (it is the ∓ of R186_036 Lemma 2). With a number: the "without n" form at T_n + ε becomes
very negative as soon as ε ≳ 0.02 (n = 3: −2.4·10⁻² at ε = 0.032; n = 4: −2.4·10⁻⁵ at 0.016, −2.4·10⁻² at 0.032) — the entering prime
is necessary for the positivity of the odd boundary F's; its cost for h* (even) is what D(ε) measures in §4.

**Table 3.3 (migration over (T_n, T_next]).** Fraction of Neg(h*) in new components (overlap criterion), peak of |ĥ*|²:

| n | ε = 0.004 | 0.012 | 0.03 | 0.06 | T_next | peak of |ĥ*|² (T_n → T_next) | ε* (D = λ_A(T_n)) | T_next − T_n |
|---|---|---|---|---|---|---|---|---|
| 3 | 2.5% | 2.3% | 1.9% | 1.3% | 0.7% | 7.53 → 7.10 | ≈ 0.037 | 0.144 |
| 4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 7.10 → 6.90 | ≈ 0.020 | 0.112 |
| 5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 (floor) | 6.90 → 6.79 | ≈ 0.006 | 0.168 |
| 7 | 10.8% | 10.5% | 49.7% | 40.7% | — | 6.49 → 9.49 → 8.90 (unresolved) | — | 0.067 |

**Reading.** (a) h* **never moves to an ex nihilo component** for T ≤ ½log7: its negative mass in them decreases with ε (n = 3) or is
zero (n = 4, 5). The real "migration" is toward the low-frequency fission products (the 70% in [4.24, 6.46], §0.3), which are not
born: they are inherited and deformed. (b) The peak of |ĥ*|² drifts slowly downward (7.5 → 6.8 from ½log3 to ½log7⁻, as in R186_022,
"≈ 4/T" up to correction) and never jumps at any birth (continuity, Lemma 3.1). (c) At n = 7 the ex nihilo [8.98, 10.36] falls for the
first time within the peak's range; the bookkeeping at the numerical floor suggests a migration (peak 6.5 → 9.5), but λ_A ≈ 10⁻¹⁴
is M = 48's floor and the vector is unreliable: **OPEN / NUMERICAL unresolved** (would need mp, R187). (d) Mass threshold for
moving: none observed; the ex nihilo components of mass 1.56 (n = 3, τ = 17) and 1.17 (n = 5, τ = 35) do not receive h*: what decides
is the frequency relative to the peak, not the mass (consistent with R186_040: the head lives at τ < 12).

## 4. The sign after creation: the exact cost of the new prime

**Def. 4.1.** D_n(ε) := λ_A^{without n}(T_n + ε) − λ_A(T_n + ε), where λ_A^{without n} is the minimum of the form with the term −v_n c_F(log n)
removed (same window, same 𝒫_T). It is the exact cost of n's entry; to first order D_n(ε) = v_n c_{h*_{T}}(log n)
(Hellmann–Feynman), and D_n(0) = 0 (Lemma 3.1).

**Table 4.2 (NUMERICAL).**

| n | ε | λ_A(T_n+ε) | D_n(ε) | v_n c_{h*}(log n) | local exponent p (D ∝ ε^p) | D/λ_A(T_n) |
|---|---|---|---|---|---|---|
| 3 | 0.002 / 0.004 / 0.008 / 0.016 | 8.72e-4 / 7.98e-4 / 6.64e-4 / 4.51e-4 | 2.28e-5 / 5.71e-5 / 1.42e-4 / 3.34e-4 | 2.70e-5 / 7.20e-5 / 1.99e-4 / 5.86e-4 | — / 1.32 / 1.32 / 1.23 | 0.024 / 0.060 / 0.150 / 0.352 |
| 4 | 0.002 / 0.004 / 0.008 | 8.86e-8 / 7.50e-8 / 5.33e-8 | 3.30e-9 / 9.16e-9 / 2.57e-8 | 3.70e-9 / 1.12e-8 / 3.92e-8 | — / 1.47 / 1.49 | 0.032 / 0.088 / 0.246 |
| 5 | 0.004 / 0.012 / 0.03 | 2.43e-12 / 1.04e-12 / 1.7e-13 | (1st order) 1.88e-12 / 2.73e-11 / 4.6e-10 | — | ≈ 2.4 | 0.52 / 7.5 / 127 |

For ε > ε* the new prime costs more than all of λ_A(T_n) (n = 3, ε = 0.064: 5.2·10⁻³ against λ_A = 2.9·10⁻⁵, 180×; n = 4, ε = 0.064:
4.4·10⁻⁶ against 4.3·10⁻¹⁰, 10⁴×) and positivity is sustained by the reorganization of h* in the rest of the form: the full problem.
Moreover λ_A's decline on (T_n, T_n + ε) splits almost evenly between the prime's cost and the window's growth
(n = 3, ε = 0.016: −5.0·10⁻⁴ = −3.3·10⁻⁴ (D) − 1.6·10⁻⁴ (window); n = 4, ε = 0.008: −2.6·10⁻⁸ − 2.5·10⁻⁸).

**Prop. 4.3 (continuation lemma; PROVED in its qualitative form, inherits in the quantitative one).** (i) If λ_A(T_n) > 0, there exists ε₀ > 0
with λ_A > 0 on [T_n, T_n + ε₀) (lem:contA + Lemma 3.1): the entry of a prime power **never** changes the sign at the instant
of entry. (ii) Quantitatively, λ_A(T_n + ε) ≥ λ_A^{without n}(T_n + ε) − v_n·sup{‖F‖²_{edge,ε} : F near-minimizing}, and neither of
the two terms is σ-computable with its own margin: the first is a λ_A of another form and the second is a datum of h* (boundary
regularity, (REG) of R165_202, OPEN). The margin of (i) is λ_A(T_n): **it inherits**. (iii) With a number, ε* (where D = λ_A(T_n)) is 0.037,
0.020, 0.006 for n = 3, 4, 5: the perturbative regime covers 25%, 18%, 4% of the interval between births and shrinks with T.

**Decision on task 3: NO.** The question "is the local M0 condition on the newly born component enough because the coupling is
second order in the mass?" is ill-posed in σ: (a) the mass is not small at birth (Lemma 2.2); (b) at birth the new
component and its coupling with the old ones sum to **exactly zero** for every F (Lemma 3.1) — there is no "local condition with
its own margin" to check, there is an identity; (c) right afterward, the quantity that grows is not the component's mass but the
visibility c_F(log n) (Lemma 3.2), controlled by h*'s behavior in the boundary strips, not by σ's slope at ∂U; (d)
the ex nihilo component does not receive h* (Table 3.3), so the M0 condition on it is vacuous; what costs is the entire cosine
(its negative lobe falls on the old low-frequency components, deforming them). **It does not escape W-loc**: the only instant
at which the argument is exact (ε = 0) has no content, and as soon as ε > 0 the margin is λ_A(T_n).

**Growth threshold from σ (M0-slope; NUMERICAL).** Between births, σ_T is constant and only T grows (Shannon ∝ T). R186_043's
threshold (β_pred = 0.7·(mass/2)·T²/b₁ = 1, b₁ = mean |σ_T′| at ∂J) gives T_c(J) = 0.87 (polar), 1.55, 1.71, 1.76, 2.95, 4.19 on
(T_3, T_4); 1.01, 1.72, 1.51, 1.73, 2.51, 2.63 on (T_4, T_5); 1.31, 2.12, 2.13, 2.18, 2.23, 3.55, 2.20, 2.72, 2.89 on (T_5, T_7);
1.59–6.4 on (T_7, T_8): **no component crosses its local threshold before the next birth, in any window up to ½log8**.
Meanwhile λ_A falls 10⁻³ → 10⁻²¹. The σ-computable threshold describes isolated sub-Shannon modes (valid for τ ≥ 27, R186_043 §5(c)) and
not the balance; it is W-loc seen from the growth side. (The even polar mode already has a negative local margin with Tate, R186_043 §5(a):
the M0 law does not apply to it because N_J ≈ 0.4–0.5 and Tate kills it.)

**On the fold (R186_036 Lemma 2; NUMERICAL against CONDITIONAL).** D_n(ε) ∝ ε^{1.2–1.5} (n = 3, 4) and ≈ ε^{2.4} (n = 5) — not ε¹. A
fold of slope −2v_n h*(T_n)h*(−T_n) would require p = 1 with h*(±T_n) ≠ 0; measured h*(T_n) = −0.048 (n = 3; predicted fold
−5.8·10⁻³, indistinguishable from the finite-difference error ≈ d·λ_A″ ≈ 4·10⁻³), −8·10⁻⁴ (n = 4; predicted −10⁻⁶ against slopes of 10⁻⁵),
≈ 0 (n = 5). If c_{h*}(2T − 2ε) ∝ ε^{2a+1} with h* ∼ (T − |t|)^a at the boundary, p ≈ 1.3–1.5 gives a ≈ 0.15–0.25: the minimizer
**vanishes at the boundary** and the entry of a prime is smoother than a fold (fractional singularity of λ_A′). This contradicts the
premise h*(±T) ≠ 0 of (REG) in the form used by Lemma 2 and leaves it as CONDITIONAL with a numerically unfavorable hypothesis; consistent with
R165_202 §1.5 ("boundary behavior not established"). Resolution M = 40–48 at the boundary: indicative, not definitive.

## 5. Honesty, inheritance and falsifier

5.1 **Inheritance.** The PROVED statements (Lemmas 2.1, 2.3, 3.1, 3.2; Prop. 4.3(i)) are identities or sign-free bounds; the only statement
with a sign (Prop. 4.3(i)) has margin λ_A(T_n) and inherits. No quantity in this memo bounds λ_A from below with its own margin.
False dichotomy avoided: it is not claimed that the new component "captures no more than σ₊ gives" — at birth it captures nothing
by identity, and afterward it captures through c_F(log n), which is not local in σ.
5.2 **What remains for all T.** Between births: σ_T fixed, the window growing — the full problem (λ_A′ = −𝒱/T, R165_202 1.4),
with the cost of the newly entered prime growing as ε^{1.2–2.4} until it exceeds λ_A at ε* ≪ gap. At the births: nothing (Lemma 3.1).
So **all of the sign's dynamics lives between births**, and the component-wise reading of σ (ex nihilo / fission / deformation) only
describes where the negative mass is, not who pays for it: h* pays it through the positive lobes of the cosines already present
(R186_043 §5(d): the slope at ∂U of the low components is the comb's), which is the global cancellation of R186_040/044.
5.3 **Falsifier M₁ (NUMERICAL).** Births at log 2 (n = 4) for M₁(δ = 0.1) and M₁(δ = 0.01): ex nihilo (62.56, 63.76) mass 0.453 and
(108.46, 108.94) mass 0.032 — the same ones as ζ (0.394, 0.026) shifted < 0.1 — plus one of mass 0.005 at (35.2, 35.5) (bhat's lobe).
Sign: λ_A(M₁, δ = 0.1) = +5.8·10⁻⁴ (½log3), +2.4·10⁻⁴ (0.56), −9.8·10⁻⁵ (0.58, n₋ = 1), −4.4·10⁻⁴ (0.64, n₋ = 2), −1.47·10⁻³ (log 2):
crosses at T ≈ 0.573 ∈ (T_3, T_4), **between boundaries**, with the same contacts {2, 3} as ζ. Every "per-birth" criterion lets it
through; the perturbative criterion of Prop. 4.3 does not see it either (at T_3, λ_A(M₁) > 0 and the regime ε < ε* is identical). Beaten in the
requested sense: the falsifier fails exactly where the memo says the full problem returns.
5.4 **Labels.** Lemma 2.1 PROVED (trivial); Prop. 2.2 PROVED (classification) + NUMERICAL (table); Lemma 2.3 PROVED; Obs. 2.4 NUMERICAL
+ PROVED (absence of a law via Weyl, CITED R186_046 §4.2); Lemma 3.1 PROVED; Lemma 3.2 PROVED; Table 3.3 NUMERICAL (n = 7: unresolved);
Def./Table 4.2 NUMERICAL; Prop. 4.3 (i) PROVED-inherits, (ii) CONDITIONAL ((REG)), (iii) NUMERICAL; decision on task 3: **NO-GO for the
perturbative argument** (not because of a declared class but because the exact instant is empty and the rest inherits); the fold of R186_036
Lemma 2: CONDITIONAL with a numerically unfavorable hypothesis (p > 1). Row D: OPEN. No grid symbol changes.

## 6. Audit notes

- Lemma 3.1 is lem:contA's continuity read in the symbol; its new content is only the reading "the new negative lobe cancels
 exactly against the positive ones of the same cosine for every F", which is ∫cos(τ log n)|F̂|² = 2πc_F(log n) (Parseval) and c_F(2T) = 0.
- Lemma 2.3 uses only that J is connected and cos > 0 on J; it does not use Λ. The strict < ½ bound does not improve the "sub-Shannon sea" (N ≤ 0.95)
 for the inherited components, which are the ones that matter to h*.
- The "new = disjoint" criterion differs from R186_046 §6's heuristic (centers/endpoints within 30%): by the one used here, [4.24, 6.46] is
 deformed (from a fission product), not new. Both criteria are bookkeeping; §0.3's genealogy is verifiable in the table.
- Exponents p: finite differences in ε with M = 40 (n = 3, 4); h*'s boundary behavior is not resolved with degree-40 Legendre
 (resolution ≈ T/M² ≈ 4·10⁻⁴); p ∈ (1, 2) is robust over three consecutive steps, the value of a is not.
- λ_A^{without n}(T_n + ε) < 0 for ε ≳ 0.02 says nothing about ζ: it is a different form (without a prime), and its negativity comes from odd
 boundary F's (Lemma 3.2), consistent with the prime's term being +v_n/2 there.
- n = 7: every h* number at ½log7 is at the numerical floor (λ_A ≈ 3.6·10⁻¹⁴ with the next eigenvalues of the same order); they
 are reported as unresolved bookkeeping and enter no conclusion.
- No equivalence with other statements; "zeros" does not appear; M₁ only as a class falsifier (R186_043 §6, R186_114).

[ note: see 03-research/phase-195-modern-tools/VERIFY_CLAMPED_AND_EDGE_LAW.md — the fit h*~(T−|t|)^a, a≈0.15–0.25, is relabeled: NUMERICAL as a fit, the power-law reading ARGUED as a resolution artifact of (log 1/δ)^{−1/2}; P_T does not impose clamped endpoints on F (it does on G=(¼−∂²)^{−1}F).]
