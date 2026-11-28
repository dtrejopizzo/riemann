# Phase 216 — New arithmetic connections

**Status: OPEN.** Round 003 proves exact crystalline costs and identifies Iwasawa/logarithm antecedents of the binomial construction; originality and exhaustive coverage remain unestablished. Start with [ROUND-003-SYNTHESIS.md](ROUND-003-SYNTHESIS.md). Round 001 completed on **2026-11-28**: three research fronts, elementary proofs and counterexamples, exact checks, and a targeted primary-literature review. Priority is not established. This phase explores autonomous mathematics beyond the GRH/RH chain; its results do not assume RH or certify the earlier chain.

## Question

Which information is lost by pair correlations, determinants and binary cup products, and what does it cost to realise the missing higher compatibility integrally? The expanded programme seeks precise connections and applications beyond the original proof, with literature checked against the requested cutoff of 2026-11-28.

The starting programme from phase 215 concerned integral compatibility between twists, kernels realisable by CM weights, and cup-product exponents. Round 001 extends it to higher CM observables, simultaneous integral realisation of diagrams, and filtered crystalline extensions. The central mathematics organised by Short Forms, Spanning and Covolume is attributed to Alpöge, as acknowledged in Paper 57; this phase distinguishes those antecedents from its own formulations and results.

## Results and status

| Result | Status and scope |
|---|---|
| Two CM types with identical two- and three-point correlations but different four-point correlations | PROVED for an explicit CM field; no priority claim |
| Fourfold E-linear Hodge tensors distinguish those types: h40 = 2 versus 1 | PROVED using classical tensor formalism; arithmetic periods and integral costs OPEN |
| Unit determinants do not ensure a common stable lattice; traces alone do not bound cost relative to a prescribed lattice | PROVED by explicit 2-by-2 examples; general theory has antecedents |
| Vanishing binary cups coexist with arbitrarily costly, rationally vanishing ternary obstruction | PROVED in a fixed-rank integral differential graded algebra; Galois/crystalline realisation OPEN |
| Integral crystalline realisation cost c_cris is finite when the prescribed rational realisation exists | PROVED by diagonal conjugation; useful uniform bounds OPEN |
| A new field or a literature-first arithmetic theorem | NOT ESTABLISHED; precise candidate problems and nearest antecedents recorded |

The bibliography includes sources from October and November 2026. Searches are targeted, not an exhaustive review of all arXiv. Several sources were inspected at abstract level only; the front reports state the limits.

## Round 002

Read [the second-round report](ROUND-002-SYNTHESIS.md) for the exact degree barrier, four-point reconstruction lemma, classical different-controlled projector cost, and crystalline zero-cost regimes. The p=3 Kummer example was resolved: its cost is zero. A binomial lattice proves zero cost for all consecutive Tate graded chains over Q_p, p odd, with arbitrary adjacent crystalline classes; priority of this exact application remains unestablished. These results narrow the novelty claims of round 001; none establishes a new field or priority.

## Round 003

[The third-round report](ROUND-003-SYNTHESIS.md) gives an exact cup-order formula for three Tate graded pieces, positive-cost examples over Q₂ and Q₃(ζ₃), and a structural prior-art comparison. The next target is a cost beyond the binary cup obstruction, with four or more graded pieces; no such arithmetic example is proved here.

## Files

- [ROUND-001-SYNTHESIS.md](ROUND-001-SYNTHESIS.md) — main report in Spanish: results, connections, novelty filter and next theorem targets.
- [FRONT-01-KERNELS.md](FRONT-01-KERNELS.md) — CM correlations, reconstruction and fourfold Hodge tensors.
- [FRONT-02-COMPATIBILIDAD.md](FRONT-02-COMPATIBILIDAD.md) — integral diagrams, lattice costs and counterexamples.
- [FRONT-03-OBSTRUCCIONES.md](FRONT-03-OBSTRUCCIONES.md) — higher integral obstructions and crystalline extensions.
- [bibliography/](bibliography/) — primary references and query records, with scope limitations.
- [experiments/cm_correlations.py](experiments/cm_correlations.py) and [output](experiments/cm_correlations.json) — exact finite CM checks.
- [experiments/check_massey_dga.py](experiments/check_massey_dga.py) — exact algebraic consistency checks.

Run the checks with Python 3 from the repository root:

```bash
python3 03-research/phase-216-new-arithmetic-connections/experiments/cm_correlations.py
python3 03-research/phase-216-new-arithmetic-connections/experiments/check_massey_dga.py
```

## Relation to other phases and next step

The original programme is in [phase 215](../phase-215-private-certification-grh-rh-with-supplements/NEW-CONNECTIONS-AND-PROGRAMME.md). Its historical verdict is separate from this exploration.

Next: compare the four-point example with existing partial-CM-type heights; compute c_cris in a nontrivial rank-one graded family; seek a proved bridge from higher extension losses to integral diagram costs. The proposed programme of quantitative integral realisation remains a research proposal, not an established new area.
