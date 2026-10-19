# INV_Q_001: the band-gap mixing inequality. The logarithm resums the mixing into a place-additive kernel (track Q)

Positivity is assumed true.
Notation: INV_L_001 (L1–L3), INV_P_001 (P1–P4). Ω={½<σ<2}, S_N={p<N}, N=e^{2T}, g_σ(t):=tF(t)e^{(σ−½)t}, so Φ_F′(σ+iτ)=ĝ_σ(τ)
(ĝ(τ)=∫g e^{iτt}dt). R_σ(u):=∫g_σ(t)g_σ(t+u)dt, which vanishes for |u|>2T. Area term 𝒜_S(F):=4∬_Ω d_S|Φ_F′|²dA.

## 0. Index check and new reasons
- MW-4, G3F Carleson, G8H strip-Hardy, P33-10 Jensen: already NO-GO for this object by P4. Not reattempted.
- Phase 152 FUP / band-limited / uncertainty (R152_001, G3H-152): those concern Gauss-map branch sums. G8H-R160_S1 (band-limited Hodge gap)
  concerns a Gram form. Nehari/Hankel (G3D-159 G1_B8) concerns the Suzuki kernel. Beurling–Malliavin (GAP-157.A) concerns p^{iτ} with LI input.
  **New reason:** none of these acts on the semilocal log-ratio d_S. The question asked here is how log|1+D_S·R| moves the edge band of D_S
  (P2) into the bulk of the window. It was left OPEN at the end of INV_P_001 §1. §1–§3 answer it exactly, so no estimate is needed.
- Semiring principle: §3 shows exactly where the (ℕ,+) structure is lost.

## 1. Precise statement of the target (Q0)
With R(s):=Π_{p∈S}(1−p^{s−1})/Γ_R(1−s)=1/ξ_S(1−s) and x_S:=D_S·R=ξ_S(s)/ξ_S(1−s)−1, d_S=log|1+x_S|. The **band-gap mixing inequality**
is any bound of the form
  (Q0)  |𝒜_S(F) − 𝒜_S^{lin}(F)| ≤ ε(T)·‖F‖²  on 𝒫_T,
where 𝒜^{lin} keeps the edge-band part of D_S (frequencies |u|∈[2T−½log2T,2T], P2) after the transport by R and the logarithm.
Combined with the L3 sources and B₂, (Q0) would give a sign statement whose ℤ-specific input is P2.

## 2. No linear regime (Theorem Q1, PROVED)
(a) For s∈Ω, |log(1+x_S)| ≤ 2(σ−½)·Σ_{p∈S}log p·p^{−½}(1−p^{−½})^{−1} + O_σ(σ−½), where the arch part is uniform on compact τ-sets.
For S_N the prime sum is ≍4e^{T}. So |x_S|≤½ is guaranteed only on the layer σ−½ ≲ e^{−T}.
(b) Conversely, on the real segment ½+δ≤σ≤1−δ, the formula of Q2 gives d_{S_N}(σ) ≤ −Σ_{p<N}(p^{σ−1}−p^{−σ}) + O_δ(1) → −∞. So x_S→−1
there: the ratio ξ_S(s)/ξ_S(1−s) is tiny and log(1+x) sits at its singularity, not near 0.
Proof: (a) is the mean value theorem on ℓ_S:=log ξ_S(s)−log ξ_S(1−s), with ℓ_S(½+iτ)∈iℝ and |ℓ_S′| ≤ |ξ_S′/ξ_S(s)|+|ξ_S′/ξ_S(1−s)|.
(b) follows from the sign of the coefficients in Q2. ∎
Consequence: the expansion log(1+x)=x−x²/2+… does not converge on the part of Ω that carries ΔG. ΔG grows like e^{2(σ−½)T}, so its mass lies
far from the layer. The breakdown is not confined to the sources s_{p,k}. Any (Q0) built termwise from that expansion fails.

## 3. Exact band formula: the mixing resums (Theorem Q2, PROVED; NUMÉRICO check of (Q2a) to 1e−15)
(Q2a) For every prime (or Beurling prime) p and every s=σ+iτ with σ≠1:
  d_p(s):=log|1−p^{s−1}|−log|1−p^{−s}| = (σ−1)_+·log p + Σ_{k≥1} (p^{−kσ} − p^{−k|σ−1|})/k · cos(kτ log p).
In Ω every coefficient is <0, because σ>|σ−1|. The constant term (σ−1)_+log p is the Jensen mean from INV_L (c).
(Q2b) d_S = d_∞ + Σ_{p∈S} d_p (additive over places). Hence, for F∈C_c^∞(I_T),
  𝒜_S(F) = 𝒜_∞(F) + 8π Σ_{p∈S} ∫_½^2 dσ [ (σ−1)_+ log p·R_σ(0) + Σ_{k: k log p ≤ 2T} (p^{−kσ}−p^{−k|σ−1|})/k · R_σ(k log p) ].
The sum is finite: only prime powers n=p^k≤N=e^{2T} enter, each with weight Λ(n)/log n. A prime p≥N contributes only the nonnegative
Jensen term (σ−1)_+log p·‖g_σ‖², which cancels in L3 against its own sources and boundary term.
Proof: (Q2a) for σ<1 expand both logarithms. For σ>1 write log|1−p^{s−1}|=(σ−1)log p+log|1−p^{1−s}|. Both series converge absolutely
for σ≠1, and the line σ=1 has measure zero, with log-integrable singularities at the sources. (Q2b) uses ∫|ĝ_σ|²cos(uτ)dτ=2πR_σ(u),
then Fubini. The cutoff k log p≤2T is exact because supp R_σ⊂[−2T,2T]. Check: the series (4000 terms) matches the closed form at
p∈{2,3,7} and s∈{0.7+1.3i, 1.4+0.2i, 0.55+5i, 1.9+2.2i}, agreement ≥14 digits (NUMÉRICO).

**What the "mixing" is.** Expanding log(1+x_S) to order j produces frequencies in j-fold sum sets, i.e. log of S-smooth numbers m. P2's
edge-band structure of D_S comes from cancellation over *all* S_N-smooth m, using [1,N)⊂⟨S_N⟩ (L2). Summing the series turns the
coefficient of log m into Λ(m)/log m. That coefficient is the Dirichlet logarithm, which vanishes off prime powers. So the area term sees
**no edge band and no smooth-number set**. It sees Λ on n≤N in the bulk band, with explicit σ-weights. Bernstein, Paley–Wiener and
Hankel/Nehari bounds add nothing, because the band truncation in Q2 is already exact (Toeplitz kernel R_σ(u), finite rank in u).
Beurling–Malliavin does not apply: the frequency set is finite.

## 4. Verdict (Theorem Q3, PROVED as structure)
Q2 holds verbatim for any Beurling system {q} (replace log p by log q) and for a_P (drop p<P). By L1 it is a sum of place-by-place
functionals. So every inequality derived from d_S, at any order of the log expansion and with any band, PW, Bernstein, Nehari or BM
estimate applied to the pieces, is comb-generic and fails clause (1). The only ℤ-specific input available, P2, is annihilated by the log:
it can return only as "a=Λ on n<N", the support identification R163_1001 / thm:shape(C), which is indexed.
Inserting Q2 into L3 gives the explicit-formula quadratic form restricted to n≤N, with σ-integrated weights. Its positivity on 𝒫_T is
(Π_L), which is REF-D.
**NO-GO** for the class 𝒦_mix = {bounds on 𝒜_S obtained by transporting the band structure of D_S through log|1+D_S/ξ_S(1−s)|}. The
reason is resummation to a place-additive kernel. Partial results requested: (i) Q1, a quantified smallness layer σ−½≲e^{−T}; (ii) Q2, the
exact formula for all T and all F, including the second order; (iii) the subclass "F̂ away from the edge" is vacuous, since no edge-band
term survives. Q2 is not Λ-specific (it survives O_6 and Beurling), and its positivity is REF-D.

## 5. What survives (new residue, ARGUED)
P2 is a property of the **sum** ξ_S (additive object). Any carrier that uses it must pair ΔG with an additive functional of ξ_S, for instance
Re(D_S·conj(ξ_S(1−s)))/|ξ_S(1−s)|², or an L3-type identity for |ξ_S(s)|²−|ξ_S(1−s)|² (not its log), and must never pass through log|·|.
The Green identity for w_S:=|ξ_S(s)|²−|ξ_S(1−s̄)|² has Δw_S=4(|ξ_S′(s)|²−|ξ_S′(1−s̄)|²), which is not signed. No sign was obtained. OPEN, seed only.

## Status
PROVED: Q1, Q2 (exact band formula), Q3 (resummation ⇒ place-additive ⇒ comb-generic). NUMÉRICO: (Q2a) check. NO-GO: 𝒦_mix (the band-gap
mixing route of INV_P_001 §1). REF-D: Q2+L3 positivity. OPEN seed: a non-logarithmic Green identity for the additive defect (§5). No sign.
