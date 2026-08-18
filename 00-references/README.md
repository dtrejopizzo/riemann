# 00-references — external source material

Downloaded papers (arXiv source dumps and PDFs) that the research phases and papers read from,
cited, and audited against. **Nothing in this folder is the program's own work** — it is the
literature the corpus engages with. Where a phase or paper reads one of these from source, it
says so explicitly and cites the exact result used; this README only explains what is here and
why it is grouped the way it is.

The subfolder names (`A`, `B`, `C`, `D`, `extension-clase-test`, `mas-papers`, `Puente`,
`papers-ref-2`, `papers-ref-phase-60`) were not self-documenting, so the thematic groupings below
are **reconstructed from the actual paper contents**, not carried over from any original intent.
Titles were extracted from each source's own `\title` (or, for two PDFs with no recoverable
`\title`, from the first page of text) — flagged individually where extraction was not possible.

## Top-level loose files

| File | Title | Author(s) |
|---|---|---|
| `1001.0448v3.pdf` | Generators of Modules in Tropical Geometry | Shuhei Yoshitomi |
| `2006.13771v1.pdf` | Weil Positivity and Trace Formula — the Archimedean Place | Alain Connes, Caterina Consani |
| `2301.00421v3.pdf` | On the Hilbert Space Derived from the Weil Distribution | Masatoshi Suzuki |
| `2307.06748v1.pdf` | On the Metaphysics of $\mathbb F_1$ | Alain Connes, Caterina Consani |
| `2310.18423v2.pdf` | Zeta Zeros and Prolate Wave Operators — Semilocal Adelic Operators | Alain Connes, Caterina Consani, Henri Moscovici |
| `connes-moscovici-2022-...pdf` | The UV Prolate Spectrum Matches the Zeros of Zeta | Alain Connes, Henri Moscovici |
| `draft4.pdf` | Prolate Spheroidal Operator and Zeta | Alain Connes, Henri Moscovici |
| `Zeta-zeros-and-prolateproofs-final-2024.pdf` | (Tusi Math. Research Group typeset copy of the Connes–Consani–Moscovici prolate-operator proofs; same result family as `2310.18423v2.pdf`) | — |
| `arXiv-2511.11199v1/` (full source, `RH.tex`) | The Riemann Hypothesis Emerges in Dynamical Quantum Phase Transitions | — |

`2310.18423v2` also appears, separately downloaded, in `papers-ref-2/`; `2006.13771v1` and
`2310.18423` also appear again in `papers-nuevos/extension-clase-test/` — kept as-is rather than
deduplicated, since each copy was pulled independently by a different research thread.

## `papers-nuevos/A` — the Connes–Consani $\mathbb F_1$/arithmetic-site core

The primary-source bibliography for the Connes–Consani programme itself: the arithmetic site and
scaling site (the two short CRAS notes), Haran's *Geometry over $\mathbb F_1$*, the Riemann–Roch
strategy for $\overline{\mathrm{Spec}\,\mathbb Z}$, Hochschild homology and $\zeta$-cycles,
*Knots, Primes and the Adele Class Space*, the Jacobian of $\overline{\mathrm{Spec}\,\mathbb
Z}$, and the absolute geometry of $\mathrm{Spec}\,\mathbb Z$ via the Fargues–Fontaine curve.
This is the source material behind every place the corpus reads Connes–Consani directly (see
`03-research/AUDIT_CONSOLIDATED.md` §3 and `NO-GO-LIST.md` MW-5 for what the corpus concluded from
it).

| Folder | Title |
|---|---|
| `arXiv-1405.4527v1` | *The Arithmetic Site* (CRAS note) |
| `arXiv-1502.05580v1` | Geometry of the Arithmetic Site |
| `arXiv-1507.05818v2` | *The Scaling Site* (CRAS note) |
| `arXiv-1509.05576v1` | An Essay on the Riemann Hypothesis |
| `arXiv-1709.05831v1` | Geometry over $\mathbb F_1$ (Haran) |
| `arXiv-1805.10501v1` | The Riemann–Roch Strategy |
| `arXiv-2205.01391v2` | Riemann–Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$ |
| `arXiv-2207.10419v1` | Hochschild Homology, Trace Map and $\zeta$-Cycles |
| `arXiv-2401.08401v1` | Knots, Primes and the Adele Class Space |
| `arXiv-2602.15941v1` | On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$ |
| `arXiv-2606.06604v1` | On the Absolute Geometry of $\mathrm{Spec}\,\mathbb Z$ and the Fargues–Fontaine Curve |

## `papers-nuevos/B` — Deninger's own programme, and its newest arithmetic input

Deninger's foundational papers on dynamical systems for arithmetic schemes and foliated spaces —
the source the corpus's own reading in `phase-107`/`phase-43`/`AUDIT_CONSOLIDATED.md` §3 is checked
against — plus one much newer paper that the corpus currently treats as its best row-(a) candidate.

| Folder | Title |
|---|---|
| `arXiv-1807.06400v4` | Dynamical Systems for Arithmetic Schemes |
| `arXiv-2301.11643v1` | Primes, Knots and Periodic Orbits |
| `arXiv-math0204110v1` | Number Theory and Dynamical Systems on Foliated Spaces |
| `arXiv-math0505354v1` | Arithmetic Geometry and Analysis on Foliated Spaces |
| `arXiv-2504.15767v3` | Is There a Birch and Swinnerton-Dyer Conjecture for Dedekind Zeta Functions? |
| **`arXiv-2508.05329v1`** | **Rational Witt Vectors and Associated Sheaves** — Deninger's Theorem 5.1 (`W_rat(O(X)) ≅ Corr(X,A)`), the source of `OPTIONS.md` §1a (G-4) and the "BUILT-MODULO-GAP" row-(a) candidate in `phase-114_a_03`. |

## `papers-nuevos/C` — foliated dynamical systems and leafwise cohomology

The technical machinery Deninger's conjecture actually runs on: leafwise cohomology, dynamical
zeta functions on foliated systems, Riemannian foliations of bounded geometry, and Connes' own
spectral interpretation of the zeros. This is what `03-research/phase-42-hodge-dynamics` and
`phase-43-hodge-foliated-specZ` read from source to test whether $\mathrm{Spec}\,\mathbb Z$
can carry a Kähler–Riemann foliation (it cannot, in the realized witness — see `NO-GO-LIST.md`).

| Folder | Title |
|---|---|
| `arXiv-1307.3851v1` | On the Analogy between $L$-functions and... (foliated dynamical zeta) |
| `arXiv-1712.04181v2` | On the Leafwise Cohomology and Dynamical Zeta Functions for Fiber Bundles over the Circle |
| `arXiv-1905.12912v3` | Analysis on Riemannian Foliations of Bounded Geometry |
| `arXiv-1912.02159v1` | Leafwise Cohomological Expression of Dynamical Zeta Functions on Foliated Dynamical Systems |
| `arXiv-2410.20758v1` | Regularized Determinant Formulas for the Zeta Functions of 3-Dimensional Riemannian Foliated Dynamical Systems (Álvarez López, Kim, Morishita) — proves a formula conjectured by Deninger |
| `arXiv-math0412277v3` | A Spectral Interpretation for the Zeros of the Riemann Zeta Function (Connes) |

## `papers-nuevos/D` — the arithmetic Hodge index theorem and Riemann–Roch over arithmetic surfaces

Row (d)'s own bibliography: the arithmetic Hodge index theorem for adelic line bundles (both
parts), quadratic Riemann–Roch formulas, the Riemann–Hurwitz formula for arithmetic surfaces, and
numerical cohomology for arithmetic surfaces. This is the literature `THE_BACKWARD_MAP.md` and
`OPTIONS.md` §1d (R16 — does a quadratic Riemann–Roch exist over $\mathrm{Spec}\,\mathbb Z$ at
all?) draw on.

| Folder | Title |
|---|---|
| `arXiv-1304.3538v1` | The Arithmetic Hodge Index Theorem for Adelic Line Bundles I: Number Fields |
| `arXiv-1304.3539v2` | The Arithmetic Hodge Index Theorem for Adelic Line Bundles II |
| `arXiv-1810.06342v2` | The Arithmetic Hodge Index Theorem and Rigidity of Dynamical Systems over Function Fields |
| `arXiv-2403.09266v1` | Quadratic Riemann–Roch Formulas |
| `arXiv-2510.08033v2` | Riemann–Hurwitz Formula for Arithmetic Surfaces |
| `arXiv-2512.01811v2` | Numerical Cohomology for Arithmetic Surfaces and Applications |

**Not a paper:** `deel-David Alejandro Trejo Pizzo-contract-mz4wej8.pdf` — an unrelated signed
document, not a reference. Left in place rather than moved without asking; flagged here so it is
not mistaken for one of the sources above.

## `papers-nuevos/extension-clase-test` — loose PDF batch (Weil positivity / explicit formula)

A standalone batch of PDFs, not arXiv source dumps, covering Weil's quadratic form and expository
treatments of the explicit formula.

| File | Title | Author(s) |
|---|---|---|
| `1910.14368.pdf` | The Scaling Hamiltonian | Alain Connes, Caterina Consani |
| `2006.13771.pdf` | Weil Positivity and Trace Formula — the Archimedean Place | Connes, Consani *(duplicate of the top-level copy)* |
| `2310.18423.pdf` | Zeta Zeros and Prolate Wave Operators | Connes, Consani, Moscovici *(duplicate of the top-level copy)* |
| `2511.22755.pdf` | Zeta Spectral Triples *(duplicate of `papers-ref-phase-60/arXiv-2511.22755v1`)* | — |
| `2606.09096.pdf` | Weil's Quadratic Form via the Screw Function | Masatoshi Suzuki |
| `math-0404394.pdf` | Li Coefficients for Automorphic $L$-Functions | Jeffrey C. Lagarias |
| `math-9810169.pdf` | The Explicit Formula in Simple Terms | Jean-François Burnol |
| `math-9902080.pdf` | The Explicit Formula and the Conductor Operator | Jean-François Burnol |

## `papers-nuevos/mas-papers` — tropical geometry

A self-contained bibliography on tropical Riemann–Roch and Hodge theory: tropical complexes,
combinatorial tropical surfaces, a specialization inequality, Hodge theory for tropical varieties,
Jacobians of tropical curves, and non-additive geometry / Frobenius correspondences (Connes–Consani
again, in the tropical/$\mathbb F_1$ register). This is the natural place to look first for
`OPTIONS.md` §1d's question — tropical geometry is exactly a setting where Riemann–Roch is already
known in a combinatorial, non-classical form, and checking whether it is genuinely quadratic there
is cheap.

| Folder | Title |
|---|---|
| `arXiv-1308.3813v4` | Tropical Complexes |
| `arXiv-1506.02023v1` | Combinatorial Tropical Surfaces |
| `arXiv-1511.00650v2` | A Specialization Inequality for Tropical Complexes |
| `arXiv-1703.02325v1` | Homological Algebra in Characteristic One (Connes, Consani) |
| `arXiv-1711.07900v4` | (tropical/floor-decomposition paper — see `epiga_vol2_jell_al.tex`; no plain `\title` recovered) |
| `arXiv-2007.07826v1` | Hodge Theory for Tropical Varieties |
| `arXiv-2209.08536v3` | Non-Additive Geometry and Frobenius Correspondences |
| `arXiv-math0612267v2` | Jacobians of Tropical Curves |

## `papers-nuevos/Puente` — a Deninger/Connes–Consani bridge fragment

`arXiv-2508.15971v5/Deninger_Connes-Consani.tex` — a single file, no recoverable `\title`/`\author`
(likely an extracted excerpt rather than a full paper source). Its acknowledgements thank Deninger,
Connes, Consani, Borger and Morava directly, consistent with the folder's name ("Puente" = bridge):
kept here as the one candidate source for a direct technical link between the two programmes,
unresolved as to its exact provenance.

## `papers-ref-2` — the Connes–Consani–Moscovici prolate-operator programme

| Folder | Title |
|---|---|
| `arXiv-2106.01715v1` | Spectral Triples and $\zeta$-Cycles |
| `arXiv-2112.05500v1` | Prolate Spheroidal Operator and Zeta |
| `arXiv-2310.18423v2` | Zeta Zeros and Prolate Wave Operators — Semilocal Adelic Operators *(duplicate; see top-level)* |
| `arXiv-2402.13082v1` | Heat Expansion and Zeta (Connes) |

## `papers-ref-phase-60` — the sources `phase-60`'s CCM tribunal reviewed directly

| File | Title |
|---|---|
| `arXiv-2501.06560v1` | Knots, Primes and Class Field Theory |
| `arXiv-2511.22755v1` | Zeta Spectral Triples |
| `arXiv-2511.23257v1` | Quadratic Forms, Real Zeros and Echoes of the Spectral Action |
| `arXiv-2602.04022v1.tex` | (single-file source; Connes's "Letter to Riemann," per `NO-GO-LIST.md` §VII CAND-1) |
| `arXiv-2606.06604v1` | On the Absolute Geometry of $\mathrm{Spec}\,\mathbb Z$ and the Fargues–Fontaine Curve *(duplicate of `papers-nuevos/A`'s copy)* |
| `compareplots3.pdf`, `weilcomp.png` | Supporting figures used by `phase-60`'s numerical audit, not papers. |

## Status

Reference material only. See `03-research/` for what the program actually did with any of it, and
`NO-GO-LIST.md` / `OPTIONS.md` for the conclusions drawn.
