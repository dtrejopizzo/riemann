# POWER_BOUNDARY_BALANCE_035 — Terminal datum and real descent up to row17

Status: **PROVED; independent review APPROVED in POWER_BOUNDARY_AUDIT_035.md**. At FIXED rate u=63/2,

    W[f_(N,k)]>(1/40)||f_(N,k)||²,
    ALL integers1<=N<=17, ALL k>=0.                  (ROWS17)

The NEW terminal datum is W[f_(17,0)]>(1/25)||f_(17,0)||². A single terminal evaluation, no campaign N13,14,...,17. Papers untouched; no new windowT nor sign of arbitrary mixtures.

## 1. Corpus and precise difference

Consulted ROUTES-TRIED-INDEX, the master grid and CROSSWORD-TO-D on descent, recurrences, terminal data and contacts; read DESCENT016, TABLE_DESCENT018 and its structural falsifier, ARITHMETIC_DIFFERENCES019, ARCH_EXACT032, DIVISOR_COMPARISON034 and the respective audits. No sign is attributed to an isolated recurrence, nor is general monotonicity of ARCH+POLAR assumed, already inadequate in007.

The new difference is combining TWO REAL sign data: the uniform k1 column034 and a single k0 endpoint certified here with the WHOLE adverse comb. That additional information permits a legitimate finite descent. N17 is chosen as the integer endpoint of034 at fixed rate: 4u²/225=17.64. Five independent k0 entries are not proved, nor is an endpoint selected by a sign sweep.

In018, recurrence and eventuality by themselves left terminal data unknown, and the falsifier preserved precisely that lack of sign. Here the terminal datum is real and rigorously positive, and it is only propagated within the range where034 already proves the required column. The descent is not extrapolated to N>=18.

## 2. TerminalN17: normalization and exact ARCH

Fix N17,d16,u63/2. The norm of the edge is

    n_N=||f_(N,0)||²
       =binom(2N−2,N−1)/[2^(2N−1)u^(2N−1)].

ARCH_EXACT032 gives the finite POSITIVE formula for A_N=ARCH/n_N,

    A_N=H15−gamma−logpi−sum_(j=1)^(N−1)b_j S_(j+1),
    b0=1, b_(j+1)=b_j u(d−j)/(2d−j),
    S_p=sum_(n>=16)n^(-p).

For this degree-16 endpoint Euler–Maclaurin up to B4 at M32 suffices. The center is

    Z_p=sum_(n=16)^31 n^(-p)+32^(1−p)/(p−1)+(1/2)32^-p
                  +(p/12)32^(-p−1)
                  −[p(p+1)(p+2)/720]32^(-p−3),
    |S_p−Z_p|<=E_p=p(p+1)(p+2)/(720·32^(p+3)).          (EM2)

The remainder is the integral of the periodic Bernoulli4; sup|B4({x})|<=|B4|=1/30. It is not assumed that the sign of the next term determines the remainder. It is the same absolute argument032 with only TWO Bernoulli terms, sufficient for this margin.

Multiplying the rational endpoints by b_j BEFORE rounding and summing all j1,...,16, the verifier proves

    A_17>−217/250=−.868.                                 (ARCH17)

Only gamma and logpi from003 with audited remainders are used; there is no quadrature nor numerical special functions in the certificate.

## 3. Exact and favorable polar17

The exact beta expression is

    p_N=POLAR/n_N
       =[4^N/(u binom(2N−2,N−1))]
                       [u²/(u²−1/4)]^N.

For N17 this positive fraction satisfies

    p_17>911/1000.                                      (POLAR17)

The polar is not replaced by zero, nor is monotonicity of its sum with ARCH assumed.

## 4. The WHOLE adverse comb from a real slope bound

Let rho_17(t)=C_17(t)/C_17(0)>0, q=−rho'/rho. At k0 the normalized comb is NEGATIVE,

    PRIME/n_17=−2sum_(n>=2)Lambda(n)n^-1/2 rho_17(logn).

By ROOT/CURV026, with d16,

    q(t)>sqrt[(d/t)²+u²]−d/t,  q'(t)>0.

Since log2>2/3 and

    u²=3969/4 >15²+2·16·15/(2/3)=945,

one obtains q(log2)>15. By monotonicity of q, for ALL n>=2,

    rho_17(logn)<=rho_17(log2)(n/2)^(-15).               (TAIL-SLOPE)

This is not an extrapolation from a few contacts: it integrates a differential bound valid on the whole half-line.

The normalized polynomial rho=e^(-ut)P_17(t) has POSITIVE coefficients p_j=b_j2^j/j!. Hence Horner with the rational upper endpoint of log2, using

    2^(-u)=2^-31/sqrt2 < (5/7)2^-31,

proves

    rho_17(log2)<1/600.                                 (RHO2)

Now Lambda(n)<=logn, n^-1/2<5/7 and the decreasing integral of x^-15logx give

    2sum_(n>=2)Lambda(n)n^-1/2 rho_17(logn)
      <=(10/7)rho_17(log2)[(8/7)log2+1/98]
      <(6/5)rho_17(log2)<1/500.                         (PRIME17)

ALL prime powers and the whole infinite remainder have been included, without an enumeration or a tail quadrature. The passage to ALL integers is an upper bound for the modulus of this adverse comb, so its direction in the lower bound of W is correct.

## 5. Real sign of the endpoint and normalized descent

ARCH17, POLAR17 and PRIME17 prove

    W[f_(17,0)]/n_17
      >−217/250+911/1000−1/500
       =41/1000>1/25.                                  (TERMINAL)

Now use the COMPLETE unnormalized recurrence, with a_(N,k)=W[f_(N,k)]:

    a_(N,0)=a_(N,1)+u²a_(N+1,0).                       (REC)

It holds both for the density tau²/(u²+tau²)^(N+1)+u²/(u²+tau²)^(N+1)=(u²+tau²)^(-N), and for the exact polar; no arithmetic term is omitted.

The beta norms give

    ||f_(N,1)||²/n_N=1/(2N),
    u²n_(N+1)/n_N=(2N−1)/(2N).

Therefore the NORMALIZED identity is a convex combination:

    W[f_(N,0)]/n_N
      =[1/(2N)] W[f_(N,1)]/||f_(N,1)||²
        +[(2N−1)/(2N)] W[f_(N+1,0)]/n_(N+1).            (CONVEX)

DIVISOR_COMPARISON034 proves the first normalized term>1/40 for ALL3<=N<=17, at this rate. TERMINAL is>1/25>1/40. Descending N16,...,3 via CONVEX one obtains W[f_(N,0)]/n_N>1/40 in that WHOLE range. Each entry is not certified: the propagation is symbolic and uses exclusively real signs already proved.

With034 for all columns k>=1, rows3,...,17 are completed. INTERIOR017 already proves row1 with margin4/3 and TABLE_DESCENT018 rows2,3 with margin1/8, for all k and u>=63/2; hence rows1,2 also satisfy margin1/40 at the fixed rate. This proves ROWS17.

## 6. Pattern and exact scope

The reusable pattern is a FINITE principle: a truly positive k1 column in1<=N<M and a truly positive k0 terminal edge at M force the earlier edges backwards via REC. The normalized margins propagate by convexity of norms. An identity without those two sign data does not permit it, as016/018 showed.

This memo supplies both data up to M17 and keeps the whole comb. It controls no terminal M>=18 nor the edge for all variable rates u; TERMINAL uses u=63/2 exactly. Nor does it prove positivity of arbitrary mixtures of all these atoms. The sufficient table of all orders and the new windowsT remain open.

Reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_boundary_balance_035_verify.py

PASS. A single terminal evaluation N17 and rational constants; no sweep N13,...,17. The proof of all rows resides in CONVEX and034.
