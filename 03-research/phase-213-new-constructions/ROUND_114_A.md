# Absolutely controlled tail from the height of the fourth root

For the weight w of 109 and fixed A,K≥0, set H(x)=x^(1/4)/(log x)^A. Unconditionally, as x grows,

    Σ_{|Im ρ|≥H(x)} |x^ρ V(ρ)| = o(√x/(log x)^K).

Here moduli are summed, even for zeros off the line and with multiplicity. In 112 one paid O(x log H/H), sufficient in a finite window. The new estimate is asymptotic, without a certified numerical threshold.

**Classical inputs.** The version with logarithmic loss of Ingham's density is N(σ,2T)≪T^[3(1−σ)/(2−σ)]log⁵T uniformly for 1/2≤σ≤1 (recorded in phase 37, document 111 §references, and phase 54 document 170). We only use the larger exponent 3(1−σ). The weaker form with fixed +ε in the exponent does not suffice for this proof at the boundary. By Korobov–Vinogradov (paper 01 §free regions), in T≤|γ|≤2T one has (1−β)log T≥c(log T/log log T)^(1/3) for some c>0 and all large T.

**Summable majorant.** For any fixed B, over β≥1/2 one has Σ (log |γ|)^B |γ|^[−4(1−β)]<∞. In a dyadic block group by j=floor((1−β)log T). The cardinality of each group is ≪exp(3(j+1))log⁵T by density (if the counting threshold falls below 1/2 use the total count O(T log T)). The weight without logarithm is ≤exp(−4j). Sum j from c(log T/log log T)^(1/3)−1 and then T=2^k: the remaining exponential beats any power of k. Symmetry covers negative ordinates.

**Application.** In the tail of the claim log x≪log |γ| and x≤|γ|⁴(log x)^(4A). For β≥1/2, |V(ρ)|≤2C/γ² by 112; thus the term normalized by √x and multiplied by (log x)^K is dominated by a constant times (log |γ|)^(K+2A)|γ|^[−4(1−β)]. The tail of the majorant tends to zero. For β<1/2 use x^(β−1/2)≤1 and Σ(log |γ|)^K/γ²<∞. This proves the bound.

**What can produce an excess.** At all large scales the absolute contribution of the zeros on the line, divided by √x V(1/2), is <0.487 even without global RH (argument of 112 applied to the whole critical subset). The squares contribute (1/2+o(1)) in that normalization by PNT. Therefore if E(x)≥0 at arbitrarily large scales, the signed sum −Σ x^ρ V(ρ) of the zeros off the line below H(x) must contribute at least (0.013−o(1))√x V(1/2) there. One can require 1/2<β: the total with β<1/2 is o(√x) by dominated convergence. The low part off the line still has no useful bound. It is not claimed that the mere presence of a zero causes an excess at that scale, nor is it presupposed that the supremum of real parts is attained.
