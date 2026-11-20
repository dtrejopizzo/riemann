# POWER_UNIFORM_STRIP_AUDIT_060

Status: **APPROVED** POWER_UNIFORM_STRIP_060 after a complete reading of its ten sections. Analytic proof; requires no campaigns nor evaluation of numerical cases. Papers untouched.

One obtains STRIP3<2 and W>norm² for all proper real numerators of dimension n and all j>=10^12(nq_n)^3, with q_n as in the source. The interior remains open. The novelty relative to 015/054 is a uniform contour estimate whose constant does not grow with n, obtained via derivatives of an amplitude without phase and a Taylor tail controlled separately. The exponential causal norms refuted in 016 are not uniformized.

## Student weight and first derivative

Checked the Pearson operator, its leading coefficient and the recurrence. The monic subleading term is c_k=−jk(k−1)/[2(2M−2k+1)]; subtracting c_(k+1) produces exactly the declared beta_k. For k<=n+2 and j>=n+8, both factors of the denominator are at least j and the numerator is <=4j²k. Thus beta_k<=4k. The moments, the norms of the required degrees and the integration-by-parts boundaries exist with room to spare under this hypothesis; Gram–Schmidt is not applied to arbitrarily high degrees with a weight having only finitely many moments.

Multiplication by y has norm <=4sqrt(d+1) on degree d<=n+1. The Sturm energy gives j||R′||²<=lambda_(n−1)||R||² and lambda_(n−1)/j<=3n. It is essential to keep that factor j. The bound for y²R′ uses two multiplications after this inequality; that for y³R uses three, within all permitted degrees. The constants 28, 4, 128 and their majorant 200 are valid, also at n=1, where R′ is zero.

The inverse change gives the two exact norm identities in GEN. The constant phases/signs on each half-line do not contribute to the derivative norm; no frequency-dependent causal phase is differentiated. The original holomorphic function H is regular at zero and its derivatives there generate no boundary terms. Its branch exists on the strip since Re(u²+z²)>0 for |Imz|<u.

## Coarse contour and Taylor

The source correctly distinguishes SINGLE-EVAL from the product of the density. For complex p, |H(z)|² is bounded by the individual evaluation of R(a/z); each resulting diagonal is a scalar density 017. The cancellations of a and of the norm are the same as audited in 054. The scalar endpoint N'=1 has its independent justification by WR11 and Cauchy. COARSE is obtained for BOTH signs of height 15, without assuming a nonexistent symmetry of a complex polynomial.

N″(eta)=4||H′(·+i eta)||² has the correct orientation and the boundaries vanish. Convexity between −15 and 15 gives the bound at all intermediate heights. L²-valued holomorphy and isometric real translations allow applying Cauchy on the circle of radius 15, strictly contained in the analytic strip. This controls the Taylor tail in norm; FIRST is not iterated to infinity.

For the first L=20nq_n derivatives, the class changes exactly to (n+3r,j−r), with numerator of degree less than n+3r. The term j u²p+z(u²+z²)p′−n z²p is correct. The threshold guarantees j−r>=j/2, j−r>=n+3r+8 and n+3r+2<=63nq_n at all steps used. The FIRST ratio stays <1/100, according to the written rational comparison of constants. Therefore the Taylor segment costs at most exp(.03), not the large constant D_n.

Also checked n=1, q_n=1: D_n<3^(10nq_n), the degree inequalities and the tail remain strict. The general estimate D_n<3^(nq+2q+2n+5)<=3^(10nq) and the tail (5/4)3^(5nq)5^−20nq<.01 are correct. Together with the segment one obtains AMP3<1.1 for both signs of height. The comparison q_n<=n justifies the weaker corollary 10^12n^6.

## Full form and scope

For p(z)=P(iz), the identity rho=H H# is exact. Off the line Cauchy is used between the norms at opposite heights; that product is not confused with a shifted |H|². The result is STRIP3<1.21<2. The vertical sides vanish by the decay of the rational density. The autocorrelation bound 2exp(−3|t|) sums the WHOLE comb, whose bound 7/(3sqrt2)<2 keeps all primes and prime powers.

MULT gives the inverse moment 16n/(u²j); the threshold implies j>=160000n and hence ARCH>4 with the global digamma lower bound. The polar 054 <1 was already valid under j>=10000n², a condition satisfied here, without using its gigantic cutoff. All terms are compared with the SAME norm. The strict balance 4−2−1 gives W>norm² as claimed.

The result is a uniform cone for all numerators, not the full table. Not deduced: sign for j<J(n), a quadratic cone, or a new time window. NECESSITY059 and the obstructions 016 remain intact.
