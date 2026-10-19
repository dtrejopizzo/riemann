# P123.070 — The diagonal target has an infinite nuclear scalar retract

Status: PROVED for the repaired coefficient-unitized
algebras with a nonempty finite prime set. This determines a constraint
on the target realization of A.5, not a proof of its existence.

Let A be the repaired unital algebra and D the scalar rapid Gamma algebra.
P123.019 and P123.053 give continuous algebra maps e:A -> D and j:D -> A
with e j=id. Applying them to every tensor factor gives split chain maps

    C_*(D,D) -> C_*(A,A) -> C_*(D,D)

for the completed diagonal complexes of P123.066. They commute with the
Hochschild differential because e and j are multiplicative. Since Gamma
is abelian, D is commutative, and the degree-one boundary into C_0(D,D)
is zero. Hence both ordinary and reduced HH_0(D,D) equal D. Therefore
D is a continuous split retract of reduced HH_0(A,A), and an algebraic
split retract of ordinary HH_0(A,A).

For nonempty S_f, D contains the linearly independent labels U_(p^n),
n in Z. Thus HH_0(A,A) is infinite-dimensional. The entire diagonal
complex of the tensor unit cannot be quasi-isomorphic over C to a
bounded complex of finite-dimensional vector spaces. In particular a
finite-dimensional determinant construction on every object of the
current category cannot be obtained by merely relabelling this diagonal
complex as perfect. This does not prevent a smaller perfect trace domain
or a different nuclear realization with its own proved comparison.

The scalar retract itself has explicit nuclear transition maps. Put

    D_k=l¹(Gamma,H^k).

In the normalized coordinate basis, the inclusion D_(k+1) -> D_k has
rank-one expansion with coefficients H(gamma)^-1. To check summability,
write gamma=product_p p^e_p. If P and Q are the logarithms of numerator
and denominator, then

    log H(gamma)=max(P,Q)
        >=(P+Q)/2=(1/2)sum_p |e_p|log p.

Consequently

    sum_gamma H(gamma)^-1
      <=product_p sum_(e in Z) p^(-|e|/2)<infinity.

The coordinate functionals and normalized target vectors have norm one,
so this is a nuclear Banach-space map by its defining summable rank-one
representation. The countable projective limit D is therefore nuclear
in the seminorm criterion: every defining seminorm has a stronger one
whose map of Banach completions is nuclear.

This also displays a limit of that information. The identity on D is
not thereby a summable operator trace. Projection onto any N distinct
label coordinates has trace N; the identity on a fixed Banach level is
not nuclear. Nuclearity of the Fréchet space and a finite scalar trace
for a given operator are different requirements. A regularization or
declared trace-class domain must still be constructed and compared.

Thus the next target construction must either specify a proper perfect
trace domain or supply the nuclear realization and summability required
by A.5. The scalar retract gives an explicit nuclear component but does
not prove that the whole completed diagonal complex is nuclear, that
its remaining homology is controlled, or that a ruling/mixed determinant
extends over it. These remain the substantive tasks; finite-dimensional
perfection of the whole current unit diagonal is now excluded.
