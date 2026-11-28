# The Riemann Program

An independent research program, a little over eleven years long, on one question: can Weil's
proof of the Riemann hypothesis for curves over finite fields be carried out, row by row, over
$\mathrm{Spec}\,\mathbb Z$?

Papers 43, 44, 45 and 46 are the answer given here: one paper for each of the four rows of Weil's
proof, on the idele class group of $\mathbb Q$, with eight companion papers (49–56) for the last
row. The last step, the sign on every window, is closed by the argument of **Levent Alpoge**,
written here on paper as three theorems. This repository contains the papers, the complete research
record (memos, proofs, audits, retractions, certificates) and the code behind the numerical
certificates, in Markdown and LaTeX, so that anyone can read it, check it, break it or reuse it.

## The route: Weil's proof over Spec Z

Weil proved the Riemann hypothesis for a curve over a finite field in four steps: a ring of
correspondences with a trace, the Frobenius correspondences inside it, a fixed-point formula for
the trace, and the Hodge-index inequality on classes of bidegree zero (*Sur les courbes
algébriques et les variétés qui s'en déduisent*, 1948). The map below shows the same four steps
over $\mathrm{Spec}\,\mathbb Z$, what each paper contributes, and on whose work it is built.

```
ROW A  A correspondence algebra and the Weil distribution            [Paper 43]
  |    graph bimodules and their Hochschild complexes, the trace T,
  |    the form T(F * G†), the Tate characters in the place of the rulings
  |    builds on: Weil (correspondences on curves; explicit formulas),
  |    Tate (thesis), Connes (trace formula, 1999), Meyer, Burnol,
  |    Connes–Consani–Marcolli (the Weil proof and the adele class space),
  |    Wodzicki, Brylinski, Nistor, Getzler–Jones (excision, crossed
  |    products), Bombieri, Yoshida
  v
ROW B  An arithmetic Frobenius family                                [Paper 44]
  |    measures with Frob_m * Frob_n = Frob_mn; the finite local terms
  |    sum to Λ(n) n^(-1/2) h(1/n)
  |    builds on: Weil, Tate, Connes, Connes–Consani (the arithmetic site),
  |    Connes–Consani–Marcolli, Bost–Connes, Burnol
  v
ROW C  An explicit formula for the trace                             [Paper 45]
  |    T_lim(Γ_h) = Φ_h(0) + Φ_h(1) − Σ_ρ Φ_h(ρ); the Tate functionals
  |    are the residues at s = 0 and s = 1; Weil's criterion in this setting
  |    builds on: Weil (explicit formula), Connes, Connes–Consani
  |    (Weil positivity), Meyer, Yoshida, Bombieri, Burnol, Barner,
  |    Suzuki (the screw function)
  v
ROW D  The sign of the radial intersection form                      [Paper 46]
       W_T(F) = Σ_ρ |Φ_F(ρ)|²  for F supported in (−T, T)

       (1) W_T ≥ 0 for every T  <=>  RH                    [Paper 46]
       (2) a one-sided criterion: if R_q(x) ≤ x^(β−1) for a
           prime sum weighted by 1 − χ_K, then no L(s, ψ)
           mod q vanishes in Re s > β                       [Paper 46;
                                                              Landau's method]
       (3) admissible arithmetic data exist                 [Paper 46]
       (4) three theorems on a lattice of integral algebraic
           modular forms on a chain of theta lifts:
             Short Forms Theorem                             [Papers 49, 50]
             Spanning Theorem                                [Papers 51, 52]
             Covolume Theorem                                [Papers 53–56]
           the mathematics they organise is Levent Alpoge's
       (5) the main inequality: the three theorems give the
           bound required by the criterion                  [Paper 46]
              |
              v
       no Dirichlet L-function vanishes in Re s > 1/2;
       RH, and W_T ≥ 0 on every window
```

| Row | Step in Weil's proof | Paper | What it contains |
|---|---|---|---|
| A | Correspondences, involution, trace, bidegree | [43](04-papers/43-row-a-correspondence-algebra/) | A convolution algebra of semilocal idele class correspondences with its involution and trace; the two Tate characters give the bidegree and define the primitive subspace. |
| B | Frobenius | [44](04-papers/44-row-b-arithmetic-family/) | A Frobenius measure for every positive integer with prime divisors in $S$; its contact with the diagonal has weight $\Lambda(n)/\sqrt n$, supported on prime powers. |
| C | Fixed-point (explicit) formula | [45](04-papers/45-row-c-explicit-formula/) | Weil's explicit formula for the radial trace: the self-intersection of a radial class equals its two Tate moments minus a sum over the nontrivial zeros of $\zeta$. |
| D | Intersection inequality (the sign) | [46](04-papers/46-row-d-sign-radial-intersection-form/) | *The sign of the radial intersection form on the idele class group*, with its eight companions (Papers 49–56): $W_T\ge 0$ on every window, and the Riemann hypothesis. |

### Who did what

Rows A, B and C are built entirely on the work of the mathematicians listed next to them; what is
done here is to carry the constructions through in one setting and write down every proof. In
row D, the study of the form, the criterion, the data and the main inequality belong to Paper 46,
on top of classical tools. For years the sign was known here only on a bounded range, certified
up to $T=2.8022$. The missing piece was global positivity.

That piece is Levent Alpoge's. It comes from his character-family argument, released as a Lean 4
formalization: <https://alpo.ge/remark.pdf>. In this series it takes the form of three theorems,
the Short Forms Theorem, the Spanning Theorem and the Covolume Theorem. The division of the
argument into these three statements, their names and the writing of their proofs as mathematics
on paper (Papers 49–56) are ours; the mathematics they organise, and the way from them to the
zero-free half-plane, are his.

### What is and is not claimed

- **Alpoge's formalization proves RH on its own.** His proof is self-contained and does not need
  these papers. Rows A, B and C, and the study of the radial form in row D, lay out a path and
  identify the inequality at its end; they do not prove it. It is his argument, in the form of
  the three theorems, that closes the path. So: Alpoge proves RH, and these papers are the same
  statement reached along Weil's four components.
- **The proof is written out on paper.** The deduction of RH is contained in Paper 46 and
  Papers 49–56, which rest on published theorems cited where they are used; rows A–C are not used
  in it and enter in the structural statement, $W_T\ge 0$ on every window. Paper 57 is a guide to
  the chain and Paper 58 gives row D in a single volume.
- **None of this has been refereed.** There may be mistakes. Corrections, questions and attempts
  to break any step are very welcome.

### Checks

- [`06-alpoge-verification/`](06-alpoge-verification/): an independent compilation of Alpoge's
  archive: it compiles in full (183,903 jobs, no error, no `sorry`) and its main theorems depend
  only on the three standard axioms of Lean. The folder holds the build logs, the axiom check,
  the checksums and the scripts.
- A Colab notebook,
  [`row-d-verification.ipynb`](04-papers/58-row-d-sign-radial-intersection-form-complete-proofs/verification/row-d-verification.ipynb),
  in the Paper 58 folder. It collects the numerical checks and the falsification attempts applied
  to individual statements of the chain, in small cases: 39 executed tests pass. It proves
  nothing, it does not reach the range in which the theorems are asserted, and it lists the
  statements that carry weight and were not tested.

## Acknowledgements

To **Levent Alpoge**, first of all. His work proves the Riemann hypothesis completely, and it also
supplies the component with which the proof along Weil's route over $\mathrm{Spec}\,\mathbb Z$ is
closed here: the argument behind the Short Forms, Spanning and Covolume Theorems. That is
the decisive input, and the whole mathematical community owes that step to his work.

To the mathematicians whose lifelong dedication made it possible even to attempt this: André Weil,
Alain Connes, Caterina Consani, Masatoshi Suzuki, Enrico Bombieri, Hiroyuki Yoshida, Ralf Meyer,
Jean-François Burnol, John Tate, and the many others cited in the papers.

## Papers 43–58

| Paper | Title | Content |
|---|---|---|
| [43](04-papers/43-row-a-correspondence-algebra/) | A Correspondence Algebra and the Weil Distribution on Semilocal Idele Class Groups | Row A. |
| [44](04-papers/44-row-b-arithmetic-family/) | An Arithmetic Frobenius Family on Semilocal Idele Class Groups | Row B. |
| [45](04-papers/45-row-c-explicit-formula/) | An Explicit Formula for the Trace on Semilocal Idele Class Groups | Row C. |
| [46](04-papers/46-row-d-sign-radial-intersection-form/) | The Sign of the Radial Intersection Form on the Idele Class Group | Row D, the main paper: the form, the one-sided criterion, the data, the three theorems and the main inequality. |
| [47](04-papers/47-intersection-frame-defect/) | An Intersection Frame for the Explicit Formula: Hodge-Index Transfer, a Frame Defect Theorem and a Function-Field Model | Structural theorems on the extended Weil form; no sign claimed. |
| [48](04-papers/48-routes-to-weil-positivity/) | Routes to Weil positivity on finite intervals: a cartography of attempts, barriers and open problems | Survey of the routes attempted toward the sign before the argument of row D was available: twenty-six families, with the mechanism of failure and the status of each, and the proved barriers. |
| [49](04-papers/49-short-forms-theorem-theta-lifts-complex-multiplication/) | The Short Forms Theorem: Theta Lifts, Complex Multiplication and Divisibility | Companion of row D: the inputs of the Short Forms Theorem and the foundations of the series. |
| [50](04-papers/50-elementary-divisors-edge-hecke-operator/) | Elementary Divisors of an Edge Hecke Operator on a Frobenius Cycle | Companion of row D: a scaled Hecke operator at inert primes is nearly unimodular. |
| [51](04-papers/51-spanning-theorem-second-moment-poincare-map/) | The Spanning Theorem: the Second Moment of a Poincaré Map | Companion of row D: the Spanning Theorem, by a second moment with exact main term. |
| [52](04-papers/52-sieve-systems-siegel-step/) | The Spanning Theorem: Sieve Systems at the Real and Finite Places and Siegel's Step | Companion of row D: the local statements behind the second moment. |
| [53](04-papers/53-covolume-theorem-exchange-identities-chain-determinant/) | The Covolume Theorem: Exchange Identities and the Determinant of a Chain of Theta Lifts | Companion of row D: the Covolume Theorem from its inputs. |
| [54](04-papers/54-covolume-theorem-one-theta-lift-hecke-l-values/) | The Covolume Theorem: One Theta Lift, Hecke $L$-values and Test Forms of Least Valuation | Companion of row D: one lift and its Hecke $L$-values. |
| [55](04-papers/55-covolume-theorem-regular-families-of-twists/) | The Covolume Theorem: Regular Families of Twists, Selmer Groups and Ribet's Method | Companion of row D: existence of the twists, by Selmer groups and Ribet's method. |
| [56](04-papers/56-explicit-cup-exponents-local-galois-representations/) | Explicit Cup Exponents for Local Galois Representations beyond the Fontaine–Laffaille Range | Companion of row D: the local input at every prime for Paper 55. |
| [57](04-papers/57-riemann-hypothesis-along-the-rows-of-weils-proof/) | The Riemann Hypothesis along the Rows of Weil's Proof: a Guide to the Series | Guide to the twelve papers 43–46 and 49–56. |
| [58](04-papers/58-row-d-sign-radial-intersection-form-complete-proofs/) | The Sign of the Radial Intersection Form on the Idele Class Group (row D in a single volume) | The whole chain of row D in one document (659 pages), with a notebook of numerical checks and falsification attempts. |

The full catalogue of papers 01–58 is in [`04-papers/README.md`](04-papers/README.md).

## How the repository is organised

| Folder | Contents |
|---|---|
| [`00-references/`](00-references/) | External literature used by the program. |
| [`01-context/`](01-context/) | Research programs RH2017–RH2025: the early computational investigations. Raw notebooks and outputs. |
| [`02-foundations/`](02-foundations/) | The validated computational core: engine, zero data, precision checks. |
| [`03-research/`](03-research/) | The research record, organised in numbered phases (0–214): memos, proofs, audits and certificates. Indexed in [`03-research/README.md`](03-research/README.md). |
| [`04-papers/`](04-papers/) | Papers 01–58. |
| [`05-meta-and-planning/`](05-meta-and-planning/) | Plans, audits and the master index of all routes attempted for the sign ([`ROUTES-MASTER-INDEX.md`](05-meta-and-planning/ROUTES-MASTER-INDEX.md)). |
| [`06-alpoge-verification/`](06-alpoge-verification/) | Independent compilation and axiom check of Alpoge's Lean archive: build logs, axiom check, checksums and scripts. |

## Building the papers

Each paper folder in `04-papers/` contains a self-contained LaTeX source `main.tex` and the compiled
PDF. To rebuild, run `pdflatex main.tex` three times inside the folder (so that references and the
table of contents settle); some folders give a `-jobname` in their own README so that the PDF
carries a descriptive name. The numerical certificates are reproduced by the scripts kept beside
each paper or in the phase folders cited in it; the computational core they rely on is described
in [`02-foundations/`](02-foundations/).

## Conventions and status labels

Every result in the papers and in the research record carries one of the following labels.

| Label | Meaning |
|---|---|
| PROVED | Complete proof in the text, checked. |
| CITED | Taken from the literature, with reference. |
| CONDITIONAL | Proved under an explicitly stated hypothesis. |
| ARGUED | A proof sketch or argument with an identified gap; not relied upon. |
| NUMERICAL | Supported by computation (interval-certified where stated); not a proof unless certified. |
| NO-GO | A negative result: a route or class of constructions shown not to work. |
| OPEN | Not established. |

A label is changed only on a written proof or a recorded retraction; retractions are recorded in the phase folder
where they occurred. Papers 01–45, 47 and 48 claim no proof of the Riemann hypothesis; Paper 46
with Papers 49–56 obtains it as described above, and Paper 58 gives the same chain in a single
volume.

## Language

Papers, READMEs and indices are in English. Many working memos of the later phases are written in
Spanish.

## Author

David Alejandro Trejo Pizzo, independent researcher.
