# POWER_SIGNED_AUDIT_014 — Independent review of the global eight-pole closure

Status: PROVED. POWER_SIGNED_TRANSFER_014.md and tools/power_signed_transfer_014_verify.py reviewed in full. Independent run of the verifier with PASS. Papers untouched.

## 1. Exact telescoping and preserved restriction

For A_j=v_j²(u²+x)/[u²(v_j²+x)], one verifies A_j-1=x(v_j²-u²)/[u²(v_j²+x)]. Multiplying by the product of the previous A_k and by |P|²/(u²+x)^n, the factors become exactly

    kappa_j=(v_j²-u²)/u² prod_(k<j)v_k²/u²,
    |G_j|²=x|P|²/[(u²+x)^(n-j+1)prod_(k<=j)(v_k²+x)].

Thus TEL keeps the constant R0, the exponents and all cross terms of the numerator; there is no missing root or norm factor. Each kappa_j is nonnegative and G_j has n+1 poles and numerator sP, of degree<=n and with a zero at s0. The condition refers to the Laplace transform, not to the time value of the vector.

The archimedean motion of004 applies to the SAME subspace of polynomials Q of degree<n+1 with Q(0)=0: the denominator map keeps Q exactly. Hence the restricted confluent bound does transport to all G_j. Integrating TEL against m-c, each summand is an archimedean form minus c times its norm; the positive sign derives from the coercivity of the restricted block, not from m being pointwise positive. This is an estimate different from the class discarded in013.

## 2. Two interval certificates and the correct Gram

The nine archimedean bands are formed with the psi derivatives at16 up to order8, summed16..2000 and enclosed via integrals from2001/2000, with correct signs. The intervals of gamma,pi and logarithms were audited previously; all operations use outward rational rounding. Interval LDL of AP8-(7/200)I passes with eight positive lower pivots.

In the restricted block Arch9, evaluating the Laplace transform of the Laguerre basis at0 gives sqrt(2/u)(-1)^j. Hence the basis B_i=e_i-(-1)^i e8, i0..7, describes exactly the kernel of that evaluation. The compressed entries are

    Arch_|i-j|-a_j Arch_(8-i)-a_i Arch_(8-j)+a_i a_j Arch0.

The program subtracts(1/4)(delta_ij+a_i a_j), which is EXACTLY(1/4)B^t B and not an improperly normalized identity. Its interval LDL passes. Thus gamma1/4 is a form bound relative to the physical norm for the WHOLE subspace.

The two eight-component moment norms satisfy4AA BB<(3/2)^2, justifying p3/2. The margin b-c-p*8/3969, with b7/200 and c3/100, is>1/1000. Integrating the decomposition and keeping the polar produces AP>.03 at all eight real poles>=31.5. No monotonicity of AP is presupposed.

## 3. All contacts and final margin

The weighted trace with alpha3/5 is covered by POWER_COMMON_TRANSFER_010§6; sigma189/10<min v_j. Its exact binomial sum satisfies4T8<25000². With beta97/5, the tail keeps the fractional factor2^-2/5<19/25: raising to the fifth power is exactly equivalent to25^5<4*19^5. The decreasing bound of(logx)x^-beta from2 and beta-1>18 give the rational majorant of the script<29/1000.

Hence the FULL form satisfies W>.001||f||² for any real numerator of degree<8 and any set of eight rates>=31.5, allowing multiplicities, arbitrary separation and rates without upper bound. The comb is the full infinite one, without favourable sign hypotheses on its individual matrices. No higher-dimensional result nor closure of Paper46 is inferred.

## 4. Scope of the advance relative to the previous limit

Round013 remained correct: it prohibited replacing the rational density by a worse pointwise cost and discarding positive gains. The current proof keeps the signed integral and proves its positivity on a restricted rational subspace, using TEL and a certified block. It explicitly changes an essential hypothesis of that class, without contradiction nor reinterpretation of a falsifier as a negative sign of the form.
