# Round 24, memo A — Leading term of the truncation defect: ROUND_019_A §§2–4 versus ROUND_021_A §3

Control note. It is not a sign attempt. Notation of P47 and of round 7: `a_T(F) = Arch(F) − Σ v_n c_F(log n)`,
`v_n = 2Λ(n)/√n`, `P_T = {∫F e^{±t/2} = 0}`, `W_*` the global form, `M = (−∂² + ¼)K_Pó`, `K_Pó = S_ζ g_0`,
`g_0(t) = (2π²e^{9t/2} − 3πe^{5t/2})e^{−πe^{2t}}`, `W_*(M∗φ, ·) ≡ 0` (CITED: R160_M4_R1 Lemma 2(a); P46 Thm 11.11).

**Files opened:** ROUND_019_A.md, ROUND_021_A.md (in full); ROUTES-MASTER-INDEX.md by grep (entries P211-17A,
l.6457 and l.9833; record of ROUND_021_A, l.31200–31204); P2_SCHUR_001.md by grep (Lemmas P2-S.2, P2-S.3).
**Not opened:** R160_M4_R1.md, 106_09, ROUND_017_A of 211, P47 main.tex, BRIEF_CONSTRUCTOR.md, RULES_AVOID.md
(the task is a computation, not a construction). No computation run.

## §0 Cross-check
The question (who dominates and why the two memos differ) is not answered in the corpus: the index records the
claim of ROUND_021_A (l.31204) and that of ROUND_019_A, without reconciliation. The coupling part is P211-17A (see §4).

## §1 Correction of the premise: both cutoffs are smooth
ROUND_019_A l.52: «`χ_T` smooth cutoff, `= 1` on `[−T+θ, T−θ]`, `θ = e^{−2T}`». It is not an abrupt cutoff. The vector
of ROUND_019_A is the special case of ROUND_021_A with `φ = δ_0` (`δ = T`), transition of width `η = θ = e^{−2T}`
and a single even correction `u_ev` (instead of `u_±`). The relevant difference is NOT the type of cutoff but (i) the distance
`D := δ − η` between the support of `φ` and the start of the transition and (ii) that ROUND_019_A compared exponents and ROUND_021_A
constants.

## §2 Rederivation of the leading term (general, `R = (1−χ)(M∗φ)`, `D = δ − η`)
**(a) Profile.** For `t → +∞`, `M(t) = −16π⁴e^{17t/2}e^{−πe^{2t}}(1 + O(e^{−2t}))` (term `n = 1` of `S_ζ`, two
derivatives of the double-exponential Gaussian). `M∗φ` at `t ≥ T − η` is `≍ ‖φ‖_{L¹}·e^{cT}e^{−πe^{2(t−(T−δ))}}`, with
local decay rate `A := 2πe^{2D}`. `R` is the product of that decay by `1−χ`, which grows from `0` at `T−η`.
The mass of `R` is in a layer of width `w`:
- if `1−χ` vanishes to finite order `r` at `T−η`: `w ≍ 1/A ≍ e^{−2D}`;
- if `χ ∈ C_c^∞` (flat vanishing, profile of type `e^{−η/x}`): `w ≍ (η/A)^{1/2}` at scale `η` and, for fixed `η`,
  `w ≍ A^{−3/4}`. (ARGUED, Laplace.)
In ROUND_019_A (`η = θ = 1/N`, `N = e^{2T}`, `A = 2πN`) both cases give `w ≍ 1/N`. In ROUND_021_A with fixed `η` and
smooth `χ`, the «finite order» of l.103 is not compatible with `χ ∈ C_c^∞`; it gives `w ≍ e^{−3D/2}`, not `e^{−2D}`.

**(b) Archimedean diagonal, sign +.** `Arch_*(R) = (1/2π)∫m(τ)|R̂(τ)|²dτ`, `m(τ) = log|τ| + O(1)` for `|τ| ≥ 1`.
`|R̂|²` is spread up to `|τ| ≍ 1/w`; the part `|τ| ≤ C` weighs `≤ C‖R‖²_{L¹} ≤ Cw‖R‖²`. Thus
`Arch_*(R) = (log(1/w) + O(1))‖R‖² = (κD + O(1))‖R‖²`, `κ = 2` (finite order) or `κ = 3/2` (flat, fixed `η`); `κD = 2T + O(1)`
in ROUND_019_A. **Positive.** (ARGUED.)

**(c) Primes, sign −.** Self-shifts: `c_R(log n)` with both factors in the same layer requires `log n ≤ w`:
impossible. Crossings `+`/`−` (or `R` with the tail of `M` beyond `T` in ROUND_019_A): `log n ∈ 2(T−η) ± O(w)`, i.e.
`≍ e^{2(T−η)}w` integers, each with `v_n ≤ 4Te^{−(T−η)}` and `|c_R(log n)| ≤ C‖R‖²` (Cauchy–Schwarz), and the sum over the window is
controlled by `∫|c_R(u)|e^{u}du ≤ Ce^{2T}‖R‖²_{L¹} ≤ Ce^{2T}w‖R‖²`. Uniform bound (without cancellation or prime distribution):

    |Σ_n v_n c_R(log n)| ≤ C·T·e^{−T}·max(1, e^{2T}w)·‖R‖².                                               (2.1)

For `e^{2T}w ≥ 1` (many integers) the factor is `C·T·e^{3T}w²`; for `e^{2T}w < 1` (at most `O(1)` integers), `C·T·e^{T}w`.
Sign: if `φ` is even and of one sign, `R ≤ 0` in both layers (`M < 0` for large `t`), `c_R(log n) > 0` and the term enters
with **−** (coincides with ROUND_019_A l.96–101). (ARGUED.)

**(d) Moment correction.** `|A(R)|, |B(R)| ≤ e^{T/2}‖R‖_{L¹} ≤ e^{T/2}w^{1/2}‖R‖`. `W_*(u, R)` (contacts `log n ≈ T`,
prime density `≈ e^{T}`, weight `2Te^{−T/2}`) is `O(Te^{T/2}‖R‖_{L¹})`. Total contribution `O(Te^{T}w)‖R‖²`, without fixed sign. (ARGUED.)

**(e) Primes/archimedean ratio.** `𝔡_T = (κD + O(1))‖R‖²·(1 + O(ρ))`, `ρ := [Te^{−T}max(1, e^{2T}w) + Te^{T}w]/(κD)`.
- ROUND_019_A (`D ≈ T`, `w ≍ e^{−2T}`): `ρ ≍ e^{−T}`. **The archimedean part dominates by `≍ e^{T}`.** Primes `n ∈ [N−2, N+2]`
  and correction `u_ev`: both `O(Te^{−T})‖R‖²`.
- ROUND_021_A with `δ = T − ½`, finite order: `ρ ≍ e^{−T}`; with flat `χ` and fixed `η`: `ρ ≍ e^{−T/2}` (this is where the
  `e^{T/2}` of l.112 comes from, by a different route from the one written there).
- General family: the bound (2.1) guarantees dominance only if `w ≪ e^{−T}`, i.e. `D ≥ T/2 + O(1)` (finite order)
  or `D ≥ 2T/3 + O(1)` (flat). For wide `φ` (smaller `D`) the uniform bound no longer suffices; the mean part of
  the prime sum is `≈ 2∫c_R(u)cosh(u/2)du`, which is moment × moment and is absorbed in (d); the rest depends on the
  distribution of primes in short intervals of length `≍ e^{2T}w`. **OPEN** outside that range.

## §3 Verdict on the discrepancy
1. **Exponent** (ROUND_019_A §2): correct. The three sources carry `e^{−2πN'}`, `N' = e^{2(T−θ)} = N − 2 + O(1/N)`:
   `‖E‖² ∝ e^{−2πN'}/N`, the crossings at `n = N' + k` carry `e^{−2π(N'+k)}` (minimum of `e^{2t} + n²e^{−2t}` at `2n`).
   PROVED as a reading (standard Laplace), ARGUED in constants.
2. **Constant** (ROUND_021_A §3): correct in the result. «They share order» of ROUND_019_A §2–§4(1) is true only
   modulo `e^{cT}`; within that factor, the prime costs `v_n ≍ 4Te^{−T}` and the diagonal `log(1/w) ≍ 2T`: the archimedean part
   dominates by `≍ e^{T}`. ROUND_019_A did not write the `e^{−T}` of `v_n` (it absorbed it into `e^{cT}`). Its conclusion (ii) («the
   lattice tail is negative and is compensated by the high-frequency archimedean energy») is compatible and is reinforced.
3. **Only the cutoff?** No. Both cutoffs are smooth. They differ in (i) level of reading (exponent vs constant), (ii) `D`:
   `D = T` in ROUND_019_A, free `D` in ROUND_021_A; (iii) the profile of `1−χ` changes `κ ∈ {3/2, 2}` and the margin
   (`e^{T}` vs `e^{T/2}`), not the sign. ROUND_021_A has two inaccuracies: «finite order» with smooth `χ` and the claim
   for general `φ`, which holds only for `D ≥ T/2 + O(1)` (§2(e)).
4. Signs: diagonal +, primes −, correction without sign; leading term `𝔡_T ≈ κD‖R‖² > 0`, blind to `Λ`. ARGUED.

## §4 Coupling with the complement
For `G ∈ P_T`, `F = M∗φ`: `χF + G = F + (G − R)`, and `W_*(F, ·) ≡ 0` gives `a_T(χF + G) = W_*(G − R)` (PROVED, one line).
On `span{G, χF}`, with `s ∈ ℝ`:

    a_T(G + sχF) = W_*(G) − 2s W_*(G, R) + s² W_*(R),

and since `W_*(R) > 0` (§2, ARGUED in the dominance range), `min_s = W_*(G) − W_*(G,R)²/W_*(R)`. This is the secular /
Schur form of P211-17A (PROVED there: `(★) ⟺ C ⪰ 0` and `ρ ≥ sup b²/a_T`) with scalar block `W_*(R)` and vector `b = W_*(G,R)`;
at `T = ∞` (`R = 0`) it is `𝒲_AB ≡ 0` of P2_SCHUR_001 (Lemma P2-S.2: Schur = the form on the quotient).

What the computation of §2 adds (ARGUED): `|W_*(G, R)| ≤ ` energy of `G` in the layer `|t| ∈ [T−η, T]` at frequencies `≍ 1/w`
(local archimedean) + prime contacts `log n ≈ 2T` and `≈ T` with weights `e^{−T}`, `e^{−T/2}`. Thus the Schur correction
`W_*(G,R)²/W_*(R)` is bounded by `(κD)^{−1}`·(high-frequency energy of `G` in the layer)² plus terms
`O(e^{−T/2})`. Reading: the near-radical family can lower `a_T` below `W_*(G)` only through the content of
`G` in the boundary layer at frequency `≍ e^{2D}`.

**New sign statement?** No. (i) `W_*(R) > 0` is positivity of the diagonal of the block, already recorded as «does not
fix `λ_A`» (ROUND_021_A §3; index l.31204). (ii) The inequality `W_*(G)W_*(R) ≥ W_*(G,R)²` is exactly the
positivity of `W_*` on `span{G, R}`, i.e. the original problem on a plane; rewriting it as Schur is P211-17A.
(iii) The bound of the coupling vector by the boundary layer is a localization of `b`, not a sign; P211-17A already showed
(NUMERICAL) that the Schur share is not attributable to arch/comb/Tate separately, and this localization neither contradicts
nor resolves it. NO-GO as a source of sign (ARGUED); no new operation.

## Labels
- Premise «abrupt cutoff» of the question: incorrect (ROUND_019_A l.52). CITED.
- Common exponent `e^{−2πe^{2T}}` (019 §2): PROVED as a reading; constants ARGUED.
- Archimedean dominance by `≍ e^{T}` at `X_T` and by `≍ e^{T}`/`e^{T/2}` (finite order/flat) with `δ = T − ½`: ARGUED.
- ROUND_021_A §3 for general `φ`: ARGUED only if `D ≥ T/2 + O(1)` (`2T/3` with flat `χ`); OPEN otherwise.
- Identity `a_T(χF + G) = W_*(G − R)` and 2×2 form: PROVED (elementary); equivalent to P211-17A / P2_SCHUR_001: CITED.
- New sign statement: none.
