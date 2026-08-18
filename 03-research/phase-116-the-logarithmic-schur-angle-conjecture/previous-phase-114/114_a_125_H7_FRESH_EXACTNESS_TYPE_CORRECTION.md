# 114.a.125 — H7: fresh-target exactness must be sourcewise, not a target sheaf

```
+------------------------------------------------------------------------+
| NO MAP      F_p^k -> F_q^l has no unital map when p!=q.                |
| NO AB       Haran's completed section sheaves are right acts/sets, not  |
|             the abelian modules of Section 6.                           |
| RETRACT     Target transitions and a long exact cohomology sequence are |
|             not a typed requirement for the fresh invariant.            |
| REPLACE     Reevaluate one source restriction diagram in the single     |
|             fresh target attached to its output degree.                  |
| OPEN        Prove the required fiber/cardinality identity sourcewise.    |
+------------------------------------------------------------------------+
```

## 1. Different fresh characteristics cannot form a target sheaf

### Lemma 1.1

For distinct primes `p!=q` and positive integers `k,l`, there is no unital
ring homomorphism

\[
 \mathbb F_p^k\longrightarrow\mathbb F_q^l.                           \tag{1.1}
\]

### Proof

In the source, `p*1=0`.  A unital map would give `p*1=0` in every target
coordinate, so `q` divides `p`, impossible for distinct primes.  QED.

The canonical fresh rule of `a118`--`a120` deliberately changes the residue
prime when a later denominator requires it.  Therefore the targets `T_D`
cannot be transition objects of a unital graded sheaf or directed ring
system.  This is the same obstruction as `a57`--`a58`, now applied to the
post-`a120` calibrated targets.

## 2. The source does not supply abelian long exact cohomology

The type audit `a66` proves that Haran's completed section sheaf (11.7) is a
sheaf of operation sets stable under a right action.  It is not identified
with an abelian `O`-module of Section 6.  Consequently expressions such as

\[
 0\to H^0(D-Z)\to H^0(D)\to H^0(D|_Z)\to H^1(D-Z)\to\cdots             \tag{2.1}
\]

are not supplied by the source for these completed right acts.  Kernels,
cokernels and derived functors in the abelian sense cannot be imposed without
first constructing and comparing a new linearization.

Thus the former phrase **H7-FRESH-EXACT**, when interpreted as target
transition maps plus (2.1), is retracted as ill-typed.  This does not retract
the degreewise section sets or their calibrated image cardinalities.

## 3. Correct replacement gate

Let `r:H^0_bd(D)->H^0_bd(D|_Z)` be a restriction map that exists at the level
of Haran's source right acts.  Attach one fresh target to the **output
diagram**, chosen to avoid every denominator occurring in `D`, `Z` and the
restriction charts.  Reevaluate all source elements directly in that same
target, exactly as products are reevaluated in `a118`.

The typed replacement is:

> **H7-FRESH-RESTR.** Construct the source restriction diagrams for the
> repaired Cartier data; prove that common fresh evaluation commutes with
> them; and establish directly the fiber/cardinality identity or inequality
> required by the RR argument.  No maps `T_D->T_E` and no abelian long exact
> sequence are requested.

Because the target is fixed within one diagram, ordinary fibers of maps of
finite sets and their cardinalities are well-defined.  Different diagrams
may use different characteristics without conflict.

## 4. Consequence for row A

`a120` already proves the all-ray leading coefficient directly, so no long
exact sequence is needed for that numerical theorem.  H7-FRESH-RESTR is
needed only if the final geometric RR proof uses restriction/moving
arguments or compares the calibrated invariant with a Cartier determinant.
It is strictly narrower and correctly typed.

This closes the old target-transition/abelian-exactness formulation
negatively.  It does not prove H7-FRESH-RESTR, H7-RULING-PF, the sheaf-level
Green comparison, row A or RH.

## 5. Verification scope

`114_a_125_h7_fresh_exactness_type_verify.py` exhausts finite prime/product
characteristic tests, checks the Section-11/Section-6 source markers and
guards the replacement scope.  The categorical type distinction is the
source theorem audited in `a66`.
