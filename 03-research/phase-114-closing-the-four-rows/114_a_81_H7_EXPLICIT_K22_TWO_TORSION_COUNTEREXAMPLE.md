# 114.a.81 — H7: the tempting K2,2 two-torsion core is actually zero

```
+-------------------------------------------------------------------------+
| CANDIDATE   Two depth-two binary trees, K2,2 leaf incidence, signs + on  |
|             one row and - on the other.                                 |
| SYMMETRY    A row/column swap identifies C with -C.                      |
| LOCAL VIEW  No unary/equal-color vertex or parallel-edge cancellation.   |
| MACRO VIEW  C is a binary other-ruling context applied to the first      |
|             cancellation generator x_0.                                 |
| CONSEQUENCE Equivalence-ideal closure gives C~0.  It is not 2-torsion.   |
| CORRECTION  Fixed-incidence local confluence does not present the full    |
|             contextual cancellation congruence.                          |
+-------------------------------------------------------------------------+
```

## 1. The candidate and its sign symmetry

Use two rooted depth-two binary trees.  The input tree has root `r`,
children `r_0,r_1`, and leaves `r_{ij}` under `r_i`.  The output tree has
root `l`, children `l_0,l_1`, and leaves `l_{ij}` under `l_j`.  Roots have
orientation `0`, depth-one vertices have orientation `1`, and

\[
 \sigma(l_{ij})=r_{ij},\qquad \mu(l_{ij})=(-1)^i.                    \tag{1.1}
\]

The internal incidence is `K2,2`.  Simultaneously sending
`(i,j)` to `(1-i,1-j)` preserves the trees, orientations and `sigma`, while
changing `mu` to `-mu`.  Hence

\[
 C\cong-C.                                                           \tag{1.2}
\]

There is no *local fixed-incidence* redex: every internal arity is two,
colors alternate and there is only one edge at each `K2,2` endpoint pair.
The error was to infer nonzeroness from this local fact.

## 2. C is a contextual cancellation image

Let `x_0` be the first-ruling cancellation generator: two boundary strands
indexed by `i in {0,1}`, with signs `(-1)^i`, between orientation-`0`
binary corollas.  Insert the orientation-`1` binary corolla as a common
multiplication/contraction context.

Formula (10.19) replaces the boundary index `i` by the Cartesian pair

\[
 (i,j)\in\{0,1\}\times\{0,1\}.                                     \tag{2.1}
\]

One intermediate vertex remembers `i`, the other remembers `j`; hence the
four strands join every `r_i` to every `l_j`, retaining sign `(-1)^i`.
This is exactly (1.1).  Relation (10.17) is the graphical interchange
between the two factorizations.

Because `E_cancel` is an equivalence ideal, it is closed under the common
multiplication/contraction context.  From `x_0~0` one obtains

\[
 C\sim0.                                                             \tag{2.2}
\]

Thus the sign symmetry (1.2) does not yield a nonzero order-two element.

## 3. Correction to the local-core claim

`a_79` proves termination and confluence only for the restricted rewrite
system which deletes visible opposite parallel strands and then performs
tree pruning/reduction on a fixed incidence presentation.  It does **not**
prove that every context instance of `x_0,x_1` decomposes into those visible
deletions.  The `K2,2` datum is a counterexample to that presentation-
completeness assertion: it is locally irreducible but zero in the full
contextual congruence.

Consequently the earlier nonzero/torsion verdict and the unconditional
odd-prime conclusion attempted in `a_80` are retracted.  The actual gate is

> **H7-MACRO-CONTEXT-SAT.** Describe the integral relation system generated
> by all multiplication/contraction context images of `x_0,x_1`, modulo
> consistent commutativity, and prove or refute its `p`-saturation.

This returns to the colon-congruence criterion of `a_76`, now with a minimal
example showing why fixed-incidence cancellation is insufficient.
H7-PRIME-REG and the completed-lattice route remain open; no counterexample
to them has been obtained here.

## 4. Verification scope

`114_a_81_h7_k22_two_torsion_verify.py` checks the trees, `K2,2` incidence,
sign-reversing automorphism, absence of local redexes, and the Cartesian
index/sign identity produced by placing `x_0` in the binary other-ruling
context.  It records `C~0` and rejects the earlier nonzero/torsion verdict.

Primary source: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (10.16)--(10.21).
