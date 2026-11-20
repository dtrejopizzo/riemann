# Audit107 — compact mixed design

Status: **DESIGN AND LITERALS APPROVED; fixed run INCONCLUSIVE, independently reproduced.** Source:`POWER_MIXED_FOUR_COMPACT_DESIGN_107.md`. Consultations and difference relative to103–106 kept; papers untouched. PASS is not guaranteed.

## Origin and explicit payment of the remainder

The new disc lambda<=1/2 corresponds to|t|<3/4, with Rey>3/80. The absolute sum Phi<2^40 and the tail m>=129<2^-583 are valid; extracting even coefficients of the partial sum is equivalent to symmetrizing it, without pretending parity of the partial sum. The coefficient errors are added before the recurrences. The source fixes a single pointwise jet for a with compatibility check098; I1/I3 remain boxes103 and all their errors are propagated.

The integral formula for K was verified, including the factor(lambda²/2) integral s(1−s)²phi(s²lambda)ds. It produces|J|,|K|<2^42 on the disc. The recurrences J_k andK_k include the correct factors2k and2k(2k−1).

The pending payment of§8 is resolved explicitly: for N=513, the sum over n>=N of n4·2^-n is less than3N4·2^-N, withN4<2^37. Onlambda<=1/4, derivatives0..4 of the remainder ofJ/K of degree512 are less than2^(42+8+39−513)=2^-424. ForPhi the bound is2^-426. In Q=−phi−2lambda phi', Q^(j)=−(2j+1)phi^(j)−2lambda phi^(j+1), j<=3, the sum of costs is less than8·2^-426<2^-423. Hence2^-400 per entry comfortably covers all these analytic tails. It is ADDITIONAL to the coefficient error of modes and moments, which the arithmetic already propagates. The determinant is formed inlambda and an uncertain jet is not divided by t6.

## Remaining branch

The form A16 with power1/4 is exactly the A16 of106 with power5/4 after cancelling y+v=y(1+v/y); it does not change the target. Cap4 for integrals and cap5 for logTheta pay for derivatives0..3. The constant column allows the3x3 minor with positive sign. The fixed scales Yc are not differentiated.

The initial half-width1/16 enlarges the union of time discs to3/32; since this branch lies in[1/2,64], it remains inside S. Scales Yc/Y and their square are less than2, keeping the Gauss majorant of106. Error2^-81·32^j covers Gauss2^-83·32^j and the v/mode tails. ColumnX receives its separate local error. Factorials are paid before the determinant; node/weight balls and rounding are additional arithmetic costs.

## Coverage and execution

Deterministic left-first subdivision with fixed depth and maximal number of evaluations is legitimate: only a complete coverage by leaves with lower>0 certifies the interval. Exhausting the budget gives INCONCLUSIVE; a ball with upper<0 certifies only that cell of the mixed target, not a negative W. The algorithm must explicitly keep the pending cells so as not to confuse a partial stop with coverage.

The design is not sampling and does not authorize adjustments after signs. Review of the literal code is pending, including complete origin theta, quadrature and their errors before forming matrices, and exact accounting of leaves/budget. No new evaluation was run in this audit.

## Literals origin and REST/main

Read in full `tools/power_mixed_four_origin_branch_107.py` and `tools/power_mixed_four_compact_107_verify.py`. Their theta functions were neither executed nor imported. Only the local docstring of arb.legendre_p_root was consulted, confirming the required node/weight balls.

Origin: a via regularized E, compatibility098 and correct precision;128 modes/cap1025, even extraction512 and tail2^(k−583) BEFORE the recurrences. J/K are differentiated polynomials; Q uses the exact formula, entrytail2^-400, determinant of24 permutations. Left-first DFS has fixed limits and exact Fraction accounting of coverage1/4 before PASS.

REST:64 nodes per10 segments with positive weights and sum enclosing2. No midpoint removes errors of nodes/exp scalars; the exp cache factors exact identities. Cap5 ofTheta before logder controlsX up to3; cap4 of integrals and real positive branch correct. Gauss/v/mode errors are added to coefficients BEFORE factorials/determinant. Expansion along the constant column leaves a3x3 minor with sign+. Constant scales Yc are propagated as intervals. The recursion reports PASS only after resolving ALL leaves of the508 initial intervals, not on exhausting the budget.

Main requires origin PASS before REST; it aborts NEGATIVE orINCONCLUSIVE without promoting coverage. Importing the codes does not evaluate theta. Both literals approved before the run; a single process is run. A positive result is not guaranteed and modifying parameters after data is not authorized.

## Execution and reproduction without modifications

Runs 5594 and 46719 ended exit2/INCONCLUSIVE. Same11 evaluations,0 accepted leaves, depth10 and cell lambda[0,1/65536], determinant[+/−2.94e−3]. REST did not start. Separate logs saved. Hashes main2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054 andorigin15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553 verified identical.

The code behaved according to the design: it stopped without proclaiming partial coverage. An enclosure containing0 does not prove the opposite sign. The mathematics of the design remains valid, but the certificate did NOT decide the sign. It is not repeated by adjusting depth/precision and no global impossibility is inferred. There is no new W result nor mathematical obstruction.
