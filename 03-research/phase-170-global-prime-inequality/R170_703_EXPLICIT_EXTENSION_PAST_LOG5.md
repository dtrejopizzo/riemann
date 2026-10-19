# R170_703 — Explicit extension after prime 5 enters

Theorem derived analytically from the `thm:log5W`
certificate of Paper 47; that certificate is not re-run here.

## Result

Let
\[
 T_0=\tfrac12\log5,\quad L=10^{24},\quad
 \varepsilon=\frac{T_0}{4}e^{-L}>0.
\]
Then, for every `0<T≤T₀+ε`, the full form satisfies
\[
 W_T(F)\ge \tfrac12\,10^{-18}\|F\|^2.
\]
The result holds on the form domain. In L² outside that domain, the
archimedean term is +∞ and the target inequality is automatic. The
width is an explicit exact number; it should not be evaluated with
ordinary floating point, where it would round to zero. Its size does
not represent a practical numerical improvement nor a uniform
mechanism up to T infinity.

## Continuity constants, with no implicit constants

We normalize `||F||=1` on `(-T₀,T₀)`, set `r=1+s`, `0<s≤1`, and
`U_rF(t)=r^{-1/2}F(t/r)`. We define
\[
 Q(F)=\frac1{2\pi}\int\log(2+|\tau|)|\widehat F(\tau)|^2d\tau.
\]

**Archimedean.** We have `sup |τm'(τ)|<10`. Indeed, with `y=|τ|/2`,
\[
 \tau m'(\tau)=2y^2\sum_{k\ge0}
 \frac{k+1/4}{((k+1/4)^2+y^2)^2}.
\]
The k=0 term is ≤2. For k≥1, the sum is bounded by
`(5/2)y² Σ k/(k²+y²)²`. If y≤1, it is ≤5, using
`Σ k^{-3}≤2`. If y≥1, the function `f(x)=x/(x²+y²)²` is unimodal,
`Σ_{k≥1}f(k)≤∫₀∞f+2 sup f`, `y²∫f=1/2` and
`y² sup f≤1`; hence it is ≤25/4. In both cases the total is <10.
Thus the archimedean variation is ≤`10 log r≤10s`.

**Primes.** Both forms can be summed over `2≤n<25`, including the
terms that vanish by support. The sum of their weights
`v_n=2Λ(n)/√n` is <200: there are 23 indices and each weight is less
than `2 log25<7`. With `δ=4T₀s/(1+s)`, the frequency separation at
`|τ|=δ^{-1/2}` gives exactly the estimate of lemma contT:
\[
 |\Delta_{primes}|\le200\sqrt\delta+
 \frac{400}{\log(2+\delta^{-1/2})}Q(F).
\]
This includes the entry of prime 5; the set of contacts is not frozen.

**Polar.** For `1≤r≤2`, `T₀<1`, the functions
`f_{±,r}(t)=√r e^{±rt/2}` have L² norm <6 and their derivative with
respect to r has norm <5. By Cauchy–Schwarz and the product rule, the
derivative of the polar term has modulus <120, and we use the
conservative bound `200s` for its variation.

**Control of Q.** `log(2+|τ|)≤m(τ)+8`: for |τ|≤2 we use
`m(τ)≥m(0)>-6` and `log4<2`; for |τ|≥2, lemma mbounds(ii)
of the paper gives an even smaller constant than 4. At T₀ the sum of
the weights of 2,3,4 is <3 and `|polar|≤4 sinh T₀<5`. Hence
\[
 Q(F)\le W_{T_0}(F)+20.
\]

## Explicit substitution and proof

We take `s=e^{-L}/4`. Then `δ≤e^{-L}` and, writing
`α=210s+200√δ`, `β=400/log(2+δ^{-1/2})`, we have
\[
 W_{rT_0}(U_rF)\ge(1-\beta)W_{T_0}(F)-20\beta-\alpha,
 \qquad\beta\le800/L.
\]
Also `α≤253e^{-L/2}≤506/L`, by `e^{L/2}≥L/2`.
With `g=10^{-18}`, the Paper 47 certificate gives
\[
 W_{rT_0}(U_rF)\ge g-\frac{16506+800g}{L}>g/2.
\]
The last comparison is exact rational. The dilation is unitary and
preserves the form domain. Taking infima gives the bound at `T₀+ε`,
and monotonicity under extension by zero transmits it to every smaller
window. No regularity of an eigenvector is required.

## Scope

This quantification closes the local extension that had been
unquantified. Its exponential dependence on an inverse gap bound comes
from the logarithmic control of the translations on the form domain. A
useful window would require better estimates or directly extending the
certificate with its control of the infinite complement. Iterating
continuity does not rule out the widths summing to a finite interval
while the gap tends to zero.
