# INV_R_001: the log-free Green identity. 𝔞_T as a Dirichlet-energy defect of the semilocal γ-ratio (track R)

Positivity is assumed true.
Notation: INV_L_001 (L1–L3), INV_P_001 (P1–P4), INV_Q_001 (Q1–Q3), AUDIT_195.md. S=S_N={p<N}, N=e^{2T}. ξ_S=Γ_Rζ_S,
ξ_S^#(s):=conj ξ_S(1−s̄)=ξ_S(1−s). Φ=Φ_F, F∈C_c^∞(I_T), Φ(½+iτ)=F̂(τ). u_S=log|ξ_S|, d_S=u_S(s)−u_S(1−s̄).
**Domain (per AUDIT_195 item 1):** Ω_1:={½<σ<σ_1}, σ_1<1 fixed. P1/P2 are PROVED only for 0<σ<1, so everything here lives in Ω_1.
𝓓(f):=∬_{Ω_1}|f′|²dA. Window identification (L1, CITED internal): 𝔞_T(F)=(1/2π)∫2∂_σu_S(½+iτ)|F̂(τ)|²dτ for S⊇S_N on 𝒫_T.

## 0. Index / corpus check and new reasons
- **de Branges / Hermite–Biehler (L16, ES-16, P0-3, G1F, G7D-159, G1E-R160_S5, G7F-R162_803 Lagarias–Herglotz, KEPdich).** w_S=|ξ_S|²−|ξ_S^#|²
  is literally the numerator of the de Branges kernel diagonal K_E(s,s) for E=ξ_S. **This is close to a retry. Exact difference:** (i) every
  indexed entry uses E built from the full ξ/Ξ, where HB is the open target, and positivity of the kernel or of the space H(E). Here E=ξ_S is
  finite-S and zero-free, and §4 proves HB **false** for ξ_S universally, so H(ξ_S) does not exist and no kernel positivity is used. (ii) w_S is
  used only as an interior Green weight. Hence the HB question (task item 3) is asked once, for a new object, and answered negatively (R4).
  The kernel/space version is not reattempted.
- **Green identities:** L3 (log weight d_S), G7A zero-residual Green identity (phase 120 cell 7A, via INV_P §0), G4A-122 P122_028 two-prime
  finite Green complex (DEAD: constant flux, needs input beyond log p, p^{−½}, N, Γ). **New reason:** the weight here is log-free and has no
  sources. Item (6) of the audit asks for these citations; G4A-122's death reason ("needs input beyond log p, N, Γ") recurs in §3 as R2.
- **Dirichlet energy:** P57-1 (Dirichlet-energy identity for E(T), classical analytic NT) is a different object. **Kreĭn/Herglotz, MW-4,
  P33-10 Jensen, Carleson:** §4 only checks that the free positivities give the MW-4 direction (P4). They are not reattempted.
- **Semilocal γ-factors:** R160_C8 ε-phase (DEAD F3), phase-183 Sonin chain, L1. §3 shows the identity's interior object is exactly ∏γ_v,
  i.e. the L1 object. This is recorded as the reason for the NO-GO and is not a new attempt.
- Grid / crossword (CROSSWORD-TO-D): no Green identity with a log-free weight is registered.

## 1. Which log-free functionals vanish on the line (Lemma R0, ARGUED)
A Green weight that recovers a σ=½ flux with no line term must vanish on σ=½. Among sesquilinear expressions in (ξ_S, ξ_S^#) with holomorphic
multipliers h, the antisymmetric ones are: (a) |hξ_S|²−|hξ_S^#|², the modulus side, whose flux is ∫|hξ_S|²·4∂_σu|F̂|²; (b) Im(h²ξ_Sξ_S^#),
the phase side, whose flux is ∫|hξ_S|²·∂_τarg ξ_S·(…), i.e. the ε-phase/Sonin object (R160_C8, phase 183, indexed, not pursued).
Re[ξ_S·conj ξ_S^#] and |D_S|² do not vanish on the line (=|ξ_S|², 4(Im ξ_S)²), so they leave a line term and do not recover 𝔞_T. Only (a) is live.

## 2. The exact identity (Theorem R1, PROVED)
**Normalization lemma.** With G=|hΦ|², the flux of (a) at σ=½ equals 2π𝔞_T(F) exactly iff |hξ_S|≡1 on σ=½. For h holomorphic and zero-free
in Ω_1 this means h=I/ξ_S^# with I unimodular on the line (outer part fixed). Then the weight is w_S|h|² = |I|²(|ρ_S|²−1), where
  ρ_S(s):=ξ_S(s)/ξ_S(1−s)=γ_∞(s)∏_{p∈S}γ_p(s),  γ_∞=Γ_R(s)/Γ_R(1−s),  γ_p=(1−p^{s−1})/(1−p^{−s}).
ρ_S is holomorphic in Re s>0 (1/ξ_S^# is entire). Its zeros are exactly the L3 sources s=1 (order 1+|S|), s=1+2πik/log p, and s=3,5,…,
so ρ_S has no zero in Ω_1, and |ρ_S|=1 on σ=½. The raw choice h=1 gives the |ξ_S|²-weighted form ∫σ_T|ξ_SF̂|². That is not 𝔞_T, because
ξ_SF̂ is not a window test and L1 fails off window tests. The choice h=1/ξ_S gives the weight 1−|ρ|^{−2}, which is singular at the sources.
**Answer to item (1):** 𝔞_T is recovered **exactly, not as a limit, with ξ_S as a weight (h=1/ξ_S^#)**. The price is that the weight becomes
v_S:=(|ρ_S|²−1)/2 = w_S/(2|ξ_S^#|²) = Re x_S + |x_S|²/2, where x_S=D_S/ξ_S^#.

**Theorem R1.** For F∈C_c^∞(I_T), S⊇S_N, ½<σ_1<1:
  𝔞_T(F) = (1/π)[𝓓(Φ) − 𝓓(ρ_SΦ)] + (1/4π)∫_{σ=σ_1}∂_σ(|ρ_SΦ|² − |Φ|²)dτ,
or equivalently 2π𝔞_T(F) = 4∬_{Ω_1}v_S|Φ′|² − 2∬_{Ω_1}|Φ|²|ρ_S′|² − B^v_{σ_1}, with B^v=∫_{σ_1}(v∂_σ|Φ|²−|Φ|²∂_σv).
*Proof.* For f holomorphic on Ω̄_1 with rapid τ-decay, Δ|f|²=4|f′|², so ∫_{½}∂_σ|f|² = ∫_{σ_1}∂_σ|f|² − 4𝓓(f). Apply this to f=ρ_SΦ and to f=Φ
and subtract. On σ=½, |ρ_S|=1 gives ∂_σ|ρ_SΦ|²−∂_σ|Φ|² = |F̂|²∂_σe^{2d_S} = |F̂|²·2∂_σd_S = |F̂|²·4∂_σu_S. Decay holds because ρ_S grows
polynomially in τ (Stirling) and Φ decays rapidly. The second form is Green's second identity with weight v_S (Δv_S=2|ρ_S′|², v_S=0 on σ=½). ∎
**Reading.** There are no sources and no point evaluations. The Tate moments of L3 (−2π|Φ(s_{p,k})|²) and the A(F) term are absorbed into the
smooth energy 𝓓(ρ_SΦ). The logarithm appears only at the boundary, linearly, through d_S=0 ⇒ ∂_σe^{2d}=2∂_σd: this is a first-order Taylor
step at d=0, which is exact. That is how a functional nonlinear in the comb returns a form linear in Λ. 𝒫_T plays no visible role in R1, since
it holds for every window F. Positivity reads: **multiplication by ρ_S does not increase the Dirichlet energy on Ω_1 beyond the σ_1 flux.**

## 3. Does P2 survive? (Theorem R2, PROVED as structure; Prop R3)
**R2.** Every interior term of R1 is a functional of ρ_S=∏_vγ_v, which is place-multiplicative and depends only on the local factors. R1 holds
verbatim for every Beurling system (γ_q) and for a_P (drop γ_p, p<P). By the normalization lemma this is forced: any log-free weight of type (a)
that recovers 𝔞_T exactly factors through ρ_S. **P2 survives only as an exact rewriting:** D_S=ξ_S^#(ρ_S−1). The edge-band cancellation of
D_S (on 0<σ<1) is the low-band cancellation between ξ_S and ξ_S^#. Dividing by ξ_S^#, which carries the frequencies log n of all S-smooth n,
spreads it over all S-unit frequencies log(m/n). Erasure of P2 is therefore **not caused by the logarithm**. It is caused by the normalization
that any exact recovery of 𝔞_T requires (division by ξ_S^#). INV_Q_001 Q3 is a special case (log of the same ratio).
**R3 (quantified failure, PROVED for the ratio; the D-side size CITED from INV_P with AUDIT_195 item 4).** For a_P with 2∉S′ (O_6), the low-band
part of D_{S′} grows like √y on the Mellin side, i.e. like a positive power of Y=N²/2T, so like e^{cT}. On Ω_1, though,
  ρ_{S′}/ρ_{S_N} = ∏_{p<P}γ_p^{−1},  |γ_2^{−1}(s)| ≤ (1+2^{−σ})/(1−2^{σ−1}) on ½<σ≤σ_1<1,
which is bounded independently of T and N. So in R1 the e^{cT} separation P2 provides between ℤ and O_6 is compressed to a T-independent
multiplicative factor (O_P(1)). For Beurling, ρ_B=∏γ_q has the same form with log q in place of log p. R1 cannot distinguish B from ℤ except
through the positions log q. That is the comb data, the same as G4A-122's "no input beyond log p, N, Γ".

## 4. Sign search (Theorem R4 PROVED; NO-GO class 𝒦_R)
**(a) Hermite–Biehler is false for every finite S, ℤ and Beurling alike (PROVED).** For ½<σ<1 real: Γ_R′/Γ_R(σ)=−½logπ+½ψ(σ/2)<0, because
ψ(σ/2)<ψ(½)≈−1.96<logπ, so Γ_R is decreasing on (0,1) and d_∞(σ)<0. Also d_p(σ)=log(1−p^{σ−1})−log(1−p^{−σ})<0, because p^{σ−1}>p^{−σ}.
Hence |ξ_S(σ)|<|ξ_S^#(σ)|, i.e. v_S<0, on (½,1) for every S and every Beurling system. The reverse inequality fails at large |τ|, where
d_∞≈(σ−½)log(|τ|/2π)>0 dominates the bounded Σd_p (bounded for fixed S). So neither HB nor reverse-HB holds on any half-strip: **ξ_S is not
a de Branges function, and this is not ℤ-specific.** Partial positive statement (ARGUED): HB holds on {|τ|>τ_0(S,σ)} with
log τ_0 ≍ Σ_{p∈S}p^{σ−1}/((σ−½)(1−p^{σ−1})). For S_N this is ≍N^σ/((σ−½)log N), far outside any window scale.
**(b) Free positivities give the MW-4 direction (PROVED).** Δv_S=2|ρ_S′|²≥0 enters R1 with a minus sign. v_S≥−½ gives only the trivial bound
2π𝔞_T ≥ −2𝓓(Φ) − 2∬|Φρ_S′|² − B^v. Subharmonicity of v_S (maximum principle) gives v_S ≤ harmonic majorant, an upper bound on the area term
(as in P4). |ρ_S|≥|Blaschke of the sources| is exact in a strip (the Riesz decomposition, = P3). The half-plane version would be a genuine
lower bound, but it fails: the archimedean zeros s=3,5,… violate the Blaschke condition, and ρ_S grows factorially as σ→∞.
**(c) Contractive-multiplier reading.** "𝓓(ρ_SΦ) ≤ 𝓓(Φ) + flux on 𝒫_T" is R1 rewritten. It is **REF-D**, and as an operator statement it is not
sparse-stable-free: it is a statement about ∏γ_v, i.e. L1's object.
NO-GO for 𝒦_R = {Hermite–Biehler/de Branges inequality for ξ_S, maximum principle and subharmonicity of v_S, |·|²-Laplacian positivity,
Blaschke lower bounds} applied to the log-free identity. No sign.

## 5. Self-check (six clauses, thm:shape, REF-D)
(1) **fails**: R1 is place-multiplicative and holds verbatim for Beurling and a_P (R2, R3). (2) ✓ not a cone on log ζ (a ρ^c-family is not
closed under the energy inequality; ARGUED). (3) ✓. (4) The identity is sparse-stable (it holds for a_P). The inequality is not (a_P fails
WP at T≥0.60), but nothing in R1 sees the difference beyond O_P(1) (R3). (5) The FE coupling is literal through ρ_S=ξ_S/ξ_S^#, but ρ_S=∏γ_v
is place-by-place, which is exactly L1's O_6-stable class ⇒ **fails**. (6) ✓: the interior is log-free, and ∂log occurs only as the exact
boundary Taylor step. REF-D: R1 is an identity, so 𝔞_T≥0 on 𝒫_T ⟺ the energy inequality, which is a reformulation.
thm:shape: ρ_S changes by O_P(1) under O_6, so no T-uniform separation is available.

## Status
PROVED: R1 (exact log-free Green/Dirichlet-energy identity on ½<σ<σ_1<1, no sources), normalization lemma, R2 (structure: any exact recovery
factors through ∏γ_v, and P2 is erased by division by ξ_S^#, not by the log), R3 (O_6 ratio bound), R4(a) (HB false for every S and every
Beurling system on (½,1)), R4(b). ARGUED: R0 classification, large-|τ| HB region. CITED: P2 sizes (INV_P, corrected by AUDIT_195).
NO-GO: 𝒦_R. REF-D: energy-comparison form. No numerics. No sign.
Do not retry: log-free Green weights recovering 𝔞_T (they factor through the γ-ratio), or HB/de Branges for ξ_S. Live residue (OPEN): a carrier
that uses ξ_S **without** normalizing on the line, i.e. accepts the |ξ_S|²-weighted form h=1 and transfers to window tests by a separate
argument. That needs L1 off the window (atoms p^k≥N), which is not available.
