# R131.019 — Lead final audit of Paper 44 (rounds 3–7) and the closure decision

Author: session lead (Fable 5.1), adversarial audit of record. Date: 2026-09-12.
Supersedes the conditional decision R131.005 (the B.4 amendment has since been
accepted by the owner, 2026-09-12; Paper 44 §6.2a′, PLAN §6 item 4).

## 1. Grep verification of round 7 (the auditor's procedural finding)

Run by the lead on the final `main.md` (5524 lines):

| item | command / result |
|---|---|
| A1 | `grep "lacks the indefinite"` → lines 331, 4986 only, both inside round-7 notes quoting the deleted sentence ✓ |
| A2 | banner region `grep "LINEARLY\|rate computed\|8bis.4(iv)"` → only the round-7 note quoting what was removed ✓ |
| A3 | `grep "modulo one named"` → 3774, 3918, 4993, all quoting notes ✓ |
| A4/p9 | every `(8bis.NN)` referenced is defined; no tag assigned twice (the three "duplicates" of a naive scan are end-of-line references, not tags) ✓ |
| A5 | `grep "bounded frequency and tilt"` → empty; (8bis.14d) carries both error terms ✓ |
| p5 | §11 says two imports; the only "three" left is the historical round-5 §10 block, which is accurate as history ✓ |
| p6, p7 | superseded Cramer order gone; "up to the fixed sign convention" survives only in the p7 quoting note; (8bis.14e) states `I_∂ = −Q` without hedge ✓ |
| (Wgr) | every occurrence is inside a withdrawal, refutation or historical note ✓ |
| numerics | `verify_131_contacts.py`: ALL CHECKS PASS, ROUND-4/5/6 CHECKS PASS ✓ |

## 2. What the lead re-derived across rounds 3–7 (record)

R131.009 (round 3: §3ter, §6bis), R131.012 (round 4: F1 repair, Thm 8bis.1b,
8bis.1e, 8bis.8; findings LF1–LF4), R131.015 (round 5: Cor 8bis.1b′,
Thm 8bis.4a, Lemma 8bis.6; findings LF5 — the false import (Wgr) — and LF6),
and this file (round 6–7: Lemma 8bis.6a, Lemma 8bis.6b, the conditional
Thm 8bis.7, all checked against the lead's own computations in R131.015 §2).
Every lead finding was either repaired or refuted by the builder with a
counterexample the lead accepts (the sub-exponential prefactor; the sup-norm
versus `C¹` size of the correction; the `2Re(A²)` coefficient under `Π`).

## 3. Renaming test (final)

Row B's content — the Frobenius family as Haar measures of fixed-point strata
with a true unit and an inverse semigroup graded by prime sets; supports that
determine `(n, P(n))`; finite contact exact at every level and zero for
composite `n` because the support meets no stratum; the integral shadow
`Sh_Z` on objects with its transitivity triangle and Möbius cofiber; the two
Gram forms and the theorem that the Weil kernel is the Gram form of
`Frob ⋆ Δ^{rad}` while the Frobenius family alone carries the finite half;
`Δ·Δ = −∞`; the uniqueness of `vol(Z_p^×) = \log p` given a universal Tate
residue — is not stated or implied by the scalar explicit formula. The one
statement that *is* Weil's criterion (Thm 8bis.4(iii)) is labelled
`CLASSICAL`, says so in words, and is used by no clause. **Pass.**

## 4. Decision

Contract (Paper 44 §2; row-A closure rule): every clause proved on Paper 43's
declared carrier, and the audit of record finds no renaming. B.1–B.3, B.5,
B.6, B.8, B.9 `PROVED`; B.4 `REFUTED AS STATED` and `PROVED AS AMENDED`
(amendment accepted by the owner 2026-09-12, now proved on objects in degree,
Thm 6bis.4); B.7 `PROVED` by the lead's ruling R131.005 §2, with the hostile
auditor's dissent (`PARTIAL` as a mechanism) recorded verbatim beside it. The
hostile auditor of record grades the label **EARNED** (R131.011, R131.014,
R131.017), conditional on apparatus items now verified in §1.

    ROW B: WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier
           (§14.0a–b), as a theorem about row A's declared trace.
           B.4 amended (owner, 2026-09-12); B.7 by lead ruling with
           dissent recorded. Granted by the lead as audit of record,
           2026-09-12, after seven builder rounds and five hostile audits.

Recorded beside the label (mandatory, in the paper and the ledger):

1. **Reservations.** R1, R3, R6 dissolved by theorems (Thm 3ter.4(iv),
   3ter.12, Rem 3ter.4a; true unit and inverse semigroup); R2 dissolved in
   degree on the monoid, refuted at object level (P123.022), not open; R4
   dissolved in the only available form — uniqueness of the normalization
   given a universal Tate residue, up to one global scale (Thm 8bis.8), the
   requirement being an axiom of the carrier, not a theorem; R5 answered in
   the form that is true — the Weil kernel is the Gram form of `Frob⋆Δ^{rad}`
   (Thm 8bis.1e) — and not dissolvable, because it asks for a sign.
2. **What row B does not deliver.** No sign, no positivity, no `𝓝_∞ = 0`, no
   statement about zeros outside Thm 8bis.4(ii)–(iii) and §8bis.3–8bis.4. Two
   quarantined `CLASSICAL` imports (Weil's criterion/explicit formula;
   Chebyshev), each used by no clause and deletable without changing a
   verdict. The sign is row D's.
3. **The three quantifiers.** The interface with Weil's criterion is a colimit
   statement (`T_∞` on `D_A^∞`) and is false at a finite chart; no divergence
   rate of the Frobenius diagonal is convention-free — what is stated is that
   `I_A(Frob_n, Frob_n)` does not exist; Thm 8bis.4a and Thm 8bis.2 are
   fixed-chart theorems (the colimit version of 8bis.4a is `OPEN`).
4. **Withdrawals of record.** `(Wgr)` — a `CLASSICAL` import carried in
   rounds 4–5 — is withdrawn as **false** (Lemma 8bis.6b, §9bis W23). The
   implication "positivity on Dirichlet-polynomial profiles ⟹ RH" is `OPEN`
   and not claimed: Thm 8bis.7 is a conditional transfer theorem, (a)
   `PROVED`, (b) `CLASSICAL`, (c) `OPEN` under the explicit hypothesis
   `(H_L)`. The withdrawn round-3 and round-4 claims are W16–W23.
5. **Honesty about Weil's proof.** Row B, like row A, is a construction of
   the objects Weil's proof needs on `Spec Z` — the correspondences, their
   Gram form, the integral shadow — and not of the section theory `H⁰` with
   nonnegative dimension that turns Riemann–Roch into an inequality. That
   remains the content of RH and belongs to row D.

## 5. What row B hands to row C (Paper 45)

Thm 9.1 (the prime packet as a theorem of row B)
**[phase 133, PANEL_2 MINOR-4: read as **§9.1**, whose content is Thm 3bis.7;
Paper 44 has no Theorem 9.1.  The decision itself is unchanged.]**; the withdrawal of the
`n−1` obligation (§9bis W1–W3; Paper 45 §11 must be corrected); Paper 43
Thm 10.8b (Mertens, `CLASSICAL`); the two-slice theorem (Frobenii off
`Im j_∞`, archimedean Frobenius off every `Im j_q`); Thm 8bis.1e; and the
convention (C1) that any statement about all primes is a colimit statement.

## Addendum 2026-09-12 (phase 133)

**[phase 133, amendment accepted 2026-09-12]** The owner accepted the
amendment of B.7 proposed in
[`PANEL_SYNTHESIS.md`](../phase-133-abc-review-panel/PANEL_SYNTHESIS.md) §4.2;
the lead's ruling (`R131.005` §2, adopted above) is superseded by the owner's
decision; the grading now reads `REFUTED AS STATED + PROVED AS AMENDED`; the
label stands unconditionally. Amended clause text, as accepted: "the
discriminating test at `p, p²` is `PROVED`; the mechanism is located on the
carrier (shell volume, trivial fixed-point weight, Thm 6.5) and on the
`Z`-model (deck `μ_n`, Thm 6.4(iv)); a map between the two locations is
`REFUTED` on a `C`-linear carrier (P123.022), so the clause's demand for a
single mechanism producing the cyclotomic factor is unsatisfiable as stated."
The hostile auditor's dissent is kept verbatim in Paper 44 §10 as history and
Remark 6.5a′ is unchanged. No theorem, proof or other grading changes.
Record: `../phase-133-abc-review-panel/AMENDMENTS_A8_B7_RECORD.md`.
