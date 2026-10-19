# Paper 46 — An Intersection Frame for the Explicit Formula

**Hodge-index transfer, a frame defect theorem and a function-field model.**

What it proves. On the class D^W of C² functions decaying like e^{-(1+ε)|t|}, Weil's explicit formula defines a
bilinear form. The paper gives it the structure Weil's proof uses on C×C: degree, effective cone, radical, an
ample class (the Pólya class K, with Φ_K = ξ) and the affine duality E ↦ K − E. It proves that Hartshorne's
Hodge-index argument transfers (conditional on a function h⁰ with three clauses), and then that no such h⁰
exists (given the verified simplicity of the first zero of ξ): a cosh inequality with constant 0.99846… < 1
makes the effective cone too thin. The same defect holds on an elliptic curve over F₂, where the Hodge index
theorem is true; there the frame's cone is the cone on the Frobenius graphs, K is half the ample ruling class,
and the missing classes are the graphs of sums m + nπ.

Status. Structural theorems with honest labels; not a paper on row D. The earlier row D manuscript that lived
in this folder (superseded by Paper 47) is kept in `archive/` with its review notes. `CHANGES_rebuild.md`
records what was kept, what was dropped and why, and the corrections made.

Build. `pdflatex main.tex` twice (amsart, no external files). 15 pages.
