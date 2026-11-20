# Dossier on the near-coincidence term (Near_M)

Gathers in one place what the corpus knows and what it attempted on the term
`Near_M(m,k) = ½ Σ_{n≥2, kn≠m} v_n c_0(log(kn/m))` of `𝔸_M = Arch_M − Div_M − Near_M` (Paper 47, prop:AM).
It is a reading compilation: it contains no new results and the labels are those of each source.

Limits: several memos were read only in the passages naming the term (phases 199, 200 and part of 211);
CA_K_002, INV_V_002, INV_G_001, phase 190 and L2_BUILD_020/023 enter Part C only through the rows of the master
index. Nothing was re-derived.

Contents: Part A, exact facts. Part B, attempts of phases 191–204. Part C, attempts of phases 161,
162, 188, 211 and 212, with the coordinate dictionary.

---

# Part A — Facts

## Dossier: the term Near_M of 𝔸_M

P47 = `04-papers/47-row-d-dual-certificates/main.tex`. Memo paths relative to `03-research/`.
Where a source reasons from the zeros side it is marked [H].

## 1. Exact definitions

- **Profile** (P47 §subsec:oneprofile, l.7759–7771): a>0, |b|>½, g(t)=e^{bt}1_{[0,a]}(t), c_g=g*g̃, G₀:=c_g*c_g, T₀:=2a,
  F₀:=(¼−∂²)G₀ ∈ 𝒫_{T₀}; F̂₀(τ)=(τ²+¼)|ĝ(τ)|⁴>0; **c₀ := c_{F₀}** (autocorrelation), ĉ₀=F̂₀². Support of c₀: [−2T₀,2T₀].
  Double zero of ĉ₀ at ±i/2 ⇒ ∫c₀e^{±u/2}=0 and ∫u c₀e^{u/2}=0 (lem:transl(iii); NT_004 Thm 4.2; EI_002 Thm 3(i)).
- **Phase-shift function** 𝖡(d)=𝔞(F₀,V_dF₀)=(1/2π)∫m F̂₀² cos(τd)dτ − ½Σ_{n≥2}v_n[c₀(log n−d)+c₀(log n+d)] (l.7769).
- **𝔸_M** := [𝖡(log m − log k)]_{m,k≤M} (prop:AM, l.7813, hypothesis 2T₀<log 2).
- **prop:AM(iii)** (l.7818–7826): 𝔸_M = Arch_M − Div_M − Near_M,
  Arch_M(m,k)=(1/2π)∫mF̂₀²cos(τ log(m/k))dτ; Div_M=½(𝕍_M+𝕍_Mᵀ), (𝕍_M)_{mk}=v_{m/k} if k|m, k<m;
  **Near_M(m,k)=½ Σ_{n≥2, kn≠m} v_n c₀(log(kn/m))** (m>k), v_n=2Λ(n)n^{−½};
  "smoothed sum of Λ(n)n^{−½} over n≠m/k in the multiplicative interval (m/k·e^{−2T₀}, m/k·e^{2T₀})". Diagonals of Div and Near are zero.
- **Relation with Ξ**: Ξ_{F₀}(D):=Σ_{n≥2}v_n c₀(log n − D)=2∫_{[1,∞)}y^{−½}c₀(log y−D)d(ψ(y)−y) (thm:band, l.7712; main term
  cancelled by Tate). **(Div_M+Near_M)_{mk}=½Ξ_{F₀}(log(m/k)) for m>k** (l.7826). Equivalent: Near_M(s)=Σ s_ms_k[Ξ_{F₀}(log(m/k)) − 1_{k|m}v_{m/k}c₀(0)]
  (N_BUILD_021 Prop 1, PROVED).
- **Spectral form** prop:AM(ii) (l.7816): sᵀ𝔸_Ms=(1/2π)∫F̂₀²|P_s|²[m(τ) − Σ_{2≤n<Me^{2T₀}}v_n cos(τ log n)]dτ, P_s=Σs_m m^{iτ}.

## 2. Facts about Near

**Structure**
1. Decomposition and Toeplitz-in-log form: Div+Near is the sample at {log m − log k} of the one-variable function ½Ξ_{F₀}; Near = that sample minus the exact coincidences n=m/k. PROVED (P47 prop:AM(iii), l.7818–7826; (S) l.10712–10717).
2. Support: for m>k, only n with |log(kn/m)|<2T₀, n≠m/k contribute; the term c₀(log n + log(m/k)) vanishes because log n ≥ log 2 > 2T₀. PROVED (prop:AM, proof of (iii), l.7834–7836).
3. Inevitability: with F₀ fixed, there are near-coincidences for every large M (gaps of log m ~1/m < 2T₀). PROVED/asserted (P47 l.7842–7843; L2_BUILD_028 §2(b)).
4. Form by additive shift h=m−kn: sᵀW₁Vs=Σ_hΣ_{m−kn=h}s_ms_kv_nc₀(−log(1−h/m)); h=0 ↔ Div, h≠0 ↔ Near; |h|≤(e^{2T₀}−1)m. PROVED (L2_BUILD_030 §1(c)). Note: the sentence "bounded number of h ∈[−c,c]" holds only in the regime 2T₀=c/M, not with fixed T₀ (see §4).
5. Near has no sign of its own: it is the finite-resolution remainder of the product |P_s|²·V(τ); W₁=[c₀(log m/k)]⪰0, V triangular, W₁V without sign. PROVED (L2_BUILD_030 §2).
6. Arithmetic side: for fixed (m,k), Near is a smoothed count of primes in a multiplicative interval of fixed relative width e^{±2T₀} (not additively short), minus n=m/k. PROVED (N_BUILD_021 Prop 1).
7. Duality: Poisson on ℤ² of the atom-n sum returns dual near-coincidences −ℓ₂≈ℓ₁n (precision e^{±2T₀}); Poisson on ℤ² maps (S) to itself, does not diagonalize Near nor separate it from Arch. PROVED (phase-192 EI_002 Thm 3(ii), l.60–63).
8. Bohr: on the torus with independent phases only Div is diagonal; Near and Arch live on the diagonal θ_p=θ log p; multiplicativity does not diagonalize 𝔸_M. NO-GO PROVED (L2_BUILD_028 §2(c); N_BUILD_022 §4).
9. Height metric: near-coincidence = r=m/k close to n with large height, defect h−ℓ=2 log den; the "damping by denominator" equals 1 on Div and suppresses Near. PROVED (phase-189 NT_001 Prop 2.1 and reading, l.45–59). Count: #{a≠nb: |log(a/nb)|≤2T₀} ≤ 2nb(e^{2T₀}−1) (NT_001_004_REVIEW l.32, CONFIRMED; requires T₀≤T_abs).

**Where it is invisible and where it is seen**
10. prop:nearfree (P47 l.7642–7669): on resonators F_b of width ε_M=1/(8KM(2+log M)) and T≥½log M+ε_M, 𝔞_T(F_b) ≥ c₀‖F_b‖² (here c₀ is a constant, not the autocorrelation). PROVED. There are no near-coincidences there: the comb is only 𝔻 (divisibility), Schur bound ≤ (log M+E)‖F_b‖² via Σ_{d|m}Λ(d)=log m; the archimedean part gives log(1/ε). Note: it uses a profile of width ~1/M, not a fixed F₀.
11. rem:boxes (l.7660–7669): in multiplicative boxes 𝔻 is a Kronecker sum of single-prime Toeplitz matrices, symbol 2log p·Re x/(1−x), range [−2log p/(√p+1), 2log p/(√p−1)]. PROVED. "Tests without visible near-coincidences carry no information on the sign beyond that": barrier.
12. Near-free multiplicative sets (2T₀<e^{−2L}/2): Near=0, 𝔸|_S = a₀I − ⊕D_i + E; ζ passes trivially because the separation buys energy ≈2L. PROVED (§1–2), a₀≈log(1/T₀) ARGUED (L2_BUILD_029 §§1–3). Verdict: the sign must involve Near.
13. Test m^{−½} with non-overlapping resolution (ε=θ/M): Near=0, Q(M)=(γ+C_χ+log(1/θ))log M+o(log M). Mertens CITED, archimedean asymptotics ARGUED (L2_BUILD_028 §3).
14. Vectors that see Near: positivity must be decided on them (P47 l.7842–7844; rem:bar-arith l.8532–8536: not excluded "𝖡 PD on vectors that see Near_M"). OPEN.
15. Twisted vectors s_m=χ(m)u_m: Div → convolution by χ(n)v_n, Arch remains that of ζ, Near carries phases χ(m)χ̄(k) with m≠kn (not χ(n)): hybrid, not the form of L(s,χ). PROVED (N_BUILD_021 Prop 3; P47 l.8394–8398). Statistics of progressions enter only via Near correlated with residue classes.
16. Progression classes (SW, BV, BDH, Brun–Titchmarsh) as class properties: closed under finite deletion/amplification ⇒ they do not prove (N_BUILD_021 Thm 2, PROVED; P47 prop:prog).
17. Restricted subspaces (R_Q rough, B_Q residue balance): equivalent to the full target, not weaker (L2_BUILD_031 Thm E, PROVED). The suppression of components p^b≤Q of §3–§4 is CORRECTED as invalid (notice at the start of the memo: counterexample M=Q=2, s=(1,1)).

**Exact identities that touch it / that do not reach it**
18. Divisor identity Δ=Z⁻¹LZ−L (ZΔ=[L,Z], matrix 1*Λ=log); spectrum of Δ+L = {log m}. PROVED (= R162_903 B2.1). Normalization: Div_M = 2D_sym (correction recorded in the memo). (N_BUILD_022 §§1–2.)
19. **NO-GO**: X_M=[Ξ(log m−log k)] = Z⁻¹Ł_M + 𝒟_M, with 𝒟_M = non-divisor contribution = Near; 𝒟_M=0 iff Near=0. No exact matrix identity derived from 1*Λ=log relates X_M with L and Δ beyond the divisor part. NO-GO PROVED; exact index of 𝒟_M ARGUED (N_BUILD_022 §3 and self-review 4).
20. Central collapse (NT_004 Thm 4.1, PROVED/CONFIRMED): on Euler tests s_a=χ(a)a^{−½}, the sum in b is complete (b≤j/2<N) and the form is exact with near-coincidences preserved: comb = 2Re ΣΣ χ(a)χ̄(j)(aj)^{−½}g_χ(j)c₀(log a−log j), g_χ=(Λχ)*1. Multiplicative near-coincidences → additive (j=bn≈a); Prop 4.4: correlations χ(a)χ̄(a+h)g_χ(a+h), |h|≤2.5T₀a (identity PROVED, reading ARGUED; requires T₀≤T_abs).
21. χ=1: comb part (Div+Near) bounded O(1) uniformly in N (Tate double zero + Euler–Maclaurin). PROVED (NT_004 Thm 4.2). 𝔞(G_N^1)=c_A N+O(√N), c_A>0 "PROVED up to routine bookkeeping" (Thm 4.3; Titchmarsh 4.11 CITED). NO-GO 4.5 as a sign carrier.
22. Lattice balance identity (C3): for s=m^{−½}, sᵀ(Div+Near)s = 2Σ_N N^{−½} log N·E_M(N), E_M(N)=Σ_{m≤M}m^{−½}c₀(log(N/m)). PROVED (elementary, class W7: linear use of Λ*1=log, without sign); checked to 12 digits (1.985815103517, M=800). Decay of E_M(N): ARGUED (Euler–Maclaurin). (phase-190 EXP_003 §4, EXP_005 C3.)
23. Family s_w=m^{−½}w(m/M) (P47 prop:shape-family, l.9008–9045, (i)–(iii) PROVED, growth of ζ CITED): collapse sᵀ𝔸s = sᵀArch s − Σ_{N<Me^{2T₀}}N^{−½}D_w(N)E_w(N); the comb enters only via Σ_{d|N}Λ(d)=log N and Λ(d), d<e^{2T₀}/η. (iv): Ψ_w is the continuous analogue of atom n of Div+Near; it vanishes to second order, ∫Ψ_w=0. EI_002 Thm 3(iii): "Div ≈ −Near" PROVED as an identity; remaining: boundary term (scale M), small-divisor defects and dual terms.
24. Variant EI_003 Thm 2 "no identity makes the symbol nonlinear in Λ": REJECTED by the review as a tautology (σ_T is affine in Λ by definition) (PHASE_192_REVIEW_SUMMARY l.17, 33; EI_003_REVIEW l.6, 16).

**Controls** (phase-190, NUMERICAL, double precision, T₀∈{0.05,0.15,0.3}, b=1)
25. Λ: 𝔸_M ⪰ 0 for every M≤3000 computed; λ_min = M^{−3+o(1)} (local exponent 2.89→2.98). (EXP_003 §1, Fact N1.)
26. Deletion a₃, a₅: indefinite already at M=50 (λ_min −1.5, −2.4) and growing ~ −M (−42, −54 at M=1500). (EXP_002 §1.)
27. Perturbed weight v₂(1±10⁻⁵): indefinite from M≈200–400; ±10⁻²: from M=50. Amplification threshold c*(M) ≍ λ_min/0.18 ≍ M^{−3}; ∂λ_min/∂v₂ = O(1). (EXP_002 §§1–2.)
28. Beurling (q=p e^{ε_p}, ε_p∈±0.02): indefinite at M=50 (−1.5) on the integer lattice and on its own. Poisson: −3…−237. (EXP_002 §1.)
29. Failure of the controls: eigenvector = smooth packet of consecutive integers at the upper scale (peak ≈0.15–0.25M); Div≈0, Near ≈ Arch + |λ| ("Near exceeds Arch"). E.g. pert₂(+10⁻⁵), M=1500: Arch 120.12, Div 0.60, Near 119.52, λ=−7.9·10⁻⁴. Near_n at M=800: n=2 +41.9, 3 +27.9, 4 +10.5, 5 −14.1. (EXP_002 §§3–4.)
30. 2×2 band (necessary): kills Poisson, Beurling (T₀=0.3), a₅; a₃, amp2(0.05), pert₂(1.01) pass it up to d=15 while being indefinite. Λ: sup|𝖡|/a₀ = 0.942 at d=12.69 (T₀=0.3). (EXP_002 §5.)

**Numerical data on Near for Λ** (NUMERICAL)
31. At the minimizer (≈ m^{−½}·w(m/M), overlap 0.993, positive entries): Div(v)≈log M+0.4, Near(v)≈−Div(v)+Arch(v)−λ; e.g. M=800: Arch 0.322, Div 6.032, Near −5.709. (EXP_003 §3; EXP_005 §5.)
32. Per atom (M=800): every n≥5 cancels its divisor part to 3 decimals; defects δ_n=Near_n+Div_n: n=2 +0.169, 3 +0.120, 4 +0.027; Σδ_n = Arch−λ. Mechanism (Riemann sum of an integral cancelled by Tate) PROVED-elementary, not specific to ζ. E_M(2,3,4)=0.778, 0.636, 0.287; |E_M(N)|≤2·10⁻⁶ for 50≤N≤400. (EXP_003 §4.)
33. Matrix: ‖Near‖_op ≈ 0.17M (T₀=0.3), 0.087M (0.15); indefinite, full rank; eigenvalues −517…+312 (M=3000); 56.5 % of entries positive; Σ entries −2786 vs Σ|·| 4.5·10⁵ (M=2000); mass ∝ Λ(n)n^{−3/2}M², n=2,3,5 carry 45 %; principal eigenvectors orthogonal (≤2.7·10⁻⁴) to the negative space of Arch. All these statistics agree to 5 digits with the 10⁻⁵ perturbations ⇒ not specific. (EXP_003 §5; EXP_005 R11.)
34. Mass per shift h flat (h=±1: 4.61, ±2: 3.90, ±3: 3.42) for Λ and controls: h does not separate. (EXP_003 §4; EXP_002 §4.)
35. Mechanism of the minimizer: P_v vanishes at the ordinates [H] (EXP_003 Fact N2; EXP_005 C2) — classified by the source as an observation from the zeros side, not an input from the primes side.
36. Conclusion of the source: no structural fact on the primes side about Near holds for Λ and fails for all the controls (EXP_005 §0; README phase-190).

## 3. Explicit open questions
- (S): Arch_M − Div_M − Near_M ⪰ 0 ∀M (P47 l.10707–10717). OPEN.
- Joint control of Near with Arch on vectors that see near-coincidences (rem:bar-arith l.8532–8536; EXP_005 §4 note R9). OPEN.
- C1 criticality law λ_min=M^{−3+o(1)}; C2 law of the minimizer (NUMERICAL; route only [H]). (EXP_005 §2.)
- Boundary term of Q_M(w) at N≈M: size of the PNT error or of the margin M^{−3}? Next step proposed, not done (EXP_005 §6; EI_002 Thm 3(iii)(a) "not estimated here").
- Row 18 of the map (conductor >1) as a source of a falsifier: UNKNOWN; other routes not excluded (N_BUILD_021 §3).
- Exact index of 𝒟_M in N_BUILD_022 §3: ARGUED.
- "Balance kills exactly the components q=p^b" beyond first order: ARGUED, and later corrected as invalid (L2_BUILD_031).

## 4. Tensions / contradictions between sources
- L2_BUILD_030 §1(c) "Near is a sum over a bounded number of h∈[−c,c]" assumes 2T₀=c/M; with fixed T₀ (P47 prop:AM) |h|≲2T₀m, unbounded. Not a logical error, but the regime differs from the paper.
- prop:nearfree (P47) treats resonators of width ~1/M, not the fixed profile F₀ of prop:AM; P47 l.7842 cites it as "tests in which Near is invisible".
- N_BUILD_022 §2 D_sym ≠ Div_M (factor 2) — corrected within the memo.
- L2_BUILD_031 §3–§4 (suppression of components p^b≤Q) invalidated by a later notice; Thm E intact.
- EI_003 Thm 2 / README phase-192 ("PROVED impossible") vs review (rejected as tautology).
- NT_002/NT_004 bounds "≤5T₀", "≤2.5T₀" need T₀≤T_abs, not only 2T₀<log 2 (NT_001_004_REVIEW l.70).
- No numerical contradiction detected: 𝔞(G_N^1)=c_A N (NT_004) is compatible with the growing Rayleigh quotient of m^{−½} in EXP_003 §2 (0.06→0.50, M=100→1200).

---

# Part B — Attempts, phases 191–204

## Inventory of attempts on Near_M (phases 191–204)

Object: 𝔸_M = Arch_M − Div_M − Near_M (P47 prop:AM), Near_M(m,k) = ½ Σ_{n≥2, kn≠m} v_n c₀(log(kn/m)).
Labels copied from the source or from its audit. "[H]" indicates that the source reasons from the zeros side or uses an equivalence; that reasoning is not used here.
Scope: the passages of each memo containing Near or near-coincidence were read (grep and context), plus the syntheses and audits. Not all memos of 199/proof-L-sharp and of 200 that only mention Near in passing were read in full. Index: ROUTES-MASTER-INDEX.md l.102, 135, 207–213, 272–310, 4397, 5770–5775, 5833, 5875, 5916, 5922, 7027, 7086, 7162, 8825–8836, 9016–9019, 9093–9119, 9255, 9278.

## Family 1. Exact rewritings (coordinates)

| id / file | operation on Near | result / label | exact reason for failure | what survived |
|---|---|---|---|---|
| CA_C_002 Prop 2(c),(d) (193) | Near_M = (μ_line∘ι⁻¹ − Haar)(Σ_p δ_p·\|P_s\|²) in boxes 𝕋^S | PROVED; review: "coordinate, not mechanism" (CA_C_002 l.90) | Requires every near-coincidence atom to be an S-unit (hypothesis of (c)); the identity is linear in Λ and fixes no sign | Identity "Hasse defect" = Near; vanishes on tests without visible near-coincidences |
| CA_H_002 Thm 3.1/3.2 (193) | Extension to Ĝ: Div = ∫g_s dHaar, Div+Near = ∫g_s dν₀; sᵀ𝔸s = Σ_q[α(log q)N_s(q) − c₀(log q)M_s(q)] | PROVED, REF-D (Cor 3.5) | "anatomy is (additive weight) × (monoid coefficient), linear in Λ, (B″)"; the sign content is (K) = the claim itself | H-K, H-T: the mass of the line beyond the integer Nyquist frequency M is ≍ M⁻³ (PROVED) |
| CA_M_001 Prop 1.1 (193) | Form on prime sites: Q = Arch − Near, Near = Σ_h C_s(h) (Chen correlations p ~ p′q^a, all shifts \|h\| ≲ 2T₀p) | PROVED | Does not encode pairs of primes at fixed shift; only the first moment in h; the sign is not determined | Exact form; Div ≡ 0 on prime sites |
| CA_K_002 Thm 3.2/Cor 3.3 (193) | Independence of sites: target ⟺ Arch(s) ≥ Near(s) ∀ s on prime sites ∀M | PROVED as reformulation; REF-D. Index l.5922 | It is the same inequality; Cor 3.3(iii): under the premise the whole deficit is paid by Near (p ≈ np′) | Clean reduction "Arch ≥ Near" (TRACT_D l.296 takes it as the canonical form of G8) |
| phase 190, identity C3 (index l.5775) | sᵀ(Div+Near)s = 2Σ_N N^{−½}log N·E_M(N) on s = m^{−½} | PROVED (class W7) | the balance occurs only through defects N = 2, 3, 4; atoms n ≥ 5 cancel their Div (Riemann sum common to every comb) | identity |
| INV_V_002 Thm V2.1 (196) | Affine form 𝔄ff_T (shifts 0<\|a\|<e^T(1+1/n)): 𝔞_T = A_∞ + ½𝔄ff − ½Re⟨Vf,f⟩_Ш | PROVED, not diagonal; (G2) REF-D tautological (AUDIT_196 l.53) | 𝔄ff = 2(𝔞_T − A_∞) + Re⟨Vf,f⟩_Ш identically; linear in the comb (Prop V2.2(d)) | Exact split; V2.2(c) FALSE (holds for every lattice αℤ) |
| CA_B_007 / CA_B_008 (193) | Concavity gap Γ = misalignment between the archimedean minimizer and the near-coincidence minimizer | EXCLUDED (REF-D + (B″) + (R)(5)) | Γ is an overlap ⟨h₁,h₂⟩ plus two gaps: window observable (R)(5); the bound Γ ≥ m(1−\|c\|) is sharp only with two low modes, and the arena has ≥ 12 | Thm 1 (angle bound between two minimizers) PROVED as coordinate |
| PROOF_L_SHARP_GG_001 / II_001 (199) | Renormalization: coupling set = near-coincidences nN ≈ N′ (exact); close pairs N′/N ∈ (μ⁻¹, μ) | PROVED (linear identities); without sign | the set of pairs is not finite; the local autocorrelation of g remains (linear identity W_T(g) = …) | radical decomposition of the full line |

## Family 2. Arithmetic of the sites (parity, residues, sieve, singular series)

| id / file | operation | result / label | exact reason | survives |
|---|---|---|---|---|
| CA_M_001 §1.2, Thm 3.1/Cor 3.2, Prop 3.3 (193) | Split Near by parity/residues of p − np′; Chen, HL, sieve | NO (PROVED: "integrality invisible") | Near^{h odd} = Near_{q=2}; each Near_q has trace 0 and is indefinite; the statement ∀M is equivalent to the same with real sites p+θ_p, θ_p ℚ-independent (no difference x − nx′ is an integer); in the decisive configurations h → ∞ and bounded shifts have weight 0 | M-S, M-I, M-P (PROVED) |
| CA_M_000 M4 (193) | Selberg sieve weights / b_θ as bounds for Near | DISCARD (pre-screen) | W-sieve: b_θ ≥ 0, b_θ ≤ Λ refutes every chain of upper bounds (R167_102); NG-A4: a sieve cannot weight Λ from below | — |
| CA_M_000 M5 (193) | Averages of singular series (Gallagher, Montgomery–Soundararajan) to evaluate Near | DISCARD | conjectural input; resolution mismatch: Near sees h at scale T₀p, bounded h have density 0 | — |
| SPEC_SIGN_OBJECT_002 Q3 (200) + AUDIT_200_SPEC_002 | Exact singular series 𝔖_n(h) of N′ = nN + h via Ramanujan sums; Bochner on ℤ | DOUBTFUL tending to NO-GO | 𝔖_1 is PD trivially (mean autocorrelation of any sequence, Herglotz); the weights ∫w_{n,h} come from c_g∗ν with ν of indefinite sign (m < 0 for \|t\| < 6.29, atoms −v_n), so they are not of positive type in h; all the content remains in 𝔈_Poisson at the boundary N ≈ μ (C6); falsifier cΛ, c > 1, leaves 𝔖_n intact | closed formula for 𝔖_n(h) (Lemma Q3.1, true); 𝔖_1(1) = −0.040360 (NUMERICAL) |

## Family 3. Statistics and spectrum of the matrix Near

| id / file | operation | result / label | exact reason | survives |
|---|---|---|---|---|
| phase 190 (index l.5774, 8825–8836) | Statistics and spectrum of Near as a fingerprint | NUMERICAL; NO-GO by [sens] | statistics identical to 5 digits under a 1e−5 perturbation of the comb; the minimizer is the smoothed partial sum [H] | norm ≈ 0.17M, full rank, 56 % of entries positive (NUMERICAL); λ_min(A_M) ≍ M^{−3+o(1)} |
| SPEC_SIGN_OBJECT_007 C1 (200) | Spectrum or components of the near-coincidence graph 𝔐_T at resolution π/T | NO-GO (PROVED, given certified Lemma E) | the support of the falsifier comb of Lemma E contains that of ζ; every monotone invariant of the support that certifies ζ also certifies that form at T ≥ 1.59, where it equals [−0.0599398587, −0.0599398456]. Lemma A.0: Baker is weaker than the separation \|log(m/n)\| ≥ ½e^{−2T} | record "Do not retry: … near-coincidence matrices or spectra" |
| CA_C_006 E1 (193) | Pila–Wilkie / o-minimality: the dangerous pairs lie in a set with small transcendental part | NO-GO as a mechanism | the near-coincidence set is semialgebraic (ARGUED), Pila–Wilkie does not act; upper counting bounds are B′; counts weighted by a positive comb are sign-generic (B″) | — |
| CA_C_006 E2 (193) | Freeness / free probability between Arch and Div+Near | DISCARD | both are compressions of convolution operators on ℚ^×_{>0} and commute (freeness requires τ((a−τa)(b−τb)(a−τa)(b−τb)) = 0, but with commutation it gives τ((a−τa)²(b−τb)²) > 0); moreover, even with freeness, λ_min ≍ M⁻³ has weight O(1/H(M)) in τ_M, and a rank-one perturbation (O5) does not change the limit moments but can make the bottom negative | — |
| AUDIT_201_SPEC_001 B-V1 (201) | Block ε = ±1 = near-coincidence matrix m = kn ± 1 (non-negative rank) | NO-GO CONDITIONAL (branch 2 + C-emb (a)) | the threshold κ_∞ compares v_n with a hand-picked archimedean piece: finite list of comparisons; moreover it repeats the "do not retry" of SPEC_007 | — |

## Family 4. Interpolation / deformation of Near

| id / file | operation | result / label | exact reason | survives |
|---|---|---|---|---|
| CA_K_002 Prop 3.1 (193) (seed K10) | Q_t = Arch − Div − Near∘E_t with Gaussian Schur multiplier e^{−tℓ(q)} (flow from the line to Haar) | NO-GO for deterministic interpolation; REF-D | ∂_tQ_t is additive weight × monoid coefficient, linear in Λ (fails P2); the sign of the path is a statement about the minimizer (Thm 1.2); Cor 3.3(ii): NO-GO PROVED for the Haar endpoint | Prop 2.1: λ_min(𝔸∘K_μ) ≥ λ_min(𝔸), i.e. averaging bounds from above (wrong direction) |
| P211-3B (index l.9776) | 𝔸_M = 𝕏∘𝕂_t + ℝ, gcd Schur multiplier | NO-GO | existence of the decomposition ⟺ 𝔸_M ⪰ 0 (reformulation) | — |

## Family 5. Rewriting as h⁰ / pairs / hyperbola (absorbing Near into another object)

| id / file | operation | result / label | exact reason | survives |
|---|---|---|---|---|
| INV_C_001 (194) | h⁰ off the multiplicative diagonal (coprime pairs a/b) | Thm 4 PROVED; (Q3) REF-D | no measure on log ℚ_{>0} equals 𝔞_T on 𝒫_T, so the identity holds only in the limit, and that limit is Arch − Near; "h⁰_off ≥ h⁰_diag in the limit" is W ≥ 0 reformulated; the Farey rate is irrelevant because the limit is needed, not the rate | Lemmas 1–3, Thm 4, Identity 5 |
| INV_B_002 (194) | Effectiveness of h⁰ at the place of the near-coincidences | OPEN, ill-posed (AUDIT_194 l.43) | removing the pairs with prime-power ratio destroys the Gram structure; the finite intersection part is ≤ 0 for effective F (PROVED) | — |
| INV_G_001 Thm G1 (194) | Balance term Σ min(d,n/d); PD kernel e^{−\|u\|/2} | NO-GO in class 𝓒_G, CONDITIONAL on the Beurling check (AUDIT_194_2) | every ingredient is Beurling-generic (B″); the positive part ∫F e^{−\|u\|/2} = Near; "Arch_T − Near-comb ≥ 0" is 𝔞_T ≥ 0 | D_M = Σ_k ζ_{≥k}(s)² (identity PROVED) |
| INV_D_001 (194), TRACT_D l.391 | renormalized defect − comb ≥ 0 | TRANSFER | ‖ω_+‖²_HS ≥ 0 does not see the comb | — |
| INV_J_001 (194), Cor J4 | FE coupling = Near | first half PROVED; "= Near ⇒ REF-D" ARGUED | J2: Gram/Bochner gives the wrong direction; MV/sieve give only upper bounds | — |

## Family 6. Transfer / identity from Λ∗1 = log

| id / file | operation | result / label | exact reason | survives |
|---|---|---|---|---|
| N_BUILD_022 (188), cited in INV_I_001 and SPEC_B | Exact matrix identity from 1∗Λ = log beyond the divisors | NO-GO (06_OPEN_RESIDUES) | ZΔ = [L,Z] exact; Near appears as a **discretization defect** | commutator identity |
| INV_V_002 Thm V2.3/V2.4 (196) | Hecke–Chebyshev transfer V*Ш = 2log\|x\|·Ш to lift to a positive Hermitian kernel | V2.4 PROVED (rigidity); NO-GO | Chebyshev is a statement about a single vector (Ш); every Hermitian lattice kernel admitting the exact transfer is constant in the transferred variable; (G1) "approximate eigen-kernels" falls into N_018 ∪ I4 (ARGUED) | the specific relation of Λ lives only in the rank-one distribution Ш |
| L2_BUILD_030 (188), dead row R9 | Near as a separately signed operator | NO-GO (dead row R9) | — (cited in SPEC_B l.160 as input, not taken up here) | — |
| SPEC_B T*₃ / C*₃ (191) | Divisor collapse D_w(N) = 2c log N − defects; Poisson on ℤ: near-coincidences = nonzero dual frequencies | C*₃ OPEN; REF-D for η ≤ η₀ ≈ 0.3–0.4 (NUMERICAL); for η > η₀ it is a necessary condition | the comb survives only at n < e^{2T₀}/η; for η → 0, ψ − y re-enters through the divisor defects at scale M and is useless at precision M⁻³; T*₃ is NUMERICAL-false for finite modifications | "EXP_005 §6 names the bulk/edge split of Q_M(w) as the next step and it has not been done" |
| SPEC_A (191) | Exact induction by contacts | O6 ARGUED / (θ) FAIL | "no line of the specification uses that the lags are log ℕ": near-coincidences appear as data, unspecified | — |
| P211-A (index l.7312) | Mean of the near-coincidences along s_w: Q_M = M·𝒜(w) + small | NO-GO (lattice→continuum transfer); decomposition PROVED | — | superpolynomially small boundary |

## Family 7. Domination Arch ≥ Near (direct bound)

| id / file | operation | result / label | exact reason | survives |
|---|---|---|---|---|
| TRACT_D G8 (204), WEAKEN_001 l.78, FINAL_204 #40 | Schoenberg/Bochner on sites; term-by-term domination | TRANSFER; "OPEN with no sign (not weakened, just separated)" | "Missing hypothesis: the inequality itself"; term-by-term domination is excluded by thm:band/Thm T/Thm L: each 2×2 section is the band \|Ξ(d)\| ≤ 2a₀ and Ξ oscillates around 0 (no term-by-term sign) | residues l.391/415 "attackable without a sign" |
| CA_M_001 Prop 4.3 (193) | What the near-coincidences must pay on prime sites (Fejér) | ARGUED; necessary under the premise; REF-D | Cesàro condition on Ξ, in class Thm Z [H] | — |
| CA_M M-R (193) | Antidiamagnetic inversion | PROVED (FE-generic identity) | m(τ) + 2Re(ζ′/ζ)(½+iτ) ≡ 0: the primes cancel C₀ with zero slack; what carries positivity is not an a.c. density [H] | — |

## (a) Reasons for failure grouped

1. **Linearity in Λ / comb genericity (B″, O7).** CA_C_002, CA_H_002, CA_M parity, CA_K_002, INV_G, INV_V_002 V2.2(d), CA_C_006 E1, phase 190 C3. Every exact identity for Near is (additive weight in log q) × (monoid coefficient), linear in Λ, and holds equally for Beurling, cΛ and a_P.
2. **Reformulation (REF-D).** Any closed form "Arch ≥ Near" (CA_K_002, INV_C Q3, INV_G, INV_V G2, P211-3B, TRACT_D G8) is the same inequality.
3. **Invisible integrality (independence of sites).** CA_M Thm 3.1/Cor 3.2 and Prop 3.3: parity, residues, sieve and singular series do not exist in the decisive class (h → ∞).
4. **Dependence only on the support or on the statistics ([sens], Lemma E falsifier, O5 rank one).** Phase 190, SPEC_007 C1, CA_C_006 E2.
5. **Wrong direction (Gram/Bochner/averages give upper bounds for λ_min).** CA_K_002 Prop 2.1, INV_J J2, Q3 (weights not of positive type).
6. **Chebyshev rank one (no Hermitian lift).** INV_V_002 V2.4 and N_022 (Near = discretization defect).
7. **Window observable (R)(5) / precision M⁻³.** CA_B_008, CA_C_006 [crit], SPEC_B (ψ − y useless at M⁻³).

Genuinely distinct: about 4. Reasons 1, 2 and 5 are the same obstruction: a linear identity or a Bochner bound does not fix the sign, and closing the inequality reformulates it. Reason 3 (real sites) is independent. Reason 4 reduces to 1 via falsifiers. Reason 6 is structural and distinct. Reason 7 is the M⁻³ scale of the bottom and is also distinct.

## (b) Operations the sources point out as not executed

- **Bulk/edge split of Q_M(w)** (SPEC_B l.160–161: "EXP_005 §6 names the bulk/edge split … has not been done"). The Euler–Maclaurin/Poisson bookkeeping of the main term is not written either (SPEC_B table: "not written out; ARGUED").
- **Proof of 𝓕_T ≤ 𝔞^♯ with the vector and the archimedean form together on vectors that see Near_M** (P47 rem:bar-arith; index B.3 #38, "terrain declared not excluded").
- **Hadamard/Schur positivity coupling distinct primes with m ≈ kn; non-Gram positive block with its own source** (index B.3 #30, no written object).
- **Joint restriction between primes (requires a new identity)** and **Hecke-type algebra with archimedean multipliers** (index B.2 #28, "no candidate").
- **Term of degree ≥ 2 in the weight vanishing at Λ; W supported on m ≈ kn; closure of {𝔸_M} under Schur with transformed weight** (index B.2 #27).
- **Approximate Chebyshev eigen-kernels with a non-Cauchy–Schwarz bound on 𝔄ff** (INV_V_002 §3 (G1); AUDIT_196: "not worth pursuing unless a concrete non-CS bound on 𝔄ff is named").
- **Residues l.391/415 of G8 "attackable without a sign"** (WEAKEN_001, TRACT_D): separated, not attacked.
- **Asymmetry test 𝔖_2(h) vs 𝔖_2(−h)** (AUDIT_200_SPEC_002: "cheap and worth running as data, not as a route").
- **OS-type reflection across log m ≈ log(kn)** (LEDGER_L1 l.99, l.144): proposed as a candidate, with the difference from INV_V_002 pending.

## (c) Partial positive results on Near

- **prop:nearfree / rem:boxes (P47, PROVED; index l.135):** positivity with margin c₀ for every b in the resonator profile ε ≍ 1/M. There the near-coincidences are invisible and Near does not contribute.
- **CA_C_002 (d):** on tests without visible near-coincidences the Hasse defect vanishes and positivity holds with margin.
- **Small windows:** with 2T₀ < log 2 and T₀ ≤ 0.3, D is already Theorem A (TRACT_D: "l.55/135 … already Theorem A"). On prime sites Div ≡ 0, but the result does not sign Near by itself.
- **Scale:** the mass of the Kronecker line beyond frequency M is ≍ M⁻³ (H-T, PROVED), equal to the order of λ_min (NUMERICAL).
- **Identity C3:** the balance against Arch depends only on the defects N = 2, 3, 4; atoms n ≥ 5 cancel their Div (PROVED, class W7).
- **SPEC_B C*₃:** for η > η₀ it is a necessary condition (does not close); for η ≤ η₀ it is REF-D.
- **P211-A:** the boundary of the near-coincidence mean is superpolynomially small (PROVED).
- No family of vectors was found that sees Near_M ≠ 0 and where Near is signed or dominated by Arch with proof.

---

# Part C — Attempts, phases 161, 162, 188, 211, 212

## Inventory of attempts on Near_M (near-coincidences m≈kn, m≠kn) and their equivalents

Reading, no construction. Convention: labels copied from the source. "[H]" marks steps of a source that
reason via zeros / functional equation ξ / forbidden equivalences; they are recorded only as what the source says.
"Read" = memo opened; "via index" = only the row of the master index (the primary source was not opened).

Object: 𝔸_M = Arch_M − Div_M − Near_M (P47 prop:AM), Near_M(m,k) = ½Σ_{n≥2, kn≠m} v_n c_0(log(kn/m)),
v_n = 2Λ(n)/√n; (Div+Near)_{mk} = ½Ξ_{F_0}(log(m/k)), Ξ_{F_0}(d) = Σ_n v_n c_0(log n − d) (211 DOSSIER_001 §1.4).
Problem (S) / R9 of the index: Arch_M − Div_M − Near_M ⪰ 0 ∀M, status **OPEN** (index l.12940–12960, l.4397).

---

## 1. Table by method family

### F1. Separating Near as an operator of its own / supports without Near (phase 188, cited by 211 and 212)

| id / file | coordinates and name | operation | result and label | exact reason for failure | what survived |
|---|---|---|---|---|---|
| L2_BUILD_029 (188; read) | integers; "Near-free sets" | restrict to S = {Πp_i^{k_i}} with 2T₀ < e^{−2L}/2 so that Near ≡ 0 | PROVED (structure); trivial test | separating requires resolution: a₀ ≈ log(1/T₀) ≈ 2L dominates Σ 2log p/(√p−1); it holds "for local reasons", without global input; amplification fails only with c ≳ a₀ | A|_S = a₀I − ⊕_i D_i + E (Kronecker sum of local Toeplitz matrices); conclusion of the source: "the sign cannot live on sets without Near" |
| L2_BUILD_030 (188; read) | integers / Dirichlet: sᵀW_1Vs; additive shift h = m − kn (h=0 Div, h≠0 Near) | write Near as a sum of shifted convolutions Σ_{m−kn=h}; Ramanujan expansion 1_{n\|j} = n^{-1}Σ_{q\|n}c_q(j) | identities PROVED; §2 "Near is not an operator with its own sign" PROVED; passage to smooth S ARGUED | W_1V has no sign (symmetric part = multiplier Re V(τ), indefinite); Near is "the finite-resolution remainder of the same product \|P_s\|²V" | Q = (form m^♯) − ⟨Chebyshev fluctuation q=1⟩ − Σ_{p^b}⟨components c_{p^b}(j)⟩, exact in the analytic pairing |
| L2_BUILD_031 (188; header read) | integers; residue-balanced vectors (R_Q),(B_Q) | annihilate components c_{p^b}, p^b ≤ Q | Theorem E PROVED: (B_Q) ⟺ D; §3–4 **corrected** (CORRECTION_RESIDUE_BALANCE_031: M=Q=2, s=(1,1), component q2 = v2/2 > 0) | the restriction does not weaken the target; the suppression of §3 was invalid | Theorem E intact |
| N_BUILD_021 (188; read §§1–3) | integers; Near = Ξ-kernel minus exact ones; on primes: shifted correlations | use statistics of progressions (SW, BV, BDH, Titchmarsh, Brun–Titchmarsh) as class properties; vectors twisted by χ | Prop 1, Thm 2, Prop 3 PROVED; class 𝒞_prog NO-GO | Thm 2: every class defined by o(x) errors is closed under finite deletion/amplification ⇒ contains falsifiers (finmod/void); Prop 3: with χ, Near carries phases χ(m)χ̄(k) ≠ χ(n) (hybrid form) | conductor >1 routes other than the two excluded ones: not excluded |
| N_BUILD_022 (188; read §§1–3) | matrices Z, Δ, L; X_M = [Ξ(log m − log k)] | exact identity ZΔ = [L,Z] (1∗Λ=log) and attempt to reach X_M | §1 PROVED (= R162_903 B2.1); §3 **NO-GO PROVED** | X_M = Z⁻¹Ł_M + 𝒟_M; 𝒟_M (non-divisors, a ≈ m/(kb)) vanishes iff Near = 0: "Near is a discretization defect"; the identity only controls exact divisibility | Bohr symbol: with independent phases θ_p only Div is diagonal; Near and Arch live on the diagonal θ_p = θ log p |

### F2. Mean of Near along smooth Dirichlet polynomials (211)

| id | coordinates | operation | result | exact reason | survived |
|---|---|---|---|---|---|
| 211 ROUND_001_A (read) / LEDGER C1 | spectral: Q_M(s) = (1/2π)∫F̂₀²\|P_s\|² s_N dτ, family s_w = m^{−½}w(m/M) | Poisson summation on ℤ; resum Div+Near | decomposition PROVED; Q_M = M·𝒜(w) + 𝒵_N + ℛ_M; ℛ_M = O(M^{−3+ε}) ARGUED; **NO-GO** (lattice→continuum transfer). Steps (0.2) and (c) use ζ/ζ′ and the functional equation [H] | in the smooth family, Q_M ≥ 0 ⟺ (up to O(M^{−3})) 𝒜(w) ≥ 0, i.e. the continuous window form at T′ = (L+2T₀)/2: reformulation, not sign. "Div and Near are lattice bookkeeping that Poisson resums" | boundary term 𝒳_M = O(M^{−K}) ∀K (PROVED); ARGUED conjecture: the exponent −3 of λ_min is regularity of the profile, not margin |
| phase 190 (via index l.8825–8840) | integers, M ≤ 3000 | numerical experiment on Near | NUMERICAL; NO-GO by [sens] | Near statistics (norm ≈0.17M, full rank, 56% positive, flat in h) identical to 5 digits under a 1e−5 perturbation of v₂: not specific | Identity C3 PROVED (class W7): sᵀ(Div+Near)s = 2Σ_N N^{−½}log N·E_M(N); balance only through defects N=2,3,4 |

### F3. Schur / multipliers / factorizations on 𝔸_M

| id | coordinates | operation | result | exact reason | survived |
|---|---|---|---|---|---|
| 211 ROUND_003_B (read) | integers; metrics ρ = \|log m − log k\| and δ = log(lcm/gcd); Near = pairs ρ<δ | 𝔸_M = 𝕏∘𝕂_t + ℝ, 𝕂_t = [(gcd²/mk)^t] | Prop 1 (restatement) PROVED; Thm 3, Thm 4 NO-GO PROVED (Thm 4 corrected in STATE_001: "Near^comb ≠ 0 for some M") | Lemma 2: \|𝔸−ℝ\|_{mk} ≤ βe^{−tδ}; on pairs m≈kn (δ large) ℝ must reproduce 𝔸: "the multiplier never sees the near-coincidences". Thm 4: with the Div/Near prescription, ℝ = −Near^comb has zero diagonal ⇒ not PSD | t*_M = inf{t: 𝔸∘𝕂_t ⪰ 0}; 𝔸 ⪰ 0 ⟺ t*_M = 0 (reformulation) |
| 212 ROUND_003_7 (read) | integers; divisor incidence | 𝔸_M = WᵀDW, W supported on d\|k | Lemma 1 format NO-GO PROVED; Lemma 2 PROVED; Cor 3 PROVED; selection: **repetition** | divisor incidence does not see coprime nearly proportional pairs; on primes WᵀDW = D₁wwᵀ + diag (rank one + diagonal), and the restriction to primes is already equivalent to the target (CA_K_002 Thm. 3.2): the whole sign remains in ρ | "a W not supported on divisibility that sees m≈kn, with its own formula and ρ with manifest sign, is missing. I do not know how to write it" |
| 212 ROUND_004_D (read §§2–3) | integers; near-divisibility support | factor 𝔸_M with support on m≈kn; look for classes closed under Schur complement | Lemmas A, B PROVED; Lemma C format NO-GO PROVED; selection does not pass | Lemma B: near-divisibility is not a partial order; its support is a threshold semiorder independent of the weight. Lemma C: 𝖡 < 0 on (θ₀, log2−θ₀), not the Laplace transform of a measure ⇒ 𝔸_M is not in TP/sign-regular, tree Green, f(gcd) | "The arithmetic information is in the VALUES of the entries of Near, not in their pattern" |
| 212 ROUND_022_A (read part 2) | Möbius congruence 𝔹_M = ZᵀArch Z − [...] − ZᵀNear Z | integer unitriangular congruence | repetition / class NO-GO recorded | cancels only the divisibility part; ZᵀNear_M Z remains without identity (N_BUILD_022 §3) | — |
| 212 ROUND_001_B (read §6) | multiplicative chains | Schur pivots along nestings | no new mechanism (repetition of C6) | Prop 5: at points αℕ+βℕ irrational Div=0 and the whole comb is Near; the multiplicative structure does not change pivots; in boxes without Near a Kronecker sum, not a product | — |
| R162_903 (read) | algebra 𝒜_T = {M_T(α)}, Gram of Möbius images | integer Gram, terminating BCH, Sylvester/Moore, tensor lift | 8 statements PROVED; route **NO-GO** | Prop 2.1: the floors ⌊y/u⌋ exist only pointwise; in L² they give a linear hyperbola/sawtooth (comb (PC)); Thm 4.1–4.2: continuous invariants collapse to (sig,det); Λχ₂ and Beurling pass all lines | refined residue: a DISCONTINUOUS functional of F that distinguishes integers from generalized integers and 1 from χ₂ is needed |

### F4. Theta / Gaussian Gram: resonant part kn² = lm² vs. non-resonant (211 POWER_GRAM_SLICES §§16–17, POWER_GLOBAL)

| id | coordinates | operation | result | exact reason | survived |
|---|---|---|---|---|---|
| GRAM §16.1–16.4 (read) | theta: A(z_k, z̄_l), z_k = ½log k + iy; modes n,m with phase kn² − lm²; near resonances = kn² ≠ lm² | asymptotic equivalent ε = cos2y → 0 | (INT-ASYM) PROVED; (NEAR) S_δ ≤ C_{k,l}δ^{−4}log(2+1/δ) PROVED; (OFF) PROVED | uniformity only for a FIXED list of integers; constants depend on k,l | main term [105/(512√2)]ρ(k,l), ρ = gcd(a,b)/√(ab) in the squarefree class; fixed complex blocks positive definite for small ε |
| GRAM §16.5 (read) | same, k, l = k+1 | compare with ρ after normalizing the diagonal | PROVED (negative) | \|C_y(k,k+1)\| → 1 while ρ(k,k+1) = 0: there is no C_y ≥ c_yρ nor uniform approximation | — |
| GRAM §17–17.5 (read) | theta; R_res = pairs kn² = lm²; Off = A − R_res (the non-resonant part, includes the theta tail) | SOS by change of scale u = λt and Λ∗1 = log (RES-SOS) | PROVED: R_res positive definite at all orders; R_res ≥ c_*E_y (UNIF-D) | "The sign of the contribution kn² ≠ lm² is NOT proved" | (RES-SOS), D_q > 0, explicit c_* |
| GRAM §17.6 (read) | theta, y=0 included | bound Off by E_y or by a fraction of R_res | PROVED (negative; RULES_AVOID D9) | pairs k,k+1: Off_y[c^{(k)}] = −log k + o(1) with E_y = 1; A_y[c]/R_res[c] → 0: there is no Off ≥ −C E_y nor A ≥ δR_res | "at y=0 Off ≥ −R_res is exactly A_0 ⪰ 0 on integers: the full target, without margin" |
| GLOBAL "resonant budget" (read) | theta, blocks k..k+N−1, k > N² | uniform upper bound of Off by R_res | PROVED (at y=0) | R^{−½}Off R^{−½} → J_N − I_N: there is no \|Off\| ≤ C R | Off ≥ −R (one-sided critical) OPEN; the limit I−J satisfies it |
| GLOBAL "Factorial extension before resonance" + corollaries (read) | theta, y=0; b_λ, squares P_m b − R_m b | Q = Σ Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b) exact | identity PROVED; D ⪰ 0 and E ≥ 0 separately refuted; E ≥ −C·S_sq refuted (c = δ₁); B+M ≥ 0 FALSE (test d=1,2, c=(1,−1/100)) | D has entries > 0 but D ≤ H and H has a negative compact test (GRAM §19.11); E(δ₁) < 0 with S_sq = 0 | Q = L + M on the squarefree kernel; 0 ≤ B ≤ L matricially |
| GLOBAL "Control of the orthogonal substitution" (read) | theta | P_m → orthogonal projection Π_m | PROVED (invalidates the replacement) | Π_m = I; Σ Λ(m)‖F − R_mF‖² = ∞ | — |
| GLOBAL "Grouped divisorial covariance" and "indefinite divisorial remainder" (read) | probabilistic lift: R(F) = Σ n^{−½}C_{½}(n) Re c_F(log n) | sign the grouped coefficients C_s(n) | PROVED (negative) | C_s(p²) < 0, C_s(p²q²) > 0; even primitive tests F_± (bumps (1,−5/2,1)) give R(F_+) = (7/4)κ‖g‖² > 0, R(F_−) = −(1/4)κ‖g‖² < 0 | does not rule out compensation with ARCH |
| GLOBAL §2 (read) | integers | strategic audit of "exact arithmetic transfer and near-coincidences" | review, no theorem | "Near has no separate sign… estimating Near in absolute value does not constitute the change" | **live obligation**: joint SIGNED inequality Arch vs terms m≈kn, uniform in vectors and sizes, keeping phases and boundaries |

### F5. Hyperbolic Gram / operator realization (211 POWER_HYPERBOLIC_MODEL_GRAM)

| id | coordinates | operation | result | exact reason | survived |
|---|---|---|---|---|---|
| §§1–6 (read) | model φ_a = exp(−a cosh 2t); kernel [(M_a(u_i)+M_a(u_j))/(u_i+u_j)] | positive Green function of an ODE in scale | PROVED for the model; transfer to the real Φ **OPEN** | there is no ODE/Green with REP identity for the real Φ; mixtures of densities do not preserve the sign (GRAM §7) | proof that failure of layers does not prevent a sign at all orders in a model |
| §12.6 (read) | realization Q,B,C,D with exact theta observation | build operators | PROVED as realization, not as sign | positive metric and Green are missing | realization and strong equation Y_rr = (b²+ν²)Y + 2DY_r + (−C+2bB̄)Y |
| §12.7 (read) | same | bounded positive local metric | NO-GO PROVED in the declared class | distinct exponents 25/2, 21/2, 11/2, 8 force m₁₁ = m₂₂ = 0 | not excluded: non-local/unbounded metrics, new connections (project rules: reopen only with an explicit non-local kernel + Green identity) |

Note: in this file Near does not appear by name; it lives inside the full kernel A (non-resonant part). The source gives no passage formula to Near_M.

### F6. Descent / recurrence / compensation between scales (211 POWER_DESCENT_016, POWER_RECURRENCE_BOUNDARY_036)

| id | coordinates | operation | result | reason | survived |
|---|---|---|---|---|---|
| DESCENT_016 (read §§1–4) | filters Q = s/(s+u), L = u/(s+u) on the full form W (contacts included) | (DEF) W[f] = W[Qf] + W[Lf], binomial (BIN), law (LAW) | PROVED; arithmetic descent OPEN | positive tail only at a boundary of zero mass; the finite prefix has no sign | (FD) finite differences eventually positive |
| RECURRENCE_036 (read §§1–5) | diagonal boundary A_{N,k} | (FRONT) with beta-binomial weights | PROVED: cone energy O(log L/√L), R_L → A_{N,k} | the remainder keeps the whole initial value | reopening criterion: R_L ≥ −ε_L, ε_L → 0 (RULES_AVOID D4) |

Near appears here only inside "all the contacts" (bounds of QUADRATIC_EXPLICIT017).

### F7. Krylov, Nyquist meshes and counts (211)

| id | coordinates | operation | result | reason | survived |
|---|---|---|---|---|---|
| ROUND_005_A Prop 3.4 (read) | powers of the comb Π³; ratio classes r = mn/k, weight W₃(r) ≥ 0 | cos³ expansion | PROVED as sign of the contribution (REVIEW_004 downgrades it to **ARGUED**); Krylov family NO-GO | in degree 2 there are no near-coincidences; in degree 3 they enter with weight ≥ 0 and Π enters with a minus sign: "they work against the sign in K₂" | — |
| ROUND_007_B §3.2 (read) | triples (m;n,k) | locate when they enter | Cor 3.2 PROVED; sizes NUMERICAL | at T = ½log5 the close triples weigh < 1e−4; the part m = k dominates | list of entry thresholds |
| ROUND_002_A Prop M (via index l.9767) | Nyquist mesh s_k | mesh form of the near-coincidence | Prop M PROVED (index row) | deep samples ⇒ near-coincidences n′^{q_n} ≈ n^{q_{n′}}; no criterion on samples alone decides (212 ROUND_003_1 row 7) | — |
| ROUND_006_C §7 (read) | k-fold products | large sieve count 𝒩_k(ν) | Thm A–B PROVED; §7 lemma **OPEN** | bound exp(2e^T) does not improve without counting near-coincidences of products | target 𝒩_k(ν) ≤ C^kΣb_m² (OPEN, multiplicative energy) |
| ROUND_015_B §2.1 (read) | low block, Poisson tail | identify which part of Λ acts | structure PROVED + sizes ARGUED | near-coincidences do not appear in the low block; only exact divisibility (Λ∗1)(N) = log N | — |
| NEAR_CASES_RESULTS (read) | packets ψ_ε centred at log m | improvement of nearfree; 2 packets; triangle (k,2k+1,4k+3) | §1 PROVED (removes log log M); §2 counterexample to Loewner monotonicity; §4 falsifier of the cycle (p,p,p²) | §1: large K still prevents near-coincidences; §4: cubic term −2x²z < 0; d → ∞, not negativity of the form | 2×2/chain/triangle battery; "the collective norm of the near-contact matrix against the archimedean energy remains to be controlled" |

### F8. Identity (PC) of phase 161 and its hyperbola tail

| id | coordinates | operation | result | exact reason | survived |
|---|---|---|---|---|---|
| R161_001 (read) | translation operators; H_{M,N} = L_M S_N − K_N (hyperbola tail, coefficients h(k) at k > N) | joint identity (PC): S_N A_M 𝓕 = {X,E_N} − L_M*E_N − JH − H𝓕 | Thm 2.1, 3.1, 4.1 PROVED; without sign | "positive coefficients do not make a sum of translates positive" | (PC); interior defect δ_a(k) of each falsifier |
| R161_002 §1 | same | square ‖R_{M,N}F‖² | Thm 1.1 PROVED (blind to the sign) | invariant under A_M → −A_M | oriented pairing (OR) = ⟨A_MG, S_N*S_NG⟩ |
| R161_002 §§4–8 | same | SP-161 / L161.1: weights w_N ≥ 0 that telescope | Thm 8.1 PROVED: NO-GO | [p](Σ w_N H_{M,N}) = log p Σ_{N<p} w_N > 0 at every large prime | Cor 8.2 (see (d)) |
| R161_003 | Mellin; S_N^ren = S_N − C_N(D) (lattice − continuum) | polar renormalization | Prop 1.1, Thm 2.1–2.2 PROVED; L161.2 OPEN → withdrawn | raw sums oscillate ≍ N^{½} | renormalized defect → 0 on Schwartz |
| R161_004 | scalar D(u) = Σ_{log n≤u} Λ(n)/√n − 2(e^{u/2} − 1); divisor fibre | scalarize or average over fibres | Cor 2.1, 3.1 PROVED (by citations): L161.2 withdrawn | scalar → Paper 41 C4–C5 (square of the wrong sign, negative density below log 2); fibre → ANOVA 104/106 (zero spectral gap); Möbius → P121 CMO (the logarithmic derivative kills the diagonal). §4 identifies the target with a rank certificate [H] | L161.3 (see (d)) |
| R161_005–006 | exterior port ℓ_T(F) = (1−P)AF; one-sided discrepancies Δ^R, Δ^L | specialization of (PC) to a first-contact state | Thm 1.1, 2.1 PROVED; critical normal symbol OPEN [H] | — | cross contamination only in the two Tate directions |
| 212 ROUND_003_6 (read) | truncated Möbius test M_N; remainder R(F) | a_T = f₀ − f₁ − R₀ + R₁ | PROVED / CONDITIONAL (domain); Lemma 1 and Cor 2 NO-GO with class | affine blindness: a_T^{(c)} = f₀ − cf₁ − (c−1)g − R₀ + cR₁ | **R(F)** "sees exactly the near-coincidences d ≈ k, k ∈ (N,N²], with unsigned Möbius weights c_N(k)" |
| 212 ROUND_004_C (read) | R(F) | study R(F) | repetition in essence; Lemmas 1–5 PROVED; R ≤ 0 false (Lemma 5) | in the translation-invariant class every manifest writing sums to a certificate without inverse (Lemma 4); needles do not distinguish c | — |
| 212 ROUND_004_A (read) | real weights w_N and sieve weights λ_d | L161.1 with sign | Lemma 1, Cor, Prop 2, Lemma 3 PROVED; NO-GO with class 𝒞_w | exact telescoping forces w = δ_{N=1} (tautological); cancelling the tail at primes requires Σw_N = 0 vs Σw_N = 1 | interior block I^λ (near-coincidences with sieve coefficients θ^λ): "its sign was not examined" |
| 212 ROUND_011_A (read §§0–2) | Δ^R ℓ_T(F) | sign of the lattice discrepancy (Euler–Maclaurin, Hermite–Hadamard) | selection NO-GO; Lemmas 1–2 PROVED | Δ^R linear in F (uniform sign ⇒ zero functional) and without Λ (blind to cΛ and deletion) | see (d) |

### F9. Sum/difference channels (R162_1003, read)

| coordinates | operation | result | reason | survived |
|---|---|---|---|---|
| full line T = ∞; sum channel Re(D²) (Λ∗Λ) and difference channel \|D\|² | cancellation of (Im D)² between channels via the functional equation [H]; Λ²-Selberg test; finite T | Thm S PROVED; Thm R PROVED [H]; Prop 4.1–4.2, Cor 4.3 PROVED; §5 NO-GO | Prop 4.2: the kernel is Toeplitz in log, not GCD; Cor 4.3: H = Z*DZ is a congruence (Sylvester); §5: at finite T P_TS_xP_TS_yP_T ≠ P_TS_xS_yP_T (Brown–Halmos), the channels differ by Hankel products | — |

### F10. Prime sites and affine form (via index; primary sources not opened)

| id | result (index) |
|---|---|
| CA_K_002 (193, l.9002, l.9016–9019) | on prime sites Div ≡ 0 and the target is Arch ≥ Near; Near = Σ_h C_s(h) (Chen correlations p − h = p′q^a); parity and residues are reindexings (each Near_q of trace 0, indefinite); irrational sites p+θ_p have the same truth value. PROVED reformulation; "candidate to re-examine" |
| INV_V_002 (196, l.9119) | 𝔞_T = A_∞ + ½𝔄ff_T − ½Re⟨Vf,f⟩_Ш; 𝔄ff not diagonal in Mellin, linear in the comb; Thm V2.4 PROVED, V2.2(c) FALSE |
| INV_G_001 (194, l.5833) | NO-GO class 𝒞_G; "positive part = Near (REF)" |
| L2_BUILD_020 (index R9) | near-triple resonator: exact at Ω ≥ N³; natural resonance O(1) |
| L2_BUILD_023 Thm T (index R9) | each 2×2 section is the band \|X(d)\| ≤ 2a₀; only necessary |
| 212 round 15 Y1 (RULES_AVOID) | reindexing m − kn = h, Farey, Ramanujan, large sieve, Selberg: repetition; class Σx_nQ_n blind (PROVED) |

---

## (a) Dictionary of the same term

| system | name in the source | formula / passage (when the source gives it) |
|---|---|---|
| integers (P47 prop:AM) | Near_M | Near_M(m,k) = ½Σ_{n≥2, kn≠m} v_n c₀(log(kn/m)); Div_M + Near_M = ½[Ξ_{F₀}(log(m/k))] (DOSSIER §1.4; N_021 Prop 1: Near = sᵀ[Ξ − 1_{k\|m}v_{m/k}c₀(0)]s) |
| integers, additive shift | slices h ≠ 0 | sᵀW₁Vs = Σ_h Σ_{m−kn=h} s_ms_kv_nc₀(−log(1 − h/m)); h = 0 ↔ Div, h ≠ 0 ↔ Near; \|h\| ≲ 2T₀m (L2_030 §1(c)) |
| spectral / Dirichlet | finite-resolution remainder of \|P_s\|²V | sᵀ𝔸s = (1/2π)∫F̂₀²\|P_s\|²[m(τ) − Re V(τ)]dτ; Div = Bohr-diagonal part, Near = near-diagonal (L2_030 §§1(b), 2) |
| Ramanujan | fluctuation q=1 + components c_{p^b}(j) | Q = m^♯ − ⟨Chebyshev q=1⟩ − Σ_{p^b}⟨c_{p^b}⟩ (L2_030 §3; suppression of 031 §3 corrected) |
| matrices Z, Δ | 𝒟_M | X_M = Z⁻¹Ł_M + 𝒟_M, 𝒟_M = Near (N_022 §3, precise index ARGUED) |
| Bohr (phases θ_p) | part off the diagonal torus | only Div is diagonal with independent θ_p (N_022 §4; L2_028 §2(c)) |
| prime sites | Near = Σ_h C_s(h) | via index (CA_K_002) |
| metrics on ℕ | pairs ρ < δ | ρ = \|log m − log k\|, δ = log(lcm/gcd); Div: ρ = δ = log p^j (ROUND_002_D, ROUND_003_B) |
| theta / Gaussian | Off = A − R_res (pairs kn² ≠ lm²) | A(z_k, z̄_l) = ∫_1^∞ w_{kl}Φ_kΦ̄_l; resonances kn² = lm²; non-resonant part bounded by (NEAR)/(OFF) (GRAM §§16.2, 17). The source gives no explicit passage Off ↔ Near_M; at y=0, "Off ≥ −R_res ⟺ A₀ ⪰ 0 on integers" (§17.6) |
| theta, factorial | D and E in Q = ΣΛ‖P_mb − R_mb‖²_K + b*Db + E | GLOBAL "Factorial extension" |
| window (translation operators) | remainder R(F) of the truncated Möbius; block I^λ | R(F) = Σ_{N<k≤N²} c_N(k)k^{−½}Re[⟨𝓜V_{−log k}F,F⟩ − Σ_{\|log(k/d)\|<2T} Λ(d)d^{−½}⟨V_{log d−log k}F,F⟩] (212 ROUND_003_6 (4.2)); I^λ (ROUND_004_A (4.3)) |
| window, Krylov | ratio classes W₃(r), r = mn/k ≈ 1 | ROUND_005_A Prop 3.4 |
| Nyquist mesh | deep samples s_k | s_k = m + r − A_T + c(−1)^k + 2Σv_n sin²(πk log n/4T) (Prop M, via index) |
| divisor hyperbola (161) | tail H_{M,N}, coefficients h_N(k), k > N | H = L_MS_N − K_N; h_N(p) = log p (N < p), 0 (N ≥ p). It is the exact-divisibility counterpart, not Near; Near appears only on compressing to the window (R(F), I^λ, Δ^R) |
| hyperbolic Gram | (not named) | inside the full kernel; no passage formula |
| packets | near-contacts | entry −v_n c/2 in the packet matrix (NEAR_CASES_RESULTS §2) |

## (b) Reasons for failure grouped

1. **Near has no sign of its own**: it is the resolution remainder of the same product (L2_030 §2; GLOBAL §2); treating it separately leaves a matrix with zero diagonal or an indefinite remainder (ROUND_003_B Thm 4; divisorial remainder with F_±).
2. **Format / pattern**: divisor incidence, Schur, semiorders and Kronecker do not see coprime nearly proportional pairs; the information is in the values, not in the pattern (ROUND_003_B Lemma 2; 212 ROUND_003_7 Lemma 1; ROUND_004_D Lemmas B–C; N_022 §3).
3. **Separating costs resolution**: removing Near (Near-free, nearfree, large K) buys archimedean energy that wins for local reasons (L2_029; RESULTADOS §1).
4. **Blindness to the weight / linearity**: identities with Λ∗1 = log, Möbius or sieve are affine in c or linear in F (Lemma 1 of 003_6; ROUND_011_A Lemmas 1–2; Y1 of RULES_AVOID; R162_903 Thm 4.1–4.2).
5. **Class closed under finite modification**: statistics of progressions/sieve (N_021 Thm 2; phase 190 [sens]).
6. **Reformulation**: Poisson in a smooth family returns to the continuous form (ROUND_001_A); balanced restrictions ⟺ D (L2_031 Thm E); Off ≥ −R_res at y=0 is the target (GRAM §17.6).
7. **Lack of uniformity**: theta equivalents only for fixed lists (GRAM §16); neither a uniform lower bound (Off ≥ −CE_y) nor upper bound (\|Off\| ≤ CR) (§17.6, resonant budget).
8. **Pairs do not imply the collective**: 2×2 sections only necessary (L2_023 Thm T); triangle and cycle (p,p,p²) with negative cubic (RESULTADOS §§3–4).
9. **Sign lost by squaring / orientation**: (SQ) blind; positive weights do not telescope the tail (R161_002 Thm 1.1, 8.1).
10. **Contribution against in degree 3**: W₃(r) ≥ 0 with Π subtracting (ROUND_005_A; ARGUED after REVIEW_004).

## (c) Explicitly pointed out as not executed / open

- Joint SIGNED inequality Arch vs terms m≈kn, uniform, with phases and boundaries (GLOBAL §2; index R9 "admissible directions": fluctuation q=1 + c_{p^b}(j) at resolution ≈ e^{2T}). OPEN.
- One-sided critical comparison Off ≥ −R_res (GLOBAL "resonant budget"). OPEN.
- Joint compensation D+E with the squares; L+M at all orders (GLOBAL factorial). Not obtained.
- W not supported on divisibility that sees m≈kn, with its own formula and signed ρ (212 ROUND_003_7, ROUND_004_D: "I do not know how to write it").
- Interior block I^λ with sieve coefficients: "its sign was not examined" (212 ROUND_004_A).
- Telescoping after compressing to the window with the leak squares of C_T; bookkeeping R161_032 (4.2) "still not derived"; tests other than S_N𝓕F; weights depending on F (ROUND_004_A).
- SP-161/L161.1 with signed weights/discrete derivatives and compressed leaks: "never written" (ANNEX_161_FILES_1 §(c)); the branch 𝒞_w later NO-GO (ROUND_004_A).
- Large sieve lemma 𝒩_k(ν) for k-fold products (ROUND_006_C §7). OPEN.
- Conductor >1 routes other than the two excluded ones (N_021 §3). Not excluded.
- Non-local / unbounded metrics and new connections for the theta realization (HYPERBOLIC §12.7). Not excluded.
- Hadamard positivity coupling primes with m≈kn; non-affine transport of lags; odd pairing nonlinear in A_M (RULES_AVOID X, no written object).
- Prime sites Arch ≥ Near: "candidate to re-examine" (index l.5922, via index).
- Phase 190: decide whether the boundary of Q_M(w) is of PNT-error size or margin M^{−3} (via index); ROUND_001_A resolved it as superpolynomial in its family and the remainder ℛ_M remained ARGUED.

## (d) Exact status of L161.3 and of the terminal derivative of R161_002 Cor 8.2

**Cor 8.2 (R161_002).** Statement: at a prime p, h_p(p) − h_{p−1}(p) = −log p; "the von Mangoldt sign appears as the terminal discrete derivative of the positive tail, not as a positive average; the next mechanism must orient this derivative". It is a PROVED corollary of Thm 8.1 (which is a PROVED NO-GO for weights ≥ 0). Follow-up:
- R161_003 §5 turned that requirement into L161.2 ("the signed derivative must recover the jump −log p"); L161.2 WITHDRAWN (R161_004) in its scalar-positive and positive-fibre forms.
- 212 ROUND_004_A: with real weights w_N, exact telescoping forces w = δ_{N=1} and cancelling the tail at primes requires Σw_N = 0, incompatible (Corollary PROVED). The pure derivative w = δ_{N+1} − δ_N gives the single-translate PC identity with coefficient 0 at r = 1: "a_T does not appear" (PROVED). NO-GO with class 𝒞_w.
- Index: row "Hyperbola tail… non-negative weights — DEAD [sign only in the terminal jump]" (l.5166, l.12346).
- I found no memo that builds an orientation of the terminal derivative outside class 𝒞_w; only the "not excluded" items of ROUND_004_A remain (tests other than S_N𝓕F, weights depending on F, telescoping after compression with C_T leaks).

**L161.3 (oriented first-contact Poisson port).** Defined in R161_004 §6: apply (PC)/(PC-ren) to a primitive first-contact state before any norm or trace and prove that its additive exterior port annihilates a critical conormal class [H] (the source's formulation uses zeros). Status in the source: **OPEN** (R161_003 §6, R161_004 §6, R161_099). PROVED pieces around it: R161_005 Thm 1.1 (PR𝓕F = PS_Nr + B_{N,T}(F)); R161_006 Thm 2.1 (B^ren = Δ^R_{N,T}ℓ_T(F) − e^{−t/2}a_−(ℓ_T(F))); cross contamination in the Tate span PROVED; "cancellation with the Tate forcing: not computed"; "extraction and annihilation of the critical normal coefficient: OPEN" [H]. R161_099 and R161_007–008 advance the identification of the jet [H].
Later status (212): ROUND_011_A / RULES_AVOID U1–U2: "quadratic L161.3 closed by R161_029 (false monotonicity), **oriented OPEN**"; sign of the lattice discrepancy on Δ^R: selection NO-GO (linear in F; without Λ). Missing: "an oriented pairing of two orientations whose cross term has the sign of D^Poisson ≥ 0 (R161_029 (6.1))". Moreover "the four residues live on the radical of an assumed first contact, not on all of P_T". ROUND_013_B: (OR) of R161_002 does not close it; oriented L161.3 remains OPEN.

## Sources read

211: README, STATEMENT_001, DOSSIER_001 §1.4, STATE_001 (rows), LEDGER (rows), NEAR_CASES_RESULTS_2026_11_04, ROUND_001_A, ROUND_003_B, ROUND_005_A §3, ROUND_006_C §7, ROUND_007_B §3.2, ROUND_015_B §2.1, POWER_GLOBAL_ROUTE_REVIEW §§1–5 and cited sections, POWER_GRAM_SLICES_OBSTRUCTION §§1–2, 16–17.7, POWER_HYPERBOLIC_MODEL_GRAM §§1, 6, 12.6–12.7, POWER_DESCENT_016 §§1–4, POWER_RECURRENCE_BOUNDARY_036 §§1–5 (rest of the 211 memos from the grep list: context lines only).
212: RULES_AVOID (C, D, E, F, U, V, X, Y), OBJECT_SPEC O6, ROUND_001_B, ROUND_003_6, ROUND_003_7, ROUND_004_A, ROUND_004_C, ROUND_004_D, ROUND_011_A, ROUND_022_A (verdict), ANNEX_161_FILES_1 (lines).
161: R161_001–006 in full or by verdict/status sections; R161_099 §4.
162: R162_903, R162_1003.
188 (antecedents cited by 211/212): L2_BUILD_029, 030, 031 (header), N_BUILD_021 §§1–3, N_BUILD_022 §§1–4.
Master index: grep for Near / near-coincidences / L161 (rows cited by line number).
