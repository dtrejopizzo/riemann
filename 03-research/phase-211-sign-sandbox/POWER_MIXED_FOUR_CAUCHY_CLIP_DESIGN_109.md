# POWER — Cauchy intersection of coefficients, design109

Status: RUN FINISHED exit2/INCONCLUSIVE because of the REST budget. Origin PASS16/16. No independent reproduction of109. 107 and108 are not modified.

## 1. Difference and antecedent

The consultation of the project rules, ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID and CROSSWORD-TO-D for the mixed object104–108 is kept.107 ended INCONCLUSIVE when evaluating separate entries.108 preserved lambda by first forming the polynomial determinant, but the run and its reproduction ended INCONCLUSIVE after15 evaluations,4 accepted cells, coverage141/8192; failed cell[141/8192,1129/65536], depth10. The remaining branch was not executed. It is an enclosure failure and not a negative sign.

109 adds ALREADY PROVED analytic information on coefficients, with no new points nor theta parameters. The run will repeat the intact107 builder to recover its coefficients; that repetition has not yet been executed. It is not claimed that the excess width has a single cause, nor is PASS guaranteed. The change is to intersect the base coefficient balls with their Cauchy bounds before differentiating and multiplying.

## 2. Bounds and exact operation

The complete functions are holomorphic in a neighbourhood of |lambda|<=1/2 and satisfy, by107,

 |phi(lambda)|<2^40, |J(lambda)|<2^42, |K(lambda)|<2^42.

By Cauchy, their true coefficients satisfy for all k>=0

 |phi_k|<=2^(40+k), |J_k|<=2^(42+k), |K_k|<=2^(42+k).

After building the BASE coefficient balls of degree512 with the107 builder, including the errors of modes, moments103 and a, intersect each with the corresponding symmetric real interval. The intersection contains the true coefficient because BOTH enclosures contain it. Do not choose a point or a central value instead of the intersection. If the intersection is empty, abort with status BUG/INCONCLUSIVE, never continue nor adjust a bound.

Rebuild all derivatives from these intersected bases. Build Q=-phi-2lambda phi' and its derivatives from the same intersected phi. Intermediate results are not arbitrarily intersected with an unproved bound. The coefficients of J and K may be intersected separately: no correlation between their errors is required or assumed.

## 3. Budget and correction unchanged

Reuse108: complete determinant of24 permutations as an interval polynomial, all degrees up to2048, Taylor shift to the rational centre of each cell and loss sum_(j>=1)|b_j|h^j. Keep the independent correction2^-200 of the determinant due to the tails of the functions. The intersection only narrows enclosures of the same true coefficients; it does not alter that proof.

Keep all precisions, modes, caps, domains, initial partitions, depth10, maximum8192 evaluations per branch and acceptance criterion of107/108. The Gauss remainder of107 stays intact and is executed only if the origin passes. Parameters are not changed nor chosen according to observed signs. The new wrapper checks hashes of reused sources before computing.

## 4. Pending items and scope

Independent mathematical and literal audit pending before executing109. The wrapper is implemented without modifying the107/108 code. An INCONCLUSIVE result remains legitimate. This operation does not prove a sign by itself, adds no W coverage and does not alter the mixed obligation. Its specific object is to exploit a uniform Cauchy enclosure of coefficients that107/108 did not yet impose on the interval representation.

## 5. Historical status during execution, before the final result

After independent mathematical and literal approval before data, run52183 was started. Log:`tools/power_mixed_four_cauchy_109_root.log`; driver hash c3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba. Complete Cauchy origin PASS16/16 in lambda[0,1/4]. The REST branch is still active with subdivision and the fixed budgets of107. NO FULLPASS nor independent reproduction announced.

Arb printouts of REST leaves may show coarse decimal forms[+/−...] despite the binary predicate value>0; the acceptance test is the interval predicate, not inferring zeros from the decimal format. Codes/parameters are not modified and no replica is launched before the run result. This status is provisional, with no record of global sign in the indices until the real exit.

## 6. Final result of run109

Run52183 ended exit2/INCONCLUSIVE because of the fixed budget of8192 REST evaluations, with4113 accepted leaves. The origin passed16/16 cells lambda[0,1/4]. The next pending REST cell was[2645/512,1323/256], depth6; it was not evaluated after the budget was exhausted. It was neither a negative-sign cell nor a stop by depth.

Audit of the LOG, without a new run: the4113 accepted leaves are contiguous and cover exactly REST[1/2,2645/512], length2389/512. The rest of[1/2,64] was not certified by this run. The log is in`tools/power_mixed_four_cauchy_109_root.log`, with driver hash c3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba and hashes107/108 intact. NO independent reproduction of109 is claimed.

Final result INCONCLUSIVE, without FULLPASS,Cheb4 global,finite U,W/T/all orders nor mathematical obstruction. The precondition of110(109 without FULLPASS) is met, but another literal must be audited before executing that representation. The parameters of109 are not modified and that run is not restarted.
