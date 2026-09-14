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
quotient `N_A` carries a canonical exact sequence
`0 -> N_A^prim -> N_A -> B_T -> 0` of topological modules, in which `B_T`
is the two-dimensional Tate boundary with the hyperbolic form `[[0,1],[1,0]]`
and with dagger exchanging its two directions, and in which `N_A^prim` is
nonzero and carries a nondegenerate induced pairing.  No splitting of this
sequence is required.  The topology and continuity of all operations are
explicit.

> **Amendment record (2026-09-12).**  The previous wording "contains the
> ruling plane and a nonzero completed mixed sector" was replaced by the
> exact-sequence formulation above.  Reason: Paper 43, Theorem 9.13(a),
> proves that on the row-A carrier no `D_A`-module subobject isomorphic to
> the Tate boundary exists (a `D_A`-eigenvector with eigenvalue
> `a-hat(-/+ i/2)` off the unitary axis cannot exist), while Theorem 9.12
> proves that `B_T` is canonically the quotient by the primitive sector.
> The new text is P123.017 section 4's own formulation.  Decision by the
> repository owner (D. Trejo Pizzo), recorded in
> `03-research/phase-129-row-a-rebuild/README.md`.

### A.7 Effectivity

`Eff_A` is a functorial cone or exact positive class constructed from the
source geometry.  It descends to the numerical theory to the extent needed
by Riemann--Roch.  Positivity of the Weil form is not used to define it.

### A.8 Mixed Riemann--Roch

`lambda_RR` extends the intrinsic periodic ruling determinant to the
admissible mixed sector.  Principal invariance, additivity/biextension,
restriction, convergence and an equality formula in `T_A` are proved.
This clause supplies no Hodge-index sign.

> **Amendment record (2026-09-12).  [phase 133, amendment accepted
> 2026-09-12]**  The clause text above is kept unchanged.  The amended
> wording, proposed by the phase-133 review panel and adopted by the lead in
> `03-research/phase-133-abc-review-panel/PANEL_SYNTHESIS.md` section 4.2, is:
> "`lambda_RR` is a based Hermitian biextension into `Pic_b(B_T)` whose Tate
> component is the ruling determinant (Def 10.6c), consistent with the test
> sector by Thms 9.14a, 9.14c'; the scalar determinant `L_S` is trivial on the
> rulings (Thm 10.8), so the extension of the *scalar* determinant demanded by
> the original clause does not exist."  Reason: Paper 43 Theorem 10.8 proves
> that no scalar determinant extends to the rulings, while Theorem 10.7 proves
> the vector-valued biextension with target `Pic_b(B_T)`; the round-1 hostile
> audit `R130.002` dissented from the lead's ruling and the review panel
> (PANEL_3 section 3) sides with the dissent.  **Decision by the repository
> owner (D. Trejo Pizzo), 2026-09-12: the amendment is ACCEPTED.**  Grading:
> `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED`.

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
| A.6 | Paper 43 (phase 129): Theorem 9.8 `N = 0` (import-free), Theorems 9.11-9.14: exact sequence `0 -> N_A^prim -> N_A -> B_T -> 0`, hyperbolic `B_T`, dagger exchange, nondegenerate primitive pairing, separated completion | PROVED under the amended wording (amendment of 2026-09-12, above) |
| A.7 | P123.021: source squares and effective graph cycles differ already on two points | OPEN: construct geometric effectivity and prove the required descent/RR compatibility |
| A.8 | Paper 43 (phase 130): Theorem 10.7 (vector-valued Riemann-Roch biextension with target `Pic_b(B_T)`), Theorem 10.8 (the scalar determinant is trivial on the rulings), Theorems 9.14a, 9.14c' (consistency with the test sector) | `REFUTED AS STATED (scalar extension) + PROVED AS AMENDED` (amendment of 2026-09-12, above; accepted by the owner D. Trejo Pizzo) **[phase 133, amendment accepted 2026-09-12]** |
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

## 5. Phase-125 campaign (2026-09-12)

See [A125.015](../phase-125-row-a-completion/A125_015_WEIL_STRENGTH_LABEL.md).
On the graph sector `G` with its Fell completion, the full cyclic shadow and
the torsion invariant of A125.014, clauses A.1–A.10 are proved and the
adversarial audit passes; the label `WEIL-STRENGTH-COMPLETE` is granted on
that declared category, with four `IMPORTED` statements listed in A125.015 §2
as its only inputs beyond the repository.  The audit of section 3 above is
superseded on that category.  Clause texts of section 2 and the closure rule
of section 4 are unchanged.

## 6. Phase-130 campaign (2026-09-12)

The phase-125 grant of section 5 was withdrawn by the phase-128 audit.  After
the phase-129 rebuild and the phase-130 closure of
[Paper 43](../../04-papers/43-row-a-torsion-theory/main.md) (builder/auditor
loop, `R130.000`–`R130.005`), the adversarial audit of record
([R130.005](../phase-130-row-a-closure/R130_005_LEAD_FINAL_AUDIT_AND_LABEL.md))
finds A.1–A.10 proved on the declared carrier — a fixed finite chart `S`
with the chart system and its colimit as additional structure, invertible
sector — with A.6 under the amendment of section 2 and A.8 with the
determinant target `Pic_b(B_T)` (forced by Paper 43 Theorem 10.8), and finds
none of A.2–A.8 a renaming of the scalar explicit formula.  Label granted:

```text
ROW A: WEIL-STRENGTH-COMPLETE (declared carrier; A.6 amended; A.8 with
       target Pic_b(B_T)).  Dissent of the round-1 hostile audit on A.8
       recorded in Paper 43 section 10.3.3.
```

Not claimed and not required by any clause: `N_infty^W = 0` on the colimit,
the imported cutoff constant `c_cut`, non-invertible correspondences as
objects, a continuous extension of `I_A` to the completion squared,
effective descent along a stack covering.  Theorem 10.8b of Paper 43
(Mertens) is `CLASSICAL` and counts toward no clause.  The table of section 3
is superseded by Paper 43 section 14.

## 7. Phase-133 amendment (2026-09-12)

**[phase 133, amendment accepted 2026-09-12]**  The phase-133 review panel
(`03-research/phase-133-abc-review-panel/`, PANEL_3 section 3 and
PANEL_SYNTHESIS section 4.2) found that the A.8 dissent of the round-1 hostile
audit `R130.002` had been resolved by a lead ruling where A.6 had gone to the
owner as an amendment, and that the two are the same logical situation.  The
lead therefore referred A.8 to the repository owner with the amended wording
reproduced in the amendment record of section 2 above.

**The repository owner (D. Trejo Pizzo) accepted the amendment on
2026-09-12.**  Consequently:

* clause A.8 is graded `REFUTED AS STATED (scalar extension) + PROVED AS
  AMENDED`; the original clause text is kept in section 2 as the text that was
  amended;
* the lead's ruling of `R130.005` (A.8 `PROVED WITH TARGET Pic_b(B_T)`, with
  the dissent recorded) is superseded by the owner's decision, and an addendum
  to that effect is appended to `R130.005`;
* the row-A label stands **unconditionally**:

```text
ROW A: WEIL-STRENGTH-COMPLETE (declared carrier; A.6 amended; A.8 amended
       (owner, 2026-09-12)).
```

No theorem, no proof and no other clause grading is changed by this record.
