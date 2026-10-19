# CHANGES_197 — Paper 47, integration of phase 197

Backup: `main_pre_197.tex`. New subsection `\subsection{Geometry of decisive premises}` (`subsec:shape-geom`), last
subsection of §`sec:shape`, immediately before §`sec:spec`. No other text changed. No summary/closing chapter added.
Sources: audited versions only (phase-197 memos + AUDIT_197_HOSTILE, REVIEW_BARRIER_EST_001, AUDIT_197_2, AUDIT_197_HOSTILE_3).

Normalisation: everything is written in the paper's weight coordinates v_n = 2a(n)/√n (§subsec:finite); w(F⋆) = (c_{F⋆}(log n))_n,
d_v = Σ|v_n−v'_n| = 2Σ|a−b|/√n. All factor-2 corrections of the audits are absorbed this way (e.g. W_p carries 2k log p p^{-k/2}).

| item | label in paper | source / audit correction applied |
|---|---|---|
| K_T convex = V_T (prop:finite(ii)); half-space over all minimizers, cor:geo-half(i) | PROVED | BARRIER_001 Thm 5; intersection over all minimizers (non-uniqueness) |
| precision in direction w, cor:geo-half(ii) | CONDITIONAL on w(F⋆)≠0 | audit (e) |
| thm:geo-tv, TV precision r ≤ λ_A for measure combs | PROVED | EST Thm 4; hybrid/support-axiom scope remark added; paper's estimate notion is integer-supported (review (a)3) |
| prop:geo-int: κ̂>0, r κ̂ ≤ λ_A+η (relative slack), minimizer form (weakening κ_T≠0 → some c_h(log n)≠0), κ̂ ≥ sup m_T − λ_A − η | (i),(iii) PROVED, (ii) CONDITIONAL; quantitative κ̂ OPEN | review (d) normalisation fixed (relative slack); positivity via lem:cpos |
| prop:geo-bohr exact Bohr defect (general r_{p,k}, Euler α family) | PROVED (numerics mentioned, not used) | D1 Thm 2 + X0 |
| prop:geo-blind first-order blindness | reduction, CONDITIONAL on w≠0 | D1 Thm 4 in the audited form (continuity suffices; not "NO-GO", not "symmetric") |
| thm:geo-split splitting + continuation | PROVED; concave-class sharpness ARGUED | D2 Thm 1, Thm 2 with corrected witness max_s[φ − d_v]; Thm 3 finite-prime rigidity in a remark (Bohr-coefficient proof only) |
| thm:geo-index W1, W1′, W2 | PROVED (ε in W1′ non-explicit) | BARRIER_W_001 |
| rem:geo-codim W3 | (a),(b) PROVED finite-dim, (c) ARGUED | BARRIER_W_001 |
| thm:geo-parity Kronecker parity | PROVED, scope as corrected (σ-closed classes; nonnegative-coefficient class is not σ-closed) | X2 + AUDIT_197_HOSTILE_3 (c) |
| rem:geo-trich classification | ARGUED/CONDITIONAL, "at least one", (ii) = reduction to dual program | AUDIT_197_HOSTILE (a)–(c) |

Not integrated (did not survive or out of scope): Theorem 3 as a theorem, Prop 4 minimality, D1.a, residues R1/R2 as routes,
X3(a) one-sidedness (false), X3(b,d)/X4 beyond one sentence, CIRC-upgrade table, relative constant 16.449.
No equivalence of the target with any other statement is invoked. Compiled with pdflatex ×3: no errors, no undefined
references; 171 pages.
