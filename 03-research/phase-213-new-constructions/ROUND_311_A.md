# Simultaneous trimming of the large and small arguments in the sieved average

Fix any D=D(x)=x^o(1) with D≥2. With the weights w_D of 310, for 0≤t≤1 and large x there exists V between 2 and 4 such that

    |Σ_(x/V<n≤x) w_D(n) B_t(x/n)| ≤ x^o(1).

One can even make this tail vanish exactly by allowing a partial weight at a single endpoint. Hence the average of 310 keeps the square-root ceiling after removing that tail. At t=0 one can choose V=V(x)→∞ without requiring a rate, keeping the same error. If in addition D→∞, outside the main sample B₀(x) only arguments in [V,x/D) remain. The growing threshold of this last statement has been proved only for the first row.

**Distribution of the weights in proportional intervals.** Let W_D(v)=Σ_(n≤v)w_D(n). Freeze D when evaluating at several scales. With h=h_D of 310, supported on n≤D⁴, the elementary formula Σ_(n≤u)τ(n)=u(log u+2γ−1)+O(√u) gives for v≥D⁴

    W_D(v)=v(A log v+E)+O(√v D^(1+o(1))),
    A=Σ h(n)/n,   E=(2γ−1)A−Σ h(n)log(n)/n.

Here and for bounded D the error is interpreted as O_ε(√v D^(1+ε)): the lcm estimate of 310 is also valid at σ=1/2. For each fixed D, A≥0 on letting v→∞, by positivity of W_D. On the other hand W_D(x)≫x/log x uniformly for D=x^o(1) since w_D(p)=2 for every prime p>D. The constraint W_D(√x)≥0, applied to the same polynomial, gives A log x≤2 W_D(x)/x+O(x^(−1/4+o(1))). Thus, for each compact interval of positive c,

    W_D(cx)/W_D(x)=c+O(1/log x)

uniformly in c (with a constant depending on the compact set, and for x sufficiently large depending on D(x)). This avoids assuming that the second coefficient E is small compared to the first.

**Choice of the endpoint.** For fixed V, interchanging the two sums gives exactly

    Σ_(n>x/V; n≤x)w_D(n) B_t(x/n)
        = Σ_(m≤V)b_t(m)[W_D(x/m)−W_D(x/V)].

Dividing by W_D(x), the right-hand side is J_t(V)+O_V(1/log x), uniformly in the frequency, where J_t(V)=Σ_(m≤V)b_t(m)(1/m−1/V). At V=2 and 4 the profiles have opposite signs with uniform margin on [0,1] by 303. The jumps when moving the endpoint in that interval cost at most O(max_(n≤x)τ(n)^3)=x^o(1) because the arguments of B are bounded and |Σ_(d|n,d≤D)μ(d)|≤τ(n). Choosing an endpoint of the jump that changes sign proves the ceiling, or interpolating only its weight between zero and the original one gives exact cancellation. At t=0, J₀(V)=−1+3/V between 2 and 4; in particular the first crossing there is at V=3+O(1/log x) by the uniform estimate on that compact set.

**Extension at t=0.** By 304 there are fixed intervals [A_j,B_j] with A_j→∞ and strictly opposite signs of the profile at their endpoints. For each j the signs transfer to the sieved tail for sufficiently large x. The jump is bounded by max_(v≤B_j)|B₀(v)| max_(n≤x)τ(n)^3. Delay passing to interval j until the first factor is ≤x^(1/j) and B_j D<x; this gives the required diagonalization. In the remaining average, the positivity of the weights does not by itself provide the floor needed for the sum of intermediate dilations. The trimming of the prime block of 303–304 and the trimming established here affect different sums: here one controls the tail of the average that already has a square-root ceiling.
