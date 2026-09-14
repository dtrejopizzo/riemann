# R130.004 — builder round 2 (phase 130): disposal of every finding

Author: builder (Opus 5). Date: 2026-09-12.
Inputs: `R130_002_AUDIT_ROUND1.md` (hostile, F1–F20) and
`R130_003_LEAD_AUDIT_ROUND1.md` (lead, F1–F6).
Target: `04-papers/43-row-a-torsion-theory/main.md` (32 passages marked
`[REBUILT, phase 130, round 2]`).  Every repair carries a complete proof.

---

## 1. Hostile audit `R130.002`

| # | sev | disposal |
|---|---|---|
| **F1** | FATAL | **REPAIRED.**  The norm is redefined, Def. 8A.7b0: `‖F‖_tr := Λ(F) + N(F)` with `Λ(F) = ∫|F|(|w|^{1/2}+|w|^{−1/2})d^*w`.  Submultiplicativity is **re-proved with constant 1** (Thm. 8A.7b(a)): `|w|^{±1/2}` are multiplicative characters, so each weighted `L¹` norm is submultiplicative, `Λ(F⋆G) ≤ Λ(F)Λ(G)`, and `N(F⋆G) ≤ ½Λ(G)N(F)`, giving `‖F⋆G‖_tr ≤ Λ(G)‖F‖_tr ≤ ‖F‖_tr‖G‖_tr`.  New **Thm. 8A.7b(a′)**: `|λ_∓(F)| ≤ Λ(F) ≤ ‖F‖_tr` by AM–GM, so `M` extends to a continuous unital `†`-algebra map `𝓐_tr → B_T` of norm `≤ 1`.  Thm. 10.7(b) restated: **both** components of `λ_RR` are defined and continuous on `𝓐_tr×𝓐_tr`.  Rem. 8A.7b0a records the auditor's counterexample and why it no longer applies (`‖F_n‖_tr ≥ λ_+(F_n) = 1`). |
| **F2** | MAJOR | **REPAIRED, by the auditor's route (i)+(ii).**  Def. 9.14c0 defines *admissible approximations* (`M(F_α)→e_±`, `‖F_α‖_{L¹}→0`) and *`N`-bounded* nets.  Thm. 9.14c′ proves `I_A(F_α,G_β) → 0` uniformly in the partner index for **every** such pair, not just the `ψ`-family, and proves the `ψ`-family is admissible and `N`-bounded.  Rem. 9.14c″ states plainly that no continuous extension of `I_A` to `N_A^{dist}×N_A^{dist}` is claimed, and that Def. 10.6c's value on `σ(B_T)` is a **definition** whose consistency is Thm. 9.14c′.  Thm. 10.8 is restated along the admissible class. |
| **F3** | MAJOR | **ACCEPTED IN FULL.**  New paragraph "What A.8's closure actually consists of" (§10.3.3) lists the five statements and says in the auditor's own words that Thm. 10.7(e)'s second slot is definitional and (10.10) is bi-additivity.  Thm. 10.7(e) carries an inline marker saying the same.  The clause verdict is changed to **`PROVED WITH TARGET Pic_b(B_T)`**, my judgement is stated as a judgement, and the auditor's dissent (both the §4 row and the §3 renaming paragraph) is reproduced **verbatim** with my response. |
| **F4** | MAJOR | **REPAIRED and DOWNGRADED.**  Thm. 8A.9(a) now states the non-unit weight as the half-density–Lefschetz factor `w_p(σ) = |σ|^{1/2}·(1/|1−σ|_p) = τ_p(σ)` (8A.23a), with the rank `1`; (8A.24) becomes `T(F) = Σ_v ∫' F·rk^{Haar}·w_v d^*x` with the split (8A.24′).  Rem. 8A.9a separates the two regimes: **theorem** at the unit shells, **declared normalization** at the non-unit shells.  The ledger line for O-A5-5 now reads "CLOSED in the exact form (8A.24)–(8A.24′) … and in no stronger form". |
| **F5** | MAJOR | **REPAIRED.**  Thm. 10.6a's *Consequence* now states its hypothesis: it kills exactly the functors **factoring through the Tate fibre**; read otherwise, (A.8-I) "is not addressed here, and I do not claim it is impossible".  §13.8 item 7 and the §14.0 ledger row are corrected. |
| **F6** | MAJOR | **ACCEPTED; the inference is DELETED.**  §14.1 item 4 now says only: inside the window the forms agree exactly; outside, the comparison is known only on the positive cone, where the correction is **non-negative**, so adding places makes the form *more* positive.  §13.8 item 10 records the withdrawal. |
| **F7** | MAJOR | **REPAIRED.**  New §14.0a names the carrier once: a fixed finite chart `S`, with the chart system and colimit as *additional structure*; it lists which clause is discharged where, and states that `𝓝_∞^W = 0` is not claimed.  Thm. 3.8(e) is corrected: the colimit carries `T_∞`, `I_∞`, `M` and — with the **vector** radical `𝓝_∞^W` — the sequence (3.10), which **no clause uses**; the per-chart (9.17) is where A.6–A.8 are proved. |
| **F8** | MAJOR | **REPAIRED by construction, not by relabeling.**  New **Thm. 8A.12**: `E_H := λ(H)` for `H ∈ 𝓐_tr` (regular representation, bounded, multiplicative, `†`-compatible, injective); `F ↦ E_F` extends `‖·‖_tr`-continuously and injectively; `Corr_A^{tr,𝓐}` is the category of presented complexes over `𝓐_tr`, all of §8A holds on it verbatim, and it is closed under `‖·‖_tr`-limits.  Rem. 8A.12a: `N_A^{dist}` is a numerical module and indexes **no** objects, so the *declared* completion is the analytic one.  A.2 stays `PROVED`, now on evidence. |
| **F9** | MAJOR | **REPAIRED, both halves.**  §9.3.6's sentence is rewritten: what (O-A6-2) closes is that the **vector** radical of the completion against the test sector is zero; the **scalar** radical is two-dimensional (Thm. 9.14c) — different pairings, no contradiction.  The identification with P123.007 (4.2) is **downgraded to an analogy** in Thm. 9.14c's title and statement, Rem. 9.14d(3), Rem. 10.8a(3) and the §14.0 ledger, with the reason (P123.007's radical is taken against a different completion on which `I_A` is not defined here). |
| F10 | MINOR | **ACCEPTED.**  Thm. 8A.7b(a) now claims only an **inclusion** `𝓐_tr ⊆ {H ∈ L¹ : Λ(H)+N(H) < ∞}`, with a Fatou argument; density is not claimed. |
| F11 | MINOR | **ACCEPTED; reason (iii) WITHDRAWN** (Def. 8A.7d, §13.8 item 8).  Only (i) declared parameter and (ii) chart-independence survive; a new (iv) records that declaring `c` declares the signature. |
| F12 | MINOR | **ACCEPTED.**  Both occurrences now read "no **chart-independent** normalization", with the note that `T̂ ↦ T̂/(|S_f|+1)` is a normalization that moves with `S`. |
| F13 | MINOR | **ACCEPTED.**  (8A.13) is marked **superseded in place** by (8A.13′); Thm. 10.5's marker now says parts (ii)–(vi) stand and **part (i) does not**, existence/convergence being Thm. 8A.7b instead. |
| F14 | MINOR | **ACCEPTED** (= lead F2).  Thm. 10.9(c)'s `I²` step is rewritten with the unitization carried: symbol `(a1+F)^∧ = a + \hat F`, `∂_±(a1+F) = ∂_±F`, and `∂_±(XY) = \hat X(±i/2)∂_±Y + \hat Y(±i/2)∂_±X = 0`. |
| F15 | MINOR | **ACCEPTED.**  §11bis item 5(iii) now says the three ingredients live in three different objects (`G`, `Corr_A^{tr}`, `N_A^{dist}`), that `Δ` is not trace class (Rem. 8.11), and that no claim is made that all three sit in one. |
| F16 | NOTE | **ACCEPTED.**  §8A.4's determinant bullet is rephrased: `Det_S^{rel} := \exp T` makes "compatibility" definitional; the content is completeness of the norm, existence of the germ for every `F ∈ 𝓐_tr`, and exact multiplicativity.  The target bullet records that A.5 in fact uses only `Pic_b(C)` and that the enlargement is A.8's. |
| F17 | NOTE | **ACCEPTED.**  Thm. 10.7(a)'s `†`-chain replaced by the one-liner `(F^†)^∧ = \overline{F̂}`, `T̂+c` real ⟹ `I_A(F^†,G^†) = \overline{I_A(F,G)}`. |
| F18 | NOTE | **RECORDED, no change.**  I agree that A.7's discharge is a thin reading of a thin clause; §14.0b now says so in the A.7 line and points at Rem. 10.3d as the place a reader may reasonably disagree. |
| F19 | NOTE | **ACCEPTED** (= lead F5).  Rem. 9.7c(1) now states that the universal-residue narrative is about the **even** component `𝔠_0`; the odd component has **no** Tate pole (poles of `ψ(¾+iτ/2)` at `i(2n+3/2)`), consistent with `λ_±` and the rulings living on `𝔠_0`. |
| F20 | NOTE | **ENDORSED.**  A.1's reading note is kept and is repeated in §14.0a and §14.0b. |

## 2. Lead audit `R130.003`

| # | disposal |
|---|---|
| **F1** | **REPAIRED** — same edit as hostile F4; (8A.23a) now writes `τ_p = |σ|^{1/2}·(1/|1−σ|_p)` as half-density × Lefschetz weight, with Lemma 8.4 and Appendix D.2 cited for the negative-valuation shells. |
| **F2** | **REPAIRED** — same edit as hostile F14. |
| **F3** | **DONE** — the one sentence asked for is the paragraph "What A.8's closure actually consists of" (§10.3.3), plus the inline marker in Thm. 10.7(e). |
| **F4** | **NEW THEOREM 10.8b WRITTEN, label `CLASSICAL`.**  Full proof in four steps: (0) `G_m^† = F_m`, profiles convolve, `φ_{n,m} = ψ_n*ψ_m` is a probability density on `[(n+m)a,(n+m)b]` with `∫|φ'_{n,m}| ≤ ‖ψ'‖_1/\max(n,m)`; (1) `Σ_p W_p(F_n⋆F_m) = Σ_N (Λ(N)/N)φ_{n,m}(\log N)`, a **finite** sum; (2) Riemann–Stieltjes partial summation against Mertens `A(x) = \log x + E(x)`, `|E| ≤ C_0`, giving `1 + O(\max(n,m)^{−1})` — hence uniformity in the order of limits and independence of `ψ`; (3) `|W_∞| ≤ (1−e^{−2a})^{−1}e^{−(n+m)a}`; (4) the self-pairing `I_∞(F_n,F_n) = O(n^{−1}e^{−na}·n)` → 0, with the two-sided bound (10.19) and a second use of Mertens to sum the finite places.  Rem. 10.8c states the four things the lead asked for: it is the PNT in Mertens' form; it is `CLASSICAL` **import `M`**, quarantined, used by no clause, deleting it changes no verdict; it does **not** repair the finite chart (Thm. 10.8 stands, and the vector-valuedness at finite `S` is the finite-chart shadow of the global scalar hyperbolic pairing); it is what row A hands to row C, and it says nothing about `𝓝_∞^W`.  Cross-referenced in §14.1 item 5 and §14.0's ledger.  The lead's `scripts/mertens_check.py` reproduces `1.0000` for three bumps; I re-ran it. |
| **F5** | **ACCEPTED** — see hostile F19. |
| **F6** | **RECORDED.**  The renaming test is the auditor's to certify; §14.0b states that round 1 passed A.2–A.7 and failed A.8 "as currently written", that the restatement it asked for is now in the paper, and that whether this converts the FAIL is the auditor's call and not mine. |

## 3. Verdict changes relative to round 1

* **A.2**: evidence replaced by a construction (Thm. 8A.12); verdict stays `PROVED`, now earned.
* **A.5**: verdict stays `PROVED`; **O-A5-5's disposal is downgraded** to "(8A.24)–(8A.24′), and in no stronger form", and reason (iii) of `c := 0` is withdrawn.
* **A.8**: verdict changed from `PROVED` to **`PROVED WITH TARGET Pic_b(B_T)`**, with the content of the closure listed explicitly and the auditor's dissent reproduced verbatim.
* **Carrier**: named once, §14.0a — a fixed finite chart, chart system as additional structure.
* **Label**: `WEIL-STRENGTH-COMPLETE` is **not** self-granted and is not claimed.  The round-1 audit did not grant it; the closure rule reserves it to the audit; I record what was repaired and leave the grade where the specification puts it.

## 4. Nothing was relabelled to earn a label

Two verdicts moved **down** (O-A5-5's disposal, A.8's qualification) and none moved up.  A.2's `PROVED` is retained only because the missing objects were constructed.  The three residual items of round 1 are unchanged and still listed: A.1's reading, `c_{cut}`, non-invertible objects; to which round 2 adds two more, both now explicit in the ledger: net-independence of `I_A` on the completion (not claimed) and `𝓝_∞^W = 0` (not claimed).
