# P122 — theorem-level dependency graph for rows (a)--(d)

## Status

Living audit.  This file records what the paper literally constructs, not
what the names suggest by analogy with a surface over a finite field.

## 1. The two columns are not yet objects of the same kind

Over a finite field, Weil uses one algebraic surface, algebraic
correspondences on that surface, their intersection product, and the Hodge
index theorem for that same intersection product.

The present `Spec Z` programme has three compatible realizations, but not
yet one common intersection theory:

| row | literal repository object | proved scope | missing relative to Weil |
|---|---|---|---|
| A | the tuple `A_DN` satisfying the five clauses of `def:strongrowa` | spherical carrier, external divisor lines, selected periodic coefficient cohomology, determinant/code contact, and a rank-three module over a nuclear Dirichlet algebra | it is not a regular proper arithmetic surface; its cohomology is not all bounded sections; mixed correspondence classes have no established effective cone, RR theorem or intersection product |
| B | `Gamma_n=(F_n,rho_n,T_n,P_n)` in a graph-image subcategory of a four-factor product category | faithful labels, componentwise multiplication, cyclotomic contact complex and determinant degree `Lambda(n)` | every undecorated support is the same diagonal; no pull-push/excess theory or Chow class on A is constructed; the reduced `star` product is deliberately not derived composition |
| C | Meyer's summable Poisson quotient super-representation, with the B-contact degrees inserted into its multiplier realization | the explicit formula as a nuclear supertrace, including both finite orientations, poles and the archimedean term | analytically this is Meyer's theorem; the trace is not shown to be an intersection number in the geometry of A, and there is no reverse functor to perfect Cartier complexes |
| D | the primitive sign of the nuclear/Weil form | certified only for `0<T<=log 2`; equivalent globally to RH | no mixed effectivity/RR/Hodge theorem and no independent source law forcing the sign |

Accordingly “A/B/C are complete” means complete under three explicitly
restricted contracts.  It does not mean that the characteristic-zero
counterparts of Weil's first three rows have been constructed in one
geometric category.

## 2. Row A dependency chain

The theorem called `thm:rowaDN` is a packaging theorem:

```text
Connes--Consani spherical curve X
  -> sheafified Day-smash square Y_S
  -> external ruling line objects
  -> selected periodic coefficient object
  -> regular-section cotangent and mixed Kunneth
  -> continuous determinant and code certificate
  -> reduced prime contact
  -> nuclear Dirichlet coefficient module N_DN
  -> tuple satisfying def:strongrowa.
```

The definition `def:strongrowa` was formulated for this package.  Therefore
the theorem proves internal consistency/completeness of the package, not an
external recognition theorem saying that it is an arithmetic surface with
the intersection theory needed in row D.

### Status

* Internal constructions: `PROVED-IN-REPOSITORY` under the custom contract;
  principal external anchors checked in `P122_ROWS_ABC_REFERENCE_AUDIT.md`.
* Identification with a Weil surface: not claimed.
* Mixed-class intersection/effectivity/RR: `MISSING`.

## 3. Row B dependency chain

For `n=product p^(v_p(n))` the construction combines four components:

```text
Witt Frobenius F_n
  x nuclear convolution rho_n
  x framed metric line T_n
  x reduced cyclic contact P_n.
```

The componentwise product gives `Gamma_m Gamma_n ~= Gamma_(mn)`.  The local
dynamic complex uses the cyclotomic polynomial, and

\[
 \log\Phi_n(1)=\Lambda(n)
\]

because `Phi_n(1)=p` for a prime power and `1` otherwise.  The metric frame
then supplies the central coefficient `Lambda(n)/sqrt(n)`.

This is a correct coefficient-producing mechanism if all component
constructions type-check.  But the product category enforces simultaneous
motion by definition.  It does not prove that the four components are the
realizations of a single algebraic/cohomological correspondence admitting
the operations required by an intersection theory.

### Status

* Multiplicative decorated family: `PROVED-IN-REPOSITORY`; the Haran source
  anchors and exact official-source hash are checked in the reference audit.
* Determinant coefficient: elementary once the complex is constructed.
* Honest undecorated cycle or common pull-push theory: `NOT CONSTRUCTED`.

## 4. Row C dependency chain

The genuinely analytic chain is

```text
Dirac comb -> Zeta operator Z -> Poisson equality
  -> closed quotient representations H_+^0, H_-^0
  -> summable Z/2 super-representation
  -> Meyer nuclear supercharacter
  -> explicit formula.
```

The programme adds a monoidal realization of B's labels and proves

\[
 Z\partial Z^{-1}
 =\sum_{n\ge2}\deg_{\det}(\mathbb L_n)U_n
 =\sum_{n\ge2}\Lambda(n)U_n.                       \tag{4.1}
\]

This supplies provenance for the finite coefficients.  The completed trace,
its summability and its spectral expression are imported from Meyer.

### Status

* Analytic explicit formula: `IMPORTED`; Meyer's spaces, summability and
  character theorem match the stated use, as recorded in the reference
  audit.
* Coefficient provenance from B: `PROVED-IN-REPOSITORY` under B's contract.
* Equality with an intersection number on A: `NOT PROVED` and explicitly not
  asserted.

## 5. Row D analytic target

On compact logarithmic support and the two-Tate primitive space,

\[
 q_T(F)=-B_{\rm nuc,T}(F,F)
 =\mathcal R_T(F,F)-\|\mathcal W_TF\|^2.            \tag{5.1}
\]

The row-D assertion is

\[
 q_T\ge0\quad\hbox{for every }T>0.                  \tag{5.2}
\]

Equivalently, the compact Birman--Schwinger operator has norm at most one.
This equivalence is a coordinate change, not a proof.  The certified base
interval supplies strict positivity through `T=log 2`.  P122.002 now proves
that any later failure has an attained parity first-contact radical.

Phase 121 then gives several conditional terminal descents.  In their
minimal active-prime version:

```text
first-contact radical
  -> [OPEN] active Euler-ideal tangency / oriented source law
  -> [PROVED] Cartwright overdensity
  -> F=0
  -> contradiction
  -> q_T >= 0 for all T.
```

The open arrow is logically equivalent in force to row D once the other
arrows are included.

## 6. What a genuine D must add

There are only two honest meanings of a completed D.

### D-geometry

Construct mixed correspondence classes in a single category carrying:

1. an intersection product extending the A/B local contacts;
2. a degree map and a positive class `H`;
3. an effective cone and a quadratic RR/equality theorem;
4. a Hodge--Rosati theorem proved internally;
5. a comparison, performed last, with `B_nuc`.

This would make the four rows a genuine Weil-style chain.  Nothing in the
current A/B/C contracts supplies items 1--4.

P122.013 now supplies a local piece of item 1 at every degree-one Euler
factor: an oriented Hardy graph-determinant line whose curvature is the
positive rank-one root form.  It is not yet a mixed global intersection
product, has no Gamma/Tate determinant factor, and carries no Hodge theorem.

### D-source

Construct, before scalar augmentation, an Euler--Gamma source law whose
equality case forces one of the already faithful phase-121 conditions:

* active Euler-ideal tangency;
* vanishing of one transverse seam;
* a nonempty zero collar;
* sparse critical residues;
* an independently derived Riccati pole-order reduction.

Calling any one of these conclusions “horizontal”, “unramified” or
“conserved” without proving the source law is only a renaming of the open
arrow.

## 7. Current shortest sound chain

```text
Meyer explicit formula [IMPORTED]
  + B coefficient provenance [INTERNAL, restricted contract]
  -> nuclear Weil form [PROVED under those contracts]
  -> compact-window balanced factorization [PROVED]
  -> certified strict base T<=log 2 [COMPUTATIONAL-CERTIFICATE]
  -> first-contact attainment if global sign fails [P122.002, PROVED]
  -> local oriented Euler determinant curvature [P122.013, PROVED]
  -> global Euler--Gamma--Tate determinant line and metric flatness [OPEN]
  -> active-prime/Cartwright rigidity [PROVED conditionally]
  -> row D [OPEN]
  -> RH [classical Weil criterion].
```

The only route faithful to the intended analogy with Weil is
`D-geometry`.  `D-source` may prove the same sign analytically, but it would
not retroactively turn A/B/C into an ordinary intersection-theoretic column.
