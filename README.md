# The Riemann Program

An independent research program on the Riemann zeta function, built around Weil's explicit
formula and the positivity of the Weil quadratic form. This repository contains the papers, the
complete research record (computations, memos, audits, retractions) and the code that produced
the numerical certificates.

No paper in this repository claims a proof of the Riemann hypothesis.

## The current programme in one paragraph

Papers 43–48 imitate the structure of Weil's proof for curves over finite fields, transplanted to
the idele class group of $\mathbb Q$. The construction is organised in four rows. Row A builds a
correspondence algebra with a canonical trace on a declared carrier; row B builds the arithmetic
Frobenius family inside it; row C proves the explicit formula for that trace; row D asks for the
sign: positivity $\lambda_A(T)\ge 0$ of the window form $A$ on the space $P_T$ of test functions
supported in $[-T,T]$. Rows A, B and C are closed on the declared carrier. **Row D is open.** It is
proved, with certified interval arithmetic, for all windows $T\le \tfrac12\log 15$ (the endpoint
$\tfrac12\log15$ is due to Mori and is cited); beyond that window it is an open problem, treated
here as a target in its own right.

## Papers 43–48

| Paper | Title | Content | Status |
|---|---|---|---|
| [43](04-papers/43-row-a-torsion-theory/) | A Correspondence Algebra with a Canonical Trace on the Idele Class Group, its Tate Symbol and its Numerical Form | Row A: the carrier, the canonical trace, twisted excision, Künneth decomposition and the torsion invariant. | Row A closed |
| [44](04-papers/44-row-b-arithmetic-family/) | An Arithmetic Frobenius Family and its Integral Shadow on a Correspondence Algebra of the Idele Class Group | Row B: the Frobenius family as Haar measures of fixed-point strata, its integral shadow and two Gram forms. | Row B closed |
| [45](04-papers/45-row-c-explicit-formula/) | An Explicit Formula and a Comparison Theorem for the Canonical Trace on a Correspondence Algebra of the Idele Class Group | Row C: the Weil explicit formula for the canonical trace and the comparison theorem with the zero side. | Row C closed |
| [46](04-papers/46-intersection-frame-defect/) | An Intersection Frame for the Explicit Formula: Hodge-Index Transfer, a Frame Defect Theorem and a Function-Field Model | The Pólya class, radical and polar plane of the extended Weil form; a conditional Hodge-index transfer; the frame defect theorem and its function-field model. | Structural theorems; no sign claimed |
| [47](04-papers/47-row-d-dual-certificates/) | Weil Positivity on a Finite Window: Duality, Certificates and a Finite Reduction | Row D: everything proved about the sign — duality, certificates up to $\tfrac12\log15$, barrier theorems, the finite reduction and the open node. | Row D OPEN |
| [48](04-papers/48-row-d-route-map/) | A Map of the Routes to Weil Positivity: Eight Arithmetic Inputs, Eight Carriers, and the Specification of a Closing Argument | Classification of the routes attempted for row D on an 8×8 grid, with walls, falsifiers and the specification any closing argument must meet. | Survey of routes |

The full catalogue of papers 01–48 is in [`04-papers/README.md`](04-papers/README.md).

## How the repository is organised

| Folder | Contents |
|---|---|
| [`00-references/`](00-references/) | External literature used by the program (Connes–Consani, Connes–Moscovici, arXiv reviews, literature surveys). |
| [`01-context/`](01-context/) | Research programs RH1–RH9: the early computational investigations (statistics of Dirichlet polynomials, ω-classes, localized Weil forms). Raw notebooks and outputs. |
| [`02-foundations/`](02-foundations/) | The validated computational core: engine, zero data, precision checks. |
| [`03-research/`](03-research/) | The research record, organised in numbered phases (0–209): memos, proofs, audits and certificates. |
| [`04-papers/`](04-papers/) | Papers 01–48. |
| [`05-meta-and-planning/`](05-meta-and-planning/) | Plans, audits and the index of all routes attempted for row D. |
| [`06-grafico/`](06-grafico/) | Illustrative plots and sonifications (not part of the phase sequence). |
| [`07-calculos-adicionales/`](07-calculos-adicionales/) | Closed numerical side audits. |
| [`08-sent/`](08-sent/) | Notes as sent to correspondents. |

## Reading guide

- [`00-MAP.md`](00-MAP.md) — map of the repository and of the research.
- [`COMPLETE-PROGRAM-SUMMARY.md`](COMPLETE-PROGRAM-SUMMARY.md) — the whole program in a few pages.
- [`MASTER-PLAN.md`](MASTER-PLAN.md) — the current plan for row D: the open node and the live gate.
- [`NO-GO-LIST.md`](NO-GO-LIST.md) — pointer to the index of routes attempted and to Paper 48.
- [`EXPLANATION.md`](EXPLANATION.md) — a non-technical explanation of the problem and of what was learned.

## Status

| Item | Status |
|---|---|
| Row A (Paper 43) | Closed on the declared carrier |
| Row B (Paper 44) | Closed on the declared carrier |
| Row C (Paper 45) | Closed on the declared carrier |
| Row D (Paper 47) | **OPEN**; proved for $T\le\tfrac12\log15$ (certified; endpoint cited from Mori) |
| Routes attempted for row D | About 1,400, indexed in [`05-meta-and-planning/ROUTES-TRIED-INDEX/`](05-meta-and-planning/ROUTES-TRIED-INDEX/) and classified in Paper 48 |

Labels used throughout: PROVED, CITED, CONDITIONAL, ARGUED, OPEN, NO-GO, NUMERICAL.

## Author

David Alejandro Trejo Pizzo, independent researcher.
