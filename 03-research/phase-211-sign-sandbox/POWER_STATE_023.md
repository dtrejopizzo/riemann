# State023 — Compensated criterion refuted; positive cell weight

Status: identities and bounds PROVED; the universal pointwise auxiliary hypothesis FALSIFIED; global sign of W OPEN. Goal active. Papers untouched. Replaces STATE022 as the current summary.

## Two full proofs, without inferences from prefixes

POWER_INVERSE_INTERIOR_022 certifies −2/3<h128(1)<−33/50. POWER_CUMULATIVE_TEST_023 certifies −1/250<K129(1)<−1/251, where K=J+xh and J is the tail primitive of the full inverse. Both certificates include the WHOLE Möbius tail, bounded by10^-10. The reinforced verifiers were reproduced; the independent audits022/023 approve results and scope.

The second test was chosen in a targeted way: K128(1) was positive with small margin; only its neighbour129 was checked. Universal h>=0 and universal K>=0 are refuted. Neither of those signs decides the full pairing nor W.

## Arithmetic result that remains valid

POWER_CUMULATIVE_INVERSE_022 proves sum_(n>=1)J_N(n)=1 exactly via mu*1, with absolute Fubini. Its cell criterion K>=0 implies an explicit negative bound for ERR; it remains a valid implication, but its hypothesis does not hold for the whole family. Even if it held, the magnitude would have to be compared with ARCH_sharp to close W.

Without a sign condition one obtains ERR=-2 integral K_N(t) C_B(t)dt, with

    C_B(t)=-t^-2 integral_1^t x dB(x)>0 for t>1.

The weight is explicit, keeps the integer jumps, equals (1-t^-2)/2 between1 and2 and is >=(.75-log2)/2 for t>=2. Also integral K_N(t)floor(t)(floor(t)+1)/(2t²)dt=1. These identities do NOT make K positive.

The adverse contribution of K^- on[1,1+delta] is bounded by delta² sup K^- for delta<=1. It is a quantitative damping of the edge, not a bound on the total damage: the extent of the adverse region and its magnitude are missing. The proofs of the weight and of this inequality were reviewed; additional review recorded in POWER_CUMULATIVE_AUDIT_023.

## W coverage and next obligation

No new W entries: full rows N1,2,3, cone k>=10000N², eight arbitrary poles and fixed block12 remain. The scalar bridge017 requires ALL N,k; no new window T certified.

The continuation must control cell averages or the negative part weighted by C_B, instead of restarting an already refuted pointwise positivity. A favourable value at one point is not enough, nor is a mass identity without control of signs. The global objective remains active, without external blockage and without closure.
