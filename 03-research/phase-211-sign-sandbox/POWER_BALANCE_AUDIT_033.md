# POWER BALANCE AUDIT 033

Status: PRIME_BALANCE033 and COEFFICIENT_BALANCE033 APPROVED. Papers untouched.

## 1. Corpus and quantitative obligation

Consulted again the ROUTES-TRIED-INDEX index, master grid and crossword, entries 032 and antecedents 019–027. The single point of 032 has a margin of order 10^−15 after cancellation of components of order 1. Coarse componentwise bounds do not automatically become a uniform proof of that residue; this requires a joint inequality or adequate error control; it does not declare a route impossible because of difficulty.

## 2. Real contraction and signed comb — APPROVED

Reviewed `POWER_PRIME_BALANCE_033.md` and `tools/power_prime_balance_033_verify.py`; independent run PASS. REGION implies the frontier of 019 below ulog2, so w(q)>0 for all q≥2. RLOW is obtained from the recurrence and p_j>xp_(j−1), with case N3 included. The exact derivative DER and the sign of x²−R are kept. SLOPE increases with log q and at log5>8/5 reduces to the indicated polynomial inequality; REGION leaves 4u(u−63/2)+270>0. This proves the decay w(mq)≤m^−2w(q) for ALL q≥5 without a sweep over orders.

The operator D acts only on q≥5. The class DECAY is preserved under D and the sum of m^−2 is bounded by 2389/3600<2/3. The coefficient b(n)=log n−log2·1_(2|n)−log3·1_(3|n)−log2·1_(4|n) coincides exactly with Σ_(d|n,d≥5)Λ(d). Hence DIV relates the real tail A to L; uncorrected log n is not used, nor is w artificially extended by 0 below 5. The sums converge absolutely and Tonelli is legitimate.

The finite telescoping gives TEL with sign (−1)^K and remainder A(D^(K+1)w)≥0. CONTRACT controls it by ρ^(K+1)A(w)≤ρ^(K+1)L(w), justifying both ends of BRACKET and the opposite signs for K even/odd. FULL adds exactly ARCH, polar and contacts 2,3,4. It is a sufficient criterion with explicit signed error; its positive lower bound has not yet been proved in a new range.

The novelty relative to 019 and 032 is the contraction of a real gamma class that converts classical inversion into uniform one-sided brackets. It is not merely rewriting Euler. The error is relative to the comb, not to the residue W. That ρ^100<10^−17 shows a finite approximation scale, but proves neither the final inequality nor global computational efficiency. It does not increase W/T coverage.

Approved algebraic addition: L(w)=A(w)+A(Dw)≤(1+ρ)A(w), hence A(w)≥3600L(w)/5989. For K odd, S_K≥(1−ρ^(K+1))A(w)>0 gives the intrinsic bracket S_K≤A(w)≤S_K/(1−ρ^(K+1)). These bounds are incorporated into the full balance keeping B_N; none proves its sign without verifying the corresponding comparator.


## 3. Finite mixture and Abel — APPROVED

Reviewed `POWER_COEFFICIENT_BALANCE_033.md` and `tools/power_coefficient_balance_033_verify.py`; independent run PASS. The weights w_Nj=a_Nj−a_N,j+1=a_Nj j/(2d−j) are nonnegative and telescope to 1; interchanging finite sums reconstructs exactly rho_N. The linear extension of the functional is normalised with rho(0) and keeps ARCH, polar and the whole comb. It is not presupposed that each Erlang profile is an autocorrelation.

The ARCH formula for S22 follows from 032 with b_j=(u/2)^j. The rational polar term has the correct factor 2. The upper bound keeps only the negative contacts 2,3 and is therefore valid; the lower bound subtracts an absolute majorant of ALL q≥4 via the endpoint 4 plus the recurrent integral, applicable because 32log4>23. −.01<E22<−.006 is certified. The even transform at τ=u equals −1/(2048u), so the profile is not positive definite: this negative functional is not W negative on an admissible datum.

For N≥23, w_N,22≤22/d and the individual damage is larger than −11/(50d). It does not control the sum of all adverse components. The v_Nj=w_Nj/j have ratio 2(d−j)/(2d−j−1)≤1, with initial equality j1 and case d1 separated. Finite Abel gives exactly the nonnegative coefficients of T_m=ΣjE_j. The explicit profile and its generator z[E0(v)−vE0′(v)]/(1−z)^3 are correct in a convergent neighbourhood of the origin.

The condition ALL T_m≥0 would imply only the row k0, and remains OPEN. No sign of coefficients of a generator is obtained from its real positivity. Negative E22 does not refute the prefixes T_m. The novelty relative to 027 is the FINITE mixture with decreasing gamma weights and the weighted criterion compatible with them; Abel summation and Erlang are classical tools. That sufficient reduction is distinguished from a final inequality not yet proved.

## 4. Closure of scope and scale

The arithmetic contraction provides uniform effective brackets; Abel provides a finite reduction compatible with the real weights and a precise failure of componentwise positivity. No construction proves the final comparator positive in a new range. Against the margin of 032 of 10^−15, applying budgets of order-1 components or errors of 10^−3 is not enough: one must keep cancellation or pay a much smaller error. The relative hierarchy can reduce its error, but still requires the sign of its lower bound; this is neither a closure by difficulty nor a global NO-GO.

There is no new W sign, new row/window T or modification of papers. A second independent review of both memos and their verifiers agrees.
