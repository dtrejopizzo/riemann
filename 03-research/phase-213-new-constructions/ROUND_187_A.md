# Sufficient negativity test at a single frequency in the critical band

Put X=exp(2T), S_X(Γ)=Σ_{n≤X}Λ(n)log(X/n)n^{iΓ}. For fixed κ>0, G=exp(κ exp T), Γ∈[2G,3G], take the profile exp(−(T−|t|)/2) on [−T,T], with phase 1 on the left half and exp(iθ) on the right. Divide by sqrt(B), B=2(1−exp(−T)), and modulate by exp(iΓt) to obtain f_θ of norm one. Uniformly in the band,

    min_θ W_T(f_θ)=log Γ−|S_X(Γ)|/sqrt(X)+O(T+1).

In particular a sequence with |S_X(Γ)|/X≥κ+δ, for fixed δ>0, would give negative values of the true form at large scale. For κ=1, exhausting the main margin on these profiles is equivalent to |S_X(Γ)|/X→1 (the total mass S_X(0)∼X by PNT). The asymptotic equality alone does not decide the residual sign.

**Exact overlap.** For l=log n∈[0,2T] the demodulated autocorrelation at positive shift consists of two parts. Between halves it has length b(l)=min(l,2T−l), constant product exp(−(2T−l)/2) and phase exp(iθ), up to the conjugation convention. Within the same half the summed overlap, for l≤T, is 2 exp(−l/2)(1−exp(−(T−l))); for l>T it is zero. Both terms carry the divisor B. Multiplying by 2Λ(n)/sqrt(n) and taking real parts, the cross part is (2/B)exp(−T) Re[exp(iθ)ΣΛ(n)b(l)n^{iΓ}] with the autocorrelation convention f(t+l)conj(f(t)). The internal part costs O(Σ_{n≤exp T}Λ(n)/n)=O(T+1).

Replacing b(l) by 2T−l in the cross sum costs O(1) in the form: exp(−T)Σ_{n≤exp T}Λ(n)(T−log n)=O(1) by integrating ψ(y)/y and using Chebyshev. Replacing 2/B by one also costs O(1), since Σ_{n≤X}Λ(n)log(X/n)≪X by the same computation. These errors are absolute even at exceptional frequencies.

**Full form.** The total variation of the demodulated profiles, their sup norm and their L¹ norm are O(1) uniformly in θ. The archimedean upper bound of 180 gives log Γ+O(1); for the lower bound, on |v|≤Γ/2 around Γ the symbol is ≥log Γ−O(1), and outside mass O(1/Γ) is lost with an absolute floor. The poles cost O(exp(T)/Γ²) by the two integrations by parts of 180. Optimizing the cross phase proves the formula.

**Antecedents and scope.** The weight log(X/n) is already in 212-57 C1 and SELECTION_092; the latter even gives a global criterion with primes alone without twist. 180 modulated an odd profile and averaged in Γ. Here the twist at the individual frequency is kept and the relative phase of the two ends is optimized, with absolute error O(T+1). Unlike the necessary condition of 184 on an interval, exceeding this threshold in the complete sum would be sufficient to obtain a real counterexample (by realification if needed). No such frequency has been found nor has the required ceiling been proved.

The independent audit confirms the formula at first order and the direction of the implication. P46 thm:band already uses two directions and prop:wit-Egamma already gives obligations for twisted sums. The finer absolute error written above comes from also including the exact overlap within each half.
