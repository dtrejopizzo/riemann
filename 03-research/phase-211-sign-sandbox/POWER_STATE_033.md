# State033 — Relative arithmetic bounds and finite grouping of coefficients

Status: partial results PROVED and audited; final conditions OPEN. Replaces STATE032. Goal active; papers untouched.

## Full comb with signed relative remainder

POWER_PRIME_BALANCE_033 proves for u>=63/2 and3<=N<=2u²/9−u/3+3/2 that the positive contact kernel k1 satisfies w(mq)<=m^-2w(q) for q>=5,m>=1. The dilation operator Df(q)=sum_(m>=2)f(mq) contracts this real class by rho=2389/3600<2/3.

Correctly subtracting the small divisors2,3,4 of logn gives a functional L on integers and the identity L(f)=A((I+D)f), where A is the real arithmetic tail q>=5. For odd K, the prefix S_K=sum_(j=0)^K(−1)^j L(D^jw) satisfies

    0<S_K<=A(w)<=S_K/(1−rho^(K+1)).

Also A(w)>=3600L(w)/5989. These are signed and uniform bounds, not arbitrary Möbius prefixes assumed positive. The error is relative to the comb or its prefix, NOT to the small residue of W. Adding ARCH, polar and contacts2,3,4 gives a full comparator, but its positive sign in a new range is not yet proved.

## Finite mixture preserving the form

POWER_COEFFICIENT_BALANCE_033 represents the gamma autocorrelation exactly as a finite mixture of Erlang profiles S_j=e^-ut sum_(r<=j)(ut)^r/r!, with weights w_Nj=a_Nj−a_N,j+1>=0. The linear functional keeps all contacts and the polar.

The premise that each component has a positive functional is false: for the single cutoff22 one proves −.01<L[S22]<−.006. Its Fourier transform takes a negative value, so S22 is NOT an admissible autocorrelation; it is not a counterexample to W. The loss of that individual component in the real mixture is bounded by .22/(N−1), without thereby controlling all the others.

A second Abel grouping gives nonnegative coefficients for T_m=sum_(j=1)^m jL[S_j]. Proving ALL T_m>=0 would suffice for row k0, but remains OPEN. It would not by itself close all k nor Paper47. The generating identity is kept as a description of the requirement, not as a sign proof.

## Evidence and scope

POWER_BALANCE_AUDIT_033 approves both memos. The identities, divisor boundaries, signs of remainders and scopes were reviewed, and both exact verifiers reproduced: PASS. No new N nor a campaign of cutoffs was certified.

There is no extension of W/T coverage in033. Rows1..5, the cone017, the single atom211,1 decided032, and the regions029 of increasing rates with their limits remain. The signed average031 and the new coefficient criterion still do not resolve the global obligation.

The next construction must prove a full positive comparison with these remainders or control the compensations of T_m; convergence of an approximation and positivity of its pieces are not equivalent to the total sign.
