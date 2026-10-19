# P123.103 — Tangential small-frequency bounds and the determinant trace domain

Status: PROVED-IN-REPOSITORY for S(Y) of P123.101.
This supplies a continuous inverse to the real derivative off its kernel
and a precise restriction on a heat-trace determinant construction.

## 1. Small denominators cost at most one conductor weight

For chi=(tau,kappa), let d be the order of kappa. Since d<=c(kappa),
the character relation exp(i tau a)kappa(q)=1 gives

    d tau a in 2pi Z.

If tau!=0, it follows that

    |tau|^-1 <= (a/(2pi)) d <= (a/(2pi)) c(kappa).           (1)

Thus arbitrarily small real frequencies do not cause uncontrolled
division in the Fourier/conductor topology. Let P_0 retain the Fourier
coefficients with tau=0. It contracts every rho_m. Define G by the
Fourier multiplier (i tau)^-1 for tau!=0 and zero for tau=0. Equation
(1) proves

    rho_m(Gf)<= (a/(2pi)) rho_(m+1)(f),
    DG=GD=1-P_0.                                           (2)

Consequently im D=ker P_0 is closed, D has a continuous linear right
inverse there, and S(Y)=ker D direct_sum im D as Frechet spaces.
These statements are proved without assuming the dimension of ker D.
The operators commute with external translations and all finite-unit
averaging projections, because they are Fourier multipliers. They also
commute with level inclusions. Hence (2) gives a uniform conductor
estimate for tangential division compatible with the previous charts.

## 2. Moving completed diagonals have a character contraction

For any nontrivial translation b on Y, a character chi separates b
from the identity. Its translated value is alpha_b(chi)=lambda chi
with |lambda|=1 and lambda!=1. The insertion identity in P123.096 is
algebraic and applies to the completed S(Y) bar as well. Therefore

    H_b=L_(chi^-1/(lambda-1)) h_chi
    satisfies dH_b+H_b d=1.                                (3)

All operators in (3) are continuous in the rho seminorms: multiplication
by a fixed character is bounded in each rho_m by W(chi)^m, and insertion
in degree n is a sum of n+1 such projective tensor operations. This
proves a genuine continuous contraction of the completed twisted bar
for every fixed nontrivial translation, not just for its finite levels.
The bound includes |lambda-1|^-1, so no uniform bound near a fixed
translation is inferred. Equation (3) does not compute the remaining
untwisted homology in degrees at least two.

## 3. Nuclear coefficient topology is not heat-trace convergence

On L2(Y) with Haar measure, characters form an orthogonal basis.
The real translation generator D has eigenvalue i tau on chi. For
each unit character kappa choose the allowed frequency in an interval
of length 2pi/a centered at zero. This yields infinitely many distinct
orthogonal characters with |tau|<=pi/a, since U has infinitely many
continuous finite-order characters.

It follows directly that the positive heat operator exp(t D^2), t>0,
is not trace class: its diagonal entries on that orthonormal sequence
are all at least exp(-t(pi/a)^2)>0. The same argument shows that
(1-D^2)^-1 is not compact. These assertions concern the Hilbert-space
generator, and do not contradict nuclearity of the stronger coefficient
space S(Y).

More quantitatively, at unit level N_n there are |U/N_n| unit characters.
Choosing the above frequency for each gives

    Tr(exp(t D^2) restricted to N_n-invariants)
       >= |U/N_n| exp(-t(pi/a)^2).                          (4)

Each finite-level trace is finite, by summing the Gaussian over finitely
many translated frequency lattices. But the lower bound diverges as
n increases. Probability normalization of the compact unit Haar measure
does not remove orthonormal spectral multiplicity.

## 4. Consequence for A

Equations (1)–(3) give completed tangential inverse and contraction
estimates compatible with the actual finite-level structure. Equation
(4) rules out silently obtaining an ordinary heat-trace determinant
of the real generator just by passing to the nuclear smooth completion.
It does not rule out an appropriately constructed relative, nuclear or
distributional determinant with an explicit trace domain.

In particular the test-integrated normal relative trace of P123.043
is not replaced by this divergent heat trace. A determinant comparison
must retain the prescribed unit/test regularization and prove its
compatibilities. Higher untwisted diagonal homology, that determinant
comparison and the mixed RR remain open for A.
