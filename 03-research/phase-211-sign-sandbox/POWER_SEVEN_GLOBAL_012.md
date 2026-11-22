# POWER_SEVEN_GLOBAL_012 — Uniform sign for all spaces of seven poles >=63/2

Status: PROVED, exact rational certificate executed and reviewed independently in POWER_SEVEN_AUDIT_012.md. Papers untouched.

## 1. Theorem and new reason relative to the previous cases

Let v_1,...,v_7>=u=63/2, allowing multiplicities, and f real nonzero with Laplace transform P(s)/Π_j(s+v_j), degreeP<7. Then

    W[f]>(1/500)||f||².                                  (SEVEN)

This includes arbitrary mixtures of up to seven exterior powers with exponents >=32 and all their corresponding confluent limits. It requires no separation nor upper bound on the rates.

Consulted the project rules, index/grid/crossword according to POWER_BRIDGE_002, the global closures of four/five/six poles and POWER_COMMON_TRANSFER_010. The semilocal family and the filter transport are not presented as new. The new reason is to use jointly TWO estimates more precise than those of the previous closure: the filter deficit is bounded directly as a product, avoiding separating its maxima, and the weighted norm is controlled by the exact confluent trace audited in COMMON_TRANSFER§6. Both keep the slack needed in dimension seven. The confluent certificate of seven is verified anew; it is not inferred from that of six.

## 2. Exact confluent certificate

In the orthonormal basis phi_j=sqrt(63)e^-uy L_j(63y), j0..6, AP=Arch+Polar is Toeplitz. Its bands are

    AP_0=psi16−log pi+4u/(u²−1/4),
    AP_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!
          +[2u/(u²−1/4)](−1)^k[(32/31)^k+(31/32)^k].

The verifier `tools/power_seven_global_012_verify.py` encloses the polygammas via the sums m16..2000 plus integral tails between 1/[r·2001^r] and 1/[r·2000^r]. It uses the rational interval module with outward rounding `power_fixed_grid_003.py` for gamma, pi and log. All computation is done with Fraction; no floating special function is involved.

The seven pivots of INTERVAL LDL of AP−(69/1000)I have strictly positive lower endpoint. Thus, for every f0 with transform P(s)/(s+u)^7,

    AP[f0]>(69/1000)||f0||².                              (BASE7)

The moment vectors have squared norms

    AA=(63/31²)Σ(j=0..6)(32/31)^(2j),
    BB=(63/32²)Σ(j=0..6)(31/32)^(2j).

The rational comparison 4AA BB<1 proves moreover |Polar[f0]|<||f0||². This bound is used only for the polar variation under the filter, keeping the favourable sign within BASE7.

## 3. Direct spectral deficit of the filter

The positive digamma series and m(0)>−5373/1000 give, for x=tau²,

    m(tau)>ell(x):=−5373/1000
             +Σ(k=0..15)x/[a_k(4a_k²+x)], a_k=k+1/4.

The constant m(0) is verified with the rational intervals of the same module. The function ell is increasing and ell(49)>1/20. Fix c=1/100. For j0..195 and x∈[j/4,(j+1)/4],

    (c−m(sqrt(x)))_+ [(1+x/u²)^7−1]
      ≤(c−ell(j/4))_+ [(1+(j+1)/(4u²))^7−1]
      <57/1000.                                         (DIRECT)

The 196 last comparisons are exact rational ones, verified individually. This is a certified finite partition of a frequency interval, not a numerical sweep nor an extrapolation between points: each interval is covered by the two monotonicities. For x>=49, m>c and the deficit is zero.

The step DIRECT is more precise than separately estimating x(c−m)_+ and the quotient of the filter: it keeps track of where its two factors are simultaneously large.

## 4. Global transport to arbitrary rates

With the same numerator, write F0=P/(s+u)^7 and F=HF0, H=Π(s+u)/(s+v_j). Set R=|H(i tau)|², R0=Πu²/v_j², r0=H(−1/2)H(1/2). Since v_j>=u,

    1≤R/R0≤(1+x/u²)^7,
    1−7/(4u²)≤r0/R0≤1.

The exact identity of COMMON_TRANSFER keeps the new target norm:

    AP[f]−c||f||²=R0(AP[f0]−c||f0||²)
       +(1/2pi)∫(R−R0)(m−c)|F0(i tau)|²d tau
       +(r0−R0)Polar[f0].

DIRECT controls the integral loss by (57/1000)R0||f0||². The polar variation loses at most 7R0||f0||²/(4u²). BASE7 gives

    AP[f]−c||f||²
      >R0[69/1000−1/100−57/1000−7/(4u²)]||f0||²>0.

The bracket is rational and strictly positive. Hence

    AP[f]>(1/100)||f||²                                 (AP7)

uniformly for the seven arbitrary poles. No monotonicity of AP is claimed nor is the polar improperly compared by its sign.

## 5. Full comb via the exact weighted trace

Use sigma=2u/3=21. The audited lemma of COMMON_TRANSFER§6 proves that the trace of the weighted Gram of the rational basis is maximal at confluence. Consequently

    ||e^(sigma y)f||²≤T7||f||²,
    T7=Σ(j=0..6)Σ(k=0..j)binom(j,k)²(2/3)^(2k)/(1/3)^(2j+1)
      =176673441.

operatornorm≤trace is used; monotonicity of the maximal weighted eigenvalue is neither needed nor claimed. The value T7 is exactly rational and 2sqrt(T7)<26600.

By shifted Cauchy–Schwarz, |c_f(log q)|≤sqrt(T7)q^-21||f||². Then, with Lambda(q)≤logq and sqrt(q)>=sqrt2>7/5,

    |Comb[f]|/||f||²
      ≤26600 Σ(q>=2)(log q)q^-21.5
      <26600(5/7)Σ(q>=2)(log q)q^-21.

The function (log x)x^-21 decreases for x>=2. Sum–integral comparison and log2<7/10 give

    Σ(q>=2)(log q)q^-21
      ≤2^-21[7/10+14/200+2/400]
       =31/(40·2^21).

The rational product 26600(5/7)31/(40·2^21)<1/125. Combining with AP7,

    W[f]>(1/100−1/125)||f||²=(1/500)||f||².

ALL contacts have been included, not a truncation of the comb.

## 6. Verification and scope

The executed verifier gives PASS for the interval pivots, polar norm, 196 panels, transport margin, exact trace and comb cost. It reuses only the explicit rational module of constants, which also accompanies the previous certificates.

Seven poles remain a finite class. No sign in all orders nor closure of Paper46 is claimed. The large-order Tate test and the twelve-dimensional arithmetic block keep their different problem: they are not resolved by extrapolating AP7.
