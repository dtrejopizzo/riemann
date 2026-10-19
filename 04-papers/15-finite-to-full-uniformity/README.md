# Paper 15 — Finite-to-full positivity is a uniformity gap: a criterion, a Hodge–Riemann stability theorem for towers, and the place of ζ

For the ξ-function every finite-order positivity (Turán inequalities, hyperbolicity of each fixed-degree Jensen polynomial, each finite total-positivity minor) is unconditional, while full-order positivity is not known. The paper identifies the gap as a quantifier-order (uniformity) gap rather than a logical-implication gap, characterizes when "eventually at each order" upgrades to "uniformly at all orders", and proves a Hodge–Riemann stability theorem for towers of forms. It places the ζ-hierarchy at the degenerate borderline of this dichotomy. All results are independent of the Riemann hypothesis.

## Main results
- `thm:crit` (Criterion): eventual implies uniform positivity iff the hierarchy is finite type (scale-free) or has bounded threshold. PROVED.
- `cor:fin`: no finite-to-full gap iff finite type or bounded threshold; reading for the ζ-hierarchies. PROVED.
- `prop:exist` (Existence): bounded-threshold hierarchies that are not finite type exist (converging strictly positive measures). PROVED.
- `thm:overRH`: uniform convergence of Jensen polynomials to the Hermite limit at rate o(1/d) is strictly stronger than RH; the RH-equivalent relaxation is circular. PROVED.
- `thm:hr` (HR stability) and `cor:towerbridge`: a convergent Hodge–Riemann tower has uniform positivity iff its limit form is strictly definite (extends Adiprasito–Huh–Katz from one object to families). PROVED.
- `prop:rate` (Rate transfer): explicit threshold from the convergence rate; threshold growth in the degenerate case. PROVED.
- Appendix: numerical illustration of the stability dichotomy. NUMERICAL.

## Files
- `main.tex`, `main.pdf` — source and compiled paper.
- `code.py` — HR stability dichotomy for definite vs degenerate limit towers.
- `code2.py` — degenerate borderline example: Hankel moment eigenvalues and threshold growth.
