# Proposal: mixture cases with cancellation

Status: OPEN, supported by a PROVED case. Three independent reviews and coordination. Papers untouched.

## Result

POWER_CONE_001 proves exterior positivity on each plane of two powers X^{-a},X^{-b}, a,b>=32, with arbitrary real coefficients. It does not prove positivity on their envelope nor PW_N admissibility. Proof independently reviewed.

## Novelty

We did not find the specific lemma a>=32 in targeted searches of the corpus, index, grid and crossword. The general Pick family and matrix elimination have antecedents: NO claim is made of a never-attempted global route. Some seed indices are outdated relative to later phases. The concrete difference is the positive case with explicit constant and the falsifier of the step from diagonals to mixtures.

## Next mathematical experiment

Define u_i=a_i-1/2, K_ij=(L(a_i)+L(a_j))/(u_i+u_j), r_ij=K_ij/sqrt(K_ii K_jj), with L real and explicit in POWER_CONE_001. The first goal is to prove or refute, for a_i=A+(i-1)h, A>=32,h>0,

    (r_23-r_12 r_13)^2 <= (1-r_12^2)(1-r_13^2).   (P3)

It is exactly the three-point determinant. Investigate small h via derivatives of L, then h=A and then general h. Look for sign remainders in the real series of digamma and Σ Lambda(n)n^{-a}, keeping cancellations. If it fails, extract a negative vector: it would only be an exterior counterexample; verify admissibility before attributing consequences to the paper.

If it is proved, continue with unequal triples and four generators. The goal would be a uniform rule controlling the residues after eliminating a generator. Elimination is known; the arithmetic inequality that would preserve the sign is NOT constructed. Do not extrapolate finite cases to all orders.

Second independent requirement: bridge to the admissible tails PW_N modulo gauge in the NORM OF THE FORM. L² density alone does not suffice. Without all orders and that bridge there is no closure.

## Falsifiers and decision

H(u)=3+cosh u is positive, even and log-convex, but the kernel at log2,2log2 has value -129/(34 log2) on (42,-41). This refutes the generic theta argument, not the arithmetic datum.

NEAR_CASES_RESULTS_2026_11_04 documents an auxiliary nearfree improvement and refutes monotonicity when adding contacts and the supposed automatic favorable contribution of the cycle (2,2,4). It does not refute the total sign.

I recommend the ladder of powers as a new experiment in its details because it already produces a theorem and an exact obstruction. There is not enough evidence to call it a closure mechanism; the global sign remains open.
