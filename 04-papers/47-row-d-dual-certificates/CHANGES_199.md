# CHANGES_199 — Paper 47, phase 199 integration

Backup: `main_pre_199.tex`.

New section `\section{The exterior form and the leakage lemma}` (`sec:ext`), inserted after `sec:spec` and before
`sec:open` (pp. 159–165 of 179). Organization paragraph updated. Bibliography: added Guo2026 (Zenodo 23297284),
Fuchs1964, SlepianPollak1961.

Contents (labels as in the audited sources):
- def:ext (admissible f, leakage, summation map E, aliasing tail, reflected tail via Z, Z_log, gauge, ℓ(g), complete form on the line with full comb, v_n = 2Λ(n)/√n).
- lem:ext-mob Möbius bijection — proved.
- thm:ext-half half-line identity (with Λ∗1 = log collapse) — proved given Guo Lemmas 4.2–4.4, Thm 4.5 (cited).
- rem:ext-killing killing-term correction; zero sum moves to the tail — proved.
- prop:ext-gauge gauge = radical, ℓ = 2 dist² — proved given Guo Lemma 4.4.
- lem:ext-ellbound ℓ(g) ≤ C₁N²‖g‖² — proved (constant re-derived: 16N(1+4N‖β‖²), even-extension factor included).
- prob:ext-L leakage lemma — OPEN; note that the version with leak(f) is false (gauge).
- prop:ext-consol consolidated form (★★), Stieltjes (ã) spelling, prolate-matrix spelling — proved equivalences.
- prop:ext-univ universal form — proved.
- thm:ext-margin leakage lemma ⇒ λ^W_T ≥ (κ/4)N^{−A₀−1}(1−χ₀(2πN))‖g‖² for every T — proved, conditional on the lemma.
- prop:ext-base base case 5 ≤ N ≤ 15, A₀ = 2 — proved given Mori15 (cited).
- lem:ext-hf high-frequency coercivity — proved, comb-generic.
- thm:ext-line, thm:ext-EM, prop:ext-residue (with the χ(s)ζ′(1−s) rewriting), prop:ext-pointwise, prop:ext-dual — proved.
- thm:ext-mirror Poisson mirror — proved for C_c^∞(1,∞) data, conditional for Paley–Wiener tails.
- prop:ext-contour off-line contour form; prop:ext-pairs pair expansion, comb collapse, indefinite diagonal class (on C_c^∞) — proved.
- prop:ext-deep deep quasimode 2+γ−log4π = 2(ξ′/ξ)(1), four-piece anatomy — proved given PNT; rem:ext-deep zero-sum value Σ1/(ρ(1−ρ)), test object only.
- prop:ext-K1b minimal-leakage admissible prolate combination — proved given Slepian–Pollak/Fuchs.
- prop:ext-flow window flow dN/dT, odd Weil distribution; continuation implication conditional, extra inequality open.
- subsec:ext-constraints: nine constraints stated mathematically.

Not integrated (unaudited or downgraded labels): S.1(d) (formal), S.3–S.5 (argued), cΛ threshold 0.785, κ-band index readings,
P.4 numerics, conjecture (C_G). No sign is claimed; no statement of the paper changes label.
Verification against the paper's own definitions: eq:symbol (m, v_n, contacts), eq:W (A, B, 2Re AB̄), Φ_F, thm:A (Lévy form,
killing), lem:roughEF, thm:geo-tv, thm:log5W, Mori15 citation; Fourier convention for additive-line functions declared locally.
Compiled pdflatex ×3: 179 pages, no errors, no undefined references, no overfull boxes (one fixed in the new section).
