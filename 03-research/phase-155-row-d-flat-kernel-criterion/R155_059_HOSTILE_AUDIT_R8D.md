# R155.059 — Hostile audit of round 8d (`R155_055`, the margin-decay bound)

*Hostile auditor, phase 155, 2026-09-22. Object: `R155_055_BUILDER_ROUND8D_MARGIN_DECAY.md` (333 lines) and
`scripts/r8d/r8d_margin_bound.py`. Reference texts read: Paper 45 `main.md:872–1100` (imports (E1)–(E5), Lemmas
9.1–9.3, Thm 9.4) and `:1631–1770` (Thm 10.4); Paper 47 `main.tex:114–150` (definitions, `eq:W`, `λ^A`, `λ^W`),
`:379–447` (`thm:A`, `eq:Aform`, `rem:Kprim`, `cor:mono`), `:450–458` (`def:PD`), `:655–660` (`lem:mbounds`),
`:1081–1110` (`def:W`, `thm:Z`); Paper 46 `main.md:3972` ((X19) row); `R155_053:261,370`. Script run once
(12.8 s, see (x)). Independent recomputations in a scratch script (not committed).*

**Verdict in one line.** Theorem 1 and Corollaries 1–2 are **correct as mathematics**; the proof is a routine
zero-sum estimate on an explicit test function, and every step checks. Three AMENDs are required before the result
enters Paper 47, one of them a genuine citation error (the "(X-N)" constants are Backlund 1918, valid for `t ≥ 200`,
not Rosser 1941), none of them affecting the truth of any PROVED statement. One DIAGNOSTIC row (`T = 2`) is at the
double-precision roundoff floor and must be flagged. No FAIL.

---

## Per-claim findings

### (i) `F ∈ P_T` — PASS

Paper 47 `main.tex:128–130`: `P_T = {F ∈ L²(I_T): A(F) = B(F) = 0}`, `A = ∫F e^{t/2}`, `B = ∫F e^{−t/2}`. The memo's
Lemma 3(iii) (`R155_055:96–99`) gives `∫F e^{ct} = P(c)∫G e^{ct}` with `P(c) = (c² − ¼)(c² + γ₁²)`, so `P(±½) = 0`
kills both moments. Checked: two integrations by parts give `∫G″e^{ct} = c²∫Ge^{ct}` (no sign issue), so
`F = P(D)G = G⁗ + (γ₁² − ¼)G″ − (γ₁²/4)G` and `F̂(τ) = P(iτ)Ĝ(τ) = (τ²+¼)(τ²−γ₁²)Ĝ(τ)` — matches `:100`. The operator
`D² − ¼` is Paper 45's primitivization `Π = −∂² + ¼` up to sign (`45/main.md:1646–1650`, Lemma 10.1:
`Φ_{ΠG} = s(1−s)Φ_G`, and `s(1−s) = ¼ − (s−½)²`); consistent. Regularity for the boundary terms: `φ_k = b_k^{∗k}` is a
degree-`(k−1)` spline, `C^{k−2}`, vanishing to order `k−1` at `±1`; for `k = 5`, `G ∈ C³`, `G^{(j)}(±T) = 0` for `j ≤ 3`,
`G⁗ ∈ L^∞` piecewise constant — the four integrations by parts are legitimate (`G‴` absolutely continuous). `F` lies
in the form domain of `𝔞_T` (`47/main.tex:124`: `∫log(2+|τ|)|F̂|² < ∞`) since `|F̂|² = O(τ^{8−2k}) = O(τ^{−2})` for
`k ≥ 5`. Also `λ^A` in Paper 47 is exactly "the bottom of `𝔞_T` on the unit sphere of `P_T`" (`main.tex:142`), and
`λ^W ≤ λ^P ≤ λ^A` is `thm:A` last line + `rem:Kprim` (`main.tex:404, 419`) — the memo's chain at `:13` is licensed.

### (ii) The factor `(D² + γ₁²)` kills both `ρ₁` and `ρ̄₁` — PASS

`Φ_F(s) = P(s−½)Φ_G(s)`; at `s = ρ₁ = ½ + iγ₁`, `c = iγ₁`, `c² + γ₁² = 0`; at `1 − ρ₁ = ρ̄₁ = ½ − iγ₁`, `c = −iγ₁`, same.
Both factors of `Φ_F(ρ₁)Φ_F(1−ρ₁)` vanish; the term is `0` regardless of multiplicity (simplicity of `ρ₁` from (X19)
is not even needed here — only that no *other* zero has `|γ| ≤ 21`, which is the (X19) clause quoted at Paper 46
`main.md:3972`). On the line, `Φ_F(½+iγ)Φ_F(½−iγ) = |F̂(γ)|²` by Paper 45 Lemma 9.1 (`main.md:934–937`). PASS.

### (iii) Lower bound `‖F‖² ≥ (γ₁⁴/64)·T·(½ − ε_k(Y))` — PASS (derivation verified)

Plancherel in the memo's convention: `‖F‖² = (1/2π)∫|F̂|²`. On `|τ| ≤ γ₁/√2`: `(τ²−γ₁²)² ≥ (γ₁²/2)² = γ₁⁴/4`,
`(τ²+¼)² ≥ 1/16`, product `≥ γ₁⁴/64`. Then `(1/2π)∫_{|τ|≤γ₁/√2}T²|φ̂_k(Tτ)|²dτ = T·(1/2π)∫_{|x|≤Y}|φ̂_k(x)|²dx`,
`Y = Tγ₁/√2`; `(1/2π)∫_ℝ|φ̂_k|² = ‖φ_k‖₂² ≥ ½` by Cauchy–Schwarz on `[−1,1]` (`(∫φ_k)² = 1 ≤ 2∫φ_k²`); the tail
`(1/2π)∫_{|x|>Y}(k/|x|)^{2k}dx = (1/π)k^{2k}Y^{1−2k}/(2k−1) = ε_k(Y)`. All three steps correct (`R155_055:104–108`).
The bound `|φ̂_k(x)| ≤ (k/|x|)^k` used on `|x| > Y` is valid for all real `x` (no `Y ≥ k` needed). PASS.

### (iv) Decay, zero sum, constant `4·10⁹`, exponent `2·21/e` — PASS with two trivial AMENDs

* `φ̂_k(x) = sinc(x/k)^k`, `|sinc y| ≤ 1/|y|` ⟹ `|F̂(τ)|² ≤ (τ²+¼)²(τ²−γ₁²)²T²(k/(T|τ|))^{2k}`; for `|τ| ≥ 21`,
  `(τ²+¼)² ≤ (1 + 1/1764)²τ⁴ = 1.001134τ⁴ ≤ 1.0012τ⁴` ✓, `(τ²−γ₁²)² ≤ τ⁴` ✓ (`:127–128`).
* Lemma 4 (`:110–116`): Stieltjes by parts is right; boundary term at `H` is `−H^{−p}N(H) ≤ 0`, at `∞` vanishes for
  `p ≥ 2` under Lemma N; `∫_H^∞t^{−p}log t\,dt = H^{1−p}[log H/(p−1) + 1/(p−1)²]` ✓ (differentiated back).
* (3.1) assembles correctly: factor `2` for `±γ`, `p = 2k − 8 ≥ 2` for `k ≥ 5`, on-line part `≤ S(21,p)` (sum over
  `(21, H₀]` of nonnegative terms), off-line part `≤ e^T S(H₀,p)` (see (v)).
* Corollary 1 (`:138–150`): with `k = 21T/e + θ`, `(k/(21T))^{2k} = exp(2k[log(1 + θe/21T) − 1]) ≤
  exp(−42T/e + 2θ²e/(21T))` ✓ (`log(1+x) ≤ x`); `2e/21 = 0.2589 ≤ 0.259` ✓. `(k/T)^{2k}S(21,p) = 21⁹(k/21T)^{2k}·
  (1/2π)(p/(p−1))[log 21 + 1/(p−1)]` ✓, value `0.57976` at `k = 8`, decreasing (`0.558, 0.544, …`) ✓. Exponent
  optimisation: `min_k (k/(21T))^{2k}` at `k = 21T/e`, value `e^{−42T/e} = e^{−15.4494T}` ✓; the table's `k_opt`
  tracks `21T/e` to within `+1` ✓. Constant: `2·1.0012·0.5797·21⁹·e^{0.259}/(14.13⁴/64·0.484) = 3.963·10⁹ < 4·10⁹` ✓
  (recomputed independently).
* **AMEND (iv-a), `:143`:** "`ε_k(Y) ≤ 0.0155` for all `T ≥ 1`" is slightly wrong. At the left endpoint of the
  `k = 9` interval, `T = 8e/21 = 1.0354`, `ε_9 = 0.01566`. The script's grid (step `0.001`) misses the endpoint and
  reports `0.0155`. Since `½ − 0.01566 = 0.48434 ≥ 0.484`, the constant `0.484` and hence `3.96·10⁹` survive.
  Fix: replace `0.0155` by `0.0157` (and `0.0157` in the list "`0.0060, 0.0157, 0.0093`" is already the right
  `k = 9` value; the `k = 8` entry `0.0060` is `ε_8` at `T = 1`, not at the interval's left endpoint `0.906`, where it
  would be `0.026` — state that `k = 8` is evaluated at `T = 1`).
* **AMEND (iv-b), `:141–142`:** the `H₀`-term factor "`[log H₀ + 1/7]/[log 21] ≤ 9`" is `9.48`. Write `≤ 10`.
  Immaterial (`< 10⁻⁷⁰` relative either way).

### (v) Off-line zeros above `H₀` — PASS

For `ρ = ½ + β + iγ`, `|β| < ½` (zeros lie strictly inside `0 < Re s < 1`; Paper 45 (E2) + the Euler product, as
Lemma 9.2 uses at `main.md:975`): `Φ_G(ρ) = Ĝ(γ − iβ) = Tφ̂_k(T(γ − iβ))`, and `|sin(a+ib)| ≤ cosh b ≤ e^{|b|}` gives
`|φ̂_k(z)| ≤ (k/|Re z|)^k e^{|Im z|}` (`|Im(z/k)|·k = |Im z|`) ✓. Each of `Φ_G(ρ)`, `Φ_G(1−ρ)` carries `e^{T|β|}`, the
product `e^{2T|β|} ≤ e^{T}` ✓ (`:131–133`). `|P(β+iγ)| ≤ (γ²+β²+¼)(γ²+β²+γ₁²) ≤ (1+10⁻²²)γ⁴` for `γ > 3·10¹²` ✓, and
`Φ_F(ρ)Φ_F(1−ρ) = P(c)P(−c)Φ_G(ρ)Φ_G(1−ρ)` with `P` even, so `|P(c)|² ≤ 1.0012γ⁸` ✓. Off-line zeros are counted in
`N(t)` with multiplicity, so Lemma 4 applies to the tail; convergence needs `p ≥ 2` ✓. The `e^T` is exactly the
uniform strip bound; nothing sharper is claimed. PASS. (The auditor notes the memo could use `|β| ≤ ½` and drop
the strictness — cosmetic.)

### (vi) Lemma 1 — PASS

Extension by zero from `I_T` to `I_{T′}`: `A, B` unchanged (integrals of the same function), `‖F‖` unchanged,
`c_F` unchanged with support `[−2T, 2T]`; the new contacts `n ∈ N_{T′}∖N_T` have `log n ≥ 2T`, so `c_F(log n) = 0`,
and `(1/2π)∫cos(τ log n)|F̂|² = c_F(log n)` (Plancherel, `47/main.tex:395`). Hence `𝔞_{T′}(F) = 𝔞_T(F)` and
`P_T ↪ P_{T′}` isometrically: `λ^A(T′) ≤ λ^A(T)`. Same for `λ^W` (`W = 𝔞 + 2Re AB̄`) and for `λ^P` (`𝒦_prim` grows,
`Lév` is `T`-free, comb unchanged). Paper 47 `cor:mono` (`main.tex:422–424`) states monotonicity of `λ^P` **"with the
contact set held fixed"**; Lemma 1 removes that clause. Correctly attributed at `:53–54`. PASS.

### (vii) Corollary 2(iii), `RH ⟺ L^A ≥ 0` — PASS with one AMEND (rough-test positivity)

* (⇒) Under RH `W_T ≥ 0` on `L²(I_T)`: Paper 47 states Weil's criterion in this form (`main.tex:138–141`), but the
  classical criterion is for smooth compactly supported tests. For `F` in the form domain the extension is the
  mollification of the memo's own Lemma 2 (dominated convergence in the archimedean term, finitely many comb terms,
  `A, B` continuous). **AMEND (vii-a):** add one sentence in Cor 2(iii)'s proof: "for `F` in the form domain,
  `W_T(F) = lim W_{T+ε}(F ∗ η_ε) ≥ 0` by the argument of Lemma 2". Then `0 ≤ λ^W ≤ λ^P ≤ λ^A ≤ B(T,k) → 0` ✓.
* (⇐) If RH fails: Paper 45 Thm 10.4 (`main.md:1680–1683`) gives a nonzero compactly supported primitive real
  `F ∈ C_c^∞` with `Σ_ρ Φ_F(ρ)Φ_F(1−ρ) < 0`; for `supp F ⊆ [−T₀, T₀]`, Thm 9.4 (`main.md:1000–1008`) with
  `Φ_F(0) = Φ_F(1) = 0` gives `𝔞_{T₀}(F) < 0`, so `λ^A(T₀) < 0`, and Lemma 1 gives `L^A ≤ λ^A(T₀) < 0` ✓. The
  contrapositive "`L^A ≥ 0 ⟹ RH`" is therefore sound; the memo's route through `λ^A(T) ≥ L^A ≥ 0 ∀T ⟹` positivity
  on every `P_T ⟹ RH` (Thm 10.4's last sentence, `main.md:1682–1683`) is equally valid. The equivalences
  `L^W = 0 ⟺ L^P = 0 ⟺ L^A = 0 ⟺ L^A ≥ 0` follow from `L^W ≤ L^P ≤ L^A ≤ 0`. PASS.
* The `OPEN` label on `L^A = −∞` under ¬RH is correct: `R155_053:271–274` records the converse as non-effective.

### (viii) Lemma 5 (Route A) — PASS

`Σ_{n∈N_T}v_n c_F(log n) = 2∫_{(0,2T)}e^{−u/2}c_F(u)\,dψ_{Ch}(e^u)` ✓ (`u ↦ ψ_{Ch}(e^u)` jumps `Λ(n)` at `log n`, and
`v_n = 2Λ(n)n^{−1/2}`). `dψ_{Ch}(e^u) = e^u du + dE(u)` ✓. Main term `2∫_0^{2T}c_F e^{u/2}du`. The identity
`∫_{−2T}^{2T}c_F(u)e^{u/2}du = A(F)B(F)` for real `F`: `∫∫F(t)F(t−u)e^{u/2}dt\,du`, `s = t − u`, `e^{u/2} = e^{t/2}e^{−s/2}`
✓. Zero on `P_T`; `c_F` even ⟹ `∫_0^{2T}c_F e^{u/2} = −∫_0^{2T}c_F e^{−u/2}` ✓. Inserting into `eq:Aform`
(`47/main.tex:383–385`, `𝔞_T = C₀‖F‖² + Lév(c_F) − Σv_n c_F(log n)`) gives exactly (4.1) with the stated signs ✓.
The expression for `E(u)` is the standard explicit formula for `ψ_{Ch}` ✓. The "Consequence" paragraph is correctly
labelled PROVED-as-stated / DIAGNOSTIC-as-verdict; its claim that `X20a`-type bounds give `+∞` is an honest
size estimate, not a theorem. PASS.

### (ix) DIAGNOSTIC labelling — PASS, with one required flag

§3.4 and §8 last column are labelled DIAGNOSTIC / not certified (`:190–197, 318–320`) ✓; the `mpmath` zero list is
declared "not an import of record" ✓; §3.3 ceiling and §6 are HEURISTIC ✓ and nothing PROVED depends on them
(`:318`). Two defects:
* **AMEND (ix-a), `:184` and `:308`, the `T = 2` row.** `𝔞_T(F)/‖F‖² = 8.4·10⁻¹⁵` is a cancellation of 15 digits
  between `(1/2π)∫m|F̂|²` and the comb, i.e. **at the double-precision roundoff floor**. Auditor's recomputation with
  panel widths `h = 0.5, 0.25, 0.125, 0.0625` gives `8.58, 8.38, 7.90, 8.02 ·10⁻¹⁵` — a `±5–10 %` scatter with no
  convergence — and the script's own zero-sum cross-check at `T = 2` (printed by the script, **omitted from the memo**,
  which quotes only `T = 1, 1.5`) disagrees by `2.1·10⁻³` relative while its stated zero tail is `4·10⁻²⁰`: the
  discrepancy is quadrature/roundoff, not zeros. The `T = 1.5` row is stable to `10⁻⁶` under the same test and the
  `T ≤ 1` rows are fine. Fix: mark the `T = 2` entry "`≈ 8·10⁻¹⁵ (±10 %, roundoff-limited)`" and add the `T = 2`
  cross-check figure to the sentence at `:196–197`.
* Minor: `:190` says panels "of width 0.25 to τ = 4000" — true; the script docstring says "eq. (1.7) of the memo"
  (should be (3.1)) and "runtime ~20 s" while the README says 9 s. Harmonise.

### (x) Script run — PASS (12.8 s, not ≤ 10 s)

Run once on this machine: all table values of §3.2 and §8 reproduce to the printed digits (`B(1,8) = 28.08`,
`B(1.5,12) = 1.685·10⁻²`, `B(2,15) = 9.651·10⁻⁶`, `B(3,23) = 2.714·10⁻¹²`, `B(10,77) = 9.398·10⁻⁵⁹`); crossings
`1.226, 1.852, 2.303` ✓; envelope ratio `0.0360 ≤ 1` ✓; constant `3.963·10⁹` ✓. Runtime `12.8 s` against the README's
"~9 s" and the round order's `≤ 10 s` — over budget by 30 %; the `mpmath.zetazero` block is the cost. Acceptable; note
it.

### (X-N), Lemma N — AMEND (citation error; statement true)

**The constants `0.137, 0.443, 4.35` at `R155_055:34–35` are not Rosser's.** They are **Backlund (1918)**:
`|N(t) − (t/2π)log(t/2πe) − 7/8| < 0.137 log t + 0.443 log log t + 4.350`, **for `t ≥ 200`**. Rosser (1941, Thm 19)
improved the constant to **`1.588`** and extended the range to **`t ≥ 2`**; Trudgian (2014) gives
`0.112 log t + 0.278 log log t + 2.510` for `t ≥ e`. The memo attributes Backlund's constants to Rosser with Rosser's
range `t ≥ 2` — a hybrid that is not a published statement. The builder flagged this himself (`:283–286`, "quote from
memory"). Consequence for Lemma N: none of substance. Auditor's check on `[21, 10¹⁵]`: slack
`(t/2π)log t − upper` is minimal at `t = 21` and equals `6.11` (Rosser), `5.45` (Trudgian), `3.35` (Backlund's
constants, if one ignores its range); `N(21)` upper bounds `4.06 / 4.73 / 6.83` against `(21/2π)log 21 = 10.18`
and the true `N(21) = 1`. The bracket is decreasing on `t ≥ 21` (derivative `0.137/t + 0.443/(t log t) − 0.4517 < 0`).
**Fix:** state (X-N) as Rosser 1941 Thm 19 with constant `1.588` for `t ≥ 2` (or Trudgian 2014, *J. Number Theory*
134, Thm 1), and rerun `(A)` with `1.588` (slack `6.11`). Also record (X-N) in the phase's import ledger as an import
of record; it is new to the corpus.

### (X19) — PASS with a bookkeeping note

Paper 46's (X19) (`main.md:3972`) imports: `ρ₁` simple on the line, `γ₁ = 14.1347…`, no other zero with `|Im ρ| ≤ 21`,
citing Platt–Trudgian 2021. The memo additionally uses "every zero with `|Im ρ| ≤ 3·10¹²` is on the line"
(`:30–32`) — that is what Platt–Trudgian prove, but it is **not the clause Paper 46 imported**. Record it as
(X19′), same source, so the ledger is exact.

### Lemma 2 (mollification of Thm 9.4) — PASS

Thm 9.4 (`45/main.md:1000–1008`) is for real `F ∈ C_c^∞`, `supp ⊆ [−T,T]`, zero sum in symmetric order, finite prime
sum over `n < e^{2T}`, polar term `2Φ_F(0)Φ_F(1)`, archimedean `(1/2π)∫|F̂|²m` — matches the memo's (EF) and Paper 47
`eq:W` (`A = Φ_F(1)`, `B = Φ_F(0)`, `2Re AB̄ = 2Φ_F(0)Φ_F(1)` for real `F`). Proof of Lemma 2 (`:64–73`): `F_ε ∈ C_c^∞`,
window `T+ε`; `|Φ_{η_ε}(s)| ≤ e^{ε|Re s−½|} ≤ e^{ε/2}` in the strip ✓; dominated convergence on the zero side by the
hypothesis (b) (each term `≤ e^{ε}|Φ_F(ρ)Φ_F(1−ρ)|`) ✓ and no circularity — (b) is verified in step (6) of Theorem 1
from the decay bounds alone; archimedean side: `|η̂_ε| ≤ 1`, `|m(τ)| ≤ |C₀| + log(1+|τ|)` follows from `lem:mbounds`
(`47/main.tex:655–660`) ✓; prime side: the window `T+ε` adds contacts `e^{2T} ≤ n < e^{2T+2ε}` where `c_F = 0` but
`c_{F_ε} ≠ 0`; the memo handles this correctly by uniform convergence `c_{F_ε} → c_F` over the finitely many `n`
(`:71–73`) ✓. PASS.

### Theorem 1 as a whole — PASS

Steps (1)–(7) (`:124–136`) verified individually above. The statement "`limsup λ^A ≤ 0`" follows from Cor 1.
Labels are right: PROVED under (X19), (X-N), (EF), (SUF). The builder's self-assessment "trivial half of Zhu" (`:171`)
is accurate and should be kept when the result enters Paper 47.

---

## Verdicts

| Item | Verdict |
|---|---|
| Lemma 1 (monotonicity, no fixed contacts) | **PASS** |
| Lemma 2 (explicit formula for rough `F`) | **PASS** |
| Lemma 3 (i)–(v) | **PASS** |
| Lemma 4 | **PASS** |
| Lemma N / (X-N) | **AMEND**: constants are Backlund 1918 (`t ≥ 200`), not Rosser 1941; cite Rosser with `1.588`, `t ≥ 2` (or Trudgian 2014); statement true, slack `6.11` |
| Theorem 1, (3.1) | **PASS** |
| Corollary 1, (3.2) | **PASS** after AMEND (iv-a) `0.0155 → 0.0157` (constant `0.484` survives) and (iv-b) `9 → 10` |
| Corollary 2 (i),(ii),(iv),(v) | **PASS** |
| Corollary 2 (iii) | **PASS** after AMEND (vii-a): one sentence extending Weil positivity to the form domain |
| Lemma 5 (Route A) | **PASS** |
| §3.3, §6 | HEURISTIC, correctly labelled; nothing depends on them |
| §3.4 DIAGNOSTIC | **AMEND** (ix-a): `T = 2` row is roundoff-limited (`±10 %`), and the omitted `T = 2` cross-check (`2·10⁻³`) must be reported |
| Script | reproduces every table entry; runtime `12.8 s` (> 10 s budget), fix docstring/README |
| (X19) usage | PASS; record the on-line-to-`3·10¹²` clause as (X19′) |

**Final verdict.** Theorem 1 and Corollaries 1–2: **PROVED**, under the imports (X19)/(X19′), (X-N) as corrected,
Paper 45 Thms 9.4 and 10.4. No claim is false; four AMENDs (X-N citation; `0.0155 → 0.0157`; `9 → 10`; rough-test
Weil positivity sentence) and one DIAGNOSTIC flag (`T = 2` row). Row-D label unchanged; endpoint of record
unchanged; no sign for `ζ` at any window — the memo says so itself (`:320–322`) and the auditor concurs.

## What may enter Paper 47, and where

1. **Lemma 1** as a remark after `cor:mono` (`main.tex:422–447`), stating that the clause "with the contact set held
   fixed" can be dropped, with the four-line proof. Also fixes the logical gap that `cor:mono` as written does not
   give monotonicity across contact thresholds.
2. **Lemma 2** as a lemma in §1 or §9 (Paper 47 already invokes Thm 9.4 for `L²(I_T)` at `main.tex:134–137` without
   proof of the rough case; Lemma 2 is that proof). This is the most useful piece for the paper's own rigour.
3. **Theorem 1 + Corollary 1 + Corollary 2(i)–(iii)** as a new subsection of §9 ("The margin decays"), replacing the
   HEURISTIC clause of `R155_053` Prop. 4.1 and placed next to the Landau–Widom remark at `main.tex:1768`; with the
   explicit sentence that the rate `e^{−15.45T}` is linear in the exponent and exponentially weaker than Zhu's
   conjectured `e^{−ce^{2T}}` — "the trivial half". State (X-N) in the paper's import table with the corrected
   Rosser/Trudgian citation and (X19′) alongside (X19).
4. **Lemma 5** as a remark in §9.3 item 5 (the prime side of a primitive test is the Chebyshev remainder).
5. **Not to enter:** §3.3 ceiling `e^{−42T}`, §6 (HEURISTIC), §3.4 values (DIAGNOSTIC) except possibly one sentence
   noting the proof loses `10⁵–10⁹` on its own test function, without the `T = 2` figure.

Per the phase rule (`feedback-check-against-paper-definitions`): all three definitions used here — `P_T`, `λ^A`,
`eq:W` — were checked against `main.tex:114–142` and match the memo's §Notation verbatim.
