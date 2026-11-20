# The diagonal dominates even when widening the critical window

With the kernel of 325, denote by E_m[h] the signed energy at width h and by Δ_m its diagonal. For every fixed 0≤b<1/50,

    h=4^(−m)m^b   ⇒   E_m[h] ∼ Δ_m ∼ 1/(2ζ(2)√(πm)).

In particular the equivalent at the edge a=log 4 is resolved and it persists in windows wider by a factor tending to infinity. For fixed a with 0<a<log 4 the rate of 327 is also improved to E_m(a)/P_m(a)≪_a m^(−1/50)log m. The exponent comes from the short-interval theorem used, with no claim of optimality.

**Quantitative estimate without discretizing the variable endpoints.** In the widened critical window fix log 4<c<2<C and work in dyadic blocks [Y,2Y] of the zone cm≤log x≤Cm. For h=exp(−am) fixed in exponent it suffices instead that a<c<2<C. In both cases H=⌊hY/m²⌋ grows exponentially and log H, log Y are comparable to m. Define M_H(n)=H^(−1)Σ_(1≤j≤H) μ(n+j). One has uniformly

    (1/Y) Σ_(Y/2≤n≤3Y) |M_H(n)|² ≪ m^(−1/50)log m.

Indeed the long mean of μ in each block is O_A(m^(−A)) by the quantitative PNT. For λ between m^(−1/100) and 1 the additive term O(log log H/log H) and the endpoints of the short sum cost o(λ). Theorem 1 of Matomäki–Radziwiłł, applied with its parameter proportional to λ, bounds the exceptional proportion by O(λ^(−2)m^(−1/50)) plus a superpolynomially small term, since H^(c'λ) grows at least like exp(c''m^(99/100)). Integrate 2λ times that proportion; below m^(−1/100) use the bound one. A bounded number of blocks covers the indicated range. [Theorem 1, pp. 1015–1016](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf)

In the local sum with weight η(log(x/n)/h), replacing μ(n) by M_H(n) costs O(H/(hY)) after normalizing by hx. Indeed, on changing n to n+j the difference of the weights is O(j/(hY)) and is supported on O(hY) integers, by smoothness and compact support. For the new weights, Cauchy–Schwarz majorizes the square of the normalized average by O((hY)^(−1)Σ |M_H(n)|²), with n at distance O(hY) from x. Integrating over x∈[Y,2Y], each n intervenes over length O(hY). This transfers the quantitative estimate without paying a factor for the number of possible endpoints. Replacing l_m(n) by l_m(x) costs another O(h) in the normalized average, as in 327.

**Separation of the two sizes of integers.** By the Gram identity, the central stretch contributes to E_m[h] at most O(m^(−1/50)log m · h binom(2m,m)). In the widened critical case this is O(m^(b−1/50)log m /√m)=o(Δ_m). The diagonal is concentrated at log n close to m, while the weight of the count of distinct pairs is concentrated at log n close to 2m. Since c>log 4>1, the portion of the diagonal included in the central stretch of the Gram integral is exponentially small relative to Δ_m (also shifting the edge by h). Outside that stretch, the absolute mass of the distinct pairs is exponentially small relative to h binom(2m,m): for each n there are O(hn) distinct neighbours; use the mean of squares of the two weights and the gamma tail of 327, with endpoints enlarged by h. By nonnegativity of the kernel this bound serves equally for portions of the Gram integral. Thus, outside the center what remains is Δ_m+o(Δ_m). The sum of the two regions proves the equivalent.

For fixed a below log 4, Δ_m and the previous tails are negligible relative to P_m(a) even after multiplying by any fixed power of m; the central ceiling and 327 give the claimed rate. This gain is polynomial in m. The full criterion needs an exponential gain in the windows a=1/j, so the global sign remains open.
