# R144.003 — Builder, round 2 (final), phase 144: ledger of repairs

*Builder: Claude Opus 5. Date 2026-09-13. Input: `R144_002_HOSTILE_AUDIT.md` (ACCEPT WITH REPAIRS;
no FATAL; M1, M2, M3 MAJOR; m1–m9 MINOR; programme-level assessment §9). All repairs are applied
**in place** in `R144_001_BUILDER_ROUND1.md`, each carrying a bracketed round-2 note naming the
finding; `README.md` is updated; `§D.40` is new. No finding is contested. The three headline results
(Lemma D.37.2 and the refutation of the blueprint's A3-line; Theorem D.38.3 `(P_m) ⟺ RH`; Theorem
D.38.5 bounded density on `S_0` ⟺ RH) are unchanged — the audit re-derived all three independently
and confirmed them.*

**Summary: 12 of 12 findings accepted and discharged. Two labels move down (D.37.3's quantifier,
D.38.1 → `INVENTORY`), one open item is closed negatively (O-30), one section is added (§D.40). No
label moves up. Row D label: UNCHANGED. Nothing was contested and nothing was repaired by
restatement alone — each repair is at the statement it touches.**

---

## 1. Per-finding status

| finding | severity | status | what was done, and where |
|---|---|---|---|
| **M1** | MAJOR | **ACCEPTED IN FULL; the label moves down** | The auditor is right on both counts and I checked the mathematics again rather than taking the ledger's word. (a) `|\cosh((½−ρ)T)| ≤ e^{θ\|T\|}` is a **real-`T`** bound: for real `T` and `½−ρ = x+iy`, `\|\cosh((x+iy)T)\|² = \cosh²(xT) − \sin²(yT) ≤ e^{2θ\|T\|}`; for complex `T` the bound is `e^{\|½−ρ\|\|T\|}` with `\|½−ρ\| → ∞` over the zeros, and admissibility (Definition D.34.1's Convention) supplies only **super-polynomial** decay of `Φ_{g_a}(1−ρ)`, never `e^{−δ\|γ_ρ\|}`. So neither entirety nor real-analyticity of `Ψ` follows, and "discrete exceptional set" is unproved. (b) Even granting entirety, (iii) quantifies over `T` in a **one-parameter family**, while (iv) and the README quantified over the **whole admissible class** — a non-sequitur independent of (a). **Repair:** D.37.3(iii) now proves only what the real-`T` Laplace argument gives — `Ψ` is **continuous** on `R` and `Ψ ≢ 0` on `[0,∞)`, hence `\{Ψ ≠ 0\}` is a **non-empty open** set, still non-empty after removing the countable admissibility exclusion — and (iv) is restated as an **existence** statement: `m_*(g_a) < ∞` always, `m_* = 1` for a non-empty open set of test classes. Words "entire", "discrete exceptional set" and "for every admissible `g_a` outside …" deleted. Propagated to: `§0` item 2, D.39 ¶1, P46-45, the `§Label` row, the README headline bullet. **Nothing downstream changes:** D.38 uses only that *some* fixed finite index fails, i.e. D.37.3(i)+(ii), which the auditor re-derived and confirmed as written. |
| **M2 / m9** | MAJOR (borderline) | **ACCEPTED; relabelled** | Round 1 wrote "say **exactly**" and "one gets nothing more" and labelled the whole of Proposition D.38.1 `PROVED`. The four clauses (i)–(iv) are proved; the **maximality** claim — that nothing else follows from (D.38.1) — is a statement about all possible consequences and is not a theorem. **Repair:** the proposition is relabelled `INVENTORY` (clauses (i)–(iv) `PROVED`, unconditional), the maximality wording is withdrawn in the bracketed note, and the preamble now reads "the following four consequences are what this round uses (no maximality is claimed)". `§Label` row updated. |
| **M3** | MAJOR (omission) | **ACCEPTED; O-30 closed negatively** | The auditor is right that round 1's own witness ray decides its own phase-145 recommendation in one line, and that I failed to notice. **Repair:** new **Corollary D.38.5c** (`PROVED`): there is no `Ψ : R³ → R` with `W(E) ≥ −Ψ(Φ_E(1),Φ_E(0),\deg E)` on `S_0` unless RH — along `E_t = tF+K` one has `Φ_{E_t}(ρ) = tΦ_F(ρ)` (because `Φ_K(ρ) = ξ(ρ) = 0`), hence `W(E_t) = t²W_F = −t²q → −∞`, while `a = b = ½` and `\deg E_t = 1` are **frozen** and `R(E_t) = ½t²q > 0` keeps `E_t ∈ S_0`; conversely under RH `Ψ ≡ 0` works. So **O-30 ⟺ RH**. Propagated: D.39(b) rewritten as a withdrawal, the open-list row moved from OPEN to **CLOSED, negatively**, P46-49 extended, `§Label` gains the D.38.5c row, README bullet updated, and the item is removed from the phase-145 recommendations. |
| **m1** | MINOR | **ACCEPTED** | P46-43's retraction list now names **four** sources: `R143_001` l. 767 (Remark D.34.16c *Reading* bullet) and `R143_001` §D.34.5 item 5; `R143_003` l. 104; **`R143_004` l. 237**; `R143_005` §2 l. 32 — the last of which my own corpus-check table listed and my paper-facing row omitted. |
| **m2** | MINOR | **ACCEPTED, and it is the more important of the two** | P46-43 is now a **partial** retraction, and says so in its first words. Retracted: the polar-arity clause ("four exponents give no AM–GM floor"). **Kept, as true and as the actual separator:** the second half of §D.34.5 item 5 — the zeros of `Ξ_a` are `ρ ± a`, so `\|n^{½−(ρ±a)}\| = n^{∓a}` is unbounded — together with the indefiniteness of `W_a`; this is Theorem D.37.4(ii). Without this the erratum would have read as retracting a true statement. |
| **m3** | MINOR | **ACCEPTED** | Lemma D.37.2(ii) amended: the involution `p ↦ 1−p` has the fixed point `½`, whose term `C_½x^0 = C_½` is a constant and is added as a singleton; the pair sum runs over `p ≠ ½`. Vacuous for `ξ` and `Ξ_a`, but the lemma is stated for every symmetric `P`, so the amendment belongs in the statement. (i) is unaffected: `Σ_p(½−p) = 0` holds with or without a fixed point, since the fixed point contributes `0`. |
| **m4** | MINOR | **ACCEPTED** | One line added to Lemma D.37.1: Proposition 12.4B's hypothesis *"`Ξ_a` has a zero `ρ_0` with `\mathrm{Re}\,ρ_0 ≠ ½`"* is automatic and unconditional — the zeros of `Ξ_a` are `ρ ∓ a`, and `\mathrm{Re}(ρ−a) = \mathrm{Re}(ρ+a)` is impossible for `a ≠ 0`, so at most one member of each pair can sit on `\mathrm{Re}\,s = ½`; under RH for `ξ` every zero of `Ξ_a` has real part `½ ± a ≠ ½`. The whole falsifier rests on `q_a > 0`, so the check belongs in the text. |
| **m5** | MINOR | **ACCEPTED** | The README now prints the normalisation: the floor `1.0058518169146380679` and the AM–GM bound `1.0057848077201793325` are computed under `Φ_{g_a}(1+a) = Φ_{g_a}(1−a) = 1`, **two** independent normalisations of a single non-explicit `g_a`, so those two numbers are **not** `a`-invariants; the normalisation-free content is `A,B > 0` and the `\cosh` shape. `α`, `β`, `\deg_aK_a` **are** `a`-invariants and are quoted as such. (The script already said "normalised"; the README did not.) |
| **m6** | MINOR | **ACCEPTED** | Clause added to Lemma D.38.2a: `F_0` from Paper 45 Theorem 10.4 is even, but `F_1` from Lemma D.26.6 is unconstrained, so `F = F_0 + εF_1` need **not** be even. Nothing in Lemma D.38.2 or Theorem D.38.3 uses evenness of `F` or of `E` — only evenness of `g` (and `K` is even automatically) — so the argument is unaffected; the preamble must not be read as requiring an even `F`. |
| **m7** | MINOR | **ACCEPTED** | Theorem D.38.5's definition of `C^{S_0}_F` is widened to **any** real `F ∈ D^W`. The proof of (ii) never used `\deg F = 0`; only (i) does, and (i) states it. |
| **m8** | MINOR | **ACCEPTED** | The RH-conditionality flag on `N ≤ 64d²` (Proposition D.34.16(iii),(iv)) is now printed in the **README** bullet/file table and in the **`§Label`** row for D.38.4, not only in D.38.4(iv). The blueprint requires it at every use. |
| **audit item 7 (scope)** | — | **ACCEPTED** | A scope caveat is printed after Theorem D.37.4: (i)–(iii) locate the separating step **of Theorem D.34.10's proof**; they are not a proof that no other separation of `ξ` from `Ξ_a` exists (that would be a (T2)-type statement). "The A3-line sits there" is a correct *reading* of (i)–(iii), not an independent theorem, and the words "and nowhere else" are not attached. |

---

## 2. What moved, in labels

| item | round 1 | round 2 |
|---|---|---|
| D.37.3(iii),(iv) | `PROVED` — "`m_* = 1` outside a discrete exceptional set, for every admissible `g_a`" | `PROVED` — **existence form**: `m_* < ∞` always; `m_* = 1` for a **non-empty open set** of test classes |
| D.38.1 | `PROVED` (including maximality) | `INVENTORY`; clauses (i)–(iv) `PROVED` unconditional; maximality **WITHDRAWN** |
| O-30 | OPEN; recommended phase-145 target | **CLOSED, negatively** (Corollary D.38.5c: `O-30 ⟺ RH`) |
| D.38.5c | — | **new**, `PROVED` |
| D.40 | — | **new**, `PROVED` (clauses) + `SYNTHESIS` |
| everything else | unchanged | unchanged |

**No label moves up. Row D label: UNCHANGED.**

---

## 3. §D.40, and why this round proposes no new positivity target

The coordinator's instruction was to close the route rather than to re-open it, and the audit's §9
gives the reason in the form I would have had to give it myself: **one ray refutes everything**.
§D.40 is therefore written as a closure, with four parts:

1. **The final form** — Restatement D.38.3a, `RH ⟺ I_∞(E,g_λ) ≥ 0` on `S_0`: one bilinear
   inequality, one test class, no index set, no cone, no `h⁰`, no transfer theorem; `PROVED` +
   `RESTATEMENT`, and explicitly *not* progress towards a proof.
2. **The universal refuter** — the ray `E_t = tF + K` with `F` primitive and `I_∞(F,F) = q > 0`,
   with the table of frozen invariants (`a = b = ½`, `\deg = 1`, `I_∞(E_t,K) = ½`, `R(E_t) = ½t²q > 0`)
   against the unbounded quantities (`W(E_t) = −t²q`, `Σ_ρ|Φ_{E_t}(ρ)|²`, `t_m(E_t)`,
   `|I_∞(E_t,F)|/\deg E_t`), and the second table listing the **six** weakenings it refutes: the
   fixed index `(P_m)`, the sparse cone (O-29), the stratification of the `d = 1` head, bounded
   density on `S_0`, the large-constant hope, and O-30. Lemma D.40.2 records that the ray exists
   **iff** RH is false and that all six rows follow from the same three identities.
3. **What the frame cannot see** — (W1) `W(E)` is a `ρ ↔ 1−ρ` pairing, a **norm iff RH**, so
   `R(E) > 0` bounds it from **above** only and Corollary D.38.5c shows no lower bound in the frame's
   invariants exists; (W2) `|n^{½−ρ}| = 1` **iff RH** (and `\inf_ρ\mathrm{Re}\,ρ > 0` is a quasi-RH
   zero-free-strip statement). Both are **zero-location** facts, neither is a Riemann–Roch or
   Hodge-index fact, and the one frame-internal ingredient that looked like a separator — the AM–GM
   polar floor — transports to the falsifier verbatim.
4. **The parting point with `Ξ_a`** — `Ξ_a` satisfies (T1′), the transfer theorem D.34.8, the
   eventual half of Proposition D.34.16, the polar floor and its `\cosh` normal form, and the
   degree/`R`-positivity of the ray, all verbatim and unconditionally. The **only** point of
   divergence is the existence of a primitive compactly supported `F` with `I_∞(F,F) > 0`: a
   **theorem** for `Ξ_a` (Proposition 12.4B, whose hypothesis is automatic — m4), and literally
   **`¬RH`** for `ξ` (Paper 45 Theorem 10.4). The separation *is* the statement, not a step towards
   it.

Per the coordinator's instruction, **no new positivity target inside the frame is proposed**, and
round 1's two suggestions are withdrawn: (a) was already closed by Theorem D.38.3, (b) by Corollary
D.38.5c. The only continuations recorded are outside the frame — Horn A (gated on O-19′/O-18′) and
O-26/(T2) on `B4^{g,0}` — and neither is a positivity clause on `S_0`.

---

## 4. Verification re-run

`python3 scripts/certify_failing_index.py --fast` → `RESULT: PASS`, exit `0`; `--a 0.1` and
`--a 0.45` → `PASS`. No script change was required by any finding (m5 is a README wording repair, not
a computational one); the script already printed "normalised" at the line the auditor flagged.

## 5. Residue

**None from this audit.** All twelve findings are discharged at the statement they touch. Carried
forward from phase 143 and untouched here, as out of scope: **H12** (Theorem D.34.7's last step),
**H13** (one sentence in Proposition D.34.16(iii)), **H14(a)–(d)** (wording and two stale table rows
in `R143_001`/`R143_005`). Open items after this round: O-24 (= RH), O-25, O-26, O-28, O-19′, O-18′,
O-31 (explicit `F_+`, low value). **O-29 and O-30 are closed, negatively.**
