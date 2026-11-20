# POWER_SIGNED_TRANSFER_014 — Preserving the signed gain through a numerator zero; global sign for eight poles

Status: PROVED, with small rational certificates. Verifier: tools/power_signed_transfer_014_verify.py. Papers untouched.

## 1. Result

In EVERY rational space of eight real poles v_j>=63/2, with multiplicities allowed, the full form satisfies

    W[f]>(1/1000)||f||², f real nonzero.                   (EIGHT)

Here this is equivalent to positivity for any mixture of eight exterior powers with exponents >=32, with no minimal separation or upper bound, and for their confluent limits. No sign is claimed at all orders.

## 2. Corpus and difference from the limit of 013

The index/grid/crossword were consulted for zero numerators, constrained arch, telescoping filters and signed transfer; POWER_POLE_MOVEMENT_004, POWER_DEFICIT_LIMIT_013 and POWER_COMMON_TRANSFER_010 were read. The filter identities are known; no automatic sign is attributed to them. The new difference is the DECOMPOSITION of the whole signed spectral correction into energies of rational functions having a FORCED NUMERATOR ZERO at s=0. The archimedean part is coercive on that concrete subspace, even though its multiplier is negative near the origin.

The pointwise loss excluded by 013 is not optimised. The integral is kept with both signs and the real restriction of its spectral density is used; that is precisely the information the earlier NO-GO discarded.

## 3. Positive identity for the filter difference

Fix u>1/2 and dimension n. Let v_j>=u, P a real polynomial of degree less than n, and

    F0(s)=P(s)/(s+u)^n,
    F(s)=P(s)/Π_j(s+v_j)=H(s)F0(s).

With x=tau², define R=|H(i tau)|², R0=Π_j u²/v_j² and

    A_j(x)=(1+x/u²)/(1+x/v_j²), R/R0=Π_j A_j.

Telescoping Π_j A_j-1=Σ_j(A_j-1)Π_{k<j}A_k and keeping the rational density gives EXACTLY

    (R-R0)|F0(i tau)|²
      =R0 Σ_{j=1}^n kappa_j |G_j(i tau)|²,                (TEL)

where

    kappa_j=[(v_j²-u²)/u²]Π_{k<j}(v_k²/u²)>=0,
    G_j(s)=sP(s)/[(s+u)^{n-j+1}Π_{k<=j}(s+v_k)].

Each G_j has n+1 real poles >=u, numerator of degree <=n and numerator ZERO at s=0. Here G_j(0)=0 is the evaluation of the LAPLACE TRANSFORM, equivalent to zero time integral; it does not mean that the time function vanishes at y=0. Verifying (TEL) amounts to multiplying denominators: A_j-1=x(v_j²-u²)/[u²(x+v_j²)]. No filter is approximated and no pointwise supremum is taken.

## 4. New operator inequality: archimedean coercivity on the zero numerator

Suppose that, in the confluent space of n+1 poles u restricted to Q(0)=0, one has proved

    Arch[g]>=gamma||g||².                                (CZ)

The archimedean monotonicity of POWER_POLE_MOVEMENT_004 applies on that SAME space of numerators Q of degree <n+1 with Q(0)=0: moving poles only reweights by an increasing function of |tau| and does not alter the restriction Q(0)=0. Hence (CZ) holds for all n+1 poles >=u and, in particular, for each G_j of (TEL).

For any c<=gamma, integrating (TEL) against m-c proves the NEW inequality

    ∫(R-R0)(m-c)|F0|²/(2pi)
      =R0 Σ_j kappa_j(Arch[G_j]-c||G_j||²)
      >=R0(gamma-c)Σ_j kappa_j||G_j||²>=0.                (SIGNED)

The negative frequency is not eliminated: its cost stays inside an archimedean energy that is positive on average thanks to the rational structure and the numerator zero. (SIGNED) is an inequality on the exact filters, not a renaming of an unsigned identity.

## 5. General signed criterion with polar

Suppose in addition, in the confluent space of n poles u,

    AP[f0]>=b||f0||², |Polar[f0]|<=p||f0||².

Define eta_n=1-(1-1/(4u²))^n<=n/(4u²). As before, r0=H(-1/2)H(1/2) satisfies R0>=r0>=R0(1-eta_n). Using the exact transport identity and (SIGNED),

    AP[f]-c||f||²
       >=R0[(b-c-p eta_n)||f0||²
             +(gamma-c)Σ_j kappa_j||G_j||²].              (GAIN)

Thus, if gamma>=c and b-c-p eta_n>0, one gets AP[f]>=c||f||² for ALL spaces of n poles >=u. This rule keeps the positive spectral gain and the polar change in a single inequality. It does not presuppose monotonicity of AP under individual moves, which fails in arbitrary dimension.

## 6. Concrete certificates n=8, u=63/2

The verifier computes by rational intervals the nine required confluent archimedean bands and the exact polar bands. For g(s)=[psi((s+1/2)/2)-log pi]/2, the archimedean diagonal is 2g(u), and band k>=1 is

    Σ_{j=1}^k g^(j)(u)(2u)^j binom(k-1,j-1)/j!.

Polar band k is [2u/(u²-1/4)](-1)^k[(32/31)^k+(31/32)^k]. The derivatives of psi at 16 are computed with rational sums up to 2000 and integral tails; gamma, pi and logarithms use the already audited intervals of fixed_grid_003. No numerical special functions are used.

### Full eight-pole basis

The interval LDL of AP8-(7/200)I has eight pivots with positive lower endpoint. Hence b=7/200 is valid. The polar vectors have squared norms

    AA=(63/31²)Σ_{j=0}^7(32/31)^{2j},
    BB=(63/32²)Σ_{j=0}^7(31/32)^{2j}.

The rational inequality 4AA BB<(3/2)² allows taking p=3/2.

### Restricted nine-pole archimedean block

In the orthonormal Laguerre basis, F_j(0)=sqrt(2/u)(-1)^j. Therefore Q(0)=0 is equivalent to Σ_{j=0}^8(-1)^j x_j=0. A rational basis of that subspace is

    B_i=e_i-(-1)^i e_8, i=0,...,7.

Its Gram is I+aa^t with a_i=(-1)^i. Interval LDL elimination of

    B^t Arch9 B-(1/4)B^t B

has eight pivots with positive lower endpoint. Thus (CZ) holds with gamma=1/4. It is a form inequality on the WHOLE subspace, not the evaluation of a particular vector.

### Uniform signed margin

Take c=3/100. The rational constants satisfy

    gamma>c,
    7/200-3/100-(3/2)*8/3969>1/1000>0.

By (GAIN), AP[f]>(3/100)||f||² for ALL eight poles >=63/2.

## 7. Infinite comb using the exact weighted trace

POWER_COMMON_TRANSFER_010 §6 shows, with independent review, that the weighted trace is maximal at confluence. For 0<alpha<1, sigma=alpha u, one may use uniformly

    ||exp(sigma y)f||²<=T_n(alpha)||f||²,
    T_n(alpha)=Σ_{j=0}^{n-1}
       [Σ_{k=0}^j binom(j,k)^2 alpha^{2k}]/(1-alpha)^{2j+1}.

With n=8, alpha=3/5, sigma=189/10 and beta=sigma+1/2=97/5, the rational verifier proves 4T8<25000². Therefore

    |Comb[f]|/||f||²<=25000Σ_{q>=2}(logq)q^-beta.

The integral comparison for the decreasing function (logx)x^-beta gives

    Σ_{q>=2}(logq)q^-beta
       <=2^-beta[log2+2log2/(beta-1)+2/(beta-1)²].

Use beta-1>18, log2<7/10 and 2^-2/5<19/25, whose last proof is the integer inequality 25^5<4*19^5. The rational bound follows

    |Comb[f]|/||f||²
       <25000*(19/25)*2^-19[7/10+14/180+2/324]
       <29/1000.

The sum includes ALL prime powers; no favourable signs were assumed and no unestimated tail was discarded. Finally

    W[f]>(3/100-29/1000)||f||²=(1/1000)||f||².

This proves (EIGHT).

## 8. Scope and next node

The general rule depends on two distinct blocks: confluent AP of order n and confluent Arch of order n+1 restricted to zero numerator. Both were fully verified for n=8. It is not claimed that their margins persist at all orders: the dimension-twelve test with negative AP still stands and eventually forces keeping favourable arithmetic. The result overcomes the pointwise obstacle of 013 through a concrete coupled inequality, without contradicting it.

Reproducible command: `python3 03-research/phase-211-sign-sandbox/tools/power_signed_transfer_014_verify.py`. It uses only integers and Fraction; it verifies the two blocks by interval LDL, the polar norm, the signed margin and the infinite cost of the comb.

## 9. Exact identity for the FULL form: the polar is also absorbed into the summands

The rational identity (TEL) has a further algebraic extension, independent of the order-eight certificate. For real numerators, replace |F(i tau)|² by F(s)F(-s) and x=tau² by -s². Since all poles are greater than 1/2, one may evaluate at s=1/2 without singularities. This gives

    Σ_j kappa_j Polar[G_j]=(r0/R0-1)Polar[f0].              (POLTEL)

Indeed the factor s in the numerator of G_j produces s*(-s)=-1/4, exactly the sign of the polar member of (TEL) at x=-1/4. This is not a pointwise evaluation of a positive spectral measure: it is an identity between rational functions.

Integrating (TEL) against m and against each cos(tau logq) keeps the archimedean part and each prime atom. The sums of the atoms converge absolutely for these rational data with poles >1/2, since each autocorrelation is a finite polynomial times an exponential. Adding (POLTEL), one gets

    W[f]-c||f||²
       =R0[(W[f0]-c||f0||²)
              +Σ_j kappa_j(W[G_j]-c||G_j||²)].             (FULL)

Also ||f||²=R0[||f0||²+Σ_j kappa_j||G_j||²], by (TEL) integrated against one. (FULL) has no polar loss: it keeps it exactly inside the forms W[G_j], together with all the arithmetic.

Hence a full criterion is: if the confluent basis of order n and ALL spaces of n+1 poles >=u restricted to zero Laplace transform at s=0 have W>=c||.||², then the same holds for all spaces of n poles >=u. The second premise has not been proved here at all orders. Its statement keeps Λ and the autocorrelations with both signs, unlike an argument using only the positivity of the arithmetic coefficients.

For a single changed pole, with rho=u²/v², (FULL) simplifies to

    W[f_v]=rho W[f_u]+(1-rho)W[sF_u(s)/(s+v)].             (ONE)

This one-pole identity agrees with the independent derivation of the case analysis. Its iteration, the normalisation of the mixture and strong convergence are developed in POWER_GEOMETRIC_TRANSFER_015; eventual positivity of the high-pass blocks is treated separately in POWER_HIGHPASS_015.
