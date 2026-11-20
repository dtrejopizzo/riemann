# Which polynomial slopes can be certified after cancelling the verified ordinates

Keep the same c=1.25·10^(−25), W=cT and the Gaussian normalization of 148. For degree d≤floor(T/2000) the ORIGINAL quadratic of 148 already has a polynomial ceiling uniform in T, which is the type of bound required by the criterion for that slope. Moreover strict uniform negativity is obtained by introducing a fixed random translation of variance <0.06: for B independent of Y, defined below,

    E[P(Y/√W)² U(T+Y+B)] = 1/ζ(1/2) + O(exp(−.005T)).

The error is uniform over all unit real polynomials of those degrees. The new average keeps the implication to the sign when proving all the slopes of 148.

**Translation.** Take B to be a sum of independent equiprobable signs multiplied by π/(2γ), with one factor for each zero of positive ordinate γ≤3·10¹², repeated according to its multiplicity. These are exactly the ordinates of statement Z2 of paper 47; the mathematical definition uses their exact values. Its transform M(s) is the finite product of cosh(πs/(2γ)). It has M(0)=1, vanishes at least with the needed multiplicity at each critical pole of the rectangle of 148 and has no zeros with Re s>0. It is bounded uniformly in height in any fixed vertical strip because B has compact support. Its variance equals (π²/4)Σ_{0<γ≤G}1/γ² with multiplicities. By Z1, 1/γ²≤(1+1/(4·14²))/(γ²+1/4). The partial sum of the latter terms is bounded by the sum of Re(1/ρ) over all zeros, since each critical pair contributes 1/(γ²+1/4) and each remaining term is positive. The classical Hadamard identity gives for that sum 1+γ_E/2−log(4π)/2<0.024, which proves the announced variance ceiling.

**Estimate on the contour.** In 148 take κ=1/2000 and shift from σ=.501 to −1/4 with fixed height 2.99·10¹²<G'<3·10¹² avoiding ordinates. The exponent per T is bounded by

    σ+c(σ²−τ²)/2 + 2√(cκ) |σ+iτ|.

For |τ|≥2.99·10¹² the majorant using |σ+iτ|≤|σ|+|τ| decreases with |τ| in the strip; at σ=.501, |τ|=2.99·10¹² already gives less than −.010. This controls horizontals and right tails, keeping a margin and integrable decay in the tails. At σ=−1/4, maximizing −cτ²/2+2√(cκ)|τ| costs at most 2κ=.001. The initial right line lies in the region of absolute convergence. With the factor M(s) only the real pole contributes; at s=0 the normalization gives exactly the bias. The stated error follows for the translated form.

For the original form the critical poles survive, but at them one can use |exp(iγY)|=1. Each residue of multiplicity m is bounded by a polynomial in T uniform in P: differentiating at most m−1 times produces factors T and moments E[P² |Y|^k]. Multiplying by the coordinate in the orthonormal Hermite basis raises or lowers the degree with coefficients ≤√(d+k+1), so these moments are O_k((1+√(W(d+k+1)))^k). The number of poles in the rectangle is finite. Neither simplicity of the poles nor a numerical value of the constants is assumed.

**The criterion over all slopes is preserved.** Under RH translating the function U by B preserves the bound of 148 since E exp(εB) is finite. If there is an off-line zero, modulate the Gaussian in Y as in 148: the contour of the modulated average of U(T+Y+B) contains M(s)R(s), with M nonzero at each pole with positive real part. The unique positive maximum and the Taylor approximation of 148 remain valid, with an extra constant E exp(B/2) in the error bound. Thus some higher slope gives exponentially large positive quotients if the sign fails. This does not claim that slope 1/2000 suffices to detect them.

**Scope.** The jump in slopes for the polynomial ceiling in the original quadratic comes from estimating the critical residues by unitarity. To obtain strict sign their contribution is cancelled by a positive distribution that still sees the off-line poles. 122 already uses cosh to concentrate a test on a zero; here a product of factors is placed to annihilate a finite list in the arithmetic mean. No numerical table of the translations was built and no additional window of P47 was verified.
