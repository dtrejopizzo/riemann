# Paper 48: Routes to Weil positivity on finite intervals — a cartography of attempts, barriers and open problems

## What the paper studies

A survey. For T > 0 the truncated Weil quadratic form on test functions supported in (−T, T) is the difference of an
archimedean form and a finite prime form. The "window problem" asks that it be nonnegative on primitive functions
(both Tate moments zero). By Weil's criterion, the window problem for every T is equivalent to the Riemann hypothesis.
The paper maps the routes tried toward this problem and toward related positivity criteria (Li–Keiper, Herglotz–Pick,
de Branges, Kreĭn spaces, Hodge-index transfers), both in the literature and in Papers 01–45 and 47 of the series. It groups
them into twenty-six families. For each family it gives the idea, what was obtained, the mechanism of failure, and
whether the route is closed by a theorem (and for which class of arguments), closed as attempted, or open. The paper
proves no new sign and claims no progress toward the Riemann hypothesis. It defines everything it uses.

## What is proved in the paper

Full proofs are given for the following.
- The explicit formula on (−T, T) in the paper's normalization (Theorem 2.1). Elementary properties, the polar-block
  equivalence and convexity in the weights (Propositions 2.7–2.9).
- The structure of the window problem: the Lévy–Khintchine form of the archimedean symbol (Prop. 3.1); a lower bound
  (2t₀/π)T − 3 for the archimedean negative index on primitive functions (Theorem 3.2); interlacing, sign changes
  and monotonicity of λ(T) in T (Props. 3.4–3.7). Also concavity in the weights (Prop. 6.1) and the falsifier
  principle (Prop. 7.2).
- Barriers: the isolation lemma (Lemma 8.1); archimedean indefiniteness (Prop. 8.2); indefiniteness of every finite
  prime part (B6, 8.3); identities valid for all multiples cΛ carry no sign for T > ½ log 2 (B1, 8.4); conditions
  stable under a large change of one coefficient cannot decide windows T > ½ log q, for any integer q ≥ 2 and either sign of the change (B11, 8.5); sublevel criteria
  cannot certify nonnegativity (B4, 8.6).
- Elementary propositions in the family sections. Among them: the polarization statement (Prop. 9.3), weak duality
  (Prop. 12.2), flat-top weights vanishing at infinity are never positive definite (Prop. 12.5), the
  even sector and one negative direction (Prop. 13.2), the negativity of the window symbol near 0
  (Prop. 13.3), the finite-modification barrier for prime-side estimates (Prop. 19.1), a Landau-type one-sided
  criterion (Prop. 19.2), the rationality obstruction (Prop. 21.3), the window transport identity (Prop. 22.3), the
  absence of T-uniform coercivity (Prop. 22.4), the bound κ* ≥ −C₀/4 ≈ 1.343 (Prop. 23.1), and the polar–prime
  inequality as an exact restatement of the even window problem (Prop. 25.2).

## Cited, conditional, heuristic, numerical, announced

- Cited: positivity on primitive functions for 0 < T ≤ log 2 (Paper 42, Theorem 9.18 and Corollary 9.20), with the explicit margin λ(T) ≥ 1.1599·10⁻⁴ for T ≤ ½ log 3 (Paper 42, Theorem 9.18); Yoshida's
  theorem; Haynsworth inertia additivity (Prop. 13.1, cited; the form version is the completion of squares of Prop. 2.8); Weil's and Li's criteria; results of Papers 08, 10, 18, 25, 36, 37, 38, 39, 45 and 47 with statement
  numbers; the de Bruijn–Newman, Jensen-polynomial and Beurling literature.
- Conditional: statements proved under a hypothesis written into them. Examples are the Kreĭn-space count of
  Paper 18 under a finite-quartet hypothesis, and the coercivity hypothesis of Paper 08, a lower bound on the on-line
  sampling norm that is not known to follow from or to imply the Riemann hypothesis.
- Heuristic: general claims about whole families of routes, for example that every square route quadratic in the
  weight can be rewritten through a polar decomposition, and that a useful transport must be nonlinear.
- Numerical: values such as κ* ≈ 7.431 at τ ≈ 3.777, the threshold of archimedean indefiniteness (about 0.58–0.60),
  and margin estimates. Values taken from unpublished computations are flagged as not reproducible from the paper.
- Announced (proofs not in the paper or in published sources; never premises of a proved statement): certified
  positivity beyond log 2; the matching upper bound for the archimedean count; the exponential bounds on the margin;
  barriers B2, B3, B5, B7–B10 (announced, in part only argued) and B12 (argued); the no-go for arithmetic sums of squares at T ≥ ½ log 3. Some external
  certificates (up to ½ log 15) could not be located in refereed form and are described as such.
- Open: the window problem and its exact restatements; the gap (½ log 2, ½ log 3) for arithmetic sums of squares;
  the Beurling frontier for remainder exponents θ ≤ 1/3; the families never carried out; the residues listed in §25.

## Known versus new

The setting, the criteria and most cited theorems are classical. What is new is the classification: each closure is
stated relative to an explicitly declared class of arguments. Barriers B1, B4, B6 and B11 are proved here in
hypothesis-free form, along with the elementary propositions listed above.

## Files

- `main.tex`: the source (a single file, bibliography included).
- `routes-to-weil-positivity.pdf`: the compiled paper, 98 pages.
- `README.md`: this file.

Build: `pdflatex -interaction=nonstopmode -halt-on-error -jobname=routes-to-weil-positivity main.tex`, run three times.
