# POWER_ARITHMETIC_BLOCK_007 — Sign on the whole Laguerre block of dimension twelve

Status: PROVED, exact rational certificate executed and independently reviewed in POWER_BLOCK_AUDIT_007.md. Papers untouched.

## Difference from antecedents

The project rules and the index/grid/crossword antecedents recorded in POWER_BRIDGE_002 are consulted, as well as the semilocal/exterior family. The semilocal reduction is not proposed as new. The new object is a COMPLETE EXPLICIT block of dimension twelve, with all its cross terms: POWER_ARITHMETIC_WITNESS_006 only decided one vector. That vector proves that ARCH+POLAR is indefinite here. Therefore positivity of this whole block needs a real arithmetic compensation, and does not follow from the earlier regions where ARCH or ARCH+POLAR are positive.

## 1. Finite theorem

Let u=63/2 and V12=span{sqrt(63)e^-uy L_j(63y)1_(y>0):0≤j≤11}. Then

    W[h] > (1/10000)||h||² for every nonzero real h in V12.

Neither all orders nor all sets of rates are proved. The corresponding exterior images are the combinations of powers and their first eleven derivatives in the exponent a=32. The negative test of ARCH+POLAR from WITNESS006 belongs to V12, so the theorem really crosses that indefinite region.

## 2. Exact Toeplitz matrices

The basis is orthonormal and all pieces are Toeplitz. The diagonal archimedean band is d=psi16−log pi. For k>=1,

    b_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!.

The polar band is

    p_k=(63/992)(−1)^k[(32/31)^k+(31/32)^k].

Set q_k(x)=L_k(x)−L_(k−1)(x), L_-1=0. The band of contact n is

    a_0(n)=−2Lambda(n)n^-32,
    a_k(n)=−Lambda(n)n^-32 q_k(63log n), k>=1.

The different factor two on the diagonal is essential: the autocorrelation has a single triangular sum, while the symmetric matrix counts its off-diagonal terms twice. No individual piece of the comb is presumed positive as a matrix.

## 3. Exact certificate of ARCH+POLAR+contact 2

The attached verifier uses only Fraction, factorials and binomial coefficients. For the sums S_p=Σ(m>=16)m^-p, p2..12, it uses m16..255 and the Euler bounds with signed remainder

    T_p(M)=M^(1−p)/(p−1)+(1/2)M^-p+(p/12)M^(-p−1),
    T_p(M)−p(p+1)(p+2)M^(-p−3)/720
      <Σ(m>=M)m^-p<T_p(M), M=256.

This is the standard Euler–Maclaurin lemma for positive powers, with alternating remainder; it can also be obtained by integrating the expansion of coth with signed remainder. For gamma one uses

    g0=H256−log256−1/(2·256)+1/(12·256²)−1/(120·256⁴),
    g0<gamma<g0+1/(252·256⁶).

Log2 and log pi are enclosed with integrated geometric series; pi via the exact identity 16atan(1/5)−4atan(1/239) and alternating series with thirty terms. The signs and remainders are explicit in the script. This yields rational intervals for all bands, including q_k(63log2), without floating-point evaluation.

Each band is temporarily replaced by its midpoint rounded down to denominator 10^12. The maximal absolute row sum of the error is <10^-8. The LDL of the central rational matrix minus (1/1250)I has ALL twelve pivots positive. Consequently

    ARCH+POLAR+contact2 > (1/1250−10^-8)I.                (B12)

The exact arithmetic of this claim is entirely reproduced by `tools/power_arithmetic_block_007_verify.py`.

## 4. Tail of all contacts n>=3 in operator norm

The majorant by absolute coefficients of q_k(x) in powers of x loses too much. Its cancellation is kept by expanding in x−40:

    q_k(x)=Σ(j=0..k) a_kj (x−40)^j.

The script verifies exactly that (−1)^k a_kj>=0 for all k≤11, j≤k. Since 63log n>42, it follows that

    |q_k(63log n)|=Σ_j |a_kj|(63log n−40)^j.

For each j≤11, f_j(x)=log x(63log x−40)^j x^-32 decreases on x≥3: its logarithmic derivative with respect to t=log x is 1/t+63j/(63t−40)−32<1+693/23−32<0. By sum–integral comparison and 1<log3<11/10=a,

    Σ(n>=3)f_j(n) ≤3^-32 a(63a−40)^j
       +3^-31 Σ(r=0..j+1) R_jr(a) r!/31^(r+1),

where R_jr(a) is the coefficient of z^r in (a+z)[63(a+z)−40]^j. All are nonnegative and increase with a>40/63; hence replacing log3 by a preserves the bound. This formula integrates the shifted polynomial exactly, without introducing values of other primes.

Multiplying by |a_kj|, using Lambda(n)≤log n and the diagonal factor two, one obtains rational majorants t_k for the sum of the absolute values of each tail band. The verifier proves

    max_i Σ(j=0..11)t_|i−j| <3/5000.

By the symmetric Schur criterion, the norm of the WHOLE tail is <3/5000. It is not presumed positive; its norm is subtracted from B12. Finally

    W > [1/1250−10^-8−3/5000]I > (1/10000)I.

## 5. Limits and next requirement

The result controls all vectors and all contacts on V12, and uses contact 2 decisively. It is not claimed that this isolated contact has positive matrix sign, nor that this margin persists when more modes are added. The step to dimension thirteen or more requires new certificates or a uniform principle; here it remains open. The bridge POWER_BRIDGE_002 identifies why a rule for all degrees would indeed reach all tests, but it does not replace that rule.
