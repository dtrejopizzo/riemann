# PROOF_L_SHARP_A_001 — Strategy A: the residual identity as a quadratic form on the exterior data

Phase 199, prover memo (pen and paper; no numerics). Target: **Lemma L′♯** (AUDIT_199): ∃κ>0, A≥0 such that
∀μ≥5, ∀g ∈ E(core): W_T(g) ≥ κμ^{−A}ℓ(g), ℓ(g) := inf{leak(f): f admissible, Ef = g}.
No zero data is used beyond citation; no equivalence of any
kind is invoked.

**Outcome in one line.** L′♯ is NOT proved. What is proved: (1) an exact *half-line identity* W_T(Ef) = 𝒲_ext[Ef|_{(0,1/λ)}]
(the window value of the complete Weil form equals the full Weil form of the aliasing tail of f below the window);
(2) the gauge is exactly the radical of 𝒲_ext and ℓ(g) is a squared distance to it; (3) a comb-generic tail
coercivity (frequencies beyond Ω_* = e^{𝒜_T+λ+O(1)}) giving L′♯ with A = 2 on that subspace; (4) the precise finite
block that remains, written as a matrix inequality in the prolate basis, with its upper-bound side CITED (Guo). The
decisive step is isolated and is OPEN; §6 shows that every step proved here is either multiplicative-generic
(holds for Beurling / deleted-prime systems with their own summation map) or comb-generic, so none of them is the
Λ-step.

## 0. Corpus check (rule ) and why this is not a retry
- **Index read:** README l.50 (coercivity walls W-*), l.52 (N_018: identities + Bochner/C–S), l.447 (C1: CCM + Guo
  residual identity, "falls on L81 unless the gluing term gives the source"), l.450 (MECH_001 + AUDIT_12), l.451
  (PROOF_L_SHARP_B_001), phase 197 BARRIER_EST_001, 06_ [opcalc]. Semiring principle (05 §"El signo tiene que venir
  del semianillo").
- **Sources read:** MECH_001 §3 (Prop 3.1), AUDIT_199 (gauge falsifier, L′♯), Paper 47 eq:symbol/eq:form/eq:W,
  lem:K, thm:A, lem:roughEF, def:W, subsec:finite; Guo (Zenodo 23297284) §2 (Lemmas 2.1–2.6, Cor 2.7), §3 (P1–P5),
  §4 (Lemmas 4.1–4.4, Thm 4.5, Rem 4.6), §6 (Lemmas 6.1–6.2, Rem 6.3), §10; Mori VII Theorem N, Rem 2.3; Mori VIII §2.
- **Why not a retry.** C1 (l.447) proposed Guo's identity as a *gluing* source and was ranked low because it
  "falls on L81" (semilocal stabilisation without a sign source). This memo does not glue and claims no sign. It
  does something the index does not record: it rewrites the residual identity as an exact *quadratic* identity
  (Theorem 1.1) rather than an operator identity, identifies the gauge with the radical (Prop 2.1), and converts
  L′♯ into a coercivity statement for the Weil form on a half-line against aliasing data (Thm 3.1). B_001 worked in
  Mori's auxiliary operators; this memo works in the intrinsic objects. By N_018 every step here that is an
  identity + Schur/C–S is non-decisive; §6 says so explicitly for each step.

## 1. Setting and the half-line identity

**Notation.** λ = e^T, μ = λ², a = T, I = (−a,a). Admissible f: even, f|_{[−λ,λ]} ∈ C², f = 0 outside [−λ,λ],
f(0) = f̂(0) = 0 (Guo's class G_λ), f̂(ξ) = ∫f e^{−2πixξ}. r_f := f̂·1_{|ξ|>λ} is the out-of-band part;
leak(f) = ‖r_f‖² = 2∫_λ^∞|f̂|². Summation map (multiplicative) (Ef)(u) = u^{1/2}Σ_{n≥1} f(nu), u > 0, and in the
log variable Φ_f(x) := (Ef)(e^x) = e^{x/2}Σ_n f(ne^x), x ∈ ℝ. Then Φ_f = 0 on [a,∞) (ne^x ≥ λ), Φ_f|_I = g is the
window vector of MECH_001 §3 (Guo's U E_λ f), and Φ_f|_{(−∞,−a)} =: Ψ_f is the **exterior (aliasing) tail**. W_T is
Paper 47's complete form; Guo's Q_{Wλ}[v] = ∫Θ_λ|Fṽ|² + ⟨v,Πv⟩ is W_T (⟨v,Πv⟩ = 2Re(AB̄), checked from Guo (2.4)
with A = ∫ve^{x/2}, B = ∫ve^{−x/2}; AUDIT_ZENODO §0, CITED). Ã is the associated operator (Guo Lemma 2.3).

The full Weil distribution on functions Φ on ℝ (Guo (4.7)):
 WΦ(x) = b_∞Φ(x) + ∫_0^∞(2Φ(x)−Φ(x−t)−Φ(x+t))ν(t)dt − Σ_{q≥2}c_q(Φ(x−log q)+Φ(x+log q)) + ∫2cosh((x−y)/2)Φ(y)dy,
with ν(t) = e^{−|t|/2}/(1−e^{−2|t|}) (Paper 47's K(|t|)/2), c_q = Λ(q)q^{−1/2}. For two functions Φ₁, Φ₂ with
disjoint supports J₁, J₂ and such that the integrals below converge absolutely, put
 𝒲(Φ₁,Φ₂) := ∫Φ̄₁ WΦ₂ = −∫∫Φ̄₁(x)Φ₂(y)ν(x−y)dxdy − Σ_q c_q∫Φ̄₁(x)(Φ₂(x−log q)+Φ₂(x+log q))dx + ∫∫Φ̄₁(x)2cosh((x−y)/2)Φ₂(y)dxdy
(the b_∞ term and the 2Φ(x) term drop by disjointness). This expression is symmetric in (Φ₁,Φ₂) for real functions
(ν even, the q-sum is symmetric under x ↦ x ± log q, cosh even). For Ψ supported in (−∞,−a) with
|Ψ(y)| ≤ Ce^{3y/2} put
 𝒲_ext[Ψ] := b_∞‖Ψ‖² + ½∫∫_{y,y'<−a}|Ψ(y)−Ψ(y')|²ν(y−y')dydy' − 2Re Σ_q c_q∫Ψ̄(y)Ψ(y−log q)dy + 2Re(A(Ψ)\overline{B(Ψ)}),
A(Ψ) = ∫Ψe^{y/2}, B(Ψ) = ∫Ψe^{−y/2}: this is the complete Weil form of the half-line function Ψ (same expression
as Paper 47 thm:A with the Lévy energy written as a double integral; absolute convergence: ν(y−y') ≤ 2/|y−y'| and
Ψ Lipschitz give the Lévy term, Σ_q c_q q^{−3/2} < ∞ and |Ψ(y−log q)| ≤ Ce^{3y/2}q^{−3/2} give the prime term,
e^{∓y/2}e^{3y/2} integrable at −∞ gives the pole term).

**Theorem 1.1 (half-line identity; PROVED).** Let f be admissible and real with f(λ) = 0. Then g = Φ_f|_I ∈ Dom(Ã),
Ψ_f = Φ_f|_{(−∞,−a)} satisfies |Ψ_f(y)| ≤ 2C_f e^{3y/2}, and
  **W_T(g) = 𝒲_ext[Ψ_f].**
*Proof.* (a) Guo Lemma 4.3 (CITED; f = v there since β = f(λ) = 0): Φ_f(x) = e^{−x/2}Σ_{n≥1}f̂(ne^{−x}) for all x,
|Φ_f(x)| ≤ 2C_f e^{3x/2}, Φ_f locally Lipschitz, Φ_f = 0 on [a,∞). Guo Lemma 4.2: g ∈ Dom(Ã).
(b) Guo Lemma 4.4 (CITED, proof read; it uses the Mellin identity H_Φ(s) = ζ(s)M_f(s), the explicit formula for
C_c^∞ tests and a cut-off): WΦ_f = 0 almost everywhere on ℝ, with absolutely convergent integrals and series.
(c) Guo Theorem 4.5 (CITED) in the form Ãg = Xℓ with ℓ = Ψ_f, X = X_∞+X_≤+X_>+X_Π. Term by term from (4.8) and
(4.7), for x ∈ I: X_∞ℓ(x) = ∫_{−∞}^{−a}ν(x−y)ℓ(y)dy = −[archimedean part of Wℓ](x) (the terms 2ℓ(x), ℓ(x+t) vanish
on I); (X_≤+X_>)ℓ(x) = Σ_q c_qℓ(x−log q) = −[prime part of Wℓ](x) (ℓ(x+log q) = 0); X_Πℓ = −[pole part of Wℓ].
Hence Xℓ = −(WΨ_f)|_I and W_T(g) = ⟨g, Ãg⟩ = −⟨g, WΨ_f⟩ = −𝒲(g,Ψ_f), where g is extended by zero.
(d) By (b), 0 = ∫_{−∞}^{−a}Ψ̄_f·WΦ_f = ∫Ψ̄_f W(Φ_f 1_I) + ∫Ψ̄_f W(Ψ_f) = 𝒲(Ψ_f,g) + 𝒲_ext[Ψ_f]; splitting is
legitimate because each of the two integrals converges absolutely (bounds listed above; for the Lévy cross term
∫∫_{x>−a>y}|g(x)||Ψ(y)|ν(x−y) < ∞ since g,Ψ are bounded near −a and ∫_0^1∫_0^1 ds dt/(s+t) < ∞; for the self term,
Ψ is Lipschitz). (e) 𝒲(Ψ_f,g) = 𝒲(g,Ψ_f) by the symmetry of the kernel for real functions. Combining (c)–(e):
W_T(g) = −𝒲(g,Ψ_f) = 𝒲_ext[Ψ_f]. □

**Remarks.** (i) Theorem 1.1 is a quadratic restatement of Guo's Theorem 4.5: for a full-line vector Φ in the
radical of 𝒲 (WΦ = 0), Φ = Φ_I + Φ_ext gives 𝒲(Φ_I) = 𝒲(Φ_ext) = −𝒲(Φ_I,Φ_ext). The whole content of W_T on
E(core) is the Weil form of the *below-window* piece of the summation image. (ii) By Poisson (Guo (4.6)),
Ψ_f(y) = e^{−y/2}Σ_n r_f(ne^{−y}) for y < −a (every ne^{−y} > λ): Ψ_f = Z r_f with Guo's map Z, so the right-hand
side depends on f only through r_f (Guo Rem 4.6(i)). With w = e^{−y} > λ: Ψ_f = (E_∞ r_f)(w) = w^{1/2}Σ_n r_f(nw),
the **same summation map applied to the out-of-band function on (λ,∞)** (full sum, convergent since r_f = O(ξ^{−2})
by Guo Lemma 4.3). (iii) Complex f: W_T and 𝒲_ext are real forms, so both sides split as Re + Im parts; L′♯ for
complex g follows from the real case with κ/2 (‖a+ib‖² ≤ 2‖a‖²+2‖b‖² for the leakages). (iv) The hypothesis
f(λ) = 0 is forced on the core: g(a−) = λ^{1/2}f(λ) and jumps of size (λ/n)^{1/2}f(λ) at x_n = log(λ/n) (Guo Lemma
4.2), so g continuous with g(T) = 0 ⟺ f(λ) = 0, for every representative. For f(λ) ≠ 0 Guo's p_λ-subtraction gives
W_T(g) = 𝒲_ext[Ψ_v] + 2f(λ)Re⟨h_p, XΨ_v⟩ + f(λ)²W_T(h_p), v = f − f(λ)p_λ, h_p = E p_λ|_I (PROVED from Thm 4.5 by
polarisation, using ⟨Φ_I,Ãh_p⟩ = ⟨ÃΦ_I,h_p⟩); the rank-one β-block is not needed below.

## 2. The gauge is the radical; ℓ(g) is a squared distance

**Gauge.** 𝒢₀ := {φ ∈ C²(ℝ) even, supp φ ⊂ [−1/λ,1/λ], φ(0) = φ̂(0) = 0}. For admissible f and φ ∈ 𝒢₀, f+φ is
admissible, E(f+φ) = Ef on [1/λ,λ] (MECH Prop 3.1, PROVED), and (f+φ)(λ) = f(λ). Conversely two admissible
representatives of the same g differ by an element of 𝒢₀ (Prop 3.1: f is determined on [1/λ,λ]).

**Proposition 2.1 (gauge = radical; PROVED).** For φ ∈ 𝒢₀: (a) Φ_φ := Eφ(e^x) is supported in (−∞,−a] and
WΦ_φ = 0 a.e.; (b) Ψ_{f+φ} = Ψ_f + Φ_φ and 𝒲_ext[Ψ_f+Φ_φ] = 𝒲_ext[Ψ_f]; (c) in terms of out-of-band data,
r_{f+φ} = r_f + (1−P_λ)φ̂, and
  ℓ(g) = dist²(r_f, 𝒢̄) in L²(|ξ|>λ),  𝒢̄ := closure of {(1−P_λ)φ̂ : φ ∈ 𝒢₀}.
*Proof.* (a) ne^x ≥ e^x > 1/λ for x > −a, so Φ_φ(x) = 0 there; φ ∈ G_λ with φ(λ) = 0, so Guo Lemma 4.4 applies.
(b) Linearity of E; then 𝒲_ext[Ψ+Φ_φ] = 𝒲_ext[Ψ] + 2𝒲(Ψ,Φ_φ) + 𝒲_ext[Φ_φ] and both extra terms are ∫(·)·WΦ_φ = 0
(absolute convergence as in Thm 1.1(d)). (c) leak(f+φ) = ‖r_f + (1−P_λ)φ̂‖²; the infimum over φ ∈ 𝒢₀ is the
squared distance to the closure. □

**Remark 2.2.** (1−P_λ) is injective on {φ̂ : φ ∈ 𝒢₀} (a compactly supported band-limited function vanishes), and
Φ_φ = Z((1−P_λ)φ̂) on (−∞,−a). So the gauge directions are exactly the *full-line radical vectors* Eφ of the
classical Connes–Consani observation (Mellin ζ(s)M_φ(s)), those whose support lies entirely below the window.
Theorem 1.1 and Prop 2.1 together say: W_T on E(core) is the quotient form of 𝒲_ext on the space
𝒱 := {Ψ_f} by its radical sub-space 𝓡 := {Φ_φ : φ ∈ 𝒢₀}.

## 3. L′♯ as a half-line coercivity statement

**Theorem 3.1 (reformulation; PROVED).** L′♯ (for real g in the core, hence for all g by Rem 1.1(iii)) is
equivalent to: ∃κ, A: ∀μ ≥ 5, ∀f admissible real with f(λ) = 0,
  (L_ext)   𝒲_ext[Z r_f] ≥ κμ^{−A}·dist²(r_f, 𝒢̄).
*Proof.* Thm 1.1 + Prop 2.1(c). □

**3.2 The structure of 𝒲_ext on Z-images (PROVED, elementary).** Write x = −y > a, r̃(x) := e^{x/2}r(e^x) (so
‖r̃‖²_{L²(a,∞)} = ∫_λ^∞|r|²dξ = ½leak(f)), and Ψ̌(x) := Ψ(−x). Then
  Ψ̌ = Σ_{n≥1} n^{−1/2} (S_{−log n} r̃)|_{(a,∞)},  (S_{−log n}r̃)(x) = r̃(x+log n),
and by the reflection symmetry of W (ν, c_q-terms, cosh are even) 𝒲_ext[Ψ] = 𝒲_{(a,∞)}[Ψ̌]. The Mellin transform
H_Ψ(s) = ∫Ψ(y)e^{(s−½)y}dy equals
  H_Ψ(s) = Σ_{n≥1} n^{s−1} R_{nλ}(s),  R_c(s) := ∫_c^∞ r(ξ)ξ^{−s}dξ   (Re s > −1),
NOT ζ(1−s)R_λ(s): the n-th dilate is truncated at ξ = nλ. The untruncated sum Ψ_full := Σ_n n^{−1/2}S_{−log n}r̃ on
all of ℝ has Mellin 2ζ(1−s)R_λ(s) on −1 < Re s < 0 (pole at s = 0 unless R_λ(0) = ½∫_{|ξ|>λ}f̂ = −½∫_{|ξ|<λ}f̂ = 0)
and Ψ_full = Ψ̌ on (a,∞), Ψ_full = Φ_f(−x) − E(P_λf̂)(e^x) on x < a. So **all of W_T(g) is a truncation
(boundary) effect at x = a**: on the untruncated object, the formal symbol of the Weil distribution vanishes
(Rem 3.3), consistently with WΦ_f = 0.

**Remark 3.3 (the formal symbol; PROVED identity, classical).** From ξ(s) = ξ(1−s) at s = ½+it:
Θ_∞(t) + 2Re(ζ′/ζ)(½+it) = 0 wherever ζ(½+it) ≠ 0 (Guo's Θ_∞ = Re(Γ′/Γ)(¼+it/2) − log π; the two Γ-terms combine
to Re(Γ′/Γ)(¼+it/2) because (1−s)/2 = \overline{s/2}). Since −2Σ_q c_q cos(t log q) = 2Re(ζ′/ζ)(½+it) formally,
the formal symbol Θ_∞ − 2Σ_{all q}c_q cos(t log q) of W (without the pole term) is 0 off the zeros: W is a sum of
point masses at the zeros (Guo (2.10): WΦ(x) = Σ_ρ H_Φ(ρ)e^{(½−ρ)x}). Hence no symbol calculus, exact or
approximate, can see the sign of 𝒲_ext[Ψ̌]: the sign sits in the truncation at x = a (the "n ≈ λ/u" boundary of
the summation, i.e. the m ≈ kn interaction of the semiring principle).

**3.4 Prolate coordinates (PROVED reformulation).** Let ψ_k = ψ_{k,λ} (k even) be the prolate functions on [−λ,λ]
with concentrations χ_k = λ_k(2πμ), r_k := (1−P_λ)ψ̂_k (orthogonal, ‖r_k‖² = 1−χ_k, Guo (3.5)). For f = Σ a_kψ_k:
leak(f) = Σ|a_k|²(1−χ_k) =: a^TDa; the admissibility constraints are three linear forms, Σa_kψ_k(0) = 0,
Σa_kκ_kψ_k(0) = 0 (f̂(0)), Σa_kψ_k(λ) = 0; the quadratic form is a^T𝔐a with
  𝔐_{jk} := W_T(Eψ_j, Eψ_k) = ⟨Eψ_j, ÃEψ_k⟩  (well defined: Eψ_k ∈ Dom(Ã), Guo Lemma 4.2),
and the gauge is B := {b : Σb_kψ_k ∈ 𝒢₀}. Then (L_ext) reads
  (★)   a^T𝔐a ≥ κμ^{−A}·inf_{b∈B̄}(a+b)^TD(a+b)   for all a in the constraint space 𝒦.
This is the "inequality on prolate matrix elements" asked for: 𝔐 ⪰ κμ^{−A}D_B on 𝒦, D_B the D-distance-squared
to the gauge. (★) is OPEN. What is known about 𝔐 is one-sided and only on Guo's finite blocks:

**Lemma 3.5 (upper side; CITED, Guo Thm 1.6 + Lemma 4.1).** For m ≥ 1, λ ≥ Λ^{tr}_m and f, f′ ∈ F_{λ,m}
(span of ψ_0, ψ_4, …, ψ_{4m+4} with f(0) = f̂(0) = 0): |W_T(Ef, Ef′)| ≤ 2√λ‖f‖ · C_mλ⁵‖D_λf′‖ ≤ 2C_mλ^{11/2}(1−χ_{4m+4})^{1/2}‖f‖‖f′‖.
So on these blocks 𝔐 is dominated by D^{1/2} (linear in the leakage amplitude), while (★) asks for a lower bound by
D (quadratic): Guo §10.1's square-root gap. Lemma 3.5 is consistent with (★) for any A ≥ 0 and shows that the
scale μ^{−A}(1−χ_k) is the only one compatible with both sides at the bottom (AUDIT_199 (e)). It is not a step
towards the lower bound.

## 4. What can be proved: the comb-generic tail

Let 𝒜_T = S_λ = 2Σ_{q<μ}Λ(q)q^{−1/2} (Paper 47's total comb mass), C_∞ the constant of Guo Lemma 2.1
(|Θ_∞(t) − log(2+|t|)| ≤ C_∞), K := C_∞ + 𝒜_T, and Ω_* := e^{K+λ+1} − 2. For g ∈ L²(I) let P_< g̃ be the part of
the Fourier transform Fg̃ on |t| < Ω_* (Plancherel, F unitary).

**Lemma 4.1 (high-frequency coercivity; PROVED, comb-generic).** For every g ∈ Dom(W_T):
  W_T(g) ≥ ‖g‖² − (K+λ+1)‖P_<g̃‖².
*Proof.* Θ_λ(t) = Θ_∞(t) − 2Σ_{q<μ}c_q cos(t log q) ≥ log(2+|t|) − K, so Θ_λ ≥ λ+1 for |t| ≥ Ω_* and Θ_λ ≥ −K
everywhere. The pole operator Π has eigenvalues 2(a+sinh a) and −2(sinh a − a) (Guo (2.4)), so ⟨g,Πg⟩ ≥ −λ‖g‖²
(2 sinh a = λ − 1/λ). Hence W_T(g) ≥ (λ+1)‖P_>g̃‖² − K‖P_<g̃‖² − λ‖g‖² = ‖P_>g̃‖² − (K+λ)‖P_<g̃‖². □

**Lemma 4.2 (ℓ(g) is at most polynomially larger than ‖g‖²; PROVED).** Fix an even B ∈ C²_c(−1,1) with B(0) = 0 and
∫B = 1, and put c_B = ‖B‖². For every g in the core (g ∈ C², vanishing to second order at ±T):
  ℓ(g) ≤ 4μ(1 + 4μc_B)‖g‖² ≤ C₀μ²‖g‖²,  C₀ := 4(1/5 + 4c_B)  (μ ≥ 5).
*Proof.* f₁ := E^{−1}g on [1/λ,λ] (even extension), ‖f₁‖ ≤ 2√μ‖g‖ (MECH Prop 3.1), f₁ ∈ C² with f₁(λ) = 0 (AUDIT
(c)). Admissible representative: f = f₁ + φ_ε + b, where φ_ε is a C² patch of width ε at ±1/λ matching the two-jet of
f₁ (‖φ_ε‖ → 0 as ε → 0) and b(x) = −2λI₁B(2λx), I₁ := ∫f₁ + ∫φ_ε, supported in (−1/(2λ),1/(2λ)), so that f(0) = 0,
∫f = 0. |I₁| ≤ ‖f₁‖(2λ)^{1/2} + o(1), ‖b‖² = 2λI₁²c_B ≤ 4μc_B‖f₁‖² + o(1). Then ℓ(g) ≤ leak(f) ≤ ‖f‖² ≤
(1+4μc_B)‖f₁‖² + o(1). □

**Corollary 4.3 (L′♯ on the high-frequency subspace; PROVED, comb-generic).** On
𝒯_* := {g ∈ E(core) : ‖P_<g̃‖² ≤ ‖g‖²/(2(K+λ+1))}, W_T(g) ≥ ½‖g‖² ≥ (2C₀)^{−1}μ^{−2}ℓ(g). So L′♯ holds on 𝒯_*
with A = 2 and κ = 1/(2C₀), and the constants do not depend on the comb beyond its mass 𝒜_T.

**4.4 The finite block that remains (PROVED statement; content OPEN).** L²(I) = 𝒯_* ∪ (complement); the complement is
contained in {g : ‖P_<g̃‖² > ‖g‖²/(2(K+λ+1))}, which by Landau's density theorem is, up to an O(1)-dimensional
slack, a subspace of dimension N_* ≈ (2/π)·T·Ω_* = (2/π)T e^{𝒜_T+λ+C_∞+1} (ARGUED for the exact dimension; the
bound ‖P_<‖ ≤ 1 and the Toeplitz eigenvalue count are classical). This is the Mori band Ω of MECH_001 §1 (S2:
Ω > 2πe^{γ} with γ ≥ 𝒜_T-floor) seen intrinsically, and it is superpolynomial in μ: N_* ≥ exp((8+o(1))√μ/log μ)
(MECH Prop 1.1(iii)). L′♯ is therefore **equivalent to (★) on this block**, and the block is exactly the part where
Lemma 4.1 says nothing.
In prolate terms (ARGUED, from the x-frequency ≈ πk/2 of the n ≈ λ/u terms of Eψ_k): E(span{ψ_k : k ≥ K_*}) lies in
a neighbourhood of 𝒯_* only for K_* ≳ (2/π)Ω_*; the prolate tail k ≥ k₀ ≈ 4μ where 1−χ_k ≥ ½ (Guo §10.3) is far
inside the block (2πμ ≪ e^{𝒜_T}). So the tail "k ≥ k₀ with 1−χ_k ≥ ½" asked for in the brief is NOT covered by the
comb-generic coercivity; what is covered is the much smaller tail k ≳ e^{𝒜_T+λ}. The jumps of Eψ_k at x_n (size
(λ/n)^{1/2}ψ_k(λ), ψ_k(λ) ≠ 0 by Guo (P3)) put energy ≈ k log μ/Ω_* below Ω_*, which is why no prolate tail with
k ≪ Ω_* can be put in 𝒯_* without the three constraints.

## 5. Attempted lower bounds for the finite block, and why each fails (ARGUED / NO-GO)
- **Diagonal first.** 𝔐_{kk} = W_T(Eψ_k) = 𝒲_ext[Zr_k] + (β-terms, ψ_k(λ) ≠ 0). No sign is available for a single
  Z-image: the explicit-formula representation 𝒲_ext[Ψ] = Σ_ρ H_Ψ(ρ)H_Ψ(1−ρ) with H_Ψ(ρ) = −H_{g}(ρ) is
  lem:roughEF again (zero data; not usable).
- **Bochner on the exterior form.** 𝒲_ext = b_∞‖·‖² + Lévy − primes + pole. The Lévy energy is ≥ 0, the pole term is
  indefinite (rank 2), b_∞ < 0, the prime term is indefinite. Any bound of the Lévy energy of Zr from below by
  ‖r‖² (Poincaré-type) plus Cauchy–Schwarz on the rest is TV-robust in the comb and therefore cannot give (★)
  (BARRIER_EST Thm 4 + B_001 Lemma 4.1): NO-GO as a class.
- **Möbius inversion of Z.** r(w) = Σ_m μ(m)(mw)^{−1/2}Ψ̌(mw) (w > λ) inverts Z on the half-line, with norm ≤ Σ_m
  m^{−1/2}·(decay) — polynomial in λ. This converts (★) into a statement about 𝒲_{(a,∞)} on all half-line
  functions of the form Z(r) with r ∈ dist-complement of 𝒢̄; it does not produce a sign (identity, N_018).
- **Self-similarity.** Ψ̌ = E_∞ r on (λ,∞) has the same shape as g = Ef on [1/λ,λ]; applying Thm 1.1 again needs a
  compactly supported object and r is not compactly supported. No recursion.

## 6. Where Λ is used (constraint (iii) of the brief)
| step | holds for cΛ? | a_P? | Beurling B? | F-DH? | verdict |
|---|---|---|---|---|---|
| Thm 1.1 (WΦ_f = 0 ⇒ half-line identity) | NO with E; YES with the weighted map E_c f = u^{1/2}Σd_c(n)f(nu) (Dirichlet series ζ^c) | YES with E over P-free integers | YES with E_B over B-integers | YES in the conductor-rescaled, pole-free form (AUDIT (d)) | multiplicative-generic: uses only "Mellin(EΦ) = ζ_a·M_f" |
| Poisson: Ψ_f = Zr_f (exterior tail = aliasing of the out-of-band data), size O(e^{3y/2}) | NO (Σd_c(n)f(nu) has no cancellation; tail O(u^{−1/2}log^{c−1})) | NO (P-free integers are not a lattice) | NO | YES (Gauss sums, mod 5) | additive-specific; selects lattices |
| Prop 2.1 (gauge = radical) | as Thm 1.1 | as Thm 1.1 | as Thm 1.1 | yes | multiplicative-generic |
| Lemma 4.1 (tail) | YES | YES | YES | YES | comb-generic |
| (★) finite block | FALSE (certified λ^W < 0) | FALSE | FALSE (NUMÉRICO) | FALSE (Ziad, UNVERIFIED) | the Λ-step; OPEN |
Conclusion (PROVED, by the table): every step proved in this memo survives at least one falsifier, so none is
decisive. The step that must carry Λ exactly is (★), and the table says *how*: the identity needs the
multiplicative monoid (E, Möbius), the smallness of the exterior data needs the additive lattice (Poisson), and (★)
asks for a sign of the truncation defect at the boundary n ≈ λ/u where both act on the same integers — the semiring
principle, stated for this object. (★) must fail for F-DH, which has both structures but conductor 5 and no pole;
so the proof of (★) must use conductor 1 / the pole term 2Re(AB̄) of 𝒲_ext (the only term of 𝒲_ext that
distinguishes ζ from DH at this level), or the positivity Λ ≥ 0 on prime powers.

## 7. Labels and verdict
- **PROVED:** Thm 1.1 (half-line identity, incl. convergence), Prop 2.1 (gauge = radical, ℓ = dist²), Thm 3.1
  (reformulation (L_ext)), §3.2 (Mellin structure, truncation), Rem 3.3 (symbol identity), Lemma 4.1, Lemma 4.2,
  Cor 4.3 (L′♯ on 𝒯_* with A = 2), the table of §6.
- **CITED:** Guo Lemmas 2.1–2.6, 4.2–4.4, Thm 4.5, Thm 1.6, (3.5), (P3); Paper 47 def of W_T; Mori Thm N (not
  needed here).
- **ARGUED:** dimension N_* of the finite block; prolate index K_* ≈ (2/π)Ω_*.
- **NO-GO (class):** Bochner/C–S bounds of 𝒲_ext (TV-robust); Möbius inversion alone (N_018).
- **OPEN:** (★) on the finite block, equivalently L′♯. No sign is claimed. Row D OPEN.
- **Not done:** no coercivity for the prolate tail k ≥ k₀ (1−χ_k ≥ ½); §4.4 shows that tail is inside the block.

**Verdict.** Strategy A yields the exact object behind L′♯ — the complete Weil form on a half-line evaluated on the
aliasing tail Zr of the out-of-band data, modulo the radical vectors Eφ — and a comb-generic proof of L′♯ only
beyond frequency e^{𝒜_T+λ}. The remaining block has superpolynomial dimension and is the whole problem. Nothing in
this memo should be retried as a sign source; the object (𝒲_ext on Z-images, (★)) is recorded as a REF-D target.
