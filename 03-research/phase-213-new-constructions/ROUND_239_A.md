# One and the same smoothed count with growing fit at two near-linear scales

Fix a single density W: the convolution of the uniform probabilities on [0,1/(10j²)] for all j≥1. Let H(s)=∫W(v)exp(sv)dv and form with the authentic primes

    A(t)=Σ_p (log p) W(log p−t) − exp(t) H(1).

It is a finite local sum. Fix m=floor(t/(log t log log t)) for large t and measure

    D(t,h)=exp(−t) inf_(deg P≤m) ∫₀ʰ |A(t+v)−P(v)|²dv,

over real polynomials in v. For the SAME W and the SAME degree m(t) one obtains:

1. If 0<h≤1 and log(1/h)=o(log t), then log(1+D(t,h))/t→2B.
2. If h=exp(−log t log log t), one has D(t,h)≤exp(−t+o(t)) for EVERY large t without hypotheses.

With X=exp(t), the second physical length is X(exp(h)−1)∼X/(log X)^(log log log X), of order X^(1−o(1)). Therefore even the description "window of length X^(1−o(1)) with small error" does not suffice for this fit; what matters is the value of h. This smoothed observable and its fit of growing degree are distinct from the unfitted cosine of 238.

**Fixed kernel.** The lengths a_j=1/(10j²) are summable and give a probability of compact support in [0,1/5]. To control the derivative of order r, differentiate the first r factors (variation ≤2/a_j each), bound in supremum the next one by 1/a_(r+1) and leave the other probabilities undifferentiated. One gets ||W^(r)||∞≤C^(r+1)((r+1)!)². Differentiating an additional factor justifies the smooth representatives. Moreover H(s)=∏(exp(sa_j)−1)/(sa_j) does not vanish for Re s>0: no factor vanishes and the tail differs from one by an absolutely summable sequence at fixed s. The continuous main term of the prime sum is exactly exp(t)H(1).

**Why it still detects zeros after removing so many coefficients.** If B>0 fix β₀=Re ρ₀>1/2 and σ between 1/2 and β₀. Build as in 231 a base filter of mass one supported in [0,h/2], annihilating the other zeros of β≥σ at ρ−ρ₀. Its norms up to two derivatives cost exp(o(t)) in regime 1. Convolve furthermore m+1 copies of

    (δ_l−exp(−ρ₀ l)δ₀)/(1−exp(−ρ₀ l)),    l=h/[4(m+1)].

Each one has mass one, variation O_(ρ₀)(1/l) for large t and a zero at −ρ₀. The total new cost is exp(O(m log((m+1)/h)))=exp(o(t)). The final filter f_t preserves mass, support inside [0,h] and the bound exp(o(t)) for its norms of order ≤2 and its L² norm. Its transform has a zero of order ≥m+1 at −ρ₀. By differentiation this gives ∫f_t(v) exp(−ρ₀v)P(v)dv=0 for ALL polynomials of degree ≤m, including those chosen from the data.

Apply the explicit formula for dψ as in 236. The logarithmic convolution by W multiplies the term of each zero by H(ρ), uniformly bounded in the strip. The main term has been subtracted. The filter in v, with the factor exp(−ρ₀(t+v)), leaves −mult(ρ₀)H(ρ₀)≠0. The zeros β<σ cost exp(−(β₀−σ)t+o(t)) by parts twice and Z3. The trivial terms and the higher prime powers also disappear after normalisation: the latter cost O(exp(t/2)poly(t)) before the filter by fixed support and boundedness of W. Cauchy–Schwarz, uniformly in P, gives D(t,h)≥exp((2β₀−1)t−o(t)). For the ceiling take P=0 and use θ(x)−x=O_ε(x^(1/2+B+ε)) from 235 by parts with the fixed W. This includes B=0 and concludes 1 without assuming that the supremum is attained.

**Direct bound on the good windows.** On [t,t+1], Chebyshev on the fixed support gives for each r the bound |A^(r)|≤exp(t) C^(r+1)((r+1)!)², increasing C for the subtracted main term. Take as P the Taylor polynomial at t of order m. The logarithm of the supremum of the error on [0,h] is ≤ t+(m+1)log h+O((m+1)log(m+2)). For the h of item 2, (m+1)log(1/h)=t+o(t) and m log m=o(t). The error is ≤exp(o(t)), hence D≤exp(−t+o(t)). It is an approximation bound by smoothness, not a proof of cancellation of the primes at the first scale.

**Optional parameter.** In both computations log log t can be replaced by any ω(t)→∞ with ω(t)log t=o(t), using m=floor(t/(ω(t)log t)) and h=t^(−ω(t)) in 2. The proof of 1 holds for h=t^(−o(1)). Each choice fixes a degree rule for both statements; the rule is not changed after examining the data. The intermediate zone, in particular h=t^(−c) with fixed c>0 for the detection of any displacement by this argument, is not resolved.
