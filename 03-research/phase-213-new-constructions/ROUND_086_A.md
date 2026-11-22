# The sum of reciprocals is exactly the half-length of the limit window

Fix S>0. Denote by b(V,S) the infimum of W(g)/||g||² over all lengths L>0 and all nonzero tests of 085 with v_j≥V and Σ 1/v_j≤S. Dimension, numerator and multiplicity are not restricted. Then, unconditionally,

    lim_{V→∞} b(V,S)=λ_W(S),

where the right-hand side is the minimum of the full form on the interval of length 2S. In particular, raising the rates while leaving the dimension free at fixed budget does not make the difficulty of that window disappear.

**Lower localization, even for arbitrarily far cutoffs.** Normalize ||f||=1. Given H>2S, choose η∈(0,1) with H>2S/(1−η²) and set σ=ηV>1. The estimate of 085 gives ||exp(σt)f||≤exp(2σ S/(1−η²)). Thus, for any L>H, k=f 1_(H,L] satisfies
     
    ||exp(t)k||≤δ=exp(H−σ[H−2S/(1−η²)]).

Also ||exp(t)f||≤exp(2S/(1−V^(−2))) for V>1. If L≤H monotonicity of the domain suffices. For L>H write g=h+k, with h=f 1_[0,H]. The norms of g and h tend uniformly to 1 since the same tail estimate holds with L infinite. The archimedean term of k is ≥m(0)||k||². The crossing of h and k costs ≤5||h||||k|| before the factor 2: the exterior kernel is −K(v+w)/2, with K(u)≤3/u by the formula of 077 (separate u≤1 and u≥1), and the norm of the Carleman operator is ≤π by its integral of dilations. This allows comparing the energies without requiring the derivative of the tail to be small.

For u≥0 the change in the autocorrelation when passing from h to g is the integral with the larger time in (H,L], bounded by exp(−u)||exp(t)k||·||g||. Paying the whole comb costs ≤2δΣ(log n)n^(−3/2)<12δ. Each polar moment of the tail costs ≤δ by Cauchy against exp(−t/2); the moments of h and g are ≤||exp(t)f|| for the same reason. The polar change costs ≤4δ||exp(t)f||. Hence W(g)≥λ_W(H/2)||h||²−O_S(δ+δ²). Take V→∞ and then H↓2S, using the continuity of P46. This proves the liminf also if λ_W(H/2) is negative.

**Recovery of the whole interval.** Use the pole v=n/S n times. The inner product B_n(s)=[(1−sS/n)/(1+sS/n)]^n converges pointwise on the imaginary axis to exp(−2Ss) and has modulus 1 there. In physical Fourier, its unitary multipliers and their adjoints converge strongly to the translation by 2S and its inverse, respectively, in each H^q(ℝ), by domination. Choose 0<q<1/2 and denote by P_+ the projection by support onto positive times, bounded on H^q by the Hardy inequality used in 077. On causal functions, the operator
    
    Q_n=I−B_n P_+ B_n^*

is the L² orthogonal projection onto the complement of B_n H² in the causal Hardy space. Its range is the space of numerators of degree <n over (s+n/S)^n: for example, the orthogonal decomposition of Blaschke products with n factors gives precisely the Malmquist basis of 084. Here B_n and its adjoint in the formula are multipliers on the full space before applying P_+. The strong limit in H^q, on causal inputs, is the restriction to [0,2S]. For any smooth compactly supported test inside that interval, Q_n f therefore converges to f in H^q. Cutting again to [0,2S] preserves convergence by the interval multiplier on H^q. The coefficients can be taken real for real inputs. On fixed support this convergence implies that of the form norm by log(2+|ξ|)≪_q(1+ξ²)^q and boundedness of comb and polar term. Smooth interior tests are a form core (P46, inward dilation and smoothing). Thus b(V,S)≤λ_W(S) for each V, taking n arbitrarily large with n/S≥V. The equality is closed. The approximation of a delay by rational factors and the Hardy projection are classical; what matters here is that the energy of the full form is recovered in a window of size EXACTLY 2S.

**An enlarged sector with constants.** If S≤3/4 and V≥10000, there holds in all lengths W(g)≥(10^(−18)/2)||g||². Take H=log 5, where P46, thm:log5W, gives λ_W(H/2)≥10^(−18). For L≤H it applies directly. In the other case choose η=1/8: H−(3/2)/(1−1/64)>0.08, σ≥1250 and δ≤5 exp(−100). Moreover ||exp(t)f||<5 and m(0)>−6. Thus the loss in W is ≤42δ+6δ² and ||h||²≥1−δ² (apply the control to the whole tail). These figures imply the stated margin since ||g||≤1. The comparison with 085 changes two parameters: the budget grows from 1/512 to 3/4 and a higher minimal rate is required; the proven margin is smaller.

**Cross-check and limit.** 002/014 use density of rational models for the global bridge; 085 controls the order through the reciprocal budget. Here the two directions identify the limiting variational value with fixed budget and poles escaping to infinity, even optimizing over L. The result transports margins of known windows and shows exactly which positivity would be needed to extend them to larger budgets. It does not prove that λ_W(S) is positive for all S.

Specific antecedent: POWER_CONFLUENT_BRIDGE_014 §6 already gives the distance of an exponential to the moving model and the criterion n/v→∞ for density on the whole half-line. At finite ratio S that distance already reflects the tail after 2S. The variational identification here includes the physical cutoff, all tests of the domain by density and, in the liminf, arbitrary configurations of poles and lengths.
