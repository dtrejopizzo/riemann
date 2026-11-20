# POWER_ROW_PATTERN_029 — Uniform region u²>=256N, k>=1

Status: **PROVED**, independent review approved and verifier PASS reproduced. For ALL integers N>=2,k>=1 and EVERY positive real rate u with u²>=256N,

    W[f_(N,k)]>(7/10)||f_(N,k)||²,
    F_(N,k)(s)=s^k/(s+u)^(N+k).                            (REGION)

The FULL comb and the polar are kept. No campaign of N, papers untouched. The edge k0 is treated separately in BOUNDARY_WEDGE029 with a stronger condition on u.

## 1. Corpus and precise difference

Read the project rules, JOINT_SCALE016 and its audit (failure of uniform exponential weights with fixed u, large N/u²), INTERIOR017 (WRN), TABLE_DESCENT018, ROW_FOUR028 and ROW_SPLIT028; consulted index/grid/crossword on centred weights, row bounds and beta moments. No sign proof is attributed to the filter identities.

The difference from016 and018 is twofold: using BOTH opposite weights in Cauchy–Schwarz, cancelling the linear cost Neta/u; and letting u grow like sqrt(N), keeping a uniform cost in Neta²/u². The counterexample016 to uniformizing weights with fixed u and unbounded N/u² does NOT belong to this region. The variable condition is not presented as a bridge towards the full table of FIXED rate u31.5. The new conclusion is an explicit region of real W in infinitely many orders, without individual certificates per N.

## 2. Gain of the first column and lower archimedean formula

If A_(N,k)(u)=ARCH_(N,k)/norm², the Poisson recurrence of018 and the beta norms give exactly

    A_(N,1)=A_(N,0)+u A_(N,0)'.                            (GAIN)

The derivation uses I_(N+1)=−I_N'/[2Nu] and norm_(N,1)²=norm_(N,0)²/(2N). The gain is nonnegative: rescaling tau=u xi, the term uA0' is the mean of tau m'(tau)>=0. GAIN does not imply a margin by itself and is not extrapolated to the full form.

To obtain a QUANTITATIVE bound valid at variable orders we first prove, for every nonzero real t,

    Re psi(1/4+it)>=log|t|−9/(8t²).                       (PSI)

Elementary proof: the Euler summation formula, integrated once more via the periodic polynomial B2, is

    psi(z)=logz−1/(2z)−1/(12z²)
            +int_0^infty B2({x})/(z+x)^3 dx,
    |B2({x})|<=1/6,  Re z>0.

For z=a+it, the modulus of the terms after logz−1/(2z) is <=1/(4t²), since |z|>=|t| and int_0^infty |z+x|^(−3)dx<=1/t². Applying at a5/4, using log|z|>=log|t| and Re(1/(2z))<=5/(8t²), and subtracting Re[1/(1/4+it)]<=1/(4t²) via the psi recurrence, proves PSI.

The probability of q=tau²/(u²+tau²) is Beta(k+1/2,N−1/2). Hence

    Elog|tau|=logu+(1/2)[psi(k+1/2)−psi(N−1/2)],
    E tau^(−2)=(N−1/2)/[u²(k−1/2)]       (k>=1).

PSI with t=tau/2 gives the uniform inequality

    A_(N,k)>=log(u/(2pi))+(1/2)[psi(k+1/2)−psi(N−1/2)]
                       −9(N−1/2)/[2u²(k−1/2)].           (ARCH-GENERAL)

This bound keeps a gain that was not accessible using only the minimum k0; the necessary inverse moment is finite from k1. For k>=1 the right-hand side increases with k. Using psi(N−1/2)<=logN, psi(3/2)=2−gamma−2log2 and u²>=256N proves

    A_(N,k)>=2log2−logpi+1−gamma/2−9/256>9/10.             (ARCH)

The last comparison is verified with rational intervals003, without evaluating another N.

## 3. Cauchy–Schwarz with BOTH weights and uniform simplification

For eta>0, the causal autocorrelation satisfies

    |c_f(t)|<=e^(−eta t)||e^(eta y)f||·||e^(−eta y)f||.

WRN017 is valid for both signs of the weight (the expression only uses the square of the second parameter). With rho_+=eta²/(u−eta)² and rho_−=eta²/(u+eta)²,

    ||e^(eta y)f||·||e^(−eta y)f||/norm²
      <=[u²/(u²−eta²)]^(N−1/2) sqrt(S_N(rho_+)S_N(rho_−)),
    S_N(r)=sum_(l>=0)B_l^(N)r^l,
    B_l^(N)=(N−1/2)_l/(1/2)_l.

The coefficientwise bound is elementary:

    B_l^(N)<=(2N−1)_l/l!,
    S_N(r)<=(1−r)^(−2N+1).

Indeed the successive quotients are compared by cross-multiplying; the difference is (N−1)l>=0. Hence, for u>2eta,

    |c_f(t)|/norm²<=e^(−eta t)
            [(u²−eta²)/(u²−4eta²)]^(N−1/2).              (CENTERED)

This is an inequality of the real kernel for ALL k, not a positivity claim from identities. The product eliminates the linear cost term that appeared in the single-weight bound.

## 4. Full comb uniform in the region

Fix eta4. Since u²>=256N,N>=2, the CENTERED factor is

    [1+48/(u²−64)]^(N−1/2)
       <=exp(48N/(224N))=exp(3/14)<14/11.

Thus, using ALL contacts,

    |PRIME|/norm²
      <(28/11)sum_(q>=2)Lambda(q)q^(−9/2)
      <=(28/11)(5/7)2^(−4)[log2+2log2/3+2/9]
      <4/25.                                            (PRIME)

We used Lambda(q)<=logq, q^(−1/2)<=2^(−1/2)<5/7 and the decreasing integral of x^(−4)logx from2. The final comparisons are Fraction. There is no arithmetic truncation nor hypothesis on the individual sign of contacts.

## 5. Alternating polar at variable N

Let c_k=binom(2k,k)/4^k. The exact beta formulas are

    norm_(N,0)²=Gamma(N−1/2)/[2sqrt(pi)Gamma(N)u^(2N−1)],
    norm_(N,k)²/norm_(N,0)²=c_k/binom(k+N−1,N−1),
    POLAR_(N,k)=2(−1/4)^k/(u²−1/4)^(N+k).

Jensen for X with law Gamma(N−1/2) gives Gamma(N)/Gamma(N−1/2)=E sqrt(X)<=sqrt(N−1/2)<sqrtN. By Bernoulli and u²>=256N,

    p_(N,0):=POLAR_(N,0)/norm_(N,0)²
      <=(4sqrt(pi)sqrtN/u)(1−1/(4u²))^(−N)
      <(9/20)(1024/1023).

We used sqrt(pi)<9/5. Since binom(k+N−1,N−1)<=N^k and c_k>=2^(−k),

    |POLAR_(N,k)|/norm²<=p_(N,0)[2N/(4u²−1)]^k,
    2N/(4u²−1)<=4/2047<1/500.

For EVEN k the polar is positive. For ODD k>=1, the two rational bounds prove

    |POLAR_(N,k)|/norm²<1/1000.                            (POLAR)

The positive contribution of even k is not subtracted nor is a constant used that grows without control with N.

## 6. Real form, boundary of the pattern and coordination of the edge

ARCH, PRIME and POLAR give for ALL the parameters of REGION,

    W[f_(N,k)]/norm²>9/10−4/25−1/1000
                    =739/1000>7/10.

This is new real coverage of W on an infinite set of orders and rates. It is not a campaign over dimensions nor a new formal descent argument.

The condition u²>=256N does NOT cover all orders at fixed u: there it only guarantees N<=u²/256. In particular it does not close the sufficient table of u31.5. The moment E tau^(−2) used in ARCH-GENERAL diverges at k0; that limits this proof, it does not refute the sign of the edge. k0 is treated in parallel by a specific real bound and a stronger wedge u>=64sqrtN, with the polar kept, in POWER_BOUNDARY_WEDGE_029.md. Its result is combined only after its own proof and review; it is not presupposed from REGION.

No new windowT nor the global sign of Paper47 is claimed. The advance is the explicit quadratic scale, keeping the gamma form and the full comb.

Reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_row_pattern_029_verify.py

The verifier only compares universal Fraction/interval constants; PASS. Uniformity in N,k,u resides in the proofs above, not in a sweep.
