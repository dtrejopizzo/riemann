# R143.004 — Hostile confirmation, round 2, phase 143

*Auditor: Claude Opus 5. Date 2026-09-13. Inputs: `R143_003_BUILDER_ROUND2.md` (ledger) and the
in-place repairs in `R143_001_BUILDER_ROUND1.md` (now 1141 lines) and `README.md`, checked against
`R143_002_HOSTILE_AUDIT.md` finding by finding. Method unchanged: nothing accepted on the ledger's
word — every repair re-derived at the statement it touches; every new constant recomputed with mpmath
at `mp.dps = 30–40`. Sources re-opened for this round: Paper 46 Definition–Theorem 11.7(i) (`K > 0`,
now elementary and printed as such), Theorem 11.8(i),(iii), Theorem 11.13(i), Prop. 12.4B;
`R141_001` Lemma D.26.1, Lemma D.26.3, Theorem D.26.5, Lemma D.26.6; `R142_001` D.31.7, D.31.10;
`R142_004` J3. No builder file edited.*

**Verdict: round 2 is ACCEPTED. Ten of eleven findings are fully discharged; H1 is discharged in its
mathematics but its re-proof introduces one new defect (H12, MAJOR, two-line repair, same
non-load-bearing theorem). Two new MINOR findings (H13, H14). The main line is untouched and still
stands. `(G⁺)` is now genuinely unconditional — Lemma D.34.9′ is correct and is the best thing in the
round. No FATAL. Row D label: unchanged, correctly.**

---

## 1. Per-finding status

| finding | claimed | verified? | auditor's note |
|---|---|---|---|
| **H1** | Lemma D.34.6a + re-proved D.34.7 give `C'_X = +∞` | **PARTLY — see H12** | The width-parametrised family is **correct** and the diagnosis was accepted exactly. I re-derived every clause of Lemma D.34.6a (below) and the trace verification of D.34.7 at `n = 1` and `n ≥ 2`, which are now right and no longer rest on an exact cancellation of digits. **But the final step — `I_∞(E,X) = −2\mathrm{Re}(Φ_E(ρ_1)Φ_X(1−ρ_1)) + O(1)` — is false as printed**: `I_∞(E_0,X) = t\,b_J(Φ_X(1)−Φ_X(0)) + εI_∞(K,X)` and `t → ∞`. See H12; the theorem is nevertheless true, by a two-line case split I give there. |
| **H2(i)** | cone defined for every admissible `g`; `∃g` in D.34.10, D.34.12, O-24 | **YES** | Definition D.34.1's Convention, Theorem D.34.5 ("for any admissible `g`"), Theorem D.34.8 ("the choice of an admissible `g`"), Corollary D.34.12 (`∃ admissible g ∃h⁰`, with the `⟸`/`⟹` asymmetry spelled out), O-24 ("is there an admissible `g` such that…"). Exactly the repair asked for, and no statement now hides a side condition in a definition. **Accepted.** |
| **H2(ii)** | count was three; now two, because `(G⁺)` is unconditional | **YES, and better than asked** | The boxed "RH-uses, counted" paragraph states the history honestly ("the count of three was correct against round 1"), and Lemma D.34.9′ removes the third rather than merely quantifying it. O-24 now names the two steps and says two, not three. **Accepted.** |
| **H3** | D.34.14(ii) → `CLAIM`, O-28 opened | **YES** | Label table, P46-40 and the open list all carry it; (i) is kept `PROVED` and restated as "the mechanism's only zero-location input", which is the correct and useful half. O-28 is stated as a realisation/interpolation problem for a general admissible `Z`, which is the right generality. **Accepted.** |
| **H4** | "strictly stronger" deleted everywhere | **YES — grep-verified** | Grep leaves four occurrences of the phrase in `R143_001`/`R143_003` and **every one of them is a retraction or a prohibition** (the round-2 header note; D.34.8's remark "Round 1 called it … That is false"; D.35(v) "*not* 'strictly stronger', since the two clauses are incomparable"; P46-37 "Must not be described as…"), and none in the README. No assertion of the claim survives; the replacement wording ("beside Theorem 12.3, incomparable clause, fewer and cheaper cone inputs, not refuted by D.31.10") is accurate. The auditor's verification that dropping `E' ≢ 0` is harmless is recorded at Definition D.34.8a, correctly attributed. **Accepted.** |
| **H5** | label split into a proved bracket and a certified value | **YES** | Theorem D.33.4 now prints `PROVED: s_* = m(γ_1) ∈ [0.99845824…, 0.99846016…]` with attainment at `ρ_1`, and `CERTIFIED: m(γ_1) = s_1` (the `θ`-argmin). Both endpoints recomputed here: `L(γ_1) = 0.998458240354706579`, `s(γ_1,π/2) = 0.998460162718809109`. The §Label row matches. (The README's headline bullet and P46-34 still print the unsplit form — H14(c).) **Accepted.** |
| **H6** | generic-`c_k` sentence withdrawn; `{2^k}` recorded; restated as (α)+(β); O-29 | **YES** | Remark D.34.15(ii) now retracts the false sentence explicitly, prints the `{2^k}` generating function correctly, and restates the role of A8 as (α) a multiplicative semigroup with a continuable generating function plus (β) `ξ`'s two **real** polar exponents. O-29 asks the right follow-up. (P46-41's table row was not updated — H14(b).) **Accepted.** |
| **H7** | round 1's Lemma D.34.9 demoted to Remark D.34.9a `SKETCH`, moot | **YES** | And the demotion is honest about both defects (RH-conditionality; the perturbation must be confined to the two bumps). Used nowhere. **Accepted.** |
| **H8(a)** | half-circle argument replaced | **YES** | "Every closed arc of length `π` contains a point at which `|\mathrm{Re}(e^{iψ}w)| = |w|`" — correct (the two such points are antipodal). **Accepted.** |
| **H8(b)** | factor-2 margins, coincidence removed | **PARTLY — H14(a)** | At `n = 1` there is now a genuine factor-`2` margin (`t_1(E) ≥ p_0ε/2`). At `n ≥ 2` the bracket `½p_0tb_J − 2rG_σ|Φ_g(ρ_1)| − 2rκΛ_σG_σ` is **exactly `0`** by the definition of `t` — the cancellation is still exact, by construction. That is mathematically fine (`t_n ≥ 0` is all `B4` requires) but the round-2 note claims "every inequality has a factor-`2` margin and the two cancellations are not exact", which is not what the proof does. Wording only. |
| **H9** | both regimes `a ≶ ¼` printed | **YES** | And the common conclusion (the cascade never closes for `Ξ_a`, while (T1′)_a does hold) is preserved. **Accepted.** |
| **H10** | Remark D.34.16c computes it; the round-1 assertion was doubly wrong | **YES, and the correction is a real gain** | I re-derived it: for `Ξ_a` the leading polar exponent is `n^{½+a}` and every zero exponent is `n^{½−\mathrm{Re}ρ}` with `\mathrm{Re}ρ ∈ (−a,1+a)` strictly, so eventual positivity **transports**; `\deg_a E_r = \deg_a K_a` and `R_a(E_r) → +∞` for **either** sign of `r` (since `q_a > 0` and `F_+` is `Ξ_a`-primitive, so it contributes nothing to the four polar coefficients); `F_+ ∉ 𝓝_∞^{(a)}` gives some `m` with `t^{(a)}_m(F_+) ≠ 0` by the `Ξ_a`-analogue of `\ker T = 𝓝_∞`; the sign of `r` is then chosen. `m` is fixed and `m < N_a(E_r)` automatically. **Accepted, and this is the sharpest falsifier statement the phase has produced.** |
| **H11** | Cor. D.34.12 carries `PROVED` + `RESTATEMENT` | **YES** | With the `∃g` quantifier and the directional asymmetry printed. **Accepted.** |

---

## 2. Per-item verdicts (the coordinator's priorities)

### (1) Lemma D.34.6a and the re-proof of Theorem D.34.7 — **ACCEPTED with H12.**
* **(i)** `∫e^{−u²/2σ²}e^{αu}du = σ\sqrt{2π}e^{α²σ²/2}` and `\sin x = (e^{ix}−e^{−ix})/2i`: correct, and
  `G_σ = σ\sqrt{2π}/2` is the right amplitude.
* **(ii)** At `s = ρ_1` the two exponents are `(2iγ_1)²σ²/2 = −2γ_1²σ²` and `0`, so
  `Φ(ρ_1) = iG_σe^{−iφ}(1+O(e^{−2γ_1²σ²}))`: modulus `G_σ`, phase free. ✓ (I checked the sign:
  `−1/i = i`.)
* **(iii)** At `s ∈ \{0,1\}`, `\mathrm{Re}((∓½±iγ_1)²)σ²/2 = (¼−γ_1²)σ²/2`. ✓
* **(iv) the exponent `23`, recomputed.** For a zero `ρ = β+iγ`, `s−½ = c−iγ` with `|c| < ½` by (E2),
  so the exponents' real part is `(c²−(|γ|−γ_1)²)σ²/2 ≤ (¼−(|γ|−γ_1)²)σ²/2`. With (V2)
  `|γ| ≥ γ_2 = 21.0220396…` I get `((γ_2−γ_1)²−¼)/2 = 23.5926`; with the weaker `|γ| ≥ 21` the
  builder's printed value, `((21−γ_1)²−¼)/2 = 23.4410`. Both exceed `23`, so
  **`Λ_σ ≤ Ce^{−23σ²}` is correct and conservative**, and the Riemann–von Mangoldt count
  `\#\{γ ∈ [T,T+1]\} ≤ \log T` makes the sum converge with an absolute `C` and **no zero list**.
  *Consistency check the builder claims and I verified:* at `σ = 3`, `e^{−23.441·9} = 10^{−91.6}` —
  exactly `R142_001`'s `10^{−90}` order. **Round 1 was the `σ = 3` slice of this family, as stated.**
* **The trace verification.** `n = 1`: `t_1(E) ≥ p_0ε − 2rκΛ_σG_σ = p_0ε/2 > 0` with
  `r = p_0ε/(4κΛ_σG_σ)`. ✓ `n ≥ 2`: `t_n(E_0) ≥ ½p_0tb_Jn^{½}` (since `1−1/n ≥ ½`), and the choice of
  `t` makes the bracket vanish, so `t_n(E) ≥ 0`. ✓ `\deg E = ε = 1` is fixed while
  `rG_σ = p_0ε/(4κΛ_σ) ≥ ce^{23σ²} → ∞`. ✓ **The amplitude is now genuinely unbounded — H1's
  mathematical content is repaired.**
* **H12 (MAJOR, new).** The last step reads *"`I_∞(E,X) = −2\mathrm{Re}(Φ_E(ρ_1)Φ_X(1−ρ_1)) + O(1)`,
  the `O(1)` being the polar and leakage terms of `X` against `E_0` and `rF_σ^{(φ)}`"*. The leakage
  part is `O(1)` (indeed `rG_σΛ_σ = p_0ε/(4κ)` is constant — nicely arranged). The `E_0` part is
  **not**: `Φ_J(ρ) ≡ 0` and `a_J = −b_J`, so
  `I_∞(E_0,X) = t\,b_J\big(Φ_X(1)−Φ_X(0)\big) + εI_∞(K,X)`, and `t ≍ 4rG_σ|Φ_g(ρ_1)|/(p_0b_J) → ∞`.
  Both surviving terms are `Θ(rG_σ)` and could cancel for a particular `X`, so the displayed
  conclusion does not follow. **The theorem is still true**, by the case split the proof should print:
   – if `Φ_X(1) ≠ Φ_X(0)`: fix `σ` (hence `r`) and let `t → ∞` (admissible: `t_n(E)` is increasing in
     `t` for every `n`, so `E` stays in `B4^g`, and `\deg E = 1` is unchanged); then
     `|I_∞(E,X)| ≥ t|b_J||Φ_X(1)−Φ_X(0)| − O(1) → ∞`;
   – if `Φ_X(1) = Φ_X(0)`: the `E_0` term is `εI_∞(K,X) = O(1)` and the printed argument runs verbatim.
  Either way `C'_X = +∞`. **Severity MAJOR (it is the proof of the theorem's headline claim), but
  non-load-bearing (nothing uses (T2)) and repairable in two lines.**

### (2) Lemma D.34.9′ — **ACCEPTED. Correct, unconditional, and the round's best result.**
Re-derived in full:
* `I_∞(g_λ,g_λ) = I_∞(K,K) + 2λI_∞(K,h) + λ²I_∞(h,h) = ½ + λ\deg h + λ²I_∞(h,h)`, using
  `I_∞(K,K) = ½` (Thm 11.8(ii)) and `I_∞(K,h) = ½\deg h` (Thm 11.8(i)). ✓ `\deg h > 0` by Thm
  11.13(i) (`h ≥ 0`, `h ≢ 0`). ✓
* **All sign configurations.** `I_∞(h,h) = 2Φ_h(0)Φ_h(1) − W(h) ≥ −W^{\mathrm{abs}}(h)` because
  `Φ_h(0),Φ_h(1) > 0` and `W(h) ≤ W^{\mathrm{abs}}(h)` **whatever the signs/phases of the individual
  `Φ_h(ρ)Φ_h(1−ρ)`** — this is the point of using the absolute sum, and it makes the bound
  unconditional. With `λ ≤ (2W^{\mathrm{abs}}(h))^{−1/2}` one gets `λ²W^{\mathrm{abs}}(h) ≤ ½`, hence
  `I_∞(g_λ,g_λ) ≥ λ\deg h > 0`. ✓ The equivalent form,
  `W^{\mathrm{abs}}(g_λ) = λ²W^{\mathrm{abs}}(h) ≤ ½ ≤ 2Φ_{g_λ}(0)Φ_{g_λ}(1)` (the last because
  `Φ_{g_λ}(0) = Φ_{g_λ}(1) = ½+λΦ_h(0) ≥ ½`), is Definition D.34.8b. ✓ `W^{\mathrm{abs}}(h) ∈ (0,∞)`
  by (11.2)+(E3d)+rapid decay, so `λ_0` is a genuine positive number. ✓
* **Is `(G⁺)`-absolute what D.34.10 consumes?** Yes: under RH `W^{\mathrm{abs}}(g) = Σ|Φ_g(ρ)|² = W(g)`,
  and unconditionally the absolute form is the stronger one. Definition D.34.8b says exactly this. ✓
* **Admissibility of `g_λ`, and the compact-support question — the coordinator's main worry.**
  `K` is real, even, `K > 0` (Paper 46 Thm 11.7(i), and since phase-135 round 2 that positivity is
  **elementary and printed**: each term of (11.7) is `2πn²e^{5u/2}e^{−πn²e^{2u}}(2πn²e^{2u}−3)` with
  `2πn²e^{2u} ≥ 2π > 3` for `u ≥ 0`, plus evenness — so no import is being leaned on), `K ∈ D^W`
  (super-exponential decay). So `g_λ ≥ 0`, even, real, `≢ 0`, in `D^W`. The Baire condition is
  inherited exactly as the builder says: `Φ_K(1−ρ) = ξ(1−ρ) = 0` ⟹ `Φ_{g_λ}(1−ρ) = λΦ_h(1−ρ) ≠ 0`,
  and the rapid decay in `|γ_ρ|` likewise. **`K` is not compactly supported, so the admissible class
  must be widened from `C_c^∞` to `D^W` + rapid decay — Definition D.34.1's Convention now says so
  explicitly.** I checked every place where `g`'s compact support was used in §D.26 and §D.34:
   – Theorem D.26.5's last line and Lemma D.34.3's convergence use only `Φ_g(1−ρ) ≠ 0` and rapid decay
     of `Φ_g(1−ρ)` — both inherited from `h`, and the widened list names them. ✓
   – `Φ_g(0),Φ_g(1) > 0`: computed directly, `= ½+λΦ_h(0)`. ✓
   – `τ_{\log n}g ∈ D^W`: `D^W` is `τ`-stable (Lemma 11.2(i)), and `K` in particular. ✓
   – the arithmetic reading `t_n = \mathrm{PRIME} − \mathrm{ARCH}`: Definition 11.4 and Theorem 11.5
     are stated on `D^W`, and the prime sum converges absolutely for every `h ∈ D^W` by (11.1)
     (Lemma D.26.3's parenthetical) — compact support was never what licensed it. ✓
   – Lemma D.26.6 (used in Theorem D.34.6(i)): its Langer argument needs `Φ_g(ρ) ≠ 0`, which holds. ✓
   – `κ := \max_ρ|Φ_g(1−ρ)| < ∞` in Theorem D.34.7: ✓.
  **Nothing in §D.26 or §D.34 breaks under the widening.** One consequence worth printing, which the
  builder does not: `B4^{g_λ}` is a *large* cone (the polar coefficients are `≈ ½` while the zero side
  carries a factor `λ`), so the `∃g` of Corollary D.34.12 is being satisfied by the most permissive
  admissible test class — which is legitimate (D.34.8 holds for **every** admissible `g`) and is the
  right way to use the quantifier, but it also means `(b′)_{B4^{g_λ}}` is the weakest form of the
  clause, and the `Ξ_a` falsifier must be (and is) run for the same `g`-freedom: Corollary D.34.13's
  proof quantifies over `h⁰` and works for every admissible `g_a`, so no FATAL appears from the
  quantifier change. **Checked.**

### (3) Remark D.34.1a — **ACCEPTED, and it is load-bearing hygiene.**
`Φ_K(1−ρ) = ξ(1−ρ) = 0` at every zero, so with `g = K` the traces are purely polar,
`t_n(E) = ½(n^{½}Φ_E(0)+n^{−½}Φ_E(1))`, every primitive class has `t_n ≡ 0`, and
`B4^K ∩ P^W = P^W ⊄ 𝓝_∞`: **(T1′) would be false**. Correct, and it identifies precisely why the Baire
condition is not decoration. It also shows the `K+λh` construction is the minimal fix rather than a
trick. Good that this is printed next to Lemma D.34.9′.

### (4) Proposition D.34.16 — **ACCEPTED with H13 (MINOR).**
* **(i)** `t_n ≥ n^{½}(bΦ_g(1) − Σ|c_ρ|n^{−\mathrm{Re}ρ}) − |a|Φ_g(0)n^{−½}` is (D.34.1) with
  `|n^{½−ρ}| = n^{½−\mathrm{Re}ρ}`; each `n^{−\mathrm{Re}ρ} → 0` by (E2) and all terms are dominated by
  the summable `|c_ρ|`, so the sum `→ 0` by dominated convergence. **Unconditional, and correctly
  flagged non-effective** when `\inf_ρ\mathrm{Re}\,ρ = 0` — which, I note, is *not* excluded by any
  classical zero-free region (those give `\mathrm{Re}\,ρ < 1 − c/\log|γ|`, hence by `ρ ↔ 1−ρ`
  `\mathrm{Re}\,ρ > c/\log|γ| → 0`). ✓
* **(ii)** Both branches are the two halvings of `bΦ_g(1)n^{½}`; arithmetic correct. ✓
* **(iii) H13 (MINOR).** The printed bound `N(E) ≤ 4W(E)W(g)/(b²Φ_g(1)²)` keeps only the **first**
  branch of (ii)'s `\max`, with no justification. It is in fact correct in context — under RH on
  `\{R > 0, \deg > 0\}` one has `a > 0` (Theorem D.34.10), so the term `aΦ_g(0)n^{−½}` is
  **positive** and never needs subtracting, and the `|a|`-branch disappears — but the proof must say
  that line, since (ii) as stated would otherwise leave the second branch unbounded. One sentence.
  The Cauchy–Schwarz step `S(E) ≤ \sqrt{W(E)W(g)}` and `β_{\min} = ½` under RH are both correct, as is
  the `\inf ∅ := +∞` convention for classes with no zero data.
* **(iv) the `a,b > ¼` derivation, re-derived independently as asked.** Under RH `W(E) ≥ 0`; `R(E) > 0`
  reads `2ab − W(E) > ½\deg E = ½(a+b)`, so `2ab > ½(a+b) ≥ ½a`, and `a > 0` gives `b > ¼`;
  symmetrically `a > ¼`. ✓ Then `W(E) < 2ab ≤ ½(a+b)² ≤ d²/2` (AM–GM) ✓, and with `g` even and `(G⁺)`
  (`W(g) ≤ 2p_0²`), `N ≤ 4·(d²/2)·2p_0²·16/p_0² = 64d²`. ✓ **The constant `64` is exactly right.**
* **Example D.34.16b:** `4·79780·2/40000 = 15.956` ✓ recomputed; `n ≤ 15` is the correct reading; J3's
  uniform margin is consistent. **H14(d):** `64d² = 1.024×10^7` at `d = 400` is `5.81` orders above
  `15.956`, not "three orders" as printed.
* **Remark D.34.16c (`Ξ_a`)** — verified in full (see H10 above). The conclusion *"the A3-line is in
  the head, not the tail"* is correct and is the most useful sentence produced this round: for `Ξ_a`
  the tail is positive for the same unconditional reason as for `ξ`, and the failure is a **single
  fixed index** `m`, determined by `F_+` alone and independent of `r`.

### (5) H5 bracket, H6 restatement, O-29 — **ACCEPTED** (details in §1). O-28 and O-29 are stated at
the right generality; O-29's observation that the sparse cone gives a **formally weaker clause** in
Theorem D.34.8 is correct (a larger cone makes `(b′)` easier) and is a legitimate cheap lead.

---

## 3. New findings of this round

* **H12 (MAJOR, non-load-bearing, two-line repair).** Theorem D.34.7's final step: `I_∞(E_0,X)` is
  `Θ(t)`, not `O(1)`, because `I_∞(J,X) = b_J(Φ_X(1)−Φ_X(0))` need not vanish. Repair by the case
  split printed in §2(1). Until repaired, Theorem D.34.7 should read `PROVED` **for every `X` with
  `Φ_X(1) = Φ_X(0)`** and `SKETCH` otherwise — or simply carry the two lines.
* **H13 (MINOR).** Proposition D.34.16(iii) silently drops the `|a|`-branch of (ii)'s `\max`; correct
  under RH because `a > 0`, but the sentence is missing.
* **H14 (MINOR, four wording/bookkeeping items).**
  (a) the H8(b) note claims factor-`2` margins "at every step"; the `n ≥ 2` bracket is still exactly
  `0` by construction (harmless, since `t_n ≥ 0` suffices);
  (b) paper-facing row **P46-41** still prints round 1's retracted formulation ("A8 enters through the
  index set `n ∈ N`") although Remark D.34.15 and the §Label row are correctly restated;
  (c) **P46-34** and the README headline bullet still print `s_* = s_1` without H5's proved/certified
  split;
  (d) "three orders of magnitude worse" in Example D.34.16b should be "nearly six" (`5.81`).

---

## 4. Overall verdict and residue

**Round 2 is accepted.** The ledger is honest (it states where the auditor's count of three was
correct *against round 1*, and where round 1 was right only accidentally), nothing was relabelled
upward without proof, two labels moved down, one theorem was genuinely re-proved, and the one label
that moved up — `(G⁺)`: OPEN → PROVED unconditionally — is earned by a correct one-line lemma.

**Residue after this round:** H12 (repair Theorem D.34.7's last step, or restrict it), H13 (one
sentence in D.34.16(iii)), H14(a)–(d) (wording and two stale table rows). **No open MAJOR touches the
main line:** Lemma D.34.3, Theorem D.34.4, Theorem D.34.5, Theorem D.34.8 are unchanged since round 1
and have now survived two independent re-derivations; Theorem D.34.10 and Corollary D.34.12 are
unchanged except for the `∃g` quantifier and the discharge of `(G⁺)`. **No FATAL**, and the
`Ξ_a` separation survives the quantifier change (Corollary D.34.13 is proved for every admissible
`g_a` and every `h⁰` with (a),(c)).

---

## 5. Is the final state correctly labelled?

**Yes, with one addition.** The state *"RH ⟺ `(b′)_{B4}` for `h⁰_{RR}^{+}`; a finite non-uniform
condition per class; uniform `N ≤ 64d²` per degree slice under RH"* is correctly labelled
`PROVED` + `RESTATEMENT` (Corollary D.34.12) with `PROVED` (i),(ii) unconditional / (iii),(iv) under
RH for Proposition D.34.16. The addition the text should make explicit, because a reader will
otherwise over-read the word "finite":

> **the finiteness of the range is conditional on `b = Φ_E(0) > 0`, which off RH does not follow from
> `R(E) > 0`,** and **the effectivity of `N(E)` is conditional on `β_{\min}(E) > 0`, which for a
> general class is a zero-free-strip statement** — no classical zero-free region gives
> `\inf_ρ\mathrm{Re}\,ρ > 0`, since `ρ ↔ 1−ρ` turns `\mathrm{Re}\,ρ < 1−c/\log|γ|` into
> `\mathrm{Re}\,ρ > c/\log|γ| → 0`.

Corollary D.34.16a states the first caveat; the second is stated qualitatively ("`β_{\min}(E)` may be
`0`") but its strength is not: **unconditional uniformity of `N` on a degree slice is equivalent to a
quasi-RH zero-free strip.** That should be printed, because it rules out one of the three candidate
phase-144 targets.

---

## 6. Phase-144 judgement

Of the coordinator's three candidates:

1. **"The unconditional uniformity of `N` on slices" — REJECT as a target.** By the remark above it
   is a zero-free-strip statement (`\inf_ρ\mathrm{Re}\,ρ ≥ δ > 0`), strictly stronger than anything
   classical and not obviously weaker than RH. Recording *why* it is blocked is worth a paragraph;
   attacking it is not.
2. **"The head `n < N(E)` on a degree slice" — ACCEPT, but only in the sharpened form below.** The
   plain form inherits both caveats (`b > 0` is itself RH-flavoured: a witness with `R(E) > 0`,
   `\deg E > 0`, `Φ_E(0) < 0` would refute `(b′)_{B4}` and hence, by Corollary D.34.12, refute RH —
   so it cannot be constructed, and the sub-question is RH-hard in the negative direction too).
3. **"The A3-line at the finite index" — ACCEPT, and this is the right target.** Remark D.34.16c is
   the first statement in row D that localises the model-dependence to a **single fixed index**: for
   `Ξ_a` the tail is positive for the same unconditional reason as for `ξ`, and the violation of
   `(b′)_{B4_a}` sits at one `m` determined by `F_+`. The sharp phase-144 question is therefore:

   > **Which index, and what is the inequality there?** Identify (or bound) the smallest `m` at which
   > `(b′)_{B4_a}` fails for `Ξ_a`; write the corresponding `ξ`-inequality at that index
   > (`t_m(E) ≥ 0` for `R(E) > 0`, `\deg E > 0`, `m` fixed — a single inequality in the finitely many
   > data `a, b, (Φ_E(ρ))_ρ` and `m`); and decide whether *that* inequality is unconditional for `ξ`
   > while false for `Ξ_a`. The structural asymmetry is already named and is index-local: at any fixed
   > `n`, `ξ`'s **two** polar exponents give the AM–GM floor `2\sqrt{ab\,Φ_g(0)Φ_g(1)}`, uniform in
   > `n`, while `Ξ_a`'s **four** give no such floor (Theorem D.34.10's proof vs. §D.34.5 item 5).

   This is a bounded, checkable, falsifier-anchored question; it does not require the whole clause;
   and a negative answer (the index-`m` inequality is *also* RH-equivalent) would be informative,
   since it would show the clause does not decompose by index.

*Secondary, in order:* **H12/H13/H14** (cheap, this round's residue); **O-29** (the sparse cone
`\{t_{2^k} ≥ 0\}` — a formally weaker clause with the same transfer theorem, and the cheapest possible
enlargement of the target); **O-26** ((T2) on `B4^{g,0}`, needed to know the shape of the cone but
needed by no theorem); Horn A stays secondary and gated on `s_*^{\mathrm{cone}}` (O-19′) and O-18′.

*Not recommended:* any attempt on O-24 as a whole. It is RH, the round says so, and the round-2
localisation does not lower its difficulty — it only tells you where to stand.
