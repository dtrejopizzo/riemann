# P123.001 — row separation and the mixed endomorphism corner

## Status

`PROVED-IN-REPOSITORY` for the algebraic/nuclear corner described below.

`OPEN` for its promotion to localized geometric kernels and for every
intersection, numerical, effectivity or mixed Riemann--Roch assertion.

## 1. Why the rows must first be separated

The current custom definition `def:strongrowa` includes an exact
correspondence module and von Mangoldt contact.  Those are useful pieces of
the existing package, but in the Weil dependency order they belong to B
and C:

```text
A constructs the general geometry and its operations;
B selects the Frobenius correspondences;
C computes their diagonal traces.
```

If `ell(delta_n)=Lambda(n)` is counted as an axiom closing A, the eventual
local part of C has already been inserted into A.  Likewise, the existing
line

```text
lambda_G := delta(lambda_int) tensor lambda_C^(-1)
```

is a coherent quotient determinant but not an independent Green object.
It therefore cannot supply the missing mixed geometry by itself.

Accordingly this phase retains all these objects but changes their logical
roles.  A is audited without the selected labels and scalar contact values;
B and C must land back in A by proved functors and comparison theorems.

## 2. Existing source object

The constructed nuclear module is

```text
N_DN = O_C e_1 direct-sum O_C e_2 direct-sum O_C e_Gamma,
```

finite locally free of rank three over the nuclear Dirichlet coefficient
algebra `O_C`.  Let `P_Gamma` be the idempotent projection onto its third
summand.  This definition uses the splitting of the already constructed
module, but does not select any integer label or contact functional.

Define the mixed endomorphism corner sheaf

```text
E_Gamma := P_Gamma End_{O_C}(N_DN) P_Gamma.
```

## 3. Corner theorem

### Theorem 3.1

There is a canonical isomorphism of unital algebra objects over the
coefficient sheaf

```text
E_Gamma ~= O_C,
```

under which composition in the endomorphism corner is multiplication in
`O_C`.  On the distinguished global nuclear Frechet sector this
multiplication is Dirichlet convolution.  The identity involution on the
real coefficient algebra (and coefficient conjugation after
complexification) supplies a continuous involution satisfying

```text
(a*b)^dagger = b^dagger*a^dagger.
```

### Proof

Because `O_C e_Gamma` is free of rank one,

```text
End_{O_C}(O_C e_Gamma) ~= O_C
```

by evaluation at `e_Gamma`.  Inserting and removing `P_Gamma` identifies
this endomorphism algebra with `E_Gamma`; the identity of the corner is
`P_Gamma`.  The composite of the maps represented by `a` and `b` sends
`e_Gamma` to `(a*b)e_Gamma`, so composition is coefficient
multiplication.  The defining seminorm estimates for `O_C` prove joint
continuity and completeness on the global rapidly decreasing sector.
The coefficient algebra is commutative; the identity is therefore an
anti-involution over the reals, and coefficient conjugation is one after
complexification.  This proves the displayed relation.  QED.

This theorem makes no claim that arbitrary completed local sections obey a
strict descent theorem in nuclear Frechet spaces.  It is a statement about
the already constructed coefficient algebra object and its distinguished
global nuclear sector.  Strict topological descent remains part of A1.

## 4. Arithmetic labels enter only in row B

After A has supplied the general corner, row B may select

```text
delta_n in Gamma(Y,E_Gamma)
```

and the associated endomorphism `rho_n`.  Then

```text
rho_m rho_n = rho_mn
```

is a consequence of composition in the already existing A-corner and the
separately proved identity `delta_m*delta_n=delta_mn`.

The continuous functional `ell(delta_n)=Lambda(n)` is deliberately absent
from Theorem 3.1.  It will qualify as diagonal intersection only after a
map from the A-trace/shadow to `ell` has been constructed and proved.

## 5. What this construction achieves

It upgrades one part of the previous bookkeeping: the mixed coefficient
direction is not merely a list of labelled maps.  Before labels are chosen,
it is an honest associative, unital, complete endomorphism corner with a
source-defined involution.  Thus it is a valid algebraic seed for A1 and
for the later B landing.

It does not yet solve the geometric problem.  In particular it supplies
none of the following:

* localization of arbitrary mixed endomorphisms as kernels on the square;
* pull--tensor--push composition on the triple product;
* diagonal pullback or categorical trace agreeing with contact;
* a numerical radical tested against all mixed objects;
* effectivity or Riemann--Roch on the completed mixed sector.

## 6. Next theorem and falsifier

The next live statement is `A1-KERNEL-LOCALIZATION`:

> Construct a full admissible subcategory of localized kernels on the
> intrinsic periodic--Deligne--nuclear square and a continuous monoidal
> realization into the endomorphism corner, with the diagonal as unit.

The finite falsifier is a two-prime block.  For distinct `p,q`, the
localized objects representing `delta_p` and `delta_q` must retain distinct
source data, compose to the object representing `delta_pq`, and possess
diagonal contacts derived by the same trace operation.  If all three
objects have only the same undecorated diagonal support and the distinction
is restored by appending their labels after localization, the candidate
has reproduced the old graph-image construction and fails A1.
