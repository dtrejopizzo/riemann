# POWER_FOUR_GLOBAL_009 — Uniform sign on ALL spaces of four real poles >=63/2

Status: PROVED, with previously certified confluent rational input. The exact scalar and constant verification is in tools/power_four_global_009_verify.py. Papers untouched.

## 1. Result and scope

Let v_1,...,v_4>=63/2, allowing multiplicities, and f a non-zero real function whose Laplace transform is P(s)/Π_j(s+v_j), with degree P<4. Then the complete form of the line satisfies

    W[f]>(2/25)||f||².                                    (FOUR)

In particular, for any four exponents a_i>=32 and real coefficients c_i, the exterior form is positive on rho(X)=Σ_i c_i X^-a_i when its image is non-zero. The coefficients of the image are c_i zeta(a_i); there is no separation restriction nor upper bound on rates. All confluent limits are also included.

The transport proved is NOT monotonicity of arch+polar quotients: that general statement was falsified. A lower coercive bound is transported keeping a strictly positive remainder, via an estimate of the spectral sector where the multiplier is negative.

## 2. Corpus and new difference

Consulted the ROUTES-TRIED-INDEX index, grid, crossword and memos POWER_POLE_MOVEMENT_004, POWER_POLAR_MOVEMENT_005, POWER_HIGH_ORDER_PM_NOGO_007, POWER_CONFLUENT_FOUR_005. Archimedean monotonicity, the confluent certificate and the local derivative were already available. The exact difference is a GLOBAL inequality for the complete rational filter, which does not require a favourable sign of the polar derivative. It is not a new parametrization of the problem nor a campaign of rate certificates.

## 3. Already proved confluent inputs

Fix u=63/2. The certificate POWER_CONFLUENT_FOUR_005 and its rational verifier prove, for every f0 in the confluent space of four poles u,

    AP[f0]:=Arch[f0]+Polar[f0]>(49/200)||f0||².             (BASE)

In that Laguerre basis, the two polar moment vectors have squared norms

    AA=(63/31²)Σ_{j=0}³(32/31)^{2j},
    BB=(63/32²)Σ_{j=0}³(31/32)^{2j}.

4AA BB<1 is verified rationally. By Cauchy--Schwarz,

    |Polar[f0]|<||f0||².                                  (PB)

The bound does not destroy the positive polar in BASE; it will only be applied to its SMALL relative variation under the filter.

## 4. Two scalar inequalities of the multiplier

With c=1/10, one has

    m(tau)>=c if tau²>=81,
    tau²(c-m(tau))_+<23 for all tau.                    (NEG)

Proof by rational sums. First m(0)>-11/2. It suffices to use gamma<3/5, pi<22/7, log2<7/10 and logpi<23/20; the sum of their upper bounds is 759/140<11/2. These bounds are verified elementarily: gamma<H32-log32<3/5 using three atanh terms giving log2>693/1000; log2<25/36<7/10 by a geometric tail; and Σ_{k=0}^6(23/20)^k/k!>22/7 implies logpi<23/20.

For x=tau²>=0, the first sixteen terms of the digamma series give

    m(tau)>ell(x):=-11/2+Σ_{k=0}^{15}x/[a_k(4a_k²+x)],
    a_k=k+1/4.

ell is increasing. Exact rational evaluation proves

    ell(4)>-4/3, ell(16)>-3/5, ell(32)>-1/4,
    ell(64)>2/25, ell(81)>1/10.

Thus m>=c for x>=81. On the five intervals with endpoints 0,4,16,32,64,81, x(c-m)_+ is bounded by the right endpoint multiplied by c minus the lower bound at the left endpoint. The resulting rational bounds are

    112/5, 344/15, 112/5, 112/5, 81/50,

all less than 23. This proves (NEG) without tables or numerical sweep.

## 5. Global filter and preservation of coercivity

For f with rates v_j>=u, use the SAME numerator to define

    F0(s)=P(s)/(s+u)^4, F(s)=H(s)F0(s),
    H(s)=Π_j(s+u)/(s+v_j).

Define

    R(tau)=|H(i tau)|²,
    R0=R(0)=Π_j u²/v_j²,
    r0=H(-1/2)H(1/2)=Π_j(u²-1/4)/(v_j²-1/4).

All are positive. For x=tau²,

    1<=R(tau)/R0<= (1+x/u²)^4,
    r0/R0 >=(1-1/(4u²))^4>=1-1/u².                       (FILTER)

The second line uses Bernoulli; moreover r0<=R0. Put

    K=[(1+81/u²)^4-1]/81.

By convexity of the polynomial, for 0<=x<=81,

    (1+x/u²)^4-1<=Kx.

The exact change of the form with respect to the target bound c is

    AP[f]-c||f||²
     =R0(AP[f0]-c||f0||²)
       +(1/2pi)∫(R-R0)(m-c)|F0(i tau)|²d tau
       +(r0-R0)Polar[f0].                                 (ID)

The polar is not compared separately with an assumed sign. Outside tau²<=81, the additional integrand is non-negative by (NEG) and R>=R0. Inside, (NEG) and FILTER bound it below by -23KR0||f0||². By (PB), the polar variation is >=-R0||f0||²/u². Finally BASE implies

    AP[f]-c||f||²
      >R0[49/200-c-23K-1/u²]||f0||².

The constant in brackets satisfies the exact rational inequality

    49/200-1/10-23K-1/u²>3/100>0.                         (MARGIN)

Since R0>0 and f0 is non-zero,

    AP[f]>(1/10)||f||²                                    (AP4)

for ALL rates v_j>=u, even arbitrarily large. The target norm of f already appears in (ID), so uniformity is not lost when R0 is small.

## 6. Complete comb, uniformly in the four rates

The weighted inequality previously proved via all-pass bases is

    ||exp(uy/2)f||²<=B4||f||², B4=(25^4-1)/12=32552.

It requires neither an upper bound nor separation of the poles. By Cauchy--Schwarz,

    |c_f(t)|<=sqrt(B4)exp(-ut/2)||f||².

Thus, using sqrt(B4)<181, Lambda(q)<=logq<=q and (u-1)/2>15,

    |Comb[f]|/||f||²
       <=362Σ_{q>=2}q^-15
       <=362/28672 <13/1000.

Combining with (AP4),

    W[f]>(1/10-13/1000)||f||²
         =(87/1000)||f||²>(2/25)||f||².

(FOUR) is proved. The comb has not been truncated: the bound controls the complete infinite sum.

## 7. What is not extrapolated

The proof uses four poles both in BASE and in the exponent of the filter and B4. For growing dimension, the filter bound and the cost of the comb change and BASE may fail without positive arithmetic contribution (the dimension-twelve test already needs it). Hence the global closure of dimension four does not prove the sign at all orders nor close the paper.
