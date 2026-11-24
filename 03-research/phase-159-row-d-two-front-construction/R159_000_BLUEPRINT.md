# R159_000 — Blueprint, phase 159: two fronts

Two groups working in parallel, each with 10 parallel tracks plus an audit panel of 5, at the standard of
Connes, Tao, Consani; do not stop until one of the two objectives is fully constructed.
* **G1 — THE OBJECT (OT-5′):** a carrier over Spec Z (the analogue of Weil's surface C×C) with a positive form defined
  BEFORE the spectrum and without using the zeros, whose compatibility with the flow/Frobenius is proved, and whose
  Lefschetz formula is the explicit formula of ζ (R158_001 object test OT-1…OT-12, as amended by R158_003).
* **G2 — THE MECHANISM:** an argument that uses the EXACT values of Λ(n), is uniform in T, has no margin and no truncation,
  and yields `∀T: λ^A_T ≥ 0` (or `λ^W_T ≥ 0`) — the "para todo T" arrow of the map.

## Premises of record (three statements that the record contradicts; these must be used)
1. The proved sign for ζ: primitive form `T ≤ log 2` (Paper 42); complete form `T ≤ ½log2` classical and `T ≤ 0.8`
  (Zhu, cited). **Nothing is proved for T > 0.8.** Each window is decidable in principle (`prop:finite`), but the margin is
  `≤ 4·10⁹·T·e^{−15.449T}` (`thm:margin`).
2. **No finite set of zeros — successive or random — carries a certificate** (`thm:finZ`: any finite symmetric multiset).
  The "100 random zeros" idea is admissible only as a probe of WHICH infinite structure is needed.
3. The "series equation that gives all results without the full series" exists: it is the explicit formula (Λ ↔ zeros).
  The positivity has to be extracted from the prime side of it.
Success criterion: a construction/proof that survives the audit panel (≥ 4 of 5) with every step checked. It would be a
proof of RH; the panel must treat it with that level of scrutiny. Failure is reported as failure.

## Mandatory reading
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-REDUCED-STATEMENT.md` (§1–§8);
`03-research/phase-158-row-d-mw5-object/R158_001_SPEC_SHEET.md` (G1: OT list, C1–C27);
`03-research/phase-157-row-d-mechanism-search/R157_000_BLUEPRINT.md` (F1–F5) and `R157_002` (the 61-row table: do not
resubmit an excluded or equivalent candidate without saying what is different); Paper 46 `04-papers/46-row-d-sign-radial-intersection-form/main.tex`
(eq:W, P_T, thm:Z, thm:finZ, thm:SC, cor:void, rem:resweights, thm:margin, thm:arena, thm:parityschur, cor:convfail, lem:Rrig);
Paper 47 `04-papers/47-intersection-frame-defect/archive/main.md` (Thm 19.25, Cor 19.25b, §21.7, T1 = Thm 18.1 + Rem 18.1a, T2 = Thm 18.16, §28.3a–b, §28.4).

Files: construction notes `G{1,2}_B{k}_R{r}.md`, panel notes `G{1,2}_P{k}_R{r}.md`, in this folder.
