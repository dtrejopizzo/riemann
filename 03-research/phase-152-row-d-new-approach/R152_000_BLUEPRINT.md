# R152.000 — Blueprint: phase 152, round 0 — feasibility of two never-analyzed non-positivity mechanisms

positivity, Deligne families are exhausted (Paper 46 Parts I–IV; phases 150–151). Every idea is checked against
the corpus before anything is built. This round is FEASIBILITY: its output is, for each mechanism, either a
precisely formulated statement (P152.A / P152.B) whose truth would yield a zero-free strip or RH and which is NOT
a restatement, or a theorem/argument of death with the exact obstruction. No sign is claimed.*

Read first: `05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-CLOSURE-PLAN.md` §§8–10;
`03-research/phase-151-row-d-the-bridge/R151_005_CLOSING_DECISION.md` §2; `04-papers/46-intersection-frame-defect/archive/main.md`
§28.2–§28.4 (the wall and the six reopening clauses); `03-research/phase-37-physics/111-target-l8-is-an-unconditional-bound.md`
§3.2; `NO-GO-LIST.md` MW-1..MW-5, NG-E1 (per-place indefiniteness), NG-C1/MW-3 (Hasse–Minkowski).

## A. Resonances of the modular surface and the Dolgopyat / fractal-uncertainty gap mechanism

**Facts to establish with references (IMPORTED/CERTIFIED as appropriate).** (1) The scattering determinant of
`PSL₂(Z)\H` is `φ(s) = √π Γ(s−½)ζ(2s−1)/(Γ(s)ζ(2s))`; the resonances (poles of the meromorphic continuation of
the resolvent / of `φ`) in the Eisenstein sector are `s = ρ/2` for the nontrivial zeros `ρ` of `ζ`, so **RH ⟺ all
Eisenstein resonances lie on `Re s = ¼`**, the symmetry line of `s ↦ ½ − s̄` (functional equation). (2) The
Maass–Selberg relations give exactly the trivial region (no poles of `φ` in `Re s > ½` off the real axis ⟺
`ζ(w) ≠ 0` for `Re w > 1`) — state and prove that this is all they give (the corpus's conclusion 2 in automorphic
clothing). (3) Bourgain–Dyatlov (Ann. Math. 187 (2018)): for every convex cocompact hyperbolic surface there is
`β > 0` with only finitely many resonances in `Re s > ½ − β` (essential spectral gap beyond the unitary
threshold), proven via the fractal uncertainty principle (FUP) for the limit set (Ahlfors–David regular,
`δ < 1`), without any positivity. (4) Dolgopyat (1998) / Naud (2005) / Baladi–Vallée (2005): oscillatory
cancellation in transfer-operator iterates (uniform non-integrability) gives resonance-free strips for
dynamical zetas, including the Gauss-map transfer operator near `Re s = 1` (Mayer: `Z_Selberg(s) =
det(1−L_s)det(1+L_s)`).

**Questions to answer (each with a proof or a precise obstruction).** (Q1) For the modular surface `δ = 1`
(finite area, cusp): does FUP degenerate (no porosity), and is that degeneration exactly the statement that the
Eisenstein resonances fill `Re s = ¼` with density `~ log T`? (Q2) Is there ANY dynamical/microlocal
mechanism (not positivity) that constrains resonances of finite-area surfaces beyond Maass–Selberg? Survey:
Selberg's `3/16` (that is L²-spectrum, not resonances), Sarnak's and Zworski's expositions, Dyatlov–Zahl,
Dyatlov–Jin (FUP for porous sets), Nonnenmacher–Zworski; state honestly if the answer is "none known". (Q3)
Arithmetic replacement for fractality: Hecke operators act on Eisenstein series (`E(·,s)` is a Hecke eigenform
with eigenvalue `p^{s−½}+p^{½−s}`); Bourgain–Lindenstrauss entropy bounds / Lindenstrauss AQUE use Hecke
recurrence to forbid concentration of eigenfunctions. Formulate the analogous non-concentration statement for
the resonant states `E*(z, ρ/2)` and determine whether it (i) is meaningful for non-`L²` states, (ii) implies
anything about `Re ρ`, (iii) is circular (Luo–Sarnak QUE for Eisenstein series uses bounds on `ζ`). (Q4) Gauss
map: `det(1 − L_s)` vanishes at `s = ρ/2`; Baladi–Vallée's Dolgopyat estimate lives near `Re s = 1` (trivial for
`ζ`); is there any obstruction of principle (not just of technique) to a Dolgopyat estimate for `L_s` on
`Re s ∈ (¼, ½)`, where the operator must be taken in its meromorphic continuation (Lewis–Zagier / Mayer on the
disc space)? Identify where the phase-coherence (UNI) hypothesis fails or holds for the Gauss map's temporal
distance function.

**Kill criterion A.** If (Q1) is yes and (Q2) is "none known" and (Q3) is circular or empty and (Q4) shows a
structural obstruction, mechanism A is DEAD for the sign and is recorded with the four reasons. Otherwise
formulate **(P152.A)**: the exact statement, its gates (must fail for `Ξ_a`: no modular surface has `Ξ_a` as
scattering determinant — say what plays its role; `Ξ_Q`: Epstein zetas DO appear as scattering determinants of
other lattices/orbifolds? check Davenport–Heilbronn-type Epstein functions vs Eisenstein series of `GL₂` over
imaginary quadratic fields), and its corpus-independence.

## B. Poineau's Berkovich spectrum `M(Z)` and the Frobenius lattice as its integer points

**Facts to establish.** (1) `M(Z)` (Berkovich spectrum of `Z` with the trivial norm): a tree with root the
trivial absolute value, one branch per prime `p` (`|·|_p^ε`, `ε ∈ (0,∞]`, the end `ε = ∞` being the residue
field `F_p`) and one archimedean branch (`|·|_∞^ε`, `ε ∈ (0,1]`). Poineau, *La droite de Berkovich sur Z*
(Astérisque 334, 2010); Lemanissier–Poineau, *Espaces de Berkovich globaux*. (2) In the coordinate
`u = −log|p|_p^ε = ε log p` on the `p`-branch, the points `ε = k ∈ N` are `u = k log p`: the corpus's Frobenius
lattice `{k log p}` (Papers 44–46) is the set of **integer points of the branches**, and the Weil kernel's
atoms `(log p)p^{−k/2}δ_{±k log p}` sit exactly there; the archimedean branch carries the continuous
Gamma term. Verify and state as a dictionary (RESTATEMENT). (3) Potential theory on metrized trees /
Berkovich curves (Baker–Rumely, *Potential theory and dynamics on the Berkovich projective line*; Thuillier;
Chambert-Loir–Ducros): Laplacian, energy pairing, negative-type of the tree metric, equidistribution.

**Questions.** (Q5) Is the Weil form `W(f*f̃)` expressible as an energy (or as a Laplacian pairing) of a measure
on `M(Z)` or on the Berkovich line `A^{1,an}_Z`, with the archimedean branch as the special branch? Compute
what the tree energy of the measure `Σ_{p,k}(log p)p^{−k/2}δ_{(p,k)}` is, and show whether it has ANY relation
to positivity of the kernel `K(u)` on `R` (the corpus's finding NG-E1: per-place forms are indefinite;
MW-3: Hasse–Minkowski does not apply). Expect: the tree only labels the atoms; positivity of a
translation-invariant kernel on `R` is not a tree-potential statement — prove or refute this expectation.
(Q6) Do global Berkovich spaces over `Z` carry a Frobenius (Poineau's `Z`-analytic spaces have no Frobenius;
but the `F_1`-geometry of Connes–Consani and the Witt/Borger `λ`-ring structure do: is there a published
comparison?) and an intersection theory (Arakelov on `Spec Z` is 1-dimensional; the square `M(Z) × M(Z)` is a
product of trees — does any published work define a pairing there)? (Q7) What does the corpus's own audit
(`03-research/AUDIT_A_CATEGORY_CHANGES.md`: "No Berkovich space over Spec Z … is built anywhere") expect from
it, and does that expectation survive (Q5)–(Q6)?

**Kill criterion B.** If (Q5) is refuted (tree energy carries no information on the positivity of `K` on `R`)
and (Q6) finds no Frobenius and no square pairing, mechanism B is DEAD as a route to the sign and recorded as a
dictionary only (the Frobenius lattice = integer points of `M(Z)`), which may still be worth one remark in
Paper 44. Otherwise formulate **(P152.B)** with gates.

## C. Reserve (do not build; one paragraph each with corpus status): `×p` measure rigidity on `R/Z`
(Furstenberg–Rudolph–Lindenstrauss; relation to Bost–Connes NO-GO Thm 161.9); model-theoretic methods;
transcendence / auxiliary-function toolkit (Bombieri–Stepanov is the square `X×X` in function-theoretic form:
Thm 22.17 closes it — verify).

## D. Deliverable

`R152_001_FEASIBILITY.md`: §0 verdicts (A, B: DEAD / (P152.x) formulated); §1 corpus check (grep commands and
results for every name above); §2 mechanism A (facts, Q1–Q4, kill criterion applied); §3 mechanism B (facts,
Q5–Q7, kill criterion applied); §4 reserve; §5 gates; §6 labels; §7 what, if anything, goes to Paper 46 §28.4
(reopening clauses) or Paper 44 (dictionary). FATAL rule in force. English, pure mathematics.
