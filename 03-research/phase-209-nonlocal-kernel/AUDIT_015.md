# AUDIT_015 — Completed domain, non-closability and global cone

2026-10-19. Independent check. **PROVED; favourable final verdict.** Reviewed `CONSTRUCTOR_015_DOMAIN_AND_CONE.md`, with 005, 007, 008, 011 and 014. Consulted: the project rules, index, grid and crossword. No paper is modified.

## 1. Difference and construction of the sequence

The written difference with respect to 008 is real: the previous primorial had divergent Gaussian norm and did not prove non-closability. The new tilted products produce a pure arithmetic constant via strong convergence in both factors.

The finite blocks exist by divergence of Σp⁻¹ and s<1. To make the choice fully deterministic one can take E_j as the consecutive primes from the first one ≥j until H_j≥j³ is reached; no estimate of its last prime is needed. The freedom of choice in the text does not affect the proof either.

Independence of the X_p under P_s gives exactly the second-moment formula; `Var_s B_j≤exp(t_j²H_j)−1→0`. The logarithmic bound (3) has the correct sign: r>s, min E_j→∞ and t_jH_j=H_j^(1/3)→∞, while t_j→0. Thus Z_r/Z_s→0 and, because r<1, Z_1/Z_s≤Z_r/Z_s→0. It follows that A_j→1 in L²(P_s), although each A_j is Haar-centred.

The centred expansion of §4 is exact, including the vanishing d=1 term. The bound of 011 is a norm bound, `||Tf_d||≤C d⁻ʳ`; the triangle inequality on the finite expansion gives `||TA_j||≤C(Z_r−1)/Z_s→0`. There is no interchange of infinite products nor zeta law on the integers for s<1. This proves `(√κ1,0)∈H`.

## 2. Completion and operator

D_n is bounded in both factors and preserves H by 007. Applying it to the new limit yields `(√κX_n,0)`. The span of the X_n is dense in L² of the product law of valuations: finite differences of thresholds generate indicators of finite patterns, with truncation of the unbounded coordinates. Hence the whole pure arithmetic factor lies in H.

Subtracting that factor from each initial image delivers `(0,TA)`, and closing gives exactly `H=L²(P_s)⊕V`, V=closure(TA₀). The reverse inclusion uses the closed product; V is not assumed to be the whole Gaussian ambient space.

A₀ is now dense in L²(P_s). The explicit sequence `F_j=f₂−(D₂A_j−A_j/2)` satisfies F_j→0 arithmetically and TF_j→Tf₂≠0 in Gaussian norm. The step uses the bounded actions of 007, not pointwise evaluation of an L² limit. It is a complete proof of non-closability of the operator T of this domain. It is not extrapolated to operators associated with other carriers.

## 3. Projections and cone

With the normalisation of ι, e=(1,0) is a unit vector and the limit obtained earlier is √κe; there is no conflict of factors. The rank one is exactly `||Proj_eι(A)||²=κ|E_sA|²`. The other pieces are the energies of the mean-zero arithmetic part and of the factor V. This claim, previously unjustified in 007, is now proved by the new decomposition; it does not identify e with the pole of Q.

Each form is dominated by S, so any fixed real combination is continuous on H. PSD on the dense A₀ extends to H. The three pure vectors of §8 are nonzero and isolate the three coefficients, proving necessity of the nonnegative orthant; sufficiency was already 005. The divergent sequence 008 is not needed for the cone.

## 4. Final scope

The combination with 014 is correct: no fixed nonzero real combination of the three pieces that is PSD **on all of A₀**, applied with map011 intact, provides the declared uniform domination. Signed combinations positive only on the image of the pullback, other maps, other kernels, T-dependent coefficients or invariance of V under the ambient inversion are not classified. No new sign for D was obtained.

**Verdict:** the three theorems are PROVED within the written scope. The negative application to map011 keeps the CITED input of 014; the internal proofs of structure, non-closability and cone do not need that spectral input.
