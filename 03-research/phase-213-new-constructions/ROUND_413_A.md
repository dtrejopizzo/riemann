# D(R) already tends to zero without RH and the strong limit has a rectangular formula

**Status: PROVED, with independent review of the uniform density and of the branches and signs of Littlewood.**

Let M(T)=Σ_{0<γ≤T}δ² with multiplicity, δ=Reρ−1/2. For N(σ,T) counting zeros strictly to the right of σ, the symmetry of the completed function and the integration of indicators give exactly

    M(T)=4∫₀^(1/2) v N(1/2+v,T)dv.

Selberg's uniform density estimate N(1/2+v,T)≪T log T exp(−v log T/4) implies M(T)≪T/log T. It suffices to integrate v exp(−v log T/4) up to infinity. [Simonič, density estimate near the line](https://arxiv.org/abs/1910.08274).

By 412, the block γ≤R in D(R) costs O(M(R)/R)=O(1/log R). The block 2^j R<γ≤2^(j+1)R costs O(2^(−j)/log(2R)), summable. Hence unconditionally

    0≤D(R)≪1/log R.

Even if there were a single exterior quartet, one would have D(R)→0; that quartet contributes of order 1/R and is not ruled out by this ceiling. Making D tend to zero is not the missing step: R D(R)→0 along a subsequence is required. As a corollary, if all zeros up to H are on the line, the projected deficit of 410 is O(1/(H³ log H)), by the same block decomposition applied to δ²/γ⁴.

**Representation without a list of zeros as input data.** Fix t₀=1 and T>t₀ without zeros at that ordinate. For a∈[1/2,2], apply Littlewood's rectangle lemma to ζ on [a,2]×[1,T]. There is no pole in that rectangle. Take the branch of the argument on each horizontal by continuation from the Euler branch at 2, without reducing it afterwards to the principal argument. Then integrate in a and permute integrals. The result is

    π M(T)/2 =
      ∫₁ᵀ ∫_(1/2)^2 log|ζ(σ+it)| dσ dt
      − (3/2) ∫₁ᵀ log|ζ(2+it)| dt
      + ∫_(1/2)^2 (σ−1/2)[arg ζ(σ+iT)−arg ζ(σ+i)]dσ.

Indeed, the zero side before integrating is 2π Σ_{β>a}(β−a), whose integral equals πΣ_{β>1/2}δ²=πM(T)/2. The singular abscissae are handled by a limit; the local logarithms are integrable. Thus the limit of 412 is four over π times the limit of the rectangular expression. The antecedent in the corpus is the Green–Littlewood method recorded in 173.C; this derivation specifies the weights and caps for the moment of 412. No new arithmetic mechanism is obtained by replacing the sum by this integral. In particular, omitting the argument term of the upper cap has no justification here.

**Review record.** The Simonič reference contains Selberg's bound in(3) and an explicit version uniform inσ∈[1/2,0.831] in theorem1 and its corollary. For the deductionM≪T/logT that range suffices: integrate0≤v≤1/4 with the uniform constant, and for v≥1/4 use N(1/2+v,T)≤N(3/4,T)≪T^(15/16)logT, which is o(T/logT). No constants depending on a v that afterwards tends to0 are used. The indicator identity carries factor4 because each right zero of displacementδ has a reflected left one with the sameδ². The dyadic blocks and the projected remainder keep their bounds with this improvement ofM.

In Littlewood the orientation is left vertical minus right vertical, plus upper cap minus lower cap. The horizontal branches are fixed from the same Euler branch at2, independently ofa; hence when integrating the weight of each cap isσ−1/2. The real pole at1 lies below the base t=1. Integrating2π(β−a) in a contributesπδ² per right zero; symmetry converts the right sum into M(T)/2 and fixesπM(T)/2. The limits at abscissae with zeros use the local integrability of log|s−ρ|, with multiplicities. The factor4/π relative to the limit of412 then follows without an omitted cap term.
