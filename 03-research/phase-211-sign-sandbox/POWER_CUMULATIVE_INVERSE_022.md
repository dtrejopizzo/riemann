# POWER_CUMULATIVE_INVERSE_022 — Compensated primitive and cellular balance with B

Status: **PROVED** primitive identities, arithmetic mass and quantitative cellular criterion; **PROVED** a positive point of the compensated kernel where h is negative. **FALSIFIED** the universal compensated hypothesis K_N>=0 by the complete test N129 of POWER_CUMULATIVE_TEST_023.md; the criterion remains valid as an implication. Global signed pairing **OPEN**. Papers untouched.

## 1. Corpus and precise difference

Read the project rules, SIGNED_MEAN019§§2–6 (PAIR), INVERSE_KERNEL020 (LOCAL/OUTER), STATE020 and the complete certificate INVERSE_INTERIOR022. Consulted the index (Euler/Möbius, moments and inverses), the master grid and CROSSWORD-TO-D.md (divisor summation and rounds019/020). The identity mu*1 and integration by parts are classical; they are not presented as new tools.

The difference is an explicit criterion WEAKER than h>=0 that uses the slopes and jumps of the SAME B, tolerates local growth of the tail primitive and produces a signed quantitative bound. Its constant is combined with a discrete mass exactly1 derived from mu*1. PAIR is not repeated as a sign assumption and no global inequality is inferred from a single point. The complete counterexample h128(1)<0 already belongs to the companion memo022 and is cited without duplicating it.

## 2. Complete, uniform primitive and exact integer mass

With u=63/2 and rho_N=C_N/C_N(0), set

    w_N(x)=x^(−1/2)rho_N(logx)=x^(−32)P_N(logx),
    H_N=−w_N',
    h_N(x)=sum_(m>=1)mu(m)mH_N(mx),
    J_N(x)=int_x^infty h_N(y)dy.

Here P_N has positive coefficients, P_N(0)=1, degree N−1; the rational recurrence is that of020/022. Term-by-term integration gives the COMPLETE formula

    J_N(x)=sum_(m>=1)mu(m)w_N(mx).                           (J)

For each fixed N, the series of (J), h and their necessary derivatives converge absolutely and uniformly on x>=1: expanding P_N(logm+logx) reduces to terms m^(−32)(logm)^j times x^(−32)(logx)^l, the latter uniformly bounded. The same observation proves J_N(x)=O_N(x^(−32)(1+logx)^(N−1)) and the limits at infinity used below. It is not a formal primitive of a conditional series.

The divisor identity contributes an EXACT discrete mass, with all its signs:

    sum_(n>=1)J_N(n)
      =sum_(n,m>=1)mu(m)w_N(mn)
      =sum_(r>=1)w_N(r)sum_(m|r)mu(m)=w_N(1)=1.            (MASS)

Fubini is absolute: the sum of moduli is bounded by sum_r d(r)w_N(r), convergent already with d(r)<=r. MASS does not prove that each J_N(n) is positive.

## 3. The compensated criterion tolerating negative h

Define

    K_N(x)=J_N(x)+x h_N(x)=J_N(x)−xJ_N'(x).                 (K)

**Cellular theorem.** If K_N(x)>=0 for ALL x>=1, then J_N>=0 and

    F_N=2int_1^infty h_N(x)B(x)dx
        <=−2(3/4−log2)[1−J_N(1)]<=0.                     (CELL)

The hypothesis K>=0 is strictly more permissive than requiring h>=0: it admits h<0 as long as its magnitude is <=J/x. An implication is claimed here, not that the global hypothesis is proved.

Proof. By (K), (J_N(x)/x)'=−K_N(x)/x²<=0. The quotient tends to0 at infinity, so J_N(x)>=0. For n>=2 and n−1<=x<=n,

    J_N(x)>=xJ_N(n)/n,
    int_(n−1)^n J_N(x)dx>=[1−1/(2n)]J_N(n).               (CELL-AVG)

B(1)=0; B has slope−H_(n−1) on(n−1,n) and jump logn at n. Integrating by parts, keeping the jumps, gives

    F_N/2=int_1^infty J_N dB
      =sum_(n>=2){logn J_N(n)−H_(n−1)int_(n−1)^n J_N(x)dx}.

The boundary J_N B vanishes at infinity and both contributions converge absolutely. By CELL-AVG, each cell is <=J_N(n)[logn−H_(n−1)(1−1/(2n))]. Now

    H_(n−1)−logn>=1−log2,
    H_(n−1)/(2n)<=1/4.

The first inequality increases from n2 by integral comparison; the second follows from H_(n−1)<=n/2 by induction. Thus each bracket is <=log2−3/4<0. Summing and applying MASS proves CELL. In particular the nonnegative discrete mass implies J_N(1)<=1. QED.

This is not the identity PAIR relabeled: K>=0 is a verifiable sufficient pointwise inequality, allows negative h and delivers the explicit constant and mass1. Nor does CELL by itself prove W>=0: it must still compensate the sharp archimedean deficit of019/020.

## 4. New arithmetic kernel and exterior region

The function whose sign remains pending has a concrete expression with the same complete inverse:

    K_N(x)=x^(−32)sum_(m>=1)mu(m)m^(−32)D_N(logx+logm),
    D_N(t)=33P_N(t)−P_N'(t).                              (KD)

All coefficients of D_N are strictly positive: the recurrence020 gives (j+1)p_(j+1)<=u p_j, and33−u=3/2>0. Positivity of the Möbius inverse is not deduced from this.

The exterior argument020 also applies to D_N: if logx>=(N−1)/30, the quotient D_N(logx+logm)/D_N(logx)<=m^30. Via sum_(m>=2)m^(−2)<=3/4,

    K_N(x)>=x^(−32)D_N(logx)/4>0                          (OUT-K)

in that region. OUT-K is an application of the already proved lemma020, not a new proof of interior cancellation. For an N to which one wants to apply CELL, controlling K on the declared finite interval is missing. The universal version for all N is false by POWER_CUMULATIVE_TEST_023.md: −1/250<K_129(1)<−1/251. OUT-K remains valid and does not erase that interior negative region.

## 5. Adversarial point128: real compensation, without extrapolation

INVERSE_INTERIOR022 proves −2/3<h_128(1)<−33/50. By continuity, the primitive from1, int_1^x h_128, is NEGATIVE near1; its universal positivity is refuted. J_128 is not monotonically decreasing there either because J_128'(1)=−h_128(1)>0.

Using EXACTLY the same cutoff64, the coefficients P128 and the tail integrals022, the attached verifier proves on the COMPLETE sum

    .665<J_128(1)<.666,
    .003<K_128(1)=J_128(1)+h_128(1)<.004.                   (POINT)

The tail of J is bounded with sum p_j I_j; that of K with sum(p_j+a_j)I_j, where a_j are the coefficients of A=32P−P'. Both are less than10^(−10). The orientative values are J128(1)≈.66561185155114 and K128(1)≈.003266751102; they play no part in the proof.

POINT shows that the compensated criterion can survive at the real point where h>=0 fails and where J increases. It does not prove K>=0 on a uniform neighborhood, on the whole half-line nor for other N; by continuity there is indeed a neighborhood of that point for N128 where K>0. No W certificate nor new table region is added.

## 6. Precise residue

The universal hypothesis K_N>=0 is refuted by023; the CELL criterion does not become a proof of PAIR for all N. The possible new target is an integrated version of CELL-AVG or the signed budget of§7, keeping the same jumps. J>=0 without controlling cell averages does not suffice; h is not replaced by its modulus nor are adverse contributions erased. The exact mass1 may serve to quantify a sign result if that global compensation is obtained, but does not supply it automatically.

Verifier: tools/power_cumulative_inverse_022_verify.py; Fraction/rational intervals, a single point and COMPLETE tails. It reuses and reproduces the interior certificate022 before proving POINT. No campaign over N nor paper modification.


## 7. Positive cellular kernel and budget of the negative part of K

The complete negativity of K129(1) is neither discarded nor absorbed into a hypothesis. Without restricted N nor sign condition, the differential identity of§3 gives

    J_N(x)=x int_x^infty K_N(t)/t² dt.

Substituting it into the Stieltjes integral of§3, by absolute Fubini, proves

    F_N=−2 int_1^infty K_N(t) C_B(t)dt,
    C_B(t)=−t^(−2) int_1^t x dB(x).                       (CB-ID)

The identity alone does not settle the sign. The additional quantitative content is the following lemma on the SAME B:

    C_B(t)>0 for t>1;
    C_B(t)=(1−t^(−2))/2 for1<=t<2;
    C_B(t)>=(3/4−log2)/2 for t>=2.                      (CB-POS)

Proof. Write S(t)=int_1^t x dB(x). On a complete cell,

    S(n)−S(n−1)=nlogn−H_(n−1)(n−1/2)<=−a n,
    a=3/4−log2>0,

by the numerical inequality proved in§3. Thus S(n)<=−a sum_(j=2)^n j and −S(n)/n²>=a/2 for n>=2. Between n and n+1,

    C_B(t)=H_n/2+[C_B(n)−H_n/2]n²/t²,

a convex combination of C_B(n) and H_n/2, both >=a/2. On the first cell dB=−dx and S(t)=−(t²−1)/2, giving the formula and the positivity. The jumps of B are kept, including the one that reduces C_B at2. QED.

The arithmetic mass also transforms WITHOUT replacing K by its modulus:

    int_1^infty K_N(t) floor(t)[floor(t)+1]/(2t²)dt=1.       (K-MASS)

It is obtained by substituting J into MASS and using sum_(n<=t)n=floor(t)[floor(t)+1]/2. Fubini is absolute by the polynomial-logarithmic decay proved in§2. K-MASS does not eliminate the negative regions of K.

The exact signed budget is now

    F_N=−2int K_N^+ C_B +2int K_N^- C_B.                  (BUDGET)

It is not claimed that writing BUDGET by itself contributes a global inequality. CB-POS does quantify where a lesion weighs: for0<delta<=1,

    2int_1^(1+delta) K_N^-(t)C_B(t)dt
      <=delta² sup_[1,1+delta] K_N^- .                    (BOUNDARY)

Indeed C_B(t)<=(t−1) on the first cell. The initial negativity of K129 really contributes an adverse term, but its weight vanishes linearly at1 and the bound of that region is quadratic in its length. That length and the magnitude of the total adverse budget have not been estimated here; hence it is not claimed that the favorable part compensates it either. OUT-K keeps exterior positivity.

This distinguishes the proved result (explicit positive kernel, uniform exterior bound, boundary damping and exact mass) from the open obligation (quantitative control of BUDGET for the real kernel, sufficient moreover to compensate ARCH_sharp). The already refuted universal hypothesis K>=0 is not restarted.
