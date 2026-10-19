# PROOF_L_SHARP_GG_001 — Strategy GG: the renormalization (self-similarity) identity (pen and paper)

Phase 199, and no
zero datum is used.
Notation as in FF_001/AA_001/A_001: μ ≥ 5, a = T = ½log μ, g even admissible on I = (−a,a), A := ∫g(x)e^{x/2}dx (= B, g even),
c_N = Σ_{m|N,m<μ}μ(m), M_μ(s) := Σ_{m<μ}μ(m)m^{−s} (the classical partial-Möbius mollifier), W = Guo's full-line Weil
distribution (A_001 §1) with translation-invariant kernel. Its even "measure" is
ν = b_∞δ₀ + (Lévy, principal value) − Σ_q c_q(δ_{log q}+δ_{−log q}) + 2cosh(u/2)du, so 𝒲(Φ₁,Φ₂) = ∫∫Φ₁(x)Φ₂(y)dν(x−y).
c_g(u) := ∫g(x)g(x+u)dx (supp ⊂ [−2a,2a]). **Shifted form:** F_g(s) := 𝒲(g, τ_s g) = ∫c_g(u−s)dν(u) = (c_g∗ν)(s). F_g(0) = W_T(g).

## 0. Corpus / index check, and why this is not a retry
Read: FF_001 (Thm FF.1/FF.2), A_001 (Thm 1.1, Prop 2.1), AA_001 Thm D(i), E_001 (comb collapse Λ∗1 = log). Index grepped for
"mollif", "renormal", "self-similar", "shifted", "c_N": hits L62 (mollifiers, proportions), G3D-159 G2_B10 (mollifier ⇒
proportion ⇒ sign, DEAD by DH/Epstein), P58-1 (mollifier floor), A14a-4, INV_K_001 (ζ universal carrier of every window comb).
**New reason:** none of these uses the mollifier as an *exact* algebraic object. Here M_μ appears as the generating
function of the FF.1 comb, with no estimate or proportion. The question is whether that exact factorization carries a sign.
§4 answers no, through a new falsifier argument. It does not reuse the DH/Epstein ground of G3D-159.

## 1. The radical vector and the exact linear identity (PROVED)
**Lemma GG.0 (polar term vanishes; gauge defect is rank one).** Admissibility gives f(0) = f̂(0) = 0 (Guo class G_λ). In (FF.1)
the polar term is ½φ₀(0)e^{−x/2} − ½f̂(0)e^{x/2}, and φ₀(0) = f(0) = 0 because H vanishes on |u| < 1/λ. So **the polar term is
identically 0**. Also Ĥ(0) = 2A, so φ̂₀(0) = f̂(0) − Σ_{m<μ}μ(m)Ĥ(0)/m = −2A·M_μ(1). Fix ψ ∈ C²_c(−1/λ,1/λ), even, ψ(0) = 0,
ψ̂(0) = 1, and write φ₀ = φ₀′ − 2AM_μ(1)ψ. Then φ₀′ ∈ 𝒢₀, so its mirror is radical (A_001 Prop 2.1). □
**Full-line form of FF.1 (PROVED).** Step (3) of the FF.1 proof holds for every x ∈ ℝ. Put Φ̌(x) := Φ_f(−x). Then
 Φ̌ = g + Σ_{N≥μ} c_N N^{−1/2} τ_{log N} g + Φ̌_{φ₀},  (τ_s g)(x) = g(x−s),          (GG.1)
and WΦ̌ = 0 a.e. (Guo Lemma 4.4, CITED, as used in A_001 Thm 1.1(b)). Hence:
**Theorem GG.1 (linear renormalization identity; PROVED).** For admissible real g with f(λ) = 0,
 W_T(g) = −∫_a^∞ Ψ̌(x)(Wg)(x)dx = −lim_{X→∞} [ Σ_{μ≤N≤e^{X−a}} c_N N^{−1/2} F_g(log N) + R_X ] + 2A·M_μ(1)·𝒲(g, Φ̌_ψ),
where R_X is the boundary cluster Σ_{e^{X−a}<N<e^{X+a}} c_N N^{−1/2}∫_a^X g(x−log N)Wg(x)dx.
*Proof.* A_001 Thm 1.1(c): W_T(g) = −𝒲(g,Ψ̌). The integral is absolutely convergent: |Ψ̌(x)| ≤ Ce^{−3x/2} (Guo L4.3), and for
x > a, Wg(x) = −(ν_{Lévy}∗g)(x) − Σ_{q∈(e^{x−a},e^{x+a})}c_q g(x−log q) + 2A cosh(x/2)·(A-terms) = O(e^{x/2+a}). Insert (GG.1)
on (a,X) (finite sum, FF.1). The φ₀′ part drops: it is radical and its support is exterior. For N ≤ e^{X−a} each integral is
complete and equals F_g(log N), because supp τ_{log N}g ⊂ [log N − a, ∞) ⊂ [a,∞). □
**Remark (convergence, honest).** R_X → 0 is NOT proved. Each F_g(log N) is O(1)·N^{1/2}·(A²) + (comb fluctuation). With A = 0 the
mean part cancels exactly: the Lévy tail e^{−t/2} piece of ν cancels the e^{−s/2} piece of the pole kernel. What remains of
F_g(log N) is the comb fluctuation Σ_n Λ(n)n^{−1/2}c_g(log n − log N) minus its mean. Bounding it uniformly in N is a prime
equidistribution statement at scale 2a. That is OPEN here, and it is not attempted. **The identity is exact as the
X-limit of (finite sum + R_X).**

## 2. The quadratic version requested in (i): what survives (PROVED / NO-GO)
Bilinearity on (GG.1) gives formally W_T(g) = 𝒲[Ψ̌] = Σ_{N,N′≥μ} c_Nc_{N′}(NN′)^{−1/2}F_g(log N′/N) + (rank-one ψ-rows).
(a) **Support claim corrected (PROVED).** Only the local part (b_∞ + short-range Lévy) of F_g(s) vanishes for |s| ≥ 2a, i.e.
outside N′/N ∈ (μ^{−1},μ). The Lévy tail is nonzero for every s (ν(t) ~ e^{−|t|/2}) and so is the pole part 2A²cosh(s/2). The
comb part of F_g(s) is −Σ_n Λ(n)n^{−1/2}[c_g(s−log n)+c_g(s+log n)]. It is nonzero exactly when nN/N′ or nN′/N ∈ (μ^{−1},μ),
i.e. at the near-coincidences m ≈ kn of the semiring (item (ii), now exact). So the pair set is not finite: every (N,N′) with
N′/N within a factor μ of a prime power couples.
(b) **The diagonal rearrangement W_T(g)(1 − Σc_N²/N) = off-diagonal: NO-GO (PROVED).** For every prime p ≥ μ, c_p = 1, so
Σ_{N≥μ}c_N²/N ≥ Σ_{p≥μ}1/p = ∞. The diagonal sum diverges, and the double series is not absolutely convergent. Splitting off the
diagonal is meaningless. Only the linear form (GG.1/Thm GG.1) is an exact identity.

## 3. Mellin side: the mollifier factorization (PROVED as an identity; Re s > 1 then continuation)
From (GG.1), for Re s > 1 the generating function of the comb is
 Σ_{N≥μ} c_N N^{−s} = ζ(s)M_μ(s) − 1 =: D_μ(s)   (c = 1∗(μ·1_{[1,μ)}) − δ),                    (GG.2)
the **mollifier defect**. Equivalently H_{Φ̌}(s) = ζ(s)M_f(s) (Guo, CITED) with M_f = M_μ(s)·ĝ-Mellin + M_{φ₀}. So
**Ψ̌ is the image of g under the mollifier defect D_μ** (plus the rank-one ψ-correction), and
 W_T(g) = 𝒲[D_μ(∂)g] (Thm 1.1 + GG.1, PROVED in the sense of §1),
"the window value is the Weil energy of the mollifier defect applied to the window function". The requested lattice
sum of a Fourier mode is Σ_{N,N′}c_Nc_{N′}(NN′)^{−1/2}(N′/N)^{it} = |D_μ(½+it)|². That is formal, since Σc_N N^{−1/2−it}
does not converge. The quadratic identity on the Fourier side then reads
 W_T(g) "=" ∫ |ĝ(t)|² |D_μ(½+it)|² dν̂(t),  ν̂ = FT of the Weil distribution,
and the corresponding statement for the full radical vector is ∫|ĝ|²|ζM_μ|²dν̂ = 0.
**Sign-carrying factor (PROVED identification).** |D_μ|² ≥ 0 and |ĝ|² ≥ 0 are free. The whole sign sits in ν̂, the Fourier
transform of the complete Weil distribution: archimedean density minus the comb's transform 2ΣΛ(n)n^{−1/2}cos(t log n) plus
pole. ν̂ is a distribution, not a measure. Its nonnegativity on the cone {|ĝ|²|D_μ|²} is exactly the positivity of 𝒲 on
the vectors D_μ(∂)g, i.e. W_T(g) ≥ 0 itself. **Restatement, no new sign.** Item (iii)(a) (|F_g(s)| ≤ F_g(0), F_g = c_g∗ν
positive-definite in s) holds iff F̂_g = |ĝ|²ν̂ ≥ 0, which is the same target: circular, NO-GO as a mechanism.

## 4. Falsifiers (PROVED / ARGUED)
- **a_P (Euler factor at p removed): the factorization is NOT Λ-specific (PROVED, corrects FF_001 §5).** a_P(n) = 1_{p∤n}
  and Σ_n a_P(n)f̂(nu) = Σ_n f̂(nu) − Σ_n f̂(pnu). Each sum has the co-Poisson mirror, so FF.1 holds for a_P with
  ζ_P(s) = (1−p^{−s})ζ(s) and the truncated inverse M^P_μ of ζ_P. The comb coefficients c^P_N = Σ_{m|N,m<μ}a_P(N/m)μ_P(m)
  again vanish for 2 ≤ N < μ (Dirichlet inverse). The defect D^P_μ = ζ_P M^P_μ − 1 has the same gap and the same |·|² structure.
  FF_001 §5's claim "a_P has no Poisson mirror" is too strong: a two-term mirror exists. So the factorization of §3 and the gap
  of the comb are shared by a falsifier system. Consequence: **no a_P-generic property of (GG.1–2) can give the sign.**
- **cΛ (c ≠ 1):** a_c(n) (coefficients of ζ^c) are not a finite combination of dilated 1's. There is no mirror, and the
  Weil-radical property of ζ^cM is unavailable (ζ^c is multivalued for c ∉ ℤ). Thm GG.1 fails at the radical step. ARGUED.
- Interaction with E_001 (comb collapse Λ∗1 = log): the comb part of F_g(log N) is ΣΛ(n)n^{−1/2}c_g(log n − log N). On
  E-images E_001 collapses Σ_N c_N·(Λ-comb) through Λ∗1 = log only when c ≡ 1. Here c = 1∗μ_{<μ} − δ, so the collapse gives
  Σ_{m<μ}μ(m)·(log-weighted) terms. These are the Ψ̌_log objects of FF_001 §4, still without a mirror. OPEN.

## 5. Labels
PROVED: Lemma GG.0 (polar term ≡ 0; gauge defect rank one, ∝ A·M_μ(1)); full-line (GG.1); Thm GG.1 (linear identity, as an
X-limit with boundary cluster R_X); §2(a) the coupling set (near-coincidences nN ≈ N′, exact); §2(b) diagonal rearrangement
diverges (NO-GO); (GG.2) D_μ = ζM_μ − 1; sign factor = ν̂ (restatement); a_P mirror and gap (falsifier ⇒ factorization not
sign-carrying, NO-GO as a route); FF_001 §5 corrected for a_P. ARGUED: cΛ failure. OPEN: R_X → 0, uniform size of F_g(log N)
(prime fluctuation at scale 2a), Ψ̌_log, L′♯. NUMÉRICO: none. No sign claimed. L′♯ OPEN. Row D OPEN.
