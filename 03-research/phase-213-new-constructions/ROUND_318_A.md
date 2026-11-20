# Cut at X^(2/3) with mean-square error sufficient for the global sign

Fix the dyadic scale X, V=X^(2/3), H=ceil(X^(1/6)) and D=X^o(1), D≥2. Keep fixed on [X,2X] the weights g of 317, with q=⌊D⌋+1. For x in that interval let I(x,t) be the average, over j=0,…,H−1, of

    Σ_(D<n≤floor(x/V)−j) g(n) C_t(x/n).

Then uniformly in 0≤t≤2,

    (X^(−1)∫_X^(2X) |C_t(x)+I(x,t)|² dx)^(1/2) ≪_ε X^(1/2+ε).

All arguments of I lie between X^(2/3) and x/D. In particular the global sign is equivalent to the mean over x and t∈[1,2] of (−I(x,t))₊ being O_ε(X^(1/2+ε)) at all dyadic scales. This reduction replaces the pointwise guarantee of 317 by a mean-square guarantee; the sufficiency criterion does not need pointwise control.

**Eliminating the boundary term.** The full mean of g against C_t already satisfies the pointwise ceiling by 317. Write G(u)=Σ_(d≤D)μ(d) r_q(u/d), where r_q(v)=⌊v⌋ mod q in [0,q−1]. For N=⌊x/V⌋−j the omitted tail is Σ_(m≤x/N)c_t(m)[G(x/m)−G(N)] (an endpoint with equality contributes zero). For m≤V it is valid for all j. The additional m lie in a stretch of length O(1+HV²/X), which costs O_ε(X^(1/2+ε)) by |G|≤qD and |c_t(m)|≪_ε m^ε. In each term d, when averaging G(N) over H consecutive integers, the period qd has mean (q−1)/2. The error of a partial period is O(q²d/H). Summed over d and multiplied by |C_t(V)|≪_ε V^(1+ε), it costs O_ε(X^(1/2+ε)). Thus the tail only requires bounding in mean square

    E(x)=Σ_(m≤V)c_t(m) Σ_(d≤D)μ(d)[r_q(x/(dm))−(q−1)/2].

**Frequencies of the residues.** The Fourier series of the centered r_q(v) has coefficients O(q/|h|) in the nonzero modes exp(2πi h v/q), by total variation over one period. Group the frequencies h/(qdm) as reduced fractions a/b with the sign in a. One has b≤qDV. For fixed d and given b, write m=j b/gcd(b,qd); then |h|=|a|j qd/gcd(b,qd)≥|a|j. By the harmonic sum, even truncating the modes, the total modulus for each a/b is O_ε(X^ε/|a|), since D,q are subpower. The sum of squares of these coefficients is O_ε(V X^ε). Two distinct frequencies are at distance at least (qDV)^(−2).

For a finite sum with separation Δ, its integrated square over an interval of length X is bounded by O(X+1/Δ) times the sum of squares: majorize the indicator by a multiple of sinc²((x−3X/2)/M), with sinc(u)=sin(πu)/(πu) and M≥2 max(X,1/Δ); its triangular transform suppresses the distinct pairs. Apply this bound to the Fejér sums of the series of the residues and pass to the limit by Fatou (the jumps form a null set). Therefore

    X^(−1)∫ |E|² ≪_ε (1+V²/X)V X^ε ≪_ε X^(1+ε).

The compensation is between frequencies of residues along the scale x. Averaging the endpoints N is essential in this proof: without it the product G(⌊x/V⌋)C_t(V) remains, which the argument does not control at root scale.

**Why the mean in x suffices.** The positive part is 1-Lipschitz, and Cauchy–Schwarz allows replacing the mean of (−I)₊ by that of (C_t)₊ with root error. Under RH the pointwise ceiling of 317 suffices. If there were an exterior zero, choose as in 292 a smooth nonnegative average in frequency that preserves a pole of the quotient with a single denominator of 317. Call A(x) the averaged summatory function; the integrated dyadic ceiling for (C_t)₊ implies X^(−1)∫ A₊≪_ε X^(1/2+ε). By summing blocks the Mellin transform of A₊ is holomorphic in Re s>1/2. The Mellin transform of A is regular on the real axis of that half-plane and has the exterior pole. Hence the Mellin transform of the negative part A₋=A₊−A would be regular on that whole real axis and would have a nonreal pole there to the right of the critical line. Landau for A₋≥0 prevents this. The ceiling of the negative part of the intermediate block remains unproved.

The large sieve for separated frequencies is classical. Here it is applied to the fractions of the residues after grouping coinciding denominators and compensating the endpoints; no novelty is attributed to the separation principle itself.
