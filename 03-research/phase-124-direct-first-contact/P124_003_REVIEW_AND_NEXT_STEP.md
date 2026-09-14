# P124.003 -- review and next step

Status: `REVIEW / NEXT-STEP SELECTION`.

Reviewed inputs: `P124_001_JOINT_VARIATION.md`,
`P124_002_TRANSMISSION_ATTACK.md`,
`P124_004_WINDOW_VARIATION.md`,
`P124_005_ARITHMETIC_COLLAR.md` and
`P124_006_RETARD_RANGE_ATTACK.md`,
`P124_007_VIRIAL_COLLAR_ATTACK.md` and
`P124_008_NULL_REGULARITY.md` and
`P124_009_SUPPORT_LEAKAGE_EQUALITY.md` and
`P124_010_TOEPLITZ_LEAKAGE_TEST.md`.

## Verdict

P124.001 now has the needed local corrections: Hermitian variations carry
`Re`, the primitive compact core uses interior bump correctors rather than
the Tate representers, and `O_{p,T}` is fixed as the physical truncated
finite-window operator with activation/tail terms retained.  Its
mathematical outcome is unchanged: the source-respecting on-shell
Gamma--Euler variation gives the radical identity `q_T(F,phi)=0` on
primitive tests, plus the existing Tate multiplier on non-primitive tests.
It proves neither `c=0` nor prime-seam matching.

This is not a rejection of special test families.  A family `G_rho` can be
useful if it brings a new arithmetic estimate, boundary limit or pre-scalar
source identity.  It is tautological only when the argument stops at
`q_T(F,G_rho)=0`.

P124.002 has been reduced to a supersession pointer, avoiding a duplicate
copy of the on-shell variation calculation.

## Window Variation

P124.004 gives a useful exact crossing quotient, but not a closure.  It
correctly avoids deriving a window derivative from mere continuity in `T`:
on the P122.002 logarithmic form domain, old Euler shift quotients are
continuous but no derivative is available.

Two points must be corrected or sharpened before P124.004 is used as a
domain obstruction:

1. The high-frequency Fourier packet model in Section 4 is only a sketch.
   A rigorous counterexample must construct compact-window functions in
   `Q` after smooth cutoff and prove the aligned translated correlation
   has no difference quotient, rather than assert this from packet mass.
2. The birth discussion is a right-crossing calculation.  If
   `n=e^{2T_*}` is exactly at threshold, the channel is absent at `T_*` and
   also absent for `s<0`; hence it does not contribute to the left
   first-contact quotient where `q_{T_s}>=0` gives the sign constraint.
   For `s>0`, the birth is real, but the form may already be negative and
   first contact gives no stationarity or positivity there.  The note must
   keep left derivative, right crossing and exact threshold convention
   separate.

After those edits, the valid conclusion is still negative: window
variation supplies no sign forcing `c=0`, zero prime flux or exclusion.
Any surviving window route needs a genuinely stronger estimate, such as a
signed logarithmic difference-quotient bound for old Euler correlations or
a one-sided endpoint collar density/phase law on the actual minimizer.

## Arithmetic Collar

P124.005 is the real new calculation in this round, but it is not a proof
of Gate R.  It rewrites the first Tate collar current as

```text
J_+(F)=<rho_{+,T},F>,        rho_{+,T}=P_T(e^{t/2} Phi_{+,T})
```

for primitive sources, and keeps the inherited parity relation

```text
c = J_+(F)/(2(sinh T + epsilon T)).
```

The formula for `c` and the crossed Tate collar matrix are inherited from
phase 121, so they should not be counted as new phase-124 progress.  The
new useful item is the explicit residual: the naive identity
`rho_{+,T}=0` is false because the collar kernel has arithmetic jumps that
Tate-character projection cannot remove.  The active `n=2` seam gives a
nonzero jump residual, with the only possible cross-orientation collision
coming from `m=e^{2T}/2`; right seams themselves are unique by the integer
label.

P124.005 still needs several presentation checks before it is used as a
reference calculation:

1. The adjoint identity `(1.3)--(1.4)` must state the inner-product
   convention and verify the signs in the shift adjoint.
2. The relation between the full adjoint kernel and the resolved
   `Phi_{+,T}` kernel must keep the sign convention visible.
3. The Gamma integral is initially an anti-dual object.  The scalar
   `kappa` separation should not split divergent near-zero pieces unless
   the cancellation is kept in the combined expression.
4. `P_T(e^{t/2}Phi_{+,T})` is an `L^2` projection only after checking that
   the endpoint logarithms are square-integrable on the finite interval.

P124.005 does not assume `J_+(F)=0`.  It correctly identifies what would
be needed to prove it at first contact:

```text
rho_{+,T} in closure Ran(L_T)
```

or the signed estimate

```text
|<rho_{+,T},F>|^2 <= C_T q_T(F,F)
```

on the primitive form domain.  For self-adjoint `L_T`, the closure-range
condition is exactly `rho_{+,T} orthogonal ker L_T`, hence exactly the
desired first-contact cancellation for all null states; it is not a
strictly smaller theorem.  The signed estimate is stronger still: it is
continuity of the collar functional on the form quotient, equivalently a
range statement at the `L_T^{1/2}`/form-dual level, not merely exclusion of
a kernel projection.  The evaluated collar kernel and the two Tate moments
alone do not provide either statement.

## Retard-Range Attack

P124.006 gives a useful local matching calculation, not a range theorem.
It shows that `L_TG` matches the arithmetic jumps of `rho_{+,T}` precisely
when the endpoint traces of `G` are those of `e^{t/2}`.  Making such a
matcher primitive forces `G=e^{t/2}+h` with `h(\pm T)=0` and two nonzero
Tate moment equations.  The exact remaining residual is

```text
rho_{+,T}-L_TG = -P_T A_T h.
```

Matching jumps and endpoint logarithms does not imply equality in the form
anti-dual; it only removes the visible singular part.  Pairing the
residual against a first-contact null vector can be killed by
self-adjointness only if the corrector lies in the required
operator/form domain and the expression is actually `L_T h` in the
primitive operator sense.  The affine corrector `h` is nonprimitive, while
projecting it loses the endpoint traces that matched the jumps.

P124.006 also correctly rejects the naive Neumann iteration.  The Euler
part is two-sided, Gamma is a two-sided logarithmic multiplier, and the
Tate projection is global.  Any contraction or bounded inverse for the
iteration would have to exclude the kernel projection at first contact,
which is the desired collar cancellation.

## Virial And Regularity

P124.007 correctly refutes the direct virial route at the algebraic level.
For regularized multipliers, the projected commutator identity contains
`J_+(F_*)` only in the finite Tate projection defect, where it cancels with
the raw commutator contribution.  Positivity `L_T>=0` gives no sign to
`[L_T,iX]`, and a formal zero from `L_TF_*=0` is not a boundary theorem:
unbounded collar multipliers and sharp cutoffs must retain their support
anomaly.

The analytic regularization in P124.007 still needs a proof if the note
wants the full singular multiplier statement: the cited Calderon
commutator estimate for `log<D>` must control constants as the smoothing
scale tends to zero, and the pass to the anti-dual limit against
first-contact vectors known only in `H^s`, `s<1/2`, cannot be assumed.
The finite-dimensional projection algebra already supports the no-go, so
the note should not depend on an unproved singular-limit claim.  The
inner-product convention in `(3.3)` and the conjugation in
`<rho,F>=J_+(F)` should also be stated explicitly; the `K_-` exponent
calculation is consistent.

P124.008 correctly blocks the logarithmic mapping bootstrap.  The null
equation with principal symbol `log<D>` can give finite logarithmic weights
inside every `H^s`, `s<1/2`, but `log<D>^{-1}` does not gain any Sobolev
power.  Iterating log gains cannot produce `H^epsilon`, cannot cross the
sharp `H^{1/2}` boundary, and does not legitimate either window
differentiation or critical transmission.  Its rank-one model is generally
not self-adjoint, since `Lu` is not a scalar multiple of `u`; therefore it
refutes arguments using only the mapping profile `(L+R)u=f`, not every
possible self-adjoint arithmetic bootstrap.  The actual boundedness
citation for `R_T:H^s->H^s` must remain tied to the precise phase-121
cutoff commutator theorem, and the truncated Tate forcing is still exactly
critical at `H^{1/2}`.

## Leakage Equality

P124.009 correctly shows that the abstract leakage identities do not force
`J=0`.  The finite model preserves `theta_sigma^* eta_sigma=I` exactly;
with `theta=(M^{-1})^*`, the calculation gives
`D_sigma=P M^{-1} N M P` with matrix `[[0,-a sigma],[0,0]]`, so the collar
functional on the primitive line is nonzero even while the primitive
Hermitian score is semidefinite with kernel.

The no-go must be delimited.  The score `S` is the Hermitian part of
`-dot D` in the abstract model; P124.009 does not prove that the actual
D.240 metric derivative has exactly that Hermitian score.  Likewise, the
rank-two Tate bound is respected only as a compatible assignment of a
crossblock of norm `1/2`; it is not shown to be the same operator as the
arithmetic Toeplitz/half-density block.  Thus the countermodel rules out
deducing collar cancellation from leakage factorization, Cauchy equality
and a Tate norm bound alone, but it does not rule out a stronger arithmetic
shorting theorem.

## Toeplitz Leakage

P124.010 verifies that the one-sided causal Euler factor has no D.240
collar anomaly: exterior score and collar leakage are different objects.
For the two-sided one-prime Toeplitz test, the displayed matrices check
out exactly:

```text
G=[[321,85],[85,33]],     H=[[20,1],[1,0]],
det(H-lambda G)=3368 lambda^2-490 lambda-1,
<dot D F_-,tau_+>=17(529 lambda_-+10)/64 != 0.
```

The primitive cell used here is the symmetric/parity primitive sector of
dimension two; the full five-point space with two Tate moments has one
additional primitive direction.  The countermodel is therefore a typed
sector test, not a full arithmetic model.

The scalar centering `L=S-lambda_- I` is the main limitation.  It makes the
compressed score semidefinite with kernel, but P124.010 does not construct
a legitimate dual Euler family whose metric derivative adds this scalar
shift while preserving the same support-anomaly derivative.  A reciprocal
scalar rescaling of `theta,eta` preserves `theta^*eta=I`, but by itself it
also preserves the support anomaly; the extra primitive score belongs to
an external normalization unless the family is explicitly realized.  Thus
P124.010 is a no-go for one-prime Toeplitz leakage plus external
first-contact centering, not a falsification of the full Gamma/all-prime
arithmetic shorting route.

The Tate `1/2` comparison has the same limitation as in P124.009: it
matches a collar crossblock norm, but it is not shown to be the actual
rank-two arithmetic Toeplitz/half-density leakage operator that would
control `q_T`.

## Selected Next Task

The next concrete line is a support-to-primitive shorting estimate for the
D.240 anomaly.  Regularize

```text
A_T(F)=< (d/dsigma)|_{1/2} D_{T,sigma} F, phi_+ >
      =-<rho_{+,T},F>
```

with collar cutoffs at scale `delta`, and prove a uniform primitive
form-bound

```text
limsup_{delta downarrow 0} |A_{T,delta}(F)|^2
   <= C_T q_T(F,F)
```

or a strictly equivalent arithmetic estimate that kills the projection of
`rho_{+,T}` on the first-contact kernel.  The estimate must connect the
exterior leakage energy to `q_T`; the factorization
`B_theta^*C_eta`, Cauchy equality and the Tate `1/2` bound do not do this
alone, and a one-prime Toeplitz model with external centering does not
replace that missing shorting.  Local retard matching, anti-dual jump
cancellation, Neumann iteration, virial commutators, log-elliptic
bootstraps and abstract leakage countermodels do not reduce the obligation
by themselves.
