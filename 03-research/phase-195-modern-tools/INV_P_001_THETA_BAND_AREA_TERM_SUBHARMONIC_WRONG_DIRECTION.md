# INV_P_001: the S-smooth theta modularity inside the Green identity; why area-term positivity points the wrong way (track P)

Notation: INV_L_001 (phase 194). Ω={½<σ<2}, S_N={p<N}, N=e^{2T}, ψ_S(x)=Σ_{n≥1, S-smooth}e^{−πn²x}, Θ_S=1+2ψ_S,
E_S(y)=Θ_S(1/y)−√yΘ_S(y), D_S(s)=ξ_S(s)−ξ_S(1−s), d_S=log|ξ_S(s)|−log|ξ_S(1−s̄)|, G=|Φ_F|², ΔG=4|Φ_F′|².

## 0. Index check and new reasons
- Jensen/LP/subharmonic entries (P33-10 "Jensen excess", MW-4 "every unconditional tool bounds in the wrong direction", MW-7, G3F
  Carleson anti-concentration, G8H strip-Hardy carriers, G7A zero-residual Green identity, G4A-122 two-prime Green complex). **New
  reason:** all of these act on log|ξ| or on zeros. Here the function is the zero-free, finite-S defect d_S, and its Riesz measure sits at
  the reflected *local* poles. §2 checks whether MW-4's wrong direction comes back for this object. It does, and §2 gives the exact
  reason.
- Poisson on ℤ / theta (CA_C_007, EI_002, H3, R163_1001, R160_C8 ε-phase): not reattempted as a sign source. §1 uses L2 only to
  locate *where in frequency* the FE defect lives. No index entry does this.

## 1. L2 entering L3: the FE defect is an edge-band object (PROVED modulo the L2 constant; ARGUED for Beurling/O_6 sizes)
**Lemma P1 (Mellin form of the defect, PROVED).** For finite S and 0<σ<1,
  D_S(s) = ∫_1^∞ e_S(y)(y^{−s/2} − y^{−(1−s)/2}) dy/y,   e_S(y):=ψ_S(1/y) − √y ψ_S(y) = ½(E_S(y)+√y−1).
Proof: split ξ_S(s)=∫_0^∞ψ_S x^{s/2}dx/x at x=1 and do the same for ξ_S(1−s). Both integrals converge on 0<σ<1 because
ψ_S(1/y)=O((log y)^{|S|}). Outside the strip D_S is defined by continuation. ∎ For ℤ, E_ℤ≡0, and P1 is Riemann's proof of the FE.

**Theorem P2 (band localisation, PROVED given L2 in the form |E_{S_N}(y)| ≤ C exp(−πN²/y) on 1≤y≤N²).** Take Y=N²/(2T). Then
  D_{S_N}(s) = P_Y(s) + ∫_Y^∞ e_{S_N}(y)(y^{−s/2}−y^{−(1−s)/2})dy/y + ε_T(s),
  P_Y(s) = Y^{(1−s)/2}/(1−s) + Y^{(s−1)/2}/(s−1) + (Y^{−s/2} − Y^{s/2})/s,
  |ε_T| ≤ C·Y·e^{−2πT} ≤ C e^{(4−2π)T}/(2T)  uniformly on compact parts of the strip.
Proof: on [1,Y], e_S = ½(√y−1) + ½E_S. Integrate the main part exactly; the constants cancel (−1/(1−s)−1/(s−1)=0, ±1/s cancel), so
P_Y is antisymmetric and has removable singularities at 0 and 1. The L2 bound with y ≤ Y gives exp(−πN²/y) ≤ e^{−2πT}. ∎

**Reading in the window variable.** Φ_F(σ+i·) has t-support [−T,T], so ΔG(σ+i·) has τ-frequencies in [−2T,2T]. Every term of
D_{S_N} is a superposition of y^{±s/2}, y^{±(1−s)/2} with y ≥ Y, so its τ-frequencies are ≥ ½log Y = 2T − ½log(2T). **At linear order
the ℤ-specific input (additive lattice ⊂ multiplicative monoid on n<N) says: the FE defect touches the window only in the edge band
|u|∈[2T−½log 2T, 2T], whose width is ½log(2T).** This is the explicit ℤ term requested.

**Failure for O_6 and Beurling (ARGUED, quantitative at the level of the leading term).** For a_P (2∉S′) one has e_{S′} − ½(√y−1) ∋
−(e^{−4π/y}−√y e^{−4πy}). This is ≍1 for y≫1, so D_{S′} carries a low-frequency piece −∫_1^Y e^{−4π/y}(y^{−s/2}−y^{(s−1)/2})dy/y. On
σ=¾ its size is ≍ Y^{1/8}, inside the window band. For a Beurling system the generalised integers are not a lattice, E_B=O(1) already
near y=1, and the low-band mass is ≍ ∫_1^Y|E_B|y^{−σ/2}dy/y ≫ 1. So the band property P2 separates ℤ from both falsifiers. It is the
first statement in this line that is **not comb-generic** (clause (1) as a hypothesis).

**Why it does not enter the sign directly (PROVED as an identity).** The area term pairs ΔG with d_S, not with D_S:
  d_S = log|1 + D_S(s)·Π_{p∈S}(1−p^{s−1}) / Γ_R(1−s)|.
The factor 1/ξ_S(1−s) is not band-limited. Γ_R^{−1} is entire of order 1, and the Euler factors shift frequencies by ±log m for
squarefree S-numbers m. The logarithm mixes frequencies as well. At the sources s_{p,k}=1+2πik/log p the ratio tends to −1, so no
linearisation holds there. The low-frequency part of d_S that the window sees is therefore produced by the mixing alone, i.e. by
(archimedean factor) × (local factors) × (edge-band D). OPEN: a Paley–Wiener / band-gap inequality for this mixing. It is the only
form in which L2 reaches the area term.

## 2. Positivity of the area term against sources + boundary
**Proposition P3 (Riesz decomposition returns L3, PROVED).** d_S is subharmonic on Ω, with Δd_S=2πΣ_{sources}δ ≥ 0, d_S=0 on σ=½,
and no zeros because ξ_S is zero-free. Riesz decomposition: d_S = h_S − Σ_{sources} g_Ω(·,s_{p,k}), where h_S is the Poisson extension of
(0 on σ=½, d_S on σ=2) and g_Ω ≥ 0 is the Green function of the strip. Inserting this into ∬d_SΔG and applying Green's identity to the
h_S part gives exactly L3: the Green-potential terms become the source sums −2π|Φ(s_{p,k})|², and h_S becomes B₂. ∎ So every
inequality that uses subharmonicity of d_S *plus* the Riesz decomposition is a weakening of L3, and the identity already contains all
of that information.

**Theorem P4 (wrong direction, PROVED).** The free positivities are (i) Δd_S ≥ 0, (ii) ΔG ≥ 0 (|Φ′|² ≥ 0, log|Φ′| subharmonic),
(iii) Jensen means of d_p ≥ 0, and (iv) Carleson embedding ∬|Φ′|²dμ ≤ C_μ‖Φ‖² for Carleson μ. Each gives an **upper** bound on
the area term:
(i) d_S ≤ h_S ⇒ 4∬d_S|Φ′|² ≤ 4∬h_S|Φ′|² (needs (ii));
(iii) a mean lower bound on d_p is no pointwise bound. With (ii), it bounds ∬d_SΔG from below only when ΔG(σ+i·) is constant in τ.
That is impossible for F∈C_c^∞ (ΔG decays) except as an averaged statement over translates τ→τ+τ₀, which is the average of 𝔞_T
over modulations. P_T is not modulation-invariant (A(F) moves), so the averaged statement does not restrict to P_T;
(iv) applied to μ=d_S^−dA it bounds the negative part from above, ∬d_S^−ΔG ≤ C‖Φ‖². A *lower* bound on ∬d_S^+ΔG would need a reverse
Carleson (sampling) inequality for ΔG on {d_S>0}. That fails for the window class: F concentrates ΔG at τ-scale 1/T, and for
p<N (log p<2T) the negative cells of d_p near σ=1, p^{−iτ}≈1, have τ-width ≍1/log p > 1/(2T). They are therefore resolvable by window
tests, so no sampling constant on {d_S^+} holds uniformly on P_T.
Conclusion: the four free positivities point the same way as MW-4, now for a zero-free object. Theorem P4 identifies the cause: for a
subharmonic weight, the Green/Riesz structure always gives d_S ≤ (harmonic majorant).

**Subclass check (ARGUED).** For T ≤ ½log2, S_N=∅ and the only source is s=1, which P_T kills. L3 then reads 𝔞_T = (1/2π)[4∬d_∞|Φ′|² − B₂],
with d_∞ → −∞ at s=1 and d_∞ ≈ (σ−½)log(|τ|/2π) at large |τ|. Positivity on this range is known (arch region, Paper 47) but does
**not** come from d_∞ ≥ 0, which fails. This confirms that even the trivial range gets its sign from cancellation in the area term,
not pointwise. No new subclass result is proved.

## 3. Self-check
- Six clauses. (1): the identity L3 is still comb-generic. The P2 band property is not comb-generic (fails for O_6 and Beurling), so a
  sign statement *hypothesised on* P2 would pass (1). (2) ✓, (3) ✓ (not integrality), (4): P2 is not sparse-stable (deleting p=2 creates
  O(1) defect) ✓. (5) ✓ (FE coupling through the local reflected poles and the theta lattice, not ζ(½+iτ)). (6): ✓ at the level of
  L3. P2's ε_T is at log level only after the mixing in §1, which is OPEN.
- thm:shape: P2 is a property of S_N alone, so it survives O_4/O_6 only in the sense that both falsifiers *violate* it.
- REF-D: (Π_L) ⟺ 𝔞_T ≥ 0 on P_T (L3 is an identity, and LHS=𝔞_T for S⊇S_N), so it **is** REF-D. Adding P2 as a hypothesis gives
  (Π_L+P2): "zero-free S-products whose FE defect is edge-band satisfy area ≥ sources+B₂". This is a reformulation with a non-generic
  hypothesis, and that hypothesis characterises S_N (L2 iff). It becomes non-tautological only if the band-gap mixing inequality of §1
  is proved for a class larger than {S_N}. OPEN.

## Status
PROVED: P1, P2 (given the L2 constant), P3, P4. ARGUED: O_6/Beurling low-band sizes, the subclass remark. OPEN: the band-gap mixing
inequality for log|1+D·Π(1−p^{s−1})/Γ_R(1−s)| (the only route by which L2 reaches the sign). NO-GO: positivity of the area term from
subharmonicity, Jensen means, or Carleson/Hardy embeddings (wrong direction). No sign. No numerics were used.
