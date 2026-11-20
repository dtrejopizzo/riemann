# POWER_INVERSE_COEFFICIENT_AUDIT_054

Status: the COEFF/EVAL lemma of POWER_INVERSE_COEFFICIENT_054 is **APPROVED**, after a complete reading of the source. No new sign of W nor a complete cutoff is claimed. Papers untouched.

## Antecedents and difference

Cross-checked index/grid/crossword and HIGHPASS015, JOINT_SCALE016, QUADRATIC_EXPLICIT017 and the moments 049/053. 015 already proves eventuality uniform in the numerators in fixed dimension through Gram convergence and Riemann–Lebesgue, without an effective dependence of the conditioning on dimension. 016 prevents a weighted time constant independent of n, but not explicit constants growing with n. 017 treats monomial densities. The new object here is a polynomial in inverse frequency whose coefficient control depends explicitly only on n and holds for all j>=n. Another qualitative proof of RL is not recorded as progress.

## Normalization and proof of the bound

For a=u sqrt(j), R(y)=y^(n−1)P(ia/y) is a polynomial of degree<=n−1, and its change of coefficients is invertible for each j. The change tau=a/y on both half-lines has absolute Jacobian a/y². Substituting the power of the denominator gives exactly

    ||Q^jF0||²=a^(1−2n)/(2pi) ∫|R(y)|²(1+y²/j)^−(n+j)dy.

No factor 2 is missing because the last integral covers the whole line. Integrability holds at zero and at infinity for all n>=1, j>=n.

On [-1,1], log(1+y²/j)<=y²/j and (n+j)/j<=2, so the weight is >=exp(−2). The Legendre recurrence implies by induction that the sum of moduli of their coefficients is <=3^k. Their orthogonality gives, by Cauchy,

    (sum|coef R|)²
      <= exp(2) D ·sum_(k<n)(2k+1)9^k/2
      <= exp(2)D n²9^(n−1).

Since exp(2)<9, the declared constant C_n=9n²9^n is ample and valid also at n=1. The proof covers complex coefficients and hence ALL numerators, not only their diagonals or a fixed numerator as j varies. It does not require an unquantified limit eigenvalue.

The complex evaluation satisfies |R(z)|<=(sum|coef R|)max(1,|z|^(n−1)); applying it to z and −z proves the two EVAL bounds with exactly the same norm D and constant C_n. No additional quadratic loss of C_n appears.

## Sign and limits

For real P, R(y)R(−y)=(−1)^(n−1)|R(y)|² holds on the real line. The source explicitly keeps that factor in DENSITY; its analytic identity is correct. Absolute majorants on a contour do not remove the obligation to integrate the complete density with its denominator.

COEFF/EVAL does not yet prove a summable arithmetic tail nor a cutoff K(n) for W. An IBP correlation bound proportional to 1/t does not by itself sum the infinite comb. The monomial endpoint N'=1 of a future reduction cannot be imported from a proof that only covers N'>=2. Section 5 of the memo keeps these obligations separate and OPEN. The previously certified sign coverage is not modified.
