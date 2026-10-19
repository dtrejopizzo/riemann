# Phase 165 — critical interlacing and the detection theorem

**Status:** closed (single round, 4 memos; audit R165_190); **geometric branch refuted; T_c bracket PROVED; (★_cell) OPEN.**

## Purpose
After phase 164 (every route returns to (★_cell)), locate T_c relative to the Landau window of the off-line
zero (detection theorem, Det±) and decide whether critical interlacing of the witness's nodes with the on-line
zeros pulls the quartet out of the cone (cell 7A, grid §6 item D.16-γ). Cells: 7A, 7D, 7E, 2A.

## Files
- `R165_000_PROPOSAL.md` — initial proposal (Det+, Det−, interlacing, node flow). Corrections in R165_190: §1 (T_c is not pinned to γ*), §2.1–2.2, §2.3.
- `R165_101_DETECTION_PLUS.md` — **Det+** PROVED (clustering caveat): T_c ≤ min_ρ τ(ρ), τ ≤ T_L(γ)+½log(π/2)+o(1), by dividing ξ by its quartet and truncating the Riemann–Pólya kernel.
- `R165_102_DETECTION_MINUS.md` — **Det−** false for large δ*Λ* (Thm 1, sub-Landau detection); contact is decided by min_ρ T_det (Cor 2(c)); false for M_m. Residuals O102.1, O102.2, O701.1–3.
- `R165_201_CRITICAL_INTERLACING.md` — exact phase identity (Thm 2, Cor 2.2; sign variable ω(E) = Rem 4.8a); **interlacing ⇏ quartet off the cone** (Thm 3(a), sin/cos).
- `R165_202_NODE_FLOW.md` — node flow: no jumps, real-rooted at every simple T, quadrature and Cauchy at every T, separation by loaded zeros (E1); "contact ⇒ EC" DEAD.
- `R165_190_AUDIT.md` — audit; authoritative labels.

## Result
Bracket **0.8047 < T_c ≤ min_ρ τ(ρ)** (PROVED, clustering caveat). Det− DEAD as a route. Geometric branch refuted. Residual: ω(E) at contact = Rem 4.8a. (★_cell) and row D: **OPEN**.
Editor (R164_301 §11): grid part 16 (997 routes, ■10 ◩20 ◧34), R163_401 v10 (§4.11(g)), Paper 48 ("Phase 165" paragraph).
- : continued in phase 166 (closed, R166_190): jet hierarchy (Re G(t_q)² = jet k=−1), ω(E) = global phase; five mechanisms DEAD; requirements (i)–(iii). See ../phase-166-omega-closure/README.md.
