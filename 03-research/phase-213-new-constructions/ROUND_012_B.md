# Energy limit for a fixed smooth mixture of translations of BUILD084

Cross-check: 106_47 §2, lemma 2, contains the moving prime quadrature. The application here treats the full energy of a linked mixture, including the comb and the archimedean symbol. Compared with the free remainders of 213-11, the tail has a limiting shape after rescaling, and the inverse moment of the limiting head pays the continuous term of the comb.

Fix a smooth complex density μ with compact support in [0,δ]. Let Y_k=∫ μ(s)V_s F_k ds. Write in the physical variable Y_k=U(A_k+D_k), where Uf(t)=exp(t/2)f(exp t). By the formula of BUILD084, A_k is the physical mixture of the head of f_k and converges, with all its derivatives on a common compact subset of (0,∞), to A, the same mixture of b1_[1,2)−a1_[2,3). This results from integrating μ(s)exp(−s/2) over intervals with logarithmic endpoints. In particular ∫A(x) dx/x=0, since b log 2−a log(3/2)=0 and the inverse moment is invariant under x↦exp(−s)x.

In the tail one has D_k(x)=k⁻¹ G_k(x/k), with

    G_k(y)=kd ∫_[log y−w, log y] μ(s)exp(−s/2)ds,     w=log(1+1/k).

Since kw→1, it converges with all derivatives to G(y)=d μ(log y)y^(−1/2) on a common compact subset of (0,∞), and is extended by zero outside it. Hence UD_k=k^(−1/2)V_(log k) UG_k. Its full self-energy is O(1/k), by covariance and boundedness of the form on these smooth profiles of fixed support. Its archimedean crossing with UA_k is O(k^(−1/2)) by Cauchy–Schwarz with the weight |m| and uniform boundedness of the weighted norms. The energy of UA_k converges to that of UA by the same regularity and fixed window.

For large k there is only one possible direction of contact between the two supports. The comb crossing being subtracted is

    2 Re k⁻¹ Σ_n Λ(n) Φ_k(n/k),    Φ_k(v)=∫ conjugate(A_k(x)) G_k(vx) dx.

Indeed the logarithmic correlation contributes √n, which cancels the denominator of the comb. The Φ_k converge uniformly to Φ(v)=∫ conjugate(A(x)) G(vx)dx and have common compact support in (0,∞). The Chebyshev bound allows replacing Φ_k by Φ with error o(1). By the prime number theorem in its quadrature form, k⁻¹ Σ_n Λ(n)Φ(n/k)→∫Φ(v)dv. By Fubini this limit is (∫conjugate(A(x))dx/x)(∫G(y)dy)=0. Consequently a(Y_k)→a(UA).

**Consequence for the sign.** The initial head has energy q(0)>0.15 by BUILD084. Choose δ₀>0 according to 213-10-A for that head. In the proof of that result, the smallest eigenvalue of the two-by-two matrix is strictly positive. Since ||cF+g||²≤2 max(1,||F||²)(|c|²+||g||²), the form dominates a positive constant times the squared norm on the whole span. The bound passes to the integral mixture UA by Riemann sums in the norm with weight 1+|m| (continuity of translation and support in a fixed window). For nonzero μ, UA does not vanish either: its transform is the product of the entire transforms of two nonzero compactly supported functions. Hence, for each nonzero smooth μ supported on [0,δ₀], the limit is strictly positive and there exists k₀(μ) such that a(Y_k)>0 for all k≥k₀(μ).

The proof uses PNT only for a fixed limiting test. Uniformity of the threshold in μ and the global sign remain open. PROVED, including the sign consequence, after independent mathematical review.
