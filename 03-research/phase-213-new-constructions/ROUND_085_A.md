# All dimensions and windows with a bounded sum of reciprocal rates

Let v_j be positive real rates, counted with multiplicity, in any finite number. Assume Σ_j 1/v_j≤1/512. For F(s)=P(s)/∏(s+v_j) strictly proper, f its causal inverse, g=f 1_[0,L], one has in every window L>0

    W(g) ≥ (1/4)||g||².

The full comb and the polar term are kept. There is no prior filter on the numerator nor a bound on the number of poles. Repeated poles and arbitrary coefficients are allowed. By translation or reflection the same statement holds in the centered window and in the opposite orientation. 084 allows smaller rates in dimension ≤13; the two results complement each other.

**Order-independent control.** Normalize ||f||=1. For σ<min v_j, set B(s)=∏(s−v_j)/(s+v_j) and G(s)=B(s)conj(F(−conj(s))). Cancellation of denominators shows that G is rational strictly proper with the same allowed poles, and its Hardy norm on the right half-plane is 1 by |B(it)|=1. On the line Re s=σ use the Hardy contraction toward the interior (Plancherel on the causal inverse of G). Reflecting gives
    
    ||exp(σt) f||₂ ≤ ∏(v_j+σ)/(v_j−σ).

Take σ=128. Then each x_j=σ/v_j≤1/4 and Σx_j≤1/4. Since log((1+x)/(1−x))≤2x/(1−(1/4)²), the product has square ≤exp(16/15)<3. This step allows many poles without the cost depending on their number.

**L≥1/64.** One has ||g||²≥1−3 exp(−2σL)≥1−3e^(−4). By Cauchy, ||g||₁²≤3/(2σ); thus the Fourier mass in |ξ|≤32 is ≤(32/π)3/256=3/(8π). P47 lem:mbounds and monotonicity give m(0)>−6 and m(32)>3/2 (the lower digamma bound there is log(32/(2π))−1/32−1/(2·32²)). Hence Arch(g)≥(3/2)||g||²−(15/2)3/(8π). The two polar moments have product of modulus ≤3/√((2σ)²−1) by weighted Cauchy. For u≥0, |c_g(u)|≤√3 exp(−σu) by Cauchy on the shifted tail and ||g||≤1. The absolute cost of the comb is ≤2√3 Σ_{n≥2}(log n)n^(−128.5)<1/1000 (use log n≤n and integral comparison from 2). Altogether W(g)>0.48 in this normalization and hence W(g)>||g||²/4.

**0<L<1/64.** Here there are no prime contacts. Independently of the rates, ||g||₁²≤L||g||², and the low mass is ≤32L||g||²/π. The polar term costs at most 2L exp(L/2)||g||². Hence
    
    W(g)/||g||² ≥ 3/2−(15/2)32L/π−2L exp(L/2)>1/4.

No external window certificate is needed for this step.

**What class of forms results.** Fix, for example, v_j=512·2^j, j=1,2,… . All finite combinations of these same exponentials belong to a single infinite-dimensional linear space. The bound is inherited on its closure in the form norm, by continuity at fixed window. No extension to its L² closure by mere continuity of W is claimed. The set of all admissible configurations without fixing a sequence is not automatically a linear space.

**Limit of the concentration strategy.** In the confluent case v_j=v, the class itself contains f(t)=t^(n−1)exp(−vt). For that normalized vector, the law |f|²dt is gamma with mean (2n−1)/(2v) and variance (2n−1)/(4v²). In particular at fixed v, as n→∞ the mass of any fixed initial interval tends to zero, and ||exp(σt)f||₂=(1−σ/v)^(−(2n−1)/2) for 0<σ<v. Hence an exponential localization budget uniform in the order cannot be kept in those spaces. This is an obstruction to the argument used; it does not imply negative energy of the vector. The value 1/512 is sufficient and has not been optimized.

**Cross-check.** POWER_COMMON_TRANSFER_010 already estimates weighted norms with rational bases; POWER_STATE_054/060 already give cones in every order by imposing an order-dependent filter. The present application admits all numerators without that filter, simultaneously controls truncation in any window and replaces the dimension bound by Σ1/v_j. Müntz density criteria do not allow deducing the global sign on a sequence with finite reciprocal sum.
