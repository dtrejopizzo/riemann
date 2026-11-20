# POWER_CONFLUENT_THIRTEEN_AUDIT_052

Status: **APPROVED** POWER_CONFLUENT_THIRTEEN_052, including its script and algebraic proof. Papers untouched.

The index/grid/crossword antecedents on Schur, BLOCK007, ZERO13 of FULL_TWELVE050 and discussion051 were cross-checked. The new case is motivated by the single direction left open by ZERO13: the complete confluent blockV13 is decided, with its crossings and the whole arithmetic tail. No sign is attributed to the complement via an abstract identity.

Read in full power_confluent_thirteen_052_verify.py and reproduced independently with python3: **five PASS messages, exit0**. The interval bandsE2/E23 keep the normalizations of007/048; the LDL13 verify E2>3/10000 and E23>7/25000 against the original orthonormal norm, paying the operator error<10^−10 againstI.

For the Schur complement, h_j=(−1)^j has norm²13; C_i=e_i−(−1)^i e12 satisfies Cᵀh=0 and has nontrivial Gram. The code uses A=CᵀTC, g=CᵀTh, delta=hᵀTh and S=(delta−gᵀA^−1g)/13. The LDL solves the system exactly without inverting interval entries. The comparison between centersT±epsilonI is valid because the minimum on the affine set h+range(C) is monotone in the order of forms. This correctly incorporates the Gram and the simultaneous variation of diagonal, coupling and inverse. The certified bounds are S_E2 in(.0004054,.0004055), S_E23 in(.0003834,.0003836), and S_W in(.0003,.0005).

The components are evaluated with intervals at the FIXED VECTOR x=h−CA_center^−1g_center: one computes xᵀT_component x/13. They are not Rayleigh quotients by norm²x nor components of the unknown exact minimizer. This normalization represents the unit coefficient of the complement h/sqrt13. In that fixed central direction AP lies in(.01839,.01841), contact2 in(−.018,−.01798), and contact3 is negative. Hence3 worsens the pivot here; it is not claimed that it rescues the sign nor that the arithmetic is monotone.

The tail from4 extends argument007 up to band12: signs of coefficients shifted by40 certified exactly, log4>4/3 for monotonicity and log4<7/5 for the sum-integral comparison with positive coefficients. The row majorant is<1/100000 and covers ALL integers from4, without truncating prime powers nor presupposing their signs. Hence W>(7/25000−1/100000)norm²>norm²/4000 on confluentV13. That tail is not transported to thirteen arbitrary poles.

Finally read the complete memo of six sections: it makes explicit the non-unitary normalization of the components, separates the central minimizer from the exact pivot and distinguishes keeping3 to improve the budget from claiming a favorable sign of3. Its confluent scope and the additional obligation for thirteen arbitrary poles are correct. The diagnostic decimal figures are not used as proof.
