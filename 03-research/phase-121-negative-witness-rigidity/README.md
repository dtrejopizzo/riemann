# Phase 121 — Negative-witness rigidity, beyond the positive-lift architecture

## Status

Active phase.  No theorem or candidate is assumed at entry.

Phase 120 closed the zero-residual Green construction but did not prove its
primitive sign.  It also classified the common architecture behind the
failed global-square candidates.  Phase 121 is not allowed to restart that
architecture under a different mathematical vocabulary.

The binding input is
[`../phase-120-global-polarization/P3_COMMON_FAILURE_ARCHITECTURE.md`](../phase-120-global-polarization/P3_COMMON_FAILURE_ARCHITECTURE.md).
The phase-120 verdict is
[`../phase-120-global-polarization/PHASE_120_CLOSURE.md`](../phase-120-global-polarization/PHASE_120_CLOSURE.md).
The corpus-wide atlas of the overloaded localized operator `A_T`, its exact
realizations and the twelve already exhausted mechanism families is
[`P121_AT_CORPUS_ATLAS.md`](P121_AT_CORPUS_ATLAS.md).  It is binding for every
new proposal: a change of coordinates on that atlas is not a new source of
sign.

The terminal dependency graph is frozen in
[`P121_GLOBAL_SQUARE_CLOSURE_MAP.md`](P121_GLOBAL_SQUARE_CLOSURE_MAP.md).
It identifies zero-mode uniqueness, annular gap transport, little-o Abel
slope and physical divisibility of the oriented commutator as four exact
coordinates of one remaining theorem.  The graph-domain theorem, Abel-slope
formula, local nilpotent inverse, first-contact reduction and cofinal passage
are already closed and must not be presented as further open gates.

The external comparison with Bombieri, Suzuki and the shifted pair is audited
in [`P121_BOMBIERI_SUZUKI_XIA_AUDIT.md`](P121_BOMBIERI_SUZUKI_XIA_AUDIT.md).
Bombieri--Suzuki validate the variational first-contact setup and the
Cartwright/Riemann--von Mangoldt endgame is unconditional.  The proposed
`Xi_a` test, however, is not yet a canonical finite test: its first-contact
state is abstract rather than explicit and its local Euler source has rank
two, so the zeta scalar range certificate must first be typed using local
rank one.  `Xi_a` is binding as a falsifier after that theorem candidate is
stated, not as a substitute for constructing it.

The common strong graph now also supplies a canonical completed incoming
boundary.  [`P121_GRAPH_RENORMALIZED_INCOMING_CURRENT.md`](P121_GRAPH_RENORMALIZED_INCOMING_CURRENT.md)
proves that on a first-contact state it exists uniquely and equals
`-Z_(T,+) r_epsilon`; hence it is at most two-dimensional (one-dimensional
after parity).  This closes the boundary-existence qualification without
claiming convergence of the separately divergent literal Euler tails.  The
remaining theorem is compatibility of this forced current with the annular
amplitude, not construction of the current itself.

[`P121_TATE_PORT_OPPOSITE_PARITY_RIGIDITY.md`](P121_TATE_PORT_OPPOSITE_PARITY_RIGIDITY.md)
then proves an exact collar lemma: a nonzero causal Tate image
`Z_(T,+)r_epsilon` cannot have parity `-epsilon`.  Consequently any genuine
cross-port matching which forces that opposite parity annihilates the Tate
multiplier and the completed incoming current.  The audit
[`P121_TWO_PORT_WRONSKIAN_AND_REAL_AUDIT.md`](P121_TWO_PORT_WRONSKIAN_AND_REAL_AUDIT.md)
corrects the tempting next inference: ordinary Real covariance relates two
different causal currents and does not force opposite parity.  It also
proves that the two-port Euler Wronskian is only v94 (321) multiplied by a
common factor, so it does not repair the physical-boundary gap.  Exclusion
of the remaining homogeneous zero mode is still open.

[`P121_CRITICAL_NEGATIVE_HALF_RESIDUE_GATE.md`](P121_CRITICAL_NEGATIVE_HALF_RESIDUE_GATE.md)
computes the exact normalized critical trace.  A nonzero Cauchy residue has
local `H^(-1/2)` mass
`2 pi |res|^2 log(1/sigma)+o(log(1/sigma))`; hence sublogarithmic growth is
equivalent to cancellation of that residue.  Cartwright then annihilates
the source once the cancellation is independently proved.  Distinct poles
in a fixed ordinate window are asymptotically orthogonal at this scale, so
one normalized norm recovers the positive sum of all squared residues in
that window.  The functional-equation symmetric port has zero normalized
mass, while the antisymmetric port has exactly four times the one-sided
mass; hence the entire critical obstruction is now isolated as a positive
squared defect in one causal coordinate.  If the source is nonzero, this
defect has nonzero coordinates at `gg R log R` simple critical zeros; it
cannot be a finite-pole or two-Tate correction.  This is a sharp detector,
not a new intermediate regularity estimate: the live target remains an
Euler-specific equality-state law annihilating that extensive
antisymmetric defect.

Exhausting the ordinate line by compact windows defines the faithful
extended critical square `D_T^crit`: it vanishes exactly for the zero
source.  This closes construction and faithfulness of the defect observable.
It does not close the global Weil square: the sole remaining implication is
that a first-contact state has `D_T^crit=0`.

[`P121_BACKWARD_FORWARD_SECOND_ORDER_EULER_CONTACT.md`](P121_BACKWARD_FORWARD_SECOND_ORDER_EULER_CONTACT.md)
reconstructs this implication backward and forward.  It identifies
`D_T^crit` with the norm of the reduced conormal class of
`H_F(z)=xi(1/2+z)K_F(z)` in the first infinitesimal neighbourhood of the
critical Euler divisor.  The frozen-source dual-number displacement
`E(z+/-epsilon)K_F(z)` constructs the two unsupertraced normal jets directly
from the local Euler--Gamma determinant and proves their symbols are
`-/+ K_F(i gamma)`.  Construction (F1) and faithful descent (F3) are closed.
The sole open object is (F2): an equality-locus, rank-one causal matching of
those two jets before scalar supertrace.  With first contact and exact nesting
already proved, F2 is equivalent in force to the global square; it must not
be reported as a separate intermediate advance.  Global derivative-ideal stability,
ordinary Real covariance and an adjoint variation of the null equation are
explicitly excluded as respectively phase-91, the two-port no-go and a
tautological kernel commutator.

[`P121_F2_DIRECT_CLOSURE_AUDIT.md`](P121_F2_DIRECT_CLOSURE_AUDIT.md)
records the direct attack on that last implication.  Exponential Gamma-step
conjugation reduces to the existing commutator no-go; the two critical
principal parts have the same microlocal orientation and may cancel; and a
universal conormal model `E=z`, `K=c` shows that rank one, Real covariance,
the dual jets and zero scalar supertrace hold for arbitrary `c != 0`.
Therefore the closed local package cannot imply F2.  A proof must derive an
additional orientation-breaking or faithful nonlinear identity from the
global first-contact equation itself.  That identity has not been proved.

[`P121_PARABOLIC_COMMON_NILPOTENT_LIFT.md`](P121_PARABOLIC_COMMON_NILPOTENT_LIFT.md)
constructs an exact common `U(1,1)` parabolic lift of the finite Euler--Gamma
Green phase.  One square-zero generator makes all local phases additive,
and its Krein Wigner--Smith connection is exactly `A_T` times a fixed
positive rank-one matrix.  This removes the artificial multiplicity of the
common `k=0` Tate pole.  The nonzero periodic pole lattices survive as
unipotent monodromy.  The source-coupled connection
`d-(E'/E)K_F N dz` has local monodromy
`I+2 pi i K_F(i gamma)N`; its triviality on a first-contact state is an exact
new coordinate for F2, not a proof of it.  On the same carrier, the two
oriented positive rank-one semimetrics add to `2I`; a parabolic monodromy
preserving both is necessarily trivial.  This two-semimetric rigidity is
proved.  Ordinary Real covariance preserves only one semimetric after
identifying the reflected fibre, so the still-missing F2 law is exactly the
opposite-semimetric compatibility on a first-contact state.  Self-adjointness
does not supply it either: the adjoint port gives the automatic coisometry
`M Pi_- M^*=Pi_-`, while rigidity needs `M^*Pi_-M=Pi_-`.
The trace of the latter defect is exactly `8|c|^2`; after inserting the
critical monodromy coefficient `c=2 pi i m_rho K_F(i gamma)`, its normalized
trace is precisely the negative-half critical square.  Hence F2 is reduced
to conservation of one explicit opposite-metric monodromy trace on a
first-contact state, not to an unspecified matrix matching.
There is also a sharper complex-line reduction.  The exact identity
`tr(M_c^*JM_c-J)=-4 Im(c)`, applied first to `F` and then to the equally
admissible first-contact vector `iF`, kills respectively the imaginary and
real parts of the critical monodromy coefficient.  Thus one scalar
Krein-flux conservation law, functorial on the complex radical line, already
annihilates the full coefficient.  The reduction is proved; deriving that
oriented scalar law from first contact is still F2.

[`P121_F2_SOURCE_FLUX_AND_FRAMING_AUDIT.md`](P121_F2_SOURCE_FLUX_AND_FRAMING_AUDIT.md)
tests four possible derivations of that scalar law.  Opposite nilpotents
create the desired quadratic curvature only by abandoning the commutative
source algebra; tensorization retains the Tate forcing; the two Tate moments
do not improve the sharp logarithmic boundary germ into `H^(1/2)`; and a
genuine sourced determinant deformation cancels the frozen residue and
sees only `K_F'`.  The surviving datum is therefore a critical **framing**
law on the equality state, stronger than preservation of the zero divisor.

[`P121_DENSITY_F2_AND_BOUNDARY_TATE_AUDIT.md`](P121_DENSITY_F2_AND_BOUNDARY_TATE_AUDIT.md)
removes an unnecessary strength from that target.  Pointwise framing at
every critical fibre is not required: it suffices that a first-contact
state's nonzero oriented residues occupy `o(R log R)` of the unconditional
simple-critical family.  Cartwright density then forces the source to
vanish.  The note also proves that a formal four-coordinate match between
two logarithmic endpoint coefficients and two Tate multipliers does not
provide an independent determinant; without a sourced boundary law its
injectivity is first-contact exclusion in new coordinates.

[`P121_RICCATI_POLE_QUANTIZATION_GATE.md`](P121_RICCATI_POLE_QUANTIZATION_GATE.md)
constructs a nonlinear density gate.  For the witness-coupled connection
`L_F=(E'/E)K_F`, the double-pole coefficient of `L_F'+L_F^2` at a simple
critical zero is `c(c-1)`, where `c=K_F(i gamma)`.  Applying the same
reduced-pole law to `F` and `iF` forces `c=0`; a zero-relative-density
version suffices by density F2.  The quantization and density descent are
proved.  In fact one real parity-fixed state is enough: odd residues are
purely imaginary, even residues are real, and Riemann--Lebesgue excludes the
remaining quantized value `1` at high ordinates.  The remaining source
theorem is to bound the double-pole support
from the first-contact equation without defining a reduced meromorphic
divisor by fiat.

## Objective

Find and construct a route to the global square which is not a positive
ambient lift followed by descent to the two-Tate primitive source.

The preferred reversal is the negative-witness problem:

```
assume F in P_T and -B_nuc,T(F,F)<0
  -> derive exact structural consequences for F
  -> contradict an Euler-specific law already fixed by rows (a)--(c),
     unique factorization, or the functional equation.             (1)
```

No positivity certificate for all `F` is to be introduced at the beginning
of (1).

## Binding exclusions

A proposal is inadmissible if, after removing terminology, it asks for any
of the following:

1. a Hilbert map `D` with `D^*D=-B_nuc`;
2. a contraction or intertwiner `Y=Theta X`;
3. a positive trace, state, curvature, metric or Hamiltonian whose pullback
   must later be identified with `-B_nuc`;
4. stability, Hodge--Riemann, reflection positivity or modular inclusion
   whose mixed-source clause is row (d);
5. homological vanishing whose surviving class is the negative direction;
6. orthogonalization, averaging or symmetrization which deletes cross-prime
   Green phases;
7. tensor amplification, Frobenius replication or recurrence already
   covered by the corpus;
8. a commutator/Mourre estimate whose strict sign excludes exactly the
   spectrum it is supposed to rule out;
9. a finite endpoint certificate presented as a cofinal mechanism;
10. an exact equality followed by an unnamed final sign theorem.

## Information that must be retained

Every admissible proposal must retain simultaneously:

* the exact `p^j` weights `(log p)p^(-j/2)`;
* the cross-place Green phase;
* the coherent degree port;
* both Tate conditions;
* compact-support stabilization in `T`;
* the distinction from Davenport--Heilbronn and the shifted rank-two pair.

It should extend naturally to Dedekind zeta functions; if it would imply
GRH for number fields, that consequence must be stated rather than hidden.

## Novelty protocol

For every proposal:

1. state its mechanism in one sentence without field-specific vocabulary;
2. map its objects to the common normal form `||X F||^2-||Y F||^2`;
3. prove that its decisive step is not a positive primitive descent;
4. run a semantic audit over phases 1--120 before construction;
5. identify a kill condition that can fail before comparison with row (d);
6. compare with Davenport--Heilbronn, the shifted pair, curves and Dedekind
   zeta;
7. construct first, compare with `B_nuc` last.

Keyword absence is not sufficient.  Semantic equivalence to an earlier
mechanism rejects the proposal.

## Initial option-search request

Search for mechanisms satisfying the following criterion:

> Propose source-side mathematical mechanisms which rule out a hypothetical
> negative mixed primitive direction for the Riemann Weil form.  Do not
> construct a positive ambient norm, contraction, polarization, stable
> object, positive curvature, positive state, modular inclusion, homological
> vanishing, tensor amplification, commutator estimate or finite numerical
> certificate.  The mechanism must use the exact Euler prime placement and
> cross-prime phase, preserve both Tate moments, and have a falsifiable step
> before any comparison with Weil positivity.  Explain explicitly why the
> proposal lies outside the common positive-lift architecture of phase 120.

Candidate families should be ranked first by architectural novelty, then by
the concreteness of their first theorem.  No candidate is to be developed
until it survives the semantic audit.

## First deliverable

Produce an option matrix with, for each genuinely admissible candidate:

```
mechanism | Euler-specific input | negative-witness consequence
          | pre-row-(d) falsifier | corpus nearest neighbour
          | proof that it is outside the retired architecture.
```

If no candidate survives, record that result.  Do not fill the phase with
reformulations merely to maintain activity.

The completed first-pass audit is
[`OPTION_MATRIX.md`](OPTION_MATRIX.md).  Its initial survivor was developed
in [`P121_CAUSAL_MOBIUS_OBSERVABILITY.md`](P121_CAUSAL_MOBIUS_OBSERVABILITY.md)
and killed by the exact source matrix in
[`P121_CMO_SOURCE_MATRIX_NO_GO.md`](P121_CMO_SOURCE_MATRIX_NO_GO.md): the
logarithmic connection and every Gamma commutator have zero root diagonal,
so the old transport operator (445), rather than the identity, survives
Mobius elimination.

The subsequent commutator-moment proposal is closed in
[`P121_COMMUTATOR_MOMENT_TOMOGRAPHY_NO_GO.md`](P121_COMMUTATOR_MOMENT_TOMOGRAPHY_NO_GO.md).
The exact true/false branch for row (d), and the no-go for propagating
decorated arithmetic singularities after the scalar row-(c) trace, are in
[`P121_REVERSE_ENGINEERING_AND_ASC_NO_GO.md`](P121_REVERSE_ENGINEERING_AND_ASC_NO_GO.md).
The nonlinear radical-domain ideal, its exact collapse to the corona for
every escaping state, and the resulting Euler--Bohr boundary target are in
[`P121_RADICAL_DOMAIN_IDEAL_AND_CORONA.md`](P121_RADICAL_DOMAIN_IDEAL_AND_CORONA.md).
The transfer audit of paper 36, including the all-channel quantifier trap
and the boundary-inner-factor blindness, is in
[`P121_PAPER36_TRANSFER_AUDIT.md`](P121_PAPER36_TRANSFER_AUDIT.md).  The
radial refinement is constructed in
[`P121_WHITE_LIGHT_NORMAL_SLOPE.md`](P121_WHITE_LIGHT_NORMAL_SLOPE.md): on
the smooth core the nuclear graph norm is exactly the first normal slope of
the normalized white-light Euler energy, and a finite slope for a rough
source forces nuclear-domain membership.  The dyadic bootstrap upgrades
the radical statement to the exact asymptotic
`W_epsilon(F_*)=2 epsilon ||zeta Fhat_*||^2+o(epsilon)`.
Consequently the strict improvement `o(epsilon)` is exactly first-contact
exclusion, not another domain estimate.
The comparison with the full phase-116 v94 audit shows that this slope is a
coordinate on the graph-domain gate, not annular gap transport.
[`P121_FRACTIONAL_REGULARITY_GATE.md`](P121_FRACTIONAL_REGULARITY_GATE.md)
identifies the quarter threshold and proves that the optimal scalar
logarithmic boundary profile lies in every `H^s`, `s<1/2`.
[`P121_DYADIC_RADICAL_BOOTSTRAP.md`](P121_DYADIC_RADICAL_BOOTSTRAP.md)
then proves that every finite-window Gamma--Euler zero mode itself belongs
to every `H^s`, `s<1/2`: the compressed logarithmic boundary commutator is
a pair of Carleman operators, and the high dyadic slope absorbs every
finite active shift.  Hence a hypothetical first-loss vector belongs to
the maximal co-Poisson graph domain.

This also corrects the earlier claim that graph membership alone excludes
first loss.  It does not: v94 still requires equality-state annular gap
transport (358)/(441).  The live target is now that transport identity,
with roughness and undefined global observation removed as escape routes.
[`P121_STRONG_COMMUTATOR_AND_FLUX_NO_GO.md`](P121_STRONG_COMMUTATOR_AND_FLUX_NO_GO.md)
uses that regularity to close the strong zeta--Gamma common-product domain
inside the boundary qualification of v94 (451)--(453).  On a radical the
global commutator is exactly zero; whenever the causal localization split
is made, the incoming current is fixed by the Tate forcing.  A separate two-border theorem proves that conservation, Real
parity and two Tate functionals cannot by themselves make this current
zero.  The remaining annular theorem must therefore use an additional
Euler-specific equality law, not another formal boundary cancellation.
The option matrix now imposes a stronger binding requirement: a future
candidate must be nonlinear in the witness, Euler-specific, and must not
linearize back to the first-loss equation or to a positive ambient Hessian.
[`P121_BILINEAR_SELECTOR_AND_NONLINEAR_POLARIZER_NO_GO.md`](P121_BILINEAR_SELECTOR_AND_NONLINEAR_POLARIZER_NO_GO.md)
closes a further escape route.  The full polarized radical equation permits
exact interpolation on every finite residue block, as already constructed
in v94, but its isolated global limit is impossible.  More strongly,
Cartwright overdetermination forces any same-window source that preserves
the critical residues -- even one chosen nonlinearly from the witness -- to
be the original source.  Hence the remaining mechanism must act directly
on one witness and force subdense critical pole support; it cannot be a
second-source selector or off-line polarizer.
[`P121_TATE_VOLterra_RADICAL_INVARIANCE_AUDIT.md`](P121_TATE_VOLterra_RADICAL_INVARIANCE_AUDIT.md)
tests a bounded replacement for the unavailable translation jet.  If the
canonical uncompressed Tate--Volterra Green operator preserved a
first-contact radical, finite-dimensional skew spectral theory and the
clamped identity `L C_TF=-2F'` would force that radical to vanish.  The
exclusion theorem is proved.  Its invariance hypothesis, however, splits
exactly into vanishing of the moving Tate jet and cancellation of the
exterior localization history.  Compressing by the primitive projection
restores primitivity but removes the Volterra Cauchy boundary that makes the
ODE unique.  The candidate therefore exposes, but does not bypass, annular
transport.
[`P121_LOCAL_HANKEL_ROOT_OBSERVABLE_AUDIT.md`](P121_LOCAL_HANKEL_ROOT_OBSERVABLE_AUDIT.md)
extracts the exact nonlinear local discriminator suggested by the
rank-one-per-place law.  On a unilateral prime tower the geometric Euler
connection satisfies
`A_r^*A_r-A_rA_r^*=v_r tensor v_r`; the shifted degree-two model has
generic rank two.  Thus running creation followed by annihilation really
does recover a rank-one root coordinate that the one-sided CMO connection
misses.  The two physical orientations, however, act on histories based at
opposite edges.  Equating those histories is precisely cancellation of the
incoming annular amplitude, so the root observable does not by itself
close first contact.
[`P121_ACTIVE_CONTACT_POLE_COMPLEXITY_NO_GO.md`](P121_ACTIVE_CONTACT_POLE_COMPLEXITY_NO_GO.md)
then closes the tempting density shortcut.  At fixed `T` the active Euler
current is an entire Dirichlet polynomial; subtracting it from
`-zeta'/zeta` leaves every critical residue unchanged in the inactive
tail.  The Gamma ladder has only linear pole complexity, but it cannot
cancel that divisor without a global identity for the tail.  Such an
identity is exactly the incoming-history/annular transport theorem.
[`P121_EULER_BACKSHIFT_RADICAL_TRANSPORT_AUDIT.md`](P121_EULER_BACKSHIFT_RADICAL_TRANSPORT_AUDIT.md)
tests whether one can attack that history by moving a radical between
support scales.  The causal inverse of `I-p^(-1/2)V_(log p)` is compact iff
the complete periodic prime seam vanishes, and then it shortens support by
`log p`.  But it loses one Tate condition at the resonant character,
requires the corresponding moving Tate jet and multiplier to vanish, and
imports the exterior history when applied to the zero-mode equation.  The
result is a precise conditional shortening theorem, not a free cofinal
induction.
[`P121_ALL_PRIME_SEAM_DIVERGENCE_THEOREM.md`](P121_ALL_PRIME_SEAM_DIVERGENCE_THEOREM.md)
proves that the unweighted Hilbert sum of the periodic seams over all primes
has trivial domain on compact sources with the resonant Tate zero.  The
single `k=1` coefficient samples the source transform at
`2 pi/log p`; these points accumulate at the Tate character, and the prime
sum diverges for every nonzero finite-order germ.  Hence finite all-prime
seam energy is already a uniqueness theorem, not a regularity input; a
surviving global law must preserve mixed-prime cancellation before taking
a norm.  The same calculation yields a sharper terminal reduction:
vanishing of only the first seam harmonic on infinitely many primes, or its
decay faster than every power of `1/log p`, forces the compact source to
vanish by accumulation at the Tate character.
[`P121_ACTIVE_EULER_IDEAL_OVERDENSITY.md`](P121_ACTIVE_EULER_IDEAL_OVERDENSITY.md)
proves a finite-window alternative which uses no inactive prime.  If the
witness derivation preserves the local ideals `1-exp(-i omega log p)` on
any active set `S` with `sum_(p in S) log p>2T`, then the associated complete
local divisor lattices have zero density larger than the Cartwright bound
`2T/pi`, so the witness vanishes.  For `T>log 2` the full active set always
satisfies the strict budget by the elementary primorial inequality
`product_(p<exp(2T))p>exp(2T)`.  Thus active local-ideal preservation alone
would close first contact.  The unresolved AEIF lift is equality-state-only:
the compressed radical equation must imply those active ideal conditions
before scalar trace; formal degree-derivation descent is still blocked by
the exact phase-91 defect.
This is a terminal rigidity lemma, not a new rung in the closure ladder:
on the already proved first-contact branch, deriving AEIF is equivalent in
force to excluding first contact and therefore to the global square itself.
[`P121_INACTIVE_PRIME_PAIR_RETURN_RIGIDITY.md`](P121_INACTIVE_PRIME_PAIR_RETURN_RIGIDITY.md)
then removes even the seam and critical-divisor layers from the terminal
descent.  Two oppositely oriented primes above the window diameter are
individually invisible, but their compression defect is exactly translation
by `log(p/q)`.  Along consecutive primes this converges strongly to the
identity.  Therefore asymptotic vanishing of one real mixed matrix
coefficient on a first-contact state forces `||F||^2=0`.  This uses no
positive all-prime bank and survives the phase-106 finite-path no-go.  The
descent is proved; the open source calculation is to obtain that scalar
asymptotic from the unsupertraced Euler--Mobius identity before positive
orthogonalization.  The normalization is load-bearing: the physical factor
`w_p w_q` tends to zero by itself, so the required statement is exact
vanishing or `o(w_p w_q)`, not merely decay of the weighted flux.
[`P121_INACTIVE_SCATTERING_MIXED_DERIVATIVE_NO_GO.md`](P121_INACTIVE_SCATTERING_MIXED_DERIVATIVE_NO_GO.md)
then performs the proposed extraction from the already closed scalar Green
identity.  It fails exactly: Wigner connections of commuting relative Euler
multipliers are additive, hence their distinct-coordinate mixed derivative
is zero for every source.  The `p/q` return visible in the state expansion
is cancelled by the transport of `Q` and unitary normalization.  Therefore
the live source, if it exists, must remain root/matrix valued and
noncommutative before scalar supertrace; scalar inactive scattering cannot
produce the normalized return law.
[`P121_INFINITESIMAL_GAP_ENLARGEMENT_RIGIDITY.md`](P121_INFINITESIMAL_GAP_ENLARGEMENT_RIGIDITY.md)
then sharpens the older v94 annular target.  Before the first delay
`log 2`, the local co-Poisson observation consists only of its `n=1` term
and is exactly the source in logarithmic coordinates.  If a first-contact
state makes it vanish on any nonempty initial subcollar, parity removes the
opposite collar and exact nesting places the same null state in a strictly
smaller window, contradicting minimality.  Thus the missing transport need
not cross the entire annulus: any positive boundary-germ enlargement is
sufficient.  Producing that germ from the oriented Euler--Gamma equality
equation remains open.
[`P121_TRANSVERSE_SEAM_FIRST_CELL_RIGIDITY.md`](P121_TRANSVERSE_SEAM_FIRST_CELL_RIGIDITY.md)
connects that germ directly to the transverse channel already constructed
in phase 120.  On the first causal cell every prime lattice trace is just
`F`, but its physical output is multiplied by `sqrt(1-p^(-1))`.  Hence two
distinct active-prime outputs cannot agree there unless `F` vanishes on a
collar.  At first contact, parity and nesting then force `F=0`.  Therefore
annihilating a single pairwise seam on the radical is sufficient; the full
operator square (5.3) is not needed for the terminal contradiction.  The
remaining source problem is to derive that seam equality directly from the
unsupertraced Euler equality case rather than from a presumed positive
completion.
[`P121_HORIZONTAL_MODULATION_RADICAL_NO_GO.md`](P121_HORIZONTAL_MODULATION_RADICAL_NO_GO.md)
audits a support-preserving attempt to obtain that extra law.  Multiplying
the radical by `exp(sigma t)` shifts its Laplace transform horizontally and
the two Tate moments can be corrected by a fixed finite-rank projection.
But the resulting entire family remains inside the primitive test space;
polarizing against it, and every derivative in `sigma`, is exactly the
already known radical identity `q(F,G)=0`.  Analytic continuation therefore
cannot isolate critical from off-line residue fibres without an additional
source input.
[`P121_COMPRESSED_EULER_DIAMOND_COCYCLE_NO_GO.md`](P121_COMPRESSED_EULER_DIAMOND_COCYCLE_NO_GO.md)
then tests whether global commutativity of the prime correspondences can be
that pre-supertrace input.  Compression converts the representation law
into the exact Toeplitz cocycle
`Omega_T(a,b)=-P U_a(1-P)U_bP`; associativity supplies only the cocycle
identity and does not set `Omega_T` to zero.  For oppositely oriented
inactive consecutive primes the defect converges strongly to `-I`, so the
global flat diamond becomes maximally nonflat on the physical window.  A
valid source law must therefore trivialize this boundary cocycle on the
first-contact state by additional arithmetic information; commutativity and
unique factorization alone cannot do it.
[`P121_EXACT_TATE_COLLAR_LOCALIZATION.md`](P121_EXACT_TATE_COLLAR_LOCALIZATION.md)
proves an elementary exact localization of the two Tate multipliers at first
contact.  Pairing a primitive vector with either Tate character removes the
interior of every prime translation and leaves only its two edge collars;
the balanced weight `Lambda(n)/sqrt(n)` becomes exactly `Lambda(n)` at one
edge and `Lambda(n)/n` at the other.  The Gamma Levy bank gives the continuous
version of the same collar current.  Hence the two first-contact multipliers
are obtained from two explicit scalar currents by an invertible crossed
Tate pairing, and parity reduces them to one scalar current.  The matrix is
the positive Tate Gram composed with the orientation swap and is indefinite;
only its invertibility is used.  This is a localization
theorem, not yet the cancellation of that current or the global sign.

The pre-supertrace `(b -> c)` gap is now typed by
[`P121_ORIENTED_K2_LOCALIZATION_EXACTNESS.md`](P121_ORIENTED_K2_LOCALIZATION_EXACTNESS.md).
The two causal relative `K_2` tame symbols admit a canonically split exact
decomposition into the scalar supertrace retained by row (c) and an oriented
first character `c^(1)`.  On the cofinal first prime harmonics, `c^(1)` is
the complete analytic germ of `K_F` at the Tate point; its vanishing is
faithful and forces `F=0`.  The remaining source theorem is exactly that a
first-contact state has zero `c^(1)` boundary.  The construction does not
infer that theorem from scalar trace cancellation.

[`P121_CENTRAL_JET_ORIENTATION_BRIDGE.md`](P121_CENTRAL_JET_ORIENTATION_BRIDGE.md)
constructs the correctly typed algebraic bridge from the scalar sum to the
oriented character.  A universal Rees variable `z` acts on the two copies
of the already localized normal fibre: evaluation at `z=1` is scalar
supertrace, while one half of its logarithmic derivative is the oriented
character.  This commutes with relative `K_2` localization and is faithful
on the physical antidiagonal.  The earlier interpretation as a componentwise
central-metric derivative is withdrawn: contact labels `(p,j)` and divisor
labels `(p,k)` are different, and moving the divisor creates a Gauss--Manin
term.  The remaining source theorem is ORL, an equivariant lift of the
first-contact equality before the augmentation `z=1`; if proved, the already
established cofinal descent gives `F=0`.

[`P121_REES_POISSON_NORMAL_COMPLEX.md`](P121_REES_POISSON_NORMAL_COMPLEX.md)
realizes that Rees variable on the actual two Poisson arrows of row (c).
For `f in H_cap`, the deformed difference
`z J Z Ff-z^(-1)Zf` has fixed-source normal exactly `Zf`, which is faithful
by Meyer's closed-range theorem.  Applying the place-resolved row-(b)
connection `Z_p partial Z_p^(-1)` after undoing `Z` gives
`K_f de_p/e_p`, exactly the Bloch regulator of the relative `K_2` class;
tame localization then gives `c^(1)_(p,k)`.  This supplies the previously
missing physical comparison between the abstract orientation jet and the
source-defined Poisson object.  The remaining global-square assertion is
that the first-contact inclusion is unramified for this fixed-source normal;
source motion may not be used to cancel it after passing to the quotient.

[`P121_TATE_COLLAR_K2_FOURIER_BRIDGE.md`](P121_TATE_COLLAR_K2_FOURIER_BRIDGE.md)
identifies that normal coefficient with a physical boundary datum.  For the
complete right Tate-collar profile `R_+(a)`, its Fourier--Stieltjes transform
at frequency `omega` is, up to the explicit phase `exp(i omega T)`, exactly
`K_F(-1/2+i omega)`.  Hence the tame coefficient at
`lambda_(p,k)` is the collar mode of frequency `2 pi k/log p`.  The first
harmonics of any unbounded prime family accumulate at the Tate point, so
their vanishing is already faithful and forces `F=0`.  This closes the
object-level bridge from the Tate boundary to oriented `K_2` and the Rees
normal without dividing by zeta.  What remains is a source law showing that
the first-contact equation annihilates those cofinal collar modes before
the complete collar profile is collapsed to the two scalar currents.

[`P121_EULER_DIVISOR_COMPRESSED_COLLAR_FORMULA.md`](P121_EULER_DIVISOR_COMPRESSED_COLLAR_FORMULA.md)
computes the transform of an entire compressed `p^j` tower at the zeros of
its own local Euler factor.  The result is an exact
`interior K_F(lambda_(p,k)) minus right/left collars` formula.  For an
inactive prime every summand cancels term by term because each collar has
already become the complete transform.  Thus inactive compression is zero
for every source while its oriented tame coefficient can remain nonzero.
This proves that the cofinal Rees lift must use the global Poisson/Euler
source before compression; it cannot be extracted from `Delta_TF=0` by
relabeling absent prime terms.

[`P121_CYCLOTOMIC_RESOLVENT_AND_LATTICE_AUDIT.md`](P121_CYCLOTOMIC_RESOLVENT_AND_LATTICE_AUDIT.md)
tests a nonlinear alternative based on root-of-unity filtering and
arithmetic discreteness.  It proves the exact operator filter extracting
the `p^(mj)` sub-tower from one localized degree-one Euler resolvent while
retaining `(log p)p^(-mj/2)`, and proves that a complex radical line whose
critical parabolic monodromy preserves one fixed arithmetic lattice has
zero conormal coefficient.  The two facts do not join: filtering the test
family is already contained in radicality, independent source twists are
unavailable, and paper 42's intrinsic gluing assigns zero integral and real
component to every nontrivial nuclear convolution.  Hence the source
monodromy does not inherit preservation of the row-(a) lattice.  This
retires the cyclotomic-filter/discrete-monodromy closure without modifying
paper 42.
[`P121_ISODIVISOR_DEFORMATION_NO_GO.md`](P121_ISODIVISOR_DEFORMATION_NO_GO.md)
then tests the remaining scalar determinant shortcut
`E_epsilon=E(1+epsilon K_F)`.  Every old zero of `E` is preserved
automatically.  More sharply, if `1+epsilon K_F` were zero-free for even one
fixed nonzero parameter, Hadamard factorization plus the Paley--Wiener `L2`
boundary condition would force `K_F=0`.  First contact supplies only
preservation of the old zeros, not absence of the new ones.  Moreover the
possible new factor has only `O_F(R)` Cartwright zeros, so it leaves the
`R log R` Riemann--von Mangoldt main term unchanged.  Thus neither
infinitesimal divisor preservation nor principal zero density can promote
the determinant deformation to F2.
[`P121_VOLterra_RELATIVE_DETERMINANT_RIGIDITY.md`](P121_VOLterra_RELATIVE_DETERMINANT_RIGIDITY.md)
constructs instead a literal rank-one determinant over the causal Volterra
carrier. Its determinant is `1-eta z K_f(z)`, and its zero-free case is
classified completely: the only nonzero sources are constant initial
interval steps, corresponding to a change of Volterra length. Either Tate
moment excludes every such step. Hence quasinilpotence of this sourced
causal operator on a first-contact state would annihilate the state without
a positive lift or a self-adjoint Euler spectrum. The causal determinant
and classification are proved; deriving quasinilpotence from the
uncompressed equality-state law is not retained as an intermediate
mechanism.  A fixed-`eta` law functorial on the complex radical line already
annihilates that line by applying it to `F` and `iF`; hence it has terminal
global-square force.  Without an independently constructed nonhomogeneous
source normalization, the determinant route is retired rather than left as
another renamed gate.

[`P121_RESOLVED_TATE_COLLAR_INTEGRAL.md`](P121_RESOLVED_TATE_COLLAR_INTEGRAL.md)
evaluates the last scalar collar integral in closed form.  The Gamma part is
the sum of two elementary logarithmic tails, while the arithmetic part is
the pair of finite Chebyshev tails with jumps `Lambda(n)` and
`-Lambda(n)/n`.  Thus the current is the ordinary pairing of `F` with an
explicit prime--Gamma potential.  The jumps prove, with an explicit
primitive witness, that the two Tate moments alone do not kill this
pairing.  At first contact the calculation removes every unevaluated
integral and leaves precisely the special-source orthogonality (4.3); that
orthogonality is not supplied by integration itself.

[`P121_CAUSAL_REES_HALF_LIFT.md`](P121_CAUSAL_REES_HALF_LIFT.md)
constructs the oriented carrier before scalar augmentation.  The localized
operator is exactly the real part of a canonical one-sided prime--Gamma
operator `C_T`, and `A_T(z)=(z C_T+z^(-1)C_T^*)/2` is its source-defined
Rees deformation.  The two coefficients of the resolved collar are
evaluated separately.  On a parity first-contact state, scalar equality
kills the same-parity primitive part of `C_TF`; the logarithmic Rees normal
is exactly the remaining opposite-parity primitive part.  A two-cell
triangular countermodel proves that causality, reflection and scalar
positivity alone do not kill this part.  More decisively, inactive-prime
separation proves that this localized normal cannot determine the global
`c^(1)` coordinate: every inactive local channel is zero while its global
tame value can be nonzero on a primitive source.  Thus the causal lift is a
valid local identity but not the missing global Poisson/Rees lift; the
latter remains an additional source theorem.
