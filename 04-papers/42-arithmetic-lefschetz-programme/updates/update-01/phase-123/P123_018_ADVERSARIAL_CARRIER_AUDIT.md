# P123.018 — adversarial audit of P123.014–P123.017

## Status

`REFUTED-AS-WRITTEN` for the unitized lift-change map and extension-by-one
map on semilocal idele classes. `OPEN` for their replacements and for the
completed geometric carrier asserted using them. This audit supersedes the
unqualified completion verdicts in P123.014–017; it does not refute the
programme or assert any result about RH.

## 1. A multiplier is not an element of the chosen unitization

P123.006 defines K as rapid families with every coefficient in C_0(A_S).
P123.014 instead takes Acal = K + C1 and uses

    Phi_gamma: Acal -> Acal, x -> x U_gamma.

For gamma != 1, U_gamma is not in Acal. Indeed every element of Acal has a
C_0 coefficient at each nonidentity group label. U_gamma has coefficient
1 at label gamma, and A_S is noncompact. Adding a scalar identity changes
only the identity-label coefficient. Thus Phi_gamma(1)=U_gamma is outside
its asserted codomain. This disproves the displayed map, regardless of
its formally correct right-action identity.

Conjugation by U_gamma does preserve Acal, but this does not make U_gamma
an invertible element of Acal. P123.014's finite matrix verifier assumes
precisely the membership that fails here.

The general distinction between canonical group unitaries in a multiplier
algebra and elements of a nonunital crossed product is also explicit in
[Phillips, Crossed Product C*-Algebras 101](https://pages.uoregon.edu/ncp/Courses/CRMCrPrdMinDyn/Notes_20170205.pdf).
The counterexample above uses the repository's coefficient definition.

Possible repairs: work with essential nonunital K-bimodules and multiplier
intertwiners, or specify a larger algebra containing all U_gamma. Neither
repair is completed here. In the first option the tensor inverse
z -> z tensor 1 is unavailable and must be replaced by a proved balanced
tensor theorem. In the second option topology, coefficients and trace
comparison must be checked again. Algebraic twisted tensor identities for
actual unital algebras remain valid.

## 2. Extension by one does not descend to idele classes

Take S={infinity,2}, S'={infinity,2,3}, with positive S-units as in P123.006.
In A_S^times the lifts a=(1,1) and a'=(2,2) represent the same class,
because a'=2a. Extension by one gives

    i(a)=(1,1,1),  i(a')=(2,2,1).

If they represented the same class modulo Gamma_S', a diagonal positive
rational r would satisfy (r,r,r)=(2,2,1). Its real coordinate forces r=2,
whereas its 3-adic coordinate forces r=1. Contradiction. Thus P123.014 §4
fails already on the identity class, and the restrictions invoked in
P123.015 §6 and P123.016 §6 do not follow.

An enlarged gauge group is not a remedy: it is still diagonal. Projection
A_S'^times -> A_S^times also does not automatically descend modulo the
specified unit groups, so reversing the arrow without a construction is
not a repair.

The coefficient embedding f -> f tensor 1_Z3 in P123.006 is a different
operation. It does not define a point map x -> (x, 'compact-unit
coordinates'), nor a functor on the quotient stacks. A geometric transition
may require a span or induction construction, with explicit coherence and
compatibility with coefficient embeddings. This audit does not refute the
coefficient embedding itself.

## 3. What the numerical argument does and does not prove

Conditional on the continuous Hermitian test pairing and dagger identities,
P123.017 §§1–4 correctly prove

    R_W = R_partial intersect ker M,
    0 -> D^0/R_W -> D/R_W -> C^2 -> 0.

There are additional issues in §§5–8:

* g -> I_partial(f,g) is conjugate-linear, so it belongs to the continuous
  anti-dual, not the conventional complex-linear distribution dual. Use the
  anti-dual consistently, or explicitly conjugate the test variable.
* An injective continuous J need not be a topological embedding for the
  quotient LF topology. The closure of its image defines a new realization;
  it is not thereby the completion of the original quotient topology.
* Separation against tests follows directly in that realization. It proves
  neither a pairing between two arbitrary boundary elements nor continuity
  of every carrier operation.
* Formula (6.1) provides, for each fixed test a, a transposed convolution
  operator. Extending dagger requires an estimate for its action in the
  induced topology: Hermitian symmetry alone is not such an estimate.
  Joint module continuity and an action of all completed Fell kernels
  require their own proofs. No map from general coefficient-valued Fell
  sections to these distribution operators is supplied.
* The map from the internal source cone to this external scalar test
  quotient must be specified. P123.010 defines a cone on an intersection
  with a chosen trace subalgebra; this does not automatically identify it
  with the external D of P123.017.

If §7's 'functorial under (6.1)' means stability of a proper nonzero cone
under all test multipliers, it is false. A cone stable under a and -a
contains both a x and -a x, so properness forces a x=0. The relevant
positive operation is a^dagger x a, or a separately specified positive
map, as in P123.010. This is an operation distinction, not a Hodge sign.

## 4. Further analytic/geometric gates

P123.015 uses continuity of the fiber action to claim smooth and locally
constant section convolution. Continuity alone does not supply smooth
vectors or an open stabilizer for each C_0-valued coefficient. One must
prove closure in the declared section class or change that class. Likewise,
stepwise bilinear continuity does not by itself establish joint continuity
on a locally convex inductive limit through its linear universal property.
These are proof gaps here, not claims that every possible replacement fails.

P123.016 requires a specified sheaf/kernel category with the indicated
pullback, derived tensor and pushforward operations, and a comparison with
the completed crossed-product category. Identities of graph supports alone
do not prove that derived comparison. In particular its stated semilocal
transition is already obstructed by §2.

## 5. Corrected acceptance and next gate

A.1–A.4 cannot retain an unconditional global completed/descent verdict on
the basis of P123.014–016. The chartwise automorphism action and formal
twisted tensor identities survive; lift independence with the chosen
unitization and the proposed chart maps do not.

A.6 retains its conditional test-level radical and exact sequence, and the
separating realization after the dual convention is fixed. Its full
completed-carrier action remains open. A.7 and A.8 remain open. B/C/D are
not advanced by this audit.

Before trying to close the cone or RR, specify (1) the corrected coefficient
and bimodule category and (2) genuine chart transition functors. Then prove
the analytic section algebra and numerical representation in those domains.
No unconditional WEIL-STRENGTH-COMPLETE label is justified.

## Verification scope

The existing P123.014, P123.015 and P123.017 regressions can pass while the
obstructions above persist: they test finite algebra identities, not
multiplier membership, semilocal class descent or completed topology.
The counterexamples in §§1–2 are exact arguments, not numerical evidence.
