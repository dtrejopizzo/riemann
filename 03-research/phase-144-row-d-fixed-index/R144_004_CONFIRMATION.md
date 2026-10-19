# R144.004 — Confirmation, phase 144 (final round)

* Input: `R144_003_ROUND2.md`, the
repaired `R144_001_ROUND1.md`, `README.md`, `scripts/certify_failing_index.py`. Every repair
was checked **at its site in `R144_001`**, not in the ledger; §D.40 was audited as new material; the
script was re-run. Nothing was contested by the round, so the work here is verification, not
adjudication.*

**Overall verdict: CONFIRMED. All 12 findings (M1–M3, m1–m9) discharged at the statements they
touch. §D.40 is correct in its clauses and correctly labelled. No new positivity target inside the
frame is proposed. Row D label UNCHANGED — correct. Four MINOR residues (r1–r4), none blocking; the
the phase may be closed over them.**

---

## 1. Per-finding status (checked at site)

| finding | site checked | status |
|---|---|---|
| **M1** | `R144_001` D.37.3(iii),(iv) (ll. 191–219) | **DISCHARGED.** "entire" and "discrete exceptional set" are gone; `Ψ` is now asserted **continuous on `R`** with the real-`T` bound `|\cosh((½−ρ)T)| ≤ e^{θ|T|}` and `Σ|d_ρ| < ∞`, giving uniform convergence on compacta of `R` — which is exactly what the hypotheses support, and no more. The Laplace argument is retained on `[0,∞)` and still yields `Ψ ≢ 0`; the conclusion is now `\{Ψ ≠ 0\}` open and non-empty, minus a countable set. (iv) is an **existence** statement and says so in italics. Propagation verified at `§0` item 2, D.38 opening, D.39 ¶1, P46-45, `§Label` row, README bullet. The bracketed note states both halves of the error (the real-vs-complex `T` bound *and* the independent quantifier non-sequitur) accurately. |
| **M2 / m9** | D.38.1 (l. 300) + `§Label` | **DISCHARGED.** Label is now `INVENTORY`, clauses (i)–(iv) `PROVED` unconditional; "say **exactly**" and "one gets nothing more" are withdrawn in the bracketed note and absent from the statement. |
| **M3** | new Cor. D.38.5c (ll. 519–538), D.39(b), open list, P46-49, README | **DISCHARGED, and the proof is correct.** Re-derived independently: `Φ_K(ρ) = ξ(ρ) = 0` ⟹ `Φ_{E_t}(ρ) = tΦ_F(ρ)` ⟹ `W(E_t) = t²W_F = −t²q → −∞`, with `a = b = ½`, `\deg = 1` frozen and `R(E_t) = ½t²q > 0`; converse `Ψ ≡ 0` under RH. **O-30 ⟺ RH.** The open-list row is moved to CLOSED-negatively, D.39(b) is rewritten as a withdrawal, and O-30 is removed from the phase-145 recommendations. |
| **m1** | P46-43 | DISCHARGED — four sources now named, `R143_004` l. 237 included. |
| **m2** | P46-43 | DISCHARGED, and well done: it is now headed **PARTIAL RETRACTION**, retracting the polar-arity clause only and printing the surviving half (`|n^{½−(ρ±a)}| = n^{∓a}` unbounded + `W_a` indefinite) as the actual separator. |
| **m3** | D.37.2(ii) (ll. 70–80) | DISCHARGED — singleton `C_½` added, with the correct note that (i) is unaffected. |
| **m4** | D.37.1 preamble (ll. 124–132) | DISCHARGED — Prop. 12.4B's hypothesis is now checked, and the argument given (`Re(ρ−a) = Re(ρ+a)` impossible for `a ≠ 0`, so at most one member of each pair is on the line) is **valid and unconditional**. |
| **m5** | README run-block | DISCHARGED — the two-fold normalisation `Φ_{g_a}(1±a) = 1` is printed, the floor and AM–GM values are explicitly declared **not** `a`-invariants, and `α, β, \deg_aK_a` are correctly kept as invariants. |
| **m6** | D.38.2a (l. 374) | DISCHARGED — the evenness clause is added and the correct observation made (nothing uses evenness of `F` or `E`, only of `g`). |
| **m7** | D.38.5 (l. 483) | DISCHARGED — `C^{S_0}_F` widened to any real `F ∈ D^W`; (i) retains `\deg F = 0` where it is needed. |
| **m8** | P46-48, `§Label` D.38.4 row, README file table | DISCHARGED — the RH-conditionality of `64 = 64d²` is now printed in all three places. |
| **audit item 7** | Scope caveat after D.37.4 (l. 271) | DISCHARGED — (i)–(iii) are located as the separating step *of D.34.10's proof*; "and nowhere else" is not attached; cross-referenced from D.40.4. |

**Script re-run by me:** `--fast` → `RESULT: PASS`, exit `0`, 0.11 s; `--a 0.1`, `--a 0.45` → `PASS`.
No script change was needed and none was made; all quoted numbers still reproduce.

## 2. Verdict on §D.40 — **CORRECT, and correctly labelled.**

* **D.40.1 (final form).** Restatement D.38.3a, quantifiers correct (`g_λ` of Lemma D.34.9′ with the
  explicit `λ`-range), labelled `PROVED` + `RESTATEMENT` with the "not progress" sentence retained.
  **Accepted.**
* **D.40.2, table 1 (frozen vs unbounded).** Every row re-derived: `a = b = ½` (`F` primitive),
  `\deg = 1`, `I_∞(E_t,K) = ½\deg E_t = ½` (Thm 11.8(i)), `R = ½t²q > 0`, `W = −t²q`,
  `Σ|Φ_{E_t}(ρ)|² = t²Σ|Φ_F(ρ)|² → ∞` (finite and non-zero since `q > 0` ⟹ `F ∉ 𝓝_∞`),
  `|I_∞(E_t,F)|/\deg E_t = |t|q`. **All correct.** (See residue r3 on the `t_m` row.)
* **D.40.2, table 2 (six weakenings).** Each row traced to the statement it cites — D.38.3(i),
  P46-49/O-29, D.38.4(iii), D.38.5(i), D.38.5a, D.38.5c — and each of those was verified in
  `R144_002`. **All six hold.**
* **Lemma D.40.2.** The statement ("the ray exists iff RH is false") is **true**; `¬RH ⟹ ∃F` is
  Paper 45 Thm 10.4, and `∃F ⟹ ¬RH` because under RH `1−ρ = \barρ` gives
  `I_∞(F,F) = −W_F = −Σ_ρ|Φ_F(ρ)|² ≤ 0`. See residue r4: the round routes the converse through
  Thm 10.4's "consequently" clause and D.34.8's last step, which is valid but circuitous; the
  one-line reason should be printed instead.
* **D.40.3 (W1),(W2).** (W1) `W` is a `ρ ↔ 1−ρ` pairing, a norm iff `1−ρ = \barρ` for every zero;
  `R(E) > 0` bounds it from above only; no lower bound in the frame's invariants (D.38.5c).
  **Correct.** (W2) `|n^{½−ρ}| = n^{½−\mathrm{Re}ρ}`, equal to `1` for all `n ≥ 2` iff `Re ρ = ½`;
  the remark that `\inf_ρ Re ρ > 0` is a quasi-RH zero-free-strip statement is `R143_004` §5 and is
  correctly cited. **Correct.** The claim "two facts, and only two" matches D.34.10's repaired
  RH-use count of **two** (the third was discharged unconditionally by Lemma D.34.9′) — **verified
  against `R143_001` l. 594 ff.**
* **D.40.4 (the parting point).** Each of the five `Ξ_a`-verbatim items re-checked against its
  source ((T1′) = §D.34.5 item 2; D.34.8 = item 4; the eventual half = Remark D.34.16c; the polar
  floor and `\cosh` form = D.37.2, D.37.1(iv); degree/`R`-positivity = D.37.1(iii)). **All five are
  correct.** The parting point is stated correctly and with the m4 check inline. The label
  `PROVED` (as a reading of the cited theorems) with the cross-reference to the D.37.4 scope caveat
  is the right calibration — it does not claim there is no other separation.
* **D.40.5.** Closure, `SYNTHESIS`. **No new positivity target inside the frame is proposed** —
  verified by inspection of the open list (O-29, O-30 CLOSED; O-24 = RH; O-25, O-26, O-28, O-19′,
  O-18′ unchanged; O-31 low-value and not a positivity clause) and by grep for new `O-3x` items:
  **none opened.** Both of round 1's proposals are withdrawn at their sites.

## 3. Residue (MINOR, non-blocking)

* **r1.** The D.38 section opening (l. ~294) still reads *"The failing index for `Ξ_a` is `m = 1`
  (Theorem D.37.3)"* unqualified — the one place the M1 repair did not reach. Should read "`m = 1`
  for the test classes of D.37.3(iii)".
* **r2.** The README **file table** still describes the open list as "(O-30, O-31 new; O-29 closed)";
  the headline bullet above it is correct (O-29 **and** O-30 closed). Stale by one round.
* **r3.** Table 1's row `t_m(E_t)` *(any fixed `m`)* presumes `t_m(F) ≠ 0`, which holds only after
  Lemma D.38.2a's index-selection perturbation — i.e. `F` depends on `m`. So "one object refutes
  all six" is exact per row but not literally one `F` across rows 1–2; add "for `F` chosen at that
  `m` by Lemma D.38.2a". (A single `F` with `t_m(F) ≠ 0` for **all** `m` simultaneously is **not**
  proved anywhere and should not be implied: D.26.6 gives surjectivity onto `R^N` for each finite
  `N`, not a simultaneous statement.)
* **r4.** Lemma D.40.2's converse citation (see §2). Statement true; citation circuitous.

---

## 4. Concurrence with the synthesis §3–§4

**I concur with the ranking β then α, but on a weaker and more honest reason than the synthesis
gives, and with two conditions.** The synthesis justifies (β) as "decidable in one phase and
informative either way". Strictly, it is *not* symmetric: §1 of the same document already says the
frame "keeps the intersection theory of `C×C` and discards its linear systems", and on a curve over
`F_q` the linear systems are present and Riemann–Roch is a theorem, so the near-certain outcome of
(β) is that the frame defect theorem **fails** there — i.e. (β) will confirm what §1 already asserts
rather than decide something open. That is still worth one phase, but for the *other* reason: (β)'s
value is not the yes/no, it is that the comparison **names** the missing ingredient concretely (a
sections functor / an actual `h⁰` with a cone of effective divisors that is not a thin moment cone,
`s₁ < 1` being the exact numerical signature of its absence), and (α) cannot be scoped until that
name exists. So: **run β, but write its predicted answer into the blueprint in advance**, so the
phase cannot be scored as a success whatever it returns, and judge it solely on whether it names the
ingredient and locates `s₁ < 1` on the function-field side. **Condition two, and this is a
correctness point, not a preference: (α) as stated in §3 has its sign backwards and must be repaired
before it is scoped.** §3(α) asks for a pairing "whose positivity on `P^W` is provable and which
dominates `I_∞` there". With this corpus's convention `I_∞(F,F) = −W_F` on primitives, RH is
`W_F ≥ 0`, i.e. **`I_∞(F,F) ≤ 0`** on `P^W` (Thm D.34.8's conclusion; Paper 45 Thm 10.4). A
dominating `J ≥ I_∞` that is *positive* proves nothing; what is needed is `J ≥ I_∞` on `P^W` with
`J ≤ 0` provable — a dominating **non-positive** form. That is a five-line fix, not a phase, but
until it is made the "one untried square" is not well posed, and a phase opened on it would spend
its first round rediscovering the sign. Finally, one accuracy point for §2 of the synthesis: the
sentence "one ray … refutes every bidegree-function `h⁰`; every 2-homogeneous trace functional; the
effective clause `(b′)⁺`" over-unifies — those three were refuted in phases 140–142 by **cousins**
of the ray (`E_0 + tF` for D.24.7; the certified `53.119F_0 + 400K`, which is the ray at `d = 400`,
for D.31.10), not by the `d = 1` ray of §D.40. The six rows of D.40.2's table **are** one ray (per
index, r3); the earlier three are the same *family*. Say "one family, `tF + dK`" and the claim is
exact and still striking. With those three corrections I concur with §4 as written: close the
trace-cone route with D.38.3a as its final form, open phase 145 on (β), hold (α) for 146, and keep
(γ) recorded as frame-internal and expected to meet the same ray.
