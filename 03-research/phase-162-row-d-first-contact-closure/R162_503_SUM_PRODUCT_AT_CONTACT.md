# R162_503 — Round 6: the sum–product quadratic quantity at the first-contact vector (O-D4.1)

Pure mathematics; no numerics.

Status: **NO-GO (PROVED) for the identity form of O-D4.1, with two PROVED STEPS and one precise residual.**
Gate 1 remains OPEN. No label moves.

- PROVED STEP 1 (§2, the two-way quantity). For a first-contact vector F and any admissible
  test operator Θ, the quantity 𝔅_Θ(F) := a_T(F, ΠPΘF) can be computed in two ways. The first
  way uses the kernel equation, possibly at an eigenvalue λ. The second uses the full-line PC
  identity, i.e. Poisson plus Λ*1=log. Their difference has the exact form
  (2.3): λ⟨F,ΠPΘF⟩ + ⟨r,PΘF⟩ + 𝔛_Θ(F) = 𝔓_Θ(F).
  Here 𝔛_Θ is the exterior pairing (Gamma tail plus prime collars) and 𝔓_Θ is the Poisson–Chebyshev side.
- PROVED STEP 2 (§3, the Gamma-lattice coefficient). Every Gamma-lattice coefficient of the
  sum–product difference is the value at s = −2m of the meromorphic function
  f′ − (f′/f)·f. That function is **identically zero**, and at the trivial zero both terms equal
  ζ′(−2m). So the combined step puts coefficient 0 on K_F(a_m)·(·) for every m. The
  trivial-zero cancellation (R162_305) and the log-channel cancellation (R162_401) are one
  cancellation, seen from the two sides.
- NO-GO (§4, the transport theorem). Every quantity in the class 𝒞 (§1.3) that is formed in one
  step from (Poisson, Λ*1=log, kernel equation, minimality) has a verbatim analogue for any
  degree-1 Dirichlet series f that has a functional equation. The analogue uses the comb a_f,
  the "von Mangoldt" coefficients Λ_f defined by −f′/f, and the conductor-dilated Fourier map.
  This includes Davenport–Heilbronn. **The DH line is empty**: neither Poisson_f nor
  Λ_f*a_f = a_f·log fails for DH. DH has a first contact (R162_407 §5b), so any closing argument
  in 𝒞 proves a falsehood. Every formulation in 𝒞 is therefore discarded by the mandatory filter.
- RESIDUAL (§5). A DH-failing line has to be an **inequality or support statement**:
  Λ ≥ 0, supp Λ ⊂ prime powers (Euler product), or a_f = 1_ℕ ≥ 0 used as positivity of a comb.
  An identity does not qualify. O-D4.1 has to be restated with "Λ*1=log" replaced by one of these,
  and §5 gives the one restatement that survives F1–F4 formally.

Notation: Paper 46 §sec:firstcontact. a_T, H_T, Π, P, 𝓕 = u_∞(D)J, S_N, K_N, L_M, A_M, E_N and
H_{M,N} as in thm:PCfinite. a_m = 2m+½, s_m = 2m+1, K_F(a) = ∫e^{−at}F, r is the Tate vector of
eq:localweak, and ε is the parity of F.

## 0. Corpus check

- R160_D4_R2 §6 states O-D4.1: use (Z2)+(Z3) in one *analytic* step, not as a group-ring identity.
  Its Thm 5.1 closes the uses of convolution identities *on tests*. This memo closes the uses
  *inside the Rayleigh pairing at the kernel vector*, which D4 did not treat. Its Thm 2.2 claims
  that (Z2) against 1_ℕ fails for DH. That is correct as a statement about the comb, and §4.3
  explains why it still gives no DH line inside a PC-type argument.
- Paper 46 eq:Qbalance / eq:Qspectral are the case Θ = S_L (Gamma Hankel) of (2.3). The
  coefficient is −2(d_m+λ), which is negative, so the sign is wrong.
- R162_305 (trivial-zero cancellation), R162_401 (log channel cancels by [X,S_N] = −K_N), and
  R162_403 (smooth comb: H^{(P)} = 0, symbol identities fail F1). §3 identifies these as one
  identity. R162_204 (regularised jets are invariant under finite changes of Λ) and R162_407 §5
  (weight-blindness; DH has a first contact) are used in §4.
- Grep over `03-research` for "Λ_f", "transport", "f′−(f′/f)f", "degree-1 transport" found no
  prior transport theorem for PC-type identities. R162_407 §5 proves weight-blindness for its own
  steps only.

## 1. Setting

### 1.1 Parity reduces 𝓕 to a multiplier
For F with JF = εF, F̂(−τ) = εF̂(τ), so (𝓕F)^ = ε u_∞ F̂. **On a parity class, 𝓕 = ε u_∞(D), a
unimodular Fourier multiplier.** S_N, K_N, L_M, L_M^* and 𝓜 are multipliers on the full line,
with symbols ζ_N(½−iτ), −ζ_N′(½−iτ), (−ζ′/ζ)_M(½−iτ), its conjugate, and m(τ). The operator X
acts as i∂_τ. The only non-multiplier operators are therefore X and the compressions P, Π.

### 1.2 The two identities
(Pois) S_∞𝓕 = JS_∞ formally, with finite defect E_N. On symbols this is the functional equation
ζ(s) = χ(s)ζ(1−s).
(Cheb) L_MS_N − K_N = H_{M,N}, supported on k > N. On symbols this is −ζ′ = (−ζ′/ζ)·ζ, and
on coefficients it is Λ*1 = log.

### 1.3 The class 𝒞
𝒞 is the class of real quadratic quantities in F obtained in *one step* as follows. Take a
finite word identity in {X, J, 𝓕, τ_{log n}, 𝓜, P, Π} with coefficient sequences (1, Λ). Prove it
only from [X,τ_c] = −cτ_c, 𝓕² = 1, X+𝓕X𝓕 = 𝓜, JX = −XJ, JL = L^*J, (Pois) and (Cheb). Pair it
with (F, ΘF) for a bounded word Θ. Then substitute the kernel equation
a_T(F,G) = λ⟨F,G⟩ + ⟨r,G⟩ (λ = 0 at contact), and optionally the minimality data
λ_A(T) ≥ 0 for T < T_* and λ_A(T_*+δ) < 0. Every construction in R161_0xx and R162_2xx–4xx lies in 𝒞.
So do eq:Qbalance and the PC-ren squares.

## 2. The two-way quantity (PROVED)

Let Θ be a bounded word that maps L²(I_T) into the Schwartz-type functions, and put G = ΠPΘF.
This is an admissible test.

**Way 1 (kernel).** For H_TF = λF,

    a_T(F, G) = λ⟨F, G⟩ + ⟨r, PΘF⟩.                                                       (2.1)

**Way 2 (full line).** a_T(F,G) = ⟨A_MF, PΘF⟩ − ⟨A_MF, P(1−Π)ΘF⟩ for M ≥ e^{2T}. Write
⟨A_MF,PΘF⟩ = ⟨A_MF,ΘF⟩ − ⟨A_MF,(1−P)ΘF⟩. The last term is the exterior pairing 𝔛_Θ(F). Since F is
supported in I_T, (1−P)A_MF = (1−P)𝓜F − (1−P)(L_M+L_M^*)F. The Gamma part has the kernel
expansion

    (1−P)𝓜F(t) = −½ Σ_{m≥0} e^{−a_m|t|} K_F(±a_m)   (t ≷ ±T),                              (2.2)

because m(τ) = ½[ψ(¼+iτ/2)+ψ(¼−iτ/2)] − log π and ψ has poles at −(m+¼)·2 in iτ.
The full-line term ⟨A_MF,ΘF⟩ is rewritten through thm:PCfinite with 𝓕 = εu_∞(D) (§1.1). Together:

    λ⟨F,ΠPΘF⟩ + ⟨r,PΘF⟩ + 𝔛_Θ(F) = 𝔓_Θ(F),
    𝔓_Θ(F) := ε⟨({X,E_N} − L_M^*E_N − JH_{M,N} − H_{M,N}𝓕)F, S_N^{−*}...⟩ ,                  (2.3)

Here the right-hand side is the PC form of ⟨A_MF,ΘF⟩. It is written with S_N factored out of Θ
when Θ = Θ′S_N, which is the case needed to make the PC identity appear. At λ = 0, (2.3) is the
unique quadratic relation in 𝒞 attached to Θ. Every relation in 𝒞 is a finite sum of such
relations.

*Proof.* (2.1) is eq:localweak with the eigenvalue term. (2.2): the distribution kernel of 𝓜 off
the diagonal is the inverse Fourier transform of m. Close the contour in the half-plane selected
by sgn t. The digamma poles τ = ±i(2m+½)·… give residues e^{−a_m|t|}, and integrating against F
gives K_F(±a_m). The remaining terms are linear algebra of thm:PCfinite. ∎

**F-tests of (2.3).** It is genuinely quadratic (F4 passes). It is orientation-sensitive, because
𝔓_Θ is linear in A_M rather than a square (F2 passes). λ enters only through λ⟨F,ΠPΘF⟩. **F1 then
requires ⟨F,ΠPΘF⟩ ≥ 0 on eigenvectors.** For the comb choices Θ = S_N or K_N this pairing is
Σn^{−1/2}c_F(log n), which is indefinite, so F1 fails. For Θ = S_N^*S_N, compressed, it is
‖PS_NF‖² ≥ 0, so F1 is formally satisfied. The rest of the memo uses this choice, and §3 shows
that it still carries no Gamma-lattice information.

## 3. The Gamma-lattice coefficient of the sum–product difference (PROVED)

Take Θ = S_N^*S_N and let N → ∞ in renormalised form (Rem Sren), with all quadratic expressions
formed at finite N first. The coefficient of K_F(a_m)·(conjugate moment of ΘF) in 𝔛_Θ − 𝔓_Θ
receives two contributions:

- Poisson side: the exterior Gamma tail (2.2), carried through S_N. Its renormalised
  multiplier is Σ n^{2m} ↦ ζ(−2m) times the jet factor. This gives the value channel ζ(−2m)·c_m.
- Chebyshev side: the log channel from K_N = −[X,S_N]. Its renormalised multiplier is
  ζ′(−2m), paired against the residue (1 at s = −2m) of −ζ′/ζ multiplied by ζ.

**Theorem 3.1.** The total coefficient is ρ_m·[ζ′ − (ζ′/ζ)ζ](−2m), with ρ_m ≠ 0 as in R162_402 (0.1).
Here [ζ′ − (ζ′/ζ)ζ] is the holomorphic extension of the identically vanishing function. Hence
the coefficient is **0 for every m**, every F and every N.

*Proof.* The Chebyshev side contributes Res_{−2m}(ζ′/ζ)·ζ′(−2m) = ζ′(−2m). The Poisson side
contributes −ζ′(−2m), from R162_402 Thm 1.3(e): G_+^0(−a_m) = −εζ′(−2m)K_F(a_m). The Q_+ and Θ_+
histories are multiplied by ζ(−2m) = 0. The sum is the Laurent constant term at −2m of
ζ′ − (ζ′/ζ)ζ ≡ 0. ∎

**Corollary 3.2.** The cancellations of R162_305 (trivial zeros kill the history) and of R162_401
(log channel cancels by [X,S_N] = −K_N) are the two halves of Theorem 3.1. Using Poisson and
Chebyshev *in the same quadratic step* does not avoid them. It *is* the identity that produces
the cancellation. What remains in (2.3) at λ = 0 has no K_F(a_m) term. It consists of
⟨r,PS_N^*S_NF⟩ (the Tate endpoint), the prime collars, and the finite-N remainders
H_{M,N} (k > N) and E_N. In the limit these are the objects of R162_202/203 (ESB), which
R162_203 showed to be equivalent to Gate 1.

## 4. The transport theorem and the DH line (NO-GO, PROVED)

Let f(s) = Σa_f(n)n^{−s} be real, with meromorphic continuation and a functional equation
f(s) = χ_q(s)f(1−s), where χ_q(s) = q^{½−s}χ(s) (degree 1, conductor q, root number 1). Define
Λ_f by −f′/f = ΣΛ_f(n)n^{−s} in a right half-plane.

**Lemma 4.1.** (i) Λ_f*a_f = a_f·log. (ii) With S_N^f = Σ_{n≤N}a_f(n)n^{−1/2}τ_{log n},
𝓕_q = τ_{−½log q}𝓕 and E_N^f = S_N^f𝓕_q − JS_N^f, thm:PCfinite holds verbatim with
(S,K,L,𝓜,𝓕,H) ↦ (S^f,K^f,L^f,𝓜+log q,𝓕_q,H^f). For M ≥ N, H^f_{M,N} is supported on k > N.

*Proof.* (i) Compare coefficients in −f′ = (−f′/f)f. (ii) The proof of thm:PCfinite uses only the
relations listed in §1.3 together with (i). 𝓕_q satisfies 𝓕_q² = 1 and X+𝓕_qX𝓕_q = 𝓜+log q, since
the dilation adds a constant to θ′. The formal Poisson relation S_∞^f𝓕_q = JS_∞^f is the
functional equation of f. ∎

**Theorem 4.2 (transport).** Every relation in 𝒞 for (1,Λ,ζ) has a verbatim analogue for
(a_f,Λ_f,f). The analogue holds at any first-contact vector of the primitive Weil form of f,
which is built from −(L^f+L^{f*}) and 𝓜+log q. Theorem 3.1 transports with f′ − (f′/f)f ≡ 0.

*Proof.* Induction on the derivation. Each primitive relation has an f-analogue (Lemma 4.1),
and the kernel and minimality data have the same form. ∎

**Corollary 4.3 (DH line: empty).** Let f = f_DH, the Davenport–Heilbronn combination of two
characters mod 5. It is real, satisfies f = χ_5f(1−·) with root number 1, and has no Euler product.
- (Pois)_f holds, because it is the functional equation of f.
- (Cheb)_f holds, by Lemma 4.1(i). This is a tautology for every Dirichlet series.
- DH has a first contact T_*^{DH} (R162_407 §5b; lem:contA is weight-blind).
- Faithfulness of R (eq:Gammaenergy) involves only Gamma poles, so it holds for DH.

So an argument in 𝒞 that proves R_LF = 0 at first contact also proves it for DH. That gives
F = 0 there, which is a contradiction. **No line of any formulation in 𝒞 fails for DH.** By the
mandatory filter every such formulation is discarded. This includes the two-way quantity of §2
for every Θ.

**Corollary 4.4 (a ≠ Λ).** Keep the comb 1 and replace Λ by a with a*1 ≠ log. Then (Cheb) fails at
the first k with (a*1)(k) ≠ log k. By R162_204, however, the regularised quantities do not see a
finite modification. The equivalent description: a = Λ_g for g = exp Σa(n)n^{−s}/log n, so
Lemma 4.1(i) holds for the comb a_g, and the failing line is **(Pois)_g**, since g has no
functional equation. Either way the defect enters linearly (R162_205), so it cannot change a
quadratic sign.

**4.3 Why D4's DH clause does not help.** R160_D4_R2 Thm 2.2 is right that (Z2) *against 1_ℕ*
fails for DH. Inside a PC argument, though, the comb is carried symbolically as S_N. Every step
is valid for S_N^f. The identification a_f = 1 is used only as a *name*. A DH-failing line must
therefore use a property of the comb 1_ℕ, or of Λ, that is not preserved by the substitution
(1,Λ) ↦ (a_f,Λ_f). No identity has this property. Properties that do: a_f ≥ 0 (false for DH),
Λ_f ≥ 0 (false for DH), supp Λ_f ⊂ prime powers (false for DH), and complete multiplicativity of
the comb.

## 5. Residual: the only surviving restatement of O-D4.1 (OPEN)

**(O-D4.1′)** In the same quadratic step as (Pois), use the **inequality** Λ ≥ 0, or the Euler
factorisation ζ_P = Π_{p≤P}(1−p^{−s})^{−1}, rather than the identity Λ*1 = log.

Formal F-tests:
- F3: this passes by §4.3, because Λ_DH changes sign.
- F4: it passes provided the inequality multiplies a square.
- F1: it requires a pairing ⟨F, ΘF⟩ ≥ 0 with Θ = S_N^*S_N-type (§2).

There is one known obstruction, recorded as a warning and not a proof. In the Weil form, Λ ≥ 0
enters only through −⟨(L+L^*)F,F⟩, which is the term *against* positivity. An oriented use has to
turn Λ ≥ 0 into an upper bound on the collar pairing ⟨A_MF,(1−P)S_N^*S_NF⟩ that is strictly
better than R162_202's ESB. R162_403 NG-F1 shows that for the smooth comb, multiplicativity alone
cancels. Positivity of Λ against an oriented (causal) half-line Hankel is the one combination not
yet tested in the corpus. It is handed to round 7 as the only survivor.

## 6. Summary table

| # | statement | label |
|---|---|---|
| (2.3) | two-way identity for 𝔅_Θ at an eigenvector; F1 needs ⟨F,ΠPΘF⟩ ≥ 0 | PROVED |
| Thm 3.1 | Gamma-lattice coefficient of Poisson + Chebyshev = [f′−(f′/f)f](−2m) = 0 | PROVED |
| Cor 3.2 | R162_305 and R162_401 are one cancellation | PROVED |
| Thm 4.2 | transport of the class 𝒞 to any degree-1 f with FE | PROVED |
| Cor 4.3 | DH line empty; O-D4.1 (identity form) discarded | NO-GO (PROVED) |
| Cor 4.4 | a ≠ Λ: failing line is Poisson for the induced comb; the defect is linear | PROVED |
| §5 | O-D4.1′: Λ ≥ 0 / Euler factorisation in the Poisson step | OPEN |
