# PROOF_L_SHARP_X_001 — Theorem B: single-cell dilate evaluation of the universal exterior form 𝔔

Phase 199, This is pen-and-paper work. One numerical check was run in the scratchpad and is not
stored; it is labelled NUMÉRICO and used only to check the proof. No
equivalence of any kind is invoked, no zero is used, and

**Outcome in one line.** BRIDGE_001's Theorem B is **PROVED**, in a corrected and sharper form.
**[ AUDIT_8 correction: PROVED confirmed after audit (AUDIT_L_SHARP_8), with two constant
repairs (gap 2δ/N in Lemma X.1, K₂ with coefficients 6, 2, 12 in Lemma X.5a/Theorem X.5). Neither repair changes
the order O(ν₀⁻¹) or the polylog dependence on N. Cor X.7(i) holds only in the single-cell high-frequency
cone, with no contradiction with the negativity of 0.85Λ (distinct data classes; see §5). Added constraint 20
(single-cell data do not test cross-interference or resonances). See AUDIT_L_SHARP_8.md.]**
- For data supported in one integer cell (N+δ, N+1−δ) with N ≥ 2, the dilates of Ψ̌_ρ have **pairwise disjoint supports**.
  So:
  - the prime part of 𝔔 is *exactly* the scalar −2H₁(N)‖ρ‖² (Lemma X.3; the a_n ≡ 1 input, through Λ∗1 = log);
  - the cross classes m ≠ n are purely archimedean, with a smooth kernel;
  - there are **no resonances**, so the hypothesis "tφ′ increasing" is not needed.
- For chirps ρ = a e^{iφ} with φ′ ≥ ν₀:
  - 𝔔[ρ] = ∫w(t,φ′(t))|a|²dt + E, with |E| ≤ C(a,φ,N,δ)/ν₀ and C explicit (Thm X.5);
  - the log² cancellation is Lemma X.4: H_N log N − 2H₁(N) = F(N) ∈ [0, γ log N + 1];
  - hence 𝔔[ρ] ≥ (H_N log(ν₀/2π) − C/ν₀)‖a‖² > 0 (Cor X.6).
- With weight c on the prime part (cΛ convention of BRIDGE §7):
  - c ≤ 1: positivity persists, with a larger weight;
  - **every c > 1:** Theorem B produces an explicit negative direction of 𝔔^c (Cor X.7, PROVED). This is the first
    *proved* place where the exterior form separates Λ from cΛ (c > 1) on an explicit data family.
- Row D OPEN. L′♯ OPEN.

## 0. Corpus / index check, and why this is not a retry
**Searched:**
- ROUTES-TRIED-INDEX README l.449–471 (phase 199, incl. BRIDGE_001, SYNTHESIS_MECHANISM_001);
- 04_PHASES ("high frequency", "Lemma 4.1", "chirp");
- A_001 Lemma 4.1 (high-frequency coercivity, comb-generic);
- F_001 Prop F.5 (shallow data = window form);
- E_001 Thm E.1/E.2/Cor E.3;
- J_001 Prop J.1;
- AUDIT_L_SHARP_7 (constraint 19);
- Paper 46 eq:Aform / thm:A (Lévy form; killing term in E §1).

**Why it is not a retry.**
- This is the first theorem *requested* by BRIDGE_001 §8, not a new route.
- The relation to A Lemma 4.1 is explicit (Rem X.9).
  - Lemma 4.1 bounds the comb by its total mass. It is comb-generic, and its threshold is frequency e^{O(√N)}.
  - Here the comb is evaluated *exactly* on single-cell data (Lemma X.3). The threshold becomes polynomial/logarithmic in
    N, and the result is Λ-sensitive (Cor X.7).
- The index records no exact evaluation of the comb on dilate-disjoint data, and no c-falsifier for 𝔔.

## 1. Setting (definitions checked against F_001 Prop F.0, E_001 §1, Cor E.3, Paper 46 eq:Aform)
- For ρ on (1,∞), set ρ̃(x) := e^{x/2}ρ(e^x).
- Ψ̌_ρ(y) := e^{y/2}Σ_{n≥1}ρ(ne^y) for y > 0, and Ψ̌_ρ := 0 for y ≤ 0.
- 𝔔[ρ] := 𝒲[Ψ̌_ρ] (F.0), with
  𝔔[ρ] = 𝒜[Ψ̌] − 2Re⟨Ψ̌,Ψ̌_log⟩ + 2Re(A\bar B)   (Cor E.3, Hermitian extension; a = 0, λ = 1).
  Here:
  - 𝒜[Ψ] = (1/2π)∫Θ_∞(τ)|Ψ̂(τ)|²dτ = b_∞‖Ψ‖² + ½∫∫_{ℝ²}|Ψ(x)−Ψ(x′)|²ν(x−x′)dxdx′. This is the full-line Lévy form of the
    zero-extended function, killing term included (E §1).
  - Ψ̂(τ) = ∫Ψe^{−iτx}dx.
  - Θ_∞(τ) = Re ψ(¼+iτ/2) − log π and b_∞ = Θ_∞(0) = −5.37218.
  - ν(s) = e^{−|s|/2}/(1−e^{−2|s|}).
  - Ψ̌_log(y) = e^{y/2}Σ(log n)ρ(ne^y).
  - A = ∫_0^∞Ψ̌e^{−y/2} and B = ∫_0^∞Ψ̌e^{y/2}.
- For complex ρ, the Hermitian extension is 𝔔[ρ] = 𝔔[Re ρ] + 𝔔[Im ρ].
- H_N = Σ_{n≤N}1/n and H₁(N) = Σ_{n≤N}(log n)/n.
- w(t,ν) := H(t)log(νt/2π) − 2H₁(t), the phase-space weight of B.0(ii).
- **Hypothesis (S) (single cell):** N ≥ 2, δ ∈ (0,¼), supp ρ ⊂ [N+δ, N+1−δ], and ρ̃ ∈ H¹.
- Put u := ρ̃, ℓ_n := log n and u_n(y) := u(y+ℓ_n). Then u_n is supported in J_n := [log((N+δ)/n), log((N+1−δ)/n)].

## 2. Exact structure on single-cell data (PROVED)

**Lemma X.1 (disjoint dilates).** Assume (S).
- (i) For n ≤ N, J_n ⊂ (0,∞). For n ≥ N+1, J_n ⊂ (−∞,0). Hence Ψ̌_ρ = Σ_{n≤N}n^{−½}u_n, with **no truncation inside any
  support**.
- (ii) For 1 ≤ m < n ≤ N, J_m and J_n are disjoint, and the gap satisfies
  g_{mn} ≥ log(n/m) − log((N+1−δ)/(N+δ)).
  In particular, g_{m,m+1} ≥ δ/N, and g_{m,m+k} ≥ k/(2N) for k ≥ 2.

*Proof.*
- (i) For n ≤ N, (N+δ)/n > 1. For n ≥ N+1, (N+1−δ)/n < 1.
- (ii) The gap is log((N+δ)/m) − log((N+1−δ)/n).
  - For n = m+k, log(n/m) ≥ k/n ≥ k/N, and log((N+1−δ)/(N+δ)) ≤ (1−2δ)/N. So g ≥ (k−1+2δ)/N. This gives k/(2N) for k ≥ 2.
  - For k = 1 one needs the exact computation. Let m = N−1 (the worst case, since (m+1)/m decreases). Then
    N(N+δ) − (N−1)(N+1−δ) = 1 + 2δN − δ ≥ 2δN, and (N−1)(N+1−δ) < N². So g ≥ log(1+2δ/N) ≥ δ/N.

  **[ AUDIT_8 correction: the bound used in the rest of the memo is g_{m,m+1} ≥ 2δ/N, not δ/N. The missing line:
  using log(1+x) ≥ x/(1+x), g ≥ (2δN+1−δ)/(N(N+δ)) ≥ 2δ/N ⟺ 1−δ ≥ 2δ², true for δ < ¼. Add this inequality
  here. Also: N ≥ 1 suffices for the disjunction (i)-(ii); N ≥ 2 is only needed for cross classes to exist
  (at least one pair m < n ≤ N) and for the worst case m = N−1 to be defined. Bound check (scratch):
  min gap/(2δ/N) ≥ 1.016 for N ≤ 100, δ ≤ 0.24.]**
□

**Lemma X.2 (exact decomposition).** Under (S),
  𝔔[ρ] = H_N·⟨Θ_∞(D)u,u⟩ − 2H₁(N)‖ρ‖² + 𝔛[ρ] + 2Re(A\bar B),
where:
- 𝔛[ρ] := −Σ_{m≠n≤N}(mn)^{−½}∫∫u_m(y)\overline{u_n(y′)}ν(y−y′)dydy′, the cross-dilate classes;
- A = N∫ρ(t)t^{−1}dt and B = H_N∫ρ(t)dt;
- ‖ρ‖² = ∫|ρ(t)|²dt = ‖u‖²_{L²(dx)}.

*Proof.*
- **Archimedean part.** By Lemma X.1(i), 𝒜[Ψ̌] = Σ_{m,n≤N}(mn)^{−½}𝒜(u_m,u_n).
  - Diagonal terms: 𝒜(u_n,u_n) = 𝒜(u,u) = ⟨Θ_∞(D)u,u⟩, because Θ_∞(D) commutes with translations. Their sum is H_N⟨Θ_∞(D)u,u⟩.
  - Off-diagonal terms: the supports are disjoint, so b_∞⟨u_m,u_n⟩ = 0. In the polarised Lévy form,
    ½∫∫(u_m(x)−u_m(x′))\overline{(u_n(x)−u_n(x′))}ν, the terms u_m(x)\bar u_n(x) vanish, and the two mixed terms are
    equal (ν is even). This gives −∫∫u_m(x)\bar u_n(x′)ν(x−x′).
  - The integral converges absolutely because ν is bounded on |s| ≥ g_{mn} > 0.
- **Prime part (Lemma X.3 below).** It equals −2H₁(N)‖ρ‖².
- **Pole.**
  - A = Σ_{n≤N}n^{−½}∫u_n e^{−y/2} = Σ_n∫u e^{−x/2}dx = N∫ρ(t)t^{−1}dt.
  - B = Σ_n n^{−1}∫u e^{x/2}dx = H_N∫ρ dt.
□

**Lemma X.3 (the comb on single-cell data; the a_n ≡ 1 input).** Assume (S). Let any comb Σ_q c_q(δ_{log q}+δ_{−log q})
with c_q = w(q)q^{−½} replace the prime comb in the full-line form. Then its contribution to 𝒲[Ψ̌_ρ] is exactly
  −2Σ_q w(q)q^{−1}H(N/q)·‖ρ‖² = −2‖ρ‖²·Σ_{n≤N}(w∗1)(n)/n.
For w = Λ (Λ∗1 = log) this is **−2H₁(N)‖ρ‖²**. It is independent of the phase of ρ.

*Proof.*
- Ψ̌(y+log q) = Σ_{l}l^{−½}u(y+log(lq)).
- By Lemma X.1, ∫u_m\bar u_{n} = 0 for m ≠ n, and ∫u_n\bar u_n = ‖u‖² for n ≤ N.
- Hence ⟨Ψ̌,S_{−log q}Ψ̌⟩ = Σ_{m=lq≤N}(m·l)^{−½}‖u‖² = q^{−½}H(N/q)‖u‖². The left shift gives the conjugate of the same number.
- Summing gives −2Σ_q c_q q^{−½}H(N/q)‖u‖².
- Finally, Σ_q w(q)q^{−1}Σ_{l≤N/q}l^{−1} = Σ_{n≤N}n^{−1}Σ_{q|n}w(q).
- This agrees with E.2's collapse: Σ_{m,n}(mn)^{−½}log(mn)I(m,n) with I(m,n) = δ_{mn}‖u‖².
□

**Lemma X.4 (log² cancellation; PROVED, elementary).** For N ≥ 1 and t ∈ [N, N+1):
  H_N log t − 2H₁(N) = F(N) + H_N log(t/N),  with 0 ≤ F(N) := H_N log N − 2H₁(N) ≤ γ log N + 1.
Hence w(t,ν) = H_N log(ν/2π) + F(N) + H_N log(t/N) ≥ H_N log(ν/2π).

*Proof.*
- **Lower bound.** F ≥ 0 is the key inequality of BRIDGE Lemma B.0, proved by induction: F(1) = 0 and
  F(N+1) − F(N) = H_N log(1+1/N) − log(N+1)/(N+1) ≥ 0.
- **Upper bound.** Use H_N ≤ log N + γ + 1/(2N), and H₁(N) ≥ ½log²N + γ₁, where γ₁ = −0.0728 is the Stieltjes constant
  (CITED). The second bound holds because, for N ≥ 3, the difference H₁(N) − ½log²N decreases to γ₁: its increment
  f(N+1) − ∫_N^{N+1}f is ≤ 0, where f = (log x)/x decreases on [e,∞). For N = 1, 2 the inequality is checked directly.
  Then F(N) ≤ γ log N + (log N)/(2N) − 2γ₁ ≤ γ log N + 1.
  (NUMÉRICO check: max_N [F(N) − γ log N] = 0.146.)
□

**Reading (where the a_n ≡ 1 input enters).**
- The archimedean diagonal of the N dilates gives H_N·log(t·φ′/2π). Its "position" part H_N log t ≈ log²N comes from
  Θ_∞ evaluated at the *Mellin* frequency τ = tφ′, which is the dilation by t of the additive frequency φ′.
- The comb gives −2Σ_{n≤N}(Λ∗1)(n)/n = −2H₁(N) ≈ −log²N.
- They cancel to F(N) ≈ γ log N. This holds exactly because Λ∗1 = log and every dilate is counted once with the harmonic
  cut (a_n ≡ 1).
- With a comb w satisfying Σ_{n≤N}(w∗1)(n)/n = ½c·log²N + O(log N), the survivor is (1−c)log²N + O(log N).

## 3. The oscillatory log-symbol lemma (PROVED)

**Lemma X.5a.** Let u = Ae^{iΦ}, with A ∈ C_c²(ℝ) and Φ ∈ C³ real.
- **Hypotheses.** Φ′ ≥ Ω on supp A, with Ω ≥ 4π.
- **Constants.**
  - K₀ := ‖A′‖₂ + ‖AΦ″/Φ′‖₂;
  - K₁ := ‖A′‖₁ + 2‖AΦ″/Φ′‖₁;
  - K₂ := ‖A″‖₁ + 4‖A′Φ″/Φ′‖₁ + 2‖AΦ‴/Φ′‖₁ + 8‖AΦ″²/Φ′²‖₁.
  **[ AUDIT_8 correction: K₂ is undercounted. With g = Φ′−τ, L²A = A″/g² − 3A′Φ″/g³ − AΦ‴/g³ + 3AΦ″²/g⁴
  (verified by algebra/sympy), and with g ≥ Ω/2+σ, g ≥ Φ′/2, the correct comparison is
  g^{−j} ≤ (2/Φ′)^{j−2}(Ω/2+σ)^{−2} (not just one power, as the text below states). The corrected constant is
  K₂ := ‖A″‖₁ + 6‖A′Φ″/Φ′‖₁ + 2‖AΦ‴/Φ′‖₁ + 12‖AΦ″²/Φ′²‖₁ (coeficientes 6, 2, 12, no 4, 2, 8). No cambia el orden
  O(ν₀⁻¹) of the error or the polylog dependence on N. Also, K₂ is independent of ν in the semiclassical family (every
  term is scale-invariant); the statement "K₂/ν ν-independent" below is incorrect but harmless,
  because the true statement is stronger. C_Θ = 0.18727 recomputed and verified (NUMERICAL).]**
- **Conclusion.**
  |⟨Θ_∞(D)u,u⟩ − ∫log(Φ′(x)/2π)|A(x)|²dx| ≤ (2log2/Ω)K₀‖A‖₂ + 4C_Θ‖A‖₂²/Ω² + 4log2·K₁K₂/(πΩ²) + K₂²(7+2log(1+Ω))/(2Ω³),
  where C_Θ := sup_{|τ|≥1}τ²|Θ_∞(τ) − log(|τ|/2π)| < ∞.
  - Stirling: CITED (DLMF 5.11.2 with the remainder bounds of 5.11(ii)).
  - NUMÉRICO check: C_Θ = 0.187.
  - Also |Θ_∞(τ)| ≤ 5.38 + log(1+|τ|) (NUMÉRICO check, sup at τ = 0).

*Proof.*

*(a) Non-stationary bound.* For τ ≤ Ω/2, write σ := Ω/2 − τ ≥ 0. On supp A one has Φ′ − τ ≥ Φ′/2 and Φ′ − τ ≥ Ω/2 + σ.
- Two integrations by parts in û(τ) = ∫Ae^{i(Φ−τx)} give |û(τ)| ≤ K₂/(Ω/2+σ)². Here
  L f := (f/(Φ′−τ))′, and |L²A| is bounded termwise using (Φ′−τ)^{−j} ≤ 2^{j−1}Φ′^{−(j−1)}(Ω/2+σ)^{−1}.
- One integration gives |û(τ)| ≤ K₁/(Ω/2+σ).

*(b) Split.* Put τ̃ := max(τ,Ω/2) and D̃ := τ̃(D) ≥ Ω/2 > 0. Then
  ⟨Θ_∞(D)u,u⟩ − ⟨log(D̃/2π)u,u⟩ = (1/2π)∫_{τ>Ω/2}ε(τ)|û|² + (1/2π)∫_{τ≤Ω/2}(Θ_∞(τ) − log(Ω/4π))|û|².
- The first term is ≤ 4C_Θ‖A‖²/Ω².
- By (a), the second term is ≤ (1/2π)K₂²∫_0^∞(5.38+2log(1+Ω/2+σ)+1)(Ω/2+σ)^{−4}dσ ≤ K₂²(7+2log(1+Ω))/(2Ω³).

*(c) Resolvent comparison.* Let M := multiplication by max(Φ′,Ω), which is Φ′ on supp A. For positive self-adjoint
X ≥ c > 0, log X = ∫_0^∞[(1+s)^{−1} − (X+s)^{−1}]ds (spectral theorem). So
  ⟨(log D̃ − log M)u,u⟩ = ∫_0^∞⟨(D̃+s)^{−1}(D̃−M)(M+s)^{−1}u,u⟩ds.
- Put v_s := (M+s)^{−1}u = A_s e^{iΦ}, with A_s = A/(Φ′+s). This lies in H¹, the domain of D̃.
- Then (D̃−M)v_s = −iA_s′e^{iΦ} + (Ω/2−D)_+v_s.
- **First piece.** Since (Φ′+s)² ≥ Φ′(Ω+s), we have ‖A_s′‖₂ ≤ K₀/(Ω+s), and ‖(D̃+s)^{−1}‖ ≤ (Ω/2+s)^{−1}. This contributes
  ≤ K₀‖A‖₂∫_0^∞ds/((Ω/2+s)(Ω+s)) = (2log2/Ω)K₀‖A‖₂.
- **Second piece.** It is supported in τ ≤ Ω/2. By (a) applied to A_s (K₁(A_s) ≤ 2K₁/(Ω+s)) and to A, its modulus is
  ≤ (1/2π)(Ω/2+s)^{−1}∫_0^∞σ·(2K₁/((Ω+s)(Ω/2+σ)))·K₂(Ω/2+σ)^{−2}dσ ≤ (2K₁K₂/(πΩ))(Ω/2+s)^{−1}(Ω+s)^{−1}.
  Integrating in s gives ≤ 4log2·K₁K₂/(πΩ²).

Since ⟨log(M/2π)u,u⟩ = ∫log(Φ′/2π)|A|², the lemma follows. □

## 4. Theorem B (PROVED)

**Theorem X.5 (Theorem B, single-cell chirp evaluation).**
- **Hypotheses.** Assume (S), and let ρ(t) = a(t)e^{iφ(t)} with:
  - a ∈ C_c²((N+δ, N+1−δ));
  - φ ∈ C³ real;
  - φ′ ≥ ν₀ on supp a, with Nν₀ ≥ 4π.
- **Constants.** In the variables x = log t, put A(x) = e^{x/2}a(e^x) and Φ(x) = φ(e^x). Then Φ′ = tφ′ ≥ Ω := (N+δ)ν₀.
  Let K₀, K₁, K₂ be as in Lemma X.5a. In t-variables:
  - K₀ = ‖½a + ta′‖ + ‖a·t(log tφ′)′‖;
  - K₁ ≤ 2N^{−½}K₀.
- **Conclusion.**
  **𝔔[ρ] = ∫ w(t,φ′(t))|a(t)|²dt + E,** with |E| ≤ E_arch + E_cross + E_pole, where:
  - E_arch := H_N·[(2log2/Ω)K₀‖a‖ + 4C_Θ‖a‖²/Ω² + 4log2K₁K₂/(πΩ²) + K₂²(7+2log(1+Ω))/(2Ω³)];
  - E_cross := (2H_N/ν₀)[K₀‖a‖(1/(2δ) + 2log N)/N + ‖a‖²(3/(4δ²) + 8)];
  - E_pole := 2√2·H_N(K₀+½‖a‖)²/(Nν₀)².
- **Order of the error.** E = O(ν₀^{−1}).
- **Semiclassical family.** For a fixed profile a and φ = ν·ϕ with ϕ′ ≥ 1 fixed, K₀ and K₂/ν are ν-independent
  (Φ″/Φ′ is scale-free), so E ≤ C(a,ϕ,N,δ)/ν.
- **No monotonicity needed.** The hypothesis "tφ′ increasing" of BRIDGE is **not needed**.

*Proof.*
- **Decomposition.** By Lemma X.2,
  𝔔[ρ] − [H_N⟨Θ_∞(D)u,u⟩ − 2H₁(N)‖a‖²] = 𝔛[ρ] + 2Re(A_p\bar B_p).
- **Diagonal.** Lemma X.5a, with ‖A‖₂ = ‖a‖, gives
  H_N⟨Θ_∞(D)u,u⟩ = H_N∫log(tφ′/2π)|a|²dt + O(E_arch).
  - Here H(t) = H_N on the support, so H_N log(tφ′/2π) − 2H₁(N) = w(t,φ′(t)) exactly.
  - (∫|A|²dx = ∫|a|²dt, and log Φ′(x) = log(tφ′(t)).)
- **Cross classes.** Fix m ≠ n. Integrate by parts in y, using e^{iΦ(y+ℓ_m)} = ∂_y e^{iΦ(y+ℓ_m)}/(iΦ′(y+ℓ_m)). The kernel
  ν(y−y′) is C^∞ on J_m × J_n, and the boundary terms vanish since A has compact support. This gives
  |∫∫u_m\bar u_nν| ≤ Ω^{−1}[(‖A′‖₁+‖AΦ″/Φ′‖₁)‖A‖₁·sup_{|s|≥g}ν + ‖A‖₁²·sup_{|s|≥g}|ν′|].
  - **Kernel bounds.** Write ν(s) = 1/f(s) with f(s) = e^{s/2} − e^{−3s/2}. Then f′ ≥ 1 (its minimum is f′(log 3) = 1.155),
    so ν(s) ≤ 1/s. Also |ν′(s)| ≤ 2/s² for s ≤ 1 (f′ ≤ 2 there), and |ν′(s)| ≤ 0.96e^{−s/2} ≤ 3/s² for s ≥ 1.
    (NUMÉRICO check: sup sν = 0.75, sup s²|ν′| = 1.08.)
  - **L¹ norms.** By Cauchy–Schwarz on [N,N+1], with ∫dt/t ≤ 1/N, we get ‖A‖₁ ≤ N^{−½}‖a‖ and
    ‖A′‖₁ + ‖AΦ″/Φ′‖₁ ≤ N^{−½}K₀.
  - **Sum over pairs.** By Lemma X.1(ii) and (mn)^{−½} ≤ m^{−1}:
    - Σ_{m<n}(mn)^{−½}/g_{mn} ≤ H_N·N(1/(2δ)+2log N), from k = 1 (g ≥ 2δ/N) and k ≥ 2 (g ≥ k/(2N));
    - Σ_{m<n}(mn)^{−½}/g_{mn}² ≤ H_N·N²(1/(4δ²) + 4(π²/6−1)).
  - Collecting the two orders (m,n), (n,m) and using Ω ≥ Nν₀ gives E_cross.
- **Pole.** Integrate by parts once in x:
  - |∫ρt^{−1}dt| = |∫Ae^{−x/2}e^{iΦ}dx| ≤ Ω^{−1}∫e^{−x/2}(|A′|+½|A|+|AΦ″/Φ′|) ≤ (K₀+½‖a‖)/(NΩ);
  - likewise |∫ρdt| ≤ √(N+1)(K₀+½‖a‖)/(√N·Ω).
  - Hence |2A_pB_p| ≤ 2N·H_N·√2(K₀+½‖a‖)²/(NΩ²) ≤ E_pole.
□

**Remark X.5b (real chirps).** For ρ_R = a cos φ one has
  𝔔[ρ_R] = ½𝔔[ρ] + ½Re 𝔔^{bil}(ρ,ρ),
where 𝔔^{bil} is the symmetric bilinear form. Every piece of 𝔔^{bil}(ρ,ρ) involves the phase 2Φ (or Φ(y+ℓ_m)+Φ(y′+ℓ_n)),
or pairs û(τ) with û(−τ), which is ≤ K₂(Ω+|τ|)^{−2} by Lemma X.5a(a). The same integrations by parts give
O(log ν₀/ν₀). Hence 𝔔[a cos φ] = ½∫w|a|² + O(log ν₀/ν₀). (PROVED; constants not tracked.)

**NUMÉRICO check (scratchpad, not stored).** Setup:
- direct quadrature of 𝔔 through the exact multiplier 𝔪_N(τ) = Σ_{m,n≤N}(mn)^{−½}cos(τlog(n/m))[Θ_∞(τ) − log mn] plus 2AB;
- bump amplitude on (N+0.1, N+0.9), φ′ = ν₀(1+0.6(t−N)).

| N | ν₀ | 𝔔[ρ] | ∫w\|a\|² |
|---|---|---|---|
| 2 | 20 | 2.7668 | 2.8095 |
| 2 | 60 | 4.4530 | 4.4574 |
| 2 | 180 | 6.10487 | 6.10536 |
| 5 | 20, 60, 180 | errors 0.065, 0.0067, 0.0007 | |

The observed error is ≈ O(ν₀^{−2}), so the O(ν₀^{−1}) bound is conservative. Improving the rate is not proved.

## 5. Corollaries (PROVED)

**Corollary X.6 (a proved positive region of 𝔔).** Under the hypotheses of Theorem X.5:
  𝔔[ρ] ≥ [H_N log(ν₀/2π) + F(N) + H_N log(1+δ/N)]‖a‖² − E ≥ (H_N log(ν₀/2π) − E/‖a‖²)‖a‖².
So 𝔔[ρ] > 0 as soon as H_N log(ν₀/2π)‖a‖² > E.
- **Fixed profile.** For the semiclassical family of Thm X.5 this holds for ν ≥ ν_*(a,ϕ,N,δ). Take for example
  φ′ ≡ ν₀ and a(t) = b(t−N), with b a fixed bump on (δ,1−δ). Then K₀ ≤ (N+1)‖b′‖ + 2‖b‖, and E ≤ C(b,δ)·H_N log(N+1)/ν₀.
  So positivity holds for ν₀ ≥ C′(b,δ)·log(N+2)/log(ν₀/2π), which is **logarithmic in N**.
- **Comparison with the brief.** On the scale ν₀ ≍ 2πμ the bound reads H_N log μ, the analogue of B.0's log 2μ. The brief's
  "log 2μ" itself refers to the ω ∈ (1,2) caustic regime, which single-cell data (N ≥ 2) do not reach.

**Corollary X.7 (c-dependence: Λ-specificity on explicit data).** Let 𝔔^c be 𝔔 with the prime part multiplied by c > 0,
i.e. comb weight w = cΛ in Lemma X.3 (BRIDGE §7 convention; Z unchanged). Then Theorem X.5 holds with
  w^c(t,ν) = H_N log(νt/2π) − 2cH₁(N) = w(t,ν) − 2(c−1)H₁(N).
- **(i) c ≤ 1.** w^c ≥ w ≥ H_N log(ν/2π). Cor X.6 holds verbatim.
  **[ AUDIT_8 correction: this positivity holds only in the single-cell high-frequency cone
  (chirp, φ′ ≥ ν₀ ≥ ν_*(a,φ,N,δ), single cell). There is no contradiction with the negativity of the 0.85Λ falsifier in the
  0.85Λ/2Λ window (AA_001, phase 198): these are distinct data classes. The negative directions of 0.85Λ are
  low-frequency window vectors near the archimedean floor (multi-cell, non-chirp after the F.5 inversion); Theorem B
  says nothing about them. Correct reading: "c ≤ 1: the single-cell high-frequency cone remains
  positive (with larger weight)"; this should not be read as positivity of 𝔔^c in general.]**
- **(ii) c > 1: a proved negative direction.** Take b fixed, φ′ ≡ ν₀ := 2πN^{(c−1)/2}, and N → ∞.
  - By Lemma X.4 and H₁(N) ≥ ½log²N + γ₁, the weight satisfies w^c ≤ H_N·(c−1)/2·log N + γlog N + 1 + H_N log 2 − (c−1)log²N.
    This is ≤ −((c−1)/2 − o(1))log²N.
  - Meanwhile E ≤ C(b,δ)H_N log(N+1)/ν₀ → 0.
  - Hence **𝔔^c[ρ_N] < 0 for all N ≥ N₀(c,b,δ)**.
  - NUMÉRICO check: c = 3, N = 40, ν₀ = 8 gives 𝔔^c = −23.16 against ∫w^c|a|² = −22.67.
- **(iii) Fixed N.** For c > 1 and fixed N, positivity still holds for ν₀ ≥ 2πN^{c−1}e^{O(1)}. **No single chirp family at
  fixed N separates Λ from cΛ.** The separation is the uniformity in N (number of active dilates) at fixed or slowly growing
  ν₀. This is the exact form of BRIDGE §7's "pointwise" caveat, now PROVED on single-cell data.
- **Scope of (ii).** 𝔔^c is the c-twisted universal form, not the exterior form of the cΛ system (whose I1 also changes;
  BRIDGE §7). Cor X.7 is a statement about the Λ-step *inside* 𝔔, not a falsifier of I1.

**Corollary X.8 (comb-genericity map).**
- Lemma X.1, Lemma X.5a, the cross bound and the pole bound are comb-generic: they use no comb.
- The only Λ-input is Lemma X.3 with Λ∗1 = log, together with the counting of dilates with weight n^{−½} (a_n ≡ 1, giving
  H_N and H₁(N)).
- Conductor 1 enters through Θ_∞ ~ log(τ/2π), which fixes the threshold ν₀ > 2π.
- Residue 1 (the pole) is O(ν₀^{−2}) here. **Theorem B does not see the pole.**

## 6. What Theorem B does NOT cover (honest)
1. **Not PW data, not the bottom.** These are C_c² chirps supported in one cell [N+δ, N+1−δ], N ≥ 2. Actual PW tails
   ρ = ĝ|_{(1,∞)}:
   - are spread over all cells and decay like t^{−2};
   - carry jumps at every integer (the dilate truncations);
   - have the extremal mass in ω ∈ (1,2) (N = 1, the caustic regime, excluded).
2. **Equivalent to a window statement.** By F Prop F.5, single-cell data have Ψ̌ supported in (0, log(N+1)). So Theorem B is
   a statement about the *complete window form* at T₀ = ½log(N+1) on high-frequency, dilate-structured data.
   - It is sharper than A Lemma 4.1 (Rem X.9), but it lives in the shallow/window regime.
   - It says nothing about L′♯'s uniformity in μ.
3. **No resonances, no edge — by hypothesis.**
   - The (1,n) resonances of SYNTHESIS §3.3 need data in cells 1 and n simultaneously.
   - Multi-cell data have overlapping dilates (cell m·k against cell k), where the cross classes are oscillatory pairings
     with relative phase Φ(y+ℓ_m) − Φ(y+ℓ_n). That case is **OPEN**. The non-stationary argument of the brief (iii) applies
     there only under the monotone-τ hypothesis, and it is not done here.
   - The edge t = 1, the integer jumps, and the edge channel P3b are excluded.
4. **Gauge.** The projection Π onto the Sonin annulus is not involved. Single-cell chirps are not shown to be Π-invariant,
   and the denominator dist²(ρ,𝒢̄₁) is not addressed.
5. **Constraint 7 is not decided.** BRIDGE §8(v) claimed Theorem B "decides constraint 7 on chirps". It does so only
   trivially: for single-cell data the cross classes are not oscillatory *pairings of overlapping dilates* at all. The real
   test is multi-cell chirps. Correction recorded.
6. **Constants.** The error bound is O(ν₀^{−1}) with a polylog-in-N constant. The data suggest O(ν₀^{−2}). Not optimised.

**Remark X.9 (relation to A Lemma 4.1).** Lemma 4.1 applied to the window T₀ = ½log(N+1):
- It bounds the comb by 2Σ_{q≤N+1}Λ(q)q^{−½} ~ 4√N and needs log-frequency ≥ e^{O(√N)}.
- It is comb-generic, so it is equally true for cΛ, c > 1 — which Cor X.7(ii) shows cannot hold at polylog frequency.
Theorem B replaces the mass bound by the exact comb value (Lemma X.3). The threshold drops to ν₀ ≳ polylog(N), and the
result becomes Λ-sensitive.

## 7. Labels, residuals, do-not-retry
- **PROVED:**
  - Lemma X.1 (disjoint dilates), Lemma X.2 (exact decomposition), Lemma X.3 (comb = −2Σ(w∗1)(n)/n·‖ρ‖²);
  - Lemma X.4 (log² cancellation F(N) ∈ [0, γlog N+1]);
  - Lemma X.5a (oscillatory log-symbol);
  - **Theorem X.5 (Theorem B)** — PROVED (audited, constants corrected: K₂ coefficients 6, 2, 12; gap 2δ/N), Cor X.6,
    Cor X.7 (c ≤ 1 positive only on the high-frequency single-cell cone; every c > 1 negative at N → ∞), Cor X.8.
  **[ AUDIT_8 correction: Rem X.5b (real chirps, "constants not tracked") is reclassified as ARGUED —
  it was not verified in detail by the audit.]**
- **CITED:** Stirling remainder for ψ (C_Θ). **NUMÉRICO (check only):** C_Θ = 0.187; ν bounds; the table in §4; c = 3 example.
- **OPEN:**
  - multi-cell chirps (overlapping dilates, resonances (1,n)) = P2 proper;
  - edge P3b; gauge Π; PW tails; L′♯; (★★).
  - No sign of row D is claimed. Row D OPEN.
- **Corrections to BRIDGE_001:**
  - "tφ′ increasing" is unnecessary for single-cell data;
  - Theorem B does not test constraint 7 or resonances (single-cell dilates are disjoint);
  - the Λ-specificity is in the uniformity in N, not at fixed N.
- **Do not retry:** using single-cell data as evidence about cross-class interference or resonances (they are disjoint by
  Lemma X.1).
