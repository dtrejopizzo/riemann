# Records cleanup — («leave these records perfect»)

Model followed:
`03-research/phase-185-crossword/R185_005B_BR_WITHOUT_EQUIVALENCE.md`. No new mathematics. No grid symbol
changes; no contact with the sign; row D: OPEN.

## 1. Rewrites into D-only form

| file | what was done |
|---|---|
| `ROW-D-REDUCED-STATEMENT.md` | §1 rewritten: D stated as an objective; former E1–E6 → **D-1…D-6**, label **REF-D** (internal reformulation of D, equivalent to D by a program theorem; sources and labels preserved); witness as the sole statement about zeros (lem:roughEF, prop:witness, lem:contA). §6 rewritten: "that statement is D itself"; options (A)/(B) kept as a historical decision with a note: (A) was a statement about the map, not a classification of D; under the premise the map is not a stop. Loose lines: §2 "E1 ⟺ E2" → "D-1 ⟺ D-2"; §4.5 Rem 19.25c "⟺ RH" → "⟺ D (REF-D)"; §7 "would prove GRH" → "row D for every number field"; §8 "forces RH together with simple zeros" → "forces D together with simplicity of the zeros". Dated editor note at the start. |
| `CROSSWORD-TO-D.md` | §0–§1 rewritten in full (REF-D cluster, D-1…D-19 with correspondence D-k = former E_k; quantifier warning in terms of the witness; verdict without external comparison). §2–§5 and addenda: line-by-line substitution (56 replacements verified one by one): "⟺ RH" → "⟺ D", "under RH" → "under D (without a witness)", "¬RH" → "¬D", "E1" → "REF-D"; I1 (catalog) and §3.1 with a note: "being a reformulation is not grounds for closure". REF-D label defined in the header. Dated editor note at the start. After the rewrite: 0 occurrences of "RH" or "E1" outside the editor's note (grep). |

Historical memos from the plan that used the equivalence or "E1" as a criterion: **intact**, with a dated editor note at the start
("use without effect; current reading: …"): `PLAN.md`, `INVENTORY-PHASES-168-184.md`,
`ROW-D-CLOSURE-PLAN.md`, `STATE-AT-PHASE-149.md`. Historical mention only (no note):
`CORPUS_COVERAGE.md` l.215 (cites the veto in OPTIONS.md and corrects it), `CORPUS_CHECK_ROW_D_PLAN.md` l.318 (cites M1).
No findings: `PATH-TO-D`, `SIGN-REAUDIT`, `SUPPORT-DESCENT-TEST`, `FIRST_CAMPAIGN`, `ROW-D-COMPLETION-PLAN`,
`ROW-D-MAP`, `ROW-D-SYNTHESIS`, `PLAN_PRIORITARIO`. `03-research/phase-186-toolbox/README.md`: only the premise (l.4)
and the note on R186_114 (l.226); clean. `03-research/phase-187-pattern/*.md`: clean (0 hits of "RH", "E1", "⟺").

## 2. Corrections C-W1 and C-W2 (dated notes, no silent rewriting)

- **C-W1** (R186_034 Thm 2.1(iv)/Thm 2.2 mix extremals). Correct: λ_A ≥ (1−β_max)Pos(h*) and λ_A ≤ (1−β_max)Pos(u₁),
  u₁ an extremal of the pencil; that is, **λ_A/Pos(u₁) ≤ 1−β_max ≤ λ_A/Pos(h*) ≤ λ_A/c_P**. Note applied in R186_034 (§0 item 3,
  Thm 2.1(iv), note after the proof, Thm 2.2, §6 proposal) and in the phase-186 README (entry R186_034).
- **C-W2** (R186_042 Thm 2.3). With J = Q₋ − Q₊: Q₋ − βQ₊ = ½[(1−β)Q **+** (1+β)J]; β = (1+cos 2φ)/(1−cos 2φ) = **cot²φ**,
  φ the angle to ran Q₋. Correct statement β_j = (s₋/s₊)cot²φ_j; Cor 2.4 already had the correct form. Note applied in R186_042
  (§0 item 2(iii), Thm 2.3 statement and proof, note after the proof) and in the phase-186 README (entry R186_042).
- **Grid**: `R162_2300_MASTER_GRID.md` §8 log, new entry **43**; entries 32 and 39 are to be read with these
  corrections. No other grid or crossword entry cites "tan²" or the interval [λ_A/Pos(h*), λ_A/c_P] (grep).
- **Verification against the definitive Paper 46 main.tex**: `thm:wh-pencil`(ii)–(iii), eq:wh-sandwich (λ_A/Pos_T(u₁) ≤ 1−β₁ ≤
  λ_A/Pos_T(h*_T) ≤ λ_A/c_P; proof by Rayleigh at u₁ and at h*) and `thm:wh-angles` (𝔫₀/𝔭₀ = (s₋/s₊)cot²φ(Qu), cos²φ =
  ‖Q₋v‖²/‖v‖²; `cor:wh-nogap` β_j = (s₋/s₊)λ_j/(1−λ_j)): **agree** with the corrections. Manual check: the
  lower bound follows from 𝔞(u₁) = (1−β₁)Pos(u₁) ≥ λ_A, the upper one from Neg ≤ β₁Pos at h*; cot² = cos²/sin² = λ/(1−λ).

## 3. Kahane–Mandelbrojt reference (Paper 46)

Verified (numdam, WebSearch): J.-P. Kahane, S. Mandelbrojt, *Sur l'équation fonctionnelle de Riemann et la
formule sommatoire de Poisson*, Ann. Sci. École Norm. Sup. (3) **75** (1958), no. 1, 57–80, DOI 10.24033/asens.1066
(numdam ASENS_1958_3_75_1_57_0). The `\bibitem{KahaneMandelbrojt1958}` in main.tex already had the correct venue/year/pages;
"no. 1" and the DOI were added. `DEFINITIVE_CHANGES.md` l.43 updated (the "to confirm" item closed).

## 4. Overfull boxes in Paper 46 main.tex (done last)

main.tex re-read right before editing (md5 0e5763f9… identical to the one at the start of the round: no concurrent change
between the reading and the editing); backup `main_pre_overfull.tex.bak`. 11 local edits, without changing any
formula: eq:m → `split` (C₀ on the second line); lem:mbounds (iii) → display; bound on the atoms (l.≈1580) → display;
𝔖(T) → `aligned` on two lines; E_edge/ε_p → `gather*`; Lev(F)/κ(x) → `aligned`; subsec:sl-split paragraph → `{\sloppy…\par}`;
eq:posext → `split`; matrix 𝖱 → `gathered`; proof of the bordered Schur Prop. (App. A) → `\sloppy`; formula for
⟨𝒢e_i,e_l⟩ ("The computation") → display. pdflatex ×2: **128 pp., 0 errors, 0 undefined references, 0 multiply
defined, 0 overfull boxes** (mild underfull ones remain, the largest badness 3919 in the proof with `\sloppy`).
