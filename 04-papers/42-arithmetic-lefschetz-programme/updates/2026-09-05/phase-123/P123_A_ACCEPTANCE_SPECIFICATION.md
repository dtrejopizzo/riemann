# P123 — acceptance specification for a Weil-strength row A

## 1. Meaning of “Weil-strength”

For this phase, “Weil-strength” means equality of structural burden:
correspondences, their composition, transpose, diagonal contact,
intersection/trace, numerical equivalence, effectivity and Riemann--Roch
must belong to one theory on one carrier.  It does not mean that the carrier
over `Spec Z` must be an ordinary finite-type algebraic surface or that its
numerical group must have finite rank.

Finite rank is in fact inadmissible for the exact full contact kernel.  The
proved matrix

```text
(Lambda(p_i p_j))_ij = diag(log p_1,...,log p_r)
```

has arbitrary finite rank.  Thus the coherent target is a separated
infinite-rank nuclear/topological numerical theory.

## 2. The object to be constructed

A completed row A is a tuple

```text
A_W = (X, Y, C_X, C_Y, Corr_A, star, Delta, dagger,
       Tr_A, N_A, Eff_A, H, lambda_RR).
```

It must satisfy the following clauses without reference to a selected
arithmetic family.

### A.1 Carrier and coefficients

`X` is the arithmetic curve, `Y` its noncollapsed square, and `C_X,C_Y`
are explicitly defined coefficient categories on them.  Restriction,
descent and the coefficient comparison maps must be constructed.  The
present spherical carrier and intrinsic periodic--Deligne--nuclear
categories are admissible inputs, not automatic proofs of the later
clauses.

### A.2 Correspondences

`Corr_A` is an additive/stable topological category of admissible mixed
correspondences.  Its objects have geometric localization on `Y` or a
proved Morita-equivalent localization.  It contains more than the two
rulings and is closed under its declared completion.

### A.3 Composition and unit

There is a continuous associative composition `star`, and `Delta` is a
two-sided unit.  If composition is written by pull--tensor--push on `X^3`,
all functors, domains and base-change identities required by that formula
must be proved or imported with hypotheses checked.

### A.4 Transpose/Rosati operation

There is a continuous contravariant involution `dagger` satisfying

```text
(K star L)^dagger ~= L^dagger star K^dagger,
Delta^dagger ~= Delta.
```

It is source-defined and cannot be selected from the desired sign of a
later scalar form.

### A.5 Diagonal trace/intersection

There is a trace/shadow on a declared trace-class domain,

```text
Tr_A : Corr_A^tr -> T_A,
```

where `T_A` is a determinant, perfect-complex or nuclear trace target.  It
is additive, cyclic, compatible with restriction and determinant, and has
a finite scalar degree whenever such a degree is asserted.  Its value on a
future `Gamma_n` is a theorem of B/C, not part of this clause.

### A.6 Numerical equivalence and completion

Numerical equivalence is the radical against all trace-class tests.  It is
proved closed, stable under composition and dagger, and its Hausdorff
quotient `N_A` contains the ruling plane and a nonzero completed mixed
sector.  The topology and continuity of all operations are explicit.

### A.7 Effectivity

`Eff_A` is a functorial cone or exact positive class constructed from the
source geometry.  It descends to the numerical theory to the extent needed
by Riemann--Roch.  Positivity of the Weil form is not used to define it.

### A.8 Mixed Riemann--Roch

`lambda_RR` extends the intrinsic periodic ruling determinant to the
admissible mixed sector.  Principal invariance, additivity/biextension,
restriction, convergence and an equality formula in `T_A` are proved.
This clause supplies no Hodge-index sign.

### A.9 Classical control

On a smooth projective curve over a finite field, the formalism admits a
comparison with ordinary perfect kernels/cycles sufficient to recover
composition, transpose and diagonal intersection.  This is an acceptance
test for structural correctness, not a definition by analogy.

### A.10 Independence

No clause uses `Lambda(n)`, a distinguished `Gamma_n`, Meyer's explicit
formula, a zeta zero, RH, or positivity of `B_nuc`.  General coefficient
algebras may be part of A; the arithmetic selection and its trace values
belong to B and C.

## 3. Audited comparison with the present constructions

Updated 2026-09-05 against P123.018–027. The former table reporting
A.1–A.6 as PROVED and A.9 as PASS is superseded. Clauses above are the
unchanged acceptance requirements; local repairs do not satisfy their
full scope automatically.

| clause | current authoritative evidence | remaining requirement / status |
|---|---|---|
| A.1 | P123.019–020: enlarged rapid algebra and normalized chart embeddings | OPEN: common integral/analytic coefficients and full geometric descent |
| A.2 | P123.019–020: gauge-generated, non-full bimodule category | OPEN: stable localized mixed category and declared completion; P123.027 module realization does not land in bimodule complexes |
| A.3 | P123.019: continuous local balanced tensor with unit; P123.020: gauge coherence | PARTIAL: extend composition to the common mixed carrier with the required base change |
| A.4 | P123.019: local dagger and inverse twisted bimodules | PARTIAL: extend to the same mixed category and completion |
| A.5 | P123.023: compatible integrated coefficient actions; P123.025–026: integral unit-contact and gluing triangles | OPEN: one cyclic diagonal shadow and its analytic/determinant comparison; these are currently different targets |
| A.6 | Earlier numerical quotient constructions depend on operations questioned in P123.018 | OPEN: verify radical ideal, continuity and separating completion on the repaired common domain |
| A.7 | P123.021: source squares and effective graph cycles differ already on two points | OPEN: construct geometric effectivity and prove the required descent/RR compatibility |
| A.8 | Earlier local determinant formulas remain inputs, not a repaired common RR theorem | OPEN: mixed equality, integral gluing, completion and periodic determinant comparison |
| A.9 | P123.021: literal cone comparison and integral Frobenius-inverse analogy fail | NOT PASSED: supply a correctly typed classical comparison; the counterexamples do not rule out every comparison |
| A.10 | The repaired local algebra and normalization are independent of RH/sign data | PARTIAL: audit independence for the eventual full A.1–A.9 construction |

The [execution ledger](P123_024_FIRST_CAMPAIGN_LEDGER.md) records exact
local proof domains. No full row is closed by the finite regressions.

## 4. Closure rule

Row A may be labelled `WEIL-STRENGTH-COMPLETE` only when A.1--A.10 are
proved and an adversarial audit confirms that none of A.2--A.8 is merely a
renaming of the scalar explicit formula.  Until then the current label is

```text
ROW A: CONSTRUCTED UNDER def:strongrowa;
       WEIL-STRENGTH EXTENSION OPEN.
```
