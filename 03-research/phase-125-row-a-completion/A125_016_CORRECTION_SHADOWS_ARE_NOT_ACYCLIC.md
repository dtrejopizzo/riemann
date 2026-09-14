# A125.016 — correction to A125.014: the full shadow is not acyclic; distinct classes have isomorphic shadows

Status: `PROVED-IN-REPOSITORY`.  Corrects A125.014 Theorem 1.1, Theorem
3.1(c), §2 and §4; the label of A125.015 stands with the corrected proofs and
imports, recorded in Paper 43.

## 1. The error

A125.014 Theorem 1.1 asserted that `Tr_A(E_w)` is acyclic over `C` for every
`w∉Γ`, and Theorem 3.1(c) gave the finite-place local factor as the Koszul
complex `[C →(σ_p−1) C]`.  Both are wrong for the actual coefficient algebra
`E_p = Cχ_p ⊕ F_p`.  The origin `x_p=0` is fixed by every external dilation,
`E_p/F_p = C` is the value at `0` with trivial twist, and the coefficient
algebra is totally disconnected, so the fixed point has no tangent direction.
Its Hochschild contribution is `C[0]`, rank one, independent of the twist.
This is exactly P123.084 (1): the degree-zero shadow of a twist is `D`,
"induced by coefficientwise evaluation at the common coordinate origin …
independent of the external twist".  The Koszul complex with differential
`σ−1` lives in the smooth polynomial model `R[z]` of P123.060 (1.1), not in
`E_p`.

## 2. The correction

* Finite-place local factor: `HH(E_p,(E_p)_σ) ≃ C[0]` for `σ_p≠1`, by the
  explicit continuous shell homotopy plus excision (Paper 43, Theorem 7.1(c)).
* The degeneracy statement is replaced by the **isomorphic-shadows theorem**
  (Paper 43, Theorem 7.4): two unit classes at one prime, both free on the
  boundary, have isomorphic full shadows.  Corollary 7.5 (no additive
  invariant is Weil-strength) follows with a cleaner proof than before.
* The invariant is the **analytic relative trace** of the corpus
  (P123.042–059, P123.105–110), whose local factor `|σ|^{1/2}/|1−σ|_p` is the
  Fourier orbital integral at the fixed point; P123.060 §4 identifies it with
  the torsion of the smooth-model Koszul complex.  "Torsion" is retained only
  in that sense.
* The exact mixed computation A125.014 (5.1) is unchanged: it uses only the
  local factors and cancellation of common lattice terms.
* Import I-3 of A125.015 (finite-place Koszul localization) is withdrawn and
  replaced by Wodzicki excision for the H-unital ideal `F_p`, with
  H-unitality proved by the explicit homotopy.

## 3. Why the insight survives and sharpens

The claim was "complexification kills cohomology, not torsion".  The correct
form is: at a totally disconnected fixed point there is no cohomological
trace of the arithmetic at all — not even an acyclic complex to take torsion
of — and the arithmetic lives entirely in the analytic normalization of a
rank-one class.  That is stronger, and it is why the smooth model's torsion
and the analytic trace must be compared (P123.060 §4) rather than identified
by fiat.
