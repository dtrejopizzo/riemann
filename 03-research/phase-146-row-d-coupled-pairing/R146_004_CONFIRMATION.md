# R146.004 — Confirmation, phase 146 (final round)

repairs in `R146_001_ROUND1.md`, the rewritten `README.md`, and `scripts/tower_gram.py`.
Checked against: Paper 44 §8bis (Thm 8bis.1 + §12 K1, Thm 8bis.1b, Cor 8bis.1b′, Rem 8bis.1c,
Cor 8bis.1d, Thm 8bis.1e, Thm 8bis.2, (8bis.0)), `R145_001` §§D.41–D.42, Paper 46 §§11/14,
and — read in full, and the decisive document of this round — `03-research/phase-147-row-d-single-prime-tower/CORPUS_CHECK_R147.md`.
Method unchanged: every claim assumed false; every number recomputed independently of the scripts.*

**FATAL screen: PASSES, but not comfortably.** Nothing in round 2 claims positivity. However **C-A below
shows that the round's one new headline is a *universal negative* whose universal quantifier is false, and
that the corner where it fails is the positive corner** — under the round's own cited constant
`c_φ = γ+log4π`, the tower form is PSD at the coarsest admissible `(ε,N)`. The claim as written is safe; the
claim as reasoned is one sign-convention away from an unscreened positivity assertion, and it must be
re-quantified before anything is built on it.

**Repairs: all 20 verified at their sites.** 24 `[R2: …]` notes in `R146_001`; M1–M13 and m2, m5 are marked
in place, M14 and m1, m3, m4, m6 are disposed in `R146_003` §0. **No dilution found**: each note states the
false sentence verbatim, says why it is false, and gives the replacement. Round 1 is now a correctly
annotated record. Residue: three stale sentences survive *below* their correction brackets (O-46.2's "a
volume `≤ 1` … the failure is only reinforced"; D.45.1's "extends … exactly"; D.44.7's `d_n` as "deg") —
acceptable as record-keeping, flagged here.

**Scripts: clean; every printed number reproduced.** `tower_gram.py` §§[1]–[7] and `cosh_test_cmn.py`
re-run. Independent hand checks: `τ_+(p) = 2/(√p+1) = 0.828427, 0.732051, 0.548584` at `p = 2,3,7`;
`τ_-(2) = −4.828427`; `λ_min(T_K(2^{−1/2})) = 0.197377, 0.177871, 0.173153` at `K = 4,8,16`, decreasing to
`(1−ρ)/(1+ρ) = 0.171573`; the `Ξ_a` row at `p=2, a=0.05`: `ρ_± = 0.732043, 0.683013`,
`τ_+ = 0.422647+0.405829 = 0.828476` ✓. The model tower re-derived from scratch via
`S_k = −S_{k−1}−2S_{k−2}` (`S_1..S_8 = −1,−3,5,1,−11,9,13,−31`), giving
`N_k = 4,8,4,16,44,56,116,288` and `κ(k) = 2.8284, 4, 1.4142, 4, 7.7782, 7, 10.2530, 18` — **all eight
values exact**. One script encoding error (C-E) and one README numerical error (C-F) found.

---

## Part 1 — Status of the fourteen MAJORs and six minors

| # | round-2 disposition | audit status |
|---|---|---|
| **M1** | withdrawn; (146.6) → `HEURISTIC`; replaced by §D.47.1 | **DISCHARGED.** The in-place note quotes the false sentence and gives 8bis.1b verbatim. Correct. |
| **M2** | accepted; `B_δ(e_m−e_n) = L(m,n)−(δ_m+δ_n)/2` confirmed; O-46.3 re-posed and answered | **DISCHARGED**, and the constructive half was executed (§D.47.1). |
| **M3** | withdrawn; `End(L_S) ⊇ ∏Z_p` contains rank-2 orders | **DISCHARGED.** D.44.6′(iii) states it correctly. |
| **M4** | accepted; the count is the `S`-part `Σ_{p∈S_f}v_p(k)\log p` | **DISCHARGED.** D.44.6′(ii) is now true as written. |
| **M5** | withdrawn; obstruction relocated to the Gram | **DISCHARGED.** The relocation (D.44.6′(iv)) is honest and is itself now carried by D.47.9 + D.47.5(ii), which is where it belongs. |
| **M6** | label → `DEFINITION`; `ℓ=2` inconsistency printed | **DISCHARGED.** Re-verified: `a_2 = 2.306853`, order predicts `N_2 = 3.678430`, dictionary gives `0.693147`. Also at `ℓ=3,5,7` (script §[5]). |
| **M7** | label → `HEURISTIC`; novelty sentence deleted | **DISCHARGED.** `d_n = \log n` ⟹ `a_ℓ = 1` at every prime and the test passes (§[6], re-verified by hand). |
| **M8** | `c_N → 0`/`→ ∞`; O-46.2 promoted to MAJOR | **DISCHARGED**, and put to use: Lemma D.47.4's observation that on the tower `c_N` is one common positive factor is the correct and non-trivial escape. |
| **M9** | blueprint item (i) recorded NOT DISCHARGED | **DISCHARGED as a correction.** |
| **M10** | adopted as the round's governing identity; `Ξ_a`-uniformity extended to all of §§D.44–D.45 | **DISCHARGED**, and it is the best thing in round 2's framing. |
| **M11** | label → `CLAIM` | **DISCHARGED.** |
| **M12** | re-labelled `OPEN, suspected RH-equivalent`; prohibition kept | **DISCHARGED.** |
| **M13** | one-line proof inserted; robustness under both normalizations | **DISCHARGED.** Re-verified: `Q_0 = Φ(0)Φ(1) = (1)(−10) = −10`; under `d_n = \log n`, `(1)(5\log6−4\log10) = −0.251482`. |
| **M14** | made load-bearing (§D.47.6, §D.49) | **DISCHARGED, and it became the round's structural finding.** |
| **m1–m6** | all accepted | **DISCHARGED**, except m1, whose in-place text still reads `d_n = "\deg Frob_n"` (disposed only in §0). Cosmetic. |

**No finding was evaded, minimised, or answered by re-assertion.** This is a clean repair round.

---

## Part 2 — The single-prime tower, audited in full

### (1) `δ_m − δ_n` — **CONFIRMED**, with one gap in the proof

The transcription of (147.1) is faithful to Thm 8bis.1b(iii)–(iv) and to `CORPUS_CHECK_R147` §1.
Re-derived independently:

* **Archimedean cancellation: exact, and for the right reason.** `Δ^{(n),[φ_ε,N]}` has archimedean profile
  `φ_ε` and *every finite coordinate `1`*; `j_∞(x)` carries `1` at all finite places, so each indicator
  `1_{1+r^NZ_r}` is evaluated at `1` and returns `1` **irrespective of `n`**. Hence `W_∞` is a function of
  `φ_ε` alone. `c_φ = γ+\log4π` is **correctly cited** (it is the `(8.5∞)` counterterm; `CORPUS_CHECK_R147`
  §3 confirms the value and warns it is *profile-dependent*, which is stated). ✓
* **Support on `P(m) △ P(n)`:** with `A = S_f∖P(m)`, `B = S_f∖P(n)`, `−Σ_A+Σ_B = Σ_{B∖A}−Σ_{A∖B}` and
  `B∖A = P(m)∖P(n)`, `A∖B = P(n)∖P(m)`. ✓ (147.2) is correct.
* **`V_N(n)` depends on `n` through `P(n)` only** — immediate from (8bis.0)'s index set `S_f∖P(n)`; and
  `Cor 8bis.1b′` gives `F⋆F^† = V_N(n)·Δ^{(n),[h⋆h^†,N]}` (confirmed at `CORPUS_CHECK_R147` §1), so the
  The assignment (bare `= V_N·𝔡`, `♭` `= V_N^{−1}𝔡`) is right and, either way, `P(m)=P(n) ⟹
  V_N(m)=V_N(n)`. **(147.3) CONFIRMED: `δ_m = δ_n` exactly, at every `(ε,N)`, in both conventions.**
* **`C-D (MINOR, gap).** D.47.2(ii)'s "⟹" direction is asserted from positivity of the bracket alone, which
  does not exclude an accidental cancellation between the two sums. It is nonetheless **true**, and the
  missing half-line is: the coefficients `c_r(N) = \frac{r−2}{r−1}+N−1` are **rational**, so a vanishing
  difference would be a rational linear relation `Σ_{r} q_r\log r = 0` over distinct primes with not all
  `q_r = 0`; clearing denominators gives `∏ r^{a_r} = 1` with `a_r ∈ Z` not all zero, contradicting unique
  factorization. Insert this and (ii) is `PROVED`.

Novelty check: `CORPUS_CHECK_R147` §1c independently confirms **"`δ_m−δ_n`: not computed anywhere found"**.
`NEW` is correctly claimed.

### (2) The tower Gram — **CONFIRMED as an identity, with an unstated domain of validity (MAJOR)**

* Off-diagonal: (8bis.2) gives `(\log q)q^{−k/2}` at ratio `p^{|j−k|}`, times `c_N(p^j,p^k)`; by K1 the
  index set is `S_f∖(P(p^j)∩P(p^k)) = S_f∖\{p\}`, **the same set for every pair and equal to `V_N(p^k)`**.
  So `c_p = V_N` and `τ_p = δ_p/(c_p\log p) = 𝔡_{ε,N}(p)/\log p` — **a ratio in which the chart constant
  cancels identically.** Lemma D.47.4 is correct and is the round's cleanest technical point: the whole of
  M8's convention problem collapses to one number. ✓
* Un-normalized count check: `(p^jp^k)^{1/2}·(\log p)p^{−|j−k|/2} = p^{\min(j,k)}\log p` ✓ — the `q^{\min}`
  prefactor is reproduced without adjustment, exactly as claimed. (The `N_k ↔ \log p` substitution remains
  the M6 inconsistency, which D.47.9 now owns.) ✓
* **C-B (MAJOR): the domain of validity of (147.4) is never stated.** Theorem 8bis.1's off-diagonal carries
  an **archimedean part** (8bis.2a) multiplied by `∏_{s∈S_f∖F}\mathbf 1[s^N \mid (n−m)]`, which vanishes only
  for *sufficiently large* `N` and only when `S_f ⊋ F = \{p\}`. At `S_f = \{p\}` the product is empty and the
  archimedean block is **present and nonzero**; at `S_f = \{2,p\}`, `p` odd, `N = 1`, the indicator
  `\mathbf 1[2 \mid p^j−p^k]` is **`1`**. In both corners (147.4) is missing a term. Cor 8bis.1d's "no
  archimedean block" is likewise conditional on `S_f ⊋ P(n)`. The tower Gram is therefore an identity **only
  for `N` large enough that the indicator vanishes on every pair in play, with `S_f ⊋ \{p\}`** — which must
  be said, and which is exactly the regime that rescues (3).

### (3) The Toeplitz trichotomy — **thresholds CONFIRMED exactly; the verdict's quantifier is FALSE (MAJOR)**

* **The spectral bound is exactly right and is the KMS/geometric kernel's.** `f_ρ(θ) = Σ_kρ^{|k|}e^{ikθ}
  = (1−ρ²)/(1−2ρ\cosθ+ρ²)`, `\min f_ρ = f_ρ(π) = (1−ρ)/(1+ρ)`, `\max f_ρ = f_ρ(0) = (1+ρ)/(1−ρ)`. PSD ⟺
  `τ−1+\min f_ρ ≥ 0` ⟺ `τ ≥ 2ρ/(1+ρ) = 2/(\sqrt p+1)` ✓; NSD ⟺ `τ ≤ −2ρ/(1−ρ) = −2/(\sqrt p−1)` ✓.
  Numbers `0.828427 / 0.732051 / 0.548584` and `−4.828427` re-derived by hand. **CONFIRMED.**
  (Pedantic: the tower is indexed `k ≥ 1`, so the operator is **semi-infinite** Toeplitz, not bi-infinite;
  the answer is unchanged, since `T(f) ⪰ 0 ⟺ f ≥ 0` and `\inf\mathrm{spec}\,T(f) = \mathrm{ess\,inf}f`.
  The word "bi-infinite" should read "semi-infinite (same threshold)".)
* `λ_{\min}(T_K) < \mathrm{tr}/K = 1` for `K ≥ 2` ✓, so `τ_p < 0` is never PSD, already at `K = 2`
  (`λ_{\min}(T_2) = 1−ρ`, threshold `ρ = 0.7071` at `p=2`). ✓
* **C-A (MAJOR — the most important finding of this round). Corollary D.47.7's "at any chart, at any level,
  at any smearing, in either convention" is FALSE, and it fails on the positive side.** Paper 44 states that
  **the divergences** are negative (`ε→0`, `N→∞`); it does **not** state that the value is negative at every
  `(ε,N)`, and Prop. D.47.5(ii) misreads it as such. Taking the round's own cited constant:
  `𝔡_{ε,N}(p) = −Σ_{r∈S_f∖\{p\}}(\log r)[\tfrac{r−2}{r−1}+N−1] − \log\tfrac1ε + (γ+\log4π)`, with
  `γ+\log4π = 3.10824` and `ε < ½\log2` forcing only `\log(1/ε) > 1.05966`. At `S_f = \{2,p\}` (`p` odd),
  `N = 1`, the finite sum is **exactly zero** (`\frac{2−2}{2−1} = 0`, `N−1 = 0`), so at `ε = 0.34`:
  `𝔡 = −1.0788+3.1082 = +2.029 > 0`, giving `τ_3 = 2.029/1.0986 = 1.847 > τ_+(3) = 0.732` — **PSD**. The
  saving grace is C-B: that corner is precisely where (147.4) is not the Gram (the archimedean indicator
  `\mathbf 1[2 \mid 3^j−3^k] = 1`). **So the result is true in the regime where the object is defined, and
  the universal quantifier is both unproved and false outside it.**
  **Required restatement:** *for every `(ε,N)` in the regime where (147.4) holds — `S_f ⊋ \{p\}` and `N`
  large enough to kill (8bis.2a) — and a fortiori as `ε→0`, one has `τ_p < 0 < τ_+(p)`, so `G^{(p)}` is not
  PSD.* This keeps the finding and removes the false corner. It is not FATAL only because the claim as
  written is the negative one; had the inequality been written the other way, C-A would be a positivity
  assertion arrived at by misquoting a source. **Flag at maximum severity short of FATAL.**
* **C-G (residue, unreported and more interesting than the headline).** In the same valid regime
  `𝔡 → −∞` linearly in `N`, so `τ_p` crosses not only `0` but `τ_-(p) = −2/(\sqrt p−1)`: the tower Gram
  becomes **negative semidefinite**, i.e. *definite*. Worked example (`S_f = \{2,3\}`, `p = 3`,
  `ε = 0.34`): NSD requires `𝔡 ≤ −3.0016`, i.e. `0.6931(N−1) ≥ 5.05`, i.e. **`N ≥ 9`**. The round reports the
  trichotomy but never says which chamber the computed object lands in. It should — **with a W-a screen
  attached**, because "the Frobenius tower form is definite" is one sign convention away from a positivity
  statement and must not be written without one.
* **C-H (deflation).** Under the round's own dictionary the result is the tower image of a known model
  statement: `τ_p < 0` corresponds to `N_0 = 2−2g < 0`, and `R145_001` D.41.18(iii) already records
  `𝓔_C ⊆ B4_C ⟺ N_0 ≥ 0 ⟺ g ≤ 1`. D.47.7 is the arithmetic instance of "the genus is `≥ 2`", which is the
  corpus's oldest row-D fact. The honest novelty is the **explicit threshold** `2/(\sqrt p+1)`, not the sign.

### (4) The `Ξ_a` tower — **formula CONFIRMED (including the coordinator's worry); conclusion OVERSTATED (MAJOR)**

* `ĝ_a(k) = ½(ρ_+^k+ρ_-^k)`, `ρ_± = p^{−(½∓a)}`, with `ĝ_a(0) = 1` ✓ (the `½` is what keeps the diagonal
  normalisation comparable). Symbol `= ½[f_{ρ_+}+f_{ρ_-}]`.
* **The coordinator's worry is resolved favourably, for a reason not given elsewhere.**
  In general `\min(f+g) ≥ \min f+\min g`, so the threshold need not be the sum of the two minima. Here it
  **is**, because both Poisson kernels attain their minimum at the *same* point `θ = π`. Hence
  `τ_+(a) = 1−½[\tfrac{1−ρ_+}{1+ρ_+}+\tfrac{1−ρ_-}{1+ρ_-}] = \tfrac{ρ_+}{1+ρ_+}+\tfrac{ρ_-}{1+ρ_-}` ✓.
  **Verified; the one-line reason (common minimiser) must be inserted.**
* Values re-derived by hand at `p=2`: `a=0 → 0.828427`; `a=0.05 → 0.828476`; `a=0.49 → 0.833135` (script
  `0.833143`, difference is rounding in my hand value) ✓; `p=7, a=0.49 → 0.622279` ✓. Monotone increasing
  in `a`, `↓ τ_+(0)` as `a→0` ✓.
* **C-C (MAJOR): "A3 does not enter here either" is not established, and it collides with a corpus
  theorem.** (a) The comparison is between a **computed `ξ`-diagonal** and a **`Ξ_a` threshold**; no `Ξ_a`
  diagonal is computed anywhere (Paper 44 §8bis is an adelic computation for `ξ`). Non-separation of the
  *thresholds* is not non-separation of the *forms*. (b) Worse, `CORPUS_CHECK_R147` §2 records
  **Doc 131 Theorem 6.7** (`phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md:791`): for the
  single-Euler-factor object `F_{p,α}` with weights `Λ(p^k)(p^{ka}+p^{−ka})` — *the same weights* —
  positivity holds **iff** `|α| = \sqrt p`, i.e. **iff `a = ½`**, proved by an explicit two-bump Mertens
  test. That is a corpus theorem saying the single-prime tower's sign **is decided by `a`**, i.e. is
  maximally `Ξ_a`-sensitive. The reconciliation exists (Doc 135 §7.2 finding B3: `ζ`'s Euler weight is
  `a = 0`, "maximally impure", the *destructive* regime, the mirror twin of Doc 131's constructive one) —
  but it must be made, and until it is, D.47.8's headline stands in apparent contradiction to
  `TRIED–PROVED` prior art that the round does not cite.
* **C-E (MINOR, script).** `thresholds()` short-circuits `ρ_+ ≥ 1 → (+∞,−∞)`, so `a = ½` is reported as
  "never PSD / unbounded". The symbol's **supremum** is unbounded (pole at `θ=0`), but its **infimum** is
  finite: `P(1,π) = −1`, giving `τ_+(½) = ½+\frac{1}{p+1}` (`= 0.8333` at `p=2`), the continuous limit of the
  `a=0.49` value `0.833143`. D.47.8(iii)'s "the form becomes unbounded" is true of the norm and false of the
  threshold; it is labelled `HEURISTIC`, so this is a correction, not a withdrawal.

### (5) The model comparison and the "two slots" verdict — **CONFIRMED, with one refinement**

* All sixteen numbers re-derived independently (above). `κ(k) ≥ q^{k/2}+q^{−k/2}−2 → ∞` by Weil's bound, so
  "grows like `q^{k/2}`" is correct as a lower bound; note `κ` is **not monotone** (`κ(3) = 1.414 < κ(1)`),
  which the text's "`∼ q^{k/2}`" glosses. MINOR.
* D.47.9(i) is right: a bounded positive symbol and a divergent one are not related by a positive scalar.
* D.47.9(ii)–(iii) — the missing block is the archimedean/polar one, present in object (B) — is **correct and
  is the round's structural finding**, with the refinement that the model's `κ(k) = q^{k/2}+q^{−k/2}
  − q^{−k/2}S_k` is *poles minus zeros* by (145.4), whereas the arithmetic prime side equals poles minus
  zeros **minus an archimedean integral**; the function field has no third term, which is `MISMATCH 5`
  stated exactly. ✓
* **"δ_n and item (21) are two slots, not one" — CONFIRMED, but over-stated.** `CORPUS_CHECK_R147` §4
  establishes that item (21) and Thm 8bis.2 concern **the same symbol** `\hat W_∞(0,τ) = \logπ −
  \mathrm{Re}\,ψ(¼+iτ/2)`, and that Paper 44's diagonal computation is "precisely the `0 ∈ \mathrm{supp}`
  case, handled by the counterterm `(γ+\log4π)`". So the *archimedean half* of `δ_n` **is** item (21)'s
  object; the second slot is the finite-place `N`-linear term. Correct statement: *round 1's identification
  was wrong about `δ_n` as a whole and right about its archimedean part; and since that part **cancels** in
  `δ_m−δ_n` (D.47.2(i)), item (21) is irrelevant to the difference — which is the actual new object.*

### (6) O-46.6 and the phase-147 recommendation — **REFUTED as chartered (MAJOR)**

`CORPUS_CHECK_R147` §6 is dispositive and the round does not cite it:

> *"a single-prime tower Gram form built only from `\log p`, `p^{−k/2}` (no phase, no cross-prime, no
> independent ingredient) is **provably inadmissible** as a sign-decider by both phase-60's theorem and
> P122.028's Gate-S rule — this is confirmed, not merely suggested, by the corpus."*

* **C-I (MAJOR, corpus-check failure).** §D.47's own object is exactly that: `G^{(p)}` is built from
  `\log p`, `p^{−k/2}` and one real diagonal, with **no phase datum**. Round 1 applied P122.028 to the
  `c_{m,n}` correction term; round 2 does not apply it to its own new object, and does not cite phase 60,
  Doc 131, Doc 135, or phase 137 D.12. The tower result is therefore *admissible as a computed negative*
  (it asserts no sign-decision) but **inadmissible as a route**, and it should be labelled so.
* **O-46.6 as written — "the same tower for object (B), `Frob ⋆ Δ^{rad}`" — does not escape the bar.**
  P122.028's barred list is `\log p, p^{−1/2}, N` **and `Γ`**: adding the archimedean block `ω_∞` adds a
  `Γ`-datum, which is *inside* the barred class, not outside it. And the semilocal version of exactly this
  object is already **phase 137 §D.12**, whose recorded verdicts are (`CORPUS_CHECK_R147` §5): beyond
  `S=\{∞\}` it is `OPEN, not provable by the named means`; **added prime blocks subtract**; and D.12.5
  imports Thm 8bis.4a as "**the finite half alone carries no positivity to donate**". Re-running it on a
  tower re-opens a closed question under a new name.
* **What is actually new**, by the corpus check's own list: (1) `δ_m−δ_n` — *done here*; (2) a
  **profile-independent finite part** of the `Δ^{rad}` self-pairing (the corpus computes `O(1)` constants
  but they are `φ`-dependent, and Rem 8bis.1c forecloses this only for the *bare* diagonal); (3) any
  construction carrying an **explicit phase/unimodularity datum**, which is the one feature by which
  Doc 131's `F_{p,α}` escapes phase-60's theorem (`α = p^{1/2}e^{iφ}`).

---

## Verdict on the tower result

**The single-prime tower is real mathematics, correctly computed, and mis-framed in three ways.**

* `δ_m = δ_n` when `P(m) = P(n)` (147.3): **CONFIRMED `PROVED`**, modulo the half-line of C-D. Genuinely
  `NEW` by the corpus check's own §1c. This is the round's solid result.
* The one-parameter Gram (147.4) and Lemma D.47.4 (the chart constant cancels in `τ_p`): **CONFIRMED**, and
  the best technical idea in phases 145–146 — but the **domain of validity must be stated** (C-B).
* The trichotomy and thresholds (147.5): **CONFIRMED exactly**, including the `Ξ_a` threshold formula and
  the reason the coordinator flagged (common minimiser at `θ=π`).
* Corollary D.47.7's verdict: **CONFIRMED in the valid regime; the universal quantifier WITHDRAWN** (C-A).
  The unreported consequence — that in that regime the form is eventually *negative semidefinite* — is more
  informative than the stated one and should be recorded with a W-a screen (C-G).
* D.47.8's "A3 does not enter here either": **NOT ESTABLISHED** (C-C), and in apparent conflict with
  Doc 131 Thm 6.7 until the destructive/constructive reconciliation is written.
* §D.49's phase-147 recommendation (O-46.6): **REFUTED as chartered** (C-I).

Labels to change: D.47.5(ii) and D.47.7 → `PROVED, in the regime of validity of (147.4)`; D.47.8 →
`PROVED as a threshold computation; the non-separation conclusion is a CLAIM`; D.47.2 → `PROVED` once C-D
is inserted; the tower result to carry an explicit *"inadmissible as a sign-route by phase-60/P122.028"*
annotation; O-46.6 → **withdrawn as stated**, replaced per the residue below.

---

## Overall

Round 2 is a **model repair round on the audit and a partially self-unaware round on its own new work**.
Every one of the fourteen MAJORs is discharged at its site without dilution, and two of them (M8, M14) were
turned into the seeds of the new section. The new section then repeats, in miniature, the pattern the audit
identified in round 1: a correct local computation (the diagonal difference, the Toeplitz threshold) wrapped
in a universal claim that its source does not support (C-A), with a domain of validity left unstated (C-B),
a falsifier conclusion drawn from the wrong comparison (C-C), and a corpus check not run against the round's
own new object (C-I) — the last being the same omission that `CORPUS_CHECK_R147`, sitting in the next phase's
directory, answers in advance and in the negative.

**FATAL: none.** But C-A is the closest this programme has come to an unscreened positivity corner, and the
one should treat the requirement "every universal quantifier over `(ε,N,S,\text{convention})` must be
checked at the corners" as mandatory from here on.

---

## Residue

1. **C-A** — re-quantify D.47.5(ii)/D.47.7 to the regime of validity of (147.4). *Required before closure.*
2. **C-B** — state the domain of (147.4): `S_f ⊋ \{p\}` and `N` large enough to kill (8bis.2a). *Required.*
3. **C-C** — either compute a `Ξ_a` diagonal or downgrade "A3 does not enter here" to a claim, and reconcile
   with Doc 131 Thm 6.7 / Doc 135 §7.2 B3. *Required.*
4. **C-I** — cite phase 60, P122.028, Doc 131/135 and phase 137 D.12 against §D.47's own object, and label
   the tower `inadmissible as a sign-route`. *Required.*
5. **C-D** — insert the unique-factorization half-line in D.47.2(ii). *Required (one line).*
6. **C-G** — record the NSD chamber and the `N ≥ 9` example, with a W-a screen. *Recommended.*
7. **C-E, C-F, C-H, and the "bi-infinite"/monotonicity/`m1` slips** — corrections. **C-F**: the README's
   "*the `Ξ_a` weights move the threshold by `< 5·10⁻³`*" is **false for `p = 3` (`1.7·10⁻²`) and `p = 7`
   (`7.4·10⁻²`)**; it holds only at `p = 2`. The body (D.47.8(ii)) is correct; only the README is wrong.
8. **O-46.6** — withdraw as chartered; see below.

---

## Programme paragraph: where the sign lives, and is O-46.6 a defensible phase 147?

**The honest state after phases 145–146 is a double negative, and it is worth more than the positive
framings that preceded it.** Phase 145 named the missing ingredient (the frame has `⋆` and no `+`; the
missing effective classes are graphs of sums). Phase 146 built the `+` formally and found that *nothing
arrives with it*: the resulting form is `Φ(0)Φ(1) − ½x^{\mathsf T}Lx`, which is Paper 46's `2ab − W` with the
zero sum deleted, hence zero-blind by construction and `Ξ_a`-uniform in every one of its statements,
including the tower. Round 1's diagnosis — *the sign lives in the diagonal counterterm of an additive
structure `Spec Z` lacks* — is now known to be wrong in its stated mechanism (the counterterm is not
`n(2−2g)`; it is a computed, `P(n)`-indexed, chart-dependent number) and right only in the weak sense the
corpus has held since Rem 8bis.1c: **the diagonal is the only entry that is not a count.** What phase 146
adds to that, and it is a real addition, is that the diagonal's variation is **exactly computable and
exactly zero along a single prime's tower**, so the one place where the object is convention-free and
one-parameter is also the place where the corpus (Doc 131, Doc 135, phase 137 D.12, phase 60, P122.028) has
already proved that pure-magnitude data decides nothing. Put plainly: **the sign is not in the additive
structure, and it is not in the pure Frobenius family's diagonal either; the additive/multiplicative framing
should be retired, and what survives is the older and better-supported statement that the pure prime block
is the finite half of the kernel and the finite half is signless.**

**Is O-46.6 a defensible phase 147? As chartered, no — the corpus already shows it is pure magnitude.**
`Frob ⋆ Δ^{rad}` adds `ω_∞`, i.e. a `Γ`-datum, and P122.028 bars relations built from `\log p, p^{−1/2}, N,
Γ` *including* `Γ`; phase 137 D.12 already ran the semilocal version and recorded that added prime blocks
subtract and that the finite half has no positivity to donate (importing Thm 8bis.4a, which D.47.7 is a
sharpening of, not an escape from); and phase 60 rules a form in `\log p, p^{−k/2}` alone inadmissible as a
sign-decider. A phase 147 that computes the `\{Γ^{rad}_{p^k}\}` Gram would produce a correct table and a
fourth instance of the same negative.

**What is defensible is narrower, and the corpus check names it.** Three threads, in order:
(i) **`δ_m − δ_n` off the equal-support regime** — done here for the equal-support case, genuinely new, and
the only piece of §D.47 that is not barred; the residual question is whether the `N`-linear divergence
admits a convention-free renormalization, and Cor 8bis.1b′ suggests not, which would close it cleanly.
(ii) **A profile-independent finite part of the `Δ^{rad}` self-pairing** — the corpus computes `γ+\log4π`
and `C_φ` exactly but both are `φ`-dependent; Rem 8bis.1c forecloses canonicity only for the *bare*
diagonal, and `CORPUS_CHECK_R147`'s own "what would be NEW" list flags this gap explicitly. This is the one
Arakelov-shaped question the corpus has not asked.
(iii) **Any tower construction that carries an explicit phase/unimodularity datum** — the single feature by
which Doc 131's `F_{p,α}` escapes phase-60's theorem, and the only form in which a coupling to `Δ^{rad}` is
admissible at all. If phase 147 is to touch the tower, this is the charter: *not* the Gram of object (B),
but object (B) **plus a named non-magnitude ingredient**, with phase 60's requirement and P122.028's Gate S
printed in the blueprint the way Prop. D.42.5 is printed now.

A fourth option deserves stating plainly: **phase 146's deliverable may be terminal for this line.** Two
phases have now converged on "the finite half is signless and everything built from it is `Ξ_a`-uniform".
That is a publishable negative (`P46-40′` plus the `δ_m−δ_n` theorem), and one should weigh closing
row D's additive/tower thread on it rather than opening a phase 147 whose admissible surface is, by the
corpus's own accounting, three narrow threads and one already-refuted one.
