# A positive Möbius weight computable with three Liouville sums

Set A(z)=Σ_{k≥1}(−1)^(k+1)exp(−k²z) and W(z)=A(z)−A(4z). For each z>0 one has W(z)>0. At scale X≥2 there is an exact identity

    F(X)=Σ_r μ(r)W(r/X)
        =Σ_n λ(n)(1−3·1_{4|n}+2·1_{16|n})exp(−n/X).

The multiples of 16 disappear; the multiples of 4 that are not multiples of 16 have coefficient −2λ(n). The identity works with the true signs. On the Möbius side the band X/(K log X)≤r≤K X log X suffices, with absolute error o(√X) and a fixed constant K large enough.

**Proof.** Jacobi's identity gives A(z)=(1−θ₄(0,e^(−z)))/2. In the product for θ₄ the factors (1−e^(−2jz))(1−e^(−(2j−1)z))² are positive and increasing in z; the product is strictly increasing. Hence the strict sign of W. Grouping by n=rk² in the series of A, the convolution of μ with the indicator of squares is λ. Giving weight −1 to even k instead of +1 subtracts 2·1_{4|n}λ(n/4). The second scale of A subtracts one copy at n multiple of 4. Use λ(n/4)=λ(n) and, when applicable, λ(n/16)=λ(n). The changes of order are absolute for fixed X.

By alternation A(z)≤e^(−z). By Poisson for the Gaussian, θ₄(0,e^(−z))=√(π/z)Σ_{m∈ℤ}exp(−π²(m+1/2)²/z). Thus W(z)≪z^(−1/2)exp(−π²/(16z)) for 0<z≤1. The two tails of the sum over r are paid using |μ(r)|≤1: the upper one costs O(X exp(−K log X)), and the lower one O(X polylog(X) exp(−(π²/16)K log X)) by monotonicity of the majorant for small z. In particular K=10 works for X large.

**Which estimate would close the sign.** An eventual one-sided ceiling F(X)≪ε X^(1/2+ε) for all ε>0 suffices, equivalent to the same ceiling on the cut band. In Re s>1 the two-sided Mellin transform in X with weight X^(−s−1) is Γ(s)η(2s)(1−4^(−s))/ζ(s), η(z)=(1−2^(1−z))ζ(z). No factor of the numerator vanishes in Re s>1/2. The real axis there is regular and the part X<1 is entire after transforming, by the exponential decay. Landau gives sufficiency as in 139. Under RH the two-sided bound follows from M₀(t)≪ε t^(1/2+ε) by Abel; the derivatives of W at both ends have the same exponential decay with power factors, by the two series above.

**What the second alternation of 139 contributed and why only one is used here.** The double coefficient ε*ε already appears in 054/055 and its factor η² in 057. For G(y)=Σ_{i,j}ε(i)ε(j)exp(−(yij)²), alternating the positive decreasing function A(y²i²) gives 0<G<1/2. But the difference G(y)−G(2y) does not inherit a sign from that argument. A single alternation provides simultaneously the strictly positive weight, the exact cancellation of dyadic classes of λ and the localization on both sides without hypotheses on μ. The theta identities, the transform of η and the Landau method are antecedents, not a proof of cancellation in the remaining band. Compare also 047 and 131 for other localizations.
