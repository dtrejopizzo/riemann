# POWER_SELBERG_DROP_OBSTRUCTION_067 — The positive Selberg term cannot be discarded in case129

Status: **PROVED/APPROVED**, independent review in POWER_SELBERG_DROP_AUDIT_067.md. Obstruction to the specific criterion of055; NOT a counterexample to the sign of W. Papers untouched. No new N, cut nor numerical campaign.

## 1. Antecedents and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked ROUND_023_A§2.1, POWER_STATE_055, POWER_GAMMA_BALANCE_030 and POWER_GAMMA_129_DECISION_061 with its audit.055 already established the full Selberg identity and warned that discarding its positive term requires a criterion stronger than W>=0, but explicitly left open the falsity of that criterion. Now061 decides W of the SAME gamma test129 with a tiny margin. That later datum allows refuting the concrete premise, without fabricating another test nor presenting the Selberg identity again as novelty.

## 2. Normalization and exact criterion

Fix u=63/2, N=129 and g(t)=t^(N−1)e^(−ut)/(N−1)! for t>0, zero for t<0. Write c0=||g||² and rho(t)=c_g(t)/c0. Define the real scalar sums

    S=Σ_(m>=2) Λ(m)m^(−1/2)rho(logm),
    U=Σ_(m>=2) (μ*log²)(m)m^(−1/2)rho(logm)/logm,
    V=Σ_(m>=2) (Λ*Λ)(m)m^(−1/2)rho(logm)/logm.

All converge absolutely: rho(t) is e^(−ut) times a fixed polynomial of degree128, and it suffices to bound in absolute value each coefficient of μ*log² and Λ*Λ by m log²m, counting at most m divisors and bounding each summand by log²m. The factor m^(−u−1/2)=m^(-32) then ensures convergence even with that coarse majorant. The convolution identity

    Λ·log + Λ*Λ = μ*log²

implies exactly S=U−V and hence

    W[g]/c0 = ARCH[g]/c0 + POLAR[g]/c0 −2U+2V.       (FULL)

A squared causal operator is not identified with a norm. This equality of absolutely convergent sums suffices. Since g>=0, rho>0 and V>=0. The criterion that would discard2V is

    ARCH[g]/c0 + POLAR[g]/c0 −2U >=0,

that is, W[g]/c0>=2V. It is proved that this criterion is false here.

## 3. Independent lower bound of the positive term

The only divisor pair2·2 gives (Λ*Λ)(4)=(log2)². By positivity of all summands,

    V >= (log2)/4 ·rho(log4).                       (PAIR)

The real mixture030, valid for N>=2, writes rho(t)=E exp(−Zt²), with Z=(u²/4)/G and G with law Gamma(N−1/2,1). Its mean is

    EZ=u²/[4(N−3/2)]=3969/2040<2.

Jensen for the convex function z↦exp(−zt²) gives rho(t)>=exp(−EZ·t²). Since log4<7/5,

    EZ·(log4)² <2·49/25=98/25<4.

With e<3 one obtains rho(log4)>exp(−4)>1/81. Moreover log2>2/3. Thus

    2V >= (log2)/2 ·rho(log4) >1/243.               (GAIN)

These are strict elementary inequalities; no new sum of contacts is evaluated.

## 4. Falsifier of the discard criterion

DECISION061, a full rational certificate with all contacts, establishes

    0<W[g]/c0<1.35·10^(−10)=27/(2·10^11).

Using this upper bound and GAIN in FULL gives

    ARCH[g]/c0+POLAR[g]/c0−2U
       =W[g]/c0−2V
       <27/(2·10^11)−1/243 <−1/250.                (FAIL-DROP)

The last comparison is rational: 1/243−1/250=7/60750>27/(2·10^11). The positive Selberg term is essential for this criterion even in a test whose full form is already certified positive.

## 5. Calibration of an isolated partial loss

More generally, retaining only the fraction1−theta of the contribution2V produces the candidate lower bound W[g]/c0−2theta V. For0<=theta<=1, if that candidate were nonnegative, necessarily

    theta <= (W[g]/c0)/(2V)
          < [27/(2·10^11)]·243
          =6561/(2·10^11)=3.2805·10^(−8).

In particular, discarding even the fraction theta=10^(−7) already makes that candidate negative. This necessary relative precision refers only to losing an isolated fraction of the positive term in THIS decomposition and THIS test. It does not exclude another organization of Selberg nor a joint compensated estimate.

## 6. Scope

Only the sufficient strategy of suppressing2V and proving positivity of what remains, applied to the existing real case129, is refuted. Neither the Selberg identity, nor the possibility of comparing U and V while keeping their cancellation, nor the sign of W is refuted. Nor is propagation in N, a new row, time window or global conclusion obtained. The useful datum for a next comparison is quantitative: the gain one tried to discard exceeds1/243, while W/c0 is less than1.35·10^(−10). Correlated intervals are not separated to recertify that margin; the approved certificate061 is used directly.
