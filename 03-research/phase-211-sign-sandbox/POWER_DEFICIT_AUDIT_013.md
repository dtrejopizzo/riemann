# POWER_DEFICIT_AUDIT_013 — Review of the limit of the pointwise envelope at eight poles

Status: PROVED for the declared class. Reviewed POWER_DEFICIT_LIMIT_013.md and tools/power_deficit_limit_013_verify.py; independent execution with PASS. Papers untouched.

## 1. Two exact certificates

The evaluation of the rational vector of eight coordinates uses the previously derived AP bands, now with psi^(j)(16) up to j7. The sums16..2000 and the tail integrals from2001/2000 have correct orientation. The interval sum of ALL pairs v_i v_j keeps the interval correlations conservatively, and certifies0<Rayleigh<1/25. No numerical eigenenergy is required or computed for this bound. Any b valid for the whole block necessarily satisfies b<=lambda_min<=that Rayleigh<1/25.

The bound on m(4) sums exactly k0..31 of the positive series and bounds the omitted terms using x/[4a_k³]. For k>=32, comparing the sum with the integral from31 of(x+1/4)^-3 produces exactly the term x/[8(125/4)^2]. The upper endpoint mzero.hi is the pertinent one. The result m(4)<-2/5 and the rational comparison(2/5)[(1+16/u²)^8-1]>1/20 were re-executed and are correct.

## 2. Failure of the best DIRECT pointwise loss

For any c>=0, evaluating at x16 already gives

    L8(c):=sup_(x>=0)(c-m(sqrtx))_+[(1+x/u²)^8-1]>1/20.

This uses exactly the uniform envelope of the filter; it can be approximated pointwise by making all the new rates arbitrarily large. It is not presupposed that a numerator of degree seven can concentrate all its probability at x16. The cost L8 refers to the class that DISCARDS that spectral restriction and replaces the loss by its pointwise supremum independently of the vector.

Since b<1/25, even granting zero polar cost and c0, b-c-L8(c)<1/25-1/20<0. Hence what fails is not only separating maxima as D*K, but also using the best direct pointwise envelope of this class. The restriction 'discards the positive gain' is decisive for identifying what has been excluded.

## 3. Case D*K and scope

If in addition X,D are used, any valid X must be>16 and D>16*(2/5). Monotonicity of[(1+x/u²)^8-1]/x yields DK8>1/20. This particular version of the failure is consistent with §2; improving the panels or the constants does not overcome it.

The result does not provide a negative AP vector: the test used has POSITIVE AP. Nor does it prove W negative, nor that an eight-pole theorem is impossible. Estimates that keep the rational measure, the positive gains, the polar coupling or the specific filters remain outside the class. The audit approves exactly that delimitation and no larger global conclusion.
