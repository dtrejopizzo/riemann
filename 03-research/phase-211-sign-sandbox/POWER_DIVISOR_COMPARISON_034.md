# POWER_DIVISOR_COMPARISON_034 — A uniform positive complete comparator

Status: **PROVED; independent review APPROVED in POWER_COMPARISON_AUDIT_034.md**. For ALL integers N>=3,k>=1 and ALL real rates u such that

    u>=63/2,   u²>=225N/4,
    W[f_(N,k)]>(1/40)||f_(N,k)||².                       (NEW-REGION)

Moreover, FOR k=1, the normalized lower comparator B_N+S_K of033 is >1/40 for EACH odd K. At the FIXED rate u31.5 one covers simultaneously N3,...,17 in ALL columns k>=1; N6,...,17 were the segment not covered by the complete rows1,...,5. For k>=2 the margin improves to3/20 via§7. Neither the whole table nor a new windowT is claimed. Papers untouched.

## 1. Corpus and new reason

Consulted ROUTES-TRIED-INDEX, master grid and CROSSWORD-TO-D on contacts, beta bounds and limits of Euler identities; read ROW_PATTERN029, CONTACT_DECISION032 and PRIME_BALANCE033 with their audits. The beta formula, archimedean monotonicity and Euler are not presented as new.

The difference is that the SIGNED comb of019/033 allows removing the absolute arithmetic cost that limited the region029 u>=16sqrtN. The complete comparator of033 now obtains a POSITIVE margin on a new infinite range, with universal constants and without certifying separate orders. The improvement here comes from ARCH−|POLAR|>0 plus the favourable comb, NOT from Neumann compensating a negative ARCH as at the point211. The critical mechanism of032 is not attributed to this region.

## 2. The region satisfies all arithmetic hypotheses

Since N<=4u²/225,

    2u²/9−u/3+3/2−N
      >=46u²/225−u/3+3/2>0,  u>=63/2.

Thus NEW-REGION lies inside REGION033. ALL contacts are positive by019 and the inequalities033 are valid: S_K>0 for each odd K. The three contacts q2,3,4 that form part of B_N are also positive. No tail of unknown sign is omitted.

## 3. Uniform archimedean margin

ARCH-GENERAL029 proves, by periodic Euler B2 and the exact beta moments, for all N>=2,

    ARCH_(N,1)/norm²
      >=log(u/(2pi))+(1/2)[psi(3/2)−psi(N−1/2)]
                        −9(N−1/2)/u².                  (A)

The bound psi(x)<=logx follows, for example, from Jensen on the law Gamma(x): psi(x)=ElogX<=logEX. Since psi(3/2)=2−gamma−2log2 and u/sqrtN>=15/2, one obtains

    ARCH_(N,1)/norm²
      >log(15/2)−log(4pi)+1−gamma/2−4/25
      >7/200.                                          (ARCH)

The last comparison is rational with the audited constants003. It is a single inequality of constants; not a sweep over N nor an approximation of ARCH at concrete N.

## 4. Exact polar and uniform loss

The beta formulas029 give

    p_(N,0)=POLAR_(N,0)/norm_(N,0)²
      <=4sqrt(pi)sqrtN/u ·(1−1/(4u²))^(−N),
    |POLAR_(N,1)|/norm_(N,1)²
      =p_(N,0)·2N/(4u²−1).

Since sqrt(pi)<9/5 and sqrtN/u<=2/15, the first factor is <24/25. Integer Bernoulli and N/(4u²)<=1/225 give

    (1−1/(4u²))^N>=1−N/(4u²)>=224/225,
    p_(N,0)<(24/25)(225/224)=27/28.

Moreover N>=3 implies

    2N/(4u²−1)<=2N/(225N−1)<=3/337.

Hence the polar of k1, which is NEGATIVE, satisfies

    |POLAR_(N,1)|/norm² <81/9436<9/1000.                  (POLAR)

Its sign is not discarded nor uniformized with a constant growing in N.

## 5. Positive comparator033 and complete form

By definition033 and arithmetic positivity,

    B_N+S_K
      =ARCH/norm²+POLAR/norm²
         +log2 w(2)+log3 w(3)+log2 w(4)+S_K
      >7/200−9/1000=13/500>1/40                         (COMPARATOR)

for EACH odd K. FULL033 keeps the WHOLE tail and gives

    W[f_(N,1)]/norm²>=B_N+S_K>1/40.

This proves NEW-REGION at k1. It can also be proved directly ignoring the favourable comb; making COMPARATOR explicit shows that the criterion033 no longer remains merely a formal obligation. The contraction is not necessary for the margin of this region and the contrary is not claimed.

## 6. Scope

The condition u²>=225N/4 improves the condition029 u²>=256N for ALL columns k>=1, using the arithmetic sign at k1 and the larger margin in the remaining columns. At u31.5, 4u²/225=441/25=17.64; hence the integer segment N<=17 without individual verifications.

No negative ARCH has been repaired here nor has the whole range033 N/u² near2/9 been decided. The almost exact cancellation of211 remains a pointwise certificate032. The edge k0 is not included. The columns k>=2 are proved separately in§7, without extrapolating to them the arithmetic sign of k1.

Reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_divisor_comparison_034_verify.py

PASS; only universal constants Fraction/intervals. The uniformity in N,u resides in the written inequalities.


## 7. Uniform extension to ALL columns k>=2

The same ARCH-GENERAL029, now with psi(k+1/2)>=psi(5/2)=psi(3/2)+2/3 and k−1/2>=3/2, gives

    ARCH_(N,k)/norm²
      >log(15/2)−log(4pi)+1−gamma/2+1/3−4/75
      >19/40,  k>=2.                                    (ARCH2)

Indeed the margin with respect to the archimedean bound of k1 is1/3+8/75=11/25. No column is evaluated separately.

Here the comb has no assumed sign. CENTERED029, valid for ALL k, with eta4 gives

    |c_f(t)|/norm²<=e^(-4t)R,
    R=[(u²−16)/(u²−64)]^(N−1/2)
      <=exp[48(N−1/2)/(u²−64)]
      <exp(9/10)<5/2.                                    (CENTER)

For the exponent, 48(N−1/2)/(u²−64)<9/10 is equivalent to48N+168/5<(9/10)u². Since 48N<=(64/75)u² and 9/10−64/75=7/150, it suffices that u²>720, guaranteed by u>=63/2. The last comparison uses the rational interval log(5/2)>9/10; exp is not replaced by a decimal.

Using ALL contacts, Lambda(q)<=logq and the decreasing integral of x^-4 logx,

    sum_(q>=2)Lambda(q)q^(-9/2)
      <(5/7)2^-4[(5/3)log2+2/9]<31/500.

We used q^-1/2<=2^-1/2<5/7. Hence

    |PRIME|/norm²<2R(31/500)<31/100.                     (PRIME2)

The beta formulas029 and binom(k+N−1,N−1)<=N^k, c_k>=2^-k prove for ANY k

    |POLAR_(N,k)|/norm²<=p_(N,0)[2N/(4u²−1)]^k.

Since 2N/(4u²−1)<=3/337<1 and p_(N,0)<27/28, the odd polar is <9/1000; the even one is favourable. It is not assumed that the comb of these columns is favourable.

Putting the three inequalities together,

    W[f_(N,k)]/norm²>19/40−31/100−9/1000
                         =39/250>3/20,  k>=2.           (HIGHER)

This completes NEW-REGION for ALL k>=1. The proof uses two regimes: the small archimedean margin of k1 needs the real sign of the comb019/033; from k2 on, the beta gain allows a uniform absolute cost. The edge k0 remains outside the statement.

## 8. Coverage corollaries from combining already audited certificates

At FIXED u63/2, ARITHMETIC_BLOCK007§1 proves W>10^-4 norm² on ALL of V12=e^(-uy)·{polynomials of degree<=11}. For N<=12, g_N(y)=y^(N−1)e^(-uy)/(N−1)! belongs to V12. Combining it with NEW-REGION (N<=17 at this rate), the rows3<=N<=12 are completed for ALL k>=0, with margin>10^-4. Rows1,2 were already proved. For N13,...,17, this corollary leaves only k0 open; it does not extend V12 to higher orders.

For EVERY rate u>=63/2, SIGNED_TRANSFER014§1 allows eight poles with multiplicities and proves W>10^-3 norm². The atom g_N with N<=8 is represented in the space of denominator(s+u)^8 via the numerator(s+u)^(8−N), of degree<8. Hence k0 is covered uniformly up to N8. NEW-REGION covers k>=1 up to N17 for all those rates (since u²>=u0²>225·17/4). Thus the rows3<=N<=8 are completed uniformly, with margin>10^-3. k0 uniform in u for N9,...,12 is not claimed: the certificateV12 uses only the fixed rate63/2.

These space inclusions do not alter the certificates007/014 nor turn the new region into a proof of the whole table. The remainder at fixed rate includes k0 forN>=13 and the uncovered interior forN>=18.
