# The Riemann Program

An independent, computer-assisted research program on the **Riemann Hypothesis (RH)**, offered
as a serious, fully-traceable contribution to one of mathematics' hardest open problems.

This is **not a claimed proof.** It is a long, candid investigation that reduces RH to a single
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
| **[Papers index](04-papers/README.md)** | The 42 publishable papers, in order, with what each one establishes |
| **[Options](OPTIONS.md)** | Where the corpus's own audit says work can still usefully continue, including targets not equivalent to RH |

## How the work is organized

The program has two layers:

- **Research Programs 1–9** — [`01-context/`](01-context/): nine large computational research
  programs (627 tasks). The empirical base.
- **Program 10** — [`03-research/`](03-research/): the theoretical program built on that base,
  run as a sequence of numbered phases, currently through **phase 119**.

Supporting material: the validated computational core ([`02-foundations/`](02-foundations/)),
the publishable papers ([`04-papers/`](04-papers/), 42 of them, catalogued in
[`04-papers/README.md`](04-papers/README.md)), external reference material
([`00-references/`](00-references/)), the planning and audit notes
([`05-meta-and-planning/`](05-meta-and-planning/)), illustrative visualization and sonification
material not part of the phase sequence ([`06-grafico/`](06-grafico/)), and closed numerical
side-audits from phase 115 ([`07-calculos-adicionales/`](07-calculos-adicionales/)).

## Where the program stands now

The program currently has **two** independent, structurally different reductions of RH to a
single classical open input — not an ending, but the state of an active investigation.

**Route 1 — the Pick/Nevanlinna chain (phases 0–76, [paper 36](04-papers/36-obstruction-ledger/)).**
A fifteen-step arithmetic Pick/Nevanlinna architecture (ARP-P) reduces RH to the classical
**Li–Keiper criterion**, $\lambda_n \ge 0$ for all $n$. Fourteen of the fifteen steps are fully
closed.

**Route 2 — the arithmetic-Lefschetz reconstruction (phases 107–119,
[paper 42](04-papers/42-arithmetic-lefschetz-programme/)).** A direct imitation of Weil's own 1948
proof of RH for curves over finite fields, built over $\mathrm{Spec}\,\mathbb Z$. Its own open
input — row (d), the Hodge-index/Castelnuovo–Severi step — is proved equivalent to RH **twice**,
independently: algebraically (phase 113, via Riemann–Roch and effectivity) and analytically
(phase 118, via the explicit formula, verified against real zeros of $\zeta$ to $10^{-10}$
relative precision).

Both routes are candid and neither is a proof: each open input is equivalent to RH and carries
its full difficulty. But they are the precise places every major route explored in this corpus
independently arrives at (see [`00-MAP.md`](00-MAP.md) and [`NO-GO-LIST.md`](NO-GO-LIST.md) for
the structural walls that block every other approach), reached by two unrelated constructions —
which is itself evidence the difficulty is a property of RH, not an artifact of either method.

Along the way the program produced genuinely new RH-*independent* mathematics (the
ω-class / multiplicative-chaos dictionary, the information barrier, Pontryagin rigidity, an
unconditional finite bottom, a Stepanov almost-periodicity theorem, among others) and a
complete, precise map of the obstructions. [`OPTIONS.md`](OPTIONS.md) records where the corpus's
own audit says work can still usefully continue — including several targets that were never shown
equivalent to RH and were simply never closed.

## Status

| Area | Status |
|---|---|
| Arc A / ω-class (Research Programs 1–9) | Documented; descriptive, did not beat convexity |
| Localized Weil detector | Rigorous in parts; the finite-defect route closed |
| Program 10, phases 0–76 (ARP-P) | Dense theory, the full no-go catalogue, and the reduction to Li–Keiper |
| Program 10, phases 107–119 (arithmetic Lefschetz) | Rows (a)–(c) built (paper 42); row (d) proved equivalent to RH twice, independently |
| RH itself | **Open.** Two independently named walls, plus a list of genuinely open sub-RH targets in [`OPTIONS.md`](OPTIONS.md). |

## Philosophy

Read everything here as an autonomous mathematical program: not a promise of victory, but a
serious collaboration with the community to push a very hard problem forward — with
traceability, candor, and a memory of the useful failures.
