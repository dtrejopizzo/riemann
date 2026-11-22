# A single POWER diagonal with variable rate: exact detection interval

Use only F(s)=s^N/(s+u)^(2N), N≥1. For u>1/2 put b_N(u)=(4u²)^N W(f). The global sign of paper 46 is equivalent to either of these obligations: for each rational rate u>1/2, (i) limsup_N |b_N(u)|^(1/N)≤1, or (ii) W(f)≥0 for all N large enough (threshold depending on u). The first condition admits subexponential bounds, even without determining the sign of each moment. The rate must vary: sufficiency of the diagonal at fixed rate is not claimed.

**Exact geometry.** For z=ρ−1/2=δ+iγ define h_u(z)=−4u²z²/(u²−z²)². The identity 201 gives b_N=Σ_ρ h_u(z)^N, and

    limsup_N |b_N(u)|^(1/N) = max_ρ |h_u(z)|.

Indeed Σ|h_u|<∞ by Z3. The nonzero h tend to zero in height; the generating function Σ_{N≥1} b_N t^(N−1)=Σ h_u/(1−th_u) is meromorphic, by local convergence away from the poles. At each coincident pole the residues equal −1 per copy and add up. Cauchy–Hadamard gives the indicated maximum.

The identity |u²−z²|²−4u²|z|²=(u²−|z|²)²−4u²δ² implies that |h_u(z)|>1 exactly for

    sqrt(γ²+2δ²)−|δ| < u < sqrt(γ²+2δ²)+|δ|.

For δ=0 the interval is empty. Therefore the open set of rates of superunitary growth is exactly the union of those intervals. Each zero off the line produces one of length 2|δ|, at heights greater than 14 by Z1. It contains rationals. Under RH all h lie in (0,1], the moments are positive and bounded for each fixed u. This proves equivalence (i). As a local corollary, if (i) is proved at each node of a mesh of step d, every detection interval entirely contained in the covered zone has |δ|≤d/2.

**Equivalence using only eventual sign.** Choose a compact set of positive length in the interior of any detection interval. The maximum is >1 with uniform slack and only finitely many zeros compete there. Put x=−z² and a=u². The magnitudes 4a|x|/|a+x|² are real rational functions of a. If two coincide identically, comparing the coefficients of a² and a after clearing denominators gives |x|=|y| and Re x=Re y, so they differ only by conjugation. Outside finitely many ties there is a unique dominant pair up to multiplicities. It does not come from the critical line. The value 4ax/(a+x)² of that pair is non-real except at a=|x|: its imaginary part has the sign of Im(x)(a²−|x|²). Choose an interior rational rate avoiding those exceptions. The dominant term is 2m |h|^N cos(N arg h); the remainder is exponentially smaller by the separation and Σ|h|<∞. The cosine is ≤−1/2 infinitely often, by periodicity or density. The sequence has infinitely many negative signs at that fixed rate. This proves (ii).

**Part already covered without new hypotheses.** By Z2, for 1/2<u≤G−1, G=3·10¹², no detection band contains u (its lower endpoint is ≥|γ|−1/2). Thus the b_N are bounded in N at each of those rates. Moreover there is eventual sign for 1/2<u≤G−1000. Z3 ensures a critical zero t₀ between G−500 and G−200 by subtraction of counts, whose main term grows more than the two errors. For q=|z|²≥G², q₀=t₀² and u≤t₀,

    1/|h_u(z)|−1/h_u(it₀)
    =(q−q₀)(1−u⁴/(q q₀))/(4u²)−δ²/q
    ≥ [(q−q₀)²/(4u²)−δ²]/q >0.

The final inequality uses q−q₀>u and |δ|≤1/2. By decay in height there is a strict gap for each fixed rate between the unverified maximum and the contribution of t₀. The critical square ends up dominating the whole tail; the threshold in N may depend on u. Negativity is not inferred at any point for the true data.

**Antecedents and open goal.** POWER_REFLECTION_TEST_044 rules out eliminating the antisymmetric sector at fixed rate via reflection of densities. Here u is varied and the complete spectrum is used directly; that reflection is not applied. 206 exposed a dominant pair by varying the slope. The new diagonal has a single index and the detection interval is computed exactly. Proving subexponential growth of b_N(u) for all arbitrarily high rational rates remains an obligation equivalent to the global sign.
