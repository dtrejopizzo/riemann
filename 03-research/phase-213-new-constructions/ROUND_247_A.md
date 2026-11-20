# A barycentre of primes with linear weights and minimum at prime endpoints

Let C(x)=Σ_{p≤x}(log p)(1−p/x)(3p/x−1). The global sign of paper 47 is equivalent to C(q)≥0 for every sufficiently large prime q. At each endpoint this says that the average of the primes p<q, weighted by (q−p)log p, is at least q/3. It is also equivalent to a single comparison of integer products, grouping the factors p^|(q−p)(3p−q)| according to the sign of the exponent. The threshold q/3 is exactly the barycentre of the continuous linear weight on [0,q].

**Choice of the weight.** Compared with the variable order of 245, three integrations with distinct poles 0,−1,−2 give a polynomial weight. The transform K(s)=∫₀¹(1−y)(3y−1)y^(s−1)dy=2(s−1)/[s(s+1)(s+2)] kills the main term. For the sum with von Mangoldt, Perron gives under RH −Σ K(ρ)x^ρ+O(1+log²x). One can shift from Re s=2 to −1/2: only the origin is additionally crossed; on the shifted line ζ'/ζ has logarithmic growth and K decays quadratically. The horizontals disappear by the zero-free heights of Z3. The inversion holds even at nodes since the weight vanishes at 1. The squares removed from the sum contribute (K(1/2)/2+o(1))√x by the prime number theorem and partial summation in p/√x; the higher exponents cost O(x^(1/3)polylog x).

On the line |ρ−1|=|ρ| and |ρ+j|≥|ρ| for j=1,2. Therefore

    |C(x)/√x−4/15| ≤ 2(2+γ_E−log(4π))+o(1)<0.094+o(1).

Here −K(1/2)/2=4/15 and the sum of reciprocal squares of the zeros from selection 092 was used. In the reverse direction, the transform in x of C for Re s>1 is K(s)Σ_p(log p)p^(−s); it extends to Re s>1/2, regular on the real half-line there and with poles at all zeros off the line to the right. Landau as in 243 prevents an eventual sign if any of those poles exists.

**Specific arithmetic step.** Between two consecutive primes write x²C(x)=−A₀x²+4A₁x−3A₂, with A_j=Σ_{p≤x}p^j log p. The expression is continuous when a prime enters and concave on the whole closed interval between primes. Two nonnegative endpoints guarantee the whole interval. The same observation holds for any constant margin in x²C(x), without additional control of the gaps between primes.

**Check and antecedents.** verify_247.py encloses the logarithms by scaled integers and verifies the 9591 endpoints from 3 to 99991. By concavity this certifies C(x)>0 on all of [3,99991]. The positive bias by squares, domination by the Hadamard sum and one-sided detection are already in 092 and 127. The contribution here is the polynomial weight of two moments with exact cancellation of the main term and the reduction by concavity to the primes themselves. None of these identities proves for now the comparison of products for arbitrarily large primes.
