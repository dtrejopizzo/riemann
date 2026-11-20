# POWER_FIVE_GLOBAL_010 — Uniform sign for all spaces of five poles >=63/2

Status: PROVED, exact rational certificate executed and independently reviewed in POWER_FIVE_AUDIT_010.md. Papers untouched.

## 1. Theorem and difference with respect to antecedents

Let v_1,...,v_5>=u=63/2, with multiplicities allowed, and f real non-zero with Laplace transform P(s)/Π_j(s+v_j), degree P<5. Then

    W[f]>(1/100)||f||².                                  (FIVE)

In particular this includes arbitrary mixtures of up to five exterior powers X^-a with exponents a>=32 and all their corresponding confluent limits. No separation nor upper bound on rates is required.

Antecedents read: the project rules, index/grid/crossword registered in POWER_BRIDGE_002; POWER_FOUR_GLOBAL_009 and its audit; the confluent certificates and the falsifiers of polar monotonicity. The global transport tool was already invented and proved in FOUR009: NO novelty is attributed to the principle. The substantive difference is a NEW confluent certificate of dimension five and a change of weight in the all-pass control of the comb that allows closing five poles uniformly. Nothing is extrapolated from points nor from the case of four.

## 2. New confluent certificate of dimension five

In the orthonormal basis phi_j=sqrt(63)e^-uy L_j(63y), j0..4, the archimedean matrix is Toeplitz. The diagonal d and the bands b_k are enclosed exactly via

    d=psi16−log pi,
    b_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!.

The polygamma sums are Σ(m>=16)m^(-r-1), with sign (-1)^(r+1), and are bounded by summing m16..255 plus integral tails between 1/[r·256^r] and 1/[r·255^r]. For d the same rational bounds on gamma, pi and log as in CONFLUENT_FOUR005 are used. High-precision remainders are not needed.

The rational centre of the five archimedean bands is

    (1596/1000,1016/1000,−16/1000,349/1000,−154/10000).

Its maximal absolute row-sum error is <1/200. The exact polar has entries

    Polar_jk=63(A_j B_k+B_j A_k),
    A_j=(−32)^j/31^(j+1), B_j=(−31)^j/32^(j+1).

The rational LDL of the central matrix plus Polar minus (39/200)I has five strictly positive pivots, verified by `tools/power_five_global_010_verify.py`. Hence

    AP[f0]:=Arch[f0]+Polar[f0]>(19/100)||f0||²             (BASE5)

for every confluent numerator of degree<5. Moreover, with AA=63ΣA_j² and BB=63ΣB_j², the same script certifies 4AA BB<1. By Cauchy–Schwarz,

    |Polar[f0]|<||f0||².                                  (PB5)

It is not used as a substitute for BASE5: PB5 only controls the small variation of the polar under the filter.

## 3. Transport to five arbitrary rates

Use the same numerator and define F0(s)=P(s)/(s+u)^5 and F(s)=H(s)F0(s), H(s)=Π_j(s+u)/(s+v_j). For x=tau², put

    R(tau)=|H(i tau)|², R0=Π_j u²/v_j²,
    r0=H(−1/2)H(1/2)=Π_j(u²−1/4)/(v_j²−1/4).

Since v_j>=u,

    1≤R/R0≤(1+x/u²)^5,
    1−5/(4u²)≤r0/R0≤1.

The second lower inequality is Bernoulli applied to five factors. FOUR009 proves via rational series of the symbol

    m(tau)≥1/10 for tau²≥81,
    tau²(1/10−m(tau))_+<23.

These bounds also hold replacing 1/10 by c=1/50. Fix K5=[(1+81/u²)^5−1]/81; by convexity of the polynomial expansion, (R−R0)/R0≤K5 x when 0≤x≤81.

The exact transport identity is

    AP[f]−c||f||²
      =R0(AP[f0]−c||f0||²)
       +(1/2pi)∫(R−R0)(m−c)|F0(i tau)|²d tau
       +(r0−R0)Polar[f0].

Outside x≤81 the additional integral is non-negative. Inside it is >−23K5 R0||f0||². By PB5, the polar variation is >−5R0||f0||²/(4u²). BASE5 gives

    AP[f]−c||f||²
      >R0[19/100−c−23K5−5/(4u²)]||f0||².

The bracket is rational and strictly greater than 3/100, as the script verifies. Hence

    AP[f]>(1/50)||f||²                                   (AP5)

uniformly in all rates. No monotonicity of the AP quotient is claimed: only a lower bound is transported keeping a positive remainder. The target term contains the norm of f, so that small R0 does not destroy the uniformity.

## 4. New all-pass weight controlling the whole comb

Use sigma=2u/3=21. In an orthonormal Malmquist basis of five poles v_j>=u, the first normalized exponential has squared norm weighted by e^(2sigma y) bounded by v_j/(v_j−sigma)≤3. Each all-pass factor is the convolution delta−2v_j e^(-v_j y), and its L¹ norm weighted by e^(sigma y) is ≤1+2v_j/(v_j−sigma)≤7.

By weighted Young, the mode j has squared norm ≤3·49^j. Cauchy–Schwarz on the five basis coefficients gives

    ||e^(sigma y)f||²≤B5||f||²,
    B5=3Σ(j=0..4)49^j=(49^5−1)/16.

No separation of poles is required nor is the result lost under multiplicities. Shifted Cauchy–Schwarz gives |c_f(t)|≤sqrt(B5)e^(-sigma t)||f||². Thus, using Lambda(q)≤q, sigma+1/2−1=20.5>20 and 2sqrt(B5)<8404,

    |Comb[f]|/||f||²
      ≤8404Σ(q>=2)q^-20
      ≤8404·2^-20(1+2/19)<1/100.

The sum includes ALL contacts and converges absolutely. Combining with AP5 gives FIVE.

## 5. Verification and limits

The attached script checks BASE5, PB5, the five scalar comparisons of the symbol used by FOUR009, the transport bracket, B5 and the final margin exclusively with Fraction. Executed result: PASS.

Five poles are not all orders. The case of dimension twelve needs a signed arithmetic contribution and is not covered by this AP transport. The present proof does not give a uniform constant as the dimension grows either. The next degree requires its own estimate, not an extrapolation of this theorem.
