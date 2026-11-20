# POWER_STATE_064 — Cubic scale needed for uniform STRIP over all numerators

Status: **PROVED/APPROVED**, independent review in POWER_STRIP_CUBIC_AUDIT_064.md; the improved threshold j≥10^6n was also verified three times independently. No new sign of W. Papers untouched.

## Proved result

Source: POWER_STRIP_CUBIC_NECESSITY_064.md. Fix u=63/2 and0<η<u. For ALL n≥4 and j≥10^6n a nonzero REAL polynomial P_(n,j), degree<n, is constructed such that the density of the test s^jP/(s+u)^(n+j) satisfies

    ∫|ρ(x+iη)|dx / ∫ρ(x)dx ≥1+η²n³/(1152u²j).

Hence there cannot exist a finite D uniform over all numerators on a cone j≥C n^p with p<3: choosing j=max(ceil(Cn^p),ceil(10^6n)) makes the lower bound diverge. This conclusion refers only to the ABSOLUTE STRIP contour bound, not to negativity of W nor impossibility of a smaller sign cone.

## Mechanism and difference relative to059

059 uses P=1 and only forces exponent at least2. Here P varies with n,j: in inverse frequency the orthonormal Student polynomial of degree d=n−1 is taken. Its parity produces an even real numerator. The exact recurrence has k/8≤β_k≤4k up to n+4; projecting the generator060 on degree d+3 leaves a component≥n^(3/2)/24 and a remainder≤n^(3/2)/48. Thus ||H′||²/||H||²≥n³/(2304u²j). Since the constructed density is H² with H real, the even convexity of the shifted norms proves the STRIP lower bound.

No Gaussian packet with uncontrolled tails is used, nor is it assumed that a narrow peak has small variance. The construction and the bounds are analytic; there was no numerical campaign nor new sign case.

## What remains valid

060 continues to prove uniform STRIP and W>norm² for all numerators at j≥10^12(nq_n)^3, q_n=ceil(log2(n+1)).064 shows that the power3 is necessary for that absolute strategy; it does not decide the logarithmic factors. The initial segments and the global objective remain open. Positivity of thirteen arbitrary poles053 and the interior case129,0 of061 are not modified. No temporal windowT is extended and no paper is touched.

## Additional deduplication: normalised recurrence on the edge k0

For the family with rate u, let G_N(s)=(s+u)^−N and H_N(s)=s/(s+u)^(N+1). Define with their RESPECTIVE norms

    A_N(u)=W[g_N]/||g_N||²,
    B_N(u)=W[h_N]/||h_N||².

The already known full identities of016/036 and the derivation relation029 are

    B_N=A_N+u∂_u A_N,
    A_(N+1)=(2N A_N−B_N)/(2N−1)
            =A_N−u∂_u A_N/(2N−1).

The derivative is taken in the family of rates and can then be evaluated at u=63/2. ARCH, polar and ALL contacts are kept; no sign is assumed when differentiating.

Propagating A_N≥0 to the next order requires the concrete bound B_N≤2N A_N. A monotone descent from infinity could use B_N≥A_N together with liminf_(N→∞)A_N≥0. None of those new inequalities has been proved here. The identity and the differences of the comb reproduce the antecedents016/036 and Bessel019; they are not presented as a new sign tool nor is it inferred that isolated positivity of B_N implies them.

This review, coordinated with insight048, is recorded as a deduplication. It adds no W coverage nor a new theorem entry to the indices.
