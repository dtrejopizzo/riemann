# Unavoidable cost of taking absolute values on a vertical of the neutralized product

**Status: PROVED, with independent review of the uniformity over all verticals σ≥1/2.**

For z=L² and either of the two cuts y of 387, let D(s)=∏_{z<p≤y}(1−p^(−s)). Define the absolute-value majorant of the Mellin integral

    M(σ)=x^σ exp((σ−1/2)²/2) ∫ exp(−t²/2)|D(σ+it)| dt / (2π).

Then inf_{σ≥1/2} M(σ)=x^(1+o(1)). At σ=1/2 there is even a band of width ≍1/log y with log |D|≫√y/log y. The orientation and the sign of the true pulse are lost before reaching square-root scale in this majorant.

**Verticals close to one or to its right.** For a standard normal T, the mean of the logarithm of the modulus equals exactly

    E log |D(σ+iT)|=−Σ_{z<p≤y}Σ_{k≥1} p^(−kσ) exp(−(k log p)²/2)/k.

It is o(1) in absolute value uniformly for σ≥1/2, by comparison with the convergent series over integers n>z. Jensen gives M(σ)≫x^σ. For σ≥1−40 log L/L this yields M(σ)≫x/L^40.

**Verticals further to the left.** Set b=log y∼L/2, d=1−σ≥40 log L/L and take 0.95π/b≤t≤1.05π/b. On y^(3/4)≤p≤y we have cos(t log p)≤−c, and hence log|1−p^(−σ−it)|≥c' p^(−σ). With p∈[y/2,y] alone one obtains ≫y^d/b by the PNT. The smaller primes could subtract at most O(Σ_{z<p≤y^(3/4)}p^(−σ))≪y^(3d/4) log b by Mertens, since p^(−σ)≤p^(−1)y^(3d/4). The quotient of this cost by the floor tends to zero uniformly since b log b exp(−bd/4)=o(1). Thus log |D|≫y^d/b on the whole band. Even at the minimal endpoint d this floor exceeds L² for large x, more than compensating the width and the decrease of x^σ.

Finally M(1)≪x exp(Σ_{p≤y}1/p)≪x log y. The two extremes prove the exponent of the infimum. The result holds for these products with a minus sign in each factor: the loss in absolute value in the inverse product of 370 had a different orientation. This obstruction concerns the absolute majorant over whole verticals with σ≥1/2; it leaves available the phase of the integrand, arithmetic groupings and non-vertical contours.

**Review record.** The logarithmic expansion is uniformly summable for σ≥1/2, since p^(−σ)≤z^(−1/2)<1; after averaging the Gaussian it is dominated by the tail of Σ_{n>z} n^(−1/2)exp(−(log n)²/2)=o(1), including prime powers. With the normalization of M, Jensen gives M(σ)≥(1+o(1))x^σ exp((σ−1/2)²/2)/sqrt(2π), so it also covers arbitrarily large σ. On the left range d∈[40log L/L,1/2], one has bd≥(20−o(1))log L: the negative quotient is O(L log L·L^(−5+o(1)))=o(1) uniformly, and the floor y^d/b≥L^(19−o(1)) exceeds L² with margin. The band has width≍1/b and Gaussian weight bounded away from0; its contribution uniformly beats any decrease of x^σ for σ≥1/2. Consequently x/L^40≪inf M≪xL, which implies exactly the exponent claim, without claiming an asymptotic constant for the infimum.
