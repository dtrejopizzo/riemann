# POWER ROWS AUDIT 028

Status: ROW_FOUR028 and ROW_SPLIT028 (N5) APPROVED. Papers untouched.

## Full row N4 — APPROVED

Reviewed `POWER_ROW_FOUR_028.md` and `tools/power_row_four_028_verify.py`; independent run PASS. The base norm5/(32u^7) and the recurrence of integrals produce A4=d−ud′+(2u²/5)d″−(u³/15)d‴. The polygamma series give exactly the three negative terms with factors u/2,u²/5,u³/20. The integral remainder on the tail from116 is correctly bounded by the integral from115. The rational endpoint A4(u0)>11/400 is certified.

The two ARCH monotonicities are legitimate: the law in ξ=τ/u is independent of u and m(uξ) increases with u; increasing k reweights by ξ²/(1+ξ²), increasing in |ξ|. Thus the endpoint u0,k0 extends the bound to all u≥31.5,k≥0. This does not use pole motion of the full form.

WR4 eta12 keeps eta<u/2. Its generating series has positive coefficients and both arguments decrease with u; R4<400 at the endpoint controls all parameters. The comb bound includes the whole von Mangoldt sum, with the factor2sqrt R<40 and the decreasing integral of(log x)x^−12. The substitution2^−1/2<5/7 and the endpoint log2<.7 give loss<.006.

The beta norm and the alternating polar are correct. The bound c_k≥2^−k and binom(k+3,3)≤4^k give the geometric ratio8q_u; p40 and q_u decrease with u. For even k the polar is not subtracted; for odd k its loss is<.001. The full REAL balance is therefore greater than41/2000>1/50, uniformly in all declared k,u.

The difference from018 is the exact evaluation of ARCH4 and the weight eta12 that leaves a positive margin; the recurrences alone do not imply this result. The full row does add a real sign of W and a strict third difference of row1, but it does not complete the table nor certify a new window T.


## Full row N5 — APPROVED

Reviewed `POWER_ROW_SPLIT_028.md` and `tools/power_row_split_028_verify.py`; independent run PASS. The Laguerre coefficients of k0 and k1 and their norms70 and28 are correct. The archimedean Toeplitz bands keep the factors1/2 and1/r!. The polygamma series use256 summands and two valid integral endpoints; ψ(127/4) is reconstructed fromψ(3/4)=−γ+π/2−3log2 via31 steps. The three rational ARCH endpoints are certified.

The legitimate ARCH monotonicities in k and u cover all infinite parameters. The beta polar has the declared normalization, sign (−1)^k and quotient (k+N)/[(k+1/2)(4u²−1)]. For N5,k≥1 that quotient is≤4/(4u0²−1)<1. The endpoint p51(u0)<.002 dominates all adverse polars. p50 decreases with u; hence using ARCH(u0)>−.13 and polar(63)>.23 on [u0,63] is valid without assuming AP monotonicity. For u≥63, ARCH>.5 and the k0 polar remains favourable.

WR5 eta12 is valid for all u≥u0 and k≥0. Its generating series has positive coefficients; the monotonicity of R5 is justified by that series, not by the closed numerator of mixed signs. R5<2500 gives2sqrt R5<100. The full comb bound viaΛ(q)≤q, q^−11.5≤q^−11 and the integral from2 is less than.06. No prime power is missing.

The full real balance gives W>norm²/25 for all k≥0,u≥31.5 and W>4norm²/5 for k≥1. The identity A_(N,1)=A_(N,0)+u∂_uA_(N,0) is derived from the resolvent recurrence and the beta norm, without asymptotic limit or extrapolation in N.

The specific difference of N5 is keeping the positive polar of the edge k0, using opposite endpoints on an interval and starting the covariance at k1. The reusable criterion of§7 is only sufficient under its hypotheses, not a theorem for all rows.

## Scope closure

Two infinite REAL rows of W with uniform u are added, and via the full recurrence the corresponding strict third and fourth differences of row1. Complete monotonicity of all orders, all matrices or a new window T are not deduced. The full sufficient table remains open. A second independent review of both rows agrees.
