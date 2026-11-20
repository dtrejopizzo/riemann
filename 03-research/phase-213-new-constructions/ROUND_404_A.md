# One part of the sum of residues already satisfies an exponential saving

**Status: PROVED, with independent review of the contour comparison and the parabolic orientation.**

Let α,K,T₀ be from 403, b=log z, z=L². There exist absolute η,c₁>0 and safe edges σ₀=α+δ (0≤δ≤1/L), H∈[2√L,2√L+1], such that in the rectangular sum R of 403 it suffices to retain the zeros ρ=β+iγ with

    β−γ²/(2L)>σ₀+η/b.

If R_par is the retained sum with complete residues, one has |R−R_par|≪T₀ exp(−c₁ L/b). This estimates the aggregate balance of the removed residues, without estimating each multiplicity separately. In particular S=R_par−(1+o(1))T₀. The parabolic exclusions of 364–366 had a fixed diffusion parameter; here the pulse has variance one and the parabola depends on L.

**Uniform saving of the product on the wings.** For 1≤|t|≤H and α≤σ≤1+1/L there is c₂>0 with

    log|E_z(σ+it)| ≤ log E_z(α)−c₂ L/b.

If σ≤α+1/b, the primes of [z/2,z] have p^(−σ)≍p^(−α); on a fixed proportion of the band the phase is separated from 2πℤ by 367, using short intervals up to height H. This gives loss ≫L/b relative to the real product E_z(σ)≤E_z(α); the higher-power terms add non-negative losses. If σ≥α+1/b, the decay of the real product already costs ≫L/b by the same primes, since 1−p^(−1/b) is separated from zero. Choose 0<η<c₂/4.

**Contour comparison.** Keep the segment σ₀+it for |t|≤1 unchanged. At each end connect horizontally with the new curve of abscissa

    s_R(t)=min(1+1/L, σ₀+η/b+t²/(2L)),    1≤|t|≤H.

There are no non-trivial zeros at heights |γ|≤2 (the finite verification used in 367 also suffices). To choose δ, exclude bands of radius 4L^(−2) both around β−α and around β−α−η/b−γ²/(2L) for all zeros up to H+2 (use 2√L+4 in advance). The lost length is o(1/L) by the count of 403. On the non-saturated curved part the slope is O(L^(−1/2)); that exclusion gives Euclidean distance ≫L^(−2) to the zeros, even looking at neighboring heights. On the saturated part the horizontal separation is already ≥1/L. Choose a safe H as in 403. Hence 1/ζ costs at most exp(O(log² L)) on both paths.

On the wings of the new curve the cost (s_R(t)−α)L−t²/2 is ≤δL+ηL/b, also when saturated. On the horizontal connector at |t|=1 the same bound holds. The saving of the product dominates that cost, the length O(√L), the real Gaussian prefactor and the bound for 1/ζ. The whole integral on these pieces costs ≪T₀ exp(−c₁L/b), reducing c₁ to absorb the prefactor √K''. The same holds on the original straight wings and on the cap at H by the argument of 403. Subtracting the two paths cancels exactly the common central segment. The residue theorem gives the announced bound for their difference, and the saturation to the right of one does not eliminate any pole satisfying the stated inequality.

**Review record.** The two families of exclusions forδ consume O(sqrt L log L·L^(−2))=o(1/L) even counting multiplicities. At a point of the non-saturated curve with |t−γ|<L^(−2), its slope O(L^(−1/2)) changes the abscissa by o(L^(−2)); the margin4L^(−2) at heightγ therefore leaves Euclidean distance≫L^(−2). If |t−γ|≥L^(−2) the distance is already sufficient, and when saturating at1+1/L the horizontal separation is≥1/L. This justifies the ceiling ofF only on the path, not in the interior with poles.

The new curve lies to the right of the old vertical. The residues remaining to its right satisfy β>σ₀+η/b+γ²/(2L), exactly the retained inequality; when the curve saturates, both criteria exclude all poles because β<1. When subtracting paths, the segment |t|≤1 cancels identically, without approximating two terms of sizeT₀. Only wings, connectors and caps remain, all with saving exp(−cL/b). Hence the aggregate ceiling forR−R_par, valid for complete residues without estimating each one. The orientations of the residue theorem give R−R_par as a difference of those integrals, whose absolute value is bounded independently of the sign.

**Scope.** Every fixed zero with β>1/2 would eventually enter the retained region as L grows, since α→1/2 and γ²/L→0. Thus the saving does not exclude an exterior zero; it identifies which aggregate is already negligible relative to the negative background at each scale.
