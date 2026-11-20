# POWER_STATE_073 — Positive progress: all pairs of powers

Status: **PROVED/APPROVED**. Sources POWER_THETA_HAZARD_COMPACT_073.md and POWER_THETA_TWO_COPY_073.md; independent review POWER_THETA_AUDIT_073.md, plus two further reviews. Verifier tools/power_theta_compact_073_verify.py reproduced three times independently: exit0/PASS on4096fixed panels. No campaign over parameters. Papers and phase103 untouched.

## Closed compact

The open obligation of phase103/103_43 was V'''(t)>0 for0<t<1/4, with V=−logPhi and the SAME positive Phi of CONE001. The stronger statement that the fourth derivative of logPhi is negative onALL of[0,1/4] is verified by rational intervals, retaining m1..4 and an explicit tail for ALLm>=5 in each of the five derivatives. Parity forces(logPhi)'''(0)=0. Integrating the certified sign and gluing the exterior proof10343 proves V'''>0 for ALLt>0.

No theta prefix is promoted as a full sum. The certificate uses outward arithmetic with70digits, Machin and rational Taylor, and a single mesh fixed before running.

## Consequence for the full form

For the bilateral tilt exp(ux)Phi(x), set M(u)=E_uX=L(u+1/2). The TWO-copy argument proves M''(u)<0 and M(u)−uM'(u)>0 for ALLu>0. In the coordinates of CONE001, for a>b>1,

    1<L(a)/L(b)<(a−1/2)/(b−1/2).

By the exact two-generator criterion, the matrix

    K_ij=[L(a_i)+L(a_j)]/(a_i+a_j−1)

is positive definite for distinct exponents a,b>1. It is the real FULL form, with ARCH, polar and ALL contacts, not an isolated positive component. The diagonal congruence of the exterior map keeps the sign for any real combination c1X^(−a)+c2X^(−b).

For a=b the matrix is positive semidefinite because both generators coincide; the nonzero represented function has strictly positive energy, while the redundant vector representing zero has zero energy.

## Difference and limit

The old a,b>=32 of CONE001§5 is superseded FOR PAIRS by all a,b>1. That result is kept as a historical antecedent, without editing it. The new proof uses the specific theta compact plus a conditional two-copy inequality; it does not presuppose positivity of the form nor use only generic logconcavity.

It does not prove three generators, matrices of all orders, the full linear envelope nor a new temporal window. The polynomial comparisons of five tilts of10343 are distinct obligations. The global sign remains OPEN.
