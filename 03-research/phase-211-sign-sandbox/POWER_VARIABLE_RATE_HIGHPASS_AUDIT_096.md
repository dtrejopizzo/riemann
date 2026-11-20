# POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096 — Independent audit

Status: **APPROVED / PROVED**, source `POWER_VARIABLE_RATE_HIGHPASS_096.md` read in full. A second independent check approved all its estimates. No campaigns or numerical certificates; papers untouched.

## 1. Fixed target and normalization

Cayley at rate u transforms the SAME normalized exponential of rate u0 into H_a=sqrt(1−a²)/(1+az), a=(u−u0)/(u+u0). The vector of pairings with z^j(1+z)^r is sqrt(1−a²)(1−a)^r(−a)^j. Therefore PROJECTION is exactly a SQUARED NORM, not a norm nor a spectral density. xi=−a covers all of (−1,1) when u>0; the target is not falsely kept constant as the rate varies.

## 2. Gegenbauer and the two parities

Rodrigues agrees with the coefficient sum. Integrating k times by parts eliminates the boundaries for lambda>=1 and gives h_k with the correct beta factor; D^kC_k=2^k(lambda)_k. The two formulas for central values and odd derivative keep pi, 4 and the Gamma ratios. The Gamma lower bound sqrt(x−1/2) uses Cauchy–Schwarz plus Gamma(x+1/2)=(x−1/2)Gamma(x−1/2); the upper is Jensen. BASE-VALUES is loose but valid even for m=0 and n=1.

At is all terms of C_k have the same phase. After normalizing, the sums with factorials (2j)! and (2j+1)! are paid by cosh and sinh(X)/X, including X=0. No oscillatory bound was used without keeping signs.

The centering exp(−idtheta/2) correctly divides integer or half-integer frequencies. E is even and O odd even with complex coefficients; the cross term vanishes by parity in the integral, not by assuming them real. The circular measure produces exactly 4^r/pi and weights lambda=r/r+1 swapped according to parity. At theta=i eta, P(xi)=xi^(d/2)T and the factor sqrt(1+s²) is paid without losing a normalization.

## 3. NEAR region

The sums of orthonormal evaluations are bounded by 8n sqrt(r) and 96n²r^(3/2)s² with the same exponential. Absent degrees give an empty sum; n=1 does not require an odd component. Cauchy–Schwarz on the direct sum of both sectors produces CENTER-KERNEL with sufficient factor 2.

The power ((1+xi)/2)^(2r) costs exp(−3r eta/4), while the kernel only restores exp(r eta/4), by r>=1024n and s<=eta<=1. The exact maxima of eta e^(−r eta/2) and eta³e^(−r eta/2) give 128+41472n/r<=168.5<200. pi<4, 1−xi²<=2eta and xi^d<=1 were included. The endpoint xi=1 is not interpreted as an admissible Hardy vector.

## 4. FAR region and uniformity

The exact determinant 094, with r>=n, gives the Gram lower bound: each factor relative to C=binom(2r,r) is >=j!/(2r)^j. lambda_min>=det/(trace)^(n−1) and ||v||²<=n pay for the full inverse, without an insufficient diagonal bound. C>=4^r/(2r+1) and 1+xi<=1+e^−1<3/2 give exactly FAR-GRAM, including ALL negative xi.

The three logarithmic bounds under r>=1e12n³ are correct. log(2r)<2r^(1/3) follows from the maximum of log x/x^(1/3) and e>2; its constants pay n²/r^(2/3)<=1e−8. The sum of positive logs is <r/100 and log(16/9)>1/2, so the exponential factor dominates uniformly in n,r. exp(r/4)>1+r/4>=sqrt(r) completes FAR. n=1 and all rate endpoints are covered without an implicit asymptotic argument.

## 5. Result and scope

It is proved that A_(n,r)(xi)<=200n/sqrt(r)<=1/5000 for ALL n>=1, r>=1e12n³, u>0 and any fixed target u0>0. Thus the distance of the normalized exponential to the UNION of all those spaces, allowing ALL rates, is >=sqrt(4999/5000). It is not claimed that each approximant has norm 1: this is the distance to a full linear subspace, computed via its orthogonal projection.

Consulted the records and 016/029/054/060/094. The difference relative to 094 is uniformity in the rate with a FIXED time target; relative to 016 it is UNWEIGHTED L². The cone 060 is included by its threshold. Not treated: the linear envelope, cross terms between blocks, mixtures of densities, or adding other continuous initial families. No negative W nor global impossibility of closing W; no new W/T coverage.
