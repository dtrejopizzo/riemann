# Cancellation of the diagonal by rational quotients in the form of 056

Let P be a squarefree integer and sum the symmetric form of 056 over the pairs, including the diagonal, such that sf(dm)|P. With the conventions of 056, for fixed 0<δ<4, P≤(log x)^(4−δ) and any fixed positive A, the value is

    C_diag L ∏_{p|P}(1−2√p/(p+1)) + O_{A,δ}(L/(log x)^A).

Here C_diag>0. Therefore the part of this block with d≠m has the same main term with the product minus one. If P runs over increasing primorials within that range, its off-diagonal contribution is −C_diag L+o(L). There are no coprimality restrictions on the index w.

**Value of each quotient.** Write d=at,m=bt with gcd(a,b)=1 and t=gcd(d,m). If both values of μ are nonzero, r=ab is squarefree, sf(dm)=r and μ(d)μ(m)=μ(r)μ²(t)1_{(t,r)=1}. In the variable u=t√r/L, after removing the cutoffs U and d,m>D, the mean of the two logarithms equals exactly log u. The remaining kernel is F(u)=Σ_w β(w)V(u²w/4), common to all quotients.

**Uniformity of that removal.** If one of the lower limits fails or a U differs from one on the support of V, then u≤C√P/(log x)²≤C(log x)^(−δ/2). For U this follows from dw≤C L√P/u on the support, and analogously for mw. For the lower limits use min(d,m)≥Lu/√P. On this interval the sum over w, for each of the two cutoffs separately or without cutoff, is O_N(u^N) for every fixed N. The dyadic proof of 056 applies with w of size comparable to u⁻²: at w=ij the derivatives of the cutoff U(di j) or U(mi j) in the long factor cost their inverse scale, uniformly in d,m. The discrete logarithms cost at most O(log x). There are at most 3^ω(P)≤P² quotients and O(L) samples t per quotient. Choosing N large according to δ,A proves the stated error.

The function f(u)=log(u)F(u) has compact upper support and extends by zero with bounded variation at the origin: applying u∂_u to V(u²w/4) the rapid-decay proof gives the same bounds. The elementary count
     
    Σ_{t≤T,(t,r)=1} μ²(t) = (T/ζ(2))∏_{p|r} p/(p+1) + O(τ(r)√T)

is obtained from the expansion μ²(t)=Σ_{k²|t}μ(k) and the count of coprimes by inclusion-exclusion. Thus partial summation of f(t√r/L) gives for the quotient a/b the term C_diag L μ(r)/√r times ∏_{p|r}p/(p+1), with error O(τ(r)√L). The sum of these errors costs √L times a fixed power of log x. For each p|P one can omit p, include it in a or include it in b. Multiplying the three contributions gives the product of the statement. Its factors lie in (0,1), and the product tends to zero along increasing primorials by divergence of Σ_p 1/√p.

**Sign of the constant.** Write η(s)=(1−2^(1−s))ζ(s), and V̂(s)=∫V(t)t^(s−1)dt. The Mellin transform of F at z is 2^(z−1)V̂(z/2)η(z/2)², by substitution where the series converges absolutely (Re z>2) and then by continuation down to z=1. The proved decay of F and its upper support justify differentiation at z=1. By 044 the hat satisfies W(t)=t⁻¹W(1/t); thus Ŵ' at 1/2 is zero. The law of 047 has mean 1/2, so that V̂'(1/2)=V̂(1/2)/2. The constant of 056 is therefore

    C_diag = V̂(1/2)η(1/2)² [log 2 + 1/4 + η'(1/2)/η(1/2)] / ζ(2).

For s>0, η(s) is the expectation of 1/(1+exp(−T)) with T gamma-distributed with shape s and rate one, by the integral of the alternating series. Its derivative is the covariance of that function with log T, strictly positive because both are strictly increasing. This proves the sign without numerical estimation.

**Limit of the extrapolation.** Already for the quotients p/1 with p prime, the sum of the absolute values of the individual constants diverges as a series: its terms are C_diag√p/(p+1). Consequently the expansion by quotients does not admit a summable majorant of the absolute values of its normalised contributions, uniform when passing to the limit in x. The grouping of the product above is essential. It remains to control the pairs with sf(dm) not dividing P. The evaluation extends the diagonal of 056; it uses classical density tools and Euler products.
