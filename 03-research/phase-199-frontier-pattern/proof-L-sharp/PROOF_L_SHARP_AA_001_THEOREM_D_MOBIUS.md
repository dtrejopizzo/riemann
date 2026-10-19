# PROOF_L_SHARP_AA_001 — Theorem D: the Möbius-lattice form of the exterior datum (pen and paper; one NUMÉRICO table)

Phase 199, , no zero
datum is used,
Notation as in BRIDGE_001 §1, E_001 §1–3, J_001: μ ≥ 5, λ = √μ, a = ½log μ, f even admissible, f = E⁻¹g on [1/λ,λ],
min-leak gauge filler on |u| < 1/λ, r = f̂|_{(λ,∞)} (f̂(ω) = 2∫_0^∞ f(u)cos 2πωu du), r̃(x) = e^{x/2}r(e^x),
Ψ̌(x) = e^{x/2}Σ_{n≥1} r(ne^x) on x > a, 𝒲_ext = 𝒜 − 2⟨Ψ̌,Ψ̌_log⟩ + 2AB (E.2/E.3).

## 0. Corpus / index check, and why this is not a retry
Read: EXTERIOR_DATUM_001 (Lemma E.1, Prop C′.1, Cor C′.2), A_001 Prop 3.1, E_001 Thms E.1/E.1′/E.2, Rem 3.2, J_001 Prop J.1,
Z_001 Theorem C + AUDIT_L_SHARP_11, BRIDGE_001 Lemma B.0 and §4, AUDIT_L_SHARP_10/11 constraints. Index README phase-199
block (l.449 ff.) grepped for "Möbius lattice / C_q / ratio q / M̃ / partial sums μ(m)/m": only EXTERIOR_DATUM_001 Cor C′.2
(ARGUED, formal) and INV_C_001 (Möbius counts of h⁰, "sin información para el signo"). New reason: C′.2 was formal and
leading-order; here the decomposition is made **exact** (one function H, one inner remainder φ₀), the grouped coefficients
are computed exactly, and the proposed closing mechanism ("PD kernel × Möbius vector, |M̃| ≤ 1") is tested and refuted
(§3–§5). Not a positivity attempt via any indexed family: no diagonal bracket (dead, C′.2), no Fresnel bound (dead).

## 1. Theorem D(i) — exact lattice structure (PROVED)
Let h(v) = v^{-1/2}g(log v) (window function pulled back, smooth on [1/λ,λ]) and **H(v) := h(|v|)·1_{[1/λ,λ)}(|v|)** (even).
**Theorem D(i).** For every admissible g, with any filler on |u| < 1/λ,
 f(u) = Σ_{1≤m<μ} μ(m) H(mu) + φ₀(u),  supp φ₀ ⊂ [−1/λ, 1/λ],                      (D.1)
 r(ω) = Σ_{1≤m<μ} (μ(m)/m) σ(ω/m) + φ̂₀(ω)  (ω > λ),  σ := Ĥ.                      (D.2)
*Proof.* On 1/λ ≤ u ≤ λ: H(mu) ≠ 0 iff mu < λ (mu ≥ u ≥ 1/λ is automatic), so Σμ(m)H(mu) = Σ_{m<λ/u}μ(m)h(mu) = E⁻¹g
(EXTERIOR Lemma E.1 = A_001 Prop 3.1). For m ≥ μ, H(mu) = 0 on u ≥ 1/λ (mu ≥ λ). Hence f − ΣμH(m·) vanishes on
[1/λ,λ] and outside [−λ,λ]: it is supported in [−1/λ,1/λ]. (D.2): F[H(m·)](ω) = m⁻¹Ĥ(ω/m). □
So the whole window part is **one function σ = Ĥ sampled on the lattice ω/m with weights μ(m)/m**; the only other object
is φ₀ (filler minus the inner pieces h(mu)1_{[1/(mλ),1/λ)}, a function on the short interval).
**Corollary D(i′) (edge jets; PROVED).** The singular support of f on (0,λ] is ⊂ {1/λ} ∪ {λ/m : m < μ}, and at u = λ/m the
jet of f jumps by μ(m)·(h(λ), m h′(λ), m²h″(λ), …) (the jet of h at its upper cut, dilated by m). Hence, as ω → ∞, with
 σ(x) ~ Σ_{k≥0} 2Re[ e^{2πiλx}(−1)^k h^{(k)}(λ)(2πix)^{-k-1} ] − (same at v = 1/λ)
   = h(λ) sin(2πλx)/(πx) + h′(λ) cos(2πλx)/(2π²x²) + O(x^{-3}) + [lower-cut terms, phase e^{2πix/λ}],
line m of r carries phase e^{2πiλω/m} (in ρ(t) = r(λt): frequency c t/m, c = 2πμ), and all lower-cut terms of all m, together
with φ̂₀, carry the single phase 2πω/λ (one extra line τ, gauge-dependent). Core data (f(λ) = 0 ⇔ g(a) = 0) kill the 1/x
term; the kink h′(λ) then leads (EXTERIOR §2: h′λ/(h c) = 53.9 at μ = 15, so the asymptotic regime starts late — the
expansion is exact as an asymptotic series but not a numerical approximation at ω/m = O(1)).
**Remark (what is not small).** Line m samples σ at ω/m ∈ (λ/m, ∞), i.e. *below the tail threshold λ* for m ≥ 2: lines m ≥ 2
read the **bulk** of Ĥ, not its tail. This is why they are O(1) and absent from every prolate (EXTERIOR §1–2).

## 2. Theorem D(ii) — the ratio-grouped identity (PROVED, exact)
**Theorem D(ii).** Assume the absolute-convergence hypotheses of E_001 §1 for r (core data suffice for the σ-part;
otherwise read Σ_n in the Abel/L² sense). Then on x > a
 Ψ̌(x) = e^{x/2} Σ_{q∈ℚ_{>0}} C_q σ(qe^x) + Ψ̌₀(x),  Ψ̌_log(x) = e^{x/2}Σ_q D_q σ(qe^x) + Ψ̌₀,log(x),
with, for q = b/a in lowest terms,
 C_{b/a} = Σ_{k<μ/a} μ(ak)/(ak) = (μ(a)/a)·M̃_a(μ/a),  M̃_a(y) := Σ_{k<y,(k,a)=1} μ(k)/k,               (D.3)
 D_{b/a} = Σ_{k<μ/a} μ(ak)log(bk)/(ak) = log b·C_{b/a} + (μ(a)/a)Σ_{k<μ/a,(k,a)=1} μ(k)log k/k.        (D.4)
*Proof.* Insert (D.2) into Ψ̌: e^{x/2}Σ_n Σ_m (μ(m)/m)σ((n/m)e^x); write (m,n) = (ak,bk), (a,b) = 1; the constraint is only
m = ak < μ (n is free: n e^x > λ for every n ≥ 1 when x > a, so no truncation enters in this variable). μ(ak) = μ(a)μ(k) if
(k,a) = 1, else 0. Same for Σ_n log n r(ne^x) with log n = log b + log k. □
**Facts on the coefficients.**
- C_q depends **only on the denominator a** of q; all integer ratios q = b share C_b = M̃(μ) := Σ_{k<μ}μ(k)/k.
- |M̃_a(y)| ≤ 1 for all y, a (PROVED for a = 1, elementary: Σ_{k≤y}μ(k)⌊y/k⌋ = 1 gives |yM̃(y) − 1| ≤ ⌊y⌋−1 … ⇒ |M̃| ≤ 1;
  coprime version CITED, Granville–Soundararajan 2007 / Ramaré 2013). M̃(y) → 0 and Σ_{k≤y}μ(k)log k/k → −1 (CITED, PNT-level,
  unconditional).
- **NUMÉRICO (exact rationals), μ = 15 (m ≤ 14):** C_{b/1} = M̃(14) = −0.0060; C_{b/2} = −0.162; C_{b/3} = −0.100;
  C_{b/5} = −0.033; C_{b/6} = +0.167; C_{b/7} = −0.071; C_{b/10} = +0.100; C_{b/11} = −0.091; C_{b/13} = −0.077;
  C_{b/14} = +0.071. D_{b/1} = log b·M̃(14) + Σ_{k≤14}μ(k)log k/k (= log b·(−0.006) − 1.01).
  **Correction to EXTERIOR_DATUM_001 §0/§4:** −0.0059 is M̃(14) (the lattice is m < μ = 15); M̃(15) = 304/5005 = +0.061.
- **Integer class (per AUDIT_L_SHARP_12 (4)):** the smallness of M̃(14) is a cutoff accident (M̃(15) = +0.061); nothing
  is built on it — only the unconditional bound |M̃_a| ≤ 1 is used. **Where the integer class sits:** only in the integer class a = 1 (C_b ≈ 0). The non-integer classes carry
  O(1/a) coefficients with sign μ(a)·sgn M̃_a: these, not the integer class, are the large lattice content. The (1,n)
  resonances of EXTERIOR (sign μ(n)) are the (m,nm) pairs; in (D.3) they are absorbed into the class sums.
- **The cΛ-free, Λ-free quadratic form.** With s_q := (e^{x/2}σ(qe^x))|_{x>a} = q^{-1/2}S_{−log q}(σ̃·1_{(a+log q,∞)}):
 𝒲_ext[Ψ̌] = Σ_{q,q′} [C_qC_{q′}(𝒜 + 2A⊗B)(s_q,s_{q′}) − (C_qD_{q′} + D_qC_{q′})⟨s_q,s_{q′}⟩] + (φ₀-terms),   (D.5)
  exact (bilinearity; E.2/E.3). The diagonal q = q′ class is the "C_1-type" sum Σ_a Σ_{(b,a)=1}C_{b/a}²(…); the
  off-diagonal pairs are Σμ(·)μ(·)/(·)-products of class sums, exactly as in (D.3).

## 2bis. Incorporation of AUDIT_L_SHARP_12 (corrections (1)–(4))
(1) σ = Ĥ is the transform of a **truncated** function: its large-ω content is the truncation tail (jump h(λ) + kink
h′(λ) at the upper cut, frequency c/m in ρ), not a Langer chirp; only line m = 1 is identified with the prolate tail
(ARGUED, EXTERIOR §3). Cor D(i′) is stated for truncation jets only. (2) AUDIT: piece m is a dilate of h·1_{[m/λ,λ)} (lower
cut moves). (D.1) is consistent and exact: H(m·) = dilate of h·1_{[1/λ,λ)} and the difference h(mu)·1_{[1/(mλ),1/λ)} is moved
into φ₀ (support |u| < 1/λ). Piece m in dilate 1 and piece nm in dilate n share h·1_{[nm/λ,λ)} entirely; in (D.1) the
extra part is again inside φ₀-type terms, so the coincidence is exact in both bookkeepings. (3) Resonance coefficient of
(line m, dilate 1) × (line nm, dilate n) is μ(m)μ(nm)/(nm²), sign μ(n) for (m,n) = 1. Pairs with μ(n) = 0 are **not**
suppressed: the dilate pair (1,4) gets no line coincidence (μ(4m) = 0) but receives non-coincident line pairs, lower-cut /
φ₀ couplings and bulk overlaps (measured +0.108); (D.5) contains all of these, the "sign μ(n)" statement concerns only the
coincident part. (4) see §2.

## 3. Theorem D(iii) — sign analysis: the proposed PD mechanism is FALSE as stated (NO-GO, PROVED)
The tentative claim "𝒲_ext on lattice data = ⟨v,𝒦v⟩ with v_m = μ(m)/m and 𝒦 positive definite (archimedean kernel PD),
comb absorbed, positivity reduced to |M̃| ≤ 1" fails at three exact points:
(a) **The archimedean kernel is not PD.** Θ_∞(τ) = b_∞ + 2∫(1−cos τu)ν(u)du with b_∞ = Θ_∞(0) = ψ(¼) − log π ≈ −5.37 < 0
  (E_001 §1, A_001 §1). Only the Lévy part 𝓛 (and the killing term) is PD; 𝒜 = b_∞‖·‖² + 𝓛 is indefinite on functions
  with Fourier mass near τ = 0. So the Gram matrix 𝒜(s_q,s_{q′}) is not PD in general.
(b) **𝒦_total is circular.** Writing Ψ̌ = Σ_m μ(m)Z[σ(·/m)/m] (D.2), 𝒲_ext = Σ_{m,m′}μ(m)μ(m′)G_{mm′},
  G_{mm′} = 𝒲_ext(Zσ^{(m)},Zσ^{(m′)}). G is the Gram matrix of 𝒲_ext itself on the ≤ (#{squarefree m < μ} + 1)-dim span
  {Zσ^{(m)}} ∪ {Zφ̂₀}; "G PD" is L′♯ on that span (stronger than needed), not an independent input.
(c) **|M̃| ≤ 1 is not a discriminant (falsifier check, PROVED formally).** By E_001 Rem 3.2 the same lattice arises for any
  (E_D,Λ_D) system with Möbius inverse μ_D (coefficients of 1/D):
  - a_P (Euler factor at P removed): μ_D(m) = μ(m)1_{P∤m}; the lattice loses the lines P | m; resonance (1,n) with P | n
    vanishes, the others keep sign μ(n); integer-class coefficient Σ_{k<y,(k,P)=1}μ(k)/k is still bounded by 1 (CITED) and
    still → 0 (∏_{p≠P}(1−1/p) = 0).
  - cΛ (D = ζ^c, 0 < c ≠ 1): μ_c(p) = −c, μ_c(p²) = c(c−1)/2 ≠ 0: non-squarefree lines appear; resonance (m,nm) for
    (m,n) = 1 has sign sgn(μ_c(m)²μ_c(n)) = sgn μ_c(n), so (1,4) has sign sgn(c(c−1)) (negative for 0 < c < 1: the μ(n)
    pattern breaks); integer-class sum Σμ_c(k)/k → 1/ζ^c(1) = 0 still (c > 0).
  So the near-cancellation C_b → 0 and any bound of type |C| ≤ 1 hold on both falsifiers: they cannot carry the sign.
  The sign must be in the **non-integer classes and their coupling to the edge line / φ₀**, through σ's shape and the
  pair Gram (D.5) — this is consistent with E_001 E.4 (classes individually indefinite; sign = interference).
(d) What is positive: diagonal self-pairings of a single Langer line (Theorem C, AUDIT_11) and the weight bound 𝔴_μ ≥ log 2μ
  (B.0) for the S-norm; neither controls the O(1/a) class coefficients of (D.3).

## 4. Theorem D(iv) — what L′♯ reduces to on the Möbius-lattice class (exact statement, OPEN)
On data of form (D.1), L′♯ is equivalent (exact, by D(i)–(ii)) to: for the finite vector v = (μ(m))_{m<μ, squarefree} ⊕ 1,
 vᵀ G v ≥ κ·S(Ψ̌)  with G_{mm′} = 𝒲_ext(Zσ^{(m)},Zσ^{(m′)}) (σ^{(m)} := m⁻¹σ(·/m)), G_{·,0} the φ₀-couplings,
equivalently the class form (D.5) ≥ κS. Status: PROVED — (D.1)–(D.5), the coefficient formulas, |M̃| ≤ 1 (a = 1),
the falsifier transport. CITED — PNT-level limits, coprime bound. NO-GO — "PD archimedean kernel ⇒ positivity", "|M̃| ≤ 1 /
M̃ → 0 closes the lattice form" (both falsifiers satisfy them). OPEN — the sign of vᵀGv, i.e. control of the non-integer
classes a ≥ 2 (coefficients C_{b/a} = μ(a)M̃_a(μ/a)/a, O(1/a)) against the diagonal, given σ = Ĥ of an *admissible* g.
Concrete next test (NUMÉRICO, cheap, uses EXTERIOR data): assemble G at μ = 15 from the stored columns (14 cells) and read
its inertia; if G has negative directions, check whether v = μ(m) avoids them only through σ's admissibility (Tate).

## 5. Labels and records
PROVED: Thm D(i) (D.1, D.2, edge jets), Thm D(ii) (D.3–D.5), |M̃(y)| ≤ 1, D(iii)(a)–(c). CITED: PNT Möbius limits,
coprime partial-sum bound. NUMÉRICO: coefficient table (exact rationals). OPEN: D(iv) inequality, L′♯. NO-GO: the PD/Möbius-bound
closing mechanism. Correction: M̃ at μ = 15 is M̃(14) = −0.006 (EXTERIOR's value right, its label M̃(15) wrong); per AUDIT_12 it is a cutoff
accident and not used. AUDIT_12 corrections (1)–(4) incorporated (§2bis).
No sign of row D claimed. L′♯ OPEN. Row D OPEN.
