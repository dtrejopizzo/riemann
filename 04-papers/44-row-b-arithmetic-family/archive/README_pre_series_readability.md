# Paper 44 — Row B: the arithmetic family inside row A

**Files.** [main.tex](main.tex) / [main.pdf](main.pdf) — the paper of record.
[main.md](main.md) — the older working draft; its numbering (3bis.x, 8bis.x, …)
and some of its material are **not** in the tex (see "md/tex divergence"
below). Every theorem number in this README is a **tex** number.
Repair log: [REPAIRS.md](REPAIRS.md).

## Status

* **Label.** `ROW B: WEIL-STRENGTH-COMPLETE` on Paper 43's declared carrier,
  **unconditional** since the author accepted the B.4 and B.7 amendments
  (phase 133, `03-research/phase-133-abc-review-panel/AMENDMENTS_A8_B7_RECORD.md`;
  PLAN.md). B.4 is proved *in degree* (the identification with
  `[Z → Φ_n(1) → Z]` is of degrees, Remark 8.8).
* **Adversarial audit ** (`AUDIT_44_45`): row B closes; defects D-B1…D-B7
  repaired in the tex on  (see the repair log). No statement used
  by later rows changed except the corrected value (9.3) of Cor 9.3 (factor
  `‖h‖²`, archimedean kernel `K_s` on the positive half-line); its qualitative
  conclusions (no limit; negative divergences) are unchanged.

## Main results (tex numbering)

| Result | Content |
|---|---|
| Def 3.6, Thm 3.9 | norm class `Γ_n^rad`; strong monoidal, dagger, bidegree `(n^{1/2},n^{-1/2})`, independence of all choices |
| Def 3.11, Lem 3.12 | smeared radial classes `Γ_h ∈ D_A^rad` |
| Thm 4.1, 4.2, 4.4, 4.7 | radial trace; representing measures; contact locus `Λ(n)n^{-1/2}`; realization in the completion |
| Defs 5.1–5.2, Thms 5.4, 5.7, 5.9 | Frobenius family; inverse semigroup graded by finite prime sets |
| Def 6.1, Thm 6.3, Cor 6.4, Thm 6.11 | smeared Frobenius; exact finite contact `Λ(n)n^{-1/2}h(1/n)` at every level; no archimedean contact |
| §7 (Thms 7.7–7.26) | Möbius cube, `deg_det`, degree law, discriminating test at `p, p²` (B.7 amended) |
| §8 (Def 8.1, Thms 8.3, 8.4, 8.7) | integral shadow `Sh_Z(Frob_n) = [L_S →n→ L_S]`; Möbius cofiber `[Z→Φ_n(1)→Z]`; degrees only |
| Thm 9.1, 9.2, Cor 9.3, Cor 9.5, Thm 9.6, 9.7 | the two Gram forms: Frobenius family carries `W_fin` only; unit-averaged family carries `W_fin + ω_∞`; Frobenius diagonal has no limit |
| Thm 9.11 | `Q_fin` strictly positive on a primitive radial class at every finite chart (one parameter `T` taken large) |
| Thm 10.1 | regularized self-pairing `−log(1/ε)+O(1)` (fixed chart) |
| Thm 11.1, Cor 11.2 | `vol(Z_p^×) = log p` is the unique local normalization (up to one scale) with universal Tate residue |
| Lems 12.1–12.4 | analytic lemmas (trace continuity, discrete approximation, C¹ control, single-frequency computation) |

External input used in the tex: Chebyshev's bound (IK). Nothing else.

## md/tex divergence (flagged)

The following appear in `main.md` (and in earlier versions of this README)
but **not in the tex**, so they must not be cited as results of Paper 44:

* the conditional "transfer theorem" `main.md` Thm 8bis.7 (hypothesis `(H_L)`)
  and its two quarantined classical imports — only the analytic lemmas
  (tex Lems 12.1–12.4) survive in the tex;
* the clause ledger B.1–B.9 and the withdrawal ledger §9bis (W1–W23).

Papers that cite Paper 44 by `main.md` numbers (8bis.x, 3bis.x) should be
re-pointed to the tex numbers above.

## History

Status blocks of phases 131–133 and the  readability revision are
kept in git history (`git log -- 04-papers/44-row-b-arithmetic-family/README.md`);
the R131 construction and audit reports are in `03-research/phase-131-row-b-closure/`.

* **Alignment with repaired Paper 43.** Citations of Paper 43 use its
  repaired tex numbering (Lemma 5.7, Thm 5.12(c), Prop 6.13(a), Conv 6.6, Thm 6.7,
  Lemma 8.12 eq. (76), Thm 11.6(b)). No result of this paper depends on the
  hypothesis (Exc_σ) of Paper 43; see REPAIRS.md.
