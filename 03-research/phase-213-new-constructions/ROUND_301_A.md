# Positive families larger than the square root after summing all their square parts

For the odd discrepancy A of 300 write n=d²e, with d,e squarefree, coprime, composed of odd primes congruent to 2 modulo 3. The signed weight is w(d)χ(e)w(e), where w(m)=4^ω(m) on that support and zero outside. Fix 0<δ<1, E=x^δ, an integer h of that support and a finite set F of odd inert primes not dividing h. Include all terms with

    e=h p a,    E<p≤2E inert prime,    a a divisor of the product of F.

The large prime is unique for sufficiently large x; all admissible d are summed. The result is asymptotic to a nonzero constant times x^((1+δ)/2), with sign −χ(h). In particular h=5 leaves a positive contribution larger than the square-root scale even after independently admitting or omitting each prime of F. For h=1 the contribution has the opposite sign. F is fixed when passing to the limit.

**Positive mean of the square part.** For fixed g of the support, the series of w(d) with (d,g)=1 has a double pole at 1 and its partial sum up to Y is asymptotic to

    c Y log Y · ∏_(ℓ|g)(1+4/ℓ)^(−1),     c>0.

Indeed the basic series ∏_(p odd inert)(1+4p^(−s)) factors as ζ(s)²/L(s,χ)² times a correction absolutely convergent for Re s>1/2: the linear term coincides at each prime except 2,3, which are adjusted separately. On Re s=1 the functions ζ and L have no zeros, and at s=1 the correction is positive. Omitting g modifies only finitely many local factors, which can be adjusted before factoring. The Ikehara–Delange Tauberian theorem for positive coefficients and a double pole gives the formula, in particular a ceiling O(Y log(2Y)). To also exclude the moving prime p, the loss is ≤4Σ_(d'≤Y/p) w(d') ≪ (Y/p)log(2Y) if p≤Y and zero otherwise. Thus it is negligible uniformly over the interval considered.

**Constant and sign.** For g=ha and each prime p take Y=√(x/(gp)). The logarithm of Y is uniformly asymptotic to (1−δ)log x/2. The sum of p^(−1/2) over the inert class between E and 2E is asymptotic to (√2−1)√E/log E by the PNT in progressions. For a=1 the contribution is then asymptotic to

    −χ(h) · 4c w(h)/√h · ∏_(ℓ|h)(1+4/ℓ)^(−1)
          · (1−δ)(√2−1)/(2δ) · x^((1+δ)/2).

Admitting all a multiplies that constant by ∏_(ℓ∈F)(1−4√ℓ/(ℓ+4)). Each factor is (√ℓ−2)²/(ℓ+4)>0. The denominator ℓ+4 matters: including ℓ in e loses the option of including it in d. Ignoring that coprimality would even give the wrong sign for some primes.

**Boundary of the argument.** For e≤(log x)^B, the absolute cost is O_B(√x·(log x)^(1+B/2)(1+log log x)^3), since w(e)≤τ₄(e) on its support, Σ_(e≤z)τ₄(e)/√e≪√z(1+log z)^3, and the ceiling for the sum over d holds uniformly when coprimality is omitted. This part does fit in x^(1/2+ε). For e growing like a power, the positive example shows that a block-by-block treatment with only a fixed set of compensating primes cannot give that budget to each block. There may still be cancellation between blocks of opposite signs. No bound for A or for C has been obtained.
