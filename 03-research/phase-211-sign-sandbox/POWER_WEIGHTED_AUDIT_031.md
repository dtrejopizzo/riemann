# POWER WEIGHTED AUDIT 031

Status: WEIGHTED_BLOCK031 and GAMMA_WEIGHT031 APPROVED. Papers untouched.

## 1. Corpus and difference

The audited antecedents 030 and the restrictions of the index/grid/crossword are kept: JOINT-G and step integration are identities; unweighted primitives of H already failed in 030. The required novelty is an inequality against the real G_N that keeps the arithmetic and compares losses with recoveries, not just another sign test of an abstract weight.

## 2. Weighted block and recovery — APPROVED

Checked `POWER_WEIGHTED_BLOCK_031.md` and `tools/power_weighted_block_031_verify.py`; independent run PASS. The formula for I*(X) incorporates all steps with factors −2Λ(q)/√q+2X^−3/2qΛ(q). If q=X its two terms cancel; contact 4 has no integral contribution at endpoint 4. Only q=2, q=3 contribute at the declared endpoints.

The general formula for J(X), with z=√X and arctan((z−1)/(z+1)), follows from the primitive verified in 030. The bounds for √2 and √3 and their reciprocals correctly keep the directions of the upper/lower evaluations. The exact intervals certify I*(225/64)<−.004 and I*(4)>.02.

The local gamma error satisfies |G_N−G*|<3M2 on [1,4], because log4<1.4 and (3/4)(1.4)²+1.4<3. The majorant of ∫|H|<10 includes length, constant, singularity and both contacts. Therefore the error 30M2 and the thresholds N≥2^22 and N≥2^24 are certified uniformly, without a sweep over orders.

The three REAL results at fixed u=31.5 are approved: prefix up to 225/64 <−.003 for N≥2^24; block up to 4 >.015 for N≥2^22; recovery between those endpoints >.018 for N≥2^24. The last is obtained by subtracting on the same function G_N, not by combining different models or truncations.

The negativity of the weighted prefix refutes universal I*≥0, but not W. The extended block shows real quantitative interior compensation and is distinct from repeating the unweighted primitives of 030. All of [4,infinity) remains to be controlled; it is not replaced by a tail of another representation and no new window T is certified.


## 3. Real gamma factor and initial cost — APPROVED

Checked `POWER_GAMMA_WEIGHT_031.md`. Strict log-concavity of D implies a unique maximum of R=e^−utD/(3/2), since the initial log-derivative is positive and its limit is −u. Reusing Jensen 026 with threshold u gives exactly t0=(2/3)d/(d+20), with ut0<d for d≥2. The case d=1 has the affine maximum 1/33. No new monotonicity assumption from the origin is introduced.

The global proof of q″<0 is valid: at every zero of q″, the Riccati equation and its derivative give q‴=2(q′)²+4qq′/t>0. The asymptotics q″<0 at infinity prevents a downward crossing from an earlier nonnegative value and excludes contacts. Concavity and q(0)=0 imply ∫_0^Tq≥Tq(T)/2.

On the increasing branch the parenthesis cq′−q−cq² is positive; hence replacing ρ≤1 before discarding −cq² keeps the direction of the bound on R′. Integration produces the overshoot ≤q(T)(c−T/2)≤M2T(c−T/2)≤2M2/9. The resulting TV keeps both real branches.

The global integration by parts has no boundary: I*(1)=0 and the gamma decay dominates its growth. The initial singularity is integrable. The increasing branch ends before log2, so it contains no prime contact. The upper bound of I* on that branch is <9/2, using the sign of c0−1 and the exact integral of the logarithm. Multiplied by the positive variation ≤2M2/9, it leaves an adverse cost ≤M2. BUDGET keeps the whole signed primitive against the positive weight −R′ of the remaining branch.

The indicated expectation criterion is sufficient but remains unproved. The positive weight is not turned into a sign of the average, because I* does have real losses. The difference relative to 030 is a quantitative control of the TOTAL variation of the gamma factor and of the cost of its initial branch, of order 1/N; not a new rewriting of IBP as a sign.

## 4. Closure

The round adds real compensation up to 4 and a global budget for the initial branch, both at fixed rate and without a campaign over orders. Neither adding them nor the positive measure of the descending branch automatically resolves all remaining contacts. There is no total sign of W, new complete row or certified window T. The negative results on primitives only delimit sufficient criteria, not a global impossibility. A second independent check agrees on the review of WEIGHTED_BLOCK031 and on the localization of the maximum via Jensen.

Final clarification on the increasing branch: also R′=cρq′−qR≤cq′−q because ρ≤1, q′>0 and R≥R(0)=1. This formulation, made explicit on request, directly keeps the direction of the overshoot bound and is approved.
