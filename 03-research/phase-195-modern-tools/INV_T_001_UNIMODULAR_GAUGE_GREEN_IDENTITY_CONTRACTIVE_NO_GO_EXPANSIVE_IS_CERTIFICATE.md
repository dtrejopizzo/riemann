# INV_T_001: the unimodular gauge in the log-free Green identity (track T)

Inputs: INV_R_001 (R1), AUDIT_195_2 (b), INV_L_001 (L1–L3), INV_P_001 (P2 on ½<σ<1), Paper 46 (def:PD, lem:spec-collapse, thm:Z,
thm:D1, thm:A, O_6 = prop:shape-eulerdel). Notation follows INV_R_001: Φ(½+iτ)=F̂(τ), Ω=Ω_{σ_1}={½<σ<σ_1}, 𝓓(f)=∬_Ω|f′|²dA, and
ψ^♭ ≡ ψ means ∫(ψ^♭−ψ)|F̂|²dτ=0 for every test of the class considered (band equality).

## 0. Index / corpus check and new reason
Index entries checked: Fase 195 (INV_P/Q/R + AUDIT_3/AUDIT_4), Fase 194, G1B/G8B-R160_X_C1 and R162_2201/2202 (Blaschke rigidity / Blaschke–torsion
NO-GO), G2A (deep limit ⟺ Blaschke=1), G3F-104 (deep Blaschke gates), G4B-R161 inner/outer law, G4E-R162_2701 (J-inner Tate chain),
de Branges L16/ES-16/G7F Herglotz, MW-4 (Jensen/Carleson wrong direction), G3D-159 mollifiers, phase-183 Sonin/ε-phase, INV_H gauge collapse.
**New reason:** none of these use a gauge in a *Green energy identity* whose interior is sourceless. AUDIT_4 explicitly opened this residue
(the gauge I that the line does not see). Here inner/Blaschke factors enter only as gauge candidates, and §3 shows they return the indexed
objects (L3/P3 sources, R162 Blaschke). Nothing indexed is reattempted beyond that identification.

## 1. The gauged identity and exact admissibility (Theorem T1, PROVED)
Let I_1, I_2 be holomorphic on a neighbourhood of Ω̄, with |I_j|=1 on σ=½ and at most polynomial growth in |τ| uniformly on Ω̄. Put q:=I_2/I_1.
Assume q is holomorphic. Then for every F∈C_c^∞(I_T) and every σ_1>½:
  (1/4π)∫_{σ=½}|F̂|²∂_σ|q|²dτ = (1/π)[𝓓(I_1Φ) − 𝓓(I_2Φ)] + (1/4π)∫_{σ=σ_1}∂_σ(|I_2Φ|² − |I_1Φ|²)dτ.      (T1)
*Proof.* Apply ∫_½∂_σ|f|² = ∫_{σ_1}∂_σ|f|² − 4𝓓(f) (INV_R_001 R1 proof, AUDIT_4 (a)) to f=I_2Φ and f=I_1Φ. On the line,
|I_2Φ|²−|I_1Φ|² = |I_1|²|F̂|²(|q|²−1)=0, so its σ-derivative is |F̂|²∂_σ|q|². The term ∂_σ|I_1|²·(|q|²−1) vanishes. ∎
**Admissibility (exact recovery).** Since |q|=1 on the line, ∂_σ|q|² = 2∂_σlog|q| there. By L1 (𝔞_T=(1/2π)∫2∂_σu_S|F̂|² for S⊇S_N),
the left side of (T1) equals 𝔞_T(F) on a test class 𝒞 **iff** ψ_q:=∂_σlog|q|(½+iτ) is band-equal to 2∂_σu_S on 𝒞:
- 𝒞=C_c^∞(I_T): iff the distribution ψ_q−2∂_σu_S has Fourier transform vanishing on (−2T,2T). (|F̂|² ranges over autocorrelations,
  supported in [−2T,2T], and by polarization these span a dense set of such test functions.)
- 𝒞=𝒫_T∩𝒟_T: in addition, ψ_q may differ by β_0ĝ_0+β_1ĝ_1 (the two moments defining 𝒫_T in def:PD).
**Only q matters.** The common factor I_1 is completely free: it does not affect admissibility or the value, and it only redistributes
the value between bulk and σ_1-flux. The arithmetic gauge freedom is therefore ψ_q ∈ 2∂_σu_S + {ν̂: supp ν⊆{|u|≥2T}} (+ β·ĝ on 𝒫_T).
This is exactly the freedom (ν,β) of def:PD. This corrects AUDIT_4 (b): the gauge does **not** carry ℤ-data visible to 𝔞_T beyond
(Λ(n))_{n<N}, which is lem:spec-collapse restated on the Green side.

**Corollary T1′ (PROVED, new, sourceless and S-free).** q_T(s):=γ_∞(s)·exp(Σ_{n<N}(Λ(n)/log n)(n^{−s}−n^{s−1})) is admissible on C_c^∞(I_T).
*Proof.* For 0<σ<1, log γ_p = Σ_k(p^{−ks}−p^{k(s−1)})/k, so log ρ_S − log q_T = Σ_{p∈S,p^k≥N}(…). This has ∂_σRe on the line equal to a
finite-S absolutely convergent cosine series with frequencies k log p ≥ 2T, which is invisible. q_T is γ_∞ times an entire zero-free
function. ∎ Hence 𝔞_T(F) = (1/π)[𝓓(Φ)−𝓓(q_TΦ)] + (1/4π)∫_{σ_1}∂_σ(|q_TΦ|²−|Φ|²) for every σ_1>½, with no S and no domain restriction.

## 2. Bulk/boundary localization (Proposition T2, PROVED)
Take I_1=e^{−λ(s−½)} (unimodular on the line) and I_2=qI_1. The σ_1-flux in (T1) is O_{F,q}((1+λ)e^{−2λ(σ_1−½)}). Hence
  𝔞_T(F) = lim_{λ→∞}(1/π)[𝓓(e^{−λ(s−½)}Φ) − 𝓓(e^{−λ(s−½)}qΦ)]   for every admissible q.
So the defect is a pure bulk energy defect. The bulk concentrates in a layer of width 1/λ at the line and reproduces the flux ∫ψ_q|F̂|².
**Consequence:** a sign for the bulk is the same statement as a sign for the line flux. The gauge can move the value between bulk and
boundary, but it cannot create information.

## 3. Candidate gauges carrying ℤ-data (task (2))
| candidate | status | result |
|---|---|---|
| completed phase ξ(s)/ξ(1−s), ξ(s,χ)/ξ(1−s,χ̄) | PROVED | constant (≡1 or ε(χ)) by FE: trivial gauge |
| ζ(s)/ζ(1−s) | PROVED | = Γ_R(1−s)/Γ_R(s) = γ_∞^{−1}: archimedean, comb-free |
| A/A^# for a Dirichlet polynomial/series A (S-smooth or theta/Mellin of L2) | PROVED | unimodular on the line, ψ=2∂_σlog\|A\|; admissible iff log\|A\| band-matches u_S, i.e. A=ξ_S·(invisible outer). L2's S-smooth sums enter only through their band part = Λ(n), n<N (as in Q2) |
| exp(iΣc_n(n^{s−½}+n^{½−s})), exp(Σa_λ sinh(λ(s−½))) | PROVED | admissible as q-modifiers iff the frequencies (log n, λ) are ≥2T or the pairing vanishes on 𝒫_T: = ν̂ (resp. β·ĝ) freedom of def:PD |
| Blaschke B=∏(s−a)/(s−1+ā), a∈Ω | PROVED | \|B\|<1 in Ω. As I_1: inert. As a q-factor: ψ gains a negative Poisson kernel at a (full band, visible) = the L3 Tate sources (P3; R162_2201 Blaschke) |
**O_6 (quantified, PROVED).** The admissible classes satisfy Q(a_P)=Q(ℤ)·∏_{p<P}γ_p^{−1}. Gauge freedom is band-invisible, so the
ℤ–a_P difference of ψ is fixed: 2∂_σ log|∏γ_p^{-1}| on the line, band part = −Σ_{p<P,p^k<N}(2log p)p^{−k/2}cos(kτlog p) (O_P(1) in T).
No gauge amplifies it (cf. R3, where the e^{cT} of P2 is erased). **Beurling (PROVED):** the construction holds verbatim for any (γ_q),
so as a method it is comb-generic. Any discrimination can only come from whether a sign-carrying q exists, and that is Theorem T4.

## 4. The "contractive ρ" idea (Theorem T3, NO-GO PROVED)
(a) Modulus domination is gauge-invariant: |I_2|≤|I_1| ⟺ |q|≤1.
(b) If q is admissible on a class containing F and |q|≤1 on Ω∩{neighbourhood of the line}, then log|q|≤0 there and =0 on the line, so
ψ_q≤0 pointwise. Hence 𝔞_T(F)=(1/2π)∫ψ_q|F̂|²≤0.
(c) At T≤log 2, λ_A(T)>0 (Paper 46 thm:A, PROVED internally), so 𝔞_T(F)>0 for every 0≠F∈𝒫_T. **Therefore no admissible q (for ℤ, on
𝒫_T) is contractive near the line at any T≤log 2.** Under the standing positivity premise the same holds at every T. The proposed key idea
"|Iρ|≤|I| ⇒ 𝓓(IΦ)≥𝓓(IρΦ)" has the wrong orientation. Energy comparison is not monotone in modulus: by T2 with q=e^{ε(s−½)}, ε>0
(|q|≥1), 𝓓(G_λ)−𝓓(qG_λ) → (ε/2)∫|F̂|²dτ > 0 (G_λ=e^{−λ(s−½)}Φ), so an *expansive* multiplier lowers the localized energy. For ε<0 the sign
reverses, which refutes the contractive version.
(d) R4 (|ρ_S|<1 on real (½,1), >1 at large τ) shows that ρ_S itself is neither. By (a) no common gauge changes this.

## 5. The expansive gauge is a dual certificate (Theorem T4, PROVED one way; converse ARGUED)
(⇒, PROVED) If an admissible q on 𝒫_T satisfies log|q| ≥ c·(σ−½) on a one-sided neighbourhood of the line, then ψ_q≥c on ℝ.
By §1, ψ_q = 2∂_σu_S + ν̂ + β·ĝ with supp ν⊆{|u|≥2T}. With L1's identification of 2∂_σu_S with the symbol s_T up to invisible terms
(CITED internal: INV_L_001 L1, AUDIT_195 (a)), (ν,β) is a certificate of value c in def:PD, so c ≤ λ_P ≤ λ_A.
(⇐, ARGUED) Given a certificate f=s_T+ν̂+β·ĝ ≥ c>0 with f real-analytic, the Cauchy problem (Re ℓ=0, ∂_σRe ℓ=f on the line) has a local
holomorphic solution, and q=e^{ℓ} is expansive in a thin layer. Without analyticity this is OPEN.
**Reading.** What I supplies is exactly the pair (ν,β) of a dual certificate: values of a positive band extension outside (−2T,2T),
plus the two 𝒫_T multipliers. It supplies nothing else. Positivity through the gauge is therefore **REF-D** (thm:D1/thm:Z,
indexed), and the gauge is a holomorphic coordinate on the certificate space.

## 6. Self-check (sec:spec clauses), labels
- Clause 1 (lem:spec-collapse): obeyed and re-proved on the Green side (T1). The gauge sees only Λ(n), n<N.
- Clause on atomic or pair-count realization (thm:spec-noatom): not used. (T1′) is an analytic identity, not a measure on log ℚ.
- O_6 / place-additivity (clause 5): the gauge construction is comb-generic, and the ℤ/a_P difference is O_P(1) and gauge-invariant
  (§3). It fails clause 5 *as a method*. The only non-generic content is T4's existence question, which is a certificate.
- Beurling: verbatim construction ⇒ fails as a discriminating object (PROVED).
- Clause 6 / falsifier O_2, O_4: not tested beyond the above. No object is proposed, so this is N/A.
- Margin: none produced.
Labels: T1, T1′, T2, T3 PROVED. T4(⇒) PROVED modulo the internal L1 identification (CITED). T4(⇐) ARGUED/OPEN. Gauge positivity = REF-D.
**NO-GO 𝒦_T:** unimodular gauges in the sourceless Green identity (common or relative, Dirichlet-ratio, FE phases, Blaschke, theta/S-smooth)
give no sign. Contractive gauges are impossible (T3), and expansive gauges are dual certificates (T4).
Live residue (OPEN): T4(⇐) for non-analytic certificates. It has no consequence for the sign. No sign. Row D: OPEN.
No numerics used.
