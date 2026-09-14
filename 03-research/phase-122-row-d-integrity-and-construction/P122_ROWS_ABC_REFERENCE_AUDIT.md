# P122 — rows A/B/C reference and scope audit

## Verdict

Rows A, B and C are internally defined and largely supported in the
restricted categories stated by paper 42.  They do **not** construct the
three pieces of Weil geometry which would make row D formal:

1. mixed correspondence classes on one surface-like carrier;
2. an intersection product and numerical quotient on those classes;
3. a Hodge-index/Riemann--Roch theorem for that mixed quotient.

Thus A/B/C supply the explicit-formula data to be controlled by D, but do
not logically imply D.  This is not merely an external-review objection:
paper 42 states each limitation explicitly.

## A — intrinsic periodic--Deligne--nuclear square

### External anchors checked

* Connes--Consani construct the relevant arithmetic `S`-algebra framework
  and prove that `HZ wedge_S HZ` is not isomorphic to `HZ` (Proposition 6.7
  in arXiv:1502.05585v1; numbering can differ in later typesetting).
  This supports the noncollapse motivation for the spherical product.
* Clausen--Scholze is invoked for symmetric monoidality of solidification.
  That invocation types the completed topological algebra; it is not an
  intersection theorem.

### Repository construction

Theorem `thm:rowaDN` proves that a tuple satisfies the bespoke Definition
`def:strongrowa`.  The tuple contains a sheafified Day-smash carrier,
external divisor lines, a selected periodic coefficient object, determinant
and code data, and a finite locally free module over a nuclear Dirichlet
algebra.

### Exact status

`PROVED-RELATIVE-TO-CUSTOM-CONTRACT`.

It is not a regular proper arithmetic surface, does not have a constructed
Neron--Severi group for the mixed Frobenius classes, and has no mixed
Riemann--Roch or Hodge-index theorem.  The paper itself says that extending
the ruling determinant/effectivity to completed mixed classes is still
required for D.

## B — Witt decorated correspondences

### External anchors checked

The official TeX source of Haran, arXiv:2209.08536v3, contains:

* (12.35): the Hilbert completion with orthogonal cyclotomic basis
  `phi_n` and norm squared `varphi(n)`;
* (12.37): the adjoint/Verschiebung family and its multiplicative zeta
  series, with `F_m^* phi_n=phi_(mn)`;
* (13.37): `tr(lambda_t(phi_n))=Phi_n(t)`.

The official source downloaded from arXiv has SHA-256
`0b9b52e0c8f24b15fb383f5089c0bbce5ff9c765c479c41b7d85703db421ad7a`,
identical to the repository copy.  Hence the source anchors used for the
cyclotomic calculation are genuine.

The elementary consequence

\[
 \log|\Phi_n(1)|=\Lambda(n),\qquad n>1,
\]

is correct.

### Repository construction

The object

\[
 \Gamma_n=(F_n,\rho_n,\mathcal T_n,P_n)
\]

lives in the graph-image of a product of four monoidal categories.  Its
composition is componentwise.  The fourth product is a deliberately
reduced `H^0` contact product, not composition of derived intersections.

### Exact status

`PROVED-AS-DECORATED-GRAPH-IMAGE-FAMILY`.

All bare supports are the same diagonal.  No pullback/product/pushforward
calculus on a triple product, excess-intersection formula, or Chow lift is
constructed.  Haran's own terminal warning says that the function-field
proof really needs intersection theory on the surface; the Witt action
alone does not replace it.

## C — nuclear Lefschetz character

### External anchor checked

Meyer's arXiv:math/0412277 constructs nuclear Frechet spaces and a scaling
representation, proves summability, identifies the spectrum with the
nontrivial zeta zeros, and proves in Theorem 5.8 that the explicit formula is
the character formula.  Paper 42 accurately labels this analytic engine a
black box.

### Repository construction

Paper 42 identifies the positive finite coefficients in Meyer's trace with
the determinant degrees of the B-contact complexes, keeps multiplicative
correspondences separate from the nonmultiplicative determinant degree, and
packages the two finite orientations, polar terms and archimedean term in a
nuclear supercharacter.

### Exact status

`PROVED-AS-MEYER-CHARACTER-WITH-WITT-COEFFICIENT-PROVENANCE`.

It is not an intersection number on A.  The completed cohomological object
is Meyer's Poisson quotient, not global cohomology constructed on the
spherical square.  The scalar supertrace retains the explicit formula but
does not provide the mixed intersection product or its signature.

## Dependency consequence

The honest chain is

```text
A: carrier/ruling/coefficient infrastructure
  + B: decorated multiplicative labels and Lambda contact masses
  + C: Meyer's scalar nuclear explicit formula
  -> exact Hermitian form B_nuc
  -> row D asks for its primitive sign
```

There is currently no green arrow

```text
A + B + C -> mixed numerical intersection theory -> Hodge index.
```

Calling A/B/C “complete” is valid only with their displayed qualifiers.  It
cannot be used to suggest that the Weil proof is complete except for a
routine verification.

## What D must add

D must add information not present in the scalar character:

* a common mixed carrier for the decorated classes;
* an intersection/duality operation before scalar supertrace;
* a numerical-equivalence quotient containing the two rulings and the
  infinite-rank mixed sector;
* an independently proved Hodge--Rosati or Riemann--Roch signature theorem;
* comparison of its pairing with `B_nuc` only after the preceding items are
  constructed.

Without those additions, any source-side “D” which simply declares an
oriented conservation law on the kernel is a restatement of row D.
