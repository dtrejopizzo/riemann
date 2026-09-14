# P123.032 — external finite-place packets and compact-support stabilization

Date: 2026-09-05. Status: PROVED for the nonunit local integral,
its normalized external-class coordinates and compact-support
stabilization. This does not identify the packet with the common
carrier shadow, nor supply the unit/archimedean/polar contributions.

## 1. Fix the local integral independently of the internal label trace

Let p be a rational prime. Normalize multiplicative Haar measure on
Q_p^* by volume(Z_p^*)=log p, and write d^*u for probability Haar
measure on Z_p^*. For a compact test f on the positive-real component
of the normalized global class group

    H^+ = R_(>0) times product_l Z_l^*,

The full positive-gauge convention of P123.023 has real factor R^*.
Here H^+ is its open-and-closed positive component. For a test on that
full group, use its restriction to H^+ in every formula below. Restriction
is continuous on the declared test steps; the resulting distribution
vanishes on tests supported in the negative component. This convention
also applies to the finite-place packets in P123.033–034.

define only the nonunit packet

    L_p^off(f) = integral_(v_p(x)!=0)
       f(j_p(x)) |x|_p^(1/2)/|1-x|_p d^*x.          (1.1)

Here j_p sends a local idele (x at p, 1 elsewhere) to its normalized
class. The weight is the local half-density fixed-point Jacobian of
P123.006; (1.1) is a defined scalar packet, not an asserted quotient
trace theorem. The region excludes the identity singularity entirely.

## 2. The normalization retains unit twists

For x=p^k u with u in Z_p^*, normalization by r=p^k gives

    real coordinate: p^-k,
    p-unit coordinate: u,
    l-unit coordinate: p^-k for every l!=p.          (2.1)

The last entries are l-adic units. This formula comes from normalizing
the full local idele; it is not raw projection of semilocal idele classes.
Set

    F_p(k)=integral_(Z_p^*) f(p^-k, u at p,
                                   p^-k at l!=p) d^*u.

For k>0, |1-p^k u|_p=1. For k<0, the ultrametric inequality gives
|1-p^k u|_p=p^-k. Thus both signs yield the weight p^(-|k|/2), and

    L_p^off(f)=(log p) sum_(k!=0) p^(-|k|/2) F_p(k). (2.2)

This is an exact shell integral, including the half-density convention.

For a radial test f(a,v)=h(log a), (2.2) reduces to

    (log p) sum_(k>=1) p^(-k/2)
                   (h(k log p)+h(-k log p)).        (2.3)

The familiar prime packet is thereby obtained by an explicit local
integration, rather than by a trace chosen to have these values.
Its identification with I_A remains a separate theorem.

## 3. Stabilization on each compact test step

Assume the real logarithmic support of f lies in [-T,T]. Then F_p(k)=0
whenever |k| log p>T. In particular L_p^off(f)=0 for p>exp(T).
Consequently the sum over all finite places is a finite sum on this
test step, with 1<=|k|<=floor(T/log p). Enlarging a finite place set
past all primes <=exp(T) makes the off-unit packet literally constant.
There is no interchange of an infinite prime sum and a limit here.

The bound

    |sum_p L_p^off(f)| <= C_T ||f||_infinity,
    C_T=2 sum_(p<=exp T) (log p)
                 sum_(1<=k<=T/log p) p^(-k/2)

proves continuity on every fixed compact-support/finite-unit-level
step. The linear inductive-limit property then gives continuity on the
scalar Bruhat test space of P123.023. This asserts no joint bilinear
LF estimate or uniform bound as T tends to infinity.

If f factors through a finite unit set S_0 and p is outside S_0,
the u-average is unnecessary: the sample is simply f evaluated at
real p^-k and unit tuple (p^-k)_(l in S_0). These twists must be retained
for nonradial tests. Appending new unit coordinates to the test by
pullback leaves each already-defined global packet unchanged.

## 4. What this resolves and what it does not

P123.031 concerned the internal rational-label Jacobian on the full
additive transverse product. Its product of Jacobians changes when a
place is added. Equations (1.1)–(2.3) instead form a sum of individual
local packets on normalized external classes. These are different
constructions; the calculation does not identify them or repair their
mismatch by a scalar rescaling.

This resolves the finite-place, off-unit normalization and prime-set
limit for the scalar comparison target in plan C. To close C one still
needs the actual common-carrier realization and a theorem comparing its
shadow with these packets, together with the local unit regularization,
archimedean term, Tate/polar terms and the spatial/spectral cutoff limits.
In particular compact-support stabilization of (2.2) supplies no bound
for those other limits. Neither RR nor the sign required by D follows.
