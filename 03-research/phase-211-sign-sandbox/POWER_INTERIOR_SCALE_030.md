# POWER_INTERIOR_SCALE_030 — Real interior compensation at fixed rate

Status: **PROVED**, independent review APPROVED in POWER_INTERIOR_AUDIT_030.md. With u=63/2 FIXED, for ALL N>=2^20,

    int_1^(9/4) G_N(x) H(x)dx>1/100.                      (BLOCK)

Here G_N is the real gamma kernel and H keeps the complete arithmetic of the joint balance; the contact q2 appears in the block. It is not the total value of W. Interior remainder, tail and global W sign **OPEN**. Papers untouched.

## 1. Corpus and new reason

Read the project rules, SIGNED_MEAN019 (PAIR), INVERSE_KERNEL020, CUMULATIVE_INVERSE022, ARCH_CELL026, DISCRETE_BALANCE027 and STATE029. Consulted the ROUTES-TRIED-INDEX index, master grid and CROSSWORD-TO-D.md on sampling, Euler/Möbius, divisor summation, Riesz means and signed arithmetic errors.

The divisor inversions and the identities are not presented as new sign results. Compared with 019–027, the complete FUNCTIONAL constraint is used to remove the Möbius inverse from the gamma function and cancel all logarithmic singularities at integers>1. The resulting weight is still signed. The positive novelty is proving that the REAL gamma kernel compensates an interior block containing an adverse contact, UNIFORMLY at large orders and at the FIXED rate 31.5. No other constant of a variable-rate wedge is improved and no campaign over N is verified.

The computation of a negative primitive also records why gamma monotonicity alone is not enough; the main result BLOCK keeps its magnitude and obtains compensation, not just another abstract obstruction.

## 2. Inversion of the joint weight and exact cancellation of singularities

Keep K_N and Omega of 026, so that W[g_N]/norm²=int_1^infty K_N(t)Omega(t)dt. The REAL scale constraint is

    G_N(x):=sum_(n>=1)K_N(nx)
           =w_N(x)−xw_N'(x)=x^(−32)D_N(logx)>0,
    D_N=33P_N−P_N', w_N=x^(−1/2)rho_N(logx).

The finite adjoint inversion of the weight is

    H(x)=sum_(m<=x)mu(m)Omega(x/m)/m.

The formula FLOOR027 and the identities sum_(m|r)mu(m)=1_(r=1), sum_(m|r)mu(m)log(r/m)=Lambda(r) simplify EXACTLY to

    H(x)=1+[log((x+1)/(x−1))+c−1−2Psi_1(x)]/x²,
    c=−gamma−log(4pi),
    Psi_1(x)=sum_(q<=x)qLambda(q).                         (H)

For example, the part H_floor of Omega becomes 1, and all singularities log((x+q)/(x−q)) with q>1 cancel when summing their divisors. Only the integrable singularity at x1 remains. The jumps of H at prime powers are NEGATIVE of size 2Lambda(q)/q. These jumps are not erased.

The joint identity becomes

    W[g_N]/norm²=int_1^infty G_N(x)H(x)dx.                (JOINT-G)

Everything is absolute for fixed N: G_N,K_N decay like x^(-32) times polynomials in logx; H grows at most like O(1+logx) and has an integrable logarithmic singularity at 1. For the interchange of scales, the sum of moduli is dominated by sum_n n^(-32) times polynomials in logn, multiplied by a convergent integral in x. The values at the jump points do not affect the integral.

JOINT-G alone is not a sign inequality and coincides with a legitimate application of classical inversion. It is used next for a specific signed bound.

## 3. Gamma monotonicity is real, but the positive-primitive criterion fails

By 025, D_N is log-concave and

    D_N'(0)/D_N(0)=63(d+10)/(2d−1), d=N−1.

It decreases in d. Hence G_N is decreasing for ALL N>=663, and G_N/x² is decreasing for ALL N>=134: it suffices to compare the previous quotient with 32 and 34, respectively. These are properties of the REAL gamma function, not added hypotheses.

However, the natural sufficient premises of a Stieltjes integration do not hold. The rational verifier proves on the SAME complete H

    int_1^(5/2) H(x)dx<−1/50,
    int_1^(5/2) x²H(x)dx<−1/4.                           (PRIMITIVE-FAIL)

Only q2 appears on that interval, with its real value Lambda(2)=log2. Thus the failure of the criterion is arithmetic and quantitative, not a counterexample to the real monotonicity of G. It is not inferred from PRIMITIVE-FAIL that the pairing with G_N is negative.

To reproduce the first bound, a primitive from 1, on 2<=T<3, is

    T−1+(c−1)(1−1/T)−log((T+1)/(T−1))/T
       +2logT−log(T²−1)+4log2/T.

The second is (T³−1)/3+(c−1)(T−1)+(T+1)log(T+1)−(T−1)log(T−1)−2log2−4log2(T−2). The comparisons at T5/2 use exclusively intervals of logarithms/gamma, with no quadrature nor test of another N.

## 4. Uniform gamma comparison on a finite block

Write rho_N(y)=C_N(y)/C_N(0). Its spectral probability has EXACT moment

    M2_N=E tau²=u²/(2N−3), u=63/2.

The elementary cosine/sine inequalities give

    |rho_N(y)−1|<=M2_N y²/2,
    |rho_N'(y)|<=M2_N |y|.

The real gamma form of the positive scale kernel is

    G_N(x)=x^(−1/2)[(3/2)rho_N(logx)−rho_N'(logx)].

Compare with G_*(x)=(3/2)x^(−1/2). Since log(9/4)<1, on ALL of 1<=x<=9/4,

    |G_N(x)−G_*(x)|<=(7/4)M2_N.                          (GAMMA-ERROR)

This is a uniform local comparison with explicit error; no infinite-N limit is interchanged with the complete form and no generic model is used instead of the gamma datum.

Also, using (H) and enlarging only for a majorant up to 5/2,

    int_1^(9/4)|H(x)|dx<6.                               (H-NORM)

Indeed |c−1|<23/5, int_1^(5/2)x^(-2)dx=3/5, int_1^infty x^(-2)log((x+1)/(x−1))dx=2log2<7/5, and the only prime term is bounded by 4log2 int_2^(5/2)x^(-2)dx<7/25. Adding the length 3/2 gives 297/50<6.

From GAMMA-ERROR and H-NORM,

    |int_1^(9/4)(G_N−G_*)H|
      <(21/2)u²/(2N−3).                                 (ERROR)

The comparison keeps the SIGN and ALL the contacts of the block in the main term; the modulus only controls the gamma approximation error.

## 5. Exact main integral, with contact 2 included

For 1<=x<=9/4, Psi_1(x)=0 if x<2 and 2log2 if x>=2. The comparison integral I_*:=int_1^(9/4)G_*(x)H(x)dx is exactly

    I_*=3/2+(19/27)(c−1)+(3/2)J
                   −log2(sqrt2−32/27),
    J=8/9−(16/81)log(13/5)+(2/3)log(5/2)
                                      −(4/3)arctan(1/5). (I)

The last contribution is precisely that of contact 2. No prime power is omitted: the next ones start at 3, outside the block.

To verify (I), integrate x^(-1/2), x^(-5/2) and the step at 2. In the logarithmic term, the change x=z² takes the upper endpoint to z3/2; integration by parts and arctan(3/2)=pi/4+arctan(1/5) give the formula J with no numerical remainder.

The rational intervals 003 for logarithms, gamma and arctan(1/5), together with sqrt2<99/70, prove

    I_*>1/50.                                           (MAIN)

Its approximate value .0219844 is only for orientation; it is not used in the proof.

## 6. Uniform real compensation at FIXED rate

For ALL N>=2^20,

    (21/2)u²/(2N−3)<1/200.

Combining MAIN and ERROR proves

    int_1^(9/4)G_N H>1/50−1/200=3/200>1/100.

This proves BLOCK on the real gamma kernel, despite PRIMITIVE-FAIL. The result does not use an N chosen and certified separately: the only threshold belongs to the explicit monotone error bound in N.

The favourable balance includes a real negative region of the weight after the jump at 2. Hence it is an integrated compensation, and not the sum of supposedly positive terms nor another exterior tail that becomes negligible.

## 7. What is missing for the total balance

JOINT-G gives

    W[g_N]/norm²=int_1^(9/4)G_NH+int_(9/4)^infty G_NH.

Only the first term has the bound BLOCK. The second keeps all the following contacts and is declared neither favourable nor small. The positive tail in the K Omega representation of 027 remains valid, but it cannot be added twice nor transferred without bookkeeping to a different truncation of JOINT-G.

The remaining goal is to control the remaining adverse stretch AGAINST the real G_N and compare it with the favourable compensations. No new abstract chain of primitives is proposed; PRIMITIVE-FAIL explains the limit of that criterion, and GAMMA-ERROR/MAIN supply the concrete return to the balance. W>=0, total ERR at another N, a new window T or complete coverage of the table are not claimed.

Verifier: tools/power_interior_scale_030_verify.py, Fraction arithmetic/exact intervals; PASS. It certifies MAIN, H-NORM, the analytic threshold and PRIMITIVE-FAIL. Uniformity in ALL N>=2^20 is proved in the text. Papers untouched.
