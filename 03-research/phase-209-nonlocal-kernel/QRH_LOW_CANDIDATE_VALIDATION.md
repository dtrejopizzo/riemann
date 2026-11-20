# QRH — validation of the low-side candidate ell=1/5

2026-10-19. **Conditional low-side proposition, using the stated source
lemmas; verified length and exponent arithmetic. Not a proof of a
zero-free half-plane, not a full audit of the source lemmas.**

## Scope and corpus check

Read project rules, ROUTES-TRIED-INDEX (L74 and current QRH entries), master
grid and CROSSWORD-TO-D.md. Source: OpenAI30Sept2026, local text
/tmp/qrh-review/september.txt, §§12–15, especially Lemma14.3 and the proof
of Lemma15.1. New difference: test the actual hypotheses of the proposed
geometry, rather than minimizing a formal exponent while leaving them
unchecked. The earlier QRH_FOUR_FIFTHS_ATTEMPT.md is not a theorem for
unpublished parameters. No papers are edited.

Assume the exact low separation of§6, marked reflection Cor14.1, hybrid
bound Lemma14.2, reflected energy Lemma14.3 and smooth calculus lemmas as
stated in the source. They are CITED inputs here, not independently proved
from their external sieve inputs. The calculation below derives a changed
Lemma15.1 and low estimate from those inputs. It does not import Prop15.3
unchanged outside its published geometry.

## Candidate and exact finite expression

Use the same finite expression(12.5), same fixed arithmetic data and masks,
with fixed positive slot lengths summing to ell=1/5 and disjoint annular
prime supports. The low proof needs no prime-supply lower bound. Set

    ell=1/5, b=1/10, lx=7/20, ly=9/20, h=17/20,
    X=Z^lx, Y=Z^ly, M=lx+ly=4/5.

Then ly−lx=b, M+ell=1 and h=1+ell−lx. For each rescaled subset J,
let d=sum_(i in J)ell_i, so0≤d≤1/5, and let r_J=Np_J/Z^d. The fixed
annular supports give c_J≤r_J≤C_J, uniformly in moving prime labels.
Exactly as in15.1,

    X'=Z^(7/20−d)/r_J, Y'=Z^(9/20−d)/r_J,
    M'=4/5−2d, ell'=1/5−d,
    Q=Nb_* Z^M'/r_J²,
    Pa=Y'^2/Q=Z^(1/10)/Nb_*.

In particular M'≥2/5, Y' has exponent≥1/4, and Q,Y',Pa≥1 for all
sufficiently large Z, with the lower threshold allowed to depend on the
fixed arithmetic datum and slot system. These are the scale conditions of
Prop15.2; no extra hypothesis on X' is inserted.

## Marked-row hypotheses of Lemma14.3

The physical tuple and mark definitions are unchanged. A fixed subset
retains product-form coefficients and pairwise disjoint prime supports.
The twist νσθ is fixed independently of the row and selected primes.
Fixing the full reflection-modulus sectors separates row and tuple
phases as in Cor14.1 and Lemma14.3; varying exponents does not change these
identities. The common logarithmic profile must be separated BEFORE
absolute row sums, as in the source proof; independently selected measures
for different tuples would not be justified.

The dual source support is retained: squarefree n and cube variable b may
share primes, and may contain the primes of S permitted by(5.2). No extra
S-mask or n–b coprimality is imposed. A forced j=4 prime assigned to N0 is
removed from the squarefree dual ideal only, even if the cube variable
shares it. A B0-assignment removes one cube occurrence and retains its
p^(-1/2) factor. Non-slot active primes are frozen; active slot primes are
whole-index marks. Thus, after freezing the powerful row part and sectors,
the remaining coefficient restrictions retain the independence conditions
of14.16, not an artificial row-dependent coefficient.

Writing O for powerful-row logarithmic length, H for the residual
squarefree-row length, and za for active slot length, the same norm/support
relations hold, up to vanishing fixed-scale offsets:

    H≤M'−O, ΔH=M'−O−H≥0,
    2A0≤O, N0≤A0, za≤ell', S0≥0, B0≥0.

These inequalities concern actual support; they are not new independent
summations over forced primes. The source's O(1/log Z) offsets and small
losses can be retained throughout instead of idealizing them as zero.

## Uniform profiles, retention and row bound

On Gaussian annuli, the joint profile of15.1 depends on log r and all slot
ratios in fixed compact boxes. Its weighted Fourier seminorms are summable,
uniformly in the moving labels, for any fixed finite slot system. The
change from total length1/6 to1/5 does not change the Gaussian derivative
argument. Retain N*=1+ell'+θ_N, with |θ_N| arbitrarily small after the
annular truncation, and discard whole outer annuli before Fourier
absolutization. Lemma14.3 allows bounded log-length ranges and supplies
uniform finite seminorm orders and polynomial norm-twist height costs.

The retained dual length is

    Td=2H+2A0+2za−1−ell'−θ_N−N0−3B0,
    v+3ell_b+e_lambda≤Td+tau_ref.

The identity M'+ell'−1=−3d still holds. Consequently the proof of15.1
still gives Td≤H−3d+small losses. Empty negative dual ranges remain
negligible; bounded unit ranges cost only arbitrarily small powers.
The hybrid quantity u=min(v,za,(v+za)/3) has the same two cases:
u=za, or u≥v/2 up to small offsets. The squared kernel saving in14.14
is extracted on the original support before any positive enlargement.
It is not recomputed on added rows.

The first branch bounds the row exponent by M'−ΔH+small losses. The
second branch, using equation(15.3) in the proof of Lemma15.1, gives

    M'+[1+3ell'−2M'−2ΔH+θ_N]/4+small losses.

Here1+3ell'−2M'=d, not d−1/6. Both expressions decrease with ΔH;
ΔH≥−O(1/log Z) therefore gives the conditional changed-row proposition

    sum_(0<Nm≪Q)|B^J_(m,σ)(Z)|²
        ≪_ε Z^(M'+d/4+ε).                         (LROW)

All fixed-part counts remain those of Lemma14.3: the powerful part adds
O/2 once, supported squarefree parts and local choices cost divisor
powers, and active tuples are already inside the hybrid norm. Counting
any of those again would invalidate this exponent.

## Additive bound and complete low estimate

Prop15.2 states squared additive norm

    ≪(1+|ν|)^JGr (Q/Y')[1+Pa^(1/6)+Pa²/Y'] Z^ε.

For the candidate, uniformly in0≤d≤1/5,

    ly−d−11b/6 ≥ 9/20−1/5−11/60 = 1/15.

Thus Y'/Pa^(11/6) grows at least like Z^(1/15); the bracket is
O(Pa^(1/6)). This checks its absorption, not just its scale range.
Combining with(LROW) by Cauchy–Schwarz gives unscaled tuple exponent

    (lx−d)/2+b/12+d/8.

As in15.8, summing rescaled tuples contributes d and their coefficient
contributes−3d/2. The net additional exponent relative to lx/2+b/12
is−d+d/8=−7d/8. Finite triangle over subsets, with integrable common
Mellin-height norms, therefore proves conditionally on the cited inputs

    |I_modified(Z)|≪_ε Z^(11/60+ε).                 (LLOW)

The exponent11/60 is lx/2+b/12. This is a genuine check of a changed low
bound from the stated scale-uniform inputs, not an invocation of the
published fixed-geometry conclusion. It has not proved the high-side
normalizer or detector estimates for this geometry.

## Exact residual target and arithmetic block requiring improvement

The principal Mellin exponent for this geometry is

    C(s)=lx/2+s−1+h/6=s−41/60.

Consequently LLOW corresponds to formal low threshold13/15. At4/5,
C(4/5)=7/60; a critical low-side improvement of at least1/15 in amplitude
is still needed. Relative to the unchanged additive estimate, this would
require a gain2/15 in squared completed-row exponent for the worst
unrescaled contribution, or another source of cancellation replacing
that Cauchy/triangle chain. No such gain is proved here.

Improving only the SECOND branch algebra is insufficient: the FIRST
branch in Lemma14.3 already permits a long squarefree-source block. For
example the relaxed support constraints allow at d=0

    O=A0=N0=S0=B0=ΔH=0, H=4/5, za=1/5,
    v=4/5, ell_b=e_lambda=0, Td=4/5.

Then u=za and the right-hand exponent14.14 equals4/5=M'. The kernel
saving is zero. In the hybrid norm14.7, this is the regime N≈K≈Z^(4/5),
L≈Z^(1/5), B≈1: its N-dominant cubic bound and long row range supply
no extra saving after normalization. This exhibits a block allowed by
these MAJORATIONS, not a lower bound or proof that actual coefficients
saturate it. The actual reflected coefficients and arithmetic restrictions
may yield cancellation beyond the arbitrary-coefficient bound; proving
that is a precise remaining task. It cannot be obtained by merely
changing ell or dropping the already controlled variance of QRH replicas.

## Limits

The proposition is conditional on the correctness of the stated source
lemmas and their exact algebraic identities. Their coefficient-support
hypotheses and dimensions used here were checked; a full independent
proof of those source lemmas, their external large sieves and all analytic
continuations has not been supplied. No high-side count, prime normalizer,
or zero-free conclusion follows from LLOW alone. In particular13/15 is
not asserted as a new zero-free theorem, and the requested4/5 goal remains
unproved.
