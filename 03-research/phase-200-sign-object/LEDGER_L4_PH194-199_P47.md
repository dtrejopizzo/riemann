# LEDGER L4 — insight ledger on the sign, phases 194–199 + Paper 46

Scope: phases 194 (invention), 195 (modern tools), 196 (global object), 197 (barrier), 198 (parity split), 199 (frontier
pattern + `proof-L-sharp/`, A–OO, AUDIT_L_SHARP_1–17, AUDIT_CONSTRAINTS_001, BRIDGE_001, SYNTHESIS_MECHANISM_001,
MORI15_EXTREMAL_001, TEST_*), and Paper 46 (`sec:spec`, `subsec:strip`, `subsec:shape-geom`, `sec:ext`, `subsec:ext-pos`,
`subsec:ext-constraints`). Labels are the audited ones (the audit wins over the original memo). Abbreviations: PL# = `03-research/phase-199-frontier-pattern/proof-L-sharp/`; P46 = Paper 46.

## 1. Positive structural facts about the sign

### 1a. Exact identities (the frame in which the sign lives)

| # | fact | label | provenance |
|---|---|---|---|
| I1 | **Half-line identity.** W_T(g) = 𝒲_ext[Ψ_f] = −𝒲(g,Ψ_f), g = Ef\|_I, Ψ_f the aliasing tail of Ef below the window; with the killing term when written on the half line. The window form *is* the complete Weil form of what the summation map pushes outside the window. | PROVED given Guo 4.2–4.5 | PL# A Thm 1.1, E Thm E.1, AUDIT_1; P46 thm:ext-half |
| I2 | **Möbius bijection.** E: L²[1/λ,λ] → L²(I), E⁻¹g = Σ μ(m)(mu)^{−½} g(log mu), norms ≤ 2√μ; gauge (−1/λ,1/λ) = radical; ℓ = dist²(r, 𝒢̄). | PROVED | MECH_001 Prop 3.1; P46 lem:ext-mob, prop:ext-gauge |
| I3 | **Universal form.** 𝒲_ext[Zr] = λ⁻¹𝔔[ρ]: one μ-free form 𝔔 on L²(1,∞); all μ-dependence is in the data class PW_μ mod the fixed radical. | PROVED | F Prop F.0; P46 prop:ext-univ |
| I4 | **Critical-line form.** 𝔔 = (1/2π)∫[Θ_∞\|F\|² − 2Re F̄F_log] + 2AB, F built from partial sums ζ_X(1−s), Θ_∞ = −2Re ζ′/ζ on Re s = ½ (Im ζ′/ζ never enters). | PROVED | F Thm F.1; P46 thm:ext-line |
| I5 | **Comb collapse.** On Z-images the prime comb is the log-weighted summation map (Λ∗1 = log): 𝒲_ext is Λ-free; W_T(Ef) = 𝒜_a[Zr] + 2AB − 2⟨Zr, Z_log r⟩. Pole cancels the Chebyshev main term exactly (residue 1). | PROVED | E Thm E.2, Lemma E.4; B L3.1 |
| I6 | **Mirror theorem.** Q(G,G) = −𝔔_line[c] + 2𝔅 − R(1)G_h(0) + c₀ρ₀² − 2ρ₀ρ₁ (Poisson self-duality of ℤ + Re M′/M = Θ_∞). The "defect half" is exterior positivity of the dual data, not a reduction. | PROVED on C_c^∞(1,∞); CONDITIONAL on PW tails | AUDIT_4 §6; P46 thm:ext-mirror |
| I7 | **Reflection / P.1–P.2.** 𝔔 = −Q(G,G) + 2Q(F,G) + 2AB, Q(F₀,F₀) = 0 (Euler–Maclaurin smooth part is a null vector of the line form); pole's F₀-piece = s = 0 residue of the coupling. | PROVED | P_001, AUDIT_3; P46 prop:ext-residue |
| I8 | **Remainder pairing (V).** 𝒲_refl[u] = ∫e^{−t/2}(u∗u) dR_Λ, R_Λ(t) = ψ(e^t) − e^t + ½log(1−e^{−2t}); W_T(g) = ∫e^{−t/2}(ǧ∗Ψ̌) dR_Λ; the PNT main term of the prime self-convolution is exactly A². | PROVED (REF-D) | V_001 §2.1 |
| I9 | **Möbius-lattice form (Thm D).** f = Σ_{m<μ} μ(m)H(mu) + φ₀ with one function H = h·1_{[1/λ,λ)}; ratio-grouped Ψ̌ with coefficients C_{b/a} = μ(a)M̃_a(μ/a)/a depending only on the denominator; line m in dilate 1 ≡ line nm in dilate n ⇒ exact resonance with sign μ(n). | PROVED | AA_001, AUDIT_13; EXTERIOR_DATUM_001 Lemma E.1; P46 thm:ext-lattice |
| I10 | **FF.1 comb of translates.** Ψ̌(x) = Σ_{N≥μ} c_N N^{−½} g(x − log N) + gauge mirror (+ polar ≡ 0 by GG), c_N = Σ_{m\|N, m<μ} μ(m) = Möbius truncation tail, c_N = 0 for 2 ≤ N < μ. Edge jet Ψ̌^{(k)}(a+) = [1 + (−1)^k c_μ μ^{−½}] g^{(k)}(a). | PROVED | FF_001, AUDIT_16 |
| I11 | **Mellin of the translate comb.** Σ c_N N^{−s} = ζ(s)M_μ(s) − 1 (mollifier defect); W_T(g) = 𝒲[D_μ g]; linear identity W_T(g) = −Σ c_N N^{−½} F_g(log N) (X-limit, boundary R_X → 0 OPEN). Gram of (g,Ψ̌) = W_T(g)·[[1,−1],[−1,1]]. | PROVED (GG.1 limit CONDITIONAL) | GG_001, II_001, AUDIT_16 |
| I12 | **Lossless loop.** Each prime channel strictly positive-real (Re ≥ 1/(1+p^{−σ})); the full-line closed loop plant × ∏(1−p^{−s})^{−1} is lossless (∂_σ\|Γ_ℝζ\|² = 0 on the line). | channel PR PROVED; loop CONDITIONAL | MM_001, AUDIT_17 |
| I13 | Strip identities: Green–FE-defect (L3), sourceless energy identity with ρ_S = ξ_S/ξ_S^# (R1, NUMÉRICO 1e−13), gauged identity (T1, entire gauge T1′), exact band formula (Q2), place-splitting (S1). | PROVED | phases 194–195; P46 subsec:strip |
| I14 | Exact split 𝔞_T = A_∞ + ½𝔄ff − ½Re⟨Vf,f⟩_Ш (affine near-coincidence form; non-diagonal); Hecke–Chebyshev transfer V*Ш = 2log\|x\|·Ш. Holds for every lattice αℤ (V2.2(c) FALSE). | PROVED | INV_V_002, AUDIT_196 |
| I15 | Divisor-gauge symbol s_φ = m − 2Re[ζ(½+iτ)Q_φ]; ζ(½+iτ) is a universal carrier common to every window comb incl. a_P. | PROVED (K2 only ARGUED) | INV_H/K, REVIEW_K2; P46 thm:spec-carrier |

### 1b. The extremal anatomy at μ = 15 (Mori's certified bottom; all NUMÉRICO unless stated)
- Galerkin bottoms 4.7634661356·10⁻⁷⁰ (even; certified 2.40·10⁻⁷⁰) and 6.109·10⁻⁶⁶ (odd). Even g* = super-Gaussian bump
  (σ = 0.209, ∫g = −0.867). (MORI15_EXTREMAL_001, reproduced AUDIT_6.)
- **Pieces (50 digits):** Γ_ℝ −5.3722 + Lévy +3.9164 + pole +1.5190 − comb 0.0632 (n = 2 carries 99 %) = 4.8·10⁻⁷⁰.
  ã-form = R_Λ = −0.785800. Odd sector: the comb (+0.340, c(log 2) < 0) is the *positive* carrier.
- **f* = E⁻¹g* is Fourier-self-dual:** f* = 1.106ψ₀ − 1.822ψ₄ + 3.3·10⁻⁵ψ₈ + …, all a_{4j+2} ≤ 6·10⁻³⁸ (repair along ψ₄,
  not ψ₂). Self-duality = parity of g* in the standard 𝔉 (PROVED identity, AUDIT_6). f* ≈ Riemann–Pólya kernel (overlap
  0.99981), but forced: f(0)=0 in span{h₀,h₄} is f_P (AUDIT_7).
- **κ_emp = W_T/ℓ ≥ 0.56** (upper end 1.09 ARGUED); W_T/(1−λ₄) = 4.08; 1−λ₄ = 1.16682499·10⁻⁷⁰ reproduced. Spectral ladder
  λ_j/(1−λ_{4j}) = 4.08, 1.99, 1.79 (even), 3.03, 1.57 (odd).
- **Caustic t* ≈ 4πμ − (2k+1)/2 = 183.9** (k = 4): Fg* vanishes at zeros below t* (10⁻⁶⁸…10⁻³⁸), plateau above; data peak at
  n = 71–72 (ARGUED + NUMÉRICO, W_001/AUDIT_7). Zero data used as check only.
- **Rough complement:** g* = p + δ (p = g*_50): W(p) = 1.2325, 2W(p,δ) = −0.4650, W(δ) = 0.2325 (×W*); δ uniform,
  91 % non-prolate, exterior at ω ≥ 2. The (1,2)/X₁₁ = −0.35 deficit is E⁻¹p − prolate on the outer window, with
  directional cross −0.481 vs reverse 0.000.
- **Loop gains μ(n)-signed:** resonance of line m@1 with nm@n carries sign μ(n) (6/6, n = 2..7; band test 8/9 squarefree;
  (1,4) of p is +0.108, sign 5/5 on μ ≠ 0). Lines m ≥ 2 are 10³²–10³⁴ × ρ_p: **33–34-digit cancellation** (AUDIT_13).
- Lattice Gram on 10 squarefree lines PD (1e59–1e67 W*); with φ₀ (10,0,1), null vector v = μ ⊕ 1; vᵀGv = W(p) needs
  ~70 digits. The sign lives in the cancellation direction, not in inertia (GRAM_INERTIA_001).
- Floor perturbation falsified: ‖QCp‖ = ‖QArp‖ = 0.2008 cancel to 1.7·10⁻³⁵ (34 digits) (BB_001).

### 1c. Proved positive regions
- **Lemma B.0** (PROVED): 𝔴_μ(ω) ≥ log 2μ for all ω > 1, μ ≥ 4, via H_N log N ≥ 2H₁(N); phase-space w(ω,ν) ≥ H(ω)log(ν/2π).
  F(N) = H_N log N − 2H₁(N) ∈ [0, γlog N + 1]. (BRIDGE_001, AUDIT_8.)
- **Theorem B** (single-cell chirps, PROVED after constant repairs): 𝔔[ρ] = ∫w|a|² + O(ν₀⁻¹) on supp ⊂ [N+δ, N+1−δ];
  comb = −2H₁(N)‖ρ‖² exactly; 𝔔 > 0 for ν₀ ≳ polylog N; cΛ with c > 1 negative as N → ∞ (proved window falsifier).
  P46 thm:ext-cell, cor:ext-cellpos, cor:ext-cfals.
- **Theorem B′** (multi-cell Langer chirps, PROVED as asymptotics): 𝔔 ≥ (log 2μ − O(c^{−½}log c))‖a‖²; relative phase of
  dilates (1,n) concave with unique stationary point s_n = √(1+n⁻²); vacuous at μ = 15 by ≈13×, μ ≳ 10³. P46 thm:ext-multi.
- **Theorem C** (caustic layer, PROVED given envelope; envelope CC_001 PROVED): layer diagonal (1−χ_k)[(2/3)log 4N − 0.107689](1+η),
  closed form ∫₁²𝔴_μ = (2/3)log 4μ − Cl₂(2π/3)/(2π); turning point regular-singular (Bessel J₀); amplitude product n-free;
  explicit |η| non-vacuous only for N ≳ 130–820. P46 thm:ext-layer (iv) open.
- **Prop JJ.3** (PROVED, elementary): branch-averaged (1,n) block |B_n|² ≤ θ_n²A_nC_n, θ_n² < 1/(nH_n) ≤ 1/3; gap ≥ 0.42 log 2μ
  uniformly. Operator version JJ.4 CONDITIONAL on Fresnel-scale transfer.
- Others: Prop H.1 base case L′♯ on 5 ≤ μ ≤ 15 with A = 2, κ = 2^{−2905}/C₀ (PROVED, Mori CITED); comb-generic L′♯ with A = 2
  above frequency Ω_* = e^{𝒜_T+λ+O(1)} (A_001, P46 lem:ext-hf); D_odd on T ≤ ½log5 (AA_001); (I_T) on 𝓔𝓟_Q for T ≤ ½log5 (D2);
  W1: n₋(𝔞_T\|P_T) non-decreasing, all crossings downward (PROVED).

### 1d. Lemma M and the falsifier battery
- **Lemma M** (PROVED, AUDIT_198): for fixed comb a, T ↦ λ_A(T;a), μ_±(T;a) are non-increasing; certificates extend upward,
  margins are piecewise between contacts (PATTERN_001).
- **Falsifier battery (PROVED by interval enclosure, CERT_FALSIFIERS_001 + Lemma M):** Y_001 deletions q = 3 (T = 0.75,
  ½log5+0.01), q = 7 (T = 1), q = 8 (log 3); odd-sector falsifiers: zero comb (½log5, 1), a_2, 2Λ, 1.15Λ (T = 1), a_3 (½log5).
  Plus the standing set cΛ (c ≠ 1), a_P, Beurling, F-DH. Quantitative signature: Λ sits at +κ(1−λ₄) with κ ≈ 4.1–5.4, each
  falsifier at −Θ(1) (NUMÉRICO). Single deletions λ_A(T; Λ−q) ≈ −0.08…−0.71 on [log2, ½log11).

### 1e. The six-clause specification (P46 prop:spec)
(1) not linear / not comb-generic — PROVED (PD/hyperbola/Dirichlet-algebra exclusion CONDITIONAL); (2) not a cone condition
on log ζ (O_4-closed) — PROVED; (3) not coefficientwise integrality (𝒞_{01}, 𝒞_ℤ, 𝒞_1 = {Λ}) — PROVED; (4) not sparse-stable
(a_P via O_6) — PROVED; (5) couples (Λ(n))_{n<N} with the FE by a route other than ζ(½+iτ) — OPEN, no object known (strip
identities meet the wording but are comb-generic); (6) crosses ∂log without losing positivity (only ID cones + Pick/real-zero
cross) — ARGUED. Supporting: thm:spec-noatom (no measure on log ℚ_{>0} equals 𝔞_T on P_T) PROVED; first non-homogeneous
relation is Selberg's ΛL + Λ∗Λ = μ∗L².

### 1f. The 28 constraints (AUDIT_CONSTRAINTS_001)
- **HARD:** 1 (TV-slack ≤ λ^W on the window carrier; size CONDITIONAL), 2 (no comb-generic identity + Bochner/C–S/Schur),
  8 (no antisymmetric Hilbert kernel in integer index, narrow), 12 (no Eψ₀ + small repair), 17 (fix gauge first),
  24(a,b) (Möbius-lattice structure; single-line models invalid).
- **SOFT:** 3, 4 (multiplier NO-GO only ARGUED after C Thm 6.1 retraction), 5, 7 (does not bind on chirps, JJ), 10
  (relocated, not vacuous: II_001), 11, 14, 15, 18, 19(b), 21, 25, 27, 28.
- **MISLABELLED:** 6, 9, 13 (a positive fact: pole is rank-one), 16 (open prerequisite), 20, 22, 23 (empty), 26 (tool gap).
- Pair exclusion: 19(b) + 26 + base μ ≤ 15 block "asymptotics + Mori base" unless 15 < μ ≲ 130 is covered.

## 2. Common failure signature (≈45 routes: INV_A–U, V, BARRIER/D1/D2/W/X/Y/Z, AA/BB/CC, A–OO)

Every route ends in one of three places, and they are the same place seen from three sides. (i) **Comb-genericity:** the
identity used (strip Green/energy/gauge identities, divisor gauge, Lévy split, Bakry–Émery, stability, passivity, boundary
triples, Hilbert kernels, multipliers) holds verbatim for cΛ, a_P or Beurling, so it carries no sign; the Λ-content is
exhausted by a_n ≡ 1, residue 1, conductor 1 and aliasing, and identities (Λ∗1 = log, pole = Chebyshev main term) *erase*
Λ rather than expose it. (ii) **REF-D:** when the identity is exact and Λ-specific, its positivity statement is the window
form rearranged — every reformulation returns "ν̂ ≥ 0 on the admissible cone" (GG: the sign factor of W_T = 𝒲[D_μ g] is ν̂;
T4: gauge freedom = dual certificates; R/L3: energy form = REF-D; OO: minimal-operator positivity = λ_A ≥ 0). (iii)
**Cancellation that bases cannot see:** in every coordinate system that makes the arithmetic visible (Möbius lines, prolate
rungs, translate comb, kink jets, ratio classes, sectors) the individual pieces are 10³²–10³⁵ times the answer and cancel to
33–34 digits (lines m ≥ 2 vs ρ_p; ‖QCp‖ vs ‖QArp‖; vᵀGv ≈ 70 digits; FF.1 comb vs gauge mirror; arch/comb in ‖QGP‖); Gram
inertia is PD and blind; no subspace is almost invariant (V_J); Schur planks need the exact resolvent. And when one tries to
make the cancellation structural as a feedback loop, the loop is **lossless** (MM): each prime channel is strictly passive
but the closed loop has zero margin on the line, the strict margin being exactly the truncation energy = W_T (circular). So
the sign is never a property of any piece, of any channel or of any basis; it is a property of the *admissibility direction*
(f(0) = f̂(0) = f(λ) = 0 modulo gauge) along which O(1) pieces cancel to e^{−4πμ}, and proved positivity exists only where
the data class avoids that direction (single/multi-cell chirps, caustic layer, high frequency, μ ≤ 15).

## 3. Seeds (OPEN residues never attacked)

1. **R2 of JJ — Möbius-channel matrix symbol.** Positivity of the lattice Gram G_{m,m′} = Σ_n [coincidence weight]·μ(n)
   with the 𝔴 diagonal, lines m = 1…⌊μ⌋ with weights μ(m)/m and exact coincidences m@1 ↔ nm@n. Explicitly "not attempted";
   "the only place a Λ-specific (Möbius) sign can enter this symbol". Needs: a branch-averaged symbol on the lattice class
   (extend JJ.3 from (1,n) to (m,nm)), a bound on Möbius partial sums C_q = Σμ(bk)/(bk) used *exactly* (not |M̃| ≤ 1,
   which holds for falsifiers), and compatibility with constraint 25 (work in a basis where the 33-digit cancellation is
   already performed, e.g. FF.1 translates).
2. **Sign of the interface I on the Sonin annulus.** LL_001: in 𝒮(1,1) the mirror closes, (C_G)(b) ⟺ 𝔔[σ] ≥ I(σ)
   (CONDITIONAL); sign of I OPEN (ARGUED indefinite). Needs: the closability/core lemma of U.3 and the Sonin→PW transfer
   (constraint 16), then a sign of a rank-limited interface functional.
3. **Fresnel transfer (R1 of JJ / Y.8).** Symbol → operator at Fresnel scale, turning JJ.3 into JJ.4. Needs a pseudo-
   differential calculus for the two-branch Langer map with remainder O(c^{−½}) uniform in X (AUDIT_9 shows the current
   bound is not uniform in X).
4. **Non-local cell content.** Δr_out = E⁻¹p − prolate on the outer window, 91 % non-prolate, not kinks (TEST_KINKS: NO),
   not jets (constraint 28). Its directional cross (−0.481, reverse 0) is unexplained. Needs a canonical description
   (probably as FF.1 translates N ≥ μ with c_N signed) and a theorem that its pairing with the prolate core is bounded by
   the leakage scale.
5. **The odd Weil distribution W⁻.** dN/dT = −2G_φ(−2T)(W⁻G_φ)(−2T) with W⁻ odd (Hilbert-type), residue-1 cancellation inside
   (H_001). Never studied as an object. Needs: sign/positivity structure of W⁻ restricted to dilated summation images; it is
   the generator of all motion in T.
6. **dR_Λ identity of V.** W_T(g) = ∫e^{−t/2}(ǧ∗Ψ̌) dR_Λ with R_Λ = ψ(e^t) − e^t + ½log(1−e^{−2t}). Labelled REF-D but never
   pushed as a *measure* question: a positive-definiteness statement for e^{−t/2}dR_Λ restricted to the cone {ǧ∗Ψ̌: g
   admissible} (a cross-correlation cone, not an autocorrelation cone). Needs a description of that cone.
7. **Conjecture κ-band.** κ₋(1−λ₄(2πμ)) ≤ λ^W ≤ κ₊(1−λ₄); upper CITED for μ ≥ 50 (Mori K, up to log μ). A *comparison*
   (stability estimate for the Guo residual identity at resolution e^{−4πμ}), not a sign. Needs coercivity off span
   E{ψ₀…ψ₃} crossing every contact jump; gap 15 < μ < 131 uncertified (KK).
8. **Exact crossing law.** λ_A is C¹ across crossings for fixed data (ARGUED), crossing of q enters at second order with
   coefficient −4c_q G_φ(−log q)φ′(1) (Cor H.4′, PROVED); edge law h* ~ (log κ/δ)^{−½} ARGUED; jump formula CONDITIONAL on
   traces. The sawtooth has no mechanism (Möbius hypothesis CONTRADICTED; Λ-contact reading 7/9). Needs the sub-integer
   high-precision test (10–25 h) and a proof of U3.
9. Smaller: Kronecker–Hurwitz elliptic seed (INV_D, unindexed); non-conic constraint on (1, Λ, L) via 1∗Λ = L (INV_F);
   small-τ sign of the pole-free q ≥ 2 divisor symbol (INV_H); approximate eigen-kernels of the Hecke–Chebyshev transfer
   (INV_V_002 G1); non-log Green identity for |ξ_S(s)|² − |ξ_S(1−s̄)|² (INV_Q); J²Σ|ρ|⁻² = 4.66·10⁻⁷⁰ coincidence (unexplained);
   R_X → 0 in GG.1; exact-resolvent Schur plank with leakage margin 0.612 (constraint 27).

## 4. The sign object, as this slice dictates it

From this slice alone, the sign object must be a **lossless-loop residue on the Möbius lattice that lives exclusively in the
admissibility direction**: an exact object whose *coordinates are already the post-cancellation quantities* — the
truncation-tail coefficients c_N = Σ_{m|N,m<μ}μ(m) of ζM_μ − 1 placed at log N, N ≥ μ, together with the gap 2 ≤ N < μ where
they vanish — so that the 33–34-digit cancellation is built into its definition instead of performed by its users. Its
positivity would not be a pointwise symbol, a channel passivity or a Gram inertia (all blind), but a *dissipation defect
of a lossless loop*: the closed loop plant × Euler product is lossless on the line, each prime channel strictly passive,
and the sign must measure how truncating the loop at λ (the Möbius mollifier of length μ) breaks losslessness — a quantity
that is O(e^{−4πμ}), measured against the prolate defect 1−λ₄ (index 4 = number of absorbed admissibility conditions,
f* self-dual on ψ₀,ψ₄), positive for Λ because the defect couples only through squarefree coincidences m ↔ nm with signs
μ(n), and −Θ(1) for every certified falsifier because cΛ (μ_c(4) ≠ 0), a_P (two-term mirror) and deletions destroy either the
gap c_N = 0 on [2,μ) or the Poisson mirror that closes the loop. Bold reading: the sign is the *index-4 truncation defect of
the Möbius–Poisson loop*, and the missing object is a positive functional on mollifier defects ζM_μ − 1 that sees the gap
[2,μ) — honestly, no such functional is known, and every construction in this slice that approached it (GG, II, MM, AA)
returned the window form.
