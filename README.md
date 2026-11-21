# The Riemann Program

An independent research program on the Riemann zeta function, built around Weil's explicit
formula and the sign of the Weil quadratic form. This repository contains the papers, the
complete research record (memos, proofs, audits, retractions, certificates) and the code that
produced the numerical certificates.

## The route: Weil's proof, transplanted to the idele class group

Weil proved the Riemann hypothesis for a curve over a finite field in four steps: a ring of
correspondences with a trace, the Frobenius correspondences inside it, a fixed-point formula for
the trace, and the Hodge-index inequality on classes of bidegree zero. Papers 43, 44, 45 and 47
carry out the same four steps for $\mathrm{Spec}\,\mathbb Z$, on the idele class group of
$\mathbb Q$.

| Row | Step in Weil's proof | Paper | What is proved |
|---|---|---|---|
| A | Correspondences, involution, trace, bidegree | [43](04-papers/43-row-a-torsion-theory/) | A convolution algebra of semilocal idele class correspondences with its involution and trace; the two Tate characters give the bidegree and define the primitive subspace. |
| B | Frobenius | [44](04-papers/44-row-b-arithmetic-family/) | A Frobenius measure for every positive integer with prime divisors in $S$; its contact with the diagonal has weight $\Lambda(n)/\sqrt n$, supported on prime powers. |
| C | Fixed-point (explicit) formula | [45](04-papers/45-row-c-explicit-formula/) | Weil's explicit formula for the radial trace: the self-intersection of a radial class equals its two Tate moments minus a sum over the nontrivial zeros of $\zeta$; if $\zeta$ had a zero off the critical line, a real primitive test function of compact support would detect it. |
| D | Intersection inequality (the sign) | [47](04-papers/47-row-d-dual-certificates/) | The sign of the radial intersection form $W_T$ on functions supported in $(-T,T)$: see below. |

### What Paper 47 establishes

- **Equivalence theorem.** The following are equivalent: (1) the Riemann hypothesis for $\zeta$;
  (2) $W_T(F)\ge 0$ for every $T>0$ and every $F$ in the form domain; (3) $\lambda_A(T)\ge 0$ for
  every $T>0$ (the primitive restriction). Together with Papers 43–45 this completes the
  equivalence between the intersection inequality for every compact support and the classical
  Riemann hypothesis.
- **Bounded windows, unconditionally.** For $T\le\tfrac12\log 5$ the lower bounds on unit vectors
  are $10^{-18}$ for the complete form and $2.5\cdot10^{-12}$ for its primitive restriction; a
  certificate using finite-height zero data gives an explicit positive lower bound up to
  $T=2.8022$.
- **Finite reduction.** On the arithmetic side the all-window inequality is reduced to positive
  semidefiniteness, in every degree, of a single sequence of explicit matrices.
- **All windows, under half-plane nonvanishing.** Assume $L(s,\chi)\ne 0$ for $\Re s>1/2$ for
  every Dirichlet character $\chi$ (the pole of a principal character excluded). Then $W_T\ge 0$
  on the entire form domain for every $T>0$, the primitive self-intersection is $\le 0$, and the
  matrices of the finite reduction are Gram matrices in every degree.

**Status of the all-window sign.** In Paper 47 the sign for every window is proved under the
half-plane nonvanishing hypothesis above; for modulus one that hypothesis is the statement that
$\zeta$ has no zero to the right of the critical line. Unconditionally the paper proves the sign
on bounded windows (up to $T=2.8022$) and the equivalence theorem. The papers therefore establish
the complete Weil-type route and the exact equivalence of its last step with the Riemann
hypothesis.

## Papers 43–48

| Paper | Title | Content |
|---|---|---|
| [43](04-papers/43-row-a-torsion-theory/) | A Correspondence Algebra and the Weil Distribution on Semilocal Idele Class Groups | Row A. |
| [44](04-papers/44-row-b-arithmetic-family/) | An Arithmetic Frobenius Family on Semilocal Idele Class Groups | Row B. |
| [45](04-papers/45-row-c-explicit-formula/) | An Explicit Formula for the Trace on Semilocal Idele Class Groups | Row C. |
| [46](04-papers/46-intersection-frame-defect/) | An Intersection Frame for the Explicit Formula: Hodge-Index Transfer, a Frame Defect Theorem and a Function-Field Model | Structural theorems on the extended Weil form; no sign claimed. |
| [47](04-papers/47-row-d-dual-certificates/) | The Sign of the Radial Intersection Form on the Idele Class Group | Row D. |
| [48](04-papers/48-row-d-route-map/) | A Map of the Routes to Weil Positivity on Finite Windows: Barriers, Falsifiers, and the Open Inequality | Reference map of the routes attempted for the sign, with barrier theorems and falsifiers. |

The full catalogue of papers 01–48 is in [`04-papers/README.md`](04-papers/README.md).

## How the repository is organised

| Folder | Contents |
|---|---|
| [`00-references/`](00-references/) | External literature used by the program. |
| [`01-context/`](01-context/) | Research programs RH2017–RH2025: the early computational investigations. Raw notebooks and outputs. |
| [`02-foundations/`](02-foundations/) | The validated computational core: engine, zero data, precision checks. |
| [`03-research/`](03-research/) | The research record, organised in numbered phases (0–213): memos, proofs, audits and certificates. Indexed in [`03-research/README.md`](03-research/README.md). |
| [`04-papers/`](04-papers/) | Papers 01–48. |
| [`05-meta-and-planning/`](05-meta-and-planning/) | Plans, audits and the master index of all routes attempted for the sign ([`ROUTES-MASTER-INDEX.md`](05-meta-and-planning/ROUTES-MASTER-INDEX.md)). |

Papers, READMEs and indices are in English. Many working memos of the later phases are written
in Spanish.

## Labels

Used throughout: PROVED, CITED, CONDITIONAL, ARGUED, OPEN, NO-GO, NUMERICAL.

## Author

David Alejandro Trejo Pizzo, independent researcher.
