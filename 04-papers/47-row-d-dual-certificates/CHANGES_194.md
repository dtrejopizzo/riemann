# CHANGES_194 — integration of phase 194 into Paper 47

Backup: `main_pre_194.tex`. Sources: phase-194 INV_C/E/F/H/I/J/K memos, AUDIT_194(_2), REVIEW_K2, ROUTES-TRIED-INDEX
"Especificación del portador del signo". Audited labels used throughout.

## New section `sec:spec` "What a sign-carrying object must satisfy" (before Open problems, after §shape)
- lem:spec-collapse (window collapse) — PROVED.
- thm:spec-noatom (no measure on log Q equals the window form on P_T; INV_C Thm 4) — PROVED; eq:spec-dlog (Λ only via ∂_σ log, Identity 5) — PROVED.
- thm:spec-gauge (divisor-gauge symbol, H1) — PROVED.
- thm:spec-carrier (gauge invariance, ζ(½+iτ) common factor, O_6 absorbed; K1) — PROVED.
- thm:spec-K2 → Proposition, ARGUED (REVIEW_K2: gap G1 = joint Ω-result for ζ and (p^{-it})_{p≤X(t)}; stated explicitly after the
  argument; mollifier obstruction CONDITIONAL on it). Fixes F1 (m = log(τ/2π)+O(1/τ)), F2 (σ ≥ 2), F3 (alignment bound) included.
  No %K2-REVIEW comment left (review completed).
- prop:spec-intcomb (integer comb ∉ C⁺, H3) — PROVED via lem:wit-conc with γ=1; values at τ=1,2,3 NUMERICAL, not used.
- prop:spec (six clauses): (1) comb-generic/B″ PROVED, Beurling-verbatim class check (G1) CONDITIONAL; (2) cone on log ζ (F2) PROVED;
  (3) integrality (I1/I2) PROVED; (4) sparse-stability (J3) PROVED; (5) FE coupling OPEN, J4 first half PROVED / second half ARGUED,
  K1 PROVED, K2 ARGUED; (6) ∂log crossing ARGUED (F1 PROVED; F classification ARGUED; E2 PROVED same-argument / ARGUED with shifts).
  Cross-refs to Problem~\ref{prob:region} (= Problem (R)): (1)→(3),(11); (2),(3)→(1); (4)→(1),(2); (5)→(2); (6)→(3).
- rem:spec-scope: only proved parts of lem:shape-scale used (never O_4^ε).
## Bibliography
Added Hamburger1921, Holder1887, Ostrowski1920; Titchmarsh1986 (existing) cited for Ch. V bound and Thm 8.12.
## Not integrated (audit verdicts)
INV_A rigidity (retry), INV_B/B_002 (retry/ill-posed), INV_D Thm 3 (Connes local trace, no content), INV_G G1 as a standalone result,
I4 (ARGUED), H residue (restatement).
## Build
pdflatex ×3, no errors, no undefined references; 163 pages (was 159).
