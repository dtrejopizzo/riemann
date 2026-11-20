# POWER_PRIME_BALANCE_033 — Real contraction and signed bounds of the comb

Status: **PROVED; independent review APPROVED in POWER_BALANCE_AUDIT_033.md**: uniform contraction and arithmetic brackets with remainder of known sign. No new W sign nor new row. Papers untouched.

## 1. Corpus and difference

Consulted ROUTES-TRIED-INDEX (Euler/divisors, Möbius transport), master grid and CROSSWORD-TO-D (Λ*1=log, lack of propagation by dilations), and SIGNED_MEAN019, ARITHMETIC_DIFFERENCES019, SIGNED_BALANCE020, CONTACT_BALANCE021, CONTACT_DECISION032. Euler inversion by Neumann series is classical and is not presented as new. Nor is a sign inferred from an identity.

The specific difference is to prove for the REAL GAMMA contact kernel a strictly contractive dilation norm at q>=5, uniform in an explicit range N/u². This property produces ONE-SIDED bounds of the full comb with geometric relative error and known sign, from sums over integers with closed logarithmic coefficients. No common minimum that erases the variation between contacts is used. The failure of positive inversion for other kernels019 does not extend to this contractive class. The comparison with ARCH+POLAR remains an explicit criterion; it is not declared solved by mere convergence.

## 2. Region and real kernel

Throughout the memo,

    u>=63/2,  N integer>=3,
    N <= 2u²/9−u/3+3/2.                                  (REGION)

The atom f_(N,1) is kept, with norm019, and one defines for REAL q>=2

    w(q)=2q^(-1/2) C_(N+1)''(logq)/||f_(N,1)||².

Thus the normalised comb is sum_(q>=2)Λ(q)w(q). By the frontier019,

    chi_N < [1+sqrt(8N−11)]/2 <=2u/3<u log2,

because (2u/3)²−2u/3−(2N−3)>=0 by REGION. Hence w(q)>0 for EVERY q>=2. Λ is not replaced by logq.

The NEW control result is

    w(mq)<=m^(-2)w(q),  q>=5, m>=1.                      (DECAY)

In particular it reaches simultaneously all3<=N<=211 at u63/2, without verifying each order.

## 3. Elementary proof of DECAY

Use the positive polynomials019

    p_j(x)=sum_(l=0)^j (2j−l)! x^l/[2^(j−l)(j−l)!l!],
    p_j=(2j−1)p_(j−1)+x²p_(j−2),
    p_j'=p_j−x p_(j−1),  p_j>x p_(j−1)  (j>=1,x>=0).

For x=u logq, the variable factor of C'' is e^(-x)r_N(x), where

    r_N=x²p_(N−2)−p_(N−1).

Put R=p_(N−1)/p_(N−2). For N>=3,

    R=2N−3+x² p_(N−3)/p_(N−2)
      >=2N−3+x²/(2N−5+x).                              (RLOW)

For N3 the comparison of the denominator is an equality; for N>=4 it follows from the recurrence and p_(N−3)>x p_(N−4). Differentiating r by means of the previous identities gives

    r_N'=r_N+x p_(N−2)(2N−R),
    (log(e^(-x)r_N))'=x(2N−R)/(x²−R).                  (DER)

The logarithmic derivative is only used where r_N>0, already guaranteed by REGION and q>=5.

Write B=2N−5>0, t=logq>=log5>8/5. Then

    u[x/(B+x)−3/x]=u²t/(B+ut)−3/t >3/2.               (SLOPE)

Indeed the left side increases in t. At t8/5 the comparison is exactly equivalent to

    64u²−216u−270N+675>0.

By REGION, this polynomial is at least

    4u²−126u+270=4u(u−63/2)+270>0.

SLOPE implies R−2N>0 by RLOW. Since 0<x²−R<x²,

    x(R−2N)/(x²−R) >=(R−2N)/x
                        >=x/(B+x)−3/x.

Finally DER and the factor q^-1/2 produce

    dlogw(q)/dlogq
      =−1/2+u x(2N−R)/(x²−R) <−2.

Integrating between q and mq proves DECAY. It is an inequality of the exact gamma form, not an assumption of monotonicity over all kernels.

## 4. Contractive space and correction of the three small contacts

On functions q>=5 define

    (Df)(q)=sum_(m>=2)f(mq),
    rho0=2389/3600<2/3.

The elementary estimate

    sum_(m>=2)m^-2
       <=sum_(m=2)^5 m^-2+int_5^infty x^-2dx=rho0

and DECAY imply 0<=Dw<=rho0 w. Moreover DECAY is preserved under D, so that

    0<=D^j w<=rho0^j w, j>=0.                           (CONTRACT)

Define the EXPLICIT arithmetic coefficient

    b(n)=logn−log2·1_(2|n)−log3·1_(3|n)−log2·1_(4|n),
    L(f)=sum_(n>=5)b(n)f(n),
    A(f)=sum_(q>=5)Λ(q)f(q).

The exact divisor identity shows

    b(n)=sum_(d|n,d>=5)Λ(d)>=0,
    L(f)=A((I+D)f).                                    (DIV)

The three corrections are essential: q2,3,4 are removed as DIVISORS, not just three terms of the sum over n. Uncorrected logn is not used and w is not artificially extended by0 below5. All sums are absolute: DECAY gives w(n)<=25w(5)n^-2 and b(n)=O(logn). The positive interchanges of DIV are also justified by Tonelli.

## 5. Signed bounds and uniform relative remainder

For K>=0 put

    S_K=sum_(j=0)^K (−1)^j L(D^j w).

Telescoping DIV gives exactly

    S_K=A(w)+(−1)^K A(D^(K+1)w).                        (TEL)

There is no sign inference from a generic Möbius prefix. The remainder HERE is positive by w>=0 and CONTRACT, and

    0<=A(D^(K+1)w)<=rho0^(K+1)A(w)
                         <=rho0^(K+1)L(w).              (REL)

Hence, for ODD K,

    S_K <= A(w) <= S_K+rho0^(K+1)L(w),
    (1−rho0^(K+1))A(w)<=S_K.                            (BRACKET)

In particular ALL those odd prefixes are positive, uniformly in REGION. For even K the prefix is an upper bound; the two directions are not confused. This is a signed arithmetic inequality over ALL contacts of the tail, with geometric remainder relative to its magnitude; it is not a bound relative to the small residue W.

Two quantitative corollaries require no estimate of an additional tail:

    L(w)/(1+rho0) <= A(w) <= L(w),
    S_K <= A(w) <= S_K/(1−rho0^(K+1))   (K odd).        (INTRINSIC)

The first follows from L(w)=A(w)+A(Dw)<=(1+rho0)A(w); the second from BRACKET. Hence the positive prefix ITSELF also controls its relative error. It is not claimed that this is relative to the small residue W.

The coefficients of L are closed logarithms and divisibilities. D^j w(n) can also be regrouped as sum_(m>=2^j)d_j(m)w(nm), where d_j counts ORDERED factorisations of m into j factors>=2. No campaign is computed nor is it claimed that this enumeration is more economical than032. The aim of the criterion is to keep the sign of the correction and offer an explicit uniform error.

## 6. Concrete comparison with the full form, still open in REGION

Let

    B_N(u)=ARCH_(N,1)/norm²+POLAR_(N,1)/norm²
            +log2 w(2)+log3 w(3)+log2 w(4).

ARCH admits the exact formulas A0/A1 of ARCH_EXACT032 for all N, with x=(u+1/2)/2; the polar is exact019. For EVERY odd K and EVERY REGION,

    B_N(u)+S_K <= W[f_(N,1)]/norm²
       <=B_N(u)+S_K+rho0^(K+1)L(w).                     (FULL)

In particular, without choosing K, the concrete magnitude bound is

    B_N(u)+(3600/5989)L(w) <= W[f_(N,1)]/norm²
                             <=B_N(u)+L(w).             (MAGNITUDE)

This is a quantitative sufficient criterion: proving B_N(u)+S_K>0 in a range proves W in that range, keeping all contacts and the remainder. The error already has a sign and a uniform factor, but that positive inequality has NOT been proved for a new range. The margin032 of order1e−15 does not authorise erasing the remainder however small a prefix is.

As a scale control, rho0^100<10^-17 by rational arithmetic. This indicates that the hierarchy can reach small relative errors with an explicit FINITE order; it does not assume that the truncated value has positive sign nor does it turn convergence into a global proof.

## 7. Result and limit

A NEW uniform tool is obtained on the real gamma class: DECAY in REGION, divisor inversion by a strictly contractive positive operator and BRACKET/FULL with signed relative remainder. The Euler identity is not presented as a discovery nor as a W sign. Relative to019, positivity of the inversion is proved by CONTRACT for this specific tail, and is not required on arbitrary prefixes of other kernels. Relative to032, no other N is certified.

A comparison of B_N+S_K that overcomes the full cancellation in a range remains open. This result controls the arithmetic approximation; it does not increase W coverage nor solve the fixed-rate rows that remain open.
