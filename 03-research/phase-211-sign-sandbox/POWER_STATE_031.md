# State031 — Real alternation of blocks and initial global budget

Status: partial results PROVED and audited. Replaces STATE030. Goal active; global sign OPEN; papers untouched.

## Adverse prefix and recovery at fixed rate

POWER_WEIGHTED_BLOCK_031 keeps the representation W[g_N]/norm²=int G_N H of030. For fixed u=63/2 it proves:

    int_1^(225/64) G_N H <−3/1000, ALL N>=2^24;
    int_1^4 G_N H >3/200, ALL N>=2^22;
    int_(225/64)^4 G_N H >9/500, ALL N>=2^24.

The contacts2 and3 are included exactly. The contact4, located at the endpoint, has zero integral contribution there. The weighted primitive I_*(X)=int_1^X(3/2)x^-1/2H has a negative value at225/64 and a positive one at4. The rational certificates of those endpoints, combined with a uniform gamma error30u²/(2N−3), prove the full ranges in N; there is no campaign over orders.

This refutes the universal criterion I_*>=0 and shows a genuine quantitative recovery. No negative partial integral is a counterexample to total W. The complement from4 to infinity remains pending.

## Gamma factor with controlled variation

POWER_GAMMA_WEIGHT_031 studies R_N(t)=rho_N(t)−(2/3)rho_N'(t), so that G_N(x)=(3/2)x^-1/2R_N(logx). For ALL N>=2 at fixed rate, R starts at1, has a unique maximum T_N<2/3 and tends to0. With M2=u²/(2N−3),

    0<R_N(T_N)−1<=2M2/9,
    TV(R_N)<=1+4M2/9.

Uniqueness uses the logconcavity025; the localisation bound reuses Jensen026. A Riccati barrier proves q''<0 for q=−rho'/rho, which sharpens the overshoot. Everything refers to the real gamma function.

Integration by parts preserving ALL contacts gives

    W[g_N]/norm²=−int_0^infinito I_*(exp t)R_N'(t)dt
      >=int_(T_N)^infinito I_*(exp t)[−R_N'(t)]dt−M2.

The increasing branch ends before the first contact and its TOTAL adverse cost is<=M2, of order1/N. On the complement the weight−R_N' is positive, but I_* has real negative values: the sign of its weighted average remains open. This inequality quantifies one part of the global balance; it does not declare the rest resolved by changing representation.

## Evidence, coverage and continuation

POWER_WEIGHTED_AUDIT_031 approves both proofs. The texts were read, the identity and the variation inequalities reviewed, and the exact block verifier reproduced: PASS. The variation argument is analytic and needs no sweep over parameters.

The coverage of total W and the windows T are not extended. At u31.5 rows1..5 for all k and cone k>=10000N² remain; N>=6 below the cone remains. The regions029 with increasing u keep their separate scope and their specific bridge obstruction.

The next obligation is a signed arithmetic inequality for the average of I_* against the real gamma measure of the descending branch, or a different mechanism controlling all contacts. Enumerating other positive and negative blocks would not replace that obligation.
