# POWER_DEFICIT_LIMIT_013 — Exact limit of separable transport by pointwise deficit at order eight

Status: PROVED (NO-GO for a precise class of estimates). It is not a counterexample to the sign nor to transport that keeps couplings. Papers untouched.

## 1. Declared class and new reason

Consulted index/grid/crossword for deficit limit, pointwise deficit, separable transport and discarded positive gain; reviewed POWER_FOUR_GLOBAL_009, POWER_SIX_GLOBAL_011 and the general transport criterion. This note identifies where the mechanism that closed the small-dimension cases stops sufficing. It does not retry or classify other routes of the paper.

Fix u=63/2, n=8. The class considered transports from the confluent base using:

1. A scalar constant b such that AP[f0]>=b||f0||² for EVERY numerator of degree less than eight.
2. A target c>=0.
3. The uniform envelope R/R0<=(1+x/u²)^8, x=tau².
4. It discards all gain at frequencies m>=c and bounds the negative loss independently of the spectral distribution of the numerator.
5. It bounds the polar variation by an independent non-negative loss.

The estimate of 011 additionally uses X,D with m>=c for x>=X and x(c-m)_+<=D, and the product D K8, K8=[(1+X/u²)^8-1]/X. It will be proved that NOT EVEN optimizing X,D,c,b up to their true values can close this class at order eight. Estimates that retain the positive gain or the rational spectral measure are not excluded.

## 2. A rational vector gives b<1/25

In the orthonormal Laguerre basis of eight poles u, take

    v=(169,-310,405,-460,460,-405,310,-169).

It is an explicit rational vector of dimension eight. Its arch+polar quotient strictly satisfies

    0<AP[v]/||v||²<1/25.                                 (B8)

The verifier tools/power_deficit_limit_013_verify.py computes the eight Toeplitz bands by the already proved Gamma+polar formula. The derivatives psi^(j)(16), j<=7, are enclosed by summing rational powers up to 2000 and using integral tails. Gamma, pi and logarithms use the rational intervals of fixed_grid_003. The evaluation of the vector is exact interval arithmetic, without computing numerical eigenvalues to certify.

A single eigenvector discovery computation produced the above vector by rounding; it plays no role in the final proof and there was no sweep over rates. By the variational principle, any b valid in item 1 of the declared class must satisfy b<1/25.

## 3. One frequency requires a loss greater than 1/20

We prove exactly

    m(4)<-2/5.                                           (M4)

To verify it, use m(0)=-gamma-pi/2-3log2-logpi with the previous intervals, and sum the first 32 positive terms of digamma at x=16. The tail is at most

    (x/4)Σ_{k>=32}(k+1/4)^-3
       <=x/[8(125/4)^2].

The rational upper endpoint obtained is less than -2/5. The comparison does not depend on a graph nor on a rounded approximation of m.

On the other hand the rational inequality

    (2/5)[(1+16/u²)^8-1]>1/20                            (LOSS)

is verified exactly. For any c>=0, (M4) implies that the smallest loss constant obtainable using ONLY the uniform pointwise envelope satisfies

    sup_{x>=0}[(1+x/u²)^8-1](c-m(sqrt x))_+
       >(2/5)[(1+16/u²)^8-1]>1/20.

The envelope really is the pointwise supremum of R/R0 when all the new poles tend to infinity. Hence there is no uniform pointwise envelope strictly smaller than the one used here for all poles v_j>=u. It is not claimed that a rational numerator of degree seven can concentrate arbitrarily at that frequency: precisely that measure restriction is information that the declared class discards.

### Theorem for the DIRECT pointwise loss

Define, without splitting the product into two constants,

    L8(c)=sup_{x>=0}(c-m(sqrt x))_+[(1+x/u²)^8-1].

For ANY c>=0, the evaluation x=16 already proves L8(c)>1/20. Combining with (B8), for every valid b and every polar loss p_loss>=0,

    b-c-L8(c)-p_loss <1/25-1/20=-1/100.

Hence the estimate that directly optimizes the complete pointwise product is also excluded. The NO-GO is not limited to the D K8 separation nor to a particular partition of panels. It is the replacement of the negative integral by a pointwise supremum independent of the numerator, discarding the positive gain, that produces the obstacle.

## 4. Impossibility of optimizing the constants of the D K8 criterion

Every valid choice X,D must have X>16, since m(4)<0<=c. Moreover

    D>=16(c-m(4))>16*(2/5).

Convexity of x->(1+x/u²)^8-1, which vanishes at zero, gives

    K8>=[(1+16/u²)^8-1]/16.

By (LOSS), D K8>1/20. Even granting ZERO polar loss, the maximal margin of the criterion is

    b-c-D K8 <1/25-1/20=-1/100<0.

Hence the criterion cannot certify order eight, even if all panels, tails, gamma bounds or constants of the negative part are optimized. The same failure holds for the version with the best exact pointwise loss instead of the product D K8.

## 5. Operational interpretation and limits

This result avoids an indefinite prolongation of constant optimizations within the same separable estimate. At order eight some discarded information must be retained: gain at the frequencies m>=c, spectral distribution of the numerator, coupling with the polar, specific filters of the rates or favourable arithmetic contribution.

It is NOT proved that AP[v]<0: the certificate vector has POSITIVE AP. Nor is W[v]<0 proved, nor is a finer global sign transport excluded. The failure belongs to the estimate that replaces the cost by its worst pointwise value independently of the vector.

Command: `python3 03-research/phase-211-sign-sandbox/tools/power_deficit_limit_013_verify.py`. It verifies (B8), (M4) and (LOSS) via integers and Fraction; it contains no numerical special functions, optimizers or floating point.
