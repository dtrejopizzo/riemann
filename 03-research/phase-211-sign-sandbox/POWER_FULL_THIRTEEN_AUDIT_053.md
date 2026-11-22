# POWER_FULL_THIRTEEN_AUDIT_053

Status: **APPROVED** the complete certificate and proof of POWER_FULL_THIRTEEN_053. One obtains W>norm²/4000 for all thirteen real poles>=63/2, multiplicities allowed, with proper real numerator. Papers untouched.

Antecedents cross-checked: index/grid/crossword, COMMON_TRANSFER010, FULLTEL014, MULTI015, FULL_TWELVE050 and CONFLUENT_THIRTEEN052. The cut J=96 and its audit precede the exhaustive segment. The difference is a FULL gain on fourteen poles with zero numerator, not positivity by codimension nor automatic extrapolation of the confluent block.

## Rational certificate and rounding

Read in full the memo and tools/power_full_thirteen_053_verify.py. Independent reproduction with python3, without modifying parameters: **exit0; logarithms/pi,108 bands, prior row error, the95 LDLs of indices1,...,95 and the final conclusions PASS**. No indices of the segment remain unchecked.

The lograw optimization keeps the same512 terms and precision10^−260: each power and sum is evaluated in rational intervals with outward rounding. The universal remainder2(1/2)^1025/[1025(1−1/4)] dominates the omitted one because the exact argument lies between0 and1/2. This avoids huge denominators without changing the statement, margin, precision, cut or success condition. Pi via Machin and logpi via monotonicity of the endpoints keep their enclosures.

Reviewed Euler–Maclaurin12 for Hurwitz: after the termB24, the periodic remainder is bounded by |B24|(p)_23/[24!CUT^(p+23)]. It is obtained by integrating the absolute value of the 24th derivative using |B24({x})|<=|B24|. The exact coefficients of each band multiply the rational endpoints BEFORE rounding. The gamma remainders and the polar bands keep the audited normalizations. Real propagation control does not rest only on a prior derivative estimate: the program checks total operator error<10^−12 before any LDL.

Vandermonde compresses C_jᵀTC_j exactly to thirteen bands; the maximal required index is12+95=107, covered by108 bands. The compressed Gram is binom(2j,j+r), and the omitted factor4^−j is common to form and norm. The error is paid against epsilon C_jᵀC_j, avoiding an incorrect payment against the coordinate identity. The95 exact LDL13 verify margin1/500 on all numerators, including their cross terms.

## Orbit, mixture and full comb

CENTERED_MOMENT053 already proves E23>norm²/10 for ALL j>=96 and ALL F0∈V13. Together with the certified segment, E23>norm²/500 holds for every j>=1. Each numeratorD of degree<=13 withD(0)=0 is sP, degreeP<13, and its confluent fourteen-pole base is QF0. MULTI015 with fourteen factors mixes exactly the indices already positive. Norm, ARCH, both contacts and polar use the same nonnegative weights; for finite rates the series are absolutely convergent. No restricted hypothesis is iterated on an unknown intermediate base.

The uniform weighted trace010 is B_T14=947334302964<973312². The total exponent of the tail is65/4; keeping n^−1/4<=5/7 for n>=4 is valid because(7/5)^4<4. The sum-integral comparison with log4<7/5 produces the rationalL4 of the memo, less than1/1000. It includes ALL integers from4 and all their prime powers. Thus W>norm²/1000 on all fourteen poles with zero numerator.

Finally, the FULLTEL corrections for thirteen poles belong precisely to that class of fourteen poles. The identity simultaneously preserves norm, polar and all contacts with nonnegative coefficients. The base052 has margin1/4000 and each correction a larger margin1/1000; subtracting1/4000 times the norm identity proves the declared margin without deterioration under rate movements. Coincidences and multiplicities require neither limits nor division by pole differences.

Neither arbitrary dimension nor general fourteen poles is proved, and the result by itself does not certify a new time window of Paper46.
