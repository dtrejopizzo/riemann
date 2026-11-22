# Schur correction depending on the jumps of each vector

In 079 a single number was used for the crossing with the complement. Here the dependence on the vector is kept. Use coefficients u_j in the basis of normalized indicators of the window, extended by zero outside it, and Δu_j=u_j−u_{j−1} (including the two edges). Set S_T=Σv_n, d=m(π/h)−S_T−4sinh T and M the matrix of W in the basis. For a>0, λ<d, the matrix inequality
    
    M−λI ≥ [(1+a)L_h² Δ*Δ + (1+1/a)e_h² I]/(d−λ)

implies λ_W(T)≥λ. Here e_h=2h sinh(T)/π. One can choose L_h=O_T(1+log(1/h)) for h≤1, with the explicit formula below. A variant keeps the full variance of the symbol, including the phases of all prime translations. It is not required that the eigenvectors of M be eigenvectors of Δ*Δ.

**Multiplier and jumps.** On the line use the real symbol b(ξ)=m(ξ)−Σ v_n cos(ξ log n). For an input supported in the window and then projected back to it, it gives exactly the non-polar part. In the fiber of 079 let b_k=b((θ+2πk)/h) and w_k the squared sinc weights. The global contribution to the squared norm of the crossing is exactly
    
    ∫_{−π}^π |Σ_j u_j exp(−ijθ)|² [Σ w_k b_k²−(Σ w_k b_k)²] dθ/(2π).

Compressing the output to the interval only reduces its norm. It is important to form b_k before the variance in order to keep the mixed terms of the comb with the archimedean symbol. This positive integral defines a finite Toeplitz matrix G according to the length of u. G can be used instead of L_h² Δ*Δ in the previous test.

For a simpler bound set D₀=m(1)−m(0), M₁=10 as in 079. For k≠0 one has |θ+2πk|≥|θ|. Monotonicity of m and the estimate on its logarithmic derivative give
    
    |b_k−b_0| ≤ d_k := D₀+10 log(1+3π|k|/h)+2S_T,
    L_h² := Σ_{k≠0} d_k²/(π² k²).

For the first inequality, up to frequency 1 one pays D₀ and above 1 one integrates 10 dt/t. The series for L_h converges and for h≤1 is bounded with log(1/h)+log(1+3π|k|). Centering the variance at b_0 and using w_k≤4sin²(θ/2)/(πk)², discrete Plancherel gives the bound L_h²||Δu||². For the polar term the output inside the window is a combination of exp(±t/2), with norm of its derivative ≤2 sinh(T)||u|| by Cauchy–Schwarz in the two moments. The L² error of replacing it by its cell means is at most h/π times the norm of the derivative. Young's inequality separates the two crossing norms, and completing the square with floor d−λ gives the certificate.

**Sharpness of the jump cost.** On the mesh of the whole line, for the archimedean operator alone, if P_h is the projection by means and Q_h=1−P_h, then for f∈H¹(ℝ)
    
    lim_{h↓0} ||Q_h m(D)P_h f|| /[h log(1/h)] = ||f'||/√12.

For f of fixed Fourier band and h small enough, in each fiber only the entry k=0 of f can be nonzero. Its projection onto the line of means has mass |f̂(ξ)|² w_0(hξ) in the physical variable ξ. For θ=hξ fixed in this form, w_0→1 and for each k≠0, w_k/h²→ξ²/(4π²k²). Moreover (m((hξ+2πk)/h)−m(ξ))/log(1/h)→1 by the asymptotics of P46. The sum of the squares of these weighted differences, divided by h²log²(1/h), tends to ξ²/12 since Σ_{k≠0}1/(4π²k²)=1/12. The square of the displacement of the fiber mean relative to b_0 is negligible: by Cauchy–Schwarz it is ≤(1−w_0) times the quadratic sum just computed. The bound d_k provides summable domination in k, uniform in any fixed band. Finally ||Δ(P_h f)||≤||f(·−h)−f||≤h||f'||, since P_h commutes with integer translations of the mesh. The jump bound extends the limit by density to H¹. The identity holds on the whole line; for the window certificate only the corresponding upper bound is used.

**Scope.** The penalty of a vector coming from a fixed H¹ profile costs O_T(h² log²(1/h)) before dividing by d−λ, versus the constant penalty of 079. This does not assume that minimizers belong to H¹; 077 only gives H^s for s<1/2. The floor of 078, the fiber identity of 079 and the Schur method are direct antecedents. The new test keeps the individual cost and the limit shows that the logarithm is real for the indicator mesh. The matrix test has not yet been verified for arbitrarily large windows.
