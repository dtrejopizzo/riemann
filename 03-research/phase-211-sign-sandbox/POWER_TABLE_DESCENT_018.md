# POWER_TABLE_DESCENT_018 — First TWO differences strictly positive, at all steps

Status: PROVED for all k>=0 and u>=63/2. It does not prove complete monotonicity of the row nor the sign of all rows. Papers untouched.

## 1. Corpus and new reason relative to the structural descent

Read POWER_STATE_017, POWER_DESCENT_016, POWER_INTERIOR_017 §7, POWER_SCALAR_BRIDGE_017 and TATE_CHAIN/PACKET_SCOPE009; consulted index/grid/crossword looking for first differences, row N=2 and complete monotonicity. The exact recurrence and the eventual properties do not suffice by themselves, as W4 of 016 shows.

The new difference is to prove TWO levels of descent at ALL steps, using the real multiplier, two explicit bounds for digamma derivatives, the uniform weighted bound of 017 and the exact alternating sign of the polar. No sign is deduced from an identity and no campaign of certificates for finite k is repeated.

Set F_{N,k}(s)=s^k/(s+u)^{N+k}, a_{N,k}=W[f_{N,k}], c_k=binom(2k,k)/4^k. We prove

    W[f_{2,k}]>(1/8)||f_{2,k}||²,
    W[f_{3,k}]>(1/8)||f_{3,k}||², all k>=0,u>=63/2.     (ROWS23)

By the complete recurrence, this implies NEW quantitative inequalities:

    a_{1,k}-a_{1,k+1}>c_k/[32u(k+1)],
    a_{1,k}-2a_{1,k+1}+a_{1,k+2}
                        >3c_k/[64u(k+1)(k+2)].           (DIFF)

Thus the row of unnormalized values a_{1,k} is strictly decreasing and strictly convex in ALL k, not only eventually.

## 2. Exact recurrence and norms

With Q=s/(s+u), L=u/(s+u), the complete identity 016 gives

    a_{N,k}=a_{N,k+1}+u²a_{N+1,k}.

By induction u^{2(N-1)}a_{N,k}=(-Δ)^{N-1}a_{1,k}. This part alone imposes no sign. The exact beta norms satisfy

    ||f_{N,k}||²/||f_{N,0}||²
      =c_k/binom(k+N-1,N-1),
    ||f_{2,k}||²=c_k/[4u³(k+1)],
    ||f_{3,k}||²=3c_k/[8u^5(k+1)(k+2)].

(DIFF) is obtained from (ROWS23) and these norms, without extrapolating an inequality between normalized quotients.

## 3. Archimedean part: two bounds for all orders k

For each fixed N,u, the change k->k+1 reweights the spectral probability by tau²/(u²+tau²). Positive covariance with m proves that Arch[f_{N,k}]/||f_{N,k}||² does not decrease with k. It then suffices to bound k=0.

Let d(u)=psi((u+1/2)/2)-logpi. Differentiating the archimedean integral of the exponential, keeping the norm, gives

    A_{2,0}=d-u d',
    A_{3,0}=d-u d'+(u²/3)d''.

The polygamma series and comparative integration give, for x>0,

    psi'(x)<=1/x+1/x²,
    psi''(x)>=-2/x³-1/x².

With x=(u+1/2)/2, for all u>=63/2,

    u d'<=1+2/u<=67/63,
    (u²/3)d''>=-1/3-4/(3u)>=-71/189.

Moreover d increases because psi'>0, and the rational interval already proved in 017 verifies d(63/2)>159/100>3/2. Therefore

    A_{2,k}>=A_{2,0}>3/2-67/63>2/5,
    A_{3,k}>=A_{3,0}>159/100-67/63-71/189
                              =2851/18900>3/20.          (ARCH)

Monotonicity of AP under motion of poles, which is false in general, was not used: the uniformity in u comes from these explicit bounds on each component.

## 4. Effective control of the infinite comb, uniform in ALL k

Use WRN of 017 with eta=15, a=u-15, rho=(15/a)². Its constants for N=2,3 are

    R2=(u/a)^3(1+rho)/(1-rho)²,
    R3=(u/a)^5(1+2rho-rho²/3)/(1-rho)³.

The representation by series with positive coefficients of 017 shows that both constants decrease as u>=63/2 increases. At u=63/2,

    R2=4641/11, 2sqrt(R2)<42,
    R3=15658881/1331, 2sqrt(R3)<220.

Since ||e^{15y}f||²<=R_N||f||², the same autocorrelation bound used in 017 gives, for ALL k and all those u,

    |Comb[f_{2,k}]|/||f_{2,k}||²
       <42Σ_{q>=2}q^-14<=42*15/[13*2^14]<3/1000,
    |Comb[f_{3,k}]|/||f_{3,k}||²
       <220Σ_{q>=2}q^-14<=220*15/[13*2^14]<1/60.         (PRIME)

The whole comb is kept with its real coefficients: only Lambda(q)<=logq<=q and the convergent integral tail were used, without truncation or the assumption that each contact helps.

## 5. The alternating sign of the polar allows the second descent

For any N,k,

    Polar[f_{N,k}]=2(-1/4)^k/(u²-1/4)^{N+k}.

Let p_{N,0}=Polar[f_{N,0}]/||f_{N,0}||²>0 and q=1/(4u²-1). The beta norms of §2 give

    |Polar[f_{N,k}]|/||f_{N,k}||²
      =p_{N,0}q^k binom(k+N-1,N-1)/c_k.

By c_k>=2^-k and binom(k+N-1,N-1)<=N^k (counting multisets versus ordered sequences), this is <=p_{N,0}(2Nq)^k. The prefactors p_{N,0} and q decrease with u; for p_{N,0}, the logarithmic derivative has numerator -u²-(2N-1)/4<0.

For N=2, p_{2,0}=8u³/(u²-1/4)²<13/50 and 4q<1, so the whole polar has normalized absolute value <13/50.

For N=3 the positive sign of even k is not wasted. For odd k one has k>=1 and 6q<1. At the endpoint u=63/2,

    p_{3,0}=32u^5/[3(u²-1/4)^3]<7/20,
    p_{3,0}(6q)<(7/20)*(6/3968)<1/1000.

Thus, for ALL k, the polar of N=3 is >=-(1/1000)||f||²; for even k it is even nonnegative. This preservation of its sign avoids the excessively large loss that bounding the whole polar of N=3 by p_{3,0} would give.

## 6. Closure and scope of the descent

From ARCH, PRIME and §5,

    W[f_{2,k}]/||f_{2,k}||²
       >2/5-13/50-3/1000=137/1000>1/8,
    W[f_{3,k}]/||f_{3,k}||²
       >3/20-1/1000-1/60=397/3000>1/8.

(ROWS23) and (DIFF) are proved. The verifier tools/power_table_descent_018_verify.py checks the constants with Fraction and the previous rational intervals; it contains no sampling in k nor a numerical spectrum.

Only the first two levels of differences were obtained. Neither complete monotonicity of a_{1,k}, nor the sign of N>=4, nor the complete table needed in the scalar bridge is inferred. The information that distinguishes the real multiplier from the shifted W4 of 016 is explicit in (ARCH) and its balance with PRIME/POLAR. The row generator and the recurrence are still identities; the new contribution is their quantitative sign at all steps of these two levels.
