# PROOF_L_SHARP_D_001 — Strategy D: the Connes–Consani / Connes–Moscovici prolate–Sonin framework

Phase 199, prover memo (pen and paper; the only numbers are cited). Target: **Lemma L′♯** (AUDIT_199): ∃κ>0, A≥0:
∀μ≥5, ∀g ∈ E(core): W_T(g) ≥ κμ^{−A}ℓ(g), equivalently (PROOF_L_SHARP_A_001 Thm 3.1) the prolate matrix inequality
  (★)  𝔐 ⪰ κμ^{−A}D_B on the constraint space 𝒦,  𝔐_{jk} = W_T(Eψ_j,Eψ_k),  D = diag(1−χ_k),  c = 2πμ.

**Outcome in one line.** L′♯ is NOT proved, and no theorem of Connes–Consani (CC, arXiv 2006.13771) or
Connes–Moscovici / Connes–Consani–Moscovici (CM22 PNAS, CCM24 "Zeta zeros and prolate wave operators") implies (★)
for any μ ≥ 5: their only positivity theorem is at the window ½log 2 (μ = 2, no primes), with one-window constants
from a Toeplitz computation. What is obtained here: (1) the exact Sonin decomposition of 𝔐 (Theorem 2.1), in which
the prolate leakage enters with the *inverse* weights D^{−1} (Prop 2.3), the opposite side from (★); (2) a proof
that the semilocal Sonin positivity is invariant under the dilation Λ ↦ cΛ of the comb (Theorem 4.1), so the
Sonin trace is not the Λ-step and (★) must fail for cΛ inside the compact remainder; (3) the gap, stated in their
notation and ours (§3). Strategy D is NO-GO *as a citation route*; its objects are recorded.

## 0. Corpus check (rule ) and why this is not a retry
- **Index read.** 05_LITERATURE L05 (Connes trace formula: restatement, R158), L06/L07 (CCM prolate, Sonin: COVERED,
  phase 183 chain "PROVED with no sign"), L39 (ζ-cycles, R184_009), L40 (CM22), L33, L109; 04_PHASES l.29 (W11′:
  W_T = Pos_S + Δ_T NO-GO, source-defined Δ blind to M_m), l.35 (W-Sonin: multiplier positive part + bounded-inertia
  remainder NO-GO, "limit density supported on zeros"), l.122–126 (R186-CCM candidates NO-GO; R186-semilocal chain
  PARTIAL, PROVED ∀S, no sign; R186-ρ* REF-D; R186-SoninZero NO-GO); 06_OPEN l.212 (boundary triples for W_λ, OPEN);
  README l.47, l.447 (C1: CCM semilocal + Guo identity, ranked low, "falls on L81"), l.450–452 (MECH_001, B_001,
  A_001); AUDIT_B (L35: semilocal descent NO-GO, Thm 2 substitutes PSD(QW−ε_N) for PSD(QW)).
- **Corpus read.** R186_010 (TC_S PROVED), R186_013 (inertia of the semilocal remainder; n₋ grows with the window,
  NUMÉRICO/ARGUED), R186_014 ((84)_S PROVED for S = {∞,2}, Δ-identity ∀λ), R186_017 D3 (level-λ dictionary:
  PROVED 0<λ≤1, λ>1 OPEN per R186_099), R186_018 (ε′_∞(1⁺) = 22.99650 reproduces CC; at ½log3 positivity is
  cancellation, E_S/Son_S = 5.7 %), R186_022 (Son_∞ on 𝒫_T is a property of the compressed operator, not of a
  pointwise symbol); A_001 §1–§4, B_001 Lemma 4.1 / Thm 4.2 (barrier), MECH_001 §4, CERT_FALSIFIERS_001 (cΛ, c>1:
  λ^W < 0 certified at T = 1, ½log 5).
- **Sources read.** CC: Thm 1, Cor 2, Thm 3/4.7 ((83)–(90)), Def 4.4, Prop 4.5 ((74)–(77)), §5 (Lemma 5.1, Prop
  5.3, Lemma 5.4, Prop 5.5, Rem 5.6), Thm 6.11, Rem 6.12, (53), (163), Appendix A. CM22: abstract, eq. [1], Thm 1.6,
  "Sonin space" section. CCM24: abstract, (1.3), §4.5–4.8 (Def 4.4, Def 4.5, Prop 4.7, Thm 4.6).
- **Why not a retry.** Phase 183/186 built the semilocal Sonin chain and measured its sign numerically; W11′/W-Sonin
  closed "Sonin positive part + bounded remainder" as a sign source. None of those entries formulates the object of
  (★): the window form on E-images of prolates, bounded below by the *leakage operator* D modulo the gauge. This
  memo asks a different question of the same framework: whether 𝔐 is expressible through the Sonin data and whether
  any CC/CM theorem lower-bounds it by D. The answers (Thm 2.1, Prop 2.3, Thm 4.1) are new identities and a new
  invariance statement; no sign is claimed, so N_018 (identities + Bochner/C–S) is not violated — it is confirmed.

## 1. Dictionary (PROVED / CITED)

CC work in H = L²(ℝ)_ev with ⟨η|ξ⟩ = ∫_0^∞ η̄ξ (CC (16)), scaling ϑ(ρ)ξ(x) = ρ^{−1/2}ξ(x/ρ), ϑ(f) = ∫f(ρ)ϑ(ρ)d*ρ for
f ∈ C_c^∞(ℝ*_+); the Schwartz kernel of ϑ(f) is k_f(x,y) = f(x/y)(xy)^{−1/2} (PROVED: substitute y = x/ρ). Convolution
f*g, involution f*(u) = \overline{f(u^{−1})}; the Weil distribution W_∞ of CC (53) has Fourier transform 2θ′(t) =
Re ψ(¼+it/2) − log π (CC (163)), i.e. **W_∞(g*g*) = (1/2π)∫a(t)|ĝ(t)|²dt is exactly the archimedean block of the
complete form W_T** (Paper 47 def:W; B_001 §1: Q = pole + (1/2π)∫a|Ff|² − ⟨f,C_pf⟩). In the log variable x = log ρ
a test g ∈ C_c^∞(ℝ*_+) is a window vector g(x) ∈ C_c^∞(I), f = g*g* is the autocorrelation c_g(a) (Mori), f(1) = ‖g‖²,
and ∫f(ρ^{−1})ε(ρ)d*ρ = ∫c_g(a)ε(e^{|a|})da =: C_ε(g) (R186 notation) for even ε.

**Prolates.** P_λ = 1_{[−λ,λ]}, P̂_λ = FP_λF, A_λ := P_λFP_λ compact self-adjoint on ran P_λ with real eigenvectors ξ_n
(the prolates ψ_n of A_001 §3.4) and eigenvalues λ(n) = ±√χ_n (CC (74): P_λFξ_n = λ(n)ξ_n), so **CC's λ(n)² is our
concentration χ_n**. CC's ψ_n := (1−P_λ)Fξ_n is **our out-of-band function r_n = (1−P_λ)ψ̂_n**, with ‖ψ_n‖² = 1−χ_n
(CC (76)) = our D_n; ζ_n := ψ_n/√(1−χ_n) = r_n/‖r_n‖ and τ_n := λ(n)/√(1−λ(n)²) = √χ_n/√(1−χ_n) = (χ_n/D_n)^{1/2}.
(PROVED: identical definitions, CC Prop 4.5 and A_001 §3.4.)

**Sonin space.** S(α,β) = {ξ ∈ H : ξ = 0 on |x| ≤ α, Fξ = 0 on |p| ≤ β} (CC Def 4.4; CCM24 Def 4.4 with α = β = λ);
Π_{α,β} its projection; Son_{α,β}(g) := Tr(ϑ(g)Π_{α,β}ϑ(g)*) = Tr(ϑ(g*g*)Π_{α,β}) ≥ 0 (positive by construction;
finite by CC Thm 4.7 / R186_010 TC′). The summation map E of A_001 is Connes' map Σ (CCM24 §1: E(f)(u) =
u^{1/2}Σf(nu) on S(ℝ)_ev^0), and **our admissibility conditions f(0) = f̂(0) = 0 are CC's (93)**: the range of
D = D_u² + D_u (the operator Q of CC (55) transported to ℝ by Lemma 5.1) consists of the functions with f(0) = f̂(0) = 0.
They are *not* the Sonin conditions (vanishing on intervals); they are the conditions for Ef to be a window vector
without pole, as in Guo Lemma 4.2. The brief's identification "constraints = Sonin conditions" is therefore
corrected: constraints = ran D = ker of the two characters at 0 (PROVED, CC §5).

## 2. 𝔐 in terms of the Sonin data

**Theorem 2.1 (Sonin decomposition of the window form; PROVED given CC Thm 4.7 CITED).** Let I = (−T,T), g ∈ C²_c(I)
real (the core), G(x) := ∫_{−∞}^x g, and 𝔅(g) := −½∫∫g(x)g(y)|x−y|dxdy (= ‖G‖² when ∫g = 0). Let ε be the CC function
(84) at Sonin level (1,1), extended by ε(ρ^{−1}) = ε(ρ). Then ε(1) = 0, ε ∈ C^∞([1,∞)) one-sidedly, and
  **W_T(g) = Son_{1,1}(g) + 2ε′(1⁺)𝔅(g) − ⟨g,K_sg⟩ − ⟨g,C_pg⟩ + 2Re(A(g)\overline{B(g)}),**
where K_s is the integral operator on L²(I) with kernel k_s(x−y), k_s(v) := ε(e^{|v|}) − ε′(1⁺)|v| ∈ C^{1,1}(ℝ) (the
kink removed), Hilbert–Schmidt on L²(I), and C_p, A, B are as in B_001 (comb of primes < μ, pole functionals).
*Proof.* CC Thm 4.7: Tr(ϑ(f)Π_{1,1}) = W_∞(f) + ∫f(ρ^{−1})ε(ρ)d*ρ for all f ∈ C_c^∞(ℝ*_+); apply to f = g*g*, where
Tr(ϑ(g*g*)Π) = Son_{1,1}(g) and W_∞(g*g*) = (1/2π)∫a|ĝ|². ε(1) = 0 because each term of (84) at ρ = 1 is ⟨ξ_n|ζ_n⟩ = 0
(disjoint supports), and ρ ↦ ρ^{1/2}∫_{1/ρ}^1 ξ_n(x)ξ_n^{an}(ρx)dx (CC proof of Lemma 5.4) is smooth on [1,∞) with the
series converging with all derivatives by CC (100) and Appendix F (CITED). Hence ε(e^{|v|}) = ε′(1⁺)|v| + k_s(v)
with k_s ∈ C^{1,1}. Then ∫c_g(a)ε(e^{|a|})da = ε′(1⁺)∫∫g(x)g(y)|x−y|dxdy + ⟨g,K_sg⟩ = −2ε′(1⁺)𝔅(g) + ⟨g,K_sg⟩. Adding
the prime and pole blocks of W_T (which are not in W_∞) gives the formula. K_s is Hilbert–Schmidt since k_s is
continuous and I bounded. For ∫g = 0: ∫∫g(x)g(y)|x−y| = −2‖G‖² (integrate by parts twice; or Plancherel with
F(|v|) = −2 f.p. t^{−2}). The core vectors g = Ef|_I with f admissible are piecewise C¹ with jumps at x_n (Guo Lemma 4.2)
and lie in H^{1/2−}(I); every term of the identity is continuous in that topology (a(t) = O(log t), K_s and 𝔅 are
L²-continuous, Son is continuous because Tr(ϑ(g)Πϑ(g)*) ≤ Tr(ϑ(g)ϑ(g)*)-regularised = W_∞ + C_ε by the identity
itself), so the identity extends to E(core) by density. □

**Corollary 2.2 (prolate matrix form; PROVED).** In the basis g_k = Eψ_k|_I,
  𝔐 = 𝔖 + 2ε′(1⁺)𝔅 − 𝔎 − ℭ + 𝔓,
with 𝔖_{jk} = Tr(ϑ(g_j)Π_{1,1}ϑ(g_k)*) (⪰ 0), 𝔅_{jk} = 𝔅(g_j,g_k) (⪰ 0 on ∫g = 0), 𝔎 = Gram of K_s, ℭ_{jk} =
⟨g_j,C_pg_k⟩, 𝔓 rank 2. (★) reads: 𝔖 + 2ε′(1⁺)𝔅 − 𝔎 − ℭ + 𝔓 ⪰ κμ^{−A}D_B on 𝒦.

**Proposition 2.3 (weight inversion; PROVED from CC Lemma 5.4 CITED).** At Sonin level (λ,λ), with prolates at
c = 2πλ², the CC series is ε_λ(ρ) = Σ_n τ_n⟨ξ_n|ϑ(ρ^{−1})ζ_n⟩ = Σ_n (√χ_n/(1−χ_n))⟨ξ_n|ϑ(ρ^{−1})r_n⟩, and its kink is
  ε_λ′(1⁺) = Σ_n χ_n ξ_n(λ)²/(1−χ_n) = Σ_n χ_n ψ_n(λ)²/D_n.
(CC Lemma 5.4 at λ = 1, where the numerical value 22.9965 is reproduced by R186_018 V; the computation is identical at
any λ: the overlap of ξ_n and ϑ(ρ^{−1})ζ_n is the shell λ/ρ < |x| < λ, and ψ_n(λ⁺) = (Fξ_n)(λ) = λ(n)ξ_n(λ) by
continuity of the entire function Fξ_n.) Hence **the leakage enters the Sonin decomposition with the weights
D_n^{−1}, on the side of the kink constant and inside K_s and Son, never as a lower bound.** In particular at the
level λ = e^T of (★): 2ε_λ′(1⁺) ≥ 2χ_0ψ_0(λ)²/(1−χ_0(2πμ)) ≍ μ^{O(1)}e^{4πμ}, the inverse of the bottom scale of ℓ(g)
(AUDIT_199 (e)); at that level the decomposition is a cancellation of two terms of size e^{4πμ} down to the margin
e^{−4πμ}. (The *full* level-λ identity needs the dictionary D3 of R186_017 for λ > 1, which is OPEN (R186_099); the
formula for ε_λ′(1⁺) and the weights do not depend on it.)

**Answer to (i).** 𝔐 is a function of the Sonin data in the sense of Cor 2.2; it is **not** a function of the prolate
wave operator W_λ. CCM24 (1.3) gives W_λ = −S² + 2πλ²(4N+1) − ¼ with S the scaling generator (so ϑ(g) = ĝ(S)) and N
the grading of polynomials in S applied to the Gaussian; N does not commute with S, so no spectral calculus of W_λ
produces ϑ(g) or Son(g). The only link is representational: W_λ commutes with Π_λ (CM22), its negative
eigenfunctions e_n span the Sonin space up to a finite-dimensional discrepancy (CM22 "Sonin space" section; CCM24
footnote 2; CITED), hence Son_λ(g) = Σ_n ‖ϑ(g)*e_n‖² over that basis. This is a representation, not a bound.
"𝔐 = (function of W_λ) + explicit correction": **NO** (PROVED, by (1.3) and the non-commutation of N and S).

## 3. (ii)–(iii) What CC/CM prove, and the exact gap

| theorem | statement | window / λ | primes | constants | label |
|---|---|---|---|---|---|
| CC Thm 4.7 (= Thm 3) | Son_{1,1}(g) = W_∞(g*g*) + C_ε(g), Son ≥ 0 | all f (no restriction) | none | exact | CITED (identity) |
| CC Cor 2 | Son_{1,1}(g) ≤ Σ_{ρ}|ĝ(ρ)|² + c|ĝ(0)|² | supp g ⊂ [2^{−1/2},2^{1/2}] | none | c < 17 | CITED (uses (1)) |
| CC Cor 3.8 | D∘Q ≤ 0 on C_c^∞(I), I = [u^{−1},u], u = 1.10246 (T ≤ 0.0975) | tiny | none | explicit | CITED |
| CC Prop 5.5 / Thm 3.6 | N_I = −2ε′(1⁺)(Id − K_I), K_I Hilbert–Schmidt | \|I\| ≤ log 2 | none | — | CITED |
| CC Thm 6.11 / Lemma 6.10 | W_∞(g*g*) ≥ Son(g) − (4γ/log 2)|ĝ(0)|², via ⟨ξ,(Id−K_I)ξ⟩ + a|⟨ξ_0,ξ⟩|² ≥ (ε_2−ε_1)‖ξ‖² | I = [−½log2, ½log2] (μ = 2) | none | λ_max(K_I) = 1.05158, ε_1 ≈ 0.00122, ε_2 ≈ 0.00441, a ≈ 0.064, 13 < c < 17: from a Toeplitz discretisation (steps 1–6 of CC §6) | CITED (numerically assisted) |
| CM22 Thm 1.6, 5.1 | W_sa self-adjoint, commutes with F and with Π_λ; discrete spectrum; UV law of negative eigenvalues ~ zeros² | λ = 1, √2 | none | — | CITED (no positivity) |
| CCM24 Thm 4.6, Prop 4.7 | semilocal Sonin spaces S_λ(X_S,α) ≅ S_λ(ℝ) via θ_S, stable in S | any λ | S finite | — | CITED (no positivity) |
| R186_014 (84)_S | Tr ϑ(f)Π_S = W_∞ − comb₂ + ∫fε_S | λ = 1 | S = {∞,2} | ε_S numerical | PROVED (corpus) |

**Answer to (ii).** No theorem of CC/CM gives a positivity or a lower bound *uniform in λ*. The positivity theorem
(Thm 6.11) holds for one window, I = [−½log 2, ½log 2], at the archimedean place only, after one linear condition
(ĝ(0) = 0, the direction of the single eigenvalue λ_max(K_I) > 1), with constants obtained by exact diagonalisation
of a finite Toeplitz approximation of K_I. Its hypotheses on λ: the prolate level is λ = 1 (c = 2π) and the window
is |I| ≤ log 2 (Prop 5.5, which uses ε only on [1,2]). No range in μ is covered beyond μ = 2.

**Answer to (iii): the deduction cannot be written; the gap, exactly.** Suppose one tries to deduce (★) from
Cor 2.2 along CC's lines. One needs, in CC notation with I_T = [−T,T] and the Y-primitives ξ of CC (143):
  (CC_μ)  ⟨ξ|N_{I_T}ξ⟩ ≥ ⟨g,C_pg⟩ − pole(g) − Son(g) + κμ^{−A}ℓ(g),  N_{I_T} = −2ε′(1⁺)(Id − K_{I_T}),
on the three-constraint space of E-images. In our notation: 𝔖 + 2ε′(1⁺)𝔅 ⪰ 𝔎 + ℭ − 𝔓 + κμ^{−A}D_B on 𝒦. The gaps:
- (G1, window) CC control K_I only for |I| ≤ log 2 (one eigenvalue above 1). For μ ≥ 5, |I_T| = log μ ≥ log 5 and the
  register of ε covers only ρ ≤ 3 (R186_022); the number of eigenvalues of the remainder above the Sonin floor grows
  with T (R186_013 §4–5 NUMÉRICO/ARGUED; R186_018 C1: two negative directions at ½log 3 with S = {∞,2}). No CC
  statement bounds that count or its μ-dependence.
- (G2, primes) C_p is absent from every CC/CM theorem; the semilocal (84)_S is corpus-proved for S = {∞,2} and two
  primes with ε_S known only numerically (R186_014/015/018). No semilocal positivity theorem exists in CC/CM
  ("all the ingredients make sense in the general semi-local case" is a programme statement, CC abstract).
- (G3, uniformity) λ_max(K_I), ε_1, ε_2, a, c are one-window numbers; nothing in CC is a function of μ.
- (G4, leakage) D never appears on the lower side in CC. Their conditioning removes one direction with the weight
  |ĝ(0)|² (a character); (★) needs a lower bound in the D-seminorm of the gauge class, whose eigenvalues range from
  1−χ_0 ≍ e^{−4πμ} to 1. The CC decomposition carries D^{−1} (Prop 2.3) in the terms that must cancel, so the inequality
  "𝔖 + 2ε′𝔅 − 𝔎 ⪰ ℭ + κμ^{−A}D_B" is a statement about the difference of two e^{4πμ}-size forms being ≥ an e^{−4πμ}-size
  form: CC's Toeplitz method would have to resolve it to that precision (this is Mori's S7, B_001 §4).

**Proposition 3.1 (the positive pieces are comb-blind, hence not the source; PROVED).** 𝔖, 𝔅, 𝔎, 𝔓 do not depend on
the comb; ℭ is linear in it. Therefore every proof of (★) of the form "𝔖 ⪰ 0, 𝔅 ⪰ 0, bound 𝔎 + ℭ by TV-robust
estimates" is excluded by B_001 Lemma 4.1 (barrier for the complete form) at every μ ≥ 5: a measure ν′ = ν_Λ + mδ_{u_0}
with m ≳ λ^W_T ≤ μ^{9/2}e^{−4πμ} (rem:moriceiling, CITED) makes W_T negative on the bottom vector while leaving
𝔖 + 2ε′𝔅 − 𝔎 + 𝔓 unchanged. □ (This is W11′ / W-Sonin of the index, now stated for the object (★).)

## 4. (iv) Where Λ enters, and the falsifiers

**Theorem 4.1 (comb-dilation invariance of the semilocal Sonin positivity; PROVED, given R186_010/014 for the
trace-class memberships, CITED).** Work in the log variable (R186_010): H = L²(ℝ), translations T_a, P = 1_{t≤a},
F_∞ = I·m_∞(D) with I the reflection and m_∞ the unimodular Tate factor, F_S = I·m_∞(D)U(D) with U = e^{iφ(D)},
φ odd, φ′(s) = Σ_{k≥1}2 log 2·2^{−k/2}cos(ks log 2) (the 2-adic factor; R186_010 R, R186_014 C′). For every real c put
U_c := e^{icφ(D)} and F_c := I·m_∞(D)U_c(D). Then:
(a) F_c is a unitary self-adjoint involution with F_cϑ(ρ)F_c = ϑ(ρ^{−1}) (the axiom L0 of R186_009), so the whole
Halmos/Sonin construction of R186_014 applies: Π_c := projection on ran(1−P) ∩ ran(1−F_cPF_c), Son_c(g) :=
Tr(ϑ(g)Π_cϑ(g)*) ≥ 0, and (84)_c: Tr ϑ(f)Π_c = W_∞(f) − comb_c(f) + ∫f(ρ^{−1})ε_c(ρ)d*ρ, with comb_c(f) :=
Tr ϑ(f)(F_cPF_c − F_∞PF_∞).
(b) **comb_c(f) = c·comb₂(f) = c·Σ_{k≥1}log 2·2^{−k/2}(f(2^k) + f(2^{−k})).**
*Proof.* (a) m_∞ and U_c commute with translations, so F_cT_aF_c = I T_a I = T_{−a}; F_c² = I M_c I M_c = M̃_cM_c = 1
because M̃_c(s) := M_c(−s) = \overline{M_c(s)} (m_∞(−s) = \overline{m_∞(s)} and φ odd); F_c* = M_c*I = I M̃_c* = I M_c = F_c.
(b) X_c := U_cPU_c* − P = ∫_0^c (d/dc′)(U_{c′}PU_{c′}*)dc′ = ∫_0^c U_{c′}(i[φ(D),P])U_{c′}*dc′ (strongly). For f ∈ C_c^∞,
ĝ(D) := ϑ(f) has Schwartz symbol; ĝ(D)[φ(D),P] is trace class (same Hankel argument as R186_014 T2, Simon Thm 4.5,
CITED), and U_{c′} commutes with ĝ(D), so by cyclicity Tr(ĝ(D)U_{c′}i[φ,P]U_{c′}*) = Tr(ĝ(D)i[φ(D),P]) for every c′;
integrating, Tr(ĝ(D)X_c) = c·Tr(ĝ(D)i[φ(D),P]). The last trace is the classical commutator trace: for multipliers
a(D), b(D) with Schwartz kernels, Tr(a(D)[b(D),P]) = ∫∫ǎ(t′−t)b̌(t−t′)(1_{t′≤a}−1_{t≤a})dtdt′ = ∫u·ǎ(−u)b̌(u)du =
(−i/2π)∫a(s)b′(s)ds, linear in b. Hence Tr(ĝ(D)X_c) = (c/2π)∫ĝ(s)φ′(s)ds = c·comb₂(f), the c = 1 case being R186_014
C′. Conjugating by I·m_∞ does not change traces. □

**Corollary 4.2 (PROVED).** For every real c, W_∞(g*g*) − c·⟨g,C_2g⟩ = Son_c(g) − C_{ε_c}(g) with Son_c ≥ 0. The same
holds with every prime p < μ given its own exponent c_p (product of the U_p^{c_p}), with primes deleted (c_p = 0:
the a_P falsifier), and with m_∞ replaced by the Tate factor of a Dirichlet character (the F-DH archimedean kernel).
**So the semilocal Sonin positivity exists for the whole family of falsifiers**, and in particular for cΛ with c > 1,
where λ^W_T < 0 is certified (CERT_FALSIFIERS_001, T = 1 and ½log 5). Consequently: (1) Λ enters the CC framework
only through the symbol φ′ of the local factor, i.e. through comb_c = −(prime block), and the Sonin trace never sees
c; (2) **(★) fails for cΛ inside the compact remainder C_{ε_c} = 2ε_c′(1⁺)𝔅 − K_s^{(c)}, not in the Sonin trace**: the
only non-robust object of the decomposition is ε_c, and the statement "Son_c ≥ C_{ε_c} + κμ^{−A}ℓ on E(core)" is
true for c = 1 (if L′♯ holds) and false for c > 1 at the certified windows, with Son_c and the kink identical in
structure. The Λ-step is therefore the sign of the compact remainder against the Sonin floor, at the e^{−4πμ} scale.

**Remark 4.3 (the semiring principle, in this language; ARGUED).** The Sonin trace is multiplicative-generic
(any unitary involution F with FϑF = ϑ^{−1}), and the prime block is additive-generic (the symbol φ′). The only
place where the integers' two structures meet in Cor 2.2 is the function ε_c, whose series Σ_n τ_n⟨ξ_n|ϑ(ρ^{−1})ζ_n⟩
pairs the band-limited prolate ξ_n (additive, Fourier) with its leakage transported by scaling (multiplicative). The
kink at ρ = 1 (ε′(1⁺), Prop 2.3) is the n ≈ λ/u boundary of A_001 Rem 3.3 seen from the Sonin side. This confirms the
semiring principle as the locus of the sign; it gives no sign.

## 5. Labels and verdict
- **PROVED:** Thm 2.1 (Sonin decomposition of W_T on the core, given CC Thm 4.7), Cor 2.2, Prop 2.3 (weight
  inversion and the kink formula at every level), the "NO" of §2 to "𝔐 = function of W_λ", Prop 3.1, Thm 4.1
  (comb-dilation invariance), Cor 4.2.
- **CITED:** CC Thm 4.7, Lemma 5.4, Prop 5.5, Thm 6.11, Cor 2, (16), (53), (93), (100), Appendix F; CM22 Thm 1.6 and
  the Sonin-space statement; CCM24 (1.3), Thm 4.6, Prop 4.7, footnote 2; R186_010/014 trace-class lemmas; Simon
  Thm 4.5; rem:moriceiling; CERT_FALSIFIERS_001.
- **CONDITIONAL:** the full level-λ identity for λ = e^T > 1 (on D3 of R186_017, OPEN for λ > 1 per R186_099).
- **ARGUED:** Rem 4.3.
- **OPEN:** (★), L′♯. No sign is claimed. Row D OPEN.
- **NO-GO (as a citation route):** Strategy D. No CC/CM theorem lower-bounds 𝔐 by D for any μ ≥ 5; the positive
  part of their decomposition is comb-blind (Prop 3.1, Thm 4.1), so it cannot be the Λ-step; their one positivity
  theorem is a one-window exact diagonalisation (μ = 2) of the same type as Mori's S7 (B_001 Thm 4.2).

**Verdict.** The Connes–Consani framework gives the exact structure of 𝔐 (Sonin trace + kink − compact − comb + pole)
and shows that the leakage weights enter inverted; it does not contain, and by Theorem 4.1 cannot contain, a lower
bound of 𝔐 by the leakage: its positive reservoir exists verbatim for every dilated comb cΛ, for deleted primes and
for the DH archimedean factor. Nothing in this memo should be retried as a sign source. Objects recorded for REF-D:
Cor 2.2 and the remainder ε_c (the Λ-dependent compact piece). The index entry is written at the same time.
