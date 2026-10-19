# P123.038 — realize the cotangent cube on the external arithmetic carrier

Status: CONSTRUCTED for the arithmetic external family,
its gauge-independent lattice index and the natural derived comparison
below. A cyclic diagonal shadow on all admissible mixed kernels remains
OPEN. No full row is declared closed.

## 1. The arithmetic maps are external, not diagonal rational gauge

Fix n>=1 and a finite chart S containing infinity and every prime
factor of n. In the semilocal idele group choose

    a_S(n)=(1 at infinity, n at each finite place of S).

Then a_S(m)a_S(n)=a_S(mn). Its valuation normalizer from P123.020 is n,
so its normalized class is

    h_S(n)=(1/n at infinity, 1 at every finite unit coordinate).

The class has Tate modulus 1/n and is not the identity for n>1.
The arithmetic correspondence is the repaired twisted bimodule
E_(beta_(a_S(n))). Its completed tensor composition is E_m tensor E_n
isomorphic to E_(mn), by P123.019. This uses the arithmetic family
inside the proved gauge-generated category, not an assertion about all
bimodule morphisms or faithful distinction of every external class.

For S contained in T, P123.020's actual lift transition adds the
coordinate r_S(a_S(n))=n. Hence

    L_ST(a_S(n))=a_T(n)

literally, and the existing tensor/gauge chart coherence applies.
The action on X_S is identity on the real coordinate and multiplication
by n on every finite additive coordinate.

## 2. Make the lattice construction independent of gauge

The distinguished integral finite lattice is

    L_S=product_(p in S_f) Z_p.

Its inclusion in the finite coordinates of X_S is part of the existing
coefficient geometry: the transition functions already use 1_Zp.
For the representative a_S(n), the finite action sends L_S to n L_S.

Using a_f L_S for an arbitrary representative would be wrong: the
normalized representative h_S(n) has finite coordinates 1 and would
give zero index. To correct this, on classes admitting a positive
rational real coordinate define the finite arithmetic anchor

    b_S(a)=a_f/a_infinity.

The real entry here is a rational number and is embedded diagonally in
the finite local fields. Under a -> gamma a for positive rational
S-unit gamma, both numerator and denominator acquire gamma, so b_S is
unchanged. It is multiplicative. For both a_S(n) and h_S(n), its value
is the finite scalar n.

Equivalently the arithmetic class has its unique representative with
real coordinate 1 when such a representative exists; the ratio above
also makes sense on the broader rational-real locus. No embedding of
arbitrary real scalars into Q_p is asserted. We do not claim a continuous
extension of this anchor to all external classes. The construction is
on the arithmetic family and its gauge presentations.

Thus n L_S is an invariant lattice of the arithmetic class, not data
chosen differently after each change of lift. Gauge arrows act as the
identity on its anchored lattice complex.

## 3. An actual derived comparison, natural on the divisor diagram

Use complexes of abelian groups and define

    Q_(S,n)=[L_S --n--> L_S], in degrees -1,0.

Multiplication by n is injective. Its cokernel is canonically Z/n:

    Z/n -> product_(p in S_f) Z_p/n Z_p

is an isomorphism by primary decomposition, since S contains all prime
factors of n. For n=1 both sides are zero. Therefore diagonal embedding
Z -> L_S gives a natural quasi-isomorphism

    C_n=[Z --n--> Z] -> Q_(S,n).                   (3.1)

The terms L_S are not claimed to be finitely generated projective
Z-modules. Rather (3.1) proves that their complex represents a perfect
object of D(Z), with C_n as its explicit finite free model.

For d dividing n, use (id,n/d) between Q_(S,d) and Q_(S,n).
The diagonal maps (3.1) commute strictly with these maps. Thus (3.1)
is a natural quasi-isomorphism of the entire divisor cube, not only
an equality of four group orders. It transports cotangent transitivity
to the exact lattice sequence

    0 -> L_S/n L_S --m--> L_S/(mn)L_S -> L_S/m L_S -> 0.

For S contained in T, coordinate projection L_T -> L_S is a chain map
Q_(T,n) -> Q_(S,n), commuting with (3.1). The kernel complex is
multiplication by n on the added Z_p factors, hence contractible
because the new primes do not divide n. These transition maps are
quasi-isomorphisms, compose exactly on chart triples and commute with
all divisor maps. This is the inverse direction for lattice complexes;
it is not being identified with a forward coefficient-algebra embedding.

## 4. Primitive contact on the same arithmetic action

Apply the total-cofiber construction of P123.037 to Q_(S,d) over the
divisor cube of n. Naturality of (3.1) produces

    Prim_n ~= total_cofiber(Q_(S,divisors of n)).    (4.1)

It follows that this arithmetic lattice construction yields Z/p for
n=p^k and an acyclic complex for mixed n. The comparison is compatible
with the chart projections just proved. It preserves the derived
attaching maps inherited from the cotangent cube.

In particular the contacts for 2,4,3,6 are now realized by the actual
finite-lattice movement of their composable external actions on X_S.
The lattice is a subspace of the analytic carrier; the finite quotient
and its exact sequence are not a scalar label attached afterwards.
Taking the index gives [L_S:nL_S]=n, matching the inverse Tate modulus.
Primitive extraction gives the logarithmic torsion degree log p for
prime powers, with the degree coming from the finite perfect complex.

## 5. Remaining shadow construction

The same finite quotient also realizes the earlier cyclotomic model.
Let M_(S,n)=Z[L_S/nL_S], the free integral module on that finite group.
Translation by the class of the diagonal integer 1 gives an operator T.
The isomorphism Z/n -> L_S/nL_S identifies this canonically with

    Z[T,T^-1]/(T^n-1).

Hence the primitive submodule obtained by multiplication by
(T^n-1)/Phi_n(T) is exactly the integral V_n of P123.025. Its derived
T=1 coinvariants are the existing cyclotomic contact K_n^W. Thus both
the cotangent cube and the primitive orbit-lattice construction have
concrete realizations on this finite quotient of the additive carrier.

For n dividing mn the quotient injection multiplies by m; on group
algebras it sends T_n to T_(mn)^m. This retains the actual power/subdivision
map and does not falsely identify it with a rooted-label inclusion.
No ordinary tensor multiplication law for the primitive lattices is
asserted. The translation operator T is an operator on this finite
quotient; it is not identified with the external dilation E_n itself.

This links three previously separate pieces by specified maps:

    power-map cotangent divisor diagram
       -> finite lattice-index diagram inside X_S
       -> primitive perfect contact of the external arithmetic family.

The final arrow needed for A/B/C is not supplied yet: the lattice-index
operation must be realized as the admissible diagonal shadow, extended
cyclically to mixed correspondences and compared with the analytic
nuclear trace. An invariant of the arithmetic family does not itself
provide that trace functor. The rational-real anchor has also not been
extended to arbitrary external classes or continuous test sections.
These are now precise extension requirements on this concrete
construction, rather than the absence of an integral realization for
the arithmetic lattice diagram. Effectivity, mixed RR and D remain open.
