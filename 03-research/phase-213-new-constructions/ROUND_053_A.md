# Where the positive term of 052 is compensated in the rows 3L<p<4L

Fix the order-two weight and K of 049–052. In the rows marked by a prime 3L<p<4L, write t=vm, X=y/p, J=K/p comparable to (log L)². With ε(v)=(−1)^(v+1), the weight is log p·ε(v)U(pv)μ(m)V(t/X). The compensation on primes of 050 does not intervene. In the formulas p|m is excluded at cost O(L) by 051.

Let H be the sum over these rows over the t with a prime q>√t, and F the sum over its complement. Then, with C=log(4/3) log(2) ∫V>0,

    H = C y/(log L)² + O(y/(log L)³),
    F = −C y/(log L)² + O(y/(log L)³).

Moreover, H+F=O_N(y/(log L)^N) for each fixed N. This last bound is still larger than the required precision O(L) at large scale.

**Computation of H.** There is a unique writing t=dq with q prime and q>d. On the support q≫√L, so that a multiple v of q cannot satisfy U(pv)≠0. Thus v|d and μ(t/v)=−μ(d/v). If q=p, then d=O(1) on the support and the total cost of that exclusion is O(L). Nor can p divide d since d≪√L. Replacing the cutoff by one in the coefficient −Σ_{v|d}ε(v)U(pv)μ(d/v) gives exactly −1_{d=1}+2·1_{d=2}, by divisor inversion. That value was already evaluated in 052. It remains to control uniformly the cost of the replacement for all d, which can now grow like √L.

Let d=hv. By the quantitative PNT and partial summation, the sum over q>hv of V(qhv/X) can be replaced by its integral with density 1/log q. Its error is O_N(X/[hv(log L)^N]), since on the effective support q is comparable to X/(hv) and q≫√L. The moving endpoint q>hv is admitted in the partial summation. Only hv≪√L intervenes; through the two harmonic sums at most two powers of log L are lost. In the integral put s=qhv/X. The condition q>hv gives v<B=√(Xs)/h. For s in the fixed support of V the correction, with its global sign omitted when bounding it, has the form

    X ∫ V(s) Σ_h μ(h)/h Σ_{v<B} ε(v) f(v) ds,
    f(v)=[U(pv)−1]/[v log(Xs/(hv))].

The inner sum is zero for B≤J. For B>J one has log(Xs/(hv))≫log L, and f vanishes up to J. On [J,B], |f(B)|≪1/(B log L), |f'(v)|≪1/(v² log L), |f''(v)|≪1/(v³ log L); the derivatives of the cutoff only intervene at v comparable to J. The alternating sum is bounded by C(1/B+1/J²)/log L. To see this, shift twice by an integer the sum with alternating signs: four times the sum is the alternating sum of second differences plus boundary terms. The second differences cost at most a constant times ∫|f''| and the final boundary terms O(1/(B log L)); the initial ones vanish when extending f by zero. The same argument holds for non-integer B.

When summing 1/h for h≤√(Xs)/J, the term 1/B costs O(1/J) and the term 1/J² costs O(log L/J²). Therefore the error per p is O(X/(log L)³). Summing log p over 3L<p<4L one obtains O(y/(log L)³). The main term and its constant are those of 052, also using the quantitative PNT for the outer sum.

**Computation of the complement.** In the whole row sum first over m. For each v≤eJ, the scale of m is X/v≫L/(log L)². The quantitative PNT for μ, with the fixed smooth weight V, gives O_N(X/[v(log L)^N]) uniformly. Summing over v and p costs a harmonic sum in v and Σ(log p)/p=O(1); increasing N absorbs that loss. The eventual exclusion p|m costs O(L). This gives the estimate for H+F and, subtracting H, that for F.

**Scope.** The positive term of 052 is compensated, to main order, within the interval of marked primes itself, by cofactors all of whose primes are ≤√t. The decomposition by the largest prime is classical. The new estimate with respect to 052 is that admitting all d<q alters the computation only by O(y/log³L), and this identifies the class that supplies the negative term. The square-root precision of the total sum remains open.

**Square-root precision in this block.** For a marked prime 3L<p<4L, the sum without U is Σ_v ε(v)g(pv/y)=V(p/y)−2V(2p/y)=0. The high part has integral zero when combining the progressions of step one and two. By 047 its absolute value is ≤C(y/p)exp(−c√(K/(2p))). Summing log p and fixing the constant of K sufficiently large, the complete block, before excluding p|m, is o(L). If m=pw, the support forces vw=O(1), so that U(pv)=1 and p∤w for large x. For each product vw the convolution ε*μ is δ₁−2δ₂. Thus the contribution with p|m is exactly Σ_p log p [−V(p²/y)+2V(2p²/y)] in this block. In the notation above,

    H+F = C₁ L+o(L),    C₁=∫₃⁴[V(u²/2)−2V(u²)]du > 0.

The asymptotic equivalence follows from PNT and partial summation. For the sign, on e≤t≤16 the averaged hat of 047 equals c[64P(3/2)t⁻²−P(−3/2)t/64], with c=64/4097 and P(z)=∫exp(zv)dν(v). It is the upper branch of 044 throughout the whole average. One obtains C₁=c[(74/81)P(3/2)+(37/128)P(−3/2)]. This estimate uses the quadrature mechanism of 049 in the parity of the rows, instead of first estimating the sum over m.
