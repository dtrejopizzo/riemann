# R141.004 — Hostile confirmation, phase 141

*Auditor: Claude Opus 5 (hostile), same auditor as `R141_002`. Date 2026-09-13. Objects: the repair
ledger `R141_003_BUILDER_ROUND2.md`, the repaired `R141_001_BUILDER_ROUND1.md` (1504 lines, round-2
notes in place), the new **§D.30** (lines 906–1309), and `README.md`. Every claim of §D.30 was
re-derived from Paper 46's normalization before being accepted; the witnesses of D.30.7 and D.30.13
were recomputed from `M(τ_cK) = ½(e^{c/2},e^{−c/2})` (Thm 11.8(iii)); the convexity of `S_0` was
re-proved from scratch, and the builder's proof of it does not survive.*

---

## 0. Verdict

**CONFIRMED, with two MAJOR corrections inside §D.30 (neither of which changes a conclusion) and one
MAJOR completion of the diagnosis (which changes what phase 142 must do).**

* All 14 findings H1–H14 are **CLOSED**, verified against the files, none contested, none cosmetically
  discharged. Three of them (H1, H2/H5, H6) genuinely changed the round's conclusions, and the round
  says so.
* §D.30's core is **correct and important**: D.30.1, D.30.3, D.30.5, D.30.7, D.30.10 (both proofs),
  D.30.11, D.30.13, D.30.15, D.30.16 all verified line by line.
* Two statements in §D.30 are wrong as written: **D.30.14(i) misidentifies `S_0`** (C5 — the theorem is
  nevertheless true; corrected proof supplied below) and **D.30.14(ii) is labelled `PROVED` on a
  sketch** (C6).
* The diagnosis of O-18 is **incomplete on the necessary side** (C4): Theorem 11.14(ii) supplies an
  explicit, unconditional, checkable family of necessary conditions that D.30.6(i) does not consider —
  the very family that refutes `Ξ_a` and that drives Proof 2 of D.30.10. This is the first place a
  counterexample to O-18 could live, and it is the concrete attack for phase 142.

| new findings | count |
|---|---|
| FATAL | 0 |
| MAJOR | 3 (C4, C5, C6) |
| MINOR | 7 (C1, C2, C3, C7, C8, C9, C10) |

| item | verdict |
|---|---|
| **D.26** | **CONFIRMED.** H7/H8/H10/H11/H14 repairs in place; labels now match what is proved. |
| **D.27** | **CONFIRMED.** H1/H2/H5/H13 repairs in place; D.27.4 relabelled `RESTATEMENT` with the trace-free two-line proof printed; the FATAL screen now says only what is true. |
| **D.28** | **CONFIRMED.** H4 repaired exactly as prescribed (order-2 `Π`; Paper 46 Lemma 3.1 for compact support), H9 repaired. O-17 stands `PROVED modulo the 106_11 import`. |
| **D.29** | **CONFIRMED** (rewritten; the round-1 recommendation withdrawn). |
| **D.30** | **CONFIRMED with corrections C4, C5, C6** (and C1–C3, C7–C10). |
| README / `§ Label` | **CONFIRMED**, subject to C5/C6/C9. |

---

## 1. Findings H1–H14: per-finding confirmation

| # | ledger status | **auditor's verification** |
|---|---|---|
| H1 | CLOSED — withdrawn | **CONFIRMED.** Head matter (ll. 19–35) withdraws both halves, names the two reasons (the unearned quantifier in case (A); provability vs truth), and the new FATAL box at D.27.6 (l. 651) says only *"nothing with a sign is proved"* and *"for `C` in case (A) the status of (c) is not decided"*. (Q1) is now explicitly `not decided` in the `§ Label` table. Correct. |
| H2 | CLOSED — reframed | **CONFIRMED.** D.27.5 is re-presented as *"(c) alone implies RH in case (B)"*, i.e. a **weakening of Theorem 12.3's hypotheses**; the `h⁰_{\deg}` example showing case (B) does **not** imply (b′) is added; "closed negatively" is gone. |
| H3 | CLOSED — restricted to the schema | **CONFIRMED** at all four sites (D.26.11 box l. 372; (AT-1)(ii) l. 745; (AT-2); D.29). D.28.2's wording kept verbatim, as certified. See **C8** for a residual cross-section tension. |
| H4 | CLOSED — repaired | **CONFIRMED** verbatim (ll. 832–845): order-2 `Π`, single Green kernel, `Π²` for the double convolution, and Paper 46 **Lemma 3.1** cited for compact support. The `D ↦ D+4` consistency check is stated. |
| H5 | CLOSED — `RESTATEMENT` | **CONFIRMED** (l. 495): the trace-free two-line proof is printed as the version of record; the D.24.7 comparison deleted; the "classical sanity check" reading stated, and §D.30's candidate satisfies it by construction. |
| H6 | CLOSED — §D.30 | **CONFIRMED and exceeded**: the ledger built the candidate out, decided the gate constant (D.30.7 — **new, not in the audit**), added the direct proof of ⟹ RH and the stable weakening. See §2. |
| H7 | CLOSED | **CONFIRMED.** D.26.9(iv) → `RESTATEMENT` with the graph observation; (v) → `PROVED ⊆ / OPEN ⊇`; "explicit" withdrawn; "all the linear conditions" withdrawn; README and P46-19 aligned. |
| H8 | CLOSED | **CONFIRMED** (ll. 145–160): multiset convention, hypothesis class (`θ < ∞` + rapid decay, `A = A_0(𝒦)`), half-plane `\mathrm{Re}\,w > 1+θ`. |
| H9 | CLOSED | **CONFIRMED**: "four interpolation conditions" replaced by one complex condition; the modulus-domination sentence for the wrong-sign tail added at *Tail domination*. |
| H10 | CLOSED | **CONFIRMED**: `𝓝_∞ ⊕ Λ_ξ` deleted; only Thm 11.10(c) used. |
| H11 | CLOSED | **CONFIRMED**: the matched string and path are printed (`04-papers/32-stepanov-band/main.tex:33`). |
| H12 | CLOSED | **CONFIRMED**: `§ Label` rewritten; every row of the audit's table applied. |
| H13 | CLOSED | **CONFIRMED**: Addendum D.27.6a; optimality at `½K` recomputed here (`1/16 − 2/16 + 4/16 = 3/16` ✓); `h⁰_{\deg}(−K) = ¼ > 0` with `\deg(−K) < 0`; the `3/16` vs `1/8` box is correct. |
| H14 | CLOSED | **CONFIRMED** (l. 91): `T` depends on a choice quantified over `Z(ξ)`; `g` re-chosen per model; D.26.11 read as "the same construction performed separately in each model". |

**Contested by the auditor: none. Cosmetically discharged: none.**

---

## 2. §D.30, audited with full hostility

### 2.1 Serre symmetry, (a), (c), growth — **all verified** (coordinator item 1)

* **D.30.1.** Re-derived independently:
  `R(K−E) = ½[I(K,K) − 2I(K,E) + I(E,E)] − ½[I(K,K) − I(E,K)] + χ = ½I(E,E) − ½I(E,K) + χ = R(E)`.
  Pure bilinearity and symmetry; `I_∞(K,K)` cancels and is never evaluated. **Correct.** Coordinate
  check also re-done: `(½−a)(½−b) − ab − ¼(1−a−b) + ¼(a+b) = [¼ − ½(a+b) + ab] − ab − ¼ + ¼(a+b) +
  ¼(a+b) = 0`. **Correct**, and `W(K−E) = W(E)` because `Φ_K(ρ) = ξ(ρ) = 0`. **Correct.**
* **D.30.5(ii), the gate case analysis.** Re-derived. `\deg E + \deg(K−E) = \deg K = 1 > 0`, so the
  two gates cannot both be off. `\deg E ≤ 0`: second gate on, LHS `≥ \max(R(K−E),0) = \max(R(E),0) ≥
  R(E)` by D.30.1. `\deg E ≥ 1`: first gate on, same bound. `0 < \deg E < 1`: both on, LHS
  `= 2\max(R(E),0) ≥ R(E)`. **No case uses `χ`, no case uses a sign.** Verified; and the boundary
  cases `\deg E = 0` and `\deg E = 1` are covered by the first and second case respectively (the gate
  is strict `> 0`, and `1 − 0 = 1 > 0`). **(c) holds unconditionally for every `χ`. Confirmed.**
* **Growth.** `\deg(mK) = m`, `I_∞(mK,mK) = m²/2`, `I_∞(mK,K) = m/2`, so
  `R(mK) = m²/4 − m/4 + χ` and the gate is on for `m > 0`. `¼m² + O(m)` on the nose. **Confirmed.**
  The number-field scaling (`r²/4`) follows from `I_∞^{(K)}(K_K,K_K) = r²/2`, `\deg_K K_K = r`.
* **Vanishing in degree `≤ 0`** — the gate, plus `\deg|_{P^W} = 0` (Thm 11.13(iii)). **Confirmed**, and
  this is exactly D.27.4's requirement met by construction, as H5 predicted it must be.
* **Not 2-homogeneous** (`R(2K) = ½+χ` versus `4R(K) = 4χ`) and **not a bidegree-function** (it reads
  `W`). **Confirmed**; so neither D.27.5 nor `R140` D.24.7 applies.
* **D.30.6 (D.24.7's witness defeated).** `W(E_0+tF) = W(E_0) + 2tW(E_0,F) + t²W(F)`, and under RH
  `W(F) = Σ_ρ|Φ_F(ρ)|² > 0` once `Φ_F(ρ_1) ≠ 0`, so `R(E_t) → −∞`. **Confirmed**, and the label
  `PROVED under RH` is the right one (unconditionally the conclusion needs `W(F) > 0`, which is where
  the builder's parenthesis puts it).

### 2.2 The gate constant (coordinator item 2)

**D.30.7 (`χ > 0` refuted) — verified in full, including the effectivity argument.**
With `M(K) = (½,½)` and `M(τ_cK) = ½(e^{c/2},e^{−c/2})`:
`a − b = ½β(e^{c/2}−e^{−c/2})`, so `a−b = −3ε` gives `β = −6ε/(e^{c/2}−e^{−c/2})` ✓ (`c > 0`, so `β`
is defined and negative); `a = ½α + ½βe^{c/2} = −ε` gives `α = −2ε − βe^{c/2}` ✓. Hence
`M(E) = (−ε,2ε)`, `\deg E = ε > 0` ✓, `Z(E) = 0` (both generators have `Φ(ρ) = e^{(ρ−½)c}ξ(ρ) = 0`)
✓, `W(E) = 0` ✓, and `R(E) = ab − ¼\deg E + χ = −2ε² − ε/4 + χ > 0` for `ε` small when `χ > 0` ✓.

*The non-effectivity argument, which the coordinator asked to be checked carefully, is correct and its
mechanism is the one named:* `\deg E = ε > 0`, so the **degree** gives nothing here; what kills it is
the **individual ruling**. `Φ_E(1) = a = −ε < 0`, while every effective `E' ≢ 0` has
`Φ_{E'}(1) = ∫E'(u)e^{u/2}du > 0` **and** `Φ_{E'}(0) = ∫E'e^{−u/2}du > 0` (both integrands `≥ 0`,
positive somewhere — Thm 11.13(i)'s proof, and D.26.9(iii)); and `M` is `𝓝_∞`-invariant because
`Φ_N(0) = Φ_N(1) = 0` for `N ∈ 𝓝_∞` (Thm 11.11, (11.14)). **So the rulings are `𝓝_∞`-invariant and
both rulings of a nonzero effective class are strictly positive: a class with a negative ruling is
equivalent to no nonzero effective class, whatever its degree. Confirmed.** This is a sharper
necessary condition than positivity of the degree, and D.30.7 is the first place in the phase where
the distinction bites.

**Corollary D.30.8 (calibration at `χ = 0`) — computation verified, one wording defect.**
Under RH every zero is `½+iγ`, `Φ_E(1−ρ) = \overline{Φ_E(ρ)}` for real `E`, the multiset is
`\barρ`-stable and `ξ(½) ≠ 0`, so `W(E) = 2Σ_{γ>0}|Φ_E(½+iγ)|²` — **equality**, not `≥`. Then
`R(E) > 0` with `χ ≤ 0` gives `Σ_{γ>0}|Φ_E(½+iγ)|² = ½W(E) < ab − ¼\deg E + χ ≤ ab`, whence
`ab > ¼\deg E > 0`, `a,b > 0` (with `a+b > 0`), and `|Φ_E(ρ)|² < ab` termwise. **Both conclusions
confirmed**, and (ii) is indeed `R140` Lemma D.24.6's bound `b^{1−β}a^{β}` at `β = ½`, made strict.
**But see C2: the calibration is one-directional, not exact.**

### 2.3 (b′)⁺ ⟹ RH (coordinator item 3) — **both proofs verified; Proof 2 is the better one**

*Proof 1* is Theorem 12.3 applied to `h⁰_{RR}^{+}`, whose (a) and (c) are D.30.5 and whose
`\{h⁰ > 0\}` is exactly `\{\deg > 0,\ R > 0\}`. **Correct.**

*Proof 2*, re-derived independently: `E := rF + K`, `F` real primitive `C_c^∞` with `q := I_∞(F,F) > 0`.
`\deg E = \deg K = 1 > 0`; `I_∞(E,E) = r²q + 2rI_∞(F,K) + I_∞(K,K) = r²q + ½` since `I_∞(F,K) = ½\deg F
= 0`; `R(E) = ½r²q + ¼ − ¼ + χ = ½r²q + χ > 0` for `r² > −2χ/q`. By (b′)⁺ there is `E' ≥ 0`, `≢ 0`,
`E − E' ∈ 𝓝_∞`; the radical property (Thm 11.11) gives `I_∞(E',F) = I_∞(E,F) = rq` and Thm 11.13(ii),(iv)
gives `\deg E' = 1`; Theorem **11.14(ii)** — *"`|I_∞(E,F)| ≤ C_F\deg E` for every effective `E`"*, with
`C_F ≤ |Φ_F(0)|+|Φ_F(1)|+Σ_ρ|Φ_F(1−ρ)| < ∞` unconditionally by (11.2) and (E3d) — gives `rq ≤ C_F`,
independent of `r`. Contradiction for `r > \max(C_F/q, \sqrt{−2χ/q})`. **Correct.**

**This proof is strictly better than Proof 1 and the round undersells it.** It uses neither ampleness,
nor Step 2 of Theorem 12.3, nor the openness of the ample cone (Thm 11.14(iii)); it needs (b′)⁺ at a
**single** class `rF+K` of degree exactly `\deg K`; and — see **C10** — it survives the stable
weakening verbatim, which Proof 1 needs D.30.11 for.

### 2.4 The stable weakening (coordinator item 4) — **verified**

**D.30.11.** Re-read against Theorem 12.3's printed proof. *Step 1* is untouched (it builds `H'` from
`F`, not from `h⁰`). *Step 2*: `N(K−nF) − E' ∈ 𝓝_∞` gives `N·I_∞(K−nF,H') = I_∞(E',H') > 0` by
ampleness, and `N ≥ 1 > 0`, so `m − nq > 0` — **the same conclusion, and the positivity of `N` is
what makes the division legitimate**. *Step 3* uses only (c). *Step 4*: `NnF − E' ∈ 𝓝_∞` gives
`\deg E' = Nn\deg F = 0` against `\deg E' > 0`. **Correct**, and Theorem 12.3 itself is untouched and
unrelabelled, as the label says. **D.30.12** ((b′)⁺_{st} ⟹ RH) follows. **Confirmed.**

### 2.5 O-18 (coordinator item 5)

**D.30.13 — verified, including the constant.** `E' := 2\sqrt{ab}\,τ_cK`, `c = \log(a/b)`. Then
`M(E') = 2\sqrt{ab}·½(e^{c/2},e^{−c/2}) = \sqrt{ab}\,(\sqrt{a/b},\sqrt{b/a}) = (a,b)` ✓ — **the
constant `2\sqrt{ab}` and the translate `\log(a/b)` are both correct**. `K > 0` pointwise (Thm
11.7(i), elementary after the phase-135 LF6 repair) and translation preserves positivity, so `E' ≥ 0`,
`≢ 0` ✓. `Φ_{E'}(ρ) = 2\sqrt{ab}\,e^{(ρ−½)c}ξ(ρ) = 0 = Φ_E(ρ)` ✓. Equality of `M` and of `Z` puts
`E − E' ∈ 𝓝_∞` by (11.14) ✓. The hypotheses `a,b > 0` come from `W(E) = 0`, `R(E) > 0`, `χ ≤ 0` ✓.
**`PROVED`, unconditional. Confirmed**, and the remark that `\{2λτ_cK\}` sweeps the open quadrant of
bidegrees is correct.

**Is the diagnosis correct and complete?** *Correct in direction, incomplete on the necessary side.*
* (ii) — "what is missing is a **sufficiency** criterion for the exponential moment problem of
  Prop. D.24.9" — is **right**, and the statement of O-18 is the right statement of it (modulo **C3**).
* (iii) — the perturbative route is blocked by `R138_001` Thm D.15.2b(ii) — **verified as a citation**
  and the reason given (super-exponential decay of `K` versus `e^{−(1+ε)|t|}` for `N ∈ D^W`) is the
  reason D.15.2b(ii) gives. Correct, and it is a real block.
* (i) — "no counterexample is available from the known necessary conditions" — is **incomplete**: see
  **C4**.

**Convexity of `S_0`:** the *statement* is right, the *proof* is not. See **C5**, which supplies a
correct proof.

### 2.6 Falsifiers (coordinator item 6) — **verified, with one caveat**

* **D.30.15.** `\deg_Z K_Z = 2I_∞^{(Z)}(K_Z,K_Z) = 2Σ_{p∈P}Z(p)Z(1−p) = 2Σ_pZ(p)²` using the
  functional equation `Z(1−p) = Z(p)` and `P = 1−P`. For `ξ`: `2(¼+¼) = 1 = \deg K` ✓. For `Ξ_Q`:
  `2·2·\tfrac1{16} = ¼` ✓. For `Ξ_a`: `> 0` and `\#P = 4` ✓. The gate argument needs only
  `\deg_Z K_Z > 0` (A2⁺), and the three-case analysis generalizes with `\deg K_Z` in place of `1`.
  **Confirmed — the rank of the polar block is indeed irrelevant, which is the coordinator's check,
  and the conclusion "the entire model-dependence of row D sits inside (b′)⁺" is earned.**
* **D.30.16 (`Ξ_a`).** `E = rF_+ + K_a`: `\deg_a E = \deg_a K_a > 0` ✓ (`F_+` is `Ξ_a`-primitive, so
  `I_∞^{(a)}(F_+,K_a) = ½\deg_a F_+ = 0`, which I verified transports: `I_∞(F,K_Z) = Σ_pΦ_F(p)Z(p) =
  ½\deg_Z F`). `R_a(E) = ½r²q + ½I^{(a)}(K_a,K_a) − ¼\deg_a K_a + χ = ½r²q + χ` **exactly**, since
  `\deg_a K_a = 2I^{(a)}(K_a,K_a)` — the same identity as for `ξ`; the builder leaves it unsimplified,
  which is harmless. The contradiction is Proof 2 transported, and the one substantive transport is
  Theorem 11.14 via §12.5(c). **Confirmed**, subject to **C7**. The independent confirmation through
  Paper 46 Theorem 12.4 is a genuine second route and agrees.
* **`Ξ_Q`: `C_F = ∞` — verified.** The polar weight is `Σ_{p∈\{0,1\}}Ξ_Q(p)e^{(p−½)u} = ¼·2\cosh(u/2)
  ≍ e^{|u|/2}`, while a Davenport–Heilbronn zero with `β > 1` contributes `e^{(β−½)|u|}` with
  `β − ½ > ½`. The ratio is unbounded, so `C_F = ∞` for any `F` with `Φ_F(1−ρ) ≠ 0` at such a `ρ`.
  **This is exactly the failure of A7** (`\sup_ρ|\mathrm{Re}\,ρ − ½| ≤ θ_P`), and since Theorem 12.3's
  Step 1 builds the ample class out of Thm 11.14(ii),(iii), **Theorem 12.3 does not transport to
  `Ξ_Q`**. **Confirmed, and this is the most valuable structural finding of round 2 after §D.30
  itself**: it localizes the `Ξ_Q` half of T2 in the *frame* rather than in the clause.
* **"A7 enters before the clause; A3 must enter the proof of (b′)⁺; A8 has no role yet."**
  **Confirmed on all three counts.** A7 at Thm 11.14, before (b′)⁺ is stated ✓. A3: the frame survives
  for `Ξ_a` (`θ_a = ½+a` finite), (a) and (c) hold there (D.30.15), and (b′)⁺ is **false** there
  (D.30.16) — so any proof of (b′)⁺ for `ξ` must break at `Ξ_a`, and T2 (R139 D.19.7) itself pins the
  `Ξ_a` falsifier to **A3**, so the attribution matches the corpus's own and is not a new claim ✓.
  A8: nothing in §D.30 reads the Euler product; the honest statement that this is "where the work
  remains" is right, and D.26.10(v) (`PRIME ≥ 0`) is correctly named as the only free sign the
  arithmetic side supplies ✓.

### 2.7 Corpus check (coordinator item 7) — **re-run independently and confirmed**

`grep -rIn "h⁰_{RR}\|h0_RR\|h⁰_RR\|RR-defined\|Riemann–Roch-defined\|Riemann-Roch-defined"` over
`--include=*.md --include=*.tex --include=*.py`, excluding phase-141: **zero hits**. Paper 46 §13
contains the `H⁰`-**set** candidate (Def. 13.1, Thm 13.2, Restatement 13.3) and the lattice count
(Def. 13.4, certified by `scripts/h0_candidate.py`); `R140` has the tensor square. **None is `\max` of
clause (c)'s own right-hand side, and no Riemann–Roch-defined `h⁰` exists in the corpus.** The two new
placements (`R138_001` Thm D.15.2 used in D.30.14, D.15.2b(ii) used in O-18(iii)) are uses, not
relabels, and I verified both statements exist at `R138_001` §D.15.2. The identification of clause
(b′)⁺ with the corpus's repeatedly named missing ingredient (*"an existence theorem for positive
self-intersection"*, `107_239`, `111_03_VERDICT`, `111_99`) is **apt and is not a relabelling**: those
documents name a gap, this one names a statement.

---

## 3. New findings

### C4 — MAJOR. The necessary side of O-18 is **not** exhausted: Theorem 11.14(ii) is a checkable, unconditional family of necessary conditions, and it is the one that refutes `Ξ_a`.

*Location:* D.30.6(i) ("*the two unconditional necessary conditions for membership in `𝔐` … are both
implied by the hypothesis*"; "*the `𝒫_g`-conditions are not checkable*"); `R141_003` §3(2).

*The omission.* If `E ≡ E' \pmod{𝓝_∞}` with `E' ≥ 0`, `≢ 0`, then for **every** `X ∈ D^W`

    |I_∞(E,X)| = |I_∞(E',X)| ≤ C_X·\deg E'= C_X·\deg E ,                       (★)

by Theorem 11.14(ii), with `C_X ≤ |Φ_X(0)|+|Φ_X(1)|+Σ_ρ|Φ_X(1−ρ)| < ∞` unconditional. This is an
**explicit, unconditional, `X`-indexed family of necessary conditions for membership in `𝔐`**, with a
computable constant — it is the `𝒫_g`-dual condition with the constant supplied, so the round's
dismissal ("*not checkable, because `𝒫_g` is undescribed*") does not apply to it. It is not one of the
two conditions D.30.6(i) considers, and it is strictly stronger than both on many classes.

*Why this matters more than a bookkeeping omission.* (★) is **exactly the mechanism of Proof 2 of
D.30.10 and of the `Ξ_a` refutation D.30.16**: there, (★) at `X = F_+` is what bounds `r`. So the
family that kills `Ξ_a` is the family the diagnosis does not test against `ξ`. If O-18 has a
counterexample, this is where it is.

*What the test looks like, carried out as far as it goes here.* Take `X = F` primitive. Under RH,
`I_∞(E,F) = −Σ_ρΦ_E(ρ)Φ_F(1−ρ)` and `Φ_F(1−ρ) = \overline{Φ_F(ρ)}`, so by Cauchy–Schwarz and
Corollary D.30.8,

    |I_∞(E,F)| ≤ \big(Σ_ρ|Φ_E(ρ)|²\big)^{1/2}\big(Σ_ρ|Φ_F(ρ)|²\big)^{1/2}
              = \big(W(E)\big)^{1/2}\big(W(F)\big)^{1/2} < \sqrt{2ab}\,\sqrt{W(F)}
              ≤ \tfrac{1}{\sqrt2}\,\deg E\,\sqrt{W(F)} ,

using `ab ≤ (\deg E)²/4`. So (★) at primitive `X = F` is implied by

    C_F ≥ \sqrt{W(F)/2} = \sqrt{−I_∞(F,F)/2} \qquad\text{for every primitive } F ∈ D^W .   (C4.1)

**(C4.1) is a purely classical, zero-free, unconditional-looking inequality between the
bounded-density constant (11.17) and the zero-sum `W`, and it is not in the corpus.** If it is true,
the whole primitive half of the necessary family is consistent with the hypothesis of O-18 and the
diagnosis is restored; if it fails for some `F`, that `F` builds a counterexample to O-18 and
therefore shows (b′)⁺ is **strictly stronger than RH**, which would settle the fork in D.30.6(iv).

*Repair, and the instruction for phase 142.* Add (★) to the list of known necessary conditions in
D.30.6(i); state (C4.1) as the sharp form on the primitive sector; and make deciding (C4.1) — together
with the non-primitive cases of (★) — the **first** task of phase 142, ahead of any attempt at O-18's
construction. It is cheaper than the moment problem and it can refute.

### C5 — MAJOR. D.30.14(i) misidentifies `S_0`; the theorem is true, but the printed proof proves something else.

*Location:* Proposition D.30.14(i): "*`S_0 = \{E : I_∞(E,E) > 0,\ I_∞(E,K) > 0\}` is a convex cone —
the forward cone of the Lorentzian form `I_∞`*."

*The error.* By definition `S_χ = \{\deg E > 0,\ R(E) > 0\}` and, with `ℓ := I_∞(E,K) = ½\deg E`,

    R(E) = \tfrac12 I_∞(E,E) − \tfrac12 I_∞(E,K) + χ ,\qquad
    R(E) > 0 \iff I_∞(E,E) > I_∞(E,K) − 2χ .

At `χ = 0` this is `Q(E) > ℓ(E)`, **not** `Q(E) > 0`. Consequently:
1. The printed identity is false. `S_0 = \{ℓ(E) > 0,\ Q(E) > ℓ(E)\}`, a proper subset of
   `\{Q > 0, ℓ > 0\}`.
2. **`S_0` is not a cone**: `R(λE) = λ²·½Q(E) − λ·½ℓ(E)`, which is not `λ`-homogeneous. So the
   sentence "*a convex cone*", the two-nappe argument, and the phrase "the forward cone of the
   Lorentzian form" are all about the wrong object. (The round already knows `h⁰_{RR}^{+}` is not
   2-homogeneous — D.30.5(v) — so `S_0` could not have been a cone.)

*The statement is nevertheless true, and here is a correct proof.* Complete the square at `½K`:

    Q(E − \tfrac12K) = Q(E) − Q(E,K) + \tfrac14Q(K) = Q(E) − ℓ(E) + \tfrac18 ,\qquad Q(\tfrac12K) = \tfrac18 ,

so, with `Y := E − ½K`,

    S_0 = \{E : Q(Y) > Q(\tfrac12K) = \tfrac18\ \text{and}\ ℓ(E) > 0\} .

Assume RH, so `Q` is Lorentzian with positive vector `K` (`Q(K) = ½ > 0`) and `Q ≤ 0` on `K^{⊥}`
(`R138_001` Thm D.15.2(a), exactly as the round argues). Then `\{Q > 0\}` has two nappes, and:
* *the backward nappe is excluded by `ℓ > 0`*: if `Y` is timelike in the nappe opposite to `K`, the
  reverse Cauchy–Schwarz inequality gives `Q(Y,K) ≤ −\sqrt{Q(Y)Q(K)} < −\sqrt{\tfrac18·\tfrac12} =
  −\tfrac14`, whence `ℓ(E) = Q(Y,K) + \tfrac12Q(K) < −\tfrac14 + \tfrac14 = 0`;
* *the forward branch is convex*: on the forward cone `\sqrt{Q}` is concave (standard for a Lorentzian
  form), so `\{Y \text{ forward} : \sqrt{Q(Y)} > 1/(2\sqrt2)\}` is convex, and `S_0` is its translate
  by `½K`.

Hence **`S_0` is convex under RH** — an *affine* convex set, not a cone. The correction is worth
making rather than deleting: the extremal class `½K` that appears here is the **same** class that is
extremal for `χ = 3/16` in Addendum D.27.6a(i), which is not a coincidence (`R` is `σ_K`-invariant and
`½K` is the fixed point of `σ_K`).

*Downstream.* D.30.14's own conclusion — that under RH the containment `T(S_0) ⊆ 𝔐` is a containment
of convex sets, so convexity of `𝔐` yields no new necessary condition — **survives verbatim** with
"cone" replaced by "convex set" (convexity of `𝔐` is still what makes `\mathrm{conv}\,T(S_χ) ⊆ 𝔐`
equivalent to (D.30.2), and that step used only convexity of `𝔐`, which is D.26.9(i)).

### C6 — MAJOR (label). D.30.14(ii) is a sketch labelled `PROVED`.

"*if `S_0` is convex then `I_∞` has at most one positive direction, i.e. RH*" is argued in two lines
("replacing `X` by `X + tK` for small `t`, which keeps `Q(X) > 0` and makes `ℓ > 0`") without
verifying that `Q(X+Y) ≤ 0` survives that replacement, and — after C5 — without the conic structure the
argument tacitly uses. The claim is plausible and is the contrapositive of D.15.2's mechanism, but it
is not proved here. **Downgrade to `SKETCH`** or prove it. It is not load-bearing: nothing else in
§D.30 or in D.29 uses (ii).

### C1 — MINOR. "`χ = 0` is the weakest **admissible** gate" presumes what is open.

Corollary D.30.8 says "*admissibility forces `χ ≤ 0`, and `χ = 0` is the weakest … admissible gate*".
Admissibility of `χ = 0` **is** clause (b′)⁺ at `χ = 0`, which is `OPEN` (D.30.9, O-18). Rewrite as
"*`χ > 0` is refuted; `χ = 0` is the weakest gate not refuted, and is the recommended normalization*".

### C2 — MINOR. The calibration at `χ = 0` is one-directional; "no more and no less" is false — and the truth is better for the candidate.

The box after Corollary D.30.8 says the gate "*cuts out precisely the classes that pass both elementary
tests for membership in the moment cone — no more and no less*". Only `⟹` is proved, and the converse
is false: the gate imposes the **`ℓ²`-sum** condition `Σ_{γ>0}|Φ_E(½+iγ)|² < ab − ¼\deg E`, while
Lemma D.24.6 imposes only the **pointwise** bound `|Φ_E(ρ)| ≤ \sqrt{ab}`. A class with many zeros each
below `\sqrt{ab}` but with a large sum passes D.24.6 and fails the gate. So `\{R > 0,\ \deg > 0\}` is
**strictly inside** the region cut out by the known necessary conditions. That is the *favourable*
direction — the clause asks less than the tests allow, so there is more room for O-18 to be true — and
it should be stated that way rather than as an exact calibration.

### C3 — MINOR. O-18 as posed is formally stronger than `RH ⟹ (b′)⁺`.

O-18 quantifies over **all** `(a,b,(z_ρ))` with `z_{1−ρ} = \bar z_ρ`, rapid decay and
`Σ_{γ>0}|z|² < ab`. Clause (b′)⁺ needs the construction only for data that are **actually realized** by
some `E ∈ D^W` with `\deg E > 0`, `R(E) > 0`. Unless every such `(z_ρ)` is realized by a class in
`D^W` — which is not proved (D.26.6 gives surjectivity of **finite** windows only) — O-18 `⟹` (b′)⁺ but
not conversely. State O-18 as *sufficient for* `RH ⟹ (b′)⁺`, and record the realizability question as
the possible slack.

### C7 — MINOR. The §12.5(c) transport of Theorem 11.14 to `Ξ_a` is borderline and needs its two side conditions printed.

D.30.16 uses `C_{F_+} < ∞` for `Ξ_a`, via the replacement of the weight `2\cosh(t/2)` by
`Σ_{p∈P}Ξ_a(p)e^{(p−½)t}`. Two things must be said: (i) the weight dominates only if
`Ξ_a(p) > 0` at the **extreme** poles `p = 1+a`, `p = −a` (otherwise the leading exponential cancels);
(ii) since `θ_a = ½+a` equals the extreme polar exponent, the domination of `|e^{(ρ−½)u}| ≤
e^{θ_a|u|}` by the weight is by a **constant factor at the borderline**, not with room to spare — it
still gives `C_F < ∞` via (11.17) and (E3d), but the borderline should be stated, because it is
precisely where `Ξ_Q` fails (there the zero exponent **exceeds** the polar one).

### C8 — MINOR. A cross-section tension that needs one sentence.

D.28.2 refutes, at `Ξ_Q`, every rule landing in case (B); D.30.8 shows that Theorem 12.3's frame
(Thm 11.14 → the ample class) **does not transport to `Ξ_Q`**. These are consistent **only** because
D.27.5(B)'s derivation uses (c), 2-homogeneity and ray-continuity — and **not** Theorem 11.14, Theorem
12.3 or ampleness. Without that sentence the two sections read as contradicting each other. Add it at
D.30.8 (and cross-reference from D.28.2).

### C9 — MINOR. Cross-reference slip.

Head matter (l. ~33): "*Theorem D.30.8 shows it **implies** RH*". The implication theorem is **D.30.10**;
D.30.8 is the corollary forcing `χ ≤ 0`.

### C10 — MINOR (an improvement, not an error). Proof 2 survives the stable weakening verbatim, and the round does not say so.

Under (b′)_{st}, Proof 2 gives `N·E − E' ∈ 𝓝_∞`, hence `I_∞(E',F) = N\,rq` and `\deg E' = N\deg E = N`,
so Theorem 11.14(ii) yields `Nrq ≤ C_F·N`, i.e. **`rq ≤ C_F`** — the multiple cancels and the
contradiction is unchanged. So **(b′)⁺_{st} ⟹ RH by the direct route too**, with no appeal to D.30.11
or to Theorem 12.3. Worth one line in D.30.11/D.30.12, since it makes the recommended target
(b′)⁺_{st} independent of the ampleness machinery — and hence of A7 — in its implication direction.

---

## 4. Is (b′)⁺ (or (b′)⁺_{st}) at `χ = 0` the right target for phase 142?

**Yes, with one instruction attached.** The judgement, stated hostilely:

**What is genuinely established.** Clauses (a) and (c) of Theorem 12.3 are now **theorems**:
unconditional, for every `χ`, with the required `¼m² + O(m)` growth, and **model-uniform** (D.30.15 —
the gate needs only `\deg_Z K_Z > 0`, i.e. A2⁺). That is a real change of state for row D: two of the
three clauses are closed, and the phase-136 growth wall and `R140`'s bidegree refutation are both
cleared by one object. The remaining clause is a single sentence about effectivity, stated with
arithmetic hypotheses (`I_∞`-pairings, Def. 11.4, naming no zero).

**Why it is the right target.**
1. It is the **weakest** form available: (b′)⁺_{st} (some positive multiple) is proved to suffice
   (D.30.11 + C10), and it is the exact arithmetic analogue of *"`D² > 0`, `D·H > 0` ⟹ `D` is big"* —
   the classical statement that Weil's argument actually consumes.
2. It **carries the whole model-dependence** (D.30.15), which is the sharpest form T2's demand has
   taken: (a) and (c) hold for `Ξ_a` and `Ξ_Q` too, so every falsifier now bites at one line.
3. It is **false for `Ξ_a`** with an explicit witness (D.30.16) — so it is not vacuous, and any proof
   must use A3.
4. It is **proved on the zero-free locus** (D.30.13), unconditionally, with an explicit two-parameter
   family of effective witnesses.
5. It is **not refuted** by anything in the corpus.

**Its exact open content, stated so phase 142 cannot drift.** Two separate questions, and they must
not be conflated:
* **(Q-A) Is (b′)⁺ consistent with the known necessary conditions?** This is a *refutation* question
  and it is cheap. The necessary conditions are: both rulings `> 0` (D.26.9(iii) — sharpened by
  D.30.7's witness, which shows the **ruling**, not the degree, is the operative test), Lemma D.24.6's
  pointwise bound, and — **omitted by the round, C4** — the bounded-density family (★)
  `|I_∞(E,X)| ≤ C_X\deg E` for every `X ∈ D^W`, whose primitive case reduces under RH to (C4.1)
  `C_F ≥ \sqrt{−I_∞(F,F)/2}`. **Decide (C4.1) first.** If it fails, (b′)⁺ is strictly stronger than
  RH and the gate must be strengthened (and the natural strengthening is the `𝒫_g`-conditions, i.e.
  O-15′′). If it holds, the consistency check passes and the diagnosis of D.30.6 is restored.
* **(Q-B) Does RH imply (b′)⁺?** This is O-18: a **sufficiency** criterion for the exponential moment
  problem — given `a,b > 0` and rapidly decaying `(z_ρ)` with `z_{1−ρ} = \bar z_ρ` and
  `Σ_{γ>0}|z|² < ab`, build a nonnegative `E' ∈ D^W` with those moments. The perturbative route is
  blocked (`R138_001` D.15.2b(ii)); no sufficiency criterion exists in the corpus; Carleman is
  unavailable (D.26.10(iv)). This is hard, and it is the honest location of row D's remaining work.

**And the standing caveat, which must travel with the target.** (b′)⁺ ⟹ RH. Therefore **a proof of
(b′)⁺ is a proof of RH**, and phase 142 operates under the FATAL rule from its first line: any
argument that appears to establish (b′)⁺ unconditionally must be screened before it is written up, and
must be checked at `Ξ_a` — where (b′)⁺ is **false** (D.30.16) and where every hypothesis of the frame
(A7, A1–A6, A2⁺) holds. That check is now cheap and decisive, and it is the reason this target is
safe to pursue: **the falsifier is available at the same line as the theorem.**

---

## 5. Residue

* **R12.** Decide (C4.1) `C_F ≥ \sqrt{−I_∞(F,F)/2}` for primitive `F ∈ D^W` (equivalently, test the
  bounded-density family (★) against the hypothesis of (b′)⁺). First task of phase 142; it can refute,
  and it is the mechanism that kills `Ξ_a`.
* **R13.** Repair D.30.14: `S_0 = \{ℓ > 0,\ Q(E−½K) > Q(½K)\}`, convex under RH by concavity of
  `\sqrt Q` on the forward cone, with the backward branch excluded by reverse Cauchy–Schwarz (C5);
  downgrade (ii) to `SKETCH` (C6).
* **R14.** Wording: C1 ("weakest not-refuted gate"), C2 (the calibration is one-directional and the
  gate is *strictly inside* the necessary region), C3 (O-18 is formally stronger than `RH ⟹ (b′)⁺`),
  C7 (the two side conditions of the `Ξ_a` transport of Thm 11.14), C8 (one sentence reconciling
  D.28.2 with D.30.8), C9 (D.30.8 → D.30.10), C10 (Proof 2 survives (b′)_{st} verbatim).
* **R15.** Carried from round 1 and untouched: O-15′′ (description of `𝒫_g`), R2 (Paper 44 `Q_{fin}`
  versus `G^{Frob}`), the 8bis.4a warning on family (A), O-10 (non-principal `Q`), O-13.

**Row D: no label change.** (a) and (c) are theorems; (b′)⁺ is not, and nothing with a sign is proved.
