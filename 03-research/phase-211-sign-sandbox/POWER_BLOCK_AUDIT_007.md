# POWER_BLOCK_AUDIT_007 — Audit of the sign on the complete Laguerre12 block

Status: PROVED. Independent review of POWER_ARITHMETIC_BLOCK_007.md and tools/power_arithmetic_block_007_verify.py; run of the script with output PASS. Papers untouched.

## 1. Formulas and factors of the contact

The coordinate norm in the Laguerre basis is the L² norm. The archimedean and polar bands coincide with the formulas audited in rounds 004–006. The autocorrelation of a real vector sums each triangular pair only once, while a symmetric matrix counts each off-diagonal pair twice. This explains exactly a0(n)=-2Lambda(n)n^-32 and ak(n)=-Lambda(n)n^-32 qk(63logn), k>=1. The script uses these two different factors both for contact 2 and for the tail majorants. It does not presuppose positivity of an individual contact matrix.

## 2. Euler–Maclaurin and the interval bands

The finite sums for S_p run from 16 to 255, and the tail starts at 256. For p2..12, the bounds given by T_p and T_p minus the cubic term are correct with the declared directions. A direct justification of their signed remainder is to write the tail as a Laplace integral of e^(-Mt)/(1-e^-t). The global inequalities

    1/t+1/2+t/12-t³/720 < 1/(1-e^-t) < 1/t+1/2+t/12

are obtained by expanding the positive denominators of the partial fraction of coth(t/2), with a positive remainder after each truncation. Integrating against t^(p-1)e^(-Mt)/Gamma(p) produces exactly the rising factorials p and p(p+1)(p+2) used. It is valid for every p>1, not only in an asymptotic regime.

The gamma interval at M256 has the correct signs: terms up to -1/(120M^4) are retained, and the remainder lies between 0 and 1/(252M^6). Machin with thirty alternating terms and the atanh series for log have correct tails. The intervals are formed entirely with Fraction and there is no hidden floating-point rounding. The sign of each coefficient when combining bands and polygamma is correctly preserved.

For qk(63log2), intervals of positive powers of log2 and full interval multiplication are used; sums with alternating coefficients take the relevant endpoints. Contact 2 includes its factor Lambda(2)=log2 via a separate interval multiplication.

## 3. Rational centre and twelve-dimensional matrix

Each centre is the rational interval midpoint rounded down to denominator 10^12. The error of each band is taken as the maximum of its distances to both endpoints: the rounding shift is included. The error sum per row uses all Toeplitz bands and the maximum over the twelve rows; its value is certified <10^-8.

The exact LDL elimination of the centre minus 1/1250 times the identity has twelve positive pivots. The loop updating the whole remaining square is safe: no entry of the column or row of pivot k is modified while i,j>k. The symmetric entries are recomputed separately from the same initial value and the same unaltered factors. Thus ARCH+POLAR+contact2>(1/1250-10^-8)I.

## 4. Full tail in operator norm

The sign test of qk(x+40) is run for all k0..11, including k0, whose only coefficient is 1. The property (-1)^k a_kj>=0 implies that, for x>=40, the sum of absolute values of its shifted monomials coincides with |qk(x)|. Hence the cancellation present before the shift is not lost and no favourable matrix sign is assigned to the tail.

For t=logx>log3>1, the logarithmic derivative of f_j is less than 1+693/23-32<0 for j<=11, so the sum from 3 is bounded by the first term plus the integral. The substitution t=log3+z leaves the coefficients of (a+z)[63(a+z)-40]^j. The formula for R_jr used by the script is exactly its binomial expansion, and all those coefficients are nonnegative and increasing in a>40/63. Replacing log3 by 11/10 preserves the majorant. Each integral of z^r e^-31z is r!/31^(r+1), explaining the factor 3^-31.

Lambda(n)<=logn is used for ALL integers n>=3: the majorant includes powers of 2 and any contact beyond 1024 without truncation. The sum of absolute bands t_k produces a row maximum <3/5000. For the symmetric matrix this controls the operator norm of the WHOLE tail, independently of its signs and cross terms. The absolute convergence of those sums is also proved by the majorant.

## 5. Conclusion and scope

Subtracting the norm of the tail gives strictly

    W|V12 > (1/1250-10^-8-3/5000)I > (1/10000)I.

This result covers all vectors of the block and all contacts. The test of WITNESS006 belongs to the block and has negative ARCH+POLAR; the advance does verify arithmetic compensation within a previously indefinite region. Positivity is not deduced when adding modes, on other arbitrary sets of twelve rates, nor on the whole window domain. The next step requires a principle or an additional certificate.
