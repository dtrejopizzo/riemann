# The Riemann Program — Internal Map

**Author:** David Alejandro Trejo Pizzo · `dtrejopizzo@gmail.com`
**Updated:** 2026-08-18

This is the navigation map for the corpus. The program is one continuous investigation of the
Riemann Hypothesis, organized in two layers:

- **Research Programs 1–9** — nine computational research programs (the empirical base).
- **Program 10** — the research phases (currently through phase 119) built on top of them.

> **Governing principle: absolute candor.** *A false victory would be worse than a failure.*
> No proof of RH has been found. Every wall, dead end, and self-correction is recorded.

## How to navigate

| Folder | What it is | Start here |
|---|---|---|
| [`00-references/`](00-references/) | External papers used as references (Connes–Consani, Connes–Moscovici prolate, etc.) | — |
| [`01-context/`](01-context/) | **Research Programs 1–9** — the empirical runs (627 tasks) | [`01-context/README.md`](01-context/README.md) |
| [`02-foundations/`](02-foundations/) | Shared computational core: the validated engine, zero data, precision validation | `02-foundations/engine/` |
| [`03-research/`](03-research/) | **Program 10** — the research phases (currently through phase 119) | [`03-research/README.md`](03-research/README.md) |
| [`04-papers/`](04-papers/) | The publishable corpus (42 publishable papers) | [`04-papers/README.md`](04-papers/README.md) |
| [`05-meta-and-planning/`](05-meta-and-planning/) | Planning notes, strategy memos, cross-cutting audits (not papers) | [`05-meta-and-planning/README.md`](05-meta-and-planning/README.md) |

## High-level documents (read in this order)

1. **[`00-MAP.md`](00-MAP.md)** — the road traveled, from the survey to the wall, as one picture.
2. **[`MASTER-PLAN.md`](MASTER-PLAN.md)** — audit of the corpus, the reorganization, and the next pushes.
3. **[`COMPLETE-PROGRAM-SUMMARY.md`](COMPLETE-PROGRAM-SUMMARY.md)** — the complete program summary (every paper, phase, no-go, and wall).
4. **[`NO-GO-LIST.md`](NO-GO-LIST.md)** — the permanent registry of everything that failed or hit a wall. *Consult before attempting any new attack.*
5. **[`OPTIONS.md`](OPTIONS.md)** — where to spend the next unit of effort, including targets not equivalent to RH.

## The scientific bottom line (one paragraph)

The program located, with surgical precision, **where RH lives**: in the sign of a single
scalar parameter κ = #(off-line zeros), which is *global*, *one-sided* (an upper bound), and
*orthogonal to all symmetry data*. Every historical approach attacks the abundant symmetry
data but not the scarce sign — which is why they all stall at the same wall (Weil positivity =
RH; catalogued as MW-1 through MW-6 in [`NO-GO-LIST.md`](NO-GO-LIST.md)). The program produced
genuinely new RH-*independent* mathematics (the ω-class / multiplicative-chaos dictionary, the
information barrier, the Pontryagin rigidity, an unconditional finite bottom), a complete and
precise map of the no-goes, and now **two** independent, structurally different full reductions of
RH to a single named open input, reached by two unrelated constructions. Paper **36**
(`04-papers/36-obstruction-ledger/`, phases 0–76) builds a fifteen-step arithmetic Pick/Nevanlinna
chain (ARP-P) equivalent to RH, terminating at the classical Li–Keiper criterion
($\lambda_n\ge0$ for all $n$). Paper **42** (`04-papers/42-arithmetic-lefschetz-programme/`,
phases 107–119) imitates Weil's 1948 proof for curves over finite fields directly over
$\operatorname{Spec}\mathbb Z$; its row (d) — the Hodge-index/Castelnuovo–Severi input — is
proved equivalent to RH **twice**, independently: algebraically (phase 113, via Riemann–Roch and
effectivity) and analytically (phase 118, via the explicit formula, verified against real zeros of
$\zeta$ to $10^{-10}$ relative precision). Neither reduction is a proof — each open input is
equivalent to RH and carries its full difficulty — but together they are the sharpest, most
concrete, and most independently cross-checked statement of where the difficulty lives that the
program has produced. [`OPTIONS.md`](OPTIONS.md) records the genuinely open next steps, including
several targets that are *not* equivalent to RH and were never closed.

## Language

The repository is in English. Folder names and front-door/summary documents are English; some
granular working notes inside `03-research/phase-*` remain in their original Spanish as the raw
research record.
