# State025 — Full integrated arithmetic balance in the adverse case129

Status: audited partial results PROVED; global sign of W OPEN. Goal active. Papers untouched. Replaces STATE023 as the current summary and incorporates024/025.

## Full signed progress

POWER_INVERSE_LOGCONCAVITY_025 proves ERR129<−33/50 for u31.5, with ALL integers of the Möbius inversion and the WHOLE half-line. This is the same N129 where K129(1)<0 was certified023. Pointwise positivity fails, but does not prevent this integrated control.

The proved chain has three independent steps:

1. POWER_CELL_TEST_024 certifies the first full cell: S129(2)>33/100, with Möbius tail<10^-10 and exact polynomial antiderivative. It also certifies integral_1^2 K C_B>31/100 and a positive weighted mass. These are distinct representations of the same balance and are NOT added to each other.
2. The coefficient ratios (j+1)c_(j+1)/c_j of D_N=33P_N−P_N' decrease for ALL N. Elementary covariance implies that D_N'/D_N decreases. A single rational check D129'(2/3)<30D129(2/3) controls all shifts logm and the FULL Möbius sum: K129(x)>0 for x>=2.
3. The primitive J129/x decreases on that half-line and is positive. All cells n>=3 have S129(n)>0, analytically, without enumeration. ERR=−2sumS and the first step give ERR129<−.66.

The proofs were read, the ratios verified independently and the Fraction certificates executed. POWER_CELL_AUDIT_024 and POWER_INVERSE_LOGCONCAVITY_AUDIT_025 approve the full chain. No floating-point quadrature was used for these results.

## Uniform lemma and scope

POWER_CELL_BALANCE_024 provides a cell budget that tolerates negative K: S_n=b_nJ(n)+(H_(n−1)/2)integral_cell[1−(n−1)²/t²]K(t)dt, b_n>=.75−log2. From it follows S_n>=b_nJ(n)−H_(n−1)sup_cellK^-/(2n). It is an effective bound, not the claim that its favourable term dominates for all N,n.

The logconcavity025 holds for ALL N and can be reused to reduce a half-line to a ratio check. The check t0=2/3 and the full balance are certified only for N129; they are not extrapolated to the whole table.

## Exact limit relative to the objective

W[g129]/||g129||²=ARCH_sharp[g129]/||g129||²−ERR129. A quantitative comparison of the archimedean deficit with the proved benefit is missing: ERR<−.66 is not declared sufficient. This round adds no sign of W and no new window T.

The earlier coverage of W remains: rows N1,2,3 for all k, cone k>=10000N², eight arbitrary poles and fixed block12. The scalar bridge017 requires completing ALL N,k. The auxiliary counterexamples022/023 remain valid; their pointwise hypothesis was overcome in this case by integration, without erasing the adverse regions.

## Continuation

Look for a joint balance with ARCH_sharp that keeps cancellations and an analytic extension of the integrated mechanism to variable orders. Do not turn the ERR result into positivity of W, do not relaunch the already refuted universal K>=0 and do not replace the universal step by a campaign of isolated certificates. Goal active, without global closure or external blockage.
