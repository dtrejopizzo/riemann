# POWER_THETA_REMAINDER_AUDIT_077

Status: **APPROVED the assembly for the real Phi**, including the complete local verification. The compact certificate run 1589 finished exit0/PASS and its code and proof were audited line by line. The independent reproduction 36038 finished exit0/FULL PASS, with the same verifier hash. Papers untouched.

Index/grid/crossword and 073–076 were cross-checked, including the warning 074 about generic hypotheses. The audited implication is G_u(z)>0 for u,z>0 under R-HYP; the two local certificates detailed below now discharge that hypothesis for the real Phi. Neither a positive two-node kernel for G nor three generators of the original form is claimed.

The forcing equation is exact: beta c=a lambda, beta u−u²=lambda and J″=(xp−1)Phi give f=Phi[xp−1+lambda(tau−a)]. Both the integral of f and that of cosh(ux)f vanish by the boundary conditions and the zero mass of F. The second keeps the Neumann boundary condition at 0 and the superexponential boundary terms at infinity; no interface term is omitted.

R-HYP makes the derivative of B have at most one negative/positive change. The tail of B is positive and unbounded. The two vanishing moments exclude 0 or 1 sign changes: subtracting cosh at the single crossing would give an integral of strict sign. Therefore B has exactly two positive roots, both simple, with pattern +−+ and B(0)>0. A single-crossing forcing is not presupposed.

H(v)=v−sqrt(v²−1) is strictly convex for v>1. Its secant at the two nodes cosh(ub_i) leaves the error sign positive outside and negative inside; multiplying it by f gives a strictly positive integral. The secant is eliminated with the two moments. The singularity of H′ at 1 does not intervene: only the continuous H is integrated. The NEGATIVE sign of the Green function of D²−u² is correct and gives F(0)<0.

The anticausal representation has positive sign and satisfies the same equation. Its difference with F is homogeneous and superexponential, hence zero. Thus F is positive after the second root of f. The even extension of f has four simple zeros; the double exponential convolution does not increase the number of zeros counted with multiplicity. In this use only the upper bound of 065 is needed. The intermediates may have multiple zeros, but the general version of Rolle with multiplicities remains valid: the solutions are real analytic, without null intervals or zeros of infinite order, and the weighted boundary terms are kept. The preservation of polynomial moments of 065 is not improperly used for another datum.

Therefore F has at most four global zeros counting multiplicity. Parity, F(0)<0 and positive tail force exactly one simple positive zero: a second touch or a larger odd multiplicity would consume at least six global ones. The integral of cosh against F, subtracting its value at that crossing and using zero mass, is strictly positive. The factors of T_u and G_u are those of 076 and are positive for u,z>0.

The criterion LOCAL-HYP was also reviewed: J=xPhi/p−integral bPhi, b=(xq−p)/p², and −(wPhi)′=C Phi/p² are correct. The boundary condition wPhi->0 turns the denominator into the TOTAL mass of the positive tail. Thus R^−1 is the average of L=D/C; if L decreases strictly to 0, the average also decreases and is less than L(x), giving R increasing to infinity. That boundary condition and the integrability are not deduced from C>0 alone: they must be verified for the real Phi.

## Exterior and compact verification

POWER_THETA_RATIO_OUTER_077 resolves the signs on ALL x>=1 via rational first-mode identities and explicit payment of the WHOLE theta tail up to order 4. The proof was read independently, the numerators checked by symbolic expansion and the Fraction verifier reproduced with three PASS. The expansions without cancelling denominators and the cancelled ones are consistent. The boundary condition wPhi->0 and L->0 are also verified there with the real theta tail, not only with local signs.

Read in full POWER_THETA_RATIO_COMPACT_077 and tools/power_theta_local_077_verify.py. At the origin division by factors x³/x⁷ is avoided: the identity REG with P=p/x, Q=q, R=r/x, D=(Q−P)/x² and E=C/x³ is exact. V6<0, parity, a=V2(0)>0, b=V4(0)>0 and b<2a² imply V5<0, R′<0, D′<0 and P²+PQ−R>0; hence E>0 and L′<0 for 0<x<=1/16. It is not necessary that V4 remain positive on that whole range; R>0 already comes from 073.

The code generates Q0..Q8 exactly and adds to EACH derivative the complete tail from m=7. The bound A·3⁹m²⁰2^(−4m²) and its ratio <1/2 are correct. Machin, exp Taylor128 with eleven squarings and all interval operators round outward. The log-jet recurrence uses ordinary derivatives and correct binomial coefficients, without mixing factorial-normalized jets. S.lower>0 is checked before each division.

The Taylor2 model of V6 uses V6/V7 at the centre and V8 on the WHOLE panel; [0,h²/2] covers the remainder for both signs of the displacement. On the compact remainder, the binomial construction of jets of C up to order 3 requires V up to 6, available. The identities N′=(xq−p)C″−(r+xV4)C and N″=xrC″+(xq−p)C‴−(2V4+xV5)C−(r+xV4)C′ are exact. The models of C and N cover each whole panel; the sign is not deduced from central samples.

The corrected run 1589 finished exit0/PASS on 1024 origin panels and 8192 remainder panels. The meshes and domains were kept when replacing the first insufficient dependent evaluation by the justified Taylor model; the earlier FAILs were not promoted as false signs of V6. Verified SHA256 of the script that finished PASS:

    896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee.

The independent reproduction 36038 finished exit0/FULL PASS at the origin and on the remaining 8192 panels; the hash matches the original version. There are therefore two complete compact executions and the mathematical and code audit, in addition to the independent reproduction of the exterior proof.

## Current conclusion and limit

COMPACT and OUTER cover ALL x>0, give C>0, L′<0, L->0 and the required boundary conditions. R-HYP is discharged for the REAL Phi. Consequently, for ALL u>0, F_u=J−betaPhi_u has exactly one simple positive zero, negative sign before and positive after; for ALL u,z>0 one obtains T_u(z)>0 and G_u(z)>0.

It is pointwise REAL positivity of the regularized Schur remainder, not positivity of the two-node kernel of G. It does not prove three generators, all orders nor the global sign of W, nor a new time window. The next obligation remains to control the cross terms of that kernel or an additional property that dominates them.

## Anchored auxiliary corollary

Reviewed the addition from insight 048: N=M/u, B=(a/N−1)/u². N′<0 gives B>0 and 2B+uB′>0. The algebraic substitution in G is exact and its removable value at the pivot itself is −aB′/[B(2B+uB′)]. Since G_u(u)>0 by the already proved theorem, B′<0. Thus F=uB satisfies |uF′/F|<1, sufficient for ALL pairs of the kernel K_F; F′ is not required to have a fixed sign.

The Schur complement of the auxiliary node 0 is [uN(u)vN(v)/a]K_F(u,v), with K_M(0,0)=a and K_M(0,u)=N(u). All factors of the congruence are positive. This proves the anchored matrix {0,u,v}, for distinct positive u,v, without contradiction with the declared scope: 0 corresponds to the original exponent 1/2 and is not an admissible W datum in the class a>1. Three arbitrary positive generators or a positive kernel G are not obtained.
