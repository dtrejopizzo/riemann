# Limit of the normalized defect in the full cell matrices

Cross-check: 212-75 and 031 give recovery of profiles; P47 lem:compact uses a fixed logarithmic window. Here the logarithmic window grows, but the jump norm provides compactness after scaling the right physical endpoint to one. The uniform error of 032 then allows removing the arithmetic cut. No rate in the discrete size is claimed.

Let H=N+1 and β_N the defect defined in 031. The finite limit Γ=lim β_N/N exists. For fixed L, let X be the completion of C_c^∞(0,1) in I(u)^(1/2), I(u)=∫₀¹ x|u'(x)|²dx; X₀ imposes ∫u=0. With h_L the corrected polar symbol of 032, define B_L(u)=∫h_L(t)|widehat(Uu)(t)|² dt/(2π), extending u by zero outside (0,1). Then

    Γ_L = sup {−B_L(u): u∈X₀, I(u)≤1},   |Γ−Γ_L|≤C/(√(1+log L)).

In particular the sign is equivalent to Γ=0 by 031. On X₀ the formula for B_L is the Fourier one; it does not require interpreting the inverse moment of u, which may diverge.

**Space and repair.** For smooth functions |u(x)|²≤I(u)log(1/x) by integration from 1. Hence X injects into L² (the identification of the derivative is checked on each interior compact set). Moreover ||(Uu)'||²=∫|u/2+xu'|²dx≤C I(u). Both bounds pass through completion. For fixed L, h_L is continuous, bounded below and O_L(1+log(2+|t|)), so B_L is continuous on X. The ordinary moment is continuous. Smooth profiles of zero ordinary moment are dense in X₀: repair any approximation with a fixed bump of integral one.

Both moments can also be imposed in that approximation. For a fixed smooth profile with zero ordinary moment and inverse moment m, choose η smooth on (−2,−1) of integral one, and v_R(x)=R⁻¹η(log(x)/R). Its inverse moment equals one, I(v_R)=R⁻³∫|η'|² and its ordinary moment t_R tends to zero. With a fixed corrector k of ordinary moment one and inverse moment zero (use two separated bumps), v_R−t_R k keeps inverse moment one and has zero ordinary moment. Subtracting m times this function costs o(1) in X for the fixed profile. Applying this repair after each approximation, choosing R according to its m, gives primitive density in X₀.

**Fixed cut L.** Let Γ_{N,L} be the supremum of −a_L over the primitive tests of N cells with HJ≤1, zero included. Scale each test to the interval (0,1) by u(x)=√H f(Hx); this is a translation for U, so its hybrid energy is B_L(u). The steps do not yet necessarily belong to X. Interpolate linearly their values u_j=√H f(j) at j/H for j=0,...,H, with u_0=u_H=0. The interpolant v satisfies

    I(v)=Σ_{j=1}^H (j−1/2)|u_j−u_{j−1}|² ≤ HJ,
    ||v−u||²= (1/(3H))Σ_{j=1}^H |u_j−u_{j−1}|² ≤1/(3H).

Each v belongs to X by H¹₀(0,1) approximation. Its unit ball is relatively compact in L²: on [δ,1] use the H¹ bound and on (0,δ) integrate log(1/x). Extract for almost optimal interpolants weak convergence in X and strong convergence in L² to a limit u_* of X₀ with I≤1. The ordinary moment passes from the steps. By unitarity the transforms of the steps also converge strongly in L². Subtracting a constant lower bound of h_L and applying semicontinuity of its nonnegative integral gives B_L(u_*)≤liminf B_L(u). Thus limsup Γ_{N,L}≤Γ_L, including u_*=0.

For the other direction, use density of smooth primitive profiles and continuity of B_L on X. Sample each one on the mesh 1/H and repair both moments as in 031: on the interior compact support the convergence in form norm and HJ→I are those of the Riemann sums of 031 with K=H and b=1. The interior support leaves the initial cell free. Scaling the amplitudes if HJ>1 costs a factor tending to one when I≤1. Hence Γ_{N,L}→Γ_L.

**Removal of the cut.** By 032, |β_N/H−Γ_{N,L}|≤C/√(1+log L) uniformly in N. The sequence β_N/H is bounded by 032; its upper and lower limits differ by at most 2C/√(1+log L) for each L. This proves convergence, H/N→1 and the announced bound. Compactness does not determine the value of the limit. PROVED after independent mathematical audit.

## Error of a finite approximation to the continuous optimum

For fixed L, Γ_L can be enclosed on both sides by a finite matrix. Galerkin is known in P47 and 212-83; the estimate here uses the degenerate geometry of X, with a finer mesh near the origin. For M≥2, take nodes y_j=(j/M)², j=1,...,M−1, and the space V spanned by

    k_y(x)=−log(max(x,y)),    k_*(x)=1−x.

These functions belong to X: they are constant or bounded near zero and can be cut there by a linear transition in log x of growing length with cost I tending to zero; near 1 they have zero trace. Then smooth in the interior. In the energy product, k_y represents evaluation at y, by integration of −u' from y to 1. The function k_* represents ∫u by parts. The identities pass from the smooth kernel to X. Thus the orthogonal projection P onto V preserves the nodal values and the ordinary mean. It is contractive in I.

Let Γ_{L,M} be the supremum defining Γ_L restricted to V∩X₀. One has

    0 ≤ Γ_L−Γ_{L,M} ≤ 6 c_L/M,    c_L=10+2 Σ_{n≤L}Λ(n)/√n +4√L.

Indeed |h_L(t)|≤c_L√(1+t²) by 032 and P47 lem:mbounds (m increasing in |t|, m(0)>−6 and the upper bound of mbounds for |t|≥1). For e=u−Pu on each interval (a,b) of the mesh, e(b)=0 including b=1. By Cauchy–Schwarz, ∫_a^b |e|²≤I_interval(e)∫_a^b log(b/x)dx. The first cell has integral 1/M²; on the others log(b/x)≤(b−x)/a gives integral ≤(b−a)²/(2a)≤9/(2M²). Hence ||e||₂≤3√I(e)/(√2 M). By parts in the smooth kernel and by continuity, ||(Uu)'||²=∫x²|u'|²dx−||u||²/4. Thus ||Uu||_{H¹}≤√(7/4)√I(u). In the difference of forms, apply the multiplier h_L to Uu and to U(Pu) in the two crossings against Ue. Plancherel, the two contractions and 3√(7/2)<6 give the bound over the whole unit ball. The order of the suprema gives the lower side.

To assemble the matrix, with s=1/2+it and the Fourier convention of P47, the transforms of Uk_y and Uk_* are (1−y^s)/s² and 1/[s(s+1)], by direct integration. The energy Gram has entries k_y(z), 1−y and 1/2 for nodes, crossings with k_* and diagonal of k_*, respectively. The moment is imposed by orthogonality to k_* and the value zero is included when maximizing. The entries of B_L are the real or Hermitian integrals of the products of those transforms against h_L dt/(2π). With 032 an additional bound C/√(1+log L) is obtained for removing the cut. Γ has not been evaluated numerically nor has a numerical constant been fixed for that second error. PROVED after independent mathematical audit.

## Exact removal of the cut in each matrix of 033

Let L≥M² and u∈V∩X₀. On [0,1/M²] one has u(x)=A+Dx. Writing m₁(u)=∫₀¹ y u(y)dy, one obtains

    B∞(u)−B_L(u)=−2 Re(D conj(m₁(u))) [−ζ′(2)/ζ(2)−Σ_{n≤L}Λ(n)/n²−1/L].

Here B∞ denotes the limit of the hybrids. To prove the identity it suffices to subtract the symbols of two finite cuts K>L. The physical contact for t∈(L,K] equals ∫conj(u(y))u(y/t)dy=D conj(m₁(u))/t because ∫u=0. Thus the difference of the sum of Λ(n)/n² and the integral of dt/t² over (L,K] remains. Both converge absolutely when K is removed. The matrix correction has rank at most two by polarization.

There is moreover a dense choice of vectors for which the correction disappears. For M=2^j use only the k_y of the nodes, with zero mean. Each combination is constant near zero, hence D=0. The union of the spaces before imposing the mean is dense in X because an orthogonal vector vanishes at all the nodes, dense in (0,1), and is locally continuous. To obtain density in X₀ correct the mean with k_{1/4}, of integral 3/4 and present in all meshes. The limit form is continuous on X₀ by the cut-difference bound of 032, transferred first to smooth primitive profiles by the sampling of 031 and then by density. Consequently semidefiniteness of these matrices with L=M² for all j suffices. The previous bound 6c_L/M corresponds to the space that includes k_*.

Compact support of tests in logarithmic coordinate already removes contacts in P47. Here the support may reach x=0 and the vanishing comes from the constant value and the zero mean. This identity allows evaluating exactly the contribution of the tail in each compression. The simultaneous inequality in j remains open. PROVED after independent audit.

## Does the vanishing tail allow applying the primitive windows directly?

The Hardy transformation v(x)=u(x)−x⁻¹∫₀ˣu turns each nodal profile constant on (0,a) and of zero mean into a profile supported on [a,1]. With U(s)=∫₀¹u(x)x^(s−1)dx and V the same transform of v, Fubini in 0<Re s<1 gives V=sU/(s−1). The multiplier has modulus one on the middle line, so it preserves the whole logarithmic autocorrelation.

However, there is an obstruction already anticipated by P47, eq:Kprim and rem:Kprim. Take a=1/16, b=1/4, u=(1−b)k_a−(1−a)k_b, of zero mean. Its initial value is A=(9/8)log 2. Using the previous nodal transform, U′(1)=−(9/32)log 2. Hence V(0)=−A, V(1)=U′(1), and the product is 81(log 2)²/256. If a compact primitive profile with transform W had the same autocorrelation, the entire products V(s)conj(V(1−conj(s))) and W(s)conj(W(1−conj(s))) would coincide on the middle line and by identity at s=0. There the second vanishes by the primitive moments. This prevents the exact transport for that vector, even when widening the interval. The product may vanish for other vectors.

Cross-check: the unimodular factor already appears in G2_B10_R5 and phase 104; the moment argument is in P47. The explicit test is recorded to avoid reopening that route as a sign mechanism. PROVED after independent audit.

### Distance to sums of primitive windows of bounded width

Let K be the logarithmic autocorrelation of the previous example and S any real linear combination of real parts of compact primitive autocorrelations, with support of each autocorrelation in [−D,D], D≥log 16. Its L² closure for fixed D is also admitted. P47 eq:Kprim gives for S the zero moments against g₀(r)=cosh(r/2) and g₁(r)=r sinh(r/2). It is linear and both functionals are continuous on this interval. For K, let p=81(log 2)²/256 and q=∫g₁K. They are independent of D: K is supported on [−log 16,log 16]. The first value is the product of moments already computed, by the bilateral transform of the autocorrelation.

Projecting K−S onto the two weights one obtains

    ||K−S||₂² ≥ p²/G₀₀ + (q−pG₀₁/G₀₀)²/(G₁₁−G₀₁²/G₀₀).

By direct integration G₀₀=D+sinh D, G₀₁=D cosh D−sinh D and G₁₁=(D²+2)sinh D−2D cosh D−D³/3. They are the entries of the Gram of g₀,g₁. Its determinant is positive by independence. As D grows, G₀₁/G₀₀=D−1+o(1) and G₁₁−G₀₁²/G₀₀ is asymptotic to exp(D)/2. The square root of the right-hand side is therefore asymptotic to √2 p D exp(−D/2).

This rules out approximating K in L² by mixtures of primitive windows of bounded width, even if signed coefficients are allowed. For growing windows it only gives a necessary cost. The distance is between autocorrelations and does not bound the sign nor the error of a single energy. It is a quantitative consequence of the moments already recorded in P47. PROVED after independent audit.

### Identification of the matrix with the full form on its window

Let u be a combination of the k_y without k_* and of zero mean. Denote by v its previous Hardy transform, by a=M⁻² the first node and by F(r)=exp(r/2)v(exp r) the logarithmic profile. The following identity identifies the whole matrix problem, including its polar terms:

    B∞(u)=W(F),    supp F ⊂ [log a,0].

On each cell u=α log x+β, so v=α−C/x with a constant C specific to the cell. It is continuous and vanishes at both ends of the interval [a,1]. The map is injective by conservation of the Mellin modulus. The nodal space of zero mean has dimension M−2, equal to the number of interior nodes of [a,1]. Hence v runs over *the whole* continuous space piecewise affine in 1/x with those nodes and zero endpoint values.

To verify the energy, write c for the common logarithmic autocorrelation. The prime contacts coincide by the equality of c. The difference between the multipliers m♯ and m in 032 contributes 2∫₀^∞exp(−r/2) Re c(r)dr, since the inverse transform of 1/(1/4+t²) is exp(−|r|/2). The continuous density integrated up to the last contact contributes 2∫₀^∞exp(r/2) Re c(r)dr by the change x=exp r and the support of c. The sum is 4∫₀^∞cosh(r/2) Re c(r)dr=2 Re(A(F)conj(B(F))), exactly the polar term of P47. The window can be centred by translation, with half-width T=log M.

This identification allows importing a bound for W on the corresponding window. A bound given only on the primitive sector requires an additional hypothesis on the profile. The identity also explains the difficulty as M grows: W is being discretized directly on growing windows. It does not provide a new uniform inequality. PROVED after independent audit.

Exact antecedent of the energy equality for compact profiles: P47, rem:polarelim-full. The specific identification of 033 consists in determining the full space of finite elements produced by the Hardy map. 018 recovered W with two correctors on enlarged windows and 212-75 already provided another dense carrier.
