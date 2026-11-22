# R162_001 — Continuity of the primitive bottom λ_A(T)

Status: PROVED; check R162_190: CORRECT WITH FIXES (fixes applied below).

Notation of Paper 46: a_T is the truncated Weil form (eq:form), D_T its form domain, P_T the primitive
subspace (A(F)=B(F)=0), λ_A(T)=inf{a_T(F): F∈P_T∩D_T, ‖F‖=1}. Paper 46 proves monotonicity
(lem:monoT) and continuity of the complete bottom λ_W (lem:contT), and explicitly does not claim
continuity of λ_A because the dilation U_r does not preserve P_T. This note supplies it.

## Theorem

T ↦ λ_A(T) is continuous on (0,∞).

## Proof

Fix T>0 and work with windows T'∈[T/2,2T] and dilation factors r with rT'∈[T/2,2T], r∈[1/2,2].
All constants below depend only on T.

**Step 1 (dilation of the form).** U_rF(t)=r^{-1/2}F(t/r) is unitary L²(I_{T'})→L²(I_{rT'}) and maps
D_{T'} onto D_{rT'}. Steps (i) archimedean and (ii) comb of the proof of lem:contT do not involve the
polar term and give, with the same η(r)→0 (r→1), uniformly in T'∈[T/2,2T],

  |a_{rT'}(U_rF) − a_{T'}(F)| ≤ η(r) ( a_{T'}(F) + C‖F‖² ),     F∈D_{T'},

(take δ=8T|1/r−1| and the comb summed over n<e^{8T}, which covers every window in [T/2,2T]
and handles contacts entering or leaving, since c_F vanishes on |u|≥2T'), using ‖F‖_Q² ≤ a_{T'}(F)+C‖F‖² (Lemma mbounds(ii),(iii)), C = C_1 + A_{2T}.

**Step 2 (the Tate defect of U_rF is small).** For F∈P_{T'},
A(U_rF)=r^{1/2}∫F(s)e^{rs/2}ds = r^{1/2}∫F(s)(e^{rs/2}−e^{s/2})ds, since A(F)=0; hence
|A(U_rF)| ≤ ε(r)‖F‖ with ε(r)=r^{1/2}‖e^{rs/2}−e^{s/2}‖_{L²(I_{2T})} → 0, and likewise for B.

**Step 3 (a fixed correction space).** Choose real φ_1,φ_2 ∈ C_c^∞(I_{T/4}) with invertible matrix
M=[[A(φ_1),A(φ_2)],[B(φ_1),B(φ_2)]] (possible: e^{±t/2} are linearly independent on I_{T/4}).
I_{T/4}⊂I_{rT'} for all admissible r,T'. By zero-extension invariance (proof of lem:monoT) the values
a_{S}(φ_i,φ_j) do not depend on the window S≥T/4. For u∈D_{rT'} put G(u)=c_1φ_1+c_2φ_2 with
Mc=(A(u),B(u)). Then u−G(u)∈P_{rT'}, and for u=U_rF, ‖F‖=1:
‖G‖ ≤ C_2 ε(r),   a_{rT'}(G) ≤ C_3 ε(r)².

**Step 4 (cross term).** With M_S := A_{S}−C_0 ≤ A_{2T}−C_0 =: M_0, the form a_S + M_0‖·‖² is
nonnegative (Lemma mbounds(i),(iii)), so by Cauchy–Schwarz for it,
|b(u,G)| ≤ b(u)^{1/2} b(G)^{1/2}, b:=a_{rT'}+M_0‖·‖², hence
|a_{rT'}(u,G)| ≤ (a_{rT'}(u)+M_0)^{1/2} (a_{rT'}(G)+M_0‖G‖²)^{1/2} + M_0‖G‖ (the term M_0⟨u,G⟩).

**Step 5 (upper semicontinuity-type bound).** Let F∈P_{T'}∩D_{T'}, ‖F‖=1, with a_{T'}(F) ≤ V
(V a fixed bound). With u=U_rF and v=u−G(u)∈P_{rT'}: by Steps 1–4,
a_{rT'}(v) ≤ a_{T'}(F) + η(r)(V+C) + 2(V+η(V+C)+M_0)^{1/2}(C_3ε²+M_0C_2²ε²)^{1/2} + C_3ε²
 + 2M_0C_2ε = a_{T'}(F) + ω(r),   ω(r)→0,
and |‖v‖²−1| ≤ 2C_2ε+C_2²ε². Also a_{rT'}(v) ≥ −M_0‖v‖² and ‖v‖ ≥ 1−C_2ε > 0 for r near 1, so |a_{rT'}(v)| is bounded and v≠0; the Rayleigh quotient satisfies
λ_A(rT') ≤ a_{rT'}(v)/‖v‖² ≤ a_{T'}(F) + ω'(r), ω'(r)→0, uniformly in F with a_{T'}(F)≤V.

**Step 6 (both directions).** λ_A is bounded on [T/2,2T]: below by C_0−A_{2T}, above by
λ_A(T/2) (monotonicity). Take V = λ_A(T/2)+1.
(a) Near-minimizers at T (T'=T): λ_A(rT) ≤ λ_A(T)+δ+ω'(r) for every δ∈(0,1); so
limsup_{r→1} λ_A(rT) ≤ λ_A(T).
(b) Near-minimizers at T'=rT with factor 1/r: λ_A(T) ≤ λ_A(rT)+δ+ω'(1/r); so
liminf_{r→1} λ_A(rT) ≥ λ_A(T).
Hence λ_A(rT)→λ_A(T) as r→1. ∎

## Consequence (first-contact lemma without hypothesis)

If RH fails, then by Paper 45 Thm 11.3 there is T_0 with λ_A(T_0)<0; λ_A≥0 on (0,log 2] (Paper 42).
T_* := sup{T: λ_A(T)≥0} ∈ [log 2, T_0) satisfies λ_A(T_*)=0 by continuity and monotonicity, the
bottom is attained (compact resolvent, proof of thm:O), and the kernel of H_{T_*} is nonzero,
finite-dimensional and J-invariant, so it contains a parity vector. Thus the continuity hypothesis
of Paper 46 lem:firstcontact can be removed.

(Minimality: for T<T_*, λ_A(T)≥0; by strict monotonicity arguments not needed here. Note λ_A(T)>0 for
T<T_* is NOT claimed; λ_A might vanish on an interval ending at T_*. The first-contact window used
downstream is T_* itself.)
