# POWER_INVERSE_LOGCONCAVITY_025 — Closing the signed arithmetic balance for N129

Status: **PROVED** log-concavity of a compensated polynomial for all N; **PROVED** improved exterior cut for K129; combined with CELL_TEST024, **PROVED** ERR129<−33/50. Independent review approved in POWER_INVERSE_LOGCONCAVITY_AUDIT_025.md, verifier PASS. W>=0 is not claimed. Papers untouched.

## 1. Corpus and precise difference

Read: the project rules, INVERSE_KERNEL020, CUMULATIVE_INVERSE022, CUMULATIVE_TEST023, CELL_BALANCE024 and CELL_TEST024. Consulted index/grid/crossword on log-concavity of coefficients/polynomials and Möbius; found antecedents of generic log-concavity and its insufficiency, also cross-checked against CONE001§4. Positive theta is not used, and positivity of an inverse is not inferred from generic log-concavity.

The mathematical difference here is to prove that the logarithmic quotient of a SPECIFIC polynomial decreases. A single rational inequality at t0 then controls the WHOLE complete Möbius sum on a half-line much larger than the degree cut of020. This allows combining a single integrated interior balance with all other cells, without a campaign over N and without again requiring K>=0 where it was already refuted. The covariance lemma and the classical quotient criteria are not presented as new tools; their application produces the new cut and a real signed bound of ERR.

## 2. Coefficients and log-concavity for ALL N

Fix u=63/2,N>=2,d=N−1. With P_N(t)=sum_(j=0)^d p_jt^j, p0=1 and the gamma recurrence of020,

    (j+1)p_(j+1)/p_j=2u(d−j)/(2d−j),
    D_N(t)=33P_N(t)−P_N'(t)=sum_(j=0)^d c_jt^j,
    c_j=p_j(3d+30j)/(2d−j)>0.                              (COEF)

The COMPLETE compensated inverse of022 is

    K_N(x)=x^(−32)sum_(m>=1)mu(m)m^(−32)D_N(logx+logm).     (INV)

Define r_j=(j+1)c_(j+1)/c_j for j<d and r_d=0. From COEF,

    r_j=2u [(d−j)/(2d−j−1)] [(3d+30(j+1))/(3d+30j)].        (RATIO)

The first ratio is nonincreasing in j: its continuous derivative has numerator1−d<=0. The second is1+30/(3d+30j), strictly decreasing. Hence r_j decreases, including the final step to0. For t>0, the weights omega_j=c_jt^j/D_N(t) form a probability and

    D_N'(t)/D_N(t)=sum_j omega_j r_j,
    (D_N'/D_N)'=Cov_omega(r_j,j)/t<=0.                     (LC)

The sign of the covariance is proved directly as (1/2)sum_(i,j)omega_iomega_j(r_i−r_j)(i−j)<=0. Thus log D_N is concave on t>0 and by continuity on t>=0. It is not claimed that this alone makes the inverse positive.

## 3. One rational certificate suffices for a complete half-line

If for some t0>0 one proves D_N'(t0)<=30D_N(t0), LC implies for ALL t>=t0 and m>=1

    D_N(t+logm)/D_N(t)<=exp(30logm)=m^30.

By INV and the COMPLETE Möbius sum,

    |K_N(x)/[x^(−32)D_N(logx)]−1|
       <=sum_(m>=2)m^(−2)<=1/4+int_2^infty y^(−2)dy=3/4.

In particular,

    K_N(x)>=x^(−32)D_N(logx)/4>0 for logx>=t0.             (CUT)

The bound controls all m, not a prefix, and does not presuppose favorable Möbius cancellation.

For N129,t0=2/3, the Fraction verifier reconstructs exactly the129 coefficients of COEF and proves

    D_129'(2/3)<30D_129(2/3).                              (CHECK)

No decimal value of the quotient is used in the proof. Since log2>2/3, CUT proves

    K_129(x)>0 for ALL x>=2.                            (TAIL-K)

The certified negativity K129(1)<−1/251 remains intact and is compatible with TAIL-K. Neither a single transition nor a uniform sign on1<x<2 is claimed.

## 4. ALL remaining cells and the complete signed balance

From J_N(x)=x int_x^infty K_N(t)/t²dt and TAIL-K, one has J129(x)>0 for x>=2 and J129(x)/x decreasing there. By lemma LOCAL024, for ALL n>=3,

    S_129(n)>=b_n J129(n)>0,
    b_n=H_(n−1)(1−1/(2n))−logn>=3/4−log2>0.

The certificate of the first cell, CELL_TEST024, proves with complete Möbius and rigorous tail

    S_129(2)>33/100.

The sum over cells is absolutely convergent. Consequently the NORMALIZED arithmetic error of019/018 satisfies on the WHOLE half-line

    F_129=ERR129=−2sum_(n>=2)S_129(n)<−33/50.               (FULL)

This is a real integrated signed inequality, not a prefix sign nor a pointwise criterion: the first cell compensates its negative K region and all remaining cells are controlled analytically, without infinite enumeration. The representation C_B of022 could also be used, but its benefit is not added to S2: they are different assignments of the same pairing.

## 5. Exact limit relative to the form W

FULL is not yet a certificate W>=0. The identity of018 keeps

    W[g129]/C129(0)=ARCH_sharp[g129]/C129(0)−ERR129.

The quantitative comparison of the ARCH_sharp deficit with the complete signed benefit is missing; the bound ERR<−.66 is not declared sufficient for that comparison. The sign of ERR is not extended to other N, nor to the complete table, nor to a new windowT. The result is a complete integrated arithmetic balance at the same order129 where the pointwise criterion failed.

Exact reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_inverse_logconcavity_025_verify.py
    python3 03-research/phase-211-sign-sandbox/tools/power_cell_test_024_verify.py

The first certifies CHECK; LC/CUT prove its infinite extension. The second certifies the single interior cell and the Möbius tail entering it. There are no approximate values in the proof.
