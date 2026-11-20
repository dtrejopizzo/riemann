# Control of the arithmetic crossing linked by the translation modulus

Antecedents 213-10-A and 213-11-A, BUILD084(1), 106_109 §§1,3 and 106_118 §§1–3. The specific difference consists in keeping the same function at both ends of the far cell when estimating the crossing. The cross-check enabled an auxiliary lemma for the indicated regularity.

Fix 0<δ≤1. Write the physical profile f_k of BUILD084 through its jumps β_j, with f_k(x)=Σ_j β_j 1_{x≥j}. For k≥4 the head jumps are at 1,2,3 and are uniformly bounded. The tail ones are d and −d at k,k+1, with d=log(4/3). For a combination of translations V_sF_k with coefficients z_s, 0≤s≤δ, subtract cF_k with c=Σ_s z_s exp(−s/2). The remainder is exactly

    exp(t/2) Σ_j β_j H(t−log j),
    H(u)=Σ_s z_s exp(−s/2)(1_{u≥s}−1_{u≥0}).

This H is supported on [0,δ]. Split the remainder into head A and tail D by the jump indices. The same pair of formulas defines A and D for every H in L² supported on [0,δ]. Write w=log(1+1/k) and ω=||H−V_w H||₂. In the tail exactly exp(t/2)d (H−V_wH)(t−log k) appears. By the supports,

    ||A||₂ ≤ Cδ ||H||₂,       ||D||₂ ≤ Cδ √k ω,

where Cδ denotes constants depending only on δ and on the fixed coefficients of BUILD084.

For k>3 exp(δ), the head precedes the tail. A comb crossing can only occur for k/(3 exp(δ))≤n≤(k+1)exp(δ), by intersection of supports. Each pairing between a translation of A and D has modulus at most ||A||₂ ||D||₂. In that band the elementary Chebyshev bound Σ_{n≤x}Λ(n)≤Cx gives Σ Λ(n)/√n≤Cδ√k. From the physical formula of the comb with weight 2Λ(n)/√n one deduces, for the full mixed contribution to the square,

    |head–tail arithmetic crossing| ≤ Cδ k ||H||₂ ||H−V_w H||₂.

In particular, for fixed H in H¹(ℝ) with that support, ω≤w||H′||₂ and kw≤1. The crossing stays bounded as k grows. The modulus bound also holds for the original step H. The derivative bound concerns regular H. A sign estimate for arbitrary combinations and for the remaining terms of the form is missing. PROVED in the indicated class after independent review.
