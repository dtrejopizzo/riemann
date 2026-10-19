# Handoff — where we stand and how to proceed (row D, phase 149)

## Record status
* Rows A, B, C: WEIL-STRENGTH-COMPLETE (Papers 43–45, LaTeX). Row D: no label, no sign.
* Paper 46: Parts I–III closed (§§1–23 + §19bis; adversarial review R1/R2 ACCEPT). Part IV (phases 145–149) pending decision.
* Phases 145–148 closed negatively, by theorem. Record reading: the wall is ONE object — a `Spec Z` with
  closed points over each `F_q` — characterized from three sides: no ring of correspondences (146–148),
  no a priori poles of the tensor square (phase 36 docs 106/107 + R147/R148), no finite base field (`F₁`).
  The zero data enters the framework through a single channel: the regularized trace of the radial sector.
* Phase 149 OPEN: Deligne route instead of Weil. Blueprint:
  `03-research/phase-149-row-d-additive-pencil/R149_000_BLUEPRINT.md`. Construction started; if the round
  died before `R149_001_ROUND1.md` was received, check whether the file exists; if not, restart the
  construction from the blueprint as is.

## The idea of phase 149 (to resume without rereading everything)
Deligne does not use a surface nor a sign: (i) even tensor powers give traces ≥ 0; (ii) Landau's lemma;
(iii) a priori poles from the invariant theory of the monodromy of a FAMILY; (iv) fiber extraction ≤ family;
(v) Künneth. Over `Z`: family = additive sheaf `Σ Λ(n)e(nα)n^{−s}` (rational fibers `L(s,χ)`, `α=0` is `ζ`,
"field size" = length `N`). Pieces:
* D.59 Extraction theorem: Gaussian `2k` moments of centered prime sums `Σ(Λ−Λ_Q)e(na/q)w(n/N)`
  over Farey `q ≤ N^c`, for every `k`, constants `C_k(log N)^{B_k}` ⟹ `ψ(N)−N ≪ N^{½+c/k+ε}` ⟹ RH.
  Literature: not stated anywhere (folklore chain). Continuous version ⟺ RH of additive twists
  (stronger than RH). `Ξ_a`-uniform: by itself it carries no arithmetic.
* D.60 Death test: what the PROVED moments give (large sieve/BDH with their error terms; Hooley;
  Green–Tao). FATAL rule: a new zero-free region derived from known theorems = range error in
  `Q`. **W-H (binding):** Hooley's conjecture in literal uniform form is REFUTED in some regimes
  (Bober–Goldmakher, "Disproving Hooley's conjecture", JEMS; arXiv:2407.01045). Exact ranges must be fixed and
  it must be checked whether the D.59 hypothesis survives; if not, that is the main finding, and other families
  are tried (weighted characters; Montgomery–Soundararajan short intervals; restricted Farey).
* D.61 Coinvariant block: additive correspondences `T_h = {(p,q): q | p−h}`, pairing normalized by
  density `κ(h−h′) = Σ_{q|h−h′} 1/φ(q)`, positive definite (Bochner), blind to the zeros = singular series = the
  "known poles" of Deligne. Künneth of the additive square (CLASSICAL: Fujii; Languasco–Perelli):
  `Σ_{h≤X}R(h) = X²/2 − 2Σ_ρ X^{ρ+1}/(ρ(ρ+1)) + Σ_{ρ,ρ′}X^{ρ+ρ′+1}Γ(ρ)Γ(ρ′)/Γ(ρ+ρ′+2)+…`. Division to state:
  Rankin/Landau live in the multiplicative square (mean square of `ψ_χ`), invariant theory in the
  additive one.
* D.62 Problem (P149), the object to CREATE: a symmetry `G` of the additive sheaf whose invariant theory computes
  the moments of the family WITHOUT knowing any fiber, and that predicts the large deviations that W-H requires.
  Candidates to examine: affine group `Z ⋊ {±1}` on sections; `SL₂(Z)` on `R/Z ∪ Q`; `Ẑ^×` action
  (Bost–Connes); Katz–Sarnak law. The only unconditional thing today is the large sieve (`k=1`).
* Caveat: strong Hardy–Littlewood contains RH as a case of a tuple; the gain only exists if the
  moments of the family are computed by symmetry, not fiber by fiber.

## Phase circuit (same as 138–148)
1. `R149_001_ROUND1.md`: D.59 proved; D.60 with W-H verdict; D.61; (P149); D.63; labels.
2. `R149_002_AUDIT.md`: attack D.59 (ranges, `Λ_Q` error, Bernstein), D.60 (illegitimate zero-free
   region? does W-H kill the hypothesis?), D.61 (exact hypotheses of `κ`; exact citation of Fujii/L–P), (P149)
   (is it a question or a directive?). Labels STANDS/DOWNGRADE/WITHDRAW.
3. Repairs (`R149_003`), confirmation (`R149_004`), decision (`R149_005`).
4. Record in `PLAN.md` and in memory (`row-d-deligne-route.md`, `row-d-completion-plan.md`).

## Open decisions
* If D.60 shows that W-H refutes the D.59 hypothesis: continue with another family (phase 150) or close D in the
  map and write Part IV of Paper 46 (phases 134–149)?
* LaTeX conversion of Part III of Paper 46 (pending).

## Standing rules
Pure mathematics, numerical only if strictly necessary; construction + adversarial audit; check the corpus
before building; never relabel to gain labels; "no more of the same": what is worthwhile has to create the
object, not go around it.

## Update: `R149_001_ROUND1.md` ARRIVED (before the cutoff)
* **D.59 PROVED with three corrections**: the Selberg majorant has PNT-strength error (circular); the
  constant-`1` model makes the hypothesis false for `k ≥ 2`; the admissible model is Vaughan's truncated
  singular series `M_Q(n) = Σ_{q≤Q}(μ(q)/φ(q))c_q(n)`. "⟹ RH" needs a family `w_θ = w·u^θ`. `Ξ_a`-uniform.
* **D.60**: `H(1,c)` = Montgomery–Vaughan large sieve, proved exactly on `c ∈ [½,1)`, a range where
  extraction gives nothing; for `c < ½` the hypothesis is OPEN (follows from GRH). For `k ≥ 2` nothing
  unconditional exists (de la Bretèche–Fiorilli 2023). No zero-free region: FATAL not triggered.
  **W-H: the hypothesis SURVIVES.** The counterexamples (Fiorilli–Martin JEMS 2023, not Bober–Goldmakher; Hayani
  2407.01045) live at `q ≍ log log x`, contribute `o(Q²N)`, and come from Littlewood's fluctuation, compatible
  with RH.
* **D.61 PROVED**: `κ(d) = Σ_{q|d} μ²(q)/φ(q) = d/φ(d)`, `κ(0) = log Q + C₀`; BDH main term
  `= xQκ(0)`; positive (Bochner, RESTATEMENT), blind to the zeros. **Fifth wall**: Rankin/Landau live in the
  multiplicative square, invariant theory in the additive one, and no known transport exists; over `F_q` they are
  the same square because `H_c(X×X) = H_c(X)^{⊗2}` carries both.
* **(P149) stated with precision** (see R149_001 §D.62): structure `𝒢` over the additive sheaf that computes
  `M_{2k}` for `k ≥ 2` without using zeros of any fiber and compatible with Fiorilli–Martin/Hayani. Partial
  mechanism: Ramanujan orthogonality gives `M_{2k} = Σ_d κ_Q(d)𝒞_{2k}(d)` exactly; `H(2,c)` implies average
  Goldbach with square-root error (Bhowmik–Ruzsa) ⟹ it is at the level of RH or above.
* Open: O-149.1 (main) `H(k,c)` for some `k ≥ 2`; O-149.2 centered large sieve with `c < ½`;
  O-149.3 centered restriction estimate; O-149.4 = (P149); O-149.5 transport between the two squares,
  to merge with O-148.2. CERTIFIED (not CLASSICAL): Hooley constant `c₀` and error `O(Q^{5/4}x^{3/4})`
  taken from a survey; verify in Crelle 274/275 before citing in a paper.
* **NEXT STEP ON RESUMING**: launch adversarial auditor → `R149_002_AUDIT.md` (attack: D.59 with the Vaughan
  model and the family `w_θ`; ranges of `c`; the reading of Fiorilli–Martin/Hayani; `κ(d) = d/φ(d)`; whether
  (P149) is a question and not a directive; the "fifth wall"). Then repairs, confirmation, `R149_005`.

## Update — audit done, new plan
* `R149_002_AUDIT.md` written. Verdicts and minimal repairs in its §0 and §5.
* D closure plan: `ROW-D-CLOSURE-PLAN.md` (read first on resuming). Side candidate #1:
  Laumon route (Fourier transform as transport between the additive and multiplicative squares; Gauss sums
  as phase data). Mandatory new falsifier: Beurling prime system (T3).
* **NEXT STEP**: `R149_003` (repairs i–vi) → `R149_005` → open phase 150 with `R150_000` (CORPUS_CHECK
  + reading of Laumon 1987 / Kedlaya 2006 + T3).

## Update (afternoon) — phase 150 closed
* Full circuit (`R150_000`–`R150_005`). Result: T5 proved (trivial), T4 → polar/entire classification
  (classical), T3 conditional (read DMV 2006: O-150.1). Does not move the sign; sharpens the wall.
* **Decision pending**: close D in the map + Part IV of Paper 46, or open MW-5 with a concrete idea.
* Minor pending items: `R149_003`–`R149_005`; Paper 46 §18 with T5 and the classification; commit/push.

## Closure — row D closed in the map
* Phases 149 (`R149_003`, `R149_005`) and 150 closed. Paper 46 Part IV §§24–28 + `PART_IV_NOTES.md` +
  `PART_IV_ADVERSARIAL_REVIEW_R1/R2.md` (ACCEPT). Wall fixed in §28.2; reopening in §28.4.
* Remaining: LaTeX of Parts III–IV of Paper 46; O-150.1; commit and push (not done).
