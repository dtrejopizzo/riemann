# Phase 125 — completion campaign for row A, then B and C

Opened 2026-09-12.  Goal: satisfy the acceptance clauses A.1–A.10 of
[P123_A_ACCEPTANCE_SPECIFICATION](../phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md)
in ONE theory on ONE carrier, then B and C.  Row D is not touched here; its
current state is phase 124.

## Entry state (audited, not re-derived)

Carried over from phase 123 as inputs, with their exact domains:

* common nuclear smooth semilocal source `A=A_sm(P)`, unitization
  `B=A_sm^u(P)=A ⊕ L` (P123.121);
* relative derived bimodule composition `M⋆N=Q(M)⊗̂_A Q(N)`, two-sided unit,
  associator/pentagon, cyclic shadow with `Tr(M⋆N)≅Tr(N⋆M)` (P123.122);
* localized twisted ideals `I_{J,β}` with `I_{J,β}⋆I_{K,η}≅I_{J∪K,βη}`,
  relatively projective on each side, stable under sums/retracts/cones
  (P123.124), and their equivariant `ρ_g` (P123.124 §6);
* derived quotients `B_O⊗^L_A B_O≅B_O`, fully faithful derived restriction
  (P123.125);
* half-density graph dagger and effective graph cone (P123.074, P123.016);
* two Tate characters with Rosati swap and the exact hyperbolic ruling plane
  `[[0,1],[1,0]]` (P123.008).

Blocking obstructions recorded in `A_DUALITY_WORK.md`, which this phase must
dissolve rather than ignore:

1. `Hom_{B-bimod}(B,A)=0` (the source has zero centre).  No degree-zero
   fully faithful involution can fix both the unit and the ideals.
2. the nonunital projective category is trivial: every idempotent in
   `M_n(A_sm(P))` is zero.
3. the bounded-convergence dual quotient `T/B` has zero separated quotient.
4. ledger rows `C1`,`C2` REFUTED: source squares are not effective graph
   cycles, and Frobenius transpose is not the integral inverse.

## Working thesis for A.4

Obstruction 1 is an obstruction to a **degree-zero, support-preserving**
duality only.  Two independent signals say the correct dagger is shifted and
support-exchanging:

* the classical model in `A_DUALITY_WORK` is `D_h(K)=σ^*(K^∨)⊗H[1]`, with an
  explicit shift and the theta twist `H=h⊠h`, `h^2=ω_C`;
* the corpus's own contact residue is proved to live in `Ext^1`, not as a
  degree-zero cyclic trace.

Accordingly the candidate is

```
D(K) = swap^*( RHom_{B^e}(K, Ω) ) [1],
```

with `Ω` a dualizing bimodule built from the half-density.  The
identification proposed here is that the arithmetic theta characteristic is
the half-density character `|·|^{1/2}` of the idele class action, whose
square is the modulus `|·|`; this is the same half-density that already
realizes the graph dagger in P123.074 and that produces the hyperbolic plane
in P123.008.  Under `D` the localized ideals are NOT self-dual: extension by
zero is exchanged with extension by multipliers/profiles, which is why
obstruction 1 does not apply to the pair `(I_{J,β}, D(I_{J,β}))`.

## Note order

| id | clause | content |
|---|---|---|
| A125.001 | A.4 | dualizing bimodule, shifted dagger, `D^2≅id`, antimultiplicativity |
| A125.002 | A.3 | two-sided excision for correspondences leaving and re-entering a removed stratum |
| A125.003 | A.5 | `Corr_A^tr` and the determinant target `T_A` |
| A125.004 | A.6 | numerical equivalence on correspondence objects; ruling plane + nonzero mixed sector |
| A125.005 | A.7 | effectivity, repairing ledger row `C1` |
| A125.006 | A.8 | mixed Riemann–Roch |
| A125.007 | A.9 | classical comparison functor, repairing `C1`,`C2` |
| A125.008 | A.1,A.2,A.10 | carrier/square, declared completion, independence audit, joint A.1–A.10 audit |

## Discipline

Status labels are mandatory and unchanged: `PROVED-IN-REPOSITORY`,
`IMPORTED` with a verified hypothesis map, `COMPUTATIONAL-CERTIFICATE`,
`CONDITIONAL`, `CANDIDATE`, `REFUTED`.  A clause is reported closed only with
every hypothesis discharged in the same theory.  Partial closure is reported
as partial.  No clause may use `Λ(n)`, a distinguished `Γ_n`, Meyer's formula,
a zero of zeta, RH, or positivity of `B_nuc` (clause A.10).
