# P123.037 — primitive cotangent cubes from composable power maps

Status: CONSTRUCTED, with the calculations below proved
on the integral multiplicative group. This is a source-defined perfect
ramification complex and a coherent primitive extraction. Its comparison
with the graph-diagonal shadow required by A/B is still OPEN.

## 1. Begin with morphisms that actually compose

Let X=G_m over Spec Z and let pi_n:X -> X be z -> z^n for n>=1.
These maps are finite locally free of rank n and pi_m pi_n=pi_(mn).
Relative to Z, both copies of X are smooth with differential basis dlog z.
The differential of pi_n is multiplication by n, so the relative
cotangent complex is

    L_(pi_n)=[O_X --n--> O_X] in degrees -1,0.

At the identity section e:Spec Z -> X, derived pullback gives the
perfect integral complex

    C_n=e^* L_(pi_n)=[Z --n--> Z],
    H^0(C_n)=Z/n,   H^(-1)(C_n)=0.                 (1.1)

For n=1 the complex is contractible. This torsion comes from the
actual derivative of a morphism, before any prime-contact value is
specified.

The [cotangent transitivity triangle](https://stacks.math.columbia.edu/tag/08QR)
for the factorization pi_(mn)=pi_n circ pi_m induces

    C_n -> C_(mn) -> C_m -> C_n[1].                (1.2)

In the displayed free models, the first map is identity in degree -1
and multiplication by m in degree 0; the second is multiplication by n
in degree -1 and identity in degree 0. Thus its cohomology is the exact
sequence 0 -> Z/n --m--> Z/(mn) -> Z/m -> 0.
The hypotheses are explicit: the two absolute cotangent complexes are
free in degree zero, and pulling the transitivity triangle to e is derived.
The displayed chain maps also verify (1.2) directly.

For every d dividing n, write i_(d,n):C_d -> C_n for the chain map
(id,n/d). These satisfy i_(b,n)i_(d,b)=i_(d,n) literally. Hence this
is a strict divisor diagram of complexes, not merely an identity of
logarithmic degrees.

## 2. Its relation to a genuine relative diagonal

The fibre product X times_(pi_n,X,pi_n) X has coordinates z,r with
r^n=1, where r is the ratio of the two X coordinates. Its diagonal
is r=1. If J is that diagonal ideal, expansion of r^n-1 modulo J^2
shows

    J/J^2 ~= O_X/n.

Pulling this conormal module to z=1 gives Z/n. More precisely C_n is
the cotangent complex of the root fibre mu_n pulled to its unit, by
base change from pi_n. Thus the construction has a concrete relative
diagonal/ramification interpretation.

It is NOT the ordinary derived intersection of the graph of pi_n with
the absolute diagonal of X times_Z X. Nor is J/J^2 a substitute for
that entire derived intersection. This distinction is required when
comparing to the stronger A.5/B contract.

## 3. Primitive extraction as a total cofiber

Let P(n) be the finite set of distinct prime divisors of n>1. Form the
cube indexed by subsets J of P(n), with vertex

    C_(n/product_(p in J) p).

An edge deleting p from J uses i_(d,pd). All faces commute by section 1.
Define Prim_n to be its total cofiber, oriented so that for one prime it
is Cone(C_(n/p) -> C_n). Use the increasing prime order for the usual
alternating signs; this specifies an actual finite free complex. Cube
permutations give the standard signed identifications, rather than a
choice of a scalar degree.

The natural maps C_d -> (Z/d)[0] commute with the divisor maps and are
quasi-isomorphisms. Therefore the same total cofiber can be calculated
using the finite cyclic modules with their injective maps x -> (n/d)x.

### Theorem

    Prim_n ~= Z/p in degree 0,   if n=p^k;
    Prim_n ~= 0,                if n has at least two prime divisors.

For n=p^k the cube is the injective map Z/p^(k-1) --p--> Z/p^k.
Its cokernel is canonically Z/p, by reduction modulo p; there is no
negative-degree cohomology.

For mixed n, decompose the finite cyclic-module cube into its primary
parts. For each primary prime ell choose a different prime p in P(n).
Every edge in direction p is an isomorphism on the ell-primary part:
the source and target have the same ell-power order, and multiplication
by p is invertible there. Taking the cofiber in that direction is
acyclic, so the total cofiber of that primary cube is acyclic. This
holds for every primary part and proves the theorem. The argument
keeps the full complexes and maps; it is not tensoring reduced H^0
contacts and discarding Tor.

## 4. The four required labels, and the integral comparison

| n | primitive module cube | total cofiber |
|---|---|---|
| 2 | 0 -> Z/2 | Z/2 |
| 4 | Z/2 --2--> Z/4 | Z/2 |
| 3 | 0 -> Z/3 | Z/3 |
| 6 | Z/2 direct-sum Z/3 -> Z/6, (a,b) -> 3a+2b | 0 |

For n=6 the omitted intersection vertex is Z/1=0; the displayed map
is an isomorphism by the coprime decomposition. In the free model that
vertex is the contractible C_1, retained until passage to cohomology.

The theorem gives the same perfect Z-complex as the unit cyclotomic
contact K_n^W in P123.022–025: both have sole cohomology Z/p for n=p^k
and are acyclic for mixed n. In the prime-power case the generators
from reduction modulo p specify the identification on H^0; canonical
truncation identifies the complexes in D(Z). This is an object-level
integral comparison, not a proof of functoriality for every proposed
correspondence operation.

The torsion degree is log p in the prime-power case and zero otherwise.
It also equals the alternating sum

    sum_(J subset P(n)) (-1)^|J| log(n/product_(p in J) p).

For one prime this is log p; for at least two primes every logarithmic
coefficient cancels. Unlike that numerical identity alone, the cube
constructs the perfect object producing the cancellation.

## 5. What has been added to the common-source problem

There is now a composable integral morphism family, its cotangent
transitivity maps, and a coherent divisor cube whose primitive object
recovers the required four contacts and all prime-power/mixed cases.
This supplies an actual source for a derived primitive operation. The
reduced contact system of phase 114.a.45 did not by itself provide
these cotangent maps and total cofibers.

The missing comparison is narrower but still substantial: realize this
relative-diagonal cotangent operation as the admissible diagonal shadow
on the same correspondence carrier as the analytic action, with the
required determinant and composition comparisons. Primitive extraction
has not been shown to commute monoidally with multiplication of labels;
transitivity (1.2) is an exact triangle, not such an isomorphism.
Complexification still kills the finite torsion. A valid analytic
realization must retain the integral comparison/determinant data rather
than claim that an acyclic complex remembers its arithmetic degree alone.
No row closure or global sign theorem is asserted.
