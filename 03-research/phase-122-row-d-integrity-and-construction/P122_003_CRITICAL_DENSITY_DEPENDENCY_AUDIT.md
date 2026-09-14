# P122.003 — critical-density dependency audit

## Verdict

The faithfulness step in
`P121_CRITICAL_NEGATIVE_HALF_RESIDUE_GATE.md` needs only

\[
 N_{0,\mathrm{simp}}(R)\gg R\log R,                 \tag{0.1}
\]

where the left side counts simple zeros of `zeta` on the critical line up
to ordinate `R`.  This is an old unconditional theorem and does not depend
on any 2026 preprint.

## Stable input

Conrey's 1989 theorem proves that more than `2/5` of the nontrivial zeros
of the Riemann zeta function are simple and lie on the critical line:

J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta
function are on the critical line*, Journal fuer die reine und angewandte
Mathematik **399** (1989), 1--26,
DOI `10.1515/crll.1989.399.1`.

Together with the Riemann--von Mangoldt asymptotic

\[
 N(R)={R\over2\pi}\log {R\over2\pi}-{R\over2\pi}+O(\log R),
\]

this implies (0.1), which is all Corollaries 3.1 and 3.2 of the phase-121
residue note use.

## Why this closes the cited subdependency

For compactly supported `F`, the transform `K_F` is a Cartwright entire
function of finite exponential type.  If it is nonzero, its zeros in a
disc of radius `R` number only `O_F(R)`.  Vanishing at every simple
critical-line zero would instead give `gg R log R` zeros.  Therefore
`K_F` is identically zero, and transform injectivity gives `F=0`.

No numerical value beyond a fixed positive proportion is used.

## 2026 citation defect

The phase-121 note formerly attributed arXiv `2608.13637` to
"Claude/Anthropic".  The arXiv record lists Levent Alpöge and Ralph Furman
as the authors of *More than two thirds of the zeta zeros are simple and
on the critical line*.  Its stronger bound is unnecessary here.  The
phase-121 text has been corrected to use Conrey as the proof dependency
and mention the newer work only as context.

## Remaining logical gap

This audit certifies only the **faithfulness** implication

\[
 \bigl[K_F(i\gamma)=0\text{ at all simple critical zeros}\bigr]
 \Longrightarrow F=0.
\]

It does not prove that a first-contact state has those vanishing residues.
That oriented equality-state law remains the actual open gate in row (d).
