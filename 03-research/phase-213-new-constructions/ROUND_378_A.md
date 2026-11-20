# One large layer at every scale and the limit of multiplicity moments

**Status: PROVED, with independent review of the uniform floor and of the abstract class of the obstruction.**

Let L=log x, h=log L and 0<c<1/2 fixed. For k=ceil(cL/h)+O(1), the mass M_k of the exact cut satisfies log M_k=(1−c+o(1))L at **every** sufficiently large x, also if we choose k even or odd at will. The ceiling is 374. For the floor we reserve the largest prime.

Write z=L² and N=π(4z)−π(2z)≫z/h. For every 1≤k≤ceil(cL/h)+O(1), take m as a product of k−1 distinct primes between 2z and 4z. Then log m≤(2c+o(1))L and Y=x/m≥exp((1−2c−o(1))L). Uniformly there are ≫Y/L primes p∈[Y,2Y]. Each mp has Gaussian weight ≥min_{[−log 2,0]}g>0, and p>4z is the only large prime, so all products of this construction are distinct. For k≥2 we obtain

    M_k ≫ (x/L) binom(N,k−1)/(4z)^(k−1)
        ≥ (x/L) (C/((k−1)h))^(k−1).

For k=1 the PNT on [x,2x] suffices. The floor is ≥exp((1−c−o(1))L) simultaneously for all those layers because log(kh)≤h+O(1). In particular the limsup of 374 for a tail of either parity is a limit.

**Consequence for reconstruction attempts via moments.** Fix j=floor(h)+2, d=floor(cL/h). On the layers k=j+i, 0≤i≤d, alter the positive masses by ±A(−1)^i binom(d,i), with A=exp((1−c−η)L), 0<η<1/2−c. The same uniform floor holds up to j+d: j=o(L/h), and its proof only uses k≤(c+o(1))L/h. Since 2^d=exp(o(L)), both choices preserve non-negativity for all large x. They leave intact the layers outside the block and all moments of degree <d, since the finite difference of order d annihilates every polynomial of lower degree. On the other hand the parity balances differ in modulus by 2 A 2^d.

Thus, with only the exterior masses, non-negativity and those exact moments, no estimator of the signed balance has absolute error of square-root scale uniformly for all compatible sequences: one of the two has error ≥A2^d. The perturbations model layer data, not new sets of primes. For an arithmetic proof one can use the divisibility relations between products, which this perturbation does not impose. The obstruction concerns reconstruction in absolute value and does not prove a general impossibility of one-sided majorants for ζ.

**Review record.** The reserved prime satisfies log p≥(1−2c−o(1))L, so it exceeds 4L² uniformly and allows recovering m from each product without multiplicities. The PNT on [Y,2Y] is uniform for all Y≥exp((1−2c−o(1))L), and the denominator log Y can be replaced by L for the floor. The layer bound remains uniform up to (c+o(1))L/h; hence it includes j+d, without wrongly identifying j=O(h) with an O(1). For each parity one takes the first k of that parity not less than the threshold, at distance at most 1, which proves the limit of the tails. Finally A·binom(d,i)≤exp((1−c−η+o(1))L) is o(M_(j+i)) uniformly. The moment identity is exact for polynomials in k=j+i, not only for monomials in i; both perturbed data are compatible and their parity separation is exactly 2A2^d. The conclusion does not require realizing these sequences as masses of integers.
