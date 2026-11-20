# A stability scale for the prime sample

Let there be two systems of weights on the primes and D(x) the difference of their accumulated sums of logarithmic weights. For example, for the relative weights λ_p and μ_p, D(x)=Σ_(p≤x)(λ_p−μ_p)log p. Form ΔC_k with the difference of weights in 217. If for some A≥0

    limsup_(x→∞) log(1+|D(x)|/√x)/(log x)^(2/3) ≤ A,

then

    limsup_(k→∞) log(1+|ΔC_k|)/k ≤ 4 A^(3/2)/(9√3).

In particular the counting error √x exp(o((log x)^(2/3))) preserves the subexponential bounds of the sample both globally and along any subsequence. 221 rules out that conclusion for a generic error √x · x^o(1). Here a sufficient ceiling with explicit constant is proved; optimality on the primes is not claimed.

**Uniform contour shift.** Write N=k², L=log x, and fix U≥3. For the observable restricted to U≤u≤N and 0≤a≤1/2, 208 and the Fourier contour give

    |c_N(L;u)|+|∂_L c_N(L;u)| ≤ C (u+u²) exp(N m_U(a)−aL),
    m_U(a)=log M_a(U)=a²/U²+O_U(a⁴).

Indeed one extracts the supremum of |H_u|^(N−2) on the shifted line; the remaining integral of (1+|τ+ia|)|H_u(τ+ia)|² is O(u+u²) by scaling and a/u≤1/6. M_a≥1 decreases in u. The upper cut L_X=2N log M₁(u) is O(N), uniformly in u.

For ΔA_N(u) integrate by parts x^(−1/2)c_N(log x;u) against dD(x) from 1 up to X inclusive. The boundary contribution at X and the integral in L are dominated by a polynomial in N times the supremum, for 0≤L≤C N, of

    exp((A+η)L^(2/3) + inf_(0≤a≤1/2)[N m_U(a)−aL]).

A constant depending on η>0 that covers bounded x is allowed. The choice of a varies with L AFTER differentiating the kernel: ∂_L c_N is estimated on each contour and the optimised envelope is not differentiated. The factors u+u² are absorbed into the polynomial since u≤N. In u integrate with the modulus of u^(−√k+ik−1), of bounded integral. The same estimate holds for ΔC_k restricted to U≤u≤N.

**Optimisation.** For ε>0 fix a₀∈(0,1/2) so small that m_U(a)≤(1+ε)a²/U² on [0,a₀]. When L≤2(1+ε)a₀N/U², use a=U²L/(2(1+ε)N). The exponent is dominated by

    (A+η)L^(2/3) − U²L²/(4(1+ε)N).

The maximum over L≥0, by the substitution z=L^(2/3), is 4√(1+ε)(A+η)^(3/2)√N/(3√3 U). On the remaining range use a=a₀: N m_U(a₀)−a₀L≤−a₀L/2 and L is of order N or larger, so the contribution is exponentially small in N. The polynomial prefactors cost o(k) in the logarithm. Send ε,η to zero and take U=3. For A>0, the maximum of the Gaussian majorant is at L of order k^(3/2). This is a scale of the majorant and not a saturation claim.

**Checkable consequences.** (i) The two perturbations of 221 that program respectively zero and exp(k) on the same orders must differ in their count by an amount satisfying

    limsup log(1+|D(x)|/√x)/(log x)^(2/3) ≥ (9√3/4)^(2/3).

If the limsup is infinite the claim is automatic; if it is finite the theorem applies. (ii) If A is finite and for each fixed U the contribution of the difference on [3,U] is subexponential along the SAME subsequence, the complete difference is subexponential there: the ceiling of the complement is 4 A^(3/2)/(3√3 U), and U can be sent to infinity after taking the limsup. (iii) The argument holds for differences of locally finite measures by the same Stieltjes integration. Applying it to the continuous model requires verifying the hypothesis on θ(x)−x; with any finite A that hypothesis already implies the bound O_ε(x^(1/2+ε)) and falls under the classical obstruction of 219. The stability result does not estimate the authentic error θ(x)−x.
