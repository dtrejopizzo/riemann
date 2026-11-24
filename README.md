# The Riemann Program

An independent research program, a little over eleven years long, on one question: can Weil's
proof of the Riemann hypothesis for curves over finite fields be carried out, row by row, over
$\mathrm{Spec}\,\mathbb Z$?

Papers 43, 44, 45 and 46 are the answer given here: one paper for each of the four rows of Weil's
proof, on the idele class group of $\mathbb Q$. The last step, the sign on every window, is closed
by a theorem of **Levent Alpoge**. This repository contains the papers, the complete research
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

       (1) W_T ≥ 0 for every T  <=>  RH                    [this paper]
       (2) enough: G(x) ≤ C x^θ on arbitrarily large
           windows [Y, Y^(3/2)], for every θ > 1/2           [this paper;
                                                              Landau's method]
       (3) that bound follows from a mean estimate
           at a single point                                 [this paper]
       (4) the mean estimate follows from a slope inequality
           for Hermitian lattices (Harder–Narasimhan, Stuhler,
           Grayson, Bost) plus a "column package"            [this paper]
       (5) families carrying a column package with uniform
           constants exist                                   [Levent Alpoge]
              |
              v
       RH, and W_T ≥ 0 on every window
```

| Row | Step in Weil's proof | Paper | What it contains |
|---|---|---|---|
| A | Correspondences, involution, trace, bidegree | [43](04-papers/43-row-a-correspondence-algebra/) | A convolution algebra of semilocal idele class correspondences with its involution and trace; the two Tate characters give the bidegree and define the primitive subspace. |
| B | Frobenius | [44](04-papers/44-row-b-arithmetic-family/) | A Frobenius measure for every positive integer with prime divisors in $S$; its contact with the diagonal has weight $\Lambda(n)/\sqrt n$, supported on prime powers. |
| C | Fixed-point (explicit) formula | [45](04-papers/45-row-c-explicit-formula/) | Weil's explicit formula for the radial trace: the self-intersection of a radial class equals its two Tate moments minus a sum over the nontrivial zeros of $\zeta$. |
| D | Intersection inequality (the sign) | [46](04-papers/46-row-d-sign-radial-intersection-form/) | *The sign of the radial intersection form on the idele class group*, with its annex *Column packages for character families*: $W_T\ge 0$ on every window, and the Riemann hypothesis. |

### Who did what

Rows A, B and C are built entirely on the work of the mathematicians listed next to them; what is
done here is to carry the constructions through in one setting and write down every proof. In
row D, steps (1)–(4) belong to Paper 46, on top of classical tools. For years the sign was known
here only on a bounded range, certified up to $T=2.8022$. The missing piece was step (5), global
positivity.

Step (5) is Levent Alpoge's. It comes from his character-family argument, released as a Lean 4
formalization: <https://alpo.ge/remark.pdf>.

### What is and is not claimed

- **Alpoge's formalization proves RH on its own.** His proof is self-contained and does not need
  these papers. Row D is not an independent proof: it takes step (5) from his development and
  shows that this is exactly the positivity that Weil's programme over $\mathrm{Spec}\,\mathbb Z$
  was missing. The deduction of RH in Paper 46 uses only that paper; rows A–C enter in the
  structural statement, $W_T\ge 0$ on every window. So: Alpoge proves RH, and these four papers
  are the same statement reached along Weil's four components.
- **Step (5) rests on his Lean development.** It has not yet been written out on paper in full.
  The annex to Paper 46 is a first attempt at a readable version: it proves the reductions,
  identifies which steps are known mathematics that the formalization re-proves (Siegel–Weil,
  Borel–Harish-Chandra, discrete series, base change, zero-density estimates, and more), and
  states exactly the new statements it takes from the formalization.
- **None of this has been refereed.** There may be mistakes. Corrections, questions and attempts
  to break any step are very welcome.

### Checks

- [`06-alpoge-verification/`](06-alpoge-verification/): an independent compilation of Alpoge's
  archive, with the build log, the axiom check of the main theorem and the dependency report.
  They will be placed there when the run finishes.
- A Colab notebook,
  [`positivity-radial-intersection-form.ipynb`](04-papers/46-row-d-sign-radial-intersection-form/positivity-radial-intersection-form.ipynb),
  in the Paper 46 folder. It reproduces with interval arithmetic the rigorous certificates of
  $W_T\ge 0$ on bounded windows (up to $T=2.8022$ in the paper) and lets you try the method for a
  $T$ of your choice; and it computes the prime sum $G(x)$ directly from the primes, with no zeros
  of zeta involved, and compares it with the bound given by Alpoge's theorem. The notebook does
  not prove global positivity, and no computation can: it shows the two pieces at work as far as
  a machine reaches, and where the proof takes over.

## Acknowledgements

To **Levent Alpoge**, first of all. His work proves the Riemann hypothesis completely, and it also
supplies the component with which the proof along Weil's route over $\mathrm{Spec}\,\mathbb Z$ is
closed here: the existence of families carrying a column package with uniform constants. That is
the decisive input, and the whole mathematical community owes that step to his work.

To the mathematicians whose lifelong dedication made it possible even to attempt this: André Weil,
Alain Connes, Caterina Consani, Masatoshi Suzuki, Enrico Bombieri, Hiroyuki Yoshida, Ralf Meyer,
Jean-François Burnol, John Tate, and the many others cited in the papers.

## Papers 43–48

| Paper | Title | Content |
|---|---|---|
| [43](04-papers/43-row-a-correspondence-algebra/) | A Correspondence Algebra and the Weil Distribution on Semilocal Idele Class Groups | Row A. |
| [44](04-papers/44-row-b-arithmetic-family/) | An Arithmetic Frobenius Family on Semilocal Idele Class Groups | Row B. |
| [45](04-papers/45-row-c-explicit-formula/) | An Explicit Formula for the Trace on Semilocal Idele Class Groups | Row C. |
| [46](04-papers/46-row-d-sign-radial-intersection-form/) | The Sign of the Radial Intersection Form on the Idele Class Group | Row D, with the annex *Column packages for character families: the arithmetic inputs for the sign of the radial intersection form*. |
| [47](04-papers/47-intersection-frame-defect/) | An Intersection Frame for the Explicit Formula: Hodge-Index Transfer, a Frame Defect Theorem and a Function-Field Model | Structural theorems on the extended Weil form; no sign claimed. |
| [48](04-papers/48-routes-to-weil-positivity/) | Routes to Weil positivity on finite intervals: a cartography of attempts, barriers and open problems | Survey of the routes attempted toward the sign before step (5) was available: twenty-six families, with the mechanism of failure and the status of each, and the proved barriers. |

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
| [`06-alpoge-verification/`](06-alpoge-verification/) | Independent compilation and axiom check of Alpoge's Lean archive (in preparation). |

## Building the papers

Each paper folder in `04-papers/` contains a self-contained LaTeX source `main.tex` and the compiled
PDF. Paper 46 has in addition `annex.tex`; its README gives the build commands. To rebuild, run `pdflatex main.tex` three times inside the folder (so that references and the
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
obtains it from Alpoge's theorem, as described above.

## Language

Papers, READMEs and indices are in English. Many working memos of the later phases are written in
Spanish.

## Author

David Alejandro Trejo Pizzo, independent researcher.
