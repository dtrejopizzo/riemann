# Frequency tail below the root with the moving cut

For large x, c=1+1/log x, T=(log x)², and the same corridor of z as 360, let D_z(s) be the Dirichlet series of the coefficients of the sieved products of 361 (without the multiplier W). RH is equivalent to the bound O_ε(x^(1/2+ε)) for a single integral:

    (1/(2π)) ∫_{−T}^T x^(c+it) exp(−√(1+c+it)) D_z(c+it) dt.

The root takes the branch with positive real part. The cost of the WHOLE removed tail is O(x^(1−1/√2)(log x)^3), unconditional and uniform in z. The height T still grows with x.

**Weight.** For u>0 take w(u)=exp(−u−1/(4u))/(2√π u^(3/2)) and for u≤0 take zero. Its Laplace transform is W(s)=exp(−√(1+s)) for Re s>−1 by the Gaussian integral. For example, after the substitution v=1/(2√u) one uses I(b)=∫_0^∞ exp(−v²−b²/v²)dv, with I(0)=√π/2 and I'(b)=−2I(b) by the change b/v, first for real b>0 and then by continuation. The weight is smooth, of finite variation and never uses n>x. Moreover u w=w*ν with ν(du)=exp(−u)du/(2√(πu)), since −W'/W=1/(2√(1+s)). This positive measure has finite weighted norm at each abscissa σ>1/2.

**Why it preserves the criterion.** With this weight the logarithmic identity of 360 keeps exactly the same form, with the new ν. The corrections cost O_ε(A(x)x^(1/2+ε)) by the weighted integral of ν and the sum over higher powers. The dilation identities and the two bounds for short and long branches of 360 are independent of the shape of w and apply literally (S_w still vanishes for x<1). The direct direction under RH uses Mertens and partial summation with w of finite variation. For the inverse, W(s)/ζ(s) is the transform of S_w and W does not vanish in Re s>1/2. Thus the root ceiling of the full pulse is equivalent to RH, with all the centers and cuts of 360.

**Truncation.** At c>1 the series is absolutely convergent and the modulus of each coefficient is at most log n, by summing over the prime divisors of n. Hence |D_z(c+it)|≪(c−1)^(−2) uniformly for 1<c≤2. Mellin inversion is absolute by the decay of W. The formula for the complex root gives Re √(1+c+it)≥√(|t|/2); the integral of the majorant from T to infinity costs O((1+√T)exp(−√(T/2))). Since x^c=ex, substituting T gives the announced bound, with exponent strictly less than 1/2.

**Scope.** The remaining integral is taken on the line of absolute convergence. It does not require evaluating 1/ζ near a zero to define it. Proving cancellation within |t|≤(log x)² is missing; taking moduli there only gives a bound of order x with logarithmic losses. This truncation is in frequencies for the sieved observable, and does not enlarge the radius T of paper 47.
