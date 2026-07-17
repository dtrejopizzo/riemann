# The Riemann Program

An independent, computer-assisted research program on the **Riemann Hypothesis (RH)**, offered
as a serious, fully-traceable contribution to one of mathematics' hardest open problems.

This is **not a claimed proof.** It is a long, honest investigation that reduces RH to a single
named, classical open input, and maps every wall, dead end, and self-correction along the way —
with reproducible code and a complete record.

> **Governing principle:** *a false victory would be worse than a failure.* Where the program
> reached a rigorous result, it says so. Where it hit a wall, it names the wall. Where it fooled
> itself and corrected, it records the correction.

## Start here

| Read | What it gives you |
|---|---|
| **[Human explanation](EXPLANATION.md)** | RH and what we learned, in plain language — layer by layer, no proof assumed |
| **[Program map](00-MAP.md)** | The whole road traveled, from the survey to the wall, in one picture |
| **[Master plan](MASTER-PLAN.md)** | Audit of the corpus, its structure, and the open route ahead |
| **[Complete program summary](COMPLETE-PROGRAM-SUMMARY.md)** | Every paper, phase, no-go, and wall, end to end |
| **[No-go list](NO-GO-LIST.md)** | The permanent registry of everything that failed or hit a wall |
| **[Papers index](04-papers/README.md)** | The 36 publishable papers, in order, with what each one establishes |

## How the work is organized

The program has two layers:

- **Research Programs 1–9** — [`01-context/`](01-context/): nine large computational research
  programs (627 tasks). The empirical base.
- **Program 10** — [`03-research/`](03-research/): the theoretical program built on that base,
  run as a sequence of numbered phases, currently through **phase 76**.

Supporting material: the validated computational core ([`02-foundations/`](02-foundations/)),
the publishable papers ([`04-papers/`](04-papers/), 36 of them, catalogued in
[`04-papers/README.md`](04-papers/README.md)), external reference material
([`00-references/`](00-references/)), and the planning and audit notes
([`05-meta-and-planning/`](05-meta-and-planning/)).

## Where the program ended

The program reduced RH, by a chain of proved equivalences (the arithmetic Pick/Nevanlinna
architecture, ARP-P — see [paper 36](04-papers/36-obstruction-ledger/)), to a single classical
open input: the **Li–Keiper criterion**, $\lambda_n \ge 0$ for all $n$. Fourteen of the chain's
fifteen steps are fully closed; the remaining one terminates exactly at that criterion. Being
equivalent to RH, it carries the full difficulty of the Hypothesis — the reduction closes
nothing by itself, but it is the precise place every major route explored in this corpus
independently arrives at (see [`00-MAP.md`](00-MAP.md) and [`NO-GO-LIST.md`](NO-GO-LIST.md) for
the six structural walls, MW-1 through MW-6, that block every other approach).

Along the way the program produced genuinely new RH-*independent* mathematics (the
ω-class / multiplicative-chaos dictionary, the information barrier, Pontryagin rigidity, an
unconditional finite bottom, a Stepanov almost-periodicity theorem, among others) and a
complete, precise map of the obstructions.

## Status

| Area | Status |
|---|---|
| Arc A / ω-class (Research Programs 1–9) | Documented; descriptive, did not beat convexity |
| Localized Weil detector | Rigorous in parts; the finite-defect route closed |
| Program 10 (phases 0–76) | Dense theory, the full no-go catalogue, and the reduction to Li–Keiper |
| RH itself | **Open.** The wall now has one name. |

## Philosophy

Read everything here as an autonomous mathematical program: not a promise of victory, but a
serious collaboration with the community to push a very hard problem forward — with
traceability, honesty, and a memory of the useful failures.
