# A single list of poles: two-sided comparison with the effective window

Let v=(v₁,…,v_n) be a finite list, repetitions allowed, S=Σ1/v_j in a compact set J⊂(0,∞), V=min v_j and ε=Σv_j^(−3). Let R(v,L) be the smallest quotient of the full form over the numerators of that list, cut to length L and normalized by the cut norm. Uniformly for V large, one has, for all 0<α<1 and 0<s<1/2,

    λ_W(S)−C_{J,α}(log V / V)^(2α/3)
       ≤ inf_{L>0} R(v,L) ≤ R(v,2S)
       ≤ λ_W(S)+C_{J,s} ε^(2s/3)(1+|log ε|).

At the cutoff 2S one also has R(v,2S)≥λ_W(S). Here ε≤S/V². Although 086 also optimized over the lists and recovered through repeated poles, each individual list under the above conditions approximates the same minimum at its own S. For example the error is O_{J,β}(V^(−β)) for any β<2/3, both at the cutoff 2S and for the infimum over the lengths. The constants have not been evaluated.

**Lower bound for any cutoff.** The reflection of 085 gives log ||exp(σt)f||≤Σ log((1+σ/v_j)/(1−σ/v_j)) for ||f||=1. If σ≤V/2, the artanh series bounds this expression by 2σS+Cσ³ S/V². Take σ=V^(2/3)(log V)^(1/3), H=2S+D(log V/V)^(2/3), with D>C sup J+3. The argument of 086 gives ||exp(t) f 1_{t>H}||≤exp(H−σ(H−2S)+Cσ³ S/V²)≤V^(−2) eventually. For L≤H the inclusion of windows gives R≥λ_W(H/2). For L>H, the Carleman archimedean crossing, the full comb and the polar moments are paid as in 086 at cost O_J(V^(−2)), also after normalizing. The power modulus of 077 on a compact set slightly larger than J gives the lower side.

**Upper bound for the prescribed list.** Take t as physical variable and B(z)=∏(1−z/v_j)/(1+z/v_j). Let E be the delay multiplier exp(−2Sz). On the imaginary axis, the phase of B is −2Σ arctan(ξ/v_j). From |u−arctan u|≤|u|³/3 and unit modulus one obtains exactly the majorant

    |B(iξ)−E(iξ)| ≤ min(2, (2/3) ε |ξ|³).

For 0≤q≤s/2 this gives ||(B*−E*)F||_{H^q} ≤ C_s ε^((s−q)/3)||F||_{H^s}, where the asterisks denote adjoint multipliers on the whole line. Choose a normalized minimizer of the window translated to [0,2S]; its extension by zero has H^s norm bounded uniformly in J by 077. By support, P_+E*F=0, with P_+ the restriction to positive times. As in 086, Q_B F=F−B P_+B*F belongs to the rational model of the list. Thus for g=1_[0,2S] Q_B F the error e=F−g satisfies the same bound in H^q, up to a uniform constant. One uses that restrictions to half-lines and intervals are uniformly bounded for q∈[0,s/2], by interpolation between L² and H^(s/2). In particular ||g||→1 uniformly.

On this fixed support, the bounded part of W has norm O_J(1); the archimedean logarithmic weight is dominated by C q^(−1)(1+ξ²)^q for small q>0. Choose q=1/|log ε| for ε small enough. The eigen-equation of F cancels the linear terms, so that
    
    W(g)/||g||²−λ_W(S)=[W(e)−λ_W(S)||e||²]/||g||²
                          ≪_{J,s} (1+|log ε|) ε^(2s/3).

The cubic phase step is used before the energy estimate; a merely qualitative density control does not give this finite comparison.

**Limit of the phase majorant.** For n equal poles v=n/S with S fixed, ε=S³/n². At ξ=ε^(−1/3) the phase difference tends to 2/3, since the next term in the expansion of arctan costs O(n^(−2/3)). By continuity in frequency this gives norm ≳ε^(s/3) for B−E from H^s to L². The computation shows the scale where the uniform approximation of the multiplier stops working; it does not prove optimality of the rate of the minima nor of the errors after projecting.

**Cross-check.** POWER_CONFLUENT_BRIDGE_014 §6 has exact distances for exponential tests in the repeated model; 086 identifies the variational limit; 077 supplies regularity and continuity in the window. The present contribution is the comparison with error for a prescribed list, including distinct or confluent poles and all arithmetic terms. It is not a bound uniform as S→∞ nor a proof of sign for the approximated window.
