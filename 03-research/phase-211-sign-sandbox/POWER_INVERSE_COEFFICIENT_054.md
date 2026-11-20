# POWER_INVERSE_COEFFICIENT_054 — Effective conditioning in inverse frequency

Status: PROVED coefficient/complex-evaluation lemma, independent review approved in POWER_INVERSE_COEFFICIENT_AUDIT_054.md. The subsequent contour and cutoff step is developed in POWER_EFFECTIVE_HIGHPASS_054.md; this memo keeps its initial proof separate. Papers untouched.

## 1. Antecedents and explicit difference

Consulted: the project rules, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reviewed HIGHPASS015, JOINT_SCALE016, INTERIOR017/WRN, QUADRATIC_EXPLICIT017§6 and the moment cutoffs 049/053. 015 already proves uniform eventual positivity in fixed dimension through a Gram limit and Riemann–Lebesgue; that eventuality is not repeated as a new result. 016 refutes exponential time norms uniform in dimension and 017 controls only monomial numerators.

The changed object is the rescaled INVERSE-FREQUENCY polynomial. Its norm admits an elementary bound on a fixed interval giving an explicit constant depending only on the dimension, for ALL numerators and ALL j≥n. No j-dependent monomial Gram matrix is inverted and no weighted constant independent of n is assumed. It is an effective coefficient inequality, not yet the sign of W.

## 2. Exact change and norm

Fix u>0, n≥1, integer j≥n, Q(s)=s/(s+u), and F0(s)=P(s)/(s+u)^n with degP<n. Put

    a=u sqrt(j),
    R(y)=y^(n−1)P(ia/y),
    w_(n,j)(y)=(1+y²/j)^−(n+j),
    D_(n,j)[R]=∫_R |R(y)|² w_(n,j)(y)dy.

R is a complex polynomial of degree≤n−1; the powers of y exactly remove the denominators. For each j the change of coefficients is invertible. The following lemma covers ALL R, even though the R associated with a fixed P depends on j.

With the corpus Fourier and Plancherel convention, the change τ=a/y, on both half-lines, gives

    ||Q^jF0||²=a^(1−2n)D_(n,j)[R]/(2π).                (NORM)

Indeed |P(iτ)|²=|τ/a|^(2n−2)|R(a/τ)|², and

    τ^(2j)|P(iτ)|²/(u²+τ²)^(n+j)dτ
      =a^(1−2n)|R(y)|²(1+y²/j)^−(n+j)dy,

with the orientation handled by the absolute value of the Jacobian. No factor 2 is missing: D integrates over the whole line.

## 3. Uniform and effective inequality

Write R(y)=Σ_(r=0)^(n−1)c_r y^r and fix

    C_n=9n²9^n.

Then, for ALL complex polynomials R and ALL j≥n,

    (Σ|c_r|)² ≤ C_n D_(n,j)[R].                         (COEFF)

Proof. On |y|≤1, log(1+y²/j)≤y²/j and (n+j)/j≤2. Thus w≥exp(−2), and

    ∫_(-1)^1|R|²≤exp(2)D_(n,j)[R].

Let L_k be the Legendre polynomials normalized by L_0=1, L_1=y. Their recurrence

    (k+1)L_(k+1)=(2k+1)yL_k−kL_(k−1)

implies by induction ||coef(L_k)||_1≤3^k: the step is dominated by 2·3^k+3^(k−1)≤3^(k+1). The elementary orthogonality ∫_(-1)^1L_kL_l=2δ_kl/(2k+1) can be obtained directly from Rodrigues and integration by parts, including the boundary terms killed by (1−y²)^k.

Expand R=Σb_kL_k. Cauchy gives

    Σ|c_r| ≤ Σ|b_k|3^k
       ≤ (∫_(-1)^1|R|²)^(1/2)
           [Σ_(k=0)^(n−1)(2k+1)9^k/2]^(1/2).

The sum is bounded by n²9^(n−1), by comparing each of its n terms with (2n−1)9^(n−1)/2. Finally exp(2)<9, and therefore n²9^nD already suffices in COEFF; the declared constant C_n, larger by a factor 9, is also valid at n=1. This proves the inequality without a limit or an unquantified eigenvalue.

## 4. Complex evaluation and real product of the density

For any complex z,

    |R(z)|² ≤ C_nD_(n,j)[R]·max(1,|z|^(2n−2)),
    |R(z)R(−z)| ≤ C_nD_(n,j)[R]·max(1,|z|^(2n−2)).     (EVAL)

Both follow from |R(z)|≤(Σ|c_r|)max(1,|z|^(n−1)); the arguments z and −z have the same modulus.

For REAL P, the complete analytic density of the filtered atom is

    ρ(z)=z^(2j)P(iz)P(−iz)/(u²+z²)^(n+j)
        =(−1)^(n−1)a^(−2n+2)
          z^(2(j+n−1))R(a/z)R(−a/z)/(u²+z²)^(n+j).   (DENSITY)

The factor (−1)^(n−1) is essential in this identity. For real y,

    R(y)R(−y)=(−1)^(n−1)|R(y)|²,

so DENSITY agrees with the nonnegative spectral density on the line. EVAL allows taking the modulus on a complex contour while keeping the complete product, without replacing it by two time norms growing in n.

## 5. Contour step separated from the proved lemma

EVAL is an explicit and uniform conditioning. By itself it does not pay for the shifted integral: the factor max(1,|a/z|^(2n−2)) and the rational denominator must be integrated, keeping the moments of the same norm NORM. Nor can one sum an autocorrelation bound decaying only like 1/logq: the infinite comb requires a justified summable tail.

A concrete continuation to be reviewed is replacing max by Σ_(r=0)^(n−1)|a/z|^(2r). Each term of DENSITY corresponds to a monomial density of 017 with N'=r+1 and k'=j+n−1−r. For j≥10000n² all terms with N'≥2 lie in the cone of the contour bound of 017. The endpoint N'=1 must be justified separately; a condition N'≥2 is not extended without proof. Then explicit bounds on the moments ∫y^(2r)w_(n,j)dy are required before concluding a contour cost depending only on n.

This memo proves only COEFF/EVAL, with an effective constant, which removes the obligation to estimate an ill-conditioned j-dependent Gram matrix. The continuation already developed is found separately in POWER_EFFECTIVE_HIGHPASS_054.md, including the endpoint N'=1 and the normalization moments; that conclusion is not attributed to COEFF without those additional steps.
