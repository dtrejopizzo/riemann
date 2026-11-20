# Round 009 B — The Fourier-class selection rule on the exterior test space, and the lower half in the self-dual sector

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Object: a_T = W_T on P_T = {F ∈ L²(I_T) : A(F) = B(F) = 0},
λ_A(T) = inf a_T on unit vectors of P_T. Notation of ROUND_008_E and Paper 47 §sec:ext: λ = e^T, N = λ², c = 2πN,
ℱf(ξ) = ∫f(x)e^{−2πixξ}dx, E the summation map Ef(x) = e^{x/2}Σ_{n≥1}f(ne^x) on I_T, Π_T the orthogonal projector of
L²(I_T) onto P_T, R the reflection RF(x) = F(−x), P_± = (I ± R)/2 the parity projectors. ψ_k = k-th prolate of [−λ, λ] at
c = 2πN, restricted to [−λ, λ] and normalised in L²; χ_k = χ_k(c) its concentration, d_k := 1 − χ_k. For even k,
ℱ(ψ_k) = i^k√χ_k ψ_k on the band [−λ, λ] (Slepian–Pollak, CITED; c = 2πλ·λ makes time and band intervals equal), and
ℱ(ψ_k) is orthogonal to every function supported in the band off its band part (double orthogonality, CITED). Class of an
even k: ε_k := i^k = +1 for k ≡ 0 (mod 4), −1 for k ≡ 2 (mod 4). The test space of def:ext consists of even f, so only
even k occur. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Searched: ROUTES-TRIED-INDEX README rows P211-2B, P211-3A, P211-4A, P211-7D, P211-8E, 05b row L106; phase 199
proof-L-sharp memos T_001, U_001, V_001 (Strategy V, Fourier-sector reduction of L′♯), S_001, MORI15_EXTREMAL_001,
AUDIT_L_SHARP_5; ROUND_001_B (Thm 1.1, Cor 1.2, Prop 1.3), ROUND_008_E (§2.2(ii)–(iii), Lemma 4.3, Prop 5.1), REVIEW_006
§1 remark (a), ROUND_009_A (mollified prolates); Paper 47 prop:ext-consol(b), prob:ext-L, thm:ext-half.

What is on record about the selection rule.
- V_001, V.1.4 (PROVED there): for admissible f, Φ_{ℱf} = Φ_f∘R on the full line, so the standard ℱ is the
  window-centre reflection; the near self-duality of the extremal f* is the window parity of g* transported by Poisson,
  "up to the out-of-band tail r* (ARGUED; quantitative bound not written)".
- V_001, V.1.3 (PROVED there, NO-GO as posed): the exact ℱ-eigen-sectors f_± = (f ± ℱf)/2 are never carrier data, the
  gauge-minimised leakage ℓ does not split by sectors, and λ_A ≠ min(λ_+, λ_−). So a reduction of prob:ext-L to exact
  ℱ-eigen-sectors is closed.
- ROUND_008_E §2.2(ii) (NUMERICAL) and REVIEW_006 §1(a): only ψ_0, ψ_4, ψ_8 enter the even sector, to precision 10⁻⁴;
  the transfer to ℱ-even prolates "fails off the band by O((1 − χ_k)^{1/2}); a numerical statement, not a structural
  one; ARGUED".
- P211-2B: no sign statement on the prolate sector at orders log N and 1 (do not retry); P211-3A: a_T commutes with
  parity on P_T.

What differs here, and why it avoids the recorded failures.
(i) The classes are prolate-index classes (k mod 4), not exact ℱ-eigen-sectors: every ψ_k is carrier data (support in
[−λ, λ]), so the obstruction V.1.3(a) does not apply; the price is a defect, and the defect is computed exactly.
(ii) The parity defect is an exact identity inside P_T (Theorem 1.1): Π_T removes the two Poisson boundary terms
exactly because span{e^{±x/2}} is R-invariant, so the "up to the tail" of V.1.4 becomes an identity with an explicit
remainder; together with the exact diagonal form of the Fourier defect on prolates (Theorem 1.2) this turns the
numerical statement of ROUND_008_E §2.2 into a proved one.
(iii) No splitting of ℓ is claimed (V.1.3(b) stands): the lower-half analysis of §2 uses the plain prolate leakage
D = diag(d_k) on the class-(+1) span at fixed representatives, and isolates where the gauge re-enters (the high range).
(iv) No sign is extracted from Poisson symmetry; the falsifier section shows that the class–parity intertwining is
Λ-free and therefore cannot be a sign step, and locates the Λ-specific part in the near-nullity of the self-dual class.
No equivalence of (★) with another statement is used; no zero data are used.

## 1. The selection rule

### 1.0 Poisson in window coordinates
For f even, C¹ on ℝ, supp f ⊂ [−λ, λ] (so ℱf = O(ξ^{−2})), Poisson summation Σ_{n∈ℤ}f(nu) = u^{−1}Σ_{k∈ℤ}ℱf(k/u) at
u = e^x gives, for every x,
    Ef(x) = (Eℱf)(−x) + ½ℱf(0)e^{−x/2} − ½f(0)e^{x/2},        (Eh)(x) := e^{x/2}Σ_{n≥1}h(ne^x),            (1.0)
both series absolutely convergent. (This is V.1.4 / def:ext in the present coordinates; PROVED, standard.)

### Theorem 1.1 (exact parity defect; PROVED)
For f as in 1.0 and ε ∈ {+1, −1},
    P_{−ε} Π_T E f = ½ R Π_T E(ℱf − εf),       equivalently   Π_T Ef − εRΠ_T Ef = RΠ_T E(ℱf − εf).
*Proof.* Write ℱf = εf + h, h := ℱf − εf. By (1.0) and linearity of E, Ef = εR(Ef) + R(Eh) + τ with
τ := ½ℱf(0)e^{−x/2} − ½f(0)e^{x/2} ∈ span{e^{x/2}, e^{−x/2}} =: 𝒯. 𝒯 is R-invariant, so its orthogonal complement P_T is
R-invariant and Π_T commutes with R; Π_T τ = 0. Apply Π_T: Π_TEf = εRΠ_TEf + RΠ_TEh. Then
P_{−ε}Π_TEf = ½(Π_TEf − εRΠ_TEf) = ½RΠ_TEh. ∎

So the wrong-parity part of Π_TEf is the E-image of the Fourier defect h, with no boundary term: the two Poisson terms,
which are O(1) (ψ_k(0) ≠ 0), are exactly the part removed by the Tate projection.

### Theorem 1.2 (the Fourier defect is diagonal in the prolates; PROVED, given the two CITED prolate facts)
For f = Σ_{k even} a_k ψ_k (finite sum, real a_k), ‖ℱf − εf‖²_{L²(ℝ)} = Σ_k 2(1 − ε ε_k √χ_k) a_k².
In particular on class ε the eigenvalue is 2(1 − √χ_k) = 2d_k/(1 + √χ_k) ∈ [d_k, 2d_k], and on the opposite class it is
2(1 + √χ_k) ∈ [2, 4]. Splitting into band and out-of-band parts: ‖(ℱf − εf)1_{|ξ|≤λ}‖² = Σ(ε_k√χ_k − ε)²a_k² and
‖ℱf 1_{|ξ|>λ}‖² = Σ d_k a_k².
*Proof.* ‖ℱf − εf‖² = ‖ℱf‖² + ‖f‖² − 2ε⟨ℱf, f⟩ = 2Σa_k² − 2εΣ_{j,k}a_ja_k⟨ℱψ_j, ψ_k⟩ (Plancherel; orthonormality of ψ_k on
[−λ, λ]). Since ψ_k is supported in the band, ⟨ℱψ_j, ψ_k⟩ = ⟨(ℱψ_j)1_{band}, ψ_k⟩ = ε_j√χ_j δ_{jk}. The band/off-band split
is the same computation with ‖ℱψ_j 1_{band}‖² = χ_j and orthogonality of the off-band parts (double orthogonality). ∎

### Lemma 1.3 (L² size of the summation image; PROVED)
For s ∈ (½, 1] and h even, locally integrable with ∫_{1/λ}^∞ u^{2s}|h(u)|²du < ∞,
    ‖Eh‖²_{L²(I_T)} ≤ ζ(2s) λ^{2s} ∫_{1/λ}^∞ u^{2s}|h(u)|² du.
*Proof.* With v = e^x, ‖Eh‖² = ∫_{1/λ}^{λ}|Σ_n h(nv)|²dv ≤ ζ(2s)∫Σ_n n^{2s}|h(nv)|²dv (Cauchy–Schwarz with weights n^{∓s})
= ζ(2s)Σ_n n^{2s−1}∫_{n/λ}^{nλ}|h(u)|²du ≤ ζ(2s)∫_{1/λ}^∞|h(u)|²Σ_{n≤uλ}n^{2s−1}du, and Σ_{n≤X}n^{2s−1} ≤ X^{2s}. ∎

### Corollary 1.4 (selection rule, quantitative; PROVED for C¹ data)
For f even, C¹, supp f ⊂ [−λ, λ], and ε = ±1,
    ‖P_{−ε}Π_TEf‖ ≤ ½‖Eh‖ ≤ ½ζ(2)^{1/2}λ·(λ‖(ℱf − εf)1_{|ξ|≤λ}‖ + ‖ξ ℱf 1_{|ξ|>λ}‖),     h = ℱf − εf,
(Theorem 1.1, Lemma 1.3 with s = 1, ‖Π_T‖ = ‖R‖ = 1; norms on ℝ, the factor ½ from evenness absorbed). For f = Σa_kψ_k
in class ε (mollified as in ROUND_009_A so that the weighted out-of-band norm is finite): the band term is
(Σ(1 − √χ_k)²a_k²)^{1/2} ≤ (Σd_k²a_k²)^{1/2}, and the out-of-band term is the weighted leakage, which ROUND_009_A bounds by
poly(N)·(Σd_ka_k²)^{1/2}. So the wrong-parity part of a class-ε image is O(poly(N)·√(max d_k)). For the raw prolates (edge
jump, ℱψ_k ≍ 1/ξ off the band) the weighted norm with s > ½ is infinite and the corollary does not apply as stated; the
NUMERICAL check below shows the true ratio is O(1)·√d_k with no polynomial loss.

NUMERICAL check (tools/prolate_sector.py + prolate_sector_anal.py; T = 0.8/1.0/1.2 with Nb = 90/160/180 sines, 40/40/80
digits; g_k = Π_TEψ_k): ρ_k := ‖P_{−ε_k}g_k‖/√d_k lies in
  [0.46, 0.64] (T = 0.8, k ≤ 18 = 0.9·4N),  [0.61, 0.74] (T = 1.0, k ≤ 26),  [0.67, 0.90] (T = 1.2, k ≤ 40),
uniformly from d_k ≈ 10⁻⁶⁰ (k = 0, T = 1.2) to d_k ≈ 10⁻¹; for k ≥ 4N (d_k ≈ 1) it is ≈ 1 (no selection). With ‖g_k‖ ≈ 0.1–1.7,
this is the bound ½‖E(ℱψ_k − εψ_k)‖ with ‖ℱψ_k − εψ_k‖ = (2(1 − √χ_k))^{1/2} ≈ √d_k (Theorem 1.2) and an E-amplification
≈ 1.0–1.6. The quotient a_T(P_{−ε}g_k)/‖P_{−ε}g_k‖² is 1.7–2.5 for k < 4N: the wrong-parity remnant is not near-null.

### Theorem 1.5 (decoupling of the two classes in the even sector; PROVED, with the bilinear bounds of Lemma 1.6)
Let f_+ be in the class-(+1) span and admissible with A(Ef_+) = B(Ef_+) = 0 (so Ef_+ ∈ P_T and the half-line identity
applies: W_T(Ef_+, G) = −𝒲(Ψ_{f_+}, G) for G ∈ P_T in the form domain, by ROUND_001_B Thm 1.1, Ef = Φ_f − Ψ_f on ℝ); let f_−
be in the class-(−1) span. Put h_± := ℱf_± ∓ f_± (Fourier defects), w_± := ½RΠ_TEh_±. Then in the even sector
    P_+Ef_+ = Ef_+ − w_+,     P_+Π_TEf_− = w_−,
    a_T(P_+Ef_+, P_+Π_TEf_−) = −𝒲(Ψ_{f_+}, w_−) − a_T(w_+, w_−).
*Proof.* Theorem 1.1 with ε = +1 for f_+ (P_−Ef_+ = w_+, and Ef_+ = Π_TEf_+) and ε = −1 for f_− (P_+Π_TEf_− = w_−). Then
a_T(Ef_+ − w_+, w_−) and the half-line identity for the first term (w_− ∈ P_T, w_− is the E-image of a C¹ function on
I_T, hence in the form domain). ∎
So every even-sector cross term between the classes is a product of two small factors: (exterior tail of f_+) × (Fourier
defect of f_−) plus (Fourier defect of f_+) × (Fourier defect of f_−). The diagonal blocks are
    a_T(P_+Ef_+) = 𝒲[Ψ_{f_+}] − 2a_T(Ef_+, w_+) + a_T(w_+) = 𝒲[Ψ_{f_+}] + 2𝒲(Ψ_{f_+}, w_+) + a_T(w_+),
    a_T(P_+Π_TEf_−) = a_T(w_−)  (size ≍ ‖w_−‖² ≍ defect of f_−, NUMERICAL quotient 1.7–2.5).

### Lemma 1.6 (bilinear bounds; PROVED, elementary)
(a) For Ψ supported in (−∞, −T], bounded, with ‖Ψ‖_{L²(−∞,−T−u)} ≤ Me^{−u} (u ≥ 0), and w ∈ P_T bounded:
|𝒲(Ψ, w)| ≤ ¾‖Ψ‖_∞‖w‖_∞ + (0.7 + C√N)‖w‖(‖Ψ‖ + M), C absolute. Proof: the pole terms vanish
(A(w) = B(w) = 0 and w is supported in I_T, so the line functionals of w are those of P_T); ⟨Ψ, w⟩ = 0 and the Lévy form
gives Arch(Ψ, w) = −∫_0^∞c^{sym}_{Ψ,w}(u)K(u)du with |c^{sym}(u)| ≤ ½u‖Ψ‖_∞‖w‖_∞ (overlap of length ≤ u) and
|c^{sym}(u)| ≤ ½‖Ψ‖‖w‖; K(u) ≤ 1/u + ½ on (0, 1] and ∫_1^∞K = Ktail(1) < 1.4; so |Arch(Ψ, w)| ≤ ¾‖Ψ‖_∞‖w‖_∞ +
0.7‖Ψ‖‖w‖. The comb pairing at log n reads Ψ on [−T − log n, T − log n] ∩ (−∞, −T], whose L²-mass is ≤ ‖Ψ‖ for n ≤ N and
≤ Me^{−(log n − 2T)} = MN/n for n > N; hence |𝒫_Λ(Ψ, w)| ≤ ½‖w‖(‖Ψ‖Σ_{n≤N}v_n + MNΣ_{n>N}v_n/n) ≤ C√N‖w‖(‖Ψ‖ + M).
(b) For u, w in the form domain of P_T: |a_T(u, w)| ≤ (|C_0| + Σ_{n<N}v_n)‖u‖‖w‖ + ∫_0^{2T}|c_u(0) − c^{sym}_{u,w}(u′)|…;
the clean statement used is |a_T(u, w)| ≤ β_T‖u‖_{H¹(I_T)}‖w‖_{H¹(I_T)} with β_T ≤ C(1 + T + √N) (Arch is dominated by the
H^{1/2+} norm with log weight, the comb by Σ_{n<N}v_n ≤ 4√N). Proof: the same Lévy-form estimate, with
|c(0) − c^{sym}(u)| ≤ u‖u′‖‖w‖ + u‖u‖‖w′‖ on (0, 1]. ∎
For f_+ ∈ 𝒜⁺_T the exterior tail Ψ_{f_+} satisfies ‖Ψ‖, M ≤ ζ(3/2)L₁(f_+)/λ and ‖Ψ‖_∞² ≤ 2‖Ψ‖‖Ψ′‖ ≤ Cλ^{−2}(L₁² + L₂²)
(ROUND_008_E Thm 3.1 (a)–(c)); ‖w_±‖ and ‖w_±‖_∞ are bounded through Lemma 1.3 by weighted Fourier defects (for ‖w‖_∞ and
‖w′‖ apply Lemma 1.3 to h and to uh′(u), since (Eh)′ = ½Eh + E(uh′)). So the cross terms of Theorem 1.5 are bounded by
    poly(N)·[(L₁(f_+) + L₂(f_+))·δ¹(f_−) + δ¹(f_+)·δ¹(f_−)],      δ¹(f) := weighted Fourier defect of order one,
and, on mollified prolate spans, δ¹(f_ε) ≤ poly(N)(Σ_{k∈class ε}d_ka_k²)^{1/2}, L₁ + L₂ ≤ poly(N)(Σd_ka_k²)^{1/2}
(ROUND_009_A). This is the requested "cross terms bounded by explicit defect products": of order poly(N)·√(d_j d_k).

### 1.7 Which class is near-null in the even sector, and why (PROVED reading of 1.1–1.5)
Poisson summation intertwines ℱ on the test space with the window reflection R on P_T (Theorem 1.1). A class-(+1) datum is
ℱ-invariant up to its defect, so its image is R-invariant (even) up to its defect; a class-(−1) datum is anti-invariant,
so its image is odd. In the even sector, therefore:
- class +1 contributes with full norm, and on admissible, Tate-constrained combinations the form value is the exterior
  value 𝒲[Ψ_{f_+}] + O(defect products), which is doubly-exponentially small (Theorem 3.1 of ROUND_008_E): near-null;
- class −1 contributes only through w_−, of norm ≍ (defect)^{1/2} and form quotient O(1): it is not near-null relative to
  its own norm, and a unit vector built from it needs coefficients of size (defect)^{−1/2}, at which point its form value
  is O(1).
In the odd sector the roles swap (class −1 near-null), which is the ROUND_008_E observation λ_A^odd ≈ κ₁₀(1 − χ_10)
with the odd class {2, 6, 10}. The count "two constraints absorb ψ_0, ψ_4, the survivor carries d_8" happens inside class
+1 only, which is why the sharp index is 8 and not 4 or 6.

## 2. The lower half in the self-dual sector

### 2.1 Setting (definitions)
Even sector, class +1: h_k := P_+Π_TEψ_k, k ∈ {0, 4, 8, …}. On coefficient vectors a, M(a) := a_T(Σa_kh_k) and
D(a) := Σd_ka_k² (the prolate leakage of f = Σa_kψ_k; exact by double orthogonality, Theorem 1.2). Low block L = {0, 4, 8},
mid range 12 ≤ k ≤ 4N, high range k > 4N. This is prop:ext-consol(b) restricted to class-(+1) data at fixed
representatives (no gauge infimum; see 2.4 for where the gauge re-enters).

### 2.2 Elimination of the constraint directions (PROVED, elementary)
On L the generalized eigenproblem M = αD has one small eigenvalue α_b (vector b, the survivor) and two huge ones (vectors
s₁, s₂: the directions that violate the two effective constraints, the symmetric admissibility f(0) + ℱf(0) = 0 and the
even Tate condition; P_T removes Tate only orthogonally, see ROUND_008_E §2.1). Let S = span{s₁, s₂} and for r ∈ R :=
span{b} ⊕ (mid ⊕ high) let s*(r) := −M_SS^{−1}M_Sr r be the M-minimising completion, M̃(r) := M(r + s*(r)) (Schur complement)
and D̂(r) := D(r + s*(r)).
**Lemma 2.1.** If M̃ ≥ κ̃D̂ on R and M ≥ α_S D on S with M_SS-orthogonality as above, then M ≥ ½min(κ̃, α_S)·D on R ⊕ S.
*Proof.* For x = r + s, M(x) = M̃(r) + M_SS[s − s*(r)] ≥ κ̃D̂(r) + α_SD(s − s*(r)) ≥ ½min(κ̃, α_S)D(x), since
D(x) ≤ 2D(r + s*(r)) + 2D(s − s*(r)). ∎
NUMERICAL: α_S = M/D on s₁, s₂ is 10¹³/10²³ (T = 0.8), 10²⁵/10³⁶ (T = 1.0), 10⁴⁴/10⁵⁶ (T = 1.2): these directions are
irrelevant to the bound; and D̂(e_k) = d_k to all printed digits for every k ≥ 12 (the completion does not move the leakage).

### 2.3 The coupling of the survivor to 12 ≤ k (NUMERICAL, tools/prolate_selfdual_schur.py)
γ_k := |M̃(b, e_k)|/√(D̂(b)d_k) (coupling measured against √(d_k · leakage of the survivor), and leak(b) = (0.45–0.46)·d_8
at all three T, so √(D̂(b)d_k) ≍ √(d_8d_k)); α_b := M̃(b)/D̂(b) (= κ₈-type constant of the survivor).
| T (4N) | α_b | γ_12 | γ_16 | γ_20 | γ_24 | γ_28 | max_{k>4N}γ_k | max_k γ_k²/(α_b·M̃_kk/D̂_kk) |
|---|---|---|---|---|---|---|---|---|
| 0.8 (19.8) | 3.50 | 1.42 | 0.73 | 0.026 | 0.11 | 0.067 | 0.13 | 0.18 |
| 1.0 (29.6) | 4.72 | 1.61 | 1.21 | 0.82 | 0.35 | 0.072 | 0.12 | 0.12 |
| 1.2 (44.1) | 7.53 | 3.65 | 1.81 | 0.44 | 0.29 | 0.28 | 0.07 | 0.24 |
Reading. The coupling is O(√(d_kd_8)) uniformly in k at each T, with the constant concentrated on the first two mid
indices (k = 12, 16) and ≤ 0.3 beyond k = 20; it is ≤ 0.13 throughout the high range. The constant grows with T at the
same rate as α_b, i.e. the normalised coupling γ_k²/(α_b α_k) stays ≤ 0.24. The answer to the question "is the coupling
O(√(d_kd_8)) uniformly" is: yes in k at fixed T; in T it is O(√(α_bα_k)·√(d_kd_8)), with α_b ≍ N^{0.6–0.9} on this range.

### 2.4 The Schur argument and where it stops
**Proposition 2.2 (two-level and three-level Schur bounds; PROVED, elementary).** Let H ⊂ R \ {b}, α_H := gen-min of
(M̃_HH, D̂_HH), Γ := ‖D̂_HH^{−1/2}M̃_{Hb}‖/D̂(b)^{1/2}. Then on span{b} ⊕ H, M̃ ≥ κ D̂ with κ = smallest root of
(α_b − κ)(α_H − κ) = Γ², which is > 0 iff Γ² < α_bα_H. The same holds with b replaced by any block LM (κ_LM its gen-min)
and Γ by the D̂-normalised operator norm of the LM–H coupling.
*Proof.* In D̂-normalised coordinates the matrix is [[α_b + P, x],[xᵀ, Q]] with P ≥ 0, Q ≥ α_H, ‖x‖ = Γ; its least
eigenvalue is ≥ that of [[α_b, Γ],[Γ, α_H]]. ∎
Combined with Lemma 2.1 and the index floor: on the constrained class-(+1) span, D ≥ d_8|a_{≥8}|² and the two constraints
fix a_0, a_4 linearly in a_{≥8} (Lemma 4.3 of ROUND_008_E with q = 2 inside class +1), so
    M(a) ≥ ½min(κ, α_S)·d_8·|a|²/(1 + κ_C²),       κ_C := conditioning of the 2×2 constraint matrix on {ψ_0, ψ_4},
and with ‖Σa_kh_k‖² ≤ ‖Gram(h)‖·|a|²:
    a_T(F) ≥ [min(κ, α_S)/(2(1 + κ_C²)‖Gram‖)]·(1 − χ_8(2πN))·‖F‖²      for F in the class-(+1) image of k ≤ K.     (2.1)
This is the shape λ_A ≥ κ(1 − χ_8)N^{−b} on that subspace, PROVED as an implication from three finite-dimensional
quantities (κ, κ_C, ‖Gram‖); the index improvement over ROUND_008_E Lemma 4.3 (index 6 there) comes from the class
separation: inside class +1 the two effective constraints are carried by ψ_0, ψ_4, so the floor is d_8, not d_6.

NUMERICAL values of the Schur bound (true gen-min in the last column):
| T | two-level (b + H, H up to k): positive up to | three-level LM = b + {k ≤ 4N}: κ_LM | three-level positive up to | ratio Γ′²/(κ_LMα_HI) at the last positive k | gen-min at largest computed K |
|---|---|---|---|---|---|
| 0.8 | k = 20 (≈ 4N), bound 0.054 | 1.67 | k = 40 (2.0·4N), bound 0.072 | 0.38 | 0.118 (K = 40) |
| 1.0 | k = 32 (1.08·4N), bound 0.014 | 1.80 | k = 52 (1.76·4N), bound 0.019 | 0.90 | 0.207 (K = 52) |
| 1.2 | k = 40 (0.91·4N), bound 0.55 | 1.82 | k = 60 (1.36·4N), bound 0.091 | 0.77 | 0.186 (K = 64) |
Readings. (i) On the low and mid range (k ≤ 4N) the Schur argument closes at every tested T with κ_LM ≈ 1.7–1.8, flat in
T: the self-dual sector up to the prolate edge obeys M ≥ 1.7·D. (ii) It stops in the high range: α_HI (the gen-min of
the high block alone) decreases monotonically with K (0.80 → 0.12 at T = 0.8; 1.10 → 0.22 at T = 1.0; 1.52 → 0.28 at T = 1.2),
while the LM–HI coupling saturates (0.27, 0.60, 0.87). The true gen-min also decreases with K (0.12–0.21 at the largest K).
(iii) The decrease is forced, not a defect of the bound (ARGUED): for k > 4N, d_k ≈ 1, and the span of high-index even
prolates contains, as K → ∞, functions concentrated in (−1/λ, 1/λ), i.e. approximations of the gauge 𝒢_T, on which
E ≈ 0, hence M ≈ 0 while D ≈ 1. So with fixed representatives, inf M/D → 0 as K → ∞; the gauge infimum of prob:ext-L is
exactly the repair, and it is needed only in the high range.

### 2.5 The spectral law in the even sector (NUMERICAL)
The j-th even eigenvalue of a_T on P_T against d_{4j+8} (Galerkin, same matrices):
| T | λ_0/d_8 | λ_1/d_12 | λ_2/d_16 | λ_3/d_20 | λ_4/d_24 |
|---|---|---|---|---|---|
| 0.8 | 1.22 | 1.47 | 0.87 (k = 16 ≈ 0.8·4N) | 0.85 (d ≈ 1) | — |
| 1.0 | 1.50 | 1.55 | 1.32 | 1.27 | 1.09 |
| 1.2 | 1.73 | 2.00 | 1.94 | 1.39 | 1.77 |
So the whole bottom of the even sector, not only λ_A, follows λ_j^ev ≈ κ_j(1 − χ_{4j+8}(2πN)) with κ_j ∈ [0.85, 2.0], for
4j + 8 ≲ 4N: the low even spectrum of a_T is the class-(+1) prolate leakage shifted by two indices (the two constraints).
This is new data (ROUND_008_E had only j = 0); it supports reading (i) above: M ≈ (1–2)·D on the whole low range.

### 2.6 The remaining estimate (OPEN), named
(HR) High-range estimate in the self-dual sector. There are κ_H > 0 and b ≥ 0 such that for every T, with
LM := span{h_k : k ≡ 0 (4), k ≤ 4N} and HI its complement in the even sector of P_T (class −1 remnants included),
    (a) inf_{G ∈ HI} a_T(G)/ℓ_HI(G) ≥ κ_H N^{−b}, with ℓ_HI the gauge-minimised leakage of prob:ext-L restricted to HI;
    (b) the LM–HI coupling in D-normalised operator norm satisfies Γ′² ≤ (1 − η)κ_LM κ_H N^{−b}.
Together with (2.1) on LM (whose three constants are finite-dimensional and measured: κ_LM ≈ 1.7, κ_C, ‖Gram‖ polynomial
— κ_C and ‖Gram‖ not measured here), (HR) gives λ_A^ev ≥ κ(1 − χ_8)N^{−b′}. The odd sector is the same statement with
classes swapped and floor d_10. (HR)(a) is prob:ext-L itself on the high range, where 1 − χ_k ≈ 1: it is an O(1)-scale
positivity of the gauge-quotient form, not a doubly-exponential one, and the class structure plays no role there
(the selection rule is void for d_k ≈ 1, §1 NUMERICAL check). So the self-dual reduction moves the whole difficulty of
prob:ext-L to the range k > 4N, where Theorem F of P211-2A (floor on the complement of the negative Nyquist block) is the
nearest available tool; the two complements are different subspaces, and no comparison between them is proved here.

## 3. Falsifiers: the defect 𝒫_{Λ−w} breaks the selection of the bottom, not the class–parity rule

### 3.1 What is Λ-free (PROVED)
Theorems 1.1, 1.2, Lemma 1.3, Corollary 1.4 involve only E, ℱ, Π_T, the prolates: no weight. They hold verbatim for the
forms a^w_T of cΛ, a_P and finite modifications (the plain summation map E is the same). Theorem 1.5's decoupling identity
uses the half-line identity for the first cross term; for a weight w, by ROUND_008_E (5.1),
    a^w_T(P_+Ef_+, w_−) = −𝒲(Ψ_{f_+}, w_−) − a_T(w_+, w_−) + 𝒫_{Λ−w}(P_+Ef_+, w_−),
and the extra term is still a product with the small factor ‖w_−‖ (Fourier defect of f_−): the cross-class decoupling
survives every weight change. Therefore the class–parity rule is not a sign step and carries no information about Λ:
this is the falsifier test applied to §1, and §1 fails it, as a Λ-free statement must.

### 3.2 What breaks (PROVED identity + NUMERICAL size)
The near-nullity of the class-(+1) block. For f_+ admissible and Tate-constrained,
    a^w_T(Ef_+) = 𝒲[Ψ_{f_+}] + 𝒫_{Λ−w}[Ef_+]                    (ROUND_008_E (5.1), PROVED)
and the second term has no small factor: on the survivor vector F_b of the low block, Π_T(F_b) = 0.033 (T = 1), 0.015
(T = 1.2) (ROUND_008_E §5). So for w ≠ Λ the class-(+1) block is no longer near-null at scale d_8, the Schur picture of §2
(M ≍ D on LM) is destroyed at first order in ‖Λ − w‖, and the even-sector bottom leaves the class-(+1) low span:
| T | w | λ^ev(w) | angle(bottom, class-(+1) span k ≤ 8) | angle(bottom, class-(−1) span k ≤ 8) |
|---|---|---|---|---|
| 0.8 | Λ | 6.0·10⁻¹² | 2.9·10⁻⁴ | 1.571 |
| 0.8 | 0.99Λ | −2.3·10⁻³ | 0.057 | 1.567 |
| 0.8 | 1.01Λ | −7.5·10⁻³ | 0.78 | 1.561 |
| 0.8 | a_3 (prime 2 deleted) | −0.51 | 0.036 | — |
| 0.8 | Λ + 0.1v_2 at n = 2 | −0.057 | 0.46 | — |
| 1.0 | Λ | 1.6·10⁻²³ | 1.2·10⁻⁴ | 1.571 |
| 1.0 | 0.99Λ | −4.9·10⁻³ | 0.195 | 1.570 |
| 1.0 | 1.01Λ | −1.4·10⁻² | 1.42 | 1.569 |
| 1.0 | a_3 | −0.53 | 0.110 | — |
| 1.0 | Λ + 0.1v_2 | −0.067 | 0.84 | — |
| 1.2 | Λ | 1.0·10⁻⁴¹ | 1.1·10⁻⁴ | 1.571 |
| 1.2 | 0.99Λ | −7.1·10⁻³ | 0.221 | 1.570 |
| 1.2 | 1.01Λ | −1.9·10⁻² | 1.558 | 1.570 |
| 1.2 | a_3 | −0.54 | 0.178 | — |
| 1.2 | Λ + 0.1v_2 | −0.076 | 0.95 | — |
(tools/prolate_sector_fals.py.) Readings: (a) for every falsifier the bottom value leaves the doubly-exponential scale and
becomes negative; the angle to the class-(+1) span grows by 2–4 orders, up to essentially orthogonal (1.56 rad at 1.01Λ,
T = 1.2); (b) the angle to the class-(−1) span stays π/2 to 10⁻³ for every w: the class–parity rule (3.1) is untouched,
as proved. So the defect 𝒫_{Λ−w} breaks the selection of the bottom by the self-dual class, not the class–parity
intertwining.
(c) Beurling systems and the a_P-adapted summation map: here §1 itself fails. Theorem 1.1 rests on (1.0), Poisson over ℤ.
For the coprime-to-Q map (Q = ∏_{p<P}p), Σ_{(n,Q)=1}f(nu) = Σ_{d|Q}μ(d)Σ_{m≥1}f(dmu) and Poisson gives
u^{−1}Σ_{d|Q}(μ(d)/d)Σ_{k≥1}ℱf(k/(du)) + (φ(Q)/Q)ℱf(0)/(2u) (the f(0) terms cancel since Σ_{d|Q}μ(d) = 0): the dual sum
runs over the frequencies k/(du), i.e. over (1/Q)ℕ/u with non-constant weights, not over ℕ/u with weight 1; so the
adapted map does not intertwine ℱ with R, and no parity-class rule holds (PROVED from the displayed formula). For a
Beurling system there is no Poisson formula at all (rem:ext-killing(ii)), so (1.0) has no analogue (ARGUED, as in
ROUND_008_E §5).
Falsifier test verdict: the selection of the bottom (§2 picture, near-nullity of class +1) fails for (a) cΛ, c ≠ 1,
(b) a_P, (c) Beurling, (d) finite modifications — as required of a Λ-specific ingredient; the class–parity rule (§1) survives
(a), (b) with the plain map, (d), and fails for (c) and for the a_P-adapted map: it is not a sign step and is not claimed
as one.

## 4. Reproducibility
tools/prolate_sector.py T Nb dps KMAX (sine coefficients of Eψ_k, k ≤ KMAX even, and exact d_k; cache
sector_T*_N*_K*.pkl), tools/prolate_sector_anal.py (selection-rule table, class spans, low-block couplings; writes
sector_g_*.pkl), tools/prolate_sector_schur.py (block-diagonal Schur test, fails: |C − I| > 1 because the stiff constraint
directions dominate before elimination), tools/prolate_selfdual_schur.py T Nb dps KMAX (§2.2–2.5: stiff elimination,
γ_k, two- and three-level Schur, even spectrum vs d_{4j+8}), tools/prolate_sector_fals.py T Nb dps KMAX 8 (§3.2).
Runs: (0.8, 90, 40, 40), (1.0, 160, 40, 52), (1.2, 180, 80, 64).

## Result
PROVED piece + PIVOT. The selection rule is proved as an exact identity (Theorem 1.1) with an exactly diagonal defect
(Theorem 1.2) and a quantitative cross-class decoupling (Theorem 1.5); the lower half is reduced, in the self-dual
sector, to a high-range estimate (HR) beyond the prolate edge k ≈ 4N, where the gauge re-enters and the class structure is
void.

### What was proved
- Theorem 1.1: P_{−ε}Π_TEf = ½RΠ_TE(ℱf − εf) exactly (Π_T removes the Poisson boundary terms because span{e^{±x/2}} is
  R-invariant).
- Theorem 1.2: ‖ℱf − εf‖² = Σ2(1 − εε_k√χ_k)a_k² on prolate spans: defect ∈ [d_k, 2d_k] on the own class, ∈ [2, 4] on the
  other.
- Lemma 1.3 and Corollary 1.4: ‖P_{−ε}Π_TEf‖ ≤ ½ζ(2)^{1/2}λ(λ·band defect + weighted leakage) for C¹ data.
- Theorem 1.5 + Lemma 1.6: even-sector cross terms between the classes are −𝒲(Ψ_{f_+}, w_−) − a_T(w_+, w_−), bounded by
  poly(N)·(defect products) ≍ poly(N)√(d_jd_k) on mollified prolate spans.
- §1.7: the near-null class in the even sector is ℱ-eigenvalue +1, because Poisson intertwines ℱ with the window
  reflection; class −1 enters the even sector only through its defect image.
- Lemma 2.1, Proposition 2.2, bound (2.1): elimination of the constraint directions and two-/three-level Schur bounds;
  floor index 8 inside class +1 (index 6 in ROUND_008_E), conditional on three finite-dimensional constants.
- §3: the decoupling identity survives every weight (Λ-free); the near-nullity of class +1 is destroyed by 𝒫_{Λ−w}[Ef_+];
  the a_P-adapted map does not intertwine ℱ with R.
NUMERICAL: ρ_k = ‖wrong-parity part‖/√d_k ∈ [0.46, 0.90] for k ≤ 4N at T = 0.8/1.0/1.2; γ_k ≤ 1.6/1.6/3.7 with normalised
coupling ≤ 0.24; κ_LM ≈ 1.7–1.8 on k ≤ 4N; three-level Schur closes up to k = 2.0/1.76/1.36 × 4N; even spectrum
λ_j^ev ≈ (0.85–2.0)·(1 − χ_{4j+8}) for j ≤ 4; falsifier angles 0.036–1.56 rad vs 1.1–2.9·10⁻⁴ for Λ.

### What failed and why
- The block-diagonal Schur test (scalar diagonal on the mid range) fails before elimination (|C − I| = 1.0–4.4): the raw
  images Π_TEψ_k (k ≥ 12) are not near-null at scale d_k (M_kk/d_k up to 10¹⁵) because each single prolate violates the
  admissibility constraint; after exact elimination of the two stiff directions the coupling is O(√(d_kd_8)).
- The Schur argument stops in the high range k > 4N: α_HI decreases with K (to 0.12–0.28 at the largest K), forced by
  approximate gauge vectors in the high prolate span (ARGUED); with fixed representatives inf M/D → 0, so prob:ext-L's gauge
  infimum is indispensable there.
- Corollary 1.4 needs edge-regular data; for the raw prolates it is NUMERICAL only.
- The class–parity rule is Λ-free and cannot be a sign source (§3.1).

### Next concrete step
Test (HR)(a) directly: on the high block (class +1, 4N < k ≤ K, K up to 3·4N) compute the gauge-minimised D (tools/
prolate_gauge.py, the formula D_g = D − DJH^{−1}JᵀD) and check whether inf M/D_g stays bounded below as K grows at T = 0.8,
1.0, 1.2; in parallel measure κ_C and ‖Gram(h)‖ to make (2.1) explicit on LM.
