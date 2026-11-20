# POWER_INVERSE_INTERIOR_022 — An interior point of the complete inverse

Status: PROVED a negative point of the COMPLETE inverse, rational certificate executed and final independent review APPROVED. The verifier was reproduced independently twice. Papers untouched.

## Corpus and new reason before building

Read the project rules, SIGNED_MEAN019 (failure ONLY of prefixes), INVERSE_KERNEL020 (complete exterior positivity), their audits and targeted searches in index/grid/crossword on inverse/kernel/Möbius/sign. The exact difference is deciding a COMPLETE sum at ONE interior point, with a rigorous tail; nothing is inferred from the prefix 019 nor from the exterior region 020.

N=128, x=1 is chosen because the local gamma approximation of the derivative term at contact 2 has scale (u²log2/(2N))exp(−u²(log2)²/(4N)), whose maximum in N falls near u²(log2)²/4≈119. The approximation only motivates the point; it does not take part in the certificate. The cutoff 64 is fixed by monotonicity: log64>127/32, which allows bounding ALL the tails of logarithmic powers of degree up to 127 by an integral.

## 1. Result on the complete sum

With the exact kernels of 020, we prove

    −2/3 <h_128(1)<−33/50<0.                            (NEG)

The sum includes ALL integers m of the Möbius inversion. In particular the lemma «h_N(x)>=0 for all N>=2, x>=1» is false. This refutes a possible premise of the sign recovery via 019; it does not refute the sign of the Weil form nor of ERR.

The result complements OUTER020: for N=128 it is known that h_128(x)>=H_128(x)/4>0 if logx>=127/30. Negativity at 1 and continuity imply a negative interior region and at least one sign change before that boundary. The sign is not extrapolated to other N.

## 2. Exact positive polynomial used

The rational coefficients are reconstructed by

    p_0=1,
    p_(j+1)=p_j·[2u(N−1−j)]/[(j+1)(2N−2−j)],
    a_j=32p_j−(j+1)p_(j+1), j<127,
    a_127=32p_127,
    A_128(t)=Σ(j=0..127)a_j t^j.

The proof of 020 gives a_j>0 and a_0=1/2; the script also verifies these signs rationally. The kernel is

    H_128(x)=x^-33 A_128(logx),
    h_128(1)=Σ(m>=1)mu(m)m^-32 A_128(logm).

The 128 lengthy coefficients are not printed: the rational recurrence determines them entirely with no numerical parameters.

## 3. Finite segment with enclosed logarithms

The script `tools/power_inverse_interior_022_verify.py` computes mu(m) for 1<=m<=64 by elementary integer factorization: a repeated prime factor gives 0, and each distinct prime factor flips the sign. It uses no external table of Möbius values.

The logarithms are enclosed with the explicit rational module `power_fixed_grid_003.py`: argument reduction to [1,2], atanh series and geometric remainder, with outward rounding at every operation. A_128 is evaluated by interval Horner and the segment m<=64 is accumulated keeping the sign of each mu(m).

All entries and operations of the certificate are Fraction; the approximate decimal value −.662345100449 is mentioned only for orientation and does not take part in NEG.

## 4. COMPLETE tail m>=65

For 0<=j<=127, the function x^-32(logx)^j decreases when logx>=j/32. Since log64=6log2>4>127/32,

    Σ(m>=65)m^-32(logm)^j
       <=∫_64^infinity x^-32(logx)^j dx.

Put L=21/5>log64. By integration by parts and positivity, rational upper bounds for these integrals are obtained from

    I_0=64^-31/31,
    I_j=64^-31 L^j/31+(j/31)I_(j−1), 1<=j<=127.

The positive coefficients a_j allow bounding the WHOLE Möbius tail, without assuming cancellation:

    |Σ(m>=65)mu(m)m^-32 A_128(logm)|
       <=Σ(j=0..127)a_j I_j <10^-10.                    (TAIL)

The last sign is an exact rational comparison executed by the verifier. This majorant controls the infinite complement of the computed segment. Hence NEG is not an inference from a negative prefix.

Adding the finite interval and the symmetric interval ±TAIL gives the two rational endpoints of NEG. The executed verifier produces PASS.

## 5. Limited consequences for the pairing with B

The sign B(x)<0 of 019 does not pass to the sign of F_N=2∫h_N B because the complete inverse can indeed be negative. By continuity, for N128 there is an interval to the right of 1 where h_N<0 and B<0, so that the product h_N B is positive: an adverse contribution really appears, not merely the loss of a bound.

This does not determine the TOTAL pairing: the regions with h_N>0 contribute favourably and the positive exterior region of 020 is kept. W[g_128]<0 and F_128>0 are not claimed. The new datum is a complete, certified falsifier of the hypothesis h_N>=0, with a single analytically chosen N and a rigorous infinite tail.
