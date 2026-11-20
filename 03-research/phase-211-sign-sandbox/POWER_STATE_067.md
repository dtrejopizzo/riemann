# POWER_STATE_067 — The positive Selberg term is essential in case129

Status: **PROVED/APPROVED**, source POWER_SELBERG_DROP_OBSTRUCTION_067.md and audit POWER_SELBERG_DROP_AUDIT_067.md; a further review also approved. No new N, cutoff, precision or campaign. Papers untouched.

## Result and difference

`POWER_SELBERG_DROP_OBSTRUCTION_067.md`, `POWER_SELBERG_DROP_AUDIT_067.md` and `POWER_STATE_067.md`: two independent reviews, without new computations or otherN. For the SAME gamma129,u=63/2 of061, Selberg gives S=U−V and W/norm²=ARCH/norm²+polar/norm²−2U+2V. The pair2·2 and the real mixture030/Jensen prove2V>1/243. Since061 certified0<W/norm²<1.35·10^(−10), the criterion that discards2V has value<−1/250. Even retaining only1−theta of2V requires theta<6561/(2·10^11); theta=10^(−7) already leaves that candidate negative.

Explicit difference relative to055/023: the Selberg identity and V>=0 are not offered again as progress.055 left open the falsity of the strong criterion W/norm²>=2V; the later full certificate061 now refutes it on an already existing test. It is an obstruction to that isolated positive loss, not to full Selberg, compensated methods or the sign of W. No new row, windowT or global conclusion. Retrospective note incorporated into STATE055; papers untouched.

## Obligation that remains

The test129 keeps the certified positive sign061. No comparison of U and V uniform in N nor a new bound of the interior was obtained. A next estimate must preserve their compensation: the individual positivity of V does not authorise discarding it without paying a loss larger than the full margin. The relative precision indicated concerns only the isolated loss in this same decomposition, it does not impose such precision on every possible proof.

## Query068 — exact regrouping and Gaussian alternative

The regrouping by prime support was verified via insight048 and a further check. For m=p^a, a>=1, the coefficients of μ*log² and Λ*Λ are, respectively, (2a−1)log²p and (a−1)log²p. For m=p^a q^b with p different from q and a,b>=1, both are 2logp logq. For m with at least three distinct primes, both are zero. Hence keeping the cancellation at fixed m returns exactly Λ(m)logm and, after dividing by logm, reconstructs S. No new inequality nor additional favourable contact appears.

The attempt to introduce cross terms between distinct contacts did not produce a new bound either: for decreasing gamma rho, rho(log(a/b))−rho(log(ab))>=0 when a,b>=1. This kernel comparison only gives the upper orientation corresponding to replacing products by correlations; it does not estimate the compensation with ARCH. The infinite contact operator is not assumed bounded without sufficient damping. The change to products rho(loga)rho(logb) reproduces the comparisons already examined025/055. Query deduplicated, not a NO-GO for every cross comparison.

The possible universal lower bound of the Gaussian functional G_W(v), defined by the autocorrelation exp(−v t²), was also audited by cases. Neither a proof nor a falsifier of G_W(v)>=0 for ALL v>0 was found: it remains OPEN. INTERIOR_CONSTRAINT027§4 keeps all the pieces and §5 refutes only global convexity; GAMMA_BALANCE030§4 proves a particular value, not all parameters. The earlier Gaussian route E101_038§6 does not supply a universal positivity available for transfer either.

The mixture rho_N(t)=E exp(−Vt²), V=(u²/4)/G and G with law Gamma(N−1/2,1), would transfer such a lower bound to the whole row k=0. The mixture also exists for N=1; it does not need the mean EV, which is only used in Jensen for N>=2. For u>1/2 the piecewise interchanges remain finite, including the polar: its Gaussian average is proportional to E[sqrt(G)exp(G/(4u²))], finite since 1/(4u²)<1. ARCH is controlled by the temporal representation, with (1−rho_1(t))/t bounded near0, and the comb by absolute convergence. That transfer is not extended to k>0 nor is the missing lower bound G_W obtained.

These diagnoses avoid relaunching the same identities as sign tools. There were no new numerical cases, new theorem for the indices nor changes to the papers.
