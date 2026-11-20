# POWER_QUADRATIC_EXPLICIT_AUDIT_017 — Independent review of the cone eta=15

Verdict: APPROVED, PROVED. POWER_QUADRATIC_EXPLICIT_017, its antecedent QUADRATIC017 and the verifier were read in full; the verifier was rerun with output PASS. No defects were detected. Does not modify papers.

## 1. Shifted density and normalised measure

The modulus identity is exact: with y²=x²+eta²,

    |u²+(x+i eta)²|²=(u²+y²)²-4u²eta².

The numerator has modulus y^{2k}; this produces the factor (1-aT²)^(-M/2), a=400/441. On |x|>=eta the Jacobian is <=sqrt2<2. Counting both half-axes and dividing by I=2∫_0^infinito rho, the main factor is exactly 2 times a beta expectation; no other factor two is lost.

## 2. Two different logarithmic estimates

The near estimate uses -log(1-z)<=z/(1-z), and

    aM/[2k(1-a)]<=202/41<5.

With T<=32N/k and k>=10000N², the exponent is <=64/125, whose exponential is <=125/61 by the geometric series. For the tail the original expression is kept: convexity of -log and f(0)=0 imply f(aT²)<=a f(T²)<=a f(T). Thus the exponent of the new beta is k/2, not 5k; its parameter a'=k/2+1/2 remains positive.

The ratio of normalisations is <=exp(N²/k)2^N. Markov with the moment N gives (1/8)^N. Their product is <=exp(1/10000)4^-N<=625/9999 for N>=2. All constants and directions of inequality are correct.

## 3. Small region and closing of the contour

The segment |x|<=eta has length 2eta and uses |x+i eta|²<=2eta². This gives exactly A=441/341 and r=200/341. The lower beta bound of QUADRATIC017 is valid here, since k>=4N. For t=k/N>=100, the function t/4-log(2t) increases, and at t=100 already exceeds logA+2 using log200<6 and logA<1. Hence the normalisation factors cost less than exp(k/4).

Since r<3/5 and log(5/3)>1/2 (first atanh term, with positive remainder), r^k<exp(-k/2). The small contribution is <exp(-k/4)<1/100. Its sum with the main segment is <5.

The poles of rho are at ±iu, outside the strip 0<=Im z<=15. The rational decay O(|Re z|^-2N) makes the vertical sides vanish, and shifting upward for t>=0 gives exp(-15t). Symmetry covers t<0. No weighted time bound that would lose the compensation between the two factors of the density was used.

## 4. All components of the form

CORR15 controls the INFINITE comb: 10Σq^-14<=150/(13*2^14)<1/1000. The beta law, the two digamma bounds proved in the main appendix and pi<4 give Arch>99/100: sqrt(k/N)>100, u*100/8>3^5>exp5 and 1/(2k)<1/100. The previous polar bound 400^-k is valid unchanged because k>=4N, and is less than 1/1000.

Thus W/||f||²>99/100-2/1000>49/50, for all N>=2,k>=10000N². The proof is uniform in those indices and sums all contacts. It does not claim the result for arbitrary numerators nor for the interior k<10000N².

The review of the main memo QUADRATIC017 also found no defect in its beta tilt .99k, small region, Gaussian approximation and passage to the infinite series; the explicit extension has its own sign closure independent of an assumption of favourable oscillation.
