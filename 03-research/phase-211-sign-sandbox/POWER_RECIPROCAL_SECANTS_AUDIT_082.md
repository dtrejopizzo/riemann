# POWER_RECIPROCAL_SECANTS_AUDIT_082 — Independent audit

Status: **APPROVED / PROVED as an algebraic criterion.** Source `POWER_RECIPROCAL_SECANTS_082.md`, read in full. The identities were verified independently twice. Papers untouched.

## Checks

DET2 and RECIPROCAL were reproduced by exact rational simplification. DET3 follows from DET079 already reproduced in079 and the RECIPROCAL identity; the cancellation of (u+w)² through (w²−u²)² produces exactly the printed Vandermonde, with no pending factor.

For PD pairs, the product of the two secants R,S is positive. Its factors cannot both be negative: R2<R1 and x2/R2<x1/R1 would be incompatible with x2>x1. Thus both secants are strictly positive, beta>0 and alpha>0. Neither increasing F nor alpha>beta uv is needed.

The RECIPROCAL formula has numerator alpha beta(w²−u²)−delta_R(alpha w²+beta u²v²). If delta_R<=0, delta_S>0. In particular the nonnegative product delta_R delta_S is equivalent to both differences being nonnegative: the case of both negative is not erroneously admitted. The same reasoning covers the case delta_S<0 by symmetry. PD pairs and positive diagonals turn the sign of the determinant3 into PSD/PD by Schur2x2.

The boundaries delta_R=0 or delta_S=0 are rank2; they cannot vanish simultaneously under strict pairs. Repeated nodes and vectors representing the zero function are separated correctly. The equivalence for all triples is exactly concavity of R and S on the interval of squares, without requiring differentiability. The congruence F↔1/F and the recovery of079 are correct: for M, R''=g''/a and S''=[u²M''+uM'−M]/(4u³)<0 by073.

## Novelty and scope

Consulted the antecedents003/074/079/081 and the three records. One switches from BASE073, which081 shows is not hereditary for the REAL remainder, to a reciprocal criterion that allows decreasing functions. It is a necessary and sufficient condition of order3 in the class of PD pairs; not a proof of its hypotheses for G_p.

For the remainder G_p one must still prove PD pairs and both concavities, and any subsequent preservation remains open.077 only gives positive values. No claim is made of order4, all orders, compact discharge080, new W coverage or a time window.081 remains valid for its limited class.
