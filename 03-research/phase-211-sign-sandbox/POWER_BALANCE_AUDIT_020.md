# POWER BALANCE AUDIT 020

Status: SIGNED_BALANCE020 and INVERSE_KERNEL020 APPROVED, with the scopes delimited below. Papers untouched.

## Novelty and scope restriction

The antecedents audited in POWER_SIGNED_AUDIT_019 are kept: Euler/Möbius and Λ*1=log are not a new proof of sign; Descartes is a classical tool. The new specific autocorrelation frontier of 019 does prove the sign of the comb at k=1 for N≤211, but not that of the full form W. The negative mean B019 and the negative inverse prefix do not decide the full inverse kernel.

This round requires verifying separately the normalisations and the balance of the three real contributions ARCH, comb and polar, or a complete signed pairing that controls it. Transferring the sign from one carrier to another without the corresponding inequality will not be accepted. The full table and new windows T remain open as long as their sufficient condition is not proved.

## SIGNED_BALANCE020 — APPROVED

Reviewed `POWER_SIGNED_BALANCE_020.md` and `tools/power_signed_balance_020_verify.py`; independent run PASS. The Euler integral of the remainder of ψ has modulus ≤(1/2)∫(a+t)^−2dt=1/(2a). The four shifts from 1/4 to 17/4 keep the minus sign of the reciprocals. In x=T², log(A+x), −a/[2(A+x)] and each −b/(b²+x) are concave; Jensen supplies the upper bound U with E T²=3u²/[4(2N−3)]. The normalisation is that of the real ARCH, without the polar term incorporated.

The beta norm and K_N are correct; the comb factor −2Λ(2)2^−1/2 and 2^−u=2^−31/√2 produce exactly (log2/2^31)K_Nr_N(u log2). The Horner evaluator keeps Fraction endpoints without intermediate rounding. ARCH/norm<−.74 and 0<P2/norm<.075 are certified at N211,k1,u31.5. The polar term is strictly negative, so the real form keeping only contact 2 is less than −.66 times the norm.

Scope: new and concrete obstruction to the balance via the first contact in this column. It is not a new positive row of W. All remaining contacts are favourable by 019 and their joint magnitude is still pending; there is no conclusion W<0 nor a prohibition of repair via several contacts. The general formula U is proved for variable N, but FAIL2 is only certified at the declared point.


## INVERSE_KERNEL020 — APPROVED

Read `POWER_INVERSE_KERNEL_020.md` and `tools/power_inverse_kernel_020_verify.py`; independent run PASS. The gamma formula for p_j and the ratio (j+1)p_(j+1)/p_j≤u are correct. Therefore A_N=(u+1/2)P_N−P_N′ has all its coefficients strictly positive and degree N−1; H_N=x^−33 A_N(log x) keeps the normalisation of 019.

The comparison of each monomial gives A(t+l)/A(t)≤exp(dl/t). For log x≥d/30, the FULL Möbius series is dominated by Σ_(m≥2)m^−2≤3/4. This proves H/4≤h≤7H/4 without any inference from prefixes. The finite expansion of A also justifies that h is x^−33 times a polynomial, with positive leading coefficient A_d/ζ(32).

For N=2, Σμ(m)log(m)m^−32=−M′(32)=−D(32)/ζ(32), so the formula H2 has the correct minus sign. The bound D(32)≤Σm^−31 and 1008D<1/4 give h2≥H2/[2ζ(32)]>H2/4 on the whole half-line. The series and its necessary derivatives are absolutely convergent.

LOCAL keeps the direction: B<0 and h≥H/4 imply 2hB≤−(a0/2)H(x−1) on the tail. The integration by parts of that tail correctly has the positive term (X−1)w(X). The adverse part of the pairing is localised in [1,exp((N−1)/30)], without it having been shown that its magnitude is compensated.

## Conclusion of the round

New sign result: positivity of the FULL Möbius kernel on the explicit exterior region for every N, and globally for N=2. New balance result: the first contact alone does not repair the atom N211,k1. Neither proves a new positive entry of the form W that was not covered, nor a new row or window T. The bound on the interior pairing and the favourable magnitude of the rest of the comb remain open; they are not replaced by the identities.
