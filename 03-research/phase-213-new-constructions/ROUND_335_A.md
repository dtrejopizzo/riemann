# Threshold of the weights on the common divisor

With the classes B_q of 334, including the diagonal, fix 0<κ<1 and put V_m(κ)=Σ q^κ |B_q|. At widths h→0 with log(1/h)=o(m),

    limsup V_m(κ)^(1/(2m)) = max{1/(3/2−Θ), 1/(1−κ/2)}.

In particular no weight q^κ with arbitrarily small κ>0 preserves the ceiling one under RH. On the other hand every fixed weight 1≤w(q)≪_ε q^ε for each ε>0 preserves exactly the rate of 334, by comparison and letting κ→0. This includes fixed losses by powers of the number of divisors.

**Ceiling.** The dual argument of 334 with |b(q)|≤q^κ gives |(μ*b)(g)|≤g^κτ(g). On the discs of radius r it therefore suffices to require σ=3/2−r>max{Θ,(1+κ)/2}. The sum of the Gram J_g with those weights converges by the bound of 334, taking 2ε<2σ−1−κ. The loss from height is subexponential. The exchanges are also absolute at fixed order: off the diagonal 331 is used with Σ g^(κ−2)τ(g)<∞; on the diagonal the total weight per n is ≤n^κτ(n)^2, summable against l_m(n)^2. The ceiling is obtained by taking r to its extreme.

**Arithmetic floor.** Besides V_m(κ)≥V_m(0), choose b(q)=q^κ. Its inversion c(g)=g^κ∏_{p|g}(1−p^(−κ)) is positive. Thus V_m(κ)≥Σ c(g)J_g. In the Gram of the multiples of a prime p the sample n=p has support disjoint from those of 2p,3p,… when h<log 2. Its individual contribution equals l_m(p)^2 by K(0)=1 and the remaining Gram is nonnegative. Therefore

    V_m(κ) ≥ Σ_p (p^κ−1) l_m(p)^2.

Take X=exp(2m/(2−κ)). The prime number theorem gives ≫X/log X primes between X and 2X. That block contributes ≫ X^(κ−2)(log X)^(2m)/((log X)(m!)²). By Stirling its 2m-th root has lower limit at least 2/(2−κ). The floor only needs h<log 2 and also holds in the exponential windows of 326. Under RH in those windows the corresponding ceiling is obtained by the same argument of 334 with arbitrarily small height exponent.

**Use for the closure.** A proof by classes can absorb subpolynomial losses in q at the level of the rate. If it pays a fixed power of q over the complete classes, the first sample of each prime progression already prevents the ceiling one. For classes with the diagonal subtracted this floor has not been proved.
