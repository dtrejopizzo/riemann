# Preserving exact moments of each cell does not suffice if their number grows without rate

For the model of 225 a question arises prior to using divisor identities: does it suffice to control exactly any fixed list of low moments per cell? At the shortest linear order, N=k (j=1), the answer is negative even if a number of moments tending to infinity without prescribed rate is preserved.

There exist positive weights λ_p→1 on the same primes and integers M_n→∞ such that on EVERY cell n≤log p<n+1 the unrounded moments of orders 0,…,M_n are identical to the authentic ones. Nevertheless,

    limsup log(1+|C_(k,1)(λ)−C_(k,1)(1)|)/k = log M_(1/2)(3)>0.

The authentic sample has rate zero here by 224: d₁=arctan(1/2)−log(5/4)>arctan(1/28)≥Θ. The modified system therefore gives a strictly positive upper rate. The sample is not programmed along every subsequence nor is the Euler product of ζ preserved.

**Block that distinguishes the models.** Set a=1/2, m=log M_a(3), v=∂_a log M_a(3), x=x_a(3) from 212. Fix the order k, N=k, n=ceil(Nv), e=n−Nv, d=log p−n. Use I_k(L) from 218 with the order changed to N=k and s=−√k+ik. Normalise I_k(n+d) by the complex factor

    F=3^(s−1) exp(Nm−an) N^(−3/2).

On d∈[0,1], I_k(n+d)/F differs by a uniform o(1) from the profile

    g_φ(d)=exp(−ad)[K exp(iφ+ixd)J₊ + conjugate(K)exp(−iφ−ixd)J₋]/2,
    J₊=3/[v(a−ix)−i],   J₋=3/[v(a+ix)−i],   φ=Nθ+xe,

with K and θ from 212. Indeed the change u=3+r/N in the proof of 216 now keeps the factor exp(ir/3) since k/N=1. The scaling of 216 and 212 give the real profile with shift e+d+rv/3. Integrating each branch with exp(ir/3−avr/3) produces J₊ and J₋. The shift e stays in the phase and the factor exp(−a(e+d)) has been normalised at n. The contour envelope dominates by C exp(−cr); the cut indicator converges to one for each fixed r since v<2 log M₁(3). This proof does not assume that the complex profile before projection is real.

**A moment the chosen data do not see.** Temporarily fix an integer M. Use on [0,1] the positive empirical measure ν_n that assigns to each d the mass exp(−n/2)(log p)/√p. By PNT it converges weakly to exp(d/2)dd. In the complex norm of this measure project I_k/F onto the space of polynomials of degree ≤M. The norm of the residual stays bounded away from zero for all large k (with constant depending on M). Indeed the Gram matrices converge to a positive definite one. No g_φ is a polynomial: it is a combination with nonzero coefficients of two exponentials with distinct nonzero exponents; differentiating M+1 times does not make it vanish identically. By compactness of the phase the minimal distance to the space is positive. This transfers to ν_n by convergence of all products of the profiles and the monomials, uniformly in φ (only finitely many harmonics appear). The projected polynomials and their residuals moreover have uniformly bounded supremum for fixed M, by boundedness of the Gram inverses and of the profile.

Take the real or imaginary part of the residual whose L² norm is larger and call it R. It is real and orthogonal to all monomials up to M. Perturb the weights of that cell by λ_p−1=R(d)/(k(1+||R||∞)). This preserves exactly the moments of 225 up to M, without using PNT for that equality. The modulus of the change of sample on the cell is at least c_M |F| exp(n/2)/k: the corresponding coordinate of the integrated product of R with I_k/F is ∫R²dν_n. Since a=1/2 the factor exp(n/2) cancels exp(−an). A floor exp(km−O(√k+log k)) times c_M remains. For any uniformly bounded relative perturbation the limsup ceiling is m by the contour of height 1/2 and Chebyshev, as in 216; this absolute ceiling does not require t=o(N).

**A single system of weights.** At stage ℓ take M=ℓ and choose k so large that the loss from c_M is exp(o(k)), for example |log c_M|≤k/ℓ. Choose the cell above the cut of all orders already treated. The effect of previous changes, on a finite set of primes, tends to zero with k by 211. Later changes do not enter the already fixed orders. On the altered cells set M_n=ℓ and on the rest M_n=n. This gives M_n→∞, λ_p→1 and the stated limsup. Necessity of the specific rate n/log n, sufficient in 225, is not proved here.

**Antecedents and decision.** 155–156 already explain the loss of detection when using factorial identities or a fixed number of derivatives of a divisor weight. Here the moments are at the positions of primes of each cell and the obstruction comes from a strict distance to a space of polynomials in a positive prime measure. Unlike 221 and 223, all low moments of each cell are preserved and the quadratic order is changed to linear. This example rules out obtaining the ceiling through positivity of the measure and those moments alone. It does not rule out the arithmetic identities relating high moments of different cells.
