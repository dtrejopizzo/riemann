# POWER INVERSE INTERIOR AUDIT 022

Status: final memo §§1–5 and verifier APPROVED. Papers untouched.

Reviewed `POWER_INVERSE_INTERIOR_022.md` and `tools/power_inverse_interior_022_verify.py`. Independent run of the verifier: PASS, with −2/3<h_128(1)<−33/50 and complete tail m≥65 less than 10^−10 in absolute value. The diagnostic decimals are not used as proof.

## 1. Identity and finite part

The kernel of 020 is kept exactly: u=63/2, d127, H_N(x)=x^−33 A_N(log x), A_N=32P_N−P_N′. The Fraction recurrence for p_j agrees with its gamma formula; a_j=32p_j−(j+1)p_(j+1) are positive, a0=1/2. Hence h_128(1)=Σμ(m)m^−32 A_128(log m).

The Möbius routine by trial division detects square factors, flips the sign once for each distinct prime factor and correctly handles the residual factor and m1. It depends neither on an external table nor on an assumed sign of μ. The sum m≤64 is evaluated with outward intervals. The logarithms are reduced to [1,2] and enclosed with 120 positive atanh terms and the geometric remainder 2t^241/[241(1−t²)]. The outward rational rounding of each operation keeps the inclusion, also when multiplying by negative μ.

## 2. Complete infinite tail

For all degrees 0≤j≤127, x^−32(log x)^j decreases on x≥64, because log64>4>127/32. Consequently the sum from 65 is bounded by the integral from 64. Replacing |μ| by 1 and the positive coefficients a_j give an absolute majorant of the WHOLE tail.

The integral I0=1/(31·64^31) and the recurrence I_j=64^−31(log64)^j/31+(j/31)I_(j−1) are exact. Replacing log64<21/5 keeps the direction because only positive summands appear. The resulting rational sum is less than 10^−10. Adding and subtracting this bound to the endpoints of the finite part proves the strict interval (−2/3,−33/50), without depending on the prefix alone.

## 3. Novelty and scope

019 had only certified a negative prefix for large orders; 020 certified positivity of the complete inverse on an exterior region and globally for N2. 022 decides here for the first time the COMPLETE inverse at a concrete interior point. It is compatible with 020: for N128 the point log x=0 lies outside the exterior range log x≥127/30.

The result refutes the hypothesis h_N(x)≥0 for all N,x for the real kernels of this construction. It does not prove negativity of F_N, of the integrated pairing with B, nor of W. Pointwise negativity does not decide the magnitude of the adverse part against the favourable tail of LOCAL020 either. It certifies no new window T, nor does it discard a complete signed control of the pairing.

Final review: the complete memo was read and the reinforced certificate was run again, PASS. Continuity and the sign B<0 correctly produce a local adverse contribution hB>0 to the right of 1; they do not decide the total integral. Continuity together with OUTER020 guarantees at least one sign change before log x=127/30. These consequences are approved with their pointwise scope.
