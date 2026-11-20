# POWER_STATE_074 — The probabilistic hypothesis073 does not automatically extend to three

Status: **PROVED/APPROVED** for the auxiliary counterexample; global sign OPEN. Papers untouched.

## Result and difference

Source [POWER_TWO_COPY_SCOPE_074.md](POWER_TWO_COPY_SCOPE_074.md), audit [POWER_TWO_COPY_SCOPE_AUDIT_074.md](POWER_TWO_COPY_SCOPE_AUDIT_074.md). The rational verifier was reproduced three times independently with exit0/PASS.

The explicit potential

    V(x)=A[x²/2+x^(2p)/(2p·2^(2p-2))],
    p=1000000, A=400000000,

is even, polynomial, strongly convex, superlinear and satisfies V'''(x)>0 for ALL x>0. By073, its tilted mean M satisfies M''<0 and M-uM'>0; ALL distinct positive pairs of the kernel K(u,v)=(M(u)+M(v))/(u+v) are positive definite.

However, at the three nodes A,2A,3A, the vector c=(40,-40,3) satisfies

    c^T K c < -53111/(10000 A)<0.

The proof controls modes and means by strong convexity and integration by parts, not by a saddle-point approximation without error. The means lie within1/10000 of(1,2,2); the limiting rational matrix gives c^T B0 c=-6 and the quadratic error is less than6889/10000. There is no quadrature, sweep over potentials nor campaign over nodes.

The difference relative to SCHUR003 is keeping EXACTLY the whole strong potential hypothesis073. The earlier auxiliaries did not satisfy it. The prescribed investigation of V=x^6 gave a first positive coalescent determinant, proved with exact gamma moments; it was not presented as a counterexample nor was a sign searched for by a campaign.

## What remains proved for the real datum

073 remains intact: for the REAL theta kernel, the hazard compact is certified, M''<0 and M-uM'>0 for ALL u>0, and the FULL form is positive on ALL planes of two powers with exponents a,b>1, including polar and all contacts. Distinct exponents give a positive definite matrix; coinciding exponents give semidefiniteness by redundancy and positive energy only for the nonzero represented function.

074 is not a counterexample to real Phi nor to W. It neither adds nor removes a sign region of W, nor a window T. To advance to three real generators an additional specific property of Phi or a quantitative comparison of its cross term is needed.

## Quantitative local obligation, NOT a proved estimate

For the REAL M of073 and some u>0, set

    r=uM'(u)/M(u), t=-u²M''(u)/M(u).

073 provides0<r<1 and t>0. The first jet of three coalescent nodes would further require

    t <= (1-r)(1+2r).                                  (OPEN-JET)

It is the local condition already associated with the first transform of SCHUR003§4, written with these variables. To make the scope precise, the matrix of Taylor coefficients of K around(u,u), with indices0,1,2 and division by the respective factorials, has determinant

    M(u)^3/(64u^9) ·(1-r+t)·[(1-r)(1+2r)-t].

Since1-r+t>0, a nonnegative local determinant requires OPEN-JET. This formula is an algebraic identification of the obligation, not a proof of its sign for Phi. Concavity of M only knows the sign of the two-copy covariance; control of its MAGNITUDE is missing. Nor would proving this pointwise jet replace the global comparison between three distinct nodes. No other identity memo is created and that obligation is not declared resolved.
