# Phase 168 — Untried inputs: a semantic survey and audit of candidate mathematical mechanisms

Before any new construction, the phase surveys the entire corpus (03-research and 04-papers) by
grep and context reading to list every open residue and every class of mathematical input
(Diophantine approximation, ergodicity, p-adic ζ, Selberg class degree 2, Deuring–Heilbronn
repulsion, Laguerre–Pólya, etc.) that could bear on the single-witness-scale question (★_cell)/(WS*)
at the center of the program's row-D witness construction, ranks the never-tried ones by plausibility,
and then audits each live candidate one by one.

## Results

- Semantic survey: 20 open residues catalogued by RH-relevance class (a/b/c) and attack status; around a dozen input classes (Baker/linear forms in logs, Diophantine approximation of p^{iγ}, ergodicity/equidistribution, o-minimality/Pila–Wilkie, p-adic ζ, random matrix statistics, Selberg class degree 2, Erdős–Turán quantitative unique factorization, Deuring–Heilbronn, Turán power sums, Montgomery–Vaughan, zero-density, Bohr–Jessen, universality) found and traced to their recorded closure, or marked NOT FOUND — **a record survey**, no new mathematics claimed.
- Ranking: witness-scale Deuring–Heilbronn repulsion identified as the only genuinely untried mechanism type that differs in kind from closed ones; Selberg-class degree-2 positivity as its natural carrier, both flagged high-risk by the surveyor.
- R168_101 (Deuring–Heilbronn re-test): the identity-level D–H/Turán repulsion is **PROVED** to be vacuous (slack) near σ = ½ for configurations of the kind the falsifier M_m produces — **WALL MET**; residue O168.101.1 (a nonlinear, non-explicit-formula zero-side law near σ=½) left **OPEN**, no candidate found.
- R168_102 (Diophantine alignment / Baker): **PROVED** every Diophantine/equidistribution input is either a null-set-blind measure statement, an alignment statement pointing the wrong direction, or a γ-uniform statement equivalent to an RH-strength zero-free-strip condition (U) — **CLOSED NEGATIVE** (single-height wall); residue O168.102.1 = (U) is RH-strength, **OPEN**.
- R168_103 (small-y regime): reduces local (★_cell) to a precise needed input (P_gap), an anti-clustering statement around a hypothetical off-line zero — **PROVED** as a reduction — but P_gap itself is **OPEN** and is shown to be freely violated by the falsifier construction M_m (**PROVED**).
- R168_201 (degree-2 carrier): ζ(s+iγ)ζ(s−iγ) and related degree-2/degree-4 Euler products are **PROVED** to inherit ζ's own positivity exactly (never weaker — identification, E1) and to give only trivial-order bounds — **CLOSED NEGATIVE**.
- R168_202 (two never-attacked residues, O-151.4 and Q27/E_(∞,T)): both **CLOSED with proof** — shown to be reformulations of Hilbert–Pólya self-adjointness or of the identification wall, not new routes.
- R168_203 (local Laguerre inequality): the proposed equivalence between (★_cell) failure and local Laguerre-inequality failure is **PROVED FALSE** — the two are logically independent conditions; the Laguerre sign is shown to be a linear (hence E1-blocked) functional of the zero measure — **CLOSED NEGATIVE**, with a new general proposition (L4) about the first Laguerre inequality's blindness to quartets.
- Overall closure: seven fronts opened, seven closed with proof; four initial surveyor hypotheses refuted. Residues left genuinely open with content: the Beurling frontier (C1/C2), O168.101.1, O168.103.1/P_gap, and the RH-strength statement (U)/(WS*).

## Documents

- `R168_001_SEMANTIC_SURVEY.md` — the full corpus grep survey and input-class ranking.
- `R168_101_DEURING_HEILBRONN.md`, `R168_102_DIOPHANTINE_ALIGNMENT.md`, `R168_103_SMALL_Y_REGIME.md` — round-1 audits.
- `R168_201_DEGREE_TWO_CARRIER.md`, `R168_202_NEVER_ATTACKED_RESIDUES.md`, `R168_203_LOCAL_LAGUERRE.md` — round-2 audits.
- `R168_190_AUDIT.md` — consolidated reference audit and closure ledger for all seven fronts.

## Relation to other phases

Builds on and re-tests NO-GO-LIST items and phase 25/37 mechanisms; directly continues the (★_cell)/(WS*) witness program of phases 163–167 (all labeled DEAD there) and feeds the input-architecture search of phase 169.
