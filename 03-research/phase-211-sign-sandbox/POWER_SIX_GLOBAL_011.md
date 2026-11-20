# POWER_SIX_GLOBAL_011 — General deficit-transport criterion and global six-pole sign

Status: PROVED. Fully rational verifier: tools/power_six_global_011_verify.py. Papers untouched.

## 1. Result

For any rational space of SIX real poles v_j>=63/2, with multiplicities allowed, the full form satisfies

    W[f]>(1/25)||f||², f nonzero.                          (SIX)

All mixtures of six exterior powers with exponents a_i>=32 and all confluent limits are included. There is no minimal separation nor upper bound on the poles. The comb is controlled in full, without truncation.

The proof applies a deficit-transport criterion valid for any declared dimension, with constants that must be verified in each case. It does not claim a uniform sign in arbitrary dimension.

## 2. Antecedents and difference

The index/grid/crossword and POWER_FOUR_GLOBAL_009, POWER_CONFLUENT_FOUR_005, POWER_HIGH_ORDER_PM_NOGO_007 were consulted. Arch+polar monotonicity is not attempted again: the coercive transport of 009 is used and its control of the negative sector is refined. The difference is obtaining an explicit quantitative rule for n and verifying it at n=6; the coefficient .12 of the confluent case is certified by rational remainders, not presupposed from the diagnosis. There is no sweep over rates.

## 3. General deficit-transport criterion

Fix u>1/2 and dimension n. Suppose in the confluent space of n poles u:

    AP[f0]>=b||f0||², |Polar[f0]|<=p||f0||².

Suppose moreover constants c, X>0 and D>=0 such that

    m(tau)>=c for tau²>=X,
    tau²(c-m(tau))_+<=D.

Define

    K_n=[(1+X/u²)^n-1]/X,
    eta_n=1-(1-1/(4u²))^n <=n/(4u²).

If

    b-c-D K_n-p eta_n>0,                                 (CRIT)

then AP[f]>=c||f||² for ALL spaces of n real poles v_j>=u.

Proof. For the same rational numerator use F0=P/(s+u)^n and F=H F0 with H=Π_j(s+u)/(s+v_j). Write R=|H(i tau)|², R0=R(0), r0=H(-1/2)H(1/2). Then

    1<=R/R0<=(1+tau²/u²)^n,
    1>=r0/R0>=(1-1/(4u²))^n.

The exact identity is

    AP[f]-c||f||²
     =R0(AP[f0]-c||f0||²)
      +∫(R-R0)(m-c)|F0|²/(2pi)
      +(r0-R0)Polar[f0].

The first correction can only hurt in tau²<=X. By convexity, there R-R0<=R0 K_n tau², so it costs at most R0 D K_n||f0||². The polar variation costs at most R0 p eta_n||f0||². (CRIT) proves the claim, keeping the TARGET norm of f in the identity. There is no incorrect division by R0 nor any need to compare R0 with the final norm.

## 4. General improvement of the weighted control by all-pass filters

This observation improves the earlier Young estimate. For 0<alpha<1, sigma=alpha u, let

    r=(1+alpha)/(1-alpha),
    B_n(alpha)=[1/(1-alpha)]Σ_{j=0}^{n-1}r^{2j}.

On every space of n poles >=u,

    ||exp(sigma y)f||²<=B_n(alpha)||f||².                  (WT)

Proof. In the orthonormal rational basis, each all-pass factor is (s-v)/(s+v). After weighting by exp(sigma y), Plancherel evaluates it at s=-sigma+i tau, and its multiplier norm is

    sup_tau |(i tau-sigma-v)/(i tau-sigma+v)|
       =(v+sigma)/(v-sigma)<=(1+alpha)/(1-alpha).

The normalised initial exponential has squared weighted norm v/(v-sigma)<=1/(1-alpha). The bounds are multiplied for each basis member and Cauchy--Schwarz is applied to the orthonormal coefficients. This proves (WT) even with repeated rates.

Consequently

    |Comb[f]|<=2sqrt(B_n(alpha))
          *Σ_{q>=2}Lambda(q)q^{-(sigma+1/2)} ||f||².        (PC)

Thus (CRIT) and any bound from (PC) smaller than c produce the full sign on the whole rate domain. The improvement r replaces the larger factor obtained by summing the L1 norms of the delta and the exponential: here the filter multiplier is kept exactly.

## 5. Confluent certificate n=6, u=63/2

The verifier obtains by rational intervals the six bands of the arch+polar Toeplitz matrix. Use

    g(s)=[psi((s+1/2)/2)-log pi]/2, r0=32/31.

The diagonal is 2g(u)+4u/(u²-1/4), and the bands k=1,...,5 are

    Σ_{j=1}^k g^(j)(u)(2u)^j binom(k-1,j-1)/j!
       +[2u/(u²-1/4)](-1)^k(r0^k+r0^-k).

The derivatives of psi at 16 are computed as

    psi^(j)(16)=(-1)^{j+1}j!Σ_{m>=16}m^{-j-1}.

The terms m<=2000 are summed and the tail is enclosed between the integrals from 2001 and from 2000. Gamma, pi and the logarithms use the rational intervals of power_fixed_grid_003, with series and explicit remainders already audited. The INTERVAL LDL elimination of AP-(3/25)I has six pivots with positive lower endpoint. Certified:

    AP[f0]>(3/25)||f0||².                                 (BASE6)

The polar moments satisfy, exactly,

    AA=(63/31²)Σ_{j=0}^5(32/31)^{2j},
    BB=(63/32²)Σ_{j=0}^5(31/32)^{2j}, 4AA BB<1.

Hence one can use p=1.

## 6. Negative sector with small constant

The rational intervals of the constants prove m(0)>-5373/1000. With the same sixteen digamma terms,

    ell(x)=-5373/1000+Σ_{k=0}^{15}x/[a_k(4a_k²+x)], a_k=k+1/4,

one has m(tau)>ell(tau²), and ell is increasing. The verifier checks

    ell(49)>1/20,
    x(1/20-m(tau))_+<9, x=tau².

For the second inequality only the 25 panels with endpoints

    0,1/4,1,2,3,4,6,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,28,32,40,49

are needed. On each panel [a,b], b*(1/20-ell(a))_+ is compared with 9 using Fraction. For x>=49 the multiplier already exceeds 1/20. These are exact scalar inequalities of the single multiplier; they are not sampled certificates over rates.

With b=3/25, c=1/20, D=9, X=49, n=6, p=1, the verifier checks

    3/25-1/20-9[(1+49/u²)^6-1]/49-6/(4u²)>3/500>0.

The general criterion gives AP[f]>(1/20)||f||² for ALL six rates >=u.

## 7. Comb and closure of the six case

In (WT) choose alpha=3/4. Then sigma=189/8, r=7, and

    B6=4Σ_{j=0}^5 49^j=(49^6-1)/12=1153440600,
    2sqrt(B6)<68000, sigma+1/2>24.

Since Lambda(q)<=logq and (logx)x^-24 decreases for x>=2,

    Σ_{q>=2}(logq)q^-24
      <=2^-24[log2+2log2/23+2/23²].

Using log2<7/10, the bound multiplied by 68000 is less than 1/250. By (PC),

    |Comb[f]|<(1/250)||f||².

Finally W[f]>(1/20-1/250)||f||²=(23/500)||f||²>(1/25)||f||². (SIX) is proved.

Reproducible command: `python3 03-research/phase-211-sign-sandbox/tools/power_six_global_011_verify.py`. It uses no floating point, optimisers or numerical special functions. It verifies BASE6, the polar norm, the 25 panels, the filter margin and the infinite tail of the comb.

## 8. Limit of the rule

The criterion is a general theorem conditional on b,p,D,X and on its explicit inequality; it does not ensure that those constants exist with margin for all n. The order-twelve test with negative AP prevents directly reusing a positive AP basis there. The weighted improvement helps keep the arithmetic as a loss when that is legitimate, but does not replace the positive compensation of the comb when it is needed.
