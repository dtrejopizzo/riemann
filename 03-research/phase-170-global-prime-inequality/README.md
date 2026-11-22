# Phase 170 — The global inequality on the primes

Status: **OPEN; audit and formulation, no closure of D**.

> Update R170_884--885: the exterior use of `S` was corrected to `S_N`
> and the exact Euler--Maclaurin port was built. The polar term replaces the
> predictor with `Z_N^*=S_N^*-C_N^*`; it does not cancel discrete coefficients
> separately. The current gap is the sign of its Wronskian on the vector of
> first contact, keeping the tails `U_N` and `R_M`.
>
> R170_886 fuses that block into the anchor
> `e_EM=q_N-C_N^*h` and proves that the full exterior law is equivalent to
> the range equation `H_T g_EM=A_M^* dot(e_EM)-dot(A_M)^*e_EM`. The next
> construction must solve this equation using the exact incidence;
> quadratic minimality alone does not force it.
>
> Audit R170_887: that range equation is the Fredholm criterion of
> the frozen law, not an autonomous reduction. For a minimal branch, `chi_e`,
> `A dot F`, `dot P`, and the Tate connection `dot R_T` must be added.
> The pending law is the covariant vanishing of R170_887(5.1).
>
> R170_888 inserts the full `Z_N` ledger into the minimality equation.
> The sign belongs to the quadratic sum of PC, polar term, combined port, and
> Tate connection. Parity refutes identifying the linear EM residue with
> `dot lambda`; without REG the next construction must live directly
> in the finite collar identity R162_405(2.2lambda).
>
> R170_889 records a second neutral audit. It keeps the frozen identities
> and the moving ledger, preserves the constructive value of the range
> source, and corrects only the gauge statement: the invariant Wronskian
> must use a covariant derivative.
>
> R170_890 studies, with a double audit, the quadratization via the
> Tate coordinate. It produces a valid rank-two operator, but the moving
> ledger uses `sigma(F)=2 Re(dotPi F,b)`, not `rho(F)`. A finite
> counterexample prevents inheriting the minimal sign without a new
> arithmetic relation between `rho`, `sigma`, and the EM source.
>
> R170_891 computes the representatives and their Gram matrix. The prime
> route `2` proves that `rho` and `sigma` are independent on the primitive
> space for `T>log(2)/2`. The theorem does not automatically extend to the
> radical; that spectral projection is the new pending piece.
>
> R170_892 formulates the bordered KKT. The physical residue `sigma*Delta`
> is exact virtual work of the moving constraint, but it forms a
> hyperbolic block and does not appear in the minimal Schur complement. A
> moving counterexample leaves its sign free while keeping all of minimality
> fixed. The covariant identification of EM with `g Delta_tot` and the
> full stabilization in `N` remain open.
>
> R170_893 removes an ambiguity: for the frozen jet, the difference
> between `g Delta_Tate` and the EM anchor is exactly a polar
> normalization scalar. The total identification is equivalent to R170_893(0.5),
> with the exterior routes and the coupling `dot C_N ell` preserved.
>
> R170_894 expands that scalar: the law reduces to two truncated
> exterior moments and the moving face `t+log N`. The interior datum of
> first contact does not determine them; the next identity must act on
> that face and the exterior routes before recombining PC.
>
> R170_895 couples `N=e^(2T)` and obtains a law of measures: moving collar,
> jumps at each integer, Euler--Maclaurin density, and the connection of `h_T`.
> After Möbius and Mangoldt, exact fibers `Lambda(d)mu(m)` appear. The
> next piece must cancel the balance as a measure in `T`, including
> the births; an identity valid only within a single chamber is not enough.
>
> R170_896 corrects the extraction: `K(dZ)M=L(dZ)` eliminates exactly
> `Lambda*mu`. The resulting law has degree zero; the virial additionally requires
> `log(r/n) partial_t`. The next piece is the antidiagonal lift
> of this measure identity with the full Leibniz rule.
>
> R170_897 carries out that lift. The connection `delta M` completes
> exactly `Lambda(r)log r`, and the birth subtracts `Lambda(r)log n`.
> The prime channel `Lambda(r)log(r/n) partial_t` is closed. The subsequent
> audit separates the frozen virial derivation from the moving evolution
> `N=e^(2T)`; summing them without declaring a curve duplicates the continuous
> face.
>
> R170_898 integrates the law at the cutoff with finite `L_M`. The weight,
> moment, and face terms of `dot C_N` come from the same density and from
> the nonzero port at `N=1`. The finiteness of `L_M` is essential: the
> infinite prime comb is not naively defined on the tail of `C_N`. What
> remains to be assembled is Gamma, the adjoint orientation, the tail, and Tate
> within the full polar residue.
>
> R170_899 carries out that finite assembly. It exactly separates the polar
> port into Gamma, causal orientation `log(x/r)`,
> adjoint orientation `log(xr)`, and discrete Tate normalization. After
> accounting for the causal channel of R170_898, the minimal residue contains
> Gamma, the prime-adjoint causal orientation, and Tate. Its vanishing or
> sign remain open; the identity assumes no exterior reciprocity.

Requested goal: prove the full inequality for every T > ½ log 5.
That proof was not obtained. This phase fixes the goal without omitting the
hypotheses that remain open in the available reductions.

- [R170_000](R170_000_GLOBAL_TARGET.md): self-contained statement and audit of the input summary.
- [R170_101](R170_101_EXACT_REDUCTIONS.md): elementary reductions proved and the scope of the finite computation.
- [R170_201](R170_201_PRIME_CHANNEL_CONSTRUCTION.md): explicit Hilbert construction via prime towers, with no cross-prime quotients; optimal constant cost and failure of the separated remainder.
- [R170_202](R170_202_HIDDEN_NETWORK_AUDIT.md): repair via hidden networks and the exact obstruction of the polar term.
- [Verification](verify_prime_channels.py): rational identities and consistency checks against the real prime parameters; not a certificate of positivity of W.
- [R170_301](R170_301_COHERENT_ARCHIMEDEAN_PATHS.md): common coupling via a convergent series of prime and archimedean paths; preserves the interactions, with global contraction still pending.
- [Path prototype](verify_coherent_paths.py) and [diagnostics](coherent_paths_diagnostics.json): checks of the identities on Galerkin subspaces, with no certification of the complement.
- [R170_401](R170_401_CONTACT_RESPONSE_AND_DIVISORS.md): exact response of the contraction to the weights, second-order obstruction, and divisor coordinates.
- [Response checks](verify_contact_response.py) and [results](contact_response_diagnostics.json): rational Möbius inversion, eigenvalue differences, and artificial contact; no global certificate.
- [R170_501](R170_501_MULTIPLICATIVE_COMPENSATION_LAW.md): multiplicative compensation candidate, exact second-order balance, and rigidity of local phases. The candidate preserves the spectrum and does not force the sign.
- [Compensation checks](verify_multiplicative_compensation.py) and [results](multiplicative_compensation_diagnostics.json): twisted divisor identity, compensation at contact, and persistence of a negative eigenvalue.
- [R170_601](R170_601_NONLOCAL_STORAGE_ATTEMPT.md): nonlocal compensation with the Möbius responses; exact minimal-cost theorem, with no free sign gain.
- [Nonlocal prototype](verify_nonlocal_storage.py) and [results](nonlocal_storage_diagnostics.json): matrix construction of the compensation and control of its cost; no global certificate.

Reviewed prior work: R163_401 §§1–2, R167_101 (including its ledger),
R169_000 v2, R169_101, R169_190, and the relevant statements of Papers 47–48.
Imported results are cited as results of that record; their numerical
certificates and proofs were not all revalidated.
The status of earlier phases or papers is not modified.

## Construction trial (continuation)

An explicit operator 𝒟_P was built on a direct sum of L² spaces,
with all weights Λ(p^k)/√(p^k), satisfying W_T(F)=‖𝒟_PF‖²+R_P(F).
Its constant budget was shown to be optimal and R_P was shown not to be
positive on its own. The alternative of scalar networks with hidden
variables also fails to represent the full form while preserving the
pointwise modulus. The scopes and prior work are made explicit in the notes.

No external literature was consulted in this trial. The corpus itself was
reviewed to identify constructions already attempted. It is not claimed
that the new documents constitute new mathematics or that they close D.

Reproducible run: `python3 verify_prime_channels.py` from this folder.

## Common coupling (second continuation)

R170_301 builds a positive E_T from Gamma, the prime jumps, and
the cosh moment, and represents W_T=E_T−C_T with explicit positive C_T.
The inverse E_T⁻¹ is built via convergent paths that preserve the
mixed products between primes, separated by the archimedean operator.
The result is a common defect energy, not an already proved positive
norm: C_T¹ᐟ²E_T⁻¹C_T¹ᐟ²≤I is still missing for the weights Λ and all T.
An explicit falsifier shows that the construction alone does not force
that sign. The reduction is linked to the already known transfer of
phase 106.105, without claiming to have overcome its pending condition.

Reproduce the diagnostic: `python3 verify_coherent_paths.py --output coherent_paths_diagnostics.json`.
Requires NumPy and SciPy. Floating-point quadrature is not an interval proof.

## Response under varying weights (third continuation)

R170_401 computes the full derivative of the coupling gain.
At the threshold κ=1 it is 2Σd_n Re c_f(log n). Making it vanish is not enough to preserve
the sign: if the change keeps coupling the kernel to the complement, a
negative second-order direction appears. The scalar and vector responses
are also written via the errors of the divisor identity and its Möbius
inversion. A sign law for the exact arithmetic point is still not proved.

Reproduce: `python3 verify_contact_response.py --output contact_response_diagnostics.json`.

## Attempt at an arithmetic law (fourth continuation)

R170_501 tries a coherent multiplicative deformation of primes, Gamma,
and the pole. The exact law PRP=PVQH_Q⁻¹QVP compensates the second-order cost,
but it is a unitary conjugation that transports the kernel and preserves
any negative eigenvalue. It is not a new positivity law.
Moreover, a local multiplier on all of ℝ realizing phases for every
prime must be e^{iφ+iθt}: the phases of 2 and 3 suffice to prove this.
The result rules out this class of local repair, not nonlocal operators
nor every possible arithmetic mechanism.

The sought sign law remains unproved.
Reproduce: `python3 verify_multiplicative_compensation.py --output multiplicative_compensation_diagnostics.json`.

## Nonlocal compensation

R170_601 moves beyond unitary conjugations and tries a nonlocal operator Z,
with Z−RZR≥I+R. It is shown that every solution has the form
Z=(I−R)⁻¹+ΣR^jSR^j with S≥0. The correction adds a positive cost to the
starting budget; it does not create the pending margin. S is built with
the commutator of the Möbius responses of indices 2 and 3 and the
computation is checked in four finite models and one falsifier. The
global sign remains OPEN; no new arithmetic positivity law has been proved.

Reproduce: `python3 verify_nonlocal_storage.py --output nonlocal_storage_diagnostics.json`.

## Comparison with Paper 46 and Gamma incorporation

[R170_701](R170_701_PAPER47_COMPARISON.md) separates phase 170's
contributions from results already present in Paper 46 and documents text
corrections.
[R170_702](R170_702_GAMMA_DETECTOR_AND_COMPLETE_COLLARS.md) incorporates the
Gamma detector faithful to the storage, computes its exact tail, and extends
the finite collar balance to the full form with its polar term.
The observation is resolved; the sign budget remains open.

Reproduce: `python3 verify_gamma_detector_bridge.py`.
The diagnostics check the identities and cancellations; they do not certify
positivity of the continuous operator. The observed errors are smaller
than 5e-17 in the matrix balance and 6e-18 in the integrated collars.

## Explicit extension and flow trial

[R170_703](R170_703_EXPLICIT_EXTENSION_PAST_LOG5.md) proves, from
Paper 46's certificate, that `W_T≥(10^-18/2)||F||²` up to
`T=(log5/2)(1+exp(-10^24)/4)`. All constants are explicit;
the width is extremely small and no practical improvement is claimed.

[R170_704](R170_704_FIRST_CONTACT_DILATION_FLUX.md) tries a dilation
energy with no new detectors. The identity is proved, but
Möbius does not provide the opposite sign that would be needed. The
global arithmetic law remains open.

## Readings and expanded math.NT search

The requested order **Dubon first, Freedman second** is kept in
[the bibliographic record](../../00-references/arxiv-math-nt-2026-review/README.md).
The record contains the priority PDFs, the full recovered monthly catalog,
the title screening, and the preliminary evaluation of 27 abstracts.
That evaluation is not to be confused with a proof audit nor with a
new positivity result for the program.

## Audit and literature transfers

- [R170_801](R170_801_THREE_GATES_AUDIT.md): checked identities and pending transport from Three Gates. The parallel attempt delivered no review; a focused local audit was carried out.
- [R170_802](R170_802_DUBON_SELECTION_TRANSFER.md): selection cost in entropy and the limit of the transfer from Haar.
- [R170_803](R170_803_BOUNDARY_REPAIR_AND_EXACT_RESPONSE.md): boundary repair and exact residual cost in the inverse metric.
- [R170_804](R170_804_LITERATURE_TRANSFER_REVIEW.md): coverage of the 27 candidates, steps examined, and conditions to make use of them in D.
- [R170_805](R170_805_COMMON_COMPLEMENT_CAPACITY.md): reconstructed proof of a simultaneous bound for windows with a common complement. Does not depend on accepting the RH claim of Three Gates.

Reproduce the diagnostics of the last bound:
`python3 verify_common_complement.py`.
These are floating-point Galerkin checks, not continuous certificates.
The transport to Paper 46's arithmetic operator and the global sign law
remain pending. The full reading of the 27 manuscripts is not complete.

## Transport built and verified

The pending archimedean step from the previous review was resolved as
an exact identity, without concluding positivity:

- [R170_806](R170_806_ARCHIMEDEAN_TRANSFER.md): construction of `Arch_T=b−[γ_E+log(2πL)]I−H_L`, with `L=2T`, explicit compact integral remainder, and joint transport of primes and the polar term.
- [R170_807](R170_807_TRANSFER_INDEPENDENT_AUDIT.md): requested independent verification of that attempt, including domains, capacity, and diagnostics.
- [R170_808](R170_808_FINAL_TRANSFER_AUDIT.md): final audit of this audit and proof that discarding the whole positive reserve can produce a complementary minimum equal to `−∞`.

Reproduce: `python3 verify_archimedean_transfer.py`.
Eight independent quadratures agree with error smaller than `9e-44`;
these are diagnostics, not positivity certificates. The arithmetic
residual with the retained positive reserve remains to be controlled. The new
identity does not validate the remaining transports nor the global
induction of Three Gates.

## Sign attempt with retained reserve

[R170_809](R170_809_SIGN_CONSTRUCTION.md) keeps the full form b in
the complement and proves a response bound via its harmonic extension.
The reserve for null cell averages is explicit:
`b≥(log M+γ_E−1/2)I`. The arithmetic sources are kept together in
the remaining coupling. The inequality obtained is sufficient by scale;
its positivity for all scales has not been proved.

[R170_810](R170_810_SIGN_AUDIT.md) records the audit and a
rational contact example where the bound loses the sign while still being
correct. The two independent attempts requested in this round failed due to
a usage limit before delivering results; both documents were produced by
this audit and do not carry that independent review.

Reproduce: `python3 verify_retained_reserve.py`.
The global problem and the closure of Paper 46 remain open.

## FIDC proposal and audit

[R170_811](R170_811_UNIFORM_ARITHMETIC_LAW_PROPOSAL.md) keeps the
proposal from that independent attempt. The audit in
[R170_812](R170_812_FIDC_AUDIT.md) detects an incorrect adjoint in the
interpretation of the Tate port and a redundant regularization.
[R170_813](R170_813_FIDC_REVISED.md) defines the corrected flow via duality
of forms and proves its exact transport and finiteness. The two proposed
signs remain unproved; the result does not close D.

Reproduce the orientation diagnostic:
`python3 verify_fidc_orientation.py`.
The example checks the adjoint defect even with even data,
but it is not an arithmetic contact nor a counterexample to RH.

## New proposal after the audit

[R170_814](R170_814_ARITHMETIC_GREEN_PROPOSAL.md) keeps the corrected Tate
adjoint and the direct definition via forms. It also builds an
interior contraction with exact correction of both primitive moments;
its energy is nonnegative at contact. The proposal calls for comparing
that energy with the exterior flow and the Gamma reserve via two
explicit arithmetic bounds. Both bounds remain conjectural. The repair of
the object is not presented as a proof of sign nor as a near closure of D.

## Construction and validation round

Two attempts worked on the bounds of R170_814 separately:
[R170_815](R170_815_GREEN_SIGN_ATTEMPT.md) examines the exterior–interior
comparison and [R170_816](R170_816_DIVISOR_SIGN_ATTEMPT.md) the
divisor inequality. Neither obtained the requested sign.
The second attempt's channel d=2 preserves the orientation and locates two
Fourier correlations that do not cancel term by term.

[R170_817](R170_817_ROUND_VALIDATION.md) records the validation,
the domain and scope corrections, and the negative result of the round.
The proof of D was not completed.

## Puzzle map

[R170_818](R170_818_PUZZLE_MAP.md) organizes the proved pieces,
the conjectural gaps, and the neighboring priorities. It distinguishes the
direct route of full energy from the primitive first-contact route;
it does not confuse definition repair with a new sign bound.

## Sequential execution of the map

Three independent attempts built, in order:

1. [R170_819](R170_819_EXTERIOR_INTERIOR_CONNECTION.md): connection via polarization and expansion of the scale defect, with explicit remainders.
2. [R170_820](R170_820_JOINT_ARITHMETIC_COMPARISON.md): joint comparison of PC with its conjugate; the divisor identity is preserved.
3. [R170_821](R170_821_UNIFORMITY_OF_SCALE_REMAINDERS.md): bounds and uniformity limits of the remainders.

[R170_822](R170_822_SEQUENTIAL_ROUND_AUDIT.md) documents the validation and
the corrections of this audit. No new one-sided inequality was obtained
in step 2; step 3 does not close its global uniformity.

## Multiscale piece

[R170_823](R170_823_MULTISCALE_AVERAGED_PC.md) proves that coherently
averaging the arithmetic translations over the scale produces a
smoothing operator and, after compression, Hilbert--Schmidt, while
preserving \(\Lambda*1=\log\). [R170_824](R170_824_MULTISCALE_AUDIT.md) records
corrections to operator order, the sign of the kernel, and the scope of the
compactness. The same gain for the collar coupled with the Poisson
transform has not yet been proved, nor a sign inequality.

[R170_825](R170_825_COUPLED_COLLAR_PHASE.md) completes the phase analysis
left open: the averaged coupled collar gains a derivative for
each fixed shift and its compression is Hilbert--Schmidt. The finite
arithmetic sum preserves the exact coefficients. [R170_826](R170_826_COUPLED_COLLAR_AUDIT.md)
validates the phase, the constants, and the scope. The compactness obtained
does not impose a sign nor is it uniform across the cutoffs with the
current bounds.

## Matrix on the radical

[R170_827](R170_827_RADICAL_MATRIX_CANCELLATION.md) compresses the full
multiscale identity to the radical, introduces the faithful Gram matrix of
Gamma moments, and gives an exact spectral criterion, plus finite-rank
approximations for the averaged collar. [R170_828](R170_828_RADICAL_MATRIX_AUDIT.md)
records the correction of a double count and the independent review.
The matrix precisely separates the two inequalities that would produce
the contradiction, but neither of them is proved.

## Gamma--exterior Euler bridge

[R170_829](R170_829_GAMMA_EULER_MATRIX_BRIDGE.md) formulates the lifting
equation that would insert the Gamma--Euler reserve into the same exterior
functional. It proves that any synthesis that stays within the
window is annihilated by the weak equation and cannot realize the reserve.
[R170_830](R170_830_GAMMA_EULER_BRIDGE_AUDIT.md) validates the factors,
signs, and scope. A Green formula for exterior exponential tails remains
to be built; the sign matrix inequality remains open.

## Exterior formula and refined map

[R170_831](R170_831_EXTERIOR_GREEN_FORMULA.md) computes the exact response
of (m(D)) and of the two prime orientations on the exponential tails of
R170_829. The jump produces a logarithmic singularity (L^2), not a
delta. The comparison with phases 121, 122, 124, and 162 shows that the
exterior kernel and the collars were already known; the new precise
blocker is that the weak equation does not define a Tate port outside the
window.

[R170_832](R170_832_PUZZLE_MAP_V2.md) updates the full map and the
non-duplication inventory. [R170_833](R170_833_EXTERIOR_GREEN_AUDIT.md)
validates the formula and separates its contribution from the still
open Green identity. The next piece is to canonically derive the ports
(\Theta_\pm), or build a boundary quotient in which that ambiguity cancels.
D remains open.

## Canonical port and source–port map

[R170_834](R170_834_CANONICAL_TATE_PORT.md) distinguishes the canonical
Hardy port produced by the source from an arbitrary Tate pairing with
exterior tails. It proves that two natural extensions do not coincide and
that the bilateral sum does not remove the ambiguity. The intrinsic quotient
only controls \(Z_0=\{F:r_F=0\}\).

[R170_835](R170_835_QUADRATIC_SOURCE_PORT.md) computes the exact Gram
matrix of the finite map towards the Gamma columns, proves the
impossibility of a universal finite factorization of the Hardy germ by
\(R_L\), and locates the effective entry point of \(\Lambda*1=\log\) in the
finite PC carrier. The next obligation is to build a finite mixed form with
the same residual in its Gamma–Euler and inverse Hardy readings.
[R170_836](R170_836_SOURCE_PORT_AUDIT.md)
validates the formulas and delimits their scope. A sign law has not yet
been obtained.

## Mixed form, two windows, and map v3

[R170_837](R170_837_MIXED_PC_FORM.md) builds the maximal
difference--sum polarization and shows that a fixed-window form cannot
contain the right minimality. Its two-window proposal is audited in
[R170_838](R170_838_TWO_WINDOW_AUDIT.md): the renormalized filter introduces
Tate and nonlocal residues with no sign, and the Chebyshev comparison was
already exhausted in R162_406. [R170_839](R170_839_PUZZLE_MAP_V3.md) records
the available pieces, the refuted connections, and the current gap: a
bilateral collar law that separates the observed Gamma moments from the
full tail using the exact arithmetic of \(\mathbb Z\).

## PC curvature and minimal residue

[R170_847](R170_847_TWO_PARAMETER_PC_CURVATURE.md)--[R170_853](R170_853_CAUSAL_GRAPH_CURVATURE_AND_ARITHMETIC_MISMATCH.md)
build the two-scale PC, its causal Möbius extraction, and the correctly
typed exterior Wronskian. [R170_854](R170_854_GRADED_EXTERIOR_WRONSKIAN_GREEN.md)
proves the Green law `bulk + exterior = Tate` and shows that its
graded realization is indefinite.

[R170_856](R170_856_FULL_PC_JET_AND_BOUNDARY_LEDGER.md) corrects the
provisional reading of [R170_855](R170_855_MOBIUS_TWO_JET_ASSEMBLY.md): the
full jet `2K+K2` cancels between Poisson--`X` and the hyperbolic
branches. The identity `gamma+W=2 Lambda log` is correct within one branch,
but it does not survive as an independent physical contribution.

Under REG/C1, [R170_857](R170_857_KATO_RADICAL_TRANSVERSE_REDUCTION.md)
separates the block signed by minimality, `Z dot H Z<=0`, from the
unsigned transversal block. [R170_858](R170_858_RESOLVENT_WARD_SANDWICH.md)
finally reduces the Tate defect to a single transfer function

\[
 (Q_K\eta,RQ_K\dot HZf),
\]

and expands it via finite PC with Möbius, tail, reflection, polar term, and
combined port. The scalar `RES--WARD` law evaluating this sandwich
remains open; linear PC, minimality alone, and isolated Selberg do not
imply it.

[R170_859](R170_859_GAUGE_INVARIANT_EXTERIOR_CONNECTION.md) corrects one
last coordinate dependence: the resolvent sandwich can vanish via a
Kato gauge and reappears in the exterior connection. The intrinsic
residue is the scalar connection defect

\[
 \Theta_{\rm ext}=(q,\chi_f)-(Q_K\eta,RQ_K\dot HZf),
\]

and the exact defect is
`g Delta_Tate = W_K + Theta_ext`. The open piece is now formulated as
a connection identity, not as the sign of a gauge-dependent spectral
block.

[R170_860](R170_860_TWO_SCALE_HOLONOMY_AUDIT.md) audits the holonomy
interpretation. The rectangle of the mixed form is an exact differential,
the physical family does not depend on the comb's scale, and `S(q)A(r)` is
not self-adjoint. Moreover, every deformation obtained by congruence with
the causal comb is pure gauge. Seven requirements are fixed for a second,
non-congruent arithmetic connection; no object built so far meets them.

[R170_861](R170_861_POSITIVE_BLOCK_DILATION_NO_GO.md) classifies the
positive self-adjoint extensions via an auxiliary space. If its Schur
complement is the physical form, the full matrix is a triangular
congruence of `H direct-sum G` and the second scale is pure gauge. If the
cross block vanishes on the physical fiber, it only contributes at second
order. The class still alive is reduced to a linear, self-adjoint,
arithmetic deformation of the Schur complement, with nonzero first jet
and every port incorporated.

[R170_862](R170_862_BORDERED_NULL_ANCHOR_LAW.md) corrects the homogeneity
of that specification: the Tate defect is linear in the contact vector,
while a Schur diagonal is quadratic. The correct encoding is a mixed
block against a boundary anchor. Bilateral positivity only annihilates
that block if the anchor also belongs to the kernel. The known Tate port
has a positive Gram matrix; what remains is to realize the interior
cancellation of the hyperbola as a second null vector within the same
positive form. This is the bordered null anchor law.

[R170_863](R170_863_DIVISOR_INCIDENCE_NULL_ANCHOR.md) builds that anchor
in a finite incidence complex of routes `(d,m) -> k=dm`. The vector
with coordinates `Lambda(d)/sqrt(dm)` and `log(k)/sqrt(k)` lies exactly
in the kernel of the positive Laplacian `partial*partial`; by Möbius, this
nullity characterizes the values of `Lambda` at each cut. Its two-scale
deformation has normal jet
`(A_raw-K_-)_{<=N}`. The Laplacian only sees the square of that jet, so
the pending piece reduces to a Green map from the normal
of the divisor complex towards the full exterior--Tate port.

[R170_864](R170_864_GLUED_INCIDENCE_POISSON_COMPLEX.md) corrects the
target of Green: the hyperbolic normal `A_raw-K_-` must be glued to the
Poisson face `-K_-`. The full Chebyshev jet cancels before compressing, and
the admissible normal is the full reduced PC of R170_856(3.5), together with
its crossed, combined, and polar boundaries. The incidence anchor
survives as a gluing condition specific to `Lambda`; what remains is to
extend it as a null vector up to the full exterior--Tate port.

[R170_865](R170_865_AUDIT_INCIDENCE_ANCHOR_AUDIT.md) performs the audit: `partial=[B,-I]` is surjective and its kernel is the
universal graph `y=Bx`. The positive Laplacian does not by itself select
`Lambda`; selectivity appears by externally freezing `y=log` and using
Möbius. The construction stands as a faithful presentation and as an
explicit projector of the gluing defect, but not as a law annihilating
the port.

[R170_866](R170_866_MULTIPLICATIVE_COMPATIBLE_NULL_LINE.md) repairs that
obstruction by requiring a single coordinate `a_d` to repeat across every
multiple `dm`. The homogenized map
`D_N(a,c)=((a*1)(k)-c log k)/sqrt(k)` is unitriangular and its positive
Laplacian has exactly one-dimensional kernel,
`R (Lambda|_[1,N],1)`. The null line is compatible for every `N` and rigid
against any interior modification. What remains is to extend it positively
to the glued PC complex, preserving that arithmetic dimension and
producing the combined port.

[R170_867](R170_867_PC_GRAPH_EXTENSION_OF_NULL_LINE.md) extends the null
line to PC homogeneous in `(a,c)`. The residual obtained by keeping only
the hyperbolic tail factors exactly as
`R_PC=T_PC D_N(a,c)`. Hence the extended PC Laplacian is
`D_N^*(I+T_PC^*T_PC)D_N`: it preserves the unique null line, but only
changes the normal metric and again loses the first jet. Every extension
factoring through the divisor defect belongs to this class; the missing
port must contain a non-factored component.

[R170_868](R170_868_UNIVERSAL_FACTOR_THROUGH_THEOREM.md) proves that such
a component is impossible within the same space: since `D_N` is
surjective and its kernel is `R(Lambda,1)`, every linear row annihilating
that line factors uniquely through `D_N`. This also holds after
tensoring with the physical space. The only linear way out is to enlarge
the null vector with a boundary coordinate `beta_T(f)` and make arithmetic
and port cancel jointly; `beta_T` must use the first-contact equation
to overcome F1.

[R170_869](R170_869_NULL_LINE_SPLITTING_AND_BOUNDARY_CLASS.md) classifies
every boundary-augmented row:
`ell((a,c) tensor F)=Q D_N((a,c) tensor F)+c beta_ell(F)`.
The class `beta_ell` is the intrinsic restriction to the null line. For the
physical port it is exactly
`beta_phys=g Delta_Tate=W_K+Theta_ext`. PC, Möbius, and every divisor
identity live in the factored ideal `Q D_N`; they do not determine this
class. The remaining obligation is isolated as a law connecting the
tangent cone of minimality with the boundary-augmented class `beta_phys`.

[R170_870](R170_870_ODD_BOUNDARY_CLASS_VS_EVEN_MINIMALITY.md) proves a
parity obstruction: `beta_phys` is linear and odd in `F`, while
minimality, the virial, and the spectral tangent cone are quadratic and
even. A one-sided sign for `beta` on the whole radical is already
equivalent to its vanishing. Moreover, any linear class can abstractly be
attached to the same first-contact operator without altering the factored
arithmetic. Hence an additional odd coupling is needed: a common second
radical, or an arithmetic symmetry that also acts on the exterior port.

[R170_871](R170_871_FACTOR_SWAP_EXTERIOR_CYCLE.md) builds the odd channel
that R170_870 required. The assignments `Lambda(d)` and `Lambda(m)`
share the column `log`; their difference is an antisymmetric cycle under
`(d,m)<->(m,d)`. The full observation kills it via `LS=SL`, but the
intermediate cut produces the exact flow
`PLQSP-PSQLP=-(PLPSP-PSPLP)`. Its antidiagonal derivative is the
exterior polarization of the Wronskian. What remains is to prove that
minimality extends this involution to the reflected, polar, and Tate
terms of the full port.

[R170_872](R170_872_FACTOR_SWAP_CORPUS_COLLISION.md) audits that channel
against R161_057/064. The flow law is correct, but it coincides with the
already known support concomitant; commutativity and the swap only
oppose the interior and exterior blocks and do not force either to vanish.
The specificity of `Lambda` is located in the common Chebyshev face,
while Tate/exterior reciprocity remains open.

[R170_873](R170_873_TATE_MODULAR_COCYCLE_AND_VIRIAL_JET.md) identifies
additional structure the static concomitant did not see. The Tate weights
`Lambda(n)` and `Lambda(n)/n` are the endpoints of the cocycle
`Lambda(n)/sqrt(n) (n^s,n^{-s})`; the swap is `s -> -s` and its jet at zero
is exactly `Lambda(n) log(n)/sqrt(n) (1,-1)`. The arithmetic virial and
the Gamma collar are thus born from the same modular derivative. The door
reduces to realizing that jet as a second null vector in a common
positive form, via the PC-ren expansion with Tate correctly placed. Its
novelty audit clarifies that the jet coincides with the moving
connection of R170_845 and the covariant jet of R161_036/041; what is new
is the dictionary with the factor swap, while the typed port equality
remains open. The object now in play is the scalar
`Delta_N,T^Tate` of R170_852 and the class `W_K+Theta_ext` of R170_859; the
provisional operator defect of R170_845 was retracted by R170_846.

[R170_874](R170_874_MODULAR_COCYCLE_QUOTIENT_NO_GO.md) proves that the
Tate cocycle and its jet still do not determine the gauge-invariant
boundary class. `beta_phys=W_K+Theta_ext` can be varied while keeping
`Lambda*1=log`, linear PC, the cocycle, and diagonal minimality fixed. The
admissible piece is now fixed as a literal exterior naturality: extend the
factor swap to the full PC-ren port, prove that it fixes the physical
datum, and that it acts by `-1` on the boundary coordinate. Postulating that
action would be circular; it must come out of `H_M,N`, `K_N`, `C_N`, the
atoms, and Gamma.

[R170_875](R170_875_STATIC_TATE_PORT_TYPING_AND_FALSIFIER.md) removes the
last static shortcut. `mathfrak P=Z_N A_M Fcal` was applied to the wrong
datum; the oriented repair is `Z_N A_M`. Its Tate port has an explicit
finite formula, and already for `T=(log 5)/2`, zero exterior, and
`r=b_+`, its coordinates are approximately `(0.95543,-1.03070)`, not
`(1,1)`. The remaining legitimate object is the combined derived port of
R170_852 together with the full polar term of R170_856(9.2)--(9.4).

[R170_876](R170_876_FULL_PC_FACTOR_SWAP_OBSTRUCTION.md) proves that the
factor swap fixes the hyperbola `LS-K`, but not the physical operator
`A_L=M-(L+L*)`: it transforms it into `A_S=M-(S+S*)`. The exact defect
between the two physical sides is
`S A_L-L A_S=(S-L)M+L S*-S L*`. Hence the pure extension proposed in
R170_874 is too strong. The admissible law must be covariant and keep this
archimedean/reflected cocycle together with its polar, Tate, and
exterior ports. Moreover the swap does not preserve PC's derivation:
`-[X,S_N]` has weight `log n`, while `-[X,L_N]` has weight
`Lambda(n) log n`. Their difference `Omega_N` is the prime virial force that
appears before recombining. R170_877 verifies that PC cancels it
exactly against the difference of the two hyperbolas; it does not survive as
a new boundary class.

[R170_877](R170_877_SWAP_PC_CANCELLATION_AND_EXTRACTION_OBSTRUCTION.md)
expands the two full orientations. The derivation defect
`D_K=K_S-K_L` and its full second jet cancel exactly against the
difference of the hyperbolas; the only residue is the swap-even physical
cocycle `partial_-(S A_L-L A_S)`, plus the renormalized polar term. After
that, the swap cannot pass to the extracted port: `PS*P` is invertible
because of `S`'s unit term, while `PL*P` is nilpotent because
`Lambda(1)=0`. The law must be proved before extraction and then transported
via the only existing causal inverse.

[R170_878](R170_878_MOBIUS_EXTERIOR_LOOP_FOR_Q.md) uses that asymmetry
instead of fighting it. From `(PS*P)^-1=PM*P` and `S*M*=I` it obtains the
exact formula `q=-QS*QM*Pb`: the causal Tate predictor is an exterior
loop of the full comb and its Möbius inverse. With `Lambda=mu*log`, also
`L=MK`, so that `z_F` and its Wronskian are written entirely in the
exterior blocks of `S,M,K`, the Gamma operator, and the explicit tail
`R_M=L-L_M`. The alternating form still has no sign, but it no longer
contains a free exterior lift nor discards the tail that keeps acting on
`Q`.

[R170_879](R170_879_BOUNDARY_MOBIUS_DIVISOR_LAW.md) expands that loop
point by point. For `t>T`, the coefficient of `b(t-log k)/sqrt(k)` is the
partial sum `sum_{n|k, |t-log n|<=T} mu(k/n)`. The full sum would be
zero; the exterior predictor is exactly the defect of the routes whose
intermediate divisor crosses the boundary. The law uses every divisor and
the exact values of Möbius, is uniform in `T`, and keeps the intermediate
point. Its coefficients have no fixed sign, so the next step must
combine it with the Euler tail and the polar continuum via a
summation by parts over divisors.

[R170_880](R170_880_BOUNDARY_FIRST_MOMENT_IS_MANGOLDT.md) obtains that
first summation exactly. The mass of the moving divisor incidence
is `2T delta_1`, while its first moment is `2T Lambda(k)`. Separating
`t` inside and outside the window gives the oriented law
`exterior moment + interior moment = 2T Lambda(k)`, with the interior
as an explicit finite sum over `n|k`, `n<e^(2T)`. What remains is to show
that the physical Wronskian and the polar continuum use exactly the same
collar before recombining; that is now a coefficient-by-coefficient test.

[R170_881](R170_881_AFFINE_MANGOLDT_EXTRACTION_AND_SHAPE_REMAINDER.md)
audits the scope of that law. For every exterior test, its affine
component produces exactly `2T Lambda(k)`; a residue remains given by
the pairing of the divisor incidence with the non-affine part of the
test. The first moment does not control that quotient. If the literal
expansion of the Wronskian and the polar term verifies the disintegration
(3.1), the closure reduces to annihilating or signing the sum of those
shape residues via minimality and the Gamma port.

[R170_882](R170_882_LOG_WEIGHTED_BOUNDARY_MOBIUS_WARD_LAW.md) carries out
the corresponding disintegration for the physical derivative. `dot q`
contains the partial sum `sum mu(k/n) log n` over divisors whose
intermediate point stays in the window; its uncut value is exactly
`Lambda(k)`. Thus the exterior Wronskian separates, on the core, into a
literal Mangoldt channel and a residue formed only by excluded routes.
The remaining door is to cancel that residue with the polar continuum and
the Gamma connection, without estimating it term by term.

[R170_883](R170_883_BOUNDARY_DIRICHLET_COVARIANT_DERIVATIVE.md) passes to
the correct type for that comparison. The incidence series is the
truncated Dirichlet sum divided by `zeta`, and the log-weighted
incidence is its covariant derivative
`-(partial_s+zeta'/zeta)`. The excluded routes are exactly the
logarithmic comb outside the multiplicative interval, also divided by
`zeta`. The polar continuum cannot cancel it coefficient by coefficient;
the legitimate door is to identify route plus polar term with the
derivative of the sum--integral discrepancy on the transformed Poisson
side.

[R170_900](R170_900_PC_TATE_COLLISION_AUDIT.md) audits the substitution of
the full PC identity into the residual of R170_899. The operator identity
is correct, but it exactly recomposes the R170_853/R170_856 ledgers and
does not reduce the logical obligation. The remaining object keeps the
tail `H_(M,N)`, the Wronskians with `k>N`, Gamma, the Fourier jet, and the
exterior ports. In Tate coordinates two copies of
`rho (dot b^0,b)` appear; cancelling one would require a tangency of the
contact branch that has not been proved.
