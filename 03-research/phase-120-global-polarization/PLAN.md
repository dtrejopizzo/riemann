# Phase 120 — global polarization from the rank-one contact category

> **CLOSED.** Phase 120 ended without a proof of the global square. This
> plan is retained as the historical execution record and must not be
> restarted. See `PHASE_120_CLOSURE.md`; the successor is
> `../phase-121-negative-witness-rigidity/README.md`.

Status: plan only. Nothing in this file is a theorem. Paper 42 is not to be
promoted until the success criterion in §8 is proved.

The semantic complement of phases 1--120 and the three carrier-level
candidates that survive it are recorded in
`P3_SEMANTIC_AUDIT_AND_NEW_CONSTRUCTIONS.md`.  The active first experiment is
the arithmetic configuration boundary complex on `S={2,3,4}`; it must be
constructed before its row-(c) trace is evaluated.  The G-125.B/T2 correction
and the required AHK-style Hodge--Riemann/persistence gate are recorded in
`P3_G125_T2_AHK_CORRECTION.md`; that correction is load-bearing.  A finite
correct sign alone has only the status of Doc 125's existing toy model.

The attempted AHK repair is resolved negatively in
`P3_MATROID_FUSION_NO_GO.md`: a faithful Frobenius tower cannot map its
additive exponent law to idempotent flat join, and the configuration repair
reproduces D.142's factorial monoidal-descent obstruction.  The
configuration/Morse implementation is therefore retired.  The active
survivor of that semantic complement is the one-page Mellin-monodromy gate for
the moving regulator cycle.

That final survivor is now resolved negatively in
`P3_TWISTED_REGULATOR_TAU_NO_GO.md`: the topological twist cancels on
self-pairs, while the analytic twist is the already constructed
Hurwitz/Quillen Gamma carrier and its prime assembly returns to G-1.  The
semantic complement is exhausted.

The new active construction is outside those three families:
`P3_GORENSTEIN_FUSION_ALGEBRA_GATE.md` replaces idempotent flat join by a
non-idempotent Artinian complete-intersection algebra.  It gives faithful
coefficient-one Frobenius fusion and finite Strong Lefschetz/HR.  Its decisive
new target is a canonical infinite socle/residue trace whose singular local
part is the contact character and whose archimedean part is the forced Gamma
residue.

The ordinary residue implementation is now resolved by
`P3_EULER_GAMMA_RESIDUE_DICHOTOMY.md`.  An isolated potential has a
finite-dimensional Jacobian algebra and necessarily collapses every faithful
prime-power tower; a non-isolated potential retains the tower but loses the
canonical perfect residue and finite HR theorem.  Separated local potentials
also cannot create the forced cross-place Green term.  Consequently the
active object is sharpened from an ``infinite socle'' to a closed
additive-generator energy form on the completed augmentation ideal, with the
two Tate functionals as its boundary quotient.

`P3_DETERMINANT_CURVATURE_DICHOTOMY.md` rules out obtaining that energy merely
by changing the Hermitian metric on the scalar Euler--Gamma determinant line.
The unique radial metric with the exact forced connection is a constant
multiple of `|D_S|^2` and is flat; Fubini--Study regularization has positive
curvature but multiplies the Green coefficient by a nonconstant factor less
than one.  Hence the missing polarization must contain a genuinely
non-radial horizontal/boundary datum, not another scalar determinant metric.

The active non-radial construction is now
`P3_DIAGONAL_CASIMIR_POLARIZATION.md`.  It assigns \(D_{1/2}^+\) to every
finite place and the forced \(D_{1/4}^+\) Meixner--Pollaczek module to infinity.
The normalized coherent coefficient gives the place-Poisson kernel exactly,
and the diagonal coproduct Casimir minus the local Casimirs is a strictly
positive infinite-depth operator by the Clebsch--Gordan decomposition.  The
remaining gate is the exact connected coefficient comparison (5.3): mixed
composites must cancel through the already proved D.247 degree/tangent
completion, while the archimedean coefficient must be the quarter-Gamma Green
term.  No contractivity or positive square remains to be chosen if that
identity holds.

The exact mixed-composite audit of that candidate led to the Eulerian
idempotent calculation in `P3_EULERIAN_IDEMPOTENT_GLOBAL_SQUARE.md`.  Its
algebraic part is exact: connected projection removes mixed composites and
the grading derivative turns the canonical \(1/j\) coefficient into
\((\log p)p^{-j/2}\).  The subsequent homological claim has been withdrawn.
No common Euler--Gamma differential was constructed, and the former boxed
condition was just the desired residual vanishing rewritten as an
intersection.  At the finite gate \(S=\{2,3,4\}\), every label-only map through
one rank-one line per place has a nonzero kernel separating the two depths at
the place 2.  A viable continuation must instead construct the explicit
depth-sensitive physical synthesis (6.4), including the shifted profile
\(V_{j\log p}F\), and derive its boundary-energy identity independently.  This
is the same unresolved global-square interface isolated by the four-port
reduction; the Eulerian idempotent does not close it.

## 0. Exact objective

For the completed mixed class `D_f`, construct independently of zeta zeros and
independently of the sign of the Weil form a global polarization norm
`||·||_pol` and prove the Hodge identity

    B_nuc(D,D) = deg(D)^2 / B_nuc(H,H) - ||D^prim||_pol^2.       (H)

After the trace/intersection comparison is established, (H) gives
`B_nuc(D,D) <= 0` on `deg D=0`, hence row (d). Equivalently, at every exact
threshold it must produce the lossless defect identity

    D_out - y_N y_N^* = W_N^* W_N.                              (O)

The constant is exactly one. An estimate with any fixed loss is insufficient
because the primitive operator has no spectral gap.

Logical calibration: Weil positivity on the full test class is equivalent to
RH. The intended advance is therefore not a weaker reformulation of that
positivity, but an independent geometric theorem implying it, exactly as the
Hodge index theorem and Rosati positivity do over a finite field.

## 1. Independence rules

A candidate is rejected immediately if it uses any of:

- a zero of `xi`, a spectral projection selected by the sign of `B_nuc`, or
  an assumption equivalent to Weil positivity;
- `A_T >= 0`, `D_out - y_N y_N^* >= 0`, or subquadratic `h^0` as an input;
- a definition of `||·||_pol` obtained by taking the positive part of the
  target operator;
- an unproved passage from finite Galerkin positivity to the continuum.

Allowed inputs are rows (a)–(c): the noncollapsed carrier, periodic section
cohomology, determinant lines, the Witt endomorphisms, the full derived local
contacts, the unique self-dual metric character, composition, and the nuclear
Lefschetz trace identity.

## 2. Counterexample firewall

Every proposed construction is tested before substantial proof work against:

1. **Davenport–Heilbronn.** It must fail at the loss of positive prime-power
   contact provenance; merely using a functional equation or explicit formula
   is disqualifying.
2. **Shifted pair** `Xi_a(s)=xi(s+a)xi(s-a)`. Its norm-indexed coefficients
   have P0, P1 and P2_norm and it has a symmetric functional equation, but
   false central-line positivity. The construction must detect its local rank
   two or its failure of the unique indecomposable self-dual contact character.
3. **Function-field curve.** After replacing the arithmetic carrier by the
   usual curve cohomology, the construction should reduce to the ordinary
   polarized `H^1` argument. Failure here does not logically refute a
   `Spec Z`-specific proof, but it identifies where the proposed object ceases
   to be a genuine Hodge mechanism.

4. **Dedekind zeta.** The place-indexed package is positive rank one exactly
   as for zeta. A proposed construction that is genuinely invariant should
   extend to this setting and would prove the corresponding GRH. If it
   obviously cannot extend, identify the specifically `Spec Z` input; if no
   such input exists, reject it.

Passing P0–P2_norm alone is never counted as evidence of closure. In curves
and number fields, the norm map can identify distinct place/iterate labels;
Hankel indefiniteness after this pushforward is an indexing artifact, not a
failure of the geometric contact package.

## 3. First target: identify the additional datum P3

Rows (a)–(b) contain more than the coefficient sequence. The candidate new
input is the **indecomposable self-dual rank-one contact package**:

- one cyclic Witt orbit `phi_1 -> phi_n`;
- one local contact line at each prime-power tower;
- coherent composition `Gamma_m Gamma_n = Gamma_mn`;
- the unique central metric character `n^{-1/2}`;
- compatibility of determinant contact with the nuclear trace.

Its invariant local model is indexed by `(v,j)`, not by the integer norm:
`K_v(i,j)=log N(v)`, an all-one rank-one Gram block at every place. For a
curve this is `deg(v) log q`; for a prime ideal it is `f_v log p`.

Task 3A: formulate P3 invariantly as a property of a dagger monoidal category,
not as a property of the numbers `Lambda(n)`.

Task 3B: prove P3 for the category already constructed in paper 42.

Task 3C: prove explicitly which clause fails for DH and for the shifted pair.

Stop if P3 reduces after forgetting structure to P0–P2_norm or to the direct
sum of the place blocks; then it adds no usable global input.

### 3D. Connes–Consani interface to test

Use the absolute `F_1`-curve only for structures it actually constructs:

- the stalk `F_1[T^{Z[1/p]_+}]`, perfected at `p`;
- universal Frobenius and the locality sieve selecting the place;
- the local Weil torsors `W_p=Q_p^x` and `W_infty=C^x`;
- the quotient `C^x/p^Z`, whose real factor is the periodic scaling orbit
  of length `log p`, plus the `p`-independent phase circle;
- the tropicalization map from Gauss-valuation profiles to convex
  piecewise-affine scaling-site sections.

These data are promising candidates for the *carrier and gluing maps* of P3,
not a supplied Hodge theorem: the paper does not construct the required
global intersection pairing, positive Rosati trace, or RR inequality. The
specific experiment is to ask whether the two local torsors and their common
archimedean phase produce a canonical cross-place Green morphism, with no
parameter fitted from `B_nuc`.

## 4. Finite-support polarization object

For a finite set of prime-power contacts `S`, construct a metrized derived
object `C_S(D)` for rational finite-support mixed classes. It must retain:

- the full derived tensor product, including local `Tor_1` excess;
- the two ruling/Tate directions;
- a global archimedean Green morphism coupling distinct primes;
- transition morphisms `C_S(D) -> C_T(D)` for `S subset T`.

The local `Tor_1` channel is not sufficient: it is block-diagonal by prime.
Its role, if any, is as the local excess term inside a global construction.
The cross-prime coupling must come from the metrized Green/duality datum and
must be derived rather than inserted from the desired sign.

**Forced-Green death test.** Before trying to prove positivity, compute the
cross-prime matrix produced by the construction. Once the finite contact term
and the exact row-(c) comparison are fixed, Theorem `forcedgreen` forces this
matrix to be the compression of
`log pi - Re psi(1/4+i tau/2)`. Any different coupling kills the candidate.

Deliverable 4A: an explicit distinguished triangle or exact complex whose
determinant recovers the already proved local contact degree.

Deliverable 4B: a dagger or star operation induced by P3 and the archimedean
metric.

Deliverable 4C: a finite Hodge identity

    q_S(D,D) = deg_S(D)^2/q_S(H,H) - ||D_S^prim||_S^2 - E_S(D),

with `E_S` an explicitly nonnegative Gram term. No appeal to the inertia of
`q_S` is allowed in defining the right side.

## 5. Retired implementation: quarter-twisted Calderon/Hodge complex

The exploratory scalar-gap route has been retired. The full residual audit at
`T=(1/2)log 5` shows why: a uniform complement constant discards the
direction-dependent Green response and simply moves the unresolved boundary
layer when the Galerkin cutoff is enlarged. Finite matrices are retained only
as death tests.

The former proof spine was `P3_QUARTER_TWISTED_CALDERON_SPINE.md`: construct the
quarter-holonomy determinant line on the common Connes--Consani phase circle,
glue the Frobenius Tate cylinders, identify the two Tate moments as the full
adjoint obstruction, and derive the exact incoming/outgoing energy identity
from Green's formula. Later audits showed that this lands on the already known
colligation/Douglas wall; it is no longer active.

The port algebra has now been reduced in
`P3_GLOBAL_FOUR_PORT_REDUCTION.md`. The place-Poisson states inserted into
the already proved D.247 conservation law eliminate every local contact
output exactly. The sole active formula is its equation (6): a Green identity
coupling Gamma, the global even/odd tangent pair, one degree port and the two
polar modes. Proving that identity would merely restate the old intertwining
gate, so it is not the current construction target.

### Retired alternatives

### A. Intrinsic Hodge–Rosati implementation (absorbed into the Calderon spine)

Construct a positive trace `tau_S` and a boundary/coboundary operator
`partial_S` such that

    -q_S(D,E) = tau_S(partial_S D (partial_S E)^*)

on the primitive subspace. The sign is load-bearing: the positive Gram must
represent `-B_nuc`, not `B_nuc`.

The decisive issue is cross-prime mixing. A direct sum of local contact Grams
is rejected by the finite-contact obstruction.

### B. Numerical-cohomology implementation (inactive)

Construct theta-type quantities from the same finite metrized complexes,
for example through a Gaussian partition function of an independently
positive reference metric. Prove by Poisson duality an arithmetic RR formula
and then the uniform estimate

    h0_S(nD) + h0_S(-nD) = o(n^2)

for degree-zero `D`, uniformly enough to pass `S -> all primes`.

The growth estimate is an output, never a definition. If its proof uses the
sign of `q_S`, this implementation is circular and stops.

## 6. Exact analytic bridge

Only after the finite polarization is constructed:

1. identify its local determinant terms with `Lambda(n)/sqrt(n)`;
2. identify its archimedean anomaly with the forced Gamma multiplier;
3. prove its bilinear form equals `B_nuc` by the row-(c) trace identity;
4. translate the finite Hodge identity into the threshold coordinates
   `(K_N,y_N,D_out)`;
5. exhibit the categorical remainder as `W_N^*W_N` in (O).

Operational non-circularity test: for a concrete finite-support `f`, one must
be able to evaluate `||D_f||_pol` as an explicit Gram matrix from the
Witt/determinant/metric data *before* evaluating `B_nuc(f,f)`. Its
normalization must already be fixed. Any free scalar or Green parameter set
by matching the row-(c) matrix is circular.

This order prevents defining the polarization from the known output-defect
target.

## 7. Cofinal completion

Prove, rather than assume:

- compatibility under finite-support inclusions;
- closability of the polarization norm;
- convergence of the Green and determinant anomalies;
- density of finite-support primitive classes;
- preservation of the two Tate constraints;
- passage of (H) to the completed mixed module.

A finite certificate may falsify a candidate but cannot establish this step.

## 8. Success criterion

Phase 120 succeeds only if it produces all four statements:

1. P3 is constructed from rows (a)–(b), and the counterexample firewall is
   passed for structural reasons.
2. The positive primitive norm is defined before comparison with `B_nuc`.
3. The comparison proves the exact identity (H), or equivalently (O), with
   constant one and a positive remainder.
4. The construction passes to the completed mixed module.

Anything less is a candidate, an equivalent reformulation, or numerical
evidence—not closure of row (d).

## 8A. Anthropic rank–trace benchmark

The 2026 two-thirds argument compresses the Weil form and uses only its
zero-side inertia blocks plus prime-side trace and Hilbert–Schmidt norm. It
proves at least `2/3` of zeros are simple and on the line (and `5/6`
distinct), but its bandwidth-one optimization has a ceiling near `0.682`.
Higher moments are not available unconditionally in the support range the
same method needs.

Use this as a benchmark and falsifier, not as the main route:

1. Every finite polarization gives a compression which can be compared with
   the Gabor/Poisson matrix in that argument.
2. A merely trace–Hilbert–Schmidt consequence has not used P3 and cannot be
   expected to cross that ceiling materially.
3. The first genuinely new quantitative output would be an additional
   prime-side inequality controlling the Lorentzian off-line blocks, derived
   from the independently constructed polarization.
4. An approximate identity may first improve the `0.6725` record; exact
   factorization with zero defect is the route to row (d). These are separate
   milestones and must not be conflated.

## 9. Immediate work order

The calibration and Galerkin loops are retired as proof engines. The sole
active attack is `P3_EXPLICIT_DIRAC_ATTACK.md`:

1. define one bulk Hilbert space and one first-order quarter-twisted
   Frobenius differential, with its domain fixed before comparison;
2. define its odd/even, degree/contact and Gamma trace maps;
3. impose the Frobenius transmission law and the two Tate exterior
   conditions;
4. compute Green's formula immediately;
5. accept closure only if the remainder is identically zero and the square
   is exactly
   `L_0(X_T^*X_T-Y_T^*Y_T)L_0`.

D.247 supplies only a partial isometry on the arithmetic source range. Its
extension across the defect complements is not canonical; choosing that
extension by comparison with row (c) would hide row (d). Thus no further
finite gate, scalar fit, spectral sweep or abstract pushout statement counts
as progress unless it supplies the explicit domain and boundary calculation
above.

The subsequent resonant-trace calculation sharpens this instruction. The
prime defect boundary is now canonically assembled in the Bohr Hilbert space
and its incoming/outgoing norms are matched by the Real Tate involution. The
active block calculation is therefore the operator-valued coherent
degree--Gamma feedback specified in
`P3_DEGREE_GAMMA_REDFEEDBACK.md`; its internal port is an `L^2` channel, not
a scalar degree line.

`P3_LITERAL_STATE_SYSTEM.md` now supplies the actual Frobenius recurrence,
the quarter-Gamma elliptic state equations and a positive variational bulk
action whose on-shell value is exactly `||W_Gamma F||^2`.
`P3_GLOBAL_SCATTERING_GREEN_IDENTITY.md` now constructs the quarter
determinant transmission `K_(1/4)=M_(b_infty)`, composes it with every
relative prime phase, and proves the exact zero-residual Green commutator.
The sole active theorem is consequently the positive primitive
factorization of that independently constructed commutator. It may not be
obtained by taking its positive square root.

`P3_GLOBAL_SQUARE_BANK_ELIMINATION.md` now puts this theorem in its minimal
non-circular form.  The Green operator is an exact difference of two
independently positive banks, and D.247 eliminates the local contact bank.
The remaining equation is the vector identity `R_T=0` for the complete
Gamma--tangent--degree transmission.  The Real Bohr theorem fixes the
stabilized Poisson boundary but is not silently identified with the D.247
tangent coordinates.  The exact expansion shows that `R_T=0` gives the
global square with no residual.
The earlier formal matrix-inner product is retired: its Gamma block is only
meromorphic `J`-unitary and does not by itself provide a positive
Wigner--Smith operator.

The absolute-geometry input is now made literal in
`P3_ABSOLUTE_TATE_POLARIZATION_ATTACK.md`.  The canonical decomposition
`E_p=C_p x X_infty_tilde` and the principal polarization give
`(i/(4pi)) integral omega_p wedge conjugate(omega_p)=log p`, exactly the
contact coefficient.  The fibre product of the `E_p` over their common
phase produces the coherent degree covector and its primitive orthogonal
complement and fixes a geometric candidate for the formerly arbitrary
D.247 defect extension.  It is not yet a completed Calderon space.  The
remaining calculation is its closure and the Green trace of the
quarter-twisted half-density operator on this fixed fibre product.

`P3_FROBENIUS_SEAM_TRACE_FACTORIZATION.md` removes the remaining reliance
on unidentified D.247 tangent landings.  Cutting each polarized Tate
cylinder gives explicit traces
`alpha_p=sqrt(log p)/(sqrt(1-p^-1)) O_pF` and
`beta_p=p^-1/2 V_(log p)alpha_p`, with
`alpha_p-beta_p=sqrt(log p)F`.  Their boundary loss is exactly
`(log p)||O_pF||^2`.  The global operator is therefore an exact difference
of Gamma/free/outgoing-seam and polar/incoming-seam positive banks.  The
active construction is now the common-phase/quarter-Gamma Calderon map for
these literal seam variables.

The decisive finite-prime elimination is proved in
`P3_COHERENT_PARALLEL_SUM_THEOREM.md`.  In the source-weighted coherent
direction `w_p=sqrt(log p/theta_T)`, the primitive incoming and outgoing
seam states coincide identically.  Their Redheffer elimination constructs
one strict contraction

    C_eff=I-theta_T[sum_p(log p)(I-C_p)^(-1)]^(-1)

and proves

    sum_p(log p)O_p^*O_p
      =theta_T O_eff^*O_eff.

Thus the entire arithmetic block is now one source-defined Schur channel,
not a growing Pontryagin cascade.  The sole active finite theorem is its
quarter-Gamma transmission on the two-Tate primitive support space.

`P3_EFFECTIVE_HERGLOTZ_GAMMA_GATE.md` puts the surviving theorem into
one-port positive-real form.  The effective arithmetic contraction is the
Cayley transform of the weighted Herglotz mean

    H_S=(1/theta_T)sum_p(log p)(1+C_p)(1-C_p)^(-1),

while the Gamma reservoir is the positive-real impedance

    H_Gamma(s)=sum_n alpha_n^(-1)s/(s+2alpha_n).

Their boundary supply difference is exactly `A_T`.  The remaining square
is therefore a finite-horizon storage identity for two explicit passive
one-port systems on `F=L_0G`, not a growing matrix-valued completion.

The cofinal direction is now settled structurally in
`P3_COFINAL_EFFECTIVE_GENERATOR_THEOREM.md`.  The correct variable is

    L_S=theta_S C_eff,S(I-C_eff,S)^(-1)
       =sum_p(log p)C_p(I-C_p)^(-1),

which is exactly additive under place inclusions and converges to
`-zeta'/zeta(s+1/2)` in `Re(s)>1/2`.  On every fixed compact support, all
new places with `log p>=2T` are exactly lossless and the compressed form
stabilizes, rather than merely converging.  Hence no separate cofinal
estimate remains: the finite storage must be functorial in `L_S`, after
which its positive energy passes by exact stabilization.

`P3_FINITE_HORIZON_STORAGE_GATE.md` proves that the final storage cannot be
stationary, since `A_T(0)<0`.  It then constructs the naive left--right
endpoint mismatch from the bilateral scattering and refutes it decisively
at the already certified gate `T=log 2`: its square differs from the exact
Green supply by `178.591...`, stably across three Fourier grids.  Thus
bilateral reflection cannot replace the missing bank transmission.  The
active theorem returns to the source-defined contraction
`Y_red P_T=Theta_T X_red P_T` of
`P3_GLOBAL_SQUARE_BANK_ELIMINATION.md`; neither a stationary factor nor a
fitted Douglas contraction counts.

`P3_PALEY_WIENER_JULIA_SHORT_CANDIDATE.md` fixes and tests a concrete replacement.
It Cayley-normalizes the two independently positive-real impedances,
compresses their Schur transfers to the Paley--Wiener interval model, and
uses the relative Halmos--Julia unitary.  Its defect-to-defect block is
automatically contractive and has the explicit physical landing
`energy direct-sum causal escape`.  The primitive short (17) nevertheless
fails at `T=log 2`: three compact primitive potentials give converged
relative residuals between `0.166` and `0.183`, while the Julia block remains
contractive with norm `0.99987`.  This confirms the phase-64 Floor theorem's
prediction.  The stronger whole-space test in the exact W3 bases gives
operator residuals `0.209`, `0.236`, `0.255` at refine `8,16,32`: the
positive half is free and the realizing half is absent.
The Julia/colligation family is therefore closed negatively for the global
square unless genuinely new geometric data alter the transmission itself.

`P3_DERIVED_THETA_TAU_GATE.md` audits the connected arithmetic-theta repair.
The local `log p` and quarter-Gamma matches are tautological logarithmic
derivatives, not discovery gates.  An arithmetic height pairing is a scalar
and contains no critical-line `tau`; Mellin transformation of its modular
generating variable creates a nonconstant `tau`, but produces the L-function
of the height coefficients and does not transport the Hodge sign pointwise.
Putting `tau` into a family of cycle classes returns to the additive
realisation prohibited by amended Gap G-1, already equivalent to row (d).
This route is closed negatively.

`P3_UNIFIED_JUMP_RECONSTRUCTION.md` is a provenance audit, not an active
construction.  The Dirichlet reduction was already `114_d_10`, its
ground-state/Doob acceptance test already rejects defining the square from
the target, and `114_d_120` already treats the prime--Gamma conductance and
closes the fixed-cutoff Cheeger/Poincare route.  The common Levy notation is

    g_Gamma(tau)=integral_0^infinity
       e^(u/2)(1-cos(tau u))/sinh(u) du,

and gives

    <A_TF,F>=||J_TF||^2-(m_0+2sigma_T)||F||^2.

Because the discrete shift-chain component gives
`J_T^*J_T>=2alpha_N I`, this notation improves the raw scalar comparison
ratio from `1/4` to `1/2` and its leading deficit from `3sqrt(N)` to
`2sqrt(N)`.  The deficit remains of leading order.  The endpoint
reconstruction `E_T` is another Douglas-equivalent formulation and is
retired; it is not the active route to row (d).

`P3_CAUSAL_PRIMITIVE_STORAGE_IDENTITY.md` now performs the finite-horizon
storage calculation that the effective Herglotz gate left abstract.  The
causal Gamma cells and causal prime-delay cells give an exact signed
bulk-plus-terminal identity.  On `F=L_0G`, polynomial division by the Gamma
generator yields a quarter-specific cancellation: the `n=0` Gamma terminal
state is exactly `(-D+1/2)G` and vanishes at the boundary, while all remaining
Gamma terminal energy becomes an explicit positive Laplace-sampling form.
Splitting time into cells of length `log p` further shows that the Gamma
states and prime-delay states are radial and boundary evaluations of one
depth polynomial: Gamma index `n` evaluates at `z=p^(-2n)`, while Frobenius
evaluates at `z=1`.  The missing `n=0` Gamma terminal mode is exactly that
boundary evaluation and is annihilated by the quarter primitive factor.
The global square is not claimed: its new literal target is a structured
radial trace theorem which must combine the interior Gamma dissipation with
the boundary delay energy.  No contraction or square root of the Weil
operator is used in this reduction.

Proposition 4.4 rules out a terminal-only radial trace: samples at
`z=p^(-2n)` cannot uniformly control the boundary value at `z=1`.  Hence the
missing Green differential must be mixed in physical time and radial depth
and must use the causal terms `Dz_n=F-lambda_n z_n`; fitting a radial measure
alone is retired.

The mixed carrier is now explicit rather than conjectural.  The depth field
obeys `(partial_t+partial_u+1/2)Y=0` and the exact seam law
`Y(z,0)-zY(z,log p)=F`.  Evaluating at `z=p^(-2n)` and taking the radial
Laplace functional gives the same causal Gamma state for every prime-cell
decomposition.  Thus no Gamma--Frobenius identification map remains to be
chosen.  The active theorem is the positive transverse Green energy of this
fixed transport system on the compact-potential domain.

The carrier also has a forced positive, un-oriented length observable
`L_p=u+(log p)z partial_z`.  It exactly intertwines source position with
transported position.  The signed Green connection is its oriented
outer-minus-inner boundary combination; the unresolved calculation is the
primitive short of this length.  Coherent degree and the two Tate modes must
leave a centered positive variance with no position leakage.

The leakage calculation is now correctly typed on one universal causal
half-line `h_F(t,l)=exp(-l/2)F(t-l)`.  Every prime cylinder is merely its
`log p` cell chart, and every `L_p=u+(log p)N_z` is conjugate to the same
multiplication operator `M_l`.  Hence support, the two Tate conditions and
coherent degree have exactly zero interior leakage; the earlier formal
variance of the differently typed `L_p` operators has been withdrawn.

The first and only nonzero leakage is created by boundary sampling: Gamma is
a continuous Laplace trace of the half-line, while prime `p` is its lattice
trace at `l=j log p`.  The complete prime energy has the exact weighted ANOVA
split into the coherent lattice trace plus the positive transverse seam
column `K_T^seam`; equivalently, that column is the parameter-free pairwise
square of the relative traces `E_p-E_q`.  The active equation is (5.3): the transverse Gamma Green
energy must reproduce that already fixed seam column with coefficient one;
the orthogonal remainder is the global square.  There is no longer an
unlocated support, Tate, degree, or boundary remainder.

Each lattice trace has now also been transgressed exactly by the first Euler
identity: `B_p=(log p)^(-1) I+(1/2)ev_0+R_p`, where `I` is precisely the
Gamma `n=0` state and `R_p` is integration of the depth derivative against
the centered `log p`-sawtooth.  In pairwise relative traces the common source
term cancels.  Hence the still-open comparison in (5.3) is no longer between
abstract banks: it is the coefficient-one comparison of Gamma dissipation
with an explicit family of Bernoulli depth transgressions, including their
finite-window masks.

The Bernoulli variables are now themselves unified with Gamma.  The depth
Laplace transform `H_F(t,s)` obeys the single resolvent equation
`(D_t+s+1/2)H_F=F`: its samples at `s=2n` are exactly the Gamma states, and
the principal-value samples at `s=-2 pi i k/log p` sum exactly to the
prime-`p` Euler transgression.  Thus (5.3) has become a quadrant Green
problem for one holomorphic field, with Gamma on the positive real axis and
Frobenius on the imaginary axis.  The active construction is the
coefficient-one two-axis Green energy with the already fixed finite-window
boundary masks.

The quadrant carrier has now been compactified to a slit-disk filling.
The generating function `Z_F(t,zeta)=sum_n z_n(t)zeta^n` has weighted
Bergman bulk equal exactly to Gamma dissipation and Hardy terminal boundary
equal exactly to Gamma storage.  Its Plemelj jump at `zeta=p^(2j)` is
`pi i h_F(t,j log p)`, so the complete Frobenius tower is literally the
discrete exterior-cut trace of the same filling.  The radial operator
`2 zeta partial_zeta+1/2` satisfies a coefficient-one Green identity; no
Gamma/Frobenius identification remains.  The active proof of (5.3) is now
the inner-boundary trace theorem for this fixed slit filling, including the
overlap of the different prime cut lattices.
