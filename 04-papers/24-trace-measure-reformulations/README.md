# Trace and measure reformulations of the Riemann Hypothesis through the discrepancy measure of the on-line projection

The paper studies the measure dν = (|ζ|² − |ζ_on|²)(½+is) dm_∞(s), where ζ_on is the on-line projection of ζ from Paper 22 (every off-line zero moved horizontally onto the critical line, with the normalisation of Paper 22) and dm_∞ is the archimedean measure. It records that dν ≥ 0 and dν = 0 ⟺ RH (both from Paper 22) and lists reformulations of RH as the vanishing of positive functionals of dν.

## What the paper proves or observes
- `thm:dominance`, `cor:dnu`: R = |ζ/ζ_on|² ≥ 1 on the critical line, so dν ≥ 0, and dν = 0 ⟺ RH (recalled from Paper 22). A remark shows the inequality fails for the canonical Hadamard normalisation (exact limit of the factor computed, with a numerical example).
- `thm:eight`: eight conditions (zero measure, Nevanlinna transform, trace, Jensen excess, L² distance, relative entropy, total mass) are equivalent to RH; all are trivial restatements of dν = 0.
- `prop:lower`: under ¬RH, T_λ = ∫ W_λ dν > 0 for every λ, with an explicit lower bound from one off-line quadruple.
- `thm:trace-crit`: T_λ = 0 for a single λ ⟺ RH (trivial).
- `thm:ff`: the function-field analogue dν^C vanishes, by Weil's theorem; the comparison of §6 is heuristic.

Known: dν ≥ 0 and dν = 0 ⟺ RH are in Paper 22; determinacy of the m_∞ moment problem is due to Connes–Consani–Moscovici. New here are only the listed reformulations and the lower bound; nothing here gives information on RH.

## Files
- [main.tex](main.tex) — LaTeX source.
- [trace-measure-reformulations.pdf](trace-measure-reformulations.pdf) — compiled paper (6 pages).
