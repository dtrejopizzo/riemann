# POWER_STATE_054 — Explicit cutoff for the full form in every dimension

Status: PROVED for the declared region; global sign OPEN. Papers untouched.

With u=63/2, Q(s)=s/(s+u), define

    C_n=9n²9^n, D_n=10C_n n!, A_n=6C_n n n!,
    K(n)=max(10000n²,A_n·3^(4D_n+20)).

For ALL n>=1, ALL nonzero real polynomials P of degree<n and ALL j>=K(n),

    W[Q^j P/(s+u)^n] > ||Q^j P/(s+u)^n||².

Source POWER_EFFECTIVE_HIGHPASS_054.md; independent review approved in POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md. Both full proofs were read and verified. It is not required to evaluate K(n), run a numerical campaign nor verify individual cases.

## New mechanism and exact scope

POWER_INVERSE_COEFFICIENT_054 and its audit establish an effective coefficient bound on inverting and rescaling frequency. A fixed interval and the Legendre expansion replace the unquantified smallest Gram eigenvalue of015. The constant depends on n and covers all numerators simultaneously.

The contour of the full density has absolute integral <=D_n times the spectral norm. The proof keeps the full polynomial product, applies017 to positive diagonals and justifies dimension1 separately. The exact beta moments control the constants; the autocorrelation is bounded by D_n exp(-15|t|)norm². This pays ALL arithmetic contacts through an absolutely convergent series.

The inverse moment is <=A_n/(u²j). FromK(n) on, ARCH>2D_n+9, the modulus of the comb<D_n and the modulus of the polar<1, all divided by the same norm². The balance proves the result with margin.

It is an effective improvement of the eventuality015: there is now an explicit universal formula in n. Its size is enormous and no optimality is claimed. It does not prove the segments j<K(n), does not show that this positive region is dense in the required carrier and does not extend the temporal windowT. Positivity on thirteen arbitrary poles053 remains valid separately.

## Proposals discarded as duplicates and live obligation

The absolute extrapolation of moments053 reproduces the obstacle016. Renaming the pending remainder as negative energy reproduces036; the renormalised tail042 does not resolve its interior nor uniformity in k. These are not new NO-GOs. Weighted temporal control independent of n is not assumed either.

The pending step toward the general objective requires controlling the initial segment as n varies while keeping its signed arithmetic. The effective cutoff does not authorise eliminating that segment by recurrence nor by small mass. There is no external blockage nor closure of the goal.
