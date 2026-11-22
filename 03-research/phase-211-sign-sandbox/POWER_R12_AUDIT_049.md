# POWER_R12_AUDIT_049 — Effective cut and first restricted transport

Status: **APPROVED** CENTERED_CUTOFF049 and R12_TRANSPORT049. Solves R12 for the first movement from V12, with c=1/2500. Does not certify full W nor iteration. Papers untouched.

Antecedents cross-checked: index/crossword, PRIME_TRANSFER014 and audit, GEOMETRIC_TRANSFER015, QUADRATIC017, BLOCK007 and ENDPOINT048. The restricted hypothesis was still OPEN. The effective difference is an analytic cut uniform in all numerators, followed by the exhaustive certificate of the only thirteen remaining indices. The universal falsifier of huge order is not used to discard this restriction.

## Analytic cut

The transformation z=exp(2ix), y=sin x and the centring exp(−11ix) are exact, even for complex coefficients. The sectors cos x R(y), S(y) have opposite parities and degrees10/11; their cross terms integrate to zero both in norm and in inverse moment. The Jacobian gives precisely exponents j+1/2 and j−1/2. The total ratio is a positive mixture of the sector ratios.

The two integrations by parts were reviewed: the symmetric polynomial operator has eigenvalues n(n+2a+1), and the boundary terms of both formulas vanish under a>0. Hence 2ar<=1+2sqrt(rD). The normalised coefficients decrease in j; the sector of degree10 is dominated by that of degree11. For every j>=14 one gets27r<=1+2sqrt(429r). The check16129/400>0 places its positive root below49/20. Hence E(tau^−2)<1/405 uniformly, without an asymptotic dimension hypothesis.

The global digamma lower bound used exists with explicit proof in Paper46, main.tex:505, lem:mbounds(ii): integration by parts of the kernel g with g'>0 and total variation1/2. Jensen and Cauchy have the correct orientation and give ARCH>859/800. Contact2 costs less than one norm² and the effective polar048 costs at most3(9/62)^j. This exceeds1/2500 for the whole tail j>=14.

## Finite certificate

power_r12_finite_segment_049_verify.py was read in full and reproduced independently with python3: **PASS for the thirteen blocks1,...,13**, exit0. The extension of007 uses bands0..24, power sums2..25 and the same explicit rational remainders. They suffice for the images of ambient dimension12+j<=25. C_j reproduces exactly the coefficients of(1+z)^j; omitting2^−j does not alter the sign. The operator error<10^−8 is paid against C_jᵀC_j, not against the identity of the original coordinates. The rational LDLs verify all cross terms and all pivots. No floating eigenvalues are used.

## Mixture and scope

For each finite v>=u, r=1−u²/v² belongs to[0,1). The density identity is |G_v|²=(1−r)sum r^j|Q^(j+1)F|². ARCH and contact2 are summed by absolute convergence; the strong norms of015 bound uniformly the energies of the orbit. The multiplier Q is a contraction in unweighted Sobolev and in exponential L² with eta between1/2 and u/2. The polar is verified separately by the exact scalar series (1−r)sum r^j(−1/3968)^(j+1)=−1/(4v²−1). No uniformity is needed as v tends to infinity.

Each term of the mixture of E2−c norm² is positive, including j=1..13 and the whole tail. Thus R12 holds for all finite v>=u from the EXACT base V12, at c=1/2500, also below the base margin007. The case v=u is r=0. The gain does not include the other contacts: their bound007 has not been transported. Nor is the hypothesis on intermediate bases automatically preserved when moving a second pole. The scope declared in R12_TRANSPORT049 is correct.
