# R142.004 — Confirmation, phase 142: repairs verified, §D.32 audited

`R142_001_ROUND1.md`, the rewritten `README.md`, and `R142_003_ROUND2.md` (§1 ledger and
**§D.32**, which phase 143 is to be built on). Sources re-read for this round: Paper 47 §§11.1–11.5,
§12.2–12.5, §13 (Thms 13.2, 13.5, 13.6, Def. 13.4, and §9.2's own ledger row for §13); `R141_001`
§D.26 (Def. D.26.2, Lemma D.26.3 (D.26.1)/(D.26.2), D.26.10(v)) and §D.30 (Thm D.30.5 with proof,
D.30.10 Proof 2); Paper 45 Thm 10.4 as quoted at Paper 47 (1.10). Numerics recomputed at `mp.dps = 30`.*

---

## 0. Headline

* **H1–H10: all ten repairs verified in place. No repair is cosmetic, none introduces a new error, and
  none weakens §§D.31.1–D.31.4.** Theorem D.31.12 continues to stand.
* **§D.32 is sound in its architecture and contains four defects**, one of which (J2) materially
  changes the phase-143 recommendation and one of which (J3) is a **new positive result** that the
  coordinator's brief had backwards.
* **Judgement on the phase-143 target: HORN B / B4, but not as §D.32 frames it** — and HORN A should be
  carried, not dropped, because one of its two blockers is smaller than the report states (J5).

---

## 1. Verification of H1–H10

| finding | claimed repair | verified? | auditor's note |
|---|---|---|---|
| **H1** | D.31.14(i),(ii) withdrawn as false with the `E = dK` counterexample printed; ray-restricted (i); existential (ii); (iv) reproved with the witness | **YES** (R142_001 L.416–460) | The withdrawal is explicit, the root cause is correctly named (`I_∞(dK,F) = ½d\deg F = 0`, so the `t = 0` ray is unconstrained), and (iv)'s new proof is correct: the witness has `\deg(K−E) = −399 < 0`, `E ∈ S_0∖S_0^{(★)}`, `R(E) = 10 > 0`. **Accepted.** The replacement phrase "thin **transversally to the canonical ray**" is the right one. |
| **H2** | completeness/polarity withdrawn; (★) kept as necessary, `𝓝_∞`-invariant, constant-optimal | **YES** (L.92–108) | The withdrawn sentence is quoted verbatim and the reason given is the one I gave (no topology; bipolar would describe `\overline{\mathrm{conv}}T(𝓔)`). Label moved to `CLAIM`, and I confirm by grep that the claim is **used nowhere**: D.31.10's proof invokes only D.31.2(ii)'s `≤` half. **Accepted.** |
| **H3** | Platt row corrected; a `"Malliavin"` grep row added marking BM as a corpus cross-reference; "support function" 3 | **YES** (L.614–620) | I re-ran all three greps: `"Malliavin"` → `phase-33-dbn/85`, `/82`; `"Platt"` → 21 files incl. papers 01/36/37; `"support function"` → 3. The report additionally takes the corpus doc's improvement (γ_ρ real unconditionally ⟹ no RH needed in the BM row), which is correct and is a genuine gain. **Accepted.** |
| **H4** | §D.31.0 box with the `m ≥ 2` computation, epistemic type, cheaper import; "given (X19)" on every headline | **YES** (L.62–70) | The box reproduces my computation correctly (`2s_1 = 1.9969 > 1.4142 = \sqrt2`). I spot-checked the `§Label` rows for D.31.9–D.31.12 and the README: all now carry "given (X19)". **Accepted.** |
| **H5** | README rewritten to lead with the frame defect | **YES** | The README now opens with "**This is a statement about the frame, not about `ζ`**" immediately under the theorem box, and closes the consequences with "nothing above is evidence about the zeros of `ζ`". **Accepted.** |
| **H6** | proof-of-record leakage bound replaced by the zero-list-free `L ≤ 5.46×10^{−91}`; script demoted to illustration | **YES** (L.224–236) | The displayed bound is mine and is correctly attributed; the dependence of the old computation on zero-list completeness to height ≈ 236 is disclosed. I re-verified `5.45833×10^{−91}` and re-confirmed the margin `G(1−s_1) = 5.78970×10^{−3}`. **Accepted.** |
| **H7** | four numeric/pointer defects | **YES** (L.218, 359, and the certified-instance line) | `t = 53.11911…` now appears alone (I re-verified `t = 53.1191142828422`); `e^{−3596.2}` replaces `e^{−1598}`; `≤` replaces `=` with the `|\sin(σ²γ_1/2)|` factor noted; the Thm 12.2 pointer is now "linearity of `\deg`, `\deg K = 1` (Thms 11.13(iv), 11.7)". **Accepted.** |
| **H8** | D.31.8 header split | **YES** (L.246) | Header now reads `PROVED ((i),(iii), unconditional); SKETCH ((ii))`. **Accepted.** |
| **H9** | "no classical criterion exists" → "none was found", `ASSESSMENT`, with the non-surveyed literature disclosed | **YES** | **Accepted.** |
| **H10** | quantifier stated; `dK` witnesses nothing | **YES** (L.460) | **Accepted.** |

**Verdict on §1 of `R142_003`: the ledger is honest and complete. No repair-round regressions.**

---

## 2. §D.32, audited in full

### Item (1) — the vacuous / survives tables

Checked entry by entry against the sources.

* **Paper 45 Theorem 10.4 — UNAFFECTED, confirmed.** As quoted at Paper 47 (1.10) it reads
  "`I_∞(F,F) ≤ 0` for every primitive `F ∈ C_c^∞` ⟹ RH"; it mentions no `h⁰`, no effectivity and no
  clause. D.31.12 removes a *supplier* of its hypothesis, not the theorem. Correctly placed in (B).
* **D.30.5 ((a),(c) for `h⁰_{RR}^{+}`) — still meaningful, confirmed, and it is the sharpest thing in
  table (B).** I re-read the proof: (c) holds because `\deg E + \deg(K−E) = \deg K = 1 > 0`, so **the
  two degree gates cannot both be off**, and no case uses `χ` or any sign. That is exactly why Horn A
  is worth trying — and, note, exactly why Horn A is hard: replacing the degree gate by the (★)-gate
  destroys the "cannot both be off" mechanism (both gates *are* off at the D.31.10 witness, which is
  D.31.14(iv)). Its placement is right; the *reason* it gives ("(a) and (c) are free, only
  (b′) failed") should carry this caveat, since the freeness of (c) is a property of the **degree**
  gate specifically. **MINOR, recorded as J5 below.**
* **Paper 47 §13 — "route vs theorem" is stated correctly, and it matches the paper's own ledger.**
  Paper 47 §9.2 already records Def. 13.4's `h⁰_{\mathbb Z}` as "`REFUTED` as a route on every finite
  truncation (Thm 13.6(ii)) and off `\{\deg>0\}` (Rem 13.5c); `PROVED` as structure (Thms 13.2, 13.5,
  Lemmas 13.5a, 13.5b); `OPEN` on the full lattice (item (23))". §D.32.1(A)'s row ("the *route*
  sentences are withdrawn; Thms 13.2, 13.5, 13.6 keep their labels as statements about their own
  objects") is a faithful restatement. **What the row should add, and does not:** D.31.12 now closes
  open items (22) and (23) of Paper 47 §14.5 **negatively as routes** — no functional of `H⁰` alone,
  on the full lattice or otherwise, can satisfy (a),(b′),(c), because *nothing* can. That is a strict
  gain in bookkeeping which §D.32.1 leaves on the table. **MINOR (J6).**
* All other rows of (A) and (B) check out: D.30.9–D.30.12 vacuously true and their targeting sentences
  withdrawn; O-18 closed negatively; D.30.13, D.30.16, D.24.6/7/9, D.26, D.27.4, Thms 11.x, 12.2,
  12.4, Lemma 12.4A, Prop. 12.4B all correctly in (B); the row-D "no label change" correct.

**Verdict (1): CORRECT, with two MINOR omissions (J5's caveat, J6's gain).**

### Item (2) — Restatement D.32.1 (the geometric half)

* **Hartshorne numbering — VERIFIED, all three.** GTM 52, Ch. V: **Theorem 1.6** is Riemann–Roch for
  surfaces (`ℓ(D) − s(D) + ℓ(K−D) = ½D.(D−K) + 1 + p_a`); **Lemma 1.8** is "`H` ample, `D.H > 0`,
  `D² > 0` ⟹ `nD` effective for `n ≫ 0`" (the lemma used in the proof of the Hodge index theorem);
  **Theorem 1.9** is the Hodge Index Theorem, which is the number Paper 47 Remark 12.3a already pins.
  Its bracketed "numbers to be re-verified in Part III" can be **discharged**: I verify them
  here. Lazarsfeld, *Positivity I*, Ergebnisse 48, §2.2 is indeed "Big line bundles and divisors" —
  the right pointer for the `big` formulation.
* **(i)'s inequality is correctly derived** (not merely quoted): `χ(D) = χ(𝒪) + ½D·(D−K)`,
  `h²(D) = h⁰(K−D)` by Serre duality, so `h⁰(D)+h⁰(K−D) = χ(D)+h¹(D) ≥ χ(D)`. ✔
* **"(i) transports with the geometric constant" — CORRECT.** `I_∞(E,E) ≤ 2ab ≤ (\deg E)²/2 =
  (\deg E)²/I_∞(2K,2K)` is `D² ≤ (D·H)²/H²` at `H = 2K` (`I_∞(2K,2K) = 4·½ = 2`; `\deg E = I_∞(E,2K)`
  by Thm 11.8(v)). The `2ab ≤ (a+b)²/2` step is AM–GM and needs no sign. ✔
* **"(ii) fails with deficit exactly `s(γ,θ)`" — CORRECT as a statement about the measured deficit, but
  the word "exactly" is doing two jobs.** What is proved: `s(γ,θ)` is the *exact* constant in
  Lemma D.31.4 (by D.31.2(i)), and `s_1 < 1` is *an* explicit deficit sufficient to refute the analogue
  of (ii). What is **not** proved: that `s_*` (the infimum over all test directions) is the exact
  measure of the total deficit — that is O-19, still open. The sentence should read "with an explicit
  deficit, `s(γ,θ) < 1` in the direction `θ` at the zero `γ`, where geometry has `1`". **MINOR (J7).**
* The "consistency remark" (no function-field model of `D^W`; recorded as O-23) is mine, correctly
  attributed as heuristic, and correctly **not** used as a check.

**Verdict (2): CORRECT; numbering discharged by me; one wording defect (J7).**

### Item (3) — HORN A

**The degree audit, done line by line as instructed.** Paper 47 Theorem 12.3's proof:

| step | class the clause is applied to | its degree | which clause |
|---|---|---|---|
| Step 1 | — (`H' := F + 2mK` is constructed; `m > C_F`) | `\deg H' = 2m` | none |
| Step 2 | `E = K − nF` | `\deg = 1` (`\deg F = 0`) | **(b′)** |
| Step 3 | `E = nF` | `\deg = 0` | **(c)**, at the instance indexed by `nF` |
| Step 4 | `E = nF` | `\deg = 0` | **(b′)** |

and `D.30.10` Proof 2 applies **(b′)⁺** at `E = rF + K`, `\deg = 1`.

**So: (c) is invoked exactly once, at an instance indexed by a class of degree `0`, whose partner
`K − nF` has degree `1`; (b′) is invoked at degrees `1` and `0`.** The coordinator's question —
"`E = rF+K` has degree 1, `K−E = −rF` has degree 0, which receives (c)?" — is about D.30.10 Proof 2,
which **uses no (c) at all**: it is a direct argument from (b′)⁺, ampleness and `\deg`. In Theorem
12.3, the (c)-instance is indexed by `nF` (degree 0); since (c) is symmetric in the pair
`\{E, K−E\}` via `R(K−E) = R(E)` (D.30.1), the same instance is equally the one indexed by `K−nF`
(degree 1). **This is why Definition D.32.2 must impose `Δ(0) = Δ(1) = 0` and `Δ(d) = Δ(1−d)`, and it
does.** ✔ **CONFIRMED.**

* **Prop. D.32.3(i) — CORRECT.** With `Δ(0) = 0`, Step 3 gives `h⁰(nF) + h⁰(K−nF) ≥ ½n²q + χ`
  unchanged; Steps 1, 2, 4 never touch (c). I also checked the *composite* run for `h⁰_★` end to end:
  `h⁰_★(nF) = 0` (degree gate), so (c′) forces `h⁰_★(K−nF) ≥ ½n²q > 0`, and (b′) at `K−nF` then
  contradicts ampleness exactly as in Step 2. **The machine still closes.** The audit's earlier fear —
  that a quadratic defect must destroy the `¼m²` growth — is **not** borne out, and I withdraw it: the
  growth is demanded at degree `0`, where `Δ` vanishes. Recorded as an accepted correction to
  `R142_002` §3.
* **Prop. D.32.3(ii) — CORRECT arithmetic, BACKWARDS WORDING (J8, MINOR).** The displayed
  `Δ(d) ≥ \tfrac{d²}4(1−s_*²) − \tfrac d4` is a **lower bound forced on `Δ`** (the largest `R` attained
  by witnesses outside `𝔐` at degree `d`, attained as `t²W_F ↓ s_*²d²/2`), i.e. the **minimum
  admissible defect**. Calling it "the strongest `Δ` that the family does not refute" inverts the
  order: larger `Δ` weakens (c′) and is equally unrefuted. I verified the extremal computation:
  `R = ½(d²/2 − s_*²d²/2) − d/4 = \tfrac{d²}4(1−s_*²) − \tfrac d4`. ✔
* **Prop. D.32.3(iii) — CORRECT.** At `E = dK`, `d > d_*`: both gates off, `R(dK) = \tfrac{d²}4 −
  \tfrac d4` and `Δ(d) = \tfrac{d²}4(1−s_*²) − \tfrac d4`, so (c′) demands `\tfrac{d²}4 ≤
  \tfrac{d²}4(1−s_*²)`, false unless `s_* = 0`. **The degree gate is dead.** ✔ (And the irony is
  correctly noted: H1's counterexample is what kills it.)
* **Prop. D.32.3(iv) — CORRECT IN SUBSTANCE, with one real gap and one missing case.**
  - **Gap (J1, MAJOR).** The Cauchy–Schwarz step "`|I_∞(E,F)| > C_F\deg E` ⟹ `W(E) > s_F²d²/2`"
    **drops the polar cross term**. For real `F` with `\deg F = 0` one has `Φ_F(0) = −Φ_F(1) =: η_F`
    and, by Thm 11.5, `I_∞(E,F) = η_F(a − b) − Σ_ρΦ_E(ρ)Φ_F(1−ρ)`, so the correct inequality is
    `|I_∞(E,F)| ≤ |η_F||a−b| + \sqrt{W(E)\,W(F)}`, and `W(F) = W_F − 2η_F²`. The conclusion follows
    only for `η_F = 0`, i.e. for **primitive** `F`. Note `F_0` itself is *not* primitive
    (`η = Φ_{F_0}(0) ≠ 0`, merely `< 10^{−390}`). **Repair, and it is free:** define `S_0^{(★)}` by the
    (★)-conditions at **primitive** `F` only (such `F` with `Φ_F(ρ_1) ≠ 0` exist — `F = Πg`, D.24.7),
    or carry the `η_F` term. **This does not touch §D.31:** D.31.10's refutation uses the *identity*
    (D.31.2), never Cauchy–Schwarz, and `I_∞(E,F_0) = −tW_{F_0}` is exact.
  - **Missing case, which I checked and which is fine (J9, MINOR).** (iv) treats only `\deg E > 1`. The
    remaining bands are covered by the same computation once one notices the corollary the report does
    not state: **under RH, `S_0 ∩ \{\deg ≤ d_*\} ⊆ S_0^{(★)}`** — because for `d ≤ d_* = (1−s_*²)^{−1}`
    the bound `R(E) < \tfrac{d²}4(1−s_*²) − \tfrac d4 ≤ 0` contradicts `E ∈ S_0`. With the symmetric
    `Δ` (`D = \max(d,1−d)`) the bands `\deg E ≤ 0` and `0 < \deg E ≤ 1` then close. **State the
    corollary: it also localises O-18′ entirely above degree `d_*`.**
  - "Under RH it also satisfies (a)" — (a) is `h⁰ ≥ 0`, true unconditionally by `\max(R,0) ≥ 0`. Stray
    hypothesis. **MINOR.**
* **The two tests, assessed.** (A3) "prove (c′) for `h⁰_★` unconditionally" and (A4)
  `S_0^{(★)} ⊆ 𝔐` (= O-18′). The report calls (A3) the sharper. **I disagree, and this is J5.**
  - **(A3) is smaller than advertised.** The only use of RH in (iv) is `W(E) ≥ 0` (to pass from
    `I_∞(E,E) = 2ab − W(E)` to `R(E) < Δ`) and the Cauchy–Schwarz on the zero sum. `W(E) ≥ 0` is
    *precisely* the Weil positivity being sought, so (A3) is **circular exactly where the programme is
    stuck** — but it is circular in a *named, single* place, and the rest of (iv) is unconditional.
    That makes (A3) a well-posed target ("remove `W ≥ 0` from the proof of (c′)"), not a vague one.
  - **(A4) is the real blocker, and §D.32 understates it.** `S_0^{(★)} ⊆ 𝔐` says that the **linear**
    necessary conditions are **sufficient** for membership in the moment cone. That is, verbatim, the
    sufficiency half of the moment problem that this very round's Q-B.2 surveyed and found **no
    criterion for**, and which Q-B.1(i) identifies as "the non-convexity gap between `𝔐` and its
    closed convex hull, plus the decay requirement" — a gap the round explicitly declines to estimate.
    O-18′ is O-18 restricted to a smaller set; it is *formally* easier, and there is **no evidence
    whatever that it is true**. §D.32's "which nothing refutes either" is correct and empty: nothing
    refutes it because nobody can compute `𝔐`.

**Verdict (3): the degree audit CONFIRMED; (i),(ii),(iii) correct ((ii) mis-worded); (iv) correct after
the primitivity repair J1 and with the `\deg ≤ d_*` corollary supplied; the ranking of the two tests is
wrong — (A4)/O-18′ is the blocker.**

### Item (4) — HORN B

* **Theorem D.32.4 — RE-DERIVED INDEPENDENTLY AND CONFIRMED.** With `s' := C'_{F_0}\sqrt{2/W_{F_0}}`,
  a witness `E = tF_0 + dK` violates (★)′ at `F_0` iff `tW_{F_0} > C'_{F_0}d`, i.e.
  `t²W_{F_0} > s'^2d²/2`, and lies in `S_χ` iff `t²W_{F_0} < d²/2 − d/2 + 2χ`; the two are compatible
  for some `d` iff `d²(1−s'^2) > d − 4χ` has a solution, i.e. **iff `s' < 1`, i.e. iff
  `C'_{F_0} < G`.** So `C'_{F_0} ≥ G` is necessary, and — a sharpening the report does not state and
  which matters — **`C'_{F_0} = G` already suffices to neutralise the entire `E_{t,d}` family**, since
  `\sup_{t,d} tW/d = \sqrt{W/2}\,\sup_d\sqrt{1−1/d} = G` is a supremum **not attained**. The test is
  therefore an inequality at the boundary, not a strict one. ✔ The two properties (T1),(T2) are indeed
  the only ones Theorem 12.3's proof uses of "effective" (Steps 2,4 use `\deg E' > 0`; Step 1 uses
  finiteness of the bounded-density constant) — I re-read the proof to confirm. ✔
* **A premise defect (J2a, MINOR).** D.32.4 is stated for `𝓔' ⊇ 𝓔`, but its proof never uses that
  inclusion — only (T1),(T2). Good (it makes the theorem stronger), but then the narrative
  "**enlarge** the class of effective representatives" is not what three of the five candidates do.
* **B1 (`G ⋆ G^∨`) — the refutation is CORRECT, and it is a failure of the cone, not of the test.**
  `Φ_{G⋆G^∨}(s) = Φ_G(s)Φ_G(1−s)`, so `\deg = 2Φ_G(0)Φ_G(1) = 0` for primitive `G`, while
  `G⋆G^∨ ≢ 0` whenever `G ≢ 0` (the transform is not identically zero). (T1) is the property Step 4's
  contradiction *is*, so a cone containing nonzero degree-`0` elements cannot serve, whatever the test
  says. **Additional, and decisive:** `B1 ⊉ 𝓔` — a nonnegative density need not be a square. The
  "witness inside?" column is also right (`Φ_{E'}(ρ) = |Φ_G(ρ)|² ≥ 0` under RH, while
  `Φ_E(ρ_1) = itG` is purely imaginary).
* **B2 — verdict right, one argument loose (J10, MINOR).** `\hat{E'} ≥ 0` ⟹ `E'` positive-definite ⟹
  `|E'(u)| ≤ E'(0)` (Bochner) ✔, and `\deg` is evaluated off the critical line, hence uncontrolled ✔,
  so (T1) fails. The added "(T2) fails because `∫|w_F|` diverges" is not an argument as written — `C'`
  is a sup of `|∫E'w_F|/\deg E'`, not `∫|w_F|`. Drop it; (T1) alone is fatal. Also `B2 ⊉ 𝓔`: `K ≥ 0`
  has `Φ_K(½+iτ) = Ξ(τ)`, which **changes sign** at every zero, so `K ∉ B2` — the cone excludes the
  canonical class, which is fatal on its own.
* **B3 — CORRECT.** The convex hull of `\{λτ_cK\}` lies **inside** `𝓔` (`τ_cK > 0`), so `C' ≤ C < G`
  and D.32.4 refutes it; it is D.30.13's zero-free family, which is why D.30.13 could realise only the
  zero-free locus.
* **B5 — CORRECT ("closure cannot raise a supremum"), with a caveat worth printing.** If `I_∞(·,X)`
  and `\deg` are continuous for the topology, the sup over `\overline{𝓔}` equals the sup over `𝓔`
  (each closure point's value is a limit of values). **Caveat:** the only way a closure could raise it
  is along sequences with `\deg E'_k → 0` and `I_∞` bounded away from `0` — and such a limit point
  violates (T1). So the closure route dies either way. ✔
* **B4 — THE SOLE SURVIVOR: three findings, one of them new mathematics.**
  - **J2 (MAJOR): B4 as literally defined fails (T1) at once, and does not contain `𝓔`.**
    (a) `t_n(N) = 0 ≥ 0` for every `N ∈ 𝓝_∞` (R141_001 L.186), so `𝓝_∞ ⊆ B4` and B4 contains nonzero
    classes of degree `0`: **(T1) is false as stated**. The repair is forced and natural — (b′)
    quantifies modulo `𝓝_∞`, so (T1) must read "`\deg E' > 0` for every `E' ∈ 𝓔' ∖ 𝓝_∞`" — but the
    report states neither the defect nor the repair.
    (b) **`𝓔 ⊄ B4` is not proved and is probably false.** D.26.10(v) gives only
    `t_n(E') = \mathrm{PRIME}(h_n) − \mathrm{ARCH}(h_n) ≥ −\mathrm{ARCH}(h_n)` for `E' ≥ 0` — a
    *one-sided bound with an archimedean term of the same order*, which is exactly row N7's finding
    that no sign is extractable. There is no reason for `t_n(E') ≥ 0` on all of `𝓔` (equivalently, for
    `w_g ≥ 0` pointwise, which would make every translate `τ_cg` nef — false in general, since Thm
    11.14(iii) needs `m > C_g` to make `g + 2mK` ample). **So B4 is not an enlargement of the effective
    cone at all; it is a different cone.** That does not break D.32.4 (whose proof ignores the
    inclusion) but it breaks the *narrative* of Horn B and, more seriously, it means (b′) with respect
    to B4 is **not** a weakening of (b′): a class effective in the old sense need not be in B4.
  - **J3 (NEW RESULT, and it reverses the coordinator's premise): the D.31.10 witness lies in B4 —
    every witness of the family does — and this is exactly why B4 passes the D.32.4 test.**
    *Proof.* `g` is Baire-selected, so `t_n` cannot be computed numerically; it can be **bounded
    exactly, uniformly in the admissible `g`**. By (D.26.1) with `E = tF_0 + dK`:
    `t_n(E) = \tfrac d2\big(n^{½}Φ_g(1) + n^{−½}Φ_g(0)\big) + tη\big(n^{½}Φ_g(1) − n^{−½}Φ_g(0)\big)
    − t\,Σ_ρ Φ_{F_0}(ρ)Φ_g(1−ρ)n^{½−ρ}`. The `ρ_1,\barρ_1` terms contribute
    `2tG·\mathrm{Im}[Φ_g(1−ρ_1)n^{−iγ_1}]`, of modulus `≤ 2tG|Φ_g(ρ_1)|` since `|n^{½−ρ_1}| = 1`; the
    others are `≤ t\,n^{½}\sup_ρ|Φ_g|·L = O(10^{−90})`, and the `η`-terms are `O(10^{−390})`. By AM–GM,
    `\tfrac d2(n^{½}Φ_g(1)+n^{−½}Φ_g(0)) ≥ d\sqrt{Φ_g(0)Φ_g(1)}`, and by **Lemma D.24.6 applied to
    `g ≥ 0`**, `|Φ_g(ρ_1)| ≤ \sqrt{Φ_g(0)Φ_g(1)}`. Hence
    `t_n(E) ≥ (d − 2tG)\sqrt{Φ_g(0)Φ_g(1)} − O(10^{−89})`, and `d − 2tG = 400 − 399.449621354 =
    0.5504 > 0`. **So `t_n(E) > 0` for every `n ≥ 1` and every admissible `g`.** ∎
    The margin is not an accident: `d − 2tG > 0` **is** the statement that the witness satisfies the old
    non-sharp bound `|Φ_E(ρ_1)| < \sqrt{ab} = d/2` — which D.31 proved it does, strictly. Along the
    whole family (`t²W ↑ d²/2 − d/2`) the margin is `d − 2\sqrt{d²/4 − d/4} → \tfrac12 > 0`; I computed
    it at `d = 400, 10³, 10⁶`: `0.50031, 0.50013, 0.50000`. **The entire `E_{t,d}` family is
    trace-positive.** Consequently `C'_{F_0}(B4) ≥ \sup_d tW/d = G` (I computed `tW/d = 3.754769`
    at `d = 400`, `3.755240`, `3.758062`, `3.759941` along the family, `↑ G = 3.759942`), so
    **B4 passes the D.32.4 test — with equality, which by the sharpening above is enough.**
    *The coordinator's premise ("if the witness is in B4 the horn fails immediately") is backwards:*
    the witness being in B4 is precisely the reason B4 is not refuted. And the mechanism is
    structurally meaningful: **trace-positivity's natural modulus bound is `\sqrt{ab}` — the non-sharp
    constant that the `R > 0` gate was calibrated against (Cor. D.30.8) — so B4 is the cone for which
    the calibration is exact after all.** That is the best sentence in phase 142 and it is not in
    `R142_003`.
  - **J4 (ASSESSMENT): where B4 will actually be decided is (T1), not (T2), and the sub-question is
    sharp.** (T2): trace-positivity constrains `E'` only against the kernel `w_g(·−\log n)` at the
    discrete points `\log n`, and `|Φ_g(ρ)| = O(|γ_ρ|^{−2})` by (11.2), so a direction `F` with `Φ_F`
    concentrated at a **high** zero `ρ_j` is barely constrained: repeating the computation above with
    `F_j(u) = e^{−u²/18}\sin(γ_ju)` gives trace-positivity for `t` as large as
    `≈ d\sqrt{Φ_g(0)Φ_g(1)}/(2G|Φ_g(ρ_j)|)`, hence `C'_{F_j} ≈ G\sqrt{Φ_g(0)Φ_g(1)}/|Φ_g(ρ_j)|` —
    **finite for each fixed `j`, but growing like `γ_j²`.** So (T2) plausibly **holds** pointwise in `X`
    (which is all Step 1 needs) while `C'` is enormous. (T1) is then the whole question:
    **is there `F ∉ 𝓝_∞` with `\deg F = 0` and `t_n(F) ≥ 0` for every `n ≥ 1`?** For primitive `F`,
    `t_n(F) = −Σ_ρΦ_F(ρ)Φ_g(1−ρ)n^{½−ρ}` is (under RH) a sampled almost-periodic function of `\log n`
    with zero mean value; nonnegativity at every sample would force it to vanish, i.e. `F ∈ 𝓝_∞` by
    Thm D.26.5 — **if** the sampling at `\{\log n\}` can be shown to detect the mean. That is a clean,
    zero-free, decidable question and it is the right shape for phase 143. Note it is **not**
    automatically favourable: if such an `F` exists, B4 dies instantly.
* **§D.32(iii)'s claim that B4 is "the sole survivor and the only candidate that reads A8" — the first
  half is CORRECT (B1,B2,B3,B5 die, as re-checked above); the second half is CORRECT but weaker than
  it sounds.** B4 reads A4/A8 only through D.26.10(v)'s one-sided bound, which row N7 already found
  yields nothing beyond (★). So "reads A8" means "is the only candidate *whose definition* mentions the
  prime side", not "extracts arithmetic content". With J2(b) in hand, the honest summary is: **B4 is the
  only candidate not refuted, it is not an enlargement of `𝓔`, it passes the D.32.4 test because it
  contains the witnesses, and it now needs (T1).**

**Verdict (4): Theorem D.32.4 CORRECT and re-derived (plus a sharpening: equality suffices); B1, B2,
B3, B5 correctly disposed of (two loose arguments, J10); B4's status materially mis-stated — J2 (MAJOR)
and J3 (new, favourable) both change it.**

### Item (5) — the overall claim of §D.32(iii)

Accepted with the amendments of J2/J3/J4. The candidate table is the right instrument and four of five
rows are right. The fifth row's "(T1) is also unproved" is too mild: **(T1) is false as literally
stated** (J2a) and, in its repaired form (mod `𝓝_∞`), is the single question on which the horn turns.

---

## 3. Judgement on the phase-143 target

**Recommendation: open phase 143 on HORN B / B4, with HORN A carried as the secondary line. Do not run
them as equals, and do not run Horn A first.**

*Why B4 first.*
1. **It has a decidable, zero-free, self-contained first question** — (T1) mod `𝓝_∞`: is there a
   primitive `F ∉ 𝓝_∞` with `t_n(F) ≥ 0` for all `n`? A **yes** kills the horn in one line; a **no**
   is a real theorem about `D^W` and hands Theorem 12.3 a satisfiable-looking clause. Either way phase
   143 ends with a result. That is not true of Horn A.
2. **It already passes the only test §D.32 could devise** (J3), and passes it for a structural reason
   (`\sqrt{ab}` is trace-positivity's natural bound), not by luck.
3. **It is where T2's demand is met.** Every previous row-D candidate was model-uniform; B4's
   definition mentions the prime side. Restatement 12.4a's schema is satisfied only by a candidate that
   reads a datum `Ξ_a` lacks, and B4 is the only one on the table.

*Why Horn A is secondary but must not be dropped.*
* Its blocker is **(A4)/O-18′**, not (A3) — and (A4) is the sufficiency half of the moment problem,
  which this phase's own Q-B.2 found no criterion for and Q-B.1(i) identifies as an unestimated gap.
  Betting phase 143 on it would be betting on the hardest open problem in the row, restated.
* But (A3) is a *small, named* circularity (the only use of RH in D.32.3(iv) is `W(E) ≥ 0` plus a
  Cauchy–Schwarz), and J9's corollary **`S_0 ∩ \{\deg ≤ d_*\} ⊆ S_0^{(★)}` under RH** localises
  O-18′ entirely above degree `d_*`. Those two facts make Horn A a cheap side-line: a bounded amount of
  work could turn it into either a clean conditional theorem or a second obstruction.
* **Before either horn: settle O-19 (`s_*`).** Both horns are stated in terms of `s_*`: Horn A's `Δ` is
  defined by it, Horn B's boundary case is `s_* = s_1`-vs-smaller. `s_* = 0` would make Horn A's `Δ`
  swallow all of `R` (and D.32.3(iii) shows the degree gate then survives), which is a *third* outcome
  neither horn anticipates. O-19 is cheap relative to both and gates both.

**Ranking for the phase-143 blueprint:** (1) (T1) for B4, mod `𝓝_∞`; (2) O-19; (3) Horn A's (A3) with
the primitivity repair J1 and the J9 corollary; (4) O-18′ only if (1)–(3) all resolve favourably.

---

## 4. Overall verdict and residue

**The repair round is accepted in full. §D.32 is accepted with four defects to fix (J1, J2, J7, J8) and
two additions to make (J3, J9).** Nothing found in this round touches Theorem D.31.12, which stands as
`PROVED` given (X19); nothing found touches §§D.31.1–D.31.4. **Row D: no label change** — concur, a
third time.

**Findings, by severity.**

| # | severity | statement | touches D.31.12? |
|---|---|---|---|
| **J1** | **MAJOR** | Prop. D.32.3(iv)'s Cauchy–Schwarz drops the polar term `η_F(a−b)`; valid only for **primitive** `F` (and `F_0` is *not* primitive). Repair: gate by primitive test classes, or carry `η_F`. §D.31 unaffected (it uses the identity (D.31.2), not Cauchy–Schwarz) | no |
| **J2** | **MAJOR** | B4 contains `𝓝_∞`, so **(T1) is false as literally stated** (repair: mod `𝓝_∞`); and `𝓔 ⊄ B4` is unproved and probably false (D.26.10(v) gives only `t_n ≥ −\mathrm{ARCH}`), so B4 is **not** an enlargement of the effective cone | no |
| **J3** | **MAJOR (favourable, new)** | The D.31.10 witness — indeed the whole `E_{t,d}` family — **lies in B4**, with `t_n(E) ≥ (d−2tG)\sqrt{Φ_g(0)Φ_g(1)} > 0` uniformly in the Baire-chosen `g`, because `2tG < d` is the old `\sqrt{ab}` bound. Hence `C'_{F_0}(B4) ≥ G` and **B4 passes the D.32.4 test, with equality (which suffices)**. The coordinator's premise is reversed | no |
| **J4** | ASSESSMENT | B4 will be decided by **(T1)**, not (T2): (T2) plausibly holds pointwise with constants `≍ γ_j²`; (T1) reduces to "does `t_n(F) ≥ 0 ∀n` force `F ∈ 𝓝_∞` for primitive `F`?" | no |
| **J5** | MINOR | §D.32.1(B)'s reason for D.30.5 ("(a),(c) are free") must carry the caveat that (c)'s freeness is a property of the **degree** gate (`\deg E + \deg(K−E) = 1 > 0`, "the two gates cannot both be off"), which the (★)-gate destroys; and (A3)/(A4) are ranked the wrong way round | no |
| **J6** | MINOR | §D.32.1 does not record the gain: D.31.12 closes Paper 47 §14.5 items (22),(23) **negatively as routes** | no |
| **J7** | MINOR | "deficit **exactly** `s(γ,θ)`" conflates the exactness of the constant in Lemma D.31.4 (proved) with exactness of the total deficit (that is `s_*`, O-19, open) | no |
| **J8** | MINOR | D.32.3(ii)'s "strongest `Δ`" is backwards — the display is the **minimum** admissible defect | no |
| **J9** | MINOR (addition) | D.32.3(iv) treats only `\deg E > 1`; the other bands close once one states the corollary **`S_0 ∩ \{\deg ≤ d_*\} ⊆ S_0^{(★)}` under RH**, which also localises O-18′ above `d_*`. Also "under RH it satisfies (a)" — (a) is unconditional | no |
| **J10** | MINOR | B2's "(T2) fails because `∫|w_F|` diverges" is not an argument (`C'` is a sup of ratios, not an `L¹` norm); (T1) alone suffices, and `K ∉ B2` (`Ξ(τ)` changes sign) is the cleaner kill. B5's caveat (`\deg → 0` sequences) should be printed | no |

**Residue carried out of phase 142.**
* `R12` discharged (round 1). **O-18 closed negatively** (round 1, confirmed).
* **O-18′, O-19, O-22, O-22′, O-23** are correctly posed; O-22′ should be re-posed as **(T1) mod
  `𝓝_∞` for B4** with J3 recorded as its standing positive datum, and O-19 promoted to a gate on both
  horns.
* **Unaudited by me, flagged as residue:** (a) `s_* > 0` versus `s_* = 0` — the "quiet window"
  heuristic in O-19 is not assessed here and is the one place where an unexamined intuition is steering
  two horns; (b) whether `\mathrm{ARCH}(h_n)` admits a sign that would put `𝓔` inside B4 after all
  (this would repair J2(b) and is worth one round's work — it is row N7/O-20 in a usable form);
  (c) the Kreĭn–Langer / truncated Nevanlinna–Pick literature that Q-B.2 discloses it did not survey,
  which is where a sufficiency criterion for O-18′ would have to come from if one exists.

**No FATAL findings in either round of phase 142.**
