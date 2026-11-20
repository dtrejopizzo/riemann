# Detection of the abscissa by a local mean without the Taylor weights

Fix the same smooth η of 325, with compact support in (0,1) and nonzero integral. For real X, 0<δ<1 and h=X^(−δ), put

    S_h(x)=Σ μ(n)η(log(x/n)/h),     L_δ(X)=∫_[X,2X] |S_h(x)|² dx/x,
    λ(δ)=limsup_(X→∞) log L_δ(X)/log X.

Then lim_(δ→0+) λ(δ)=2Θ. Moreover RH is equivalent to the bound L_δ(X)≪_(δ,ε) X^(1+ε)h for every ε>0 and δ=1/j, j≥2. In each block h is constant. The target is thus equivalent to a mean square of size Xh, up to X^ε, over the centers of intervals of length comparable to Xh. No differentiation orders m nor a maximum over exceptional centers intervene.

**Ceiling.** The Mellin transform of S_h is F(s)k_h(s), with F=1/ζ and k_h(s)=h∫η(v)e^(−shv)dv. For each σ>Θ, on the line Re s=σ one has |F(s)|≪_σ(2+|Im s|)^C by 325. In any fixed vertical strip, |k_h(s)|≪_N h(1+h|Im s|)^(−N) by integration by parts. The inversion on a line of abscissa >1 is shifted to σ by these same bounds, uniform in the strip. Plancherel in log x gives

    L_δ(X) ≪ X^(2σ) ∫ |F(σ+it)k_h(σ+it)|²dt ≪ X^(2σ) h^(1−2C).

Hence limsup_(δ→0)λ(δ)≤2σ. Under RH one can take σ arbitrarily close to 1/2 and C arbitrarily small, as in 326, which implies the ceiling X^(1+ε)h.

**Inverse detection.** For φ smooth with compact support in (0,log 2), integrating S_h against ψ(log(x/X)) and dividing by h replaces the weight in n by T_hψ(u)=∫η(v)ψ(u+hv)dv, u=log(n/X). For each fixed integer K there is ψ_h with the same support control as φ, L² norm uniformly bounded and T_hψ_h=φ+O(h^K) uniformly. Indeed use ψ_h=P(h∂)φ, where P is the formal inverse up to degree K−1 of Σ_{k<K}(∫v^kη(v)dv)z^k/k!. The constant term is invertible and Taylor with bounded remainder justifies the error. For small h both weights vanish outside a fixed compact set, so the sum of errors costs O(Xh^K). Cauchy–Schwarz gives

    |Σ μ(n)φ(log(n/X))| ≪_φ,K L_δ(X)^(1/2)/h + Xh^K.

In particular Θ≤λ(δ)/2+δ: if the right-hand side were less than Θ, choose a positive abscissa between both. A smooth partition of the logarithmic line by translates of such a φ (fixed step less than log 2, normalize an overlapping bump by the periodic sum) decomposes the series of F into geometric blocks X. For s in a compact set to the right of that abscissa apply the last inequality to φ(u)e^(−su) and multiply by X^(−Re s). The constants of the derivatives are uniform there. Choose K with 1−Kδ less than the chosen abscissa. The sum of blocks converges normally, coincides with F in Re s>1 and contradicts a pole to the right of the chosen abscissa. This proves the floor and, together with the ceiling, the limit. Under the proposed bound λ(δ)≤1−δ, hence Θ≤(1+δ)/2 for δ=1/j; let j→∞.

**Scope.** It is a reduction for μ in dyadic mean. The index already records variances of primes and averages in short intervals, and 327–329 use means of μ with logarithmic savings. Here the inverse implication is proved for intervals of length X^(1−δ) with the same fixed smoothing, including the error of undoing the average. Proving unconditionally the ceiling of size Xh is missing.
