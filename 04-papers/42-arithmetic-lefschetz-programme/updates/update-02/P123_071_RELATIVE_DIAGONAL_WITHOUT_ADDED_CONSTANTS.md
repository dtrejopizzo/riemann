# P123.071 — Relative diagonal retaining the original coefficient ideal

Status: PROVED as a split continuous relative chain
construction. No nuclearity or determinant finiteness is inferred.

Use the continuous split algebra maps e:A -> D, j:D -> A from P123.070
and put I=ker e. Define

    C_rel(A,D)=ker(C_*(A,A) -> C_*(D,D)).

In degree n its continuous projection is

    P_n=1-(j e)^(tensor(n+1)).

Because e and j are algebra maps these projections commute with the
Hochschild differential. They are idempotent; their ranges are closed
and complete. Thus there is an actual direct decomposition of continuous
chain complexes

    C_*(A,A)=C_rel(A,D) direct_sum j C_*(D,D).

The relative complex is also a model for the mapping fiber of e: the
mapping fiber of the split identity on the second summand is continuously
contractible. This identifies a relative operation without using an
unproved excision theorem for the ideal I.

The continuous decomposition A=I direct_sum jD gives a more explicit
description. In degree n, C_rel is the finite direct sum of all tensor
words of length n+1 in I and jD containing at least one I factor. Tensor
products here are completed projective products. Multiplication of an
I factor with either type stays in I, so the differential stays within
these words. This description proves that the original ideal contribution
has not been removed together with the added scalar labels.

In degree zero C_rel,0=I. Its degree-one boundaries span the mixed
commutators [A,I], so its reduced H0 is

    I / closure(span[A,I]).

Every continuous functional on I annihilating mixed commutators therefore
gives a continuous chain map C_rel -> its scalar target concentrated in
degree zero. The source traces constructed earlier apply only on their
proved integrable bimodule domains; this universal statement does not
extend them to all of I without continuity and integrability estimates.

For a chart homomorphism preserving e and j, the tensorwise map preserves
the displayed projections and restricts to a continuous map of relative
complexes. Such maps compose exactly on chart triples. The original
repaired charts of P123.020 and the scalar splitting of P123.019 have
this property. No full-Hom transport for arbitrary twisted complexes is
claimed by this coefficient-level naturality.

The same algebra splitting extends to a twisted coefficient module
E_beta whenever beta fixes jD and preserves I, as the external actions
do. Applying e on its coefficient and bar factors gives a split map to
C_*(D,D), since the induced twist on D is identity. Its kernel is again
the finite sum of words with at least one ideal factor. This defines
the relative diagonal for every individual external twist and makes
its construction compatible with the external action.

The relative construction removes the precise infinite scalar retract
identified in P123.070. It does not prove that the remainder is perfect,
nuclear, or trace class. Nor is the relative complex automatically the
Hochschild complex of the nonunital ideal: that would require excision.
The trace target, its summability and the ruling/mixed determinant
comparison remain to be established for A.5–A.8. The subtraction here
is canonical for the specified split source; it is not an arbitrary
subtraction chosen from the desired Weil form.
