# P123.060 — Integral normal graph contact versus ramification contact

Date: 2026-09-05. Status: PROVED for the explicit integral models below.
The calculation refutes identifying the two operations directly; it does
not refute the ramification contacts already constructed in P123.037.

## 1. An integral model of the composable normal graphs

Over R=Z or Z_p, take X=Spec R[z] and the normal dilation d_n:z -> nz,
where n>=2. These morphisms compose by d_m d_n=d_(mn). In X times_R X
the diagonal is cut out by w-z, and the graph of d_n by w-nz. Resolving
the diagonal by its one-term Koszul resolution and pulling it to the
graph gives the actual derived intersection algebra

    K_fix(n)=[R[z] --(n-1)z--> R[z]],             (1.1)

in degrees -1,0. Since R is a domain and n>=2, the differential is
injective. Hence the intersection has ordinary coordinate ring

    R[z]/((n-1)z).

Away from primes dividing n-1, this is just the zero section. Extra
vertical fixed-locus behavior is supported at primes dividing n-1,
not at primes dividing n.

## 2. The transverse cotangent factor

The relative cotangent complex of the zero-locus presentation, pulled
back to its zero section, is

    C_fix(n)=[R --(n-1)--> R].                   (2.1)

This is the conormal-to-ambient differential of the equation (n-1)z.
It is not the same as tensoring the underlying Koszul complex (1.1)
with R along z=0: that latter derived operation gives [R --0--> R]
and retains the self-intersection excess. Keeping these operations
distinct avoids replacing a cotangent determinant by excess homology.

For n=p^k over R=Z_p, n-1 is a unit. Thus (2.1) is contractible and
the graph-diagonal fixed scheme is simply Spec Z_p. There is no p-primary
torsion in this transverse fixed-contact complex.

Its analytic normal Jacobian is exactly the factor in P123.042–059:

    |n|_p^1/2 / |1-n|_p = p^-k/2.

Here the denominator comes from (2.1), while the half-density numerator
comes from the dilation action. Neither supplies a Z/p ramification
contact as the cohomology of (2.1).

## 3. The ramification operation has a different differential

For the integral power map pi_n:z -> z^n on G_m, P123.037 gives

    C_ram(n)=[Z --n--> Z]

at the identity, followed by its primitive divisor total-cofiber cube.
The full ramification differential is n, rather than n-1. Its primitive
contacts for 2,4,3,6 are Z/2,Z/2,Z/3,0 respectively.

The transverse fixed complexes (2.1) over Z instead have cokernels
Z/(n-1), namely 0,Z/3,Z/2,Z/5 for those same four labels. This is an
exact calculation of the candidate fixed-contact operation, not an
alternative definition of the required B contacts. In particular even
before comparing primitive constructions, localization at p for n=p^k
shows a decisive mismatch: C_fix is contractible, whereas the primitive
ramification contact has nonzero Z/p cohomology.

The linear dilation d_n also has its own relative cotangent differential
n. Thus the two differentials can coexist on the same linear model:
ramification concerns the derivative of d_n; fixed intersection concerns
the derivative of d_n-id. Having the same underlying morphism does not
identify these two derived operations.

## 4. Consequence for the B/C bridge

The actual normal graph calculation now identifies exactly what the
local Fourier trace sees transversely: the fixed differential 1-n,
together with the dilation half-density. The known primitive B contact
comes from ramification differential n and its divisor operation.
Therefore a direct quasi-isomorphism between these two contact complexes
cannot be the missing comparison, already at a prime-power local label.

A successful common-source comparison must specify how ramification,
primitive extraction and the global diagonal shadow are related, with
any excess or relative determinant operation explicitly included. It
cannot obtain that relation by renaming the transverse normal fixed
complex as the primitive ramification complex. The finite-orbit
determinant bridge of P123.039 remains a possible additional ingredient;
it is not proved equivalent to (1.1) here.

This calculation keeps both established constructions intact and rules
out one specific direct identification. It leaves the full mixed RR and
integral-contact transport open, as required by the A/B/C plan.
