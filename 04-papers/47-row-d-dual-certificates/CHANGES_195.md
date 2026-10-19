# CHANGES_195 — Paper 47, phase 194–195 integration

Backup: main_pre_195.tex. Sources: phase-194 INV_L_001; phase-195 INV_M..T_001, using the audited labels of AUDIT_195, _2 and _3.

## New subsection sec:spec / "Identities on the strip" (label subsec:strip, before "The specification")
- lem:strip-L1: the window symbol is 2∂_σu_S on the line (PROVED).
- thm:strip-L3: Green identity for the functional-equation defect d_S on ½<σ<2 (PROVED, smooth F). Parseval constant is log p (corrected).
  The edge-band reading (valid only on ½<σ<1) is NOT included.
- thm:strip-R1: sourceless Dirichlet-energy identity, every σ_1>½ (PROVED). The remark cites the 1.7e−13 numerical agreement. The normalization
  lemma is not included because its "only if" is false.
- thm:strip-T1: gauged identity (PROVED). Its freedom is a tempered distribution ν, which strictly contains def:PD, as stated in the text.
- cor:strip-T1p: entire gauge q_T, ψ = σ_T exactly (PROVED).
- thm:strip-T3: no contractive gauge, PROVED for T ≤ ½log5 via thm:log5A, CONDITIONAL beyond.
- thm:strip-T4: method theorem. (i) gives c ≤ λ_A, and c ≤ λ_P when ν is a finite measure (prop:weak). (ii) finite-atomic certificates
  give expansive gauges (PROVED). The supremum over finite-measure gauges is λ_P (thm:D1). Outside the declared class: argued only.
- prop:strip-R4: Hermite–Biehler fails on (½,1) for every finite S and every finite Beurling system (PROVED).
- prop:strip-Q2: exact band formula (PROVED), plus the remark that the log resums smooth-number sums to prime powers.
- prop:strip-S1: place-splitting of the singular data (PROVED). prop:strip-S2: frozen comb {2,3,4}, closed form PROVED, −8.314157 numerical.
- Remark: curvature/Poincaré ceiling g_T + ess inf W_T < 0 at ½log3, constants numerical.
- Remark: real stability (M1/M2). New bibitem Branden2007.

## Other edits
- prop:spec clause (5): the strip identities meet the wording of the clause but are comb-generic, fail clause (1), and their gauge
  freedom returns the dual certificates.
- cor:margin1: footnote saying that 42/e belongs to the test family (cutoff 21 < γ_2) and is not a sharp rate.

Excluded: the P2 edge band on Ω, the normalization "only if", Q1(a), the combined claim (argued), and the bootstrap/Mazáč material (only ARGUED).
Compile: pdflatex ×3, no errors, no undefined references, 166 pp.
